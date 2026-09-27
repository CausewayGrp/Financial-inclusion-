#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Content-parity check for the reference implementation against the baseline build (`dist/`).

  python3 design/reference/check_content.py [site_dir]

For every document the reference site renders, in both languages:
- every number the baseline prints in <main> must also be printed by the reference (a missing governed number fails),
  except the baseline's decorative two-digit section ordinals (01, 02 …), which are presentation, not content;
- every number the reference prints that the baseline does not must be a governed value: a row value, derived value
  or identifier of a visual contract in `site-src/content/visuals/visual_design_contracts.json` (the baseline draws no
  chart and prints no contract row by rule P3-G02; the reference draws them at their canonical routes); axis tick
  labels of a drawn chart (SVG `<text class="lbl">`) are scale presentation, not content, and are excluded.
Number normalisation is that of audit/tranche_c/checks/bilingual_invariance.py, so the same rules apply. Exit 1 on any
failure. This protects the loader against silent drift from the projections; it is not a design check.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "audit/tranche_c/checks"))
import bilingual_invariance as BI  # noqa: E402

DECORATIVE = re.compile(r"^0\d$")
AXIS_LABEL = re.compile(r'<text class="lbl[^"]*"[^>]*>[^<]*</text>')


def governed_visual_numbers() -> set[str]:
    """Numbers a reference page may print beyond the baseline: visual-contract values and derived values, and the
    numeric fragments of governed source identifiers (a reference printed as a labelled reference is not a figure)."""
    text = (ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8")
    out = set()
    for x in re.findall(r"\d[\d,]*(?:\.\d+)?", text):
        v = x.replace(",", "").rstrip(".")
        if v:
            out.add(v)
            if re.fullmatch(r"\d+\.0", v):
                out.add(v[:-2])
    ids = " ".join(str(r.get("source_id") or "") for r in json.loads((ROOT / "site-src/content/sources/source_reference_map.json").read_text(encoding="utf-8")))
    tmp = ROOT / "design/reference/out/_bundle/.ids.html"
    tmp.write_text(f"<main>{ids}</main>", encoding="utf-8")
    out |= set(BI.nums(str(tmp)))
    tmp.unlink()
    return out


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "design/reference/out")
    governed = governed_visual_numbers()
    bad = 0
    for lang in ("en", "ar"):
        for page in sorted((site / lang).rglob("index.html")):
            rel = page.relative_to(site)
            base = ROOT / "dist" / rel
            if not base.exists():
                print("no baseline for", rel)
                bad += 1
                continue
            stripped = page.parent / ".stripped.html"
            stripped.write_text(AXIS_LABEL.sub("", page.read_text(encoding="utf-8")), encoding="utf-8")
            a, b = BI.nums(str(base)), BI.nums(str(stripped))
            stripped.unlink()
            missing = Counter({k: v for k, v in (a - b).items() if not DECORATIVE.match(k)})
            extra = Counter({k: v for k, v in (b - a).items() if k not in governed})
            if missing or extra:
                bad += 1
                print(f"DIFF {rel}: missing from reference {dict(missing)} · ungoverned in reference {dict(extra)}")
    print(f"CONTENT PARITY: {'PASS' if not bad else 'FAIL'} ({bad} differing documents)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
