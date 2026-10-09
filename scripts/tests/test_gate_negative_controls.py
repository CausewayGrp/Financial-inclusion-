#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every gate re-pointed at the production runtime still fails on the fault it was written to catch (EAD-01).

  python3 scripts/tests/test_gate_negative_controls.py              # all controls, one worker per CPU
  python3 scripts/tests/test_gate_negative_controls.py --only bread   # the controls whose name contains "bread"
  python3 scripts/tests/test_gate_negative_controls.py --jobs 1       # one at a time
  python3 scripts/tests/test_gate_negative_controls.py --shard 2/3    # every third control, from the second (CI matrix)

The cutover replaced the pre-design renderer, and the repository validator found its evidence by the baseline's exact
class names and attribute order. Those selectors were re-pointed at the accepted design's hooks — and a re-pointed
selector is worth nothing if it silently matches nothing. So each one is proved here the only way that means anything:
break one thing in the built site, run the validator, and require the gate to say so.

The assertions were never changed to let the cutover pass. These controls are what makes that checkable rather than
claimed: if a future change quietly loosens one, its control stops failing and this test goes red.

Each control breaks exactly one thing, runs its gate (`scripts/validate.py` unless it names another) and restores. It
needs a built site (`python3 scripts/build.py`). The faults are never made in the repository: each worker gets its own
full copy of the work tree (every file Git tracks or would track, `dist/` included), made before the first fault, and
a fault and its gate run only inside that copy. So the controls run side by side, one per CPU, and none can leak into
another or into the tree. CI splits them across six runners instead (`--shard K/6`, `.github/workflows/verify.yml`):
on its 2-CPU runner two faults side by side took as long as two in a row (owner note of 3 October 2026, 13:00, point 1). Before any fault, the gates run once on every copy and must pass, and no control's
expected message may appear in that clean output: a message the clean tree already prints would prove nothing. The
repository itself is never written, so an interrupt leaves it as it was.
"""
from __future__ import annotations

import argparse
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"


def _run(tree: Path, script: str) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(tree / script)], capture_output=True, text=True, encoding="utf-8",
                       cwd=tree, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1",
                                      "YFIE_SITE_DIR": str(tree / "dist")})
    return r.returncode, r.stdout + r.stderr


# A control may name the gate that must catch it; the default is the repository validator. Each runs inside a copy.
GATE_SCRIPTS = {"validate": "scripts/validate.py", "content_parity": "scripts/tests/test_content_parity.py"}


def tree_files() -> list[str]:
    """The work tree a gate reads: every file Git tracks or would track (not ignored), as it is on disk now."""
    try:
        out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT,
                             capture_output=True, check=True).stdout
        return sorted({p for p in out.decode("utf-8").split("\0") if p and (ROOT / p).is_file()})
    except (OSError, subprocess.CalledProcessError):   # an extracted archive: the same set checksums.py covers there
        sys.path.insert(0, str(ROOT / "scripts"))
        import checksums   # noqa: PLC0415
        return sorted(checksums.tracked_files())


def copy_tree(files: list[str], dest: Path) -> None:
    """A full, independent copy (no hard links: a fault written into a copy can never reach the repository)."""
    for rel in files:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, target)


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


def lineage_label(rid: str, col: int) -> str:
    """A 22_PROVIDERS_DATA lineage label exactly as a renderer would print it (escaped): the bytes such a regression emits.
    The projection site-src/content/data/providers_data.json is non-public lineage: no renderer reads it and the build
    copies only the search files into static-data/ (owner note of 3 October 2026, 13:00, point 3)."""
    import html as _h, json as _j   # noqa: PLC0415
    rows = _j.loads((ROOT / "site-src/content/data/providers_data.json").read_text(encoding="utf-8"))["rows"]
    return _h.escape(str(next(r for r in rows if r and r[0] == rid)[col]), quote=False)


def into_main(fragment_fn):
    """Insert a fragment, computed when the control runs, as the first child of <main>."""
    return lambda t: re.sub(r"(<main[^>]*>)", lambda m: m.group(1) + fragment_fn(), t, count=1)


def full_alt_text(vid: str, lang: str) -> str:
    """A figure's full governed alt text as a page would print it (escaped): summary, label and boundary (A3 / C3)."""
    import html as _h, json as _j   # noqa: PLC0415
    vis = _j.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))["visuals"]
    return _h.escape(next(v for v in vis if v["visual_id"] == vid)["governed"][f"alt_text_{lang}"], quote=False)


def edit_states(oid: str, edit):
    """Change one record's value_states in the projected evidence objects (E2-READ / E2-DATES): `edit` maps the list."""
    import json as _j   # noqa: PLC0415

    def mutate(text):
        objs = _j.loads(text)
        for o in objs:
            if o["object_id"] == oid:
                o["value_states"] = edit(o["value_states"])
        return _j.dumps(objs, ensure_ascii=False, indent=2)
    return mutate


# name, the file to break, how to break it, the gate text that must appear.
# The text must be a substring of the real message: several gates interpolate a route or a visual id into the middle of
# theirs, so a control that names the gate and then the wording would never match (found by running these).
# Source contracts and audit records are rooted in the repository; other paths are under dist/.
SOURCE_PREFIXES = ("site-src/", "scripts/", "audit/", "handoff/")   # audit/: the generated literal closure (E2-DIFF)


def visual_title(vid: str, lang: str) -> str:
    """A title repeats in a figure's heading and table caption: remove every copy for this control."""
    import html, json
    visuals = json.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))["visuals"]
    return html.escape(next(v for v in visuals if v["visual_id"] == vid)["governed"][f"title_{lang}"], quote=False)


CONTROLS = [
    ("portability: Arabic drawing loses its governed title", "ar/remittances/index.html",
     lambda t: t.replace(visual_title("VIS-REMITTANCE-MACRO", "ar"), "missing title"),
     "P3-G02 VIS-REMITTANCE-MACRO drawn without its governed title in ar/remittances/index.html"),
    ("portability: English page has an Arabic placeholder", "en/people/index.html",
     insert_after('<main id="main">', '<input placeholder="\u0628\u062d\u062b">'),
     "P2-G03 Arabic placeholder on an English page en/people/index.html"),
    ("portability: Arabic page has a Latin month", "ar/people/index.html",
     insert_after('<main id="main">', '<p>January</p>'),
     "R85-G08 Latin month name on an Arabic page ar/people/index.html"),
    ("portability: Arabic Findex precision drifts", "ar/people/index.html",
     replace("18.3%", "18.35%"),
     "E2-PREC ar/people/index.html prints a Findex share or gap to two decimals: 18.35"),
    ("portability: Arabic uncertainty becomes unquantified", "ar/people/index.html",
     insert_after('<main id="main">', '<p>\u0644\u0627 \u064a\u064f\u0642\u062f\u064e\u0631 \u0643\u0645\u064a\u064b\u0627 \u0647\u0646\u0627</p>'),
     "FC-MOE ar/people/index.html still says the Findex uncertainty is not quantified"),
    ("portability: context figure reaches Arabic Home", "ar/index.html",
     insert_after('<main id="main">', '<p>35.2% in 19 low-income economies</p>'),
     "E2-CTX ar/index.html prints the low-income context figure on Home"),
    ("portability: Arabic guarantee volume loses its boundary", "ar/firms/index.html",
     replace("\u0644\u0627 \u0639\u062f\u062f \u0627\u0644\u0645\u0646\u0634\u0622\u062a", "guarantee volume", 0),
     "E2-YLG ar/firms/index.html prints the guarantee volume without saying it is not firms' access to finance"),
    ("portability: handoff inventory is stale", "handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json",
     replace('"schema": "YFIE_ROUTE_CONTENT_AND_STATE_INVENTORY/1.3"', '"schema": "broken"'),
     "R86-G02 HANDOFF INVENTORY STALE"),
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
    # The definition (q2) is printed once. Since RC-18 the universe (q3) is also in the record's head (WHEN, then FOR
    # WHOM), so blanking q3 no longer removes a field from first load (found on CI, run 37117577689).
    ("a governed first-load field is dropped", "en/evidence/CLM-002/index.html",
     sub_once(r'<div class="qa" id="q2">.*?</div></div>', '<div class="qa" id="q2"></div>'),
     "S04.1 first-load evidence field missing /evidence/CLM-002/ en definition"),
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
    # The second direction of RC-B13 — a filter must offer an option for every key a listed source carries — was
    # added without a control, so nothing proved it fires. It is the direction that matters most here: it is the
    # gap that let the "used on" filter leave 44 of 158 listed sources, twelve of them curated cards, unreachable
    # under every one of its values while the gate passed. Remove the option and the gate must say so.
    ("a source filter stops offering an option for a key its records carry", "en/data/index.html",
     sub_once(r'(<select data-source-facet="domain">.*?)<option value="none">[^<]*</option>', r'\1'),
     "RC-B13 the domain filter has no option for 'none', so a listed source is unreachable en"),
    # RC-LATEST (Owner Addendum 2, lessons; RC-16): no title or description calls anything "latest" without its date.
    ("a page title calls a measure 'latest' without saying when", "en/people/index.html",
     sub_once(r'(<title>)', r'\1Latest '),
     "RC-LATEST an undated 'latest' in a title or description en/people/index.html"),
    # RC-B15 (Part B B15 d; RC-15): Home links the priorities bound to it; a figure never links its own record page.
    ("Home drops a measurement priority bound to it", "ar/index.html",
     replace('href="/ar/measurement/#MA-005"', 'href="/ar/measurement/"', 0),
     "RC-B15 Home (ar) does not link the bound priority MA-005 under the gaps section"),
    ("a figure links its own record page", "en/evidence/VIS-FINDEX-GAPS/index.html",
     sub_once(r'(<span class="ed">)', r'<a class="canon-l" href="/en/evidence/VIS-FINDEX-GAPS/">Open evidence record</a>\1'),
     "RC-B15 /en/evidence/VIS-FINDEX-GAPS/ links its own figure to itself"),
    # RC-B6 (Part B B6): a Reading page links every priority its bindings name.
    ("a Reading page drops a bound measurement priority", "en/readings/from-rail-to-result-missing-middle/index.html",
     replace('href="/en/measurement/#MA-006"', 'href="/en/measurement/"', 0),   # both links: the card's title and its "Open" link
     "RC-B6 a Reading page does not link its measurement priority en/readings/from-rail-to-result-missing-middle/ MA-006"),
    # RC-NAMES (owner note, 3 October 2026, point 1): no enforcement-decision entity name is published.
    ("an enforcement-decision entity name is published", "en/providers/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>Saddam Express Exchange and Transfers Company</p>'),
     "RC-NAMES an enforcement-decision entity name is published en/providers/index.html PRV-EXCH-E023"),
    # hardened after the RC-17 adversarial review: a short form, a joined spelling, a prefixed or partial Arabic name
    ("an enforcement-decision entity is published by its short form", "en/readings/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>Al-Buraq</p>'),
     "RC-NAMES an enforcement-decision entity name is published en/readings/index.html PRV-EXCH-E022"),
    # RC-NAMES, the 2024 circular (owner decisions of 3 October 2026, point 2): none of its twelve names prints, on a page
    # or in the search index.
    ("a name from the 2024 e-wallet circular is published on a page", "en/payments/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>Floosak</p>'),
     "RC-NAMES a name from the 2024 e-wallet circular is published en/payments/index.html NEG-EW-004"),
    ("a circular name is published joined up", "en/evidence/NEG-EW-011/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>WeCash</p>'),
     "RC-NAMES a name from the 2024 e-wallet circular is published en/evidence/NEG-EW-011/index.html NEG-EW-011"),
    ("a circular name is published with an Arabic proclitic", "ar/payments/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>وجوالي</p>'),
     "RC-NAMES a name from the 2024 e-wallet circular is published ar/payments/index.html NEG-EW-003"),
    ("a circular name is published with its wallet word only", "ar/providers/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>محفظة جيب</p>'),
     "RC-NAMES a name from the 2024 e-wallet circular is published ar/providers/index.html NEG-EW-010"),
    ("a name from the 2024 e-wallet circular enters the search index", "static-data/search_index.json",
     replace('"title_ar": "', '"title_ar": "وي كاش '),
     "RC-NAMES a name from the 2024 e-wallet circular is published static-data/search_index.json NEG-EW-011"),
    # The lineage projection holds the names (owner note of 3 October 2026, 13:00, point 3): a renderer that printed a
    # NEG-EW-011 label, in either language, or a build that copied the projection into the site, must each be caught.
    ("a renderer prints the circular's English lineage label", "en/payments/index.html",
     into_main(lambda: f"<td>{lineage_label('NEG-EW-011', 5)}</td>"),
     "RC-NAMES a name from the 2024 e-wallet circular is published en/payments/index.html NEG-EW-011"),
    ("a renderer prints the circular's Arabic lineage label", "ar/payments/index.html",
     into_main(lambda: f"<td>{lineage_label('NEG-EW-011', 4)}</td>"),
     "RC-NAMES a name from the 2024 e-wallet circular is published ar/payments/index.html NEG-EW-011"),
    ("the provider lineage projection is copied into the built site", "static-data/providers_data.json",
     lambda t: t + (ROOT / "site-src/content/data/providers_data.json").read_text(encoding="utf-8"),
     "RC-NAMES an enforcement-decision entity name is published static-data/providers_data.json"),
    # RC-0950 (owner instructions of 3 October 2026, 09:50, C5 and E1): the reading rule is printed on /methodology/ only;
    # a record's citation is two lines.
    ("a domain answer prints the reading rule under its heading", "en/payments/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p class="small">Every consequential number stays attached to its unit, scope, time and limitation. Evidence measured at different times is never presented as if it described the same moment.</p>'),
     "RC-0950 /en/payments/ prints the reading rule; it belongs on /methodology/ only"),
    ("a record's citation loses its second line", "ar/evidence/CLM-001/index.html",
     sub_once(r'<br><span class="cite-l2" data-cite-line>', r'<span class="cite-l2">'),
     "RC-0950 ar/evidence/CLM-001/index.html the citation is not two lines with the page address ending the first"),
    # RC-NAV (owner decisions of 3 October 2026, point 3): the opened mobile menu carries the trust links, About first.
    ("the mobile menu drops About", "ar/evidence/CLM-002/index.html",
     sub_once(r'(data-menu-trust>.*?)<a href="/ar/about/"[^>]*>[^<]*</a>', r'\1'),
     "RC-NAV ar/evidence/CLM-002/index.html the opened menu does not carry the trust links, About first"),
    # RC-A1 (Owner Addendum 2, A1): the text alternative of a chain figure names only steps the drawing has.
    ("a chain figure's text alternative names a step its drawing lacks", "en/evidence/VIS-PAYMENT-RAILS/index.html",
     sub_once(r'(<div class="alt"[^>]*>.*?<p class="small">)', r'\1The mobile e-money amendment (9 July 2025). '),
     "RC-A1 a chain figure's text alternative names a step its drawing lacks en/evidence/VIS-PAYMENT-RAILS/index.html"),
    # E2-PREC (edition 2, R-11): every Global Findex share and gap a reader sees prints to one decimal place.
    ("a Findex share prints to two decimals again", "en/people/index.html",
     replace("18.3%", "18.35%"),
     "E2-PREC en/people/index.html prints a Findex share or gap to two decimals: 18.35"),
    ("a Findex gap prints to two decimals in a table cell", "ar/evidence/VIS-FINDEX-GAPS/index.html",
     replace(">12.9</bdi></td>", ">12.91</bdi></td>"),
     "E2-PREC ar/evidence/VIS-FINDEX-GAPS/index.html prints a Findex share or gap to two decimals: 12.91"),
    ("a Findex gap prints to two decimals on Home", "en/index.html",
     replace('<b class="fnum">12.9</b>', '<b class="fnum">12.91</b>'),
     "E2-PREC en/index.html prints a Findex share or gap to two decimals: 12.91"),
    # FC-MOE (final content pass, FC-1): the derived interval of a Findex figure is printed, attributed to this
    # resource, and carries its clustering limit. One governed field renders several times on a record page, so each
    # control removes its target everywhere (count=0): a partial loss cannot happen from one governed cell.
    ("a derived Findex interval loses a bound", "en/evidence/CLM-002/index.html",
     replace("from 14.6% to 22.1% for men", "for men", 0),
     "FC-MOE en/evidence/CLM-002/ does not print the derived bound 14.6"),
    ("a derived Findex interval stops saying who derived it", "ar/evidence/CLM-002/index.html",
     replace("\u064a\u0633\u062a\u062e\u0631\u062c\u0647\u0627 \u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0631\u062f",
             "\u0646\u064f\u0634\u0650\u0631\u062a", 0),
     "FC-MOE ar/evidence/CLM-002/ prints a derived interval without saying"),
    ("a derived Findex interval drops its clustering limit", "en/evidence/VIS-FINDEX-GAPS/index.html",
     replace("so clustering is not captured and the true intervals may be wider, never narrower",
             "so the intervals are exact", 0),
     "FC-MOE en/evidence/VIS-FINDEX-GAPS/ prints a derived interval without saying 'clustering is not captured'"),
    ("a page says the Findex uncertainty is not quantified again", "en/evidence/CLM-002/index.html",
     replace("The file open to researchers carries no sampling-unit identifier",
             "The sampling uncertainty is not quantified here", 0),
     "FC-MOE en/evidence/CLM-002/index.html still says the Findex uncertainty is not quantified"),
    # E2-CTX (edition 2, REOPEN-INTL): the low-income context figure is never bare and never on Home.
    ("the low-income context figure loses what it averages", "en/people/index.html",
     replace("across the 19 low-income economies surveyed in it, Yemen among them, is 35.2%",
             "is 35.2%"),
     "E2-CTX en/people/index.html prints the low-income context figure without naming what it averages"),
    ("the low-income context figure reaches Home", "ar/index.html",
     sub_once(r"(<p class=\"sent[^\"]*\">)", r"\1للمقارنة: 35.2% في 19 اقتصادًا منخفض الدخل. "),
     "E2-CTX ar/index.html prints the low-income context figure on Home"),
    # E2-DIFF (edition 2, candidate d): a pair that looks contradictory is explained where it meets, and each number
    # traces to the record that governs it.
    ("a pair that looks contradictory loses its explanation", "en/payments/index.html",
     replace("Why the numbers differ: the January 2025 baseline", "The January 2025 baseline"),
     "E2-DIFF en/payments/index.html does not say why 2,102,484 / 375,252 / FMIIP-BASELINE-2025-01 differ"),
    ("a record stops naming its counterpart", "ar/evidence/CLM-016/index.html",
     lambda t: re.sub(r"\(السجل (?:<bdi[^>]*>)?CLM-009(?:</bdi>)?\)", "", t),
     "E2-DIFF ar/evidence/CLM-016/index.html does not say why CLM-009 differ"),
    ("a pair number traces to its counterpart's record", "audit/PUBLIC_LITERAL_CLOSURE.json",
     sub_once(r'("route": "/reforms/",\s*"surface": "section",\s*"field": "body_en",\s*"token": "2,102,484",\s*"category": "[A-Z_]+",'
              r'\s*"context": "(?:[^"\\]|\\.)*",\s*"source_object": ")CLM-010(")', r"\1FMIIP-BASELINE-2025-01\2"),
     "E2-DIFF 2,102,484 on /reforms/ traces to FMIIP-BASELINE-2025-01, not to CLM-010"),
    # E2-YLG (edition 2, candidate a): a guarantee volume is never shown without its boundary.
    ("the guarantee volume loses its boundary", "en/firms/index.html",
     replace("not how many firms could borrow", "how firms borrowed", 0),
     "E2-YLG en/firms/index.html prints the guarantee volume without saying it is not firms' access to finance"),
    # E2-READ and E2-DATES (owner message of 4 October 2026, block 1): bound is not read; dates are values.
    ("a page prints an event date no record states", "en/reforms/index.html",
     into_main(lambda: "<p>On 17 May 2019 the authority closed the register.</p>"),
     "E2-DATES en/reforms/index.html prints the date 2019-05-17, which no record, event or source states"),
    ("a record's printed date loses its state", "site-src/content/evidence/evidence_objects.json",
     edit_states("CLM-001", lambda vs: [e for e in vs if e["t"] != "7 November 2022"]),
     "E2-DATES CLM-001 summary_en prints the date 2022-11-07 without a stated state in its record"),
    ("a traced value loses its state", "site-src/content/evidence/evidence_objects.json",
     edit_states("CLM-001", lambda vs: [e for e in vs if e["t"] != "11.9%"]),
     "E2-READ /people/ prints '11.9%', traced to CLM-001, which gives it no state"),
    ("a read value loses its locator", "site-src/content/evidence/evidence_objects.json",
     edit_states("CLM-001", lambda vs: [dict(e, loc="") if e["t"] == "11.9%" else e for e in vs]),
     "E2-READ CLM-001 value '11.9%' is READ without a source and locator"),
    ("a value whose original was not opened loses its label", "en/evidence/CLM-049/index.html",
     replace("not been re-read in the original", "been checked", 0),
     "E2-READ en/evidence/CLM-049/ prints"),
    # RC-NOINDEX (owner decision B3): until release every page carries the pre-release noindex meta.
    ("a page loses its pre-release noindex", "en/people/index.html",
     replace('<meta name="robots" content="noindex, nofollow">', ""),
     "RC-NOINDEX en/people/index.html lacks the pre-release noindex, nofollow meta"),
    # RC-1115 (owner note of 3 October 2026, 11:15, 4.1, 4.2, 4.5): the presentation rules RC-18 built, one fault each.
    ("RC-1115: the inline figure emphasis is given box styling", "assets/yfie.css",
     replace("b.fnum{font-weight:700", "b.fnum{padding:18px 16px 16px;font-weight:700"),
     "RC-1115 the inline figure emphasis carries box styling"),
    ("RC-1115: an inline figure is emphasised with the figure frame class (the B.0 defect)", "en/index.html",
     replace('<b class="fnum">', '<b class="fig">'),
     "RC-1115 en/index.html an element other than a figure carries the .fig frame class"),
    ("RC-1115: Home's first figure group loses its emphasised figure", "ar/index.html",
     sub_once(r'(id="s3".*?<p class="sent">[^<]*)<b class="fnum">([^<]*)</b>', r'\1\2'),
     "RC-1115 /ar/ Home's first figure group does not carry an emphasised figure"),
    ("RC-1115: a record's head drops FOR WHOM", "en/evidence/CLM-019/index.html",
     sub_once(r'(<div class="head">.*?</div>)<div class="clock">.*?</div>(<h1)', r'\1\2'),
     "RC-1115 en/evidence/CLM-019/index.html has a q3 section but no FOR WHOM clock before its h1"),
    ("RC-1115: Home section 6 loses the drawn payment chain", "ar/index.html",
     replace('href="/ar/evidence/VIS-PAYMENT-RAILS/"', 'href="/ar/evidence/"', 0),
     "RC-1115 /ar/ Home section 6 does not link the drawn payment chain"),
    ("RC-1115: a page carries a second icon link", "en/about/index.html",
     duplicate(r'<link rel="icon"[^>]*>'),
     "RC-1115 en/about/index.html does not carry exactly one icon link to the 32 px logo"),
    ("RC-1115: the master logo is shipped", "assets/logo/CauseWay_Master_Logo.png",
     lambda t: t + "not a derivative",
     "RC-1115 the master logo is shipped in dist/"),
    ("RC-1115: /measurement/ drops the dimensions from one Arabic card", "ar/measurement/index.html",
     replace("<p data-ma-dimensions>", "<p>"),
     "RC-1115 /measurement/ does not print the dimensions on the same cards with equal counts"),
    # RC-19 (independent review of 70398d1; owner decision of 3 October 2026, 23:54 Aden): FMIIP is never dated to July
    # 2025; a retired record address leads on to its record and nothing links it or keeps its social image; the language
    # switch and the menu are links; only the first sentence's figures are emphasised.
    ("RC-19: FMIIP is dated to July 2025 again", "en/reforms/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<p>The FMIIP, which started in July 2025, has three components.</p>'),
     "RC-19 en/reforms/index.html dates FMIIP to July 2025"),
    ("RC-19: the retired address stops leading to its record", "en/evidence/NEG-EW-011/index.html",
     replace('<meta http-equiv="refresh" content="0;url=/en/evidence/CLM-015/">', ""),
     "RC-19 /en/evidence/NEG-EW-011/ is not the moved-record page for /evidence/CLM-015/"),
    ("RC-19: a page links the retired address", "en/providers/index.html",
     sub_once(r'(<main[^>]*>)', r'\1<a href="/en/evidence/NEG-EW-011/">record</a>'),
     "RC-19 en/providers/index.html still links the retired address /evidence/NEG-EW-011/"),
    ("RC-19: the language switch is a button again", "ar/payments/index.html",
     sub_once(r'<a class="tbtn lang" href="[^"]*" hreflang="en"', '<button type="button" class="tbtn lang"'),
     "RC-19 ar/payments/index.html the language switch or the menu is not a working link"),
    ("RC-19: the coverage figure is emphasised like the finding", "en/index.html",
     replace("Areas holding about 23%", 'Areas holding about <b class="fnum">23%</b>'),
     "RC-19 /en/ Home: a figure after the first sentence is emphasised like the finding"),
    ("RC-19: a social image stands for the retired address", "assets/social/evidence_NEG-EW-011__en.png",
     lambda t: t + "an image",
     "RC-19 a social image still stands for the retired address /evidence/NEG-EW-011/ (en)"),
    # The standing content gate (release candidate, RC-1): a governed sentence dropped from a page, and a number no governed
    # record or contract holds, must each be reported by scripts/tests/test_content_parity.py.
    ("a domain answer drops a governed sentence", "en/people/index.html",
     replace("a gap of 12.5 percentage points", "a gap of percentage points"),
     "TEXT en/people/index.html", "content_parity"),
    ("a page prints an ungoverned number", "ar/people/index.html",
     replace("19.5%", "19.5% (88.8)"),
     "NUMBER ar/people/index.html", "content_parity"),
]


def run_control(tree: Path, control) -> tuple[bool, str, float]:
    """Break one thing in the copy, run the gate that must catch it there, restore the copy. (caught, note, seconds)"""
    name, rel, mutate, gate, *runner = control
    script = GATE_SCRIPTS[runner[0] if runner else "validate"]
    page = tree / rel if rel.startswith(SOURCE_PREFIXES) else tree / "dist" / rel
    started = time.monotonic()
    existed = page.exists()            # a control may add a file the build never writes; it is removed afterwards
    original_bytes = page.read_bytes() if existed else b""
    original = original_bytes.decode("utf-8")
    note = ""
    try:
        broken = mutate(original)
        if broken == original:
            raise AssertionError("the control changed nothing — its selector no longer matches the page")
        page.write_text(broken, encoding="utf-8", newline="\n")
        rc, output = _run(tree, script)
        fired = rc != 0 and gate in output
    except Exception as exc:                 # a control that cannot break the page proves nothing either
        fired, note = False, f" — {exc}"
    finally:
        if existed:
            page.write_bytes(original_bytes)
        else:
            page.unlink(missing_ok=True)
    return fired, note, time.monotonic() - started


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="run only the controls whose name contains this text")
    ap.add_argument("--jobs", type=int, default=0, help="workers, each on its own copy of the tree (default: one per CPU)")
    ap.add_argument("--shard", default="1/1", help="K/N: run every N-th control, starting from the K-th (a CI matrix)")
    args = ap.parse_args()
    if not (DIST / "en" / "index.html").exists():
        print("GATE NEGATIVE CONTROLS: FAIL (no built site: run python3 scripts/build.py)")
        return 1
    try:
        k, n = (int(x) for x in args.shard.split("/"))
        assert 1 <= k <= n
    except (ValueError, AssertionError):
        print(f"--shard takes K/N with 1 <= K <= N, not {args.shard!r}")
        return 1
    controls = [c for i, c in enumerate(CONTROLS) if args.only.lower() in c[0].lower() and i % n == k - 1]
    if not controls:
        print(f"no control matches {args.only!r} in shard {args.shard}")
        return 1
    jobs = max(1, min(args.jobs or os.cpu_count() or 1, len(controls)))
    started = time.monotonic()
    files = tree_files()

    with tempfile.TemporaryDirectory(prefix="yfie-gate-controls-") as tmp:
        trees = [Path(tmp) / f"tree-{w}" for w in range(jobs)]
        with ThreadPoolExecutor(jobs) as pool:
            list(pool.map(lambda d: copy_tree(files, d), trees))
            # The clean copies first: every gate a control relies on passes there, and no expected message is printed.
            scripts = sorted({GATE_SCRIPTS[c[4] if len(c) > 4 else "validate"] for c in controls})
            clean = list(pool.map(lambda job: (job, _run(*job)), [(trees[i % jobs], s) for i, s in enumerate(scripts)]))
        baseline_bad = False
        for (tree, script), (rc, out) in clean:
            if rc != 0:
                baseline_bad = True
                print(f"  CLEAN COPY FAILS  {script} — the copy of the tree does not pass before any fault:")
                print("    " + "\n    ".join(out.strip().splitlines()[-15:]))
            for c in controls:
                if GATE_SCRIPTS[c[4] if len(c) > 4 else "validate"] == script and c[3] in out:
                    baseline_bad = True
                    print(f"  PRINTED CLEAN     {c[0]}  [{c[3]}] — the clean tree already prints this message")
        if baseline_bad:
            print("GATE NEGATIVE CONTROLS: FAIL — the clean copies are not clean, so no fault could be proved")
            return 1
        print(f"  {len(controls)} controls on {jobs} isolated copies of the tree ({len(files)} files each); clean copies pass",
              flush=True)

        free: queue.Queue[Path] = queue.Queue()
        for d in trees:
            free.put(d)

        def task(control):
            tree = free.get()
            try:
                return run_control(tree, control)
            finally:
                free.put(tree)

        results = [None] * len(controls)
        with ThreadPoolExecutor(jobs) as pool:
            futures = {pool.submit(task, c): i for i, c in enumerate(controls)}
            for done, fut in enumerate(as_completed(futures), 1):
                i = futures[fut]
                results[i] = fut.result()
                print(f"  [{done}/{len(controls)}] {'caught' if results[i][0] else 'NOT CAUGHT'}: {controls[i][0]}", flush=True)

    caught = missed = 0
    for (name, _rel, _mutate, gate, *_), (fired, note, secs) in zip(controls, results):
        print(("  CAUGHT      " if fired else "  NOT CAUGHT ") + f"{name}  [{gate}]{note}  ({secs:.0f} s)")
        caught += fired
        missed += not fired
    print(f"GATE NEGATIVE CONTROLS: {'PASS' if not missed else 'FAIL'} — {caught} of {len(controls)} faults caught "
          f"(shard {args.shard} of all {len(CONTROLS)} controls, {jobs} workers, {time.monotonic() - started:.0f} s)")
    return 1 if missed else 0


if __name__ == "__main__":
    raise SystemExit(main())
