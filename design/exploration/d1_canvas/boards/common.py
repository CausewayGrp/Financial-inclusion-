# -*- coding: utf-8 -*-
"""Board authoring layer for the D1 canvas. A proposition module gives CSS and compositions; this layer supplies the
governed text (from the neutral harness bundle — never retyped), the fonts and logo, and the canvas file format."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from proto_common import esc, num, plain_num, bdi, paragraphs, reading_blocks, font_css, rv001_data, rv001_panel1_svg, rv001_panel1_rows_svg, rv001_index_panel_svg, rv001_tables, rv001_frame_lines, LOGO_BLOB  # noqa: E402,F401
from proto_shell import mobile_rules, responsive_rules  # noqa: E402,F401

ROOT = HERE.parents[3]  # repository root
BUNDLE = ROOT / "design/reference/out/_bundle"  # written by: python3 design/reference/build.py --renderer neutral
ROUTES = {"home": "/", "record": "/evidence/CLM-003/", "reading": "/readings/same-year-different-number/"}
LOGO_LOCAL = "/assets/CauseWay_Master_Logo.png"
SIZES = {"d": 1440, "m": 390}


def load(surface: str, lang: str) -> tuple[dict, dict]:
    name = (ROUTES[surface].strip("/").replace("/", "_") or "home") + f"__{lang}.json"
    b = json.loads((BUNDLE / name).read_text(encoding="utf-8"))
    return b["page"], b["shell"]


def nav_flat(shell: dict) -> list[dict]:
    out = []
    for item in shell["nav"]:
        if item.get("children"):
            out.append({"group": item["label"], "children": item["children"], "active": any(k["active"] for k in item["children"])})
        else:
            out.append({"label": item["label"], "href": item["href"], "active": item.get("active", False)})
    return out


def logo(px: int, mode: str = "local", cls: str = "") -> str:
    src = LOGO_BLOB if mode == "blob" else LOGO_LOCAL
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{src}" alt="CauseWay" width="{px}" height="{px}">'


def base_mechanics() -> str:
    return ("*,*::before,*::after{box-sizing:border-box}img{max-width:100%;height:auto;display:block}"
            ".sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}"
            ".table-wrap{overflow-x:auto;max-width:100%}")


def twin_html(css: str, body: str, lang: str, size: str, width: int) -> str:
    """A plain HTML twin of a board for local rendering (Playwright): same markup, same CSS, local fonts and logo."""
    d = "rtl" if lang == "ar" else "ltr"
    cls = "vp-m" if size == "m" else "vp-d"
    return (f'<!doctype html><html lang="{lang}" dir="{d}" class="{cls}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<style>{font_css("local")}{base_mechanics()}{css}</style></head><body>{body}</body></html>')


def board_html(css: str, body: str, lang: str, size: str, width: int, height: int, title: str) -> str:
    """The canvas artboard (.dc.html): self-contained, fonts and logo as uploaded assets, root fixed to the frame."""
    d = "rtl" if lang == "ar" else "ltr"
    cls = "root vp-m" if size == "m" else "root vp-d"
    body_blob = body.replace(LOGO_LOCAL, LOGO_BLOB)
    return (f'<!doctype html>\n<html lang="{lang}" dir="{d}">\n<head>\n<meta charset="utf-8">\n<title>{esc(title)}</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n<style>\n'
            f'body{{margin:0}}{font_css("blob")}{base_mechanics()}{css}\n</style>\n</helmet>\n'
            f'<div class="{cls}" style="width: {width}px; height: {height}px; overflow: hidden; direction: {d}">\n{body_blob}\n</div>\n</x-dc>\n'
            f'<script type="text/x-dc" data-dc-script data-props=\'{{"$preview":{{"width":{width},"height":{height}}}}}\'>\nclass Component extends DCLogic {{\nrenderVals() {{ return {{}}; }}\n}}\n</script>\n</body>\n</html>\n')
