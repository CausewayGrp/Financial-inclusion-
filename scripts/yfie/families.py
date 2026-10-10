# -*- coding: utf-8 -*-
"""The page families beyond the D1 trio, composed in the same T4 · Instrument grammar (design/01_FOUNDATIONS.md §4, §5):
one page object per route with its head (crumb, rubric, question, title, statement), answers as numbered `h2`
sections with governed rubrics, one boundary voice for every limit, figures as framed objects, compact clock-first
objects for every bound record, a verification spine, and the page's own actions at its foot. Composition rules per
family are recorded in design/04_PAGE_FAMILY_COMPOSITIONS.md; nothing here authors public text.

Question Entry · Domain Answer · Evidence Directory · Comparison · Data & Source (D2) and, as the family rule that lets
every document build and the repository suites run, Reading Index · Measurement · Reference / Trust · 404 · root.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import render as R
from .render import CUR, bdi, clock, compact, crumb, esc, footer, head, header, iso, json_block, page_tools, page_util, paras, print_foot, rubric, source_card, spine, strip
from .visuals import figure, num, text_alt

ROOT = Path(__file__).resolve().parents[2]
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

# Design decision (DL-D2-003): the section beside which each bound visual that the presentation contract does not place
# in the first screen is drawn. A visual whose section is not a primary answer, or that is not listed, sits in the
# page's depth after the primary answers (never inside a disclosure).
VISUAL_PLACEMENT = {
    "/reforms/": {"VIS-PAYMENT-RAILS": 6, "VIS-TARGET-RESULT-STATE": 6, "VIS-FCP-REDRESS-PATH": 3, "VIS-OECD-FCP-TIMELINE": 11},
    "/payments/": {"VIS-E-MONEY-RULE-STACK": 6},
    "/remittances/": {"VIS-REMITTANCE-COST": 5},
}
SMALL_MULTIPLES = {"/payments/": ["VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE"]}


# NB-2 (owner brief of 10 October 2026, B4): the official Creative Commons licence addresses that /rights/ states (deed and
# legal code, each language's own) are links; no other address in governed text is turned into one.
CC_LICENCE_URL = re.compile(r"https://creativecommons\.org/licenses/by/4\.0/(?:deed\.ar|legalcode\.(?:en|ar))?(?![\w/.-])")


def linkify(escaped: str) -> str:
    """A governed contact address and an official licence address are actionable; the text is unchanged (presentation only)."""
    out = EMAIL.sub(lambda m: f'<a href="mailto:{m.group(0)}" dir="ltr">{m.group(0)}</a>', escaped)
    return CC_LICENCE_URL.sub(lambda m: f'<a href="{m.group(0)}" rel="license" dir="ltr">{m.group(0)}</a>', out)


def body_paras(paragraphs, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{linkify(iso(esc(p)))}</p>" for p in paragraphs)


def answer(sec: dict, n: int | None, id_: str, tone: str = "") -> str:
    """A governed section as an answer: its role as the rubric (with its ordinal), its heading as `h2`, its body."""
    if tone == "bnd":
        return (f'<section class="bnd" id="{id_}">' + (f'<span class="rubric">{esc(sec.get("role") or "")}</span>' if sec.get("role") else "")
                + f'<h2>{esc(sec["heading"])}</h2><div class="mt8">{body_paras(sec["paragraphs"])}</div></section>')
    rub = (f'<span class="rubric">' + (f'<span class="n">{n:02d}</span>' if n else "") + f'{esc(sec.get("role") or "")}</span>') if (sec.get("role") or n) else ""
    return f'<section class="qa" id="{id_}"><div>{rub}<h2>{esc(sec["heading"])}</h2></div><div class="body">{body_paras(sec["paragraphs"])}</div></section>'


def compact_obj(rec: dict, L: dict, open_label: str | None = None, cls: str = "compact", boundary: bool = False) -> str:
    """Clock-first compact evidence object: when → title → for whom → (boundary) → open (+ reference where the directory shows it)."""
    parts = [clock(L["period"], esc(rec.get("period") or "")), f'<div class="q"><a href="{rec["href"]}">{esc(rec["title"])}</a></div>']
    if rec.get("summary"):
        parts.append(f'<div class="small">{esc(rec["summary"])}</div>')
    if rec.get("universe"):
        parts.append(f'<div class="small pop"><b>{esc(L["applies"])}</b> {esc(rec["universe"])}</div>')
    if boundary and rec.get("does_not_establish"):
        parts.append(f'<div class="small bnd-line"><b>{esc(L["does_not_establish"])}</b> {esc(rec["does_not_establish"])}</div>')
    acts = f'<a href="{rec["href"]}">{esc(open_label or L["open_record"])}</a>'
    if rec.get("ref"):
        acts += f' <span class="rref">{esc(L["reference"])} {bdi(rec["ref"])}</span>'
    parts.append(f'<div class="open">{acts}</div>')
    return f'<article class="{cls}">{"".join(parts)}</article>'


def reading_obj(r: dict, L: dict, cls: str = "compact") -> str:
    return (f'<article class="{cls}">{clock(L["evidence_period"], esc(r["evidence_period"]))}<div class="q"><a href="{r["href"]}">{esc(r["title"])}</a></div>'
            f'<div class="small">{esc(r["thesis"])}</div><div class="open"><a href="{r["href"]}">{esc(L["open_reading"])}</a></div></article>')


def measure_obj(m: dict, cls: str = "compact") -> str:
    """A Measurement priority as a compact object: title, the missing evidence, the decision it would strengthen, open."""
    ML = m["labels"]
    return (f'<article class="{cls}"><div class="clock"><span class="k">{esc(ML["priority"])}</span><span class="v">{bdi(m["priority"])} · {esc(m["domain"])}</span></div>'
            f'<div class="q"><a href="{m["href"]}">{esc(m["title"])}</a></div>'
            + (f'<div class="small">{esc(m["current"])}</div>' if m.get("current") else "")
            + f'<div class="small"><b>{esc(ML["needed"])}</b> {esc(m["missing"])}</div>'
            + (f'<div class="small"><b>{esc(ML["unlocked"])}</b> {esc(m["unlocked"])}</div>' if m.get("unlocked") else "")
            + f'<div class="open"><a href="{m["href"]}">{esc(ML["open"])}</a></div></article>')


def blocks(page: dict, L: dict, start_id: str = "blk") -> tuple[str, list]:
    """The bound objects a static page carries: records, visuals, priorities — each group an answer with its governed heading."""
    out, index = [], []
    for i, b in enumerate(page.get("blocks") or []):
        id_ = f"{start_id}-{b['kind']}"
        if b["kind"] == "visuals":
            figs = "".join(figure(v, L["cite"], R.DISC.origin()) for v in b["items"])
            out.append(f'<section class="qa" id="{id_}"><div>{rubric(L.get("visual_eyebrow") or "")}</div><div>{figs}</div></section>' if L.get("visual_eyebrow") else f'<section class="qa" id="{id_}"><div></div><div>{figs}</div></section>')
            continue
        if b["kind"] == "records":
            items = "".join(compact_obj(r, L, boundary=True) for r in b["items"])
        else:
            items = "".join(measure_obj(m) for m in b["items"])
        # RC-15 (B15 d, B-5): a governed line that says which priorities a page shows (Explore: the P0 items)
        note = f'<p class="small" data-ma-basis>{esc(b["note"])}</p>' if b.get("note") else ""
        out.append(f'<section class="qa" id="{id_}"><div><h2>{esc(b["heading"])}</h2></div><div>{note}<div class="objs">{items}</div></div></section>')
        index.append((id_, b["heading"]))
    return "".join(out), index


def next_actions(nx: dict | None, id_: str = "next") -> tuple[str, list]:
    if not nx:
        return "", []
    links = "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in nx["links"])
    return f'<section class="qa" id="{id_}"><div><h2>{esc(nx["title"])}</h2></div><div><p class="small">{esc(nx["intro"])}</p><nav class="actions" aria-labelledby="next-h">{links}</nav></div></section>'.replace('<h2>', '<h2 id="next-h">', 1), [(id_, nx["title"])]


def lead_paragraphs(lead: str) -> str:
    """A governed lead as its paragraphs: a blank line in the Master starts a new one (the Compare intro, B7)."""
    return "".join(f"<p>{linkify(iso(esc(x.strip())))}</p>" for x in re.split(r"\n\s*\n", lead) if x.strip())


def head_block(page: dict, shell: dict, rubric_text: str = "", question: str = "", lead: str = "", crumb_html: str = "") -> str:
    return (f'<div class="head">{crumb_html}' + (f'<span class="rubric">{esc(rubric_text)}</span>' if rubric_text else "")
            + (f'<p class="q">{esc(question)}</p>' if question else "") + f'<h1 id="page-title">{esc(page["title"])}</h1>{page_tools(shell)}'
            + (f'<div class="st">{lead_paragraphs(lead)}</div>' if lead else "") + "</div>")   # B7 review: a blank line starts a paragraph


def page_html(page: dict, shell: dict, body: str, index: list, edges: list, kind: str = "website", extra: str = "", foot_index: bool = True) -> str:
    return (head(page, shell, page["route"], kind=kind, extra=extra) + header(shell)
            + f'<article class="obj page-obj">{body}{page_util(shell, page)}</article>{spine(index, edges)}{spine(index, edges, foot=True, foot_index=foot_index)}'
            + footer(shell, print_foot(shell, page["route"], page["title"])))


# ------------------------------------------------------------------------------------------------ Question Entry
def question_entry(page: dict, shell: dict) -> str:
    L = page["labels"]
    ls = page["list_section"] or {}
    groups = []
    for g in page["groups"]:
        items = "".join(f'<li><div><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="gets small">{esc(q["gets"])}</div></div></li>' for q in g["items"])
        groups.append(f'<div class="cluster"><h3>{esc(g["heading"])} <span class="count">({bdi(len(g["items"]))})</span></h3><ol class="qlist">{items}</ol></div>')
    parts = [head_block(page, shell, L["flow"], lead=page["lead"])]
    # The governed questions section (section 5) renders once, here, as the answer that holds the clusters it
    # introduces: its role and heading head the section, its body is the clusters' introduction, and the interface
    # lead (eyebrow, list title, intro) sits between the body and the clusters (DEBT-019; it is excluded from the
    # loop below, so no second, question-less rendering exists).
    parts.append(f'<section class="qa first" id="questions"><div><span class="rubric"><span class="n">01</span>{esc(ls.get("role") or "")}</span><h2>{esc(ls.get("heading") or L["list_title"])}</h2></div>'
                 f'<div>{body_paras(ls.get("paragraphs") or [], "st")}'
                 f'<div class="clusters-lead">{rubric(L["eyebrow"])}<p class="q">{esc(L["list_title"])}</p><p class="small">{esc(L["list_intro"])}</p></div>'
                 f'<div class="clusters">{"".join(groups)}</div></div></section>')
    index = [("questions", ls.get("heading") or L["list_title"])]
    for s in page["sections"]:
        if ls and s["order"] == ls.get("order"):
            continue
        kind = "bnd" if s.get("role") and ("does not establish" in s["role"].lower() or "لا يثبته" in s["role"] or "know" in s["role"].lower() or "نعرف" in s["role"]) else ""
        parts.append(answer(s, None if kind else len(index) + 1, f"s{s['order']}", kind))
        index.append((f"s{s['order']}", s["heading"]))
    b, bi = blocks(page, L)
    parts.append(b); index += bi
    if page["featured"]:
        f = page["featured"]
        parts.append(f'<section class="qa" id="deeper">{rubric(L["go_deeper"], tag="h2")}<div>{reading_obj(f, L, "compact first-obj")}<p class="small mt12"><a href="{page["readings_href"]}">{esc(L["all_readings"])}</a></p></div></section>')
        index.append(("deeper", L["go_deeper"]))
    n, ni = next_actions(page.get("next"))
    parts.append(n); index += ni
    parts.insert(2, strip(index))   # the phone's in-page navigation after the clusters; the foot spine keeps only the edges (DEBT-014)
    edges = [(L["go_deeper"], [f'<a href="{page["featured"]["href"]}">{esc(page["featured"]["title"])}</a>'] if page["featured"] else [])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ Domain Answer
def domain(page: dict, shell: dict) -> str:
    L = page["labels"]; route = page["route"]
    origin = R.DISC.origin()
    # the governed question is the head's framing line (rubric "the question this page answers"); the Explore link sits in the head's actions
    parts = [head_block(page, shell, L["answer_crumb"] if page["question"] else L["question_flow"], question=page["question"], lead=page["lead"])]
    # the two governed head actions. The reading rule ("How numbers are presented") is printed once, on /methodology/,
    # and reached from this page's spine (owner instructions of 3 October 2026, 09:50, C5)
    parts.append(f'<div class="head-rule"><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["primary_verify"]}">{esc(L["verify_action"])}</a></div></div>')
    index = []
    # the always-visible boundaries (the contract's supporting sections) come before the answers, as the contract's mobile priority orders them
    for s in page["band"]:
        parts.append(answer(s, None, f"s{s['order']}", "bnd"))
        index.append((f"s{s['order']}", s["heading"]))
    drawn = set()
    def fig(vid: str) -> str:
        v = page["visuals"].get(vid)
        if not v or vid in drawn:
            return ""
        drawn.add(vid)
        html_ = figure(v, L["cite"], origin)
        return html_ or ""
    placement = VISUAL_PLACEMENT.get(route, {})
    primary_orders = [s["order"] for s in page["primary"]]
    for i, s in enumerate(page["primary"], 1):
        # the rubric ordinal is the section's position in the page index, so the spine and the rubrics agree (DEBT-019)
        parts.append(answer(s, len(index) + 1, f"s{s['order']}"))
        index.append((f"s{s['order']}", s["heading"]))
        figs = ""
        if i == page["visual_after"] and page["primary_visual"]:
            figs += fig(page["primary_visual"])
        for vid, order in placement.items():
            if order == s["order"] and order in primary_orders:
                figs += fig(vid)
        if figs:
            parts.append(f'<section class="qa figs"><div>{rubric(L["visual"])}</div><div>{figs}</div></section>')
    # the page's depth: the small multiple and every other bound visual, beside no first-screen answer
    depth = ""
    for vid in SMALL_MULTIPLES.get(route, []):
        depth += fig(vid)
    if depth:
        depth = f'<div class="multiple">{depth}</div>'
    for vid, v in page["visuals"].items():
        # A5 / C4 (owner decision, 2 October 2026): a contract retired from design is not a depth frame on a domain
        # answer (VIS-CAPITAL-CONTEXT on /reforms/); its record page and the link to it stay
        if v.get("tier") == "RETIRE_FROM_DESIGN":
            continue
        depth += fig(vid)
    if depth:
        # V1 (DL-V1-009): the depth figures are views a reader opens, not the page's answer; the governed label that headed
        # them becomes the disclosure's summary, with the number of views. The primary visual above stays first-load.
        n_views = depth.count("<figure ")
        parts.append(f'<section class="qa figs fold-sec" id="views"><details class="fold views-fold"><summary>{esc(L["visual"])} <span class="count">({bdi(n_views)})</span></summary>{depth}</details></section>')
        index.append(("views", L["visual"]))
    if page["progressive"]:
        more = "".join(f'<div class="qa"><div><span class="rubric">{esc(s.get("role") or "")}</span></div><div><h3>{esc(s["heading"])}</h3><div class="body">{body_paras(s["paragraphs"])}</div></div></div>' for s in page["progressive"])
        parts.append(f'<section class="qa" id="more"><div>{rubric(L["more"], tag="h2")}</div><details class="more"><summary>{esc(L["more_intro"])}</summary>{more}</details></section>')
        index.append(("more", L["more"]))
    if page.get("chronology"):
        parts.append(chronology_block(page["chronology"], L, "chronology"))
        index.append(("chronology", page["chronology"]["heading"]))
    if page["readings"]:
        parts.append(f'<section class="qa" id="readings"><div><h2>{esc(L["readings"])}</h2></div><div class="objs">{"".join(reading_obj(r, L) for r in page["readings"])}</div></section>')
        index.append(("readings", L["readings"]))
    if page["related"]:
        rel = page["related"]
        links = "".join(f'<li><a href="{l["href"]}">{esc(l["label"])}</a></li>' for l in rel["links"])
        parts.append(f'<section class="qa" id="related"><div><h2>{esc(rel["heading"])}</h2></div><div><p class="small">{esc(rel["note"])}</p><ul class="rlist">{links}</ul></div></section>')
        index.append(("related", rel["heading"]))
    if page["measurement"]:
        parts.append(f'<section class="qa" id="measure"><div><h2>{esc(L["measure"])}</h2></div><div class="objs">{"".join(measure_obj(m) for m in page["measurement"])}</div></section>')
        index.append(("measure", L["measure"]))
    all_recs = "".join(f'<li><a href="{r["href"]}">{esc(r["title"])}</a></li>' for r in page["all_records"])
    verify = "".join(compact_obj(r, L, L["open_record"]) for r in page["verify"])
    parts.append(f'<section class="qa" id="verify"><div><h2>{esc(L["verify"])}</h2></div><div><p class="small">{esc(L["verify_intro"])}</p><div class="objs">{verify}</div>'
                 f'<div class="actions"><a href="{page["hrefs"]["evidence"]}">{esc(L["evidence"])}</a><a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a><a href="{page["hrefs"]["methodology"]}">{esc(L["method"])}</a>'
                 + (f'<a href="{page["compare_preset"]["href"]}" data-compare-preset>{esc(page["compare_preset"]["label"])}</a>' if page.get("compare_preset") else "") + '</div>'
                 + (f'<details class="more mt12"><summary>{esc(L["all_records"])} ({bdi(len(page["all_records"]))})</summary><ul class="rlist">{all_recs}</ul></details>' if all_recs else "") + "</div></section>")
    index.append(("verify", L["verify"]))
    parts.insert(2 + len(page["band"]), strip(index))   # after the always-visible boundaries, before the first answer (DEBT-014; band stays first)
    edges = [(L["verify"], [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["verify"]], L["verify_intro"]),
             (L["readings"], [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["readings"]]),
             (page["related"]["heading"] if page["related"] else "", [f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in (page["related"] or {}).get("links", [])]),
             (L["method"], [f'<a href="{page["hrefs"]["reading_rule"]}" data-reading-rule>{esc(L["reading_rule"])}</a>'])]   # 09:50 C5: under the governed "Methodology" heading
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


def chronology_block(ch: dict, L: dict, id_: str) -> str:
    CL = ch["labels"]
    items = []
    for e in ch["items"]:
        src = " · ".join(f'<a href="{s["href"]}">{esc(s["title"] or s["id"])}</a>' for s in e["sources"])
        items.append(f'<li class="compact" id="{esc(e["id"])}">{clock(L["period"], esc(e["period"]))}<div class="q">{esc(e["fact"])}</div>'
                     + (f'<div class="small"><b>{esc(CL["relevance"])}</b> {esc(e["relevance"])}</div>' if e["relevance"] else "")
                     + (f'<div class="small bnd-line"><b>{esc(CL["does_not_establish"])}</b> {esc(e["does_not_establish"])}</div>' if e["does_not_establish"] else "")
                     + (f'<div class="small"><b>{esc(CL["sources"])}</b> {src}</div>' if src else "")
                     + (f'<div class="small vnote">{esc(e["verification_note"])}</div>' if e.get("verification_note") else "") + "</li>")
    # V1B-1 (owner decision B-b): the dated list is a disclosure named by its own governed label and the number of events,
    # as on /data/; the section's heading and the intro (order is not causation) stay first-load
    return (f'<section class="qa" id="{id_}"><div><h2>{esc(ch["heading"])}</h2></div><div><p class="small">{esc(ch["intro"])}</p>'
            f'<details class="fold chron-fold"><summary>{esc(CL["list_summary"])} <span class="count">({bdi(len(items))})</span></summary>'
            f'<ol class="objs chron">{"".join(items)}</ol></details></div></section>')


# ------------------------------------------------------------------------------------------------ Evidence Directory
def evidence_directory(page: dict, shell: dict) -> str:
    L = page["labels"]; SL = shell["labels"]
    parts = [head_block(page, shell, SL["understand_explore_verify"])]
    search = (f'<section class="qa first" id="search"><div>{rubric(L["search"], tag="h2")}</div><div><div class="search-inline">'
              f'<input id="global-search" data-search-input data-search-url-state class="search-input" type="search" placeholder="{esc(L["search_placeholder"])}" aria-label="{esc(L["search"])}">'
              f'<div class="search-status" data-search-status role="status" aria-live="polite" aria-label="{esc(L["search_status"])}"></div>'
              f'<div id="search-results" data-search-results class="search-results" aria-live="polite"></div></div>'
              f'<div class="actions"><a href="{page["compare_href"]}">{esc(L["compare"])}</a></div></div></section>')
    parts.append(search)
    index = [("search", L["search"])]
    for s in page["sections"]:
        parts.append(answer(s, len(index) + 1, f"s{s['order']}"))
        index.append((f"s{s['order']}", s["heading"]))
    L2 = {**L, "visual_eyebrow": SL.get("visual_eyebrow", "")}
    b, bi = blocks(page, L2)
    parts.append(b); index += bi
    groups = []
    for g in page["hub"]:
        rows = "".join(f'<li><a href="{r["href"]}">{esc(r["title"])}</a><span class="when">{iso(esc(r["period"]))}</span></li>' for r in g["items"])
        groups.append(f'<details class="hub"><summary>{esc(g["heading"])} <span class="count">({bdi(len(g["items"]))})</span></summary><ol class="hublist">{rows}</ol></details>')
    parts.append(f'<section class="qa" id="all"><div><h2>{esc(L["hub"])}</h2></div><div class="hubs">{"".join(groups)}</div></section>')
    index.append(("all", L["hub"]))
    n, ni = next_actions(page.get("next"))
    parts.append(n); index += ni
    parts.insert(2, strip(index))   # after the search, before the register (DEBT-014)
    edges = [(page["next"]["title"] if page.get("next") else "", [f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in (page.get("next") or {}).get("links", [])])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ Comparison
def comparison(page: dict, shell: dict) -> str:
    L = page["labels"]; SL = shell["labels"]; lang = page["lang"]
    opts = "".join(f'<option value="{esc(x["id"])}">{esc(x["title"])}</option>' for x in page["records"])
    optional = f'<option value="">{esc(L["optional"])}</option>' + opts
    v = page["visual"] or {}
    boundary = (f'<section class="bnd" data-compare-boundary><span class="rubric">{esc(L["do_not"])}</span><p>{esc(v.get("prohibited_inference") or "")}</p></section>' if v else "")
    def slot(id_, label, options, kind):
        return f'<label class="slot"><span>{esc(label)}</span><select id="{id_}" data-compare-slot="{kind}">{options}</select></label>'
    controls = (slot("compare-a", L["first"], opts, "required") + slot("compare-b", L["second"], opts, "required")
                + slot("compare-c", L["third"], optional, "optional") + slot("compare-d", L["fourth"], optional, "optional"))
    data = json.dumps(page["records"], ensure_ascii=False).replace("</", "<\\/")
    dims = json.dumps(page["dimensions"], ensure_ascii=False).replace("</", "<\\/")
    # The governed lead closes with the tool's prompt on its own line ("Select at least two records."): it stands beside the
    # controls, and the runtime shows it only while fewer than two records are selected (release candidate G4 item 6)
    lead, prompt = page["lead"].rsplit("\n", 1) if "\n" in (page["lead"] or "") else (page["lead"], "")
    prompt_html = f'<p class="small compare-prompt" data-compare-prompt>{esc(prompt)}</p>' if prompt else ""
    tool = (f'<section class="qa first compare" id="compare" data-comparison-family="Comparison"><div>{rubric(L["intro"])}<h2>{esc(L["title"])}</h2></div><div>'
            + (f'<p class="st">{esc(text_alt(v))}</p>' if v else "") + boundary + prompt_html   # A3: the summary; the boundary prints once
            + f'<div class="controls-grid">{controls}</div><div class="actions"><button type="button" class="tbtn" data-compare-copy>{esc(L["copy_link"])}</button></div>'
            f'<p class="small never">{esc(L["never"])}</p><div id="compare-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div><div id="compare-output"></div>'
            f'<script type="application/json" id="yfie-compare">{data}</script><script type="application/json" id="yfie-compare-dimensions">{dims}</script></div></section>')
    parts = [head_block(page, shell, SL["understand_explore_verify"], lead=lead), tool]
    index = [("compare", L["title"])]
    pre = page.get("compare_preset")
    for s in page["sections"]:
        html_ = answer(s, len(index) + 1, f"s{s['order']}")
        if pre and s["order"] == 2 and html_.endswith("</div></section>"):   # RC-17: under "Three measures that cannot be combined"
            html_ = html_[: -len("</div></section>")] + f'<p class="small mt8" data-compare-preset><a href="{pre["href"]}">{esc(pre["label"])}</a></p></div></section>'
        parts.append(html_)
        index.append((f"s{s['order']}", s["heading"]))
    n, ni = next_actions(page.get("next"))
    parts.append(n); index += ni
    # before the tool: the comparison table is the page's whole bulk, so a strip after it indexes only what the reader
    # has already passed (the D7 phone lens measured it at 71 % of the scroll) — here the map comes first (DL-D7-011)
    parts.insert(1, strip(index))
    edges = [(page["next"]["title"] if page.get("next") else "", [f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in (page.get("next") or {}).get("links", [])])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ Data & Source
METHODS_SHELF = "measurement-methods-and-international-references"   # RC-12 (B13 c): the governed category's key


def facet_attrs(c: dict) -> str:
    """RC-12 (B13 a): the language-neutral filter keys and the sort date a source carries for the library's filters."""
    f = c.get("facets") or {}
    return "".join(f' data-f-{k}="{esc(f.get(k, ""))}"' for k in ("type", "publisher", "year", "domain", "date"))


def library_controls(page: dict, L: dict) -> str:
    """RC-12 (B13 a): the research library's filters and order. Hidden until the runtime runs, so without JavaScript
    the full list stays as it is; every option is a governed value of a listed source (no option can return nothing)."""
    def sel(key: str, label: str) -> str:
        opts = "".join(f'<option value="{esc(k)}">{esc(v)}</option>' for k, v in page["facets"][key])
        return (f'<label class="facet"><span>{esc(label)}</span><select data-source-facet="{key}">'
                f'<option value="">{esc(L["f_any"])}</option>{opts}</select></label>')
    order = (f'<label class="facet"><span>{esc(L["sort"])}</span><select data-source-sort><option value="">{esc(L["sort_grouped"])}</option>'
             f'<option value="newest">{esc(L["sort_newest"])}</option></select></label>')
    return (f'<div class="source-facets" data-source-facets hidden>{sel("type", L["f_type"])}{sel("publisher", L["f_publisher"])}'
            f'{sel("year", L["f_year"])}{sel("domain", L["f_domain"])}{order}'
            f'<button type="button" class="tbtn" data-source-facets-clear>{esc(L["f_clear"])}</button></div>')


def source_row(c: dict, L: dict, curated: bool = False) -> str:
    """A source in the register. Curated cards carry their category, why they matter and their boundary; citation
    cards their governed title, kind and date; locator-only sources their reference and locator (never a title)."""
    deps = ""
    if c["dependents"]:
        deps = (f'<details class="deps" data-dependent-evidence="{esc(c["id"])}"><summary>{esc(L["dependents"])} ({bdi(len(c["dependents"]))})</summary><ul class="rlist">'
                + "".join(f'<li><a href="{d["href"]}">{esc(d["title"])}</a></li>' for d in c["dependents"]) + "</ul></details>")
    if c.get("readings"):   # RC-12 (B13 b): the Evidence Readings that use the source
        deps += (f'<details class="deps" data-source-readings="{esc(c["id"])}"><summary>{esc(L["readings"])} ({bdi(len(c["readings"]))})</summary><ul class="rlist">'
                 + "".join(f'<li><a href="{d["href"]}">{esc(d["title"])}</a></li>' for d in c["readings"]) + "</ul></details>")
    cite = f'<button type="button" class="tbtn" data-source-cite data-source-citation="{esc(c["cite_payload"])}">{esc(L["copy_reference"])}</button>'
    # RC-12 (B13 d): a locator that is an archived copy (web.archive.org) says so on its link
    open_ = f'<a class="source-locator" href="{esc(c["url"])}" rel="noopener noreferrer" target="_blank"{" data-archived-copy" if c.get("archived") else ""}>{esc(L["open_archived"] if c.get("archived") else L["open_original"])}</a>'
    rights = f'<p class="rights" data-rights-state>{esc(c["rights_state"])}</p>'
    ref = f'<span class="rref">{esc(L["reference"])} {bdi(c["id"])}</span>'
    common = f'id="source-{esc(c["id"])}" data-source-record data-source-search="{esc(c["search"])}" tabindex="-1"' + facet_attrs(c)
    if curated:
        return (f'<article class="src card" {common}><h4 dir="auto">{esc(c["title"])}</h4><span class="kind" dir="auto">{esc(c["kind_line"])}</span>{ref}'
                # V1B-1 (owner decision B-b): the description opens on demand under "About this source"; the boundary line,
                # the reference and the cite controls stay outside the disclosure
                + (f'<details class="about" data-source-about><summary>{esc(L["about_source"])}</summary><p class="small">{esc(c["why"])}</p></details>' if c["why"] else "")
                + (f'<p class="small bnd-line"><b>{esc(L["does_not_establish"])}</b> {esc(c["does_not_establish"])}</p>' if c["does_not_establish"] else "")
                + f'<div class="acts">{open_}{cite}</div>{rights}{deps}</article>')
    if c["display_ready"] and c["title"]:
        return f'<article class="src source-locator" {common}><strong dir="auto">{esc(c["title"])}</strong><span class="kind" dir="auto">{esc(c["kind_line"])}</span>{ref}<div class="acts">{open_}{cite}</div>{rights}{deps}</article>'
    kind = f'<span class="kind" dir="auto">{esc(c["kind_line"])}</span>' if c.get("kind_line") else ""   # B5 / EAD-07: "Document type not recorded"
    return f'<article class="src source-locator" {common}><strong>{esc(L["untitled"])}</strong>{kind}{ref}<a class="source-url" dir="ltr" href="{esc(c["url"])}" rel="noopener noreferrer" target="_blank">{esc(c["url"])}</a><div class="acts">{cite}</div>{rights}{deps}</article>'


def data_sources(page: dict, shell: dict) -> str:
    L = page["labels"]; SL = shell["labels"]
    parts = [head_block(page, shell, SL["understand_explore_verify"], lead=page["lead"])]
    # RC-12 (B13 c): each curated shelf is addressable (#shelf-<key>), and the methods and international references shelf
    # is reached from the page index
    curated = "".join(f'<div class="cat" id="shelf-{esc(g["key"])}"><h3>{esc(g["category"])}</h3><div class="objs">{"".join(source_row(c, L, curated=True) for c in g["items"])}</div></div>' for g in page["curated"])
    supporting = "".join(source_row(c, L) for c in page["supporting"])
    # B5: the regulatory documents in one group with its scope line; a curated one keeps its card and is linked from here
    also = "".join(f'<p class="src-also" data-source-also data-source-search="{esc(c["search"])}"{facet_attrs(c)}><a href="#source-{esc(c["id"])}" dir="auto">{esc(c["title"])}</a>'
                   f' <span class="kind" dir="auto">{esc(c["kind_line"])} · {esc(L["curated"])}</span></p>' for c in page.get("regulatory_also") or [])
    regulatory = "".join(source_row(c, L) for c in page.get("regulatory") or [])
    reg_n = len(page.get("regulatory") or []) + len(page.get("regulatory_also") or [])
    reference = "".join(source_row(c, L) for c in page["reference"])
    tool = (f'<section class="qa first" id="directory"><div>{rubric(L["directory"], tag="h2")}</div><div><p class="small">{esc(L["intro"])}</p><p class="small">{esc(L["rights_note"])}</p>'
            f'<div class="search-inline"><input data-source-filter class="search-input" type="search" placeholder="{esc(L["filter_placeholder"])}" aria-label="{esc(L["filter"])}">'
            f'<div class="search-status" data-source-filter-status role="status" aria-live="polite"></div></div>'
            + library_controls(page, L) +
            f'<p class="small reuse-once" data-reuse-terms>{esc(L["reuse_once"])}</p>'   # B8: the reuse terms, stated once above the list
            f'<h3 class="grp" id="curated">{esc(L["curated"])} <span class="count">({bdi(page["curated_count"])})</span></h3><div class="curated">{curated}</div>'
            + (f'<details class="source-locator-details source-regulatory-details grp" id="regulatory" open><summary>{esc(L["regulatory"])} <span class="count">({bdi(reg_n)})</span></summary>'
               f'<p class="small">{esc(L["regulatory_scope"])}</p><div class="objs">{regulatory}</div>{also}</details>' if reg_n else "")
            +
            # The supporting group stays open: it is the only place a locator-only source appears, and
            # `scripts/tests/test_public_tools.py` drives that source's cite control on this page. Closing it by
            # default shortened the page by 44 % but put that governed path behind a disclosure, and Design does not
            # weaken a repository test to let its own change pass — DEBT-011 stays open (DL-D7-013).
            f'<details class="source-locator-details source-supporting-details grp" open><summary>{esc(L["supporting"])} <span class="count">({bdi(len(page["supporting"]))})</span></summary><p class="small">{esc(L["supporting_intro"])}</p><div class="objs">{supporting}</div></details>'
            f'<details class="source-locator-details source-reference-details grp"><summary>{esc(L["reference_group"])} <span class="count">({bdi(len(page["reference"]))})</span></summary><p class="small">{esc(L["reference_intro"])}</p><div class="objs">{reference}</div></details>'
            f'<div class="empty small" data-source-no-results hidden>{esc(L["no_results"])}</div></div></section>')
    parts.append(tool)
    index = [("directory", L["directory"])] + [(f"shelf-{g['key']}", g["category"]) for g in page["curated"] if g["key"] == METHODS_SHELF]
    for s in page["sections"]:
        if s.get("inventory"):
            items = "".join(f'<div><dt>{esc(x["label"])}</dt><dd dir="ltr">{esc(x["value"])}</dd></div>' for x in s["inventory"])
            parts.append(f'<section class="qa" id="s{s["order"]}"><div>{rubric(s.get("role") or "")}<h2>{esc(s["heading"])}</h2></div><dl class="inventory" data-public-inventory>{items}</dl></section>')
        elif s["order"] == 9 and page.get("chronology"):
            ch = page["chronology"]; CL = ch["labels"]
            ev = []
            for e in ch["items"]:
                src = " · ".join(f'<a href="{x["href"]}">{esc(x["title"] or x["id"])}</a>' for x in e["sources"])
                ev.append(f'<li class="compact" id="{esc(e["id"])}">{clock(L["period"], esc(e["period"]))}<div class="q">{esc(e["fact"])}</div>'
                          + (f'<div class="small"><b>{esc(CL["relevance"])}</b> {esc(e["relevance"])}</div>' if e["relevance"] else "")
                          + (f'<div class="small bnd-line"><b>{esc(CL["does_not_establish"])}</b> {esc(e["does_not_establish"])}</div>' if e["does_not_establish"] else "")
                          + (f'<div class="small"><b>{esc(CL["sources"])}</b> {src}</div>' if src else "")
                          + (f'<div class="small vnote">{esc(e["verification_note"])}</div>' if e.get("verification_note") else "") + "</li>")
            parts.append(f'<section class="qa" id="chronology"><div>{rubric(s.get("role") or "")}<h2>{esc(s["heading"])}</h2></div><div><div class="body">{body_paras(s["paragraphs"])}</div>'
                         f'<details class="fold chron-fold"><summary>{esc(ch["heading"])} <span class="count">({bdi(len(ev))})</span></summary><p class="small">{esc(ch["intro"])}</p><ol class="objs chron">{"".join(ev)}</ol></details></div></section>')
            index.append(("chronology", s["heading"]))
            continue
        else:
            kind = "bnd" if s.get("role") and ("does not establish" in s["role"].lower() or "لا يثبته" in s["role"] or "know" in s["role"].lower() or "نعرف" in s["role"]) else ""
            parts.append(answer(s, None if kind else len(index) + 1, f"s{s['order']}", kind))
        index.append((f"s{s['order']}", s["heading"]))
    b, bi = blocks(page, L)
    parts.append(b); index += bi
    nx, ni = next_actions(page.get("next"))
    parts.append(nx); index += ni
    parts.insert(1, strip(index))   # before the register: the phone reader gets the page map before the long groups (DEBT-014)
    edges = [(page["next"]["title"] if page.get("next") else "", [f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in (page.get("next") or {}).get("links", [])])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ Reading Index (family rule; composed at D3)
def reading_index(page: dict, shell: dict) -> str:
    L = page["labels"]
    parts = [head_block(page, shell, L["flow"], lead=page["lead"])]
    index = []
    if page["featured"]:
        parts.append(f'<section class="qa first" id="featured">{rubric(L["featured"], tag="h2")}<div>{reading_obj(page["featured"], L, "compact first-obj")}</div></section>')
        index.append(("featured", L["featured"]))
    items = "".join(f'<li class="compact">{clock(L["evidence_period"], esc(r["evidence_period"]))}<div class="q"><a href="{r["href"]}">{esc(r["title"])}</a></div><div class="small">{esc(r["question"])}</div></li>' for r in page["readings"])
    parts.append(f'<section class="qa" id="all"><div><h2>{esc(L["all_readings"])}</h2></div><ol class="objs">{items}</ol></section>')
    index.append(("all", L["all_readings"]))
    nx, ni = next_actions(page.get("next"))
    parts.append(nx); index += ni
    parts.insert(2 if page["featured"] else 1, strip(index))   # after the featured Reading (DEBT-014)
    edges = [(L["all_readings"], [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["readings"]])]
    return page_html(page, shell, "".join(parts), index, edges, kind="website", foot_index=False)


# ------------------------------------------------------------------------------------------------ Measurement (family rule; composed at D3)
def measurement(page: dict, shell: dict) -> str:
    L = page["labels"]
    parts = [head_block(page, shell, L["flow"], lead=page["lead"])]
    index = []
    prios = []
    for m in page["priorities"]:
        ML = m["labels"]
        more = "".join(f'<dt>{esc(x["label"])}</dt><dd>{esc(x["text"])}</dd>' for x in m.get("more") or [])
        examined = (f'<p class="small" data-measurement-readings><b>{esc(ML["examined"])}</b> ' + " · ".join(f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in m["examined"]) + "</p>") if m["examined"] else ""
        prios.append(f'<article class="obj prio" id="{esc(m["id"])}" tabindex="-1"><div class="head"><div class="clock"><span class="k">{esc(ML["priority"])}</span><span class="v">{bdi(m["priority"])} · {esc(m["domain"])}</span></div><h3>{esc(m["title"])}</h3></div>'
                     f'<div class="body">' + (f'<p data-ma-dimensions><b>{esc(ML["dimensions"])}</b> {esc(("، " if shell["lang"] == "ar" else ", ").join(m["dimensions"]))}</p>' if m.get("dimensions") else "")
                     + f'<p><b>{esc(ML["current"])}</b> {esc(m["current"])}</p><p><b>{esc(ML["missing"])}</b> {esc(m["missing"])}</p><p><b>{esc(ML["unlocked"])}</b> {esc(m["unlocked"])}</p>'
                     + (f'<div data-ma-decisions><p><b>{esc(ML["decisions"])}</b></p><ul class="rlist">' + "".join(f"<li>{esc(x)}</li>" for x in m["decisions"]) + "</ul></div>" if m.get("decisions") else "")
                     + (f'<p data-ma-blocked><b>{esc(ML["blocked"])}</b> {esc(m["blocked"])}</p>' if m.get("blocked") else "")   # B6
                     + f'</div>{examined}'
                     f'<div class="ref"><b>{esc(ML["reference"])}</b> {bdi(m["id"])}</div>' + (f'<details class="more"><summary>{esc(ML["more"])}</summary><dl class="kv">{more}</dl></details>' if more else "") + "</article>")
    ag = next((s for s in page["sections"] if s["order"] == 10), None)
    first_secs = [s for s in page["sections"] if s["order"] != 10]
    for s in first_secs:
        kind = "bnd" if s.get("role") and ("does not establish" in s["role"].lower() or "لا يثبته" in s["role"] or "know" in s["role"].lower() or "نعرف" in s["role"]) else ""
        parts.append(answer(s, None if kind else len(index) + 1, f"s{s['order']}", kind))
        index.append((f"s{s['order']}", s["heading"]))
    head_ag = (f'<div>{rubric(ag.get("role") or "")}<h2>{esc(ag["heading"])}</h2></div><div class="body">{body_paras(ag["paragraphs"])}</div>' if ag else "")
    parts.append(f'<section class="qa" id="agenda">{head_ag}</section><div class="prios">{"".join(prios)}</div>')
    if ag:
        index.append(("agenda", ag["heading"]))
    b, bi = blocks(page, L)
    parts.append(b); index += bi
    nx, ni = next_actions(page.get("next"))
    parts.append(nx); index += ni
    parts.insert(1, strip(index))   # after the head: the map before the answers and the agenda (DEBT-014)
    edges = [(ag["heading"] if ag else "", [f'<a href="#{esc(m["id"])}">{esc(m["title"])}</a>' for m in page["priorities"]])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ Reference / Trust (family rule; composed at D3)
def reference(page: dict, shell: dict) -> str:
    L = page["labels"]
    parts = [head_block(page, shell, L["flow"], lead=page["lead"])]
    index = []
    ctx = page.get("context")
    if ctx:
        ids = json.dumps(ctx["record_ids"]).replace("</", "<\\/")
        origin_html = (f'<div class="correction-origin" data-correction-origin hidden><span class="small">{esc(ctx["current"])}</span> <strong data-correction-record dir="ltr"></strong> '
                       f'<a data-correction-link href="#">{esc(ctx["open"])}</a></div>'
                       f'<div class="correction-link-error empty small" data-correction-error hidden role="alert" data-msg-malformed="{esc(ctx["malformed"])}" data-msg-unknown="{esc(ctx["unknown"])}"></div>'
                       f'<script type="application/json" id="yfie-record-ids">{ids}</script>')
        if ctx["mode"] == "contact":
            mail = f'<a class="mail" data-correction-mail hidden href="mailto:{esc(ctx["address"])}" data-mail-address="{esc(ctx["address"])}" data-mail-subject="{esc(ctx["subject"])}">{esc(ctx["write"])}</a>'
            parts.append(f'<section class="qa first ctx" data-correction-context data-context-mode="contact"><div></div><div>{origin_html}<div class="actions">{mail}</div></div></section>')
        else:
            parts.append(f'<section class="qa first ctx" id="record" data-correction-context><div><h2>{esc(ctx["title"])}</h2></div><div><p class="small">{esc(ctx["intro"])}</p><div class="small" data-correction-empty>{esc(ctx["empty"])}</div>{origin_html}</div></section>')
            index.append(("record", ctx["title"]))
    if page.get("reading_rule"):   # owner instructions of 3 October 2026, 09:50, C5: printed once, here
        rr = page["reading_rule"]
        parts.append(answer({"heading": rr["heading"], "role": "", "paragraphs": [rr["copy"]]}, len(index) + 1, "how-numbers"))
        index.append(("how-numbers", rr["heading"]))
    for s in page["sections"]:
        parts.append(answer(s, len(index) + 1, f"s{s['order']}"))
        index.append((f"s{s['order']}", s["heading"]))
    b, bi = blocks(page, L)
    parts.append(b); index += bi
    nx, ni = next_actions(page.get("next"))
    parts.append(nx); index += ni
    parts.insert(2 if ctx else 1, strip(index))   # after the report context where one exists (DEBT-014)
    edges = [(page["next"]["title"] if page.get("next") else "", [f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in (page.get("next") or {}).get("links", [])])]
    return page_html(page, shell, "".join(parts), index, edges, foot_index=False)


# ------------------------------------------------------------------------------------------------ root and 404
def root_page(shell_ar: dict, shell_en: dict) -> str:
    origin = R.DISC.origin()
    links = R.DISC.head_links("/", "ar", origin).split(">", 1)[1]
    return (f'<!doctype html><html><head><meta charset="utf-8">{R.DISC.robots_meta()}<link rel="icon" type="image/png" sizes="32x32" href="/assets/logo/CauseWay_logo_32.png"><title>{esc(shell_ar["product"])} · {esc(shell_en["product"])}</title>{links}'
            f'<script src="/assets/lang-redirect.js"></script><noscript><meta http-equiv="refresh" content="0;url=/ar/"></noscript></head></html>')


def not_found(page: dict, shell_ar: dict) -> str:
    """The bilingual 404: Arabic first (as the root route), every word governed; the search dialog and runtime only."""
    def section(lang):
        s = page["sections"][lang]; h = "h1" if lang == "ar" else "h2"
        hid = ' id="page-title"' if lang == "ar" else ""
        return (f'<section lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}" class="nf"><{h}{hid}>{esc(s["heading"])}</{h}><p class="st">{esc(s["body"])}</p>'
                f'<div class="actions"><a href="/{lang}/">{esc(s["home"])}</a><a href="/{lang}/explore/">{esc(s["explore"])}</a><a href="/{lang}/evidence/">{esc(s["evidence"])}</a>'
                f'<button type="button" class="tbtn" data-search-open>{esc(s["search"])}</button></div></section>')
    return (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/png" sizes="32x32" href="/assets/logo/CauseWay_logo_32.png">'
            f'<title>{esc(page["title"]["ar"])} — {esc(page["product"]["en"])}</title>{R.DISC.robots_meta("noindex")}<link rel="stylesheet" href="/assets/yfie.css"></head><body>'
            f'<main id="main"><div class="page"><article class="obj page-obj"><div class="head">{R.logo(48)}<span class="rubric">404 · {esc(page["title"]["ar"])} / <span dir="ltr">{esc(page["title"]["en"])}</span></span></div>'
            f'{section("ar")}{section("en")}</article></div></main>{R.search_dialog(shell_ar)}{json_block("yfie-ui", shell_ar["ui_json"])}<script src="/assets/app.js" defer></script></body></html>')


RENDERERS = {"Question Entry": question_entry, "Domain Answer": domain, "Evidence Directory": evidence_directory, "Comparison": comparison,
             "Data & Source": data_sources, "Reading Index": reading_index, "Measurement": measurement, "Reference / Trust": reference}
