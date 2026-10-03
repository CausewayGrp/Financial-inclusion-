#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The production build: site-src/content/** -> dist/, through the one renderer (EAD-01).

  python3 scripts/build.py                                   # dist/: the review build every gate reads
  python3 scripts/build.py --out build/site                  # the site as it is published
  python3 scripts/build.py --origin https://causewaygrp.com/financial-inclusion-evidence --out /tmp/site

The public origin may carry a path (owner decision B1: https://causewaygrp.com/financial-inclusion-evidence); the site is
then served under that path. Two outputs, one renderer:

- `dist/` is the review build. Its own links stay root-relative, so every gate serves and reads it at a server root as
  it always has; its discovery addresses (canonical, hreflang, Open Graph, structured data, sitemap) are absolute from
  the origin, path included, as soon as one is set. With no origin (today) it is byte for byte what it was before the
  base path existed.
- `--out DIR` writes the site as it is published: after the pages are written, `scripts/base_path.py` moves every
  root-absolute reference under the origin's base path (nothing, when the origin has none). `--origin URL` builds for
  another origin, for that one build only. site-src/deployment.json and dist/ are not touched.
  `scripts/tests/test_base_path.py` builds the decided origin this way and serves it under the path; the deploy
  workflow publishes this output (docs/RELEASE_RUNBOOK.md, "Hosting").

Writes the complete static site a host serves: every controlled route in both languages as real,
deep-link-safe HTML, the neutral root entry, the bilingual 404, `robots.txt` and — once the owner sets
`public_origin` — `sitemap.xml`. Nothing is rendered in the browser that is not already in the file.

This script composes nothing. Every page is rendered by `scripts/yfie`, the accepted Design implementation:
`content.py` reads the governed projections and the two controlled contracts, `render.py` and `families.py`
compose the eleven page families, `visuals.py` draws the governed visual contracts, `theme.py` is the one
stylesheet and `text.py` the one text layer. `scripts/discovery.py` stays the single implementation of
canonical, hreflang, Open Graph and structured data. The Production Master is never read here and never ships.

The renderer this replaced (the pre-design baseline that composed pages in this file) is removed. What it
printed is frozen in `scripts/tests/baseline_content_oracle.json`, and `scripts/tests/test_cutover_parity.py`
holds this build to it: no governed number lost, no ungoverned number gained, no governed sentence lost.

Assets are copied unchanged, never transformed: the master logo (never redrawn, recoloured, filtered, cropped
or masked — EAD-04), the tools runtime `app.js`, the root-entry `lang-redirect.js`, the IBM Plex faces the
stylesheet declares, from `vendor/fonts/` with their OFL licence (EAD-08), and the governed social images
(EAD-09), which `scripts/social_images.py` rasterises from the design's template because that needs a browser. The review artefacts of the Design
package — content bundles, export frames, social frames — are not part of a hosted site and are written by
`design/reference/build.py`, which renders through this same package.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "site-src"
DIST = ROOT / "dist"
sys.path.insert(0, str(ROOT / "scripts"))
import base_path  # noqa: E402
import discovery  # noqa: E402
from yfie import content as C, render  # noqa: E402

# The faces theme.FONT_FACES declares, and only those: three weights per family (08_ASSET_MAP.md §2). The licence
# ships with each family; the unused files in vendor/ stay unshipped rather than being served and never requested.
FONT_FILES = {
    "ibm-plex-sans": ["IBMPlexSans-Regular.woff2", "IBMPlexSans-Medium.woff2", "IBMPlexSans-SemiBold.woff2", "LICENSE.txt"],
    "ibm-plex-sans-arabic": ["IBMPlexSansArabic-Regular.woff2", "IBMPlexSansArabic-Medium.woff2", "IBMPlexSansArabic-SemiBold.woff2", "LICENSE.txt"],
}


def copy_assets(out: Path) -> None:
    (out / "assets").mkdir(parents=True)
    (out / "static-data").mkdir()
    shutil.copy2(SRC / "assets/CauseWay_Master_Logo.png", out / "assets/CauseWay_Master_Logo.png")   # the social-image template keeps the master
    shutil.copytree(SRC / "assets/logo", out / "assets/logo", ignore=shutil.ignore_patterns("INDEX.json"))   # EAD-03: the web-size derivatives every page serves (scripts/logo_derivatives.py)
    shutil.copy2(SRC / "app.js", out / "assets/app.js")                      # the tools runtime: search, compare, cite, menu, language
    shutil.copy2(SRC / "lang-redirect.js", out / "assets/lang-redirect.js")  # the neutral root entry (F6)
    shutil.copy2(SRC / "content/content/search_index.json", out / "static-data/search_index.json")
    shutil.copy2(SRC / "content/content/search_aliases.json", out / "static-data/search_aliases.json")
    # The governed social images (EAD-09): one 1200x630 PNG per route and language, rasterised from the design's own
    # template by `scripts/social_images.py`, which needs a browser and so runs separately. They are copied, never made
    # here, so this build stays standard-library only and deterministic. `--check` there catches a stale set.
    social = SRC / "assets" / "social"
    (out / "assets/social").mkdir()
    for png in sorted(social.glob("*.png")):
        shutil.copy2(png, out / "assets/social" / png.name)
    for folder, names in FONT_FILES.items():
        (out / "assets/fonts" / folder).mkdir(parents=True)
        for name in names:
            shutil.copy2(ROOT / "vendor/fonts" / folder / name, out / "assets/fonts" / folder / name)
    # B14 b: the host headers (security policy and cache rules) for hosts that read `_headers` from the publish root
    shutil.copy2(SRC / "hosting/_headers", out / "_headers")


def output_dir(arg: str | None) -> Path:
    """dist/ by default. Another directory must be new or empty, and outside the repository's own folders (build/ is
    the exception, and is not tracked), so that a mistyped path can never be emptied by the build."""
    if not arg:
        return DIST
    out = Path(arg).resolve()
    if out == DIST:
        raise SystemExit("--out dist: dist/ is the review build and is written without --out")
    if out == ROOT or ROOT in out.parents and out.relative_to(ROOT).parts[0] != "build":
        raise SystemExit(f"--out {arg}: use dist/ (the default), a folder under build/, or a directory outside the repository")
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise SystemExit(f"--out {arg}: the directory exists and is not empty")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the static site.")
    ap.add_argument("--origin", help="build for this public origin instead of site-src/deployment.json's (this build only)")
    ap.add_argument("--out", help="write the site as published (under the origin's base path) into this new or empty directory")
    args = ap.parse_args(argv)
    if args.origin is not None:
        discovery.override(public_origin=args.origin)
    out = output_dir(args.out)
    if out.exists():
        shutil.rmtree(out)
    copy_assets(out)
    render.assets(out)                       # assets/yfie.css — the one stylesheet, from theme.py
    content = C.load()
    routes = content.routes()
    for lang in ("ar", "en"):
        for route in routes:
            html = render.render(content.page(route, lang), content.shell(lang, route))
            d = out / lang / route.strip("/")
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(html, encoding="utf-8")
    extra = render.render_site_files(out, content)   # the root entry, the bilingual 404, robots.txt, sitemap.xml with an origin
    # B14 a: the data exports are published only when the owner turns the switch on (site-src/deployment.json)
    if discovery.deployment().get("public_downloads") is True:
        exports = ROOT / "build" / "exports"
        if not (exports / "MANIFEST.json").exists():
            raise SystemExit("public_downloads is on but build/exports/ is missing: run python3 scripts/exports.py first")
        shutil.copytree(exports, out / "downloads")
    # Owner decision B1: the published site (--out) is served under the origin's path, so every root-absolute reference
    # moves under it. dist/, the review build, keeps root-relative links; with no path nothing runs at all.
    base = discovery.base_path(discovery.origin()) if out != DIST else ""
    moved = base_path.relocate(out, base)
    where = "" if out == DIST else f" into {out}"
    under = f", served under {base}/ ({moved} files relocated)" if base else ""
    print(f"Built {len(routes) * 2 + extra} HTML files from {len(routes)} controlled page specs{where}{under}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
