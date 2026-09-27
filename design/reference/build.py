#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Design reference implementation into design/reference/out/ (git-ignored).

  python3 design/reference/build.py                       # accepted renderer (D1: the stress trio only)
  python3 design/reference/build.py --renderer neutral    # the neutral test harness (no stylesheet, no design decisions)
  python3 design/reference/build.py --renderer /abs/path/to/module.py --out /abs/path   # mount a Design prototype renderer

Every renderer receives the same governed content from `yfie.content` (read from site-src/content/**) and the shell; it
never reads a copied content model. The build also writes `out/_bundle/<route>__<lang>.json` — the exact content
structures a renderer receives — so Design prototypes and reviewers can bind the real governed text.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from yfie import content as C  # noqa: E402

TRIO = ["/", "/evidence/CLM-003/", "/readings/same-year-different-number/"]


def load_renderer(name: str):
    if name == "neutral":
        from yfie import neutral
        return neutral
    if name == "accepted":
        from yfie import render
        return render
    spec = importlib.util.spec_from_file_location("prototype_renderer", name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--renderer", default="accepted")
    ap.add_argument("--out", default=str(HERE / "out"))
    ap.add_argument("--routes", default="trio")
    ap.add_argument("--variant", default="")
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    (out / "static-data").mkdir()
    (out / "_bundle").mkdir()
    shutil.copy2(ROOT / "site-src/assets/CauseWay_Master_Logo.png", out / "assets/CauseWay_Master_Logo.png")
    shutil.copy2(ROOT / "site-src/content/content/search_index.json", out / "static-data/search_index.json")
    shutil.copy2(ROOT / "site-src/content/content/search_aliases.json", out / "static-data/search_aliases.json")
    shutil.copy2(ROOT / "site-src/app.js", out / "assets/app.js")   # baseline runtime for the tools (search, cite, language, menu)
    fonts = out / "assets/fonts"
    for folder in ("ibm-plex-sans", "ibm-plex-sans-arabic"):
        shutil.copytree(ROOT / "vendor/fonts" / folder, fonts / folder)   # unchanged files, with LICENSE.txt
    content = C.load()
    renderer = load_renderer(args.renderer)
    if hasattr(renderer, "assets"):
        renderer.assets(out, args.variant)
    routes = TRIO if args.routes == "trio" else [r.strip() for r in args.routes.split(",")]
    written = 0
    for lang in ("ar", "en"):
        shell = content.shell(lang, "/")
        pages = content.trio(lang)
        for route in routes:
            page = pages[route]
            shell = content.shell(lang, route)
            bundle_name = (route.strip("/").replace("/", "_") or "home") + f"__{lang}.json"
            (out / "_bundle" / bundle_name).write_text(json.dumps({"shell": shell, "page": page}, ensure_ascii=False, indent=1), encoding="utf-8")
            html = renderer.render(page, shell, args.variant) if renderer.render.__code__.co_argcount >= 3 else renderer.render(page, shell)
            d = out / lang / route.strip("/")
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(html, encoding="utf-8")
            written += 1
    print(f"Built {written} documents with renderer '{args.renderer}' into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
