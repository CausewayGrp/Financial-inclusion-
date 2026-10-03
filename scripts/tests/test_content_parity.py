#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The standing content gate: every page prints what the Master governs for it, and prints no number the Master does not.

  python3 scripts/tests/test_content_parity.py              # against dist/
  YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_content_parity.py

`scripts/tests/test_cutover_parity.py` proved the EAD-01 cutover against a frozen copy of the pre-design build. That
oracle is pinned to the projections it was frozen against, so the first Master transaction after the cutover moves it
out of reach — by design, it then reports itself pinned instead of passing on a comparison it can no longer make. This
file is the gate that follows the Master from then on (named as such in the cutover test's docstring). It makes the
cutover test's assertions 2 and 3 live, against the governed content the loader hands the renderer today, for every
localized document of the site:

1. **No governed sentence is lost.** Every governed string the loader hands the renderer for a page (the same walk as the
   cutover test: public-text keys only, 12 characters or more) is rendered in `<main>` — whole, or as its sentences in
   order where the composition paces a paragraph around objects (DEBT-008) — for the page's own governed copy (OWN_KEYS:
   title, framing, every section heading and paragraph, and an Evidence Record's governed fields). The one recorded
   exception is the cutover test's (the governed source intro, printed only where a record offers a source card).
2. **No ungoverned number appears.** Every number the page prints in `<main>` (axis tick labels excluded: they are scale
   presentation) is a number inside the governed content the loader handed the renderer for that page, a row or derived
   value of a governed visual contract, or a numeric fragment of a governed identifier; decorative two-digit
   section ordinals are excluded as in the cutover test.

What it does not do — and the cutover test did — is compare with a frozen baseline: a governed change in the Master is
the point of a transaction, so a value that changed in the Master is expected to change on the page. The bilingual
invariance check, the public-literal audit and the validator keep holding the numbers to their records.
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/tests"))
import content_oracle as CO  # noqa: E402
import test_cutover_parity as CP  # noqa: E402  (one implementation of the governed-string walk and the number rules)

# The page's own governed copy: the fields a family renderer must print in <main> for the page itself (its title, framing
# and every governed section), read from these keys at the top of the bundle and inside the subtrees that hold sections.
# Strings of objects a page merely lists (records, visuals, labels, navigation) are not the page's own copy; the
# validator, the bilingual invariance check and the design checks hold those.
OWN_KEYS = {"title", "lead", "question", "thesis", "prohibited_inference", "heading", "paragraphs", "summary", "definition",
            "universe", "period", "method", "does_not_establish", "currentness", "change_trigger", "verification", "measurement_limits"}
SECTION_TREES = {"sections", "primary", "progressive", "band", "list_section"}


# Recorded exceptions: governed copy a family composition does not print, with the reason. Each is pre-existing (the frozen
# pre-design oracle shows it absent too) and listed for the product challenge (audit/release_candidate/PRODUCT_CHALLENGE.md).
NOT_PRINTED = {
    ("/", 2): "Home section 2 (\"Start with the question, not the dataset\") is not printed by the Orientation composition, as in the "
              "pre-design baseline; section 9 carries the starting questions and their instruction (scripts/yfie/render.py home).",
}


def own_copy(page: dict) -> set[str]:
    out: set[str] = set()

    def take(v):
        if isinstance(v, str):
            # a governed paragraph that opens with "> " or "- " is rendered as a pull quote or a list item, without the marker
            CP.governed_strings(v[2:] if v[:2] in ("> ", "- ") else v, out)
        elif isinstance(v, list):
            for x in v:
                take(x)

    def walk(node, depth=0):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in OWN_KEYS:
                    take(v)
                elif k in SECTION_TREES or depth > 0:
                    walk(v, depth + 1)
        elif isinstance(node, list):
            for x in node:
                walk(x, depth)

    walk(page)
    skip = {k[1] for k in NOT_PRINTED if k[0] == page.get("route")}
    for sec in page.get("sections") or []:
        if isinstance(sec, dict) and sec.get("order") in skip:
            for x in [sec.get("heading") or "", sec.get("body") or ""] + list(sec.get("paragraphs") or []):
                out.discard(re.sub(r"\s+", " ", x).strip())
    return out


def id_fragments(page: dict) -> set[str]:
    """Numeric fragments of every governed identifier the bundle carries (CLM-032 → 032 …): printed as references, not as
    statistics; the cutover test admitted them through its baseline."""
    import re   # noqa: PLC0415
    ids: list[str] = []

    def walk(node):
        if isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        elif isinstance(node, str) and re.match(r"^(?:CLM|SRC|VIS|RV|DS|EP|MA|CWR|YSC|REF|OBS|FFO|PB|QE|WB|RMO)-", node):
            ids.append(node)

    walk(page)
    out = set()
    for i in ids:
        for x in re.findall(r"\d+(?:\.\d+)?", i):
            out.add(x)
            out.add(x.lstrip("0") or "0")
    return out


def main() -> int:
    site = Path(os.environ.get("YFIE_SITE_DIR") or (ROOT / "dist"))
    if not site.is_absolute():
        site = ROOT / site
    if not (site / "en" / "index.html").exists():
        print(f"CONTENT PARITY: FAIL (site not built: {site})")
        return 1
    content = CP.load_content_module().load()
    import json   # noqa: PLC0415
    framing = {lang: next((r.get(f"label_{lang}") for r in json.loads((ROOT / "site-src/content/content/interface_copy.json").read_text(encoding="utf-8"))
                           if r.get("ui_id") == CP.SOURCE_INTRO), "") for lang in ("en", "ar")}
    governed_vis = CP.governed_visual_numbers()
    built = CO.pages(site)
    bad = 0
    ui = {r.get("ui_id"): r for r in json.loads((ROOT / "site-src/content/content/interface_copy.json").read_text(encoding="utf-8"))}
    for rel, path in sorted(built.items()):
        lang, route = CP.route_of(rel)
        raw = Path(path).read_text(encoding="utf-8")
        if "data-moved-to=" in raw:
            # RC-19: a retired record address is not a page of its own; it prints exactly its two governed labels and the
            # governed title of the record it leads to, and no number beyond theirs
            import re as _re   # noqa: PLC0415
            target = "/" + _re.search(r'data-moved-to="([^"]+)"', raw).group(1) + "/"
            want = [ui["UI-MOVED-RECORD-TITLE"][f"label_{lang}"], ui["UI-MOVED-RECORD-BODY"][f"label_{lang}"],
                    content.page(target, lang)["title"]]
            text = CO.main_text(path)
            allowed = Counter(n for w in want for n in _re.findall(r"\d+(?:[.,]\d+)*", w))
            printed = Counter(CO.main_numbers(path, drop_axis_labels=True))
            if any(w not in text for w in want) or [k for k in printed if k not in allowed]:
                bad += 1
                print(f"MOVED {rel}: not exactly the governed moved-record text for {target}")
            continue
        try:
            page_data = content.page(route, lang)
        except Exception as exc:   # a built document the loader cannot describe is itself a failure
            print(f"LOADER {rel}: {exc}")
            bad += 1
            continue
        # 2 · no ungoverned number
        printed = Counter(CO.main_numbers(path, drop_axis_labels=True))
        page_governed = CP.numbers_of(page_data) | id_fragments(page_data)
        extra = sorted(k for k in printed if k not in governed_vis and k not in page_governed and not CP.DECORATIVE.match(k))
        if extra:
            bad += 1
            print(f"NUMBER {rel}: printed but not governed for this page: {extra[:12]}")
        # 1 · no governed sentence lost
        text = CO.main_text(path)

        def present(x: str) -> bool:
            if x in text:
                return True
            m = re.fullmatch(r"(.+?):\s*([\d,]+)", x)   # an inventory line "label: N" is a <dt>/<dd> pair
            if m and f"{m.group(1)} {m.group(2)}" in text:
                return True
            parts = [y.strip() for y in CP.SENT.split(x) if y.strip()]
            if len(parts) > 1 and all(y in text for y in parts):
                pos = [text.index(y) for y in parts]
                return pos == sorted(pos)
            return False

        no_source_card = isinstance(page_data.get("sources"), list) and not page_data["sources"]
        lost = []
        for x in sorted(own_copy(page_data)):
            if present(x):
                continue
            if no_source_card and framing[lang] and (x == framing[lang] or x in framing[lang]):
                continue
            lost.append(x)
        if lost:
            bad += 1
            print(f"TEXT {rel}: {len(lost)} governed string(s) not rendered in <main>:")
            for x in lost[:5]:
                print("   -", x[:160])
    print(f"CONTENT PARITY: {'PASS' if not bad else 'FAIL'} ({len(built)} documents checked, {bad} differing)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
