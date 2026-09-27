# -*- coding: utf-8 -*-
"""Native-size inspection of a proposition: render each surface × language as a fluid twin (no fixed viewport class, so
the media queries decide) at the review widths, at device scale 1 and — for the narrowest and the widest — at scale 2.
Writes first-screen and full-page screenshots to out/inspect/ and prints, per render, the document height and any
horizontal overflow. Proof for critique, not authority.

  python3 design/exploration/d1_canvas/inspect_widths.py t4 [--widths 320,360,390,430,768,1024,1280,1440] [--surfaces home,record,reading]
"""
from __future__ import annotations

import argparse
import functools
import http.server
import socket
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "boards"))
from common import load, base_mechanics, font_css  # noqa: E402

OUT = HERE / "out"
LOCAL = OUT / "local"
INSPECT = OUT / "inspect"


def fluid_twin(css: str, body: str, lang: str) -> str:
    d = "rtl" if lang == "ar" else "ltr"
    return (f'<!doctype html><html lang="{lang}" dir="{d}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<style>{font_css("local")}{base_mechanics()}{css}</style></head><body>{body}</body></html>')


def serve(directory: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=str(directory)))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("thesis")
    ap.add_argument("--widths", default="320,360,390,430,768,1024,1280,1440")
    ap.add_argument("--surfaces", default="home,record,reading")
    ap.add_argument("--langs", default="en,ar")
    ap.add_argument("--full", action="store_true", help="also save full-page screenshots")
    args = ap.parse_args()
    import importlib
    mod = importlib.import_module(args.thesis)
    widths = [int(w) for w in args.widths.split(",")]
    INSPECT.mkdir(parents=True, exist_ok=True)
    assert (LOCAL / "assets").exists(), "run build_boards.py first (it copies fonts and the logo into out/local/assets)"
    pages = []
    for surface in args.surfaces.split(","):
        for lang in args.langs.split(","):
            page, shell = load(surface, lang)
            body = mod.COMPOSE[surface](page, shell)
            name = f"{args.thesis.upper()}-{surface}-{lang}-fluid"
            (LOCAL / f"{name}.html").write_text(fluid_twin(mod.CSS, body, lang), encoding="utf-8")
            pages.append((name, surface, lang))
    from playwright.sync_api import sync_playwright
    httpd, base = serve(LOCAL)
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, surface, lang in pages:
            for w in widths:
                scales = [1] + ([2] if w in (widths[0], widths[-1]) else [])
                for dpr in scales:
                    ctx = b.new_context(viewport={"width": w, "height": 900 if w >= 768 else 844}, device_scale_factor=dpr)
                    pg = ctx.new_page()
                    pg.goto(f"{base}/{name}.html", wait_until="load")
                    pg.wait_for_timeout(120)
                    h = pg.evaluate("document.documentElement.scrollHeight")
                    over = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
                    # the widest element, if anything overflows
                    culprit = pg.evaluate("""() => { const cw=document.documentElement.clientWidth; let worst=null;
                        for (const el of document.querySelectorAll('body *')) { const r=el.getBoundingClientRect();
                          if (r.right>cw+0.5 || r.left<-0.5) { const o=Math.max(r.right-cw, -r.left); if(!worst||o>worst.o) worst={o, tag:el.tagName.toLowerCase(), cls:el.className&&el.className.toString().slice(0,60)} } }
                        return worst }""")
                    tag = f"{name}@{w}" + (f"x{dpr}" if dpr != 1 else "")
                    pg.screenshot(path=str(INSPECT / f"{tag}.png"))
                    if args.full:
                        pg.screenshot(path=str(INSPECT / f"{tag}-full.png"), full_page=True)
                    rows.append((tag, int(h), over, culprit))
                    ctx.close()
        b.close()
    httpd.shutdown()
    bad = 0
    for tag, h, over, culprit in rows:
        flag = "" if (over <= 0 and not culprit) else f"  <-- overflow {over} {culprit}"
        bad += bool(flag)
        print(f"{tag:36s} height={h:6d}{flag}")
    print(f"{len(rows)} renders; {bad} with horizontal overflow")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
