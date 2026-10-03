# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-11: Part B items B10 (accessibility) and B11 (/payments/ frame note), with the
independent review of RC-10 folded in (RC-10b).

  python3 rc_11_b10_b11.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

B10 b (NCC-02): every fallback table names its row-header column with a governed label that fits it. The axe rule
    `empty-table-header` found 12 empty corner cells. The labels are period, group, corridor and amount, object, step,
    dimension, date and item (scripts/yfie/visuals.py `th`).
B11 VIS-POS-TRANSACTIONS carries one frame note, bound by rc_11_stage_inputs.py, written only from governed fields:
    - the first-half 2025 payment-system report also gives a POS-transaction total (OBS-00036);
    - this resource withholds it, because its governed caveat requires a methodology note before public use, and it
      prints as WITHHELD in VIS-PAYMENT-ANATOMY;
    - the monthly releases are shown because each is DIRECTLY_COMPARABLE: the same POS measures, one month, the same
      reporting scope.
B10 a (code, scripts/yfie/render.py): a spine's edge group is named by its own heading and the page's h1, so it no
    longer shares the name "Continue from here" with the page's next-actions landmark (axe `landmark-unique`).
RC-10b — the independent review of RC-10 (ACCEPTABLE; eleven should-fix items, all applied):
    - ELS-009 «الجنس», the site's term.
    - ELS-018 «النشط» for "active"; the programme baseline linked; the type is secondary analysis and programme record.
    - ELS-019 names its scope (POS, CBY-Aden reporting scope).
    - ELS-020 is regulatory material only, because the survey variable is not computed.
    - ELS-022 people, not households (CLM-030 counts adults).
    - ELS-026 links CLM-015, the 2024 list of unlicensed e-payment services (regulatory material, a measurement gap).
    - ELS-027 links CLM-054, the SFD primary tables.
    - ELS-032 names MSMEs.
    - UI-LAND-COL-NEXT in Arabic says «قد» (would), not a definite future.
    - A new label UI-LAND-NO-NEXT replaces an ungoverned "·".
    - A period's closing full stop is dropped before the joiner (code).
    - VIS-EVIDENCE-FRESHNESS lists its member records, so its record reads as a composite of the linked records.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui  # noqa: E402

F10, F11, F10B = "RC-11:B10", "RC-11:B11", "RC-10b"
TH = [("UI-VIS-TH-PERIOD", "Period", "الفترة"), ("UI-VIS-TH-GROUP", "Group", "الفئة"),
      ("UI-VIS-TH-CORRIDOR", "Corridor and amount", "الممر والمبلغ"), ("UI-VIS-TH-OBJECT", "What is counted", "ما يُعدّ"),
      ("UI-VIS-TH-STEP", "Step", "الخطوة"), ("UI-VIS-TH-DIMENSION", "Dimension", "البُعد"),
      ("UI-VIS-TH-DATE", "Date", "التاريخ"), ("UI-VIS-TH-ITEM", "Item", "البند")]
TH_RULE = "RC-11 (Part B B10 b, NCC-02). The heading of a fallback table's row-header column; no corner cell is empty."
NOTE = ("UI-VIS-NOTE-POS-H1-WITHHELD",
        "The payment-system report for the first half of 2025 also gives a POS-transaction total for that half-year. It is "
        "withheld here because its definition and period need a methodology note before public use. The monthly releases "
        "are shown because each reports the same POS measures for one month within the same reporting scope, so "
        "consecutive months are comparable.",
        "يذكر تقرير نظام المدفوعات للنصف الأول من 2025 أيضًا إجماليًا لمعاملات نقاط البيع في ذلك النصف، وهو محجوب هنا "
        "لأن تعريفه وفترته يحتاجان إلى ملاحظة منهجية قبل النشر. أما الإصدارات الشهرية فتُعرض لأن كلًّا منها يذكر مقاييس "
        "نقاط البيع نفسها لشهر واحد ضمن نطاق الإبلاغ نفسه، فتكون الأشهر المتتالية قابلة للمقارنة.",
        "RC-11 (Part B B11). Frame note of VIS-POS-TRANSACTIONS: the withheld H1 2025 transaction total (OBS-00036) and why "
        "the monthly series is admissible; from governed fields only.")
LAND = ("00_MASTER", 51)
MEMBERS = ["CLM-001", "CLM-025", "CLM-029", "CLM-031", "CLM-028", "CLM-013", "VIS-FL-EVIDENCE-LADDER", "VIS-FINDEX-RESILIENCE",
           "CLM-002", "VIS-FINDEX-GAPS", "XW-FMIIP-005", "CLM-052", "CLM-050", "FMIIP-BASELINE-2025-01", "CLM-003", "CLM-017",
           "CLM-012", "CLM-045", "CLM-030", "CLM-007", "CLM-032", "VIS-REMITTANCE-COST", "CLM-008", "CLM-009", "CLM-019",
           "CLM-015", "CLM-053", "CLM-054", "CLM-033", "CLM-038", "CLM-005", "CLM-006", "CLM-059", "CLM-060", "CLM-011",
           "DS-FCP-ARCH", "CLM-018"]
REVIEW = [  # RC-10b: (finding, kind, args)
    (F10B, "table", (*LAND, "ELS-009", "dimension_ar", "الجنس", "النوع الاجتماعي")),
    (F10B, "table", (*LAND, "ELS-018", "dimension_ar", "الاستخدام النشط ومدى تكراره", "الاستخدام الفعلي ومدى تكراره")),
    (F10B, "table", (*LAND, "ELS-018", "record_ids", '["CLM-050", "FMIIP-BASELINE-2025-01"]', '["CLM-050"]')),
    (F10B, "table", (*LAND, "ELS-018", "evidence_class", "ANALYTICAL;PROGRAMME", "SURVEY;ANALYTICAL;PROGRAMME")),
    (F10B, "table", (*LAND, "ELS-019", "dimension_en", "Payment infrastructure (POS, CBY-Aden reporting scope)", "Payment infrastructure")),
    (F10B, "table", (*LAND, "ELS-019", "dimension_ar", "البنية التحتية للمدفوعات (نقاط البيع، ضمن نطاق إبلاغ البنك المركزي اليمني – عدن)",
                     "البنية التحتية للمدفوعات")),
    (F10B, "table", (*LAND, "ELS-020", "evidence_class", "REGULATORY", "REGULATORY;SURVEY")),
    (F10B, "table", (*LAND, "ELS-022", "dimension_en", "Remittances received by people", "Remittances received by households")),
    (F10B, "table", (*LAND, "ELS-022", "dimension_ar", "التحويلات التي يتلقاها الأفراد", "التحويلات التي تتلقاها الأسر")),
    (F10B, "table", (*LAND, "ELS-026", "record_ids", '["CLM-015"]', "[]")),
    (F10B, "table", (*LAND, "ELS-026", "evidence_class", "REGULATORY", None)),
    (F10B, "table", (*LAND, "ELS-026", "coverage_state", "MEASUREMENT_GAP", "NO_EVIDENCE")),
    (F10B, "table", (*LAND, "ELS-026", "verify_routes", '["/providers/"]', "[]")),
    (F10B, "table", (*LAND, "ELS-027", "record_ids", '["CLM-053", "CLM-054"]', '["CLM-053"]')),
    (F10B, "table", (*LAND, "ELS-032", "dimension_en", "Reach of programmes for MSMEs", "Reach of programmes for small firms")),
    (F10B, "table", (*LAND, "ELS-032", "dimension_ar", "وصول البرامج إلى المنشآت الأصغر والصغيرة والمتوسطة", "وصول البرامج إلى المنشآت الصغيرة")),
    (F10B, "ui", ("UI-LAND-COL-NEXT", None, "أين يُتحقق منه · ما الذي قد يغيّره", None, "أين يُتحقق منه · ما الذي سيغيّره")),
    (F10B, "table", ("06_EVIDENCE_OBJECTS", 4, "VIS-EVIDENCE-FRESHNESS", "source_dependencies", "; ".join(MEMBERS), None)),
    # a listed composite prints the governed template UI-VERIFY-COMPOSITE (the generator holds the 06 text to it)
    (F10B, "table", ("06_EVIDENCE_OBJECTS", 4, "VIS-EVIDENCE-FRESHNESS", "verification_en",
                     "This view assembles other evidence records. Check each linked record against its own source.",
                     "This view summarises other evidence records, which are not yet linked individually here. Before reusing a figure, "
                     "open the evidence record that reports it and check that record against its own source.")),
    (F10B, "table", ("06_EVIDENCE_OBJECTS", 4, "VIS-EVIDENCE-FRESHNESS", "verification_ar",
                     "يجمع هذا العرض سجلات أدلة أخرى، فطابِق كل سجل مرتبط مع مصدره.",
                     "يلخص هذا العرض سجلات أدلة أخرى لم تُربط بعدُ هنا كلٌّ على حدة. وقبل إعادة استخدام أي رقم، افتح سجل الدليل الذي "
                     "يورده وطابِقه مع مصدره.")),
]
NO_NEXT = ("UI-LAND-NO-NEXT", "No domain page or measurement priority in this base",
           "لا توجد صفحة مجال ولا أولوية قياس في قاعدة الأدلة هذه",
           "RC-10b. Evidence landscape: the last cell of a row that has neither a domain page nor a priority.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, F10, [(a, b, c, TH_RULE) for a, b, c in TH])
    insert_ui_rows(s, F11, [NOTE])
    insert_ui_rows(s, F10B, [NO_NEXT])
    for finding, kind, args in REVIEW:
        if kind == "ui":
            set_ui(s, finding, *args)
        elif kind == "cell":
            s.replace(finding, *args)
        elif kind == "table":
            sheet, header_row, key, field, new, old = args
            Table(s, sheet, header_row).set(finding, key, field, new, old)
        else:
            raise TxError(f"unknown review kind {kind}")
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-11"), ("summary", "B10 corner labels; B11 frame note; RC-10 review"),
                                           ("items", OrderedDict([("B10b", len(TH)), ("B11", 1), ("RC-10b", len(REVIEW))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
