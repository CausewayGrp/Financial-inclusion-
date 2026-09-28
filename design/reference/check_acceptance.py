#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D7 acceptance check on the reference site (design/reference/out): the whole-product conditions of
handoff/DESIGN_ACCEPTANCE_CRITERIA.md that no earlier gate's check asserts, and the last-ten-percent surfaces of the
brief (§20, D7) driven in both languages, with evidence.

  python3 design/reference/check_acceptance.py [--site design/reference/out] [--evidence design/evidence/d7] [--static-only]

Static phase — every document the build wrote (286 edition pages, the root entry, the 404; the export and social
frames for the placeholder and CSP rules):
  no development placeholder · strict-CSP output (no inline executable script, inline style, inline handler, form,
  frame or external resource) · the discovery head as the baseline writes it — title, description, canonical,
  hreflang, Open Graph without image, citation meta and JSON-LD byte-equal with dist/ for the same route · one h1,
  lang and dir, the skip link first, #main · the language switch on every edition page · the trust layer in every
  footer · no download offered and no document bundled · the sources without a public locator never named · the
  withheld CLM-044 value never printed · every original-source link external, in a new window, rel=noopener, with a
  visible cue · only the shipped fonts and their licence.
Browser phase (Playwright, EN and AR): the skip link on the first Tab with a visible outline; search with no match
announced, Escape closing the dialog and returning focus; the language switch keeping the route; Compare at 320 px in
its stacked form with labelled inputs and the verdict before the table; Contact and Corrections with a record
context; the neutral 404; every trust route; the longest title of each language at 320 px; reduced motion (no
transition or animation anywhere, in either preference); the review-test surfaces — Home, CLM-003, the flagship
Reading, /people/, Compare with a comparison and the RV-CWR-001 export frame — at 1440 and 390 px without overflow.
With --evidence, a PNG of each surface. Exit 1 on any failure; the record is `out/_review_acceptance.json`.
Proof for the record, not authority.
"""
from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REF = ROOT / "design" / "reference"
sys.path.insert(0, str(REF))
from yfie import content as C  # noqa: E402
import check_visuals as CV  # noqa: E402  (serve)

NAV = json.loads((ROOT / "site-src/content/content/navigation_interaction.json").read_text(encoding="utf-8"))
INV = json.loads((ROOT / "handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json").read_text(encoding="utf-8"))
TRUST = NAV.get("trust_navigation") or []
TRUST_ROUTES = [r["route"] for r in INV["routes"] if r["page_family"] == "Reference / Trust"]
LONGEST = {lang: max(INV["routes"], key=lambda r: len(r.get(f"title_{lang}") or ""))["route"] for lang in ("en", "ar")}
COMPARE_PAIR = "CLM-001,CLM-010"   # two records of the comparable set (the D5 language-switch state uses the same pair)
REVIEW = [("home", "/"), ("record", "/evidence/CLM-003/"), ("reading", "/readings/same-year-different-number/"), ("domain", "/people/"),
          ("compare", f"/evidence/compare/?records={COMPARE_PAIR}")]   # the four review tests' surfaces (brief §7; the export frame is added in the browser phase)
HEAD_PARTS = [r'<title>.*?</title>', r'<meta name="description"[^>]*>', r'<link rel="canonical"[^>]*>', r'<link rel="alternate"[^>]*>',
              r'<meta property="og:[^>]*>', r'<meta name="twitter:card"[^>]*>', r'<meta name="yfie-citation"[^>]*>', r'<meta name="yfie-record-id"[^>]*>',
              r'<script type="application/ld\+json">.*?</script>']
DOC_EXT = r'\.(?:pdf|xlsx|xls|docx|doc|csv|zip|json|pptx)'
TAG = re.compile(r"<[^>]+>")
BLOCK = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S)


def text_of(doc: str) -> str:
    return re.sub(r"\s+", " ", html_mod.unescape(TAG.sub(" ", BLOCK.sub(" ", doc))))


def head_of(doc: str) -> dict:
    h = doc[:doc.find("</head>")]
    return {k: re.findall(k, h, re.S) for k in HEAD_PARTS}


def edition_pages(site: Path):
    for lang in ("en", "ar"):
        for f in sorted((site / lang).rglob("index.html")):
            route = "/" + "/".join(f.relative_to(site / lang).parts[:-1])
            route = route if route.endswith("/") else route + "/"
            yield lang, route, f


def static_phase(site: Path, failures: list) -> dict:
    content = C.load()
    no_locator = sorted(sid for sid, s in content.sources.items() if not content.public_locator(s.get("primary_url")))
    counts = {"documents": 0, "assertions": 0, "frames": 0}
    observations: dict = {"no_locator_ids_in_data_blocks": []}

    def check(where: str, name: str, ok: bool):
        counts["assertions"] += 1
        if not ok:
            failures.append({"static": where, "failed": name})

    def csp(where: str, doc: str):
        for attrs in re.findall(r"<script\b([^>]*)>", doc):
            check(where, "script_is_data_or_same_origin", bool(re.search(r'type="application/(?:ld\+)?json"', attrs)) or bool(re.search(r'\ssrc="/assets/[\w.-]+\.js"', attrs)))
        check(where, "no_inline_style", not re.search(r'\sstyle="', doc))
        check(where, "no_inline_handler", not re.search(r'\son[a-z]+="', doc))
        check(where, "no_form_frame_object", not re.search(r"<(?:form|iframe|object|embed)\b", doc))
        check(where, "no_external_resource", not re.search(r'<(?:link|script|img|source|video|audio)\b[^>]*\s(?:href|src)="https?://', doc))
        check(where, "no_placeholder", "⟦NCC:" not in doc)

    for lang, route, f in edition_pages(site):
        counts["documents"] += 1
        doc = f.read_text(encoding="utf-8"); text = text_of(doc); where = f"/{lang}{route}"
        other = "ar" if lang == "en" else "en"
        csp(where, doc)
        # the discovery head as the baseline writes it (F6 kept; JSON-LD as today)
        twin = ROOT / "dist" / lang / route.strip("/") / "index.html"
        check(where, "baseline_twin_exists", twin.exists())
        if twin.exists():
            mine, theirs = head_of(doc), head_of(twin.read_text(encoding="utf-8"))
            for k in HEAD_PARTS:
                check(where, f"head_equals_baseline:{k[:24]}", mine[k] == theirs[k])
        check(where, "no_og_image", "og:image" not in doc)
        check(where, "html_lang_dir", bool(re.search(rf'<html lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}">', doc)))
        body = doc[doc.find("<body"):]
        check(where, "one_h1", len(re.findall(r"<h1\b", body)) == 1)
        first_a = re.search(r"<a\b[^>]*>", body)
        check(where, "skip_link_first", bool(first_a) and 'class="skip"' in first_a.group(0) and 'href="#main"' in first_a.group(0) and 'id="main"' in body)
        check(where, "language_switch_present", f'data-lang="{other}"' in body)
        footer = body[body.find("<footer"):]
        for t in TRUST:
            check(where, f"footer_trust:{t['route']}", f'href="/{lang}{t["route"]}"' in footer and html_mod.escape(t.get(f"label_{lang}") or "", quote=False) in footer)
        check(where, "no_download_attribute", not re.search(r"<a\b[^>]*\sdownload(?:=|\s|>)", body))   # the attribute, never the word in governed prose
        check(where, "no_document_offered", not re.search(rf'href="/[^"]*{DOC_EXT}"', body))
        for sid in no_locator:
            check(where, f"no_locator_source_never_named:{sid}", sid not in text)
            if sid in doc and sid not in text:
                observations["no_locator_ids_in_data_blocks"].append(f"{where} {sid}")
        if route == "/evidence/CLM-044/":
            check(where, "withheld_value_never_printed", not re.search(r"US\$\s?\d|\d[\d,]*\s?(?:million|مليون)", text))
        for attrs, inner in re.findall(r'<a class="source-locator"([^>]*)>(.*?)</a>', body, re.S):
            named = len(TAG.sub("", inner).strip()) > 1 or 'aria-label="' in attrs   # the governed "Open original source ↗", or the chain's "↗" glyph named by its aria-label
            ok = 'target="_blank"' in attrs and "noopener" in attrs and bool(re.search(r'href="https?://', attrs)) and "↗" in inner and named
            check(where, "source_locator_external_with_cue", ok)
    for name in ("index.html", "404.html"):
        doc = (site / name).read_text(encoding="utf-8"); counts["documents"] += 1
        csp("/" + name, doc)
        check("/" + name, "both_editions_linked", 'href="/en/"' in doc and 'href="/ar/"' in doc)
    for f in sorted(list((site / "_export").glob("*.html")) + list((site / "_social").glob("*.html"))):
        counts["frames"] += 1
        csp(str(f.relative_to(site)), f.read_text(encoding="utf-8"))
    css = (site / "assets" / "yfie.css").read_text(encoding="utf-8")
    for url in sorted(set(re.findall(r"url\('([^']+)'\)", css))):
        check("assets/yfie.css", f"font_file_shipped:{Path(url).name}", url.startswith("/assets/fonts/") and (site / url.lstrip("/")).exists())
    check("assets/yfie.css", "no_external_url_in_css", "url(http" not in css and "url('http" not in css and "@import" not in css)
    for folder in ("ibm-plex-sans", "ibm-plex-sans-arabic"):
        check("assets/fonts", f"licence_shipped:{folder}", (site / "assets" / "fonts" / folder / "LICENSE.txt").exists())
    counts["observations"] = observations
    return counts


def browser_phase(site: Path, evidence: Path | None, failures: list) -> int:
    from playwright.sync_api import sync_playwright
    httpd, base = CV.serve(site)
    n = 0

    def check(lang: str, name: str, ok: bool):
        nonlocal n
        n += 1
        if not ok:
            failures.append({"browser": name, "lang": lang})

    def shot(pg, name: str, lang: str, w: int, full: bool = False):
        if evidence:
            pg.screenshot(path=str(evidence / f"{name}-{lang}-{w}.png"), full_page=full)

    NO_OVERFLOW = "document.documentElement.scrollWidth-document.documentElement.clientWidth<=1"
    MOTION = """[...document.querySelectorAll('*')].filter(e=>{const cs=getComputedStyle(e);return cs.animationName!=='none'||cs.transitionDuration.split(',').some(d=>parseFloat(d)>0)}).length"""
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("en", "ar"):
            other = "ar" if lang == "en" else "en"
            ctx = b.new_context(viewport={"width": 390, "height": 844}); pg = ctx.new_page()
            # focus: the first Tab lands on the skip link, outlined and in view
            pg.goto(f"{base}/{lang}/", wait_until="load"); pg.keyboard.press("Tab"); pg.wait_for_timeout(100)
            st = pg.evaluate("(()=>{const a=document.activeElement;const cs=getComputedStyle(a);const r=a.getBoundingClientRect();return {skip:a.classList.contains('skip'),outline:cs.outlineStyle!=='none'&&parseFloat(cs.outlineWidth)>0,visible:r.width>0&&r.height>0&&r.bottom>0}})()")
            check(lang, "skip_link_first_tab_outlined", all(st.values())); shot(pg, "focus-skip", lang, 390)
            # search: no match announced in the technical voice; Escape closes and returns focus
            pg.click("[data-search-open]"); pg.fill("#global-search-dialog", "zzqqxxvv"); pg.wait_for_timeout(600)
            st = pg.evaluate("(()=>{const d=document.querySelector('#search-dialog');const e=d.querySelector('[data-search-results] .empty, #search-results .empty');return {open:!!d&&d.open,empty:!!e&&e.offsetParent!==null&&e.innerText.trim().length>0,status:[...d.querySelectorAll('[data-search-status]')].some(x=>x.innerText.trim().length>0),notEvidence:!!e&&!e.closest('section.bnd')}})()")
            check(lang, "search_no_match_announced", all(st.values())); shot(pg, "search-nomatch", lang, 390)
            pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
            check(lang, "escape_closes_search_returns_focus", pg.evaluate("(()=>{const d=document.querySelector('#search-dialog');return !d.open&&document.activeElement.hasAttribute('data-search-open')})()"))
            # the language switch keeps the route
            pg.goto(f"{base}/{lang}/about/", wait_until="load"); pg.click("[data-lang]"); pg.wait_for_load_state("load"); pg.wait_for_timeout(200)
            check(lang, "language_switch_keeps_route", pg.url.endswith(f"/{other}/about/"))
            # Compare at 320 px: the stacked form, labelled inputs, the verdict before the table, no overflow
            pg.set_viewport_size({"width": 320, "height": 844}); pg.goto(f"{base}/{lang}/evidence/compare/?records={COMPARE_PAIR}", wait_until="load"); pg.wait_for_timeout(500)
            st = pg.evaluate("""(()=>{const d=document.documentElement;const t=document.querySelector('table.compare-table');const sel=[...document.querySelectorAll('select[id^=compare-]')];const v=document.querySelector('[data-compare-verdict]');
              return {over:d.scrollWidth-d.clientWidth<=1, rows:!!t&&t.querySelectorAll('tbody tr').length>0, stacked:!!t&&getComputedStyle(t.querySelector('tbody th')).display==='block',
                labelled:sel.length===4&&sel.every(s=>s.labels.length>0||s.getAttribute('aria-label')||s.getAttribute('aria-labelledby')), verdictFirst:!!v&&!!t&&!!(v.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_FOLLOWING)}})()""")
            check(lang, "compare_320_stacked_labelled_verdict_first", all(st.values())); shot(pg, "compare", lang, 320)
            # Contact and Corrections with a record context: the record carried, the way on (Contact: the mail action
            # naming the record; Corrections: the link to the current public record), no error
            pg.set_viewport_size({"width": 390, "height": 844})
            for route, way_on in (("/contact/", "[data-correction-mail]"), ("/corrections/", "[data-correction-link]")):
                pg.goto(f"{base}/{lang}{route}?record=CLM-003", wait_until="load"); pg.wait_for_timeout(300)
                st = pg.evaluate("(sel)=>{const o=document.querySelector('[data-correction-origin]');const m=document.querySelector(sel);const e=document.querySelector('[data-correction-error]');const h=m?(m.getAttribute('href')||''):'';return {record:!!o&&!o.hidden&&/CLM-003/.test(o.innerText),wayOn:!!m&&!m.hidden&&m.offsetParent!==null&&(/^mailto:/.test(h)?/CLM-003/.test(h):/\\/evidence\\/CLM-003\\//.test(h)),noError:!e||e.hidden,h1:document.querySelectorAll('h1').length===1}}", way_on)
                check(lang, f"record_context{route}", all(st.values())); shot(pg, route.strip("/"), lang, 390)
            # every trust route renders with its h1 and body, in view at 390
            for route in TRUST_ROUTES:
                pg.goto(f"{base}/{lang}{route}", wait_until="load"); pg.wait_for_timeout(120)
                st = pg.evaluate("(()=>({h1:document.querySelectorAll('h1').length===1,text:document.querySelector('#main').innerText.length>200,over:" + NO_OVERFLOW + "}))()")
                check(lang, f"trust_route{route}", all(st.values())); shot(pg, "trust-" + route.strip("/"), lang, 390)
            # the longest governed title of this language at 320 px
            pg.set_viewport_size({"width": 320, "height": 844}); pg.goto(f"{base}/{lang}{LONGEST[lang]}", wait_until="load"); pg.wait_for_timeout(150)
            check(lang, "longest_title_fits_320", pg.evaluate(NO_OVERFLOW)); shot(pg, "longest-title", lang, 320)
            # reduced motion: nothing moves, whatever the preference (the product has no motion)
            check(lang, "no_motion_default", pg.evaluate(MOTION) == 0)
            ctx2 = b.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce"); p2 = ctx2.new_page()
            p2.goto(f"{base}/{lang}/", wait_until="load"); check(lang, "no_motion_reduced", p2.evaluate(MOTION) == 0); ctx2.close()
            # the review-test surfaces at 1440 and 390 (evidence for brief §7), each without overflow
            for name, route in REVIEW:
                for w in (1440, 390):
                    pg.set_viewport_size({"width": w, "height": 900 if w == 1440 else 844}); pg.goto(f"{base}/{lang}{route}", wait_until="load"); pg.wait_for_timeout(400 if "compare" in route else 150)
                    check(lang, f"review_{name}_{w}_fits", pg.evaluate(NO_OVERFLOW)); shot(pg, f"review-{name}", lang, w)
            pg.set_viewport_size({"width": 900, "height": 900}); pg.goto(f"{base}/_export/RV-CWR-001__{lang}.html", wait_until="load"); pg.wait_for_timeout(150)
            check(lang, "review_export_fits", pg.evaluate(NO_OVERFLOW)); shot(pg, "review-export-RV-CWR-001", lang, 900, full=True)
            ctx.close()
        ctx = b.new_context(viewport={"width": 390, "height": 844}); pg = ctx.new_page()
        pg.goto(f"{base}/404.html", wait_until="load"); pg.wait_for_timeout(120)
        check("neutral", "not_found_bilingual", pg.evaluate("document.querySelectorAll('a[href=\"/en/\"],a[href=\"/ar/\"]').length>=2&&document.querySelectorAll('[lang=ar]').length>0&&document.querySelectorAll('[lang=en]').length>0"))
        shot(pg, "not-found", "neutral", 390); ctx.close()
        b.close()
    httpd.shutdown()
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=str(REF / "out"))
    ap.add_argument("--evidence", default="")
    ap.add_argument("--static-only", action="store_true")
    args = ap.parse_args()
    site = Path(args.site)
    if not (site / "en" / "index.html").exists():
        print(f"site not built: {site}"); return 2
    evidence = Path(args.evidence) if args.evidence else None
    if evidence:
        evidence.mkdir(parents=True, exist_ok=True)
    failures: list = []
    counts = static_phase(site, failures)
    n_browser = 0 if args.static_only else browser_phase(site, evidence, failures)
    for f in failures[:80]:
        print("FAIL", json.dumps(f, ensure_ascii=False))
    (site / "_review_acceptance.json").write_text(json.dumps({**counts, "browser_assertions": n_browser, "failures": failures}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ACCEPTANCE: {'FAIL' if failures else 'PASS'} — {counts['documents']} documents and {counts['frames']} frames checked statically ({counts['assertions']} assertions); "
          f"{n_browser} browser assertions on the last-ten-percent surfaces in EN and AR; {len(failures)} failures"
          + (f"; observations: {len(counts['observations']['no_locator_ids_in_data_blocks'])} no-locator ids inside data blocks" if counts["observations"]["no_locator_ids_in_data_blocks"] else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
