# -*- coding: utf-8 -*-
"""Neutral test harness renderer (D1).

Renders the governed content of a route as plain semantic HTML with **no stylesheet**: the user agent's defaults only.
It exists to prove that the loader carries the whole governed content in both languages, to give the browser suites
something to drive (skip link, `#main`, search dialog, `data-*` hooks, JSON blocks), and to mount Design prototypes.
It establishes no typography, grid, hierarchy, component grammar, navigation model, colour, spacing, evidence
presentation or interaction language: every one of those is a Design decision made on the canvas and recorded in
`design/01_FOUNDATIONS.md` before any renderer carries it.
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import discovery as DISC  # noqa: E402  (F6: one implementation of canonical, hreflang, Open Graph and structured data)


def esc(x) -> str:
    return html.escape(str(x or ""), quote=True)


def paras(items) -> str:
    return "".join(f"<p>{esc(p)}</p>" for p in items)


def json_block(id_: str, data) -> str:
    return f'<script type="application/json" id="{id_}">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def shell_head(page: dict, shell: dict, route: str, kind: str = "website", extra: str = "") -> str:
    lang = shell["lang"]
    origin = DISC.origin()
    return (f'<!doctype html><html lang="{lang}" dir="{shell["dir"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(page["title"])} — {esc(shell["product"])}</title>'
            f'<meta name="description" content="{esc(page.get("meta_description"))}">{extra}'
            f'{DISC.head_links(route, lang, origin)}{DISC.social_meta(page["title"], page.get("meta_description") or "", lang, route, shell["product"], kind, origin)}'
            f"</head><body>")


def shell_header(shell: dict) -> str:
    L = shell["labels"]
    lang = shell["lang"]
    other = shell["other_lang"]
    nav = []
    current = ' aria-current="page"'
    for item in shell["nav"]:
        if item.get("children"):
            kids = "".join(f'<a href="{k["href"]}"{current if k["active"] else ""}>{esc(k["label"])}</a>' for k in item["children"])
            nav.append(f'<span role="group" aria-label="{esc(item["label"])}"><span>{esc(item["label"])}</span>{kids}</span>')
        else:
            nav.append(f'<a href="{item["href"]}"{current if item.get("active") else ""}>{esc(item["label"])}</a>')
    trust = "".join(f'<a href="{t["href"]}">{esc(t["label"])}</a>' for t in shell["trust"])
    return (f'<noscript><div>{esc(L["noscript"])}</div></noscript><a class="skip" href="#main">{esc(L["skip"])}</a>'
            f'<nav aria-label="{esc(L["trust_nav"])}">{trust}</nav>'
            f'<header><a href="{shell["home_href"]}" aria-label="CauseWay — {esc(shell["product"])}"><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay" width="120" height="120"></a>'
            f'<nav id="primary-nav" aria-label="{esc(L["primary_nav"])}">{"".join(nav)}</nav>'
            f'<div><button type="button" data-search-open aria-label="{esc(L["search"])}">{esc(L["search"])}</button>'
            f'<button type="button" data-cite aria-label="{esc(L["cite"])}">{esc(L["cite"])}</button>'
            f'<a href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" data-lang="{other}" aria-label="{esc(L["lang_switch_action"])}" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button>'
            f'<button type="button" data-menu aria-label="{esc(L["menu"])}" aria-controls="primary-nav" aria-expanded="false">{esc(L["menu"])}</button></div>'
            f'<div id="utility-status" role="status" aria-live="polite" aria-atomic="true" data-copied-label="{esc(L["copied"])}"></div></header>'
            f'<dialog id="search-dialog" aria-labelledby="search-dialog-title"><div><strong id="search-dialog-title">{esc(L["search_title"])}</strong>'
            f'<button type="button" data-search-close aria-label="{esc(L["search_close"])}">{esc(L["search_close"])}</button>'
            f'<input id="global-search-dialog" data-search-input placeholder="{esc(L["search_placeholder"])}" aria-label="{esc(L["search"])}">'
            f'<div data-search-status role="status" aria-live="polite" aria-label="{esc(L["search_status"])}"></div><div data-search-results></div></div></dialog>'
            f'<main id="main">')


def shell_footer(shell: dict) -> str:
    L = shell["labels"]
    groups = "".join(f'<div><strong>{esc(g["label"])}</strong>' + "".join(f'<a href="{l["href"]}">{esc(l["label"])}</a>' for l in g["links"]) + "</div>"
                     for g in shell["footer"])
    return (f'</main><footer><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay" width="120" height="120"><p>{esc(L["footer_strapline"])}</p>'
            f'<nav aria-label="{esc(L["footer_nav"])}">{groups}</nav><p>© 2026 CauseWay · {esc(L["footer_rights"])}</p></footer>'
            f'{json_block("yfie-ui", shell["ui_json"])}<script src="/assets/app.js" defer></script></body></html>')


def breadcrumb(bc: dict | None, shell: dict) -> str:
    if not bc:
        return ""
    cur = f'<span aria-current="page"><bdi dir="ltr">{esc(bc["current"])}</bdi></span>' if bc["mode"] == "STABLE_OBJECT_ID" else f'<span aria-current="page">{esc(bc["current"])}</span>'
    return f'<nav aria-label="{esc(shell["labels"]["breadcrumb"])}"><a href="{bc["parent_href"]}">{esc(bc["parent_label"])}</a> / {cur}</nav>'


def source_item(s: dict) -> str:
    ref = f'<div>{esc(s["reference_label"])} <bdi dir="ltr">{esc(s["id"])}</bdi></div>'
    head = (f'<strong dir="auto">{esc(s["title"])}</strong><div dir="auto">{esc(s["kind_line"])}</div>{ref}' if s["display_ready"] and s["title"]
            else f'<strong>{esc(s["untitled_label"])}</strong>{ref}')
    rights = f'<p>{esc(s["rights_note"])}</p>' if s["rights_note"] else ""
    return (f'<article data-evidence-source="{esc(s["id"])}">{head}<a href="{s["data_href"]}">{esc(s["labels"]["open_source_record"])}</a> '
            f'<a href="{esc(s["url"])}" rel="noopener noreferrer" target="_blank">{esc(s["labels"]["open_original"])}</a> '
            f'<button type="button" data-source-cite data-source-citation="{esc(s["cite_payload"])}">{esc(s["labels"]["copy_reference"])}</button>{rights}</article>')


# ------------------------------------------------------------------------------------------------ pages
def home(page: dict, shell: dict) -> str:
    L = page["labels"]
    out = [shell_head(page, shell, "/", extra=""), shell_header(shell)]
    out.append(f'<h1>{esc(page["title"])}</h1>')
    for s in page["sections"]:
        if s["order"] == 1:
            out.append(paras(s["paragraphs"]))
            out.append(f'<p><a href="{page["hrefs"]["explore"]}">{esc(L["start"])}</a> <a href="{page["hrefs"]["evidence"]}">{esc(L["verify"])}</a></p>')
        elif s["order"] in (2, 9):
            continue  # introduce the question list (brief §4.5): rendered once as the list heading
        else:
            if s["order"] == 6:
                out.append('<div id="system" tabindex="-1"></div>')
            out.append(f'<section><h2>{esc(s["heading"])}</h2>{paras(s["paragraphs"])}</section>')
            if s["order"] == 3:
                out.append(f'<details><summary>{esc(L["records_heading"])} ({len(page["records"])})</summary><ul>' +
                           "".join(f'<li><a href="{r["href"]}">{esc(r["title"])}</a></li>' for r in page["records"]) + "</ul></details>")
            if s["order"] == 6:
                v = page["system_visual"]
                out.append(f'<section data-visual-id="{esc(v["id"])}"><h3>{esc(v["title"])}</h3><p>{esc(v["question"])}</p><p>{esc(v["alt_text"])}</p>'
                           f'<a href="{v["canonical_href"]}">{esc(L["open_record"])}</a></section>')
    out.append(f'<section><h2>{esc(L["questions_title"])}</h2><ol>' +
               "".join(f'<li><a href="{q["href"]}">{esc(q["question"])}</a><p>{esc(q["gets"])}</p></li>' for q in page["starting_questions"]) +
               f'</ol><a href="{page["hrefs"]["explore"]}">{esc(L["view_all"])}</a></section>')
    f = page["featured"]
    if f:
        out.append(f'<section><p>{esc(L["featured"])}</p><h2><a href="{f["href"]}">{esc(f["title"])}</a></h2><p>{esc(f["thesis"])}</p>'
                   f'<p>{esc(L["evidence_period"])}: {esc(f["evidence_period"])}</p><a href="{f["href"]}">{esc(L["open_reading"])}</a> <a href="{page["hrefs"]["readings"]}">{esc(L["all_readings"])}</a></section>')
    out.append(f'<section><ul><li><a href="{page["hrefs"]["readings"]}">{esc(L["readings_nav"])}</a> {esc(L["cta_readings"])}</li>'
               f'<li><a href="{page["hrefs"]["measurement"]}">{esc(L["measurement_nav"])}</a> {esc(L["cta_measurement"])}</li>'
               f'<li><a href="{page["hrefs"]["data"]}">{esc(L["data_nav"])}</a> {esc(L["cta_data"])}</li></ul></section>')
    out.append(shell_footer(shell))
    return "".join(out)


def evidence_record(page: dict, shell: dict) -> str:
    L = page["labels"]
    meta = f'<meta name="yfie-citation" content="{esc(page["citation"])}"><meta name="yfie-record-id" content="{esc(page["id"])}">'
    out = [shell_head(page, shell, page["route"], extra=meta), shell_header(shell), breadcrumb(page["breadcrumb"], shell)]
    out.append(f'<p>{esc(L["family"])}</p><h1>{esc(page["title"])}</h1>')
    if page["lead"]:
        out.append(f'<p>{esc(page["lead"])}</p>')
    out.append(f'<section><h2>{esc(L["establishes"])}</h2><p>{esc(page["summary"])}</p></section><dl>')
    for key, label in (("definition", "measures"), ("universe", "applies"), ("period", "period"), ("currentness", "currentness")):
        if page[key]:
            out.append(f'<dt>{esc(L[label])}</dt><dd>{esc(page[key])}</dd>')
    out.append("</dl>")
    if page["does_not_establish"]:
        out.append(f'<section data-evidence-boundary-first-load><h2>{esc(L["does_not_establish"])}</h2><p>{esc(page["does_not_establish"])}</p>')
        if page["measurement_limits"]:
            out.append(f'<h3>{esc(L["measurement_limits"])}</h3><p>{esc(page["measurement_limits"])}</p>')
        out.append("</section>")
    out.append(f'<section id="source"><h2>{esc(L["source"])}</h2><p>{esc(L["source_intro"])}</p>' + "".join(source_item(s) for s in page["sources"]))
    if page["sources_without_locator_note"]:
        out.append(f'<p data-evidence-sources-without-locator>{esc(page["sources_without_locator_note"])}</p>')
    if page["members"]:
        out.append(f'<h3>{esc(page["members_heading"])}</h3><ul>' + "".join(f'<li><a href="{m["href"]}">{esc(m["title"])}</a> <bdi dir="ltr">{esc(m["id"])}</bdi></li>' for m in page["members"]) + "</ul>")
    if page["lineage_statement"]:
        out.append(f'<p data-lineage-state="{esc(page["closure_state"])}">{esc(page["lineage_statement"])}</p>')
    if page["no_source_message"]:
        out.append(f'<p class="empty" data-evidence-source-unavailable>{esc(page["no_source_message"])}</p>')
    out.append("</section>")
    if page["trace_ids"]:
        out.append(f'<section><h2>{esc(L["trace"])}</h2><p>{esc(L["trace_intro"])}</p><p><bdi dir="ltr">{esc(page["id"])}</bdi> → ' +
                   " ".join(f'<a href="/{shell["lang"]}/data/?source={esc(sid)}#source-{esc(sid)}"><bdi dir="ltr">{esc(sid)}</bdi></a>' for sid in page["trace_ids"]) + "</p></section>")
    if page["used_in_readings"]:
        out.append(f'<section data-used-in-readings><h2>{esc(L["used_in"])}</h2><ul>' + "".join(f'<li><a href="{x["href"]}">{esc(x["title"])}</a></li>' for x in page["used_in_readings"]) + "</ul></section>")
    out.append(f'<section><h2>{esc(L["related"])}</h2><p>{esc(L["related_intro"])}</p><ul>' +
               "".join(f'<li><a href="{x["href"]}">{esc(x["label"])}</a></li>' for x in page["routes_back"]) +
               f'<li><a href="{page["hrefs"]["evidence"]}">{esc(L["evidence_hub"])}</a></li><li><a href="{page["hrefs"]["data"]}">{esc(L["data"])}</a></li>'
               f'<li><a href="{page["hrefs"]["methodology"]}">{esc(L["methodology"])}</a></li></ul></section>')
    more = []
    for key in ("method", "change_trigger", "verification"):
        if page[key]:
            more.append(f'<h3>{esc(L[key])}</h3><p>{esc(page[key])}</p>')
    if page["reading_guidance"]:
        more.append(f'<h3>{esc(L["reading_guidance"])}</h3>{paras(page["reading_guidance"]["paragraphs"])}')
    if more:
        out.append(f'<details><summary>{esc(L["more"])} — {esc(L["more_intro"])}</summary>{"".join(more)}</details>')
    out.append(f'<section data-record-id="{esc(page["id"])}"><p>{esc(L["reference"])} <strong><bdi dir="ltr">{esc(page["id"])}</bdi></strong></p>'
               f'<button type="button" class="evidence-cite-button" data-cite>{esc(L["cite"])}</button> <a href="{page["hrefs"]["rights"]}">{esc(L["reuse"])}</a> '
               f'<a href="{page["hrefs"]["corrections"]}">{esc(L["history"])}</a> <a href="{page["hrefs"]["report"]}">{esc(L["report"])}</a>'
               f'<p>{esc(L["reuse_note"])}</p></section>')
    out.append(shell_footer(shell))
    return "".join(out)


def visual_fallback(v: dict) -> str:
    """The governed text alternative plus the contract's fallback table (RV-CWR-001 shape), no chart."""
    rows = []
    for s in v.get("series") or []:
        for val in s["values"]:
            rows.append(f'<tr><td>{esc(val["series_label"])}</td><td dir="ltr">{esc(val["x"])}</td><td dir="ltr">{esc(val["y"])}</td><td>{esc(val["unit"])}</td><td><bdi dir="ltr">{esc(val["source"])}</bdi></td></tr>')
    for d in v.get("derived") or []:
        if d.get("x") is not None:
            rows.append(f'<tr><td>{esc(d["series_label"])}</td><td dir="ltr">{esc(d["x"])}</td><td dir="ltr">{esc(d["value"])}</td><td>{esc(d["unit"])} — {esc(v["labels"]["derived"])}</td><td></td></tr>')
    table = f'<table><caption>{esc(v["title"])} — {esc(v["period"])} — {esc(v["universe"])}</caption><tbody>{"".join(rows)}</tbody></table>' if rows else ""
    return (f'<figure data-visual-id="{esc(v["id"])}" data-image-independent="true"><figcaption><h2>{esc(v["title"])}</h2><p>{esc(v["labels"]["analytical_question"])}: {esc(v["question"])}</p>'
            f'<p>{esc(v["alt_text"])}</p><p>{esc(v["labels"]["scope"])}: {esc(v["period"])} · {esc(v["universe"])}</p>'
            f'<p><strong>{esc(v["labels"]["does_not_establish"])}</strong> {esc(v["prohibited_inference"])}</p>'
            f'<p>{esc(v["labels"]["source"])} {esc(v.get("credit") or "")} · {esc(v["labels"]["full_record"])} <a href="{v["canonical_href"]}">{esc(v["canonical_href"])}</a></p></figcaption>{table}</figure>')


def reading(page: dict, shell: dict) -> str:
    L = page["labels"]
    out = [shell_head(page, shell, page["route"], kind="article"), shell_header(shell), breadcrumb(page["breadcrumb"], shell)]
    out.append(f'<p>{esc(L["eyebrow"])}</p><h1>{esc(page["title"])}</h1><p>{esc(page["thesis"])}</p><dl><dt>{esc(L["evidence_period"])}</dt><dd>{esc(page["evidence_period"])}</dd>'
               f'<dt>{esc(L["last_reviewed"])}</dt><dd><time datetime="{esc(page["last_reviewed_iso"])}">{esc(page["last_reviewed"])}</time></dd></dl>'
               f'<p data-reading-boundary><strong>{esc(L["do_not_infer"])}:</strong> {esc(page["prohibited_inference"])}</p><article>')
    for i, s in enumerate(page["sections"]):
        out.append(f'<section data-reading-section="{esc(s["section_id"])}">' + (f'<h2>{esc(s["heading"])}</h2>' if s["heading"] else ""))
        for b in s["blocks"]:
            if b["kind"] == "p":
                out.append(f'<p>{esc(b["text"])}</p>')
            elif b["kind"] == "pull":
                out.append(f'<blockquote><p>{esc(b["text"])}</p></blockquote>')
            else:
                out.append("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in b["items"]) + "</ul>")
        out.append("</section>")
        if i == 0:
            out.append("".join(visual_fallback(v) for v in page["visuals"]))
    out.append("</article>")
    out.append(f'<section data-reading-verify data-reading-path-state="{esc(page["trace_state"])}"><h2>{esc(L["trace"])}</h2><p>{esc(L["trace_intro"])}</p><p>{esc(page["trace_status"])}</p>')
    if page["compare_href"]:
        out.append(f'<a href="{page["compare_href"]}">{esc(L["compare"])}</a>')
    if page["return_to"]:
        out.append(f'<h3>{esc(L["return"])}</h3><ul>' + "".join(f'<li><a href="{b["href"]}">{esc(b["label"])}</a></li>' for b in page["return_to"]) + "</ul>")
    out.append("<ol>")
    for st in page["trace"]:
        srcs = "".join(f'<li><a href="{s["data_href"]}">{esc(s["title"] or s["id"])}</a></li>' for s in st["sources"])
        if st["no_locator_note"]:
            srcs += f'<li>{esc(st["no_locator_note"])}</li>'
        flag = f' <span data-path-state>{esc(st["state_flag"])}</span>' if st["state_flag"] else ""
        out.append(f'<li data-path-record="{esc(st["id"])}"><a href="{st["href"]}">{esc(st["proposition"])}</a> <bdi dir="ltr">{esc(st["id"])}</bdi>{flag}<ul>{srcs}</ul></li>')
    out.append("</ol></section>")
    if page["sources"]:
        out.append(f'<section><h2>{esc(L["sources"])}</h2>' + "".join(source_item(s) for s in page["sources"]) + "</section>")
    if page["related"]:
        out.append(f'<section data-reading-related><h2>{esc(L["related"])}</h2><ul>' + "".join(f'<li><a href="{x["href"]}"><strong>{esc(x["title"])}</strong></a> {esc(x["thesis"])}</li>' for x in page["related"]) +
                   f'</ul><a href="{L["readings_index_href"]}">{esc(L["all"])}</a></section>')
    out.append(shell_footer(shell))
    return "".join(out)


RENDERERS = {"Orientation": home, "Evidence Record": evidence_record, "Reading": reading}


def render(page: dict, shell: dict) -> str:
    return RENDERERS[page["family"]](page, shell)
