#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Content parity for a site built by the one renderer, against the frozen pre-design oracle.

  python3 design/reference/check_content.py [site_dir] [--text]

This check compared the reference implementation with the baseline build in `dist/`, because two renderers existed and
each was the other's independent second opinion: every number the baseline printed had to be printed by the reference,
every extra number had to be a governed value, and `--text` required every governed sentence the baseline rendered to
be rendered by the reference too.

EAD-01 removed the baseline renderer. `dist/` is now produced by the same renderer as `design/reference/out/`, so
comparing them would compare a tree with itself and prove nothing. The baseline's side was therefore frozen before it
was removed — `scripts/tests/baseline_content_oracle.json`, the normalised number multiset and rendered text of
`<main>` for all 286 documents as the pre-design renderer gave them at `2f9a93c` — and this check now runs against
that oracle, at the same strength and by the same rules.

The work lives in `scripts/tests/test_cutover_parity.py` so there is one implementation of it. This file keeps the
name and the command the Design package documents. Text parity is no longer optional: `--text` is accepted and
ignored, because the oracle makes both halves of the comparison equally cheap and there is no reason to skip one.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    site = Path(argv[0]).resolve() if argv else ROOT / "design/reference/out"
    env = {**os.environ, "YFIE_SITE_DIR": str(site), "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([sys.executable, str(ROOT / "scripts/tests/test_cutover_parity.py")], cwd=ROOT, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
