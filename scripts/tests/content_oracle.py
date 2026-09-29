# -*- coding: utf-8 -*-
"""The content oracle: what a built site prints, reduced to the two things content parity is made of.

  python3 scripts/tests/content_oracle.py --freeze dist scripts/tests/baseline_content_oracle.json

The production runtime is being cut over from `scripts/build.py` (the pre-design baseline renderer) to the accepted
Design implementation (EAD-01). The two render the same governed truth in different markup, so parity cannot be a
diff of HTML. It is this, per page and language:

- **numbers** — the normalised number multiset of `<main>`, by the rules of
  `audit/tranche_c/checks/bilingual_invariance.py`, so a value the new renderer rounds, truncates or drops is caught;
- **text** — the rendered text of `<main>` (inline tags removed, block tags separated, entities decoded, whitespace
  collapsed), against which a governed string is tested for presence.

`design/reference/check_content.py` computed both sides live, because both renderers existed. After the cutover only
one renderer exists, so the baseline side is frozen here instead: `baseline_content_oracle.json` is the pre-design
build's own answer, taken once, and `test_cutover_parity.py` holds the new runtime to it. The freeze carries the
SHA-256 of every projection it was derived from, so a later Master transaction cannot make the oracle quietly wrong —
the check reports the moved projections and narrows itself to the pages whose governed content still matches, rather
than passing on a comparison it can no longer make.

This module reads a site directory; it never renders. It therefore stays runnable after the baseline renderer is gone.
"""
from __future__ import annotations

import hashlib
import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "audit/tranche_c/checks"))
import bilingual_invariance as BI  # noqa: E402  (one number-normalisation rule for every content check)

INLINE_TAG = re.compile(r"</?(?:bdi|a|b|i|em|strong|span|time|button)\b[^>]*>")   # inline elements add no word break
TAG = re.compile(r"<[^>]+>")
AXIS_LABEL = re.compile(r'<text class="lbl[^"]*"[^>]*>[^<]*</text>')   # a drawn axis tick is scale presentation, not content
PROJECTIONS = "site-src/content"


def main_text(path: Path) -> str:
    """The text of `<main>` as rendered: inline tags removed, block tags separated, entities decoded, space collapsed."""
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"<main[^>]*>(.*)</main>", raw, re.S)
    text = TAG.sub(" ", INLINE_TAG.sub("", m.group(1) if m else raw))
    return re.sub(r"\s+", " ", _html.unescape(text)).strip()


def main_numbers(path: Path, drop_axis_labels: bool = False) -> dict[str, int]:
    """The normalised number multiset of `<main>`, by the bilingual-invariance rules."""
    if not drop_axis_labels:
        return dict(BI.nums(str(path)))
    stripped = path.parent / ".oracle-stripped.html"
    stripped.write_text(AXIS_LABEL.sub("", path.read_text(encoding="utf-8")), encoding="utf-8")
    try:
        return dict(BI.nums(str(stripped)))
    finally:
        stripped.unlink()


def pages(site: Path) -> dict[str, Path]:
    """Every localized document of a built site, keyed by its `<lang>/<route>/index.html` path."""
    out = {}
    for lang in ("en", "ar"):
        for page in sorted((site / lang).rglob("index.html")):
            out[str(page.relative_to(site)).replace("\\", "/")] = page
    return out


def projection_hashes() -> dict[str, str]:
    """The SHA-256 of every governed projection the renderers read, so a frozen oracle knows what it was frozen against."""
    base = ROOT / PROJECTIONS
    return {str(p.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(base.rglob("*.json"))}


def freeze(site: Path, out: Path, note: str) -> int:
    doc = {
        "schema": "YFIE_BASELINE_CONTENT_ORACLE/1.0",
        "what": "What the pre-design baseline renderer printed in <main>, per page and language: the normalised number "
                "multiset and the rendered text. Frozen once; never regenerated from the renderer that replaced it.",
        "note": note,
        "projection_sha256": projection_hashes(),
        "pages": {rel: {"nums": main_numbers(p), "text": main_text(p)} for rel, p in pages(site).items()},
    }
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"FROZE {len(doc['pages'])} documents from {site} into {out.relative_to(ROOT)}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 4 and argv[0] == "--freeze":
        return freeze(Path(argv[1]).resolve(), Path(argv[2]).resolve(), argv[3])
    if len(argv) == 3 and argv[0] == "--freeze":
        return freeze(Path(argv[1]).resolve(), Path(argv[2]).resolve(), "")
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
