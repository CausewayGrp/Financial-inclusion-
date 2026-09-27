# -*- coding: utf-8 -*-
"""Put the reference implementation on the canvas beside the propositions (row R): every built page of the trio, in
both languages, as a self-contained artboard at 1440 and 390 px — so the Design review compares real rendered code
with the converged proposition on the same canvas (Design → Code → Design, drift check).

  python3 design/reference/build.py --renderer accepted && python3 design/reference/check_trio.py --shots
  python3 design/exploration/d1_canvas/reference_boards.py

The stylesheet's width media queries are resolved per board (a canvas frame is not a viewport): the 390 board carries
the base rules only; the 1440 board carries the base rules plus every `min-width` block unwrapped. Print, reduced-motion
and forced-colours queries are kept as they are. Scripts are removed (a static artboard); fonts and the logo are the
canvas's uploaded, unchanged assets.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
from proto_common import font_css, LOGO_BLOB  # noqa: E402

SITE = ROOT / "design/reference/out"
PROJECT = HERE / "out/project/project"
ROUTES = {"home": "/", "record": "/evidence/CLM-003/", "reading": "/readings/same-year-different-number/"}
SIZES = {"d": 1440, "m": 390}


def split_media(css: str):
    """Return (base_css, [(min_width_px, block_css), ...]) — other @media blocks stay in base_css."""
    out, blocks, i = [], [], 0
    while i < len(css):
        m = re.compile(r"@media \(min-width:(\d+)px\)\{").search(css, i)
        if not m:
            out.append(css[i:]); break
        out.append(css[i:m.start()])
        depth, j = 1, m.end()
        while depth and j < len(css):
            if css[j] == "{": depth += 1
            elif css[j] == "}": depth -= 1
            j += 1
        blocks.append((int(m.group(1)), css[m.end():j-1]))
        i = j
    return "".join(out), blocks


def board_css(css: str, width: int) -> str:
    base, blocks = split_media(css)
    return base + "".join(b for w, b in blocks if width >= w)


def main() -> int:
    css_site = (SITE / "assets/yfie.css").read_text(encoding="utf-8")
    css_site = re.sub(r"@font-face\{[^}]*\}", "", css_site)
    heights = {(r["route"], r["lang"], r["width"]): r["height"] for r in json.loads((SITE / "_review_trio.json").read_text(encoding="utf-8"))}
    idx = json.loads((PROJECT / "canvas.json").read_text(encoding="utf-8"))
    y0 = max(v["y"] + v["h"] for v in idx["boards"].values()) + 420
    idx["notes"]["row-ref"] = {"x": 0, "y": y0 - 300, "kind": "title1", "maxW": 9000,
                               "text": "R · Reference implementation — real rendered code (design/reference, renderer 'accepted'): compare with T4 for drift"}
    x, row_h, written = 0, 0, []
    for size, width in SIZES.items():
        for surface, route in ROUTES.items():
            for lang in ("ar", "en"):
                html = (SITE / lang / route.strip("/") / "index.html").read_text(encoding="utf-8")
                body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
                body = re.sub(r"<script[^>]*>.*?</script>", "", body, flags=re.S).replace("/assets/CauseWay_Master_Logo.png", LOGO_BLOB)
                d = "rtl" if lang == "ar" else "ltr"
                h = min(int(heights[(route, lang, width)]) + 8, 8000)
                name = f"R-{surface}-{lang}-{size}"
                title = f"R · Reference · {surface} · {lang.upper()} · {width}"
                doc = (f'<!doctype html>\n<html lang="{lang}" dir="{d}">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n<style>\nbody{{margin:0}}{font_css("blob")}{board_css(css_site, width)}\n</style>\n</helmet>\n'
                       f'<div class="root" style="width: {width}px; height: {h}px; overflow: hidden; direction: {d}">\n{body}\n</div>\n</x-dc>\n'
                       f'<script type="text/x-dc" data-dc-script data-props=\'{{"$preview":{{"width":{width},"height":{h}}}}}\'>\nclass Component extends DCLogic {{\nrenderVals() {{ return {{}}; }}\n}}\n</script>\n</body>\n</html>\n')
                fname = f"{name}.dc.html"
                (PROJECT / fname).write_text(doc, encoding="utf-8")
                entry = {"x": x, "y": y0, "w": width, "h": h, "title": title}
                if heights[(route, lang, width)] + 8 > 8000:
                    entry["expand"] = "fill"
                idx["boards"][fname] = entry
                if fname not in idx["order"]:
                    idx["order"].append(fname)
                written.append(fname)
                x += width + 80
                row_h = max(row_h, h)
    (PROJECT / "canvas.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(written)} reference boards at y={y0}; index updated ({len(idx['boards'])} boards)")
    print(" ".join(written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
