#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The display faces' reproducible recipe and coverage record (owner decision OD-1018 D2, 18 October 2026).

  python3 scripts/font_subset.py --naskh-zip NotoNaskhArabic-v2.021.zip     # build the Naskh subset, write the record
  python3 scripts/font_subset.py --check [--naskh-zip ...]                  # the record matches the vendored files;
                                                                            # with the zip, the rebuild is byte-identical

Two display faces ship, one per edition, for titles and section headings only:

- Noto Naskh Arabic SemiBold (600), notofonts/arabic release NotoNaskhArabic-v2.021, the unhinted TTF, subset here to the
  Arabic letters, marks, Arabic punctuation and the few neutral marks Arabic headings use — no Latin letters and no
  Western digits, so a source name, a year or a figure inside an Arabic title falls back to IBM Plex Sans Arabic 600, the
  body face already on the page (figures stay in Western tabular digits from a loaded face). The OFL of this release
  carries no Reserved Font Name, so a subset may keep the family name.
- IBM Plex Serif SemiBold (600), npm @ibm/plex-serif@2.0.0, IBM's own Latin-1 split, copied unchanged (Plex reserves its
  name; the project never subsets a Plex file — vendor/fonts/README.md).

The record `vendor/fonts/display_coverage.json` holds each file's SHA-256 and the code points its cmap covers, so the
standard-library gate `scripts/tests/test_display_font_coverage.py` can check every generated heading without fontTools.
The recipe needs fontTools 4.67.0 and brotli 1.2.0 (not in requirements.txt: the build and the gates never subset).
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor" / "fonts"
RECORD = VENDOR / "display_coverage.json"

NASKH_ZIP_SHA256 = "6c050ab9bd087d69b733c505a7576e60c528c2f33cd7b91005a5bd7da4514032"
NASKH_MEMBER = "NotoNaskhArabic/unhinted/ttf/NotoNaskhArabic-SemiBold.ttf"
NASKH_OUT = VENDOR / "noto-naskh-arabic" / "NotoNaskhArabic-SemiBold-subset.woff2"
SERIF = VENDOR / "ibm-plex-serif" / "IBMPlexSerif-SemiBold-Latin1.woff2"

# Arabic headings only: letters, marks, Arabic punctuation and digits, the bidi controls, and the neutral marks an Arabic
# heading sets between Arabic words (space, no-break space, parentheses, comma, full stop, colon, hyphen and dashes,
# quotation marks, guillemets, ellipsis). No Latin letter, no Western digit.
NASKH_UNICODES = (
    [0x0020, 0x0021, 0x0028, 0x0029, 0x002C, 0x002D, 0x002E, 0x003A, 0x00A0, 0x00AB, 0x00BB]
    + [0x060C, 0x061B, 0x061C, 0x061F] + list(range(0x0621, 0x063B)) + list(range(0x0640, 0x0656))
    + list(range(0x0660, 0x066E)) + [0x0670, 0x0671, 0x06D4]
    + list(range(0x200C, 0x2010)) + list(range(0x2010, 0x2016)) + list(range(0x2018, 0x201E)) + [0x2026]
)
TOOLS = {"fontTools": "4.67.0", "brotli": "1.2.0"}


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def tools() -> None:
    import brotli  # noqa: F401
    import fontTools
    have = {"fontTools": fontTools.version, "brotli": getattr(__import__("brotli"), "__version__", "")}
    for k, v in TOOLS.items():
        if have[k] != v:
            sys.exit(f"font_subset: needs {k} {v}, found {have[k]} (the subset is byte-reproducible only on the pinned tools)")


def build_naskh(zip_path: Path) -> bytes:
    from fontTools import subset
    from fontTools.ttLib import TTFont
    raw = zip_path.read_bytes()
    if NASKH_ZIP_SHA256 != "__FILL__" and sha256(raw) != NASKH_ZIP_SHA256:
        sys.exit(f"font_subset: {zip_path.name} is not the recorded release (sha256 {sha256(raw)})")
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        ttf = z.read(NASKH_MEMBER)
    font = TTFont(io.BytesIO(ttf))
    opts = subset.Options()
    opts.layout_features = ["*"]          # every shaping feature of the kept glyphs (init/medi/fina, rlig, mark, mkmk, calt …)
    opts.flavor = "woff2"
    opts.notdef_outline = True
    opts.recalc_timestamp = False         # the head table keeps the release's timestamp: the output is reproducible
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=NASKH_UNICODES)
    sub.subset(font)
    out = io.BytesIO()
    font.flavor = "woff2"
    font.save(out, reorderTables=True)
    return out.getvalue()


def cmap(data: bytes) -> list[int]:
    from fontTools.ttLib import TTFont
    return sorted(TTFont(io.BytesIO(data)).getBestCmap())


def ranges(cps: list[int]) -> list[str]:
    out, start, prev = [], None, None
    for c in cps:
        if start is None:
            start = prev = c
        elif c == prev + 1:
            prev = c
        else:
            out.append(f"{start:04X}" if start == prev else f"{start:04X}-{prev:04X}"); start = prev = c
    if start is not None:
        out.append(f"{start:04X}" if start == prev else f"{start:04X}-{prev:04X}")
    return out


def record(naskh: bytes, serif: bytes) -> dict:
    return {
        "schema": "YFIE_DISPLAY_COVERAGE/1.0",
        "decision": "OD-1018 D2 (18 October 2026): display faces for titles and section headings, one per edition",
        "faces": {
            "ar": {"family": "Noto Naskh Arabic", "weight": 600, "file": "noto-naskh-arabic/NotoNaskhArabic-SemiBold-subset.woff2",
                   "upstream": "notofonts/arabic release NotoNaskhArabic-v2.021 (16 January 2026), " + NASKH_MEMBER,
                   "upstream_zip_sha256": NASKH_ZIP_SHA256, "recipe": "scripts/font_subset.py (fontTools 4.67.0, brotli 1.2.0)",
                   "licence": "SIL Open Font License 1.1, no Reserved Font Name (noto-naskh-arabic/OFL.txt)",
                   "sha256": sha256(naskh), "bytes": len(naskh), "codepoints": ranges(cmap(naskh)),
                   "fallback": "IBM Plex Sans Arabic 600 for any character outside the subset (Latin letters, Western digits): by design"},
            "en": {"family": "IBM Plex Serif", "weight": 600, "file": "ibm-plex-serif/IBMPlexSerif-SemiBold-Latin1.woff2",
                   "upstream": "npm @ibm/plex-serif@2.0.0 (2 February 2026), fonts/split/woff2/IBMPlexSerif-SemiBold-Latin1.woff2, unchanged",
                   "upstream_integrity": "sha512-xVu9JsC18tBoQF2M6fofpsWrHj5a94saxlOZbYmXoC0E3UfjgS1JlibgrnaUJjnkLlEyCpMgI2PdhkDxijw0gA==",
                   "licence": "SIL Open Font License 1.1, Reserved Font Name \"Plex\" (ibm-plex-serif/LICENSE.txt)",
                   "sha256": sha256(serif), "bytes": len(serif), "codepoints": ranges(cmap(serif)),
                   "fallback": "none expected: the gate fails on any heading character outside this file"},
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--naskh-zip", type=Path)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    tools()
    if a.check:
        rec = json.loads(RECORD.read_text(encoding="utf-8"))
        want = record(NASKH_OUT.read_bytes(), SERIF.read_bytes())
        bad = [k for k in ("ar", "en") if rec["faces"][k] != want["faces"][k]]
        if a.naskh_zip and build_naskh(a.naskh_zip) != NASKH_OUT.read_bytes():
            bad.append("ar rebuild differs from the vendored subset")
        print("DISPLAY FONTS " + ("CURRENT" if not bad else "STALE: " + ", ".join(bad)))
        return 1 if bad else 0
    if not a.naskh_zip:
        ap.error("--naskh-zip is required to build")
    data = build_naskh(a.naskh_zip)
    NASKH_OUT.parent.mkdir(parents=True, exist_ok=True)
    NASKH_OUT.write_bytes(data)
    RECORD.write_text(json.dumps(record(data, SERIF.read_bytes()), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"BUILT {NASKH_OUT.relative_to(ROOT)} {len(data)} bytes sha256 {sha256(data)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
