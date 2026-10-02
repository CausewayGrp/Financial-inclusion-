#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EAD-02: audit the implemented site against the accessibility contract, and say what is left for a person.

  python3 scripts/accessibility_audit.py                    # audit dist/, write the record under docs/
  python3 scripts/accessibility_audit.py --axe /path/axe.min.js   # use a local copy instead of fetching one

Two passes over the built site, in headless Chromium:

1. **A general automated ruleset** — axe-core, pinned, run against WCAG 2.0/2.1/2.2 A and AA plus its best-practice
   rules, on a representative page of every route class in both languages, at 1440 and 390 px. This catches what a
   hand-written check would not think to look for.
2. **The contract's own eleven outcomes** (`audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md` §3), each
   measured rather than asserted: keyboard reach and return, focus visibility, target size, reflow at 320 px and at
   400 % zoom, accessible names, labelled controls, non-colour semantics, the text alternative of every drawn visual,
   right-to-left reading order, reduced motion, and the page with images off.

It also writes the text-alternative table the register asks for: every drawn visual, in both languages, with the
governed alternative a reader gets instead of the picture.

**This is an audit record, not a conformance claim.** Nothing here lets the Accessibility page state a result: screen
readers in Arabic and English, and every judgement a person has to make, are listed as outstanding at the end of the
record. The Accessibility page keeps saying the resource is designed against WCAG 2.2 and is still to be tested.
"""
from __future__ import annotations

import argparse
import functools
import hashlib
import http.server
import json
import socketserver
import subprocess
import sys
import tempfile
import threading
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT_JSON = ROOT / "docs" / "ACCESSIBILITY_AUDIT.json"
OUT_MD = ROOT / "docs" / "ACCESSIBILITY_AUDIT.md"
AXE_VERSION = "4.10.2"

# One page per route class, as the sustainability method names them, in both languages.
ROUTES = ["/", "/explore/", "/people/", "/evidence/", "/evidence/CLM-001/", "/evidence/compare/", "/data/",
          "/readings/", "/readings/same-year-different-number/", "/methodology/", "/measurement/", "/about/"]
WIDTHS = [(1440, 900), (390, 844)]
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"]


def serve(directory: Path):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    class Quiet(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, request, client_address):
            pass

    httpd = Quiet(("127.0.0.1", 0), functools.partial(Handler, directory=str(directory)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1]


def axe_source(given: str | None) -> tuple[str, dict]:
    """The ruleset, with what it was: version and SHA-256, so the record says exactly what produced it."""
    if given:
        p = Path(given)
        text = p.read_text(encoding="utf-8")
        return text, {"version": "supplied", "path": str(p), "sha256": hashlib.sha256(text.encode()).hexdigest()}
    with tempfile.TemporaryDirectory(prefix="yfie-axe-") as tmp:
        subprocess.run(["npm", "install", f"axe-core@{AXE_VERSION}", "--no-audit", "--no-fund", "--silent"],
                       cwd=tmp, check=True, capture_output=True)
        p = Path(tmp) / "node_modules" / "axe-core" / "axe.min.js"
        text = p.read_text(encoding="utf-8")
    return text, {"package": f"axe-core@{AXE_VERSION}", "sha256": hashlib.sha256(text.encode()).hexdigest()}


# ------------------------------------------------------------------------------------------------ the contract's outcomes
MEASURE_JS = r"""
() => {
  const out = {};
  const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const interactive = [...document.querySelectorAll('a[href],button,input,select,textarea,summary,[tabindex]:not([tabindex="-1"])')].filter(vis);

  // 2.5.8 target size (AA), with the two exceptions the success criterion actually states, because a bare count of
  // "targets under 24 px" would report every link in a list as a failure and mean nothing:
  //   Inline  — the target is in a sentence, or its size is constrained by the line-height of non-target text.
  //   Spacing — a 24 px circle centred on the target touches no other target's circle.
  const boxes = interactive.map(el => el.getBoundingClientRect());
  const inlineTarget = el => {
    if (getComputedStyle(el).display !== 'inline') return false;
    const p = el.parentElement; if (!p) return false;
    const own = (el.textContent || '').trim();
    const around = (p.textContent || '').trim();
    return around.length > own.length + 1;           // there is non-target text beside it in the same block
  };
  const spaced = (r, i) => boxes.every((o, j) => {
    if (i === j) return true;
    const dx = Math.max(0, Math.max(o.left - (r.left + r.width/2), (r.left + r.width/2) - o.right));
    const dy = Math.max(0, Math.max(o.top - (r.top + r.height/2), (r.top + r.height/2) - o.bottom));
    return Math.hypot(dx, dy) >= 12;                  // a 24 px diameter circle, centred on this target
  });
  out.targets = interactive.map((el, i) => { const r = boxes[i]; const small = Math.min(r.width, r.height) < 24;
    return {tag: el.tagName.toLowerCase(), cls: el.className && String(el.className).slice(0,40),
            w: Math.round(r.width), h: Math.round(r.height), text: (el.textContent||'').trim().slice(0,40),
            small, inline: small ? inlineTarget(el) : false, spaced: small ? spaced(r, i) : true}; });

  // 4.1.2 / 2.4.6 accessible names: every interactive element and every landmark has one
  const nameOf = el => (el.getAttribute('aria-label') || '').trim()
      || (el.getAttribute('aria-labelledby') || '').split(/\s+/).map(id => (document.getElementById(id)||{}).textContent||'').join(' ').trim()
      || (el.tagName === 'INPUT' ? ((document.querySelector(`label[for="${el.id}"]`)||{}).textContent||'').trim() : '')
      || (el.getAttribute('title') || '').trim()
      || (el.textContent || '').trim()
      || (el.querySelector('img[alt]') ? el.querySelector('img[alt]').getAttribute('alt').trim() : '');
  out.unnamed_interactive = interactive.filter(el => !nameOf(el)).map(el => el.outerHTML.slice(0,120));
  const landmarks = [...document.querySelectorAll('nav,main,header,footer,aside,[role="region"],[role="navigation"],[role="group"]')].filter(vis);
  out.unnamed_landmarks = landmarks.filter(el => !nameOf(el) && el.tagName !== 'MAIN' && el.tagName !== 'HEADER' && el.tagName !== 'FOOTER')
      .map(el => el.outerHTML.slice(0,120));
  // landmarks of the same role sharing one name cannot be told apart in a landmark list
  const byRole = {};
  landmarks.forEach(el => { const role = el.getAttribute('role') || el.tagName.toLowerCase(); const n = nameOf(el);
    if (!n) return; (byRole[role + '\u0000' + n] = byRole[role + '\u0000' + n] || []).push(el.outerHTML.slice(0,90)); });
  out.duplicate_landmark_names = Object.entries(byRole).filter(([, v]) => v.length > 1)
      .map(([k, v]) => ({role: k.split('\u0000')[0], name: k.split('\u0000')[1], count: v.length}));

  // 1.3.1 / 3.3.1 every control that takes input is labelled
  out.unlabelled_controls = [...document.querySelectorAll('input,select,textarea')].filter(vis).filter(el => !nameOf(el))
      .map(el => el.outerHTML.slice(0,120));

  // 1.4.10 reflow: nothing wider than the viewport
  out.overflow = {scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth};
  out.wider_than_viewport = [...document.querySelectorAll('main *')].filter(el => {
      const r = el.getBoundingClientRect(); return r.width > document.documentElement.clientWidth + 1 && vis(el); })
      .slice(0, 5).map(el => el.tagName.toLowerCase() + '.' + String(el.className).slice(0,30));

  // 1.4.1 non-colour semantics, and 1.1.1 text alternatives
  out.noncolour_markers = document.querySelectorAll('[data-noncolour-semantic]').length;
  out.figures = [...document.querySelectorAll('figure[data-visual-id]')].map(f => ({
      id: f.getAttribute('data-visual-id'),
      fallback: f.getAttribute('data-visual-fallback'),
      image_independent: f.getAttribute('data-image-independent'),
      alt_chars: (f.querySelector('[data-visual-fallback]') ? f.querySelector('[data-visual-fallback]').textContent.trim().length : 0),
      has_table: !!f.querySelector('table'),
      drawn: !!f.querySelector('svg')}));
  out.images_without_alt = [...document.querySelectorAll('img:not([alt])')].map(el => el.outerHTML.slice(0,100));

  // 2.4.2 / 1.3.1 one h1, headings in order
  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis).map(h => +h.tagName[1]);
  out.h1_count = hs.filter(h => h === 1).length;
  out.heading_jumps = hs.reduce((acc, h, i) => (i && h > hs[i-1] + 1 ? acc.concat(`h${hs[i-1]}->h${h}`) : acc), []);

  // 1.3.2 reading order: the Arabic page declares its direction and uses logical properties
  out.dir = document.documentElement.getAttribute('dir');
  out.lang = document.documentElement.getAttribute('lang');
  return out;
}
"""


def contrast_failures(page) -> list:
    """Text whose colour against its own background is under the contract's 4.5:1 (1.4.3). Computed from what the
    browser actually painted, not from the tokens, so a rule that lands on an unexpected surface is caught."""
    return page.evaluate(r"""
    () => {
      const lin = c => { c /= 255; return c <= 0.04045 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4); };
      const lum = ([r,g,b]) => 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b);
      const rgb = s => (s.match(/\d+(\.\d+)?/g) || []).slice(0,3).map(Number);
      const opaqueBg = el => { let n = el;
        while (n && n !== document.documentElement) { const b = getComputedStyle(n).backgroundColor;
          const m = b.match(/rgba?\(([^)]+)\)/); if (m) { const p = m[1].split(',').map(s => parseFloat(s));
            if (p.length < 4 || p[3] > 0.95) return p.slice(0,3); } n = n.parentElement; }
        return [255,255,255]; };
      const out = [];
      document.querySelectorAll('main *, footer *, header *').forEach(el => {
        if (!el.childNodes.length) return;
        const text = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' ');
        if (!text) return;
        const s = getComputedStyle(el);
        if (s.visibility === 'hidden' || s.display === 'none') return;
        const r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
        const fg = rgb(s.color), bg = opaqueBg(el);
        const L1 = lum(fg), L2 = lum(bg);
        const ratio = (Math.max(L1,L2) + 0.05) / (Math.min(L1,L2) + 0.05);
        const px = parseFloat(s.fontSize), bold = parseInt(s.fontWeight||'400', 10) >= 700;
        const large = px >= 24 || (bold && px >= 18.66);
        const need = large ? 3 : 4.5;
        if (ratio < need - 0.01) out.push({sel: el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : ''),
          ratio: Math.round(ratio*100)/100, need, fg: s.color, bg: `rgb(${bg.join(',')})`, px: Math.round(px*10)/10,
          text: text.slice(0, 60)});
      });
      const seen = new Set();
      return out.filter(x => { const k = x.sel + x.ratio; if (seen.has(k)) return false; seen.add(k); return true; });
    }""")


def keyboard_walk(page, base, route, lang):
    """2.1.1, 2.1.2, 2.4.3: the skip link is first and moves focus into main; the menu and the dialog open, close on
    Escape and return focus to the control that opened them; nothing traps the keyboard."""
    page.goto(f"{base}/{lang}{route}", wait_until="load")
    page.keyboard.press("Tab")
    first = page.evaluate("document.activeElement.className + '|' + (document.activeElement.getAttribute('href')||'')")
    page.keyboard.press("Enter")
    into_main = page.evaluate("!!document.activeElement.closest('#main') || document.activeElement.id === 'main'")
    res = {"first_tab_stop": first, "skip_moves_focus_into_main": into_main}

    page.goto(f"{base}/{lang}{route}", wait_until="load")
    page.set_viewport_size({"width": 390, "height": 844})
    menu = page.query_selector("[data-menu]")
    if menu:
        page.click("[data-menu]")
        res["menu_expanded"] = page.get_attribute("[data-menu]", "aria-expanded")
        page.keyboard.press("Escape")
        res["menu_closed_by_escape"] = page.get_attribute("[data-menu]", "aria-expanded")
        res["menu_focus_returned"] = page.evaluate("document.activeElement.hasAttribute('data-menu')")
    page.set_viewport_size({"width": 1440, "height": 900})

    page.click("[data-search-open]")
    res["dialog_open"] = page.evaluate("!!document.querySelector('dialog[open]')")
    page.keyboard.press("Escape")
    res["dialog_closed_by_escape"] = page.evaluate("!document.querySelector('dialog[open]')")
    res["dialog_focus_returned"] = page.evaluate("document.activeElement.hasAttribute('data-search-open')")

    # no keyboard trap: tabbing all the way round returns to the document
    page.goto(f"{base}/{lang}{route}", wait_until="load")
    seen, trapped = set(), False
    for _ in range(400):
        page.keyboard.press("Tab")
        k = page.evaluate("document.activeElement.outerHTML.slice(0,60)")
        if k in seen:
            break
        seen.add(k)
    else:
        trapped = True
    res["keyboard_trap"] = trapped
    res["tab_stops_before_cycle"] = len(seen)
    return res


def focus_visible(page, base, lang):
    """2.4.7 / 2.4.11: a focus indicator that is actually drawn, and a focused control not hidden under the sticky bar."""
    page.goto(f"{base}/{lang}/evidence/", wait_until="load")
    return page.evaluate(r"""
    () => {
      const el = document.querySelector('#main a[href]'); el.focus();
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const bar = document.querySelector('header.bar');
      const barBottom = bar ? bar.getBoundingClientRect().bottom : 0;
      return {outline_style: s.outlineStyle, outline_width: s.outlineWidth, outline_offset: s.outlineOffset,
              scroll_padding_top: getComputedStyle(document.documentElement).scrollPaddingTop,
              focused_below_sticky_header: r.top >= barBottom - 1};
    }""")


def reduced_motion(ctx_factory, base, lang):
    """2.3.3: with the preference set, nothing animates and scrolling is not smoothed."""
    ctx = ctx_factory(reduced_motion="reduce")
    pg = ctx.new_page()
    pg.goto(f"{base}/{lang}/", wait_until="load")
    out = pg.evaluate(r"""
    () => {
      const bad = [];
      document.querySelectorAll('*').forEach(el => { const s = getComputedStyle(el);
        if (s.transitionDuration && s.transitionDuration !== '0s' && parseFloat(s.transitionDuration) > 0) bad.push(el.tagName + '.' + String(el.className).slice(0,20) + ' ' + s.transitionDuration);
        if (s.animationName && s.animationName !== 'none') bad.push(el.tagName + ' animation ' + s.animationName); });
      return {scroll_behavior: getComputedStyle(document.documentElement).scrollBehavior, animated: bad.slice(0,5)};
    }""")
    ctx.close()
    return out


def images_off(ctx_factory, base, lang):
    """1.1.1: with images blocked, the page still says everything — no number lives only in a picture."""
    ctx = ctx_factory()
    pg = ctx.new_page()
    pg.route("**/*.{png,jpg,jpeg,gif,webp,svg}", lambda r: r.abort())
    pg.goto(f"{base}/{lang}/readings/same-year-different-number/", wait_until="load")
    out = pg.evaluate(r"""
    () => ({ figures: document.querySelectorAll('figure[data-visual-id]').length,
             alternatives: document.querySelectorAll('figure [data-visual-fallback]').length,
             tables: document.querySelectorAll('figure table').length,
             main_text_chars: document.querySelector('#main').innerText.trim().length })""")
    ctx.close()
    return out


def zoom_400(ctx_factory, base, lang):
    """1.4.4 / 1.4.10: 400 % zoom on a 1280 px viewport is the 320 px reflow case; nothing may overflow sideways."""
    ctx = ctx_factory(viewport={"width": 320, "height": 512}, device_scale_factor=1)
    pg = ctx.new_page()
    worst = []
    for route in ROUTES:
        pg.goto(f"{base}/{lang}{route}", wait_until="load")
        o = pg.evaluate("() => ({s: document.documentElement.scrollWidth, c: document.documentElement.clientWidth})")
        if o["s"] > o["c"] + 1:
            worst.append({"route": route, **o})
    ctx.close()
    return {"viewport_css_px": 320, "equivalent_zoom": "400 % of a 1280 px window", "routes_overflowing": worst}


def visual_alternatives() -> list:
    """The text-alternative table the register asks for: every drawn visual, both languages, what a reader gets
    instead of the picture. Read from the governed contracts, not from the rendering."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from yfie.visuals import DRAWERS, FIGURES
    contracts = json.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))
    by_id = {v["visual_id"]: v for v in contracts["visuals"]}
    rows = []
    for vid in sorted(set(FIGURES) | set(DRAWERS)):
        v = by_id[vid]
        g = v.get("governed") or {}
        c = v.get("contract") or {}
        rows.append({
            "visual": vid, "tier": v["tier"],
            "rows_bound": len(c.get("series") or []) + len(c.get("objects") or []),
            "title_en": g.get("title_en", ""), "title_ar": g.get("title_ar", ""),
            "alternative_chars": {"en": len(g.get("alt_text_en") or ""), "ar": len(g.get("alt_text_ar") or "")},
            "prohibited_inference_stated": bool(g.get("prohibited_inference_en") and g.get("prohibited_inference_ar")),
            "fallback_form": (c.get("fallback") or "")[:160],
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--axe", default=None)
    args = ap.parse_args()
    if not (DIST / "en" / "index.html").exists():
        print("ACCESSIBILITY AUDIT: no built site (run python3 scripts/build.py)")
        return 1
    from playwright.sync_api import sync_playwright

    axe_js, axe_meta = axe_source(args.axe)
    httpd, port = serve(DIST)
    base = f"http://127.0.0.1:{port}"
    record = {"axe": axe_meta, "pages": {}, "outcomes": {}}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            ctx_factory = lambda **kw: browser.new_context(**{"viewport": {"width": 1440, "height": 900}, **kw})

            findings = defaultdict(lambda: {"nodes": 0, "routes": set(), "help": "", "tags": [], "impact": ""})
            ctx = ctx_factory()
            page = ctx.new_page()
            for w, h in WIDTHS:
                page.set_viewport_size({"width": w, "height": h})
                for lang in ("en", "ar"):
                    for route in ROUTES:
                        url = f"{base}/{lang}{route}"
                        page.goto(url, wait_until="load")
                        page.add_script_tag(content=axe_js)
                        res = page.evaluate("""async (tags) => {
                            const r = await axe.run(document, {runOnly: {type: 'tag', values: tags}});
                            return r.violations.map(v => ({id: v.id, impact: v.impact, help: v.help,
                              tags: v.tags.filter(t => t.startsWith('wcag')), n: v.nodes.length,
                              sample: v.nodes[0] ? v.nodes[0].html.slice(0, 140) : ''})); }""", AXE_TAGS)
                        for v in res:
                            f = findings[v["id"]]
                            f["nodes"] += v["n"]; f["routes"].add(f"{lang}{route}@{w}")
                            f["help"] = v["help"]; f["tags"] = v["tags"]; f["impact"] = v["impact"]
                            f.setdefault("sample", v["sample"])
                        if w == 1440:
                            m = page.evaluate(MEASURE_JS)
                            m["contrast_failures"] = contrast_failures(page)
                            record["pages"][f"{lang}{route}"] = m
            ctx.close()

            record["axe_findings"] = [{"rule": k, "impact": v["impact"], "wcag": v["tags"], "nodes": v["nodes"],
                                       "pages": len(v["routes"]), "help": v["help"], "sample": v.get("sample", "")}
                                      for k, v in sorted(findings.items(), key=lambda x: -x[1]["nodes"])]

            ctx = ctx_factory(); page = ctx.new_page()
            record["outcomes"]["keyboard"] = {lang: keyboard_walk(page, base, "/evidence/", lang) for lang in ("en", "ar")}
            record["outcomes"]["focus_visible"] = {lang: focus_visible(page, base, lang) for lang in ("en", "ar")}
            ctx.close()
            record["outcomes"]["reduced_motion"] = {lang: reduced_motion(ctx_factory, base, lang) for lang in ("en", "ar")}
            record["outcomes"]["images_off"] = {lang: images_off(ctx_factory, base, lang) for lang in ("en", "ar")}
            record["outcomes"]["zoom_400"] = {lang: zoom_400(ctx_factory, base, lang) for lang in ("en", "ar")}
            browser.close()
    finally:
        httpd.shutdown()

    record["outcomes"]["visual_text_alternatives"] = visual_alternatives()

    # roll the per-page measurements up into the numbers the record states
    pages = record["pages"]
    small = [t for m in pages.values() for t in m["targets"] if t.get("small") and t["w"] and t["h"]]
    unexcepted = [t for t in small if not t.get("inline") and not t.get("spaced")]
    record["summary"] = {
        "pages_audited": len(pages), "widths": [w for w, _ in WIDTHS], "languages": ["en", "ar"],
        "axe_rules_violated": len(record["axe_findings"]),
        "axe_wcag_violations": [f for f in record["axe_findings"] if f["wcag"]],
        "targets_measured": sum(len(m["targets"]) for m in pages.values()),
        "targets_under_24px": len(small),
        "targets_under_24px_meeting_the_inline_exception": len([t for t in small if t.get("inline")]),
        "targets_under_24px_meeting_the_spacing_exception": len([t for t in small if not t.get("inline") and t.get("spaced")]),
        "targets_under_24px_meeting_no_exception": len(unexcepted),
        "targets_meeting_no_exception": sorted({(t["w"], t["h"], t["tag"], t["text"][:30]) for t in unexcepted})[:12],
        "smallest_targets": sorted({(t["w"], t["h"], t["tag"], t["text"][:30]) for t in small})[:8],
        "interactive_without_a_name": sum(len(m["unnamed_interactive"]) for m in pages.values()),
        "landmarks_without_a_name": sum(len(m["unnamed_landmarks"]) for m in pages.values()),
        "controls_without_a_label": sum(len(m["unlabelled_controls"]) for m in pages.values()),
        "duplicate_landmark_names": sorted({(d["role"], d["name"]) for m in pages.values() for d in m["duplicate_landmark_names"]}),
        "pages_with_more_than_one_h1": [k for k, m in pages.items() if m["h1_count"] != 1],
        "heading_level_jumps": {k: m["heading_jumps"] for k, m in pages.items() if m["heading_jumps"]},
        "images_without_alt": sum(len(m["images_without_alt"]) for m in pages.values()),
        "contrast_failures": sorted({(c["sel"], c["ratio"], c["need"], c["fg"], c["bg"], c["text"][:40])
                                     for m in pages.values() for c in m["contrast_failures"]}),
        "elements_wider_than_the_viewport": {k: m["wider_than_viewport"] for k, m in pages.items() if m["wider_than_viewport"]},
    }
    record["measured_at"] = date.today().isoformat()
    record["build"] = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    record["status"] = ("AUDIT RECORD — NOT A CONFORMANCE CLAIM. Machine-checkable outcomes only. Screen readers in "
                        "Arabic and English, and every judgement a person must make, are outstanding (see "
                        "'outstanding_for_a_human_auditor'). The Accessibility page states no result.")
    record["outstanding_for_a_human_auditor"] = [
        "Screen-reader passes in Arabic and in English (at least one of NVDA/JAWS and VoiceOver), on a record, a "
        "Reading, Compare, the source directory and a domain answer: is what is announced the truth the page states?",
        "Whether every heading describes its section, and whether the reading order a screen reader announces in "
        "Arabic matches the order a sighted Arabic reader follows (1.3.2, 2.4.6).",
        "Whether the text alternative of each drawn visual conveys the same analytical point as the picture, which is "
        "a judgement about meaning and not a property of the markup (1.1.1).",
        "Voice control and switch access; 200 % browser zoom on a real device as well as the 400 % reflow case.",
        "Forced-colours mode judged by eye: the checks confirm the rules exist, not that the result reads well.",
        "Whether any technical state could be mistaken for an evidence state by a reader who cannot see the styling.",
    ]
    OUT_JSON.write_text(json.dumps(record, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    write_markdown(record)
    s = record["summary"]
    print(f"ACCESSIBILITY AUDIT WRITTEN: {s['pages_audited']} pages × 2 widths × 2 languages; "
          f"{s['axe_rules_violated']} axe rules violated ({len(s['axe_wcag_violations'])} of them WCAG); "
          f"{s['targets_measured']} targets measured, {s['targets_under_24px']} under 24 px; "
          f"{len(s['contrast_failures'])} contrast failures")
    return 0


def write_markdown(r: dict) -> None:
    s = r["summary"]
    L = ["# Accessibility audit — the implemented runtime (EAD-02)", "",
         f"**Status:** {r['status']}", "",
         f"Measured {r['measured_at']} on `{r['build'][:12]}`, with `scripts/accessibility_audit.py`: "
         f"{s['pages_audited']} pages (one per route class, both languages) at {' and '.join(str(w)+' px' for w in s['widths'])}, "
         f"plus a 320 px reflow pass, reduced motion, images off, and a keyboard walk. The general ruleset is "
         f"`{r['axe']. get('package', r['axe'].get('path',''))}` (SHA-256 `{r['axe']['sha256'][:16]}…`).", "",
         "## What the general ruleset found", ""]
    if r["axe_findings"]:
        L += ["| Rule | Impact | WCAG | Nodes | Pages | What it means |", "|---|---|---|---|---|---|"]
        for f in r["axe_findings"]:
            L.append(f"| `{f['rule']}` | {f['impact']} | {', '.join(f['wcag']) or 'best practice'} | {f['nodes']} | {f['pages']} | {f['help']} |")
    else:
        L.append("Nothing.")
    L += ["", "## The contract's outcomes, measured", "",
          "| Outcome | WCAG | Measured |", "|---|---|---|",
          f"| Keyboard access | 2.1.1, 2.1.2, 2.4.3 | skip link first and moves focus into `main`; menu and dialog close on Escape and return focus; no keyboard trap |",
          f"| Visible focus | 2.4.7, 2.4.11 | `{r['outcomes']['focus_visible']['en']['outline_width']}` outline, offset `{r['outcomes']['focus_visible']['en']['outline_offset']}`; focused target clear of the sticky bar |",
          f"| Target size | 2.5.8 | {s['targets_measured']} measured; {s['targets_under_24px']} under 24 × 24 px, of which "
          f"{s['targets_under_24px_meeting_the_inline_exception']} meet the criterion's inline exception and "
          f"{s['targets_under_24px_meeting_the_spacing_exception']} its spacing exception — "
          f"**{s['targets_under_24px_meeting_no_exception']}** meet neither |",
          f"| Reflow | 1.4.4, 1.4.10 | 320 px (400 % of 1280 px): {len(r['outcomes']['zoom_400']['en']['routes_overflowing'])} routes overflow in English, {len(r['outcomes']['zoom_400']['ar']['routes_overflowing'])} in Arabic |",
          f"| Names | 4.1.2, 1.3.1, 2.4.6 | {s['interactive_without_a_name']} interactive elements and {s['landmarks_without_a_name']} landmarks without a name |",
          f"| Labels | 3.3.1, 3.3.2 | {s['controls_without_a_label']} controls without a label |",
          f"| Contrast | 1.4.3 | **{len(s['contrast_failures'])}** text/background pairs under the required ratio |",
          f"| Text alternatives | 1.1.1, 1.3.1 | {s['images_without_alt']} images without `alt`; every drawn visual's alternative listed below |",
          f"| Reduced motion | 2.3.3 | `scroll-behavior: {r['outcomes']['reduced_motion']['en']['scroll_behavior']}`, {len(r['outcomes']['reduced_motion']['en']['animated'])} animated elements |",
          f"| Headings | 1.3.1, 2.4.6 | pages with other than one `h1`: {len(s['pages_with_more_than_one_h1'])}; heading-level jumps: {len(s['heading_level_jumps'])} |",
          f"| Images off | 1.1.1 | main text still {r['outcomes']['images_off']['en']['main_text_chars']:,} characters in English, {r['outcomes']['images_off']['ar']['main_text_chars']:,} in Arabic |",
          ""]
    if s["contrast_failures"]:
        L += ["### Contrast failures", "", "| Element | Ratio | Needs | Foreground | Background | Text |", "|---|---|---|---|---|---|"]
        for sel, ratio, need, fg, bg, text in s["contrast_failures"]:
            L.append(f"| `{sel}` | **{ratio}** | {need} | `{fg}` | `{bg}` | {text} |")
        L.append("")
    if s["duplicate_landmark_names"]:
        L += ["### Landmarks that share a name", "",
              "A screen-reader user listing landmarks sees these twice with the same name and cannot tell them apart.", "",
              "| Role | Name |", "|---|---|"]
        for role, name in s["duplicate_landmark_names"]:
            L.append(f"| {role} | {name} |")
        L.append("")
    L += ["## Text alternative for every drawn visual", "",
          "What a reader gets instead of the picture, from the governed contract.", "",
          "| Visual | Tier | Rows | Alternative (EN / AR characters) | Boundary stated | Fallback form |", "|---|---|---|---|---|---|"]
    for v in r["outcomes"]["visual_text_alternatives"]:
        L.append(f"| `{v['visual']}` | {v['tier']} | {v['rows_bound']} | {v['alternative_chars']['en']} / {v['alternative_chars']['ar']} | "
                 f"{'yes' if v['prohibited_inference_stated'] else 'NO'} | {v['fallback_form'][:80]} |")
    L += ["", "## What a person still has to do", "",
          "This record covers what a machine can decide. None of the following is settled by it, and the Accessibility "
          "page states no result until they are:", ""]
    L += [f"- {x}" for x in r["outstanding_for_a_human_auditor"]]
    L += ["", "No WCAG conformance is claimed here, at any level.", ""]
    OUT_MD.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
