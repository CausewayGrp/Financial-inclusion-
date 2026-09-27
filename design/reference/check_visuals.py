#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contract-by-contract checks of the visual system on the rendered reference site (D6), in both languages.

  python3 design/reference/check_visuals.py [--site design/reference/out] [--only VIS-ID,...] [--phases contracts,degraded,frames,print] [--evidence DIR]

For each of the 36 governed visual contracts (`site-src/content/visuals/visual_design_contracts.json`, never a hand-kept
list), on its canonical route and on every public route that binds it, in English and Arabic:
- its tier's rule holds on the DOM: a SIGNATURE or CORE_ANALYTICAL contract with resolved rows is drawn and prints every
  governed value it binds (series values, object counts, derived values), with every marker in its data labelled by the
  governed grammar label (a WITHHELD value never printed); a SUPPORTING contract plots no value (a chain of governed
  states or the governed text); a TABLE_TEXT_FIRST contract is the governed text, never a chart; the RETIRE_FROM_DESIGN
  contract is never drawn and has no figure on its record page;
- the detached frame is complete in every figure: title, question, scope (period · universe), the prohibited inference
  once in the boundary voice, the credit where the contract has one (isolated left-to-right), the canonical link, the
  edition; the text alternative with the governed alt text and, for drawn contracts, a table with a caption and scoped
  headers; every SVG left-to-right; every ISO date isolated left-to-right (after Arabic letters a plain one renders
  reversed); no inline style; no red, amber or green;
- every fallback table names each data column with a governed string and sits in a focusable region with an
  accessible name; at 320 and 390 px the figure never overflows its column and its plot area never scrolls; a table
  scrolls only inside that region, and only when it is declared wide (the provider matrix; DEBT-010 closed elsewhere);
- in forced colours every mark and label takes the system colour; in print the frame foot stays visible;
- the development placeholders on the site are exactly the escalated set (the five matrix headings), nowhere else.
Then the portable frames the build writes: every export frame (`_export/`) renders at 900 px without overflow with the
same frame lines, the identity line and no cite control; every social frame (`_social/`, 286) fits 1200 × 630 with its
title, canonical link, edition and the unaltered logo. Then print: one route per family in both languages is printed to
PDF (A4) and its first page must carry the page title; with PyMuPDF installed the pages are rasterised for the evidence.
With --evidence DIR: figure crops of every drawn contract (1440 px, both languages), export and social PNGs, print pages.
Exit 1 on any failure. Proof for the record, not authority; design/COVERAGE.csv cites this tool's output.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import re
import socket
import sys
import threading
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REF = ROOT / "design" / "reference"
sys.path.insert(0, str(REF))
from yfie.visuals import DRAWERS, FIGURES, plain_num  # noqa: E402

CONTRACTS = json.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))
GRAMMAR = CONTRACTS["grammar_labels"]
DRAWN = set(FIGURES) | set(DRAWERS)
PLACEHOLDERS = {"UI-VIS-MATRIX-AUTHORITY", "UI-VIS-MATRIX-UNIVERSE", "UI-VIS-MATRIX-STATUS", "UI-VIS-MATRIX-NEGATIVE", "UI-VIS-MATRIX-OPERATION"}   # ESCALATIONS.md (D6)
PALETTE = {"rgb(23, 33, 43)", "rgb(61, 73, 84)", "rgb(102, 113, 123)", "rgb(216, 221, 226)", "rgb(174, 183, 191)", "rgb(122, 90, 29)", "rgb(214, 184, 106)", "rgb(30, 86, 80)", "rgb(245, 241, 233)", "rgb(255, 255, 255)", "rgba(0, 0, 0, 0)", "none"}
EXPORT_EVIDENCE = {"RV-CWR-001", "VIS-PROVIDER-OBSERVABILITY", "RV-CWR-004", "VIS-FIRM-CONSTRAINTS"}   # export PNGs kept as evidence (every frame is checked)
PRINT_ROUTES = ["/", "/explore/", "/people/", "/evidence/", "/evidence/CLM-003/", "/evidence/compare/", "/readings/", "/readings/same-year-different-number/", "/data/", "/measurement/", "/about/"]   # one per family
MARKER_LABEL = {"BREAK_VINTAGE": "UI-VIS-BREAK-VINTAGE", "BREAK_UNIVERSE": "UI-VIS-BREAK-UNIVERSE", "SAME_YEAR_REVISION": "UI-VIS-SAME-YEAR-REVISION", "MISSING": "UI-VIS-MISSING",
                "DISAGREEMENT": "UI-VIS-DISAGREEMENT", "NOT_COMPARABLE": "UI-VIS-NOT-COMPARABLE", "NOMINAL": "UI-VIS-NOMINAL", "WITHHELD": "UI-VIS-WITHHELD", "TARGET": "UI-VIS-TARGET", "RESULT": "UI-VIS-RESULT"}


def routes_of(c: dict) -> list[str]:
    g = c["governed"]
    out = [g["canonical_route"]] + [r if r.endswith("/") else r + "/" for r in g.get("public_routes") or []]
    return list(dict.fromkeys(r for r in out if r))


def governed_values(c: dict) -> tuple[list, list]:
    """(values that must print, values that must never print) for a contract with rows."""
    con = c.get("contract") or {}
    must, never = [], []
    for s in con.get("series") or []:
        for r in s.get("values") or []:
            if r.get("withheld") or "WITHHELD" in (r.get("markers") or []):
                if r.get("y") is not None:
                    never.append(plain_num(r["y"]))
            elif r.get("y") is not None:
                must.append(plain_num(r["y"]))
    for o in con.get("objects") or []:
        for r in o.get("records") or []:
            if r.get("count") is not None:
                must.append(plain_num(r["count"]) if not isinstance(r["count"], str) else r["count"])
            if r.get("y") is not None:
                must.append(plain_num(r["y"]))
    for d in con.get("derived") or []:
        if d.get("value") is not None:
            must.append(plain_num(d["value"]))
    return must, never


def markers_of(c: dict) -> set:
    con = c.get("contract") or {}
    out = set()
    for s in con.get("series") or []:
        out |= set(s.get("markers") or [])
        for r in s.get("values") or []:
            out |= set(r.get("markers") or [])
            if r.get("withheld"):
                out.add("WITHHELD")
        for m in s.get("missing_x") or []:
            out.add(m.get("marker") or "MISSING")
    for o in con.get("objects") or []:
        for r in o.get("records") or []:
            out |= set(r.get("markers") or [])
    return out


def serve(directory: Path):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()

    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    h = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(Q, directory=str(directory)))
    threading.Thread(target=h.serve_forever, daemon=True).start()
    return h, f"http://127.0.0.1:{port}"


FIG_STATE = """(vid) => { const f=document.querySelector(`figure.fig[data-visual-id='${vid}']`); if(!f) return null;
  const q=s=>f.querySelectorAll(s).length; const txt=f.textContent.replace(/\\s+/g,' ');
  const foot=f.querySelector('.foot'); const b=f.querySelector('.foot .b');
  const clone=f.cloneNode(true); clone.querySelectorAll('.alt,figcaption').forEach(e=>e.remove()); const frameTxt=clone.textContent.replace(/\\s+/g,' ');
  const els=[...f.querySelectorAll('svg *')]; const fills=els.filter(e=>e.tagName!=='line').map(e=>getComputedStyle(e).fill).concat(els.map(e=>getComputedStyle(e).stroke));
  return {text:txt, frame:frameTxt, textOnly:f.classList.contains('fig-text'), svg:q('svg'), vals:q('svg text.val'), canvas:q('canvas')+q('img'), inline:q('[style]'),
    ltr:[...f.querySelectorAll('svg')].every(s=>s.getAttribute('direction')==='ltr'), title:(f.querySelector('.fig-t')||{}).textContent||'',
    caps:[...f.querySelectorAll('p.cap')].map(p=>p.textContent), bnd:b?b.textContent:'', bndOnce:(()=>{if(!b)return false;const s=b.innerText.replace(/^[^:]*:\\s*/,'').slice(0,40);return frameTxt.split(s).length===2})(),
    credit:!!f.querySelector('.foot bdi[dir=ltr]'), canon:(f.querySelector('.foot a.canon, .foot a.canon-l')||{}).getAttribute?.('href')||'', ed:(f.querySelector('.foot .ed')||{}).textContent||'',
    alt:!!f.querySelector('.alt[data-visual-fallback]'), altText:(f.querySelector('.alt[data-visual-fallback]')||{}).textContent||'', table:q('.alt table'), caption:q('.alt table caption'), th:q('.alt table th[scope]'),
    emptyTh:[...f.querySelectorAll('.alt table thead th:not(:first-child)')].filter(t=>!t.textContent.trim()).length, wrapNamed:[...f.querySelectorAll('.alt .table-wrap')].every(w=>w.getAttribute('role')==='region'&&(w.getAttribute('aria-label')||'').trim().length>0),
    fills:[...new Set(fills)], ncc:[...f.querySelectorAll('.ncc')].map(e=>e.textContent), fw:f.getBoundingClientRect().width, fr:f.getBoundingClientRect().right,
    panelsOver:[...f.querySelectorAll('.panels')].some(p=>p.scrollWidth>p.clientWidth+1),
    tables:[...f.querySelectorAll('.alt .table-wrap')].map(w=>({wide:!!w.querySelector('table.wide'), scrolls:w.scrollWidth>w.clientWidth+1})),
    fallbackAttr:f.getAttribute('data-visual-fallback'), indep:f.getAttribute('data-image-independent'),
    isoLoose:(()=>{const w=document.createTreeWalker(f,NodeFilter.SHOW_TEXT);let n=0;while(w.nextNode()){const t=w.currentNode;if(/\d{4}-\d{2}(-\d{2})?/.test(t.nodeValue)&&!t.parentElement.closest('[dir=ltr],svg'))n++;}return n;})()}; }"""


def check_contract(pg, base: str, c: dict, lang: str, failures: list, evidence: Path | None, crops: set) -> int:
    vid = c["visual_id"]; tier = c["tier"]; g = c["governed"]
    must, never = governed_values(c)
    markers = markers_of(c)
    n = 0
    for route in routes_of(c):
        url = f"{base}/{lang}{route}"
        pg.set_viewport_size({"width": 1440, "height": 900})
        pg.goto(url, wait_until="load"); pg.wait_for_timeout(120)
        st = pg.evaluate(FIG_STATE, vid)
        checks = {}
        if vid == "VIS-SOURCE-COMPARISON" and route == "/evidence/compare/":   # the Compare tool is the contract's rendering (D4): boundary first, the alt text as the standfirst, no figure
            tool = pg.evaluate("() => ({b:(document.querySelector('[data-compare-boundary]')||{}).textContent||'', st:[...document.querySelectorAll('main p.st')].map(p=>p.textContent).join(' '), fig:!!document.querySelector(`figure.fig[data-visual-id='VIS-SOURCE-COMPARISON']`)})")
            checks["tool_carries_boundary"] = (g.get(f"prohibited_inference_{lang}") or "")[:40] in tool["b"]
            checks["tool_carries_alt_text"] = (g.get(f"alt_text_{lang}") or "")[:60] in tool["st"]
            checks["no_figure_beside_the_tool"] = not tool["fig"]
            n += len(checks)
            bad = [k for k, v in checks.items() if not v]
            if bad:
                failures.append({"visual": vid, "tier": tier, "lang": lang, "route": route, "failed": bad})
            continue
        if tier == "RETIRE_FROM_DESIGN":
            if route == g["canonical_route"]:
                checks["record_page_has_no_figure"] = st is None
            else:
                checks["never_drawn"] = st is None or (st["textOnly"] and st["svg"] == 0 and st["canvas"] == 0)
        else:
            checks["figure_present"] = st is not None
            if st:
                checks["title_governed"] = st["title"].strip() == (g.get(f"title_{lang}") or "").strip()
                checks["question_in_frame"] = any((g.get(f"question_{lang}") or "").strip() == x.strip() for x in st["caps"]) or (g.get(f"question_{lang}") or "") in st["frame"]
                body = st["text"] if st["textOnly"] else st["frame"]   # a text frame's scope line is its body (D3)
                checks["scope_in_frame"] = all((x or "") in body for x in (g.get(f"period_{lang}"), g.get(f"universe_{lang}")))
                checks["boundary_once_in_foot"] = st["bndOnce"] and (g.get(f"prohibited_inference_{lang}") or "")[:40] in st["bnd"]
                credit = ((c.get("contract") or {}).get("credit") or {}).get("text")
                checks["credit_isolated"] = (credit in st["frame"] and st["credit"]) if credit else True
                canon = f"/{lang}{g['canonical_route']}"
                checks["canonical_link"] = st["canon"] == canon
                checks["edition_in_frame"] = st["ed"].strip() != "" and st["ed"] in st["frame"]
                checks["alt_text"] = (g.get(f"alt_text_{lang}") or "")[:60] in st["altText"] and st["fallbackAttr"] == "ordered-text" and st["indep"] == "true"
                checks["no_inline_style"] = st["inline"] == 0
                checks["iso_dates_isolated"] = st["isoLoose"] == 0   # after Arabic letters a plain ISO date renders reversed (Lock §4.1.8)
                checks["svg_ltr"] = st["ltr"]
                checks["palette_only"] = all(f in PALETTE for f in st["fills"])
                checks["placeholders_escalated_only"] = all(any(k in t for k in PLACEHOLDERS) for t in st["ncc"]) and (not st["ncc"] or vid == "VIS-PROVIDER-OBSERVABILITY")
                if tier in ("SIGNATURE", "CORE_ANALYTICAL"):
                    checks["drawn"] = not st["textOnly"] and vid in DRAWN
                    checks["values_printed"] = all(v in st["text"] for v in must)
                    checks["withheld_never_printed"] = all(v not in st["text"] for v in never)
                    checks["markers_labelled"] = all(GRAMMAR[MARKER_LABEL[m]][lang] in st["text"] for m in markers if m in MARKER_LABEL)
                    checks["table_with_caption_and_scoped_headers"] = st["table"] >= 1 and st["caption"] == st["table"] and st["th"] > 0
                    checks["table_columns_named_and_region_named"] = st["emptyTh"] == 0 and st["wrapNamed"]
                elif tier == "SUPPORTING":
                    checks["no_value_plotted"] = st["vals"] == 0 and st["canvas"] == 0
                    checks["governed_text_or_states"] = st["textOnly"] or vid in DRAWN
                else:   # TABLE_TEXT_FIRST
                    checks["never_a_chart"] = st["svg"] == 0 and st["canvas"] == 0 and st["vals"] == 0
                    checks["governed_text"] = st["textOnly"]
                if evidence and vid in DRAWN and route == g["canonical_route"] and (vid, lang) not in crops:
                    crops.add((vid, lang))
                    pg.locator(f"figure.fig[data-visual-id='{vid}']").first.screenshot(path=str(evidence / f"figure-{vid}-{lang}.png"))
        # narrow widths: the figure fits its column; the plot never scrolls; a table scrolls inside its wrapper only when declared wide
        for w in (320, 390):
            pg.set_viewport_size({"width": w, "height": 844}); pg.goto(url, wait_until="load"); pg.wait_for_timeout(100)
            s2 = pg.evaluate(FIG_STATE, vid)
            if s2:
                checks[f"fits_{w}"] = s2["fr"] <= w + 1 and not s2["panelsOver"]
                checks[f"tables_{w}"] = all(t["wide"] or not t["scrolls"] for t in s2["tables"])
                if evidence and vid in ("VIS-PROVIDER-OBSERVABILITY", "RV-CWR-004", "VIS-FIRM-CONSTRAINTS", "RV-CWR-001") and w == 390 and route == g["canonical_route"]:
                    pg.locator(f"figure.fig[data-visual-id='{vid}']").first.screenshot(path=str(evidence / f"figure-{vid}-{lang}-390.png"))
        n += len(checks)
        bad = [k for k, v in checks.items() if not v]
        if bad:
            failures.append({"visual": vid, "tier": tier, "lang": lang, "route": route, "failed": bad})
    return n


def check_degraded(b, base: str, failures: list) -> int:
    """Forced colours (marks and labels take the system colour) and print (the frame foot stays) on every drawn contract."""
    n = 0
    for lang in ("en", "ar"):
        for vid in sorted(DRAWN):
            c = next(x for x in CONTRACTS["visuals"] if x["visual_id"] == vid)
            route = c["governed"]["canonical_route"]
            url = f"{base}/{lang}{route}"
            ctx = b.new_context(viewport={"width": 1440, "height": 900}, forced_colors="active", color_scheme="dark"); pg = ctx.new_page()
            pg.goto(url, wait_until="load"); pg.wait_for_timeout(120)
            fc = pg.evaluate("""(vid) => { const f=document.querySelector(`figure.fig[data-visual-id='${vid}']`); if(!f) return false;
                const els=[...f.querySelectorAll('svg text, svg .mark, svg rect.bar, svg .path, svg .axis')]; if(!els.length) return true;
                const cols=new Set(els.map(e=>{const cs=getComputedStyle(e); return e.tagName==='text'?cs.fill:(cs.stroke!=='none'?cs.stroke:cs.fill)}));
                return ![...cols].some(c=>c==='rgb(23, 33, 43)'||c==='rgb(30, 86, 80)'||c==='rgb(122, 90, 29)'); }""", vid)
            ctx.close()
            ctx = b.new_context(viewport={"width": 794, "height": 1123}); pg = ctx.new_page()
            pg.goto(url, wait_until="load"); pg.emulate_media(media="print"); pg.wait_for_timeout(120)
            pr = pg.evaluate("""(vid) => { const f=document.querySelector(`figure.fig[data-visual-id='${vid}']`); if(!f) return false;
                const b=f.querySelector('.foot .b'), ed=f.querySelector('.foot .ed'), cite=f.querySelector('.foot .cite-sep');
                const vis=e=>!!e&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().height>0;
                return vis(b)&&vis(ed)&&!vis(cite)&&getComputedStyle(document.querySelector('.print-foot')).display!=='none'; }""", vid)
            ctx.close()
            n += 2
            if not fc:
                failures.append({"visual": vid, "lang": lang, "degraded": "forced_colours"})
            if not pr:
                failures.append({"visual": vid, "lang": lang, "degraded": "print_frame"})
    return n


def check_frames(b, base: str, site: Path, failures: list, evidence: Path | None) -> tuple[int, int]:
    """Every export frame and every social frame the build wrote."""
    ctx = b.new_context(viewport={"width": 900, "height": 900}); pg = ctx.new_page()
    n_x = 0
    for f in sorted((site / "_export").glob("*.html")):
        pg.goto(f"{base}/_export/{f.name}", wait_until="load"); pg.wait_for_timeout(100)
        st = pg.evaluate("""() => { const f=document.querySelector('figure.fig'); const d=document.documentElement;
            return {over:d.scrollWidth-d.clientWidth, fig:!!f, foot:!!f&&!!f.querySelector('.foot .b')&&!!f.querySelector('.foot .ed')&&!!f.querySelector('.foot a.canon'),
              cite:!!f&&!!f.querySelector('.foot .cite-sep')&&getComputedStyle(f.querySelector('.foot .cite-sep')).display!=='none',
              alt:!!f&&!!f.querySelector('.alt')&&getComputedStyle(f.querySelector('.alt')).display!=='none', ident:!!document.querySelector('.exp-id img[alt]'),
              inline:document.querySelectorAll('[style]').length, script:document.querySelectorAll('script').length,
              isoLoose:(()=>{const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n=0;while(w.nextNode()){const t=w.currentNode;if(/\d{4}-\d{2}(-\d{2})?/.test(t.nodeValue)&&!t.parentElement.closest('[dir=ltr],svg'))n++;}return n;})()}; }""")
        ok = st["over"] <= 1 and st["fig"] and st["foot"] and not st["cite"] and not st["alt"] and st["ident"] and st["inline"] == 0 and st["script"] == 0 and st["isoLoose"] == 0
        n_x += 1
        if not ok:
            failures.append({"export": f.name, "state": st})
        if evidence and ok and f.stem.split("__")[0] in EXPORT_EVIDENCE:
            pg.screenshot(path=str(evidence / f"export-{f.stem}.png"), full_page=True)
    ctx.close()
    ctx = b.new_context(viewport={"width": 1200, "height": 630}); pg = ctx.new_page()
    n_s = 0
    social_evidence = {f"{(r.strip('/').replace('/', '_') or 'home')}__{l}.html" for r in PRINT_ROUTES for l in ("en", "ar")}
    for f in sorted((site / "_social").glob("*.html")):
        pg.goto(f"{base}/_social/{f.name}", wait_until="load"); pg.wait_for_timeout(60)
        st = pg.evaluate("""() => { const m=document.querySelector('main'); const body=document.querySelector('.soc-body'); const d=document.documentElement;
            return {h:m.scrollHeight, bh:body.scrollHeight, bc:body.clientHeight, w:d.scrollWidth, title:!!document.querySelector('.soc-title')&&document.querySelector('.soc-title').textContent.trim().length>0,
              canon:!!document.querySelector('.soc-foot .canon')&&document.querySelector('.soc-foot .canon').textContent.trim().length>0, ed:!!document.querySelector('.soc-foot .ed'),
              logo:!!document.querySelector('.soc-head img[alt][src$="CauseWay_Master_Logo.png"]'), inline:document.querySelectorAll('[style]').length, script:document.querySelectorAll('script').length,
              isoLoose:(()=>{const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n=0;while(w.nextNode()){const t=w.currentNode;if(/\d{4}-\d{2}(-\d{2})?/.test(t.nodeValue)&&!t.parentElement.closest('[dir=ltr]'))n++;}return n;})()}; }""")
        ok = st["h"] <= 630 and st["bh"] <= st["bc"] and st["w"] <= 1200 and st["title"] and st["canon"] and st["ed"] and st["logo"] and st["inline"] == 0 and st["script"] == 0 and st["isoLoose"] == 0
        n_s += 1
        if not ok:
            failures.append({"social": f.name, "state": st})
        if evidence and ok and f.name in social_evidence:
            pg.screenshot(path=str(evidence / f"social-{f.stem}.png"))
    ctx.close()
    return n_x, n_s


_DIACRITICS = re.compile(r"[\u064B-\u0652\u0670\u0640]")


def _tokens(text: str) -> list:
    """The words of a title or of a PDF page as comparable tokens: compatibility-normalised (Arabic presentation
    forms and ligatures back to letters), diacritics and punctuation dropped, lower-cased, each word's letters sorted —
    the text of an Arabic PDF run comes back shaped and reordered within a word, but its words keep their order."""
    text = _DIACRITICS.sub("", unicodedata.normalize("NFKC", text or "")).lower()
    return ["".join(sorted(ch for ch in w if ch.isalnum())) for w in re.split(r"\s+", text) if any(ch.isalnum() for ch in w)]


def title_on_page(title: str, page_text: str, max_words: int = 8) -> bool:
    """The page title's words (its first eight) occur on the page in order, each as a bag of letters; a title word may
    come back as up to three page tokens (the extractor splits a word at a diacritic). Order and word bags together
    reject another page's title (the negative control below), which a whole-title letter bag did not."""
    want = _tokens(title)[:max_words]
    have = _tokens(page_text)
    if not want:
        return False
    n = len(have)
    for i in range(n):
        j, ok = i, True
        for w in want:
            for k in (1, 2, 3):
                if j + k <= n and "".join(sorted("".join(have[j:j + k]))) == w:
                    j += k
                    break
            else:
                ok = False
                break
        if ok:
            return True
    return False


def selftest_title_matcher() -> list:
    """Fixed positives (a shaped, spaced Arabic PDF run; an English run) and negative controls (a page holding only the
    product name; another route's title): the matcher must accept the former and reject the latter."""
    cases = [
        ("الشمول المالي في اليمن ليس رقمًا واحدًا.", "أدلة الشمول المايل يف اليمن .الشمول المايل يف اليمن ليس رق ًما واح ًد ا «أدلة الشمول", True),
        ("People: one population, evidence from different dates", "THE QUESTION THIS PAGE ANSWERS Who is being left behind People: one population, evidence from different dates The latest", True),
        ("People: one population, evidence from different dates", "Yemen Financial Inclusion Evidence", False),
        ("الأفراد: مجتمع سكاني واحد، وأدلة من تواريخ مختلفة", "أدلة الشمول المايل يف اليمن", False),
        ("Start with the question, not the data.", "Financial inclusion in Yemen is not one number. Yemen Financial Inclusion Evidence is a bilingual public evidence resource", False),
        # the letter-bag matcher of the first D6 pass accepted these two; a title's words must occur in order
        ("Financial inclusion in Yemen is not one number.", "Inspect the evidence behind the answer Yemen Financial Inclusion Evidence is a bilingual public evidence resource that helps users understand, compare and verify evidence on financial inclusion in Yemen", False),
        ("Evidence Readings", "YEMEN FINANCIAL INCLUSION EVIDENCE Financial inclusion in Yemen is not one number. Yemen Financial Inclusion Evidence is a bilingual public evidence resource", False),
    ]
    return [f"title matcher self-test failed: {t!r} on {p[:40]!r} expected {want}" for t, p, want in cases if title_on_page(t, p) is not want]


def check_print(b, base: str, failures: list, evidence: Path | None, tmp: Path) -> int:
    """One route per family printed to PDF in both languages: the first page carries the page title (the print system
    no longer keeps the whole page object together); with PyMuPDF the pages become PNG evidence."""
    try:
        import pymupdf  # type: ignore
    except ImportError:
        pymupdf = None
    n = 0
    for bad in selftest_title_matcher():
        failures.append({"print": "self-test", "failed": [bad]})
    n += 1
    first_pages: dict = {}   # (lang, route) -> (title, page-1 text), for the cross-route negative control
    for lang in ("en", "ar"):
        for route in PRINT_ROUTES:
            ctx = b.new_context(viewport={"width": 794, "height": 1123}); pg = ctx.new_page()
            pg.goto(f"{base}/{lang}{route}", wait_until="load"); pg.wait_for_timeout(150)
            title = pg.evaluate("document.querySelector('h1').textContent.trim()")
            body_text = " ".join(pg.evaluate("document.body.innerText").split())
            pg.emulate_media(media="print"); pg.wait_for_timeout(100)
            dom = pg.evaluate("""() => { const vis=e=>!!e&&getComputedStyle(e).display!=='none'; const hid=s=>!vis(document.querySelector(s));
                return {chrome_hidden: hid('#primary-nav')&&hid('.controls')&&hid('dialog')&&hid('.spine .index')&&hid('.skip'),
                  foot: vis(document.querySelector('.print-foot'))&&/\\/(en|ar)\\//.test(document.querySelector('.print-foot .canon').textContent)&&document.querySelector('.print-foot .cite').textContent.trim().length>0,
                  edition: document.querySelector('.print-foot').textContent.includes(document.querySelector('footer .fine').textContent.split('·').pop().trim()),
                  figures_whole: [...document.querySelectorAll('figure.fig')].every(f=>vis(f.querySelector('.foot .b'))) }; }""")
            tag = f"{(route.strip('/').replace('/', '_') or 'home')}-{lang}"
            pdf = tmp / f"{tag}.pdf"
            pg.pdf(path=str(pdf), format="A4", print_background=False)
            ctx.close()
            first_page_has_title = True
            pages = 0
            if pymupdf:
                doc = pymupdf.open(str(pdf)); pages = doc.page_count
                first_text = doc[0].get_text()
                first_page_has_title = title_on_page(title, first_text)
                first_pages[(lang, route)] = (title, first_text, body_text)
                if evidence:
                    keep = 6 if route.startswith("/readings/") and route != "/readings/" else 2
                    for i, page in enumerate(doc):
                        if i >= keep:
                            break
                        page.get_pixmap(dpi=72).save(str(evidence / f"print-{tag}-p{i + 1}.png"))
            checks = {**dom, "first_page_has_title": first_page_has_title}
            n += len(checks)
            bad = [k for k, v in checks.items() if not v]
            if bad:
                failures.append({"print": route, "lang": lang, "failed": bad, "pages": pages})
            print(f"print  {lang} {route:40s} pages={pages:2d} {'ok' if not bad else 'FAIL ' + str(bad)}")
    # negative control: no route's first page matches another route's title in the same language (the matcher is not
    # so loose that any Arabic page passes); the product name alone is on every page and must never count as a title
    for (lang, route), (title, text, body) in first_pages.items():
        others = [(r2, t2) for (l2, r2), (t2, _, _) in first_pages.items() if l2 == lang and r2 != route and t2.strip() != title.strip()
                  and " ".join(t2.split()) not in body]   # a title the page genuinely prints (the Readings index lists the Readings; a Reading carries its family rubric) is no control
        cross = [r2 for r2, t2 in others if title_on_page(t2, text)]
        n += 1
        if cross:
            failures.append({"print": route, "lang": lang, "failed": ["title_negative_control"], "matches_other_titles": cross})
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=str(REF / "out"))
    ap.add_argument("--only", default="")
    ap.add_argument("--phases", default="contracts,degraded,frames,print", help="comma-separated subset of the four phases (for iteration; the record needs all four)")
    ap.add_argument("--evidence", default="")
    args = ap.parse_args()
    site = Path(args.site)
    if not (site / "en" / "index.html").exists():
        print(f"site not built: {site}"); return 2
    evidence = Path(args.evidence) if args.evidence else None
    if evidence:
        evidence.mkdir(parents=True, exist_ok=True)
    keys = [k for k in args.only.split(",") if k]
    phases = {p.strip() for p in args.phases.split(",") if p.strip()}
    contracts = [c for c in CONTRACTS["visuals"] if not keys or any(k in c["visual_id"] for k in keys)]
    from playwright.sync_api import sync_playwright
    httpd, base = serve(site)
    failures: list = []
    n_checks = n_deg = n_x = n_s = n_p = 0
    crops: set = set()
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page()
        for lang in ("en", "ar"):
            for c in (contracts if "contracts" in phases else []):
                n_checks += check_contract(pg, base, c, lang, failures, evidence, crops)
        # the placeholders on the whole site: exactly the escalated set, only inside the matrix
        seen = set()
        for f in sorted(site.rglob("index.html")):
            if any(part.startswith("_") for part in f.relative_to(site).parts):
                continue
            for m in re.finditer(r"⟦NCC:([^⟧]+)⟧", f.read_text(encoding="utf-8")):
                seen.add(m.group(1))
        if seen - PLACEHOLDERS:
            failures.append({"placeholders_not_escalated": sorted(seen - PLACEHOLDERS)})
        ctx.close()
        if not keys:
            if "degraded" in phases:
                n_deg = check_degraded(b, base, failures)
            if "frames" in phases:
                n_x, n_s = check_frames(b, base, site, failures, evidence)
            if "print" in phases:
                tmp = site / "_review" / "print"; tmp.mkdir(parents=True, exist_ok=True)
                n_p = check_print(b, base, failures, evidence, tmp)
        b.close()
    httpd.shutdown()
    for f in failures:
        print("FAIL", json.dumps(f, ensure_ascii=False))
    (site / "_review_visuals.json").write_text(json.dumps({"contracts": len(contracts), "checks": n_checks, "degraded": n_deg, "export_frames": n_x, "social_frames": n_s, "print_checks": n_p, "placeholders": sorted(seen), "failures": failures}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"VISUALS: {'FAIL' if failures else 'PASS'} — {len(contracts)} contracts × EN/AR on their routes: {n_checks} contract assertions; {n_deg} forced-colours and print checks on the {len(DRAWN)} drawn contracts; "
          f"{n_x} export frames; {n_s} social frames; {n_p} print checks on {len(PRINT_ROUTES)} family routes × EN/AR; placeholders on the site: {sorted(seen)}; {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
