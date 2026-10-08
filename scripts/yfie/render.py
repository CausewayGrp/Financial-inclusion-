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

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import discovery as DISC  # noqa: E402  (F6: one implementation of canonical, hreflang, Open Graph and structured data)

from . import theme  # noqa: E402
from .visuals import figure, num  # noqa: E402

CUR = ' aria-current="page"'
SENT = re.compile(r"(?<=[.؟?!])\s+(?=[A-Z«؀-ۿ])")
GROUP_STARTS = ("In the same survey", "Separately,", "These are different measures", "وفي المسح نفسه", "وبصورة منفصلة", "هذه مقاييس مختلفة")
RESOLUTION = ("These are different measures", "هذه مقاييس مختلفة")


from .text import ID_RUN, bdi, esc, isolate_document, isolate_iso as iso, isolate_plain  # noqa: E402  (one text layer for every renderer, D6; `iso` takes escaped text)


def paras(items, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{esc(p)}</p>" for p in items)


def json_block(id_: str, data) -> str:
    return f'<script type="application/json" id="{id_}">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ------------------------------------------------------------------------------------------------ build hook
def assets(out: Path, variant: str = "") -> None:
    """Write the stylesheet. Fonts and the logo are copied unchanged by the build."""
    (out / "assets" / "yfie.css").write_text(theme.FONT_FACES + "\n" + theme.CSS + "\n" + theme.CSS_D2 + "\n" + theme.CSS_D6, encoding="utf-8", newline="\n")


# ------------------------------------------------------------------------------------------------ shell
def head(page: dict, shell: dict, route: str, kind: str = "website", extra: str = "") -> str:
    lang = shell["lang"]
    origin = DISC.origin()
    return (f'<!doctype html><html lang="{lang}" dir="{shell["dir"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">{DISC.robots_meta()}<link rel="icon" type="image/png" sizes="32x32" href="/assets/logo/CauseWay_logo_32.png"><title>{esc(page["title"])} — {esc(shell["product"])}</title>'
            f'<meta name="description" content="{esc(page.get("meta_description"))}">{extra}<link rel="stylesheet" href="/assets/yfie.css">{font_preloads(lang)}'
            f'{DISC.head_links(route, lang, origin)}{DISC.social_meta(page["title"], page.get("meta_description") or "", lang, route, shell["product"], kind, origin)}'
            f"{structured_data(page, shell, route)}</head><body>")


def font_preloads(lang: str) -> str:
    """The two faces a first paint needs in the page's language — Regular (body) and SemiBold (headings, values,
    emphasis) — preloaded from the shipped files (D7, DL-D7-005; `08_ASSET_MAP.md` §2). Medium and the other
    language's faces load on demand with `font-display: swap`. Same origin; `crossorigin` because fonts are fetched in
    CORS mode and a preload without it is fetched twice."""
    folder, stem = ("ibm-plex-sans-arabic", "IBMPlexSansArabic") if lang == "ar" else ("ibm-plex-sans", "IBMPlexSans")
    return "".join(f'<link rel="preload" as="font" type="font/woff2" crossorigin href="/assets/fonts/{folder}/{stem}-{w}.woff2">' for w in ("Regular", "SemiBold"))


def structured_data(page: dict, shell: dict, route: str) -> str:
    """The structured data the baseline writes (F6, one implementation in scripts/discovery.py): WebSite on Home, a
    BreadcrumbList where the page shows its governed breadcrumb, an Article on a Reading — governed fields only, from
    the same content path as the visible breadcrumb (D7: kept byte for byte with dist/, asserted by check_acceptance.py)."""
    lang = shell["lang"]; origin = DISC.origin(); out = []
    crumb = page.get("breadcrumb") or {}
    parent_route = re.sub(r"^/(?:en|ar)(?=/)", "", crumb.get("parent_href") or "")
    if route == "/":
        out.append(DISC.website_ld(lang, shell["product"], origin))
    elif page["family"] == "Evidence Record" and parent_route and page.get("id"):
        out.append(DISC.breadcrumb_ld(parent_route, crumb.get("parent_label") or "", page["id"], lang, origin))
    elif page["family"] == "Reading" and page.get("title"):
        if parent_route:
            out.append(DISC.breadcrumb_ld(parent_route, crumb.get("parent_label") or "", page["title"], lang, origin))
        if page.get("thesis"):
            out.append(DISC.article_ld(route, lang, page["title"], page["thesis"], shell["product"], origin))
    return "".join(DISC.ld_script(x) for x in out)


LOGO_SIZES = (32, 40, 48, 64, 72, 80, 96, 144)   # scripts/logo_derivatives.py: pure resamples of the unchanged master (EAD-03)


def logo(px: int, sizes: str = "") -> str:
    """The canonical mark at an interface size: a web-size derivative (EAD-03, owner decision of 2 October 2026) — the
    1× file as src and the 1× and 2× files of every size the surface can take in srcset, so a phone never downloads the
    10 MB master. `sizes` names the surface's CSS widths where they change (the product bar: 40 px, 48 px from 900 px)."""
    widths = sorted({w for w in LOGO_SIZES if w in (px, px * 2)} | ({w for s in (40, 48) for w in (s, s * 2)} if sizes else set()))
    srcset = ", ".join(f"/assets/logo/CauseWay_logo_{w}.png {w}w" for w in widths)
    return (f'<img src="/assets/logo/CauseWay_logo_{px}.png" srcset="{srcset}" sizes="{sizes or f"{px}px"}" '
            f'alt="CauseWay" width="{px}" height="{px}">')


def header(shell: dict) -> str:
    L = shell["labels"]
    other = shell["other_lang"]
    nav = []
    for item in shell["nav"]:
        kids = "".join(f'<li><a href="{k["href"]}"{CUR if k["active"] else ""}>{esc(k["label"])}</a></li>'
                       for k in item["children"])
        current = ' aria-current="location"' if item.get("active") else ""
        active = " active" if item.get("active") else ""
        nav.append(f'<details class="nav-family{active}"><summary data-nav-route="{item["href"]}"{current}>{esc(item["label"])}</summary>'
                   f'<ul class="nav-submenu">{kids}</ul></details>')
    # Below 900 px the existing menu also carries trust links and the governed cite action; desktop keeps them in controls.
    if shell.get("mobile_menu"):
        trust_label = next((g["label"] for g in shell["footer"] if any(l["href"].endswith("/about/") for l in g["links"])), L["trust_nav"])
        trust = "".join(f'<a href="{t["href"]}"{CUR if t.get("active") else ""}>{esc(t["label"])}</a>' for t in shell["trust"])
        nav.append(f'<span class="group m-only" role="group" aria-label="{esc(trust_label)}" data-menu-trust><span class="glabel">{esc(trust_label)}</span>{trust}</span>'
                   f'<button type="button" class="tbtn m-only" data-cite data-menu-cite>{esc(L["cite"])}</button>')
    return (f'<noscript><div class="noscript">{esc(L["noscript"])}</div></noscript><a class="skip" href="#main">{esc(L["skip"])}</a>'
            f'<header class="bar"><div class="bar-in"><a class="brand" href="{shell["home_href"]}" aria-label="CauseWay — {esc(shell["product"])}">{logo(40, "(min-width: 900px) 48px, 40px")}<span class="brand-text"><span class="brand-pub" dir="ltr">CauseWay</span><span class="brand-name">{esc(shell["product"])}</span></span></a>'
            f'<nav id="primary-nav" class="nav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div class="controls"><button type="button" class="tbtn" data-search-open aria-label="{esc(L["search"])}">{esc(L["search"])}</button>'
            f'<button type="button" class="tbtn cite" data-cite aria-label="{esc(L["cite"])}">{esc(L["cite"])}</button>'
            f'<a class="report" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            # R-05 (independent review of 70398d1): the language switch and the menu are links, so both work without
            # JavaScript. The switch opens the same route in the other edition; the menu opens the footer, which carries
            # every navigation and trust link. The runtime enhances the menu into a disclosure button (app.js).
            f'<a class="tbtn lang" href="{shell["other_href"]}" hreflang="{other}" data-lang="{other}" aria-label="{esc(L["lang_switch_action"])}" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">'
            f'<svg aria-hidden="true" viewBox="0 0 24 24" focusable="false"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"></path></svg>'
            f'<span class="sr-only">{esc(L["lang_switch_name"])}</span></a>'
            f'<a class="tbtn menu" href="#site-footer" data-menu aria-label="{esc(L["menu"])}" aria-controls="primary-nav" aria-expanded="false">{esc(L["menu"])}</a></div>'
            f'<div id="utility-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true" data-copied-label="{esc(L["copied"])}"></div></div></header>'
            f'{search_dialog(shell)}<main id="main"><div class="page">')


def search_dialog(shell: dict) -> str:
    L = shell["labels"]
    return (f'<dialog id="search-dialog" class="search" aria-labelledby="search-dialog-title"><div class="search-panel"><div class="search-head"><strong id="search-dialog-title">{esc(L["search_title"])}</strong>'
            f'<button type="button" class="tbtn" data-search-close aria-label="{esc(L["search_close"])}">{esc(L["search_close"])}</button></div>'
            f'<input id="global-search-dialog" data-search-input class="search-input" placeholder="{esc(L["search_placeholder"])}" aria-label="{esc(L["search"])}">'
            f'<div class="search-status" data-search-status role="status" aria-live="polite" aria-label="{esc(L["search_status"])}"></div><div data-search-results class="search-results"></div></div></dialog>')


def footer(shell: dict, tail: str = "") -> str:
    """The institutional band; `tail` is the print-only provenance block, the last element of a printed page."""
    L = shell["labels"]
    trust = "".join(f'<a href="{t["href"]}"{CUR if t.get("active") else ""}>{esc(t["label"])}</a>' for t in shell["trust"])
    trust_label = next((g["label"] for g in shell["footer"] if any(l["href"].endswith("/about/") for l in g["links"])), L["trust_nav"])
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>"
                     for g in shell["footer"] if not any(l["href"].endswith("/about/") for l in g["links"]))
    return (f'</div></main><footer id="site-footer" class="inst"><div class="inst-in"><div class="trust"><h3>{esc(trust_label)}</h3><nav aria-label="{esc(L["trust_nav"])}">{trust}</nav></div>'
            f'<div class="id">{logo(40)}<p>{esc(L["footer_strapline"])}</p></div><nav class="groups" aria-label="{esc(L["footer_nav"])}">{groups}</nav>'
            f'<div class="fine">© 2026 CauseWay · {esc(L["footer_rights"])} · {esc(shell["edition"])}</div></div>{tail}</footer>'
            f'{json_block("yfie-ui", shell["ui_json"])}<script src="/assets/app.js" defer></script></body></html>')


# ------------------------------------------------------------------------------------------------ objects
def rubric(t, n: int | None = None, tag: str = "span", cls: str = "rubric") -> str:
    num_ = f'<span class="n">{n:02d}</span>' if n else ""
    return f'<{tag} class="{cls}">{num_}{esc(t)}</{tag}>'


# 4.1 (owner note of 3 October 2026, 11:15): the figure is set in its own governed sentence, in the figure weight — never
# lifted out of it (D7 Design Intent Lock §4.1.1: no lifted figures, no stat tiles). A value is a percentage, a decimal, a
# number with thousands separators, or a whole number of three digits or more that is not a year; dates, identifiers and
# ranges (hyphenated, slashed or already isolated) are left as they are. Applied to text outside tags only.
_FIG = re.compile(r'(?<![\d.,/:\-])(\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|\d+\.\d+%?|\d+%|(?!(?:19|20)\d\d(?!\d))\d{3,})(?![\d/:\-]|[.,]\d)')


# R-10 (independent review of 70398d1): only the figures of the first sentence — the finding — are emphasised. A later
# sentence qualifies it (coverage, exclusion, derivation, a source's own discrepancy), and the same weight would make
# its figure read as a second finding ("11.9% … 23%"). A sentence ends at . ! ? or ؟ before a space or the end of the
# text, except after "No" or "p"/"pp" (an instrument or page number continues the sentence).
_SENT_END = re.compile(r'(?<!\bNo)(?<!\bpp)(?<!\bp)[.!?؟](?=\s|$)')


def fig_emph(html_text: str) -> str:
    parts = re.split(r'(<[^>]+>)', html_text)
    out, in_bdi, done = [], 0, False
    for p in parts:
        if p.startswith("<"):
            in_bdi += 1 if p.startswith("<bdi") else (-1 if p.startswith("</bdi") else 0)
            out.append(p)
        elif in_bdi or done:
            out.append(p)
        else:
            m = _SENT_END.search(p)
            head, tail = (p[:m.end()], p[m.end():]) if m else (p, "")
            out.append(_FIG.sub(r'<b class="fnum">\1</b>', head) + tail)
            done = bool(m)
    return "".join(out)


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
    # RC-15 (B15 d, C-1): the series this record uses, where they differ from the source's main locator (link text: the
    # locator's own series code)
    series = (f'<p class="small" data-series-used><b>{esc(L["series_used"])}</b> '
              + " · ".join(f'<a href="{esc(u)}" rel="noopener noreferrer" target="_blank"><bdi dir="ltr">{esc(urlparse(u).path.rstrip("/").rsplit("/", 1)[-1])}</bdi></a>' for u in s["series"])
              + "</p>") if s.get("series") else ""
    return (f'<article class="src" data-evidence-source="{esc(s["id"])}">{head_}{series}<div class="acts"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a>'
            f'<a class="source-locator" href="{esc(s["url"])}" rel="noopener noreferrer" target="_blank">{esc(L["open_original"])}</a>'
            f'<button type="button" class="tbtn" data-source-cite data-source-citation="{esc(s["cite_payload"])}">{esc(L["copy_reference"])}</button></div>{rights}</article>')


_COMPACT_N = [0]


def compact(rec: dict, L: dict, open_label: str, cls: str = "compact") -> str:
    """Clock-first compact evidence object: when → title → for whom → open. One link per object (D3, cold-reader test:
    two links to one record read as two destinations): the governed action is the link, and its accessible name is the
    action followed by the record's title (`aria-labelledby` over the two governed strings; nothing is authored)."""
    _COMPACT_N[0] += 1
    n = _COMPACT_N[0]
    ck = clock(L["period"], esc(rec.get("period") or ""))
    return (f'<article class="{cls}">{ck}<div class="q" id="co-t{n}">{esc(rec["title"])}</div>'
            + (f'<div class="small">{esc(rec["universe"])}</div>' if rec.get("universe") else "")
            + f'<div class="open"><a href="{rec["href"]}" id="co-a{n}" aria-labelledby="co-a{n} co-t{n}">{esc(open_label)}</a></div></article>')


def spine(index: list, edges: list, foot: bool = False, foot_index: bool = True) -> str:
    """The verification spine. Exactly one is visible at any width: beside the object from 900 px (index + edges), at
    the object's foot below (index unless the page carries a strip, + edges). Accessible names come from governed text
    already on the page: the index is named by the `h1` of the object it indexes (`aria-labelledby="page-title"`), each
    edge group by its own governed heading — no label is authored (D2, closes DEBT-006)."""
    sfx = "f" if foot else "s"
    idx = "".join(f'<li><a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a></li>' for i, (a, t) in enumerate(index))
    # B10 a: an edge group is named by its heading and the page's h1, so it never shares a name with the page's own
    # next-actions landmark ("Continue from here"); both are governed text already on the page
    ed = "".join(f'<nav class="edges" aria-labelledby="edge-{sfx}{n} page-title"><h3 id="edge-{sfx}{n}">{esc(e[0])}</h3>' + (f'<p class="small">{esc(e[2])}</p>' if len(e) > 2 and e[2] else "") + "<ul>" + "".join(f"<li>{x}</li>" for x in e[1]) + "</ul></nav>"
                 for n, e in enumerate(edges) if e[1])
    cls = "spine foot-spine" if foot else "spine"
    index_html = f'<nav class="index" aria-labelledby="page-title"><ul>{idx}</ul></nav>' if (not foot or foot_index) else ""
    return f'<aside class="{cls}">{index_html}{ed}</aside>'


def strip(index: list) -> str:
    return '<nav class="strip" aria-labelledby="page-title">' + "".join(f'<a href="#{a}"><span class="n">{i+1:02d}</span><span>{esc(t)}</span></a>' for i, (a, t) in enumerate(index)) + "</nav>"


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
    for_whom = clock(L["applies"], esc(page["universe"])) if page.get("universe") else ""   # 4.1: WHEN, then FOR WHOM, before the claim
    head_ = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["family"])}{clock(L["period"], esc(page["period"]))}{for_whom}<h1 id="page-title">{esc(page["title"])}</h1>'
             + (f'<p class="st">{esc(page["lead"])}</p>' if page["lead"] else "") + "</div>")
    own_fig = (f'<span class="rubric mt18">{esc(L["visual_eyebrow"])}</span>' + figure({**page["visual"], "here": True}, shell["labels"]["cite"], DISC.origin(), heading="h3")) if page.get("visual") and page["visual"].get("tier") != "RETIRE_FROM_DESIGN" else ""
    qa = [f'<div class="qa first" id="q1">{rubric(L["establishes"], 1, "h2")}<div class="st"><p>{fig_emph(iso(esc(page["summary"])))}</p></div>{own_fig}</div>' + strip(index),
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
    if page["lineage_statement"]:   # an evidence state (framing rule, composite, partial): the answer itself, never an error
        src_extra += f'<div class="body"><p data-lineage-state="{esc(page["closure_state"])}">{esc(page["lineage_statement"])}</p></div>'
    if page["no_source_message"]:   # no public locator: an honest state of the record, stated in the body voice
        src_extra += f'<div class="body"><p data-evidence-source-unavailable>{esc(page["no_source_message"])}</p></div>'
    trace = (f'<div class="mt16"><span class="small"><b>{esc(L["trace"])}</b> · {esc(L["trace_intro"])}</span><div class="chips"><span class="chip">{bdi(page["id"])}</span>{chips}</div></div>' if page["trace_ids"] else "")
    # The governed intro ("open the source record here, or go to the original document …") names two actions, so it is
    # printed only where the record actually offers one: a source card to open. On a framing rule (no source expected),
    # on a composite whose members are not listed and on a record whose source has no public locator, there is nothing
    # to open, and the D7 cold reader read the promise followed by its own denial as the page breaking (DL-D7-011).
    # The record still answers question 6 — with its lineage statement or its no-locator statement, in the body voice.
    intro = f'<p class="small">{esc(L["source_intro"])}</p>' if page["sources"] else ""
    qa.append(f'<section class="qa" id="q6"><div>{rubric(L["source"], 6, "h2")}<span id="source"></span></div><div>{intro}<div class="mt10">{"".join(source_card(s) for s in page["sources"])}</div>{src_extra}{trace}</div></section>')
    more = "".join(f'<div class="qa"><h3 class="rubric">{esc(L[k])}</h3><div class="body"><p>{esc(page[k])}</p></div></div>' for k in ("method", "change_trigger", "verification") if page[k])
    if page["reading_guidance"]:
        more += f'<div class="qa"><h3 class="rubric">{esc(L["reading_guidance"])}</h3><div class="body">{paras(page["reading_guidance"]["paragraphs"])}</div></div>'
    qa.append(f'<div class="qa" id="q7">{rubric(L["more"], 7, "h2")}<details class="more"><summary>{esc(L["more_intro"])}</summary>{more}</details></div>')
    util = (f'<section class="util" data-record-id="{esc(page["id"])}"><div class="ref"><b>{esc(L["reference"])}</b> {bdi(page["id"])}</div>'
            f'<div class="actions">{cite_tools(shell, page["route"], page["citation_short"], record=True, long_form=page["citation"])}'
            f'<button type="button" class="tbtn" data-share data-share-text="{esc(isolate_plain(page["share_text"]) if shell["lang"] == "ar" else page["share_text"])}">{esc(shell["labels"]["share_record"])}</button>'
            + (f'<a href="{page["compare_href"]}" data-compare-entry>{esc(L["compare"])}</a>' if page.get("compare_href") else "")
            + f'<a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a>'
            f'<a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a><a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a></div><p class="small">{esc(L["reuse_note"])}</p></section>')
    used = [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in page["used_in_readings"]]
    edges = [(L["used_in"], used),
             (L["related"], [f'<a href="{x["href"]}">{esc(x["label"])}</a>' for x in page["routes_back"]] + [f'<a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a>', f'<a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a>', f'<a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a>'], L["related_intro"])]
    used_attr = " data-used-in-readings" if used else ""
    body = f'<article class="obj page-obj"{used_attr}>{head_}{"".join(qa)}{util}</article>{spine(index, edges)}{spine(index, edges, foot=True, foot_index=False)}'
    return head(page, shell, page["route"], extra=meta) + header(shell) + body + footer(shell, print_foot(shell, page["route"], page["title"], page["citation"]))


def home(page: dict, shell: dict) -> str:
    L = page["labels"]; S = {s["order"]: s for s in page["sections"]}
    index = [("s3", S[3]["heading"]), ("s4", S[4]["heading"]), ("s9", S[9]["heading"]), ("s5", S[5]["heading"]), ("s6", S[6]["heading"]), ("s7", S[7]["heading"]), ("s8", S[8]["heading"]), ("sf", L["featured"])]
    # The product's statement (section 1) and its two governed actions sit in the head, under the headline and before
    # the first figure: four cold readers (EN/AR × 390/1440, D3) reached the third screen before learning what the
    # product is. The product rubric is kept for the wide head; the masthead already names the product on a phone.
    parts = [f'<div class="head">{rubric(L["product"], cls="rubric product")}<h1 id="page-title">{esc(page["title"])}</h1><div class="st" id="s1">{paras(S[1]["paragraphs"])}</div>'
             f'<div class="actions"><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a><a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></div></div>']
    recs = list(page["records"])
    demo = []
    for res, html_ in paced_groups(S[3]["body"]):
        demo.append(fig_emph(html_))
        if recs and not res:
            demo.append(compact(recs.pop(0), L, L["open_evidence_record"], cls="compact bound"))
    def h2(sec):   # governed kicker (role) above the governed heading
        return (f'<span class="rubric">{esc(sec["role"])}</span>' if sec.get("role") else "") + f'<h2>{esc(sec["heading"])}</h2>'
    parts.append(f'<section class="qa first" id="s3"><div>{h2(S[3])}</div><div class="paced">{"".join(demo)}</div></section>')
    parts.append(f'<section class="bnd" id="s4">{rubric(S[4]["role"])}<h2>{esc(S[4]["heading"])}</h2><div class="mt8">{paras(S[4]["paragraphs"])}</div></section>')
    # the governed instruction and the section's body read as one paragraph (three restatements in a row, D3 test)
    qs = "".join(f'<li><div><div class="q"><a href="{q["href"]}">{esc(q["question"])}</a></div><div class="gets small">{esc(q["gets"])}</div></div></li>' for q in page["starting_questions"])
    parts.append(f'<section class="qa" id="s9"><div><span class="rubric">{esc(L["questions_eyebrow"])}</span><h2>{esc(S[9]["heading"])}</h2></div><div><p class="body"><b>{esc(L["questions_title"])}.</b> {esc(S[9]["body"])}</p><ol class="qlist">{qs}</ol><p class="small mt12"><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></p></div></section>')
    parts.append(f'<section class="qa" id="s5"><div>{h2(S[5])}</div><div class="body">{paras(S[5]["paragraphs"])}</div></section>')
    v = page["system_visual"]
    # the records not behind a figure (the framing record) belong to the system-context section they frame, not to a
    # group labelled "behind these figures" (D3 test: the label promised four and showed one)
    # 4.2 (owner note, 11:15): the section describes the chain from rule to result; its drawn chain (VIS-PAYMENT-RAILS,
    # on /reforms/) is offered first, then the framing record
    recs = ([page["chain_record"]] if page.get("chain_record") else []) + recs
    rest = f'<div class="objs mt18">{"".join(compact(r, L, L["open_evidence_record"]) for r in recs)}</div>' if recs else ""
    parts.append(f'<section class="qa" id="s6"><div>{rubric(S[6]["role"])}<h2 id="system" tabindex="-1">{esc(S[6]["heading"])}</h2></div><div><div class="body">{paras(S[6]["paragraphs"])}</div>{rest}'
                 f'<span class="rubric mt18">{esc(L["visual_eyebrow"])}</span>{figure(v, shell["labels"]["cite"], DISC.origin(), heading="h3", boundary_label=L["boundary"], open_label=L["open_record"])}</div></section>')
    # RC-15 (B15 d, A-8): the gaps section links the measurement priorities bound to Home, by their governed titles
    gp = page.get("gap_priorities") or []
    gaps = (f'<h3 class="mt18">{esc(L["gaps_heading"])}</h3><p class="small">{esc(L["gaps_note"])}</p><ul class="rlist" data-home-gap-priorities>'
            + "".join(f'<li><a href="{m["href"]}">{esc(m["title"])}</a></li>' for m in gp) + "</ul>") if gp else ""
    for o, i in ((7, "s7"), (8, "s8")):
        parts.append(f'<section class="qa" id="{i}"><div>{h2(S[o])}</div><div class="body">{paras(S[o]["paragraphs"])}{gaps if o == 7 else ""}</div></section>')
    f = page["featured"]
    if f:
        parts.append(f'<section class="qa" id="sf">{rubric(L["featured"], tag="h2")}<div><article class="compact first-obj">{clock(L["evidence_period"], esc(f["evidence_period"]))}<div class="q"><a href="{f["href"]}">{esc(f["title"])}</a></div><div class="st"><p>{esc(f["thesis"])}</p></div><div class="open"><a href="{f["href"]}">{esc(L["open_reading"])}</a> · <a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></div></article></div></section>')
    parts.insert(2, strip(index))   # the phone's in-page navigation after the first figure group; the foot spine keeps only the edges (DEBT-014)
    edges = [(f'{L["records_heading"]} ({len(page["records"])})', [f'<a href="{r["href"]}">{esc(r["title"])}</a>' for r in page["records"]]),
             (L["flow"], [f'<a href="{h}">{esc(t)}</a><br><span class="small">{esc(d)}</span>' for h, t, d in ((page["hrefs"]["readings"], L["readings_nav"], L["cta_readings"]), (page["hrefs"]["measurement"], L["measurement_nav"], L["cta_measurement"]), (page["hrefs"]["data"], L["data_nav"], L["cta_data"]))], L["side"])]
    body = f'<article class="obj page-obj">{"".join(parts)}{page_util(shell, page)}</article>{spine(index, edges)}{spine(index, edges, foot=True, foot_index=False)}'
    return head(page, shell, "/") + header(shell) + body + footer(shell, print_foot(shell, "/", page["title"]))


def reading(page: dict, shell: dict) -> str:
    L = page["labels"]; SL = shell["labels"]
    origin = DISC.origin()
    index = ([(f's-{s["section_id"]}', s["heading"]) for s in page["sections"] if s["heading"]] + [("trace", L["trace"]), ("sources", L["sources"])]
             + ([("measure", L["measurement"])] if page.get("measurement") else []) + [("related", L["related"])])
    head_ = (f'<div class="head">{crumb(page["breadcrumb"], shell)}{rubric(L["eyebrow"])}<p class="q">{esc(page["question"])}</p><h1 id="page-title">{esc(page["title"])}</h1><div class="st"><p>{esc(page["thesis"])}</p></div>'
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
        # RC-15 (B15 d, C-9): a Reading's own figure does not link the Reading to itself on screen
        here = DISC.localized(page["route"], shell["lang"])
        figs = "".join(figure({**v, "here": v.get("canonical_href") == here}, SL["cite"], origin) for v in page["visuals"]) if i == 0 else ""
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
    from .families import measure_obj   # noqa: PLC0415  (families imports this module)
    measure = (f'<section class="qa" id="measure" data-reading-measurement><h2>{esc(L["measurement"])}</h2><div><p class="small">{esc(L["measurement_note"])}</p><div class="objs">'
               f'{"".join(measure_obj(m) for m in page["measurement"])}</div></div></section>') if page.get("measurement") else ""   # B6
    body = f'<article class="obj page-obj">{head_}{bnd}{strip(index)}<div class="essay">{"".join(essay)}</div>{trace}{sources}{measure}{related}{page_util(shell, page)}</article>{spine(index, edges)}{spine(index, edges, foot=True, foot_index=False)}'   # the strip after the boundary is the phone's map of the essay (DEBT-014)
    return head(page, shell, page["route"], kind="article") + header(shell) + body + footer(shell, print_foot(shell, page["route"], page["title"]))


# every locator (RC-15, C-2: the short citation names each original source's URL), every identifier (the text layer's
# ID_RUN) and the publisher; a URL is matched first, so an identifier inside it is not isolated twice
_CITE_LTR = re.compile(f'(https?://[^\\s<؛،]*[^\\s<؛،.,;)]|{ID_RUN.pattern}|(?<![\\w-])CauseWay(?![\\w-]))')


def cite_isolate(html_text: str) -> str:
    """B9 review (blocking): in an Arabic citation a record or source identifier next to "CauseWay" ran as one
    left-to-right run ("CLM-001. CauseWay."), so the publisher read before the record. Each identifier and the publisher's
    name is isolated, as the text layer isolates dates; the copied text is unchanged. Applied to escaped text outside tags."""
    parts = re.split(r'(<[^>]+>)', html_text)
    # G0 (owner instructions of 3 October 2026, 09:50): only a URL may wrap inside a citation; an identifier stays whole
    # (an Arabic citation showed "-CLM … 001" when the record ID broke at its hyphen)
    return "".join(p if p.startswith("<") else _CITE_LTR.sub(lambda m: f'<bdi dir="ltr" class="nw{" url" if m.group(1).startswith("http") else ""}">{m.group(1)}</bdi>', p) for p in parts)


def page_citation(shell: dict, title: str) -> str:
    """B9: the citation of a page that is not an Evidence Record — its governed title, then the governed page line
    UI-CITE-PAGE-LINE (product, publisher, edition; the record line UI-CITE-RECORD-LINE without the record name). The
    record citation adds its period, population, boundary and sources; the canonical URL follows either."""
    t = str(title or "").strip().rstrip(".")
    return f'{t if t.endswith(("?", "؟", "!")) else t + "."} {shell["cite_page_line"]}'   # never "?." after a question title


def cite_tools(shell: dict, route: str, citation: str, record: bool = False, long_form: str = "") -> str:
    """B9: the citation preview (what "Copy citation" copies, shown before copying) and the print control. The canonical
    URL is the build's (absolute once the origin is set); the runtime writes the page's own canonical into it."""
    L = shell["labels"]
    canon = DISC.url(DISC.localized(route, shell["lang"]), DISC.origin())
    lead = f' {esc(L["current_record"])}' if record else ""
    cls = "tbtn evidence-cite-button" if record else "tbtn"
    # RC-15 (B15 d, C-2; OWN-04): a record copies its short citation; the long form, with the period, population and
    # limits, is one disclosure away and copies on its own
    long_ = (f'<details class="cite-long"><summary>{esc(L["cite_long"])}</summary><p class="cite-text" data-cite-long-text>{cite_isolate(iso(esc(long_form)))}{lead}'
             f' <bdi dir="ltr" data-cite-url>{esc(canon)}</bdi></p><button type="button" class="tbtn" data-cite-long>{esc(L["copy_long"])}</button></details>') if long_form else ""
    # a record's short citation has two lines: this resource (ending with the page address), then the original sources
    line1, _, line2 = str(citation).partition("\n")
    second = f'<br><span class="cite-l2" data-cite-line>{cite_isolate(iso(esc(line2)))}</span>' if line2 else ""
    return (f'<div class="cite-preview"><p class="cite-h">{esc(L["cite_preview"])}</p><p class="cite-text" data-cite-text><span data-cite-line>{cite_isolate(iso(esc(line1)))}{lead}'
            f' <bdi dir="ltr" data-cite-url>{esc(canon)}</bdi></span>{second}</p>{long_}</div><button type="button" class="{cls}" data-cite>{esc(L["copy_citation"])}</button>'
            f'<button type="button" class="tbtn" data-print>{esc(L["print"])}</button>')


def page_util(shell: dict, page: dict | None = None) -> str:
    """The page's own actions at the foot of its object (cite, print, report), reachable at every width — the product
    bar shows them only on wide screens."""
    L = shell["labels"]
    tools = cite_tools(shell, page["route"], page_citation(shell, page.get("title"))) if page else f'<button type="button" class="tbtn" data-cite>{esc(L["cite"])}</button>'
    return (f'<section class="util"><div class="actions">{tools}'
            f'<a href="{shell["contact_href"]}">{esc(L["report"])}</a></div></section>')


def print_foot(shell: dict, route: str, title: str, citation: str = "") -> str:
    """Provenance that survives a printed page (D6, brief §10): the product name, the edition, the canonical URL
    (absolute once the deployment origin is set) and the citation — the record's governed citation where one exists,
    otherwise the page title, the product and the canonical URL, exactly what the runtime's cite action copies. Shown
    by the print system only (hidden on screen); no word is authored."""
    origin = DISC.origin()
    canon = DISC.url(DISC.localized(route, shell["lang"]), origin)
    cite = cite_isolate(iso(esc(citation))) if citation else f'{cite_isolate(iso(esc(page_citation(shell, title))))} <bdi dir="ltr">{esc(canon)}</bdi>'   # B9: the one template
    return (f'<div class="print-foot"><p><b>{esc(shell["product"])}</b> · {esc(shell["edition"])} · <bdi dir="ltr" class="canon">{esc(canon)}</bdi></p>'
            f'<p class="cite">{cite}</p></div>')


RENDERERS = {"Orientation": home, "Evidence Record": evidence_record, "Reading": reading}


_NEW_TAB_LINK = re.compile(r'(<a\b[^>]*\btarget="_blank"[^>]*>)(.*?)(</a>)', re.S)


def mark_new_tab(html: str, cue: str) -> str:
    """Release candidate G4 (D5 escalation; UI-EXTERNAL-NEW-TAB): every link that opens a new tab says so to assistive
    technology — a visually hidden cue inside the link, or, where the link is named by aria-label, at the end of that name."""
    if not cue:
        return html

    def one(m):
        open_, inner, close = m.groups()
        if 'aria-label="' in open_:
            return re.sub(r'aria-label="([^"]*)"', lambda a: f'aria-label="{a.group(1)} {esc(cue)}"', open_, count=1) + inner + close
        return f'{open_}{inner}<span class="sr-only"> {esc(cue)}</span>{close}'
    return _NEW_TAB_LINK.sub(one, html)


def render(page: dict, shell: dict, variant: str = "") -> str:
    _COMPACT_N[0] = 0   # ids restart per page (deterministic output whatever the route order)
    if page["family"] in RENDERERS:
        return mark_new_tab(isolate_document(RENDERERS[page["family"]](page, shell)), shell["labels"].get("new_tab", ""))
    from . import families   # the D2 families share this module's objects and shell
    # the one isolation pass (text.py): no date or range leaves plain; then every new-tab link carries its cue
    return mark_new_tab(isolate_document(families.RENDERERS[page["family"]](page, shell)), shell["labels"].get("new_tab", ""))


def render_site_files(out: Path, content) -> int:
    """The neutral root entry, the bilingual 404 and the discovery files (F6: one implementation in scripts/discovery.py)."""
    from . import families
    origin = DISC.origin()
    (out / "index.html").write_text(isolate_document(families.root_page(content.shell("ar", "/"), content.shell("en", "/"))), encoding="utf-8", newline="\n")
    (out / "404.html").write_text(isolate_document(families.not_found(content.not_found(), content.shell("ar", "/"))), encoding="utf-8", newline="\n")
    for r in moved_routes():
        for lang in ("ar", "en"):
            dest = out / lang / r["from"].strip("/") / "index.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(isolate_document(moved_page(content, lang, r)), encoding="utf-8", newline="\n")
    (out / "robots.txt").write_text(DISC.robots_txt(origin), encoding="utf-8", newline="\n")
    if origin:
        (out / "sitemap.xml").write_text(DISC.sitemap_xml(content.routes(), origin), encoding="utf-8", newline="\n")
    return 2 + 2 * len(moved_routes())


# ------------------------------------------------------------------------------------------------ retired addresses
# Owner decision of 3 October 2026, 23:54 Aden (X-ESC-RC17-01): a record that is no longer published on its own keeps
# its address, which leads to the record that now covers it. The map is site-src/hosting/moved_routes.json (hosting
# configuration, like _headers). The page is never indexed, names the target as its canonical address, says why in two
# governed labels (UI-MOVED-RECORD-*), links the target by its governed title and moves the reader on at once; it works
# without JavaScript. Checked by RC-19 (scripts/validate.py).
MOVED_ROUTES = Path(__file__).resolve().parents[2] / "site-src" / "hosting" / "moved_routes.json"


def moved_routes() -> list[dict]:
    return json.loads(MOVED_ROUTES.read_text(encoding="utf-8"))["moved"] if MOVED_ROUTES.exists() else []


def moved_page(content, lang: str, r: dict) -> str:
    shell = content.shell(lang, r["from"])
    target = content.href(r["to"], lang)
    title = content.loc(content.spec_by_route[r["to"]], "title", lang)
    heading, body = content.t("UI-MOVED-RECORD-TITLE", lang), content.t("UI-MOVED-RECORD-BODY", lang)
    origin = DISC.origin()
    return (f'<!doctype html><html lang="{lang}" dir="{shell["dir"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">{DISC.robots_meta("noindex")}'
            f'<meta http-equiv="refresh" content="0;url={target}">'
            f'<link rel="icon" type="image/png" sizes="32x32" href="/assets/logo/CauseWay_logo_32.png"><title>{esc(heading)} — {esc(shell["product"])}</title>'
            f'<meta name="description" content="{esc(body)}"><link rel="stylesheet" href="/assets/yfie.css">{font_preloads(lang)}'
            f'{DISC.head_links(r["to"], lang, origin)}</head><body>'
            f'{header(shell)}<article class="obj page-obj" data-moved-to="{r["to"].strip("/")}"><h1 id="page-title">{esc(heading)}</h1>'
            f'<p class="st">{esc(body)}</p><div class="actions"><a href="{target}">{esc(title)}</a></div></article>'
            f'{footer(shell)}')
