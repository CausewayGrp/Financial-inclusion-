# -*- coding: utf-8 -*-
"""Public naming and terminology, transaction PN-1. English and Arabic together.

  python3 pn_1_public_naming.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The owner's brief of 10 October 2026, Part B, under the steward designation recorded in
audit/OWNER_DECISIONS_2026-10-10.md (OWN-NAME-01). Language only: no route, URL or feature changes, no change to the
meaning of evidence, and no number, period, universe or limit moves. Every change is a label, a governed term, a title
prefix or a search alias. English and Arabic move together; where one language already held the right name, only the
other moves, and that is stated per row.

What it changes, and why (the lead's decisions after an independent Arabic editor, English editor, information-
architecture lead, red team and an institutional benchmark; audit/public_naming/PUBLIC_NAMING_LOG.md carries the full
table, the dissents and the hypotheses that were overturned):

 1. "Measurement Agenda" -> "Measurement priorities" (English only). "Agenda" implies this resource will carry out the
    measurement; it only names what is missing. The object type (UI-MA-OPEN), the Arabic nav label and the search
    alias already say priorities, so English was the sole outlier.
 2. "Report an issue" -> "Report an error" / «أبلغ عن مشكلة» -> «أبلغ عن خطأ», on both controls. The destination's own
    governed copy says error twice: /contact/'s title is "Contact and report an error / التواصل والإبلاغ عن خطأ" and
    its section heading is "Report a suspected error / أبلغ عن خطأ محتمل".
 3. The Reading item's eyebrow "Evidence Reading / قراءة أدلة" -> "Reading / قراءة". It removes the Evidence/Evidence
    stutter where a reader meets it; the search facet and the breadcrumb family key already say Reading / قراءة. The
    section keeps its own name.
 4. The /remittances/ domain label «التحويلات» -> «الحوالات» (Arabic only). One page had two Arabic names: this label
    said «التحويلات» while the route surface said «الحوالات». «الحوالات» is the operation sense this corpus already
    reserves («وكيل حوالات»; «الحوالات المحلية», 216 occurrences) and it never collides with «التحويلات النقدية»
    (cash transfers, 102 occurrences). No sweep: see the register block, rule TERM-REMIT.
 5. The /providers/ label «مقدمو الخدمات» -> «مقدمو الخدمات المالية» (Arabic only). Bare «مقدمو الخدمات» is generic.
    English stays "Providers", so no new claim is made in English, and the page's own rule
    («الإدراج أو الترخيص ≠ التشغيل») is untouched.
 6. The /access/ label «الوصول» -> «الوصول إلى الخدمات المالية» (Arabic only). Bare «الوصول» did three jobs in Arabic
    (this domain, the chain label, and accessibility «إتاحة الوصول»). This exact string is already governed for
    English "Access" at UI-VIS-CHAIN-ACCESS, so no new string enters the corpus.
 7. "Data & sources / البيانات والمصادر" -> "Sources / المصادر". The one truthfulness failure in the navigation:
    nothing on the page is downloadable (public_downloads = false); it is a directory of the original sources. The
    promotion rule is recorded in the register (TERM-SOURCES): it becomes "Sources and data / المصادر والبيانات" only
    when a machine-readable file of the published evidence is downloadable from this site and reachable from that page.
 8. "Explore / استكشف" -> "Key questions / الأسئلة الرئيسية". The only imperative among five nouns, and the only verb
    in the Arabic menu. Qualified so it cannot be read as an FAQ: bare "Questions" / «الأسئلة» would collide with 103
    governed uses of «الأسئلة» in other senses. The verb "explore" keeps its own strings
    (UI-DOM-EXPLORE-QUESTIONS, UI-DOM-UNDERSTAND-EXPLORE-VERIFY) and is not touched.
 9. Sentence case, and "and" for "&", on every label in scope (GOV.UK style guide). Named object types stay
    capitalised in prose: Evidence Record, Evidence Reading, Evidence Passport.
10. Accessible names: "Trust links / روابط الثقة" -> "About and policy links / روابط المعلومات والسياسات", and
    "Product and trust links / روابط المنتج والثقة" -> "Site and policy links / روابط الموقع والسياسات". An accessible
    name must say what it opens; "product" is repository vocabulary a reader never sees.
11. One Arabic string for "Cite this page": UI-COLOPHON-CITATION adopts UI-HEADER-CITE-THIS-PAGE's «استشهد بهذه
    الصفحة». Both are links a reader activates.
12. The /data/ facet "Used on / مستخدم في" -> "Where it is used / مجال الاستخدام": a cryptic fragment among three
    nominal sibling facets.
13. Prefix parity on the eight domain titles: English lacked the domain prefix on /reforms/; Arabic lacked it on
    /access/, /providers/ and /reforms/. Four titles gain their prefix and the three terminal full stops go, so all
    eight are self-identifying in their first two words and none ends in a full stop. No number, period, universe or
    limit moves; where a prefix repeats a phrase the sentence already carried, the phrase is said once.
14. Five search aliases, so no retired word and no reader's habit stops working: explore, data/dataset/download and
    «البيانات والمصادر», issue/«مشكلة», «الوصول»/«الوصول إلى الخدمات», and «مقدمو الخدمات».
15. A governed terminology register (English | Arabic | definition | do-not-use | rule), so the next editor does not
    re-introduce a retired form or flatten a distinction the evidence depends on.

NOT changed, and why, is in audit/public_naming/PUBLIC_NAMING_LOG.md: "Evidence Readings" is not renamed to
"Analysis / التحليلات" (three collisions, two of them in the bytes); "Finance" is not renamed to "Credit and savings"
(narrower than the page); «التحويلات» is not swept to «الحوالات» (it would change governed concept names); "About /
عن الموقع" is not changed to «عن المورد» (unvocalised «المورد» reads as *muwarrid*, "supplier"); and the <title>/h1
split is escalated, not done.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError, set_ui, ui_block_end  # noqa: E402

F = "PN-1:NAMING"
S04 = "04_NAV_UX"
S02 = "02_SITE_MAP"
S03 = "03_PAGE_SECTIONS"

# ---------------------------------------------------------------- 04 primary navigation (rows 6-10: label_en, label_ar, route_or_group)
NAV_ROWS = [
    (6, "Explore", "Key questions", "استكشف", "الأسئلة الرئيسية",
     '{"id":"NAV-EXPLORE","label":{"en":"Explore","ar":"استكشف"},"route":"/explore","kind":"DIRECT"}',
     '{"id":"NAV-EXPLORE","label":{"en":"Key questions","ar":"الأسئلة الرئيسية"},"route":"/explore","kind":"DIRECT"}'),
    (8, "Evidence Readings", "Evidence readings", None, None,
     '{"id":"NAV-READINGS","label":{"en":"Evidence Readings","ar":"قراءات الأدلة"},"route":"/readings","kind":"DIRECT"}',
     '{"id":"NAV-READINGS","label":{"en":"Evidence readings","ar":"قراءات الأدلة"},"route":"/readings","kind":"DIRECT"}'),
    (9, "Data & sources", "Sources", "البيانات والمصادر", "المصادر",
     '{"id":"NAV-DATA","label":{"en":"Data & sources","ar":"البيانات والمصادر"},"route":"/data","kind":"DIRECT"}',
     '{"id":"NAV-DATA","label":{"en":"Sources","ar":"المصادر"},"route":"/data","kind":"DIRECT"}'),
    (10, "Method & Measurement", "Method and measurement", None, None,
     '{"id":"NAV-METHOD-MEASUREMENT","label":{"en":"Method & Measurement","ar":"المنهج والقياس"},"kind":"GROUP",'
     '"children":[{"id":"NAV-METHODOLOGY","label":{"en":"Methodology","ar":"المنهجية"},"route":"/methodology"},'
     '{"id":"NAV-MEASUREMENT","label":{"en":"Measurement Agenda","ar":"أولويات القياس"},"route":"/measurement"}]}',
     '{"id":"NAV-METHOD-MEASUREMENT","label":{"en":"Method and measurement","ar":"المنهج والقياس"},"kind":"GROUP",'
     '"children":[{"id":"NAV-METHODOLOGY","label":{"en":"Methodology","ar":"المنهجية"},"route":"/methodology"},'
     '{"id":"NAV-MEASUREMENT","label":{"en":"Measurement priorities","ar":"أولويات القياس"},"route":"/measurement"}]}'),
]

# ---------------------------------------------------------------- 04 route dictionary (surface_en col 3, surface_ar col 4)
SURFACES = [
    (16, "Explore", "Key questions", "استكشف", "الأسئلة الرئيسية"),
    (17, "People & Needs", "People and needs", "الناس والاحتياجات", "الأفراد والاحتياجات"),
    (18, "Firms & Finance", "Firms and finance", None, None),
    (19, "Finance & Institutions", "Finance and institutions", None, None),
    (20, None, None, "مقدمو الخدمات", "مقدمو الخدمات المالية"),
    (21, "Payments & Flows", "Payments and flows", None, None),
    (23, "Access & Infrastructure", "Access and infrastructure", None, None),
    (24, "Reforms & Programmes", "Reforms and programmes", None, None),
    (27, "Compare Evidence", "Compare evidence", None, None),
    (28, "Evidence Readings", "Evidence readings", None, None),
    (29, "Reading detail", "Reading", "تفاصيل القراءة", "قراءة"),
    (30, "Measurement Agenda", "Measurement priorities", None, None),
    (31, "Data & sources", "Sources", "البيانات والمصادر", "المصادر"),
]

# ---------------------------------------------------------------- 04 trust navigation (label_en col 2, label_ar col 3)
TRUST = [(610, "Rights & reuse", "Rights and reuse", None, None)]

# ---------------------------------------------------------------- 04 governed interface copy (by UI id)
UI_SET = [
    ("UI-HEADER-REPORT-AN-ISSUE", "Report an error", "أبلغ عن خطأ", "Report an issue", "أبلغ عن مشكلة"),
    ("UI-EVID-REPORT-AN-ISSUE", "Report an error", "أبلغ عن خطأ", "Report an issue", "أبلغ عن مشكلة"),
    ("UI-READING-EYEBROW", "Reading", "قراءة", "Evidence Reading", "قراءة أدلة"),
    ("UI-READING-ALL-H", "All Evidence readings", None, "All Evidence Readings", None),
    ("UI-EVIDENCE-USED-IN-READINGS", "Used in these Evidence readings", None, "Used in these Evidence Readings", None),
    ("UI-DOM-EVIDENCE-READINGS-ON-THIS-QUESTION", "Evidence readings on this question", None,
     "Evidence Readings on this question", None),
    ("UI-DATA-READINGS-USING-SOURCE", "Evidence readings using this source", None,
     "Evidence Readings using this source", None),
    ("UI-LAND-DOM-REMITTANCES", None, "الحوالات", None, "التحويلات"),
    ("UI-LAND-DOM-PROVIDERS", None, "مقدمو الخدمات المالية", None, "مقدمو الخدمات"),
    ("UI-LAND-DOM-ACCESS", None, "الوصول إلى الخدمات المالية", None, "الوصول"),
    ("UI-HEADER-TRUST-LINKS", "About and policy links", "روابط المعلومات والسياسات", "Trust links", "روابط الثقة"),
    ("UI-FOOTER-PRODUCT-AND-TRUST-LINKS", "Site and policy links", "روابط الموقع والسياسات",
     "Product and trust links", "روابط المنتج والثقة"),
    ("UI-COLOPHON-CITATION", None, "استشهد بهذه الصفحة", None, "الاستشهاد بهذه الصفحة"),
    ("UI-DATA-FILTER-DOMAIN", "Where it is used", "مجال الاستخدام", "Used on", "مستخدم في"),
    ("UI-404-EXPLORE", "Key questions", "الأسئلة الرئيسية", "Explore", "استكشف"),
    ("UI-EVID-DATA-SOURCES", "Sources", "المصادر", "Data & sources", "البيانات والمصادر"),
    ("UI-EXPLORE-MA-BASIS",
     "These are the priorities the Measurement priorities page marks P0. The full list, including its P1 items, is on "
     "the Measurement priorities page.", None,
     "These are the priorities the Measurement Agenda marks P0. The full agenda, including its P1 items, is on the "
     "Measurement Agenda page.", None),
    ("UI-JS-SEARCH-NAMES-NOTE",
     "Names of entities from the regulator's lists and enforcement decisions are not reproduced here; the original "
     "documents are linked from Sources.",
     "لا تُذكر هنا أسماء الجهات الواردة في قوائم الجهة الرقابية وقرارات الإنفاذ؛ ويمكن الوصول إلى الوثائق الأصلية من صفحة المصادر.",
     "Names of entities from the regulator's lists and enforcement decisions are not reproduced here; the original "
     "documents are linked from Data & sources.",
     "لا تُذكر هنا أسماء الجهات الواردة في قوائم الجهة الرقابية وقرارات الإنفاذ؛ ويمكن الوصول إلى الوثائق الأصلية من صفحة البيانات والمصادر."),
    ("UI-SEARCH-SEARCH-QUESTIONS-EVIDENCE-READINGS-AND",
     "Search questions, evidence, readings and sources",
     "ابحث في الأسئلة والأدلة والقراءات والمصادر",
     "Search questions, evidence, readings and sources...",
     "ابحث في الأسئلة والأدلة والقراءات والمصادر..."),
]

# ---------------------------------------------------------------- 02 site map titles (title_en col 5, title_ar col 6)
TITLES = [
    ("/access/", None, None,
     "نعرف أجزاءً من شبكة الوصول إلى الخدمات المالية، لكننا لا نملك بعد خريطة وطنية موثوقة لما يعمل فعليًا على الأرض.",
     "الوصول إلى الخدمات المالية: نعرف أجزاءً من الشبكة، لكننا لا نملك بعد خريطة وطنية موثوقة لما يعمل فعليًا على الأرض"),
    ("/providers/", None, None,
     "قائمة مقدمي الخدمات تثبت وضعًا رسميًا في تاريخ محدد، لكنها لا تثبت التشغيل بذاتها.",
     "مقدمو الخدمات المالية: القائمة الرسمية تثبت وضعًا رسميًا في تاريخ محدد، لكنها لا تثبت التشغيل بذاتها"),
    ("/reforms/", "A reform can be real before its outcome is known.",
     "Reforms: a reform can be real before its outcome is known",
     "قد يقع الإصلاح فعلًا وتبقى نتيجته مجهولة.",
     "الإصلاحات: قد يقع الإصلاح فعلًا وتبقى نتيجته مجهولة"),
    ("/readings/", "Evidence Readings", "Evidence readings", None, None),
]

# ---------------------------------------------------------------- 03 page sections (/data/ "What this resource holds")
COVERAGE_OLD = ("Public Evidence Records: {{n:evidence_records}}\n"
                "Documented chronology events: {{n:chronology_events}}\n"
                "Public claims (each is also an Evidence Record): {{n:public_claims}}\n"
                "Registered source records: {{n:sources}}\n"
                "Source records with a public link to the original: {{n:public_locators}}\n"
                "Curated source and report cards: {{n:curated_resources}}\n"
                "Evidence Readings: {{n:readings}}\n"
                "Measurement Agenda priorities: {{n:measurement_priorities}}")
COVERAGE_NEW = COVERAGE_OLD.replace("Evidence Readings: ", "Evidence readings: ") \
                           .replace("Measurement Agenda priorities: ", "Measurement priorities: ")

# ---------------------------------------------------------------- 04 search aliases (new rows)
ALIASES = [
    ("SEARCH-ALIAS-034", "explore; explore the questions", "استكشف; الاستكشاف", "route:/explore/",
     "Discovery aid only: the questions hub is named \"Key questions\".",
     "أداة اكتشاف فقط: اسم صفحة الأسئلة هو «الأسئلة الرئيسية»."),
    ("SEARCH-ALIAS-035", "data; dataset; datasets; download; downloads; data and sources",
     "البيانات; بيانات; تنزيل; تحميل; البيانات والمصادر", "route:/data/",
     "Discovery aid only: no dataset is downloadable here. The Sources page is a directory of the original sources "
     "behind each figure, each linked where it was published.",
     "أداة اكتشاف فقط: لا تتوفر هنا أي مجموعة بيانات للتنزيل. وصفحة المصادر فهرس للمصادر الأصلية التي يستند إليها كل رقم، "
     "وكل منها مرتبط بموضع نشره."),
    ("SEARCH-ALIAS-036", "issue; report an issue; problem", "مشكلة; الإبلاغ عن مشكلة; بلاغ",
     "route:/contact/ | route:/corrections/",
     "Discovery aid only: the control is named \"Report an error\".",
     "أداة اكتشاف فقط: اسم الزر هو «أبلغ عن خطأ»."),
    ("SEARCH-ALIAS-037", "access; access to services", "الوصول; الوصول إلى الخدمات", "route:/access/",
     "Discovery aid only: this is the evidence on where financial services can be reached, which is only partly "
     "mapped. For this resource's own accessibility statement, see /accessibility/.",
     "أداة اكتشاف فقط: هذه أدلة الوصول إلى الخدمات المالية، وهي شبكة غير ممسوحة بالكامل. أما بيان إتاحة الوصول الخاص "
     "بهذا المورد فهو في صفحة إتاحة الوصول."),
    ("SEARCH-ALIAS-038", "service providers; financial service providers",
     "مقدمو الخدمات; مقدمي الخدمات; مقدمو الخدمات المالية", "route:/providers/",
     "Discovery aid only: a listing or a licence does not establish operation.",
     "أداة اكتشاف فقط: الإدراج أو الترخيص لا يثبت التشغيل."),
]

# ---------------------------------------------------------------- 04 governed terminology register (new block)
REGISTER_TITLE = "Governed terminology register / سجل المصطلحات الخاضعة للحوكمة"
REGISTER_HEADER = ("term_id", "term_en", "term_ar", "definition_en", "definition_ar", "do_not_use", "rule")
REGISTER = [
    ("TERM-REMIT", "remittances", "الحوالات",
     "Money sent by a person to a person, and the corridors, methods, costs, channels and agents that carry it.",
     "المال الذي يرسله شخص إلى شخص، وما يحمله من ممرات وطرق وتكاليف وقنوات ووكلاء.",
     "التحويلات (as the generic word for remittances); تحويلات العاملين (a pre-BPM6 concept, source captions only)",
     "«الحوالات» names the operation. «التحويلات» stays for a published balance-of-payments or national-accounts "
     "series, aggregate, revision, vintage or scope, and «التحويلات الشخصية» only where the source's caption says "
     "personal transfers. Never substitute one for the other: «التحويلات النقدية» (cash transfers), «التحويلات "
     "الحكومية» (government transfers), «التحويلات الواردة» (a balance-of-payments series), «الحوالات النقدية "
     "الداخلية» (Governor's Decision (23) of 2024), «تحويل مصرفي» and any quoted source title or a source's own term "
     "are fixed. A changed concept name is a changed universe; no mechanical replacement is permitted."),
    ("TERM-CASH-TRANSFER", "cash transfers", "التحويلات النقدية",
     "Humanitarian or social assistance paid in cash or to an account.",
     "مساعدات إنسانية أو اجتماعية تُدفع نقدًا أو إلى حساب.",
     "الحوالات; remittances",
     "Never rendered as «الحوالات» and never called remittances in English: the payer is a programme, not a person."),
    ("TERM-LICENCE-REUSE", "licence (reuse)", "رخصة",
     "The copyright instrument under which content may be reused, here CC BY 4.0 for CauseWay's own content.",
     "الصك المتعلق بحقوق المؤلف الذي يُتاح المحتوى بموجبه، وهو هنا رخصة CC BY 4.0 لمحتوى CauseWay الخاص.",
     "ترخيص (for the reuse licence)",
     "«رخصة» is the reuse instrument. Regulatory licensing is «ترخيص» (TERM-LICENSING). The two senses are never "
     "interchanged: CauseWay is not a licensed financial institution and claims no such status "
     "(audit/OWNER_DECISIONS_2026-10-10.md)."),
    ("TERM-LICENSING", "licensing (regulatory)", "ترخيص",
     "The act and status of being licensed by a financial authority, as recorded by that authority on a date.",
     "واقعة الترخيص من جهة رقابية مالية وحالته، كما تسجلها تلك الجهة في تاريخ محدد.",
     "رخصة (for regulatory licensing)",
     "A licence or a listing does not establish operation (the semantic firewall). Never rendered «رخصة»."),
    ("TERM-SOURCES", "Sources", "المصادر",
     "The directory of the original sources behind the published evidence, each linked where it was published.",
     "فهرس المصادر الأصلية التي تستند إليها الأدلة المنشورة، وكل منها مرتبط بموضع نشره.",
     "Data & sources; البيانات والمصادر",
     "The page is named \"Sources / المصادر\" while nothing on it is downloadable. It becomes \"Sources and data / "
     "المصادر والبيانات\" only when a machine-readable file of the published evidence is downloadable from this site "
     "and reachable from that page (site-src/deployment.json public_downloads true) — not when an API exists, not "
     "when a third party hosts the data. SEARCH-ALIAS-035 keeps the retired words working."),
    ("TERM-QUESTIONS", "Key questions", "الأسئلة الرئيسية",
     "The hub of the governed entry questions, and the route into the eight domain answers.",
     "صفحة الأسئلة الخاضعة للحوكمة التي يبدأ منها القارئ، والمَدخل إلى أجوبة المجالات الثمانية.",
     "Explore; استكشف (as the hub's name); الأسئلة (bare, which reads as an FAQ)",
     "A hub is a noun phrase, not an imperative. \"Explore\" and «استكشف» keep their own strings where they are verbs "
     "(UI-DOM-EXPLORE-QUESTIONS, UI-DOM-UNDERSTAND-EXPLORE-VERIFY). SEARCH-ALIAS-034 keeps the retired word working."),
    ("TERM-MEASUREMENT-PRIORITY", "measurement priority", "أولوية القياس",
     "One named gap in the evidence that would change a decision if it were measured.",
     "فجوة مسماة في الأدلة، من شأن قياسها أن يغيّر قرارًا.",
     "Measurement Agenda; أجندة القياس",
     "The collection is \"Measurement priorities / أولويات القياس\" and one item is a \"measurement priority / أولوية "
     "القياس\". This resource names what is missing; it does not set national priorities and does not undertake the "
     "measurement."),
    ("TERM-EVIDENCE-READING", "Evidence Reading", "قراءة الأدلة",
     "One long-form reading of the published evidence, every statement of which rests on an Evidence Record.",
     "قراءة موسعة في الأدلة المنشورة، تستند كل مقولة فيها إلى سجل دليل.",
     "Analysis; التحليلات; تحليلات",
     "The collection is \"Evidence readings / قراءات الأدلة\"; one item's eyebrow is \"Reading / قراءة\". It is never "
     "called \"Analysis\" or «التحليلات»: «التحليلات» already names analytics on /privacy/, \"Analysis\" / «التحليل» "
     "already names a section role on 31 page sections, and the word would promise interpretation beyond the evidence."),
    ("TERM-RESOURCE-SELF", "this resource", "هذا المورد",
     "How the product refers to itself in prose.",
     "كيف يشير المنتج إلى نفسه في النص.",
     "عن المورد (as a menu label, where unvocalised «المورد» reads as *muwarrid*, a supplier)",
     "«هذا المورد» stays in prose. The About page's label is \"About / عن الموقع\"; a two-word menu label has none of "
     "the context a demonstrative inside a sentence has."),
    ("TERM-ACCESS", "Access", "الوصول إلى الخدمات المالية",
     "The observed geography of where financial services can be reached; it is only partly mapped.",
     "الجغرافيا المرصودة لمواضع إمكان الوصول إلى الخدمات المالية، وهي ممسوحة جزئيًا فقط.",
     "الوصول (bare)",
     "Bare «الوصول» is never a label: it collided with the chain label and with «إتاحة الوصول» (this resource's own "
     "accessibility statement). Access is not use (the semantic firewall); the label names the subject, and the page's "
     "own title states the limit."),
    ("TERM-PROVIDERS", "Providers", "مقدمو الخدمات المالية",
     "Banks, exchange companies, remittance agents and e-wallet services, as named in an authority's dated list.",
     "البنوك وشركات الصرافة ووكلاء الحوالات وخدمات المحافظ الإلكترونية، كما تسميها قائمة مؤرخة لجهة مختصة.",
     "مقدمو الخدمات (bare)",
     "The label names the category, never a status: a listing or a licence does not establish operation, and this "
     "resource confirms no entity's current licensed or operating status."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # 04 primary navigation
    for row, en_old, en_new, ar_old, ar_new, j_old, j_new in NAV_ROWS:
        if en_new is not None:
            s.set(F, S04, row, 2, en_new, en_old, f"04!nav{row}.label_en")
        if ar_new is not None:
            s.set(F, S04, row, 3, ar_new, ar_old, f"04!nav{row}.label_ar")
        s.set(F, S04, row, 4, j_new, j_old, f"04!nav{row}.route_or_group")

    # 04 route dictionary
    for row, en_old, en_new, ar_old, ar_new in SURFACES:
        if en_new is not None:
            s.set(F, S04, row, 3, en_new, en_old, f"04!route{row}.surface_en")
        if ar_new is not None:
            s.set(F, S04, row, 4, ar_new, ar_old, f"04!route{row}.surface_ar")

    # 04 trust navigation
    for row, en_old, en_new, ar_old, ar_new in TRUST:
        if en_new is not None:
            s.set(F, S04, row, 2, en_new, en_old, f"04!trust{row}.label_en")
        if ar_new is not None:
            s.set(F, S04, row, 3, ar_new, ar_old, f"04!trust{row}.label_ar")

    # 04 governed interface copy
    for ui_id, en_new, ar_new, en_old, ar_old in UI_SET:
        set_ui(s, F, ui_id, en_new, ar_new, en_old, ar_old)

    # 02 site map titles
    t02 = Table(s, S02, header_row=4)
    for route, en_old, en_new, ar_old, ar_new in TITLES:
        if en_new is not None:
            t02.set(F, route, "title_en", en_new, en_old)
        if ar_new is not None:
            t02.set(F, route, "title_ar", ar_new, ar_old)

    # 03 /data/ coverage list (English row only; the Arabic row already says أولويات القياس and قراءات الأدلة)
    g03 = s.grid(S03)
    rows03 = [i for i, r in enumerate(g03, 1)
              if r and r[0] == "/data/" and str(r[1]) == "8" and (r[4] or "").startswith("Public Evidence Records:")]
    if len(rows03) != 1:
        raise TxError(f"03: /data/ section 8 English body found {len(rows03)} times")
    s.set(F, S03, rows03[0], 5, COVERAGE_NEW, COVERAGE_OLD, "03!/data/.8.body_en")

    # 04 search aliases — appended to the end of the block
    g04 = s.grid(S04)
    ali = [i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("SEARCH-ALIAS-")]
    if not ali:
        raise TxError("04: no search-alias rows found")
    have = {g04[i - 1][0] for i in ali}
    for a in ALIASES:
        if a[0] in have:
            raise TxError(f"04: {a[0]} already exists")
    s.ed.insert_rows(S04, max(ali) + 1,
                     [{1: a[0], 2: a[1], 3: a[2], 4: a[3], 5: a[4], 6: a[5]} for a in ALIASES])
    for a in ALIASES:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S04), ("row", None), ("col", None), ("field", a[0]),
                                     ("old", None), ("new", a[1] + " || " + a[2] + " -> " + a[3])]))

    # 04 governed terminology register — a new block after the search aliases
    g04 = s.grid(S04)
    ali = [i for i, r in enumerate(g04, 1) if r and isinstance(r[0], str) and r[0].startswith("SEARCH-ALIAS-")]
    at = max(ali) + 1
    block = [{}, {1: REGISTER_TITLE}, {i + 1: h for i, h in enumerate(REGISTER_HEADER)}]
    block += [{i + 1: v for i, v in enumerate(r)} for r in REGISTER]
    s.ed.insert_rows(S04, at, block)
    for r in REGISTER:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S04), ("row", None), ("col", None), ("field", r[0]),
                                     ("old", None), ("new", r[1] + " || " + r[2])]))

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "PN-1"),
        ("summary", "Public naming and terminology (the owner's brief of 10 October 2026, Part B): navigation, trust "
                    "and footer labels, accessible names, the eight domain names, object-type names, search facets, "
                    "the 404, domain title prefixes, five search aliases and a governed terminology register. "
                    "English and Arabic together; language only."),
        ("items", OrderedDict([("nav_items", len(NAV_ROWS)), ("route_surfaces", len(SURFACES)),
                               ("trust_items", len(TRUST)), ("interface_labels", len(UI_SET)),
                               ("titles", len(TITLES)), ("page_section_bodies", 1),
                               ("search_aliases", len(ALIASES)), ("register_terms", len(REGISTER))])),
    ]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
