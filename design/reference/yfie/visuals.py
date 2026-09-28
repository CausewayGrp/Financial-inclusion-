# -*- coding: utf-8 -*-
"""Visual contracts for the reference implementation — D1: RV-CWR-001 in the converged form (design/01_FOUNDATIONS.md
§3.3, §4.1 item 5). Every drawing uses percentage x-coordinates on an SVG without a viewBox, so the figure follows its
column at every width without scaling its text and needs no inline style (strict CSP). Numeric value and time axes run
left to right in both languages (governed contract rule); labels, legends and panel order follow the reading direction.
The text alternative (alt text plus the contract's tables) ships visibly with the chart."""
from __future__ import annotations

from .text import ISO_DATE, bdi, esc, iso as iso_run  # noqa: F401  (one text layer for every renderer, D6)


def plain_num(x, year: bool = False) -> str:
    """One number rule: Western digits, thousands separators on every value, years never separated, precision as
    governed (no trailing .0). A governed value that is not a number prints escaped, never as markup."""
    if year:
        return esc(x)
    if isinstance(x, bool):
        return esc(x)
    if isinstance(x, float):
        return f"{int(x):,}" if x.is_integer() else f"{x:,}"   # the shortest exact representation, thousands separated
    if isinstance(x, int):
        return f"{x:,}"
    return esc(x)


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
    t1 = (f'<table class="{cls}"><caption>{cap} — {num(d["panel1"][0]["x"], year=True)} · {esc(d["unit_usd"])} · {esc(L["reported"])}</caption><thead><tr><th scope="col">{esc(L["source"])}</th><th scope="col">{esc(d["unit_usd"])}</th></tr></thead><tbody>'
          + "".join(f'<tr><th scope="row">{esc(r["series_label"])}</th><td class="num">{num(r["y"])}</td></tr>' for r in d["panel1"])
          + f'<tr><td colspan="2" class="marker">{esc(L["same_year_revision"])}</td></tr></tbody></table>')
    # Panel 2: one table per lane. The two indexed paths are separate series that never share a value axis (Lock §4.1.5),
    # so they never share a row either; the governed not-comparable label stands between the two tables. Three columns
    # fit 288 px without scrolling (D6, closes DEBT-010 for this figure).
    lanes = []
    for label, series, index in ((d["label_cby"], d["cby"], d["cby_index"]), (d["label_imf"], d["imf"], d["imf_index"])):
        rows = "".join(f'<tr><th scope="row">{yr}</th><td class="num">{num(next(r for r in series if r["x"] == yr)["y"])}</td><td class="num">{num(index[yr]["value"])}</td></tr>' for yr in (2021, 2022, 2023, 2024))
        lanes.append(f'<table class="{cls}"><caption>{cap} — <span dir="auto">{esc(label)}</span> — {esc(d["unit_index"])} · {esc(L["derived"])}</caption><thead>'
                     f'<tr><th scope="col"></th><th scope="col">{esc(d["unit_usd"])}</th><th scope="col">{esc(d["unit_index"])}</th></tr></thead><tbody>{rows}</tbody></table>')
    return t1 + lanes[0] + f'<p class="marker between-tables">{esc(L["not_comparable"])}</p>' + lanes[1]


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
    """One filled mark per publication or group, the same in every panel: ● circle, ■ square, ◆ diamond. Filled
    shapes only — a hollow mark means an estimate or a projection in the state grammar and nothing else (D6). Drawn
    from percentage x; the diamond is a square rotated about its own box by the stylesheet (no absolute x needed)."""
    if kind == "circle":
        return f'<circle class="mark a" cx="{x}" cy="{cy}" r="{r}"/>'
    if kind == "square":
        return f'<rect class="mark a" x="{x}" y="{cy-r}" width="{2*r}" height="{2*r}" transform="translate(-{r},0)"/>'
    side = round(2 * r * 0.8, 1)
    return f'<g transform="translate(-{side/2:.1f},0)"><rect class="mark a dia" x="{x}" y="{cy-side/2:.1f}" width="{side}" height="{side}"/></g>'


def p1_rows(d: dict, same_year: str) -> str:
    """Panel 1 as rows: one row per publication keyed by its governed label (HTML, so it wraps and mirrors), the value
    on a horizontal axis from zero, the value printed above the mark; the governed same-year marker stands between the
    two rows (the contract places the break between the two values), so a crop of the rows never reads as a fall.
    The axis end and its ticks come from the data."""
    vmax, step = axis_scale([v["y"] for v in d["panel1"]])
    rows = []
    for val, kind in ((d["panel1"][0], "circle"), (d["panel1"][1], "square")):
        x = _pct(val["y"], vmax=vmax)
        track = (f'<svg class="trk" width="100%" height="38" aria-hidden="true" focusable="false" direction="ltr">'
                 f'<line class="stem" x1="1%" y1="26" x2="{x:.2f}%" y2="26"/>{svg_mark(kind, f"{x:.2f}%", 26, 7)}'
                 f'<text class="val" x="{x:.2f}%" y="11" text-anchor="middle">{plain_num(val["y"])}</text></svg>')
        rows.append(f'<div class="row"><div class="rl">{esc(val["series_label"])}</div>{track}</div>')
    rows.insert(1, f'<div class="between same"><b>{esc(same_year)}</b></div>')
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
    def x(yr): return 17 + 74 * (xs.index(yr) / (len(xs) - 1))   # inset: the first mark clear of the axis
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


def frame_foot(v: dict, cite_label: str, origin: str | None, open_label: str | None = None) -> str:
    """The detached frame's foot, the same on every figure and in every export (D6, `06_VISUAL_TABLE_SYSTEM.md` §2):
    the governed prohibited inference under the governed "What not to conclude" label (UI-DOM-WHAT-NOT-TO-CONCLUDE, the
    label the baseline prints for every visual — D3; the governed alt text carries its own "Does not establish:"),
    the credit as an isolated left-to-right run, the canonical link (absolute once the
    deployment origin is set), the edition of the resource, and the cite action. A crop that loses any line is not a
    supported export."""
    L = v["labels"]
    canon = (origin or "") + v["canonical_href"]
    credit = f'<p>{credit_line(v)}</p>' if v.get("credit") else ""
    link = (f'<a class="canon" dir="ltr" href="{esc(v["canonical_href"])}">{esc(canon)}</a>' if not open_label
            else f'<a class="canon-l" href="{esc(v["canonical_href"])}">{esc(open_label)}</a>')
    return (f'<div class="foot"><p class="b"><b>{esc(L["what_not_to_conclude"])}:</b> {iso_run(v["prohibited_inference"])}</p>{credit}'
            f'<p>{esc(L["full_record"])} {link} ·\u00a0<span class="ed">{esc(v.get("edition") or "")}</span>'
            f'<span class="cite-sep"> ·\u00a0<button type="button" class="tbtn" data-cite>{esc(cite_label)}</button></span></p></div>')


def rv001_figure(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """The whole figure object: frame (rubric, title, question, scope), panel 1 rows, panel 2 lanes with the
    not-comparable divider between them, the in-frame note, the frame foot (boundary, credit, canonical link, edition,
    cite), then the visible text alternative."""
    d = rv001_data(v); f = rv001_frame_lines(v); sub = sub_heading(heading)
    def base(series):
        r = next(r for r in series if r["x"] == 2021)
        return f'<span class="base">2021 · {num(r["y"])} {esc(r["unit"])}</span>'
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(v["labels"]["analytical_question"])}</span><{heading} class="fig-t">{esc(f["title"])}</{heading}><p class="cap">{esc(v["question"])}</p><p class="cap">{iso_run(f["scope"])}</p>'
            f'<div class="panels"><div class="panel p1p"><p class="ph">2024 · {esc(d["unit_usd"])} · {esc(v["labels"]["reported"])}</p>{p1_rows(d, f["same_year"])}</div>'
            f'<div class="panel p2">'
            f'<div class="lanes"><div class="lane"><{sub}>{esc(d["label_cby"])}</{sub}><p class="ph">{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</p>{base(d["cby"])}{lane(d["cby_index"], "square")}</div><div class="between">{esc(f["not_comparable"])}</div>'
            f'<div class="lane"><{sub}>{esc(d["label_imf"])}</{sub}><p class="ph">{esc(d["unit_index"])} · {esc(v["labels"]["derived"])}</p>{base(d["imf"])}{lane(d["imf_index"], "diamond")}</div></div><p class="cap note">{esc(f["note"])}</p></div></div>'
            + frame_foot(v, cite_label, origin)
            + f'<div class="alt" data-visual-fallback="ordered-text"><{sub} class="alt-h">{esc(v["labels"]["text_alternative"])}</{sub}>'
            f'<p class="small"><b>{esc(v["labels"]["what_it_shows"])}</b> {iso_run(v["alt_text"])}</p><p class="small"><b>{esc(v["labels"]["scope"])}:</b> {iso_run(f["scope"])}</p>'
            + table_region(v, rv001_tables(d, v)) + "</div>"
            + f'<figcaption class="sr-only">{iso_run(v["title"])}</figcaption></figure>')


FIGURES = {"RV-CWR-001": rv001_figure}


def credit_line(v: dict) -> str:
    """The governed credit. Publisher names are governed in English only; Arabic frames print them as isolated
    left-to-right runs (the contract's `credit.language_note`)."""
    return f'{esc(v["labels"]["source"])} <bdi dir="ltr" lang="en">{esc(v.get("credit") or "")}</bdi>'


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
    # A text frame has no view: the governed description is the frame's body, so its heading ("Text description of this
    # view") stays in the accessibility tree only, and the boundary is printed once, in the foot (D3, cold-reader test;
    # the label itself is escalated — ESCALATIONS.md, text-first tiers). The foot is the detached frame's (D6).
    return (f'<figure class="fig fig-text" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(rub)}</span><{heading} class="fig-t">{esc(v["title"])}</{heading}>'
            f'<p class="cap">{esc(v["question"])}</p>'
            f'<div class="alt alt-body" data-visual-fallback="ordered-text"><{sub_heading(heading)} class="alt-h sr-only">{esc(v["labels"]["text_alternative"])}</{sub_heading(heading)}><p class="body"><b>{esc(v["labels"]["what_it_shows"])}</b> {iso_run(v["alt_text"])}</p>'
            + (f'<p class="small"><b>{esc(v["labels"]["scope"])}:</b> {iso_run(scope)}</p>' if scope else "")
            + '</div>' + frame_foot(v, cite_label, origin, open_label) + '</figure>')


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


def sub_heading(heading: str) -> str:
    """The level of a figure's inner headings (lanes, steps, classes, the text alternative): one under its title."""
    return f"h{min(6, int(heading[1]) + 1)}"


def frame_open(v: dict, heading: str, panel_head: str = "") -> str:
    scope = " · ".join(x for x in (v.get("period"), v.get("universe")) if x)
    return (f'<figure class="fig" data-visual-id="{esc(v["id"])}" {FIG_ATTRS}><span class="rubric">{esc(v["labels"]["analytical_question"])}</span>'
            f'<{heading} class="fig-t">{esc(v["title"])}</{heading}><p class="cap">{esc(v["question"])}</p><p class="cap">{iso_run(scope)}</p>{panel_head}')


def frame_close(v: dict, cite_label: str, origin: str | None, tables: str, notes: str = "", key: str = "", heading: str = "h2") -> str:
    L = v["labels"]; sub = sub_heading(heading)
    scope = " · ".join(x for x in (v.get("period"), v.get("universe")) if x)
    frame_notes = "".join(f'<p class="cap note">{esc(t)}</p>' for t in (v.get("frame_labels") or {}).values() if t) if not v.get("_frame_notes_drawn") else ""
    table_html = table_region(v, tables) if tables else ""
    # The boundary is printed once per frame, in the boundary voice, in the detached frame's foot; the text alternative
    # below carries what the view shows, its scope and the contract's table — never a second copy of the boundary (D3,
    # cold-reader test; D6: one foot for every figure and export).
    return (f'{key}{notes}{frame_notes}' + frame_foot(v, cite_label, origin)
            + f'<div class="alt" data-visual-fallback="ordered-text"><{sub} class="alt-h">{esc(L["text_alternative"])}</{sub}>'
            f'<p class="small"><b>{esc(L["what_it_shows"])}</b> {iso_run(v["alt_text"])}</p><p class="small"><b>{esc(L["scope"])}:</b> {iso_run(scope)}</p>'
            f'{table_html}</div>'
            f'<figcaption class="sr-only">{iso_run(v["title"])}</figcaption></figure>')   # the figure's name is its governed title; the visible alt block is its description


NUMERIC = __import__("re").compile(r'^(?:<bdi dir="ltr">)?[\d,.]+(?:</bdi>)?$')


def table(caption: str, head: list, rows: list, cls: str = "rvtab", foot: str = "") -> str:
    """The fallback table: caption, scoped headers, numeric cells marked (`td.num` keeps its run unbroken; text cells
    wrap). Every data column is headed by a governed string (the corner cell above the row headers may be empty);
    a qualifier that holds for every row (state, unit, marker, document) is stated once in the caption and one that
    varies travels in the value's own cell, so a table is two or three columns wide and fits 256 px without scrolling
    (D6, closes DEBT-010 for every drawn contract but the declared-wide matrix)."""
    if any(not str(h).strip() for h in head[1:]):
        raise ValueError(f"a fallback table has an unnamed data column: {head}")
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = "".join("<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 else (f'<td class="num">{c}</td>' if NUMERIC.match(str(c)) else f"<td>{c}</td>")) for i, c in enumerate(r)) + "</tr>" for r in rows)
    foot_html = f'<tr><td colspan="{len(head)}" class="marker">{foot}</td></tr>' if foot else ""
    return f'<table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}{foot_html}</tbody></table>'


def grouped_table(caption: str, head: list, groups: list, cls: str = "rvtab") -> str:
    """A fallback table whose rows fall into named groups: each group is its own `tbody` opened by a row-group header
    (`th[scope=rowgroup]` spanning the table), then its rows as in `table()`."""
    if any(not str(h).strip() for h in head[1:]):
        raise ValueError(f"a fallback table has an unnamed data column: {head}")
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    bodies = []
    for gh, rows in groups:
        body = "".join("<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 else (f'<td class="num">{c}</td>' if NUMERIC.match(str(c)) else f"<td>{c}</td>")) for i, c in enumerate(r)) + "</tr>" for r in rows)
        group_row = f'<tr><th scope="rowgroup" colspan="{len(head)}" class="rg">{gh}</th></tr>' if gh else ""
        bodies.append(f"<tbody>{group_row}{body}</tbody>")
    return f'<table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead>{"".join(bodies)}</table>'


def caption_of(v: dict, extra: str = "") -> str:
    parts = [iso_run(v["title"]), iso_run(v.get("period") or ""), iso_run(v.get("universe") or "")]
    return " — ".join(p for p in parts if p) + (f" — {extra}" if extra else "")


def qual(*parts) -> str:
    """A value with its qualifiers, or a caption's qualifiers: the non-empty parts joined by the middle dot."""
    return " · ".join(str(x) for x in parts if x)


def uniform(rows: list, key) -> str | None:
    """The one value `key` takes on every row, or None when it varies or is absent."""
    vals = {key(r) for r in rows}
    return vals.pop() if len(vals) == 1 and None not in vals and "" not in vals else None


def table_region(v: dict, tables: str) -> str:
    """The named region a fallback table sits in; focusable only when the table is declared wide and can scroll (a
    table that fits its column is never an idle tab stop)."""
    tab = ' tabindex="0"' if 'class="rvtab wide"' in tables else ""
    return f'<div class="table-wrap"{tab} role="region" aria-label="{esc(v["labels"]["text_alternative"])}: {esc(v["title"])}">{tables}</div>'


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
    state = uniform(vals, lambda r: r["state"])
    rows = [[esc(r["x_text"]), qual(num(r["y"]), esc(r["unit"]) if r["unit"] != common_unit else "", "" if state else esc(state_label(v, r["state"])))] for r in vals]
    gap_unit = uniform([d for d, _, _ in pairs], lambda d: d.get("unit")) or ""
    gaps = [[esc(f'{by_id[d["from"][0]]["x_text"]} − {by_id[d["from"][1]]["x_text"]}'), qual(num(d["value"]), "" if gap_unit else esc(d.get("unit") or ""))] for d, _, _ in pairs]
    tbl = grouped_table(caption_of(v, qual(esc(common_unit), esc(state_label(v, state)) if state else "")), ["", esc(common_unit)],
                        [(None, rows), (qual(esc(gap_unit), esc(derived_label)), gaps)])   # the gaps: their own unit and the DERIVED state as the group's header, the pair as the row
    return frame_open(v, heading) + f'<div class="panels">{"".join(html_)}</div>' + frame_close(v, cite_label, origin, tbl, heading=heading)


# ------------------------------------------------------------------------------------------------ time-series lines
def line_panel(v: dict, series: dict, panel_id: str, height: int = 200) -> tuple[str, list]:
    """One line panel: the governed values on a zero-based value axis with a left-to-right time axis; marks keyed by
    evidence state (filled = reported/administrative/measured, hollow = estimated/projected; square = administrative);
    a projected segment dashed; a BREAK never joined and marked; a MISSING x a labelled gap; DISAGREEMENT ringed.
    Where the series changes state, each state's governed label stands on the panel above its segment (a plot-only
    crop keeps its states; hidden under narrow containers, where the key directly under the plot carries them). Value
    labels: the first starts at its mark and the last ends at it, a label beside a break keeps to its side of the rule,
    and a dense series alternates two rows by the distance to its neighbour so labels never meet. Returns the SVG and
    the list of note lines (break, missing, disagreement) for the HTML under it."""
    vals = series["values"]
    xs = sorted({str(r["x"]) for r in vals} | {str(m["x"]) for m in series.get("missing_x") or []})
    top, step = axis_scale([r["y"] for r in vals if r.get("y") is not None])
    valued = [r for r in vals if r.get("y") is not None]
    segments: list = []   # runs of consecutive valued points with the same state
    for r in valued:
        if segments and segments[-1][0] == r["state"]:
            segments[-1][1].append(r)
        else:
            segments.append([r["state"], [r]])
    band = 13 * len(segments) if len(segments) > 1 else 0
    height += band
    lo, hi = 24 + band, height - 36
    def X(x): return 16 + 80 * (xs.index(str(x)) / max(1, len(xs) - 1))   # inset: the first mark clear of the axis; a 12 % margin keeps the axis labels whole at 320 px
    def Y(y): return lo + (hi - lo) * (1 - y / top)
    g = [f'<line class="axis" x1="12%" y1="{lo}" x2="12%" y2="{hi}"/>', f'<line class="axis" x1="12%" y1="{hi}" x2="96%" y2="{hi}"/>']
    t = step
    while t <= top + 1e-9:
        g.append(f'<line class="grid" x1="12%" y1="{Y(t):.1f}" x2="96%" y2="{Y(t):.1f}"/><text class="lbl" x="10.5%" y="{Y(t)+4:.1f}" text-anchor="end">{plain_num(int(t) if float(t).is_integer() else t)}</text>')
        t += step
    g.append(f'<text class="lbl origin" x="10.5%" y="{hi+4}" text-anchor="end">0</text>')
    for i, x in enumerate(xs):
        cls = "lbl" if (i in (0, len(xs) - 1) or len(xs) <= 7 or i % 2 == 0) else "lbl alt"
        g.append(f'<text class="{cls}" x="{X(x):.2f}%" y="{hi+18}" text-anchor="middle">{esc(x)}</text>')
    missing = {str(m["x"]): m.get("marker") for m in series.get("missing_x") or []}
    break_before = {i for i, r in enumerate(valued) if any(m.startswith("BREAK") for m in r["markers"])}
    notes = []
    prev = None
    prev_label_y = None
    dense = len(vals) > 8
    for i, r in enumerate(valued):
        x, y = X(r["x"]), Y(r["y"])
        broken = i in break_before
        gap_between = prev is not None and any(xs.index(str(prev["x"])) < xs.index(mx) < xs.index(str(r["x"])) for mx in missing)
        if prev is not None and not broken and not gap_between:
            dashed = r["state"] == "PROJECTED" or prev["state"] == "PROJECTED"
            g.append(f'<line class="path{" dashed" if dashed else ""}" x1="{X(prev["x"]):.2f}%" y1="{Y(prev["y"]):.1f}" x2="{x:.2f}%" y2="{y:.1f}"/>')
        if broken and prev is not None:
            bx = (X(prev["x"]) + x) / 2
            g.append(f'<line class="brk" x1="{bx-0.4:.2f}%" y1="{lo}" x2="{bx-0.4:.2f}%" y2="{hi}"/><line class="brk" x1="{bx+0.4:.2f}%" y1="{lo}" x2="{bx+0.4:.2f}%" y2="{hi}"/>')
            for m in r["markers"]:
                if m.startswith("BREAK"):
                    notes.append(("brk", (str(prev["x"]), str(r["x"])), marker_label(v, m)))
        shape = MARK_SHAPE.get(r["state"], "circle")
        mark = {"circle": svg_mark("circle", f"{x:.2f}%", round(y, 1), 5), "square": f'<rect class="mark a" x="{x:.2f}%" y="{y-5:.1f}" width="10" height="10" transform="translate(-5,0)"/>',
                "hollow": f'<circle class="mark b" cx="{x:.2f}%" cy="{y:.1f}" r="5"/>'}[shape]
        if "DISAGREEMENT" in r["markers"]:
            mark += f'<circle class="ring" cx="{x:.2f}%" cy="{y:.1f}" r="9"/>'
        g.append(mark)
        own_marks = [m for m in r["markers"] if m not in (series.get("markers") or [])]   # a series-wide marker (NOMINAL) marks no point
        keep = (i == 0 or i == len(valued) - 1 or own_marks or (prev is not None and prev["state"] != r["state"]))
        rows = [y - 12, y - 26] if dense else [y - 12]
        ly = rows[0] if prev_label_y is None else max(rows, key=lambda c: abs(c - prev_label_y))
        anchor, dx = "middle", 0.0
        if i == 0:
            anchor, dx = "start", -0.8
        elif i == len(valued) - 1:
            anchor, dx = "end", 0.8
        if (i + 1) in break_before:
            anchor, dx = "end", 0.8
        elif i in break_before:
            anchor, dx = "start", -0.8
        g.append(f'<text class="val{" dense" if dense and not keep else ""}" x="{x + dx:.2f}%" y="{ly:.1f}" text-anchor="{anchor}">{plain_num(r["y"])}</text>')
        prev = r
        prev_label_y = ly
    for mx, marker in missing.items():
        x = X(mx)
        g.append(f'<line class="miss" x1="{x:.2f}%" y1="{lo+20}" x2="{x:.2f}%" y2="{hi}"/>')
        notes.append(("miss", mx, marker_label(v, marker or "MISSING")))
    dis = [str(r["x"]) for r in vals if "DISAGREEMENT" in r["markers"]]
    if dis:
        notes.append(("dis", ", ".join(dis), marker_label(v, "DISAGREEMENT")))
    if band:
        for k, (state, rs) in enumerate(segments):
            sx = X(rs[0]["x"])
            anchor = "start" if sx < 40 else ("end" if sx > 60 else "middle")
            g.append(f'<text class="lbl st" x="{sx:.2f}%" y="{10 + 13 * k}" text-anchor="{anchor}">{esc(state_label(v, state))}</text>')
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
        at = " · ".join(bdi(w) for w in where) if isinstance(where, tuple) else bdi(where)   # a break: the period before and the period after, no arrow
        items.append(f'<li class="{kind}"><span class="glyph" aria-hidden="true">{glyph}</span> {at} · <b>{esc(label)}</b></li>')
    if any(k == "dis" for k, _, _ in notes) and method:
        items.append(f'<li class="dis-note">{esc(method)}</li>')
    return f'<ul class="marks">{"".join(items)}</ul>' if items else ""


def ts_table(v: dict, series: dict, unit: str) -> str:
    """A time series as period × value: the value's state, markers and source document travel in its cell when they
    vary between rows and stand once in the caption when they do not; a missing period prints its governed marker."""
    rows = []
    vals = series["values"]
    missing = {str(m["x"]): m.get("marker") for m in series.get("missing_x") or []}
    xs = sorted({str(r["x"]) for r in vals} | set(missing))
    by_x = {str(r["x"]): r for r in vals}
    state = uniform(vals, lambda r: r["state"])
    doc = uniform(vals, lambda r: r.get("series_label"))
    shared = set.intersection(*[set(r["markers"]) for r in vals]) if vals else set()   # a marker every valued row carries (NOMINAL) stands once in the caption
    for x in xs:
        r = by_x.get(x)
        if r is None:
            rows.append([bdi(x), esc(marker_label(v, missing[x] or "MISSING"))])
            continue
        marks = "; ".join(marker_label(v, m) for m in r["markers"] if m not in shared and marker_label(v, m))
        rows.append([bdi(x), qual(num(r["y"]), esc(marks), "" if state else esc(state_label(v, r["state"])),
                                  f'<span dir="auto">{esc(r["series_label"])}</span>' if r.get("series_label") and not doc else "")])
    caption = caption_of(v, qual(esc(unit), esc(state_label(v, state)) if state else "", f'<span dir="auto">{esc(doc)}</span>' if doc else "",
                                 esc("; ".join(marker_label(v, m) for m in sorted(shared) if marker_label(v, m)))))
    return table(caption, ["", esc(unit)], rows)


def remittance_macro(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    s = v["series"][0]
    svg, notes = line_panel(v, s, "macro")
    unit = s["values"][0]["unit"]
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(unit)}</p>{svg}{state_key(v, s["values"])}{note_lines(notes)}</div></div>'
    tbl = ts_table(v, s, unit)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


def pos_panel(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """One panel of the POS small multiple (the three visuals share a time axis form but never a value axis)."""
    s = v["series"][0]
    svg, notes = line_panel(v, s, v["id"])
    unit = s["values"][0]["unit"]
    nominal = f' · {esc(marker_label(v, "NOMINAL"))}' if "NOMINAL" in (s.get("markers") or []) else ""
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(unit)}{nominal}</p>{svg}{state_key(v, s["values"])}{note_lines(notes, v.get("record_method") or "")}</div></div>'
    tbl = ts_table(v, s, unit)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


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
            shape = shapes.setdefault(r.get("group"), ["circle", "square", "diamond"][len(shapes) % 3])
            x = _pct(r["y"], vmax=vmax)
            rows.append(f'<div class="row"><div class="rl">{esc(r["group_text"])}</div><svg class="trk" width="100%" height="34" aria-hidden="true" focusable="false" direction="ltr">'
                        f'<line class="stem" x1="1%" y1="22" x2="{x:.2f}%" y2="22"/>{svg_mark(shape, f"{x:.2f}%", 22, 6)}<text class="val" x="{x:.2f}%" y="9" text-anchor="middle">{plain_num(r["y"])}</text></svg></div>')
        html_.append(f'<div class="lane"><h3>{esc(c)}</h3><div class="p1">{"".join(rows)}</div></div>')
    html_.append('<div class="p1">' + axis_row(vmax, step) + "</div></div>")
    state = uniform(vals, lambda r: r["state"])
    rows = [[f'{esc(r["x_text"])} — {esc(r["group_text"])}', qual(num(r["y"]), "" if state else esc(state_label(v, r["state"])))] for r in vals]
    tbl = table(caption_of(v, qual(esc(vals[0]["unit"]), esc(state_label(v, state)) if state else "")), ["", esc(vals[0]["unit"])], rows)
    return frame_open(v, heading) + f'<div class="panels">{"".join(html_)}</div>' + frame_close(v, cite_label, origin, tbl, heading=heading)


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
        items.append(f'<li class="obj-card"><span class="rubric">{esc(r["x_text"])}</span><div class="v">{value}</div><p class="cl2">{iso_run(v.get("period") or "")} · {esc(state_label(v, "ADMINISTRATIVE"))}</p><div class="isnot">{esc(r["is_not_text"])}</div>{marks_html}</li>')
    panel = f'<div class="panels"><div class="panel"><p class="ph">{esc(vals[0]["unit"])} · {esc(state_label(v, "ADMINISTRATIVE"))}</p><ol class="anatomy">{"".join(items)}</ol></div></div>'
    shared_marks = set.intersection(*[{m for m in r["markers"] if m != "WITHHELD"} for r in vals]) if vals else set()   # a marker every object carries stands once in the caption
    rows = [[esc(r["x_text"]), qual(esc(withheld_label) if r.get("withheld") or r.get("y") is None else num(r["y"]), esc(r["unit"]) if r["unit"] != vals[0]["unit"] else "", esc(r["is_not_text"]),
                                    esc("; ".join(marker_label(v, m) for m in r["markers"] if m != "WITHHELD" and m not in shared_marks)))] for r in vals]
    tbl = table(caption_of(v, qual(esc(vals[0]["unit"]), esc(state_label(v, "ADMINISTRATIVE")), esc("; ".join(marker_label(v, m) for m in sorted(shared_marks))))), ["", esc(vals[0]["unit"])], rows)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


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
    L = v["chain_labels"]; sub = sub_heading(heading)
    steps = chain_steps(chain_src, include_activity)
    first_open = next((i for i, s in enumerate(steps) if not s["evidenced"]), None)
    items = []
    for i, s in enumerate(steps):
        state = L["EVIDENCED"] if s["evidenced"] else L["OPEN"]
        cls = "step " + ("evidenced" if s["evidenced"] else "open") + (" stop" if i == first_open else "")
        entries = sorted([("e", str(e.get("date")), e) for e in s["events"]] + [("a", str(a.get("x")), a) for a in s["activity"]], key=lambda t: t[1])   # one dated order within a step
        evs = ""
        for kind, when, e in entries:
            if kind == "e":
                evs += (f'<li><span class="clock"><span class="v">{bdi(when)}</span></span><span class="ev">{esc(e["label_text"])}'
                        + (f' <a class="source-locator" href="{esc(e["source"])}" rel="noopener noreferrer" target="_blank" aria-label="{esc(v["labels"]["source"])} {esc(e["label_text"])}">↗</a>' if str(e.get("source", "")).startswith("http") else "")
                        + "</span></li>")
            else:
                evs += f'<li><span class="clock"><span class="v">{bdi(when)}</span></span><span class="ev">{esc(e["label_text"])} · {num(e["y"])} {esc(e["unit"])}</span></li>'
        items.append(f'<li class="{cls}"><div class="st-head"><span class="glyph" aria-hidden="true">{"■" if s["evidenced"] else "□"}</span><{sub}>{esc(L[s["step"]])}</{sub}><span class="st-state">{esc(state)}</span></div>'
                     + (f'<ul class="evs">{evs}</ul>' if evs else "") + "</li>")
    panel = f'<div class="panels"><div class="panel"><ol class="chain">{"".join(items)}</ol></div></div>'
    rows = []
    for s in steps:
        state = L["EVIDENCED"] if s["evidenced"] else L["OPEN"]
        entries = sorted([(str(e.get("date")), f'{e.get("date")} {e["label_text"]}') for e in s["events"]] + [(str(a.get("x")), f'{a.get("x")} {a["label_text"]} {plain_num(a["y"])} {a["unit"]}') for a in s["activity"]])
        ev_text = "; ".join(t for _, t in entries)
        rows.append([esc(L[s["step"]]), qual(esc(state), iso_run(ev_text))])
    tbl = table(caption_of(v), ["", esc(v["labels"]["what_it_shows"])], rows)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


def rv009_figure(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    return chain_figure(v, v, cite_label, origin, heading, include_activity=True)


def payment_rails(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """SUPPORTING: the chain as a non-quantitative state diagram built from the governed chain labels and the
    deduplicated event set of RV-CWR-009 (its rationale asks for exactly that reuse); no value is plotted."""
    src = v.get("_chain_source")
    if not src:
        return text_frame(v, cite_label, origin, heading)
    return chain_figure(v, src, cite_label, origin, heading, include_activity=False)


# ================================================================================================ D6 drawings
# The signature matrix, the dated lanes and the multi-response bars, in the same anatomy and technique as D1–D2
# (design/06_VISUAL_TABLE_SYSTEM.md). Every word is a governed label or a governed data value; a heading the Master
# does not govern yet is rendered as a visibly marked development placeholder (⟦NCC:<request key>⟧, brief §10) and
# listed in ESCALATIONS.md — the accepted site contains none.


def ncc(key: str, text: str = "") -> str:
    """A governed label where it exists; otherwise the brief §10 development placeholder for the requested key."""
    return esc(text) if text else f'<span class="ncc" lang="en" dir="ltr">⟦NCC:{esc(key)}⟧</span>'


LATIN = __import__("re").compile(r"[A-Za-z]")


def date_token(value) -> str:
    """A governed date value printed exactly as the Master holds it, as an isolated left-to-right run: an ISO date, a
    quarter or half ("2024 Q3"), or a free-text time boundary ("observed 2026-09-07", "2026-01-22 event") whose
    qualifier is part of the boundary and is never dropped. The free text is English in both editions today — it is
    marked `lang="en"` and its bilingual form is escalated (ESCALATIONS.md, D6) — never rewritten here."""
    v = str(value or "").strip()
    if LATIN.search(v):
        return f'<bdi dir="ltr" lang="en">{esc(v)}</bdi>'
    return bdi(v)


def source_link(r: dict, L: dict) -> str:
    """The source record behind a governed row (its data-page card), when the source has a public locator."""
    if r.get("source_href"):
        return f'<a class="srcl" href="{esc(r["source_href"])}">{esc(L["source_record"])}: <span dir="auto">{esc(r["source_title"])}</span></a>'
    return ""


# ------------------------------------------------------------------------------------------------ the provider matrix (VIS-PROVIDER-OBSERVABILITY)
MATRIX_HEADINGS = ("UI-VIS-MATRIX-AUTHORITY", "UI-VIS-MATRIX-UNIVERSE", "UI-VIS-MATRIX-STATUS", "UI-VIS-MATRIX-NEGATIVE", "UI-VIS-MATRIX-OPERATION")
CLASS_ORDER = ("PUC-BANK-2026-01", "PUC-EXCH-2026-01", "PUC-WALLET-2025-01", "PUC-MFI-2026-01")   # the contract's row order
STATUS_CLASS = {"PUC-EXCH-2026-01": ("EXCHANGE", "REMITTANCE"), "PUC-WALLET-2025-01": ("E_WALLET",)}   # which status rows belong to which class (event class prefix)


def provider_matrix(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """SIGNATURE · one row per provider class, five dimensions in the contract's column order (issuing authority or
    source; dated named universe or count; status events; negative authority; evidence of operation). Cells hold
    governed words and dates, never dots; a dimension with no governed row is UNKNOWN in the state grammar (never
    zero, never 'none exist'); counts only as governed: the roster by category (never 429 as providers), the wallet
    counts listed by date and wording (never one number). Every dated cell links its source record. The five column
    headings and the fifth row's class label are not governed yet (escalated): they render as placeholders, each cell
    keeps its own governed label as well, and the payment-system-operators row — the contract's known gap — is always
    drawn, UNKNOWN in every dimension with the three institution events as context. Narrow form: one card per class,
    the dimensions stacked. Fallback: one two-column table per class, dimension by dimension (the same words)."""
    L = v["labels"]; O = v["objects"]; sub = sub_heading(heading)
    universe = {r["id"]: r for r in O.get("universe") or []}
    roster = O.get("roster_counts") or []
    status = sorted(O.get("status_events") or [], key=lambda e: str(e.get("date")))
    negative = O.get("negative_authority") or []
    wallets = O.get("wallet_counts") or []
    heads = v.get("matrix_headings") or {}
    unknown = f'<p class="unk">{esc(L["unknown"])}</p>'
    pso_label = L.get("class_pso") or ""
    ctx = v.get("_context_events") or []

    def dim(n: int) -> str:
        return ncc(MATRIX_HEADINGS[n], heads.get(MATRIX_HEADINGS[n], ""))

    def cell(n: int, inner: str, label: str = "") -> str:
        lab = f'<p class="cl">{esc(label)}</p>' if label else ""
        return f'<div class="cell c{n + 1}"><span class="dim">{dim(n)}</span>{lab}{inner}</div>'

    def joined(parts: list) -> str:
        """Tokens separated by the middle dot, each dot bound to the first word after it by a no-break space (a dot
        never ends a line; the token itself still wraps)."""
        return "".join(x if i == 0 else f' ·\u00a0{x}' for i, x in enumerate(parts))

    def event_lines(evs: list) -> str:
        """Status events grouped by their governed state: the state label, then the dates in order, each date the
        link to its source record (named by the date it shows, then the record: Label in Name)."""
        groups: dict = {}
        for e in evs:
            groups.setdefault(e["state_text"], []).append(e)
        out = []
        for state, es in groups.items():
            dates = []
            for e in es:
                d = date_token(e.get("date"))
                if e.get("source_href"):
                    dates.append(f'<a class="dl" href="{esc(e["source_href"])}" aria-label="{esc(e.get("date"))} · {esc(L["source_record"])}: {esc(e["source_title"])}">{d}</a>')
                else:
                    dates.append(d)
            out.append(f'<li><b>{esc(state)}</b><span class="dates">{joined(dates)}</span></li>')
        return "".join(out)

    def sources_of(u: dict) -> list:
        return [u] if u.get("source_href") else [w for w in wallets if w.get("source_href")]

    rows = []
    for pid in CLASS_ORDER:
        u = universe.get(pid)
        if not u:
            continue
        # 1 · authority or source
        srcs = list(dict.fromkeys(x for x in (source_link(r, L) for r in sources_of(u)) if x))
        c1 = cell(0, "<ul class=\"srcs\">" + "".join(f"<li>{x}</li>" for x in srcs) + "</ul>" if srcs else unknown)
        # 2 · dated named universe or count
        if pid == "PUC-EXCH-2026-01":
            counts = "".join(f'<li><b class="n">{num(r["count"])}</b> <span dir="auto">{esc(r["label_text"])}</span>{joined(["", esc(r["unit_text"]), date_token(r.get("date"))])}</li>' for r in roster)
            body = f'<ul class="counts">{counts}</ul>'
        elif pid == "PUC-WALLET-2025-01":
            counts = "".join(f'<li><b class="n">{bdi(r["count"])}</b> {esc(r["unit_text"])}{joined(["", esc(r["state_text"]), date_token(r.get("date"))])} {source_link(r, L)}</li>' for r in wallets)
            body = f'<ul class="counts">{counts}</ul>'
        elif u.get("count") is not None:
            body = f'<p class="cnt"><b class="n">{num(u["count"])}</b>{joined(["", date_token(u.get("date"))])}</p>'
        else:
            body = f'<p class="cnt">{date_token(u.get("date"))}</p>'
        c2 = cell(1, body + f'<p class="cl2">{iso_run(u["named_text"])}</p>', u["count_state_text"])
        # 3 · status events
        evs = [e for e in status if any(e.get("class", "").startswith(k) for k in STATUS_CLASS.get(pid, ()))]
        c3 = cell(2, (f'<ul class="evl">{event_lines(evs)}</ul>' if evs else ""), u["events_text"])
        # 4 · negative authority (a dated list of unlicensed names exists for wallets only; elsewhere none is held)
        if pid == "PUC-WALLET-2025-01" and negative:
            n0 = negative[0]
            neg_auth = f'<span dir="auto">{esc(n0["authority_text"])}</span>'
            neg_state = f'<b>{esc(n0["state_text"])}</b>'
            c4 = cell(3, f'<ul class="evl"><li>{date_token(n0.get("date"))}{joined(["", neg_auth, neg_state])} {source_link(n0, L)}</li></ul>')
        else:
            c4 = cell(3, unknown)
        # 5 · evidence of operation: no governed row for any class
        c5 = cell(4, unknown)
        rows.append(f'<li class="prow" data-provider-class="{esc(pid)}"><{sub} class="cls">{esc(u["class_text"])}</{sub}><div class="cells">{c1}{c2}{c3}{c4}{c5}</div>'
                    f'<p class="lim"><b>{esc(L["does_not_establish"])}</b> {iso_run(u["limit_text"])}</p></li>')
    # the fifth row: payment-system operators — the contract's known gap, drawn as UNKNOWN in every dimension with the
    # institution events as context (never as a named universe); its class label is a placeholder until governed
    ctx_html = ""
    for e in ctx:
        ctx_label = f'<span dir="auto">{esc(e["label_text"])}</span>'
        ctx_link = f' <a class="source-locator" href="{esc(e["source"])}" rel="noopener noreferrer" target="_blank" aria-label="{esc(L["source"])} {esc(e["label_text"])}">↗</a>' if str(e.get("source", "")).startswith("http") else ""
        ctx_html += f'<li>{bdi(e.get("date"))}{joined(["", ctx_label])}{ctx_link}</li>'
    ctx_cell = f'<ul class="evl ctx">{ctx_html}</ul>' if ctx else unknown
    rows.append(f'<li class="prow pso" data-provider-class="PSO"><{sub} class="cls">{ncc("UI-VIS-CAT-PRV-CLASS-PSO", pso_label)}</{sub}><div class="cells">{cell(0, unknown)}{cell(1, unknown)}'
                f'{cell(2, ctx_cell)}{cell(3, unknown)}{cell(4, unknown)}</div></li>')
    authorities = list(dict.fromkeys(e["authority_text"] for e in status + negative if e.get("authority_text")))
    scope_note = "".join(f'<p class="cap note issuer"><span dir="auto">{esc(a)}</span>: {esc(L["issuer_scope"])}</p>' for a in authorities)
    panel = f'<div class="panels"><div class="panel"><ol class="matrix">{"".join(rows)}</ol>{scope_note}</div></div>'
    # the fallback: one two-column table per class, the five dimensions as rows — the same words as the cells
    tables = []
    unk = esc(L["unknown"])
    for pid in CLASS_ORDER:
        u = universe.get(pid)
        if not u:
            continue
        auth = "; ".join(dict.fromkeys(iso_run(r["source_title"]) for r in sources_of(u) if r.get("source_title"))) or unk
        if pid == "PUC-EXCH-2026-01":
            cnt = "; ".join(f'{num(r["count"])} <span dir="auto">{esc(r["label_text"])}</span> ({esc(r["unit_text"])}, {date_token(r.get("date"))})' for r in roster)
        elif pid == "PUC-WALLET-2025-01":
            cnt = "; ".join(f'{bdi(r["count"])} {esc(r["unit_text"])} ({esc(r["state_text"])}, {date_token(r.get("date"))})' for r in wallets)
        else:
            cnt = (f'{num(u["count"])} ({date_token(u.get("date"))})' if u.get("count") is not None else date_token(u.get("date")))
        evs = [e for e in status if any(e.get("class", "").startswith(k) for k in STATUS_CLASS.get(pid, ()))]
        ev_txt = "; ".join(f'{date_token(e.get("date"))} {esc(e["class_text"])}: {esc(e["state_text"])}' for e in evs)
        neg_txt = f'{date_token(negative[0].get("date"))} <span dir="auto">{esc(negative[0]["authority_text"])}</span>: {esc(negative[0]["state_text"])}' if (pid == "PUC-WALLET-2025-01" and negative) else unk
        trows = [[dim(0), auth], [dim(1), f'{esc(u["count_state_text"])}: {cnt}. {iso_run(u["named_text"])}'],
                 [dim(2), esc(u["events_text"]) + (f': {ev_txt}' if ev_txt else "")], [dim(3), neg_txt], [dim(4), unk]]
        tables.append(table(caption_of(v, esc(u["class_text"])), ["", esc(L["what_it_shows"])], trows))
    ctx_txt = "; ".join(f'{bdi(e.get("date"))} <span dir="auto">{esc(e["label_text"])}</span>' for e in ctx) or unk
    tables.append(table(caption_of(v, ncc("UI-VIS-CAT-PRV-CLASS-PSO", pso_label)), ["", esc(L["what_it_shows"])],
                        [[dim(0), unk], [dim(1), unk], [dim(2), ctx_txt], [dim(3), unk], [dim(4), unk]]))
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, "".join(tables), heading=heading)


def _days(iso: str) -> int:
    """Days since 2000-01-01 for a governed date (YYYY, YYYY-MM or YYYY-MM-DD; a month counts from its first day)."""
    import datetime
    parts = [int(x) for x in str(iso).split("-")]
    while len(parts) < 3:
        parts.append(1)
    return (datetime.date(parts[0], parts[1], parts[2]) - datetime.date(2000, 1, 1)).days


LANE_KEYS = ("UI-VIS-CAT-LANE-PEOPLE-SURVEY", "UI-VIS-CAT-LANE-PAYMENT-INFRA-ADMIN", "UI-VIS-CAT-LANE-INSTITUTIONS-REFORMS")


def dated_lanes(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """CORE · three dated lanes on one left-to-right time axis — people (the fieldwork span from CLM-001's governed
    period), payment infrastructure (monthly dated presence, first and latest values labelled with their governed
    object label) and institutions and reforms (dated events, keyed to the list beneath) — ending in an OPEN outcome
    node in the chain vocabulary. No lane has a value axis; lanes never share one; the governed not-comparable label
    stands between them. The axis is padded at both ends so no mark sits on its edge; event keys closer than 4 % of
    the axis share one bracketed key; when the infrastructure span is short its two labels stand outside it. Narrow
    form (the contract's): the lanes become the dated lists under them (the strips are hidden by the stylesheet).
    The table: one group per lane, its dated rows."""
    L = v["labels"]; FLD = v.get("frame_labels") or {}; CL = v["chain_labels"]; sub = sub_heading(heading)
    FL = [FLD.get(k) or "" for k in LANE_KEYS]
    if not all(FL):   # the three lane titles by their governed keys; positional only if a key is absent
        FL = list(FLD.values())[:3]
    v = {**v, "_frame_notes_drawn": True}   # the three governed frame labels are the lane titles
    people = next(s for s in v["series"] if s["id"] == "people")
    infra = next(s for s in v["series"] if s["id"] == "infrastructure")
    inst = sorted(v["objects"].get("institutions") or [], key=lambda e: str(e.get("date")))
    span = v.get("people_span") or {}
    p0 = people["values"][0]
    dates = [span.get("from"), span.get("to")] + [str(r["x"]) for r in infra["values"]] + [str(e["date"]) for e in inst]
    dates = [d for d in dates if d]
    t0, t1 = min(_days(d) for d in dates) - 45, max(_days(d) for d in dates) + 45   # padded: no mark on an edge
    def X(d) -> float:
        return 3 + 86 * (_days(d) - t0) / max(1, t1 - t0)
    years = range(int(min(dates)[:4]), int(max(dates)[:4]) + 2)
    ticks = [y for y in years if t0 <= _days(f"{y}-01-01") <= t1 + 60]
    axis = "".join(f'<line class="tick" x1="{X(f"{y}-01-01"):.2f}%" y1="0" x2="{X(f"{y}-01-01"):.2f}%" y2="6"/><text class="lbl" x="{X(f"{y}-01-01"):.2f}%" y="19" text-anchor="middle">{y}</text>' for y in ticks)
    axis_svg = f'<svg class="ax lanes-ax" width="100%" height="24" aria-hidden="true" focusable="false" direction="ltr"><line class="axis" x1="3%" y1="0.5" x2="97%" y2="0.5"/>{axis}</svg>'
    def strip(inner: str, cls: str = "", height: int = 34) -> str:
        return f'<svg class="lane-svg{(" " + cls) if cls else ""}" width="100%" height="{height}" aria-hidden="true" focusable="false" direction="ltr"><line class="stem" x1="3%" y1="20" x2="97%" y2="20"/>{inner}</svg>'
    # lane 1 · people: the fieldwork span
    x_a, x_b = X(span["from"]), X(span["to"])
    mid = f"{(x_a + x_b) / 2:.2f}%"
    lane1 = strip(f'<line class="span" x1="{x_a:.2f}%" y1="20" x2="{x_b:.2f}%" y2="20"/>' + svg_mark("circle", mid, 20, 5))
    period_txt = iso_run(span.get("text") or "")
    period_html = f'<a href="{esc(span["href"])}">{period_txt}</a>' if span.get("href") else period_txt
    lane1_txt = (f'<p class="ln"><b>{esc(p0["series_label_text"])}</b> · {num(p0["y"])} {esc(p0["unit_text"])} · <span dir="auto">{esc(p0["group_text"])}</span> · {esc(state_label(v, "MEASURED"))}</p>'
                 f'<div class="clock ln"><span class="k">{esc(L["period"])}</span><span class="v">{period_html}</span></div>')
    # lane 2 · infrastructure: monthly presence, first and latest labelled (outside the span when it is short)
    vals = infra["values"]
    marks = "".join(f'<rect class="mark a" x="{X(str(r["x"])):.2f}%" y="16" width="8" height="8" transform="translate(-4,0)"/>' for r in vals)
    first, last = vals[0], vals[-1]
    xf, xl = X(str(first["x"])), X(str(last["x"]))
    if xl - xf < 14:
        labels = (f'<text class="val" x="{xf - 1.2:.2f}%" y="24" text-anchor="end">{plain_num(first["y"])}</text>'
                  f'<text class="val" x="{xl + 1.2:.2f}%" y="24" text-anchor="start">{plain_num(last["y"])}</text>')
    else:
        labels = (f'<text class="val" x="{xf:.2f}%" y="10" text-anchor="start">{plain_num(first["y"])}</text>'
                  f'<text class="val" x="{xl:.2f}%" y="10" text-anchor="end">{plain_num(last["y"])}</text>')
    lane2 = strip(marks + labels)
    lane2_txt = (f'<p class="ln"><b>{esc(first["label_text"])}</b> · {bdi(first["x"])} · {num(first["y"])} {esc(first["unit_text"])} — {bdi(last["x"])} · {num(last["y"])} {esc(last["unit_text"])} · {esc(state_label(v, "ADMINISTRATIVE"))}</p>')
    # lane 3 · institutions and reforms: dated events keyed 1..n
    ev_marks = "".join(svg_mark("circle", f"{X(str(e['date'])):.2f}%", 20, 4) for e in inst)
    clusters: list[list[int]] = []   # events closer than 4 % of the axis share one bracketed key ("3–6")
    for i, e in enumerate(inst):
        if clusters and X(str(e["date"])) - X(str(inst[clusters[-1][-1]]["date"])) < 4.0:
            clusters[-1].append(i)
        else:
            clusters.append([i])
    for c in clusters:
        cx = sum(X(str(inst[i]["date"])) for i in c) / len(c)
        key = f"{c[0] + 1}" if len(c) == 1 else f"{c[0] + 1}–{c[-1] + 1}"
        ev_marks += f'<text class="lbl key" x="{cx:.2f}%" y="9" text-anchor="middle">{key}</text>'
    lane3 = strip(ev_marks)
    ev_list = "".join(f'<li><span class="k">{i + 1}</span><span class="clock"><span class="v">{bdi(e["date"])}</span></span><span class="ev"><span dir="auto">{esc(e["label_text"])}</span>'
                      + (f' <a class="source-locator" href="{esc(e["source"])}" rel="noopener noreferrer" target="_blank" aria-label="{esc(L["source"])} {esc(e["label_text"])}">↗</a>' if str(e.get("source", "")).startswith("http") else "")
                      + "</span></li>" for i, e in enumerate(inst))
    # the outcome node: open, at the end of the axis
    lane4 = strip(f'<line class="stem open" x1="3%" y1="20" x2="97%" y2="20"/><rect class="mark b" x="97%" y="14" width="12" height="12" transform="translate(-6,0)"/>', "open")
    between = f'<div class="between">{esc(L["not_comparable"])}</div>'
    panel = (f'<div class="panels"><div class="panel lanes-dated">'
             f'<div class="lane"><{sub}>{esc(FL[0])}</{sub}>{lane1}{lane1_txt}</div>{between}'
             f'<div class="lane"><{sub}>{esc(FL[1])}</{sub}>{lane2}{lane2_txt}</div>{between}'
             f'<div class="lane"><{sub}>{esc(FL[2])}</{sub}>{lane3}<ol class="evs keyed">{ev_list}</ol></div>'
             f'<div class="lane outcome"><{sub}>{esc(CL["OUTCOME"])}</{sub}><span class="st-state">{esc(CL["OPEN"])}</span>{lane4}</div>'
             f'{axis_svg}</div></div>')
    groups = [(esc(FL[0]), [[period_txt, esc(f'{p0["series_label_text"]} · {plain_num(p0["y"])} {p0["unit_text"]} · {p0["group_text"]} · {state_label(v, "MEASURED")}')]]),
              (esc(FL[1]), [[bdi(r["x"]), esc(f'{r["label_text"]} · {plain_num(r["y"])} {r["unit_text"]} · {state_label(v, "ADMINISTRATIVE")}')] for r in vals]),
              (esc(FL[2]), [[bdi(e["date"]), esc(e["label_text"])] for e in inst]),
              (None, [[esc(CL["OUTCOME"]), esc(CL["OPEN"])]])]
    tbl = grouped_table(caption_of(v), ["", esc(v["labels"]["what_it_shows"])], groups)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


# ------------------------------------------------------------------------------------------------ multi-response bars (VIS-FIRM-CONSTRAINTS)
def firm_constraints(v: dict, cite_label: str, origin: str | None, heading: str = "h2") -> str:
    """CORE · horizontal bars from zero, in the contract's descending order without rank numbers; the record's
    governed measurement limitation (firms could name more than one challenge; the base is not held) in the frame;
    the table lists the eight governed rows the contract resolves (the contract names sixteen; the other eight are
    requested Master-first — ESCALATIONS.md)."""
    vals = v["series"][0]["values"]
    vmax, step = axis_scale([r["y"] for r in vals])
    unit = vals[0]["unit"]
    v = {**v, "_frame_notes_drawn": True}
    note = f'<p class="cap note">{esc(v.get("record_limit") or "")}</p>' if v.get("record_limit") else ""
    panel = (f'<div class="panels"><div class="panel bars"><p class="ph">{esc(unit)} · {esc(state_label(v, "MEASURED"))}</p>'
             f'<div class="p1 noranks">{bar_rows(vals, vmax)}{axis_row(vmax, step)}</div>{note}</div></div>')
    state = uniform(vals, lambda r: r["state"])
    rows = [[esc(r["x_text"]), qual(num(r["y"]), esc(r["unit"]) if r["unit"] != unit else "", "" if state else esc(state_label(v, r["state"])))] for r in vals]
    tbl = table(caption_of(v, qual(esc(unit), esc(state_label(v, state)) if state else "")), ["", esc(unit)], rows)
    return frame_open(v, heading) + panel + frame_close(v, cite_label, origin, tbl, heading=heading)


DRAWERS = {"VIS-FINDEX-GAPS": findex_gaps, "VIS-REMITTANCE-MACRO": remittance_macro, "VIS-POS-TERMINALS": pos_panel, "VIS-POS-TRANSACTIONS": pos_panel,
           "VIS-POS-VALUE": pos_panel, "VIS-REMITTANCE-COST": remittance_cost, "VIS-PAYMENT-ANATOMY": payment_anatomy, "RV-CWR-009": rv009_figure,
           "VIS-PAYMENT-RAILS": payment_rails,
           "VIS-PROVIDER-OBSERVABILITY": provider_matrix, "RV-CWR-004": dated_lanes, "VIS-FIRM-CONSTRAINTS": firm_constraints}   # D6
