# -*- coding: utf-8 -*-
"""Shared helpers for the D1 thesis prototypes (Design workspace; not part of the reference implementation until a
thesis is chosen). Fonts, escaping, the shell hooks every prototype must keep, and the RV-CWR-001 geometry that every
thesis draws per its contract (the visual language differs per thesis through markup classes and CSS)."""
from __future__ import annotations

import html
import json

FONT_FILES = {
    "sans": [("Light", 300, "normal"), ("Regular", 400, "normal"), ("Italic", 400, "italic"), ("Medium", 500, "normal"), ("SemiBold", 600, "normal"), ("Bold", 700, "normal")],
    "arabic": [("Light", 300, "normal"), ("Regular", 400, "normal"), ("Medium", 500, "normal"), ("SemiBold", 600, "normal"), ("Bold", 700, "normal")],
}
BLOBS = {  # canvas uploads of the unchanged vendor files (same bytes as vendor/fonts/**)
    ("sans", "Regular"): "/_blob/af53b1fe767379e225167b5e03d42f0b", ("sans", "Italic"): "/_blob/847dbc8b6164544bd27b0ea3a54d7efb",
    ("sans", "Medium"): "/_blob/16e8b0d02bea1a8bd2ed08001e019cf1", ("sans", "SemiBold"): "/_blob/86a1126fe2569687147f56eaedf26478",
    ("sans", "Bold"): "/_blob/5f695190b606233d874c43c237a50a85", ("sans", "Light"): "/_blob/a4712ca1e68d8d82131353d9e8f61fed",
    ("arabic", "Regular"): "/_blob/2809b45611e3b6943eafdad61a699ce4", ("arabic", "Medium"): "/_blob/a9fd95de7d4800da5d7a26540b104c8b",
    ("arabic", "SemiBold"): "/_blob/086cd7cd8071bcfd38e071ea6f006adf", ("arabic", "Bold"): "/_blob/de02d44d7ad02a8eec017a1d14623b0d",
    ("arabic", "Light"): "/_blob/026126139d540dae0ce0eccb5fc96cbc",
}
LOGO_BLOB = "/_blob/0bd5d2628d11947a1719cfa95a477214"


def font_css(mode: str = "local") -> str:
    out = []
    for fam, faces in FONT_FILES.items():
        family = "IBM Plex Sans" if fam == "sans" else "IBM Plex Sans Arabic"
        folder = "ibm-plex-sans" if fam == "sans" else "ibm-plex-sans-arabic"
        file_base = "IBMPlexSans" if fam == "sans" else "IBMPlexSansArabic"
        for name, weight, style in faces:
            url = BLOBS[(fam, name)] if mode == "blob" else f"/assets/fonts/{folder}/{file_base}-{name}.woff2"
            out.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};font-display:swap;src:url('{url}') format('woff2')}}")
    return "".join(out)


def esc(x) -> str:
    return html.escape(str(x or ""), quote=True)


def bdi(x) -> str:
    return f'<bdi dir="ltr">{esc(x)}</bdi>'


def num(x) -> str:
    """A number as text: Western digits, thousands separators as in governed copy, isolated as an LTR run."""
    if isinstance(x, float):
        s = f"{x:,.2f}".rstrip("0").rstrip(".") if abs(x - round(x)) > 1e-9 else f"{int(round(x)):,}"
    elif isinstance(x, int):
        s = f"{x:,}" if abs(x) >= 10000 else str(x)   # years stay unseparated
    else:
        s = str(x)
    return f'<bdi dir="ltr">{s}</bdi>'


def json_block(id_: str, data) -> str:
    return f'<script type="application/json" id="{id_}">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def paragraphs(items, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{esc(p)}</p>" for p in items)


def reading_blocks(blocks, pull_cls="pull", list_cls="rlist") -> str:
    out = []
    for b in blocks:
        if b["kind"] == "p":
            out.append(f"<p>{esc(b['text'])}</p>")
        elif b["kind"] == "pull":
            out.append(f'<blockquote class="{pull_cls}"><p>{esc(b["text"])}</p></blockquote>')
        else:
            out.append(f'<ul class="{list_cls}">' + "".join(f"<li>{esc(x)}</li>" for x in b["items"]) + "</ul>")
    return "".join(out)


# ------------------------------------------------------------------------------------------------ RV-CWR-001 geometry
def rv001_data(v: dict) -> dict:
    """Resolve the governed contract rows of RV-CWR-001 into the two panels the contract prescribes."""
    series = {s["id"]: s for s in v["series"]}
    p1 = series["cby_vintages"]["values"]                     # two values at x=2024, keyed by publication
    cby = series["cby_ar2025_path"]["values"]
    imf = series["imf_staff_path"]["values"]
    idx = {}
    for d in v["derived"]:
        if d.get("x") is not None:
            idx.setdefault(d["series"], {})[d["x"]] = d
    gap = next((d for d in v["derived"] if d["id"] == "annual_growth_gap_pp"), None)
    return {"panel1": p1, "cby": cby, "imf": imf, "cby_index": idx["cby_ar2025_index"], "imf_index": idx["imf_staff_index"], "gap": gap,
            "unit_usd": p1[0]["unit"], "unit_index": idx["cby_ar2025_index"][2021]["unit"],
            "label_cby": cby[0]["series_label"], "label_imf": imf[0]["series_label"],
            "label_ar2024": p1[0]["series_label"], "label_ar2025": p1[1]["series_label"]}


def rv001_panel1_svg(d: dict, lang: str, w=420, h=300, mark_a="circle", mark_b="square", cls="rv1") -> str:
    """Panel 1: a value axis from zero; two markers at one x (2024) keyed by publication; no joining line."""
    left, right, top, bottom = 64, 24, 28, 44
    ymax = 7000
    def y(val): return top + (h - top - bottom) * (1 - val / ymax)
    x = left + (w - left - right) * 0.5
    a, b = d["panel1"][0], d["panel1"][1]
    ticks = [0, 2000, 4000, 6000]
    g = [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{h-bottom}"/>', f'<line class="axis" x1="{left}" y1="{h-bottom}" x2="{w-right}" y2="{h-bottom}"/>']
    for t in ticks:
        g.append(f'<line class="tick" x1="{left-4}" y1="{y(t):.1f}" x2="{left}" y2="{y(t):.1f}"/><text class="lbl" x="{left-8}" y="{y(t)+4:.1f}" text-anchor="end">{t:,}</text>')
    g.append(f'<text class="lbl" x="{x:.1f}" y="{h-bottom+18}" text-anchor="middle">2024</text>')
    g.append(f'<text class="unit" x="{left}" y="{top-12}">{esc(d["unit_usd"])}</text>')
    def mark(kind, cx, cy, r=7):
        return f'<circle class="mark a" cx="{cx:.1f}" cy="{cy:.1f}" r="{r}"/>' if kind == "circle" else f'<rect class="mark b" x="{cx-r:.1f}" y="{cy-r:.1f}" width="{2*r}" height="{2*r}"/>'
    ya, yb = y(a["y"]), y(b["y"])
    g.append(mark(mark_a, x, ya)); g.append(mark(mark_b, x, yb))
    g.append(f'<text class="val" x="{x+14:.1f}" y="{ya+5:.1f}">{num(a["y"])}</text>')
    g.append(f'<text class="val" x="{x+14:.1f}" y="{yb+5:.1f}">{num(b["y"])}</text>')
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" focusable="false" direction="ltr">'
            + "".join(g) + "</svg>")


def rv001_index_panel_svg(points: dict, lang: str, w=300, h=220, mark="circle", cls="rv2") -> str:
    """Panel 2, one lane: an indexed path 2021–2024 with its own axis (origin labelled), never shared with the other lane."""
    left, right, top, bottom = 48, 16, 24, 36
    ymin, ymax = 95, 122
    xs = [2021, 2022, 2023, 2024]
    def x(year): return left + (w - left - right) * (xs.index(year) / 3)
    def y(val): return top + (h - top - bottom) * (1 - (val - ymin) / (ymax - ymin))
    g = [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{h-bottom}"/>', f'<line class="axis" x1="{left}" y1="{h-bottom}" x2="{w-right}" y2="{h-bottom}"/>']
    for t in (100, 110, 120):
        g.append(f'<line class="grid" x1="{left}" y1="{y(t):.1f}" x2="{w-right}" y2="{y(t):.1f}"/><text class="lbl" x="{left-6}" y="{y(t)+4:.1f}" text-anchor="end">{t}</text>')
    g.append(f'<text class="lbl origin" x="{left-6}" y="{h-bottom+4}" text-anchor="end">{ymin}</text>')
    for yr in xs:
        g.append(f'<text class="lbl" x="{x(yr):.1f}" y="{h-bottom+16}" text-anchor="middle">{yr}</text>')
    pts = [(x(yr), y(points[yr]["value"])) for yr in xs]
    g.append('<polyline class="path" fill="none" points="' + " ".join(f"{px:.1f},{py:.1f}" for px, py in pts) + '"/>')
    for (px, py), yr in zip(pts, xs):
        if mark == "circle":
            g.append(f'<circle class="mark a" cx="{px:.1f}" cy="{py:.1f}" r="5"/>')
        else:
            g.append(f'<rect class="mark b" x="{px-5:.1f}" y="{py-5:.1f}" width="10" height="10"/>')
        g.append(f'<text class="val small" x="{px:.1f}" y="{py-10:.1f}" text-anchor="middle">{num(points[yr]["value"])}</text>')
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" focusable="false" direction="ltr">' + "".join(g) + "</svg>")


def rv001_tables(d: dict, v: dict, lang: str, cls="rvtab") -> str:
    """The contract's fallback: panel 1 as a two-row table; panel 2 as year × (value, index) per source, each column
    group with its own source. Scoped headers, caption with title, period and universe (accessibility contract)."""
    L = v["labels"]
    cap = f'{esc(v["title"])} — {esc(v["period"])} — {esc(v["universe"])}'
    p1 = d["panel1"]
    t1 = (f'<table class="{cls}"><caption>{cap}</caption><thead><tr><th scope="col">{esc(L["source"])}</th><th scope="col">2024</th><th scope="col">{esc(d["unit_usd"])}</th></tr></thead><tbody>'
          + "".join(f'<tr><th scope="row">{esc(r["series_label"])}</th><td>{num(r["x"])}</td><td>{num(r["y"])} <span class="state">{esc(L["reported"])}</span></td></tr>' for r in p1)
          + f'<tr><td colspan="3" class="marker">{esc(L["same_year_revision"])}</td></tr></tbody></table>')
    rows = []
    for yr in (2021, 2022, 2023, 2024):
        c = next(r for r in d["cby"] if r["x"] == yr); i = next(r for r in d["imf"] if r["x"] == yr)
        rows.append(f'<tr><th scope="row">{yr}</th><td>{num(c["y"])}</td><td>{num(d["cby_index"][yr]["value"])}</td><td>{num(i["y"])}</td><td>{num(d["imf_index"][yr]["value"])}</td></tr>')
    t2 = (f'<table class="{cls}"><caption>{cap} — {esc(d["unit_index"])} · {esc(L["derived"])}</caption><thead>'
          f'<tr><th scope="col" rowspan="2"></th><th scope="colgroup" colspan="2">{esc(d["label_cby"])}</th><th scope="colgroup" colspan="2">{esc(d["label_imf"])}</th></tr>'
          f'<tr><th scope="col">{esc(d["unit_usd"])}</th><th scope="col">{esc(d["unit_index"])}</th><th scope="col">{esc(d["unit_usd"])}</th><th scope="col">{esc(d["unit_index"])}</th></tr></thead>'
          f'<tbody>{"".join(rows)}<tr><td colspan="5" class="marker">{esc(L["not_comparable"])}</td></tr></tbody></table>')
    return t1 + t2


def rv001_frame_lines(v: dict) -> dict:
    """The detached-frame lines every drawing must carry inside the figure (rule 4)."""
    L = v["labels"]
    return {"title": v["title"], "scope": f'{v["period"]} · {v["universe"]}', "credit": f'{L["source"]} {v.get("credit") or ""}',
            "boundary_label": L["does_not_establish"], "boundary": v["prohibited_inference"],
            "full_record_label": L["full_record"], "full_record": v["canonical_href"],
            "note": (v.get("frame_labels") or {}).get("UI-VIS-NOTE-INDEX-CONCORDANCE", ""),
            "same_year": L["same_year_revision"], "not_comparable": L["not_comparable"]}


def rv001_panel1_rows_svg(d: dict, lang: str, w=520, h=150, cls="rv1"):
    """Panel 1 as rows: each publication is a row keyed by its label; the value sits on a horizontal axis from zero.
    Both rows belong to reference year 2024 (the panel title carries it), so the two values cannot be read as two
    consecutive points in time. Text labels are drawn by the page (HTML), not inside the SVG, so they wrap and mirror."""
    left, right, top, bottom = 12, 90, 14, 30
    xmax = 7000
    def x(val): return left + (w - left - right) * (val / xmax)
    a, b = d["panel1"][0], d["panel1"][1]
    rows = [(a, "circle", top + 30), (b, "square", top + 78)]
    g = [f'<line class="axis" x1="{left}" y1="{h-bottom}" x2="{w-right}" y2="{h-bottom}"/>']
    for t in (0, 2000, 4000, 6000):
        g.append(f'<line class="grid" x1="{x(t):.1f}" y1="{top}" x2="{x(t):.1f}" y2="{h-bottom}"/><text class="lbl" x="{x(t):.1f}" y="{h-bottom+16}" text-anchor="middle">{t:,}</text>')
    for val, kind, cy in rows:
        cx = x(val["y"])
        g.append(f'<line class="stem" x1="{left}" y1="{cy}" x2="{cx:.1f}" y2="{cy}"/>')
        if kind == "circle":
            g.append(f'<circle class="mark a" cx="{cx:.1f}" cy="{cy}" r="7"/>')
        else:
            g.append(f'<rect class="mark b" x="{cx-7:.1f}" y="{cy-7}" width="14" height="14"/>')
        g.append(f'<text class="val" x="{cx+14:.1f}" y="{cy+5}">{num(val["y"])}</text>')
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" focusable="false" direction="ltr">' + "".join(g) + "</svg>")
