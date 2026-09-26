# -*- coding: utf-8 -*-
"""RP-F2 transaction input: the adjudicated Evidence Readings portfolio (F1, 26 September 2026).

This file is lineage, not authority. It is read once by rp_integration.py, which writes it into the Production Master
(08_READINGS, 03_PAGE_SECTIONS, 09_READING_SECTIONS, 11_VISUAL_LIBRARY, 02_SITE_MAP, 04_NAV_UX). After that transaction
the Master is the only Reading truth; this file is never read by the generator, the build or the runtime.

Conventions inside section bodies (rendered by scripts/build.py): one paragraph per line; a line that starts with "- "
is a list item; a line that starts with "> " is the Reading's pulled line. No other markup.
Decisions and departures from the Appendix A candidate: audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md and
audit/READING_PORTFOLIO_CHANGE_LEDGER.csv.
"""

REVIEWED = "2026-09-26"
CHANGE_H = ("What would change this reading?", "ما الذي قد يغيّر هذه القراءة؟")

READINGS = [
# ---------------------------------------------------------------------------------------------------------------- 001
{
"reading_id": "CWR-001",
"disposition": "MERGE NARROWLY",
"title": ("Same year, different number", "العام نفسه، رقم مختلف"),
"question": ("When two official reports give different remittance values for the same year, what changed: the economy or the measurement?",
             "عندما يعطي تقريران رسميان قيمتين مختلفتين للتحويلات في السنة نفسها، ما الذي تغيّر: الاقتصاد أم القياس؟"),
"thesis": ("Successive annual reports of the Central Bank of Yemen – Aden give very different remittance values for 2024. A revision of this size is a measurement event to be explained before it can be read as an economic story.",
           "تعطي التقارير السنوية المتتالية للبنك المركزي اليمني – عدن قيمتين مختلفتين كثيرًا للتحويلات في عام 2024. ومراجعة بهذا الحجم حدثٌ في القياس ينبغي تفسيره قبل أن يُقرأ قصةً اقتصادية."),
"evidence_period": ("Reference years 2021–2024 · CBY-Aden annual reports 2024 and 2025 · IMF Article IV consultation 2025",
                    "السنوات المرجعية 2021–2024 · التقريران السنويان للبنك المركزي اليمني – عدن 2024 و2025 · مشاورات المادة الرابعة لصندوق النقد الدولي 2025"),
"prohibited_inference": None,   # current governed text kept
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-001"],
"domain_surface_routes": ["/remittances/"],
"related_readings": ["CWR-002", "CWR-004"],
"measurement_bindings": [],
"featured": False,
"sections": [
 ("opening", None, None,
  "Two annual reports of the Central Bank of Yemen – Aden (CBY-Aden) give markedly different remittance values for the same reference year. The 2024 report put remittances in 2024 at USD 6.245 billion; the 2025 report restated 2024 at about USD 3.42 billion.\n"
  "The gap is large, but the first thing it establishes is not that remittances collapsed. Both values describe 2024. Before the difference can be read as economic movement, the change in statistical vintage, scope or method has to be understood.",
  "يورد تقريران سنويان للبنك المركزي اليمني – عدن قيمتين مختلفتين كثيرًا للتحويلات في السنة المرجعية نفسها. فقد قدّر تقرير 2024 التحويلات في عام 2024 بنحو 6.245 مليار دولار، ثم أعاد تقرير 2025 عرض قيمة عام 2024 عند 3.42 مليار دولار تقريبًا.\n"
  "الفرق كبير، لكنه لا يثبت أن التحويلات انهارت؛ فالقيمتان تصفان عام 2024 نفسه. وقبل قراءة الفرق حركةً في الاقتصاد، ينبغي فهم ما تغيّر في نسخة النشر أو نطاق الإحصاء أو منهجه."),
 ("evidence_vintage", "Two publications, one reference year", "إصداران لسنة مرجعية واحدة",
  "Revisions are normal in economic statistics. They become consequential when the revised value is large enough to change the baseline that analysis depends on, and this one is.\n"
  "So “2024 remittances” is not precise enough on its own when two official publications attach materially different values to that year. The publication vintage has to travel with the reference year.",
  "المراجعات أمر معتاد في الإحصاءات الاقتصادية، لكنها تصبح ذات أثر حين تكون القيمة المعدلة كبيرة بما يكفي لتغيير خط الأساس الذي يقوم عليه التحليل، وهذه المراجعة من هذا النوع.\n"
  "لذلك لا تكفي عبارة «تحويلات 2024» وحدها عندما يعطي إصداران رسميان قيمتين مختلفتين جوهريًا للسنة نفسها؛ إذ ينبغي أن ترافق نسخةُ النشر السنةَ المرجعية أينما ذُكر الرقم."),
 ("evidence_concordance", "The shape of the series is a clue, not a crosswalk", "تشابه المسار قرينة، لا جدول مطابقة",
  "When the remittance series in the 2025 CBY-Aden report and the IMF’s 2025 Article IV series are each indexed to 2021 = 100, their paths through 2024 are almost identical: the largest difference in annual growth over 2022–2024 is 0.0032 percentage points. Their levels are not: in every year from 2021 to 2024 the CBY-Aden value is 1.838 times the IMF value.\n"
  "That regularity is useful. It suggests closely related trajectories compiled under different scopes or methods. It does not supply a conversion formula, and nothing public explains what the ratio represents.\n"
  "IMF documentation describes a reconstruction of Yemen’s external-sector statistics under severe data constraints, including a model of personal transfers where information on informal channels was limited. That is method context. It does not reveal the exact formula behind each value in the CBY-Aden annual report.\n"
  "> A statistical clue is not yet a documented crosswalk.",
  "عند تحويل سلسلة التحويلات في تقرير البنك المركزي اليمني – عدن لعام 2025 وسلسلة صندوق النقد الدولي في مشاورات المادة الرابعة لعام 2025 إلى رقمين قياسيين (2021 = 100)، يكاد مساراهما يتطابقان حتى عام 2024؛ إذ لا يتجاوز أكبر فرق في معدل النمو السنوي خلال 2022–2024 نحو 0.0032 نقطة مئوية. أما المستويات فلا تتطابق: ففي كل سنة من 2021 إلى 2024 تعادل قيمة البنك المركزي في عدن 1.838 ضعف قيمة الصندوق.\n"
  "هذا الانتظام مفيد، إذ يوحي بمسارين متقاربين جُمعا وفق نطاقين أو منهجين مختلفين. لكنه لا يقدم صيغة تحويل، ولا يوجد ما هو منشور يفسر ما تمثله هذه النسبة.\n"
  "وتصف وثائق صندوق النقد إعادة بناء إحصاءات القطاع الخارجي في اليمن في ظل قيود شديدة على البيانات، بما في ذلك نموذج لتقدير التحويلات الشخصية حيث كانت المعلومات عن القنوات غير الرسمية محدودة. هذا سياق منهجي، ولا يكشف الصيغة الدقيقة وراء كل قيمة في التقرير السنوي للبنك المركزي.\n"
  "> القرينة الإحصائية ليست بعدُ جدول مطابقة موثقًا."),
 ("why_it_matters", "Why the revision matters", "لماذا تهم هذه المراجعة؟",
  "Remittances matter at several levels at once: household livelihoods, the supply of foreign exchange, balance-of-payments analysis and the channels, formal and informal, through which money moves. A large revision to the macro series can therefore shift several analytical baselines without any new event in a single household.\n"
  "Read without both the reference year and the publication vintage, a statistical revision can be mistaken for growth or collapse. Read with both, the useful question becomes: what changed in the measurement, and what, if anything, changed in the economy?",
  "تمس التحويلات مستويات عدة في آن واحد: معيشة الأسر، والمعروض من النقد الأجنبي، وتحليل ميزان المدفوعات، والقنوات الرسمية وغير الرسمية التي تنتقل عبرها الأموال. لذلك قد تغيّر مراجعةٌ كبيرة للسلسلة الكلية أكثر من خط أساس تحليلي من دون أن يقع حدث جديد لدى أي أسرة.\n"
  "وإذا قُرئت المراجعة الإحصائية من دون السنة المرجعية ونسخة النشر معًا، فقد تُفهم خطأً على أنها نمو أو انهيار. أما حين يُقرأ الرقم بهما معًا، فيصبح السؤال المفيد: ما الذي تغيّر في القياس، وما الذي تغيّر في الاقتصاد، إن كان قد تغيّر شيء؟"),
 ("boundary", "What this evidence does not tell us", "ما الذي لا تخبرنا به هذه الأدلة",
  "It does not show that one series is correct for every purpose and the other wrong, and it offers no general conversion factor between the CBY-Aden and IMF series. It says nothing about how remittances are distributed across households, governorates or channels. And net errors and omissions in the balance of payments cannot be relabelled as unrecorded remittances: the residual balances the accounts; it is not an observed flow.",
  "لا تبين الأدلة أن إحدى السلسلتين صحيحة لكل غرض والأخرى خاطئة، ولا تقدم معامل تحويل عامًّا بين سلسلتي البنك المركزي في عدن وصندوق النقد. ولا تقول شيئًا عن توزيع التحويلات بين الأسر أو المحافظات أو القنوات. كما لا يجوز إعادة تسمية صافي السهو والخطأ في ميزان المدفوعات تحويلاتٍ غير مسجلة؛ فهو بند موازنة للحسابات، لا تدفق مرصود."),
 ("use", "How to use the figures", "كيف تُستخدم هذه الأرقام",
  "For trend analysis, use a consistent statistical vintage wherever possible, and where the vintage changes, show the break. For scenario work it is legitimate to keep more than one baseline, provided each result says which one it uses. In public communication, describe a same-year difference as a statistical restatement, not as movement from one year to the next.",
  "في تحليل الاتجاهات، استخدم نسخة إحصائية واحدة متسقة كلما أمكن، وحين تتغير النسخة أظهر نقطة الانقطاع. وفي تحليل السيناريوهات يجوز الاحتفاظ بأكثر من خط أساس، بشرط أن تذكر كل نتيجة الخط الذي تعتمد عليه. أما في التواصل العام، فيوصف الفرق في السنة نفسها بأنه إعادة عرض إحصائية، لا حركة من سنة إلى أخرى."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A primary methodological note linking the restated CBY-Aden series to the external-sector reconstruction would change the analysis materially. The most useful note would set out the scope, the source inputs, the treatment of informal flows, the revision policy and how the old and new vintages relate.\n"
  "Until it exists, keep the vintage with the number.",
  "من شأن مذكرة منهجية صادرة عن المصدر نفسه، تربط سلسلة البنك المركزي في عدن المعاد عرضها بإعادة بناء إحصاءات القطاع الخارجي، أن تغيّر التحليل تغييرًا جوهريًا. وأكثر ما يفيد أن توضح النطاق، ومصادر البيانات، ومعالجة التدفقات غير الرسمية، وسياسة المراجعة، والعلاقة بين النسختين القديمة والجديدة.\n"
  "وإلى أن تتوافر هذه المذكرة، ينبغي أن تبقى نسخة النشر ملازمة للرقم."),
],
},
# ---------------------------------------------------------------------------------------------------------------- 002
{
"reading_id": "CWR-002",
"disposition": "ADOPT CANDIDATE",
"title": ("When the baseline moves", "حين يتحرك خط الأساس"),
"question": ("When the same year’s banking positions are published at higher levels in a later report, how much of the jump is the economy and how much is the measurement?",
             "عندما تُنشر المراكز المصرفية للسنة نفسها بمستويات أعلى في تقرير لاحق، كم من هذه القفزة يعود إلى الاقتصاد، وكم يعود إلى القياس؟"),
"thesis": ("Yemen’s banking series shows why a large published jump must be separated from a change in measurement before it becomes an economic story.",
           "تبيّن السلسلة المصرفية في اليمن لماذا ينبغي فصل القفزة المنشورة عن أي تغير في طريقة القياس قبل أن تتحول إلى قصة عن الاقتصاد."),
"evidence_period": ("Positions at end-2022 as published in the 2022 annual report and restated from 2023 · valuation change of January 2023",
                    "المراكز في نهاية 2022 كما نُشرت في التقرير السنوي لعام 2022 وكما أُعيد عرضها ابتداءً من 2023 · تغيير التقييم في يناير 2023"),
"prohibited_inference": ("A same-year restatement does not show a credit, deposit or asset boom or a change in solvency, and the evidence does not yet divide the jump between valuation and economic movement.",
                         "لا تُظهر إعادة عرض أرقام السنة نفسها طفرة في الائتمان أو الودائع أو الأصول ولا تغيرًا في الملاءة، ولا تقسم الأدلة حتى الآن القفزة بين أثر التقييم والحركة الاقتصادية."),
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-002"],
"domain_surface_routes": ["/finance/"],
"related_readings": ["CWR-001", "CWR-006"],
"measurement_bindings": [],
"featured": False,
"sections": [
 ("opening", None, None,
  "A number can rise because the economy changed. It can also rise because the way an existing position is valued, classified or reported changed. Yemen’s banking data require the two to be kept apart.\n"
  "The same 2022 consolidated positions of commercial and Islamic banks are published at materially higher levels in the annual reports of the Central Bank of Yemen – Aden (CBY-Aden) from 2023 onward than in the 2022 report. The change comes alongside a documented January 2023 shift to valuing foreign-currency positions at the market exchange rate.\n"
  "The point is not that the later values are wrong. It is that a comparison across the break does not start from a single, unchanged statistical base.\n"
  "> A growth rate calculated across a method break can partly measure the method.",
  "قد يرتفع الرقم لأن الاقتصاد تغيّر، وقد يرتفع لأن طريقة تقييم مركز قائم أو تصنيفه أو الإبلاغ عنه تغيّرت. وفي البيانات المصرفية اليمنية ينبغي إبقاء الاحتمالين منفصلين.\n"
  "تظهر المراكز المجمعة للبنوك التجارية والإسلامية في نهاية 2022 بمستويات أعلى جوهريًا في التقارير السنوية للبنك المركزي اليمني – عدن ابتداءً من تقرير 2023 مقارنةً بتقرير 2022، بالتزامن مع تحول موثق في يناير 2023 إلى تقييم المراكز بالعملات الأجنبية بسعر الصرف في السوق.\n"
  "ولا يعني ذلك أن القيم اللاحقة خاطئة؛ فالمشكلة أن المقارنة عبر نقطة الانقطاع لا تنطلق من أساس إحصائي واحد لم يتغير.\n"
  "> قد يقيس معدل النمو المحسوب عبر انقطاع منهجي جزءًا من تغيّر المنهج نفسه."),
 ("evidence_break", "The break runs across more than one line", "الانقطاع لا يقتصر على بند واحد",
  "The restatement shows up across several balance-sheet positions, not in one isolated indicator. That matters, because a simultaneous change in deposits, credit, assets or foreign-currency positions can otherwise be read as an equally large shift in financial intermediation. The current evidence does not support that reading.\n"
  "The valuation note documents a change in treatment. It does not provide a line-by-line bridge showing how much of each restated balance comes from valuation, classification, coverage or economic movement, so that decomposition remains open.",
  "تظهر إعادة العرض في أكثر من بند من بنود الميزانية، لا في مؤشر منفرد. وهذا مهم، لأن التغير المتزامن في الودائع أو الائتمان أو الأصول أو المراكز بالعملات الأجنبية قد يُقرأ عندئذ على أنه تحول بالحجم نفسه في الوساطة المالية، والأدلة الحالية لا تسند هذه القراءة.\n"
  "توثّق ملاحظة التقييم تغيّرًا في المعالجة، لكنها لا تقدم جسرًا بندًا ببند يبين مقدار ما يعود في كل رصيد معاد عرضه إلى التقييم أو التصنيف أو نطاق التغطية أو الحركة الاقتصادية الفعلية، ولذلك يبقى هذا التفكيك مفتوحًا."),
 ("context_history", "History rules out an easy “first-ever” story", "التاريخ ينفي رواية «المرة الأولى»",
  "Market-rate valuation of foreign-currency accounts has documented precedent in Yemen from 1996. That does not prove the 1996 and 2023 arrangements were identical, but it does mean January 2023 should not be described as the first time Yemen used market-rate valuation.\n"
  "The defensible statement is narrower: the current banking series contains a documented valuation or reporting break from January 2023, and that break changes how comparisons around it should be read.",
  "لتقييم الحسابات بالعملات الأجنبية بسعر السوق سابقةٌ موثقة في اليمن منذ 1996. ولا يثبت ذلك أن ترتيبات 1996 و2023 كانت متطابقة، لكنه يعني أن يناير 2023 لا ينبغي وصفه بأنه أول مرة يُستخدم فيها التقييم بسعر السوق في اليمن.\n"
  "والصياغة القابلة للدفاع أضيق: تتضمن السلسلة المصرفية الحالية انقطاعًا موثقًا في التقييم أو الإبلاغ ابتداءً من يناير 2023، وهذا الانقطاع يغيّر طريقة قراءة المقارنات من حوله."),
 ("use", "What remains usable", "ما الذي يبقى صالحًا للاستخدام",
  "A method break does not make the banking series unusable; it changes the rule for comparing it. Where possible, compare observations within one statistical vintage and under the same reported treatment. Where a value for the same period is restated, keep both vintages visible until the bridge between them is understood.\n"
  "Even within a consistent vintage, nominal balance-sheet growth does not by itself establish:\n"
  "- real credit growth;\n"
  "- more borrowers;\n"
  "- wider access;\n"
  "- better allocation of credit;\n"
  "- stronger bank soundness;\n"
  "- or greater financial inclusion.\n"
  "Those are separate questions, each with its own evidence.",
  "لا يجعل الانقطاع المنهجي السلسلةَ المصرفية عديمة الفائدة، لكنه يغيّر قاعدة المقارنة. فحيثما أمكن، تُقارن المشاهدات داخل نسخة إحصائية واحدة وبالمعالجة المبلغ عنها نفسها. وحين يُعاد عرض قيمة للفترة نفسها، تبقى النسختان ظاهرتين إلى أن يُفهم الجسر بينهما.\n"
  "وحتى داخل نسخة متسقة، لا يثبت النمو الاسمي في أرصدة الميزانية وحده:\n"
  "- نموًا حقيقيًا في الائتمان؛\n"
  "- أو زيادة في عدد المقترضين؛\n"
  "- أو اتساعًا في الوصول؛\n"
  "- أو تحسنًا في تخصيص الائتمان؛\n"
  "- أو متانة أكبر للبنوك؛\n"
  "- أو زيادة في الشمول المالي.\n"
  "فهذه أسئلة مستقلة، ولكل منها دليله."),
 ("boundary", "Where the evidence stops", "أين يتوقف الدليل؟",
  "The evidence does not yet include a verified line-by-line reconciliation of the old and new 2022 bases. For that reason this Reading publishes no headline percentage for the size of the restatement and does not treat the difference as a measured economic gain. That restraint is part of the result.",
  "لا تتضمن الأدلة حتى الآن مطابقة محققة بندًا ببند بين أساس 2022 القديم والأساس المعاد عرضه. ولهذا لا تنشر هذه القراءة نسبة رئيسية لحجم إعادة العرض، ولا تعامل الفرق مكسبًا اقتصاديًا مقاسًا. وهذا التحفظ جزء من النتيجة."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "The exact January 2023 circular, together with a reconciliation table showing, for each affected balance-sheet line:\n"
  "- the legacy value;\n"
  "- the restated value;\n"
  "- the valuation treatment;\n"
  "- any change in classification or in the reporting population;\n"
  "- and the part, if any, attributable to underlying economic movement.\n"
  "Until that bridge exists, the safe rule is simple.\n"
  "> Show the break. Keep the vintage. Do not calculate growth through a changed base as if the base had never moved.",
  "التعميم الدقيق الصادر في يناير 2023، مع جدول مطابقة يبين لكل بند متأثر في الميزانية:\n"
  "- القيمة القديمة؛\n"
  "- القيمة المعاد عرضها؛\n"
  "- معالجة التقييم؛\n"
  "- أي تغير في التصنيف أو في مجتمع الإبلاغ؛\n"
  "- والجزء الذي يمكن إسناده، إن وُجد، إلى حركة اقتصادية فعلية.\n"
  "وإلى أن يتوافر هذا الجسر، تبقى القاعدة الآمنة بسيطة.\n"
  "> أظهِر الانقطاع، واحتفظ بنسخة النشر، ولا تحسب النمو عبر أساس تغيّر كأنه لم يتغير."),
],
},
# ---------------------------------------------------------------------------------------------------------------- 003
{
"reading_id": "CWR-003",
"disposition": "MERGE NARROWLY",
"title": ("When the unit changes, the story changes", "حين تتغير وحدة القياس، تتغير القصة"),
"question": None,   # current governed question kept
"thesis": ("People, accounts, subscribers, terminals and transactions all describe parts of Yemen’s financial system. They are not interchangeable measures of financial inclusion, and a target or a trend is only as sound as the unit it keeps.",
           "يصف الأشخاص والحسابات والمشتركون والأجهزة والمعاملات جميعًا أجزاءً من المنظومة المالية في اليمن، لكنها ليست مقاييس متبادلة للشمول المالي؛ ولا يكون المستهدف أو الاتجاه سليمًا إلا بقدر ثبات الوحدة التي يقيسها."),
"evidence_period": ("Global Findex fieldwork 2022–2023 · POS counts March 2025 – January 2026 · project baseline January 2025, target 2030",
                    "العمل الميداني لمسح Findex العالمي 2022–2023 · أعداد نقاط البيع مارس 2025 – يناير 2026 · خط أساس المشروع يناير 2025 ومستهدفه 2030"),
"prohibited_inference": None,
"claim_bindings": ["CLM-004", "CLM-023", "CLM-024", "CLM-025", "CLM-026", "CLM-001", "CLM-003", "XW-FMIIP-005"],
"evidence_bindings": ["CLM-004", "CLM-023", "CLM-024", "CLM-025", "CLM-026", "CLM-001", "CLM-003", "XW-FMIIP-005"],
"verification_add": ["CLM-001", "CLM-003", "XW-FMIIP-005"],
"visual_bindings": ["RV-CWR-003"],
"domain_surface_routes": ["/access/"],
"related_readings": ["CWR-005", "CWR-008"],
"measurement_bindings": ["MA-005"],
"featured": False,
"sections": [
 ("opening", None, None,
  "Financial-inclusion figures can all move in the same direction and still tell us different things. Adults with an account, accounts on a provider’s books, registered wallet subscribers, active accounts, transactions, POS terminals, programme beneficiaries: each can be useful. The problem begins when one quietly takes the place of another.\n"
  "Yemen’s representative Findex evidence measures people. Administrative systems count financial objects, infrastructure and activity. Programmes count the firms or beneficiaries they support. These measures can describe one financial system without measuring one outcome.",
  "قد تتحرك أرقام الشمول المالي كلها في الاتجاه نفسه، ومع ذلك لا تخبرنا بالشيء نفسه. البالغون الذين يملكون حسابًا، والحسابات المسجلة لدى مقدم الخدمة، والمشتركون في المحافظ الإلكترونية، والحسابات النشطة، والمعاملات، وأجهزة نقاط البيع، والمستفيدون من البرامج: لكل منها فائدته. وتبدأ المشكلة حين يحل أحدها بصمت محل الآخر.\n"
  "يقيس مسح Findex الممثل في اليمن أشخاصًا. أما الأنظمة الإدارية فتعد أدوات مالية وبنية تحتية ونشاطًا، وتعد البرامج المنشآت أو المستفيدين الذين تدعمهم. ويمكن لهذه المقاييس أن تصف منظومة مالية واحدة من دون أن تقيس نتيجة واحدة."),
 ("evidence_unit", "Start with the noun", "ابدأ بما يُعَدّ",
  "“11.9% of adults aged 15 and over in the areas surveyed had an account” (Global Findex, fieldwork 2022–2023) and “POS terminals reported by the Central Bank of Yemen – Aden rose from 561 to 1,473 between March 2025 and January 2026” are both legitimate observations. The first is about people, estimated from a weighted survey. The second is about pieces of infrastructure counted in an administrative system.\n"
  "One terminal can serve many people, and one person can use many terminals. A person can hold several accounts; an account can generate many transactions; a registered subscriber may be inactive.\n"
  "> The noun is part of the metric. Change the noun and the story can change without anything changing in reality.",
  "«كان لدى 11.9% من البالغين في سن 15 عامًا فأكثر في المناطق التي شملها المسح حساب» (مسح Findex العالمي، العمل الميداني 2022–2023)، و«ارتفع عدد أجهزة نقاط البيع التي يبلغ عنها البنك المركزي اليمني – عدن من 561 إلى 1,473 بين مارس 2025 ويناير 2026»: ملاحظتان مشروعتان. الأولى عن أشخاص، مقدَّرة من مسح مرجّح. والثانية عن قطع من البنية التحتية تُعد في نظام إداري.\n"
  "قد يخدم الجهاز الواحد أشخاصًا كثيرين، وقد يستخدم الشخص الواحد أجهزة كثيرة. وقد يملك الشخص أكثر من حساب، وقد يولد الحساب الواحد معاملات كثيرة، وقد يكون المشترك المسجل غير نشط.\n"
  "> ما نعدّه جزء من المؤشر نفسه؛ فإذا تغيّر المعدود قد تتغير القصة من دون أن يتغير شيء في الواقع."),
 ("evidence_denominator", "The denominator still matters", "قاعدة الاحتساب تبقى مهمة",
  "Even when the counted object is people, the denominator cannot disappear. The Yemen Findex study has 1,000 respondents, but population estimates require the survey weights and design. The respondents are the observations from which the estimate is made, not the denominator of Yemen’s adult population, and raw case percentages are not population estimates. The survey frame also excludes areas holding about 23% of the population.",
  "حتى عندما يكون المعدود أشخاصًا، لا يمكن أن تختفي قاعدة الاحتساب. تضم دراسة Findex لليمن 1,000 مستجيب، لكن التقديرات السكانية تتطلب أوزان المسح وتصميمه. فالمستجيبون هم المشاهدات التي يُبنى منها التقدير، وليسوا قاعدة الاحتساب السكانية للبالغين في اليمن، ونسب الحالات الخام ليست تقديرات للسكان. كما أن إطار المسح يستبعد مناطق يقطنها نحو 23% من السكان."),
 ("evidence_programme", "Programme measures are legitimate within their own universe", "مؤشرات البرامج مشروعة داخل نطاقها",
  "The World Bank-financed Financial Market Infrastructure and Inclusion Project sets a 2030 target of 1,021 access points against a January 2025 baseline of 817, under the project’s own definition. That is legitimate project-monitoring evidence.\n"
  "It is not a count of people. Nor can it be added to, or compared directly with, counts of ATMs, POS terminals or agents unless the project’s access-point definitions and de-duplication rules are documented, and in the evidence base they are not. A bounded measure is not weak because its universe is narrow; it becomes misleading when that universe disappears from view.",
  "يحدد مشروع البنية التحتية للأسواق المالية والشمول المالي، الممول من البنك الدولي، مستهدفًا قدره 1,021 نقطة وصول في 2030، مقابل خط أساس قدره 817 نقطة في يناير 2025، وفق تعريف المشروع نفسه. وهذا دليل مشروع صالح للمتابعة.\n"
  "لكنه ليس عددًا للأشخاص. ولا يجوز جمعه مع أعداد أجهزة الصراف الآلي أو نقاط البيع أو الوكلاء، أو مقارنته بها مباشرة، ما لم تُوثَّق تعريفات المشروع لنقاط الوصول وقواعد إزالة الازدواج، وهي غير موثقة في قاعدة الأدلة. ضيق نطاق المقياس لا يجعله ضعيفًا؛ ما يجعله مضللًا أن يغيب هذا النطاق عن العرض."),
 ("interpretation_drift", "When targets drift", "حين ينزلق المستهدف",
  "A baseline may measure adults with an account. Monitoring may later report registered accounts; a dashboard may highlight active wallets; a performance report may celebrate transactions; and the final narrative may call the result greater inclusion. Every number in that chain can be correct while the chain itself is wrong. That is metric drift.\n"
  "Before accepting any baseline, target or claim of progress, ask:\n"
  "- What exactly is being counted?\n"
  "- Among whom does the number apply?\n"
  "- What makes the unit active, or included?\n"
  "- Are the baseline and the result measured under the same definition?\n"
  "- What does the measure still not tell us?",
  "قد يقيس خط الأساس البالغين الذين يملكون حسابًا، ثم تبلغ المتابعة لاحقًا عن الحسابات المسجلة، وتبرز لوحة المؤشرات المحافظ النشطة، ويحتفي تقرير الأداء بالمعاملات، ثم تسمي الرواية الختامية النتيجة «شمولًا أكبر». قد يكون كل رقم في هذه السلسلة صحيحًا بينما السلسلة نفسها خاطئة. هذا هو انزلاق المؤشر.\n"
  "وقبل قبول أي خط أساس أو مستهدف أو ادعاء بالتقدم، اسأل:\n"
  "- ما الذي يُعدّ بالضبط؟\n"
  "- على من ينطبق الرقم؟\n"
  "- ما الذي يجعل الوحدة نشطة أو مشمولة؟\n"
  "- هل قيس خط الأساس والنتيجة بالتعريف نفسه؟\n"
  "- ما الذي لا يخبرنا به المقياس بعد؟"),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A metric crosswalk for Yemen’s main inclusion measures, recording for each one the counted object, whether units are unique, the universe, the denominator, the activity rule, the period, the source, any link to unique people or firms, and whether it measures access, registration, active use, frequency, quality or outcome. Where a bridge is missing, the gap should be visible rather than filled by assumption.\n"
  "The practical rule:\n"
  "> Do not compare two numbers until you can complete this sentence for both: “This counts ___ among ___ under the rule ___ during ___.”\n"
  "If the blanks differ materially, the first question is not how much the number changed. It is whether there is a comparison at all.",
  "جدول ربط لمقاييس الشمول الرئيسية في اليمن، يسجل لكل مقياس: الشيء المعدود، وهل الوحدات فريدة، والمجتمع الذي ينطبق عليه الرقم، وقاعدة الاحتساب، وقاعدة النشاط، والفترة، والمصدر، وأي ربط بالأشخاص أو المنشآت الفريدة، وما إذا كان يقيس الوصول أو التسجيل أو الاستخدام النشط أو التكرار أو الجودة أو النتيجة. وحيث يغيب الجسر بين مقياسين، ينبغي أن تبقى الفجوة ظاهرة لا أن تُملأ بافتراض.\n"
  "والقاعدة العملية:\n"
  "> لا تقارن رقمين قبل أن تستطيع إكمال هذه الجملة لكل منهما: «هذا الرقم يعدّ ___، ضمن ___، وفق قاعدة ___، خلال ___».\n"
  "فإذا اختلفت الفراغات اختلافًا جوهريًا، فالسؤال الأول ليس: كم تغيّر الرقم؟ بل: هل لدينا مقارنة أصلًا؟"),
],
},
# ---------------------------------------------------------------------------------------------------------------- 004
{
"reading_id": "CWR-004",
"disposition": "MERGE NARROWLY",
"title": ("The system is changing. What has reached people?", "المنظومة المالية تتغير. فما الذي وصل إلى الناس؟"),
"question": ("What can we say about people when rules, institutions and payment infrastructure change after the latest representative survey?",
             "ماذا يمكن أن نقول عن الناس حين تتغير القواعد والمؤسسات والبنية التحتية للمدفوعات بعد أحدث مسح ممثل؟"),
"thesis": ("Yemen’s rules, institutions and payment infrastructure have moved faster than its representative evidence about people. The gap between the two is not an answer to guess; it is the next thing to measure.",
           "تحركت القواعد والمؤسسات والبنية التحتية المالية في اليمن بوتيرة أسرع من تجدد الأدلة الممثلة عن الناس. والفجوة بين الأمرين ليست نتيجة يجوز افتراضها؛ إنها السؤال التالي الذي ينبغي قياسه."),
"evidence_period": ("Global Findex fieldwork November 2022 – January 2023 · POS counts March 2025 – January 2026 · institutional records June–August 2026",
                    "العمل الميداني لمسح Findex العالمي نوفمبر 2022 – يناير 2023 · أعداد نقاط البيع مارس 2025 – يناير 2026 · سجلات مؤسسية يونيو–أغسطس 2026"),
"prohibited_inference": None,
"claim_bindings": ["CLM-001", "CLM-003", "CLM-018", "CLM-025"],
"evidence_bindings": ["CLM-001", "CLM-003", "CLM-018", "CLM-025"],
"verification_add": [], "verification_remove": ["CLM-049"],
"visual_bindings": ["RV-CWR-004"],
"domain_surface_routes": ["/people/"],
"related_readings": ["CWR-009", "CWR-003"],
"measurement_bindings": ["MA-001"],
"featured": True,
"sections": [
 ("opening", None, None,
  "The latest representative observation of account ownership in Yemen remains 11.9% of adults aged 15 and over in the areas surveyed, from Global Findex fieldwork conducted between 7 November 2022 and 9 January 2023.\n"
  "The financial system around that observation has kept moving. Rules changed, reported payment infrastructure expanded, institutional arrangements evolved and programmes advanced. All of that matters, and none of it, by itself, tells us Yemen’s current population-level inclusion rate.\n"
  "> The newest evidence is not always the evidence closest to the outcome.\n"
  "The founding assembly of the Yemeni Payments and Clearing Company in August 2026 is current evidence of institution-building. A January 2026 count of POS terminals is current evidence of reported acceptance infrastructure. Neither is a 2026 population estimate.",
  "يبقى أحدث قياس ممثل لامتلاك الحساب في اليمن عند 11.9% من البالغين في سن 15 عامًا فأكثر في المناطق التي شملها المسح، وفق العمل الميداني لمسح Findex العالمي الذي نُفذ بين 7 نوفمبر 2022 و9 يناير 2023.\n"
  "لكن المنظومة المالية المحيطة بهذا القياس لم تتوقف: تغيرت قواعد، واتسعت البنية التحتية للمدفوعات المبلغ عنها، وتطورت ترتيبات مؤسسية، وتقدمت برامج. كل ذلك مهم، ولا شيء منه يخبرنا وحده بمعدل الشمول المالي الحالي لدى السكان.\n"
  "> الأحدث زمنًا ليس بالضرورة الأقرب إلى النتيجة التي نريد قياسها.\n"
  "فانعقاد الجمعية التأسيسية للشركة اليمنية للمدفوعات والمقاصة في أغسطس 2026 دليل حديث على بناء المؤسسات، وعدد أجهزة نقاط البيع في يناير 2026 دليل حديث على بنية قبول الدفع المبلغ عنها، لكن أيًا منهما ليس تقديرًا سكانيًا لعام 2026."),
 ("evidence_clocks", "Four clocks, four questions", "أربعة توقيتات للقياس، وأربعة أسئلة",
  "Findex answers a question administrative systems cannot: what share of people in the survey population report owning an account as Findex defines it? Its limits travel with the number. It is a weighted survey, not a census; its frame excludes areas holding about 23% of the population; more than a quarter of its primary sampling units were replaced during fieldwork; it cannot be mapped by governorate; and it is not a 2026 rate.\n"
  "Rules and institutional records can establish that an instruction was issued, an institution was founded or a governance step occurred. They do not establish effective implementation, customer experience, active use or outcomes.\n"
  "The infrastructure clock moves fastest. POS terminals reported by the Central Bank of Yemen – Aden rose from 561 in March 2025 to 1,473 in January 2026 within its reporting scope. That is meaningful administrative evidence, but it does not tell us how many terminals were routinely working, how many unique merchants or customers used them, how reliable or costly the service was, or whether use was repeated. The count has not failed because it cannot answer those questions; it was not designed to.\n"
  "Programme baselines and targets are valuable management evidence. But a baseline is not a result, a target is not an achievement, and a programme-defined unit is not national prevalence.",
  "يجيب مسح Findex عن سؤال لا تستطيع الأنظمة الإدارية الإجابة عنه: ما نسبة الأشخاص في المجتمع الذي يغطيه المسح ممن يفيدون بامتلاك حساب وفق تعريف Findex؟ وحدود هذا الرقم ترافقه أينما ذُكر: فهو مسح مرجّح لا تعداد، ويستبعد إطاره مناطق يقطنها نحو 23% من السكان، واستُبدل أكثر من ربع وحدات المعاينة الأولية أثناء العمل الميداني، ولا يمكن توزيعه على المحافظات، وليس معدلًا لعام 2026.\n"
  "أما القواعد والسجلات المؤسسية فتثبت أن تعليمات صدرت، أو أن مؤسسة أُنشئت، أو أن خطوة في الحوكمة تمت. ولا تثبت التنفيذ الفعلي، ولا تجربة العملاء، ولا الاستخدام النشط، ولا النتائج.\n"
  "وبيانات البنية التحتية هي الأسرع تجددًا. فقد ارتفع عدد أجهزة نقاط البيع التي يبلغ عنها البنك المركزي اليمني – عدن من 561 في مارس 2025 إلى 1,473 في يناير 2026 ضمن نطاق إبلاغه. هذا دليل إداري مهم، لكنه لا يخبرنا كم جهازًا كان يعمل بانتظام، ولا كم تاجرًا أو عميلًا فريدًا استخدمها، ولا مدى موثوقية الخدمة أو كلفتها، ولا ما إذا تكرر الاستخدام. ولم يفشل هذا العدد لأنه لا يجيب عن تلك الأسئلة؛ فهو لم يُصمَّم للإجابة عنها.\n"
  "وتُعد خطوط الأساس والمستهدفات في البرامج أدلة إدارية قيّمة، لكن خط الأساس ليس نتيجة، والمستهدف ليس إنجازًا، ووحدة القياس في البرنامج ليست معدل انتشار وطنيًا."),
 ("interpretation_currentness", "There is no single date called “current”", "لا يوجد تاريخ واحد اسمه «الحالي»",
  "The better question is not “what is the latest number?” but “latest evidence of what?” Currentness is specific to the question. A newer administrative source can sit beside an older representative survey without contradiction, because they answer different questions.\n"
  "Whether change has reached people is itself a set of measurement questions: access, active use, quality, protection, persistence and outcomes. These are not automatic stages that follow from one another.",
  "السؤال الأفضل ليس «ما أحدث رقم؟» بل «أحدث دليل على ماذا؟». فحداثة الأدلة تتحدد بالسؤال. ويمكن لمصدر إداري أحدث أن يقف إلى جانب مسح ممثل أقدم من دون تناقض، لأنهما يجيبان عن سؤالين مختلفين.\n"
  "أما هل وصل التغيير إلى الناس فهو نفسه مجموعة من أسئلة القياس: الوصول، والاستخدام النشط، والجودة، والحماية، والاستمرار، والنتائج. وهي ليست مراحل يتبع بعضها بعضًا تلقائيًا."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A new representative measurement of people that keeps comparability on account ownership and adds:\n"
  "- active and repeated digital use;\n"
  "- saving and borrowing;\n"
  "- the purposes of payments;\n"
  "- barriers to opening an account;\n"
  "- affordability and reliability;\n"
  "- fraud and redress;\n"
  "- receipt and use of remittances;\n"
  "- gaps by gender and income;\n"
  "- geography and displacement, where statistically supportable;\n"
  "- persistence after programme participation or a transfer.\n"
  "Read alongside sharper administrative data on unique users, frequency, reliability, cost and complaints, it would not force survey and administrative data into one number. It would build the bridge between what changed in the system and what changed for people.",
  "قياس سكاني ممثل جديد يحافظ على قابلية المقارنة في امتلاك الحساب، ويضيف:\n"
  "- الاستخدام الرقمي النشط والمتكرر؛\n"
  "- الادخار والاقتراض؛\n"
  "- أغراض المدفوعات؛\n"
  "- عوائق فتح الحساب؛\n"
  "- القدرة على تحمل الكلفة وموثوقية الخدمة؛\n"
  "- الاحتيال والانتصاف؛\n"
  "- تلقي التحويلات واستخدامها؛\n"
  "- الفجوات بحسب الجنس والدخل؛\n"
  "- الجغرافيا والنزوح حيث يسمح الإحصاء بذلك؛\n"
  "- الاستمرار بعد المشاركة في برنامج أو تلقي تحويل.\n"
  "وإذا قُرئ إلى جانب بيانات إدارية أدق عن المستخدمين الفريدين والتكرار والموثوقية والكلفة والشكاوى، فلن يدمج بيانات المسح والبيانات الإدارية في رقم واحد، بل سيبني الجسر بين ما تغيّر في المنظومة وما تغيّر لدى الناس."),
],
},
# ---------------------------------------------------------------------------------------------------------------- 005
{
"reading_id": "CWR-005",
"disposition": "MERGE NARROWLY",
"title": ("When does digital growth become durable use?", "متى يتحول النمو الرقمي إلى استخدام مستمر؟"),
"question": None,
"thesis": ("Historical evidence from Yemen records a large base of e-money accounts by 2019 alongside dormancy, one-off use and a transaction mix still closely tied to cash. The open question is whether people choose to return to digital finance and find enough value to keep using it.",
           "تسجل الأدلة التاريخية في اليمن قاعدة كبيرة من حسابات النقود الإلكترونية بحلول 2019، إلى جانب الخمول والاستخدام العابر وتركيبة معاملات ما تزال مرتبطة ارتباطًا وثيقًا بالنقد. والسؤال المفتوح هو: هل يعود الناس إلى الخدمات المالية الرقمية باختيارهم، ويجدون فيها منفعة تكفي للاستمرار في استخدامها؟"),
"evidence_period": ("Provider data 2016–2019, from a 2020 study of five e-money providers",
                    "بيانات مقدمي الخدمة 2016–2019، من دراسة صدرت في 2020 عن خمسة من مقدمي خدمات النقود الإلكترونية"),
"prohibited_inference": ("Registrations, accounts, one-time use, transaction growth and infrastructure expansion do not prove unique, repeat, voluntary or durable financial use.",
                         "لا تثبت التسجيلات أو الحسابات أو الاستخدام لمرة واحدة أو نمو المعاملات أو توسع البنية استخدامًا فريدًا أو متكررًا أو طوعيًا أو مستمرًا."),
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-005"],
"domain_surface_routes": ["/payments/"],
"related_readings": ["CWR-010", "CWR-009"],
"measurement_bindings": ["MA-002"],
"featured": False,
"sections": [
 ("opening", None, None,
  "By December 2019, the five e-money providers covered by a study of the Institute of Banking Studies had 807,919 electronic-money accounts. The same study reports an average dormant or inactive share of 23%, and notes that some accounts were used only once, or because circumstances required it.\n"
  "This is not a paradox. The number of accounts establishes scale within the source universe. Dormancy and one-off use show why scale alone does not establish durable financial use.",
  "بحلول ديسمبر 2019، بلغ عدد حسابات النقود الإلكترونية لدى مقدمي الخدمة الخمسة الذين شملتهم دراسة معهد الدراسات المصرفية 807,919 حسابًا. وتذكر الدراسة نفسها أن متوسط نسبة الحسابات الخاملة أو غير النشطة بلغ 23%، وأن بعض الحسابات لم يُستخدم إلا مرة واحدة، أو استُخدم لأن الظروف فرضت ذلك.\n"
  "ليس في ذلك تناقض. فعدد الحسابات يثبت أن القناة الرقمية بلغت نطاقًا مهمًا داخل المجتمع الذي يغطيه المصدر، أما الخمول والاستخدام العابر فيبينان لماذا لا يثبت الحجم وحده استخدامًا ماليًا مستمرًا."),
 ("interpretation_relationship", "An account can exist without becoming a relationship", "قد يوجد الحساب من دون أن تنشأ علاقة مالية",
  "Registration does not tell us whether an account was used once or repeatedly, whether use was voluntary or triggered by a payment someone else made, whether value stayed in the account, whether the user paid or saved with it, or whether the service became preferable to cash for any purpose.",
  "لا يخبرنا التسجيل ما إذا كان الحساب قد استُخدم مرة واحدة أم بصورة متكررة، ولا ما إذا كان الاستخدام طوعيًا أم فرضته دفعة أرسلها طرف آخر، ولا ما إذا بقيت القيمة في الحساب، ولا ما إذا دفع المستخدم أو ادخر من خلاله، ولا ما إذا أصبحت الخدمة أفضل من النقد لأي غرض."),
 ("evidence_mix", "What the money moved for", "فيمَ تحركت الأموال",
  "CauseWay’s grouping of a 2019 transaction table in the same study indicates that 57.03% of recorded e-money transaction value was cash-in or cash-out and 29.97% was movement between bank and electronic accounts; bills and purchases together were 2.41%. The grouping is CauseWay’s, not a headline in the source.\n"
  "Cash-in and cash-out are not failed digital finance. Where moving value safely or easily is hard, that function has real economic use. But a system dominated by entry to and exit from cash tells us something different from repeated merchant, bill, saving or other digital use.",
  "يشير تجميع أجرته CauseWay لجدول معاملات 2019 في الدراسة نفسها إلى أن 57.03% من قيمة معاملات النقود الإلكترونية المسجلة ارتبط بإدخال النقد وسحبه، و29.97% بتحريك الأموال بين الحسابات المصرفية والإلكترونية، بينما بلغت الفواتير والمشتريات معًا 2.41%. والتجميع من إعداد CauseWay، وليس رقمًا رئيسيًا في المصدر.\n"
  "ولا يعني إدخال النقد وسحبه أن التمويل الرقمي فشل؛ ففي بيئة يصعب فيها تحريك القيمة بأمان أو بسهولة، لهذه الوظيفة منفعة اقتصادية حقيقية. لكن منظومة يغلب عليها الدخول إلى النقد والخروج منه تخبرنا بشيء مختلف عن الاستخدام الرقمي المتكرر للدفع للتجار أو سداد الفواتير أو الادخار."),
 ("interpretation_useful", "Useful before durable", "مفيد قبل أن يصبح مستمرًا",
  "The evidence supports neither extreme: that every new account proves inclusion, or that episodic use proves digital finance failed. A service can solve a real problem once and still not become a persistent financial relationship.\n"
  "The historical provider evidence also reports strong urban concentration and a low share of women within its own universe. These are not 2026 national estimates. Their present value is to show what current measurement must test: who uses digital finance, not merely how many accounts exist.",
  "لا تسند الأدلة أيًا من الطرفين: لا أن كل حساب جديد يثبت الشمول، ولا أن الاستخدام المتقطع يثبت فشل الخدمات المالية الرقمية. فقد تحل الخدمة مشكلة حقيقية مرة واحدة من دون أن تتحول إلى علاقة مالية مستمرة.\n"
  "وتشير أدلة مقدمي الخدمة التاريخية أيضًا إلى تركز قوي في المدن وحصة منخفضة للنساء داخل المجتمع الذي تغطيه. وهذه ليست تقديرات وطنية لعام 2026. قيمتها اليوم أنها تحدد ما ينبغي للقياس الحالي أن يختبره: من يستخدم الخدمات المالية الرقمية، لا عدد الحسابات الموجودة فحسب."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "Current data on unique active users, recency and frequency of use, what accounts are used for, value retained in the account, merchant and bill payments, dormancy, failed transactions, cost, complaints and provider-side behaviour, combined with demand-side questions on why people open an account, use it, return to it or stop. The measures that matter are registration, activity, recency, frequency, function, choice or trigger, quality and persistence, and they should not be read as an automatic ladder.\n"
  "> Scale tells us how large the digital system became. Return use tells us whether it entered financial life.",
  "بيانات حديثة عن المستخدمين الفريدين النشطين، وحداثة الاستخدام وتكراره، والأغراض التي تُستخدم لها الحسابات، والقيمة المحتفظ بها في الحساب، والمدفوعات للتجار وسداد الفواتير، والخمول، والمعاملات الفاشلة، والكلفة، والشكاوى، وسلوك مقدمي الخدمة، إلى جانب أسئلة من جانب الطلب عن سبب فتح الناس للحساب واستخدامهم له وعودتهم إليه أو توقفهم. والمقاييس المهمة هي التسجيل، والنشاط، وحداثة الاستخدام، وتكراره، ووظيفته، والاختيار أو الدافع، والجودة، والاستمرار، ولا ينبغي قراءتها سُلّمًا تلقائيًا.\n"
  "> حجم المنظومة الرقمية يخبرنا إلى أي مدى اتسعت، أما عودة المستخدم إليها فتخبرنا إن كانت قد دخلت حياته المالية."),
],
},
# ---------------------------------------------------------------------------------------------------------------- 006
{
"reading_id": "CWR-006",
"disposition": "MERGE NARROWLY (TITLE REPLACED)",
"title": ("What exactly do we mean by microfinance growth?", "ماذا نعني تحديدًا بنمو التمويل الأصغر؟"),
"question": None,
"thesis": ("Yemen’s microfinance record does not move on one axis. Borrower counts, saver or depositor measures, nominal portfolios and institutional form are not the same measure, and they do not yet form one harmonised growth series.",
           "لا يتحرك سجل التمويل الأصغر في اليمن على محور واحد. فأعداد المقترضين، ومقاييس المدخرين أو المودعين، والمحافظ الاسمية، والشكل المؤسسي ليست مقياسًا واحدًا، ولا تشكل حتى الآن سلسلة نمو موحدة."),
"evidence_period": ("Borrower, saver and portfolio observations for end-2015, end-2020 and 2023 · licensed-bank list checked on 7 September 2026",
                    "مشاهدات المقترضين والمدخرين والمحافظ لنهاية 2015 ونهاية 2020 وعام 2023 · قائمة البنوك المرخصة كما رُوجعت في 7 سبتمبر 2026"),
"prohibited_inference": ("Changes in saver or depositor counts, nominal portfolio or provider structure do not, on their own, establish broader inclusion, real credit deepening, market dominance, growth in unique people or improved borrower outcomes, and the borrower, saver and portfolio observations do not form one harmonised trend.",
                         "لا يثبت التغير في أعداد المدخرين أو المودعين، أو في المحفظة الاسمية، أو في هيكل مقدمي الخدمة، في حد ذاته اتساع الشمول أو تعمق الائتمان الحقيقي أو الهيمنة السوقية أو نمو عدد الأشخاص الفريدين أو تحسن نتائج المقترضين، ولا تشكل مشاهدات المقترضين والمدخرين والمحفظة اتجاهًا واحدًا موحدًا."),
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-006"],
"domain_surface_routes": ["/finance/", "/providers/"],
"related_readings": ["CWR-002", "CWR-003"],
"measurement_bindings": [],
"featured": False,
"sections": [
 ("opening", None, None,
  "“Microfinance growth” sounds like one result. The evidence describes several.\n"
  "Among providers reporting to the Social Fund for Development (SFD), verified primary tables record 93,118 active borrowers at end-2015 and 88,445 at end-2020. A 2024 policy paper citing SFD data reports 78,686 active borrowers at end-2023, but the set of providers behind that later point has not been verified against the earlier primary series. The observations are informative. They are not yet one continuous trend.",
  "تبدو عبارة «نمو التمويل الأصغر» كأنها نتيجة واحدة، لكن الأدلة تصف أكثر من نتيجة.\n"
  "فبين مقدمي الخدمة الذين يرفعون بياناتهم إلى الصندوق الاجتماعي للتنمية، تسجل الجداول الأولية المتحقق منها 93,118 مقترضًا نشطًا في نهاية 2015، و88,445 في نهاية 2020. وتورد ورقة سياسات صدرت في 2024، استنادًا إلى بيانات الصندوق، 78,686 مقترضًا نشطًا في نهاية 2023، لكن مجموعة مقدمي الخدمة التي تقف خلف هذه النقطة اللاحقة لم تُطابق بعد مع السلسلة الأولية الأقدم. هذه مشاهدات مفيدة، لكنها ليست بعدُ اتجاهًا واحدًا متصلًا."),
 ("evidence_borrowers", "Borrowers are one dimension", "المقترضون بُعد واحد",
  "The borrower record shows that the number of active borrowers can move differently from the financial volume that providers carry. The World Bank’s Financial Sector Diagnostics describe an active borrower base that stayed broadly around 80,000–90,000 through 2021 while average loan amounts rose. That supports a bounded historical reading: financial volume can expand without a comparable expansion in the number of active borrowers.\n"
  "It does not tell us why. Loan size, client mix, provider composition, inflation, currency conditions and reporting coverage may all matter, and the current evidence does not separate their effects.",
  "يبين سجل المقترضين أن عدد المقترضين النشطين قد يتحرك بصورة مختلفة عن الحجم المالي الذي تحمله المؤسسات. وتصف التشخيصات المالية للقطاع التي أعدها البنك الدولي قاعدةً من المقترضين النشطين ظلت عمومًا بين 80,000 و90,000 حتى 2021، بينما ارتفع متوسط مبالغ القروض. وهذا يسند قراءة تاريخية محدودة: قد يتوسع الحجم المالي من دون توسع مماثل في عدد المقترضين النشطين.\n"
  "لكنه لا يفسر السبب. فحجم القروض، وتركيبة العملاء، وتكوين مقدمي الخدمة، والتضخم، والظروف النقدية، ونطاق الإبلاغ قد تؤثر كلها، والأدلة الحالية لا تفصل بين آثارها."),
 ("evidence_savers", "Savers and depositors are another", "المدخرون والمودعون بُعد آخر",
  "The verified 2020 anchor records about 1.611 million savers or depositors. The same 2024 paper reports what it calls 3.3 million “active savers” in 2023.\n"
  "The two labels are not assumed to describe the same measure: the provider universe, the definition of an active saver and the de-duplication rule have not been harmonised across the evidence. The later figure therefore remains a bounded secondary observation. It is not 3.3 million unique people, and it is not a national savings rate.",
  "تسجل النقطة المتحقق منها لعام 2020 نحو 1.611 مليون مدخر أو مودع. وتورد الورقة نفسها الصادرة في 2024 ما تسميه 3.3 ملايين «مدخر نشط» في 2023.\n"
  "ولا نفترض أن التسميتين تصفان المقياس نفسه؛ فمجتمع مقدمي الخدمة، وتعريف المدخر النشط، وقاعدة إزالة الازدواج لم تُوحَّد عبر الأدلة. ولذلك يبقى الرقم اللاحق ملاحظة ثانوية محدودة الدلالة؛ فهو ليس 3.3 ملايين شخص فريد، وليس معدلًا وطنيًا للادخار."),
 ("evidence_portfolio", "Nominal portfolio is a third", "المحفظة الاسمية بُعد ثالث",
  "The verified 2020 record shows an outstanding portfolio of about YER 33.379 billion; the 2024 paper reports a nominal portfolio of about YER 44 billion for 2023. A larger nominal portfolio does not, on its own, establish deeper real credit. The evidence base holds no common price or exchange-rate treatment that would turn these nominal rials into one real series across Yemen’s divided monetary conditions, and it does not record which rial valuation each figure uses.\n"
  "The portfolio can be described as larger in nominal reported terms where the source supports it. It should not be presented as measured real financial deepening.",
  "يُظهر السجل المتحقق منه لعام 2020 محفظة قائمة بنحو 33.379 مليار ريال، وتورد ورقة 2024 محفظة اسمية تقارب 44 مليار ريال لعام 2023. ولا يثبت كبر المحفظة الاسمية وحده تعمقًا حقيقيًا في الائتمان؛ فقاعدة الأدلة لا تتضمن معالجة موحدة للأسعار أو لسعر الصرف تحوّل هذه القيم الاسمية بالريال إلى سلسلة حقيقية واحدة في ظل الانقسام النقدي في اليمن، ولا تسجل تقييم الريال الذي يستخدمه كل رقم.\n"
  "يمكن وصف المحفظة بأنها أكبر بالقيمة الاسمية المنشورة حيث يسند المصدر ذلك، ولا ينبغي تقديمها على أنها تعمق مالي حقيقي مقاس."),
 ("evidence_institutions", "Institutional form is a fourth", "الشكل المؤسسي بُعد رابع",
  "Institutional form matters too. The licensed-bank list of the Central Bank of Yemen – Aden, as checked on 7 September 2026, names 26 banks, 12 of which this resource classifies as microfinance banks from their names. A listing or licence establishes an institutional status. It does not establish current operation, geographic reach, client mix or outreach, so institutional change can matter without answering the inclusion question.",
  "والشكل المؤسسي مهم أيضًا. فقائمة البنوك المرخصة لدى البنك المركزي اليمني – عدن، كما رُوجعت في 7 سبتمبر 2026، تضم 26 بنكًا، يصنّف هذا المورد 12 منها بنوكَ تمويل أصغر استنادًا إلى أسمائها. ويثبت الإدراج أو الترخيص وضعًا مؤسسيًا، لكنه لا يثبت التشغيل الحالي ولا الانتشار الجغرافي ولا تركيبة العملاء ولا حجم الوصول؛ ولذلك قد يكون التغير المؤسسي مهمًا من دون أن يجيب عن سؤال الشمول."),
 ("interpretation_share", "A share of growth is not a share of the stock", "حصة من النمو ليست حصة من الرصيد",
  "A 2024 Sana’a Center paper attributes about 91% of saver growth over the period it analyses to Al-Kuraimi. That is a statement about the source of an increase. It is not, in this evidence base, a verified 2023 share of the total saver stock, and a later restatement that treats it as one is not used here. The case shows why the unit and the calculation base must travel with the number.",
  "تنسب ورقة لمركز صنعاء للدراسات الاستراتيجية صدرت في 2024 نحو 91% من نمو المدخرين خلال الفترة التي تحللها إلى بنك الكريمي. وهذه عبارة عن مصدر الزيادة، وليست، في قاعدة الأدلة الحالية، حصة محققة من إجمالي رصيد المدخرين في 2023؛ ولذلك لا تستخدم هذه القراءة إعادة عرض لاحقة تعاملها بوصفها حصة من الرصيد. والحالة مثال مباشر على ضرورة أن تبقى الوحدة وقاعدة الاحتساب ملازمتين للرقم."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "The defensible answer to “is microfinance growing?” is a set of separate questions rather than one sector growth rate. Did active borrowers increase? Did saver or depositor relationships expand under a stable definition? Did the nominal portfolio grow, and did average loan exposure change? Did provider structure change? Did any of this reach more unique people or firms, and did service quality or borrower outcomes improve? Different answers can coexist.\n"
  "Answering them needs a reconciled provider-level panel with stable definitions for unique active borrowers, unique active depositors or savers, balances and outstanding exposure, loan size, portfolio quality, geography, provider type, operating status, and complaints and customer outcomes, together with explicit rules for provider coverage, de-duplication, and prices or exchange rates when nominal values are compared over time.\n"
  "> If borrower counts, saver relationships, nominal portfolios and institutional form move differently, what exactly should we mean when we say microfinance is growing in Yemen?",
  "الإجابة القابلة للدفاع عن سؤال «هل ينمو التمويل الأصغر؟» مجموعة أسئلة منفصلة لا معدل نمو واحد للقطاع: هل زاد عدد المقترضين النشطين؟ هل اتسعت علاقات الادخار أو الإيداع وفق تعريف ثابت؟ هل كبرت المحفظة الاسمية، وهل تغير متوسط التمويل القائم لكل مقترض؟ هل تغير هيكل مقدمي الخدمة؟ وهل وصل أي من ذلك إلى عدد أكبر من الأشخاص أو المنشآت الفريدة، وهل تحسنت جودة الخدمة أو نتائج المقترضين؟ قد تختلف الإجابات وتتعايش معًا.\n"
  "وتتطلب الإجابة عنها لوحة بيانات موحدة على مستوى مقدمي الخدمة، بتعريفات ثابتة للمقترضين الفريدين النشطين، والمودعين أو المدخرين الفريدين النشطين، والأرصدة والتمويل القائم، وحجم القرض، وجودة المحفظة، والجغرافيا، ونوع مقدم الخدمة، وحالة التشغيل، والشكاوى ونتائج العملاء، مع قواعد صريحة لنطاق مقدمي الخدمة، وإزالة الازدواج، ومعالجة الأسعار أو سعر الصرف عند مقارنة القيم الاسمية عبر الزمن.\n"
  "> إذا تحركت أعداد المقترضين وعلاقات الادخار والمحافظ الاسمية والشكل المؤسسي في اتجاهات مختلفة، فما الذي نعنيه تحديدًا حين نقول إن التمويل الأصغر ينمو في اليمن؟"),
],
},
# ---------------------------------------------------------------------------------------------------------------- 007
{
"reading_id": "CWR-007",
"disposition": "MERGE NARROWLY",
"title": ("The gender gap is measured. Its explanation is still open.", "الفجوة بين النساء والرجال مقاسة. أما تفسيرها فما يزال مفتوحًا."),
"question": None,
"thesis": ("The latest Findex observation shows a large gap between women’s and men’s account ownership inside a system where few adults of either sex have an account. The evidence tells us where the disparity is. It does not yet tell us which barriers produce it.",
           "يُظهر أحدث قياس من مسح Findex فجوة كبيرة بين النساء والرجال في امتلاك الحساب، داخل منظومة لا يملك فيها حسابًا إلا قليل من البالغين من الجنسين. تخبرنا الأدلة أين يقع التفاوت، لكنها لا تخبرنا بعدُ أي العوائق تنتجه."),
"evidence_period": ("Global Findex, Yemen fieldwork 7 November 2022 – 9 January 2023",
                    "مسح Findex العالمي، العمل الميداني في اليمن 7 نوفمبر 2022 – 9 يناير 2023"),
"prohibited_inference": None,
"claim_bindings": ["CLM-002", "CLM-001", "CLM-025", "VIS-FINDEX-GAPS"],
"evidence_bindings": ["CLM-002", "CLM-001", "CLM-025", "VIS-FINDEX-GAPS"],
"verification_add": ["VIS-FINDEX-GAPS"],
"visual_bindings": ["RV-CWR-007"],
"domain_surface_routes": ["/people/"],
"related_readings": ["CWR-005", "CWR-004"],
"measurement_bindings": ["MA-003"],
"featured": False,
"sections": [
 ("opening", None, None,
  "In the latest Global Findex wave for Yemen, 18.35% of men and 5.44% of women aged 15 and over in the areas surveyed had an account, a gap of 12.91 percentage points. This is a valid comparison within one survey wave. It is a measured disparity, and it is not, by itself, an explanation.\n"
  "The gap also sits inside a low-access system. Overall account ownership in the same wave is 11.9%, and men’s measured level is low too. The sharper question is therefore:\n"
  "> Why does an already low-access financial system reach women so much less than men?\n"
  "That moves attention away from “fixing women” and towards the conditions under which access is produced.",
  "في أحدث موجة من مسح Findex العالمي في اليمن، كان لدى 18.35% من الرجال و5.44% من النساء في سن 15 عامًا فأكثر، في المناطق التي شملها المسح، حساب، بفجوة قدرها 12.91 نقطة مئوية. وهذه مقارنة سليمة داخل موجة مسح واحدة؛ إنها تفاوت مقاس، لكنها ليست في حد ذاتها تفسيرًا.\n"
  "وتقع الفجوة أيضًا داخل منظومة منخفضة الوصول أصلًا؛ إذ يبلغ امتلاك الحساب إجمالًا 11.9% في الموجة نفسها، ومستوى الرجال المقاس منخفض بدوره. ولذلك يصبح السؤال الأدق:\n"
  "> لماذا تصل منظومة مالية منخفضة الوصول أصلًا إلى النساء بدرجة أقل بكثير من الرجال؟\n"
  "وهذا ينقل الاهتمام من «إصلاح النساء» إلى الظروف التي يُنتَج فيها الوصول."),
 ("interpretation_mechanism", "The mechanism is still open", "الآلية ما تزال مفتوحة",
  "Plausible mechanisms include income, employment, identity documents, phone ownership and control, distance, mobility, trust, household decision-making, provider practice and product design. For Yemen these are hypotheses to test, not findings; the current evidence does not divide the 12.91-point gap among them.\n"
  "The same survey records a gap of about 9.0 percentage points between adults in the poorest 40% of households by income (6.5%) and those in the richest 60% (15.5%). That does not explain the gender gap. It shows why one-dimensional explanations are risky.",
  "من الآليات المحتملة: الدخل، والعمل، ووثائق الهوية، وامتلاك الهاتف والتحكم فيه، والمسافة، والقدرة على التنقل، والثقة، واتخاذ القرار داخل الأسرة، وممارسات مقدمي الخدمة، وتصميم المنتجات. وهذه في حالة اليمن فرضيات ينبغي اختبارها، لا نتائج؛ فالأدلة الحالية لا توزع فجوة الـ12.91 نقطة بين هذه الأسباب.\n"
  "ويسجل المسح نفسه فجوة تقارب 9.0 نقاط مئوية بين البالغين في أفقر 40% من الأسر بحسب الدخل (6.5%) وأغنى 60% (15.5%). وهذا لا يفسر الفجوة بين النساء والرجال، لكنه يبين لماذا تنطوي التفسيرات الأحادية على مخاطرة."),
 ("interpretation_journey", "Measure the journey, not only the endpoint", "قِس الرحلة، لا نقطة الوصول وحدها",
  "Account ownership is one point on a longer path. Better measurement would ask whether a woman can open an account, whether she controls the device and the account, whether she uses it and returns to it, what it costs her, whether it works, whether she can obtain redress, whether she decides how it is used, and whether it improves something she values.\n"
  "Provider data can follow the same path from the other side: applications, approvals, rejections, active use, dormancy, balances, credit, complaints, fraud, resolution and exit, each with a visible denominator.",
  "امتلاك الحساب نقطة واحدة على مسار أطول. والقياس الأفضل يسأل: هل تستطيع المرأة فتح حساب؟ وهل تتحكم في الجهاز والحساب؟ وهل تستخدمه وتعود إليه؟ وكم يكلفها؟ وهل يعمل؟ وهل تستطيع الحصول على انتصاف؟ وهل تقرر هي كيف يُستخدم؟ وهل يحسّن شيئًا تقدّره؟\n"
  "ويمكن لبيانات مقدمي الخدمة أن تتتبع المسار نفسه من الجهة الأخرى: الطلبات، والموافقات، وحالات الرفض، والاستخدام النشط، والخمول، والأرصدة، والائتمان، والشكاوى، والاحتيال، ومعالجتها، والخروج، مع إظهار قاعدة الاحتساب لكل منها."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A current representative survey design for Yemen that combines up-to-date sex-disaggregated measures of access, use, quality and protection; the variables that could explain the gap, collected in the same survey; comparisons among different groups of women; and provider-side customer funnels.\n"
  "> The gap tells us where to investigate. It does not tell us which intervention to choose.\n"
  "If we can measure the gap but cannot yet locate where women are being lost — at access, activation, use, persistence or quality — how can we know that an intervention is aimed at the right problem?",
  "تصميم مسح ممثل وحديث في اليمن يجمع مقاييس محدثة مصنفة بحسب الجنس للوصول والاستخدام والجودة والحماية، والمتغيرات التي قد تفسر الفجوة ضمن المسح نفسه، والمقارنات بين فئات مختلفة من النساء، ومسارات العملاء لدى مقدمي الخدمة.\n"
  "> الفجوة تحدد لنا أين ينبغي أن نبحث، لكنها لا تختار لنا التدخل.\n"
  "إذا كنا نستطيع قياس الفجوة، لكننا لا نعرف بعدُ أين تخرج النساء من المسار — عند الوصول أو التفعيل أو الاستخدام أو الاستمرار أو الجودة — فكيف نعرف أن التدخل موجَّه إلى المشكلة الصحيحة؟"),
],
},
# ---------------------------------------------------------------------------------------------------------------- 008
{
"reading_id": "CWR-008",
"disposition": "MERGE NARROWLY",
"title": ("How can 22% and 91.84% both be right?", "كيف تكون 22% و91.84% صحيحتين معًا؟"),
"question": ("In a 2022 survey of formal firms in seven governorates, how can 22% name access to finance as a business challenge while 91.84% of a filtered group rate it a major or moderate obstacle?",
             "في مسح أُجري عام 2022 للمنشآت الرسمية في سبع محافظات، كيف تذكر 22% منها الوصول إلى التمويل ضمن تحديات أعمالها، بينما تصفه 91.84% من مجموعة مصفّاة بأنه عائق كبير أو متوسط؟"),
"thesis": ("A 2022 survey of formal firms in seven selected governorates can tell us that finance was named less often than electricity or fuel, and also that finance was a severe obstacle for a narrower group of firms. The numbers do not contradict each other. They answer different questions.",
           "يمكن لمسح أُجري عام 2022 للمنشآت الرسمية في سبع محافظات مختارة أن يخبرنا بأن التمويل ذُكر أقل من الكهرباء والوقود ضمن تحديات الأعمال، وأنه كان في الوقت نفسه عائقًا شديدًا لدى مجموعة أضيق من المنشآت. لا يتناقض الرقمان؛ فكل منهما يجيب عن سؤال مختلف."),
"evidence_period": ("World Bank custom enterprise survey, September 2022, seven governorates · SMEPS programme report for 2024",
                    "مسح مخصص للمنشآت أجراه البنك الدولي في سبتمبر 2022 في سبع محافظات · تقرير وكالة تنمية المنشآت الصغيرة والأصغر لعام 2024"),
"prohibited_inference": None,
"claim_bindings": ["CLM-005", "CLM-006", "CLM-060", "CLM-062", "VIS-FIRM-CONSTRAINTS", "VIS-FIRM-FINANCE-PATH"],
"evidence_bindings": ["CLM-005", "CLM-006", "CLM-060", "CLM-062", "VIS-FIRM-CONSTRAINTS", "VIS-FIRM-FINANCE-PATH"],
"verification_add": ["CLM-062", "VIS-FIRM-CONSTRAINTS", "VIS-FIRM-FINANCE-PATH"],
"visual_bindings": ["RV-CWR-008"],
"domain_surface_routes": ["/firms/"],
"related_readings": ["CWR-003", "CWR-006"],
"measurement_bindings": ["MA-004"],
"featured": False,
"sections": [
 ("opening", None, None,
  "Among formal firms in a 2022 custom survey covering seven selected governorates, 22% named access to finance as a business challenge. In the same question, 50% named electricity, 46% fuel shortages, 32% transport or road blockades, 30% tax administration or tax rates and 27% political instability. Firms could name more than one challenge. Read alone, 22% makes finance look secondary.\n"
  "A separate tabulation in the same survey report excludes firms that said they did not need a loan. Among the firms that remain, 68.71% rate access to finance a major obstacle and 23.13% a moderate one: 91.84% together.\n"
  "Both figures can be right.\n"
  "> The denominator is not a footnote to the result. It is part of the result.",
  "بين المنشآت الرسمية في مسح مخصص أُجري عام 2022 وشمل سبع محافظات مختارة، أفادت 22% من المنشآت بأن الوصول إلى التمويل كان من بين التحديات التي تواجه أعمالها. وفي السؤال نفسه ذكرت 50% الكهرباء، و46% نقص الوقود، و32% النقل أو إغلاق الطرق، و30% إدارة الضرائب أو معدلاتها، و27% عدم الاستقرار السياسي. وكان بوسع المنشأة أن تذكر أكثر من تحدٍّ. وإذا قُرئت نسبة 22% وحدها، بدا التمويل مسألة ثانوية.\n"
  "لكن جدولًا آخر في تقرير المسح نفسه يستبعد المنشآت التي قالت إنها لا تحتاج إلى قرض. وبين المنشآت المتبقية، وصفت 68.71% الوصول إلى التمويل بأنه عائق كبير، و23.13% بأنه عائق متوسط، أي 91.84% مجتمعتين.\n"
  "يمكن أن يكون الرقمان صحيحين معًا.\n"
  "> قاعدة الاحتساب ليست حاشية على النتيجة؛ إنها جزء منها."),
 ("interpretation_denominators", "Two questions, two groups of firms", "سؤالان ومجموعتان من المنشآت",
  "The 22% is comparative. It places finance among electricity, fuel, transport, taxation and instability, following the survey’s own item wording; it is not the standard Enterprise Survey “biggest obstacle” indicator, and it does not rank constraints by cause. A loan does not make electricity reliable, and a guarantee does not reopen a road. Finance belongs inside the business environment, not above it.\n"
  "The 91.84% describes severity within a narrower, finance-relevant group. It does not mean that 91.84% of Yemeni firms, or even of the surveyed firms, face a major or moderate finance obstacle: the group changed before the percentage was calculated, and the number of firms in that tabulation is not held in the evidence base.",
  "نسبة 22% مقارنة؛ فهي تضع التمويل بين الكهرباء والوقود والنقل والضرائب وعدم الاستقرار، وفق صياغة البنود في المسح نفسه، وليست مؤشر «أكبر عائق» المعياري في مسوح المنشآت، ولا ترتب القيود بحسب أثرها السببي. فالقرض لا يجعل الكهرباء موثوقة، والضمان لا يعيد فتح طريق. التمويل جزء من بيئة الأعمال، لا فوقها.\n"
  "أما 91.84% فتصف شدة القيد داخل مجموعة أضيق معنية بالتمويل. ولا تعني أن 91.84% من المنشآت اليمنية، أو حتى من المنشآت التي شملها المسح، تواجه عائقًا تمويليًا كبيرًا أو متوسطًا؛ فالمجموعة تغيّرت قبل حساب النسبة، وعدد المنشآت في ذلك الجدول غير متوافر في قاعدة الأدلة."),
 ("evidence_funding", "How firms actually fund themselves", "كيف تموّل المنشآت نشاطها فعلًا",
  "The survey covered 328 formal firms. Of these, 31 reported a line of credit, and the question on loan sources has 18 valid responses; the evidence base does not show whether those 18 come from the 31. Counts this small can describe the responses. They cannot support national market-share claims.\n"
  "Working capital adds another layer. On average, formal firms reported financing working capital as follows: 69.12% from internal funds or retained earnings, 16.66% from money lenders, friends or relatives, 10.15% from advance payments by clients, 1.97% from non-bank financial institutions, 1.31% from supplier credit and 0.56% from banks. These are average shares, not shares of firms. The mix does not prove that every non-bank source hides unmet demand for bank credit, but it does show that formal bank finance plays a very small observed role in this survey’s working-capital mix.",
  "شمل المسح 328 منشأة رسمية، أفادت 31 منها بوجود خط ائتمان، ولسؤال مصادر القروض 18 استجابة صالحة؛ ولا تبين قاعدة الأدلة ما إذا كانت هذه الاستجابات الـ18 صادرة عن المنشآت الـ31. وأعداد بهذا الصغر تصف الاستجابات نفسها، لكنها لا تصلح أساسًا لادعاءات عن حصص سوقية وطنية.\n"
  "ويضيف رأس المال العامل طبقة أخرى. ففي المتوسط، أفادت المنشآت الرسمية بأنها موّلت رأس مالها العامل على النحو الآتي: 69.12% من الأموال الذاتية أو الأرباح المحتجزة، و16.66% من المقرضين غير الرسميين أو الأصدقاء أو الأقارب، و10.15% من دفعات مقدمة من العملاء، و1.97% من مؤسسات مالية غير مصرفية، و1.31% من ائتمان الموردين، و0.56% من البنوك. وهذه حصص متوسطة، لا نسب من المنشآت. ولا تثبت هذه التركيبة أن كل مصدر غير مصرفي يخفي طلبًا غير ملبى على الائتمان المصرفي، لكنها تبين أن التمويل المصرفي الرسمي يؤدي دورًا ضئيلًا جدًا في تركيبة رأس المال العامل التي سجلها هذا المسح."),
 ("context_constraints", "Constraints can be complements", "قد يكمل القيد قيدًا آخر",
  "Electricity and finance do not need to compete for first place. Finance can help a firm invest in resilience, inventory, equipment or energy; but if operating conditions destroy expected returns, available finance may remain unattractive. The interaction between them is the important economic question.\n"
  "Programme evidence adds another universe. SMEPS reports that 19% of the MSMEs it supported accessed financial services in 2024, and 15% over 2021–2024 against a 40% programme target. That is useful programme evidence, not a national MSME rate.",
  "لا حاجة إلى أن تتنافس الكهرباء والتمويل على المرتبة الأولى. فقد يساعد التمويل المنشأة على الاستثمار في قدرتها على الصمود أو في المخزون أو المعدات أو الطاقة؛ لكن إذا كانت ظروف التشغيل تقضي على العائد المتوقع، فقد يبقى التمويل المتاح غير مجدٍ. والتفاعل بين القيدين هو السؤال الاقتصادي المهم.\n"
  "وتضيف أدلة البرامج مجتمعًا آخر. إذ تفيد وكالة تنمية المنشآت الصغيرة والأصغر بأن 19% من المنشآت المتناهية الصغر والصغيرة والمتوسطة التي دعمتها وصلت إلى خدمات مالية في 2024، و15% خلال 2021–2024 مقابل مستهدف برامجي قدره 40%. وهذا دليل برامجي مفيد، لا معدل وطني."),
 ("why_it_matters", "Why it matters in Yemen", "لماذا يهم هذا في اليمن؟",
  "Two misreadings are tempting. One says 22% means finance is not a serious issue. The other says 91.84% means nearly all Yemeni firms are severely finance-constrained. Neither is supported.\n"
  "A stronger reading is that finance appears serious for an important subset of firms, while firms also face severe non-financial constraints and rely heavily on internal or non-bank sources. That changes the intervention question: for which firms, for what productive purpose, on what terms, and alongside which other constraints would additional finance unlock investment or resilience?",
  "ثمة قراءتان خاطئتان مغريتان: الأولى أن 22% تعني أن التمويل ليس مشكلة جادة، والثانية أن 91.84% تعني أن كل منشآت اليمن تقريبًا مقيدة تمويليًا بشدة. ولا تسند الأدلة أيًا منهما.\n"
  "والقراءة الأقوى أن التمويل يبدو قيدًا جادًا لدى شريحة مهمة من المنشآت، في حين تواجه المنشآت أيضًا قيودًا غير مالية شديدة وتعتمد اعتمادًا كبيرًا على مصادر داخلية أو غير مصرفية. وهذا يغيّر سؤال التدخل: لأي منشآت، ولأي غرض إنتاجي، وبأي شروط، وإلى جانب أي قيود أخرى، يمكن لتمويل إضافي أن يطلق الاستثمار أو يعزز القدرة على الصمود؟"),
 ("boundary", "Where the evidence stops", "أين يتوقف الدليل؟",
  "The survey covers formal firms in seven selected governorates, not all Yemeni firms. Its finance questions use different denominators, the loan-source table rests on 18 valid responses, and SMEPS reports on its own programme universe. None of this supports a current national rate of MSME access to finance, or a causal effect.",
  "يغطي المسح المنشآت الرسمية في سبع محافظات مختارة، لا جميع منشآت اليمن. وتستخدم أسئلته عن التمويل قواعد احتساب مختلفة، ويقوم جدول مصادر القروض على 18 استجابة صالحة، وتُبلغ الوكالة عن مجتمع برنامجها. ولا يسند شيء من ذلك معدلًا وطنيًا حاليًا لوصول المنشآت الصغيرة والمتوسطة إلى التمويل، ولا أثرًا سببيًا."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A current, representative measure of the firm-finance journey — need, demand, application or discouragement, approval, terms, source, use and outcome — linked to firm size, sector, formality, ownership, the owner’s sex where statistically supportable, geography and the other operating constraints firms face.\n"
  "> If firms can face severe financing constraints while facing even more immediate problems, and many fund operations without banks, what exactly should a successful firm-finance intervention be trying to unlock?",
  "قياس حديث وممثل لمسار تمويل المنشأة — الحاجة، والطلب، والتقدم بطلب أو الإحجام عنه، والموافقة، والشروط، والمصدر، والاستخدام، والنتيجة — مرتبطًا بحجم المنشأة وقطاعها ورسميتها وملكيتها، وجنس المالك حيث يسمح الإحصاء بذلك، والجغرافيا، وبقية قيود التشغيل التي تواجهها.\n"
  "> إذا كانت المنشأة قد تواجه قيدًا تمويليًا شديدًا وقيودًا أكثر إلحاحًا في الوقت نفسه، وكانت منشآت كثيرة تموّل نشاطها بعيدًا عن البنوك، فما الذي ينبغي أن يسعى تدخل ناجح في تمويل المنشآت إلى إطلاقه فعلًا؟"),
],
},
# ---------------------------------------------------------------------------------------------------------------- 009
{
"reading_id": "CWR-009",
"disposition": "ADOPT CANDIDATE",
"title": ("When does a payment reform become financial inclusion?", "متى يصبح إصلاح المدفوعات تحسنًا في الشمول المالي؟"),
"question": None,
"thesis": ("A rule can be issued, infrastructure can expand, institutions can be created and transactions can appear while evidence on reach, repeated use, service quality, protection and outcomes remains incomplete. The question is how far a reform’s effects can actually be traced.",
           "قد تصدر قاعدة جديدة، وتتوسع البنية التحتية، وتنشأ مؤسسات، وتظهر معاملات، بينما يظل ما نعرفه عن الوصول الفعلي والاستخدام المتكرر وجودة الخدمة والحماية والنتائج ناقصًا. والسؤال هو: إلى أي مدى نستطيع أن نتتبع آثار الإصلاح فعلًا؟"),
"evidence_period": ("POS counts March 2025 – January 2026 · institutional records June–August 2026 · project results framework January 2025",
                    "أعداد نقاط البيع مارس 2025 – يناير 2026 · سجلات مؤسسية يونيو–أغسطس 2026 · إطار نتائج المشروع يناير 2025"),
"prohibited_inference": None,
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-009"],
"domain_surface_routes": ["/payments/", "/reforms/"],
"related_readings": ["CWR-004", "CWR-010"],
"measurement_bindings": ["MA-010"],
"featured": False,
"sections": [
 ("opening", None, None,
  "Yemen’s payment system has changed. Official records document new rules, institutional steps, integration work, expanding reported infrastructure and transaction activity. POS terminals reported by the Central Bank of Yemen – Aden rose from 561 in March 2025 to 1,473 in January 2026 within its reporting scope. Between June and August 2026, its records also document further institution-building: integration work on the unified domestic money-transfer network, and the founding of the Yemeni Payments and Clearing Company.\n"
  "These are material developments, and they do not all prove the same thing.\n"
  "> A completed milestone tells us where implementation has reached. It does not tell us what changed downstream.",
  "تغيرت منظومة المدفوعات في اليمن. فالسجلات الرسمية توثق قواعد جديدة، وخطوات مؤسسية، وأعمال تكامل، وتوسعًا في البنية التحتية المبلغ عنها، ونشاطًا في المعاملات. وقد ارتفع عدد أجهزة نقاط البيع التي يبلغ عنها البنك المركزي اليمني – عدن من 561 جهازًا في مارس 2025 إلى 1,473 جهازًا في يناير 2026 ضمن نطاق إبلاغه. وبين يونيو وأغسطس 2026 توثق سجلاته أيضًا خطوات إضافية في بناء المؤسسات: أعمال تكامل الشبكة الموحدة للحوالات المالية الداخلية، وتأسيس الشركة اليمنية للمدفوعات والمقاصة.\n"
  "هذه تطورات مهمة، لكنها لا تثبت كلها الشيء نفسه.\n"
  "> يخبرنا الإنجاز المكتمل إلى أين وصل التنفيذ، لكنه لا يخبرنا بما تغيّر بعده."),
 ("interpretation_chain", "A reform passes through different evidence states", "يمر الإصلاح بحالات مختلفة من الدليل",
  "A payment reform can be followed along a chain:\n"
  "> rule or funding → implementation or institution → operation → reachable access → actual use → quality and protection → outcome\n"
  "Each link asks for different evidence. A legal instrument can establish that a rule exists. An institutional decision can establish that a company, a governance arrangement or an integration step was created. A technical launch can establish that a service became operational. Infrastructure counts can establish that acceptance devices or service points were reported, and transactions can establish activity. None of these, by itself, establishes population reach, repeated use, affordability, reliability, consumer protection or a financial outcome.\n"
  "The links can also move out of step. The Yemeni Payments and Clearing Company is an institution that has been established, not a system in operation, and the results framework of the World Bank-financed Financial Market Infrastructure and Inclusion Project recorded the fast payment system and the real-time gross settlement system as not yet operational in January 2025, with no later operational state recorded here.",
  "يمكن تتبع إصلاح المدفوعات عبر سلسلة:\n"
  "> قاعدة أو تمويل ← تنفيذ أو مؤسسة ← تشغيل ← وصول فعلي ← استخدام فعلي ← جودة وحماية ← نتيجة\n"
  "ولكل حلقة دليلها. فالأداة القانونية قد تثبت وجود القاعدة، والقرار المؤسسي قد يثبت إنشاء شركة أو ترتيب حوكمة أو خطوة تكامل، وبدء التشغيل التقني قد يثبت أن الخدمة أصبحت عاملة. وأعداد البنية التحتية قد تثبت أن أجهزة قبول أو نقاط خدمة جرى الإبلاغ عنها، والمعاملات قد تثبت وقوع نشاط. لكن أيًا من ذلك لا يثبت وحده الوصول السكاني، أو تكرار الاستخدام، أو القدرة على تحمل الكلفة، أو الموثوقية، أو حماية المستهلك، أو نتيجة مالية.\n"
  "وقد لا تسير الحلقات بالإيقاع نفسه. فالشركة اليمنية للمدفوعات والمقاصة مؤسسة أُنشئت، لا نظام قيد التشغيل، وقد سجل إطار النتائج في مشروع البنية التحتية للأسواق المالية والشمول المالي، الممول من البنك الدولي، نظامَ الدفع الفوري ونظامَ التسوية الإجمالية الفورية على أنهما غير عاملين بعد في يناير 2025، من دون حالة تشغيل لاحقة مسجلة هنا."),
 ("interpretation_measures", "Infrastructure and transactions answer their own questions", "البنية والمعاملات تجيب عن أسئلتها هي",
  "The rise in POS terminals is meaningful, but a terminal count is not a count of people. It does not tell us how many terminals were routinely working, how many unique merchants used them, how many unique customers paid through them, how reliable the service was, or whether the expansion changed financial behaviour. The series has not failed because it cannot answer those questions; it answers a different one.\n"
  "A recorded transaction brings us closer to use: it proves that activity occurred inside the reporting system. It does not tell us how many unique people used the service, whether they came back, what the transaction cost, whether it succeeded at the first attempt, what happened when it failed, whether complaints were resolved, or whether the service changed convenience, safety, resilience or productive activity.",
  "ارتفاع عدد أجهزة نقاط البيع مهم، لكن عدد الأجهزة ليس عددًا للأشخاص. فهو لا يخبرنا كم جهازًا كان يعمل بانتظام، ولا كم تاجرًا فريدًا استخدمها، ولا كم عميلًا فريدًا دفع من خلالها، ولا مدى موثوقية الخدمة، ولا ما إذا كان التوسع قد غيّر السلوك المالي. ولم تفشل هذه السلسلة لأنها لا تجيب عن تلك الأسئلة؛ فهي تجيب عن سؤال آخر.\n"
  "أما المعاملة المسجلة فتقربنا من الاستخدام، إذ تثبت أن نشاطًا وقع داخل النظام الذي يرصده. لكنها لا تخبرنا كم شخصًا فريدًا استخدم الخدمة، ولا هل عاد إليها، ولا كم كلفت المعاملة، ولا هل نجحت من المحاولة الأولى، ولا ماذا حدث عند فشلها، ولا هل عولجت الشكاوى، ولا هل غيّرت الخدمة شيئًا في الراحة أو الأمان أو القدرة على الصمود أو النشاط المنتج."),
 ("boundary", "Missing evidence is not evidence of failure", "غياب الدليل ليس دليلًا على الفشل",
  "The distinction works in both directions. It is wrong to call a new rail or regulation “financial inclusion” simply because it exists, and equally wrong to call a reform a failure because its downstream effects have not yet been measured. The accurate statement is narrower: the evidence has reached a particular stage, and the next stage remains open. That is a conclusion about the evidence, not a judgement on the reform.\n"
  "For each major reform or system change, monitoring should identify the furthest stage that is actually evidenced and then ask for the next missing link. A rule may be in place while implementation remains open; an institution may exist while operation remains open; operation may be proven while reach remains open; reach may be proven while repeated use remains open; use may be proven while reliability, cost or redress remain open; and service quality may be proven while household or firm outcomes remain open.",
  "يعمل هذا التمييز في الاتجاهين. فمن الخطأ أن نسمي نظام دفع أو لائحة جديدة «شمولًا ماليًا» لمجرد وجودهما، ومن الخطأ بالقدر نفسه أن نصف إصلاحًا بالفشل لأن آثاره اللاحقة لم تُقَس بعد. والصياغة الأدق أضيق: وصل الدليل إلى مرحلة محددة، وما بعدها ما يزال مفتوحًا للقياس. وهذه نتيجة عن حالة الدليل، لا حكم على الإصلاح.\n"
  "ولكل إصلاح رئيسي أو تغير في المنظومة، ينبغي أن تحدد المتابعة أبعد مرحلة أثبتتها الأدلة فعلًا، ثم تسأل عن أول حلقة مفقودة بعدها. فقد تكون القاعدة قائمة بينما يبقى التنفيذ مفتوحًا، وقد توجد المؤسسة بينما يبقى التشغيل مفتوحًا، وقد يثبت التشغيل بينما يبقى الوصول مفتوحًا، وقد يثبت الوصول بينما يبقى تكرار الاستخدام مفتوحًا، وقد يثبت الاستخدام بينما تبقى الموثوقية أو الكلفة أو الانتصاف مفتوحة، وقد تثبت جودة الخدمة بينما تبقى نتائج الأسر أو المنشآت مفتوحة."),
 ("why_it_matters", "Why it matters in Yemen", "لماذا يهم ذلك في اليمن؟",
  "The evidence clocks are not synchronised. Regulation, institution-building and administrative payment data can move faster than representative evidence about people. Fragmented authority, infrastructure constraints and different reporting universes make it especially risky to turn one operational signal into a national outcome, so the public record needs to keep the chain visible rather than compress it into a single word.",
  "لا تتجدد الأدلة بالإيقاع نفسه. فالتنظيم وبناء المؤسسات والبيانات الإدارية للمدفوعات قد تتقدم أسرع من الأدلة الممثلة عن الناس. كما أن تعدد السلطات وقيود البنية التحتية واختلاف مجتمعات الإبلاغ تجعل تحويل إشارة تشغيلية واحدة إلى نتيجة وطنية أمرًا بالغ الخطورة؛ ولذلك ينبغي أن يبقي السجل العام السلسلة ظاهرة بدل أن يختزلها في كلمة واحدة."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "For each major reform or rail, a connected set of measures covering operational status and coverage; participating institutions; reachable access; unique active users; recency and frequency of use; transaction success, failure, reversal and delay; the cost customers actually pay; complaints and redress; repeated use; and the outcome the reform is ultimately expected to affect. The data need not live in one system, but their definitions must connect without pretending that unlike measures are equivalent.\n"
  "> Measure forward from the last proven state, not backward from the outcome you hope to claim.",
  "لكل إصلاح أو نظام دفع رئيسي، مجموعة مترابطة من القياسات تغطي حالة التشغيل ونطاق التغطية، والمؤسسات المشاركة، والوصول الفعلي، والمستخدمين الفريدين النشطين، وحداثة الاستخدام وتكراره، ونجاح المعاملات وفشلها وعكسها وتأخرها، والكلفة التي يتحملها العميل فعلًا، والشكاوى والانتصاف، وتكرار الاستخدام، والنتيجة التي يُفترض أن يؤثر فيها الإصلاح في النهاية. ولا يلزم أن تجتمع هذه البيانات في نظام واحد، لكن تعريفاتها ينبغي أن تتصل من دون أن تُعامَل مقاييس غير متكافئة كأنها متكافئة.\n"
  "> ابدأ القياس من آخر مرحلة ثبتت بالأدلة، لا من النتيجة التي تأمل أن تعلنها."),
],
},
# ---------------------------------------------------------------------------------------------------------------- 010
{
"reading_id": "CWR-010",
"disposition": "MERGE NARROWLY",
"title": ("The payment arrived. What happened next?", "وصلت الدفعة. ماذا حدث بعدها؟"),
"question": ("When a cash transfer is paid into an account, what would show that the account became part of the recipient’s financial life?",
             "حين تُدفع تحويلة نقدية إلى حساب، ما الذي يثبت أن الحساب أصبح جزءًا من الحياة المالية للمستفيد؟"),
"thesis": ("Material on Yemen’s digital-payment pilot describes transfers paid into fully functional accounts, with recipient choice, for 45,460 recipients. That is an important step in delivery. It is not yet evidence that the accounts stayed part of recipients’ financial lives after the payments.",
           "تصف مواد تجربة الدفع الرقمي في اليمن دفع التحويلات إلى حسابات كاملة الوظائف، مع إتاحة الاختيار للمستفيدين، لصالح 45,460 مستفيدًا. وهذه خطوة مهمة في إيصال الدفعات، لكنها ليست بعدُ دليلًا على أن الحسابات بقيت جزءًا من الحياة المالية للمستفيدين بعد وصول الدفعات."),
"evidence_period": ("World Bank and G2Px material, May 2024 · reference period of the recipient figure not recorded",
                    "مواد البنك الدولي ومبادرة G2Px، مايو 2024 · الفترة المرجعية لعدد المستفيدين غير مسجلة"),
"prohibited_inference": ("A delivered payment, a recipient count or an opened account is not durable active use unless follow-up shows continued use, and immediate cash-out is not by itself evidence of failure.",
                         "لا تُعد الدفعة التي وصلت، ولا عدد المستفيدين، ولا الحساب المفتوح استخدامًا نشطًا مستمرًا ما لم تُظهر المتابعة استمرار الاستخدام، ولا يُعد السحب النقدي الفوري في حد ذاته دليلًا على الفشل."),
"claim_bindings": None, "evidence_bindings": None, "verification_add": [],
"visual_bindings": ["RV-CWR-010"],
"domain_surface_routes": ["/reforms/"],
"related_readings": ["CWR-005", "CWR-009"],
"measurement_bindings": ["MA-009"],
"featured": False,
"sections": [
 ("opening", None, None,
  "A transfer can succeed before a financial relationship begins. The intended recipient can be identified, the payment authorised and the funds delivered; the recipient can reach them; an account can be opened and made usable; and a programme can extend a new delivery channel into places where distributing cash is hard. Those are real results, and they should be measured and credited as such. Financial inclusion asks a different question: what happens after the money arrives?\n"
  "World Bank and G2Px material from May 2024 describes a digital-payment pilot within Yemen’s unconditional cash-transfer programme in eight districts, reported by programme partners to have benefited 45,460 recipients. The pilot emphasised payment into fully functional accounts and recipient choice. That goes beyond a change in disbursement technology. A fully functional account can, by design, receive money, hold value and make payments; and choice matters because a system built around recipients should not treat them as passive receivers of a programme payment.\n"
  "But possibility is not persistence. The available Yemen evidence does not yet tell us whether recipients used those accounts between transfers, kept balances in them, received other money, paid merchants or bills, made transfers of their own, switched providers, or kept using the account after the programme payments that prompted it weakened or ended. That is the missing observation.",
  "قد تنجح عملية التحويل قبل أن تبدأ علاقة مالية. فيمكن تحديد المستفيد المقصود، واعتماد الدفعة، وإيصال الأموال، وتمكين المستفيد من الوصول إليها، وفتح حساب صالح للاستخدام، وتوسيع قناة صرف جديدة إلى أماكن يصعب فيها توزيع النقد. وهذه نتائج حقيقية ينبغي قياسها والاعتراف بها كما هي. أما الشمول المالي فيطرح سؤالًا آخر: ماذا يحدث بعد وصول المال؟\n"
  "تصف مواد البنك الدولي ومبادرة G2Px الصادرة في مايو 2024 تجربة للدفع الرقمي ضمن برنامج التحويلات النقدية غير المشروطة في اليمن، نُفذت في ثماني مديريات، وأفاد شركاء البرنامج بأنها شملت 45,460 مستفيدًا. وركزت التجربة على الدفع إلى حسابات كاملة الوظائف وعلى حرية المستفيد في الاختيار. وهذا يتجاوز مجرد تغيير أداة الصرف؛ فالحساب الكامل الوظائف يستطيع، من حيث التصميم، أن يستقبل الأموال ويحتفظ بالقيمة ويُجري المدفوعات، والاختيار مهم لأن نظامًا يضع المستفيد في مركزه لا ينبغي أن يعامله متلقيًا سلبيًا لدفعة برنامجية.\n"
  "لكن الإمكانية لا تعني الاستمرار. فالأدلة المتاحة عن اليمن لا تخبرنا بعدُ ما إذا كان المستفيدون قد استخدموا هذه الحسابات بين دفعة وأخرى، أو أبقوا فيها أرصدة، أو تلقوا فيها أموالًا من خارج البرنامج، أو دفعوا منها لتجار أو سددوا فواتير، أو أجروا تحويلات بمبادرتهم، أو بدّلوا مقدم الخدمة، أو واصلوا استخدام الحساب بعد أن ضعفت دفعات البرنامج التي دفعتهم إليه أو انتهت. وهذه هي الملاحظة المفقودة."),
 ("interpretation_results", "Delivery and inclusion are different results", "إيصال الدفعة والشمول المالي نتيجتان مختلفتان",
  "A digital cash-transfer programme may improve delivery even if recipients later withdraw most or all of each transfer in cash. Immediate cash-out can be rational: local merchants may prefer cash, acceptance networks may be thin, liquidity may be uncertain, and fees, distance, reliability, trust or familiarity may make cash the better instrument for immediate needs. Cash-out should not automatically be labelled failure, and account opening should not automatically be labelled inclusion.\n"
  "It is more useful to report three families of results separately:\n"
  "- Delivery: was the right payment made to the right person, safely, accurately and on time?\n"
  "- Access to a usable account: did the recipient obtain a genuinely functional account, on terms they could understand, with a meaningful choice?\n"
  "- Persistent use: did the account keep a role in the recipient’s financial life between or after programme payments?\n"
  "Each can improve while another remains unmeasured.",
  "قد يحسّن برنامج رقمي للتحويلات النقدية طريقةَ إيصال الدفعة حتى لو سحب المستفيدون معظم كل تحويلة أو كلها نقدًا بعد ذلك. والسحب الفوري قد يكون قرارًا رشيدًا: فقد يفضل التجار المحليون النقد، وقد تكون شبكة القبول محدودة، والسيولة غير مضمونة، وقد تجعل الرسوم أو المسافة أو ضعف الموثوقية أو نقص الثقة أو قلة الألفة النقدَ الأداة الأنسب للحاجات العاجلة. لذلك لا ينبغي وصف السحب النقدي بالفشل تلقائيًا، ولا وصف فتح الحساب بالشمول تلقائيًا.\n"
  "والأجدى أن تُعرض ثلاث مجموعات من النتائج كلٌّ على حدة:\n"
  "- إيصال الدفعة: هل وصلت الدفعة الصحيحة إلى الشخص المقصود بأمان ودقة وفي موعدها؟\n"
  "- إتاحة حساب قابل للاستخدام: هل حصل المستفيد على حساب يعمل فعلًا، بشروط يفهمها، ومع اختيار له معنى؟\n"
  "- الاستخدام المستمر: هل احتفظ الحساب بدور في الحياة المالية للمستفيد بين الدفعات أو بعدها؟\n"
  "قد يتحسن أحد هذه الجوانب بينما يبقى غيره غير مقاس."),
 ("evidence_between_payments", "The period between payments may tell us most", "قد تكون الفترة بين دفعتين أكثر ما يخبرنا",
  "A payment-day metric tells us whether the programme worked on payment day. Persistence runs on another clock. Useful questions include:\n"
  "- Was the account still active a month, three months, six months and a year later?\n"
  "- Was it used between transfer cycles?\n"
  "- Did money from outside the programme enter the account?\n"
  "- Was some value kept rather than withdrawn at once?\n"
  "- Did the recipient pay a merchant or a bill from it, or start a transfer?\n"
  "- Was it used after the programme payments ended?\n"
  "- Did the recipient stay with the provider, switch or stop?\n"
  "- What happened when a transaction failed or a complaint was made?\n"
  "- What did using the account cost in money, time and travel?\n"
  "The aim is not to expect every cash-transfer recipient to become a frequent user of digital finance. It is to find out whether the new channel created an option of lasting value, and for whom.",
  "مؤشر يوم الصرف يخبرنا إن كان البرنامج قد نجح في يوم الصرف، أما الاستمرار فيُقاس بتوقيت آخر. ومن الأسئلة المفيدة:\n"
  "- هل ظل الحساب نشطًا بعد شهر، ثم بعد ثلاثة أشهر وستة أشهر وسنة؟\n"
  "- هل استُخدم بين دورات التحويل؟\n"
  "- هل دخلته أموال من خارج البرنامج؟\n"
  "- هل احتُفظ بجزء من القيمة بدل سحبها فورًا؟\n"
  "- هل دفع المستفيد منه لتاجر أو سدد فاتورة، أو بادر بتحويل؟\n"
  "- هل استُخدم بعد انتهاء دفعات البرنامج؟\n"
  "- هل بقي المستفيد مع مقدم الخدمة، أم انتقل إلى غيره، أم توقف؟\n"
  "- ماذا حدث عند فشل معاملة أو تقديم شكوى؟\n"
  "- كم كلّف استخدام الحساب من مال ووقت وانتقال؟\n"
  "ليس الهدف أن يصبح كل متلقٍّ لتحويل نقدي مستخدمًا كثيفًا للخدمات المالية الرقمية، بل أن نعرف إن كانت القناة الجديدة قد أوجدت خيارًا ماليًا ذا قيمة مستمرة، ولمن."),
 ("interpretation_choice", "Choice matters only if it can be exercised", "لا معنى للاختيار ما لم يمكن ممارسته",
  "The pilot’s emphasis on recipient choice is analytically important. Whether an account can become more than a payment channel depends on design features such as a real choice of provider, a fully functional account, reachable access points, clear terms and the ability to use the account beyond the programme payment.\n"
  "But choice written into a programme design is not necessarily choice experienced by recipients. Exercising it needs viable providers or channels, understandable fees, usable access points, control of credentials, reliable service and a practical ability to switch. So the measurement question is not only whether choice was offered, but whether recipients could exercise it without risking their access to the payment.",
  "لتركيز التجربة على اختيار المستفيد أهمية تحليلية. فإمكان أن يصبح الحساب أكثر من قناة لتلقي الدفعة يتوقف على عناصر في التصميم، مثل الاختيار الفعلي لمقدم الخدمة، والحساب الكامل الوظائف، ونقاط الوصول القريبة، ووضوح الشروط، وإمكان استخدام الحساب خارج دفعة البرنامج.\n"
  "لكن الاختيار المكتوب في تصميم البرنامج ليس بالضرورة اختيارًا عاشه المستفيدون. فممارسته تحتاج إلى مقدمي خدمة أو قنوات بديلة قابلة للاستخدام، ورسوم مفهومة، ونقاط وصول عملية، وتحكّم في بيانات الدخول، وخدمة موثوقة، وقدرة عملية على الانتقال. ولذلك لا يقتصر سؤال القياس على ما إذا كان الاختيار قد أُتيح، بل يشمل ما إذا استطاع المستفيدون ممارسته من دون المخاطرة بوصولهم إلى الدفعة."),
 ("boundary", "Where the evidence stops", "أين يتوقف الدليل؟",
  "The current evidence does not establish that Yemen’s pilot produced persistent use. It does not establish that cashing out was irrational or undesirable, or that paying transfers digitally automatically improves household resilience, women’s agency or financial health. And it does not establish that the pilot failed simply because those later outcomes have not been measured. The 45,460 figure counts recipients reported by the programme, not people who kept using an account.\n"
  "> The pilot provides evidence of movement toward digital delivery and of recipients being given usable accounts. Whether that became a durable financial relationship is a separate empirical question.",
  "لا تثبت الأدلة الحالية أن تجربة اليمن أنتجت استخدامًا مستمرًا. ولا تثبت أن السحب النقدي كان سلوكًا غير رشيد أو غير مرغوب، ولا أن صرف التحويلات رقميًا يحسّن تلقائيًا قدرة الأسر على الصمود أو تمكين النساء أو الصحة المالية. كما لا تثبت أن التجربة فشلت لمجرد أن هذه النتائج اللاحقة لم تُقَس بعد. ورقم 45,460 يعدّ المستفيدين كما أبلغ عنهم البرنامج، لا الأشخاص الذين واصلوا استخدام حساب.\n"
  "> تقدم التجربة دليلًا على التقدم نحو الصرف الرقمي وعلى إتاحة حسابات قابلة للاستخدام للمستفيدين، أما تحوّل ذلك إلى علاقة مالية مستمرة فسؤال تجريبي مستقل."),
 ("what_would_change", CHANGE_H[0], CHANGE_H[1],
  "A longitudinal follow-up of recipients, linked where appropriate and safely possible to administrative payment data. At minimum it would distinguish payment success, account activation, the timing of cash-out, activity between transfers, activity a month, three months, six months and a year later, balances kept, deposits from outside the programme, payments and transfers the recipient starts, switching provider, dormancy, complaints, failed or reversed transactions, fees, the cost in travel and time, control of the account, and use after the transfers end. It should then ask recipients why they used, returned, switched or stopped.\n"
  "> If the account disappears from the recipient’s financial life between one payment and the next, did digitisation change the delivery channel, or did it change the financial relationship?",
  "متابعة طولية للمستفيدين، تُربط ببيانات الدفع الإدارية حيثما كان ذلك مناسبًا وممكنًا بأمان. وينبغي أن تميز، على الأقل، بين نجاح الدفع، وتفعيل الحساب، وتوقيت السحب النقدي، والنشاط بين الدفعات، والنشاط بعد شهر وثلاثة أشهر وستة أشهر وسنة، والأرصدة المحتفظ بها، والإيداعات من خارج البرنامج، والمدفوعات والتحويلات التي يبادر بها المستفيد، والانتقال إلى مقدم خدمة آخر، والخمول، والشكاوى، والمعاملات الفاشلة أو المعكوسة، والرسوم، وكلفة الانتقال والوقت، والتحكم في الحساب، والاستخدام بعد انتهاء التحويلات. ثم ينبغي أن نسأل المستفيدين أنفسهم: لماذا استخدموا الحساب، ولماذا عادوا إليه، أو انتقلوا عنه، أو توقفوا؟\n"
  "> إذا اختفى الحساب من الحياة المالية للمستفيد بين دفعة وأخرى، فهل غيّرت الرقمنة قناة الصرف فقط، أم غيّرت العلاقة المالية نفسها؟"),
],
},
]

# /readings/ index (02 title + 03 section 1): the family definition supplied by the programme owner, verbatim.
INDEX = {
    "title": ("Evidence Readings", "قراءات الأدلة"),
    "definition": ("Evidence-led essays on the points where Yemen’s financial-inclusion data change the question—not just the answer. Each Reading is traceable to the evidence behind it.",
                   "قراءات تحليلية تنطلق من الأدلة عند النقاط التي تغيّر فيها بيانات الشمول المالي في اليمن السؤال نفسه، لا الإجابة فقط. ويمكن تتبّع كل قراءة إلى الأدلة التي قامت عليها."),
}

# 11 Reading-visual parity (BIL-05) and wording aligned to the accepted Readings.
VISUALS = [
    ("RV-CWR-001", "accessible_summary_ar", "ثم أعاد تقرير 2025 عرض السنة نفسها بقيمة 3,422.16 مليون دولار", "ثم أعاد تقرير 2025 عرض عام 2024 نفسه بقيمة 3,422.16 مليون دولار"),
    ("RV-CWR-002", "what_it_shows_ar", "يعرض الأوضاع المصرفية المرجعية نفسها كما نُشرت في نسخ مختلفة", "يعرض المراكز المصرفية لعام 2022 نفسها كما نُشرت في نسخ مختلفة"),
    ("RV-CWR-005", "title_ar", "نمو الحسابات لا يساوي استخدامًا رقميًا مستدامًا", "نمو الحسابات لا يساوي استخدامًا رقميًا مستمرًا"),
    ("RV-CWR-010", "prohibited_inference_ar", "استخدامًا نشطًا مستدامًا", "استخدامًا نشطًا مستمرًا"),
]

# 04 governed interface copy for the Reading family (new rows) — (ui_id, label_en, label_ar, use_rule)
UI_NEW = [
    ("UI-READING-EYEBROW", "Evidence Reading", "قراءة أدلة", "Eyebrow above a Reading title (Reading page, featured Reading)."),
    ("UI-READING-EVIDENCE-PERIOD", "Evidence period", "فترة الأدلة", "Label of the Reading's governed evidence period (08 evidence_period)."),
    ("UI-READING-LAST-REVIEWED", "Last reviewed", "آخر مراجعة", "Label of the Reading's governed review date (08 last_reviewed)."),
    ("UI-READING-DO-NOT-INFER", "Do not infer", "لا يُستنتج", "Label of the Reading's governed prohibited inference (08)."),
    ("UI-READING-TRACE-H", "Trace the evidence", "تتبّع الأدلة", "Heading of the Reading's evidence path, after 'What would change this reading?'."),
    ("UI-READING-RELATED-H", "Related readings", "قراءات ذات صلة", "Heading of the one or two governed related Readings (08 related_readings)."),
    ("UI-READING-FEATURED", "Featured Reading", "قراءة مختارة", "Label of the one governed featured Reading (08 featured) on Home, Explore and the Readings index."),
    ("UI-READING-OPEN", "Read this Reading", "اقرأ هذه القراءة", "Link from the featured Reading to its page."),
    ("UI-READING-ALL-H", "All Evidence Readings", "كل قراءات الأدلة", "Heading of the editorial list on the Readings index; link label to the index elsewhere."),
    ("UI-EXPLORE-GO-DEEPER", "Go deeper", "تعمّق في التحليل", "Heading of the single Explore pointer to the featured Reading."),
    ("UI-EVIDENCE-USED-IN-READINGS", "Used in these Evidence Readings", "يُستخدم هذا الدليل في قراءات الأدلة الآتية", "Evidence Record: the Readings whose evidence path includes this record (derived from 08)."),
    ("UI-MEASUREMENT-EXAMINED-IN", "This gap is examined in", "تناقش هذه الفجوة في", "Measurement Agenda: the Readings bound to this priority (08 measurement_bindings)."),
]
