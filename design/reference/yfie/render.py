# -*- coding: utf-8 -*-
"""Reference renderer — the accepted D1 direction, T4 · Instrument (design/01_FOUNDATIONS.md §3.6, §4).

One mental model: YFIE is an instrument that answers the reader's questions about the evidence and states what it
cannot answer. Every bound evidence object opens with its clock (when, for whom) before its statement; the seven
governed questions are the Record's structure and index; every boundary is one second voice; a verification spine
sits on every page; unlike things never share an axis, a row or a colour. Composed mobile-first; Arabic with its own
metrics. This module carries the same test hooks as the neutral harness (brief §19) and no inline style or script.

Governed text is rendered exactly as the content module gives it; pacing on Home is presentation only (DEBT-008).
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import discovery as DISC  # noqa: E402  (F6: one implementation of canonical, hreflang, Open Graph and structured data)

from . import theme  # noqa: E402
from .visuals import figure, num  # noqa: E402

CUR = ' aria-current="page"'
ISO = re.compile(r"\d{4}-\d{2}-\d{2}")
SENT = re.compile(r"(?<=[.؟?!])\s+(?=[A-Z«؀-ۿ])")
GROUP_STARTS = ("In the same survey", "Separately,", "These are different measures", "وفي المسح نفسه", "وبصورة منفصلة", "هذه مقاييس مختلفة")
RESOLUTION = ("These are different measures", "هذه مقاييس مختلفة")


def esc(x) -> str:
    return html.escape(str(x or ""), quote=True)


def bdi(x) -> str:
    return f'<bdi dir="ltr">{esc(x)}</bdi>'


def iso(escaped: str) -> str:
    """ISO dates inside governed text as unbroken left-to-right runs (presentation only)."""
    return ISO.sub(lambda m: f'<bdi dir="ltr" class="nw">{m.group(0)}</bdi>', escaped)


def paras(items, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{esc(p)}</p>" for p in items)


def json_block(id_: str, data) -> str:
    return f'<script type="application/json" id="{id_}">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ------------------------------------------------------------------------------------------------ build hook
def assets(out: Path, variant: str = "") -> None:
    """Write the stylesheet. Fonts and the logo are copied unchanged by the build."""
    (out / "assets" / "yfie.css").write_text(theme.FONT_FACES + "\n" + theme.CSS, encoding="utf-8")


# ------------------------------------------------------------------------------------------------ shell
def head(page: dict, shell: dict, route: str, kind: str = "website", extra: str = "") -> str:
    lang = shell["lang"]
    origin = DISC.origin()
    return (f'<!doctype html><html lang="{lang}" dir="{shell["dir"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(page["title"])} — {esc(shell["product"])}</title>'
            f'<meta name="description" content="{esc(page.get("meta_description"))}">{extra}<link rel="stylesheet" href="/assets/yfie.css">'
            f'{DISC.head_links(route, lang, origin)}{DISC.social_meta(page["title"], page.get("meta_description") or "", lang, route, shell["product"], kind, origin)}'
            f"</head><body>")


def logo(px: int) -> str:
    return f'<img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay" width="{px}" height="{px}">'


def header(shell: dict) -> str:
    L = shell["labels"]
    other = shell["other_lang"]
    nav = []
    for item in shell["nav"]:
        if item.get("children"):
            kids = "".join(f'<a href="{k["href"]}"{CUR if k["active"] else ""}>{esc(k["label"])}</a>' for k in item["children"])
            nav.append(f'<span class="group" role="group" aria-label="{esc(item["label"])}"><span class="glabel">{esc(item["label"])}</span>{kids}</span>')
        else:
            nav.append(f'<a href="{item["href"]}"{CUR if item.get("active") else ""}>{esc(item["label"])}</a>')
    return (f'<noscript><div class="noscript">{esc(L["noscript"])}</div></noscript><a class="skip" href="#main">{esc(L["skip"])}</a>'
            f'<header class="bar"><div class="bar-in"><a class="brand" href="{shell["home_href"]}" aria-label="CauseWay — {esc(shell["product"])}">{logo(40)}<span class="brand-name">{esc(shell["product"])}</span></a>'
            f'<nav id="primary-nav" class="nav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div class="controls"><button type="button" class="tbtn" data-search-open aria-label="{esc(L["search"])}">{esc(L["search"])}</button>'
            f'<button type="button" class="tbtn cite" data-cite aria-label="{esc(L["cite"])}">{esc(L["cite"])}</button>'
            f'<a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" data-lang="{other}" aria-label="{esc(L["lang_switch_action"])}" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button>'
            f'<button type="button" class="tbtn menu" data-menu aria-label="{esc(L["menu"])}" aria-controls="primary-nav" aria-expanded="false">{esc(L["menu"])}</button></div>'
            f'<div id="utility-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true" data-copied-label="{esc(L["copied"])}"></div></div></header>'
            f'<dialog id="search-dialog" class="search" aria-labelledby="search-dialog-title"><div class="search-panel"><div class="search-head"><strong id="search-dialog-title">{esc(L["search_title"])}</strong>'
            f'<button type="button" class="tbtn" data-search-close aria-label="{esc(L["search_close"])}">{esc(L["search_close"])}</button></div>'
            f'<input id="global-search-dialog" data-search-input class="search-input" placeholder="{esc(L["search_placeholder"])}" aria-label="{esc(L["search"])}">'
            f'<div class="search-status" data-search-status role="status" aria-live="polite" aria-label="{esc(L["search_status"])}"></div><div data-search-results class="search-results"></div></div></dialog>'
            f'<main id="main"><div class="page">')


def footer(shell: dict) -> str:
    L = shell["labels"]
    trust = "".join(f'<a href="{t["href"]}"{CUR if t.get("active") else ""}>{esc(t["label"])}</a>' for t in shell["trust"])
    trust_label = next((g["label"] for g in shell["footer"] if any(l["href"].endswith("/about/") for l in g["links"])), L["trust_nav"])
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>"
                     for g in shell["footer"] if not any(l["href"].endswith("/about/") for l in g["links"]))
    return (f'</div></main><footer class="inst"><div class="inst-in"><div class="trust"><h3>{esc(trust_label)}</h3><nav aria-label="{esc(L["trust_nav"])}">{trust}</nav></div>'
            f'<div class="id">{logo(40)}<p>{esc(L["footer_strapline"])}</p></div><nav class="groups" aria-label="{esc(L["footer_nav"])}">{groups}</nav>'
            f'<div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></div></footer>'
            f'{json_block("yfie-ui", shell["ui_json"])}<script src="/assets/app.js" defer></script></body></html>')


# ------------------------------------------------------------------------------------------------ objects
def rubric(t, n: int | None = None, tag: str = "span", cls: str = "rubric") -> str:
    num_ = f'<span class="n">{n:02d}</span>' if n else ""
    return f'<{tag} class="{cls}">{num_}{esc(t)}</{tag}>'


def clock(label, value_escaped: str) -> str:
    return f'<div class="clock"><span class="k">{esc(label)}</span><span class="v">{iso(value_escaped)}</span></div>'


def crumb(bc: dict | None, shell: dict) -> str:
    if not bc:
        return ""
    cur = bdi(bc["current"]) if bc["mode"] == "STABLE_OBJECT_ID" else esc(bc["current"])
    return f'<nav class="crumb" aria-label="{esc(shell["labels"]["breadcrumb"])}"><a href="{bc["parent_href"]}">{esc(bc["parent_label"])}</a> / <span aria-current="page">{cur}</span></nav>'


def source_card(s: dict) -> str:
    L = s["labels"]
    ref = f'<span class="rref">{esc(s["reference_label"])} {bdi(s["id"])}</span>'
    head_ = (f'<strong dir="auto">{esc(s["title"])}</strong><span class="kind" dir="auto">{esc(s["kind_line"])}</span>{ref}' if s["display_ready"] and s["title"]
             else f'<strong>{esc(s["untitled_label"])}</strong>{ref}')
    rights = f'<p class="rights">{esc(s["rights_note"])}</p>' if s["rights_note"] else ""
    return (f'<article class="src" data-evidence-source="{esc(s["id"])}">{head_}<div class="acts"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a>'
            f'<a class="source-locator" href="{esc(s["url"])}" rel="noopener noreferrer" target="_blank">{esc(L["open_original"])}</a>'
            f'<button type="button" class="tbtn" data-source-cite data-source-citation="{esc(s["cite_payload"])}">{esc(L["copy_reference"])}</button></div>{rights}</article>')


def compact(rec: dict, L: dict, open_label: str, cls: str = "compact") -> str:
    """Clock-first compact evidence object: when → title → for whom → open."""
    ck = clock(L["period"], esc(rec.get("period") or ""))
    return (f'<article class="{cls}">{ck}<div class="q"><a href="{rec["href"]}">{esc(rec["title"])}</a></div>'
            + (f'<div class="small">{esc(rec["universe"])}</div>' if rec.get("universe") else "")
            + f'<div class="open"><a href="{rec["href"]}">{esc(open_label)}</a></div></article>')


def spine(index: list, edges: list, foot: bool = False, foot_index: bool = True) -> str:
    """The verification spine. Exactly one is visible at any width: beside the object from 900 px (index + edges), at
    the object's foot below (index unless the page carries a strip, + edges). Accessible name: escalated (DEBT-006)."""
    idx = "".join(f'<li><a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a></li>' for i, (a, t) in enumerate(index))
    ed = "".join(f'<div class="edges"><h3>{esc(e[0])}</h3>' + (f'<p class="small">{esc(e[2])}</p>' if len(e) > 2 and e[2] else "") + "<ul>" + "".join(f"<li>{x}</li>" for x in e[1]) + "</ul></div>" for e in edges if e[1])
    cls = "spine foot-spine" if foot else "spine"
    index_html = f'<nav class="index"><ul>{idx}</ul></nav>' if (not foot or foot_index) else ""
    return f'<aside class="{cls}">{index_html}{ed}</aside>'


def strip(index: list) -> str:
    return '<nav class="strip">' + "".join(f'<a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a>' for i, (a, t) in enumerate(index)) + "</nav>"


def paced_groups(text: str) -> list[tuple[bool, str]]:
    """The governed paragraph paced as figure groups (a new group at each governed connective that introduces another
    measure; the last group is the resolution). Words and order intact. Falls back to the whole paragraph when no
    connective is found (DEBT-008)."""
    sents = [x.strip() for x in SENT.split(text) if x.strip()]
    groups, cur = [], []
    for s in sents:
        if cur and s.startswith(GROUP_STARTS):
            groups.append(cur); cur = []
        cur.append(s)
    if cur:
        groups.append(cur)
    if len(groups) < 2:
        return [(False, f"<p>{esc(text)}</p>")]
    return [(g[0].startswith(RESOLUTION), f'<p class="{"sent res" if g[0].startswith(RESOLUTION) else "sent"}">{" ".join(esc(x) for x in g)}</p>') for g in groups]


# ------------------------------------------------------------------------------------------------ pages
def evidence_record(page: dict, shell: dict) -> str:
    L = page["labels"]
    meta = f'<meta name="yfie-citation" content="{esc(page["citation"])}"><meta name="yfie-record-id" content="{esc(page["id"])}">'
    index = [("q1", L["establishes"]), ("q2", L["measures"]), ("q3", L["applies"]), ("q4", L["currentness"]), ("q5", L["does_not_establish"]), ("q6", L["source"]), ("q7", L["more"])]
    head_ = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["family"])}{clock(L["period"], esc(page["period"]))}<h1>{esc(page["title"])}</h1>'
             + (f'<p class="st">{esc(page["lead"])}</p>' if page["lead"] else "") + "</div>")
    qa = [f'<div class="qa first" id="q1">{rubric(L["establishes"], 1, "h2")}<div class="st"><p>{esc(page["summary"])}</p></div></div>' + strip(index),
          f'<div class="qa" id="q2">{rubric(L["measures"], 2, "h2")}<div class="body"><p>{esc(page["definition"])}</p></div></div>',
          f'<div class="qa" id="q3">{rubric(L["applies"], 3, "h2")}<div class="body"><p>{esc(page["universe"])}</p></div></div>',
          f'<div class="qa" id="q4">{rubric(L["currentness"], 4, "h2")}<div class="body"><p>{esc(page["currentness"])}</p></div></div>']
    limits = f'<h3>{esc(L["measurement_limits"])}</h3><p>{esc(page["measurement_limits"])}</p>' if page["measurement_limits"] else ""
    qa.append(f'<section class="bnd" id="q5" data-evidence-boundary-first-load data-boundary-part="does-not-establish">{rubric(L["does_not_establish"], 5, "h2")}<p>{esc(page["does_not_establish"])}</p>{limits}</section>')
    chips = "".join(f'<a class="chip" href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}">{bdi(sid)}</a>' for sid in page["trace_ids"])
    src_extra = ""
    if page["sources_without_locator_note"]:
        src_extra += f'<p class="small" data-evidence-sources-without-locator>{esc(page["sources_without_locator_note"])}</p>'
    if page["members"]:
        src_extra += f'<h3>{esc(page["members_heading"])}</h3><ul class="rlist">' + "".join(f'<li><a href="{m["href"]}">{esc(m["title"])}</a> {bdi(m["id"])}</li>' for m in page["members"]) + "</ul>"
    if page["lineage_statement"]:
        src_extra += f'<p class="small" data-lineage-state="{esc(page["closure_state"])}">{esc(page["lineage_statement"])}</p>'
    if page["no_source_message"]:
        src_extra += f'<p class="small empty" data-evidence-source-unavailable>{esc(page["no_source_message"])}</p>'
    trace = (f'<div class="mt16"><span class="small"><b>{esc(L["trace"])}</b> · {esc(L["trace_intro"])}</span><div class="chips"><span class="chip">{bdi(page["id"])}</span>{chips}</div></div>' if page["trace_ids"] else "")
    qa.append(f'<section class="qa" id="q6"><div>{rubric(L["source"], 6, "h2")}<span id="source"></span></div><div><p class="small">{esc(L["source_intro"])}</p><div class="mt10">{"".join(source_card(s) for s in page["sources"])}</div>{src_extra}{trace}</div></section>')
    more = "".join(f'<div class="qa"><h3 class="rubric">{esc(L[k])}</h3><div class="body"><p>{esc(page[k])}</p></div></div>' for k in ("method", "change_trigger", "verification") if page[k])
    if page["reading_guidance"]:
        more += f'<div class="qa"><h3 class="rubric">{esc(L["reading_guidance"])}</h3><div class="body">{paras(page["reading_guidance"]["paragraphs"])}</div></div>'
    qa.append(f'<div class="qa" id="q7">{rubric(L["more"], 7, "h2")}<details class="more"><summary>{esc(L["more_intro"])}</summary>{more}</details></div>')
    util = (f'<section class="util" data-record-id="{esc(page["id"])}"><div class="ref"><b>{esc(L["reference"])}</b> {bdi(page["id"])}</div>'
            f'<div class="actions"><button type="button" class="tbtn evidence-cite-button" data-cite>{esc(L["cite"])}</button><a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a>'
            f'<a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div><p class="small">{esc(L["reuse_note"])}</p></section>')
    used = [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in page["used_in_readings"]]
    edges = [(L["used_in"], used),
             (L["related"], [f'<a href="{x["href"]}">{esc(x["label"])}</a>' for x in page["routes_back"]] + [f'<a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a>', f'<a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a>', f'<a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a>'], L["related_intro"])]
    used_attr = " data-used-in-readings" if used else ""
    body = f'<article class="obj page-obj"{used_attr}>{head_}{"".join(qa)}{util}</article>{spine(index, edges)}{spine(index, edges, foot=True, foot_index=False)}'
    return head(page, shell, page["route"], extra=meta) + header(shell) + body + footer(shell)


def home(page: dict, shell: dict) -> str:
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    index = [("s3", S[3]["heading"]), ("s4", S[4]["heading"]), ("s9", S[9]["heading"]), ("s5", S[5]["heading"]), ("s6", S[6]["heading"]), ("s7", S[7]["heading"]), ("s8", S[8]["heading"]), ("sf", L["featured"])]
    parts = [f'<div class="head">{rubric(L["product"])}<h1>{esc(page["title"])}</h1></div>']
    recs = list(page["records"])
    demo = []
    for res, html_ in paced_groups(S[3]["body"]):
        demo.append(html_)
        if recs and not res:
            demo.append(compact(recs.pop(0), L, L["open_evidence_record"], cls="compact bound"))
    def h2(sec):   # governed kicker (role) above the governed heading
        return (f'<span class="rubric">{esc(sec["role"])}</span>' if sec.get("role") else "") + f'<h2>{esc(sec["heading"])}</h2>'
    parts.append(f'<section class="qa first" id="s3"><div>{h2(S[3])}</div><div class="paced">{"".join(demo)}</div></section>')
    if recs:
        parts.append(f'<div class="qa">{rubric(L["records_heading"])}<div class="objs">{"".join(compact(r, L, L["open_evidence_record"]) for r in recs)}</div></div>')
    parts.append(f'<section class="bnd" id="s4">{rubric(S[4]["role"])}<h2>{esc(S[4]["heading"])}</h2><div class="mt8">{paras(S[4]["paragraphs"])}</div></section>')
    parts.append(f'<section class="qa" id="s1">{rubric(L["flow"])}<div><div class="st">{paras(S[1]["paragraphs"])}</div><p class="small">{esc(L["side"])}</p><div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div></div></section>')
    qs = "".join(f'<li><div><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="gets small">{esc(q["gets"])}</div></div></li>' for q in page["starting_questions"])
    parts.append(f'<section class="qa" id="s9"><div><span class="rubric">{esc(L["questions_eyebrow"])}</span><h2>{esc(S[9]["heading"])}</h2></div><div><p class="st">{esc(L["questions_title"])}</p><p class="small">{esc(S[9]["body"])}</p><ol class="qlist">{qs}</ol><p class="small mt12"><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p></div></section>')
    parts.append(f'<section class="qa" id="s5"><div>{h2(S[5])}</div><div class="body">{paras(S[5]["paragraphs"])}</div></section>')
    v = page["system_visual"]
    parts.append(f'<section class="qa" id="s6"><div>{rubric(S[6]["role"])}<h2 id="system" tabindex="-1">{esc(S[6]["heading"])}</h2></div><div><div class="body">{paras(S[6]["paragraphs"])}</div>'
                 f'<span class="rubric mt18">{esc(L["visual_eyebrow"])}</span>{figure(v, shell["labels"]["cite"], DISC.origin(), heading="h3", boundary_label=L["boundary"], open_label=L["open_record"])}</div></section>')
    for o, i in ((7, "s7"), (8, "s8")):
        parts.append(f'<section class="qa" id="{i}"><div>{h2(S[o])}</div><div class="body">{paras(S[o]["paragraphs"])}</div></section>')
    f = page["featured"]
    if f:
        parts.append(f'<section class="qa" id="sf">{rubric(L["featured"], tag="h2")}<div><article class="compact first-obj">{clock(L["evidence_period"], esc(f["evidence_period"]))}<div class="q"><a href="{f["href"]}">{esc(f["title"])}</a></div><div class="st"><p>{esc(f["thesis"])}</p></div><div class="open"><a href="{f["href"]}">{esc(L["open_reading"])}</a> · <a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></div></article></div></section>')
    edges = [(f'{L["records_heading"]} ({len(page["records"])})', [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["records"]]),
             (L["flow"], [f'<a href="{h}">{esc(t)}</a><br><span class="small">{esc(d)}</span>' for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"]))])]
    body = f'<article class="obj page-obj">{"".join(parts)}{page_util(shell)}</article>{spine(index, edges)}{spine(index, edges, foot=True)}'
    return head(page, shell, "/") + header(shell) + body + footer(shell)


def reading(page: dict, shell: dict) -> str:
    L = page["labels"]; SL = shell["labels"]
    origin = DISC.origin()
    index = [(f's-{s["section_id"]}', s["heading"]) for s in page["sections"] if s["heading"]] + [("trace", L["trace"]), ("sources", L["sources"]), ("related", L["related"])]
    head_ = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["eyebrow"])}<p class="q">{esc(page["question"])}</p><h1>{esc(page["title"])}</h1><div class="st"><p>{esc(page["thesis"])}</p></div>'
             f'<div class="clocks">{clock(L["evidence_period"], esc(page["evidence_period"]))}<div class="clock"><span class="k">{esc(L["last_reviewed"])}</span><span class="v"><time datetime="{esc(page["last_reviewed_iso"])}">{esc(page["last_reviewed"])}</time></span></div></div></div>')
    bnd = f'<section class="bnd" data-reading-boundary>{rubric(L["do_not_infer"], tag="h2")}<p>{esc(page["prohibited_inference"])}</p></section>'
    essay = []
    for i, s in enumerate(page["sections"]):
        h = f'<h2 id="s-{esc(s["section_id"])}">{esc(s["heading"])}</h2>' if s["heading"] else ""
        blocks = []
        for b in s["blocks"]:
            if b["kind"] == "p":
                blocks.append(f'<p>{esc(b["text"])}</p>')
            elif b["kind"] == "pull":
                blocks.append(f'<blockquote class="pull"><p>{esc(b["text"])}</p></blockquote>')
            else:
                blocks.append('<ul class="rlist">' + "".join(f"<li>{esc(x)}</li>" for x in b["items"]) + "</ul>")
        figs = "".join(figure(v, SL["cite"], origin) for v in page["visuals"]) if i == 0 else ""
        essay.append(f'<section data-reading-section="{esc(s["section_id"])}">{h}<div class="{"st" if i == 0 else "read"}">{"".join(blocks)}</div>{figs}</section>')
    steps = []
    for x in page["trace"]:
        srcs = " · ".join(f'<a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a>' for s in x["sources"])
        if srcs:
            srcs = f'{esc(L["source_record"])}: ' + srcs
        if x["no_locator_note"]:
            srcs += (" · " if srcs else "") + esc(x["no_locator_note"])
        flag = f' · <span data-path-state>{esc(x["state_flag"])}</span>' if x["state_flag"] else ""
        steps.append(f'<article class="compact" data-path-record="{esc(x["id"])}">{clock(L["evidence_period"], esc(x["period"]))}<div class="q"><a href="{x["href"]}">{esc(x["proposition"])}</a></div><div class="small">{esc(L["reference"])} {bdi(x["id"])}{flag}</div><div class="small">{srcs}</div></article>')
    compare = f'<div class="actions"><a href="{page["compare_href"]}">{esc(L["compare"])}</a></div>' if page["compare_href"] else ""
    trace = (f'<section class="qa" id="trace" data-reading-verify data-reading-path-state="{esc(page["trace_state"])}"><h2>{esc(L["trace"])}</h2><div><p class="small">{esc(L["trace_intro"])}</p><p class="small"><b>{esc(page["trace_status"])}</b></p><div class="objs">{"".join(steps)}</div>{compare}</div></section>')
    sources = f'<section class="qa" id="sources"><h2>{esc(L["sources"])}</h2><div>{"".join(source_card(s) for s in page["sources"])}</div></section>' if page["sources"] else ""
    rel = "".join(f'<article class="compact">{clock(L["evidence_period"], esc(x["evidence_period"]))}<div class="q"><a href="{x["href"]}">{esc(x["title"])}</a></div><div class="small">{esc(x["thesis"])}</div></article>' for x in page["related"])
    related = f'<section class="qa" id="related" data-reading-related><h2>{esc(L["related"])}</h2><div><div class="objs">{rel}</div><p class="small mt12"><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></p></div></section>' if page["related"] else ""
    edges = [(L["trace"], [f'<a href="{x["href"]}">{esc(x["proposition"])}</a>' for x in page["trace"]]),
             (L["return"], [f'<a href="{b["href"]}">{esc(b["label"])}</a>' for b in page["return_to"]])]
    body = f'<article class="obj page-obj">{head_}{bnd}<div class="essay">{"".join(essay)}</div>{trace}{sources}{related}{page_util(shell)}</article>{spine(index, edges)}{spine(index, edges, foot=True)}'
    return head(page, shell, page["route"], kind="article") + header(shell) + body + footer(shell)


def page_util(shell: dict) -> str:
    """The page's own actions at the foot of its object (cite, report), reachable at every width — the product bar
    shows them only on wide screens."""
    L = shell["labels"]
    return (f'<section class="util"><div class="actions"><button type="button" class="tbtn" data-cite>{esc(L["cite"])}</button>'
            f'<a href="{shell["contact_href"]}">{esc(L["report"])}</a></div></section>')


RENDERERS = {"Orientation": home, "Evidence Record": evidence_record, "Reading": reading}


def render(page: dict, shell: dict, variant: str = "") -> str:
    return RENDERERS[page["family"]](page, shell)
