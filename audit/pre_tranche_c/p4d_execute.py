# -*- coding: utf-8 -*-
"""P4-D — resolution of the independent verification of P2-P4 (Master-first): publication firewall, limitations,
Arabic grammar labels, Reading index.

  python3 p4d_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

V-D1  CLM-044 named a source with no public locator and unassessed rights (CCY) and printed its value on the record and
      on the Reading "Same year, different number". Lead decision: withhold the producer and the value on every public
      surface until a public locator and a rights assessment exist; keep the record as a method record that explains
      why a residual-model estimate is not the canonical baseline. A governed status line covers a Reading whose records
      also rest on unlisted material.
V-D4  Limitations part B: dangling Arabic connectives removed; B written as a limit of the measure where it restated A;
      Arabic/English meaning aligned (CLM-018/029/030/037/051).
V-D7  VIS-INCLUSION-TRANSMISSION and VIS-CAPITAL-CONTEXT no longer describe a drawing ("The map links", "The visual
      separates") that the product does not draw.
V-D8  CLM-007: definition, period and currentness say "reported history", never "observed"; currentness no longer treats
      a projection as the currentness bound.
V-D9  Arabic grammar labels (chain access/outcome, missing, nominal, not comparable, estimate/projection, reported),
      the "does not establish" label, RV-CWR-002/008 universe wording.
V-D10/D12/D14  Home heading repeated its eyebrow; /evidence/ lead repeated; /payments/ "the charts" and the July high;
      /data/ promised filters and downloads that do not exist; Arabic "تشير... بأن", "جغرافيا تمثل", two English-only
      Arabic card titles; RV-CWR-001 universe repeated its period.
V-D16 09_READING_SECTIONS becomes a pure index: its copy (all orders) and titles (orders 2-9) are emptied; the generator
      takes them from 08/03 and stops if text is written into 09.
Arabic is authored by the Lead in the product's existing register; it has not been certified by an outside native editor.
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S03, S04, S06, S07, S08, S09, S11, S15 = ("03_PAGE_SECTIONS", "04_NAV_UX", "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS", "08_READINGS",
                                          "09_READING_SECTIONS", "11_VISUAL_LIBRARY", "15_SOURCE_LIBRARY")

# ---------------------------------------------------------------- V-D1 CLM-044
CLM044 = {
    "summary_en": "A balance-of-payments residual model estimates remittances by assigning an assumed residual discrepancy to them. "
                  "Such an estimate is an alternative model, not a direct observation or the canonical remittance baseline. The estimate "
                  "considered here rests on material that has no public original locator and whose reuse rights have not been assessed, "
                  "so neither its value nor its producer is reproduced on this site.",
    "summary_ar": "يقدّر نموذج قائم على متبقي ميزان المدفوعات التحويلات بإسناد فرق متبقٍّ مفترض إليها. ومثل هذا التقدير نموذج بديل، "
                  "لا مشاهدة مباشرة ولا خط أساس مرجعي للتحويلات. ويستند التقدير المعني هنا إلى مادة لا يتوافر لها رابط أصلي عام ولم "
                  "تُقيَّم حقوق إعادة استخدامها بعد، لذلك لا يعرض هذا الموقع قيمته ولا الجهة التي أعدّته.",
    "method_en": "Balance-of-payments residual model. The underlying material has no public original locator, so this record cannot be "
                 "verified from this site.",
    "method_ar": "نموذج متبقي ميزان المدفوعات. ولا يتوافر للمادة الأصلية رابط عام، لذلك لا يمكن التحقق من هذا السجل عبر هذا الموقع.",
    "limitations_en": "Do not present any residual-model estimate as an official or observed national value, or treat the residual as "
                      "directly observed informal remittances. | Errors in other balance-of-payments components, and the assumption made "
                      "about errors and omissions, flow into the remittance residual; informal remittances are not directly observed.",
    "limitations_ar": "لا يجوز تقديم أي تقدير ناتج عن نموذج المتبقي بوصفه قيمة وطنية رسمية أو مرصودة، ولا معاملة المتبقي على أنه "
                      "تحويلات غير رسمية مرصودة مباشرة. | تنتقل أخطاء مكونات ميزان المدفوعات الأخرى، والافتراض المعتمد لبند الأخطاء "
                      "والسهو، إلى متبقي التحويلات؛ والتحويلات غير الرسمية ليست مرصودة مباشرة.",
    "verification_en": None,    # set to the governed template UI-VERIFY-UNLISTED below
    "verification_ar": None,
}
CLM044_LEAD = (
    "A residual model derives remittances from what is left in the balance of payments once its other components are counted. "
    "This record explains why such an estimate is kept separate from the canonical remittance baseline, and why the value of the "
    "estimate considered here is not shown.",
    "يستخلص نموذج المتبقي التحويلات مما يتبقى في ميزان المدفوعات بعد احتساب مكوناته الأخرى. ويوضح هذا السجل سبب إبقاء مثل هذا "
    "التقدير منفصلًا عن خط الأساس المرجعي للتحويلات، وسبب عدم عرض قيمة التقدير المعني هنا.")
READING_CCY = (
    ("and the model estimate of at least US$7.4 billion by CCY (Cash Consortium of Yemen) is not a baseline.",
     "and a residual-model estimate is not a baseline."),
    ("ولا يُعتمد تقدير نموذج ائتلاف النقد في اليمن (CCY) البالغ 7.4 مليار دولار على الأقل خطَّ أساس.",
     "ولا يُعتمد تقدير ناتج عن نموذج المتبقي خطَّ أساس."))

VERIFY_UNLISTED = (
    "The material behind this record has no public original locator, so no source is listed or linked here and no figure from that "
    "material is shown. Read the record as an explanation of method, not as a verifiable figure.",
    "لا يتوافر للمادة التي يستند إليها هذا السجل رابط أصلي عام، لذلك لا يُدرج هنا أي مصدر ولا يُربط به، ولا يُعرض أي رقم مأخوذ من "
    "تلك المادة. فاقرأ السجل بوصفه شرحًا للمنهج، لا رقمًا قابلًا للتحقق.")
CLM044["verification_en"], CLM044["verification_ar"] = VERIFY_UNLISTED

NEW_UI = [
    ("UI-VERIFY-UNLISTED", VERIFY_UNLISTED[0], VERIFY_UNLISTED[1],
     "Pre-Tranche-C P4 (V-D1). Verification template of a record whose every bound source lacks a public locator "
     "(closure template BOUND_UNLISTED); such a record prints no figure from that material."),
    ("UI-READING-PATH-COMPLETE-UNLISTED",
     "Every figure in this Reading traces through the records below to a named source. Where a record also rests on material "
     "with no public original locator, that material is not listed and no figure from it is shown.",
     "يمكن تتبّع كل رقم في هذه القراءة، عبر السجلات أدناه، إلى مصدر مسمّى. وحيث يستند سجل أيضًا إلى مادة لا يتوافر لها رابط أصلي "
     "عام، فلا تُدرج تلك المادة ولا يُعرض هنا أي رقم مأخوذ منها.",
     "Pre-Tranche-C P4 (V-D1). Reading path status when the Reading is closed to named sources and a bound record also rests on "
     "material without a public locator (publication firewall)."),
]

# ---------------------------------------------------------------- V-D4 limitations (A | B), full new values where changed
FINDEX_B_AR = "يستبعد إطار المسح مناطق يقطنها نحو 23% من السكان، كما استُبدل أكثر من ربع (1/4) وحدات المعاينة الأولية."
LIMITS = {
    # oid: {"b_en": ..., "b_ar": ..., "a_en": ...}
    "CLM-001": {"b_ar": FINDEX_B_AR},
    "CLM-002": {"b_ar": FINDEX_B_AR},
    "CLM-025": {"b_ar": FINDEX_B_AR},
    "CLM-007": {"b_ar": "هذا مفهوم اقتصادي كلي للقطاع الخارجي، وليس قياسًا لتسوية المدفوعات عبر نظام الدفع ولا قياسًا مباشرًا لحجم "
                        "الحوالة غير الرسمية."},
    "CLM-008": {"a_en": "Do not infer active branches, products, market share or payment-rail participation.",
                "b_en": "Appearing on the list establishes listing or licensing in that source only; it does not establish operation, all "
                        "branches, participation, or national coverage beyond the scope of the issuing authority."},
    "CLM-012": {"b_ar": "القواعد والسقوف لا تحدد المجموعة الحالية لمقدمي الخدمات المشمولين بالأدلة، ولا توافر المنتجات، ولا الأرصدة أو "
                        "المعاملات الفعلية، ولا الامتثال، ولا عدد المستخدمين الفريدين."},
    "CLM-015": {"b_en": "The source is a warning list of names declared unlicensed on its publication date; it records a regulatory "
                        "declaration, not an observation of whether those services operated then or later.",
                "b_ar": "المصدر قائمة تحذيرية بأسماء أُعلن عدم ترخيصها في تاريخ نشرها؛ فهي تسجل إعلانًا رقابيًا، لا رصدًا لما إذا كانت "
                        "تلك الخدمات تعمل آنذاك أو بعده."},
    "CLM-018": {"b_en": "The evidence records institutional and implementation states only; it contains no measure of participation, "
                        "reliability, adoption or transaction coverage for these systems.",
                "b_ar": "يسجل الدليل حالات مؤسسية وتنفيذية فقط، ولا يتضمن أي قياس للمشاركة أو الموثوقية أو التبني أو تغطية المعاملات في "
                        "هذه الأنظمة."},
    "CLM-020": {"b_en": "The two dates describe different layers of institutional and programme development; the sources do not date the "
                        "same event.",
                "b_ar": "يصف التاريخان طبقتين مختلفتين من التطور المؤسسي والبرامجي، ولا يؤرخ المصدران الحدث نفسه."},
    "CLM-027": {"b_ar": "تختلف صياغة مقياس 2011 عن مفهوم الحساب المعتمد لاحقًا، وقيم 2014 مقرّبة، وتظل قيود العمل الميداني "
                        "(2022–2023) والاستبعاد الجغرافي جوهرية."},
    "CLM-029": {"b_en": "Historical, not current. '..' means no observation, and saving and borrowing indicators can overlap."},
    "CLM-030": {"b_en": "Historical, not current. '..' means no observation, and remittance-channel values are shares of a conditional "
                        "sub-population, not of all adults.",
                "b_ar": "هذه أدلة تاريخية؛ والرمز «..» يعني عدم وجود ملاحظة، وقيم قنوات التحويل نسب من مجتمع فرعي مشروط لا من جميع "
                        "البالغين."},
    "CLM-037": {"b_en": "After normalisation the two series follow closely matching paths, but the exact CBY↔IMF crosswalk of level, "
                        "geography and statistical concept is not published; a same-year revision remains distinct from change over time.",
                "b_ar": "بعد التطبيع يتبع المساران مسارين متطابقين تقريبًا، لكن المطابقة الدقيقة بين البنك المركزي وصندوق النقد في المستوى "
                        "والجغرافيا والمفهوم الإحصائي غير منشورة؛ وتظل مراجعة السنة نفسها منفصلة عن التغير عبر الزمن."},
    "CLM-051": {"b_ar": "قيمة المعاملات لا تقيس المستخدمين الفريدين أو تبني التجار أو الرفاه أو الشمول المستدام؛ والتجميع من إعداد "
                        "هذا المورد، وليس تصنيفًا أصليًا في المصدر."},
    "CLM-053": {"b_en": "The primary 2023 source and the bridge between provider coverage across periods are not yet available for direct "
                        "verification."},
    "CLM-055": {"b_en": "Appearing on the list establishes listing or licensing in that source only; it does not establish operation, "
                        "branches, participation in payment systems, products or market share.",
                "b_ar": "الظهور في القائمة يثبت الإدراج أو الترخيص في المصدر فقط، ولا يثبت التشغيل أو الفروع أو المشاركة في أنظمة الدفع "
                        "أو المنتجات أو الحصة السوقية."},
    "CLM-059": {"b_en": "Programme figures count the programme's own participants and disbursements; they are not drawn from a national "
                        "sample of firms.",
                "b_ar": "تعدّ أرقام البرنامج المشاركين فيه وما صرفه هو، ولا تستند إلى عينة وطنية من المنشآت."},
    "CLM-060": {"b_ar": "لا يوضح جدول المؤشرات الموجز بصورة كاملة قاعدة الاحتساب أو التقييم الخاصة بالمؤشر، ولا التعريف التشغيلي "
                        "لعبارة «الوصول إلى الخدمات المالية»؛ وهذا يضيّق نطاق الخلاصة ولا يلغي المؤشر الذي أورده المصدر."},
}

# ---------------------------------------------------------------- V-D7
TRANSMISSION = (
    "Financial inclusion in Yemen is described here as connected parts: people and capability, firms and income, providers, payment "
    "rails, remittance and capital flows, regulation and consumer protection, and enabling constraints. The documented relationships "
    "describe context, dependency or plausible mechanisms where evidence supports them; they do not form a composite score and do not "
    "claim that one part causes another.",
    "يصف هذا العرض الشمول المالي في اليمن بوصفه أجزاء مترابطة: الناس وقدراتهم، والمنشآت والدخل، ومقدمو الخدمات، وبنية المدفوعات، "
    "وتدفقات الحوالات ورأس المال، والتنظيم وحماية المستهلك، والقيود المُمكِّنة أو المعطِّلة. وتصف العلاقات الموثقة السياق أو الاعتماد "
    "أو آليات محتملة حين تسندها الأدلة؛ ولا تتحول الأجزاء إلى درجة واحدة، ولا تثبت أن جزءًا منها سبب لآخر.")
CAPITAL = (
    "Humanitarian finance, development finance, project financing and financial-institution finance are different pathways with "
    "different purposes, recipients and evidence states. They give context for how resources may enter the wider system; they are not "
    "added into one financial-inclusion total, and programme finance is not an observed inclusion outcome.",
    "التمويل الإنساني والتمويل التنموي وتمويل المشروعات وتمويل المؤسسات المالية مسارات مختلفة في الغرض والمستفيدين وحالة الدليل. "
    "وهي تقدم سياقًا لكيفية دخول الموارد إلى النظام الأوسع، لكنها لا تُجمع في إجمالي واحد للشمول المالي، ولا يُعامل تمويل البرامج "
    "بوصفه نتيجة مرصودة للشمول.")

# ---------------------------------------------------------------- V-D8 CLM-007
CLM007 = {
    "definition_en": "A series that explicitly separates reported history, estimates and projections.",
    "definition_ar": "سلسلة تفصل بوضوح بين القيم التاريخية الواردة في المصدر والتقديرات والتوقعات.",
    "period_ar": "قيم تاريخية للفترة 2018–2024 (حسابات الخبراء)؛ تقدير 2025؛ توقعات 2026–2030",
    "currentness_en": "The latest reported value is for 2024 (staff calculations). The 2025 value is an estimate and the 2026–2030 values "
                      "are projections; none of them is a later observation. Do not carry the 2024 value forward as a current level "
                      "without a newer comparable observation.",
    "currentness_ar": "آخر قيمة تاريخية واردة في المصدر هي لعام 2024 (حسابات الخبراء). أما قيمة 2025 فتقدير، وقيم 2026–2030 توقعات، "
                      "وليست أي منها مشاهدة لاحقة. ولا يجوز ترحيل قيمة 2024 بوصفها مستوى حاليًا من دون مشاهدة أحدث قابلة للمقارنة.",
}

# ---------------------------------------------------------------- V-D9 04 labels (Arabic unless stated)
LABELS_AR = {
    "UI-VIS-STATE-ESTIMATED": "تقدير — ليس قيمة مرصودة",
    "UI-VIS-STATE-PROJECTED": "توقع — ليس قيمة مرصودة",
    "UI-VIS-MISSING": "لا قيمة موثَّقة لهذه الفترة — ليست صفرًا",
    "UI-VIS-NOT-COMPARABLE": "لا تصح المقارنة المباشرة",
    "UI-VIS-NOMINAL": "اسمية — لم تُعدَّل وفق الأسعار أو سعر الصرف",
    "UI-VIS-CHAIN-ACCESS": "الوصول إلى الخدمات المالية",
    "UI-VIS-CHAIN-OUTCOME": "النتيجة للأفراد أو المنشآت",
    "UI-VIS-STATE-REPORTED": "وارد في المصدر (إحصاءات رسمية)",
    "UI-EVID-DOES-NOT-ESTABLISH": "ما الذي لا يثبته هذا الدليل",
}


def col_of(header, name):
    try:
        return header.index(name) + 1
    except ValueError:
        raise TxError(f"column {name} not found")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)

    # ---- V-D1 ----------------------------------------------------------------------------------------------
    g06 = wb.grid(S06)
    h06 = [str(x) if x is not None else None for x in g06[3]]
    row06 = {r[0]: i for i, r in enumerate(g06, 1) if i > 4 and r and r[0]}
    r = row06["CLM-044"]
    for field, new in CLM044.items():
        c = col_of(h06, field)
        s.set("V-D1", S06, r, c, new, g06[r - 1][c - 1], f"CLM-044.{field}")
    for lang, new in zip(("en", "ar"), CLM044_LEAD):
        row = s.section_row("/evidence/CLM-044/", 1, lang)
        cur = s.ed.get_value(S03, row, 5 if lang == "en" else 7)
        if "7.4" not in cur:
            raise TxError("CLM-044 lead no longer carries the value")
        s.set("V-D1", S03, row, 5 if lang == "en" else 7, new, cur, f"/evidence/CLM-044/#s1.body_{lang}")
    (old_en, new_en), (old_ar, new_ar) = READING_CCY
    s.replace_section("V-D1", "/readings/same-year-different-number/", 5, "en", "body", old_en, new_en)
    s.replace_section("V-D1", "/readings/same-year-different-number/", 5, "ar", "body", old_ar, new_ar)
    g08 = wb.grid(S08)
    h08 = [str(x) if x is not None else None for x in g08[3]]
    r8 = next(i for i, x in enumerate(g08, 1) if x and x[0] == "CWR-001")
    s.replace("V-D1", S08, r8, col_of(h08, "prohibited_inference_en"), old_en, new_en, "CWR-001.prohibited_inference_en")
    s.replace("V-D1", S08, r8, col_of(h08, "prohibited_inference_ar"), old_ar, new_ar, "CWR-001.prohibited_inference_ar")

    # ---- V-D4 limitations --------------------------------------------------------------------------------------
    ce, ca = col_of(h06, "limitations_en"), col_of(h06, "limitations_ar")
    for oid, ch in LIMITS.items():
        r = row06[oid]
        for lang, col in (("en", ce), ("ar", ca)):
            cur = g06[r - 1][col - 1]
            if " | " not in cur:
                raise TxError(f"{oid}: limitations_{lang} has no A | B structure")
            a, b = cur.split(" | ", 1)
            a2, b2 = ch.get(f"a_{lang}", a), ch.get(f"b_{lang}", b)
            if (a2, b2) != (a, b):
                s.set("V-D4", S06, r, col, f"{a2} | {b2}", cur, f"{oid}.limitations_{lang}")
    # 07 does_not_prove_ar (claim cards) and 07 copy: the same Arabic wording defects
    g07 = wb.grid(S07)
    h07 = [str(x) if x is not None else None for x in g07[3]]
    for i, x in enumerate(g07, 1):
        if i <= 4 or not x or not x[0]:
            continue
        for fld in ("does_not_prove_ar", "copy_ar"):
            c = col_of(h07, fld)
            v = x[c - 1]
            if isinstance(v, str):
                new = v.replace("جغرافيا تمثل نحو 23% من السكان", "مناطق يقطنها نحو 23% من السكان")
                new = new.replace("من المؤشر العالمي للشمول المالي بأن نسبة", "من المؤشر العالمي للشمول المالي إلى أن نسبة")
                if new != v:
                    s.set("V-D14", S07, i, c, new, v, f"{x[0]}.{fld}")

    # ---- V-D7 ----------------------------------------------------------------------------------------------------
    g11 = wb.grid(S11)
    h11 = [str(x) if x is not None else None for x in g11[3]]
    row11 = {x[0]: i for i, x in enumerate(g11, 1) if i > 4 and x and x[0]}
    for vid, (en, ar) in (("VIS-INCLUSION-TRANSMISSION", TRANSMISSION), ("VIS-CAPITAL-CONTEXT", CAPITAL)):
        r11 = row11[vid]
        for fld, new in (("accessible_summary_en", en), ("accessible_summary_ar", ar)):
            c = col_of(h11, fld)
            s.set("V-D7", S11, r11, c, new, g11[r11 - 1][c - 1], f"{vid}.{fld}")
        r = row06[vid]
        for fld, new in (("summary_en", en), ("summary_ar", ar)):
            c = col_of(h06, fld)
            s.set("V-D7", S06, r, c, new, g06[r - 1][c - 1], f"{vid}.{fld}")
        for lang, new in (("en", en), ("ar", ar)):
            row = s.section_row(f"/evidence/{vid}/", 1, lang)
            col = 5 if lang == "en" else 7
            cur = s.ed.get_value(S03, row, col)
            if not (cur.startswith("The map links") or cur.startswith("The visual separates") or cur.startswith("يربط المخطط")
                    or cur.startswith("يفصل العرض")):
                raise TxError(f"{vid} s1 {lang}: unexpected lead")
            s.set("V-D7", S03, row, col, new, cur, f"/evidence/{vid}/#s1.body_{lang}")

    # ---- V-D8 CLM-007 ------------------------------------------------------------------------------------------------
    r = row06["CLM-007"]
    for fld, new in CLM007.items():
        c = col_of(h06, fld)
        s.set("V-D8", S06, r, c, new, g06[r - 1][c - 1], f"CLM-007.{fld}")
    r = row06["VIS-REMITTANCE-MACRO"]
    s.replace("V-D8", S06, r, col_of(h06, "currentness_ar"), "يمتد التاريخ المبلغ عنه حتى 2024", "تمتد القيم التاريخية الواردة في المصدر حتى 2024",
              "VIS-REMITTANCE-MACRO.currentness_ar")
    s.replace_section("V-D8", "/remittances/", 2, "ar", "body", "بوصفها تاريخًا مبلغًا عنه يستند", "بوصفها قيمًا تاريخية تستند")
    s.replace_section("V-D8", "/remittances/", 2, "ar", "body", "ولا يُمد التاريخ المبلغ عنه عبر التوقعات", "ولا تُمد القيم التاريخية عبر التوقعات")

    # ---- V-D9 labels ---------------------------------------------------------------------------------------------------
    g04 = wb.grid(S04)
    row04 = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    for uid, new in LABELS_AR.items():
        r4 = row04[uid]
        s.set("V-D9", S04, r4, 3, new, g04[r4 - 1][2], f"{uid}.label_ar")
    r11 = row11["RV-CWR-002"]
    s.replace("V-D9", S11, r11, col_of(h11, "universe_ar"), "لفترة الإسناد نفسها", "للفترة المرجعية نفسها", "RV-CWR-002.universe_ar")
    r11 = row11["RV-CWR-008"]
    s.replace("V-D9", S11, r11, col_of(h11, "universe_ar"), "ومجتمع المنشآت الصغيرة والمتوسطة المدعومة", "ومجتمع المنشآت الصغرى والصغيرة والمتوسطة المدعومة",
              "RV-CWR-008.universe_ar")
    s.replace_section("V-D9", "/firms/", 6, "ar", "body", "معدلًا وطنيًا للمنشآت الصغيرة والمتوسطة", "معدلًا وطنيًا للمنشآت الصغرى والصغيرة والمتوسطة")
    r11 = row11["RV-CWR-001"]
    s.set("V-D12", S11, r11, col_of(h11, "denominator_universe"), "2024 reference year across named publication vintages",
          g11[r11 - 1][col_of(h11, "denominator_universe") - 1], "RV-CWR-001.denominator_universe")
    s.set("V-D12", S11, r11, col_of(h11, "universe_ar"), "السنة المرجعية 2024 عبر نسختي نشر مسماتين",
          g11[r11 - 1][col_of(h11, "universe_ar") - 1], "RV-CWR-001.universe_ar")

    # ---- V-D10 / V-D12 / V-D14 page copy ----------------------------------------------------------------------------------
    s.set_section("V-D10", "/", 7, "en", "heading", "The gaps the evidence cannot yet close", "What we still do not know")
    s.set_section("V-D10", "/", 7, "ar", "heading", "فجوات لا تستطيع الأدلة سدّها بعد", "ما الذي ما زلنا لا نعرفه؟")
    # /evidence/: the hero no longer repeats a headed first section (scripts/build.py hero); no copy change is needed
    s.replace_section("V-D12", "/payments/", 2, "en", "body",
                      "transaction counts 8,015→24,026 and nominal transaction value YER 320 million→YER 1.262 billion. The charts keep these three objects separate.",
                      "transaction counts 8,015→24,026 (after a high of 27,187 in July 2025) and nominal transaction value YER 320 million→YER 1.262 billion. This page keeps these three objects separate.")
    s.replace_section("V-D12", "/payments/", 2, "ar", "body",
                      "وعدد المعاملات من 8,015 إلى 24,026، والقيمة الاسمية من 320 مليون ريال إلى 1.262 مليار ريال. وتبقي الرسوم هذه المقاييس منفصلة:",
                      "وعدد المعاملات من 8,015 إلى 24,026 (بعد ذروة بلغت 27,187 معاملة في يوليو 2025)، والقيمة الاسمية من 320 مليون ريال إلى 1.262 مليار ريال. وتُبقي هذه الصفحة المقاييس الثلاثة منفصلة:")
    s.rewrite_section("V-D12", "/data/", 1, "en", "body",
                      "Find an original source by its title or reference, browse the curated reports and method references, or open the full "
                      "register of sources. Each source record keeps its publisher, date and public locator, and its reuse terms where they "
                      "have been assessed; the figures themselves are held in the evidence records that cite the source.",
                      "Search by topic, question, source, period, geography, evidence type or reference ID.")
    s.rewrite_section("V-D12", "/data/", 1, "ar", "body",
                      "ابحث عن مصدر أصلي بعنوانه أو بمرجعه، أو تصفح التقارير والمراجع المنهجية المختارة، أو افتح السجل الكامل للمصادر. ويحتفظ "
                      "كل سجل مصدر بالجهة الناشرة وتاريخ النشر ورابطه العام، وبشروط إعادة الاستخدام حيثما قُيّمت؛ أما الأرقام نفسها فتحملها "
                      "سجلات الأدلة التي تستشهد بالمصدر.",
                      "ابحث حسب الموضوع أو السؤال أو المصدر أو الفترة")
    s.set_section("V-D12", "/data/", 3, "en", "heading", "A value copied from here still needs its context", "A downloadable value still needs its context")
    s.set_section("V-D12", "/data/", 3, "ar", "heading", "القيمة المنقولة من هنا ما تزال تحتاج إلى سياقها", "القيمة القابلة للتنزيل ما تزال تحتاج إلى سياقها")
    s.replace_section("V-D12", "/data/", 3, "en", "body",
                      "Downloads therefore carry the metadata needed to preserve what the value actually means.",
                      "When you copy or cite a figure, take its evidence record reference with it so that its meaning travels with the value.")
    s.rewrite_section("V-D12", "/data/", 3, "ar", "body",
                      "قد يكتسب الرقم معنى مختلفًا إذا أُعيد استخدامه من دون وحدته، أو المجتمع أو قاعدة القياس، أو الفترة، أو الجغرافيا، أو "
                      "المصدر. لذلك انقل مع أي رقم تنسخه أو تستشهد به مرجع سجل الدليل الخاص به، كي يبقى معناه مرتبطًا بقيمته.",
                      "قد يكتسب الرقم معنى مختلفًا إذا أُعيد استخدامه")
    for route, order in (("/evidence/CLM-001/", 1), ("/readings/reforms-newer-than-people-evidence/", 2)):
        s.replace_section("V-D14", route, order, "ar", "body", "من المؤشر العالمي للشمول المالي بأن نسبة", "من المؤشر العالمي للشمول المالي إلى أن نسبة")
    g15 = wb.grid(S15)
    h15 = [str(x) if x is not None else None for x in g15[3]]
    ct = col_of(h15, "display_title_ar")
    for sid, ar in (("SRC-CGAP-ARAB-MEAS-2017-001", "قياس الشمول المالي في العالم العربي"),
                    ("SRC-OECD-YOUTH-DFI-2020-001", "تعزيز الشمول المالي الرقمي للشباب")):
        r15 = next(i for i, x in enumerate(g15, 1) if x and x[0] == sid)
        s.set("V-D14", S15, r15, ct, ar, g15[r15 - 1][ct - 1], f"{sid}.display_title_ar")

    # ---- V-D16 09 index ------------------------------------------------------------------------------------------------------
    g09 = wb.grid(S09)
    h09 = [str(x) if x is not None else None for x in g09[3]]
    cols = {k: col_of(h09, k) for k in ("section_order", "title_en", "title_ar", "copy_en", "copy_ar")}
    n = 0
    for i, x in enumerate(g09, 1):
        if i <= 4 or not x or not x[0]:
            continue
        order = int(float(x[cols["section_order"] - 1]))
        for k in ("copy_en", "copy_ar") + (("title_en", "title_ar") if order > 1 else ()):
            if x[cols[k] - 1] not in (None, ""):
                s.set("V-D16", S09, i, cols[k], None, x[cols[k] - 1], f"{x[0]}.s{order}.{k}")
                n += 1
    s.set("V-D16", S09, 1, 1, "Reading sections — section index", g09[0][0], "09.title")
    s.set("V-D16", S09, 2, 1,
          "Section index of the Readings (reading_id, section_order, section_id; the section-1 title labels the thesis). Copy is owned by "
          "08_READINGS (section 1 = thesis) and 03_PAGE_SECTIONS (sections 2-9, heading and body); the copy and title cells here stay "
          "empty and the generator stops if text is written into them. Edit the owners, not this sheet.",
          g09[1][0], "09.description")

    # ---- 04 new interface copy (last: row insertion) --------------------------------------------------------------------------
    last = row04["UI-EVID-MEASUREMENT-LIMITS"]
    if any(c not in (None, "") for c in g04[last]):
        raise TxError("04: interface-copy block does not end after UI-EVID-MEASUREMENT-LIMITS")
    if any(a in row04 for a, *_ in NEW_UI):
        raise TxError("04: new UI id exists")
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in NEW_UI])
    for a, b, c, _ in NEW_UI:
        s.ledger.append(OrderedDict([("finding", "V-D1"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    changed = s.regenerate_full_copy()
    rep = s.save(out, ledger, [("transaction", "P4-D"), ("scope", "Independent-verification resolution: publication firewall (CLM-044), limitations parts, "
                                "Arabic grammar labels, CLM-007, visual summaries, page copy, 09 Reading index"),
                               ("full_copy_regenerated", changed), ("reading_index_cells_cleared", n)])
    print(f"P4-D staged: {rep['cells_written']} changes ({n} 09 cells cleared; {len(changed)} full copies); Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
