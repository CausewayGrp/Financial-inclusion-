#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Journeys and technical states on the rendered reference site (D5), by keyboard, on mobile and desktop, in both languages.

  python3 design/reference/check_journeys.py [--site design/reference/out] [--only J01,J10,...] [--evidence DIR]

Journeys: the thirteen journeys of the inventory (`handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` → `journeys`). Each is
walked at 390 and 1440 px in English and Arabic: from each page of the path, the next page must be reachable through a
link the page itself offers (in the page object, the spine, the product bar or the footer; through the menu on a phone),
that link must take keyboard focus and activate with Enter, and the landing page must hold the journey's success
condition, asserted on the DOM (`SUCCESS`). Technical states: every technical state of the ledger is driven and must
look technical — an announced status or alert in the technical voice (a dashed rule, never the boundary's double rule,
never the evidence-gap object) — while the evidence around it stays readable and navigation keeps working. Exit 1 on
any failure. Proof for the record, not authority; design/COVERAGE.csv cites this tool's output.
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
INV = json.loads((ROOT / "handoff" / "ROUTE_CONTENT_AND_STATE_INVENTORY.json").read_text(encoding="utf-8"))
JOURNEYS = INV["journeys"]
WIDTHS = {"mobile": (390, 844), "desktop": (1440, 900)}

JS_ORDER = "(ab)=>{const [a,b]=ab;const x=document.querySelector(a),y=document.querySelector(b);return !!x&&!!y&&!!(x.compareDocumentPosition(y)&Node.DOCUMENT_POSITION_FOLLOWING)}"

# What each landing must show for the journey's success condition (proxies asserted on the DOM; the sentence itself is
# in the inventory). Keys are route prefixes.
def SUCCESS(pg, route: str) -> dict:
    ev = pg.evaluate
    q = lambda s: ev("(s)=>document.querySelectorAll(s).length", s)  # noqa: E731
    out = {"one_h1": q("h1") == 1, "main": q("#main") == 1}
    if route.startswith("/evidence/") and route not in ("/evidence/", "/evidence/compare/"):
        out["clock_before_claim"] = ev(JS_ORDER, [".head .clock", "h1#page-title"])
        out["population_answer"] = q("#q3 p") >= 1
        out["limitation_first_load"] = q("#q5[data-evidence-boundary-first-load]") == 1
        out["source_path"] = q("#q6 [data-evidence-source], #q6 [data-lineage-state], #q6 [data-evidence-source-unavailable]") >= 1
        out["method_in_depth"] = q("#q7 details") == 1
        out["report_carries_record"] = ev("!![...document.querySelectorAll('a[href*=\"/contact/?record=\"]')].length")
    elif route in ("/people/", "/access/", "/payments/", "/remittances/", "/reforms/", "/firms/", "/finance/", "/providers/"):
        out["question_then_answer"] = ev(JS_ORDER, [".head .q", "h1#page-title"])
        out["answer_before_depth"] = ev(JS_ORDER, ["section.qa", "details.more"]) if q("details.more") else True
        out["boundary_visible"] = q("section.bnd") >= 1
        out["primary_verification_route"] = q(".head .actions a, .head-rule .actions a") == 2 and q("#verify .compact") >= 1
    elif route == "/explore/":
        out["questions_first"] = q("#questions .cluster ol.qlist li") == 11
    elif route == "/":
        out["statement_then_figures"] = ev(JS_ORDER, [".head .st", "#s3 .compact"])
    elif route == "/data/":
        out["register_with_filter"] = q("[data-source-filter]") == 1 and q("[data-source-record]") >= 1
        out["rights_note"] = q("[data-rights-note], .src .rights, #s2, .register .small") >= 1
    elif route == "/evidence/":
        out["search_and_compare_entry"] = q("#global-search") == 1 and q("a[href$='/evidence/compare/']") >= 1
    elif route == "/evidence/compare/":
        out["boundary_before_controls"] = ev(JS_ORDER, ["[data-compare-boundary]", "select#compare-a"])
    elif route.startswith("/readings/") and route != "/readings/":
        out["boundary_before_essay"] = ev(JS_ORDER, ["[data-reading-boundary]", ".essay"])
        out["direct_links_to_records"] = q("[data-path-record] a[href*='/evidence/']") >= 1
    elif route == "/methodology/":
        out["records_bound_at_method_depth"] = q("#blk-records .compact") >= 1
    elif route == "/contact/":
        out["report_path"] = q("[data-correction-context][data-context-mode=contact]") == 1
        if "record=" in pg.url:
            out["record_carried"] = ev("(()=>{const o=document.querySelector('[data-correction-origin]');return !!o&&!o.hidden&&/[A-Z]+-\\d+/.test(o.innerText)})()")
            out["mail_action_revealed"] = ev("(()=>{const m=document.querySelector('[data-correction-mail]');return !!m&&!m.hidden})()")
        out["links_on_to_corrections"] = q("a[href$='/corrections/']") >= 1
    elif route == "/corrections/":
        out["correction_context"] = q("[data-correction-context]") == 1
    elif route in ("/rights/", "/terms/", "/accessibility/", "/about/", "/privacy/"):
        out["sections"] = q("article.page-obj section.qa") >= 1
        if route == "/accessibility/":
            out["report_path_discoverable"] = q("a[href$='/contact/']") >= 1
    return out


def find_link(pg, lang: str, nxt: str, carry: str = "") -> str | None:
    """A selector for a link to `nxt` the page itself offers, in preference order: the page object, the spine, the
    product bar, the footer. Returns None when the page offers none (a broken journey)."""
    target = f"/{lang}{nxt}"
    pg.evaluate("document.querySelectorAll('[data-jw]').forEach(e=>e.removeAttribute('data-jw'))")
    for scope in ("article.page-obj", "aside.spine", "#primary-nav", "footer", "body"):
        sel = f"{scope} a[href='{target}'], {scope} a[href^='{target}?'], {scope} a[href^='{target}#']" if not carry else f"{scope} a[href^='{target}?{carry}'], {scope} a[href*='{target}?'][href*='{carry}']"
        # the first link the reader can see at this width (a phone hides the side spine and the primary nav until opened)
        found = pg.evaluate("(s)=>{const all=[...document.querySelectorAll(s)];const vis=all.find(a=>a.offsetParent!==null)||all.find(a=>a.closest('#primary-nav'));if(!vis)return false;vis.setAttribute('data-jw','');return true}", sel)
        if found:
            return "[data-jw]"
    return None


def keyboard_follow(pg, sel: str, mobile: bool) -> dict:
    """Give the link keyboard focus and activate it with Enter (a phone's primary-nav link first opens the menu by
    keyboard). Focus must be visible (an outline) and the activation must navigate."""
    r = {}
    in_nav = pg.evaluate("(s)=>{const a=document.querySelector(s);return !!a&&!!a.closest('#primary-nav')}", sel)
    if in_nav and mobile:
        pg.focus("[data-menu]"); pg.keyboard.press("Enter"); pg.wait_for_timeout(120)
        r["menu_opened_by_keyboard"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded')==='true'")
    pg.focus(sel)
    r["focusable"] = pg.evaluate("(s)=>document.activeElement===document.querySelector(s)", sel)
    r["focus_visible"] = pg.evaluate("(s)=>{const a=document.querySelector(s);const cs=getComputedStyle(a);return cs.outlineStyle!=='none'&&parseFloat(cs.outlineWidth)>0}", sel)
    r["in_viewport"] = pg.evaluate("(s)=>{const b=document.querySelector(s).getBoundingClientRect();return b.width>0&&b.height>0&&b.bottom>0&&b.top<innerHeight}", sel)
    before = pg.url
    pg.keyboard.press("Enter"); pg.wait_for_load_state("load"); pg.wait_for_timeout(120)
    r["navigated"] = pg.url != before
    return r


def walk(pg, base: str, lang: str, mode: str, j: dict) -> tuple[bool, list]:
    path = j["path"]; steps = []
    mobile = mode == "mobile"
    pg.goto(f"{base}/{lang}{path[0]}", wait_until="load"); pg.wait_for_timeout(120)
    ok = True
    s0 = SUCCESS(pg, path[0]); steps.append({"route": path[0], "success": s0}); ok &= all(s0.values())
    for i in range(1, len(path)):
        nxt = path[i]
        carry = "record=" if (j["journey_id"] == "J10_CHALLENGE_CORRECTION" and nxt == "/contact/") else ""
        sel = find_link(pg, lang, nxt, carry)
        step = {"route": nxt, "link_offered": bool(sel)}
        if sel:
            step["keyboard"] = keyboard_follow(pg, sel, mobile)
            from urllib.parse import urlparse
            step["landed"] = urlparse(pg.url).path[len(f"/{lang}"):]
            step["landed_ok"] = step["landed"] == nxt
            if not step["landed_ok"]:
                pg.goto(f"{base}/{lang}{nxt}", wait_until="load")
            step["success"] = SUCCESS(pg, nxt)
            ok &= all(step["keyboard"].values()) and step["landed_ok"] and all(step["success"].values())
        else:
            ok = False
            pg.goto(f"{base}/{lang}{nxt}", wait_until="load")
        steps.append(step)
    return ok, steps


# ------------------------------------------------------------------------------------------------ technical states
TECH_VOICE = "(s)=>{const e=document.querySelector(s);if(!e)return false;const cs=getComputedStyle(e);return e.offsetParent!==null&&cs.borderTopStyle==='dashed'&&cs.borderTopStyle!=='double'}"
NAV_WORKS = "document.querySelectorAll('#primary-nav a').length>0 && document.querySelectorAll('#main').length===1"
NOT_EVIDENCE_GAP = "(s)=>{const e=document.querySelector(s);return !!e&&!e.closest('section.bnd')&&!e.querySelector('[data-lineage-state],[data-evidence-source-unavailable]')}"


def technical_states(pg, base: str, lang: str, ctx_factory) -> dict:
    out = {}
    def st(name, checks):
        out[name] = checks
    # Compare: wrong count, unknown id, malformed, duplicate, a real record outside the comparable set
    for name, query in (("compare_wrong_count", "records=CLM-001"), ("compare_unknown_id", "records=CLM-001,NOT-A-RECORD"), ("compare_malformed", "records=,,"),
                        ("compare_not_comparable_record", "records=CLM-001,CLM-003")):
        pg.goto(f"{base}/{lang}/evidence/compare/?{query}", wait_until="load"); pg.wait_for_timeout(250)
        err = pg.evaluate("(()=>{const e=document.querySelector('.compare-url-error');return e?{text:e.innerText.length>0,role:e.getAttribute('role')}:null})()")
        st(name, {"announced": bool(err) and err["text"] and err["role"] == "alert",
                  "technical_voice": bool(err) and pg.evaluate(TECH_VOICE, ".compare-url-error"),
                  "no_verdict": pg.evaluate("!document.querySelector('[data-compare-verdict]')"),
                  "not_evidence_gap": bool(err) and pg.evaluate(NOT_EVIDENCE_GAP, ".compare-url-error"),
                  "navigation_works": pg.evaluate(NAV_WORKS)})
    # the same record twice: a visible same-record state, never one of the four assessments, in the technical voice
    pg.goto(f"{base}/{lang}/evidence/compare/?records=CLM-001,CLM-001", wait_until="load"); pg.wait_for_timeout(250)
    st("compare_duplicate", {"same_record_state_visible": pg.evaluate("(()=>{const e=document.querySelector('[data-compare-verdict=\"same-record\"]');return !!e&&e.offsetParent!==null&&e.innerText.trim().length>0})()"),
                             "not_an_assessment": pg.evaluate("[...document.querySelectorAll('[data-compare-verdict]')].every(e=>e.getAttribute('data-compare-verdict')==='same-record')"),
                             "technical_voice": pg.evaluate(TECH_VOICE, "[data-compare-verdict=\"same-record\"]"),
                             "navigation_works": pg.evaluate(NAV_WORKS)})
    # Search: no match; index unavailable
    pg.goto(f"{base}/{lang}/evidence/", wait_until="load"); pg.fill("#global-search", "zzqqxxvv"); pg.wait_for_timeout(500)
    st("search_no_match", {"announced": pg.evaluate("[...document.querySelectorAll('[data-search-status]')].some(s=>s.innerText.trim().length>0)"),
                           "empty_state_is_technical_not_evidence": pg.evaluate("(()=>{const e=document.querySelector('#search-results .empty');return !!e&&!e.closest('section.bnd')})()"),
                           "technical_voice": pg.evaluate(TECH_VOICE, "#search-results .empty"),
                           "navigation_works": pg.evaluate(NAV_WORKS)})
    ctx = ctx_factory(); p2 = ctx.new_page()
    p2.route("**/static-data/search_index.json", lambda r: r.fulfill(status=503, body="unavailable"))
    p2.goto(f"{base}/{lang}/evidence/", wait_until="load"); p2.fill("#global-search", "remittances"); p2.wait_for_timeout(600)
    st("search_index_unavailable", {"announced": p2.evaluate("(()=>{const e=document.querySelector('#search-results .empty');return !!e&&e.innerText.trim().length>0})()"),
                                    "no_hits": p2.evaluate("document.querySelectorAll('#search-results .search-hit').length===0"),
                                    "technical_voice": p2.evaluate(TECH_VOICE, "#search-results .empty"),
                                    "navigation_works": p2.evaluate(NAV_WORKS)})
    ctx.close()
    # Sources: unknown deep link; filter with no match
    pg.goto(f"{base}/{lang}/data/?source=SRC-NOT-A-SOURCE#source-SRC-NOT-A-SOURCE", wait_until="load"); pg.wait_for_timeout(300)
    st("source_link_unknown", {"announced": pg.evaluate("(()=>{const e=document.querySelector('[data-source-link-error]');return !!e&&e.getAttribute('role')==='alert'&&e.innerText.trim().length>0})()"),
                               "every_source_visible": pg.evaluate("[...document.querySelectorAll('[data-source-record]')].length>0 && [...document.querySelectorAll('[data-source-record]')].every(r=>!r.hidden)"),
                               "technical_voice": pg.evaluate(TECH_VOICE, "[data-source-link-error]"),
                               "navigation_works": pg.evaluate(NAV_WORKS)})
    pg.goto(f"{base}/{lang}/data/", wait_until="load"); pg.fill("[data-source-filter]", "zzqqxxvv"); pg.wait_for_timeout(400)
    st("source_filter_no_match", {"announced": pg.evaluate("(()=>{const s=document.querySelector('[data-source-filter-status]');return !!s&&s.innerText.trim().length>0})()"),
                                  "no_match_is_not_absence": pg.evaluate("(()=>{const e=document.querySelector('[data-source-no-results]');return !!e&&!e.hidden&&e.offsetParent!==null&&!e.closest('section.bnd')})()"),
                                  "technical_voice": pg.evaluate(TECH_VOICE, "[data-source-no-results]"),
                                  "navigation_works": pg.evaluate(NAV_WORKS)})
    # Record context: unknown, malformed, valid
    pg.goto(f"{base}/{lang}/contact/?record=CLM-999", wait_until="load"); pg.wait_for_timeout(200)
    st("record_context_unknown", {"announced": pg.evaluate("(()=>{const e=document.querySelector('[data-correction-error]');return !!e&&!e.hidden&&e.getAttribute('data-correction-error')==='unknown'&&e.getAttribute('role')==='alert'})()"),
                                  "report_path_still_works": pg.evaluate("!!document.querySelector('[data-correction-context]') && document.querySelectorAll('a[href$=\"/corrections/\"]').length>0"),
                                  "technical_voice": pg.evaluate(TECH_VOICE, "[data-correction-error]"),
                                  "navigation_works": pg.evaluate(NAV_WORKS)})
    pg.goto(f"{base}/{lang}/corrections/?record=%3Cx%3E", wait_until="load"); pg.wait_for_timeout(200)
    st("record_context_malformed", {"announced": pg.evaluate("(()=>{const e=document.querySelector('[data-correction-error]');return !!e&&!e.hidden&&e.getAttribute('data-correction-error')==='malformed'})()"),
                                    "technical_voice": pg.evaluate(TECH_VOICE, "[data-correction-error]"),
                                    "navigation_works": pg.evaluate(NAV_WORKS)})
    pg.goto(f"{base}/{lang}/contact/?record=CLM-001", wait_until="load"); pg.wait_for_timeout(200)
    st("record_context_valid", {"record_carried": pg.evaluate("(()=>{const o=document.querySelector('[data-correction-origin]');return !!o&&!o.hidden&&/CLM-001/.test(o.innerText)})()"),
                                "mail_action": pg.evaluate("(()=>{const m=document.querySelector('[data-correction-mail]');return !!m&&!m.hidden&&/CLM-001/.test(m.getAttribute('href'))})()"),
                                "no_error_shown": pg.evaluate("(()=>{const e=document.querySelector('[data-correction-error]');return !e||e.hidden})()")})
    # Language switch keeps the comparison
    pg.goto(f"{base}/{lang}/evidence/compare/?records=CLM-001,CLM-010", wait_until="load"); pg.wait_for_timeout(300)
    pg.focus("[data-lang]"); pg.keyboard.press("Enter"); pg.wait_for_load_state("load"); pg.wait_for_timeout(300)
    other = "ar" if lang == "en" else "en"
    st("language_switch_state", {"same_route_other_edition": f"/{other}/evidence/compare/" in pg.url, "query_kept": "records=CLM-001,CLM-010" in pg.url,
                                 "comparison_kept": pg.evaluate("document.querySelectorAll('table.compare-table tbody tr').length>0")})
    # No JavaScript: the governed note, the evidence readable, the tools' shells honest
    ctx = ctx_factory(js=False); p3 = ctx.new_page()
    p3.goto(f"{base}/{lang}/evidence/CLM-001/", wait_until="load")
    st("no_javascript", {"governed_note_visible": p3.evaluate("(()=>{const n=document.querySelector('.noscript');return !!n&&n.offsetParent!==null&&n.innerText.trim().length>0})()"),
                         "technical_voice": p3.evaluate(TECH_VOICE, ".noscript"),
                         "evidence_readable": p3.evaluate("document.querySelectorAll('#q1,#q5,#q6').length===3"),
                         "navigation_works": p3.evaluate(NAV_WORKS)})
    ctx.close()
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
    ap.add_argument("--site", default=str(ROOT / "design" / "reference" / "out"))
    ap.add_argument("--only", default="")
    ap.add_argument("--evidence", default="")
    ap.add_argument("--no-states", action="store_true")
    args = ap.parse_args()
    site = Path(args.site)
    if not (site / "en" / "index.html").exists():
        print(f"site not built: {site}"); return 2
    from playwright.sync_api import sync_playwright
    httpd, base = serve(site)
    keys = [k for k in args.only.split(",") if k]
    journeys = [j for j in JOURNEYS if not keys or any(k in j["journey_id"] for k in keys)]
    results, failures = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for mode, (w, h) in WIDTHS.items():
            for lang in ("en", "ar"):
                ctx = b.new_context(viewport={"width": w, "height": h}, reduced_motion="reduce"); pg = ctx.new_page()
                for j in journeys:
                    ok, steps = walk(pg, base, lang, mode, j)
                    results.append({"journey": j["journey_id"], "lang": lang, "mode": mode, "ok": ok, "steps": steps})
                    if not ok:
                        failures.append({"journey": j["journey_id"], "lang": lang, "mode": mode,
                                         "steps": [{k: v for k, v in s.items() if k != "success" or not all(v.values())} for s in steps if not (s.get("link_offered", True) and all(s.get("keyboard", {"x": True}).values()) and s.get("landed_ok", True) and all(s.get("success", {}).values()))]})
                    if args.evidence and mode == "desktop":
                        evd = Path(args.evidence); evd.mkdir(parents=True, exist_ok=True)
                        pg.screenshot(path=str(evd / f"{j['journey_id']}-{lang}-end.png"))
                ctx.close()
        states = {}
        if not args.no_states:
            for lang in ("en", "ar"):
                ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page()
                def factory(js=True, _b=b):
                    return _b.new_context(viewport={"width": 1440, "height": 900}, java_script_enabled=js)
                states[lang] = technical_states(pg, base, lang, factory)
                for name, checks in states[lang].items():
                    if not all(checks.values()):
                        failures.append({"state": name, "lang": lang, "failed": [k for k, v in checks.items() if not v]})
                if args.evidence:
                    evd = Path(args.evidence); evd.mkdir(parents=True, exist_ok=True)
                    for name, url in (("compare_unknown_id", f"/{lang}/evidence/compare/?records=CLM-001,NOT-A-RECORD"), ("record_context_unknown", f"/{lang}/contact/?record=CLM-999")):
                        pg.goto(base + url, wait_until="load"); pg.wait_for_timeout(250); pg.screenshot(path=str(evd / f"state-{name}-{lang}.png"))
                ctx.close()
        b.close()
    httpd.shutdown()
    (site / "_review_journeys.json").write_text(json.dumps({"journeys": results, "states": states, "failures": failures}, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in results:
        flag = "" if r["ok"] else "  <-- FAILED"
        print(f"{r['mode']:7s} {r['lang']} {r['journey']:34s} {'ok' if r['ok'] else 'FAIL'}{flag}")
    for lang, st in states.items():
        for name, checks in st.items():
            print(f"state   {lang} {name:34s} {'ok' if all(checks.values()) else 'FAIL ' + str([k for k, v in checks.items() if not v])}")
    n_j = len(results); n_ok = sum(1 for r in results if r["ok"])
    n_s = sum(len(v) for v in states.values()); n_sok = sum(1 for v in states.values() for c in v.values() if all(c.values()))
    print(f"{n_j} journey walks ({len(journeys)} journeys × EN/AR × mobile/desktop), {n_ok} passed; {n_s} technical-state drives, {n_sok} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
