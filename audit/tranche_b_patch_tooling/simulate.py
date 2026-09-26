# -*- coding: utf-8 -*-
"""PROPOSED-PATCH VALIDATION (simulation). Applies every SUBSTR patch, in patch-ID order,
to a copy of the Master cell text and scans for residual forbidden strings and collisions."""
import json, glob, os, re, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from pdefs_p2 import P2
from pdefs_p3 import P3
from pdefs_p4 import P4
SCR = os.path.dirname(os.path.abspath(__file__)); M = os.environ.get("YFI_MASTER_JSON", f"{SCR}/master")
sheets = {os.path.basename(f)[:-5]: json.load(open(f)) for f in sorted(glob.glob(f"{M}/*.json")) if not f.endswith("_index.json")}
subs = sorted([d for d in P2 + P3 + P4 if d["op"] == "SUBSTR"], key=lambda d: d["pid"])
lost = []
for d in subs:
    applied = 0
    for sh, recs in sheets.items():
        if d.get("sheets") and sh not in d["sheets"]: continue
        for r in recs:
            if d.get("rows") and (sh, r["_row"]) not in d["rows"]: continue
            for k, v in list(r.items()):
                if k == "_row" or not isinstance(v, str): continue
                if d.get("fields") and k not in d["fields"]: continue
                if d["old"] in v:
                    r[k] = v.replace(d["old"], d["new"]); applied += 1
    if applied == 0: lost.append(d["pid"])
print("patches whose old text was already consumed by an earlier patch (collision):", lost or "none")
from sweeps import sweep, apply_ops
from sweeps import rid
sw_rows, sw_keeps, sw_ops = sweep(sheets, rid)
miss = apply_ops(sheets, sw_ops)
print(f"sweeps: {len(sw_ops)} per-cell edits applied; before-text not found exactly once: {len(miss)}")
_pub = [(sh, r) for sh, recs in sheets.items() if sh not in {"36_SUPPLEMENT_ARCHIVE","30_FCS_CONTEXT","29_OECD_BENCHMARKS","25_FINDEX_BASELINE","16_DATASET_CATALOG","28_METHODS_RIGHTS"} for r in recs]
for root, pat in (("PB-0413", r"ادعا"), ("PB-0414", r"منظومة"), ("PB-0415", r"\b[Tt]he (system|product)\b")):
    resid = sum(len(re.findall(pat, v)) for sh, r in _pub for k, v in r.items() if k != "_row" and isinstance(v, str))
    kc = sum(1 for k in sw_keeps if k[0] == root)
    print(f"  {root}: residual occurrences after sweep = {resid}; KEEP-register entries = {kc}; {'MATCH' if resid == kc else 'MISMATCH'}")

FORBID = {
 "EN 'observed history' (remittance evidence-state upgrade)": r"observed history",
 "AR «تاريخ مرصود»": r"تاريخ مرصود",
 # Acceptance correction A: the OECD/INFE 2023 Yemen values are verified and published survey-scoped; only a ranking stays forbidden.
 "OECD 'lowest among participating' ranking": r"lowest (score )?among participating|أدنى نتيجة بين البلدان",
 "unattributed 'active savers' (EN)": r"(?<!“)\b3\.3 million active savers",
 "unattributed «مدخر نشط» (AR, without guillemets)": r"مليون مدخر نشط|ملايين مدخر نشط",
 "'divergence' claim wording (excluding IDs/slugs/other claim types)": r"points to a divergence|available divergence|divergence across distinct|divergent nominal",
 "AR «تباعد» claim wording": r"إلى تباعد|التباعد المتاح|هذا التباعد|يُظهر التباعد",
 "leaked authoring instruction": r"Use the documented system chronology|استخدم السلسلة الزمنية الموثقة|Present them as filterable|تُعرض كبنود قابلة للتصفية",
 "six-figure BOP precision": r"3\.42216",
 "unqualified 'official CBY' roster": r"The official CBY 20\d\d roster|القائمة الرسمية للبنك المركزي لعام",
 "YPCC as «مركز»": r"مركز اليمن للمقاصة",
 "backend voice 'The system controls'": r"The system controls",
 "CCY rendered as local currency": r"من العملة المحلية",
 "unexplained 'CCY 7.4bn'": r"CCY 7\.4bn",
 "'measure in the system' (flagship sentence)": r"measure(s)? (available )?in the system",
 "calque «صفًا مصرفيًا / صفًا للبنوك»": r"صفًا مصرفيًا|صفًا للبنوك",
 "calque «كائن/كائنات», «منزوع الازدواج», «الكون»": r"كائن|منزو[عَ]+ الازدواج|منزوعة الازدواج|الكون",
 "'bounded directional signal'": r"bounded directional signal|إشارة اتجاهية",
 "OECD review 'reports' (unread text)": r"The OECD financial-sector review reports|يعرض استعراض OECD للقطاع المالي",
}
EXEMPT_FIELDS = {"route", "slug", "instance_id", "visual_id", "claim_id", "object_id", "record_json", "source_sheet"}
EXEMPT_SHEETS = {"36_SUPPLEMENT_ARCHIVE", "30_FCS_CONTEXT", "29_OECD_BENCHMARKS", "25_FINDEX_BASELINE", "16_DATASET_CATALOG", "28_METHODS_RIGHTS"}  # removed/non-public per PB-0108..0110, PB-0220..0221
res = collections.defaultdict(list); DERIVED = collections.Counter()
for sh, recs in sheets.items():
    if sh in EXEMPT_SHEETS: continue
    for r in recs:
        for k, v in r.items():
            if k in EXEMPT_FIELDS or not isinstance(v, str): continue
            if sh == "02_SITE_MAP" and k.startswith("full_copy"):
                for label, pat in FORBID.items():
                    if re.search(pat, v): DERIVED[label] += 1
                continue
            for label, pat in FORBID.items():
                for m in re.finditer(pat, v):
                    res[label].append(f"{sh}!r{r['_row']}.{k}: …{v[max(0,m.start()-70):m.end()+50]}…".replace("\n", " "))

_imp = [f"r{v['_row']}.{f}" for v in sheets["11_VISUAL_LIBRARY"] for f in ("what_it_shows_en", "accessible_summary_en")
        if re.match(r"(Place|Show|Plot|Render|Lead|Use|Compare|Separate)\b", v.get(f) or "")]
print("11_VISUAL_LIBRARY what_it_shows_en / accessible_summary_en still in drawing-instruction voice:", _imp or "none")
_imp6 = [e["object_id"] for e in sheets["06_EVIDENCE_OBJECTS"] if re.match(r"(Show|Keep|Preserve|Plot|Place|Display|Use|Render|Lead|Separate|Compare|Stage 1 shows|Barrier values share)\b", e.get("summary_en") or "")]
print("06_EVIDENCE_OBJECTS summary_en still in drawing-instruction voice:", _imp6 or "none")
print("\nRESIDUAL FORBIDDEN STRINGS AFTER SIMULATED APPLICATION (public-bearing sheets):")
for label in FORBID:
    hits = res.get(label, [])
    print(f"  [{len(hits):>3}] {label}")
    for h in hits[:6]: print("        ", h[:260])
print("\nResiduals only in 02_SITE_MAP.full_copy_* (derived, non-rendered field; all in 02 r139, resolved by PB-0472 regeneration under PB-0470):", dict(DERIVED))
json.dump({k: v for k, v in res.items()}, open(os.environ.get("YFI_SIM_OUT", f"{SCR}/simulation_residuals.json"), "w"), ensure_ascii=False, indent=1)
