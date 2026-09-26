# -*- coding: utf-8 -*-
"""P1-C — adjudicated held additions (P1.6).

  python3 p1c_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir> <staged_dir>

Writes the staged Master plus three controlled files into <staged_dir>: presentation_priority.json (tier shifts for the new
domain sections), page_spec_design_intent.json and navigation_interaction.json (two new Evidence Record routes).
Lead dispositions: audit/pre_tranche_c/P1_6_HELD_ADDITIONS_ADJUDICATION.md.
"""
import copy, json, os, sys
from collections import OrderedDict
from ptc_lib import Session, TxError, ROOT, S03
from projection.master_reader import Workbook

S02, S06, S07 = "02_SITE_MAP", "06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS"


def header(wb, sheet, row=4):
    return {h: j + 1 for j, h in enumerate(wb.grid(sheet)[row - 1]) if h}


def row_of(grid, key, first=5):
    hits = [i for i, r in enumerate(grid, 1) if i >= first and r and r[0] == key]
    if len(hits) != 1:
        raise TxError(f"{key}: {len(hits)} rows")
    return hits[0]


# ============================================================ texts (EN/AR), adjudicated by the Lead
CLM010 = OrderedDict([
    ("title_en", "Wallet and subscriber counts require semantic reconciliation"),
    ("title_ar", "اختلاف أعداد المحافظ ومشتركيها يحتاج إلى مطابقة دلالية"),
    ("summary_en", "Official CBY-Aden publications report different wallet counts at different dates and in different contexts—7 in 2024 Q3, 9 in 2025 H1 and 8 licensed e-wallets in a September 2025 official statement. The same two payment reports give e-wallet subscriber counts of 414,631, 507,585 and 581,075 for the first three quarters of 2024 (2024 Q3 report) and 2,102,484 for 2025 H1 (H1 2025 infographic). Because definitions and reporting scope have not been reconciled across these publications, neither set is presented as a continuous trend, and subscribers are not unique people or active users."),
    ("summary_ar", "تورد وثائق رسمية للبنك المركزي اليمني – عدن أعدادًا مختلفة للمحافظ في تواريخ وسياقات مختلفة: 7 في الربع الثالث 2024، و9 في النصف الأول 2025، و8 محافظ إلكترونية مرخصة في بيان رسمي في سبتمبر 2025. ويورد تقريرا المدفوعات نفسهما أعداد مشتركي المحافظ الإلكترونية: 414,631 و507,585 و581,075 للأرباع الثلاثة الأولى من 2024 (تقرير الربع الثالث 2024)، و2,102,484 للنصف الأول من 2025 (إنفوغرافيك النصف الأول 2025). ولأن التعريفات ونطاق الإبلاغ لم تُطابَق بين هذه الإصدارات، لا تُعرض أيٌّ من المجموعتين كسلسلة اتجاه متصلة، والمشتركون ليسوا أشخاصًا فريدين ولا مستخدمين نشطين."),
    ("period_en", "CBY source observations in 2024 Q1–Q3 (subscribers), 2024 Q3, 2025 H1 and September 2025; later official context is retained separately."),
    ("period_ar", "مشاهدات من مصادر البنك المركزي للأرباع الثلاثة الأولى من 2024 (المشتركون)، والربع الثالث 2024، والنصف الأول 2025، وسبتمبر 2025؛ ويُحفظ أي سياق رسمي أحدث بصورة منفصلة."),
    ("universe_en", "Wallet/e-wallet provider counts and e-wallet subscriber counts as defined by each cited CBY source; the provider definition, subscriber definition and counting basis may differ by source."),
    ("universe_ar", "أعداد المحافظ أو مقدمي المحافظ الإلكترونية وأعداد مشتركي المحافظ الإلكترونية وفق تعريف كل مصدر من مصادر البنك المركزي؛ وقد يختلف تعريف مقدم الخدمة وتعريف المشترك وقاعدة العد بين المصادر."),
    ("method_en", "Cross-source semantic reconciliation: compare date, label, provider definition and counting basis before treating 7, 9 and 8 as a sequence. The same test applies before the 2024 subscriber quarters and the 2025 H1 subscriber count are read together."),
    ("method_ar", "مواءمة دلالية بين المصادر: تُقارن التواريخ والتسميات وتعريف مقدم الخدمة وقاعدة العد قبل التعامل مع القيم 7 و9 و8 كسلسلة زمنية. ويُطبق الاختبار نفسه قبل قراءة أرباع المشتركين في 2024 مع عدد المشتركين في النصف الأول 2025 معًا."),
    ("limitations_en", "Do not infer entry/exit events or net provider growth from 7→9→8. Do not join 581,075 (2024 Q3) and 2,102,484 (2025 H1) as growth, and do not treat subscribers as unique people or active users."),
    ("limitations_ar", "لا يجوز تفسير التسلسل 7→9→8 باعتباره دخولًا وخروجًا فعليًا لمقدمي خدمات أو صافي نمو في عددهم. ولا يجوز وصل 581,075 (الربع الثالث 2024) بـ2,102,484 (النصف الأول 2025) بوصفه نموًا، ولا معاملة المشتركين كأشخاص فريدين أو مستخدمين نشطين."),
    ("currentness_en", "The latest comparable wallet count stated in this claim is the September 2025 figure of 8 licensed e-wallets, and the latest subscriber count is 2,102,484 for 2025 H1. A later source does not extend either series unless its definition is shown to be comparable."),
    ("currentness_ar", "أحدث قيمة قابلة للمقارنة لعدد المحافظ في هذه الخلاصة هي 8 محافظ إلكترونية مرخصة في سبتمبر 2025، وأحدث عدد للمشتركين هو 2,102,484 للنصف الأول 2025. ولا تُمدد أي من السلسلتين بمصدر أحدث ما لم يثبت توافق تعريفه وقاعدة عده."),
])

XW005 = OrderedDict([
    ("summary_en", "The FMIIP 2030 target of 1,021 access points, set against a January 2025 project baseline of 817 under the same project definition, cannot be added to or directly compared with ATMs, POS terminals or agents unless the project's access-point taxonomy and deduplication rules are documented."),
    ("summary_ar", "لا يجوز جمع مستهدف FMIIP البالغ 1,021 نقطة وصول بحلول 2030، مقابل خط أساس للمشروع قدره 817 نقطة في يناير 2025 وفق التعريف نفسه، أو مقارنته مباشرة بأجهزة الصراف الآلي أو نقاط البيع أو الوكلاء ما لم تُوثق تصنيفات المشروع وقواعد إزالة الازدواج."),
    ("period_en", "January 2025 project baseline / 2030 project target; 2025 administrative context"),
    ("period_ar", "خط أساس المشروع في يناير 2025 / مستهدف المشروع 2030؛ سياق إداري 2025"),
    ("limitations_en", "No valid additive crosswalk is established. The 1,021 target is shown only with its 817 baseline, and no progress percentage is calculated."),
    ("limitations_ar", "لا توجد مطابقة صالحة تسمح بالجمع بين هذه المقاييس. ولا يُعرض مستهدف 1,021 إلا مع خط أساسه البالغ 817، ولا تُحسب نسبة للتقدم."),
    ("currentness_en", "Currentness is bounded to the January 2025 project baseline / 2030 project target; 2025 administrative context. Do not carry the value, status or interpretation beyond the latest comparable evidence available from a comparable source without a newer comparable observation."),
    ("currentness_ar", "تقتصر حداثة هذا الدليل على خط أساس المشروع في يناير 2025 / مستهدف المشروع 2030؛ سياق إداري 2025. ولا يجوز ترحيل القيمة أو الحالة أو التفسير إلى فترة لاحقة على أحدث دليل قابل للمقارنة من دون مشاهدة أحدث قابلة للمقارنة."),
])

FIRMS_EN = ("Among formal firms in the 2022 seven-governorate survey, 58.2% (191 of 328) reported a checking or savings account. Their working capital came mainly from internal sources: on average, 69.12% came from internal funds or retained earnings, 16.66% from money lenders, friends or relatives, 10.15% from advance payments by clients, 1.97% from non-bank financial institutions, 1.31% from supplier credit and 0.56% from banks. In a separate question on the financial intermediaries they use, 73.48% of responding formal firms named an exchange store or money exchanger and 24.39% a commercial bank; firms could name more than one, so these are not market shares. The evidence base does not hold the number of firms behind the working-capital averages or the intermediary question. Among the 217 informal firms surveyed, 80.18% had no bank account; that sample was drawn from activity and location lists rather than a national register. The formal-firm sample includes micro firms with fewer than five employees, and neither sample represents all Yemeni firms.")
FIRMS_AR = ("أفادت 58.2% من المنشآت الرسمية في مسح عام 2022 الذي شمل سبع محافظات (191 من أصل 328 منشأة) بأن لديها حسابًا جاريًا أو حساب ادخار. غير أن رأس مالها العامل اعتمد أساسًا على مصادر داخلية: ففي المتوسط جاء 69.12% منه من الأموال الذاتية أو الأرباح المحتجزة، و16.66% من المقرضين أو الأصدقاء أو الأقارب، و10.15% من دفعات مقدمة من العملاء، و1.97% من مؤسسات مالية غير مصرفية، و1.31% من ائتمان الموردين، و0.56% فقط من البنوك. وفي سؤال مستقل عن الوسطاء الماليين الذين تتعامل معهم، ذكرت 73.48% من المنشآت الرسمية المجيبة محلات الصرافة أو الصرافين، و24.39% البنوك التجارية؛ ولأن المنشأة كان بإمكانها ذكر أكثر من وسيط، فهذه النسب ليست حصصًا سوقية. ولا تتضمن قاعدة الأدلة عدد المنشآت التي تستند إليها متوسطات رأس المال العامل ولا عدد المجيبين عن سؤال الوسطاء. أما المنشآت غير الرسمية التي شملها المسح، وعددها 217 منشأة، فلم يكن لدى 80.18% منها حساب مصرفي، وقد سُحبت عينتها من قوائم للأنشطة والمواقع لا من سجل وطني. وتضم عينة المنشآت الرسمية منشآت صغرى يقل عدد العاملين فيها عن خمسة، ولا تمثل أيٌّ من العينتين جميع المنشآت في اليمن.")

CHANGE_TRIGGER_EN = None     # copied verbatim from an existing record (standard text)
CHANGE_TRIGGER_AR = None

CLM062 = OrderedDict([
    ("object_id", "CLM-062"), ("object_class", "CLAIM"), ("public_routes", "/firms/ | /evidence/"),
    ("title_en", "Formal firms in the 2022 survey: accounts were common, bank finance for working capital was not"),
    ("title_ar", "المنشآت الرسمية في مسح 2022: الحساب المصرفي شائع، أما تمويل البنوك لرأس المال العامل فنادر"),
    ("summary_en", FIRMS_EN), ("summary_ar", FIRMS_AR),
    ("definition_en", "Firm-level financial behaviour reported by a World Bank custom enterprise survey: account holding, average working-capital source shares, financial intermediaries used, and informal firms' account holding."),
    ("definition_ar", "سلوك مالي للمنشآت كما أورده مسح مخصص للمنشآت أجراه البنك الدولي: امتلاك الحساب، ومتوسط حصص مصادر رأس المال العامل، والوسطاء الماليون المستخدمون، وامتلاك المنشآت غير الرسمية للحسابات."),
    ("period_en", "2022 survey (September 2022); published 2024"), ("period_ar", "مسح 2022 (سبتمبر 2022)؛ نُشر في 2024"),
    ("universe_en", "Two separate samples in seven selected governorates: 328 formal enterprises (including micro firms with fewer than five employees) and 217 informal enterprises drawn from activity and location lists. Neither sample represents all Yemeni firms."),
    ("universe_ar", "عينتان منفصلتان في سبع محافظات مختارة: 328 منشأة رسمية (تشمل منشآت صغرى يقل عدد العاملين فيها عن خمسة)، و217 منشأة غير رسمية سُحبت عينتها من قوائم للأنشطة والمواقع. ولا تمثل أيٌّ من العينتين جميع المنشآت في اليمن."),
    ("method_en", "Source-reported survey tabulations (Annex III, Figures 104, 109, 110 and 114–115): an account share with its numerator and base; average working-capital source shares; a multiple-response question on intermediaries; an informal-firm account share with its base."),
    ("method_ar", "جداول مسحية كما أوردها المصدر (الملحق الثالث، الأشكال 104 و109 و110 و114–115): حصة امتلاك الحساب مع بسطها وقاعدتها، ومتوسط حصص مصادر رأس المال العامل، وسؤال متعدد الإجابات عن الوسطاء، وحصة امتلاك الحساب بين المنشآت غير الرسمية مع قاعدتها."),
    ("limitations_en", "The evidence base does not hold the number of firms behind the working-capital averages or the intermediary question. An average working-capital share is not a share of firms, and multiple-response percentages are not market shares. Holding an account does not show that a firm uses bank credit. The formal and informal samples use different frames: they must not be added together or compared with the 2013 survey. Firms are not people, so these shares must not be set beside the Findex account-ownership rate."),
    ("limitations_ar", "لا تتضمن قاعدة الأدلة عدد المنشآت التي تستند إليها متوسطات رأس المال العامل ولا عدد المجيبين عن سؤال الوسطاء. ومتوسط حصة رأس المال العامل ليس نسبة من المنشآت، ونسب الأسئلة متعددة الإجابات ليست حصصًا سوقية. وامتلاك المنشأة حسابًا لا يثبت أنها تستخدم الائتمان المصرفي. كما يختلف إطار العينتين الرسمية وغير الرسمية، فلا يجوز جمعهما ولا مقارنتهما بمسح 2013. والمنشآت ليست أفرادًا، فلا تُوضع هذه النسب بجانب نسبة امتلاك الحساب في Findex."),
    ("currentness_en", "Currentness is bounded to the 2022 survey (September 2022). Do not carry the value, status or interpretation beyond the latest comparable evidence available from a comparable source without a newer comparable observation."),
    ("currentness_ar", "تقتصر حداثة هذا الدليل على مسح 2022 (سبتمبر 2022). ولا يجوز ترحيل القيمة أو الحالة أو التفسير إلى فترة لاحقة على أحدث دليل قابل للمقارنة من دون مشاهدة أحدث قابلة للمقارنة."),
    ("source_dependencies", "SRC-WB-FSD-2024-001"), ("lineage_state", "BOUND_EXACT"),
])
CLM062_07 = OrderedDict([
    ("claim_id", "CLM-062"), ("theme", "Firms / access to finance"), ("claim_type", "BOUNDED_SURVEY_COMPARISON"),
    ("headline_en", CLM062["title_en"]), ("headline_ar", CLM062["title_ar"]), ("copy_en", FIRMS_EN), ("copy_ar", FIRMS_AR),
    ("evidence_badge", "PRIMARY_CUSTOM_SURVEY"), ("evidence_inputs", '["20_FIRM_FINANCE","FFM-001","FFM-008","FFM-009","FFM-011"]'),
    ("does_not_prove_en", CLM062["limitations_en"]), ("does_not_prove_ar", CLM062["limitations_ar"]),
    ("change_trigger_en", "A newer enterprise survey with comparable questions, the survey's response bases, or a source correction."),
    ("change_trigger_ar", "مسح أحدث للمنشآت بأسئلة قابلة للمقارنة، أو إتاحة قواعد الاستجابة في المسح، أو تصحيح للمصدر."),
    ("public_routes", '["/firms","/evidence"]'),
])

FMIIP_BASE = OrderedDict([
    ("object_id", "FMIIP-BASELINE-2025-01"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/reforms/ | /evidence/compare/"),
    ("title_en", "FMIIP project baselines for January 2025 count accounts, access points, merchants and agents — not people"),
    ("title_ar", "خطوط الأساس لمشروع FMIIP في يناير 2025 تعدّ الحسابات ونقاط الوصول والتجار والوكلاء، لا الأشخاص"),
    ("summary_en", "The results framework of the World Bank-financed Yemen Financial Market Infrastructure and Inclusion Project (FMIIP, P180708) records January 2025 baselines for its own project-defined indicators: 1,062,441 active bank accounts (200,898 of them owned by women), 375,252 active e-wallet accounts, 817 financial access points, 170 merchants accepting electronic payments and 65 agents of licensed financial institutions. These are project baselines that count accounts, access points, merchants and agents — not people."),
    ("summary_ar", "يسجل إطار نتائج مشروع البنية التحتية للأسواق والشمول المالي في اليمن (FMIIP، P180708) الممول من البنك الدولي خطوط أساس في يناير 2025 لمؤشراته المعرّفة داخل المشروع: 1,062,441 حسابًا مصرفيًا نشطًا (منها 200,898 حسابًا مملوكًا لنساء)، و375,252 حساب محفظة إلكترونية نشطًا، و817 نقطة وصول مالي، و170 تاجرًا يقبلون المدفوعات الإلكترونية، و65 وكيلًا لمؤسسات مالية مرخصة. وهذه خطوط أساس للمشروع تعدّ الحسابات ونقاط الوصول والتجار والوكلاء، لا الأشخاص."),
    ("definition_en", "Baseline values recorded in a project results framework for indicators the project itself defines; a baseline is the project's starting reference, not an independent measurement of the financial system."),
    ("definition_ar", "قيم خط الأساس المسجلة في إطار نتائج مشروع لمؤشرات يعرّفها المشروع نفسه؛ وخط الأساس نقطة انطلاق مرجعية للمشروع، لا قياس مستقل للنظام المالي."),
    ("period_en", "January 2025 (project baseline)"), ("period_ar", "يناير 2025 (خط أساس المشروع)"),
    ("universe_en", "Project-defined indicators of the FMIIP results framework. The definitions and reporting scope behind each baseline are the project's own and are not documented in the evidence base."),
    ("universe_ar", "مؤشرات يعرّفها إطار نتائج مشروع FMIIP. وتعريفات كل خط أساس ونطاق الإبلاغ الخاص به تعود إلى المشروع نفسه، ولا توثقها قاعدة الأدلة."),
    ("method_en", "Baseline values as reported in the project's results framework."), ("method_ar", "قيم خط الأساس كما يوردها إطار نتائج المشروع."),
    ("limitations_en", "Accounts are not unique people, and active e-wallet accounts are not subscribers unless a definition shows otherwise. Accounts classified by owner are not a count of women. Merchants are not POS terminals, and agents are not customers. These baselines have not been reconciled with the Central Bank's payment-report totals or with survey measures of account ownership, and they must not be divided by a population total."),
    ("limitations_ar", "الحسابات ليست أشخاصًا فريدين، وحسابات المحافظ النشطة ليست مرادفة لعدد المشتركين ما لم يثبت التعريف ذلك. والحسابات المصنفة بحسب ملكيتها ليست عددًا للنساء. والتجار ليسوا أجهزة نقاط بيع، والوكلاء ليسوا عملاء. ولم تُطابَق خطوط الأساس هذه مع مجاميع تقارير المدفوعات لدى البنك المركزي ولا مع قياسات امتلاك الحساب في المسوح، ولا يجوز قسمتها على عدد السكان."),
    ("currentness_en", "Currentness is bounded to January 2025 (project baseline). Do not carry the value, status or interpretation beyond the latest comparable evidence available from a comparable source without a newer comparable observation."),
    ("currentness_ar", "تقتصر حداثة هذا الدليل على يناير 2025 (خط أساس المشروع). ولا يجوز ترحيل القيمة أو الحالة أو التفسير إلى فترة لاحقة على أحدث دليل قابل للمقارنة من دون مشاهدة أحدث قابلة للمقارنة."),
    ("source_dependencies", "SRC-WB-FMIIP-P180708"), ("lineage_state", "BOUND_EXACT"),
])

# New sections: (finding, route, order, role_en, role_ar, heading_en, body_en, heading_ar, body_ar, tier)
SECTIONS = [
    ("P1-H01", "/payments/", 5, "Evidence", "الدليل",
     "E-wallet subscribers: figures from two reports that do not form one series",
     "The CBY-Aden payments report for the third quarter of 2024 gives e-wallet subscriber counts of 414,631 for Q1, 507,585 for Q2 and 581,075 for Q3. The first-half 2025 infographic reports 2,102,484 subscribers. The two publications' subscriber definitions and reporting scope have not been reconciled, so the 2025 figure is not joined to the 2024 quarters and the difference is not read as growth. A subscriber count is not a count of unique people or of active users, and neither publication measures how many adults use a wallet.",
     "مشتركو المحافظ الإلكترونية: أرقام من تقريرين لا تشكل سلسلة واحدة",
     "يورد تقرير المدفوعات الصادر عن البنك المركزي اليمني – عدن للربع الثالث من 2024 أعداد مشتركي المحافظ الإلكترونية: 414,631 في الربع الأول، و507,585 في الربع الثاني، و581,075 في الربع الثالث. أما إنفوغرافيك النصف الأول من 2025 فيورد 2,102,484 مشتركًا. ولم يُطابَق تعريف المشترك ولا نطاق الإبلاغ بين الإصدارين، لذلك لا يُوصل رقم 2025 بأرباع 2024، ولا يُقرأ الفرق بينهما نموًا. وعدد المشتركين ليس عددًا للأشخاص الفريدين ولا للمستخدمين النشطين، ولا يقيس أيٌّ من الإصدارين عدد البالغين الذين يستخدمون المحافظ.",
     "primary"),
    ("P1-H02", "/access/", 3, "Evidence", "الدليل",
     "Lists show who is registered, not where services operate",
     "Official lists document a substantial exchange and remittance provider presence relevant to the access question. The 2026 CBY-Aden roster lists 98 exchange companies, 225 individual exchange establishments and 106 remittance agents — three source categories, not a deduplicated count of firms — and the current CBY-Aden list of licensed banks names 26 banks. Listing or licensing is not operation, and later suspension or closure decisions are separate status events. Separately, the FMIIP results framework sets a January 2025 baseline of 817 financial access points against a 2030 target of 1,021, under a project definition that the evidence base does not document. None of these figures shows where services operate or how far people are from them.",
     "القوائم الرسمية تبيّن الجهات المسجلة، لا أماكن تقديم الخدمة",
     "توثق القوائم الرسمية حضورًا كبيرًا لمقدمي خدمات الصرافة والحوالات يتصل بسؤال الوصول: فقائمة البنك المركزي اليمني – عدن لعام 2026 تضم 98 شركة صرافة و225 منشأة صرافة فردية و106 وكلاء حوالات — وهي ثلاث فئات يحددها المصدر، لا عددًا لمنشآت فريدة بعد إزالة الازدواج — كما تضم قائمته الحالية للبنوك المرخصة 26 بنكًا. والإدراج أو الترخيص لا يعني التشغيل، وقرارات الإيقاف أو الإغلاق اللاحقة أحداث حالة منفصلة. وبصورة مستقلة، يحدد إطار نتائج مشروع FMIIP خط أساس قدره 817 نقطة وصول مالي في يناير 2025 مقابل مستهدف قدره 1,021 نقطة في 2030، وفق تعريف للمشروع لا توثقه قاعدة الأدلة. ولا يبين أي من هذه الأرقام أين تعمل الخدمات ولا مدى بُعد الناس عنها.",
     "primary"),
    ("P1-H03", "/firms/", 5, "Evidence", "الدليل",
     "Formal firms in this sample: most held a bank account, but banks financed almost none of their working capital",
     FIRMS_EN,
     "المنشآت الرسمية في هذه العينة: لدى أغلبها حساب مصرفي، لكن البنوك لم تموّل إلا جزءًا ضئيلًا جدًا من رأس مالها العامل",
     FIRMS_AR,
     "primary"),
    ("P1-H04", "/evidence/compare/", 2, "Analysis", "التحليل",
     "Three measures that cannot be combined",
     "Three kinds of figure are often set side by side. 11.9% is the share of adults (15+) in the survey's covered areas who had an account in the 2021 Global Findex wave, with fieldwork in 2022–2023. About 3.3 million is what a 2024 secondary source calls “active savers” in microfinance in 2023 — a count that has not been deduplicated into unique people. And 1,062,441 active bank accounts and 375,252 active e-wallet accounts are the FMIIP project's baselines for January 2025 — accounts, not people. These figures measure different things, for different populations and dates, from different kinds of evidence. They cannot be added, subtracted, ranked or converted into one another, and no population total is used here to turn the counts into shares. For these figures, “not comparable” is the correct result.",
     "ثلاثة مقاييس لا يصح الجمع بينها",
     "كثيرًا ما توضع ثلاثة أنواع من الأرقام جنبًا إلى جنب. فنسبة 11.9% هي حصة البالغين (15 سنة فأكثر) في المناطق التي غطاها المسح ممن كان لديهم حساب في موجة 2021 من المؤشر العالمي للشمول المالي (Findex)، التي نُفذ عملها الميداني خلال 2022–2023. ونحو 3.3 مليون هو ما يسميه مصدر ثانوي منشور في 2024 «مدخرين نشطين» في قطاع التمويل الأصغر في 2023، وهو عدد لم تُزَل منه الازدواجية، فلا يمثل أشخاصًا فريدين. أما 1,062,441 حسابًا مصرفيًا نشطًا و375,252 حساب محفظة إلكترونية نشطًا فهي خطوط الأساس لمشروع FMIIP في يناير 2025، أي حسابات لا أشخاص. وتقيس هذه الأرقام أشياء مختلفة، لمجتمعات وتواريخ مختلفة، ومن أنواع مختلفة من الأدلة؛ فلا يجوز جمعها أو طرحها أو ترتيبها أو تحويل بعضها إلى بعض، ولا يُستخدم هنا أي عدد للسكان لتحويل الأعداد إلى نسب. والنتيجة الصحيحة في هذه الحالة هي «غير قابلة للمقارنة».",
     None),
    ("P1-H05", "/methodology/", 7, "Analysis", "التحليل",
     "Uncertainty is stated, not manufactured",
     "Survey estimates carry sampling and coverage uncertainty. Where a source publishes a confidence interval or standard error, it is reported with the estimate. Where it does not, no interval, standard error or significance test is added unless it can be reproduced from the survey's own weights and design. A derived value, such as the difference between two percentages, keeps the precision of its inputs, with no added decimal places, and small differences between estimates are not read as a ranking.",
     "عدم اليقين يُبيَّن ولا يُصطنع",
     "تنطوي تقديرات المسوح على قدر من عدم اليقين مصدره المعاينة ونطاق التغطية. فإذا نشر المصدر فترة ثقة أو خطأً معياريًا عُرض مع التقدير، وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن إعادة احتسابها من أوزان المسح وتصميمه. وتحتفظ القيمة المشتقة، كالفرق بين نسبتين، بدقة مدخلاتها من دون منازل عشرية إضافية، ولا تُقرأ الفروق الطفيفة بين التقديرات على أنها ترتيب.",
     None),
]


def main():
    src, out, ledger, work, staged = sys.argv[1:6]
    os.makedirs(staged, exist_ok=True)
    s = Session(src, work)
    wb = Workbook(src)
    H06, H07, H02 = header(wb, S06), header(wb, S07), header(wb, S02)
    g06, g07, g02, g03 = wb.grid(S06), wb.grid(S07), wb.grid(S02), wb.grid(S03)

    def set06(finding, oid, field, new):
        r = row_of(g06, oid)
        s.set(finding, S06, r, H06[field], new, s.ed.get_value(S06, r, H06[field]), f"{oid}.{field}")

    def set07(finding, cid, field, new):
        r = row_of(g07, cid)
        s.set(finding, S07, r, H07[field], new, s.ed.get_value(S07, r, H07[field]), f"{cid}.{field}")

    # ---- PB-0521: CLM-010 carries the subscriber series with its break; bound to /payments/ and /providers/ (which states 7/9/8)
    for f, v in CLM010.items():
        set06("P1-H01", "CLM-010", f, v)
    set06("P1-H01", "CLM-010", "public_routes", "/evidence/compare/ | /payments/ | /providers/")
    set07("P1-H01", "CLM-010", "headline_en", CLM010["title_en"]); set07("P1-H01", "CLM-010", "headline_ar", CLM010["title_ar"])
    set07("P1-H01", "CLM-010", "copy_en", CLM010["summary_en"]); set07("P1-H01", "CLM-010", "copy_ar", CLM010["summary_ar"])
    set07("P1-H01", "CLM-010", "does_not_prove_en", CLM010["limitations_en"]); set07("P1-H01", "CLM-010", "does_not_prove_ar", CLM010["limitations_ar"])
    set07("P1-H01", "CLM-010", "evidence_inputs", '["11_CBY_PAYMENTS","PUC-WALLET-2025-01","POB-003","OBS-00014","OBS-00015","OBS-00016","OBS-00034"]')
    set07("P1-H01", "CLM-010", "public_routes", '["/evidence/compare","/payments","/providers"]')

    # ---- PB-0522: bind CLM-009 and CLM-008 to /access/; XW-FMIIP-005 shows the 1,021 target only with its 817 baseline
    for cid, r06, r07 in (("CLM-009", "/providers/ | /evidence/ | /access/", '["/providers", "/evidence", "/measurement", "/access"]'),
                          ("CLM-008", "/providers/ | /access/", '["/providers", "/access"]')):
        set06("P1-H02", cid, "public_routes", r06)
        set07("P1-H02", cid, "public_routes", r07)
    for f, v in XW005.items():
        set06("P1-H02", "XW-FMIIP-005", f, v)
    set06("P1-H02", "XW-FMIIP-005", "public_routes", "/reforms/ | /payments/ | /access/")
    set06("P1-H02", "XW-FMIIP-005", "source_dependencies", "SRC-UNDP-FMIIP-001; SRC-CBY-PAYREPORT-H1-2025; SRC-WB-FMIIP-P180708")
    links = json.loads(s.ed.get_value(S06, row_of(g06, "XW-FMIIP-005"), H06["source_links"]))
    links.append({"source_id": "SRC-WB-FMIIP-P180708", "url": "https://maps.worldbank.org/projects/wb/pid/P180708?status=active", "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"})
    set06("P1-H02", "XW-FMIIP-005", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")))

    # ---- PB-0345: CLM-001 is selectable in Compare
    set06("P1-H04", "CLM-001", "public_routes", "/people/ | / | /evidence/compare/")
    set07("P1-H04", "CLM-001", "public_routes", '["/people","/","/evidence/compare"]')

    # ---- new Evidence Records (06 rows appended; CLM-062 also in 07); standard text copied from an existing record
    tmpl = g06[row_of(g06, "CLM-060") - 1]
    std = {f: tmpl[H06[f] - 1] for f in ("change_trigger_en", "change_trigger_ar", "verification_en", "verification_ar")}
    fsd_url = "https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf"
    fm_url = "https://maps.worldbank.org/projects/wb/pid/P180708?status=active"
    nxt06 = len(g06) + 1
    for k, (rec, url) in enumerate(((CLM062, fsd_url), (FMIIP_BASE, fm_url))):
        row = nxt06 + k
        vals = OrderedDict(rec)
        vals.update(std)
        vals["source_links"] = json.dumps([{"source_id": rec["source_dependencies"], "url": url, "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}], separators=(",", ":"))
        for f, v in vals.items():
            s.set("P1-H03" if rec is CLM062 else "P1-H04", S06, row, H06[f], v, None, f"{rec['object_id']}.{f}")
    row07 = len(g07) + 1
    for f, v in CLM062_07.items():
        s.set("P1-H03", S07, row07, H07[f], v, None, f"CLM-062.{f}")

    # ---- 02 site-map rows for the two Evidence Record routes (full copy derived below, EXF-002)
    nxt02 = len(g02) + 1
    new_routes = []
    for k, rec in enumerate((CLM062, FMIIP_BASE)):
        route = f"/evidence/{rec['object_id']}/"
        new_routes.append((route, rec))
        for f, v in (("route", route), ("page_class", "evidence_detail"), ("template_route", "/evidence/[id]"), ("instance_id", rec["object_id"]),
                     ("title_en", rec["title_en"]), ("title_ar", rec["title_ar"])):
            s.set("P1-H0", S02, nxt02 + k, H02[f], v, None, f"{route}.{f}")

    # ---- 03 sections: detail pages (s1 summary, s2 standard reading guidance) and the five new route sections
    std2 = next(r for r in g03 if r and r[0] == "/evidence/CLM-060/" and r[1] == 2)
    nxt03 = len(g03) + 1
    rows03 = []
    for route, rec in new_routes:
        rows03.append({1: route, 2: 1, 5: rec["summary_en"], 7: rec["summary_ar"]})
        rows03.append({1: route, 2: 2, 3: std2[2], 4: std2[3], 5: std2[4], 6: std2[5], 7: std2[6]})
    shifts = []
    for f, route, order, ren, rar, hen, ben, har, bar, tier in SECTIONS:
        # later sections of the route move +1 (exact-value checked)
        for i, r in enumerate(g03, 1):
            if i > 4 and r and r[0] == route and r[1] not in (None, "") and int(float(r[1])) >= order:
                cur = s.ed.get_value(S03, i, 2)
                s.set(f, S03, i, 2, int(float(cur)) + 1, cur, f"{route}#s{r[1]}.section_order")
        shifts.append((route, order, tier))
        rows03.append({1: route, 2: order, 3: ren, 4: hen, 5: ben})
        rows03.append({1: route, 2: order, 3: rar, 6: har, 7: bar})
    for k, vals in enumerate(rows03):
        for col, v in vals.items():
            s.set("P1-H0", S03, nxt03 + k, col, v, None, f"{vals[1]}#s{vals[2]} new")
    s.regenerate_full_copy()

    # ---- controlled files: presentation tiers (domain routes), design intent and navigation contract (new routes)
    pp = json.load(open(os.path.join(ROOT, "site-src/content/presentation_priority.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    for route, order, tier in shifts:
        ent = next((r for r in pp["routes"] if r["route"] == route), None)
        if ent is None:
            continue                                      # not a Domain Answer page (compare, methodology render every section)
        for t in ("primary", "supporting", "progressive", "first_load_exclusions", "always_visible_boundaries"):
            for x in ent.get(t, []):
                if x.get("kind") == "section" and x["section_order"] >= order:
                    x["section_order"] += 1
        prim = ent["primary"]
        sec_idx = [j for j, x in enumerate(prim) if x.get("kind") == "section"]
        before = [j for j in sec_idx if prim[j]["section_order"] < order]
        pos = (before[-1] + 1) if before else 0
        prim.insert(pos, OrderedDict([("kind", "section"), ("section_order", order)]))
        for x in prim:                                    # the visual keeps following the same section
            if x.get("kind") == "visual":
                n_before = len([j for j in before])
                if x.get("after_primary", 2) > n_before:
                    x["after_primary"] = x.get("after_primary", 2) + 1
    for route, oid in (("/firms/", "CLM-062"), ("/payments/", "CLM-010"), ("/access/", "CLM-009")):
        ent = next(r for r in pp["routes"] if r["route"] == route)
        for x in ent["utility"]:
            if x.get("kind") == "verification_records" and oid not in x["object_ids"]:
                x["object_ids"].append(oid)                # the record behind the new section is one click from the page
    json.dump(pp, open(os.path.join(staged, "presentation_priority.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(staged, "presentation_priority.json"), "a").write("\n")

    di_path = os.path.join(ROOT, "scripts/projection/controlled_inputs/page_spec_design_intent.json")
    di = json.load(open(di_path, encoding="utf-8"), object_pairs_hook=OrderedDict)
    tmpl_di = di["routes"]["/evidence/CLM-060/"]
    for route, rec in new_routes:
        e = copy.deepcopy(tmpl_di)
        e["primary_user_question_internal"] = f"What exactly supports and limits “{rec['title_en']}”?"
        di["routes"][route] = e
    json.dump(di, open(os.path.join(staged, "page_spec_design_intent.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(staged, "page_spec_design_intent.json"), "a").write("\n")

    nav_path = os.path.join(ROOT, "site-src/content/content/navigation_interaction.json")
    nav = json.load(open(nav_path, encoding="utf-8"), object_pairs_hook=OrderedDict)
    tmpl_nav = next(r for r in nav["routes"] if r["route"] == "/evidence/CLM-060/")
    for route, rec in new_routes:
        e = copy.deepcopy(tmpl_nav)
        e["route"] = route
        e["stable_object_id"] = rec["object_id"]
        nav["routes"].append(e)
    json.dump(nav, open(os.path.join(staged, "navigation_interaction.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(staged, "navigation_interaction.json"), "a").write("\n")

    rep = s.save(out, ledger, [("transaction", "P1-C"), ("scope", "P1.6 held additions: PB-0521, PB-0522, PB-0345, PB-0520, PB-0614 applied as adjudicated; PB-0160/0161 and PB-0322 rejected"),
                               ("new_routes", [r for r, _ in new_routes])])
    print(f"P1-C staged: {rep['cells_written']} cells; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
