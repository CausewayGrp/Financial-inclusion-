# -*- coding: utf-8 -*-
"""Public naming and terminology, transaction NB-1. Labels and governed term substitutions only; English and Arabic together.

  python3 nb_1_naming.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner brief "Rights closure + public naming and terminology", Part B (10 October 2026); the owner designated this
session programme steward for the naming change (audit/OWNER_DECISIONS_2026-10-10.md). The labels were judged by an
independent Arabic editor, an independent English editor, an information-architecture lead and a five-persona red team;
the lead's decision for every label, with its reason, is in audit/naming/NAMING_DECISIONS_2026-10-10.md.

No route, URL, identifier, figure, unit, period, universe or source changes. What changes:
  B3/B5  the global navigation, the trust layer, the route dictionary, interface labels, the domain names and the
         stable page titles of /readings/ and the domain h1 prefixes (parity in both languages);
  B3.9   the governed glossary: remittances = الحوالات where the meaning is identical (six-condition test, 102 cells,
         audit/naming/nb_1_remittance_substitutions.json); regulatory licensing = الترخيص where «الرخصة» meant it;
         web accessibility = إمكانية الوصول where «إتاحة الوصول» meant accessibility (not where it means access to
         services, 03 /explore/ s6);
  B4     the footer licence line and the licence deed address, and the exact scope of /rights/ section 6;
  B5     old labels kept as search aliases; a governed terminology register (04 titled block "Terminology register").
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, insert_ui_rows, set_ui, ui_block_end  # noqa: E402

F = "NB-1:NAMING"
FG = "NB-1:GLOSSARY"
FR = "NB-1:RIGHTS"
S04, S03, S02 = "04_NAV_UX", "03_PAGE_SECTIONS", "02_SITE_MAP"
COLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def col(letter):
    n = 0
    for ch in letter:
        n = n * 26 + COLS.index(ch) + 1
    return n


# ---------------------------------------------------------------------------------------------------- interface labels
# ui_id -> (old_en, new_en or None, old_ar, new_ar or None)
UI = OrderedDict([
    ("UI-HEADER-REPORT-AN-ISSUE", ("Report an issue", "Report an error", "أبلغ عن مشكلة", "أبلغ عن خطأ")),
    ("UI-EVID-REPORT-AN-ISSUE", ("Report an issue", "Report an error", "أبلغ عن مشكلة", "أبلغ عن خطأ")),
    ("UI-JS-COPY-LONG-CITATION", ("Copy long form", "Copy long citation", None, None)),
    ("UI-READING-RETURN", (None, None, "عد إلى السؤال", "ارجع إلى السؤال")),
    ("UI-EVID-RETURN-TO-INTERPRETATION", (None, None, "عد إلى التفسير", "ارجع إلى التفسير")),
    ("UI-COLOPHON-CITATION", (None, None, "الاستشهاد بهذه الصفحة", "استشهد بهذه الصفحة")),
    ("UI-READING-EYEBROW", ("Evidence Reading", "Reading", "قراءة أدلة", "قراءة تحليلية")),
    ("UI-READING-FEATURED", ("Featured Reading", "Featured reading", "قراءة مختارة", "قراءة تحليلية مختارة")),
    ("UI-READING-ALL-H", ("All Evidence Readings", "All readings", "كل قراءات الأدلة", "كل القراءات التحليلية")),
    ("UI-EVIDENCE-USED-IN-READINGS", ("Used in these Evidence Readings", "Used in these readings",
                                      "يُستخدم هذا الدليل في قراءات الأدلة الآتية", "يُستخدم هذا الدليل في القراءات التحليلية الآتية")),
    ("UI-DOM-EVIDENCE-READINGS-ON-THIS-QUESTION", ("Evidence Readings on this question", "Readings on this question",
                                                   "قراءات الأدلة المتعلقة بهذا السؤال", "القراءات التحليلية المتعلقة بهذا السؤال")),
    ("UI-DATA-READINGS-USING-SOURCE", ("Evidence Readings using this source", "Readings using this source",
                                       "قراءات الأدلة التي تستخدم هذا المصدر", "القراءات التحليلية التي تستخدم هذا المصدر")),
    ("UI-JS-TYPE-READING", (None, None, "قراءة", "قراءة تحليلية")),
    ("UI-READING-DO-NOT-INFER", (None, None, "ما لا يُستنتج", "ما لا ينبغي استنتاجه")),
    ("UI-DOM-WHAT-NOT-TO-CONCLUDE", (None, None, "ما لا يُستنتج", "ما لا ينبغي استنتاجه")),
    ("UI-JS-COMPARE-BOUNDARY", (None, None, "ما لا يُستنتج", "ما لا ينبغي استنتاجه")),
    ("UI-VIS-STATE-UNKNOWN", (None, None, "غير معروف — ليس صفرًا", "غير معروف — لا يعني صفرًا")),
    ("UI-VIS-MISSING", (None, None, "لا قيمة موثَّقة لهذه الفترة — ليست صفرًا", "لا قيمة متحقَّق منها لهذه الفترة — وهذا لا يعني صفرًا")),
    ("UI-VIS-CHAIN-OPEN", (None, None, "لم تُقس بعد — ليس إخفاقًا", "لم تُقس بعد — وهذا لا يعني إخفاقًا")),
    ("UI-VIS-RESULT-NOT-HELD", (None, None, "لا تتضمن قاعدة الأدلة نتيجة مرصودة — ليست صفرًا",
                                "لا تتضمن قاعدة الأدلة نتيجة مرصودة — وهذا لا يعني صفرًا")),
    ("UI-LAND-COV-SUFFICIENT_FOR_QUESTION", ("Sufficient for its question", "Sufficient for the question", "كافٍ لسؤاله", "كافٍ للإجابة عن السؤال")),
    ("UI-LAND-CLASS-REGULATORY", (None, None, "مادة تنظيمية", "نص تنظيمي")),
    ("UI-LAND-CLASS-CONTEXT", ("Context source", "Contextual source", None, None)),
    ("UI-DATA-FILTER-DOMAIN", (None, None, "مستخدم في", "يُستخدم في")),
    ("UI-DATA-FILTER-CLEAR", (None, None, "مسح عوامل التصفية", "إلغاء التصفية")),
    ("UI-DATA-SORT", ("Order", "Sort by", None, None)),
    ("UI-COLOPHON-H", ("Evidence colophon", "About this edition", "بيان الأدلة", "معلومات الإصدار")),
    ("UI-HEADER-TRUST-LINKS", ("Trust links", "About and policies", "روابط الثقة", "عن هذا المورد وسياساته")),
    ("UI-FOOTER-PRODUCT-AND-TRUST-LINKS", ("Product and trust links", "Site sections", "روابط المنتج والثقة", "أقسام المورد")),
    ("UI-CRUMB-BREADCRUMB", (None, None, "مسار الصفحة", "مسار التنقل")),
    ("UI-404-EXPLORE", ("Explore", "Questions", "استكشف", "الأسئلة")),
    ("UI-EVID-DATA-SOURCES", ("Data & sources", "Sources", "البيانات والمصادر", "المصادر")),
    ("UI-EVID-CORRECTIONS-RELEASE-HISTORY", ("Corrections & release history", "Corrections and release history", None, None)),
    ("UI-LAND-DOM-FINANCE", ("Finance", "Banks and microfinance", "التمويل", "البنوك والتمويل الأصغر")),
    ("UI-LAND-DOM-REMITTANCES", (None, None, "التحويلات", "الحوالات")),
    ("UI-LAND-DOM-PROVIDERS", (None, None, "مقدمو الخدمات", "مقدمو الخدمات المالية")),
    ("UI-LAND-DOM-ACCESS", (None, None, "الوصول", "الوصول إلى الخدمات")),
])

# Substrings inside longer interface rows and use rules (column, old, new); each must occur exactly once.
UI_SUBS = [
    ("UI-EXPLORE-MA-BASIS", 2, "These are the priorities the Measurement Agenda marks P0. The full agenda, including its P1 items, is on the Measurement Agenda page.",
     "These are the measurement priorities marked P0. The full list, including its P1 items, is on the Measurement priorities page."),
    ("UI-JS-SEARCH-NAMES-NOTE", 2, "linked from Data & sources.", "linked from Sources."),
    ("UI-JS-SEARCH-NAMES-NOTE", 3, "البيانات والمصادر", "المصادر"),
    ("UI-NAV-HUB-03", 4, "(Evidence Readings)", "(Readings)"),
    ("UI-NAV-HUB-04", 4, "(Data & sources)", "(Sources)"),
    ("UI-NAV-HUB-05", 4, "Method & Measurement", "Method and measurement"),
    ("UI-NAV-HUB-01", 4, "(Explore)", "(Questions)"),
]

# ---------------------------------------------------------------------------------------------------- navigation rows
# (row, column, old, new): primary navigation (rows 6-10; column D is the JSON the generator reads), the route
# dictionary (rows 16-33) and the trust navigation (rows 608-613).
NAV_SUBS = [
    (6, 2, "Explore", "Questions"), (6, 3, "استكشف", "الأسئلة"),
    (6, 4, '"label":{"en":"Explore","ar":"استكشف"}', '"label":{"en":"Questions","ar":"الأسئلة"}'),
    (8, 2, "Evidence Readings", "Readings"), (8, 3, "قراءات الأدلة", "القراءات التحليلية"),
    (8, 4, '"label":{"en":"Evidence Readings","ar":"قراءات الأدلة"}', '"label":{"en":"Readings","ar":"القراءات التحليلية"}'),
    (9, 2, "Data & sources", "Sources"), (9, 3, "البيانات والمصادر", "المصادر"),
    (9, 4, '"label":{"en":"Data & sources","ar":"البيانات والمصادر"}', '"label":{"en":"Sources","ar":"المصادر"}'),
    (10, 2, "Method & Measurement", "Method and measurement"),
    (10, 4, '"label":{"en":"Method & Measurement","ar":"المنهج والقياس"}', '"label":{"en":"Method and measurement","ar":"المنهج والقياس"}'),
    (10, 4, '"label":{"en":"Measurement Agenda","ar":"أولويات القياس"}', '"label":{"en":"Measurement priorities","ar":"أولويات القياس"}'),
    (16, 3, "Explore", "Questions"), (16, 4, "استكشف", "الأسئلة"),
    (17, 3, "People & Needs", "People"), (17, 4, "الناس والاحتياجات", "الأفراد"),
    (18, 3, "Firms & Finance", "Firms"), (18, 4, "المنشآت والتمويل", "المنشآت"),
    (19, 3, "Finance & Institutions", "Banks and microfinance"), (19, 4, "التمويل والمؤسسات", "البنوك والتمويل الأصغر"),
    (20, 4, "مقدمو الخدمات", "مقدمو الخدمات المالية"),
    (21, 3, "Payments & Flows", "Payments"), (21, 4, "المدفوعات والتدفقات", "المدفوعات"),
    (23, 3, "Access & Infrastructure", "Access"), (23, 4, "الوصول والبنية التحتية", "الوصول إلى الخدمات"),
    (24, 3, "Reforms & Programmes", "Reforms"), (24, 4, "الإصلاحات والبرامج", "الإصلاحات"),
    (27, 3, "Compare Evidence", "Compare evidence"),
    (28, 3, "Evidence Readings", "Readings"), (28, 4, "قراءات الأدلة", "القراءات التحليلية"),
    (29, 3, "Reading detail", "Reading"), (29, 4, "تفاصيل القراءة", "قراءة تحليلية"),
    (30, 3, "Measurement Agenda", "Measurement priorities"),
    (31, 3, "Data & sources", "Sources"), (31, 4, "البيانات والمصادر", "المصادر"),
    (31, 8, "Approved reusable data, metadata, sources, versions, rights and citations.",
     "Source directory: metadata, original locators, rights state and citations; no dataset is offered for download. "
     "Named \"Sources\" while public_downloads is false, and \"Sources and data\" (المصادر والبيانات) on the day downloads go live."),
    (33, 4, "عن الموقع", "التعريف بهذا المورد"),
    (608, 3, "عن الموقع", "التعريف بهذا المورد"),
    (610, 2, "Rights & reuse", "Rights and reuse"), (610, 3, "الحقوق وإعادة الاستخدام", "حقوق إعادة الاستخدام"),
    (611, 3, "إتاحة الوصول", "إمكانية الوصول"),
    (613, 2, "Terms", "Terms of use"),
]

# ---------------------------------------------------------------------------------------------------- 02 titles and 03 copy
# (sheet, row, column, old, new)
COPY_SUBS = [
    # /readings/ hub: its title is its navigation name
    (S02, 137, 5, "Evidence Readings", "Readings"), (S02, 137, 6, "قراءات الأدلة", "القراءات التحليلية"),
    # domain h1 prefixes: every domain carries its governed name, in both languages (B3.10 parity)
    (S02, 121, 5, "Finance: ", "Banks and microfinance: "), (S02, 121, 6, "التمويل: ", "البنوك والتمويل الأصغر: "),
    (S02, 129, 6, "قائمة مقدمي الخدمات تثبت", "مقدمو الخدمات المالية: قائمة مقدمي الخدمات تثبت"),
    (S02, 6, 6, "نعرف أجزاءً من شبكة", "الوصول إلى الخدمات: نعرف أجزاءً من شبكة"),
    (S02, 141, 5, "A reform can be real before its outcome is known.", "Reforms: a reform can be real before its outcome is known."),
    (S02, 141, 6, "قد يقع الإصلاح فعلًا", "الإصلاحات: قد يقع الإصلاح فعلًا"),
    # web accessibility = إمكانية الوصول (accessibility sense only)
    (S02, 7, 6, "بيان إتاحة الوصول", "بيان إمكانية الوصول"),
    (S02, 8, 8, "مشكلات إتاحة الوصول", "مشكلات إمكانية الوصول"),
    (S03, 54, 6, "مشكلة في إتاحة الوصول", "مشكلة في إمكانية الوصول"),
    (S03, 54, 7, "مشكلات إتاحة الوصول", "مشكلات إمكانية الوصول"),
    (S03, 55, 7, "هدفًا لإتاحة الوصول", "هدفًا لإمكانية الوصول"),
    (S03, 56, 7, "مشكلات إتاحة الوصول", "مشكلات إمكانية الوصول"),
    (S03, 58, 7, "مشكلات إتاحة الوصول", "مشكلات إمكانية الوصول"),
    # the public inventory list (/data/ s?) names the sections by their labels
    (S03, 79, 5, "Evidence Readings: {{n:readings}}", "Readings: {{n:readings}}"),
    (S03, 79, 5, "Measurement Agenda priorities: {{n:measurement_priorities}}", "Measurement priorities: {{n:measurement_priorities}}"),
    (S03, 80, 7, "قراءات الأدلة: {{n:readings}}", "القراءات التحليلية: {{n:readings}}"),
    # /terms/ points to the rights page by its name
    (S03, 337, 5, "see Rights & reuse.", "see Rights and reuse."),
    (S03, 339, 5, "Rights & reuse.", "Rights and reuse."),
    (S03, 339, 7, "«الحقوق وإعادة الاستخدام»", "«حقوق إعادة الاستخدام»"),
    # /measurement/: the page is the list of measurement priorities, not an "agenda"
    (S03, 136, 5, "This agenda links", "These measurement priorities link"),
    (S03, 137, 4, "How to read the agenda", "How to read the priorities"),
    (S03, 147, 4, "What remains uncertain about the agenda itself", "What remains uncertain about the priorities themselves"),
    (S03, 149, 4, "How the agenda changes", "How the priorities change"),
    (S03, 153, 5, "Each agenda priority sets out", "Each measurement priority sets out"),
]

# regulatory licensing = الترخيص where «الرخصة» meant it (06 CLM-018 and 11 VIS-PROVIDER-OBSERVABILITY)
LICENSING = [("06_EVIDENCE_OBJECTS", 18, 7), ("06_EVIDENCE_OBJECTS", 18, 17), ("11_VISUAL_LIBRARY", 19, 20), ("11_VISUAL_LIBRARY", 19, 22)]

# ---------------------------------------------------------------------------------------------------- B4 rights
RIGHTS_RULE = "Owner brief of 10 October 2026, Part B, B4 (rights presentation). "
UI_NEW = [
    ("UI-FOOTER-LICENCE",
     "CauseWay's own text, analysis and visual designs are licensed under {licence} unless otherwise noted; third-party material remains under its owners' terms.",
     "يُتاح نص CauseWay الخاص وتحليلاته وتصاميمه المرئية بموجب رخصة {licence} ما لم يُذكر خلاف ذلك، وتبقى مواد الجهات الأخرى خاضعة لشروط أصحابها.",
     RIGHTS_RULE + "Footer licence line on every page; {licence} is UI-LICENCE-NAME linked to UI-LICENCE-DEED-URL. Text only, no badge."),
    ("UI-LICENCE-NAME", "CC BY 4.0", "CC BY 4.0",
     RIGHTS_RULE + "Short name of the reuse licence of CauseWay's own content, as decided on 3 October 2026 and closed on 10 October 2026; an identifier, not a quantity."),
    ("UI-LICENCE-DEED-URL", "https://creativecommons.org/licenses/by/4.0/", "https://creativecommons.org/licenses/by/4.0/deed.ar",
     RIGHTS_RULE + "The official Creative Commons deed of CC BY 4.0, each language's own (both checked 10 October 2026, HTTP 200). Printed as "
                   "the footer link and as <link rel=\"license\"> in every page's head."),
]

RIGHTS_S6_EN_OLD_START = "CauseWay licenses the content it owns in this resource under the Creative Commons Attribution 4.0 International licence"
RIGHTS_S6_EN = (
    "CauseWay licenses the content it owns in this resource under the Creative Commons Attribution 4.0 International licence "
    "(CC BY 4.0; deed https://creativecommons.org/licenses/by/4.0/, legal code https://creativecommons.org/licenses/by/4.0/legalcode.en). "
    "Covered: CauseWay's text and analysis in English and Arabic, its visual designs, the compiled evidence records and the figures "
    "CauseWay calculates, and the structure and annotations of the data exports when they are published. "
    "Not covered: material published by others — documents, data, tables, figures and text remain under their publishers' terms, including "
    "where this resource reports, quotes or translates them, and this resource does not host copies of their files; the CauseWay name, logo "
    "and marks; and the software code of the repository that builds this resource, which is outside this licence. "
    "Figures derived from survey microdata: the confidence intervals this resource derives from the Global Findex respondent file for Yemen "
    "(evidence record CLM-026) are computed under the World Bank Microdata Research License, which permits publishing aggregate statistics "
    "with the data cited. Cite the data as that licence requires: Demirgüç-Kunt, Klapper, Singer and Ansar, The Global Findex Database 2021: "
    "Financial Inclusion, Digital Payments, and Resilience in the Age of COVID-19, World Bank. CC BY 4.0 does not extend to the underlying "
    "microdata, which this resource does not host or redistribute. "
    "You may share and adapt CauseWay's content for any purpose, provided you credit CauseWay, link to the licence and indicate whether you "
    "made changes: give the title, the author (CauseWay), the source (this resource and the page address), the licence (CC BY 4.0) and the "
    "changes made. For a reused figure, use two lines: first this resource (Yemen Financial Inclusion Evidence, the record, CauseWay, the "
    "edition and the page address), then the original source that the record names (publisher, title, year and link). "
    "This page states the licence CauseWay applies to its own content; it does not state that any third-party rights have been cleared.")
RIGHTS_S6_AR_OLD_START = "تتيح CauseWay المحتوى الذي تملكه في هذا المورد بموجب رخصة المشاع الإبداعي"
RIGHTS_S6_AR = (
    "تتيح CauseWay المحتوى الذي تملكه في هذا المورد بموجب رخصة المشاع الإبداعي «نَسب المُصنَّف 4.0 دولي» "
    "(CC BY 4.0؛ صك الرخصة https://creativecommons.org/licenses/by/4.0/deed.ar، والنص القانوني https://creativecommons.org/licenses/by/4.0/legalcode.ar). "
    "تشمل الرخصة: نصوص CauseWay وتحليلاتها بالعربية والإنجليزية، وتصاميمها المرئية، وسجلات الأدلة المجمَّعة والأرقام التي تحتسبها CauseWay، "
    "وبنية ملفات البيانات المُصدَّرة وشروحها عند نشرها. "
    "ولا تشمل الرخصة: مواد الجهات الأخرى، فالوثائق والبيانات والجداول والرسوم والنصوص التي تنشرها جهات أخرى تبقى خاضعة لشروط ناشريها، بما في ذلك "
    "حين يوردها هذا المورد أو يقتبسها أو يترجمها، ولا يستضيف هذا المورد نسخًا من ملفاتها؛ واسم CauseWay وشعارها وعلاماتها؛ والشيفرة البرمجية "
    "للمستودع الذي يبني هذا المورد، فهي خارج نطاق هذه الرخصة. "
    "الأرقام المشتقة من البيانات الجزئية للمسوح: تُحتسب فترات الثقة التي يستخرجها هذا المورد من ملف المستجيبين في مسح Global Findex لليمن "
    "(سجل الدليل CLM-026) بموجب رخصة البحث للبيانات الجزئية لدى البنك الدولي، التي تجيز نشر الإحصاءات التجميعية مع الاستشهاد بالبيانات. "
    "استشهد بالبيانات كما تشترط تلك الرخصة: Demirgüç-Kunt وKlapper وSinger وAnsar، The Global Findex Database 2021: Financial Inclusion, "
    "Digital Payments, and Resilience in the Age of COVID-19، البنك الدولي. ولا تمتد رخصة CC BY 4.0 إلى البيانات الجزئية الأصلية، التي لا "
    "يستضيفها هذا المورد ولا يعيد توزيعها. "
    "ويجوز لك مشاركة محتوى CauseWay وتعديله لأي غرض، بشرط أن تنسبه إلى CauseWay، وأن تضع رابطًا إلى الرخصة، وأن تبيّن ما إذا كنت قد أجريت "
    "تغييرات: اذكر العنوان، والمؤلف (CauseWay)، والمصدر (هذا المورد ورابط الصفحة)، والرخصة (CC BY 4.0)، والتغييرات التي أجريتها. وعند إعادة "
    "استخدام رقم، استعمل سطرين: أولًا هذا المورد (أدلة الشمول المالي في اليمن، والسجل، وCauseWay، والإصدار، ورابط الصفحة)، ثم المصدر الأصلي "
    "الذي يسمّيه السجل (الناشر، والعنوان، والسنة، والرابط). "
    "وتذكر هذه الصفحة الرخصة التي تطبقها CauseWay على محتواها الخاص، ولا تفيد بأن أي حقوق لجهات أخرى قد سُوّيت.")

# ---------------------------------------------------------------------------------------------------- search aliases
ALIASES = [
    ("explore; explore questions", "استكشف; استكشف الأسئلة", "route:/explore/", None, None),
    ("evidence readings; evidence reading; readings; reading; analysis", "قراءات الأدلة; قراءة أدلة; القراءات; قراءة تحليلية; التحليلات",
     "route:/readings/", None, None),
    ("data; data and sources; data & sources; dataset; datasets; download", "البيانات; البيانات والمصادر; بيانات; مجموعة بيانات; تنزيل",
     "route:/data/",
     "Discovery aid only: this resource is a directory of sources that links to their publishers; it offers no dataset for download.",
     "أداة اكتشاف فقط: هذا المورد فهرس للمصادر يحيل إلى ناشريها، ولا يتيح أي مجموعة بيانات للتنزيل."),
    ("method and measurement; method & measurement", "المنهج والقياس", "route:/methodology/ | route:/measurement/", None, None),
    ("report an issue; report an error; error", "أبلغ عن مشكلة; أبلغ عن خطأ; خطأ", "route:/contact/ | route:/corrections/", None, None),
    ("trust; about this resource", "الثقة; عن الموقع; عن المورد; التعريف بالمورد", "route:/about/", None, None),
    ("finance; banks; banking", "التمويل; البنوك; المصارف", "route:/finance/", None, None),
    ("accessibility; accessibility statement", "إتاحة الوصول; إمكانية الوصول; بيان إمكانية الوصول", "route:/accessibility/", None, None),
    ("access; access to services; access points", "الوصول; الوصول إلى الخدمات; نقاط الوصول", "route:/access/", None, None),
    ("providers; service providers; financial service providers", "مقدمو الخدمات; مقدمي الخدمات; مقدمو الخدمات المالية", "route:/providers/", None, None),
    ("personal remittances; workers' remittances; migrant remittances", "الحوالات; التحويلات الشخصية; تحويلات العاملين; رسوم الحوالات",
     "route:/remittances/", None, None),
    ("licensed; unlicensed; licence withdrawal", "مرخص; غير مرخص; سحب الترخيص", "route:/providers/ | document_type:decision/enforcement", None, None),
]

# ---------------------------------------------------------------------------------------------------- terminology register
REG_RULE = "Governed terminology register (owner brief of 10 October 2026, Part B, B5). One term per concept, both languages."
REGISTER_HEADER = ["term_id", "term_en", "term_ar", "definition_en", "definition_ar", "do_not_use", "rule_en", "rule_ar"]
REGISTER = [
    ("TERM-001", "remittances", "الحوالات",
     "Money sent by a person or household to a person or household, from abroad or within Yemen, and aggregates of such flows.",
     "أموال يرسلها فرد أو أسرة إلى فرد أو أسرة، من الخارج أو داخل اليمن، ومجاميع هذه التدفقات.",
     "bare «التحويلات» for remittances",
     "In balance-of-payments text keep the source's own concept (personal remittances, workers' remittances) and present it as the source's label.",
     "في نصوص ميزان المدفوعات يُحتفظ بمفهوم المصدر نفسه (التحويلات الشخصية، تحويلات العاملين، تحويلات المغتربين) ويُقدَّم بوصفه تسمية المصدر."),
    ("TERM-002", "cash transfers", "التحويلات النقدية",
     "Payments to people from a government, programme, donor or humanitarian agency.",
     "مدفوعات للأفراد من حكومة أو برنامج أو جهة مانحة أو إنسانية.",
     "«الحوالات النقدية»; 'remittances' for programme payments",
     "Always qualified; a cash transfer is not a remittance.", "تُقيَّد دائمًا بالوصف؛ والتحويل النقدي ليس حوالة."),
    ("TERM-003", "funds transfer", "التحويل / تحويل الأموال",
     "The act or regulated activity of moving funds between accounts or providers.",
     "عملية نقل الأموال بين الحسابات أو مقدمي الخدمات، أو النشاط المنظَّم الذي يؤديها.",
     "«حوالة» for the act of transfer",
     "Quote the names of regulated activities and decisions as published.", "تُنقل أسماء الأنشطة المنظمة والقرارات كما نُشرت."),
    ("TERM-004", "reuse licence (CC BY 4.0)", "الرخصة (رخصة CC BY 4.0)",
     "The copyright licence under which CauseWay publishes its own content.",
     "رخصة حق المؤلف التي تتيح CauseWay بموجبها محتواها الخاص.",
     "«الترخيص» for the reuse licence; 'license' as a noun",
     "'licence' is the noun and 'license' the verb; write 'licensed under CC BY 4.0'.",
     "تُكتب «متاح بموجب رخصة CC BY 4.0»."),
    ("TERM-005", "regulatory licensing", "الترخيص",
     "Authorisation by a regulator for an institution to carry out an activity.",
     "إذن تمنحه جهة رقابية لمؤسسة كي تزاول نشاطًا.",
     "«الرخصة» in the regulatory sense",
     "Name the issuer and the date. A licence is not operation. CauseWay holds no regulatory licence and claims none.",
     "يُذكر مُصدر الترخيص وتاريخه. والترخيص لا يعني التشغيل. ولا تملك CauseWay ترخيصًا رقابيًا ولا تدّعيه."),
    ("TERM-006", "licensed (regulatory)", "مرخَّص",
     "Holding a regulatory licence on a stated date.", "حاصل على ترخيص رقابي في تاريخ محدد.",
     "«معتمد»; «مسجَّل»", "Unlicensed = غير مرخَّص.", "غير الحاصل على ترخيص = غير مرخَّص."),
    ("TERM-007", "listing", "الإدراج في قائمة / مُدرَج",
     "Appearance on an official list on a date.", "الظهور في قائمة رسمية في تاريخ محدد.",
     "«التسجيل»; 'listing or licensing' as one concept",
     "Listing is not licensing, and neither is operation.", "الإدراج ليس ترخيصًا، ولا أيٌّ منهما يعني التشغيل."),
    ("TERM-008", "account", "الحساب",
     "An account held at a bank or another provider.", "حساب لدى بنك أو مقدم خدمة آخر.",
     "'people' or «الأشخاص» for accounts", "Accounts are not people.", "الحسابات ليست أشخاصًا."),
    ("TERM-009", "active (account, wallet, user)", "نشط / نشطة",
     "Used within the activity window the source defines.", "مستخدَم خلال نافذة النشاط التي يحددها المصدر.",
     "«فعّال»; «مفعَّل»; «قائم»",
     "State the source's activity window once. Inactive = غير نشط; dormant = خامل. A branch or point is 'operating' (عامل) only when operation is evidenced.",
     "تُذكر نافذة النشاط التي يحددها المصدر مرة واحدة. غير النشط = غير نشط؛ والخامل = خامل. ولا يوصف الفرع أو النقطة بأنه عامل إلا إذا ثبت التشغيل."),
    ("TERM-010", "subscriber", "المشترك",
     "A count as labelled by its publisher.", "عدد كما يسميه ناشره.",
     "«المستخدم»; «العميل» for subscribers",
     "Subscribers are not users, accounts or people, and are never summed with them.",
     "المشتركون ليسوا مستخدمين ولا حسابات ولا أشخاصًا، ولا يُجمعون معها."),
    ("TERM-011", "evidence record", "سجل الدليل / سجلات الأدلة",
     "The governed public record of one piece of evidence.", "السجل العام الخاضع للحوكمة لدليل واحد.",
     "'Evidence Record' in running text; «السجل الدليلي»",
     "Capital only at the start of a label.", "تبدأ التسمية بها دون تغيير."),
    ("TERM-012", "reading", "قراءة تحليلية / القراءات التحليلية",
     "A bounded argument built across several evidence records.", "حجة محددة النطاق مبنية على عدة سجلات أدلة.",
     "'Evidence Reading'; «قراءة أدلة»; «التحليلات»",
     "The section is 'Readings' (القراءات التحليلية); each item is 'Reading' (قراءة تحليلية).",
     "القسم «القراءات التحليلية»، وكل بند «قراءة تحليلية»."),
    ("TERM-013", "measurement priority", "أولوية القياس / أولويات القياس",
     "A decision-valued unknown with the evidence needed to resolve it.", "مجهول مؤثر في القرار مع الدليل اللازم لحسمه.",
     "'Measurement Agenda'; «أجندة القياس» (search alias only)",
     "The section is 'Measurement priorities'.", "القسم «أولويات القياس»."),
    ("TERM-014", "source record", "سجل المصدر",
     "The directory entry for one source.", "مُدخل الفهرس لمصدر واحد.",
     "", "The copyable identifier is the source reference (مرجع المصدر).", "المعرّف القابل للنسخ هو «مرجع المصدر»."),
    ("TERM-015", "this resource", "هذا المورد",
     "The product's self-reference.", "الإشارة التي يستعملها المنتج إلى نفسه.",
     "'this site'; «هذا الموقع»; «المنصة»",
     "'Evidence base' (قاعدة الأدلة) is the governed evidence, written in full.", "«قاعدة الأدلة» هي الأدلة الخاضعة للحوكمة، وتُكتب كاملة."),
    ("TERM-016", "people (domain)", "الأفراد",
     "The people-side domain.", "مجال جانب الأفراد.",
     "«الناس» in labels",
     "Use 'adults' (البالغون) when the source counts adults; 'population' (السكان) for the whole population.",
     "تُستعمل «البالغون» حين يعدّ المصدر البالغين، و«السكان» لمجموع السكان."),
    ("TERM-017", "providers", "مقدمو الخدمات المالية",
     "Institutions that provide financial services.", "المؤسسات التي تقدم الخدمات المالية.",
     "«مزودو» / «مزودي» (except in quoted regulatory names)",
     "Case forms (مقدمو / مقدمي) follow grammar.", "تتبع صيغتا «مقدمو» و«مقدمي» قواعد الإعراب."),
    ("TERM-018", "access point", "نقطة الوصول المالي",
     "A location or device where a financial service can be reached.", "موقع أو جهاز يمكن الوصول منه إلى خدمة مالية.",
     "«نقطة خدمة»; «منفذ»", "A count of access points is not use.", "عدد نقاط الوصول لا يعني الاستخدام."),
    ("TERM-019", "web accessibility", "إمكانية الوصول",
     "Whether people with disabilities can use the pages.", "قدرة الأشخاص ذوي الإعاقة على استخدام الصفحات.",
     "«إتاحة الوصول» for accessibility",
     "Keeps accessibility apart from the Access domain (الوصول إلى الخدمات).", "يفصل بين إمكانية الوصول ومجال «الوصول إلى الخدمات»."),
    ("TERM-020", "sources (section)", "المصادر",
     "The directory of sources and their original locators.", "فهرس المصادر وروابطها الأصلية.",
     "'Data & sources' while nothing is downloadable",
     "Becomes 'Sources and data' (المصادر والبيانات) on the day public_downloads is true.",
     "تصبح «المصادر والبيانات» يوم يصبح public_downloads صحيحًا."),
    ("TERM-021", "missing value", "غير معروف — لا يعني صفرًا",
     "A value the evidence base does not hold.", "قيمة لا تتضمنها قاعدة الأدلة.",
     "«ليس صفرًا» (reads as a stated value)", "Missing is not zero.", "المفقود لا يعني صفرًا."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    _, ui = ui_block_end(s)

    for ui_id, (oe, ne, oa, na) in UI.items():
        set_ui(s, F, ui_id, ne, na, oe, oa)

    for ui_id, c, old, new in UI_SUBS:
        if ui_id not in ui:
            raise TxError(f"{F}: 04 has no {ui_id}")
        s.replace(F, S04, ui[ui_id], c, old, new, f"{ui_id}.c{c}")

    for row, c, old, new in NAV_SUBS:
        cur = s.ed.get_value(S04, row, c)
        if cur == old:
            s.set(F, S04, row, c, new, old, f"04!r{row}c{c}")
        else:
            s.replace(F, S04, row, c, old, new, f"04!r{row}c{c}")

    for sheet, row, c, old, new in COPY_SUBS:
        cur = s.ed.get_value(sheet, row, c)
        if cur == old:
            s.set(F, sheet, row, c, new, old, f"{sheet}!r{row}c{c}")
        else:
            s.replace(F, sheet, row, c, old, new, f"{sheet}!r{row}c{c}")

    for sheet, row, c in LICENSING:
        s.replace(FG, sheet, row, c, "القائمة أو الرخصة", "القائمة أو الترخيص", f"{sheet}!r{row}c{c}")

    subs = json.load(open(os.path.join(HERE, "nb_1_remittance_substitutions.json"), encoding="utf-8"))
    for p in subs:
        s.set(FG, p["sheet"], int(p["row"]), col(p["col_letter"]), p["new_ar"], p["old_ar"], f"{p['field']} (remittances = الحوالات)")

    # B4: the /rights/ licence section, guarded by its authored opening words
    s.rewrite_section(FR, "/rights/", 6, "en", "body", RIGHTS_S6_EN, RIGHTS_S6_EN_OLD_START)
    s.rewrite_section(FR, "/rights/", 6, "ar", "body", RIGHTS_S6_AR, RIGHTS_S6_AR_OLD_START)
    insert_ui_rows(s, FR, UI_NEW)

    # B5: search aliases appended to the alias block; the terminology register as a new titled block after it
    g = s.grid(S04)
    ids = [i for i, x in enumerate(g, 1) if x and isinstance(x[0], str) and x[0].startswith("SEARCH-ALIAS-")]
    last = max(ids)
    if any(c not in (None, "") for c in (g[last] if last < len(g) else [])):
        raise TxError(f"{F}: the row after the last search alias is not empty")
    have = {t.strip().lower() for i in ids for k in (1, 2) for t in str(g[i - 1][k] or "").split(";") if t.strip()}
    n0 = int(g[last - 1][0].rsplit("-", 1)[1])
    rows = []
    for k, (en, ar, tgt, ben, bar) in enumerate(ALIASES, start=1):
        for t in [x.strip().lower() for x in (en + ";" + ar).split(";")]:
            if t in have:
                raise TxError(f"{F}: alias term {t!r} already in the alias block")
            have.add(t)
        rows.append({1: f"SEARCH-ALIAS-{n0 + k:03d}", 2: en, 3: ar, 4: tgt, 5: ben, 6: bar})
    reg = [{}, {1: "Terminology register"}, {i + 1: h for i, h in enumerate(REGISTER_HEADER)}]
    reg += [{i + 1: v for i, v in enumerate(r)} for r in REGISTER]
    s.ed.insert_rows(S04, last + 1, rows + reg)
    for r in rows:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S04), ("row", None), ("col", None), ("field", r[1]), ("old", None),
                                     ("new", r[2] + " || " + r[3] + " -> " + r[4])]))
    for r in REGISTER:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S04), ("row", None), ("col", None), ("field", r[0]), ("old", None),
                                     ("new", r[1] + " || " + r[2])]))

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "NB-1"),
        ("summary", "Public naming and terminology (owner brief of 10 October 2026, Part B): labels, governed term substitutions, "
                    "rights presentation, search aliases and a terminology register; no figure, unit, period, universe, source, route or identifier changed"),
        ("items", OrderedDict([("interface_labels", len(UI)), ("interface_substrings", len(UI_SUBS)), ("navigation_cells", len(NAV_SUBS)),
                               ("copy_cells", len(COPY_SUBS)), ("licensing_cells", len(LICENSING)), ("remittance_cells", len(subs)),
                               ("new_interface_rows", len(UI_NEW)), ("search_aliases", len(ALIASES)), ("register_terms", len(REGISTER))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
