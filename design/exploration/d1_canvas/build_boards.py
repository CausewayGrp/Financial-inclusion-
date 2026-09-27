# -*- coding: utf-8 -*-
"""Build the D1 canvas: for every thesis × surface × language × size, compose the board, render its plain twin to
measure height (and to screenshot for critique), then write the canvas artboard and the index.

  python3 design/exploration/d1_canvas/build_boards.py [t1,t2,t3,t4]   # after: python3 design/reference/build.py --renderer neutral
"""
from __future__ import annotations

import datetime
import functools
import http.server
import json
import socket
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "boards"))
from common import load, twin_html, board_html, SIZES  # noqa: E402
import t1, t2, t3, t4  # noqa: E402

THESES = {"t1": t1, "t2": t2, "t3": t3, "t4": t4}
SURFACES = ["home", "record", "reading"]
LANGS = ["en", "ar"]
ROOT = HERE.parents[2]  # repository root
OUT = HERE / "out"  # git-ignored
LOCAL = OUT / "local"
PROJECT = OUT / "project" / "project"
SHOTS = OUT / "shots"


def serve(directory: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=str(directory)))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


def main() -> int:
    which = sys.argv[1].split(",") if len(sys.argv) > 1 else list(THESES)
    LOCAL.mkdir(exist_ok=True); PROJECT.mkdir(parents=True, exist_ok=True); SHOTS.mkdir(exist_ok=True)
    # assets for the twins
    assets = LOCAL / "assets"
    if not assets.exists():
        import shutil
        assets.mkdir()
        shutil.copy2(ROOT / "site-src/assets/CauseWay_Master_Logo.png", assets / "CauseWay_Master_Logo.png")
        (assets / "fonts").mkdir()
        for folder in ("ibm-plex-sans", "ibm-plex-sans-arabic"):
            shutil.copytree(ROOT / "vendor/fonts" / folder, assets / "fonts" / folder)
    boards = []
    for key in which:
        mod = THESES[key]
        for surface in SURFACES:
            for lang in LANGS:
                page, shell = load(surface, lang)
                body = mod.COMPOSE[surface](page, shell)
                for size, width in SIZES.items():
                    name = f"{key.upper()}-{surface}-{lang}-{size}"
                    (LOCAL / f"{name}.html").write_text(twin_html(mod.CSS, body, lang, size, width), encoding="utf-8")
                    boards.append({"name": name, "key": key, "surface": surface, "lang": lang, "size": size, "width": width, "css": mod.CSS, "body": body, "title": f"{mod.NAME} · {surface} · {lang.upper()} · {width}"})
    # measure heights and screenshot
    from playwright.sync_api import sync_playwright
    httpd, base = serve(LOCAL)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for bd in boards:
            ctx = b.new_context(viewport={"width": bd["width"], "height": 900}, device_scale_factor=1)
            pg = ctx.new_page()
            pg.goto(f"{base}/{bd['name']}.html", wait_until="load")
            pg.wait_for_timeout(150)
            h = pg.evaluate("document.documentElement.scrollHeight")
            over = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
            bd["height"] = int(h) + 8
            bd["overflow"] = over
            pg.screenshot(path=str(SHOTS / f"{bd['name']}.png"), full_page=True)
            ctx.close()
        b.close()
    httpd.shutdown()
    # canvas files
    index_path = PROJECT / "canvas.json"
    existing = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else None
    idx = existing or {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
                       "title": "YFIE D1 Thesis Exploration", "launch": {"view": "canvas"}, "pages": [], "boards": {}, "order": [], "notes": {}, "designSystems": []}
    y = 0
    gap_x, gap_y = 80, 120
    order = []
    for key in list(THESES):
        row = [bd for bd in boards if bd["key"] == key]
        if not row:
            continue
        idx["notes"][f"row-{key}"] = {"x": 0, "y": y - 300, "text": THESES[key].NAME + " — " + {"t1": "the evidence record as the organising object; the apparatus visible (manuscript page)",
                                                                                              "t2": "reading-first; the proposition leads; evidence discloses in place (image-free control)",
                                                                                              "t3": "the evidence system made spatial; strata and trail (built form)",
                                                                                              "t4": "second generation: an instrument that answers questions and states what it cannot answer (clock-first objects, seven questions, boundary voice, verification spine)"}[key], "kind": "title1", "maxW": 9000}
        x = 0
        row_h = 0
        for bd in sorted(row, key=lambda z: (z["size"] != "d", SURFACES.index(z["surface"]), z["lang"])):
            h = min(bd["height"], 8000)
            fname = f"{bd['name']}.dc.html"
            entry = {"x": x, "y": y, "w": bd["width"], "h": h, "title": bd["title"]}
            if bd["height"] > 8000:
                entry["expand"] = "fill"
            idx["boards"][fname] = entry
            order.append(fname)
            (PROJECT / fname).write_text(board_html(bd["css"], bd["body"], bd["lang"], bd["size"], bd["width"], bd["height"], bd["title"]), encoding="utf-8")
            x += bd["width"] + gap_x
            row_h = max(row_h, h)
        y += row_h + gap_y + 300
    idx["order"] = order
    index_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    for bd in boards:
        print(f"{bd['name']:24s} height={bd['height']:5d} overflow={bd['overflow']}")
    print(f"{len(boards)} boards; index at {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
