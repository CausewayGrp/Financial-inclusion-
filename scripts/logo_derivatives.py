#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Web-size derivatives of the canonical logo (EAD-03; owner decision of 2 October 2026, `audit/OWNER_DECISIONS_2026-10-02.md`).

  python3 scripts/logo_derivatives.py           # write site-src/assets/logo/CauseWay_logo_<px>.png and INDEX.json
  python3 scripts/logo_derivatives.py --check   # every derivative is a pure resample of the unchanged master

The master, `site-src/assets/CauseWay_Master_Logo.png` (6 250 × 6 250 px RGBA), is never altered: its SHA-256 is recorded
in INDEX.json and checked. Each derivative is the whole mark resampled to a square of the listed size with Lanczos
filtering and nothing else — no crop, filter, recolour, mask or matte (`design/08_ASSET_MAP.md` §1: 40, 48 and 72 px at
1× and 2×, and 32 px at 1× and 2× for the export identity line). `--check` decodes every derivative and compares its
pixels with a fresh resample of the master, so a derivative edited by hand, or made from an altered master, fails; the
PNG bytes themselves may differ between Pillow builds, the pixels may not. The 72 px social-image template keeps the
master file, so the 286 governed social images stay byte-identical (`scripts/social_images.py --check`).
"""
from __future__ import annotations

import hashlib
import io
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "site-src/assets/CauseWay_Master_Logo.png"
OUT = ROOT / "site-src/assets/logo"
SIZES = (32, 40, 48, 64, 72, 80, 96, 144)   # 32/40/48/72 px at 1× and 2× (64, 80, 96, 144)


def name(px: int) -> str:
    return f"CauseWay_logo_{px}.png"


def resample(master: Image.Image, px: int) -> Image.Image:
    return master.resize((px, px), Image.Resampling.LANCZOS)


def png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_master() -> tuple[Image.Image, str]:
    raw = MASTER.read_bytes()
    img = Image.open(io.BytesIO(raw))
    img.load()
    if img.size[0] != img.size[1]:
        raise SystemExit(f"master is not square: {img.size}")
    return img.convert("RGBA"), sha(raw)


def write() -> int:
    master, master_sha = load_master()
    OUT.mkdir(parents=True, exist_ok=True)
    index = {"master": {"path": MASTER.relative_to(ROOT).as_posix(), "sha256": master_sha, "size_px": master.size[0]},
             "method": "Pillow LANCZOS resample of the whole RGBA master to a square; PNG, optimize=True; nothing else",
             "rule": "scripts/logo_derivatives.py --check compares each derivative's decoded pixels with a fresh resample",
             "derivatives": []}
    for px in SIZES:
        b = png_bytes(resample(master, px))
        (OUT / name(px)).write_bytes(b)
        index["derivatives"].append({"file": name(px), "px": px, "bytes": len(b), "sha256": sha(b)})
    (OUT / "INDEX.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"LOGO DERIVATIVES WRITTEN: {len(SIZES)} sizes ({', '.join(map(str, SIZES))} px), "
          f"{sum(d['bytes'] for d in index['derivatives']):,} bytes in all; master unchanged ({master_sha[:12]})")
    return 0


def check() -> int:
    master, master_sha = load_master()
    problems = []
    try:
        index = json.loads((OUT / "INDEX.json").read_text(encoding="utf-8"))
    except Exception as exc:   # noqa: BLE001
        print(f"LOGO DERIVATIVES: FAIL (no index: {exc})")
        return 1
    if index["master"]["sha256"] != master_sha:
        problems.append("the master logo differs from the one the derivatives were made from")
    listed = {d["file"] for d in index["derivatives"]}
    on_disk = {p.name for p in OUT.glob("*.png")}
    if listed != {name(px) for px in SIZES} or on_disk != listed:
        problems.append(f"derivative set differs: listed {sorted(listed)}, on disk {sorted(on_disk)}")
    for d in index["derivatives"]:
        p = OUT / d["file"]
        if not p.exists():
            continue
        b = p.read_bytes()
        if sha(b) != d["sha256"]:
            problems.append(f"{d['file']}: bytes differ from INDEX.json")
        got = Image.open(io.BytesIO(b)).convert("RGBA")
        want = resample(master, d["px"])
        if got.size != (d["px"], d["px"]) or got.tobytes() != want.tobytes():
            problems.append(f"{d['file']}: not a pure resample of the master at {d['px']} px")
    if problems:
        print("LOGO DERIVATIVES: FAIL")
        for x in problems:
            print("  -", x)
        return 1
    print(f"LOGO DERIVATIVES CURRENT: {len(SIZES)} pure resamples of the unchanged master ({master_sha[:12]})")
    return 0


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv[1:] else write())
