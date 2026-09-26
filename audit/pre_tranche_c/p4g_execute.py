# -*- coding: utf-8 -*-
"""P4-G — resolution of the independent re-verification (Master-first).

  python3 p4g_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

R1  Evidence Passports (34) still named the producer of material without a public locator and printed its value. The
    passport display fields are rewritten; the value and producer are withheld as on the record (CLM-044).
R3  Text-first and retired visuals (tiers TABLE_TEXT_FIRST / RETIRE_FROM_DESIGN) no longer describe a drawing: summaries,
    methods, definitions and scopes describe the text-first form. The Home system summary no longer repeats the
    enumeration its scope line already carries (N3).
R4  /remittances/ no longer refers to a chart.
R5  Governed in-frame text for VIS-PAYMENT-ANATOMY ("is not" line per object) and VIS-REMITTANCE-COST (average-of-quotes
    note), in both languages.
R6  Arabic chart labels: agreement, tense and calques corrected; "current" list label dated; ban stated as of the source date.
R7  Limitations part B: CLM-016/051 state a limit of the measure; CLM-037 Arabic no longer tautological; CLM-036/040 share
    one wording; missing full stops.
R8  «مليار» after decimal numbers, consistently.
R9  MSME in Arabic is «المنشآت الصغرى والصغيرة والمتوسطة» wherever the English says MSME (SMEPS's proper name is kept).
N2  /terms/ section 6 gains its heading. N4 /evidence/ section 1 heading and /data/ title no longer echo each other;
    «فهرس البيانات» for the data catalogue. N5 the REPORTED state label no longer says "official statistics".
Arabic is authored by the Lead in the product's register; it has not been certified by an outside native editor.
"""
import re
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S03, S04, S06, S07, S10, S11, S14, S15, S34 = ("03_PAGE_SECTIONS", "04_NAV_UX", "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS",
                                              "10_MEASUREMENT_AGENDA", "11_VISUAL_LIBRARY", "14_SYSTEM_CHRONOLOGY", "15_SOURCE_LIBRARY",
                                              "34_EVIDENCE_PASSPORTS")

PASSPORT_46 = {
    "object": "Residual-model remittance estimate, 2024 (producer and value withheld: no public locator; reuse rights not assessed)",
    "publisher": "Withheld — no public locator; reuse rights not assessed",
    "method": "Balance-of-payments residual model; the underlying material has no public locator",
    "route": "/evidence/CLM-044/",
    "display_requirements": "Never replace official baselines. Do not show the value or name the producer until the material has a public "
                            "locator and a rights assessment (Master-first).",
}
PASSPORT_49_PUBLISHER = ("CCY/REACH + World Bank/G2Px + RPW", "World Bank/G2Px + RPW + material without a public locator (not named)")

TEXT_FIRST_DEF = ("A text summary of the evidence. Read it with the stated question, scope, unit, period, source and limitations.",
                  "ملخص نصي للدليل، يُقرأ مع السؤال والنطاق والوحدة والفترة والمصدر والحدود المبينة له.")
TEXT_FIRST = ["VIS-INCLUSION-TRANSMISSION", "VIS-EVIDENCE-FRESHNESS", "VIS-EVIDENCE-GAPS", "VIS-SOURCE-COMPARISON", "VIS-FIRM-FINANCE-SEVERITY",
              "VIS-OECD-FCP-TIMELINE", "VIS-MECHANISM-METRIC-BRIDGE", "VIS-ACCESS-EVIDENCE-LAYER", "VIS-CAPITAL-CONTEXT"]
# summary rewrites: (visual, old substring, new substring) applied to 06 summary, 11 accessible_summary and the 03 lead
SUMMARY_SUBS = [
    ("VIS-EVIDENCE-FRESHNESS", "The visual places evidence by its observation or publication vintage across domains and distinguishes",
     "Evidence is ordered here by its observation or publication vintage across domains, distinguishing"),
    ("VIS-EVIDENCE-FRESHNESS", "It shows where this resource relies", "This shows where this resource relies"),
    ("VIS-EVIDENCE-FRESHNESS", "يضع العرض الأدلة بحسب تاريخ القياس أو النشر عبر المجالات، ويميز بين",
     "تُرتَّب الأدلة هنا بحسب تاريخ القياس أو النشر عبر المجالات، مع التمييز بين"),
    ("VIS-EVIDENCE-FRESHNESS", "ويبين أين تعتمد الإجابة", "ويتضح بذلك أين تعتمد الإجابة"),
    ("VIS-EVIDENCE-GAPS", "The visual groups current evidence gaps by type:", "Current evidence gaps are grouped here by type:"),
    ("VIS-EVIDENCE-GAPS", "is never plotted as zero", "is never shown as zero"),
    ("VIS-EVIDENCE-GAPS", "يجمع العرض فجوات الأدلة الحالية بحسب نوعها:", "تُجمع فجوات الأدلة الحالية هنا بحسب نوعها:"),
    ("VIS-OECD-FCP-TIMELINE", "The timeline separates the existence", "The sequence separates the existence"),
    ("VIS-OECD-FCP-TIMELINE", "يفصل الخط الزمني بين وجود", "يفصل هذا التسلسل بين وجود"),
    ("VIS-MECHANISM-METRIC-BRIDGE", "The visual starts from one quantitative", "This summary starts from one quantitative"),
    ("VIS-MECHANISM-METRIC-BRIDGE", "يبدأ العرض من دليل كمي واحد", "يبدأ هذا الملخص من دليل كمي واحد"),
    ("VIS-INCLUSION-TRANSMISSION",
     "Financial inclusion in Yemen is described here as connected parts: people and capability, firms and income, providers, payment "
     "rails, remittance and capital flows, regulation and consumer protection, and enabling constraints.",
     "Financial inclusion in Yemen is described here as a set of connected parts, listed in the scope below."),
    ("VIS-INCLUSION-TRANSMISSION",
     "يصف هذا العرض الشمول المالي في اليمن بوصفه أجزاء مترابطة: الناس وقدراتهم، والمنشآت والدخل، ومقدمو الخدمات، وبنية المدفوعات، "
     "وتدفقات الحوالات ورأس المال، والتنظيم وحماية المستهلك، والقيود المُمكِّنة أو المعطِّلة.",
     "يصف هذا الملخص الشمول المالي في اليمن بوصفه أجزاء مترابطة، يرد بيانها في النطاق أدناه."),
]
METHODS = {
    "VIS-INCLUSION-TRANSMISSION": ("Text summary of the system relationships documented in the evidence base. No arrows or evidence-strength "
                                   "markers are used, because no relationship carries a governed evidence strength.",
                                   "ملخص نصي للعلاقات الموثقة بين أجزاء المنظومة في قاعدة الأدلة؛ ولا تُستخدم أسهم ولا علامات لقوة الدليل، لأن "
                                   "أي علاقة لا تحمل قوة دليل محددة."),
    "VIS-EVIDENCE-FRESHNESS": ("Evidence is listed by vintage and evidence class; no freshness score is computed.",
                               "تُدرج الأدلة بحسب تاريخ القياس أو النشر وفئة الدليل، من دون احتساب درجة رقمية للحداثة."),
    "VIS-EVIDENCE-GAPS": ("Gaps are listed by explicit type; a blank or unknown value is never shown as zero.",
                          "تُدرج الفجوات بفئات صريحة، ولا يُعرض الفراغ أو المجهول على أنه صفر."),
    "VIS-FIRM-FINANCE-SEVERITY": ("Percentages are shown with their calculation base and filter definition beside them.",
                                  "تُعرض النسب مع تعريف المرشح وقاعدة القياس بجوارها حتى لا تتحول 91.84% إلى نسبة لجميع المنشآت."),
    "VIS-OECD-FCP-TIMELINE": ("An ordered sequence separates framework, purpose, output, implementation, complaints and redress, enforcement "
                              "and outcome.",
                              "يفصل تسلسل مرتب بين الإطار والغرض والمخرج والتنفيذ والشكاوى والتظلم والإنفاذ والنتيجة، مع بقاء الحالات غير "
                              "المقاسة مفتوحة."),
    "VIS-MECHANISM-METRIC-BRIDGE": ("Each link is labelled as context, policy proposition, research priority or verification need; no causal "
                                    "arrow is used without independent evidence.",
                                    "تُسمى الروابط صراحةً: سياق، أو مقترح سياسة، أو أولوية بحث، أو حاجة إلى تحقق؛ ولا تُستخدم أسهم سببية من "
                                    "دون دليل مستقل."),
    "VIS-CAPITAL-CONTEXT": ("Pathways are described in text by flow class and evidence state; unlike funding states are never added into one "
                            "total.",
                            "تُوصف المسارات نصيًا بحسب فئة التدفق وحالته، ولا يُنشأ إجمالي جمعي بين حالات تمويل غير متجانسة."),
}

NEW_UI = [
    ("UI-VIS-NOT-PAY-CARDS", "Not people, and not active cardholders", "ليست أشخاصًا، ولا حاملي بطاقات نشطين"),
    ("UI-VIS-NOT-PAY-ACCOUNTS", "Not people, and not active accounts", "ليست أشخاصًا، ولا حسابات نشطة"),
    ("UI-VIS-NOT-PAY-EWALLETS", "Not users: a count of wallet products", "ليست مستخدمين: عدد منتجات المحافظ"),
    ("UI-VIS-NOT-PAY-EWALLET-SUBSCRIBERS", "Not unique people, and not active users", "ليسوا أشخاصًا فريدين، ولا مستخدمين نشطين"),
    ("UI-VIS-NOT-PAY-ATMS", "Infrastructure, not use", "بنية تحتية، لا استخدام"),
    ("UI-VIS-NOT-PAY-POS-TERMINALS", "Infrastructure, not use", "بنية تحتية، لا استخدام"),
    ("UI-VIS-NOT-PAY-POS-TRANSACTIONS", "Events, not people", "أحداث، لا أشخاص"),
    ("UI-VIS-RPW-AVERAGE-NOTE", "Average of quotes for this amount — not the cost of all remittances",
     "متوسط عروض الأسعار لهذا المبلغ — وليس تكلفة جميع الحوالات"),
]
LABEL_EDITS = {   # uid: (new_en or None, new_ar)
    "UI-VIS-STATE-REPORTED": ("Reported by the source", "وارد في المصدر"),
    "UI-VIS-UNIT-YER-MILLION": (None, "مليون ريال يمني (بالقيمة الاسمية)"),
    "UI-VIS-CAT-PRV-COUNT-CURRENT-LIST": ("Count from the official list, as dated in the record", "عدد مأخوذ من القائمة الرسمية بتاريخها المسجل"),
    "UI-VIS-CAT-PRV-NAMED-PARTIAL": (None, "عضوية جزئية في الشبكة، ولا تمثل كامل الجهات الخاضعة للتنظيم"),
    "UI-VIS-CAT-PRV-EVENTS-WALLETS": (None, "قائمة 2024 بالأسماء غير المرخصة وأعداد مؤرخة للمحافظ، ولا يوجد سجل حالي بحالة الترخيص"),
    "UI-VIS-CAT-PRV-LIMIT-EWALLETS": ("Official sources report 7 e-wallets (2024 Q3), 9 e-wallets (2025 H1), 8 licensed e-wallets (2025-09-10) and "
                                      "more than 9 event participants (2026-01-22). The counts stay separate; no named current list of licensed "
                                      "wallets and payment service providers has yet been established.",
                                      "تورد المصادر الرسمية 7 محافظ إلكترونية (الربع الثالث 2024)، و9 محافظ (النصف الأول 2025)، و8 محافظ مرخصة "
                                      "(2025-09-10)، وأكثر من 9 مشاركين في فعالية (2026-01-22). وتبقى هذه الأعداد منفصلة، ولم تُحسم بعد قائمة "
                                      "حالية مسماة بالمحافظ ومقدمي خدمات الدفع المرخصين."),
    "UI-VIS-CAT-PRV-LIMIT-MFI": (None, "العضوية في شبكة YMN لا تثبت الترخيص أو التشغيل، ولا تمثل حصرًا وطنيًا مكتملًا."),
    "UI-VIS-CAT-PRV-STATUS-PROHIBITED": ("Dealing prohibited as of the source date (unlicensed on that date)",
                                         "حُظر التعامل في تاريخ المصدر (غير مرخص في ذلك التاريخ)"),
    "UI-VIS-CAT-PRV-STATUS-NAMED-UNLICENSED": (None, "ورد اسمه بوصفه غير مرخص في تاريخ المصدر"),
}
LIMITS = {
    "CLM-016": {"b_en": "The figure is the sum of category entries on the 2025 roster, which the 2026 roster supersedes; entries are counted "
                        "as listed, not as distinct operating firms.",
                "b_ar": "الرقم مجموع القيود في قائمة 2025 حسب الفئة، وقد حلت محلها قائمة 2026؛ وتُعدّ القيود كما وردت، لا بوصفها شركات "
                        "عاملة مستقلة."},
    "CLM-051": {"b_en": "The source table reports transaction values by type; it does not count users or merchants, and the grouping used here "
                        "is this resource's own, not the source's classification.",
                "b_ar": "يورد جدول المصدر قيم المعاملات حسب نوعها، ولا يعدّ المستخدمين ولا التجار؛ والتجميع المستخدم هنا من إعداد هذا "
                        "المورد، وليس تصنيفًا أصليًا في المصدر."},
    "CLM-037": {"b_en": "After normalisation the two series move almost identically, but the exact CBY↔IMF crosswalk of level, geography "
                        "and statistical concept is not published; a same-year revision remains distinct from change over time.",
                "b_ar": "بعد التطبيع تتحرك السلسلتان بصورة شبه متطابقة، لكن المطابقة الدقيقة بين البنك المركزي وصندوق النقد في المستوى "
                        "والجغرافيا والمفهوم الإحصائي غير منشورة؛ وتظل مراجعة السنة نفسها منفصلة عن التغير عبر الزمن."},
    "CLM-036": {"b_en": "The reconstruction work is documented; a line-by-line crosswalk to the CBY 2025 annual report is not public.",
                "b_ar": "أعمال إعادة البناء موثقة، لكن المطابقة التفصيلية بندًا ببند مع التقرير السنوي للبنك المركزي لعام 2025 غير منشورة."},
    "CLM-040": {"b_en": "The reconstruction work is documented; a line-by-line crosswalk to the CBY 2025 annual report is not public.",
                "b_ar": "أعمال إعادة البناء موثقة، لكن المطابقة التفصيلية بندًا ببند مع التقرير السنوي للبنك المركزي لعام 2025 غير منشورة."},
    "CLM-033": {"b_en": "A method or valuation break materially changes the values for the same reference year; line-level attribution beyond "
                        "the documented valuation note remains bounded."},
    "CLM-038": {"b_en": "Historical precedent does not establish continuity or equivalence with the 2023 regime; the exact circular text and "
                        "its legal and statistical lineage remain open."},
}
SMEPS_NAMES = ("وكالة تنمية المنشآت الصغيرة والأصغر", "برنامج تنمية المنشآت الصغيرة والأصغر", "وحدة تنمية المنشآت الصغيرة والأصغر")
MSME_AR = "المنشآت الصغرى والصغيرة والمتوسطة"


def col_of(h, name):
    if name not in h:
        raise TxError(f"column {name} not found")
    return h.index(name) + 1


def msme_fix(text):
    """Generic MSME -> «المنشآت الصغرى والصغيرة والمتوسطة»; SMEPS's proper name is kept."""
    keep = {}
    for i, n in enumerate(SMEPS_NAMES):
        keep[f"\u0000{i}\u0000"] = n
        text = text.replace(n, f"\u0000{i}\u0000")
    text = re.sub(r"المنشآت الصغيرة والأصغر", MSME_AR, text)
    text = re.sub(r"(?<!الصغرى و)(المنشآت|للمنشآت)(/المشروعات)? الصغيرة والمتوسطة",
                  lambda m: m.group(1) + (m.group(2) or "") + " الصغرى والصغيرة والمتوسطة", text)
    text = text.replace("متناهية الصغر والصغيرة والمتوسطة", "الصغرى والصغيرة والمتوسطة")
    for k, n in keep.items():
        text = text.replace(k, n)
    return text


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)

    # ---- R1 passports -------------------------------------------------------------------------------------------------
    g34 = wb.grid(S34)
    h34 = [str(x) if x is not None else None for x in g34[3]]
    r = next(i for i, x in enumerate(g34, 1) if x and x[0] == "EP-CCY-REMIT-RESIDUAL-MODEL-K04")
    for fld, new in PASSPORT_46.items():
        c = col_of(h34, fld)
        s.set("R1", S34, r, c, new, g34[r - 1][c - 1], f"EP-CCY-REMIT-RESIDUAL-MODEL-K04.{fld}")
    r = next(i for i, x in enumerate(g34, 1) if x and x[0] == "EP-YEM-CASH-FIN-TRANSMISSION-K04")
    s.set("R1", S34, r, col_of(h34, "publisher"), PASSPORT_49_PUBLISHER[1], PASSPORT_49_PUBLISHER[0], "EP-YEM-CASH-FIN-TRANSMISSION-K04.publisher")

    # ---- R3 text-first visuals ------------------------------------------------------------------------------------------
    g06 = wb.grid(S06)
    h06 = [str(x) if x is not None else None for x in g06[3]]
    row06 = {x[0]: i for i, x in enumerate(g06, 1) if i > 4 and x and x[0]}
    g11 = wb.grid(S11)
    h11 = [str(x) if x is not None else None for x in g11[3]]
    row11 = {x[0]: i for i, x in enumerate(g11, 1) if i > 4 and x and x[0]}
    for vid in TEXT_FIRST:
        if vid not in row06:          # a visual without an Evidence Record (e.g. VIS-ACCESS-EVIDENCE-LAYER) has no definition field
            continue
        r = row06[vid]
        for lang, new in zip(("en", "ar"), TEXT_FIRST_DEF):
            c = col_of(h06, f"definition_{lang}")
            s.set("R3", S06, r, c, new, g06[r - 1][c - 1], f"{vid}.definition_{lang}")
    for vid, (en, ar) in METHODS.items():
        r = row06[vid]
        for lang, new in (("en", en), ("ar", ar)):
            c = col_of(h06, f"method_{lang}")
            s.set("R3", S06, r, c, new, g06[r - 1][c - 1], f"{vid}.method_{lang}")
    s.replace("R3", S06, row06["VIS-INCLUSION-TRANSMISSION"], col_of(h06, "universe_ar"), "الأدلة المرتبطة بالشكل", "الأدلة المرتبطة بهذا الملخص",
              "VIS-INCLUSION-TRANSMISSION.universe_ar")
    for vid, old, new in SUMMARY_SUBS:
        lang = "ar" if re.search(r"[؀-ۿ]", old) else "en"
        targets = [(S06, row06[vid], col_of(h06, f"summary_{lang}")), (S11, row11[vid], col_of(h11, f"accessible_summary_{lang}")),
                   (S03, s.section_row(f"/evidence/{vid}/", 1, lang), 5 if lang == "en" else 7)]
        hit = 0
        for sh, rr, cc in targets:
            cur = s.ed.get_value(sh, rr, cc)
            if isinstance(cur, str) and cur.count(old) == 1:
                s.set("R3", sh, rr, cc, cur.replace(old, new), cur, f"{vid}.{sh[:2]}.{lang}")
                hit += 1
        if hit == 0:
            raise TxError(f"R3 {vid}: {old[:50]!r} not found")

    # ---- R4 /remittances/ ------------------------------------------------------------------------------------------------
    s.replace_section("R4", "/remittances/", 2, "en", "body",
                      "The chart breaks the line where the source document changes and never extends reported history through the forecast as if all years had the same status.",
                      "The series is kept apart where the source document changes: reported history is never extended through the forecast as if all years had the same status.")
    s.replace_section("R4", "/remittances/", 2, "ar", "body",
                      "وينقطع الخط في الرسم عند تغير الوثيقة المصدر، ولا تُمد القيم التاريخية عبر التوقعات",
                      "وتُفصل السلسلة عند تغير الوثيقة المصدر، فلا تُمد القيم التاريخية عبر التوقعات")

    # ---- R6 / N5 labels -------------------------------------------------------------------------------------------------------
    g04 = wb.grid(S04)
    row04 = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    for uid, (en, ar) in LABEL_EDITS.items():
        r = row04[uid]
        if en is not None:
            s.set("R6", S04, r, 2, en, g04[r - 1][1], f"{uid}.label_en")
        s.set("R6", S04, r, 3, ar, g04[r - 1][2], f"{uid}.label_ar")

    # ---- R7 limitations ---------------------------------------------------------------------------------------------------------
    for oid, ch in LIMITS.items():
        r = row06[oid]
        for lang in ("en", "ar"):
            c = col_of(h06, f"limitations_{lang}")
            cur = g06[r - 1][c - 1]
            a, b = cur.split(" | ", 1)
            new = f"{a} | {ch.get('b_' + lang, b)}"
            if new != cur:
                s.set("R7", S06, r, c, new, cur, f"{oid}.limitations_{lang}")

    # ---- R8 / R9 Arabic across public sheets --------------------------------------------------------------------------------------
    for sh in (S03, S06, S07, S10, S14, S15):
        g = wb.grid(sh)
        for i, x in enumerate(g, 1):
            if i <= 4 or not x:
                continue
            for j, v in enumerate(x, 1):
                if not isinstance(v, str) or not re.search(r"[؀-ۿ]", v):
                    continue
                cur = s.ed.get_value(sh, i, j)
                new = re.sub(r"(\d+\.\d+) مليارات", r"\1 مليار", cur)
                new = msme_fix(new)
                if new != cur:
                    s.set("R8/R9", sh, i, j, new, cur, f"{x[0]}.c{j}")

    # ---- N2 / N4 page copy ---------------------------------------------------------------------------------------------------------
    s.set_section("N2", "/terms/", 6, "en", "heading", "Rights stay with the source", None)
    s.set_section("N2", "/terms/", 6, "ar", "heading", "تبقى الحقوق لمصدرها", None)
    s.set_section("N4", "/evidence/", 1, "en", "heading", "How to search, inspect and compare the records", "Find the evidence behind the answer")
    s.set_section("N4", "/evidence/", 1, "ar", "heading", "كيف تبحث في السجلات وتفحصها وتقارن بينها", "اعثر على الدليل وراء الإجابة")
    g02 = wb.grid("02_SITE_MAP")
    h02 = [str(x) if x is not None else None for x in g02[3]]
    r2 = next(i for i, x in enumerate(g02, 1) if x and x[0] == "/data/")
    s.set("N4", "02_SITE_MAP", r2, col_of(h02, "title_en"), "Find the original source behind each piece of evidence",
          "Find the evidence behind the answers — without losing its meaning.", "/data/.title_en")
    s.set("N4", "02_SITE_MAP", r2, col_of(h02, "title_ar"), "اعثر على المصدر الأصلي وراء كل دليل",
          "اعثر على الدليل وراء الإجابة من دون أن تفقد معناه.", "/data/.title_ar")
    s.replace_section("N4", "/data/", 2, "ar", "heading", "ماذا يتضمن دليل البيانات؟", "ماذا يتضمن فهرس البيانات؟")
    s.replace_section("N4", "/data/", 7, "ar", "body", "من أي نتيجة في دليل البيانات،", "من أي نتيجة في فهرس البيانات،")

    # ---- R5 new interface copy (last: row insertion) ---------------------------------------------------------------------------------
    g04b = s.grid(S04)
    ids = {x[0]: i for i, x in enumerate(g04b, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    last = max(i for u, i in ids.items() if i < 260)
    if any(c not in (None, "") for c in g04b[last]) or g04b[last + 1][0] != "Trust navigation":
        raise TxError("04: interface-copy block end not where expected")
    rows = [{1: a, 2: b, 3: c, 4: f"Pre-Tranche-C P4 (re-verification R5). In-frame chart text."} for a, b, c in NEW_UI]
    if any(a in ids for a, *_ in NEW_UI):
        raise TxError("04: a new UI id exists")
    s.ed.insert_rows(S04, last + 1, rows)
    for a, b, c in NEW_UI:
        s.ledger.append(OrderedDict([("finding", "R5"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    changed = s.regenerate_full_copy()
    rep = s.save(out, ledger, [("transaction", "P4-G"), ("scope", "Re-verification resolution: passports firewall, text-first visuals, in-frame text, "
                                "Arabic labels and terms, limitations part B, page copy"), ("full_copy_regenerated", changed)])
    print(f"P4-G staged: {rep['cells_written']} changes ({len(changed)} full copies); Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
