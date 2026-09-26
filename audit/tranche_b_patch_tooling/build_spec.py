# -*- coding: utf-8 -*-
import json, csv, glob, os, re, sys, collections
from urllib.parse import urlparse
sys.path.insert(0, os.path.dirname(__file__))
from pdefs_p1 import P1, binding_rows
from pdefs_p2 import P2
from pdefs_p3 import P3, P3_SEARCH
from pdefs_p4 import P4
import copy
from sweeps import sweep
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tranche_b_execution"))
from stage5_execute import R414 as D2_R414, K413 as D2_K413, R415 as D2_R415   # executed per-cell decisions (D2)

SCR = os.path.dirname(os.path.abspath(__file__))
M = os.environ.get("YFI_MASTER_JSON", f"{SCR}/master")
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{SCR}/out"
os.makedirs(OUT, exist_ok=True)
SESSION = "TRB-C2"
COLS = ["patch_id","session","sheet","stable_object_id","row_locator_if_needed","field","current_value","proposed_value","language",
        "change_type","semantic_change_yes_no","source_basis","reason","evidence_boundary_preserved","downstream_projections",
        "search_impact","IA_impact","visual_impact","rights_impact","priority","validation_required","Claude_status"]

# Deterministic load: sheets are keyed and iterated in sorted sheet-name order, never filesystem order.
sheets = {os.path.basename(f)[:-5]: json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(f"{M}/*.json")) if not f.endswith("_index.json")}
sheets = dict(sorted(sheets.items()))
IDX = json.load(open(f"{M}/_index.json", encoding="utf-8"))

def target_key(sh, r, k):
    """Canonical target order for multi-hit patches: sheet -> Excel row -> field (column index) -> stable object id."""
    cols = IDX.get(sh, {}).get("cols", [])
    ci = cols.index(k) if k in cols else len(cols)
    return (sh, int(r["_row"]), ci, k, rid(sh, r))

def rid(sheet, rec):
    keys = [k for k in rec if k != "_row"]
    if sheet == "03_PAGE_SECTIONS":
        return f"{rec.get('route')}#s{rec.get('section_order')}"
    if sheet == "09_READING_SECTIONS":
        return f"{rec.get('reading_id')}#{rec.get('section_id')}"
    return str(rec.get(keys[0])) if keys else "?"

def boundary(ctype, sem):
    if ctype in ("EDITORIAL_NO_SEMANTIC_CHANGE",): return "YES — meaning unchanged; wording only"
    if ctype == "BOUNDARY_TIGHTENING": return "YES — narrows the statement to what the cited Master cells and sources support"
    return "YES — no fact beyond the cited Master cells/sources"

def status(d):
    s = d.get("status") or "SPEC_PENDING_EXECUTION"
    parts = ["VERIFIED_BY_CLAUDE_TEAM"] + [p for p in s.split("|") if p != "VERIFIED_BY_CLAUDE_TEAM"]
    # Acceptance correction A: PRIMARY_SOURCE_PENDING is carried only where a row itself states it (no lead-level blanket rule).
    if d.get("lang") == "ar" and d.get("ctype") == "EDITORIAL_NO_SEMANTIC_CHANGE" and "EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED" not in parts:
        parts.append("EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED")
    if "SPEC_PENDING_EXECUTION" not in parts and not any(p.startswith("SUPERSEDED") for p in parts): parts.append("SPEC_PENDING_EXECUTION")
    parts.append("INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED")
    if any(p.startswith("SUPERSEDED") for p in parts):
        parts = [p for p in parts if p != "SPEC_PENDING_EXECUTION"]
    ORDER = ["VERIFIED_BY_CLAUDE_TEAM", "SUPERSEDED", "KEEP", "LEAD_REVISED_PER_CELL", "ACCEPTANCE_CORRECTION_A", "ACCEPTANCE_CORRECTION_G", "SOURCE_PENDING", "HELD_LANGUAGE_REVIEW", "PRIMARY_SOURCE_PENDING", "EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED", "SPEC_PENDING_EXECUTION", "INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED"]
    extra = [p for p in dict.fromkeys(parts) if p not in ORDER]
    return "|".join([p for p in ORDER if p in parts] + extra)

rows, errors, hitlog = [], [], []

def emit(d, sheet, obj, loc, field, cur, new):
    rows.append({"patch_id": d["pid"], "session": SESSION, "sheet": sheet, "stable_object_id": obj, "row_locator_if_needed": loc,
      "field": field, "current_value": cur, "proposed_value": new, "language": d.get("lang","n/a"), "change_type": d["ctype"],
      "semantic_change_yes_no": d.get("sem","yes"), "source_basis": d.get("basis",""), "reason": d.get("reason",""),
      "evidence_boundary_preserved": boundary(d["ctype"], d.get("sem")), "downstream_projections": d.get("down",""),
      "search_impact": d.get("search","none"), "IA_impact": d.get("ia","none"), "visual_impact": d.get("vis","none"),
      "rights_impact": d.get("rights","none"), "priority": d["pri"], "validation_required": d.get("val",""), "Claude_status": status(d)})

def do_substr(d):
    if d["old"] == d["new"]:
        errors.append(f"{d['pid']}: old == new"); return
    hits = []
    for sh, recs in sheets.items():
        if d.get("sheets") and sh not in d["sheets"]: continue
        for r in recs:
            if d.get("rows") and (sh, r["_row"]) not in d["rows"]: continue
            for k, v in r.items():
                if k == "_row" or not isinstance(v, str): continue
                if d.get("fields") and k not in d["fields"]: continue
                n = v.count(d["old"])
                if n: hits.append((sh, r, k, n))
    hits.sort(key=lambda h: target_key(h[0], h[1], h[2]))
    if not hits:
        errors.append(f"{d['pid']}: ZERO HITS for old substring: {d['old'][:90]!r}"); return
    total = sum(h[3] for h in hits)
    hitlog.append((d["pid"], len(hits), total))
    if len(hits) <= 12:
        for i, (sh, r, k, n) in enumerate(hits, 1):
            d2 = dict(d); d2["pid"] = f"{d['pid']}.{i:02d}"
            emit(d2, sh, rid(sh, r), f"Excel row {r['_row']}; exact-substring replace ({n}× in cell)", k, d["old"],
                 d["new"] if d["new"] else "(DELETE — remove this exact substring; nothing is inserted)")
    else:
        loc = "; ".join(f"{sh}!r{r['_row']}.{k}" for sh, r, k, n in hits)
        by = collections.Counter(sh for sh, *_ in hits)
        emit(d, "MULTI: " + ", ".join(f"{s}×{c}" for s, c in by.items()), f"{len(hits)} cells", "Exact-substring replace in: " + loc,
             "(see locator)", d["old"], d["new"])

def do_cell(d):
    emit(d, d["sheet"], d["obj"], d.get("loc", f"op={d['op']}"), d["field"], d["cur"], d["new"])

for d in P1 + P2 + P3 + P4 + P3_SEARCH:
    if d["op"] == "SUBSTR": do_substr(d)
    elif d["op"] == "FIELD_ALL" and d.get("sheet") == "06_EVIDENCE_OBJECTS":
        recs = [r for r in sheets["06_EVIDENCE_OBJECTS"] if r.get(d["field"]) == d["cur"]]
        if not recs: errors.append(f"{d['pid']}: FIELD_ALL value not found in {d['field']}")
        d = dict(d); d["loc"] = f"{len(recs)} rows: " + ", ".join(f"r{r['_row']}({r['object_id']})" for r in recs)
        do_cell(d)
    else: do_cell(d)

# ---- terminology sweeps PB-0413/0414/0415: per cell, on post-patch text (execution step: LAST) ----
post = copy.deepcopy(sheets)
for d in sorted([d for d in P2 + P3 + P4 if d["op"] == "SUBSTR"], key=lambda d: d["pid"]):
    for sh, recs in post.items():
        if d.get("sheets") and sh not in d["sheets"]: continue
        for r in recs:
            if d.get("rows") and (sh, r["_row"]) not in d["rows"]: continue
            for k, v in list(r.items()):
                if k == "_row" or not isinstance(v, str): continue
                if d.get("fields") and k not in d["fields"]: continue
                if d["old"] in v: r[k] = v.replace(d["old"], d["new"])
sw_rows, sw_keeps, _ = sweep(post, rid)
SWMETA = {"PB-0413": ("LEAD-B05", "P3", "ar", "Arabic terminology decision (Lead): governed-claim noun «خلاصة/الخلاصات». ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md §3."),
          "PB-0414": ("ARABIC-SELFREF", "P5", "ar", "Lead decision: product self-referent «المنصة» (feminine; agreement preserved). ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md §4."),
          "PB-0415": ("ENGLISH-SELFREF", "P5", "en", "English self-referent rule. ENGLISH_EDITORIAL_CLOSURE.md §2.")}
seq = collections.Counter()
for w in sw_rows:
    root = w["pid"].split("+")[0]; seq[root] += 1
    lead, pri, lang, basis = SWMETA[root]
    d = dict(pid=f"{root}.S{seq[root]:03d}", lead=lead, pri=pri, lang=lang, sem="no", ctype="EDITORIAL_NO_SEMANTIC_CHANGE",
             basis=basis + (f" Combined window: {w['pid']}." if "+" in w["pid"] else ""),
             reason=w["rule"], down="Regenerate this Master cell; page_specs.json; search_index.json; dist " + lang.upper(),
             search="Index text updates on regeneration", val="Apply AFTER every other SUBSTR/CELL patch in this spec (the before-text is the post-patch text). Before-text occurs exactly once in the cell; after execution the after-text occurs once.",
             status="VERIFIED_BY_CLAUDE_TEAM|EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED" if lang == "ar" else "SPEC_PENDING_EXECUTION")
    new_text = w["new"]
    # Recipient acceptance directive (D2): PB-0413/PB-0414 re-adjudicated per cell; the executed text is recorded here.
    if root == "PB-0414" and w["old"] in D2_R414:
        new_text = D2_R414[w["old"]]
        d["status"] = d["status"] + "|LEAD_REVISED_PER_CELL"
        d["reason"] = d["reason"] + " | D2 per-cell re-adjudication: self-reference rendered by context (هذا الموقع / قاعدة الأدلة / هنا / impersonal), «المنصة» not used."
    if root == "PB-0415" and w["old"] in D2_R415:
        new_text = D2_R415[w["old"]]
        d["status"] = d["status"] + "|LEAD_REVISED_PER_CELL"
        d["reason"] = d["reason"] + " | Execution review: the second 'system' is the financial system and is kept."
    if root == "PB-0413" and w["old"] in D2_K413:
        d["status"] = "VERIFIED_BY_CLAUDE_TEAM|SUPERSEDED|KEEP"
        d["reason"] = d["reason"] + " | D2 per-cell re-adjudication: KEEP — " + D2_K413[w["old"]]
    emit(d, w["sheet"], w["obj"], f"Excel row {w['row']}; exact-substring replace in this cell only ({w['n']} occurrence(s)); execution step LAST", w["field"], w["old"], new_text)
with open(f"{OUT}/TERMINOLOGY_SWEEP_KEEP_REGISTER.csv", "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL); wr.writerow(["sweep", "sheet", "excel_row", "field", "context", "keep_rule"])
    for k in sw_keeps: wr.writerow(k)
    wr.writerow(["PB-0413", "07_PUBLIC_CLAIMS", 1, "A1 (sheet title)", "الادعاءات التحليلية العامة", "REPLACED by PB-0413.T01 (listed here for count closure; not a KEEP)"])
unclassified = [k for k in sw_keeps if k[5] == "UNCLASSIFIED"]
if unclassified: errors.append(f"sweeps: {len(unclassified)} UNCLASSIFIED occurrences")
print("sweep rows:", collections.Counter(r["pid"].split("+")[0] for r in sw_rows), "| keeps:", collections.Counter(k[0] for k in sw_keeps))

# ---- per-object source bindings (PB-0010 … ) ----
alt_msgs = []
for i, b in enumerate(binding_rows()):
    pid = f"PB-{10+i:04d}"
    rec = [r for r in sheets["06_EVIDENCE_OBJECTS"] if r["object_id"] == b["oid"]][0]
    if rec.get("source_dependencies"): errors.append(f"{pid}: {b['oid']} already has Master source_dependencies")
    lib = {r["source_id"] for r in sheets["15_SOURCE_LIBRARY"]}
    missing = [s for s in b["srcs"] if s not in lib]
    if missing: errors.append(f"{pid}: {b['oid']} proposes source IDs absent from 15_SOURCE_LIBRARY: {missing}")
    srcs = "; ".join(b["srcs"]) if b["srcs"] else "(none — not a direct-source object)"
    new = f"source_dependencies = {srcs} || lineage_state = {b['state']}"
    removed = ("; removes from rendered trace: " + ", ".join(b["removed"])) if b["removed"] else ""
    d = dict(pid=pid, lead="LEAD-B07", pri="P1", lang="n/a", sem="yes",
             ctype="BOUNDARY_TIGHTENING",
             basis=f"Master 06 r{rec['_row']} source_dependencies empty; closure fallback resolved via {b['alt_via']}{removed}. {b['note']}",
             reason="Object-level lineage replaces dataset-level resolution; a COMPOSITE or unbound state is said, not implied.",
             down="evidence_objects.json; public_object_source_closure.json; /evidence/%s/ (EN/AR)" % b["oid"],
             search="none", ia="none", vis="Trace block lists only bound sources" if b["cls"]=="VISUAL" else "none", rights="Rights attach per bound source",
             val=("Execution check: confirm each proposed source against the object's own copy/data before binding. " if b["state"].startswith("BOUND_CANDIDATE") else "") +
                 "After regeneration the evidence page trace equals this list (or the COMPOSITE/UNBOUND statement).",
             status="SPEC_PENDING_EXECUTION")
    emit(d, "06_EVIDENCE_OBJECTS", b["oid"], f"Excel row {rec['_row']}", "source_dependencies + lineage_state", "(empty)", new)

# ---- publisher proposals for PB-0390 ----
HOST = [
 (r"cby-ye\.com", "Central Bank of Yemen – Aden", "البنك المركزي اليمني – عدن"),
 (r"worldbank\.org", "World Bank", "البنك الدولي"),
 (r"imf\.org", "International Monetary Fund", "صندوق النقد الدولي"),
 (r"sfd-yemen\.org|sfd\.org\.ye", "Social Fund for Development (Yemen)", "الصندوق الاجتماعي للتنمية"),
 (r"yemenmn\.org|ymn", "Yemen Microfinance Network", "شبكة اليمن للتمويل الأصغر"),
 (r"oecd\.org", "OECD", "منظمة التعاون الاقتصادي والتنمية"),
 (r"undp\.org", "UNDP", "برنامج الأمم المتحدة الإنمائي"),
 (r"unocha\.org|fts\.", "UN OCHA — Financial Tracking Service", "مكتب الأمم المتحدة لتنسيق الشؤون الإنسانية — خدمة تتبع التمويل"),
 (r"gsma\.com", "GSMA", "GSMA"),
 (r"ilo\.org", "International Labour Organization", "منظمة العمل الدولية"),
 (r"kfw", "KfW Development Bank", "بنك التنمية الألماني KfW"),
 (r"sanaacenter\.org", "Sana'a Center for Strategic Studies", "مركز صنعاء للدراسات الاستراتيجية"),
 (r"saba\.ye|sabanew", "Saba News Agency", "وكالة الأنباء اليمنية سبأ"),
 (r"bis\.org", "Bank for International Settlements", "بنك التسويات الدولية"),
 (r"cgap\.org", "CGAP", "المجموعة الاستشارية لمساعدة الفقراء"),
 (r"afi-global\.org", "Alliance for Financial Inclusion", "التحالف من أجل الشمول المالي"),
 (r"wfp\.org", "World Food Programme", "برنامج الأغذية العالمي"),
 (r"unicef\.org", "UNICEF", "اليونيسف"),
 (r"reliefweb\.int", "ReliefWeb (host of third-party document — publisher to confirm)", "ReliefWeb (منصة استضافة — تُؤكد الجهة الناشرة)"),
]
prop = []
for r in sheets["15_SOURCE_LIBRARY"]:
    if r.get("publisher"): continue
    url = r.get("primary_url") or ""; host = urlparse(url).netloc.lower()
    pe, pa, basis = "", "", "UNRESOLVED — confirm manually"
    for pat, en, ar in HOST:
        if re.search(pat, host) or re.search(pat, url.lower()):
            pe, pa, basis = en, ar, f"URL host '{host}'"; break
    if not pe and r["source_id"].startswith("SRC-CBY-SANAA"):
        pe, pa, basis = "Central Bank of Yemen – Sana'a (as issuer named in source)", "البنك المركزي اليمني – صنعاء (بحسب الجهة المصدِرة المذكورة)", "source-ID family SRC-CBY-SANAA"
    prop.append({"source_id": r["source_id"], "excel_row": r["_row"], "public_card_state": r.get("public_card_state"),
                 "primary_url": url, "proposed_publisher_en": pe, "proposed_publisher_ar": pa, "derivation_basis": basis,
                 "status": "PROPOSAL__CONFIRM_AT_EXECUTION" if pe else "UNRESOLVED"})

# ---- write ----
with open(f"{OUT}/MASTER_FIRST_PATCH_SPEC.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_ALL); w.writeheader(); [w.writerow(r) for r in rows]
with open(f"{OUT}/SOURCE_PUBLISHER_PROPOSALS.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(prop[0].keys()), quoting=csv.QUOTE_ALL); w.writeheader(); [w.writerow(r) for r in prop]

print("ROWS:", len(rows), "| distinct patch roots:", len({r['patch_id'].split('.')[0] for r in rows}))
print("by priority:", collections.Counter(r["priority"] for r in rows))
print("by change_type:", collections.Counter(r["change_type"] for r in rows))
print("semantic yes/no:", collections.Counter(r["semantic_change_yes_no"] for r in rows))
print("publisher proposals:", len(prop), collections.Counter(p["status"] for p in prop))
print("unresolved hosts:", collections.Counter(urlparse(p["primary_url"]).netloc for p in prop if p["status"]=="UNRESOLVED").most_common(15))
print("SUBSTR hit summary (pid, cells, occurrences):", hitlog)
print("ERRORS:", len(errors)); [print("  ", e) for e in errors]
