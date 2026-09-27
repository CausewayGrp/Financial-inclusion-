# -*- coding: utf-8 -*-
"""Visual contracts for the reference implementation — D1: RV-CWR-001 in the converged form (design/01_FOUNDATIONS.md
§3.3, §4.1 item 5). Every drawing uses percentage x-coordinates on an SVG without a viewBox, so the figure follows its
column at every width without scaling its text and needs no inline style (strict CSP). Numeric value and time axes run
left to right in both languages (governed contract rule); labels, legends and panel order follow the reading direction.
The text alternative (alt text plus the contract's tables) ships visibly with the chart."""
from __future__ import annotations

import html


def esc(x) -> str:
    return html.escape(str(x or ""), quote=True)


def plain_num(x, year: bool = False) -> str:
    """One number rule: Western digits, thousands separators on every value, years never separated, precision as
    governed (no trailing .0)."""
    if year:
        return str(x)
    if isinstance(x, float):
        return f"{x:,.2f}".rstrip("0").rstrip(".") if abs(x - round(x)) > 1e-9 else f"{int(round(x)):,}"
    if isinstance(x, int):
        return f"{x:,}"
    return str(x)


def num(x, year: bool = False) -> str:
    """plain_num, isolated as a left-to-right run for HTML text (never inside SVG <text>)."""
    return f'<bdi dir="ltr">{plain_num(x, year)}</bdi>'


# ------------------------------------------------------------------------------------------------ RV-CWR-001
def rv001_data(v: dict) -> dict:
    """Resolve the governed contract rows into the two panels the contract prescribes."""
    series = {s["id"]: s for s in v["series"]}
    p1 = series["cby_vintages"]["values"]
    cby = series["cby_ar2025_path"]["values"]
    imf = series["imf_staff_path"]["values"]
    idx: dict = {}
    for d in v["derived"]:
        if d.get("x") is not None:
            idx.setdefault(d["series"], {})[d["x"]] = d
    return {"panel1": p1, "cby": cby, "imf": imf, "cby_index": idx["cby_ar2025_index"], "imf_index": idx["imf_staff_index"],
            "unit_usd": p1[0]["unit"], "unit_index": idx["cby_ar2025_index"][2021]["unit"],
            "label_cby": cby[0]["series_label"], "label_imf": imf[0]["series_label"],
            "label_ar2024": p1[0]["series_label"], "label_ar2025": p1[1]["series_label"]}


def rv001_frame_lines(v: dict) -> dict:
    L = v["labels"]
    return {"title": v["title"], "scope": f'{v["period"]} · {v["universe"]}', "credit": f'{L["source"]} {v.get("credit") or ""}',
            "boundary_label": L["does_not_establish"], "boundary": v["prohibited_inference"],
            "full_record_label": L["full_record"], "full_record": v["canonical_href"],
            "note": (v.get("frame_labels") or {}).get("UI-VIS-NOTE-INDEX-CONCORDANCE", ""),
            "same_year": L["same_year_revision"], "not_comparable": L["not_comparable"]}


def rv001_tables(d: dict, v: dict, cls: str = "rvtab") -> str:
    """The contract's fallback: panel 1 as a two-row table; panel 2 as year × (value, index) per source, each column
    group with its own source. Scoped headers; caption with title, period and universe."""
    L = v["labels"]
    cap = f'{esc(v["title"])} — {esc(v["period"])} — {esc(v["universe"])}'
    t1 = (f'<table class="{cls}"><caption>{cap}</caption><thead><tr><th scope="col">{esc(L["source"])}</th><th scope="col">2024</th><th scope="col">{esc(d["unit_usd"])}</th></tr></thead><tbody>'
          + "".join(f'<tr><th scope="row">{esc(r["series_label"])}</th><td>{num(r["x"], year=True)}</td><td>{num(r["y"])} <span class="state">{esc(L["reported"])}</span></td></tr>' for r in d["panel1"])
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


def _pct(v, lo=1.0, hi=88.0, vmax=7000.0):
    return lo + (hi - lo) * (v / vmax)


def svg_mark(kind: str, x: str, cy: float, r: float) -> str:
    """One mark per publication, the same in every panel: ● Annual Report 2024, □ Annual Report 2025, ◎ IMF.
    Drawn from percentage x (no rotation: a transform would need the absolute x)."""
    if kind == "circle":
        return f'<circle class="mark a" cx="{x}" cy="{cy}" r="{r}"/>'
    if kind == "square":
        return f'<rect class="mark b" x="{x}" y="{cy-r}" width="{2*r}" height="{2*r}" transform="translate(-{r},0)"/>'
    return f'<circle class="mark b" cx="{x}" cy="{cy}" r="{r}"/><circle class="mark a" cx="{x}" cy="{cy}" r="{max(1.5, r/2.6):.1f}"/>'


def p1_rows(d: dict) -> str:
    """Panel 1 as rows: one row per publication keyed by its governed label (HTML, so it wraps and mirrors), the value
    on a horizontal axis from zero, the value printed above the mark."""
    rows = []
    for val, kind in ((d["panel1"][0], "circle"), (d["panel1"][1], "square")):
        x = _pct(val["y"])
        track = (f'<svg class="trk" width="100%" height="38" aria-hidden="true" focusable="false" direction="ltr">'
                 f'<line class="stem" x1="1%" y1="26" x2="{x:.2f}%" y2="26"/>{svg_mark(kind, f"{x:.2f}%", 26, 7)}'
                 f'<text class="val" x="{x:.2f}%" y="11" text-anchor="middle">{plain_num(val["y"])}</text></svg>')
        rows.append(f'<div class="row"><div class="rl">{esc(val["series_label"])}</div>{track}</div>')
    ticks = "".join(f'<line class="tick" x1="{_pct(t):.2f}%" y1="0" x2="{_pct(t):.2f}%" y2="5"/><text class="lbl" x="{_pct(t):.2f}%" y="18" text-anchor="middle">{t:,}</text>' for t in (0, 2000, 4000, 6000))
    axis = (f'<div class="row ax-row"><div></div><svg class="ax" width="100%" height="22" aria-hidden="true" focusable="false" direction="ltr">'
            f'<line class="axis" x1="1%" y1="0.5" x2="88%" y2="0.5"/>{ticks}</svg></div>')
    return f'<div class="p1">{"".join(rows)}{axis}</div>'


def lane(points: dict, mark: str) -> str:
    """Panel 2, one lane: the indexed path 2021–2024 on its own axis whose baseline is the index origin (2021 = 100)."""
    xs = [2021, 2022, 2023, 2024]
    def x(yr): return 12 + 82 * (xs.index(yr) / 3)
    def y(v): return 24 + (200 - 24 - 36) * (1 - (v - 100) / (122 - 100))
    g = ['<line class="axis" x1="12%" y1="24" x2="12%" y2="164"/>', '<line class="axis" x1="12%" y1="164" x2="94%" y2="164"/>']
    for t in (110, 120):
        g.append(f'<line class="grid" x1="12%" y1="{y(t):.1f}" x2="94%" y2="{y(t):.1f}"/><text class="lbl" x="10%" y="{y(t)+4:.1f}" text-anchor="end">{t}</text>')
    g.append('<text class="lbl origin" x="10%" y="168" text-anchor="end">100</text>')
    for yr in xs:
        g.append(f'<text class="lbl" x="{x(yr):.2f}%" y="182" text-anchor="middle">{yr}</text>')
    pts = [(x(yr), y(points[yr]["value"])) for yr in xs]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        g.append(f'<line class="path" x1="{x1:.2f}%" y1="{y1:.1f}" x2="{x2:.2f}%" y2="{y2:.1f}"/>')
    for (px, py), yr in zip(pts, xs):
        g.append(svg_mark(mark, f"{px:.2f}%", round(py, 1), 5))
        if yr != xs[0]:
            g.append(f'<text class="val small" x="{px:.2f}%" y="{py-10:.1f}" text-anchor="middle">{plain_num(points[yr]["value"])}</text>')
    return f'<svg class="rv2" width="100%" height="200" aria-hidden="true" focusable="false" direction="ltr">{"".join(g)}</svg>'


def rv001_figure(v: dict, cite_label: str, origin: str | None) -> str:
    """The whole figure object: frame (rubric, title, question, scope), panel 1 rows, panel 2 lanes with the
    not-comparable divider between them, the in-frame note, boundary, credit, canonical link (absolute when the
    deployment origin is set) and cite action, then the visible text alternative."""
    d = rv001_data(v); f = rv001_frame_lines(v)
    def base(series):
        r = next(r for r in series if r["x"] == 2021)
        return f'<span class="base">2021 · {num(r["y"])} {esc(r["unit"])}</span>'
    canon = (origin or "") + f["full_record"]
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" data-image-independent="true"><span class="rubric">{esc(v["labels"]["analytical_question"])}</span><h2 class="fig-t">{esc(f["title"])}</h2><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(f["scope"])}</p>'
            f'<div class="panels"><div class="panel p1p"><p class="ph">2024 · {esc(d["unit_usd"])}</p><p class="cap same"><b>{esc(f["same_year"])}</b></p>{p1_rows(d)}</div>'
            f'<div class="panel p2"><p class="ph">{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</p>'
            f'<div class="lanes"><div class="lane"><h3>{esc(d["label_cby"])}</h3>{base(d["cby"])}{lane(d["cby_index"], "square")}</div><div class="between">{esc(f["not_comparable"])}</div><div class="lane"><h3>{esc(d["label_imf"])}</h3>{base(d["imf"])}{lane(d["imf_index"], "ring")}</div></div><p class="cap note">{esc(f["note"])}</p></div></div>'
            f'<div class="foot"><p class="b"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{esc(f["credit"])}</p><p>{esc(f["full_record_label"])} <a class="canon" dir="ltr" href="{esc(f["full_record"])}">{esc(canon)}</a> · <button type="button" class="tbtn" data-cite>{esc(cite_label)}</button></p></div>'
            f'<div class="alt"><h3 class="alt-h">{esc(v["labels"]["text_alternative"])}</h3><p class="small">{esc(v["alt_text"])}</p><div class="table-wrap" tabindex="0">{rv001_tables(d, v)}</div></div>'
            f'<figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


FIGURES = {"RV-CWR-001": rv001_figure}


def figure(v: dict, cite_label: str, origin: str | None) -> str:
    """Draw a bound visual per its contract. D1 draws RV-CWR-001; any other contract renders its governed text
    alternative as a frame (no chart is invented — SUPPORTING and TABLE_TEXT_FIRST tiers never plot values)."""
    if v["id"] in FIGURES:
        return FIGURES[v["id"]](v, cite_label, origin)
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" data-image-independent="true"><span class="rubric">{esc(v["labels"]["analytical_question"])}</span><h2 class="fig-t">{esc(v["title"])}</h2>'
            f'<p class="cap">{esc(v["question"])}</p><div class="body"><p>{esc(v["alt_text"])}</p></div>'
            f'<div class="foot"><p class="b"><b>{esc(v["labels"]["does_not_establish"])}</b> {esc(v["prohibited_inference"])}</p><p>{esc(v["labels"]["source"])} {esc(v.get("credit") or "")}</p>'
            f'<p>{esc(v["labels"]["full_record"])} <a class="canon" dir="ltr" href="{esc(v["canonical_href"])}">{esc((origin or "") + v["canonical_href"])}</a></p></div><figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')
