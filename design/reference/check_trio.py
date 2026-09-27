#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendered checks for the D1 reference implementation of the stress trio (the routes it builds), in both languages.

  python3 design/reference/check_trio.py [--site design/reference/out] [--shots]

Per route × language × width (320, 390, 640, 1440), the same conditions as audit/tranche_c/checks/viewport_acceptance.py
(no horizontal overflow, every image has alt, exactly one h1, the document dir matches the language, the first Tab lands
on the skip link, no element wider than the viewport outside a .table-wrap) plus the brief §19 hooks the trio must
carry, and an interaction smoke test with the baseline runtime: the search dialog opens from its button and closes on
Escape, the menu button toggles aria-expanded at 390 px and the first navigation link takes focus, the cite button
announces in #utility-status, and the boundary section is present before any interaction — by pointer and again by
keyboard only (Tab, Enter, Escape). With --shots, first-screen and full-page screenshots go to <site>/_review/; with
--degraded, print (PNG and PDF), no-stylesheet/no-script/image-off renders and their text go to <site>/_review/degraded/
and are checked (the record's disclosure content prints; the h1 sits inside #main without styles); with --evidence DIR,
the committed PNG evidence (first screens at 390 and 1440 px, printed pages) is written to DIR. Exit 1 on any failure.
Proof for the record, not authority.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import socket
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTES = ["/", "/evidence/CLM-003/", "/readings/same-year-different-number/"]
WIDTHS = [320, 390, 640, 1440]
HOOKS = {
    "all": ["#main", "a.skip", "#primary-nav", "[data-search-open]", "[data-cite]", "[data-lang]", "[data-menu][aria-controls=primary-nav]",
            "#utility-status[role=status]", "dialog#search-dialog", "#global-search-dialog[data-search-input]", "[data-search-status]", "[data-search-results]",
            "script#yfie-ui[type='application/json']", "script[src='/assets/app.js']", "link[rel=stylesheet][href='/assets/yfie.css']", "footer nav", "img[alt]"],
    "/evidence/CLM-003/": ["meta[name=yfie-citation]", "meta[name=yfie-record-id]", "[data-evidence-boundary-first-load]", "#source", "[data-evidence-source] [data-source-cite][data-source-citation]",
                           "[data-evidence-source] a.source-locator[rel~=noopener]", "[data-record-id] .evidence-cite-button[data-cite]", "h2#q1, #q1 h2", "#q5", "#q7 details"],
    "/readings/same-year-different-number/": ["[data-reading-boundary]", "[data-reading-section]", "figure[data-visual-id='RV-CWR-001'][data-image-independent]", "figure .alt table.rvtab", "[data-reading-verify][data-reading-path-state]",
                                              "[data-path-record]", "[data-reading-related]", "figure svg.trk", "figure svg.rv2", "figure a.canon[dir=ltr]"],
    "/": ["#system", "[data-visual-id]", ".paced", ".compact.bound", "#s4.bnd", "ol.qlist"],
}


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
    ap.add_argument("--shots", action="store_true")
    ap.add_argument("--degraded", action="store_true", help="print, no-stylesheet, no-script and image-off renders into <site>/_review/degraded/")
    ap.add_argument("--evidence", default="", help="directory for the committed PNG evidence (first screens at 390 and 1440, printed pages)")
    args = ap.parse_args()
    site = Path(args.site)
    if not (site / "en" / "index.html").exists():
        print(f"site not built: {site}"); return 2
    shots = site / "_review"
    if args.shots:
        shots.mkdir(exist_ok=True)
    from playwright.sync_api import sync_playwright
    httpd, base = serve(site)
    failures, rows = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in WIDTHS:
            ctx = b.new_context(viewport={"width": w, "height": 844 if w < 700 else 900}, reduced_motion="reduce")
            ctx.grant_permissions(["clipboard-read", "clipboard-write"])   # the cite action writes the citation to the clipboard
            pg = ctx.new_page()
            for lang in ("en", "ar"):
                for r in ROUTES:
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
                      return {over,imgs,h1,dir,wide,inline,height:d.scrollHeight};
                    }""")
                    pg.keyboard.press("Tab")
                    first = pg.evaluate("document.activeElement && document.activeElement.className")
                    pg.evaluate("document.activeElement && document.activeElement.blur()")   # a pointer user has not tabbed
                    missing = [sel for sel in HOOKS["all"] + HOOKS.get(r, []) if pg.evaluate("(s)=>!!document.querySelector(s)", sel) is False]
                    ok = (res["over"] <= 1 and res["imgs"] == 0 and res["h1"] == 1 and first == "skip" and res["dir"] == ("rtl" if lang == "ar" else "ltr")
                          and not res["wide"] and res["inline"] == 0 and not missing)
                    row = {"width": w, "lang": lang, "route": r, **res, "first_tab": first, "missing_hooks": missing, "ok": ok}
                    rows.append(row)
                    if not ok:
                        failures.append(row)
                    if args.shots and w in (390, 1440):
                        tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}-{w}"
                        pg.screenshot(path=str(shots / f"{tag}.png"))
                        pg.screenshot(path=str(shots / f"{tag}-full.png"), full_page=True)
                    # interaction smoke test at 390 and 1440 (baseline runtime)
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
                            smoke["menu_visible"] = pg.evaluate("getComputedStyle(document.querySelector('#primary-nav')).display !== 'none'")
                            smoke["menu_first_focus"] = pg.evaluate("document.activeElement && document.activeElement.closest('#primary-nav') !== null")
                            pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
                            smoke["menu_closed"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded') === 'false'")
                        else:
                            smoke["nav_visible_desktop"] = pg.evaluate("getComputedStyle(document.querySelector('#primary-nav')).display !== 'none'")
                        pg.locator("[data-cite]:visible").first.click(); pg.wait_for_timeout(250)
                        smoke["cite_announced"] = pg.evaluate("document.querySelector('#utility-status').textContent.trim().length > 0")
                        if r == "/evidence/CLM-003/":
                            smoke["boundary_visible"] = pg.evaluate("(() => { const e=document.querySelector('[data-evidence-boundary-first-load]'); const r=e.getBoundingClientRect(); return r.height>0 && getComputedStyle(e).visibility!=='hidden'; })()")
                        # keyboard-only path: Tab to the search button, Enter opens, Escape closes; at 390 Tab to the menu button, Enter opens
                        pg.goto(url, wait_until="load"); pg.wait_for_timeout(120)
                        def tab_to(selector, limit=40):
                            for _ in range(limit):
                                pg.keyboard.press("Tab")
                                if pg.evaluate("(s)=>document.activeElement===document.querySelector(s)", selector):
                                    return True
                            return False
                        smoke["kb_search_reached"] = tab_to("[data-search-open]")
                        pg.keyboard.press("Enter"); pg.wait_for_timeout(150)
                        smoke["kb_dialog_open"] = pg.evaluate("document.querySelector('#search-dialog').open === true && document.activeElement.id === 'global-search-dialog'")
                        pg.keyboard.press("Escape"); pg.wait_for_timeout(150)
                        smoke["kb_dialog_closed"] = pg.evaluate("document.querySelector('#search-dialog').open === false")
                        if w == 390:
                            smoke["kb_menu_reached"] = tab_to("[data-menu]")
                            pg.keyboard.press("Enter"); pg.wait_for_timeout(150)
                            smoke["kb_menu_open"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded') === 'true'")
                            pg.keyboard.press("Escape"); pg.wait_for_timeout(150)
                            smoke["kb_menu_closed"] = pg.evaluate("document.querySelector('[data-menu]').getAttribute('aria-expanded') === 'false'")
                        smoke["focus_visible_rule"] = pg.evaluate("[...document.styleSheets].some(ss=>{try{return [...ss.cssRules].some(r=>r.selectorText&&r.selectorText.includes(':focus-visible'))}catch(e){return false}})")
                        bad = [k for k, v in smoke.items() if not v]
                        row["smoke"] = smoke
                        if bad:
                            failures.append({"width": w, "lang": lang, "route": r, "smoke_failed": bad})
            ctx.close()
        if args.degraded or args.evidence:
            deg = site / "_review" / "degraded"; deg.mkdir(parents=True, exist_ok=True)
            evd = Path(args.evidence) if args.evidence else None
            if evd:
                evd.mkdir(parents=True, exist_ok=True)
            for lang in ("en", "ar"):
                for r in ROUTES:
                    tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}"
                    url = f"{base}/{lang}{r}"
                    # print: the page as a printer composes it (A4 width), one PNG of the first page and the PDF (ignored dir)
                    ctx = b.new_context(viewport={"width": 794, "height": 1123}); pg = ctx.new_page()
                    pg.goto(url, wait_until="load"); pg.emulate_media(media="print"); pg.wait_for_timeout(150)
                    pg.screenshot(path=str(deg / f"{tag}-print.png"))
                    pg.pdf(path=str(deg / f"{tag}.pdf"), format="A4", print_background=False)
                    details_printed = pg.evaluate("(() => { const d=document.querySelector('details.more'); if(!d) return true; const p=d.querySelector('.qa p'); if(!p) return false; const r=p.getBoundingClientRect(); return r.height>0; })()")
                    if evd:
                        pg.screenshot(path=str(evd / f"{tag}-print.png"))
                    ctx.close()
                    # no stylesheet, no script, no images: meaning and order must survive
                    ctx = b.new_context(viewport={"width": 390, "height": 844}, java_script_enabled=False); pg = ctx.new_page()
                    pg.route("**/*.css", lambda rt: rt.abort()); pg.route("**/*.png", lambda rt: rt.abort())
                    pg.goto(url, wait_until="load"); pg.wait_for_timeout(100)
                    pg.screenshot(path=str(deg / f"{tag}-nocss-nojs-noimg.png"))
                    text = pg.evaluate("document.body.innerText")
                    (deg / f"{tag}-nocss.txt").write_text(text, encoding="utf-8")
                    order_ok = pg.evaluate("(() => { const h1=document.querySelector('h1'); const main=document.querySelector('#main'); return !!h1 && !!main && main.contains(h1); })()")
                    ctx.close()
                    rows.append({"width": "degraded", "lang": lang, "route": r, "height": 0, "over": 0, "imgs": 0, "h1": 1, "dir": "", "wide": [], "inline": 0, "first_tab": "skip", "missing_hooks": [],
                                 "ok": details_printed and order_ok, "degraded": {"details_printed": details_printed, "no_css_order_ok": order_ok}})
                    if not (details_printed and order_ok):
                        failures.append({"lang": lang, "route": r, "degraded_failed": [k for k, v in {"details_printed": details_printed, "no_css_order_ok": order_ok}.items() if not v]})
            if evd:
                for w in (390, 1440):
                    ctx = b.new_context(viewport={"width": w, "height": 844 if w < 700 else 900}); pg = ctx.new_page()
                    for lang in ("en", "ar"):
                        for r in ROUTES:
                            tag = f"{(r.strip('/').replace('/', '_') or 'home')}-{lang}-{w}"
                            pg.goto(f"{base}/{lang}{r}", wait_until="load"); pg.wait_for_timeout(120)
                            pg.screenshot(path=str(evd / f"{tag}.png"))
                    ctx.close()
        b.close()
    httpd.shutdown()
    for row in rows:
        if row["width"] == "degraded":
            print(f"degrad {row['lang']} {row['route']:40s} {row['degraded']}")
            continue
        flag = "" if row["ok"] else f"  <-- over={row['over']} imgs={row['imgs']} h1={row['h1']} first={row['first_tab']} wide={row['wide']} inline={row['inline']} missing={row['missing_hooks']}"
        print(f"{row['width']:5d} {row['lang']} {row['route']:40s} height={row['height']:6d}{flag}")
    smokes = [r for r in rows if "smoke" in r]
    main_rows = [r for r in rows if r["width"] != "degraded"]
    deg_rows = [r for r in rows if r["width"] == "degraded"]
    print(f"{len(main_rows)} renders checked; {sum(1 for r in main_rows if not r['ok'])} failed; {len(smokes)} interaction smoke tests (pointer and keyboard), {sum(1 for r in smokes if all(r['smoke'].values()))} passed"
          + (f"; {len(deg_rows)} degraded renders, {sum(1 for r in deg_rows if r['ok'])} ok" if deg_rows else ""))
    (site / "_review_trio.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
