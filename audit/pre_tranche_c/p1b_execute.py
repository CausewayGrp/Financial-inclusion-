# -*- coding: utf-8 -*-
"""P1-B — source-lineage residuals and Reading verification paths (P1.5).

  python3 p1b_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir> <P15_analysis.json>

Every binding below is taken from governed Master evidence (Lead adjudication of the P15 specialist analysis, recorded in
audit/pre_tranche_c/P1_5_LINEAGE_ADJUDICATION.md). No dataset token is expanded into a source list.
"""
import json, sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook
from projection.structure import keyed_records

S06, S08, S04 = "06_EVIDENCE_OBJECTS", "08_READINGS", "04_NAV_UX"
C06 = {}   # filled from the 06 header row (1-based columns)


def ui(wb, ui_id):
    for _, r in keyed_records(wb.grid(S04), S04, block="Governed interface copy"):
        if r["ui_id"] == ui_id:
            return r["label_en"], r["label_ar"]
    raise TxError(f"04 interface copy {ui_id} missing")


def row_of(grid, key, col=1, first=5):
    hits = [i for i, r in enumerate(grid, 1) if i >= first and r and r[col - 1] == key]
    if len(hits) != 1:
        raise TxError(f"{key}: {len(hits)} rows")
    return hits[0]


def main():
    src, out, ledger, work, analysis = sys.argv[1:6]
    s = Session(src, work)
    wb = Workbook(src)
    g06 = wb.grid(S06)
    hdr06 = g06[3]
    for k in ("source_dependencies", "lineage_state", "verification_en", "verification_ar"):
        C06[k] = hdr06.index(k) + 1
    ub, uc = ui(wb, "UI-VERIFY-BOUND"), ui(wb, "UI-VERIFY-COMPOSITE")
    ucu, uun = ui(wb, "UI-VERIFY-COMPOSITE-UNLISTED"), ui(wb, "UI-EVID-UNBOUND")
    upa = ui(wb, "UI-VERIFY-PARTIAL")

    def rec(finding, oid, deps_from, deps_to, state_from, state_to, verif_from, verif_to):
        r = row_of(g06, oid)
        s.set(finding, S06, r, C06["source_dependencies"], deps_to, deps_from, f"{oid}.source_dependencies")
        if state_to != state_from:
            s.set(finding, S06, r, C06["lineage_state"], state_to, state_from, f"{oid}.lineage_state")
        if verif_to != verif_from:
            for k, lang in ((0, "en"), (1, "ar")):
                s.set(finding, S06, r, C06["verification_" + lang], verif_to[k], verif_from[k], f"{oid}.verification_{lang}")

    # --- CLOSE: the listing page is itself a governed source record (15 r70, DS-PAYMENT-CURRENTNESS)
    rec("P1-L01", "CLM-017", "SRC-CBY-POS-2026-01; UNBOUND:CBY-PAYMENTS-RELEASE-LISTING",
        "SRC-CBY-POS-2026-01; SRC-CBY-POS-PUBLICATION-PAGE-2026-001", "BOUND_PARTIAL", "BOUND_EXACT", upa, ub)
    # --- CLOSE: the claim's three named links map row by row to 32 QQL-012/013/014 -> QUAL-014/016/018 and their sources
    rec("P1-L02", "CLM-045", "SRC-WB-G2PX-YEM-UCT-2024-001; EP-YEM-CASH-FIN-TRANSMISSION-K04; DS-K04-CASH-FIN-TRANSMISSION",
        "SRC-WB-G2PX-YEM-UCT-2024-001; SRC-CCY-SAM-2024; SRC-CCY-ISP-2024; SRC-CCY-PRESSURE-2026; EP-YEM-CASH-FIN-TRANSMISSION-K04",
        "BOUND_PARTIAL", "BOUND_EXACT", upa, ub)
    # --- LINEAGE DEFECT: CLM-054 prints CBY-Aden market rates (18 OBS-CBY-00621/00657, SRC-CBY-001) without binding that source
    r = row_of(g06, "CLM-054")
    cur = s.ed.get_value(S06, r, C06["source_dependencies"])
    if cur != "SRC-SFD-Q4-2015-001; SRC-SFD-Q4-2020-001; SRC-SANAA-MFB-2024; INS-K04-023":
        raise TxError(f"CLM-054 deps {cur!r}")
    s.set("P1-L03", S06, r, C06["source_dependencies"], "SRC-SFD-Q4-2015-001; SRC-SFD-Q4-2020-001; SRC-SANAA-MFB-2024; SRC-CBY-001; INS-K04-023",
          cur, "CLM-054.source_dependencies")
    # --- COMPOSITES whose members are demonstrable from the record's own governed text
    rec("P1-L04", "VIS-PROVIDER-TIME", None, "CLM-009; CLM-019", "SOURCE_NOT_YET_BOUND", "COMPOSITE_OF_OBJECTS", uun, uc)
    rec("P1-L05", "VIS-DEMAND-VINTAGE-LADDER", None,
        "CLM-001; CLM-027; CLM-028; CLM-029; CLM-030; VIS-FINDEX-RESILIENCE; VIS-FINDEX-BARRIERS",
        "COMPOSITE_OF_OBJECTS", "COMPOSITE_OF_OBJECTS", ucu, uc)
    rec("P1-L06", "DS-FINDEX-HISTORY-CROSSWALK", None, "DS-FINDEX-PUBLIC-HISTORY; CLM-026", "COMPOSITE_OF_OBJECTS", "COMPOSITE_OF_OBJECTS", ucu, uc)
    # --- REGISTER: the 20 register rows (32 'Qualitative evidence') each cite one source; the register is drawn from those 10 sources
    qsrc = []
    for _, q in keyed_records(wb.grid("32_QUAL_LITERATURE"), "32_QUAL_LITERATURE", block="Qualitative evidence"):
        if q["source_id"] not in qsrc:
            qsrc.append(q["source_id"])
    if len(qsrc) != 10:
        raise TxError(f"qualitative register sources: {qsrc}")
    rec("P1-L07", "DS-QUAL-EVIDENCE", None, "; ".join(qsrc), "COMPOSITE_OF_OBJECTS", "BOUND_EXACT", ucu, ub)

    # --- 08 Readings: bind the records that carry each proposition; drop dataset/internal tokens those records already carry
    g08 = wb.grid(S08)
    hdr = g08[3]
    col = {h: j + 1 for j, h in enumerate(hdr) if h}
    changes = json.load(open(analysis, encoding="utf-8"))["readings"]
    for rid, a in changes.items():
        ch = a.get("08_changes") or {}
        r = row_of(g08, rid)
        for field in ("claim_bindings", "evidence_bindings", "source_bindings"):
            if field not in ch:
                continue
            cur = s.ed.get_value(S08, r, col[field])
            if json.loads(cur) != ch[field]["frm"]:
                raise TxError(f"{rid}.{field}: current {cur!r} differs from the adjudicated 'from' value")
            sep = (", ", ": ") if ", " in cur else (",", ":")
            s.set("P1-L08", S08, r, col[field], json.dumps(ch[field]["to"], ensure_ascii=False, separators=sep), cur, f"{rid}.{field}")
        if "verification_claim_ids" in ch or "verification_dependency_ids" in ch:
            cur = s.ed.get_value(S08, r, col["verification_bindings"])
            vb = json.loads(cur, object_pairs_hook=OrderedDict)
            for key, k2 in (("verification_claim_ids", "claim_ids"), ("verification_dependency_ids", "dependency_ids")):
                if key in ch:
                    if vb.get(k2) != ch[key]["frm"]:
                        raise TxError(f"{rid}.verification_bindings.{k2}: current differs from the adjudicated 'from' value")
                    vb[k2] = ch[key]["to"]
            s.set("P1-L08", S08, r, col["verification_bindings"], json.dumps(vb, ensure_ascii=False, separators=(", ", ": ")), cur,
                  f"{rid}.verification_bindings")

    # --- 04 governed interface copy for the Reading verification path and locator-less sources (P1.5 / P15-F2)
    g04 = wb.grid(S04)
    last = row_of(g04, "UI-FOOTER-STRAPLINE", first=5)
    if g04[last] and any(c not in (None, "") for c in g04[last]):
        raise TxError("04: the row after UI-FOOTER-STRAPLINE is not the block separator")
    new = [
        ("UI-READING-PATH-INTRO",
         "Each statement this Reading relies on is carried by an Evidence Record. Follow a record to its original sources before reusing a figure.",
         "كل مقولة تعتمد عليها هذه القراءة يحملها سجل دليل. تتبّع السجل إلى مصادره الأصلية قبل إعادة استخدام أي رقم.",
         "Pre-Tranche-C P1.5. Introduction to the Reading verification path (Reading proposition -> Evidence Record -> source)."),
        ("UI-READING-PATH-COMPLETE",
         "Every figure in this Reading traces through the records below to a named source.",
         "يمكن تتبّع كل رقم في هذه القراءة، عبر السجلات أدناه، إلى مصدر مسمّى.",
         "P1.5. Shown when the Reading's closure state is CLOSED_TO_SOURCE_ID."),
        ("UI-READING-PATH-PARTIAL",
         "Most figures in this Reading trace through the records below to a named source. A record marked as not yet fully traced still has an input that is not linked to a specific original source; treat that figure as unverified for reuse.",
         "يمكن تتبّع معظم أرقام هذه القراءة، عبر السجلات أدناه، إلى مصدر مسمّى. أما السجل الموسوم بأنه لم يُتتبّع بالكامل بعدُ، فما زال أحد مدخلاته غير مربوط بمصدر أصلي محدد؛ فعامِل ذلك الرقم على أنه غير متحقق منه عند إعادة الاستخدام.",
         "P1.5. Shown when the Reading's closure state is PARTIALLY_RESOLVED."),
        ("UI-READING-PATH-RECORD-PARTIAL", "Not yet fully traced to a source", "لم يُتتبّع بالكامل إلى مصدر بعدُ",
         "P1.5. Label on a path step whose record is PARTIALLY_RESOLVED."),
        ("UI-READING-PATH-RECORD-COMPOSITE", "Assembles other evidence records", "يجمع سجلات أدلة أخرى",
         "P1.5. Label on a path step whose record is a composite of other records."),
        ("UI-SOURCE-NO-PUBLIC-LOCATOR",
         "Also draws on source material with no public original locator recorded here; it is not listed or linked.",
         "ويستند أيضًا إلى مواد مصدرية لا يُسجَّل لها هنا رابط أصلي عام، فلا تُدرج ولا تُربط.",
         "P1.5 / P15-F2. Reading path step whose record also rests on a source without an http(s) locator. The publication firewall (validator S04.1/S04.2) keeps such sources unnamed on public pages."),
        ("UI-EVID-SOURCES-WITHOUT-LOCATOR",
         "This record also draws on source material for which no public original locator is recorded. That material is held in the evidence base but is not listed or linked here, so the sources shown above are not the record's only basis.",
         "ويستند هذا السجل أيضًا إلى مواد مصدرية لا يُسجَّل لها رابط أصلي عام، وهي محفوظة في قاعدة الأدلة لكنها لا تُدرج ولا تُربط هنا؛ لذلك فالمصادر المعروضة أعلاه ليست الأساس الوحيد للسجل.",
         "P15-F2. Evidence Record page: shown whenever a bound source is not rendered because it has no public locator (never named: publication firewall)."),
    ]
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in new])
    for a, b, c, d in new:
        s.ledger.append(OrderedDict([("finding", "P1-L09"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    rep = s.save(out, ledger, [("transaction", "P1-B"), ("scope", "P1.5 lineage residuals, Reading bindings, verification-path interface copy")])
    print(f"P1-B staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
