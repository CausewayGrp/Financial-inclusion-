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


# name, the page to break, how to break it, the gate text that must appear
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
    ("a figure loses its governed accessible summary", "en/evidence/VIS-FINDEX-GAPS/index.html",
     sub_once(r'<p class="body"><b>[^<]*</b>.*?</p>', ""),
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
    ("a drawn figure rounds a governed row value", "en/remittances/index.html",
     replace("1,329.2", "1,329"),
     "P3-G02 does not print its governed row value"),
    ("a drawn figure loses its ordered-text fallback", "en/remittances/index.html",
     replace('data-visual-fallback="ordered-text"', 'data-visual-fallback="none"'),
     "P3-G02 drawn without data-visual-fallback"),
    ("a decorative graphic appears outside a governed figure", "en/about/index.html",
     insert_after('<main id="main">', '<svg width="10" height="10"></svg>'),
     "P3-G02 graphic outside a governed visual figure"),
    ("a DOM id is used twice", "en/about/index.html",
     insert_after('<main id="main">', '<div id="page-title"></div>'),
     "duplicate DOM id"),
    ("a Reading no longer ends with its governed question", "en/readings/define-what-you-count/index.html",
     replace("What would change this reading?", "What changes this?"),
     "RP-G01 Reading essay does not end"),
    ("a Reading loses its related Readings", "en/readings/define-what-you-count/index.html",
     sub_once(r'(?<=data-reading-related>)(.*?)</section>', "</section>"),
     "RP-G01 a Reading links one or two related Readings"),
    ("an inventory count phrase disagrees with the contract", "en/measurement/index.html",
     insert_after('<div class="body">', "<p>This resource publishes 42 Evidence records, each traced.</p>"),
     "P1-G04 inventory count phrase not from the contract"),
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
            for name, rel, mutate, gate in controls:
                page = DIST / rel
                original = page.read_text(encoding="utf-8")
                try:
                    broken = mutate(original)
                    if broken == original:
                        raise AssertionError("the control changed nothing")
                    page.write_text(broken, encoding="utf-8")
                    fired = gate in run_validator()
                finally:
                    page.write_text(original, encoding="utf-8")
                print(("  CAUGHT      " if fired else "  NOT CAUGHT ") + f"{name}  [{gate}]")
                caught += fired
                missed += not fired
        finally:
            shutil.rmtree(DIST)
            shutil.copytree(backup, DIST)
    print(f"GATE NEGATIVE CONTROLS: {'PASS' if not missed else 'FAIL'} — {caught} of {len(controls)} faults caught")
    return 1 if missed else 0


if __name__ == "__main__":
    raise SystemExit(main())
