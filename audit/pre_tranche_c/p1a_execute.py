# -*- coding: utf-8 -*-
"""P1-A — public inventory tokens (P1.2), counts and identifiers in public copy (P1.2/P1.4), flattened evidence-card
bodies on /people/, /firms/ and /finance/ (P1.3).

  python3 p1a_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Findings: audit/pre_tranche_c/FINDINGS_LEDGER.csv (P1-F01 ... P1-F06).
"""
import sys
from ptc_lib import Session

# ---------------------------------------------------------------- P1.2: /data/ inventory (label-value lines; counts derived)
DATA_INV_EN = "\n".join([
    "Public Evidence Records: {{n:evidence_records}}",
    "Documented chronology events: {{n:chronology_events}}",
    "Public claims (each is also an Evidence Record): {{n:public_claims}}",
    "Registered source records: {{n:sources}}",
    "Source records with a public original locator: {{n:public_locators}}",
    "Curated source and report cards: {{n:curated_resources}}",
    "Evidence Readings: {{n:readings}}",
    "Measurement Agenda priorities: {{n:measurement_priorities}}",
])
DATA_INV_AR = "\n".join([
    "سجلات الأدلة العامة: {{n:evidence_records}}",
    "أحداث السلسلة الزمنية الموثقة: {{n:chronology_events}}",
    "الخلاصات العامة (وكل منها سجل دليل أيضًا): {{n:public_claims}}",
    "سجلات المصادر المسجلة: {{n:sources}}",
    "سجلات المصادر التي لها رابط أصلي عام: {{n:public_locators}}",
    "بطاقات المصادر والتقارير المنتقاة: {{n:curated_resources}}",
    "قراءات الأدلة: {{n:readings}}",
    "أولويات أجندة القياس: {{n:measurement_priorities}}",
])

# ---------------------------------------------------------------- P1.3: flattened evidence cards -> one authored narrative
# (finding, route, order, lang, must_start, new body)
CARDS = [
    # /people/
    ("P1-F03", "/people/", 2, "en", "Global Findex 2021 reports 11.9% account ownership",
     "Global Findex 2021 reports 11.9% account ownership for Yemen; the Yemen fieldwork was carried out in 2022–23. The value is a survey measure for that wave and fieldwork period, not a 2026 population rate."),
    ("P1-F03", "/people/", 2, "ar", "تسجل موجة Global Findex 2021 لليمن",
     "تسجل موجة Global Findex 2021 لليمن امتلاك حساب بنسبة 11.9%، مع تنفيذ العمل الميداني في اليمن خلال 2022–2023. هذا قياس مسحي لتلك الموجة والفترة، وليس نسبة سكانية لعام 2026."),
    ("P1-F03", "/people/", 3, "en", "In the same wave, 5.44% of women",
     "In the same wave, 5.44% of women and 18.35% of men have an account — a difference of 12.91 percentage points. Adults in the richest 60% by household income (15.5%) and in the poorest 40% (6.5%) differ by about 9.0 percentage points. Among adults with primary education or less, 6.98% have an account; the matching figure for adults with more education is not in the evidence base, so no education gap is stated. Because each comparison is within one survey wave, the disparities can be described; their causes cannot be established from these differences alone, and they are not 2026 estimates."),
    ("P1-F03", "/people/", 3, "ar", "في الموجة نفسها تملك 5.44% من النساء",
     "في الموجة نفسها تملك 5.44% من النساء و18.35% من الرجال حسابًا، بفارق 12.91 نقطة مئوية. ويبلغ الفارق بين البالغين في أغنى 60% بحسب دخل الأسرة (15.5%) وفي أفقر 40% (6.5%) نحو 9.0 نقاط مئوية. وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، بينما لا تتضمن قاعدة الأدلة الرقم المقابل لمن تلقوا تعليمًا أعلى، ولذلك لا تُذكر فجوة بحسب التعليم. وهذه مقارنات داخل موجة مسح واحدة: يمكن وصف الفروق، لكن لا يمكن استنتاج أسبابها منها وحدها، ولا تمثل تقديرات لعام 2026."),
    ("P1-F03", "/people/", 5, "en", "Selected survey anchors can be shown",
     "Official World Bank evidence gives three survey anchors: a 2011 comparator of 3.7% for accounts at a financial institution, a 2014 account headline of 6.4%, and 11.9% in the latest verified wave (Global Findex 2021, with Yemen fieldwork in 2022–23). The years between them are not observed, and the concepts are not assumed to be identical across waves, so this resource does not interpolate an annual trend."),
    ("P1-F03", "/people/", 5, "ar", "يمكن عرض نقاط رصد مختارة",
     "تقدم أدلة البنك الدولي الرسمية ثلاث نقاط رصد مسحية: نقطة مقارنة لعام 2011 لامتلاك حساب لدى مؤسسة مالية بنسبة 3.7%، ونسبة إجمالية لامتلاك الحساب بلغت 6.4% في 2014، ونسبة 11.9% في أحدث موجة متحقق منها (Global Findex 2021، مع تنفيذ العمل الميداني في اليمن خلال 2022–2023). والسنوات الواقعة بينها غير مقاسة، ولا يُفترض أن المفاهيم متطابقة بين الموجات؛ لذلك لا يُنشئ هذا الموقع اتجاهًا سنويًا بين هذه النقاط."),
    ("P1-F03", "/people/", 6, "en", "In the 2014 evidence, 65.9% of adults",
     "In the 2014 World Bank weighted country profile, 65.9% of adults reported borrowing any money, including 51.7% from family or friends, 15.0% from a private informal lender and 0.4% from a financial institution. Separately, 20.6% reported saving any money, including 0.9% at a financial institution and 4.5% through a savings club or a person outside the family. The categories are not additive, and each percentage applies to the all-adult base used by that question."),
    ("P1-F03", "/people/", 6, "ar", "في أدلة 2014، أفاد 65.9% من البالغين",
     "في الملف القطري الموزون للبنك الدولي لعام 2014، أفاد 65.9% من البالغين بأنهم اقترضوا أي مبلغ، منهم 51.7% من الأسرة أو الأصدقاء، و15.0% من مقرض خاص غير رسمي، و0.4% من مؤسسة مالية. وبشكل منفصل، أفاد 20.6% بأنهم ادخروا أي مبلغ، منهم 0.9% لدى مؤسسة مالية و4.5% عبر جمعية ادخار أو شخص من خارج الأسرة. وهذه الفئات غير قابلة للجمع، وكل نسبة تنطبق على قاعدة جميع البالغين المستخدمة في السؤال المعني."),
    ("P1-F03", "/people/", 7, "en", "In 2014, 18.3% of adults reported receiving",
     "In the 2014 World Bank weighted country profile, 18.3% of adults reported receiving domestic remittances. Among recipients, 31.1% received them through a money-transfer operator, 2.0% through a financial institution and 0.0% through a mobile phone. The base changes from all adults to remittance recipients, so the channel percentages cannot be read on the same base as the 18.3% receipt rate."),
    ("P1-F03", "/people/", 7, "ar", "في 2014، أفاد 18.3% من البالغين",
     "في الملف القطري الموزون للبنك الدولي لعام 2014، أفاد 18.3% من البالغين بتلقي حوالات محلية. ومن بين المتلقين، تلقاها 31.1% عبر شركة تحويل أموال، و2.0% عبر مؤسسة مالية، و0.0% عبر الهاتف المحمول. وهنا تتغير قاعدة الاحتساب من جميع البالغين إلى متلقي الحوالات، لذلك لا يجوز قراءة نسب القنوات على القاعدة نفسها لنسبة التلقي البالغة 18.3%."),
    ("P1-F03", "/people/", 8, "en", "The latest Yemen Findex wave excludes",
     "The latest Yemen Findex wave excludes Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several districts elsewhere; the source states that excluded areas represent approximately 23% of the population and that over one-fourth of primary sampling units were replaced during fieldwork. The Yemen sample has 1,000 respondents, interviewed between 7 November 2022 and 9 January 2023, and population estimates require the survey weights."),
    ("P1-F03", "/people/", 8, "ar", "تستبعد أحدث موجة للمؤشر العالمي في اليمن",
     "تستبعد أحدث موجة للمؤشر العالمي في اليمن محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى. ويذكر المصدر أن المناطق المستبعدة تمثل نحو 23% من السكان، وأن أكثر من ربع وحدات المعاينة الأولية استُبدل أثناء العمل الميداني. وتضم عينة اليمن 1,000 مستجيب أُجريت المقابلات معهم بين 7 نوفمبر 2022 و9 يناير 2023، وتتطلب تقديرات السكان استخدام أوزان المسح."),
    ("P1-F03", "/people/", 9, "en", "CBY Global Money Week records show programme activity",
     "CBY Global Money Week records show programme activity during 2023–2025. Activity, documented output or completion, population-level capability measurement and evaluated programme outcome are four different levels of evidence: taking part in an activity does not by itself establish improved capability or impact, and programme effectiveness cannot be claimed without evaluation evidence that has a baseline and an endline. Population capability measures, such as the OECD/INFE scores, are a different kind of evidence, and this resource does not attribute them to these activities."),
    ("P1-F03", "/people/", 9, "ar", "تثبت سجلات الأسبوع العالمي للمال",
     "تثبت سجلات الأسبوع العالمي للمال لدى البنك المركزي تنفيذ أنشطة خلال 2023–2025. غير أن النشاط، والمخرجات أو الإكمال الموثق، وقياس القدرات على مستوى السكان، والنتيجة التي يثبتها تقييم، أربعة مستويات مختلفة من الأدلة: فالمشاركة في نشاط لا تثبت بذاتها تحسن القدرة أو تحقق أثر، ولا يُنسب إلى البرنامج أثر فعلي من دون تقييم يتضمن خط أساس وقياسًا نهائيًا. أما مقاييس القدرات المالية للسكان، مثل نتائج مسح OECD/INFE، فهي نوع مختلف من الأدلة، ولا ينسبها هذا الموقع إلى هذه الأنشطة."),
    ("P1-F03", "/people/", 10, "ar", "الرقم السكاني يقيس الأشخاص",
     "الرقم السكاني يقيس الأشخاص وفق تصميم المسح وأوزانه، ولا يجوز استبداله بعدد الحسابات المصرفية أو المحافظ أو المدخرين أو المعاملات أو أجهزة الدفع؛ فهذه وحدات قياس مختلفة."),
    # /firms/
    ("P1-F04", "/firms/", 2, "en", "In the seven-governorate 2022 survey, the reported challenge shares",
     "In the seven-governorate 2022 survey, the reported challenge shares were: electricity 50%, fuel 46%, transport 32%, tax 30%, political instability 27%, access to finance 22%, siege 18% and informal competition 17%. Respondents could name more than one challenge, so the shares add up to more than 100%, and the base for this question is not recorded in the evidence base; small differences between adjacent items should not be read as a firm ranking. These results answer “what was cited as a general challenge in this survey?” — not “what is the national ranking of constraints for all Yemeni firms?”"),
    ("P1-F04", "/firms/", 2, "ar", "في المسح المخصص الذي شمل سبع محافظات عام 2022، ذكرت 50%",
     "في المسح المخصص الذي شمل سبع محافظات عام 2022، ذكرت 50% من المنشآت الكهرباء كتحدٍ، و46% الوقود، و32% النقل، و30% الضرائب، و27% عدم الاستقرار السياسي، مقابل 22% للوصول إلى التمويل و18% للحصار و17% للمنافسة غير الرسمية. وكان بإمكان المنشأة ذكر أكثر من تحدٍّ، لذلك يتجاوز مجموع النسب 100%، ولا تتضمن قاعدة الأدلة حجم العينة التي أجابت عن هذا السؤال؛ فلا ينبغي قراءة الفروق الصغيرة بين البنود المتجاورة كترتيب ثابت. وهذه النتائج تخص عينة المسح وجغرافيته، ولا تمثل ترتيبًا وطنيًا لجميع منشآت اليمن."),
    ("P1-F04", "/firms/", 3, "en", "Among the firms in the report's finance-obstacle tabulation",
     "Among the firms in the report's finance-obstacle tabulation, which excludes firms that said they did not need a loan, 68.71% rated financing obstacles as major and 23.13% as moderate — 91.84% combined. This is a result for that filtered group, not the share of all Yemeni firms facing a major or moderate finance obstacle."),
    ("P1-F04", "/firms/", 3, "ar", "بين المنشآت التي شملها جدول عوائق التمويل في التقرير",
     "بين المنشآت التي شملها جدول عوائق التمويل في التقرير، بعد استبعاد المنشآت التي قالت إنها لا تحتاج إلى قرض، صنفت 68.71% عوائق التمويل بأنها كبيرة و23.13% بأنها متوسطة، أي 91.84% معًا. وتخص هذه النسبة تلك الفئة المصفاة وقاعدة احتسابها، ولا تعني أن 91.84% من جميع منشآت اليمن تواجه عائقًا تمويليًا كبيرًا أو متوسطًا."),
    ("P1-F04", "/firms/", 4, "en", "Within the formal-firm sample, 31 of 328 firms",
     "Within the formal-firm sample, 31 of 328 firms reported a line of credit, and only 18 gave a valid response to the loan-source question. The source mix can therefore be described only for those 18 responses — not for all surveyed firms, all borrowers or all Yemeni enterprises."),
    ("P1-F04", "/firms/", 4, "ar", "داخل عينة المنشآت الرسمية في المسح، أبلغ 31",
     "داخل عينة المنشآت الرسمية في المسح، أبلغت 31 من أصل 328 منشأة عن وجود خط ائتمان، ولا تتوفر سوى 18 استجابة صالحة لسؤال مصدر القرض. لذلك لا يمكن وصف تركيبة مصادر الائتمان إلا لهذه الاستجابات الثماني عشرة، لا لجميع منشآت العينة ولا لجميع المقترضين ولا لجميع المنشآت اليمنية."),
    ("P1-F04", "/firms/", 6, "en", "SMEPS reports support to 8,217 MSMEs",
     "SMEPS reports that in 2024 it supported 8,217 MSMEs and disbursed USD 22,865,322, and that across 2021–2024 its support reached 31,560 MSMEs with USD 54.7 million in programme funding or disbursement. These are programme-delivery measures within the programme’s own beneficiary universe; they are not a count of Yemen’s MSME population, a measure of financial-sector lending, or proof of causal impact."),
    ("P1-F04", "/firms/", 6, "ar", "تفيد SMEPS بأنها دعمت 8,217",
     "تفيد وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS) بأنها دعمت 8,217 منشأة صغرى وصغيرة ومتوسطة في 2024 وصرفت 22,865,322 دولارًا، وأن دعمها خلال 2021–2024 شمل 31,560 منشأة بتمويل أو صرف برامجي قدره 54.7 مليون دولار. وهذه مقاييس لتنفيذ البرنامج داخل نطاق المستفيدين منه، ولا تمثل عدد المنشآت في اليمن ولا حجم إقراض القطاع المالي، ولا تثبت أثرًا سببيًا."),
    ("P1-F04", "/firms/", 7, "en", "The SMEPS 2024 report gives a 19%",
     "SMEPS’s 2024 Annual Report states that 19% of supported MSMEs accessed financial services in 2024, and gives 15% for 2021–2024 against a programme target of 40%. The report does not fully specify the calculation base or the operational definition of “accessed financial services”. The KPI is therefore readable only within the programme’s own universe, with that limitation visible: it is not a national MSME access rate, and the 40% remains a target, not an observed result."),
    ("P1-F04", "/firms/", 7, "ar", "يذكر تقرير SMEPS لعام 2024 أن 19%",
     "يورد التقرير السنوي 2024 لوكالة SMEPS أن 19% من المنشآت التي دعمها البرنامج «وصلت إلى خدمات مالية» في 2024، ونسبة 15% للفترة 2021–2024 مقابل مستهدف برامجي قدره 40%. ولا يحدد التقرير بصورة كاملة قاعدة احتساب هذا المؤشر ولا التعريف التشغيلي لعبارة «الوصول إلى خدمات مالية». ولذلك لا يُقرأ المؤشر إلا داخل نطاق البرنامج، مع إبقاء هذا القيد ظاهرًا: فهو ليس معدلًا وطنيًا لوصول المنشآت إلى الخدمات المالية، وتبقى نسبة 40% مستهدفًا لا نتيجة مرصودة."),
    ("P1-F04", "/firms/", 8, "ar", "مشكلة التمويل لا تبدأ وتنتهي",
     "مشكلة التمويل لا تبدأ وتنتهي عند سؤال «هل يوجد قرض؟». فالمسار الكامل يشمل الحاجة إلى التمويل، ثم التقديم، والموافقة أو الرفض، وحجم التمويل وشروطه ومصدره، وكيفية استخدامه، وضغوط السداد، وما حدث للمنشأة بعده. والأدلة الحالية لا تغطي هذا المسار كاملًا على المستوى الوطني."),
    # /finance/
    ("P1-F04", "/finance/", 6, "en", "The compiled monetary series provide balance-sheet context",
     "The compiled monetary series provide balance-sheet context on bank deposits, credit to the private sector, bank reserves, capital and reserves, loans and advances, and foreign-currency deposits across their available reporting periods. These measures help describe intermediation capacity and structure, but they are not a complete current financial-soundness assessment: solvency, asset quality or current system-wide soundness cannot be inferred from balance-sheet aggregates alone. The current evidence base does not yet contain a harmonized, publication-ready set of non-performing-loan, capital-adequacy and liquidity ratios with common definitions and vintages."),
    ("P1-F04", "/finance/", 6, "ar", "تتيح السلاسل النقدية المعتمدة هنا",
     "تتيح السلاسل النقدية المعتمدة هنا قراءةً لسياق الميزانيات والوساطة، بما يشمل الودائع والائتمان المقدم للقطاع الخاص واحتياطيات البنوك ورأس المال والاحتياطيات والقروض والسلف والودائع بالعملات الأجنبية، كلٌّ ضمن فترته المتاحة. وتفيد هذه المؤشرات في فهم قدرة النظام على الوساطة وهيكله، لكنها لا تشكل تشخيصًا مكتملًا وحديثًا للمتانة المالية؛ فلا يُستنتج من مجاميع الميزانيات وحدها مستوى الملاءة أو جودة الأصول أو المتانة المالية الحالية للنظام ككل. ولا تتضمن قاعدة الأدلة بعدُ مجموعة منسجمة وجاهزة للنشر لمؤشرات القروض المتعثرة وكفاية رأس المال والسيولة بتعريفات ونسخ زمنية قابلة للمقارنة."),
    ("P1-F04", "/finance/", 8, "en", "The documented chronology traces several distinct breaks",
     "The documented chronology traces several distinct breaks: reserve and import-finance pressure by 2015–16; the 2016 central-bank split; rapid growth of currency outside banks by 2017; Saudi reserve support in 2018 and 2023; the 2019 split-cash/payment episode; the oil-export shock after 2022; FX auctions and external support in 2023–24; banking-liquidity stress and administrative FX/import measures in 2025; and later payment-infrastructure investment. Each event keeps its territorial and institutional scope; where money is involved, agreement, deposit, availability, disbursement and downstream use are kept apart and never added together; and same-year remittance revisions are kept separate from economic change. These events help explain the environment in which finance operates, but their sequence does not prove that any one event caused a financial-inclusion outcome."),
    ("P1-F04", "/finance/", 8, "ar", "تتبع السلسلة الزمنية المعتمدة تحولات مختلفة",
     "تتبع السلسلة الزمنية المعتمدة تحولات مختلفة لا يجوز دمجها في اتجاه واحد: ضغوط الاحتياطيات وتمويل الواردات بحلول 2015–2016؛ وانقسام البنك المركزي في 2016؛ والارتفاع السريع للنقد خارج البنوك بحلول 2017؛ ودعم الاحتياطيات السعودي في 2018 و2023؛ وانقسام دورة النقد والمدفوعات في 2019؛ وصدمة توقف صادرات النفط بعد 2022؛ ومزادات النقد الأجنبي والدعم الخارجي في 2023–2024؛ وضغوط السيولة المصرفية وتدابير النقد الأجنبي وتمويل الواردات في 2025؛ ثم الاستثمار اللاحق في بنية المدفوعات. ويحتفظ كل حدث بنطاقه الجغرافي والمؤسسي؛ وحين يتعلق الحدث بتمويل، تبقى حالات الاتفاق والإيداع والإتاحة والصرف والاستخدام اللاحق منفصلة ولا تُجمع مبالغها؛ كما تُفصل مراجعات أرقام التحويلات للسنة نفسها عن التغير الاقتصادي الفعلي. تساعد هذه الأحداث على تفسير البيئة التي تعمل فيها الوساطة المالية، لكن تعاقبها لا يثبت أن حدثًا بعينه تسبب في نتيجة للشمول المالي."),
]

# ---------------------------------------------------------------- P1.2 / P1.4: typed counts and identifier jargon in public copy
# (finding, route, order, lang, field, old substring, new substring)
SUBS = [
    ("P1-F02", "/data/", 9, "en", "body", "The chronology brings together 24 documented events across", "The chronology brings together documented events across"),
    ("P1-F02", "/data/", 9, "ar", "body", "تجمع السلسلة الزمنية 24 حدثًا موثقًا عبر", "تجمع السلسلة الزمنية أحداثًا موثقة عبر"),
    ("P1-F02", "/explore/", 5, "en", "heading", "Eleven questions to start from", "Questions to start from"),
    ("P1-F02", "/explore/", 5, "en", "body", "Use the 11 questions below to enter", "Use the questions below to enter"),
    ("P1-F02", "/explore/", 5, "ar", "heading", "أحد عشر سؤالًا للبدء", "أسئلة للبدء"),
    ("P1-F02", "/explore/", 5, "ar", "body", "استخدم الأسئلة الأحد عشر أدناه", "استخدم الأسئلة أدناه"),
    ("P1-F02", "/", 9, "en", "heading", "Eleven questions to start from", "Questions to start from"),
    ("P1-F02", "/", 9, "ar", "heading", "أحد عشر سؤالًا للبدء", "أسئلة للبدء"),
    ("P1-F02", "/measurement/", 10, "en", "heading", "Ten measurements that would change decisions", "Measurements that would change decisions"),
    ("P1-F02", "/measurement/", 10, "en", "body", "The agenda contains ten public measurement priorities. Each item sets out", "Each agenda priority sets out"),
    ("P1-F02", "/measurement/", 10, "ar", "heading", "عشرة قياسات قد تغير القرار", "قياسات قد تغيّر القرار"),
    ("P1-F02", "/measurement/", 10, "ar", "body", "تضم الأجندة عشر أولويات عامة للقياس، ويبيّن كل بند", "يبيّن كل بند في الأجندة"),
    ("P1-F02", "/readings/", 1, "en", "heading", "Ten evidence readings for consequential questions", "Evidence Readings for consequential questions"),
    ("P1-F02", "/readings/", 1, "en", "body", "The ten readings connect multiple evidence records", "The Readings connect multiple evidence records"),
    ("P1-F02", "/readings/", 1, "ar", "heading", "عشر قراءات للأسئلة ذات الأثر", "قراءات الأدلة للأسئلة ذات الأثر"),
    ("P1-F02", "/readings/", 1, "ar", "body", "تربط القراءات العشر عدة أدلة", "تربط هذه القراءات عدة أدلة"),
    # /about/: the lead already defines what the resource does not do (P1.3); the correction path names the public reference (P1.4)
    ("P1-F06", "/about/", 5, "en", "body", "This resource does not manufacture certainty that the evidence does not contain. It does not make decisions for users or simulate policy outcomes. It distinguishes",
     "This resource does not manufacture certainty that the evidence does not contain. It distinguishes"),
    ("P1-F06", "/about/", 5, "ar", "body", "لا يصنع هذا المورد يقينًا غير موجود، ولا يتخذ القرارات نيابة عن المستخدمين، ولا يحاكي نتائج السياسات. فهو يميز",
     "لا يصنع هذا المورد يقينًا لا تحتمله الأدلة؛ فهو يميز"),
    ("P1-F06", "/about/", 5, "ar", "body", "بل يوضح المنتج ما الدليل المطلوب لاحقًا", "بل يوضح ما الدليل المطلوب لاحقًا"),
    ("P1-F05", "/about/", 7, "en", "body", "Suspected errors should be reported with the evidence record or source ID so they can be traced.",
     "Suspected errors should be reported with the reference of the evidence record or source so they can be traced."),
    ("P1-F05", "/about/", 7, "ar", "body", "باستخدام معرّف سجل الدليل أو المصدر حتى يمكن تتبعه.", "باستخدام مرجع سجل الدليل أو المصدر حتى يمكن تتبعه."),
]
WHOLE = [
    # /measurement/ s3: the stable reference is explained for citation, without internal release jargon (P1.4)
    ("P1-F05", "/measurement/", 3, "en", "body",
     "The list is built from the ten measurement items MA-001 to MA-010. Every item keeps its immutable ID so it can be searched, deep-linked, cited, corrected and carried through release history without relying on a title that may change.",
     "Each priority has a stable reference, such as MA-001, so that it can be cited, linked and corrected without depending on a title that may change."),
    ("P1-F05", "/measurement/", 3, "ar", "body",
     "تُنشأ القائمة العامة من عناصر القياس الثابتة MA-001…MA-010. يحتفظ كل بند بمعرفه الدائم حتى يمكن البحث عنه وربطه مباشرة والاستشهاد به وتصحيحه وتتبع تاريخه من دون الاعتماد على عنوان قد يتغير.",
     "لكل أولوية مرجع ثابت، مثل MA-001، يتيح الاستشهاد بها وربطها مباشرة وتصحيحها من دون الاعتماد على عنوان قد يتغير."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    # P1.2: /data/ inventory — {N_CLAIMS} and the stale 159/158 counts are replaced by derived tokens
    for lang, new in (("en", DATA_INV_EN), ("ar", DATA_INV_AR)):
        row = s.section_row("/data/", 8, lang)
        col = 5 if lang == "en" else 7
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
        if "{N_CLAIMS}" not in cur or ("159" not in cur):
            raise SystemExit(f"/data/ s8 {lang}: unexpected current inventory text")
        s.set("P1-F01", "03_PAGE_SECTIONS", row, col, new, cur, f"/data/#s8.body_{lang}")
    for f, route, order, lang, field, old, new in SUBS:
        s.replace_section(f, route, order, lang, field, old, new)
    for f, route, order, lang, field, old, new in WHOLE:
        s.set_section(f, route, order, lang, field, new, old)
    for f, route, order, lang, start, new in CARDS:
        s.rewrite_section(f, route, order, lang, "body", new, start)
    changed = s.regenerate_full_copy()
    rep = s.save(out, ledger, [("transaction", "P1-A"), ("scope", "P1.2 inventory tokens; P1.2/P1.4 counts and identifiers in copy; P1.3 flattened card bodies"),
                               ("full_copy_regenerated", changed)])
    print(f"P1-A staged: {rep['cells_written']} cells; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
