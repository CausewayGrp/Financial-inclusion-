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


def bdi(x) -> str:
    """An identifier, date or numeric run isolated as an unbroken left-to-right run (HTML text only)."""
    return f'<bdi dir="ltr" class="nw">{esc(x)}</bdi>'


def plain_num(x, year: bool = False) -> str:
    """One number rule: Western digits, thousands separators on every value, years never separated, precision as
    governed (no trailing .0)."""
    if year:
        return str(x)
    if isinstance(x, float):
        return f"{int(x):,}" if x.is_integer() else f"{x:,}"   # the shortest exact representation, thousands separated
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


def nice_step(span: float) -> float:
    """A round tick step (1, 2 or 5 × a power of ten) giving three to four ticks across `span`."""
    import math
    raw = span / 3.5
    mag = 10 ** math.floor(math.log10(raw))
    for k in (1, 2, 5, 10):
        if k * mag >= raw:
            return k * mag
    return 10 * mag


def axis_scale(values) -> tuple[float, float]:
    """(axis end, tick step): a round step from the data's span, the axis end the next step above 1.08 × max."""
    import math
    m = max(values) * 1.08
    step = nice_step(m)
    return step * math.ceil(m / step), step


FIG_ATTRS = 'data-visual-fallback="ordered-text" data-image-independent="true" data-noncolour-semantic="text-structure-label-position"'


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
    on a horizontal axis from zero, the value printed above the mark. The axis end and its ticks come from the data."""
    vmax, step = axis_scale([v["y"] for v in d["panel1"]])
    rows = []
    for val, kind in ((d["panel1"][0], "circle"), (d["panel1"][1], "square")):
        x = _pct(val["y"], vmax=vmax)
        track = (f'<svg class="trk" width="100%" height="38" aria-hidden="true" focusable="false" direction="ltr">'
                 f'<line class="stem" x1="1%" y1="26" x2="{x:.2f}%" y2="26"/>{svg_mark(kind, f"{x:.2f}%", 26, 7)}'
                 f'<text class="val" x="{x:.2f}%" y="11" text-anchor="middle">{plain_num(val["y"])}</text></svg>')
        rows.append(f'<div class="row"><div class="rl">{esc(val["series_label"])}</div>{track}</div>')
    tick_values = [t * step for t in range(0, int(vmax // step) + 1) if t * step <= vmax * 0.999 or t == 0]
    ticks = "".join(f'<line class="tick" x1="{_pct(t, vmax=vmax):.2f}%" y1="0" x2="{_pct(t, vmax=vmax):.2f}%" y2="5"/><text class="lbl" x="{_pct(t, vmax=vmax):.2f}%" y="18" text-anchor="middle">{plain_num(int(t))}</text>' for t in tick_values)
    axis = (f'<div class="row ax-row"><div></div><svg class="ax" width="100%" height="22" aria-hidden="true" focusable="false" direction="ltr">'
            f'<line class="axis" x1="1%" y1="0.5" x2="88%" y2="0.5"/>{ticks}</svg></div>')
    return f'<div class="p1">{"".join(rows)}{axis}</div>'


def lane(points: dict, mark: str) -> str:
    """Panel 2, one lane: the indexed path on its own axis whose baseline is the index origin (first year = 100);
    years and the axis top come from the data."""
    import math
    xs = sorted(points)
    top = max(110.0, 10 * math.ceil(max(p["value"] for p in points.values()) * 1.02 / 10))
    def x(yr): return 12 + 82 * (xs.index(yr) / (len(xs) - 1))
    def y(v): return 24 + (200 - 24 - 36) * (1 - (v - 100) / (top - 100))
    g = ['<line class="axis" x1="12%" y1="24" x2="12%" y2="164"/>', '<line class="axis" x1="12%" y1="164" x2="94%" y2="164"/>']
    for t in range(110, int(top) + 1, 10):
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


def rv001_figure(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """The whole figure object: frame (rubric, title, question, scope), panel 1 rows, panel 2 lanes with the
    not-comparable divider between them, the in-frame note, boundary, credit, canonical link (absolute when the
    deployment origin is set) and cite action, then the visible text alternative."""
    d = rv001_data(v); f = rv001_frame_lines(v)
    def base(series):
        r = next(r for r in series if r["x"] == 2021)
        return f'<span class="base">2021 · {num(r["y"])} {esc(r["unit"])}</span>'
    canon = (origin or "") + f["full_record"]
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(v["labels"]["analytical_question"])}</span><{heading} class="fig-t">{esc(f["title"])}</{heading}><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(f["scope"])}</p>'
            f'<div class="panels"><div class="panel p1p"><p class="ph">2024 · {esc(d["unit_usd"])}</p><p class="cap same"><b>{esc(f["same_year"])}</b></p>{p1_rows(d)}</div>'
            f'<div class="panel p2"><p class="ph">{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</p>'
            f'<div class="lanes"><div class="lane"><h3>{esc(d["label_cby"])}</h3>{base(d["cby"])}{lane(d["cby_index"], "square")}</div><div class="between">{esc(f["not_comparable"])}</div><div class="lane"><h3>{esc(d["label_imf"])}</h3>{base(d["imf"])}{lane(d["imf_index"], "ring")}</div></div><p class="cap note">{esc(f["note"])}</p></div></div>'
            f'<div class="foot"><p class="b"><b>{esc(f["boundary_label"])}</b> {esc(f["boundary"])}</p><p>{credit_line(v)}</p><p>{esc(f["full_record_label"])} <a class="canon" dir="ltr" href="{esc(f["full_record"])}">{esc(canon)}</a> · <button type="button" class="tbtn" data-cite>{esc(cite_label)}</button></p></div>'
            f'<div class="alt" data-visual-fallback="ordered-text"><h3 class="alt-h">{esc(v["labels"]["text_alternative"])}</h3>'
            f'<p class="small"><b>{esc(v["labels"]["what_it_shows"])}</b> {esc(v["alt_text"])}</p><p class="small"><b>{esc(v["labels"]["scope"])}:</b> {esc(f["scope"])}</p>'
            f'<div class="table-wrap" tabindex="0">{rv001_tables(d, v)}</div></div>'
            f'<figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


FIGURES = {"RV-CWR-001": rv001_figure}


def credit_line(v: dict) -> str:
    """The governed credit. Publisher names are governed in English only; Arabic frames print them as isolated
    left-to-right runs (the contract's `credit.language_note`)."""
    return f'{esc(v["labels"]["source"])} <bdi dir="ltr">{esc(v.get("credit") or "")}</bdi>'


def figure(v: dict, cite_label: str, origin: str | None, heading: str = "h2", eyebrow: str | None = None, open_label: str | None = None, boundary_label: str | None = None) -> str:
    """Draw a bound visual per its contract. D1 draws RV-CWR-001; D2 draws the CORE_ANALYTICAL contracts of the hard
    families and the payment chain (DRAWERS); any other contract renders its governed text alternative as a frame
    with the same anatomy — rubric, title, question, scope, the alternative, boundary, credit, canonical link (no chart
    is invented: SUPPORTING and TABLE_TEXT_FIRST tiers never plot values)."""
    if v["id"] in FIGURES:
        return FIGURES[v["id"]](v, cite_label, origin, heading)
    if v["id"] in DRAWERS:
        return DRAWERS[v["id"]](v, cite_label, origin, heading)
    return text_frame(v, cite_label, origin, heading, eyebrow, open_label, boundary_label)


def text_frame(v: dict, cite_label: str, origin: str | None, heading: str = "h2", eyebrow: str | None = None, open_label: str | None = None, boundary_label: str | None = None) -> str:
    """A contract without a drawing: the governed text alternative in the frame anatomy (no chart is invented)."""
    rub = eyebrow if eyebrow is not None else v["labels"]["analytical_question"]
    scope = f'{v["period"]} · {v["universe"]}' if v.get("period") or v.get("universe") else ""
    canon = (origin or "") + v["canonical_href"]
    link = f'<a class="canon" dir="ltr" href="{esc(v["canonical_href"])}">{esc(canon)}</a>' if not open_label else f'<a href="{esc(v["canonical_href"])}">{esc(open_label)}</a>'
    # A text frame has no view: the governed description is the frame's body, so its heading ("Text description of this
    # view") stays in the accessibility tree only, and the boundary is printed once, in the foot (D3, cold-reader test;
    # the label itself is escalated — ESCALATIONS.md, text-first tiers).
    return (f'<figure class="fig fig-text" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(rub)}</span><{heading} class="fig-t">{esc(v["title"])}</{heading}>'
            f'<p class="cap">{esc(v["question"])}</p>'
            f'<div class="alt alt-body" data-visual-fallback="ordered-text"><h3 class="alt-h sr-only">{esc(v["labels"]["text_alternative"])}</h3><p class="body"><b>{esc(v["labels"]["what_it_shows"])}</b> {esc(v["alt_text"])}</p>'
            + (f'<p class="small"><b>{esc(v["labels"]["scope"])}:</b> {esc(scope)}</p>' if scope else "")
            + '</div>'
            f'<div class="foot"><p class="b"><b>{esc(v["labels"]["what_not_to_conclude"])}:</b> {esc(v["prohibited_inference"])}</p>' + (f'<p>{credit_line(v)}</p>' if v.get("credit") else "")
            + f'<p>{esc(v["labels"]["full_record"])} {link} · <button type="button" class="tbtn" data-cite>{esc(cite_label)}</button></p></div></figure>')


# ================================================================================================ D2 drawings
# Every D2 figure shares one anatomy with RV-CWR-001: rubric, governed title, question, scope; the panels; the in-frame
# notes; the boundary, the credit (isolated left-to-right), the canonical link and the cite action; then the visible
# text alternative (the governed alt text, the scope and the contract's table). Percentage x-coordinates on SVGs
# without a viewBox keep text at type size at every width (D1 technique); nothing carries meaning by colour alone.

MONTHS_SHORT = {"en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}
MARK_SHAPE = {"REPORTED": "circle", "MEASURED": "circle", "ADMINISTRATIVE": "square", "ESTIMATED": "hollow", "PROJECTED": "hollow", "HISTORICAL": "circle", "PROGRAMME": "hollow", "DERIVED": "none"}


def marker_label(v: dict, token: str) -> str:
    return v["marker_labels"].get(token.replace("_", "-"), "") or v["marker_labels"].get(token, "")


def state_label(v: dict, token: str) -> str:
    return v["state_labels"].get(token, "")


def frame_open(v: dict, heading: str, panel_head: str = "") -> str:
    scope = " · ".join(x for x in (v.get("period"), v.get("universe")) if x)
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(v["labels"]["analytical_question"])}</span>'
            f'<{heading} class="fig-t">{esc(v["title"])}</{heading}><p class="cap">{esc(v["question"])}</p><p class="cap">{esc(scope)}</p>{panel_head}')


def frame_close(v: dict, cite_label: str, origin: str | None, tables: str, notes: str = "", key: str = "") -> str:
    L = v["labels"]
    scope = " · ".join(x for x in (v.get("period"), v.get("universe")) if x)
    canon = (origin or "") + v["canonical_href"]
    frame_notes = "".join(f'<p class="cap note">{esc(t)}</p>' for t in (v.get("frame_labels") or {}).values() if t)
    credit = f'<p>{credit_line(v)}</p>' if v.get("credit") else ""
    table_html = f'<div class="table-wrap" tabindex="0">{tables}</div>' if tables else ""
    # The boundary is printed once per frame, in the boundary voice, under the governed "What not to conclude" label
    # (the label the baseline uses for a visual); the text alternative below carries what the view shows, its scope
    # and the contract's table — never a second copy of the boundary (D3, cold-reader test).
    return (f'{key}{notes}{frame_notes}'
            f'<div class="foot"><p class="b"><b>{esc(L["what_not_to_conclude"])}:</b> {esc(v["prohibited_inference"])}</p>{credit}'
            f'<p>{esc(L["full_record"])} <a class="canon" dir="ltr" href="{esc(v["canonical_href"])}">{esc(canon)}</a> · <button type="button" class="tbtn" data-cite>{esc(cite_label)}</button></p></div>'
            f'<div class="alt" data-visual-fallback="ordered-text"><h3 class="alt-h">{esc(L["text_alternative"])}</h3>'
            f'<p class="small"><b>{esc(L["what_it_shows"])}</b> {esc(v["alt_text"])}</p><p class="small"><b>{esc(L["scope"])}:</b> {esc(scope)}</p>'
            f'{table_html}</div>'
            f'<figcaption class="sr-only">{esc(v["alt_text"])}</figcaption></figure>')


def table(caption: str, head: list, rows: list, cls: str = "rvtab", foot: str = "") -> str:
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = "".join("<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>" for r in rows)
    foot_html = f'<tr><td colspan="{len(head)}" class="marker">{foot}</td></tr>' if foot else ""
    return f'<table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}{foot_html}</tbody></table>'


def caption_of(v: dict, extra: str = "") -> str:
    parts = [esc(v["title"]), esc(v.get("period") or ""), esc(v.get("universe") or "")]
    return " — ".join(p for p in parts if p) + (f" — {extra}" if extra else "")


# ------------------------------------------------------------------------------------------------ bars (VIS-FINDEX-GAPS)
def bar_rows(rows: list, vmax: float, unit_col: bool = False) -> str:
    """Horizontal bars from zero on a shared axis; one HTML row per governed group (the label wraps and mirrors), the
    value printed at the bar's end. Rows may print their own unit when it differs from the panel's."""
    out = []
    for r in rows:
        x = _pct(r["y"], vmax=vmax)
        unit = f'<span class="unit-l">{esc(r["unit"])}</span>' if unit_col and r.get("unit") else ""
        out.append(f'<div class="row"><div class="rl">{esc(r["x_text"])}{unit}</div>'
                   f'<svg class="trk" width="100%" height="30" aria-hidden="true" focusable="false" direction="ltr"><rect class="bar" x="1%" y="7" width="{x-1:.2f}%" height="16"/>'
                   f'<text class="val" x="{x+1:.2f}%" y="19" text-anchor="start">{plain_num(r["y"])}</text></svg></div>')
    return "".join(out)


def axis_row(vmax: float, step: float, height: int = 22) -> str:
    ticks = [t * step for t in range(0, int(vmax // step) + 1) if t * step <= vmax * 0.999 or t == 0]
    tk = "".join(f'<line class="tick" x1="{_pct(t, vmax=vmax):.2f}%" y1="0" x2="{_pct(t, vmax=vmax):.2f}%" y2="5"/><text class="lbl" x="{_pct(t, vmax=vmax):.2f}%" y="18" text-anchor="middle">{plain_num(int(t) if float(t).is_integer() else t)}</text>' for t in ticks)
    return f'<div class="row ax-row"><div></div><svg class="ax" width="100%" height="{height}" aria-hidden="true" focusable="false" direction="ltr"><line class="axis" x1="1%" y1="0.5" x2="88%" y2="0.5"/>{tk}</svg></div>'


def findex_gaps(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    vals = v["series"][0]["values"]
    by_id = {r["id"]: r for r in vals}
    vmax, step = axis_scale([r["y"] for r in vals])
    derived_label = state_label(v, "DERIVED")
    # pairs come from the governed derived rows: each names the two observations it is calculated from
    pairs = [(d, by_id[d["from"][0]], by_id[d["from"][1]]) for d in v["derived"] if len(d.get("from") or []) == 2 and all(i in by_id for i in d["from"])]
    paired = {r["id"] for _, a, b in pairs for r in (a, b)}
    common_unit = vals[0]["unit"]
    html_ = [f'<div class="panel bars"><p class="ph">{esc(common_unit)} · {esc(state_label(v, "MEASURED"))}</p>']
    html_.append('<div class="p1">' + bar_rows([r for r in vals if r["id"] not in paired], vmax) + "</div>")
    for d, a, b in pairs:
        pair_rows = [b, a] if vals.index(b) < vals.index(a) else [a, b]   # governed order of the contract (women before men, …)
        own_unit = any(r["unit"] != common_unit for r in pair_rows)
        html_.append(f'<div class="pair"><div class="p1">{bar_rows(pair_rows, vmax, unit_col=own_unit)}</div>'
                     f'<p class="gap"><span class="bracket" aria-hidden="true"></span>{esc(derived_label)} · {num(d["value"])} {esc(d["unit"])}</p></div>')
    html_.append('<div class="p1">' + axis_row(vmax, step) + "</div></div>")
    rows = [[esc(r["x_text"]), num(r["y"]), esc(r["unit"]), esc(state_label(v, r["state"]))] for r in vals]
    rows += [[esc(derived_label), num(d["value"]), esc(d["unit"]), esc(f'{by_id[d["from"][0]]["x_text"]} − {by_id[d["from"][1]]["x_text"]}')] for d, _, _ in pairs]
    tbl = table(caption_of(v), ["", esc(common_unit), "", ""], rows)
    return frame_open(v, heading) + f'<div class="panels">{"".join(html_)}</div>' + frame_close(v, cite_label, origin, tbl)


# ------------------------------------------------------------------------------------------------ time-series lines
def line_panel(v: dict, series: dict, panel_id: str, height: int = 200) -> tuple[str, list]:
    """One line panel: the governed values on a zero-based value axis with a left-to-right time axis; marks keyed by
    evidence state (filled = reported/administrative/measured, hollow = estimated/projected; square = administrative);
    a projected segment dashed; a BREAK never joined and marked; a MISSING x a labelled gap; DISAGREEMENT ringed.
    Returns the SVG and the list of note lines (state key, break, missing, disagreement) for the HTML under it."""
    vals = series["values"]
    xs = sorted({str(r["x"]) for r in vals} | {str(m["x"]) for m in series.get("missing_x") or []})
    top, step = axis_scale([r["y"] for r in vals if r.get("y") is not None])
    lo, hi = 24, height - 36
    def X(x): return 8 + 88 * (xs.index(str(x)) / max(1, len(xs) - 1))
    def Y(y): return lo + (hi - lo) * (1 - y / top)
    g = [f'<line class="axis" x1="8%" y1="{lo}" x2="8%" y2="{hi}"/>', f'<line class="axis" x1="8%" y1="{hi}" x2="96%" y2="{hi}"/>']
    t = step
    while t <= top + 1e-9:
        g.append(f'<line class="grid" x1="8%" y1="{Y(t):.1f}" x2="96%" y2="{Y(t):.1f}"/><text class="lbl" x="6.5%" y="{Y(t)+4:.1f}" text-anchor="end">{plain_num(int(t) if float(t).is_integer() else t)}</text>')
        t += step
    g.append(f'<text class="lbl origin" x="6.5%" y="{hi+4}" text-anchor="end">0</text>')
    for i, x in enumerate(xs):
        cls = "lbl" if (i in (0, len(xs) - 1) or len(xs) <= 7 or i % 2 == 0) else "lbl alt"
        g.append(f'<text class="{cls}" x="{X(x):.2f}%" y="{hi+18}" text-anchor="middle">{esc(x)}</text>')
    missing = {str(m["x"]): m.get("marker") for m in series.get("missing_x") or []}
    notes = []
    prev = None
    for r in vals:
        if r.get("y") is None:
            continue
        x, y = X(r["x"]), Y(r["y"])
        broken = any(m.startswith("BREAK") for m in r["markers"])
        gap_between = prev is not None and any(xs.index(str(prev["x"])) < xs.index(mx) < xs.index(str(r["x"])) for mx in missing)
        if prev is not None and not broken and not gap_between:
            dashed = r["state"] == "PROJECTED" or prev["state"] == "PROJECTED"
            g.append(f'<line class="path{" dashed" if dashed else ""}" x1="{X(prev["x"]):.2f}%" y1="{Y(prev["y"]):.1f}" x2="{x:.2f}%" y2="{y:.1f}"/>')
        if broken and prev is not None:
            bx = (X(prev["x"]) + x) / 2
            g.append(f'<line class="brk" x1="{bx-0.4:.2f}%" y1="{lo}" x2="{bx-0.4:.2f}%" y2="{hi}"/><line class="brk" x1="{bx+0.4:.2f}%" y1="{lo}" x2="{bx+0.4:.2f}%" y2="{hi}"/>')
            for m in r["markers"]:
                if m.startswith("BREAK"):
                    notes.append(("brk", f'{prev["x"]} → {r["x"]}', marker_label(v, m)))
        shape = MARK_SHAPE.get(r["state"], "circle")
        mark = {"circle": svg_mark("circle", f"{x:.2f}%", round(y, 1), 5), "square": f'<rect class="mark a" x="{x:.2f}%" y="{y-5:.1f}" width="10" height="10" transform="translate(-5,0)"/>',
                "hollow": f'<circle class="mark b" cx="{x:.2f}%" cy="{y:.1f}" r="5"/>'}[shape]
        if "DISAGREEMENT" in r["markers"]:
            mark += f'<circle class="ring" cx="{x:.2f}%" cy="{y:.1f}" r="9"/>'
        g.append(mark)
        dense = len(vals) > 8
        own_marks = [m for m in r["markers"] if m not in (series.get("markers") or [])]   # a series-wide marker (NOMINAL) marks no point
        keep = (r is vals[0] or r is vals[-1] or own_marks or (prev is not None and prev["state"] != r["state"]))
        row = 12 if (not dense or vals.index(r) % 2 == 0) else 26   # dense series: labels on two rows so neighbours never collide
        g.append(f'<text class="val{" dense" if dense and not keep else ""}" x="{x:.2f}%" y="{y-row:.1f}" text-anchor="middle">{plain_num(r["y"])}</text>')
        prev = r
    for mx, marker in missing.items():
        x = X(mx)
        g.append(f'<line class="miss" x1="{x:.2f}%" y1="{lo+20}" x2="{x:.2f}%" y2="{hi}"/>')
        notes.append(("miss", mx, marker_label(v, marker or "MISSING")))
    dis = [str(r["x"]) for r in vals if "DISAGREEMENT" in r["markers"]]
    if dis:
        notes.append(("dis", ", ".join(dis), marker_label(v, "DISAGREEMENT")))
    return f'<svg class="rv2 ts" width="100%" height="{height}" aria-hidden="true" focusable="false" direction="ltr">{"".join(g)}</svg>', notes


def state_key(v: dict, vals: list) -> str:
    """The evidence states drawn, each with its mark form, its governed label and the x-range it covers (and the
    source document, where the rows carry a series label)."""
    seen, items = [], []
    for r in vals:
        if r.get("y") is None:
            continue
        key = (r["state"], r.get("series_label") or "")
        if key in seen:
            continue
        seen.append(key)
        rng = [str(x["x"]) for x in vals if (x["state"], x.get("series_label") or "") == key]
        span = rng[0] if len(rng) == 1 else f"{rng[0]}–{rng[-1]}"
        glyph = {"circle": "●", "square": "■", "hollow": "○"}[MARK_SHAPE.get(r["state"], "circle")]
        dash = " ╌" if r["state"] == "PROJECTED" else ""
        doc = f' · <span dir="auto">{esc(r["series_label"])}</span>' if r.get("series_label") else ""
        items.append(f'<li><span class="glyph" aria-hidden="true">{glyph}{dash}</span> <b>{esc(state_label(v, r["state"]))}</b> · {bdi(span)}{doc}</li>')
    return f'<ul class="key">{"".join(items)}</ul>'


def note_lines(notes: list, method: str = "") -> str:
    items = []
    for kind, where, label in notes:
        glyph = {"brk": "‖", "miss": "┆", "dis": "◎"}[kind]
        items.append(f'<li class="{kind}"><span class="glyph" aria-hidden="true">{glyph}</span> {bdi(where)} · <b>{esc(label)}</b></li>')
    if any(k == "dis" for k, _, _ in notes) and method:
        items.append(f'<li class="dis-note">{esc(method)}</li>')
    return f'<ul class="marks">{"".join(items)}</ul>' if items else ""


def ts_table(v: dict, series: dict, caption: str, unit: str, extra_col: str = "") -> str:
    rows = []
    missing = {str(m["x"]): m.get("marker") for m in series.get("missing_x") or []}
    xs = sorted({str(r["x"]) for r in series["values"]} | set(missing))
    by_x = {str(r["x"]): r for r in series["values"]}
    for x in xs:
        r = by_x.get(x)
        if r is None:
            rows.append([bdi(x), esc(marker_label(v, missing[x] or "MISSING")), "", ""])
            continue
        note = "; ".join(marker_label(v, m) for m in r["markers"] if marker_label(v, m))
        parts = [esc(note)] + ([f'<span dir="auto">{esc(r["series_label"])}</span>'] if r.get("series_label") else [])
        rows.append([bdi(x), num(r["y"]), esc(state_label(v, r["state"])), " · ".join(x for x in parts if x)])
    return table(caption, ["", esc(unit), "", ""], rows)


def remittance_macro(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    s = v["series"][0]
    svg, notes = line_panel(v, s, "macro")
    unit = s["values"][0]["unit"]
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(unit)}</p>{svg}{state_key(v, s["values"])}{note_lines(notes)}</div></div>'
    tbl = ts_table(v, s, caption_of(v, esc(unit)), unit)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl)


def pos_panel(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """One panel of the POS small multiple (the three visuals share a time axis form but never a value axis)."""
    s = v["series"][0]
    svg, notes = line_panel(v, s, v["id"])
    unit = s["values"][0]["unit"]
    nominal = f' · {esc(marker_label(v, "NOMINAL"))}' if "NOMINAL" in (s.get("markers") or []) else ""
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(unit)}{nominal}</p>{svg}{state_key(v, s["values"])}{note_lines(notes, v.get("record_method") or "")}</div></div>'
    tbl = ts_table(v, s, caption_of(v, esc(unit)), unit)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl)


# ------------------------------------------------------------------------------------------------ dot rows (VIS-REMITTANCE-COST)
def remittance_cost(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    vals = v["series"][0]["values"]
    vmax, step = axis_scale([r["y"] for r in vals])
    corridors = list(dict.fromkeys(r["x_text"] for r in vals))
    shapes = {}
    html_ = [f'<div class="panel bars"><p class="ph">{esc(vals[0]["unit"])} · {esc(state_label(v, "MEASURED"))}</p>']
    for c in corridors:
        rows = []
        for r in [x for x in vals if x["x_text"] == c]:
            shape = shapes.setdefault(r.get("group"), ["circle", "square", "ring"][len(shapes) % 3])
            x = _pct(r["y"], vmax=vmax)
            rows.append(f'<div class="row"><div class="rl">{esc(r["group_text"])}</div><svg class="trk" width="100%" height="34" aria-hidden="true" focusable="false" direction="ltr">'
                        f'<line class="stem" x1="1%" y1="22" x2="{x:.2f}%" y2="22"/>{svg_mark(shape, f"{x:.2f}%", 22, 6)}<text class="val" x="{x:.2f}%" y="9" text-anchor="middle">{plain_num(r["y"])}</text></svg></div>')
        html_.append(f'<div class="lane"><h3>{esc(c)}</h3><div class="p1">{"".join(rows)}</div></div>')
    html_.append('<div class="p1">' + axis_row(vmax, step) + "</div></div>")
    rows = [[esc(r["x_text"]), esc(r["group_text"]), num(r["y"]), esc(r["unit"])] for r in vals]
    tbl = table(caption_of(v), ["", "", esc(vals[0]["unit"]), ""], rows)
    return frame_open(v, heading) + f'<div class="panels">{"".join(html_)}</div>' + frame_close(v, cite_label, origin, tbl)


# ------------------------------------------------------------------------------------------------ objects (VIS-PAYMENT-ANATOMY)
def payment_anatomy(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    vals = v["series"][0]["values"]
    withheld_label = marker_label(v, "WITHHELD")
    nc_label = marker_label(v, "NOT_COMPARABLE")
    items = []
    for r in vals:
        if r.get("withheld") or r.get("y") is None:
            value = f'<span class="withheld">{esc(withheld_label)}</span>'
        else:
            value = num(r["y"]) + (f' <span class="unit-l">{esc(r["unit"])}</span>' if r["unit"] != vals[0]["unit"] else "")
        marks = "".join(f'<span class="mk">{esc(marker_label(v, m))}</span>' for m in r["markers"] if m != "WITHHELD" and marker_label(v, m))
        marks_html = f'<div class="mks">{marks}</div>' if marks else ""
        items.append(f'<li class="obj-card"><span class="rubric">{esc(r["x_text"])}</span><div class="v">{value}</div><div class="isnot">{esc(r["is_not_text"])}</div>{marks_html}</li>')
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(vals[0]["unit"])} · {esc(state_label(v, "ADMINISTRATIVE"))}</p><ol class="anatomy">{"".join(items)}</ol></div></div>'
    rows = [[esc(r["x_text"]), (esc(withheld_label) if r.get("withheld") or r.get("y") is None else num(r["y"])), esc(r["is_not_text"]), esc("; ".join(marker_label(v, m) for m in r["markers"] if m != "WITHHELD"))] for r in vals]
    tbl = table(caption_of(v), ["", esc(vals[0]["unit"]), "", ""], rows)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl)


# ------------------------------------------------------------------------------------------------ the chain (RV-CWR-009, VIS-PAYMENT-RAILS)
CHAIN_STEPS = ["RULE", "IMPLEMENTATION", "OPERATION", "ACCESS", "USE", "QUALITY", "OUTCOME"]
# The governed step mapping of RV-CWR-009 (`contract.step_mapping`), read as event class → chain step.
CLASS_STEP = {"NETWORK_RULE": "RULE", "PAYMENTS_ARCHITECTURE_DECISION": "RULE", "PROJECT_START": "RULE", "PAYMENT_RAIL_COMPONENT": "RULE", "ACCESS_USAGE_COMPONENT": "RULE",
              "NETWORK_INTEGRATION": "IMPLEMENTATION", "UNIFIED_NETWORK_COMPANY": "IMPLEMENTATION", "YPCC": "IMPLEMENTATION", "NETWORK_ACTIVITY_SIGNAL": "OPERATION"}
ACTIVITY_STEP = {"OBS-00080": "IMPLEMENTATION", "OBS-00081": "OPERATION"}


def chain_steps(chain_src: dict, include_activity: bool) -> list[dict]:
    events = chain_src["objects"].get("reform_events") or []
    activity = chain_src["objects"].get("pos_activity") or [] if include_activity else []
    steps = []
    for st in CHAIN_STEPS:
        evs = sorted([e for e in events if CLASS_STEP.get(e.get("class")) == st], key=lambda e: str(e.get("date")))
        acts = [a for a in activity if ACTIVITY_STEP.get(a["id"]) == st]
        steps.append({"step": st, "events": evs, "activity": acts, "evidenced": bool(evs or acts)})
    return steps


def chain_figure(v: dict, chain_src: dict, cite_label: str, origin: str | None, heading: str = "h2", include_activity: bool = True) -> str:
    """The transmission chain, top to bottom: each governed step EVIDENCED (its dated events, each with its source
    locator) or OPEN (never a failure, never a percentage); the first open step after the evidenced ones is where the
    evidence stops and is set in the boundary voice."""
    L = v["chain_labels"]
    steps = chain_steps(chain_src, include_activity)
    first_open = next((i for i, s in enumerate(steps) if not s["evidenced"]), None)
    items = []
    for i, s in enumerate(steps):
        state = L["EVIDENCED"] if s["evidenced"] else L["OPEN"]
        cls = "step " + ("evidenced" if s["evidenced"] else "open") + (" stop" if i == first_open else "")
        evs = "".join(f'<li><span class="clock"><span class="v">{bdi(e.get("date"))}</span></span><span class="ev">{esc(e["label_text"])}</span>'
                      + (f' <a class="source-locator" href="{esc(e["source"])}" rel="noopener noreferrer" target="_blank" aria-label="{esc(v["labels"]["source"])} {esc(e["label_text"])}">↗</a>' if str(e.get("source", "")).startswith("http") else "")
                      + "</li>" for e in s["events"])
        evs += "".join(f'<li><span class="clock"><span class="v">{bdi(a.get("x"))}</span></span><span class="ev">{esc(a["label_text"])} · {num(a["y"])} {esc(a["unit"])}</span></li>' for a in s["activity"])
        items.append(f'<li class="{cls}"><div class="st-head"><span class="glyph" aria-hidden="true">{"■" if s["evidenced"] else "□"}</span><h3>{esc(L[s["step"]])}</h3><span class="st-state">{esc(state)}</span></div>'
                     + (f'<ul class="evs">{evs}</ul>' if evs else "") + "</li>")
    panel = f'<div class="panels"><div class="panel"><ol class="chain">{"".join(items)}</ol></div></div>'
    rows = []
    for s in steps:
        state = L["EVIDENCED"] if s["evidenced"] else L["OPEN"]
        ev_text = "; ".join(f'{e.get("date")} {e["label_text"]}' for e in s["events"]) + ("; " if s["events"] and s["activity"] else "") + "; ".join(f'{a.get("x")} {a["label_text"]} {plain_num(a["y"])} {a["unit"]}' for a in s["activity"])
        rows.append([esc(L[s["step"]]), esc(state), esc(ev_text)])
    tbl = table(caption_of(v), ["", "", ""], rows)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl)


def rv009_figure(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    return chain_figure(v, v, cite_label, origin, heading, include_activity=True)


def payment_rails(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """SUPPORTING: the chain as a non-quantitative state diagram built from the governed chain labels and the
    deduplicated event set of RV-CWR-009 (its rationale asks for exactly that reuse); no value is plotted."""
    src = v.get("_chain_source")
    if not src:
        return text_frame(v, cite_label, origin, heading)
    return chain_figure(v, src, cite_label, origin, heading, include_activity=False)


DRAWERS = {"VIS-FINDEX-GAPS": findex_gaps, "VIS-REMITTANCE-MACRO": remittance_macro, "VIS-POS-TERMINALS": pos_panel, "VIS-POS-TRANSACTIONS": pos_panel,
           "VIS-POS-VALUE": pos_panel, "VIS-REMITTANCE-COST": remittance_cost, "VIS-PAYMENT-ANATOMY": payment_anatomy, "RV-CWR-009": rv009_figure,
           "VIS-PAYMENT-RAILS": payment_rails}
