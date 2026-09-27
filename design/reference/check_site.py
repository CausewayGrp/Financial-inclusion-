#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendered checks for the reference implementation beyond the D1 trio — the D2 hard families and the D3 synthesis pages
(Home after the cold-reader test, the Reading index, the Readings, Measurement, Methodology, the trust pages, the 404) —
in both languages.

  python3 design/reference/check_site.py [--site design/reference/out] [--gate d2|d3] [--shots] [--degraded] [--evidence DIR]

Per route × language × width (320, 390, 640, 1440): the viewport-suite conditions (no horizontal overflow, alt on every
image, exactly one h1, the document dir matches the language, the first Tab lands on the skip link, no element wider
than the viewport outside a .table-wrap), the brief §19 hooks of the family, no inline style, WCAG 2.2 target size on
every non-inline link and button in main, and the accessible name of every in-page navigation; the interaction smoke
test of check_trio.py at 390 and 1440 (search dialog, menu, cite, keyboard path). Then, once per route × language, the
**hard-state assertions** of brief §9.2 for the gate's routes, evaluated on the rendered DOM (what each case must
prove). With --degraded: print, no-stylesheet/no-script/image-off and forced-colours renders (chart text and marks take
the system colour) into <site>/_review/degraded/. With --evidence DIR: first screens at 390 and 1440 px and figure
crops at 1440 px in both languages. Exit 1 on any failure. Proof for the record, not authority; design/COVERAGE.csv
cites this tool's output.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import socket
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIDTHS = [320, 390, 640, 1440]
GATES = {
    "d2": ["/explore/", "/people/", "/access/", "/payments/", "/remittances/", "/reforms/", "/evidence/", "/evidence/CLM-001/", "/evidence/CLM-004/",
           "/evidence/CLM-014/", "/evidence/CLM-015/", "/evidence/CLM-031/", "/evidence/CLM-037/", "/evidence/CLM-039/", "/evidence/CLM-044/",
           "/evidence/CLM-045/", "/evidence/compare/", "/data/", "/evidence/VIS-FINDEX-GAPS/", "/evidence/VIS-REMITTANCE-MACRO/", "/evidence/VIS-PAYMENT-ANATOMY/"],
}
GATES["d3"] = ["/", "/readings/", "/readings/same-year-different-number/", "/readings/after-transfer-persistence/", "/readings/banking-jump-measurement-basis/",
               "/readings/define-what-you-count/", "/readings/digital-workaround-not-yet-durable-inclusion/", "/readings/finance-constraint-different-questions/",
               "/readings/from-rail-to-result-missing-middle/", "/readings/gender-gap-measured-causes-open/", "/readings/microfinance-structural-divergence/",
               "/readings/reforms-newer-than-people-evidence/", "/measurement/", "/methodology/", "/about/", "/corrections/", "/rights/", "/accessibility/",
               "/privacy/", "/terms/", "/contact/"]
GATES["d4"] = ["/firms/", "/finance/", "/providers/"]   # + every evidence record, read from the built site (record_routes)
EVIDENCE_BY_GATE = {
    "d2": ["/explore/", "/people/", "/access/", "/payments/", "/remittances/", "/reforms/", "/evidence/", "/evidence/compare/", "/data/", "/evidence/CLM-004/", "/evidence/CLM-044/"],
    "d3": ["/", "/readings/", "/readings/after-transfer-persistence/", "/readings/banking-jump-measurement-basis/", "/measurement/", "/methodology/", "/about/", "/contact/", "/corrections/"],
    # D4: the three remaining domain answers and one record per verification state outside the §9.1 set
    "d4": ["/firms/", "/finance/", "/providers/", "/evidence/CLM-005/", "/evidence/CLM-046/", "/evidence/DS-FINDEX-HISTORY-CROSSWALK/", "/evidence/DS-DEMAND-VINTAGE-LENS/",
           "/evidence/DS-QUAL-EVIDENCE/", "/evidence/VIS-PROVIDER-OBSERVABILITY/", "/evidence/VIS-FIRM-CONSTRAINTS/"],
}
SITE = ROOT / "design" / "reference" / "out"


def record_routes(site: Path) -> list[str]:
    """Every evidence record the site built, from its bundles (never a hand-kept list)."""
    return sorted(f"/evidence/{f.name[len('evidence_'):-len('__en.json')]}/" for f in (site / "_bundle").glob("evidence_*__en.json")
                  if f.name not in ("evidence__en.json", "evidence_compare__en.json"))


def bundle(route: str, lang: str) -> dict | None:
    """The page's governed bundle as the build wrote it (`check_content.py` reads the same files)."""
    name = (route.strip("/").replace("/", "_") or "home") + f"__{lang}.json"
    f = SITE / "_bundle" / name
    return json.loads(f.read_text(encoding="utf-8"))["page"] if f.exists() else None
EVIDENCE_ROUTES = EVIDENCE_BY_GATE["d2"]
HOOKS_ALL = ["#main", "a.skip", "#primary-nav", "[data-search-open]", "[data-cite]", "[data-lang]", "[data-menu][aria-controls=primary-nav]",
             "#utility-status[role=status]", "dialog#search-dialog", "#global-search-dialog[data-search-input]", "[data-search-status]", "[data-search-results]",
             "script#yfie-ui[type='application/json']", "script[src='/assets/app.js']", "link[rel=stylesheet][href='/assets/yfie.css']", "footer nav", "img[alt]",
             "h1#page-title", "nav[aria-labelledby=page-title]", "aside.spine nav.edges[aria-labelledby]"]
HOOKS_FAMILY = {
    "Evidence Record": ["meta[name=yfie-citation]", "meta[name=yfie-record-id]", "[data-evidence-boundary-first-load]", "#source", "[data-record-id] .evidence-cite-button[data-cite]", "#q1", "#q5", "#q7 details", "nav.strip[aria-labelledby=page-title]"],
    "Domain Answer": ["section.bnd", "#verify", "figure[data-visual-id][data-image-independent]", "figure .alt[data-visual-fallback]", "details.more"],
    "Question Entry": ["#questions", ".cluster ol.qlist", "#deeper"],
    "Orientation": ["section.bnd", "figure[data-visual-id][data-image-independent]", "figure .alt[data-visual-fallback]", ".head .st", ".head .actions", "#system", ".paced .compact.bound", "#sf .compact"],
    "Evidence Directory": ["#global-search[data-search-input]", "#search-results[data-search-results][aria-live]", "details.hub ol.hublist"],
    "Comparison": ["select#compare-a", "select#compare-b", "select#compare-c", "select#compare-d", "#compare-output", "#compare-status[role=status]", "script#yfie-compare", "script#yfie-compare-dimensions", "[data-compare-copy]", "[data-compare-boundary]"],
    "Data & Source": ["[data-source-filter]", "[data-source-filter-status][role=status]", "[data-source-no-results]", "[data-source-record][tabindex='-1']", "details.source-locator-details", ".source-locator [data-source-cite]"],
    "Reading": ["[data-reading-boundary]", "[data-reading-section]", "[data-reading-verify][data-reading-path-state]", "[data-path-record]", "[data-reading-related]", ".head .st", ".head .clocks time[datetime]"],
    "Reading Index": ["#featured", "#all ol.objs li.compact"],
    "Measurement": ["article.prio[id^=MA-][tabindex='-1']", "[data-measurement-readings]", "#agenda"],
    "Reference / Trust": ["section.qa h2"],
}
HOOKS_ROUTE = {
    "/contact/": ["[data-correction-context][data-context-mode=contact]", "[data-correction-mail][hidden]", "script#yfie-record-ids", "a[href^='mailto:']"],
    "/corrections/": ["[data-correction-context]", "[data-correction-empty]", "[data-correction-origin][hidden]", "[data-correction-error][hidden][role=alert]"],
}


def family_of(route: str) -> str:
    if route == "/readings/":
        return "Reading Index"
    if route.startswith("/readings/"):
        return "Reading"
    if route == "/measurement/":
        return "Measurement"
    if route in ("/methodology/", "/about/", "/corrections/", "/rights/", "/accessibility/", "/privacy/", "/terms/", "/contact/"):
        return "Reference / Trust"
    if route == "/explore/":
        return "Question Entry"
    if route == "/evidence/":
        return "Evidence Directory"
    if route == "/evidence/compare/":
        return "Comparison"
    if route == "/data/":
        return "Data & Source"
    if route.startswith("/evidence/"):
        return "Evidence Record"
    if route == "/":
        return "Orientation"
    return "Domain Answer"


# ------------------------------------------------------------------------------------------------ hard-state assertions (brief §9.2)
JS_ORDER = "(ab)=>{const [a,b]=ab;const x=document.querySelector(a),y=document.querySelector(b);return !!x&&!!y&&!!(x.compareDocumentPosition(y)&Node.DOCUMENT_POSITION_FOLLOWING)}"


def hard_state(pg, route: str, lang: str) -> dict:
    """Each case returns {check: bool}; every value must be true."""
    ev = pg.evaluate
    q = lambda s: ev("(s)=>document.querySelectorAll(s).length", s)  # noqa: E731
    out = {}
    if route == "/":   # orientation (D3 cold-reader test): the product's statement before the first figure; one link per object; one boundary per frame
        out["statement_in_head"] = q(".head .st p") >= 1 and q(".head .actions a") == 2
        out["statement_before_first_figure"] = ev(JS_ORDER, [".head .st", "#s3 .compact"])
        out["one_link_per_bound_object"] = ev("[...document.querySelectorAll('.compact.bound')].every(a=>a.querySelectorAll('a').length===1)")
        # the frame prints its boundary once; the governed text alternative may restate it (that is content — escalated)
        out["boundary_once_per_frame"] = ev("[...document.querySelectorAll('figure.fig')].every(f=>{const t=f.querySelector('.foot .b');if(!t)return false;const s=t.innerText.replace(/^[^:]*:\\s*/,'').slice(0,40);const c=f.cloneNode(true);c.querySelectorAll('.alt,figcaption').forEach(e=>e.remove());return c.textContent.split(s).length===2})")
        out["records_edge_lists_all"] = ev("document.querySelector('aside.spine:not(.foot-spine) nav.edges').querySelectorAll('li').length===4")
        out["double_rule_spans_column"] = ev("(()=>{const b=document.querySelector('section.bnd'),o=document.querySelector('article.page-obj');return !!b&&Math.abs(b.getBoundingClientRect().width-o.getBoundingClientRect().width)<2})()")
    if route == "/people/":   # dense_domain: wave, fieldwork, population and limitation attached to the headline figure
        fig = "figure[data-visual-id='VIS-FINDEX-GAPS']"
        out["figure_drawn"] = q(f"{fig} rect.bar") == 9
        out["values_printed"] = q(f"{fig} svg text.val") == 9
        out["gaps_calculated_not_bars"] = q(f"{fig} .gap") == 4 and q(f"{fig} .gap rect") == 0
        out["fieldwork_in_frame"] = ev(f"document.querySelector(\"{fig} .cap\").parentElement.innerText.includes('2022-11-07')")
        out["coverage_note_in_frame"] = ev(f"[...document.querySelectorAll(\"{fig} p.cap.note\")].some(p=>/1,000|1٬000/.test(p.innerText))")
        out["boundary_in_frame"] = q(f"{fig} .foot .b") == 1
        out["scannable_first_screen"] = ev("document.querySelector('h1').getBoundingClientRect().top < window.innerHeight")
    if route == "/access/":   # sparse_unknown: unknown geography visibly unknown — no map, no chart, the unknown stated before the answers
        fig = "figure[data-visual-id='VIS-ACCESS-EVIDENCE-LAYER']"
        out["no_map_no_chart"] = q(f"{fig} svg") == 0 and q(f"{fig} canvas") == 0 and q(f"{fig} img") == 0
        out["frame_present"] = q(f"{fig} .foot .b") == 1
        out["unknown_band_before_answers"] = ev("(()=>{const b=[...document.querySelectorAll('section.bnd')];const a=document.querySelector('article.page-obj section.qa h2');return b.length>=2&&!!a&&b.every(x=>x.compareDocumentPosition(a)&Node.DOCUMENT_POSITION_FOLLOWING)})()")
        out["no_zero_invented"] = ev("!/\\b0\\s*(access points|نقاط وصول)/.test(document.querySelector('#main').innerText)")
    if route == "/payments/":   # institutional_sequence: FPS, RTGS, institution-building as objects; withheld stays withheld; the small multiple never shares an axis
        fig = "figure[data-visual-id='VIS-PAYMENT-ANATOMY']"
        out["seven_objects"] = q(f"{fig} .obj-card") == 7
        out["withheld_without_value"] = q(f"{fig} .obj-card .withheld") == 2 and ev(f"[...document.querySelectorAll(\"{fig} .obj-card\")].filter(c=>c.querySelector('.withheld')).every(c=>!/\\d/.test(c.querySelector('.v').innerText))")
        out["not_comparable_marked"] = q(f"{fig} .mk") == 5
        out["is_not_lines"] = q(f"{fig} .isnot") == 7
        out["pos_three_panels_own_axes"] = q(".multiple figure svg.ts") == 3 and q(".multiple figure") == 3
        out["disagreement_marked"] = q("figure[data-visual-id='VIS-POS-TERMINALS'] .ring") == 3 and q("figure[data-visual-id='VIS-POS-TERMINALS'] .marks .dis") == 1
        out["missing_month_gap"] = q("figure[data-visual-id='VIS-POS-VALUE'] line.miss") == 1 and q("figure[data-visual-id='VIS-POS-VALUE'] .marks .miss") == 1 and q("figure[data-visual-id='VIS-POS-VALUE'] line.path") == 8
        out["nominal_on_axis_title"] = ev("document.querySelector(\"figure[data-visual-id='VIS-POS-VALUE'] .ph\").innerText.length > 0 && /nominal|الاسمية|اسمية/i.test(document.querySelector(\"figure[data-visual-id='VIS-POS-VALUE'] .ph\").innerText)")
        out["fps_rtgs_section_present"] = q("#s7") == 1
        if lang == "ar":   # mobile_rtl (asserted at every width; the ledger cites the 320 and 390 rows)
            out["ids_isolated_ltr"] = q("#main bdi[dir=ltr]") > 10
            out["axes_ltr"] = ev("[...document.querySelectorAll('figure svg')].every(s=>s.getAttribute('direction')==='ltr')")
            out["verify_path_present"] = q("#verify .compact") >= 3
    if route == "/reforms/":   # institutional_sequence: the rule-to-outcome chain with the first unproven link visible
        fig = "figure[data-visual-id='VIS-PAYMENT-RAILS']"
        out["chain_seven_steps"] = q(f"{fig} ol.chain li.step") == 7
        out["three_evidenced"] = q(f"{fig} li.step.evidenced") == 3
        out["first_open_marked"] = ev(f"(()=>{{const s=[...document.querySelectorAll(\"{fig} li.step\")];return s.findIndex(x=>x.classList.contains('open'))===3&&s[3].classList.contains('stop')}})()")
        out["no_values_plotted"] = q(f"{fig} svg") == 0
        out["events_dated_with_sources"] = q(f"{fig} .evs li") == 11 and q(f"{fig} .evs a.source-locator") == 11
    if route == "/remittances/":   # vintage_conflict: three states legible, the break not joined, MA-001 apart from the macro series
        fig = "figure[data-visual-id='VIS-REMITTANCE-MACRO']"
        out["three_states_keyed"] = q(f"{fig} .key li") == 3
        out["break_not_joined"] = q(f"{fig} line.brk") == 2 and q(f"{fig} line.path") == 11 and q(f"{fig} .marks .brk") == 1
        out["projection_dashed"] = q(f"{fig} line.path.dashed") == 5
        out["marks_by_state"] = q(f"{fig} circle.mark.a") == 7 and q(f"{fig} circle.mark.b") == 6
        out["values_printed"] = q(f"{fig} svg text.val") == 13
        out["reading_linked_not_redrawn"] = q("figure[data-visual-id='RV-CWR-001']") == 0 and q("#readings a[href*='same-year-different-number']") >= 1
        out["ma001_apart"] = q("#measure .compact") == 1 and q("figure #measure") == 0
        out["cost_figure_rows"] = q("figure[data-visual-id='VIS-REMITTANCE-COST'] .lane") == 2 and q("figure[data-visual-id='VIS-REMITTANCE-COST'] svg.trk") == 4
    if route.startswith("/evidence/") and route not in ("/evidence/", "/evidence/compare/"):   # every record (D4): the bundle says what the page must show
        b = bundle(route, lang)
        if b:
            cs = b["closure_state"]; v = b.get("visual")
            out["seven_questions"] = all(q(f"#q{i}") == 1 for i in range(1, 8))
            out["boundary_first_load"] = q("#q5[data-evidence-boundary-first-load]") == 1
            out["clock_before_claim"] = ev(JS_ORDER, [".head .clock", "h1#page-title"])
            out["strip_named"] = q("nav.strip[aria-labelledby=page-title]") == 1
            out["util_record"] = q(f"section.util[data-record-id='{b['id']}'] .evidence-cite-button[data-cite]") == 1
            out["nothing_looks_empty"] = q("#main .empty") == 0 and q("#main [role=alert]:not([hidden])") == 0
            out["source_cards_as_bundle"] = q("[data-evidence-source]") == len(b["sources"])
            out["locators_public"] = ev("[...document.querySelectorAll('a.source-locator')].every(a=>/^https?:/.test(a.getAttribute('href')||''))")
            out["lineage_state"] = (q(f".body [data-lineage-state='{cs}']") == 1) if b["lineage_statement"] else (q("[data-lineage-state]") == 0)
            out["members_listed"] = (q("#q6 ul.rlist li a") == len(b["members"])) if b["members"] else (q("#q6 ul.rlist") == 0)
            out["no_locator_state"] = (q(".body [data-evidence-source-unavailable]") == 1) == bool(b["no_source_message"])
            out["some_without_locator"] = (q("[data-evidence-sources-without-locator]") == 1) == bool(b["sources_without_locator_note"])
            out["trace_chips"] = (q(".chips .chip") == len(b["trace_ids"]) + 1) if b["trace_ids"] else (q(".chips") == 0)
            out["compare_entry"] = (q("[data-compare-entry]") == 1) == bool(b.get("compare_href"))
            out["own_visual"] = (q(f"#q1 figure.fig[data-visual-id='{v['id']}'][data-visual-fallback]") == 1) if (v and v.get("tier") != "RETIRE_FROM_DESIGN") else (q("#q1 figure.fig") == 0)
            out["used_in_readings"] = (q("article.page-obj[data-used-in-readings]") == 1) == bool(b["used_in_readings"])
            out["boundary_once_per_frame"] = ev("[...document.querySelectorAll('figure.fig')].every(f=>{const t=f.querySelector('.foot .b');if(!t)return false;const s=t.innerText.replace(/^[^:]*:\\s*/,'').slice(0,40);const c=f.cloneNode(true);c.querySelectorAll('.alt,figcaption').forEach(e=>e.remove());return c.textContent.split(s).length===2})")
    if route in ("/firms/", "/finance/", "/providers/"):   # the remaining domain answers (D4): the contract's order and every bound object
        b = bundle(route, lang)
        if b:
            out["question_then_answer"] = ev(JS_ORDER, [".head .q", "h1#page-title"])
            out["band_before_primary"] = (ev(JS_ORDER, ["section.bnd", "section.qa"]) if b["band"] else True)
            out["primary_visual_framed"] = (q(f"figure.fig[data-visual-id='{b['primary_visual']}'][data-visual-fallback]") == 1) if b["primary_visual"] else (q("figure.fig") == 0)
            out["verify_objects"] = q("#verify .compact") == len(b["verify"])
            out["all_records_disclosed"] = q("#verify details ul.rlist li") == len(b["all_records"])
            out["readings_at_most_two"] = q("#readings .compact") == min(len(b["readings"]), 2)
            out["measurement_objects"] = q("#measure .compact") == len(b["measurement"])
            out["one_disclosure_for_depth"] = (q("#more details.more") == 1) if b["progressive"] else (q("#more") == 0)
            out["related_governed"] = (q("#related li") == len(b["related"]["links"]) and q("#related p.small") == 1) if b["related"] else (q("#related") == 0)
            if route == "/finance/":
                out["chronology_bound"] = q("#chronology ol.chron li.compact") == len(b["chronology"]["items"])
    if route == "/evidence/CLM-004/":   # verification_sparse: a framing rule is not an error
        out["no_source_cards"] = q("[data-evidence-source]") == 0
        out["framing_statement_as_answer"] = q(".body [data-lineage-state='FRAMING_NO_FACT']") == 1
        out["nothing_looks_empty"] = q("#main .empty") == 0 and q("#main [role=alert]") == 0
        out["seven_questions"] = all(q(f"#q{i}") == 1 for i in range(1, 8))
    if route == "/evidence/CLM-015/":   # thin single-source record: the same object, not weaker
        out["one_source_card"] = q("[data-evidence-source]") == 1
        out["seven_questions"] = all(q(f"#q{i}") == 1 for i in range(1, 8))
        out["nothing_looks_empty"] = q("#main .empty") == 0
    if route == "/evidence/CLM-044/":   # withheld: the value never appears; the missing locator is a stated state
        out["no_locator_stated"] = q(".body [data-evidence-source-unavailable]") == 1
        out["no_source_named"] = q("[data-evidence-source]") == 0 and q("a.source-locator") == 0
        out["nothing_looks_empty"] = q("#main .empty") == 0
        out["no_usd_value"] = ev("!/US\\$\\s?\\d|\\d[\\d,]*\\s?(million|مليون)/.test(document.querySelector('#main').innerText)")
    if route == "/evidence/CLM-031/":
        out["composite_with_members"] = q(".body [data-lineage-state='COMPOSITE_OF_OBJECTS']") == 1 and q("#q6 ul.rlist li a") == 5
    if route == "/evidence/CLM-014/":
        out["composite_without_members"] = q(".body [data-lineage-state='COMPOSITE_MEMBERS_NOT_LISTED']") == 1 and q("#q6 ul.rlist") == 0 and q("#main .empty") == 0
    if route == "/evidence/CLM-039/":
        out["partial_lineage"] = q(".body [data-lineage-state='PARTIALLY_RESOLVED']") == 1 and q("[data-evidence-source]") == 1
    if route == "/evidence/CLM-045/":
        out["some_without_locator"] = q("[data-evidence-sources-without-locator]") == 1 and q("[data-evidence-source]") >= 1
    if route == "/evidence/CLM-001/":
        out["sources_listed"] = q("[data-evidence-source]") == 2 and q("[data-compare-entry]") == 1
    if route == "/evidence/compare/":   # compare_unlike: the boundary is the first conclusion; no visual pressure to compare values
        out["boundary_before_controls"] = ev(JS_ORDER, ["[data-compare-boundary]", "select#compare-a"])
        out["verdict_before_table"] = ev(JS_ORDER, ["[data-compare-verdict]", "table.compare-table"])
        out["verdict_in_boundary_voice"] = ev("getComputedStyle(document.querySelector('[data-compare-verdict]')).borderTopStyle==='double'")
        out["no_numeric_columns"] = ev("![...document.querySelectorAll('table.compare-table thead th')].some(th=>/^\\d/.test(th.innerText.trim()))")
        out["states_text_labelled"] = ev("[...document.querySelectorAll('table.compare-table tbody tr')].every(tr=>tr.querySelector('.compare-state')&&tr.querySelector('.compare-state').innerText.trim().length>0)")
        out["table_in_named_region"] = q(".table-wrap[role=region][aria-label]") >= 1
    if route == "/data/":   # source_scale: every source discoverable, none a wall of links; curated cards visibly curated
        out["all_public_sources"] = q("[data-source-record]") == 151
        out["curated_28_by_category"] = q(".curated [data-source-record]") == 28 and q(".curated .cat") == 6
        out["supporting_open_reference_closed"] = ev("document.querySelector('details.source-supporting-details').open===true && document.querySelector('details.source-reference-details').open===false")
        out["every_source_named_or_referenced"] = ev("[...document.querySelectorAll('[data-source-record]')].every(r=>r.querySelector('h4,strong')&&r.querySelector('.rref'))")
        out["chronology_24"] = q("ol.chron li.compact") == 24
        out["no_locator_never_named"] = ev("!/SRC-CCY-REMIT-ESTIMATE-2025/.test(document.querySelector('#main').innerText)")
    if route == "/explore/":
        out["four_clusters_eleven_questions"] = q(".cluster") == 4 and q(".cluster ol.qlist li") == 11
        out["no_pills_no_cards"] = q(".pill") == 0 and q(".card-grid") == 0
    if route == "/evidence/":
        out["hub_groups_all_records"] = q("details.hub") == 10 and q(".hublist li") == 110
        out["search_with_status"] = q("#global-search") == 1 and q("[data-search-status]") >= 2
    if route.startswith("/readings/") and route != "/readings/":   # reading_longform: bounded, readable, traceable
        out["boundary_before_essay"] = ev(JS_ORDER, ["[data-reading-boundary]", ".essay [data-reading-section]"])
        out["standfirst_and_clocks"] = q(".head .st p") == 1 and q(".head .clock") == 2
        out["essay_sections"] = q(".essay [data-reading-section]") >= 3
        out["closing_section_headed"] = ev("(()=>{const s=[...document.querySelectorAll('.essay [data-reading-section]')];const l=s[s.length-1];return !!l&&!!l.querySelector('h2')})()")
        out["at_most_one_figure_after_opening"] = q("figure.fig") <= 1 and (q("figure.fig") == 0 or q(".essay [data-reading-section]:first-child figure.fig") == 1)
        out["trace_to_records"] = q("[data-path-record]") >= 1 and q("[data-reading-verify] .compact .q a") >= 1
        out["sources_or_status"] = q("#sources article.src") >= 1 or q("[data-reading-path-state]") == 1
        out["related_one_or_two"] = 1 <= q("[data-reading-related] .compact") <= 2
        out["no_lifted_number"] = q(".head .st b, .head .st strong") == 0
        # the essay measure is the language's --measure (64ch Latin / 34em Arabic), never the column: a paragraph is
        # narrower than the page object at 1440 and never wider than 720 px
        out["measure_bounded"] = ev("(()=>{const p=document.querySelector('.essay .read p');const o=document.querySelector('article.page-obj');if(!p||!o)return false;const w=p.getBoundingClientRect().width,c=o.getBoundingClientRect().width;return w<=720&&(c<900||w<c*0.9)})()")
    if route == "/readings/":
        out["featured_then_all"] = q("#featured .compact") == 1 and q("#all li.compact") == 9 and q("#all li.compact .clock") == 9
    if route == "/measurement/":   # measurement_nonranking: sequencing within the agenda, never a ranking
        out["ten_priorities_deep_linkable"] = q("article.prio[id^=MA-][tabindex='-1']") == 10
        out["no_ordinal_numbering"] = q(".prios ol, .prios .n, .prios li") == 0
        out["priority_label_governed"] = ev("[...document.querySelectorAll('.prios .clock .k')].every(k=>k.innerText.trim().length>0) && [...document.querySelectorAll('.prios .clock .v')].every(v=>/P[01]/.test(v.innerText))")
        out["equal_weight"] = ev("(()=>{const h=[...document.querySelectorAll('.prios h3')];const s=new Set(h.map(x=>getComputedStyle(x).fontSize));return h.length===10&&s.size===1})()")
        out["current_missing_decision"] = q(".prios .body p") == 30
        out["gaps_examined_links"] = q("[data-measurement-readings] a") >= 1
    if route == "/methodology/":
        out["sections_indexed"] = q("article.page-obj section.qa h2") >= 13 and q("aside.spine nav.index li") >= 13
        out["records_bound"] = q("#blk-records .compact") >= 1
    if route == "/about/":   # trust_plain_language: no backend terminology
        out["plain_language"] = ev("!/\\b(CLM|VIS|SRC|DS|UI|MA)-\\d|Page Spec|projection|closure_state|backend|enum/i.test(document.querySelector('article.page-obj').innerText)")
        out["purpose_role_limits_correction"] = q("article.page-obj section.qa") >= 6
        out["contact_actionable"] = q("a[href^='mailto:']") >= 1
    if route == "/contact/":
        out["mail_hidden_without_record"] = ev("document.querySelector('[data-correction-mail]').hidden===true")
        out["address_actionable"] = q("article.page-obj a[href^='mailto:']") >= 2
    if route == "/corrections/":
        out["no_manufactured_history"] = ev("document.querySelector('[data-correction-empty]').hidden!==true && document.querySelector('[data-correction-origin]').hidden===true")
    if route in ("/rights/", "/accessibility/", "/privacy/", "/terms/"):
        out["governed_sections"] = q("article.page-obj section.qa h2") >= 3 and q("#main .empty") == 0
    return out


def not_found_checks(pg, base: str) -> dict:
    """The bilingual 404 (not a per-language route): Arabic first, both sections, one h1, the search action, no inline style."""
    out = {}
    for w in (320, 1440):
        pg.set_viewport_size({"width": w, "height": 844 if w < 700 else 900})
        pg.goto(f"{base}/404.html", wait_until="load"); pg.wait_for_timeout(120)
        r = pg.evaluate("""() => { const d=document.documentElement; return {over:d.scrollWidth-d.clientWidth, h1:document.querySelectorAll('h1').length, ar:d.lang==='ar'&&d.dir==='rtl',
            sections:document.querySelectorAll('section.nf').length, en:!!document.querySelector("section.nf[lang=en][dir=ltr]"), search:!!document.querySelector('[data-search-open]'), dialog:!!document.querySelector('dialog#search-dialog'),
            inline:document.querySelectorAll('[style]').length, imgs:[...document.images].filter(i=>!i.hasAttribute('alt')).length, robots:!!document.querySelector('meta[name=robots][content=noindex]')} }""")
        out[f"{w}px"] = r["over"] <= 1 and r["h1"] == 1 and r["ar"] and r["sections"] == 2 and r["en"] and r["search"] and r["dialog"] and r["inline"] == 0 and r["imgs"] == 0 and r["robots"]
    return out


def root_checks(pg, base: str) -> dict:
    """The neutral root entry (hreflang x-default): no inline script; with script it opens the edition chosen before, else
    Arabic; without script the same fallback through the no-script refresh."""
    out = {}
    raw = pg.request.get(f"{base}/index.html").text()
    out["no_inline_script"] = ("<script src=" in raw) and ("<script>" not in raw) and ("style=" not in raw)
    out["hreflang_both"] = ('hreflang="en"' in raw) and ('hreflang="ar"' in raw) and ('hreflang="x-default"' in raw)
    pg.goto(f"{base}/index.html", wait_until="load"); pg.wait_for_timeout(200)
    out["arabic_by_default"] = pg.url.rstrip("/").endswith("/ar")
    pg.evaluate("localStorage.setItem('yfie-lang','en')")
    pg.goto(f"{base}/index.html", wait_until="load"); pg.wait_for_timeout(200)
    out["chosen_edition_kept"] = pg.url.rstrip("/").endswith("/en")
    pg.evaluate("localStorage.removeItem('yfie-lang')")
    return out


def serve(directory: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=str(directory)))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=str(ROOT / "design/reference/out"))
    ap.add_argument("--gate", default="d2")
    ap.add_argument("--shots", action="store_true")
    ap.add_argument("--degraded", action="store_true")
    ap.add_argument("--evidence", default="")
    ap.add_argument("--only", default="", help="comma-separated substrings; keep only the gate's routes that contain one (a quick partial run, never a record)")
    args = ap.parse_args()
    site = Path(args.site)
    global SITE
    SITE = site
    routes = GATES[args.gate] + (record_routes(site) if args.gate == "d4" else [])
    if args.only:
        keys = [k for k in args.only.split(",") if k]
        routes = [r for r in routes if any(k in r for k in keys)]
    if not (site / "en" / "index.html").exists():
        print(f"site not built: {site}"); return 2
    shots = site / "_review"
    shots.mkdir(exist_ok=True)
    from playwright.sync_api import sync_playwright
    httpd, base = serve(site)
    failures, rows = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in WIDTHS:
            ctx = b.new_context(viewport={"width": w, "height": 844 if w < 700 else 900}, reduced_motion="reduce")
            ctx.grant_permissions(["clipboard-read", "clipboard-write"])
            pg = ctx.new_page()
            for lang in ("en", "ar"):
                for r in routes:
                    url = f"{base}/{lang}{r}"
                    pg.goto(url, wait_until="load"); pg.wait_for_timeout(120)
                    res = pg.evaluate("""() => {
                      const d=document.documentElement;
                      const over=d.scrollWidth-d.clientWidth;
                      const imgs=[...document.images].filter(i=>!i.hasAttribute('alt')).length;
                      const h1=document.querySelectorAll('h1').length;
                      const dir=d.getAttribute('dir');
                      const wide=[...document.querySelectorAll('main *')].filter(e=>{const rr=e.getBoundingClientRect();return rr.width>0&&rr.right>d.clientWidth+2&&getComputedStyle(e).position!=='fixed'&&!e.closest('.table-wrap')}).slice(0,3).map(e=>e.tagName+'.'+(e.className&&e.className.baseVal!==undefined?e.className.baseVal:e.className));
                      const inline=document.querySelectorAll('[style]').length;
                      const unnamed=[...document.querySelectorAll('nav')].filter(n=>!n.getAttribute('aria-label')&&!n.getAttribute('aria-labelledby')).length;
                      return {over,imgs,h1,dir,wide,inline,unnamed,height:d.scrollHeight};
                    }""")
                    pg.keyboard.press("Tab")
                    first = pg.evaluate("document.activeElement && document.activeElement.className")
                    pg.evaluate("document.activeElement && document.activeElement.blur()")
                    fam = family_of(r)
                    missing = [sel for sel in HOOKS_ALL + HOOKS_FAMILY.get(fam, []) + HOOKS_ROUTE.get(r, []) if pg.evaluate("(s)=>!!document.querySelector(s)", sel) is False]
                    small = pg.evaluate("""() => [...document.querySelectorAll('main a[href], main button, main select')].filter(e=>{const r=e.getBoundingClientRect(); return getComputedStyle(e).display!=='inline' && r.width>0 && r.height>0 && r.height<24}).slice(0,5).map(e=>e.tagName+'.'+(e.className||'')+':'+Math.round(e.getBoundingClientRect().height))""")
                    ok = (res["over"] <= 1 and res["imgs"] == 0 and res["h1"] == 1 and first == "skip" and res["dir"] == ("rtl" if lang == "ar" else "ltr")
                          and not res["wide"] and res["inline"] == 0 and res["unnamed"] == 0 and not missing and not small)
                    row = {"width": w, "lang": lang, "route": r, "family": fam, **res, "first_tab": first, "missing_hooks": missing, "small_targets": small, "ok": ok}
                    if w == 1440 or (w == 390 and r == "/payments/" and lang == "ar") or (w == 320 and r == "/payments/" and lang == "ar"):
                        hs = hard_state(pg, r, lang)
                        row["hard_state"] = hs
                        bad = [k for k, v in hs.items() if not v]
                        if bad:
                            failures.append({"width": w, "lang": lang, "route": r, "hard_state_failed": bad})
                    rows.append(row)
                    if not ok:
                        failures.append(row)
                    if args.shots and w in (390, 1440):
                        tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}-{w}"
                        pg.screenshot(path=str(shots / f"{tag}.png"))
                    if w in (390, 1440):
                        smoke = {}
                        pg.click("[data-search-open]"); pg.wait_for_timeout(100)
                        smoke["dialog_open"] = pg.evaluate("document.querySelector('#search-dialog').open === true")
                        smoke["dialog_focus_in"] = pg.evaluate("document.activeElement && document.activeElement.id === 'global-search-dialog'")
                        pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
                        smoke["dialog_closed"] = pg.evaluate("document.querySelector('#search-dialog').open === false")
                        if w == 390:
                            pg.click("[data-menu]"); pg.wait_for_timeout(100)
                            smoke["menu_expanded"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded') === 'true' && document.querySelector('#primary-nav').classList.contains('open')")
                            pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
                            smoke["menu_closed"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded') === 'false'")
                        pg.locator("[data-cite]:visible").first.click(); pg.wait_for_timeout(250)
                        smoke["cite_announced"] = pg.evaluate("document.querySelector('#utility-status').textContent.trim().length > 0")
                        pg.goto(url, wait_until="load"); pg.wait_for_timeout(120)
                        reached = False
                        for _ in range(40):
                            pg.keyboard.press("Tab")
                            if pg.evaluate("document.activeElement===document.querySelector('[data-search-open]')"):
                                reached = True; break
                        smoke["kb_search_reached"] = reached
                        pg.keyboard.press("Enter"); pg.wait_for_timeout(150)
                        smoke["kb_dialog_open"] = pg.evaluate("document.querySelector('#search-dialog').open === true && document.activeElement.id === 'global-search-dialog'")
                        pg.keyboard.press("Escape"); pg.wait_for_timeout(150)
                        smoke["kb_dialog_closed"] = pg.evaluate("document.querySelector('#search-dialog').open === false")
                        row["smoke"] = smoke
                        bad = [k for k, v in smoke.items() if not v]
                        if bad:
                            failures.append({"width": w, "lang": lang, "route": r, "smoke_failed": bad})
            ctx.close()
        if args.degraded:
            deg = site / "_review" / "degraded"; deg.mkdir(parents=True, exist_ok=True)
            for lang in ("en", "ar"):
                for r in {"d2": ["/payments/", "/remittances/", "/people/", "/reforms/", "/access/", "/evidence/compare/", "/data/", "/explore/", "/evidence/", "/evidence/CLM-004/"],
                          "d3": ["/", "/readings/after-transfer-persistence/", "/readings/banking-jump-measurement-basis/", "/readings/", "/measurement/", "/methodology/", "/about/", "/contact/", "/corrections/"],
                          "d4": ["/firms/", "/finance/", "/providers/", "/evidence/CLM-046/", "/evidence/VIS-PROVIDER-OBSERVABILITY/"]}[args.gate]:
                    tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}"
                    url = f"{base}/{lang}{r}"
                    ctx = b.new_context(viewport={"width": 794, "height": 1123}); pg = ctx.new_page()
                    pg.goto(url, wait_until="load"); pg.emulate_media(media="print"); pg.wait_for_timeout(150)
                    pg.screenshot(path=str(deg / f"{tag}-print.png"))
                    print_ok = pg.evaluate("(() => { const f=document.querySelector('figure.fig'); if(!f) return true; return f.getBoundingClientRect().height>0 && getComputedStyle(f.querySelector('.foot .b')).display!=='none'; })()")
                    ctx.close()
                    ctx = b.new_context(viewport={"width": 390, "height": 844}, java_script_enabled=False); pg = ctx.new_page()
                    pg.route("**/*.css", lambda rt: rt.abort()); pg.route("**/*.png", lambda rt: rt.abort())
                    pg.goto(url, wait_until="load"); pg.wait_for_timeout(100)
                    pg.screenshot(path=str(deg / f"{tag}-nocss-nojs-noimg.png"))
                    order_ok = pg.evaluate("(() => { const h1=document.querySelector('h1'); const main=document.querySelector('#main'); return !!h1 && !!main && main.contains(h1); })()")
                    ctx.close()
                    fc_ok = True
                    ctx = b.new_context(viewport={"width": 1440, "height": 900}, forced_colors="active", color_scheme="dark"); pg = ctx.new_page()
                    pg.goto(url, wait_until="load"); pg.wait_for_timeout(150)
                    if pg.evaluate("!!document.querySelector('figure svg text.val')"):
                        fc_ok = pg.evaluate("""() => { const t=document.querySelector('figure svg text.val'); const m=document.querySelector('figure svg .mark.a, figure svg rect.bar');
                            const f=e=>getComputedStyle(e).fill; return !!t && !!m && f(t)===f(m) && f(t)!=='rgb(23, 33, 43)'; }""")
                    pg.screenshot(path=str(deg / f"{tag}-forced-colours.png"))
                    ctx.close()
                    checks = {"print_figure_whole": print_ok, "no_css_order_ok": order_ok, "forced_colours_ok": fc_ok}
                    rows.append({"width": "degraded", "lang": lang, "route": r, "ok": all(checks.values()), "degraded": checks})
                    if not all(checks.values()):
                        failures.append({"lang": lang, "route": r, "degraded_failed": [k for k, v in checks.items() if not v]})
        if args.gate in ("d3", "d4"):
            ctx = b.new_context(viewport={"width": 320, "height": 844}); pg = ctx.new_page()
            nf = not_found_checks(pg, base)
            if args.gate == "d4":
                rc = root_checks(pg, base)
                rows.append({"width": "404", "lang": "neutral", "route": "/index.html", "ok": all(rc.values()), "hard_state": rc, "height": 0, "over": 0, "imgs": 0, "h1": 1, "dir": "-", "wide": [], "inline": 0, "unnamed": 0, "first_tab": "", "missing_hooks": [], "small_targets": []})
                if not all(rc.values()):
                    failures.append({"route": "/index.html", "root_failed": [k for k, v in rc.items() if not v]})
            rows.append({"width": "404", "lang": "ar+en", "route": "/404.html", "ok": all(nf.values()), "hard_state": nf, "height": 0, "over": 0, "imgs": 0, "h1": 1, "dir": "rtl", "wide": [], "inline": 0, "unnamed": 0, "first_tab": "", "missing_hooks": [], "small_targets": []})
            if not all(nf.values()):
                failures.append({"route": "/404.html", "not_found_failed": [k for k, v in nf.items() if not v]})
            if args.evidence:
                evd = Path(args.evidence); evd.mkdir(parents=True, exist_ok=True)
                for w in (390, 1440):
                    pg.set_viewport_size({"width": w, "height": 844 if w < 700 else 900}); pg.goto(f"{base}/404.html", wait_until="load"); pg.wait_for_timeout(120)
                    pg.screenshot(path=str(evd / f"404-{w}.png"))
            ctx.close()
        if args.evidence:
            evd = Path(args.evidence); evd.mkdir(parents=True, exist_ok=True)
            for w in (390, 1440):
                ctx = b.new_context(viewport={"width": w, "height": 844 if w < 700 else 900}); pg = ctx.new_page()
                for lang in ("en", "ar"):
                    for r in EVIDENCE_BY_GATE.get(args.gate, EVIDENCE_ROUTES):
                        tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}-{w}"
                        pg.goto(f"{base}/{lang}{r}", wait_until="load"); pg.wait_for_timeout(150)
                        pg.screenshot(path=str(evd / f"{tag}.png"))
                        if w == 1440 and r in ("/payments/", "/remittances/", "/people/", "/reforms/"):
                            for fig in pg.locator("figure.fig").all():
                                vid = fig.get_attribute("data-visual-id")
                                if vid in ("VIS-FINDEX-GAPS", "VIS-REMITTANCE-MACRO", "VIS-REMITTANCE-COST", "VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE", "VIS-PAYMENT-ANATOMY", "VIS-PAYMENT-RAILS"):
                                    fig.screenshot(path=str(evd / f"figure-{vid}-{lang}.png"))
                ctx.close()
        b.close()
    httpd.shutdown()
    for row in rows:
        if row["width"] == "degraded":
            print(f"degrad {row['lang']} {row['route']:36s} {row['degraded']}")
            continue
        if row["width"] == "404":
            print(f"  404 {row['lang']} {row['route']:36s} {row['hard_state']}")
            continue
        flag = "" if row["ok"] else f"  <-- over={row['over']} imgs={row['imgs']} h1={row['h1']} first={row['first_tab']} wide={row['wide']} inline={row['inline']} unnamed={row['unnamed']} missing={row['missing_hooks']} small={row.get('small_targets')}"
        hs = row.get("hard_state")
        hflag = "" if not hs or all(hs.values()) else f"  HARD-STATE FAILED: {[k for k, v in hs.items() if not v]}"
        print(f"{row['width']:5d} {row['lang']} {row['route']:36s} height={row['height']:6d}{flag}{hflag}")
    main_rows = [r for r in rows if r["width"] not in ("degraded", "404")]
    smokes = [r for r in main_rows if "smoke" in r]
    hard = [r for r in rows if r.get("hard_state") and r["width"] != "degraded"]
    print(f"{len(main_rows)} renders checked; {sum(1 for r in main_rows if not r['ok'])} failed; {len(smokes)} smoke tests, {sum(1 for r in smokes if all(r['smoke'].values()))} passed; "
          f"{sum(len(r['hard_state']) for r in hard)} hard-state assertions on {len(hard)} route renders, {sum(sum(1 for v in r['hard_state'].values() if v) for r in hard)} passed"
          + (f"; {sum(1 for r in rows if r['width']=='degraded')} degraded renders, {sum(1 for r in rows if r['width']=='degraded' and r['ok'])} ok" if args.degraded else ""))
    (site / f"_review_{args.gate}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
