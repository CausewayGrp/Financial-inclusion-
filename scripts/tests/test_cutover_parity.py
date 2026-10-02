#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EAD-01 cutover proof: the new production runtime prints everything the pre-design baseline printed.

  python3 scripts/tests/test_cutover_parity.py              # against dist/
  YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_cutover_parity.py

`design/reference/check_content.py` compared the Design reference against the baseline build in `dist/`, because both
renderers existed. EAD-01 removes the baseline renderer, at which point that check would compare a tree with itself.
This is its replacement at equal strength: the baseline's side is frozen in `baseline_content_oracle.json`, and the
same two assertions are made against whichever site is under test.

Per page and language:

1. **No governed number is lost.** Every number the baseline printed in `<main>` is printed by the new runtime, at the
   same multiplicity, except the baseline's decorative two-digit section ordinals (01, 02 …), which are presentation.
2. **No ungoverned number appears.** A number the new runtime prints and the baseline did not must be a governed value:
   a row or derived value of a visual contract (the baseline drew no chart — old gate P3-G02 — and the accepted design
   draws thirteen), a number inside the governed content the loader handed the renderer for that page, or an axis tick
   label of a drawn chart, which is scale presentation and is excluded before counting.
3. **No governed sentence is lost.** Every governed string the loader hands the renderer, which the baseline rendered
   in `<main>`, is rendered by the new runtime — whole, or as its sentences in order where the composition paces a
   paragraph around objects (DEBT-008). The one recorded exception is the governed source intro, printed only where a
   record offers a source card to open (DL-D7-011).

This is a cutover artefact, not a standing gate: it is pinned to the projections it was frozen against, and it says so
rather than passing on a comparison it can no longer make. The standing content gate that follows the Master is
`scripts/tests/test_content_parity.py`.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/tests"))
import content_oracle as CO  # noqa: E402

ORACLE = ROOT / "scripts/tests/baseline_content_oracle.json"
DECORATIVE = re.compile(r"^0\d$")
SENT = re.compile(r"(?<=[.؟?!:;])\s+")
SOURCE_INTRO = "UI-EVID-OPEN-THE-SOURCE-RECORD-HERE"
PINNED = 2   # exit status when the oracle's projections have moved: not a pass, not a content failure (release candidate RC-1)

# The governed-string walk of design/reference/check_content.py, unchanged: which keys of the content bundle carry
# public text (and so must be rendered) and which carry routing, state or machine values (and so must not be counted).
SKIP_KEYS = {"href", "url", "route", "id", "cite_payload", "citation", "meta_description", "canonical_href", "data_href", "compare_href",
             "last_reviewed_iso", "hrefs", "ui_json", "readings_index_href", "parent_href", "mode", "family", "lang", "dir", "closure_state",
             "trace_state", "state", "series", "derived", "kind", "section_id", "order", "active", "other_lang", "edition"}
NUMBER_KEYS = {"id", "citation"}   # the page's own identifier and citation: printed as often as the composition needs


def load_content_module():
    """The one governed-content loader of the production renderer (EAD-01)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from yfie import content   # noqa: PLC0415  (imported here so the module stays importable without the renderer)
    return content


def governed_strings(obj, out: set, key: str = "", min_len: int = 12) -> set:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k not in SKIP_KEYS or (min_len <= 1 and k in NUMBER_KEYS):
                governed_strings(v, out, k, min_len)
    elif isinstance(obj, list):
        for v in obj:
            governed_strings(v, out, key, min_len)
    elif isinstance(obj, str) and len(obj.strip()) >= min_len and not obj.startswith(("/", "http", "UI-", "SRC-", "CLM-", "VIS-", "RV-")):
        out.add(re.sub(r"\s+", " ", obj).strip())
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool) and min_len <= 1:
        out.add(str(obj))
    return out


def governed_visual_numbers() -> set[str]:
    """Values a page may print that the baseline never did: visual-contract rows and derived values, and the numeric
    fragments of governed source identifiers."""
    text = (ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8")
    out = set()
    for x in re.findall(r"\d[\d,]*(?:\.\d+)?", text):
        v = x.replace(",", "").rstrip(".")
        if v:
            out.add(v)
            if re.fullmatch(r"\d+\.0", v):
                out.add(v[:-2])
    ids = " ".join(str(r.get("source_id") or "") for r in json.loads((ROOT / "site-src/content/sources/source_reference_map.json").read_text(encoding="utf-8")))
    tmp = ROOT / "scripts/tests/.ids.html"
    tmp.write_text(f"<main>{ids}</main>", encoding="utf-8")
    try:
        out |= set(CO.BI.nums(str(tmp)))
    finally:
        tmp.unlink()
    return out


def numbers_of(obj) -> set[str]:
    tmp = ROOT / "scripts/tests/.bundle.html"
    tmp.write_text("<main>" + " ".join(sorted(governed_strings(obj, set(), min_len=1))) + "</main>", encoding="utf-8")
    try:
        return set(CO.BI.nums(str(tmp)))
    finally:
        tmp.unlink()


def route_of(rel: str) -> tuple[str, str]:
    """`en/evidence/CLM-003/index.html` → ('en', '/evidence/CLM-003/')."""
    parts = rel.split("/")
    return parts[0], "/" + "/".join(parts[1:-1]) + "/" if len(parts) > 2 else "/"


def main() -> int:
    site = Path(os.environ.get("YFIE_SITE_DIR") or (ROOT / "dist"))
    if not site.is_absolute():
        site = ROOT / site
    oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
    moved = sorted(p for p, h in oracle["projection_sha256"].items() if CO.projection_hashes().get(p) != h)
    if moved:
        print(f"ORACLE PINNED TO OLDER PROJECTIONS: {len(moved)} projection(s) have moved since the freeze:")
        for p in moved[:10]:
            print("   -", p)
        print("   The cutover comparison is no longer the one this oracle can make. Re-read the record before trusting it.")
        print("   The standing content gate is scripts/tests/test_content_parity.py (CI runs it on every push).")
        return PINNED
    if not (site / "en" / "index.html").exists():
        print(f"CUTOVER PARITY: FAIL (site not built: {site})")
        return 1

    content = load_content_module().load()
    framing = {lang: next((r.get(f"label_{lang}") for r in json.loads((ROOT / "site-src/content/content/interface_copy.json").read_text(encoding="utf-8"))
                           if r.get("ui_id") == SOURCE_INTRO), "") for lang in ("en", "ar")}
    governed = governed_visual_numbers()
    built = CO.pages(site)
    bad = 0
    for rel, frozen in sorted(oracle["pages"].items()):
        page_path = built.get(rel)
        if page_path is None:
            print(f"MISSING {rel}: the new runtime does not render this document")
            bad += 1
            continue
        lang, route = route_of(rel)
        page_data = content.page(route, lang)
        a = Counter(frozen["nums"])
        b = Counter(CO.main_numbers(page_path, drop_axis_labels=True))
        page_governed = numbers_of(page_data)
        missing = Counter({k: v for k, v in (a - b).items() if not DECORATIVE.match(k)})
        extra = Counter({k: v for k, v in (b - a).items() if k not in governed and k not in page_governed})
        if missing or extra:
            bad += 1
            print(f"DIFF {rel}: lost from the baseline {dict(missing)} · ungoverned in the new runtime {dict(extra)}")

        gov = governed_strings(page_data, set())
        base_text, new_text = frozen["text"], CO.main_text(page_path)

        def present(x: str) -> bool:
            if x in new_text:
                return True
            parts = [y.strip() for y in SENT.split(x) if y.strip()]
            if len(parts) > 1 and all(y in new_text for y in parts):
                pos = [new_text.index(y) for y in parts]
                return pos == sorted(pos)
            return False

        no_source_card = isinstance(page_data.get("sources"), list) and not page_data["sources"]

        def intro_exempt(x: str) -> bool:
            if not (no_source_card and framing[lang]):
                return False
            return x == framing[lang] or (x in framing[lang] and x not in base_text.replace(framing[lang], ""))

        lost = sorted(x for x in gov if x in base_text and not present(x) and not intro_exempt(x))
        if lost:
            bad += 1
            print(f"TEXT {rel}: {len(lost)} baseline sentence(s) not in the new runtime:")
            for x in lost[:5]:
                print("   -", x[:160])
    print(f"CUTOVER PARITY: {'PASS' if not bad else 'FAIL'} ({len(oracle['pages'])} baseline documents checked, {bad} differing)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
