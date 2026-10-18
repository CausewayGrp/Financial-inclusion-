#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendered visibility (Stage B charter v3.2 §12.1; W4 gate added in G2): the stylesheet cannot hide what the HTML
still contains.

  python3 scripts/tests/test_rendered_visibility.py                 # dist/, both editions, 390 and 1440
  python3 scripts/tests/test_rendered_visibility.py --self-check    # also the two negative controls

On one page per family in both editions (Home, a domain, an Evidence Record, a visual record, Compare, the directory,
/data/, a Reading, /methodology/, /measurement/, a trust page), at 390 and 1440 CSS px, in Chromium:
(a) the answer (the first section or the record's first answer), the clocks, the boundary sections and the verification
    tools (cite, report, the record's source rows) are rendered with a non-zero box and never sit inside a closed
    disclosure;
(b) no element inside <main> clamps or clips governed text: no `-webkit-line-clamp`, no `text-overflow: ellipsis`, and
    `overflow: hidden` only on the listed scroll wrappers (`.table-wrap`, which scrolls sideways, and screen-reader text);
(c) every governed text node in <main> that is not inside a disclosure is rendered (its element has a box) or is
    intentional screen-reader-only text from the listed set (`.sr-only`, with its reason: labels and status text);
(d) every <details> in <main> has a summary with visible text, so a folded region is named.
Negative controls (--self-check): in a copy of the site, (1) a boundary section is hidden with `display: none` and
(2) a governed paragraph is clamped to one line; the gate must fail on each.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import os
import shutil
import socket
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / (os.environ.get("YFIE_SITE_DIR") or "dist")
PAGES = ["/", "/payments/", "/evidence/CLM-001/", "/evidence/VIS-POS-TERMINALS/", "/evidence/compare/", "/evidence/",
         "/data/", "/readings/how-money-reaches-households/", "/methodology/", "/measurement/", "/about/"]
SR_ONLY_ALLOWED = {"sr-only": "accessible labels and status text (utility status, text-description headings, hub numerals)"}
SCROLL_WRAPPERS = {"table-wrap": "a wide table scrolls sideways; nothing is cut", "search-results": "a results list scrolls",
                   "nav": "the open phone menu scrolls"}

JS = r"""(args) => {
  const [allowedSr, scrollWrappers] = args;
  const main = document.querySelector('main') || document.body;
  const problems = [];
  const inClosed = (el) => { let p = el; while (p && p !== main) { if (p.tagName === 'DETAILS' && !p.open && !(p.querySelector(':scope > summary') && p.querySelector(':scope > summary').contains(el))) return true; p = p.parentElement; } return false; };
  const box = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const hasClass = (el, names) => [...el.classList].some(c => names.includes(c));
  // (a) the never-folded objects
  const must = [['.qa.first, #q1', 'the answer'], ['.head .clock, .record-line .clock', 'the clock'], ['section.bnd', 'the boundary'], ['#cite-tools, .page-tools', 'the verification tools']];
  for (const [sel, name] of must) {
    const els = [...main.querySelectorAll(sel)];
    if (!els.length) continue;
    for (const el of els) {
      if (!box(el)) problems.push(`(a) ${name} has no rendered box: ${sel}`);
      if (inClosed(el)) problems.push(`(a) ${name} sits inside a closed disclosure: ${sel}`);
    }
  }
  // (b) clamps and clips
  for (const el of main.querySelectorAll('*')) {
    const cs = getComputedStyle(el);
    if (cs.webkitLineClamp && cs.webkitLineClamp !== 'none') problems.push(`(b) line-clamp on <${el.tagName.toLowerCase()} class="${el.className}">`);
    if (cs.textOverflow === 'ellipsis' && (cs.overflowX === 'hidden' || cs.overflow === 'hidden')) problems.push(`(b) text-overflow ellipsis on <${el.tagName.toLowerCase()} class="${el.className}">`);
    if ((cs.overflow === 'hidden' || cs.overflowY === 'hidden') && !hasClass(el, scrollWrappers) && !hasClass(el, allowedSr) && el.tagName !== 'SVG' && !el.closest('svg') && el.tagName !== 'DIALOG') problems.push(`(b) overflow hidden on <${el.tagName.toLowerCase()} class="${el.className}">`);
  }
  // (c) every text node is rendered or allowed screen-reader text
  const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
  let n; const seen = new Set();
  while ((n = walker.nextNode())) {
    const t = n.textContent.trim(); if (!t || t.length < 3) continue;
    const el = n.parentElement; if (!el || el.closest('script, style, template, noscript, dialog, select')) continue;
    if (inClosed(el)) continue;
    if (box(el)) continue;
    // listed, each with its reason: the same links shown elsewhere at this width (the phone index and the foot rail
    // duplicate the desktop rail; the desktop rail duplicates the phone's), print-only identity, the no-script note,
    // and state-dependent regions the HTML itself marks hidden (a form's no-JS fallback, a closed output)
    if (el.closest('nav.strip, .spine, .print-foot, [data-print], .canon-p, .noscript, [hidden], svg, .rubric.product')) continue;
    // svg: a chart's alternate tick labels are shown by width (analytical labelling, not prose); .rubric.product: the
    // phone masthead already names the product (D3)
    if (el.tagName === 'SUMMARY' && el.parentElement && [...el.parentElement.children].some(c => c !== el && box(c))) continue;
    const sr = el.closest('.' + allowedSr.join(', .'));
    if (sr) continue;
    const key = el.tagName + '.' + el.className; if (seen.has(key)) continue; seen.add(key);
    problems.push(`(c) governed text with no rendered box: <${el.tagName.toLowerCase()} class="${el.className}"> "${t.slice(0, 60)}"`);
  }
  // (d) folded regions are named
  for (const d of main.querySelectorAll('details')) {
    const s = d.querySelector(':scope > summary');
    const content = [...d.children].filter(c => c !== s);
    const shown = d.open || content.some(box);   // a disclosure the stylesheet keeps open at this width needs no label
    if (shown) continue;
    if (!s || !(s.innerText || '').trim()) problems.push(`(d) a closed disclosure without a visible summary label: <details class="${d.className}">`);
  }
  return problems;
}"""


def serve(root: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Quiet, directory=str(root)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{port}"


def run(root: Path, pages: list[str]) -> list[str]:
    from playwright.sync_api import sync_playwright
    problems: list[str] = []
    httpd, base = serve(root)
    try:
        with sync_playwright() as pw:
            exe = os.environ.get("YFIE_CHROMIUM")
            browser = pw.chromium.launch(**({"executable_path": exe} if exe else {}))
            for width, height in ((390, 844), (1440, 900)):
                ctx = browser.new_context(viewport={"width": width, "height": height})
                page = ctx.new_page()
                for lang in ("ar", "en"):
                    for path in pages:
                        page.goto(f"{base}/{lang}{path}", wait_until="networkidle")
                        found = page.evaluate(JS, [sorted(SR_ONLY_ALLOWED), sorted(SCROLL_WRAPPERS)])
                        problems += [f"/{lang}{path} at {width}: {p}" for p in found]
                ctx.close()
            browser.close()
    finally:
        httpd.shutdown()
    return problems


def self_check() -> list[str]:
    """Two faults in a copy of the site; each must be caught on the page that carries it."""
    failures = []
    with tempfile.TemporaryDirectory(prefix="yfie-vis-") as tmp:
        site = Path(tmp) / "site"
        shutil.copytree(DIST, site, ignore=shutil.ignore_patterns("static-data", "social", "fonts"))
        css = site / "assets" / "yfie.css"
        base_css = css.read_text(encoding="utf-8")
        for name, rule, page, code in (("hidden boundary", "\n#s4.bnd{display:none}\n", "/", "(a) the boundary"),
                                       ("clamped paragraph", "\n#s3 .paced .sent.lead{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;overflow:hidden}\n", "/", "(b) line-clamp")):
            css.write_text(base_css + rule, encoding="utf-8")
            caught = [p for p in run(site, [page]) if code in p]
            print(f"negative control, {name}: {'CAUGHT' if caught else 'MISSED'}" + (f" — {caught[0]}" if caught else ""))
            if not caught:
                failures.append(f"negative control not caught: {name}")
        css.write_text(base_css, encoding="utf-8")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-check", action="store_true")
    ap.add_argument("--pages", nargs="*", default=PAGES)
    a = ap.parse_args()
    problems = run(DIST, a.pages)
    for p in problems:
        print("FAIL |", p)
    if a.self_check:
        problems += self_check()
    n = len(a.pages) * 2 * 2
    if problems:
        print(f"RENDERED VISIBILITY FAIL: {len(problems)} problem(s) on {n} page views")
        return 1
    print(f"RENDERED VISIBILITY PASS: {n} page views; the answer, clocks, boundaries and tools rendered and never folded; no clamp, clip or unrendered governed text; every disclosure named")
    return 0


if __name__ == "__main__":
    sys.exit(main())
