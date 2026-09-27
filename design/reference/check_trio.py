#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendered checks for the D1 reference implementation of the stress trio (the routes it builds), in both languages.

  python3 design/reference/check_trio.py [--site design/reference/out] [--shots]

Per route × language × width (320, 390, 640, 1440), the same conditions as audit/tranche_c/checks/viewport_acceptance.py
(no horizontal overflow, every image has alt, exactly one h1, the document dir matches the language, the first Tab lands
on the skip link, no element wider than the viewport outside a .table-wrap) plus the brief §19 hooks the trio must
carry, and an interaction smoke test with the baseline runtime: the search dialog opens from its button and closes on
Escape, the menu button toggles aria-expanded at 390 px and the first navigation link takes focus, the cite button
announces in #utility-status, and the boundary section is present before any interaction. With --shots, first-screen
and full-page screenshots go to <site>/_review/. Exit 1 on any failure. Proof for the record, not authority.
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
                        bad = [k for k, v in smoke.items() if not v]
                        row["smoke"] = smoke
                        if bad:
                            failures.append({"width": w, "lang": lang, "route": r, "smoke_failed": bad})
            ctx.close()
        b.close()
    httpd.shutdown()
    for row in rows:
        flag = "" if row["ok"] else f"  <-- over={row['over']} imgs={row['imgs']} h1={row['h1']} first={row['first_tab']} wide={row['wide']} inline={row['inline']} missing={row['missing_hooks']}"
        print(f"{row['width']:5d} {row['lang']} {row['route']:40s} height={row['height']:6d}{flag}")
    smokes = [r for r in rows if "smoke" in r]
    print(f"{len(rows)} renders checked; {sum(1 for r in rows if not r['ok'])} failed; {len(smokes)} interaction smoke tests, {sum(1 for r in smokes if all(r['smoke'].values()))} passed")
    (site / "_review_trio.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
