#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every generated heading set in a display face is covered by that face (owner decision OD-1018 D2, 18 October 2026).

  python3 scripts/tests/test_display_font_coverage.py              # against dist/
  python3 scripts/tests/test_display_font_coverage.py --control    # and prove it fails on an uncovered character

The stylesheet sets titles and section headings in one display face per edition (scripts/yfie/theme.py, `--font-display`):
every `h1`, every `h2` that is not an eyebrow (`h2.rubric`), and the featured Reading's title on Home, the Readings
index and the Questions hub. This gate reads those texts from every built page of both editions and checks them against the code points
the vendored display files cover, as recorded with their hashes in vendor/fonts/display_coverage.json
(scripts/font_subset.py writes and checks that record; this gate needs only the standard library):

- English: every character must be in IBM Plex Serif SemiBold's Latin-1 file — a miss would fall back to another face.
- Arabic: every Arabic-script character must be in the Noto Naskh Arabic subset. Latin letters, Western digits and the
  punctuation outside the subset fall back to IBM Plex Sans Arabic 600 by design (the subset carries no Latin); they
  are counted, not failed.

It also checks that the record's hashes are the vendored files' hashes, so a replaced font file cannot pass on a stale
record.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "dist"
RECORD = ROOT / "vendor" / "fonts" / "display_coverage.json"
ARABIC = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
HEAD = re.compile(r'<(h1|h2)\b([^>]*)>(.*?)</\1>', re.S)
FEATURED = re.compile(r'<section class="qa[^"]*" id="(?:sf|featured|deeper)">.*?<div class="q">(.*?)</div>', re.S)


def codepoints(ranges: list[str]) -> set[int]:
    out = set()
    for r in ranges:
        a, _, b = r.partition("-")
        out.update(range(int(a, 16), int(b or a, 16) + 1))
    return out


def texts(raw: str) -> list[str]:
    main = raw[raw.find("<main"):raw.find("</main>")] if "<main" in raw else raw
    out = [m.group(3) for m in HEAD.finditer(main) if not re.search(r'class="[^"]*\brubric\b', m.group(2))]
    out += FEATURED.findall(main)
    return [html.unescape(re.sub(r"<[^>]+>", "", t)) for t in out]


def check(extra: dict[str, str] | None = None) -> list[str]:
    rec = json.loads(RECORD.read_text(encoding="utf-8"))
    errors, fallback = [], 0
    cover = {}
    for lang, face in rec["faces"].items():
        f = ROOT / "vendor" / "fonts" / face["file"]
        if hashlib.sha256(f.read_bytes()).hexdigest() != face["sha256"]:
            errors.append(f"{lang}: {face['file']} does not match its recorded hash (run scripts/font_subset.py --check)")
        cover[lang] = codepoints(face["codepoints"])
    pages = 0
    for lang in ("ar", "en"):
        for p in sorted((SITE / lang).rglob("index.html")):
            raw = p.read_text(encoding="utf-8")
            if extra and p.relative_to(SITE).as_posix() in extra:
                raw = raw.replace("</h1>", extra[p.relative_to(SITE).as_posix()] + "</h1>", 1)
            pages += 1
            for t in texts(raw):
                for ch in set(t):
                    if ch.isspace() or ord(ch) < 0x20 or ch in "‎‏⁦⁧⁨⁩":
                        continue
                    if lang == "en" and ord(ch) not in cover["en"]:
                        errors.append(f"en: {p.relative_to(SITE).as_posix()} heading character U+{ord(ch):04X} {ch!r} is not in IBM Plex Serif")
                    elif lang == "ar":
                        if ARABIC.match(ch) and ord(ch) not in cover["ar"]:
                            errors.append(f"ar: {p.relative_to(SITE).as_posix()} heading character U+{ord(ch):04X} {ch!r} is not in the Noto Naskh Arabic subset")
                        elif not ARABIC.match(ch) and ord(ch) not in cover["ar"]:
                            fallback += 1
    if pages < 280:
        errors.append(f"read only {pages} pages")
    print(f"DISPLAY FONT COVERAGE: {pages} pages; Arabic heading characters outside the subset by design (Latin, digits, "
          f"punctuation, falling back to IBM Plex Sans Arabic): {fallback}")
    return sorted(set(errors))


def main() -> int:
    errors = check()
    for e in errors[:40]:
        print("FAIL", e)
    if "--control" in sys.argv:
        caught = [check({"ar/about/index.html": "ٹ"}), check({"en/about/index.html": "ł"})]
        ok = all(any("not in" in e for e in c) for c in caught)
        print("CONTROL " + ("CAUGHT: an uncovered Arabic letter and an uncovered Latin letter both fail" if ok else "NOT CAUGHT"))
        if not ok:
            return 1
    print("DISPLAY FONT COVERAGE " + ("PASS" if not errors else f"FAIL ({len(errors)})"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
