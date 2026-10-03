# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-17: the governed half of Owner Addendum 2's improvements that a sub-item audit found
not yet done (B16; the audit's table is summarised in audit/release_candidate/OPEN_ITEMS_DISPOSITION.md). English and
Arabic change together. The code half (the regulatory group's date order, its link from "Verify it yourself", the
whole-phrase search bonus, the Compare presets) ships in the same commit.

  python3 rc_17_addendum2.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Improvement 1, regulatory findability.
- document_type: the 2024 e-wallet circular (SRC-CBY-UNLICENSED-EWALLET-2024-001) is an instruction/circular, not a
  "provider-status instrument"; the 2025 e-money amendment (SRC-CBY-EMONEY-AMD-2025-001) is a regulatory decision, not
  an enforcement decision. Their public labels already said so.
- Search alias 002 ("decision" / «قرار») targets regulatory decisions, so Decision No. 23 of 2024 and Decision No. 4 of
  2025 rank above the fourteen enforcement decisions, which still match on their own words.
- /reforms/ names the instruments by number once, where it already describes them, from their governed titles: the
  e-money amendment (Governor's Decision No. 4 of 2025, section 4) and, in VIS-PAYMENT-RAILS, the 26 June 2024 decision
  on domestic transfers (Governor's Decision No. 23 of 2024; the record cites that source).
Improvement 2, entity and Arabic search: aliases Findex / «فيندكس» and PSP / «مزوّد خدمات الدفع»; alias 007's note says
  that «محفظة» means both an e-wallet and a loan portfolio, and names the two record families.
Improvement 5, Compare presets: one governed link label.
Improvement 9: a shorter /payments/ title (English 36 words → 28; Arabic 29), the same claim and the same scope boundary.
Improvement 10: the self-description counts of 00_MASTER and 37_READINESS_CHECKLIST, stale again (sources 160 → 165;
  payment observations 82 → 97), counted from the sheets themselves.
Improvement 11: "you need to resolve" / «تريد حسمها» twice in a row on Home and on Explore; the second becomes "in front
  of you" / «التي أمامك».
Lesson (Findex 2025): four 2021-wave records that discuss currency (CLM-025 and three indicator records) say that the
  Global Findex 2025 edition adds no newer Yemen observation, in the words VIS-FINDEX-ACCESS-USE already uses.

Owner decisions on the open escalations, 3 October 2026, 09:05 Cairo (audit/OWNER_DECISIONS_2026-10-02.md):
- Point 1: the public_use field of every status event says that entity names are non-public lineage and are not
  printed. The owner named PSE-006, -007, -010, -013 and -014. The same rule is applied to the events whose field
  allowed names conditionally (PSE-002…005, -008, -009), to PSE-012, and to PSE-001, the 2024 circular's list (point 2).
  The owner's aim is "so that no governed field allows an enforcement-decision entity name to be shown". RC-NAMES stays.
- Point 2: the twelve names of the 2024 e-wallet circular are withheld alike. NEG-EW-011 keeps its ID, route and counts;
  its summary, universe and method and its page description no longer carry the name, which stays in 22_PROVIDERS_DATA
  as non-public lineage. The search empty state gains one governed sentence (UI-JS-SEARCH-NAMES-NOTE). The validator's
  RC-NAMES now covers the circular's names, in every built file and the search index, with a negative control.

Folded from the two reviews (one bilingual, ACCEPTABLE with minor findings; one adversarial on the entity and regulatory
statements, NOT ACCEPTABLE), in this one rerun:
- No governed field allows a name (owner point 1, "so that no governed field allows an enforcement-decision entity name
  to be shown"): the public_claim_rule of the 30 enforcement-subject rows (PRV-EXCH-E001…E022 and branches B004A, B005A,
  B014A; PRV-REM-E001…E005) becomes the withholding rule E023…E025 already carry, and their note no longer lets a
  primary-controlled name be shown; the provider-status passport's display requirement shows the decision number, not
  the named entity; the status events' own text names each subject by entity ID, as PSE-015 does; PSE-011's public_use
  matches what its page prints. The citations name the owner note (03:10, point 1) and the decisions (09:05, point 1;
  point 2 for the circular's list).
- Related public text says the names are withheld: CLM-015's method and /providers/ section 6.
- VIS-PAYMENT-RAILS states the decision's scope as the signed scan reads it (Article 2(a)): exchange companies,
  exchange establishments and money-transfer agents, only through the unified network.
- The record ID NEG-EW-011 is the circular's own item number; with the circular linked, withholding the name does not
  withhold the identity. That follows from the owner's "same ID, same route" and goes back to the owner
  (design/ESCALATIONS.md, raised at RC-17).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, formula_of, set_formula_cache  # noqa: E402

UI_ROWS = [
    ("UI-JS-SEARCH-NAMES-NOTE",
     "Names of entities from the regulator's lists and enforcement decisions are not reproduced here; the original documents are linked from Data & sources.",
     "لا تُذكر هنا أسماء الجهات الواردة في قوائم الجهة الرقابية وقرارات الإنفاذ؛ ويمكن الوصول إلى الوثائق الأصلية من صفحة البيانات والمصادر.",
     "RC-17 (owner decisions of 3 October 2026, point 2). Search: the governed sentence under the empty result."),
    ("UI-COMPARE-PRESET-REMITTANCES", "Compare the CBY-Aden and IMF remittance records side by side",
     "قارن سجلات التحويلات لدى البنك المركزي اليمني – عدن وصندوق النقد الدولي جنبًا إلى جنب",
     "RC-17 (Owner Addendum 2, improvement 5; bilingual review). /remittances/ 'Verify it yourself': the preset CLM-032, CLM-037, CLM-041, which the page's cards do not all show, so the label names them."),
    ("UI-COMPARE-PRESET", "Compare these records side by side", "قارن هذه السجلات جنبًا إلى جنب",
     "RC-17 (Owner Addendum 2, improvement 5). A preset Compare link under a governed paragraph or a page's verify actions; the records are named in code (scripts/yfie)."),
]

DOC_TYPES = [("SRC-CBY-UNLICENSED-EWALLET-2024-001", "provider-status instrument", "instruction/circular"),
             ("SRC-CBY-EMONEY-AMD-2025-001", "decision/enforcement", "regulatory decision")]

ALIAS_002 = ("document_type:decision/enforcement | route:/providers/ | route:/reforms/",
             "document_type:regulatory decision | route:/reforms/ | route:/providers/")
ALIAS_007_NOTE = (
    "Discovery aid only: in Arabic «محفظة» means both an e-wallet and a loan portfolio. E-wallet records are under "
    "Payments; loan-portfolio records are under Finance (microfinance and banks).",
    "أداة اكتشاف فقط: قد تعني كلمة «محفظة» المحفظة الإلكترونية أو محفظة القروض. وسجلات المحافظ الإلكترونية في صفحة "
    "المدفوعات، أما سجلات محافظ القروض ففي صفحة التمويل (التمويل الأصغر والبنوك).")
NEW_ALIASES = [
    ("SEARCH-ALIAS-029", "Findex; Global Findex", "فيندكس; فندكس; Findex; المؤشر العالمي للشمول المالي", "route:/people/"),
    ("SEARCH-ALIAS-030", "PSP; PSPs; payment service provider; payment service providers",
     "مزود خدمات الدفع; مزودو خدمات الدفع; مزودي خدمات الدفع; مقدم خدمات الدفع; مقدمو خدمات الدفع; مقدمي خدمات الدفع", "document_type:regulation | route:/payments/"),
]

REFORMS_S4 = [
    ("en", "The signed 2025 mobile e-money amendment permits",
     "The signed mobile e-money amendment (Governor's Decision No. 4 of 2025) permits"),   # the year once, as in Arabic (RP-G06)
    ("ar", "يسمح تعديل النقود الإلكترونية عبر الهاتف المحمول الذي وُقِّع في 2025 بفئات",
     "يسمح تعديل النقود الإلكترونية عبر الهاتف المحمول، الصادر بقرار المحافظ رقم (4) لسنة 2025 والموقَّع في ذلك العام، بفئات"),
]
RAILS = [
    ("en", "a decision of the Central Bank of Yemen – Aden (CBY-Aden) requiring exchange companies and money-transfer agents "
           "to execute new domestic cash transfers through the unified",
     "Governor's Decision No. 23 of 2024, issued by the Central Bank of Yemen – Aden (CBY-Aden), requiring exchange companies, "
     "exchange establishments and money-transfer agents to execute new domestic cash transfers only through the unified"),
    ("ar", "قرار للبنك المركزي اليمني – عدن يُلزم شركات الصرافة ووكلاء الحوالات بتنفيذ الحوالات النقدية الداخلية الجديدة عبر الشبكة",
     "قرار المحافظ رقم (23) لسنة 2024 الصادر عن البنك المركزي اليمني – عدن، الذي يُلزم شركات ومنشآت الصرافة ووكلاء الحوالات "
     "بتنفيذ الحوالات النقدية الداخلية الجديدة حصرًا عبر الشبكة"),
]

PAYMENTS_TITLE_RC17 = (
    ("Payments: point-of-sale (POS) terminals reported by the Central Bank of Yemen – Aden rose from 561 to 1,651 between "
     "March 2025 and June 2026, within its reporting scope; how many people use them is not measured",
     "Payments: reported point-of-sale (POS) terminals rose from 561 to 1,651 between March 2025 and June 2026, within "
     "CBY-Aden's reporting scope; how many people use them is not measured"),
    ("المدفوعات: ارتفع عدد أجهزة نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 561 إلى 1,651 بين مارس 2025 "
     "ويونيو 2026، ضمن نطاق إبلاغه؛ أما عدد من يستخدمونها فغير مقيس",
     "المدفوعات: ارتفع عدد أجهزة نقاط البيع المُبلَّغ عنها من 561 إلى 1,651 بين مارس 2025 ويونيو 2026، ضمن نطاق إبلاغ "
     "البنك المركزي في عدن؛ أما عدد مستخدميها فغير مقيس"),
)

# Owner instructions of 3 October 2026, 09:50 Cairo (audit/OWNER_DECISIONS_2026-10-02.md) -----------------------------
# C2: the /payments/ headline (page title, og title, search title) is short and keeps the meaning; the full sentence
# stays as the lead, the first sentence of section 1.
PAYMENTS_TITLE = (
    (PAYMENTS_TITLE_RC17[0][0], "Payments: reported POS terminals rose between March 2025 and June 2026; how many people use them is not measured"),
    (PAYMENTS_TITLE_RC17[1][0], "المدفوعات: ارتفع عدد أجهزة نقاط البيع المُبلَّغ عنها بين مارس 2025 ويونيو 2026، أما عدد مستخدميها فغير مقيس"),
)
PAYMENTS_LEAD = [
    ("en", "Administrative payment data can show devices",
     "Point-of-sale (POS) terminals reported by the Central Bank of Yemen – Aden rose from 561 to 1,651 between March 2025 "
     "and June 2026, within its reporting scope; how many people use them is not measured. "),
    ("ar", "تستطيع البيانات الإدارية للمدفوعات",
     "ارتفع عدد أجهزة نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 561 إلى 1,651 بين مارس 2025 ويونيو 2026، "
     "ضمن نطاق إبلاغه؛ أما عدد من يستخدمونها فغير مقيس. و"),   # «وتستطيع…»: the paragraph continues (bilingual review)
]
# D: who publishes this — the owner's pair, byte-exact, in "CauseWay's role" before the funding paragraph (unchanged)
D_TRUTH = [("every record can be checked against its original source", "every record can be checked against the sources it names"),
           ("ويمكن التحقق من كل سجل بالرجوع إلى مصدره الأصلي", "ويمكن التحقق من كل سجل بالرجوع إلى المصادر التي يسمّيها")]
ABOUT_D = [
    ("en", "and for correcting errors.\n\nFunding.", "and for correcting errors.\n\n" + 'CauseWay is a Yemeni institutional advisory firm based in Aden (Commercial Registration No. 26666). It works with financial institutions, public institutions and development partners where finance, governance, regulation and implementation meet. Some of those institutions publish evidence used in this resource. That evidence is selected and presented by the method published here, and every record can be checked against its original source and corrected through the published route.' + "\n\nFunding."),
    ("ar", "وعن تصحيح الأخطاء.\n\nالتمويل:", "وعن تصحيح الأخطاء.\n\n" + 'CauseWay شركة استشارات مؤسسية يمنية مقرّها عدن (سجل تجاري رقم 26666)، تعمل مع المؤسسات المالية والمؤسسات العامة وشركاء التنمية حيث تلتقي المالية والحوكمة والتنظيم والتنفيذ. وتنشر بعض هذه المؤسسات أدلةً يستخدمها هذا المورد؛ وتُختار هذه الأدلة وتُعرض وفق المنهج المنشور هنا، ويمكن التحقق من كل سجل بالرجوع إلى مصدره الأصلي وتصحيحه عبر المسار المنشور.' + "\n\nالتمويل:"),
]
# E: the licence of CauseWay's own content, on /rights/ (first screen and a new last section) and pointed to from /terms/
RIGHTS_S1 = [
    ("en", "How source rights affect what this resource shows and what you may republish.",
     "CauseWay's own content in this resource is licensed under CC BY 4.0; material from other publishers stays under "
     "their terms. This page explains how both affect what this resource shows and what you may republish."),
    ("ar", "كيف تؤثر حقوق كل مصدر في ما يعرضه هذا المورد وفي ما يجوز لك إعادة نشره.",
     "يُتاح محتوى CauseWay الخاص في هذا المورد بموجب رخصة CC BY 4.0، وتبقى مواد الناشرين الآخرين خاضعة لشروطهم. "
     "وتوضح هذه الصفحة كيف يؤثر كلاهما في ما يعرضه هذا المورد وفي ما يجوز لك إعادة نشره."),
]
RIGHTS_LICENCE = {   # consolidated after the bilingual and hostile reviews
    "heading_en": "CauseWay's own content: CC BY 4.0",
    "heading_ar": "محتوى CauseWay الخاص: رخصة CC BY 4.0",
    "body_en": ("CauseWay licenses the content it owns in this resource under the Creative Commons Attribution 4.0 "
                "International licence (CC BY 4.0, https://creativecommons.org/licenses/by/4.0): its text, analysis and "
                "visual designs, the compiled evidence records, and the structure and annotations of the data exports when "
                "they are published. The CauseWay logo is not part of the licensed content. You may share and adapt that "
                "content for any purpose, provided you credit CauseWay, link to the licence and indicate whether you made "
                "changes. The licence does not cover third-party material: documents, data, tables, figures and text "
                "published by others remain under their publishers' terms, including where this resource reports them, "
                "and this resource does not host copies of their files. CauseWay asks that a reused figure be credited in "
                "two lines: first this resource (Yemen Financial Inclusion Evidence, the record, CauseWay, the edition and "
                "the page address), then the original source that the record names (publisher, title, year and link). This "
                "page states the licence CauseWay applies to its own content; it does not state that any third-party rights "
                "have been cleared."),
    "body_ar": ("تتيح CauseWay المحتوى الذي تملكه في هذا المورد بموجب رخصة المشاع الإبداعي «نَسب المُصنَّف 4.0 دولي» "
                "(CC BY 4.0، https://creativecommons.org/licenses/by/4.0): نصوصه وتحليلاته وتصاميمه المرئية، وسجلات الأدلة "
                "المجمَّعة، وبنية ملفات البيانات المُصدَّرة وشروحها عند نشرها. ولا يدخل شعار CauseWay في المحتوى المرخَّص. "
                "ويجوز لك مشاركة هذا المحتوى وتعديله لأي غرض، بشرط أن تنسبه إلى CauseWay، وأن تضع رابطًا إلى الرخصة، وأن تبيّن "
                "ما إذا كنت قد أجريت تغييرات. ولا تشمل الرخصة مواد الجهات الأخرى: فالوثائق والبيانات والجداول والرسوم والنصوص "
                "التي تنشرها جهات أخرى تبقى خاضعة لشروط ناشريها، بما في ذلك حين يوردها هذا المورد، ولا يستضيف هذا المورد نسخًا "
                "من ملفاتها. وتطلب CauseWay أن يُنسب الرقم المُعاد استخدامه في سطرين: أولًا هذا المورد (أدلة الشمول المالي في "
                "اليمن، والسجل، وCauseWay، والإصدار، ورابط الصفحة)، ثم المصدر الأصلي الذي يسمّيه السجل (الناشر، والعنوان، "
                "والسنة، والرابط). وتذكر هذه الصفحة الرخصة التي تطبقها CauseWay على محتواها الخاص، ولا تفيد بأن أي حقوق لجهات "
                "أخرى قد سُوّيت."),
}
TERMS_S5 = [   # one citation rule on /terms/ and /rights/ (hostile review)
    ("en", "Where CauseWay’s processing, calculation or synthesis materially shapes the result, cite the relevant evidence record or analytical reading as well.",
     "When you take a figure or a finding from this resource, also cite the evidence record, in the two-line form shown on Rights & reuse."),
    ("ar", "وعندما تكون معالجة CauseWay أو طريقة الاحتساب أو التجميع جزءًا جوهريًا من النتيجة، استشهد أيضًا بسجل الدليل أو القراءة التحليلية ذات الصلة.",
     "وعندما تأخذ رقمًا أو نتيجة من هذا المورد، استشهد أيضًا بسجل الدليل بصيغة السطرين المبيّنة في صفحة «الحقوق وإعادة الاستخدام»."),
]
TERMS_S3 = [
    ("en", "Source-specific restrictions continue to apply to underlying data, tables, figures and text.",
     "Source-specific restrictions continue to apply to underlying data, tables, figures and text. CauseWay's own content "
     "is licensed under CC BY 4.0; see Rights & reuse."),
    ("ar", "وتبقى القيود الخاصة بكل مصدر سارية على البيانات والجداول والرسوم والنصوص الأصلية.",
     "وتبقى القيود الخاصة بكل مصدر سارية على البيانات والجداول والرسوم والنصوص الأصلية. ويُتاح محتوى CauseWay الخاص "
     "بموجب رخصة CC BY 4.0؛ راجع صفحة «الحقوق وإعادة الاستخدام»."),
]
# B7: /privacy/ stays true at the public address on causewaygrp.com (one sentence, both languages)
PRIVACY_S4 = [
    ("en", "included in any choice or consent mechanism that applies.",
     "included in any choice or consent mechanism that applies. This resource sets no cookies; at its public address on "
     "causewaygrp.com, browsers may also send a cookie that the causewaygrp.com website sets for all its pages, and this "
     "resource does not read it."),
    ("ar", "وإدراجها في أي آلية للاختيار أو الموافقة تنطبق عليها.",
     "وإدراجها في أي آلية للاختيار أو الموافقة تنطبق عليها. ولا يضع هذا المورد أي ملف ارتباط؛ وفي عنوانه العام على "
     "causewaygrp.com قد ترسل المتصفحات أيضًا ملف ارتباط يضعه موقع causewaygrp.com لجميع صفحاته، ولا يقرؤه هذا المورد."),
]

RESOLVE = [  # (route, order, lang, old, new)
    ("/", 9, "en", "Choose the question closest to the decision or uncertainty you need to resolve.",
     "Choose the question closest to the decision or uncertainty in front of you."),
    ("/", 9, "ar", "ابدأ بالسؤال الأقرب إلى القرار أو المسألة التي تريد حسمها.",
     "اختر السؤال الأقرب إلى القرار أو المسألة التي أمامك."),
    ("/explore/", 5, "en", "Use the questions below to enter the evidence from the problem you need to resolve.",
     "Use the questions below to enter the evidence from the problem in front of you."),
    ("/explore/", 5, "ar", "استخدم الأسئلة أدناه للدخول إلى الأدلة من المسألة التي تريد حسمها.",
     "استخدم الأسئلة أدناه للدخول إلى الأدلة من المسألة التي أمامك."),
]

FINDEX_2025 = (" The Global Findex 2025 edition adds no newer Yemen observation.",
               " ولا تضيف نسخة Global Findex 2025 مشاهدة أحدث لليمن.")
FINDEX_2025_KEYS = ["CLM-025", "VIS-FINDEX-BARRIERS", "VIS-FINDEX-RESILIENCE", "VIS-FINDEX-FLOW-CHANNELS"]


PSE_RULE = ("The entity names are non-public lineage and are not printed (owner note of 3 October 2026, 03:10, point 1; "
            "owner decisions of 3 October 2026, 09:05, point 1).")
PSE_RULE_LIST = "The names are non-public lineage and are not printed (owner decisions of 3 October 2026, 09:05, point 2)."
PSE_PUBLIC_USE = {
    "PSE-001": "May show the dated list's source, date and count (12 wallets, entities or services). " + PSE_RULE_LIST,
    "PSE-002": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-003": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-004": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-005": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-006": "May show the dated branch-level event, decision number, class and action. " + PSE_RULE,
    "PSE-007": "May show the dated branch-level event, decision number, class and action. " + PSE_RULE,
    "PSE-008": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-009": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-010": "May show the dated branch-level event, decision number, class and action. " + PSE_RULE,
    "PSE-011": "May show the dated event, decision number, class, action and the district the decision names; the subject is "
               "an individual and is not named.",
    "PSE-013": "May show the dated event, decision number, class and action. " + PSE_RULE,
    "PSE-014": "May show the dated event, decision number, class and action. " + PSE_RULE,
}
PSE_012_ADD = " " + PSE_RULE

# adversarial review 3b: no governed field allows a name. The status events' own text names each subject by its entity
# ID, as PSE-015 already does (English-only lineage fields; none is printed: the matrix reads date, authority, class,
# state and source). Each old value is checked by its decision number, so no name is repeated here.
PSE_TEXT = {  # id: (decision guard, event_scope, normalized_event)
    "PSE-006": ("Decision No. 2 of 2026", "One exchange-company branch (PRV-EXCH-B004A; the name is non-public lineage)",
                "Governor Decision No. 2 of 2026 withdraws the licence of a non-compliant exchange-company branch (PRV-EXCH-B004A) based on Banking Supervision field-inspection reporting."),
    "PSE-007": ("Decision No. 3 of 2026", "One exchange-company branch (PRV-EXCH-B005A; the name is non-public lineage)",
                "Governor Decision No. 3 of 2026 withdraws the licence of an exchange-company branch (PRV-EXCH-B005A) based on Banking Supervision field-inspection reporting."),
    "PSE-010": ("Decision No. 6 of 2026", "One exchange-company branch — Al-Mahra (PRV-EXCH-B014A; the name is non-public lineage)",
                "Governor Decision No. 6 of 2026 suspends the licence of an exchange-company branch in Al-Mahra (PRV-EXCH-B014A) and closes its premises."),
    "PSE-012": ("Decision No. 10 of 2026", "One remittance agent — Shabwa/Habban (PRV-REM-E002; the name is non-public lineage)",
                "Governor Decision No. 10 of 2026 suspends the licence of a remittance agent in Shabwa/Habban (PRV-REM-E002) and closes the premises."),
    "PSE-013": ("Decision No. 11 of 2026", "One remittance agent — Lahj/Yafa Al-Hadd (PRV-REM-E003; the name is non-public lineage)",
                "Governor Decision No. 11 of 2026 suspends the licence of a remittance agent in Lahj/Yafa Al-Hadd (PRV-REM-E003) and closes the premises."),
    "PSE-014": ("Decision No. 17 of 2026", "One exchange and transfers company (PRV-EXCH-E022; the name is non-public lineage)",
                "Governor Decision No. 17 of 2026 suspends the licence granted to an exchange and transfers company (PRV-EXCH-E022) and closes its premises, based on violations recorded in a field-inspection report from Banking Supervision."),
}
PSE_014_NOT_PROVEN = ("a later status for ", "a later status for this company beyond the source date")
ENTITY_RULE = ("NON-PUBLIC LINEAGE ONLY (owner decisions of 3 October 2026, 09:05, point 1): the name is printed on no page, "
               "table, search record or social image. The public record shows the dated event, decision number, class and "
               "action only. ")
ENTITY_RULE_TAIL = {"default": "Do not imply that event-identified entities form the complete current provider universe.",
                    "PRV-EXCH-E022": "Do not infer the complete provider universe, other locations, products, activity or later status."}
ENTITY_NOTES = "Names are non-public lineage at every corroboration tier (owner decisions of 3 October 2026, 09:05, point 1)."
PASSPORT_DISPLAY = ("EP-CBY-PROVIDER-STATUS-2026",
                    "Show the decision date, named entity or branch type, action, annual-roster context and the fact that current operation requires entity-level reconciliation.",
                    "Show the decision date, decision number, entity class or branch type, and action, with the annual-roster context and the fact that current operation requires entity-level reconciliation. Entity names are non-public lineage and are not shown.")
CLM_015_METHOD = [
    ("en", "and recorded by name and date.", "and recorded by name and date in this resource's internal source records; they are not reproduced here."),
    ("ar", "وسُجلت بحسب الاسم والتاريخ.", "وسُجلت بحسب الاسم والتاريخ في سجل المصادر الداخلي لهذا المورد، ولا تُذكر هنا."),
]
PROVIDERS_S6 = [
    ("en", "are dated events for named entities and belong on each provider's status history.",
     "are dated events for specific entities. For the decisions it shows, which are a selection rather than a complete list, "
     "this resource records the date, decision number, entity class and action; the entity names stay in its internal source records."),
    ("ar", "أحداثًا مؤرخة تخص جهات مسماة وتُسجَّل ضمن سجل الوضع الخاص بكل جهة.",
     "أحداثًا مؤرخة تخص جهات بعينها. وللقرارات التي يعرضها، وهي مختارة وليست قائمة كاملة، يسجّل هذا المورد التاريخ ورقم القرار "
     "وفئة الجهة والإجراء، وتبقى أسماء الجهات في سجل المصادر الداخلي لهذا المورد."),
]

NEG_011 = {  # field: (must contain, new value)
    "summary_en": ("We Cash", "This wallet service is one of the 12 wallets, entities or services that a 26 June 2024 circular of the Central Bank of Yemen – Aden (CBY-Aden) names as unlicensed by CBY-Aden on that date, and with which banks and exchange businesses were told not to deal. Names from the regulator's lists are not reproduced here; the circular itself is linked from this record. The service's status under any other authority, and its status after that date, are not established here."),
    "summary_ar": ("وي كاش", "خدمة المحفظة هذه واحدة من 12 محفظة أو جهة أو خدمة يسمّيها تعميم للبنك المركزي اليمني – عدن بتاريخ 26 يونيو 2024 بوصفها غير مرخصة لديه في ذلك التاريخ، ويوجّه البنوك وشركات الصرافة إلى عدم التعامل معها. ولا تُذكر هنا أسماء الجهات الواردة في قوائم الجهة الرقابية، ويمكن الوصول إلى التعميم نفسه من هذا السجل. ولا يثبت هذا الدليل وضع الخدمة لدى أي سلطة أخرى، ولا وضعها بعد ذلك التاريخ."),
    "universe_en": ("this one", "One of the 12 wallets, entities or services the circular names; the name is not reproduced here."),
    "universe_ar": ("هذا الاسم", "واحدة من المحافظ أو الجهات أو الخدمات الـ12 التي يسمّيها التعميم؛ ولا يُذكر اسمها هنا."),
    "method_en": ("which names 12", "Taken from the text of the circular of the Central Bank of Yemen – Aden (CBY-Aden) dated 26 June 2024, which names 12 wallets, entities or services. The name is kept in this resource's internal source records and is not reproduced here."),
    "method_ar": ("الذي يسمّي 12", "مأخوذ من نص تعميم البنك المركزي اليمني – عدن المؤرخ في 26 يونيو 2024، الذي يسمّي 12 محفظة أو جهة أو خدمة. ويُحفظ الاسم في سجل المصادر الداخلي لهذا المورد ولا يُذكر هنا."),
}
NEG_011_META = {
    "en": ("We Cash", "One of 12 wallets, entities or services that a 26 June 2024 circular of the Central Bank of Yemen – Aden names as unlicensed on that date; the names are not reproduced here."),
    "ar": ("وي كاش", "واحدة من 12 محفظة أو جهة أو خدمة يسمّيها تعميم للبنك المركزي اليمني – عدن بتاريخ 26 يونيو 2024 بوصفها غير مرخصة في ذلك التاريخ؛ ولا تُذكر الأسماء هنا."),
}


def find_rows(g, pred):
    return [i for i, r in enumerate(g, 1) if r and pred(r)]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, "RC-17:IMP5", UI_ROWS)

    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    for sid, old, new in DOC_TYPES:
        t15.set("RC-17:IMP1", sid, "document_type", new, old)

    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    deps = str(t06.get("VIS-PAYMENT-RAILS", "source_dependencies") or "")
    if "SRC-CBY-DEC-23-2024-001" not in deps:
        raise TxError("RC-17:IMP1: VIS-PAYMENT-RAILS does not cite SRC-CBY-DEC-23-2024-001; the decision is not named")
    for lang, old, new in RAILS:
        s.replace("RC-17:IMP1", "06_EVIDENCE_OBJECTS", t06.rows["VIS-PAYMENT-RAILS"], t06.col(f"summary_{lang}"), old, new, f"VIS-PAYMENT-RAILS.summary_{lang}")
    t11 = Table(s, "11_VISUAL_LIBRARY", 4)
    n11 = 0
    for lang, old, new in RAILS:
        for field in [h for h in t11.head if h and h.endswith(f"_{lang}")]:
            if old in str(t11.get("VIS-PAYMENT-RAILS", field) or ""):
                s.replace("RC-17:IMP1", "11_VISUAL_LIBRARY", t11.rows["VIS-PAYMENT-RAILS"], t11.col(field), old, new, f"VIS-PAYMENT-RAILS.{field}")
                n11 += 1
    if n11 < 2:
        raise TxError(f"RC-17:IMP1: the 26 June 2024 rule text was found in {n11} visual-library fields, expected at least 2")
    for lang, old, new in REFORMS_S4:
        s.replace_section("RC-17:IMP1", "/reforms/", 4, lang, "body", old, new)

    t02 = Table(s, "02_SITE_MAP", 4)
    t02.set("RC-17:IMP9", "/payments/", "title_en", PAYMENTS_TITLE[0][1], PAYMENTS_TITLE[0][0])
    t02.set("RC-17:IMP9", "/payments/", "title_ar", PAYMENTS_TITLE[1][1], PAYMENTS_TITLE[1][0])

    for lang, must, lead in PAYMENTS_LEAD:
        row = s.section_row("/payments/", 1, lang)
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, {"en": 5, "ar": 7}[lang])
        if not isinstance(cur, str) or not cur.startswith(must):
            raise TxError(f"RC-17:OWN-C2: /payments/ section 1 ({lang}) does not open as expected")
        s.set("RC-17:OWN-C2", "03_PAGE_SECTIONS", row, {"en": 5, "ar": 7}[lang], lead + cur, cur, f"/payments/#s1.body_{lang}")   # AR: «و» + «تستطيع…»
    for lang, old, new in ABOUT_D:
        s.replace_section("RC-17:OWN-D", "/about/", 6, lang, "body", old, new)
    for (old, new), lang in zip(D_TRUTH, ("en", "ar")):   # hostile review: the one truth change to the owner's pair
        s.replace_section("RC-17:OWN-D-TRUTH", "/about/", 6, lang, "body", old, new)
    for lang, old, new in TERMS_S5:
        s.replace_section("RC-17:OWN-E", "/terms/", 5, lang, "body", old, new)
    for lang, old, new in RIGHTS_S1:
        s.set_section("RC-17:OWN-E", "/rights/", 1, lang, "body", new, old)
    for lang, old, new in TERMS_S3:
        s.replace_section("RC-17:OWN-E", "/terms/", 3, lang, "body", old, new)
    for lang, old, new in PRIVACY_S4:
        s.replace_section("RC-17:OWN-B7", "/privacy/", 4, lang, "body", old, new)
    g03 = s.grid("03_PAGE_SECTIONS")
    orders = sorted(int(float(r[1])) for r in g03[4:] if r and r[0] == "/rights/" and r[1] not in (None, ""))
    if orders != [1, 2, 3, 4, 5]:
        raise TxError(f"RC-17:OWN-E: /rights/ has sections {orders}, expected 1-5")
    new_row = max(i for i, r in enumerate(g03, 1) if any(c not in (None, "") for c in r)) + 1
    for col, val in ((1, "/rights/"), (2, 6), (4, RIGHTS_LICENCE["heading_en"]), (5, RIGHTS_LICENCE["body_en"]),
                     (6, RIGHTS_LICENCE["heading_ar"]), (7, RIGHTS_LICENCE["body_ar"])):
        s.ed.set_cell("03_PAGE_SECTIONS", new_row, col, val, expect=None)
    s.ledger.append(OrderedDict([("finding", "RC-17:OWN-E"), ("sheet", "03_PAGE_SECTIONS"), ("row", new_row), ("col", None),
                                 ("field", "/rights/#s6"), ("old", None),
                                 ("new", " || ".join(RIGHTS_LICENCE[k] for k in ("heading_en", "body_en", "heading_ar", "body_ar")))]))
    for route, order, lang, old, new in RESOLVE:
        s.replace_section("RC-17:IMP11", route, order, lang, "body", old, new)

    for key in FINDEX_2025_KEYS:
        for lang, add in (("en", FINDEX_2025[0]), ("ar", FINDEX_2025[1])):
            cur = t06.get(key, f"currentness_{lang}")
            if not isinstance(cur, str) or "2025" in cur:
                raise TxError(f"RC-17:LESSON: {key}.currentness_{lang} is empty or already mentions 2025")
            t06.set("RC-17:LESSON", key, f"currentness_{lang}", cur.rstrip() + add, cur)

    # owner decisions of 3 October 2026, point 1 (and point 2 for PSE-001): every status event withholds entity names
    g22 = s.grid("22_PROVIDERS_DATA")
    hr = [i for i, r in enumerate(g22, 1) if r and r[0] == "status_event_id"]
    if len(hr) != 1:
        raise TxError("RC-17:OWN-1: status-event header not found once")
    tse = Table(s, "22_PROVIDERS_DATA", hr[0])
    for pse, new in PSE_PUBLIC_USE.items():
        t_old = tse.get(pse, "public_use")
        if not isinstance(t_old, str) or "non-public lineage" in t_old or (pse == "PSE-011" and "is not named" not in t_old):
            raise TxError(f"RC-17:OWN-1: {pse}.public_use is empty or already withholds names")
        tse.set("RC-17:OWN-1", pse, "public_use", new, t_old)
    cur = tse.get("PSE-012", "public_use")
    tse.set("RC-17:OWN-1", "PSE-012", "public_use", cur.rstrip() + PSE_012_ADD, cur)
    # point 2: NEG-EW-011 without the name, in both languages
    for field, (must, new) in NEG_011.items():
        cur = t06.get("NEG-EW-011", field)
        if not isinstance(cur, str) or must not in cur:
            raise TxError(f"RC-17:OWN-2: NEG-EW-011.{field} does not hold the expected text")
        t06.set("RC-17:OWN-2", "NEG-EW-011", field, new, cur)
    for lang, (must, new) in NEG_011_META.items():
        cur = t02.get("/evidence/NEG-EW-011/", f"meta_description_{lang}")
        if not isinstance(cur, str) or must not in cur:
            raise TxError(f"RC-17:OWN-2: NEG-EW-011 meta_description_{lang} does not hold the expected text")
        t02.set("RC-17:OWN-2", "/evidence/NEG-EW-011/", f"meta_description_{lang}", new, cur)
    # adversarial review 3b and 3c: no governed field allows a name; related public text says the names are withheld
    for pse, (guard, scope, norm) in PSE_TEXT.items():
        cur_n = tse.get(pse, "normalized_event")
        if not isinstance(cur_n, str) or guard not in cur_n or "PRV-" in cur_n:
            raise TxError(f"RC-17:REV-3b: {pse}.normalized_event is not the expected {guard} text")
        tse.set("RC-17:REV-3b", pse, "normalized_event", norm, cur_n)
        tse.set("RC-17:REV-3b", pse, "event_scope", scope, tse.get(pse, "event_scope"))
    cur = tse.get("PSE-014", "not_proven")
    m = cur.split(PSE_014_NOT_PROVEN[0], 1)
    if len(m) != 2 or " beyond the source date" not in m[1]:
        raise TxError("RC-17:REV-3b: PSE-014.not_proven does not hold the expected text")
    tse.set("RC-17:REV-3b", "PSE-014", "not_proven", m[0] + PSE_014_NOT_PROVEN[1] + m[1].split(" beyond the source date", 1)[1], cur)
    tent = Table(s, "22_PROVIDERS_DATA", 4)
    n_ent = 0
    for eid in list(tent.rows):
        if not (isinstance(eid, str) and (eid.startswith("PRV-EXCH-") or eid.startswith("PRV-REM-"))):
            continue
        rule = str(tent.get(eid, "public_claim_rule") or "")
        if rule.startswith("NON-PUBLIC LINEAGE ONLY"):
            continue
        if not rule.startswith("May describe the "):
            raise TxError(f"RC-17:REV-3b: {eid}.public_claim_rule is not the expected permission")
        tent.set("RC-17:REV-3b", eid, "public_claim_rule", ENTITY_RULE + ENTITY_RULE_TAIL.get(eid, ENTITY_RULE_TAIL["default"]), rule)
        note = tent.get(eid, "notes")
        if note == "Names with non-primary corroboration remain non-public until primary decision content is controlled.":
            tent.set("RC-17:REV-3b", eid, "notes", ENTITY_NOTES, note)
        n_ent += 1
    if n_ent != 30:
        raise TxError(f"RC-17:REV-3b: rewrote {n_ent} enforcement-subject rules, expected 30 (PRV-*-E001…E022 and branches)")
    tpp = Table(s, "34_EVIDENCE_PASSPORTS", 4)
    tpp.set("RC-17:REV-3b", PASSPORT_DISPLAY[0], "display_requirements", PASSPORT_DISPLAY[2], PASSPORT_DISPLAY[1])
    for lang, old, new in CLM_015_METHOD:
        cur = t06.get("CLM-015", f"method_{lang}")
        if not isinstance(cur, str) or old not in cur:
            raise TxError(f"RC-17:REV-3c: CLM-015.method_{lang} does not hold the expected text")
        t06.set("RC-17:REV-3c", "CLM-015", f"method_{lang}", cur.replace(old, new), cur)
    for lang, old, new in PROVIDERS_S6:
        s.replace_section("RC-17:REV-3c", "/providers/", 6, lang, "body", old, new)

    # improvement 10: the self-description counts, counted from the sheets
    n_src = len([r for r in s.grid("15_SOURCE_LIBRARY")[4:] if r and isinstance(r[0], str) and r[0].startswith("SRC-")])
    g19 = s.grid("19_PAYMENTS_DATA")
    n_pay = len([r for r in g19[4:] if r and r[0] not in (None, "") and not str(r[0]).startswith(("payment_", "observation_id"))])
    for sheet, row_label_col, label, new in (("00_MASTER", 1, "Sources", n_src), ("37_READINESS_CHECKLIST", 2, "Source records", n_src),
                                             ("37_READINESS_CHECKLIST", 2, "Payment observations", n_pay)):
        g = s.grid(sheet)
        rows = find_rows(g, lambda r: len(r) >= row_label_col and r[row_label_col - 1] == label)
        if len(rows) != 1:
            raise TxError(f"RC-17:IMP10: {sheet} row {label!r} found {len(rows)} times")
        row = rows[0]
        for col in ((2, 3) if sheet == "00_MASTER" else (3, 4)):
            f = formula_of(s, sheet, row, col)
            if f:
                set_formula_cache(s, "RC-17:IMP10", sheet, row, col, new, g[row - 1][col - 1], f, f"{label}.c{col}")
            else:
                cur = s.ed.get_value(sheet, row, col)   # the stored value, as stored (a number or its text)
                if str(cur).strip() not in ("160", "82"):
                    raise TxError(f"RC-17:IMP10: {sheet}!r{row}c{col} holds {cur!r}, expected the stale count")
                s.set("RC-17:IMP10", sheet, row, col, int(new), cur, f"{label}.c{col}")   # a number stays a number (bilingual review)

    # search aliases (04, titled block "Search aliases"), found by its header after the interface rows were inserted
    g = s.grid("04_NAV_UX")
    hdr = [i for i, r in enumerate(g, 1) if r and r[0] == "alias_id"]
    if len(hdr) != 1:
        raise TxError("RC-17:IMP2: alias header not found once")
    ta = Table(s, "04_NAV_UX", hdr[0])
    ta.set("RC-17:IMP1", "SEARCH-ALIAS-002", "targets", ALIAS_002[1], ALIAS_002[0])
    ta.set("RC-17:IMP2", "SEARCH-ALIAS-007", "boundary_note_en", ALIAS_007_NOTE[0], None)
    ta.set("RC-17:IMP2", "SEARCH-ALIAS-007", "boundary_note_ar", ALIAS_007_NOTE[1], None)
    last = max(ta.rows.values())
    if list(ta.rows)[-1] != "SEARCH-ALIAS-028":
        raise TxError("RC-17:IMP2: the alias block does not end at SEARCH-ALIAS-028")
    s.ed.insert_rows("04_NAV_UX", last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in NEW_ALIASES])
    for a, b, c, d in NEW_ALIASES:
        s.ledger.append(OrderedDict([("finding", "RC-17:IMP2"), ("sheet", "04_NAV_UX"), ("row", None), ("col", None), ("field", a),
                                     ("old", None), ("new", f"{b} || {c} || {d}")]))

    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-17"), ("summary", "Owner Addendum 2 improvements: governed half"),
                                           ("items", OrderedDict([("doc_types", len(DOC_TYPES)), ("aliases_new", len(NEW_ALIASES)),
                                                                  ("sources_counted", n_src), ("payment_observations_counted", n_pay)]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}), n_src, n_pay)


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
