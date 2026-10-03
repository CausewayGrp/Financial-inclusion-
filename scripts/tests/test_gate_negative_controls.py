#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every gate re-pointed at the production runtime still fails on the fault it was written to catch (EAD-01).

  python3 scripts/tests/test_gate_negative_controls.py            # all controls
  python3 scripts/tests/test_gate_negative_controls.py --only bread   # the controls whose name contains "bread"

The cutover replaced the pre-design renderer, and the repository validator found its evidence by the baseline's exact
class names and attribute order. Those selectors were re-pointed at the accepted design's hooks — and a re-pointed
selector is worth nothing if it silently matches nothing. So each one is proved here the only way that means anything:
break one thing in the built site, run the validator, and require the gate to say so.

The assertions were never changed to let the cutover pass. These controls are what makes that checkable rather than
claimed: if a future change quietly loosens one, its control stops failing and this test goes red.

Each control copies `dist/`, breaks exactly one thing, runs `scripts/validate.py`, and restores. It needs a built site
(`python3 scripts/build.py`) and it leaves the tree exactly as it found it, including after an interrupt.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"


def run_validator() -> str:
    r = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], capture_output=True, text=True,
                       cwd=ROOT, env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    return r.stdout + r.stderr


def run_content_parity() -> str:
    r = subprocess.run([sys.executable, str(ROOT / "scripts/tests/test_content_parity.py")], capture_output=True, text=True,
                       cwd=ROOT, env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    return r.stdout + r.stderr


# A control may name the gate that must catch it; the default is the repository validator.
GATE_RUNNERS = {"validate": run_validator, "content_parity": run_content_parity}


def sub_once(pattern: str, repl: str):
    return lambda t: re.sub(pattern, repl, t, count=1, flags=re.S)


def replace(old: str, new: str, count: int = 1):
    return lambda t: t.replace(old, new, count) if count else t.replace(old, new)


def duplicate(pattern: str):
    """Insert a second copy of the first match immediately after it."""
    def fn(t: str) -> str:
        m = re.search(pattern, t, re.S)
        if not m:
            raise AssertionError(f"control could not find {pattern!r}")
        return t[:m.end()] + m.group(0) + t[m.end():]
    return fn


def insert_after(anchor: str, fragment: str):
    return lambda t: t.replace(anchor, anchor + fragment, 1)


def full_alt_text(vid: str, lang: str) -> str:
    """A figure's full governed alt text as a page would print it (escaped): summary, label and boundary (A3 / C3)."""
    import html as _h, json as _j   # noqa: PLC0415
    vis = _j.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))["visuals"]
    return _h.escape(next(v for v in vis if v["visual_id"] == vid)["governed"][f"alt_text_{lang}"], quote=False)


# name, the file to break, how to break it, the gate text that must appear.
# The text must be a substring of the real message: several gates interpolate a route or a visual id into the middle of
# theirs, so a control that names the gate and then the wording would never match (found by running these).
# A path under `site-src/` or `scripts/` is a source file; anything else is a page of the built site.
SOURCE_PREFIXES = ("site-src/", "scripts/")
CONTROLS = [
    ("active navigation loses its aria-current", "en/evidence/CLM-001/index.html",
     replace('<a href="/en/evidence/" aria-current="page">', '<a href="/en/evidence/">'),
     "active navigation missing aria-current"),
    ("a record loses its breadcrumb", "en/evidence/CLM-001/index.html",
     sub_once(r'<nav class="crumb".*?</nav>', ""),
     "R4 deep-detail breadcrumb missing"),
    ("a record loses its utility region", "en/evidence/CLM-001/index.html",
     replace('class="util" data-record-id=', 'class="util" data-rec-id='),
     "R4 Evidence Record lacks verify/exit actions"),
    ("a domain answer loses its verification section", "en/people/index.html",
     replace('<section class="qa" id="verify">', '<section class="qa" id="verify-x">'),
     "R4 domain lacks verification next action"),
    ("a page loses its search utility", "en/about/index.html",
     replace("data-search-open", "data-search-x"),
     "S05.2 missing search utility reachable"),
    ("a record's boundary stops being first-load", "en/evidence/CLM-001/index.html",
     replace("data-evidence-boundary-first-load", "data-evidence-boundary-later"),
     "S04.1 Evidence Record structural family mismatch"),
    ("a governed first-load field is dropped", "en/evidence/CLM-002/index.html",
     sub_once(r'<div class="qa" id="q3">.*?</div></div>', '<div class="qa" id="q3"></div>'),
     "S04.1 first-load evidence field missing"),
    ("JSON-LD disagrees with the visible breadcrumb", "en/evidence/CLM-001/index.html",
     replace('>Evidence</a> / <span aria-current="page">', '>Evidence hub</a> / <span aria-current="page">'),
     "F6-G04 breadcrumb data differs"),
    ("a record loses the source reuse boundary", "en/evidence/CLM-001/index.html",
     replace('<p class="rights">', '<p class="rgts">', 0),
     "S04.2 source reuse boundary missing"),
    ("an authored paragraph is printed twice", "en/people/index.html",
     duplicate(r'(?<=<div class="body">)<p>.{120,400}?</p>'),
     "P1-G06 repeated sentence"),
    ("a band boundary is demoted to an answer", "en/people/index.html",
     replace('<section class="bnd" id="s4"', '<section class="qa" id="s4"'),
     "S03 scope count mismatch"),
    ("a governed section is dropped from a domain answer", "en/people/index.html",
     sub_once(r'<section class="qa" id="s2"><div>.*?</div><div class="body">.*?</div></section>', ""),
     "S03 controlled section lost"),
    ("a table header loses its scope", "en/remittances/index.html",
     replace('<th scope="col">', "<th>"),
     "P2-G03 table header cell without scope"),
    # On a VIS- record the governed accessible summary is also the record's own summary, so it renders twice and
    # removing one copy proves nothing; `/remittances/` carries this contract's summary exactly once, in the figure's
    # text alternative. `p` cannot nest, so the first paragraph after the fallback marker is that summary.
    ("a figure loses its governed accessible summary", "en/remittances/index.html",
     sub_once(r'(data-visual-fallback="ordered-text">.*?)<p class="small">.*?</p>', r"\1"),
     "S05.3 governed accessible summary missing"),
    ("a controlled question is dropped from Explore", "en/explore/index.html",
     sub_once(r'<li><div><div class="q">.*?</div></li>', ""),
     "S02 Explore must retain all"),
    ("the /data/ inventory list is unhooked", "en/data/index.html",
     replace("data-public-inventory", "data-public-inv"),
     "P1-G03 /data/ inventory list"),
    ("a source card loses its reuse-terms state", "en/data/index.html",
     replace("data-rights-state", "data-rights-st", 0),
     "P2-G02 /data/ source cards lack their reuse-terms state"),
    ("the featured Reading differs between pages", "en/explore/index.html",
     replace("/en/readings/reforms-newer-than-people-evidence/", "/en/readings/define-what-you-count/"),
     "RP-G03"),
    # The value is printed twice — once as the drawn label, once in the value table — so a control that changes one
    # copy proves nothing. Rounding both is the fault: a governed row value the figure no longer prints anywhere.
    ("a drawn figure rounds a governed row value", "en/remittances/index.html",
     replace("1,329.2", "1,329", 0),
     "does not print its governed row value"),
    ("a drawn label shows a number the contract does not govern", "en/remittances/index.html",
     replace('<text class="val" x="15.20%" y="150.5" text-anchor="start">1,329.2</text>',
             '<text class="val" x="15.20%" y="150.5" text-anchor="start">1,329</text>'),
     "draws a value label that is not a governed value"),
    # The figure declares the fallback on its own element and again on the block that carries it; the gate must read
    # the figure's own attribute, so the control breaks exactly that one.
    ("a drawn figure loses its ordered-text fallback", "en/remittances/index.html",
     replace('<figure class="fig" data-visual-id="VIS-REMITTANCE-MACRO" data-visual-fallback="ordered-text"',
             '<figure class="fig" data-visual-id="VIS-REMITTANCE-MACRO" data-visual-fallback="none"'),
     "drawn without data-visual-fallback"),
    ("a decorative graphic appears outside a governed figure", "en/about/index.html",
     insert_after('<main id="main">', '<svg width="10" height="10"></svg>'),
     "P3-G02 graphic outside a governed visual figure"),
    ("a DOM id is used twice", "en/about/index.html",
     insert_after('<main id="main">', '<div id="page-title"></div>'),
     "duplicate DOM id"),
    # The closing question also names itself in the in-page index and the strip, so only replacing every copy of it
    # actually takes it off the end of the essay.
    ("a Reading no longer ends with its governed question", "en/readings/define-what-you-count/index.html",
     replace("What would change this reading?", "What changes this?", 0),
     "RP-G01 Reading essay does not end"),
    ("a Reading loses its related Readings", "en/readings/define-what-you-count/index.html",
     sub_once(r'(?<=data-reading-related>)(.*?)</section>', "</section>"),
     "RP-G01 a Reading links one or two related Readings"),
    ("og:image names an image the build does not ship", "en/people/index.html",
     replace('content="/assets/social/people__en.png"', 'content="/assets/social/people__xx.png"'),
     "F6-G01 og:image is not this page"),
    ("og:image loses its declared size", "en/people/index.html",
     replace('<meta property="og:image:width" content="1200">', ""),
     "F6-G01 og:image does not declare its governed size"),
    # The runtime's isolation of governed dates and ranges is the renderer's own expression; if the two drift, a value a
    # tool writes into an Arabic page reads differently from one the page was rendered with (the D6 RUNTIME_DEFECT).
    ("the runtime's isolation drifts from the renderer's", "site-src/app.js",
     replace(r"(?<![A-Za-z0-9_-])\d{4}-\d{2}", r"(?<![A-Za-z0-9_-])\d{4}-\d{3}"),
     "the runtime's left-to-right isolation is not the renderer's expression"),
    ("the runtime loses its isolation helper", "site-src/app.js",
     replace("function iso(s){return esc(s).replace(LTR_RUN", "function iso(s){return esc(s).replace(/$^/"),
     "the runtime has no isolation helper"),
    ("the search query stops being URL-addressable", "site-src/app.js",
     replace("function writeSearchUrl(term,type){", "function writeSearchUrlX(term,type){"),
     "missing runtime contract: search query written to the URL"),
    ("the search status hides the true total when hits are capped", "site-src/app.js",
     replace("TF('UI-JS-SEARCH-RESULTS-OF',{n:scored.length,m:matching.length})", "TF('UI-JS-SEARCH-RESULTS',{n:scored.length})"),
     "missing runtime contract: search status with the true total when hits are capped"),
    ("the directory's search stops owning the page address", "en/evidence/index.html",
     replace("data-search-input data-search-url-state", "data-search-input"),
     "the Evidence directory's search does not own the page address"),
    ("an inventory count phrase disagrees with the contract", "en/measurement/index.html",
     insert_after('<div class="body">', "<p>This resource publishes 42 Evidence records, each traced.</p>"),
     "P1-G04 inventory count phrase not from the contract"),
    # Release candidate G4: the behaviours the owner decisions and the RC-3 labels unlocked must stay shipped.
    ("an external link loses its new-tab cue", "en/evidence/CLM-001/index.html",
     replace('<span class="sr-only"> (opens in a new tab)</span>', ""),
     "RC-G4 new-tab link without its cue"),
    ("a retired contract is framed on a domain answer again", "en/reforms/index.html",
     insert_after('<main id="main"', ' data-x=""><figure class="fig" data-visual-id="VIS-CAPITAL-CONTEXT"></figure><span hidden'),
     "RC-G4 retired contract VIS-CAPITAL-CONTEXT framed on"),
    ("a page prints a figure's full alt text, boundary and all", "en/people/index.html",
     insert_after('<p class="small"><b>', full_alt_text("VIS-FINDEX-GAPS", "en")),
     "RC-G4 the full alt text of VIS-FINDEX-GAPS"),
    ("a page loads the 10 MB master logo again", "en/people/index.html",
     replace('src="/assets/logo/CauseWay_logo_40.png"', 'src="/assets/CauseWay_Master_Logo.png"'),
     "RC-G4 a page loads the master logo instead of a derivative"),
    ("a table-only record hides its governed method text again", "en/evidence/VIS-FINDEX-BARRIERS/index.html",
     replace("with adults who do not have an account as the base", "", 0),
     "S04.1 progressive evidence field missing /evidence/VIS-FINDEX-BARRIERS/ en method"),
    ("the reuse terms disappear from /data/", "ar/data/index.html",
     sub_once(r'<p class="small reuse-once" data-reuse-terms>[^<]*</p>', ""),
     "RC-GB B8 the reuse terms are not stated above the source list ar"),
    ("the copied citation stops being the previewed one", "site-src/app.js",
     replace("preview.textContent.replace(/\\s+/g,' ').trim()", "document.title"),
     "RC-GB missing runtime contract: B9 the copied citation is the previewed one"),
    ("the Compare prompt shows whatever is selected", "site-src/app.js",
     replace("prompt.hidden=records.length>=2", "prompt.hidden=false"),
     "RC-G4 missing runtime contract: the Compare prompt"),
    # RC-DATES (owner request, after RC-5): a date, range or dated identifier on an Arabic page displays in the English
    # order only when it is isolated left to right — in markup, or with the Unicode isolates where markup cannot go.
    ("an Arabic page prints a date range outside an isolate", "ar/evidence/CLM-024/index.html",
     replace('<bdi dir="ltr" class="nw">2022–2023</bdi>', "2022–2023"),
     "RC-DATES an Arabic page prints a digit-hyphen-digit run outside an isolate ar/evidence/CLM-024/index.html"),
    ("an Arabic title and social card lose their Unicode isolates", "ar/evidence/CLM-040/index.html",
     replace("\u2066", "", 0),
     "RC-DATES an Arabic page prints a digit-hyphen-digit run outside an isolate ar/evidence/CLM-040/index.html [title]"),
    ("the runtime stops isolating the identifiers it writes", "site-src/app.js",
     replace(".replace(ID_RUN,m=>`<bdi dir=\"ltr\">${m}</bdi>`)", ""),
     "RC-DATES the runtime does not isolate the identifiers it writes"),
    # RC-LAND (Owner Addendum 2, improvement 3): the landscape prints every governed row.
    ("the evidence landscape drops a row", "en/evidence/VIS-EVIDENCE-FRESHNESS/index.html",
     sub_once(r'(<div data-evidence-landscape>.*?)<tr><th scope="row">.*?</tr>', r'\1'),
     "RC-LAND the evidence landscape prints 33 of 34 governed rows en"),
    # RC-PERF (Part B B14 d): a page family that outgrows the byte budget is reported.
    ("a page outgrows the performance budget", "en/data/index.html",
     replace("</main>", "<!--" + __import__("base64").b64encode(__import__("os").urandom(400 * 1024)).decode() + "--></main>"),
     "RC-PERF a cold /en/data page needs"),
    # RC-B12 (Part B B12): a text-first contract's bound table prints its governed numbers.
    ("a bound text-first table prints a number no governed row holds", "en/evidence/VIS-TARGET-RESULT-STATE/index.html",
     sub_once(r'(<div data-text-first-table>.*?)<bdi dir="ltr">1,021</bdi>', r'\1<bdi dir="ltr">1,201</bdi>'),
     "RC-B12 the table's numbers differ from the bound rows en VIS-TARGET-RESULT-STATE"),
    # RC-B13 (Part B B13): every listed source carries its filter keys; an archived copy never claims to be the original.
    ("a listed source loses its year key", "ar/data/index.html",
     sub_once(r'(<article [^>]*data-source-record[^>]*?) data-f-year="[^"]*"', r'\1'),
     "RC-B13 a listed source has no year key ar"),
    ("an archived copy is offered as the original", "en/data/index.html",
     sub_once(r'(<a class="source-locator" href="https://web\.archive\.org/[^"]*"[^>]*>)[^<]*', r'\1Open original source ↗'),
     "RC-B13 an archived copy is offered as the original en"),
    # RC-B15 (Part B B15 d; RC-15): Home links the priorities bound to it.
    ("Home drops a measurement priority bound to it", "ar/index.html",
     replace('href="/ar/measurement/#MA-005"', 'href="/ar/measurement/"', 0),
     "RC-B15 Home (ar) does not link the bound priority MA-005 under the gaps section"),
    # RC-B6 (Part B B6): a Reading page links every priority its bindings name.
    ("a Reading page drops a bound measurement priority", "en/readings/from-rail-to-result-missing-middle/index.html",
     replace('href="/en/measurement/#MA-006"', 'href="/en/measurement/"', 0),   # both links: the card's title and its "Open" link
     "RC-B6 a Reading page does not link its measurement priority en/readings/from-rail-to-result-missing-middle/ MA-006"),
    # RC-NAMES (owner note, 3 October 2026, point 1): no enforcement-decision entity name is published.
    ("an enforcement-decision entity name is published", "en/providers/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>Saddam Express Exchange and Transfers Company</p>'),
     "RC-NAMES an enforcement-decision entity name is published en/providers/index.html Saddam Express Exchange and Transfers Company"),
    # RC-A1 (Owner Addendum 2, A1): the text alternative of a chain figure names only steps the drawing has.
    ("a chain figure's text alternative names a step its drawing lacks", "en/evidence/VIS-PAYMENT-RAILS/index.html",
     sub_once(r'(<div class="alt"[^>]*>.*?<p class="small">)', r'\1The mobile e-money amendment (9 July 2025). '),
     "RC-A1 a chain figure's text alternative names a step its drawing lacks en/evidence/VIS-PAYMENT-RAILS/index.html"),
    # The standing content gate (release candidate, RC-1): a governed sentence dropped from a page, and a number no governed
    # record or contract holds, must each be reported by scripts/tests/test_content_parity.py.
    ("a domain answer drops a governed sentence", "en/people/index.html",
     replace("a gap of 12.55 percentage points", "a gap of percentage points"),
     "TEXT en/people/index.html", "content_parity"),
    ("a page prints an ungoverned number", "ar/people/index.html",
     replace("19.53%", "19.53% (88.8)"),
     "NUMBER ar/people/index.html", "content_parity"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    if not (DIST / "en" / "index.html").exists():
        print("GATE NEGATIVE CONTROLS: FAIL (no built site: run python3 scripts/build.py)")
        return 1
    controls = [c for c in CONTROLS if args.only.lower() in c[0].lower()]
    if not controls:
        print(f"no control matches {args.only!r}")
        return 1

    caught = missed = 0
    with tempfile.TemporaryDirectory(prefix="yfie-gate-controls-") as tmp:
        backup = Path(tmp) / "dist"
        shutil.copytree(DIST, backup)
        try:
            for name, rel, mutate, gate, *runner in controls:
                run_gate = GATE_RUNNERS[runner[0] if runner else "validate"]
                page = (ROOT / rel) if rel.startswith(SOURCE_PREFIXES) else (DIST / rel)
                original = page.read_text(encoding="utf-8")
                note = ""
                try:
                    broken = mutate(original)
                    if broken == original:
                        raise AssertionError("the control changed nothing — its selector no longer matches the page")
                    page.write_text(broken, encoding="utf-8")
                    fired = gate in run_gate()
                except Exception as exc:                 # a control that cannot break the page proves nothing either
                    fired, note = False, f" — {exc}"
                finally:
                    page.write_text(original, encoding="utf-8")
                print(("  CAUGHT      " if fired else "  NOT CAUGHT ") + f"{name}  [{gate}]{note}")
                caught += fired
                missed += not fired
        finally:
            shutil.rmtree(DIST)
            shutil.copytree(backup, DIST)
    print(f"GATE NEGATIVE CONTROLS: {'PASS' if not missed else 'FAIL'} — {caught} of {len(controls)} faults caught")
    return 1 if missed else 0


if __name__ == "__main__":
    raise SystemExit(main())
