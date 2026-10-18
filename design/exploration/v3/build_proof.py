"""Build and measure the Folio proof variants as CSS deltas over a scratch copy of dist/ (HTML and JS byte-identical).
Variants: D (baseline, nothing appended), T0 (Folio on the incumbent faces), T1 (Folio + Noto Naskh Arabic / Plex Serif),
T2 (Folio + Amiri / Plex Serif). Same views for every variant; first-screen and full-page shots; cold bytes at 390."""
import filecmp
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Maher Farea\Financial-inclusion-")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))
sys.path.insert(0, str(ROOT / "design" / "exploration" / "v2"))
import build_candidates as bc  # noqa: E402

import os
FONTS = Path(os.environ.get("YFIE_G1_FONTS", r"C:\Users\Maher Farea\AppData\Local\Temp\g1\fonts"))   # the G1 candidate files (design/evidence/v2/g1/README.md); not committed
FONT_FILES = ["NotoNaskhArabic-Bold.woff2", "Amiri-Bold.woff2", "IBMPlexSerif-SemiBold-Latin1.woff2"]
DELTAS = {"D": [], "T0": ["folio.css"], "T1": ["folio.css", "faces_T1.css"], "T2": ["folio.css", "faces_T2.css"]}
ROUTES = ["/", "/payments/", "/evidence/CLM-001/", "/data/", "/readings/how-money-reaches-households/", "/methodology/"]
VIEWS = [("ar", 390, 844), ("en", 1440, 900), ("ar", 1440, 900), ("en", 390, 844)]
FULL = {"/", "/evidence/CLM-001/"}


def build(v: str, scratch: Path) -> Path:
    dst = scratch / v
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT / "dist", dst, ignore=shutil.ignore_patterns("static-data", "social"))
    css = dst / "assets" / "yfie.css"
    extra = "".join("\n/* ---- proof " + v + ": " + d + " ---- */\n" + (HERE / d).read_text(encoding="utf-8") for d in DELTAS[v])
    if extra:
        css.write_text(css.read_text(encoding="utf-8") + extra, encoding="utf-8")
    fdir = dst / "assets" / "fonts" / "candidates"
    fdir.mkdir(parents=True, exist_ok=True)
    for f in FONT_FILES:
        shutil.copy(FONTS / f, fdir / f)
    for f in (HERE / "fonts").glob("*.woff2"):   # the subset files made for the proof
        shutil.copy(f, fdir / f.name)
    return dst


def measure(v: str, site: Path, out: Path) -> None:
    from playwright.sync_api import sync_playwright
    srv, base = bc.serve(site)
    out.mkdir(parents=True, exist_ok=True)
    metrics, by = {}, {}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for lang, w, h in VIEWS:
                for route in ROUTES:
                    ctx = b.new_context(viewport={"width": w, "height": h}, locale=lang, device_scale_factor=1)
                    pg = ctx.new_page()
                    tot = {"total": 0, "font": 0, "font_files": 0}

                    def on_resp(resp, tot=tot):
                        try:
                            n = int(resp.headers.get("content-length") or 0)
                        except ValueError:
                            n = 0
                        tot["total"] += n
                        if resp.url.endswith(".woff2"):
                            tot["font"] += n
                            tot["font_files"] += 1
                    pg.on("response", on_resp)
                    pg.goto(f"{base}/{lang}{route}", wait_until="networkidle")
                    pg.wait_for_timeout(250)
                    m = pg.evaluate(bc.PAGE_JS, h)
                    slug = route.strip("/").replace("/", "_") or "home"
                    name = f"{v}_{lang}{w}_{slug}"
                    pg.screenshot(path=str(out / f"{name}.png"))
                    if route in FULL and w == 1440:
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
    same_html = all(bc._same_tree(ROOT / "dist" / lang, site / lang) for lang in ("ar", "en"))
    same_js = filecmp.cmp(ROOT / "dist" / "assets" / "app.js", site / "assets" / "app.js", shallow=False)
    (out / f"{v}_metrics.json").write_text(json.dumps({"variant": v, "html_identical_to_dist": same_html, "js_identical": same_js,
                                                        "pages": metrics, "cold_bytes_390": by}, indent=1, ensure_ascii=False), encoding="utf-8")
    for k, m in metrics.items():
        print(f"{v} {k:34} screens {m['screens']:5} h1 {m['h1Lines']} overflow {m['overflow']} answer {m['firstAnswerScreens']} boundary {m['firstBoundaryScreens']} hidden {m['hiddenGoverned']}")
    for k, t in by.items():
        print(f"{v} {k:34} cold {t['total'] / 1024:6.1f} KB fonts {t['font'] / 1024:6.1f} KB ({t['font_files']})")
    print(f"{v} html identical to dist: {same_html} · app.js identical: {same_js}")


if __name__ == "__main__":
    scratch = Path(sys.argv[1])
    for v in (sys.argv[2:] or list(DELTAS)):
        measure(v, build(v, scratch), scratch / "out")
