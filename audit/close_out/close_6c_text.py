# -*- coding: utf-8 -*-
"""CLOSE-6C: the review pair's changes to the CWR-012 draft, as exact edits (audit/close_out/addendum/REDTEAM_6C.md,
ARABIC_6C.md). Each EDIT must match its field exactly once; SET replaces a whole field. English and Arabic change together.

Red-team blockers: B1 (no "informal" transfers through licensed providers), B2 ("more … than", not "mainly", with the
2014 channel shares stated as they are), B3 (CBY-Aden's balance of payments is not "the economy as a whole"; its territory
is unmapped). Should-fix: S1 (other routes; explanations and limits), S2 (providers, not "the network"), S3 (the June 2024
domestic-transfer rule, bound through VIS-PAYMENT-RAILS), S4 (the roster's scope), S7/S8 (the CCY rankings and "hawala"
as the study's word), S13 (both corridors). Nits N1, N2, N4, N5, N6, N10, N11. Arabic: M1–M3, S2–S6, N1–N3.
"""

THESIS_EN = ("In Yemen’s Global Findex 2021 wave, 31.9% of adults in surveyed areas received domestic remittances, while 11.9% of "
             "adults in those areas had an account. That is consistent with the hypothesis that money sent between people moves "
             "more through exchange companies and other money-transfer providers than through accounts, but it is a hypothesis: "
             "the survey counts adults, not households, its values here cover transfers within Yemen only, and no channel value "
             "for that wave is held here. Other routes and humanitarian cash fit the same numbers, and survey coverage, currency "
             "and the meaning of “remittance” limit what they show.")
THESIS_AR = ("في موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) الخاصة باليمن، تلقى 31.9% من البالغين في المناطق التي "
             "شملها المسح حوالات محلية، في حين كان لدى 11.9% من البالغين في تلك المناطق حساب. ويتسق ذلك مع فرضية أن الأموال "
             "المرسلة بين الأفراد تنتقل عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال أكثر مما تنتقل عبر الحسابات، لكنه "
             "يبقى فرضية: فالمسح يعدّ البالغين لا الأسر، ولا تغطي قيمه الواردة هنا إلا الحوالات داخل اليمن، ولا تتضمن قاعدة "
             "الأدلة أي قيمة لقنوات الحوالات في تلك الموجة. وتنسجم الطرق الأخرى والمساعدات النقدية الإنسانية مع الأرقام نفسها، "
             "وتحدّ تغطيةُ المسح والعملةُ ومعنى «الحوالة» مما تُظهره.")

S4_EN = ("The evidence is consistent with a hypothesis: that transfers from relatives and friends are a main channel through which "
         "many households receive cash, and that this money moves more through exchange companies and other money-transfer "
         "providers than through accounts. A larger share of adults received domestic remittances than had an account; in 2014, "
         "31.1% of recipients named a money transfer operator and 2.0% a financial institution, and the profile held here does "
         "not show how the others received money; and CBY-Aden lists exchange companies, exchange establishments and remittance "
         "agents as separate licensed classes. This Reading states that as a hypothesis. No source here measures what share of "
         "household cash comes from transfers, or how often transfers arrive. A money transfer operator in the survey is not "
         "necessarily an exchange company, a roster entry does not by itself show that a provider operates now, and the survey "
         "values do not show whether the adults who received money were those without an account.")
S4_AR = ("تتسق الأدلة مع فرضية مفادها أن الأموال التي يرسلها الأقارب والأصدقاء قناة رئيسية تتلقى عبرها أسر كثيرة النقد، وأن هذه "
         "الأموال تنتقل عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال أكثر مما تنتقل عبر الحسابات. فنسبة البالغين الذين "
         "تلقوا حوالات محلية أعلى من نسبة من يملكون حسابًا؛ وفي 2014 ذكر 31.1% من المتلقين مشغل تحويل أموال، و2.0% مؤسسة "
         "مالية، ولا يبيّن الملف الوارد في قاعدة الأدلة هذه كيف تلقى الباقون أموالهم؛ ويُدرج البنك المركزي اليمني – عدن شركات الصرافة ومنشآت "
         "الصرافة ووكلاء الحوالات فئاتٍ مرخّصة مستقلة. وتطرح هذه القراءة ذلك فرضيةً. فلا يقيس أي مصدر هنا حصة الحوالات من النقد "
         "الذي تتلقاه الأسر، ولا عدد مرات وصولها. ومشغل تحويل الأموال في المسح ليس بالضرورة شركة صرافة، والقيد في القائمة لا "
         "يُثبت وحده أن مقدم الخدمة يعمل حاليًا، ولا تُظهر قيم المسح ما إذا كان البالغون الذين تلقوا الأموال هم أنفسهم من لا "
         "يملكون حسابًا.")

# The humanitarian-cash sentence that replaces the draft's "not yet held" sentence in s5 (S7, S8; Arabic M3).
HUM_EN = ("Two Cash Consortium of Yemen studies of aid recipients show how large that route can be where it operates: in three "
          "areas surveyed in June 2024, the assistance made up most of the recipients’ cash income, loans from informal networks "
          "came second in two of the three areas, and gifts were the smallest share in all three; and in the other study’s "
          "sample, in selected villages of Ad-Dali and Ja’ar, some respondents did not count money received by “hawala” (the "
          "study’s word) as income. Both studies cover aid recipients only and record no channel for money moving between "
          "households, so they neither confirm nor overturn the hypothesis.")
HUM_AR = ("وتُظهر دراستان لتحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات ما قد يبلغه حجم هذا الطريق حيث "
          "يعمل: ففي ثلاث مناطق شملها مسح في يونيو 2024 شكّلت المساعدات معظم الدخل النقدي للمستفيدين، وجاءت القروض من الشبكات "
          "غير الرسمية ثانيةً في منطقتين من الثلاث، وكانت الهدايا أصغر الحصص فيها جميعًا؛ وفي عينة الدراسة الأخرى، في قرى "
          "مختارة من الضالع وجعار، لم يحتسب بعض المستجيبين ما تلقوه عن طريق «الحوالة» (بتعبير الدراسة) دخلًا. وتقتصر الدراستان "
          "على متلقي المساعدات، ولا تسجلان أي قناة لانتقال المال بين الأسر، فهما لا تؤكدان الفرضية ولا تنقضانها.")

# (target, field) -> whole new value. target "reading" is the 08 row; an int is the section order.
SET = {
    ("reading", "question_en"): "Does money sent between people in Yemen reach households more through exchange companies than "
                                "through accounts?",
    ("reading", "question_ar"): "هل تصل الأموال المرسلة بين الأفراد في اليمن إلى الأسر عبر شركات الصرافة أكثر مما تصل عبر الحسابات؟",
    ("reading", "thesis_en"): THESIS_EN,
    ("reading", "thesis_ar"): THESIS_AR,
    (1, "body_en"): THESIS_EN,
    (1, "body_ar"): THESIS_AR,
    ("reading", "evidence_period_en"):
        "Global Findex 2021, Yemen fieldwork November 2022 – January 2023 · World Bank country profile for 2014 · CBY-Aden "
        "roster for 2026 · CBY-Aden domestic-transfer rule of June 2024 · remittance prices for 2023 and 2025 Q3 · CBY-Aden "
        "annual reports 2024 and 2025 · Cash Consortium of Yemen studies of aid recipients (survey data of January and June "
        "2024)",
    ("reading", "evidence_period_ar"):
        "المؤشر العالمي للشمول المالي (Global Findex) 2021، العمل الميداني في اليمن نوفمبر 2022 – يناير 2023 · الملف القطري "
        "للبنك الدولي لعام 2014 · قائمة البنك المركزي اليمني – عدن لعام 2026 · قرار البنك المركزي اليمني – عدن بشأن الحوالات الداخلية الصادر في يونيو 2024 · أسعار الحوالات لعام 2023 والربع الثالث من 2025 · التقريران السنويان للبنك المركزي "
        "اليمني – عدن 2024 و2025 · دراستا تحالف النقد في اليمن (Cash Consortium of Yemen) عن متلقي المساعدات (بيانات مسوح "
        "يناير ويونيو 2024)",
    (3, "heading_en"): "The channel evidence is old, and providers are listed, not measured",
    (3, "heading_ar"): "أدلة القنوات قديمة، ومقدمو الخدمة مُدرجون في قوائم لا مَقيسون",
    (4, "body_en"): S4_EN,
    (4, "body_ar"): S4_AR,
    (5, "heading_en"): "Other explanations and limits",
    (5, "heading_ar"): "تفسيرات أخرى وحدود للأدلة",
}

# (target, field, old, new): old must occur exactly once in the field as the draft (CR-21 and HUM applied) holds it.
EDITS = [
    # s2: N2; Arabic M2
    (2, "body_en", "Each is a share of all adults, from a separate question, so the figures",
     "Each is a share of all adults, from its own question or, for “either”, from the two combined, so the figures"),
    (2, "body_ar", "لكن المسح لا يبيّن كيف وصلت تلك الأموال", "لكن المسح لا يبيّن كيف انتقلت تلك الأموال"),
    (2, "body_ar", "ففي موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) الخاصة باليمن، التي نُفّذ عملها الميداني",
     "ففي موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) التابع للبنك الدولي، وهي الموجة الخاصة باليمن التي نُفّذ "
     "عملها الميداني"),
    (2, "body_ar", "من البالغين في المناطق المشمولة حوالات محلية", "من البالغين في المناطق التي شملها المسح حوالات محلية"),
    (2, "body_ar", "مأخوذة من سؤال مستقل، فلا تُظهر",
     "مأخوذة من سؤالها الخاص، أو من السؤالين معًا في حالة «أيٍّ من الأمرين»، فلا تُظهر"),
    # s3: S4 (roster scope), N11 (CLM-016's wording), S3 (the June 2024 rule); Arabic S4
    (3, "body_en", "not a count of unique providers or of providers operating now. Older counts",
     "not a count of unique providers or of providers operating now. The roster covers entities licensed by CBY-Aden; this "
     "evidence base holds no list from the Central Bank of Yemen in Sana'a, so these entries are not a count for all of Yemen. "
     "Older counts"),
    (3, "body_en", "presents the same pair as estimates of entities, including microfinance institutions.",
     "presents the same pair as World Bank estimates of entities, including exchange firms and microfinance institutions.\n"
     "On 26 June 2024, a CBY-Aden decision required the exchange companies, exchange establishments and money-transfer agents "
     "under its supervision to execute new domestic cash transfers only through the unified money-transfer network. The rule post-dates the survey’s "
     "fieldwork, and a rule is not evidence of how transfers actually move."),
    (3, "body_ar", "ولا تبيّن حصة الأموال التي مرت عبر كل قناة", "ولا تبيّن مقدار الأموال التي مرت عبر كل قناة"),
    (3, "body_ar", "لا عدد لمقدمي خدمات فريدين ولا لمن يعمل منهم حاليًا. ولا تُقارن بها أعداد أقدم:",
     "لا عدد لمقدمي خدمات فريدين ولا لمن يعمل منهم حاليًا. وتشمل القائمة الجهات المرخّصة من البنك المركزي اليمني – عدن، ولا "
     "تتضمن قاعدة الأدلة هذه قائمة صادرة عن البنك المركزي اليمني في صنعاء، فلا تمثل هذه القيود عددًا لليمن كله. ولا تقبل "
     "الأعدادُ الأقدم المقارنةَ بها:"),
    (3, "body_ar", "بوصفه تقديرات لعدد الكيانات، بما فيها مؤسسات التمويل الأصغر.",
     "بوصفه تقديرات للبنك الدولي لعدد الكيانات، بما فيها شركات الصرافة ومؤسسات التمويل الأصغر.\n"
     "وفي 26 يونيو 2024 ألزم قرار صادر عن البنك المركزي اليمني – عدن شركات ومنشآت الصرافة ووكلاء الحوالات الخاضعين لرقابته "
     "بتنفيذ الحوالات النقدية الداخلية الجديدة حصرًا عبر الشبكة الموحدة للحوالات المالية. وهذا القرار لاحق للعمل الميداني للمسح، ووجود قاعدة لا يدل بذاته على كيفية انتقال الحوالات فعليًا."),
    # s5: S1 (other routes first); Arabic N2, S5, N3
    (5, "body_en", "- Survey coverage.",
     "- Other routes. Money may also travel by hand, with travellers or through providers other than exchange companies, and "
     "some recipients may be among the 11.9% of adults who had an account; the survey values do not separate these routes.\n"
     "- Survey coverage."),
    (5, "body_ar", "- تغطية المسح:",
     "- طرق أخرى: قد تنتقل الأموال أيضًا باليد أو مع المسافرين أو عبر مقدمي خدمات غير شركات الصرافة، وقد يكون بعض المتلقين ضمن "
     "نسبة 11.9% من البالغين الذين كان لديهم حساب؛ ولا تفصل قيم المسح بين هذه الطرق.\n- تغطية المسح:"),
    (5, "body_ar", "كما تستند قيم الفئات إلى عينات أصغر.", "كما تستند قيم الفئات إلى عينات أصغر من ذلك."),
    (5, "body_ar", "تمارس شركات الصرافة تبديل العملات إلى جانب صرف الحوالات",
     "تمارس شركات الصرافة تصريف العملات إلى جانب تسليم الحوالات"),
    (5, "body_ar", "فالثلاثة تشترك في الكلمة لا في المقياس.", "فالمعاني الثلاثة تشترك في اللفظ لا في المقياس."),
    # s6: S13 (both corridors), B3 (balance of payments; territory unmapped); Arabic S3 (N4)
    (6, "body_en", "averaged 2.70%. These are prices",
     "averaged 2.70%, one of the two corridors held here (the other, from the United Arab Emirates, averaged 7.53%, lifted by a "
     "single high quote). These are prices"),
    (6, "body_en", "For the economy as a whole, CBY-Aden’s annual reports give", "In the balance of payments, CBY-Aden’s annual reports give"),
    (6, "body_en", "Neither value says how many households received money, or through which channel.",
     "Neither value says how many households received money, or through which channel, and the territory these values cover "
     "has not been mapped here."),
    (6, "body_ar", "من السعودية إلى اليمن 2.70%. وهذه أسعار",
     "من السعودية إلى اليمن 2.70%، وهو أحد ممرّين تتضمنهما قاعدة الأدلة هذه (وبلغ متوسط الممر الآخر، من الإمارات، 7.53%، "
     "ويرفعه عرض سعر مرتفع واحد). وهذه أسعار"),
    (6, "body_ar", "وعلى مستوى الاقتصاد ككل، تورد التقارير السنوية", "وفي ميزان المدفوعات، تعطي التقارير السنوية"),
    (6, "body_ar", "فقد قدّر التقرير السنوي 2024 الحوالات في عام 2024 بمبلغ 6,245 مليون دولار",
     "فقد أورد التقرير السنوي 2024 قيمة الحوالات في عام 2024 عند 6,245 مليون دولار"),
    (6, "body_ar", "ولا تبيّن أيٌّ من القيمتين عدد الأسر التي تلقت أموالًا ولا القناة التي وصلت عبرها.",
     "ولا تبيّن أيٌّ من القيمتين عدد الأسر التي تلقت أموالًا ولا القناة التي وصلت عبرها، ولم تُحدَّد هنا التغطية الجغرافية "
     "لهذه القيم."),
    # s7: "exchange outlets", so the sentence is not read as the unified network that s3 now names; Arabic S6 (N10)
    (7, "body_en", "that a larger exchange network brought more transfers", "that more exchange outlets brought more transfers"),
    (7, "body_ar", "ولا أن اتساع شبكة الصرافة أدى إلى زيادة الحوالات", "ولا أن ازدياد منافذ الصرافة أدى إلى زيادة الحوالات"),
    (7, "body_ar", "وقيمة القناة الغائبة غير معروفة — لا يعني ذلك صفرًا.", "والقيمة الغائبة لأي قناة غير معروفة — ولا تعني صفرًا."),
    # s8: N5; Arabic N1
    (8, "body_en", "- the status of a provider: a roster entry is not proof that it operates now.",
     "- the status of a provider: a roster entry shows a licence listed for 2026; it does not by itself show that the provider "
     "operates now."),
    (8, "body_ar", "- الوحدة: البالغون في المناطق المشمولة بالمسح، لا الأسر ولا الحسابات؛",
     "- الوحدة: البالغون في المناطق التي شملها المسح، لا الأسر ولا الحسابات؛"),
    (8, "body_ar", "- وضع مقدم الخدمة: الإدراج في القائمة ليس دليلًا على أنه يعمل حاليًا.",
     "- وضع مقدم الخدمة: يُظهر القيد في القائمة ترخيصًا مدرجًا لعام 2026، ولا يُثبت وحده أن مقدم الخدمة يعمل حاليًا."),
    # s9: N6; the test follows B2's comparative hypothesis; Arabic S5
    (9, "body_en", "- reporting by exchange companies and remittance agents that separates remittance pay-outs from currency exchange, by area;",
     "- published figures, from exchange companies, remittance agents or their supervisor, that separate remittance pay-outs "
     "from currency exchange, by area;"),
    (9, "body_en", "If households that receive transfers mostly used accounts or wallets, or if",
     "If households that receive transfers used accounts or wallets more than exchange companies and other money-transfer "
     "providers, or if"),
    (9, "body_ar", "- بيانات من شركات الصرافة ووكلاء الحوالات تفصل صرف الحوالات عن تبديل العملات، بحسب المنطقة؛",
     "- أرقام منشورة، من شركات الصرافة أو وكلاء الحوالات أو الجهة الرقابية عليها، تفصل تسليم الحوالات عن تصريف العملات، بحسب "
     "المنطقة؛"),
    (9, "body_ar", "تستخدم الحسابات أو المحافظ الإلكترونية في الغالب، أو",
     "تستخدم الحسابات أو المحافظ الإلكترونية أكثر مما تستخدم شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال، أو"),
    # the Reading's route description: NB1 (confirmation pass) — the channel was asked and is published for all adults,
    # but no channel value is held here ("restricted does not mean missing"); Arabic N1 house form
    ("site_map", "meta_description_en", "; the channel is not measured.", "; no channel value for that wave is held here."),
    ("site_map", "meta_description_ar", "من البالغين في المناطق المشمولة حوالات محلية",
     "من البالغين في المناطق التي شملها المسح حوالات محلية"),
    ("site_map", "meta_description_ar", "؛ ولم تُقَس قناة وصول المال.", "؛ ولا تتضمن قاعدة الأدلة قيمة لقنوات الحوالات في تلك الموجة."),
]

# Phrases the review pair removed (first pass and confirmation pass); none may remain anywhere in the Reading (B1, B2, B3, S2, Arabic M1, S3, S5).
GONE = ["mainly", "informal transfers", "between households travels", "economy as a whole", "the network is listed",
        "hawala transfers", "larger exchange network", "channel is not measured", "has required", "أساسًا", "بطرق غير رسمية", "الاقتصاد ككل", "والشبكة مُدرجة", "لقناة الاستلام", "تبديل العملات",
        "صرف الحوالات", "اتساع شبكة الصرافة", "لم تُقَس", "قاعدة البنك المركزي", "الملف المتاح", "ومنذ 26 يونيو", "قدّر التقرير السنوي 2024"]

# VIS-PAYMENT-RAILS holds the June 2024 rule (S3); its decision is the direct source.
ADD_CLAIMS = ["VIS-PAYMENT-RAILS"]
ADD_SOURCES = ["SRC-CBY-DEC-23-2024-001"]

# Search alias 001 (04_NAV_UX), found while closing CLOSE-6B: the note said the evidence base holds no law as a source
# document; it holds one, on the Bank Deposit Insurance Institution (SRC-CBY-DIL-21-2008), as the /data/ scope line says.
# (old, new) per field; the old value is checked exactly.
ALIAS001 = {
    "alias_id": "SEARCH-ALIAS-001",
    "boundary_note_en": (
        "Discovery aid only: this evidence base holds no law as a source document. It holds regulations, circulars, decisions "
        "and official lists issued by the Central Bank of Yemen – Aden, listed on the Data & sources page.",
        "Discovery aid only: this evidence base holds one law as a source document, on the Bank Deposit Insurance Institution. "
        "Its regulations, circulars, decisions and official lists were issued or posted by the Central Bank of Yemen – Aden, "
        "except one circular of the Central Bank of Yemen in Sana'a. All are listed on the Data & sources page."),
    "boundary_note_ar": (
        "أداة اكتشاف فقط: لا تضم قاعدة الأدلة هذه أي قانون بوصفه وثيقة مصدرية. وتضم لوائح وتعاميم وقرارات وقوائم رسمية صادرة عن "
        "البنك المركزي اليمني – عدن، مدرجة في صفحة البيانات والمصادر.",
        "أداة اكتشاف فقط: تضم قاعدة الأدلة هذه قانونًا واحدًا بوصفه وثيقة مصدرية، هو قانون مؤسسة ضمان الودائع المصرفية. أما "
        "لوائحها وتعاميمها وقراراتها وقوائمها الرسمية فقد أصدرها البنك المركزي اليمني – عدن أو نشرها، عدا تعميم واحد للبنك "
        "المركزي اليمني في صنعاء. وجميعها مدرجة في صفحة البيانات والمصادر."),
}
