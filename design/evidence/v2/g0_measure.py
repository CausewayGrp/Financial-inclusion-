#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stage B G0 baseline measurement (BRIEF W4 G0; takeover brief Part 5 row B0; owner directive 17 Oct 2026 §9).

  python3 design/evidence/v2/g0_measure.py --out design/evidence/v2/g0 --shots SCRATCH_DIR [--site dist] [--label g0]

Measures the built site exactly as a reader's browser receives it (Chromium via Playwright; gzip served as
`dist/_headers` declares, as scripts/performance_budget.py does), in both languages, at 320, 390, 768 and 1440 CSS px:

  per page and width   screens (scrollHeight / viewport height); horizontal overflow; H1 line count; TOC entries
                       (nav.strip links) and whether the strip overflows sideways; ISO dates visible in the text;
                       interactive targets under 24 px; visible words; first-screen proxies for charter P1
                       (figure .fnum, clock .clock, boundary [data-boundary-part] or .bound, evidence link, source link
                       inside the first viewport) and the first-screen word count
  per page (390)       cold transfer bytes on the wire by type, font files loaded, requests
  states               screenshots of the interaction states the brief lists, on the proving pages only
  journeys             shortest click paths (link graph of the built HTML, main + header links) from Home to the
                       objects the six personas and the first-visit journeys need

Numbers are reproducible from the committed site; screenshots go to a scratch directory and only the decision set is
copied into the repository. Automated timings are never reported as human reading or comprehension time.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import OrderedDict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))

LANGS = ("ar", "en")
WIDTHS = (320, 390, 768, 1440)
HEIGHT = {320: 568, 390: 844, 768: 1024, 1440: 900}

# One row per page family plus the Part 2 scoreboard rows and every domain.
ROUTES = ["/", "/explore/", "/people/", "/payments/", "/remittances/", "/firms/", "/finance/", "/providers/", "/access/",
          "/reforms/", "/evidence/", "/evidence/CLM-001/", "/evidence/CLM-003/", "/evidence/VIS-POS-TERMINALS/",
          "/evidence/compare/", "/readings/", "/readings/how-money-reaches-households/", "/data/", "/methodology/",
          "/measurement/", "/about/", "/corrections/", "/contact/"]
PROVING = ["/", "/payments/", "/evidence/CLM-001/", "/data/"]

ISO = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

PAGE_JS = """
(vh) => {
  const main = document.querySelector('main') || document.body;
  const text = main.innerText || '';
  const words = text.split(/\\s+/).filter(Boolean).length;
  const h1 = document.querySelector('h1');
  let h1Lines = null, h1Chars = null;
  if (h1) { const cs = getComputedStyle(h1); const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2;
            h1Lines = Math.round(h1.getBoundingClientRect().height / lh); h1Chars = (h1.innerText || '').length; }
  const strip = document.querySelector('nav.strip');
  const toc = strip ? strip.querySelectorAll('a').length : 0;
  const stripOverflow = strip ? (strip.scrollWidth > strip.clientWidth + 1) : false;
  const firstTop = (sel) => { let best = null; for (const el of main.querySelectorAll(sel)) { const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue; const t = r.top + window.scrollY; if (best === null || t < best) best = t; } return best; };
  const fig = firstTop('.fnum'); const clock = firstTop('.clock'); const bound = firstTop('[data-boundary-part], .bound, .isnot');
  const evlink = firstTop('a[href*="/evidence/"]'); const srclink = firstTop('a[href^="http"]');
  let firstWords = 0; const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) { const n = walker.currentNode; const p = n.parentElement; if (!p) continue;
    const r = p.getBoundingClientRect(); if (r.bottom + window.scrollY <= vh && r.width > 0) firstWords += (n.textContent || '').split(/\\s+/).filter(Boolean).length; }
  let small = 0, targets = 0; for (const el of main.querySelectorAll('a[href], button, input, select, summary')) {
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue; targets++; if (r.width < 24 || r.height < 24) small++; }
  const details = main.querySelectorAll('details').length; const openDetails = main.querySelectorAll('details[open]').length;
  const figures = main.querySelectorAll('figure[data-visual-id]').length; const tables = main.querySelectorAll('table').length;
  const fonts = performance.getEntriesByType('resource').filter(e => /\\.woff2?(\\?|$)/.test(e.name)).length;
  return { scrollHeight: document.documentElement.scrollHeight, scrollWidth: document.documentElement.scrollWidth,
           clientWidth: document.documentElement.clientWidth, words, h1Lines, h1Chars, h1: h1 ? h1.innerText : null,
           toc, stripOverflow, first: { fig, clock, bound, evlink, srclink, words: firstWords },
           targets, small, details, openDetails, figures, tables, fonts, text };
}
"""

BYTES_JS = """
() => { const nav = performance.getEntriesByType('navigation')[0]; const res = performance.getEntriesByType('resource');
  const by = {}; let total = nav ? nav.transferSize : 0; let n = 1;
  const kind = (u) => /\\.woff2?/.test(u) ? 'font' : /\\.css/.test(u) ? 'css' : /\\.js/.test(u) ? 'js' : /\\.(png|jpg|jpeg|webp|svg|gif|ico)/.test(u) ? 'image' : /\\.json/.test(u) ? 'json' : 'other';
  by.html = nav ? nav.transferSize : 0;
  for (const e of res) { n++; total += e.transferSize; const k = kind(e.name); by[k] = (by[k] || 0) + e.transferSize; }
  return { total, requests: n, by }; }
"""


def serve_gzip():
    import performance_budget as pb
    rules = pb.parse_headers((pb.DIST / "_headers").read_text(encoding="utf-8"))
    srv = pb.serve(rules)
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def measure_pages(base, shots: Path, label: str):
    from playwright.sync_api import sync_playwright
    out = OrderedDict()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for lang in LANGS:
            for route in ROUTES:
                key = f"{lang}:{route}"
                out[key] = OrderedDict([("lang", lang), ("route", route), ("widths", OrderedDict())])
                for w in WIDTHS:
                    ctx = browser.new_context(viewport={"width": w, "height": HEIGHT[w]}, locale="ar" if lang == "ar" else "en")
                    page = ctx.new_page()
                    page.goto(f"{base}/{lang}{route}", wait_until="networkidle")
                    m = page.evaluate(PAGE_JS, HEIGHT[w])
                    text = m.pop("text")
                    rec = OrderedDict()
                    rec["screens"] = round(m["scrollHeight"] / HEIGHT[w], 1)
                    rec["px"] = m["scrollHeight"]
                    rec["overflow_x"] = m["scrollWidth"] > m["clientWidth"]
                    rec["h1_lines"] = m["h1Lines"]
                    rec["h1_chars"] = m["h1Chars"]
                    rec["toc_entries"] = m["toc"]
                    rec["toc_strip_overflows"] = m["stripOverflow"]
                    rec["iso_dates_visible"] = len(ISO.findall(text))
                    rec["words"] = m["words"]
                    rec["targets"] = m["targets"]
                    rec["targets_under_24px"] = m["small"]
                    rec["details"] = m["details"]
                    rec["details_open"] = m["openDetails"]
                    rec["figures"] = m["figures"]
                    rec["tables"] = m["tables"]
                    vh = HEIGHT[w]
                    f = m["first"]
                    rec["first_screen"] = OrderedDict([
                        ("words", f["words"]),
                        ("figure", f["fig"] is not None and f["fig"] < vh),
                        ("clock", f["clock"] is not None and f["clock"] < vh),
                        ("boundary", f["bound"] is not None and f["bound"] < vh),
                        ("evidence_link", f["evlink"] is not None and f["evlink"] < vh),
                        ("source_link", f["srclink"] is not None and f["srclink"] < vh),
                        ("positions_px", OrderedDict([(k, None if v is None else int(v)) for k, v in
                                                      (("figure", f["fig"]), ("clock", f["clock"]), ("boundary", f["bound"]),
                                                       ("evidence_link", f["evlink"]), ("source_link", f["srclink"]))])),
                    ])
                    if w == 390:
                        rec["h1_text"] = m["h1"]
                        b = page.evaluate(BYTES_JS)
                        rec["cold_bytes"] = b["total"]
                        rec["requests"] = b["requests"]
                        rec["bytes_by_type"] = b["by"]
                        rec["font_files"] = m["fonts"]
                    slug = route.strip("/").replace("/", "_") or "home"
                    d = shots / label / lang / slug
                    d.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(d / f"{w}_first.png"))
                    if w in (390, 1440):
                        page.screenshot(path=str(d / f"{w}_full.png"), full_page=True)
                    out[key]["widths"][str(w)] = rec
                    ctx.close()
        browser.close()
    return out


STATES = [
    ("menu_open", "/", "click [data-menu]"),
    ("search_results", "/", "search"),
    ("source_filter", "/data/?source=SRC-WB-FSD-2024-001", "none"),
    ("source_facet", "/data/", "facet"),
    ("compare_verdict", "/evidence/compare/?records=CLM-001,CLM-003", "none"),
    ("cite_open", "/evidence/CLM-001/", "click [data-cite]"),
    ("report_link", "/evidence/CLM-001/", "scroll .report"),
    ("disclosure_open", "/payments/", "open details"),
]


def capture_states(base, shots: Path, label: str):
    from playwright.sync_api import sync_playwright
    log = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for lang, w in (("ar", 390), ("en", 1440)):
            q = "حوالات" if lang == "ar" else "remittances"
            for name, route, action in STATES:
                ctx = browser.new_context(viewport={"width": w, "height": HEIGHT[w]})
                page = ctx.new_page()
                page.goto(f"{base}/{lang}{route}", wait_until="networkidle")
                note = ""
                try:
                    if action.startswith("click "):
                        sel = action[6:]
                        if page.locator(sel).first.is_visible():
                            page.locator(sel).first.click()
                            page.wait_for_timeout(300)
                        else:
                            note = f"{sel} not visible at {w}"
                    elif action == "search":
                        page.locator("[data-search-open]").first.click()
                        page.locator("[data-search-input]").first.fill(q)
                        page.wait_for_timeout(600)
                        note = f"query={q}; results={page.locator('[data-search-results] a').count()}"
                    elif action == "facet":
                        sel = page.locator("select[data-source-facet='publisher']").first
                        opts = sel.locator("option").all_text_contents()
                        if len(opts) > 1:
                            sel.select_option(index=1)
                            page.wait_for_timeout(400)
                            note = f"facet publisher={opts[1]!r}; status={page.locator('[data-source-filter-status]').first.inner_text()[:80]!r}"
                    elif action == "scroll .report":
                        el = page.locator(".report").first
                        el.scroll_into_view_if_needed()
                        note = f"report href={el.get_attribute('href')!r}"[:160]
                    elif action == "open details":
                        page.locator("main details").first.evaluate("d => d.open = true")
                        page.locator("main details").first.scroll_into_view_if_needed()
                except Exception as e:  # a state that cannot be reached is itself a finding
                    note = f"ERROR {type(e).__name__}: {str(e)[:120]}"
                d = shots / label / "states" / lang
                d.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(d / f"{name}_{w}.png"))
                log.append(OrderedDict([("lang", lang), ("width", w), ("state", name), ("route", route), ("note", note)]))
                ctx.close()
            # no-JS
            ctx = browser.new_context(viewport={"width": w, "height": HEIGHT[w]}, java_script_enabled=False)
            page = ctx.new_page()
            for route in ("/", "/evidence/CLM-001/", "/data/"):
                page.goto(f"{base}/{lang}{route}", wait_until="load")
                slug = route.strip("/").replace("/", "_") or "home"
                d = shots / label / "states" / lang
                page.screenshot(path=str(d / f"nojs_{slug}_{w}.png"))
                log.append(OrderedDict([("lang", lang), ("width", w), ("state", "no_js"), ("route", route),
                                        ("note", f"menu links={page.locator('nav#primary-nav a').count()}")]))
            ctx.close()
        browser.close()
    return log


HREF = re.compile(r'<a\b[^>]*href="([^"#?]*)(?:[#?][^"]*)?"', re.I)
EXT = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"', re.I)
TARGETS = OrderedDict([
    ("people_answer", "/people/"), ("payments", "/payments/"), ("reforms", "/reforms/"), ("record_clm001", "/evidence/CLM-001/"),
    ("record_clm003", "/evidence/CLM-003/"), ("compare", "/evidence/compare/"), ("methodology", "/methodology/"),
    ("measurement", "/measurement/"), ("reading_cwr012", "/readings/how-money-reaches-households/"), ("sources", "/data/"),
    ("corrections", "/corrections/"), ("contact", "/contact/"), ("about", "/about/"), ("explore", "/explore/"),
])


def link_graph(site: Path, lang: str, scope: str):
    """scope: 'main' = links inside <main> and <header> only; 'all' = every link on the page."""
    graph = {}
    ext = {}
    for html in (site / lang).rglob("index.html"):
        route = "/" + html.parent.relative_to(site / lang).as_posix().strip(".") + "/"
        route = route.replace("//", "/")
        if route == "/./":
            route = "/"
        t = html.read_text(encoding="utf-8", errors="replace")
        if scope == "main":
            parts = re.findall(r"<header\b.*?</header>|<main\b.*?</main>", t, re.S | re.I)
            t2 = "\n".join(parts)
        else:
            t2 = t
        links = set()
        for h in HREF.findall(t2):
            if h.startswith(f"/{lang}/"):
                r = h[len(lang) + 1:]
                if not r.endswith("/"):
                    r = r.rsplit("/", 1)[0] + "/"
                links.add(r)
        graph[route] = links
        ext[route] = len(EXT.findall(t2))
    return graph, ext


def journeys(site: Path):
    out = OrderedDict()
    for lang in LANGS:
        for scope in ("main", "all"):
            g, ext = link_graph(site, lang, scope)
            dist = {"/": 0}
            prev = {}
            dq = deque(["/"])
            while dq:
                u = dq.popleft()
                for v in g.get(u, ()):
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        prev[v] = u
                        dq.append(v)
            res = OrderedDict()
            for name, target in TARGETS.items():
                if target in dist:
                    path, cur = [], target
                    while cur != "/":
                        path.append(cur)
                        cur = prev[cur]
                    res[name] = OrderedDict([("clicks", dist[target]), ("path", ["/"] + list(reversed(path))),
                                             ("external_links_on_target", ext.get(target, 0))])
                else:
                    res[name] = OrderedDict([("clicks", None), ("path", None), ("external_links_on_target", ext.get(target, 0))])
            out[f"{lang}:{scope}"] = res
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "design/evidence/v2/g0"))
    ap.add_argument("--shots", required=True, help="scratch directory for screenshots (outside the repository)")
    ap.add_argument("--site", default="dist")
    ap.add_argument("--label", default="g0")
    ap.add_argument("--no-states", action="store_true")
    a = ap.parse_args()
    site = ROOT / a.site
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    shots = Path(a.shots)
    import performance_budget as pb
    pb.DIST = site
    t0 = time.time()
    srv, base = serve_gzip()
    try:
        pages = measure_pages(base, shots, a.label)
        states = [] if a.no_states else capture_states(base, shots, a.label)
    finally:
        srv.shutdown()
    j = journeys(site)
    import subprocess
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    report = OrderedDict([
        ("label", a.label), ("commit", sha), ("site", a.site), ("measured_at_utc", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())),
        ("method", "Chromium (Playwright), gzip static server as dist/_headers declares; screens = scrollHeight / viewport height "
                   "(320x568, 390x844, 768x1024, 1440x900); cold bytes = transferSize of the navigation and every resource in a "
                   "fresh context at 390; journeys = shortest click path over the built HTML link graph from Home; "
                   "automated, not human timing"),
        ("routes", ROUTES), ("widths", list(WIDTHS)), ("pages", pages), ("states", states), ("journeys", j),
        ("duration_s", round(time.time() - t0, 1)),
    ])
    (out / f"{a.label}_metrics.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    # the scoreboard, as the brief's Part 2 table
    rows = []
    for route in ROUTES:
        ar = pages.get(f"ar:{route}", {}).get("widths", {})
        en = pages.get(f"en:{route}", {}).get("widths", {})
        rows.append((route, ar.get("390", {}).get("screens"), en.get("390", {}).get("screens"), en.get("1440", {}).get("screens"),
                     ar.get("390", {}).get("toc_entries"), ar.get("390", {}).get("h1_lines"), en.get("1440", {}).get("h1_lines"),
                     ar.get("390", {}).get("cold_bytes"), ar.get("390", {}).get("font_files")))
    lines = ["| Route | AR 390 screens | EN 390 | EN 1440 | TOC (AR) | H1 lines AR 390 | H1 lines EN 1440 | AR cold bytes | fonts |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append("| " + " | ".join("—" if v is None else str(v) for v in r) + " |")
    (out / f"{a.label}_scoreboard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"G0 MEASURED: {len(pages)} page×lang rows, {len(states)} states, journeys for {len(TARGETS)} targets, "
          f"{report['duration_s']} s -> {out}")


if __name__ == "__main__":
    main()
