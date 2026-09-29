#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EAD-09: the governed social images, rasterised from the design's own templates.

  python3 scripts/social_images.py            # regenerate every image (needs Chromium)
  python3 scripts/social_images.py --check    # standard library only: is every image present and current?

`scripts/yfie/frames.py` builds one 1200 x 630 social template per page and language, filled only with governed text
(`design/08_ASSET_MAP.md` §4). This turns each into the PNG a platform shows beside a shared link, and the build copies
them into `dist/assets/social/` so that `og:image` can be emitted at all.

**Why they are generated here and not inside `scripts/build.py`.** Rasterising needs a browser, and the build must stay
standard library only and finish in seconds: it runs inside every Master transaction and in the gates job, which has no
Chromium. So the images are build *inputs*, regenerated deliberately by this command and committed with everything else
the repository publishes — the same promise `dist/` makes, that the reviewed bytes are the served bytes.

**How staleness is caught without a browser.** The template is pure Python, so `--check` rebuilds every frame's HTML and
compares its SHA-256 with the one recorded in `INDEX.json` when the image was made. A governed string changing anywhere
on a page therefore fails the check with the routes that need regenerating — deterministically, in a second, with no
rendering. Comparing rendered bytes instead would make a Chromium version bump look like a content change.
"""
from __future__ import annotations

import functools
import hashlib
import http.server
import json
import socketserver
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site-src" / "assets" / "social"
INDEX = OUT / "INDEX.json"
sys.path.insert(0, str(ROOT / "scripts"))

WIDTH, HEIGHT = 1200, 630


def frame_name(route: str, lang: str) -> str:
    return (route.strip("/").replace("/", "_") or "home") + f"__{lang}"


def frames() -> dict[str, str]:
    """Every social frame's HTML, keyed by `<route-slug>__<lang>`. Pure Python: no browser, no built site."""
    from yfie import content as C, frames as F
    content = C.load()
    out = {}
    for lang in ("ar", "en"):
        for route in content.routes():
            out[frame_name(route, lang)] = F.social_document(content.page(route, lang), content.shell(lang, route), route)
    return out


def check() -> int:
    if not INDEX.exists():
        print("SOCIAL IMAGES STALE: no site-src/assets/social/INDEX.json; run python3 scripts/social_images.py")
        return 1
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    recorded = index.get("images") or {}
    current = {k: hashlib.sha256(v.encode("utf-8")).hexdigest() for k, v in frames().items()}
    missing = sorted(k for k in current if k not in recorded)
    extra = sorted(k for k in recorded if k not in current)
    stale = sorted(k for k, h in current.items() if k in recorded and recorded[k].get("frame_sha256") != h)
    absent = sorted(k for k in recorded if not (OUT / f"{k}.png").exists())
    if missing or extra or stale or absent:
        print("SOCIAL IMAGES STALE: run python3 scripts/social_images.py and commit")
        for label, rows in (("no image for", missing), ("image for a route that no longer exists", extra),
                            ("governed text changed since the image was made", stale), ("recorded but the file is gone", absent)):
            for k in rows[:10]:
                print(f"  {label}: {k}")
            if len(rows) > 10:
                print(f"  … and {len(rows) - 10} more {label}")
        return 1
    print(f"SOCIAL IMAGES CURRENT: {len(recorded)} images, 1200x630, one per route and language")
    return 0


def serve(directory: Path):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):     # 286 frames x 5 assets is not output anyone reads
            pass

    class Quiet(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, request, client_address):   # a page closed mid-request is not an error
            pass

    handler = functools.partial(Handler, directory=str(directory))
    httpd = Quiet(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1]


def generate() -> int:
    import shutil
    import tempfile
    from playwright.sync_api import sync_playwright

    from yfie import theme

    built = frames()
    with tempfile.TemporaryDirectory(prefix="yfie-social-") as tmp:
        stage = Path(tmp)
        (stage / "assets").mkdir()
        (stage / "assets" / "yfie.css").write_text(theme.FONT_FACES + "\n" + theme.CSS + "\n" + theme.CSS_D2 + "\n" + theme.CSS_D6, encoding="utf-8")
        shutil.copy2(ROOT / "site-src/assets/CauseWay_Master_Logo.png", stage / "assets/CauseWay_Master_Logo.png")
        import build as B   # the one list of the faces the stylesheet declares
        for folder, names in B.FONT_FILES.items():
            (stage / "assets/fonts" / folder).mkdir(parents=True)
            for name in names:
                shutil.copy2(ROOT / "vendor/fonts" / folder / name, stage / "assets/fonts" / folder / name)
        for key, html in built.items():
            (stage / f"{key}.html").write_text(html, encoding="utf-8")

        httpd, port = serve(stage)
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                ctx = browser.new_context(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=1)
                page = ctx.new_page()
                for i, key in enumerate(sorted(built), 1):
                    page.goto(f"http://127.0.0.1:{port}/{key}.html", wait_until="load")
                    page.wait_for_timeout(120)   # let the shipped faces settle before the shot
                    page.screenshot(path=str(OUT / f"{key}.png"))
                    if i % 50 == 0:
                        print(f"  {i} of {len(built)}")
                browser.close()
        finally:
            httpd.shutdown()

    index = {
        "schema": "YFIE_SOCIAL_IMAGES/1.0",
        "what": f"One {WIDTH}x{HEIGHT} PNG per route and language, rasterised from the governed social template "
                "(scripts/yfie/frames.py social_document). Regenerate with python3 scripts/social_images.py.",
        "rule": "frame_sha256 is the SHA-256 of the template's HTML at the time the image was made. --check rebuilds "
                "the templates and compares, so a governed text change is caught without rendering anything.",
        "width": WIDTH, "height": HEIGHT,
        "images": {k: {"frame_sha256": hashlib.sha256(v.encode("utf-8")).hexdigest()} for k, v in sorted(built.items())},
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    total = sum(p.stat().st_size for p in OUT.glob("*.png"))
    print(f"SOCIAL IMAGES WRITTEN: {len(built)} PNG ({total / 1024 / 1024:.1f} MB) in {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(check() if "--check" in sys.argv else generate())
