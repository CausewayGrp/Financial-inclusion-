# -*- coding: utf-8 -*-
"""P3-B — governed vocabulary of the semantic visual grammar, and data rows the P3 data contracts need (Master-first).

  python3 p3b_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

1. 04 'Governed interface copy' gains the bilingual labels of the visual grammar (UI-VIS-*): evidence states, breaks,
   missing values, disagreement, target/result, the rule-to-outcome chain and the detached-frame labels. Design uses these
   labels; it never authors them. Arabic is authored by the Lead in the product's existing register; it has not been
   certified by a native editor outside this programme.
2. 23_REMITTANCES gains the two CBY publication-vintage values for reference year 2024 that RV-CWR-001 draws. Both values
   are already governed (14 YSC-013 fact; 07 CLM-032 copy gives the unit); they become data rows so that a chart binds to
   a row, not to prose. Sources SRC-CBY-AR2024-BOP / SRC-CBY-AR2025-BOP are DISPLAY_READY in 15.
3. 14 YSC-013 fact: the unit (USD million, from CLM-032's USD billion values) is stated with the figures.
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S04 = "04_NAV_UX"

GRAMMAR = [
    # evidence states of a value or mark
    ("UI-VIS-STATE-MEASURED", "Measured in a survey", "مقيس في مسح", "Value from a survey measure of the stated population."),
    ("UI-VIS-STATE-ADMINISTRATIVE", "Reported in administrative records", "وارد في سجلات إدارية", "Count or value an institution reports from its own records."),
    ("UI-VIS-STATE-DERIVED", "Calculated here from published figures", "محسوب هنا من أرقام منشورة", "A difference, ratio or share this resource calculates from governed values."),
    ("UI-VIS-STATE-HISTORICAL", "Historical — not a current value", "تاريخي — ليس قيمة حالية", "Value whose period is not current and must not be carried forward."),
    ("UI-VIS-STATE-PROGRAMME", "Programme figure — not a national rate", "رقم برنامج — ليس معدلًا وطنيًا", "Result, target or KPI of a programme's own universe."),
    ("UI-VIS-STATE-ESTIMATED", "Estimate — not an observation", "تقدير — ليس مشاهدة", "Source-labelled estimate."),
    ("UI-VIS-STATE-PROJECTED", "Projection — not an observation", "توقع — ليس مشاهدة", "Source-labelled projection or forecast."),
    ("UI-VIS-STATE-PARTIAL", "Partial coverage — not the whole population or sector", "تغطية جزئية — لا تشمل المجتمع أو القطاع كله", "Value whose universe is a bounded subset."),
    ("UI-VIS-STATE-UNKNOWN", "Unknown — not zero", "غير معروف — ليس صفرًا", "Cell or value the evidence does not establish."),
    # structure markers
    ("UI-VIS-BREAK-VINTAGE", "Source document changes here — lines are not joined", "تتغير وثيقة المصدر هنا — لا يُوصل الخطان", "Vintage or document break in a series."),
    ("UI-VIS-BREAK-UNIVERSE", "What is counted changes here — lines are not joined", "يتغير ما يُعدّ هنا — لا يُوصل الخطان", "Definition or reporting-universe break in a series."),
    ("UI-VIS-SAME-YEAR-REVISION", "Same year, different publication", "السنة نفسها، إصدار مختلف", "Two published values for one reference year."),
    ("UI-VIS-MISSING", "No verified value for this period — not zero", "لا قيمة معتمدة لهذه الفترة — ليست صفرًا", "Missing observation kept as a gap."),
    ("UI-VIS-DISAGREEMENT", "Source figures disagree — both are shown", "أرقام المصدر غير متسقة — يُعرض الرقمان", "A published figure and the figure implied by the same source's totals differ."),
    ("UI-VIS-TARGET", "Target — not a result", "مستهدف — ليس نتيجة متحققة", "Stated target value."),
    ("UI-VIS-RESULT", "Observed value", "قيمة مرصودة", "Observed or source-reported value set beside a target."),
    ("UI-VIS-NOT-COMPARABLE", "Not directly comparable", "غير قابل للمقارنة المباشرة", "Two values whose definition, unit, period or universe differ."),
    ("UI-VIS-NOMINAL", "Nominal — not adjusted for prices or exchange rates", "اسمية — غير معدلة للأسعار أو لسعر الصرف", "Nominal currency series."),
    # rule-to-outcome chain
    ("UI-VIS-CHAIN-RULE", "Rule or programme", "قاعدة أو برنامج", "Chain step 1."),
    ("UI-VIS-CHAIN-IMPLEMENTATION", "Implementation", "تنفيذ", "Chain step 2."),
    ("UI-VIS-CHAIN-OPERATION", "Operation — activity recorded", "تشغيل — نشاط مسجَّل", "Chain step 3: the rail or service runs and records transactions; not use by people."),
    ("UI-VIS-CHAIN-ACCESS", "Access", "إتاحة الوصول", "Chain step 4."),
    ("UI-VIS-CHAIN-USE", "Use by people or firms", "استخدام الأفراد أو المنشآت", "Chain step 5: needs a person- or firm-level measure."),
    ("UI-VIS-CHAIN-QUALITY", "Quality", "الجودة", "Chain step 6."),
    ("UI-VIS-CHAIN-OUTCOME", "Outcome for people or firms", "الأثر على الأفراد أو المنشآت", "Chain step 7."),
    ("UI-VIS-CHAIN-EVIDENCED", "Evidence reaches this step", "تصل الأدلة إلى هذه الحلقة", "State of a chain step with governed evidence."),
    ("UI-VIS-CHAIN-OPEN", "Not yet measured — not a failure", "لم تُقس بعد — ليس إخفاقًا", "State of a chain step without governed evidence."),
    # detached frame
    ("UI-VIS-DOES-NOT-ESTABLISH", "Does not establish:", "لا يثبت:", "Label before the in-frame prohibited inference."),
    ("UI-VIS-SOURCE", "Source:", "المصدر:", "Label before the in-frame credit line."),
    ("UI-VIS-ISSUER-SCOPE", "Status as recorded by the named authority only; absence from its list is not a status elsewhere.",
     "وضعٌ كما سجلته الجهة المسماة وحدها؛ وعدم الإدراج في قائمتها لا يحدد وضعًا لدى جهة أخرى.", "Provider and status visuals."),
    ("UI-VIS-FULL-RECORD", "Full record:", "السجل الكامل:", "Label before the canonical link in a detached frame."),
]

RMT_ROWS = [
    OrderedDict([("observation_id", "RMO-CBY-2024-AR2024"), ("source_id", "SRC-CBY-AR2024-BOP"), ("series_vintage", "CBY_ANNUAL_REPORT_2024"),
                 ("period_state", "PUBLISHED_VALUE__AR2024_VINTAGE"), ("value", 6245), ("source_table_or_section", "CBY Annual Report 2024 — balance of payments"),
                 ("source_url", "https://english.cby-ye.com/files/68c2ef16b4225.pdf")]),
    OrderedDict([("observation_id", "RMO-CBY-2024-AR2025"), ("source_id", "SRC-CBY-AR2025-BOP"), ("series_vintage", "CBY_ANNUAL_REPORT_2025"),
                 ("period_state", "RESTATED_VALUE__AR2025_VINTAGE"), ("value", 3422.16), ("source_table_or_section", "CBY Annual Report 2025 — balance of payments"),
                 ("source_url", "https://english.cby-ye.com/files/6a54b8fcd8b68.pdf")]),
]
RMT_COMMON = OrderedDict([
    ("domain", "remittances_macro"), ("geography", "CBY publication scope"), ("period", "2024"), ("metric_id", "RMT-001"),
    ("metric_label_en", "External-sector remittances"), ("metric_label_ar", "التحويلات في الحساب الخارجي وفق تعريف المصدر"), ("unit", "USD million"),
    ("evidence_type", "PRIMARY_OFFICIAL_PUBLICATION_VINTAGE"), ("universe", "CBY publication-level BOP remittance series"),
    ("calculation_state", "SOURCE_PUBLISHED"), ("comparability_state", "SAME_REFERENCE_YEAR_DIFFERENT_VINTAGE__DO_NOT_JOIN"),
    ("caveat_en", "One reference year published in two CBY annual-report vintages: a restatement, not a change between years (CLM-032). Not comparable in level with the IMF series (CLM-037)."),
    ("caveat_ar", "سنة مرجعية واحدة منشورة في نسختين من التقرير السنوي للبنك المركزي: هذه إعادة عرض، لا تغير بين عامين (CLM-032). ولا يقارن مستواها بسلسلة صندوق النقد (CLM-037)."),
])


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)

    # 1. grammar labels
    g04 = wb.grid(S04)
    last = max(i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("UI-") and i < 120)
    if g04[last - 1][0] != "UI-EVID-SOURCES-WITHOUT-LOCATOR" or any(c not in (None, "") for c in g04[last]):
        raise TxError("04: interface-copy block end not where expected")
    existing = {r[0] for r in g04 if r and isinstance(r[0], str)}
    if any(a in existing for a, *_ in GRAMMAR):
        raise TxError("04: a UI-VIS label already exists")
    rows = [{1: a, 2: b, 3: c, 4: f"Pre-Tranche-C P3 visual grammar. {d}"} for a, b, c, d in GRAMMAR]
    s.ed.insert_rows(S04, last + 1, rows)
    for a, b, c, _ in GRAMMAR:
        s.ledger.append(OrderedDict([("finding", "P3-G01"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    # 2. CBY vintage rows in 23_REMITTANCES (appended after the last row)
    g23 = wb.grid("23_REMITTANCES")
    hdr = [str(x) for x in g23[3]]
    lastr = max(i for i, r in enumerate(g23, 1) if r and any(c not in (None, "") for c in r))
    if g23[lastr - 1][0] != "RMO-RPW-UAE-2025Q3-500":
        raise TxError("23: last row is not RMO-RPW-UAE-2025Q3-500")
    ids = {r[0] for r in g23}
    new = []
    for spec in RMT_ROWS:
        if spec["observation_id"] in ids:
            raise TxError(f"23: {spec['observation_id']} exists")
        rec = OrderedDict(RMT_COMMON)
        rec.update(spec)
        new.append({hdr.index(k) + 1: v for k, v in rec.items()})
    s.ed.insert_rows("23_REMITTANCES", lastr + 1, new)
    for spec in RMT_ROWS:
        s.ledger.append(OrderedDict([("finding", "P3-F11"), ("sheet", "23_REMITTANCES"), ("row", None), ("col", None),
                                     ("field", spec["observation_id"]), ("old", None), ("new", f"{spec['value']} USD million ({spec['series_vintage']})")]))

    # 3. unit on YSC-013
    g14 = wb.grid("14_SYSTEM_CHRONOLOGY")
    r = next(i for i, x in enumerate(g14, 1) if x and x[0] == "YSC-013")
    s.replace("P3-F11", "14_SYSTEM_CHRONOLOGY", r, 4, "at 6,245 in the 2024 annual-report vintage versus 3,422.16 in the 2025 vintage",
              "at USD 6,245 million in the 2024 annual-report vintage versus USD 3,422.16 million in the 2025 vintage", "YSC-013.fact_en")
    s.replace("P3-F11", "14_SYSTEM_CHRONOLOGY", r, 5, "وردت عند 6,245 في نسخة التقرير السنوي لعام 2024 مقابل 3,422.16 في نسخة 2025",
              "وردت عند 6,245 مليون دولار في نسخة التقرير السنوي لعام 2024 مقابل 3,422.16 مليون دولار في نسخة 2025", "YSC-013.fact_ar")

    rep = s.save(out, ledger, [("transaction", "P3-B"), ("scope", "P3 visual grammar vocabulary; data rows for RV-CWR-001; YSC-013 unit")])
    print(f"P3-B staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
