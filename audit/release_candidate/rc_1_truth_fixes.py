# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-1 — truth fixes (audit/release_candidate/INSTRUCTIONS.md, Part A, G2 items 1–8, 16, 17).

  python3 rc_1_truth_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every cell write states the value it expects to replace (CONTRIBUTING.md §4); a FROM string that is not found exactly
once stops that item. Items whose original source could not be read in this session take the brief's Path B, and the
ledger says so: the execution environment's network policy refuses every external host (imf.org, elibrary.imf.org,
documents.worldbank.org, remittanceprices.worldbank.org, cby-ye.com, web.archive.org — HTTP CONNECT 403), so no
original could be opened.

  1  /people/ education gap: section text, heading and boundary extended to the education gap the VIS-FINDEX-GAPS
     contract already binds (WB-FINDEX-OBS-2022-006 / -007, SRC-WB-FINDEX-AGG-2022).
  2  Compare description (VIS-SOURCE-COMPARISON summary and accessible summary): the six dimensions the runtime compares.
  3  Path B: Methodology lead sentence; the four IMF-attributed chronology events (YSC-008, -014, -015, -017) carry
     "Not yet checked against the original document." in two new 14 columns (verification_note_en / _ar; master
     structure installed with --install).
  4  POS-value notation: the VIS-POS-VALUE series is displayed in whole YER million (one unit, one precision; the
     source-native value stays in source_value_as_reported and in this ledger); every prose citation uses the same
     unit. The remittance prose (6.245 / 3.42 billion) is aligned to the unit and digits of its table (USD million).
  5  CBY-Aden reporting-scope qualifier (the VIS-POS-* universe wording) as governed frame label UI-VIS-NOTE-POS-SCOPE,
     bound to RV-CWR-004 and RV-CWR-009 (controlled input installed with --install; the renderer prints it with the
     lane and the activity rows).
  6  Path B: VIS-FIRM-CONSTRAINTS frame note UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL ("Partial list: 8 of the 16 …").
  7  CLM-003 and the POS legend: describe only what is drawn and say where the release's percentage is stated.
  8  Three firewall questions adjudicated (ledger: CHANGE / KEEP with reasons).
  16 interface_copy use_rule pointers to the current renderer location (PR #8 acceptance C9 / A7 item 8).
  17 Four-digit unit check (audit/release_candidate/four_digit_unit_check.py): the one true instance outside item 4
     (YSC-004: YER 810.9 billion beside YER 1,673 billion) displayed to whole billions; source value kept in the row's
     interpretation_note.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui, ui_block_end  # noqa: E402

S03, S04, S06, S11, S14, S19 = "03_PAGE_SECTIONS", "04_NAV_UX", "06_EVIDENCE_OBJECTS", "11_VISUAL_LIBRARY", "14_SYSTEM_CHRONOLOGY", "19_PAYMENTS_DATA"

NETWORK_NOTE = ("The original could not be read in this session: the execution environment's network policy refuses every external "
                "host (HTTP CONNECT 403 for imf.org, elibrary.imf.org, documents.worldbank.org, remittanceprices.worldbank.org, "
                "cby-ye.com and web.archive.org). Path B of the brief applies.")

# ---------------------------------------------------------------------------------------------------- item 1
I1 = {
    "body_en_from": "Among adults with primary education or less, 6.98% have an account; the matching figure for adults with more education is not in the evidence base, so no education gap is stated.",
    "body_en_to": "Among adults with primary education or less, 6.98% have an account, compared with 19.53% of adults with secondary education or more: a gap of 12.55 percentage points. Adults aged 15–24 (5.01%) and adults aged 25 and over (16.11%) differ by 11.10 percentage points.",
    "body_ar_from": "وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، بينما لا تتضمن قاعدة الأدلة الرقم المقابل لمن تلقوا تعليمًا أعلى، ولذلك لا تُذكر فجوة بحسب التعليم.",
    "body_ar_to": "وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، مقابل 19.53% بين الحاصلين على تعليم ثانوي فأعلى، أي بفارق 12.55 نقطة مئوية. ويبلغ الفارق بين الشباب بعمر 15–24 سنة (5.01%) والبالغين بعمر 25 سنة فأكثر (16.11%) 11.10 نقطة مئوية.",
    "head_en_from": "Measured gaps by sex and income — not yet explanations",
    "head_en_to": "Measured gaps by sex, income, education and age — not yet explanations",
    "head_ar_from": "فجوات مقاسة بحسب الجنس والدخل — من دون افتراض أسبابها",
    "head_ar_to": "فجوات مقاسة بحسب الجنس والدخل والتعليم والعمر — من دون افتراض أسبابها",
    # the page boundary (section 4) names the sex and income gaps; extended to education in the same wording
    "bnd_en_from": "The 12.91-point gender difference and the 9.0-point income difference do not establish their causes.",
    "bnd_en_to": "The 12.91-point gender difference, the 9.0-point income difference, the 12.55-point education difference and the 11.10-point age difference do not establish their causes.",
    "bnd_ar_from": "كما أن فارق 12.91 نقطة بين الرجال والنساء وفارق 9.0 نقاط بين فئتي الدخل لا يثبتان أسبابهما.",
    "bnd_ar_to": "كما أن فارق 12.91 نقطة بين الرجال والنساء وفارق 9.0 نقاط بين فئتي الدخل وفارق 12.55 نقطة بين فئتي التعليم وفارق 11.10 نقطة بين فئتي العمر لا تثبت أسبابها.",
}

# ---------------------------------------------------------------------------------------------------- item 2
I2_EN_FROM = "The comparison table sets the selected records side by side on definition, period, population or calculation base, source scope and method, and on geography and unit where these are recorded."
I2_EN_TO = "The comparison table sets the selected records side by side on definition, population or calculation base, period, method, source and currentness. Check geography and unit in each evidence record before comparing values."
I2_AR_FROM = "يضع جدول المقارنة السجلات المختارة جنبًا إلى جنب من حيث التعريف والفترة والمجتمع أو قاعدة الاحتساب ونطاق المصدر والطريقة، ومن حيث الجغرافيا والوحدة حيث تكون مسجلة."
I2_AR_TO = "يضع جدول المقارنة السجلات المختارة جنبًا إلى جنب من حيث التعريف والمجتمع أو قاعدة الاحتساب والفترة والطريقة والمصدر ومدى الحداثة. وتحقّق من النطاق الجغرافي والوحدة في كل سجل دليل قبل المقارنة بين القيم."   # brief's TO; term aligned to «سجل الدليل» (review 13)

# ---------------------------------------------------------------------------------------------------- item 3 (Path B)
# The brief's Path B TO sentence still claimed every figure "has been checked"; the independent bilingual review showed that the
# site itself contradicts it (the four flagged chronology events carry figures; CLM-039 and CLM-046 print UI-VERIFY-PARTIAL) and
# that the next sentence ("A figure that could not be verified is withheld") then misstates the flagged events. Per the brief
# ("If a TO string … conflicts … record the conflict and the corrected wording"), the corrected wording replaces both sentences.
I3_EN_FROM = ("Every published figure has been checked against the source it is attributed to. A figure that could not be verified is "
              "withheld, and a figure known only from a secondary source is labelled as secondary.")
I3_EN_TO = ("Every figure on this resource's pages and in its evidence records is checked against the source it is attributed to, and any "
            "exception is marked where the figure appears: an evidence record with an input not yet linked to a specific original source "
            "says so, and a dated event in the system chronology that has not yet been checked against its original document carries a "
            "note saying so. A figure that was checked and could not be verified is withheld, and a figure known only from a secondary "
            "source is labelled as secondary.")
I3_AR_FROM = ("رُوجِع كل رقم منشور هنا مقابل المصدر المنسوب إليه. ويُحجب الرقم الذي تعذّر التحقق منه، ويوسم الرقم الذي لا يُعرف إلا "
              "من مصدر ثانوي بأنه ثانوي.")
I3_AR_TO = ("يُراجَع كل رقم في صفحات هذا المورد وسجلات أدلته مقابل المصدر المنسوب إليه، ويُشار إلى أي استثناء حيث يظهر الرقم: فسجل "
            "الدليل الذي لم يُربط أحد مدخلاته بعدُ بمصدر أصلي محدد يذكر ذلك، والحدث المؤرخ في السلسلة الزمنية الذي لم يُراجَع بعدُ "
            "مقابل وثيقته الأصلية تُرفق به ملاحظة بذلك. ويُحجب الرقم الذي رُوجع وتعذّر التحقق منه، ويوسم الرقم الذي لا يُعرف إلا من "
            "مصدر ثانوي بأنه ثانوي.")
FLAG_EN = "This event has not yet been checked against the original source document."   # brief: "Not yet checked against the original document." — subject added (review 9)
FLAG_AR = "لم يُراجَع هذا الحدث بعدُ مقابل وثيقة المصدر الأصلية."
IMF_EVENTS = ("YSC-008", "YSC-014", "YSC-015", "YSC-017")

# ---------------------------------------------------------------------------------------------------- item 4
# VIS-POS-VALUE (19 IND-0004 monthly rows): source-native value → displayed value, whole YER million
POS_VALUE_DISPLAY = [  # observation, month, source-native (as the row records it), displayed
    ("OBS-00053", "2025-03", 320, 320), ("OBS-00056", "2025-04", 317.639, 318), ("OBS-00059", "2025-05", 386.792, 387),
    ("OBS-00062", "2025-06", 535.189, 535), ("OBS-00065", "2025-07", 490.759, 491), ("OBS-00068", "2025-08", 580.021, 580),
    ("OBS-00073", "2025-10", 795.006, 795), ("OBS-00076", "2025-11", 783.583, 784), ("OBS-00079", "2025-12", 910.688, 911),
    ("OBS-00082", "2026-01", 1262, 1262),
]
POS_CAVEAT = " Displayed to whole YER million (RC-1, item 4: one unit and one display precision for the series); the source value as reported is kept in source_value_as_reported."
POS_PROSE = [  # (sheet, row-locator, column, from, to)
    ("EN", "YER 1.262 billion", "YER 1,262 million"),
    ("AR", "1.262 مليار ريال", "1,262 مليون ريال"),
]
# Remittance prose aligned to the unit and digits of its table (USD million; the governed rows RMO-CBY-2024-AR2024 = 6,245
# and RMO-CBY-2024-AR2025 = 3,422.16 are unchanged). Each tuple: (route, section order, lang, FROM, TO).
REMIT_PROSE = [
    ("/readings/same-year-different-number/", 2, "en", "at USD 6.245 billion; the 2025 report restated 2024 at about USD 3.42 billion.",
     "at USD 6,245 million; the 2025 report restated 2024 at USD 3,422.16 million."),
    ("/readings/same-year-different-number/", 2, "ar", "بمبلغ 6.245 مليار دولار، ثم أعاد تقرير 2025 عرض قيمة عام 2024 عند 3.42 مليار دولار تقريبًا.",
     "بمبلغ 6,245 مليون دولار، ثم أعاد تقرير 2025 عرض قيمة عام 2024 عند 3,422.16 مليون دولار."),
    ("/remittances/", 1, "en", "gave remittances of US$6.245 billion, and its 2025 annual report restated the same year at about US$3.42 billion:",
     "gave remittances of US$6,245 million, and its 2025 annual report restated the same year at US$3,422.16 million:"),
    ("/remittances/", 1, "ar", "تحويلات قدرها 6.245 مليار دولار، ثم أعاد تقريره السنوي 2025 عرض السنة نفسها عند نحو 3.42 مليار دولار:",
     "تحويلات قدرها 6,245 مليون دولار، ثم أعاد تقريره السنوي 2025 عرض السنة نفسها عند 3,422.16 مليون دولار:"),
    ("/remittances/", 3, "en", "gave US$6.245 billion, while its 2025 annual report restated 2024 at about US$3.42 billion.",
     "gave US$6,245 million, while its 2025 annual report restated 2024 at US$3,422.16 million."),
    ("/remittances/", 3, "ar", "قيمة قدرها 6.245 مليار دولار، بينما أعاد تقرير 2025 عرض 2024 عند 3.42 مليار دولار تقريبًا.",
     "قيمة قدرها 6,245 مليون دولار، بينما أعاد تقرير 2025 عرض 2024 عند 3,422.16 مليون دولار."),
    ("/remittances/", 9, "en", "gives remittances of about US$3.42 billion, while", "gives remittances of US$3,422.16 million, while"),
    ("/remittances/", 9, "ar", "تحويلات بنحو 3.42 مليار دولار، بينما", "تحويلات قدرها 3,422.16 مليون دولار، بينما"),
]
CLM032 = [  # 06 CLM-032 summary_en / summary_ar
    ("summary_en", "gave USD 6.245 billion, while the 2025 annual report restated 2024 at USD 3.42 billion.",
     "gave USD 6,245 million, while the 2025 annual report restated 2024 at USD 3,422.16 million."),
    ("summary_ar", "عند 6.245 مليار دولار، بينما أعاد التقرير السنوي 2025 عرض عام 2024 عند 3.42 مليار دولار.",
     "عند 6,245 مليون دولار، بينما أعاد التقرير السنوي 2025 عرض عام 2024 عند 3,422.16 مليون دولار."),
]

# ---------------------------------------------------------------------------------------------------- items 5 and 6 (new 04 rows)
UI_POS_SCOPE = ("UI-VIS-NOTE-POS-SCOPE",
                "within the payment-system reporting scope of the Central Bank of Yemen – Aden (CBY-Aden)",
                "ضمن نطاق الإبلاغ عن نظام المدفوعات لدى البنك المركزي اليمني – عدن",
                "RC-1 item 5 (design/ESCALATIONS.md, D6: RV-CWR-004 infrastructure lane and RV-CWR-009 activity rows). The reporting-scope "
                "qualifier of the VIS-POS-* universe, printed after the POS object label on the lane and the activity rows and in their "
                "fallback tables (scripts/yfie/visuals.py dated_lanes, chain_figure); bound through the contracts' frame_labels.")
UI_FIRM_PARTIAL = ("UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL",
                   "Partial list: 8 of the 16 challenges recorded in the source are shown.",
                   "قائمة جزئية: تُعرض 8 من أصل 16 تحديًا مسجّلًا في المصدر.",
                   "RC-1 item 6, Path B (design/ESCALATIONS.md, D6: VIS-FIRM-CONSTRAINTS names sixteen challenges and resolves eight rows). "
                   "Frame note printed by scripts/yfie/visuals.py firm_constraints through the contract's frame_labels; removed the day "
                   "FFO-2022-CH-09…16 are verified against the original and bound.")

# ---------------------------------------------------------------------------------------------------- item 7
I7_LEGEND = {
    "en_from": "Source figures disagree — both are shown",
    "en_to": "Source figures disagree — the published total is plotted; the percentage the release displays is given in the chart note",
    "ar_from": "أرقام المصدر غير متسقة — يُعرض الرقمان",
    "ar_to": "أرقام المصدر غير متسقة — يعرض الرسم البياني الإجمالي المنشور، أما النسبة التي يوردها الإصدار فمذكورة في ملاحظة الرسم",
}
I7_TEXT = {
    "CLM-003": [
        ("summary_en", "both are shown, and the difference is recorded as an inconsistency within the source.",
         "the POS terminals chart plots the published totals, the +11% is stated under 'How was it produced?' in this record, and the difference is recorded as an inconsistency within the source."),
        ("summary_ar", "وتُعرض القيمتان معًا بوصفهما تعارضًا داخل المصدر نفسه.",
         "ويعرض الرسم البياني لأجهزة نقاط البيع الإجماليات المنشورة، وتُذكر نسبة +11% تحت «كيف أُنتج؟» في هذا السجل، ويُسجَّل الفرق بوصفه تعارضًا داخل المصدر نفسه."),
    ],
    "VIS-POS-TERMINALS": [
        ("en", "both the reported totals and the publisher's displayed percentage are shown, and the mismatch is recorded as a discrepancy within the source.",
         "the chart plots the reported totals, the publisher's displayed percentage is given in the chart note, and the mismatch is recorded as a discrepancy within the source."),
        ("ar", "وتُعرض الإجماليات المنشورة والنسبة التي عرضها الناشر معًا، ويُسجَّل الفرق بينهما بوصفه اختلافًا داخل المصدر.",
         "ويعرض الرسم البياني الإجماليات المنشورة، وتُذكر في ملاحظة الرسم النسبةُ التي عرضها الناشر، ويُسجَّل الفرق بينهما بوصفه اختلافًا داخل المصدر."),
    ],
    "VIS-POS-TRANSACTIONS": [
        ("en", "both are shown, and the mismatch is recorded as a discrepancy within the source.",
         "the chart plots the reported totals, the +4.9% is given in the chart note, and the mismatch is recorded as a discrepancy within the source."),
        ("ar", "وتُعرض القيمتان معًا، ويُسجَّل الفرق بينهما بوصفه اختلافًا داخل المصدر.",
         "ويعرض الرسم البياني الإجماليات المنشورة، وتُذكر نسبة +4.9% في ملاحظة الرسم، ويُسجَّل الفرق بينهما بوصفه اختلافًا داخل المصدر."),
    ],
}

# ---------------------------------------------------------------------------------------------------- item 8 (adjudication; filled from the specialist's report)
ITEM8 = OrderedDict()   # written by main() after the cell writes it may imply

# ---------------------------------------------------------------------------------------------------- item 16
I16_FROM, I16_TO = "build.py _domain_labels[", "scripts/yfie/content.py _DOMAIN_LABELS["

# ---------------------------------------------------------------------------------------------------- item 17
# Item 17 — the other true instances the sweep found (one series, two values, a point-only value beside a comma-separated one):
#   the CBY-Aden average market rate (792.69 → 1,529.4 rials per US dollar; 18_CBY_MONETARY OBS-CBY-00621 / OBS-CBY-00657 unchanged)
#   displayed to whole rials, and the SFD savers/depositors series (509,590 at end-2015 beside "1.611 million" at end-2020) displayed
#   as the source-native count 1,611,206 (21_MFI_DATA, SRC-SFD-Q4-2020-001), which the record's sibling figures already use.
I17_RATE = [  # (sheet, key/row locator, field, FROM, TO)
    ("03", ("/finance/", 3, "en"), "moved from 792.69 to 1,529.4 rials per US dollar", "moved from about 793 to about 1,529 rials per US dollar"),
    ("03", ("/finance/", 3, "ar"), "من 792.69 إلى 1,529.4 ريال للدولار", "من نحو 793 إلى نحو 1,529 ريالًا للدولار"),
    ("06", ("CLM-054", "summary_en"), "moved from 792.69 to 1,529.4 rials per US dollar", "moved from about 793 to about 1,529 rials per US dollar"),
    ("06", ("CLM-054", "summary_ar"), "من 792.69 إلى 1,529.4 ريال للدولار", "من نحو 793 إلى نحو 1,529 ريالًا للدولار"),
]
I17_SAVERS = [
    ("03", ("/finance/", 3, "en"), "The verified 2020 figures are 1.611 million savers/depositors", "The verified 2020 figures are 1,611,206 savers/depositors"),
    ("03", ("/finance/", 3, "ar"), "فهي 1.611 مليون مدخر/مودع", "فهي 1,611,206 من المدخرين/المودعين"),
    ("03", ("/readings/microfinance-structural-divergence/", 4, "en"), "shows about 1.611 million savers or depositors.", "shows 1,611,206 savers or depositors."),
    ("03", ("/readings/microfinance-structural-divergence/", 4, "ar"), "لعام 2020 نحو 1.611 مليون مدخر أو مودع.", "لعام 2020 عددًا قدره 1,611,206 من المدخرين أو المودعين."),
    ("06", ("CLM-054", "summary_en"), "the verified 2020 anchors are 1.611 million savers/depositors", "the verified 2020 anchors are 1,611,206 savers/depositors"),
    ("06", ("CLM-054", "summary_ar"), "قدرها 1.611 مليون مدخر/مودع", "قدرها 1,611,206 من المدخرين/المودعين"),
    ("11", ("VIS-MFI-DIVERGENCE", "accessible_summary_en"), "88,445 borrowers and 1.611 million savers/depositors at end-2020", "88,445 borrowers and 1,611,206 savers/depositors at end-2020"),
    ("11", ("VIS-MFI-DIVERGENCE", "accessible_summary_ar"), "و88,445 مقترضًا و1.611 مليون مدخر/مودع في نهاية 2020", "و88,445 مقترضًا و1,611,206 من المدخرين/المودعين في نهاية 2020"),
]
I17 = {  # YSC-004: one series (currency outside banks, YER billion) printed with a decimal point and a thousands comma
    "en_from": "rose from YER810.9 billion in 2014 to YER1,673 billion by end-2017",
    "en_to": "rose from about YER 811 billion in 2014 to YER 1,673 billion by end-2017",
    "ar_from": "من 810.9 مليار ريال في 2014 إلى 1,673 مليار ريال بنهاية 2017",
    "ar_to": "من نحو 811 مليار ريال في 2014 إلى 1,673 مليار ريال بنهاية 2017",
    "note": "RC-1 item 17: the source value YER 810.9 billion (2014) is displayed as YER 811 billion so that the two values of this series share one display precision (whole YER billion); the 2017 value 1,673 is as published.",
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()

    # ---- item 1 · /people/ education gap (03 rows: EN 192, AR 193; boundary EN 194, AR 195)
    s.set_section("RC-1:ITEM-01", "/people/", 3, "en", "heading", I1["head_en_to"], I1["head_en_from"])
    s.replace_section("RC-1:ITEM-01", "/people/", 3, "en", "body", I1["body_en_from"], I1["body_en_to"])
    s.set_section("RC-1:ITEM-01", "/people/", 3, "ar", "heading", I1["head_ar_to"], I1["head_ar_from"])
    s.replace_section("RC-1:ITEM-01", "/people/", 3, "ar", "body", I1["body_ar_from"], I1["body_ar_to"])
    s.replace_section("RC-1:ITEM-01", "/people/", 4, "en", "body", I1["bnd_en_from"], I1["bnd_en_to"])
    s.replace_section("RC-1:ITEM-01", "/people/", 4, "ar", "body", I1["bnd_ar_from"], I1["bnd_ar_to"])
    notes["item_1"] = "DONE — section 3 heading and body, and the section-4 boundary, extended to the education gap VIS-FINDEX-GAPS binds (WB-FINDEX-OBS-2022-006/-007, SRC-WB-FINDEX-AGG-2022)."

    # ---- item 2 · Compare description (06 VIS-SOURCE-COMPARISON summary; 11 accessible summary)
    t06 = Table(s, S06); t11 = Table(s, S11)
    s.replace("RC-1:ITEM-02", S06, t06.rows["VIS-SOURCE-COMPARISON"], t06.col("summary_en"), I2_EN_FROM, I2_EN_TO, "VIS-SOURCE-COMPARISON.summary_en")
    s.replace("RC-1:ITEM-02", S06, t06.rows["VIS-SOURCE-COMPARISON"], t06.col("summary_ar"), I2_AR_FROM, I2_AR_TO, "VIS-SOURCE-COMPARISON.summary_ar")
    s.replace("RC-1:ITEM-02", S11, t11.rows["VIS-SOURCE-COMPARISON"], t11.col("accessible_summary_en"), I2_EN_FROM, I2_EN_TO, "VIS-SOURCE-COMPARISON.accessible_summary_en")
    s.replace("RC-1:ITEM-02", S11, t11.rows["VIS-SOURCE-COMPARISON"], t11.col("accessible_summary_ar"), I2_AR_FROM, I2_AR_TO, "VIS-SOURCE-COMPARISON.accessible_summary_ar")
    notes["item_2"] = "DONE — both governed cells in each language (the FROM sentence occurs once in each)."

    # ---- item 3 · Path B: Methodology lead and the four IMF-attributed events
    s.replace_section("RC-1:ITEM-03", "/methodology/", 1, "en", "body", I3_EN_FROM, I3_EN_TO)
    s.replace_section("RC-1:ITEM-03", "/methodology/", 1, "ar", "body", I3_AR_FROM, I3_AR_TO)
    head14 = s.header(S14, 4)
    if len(head14) != 17 or head14[16] != "period_ar":
        raise TxError(f"14 header not as expected: {head14}")
    s.set("RC-1:ITEM-03", S14, 4, 18, "verification_note_en", None, "14 header")
    s.set("RC-1:ITEM-03", S14, 4, 19, "verification_note_ar", None, "14 header")
    t14 = Table(s, S14)
    for eid in IMF_EVENTS:
        if t14.get(eid, "source_ids") != "SRC-IMF-AIV-2025-STAFF-001":
            raise TxError(f"{eid} is not attributed to SRC-IMF-AIV-2025-STAFF-001 alone")
        s.set("RC-1:ITEM-03", S14, t14.rows[eid], 18, FLAG_EN, None, f"{eid}.verification_note_en")
        s.set("RC-1:ITEM-03", S14, t14.rows[eid], 19, FLAG_AR, None, f"{eid}.verification_note_ar")
    notes["item_3"] = ("PATH B — " + NETWORK_NOTE + " The Methodology lead sentence is replaced and YSC-008, YSC-014, YSC-015 and YSC-017 carry the flag in the new "
                       "14 columns verification_note_en/_ar (scripts/projection/master_structure.json installed with --install; rendered with each event). "
                       "Register EXT-01 stays open until a primary read; the flag is removed Master-first when it happens.")

    # ---- item 4 · POS-value notation and the prose that cites it
    t19 = Table(s, S19)
    disp = []
    for oid, month, native, shown in POS_VALUE_DISPLAY:
        cur = t19.get(oid, "value")
        if str(cur) != str(native) and not (isinstance(cur, (int, float)) and float(cur) == float(native)):
            raise TxError(f"{oid} value holds {cur!r}, expected {native!r}")
        if t19.get(oid, "unit") != "YER_million":
            raise TxError(f"{oid} unit is not YER_million")
        if shown != native:
            t19.set("RC-1:ITEM-04", oid, "value", shown, cur)
            cav = t19.get(oid, "caveats") or ""
            t19.set("RC-1:ITEM-04", oid, "caveats", cav + POS_CAVEAT, cav)
        disp.append(OrderedDict([("observation", oid), ("month", month), ("source_native", t19.get(oid, "source_value_as_reported")),
                                 ("master_value_before", native), ("displayed", shown), ("unit", "YER million (nominal)")]))
    for lang, frm, to in POS_PROSE:
        L = lang.lower()
        s.replace_section("RC-1:ITEM-04", "/payments/", 2, L, "body", frm, to)
        s.replace("RC-1:ITEM-04", S06, t06.rows["VIS-POS-VALUE"], t06.col(f"summary_{L}"), frm, to, f"VIS-POS-VALUE.summary_{L}")
        s.replace("RC-1:ITEM-04", S11, t11.rows["VIS-POS-VALUE"], t11.col(f"accessible_summary_{L}"), frm, to, f"VIS-POS-VALUE.accessible_summary_{L}")
    for route, order, L, frm, to in REMIT_PROSE:
        s.replace_section("RC-1:ITEM-04", route, order, L, "body", frm, to)
    for L, add in (("en", " Each value is shown to the nearest million rials (for example, 317.639 million is shown as 318)."),
                   ("ar", " وتُعرض كل قيمة مقرّبة إلى أقرب مليون ريال (فمثلًا تُعرض 317.639 مليون ريال على أنها 318).")):
        cur = t06.get("VIS-POS-VALUE", f"method_{L}")
        t06.set("RC-1:ITEM-04", "VIS-POS-VALUE", f"method_{L}", cur + add, cur)
    for fld, frm, to in CLM032:
        s.replace("RC-1:ITEM-04", S06, t06.rows["CLM-032"], t06.col(fld), frm, to, f"CLM-032.{fld}")
    notes["item_4"] = OrderedDict([
        ("decision", "The VIS-POS-VALUE series (nominal YER million) is displayed to whole YER million: no value in the series now carries a decimal point, "
                     "so none can be misread against the thousands comma of 1,262; the unit label (UI-VIS-UNIT-YER-MILLION) heads every value and the prose "
                     "writes the unit beside the value in both languages (YER 1,262 million / 1,262 مليون ريال). Source-native values stay in "
                     "source_value_as_reported, normalized_value and this ledger; each changed row's caveats cell records the display rule."),
        ("series_display", disp),
        ("remittances", "The CBY-Aden 2024 vintages (RMO-CBY-2024-AR2024 = 6,245; RMO-CBY-2024-AR2025 = 3,422.16 US$ million) are unchanged; the prose that "
                        "cited them in billions (USD 6.245 billion / about USD 3.42 billion; 6.245 مليار دولار / 3.42 مليار دولار تقريبًا) now uses the table's "
                        "unit and digits (USD 6,245 million / USD 3,422.16 million) on /remittances/ §1, §3, §9, the Reading same-year-different-number §2 and "
                        "CLM-032. Every value of the series carries the thousands comma, so no point-only value exists to be misread; the derived claims of "
                        "CLM-037 (0.0032 pp; 1.838) keep their exact inputs."),
        ("kept", ["CLM-034 / /remittances/ residual prose (US$7.117 billion against US$3.614 billion; 1.97): a prose-only pair in one unit and one precision; "
                  "the 2025 remittance row (3,614.05) is context-only and drawn in no table, so no table/prose split exists.",
                  "MFI portfolio prose (YER 6.741 / 33.379 / 44 billion): one unit, three-decimal precision, no table counterpart (TABLE_TEXT_FIRST contracts without rows)."]),
    ])

    # ---- item 7 · CLM-003 and the POS legend: describe only what is drawn
    set_ui(s, "RC-1:ITEM-07", "UI-VIS-DISAGREEMENT", I7_LEGEND["en_to"], I7_LEGEND["ar_to"], I7_LEGEND["en_from"], I7_LEGEND["ar_from"])
    for fld, frm, to in I7_TEXT["CLM-003"]:
        s.replace("RC-1:ITEM-07", S06, t06.rows["CLM-003"], t06.col(fld), frm, to, f"CLM-003.{fld}")
    for vid in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS"):
        for L, frm, to in I7_TEXT[vid]:
            s.replace("RC-1:ITEM-07", S06, t06.rows[vid], t06.col(f"summary_{L}"), frm, to, f"{vid}.summary_{L}")
            s.replace("RC-1:ITEM-07", S11, t11.rows[vid], t11.col(f"accessible_summary_{L}"), frm, to, f"{vid}.accessible_summary_{L}")
    notes["item_7"] = ("DONE — the legend UI-VIS-DISAGREEMENT, CLM-003 and the VIS-POS-TERMINALS / VIS-POS-TRANSACTIONS summaries (06 and 11) now say that the "
                       "published totals are drawn and that the release's percentage is stated in the record's method text (which the disagreement note prints "
                       "under the terminals panel). No row added; the method texts, which already give both figures, are unchanged.")

    # ---- item 16 · use_rule pointers (C9 / A7 item 8)
    _, ui = ui_block_end(s)
    g04 = s.grid(S04)
    n16 = 0
    for ui_id, row in sorted(ui.items(), key=lambda kv: kv[1]):
        cur = g04[row - 1][3]
        if isinstance(cur, str) and I16_FROM in cur:
            special = {"build.py _domain_labels['visual_question']": "scripts/yfie/content.py visual() labels['analytical_question']",
                       "build.py _domain_labels['text_alternative']": "scripts/yfie/content.py visual() labels['text_alternative']"}
            if cur in special:   # keys that live in visual(), not in _DOMAIN_LABELS (review 8)
                s.set("RC-1:ITEM-16", S04, row, 4, special[cur], cur, f"{ui_id}.use_rule")
            else:
                s.replace("RC-1:ITEM-16", S04, row, 4, I16_FROM, I16_TO, f"{ui_id}.use_rule")
            n16 += 1
    if n16 != 20:
        raise TxError(f"item 16: expected 20 use_rule cells naming build.py _domain_labels, found {n16}")
    notes["item_16"] = f"DONE — {n16} use_rule cells now point to scripts/yfie/content.py _DOMAIN_LABELS (audit/PR8_INDEPENDENT_ACCEPTANCE.md A7 item 8, C9)."

    # ---- item 17 · four-digit unit check: the one true instance outside item 4
    s.replace("RC-1:ITEM-17", S14, t14.rows["YSC-004"], t14.col("fact_en"), I17["en_from"], I17["en_to"], "YSC-004.fact_en")
    s.replace("RC-1:ITEM-17", S14, t14.rows["YSC-004"], t14.col("fact_ar"), I17["ar_from"], I17["ar_to"], "YSC-004.fact_ar")
    if t14.get("YSC-004", "interpretation_note") not in (None, ""):
        raise TxError("YSC-004 interpretation_note is not empty")
    s.set("RC-1:ITEM-17", S14, t14.rows["YSC-004"], t14.col("interpretation_note"), I17["note"], None, "YSC-004.interpretation_note")
    for sheet, loc, frm, to in I17_RATE + I17_SAVERS:
        if sheet == "03":
            route, order, L = loc
            # the section is located by its order and language (/finance/ §3 Analysis; the Reading's §4)
            row = s.section_row(route, order, L)
            s.replace("RC-1:ITEM-17", S03, row, 5 if L == "en" else 7, frm, to, f"{route}#s{order}.body_{L}")
        elif sheet == "06":
            key, fld = loc
            s.replace("RC-1:ITEM-17", S06, t06.rows[key], t06.col(fld), frm, to, f"{key}.{fld}")
        else:
            key, fld = loc
            s.replace("RC-1:ITEM-17", S11, t11.rows[key], t11.col(fld), frm, to, f"{key}.{fld}")
    notes["item_17_display"] = [
        OrderedDict([("series", "CBY-Aden average market rate, rials per US dollar (CLM-054; /finance/)"), ("source_native", ["792.69 (December 2020; 18_CBY_MONETARY OBS-CBY-00621)", "1529.4 (December 2023; OBS-CBY-00657)"]),
                     ("displayed", ["793", "1,529"]), ("rule", "whole rials; the 18 rows keep the exact values")]),
        OrderedDict([("series", "SFD savers/depositors (VIS-MFI-DIVERGENCE; CLM-054; /finance/; Reading microfinance-structural-divergence)"), ("source_native", ["509,590 (end-2015)", "1,611,206 (end-2020; 21_MFI_DATA, SRC-SFD-Q4-2020-001)"]),
                     ("displayed", ["509,590", "1,611,206"]), ("rule", "the source-native count in place of the rounded '1.611 million', so both values of the series share one notation")]),
        OrderedDict([("series", "Currency outside banks, YER billion (YSC-004)"), ("source_native", ["810.9 (2014)", "1,673 (end-2017)"]), ("displayed", ["811", "1,673"]),
                     ("rule", "whole YER billion; the source value is kept in the row's interpretation_note")]),
    ]
    notes["item_17"] = ("DONE — audit/release_candidate/four_digit_unit_check.py swept every public figure of four or more digits (report in "
                        "audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md). True instances: the VIS-POS-VALUE series (item 4), the remittance prose/table unit split "
                        "(item 4), YSC-004 (YER 810.9 billion beside YER 1,673 billion; whole YER billion, the source value kept in the row's interpretation_note), "
                        "the CBY-Aden average market rate (792.69 beside 1,529.4; whole rials) and the SFD savers series ('1.611 million' beside 509,590; the "
                        "source-native count 1,611,206). Not instances: axis and index labels, table cells whose unit is their column header, percentages, "
                        "figures of different series in one sentence, identifiers and project numbers (see the report).")

    # ---- items 5 and 6 · new governed frame labels (rows appended to the 04 interface-copy block; inserts last so no earlier row index moves)
    insert_ui_rows(s, "RC-1:ITEM-05", [UI_POS_SCOPE])
    insert_ui_rows(s, "RC-1:ITEM-06", [UI_FIRM_PARTIAL])
    notes["item_5"] = ("DONE — UI-VIS-NOTE-POS-SCOPE carries the VIS-POS-* universe qualifier verbatim; bound to RV-CWR-004 and RV-CWR-009 through the controlled "
                       "visual design contract (frame_labels, installed with --install) and printed by the renderer after the POS object label on the "
                       "infrastructure lane, the activity rows and their fallback tables. The two alt texts already carried the qualifier (RV-CWR-004: 'within "
                       "the reporting scope of the Central Bank of Yemen – Aden (CBY-Aden)'; RV-CWR-009: 'within CBY-Aden's reporting scope') and are unchanged.")
    notes["item_6"] = ("PATH B — " + NETWORK_NOTE + " FFO-2022-CH-09…16 stay unbound (their values exist in 20_FIRM_FINANCE with the locator 'Annex III, Table 8 / "
                       "Figure 108, p.146' but were not checked against that page); the governed frame note UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL is bound to "
                       "VIS-FIRM-CONSTRAINTS and printed in frame.")

    # ---- item 8 · firewall adjudication (see ITEM8 below; cell writes, if any, are made here)
    item8_writes = item8(s, t06, t11)
    notes["item_8"] = ITEM8
    notes["item_8"]["cells_written"] = item8_writes

    # 02 full_copy is derived by the generator since TC-S1 (scripts/projection/derived.py _full_copy); nothing to write here.

    notes["independent_review"] = OrderedDict([
        ("reviewer", "independent subagent that did not write the transaction (senior Arab economic editor and senior institutional English editor lenses)"),
        ("verdict_before_fixes", "NOT ACCEPTABLE AS-IS: 1 BLOCKING, 6 SHOULD FIX, 8 OPTIONAL"),
        ("applied", ["1 BLOCKING Methodology lead (brief's Path B TO conflicts with the site's own flags; corrected wording applied, conflict recorded)",
                     "2 legend wording", "3 POS summaries name the chart note", "4 CLM-003 names its own section", "5 Arabic counted nouns after 1,611,206",
                     "6 Arabic accusative after 1,529", "7 rounding disclosed (about …; VIS-POS-VALUE method)", "8 two use_rule pointers to visual()",
                     "9 verification note names its subject", "10 'challenges' in the partial-list note", "11 the age gap on /people/ (governed in VIS-FINDEX-GAPS)",
                     "12 Arabic parallelism «بين فئتي التعليم»", "13 «كل سجل دليل»"]),
        ("not_applied", ["14 CLM-032 'balance of payments' qualifier: pre-existing asymmetry, recorded for the Part B Arabic/English editorial pass",
                         "15 «السلسلة الزمنية» → «التسلسل الزمني» programme-wide: Part B, B2 (one Arabic term per concept)",
                         "10 follow-up: /firms/ §2 prose reads as a complete list — Part B"]),
    ])
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-1"), ("summary", "Release-candidate truth fixes: items 1–8, 16, 17 of audit/release_candidate/INSTRUCTIONS.md Part A G2"),
                                           ("environment_note", NETWORK_NOTE), ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


def item8(s, t06, t11):
    """Three firewall questions of design/ESCALATIONS.md adjudicated against the governed data and the sources' own governed text
    (the originals could not be re-read in this session). Returns the number of cells written."""
    written = 0
    ITEM8["a_RV-CWR-009_VIS-PAYMENT-RAILS_NETWORK_ACTIVITY_SIGNAL"] = OrderedDict([
        ("verdict", "KEEP"),
        ("reason", "The OPERATION step of the chain is defined by the contract as 'activity counts evidence operation, not use' and already holds the POS "
                   "transaction counts (OBS-00081). REF-PAY-009 is an attributed CBY-Aden statement about activity on the unified network (January 2026): it "
                   "is evidence that the network was operating at that date in the sense the chain uses (recorded activity), and nothing stronger. Both "
                   "contracts guard the reading: the step is labelled with its governed state, the alt texts call it 'an attributed CBY-Aden statement' / "
                   "'CBY-Aden's own statement, not an independent measurement', ACCESS and USE stay OPEN, and the prohibited inference says a go-live or "
                   "event does not show access, use, quality or outcome. Licence ≠ operation is kept: the event is not placed at RULE or IMPLEMENTATION "
                   "as if a licence proved operation, and it is not promoted to ACCESS or USE. Mapping it lower would present recorded activity as a rule, "
                   "which the source does not say. The specialist's proposal to qualify the event's governed label (UI-VIS-CAT-EVT-EXHIBITION) with "
                   "'— a statement, not recorded activity' is new interface copy, which Part A does not author; it is recorded for the Part B editorial "
                   "pass, together with the VIS-PAYMENT-RAILS alt-text phrase 'the only information on use' (the grammar maps activity to operation, not use)."),
    ])
    ITEM8["b_VIS-REMITTANCE-COST_MEASURED"] = OrderedDict([
        ("verdict", "CHANGE — series state MEASURED → REPORTED (controlled visual design contract, installed with --install; the renderer's panel header "
                    "follows the series state instead of a literal)"),
        ("reason", "The governed grammar defines MEASURED ('Measured in a survey' / 'مقيس في مسح') by its use_rule 'Value from a survey measure of the stated "
                   "population', and REPORTED ('Reported by the source' / 'وارد في المصدر') as 'Official statistics reported by a source that are neither a "
                   "survey measure nor an administrative count'. The four RPW values are averages the World Bank publishes from a standardised collection of "
                   "provider price quotes (23_REMITTANCES: period_state OBSERVED_QUOTE_COLLECTION_PERIOD, calculation_state SOURCE_PUBLISHED_AVERAGE; the "
                   "record's method: 'from standardized collection of provider price quotes'; passport EP-WB-RPW-KSA-YEM-K04: 'Standardized primary price "
                   "collection'). Their universe is a set of listed products in two corridors, not a population of people or firms, and no governed field "
                   "calls the collection a survey. MEASURED is the token this product reserves for population-survey measures (Findex, the 2022 firm survey); "
                   "lending it to price quotes weakens the people-side meaning the semantic firewall depends on. REPORTED is the exact governed fit; the mark "
                   "and line do not change (both states draw a filled circle), only the printed state label. The governed frame note 'Average of quotes for "
                   "this amount — not the cost of all remittances' and the record text stay."),
        ("edits", ["scripts/projection/controlled_inputs/visual_design_contract.json: VIS-REMITTANCE-COST contract.series[rpw].state MEASURED → REPORTED (installed)",
                   "scripts/yfie/visuals.py remittance_cost(): the panel header prints the series' state label, not a literal MEASURED"]),
        ("needs_original", "Whether the RPW methodology page itself uses the word 'survey' could not be read here; it does not change the governed definition that decides this verdict."),
    ])
    ITEM8["c_RV-CWR-001_imf_staff_path_REPORTED"] = OrderedDict([
        ("verdict", "KEEP"),
        ("reason", "The IMF rows for 2018–2024 (RMO-IMF-*-HIST) carry period_state HISTORICAL_REPORTED and calculation_state "
                   "SOURCE_REPORTED__IMF_STAFF_CALCULATIONS: the staff report publishes them as its external-sector table values for past years, which the "
                   "resource reports as the source reports them; the 2025 value is ESTIMATE and 2026–2030 PROJECTION, and VIS-REMITTANCE-MACRO draws those "
                   "states hollow and dashed. The Reading's prose describes the IMF path as a staff reconstruction with a modelled personal-transfers "
                   "component — that is a statement about how the source built its series, and the record's universe already says the series is 'on the "
                   "IMF's analytical scope for areas under the internationally recognized government'. REPORTED ('Reported by the source') is the governed "
                   "state for a value a source publishes as data, whether or not the source derived it; ESTIMATED ('Estimate — not an observation') is "
                   "reserved for values the source itself labels estimates. Changing 2018–2024 to ESTIMATED would contradict the IMF table's own presentation "
                   "as read at ingestion, and the original cannot be re-read here to settle it; the Reading's wording stands as the place where the "
                   "reconstruction is explained. The specialist's companion proposal — the RV-CWR-001 universe to carry '(reported history based on staff "
                   "calculations)' as VIS-REMITTANCE-MACRO and CLM-007 already do — is a wording improvement, not a state correction; recorded for Part B."),
    ])
    return written


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
