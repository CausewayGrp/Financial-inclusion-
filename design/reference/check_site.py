#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendered checks for the reference implementation beyond the D1 trio — the D2 hard families — in both languages.

  python3 design/reference/check_site.py [--site design/reference/out] [--gate d2] [--shots] [--degraded] [--evidence DIR]

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
EVIDENCE_ROUTES = ["/explore/", "/people/", "/access/", "/payments/", "/remittances/", "/reforms/", "/evidence/", "/evidence/compare/", "/data/", "/evidence/CLM-004/", "/evidence/CLM-044/"]
HOOKS_ALL = ["#main", "a.skip", "#primary-nav", "[data-search-open]", "[data-cite]", "[data-lang]", "[data-menu][aria-controls=primary-nav]",
             "#utility-status[role=status]", "dialog#search-dialog", "#global-search-dialog[data-search-input]", "[data-search-status]", "[data-search-results]",
             "script#yfie-ui[type='application/json']", "script[src='/assets/app.js']", "link[rel=stylesheet][href='/assets/yfie.css']", "footer nav", "img[alt]",
             "h1#page-title", "nav[aria-labelledby=page-title]", "aside.spine nav.edges[aria-labelledby]"]
HOOKS_FAMILY = {
    "Evidence Record": ["meta[name=yfie-citation]", "meta[name=yfie-record-id]", "[data-evidence-boundary-first-load]", "#source", "[data-record-id] .evidence-cite-button[data-cite]", "#q1", "#q5", "#q7 details", "nav.strip[aria-labelledby=page-title]"],
    "Domain Answer": ["section.bnd", "#verify", "figure[data-visual-id][data-image-independent]", "figure .alt[data-visual-fallback]", "details.more"],
    "Question Entry": ["#questions", ".cluster ol.qlist", "#deeper"],
    "Evidence Directory": ["#global-search[data-search-input]", "#search-results[data-search-results][aria-live]", "details.hub ol.hublist"],
    "Comparison": ["select#compare-a", "select#compare-b", "select#compare-c", "select#compare-d", "#compare-output", "#compare-status[role=status]", "script#yfie-compare", "script#yfie-compare-dimensions", "[data-compare-copy]", "[data-compare-boundary]"],
    "Data & Source": ["[data-source-filter]", "[data-source-filter-status][role=status]", "[data-source-no-results]", "[data-source-record][tabindex='-1']", "details.source-locator-details", ".source-locator [data-source-cite]"],
}


def family_of(route: str) -> str:
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
    return "Domain Answer"


# ------------------------------------------------------------------------------------------------ hard-state assertions (brief §9.2)
JS_ORDER = "(ab)=>{const [a,b]=ab;const x=document.querySelector(a),y=document.querySelector(b);return !!x&&!!y&&!!(x.compareDocumentPosition(y)&Node.DOCUMENT_POSITION_FOLLOWING)}"


def hard_state(pg, route: str, lang: str) -> dict:
    """Each case returns {check: bool}; every value must be true."""
    ev = pg.evaluate
    q = lambda s: ev("(s)=>document.querySelectorAll(s).length", s)  # noqa: E731
    out = {}
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
    args = ap.parse_args()
    site = Path(args.site)
    routes = GATES[args.gate]
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
                    missing = [sel for sel in HOOKS_ALL + HOOKS_FAMILY.get(fam, []) if pg.evaluate("(s)=>!!document.querySelector(s)", sel) is False]
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
                for r in ["/payments/", "/remittances/", "/people/", "/reforms/", "/access/", "/evidence/compare/", "/data/", "/explore/", "/evidence/", "/evidence/CLM-004/"]:
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
        if args.evidence:
            evd = Path(args.evidence); evd.mkdir(parents=True, exist_ok=True)
            for w in (390, 1440):
                ctx = b.new_context(viewport={"width": w, "height": 844 if w < 700 else 900}); pg = ctx.new_page()
                for lang in ("en", "ar"):
                    for r in EVIDENCE_ROUTES:
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
        flag = "" if row["ok"] else f"  <-- over={row['over']} imgs={row['imgs']} h1={row['h1']} first={row['first_tab']} wide={row['wide']} inline={row['inline']} unnamed={row['unnamed']} missing={row['missing_hooks']} small={row.get('small_targets')}"
        hs = row.get("hard_state")
        hflag = "" if not hs or all(hs.values()) else f"  HARD-STATE FAILED: {[k for k, v in hs.items() if not v]}"
        print(f"{row['width']:5d} {row['lang']} {row['route']:36s} height={row['height']:6d}{flag}{hflag}")
    main_rows = [r for r in rows if r["width"] != "degraded"]
    smokes = [r for r in main_rows if "smoke" in r]
    hard = [r for r in main_rows if r.get("hard_state")]
    print(f"{len(main_rows)} renders checked; {sum(1 for r in main_rows if not r['ok'])} failed; {len(smokes)} smoke tests, {sum(1 for r in smokes if all(r['smoke'].values()))} passed; "
          f"{sum(len(r['hard_state']) for r in hard)} hard-state assertions on {len(hard)} route renders, {sum(sum(1 for v in r['hard_state'].values() if v) for r in hard)} passed"
          + (f"; {sum(1 for r in rows if r['width']=='degraded')} degraded renders, {sum(1 for r in rows if r['width']=='degraded' and r['ok'])} ok" if args.degraded else ""))
    (site / f"_review_{args.gate}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
