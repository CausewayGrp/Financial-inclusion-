#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete-binding check for the reference implementation (D4).

  python3 design/reference/check_binding.py [--site design/reference/out]

Proves, from the repository's own inventory, that the one content path binds exactly what the projection roles allow:
every RENDER and CONTRACT projection is read by `yfie/content.py` (or shipped unchanged for the runtime by `build.py`);
no REFERENCE or VIA_SPEC projection is read by any reference module; a STRUCTURE projection is read by the content
path only. Then that the built site holds every document the inventory counts (286 edition pages + the root entry +
the 404), one bundle per edition page, and no copied content model beyond the two files the runtime fetches. Exit 1 on
any failure. Proof for the record, not authority; design/COVERAGE.csv cites this tool's output.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REF = ROOT / "design" / "reference"
RUNTIME_STATIC = {"content/search_index.json", "content/search_aliases.json"}   # fetched by site-src/app.js as /static-data/*


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=str(REF / "out"))
    args = ap.parse_args()
    site = Path(args.site)
    inv = json.loads((ROOT / "handoff" / "ROUTE_CONTENT_AND_STATE_INVENTORY.json").read_text(encoding="utf-8"))
    roles = inv["projection_roles"]["files"]
    counts = inv.get("counts", {})
    content_src = (REF / "yfie" / "content.py").read_text(encoding="utf-8")
    build_src = (REF / "build.py").read_text(encoding="utf-8")
    other_src = "".join((REF / "yfie" / n).read_text(encoding="utf-8") for n in ("render.py", "families.py", "visuals.py", "theme.py", "neutral.py") if (REF / "yfie" / n).exists())
    bad: list[str] = []
    named = lambda f, src: (f in src) or (Path(f).name in src)  # noqa: E731
    for f, role in sorted(roles.items()):
        in_content, in_build, in_other = named(f, content_src), named(f, build_src), named(f, other_src)
        if role in ("RENDER", "CONTRACT") and not (in_content or (in_build and f in RUNTIME_STATIC)):
            bad.append(f"{role} projection not bound: {f}")
        if role in ("REFERENCE", "VIA_SPEC") and (in_content or in_build or in_other):
            bad.append(f"{role} projection must never be read, but is named: {f}")
        if role == "STRUCTURE" and (in_other or in_build):
            bad.append(f"STRUCTURE projection read outside the content path: {f}")
        if in_other:
            bad.append(f"a renderer reads a projection directly (only the content path may): {f}")
    # the built site: every document, one bundle per edition page, no copied content model
    docs = sorted(p for p in site.rglob("index.html") if p.parent != site and "_review" not in p.parts and "_bundle" not in p.parts)
    edition_pages = [p for p in docs if p.relative_to(site).parts[0] in ("en", "ar")]
    n_spec = int(counts.get("page_specs", 143))
    if len(edition_pages) != 2 * n_spec:
        bad.append(f"edition pages built {len(edition_pages)}, expected {2 * n_spec}")
    for name in ("index.html", "404.html", "robots.txt"):
        if not (site / name).exists():
            bad.append(f"missing {name}")
    bundles = list((site / "_bundle").glob("*.json"))
    if len(bundles) != 2 * n_spec:
        bad.append(f"bundles {len(bundles)}, expected {2 * n_spec}")
    shipped = sorted(str(p.relative_to(site)) for p in site.rglob("*.json") if "_bundle" not in p.parts and "_review" not in p.parts and not p.name.startswith("_review"))
    allowed = {"static-data/search_index.json", "static-data/search_aliases.json"}
    extra = [s for s in shipped if s not in allowed]
    if extra:
        bad.append(f"copied content shipped beyond the runtime's two files: {extra}")
    for lang in ("en", "ar"):
        for p in edition_pages:
            rel = p.relative_to(site)
            if rel.parts[0] == lang:
                twin = site / ("ar" if lang == "en" else "en") / Path(*rel.parts[1:])
                if not twin.exists():
                    bad.append(f"no twin edition for {rel}")
    for b in bad:
        print("FAIL", b)
    print(f"BINDING: {'FAIL' if bad else 'PASS'} — {len(roles)} projections by role, {len(edition_pages)} edition pages + root + 404, {len(bundles)} bundles, shipped data {sorted(allowed & set(shipped))}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
