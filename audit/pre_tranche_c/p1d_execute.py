# -*- coding: utf-8 -*-
"""P1-D — chronology assurance fixes (P1.7), one duplicate source identity, and the one public number the strict
(v2) literal audit found untraced (P15-F4).

  python3 p1d_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>
"""
import json, re, sys
from collections import OrderedDict
from ptc_lib import Session, TxError, S03
from projection.master_reader import Workbook

S06, S07, S14, S15, S16 = "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS", "14_SYSTEM_CHRONOLOGY", "15_SOURCE_LIBRARY", "16_DATASET_CATALOG"
PILOT_EN = ("World Bank/G2Px material documents an eight-district digital-payment pilot within Yemen's unconditional cash-transfer programme "
            "that reached 45,460 recipients, with payments into fully functional accounts and recipient choice; this establishes delivery "
            "and exposure to a formal digital service. ")
PILOT_AR = ("توثق مواد البنك الدولي/مبادرة G2Px تجربة للمدفوعات الرقمية ضمن برنامج التحويلات النقدية غير المشروطة في اليمن شملت ثماني مديريات "
            "واستفاد منها 45,460 مستفيدًا، مع الإيداع في حسابات كاملة الوظائف وإتاحة الاختيار للمستفيد؛ وهذا يثبت الإيصال والتعرض لخدمة رقمية رسمية. ")


def header(g, row=4):
    return {h: j + 1 for j, h in enumerate(g[row - 1]) if h}


def row_of(g, key, first=5):
    hits = [i for i, r in enumerate(g, 1) if i >= first and r and r[0] == key]
    if len(hits) != 1:
        raise TxError(f"{key}: {len(hits)} rows")
    return hits[0]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)
    g06, g07, g14, g15, g16, g03 = (wb.grid(x) for x in (S06, S07, S14, S15, S16, S03))
    H06, H07, H14, H15, H16 = header(g06), header(g07), header(g14), header(g15), header(g16)

    def pre(finding, sheet, g, H, key, field, prefix):
        r = row_of(g, key)
        cur = s.ed.get_value(sheet, r, H[field])
        if cur.startswith(prefix):
            raise TxError(f"{key}.{field} already extended")
        s.set(finding, sheet, r, H[field], prefix + cur, cur, f"{key}.{field}")

    # ---- P15-F4: the G2Px pilot reach stated by Reading CWR-010 is carried by CLM-045, whose bound source reports it
    pre("P1-L10", S06, g06, H06, "CLM-045", "summary_en", PILOT_EN)
    pre("P1-L10", S06, g06, H06, "CLM-045", "summary_ar", PILOT_AR)
    pre("P1-L10", S07, g07, H07, "CLM-045", "copy_en", PILOT_EN)
    pre("P1-L10", S07, g07, H07, "CLM-045", "copy_ar", PILOT_AR)
    r03 = [i for i, r in enumerate(g03, 1) if i > 4 and r and r[0] == "/evidence/CLM-045/" and r[1] in (1, "1")]
    if len(r03) != 1:
        raise TxError("03 /evidence/CLM-045/ s1")
    for col, prefix in ((5, PILOT_EN), (7, PILOT_AR)):
        cur = s.ed.get_value(S03, r03[0], col)
        s.set("P1-L10", S03, r03[0], col, prefix + cur, cur, f"/evidence/CLM-045/#s1.body_{'en' if col == 5 else 'ar'}")

    # ---- P1.7 / P17-04: an agreement to deposit is not a deposit or a disbursement
    r = row_of(g14, "YSC-019")
    for lang, add in (("en", " An agreement to deposit is not evidence that a deposit or a disbursement has taken place."),
                      ("ar", " والاتفاق على الإيداع لا يثبت أن إيداعًا أو صرفًا قد تم فعلًا.")):
        c = H14["does_not_establish_" + lang]
        cur = s.ed.get_value(S14, r, c)
        s.set("P1-C01", S14, r, c, cur + add, cur, f"YSC-019.does_not_establish_{lang}")

    # ---- P1.7 / P17-03: one document, one source identity (both records carry the same World Bank ISR URL)
    dup, keep = "SRC-WB-FMIIP-ISR-2026-04", "SRC-WB-FMIIP-ISR2-2026-001"
    r_dup, r_keep = row_of(g15, dup), row_of(g15, keep)
    if g15[r_dup - 1][H15["primary_url"] - 1] != g15[r_keep - 1][H15["primary_url"] - 1]:
        raise TxError("ISR records do not share a locator")
    r = row_of(g14, "YSC-018")
    s.replace("P1-C02", S14, r, H14["source_ids"], dup, keep, "YSC-018.source_ids")
    # P17-08: Arabic project name as on its source card
    s.replace("P1-C03", S14, r, H14["fact_ar"], "لمشروع البنية التحتية للأسواق المالية والشمول في اليمن", "لمشروع البنية التحتية للأسواق والشمول المالي في اليمن", "YSC-018.fact_ar")
    r16 = row_of(g16, "DS-FMIIP-IMPLEMENTATION-2026")
    s.replace("P1-C02", S16, r16, H16["sample_source_ids"], dup, keep, "DS-FMIIP-IMPLEMENTATION-2026.sample_source_ids")
    cur = s.ed.get_value(S15, r_keep, H15["datasets_or_use"])
    s.set("P1-C02", S15, r_keep, H15["datasets_or_use"], cur + ",DS-FMIIP-IMPLEMENTATION-2026", cur, f"{keep}.datasets_or_use")
    s.ed.delete_rows(S15, r_dup, r_dup)
    s.ledger.append(OrderedDict([("finding", "P1-C02"), ("sheet", S15), ("row", r_dup), ("col", None), ("field", f"{dup} (row deleted)"),
                                 ("old", "duplicate LOCATOR_ONLY record of " + keep), ("new", None)]))

    # ---- P17-08: the IMF document behind YSC-023 is a press release reporting the mission, not a 'mission statement'
    r = row_of(g14, "YSC-023")
    s.replace("P1-C03", S14, r, H14["fact_en"], "and the mission statement says it will not result", "and the IMF press release on the mission states that it will not result", "YSC-023.fact_en")
    s.replace("P1-C03", S14, r, H14["fact_ar"], "كما يوضح بيان البعثة", "كما يوضح البيان الصحفي للصندوق بشأن البعثة", "YSC-023.fact_ar")

    # ---- P17-05: the chronology catalog row describes the governed sheet as it now stands
    ev = [x for x in wb.grid(S14)[4:] if x and str(x[0]).startswith("YSC-")]
    ids = []
    for x in ev:
        v = x[H14["source_ids"] - 1] or ""
        v = v.replace(dup, keep)
        for t in re.split(r"\s*\|\s*", v):
            if t and t not in ids:
                ids.append(t)
    http = {x[0] for x in g15[4:] if x and str(x[H15["primary_url"] - 1] or "").lower().startswith(("http://", "https://"))}
    r16 = row_of(g16, "DS-V4R3-SYSTEM-CHRONOLOGY")
    for field, new in (("rows", str(len(ev))), ("period_max", "2026-07-16"), ("source_id_count", str(len(ids))),
                       ("source_url_count", str(sum(1 for i in ids if i in http)))):
        s.set("P1-C04", S16, r16, H16[field], new, s.ed.get_value(S16, r16, H16[field]), f"DS-V4R3-SYSTEM-CHRONOLOGY.{field}")

    s.regenerate_full_copy()
    rep = s.save(out, ledger, [("transaction", "P1-D"), ("scope", "P1.7 chronology assurance fixes; ISR source identity; P15-F4 pilot figure carried by CLM-045")])
    print(f"P1-D staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
