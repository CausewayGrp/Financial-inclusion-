#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stage B G0: audit of every visual contract (BRIEF W4 G0; takeover brief Part 6 item 10: 42 contracts today).

  python3 design/evidence/v2/g0_visuals.py [--out design/evidence/v2/g0] [--site dist]

For each contract in site-src/content/visuals/visual_library.json: the Master's visual_contract_state (06_EVIDENCE_OBJECTS,
read with openpyxl), the routes the contract names, the routes where the built site actually renders its figure
(figure[data-visual-id]), and inside that figure: an SVG, a data table (table.rvtab), a boundary part
([data-boundary-part]) and the words of a withheld / no-values state, in English and in Arabic. Mechanical facts only;
the judgement (is every withheld or empty state justified by a reason that is true today?) is recorded in
design/DESIGN_INTEGRATION_V2.md.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIG = re.compile(r'<figure\b[^>]*data-visual-id="([^"]+)"[^>]*>(.*?)</figure>', re.S)
STATE_WORDS_EN = ("withheld", "held back", "no values", "not drawn", "no governed", "table only", "not yet measured", "not yet available",
                  "no public render", "publishes no value", "cannot yet be built")
STATE_WORDS_AR = ("محجوب", "يُحجب", "لا توجد قيم", "لا تتوفر", "لم تُرسم", "لا قيمة", "جدول فقط", "لم تُقس بعد", "لا ينشر", "غير متاح بعد")
TAG = re.compile(r"<[^>]+>")


def master_states():
    try:
        import openpyxl
    except ImportError:
        return {}
    wb = openpyxl.load_workbook(ROOT / "authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx", read_only=True)
    rows = list(wb["06_EVIDENCE_OBJECTS"].iter_rows(values_only=True))
    h = [str(x) for x in rows[3]]
    ci, cs, cv, cl = h.index("object_id"), h.index("visual_contract_state"), h.index("value_states"), h.index("lineage_state")
    out = {}
    for r in rows[4:]:
        if r and r[0]:
            vs = r[cv] if cv < len(r) else None
            n_values = 0
            if isinstance(vs, str) and vs.startswith("["):
                try:
                    n_values = sum(1 for x in json.loads(vs) if x.get("k") == "v" and x.get("s") in ("READ", "DERIVED"))
                except Exception:
                    n_values = -1
            out[r[0]] = OrderedDict([("visual_contract_state", r[cs] if cs < len(r) else None),
                                     ("lineage_state", r[cl] if cl < len(r) else None), ("bound_values", n_values)])
    return out


def scan(site: Path):
    found = {}
    for lang in ("en", "ar"):
        for html in (site / lang).rglob("index.html"):
            route = "/" + html.parent.relative_to(site / lang).as_posix() + "/"
            route = "/" if route == "/./" else route.replace("//", "/")
            t = html.read_text(encoding="utf-8", errors="replace")
            for vid, body in FIG.findall(t):
                visible = TAG.sub(" ", body)
                low = visible.lower()
                found.setdefault(vid, {}).setdefault(lang, OrderedDict())[route] = OrderedDict([
                    ("svg", "<svg" in body), ("table", "<table" in body),
                    ("boundary", any(k in body for k in ("data-boundary-part", 'class="cap note"', 'class="dis-note"', 'class="isnot"', "does not establish", "لا يثبت", "لا تثبت"))),
                    ("details", "<details" in body),
                    ("state_words", [w for w in (STATE_WORDS_EN if lang == "en" else STATE_WORDS_AR) if w in low or w in visible]),
                    ("chars", len(re.sub(r"<[^>]+>", "", body))),
                ])
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "design/evidence/v2/g0"))
    ap.add_argument("--site", default="dist")
    a = ap.parse_args()
    site = ROOT / a.site
    lib = json.loads((ROOT / "site-src/content/visuals/visual_library.json").read_text(encoding="utf-8"))
    raw = json.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))
    if isinstance(raw, dict):   # the contract file wraps its list in a header object
        raw = next(v for v in raw.values() if isinstance(v, list) and v and isinstance(v[0], dict) and "visual_id" in v[0])
    dc = {d["visual_id"]: d for d in raw}
    ms = master_states()
    rendered = scan(site)
    out = []
    for v in lib:
        vid = v["visual_id"]
        intended = v.get("public_route_list") or []
        if isinstance(intended, str):
            intended = [x.strip() for x in intended.split(";") if x.strip()]
        intended = [r if r.endswith("/") else r + "/" for r in intended]
        tier = dc.get(vid, {}).get("tier")
        if tier and "RETIRE" in str(tier):      # owner decision A5/C4 (2 Oct 2026): retired tiers are excluded from the domain frames
            intended = []
        if vid == "VIS-SOURCE-COMPARISON":      # the Compare tool carries it as a JS table (B12; design/06 section 41)
            cmp = site / "en/evidence/compare/index.html"
            if cmp.exists() and "data-compare-boundary" in cmp.read_text(encoding="utf-8", errors="replace"):
                rendered.setdefault(vid, {}).setdefault("en", OrderedDict())["/evidence/compare/"] = OrderedDict(
                    [("svg", False), ("table", True), ("boundary", True), ("details", False), ("state_words", []), ("chars", 0), ("via", "compare tool")])
        pi = (v.get("prohibited_inference_en") or "")[:50]
        pages_en = {r: (site / "en" / r.strip("/") / "index.html") for r in rendered.get(vid, {}).get("en", {})}
        pi_present = {r: (pi in f.read_text(encoding="utf-8", errors="replace")) for r, f in pages_en.items() if f.exists()} if pi else {}
        en = rendered.get(vid, {}).get("en", {})
        ar = rendered.get(vid, {}).get("ar", {})
        rec_route = f"/evidence/{vid}/"
        row = OrderedDict([
            ("visual_id", vid), ("form", v.get("visual_form")), ("tier", dc.get(vid, {}).get("tier")),
            ("governed", dc.get(vid, {}).get("governed")), ("master", ms.get(vid)),
            ("intended_routes", intended), ("rendered_en", list(en.keys())), ("rendered_ar", list(ar.keys())),
            ("missing_on_intended", [r for r in intended if r not in en]),
            ("record_page_exists", (site / "en/evidence" / vid / "index.html").exists()),
            ("record_page_has_figure", rec_route in en),
            ("record_figure", en.get(rec_route)), ("record_figure_ar", ar.get(rec_route)),
            ("any_svg", any(x["svg"] for x in en.values())), ("any_table", any(x["table"] for x in en.values())),
            ("any_boundary", any(x["boundary"] for x in en.values())),
            ("prohibited_inference_on_page", pi_present),
            ("state_words_en", sorted({w for x in en.values() for w in x["state_words"]})),
            ("state_words_ar", sorted({w for x in ar.values() for w in x["state_words"]})),
            ("en_ar_route_mismatch", sorted(set(en.keys()) ^ set(ar.keys()))),
        ])
        out.append(row)
    extra = [k for k in ms if k.startswith("VIS-") and k not in {v["visual_id"] for v in lib}]
    for vid in extra:                           # visual objects in 06 with no library contract (VIS-FINDEX-BARRIERS)
        out.append(OrderedDict([("visual_id", vid), ("form", None), ("tier", None), ("governed", None), ("master", ms.get(vid)),
                                ("intended_routes", []), ("rendered_en", []), ("rendered_ar", []), ("missing_on_intended", []),
                                ("record_page_exists", (site / "en/evidence" / vid / "index.html").exists()), ("record_page_has_figure", False),
                                ("record_figure", None), ("record_figure_ar", None), ("any_svg", False), ("any_table", False), ("any_boundary", False),
                                ("prohibited_inference_on_page", {}), ("state_words_en", []), ("state_words_ar", []), ("en_ar_route_mismatch", []),
                                ("note", "no contract in visual_library.json; 06 object only")]))
    outdir = Path(a.out)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "g0_visuals.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = ["| Visual | Form | Master state | Bound values | Intended routes | Rendered (EN) | Missing on intended | SVG | Table | Boundary | State words |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in out:
        m = r["master"] or {}
        lines.append(f"| {r['visual_id']} | {r['form']} | {m.get('visual_contract_state')} | {m.get('bound_values')} | {len(r['intended_routes'])} | "
                     f"{len(r['rendered_en'])} | {', '.join(r['missing_on_intended']) or '—'} | {'yes' if r['any_svg'] else 'no'} | "
                     f"{'yes' if r['any_table'] else 'no'} | {'yes' if r['any_boundary'] else 'no'} | {', '.join(r['state_words_en']) or '—'} |")
    (outdir / "g0_visuals.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_missing = sum(1 for r in out if r["missing_on_intended"])
    n_nosvg = sum(1 for r in out if not r["any_svg"])
    n_notable = sum(1 for r in out if not r["any_table"])
    n_nobound = sum(1 for r in out if not r["any_boundary"])
    print(f"G0 VISUALS: {len(out)} contracts; {n_missing} missing on an intended route; {n_nosvg} without an SVG anywhere; "
          f"{n_notable} without a table; {n_nobound} without a boundary part; EN/AR route mismatches: "
          f"{sum(1 for r in out if r['en_ar_route_mismatch'])}")


if __name__ == "__main__":
    main()
