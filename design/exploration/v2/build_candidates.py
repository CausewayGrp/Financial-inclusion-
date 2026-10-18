#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stage B G1 — the direction challenge (charter §10; owner directive 17 October 2026 §9 "G1").

  python3 design/exploration/v2/build_candidates.py --scratch SCRATCH [--fonts FONTS] [A B C D E]

Builds each candidate as a scratch copy of dist/ with one CSS delta (`cand_<X>.css`, this folder) appended to the
shipped stylesheet, then renders the four proving pages (Home, /payments/, /evidence/CLM-001/, /data/) in both
languages at 390 and 1440, served gzip as `dist/_headers` declares, and writes per candidate: first-screen and
full-page PNGs, `<X>_metrics.json` (screens, H1 lines, overflow, fonts loaded, P1 proxies, first-answer and
first-boundary position in phone screens), cold transfer bytes by type, and the disqualifier checks of charter
§10.3 that a stylesheet can fail (HTML and JS byte-identical to dist/; no governed region at zero height; no
horizontal overflow). D is the incumbent (no delta). The candidate fonts (B and E: Markazi Text 600 and IBM Plex
Serif 600, OFL) are read from --fonts, a folder outside the repository until the adopted pair is vendored in G2.

Nothing here touches site-src/, dist/ or the Master. The decision is DL-V2-001 in design/DESIGN_INTEGRATION_V2.md;
the committed evidence is design/evidence/v2/g1/.
"""
from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))

ROUTES = ["/", "/payments/", "/evidence/CLM-001/", "/data/"]
VIEWS = (("ar", 390, 844, True), ("en", 390, 844, False), ("en", 1440, 900, False), ("ar", 1440, 900, False))
CANDIDATE_FONTS = ("MarkaziText-SemiBold.woff2", "IBMPlexSerif-SemiBold-Latin1.woff2")

PAGE_JS = """(vh) => {
  const h1 = document.querySelector('h1'); let h1Lines = null;
  if (h1) { const cs = getComputedStyle(h1); const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2;
            h1Lines = Math.round(h1.getBoundingClientRect().height / lh); }
  const fonts = []; document.fonts.forEach(f => { if (f.status === 'loaded') fonts.push(f.family + ' ' + f.weight); });
  const vis = (sel) => { const e = document.querySelector(sel); if (!e) return false; const r = e.getBoundingClientRect(); return r.top < vh && r.bottom > 0 && r.height > 0; };
  const sc = (e) => e ? Math.round((e.getBoundingClientRect().top + window.scrollY) / vh * 10) / 10 : null;
  const hidden = [...document.querySelectorAll('.bnd, [data-boundary-part], .bound, .cstrip, .page-tools, .topics, .strip')]
    .filter(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.height === 0 || cs.visibility === 'hidden' || cs.display === 'none'; })
    .map(e => e.className || e.tagName);
  return { scrollHeight: document.documentElement.scrollHeight, scrollWidth: document.documentElement.scrollWidth,
           clientWidth: document.documentElement.clientWidth, h1Lines, fonts: [...new Set(fonts)].sort(),
           p1: { figure: vis('.fnum'), clock: vis('.clock'), boundary: vis('[data-boundary-part], .bound, .bnd'), evidence: vis('a[href*="/evidence/"]') },
           firstAnswerScreens: sc(document.querySelector('.fnum') || document.querySelector('.qa.first, #q1')),
           firstBoundaryScreens: sc(document.querySelector('.bnd, .bound')), hiddenGoverned: hidden };
}"""


def build(c: str, scratch: Path, fonts: Path | None) -> Path:
    dst = scratch / "cand" / c
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT / "dist", dst, ignore=shutil.ignore_patterns("static-data", "social"))
    delta = HERE / f"cand_{c}.css"
    if delta.exists():
        css = dst / "assets" / "yfie.css"
        css.write_text(css.read_text(encoding="utf-8") + "\n/* ---- G1 candidate " + c + " ---- */\n" + delta.read_text(encoding="utf-8"), encoding="utf-8")
    if fonts:
        fdir = dst / "assets" / "fonts" / "candidates"
        fdir.mkdir(parents=True, exist_ok=True)
        for f in CANDIDATE_FONTS:
            if (fonts / f).exists():
                shutil.copy(fonts / f, fdir / f)
    return dst


def serve(site: Path):
    import performance_budget as pb
    pb.DIST = site
    srv = pb.serve(pb.parse_headers((site / "_headers").read_text(encoding="utf-8")))
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def measure(c: str, site: Path, out: Path) -> None:
    from playwright.sync_api import sync_playwright
    srv, base = serve(site)
    out.mkdir(parents=True, exist_ok=True)
    metrics, by = {}, {}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for lang, w, h, full in VIEWS:
                for route in ROUTES:
                    ctx = b.new_context(viewport={"width": w, "height": h}, locale=lang, device_scale_factor=1)
                    pg = ctx.new_page()
                    tot = {"total": 0, "font": 0, "css": 0, "html": 0, "js": 0, "other": 0, "font_files": 0}

                    def on_resp(resp, tot=tot):
                        try:
                            n = int(resp.headers.get("content-length") or 0)
                        except ValueError:
                            n = 0
                        u = resp.url
                        k = "font" if u.endswith(".woff2") else "css" if u.endswith(".css") else "js" if u.endswith(".js") else "html" if u.endswith("/") or u.endswith(".html") else "other"
                        tot[k] += n
                        tot["total"] += n
                        if k == "font":
                            tot["font_files"] += 1
                    pg.on("response", on_resp)
                    pg.goto(f"{base}/{lang}{route}", wait_until="networkidle")
                    m = pg.evaluate(PAGE_JS, h)
                    slug = route.strip("/").replace("/", "_") or "home"
                    name = f"{c}_{lang}{w}_{slug}"
                    pg.screenshot(path=str(out / f"{name}.png"))
                    if full:
                        pg.screenshot(path=str(out / f"{name}_full.png"), full_page=True)
                    m["screens"] = round(m["scrollHeight"] / h, 1)
                    m["overflow"] = m["scrollWidth"] > m["clientWidth"]
                    metrics[f"{lang}:{w}:{route}"] = m
                    if w == 390:
                        by[f"{lang}:{route}"] = tot
                    ctx.close()
            b.close()
    finally:
        srv.shutdown()
    same_html = all(_same_tree(ROOT / "dist" / lang, site / lang) for lang in ("ar", "en"))
    same_js = filecmp.cmp(ROOT / "dist" / "assets" / "app.js", site / "assets" / "app.js", shallow=False)
    (out / f"{c}_metrics.json").write_text(json.dumps({"candidate": c, "html_identical_to_dist": same_html, "js_identical": same_js,
                                                        "pages": metrics, "cold_bytes_390": by}, indent=1, ensure_ascii=False), encoding="utf-8")
    for k, v in metrics.items():
        print(f"{c} {k:30} screens {v['screens']:5} h1 {v['h1Lines']} overflow {v['overflow']} first answer {v['firstAnswerScreens']} boundary {v['firstBoundaryScreens']} hidden {v['hiddenGoverned']}")
    for k, v in by.items():
        print(f"{c} {k:30} cold {v['total'] / 1024:6.1f} KB fonts {v['font'] / 1024:6.1f} KB ({v['font_files']})")
    print(f"{c} html identical to dist: {same_html} · app.js identical: {same_js}")


def _same_tree(a: Path, b: Path) -> bool:
    dc = filecmp.dircmp(a, b)
    if dc.diff_files or dc.left_only or dc.right_only:
        return False
    return all(_same_tree(a / s, b / s) for s in dc.subdirs)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scratch", required=True, help="a folder outside the repository")
    ap.add_argument("--fonts", default="", help="folder holding the candidate WOFF2 files (B and E)")
    ap.add_argument("candidates", nargs="*", default=["A", "B", "C", "D", "E"])
    a = ap.parse_args()
    scratch = Path(a.scratch)
    fonts = Path(a.fonts) if a.fonts else None
    for c in a.candidates:
        site = build(c, scratch, fonts)
        measure(c, site, scratch / "shots" / c)


if __name__ == "__main__":
    main()
