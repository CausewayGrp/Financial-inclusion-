#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The site works without JavaScript where its no-JavaScript note says it does (R-05, independent review of 70398d1).

  python3 scripts/tests/test_no_javascript.py

The note every page prints when JavaScript is off (UI-NOSCRIPT-NOTE) says that Search, Compare and the copy and print
buttons need JavaScript, and that every other page, the menu and the language switch work without it. In Chromium with
JavaScript disabled, at 390 px (the phone header, where the navigation is folded behind the menu) in both editions,
on Home, a domain page, an Evidence Record, Compare and a trust page:
(a) the note is visible;
(b) the language switch is visible, and following it opens the same route in the other edition;
(c) the menu is visible, and following it brings the footer into view, with its links (About among them) visible;
(d) at 1440 px the language switch works the same way.
Negative control: in a copy of the site, one page's language switch is turned back into a button (the 70398d1
markup); (b) must fail on that page.
"""
from __future__ import annotations

import functools
import http.server
import os
import re
import shutil
import socket
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / (os.environ.get("YFIE_SITE_DIR") or "dist")
PAGES = ["/ar/", "/en/", "/ar/payments/", "/en/payments/", "/ar/evidence/CLM-002/", "/en/evidence/CLM-002/",
         "/ar/evidence/compare/", "/en/about/"]
NEGATIVE = "en/payments/index.html"


def serve(root: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Quiet, directory=str(root)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{port}"


def other(path: str) -> str:
    lang, rest = path[1:3], path[3:]
    return "/" + ("en" if lang == "ar" else "ar") + rest


def run(root: Path, pages: list[str]) -> list[str]:
    from playwright.sync_api import sync_playwright
    problems = []
    httpd, base = serve(root)
    try:
        with sync_playwright() as pw:
            exe = os.environ.get("YFIE_CHROMIUM")
            browser = pw.chromium.launch(**({"executable_path": exe} if exe else {}))
            for width in (390, 1440):
                ctx = browser.new_context(viewport={"width": width, "height": 844}, java_script_enabled=False)
                page = ctx.new_page()
                for path in (pages if width == 390 else pages[:2]):
                    where = f"{path} at {width} px"
                    page.goto(base + path)
                    if width == 390 and not page.locator(".noscript").first.is_visible():
                        problems.append(f"(a) {where}: the no-JavaScript note is not visible")
                    sw = page.locator("header .controls [data-lang]").first
                    if not sw.count() or not sw.is_visible():
                        problems.append(f"(b) {where}: no visible language switch")
                    else:
                        sw.click()
                        page.wait_for_load_state()
                        if not page.url.endswith(other(path)):
                            problems.append(f"(b) {where}: the language switch opened {page.url[len(base):]}, not {other(path)}")
                    if width == 390:
                        page.goto(base + path)
                        mn = page.locator("header .controls [data-menu]").first
                        if not mn.count() or not mn.is_visible():
                            problems.append(f"(c) {where}: no visible menu")
                        else:
                            mn.click()
                            page.wait_for_timeout(150)
                            about = page.locator("#site-footer a[href$='/about/']").first
                            if not page.url.endswith("#site-footer") or not about.count() or not about.is_visible() \
                                    or not about.is_visible() or not page.evaluate(
                                        "() => { const r = document.querySelector('#site-footer').getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0; }"):
                                problems.append(f"(c) {where}: the menu does not bring the footer navigation into view")
                ctx.close()
            browser.close()
    finally:
        httpd.shutdown()
    return problems


def main() -> int:
    if not (DIST / "en" / "index.html").exists():
        print("NO JAVASCRIPT: FAIL — build the site first (python3 scripts/build.py)")
        return 1
    problems = run(DIST, PAGES)
    with tempfile.TemporaryDirectory(prefix="yfie-nojs-") as tmp:
        copy = Path(tmp) / "site"
        shutil.copytree(DIST, copy)
        f = copy / NEGATIVE
        t = f.read_text(encoding="utf-8")
        t2 = re.sub(r'<a class="tbtn lang" href="[^"]*" hreflang="(\w+)"([^>]*)>(.*?)</a>',
                    r'<button type="button" class="tbtn lang"\2>\3</button>', t, count=1)
        if t2 == t:
            problems.append("negative control: the language switch link was not found in " + NEGATIVE)
        else:
            f.write_text(t2, encoding="utf-8")
            caught = [p for p in run(copy, ["/" + NEGATIVE[:-len("index.html")]]) if p.startswith("(b)")]
            if caught:
                print("negative control: a language switch that is a button again — caught")
            else:
                problems.append("negative control: a button language switch passed (b)")
    for p in problems:
        print("FAIL", p)
    print(f"NO JAVASCRIPT: {'PASS' if not problems else 'FAIL'} — {len(PAGES)} pages at 390 px and 2 at 1440 px with JavaScript off; "
          f"note, language switch and menu; {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
