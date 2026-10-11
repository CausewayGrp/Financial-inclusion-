# -*- coding: utf-8 -*-
"""CLOSE-6D (Stage A final instruction v5, section 4): the truth corrections 6B-1 to 6B-5, as exact edits.
English and Arabic change together; each EDIT must match its cell exactly once.

SEC   (finding, route, order, lang, field, old, new)        03 section cells, substring edits
CELL  (finding, sheet, key, field, old, new)                keyed rows (column 1), substring edits; field is a header
                                                            name or a column number
WHOLE (finding, sheet, key, field, must_start, new)         a whole cell, guarded by its opening words
SECW  (finding, route, order, lang, field, must_start, new) a whole 03 cell, guarded by its opening words
VS    {record: (drop_tokens, add_entries)}                  06 value_states

The reads behind the edits are in the session's verification reports (V1 Findex DDI and methodology; V2 YLG Annual
Report 2022 and OECD 2026; V4 IMF CR 26/80, WB FSD 2024; V6 POS and OECD locators), summarised in the CLOSE-6D record
of audit/close_out/PROGRESS.md; the World Bank API values are in audit/close_out/fixtures/wb_api_close6d_2026-10-11.json.
"""

FX = "audit/close_out/fixtures/wb_api_close6d_2026-10-11.json"

# ---------------------------------------------------------------------------------------------------------------- 6B-1(e)
SHORT_EN = ("The World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
            "institution is the same as its account figure, so this value reflects accounts at financial institutions.")
SHORT_AR = ("لا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية مساوٍ "
            "لرقم ملكية الحساب؛ فهذه القيمة تعبر عن الحسابات لدى المؤسسات المالية.")
VALS_EN = SHORT_EN.replace("so this value reflects", "so these values reflect")
VALS_AR = SHORT_AR.replace("فهذه القيمة تعبر", "فهذه القيم تعبر")

# ---------------------------------------------------------------------------------------------------------------- 6B-1(a)
LIC_EN = ("For context only, and not as a benchmark, a target or a ranking: the World Bank's own aggregate for low-income "
          "economies in the same survey wave puts adults with an account at a financial institution at 24.5%. Its headline "
          "account figure for those economies, 35.2%, also counts mobile-money accounts, and the World Bank publishes no "
          "mobile-money figure for Yemen, so 35.2% does not compare with Yemen's 11.9% on the same definition. The aggregate "
          "averages economies in very different conditions, includes Yemen itself, and groups economies by the World Bank "
          "income classification.")
LIC_AR = ("للسياق فقط، وليس معيارًا أو هدفًا أو ترتيبًا: يضع تجميع البنك الدولي نفسه للاقتصادات منخفضة الدخل، ضمن موجة "
          "المسح نفسها، نسبة البالغين الذين لديهم حساب لدى مؤسسة مالية عند 24.5%. أما رقمه الرئيسي لملكية الحساب في هذه "
          "الاقتصادات، 35.2%، فيشمل أيضًا حسابات الأموال عبر الهاتف المحمول، ولا ينشر البنك الدولي أي رقم لليمن عن هذه "
          "الحسابات؛ فلا تُقارَن نسبة 35.2% بنسبة اليمن البالغة 11.9% على التعريف نفسه. ويتوسط التجميع اقتصادات شديدة "
          "التباين في أحوالها، ويشمل اليمن نفسه، ويصنف الاقتصادات وفق تصنيف الدخل المعتمد في البنك الدولي.")

# ---------------------------------------------------------------------------------------------------------------- 6B-1(c)
CH_OLD_EN = ("The channels through which money was paid, sent or received are not shown: the World Bank publishes most channel "
             "values for all adults only, and Yemen's survey did not ask the mobile-money questions.")
CH_OLD_AR = ("ولا تُعرض القنوات التي دُفعت أو أُرسلت أو استُلمت عبرها الأموال: فالبنك الدولي ينشر معظم قيم القنوات لجميع "
             "البالغين فقط، ولم يطرح مسح اليمن أسئلة خدمات الأموال عبر الهاتف.")
# V1: the published fin29 is a share of all adults; its definition does not explain a printed zero, so the conflict stands.
# The instruction's Arabic gave a reason ("so the printed zero is not a measured zero") that its English withholds; the
# Arabic below says what the English says.
CH_NEW_EN = ("The channels through which money was paid, sent or received are not shown in this table. For domestic remittances "
             "the World Bank's database prints zero for receipt into an account, with no recipient or group value. Its "
             "published variable documentation for the same wave records that the question was asked and that some recipients "
             "answered yes, as unweighted response counts. The two statements cannot both describe the same quantity, so the "
             "printed value is not used here and no reason for the difference is offered. The database publishes no cash or "
             "money-transfer-operator series.")
CH_NEW_AR = ("ولا يعرض هذا الجدول القنوات التي دُفعت أو أُرسلت أو استُلمت عبرها الأموال. ففي الحوالات المحلية تطبع قاعدة "
             "بيانات البنك الدولي صفرًا لاستلام الأموال في حساب، من دون قيمة للمتلقين أو للفئات. ويُظهر توثيق المتغيرات الذي "
             "ينشره البنك للموجة نفسها أن السؤال طُرح وأن بعض المتلقين أجابوا بنعم، في صورة أعداد غير موزونة من الإجابات. "
             "ولا يمكن أن يصف البيانان الكمية نفسها، لذلك لا تُستخدم القيمة المطبوعة هنا ولا يُقدَّم أي سبب للاختلاف. ولا "
             "تنشر القاعدة أي سلسلة للاستلام نقدًا أو عبر مشغلي تحويل الأموال.")
# 6B-5(a): the bound, held on the record the Reading binds, so that the literal audit traces 62.7% to a record and a state
BOUND_EN = (" By CauseWay’s calculation from the receiving share and the published share of adults with an account at a "
            "financial institution (11.9%), at least 62.7% of the adults who received domestic remittances did not have such "
            "an account: a bound on the group, not on any individual. It says nothing about how the money travelled and does "
            "not rule out an account type for which the World Bank publishes no Yemen value.")
BOUND_AR = (" وبحساب أجرته CauseWay من نسبة المتلقين ومن النسبة المنشورة للبالغين الذين لديهم حساب لدى مؤسسة مالية (11.9%)، "
            "لم يكن لدى 62.7% على الأقل من البالغين الذين تلقوا حوالات محلية حساب من هذا النوع؛ وهذا حدّ يتعلق بالمجموعة "
            "لا بأي فرد بعينه. ولا يقول شيئًا عن الطريق التي انتقلت بها الأموال، ولا يستبعد نوعًا من الحسابات لا ينشر البنك "
            "الدولي له قيمة لليمن.")
FLOW_SUM_END_EN = "no interval is published here for a group value, and a difference between groups is not a cause."
FLOW_SUM_END_AR = "ولا تُنشر هنا فترة ثقة لقيمة أي فئة، والفرق بين الفئات ليس سببًا."

# ---------------------------------------------------------------------------------------------------------------- 6B-2(a)
YLG_OLD_EN = ("Separately, the Organisation for Economic Co-operation and Development (OECD) reports that since 2017 the Yemen "
              "Loan Guarantee Program (YLG), which offers partial guarantees on loans that banks and microfinance institutions "
              "make to MSMEs, has guaranteed 5,731 transactions, with a cumulative USD 42.8 million of guarantees, in nominal "
              "terms, for USD 63.6 million of loan principal.")
YLG_OLD_AR = ("وبصورة منفصلة، تفيد منظمة التعاون الاقتصادي والتنمية (OECD) بأن برنامج ضمان القروض اليمني (YLG)، الذي يقدم "
              "ضمانات جزئية للقروض التي تمنحها البنوك ومؤسسات التمويل الأصغر للمنشآت الأصغر والصغيرة والمتوسطة، بلغ عدد "
              "المعاملات التي ضمنها منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون دولار بالقيمة "
              "الاسمية لأصل قروض قدره 63.6 مليون دولار.")
YLG_EN = ("Two publishers report on the Yemen Loan Guarantee Program (YLG), which shares credit risk with partner banks and "
          "microfinance providers on loans to micro, small and medium enterprises. The programme's own Annual Report 2022 states "
          "that in 2022 it issued 3,387 letters of guarantee, worth YER 6.4 billion and covering loans of YER 9.4 billion, "
          "through 12 partner institutions; women-led businesses received 693 of them (about 20%). Its yearly counts for "
          "2018–2022 sum to 6,976 guarantees. Separately, the Organisation for Economic Co-operation and Development (OECD) "
          "reports, in 2026, that YLG has guaranteed 5,731 transactions since 2017, with USD 42.8 million of guarantees for "
          "USD 63.6 million of loan principal in nominal terms, 72.7% of them to men-owned businesses; it states neither a "
          "cutoff date nor an exchange rate. The two sets of figures differ in total and in gender split, and the published "
          "documents do not explain why, so they are shown side by side and not combined.")
YLG_AR = ("يتناول مصدران برنامجَ ضمان القروض في اليمن (YLG)، الذي يتقاسم مخاطر الائتمان مع البنوك ومؤسسات التمويل الأصغر "
          "الشريكة على قروض المنشآت الأصغر والصغيرة والمتوسطة. يذكر التقرير السنوي للبرنامج لعام 2022 أنه أصدر خلال عام 2022 "
          "ما مجموعه 3,387 خطاب ضمان بقيمة 6.4 مليار ريال، تغطي قروضًا بقيمة 9.4 مليار ريال، عبر 12 مؤسسة شريكة، وأن المنشآت التي "
          "تقودها نساء حصلت على 693 منها (نحو 20%). وتبلغ أعداده السنوية للفترة 2018–2022 في مجموعها 6,976 ضمانًا. وفي "
          "مصدر منفصل، تذكر منظمة التعاون الاقتصادي والتنمية (OECD) في عام 2026 أن البرنامج ضمن منذ عام 2017 ما مجموعه "
          "5,731 معاملة، بضمانات قدرها 42.8 مليون دولار لأصل قروض قدره 63.6 مليون دولار بالقيمة الاسمية، 72.7% منها لمنشآت "
          "يملكها رجال، من دون أن تذكر تاريخ انتهاء بياناتها أو سعر الصرف المستخدم. ويختلف الرقمان في المجموع وفي التوزيع "
          "بحسب الجنس، ولا تشرح الوثائق المنشورة سبب ذلك، لذا يُعرضان جنبًا إلى جنب ولا يُدمجان في سلسلة واحدة.")
FIRMS_OLD_EN = ("Guarantee data tell a different story: the OECD reports that since 2017 the Yemen Loan Guarantee Program (YLG) has "
                "guaranteed 5,731 transactions, with a cumulative USD 42.8 million of guarantees, in nominal terms, for USD 63.6 "
                "million of loan principal. These are guarantee volumes: they show what the programme backed, not how many firms "
                "could borrow, on what terms, or what share of MSME lending they represent.")
FIRMS_OLD_AR = ("وتقدم بيانات الضمانات صورة من نوع آخر: تفيد منظمة التعاون الاقتصادي والتنمية (OECD) بأن برنامج ضمان القروض "
                "اليمني (YLG) بلغ عدد المعاملات التي ضمنها منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون "
                "دولار بالقيمة الاسمية لأصل قروض قدره 63.6 مليون دولار. وهذه أحجام ضمانات: تبين ما دعمه البرنامج، لا عدد "
                "المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت الأصغر والصغيرة والمتوسطة.")
FIRMS_NEW_EN = ("Guarantee data tell a different story. " + YLG_EN + " Both publishers count guarantees or transactions, not firms: "
                "the figures show what the programme backed, not how many firms could borrow, on what terms, or what share of "
                "MSME lending they represent.")
FIRMS_NEW_AR = ("وتقدم بيانات الضمانات صورة من نوع آخر. " + YLG_AR + " ويعدّ المصدران خطابات الضمان أو المعاملات لا المنشآت: "
                "فتبين الأرقام ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت "
                "الأصغر والصغيرة والمتوسطة.")
YLG_DNE_OLD_EN = ("A guarantee volume is not firms' access to finance: guaranteed transactions are not unique firms, and guarantees "
                  "and loan principal show what the programme backed, not how many firms could borrow, on what terms, or what "
                  "share of MSME lending they represent.")
YLG_DNE_OLD_AR = ("وليس حجم الضمانات وصولًا للمنشآت إلى التمويل: فالمعاملات المضمونة ليست منشآت فريدة، والضمانات وأصل القروض "
                  "يبينان ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت الأصغر "
                  "والصغيرة والمتوسطة.")
YLG_DNE_EN = ("Both publishers count guarantees or transactions, not firms. Neither shows how many MSMEs could borrow, on what "
              "terms, or whether guaranteed loans would have been made anyway: guarantees and loan principal show what the "
              "programme backed, not how many firms could borrow or what share of MSME lending they represent. Programme amounts "
              "are nominal rials as reported; the report does not say in which area's rial loans were made, and nothing is "
              "converted here. 2022 is the latest year for which a programme report was verified in this review; later reports "
              "were not searched.")
YLG_DNE_AR = ("ويعدّ المصدران خطابات الضمان أو المعاملات لا المنشآت. ولا يبيّن أيٌّ منهما عدد المنشآت الأصغر والصغيرة "
              "والمتوسطة التي استطاعت الاقتراض ولا شروطه، ولا ما إذا كانت القروض المضمونة ستُمنح على أي حال: فالضمانات وأصل "
              "القروض تبين ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا حصته من إقراض هذه المنشآت. ومبالغ "
              "البرنامج بالريال الاسمي كما أُبلغ عنها، ولا يذكر التقرير ريالَ أي منطقة مُنحت به القروض، ولا يُحوَّل هنا أي مبلغ. "
              "وعام 2022 هو أحدث عام جرى في هذه المراجعة التحقق من تقرير للبرنامج عنه؛ ولم يُبحث عن تقارير لاحقة.")
VER_EN = (" The OECD's six sector shares for the programme sum to 104%, so they are shown neither as a breakdown nor "
          "renormalised; the programme's own portfolio-at-risk figure has no stated base and is not shown.")
VER_AR = (" وتبلغ حصص القطاعات الست التي تذكرها منظمة التعاون الاقتصادي والتنمية للبرنامج في مجموعها 104%، فلا تُعرض "
          "توزيعًا ولا يُعاد توزيعها نسبيًا؛ ونسبة المحفظة المعرضة للمخاطر في تقرير البرنامج بلا أساس معلن، فلا تُعرض.")

# ---------------------------------------------------------------------------------------------------------------- 6B-2(c)
SURVEY141_EN = "The appraisal document gives no title, fieldwork dates, sampling frame or size definitions for this survey."
SURVEY141_AR = "لا تذكر وثيقة التقييم عنوانًا لهذا المسح ولا تواريخ عمله الميداني ولا إطار المعاينة ولا تعريفات أحجام المنشآت."

# ---------------------------------------------------------------------------------------------------------------- 6B-5
R = "/readings/how-money-reaches-households/"
CWR_SET = {
    "title_en": "Domestic remittances and accounts: what the evidence establishes",
    "title_ar": "الحوالات المحلية والحسابات: ما الذي تثبته الأدلة؟",
    "question_en": ("What does the published evidence establish about whether adults in Yemen who received domestic remittances "
                    "received them into an account of their own?"),
    "question_ar": ("ما الذي تثبته الأدلة المنشورة بشأن ما إذا كان البالغون في اليمن الذين تلقوا حوالات محلية قد تلقوها في "
                    "حسابات خاصة بهم؟"),
    "thesis_en": ("In Yemen’s Global Findex 2021 wave, 31.9% of adults in surveyed areas received domestic remittances and 11.9% "
                  "of adults in those areas had an account at a financial institution. By CauseWay’s calculation from these two "
                  "published World Bank shares, at least 62.7% of the adults who received domestic remittances did not have such "
                  "an account; that is a bound on the group, not a statement about any individual. It says nothing about how the "
                  "money travelled, and it does not rule out a mobile wallet or another account type for which the World Bank "
                  "publishes no Yemen value. For the 2021 wave, no weighted estimate of the channel is published or held here; "
                  "the World Bank’s published variable documentation records that recipients were asked whether they received the "
                  "money into an account and that some answered yes. That money sent between people reaches recipients more "
                  "through exchange companies and other money-transfer providers than into accounts of their own remains a "
                  "hypothesis: the survey counts adults, not households, and its values here cover transfers within Yemen only."),
    "thesis_ar": ("في موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) الخاصة باليمن، تلقى 31.9% من البالغين في المناطق "
                  "التي شملها المسح حوالات محلية، وكان لدى 11.9% من البالغين في تلك المناطق حساب لدى مؤسسة مالية. وبحساب أجرته "
                  "CauseWay من هاتين النسبتين المنشورتين للبنك الدولي، لم يكن لدى 62.7% على الأقل من البالغين الذين تلقوا "
                  "حوالات محلية حساب من هذا النوع؛ وهذا حدّ يتعلق بالمجموعة لا بأي فرد بعينه. ولا يقول شيئًا عن الطريق التي "
                  "انتقلت بها الأموال، ولا يستبعد محفظة إلكترونية أو نوعًا آخر من الحسابات لا ينشر البنك الدولي له قيمة لليمن. "
                  "ولموجة 2021 لا يُنشر أي تقدير موزون للقناة ولا يُحتفظ به هنا؛ ويسجل توثيق المتغيرات الذي "
                  "ينشره البنك الدولي أن المتلقين سُئلوا عمّا إذا كانوا قد تلقوا المال في حساب، وأن بعضهم أجاب بنعم. ويبقى "
                  "القول بأن الأموال المرسلة بين الأفراد تصل إلى متلقيها عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال "
                  "أكثر مما تصل إلى حسابات خاصة بهم فرضيةً: فالمسح يعدّ البالغين لا الأسر، ولا تغطي قيمه الواردة هنا إلا "
                  "الحوالات داخل اليمن."),
    "prohibited_inference_en": ("A share of adults who received domestic remittances is not a share of households that depend on "
                                "them; the bound that CauseWay calculates from the two published shares (at least 62.7% of "
                                "recipients without an account at a financial institution) describes the group, not any "
                                "individual recipient, and does not show how the money travelled or rule out an account type "
                                "for which no Yemen value is published; a roster entry or a branch count is not a measure of "
                                "remittance flows; and a price of sending money from abroad is not the cost a household pays "
                                "to collect it."),
    "prohibited_inference_ar": ("لا تمثل نسبة البالغين الذين تلقوا حوالات محلية نسبة الأسر التي تعتمد عليها؛ والحدّ الذي تحسبه "
                                "CauseWay من النسبتين المنشورتين (62.7% على الأقل من المتلقين بلا حساب لدى مؤسسة مالية) يصف "
                                "المجموعة لا أي متلقٍّ بعينه، ولا يُظهر الطريق التي انتقلت بها الأموال، ولا يستبعد نوعًا من "
                                "الحسابات لا تُنشر له قيمة لليمن؛ وليس القيد في قائمة أو عدد الفروع مقياسًا لتدفقات الحوالات؛ "
                                "وليس سعر إرسال المال من الخارج التكلفة التي تتحملها الأسرة لاستلامه."),
}
CWR_OLD_START = {"title_en": "How money reaches households", "title_ar": "كيف يصل المال إلى الأسر",
                 "question_en": "Does money sent between people", "question_ar": "هل تصل الأموال المرسلة",
                 "thesis_en": "In Yemen’s Global Findex 2021 wave, 31.9%", "thesis_ar": "في موجة 2021 من المؤشر العالمي",
                 "prohibited_inference_en": "A share of adults who received domestic remittances is not",
                 "prohibited_inference_ar": "لا تمثل نسبة البالغين الذين تلقوا"}
S1_HEAD = (("What the evidence supports", "What the two published shares establish"),
           ("ما الذي تسنده الأدلة", "ما الذي تثبته النسبتان المنشورتان؟"))
META_OLD_START = ("In Yemen’s Findex 2021 wave, 31.9%", "في موجة 2021 من Global Findex لليمن")
META_EN = ("A hypothesis on domestic remittances and accounts in Yemen. For the 2021 wave no weighted channel estimate is "
           "published or held; World Bank documentation records the item as asked and answered.")
META_AR = ("فرضية عن الحوالات المحلية والحسابات في اليمن. لموجة 2021 لا يُنشر ولا يُحتفظ هنا بأي تقدير موزون للقناة؛ ويسجل "
           "توثيق البنك الدولي أن السؤال طُرح وأُجيب عنه.")

S4_EN = ("This Reading’s hypothesis is that money sent between people within Yemen reaches recipients more through exchange "
         "companies and other money-transfer providers than into accounts of their own. “Into accounts” means receipt into the "
         "recipient’s own account: a transfer can move through the banking system and still be paid out in cash to a recipient "
         "without one, so the hypothesis says nothing about the part banks play in moving money. The evidence bears on whether "
         "recipients held accounts and says nothing about magnitudes: no source here measures what share of households’ cash "
         "comes from transfers, how much money moves through each channel, or how often transfers arrive. In 2014, 31.1% of "
         "recipients named a money transfer operator and 2.0% a financial institution, and the profile held here does not show "
         "how the others received money; a money transfer operator in the survey is not necessarily an exchange company. For "
         "the 2021 wave, the two published shares bound how far they can overlap: by CauseWay’s calculation from them (31.9% of "
         "adults received domestic remittances; 11.9% had an account at a financial institution), at most 11.9% of adults can "
         "be both, so at least 62.7% of the adults who received domestic remittances did not have an account at a financial "
         "institution. That is a bound on the group, not a statement about any individual; it says nothing about how the money "
         "travelled, and it does not rule out a mobile wallet or another account type for which the World Bank publishes no "
         "Yemen value. This Reading states a hypothesis, not a finding.")
S4_AR = ("تفترض هذه القراءة أن الأموال المرسلة بين الأفراد داخل اليمن تصل إلى متلقيها عبر شركات الصرافة وغيرها من مقدمي خدمات "
         "تحويل الأموال أكثر مما تصل إلى حسابات خاصة بهم. والمقصود بالوصول «إلى الحسابات» استلامُ المال في حساب المتلقي نفسه: "
         "فقد تنتقل الحوالة عبر النظام المصرفي ثم تُسلَّم نقدًا لمتلقٍّ لا يملك حسابًا، لذلك لا تقول الفرضية شيئًا عن الدور الذي "
         "تؤديه البنوك في نقل الأموال. وتتصل الأدلة بمسألة امتلاك المتلقين حسابات، ولا تقول شيئًا عن الأحجام: فلا يقيس أي "
         "مصدر هنا حصة الحوالات من النقد الذي تتلقاه الأسر، ولا مقدار ما ينتقل عبر كل قناة، ولا عدد مرات وصول الحوالات. وفي "
         "2014 ذكر 31.1% من المتلقين مشغل تحويل أموال، و2.0% مؤسسة مالية، ولا يبيّن الملف الوارد في قاعدة الأدلة هذه كيف "
         "تلقى الباقون أموالهم؛ ومشغل تحويل الأموال في المسح ليس بالضرورة شركة صرافة. أما في موجة 2021 فتحدّ النسبتان "
         "المنشورتان مدى التقاطع بينهما: فبحساب أجرته CauseWay منهما (تلقى 31.9% من البالغين حوالات محلية؛ وكان لدى 11.9% "
         "من البالغين حساب لدى مؤسسة مالية)، لا يمكن أن يجمع بين الأمرين أكثر من 11.9% من البالغين، أي أن 62.7% على الأقل "
         "ممن تلقّوا حوالات محلية لم يكن لديهم حساب لدى مؤسسة مالية. وهذا حدّ يتعلق بالمجموعة لا بأي فرد بعينه؛ ولا يقول "
         "شيئًا عن الطريق التي انتقلت بها الأموال، ولا يستبعد محفظة إلكترونية أو نوعًا آخر من الحسابات لا ينشر البنك الدولي "
         "له قيمة لليمن. وتطرح هذه القراءة فرضيةً لا نتيجة.")

SECW = [
    ("6B-5", R, 4, "en", "body", "The evidence is consistent with a hypothesis", S4_EN),
    ("6B-5", R, 4, "ar", "body", "تتسق الأدلة مع فرضية", S4_AR),
]

SEC = [
    # 6B-1(e): home page, the three-figures section
    ("6B-1e", "/", 3, "en", "body",
     "but the mobile-money questions were not asked in Yemen's survey, so the figure here reflects accounts at financial "
     "institutions.",
     "but the World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
     "institution is the same as its account figure, so this value reflects accounts at financial institutions."),
    ("6B-1e", "/", 3, "ar", "body",
     "غير أن أسئلة خدمات الأموال عبر الهاتف لم تُطرح في مسح اليمن، فالنسبة هنا تعكس الحسابات لدى المؤسسات المالية.",
     "غير أن البنك الدولي لا ينشر أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية مساوٍ "
     "لرقم ملكية الحساب؛ فهذه القيمة تعبر عن الحسابات لدى المؤسسات المالية."),
    # 6B-1(a): /people/
    ("6B-1a", "/people/", 2, "en", "body",
     "For context only, the World Bank's figure for the same wave across the 19 low-income economies surveyed in it, Yemen "
     "among them, is 35.2%; it averages very different economies and is not a benchmark or a ranking.", LIC_EN),
    ("6B-1a", "/people/", 2, "ar", "body",
     "وللسياق فقط، يبلغ رقم البنك الدولي للموجة نفسها في الاقتصادات منخفضة الدخل الـ19 التي شملتها، ومنها اليمن، 35.2%؛ وهو "
     "متوسط لاقتصادات متباينة جدًا، وليس معيارًا ولا ترتيبًا.", LIC_AR),
    # 6B-1(d): /finance/
    ("6B-1d", "/finance/", 13, "en", "body",
     "Product-holding and mobile-access figures attributed to the OECD's 2026 financial-sector review have not yet been "
     "verified against the review's own text, and they are not shown here.",
     "The OECD's 2026 review prints figures for current accounts, savings accounts and mobile-phone access without naming the "
     "survey or period behind them. They are not used here, they are not 2026 measurements, and they are not comparable with "
     "the Global Findex."),
    ("6B-1d", "/finance/", 13, "ar", "body",
     "لم يُتحقق بعد من أرقام حيازة المنتجات المالية والوصول إلى الهاتف المحمول المنسوبة إلى استعراض منظمة التعاون الاقتصادي "
     "والتنمية (OECD) للقطاع المالي لعام 2026 مقابل نصه الأصلي، ولذلك لا تُعرض هنا.",
     "تورد مراجعة منظمة التعاون الاقتصادي والتنمية (OECD) لعام 2026 أرقامًا عن الحسابات الجارية وحسابات الادخار والنفاذ إلى "
     "الهاتف المحمول من دون تسمية المسح أو الفترة التي تستند إليها. ولا تُستخدم هنا، وليست قياسات لعام 2026، ولا تُقارَن "
     "بقاعدة Global Findex."),
    # 6B-2(a): /firms/ section 7, second paragraph
    ("6B-2a", "/firms/", 7, "en", "body", FIRMS_OLD_EN, FIRMS_NEW_EN),
    ("6B-2a", "/firms/", 7, "ar", "body", FIRMS_OLD_AR, FIRMS_NEW_AR),
    # 6B-2(c): the 2018 survey
    ("6B-2c", "/firms/", 6, "en", "body",
     "it is a different survey with a different question, so it is not a baseline for the 2022 seven-governorate survey.",
     "it is a different survey with a different question, so it is not a baseline for the 2022 seven-governorate survey. "
     + SURVEY141_EN),
    ("6B-2c", "/firms/", 6, "ar", "body",
     "وهو مسح مختلف بسؤال مختلف، فلا يُتخذ خط أساس لمسح 2022 في المحافظات السبع.",
     "وهو مسح مختلف بسؤال مختلف، فلا يُتخذ خط أساس لمسح 2022 في المحافظات السبع. " + SURVEY141_AR),
    ("6B-2c", "/readings/finance-constraint-different-questions/", 7, "en", "body",
     "The document does not name the survey further, and its question and sample differ from the 2022 survey’s.",
     SURVEY141_EN + " Its question and sample differ from the 2022 survey’s."),
    ("6B-2c", "/readings/finance-constraint-different-questions/", 7, "ar", "body",
     "ولا تذكر الوثيقة عن المسح أكثر من ذلك، ويختلف سؤاله وعينته عن سؤال مسح 2022 وعينته.",
     "و" + SURVEY141_AR + " ويختلف سؤاله وعينته عن سؤال مسح 2022 وعينته."),
    ("6B-2c", "/readings/finance-constraint-different-questions/", 7, "ar", "body", "فهو قيد مؤرخ لا خط أساس",
     "فهو قيدٌ قديم العهد، لا خطُّ أساس"),
    # 6B-3(c): /methodology/, Yemen Post (WB FSD 2024, Executive Summary, p.16)
    ("6B-3c", "/methodology/", 4, "en", "body",
     "Yemen Post is not covered by any evidence record in this resource; its network and any financial services it may offer "
     "would be measured through the postal operator's own records of offices, services and transactions.",
     "Yemen Post is not covered here. The World Bank (2024, p. 16) describes the Yemen Post and Postal Savings Authority as providing "
     "payment services, savings accounts and other financial products, and gives no count of its offices, accounts or "
     "balances; its network and services would be measured through the postal operator's own records of offices, services "
     "and transactions."),
    ("6B-3c", "/methodology/", 4, "ar", "body",
     "أما البريد اليمني فلا يغطيه أي سجل دليل في هذا المورد، ويمكن قياس شبكته وما قد يقدمه من خدمات مالية من سجلات مشغل "
     "البريد نفسه عن المكاتب والخدمات والمعاملات.",
     "أما البريد اليمني فلا يغطيه هذا المورد. ويصف البنك الدولي (2024، ص. 16) الهيئة العامة للبريد والتوفير البريدي بأنها تقدم "
     "خدمات دفع وحسابات ادخار ومنتجات مالية أخرى، ولا يورد عددًا لمكاتبها أو حساباتها أو أرصدتها؛ ويمكن قياس شبكتها "
     "وخدماتها من سجلات مشغل البريد نفسه عن المكاتب والخدمات والمعاملات."),
    # 6B-5: the Reading's sections (s4 is rewritten whole, in SECW)
    ("6B-5", R, 2, "en", "body", "but the survey does not say how that money travelled.",
     "but the published values do not say how that money travelled."),
    ("6B-5", R, 2, "en", "body", "11.9% of adults had an account.", "11.9% of adults had an account at a financial institution."),
    ("6B-5", R, 2, "en", "body", "so the figures do not show how many of the adults who received money had an account.",
     "so the figures give no exact count of the recipients who had an account; the hypothesis section below sets out the "
     "bound that the two shares do give."),
    ("6B-5", R, 2, "ar", "body", "لكن المسح لا يبيّن كيف انتقلت تلك الأموال", "لكن القيم المنشورة لا تبيّن كيف انتقلت تلك الأموال"),
    ("6B-5", R, 2, "ar", "body", "وكان لدى 11.9% من البالغين حساب.", "وكان لدى 11.9% من البالغين حساب لدى مؤسسة مالية."),
    ("6B-5", R, 2, "ar", "body", "فلا تُظهر الأرقام كم ممن تلقوا الأموال كان لديهم حساب.",
     "فلا تعطي الأرقام عددًا دقيقًا للمتلقين الذين كان لديهم حساب؛ ويعرض قسم الفرضية أدناه الحدّ الذي تعطيه النسبتان."),
    ("6B-5", R, 3, "en", "heading", "The channel evidence is old, and providers are listed, not measured",
     "Weighted channel values are old, and providers are listed, not measured"),
    ("6B-5", R, 3, "ar", "heading", "أدلة القنوات قديمة، ومقدمو الخدمة مُدرجون في قوائم لا مَقيسون",
     "قيم القنوات الموزونة قديمة، ومقدمو الخدمة مُدرجون في قوائم لا مَقيسون"),
    ("6B-5", R, 3, "en", "body", "The only channel values held here are historical.",
     "The only weighted channel values held here are historical."),
    ("6B-5", R, 3, "en", "body",
     "For the 2021 wave, this evidence base holds no channel value for domestic remittances, and Yemen’s survey did not ask "
     "the mobile-money questions.",
     "For the 2021 wave, no weighted estimate of the channel for domestic remittances is published or held here. The World "
     "Bank’s published variable documentation for that wave records that recipients were asked whether they received the "
     "money into an account and that some answered yes; these are unweighted counts of answers, not an estimate for the "
     "population, and they are not used here. The World Bank’s database prints zero for receipt into an account, with no "
     "recipient or group value; the two statements cannot both describe the same quantity, so the printed value is not used "
     "either. The World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
     "institution is the same as its account figure."),
    ("6B-5", R, 3, "ar", "body", "القيم الوحيدة المتعلقة بالقنوات في قاعدة الأدلة هذه قيم تاريخية.",
     "القيم الموزونة الوحيدة المتعلقة بالقنوات في قاعدة الأدلة هذه قيم تاريخية."),
    ("6B-5", R, 3, "ar", "body",
     "أما موجة 2021، فلا تتضمن قاعدة الأدلة هذه أي قيمة لقنوات الحوالات المحلية فيها، ولم يطرح مسح اليمن أسئلة خدمات الأموال "
     "عبر الهاتف.",
     "أما موجة 2021، فلا يُنشر لها أي تقدير موزون لقناة الحوالات المحلية ولا يُحتفظ به هنا. ويسجل توثيق "
     "المتغيرات الذي ينشره البنك الدولي لتلك الموجة أن المتلقين سُئلوا عمّا إذا كانوا قد تلقوا المال في حساب، وأن بعضهم "
     "أجاب بنعم؛ وهذه أعداد غير موزونة من الإجابات، لا تقدير للسكان، ولا تُستخدم هنا. وتطبع قاعدة بيانات البنك الدولي صفرًا "
     "لاستلام الأموال في حساب، من دون قيمة للمتلقين أو للفئات؛ ولا يمكن أن يصف البيانان الكمية نفسها، فلا تُستخدم القيمة "
     "المطبوعة أيضًا. ولا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة "
     "مالية مساوٍ لرقم ملكية الحساب."),
    ("6B-5", R, 7, "en", "body",
     "It does not show what share of household cash comes from remittances, how recipients collected the money in the 2021 "
     "wave, or whether the adults who received money were those without an account.",
     "It does not show what share of household cash comes from remittances or how recipients collected the money in the 2021 "
     "wave. The two survey shares bound the share of recipients who lacked an account at a financial institution (at least 62.7%, by "
     "CauseWay’s calculation), but that bound describes the group, not any individual, and says nothing about the channel."),
    ("6B-5", R, 7, "ar", "body",
     "فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021، ولا ما إذا كان البالغون "
     "الذين تلقوا الأموال هم أنفسهم من لا يملكون حسابًا.",
     "فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021. وتحدّ نسبتا المسح نسبةَ "
     "المتلقين الذين لم يكن لديهم حساب لدى مؤسسة مالية (62.7% على الأقل، بحساب أجرته CauseWay)، لكن هذا الحدّ يصف المجموعة "
     "لا أي فرد بعينه، ولا يقول شيئًا عن القناة."),
    ("6B-5", R, 8, "en", "body", "and the only channel values are for 2014;", "and the only weighted channel values are for 2014;"),
    ("6B-5", R, 8, "ar", "body", "وقيم القنوات الوحيدة تخص عام 2014؛", "وقيم القنوات الموزونة الوحيدة تخص عام 2014؛"),
    ("6B-5", R, 9, "en", "body", "- channel values for domestic remittances from a current survey wave;",
     "- weighted channel estimates for domestic remittances: for the 2021 wave the World Bank documents that the question was "
     "asked and answered, but no weighted estimate is published or held here, and the World Bank has published no later "
     "Yemen wave;"),
    ("6B-5", R, 9, "en", "body",
     "If households that receive transfers used accounts or wallets more than exchange companies and other money-transfer "
     "providers, or if transfers were a small part of household cash, the hypothesis would fail.",
     "If adults who receive transfers received them into accounts or wallets of their own more often than through exchange "
     "companies and other money-transfer providers, the hypothesis would fail."),
    ("6B-5", R, 9, "ar", "body", "- قيم لقنوات الحوالات المحلية من موجة مسح حديثة؛",
     "- تقديرات موزونة لقنوات الحوالات المحلية: ففي موجة 2021 يوثّق البنك الدولي أن السؤال طُرح وأُجيب عنه، لكن لا يُنشر أي "
     "تقدير موزون ولا يُحتفظ به هنا، ولم ينشر البنك الدولي موجة أحدث لليمن؛"),
    ("6B-5", R, 9, "ar", "body",
     "وإذا تبيّن أن الأسر التي تتلقى الحوالات تستخدم الحسابات أو المحافظ الإلكترونية أكثر مما تستخدم شركات الصرافة وغيرها من "
     "مقدمي خدمات تحويل الأموال، أو أن الحوالات جزء صغير من النقد الذي تتلقاه الأسر، سقطت الفرضية.",
     "وإذا تبيّن أن البالغين الذين يتلقون الحوالات يستلمونها في حسابات أو محافظ إلكترونية خاصة بهم أكثر مما يستلمونها عبر "
     "شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال، سقطت الفرضية."),
]

O6 = "06_EVIDENCE_OBJECTS"
CELL = [
    # ------------------------------------------------------------ 6B-1(e) and (a): CLM-001
    ("6B-1e", O6, "CLM-001", "summary_en",
     "in the areas covered by Yemen's survey; it reflects accounts at financial institutions, because the mobile-money "
     "questions were not asked in this survey.", "in the areas covered by Yemen's survey. " + SHORT_EN),
    ("6B-1a", O6, "CLM-001", "summary_en",
     "For context, the World Bank's figure for the same survey wave across the 19 low-income economies surveyed in it, Yemen "
     "among them, is 35.2%.",
     "For context only, and not as a benchmark: the World Bank's own aggregate for low-income economies in the same survey wave "
     "puts adults with an account at a financial institution at 24.5%; its headline account figure for those economies, "
     "35.2%, also counts mobile-money accounts, so it does not compare with Yemen's 11.9% on the same definition."),
    ("6B-1e", O6, "CLM-001", "summary_ar",
     "في المناطق التي شملها مسح اليمن، وهي تعكس الحسابات لدى المؤسسات المالية، لأن أسئلة خدمات الأموال عبر الهاتف لم تُطرح "
     "في هذا المسح.", "في المناطق التي شملها مسح اليمن. و" + SHORT_AR),
    ("6B-1a", O6, "CLM-001", "summary_ar",
     "وللسياق، يبلغ رقم البنك الدولي لموجة المسح نفسها في الاقتصادات منخفضة الدخل الـ19 التي شملتها الموجة، ومنها اليمن، "
     "35.2%.",
     "وللسياق فقط، وليس معيارًا: يضع تجميع البنك الدولي نفسه للاقتصادات منخفضة الدخل، ضمن موجة المسح نفسها، نسبة البالغين "
     "الذين لديهم حساب لدى مؤسسة مالية عند 24.5%؛ أما رقمه الرئيسي لملكية الحساب في هذه الاقتصادات، 35.2%، فيشمل أيضًا "
     "حسابات الأموال عبر الهاتف المحمول، فلا يُقارَن بنسبة اليمن البالغة 11.9% على التعريف نفسه."),
    ("6B-1e", O6, "CLM-001", "definition_en",
     "In Yemen's survey the mobile-money questions were not asked, so the figure reflects accounts at banks and other "
     "financial institutions.", SHORT_EN),
    ("6B-1e", O6, "CLM-001", "definition_ar",
     "ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تعكس النسبة الحسابات لدى البنوك والمؤسسات المالية الأخرى.",
     "و" + SHORT_AR),
    ("6B-1a", O6, "CLM-001", "method_en",
     "The low-income context figure, 35.2%, is the World Bank's own aggregate for the same wave and indicator; this resource "
     "reproduced it as the average of the published values of the 19 low-income economies surveyed in the wave, weighted by "
     "their adult populations.",
     "The low-income context figures are the World Bank's own aggregates for the same survey wave, as its database publishes "
     "them: 24.5% for an account at a financial institution, and 35.2% for account ownership, which also counts mobile-money "
     "accounts. The database files the low-income aggregate at year 2021 and Yemen's observation at year 2022, within one "
     "survey wave, and groups economies by the World Bank's income classification for fiscal year 2024 (a 2022 Atlas GNI per "
     "capita of USD 1,135 or less)."),
    ("6B-1a", O6, "CLM-001", "method_ar",
     "ورقم السياق للاقتصادات منخفضة الدخل، 35.2%، هو التجميع الذي ينشره البنك الدولي نفسه للموجة والمؤشر ذاتيهما؛ وقد أعاد هذا "
     "المورد احتسابه متوسطًا للقيم المنشورة للاقتصادات منخفضة الدخل الـ19 التي شملتها الموجة، مرجّحًا بعدد البالغين في كل منها.",
     "وأرقام السياق للاقتصادات منخفضة الدخل هي التجميعات التي ينشرها البنك الدولي نفسه لموجة المسح نفسها كما تنشرها قاعدة "
     "بياناته: 24.5% للحساب لدى مؤسسة مالية، و35.2% لملكية الحساب، وهو رقم يشمل أيضًا حسابات الأموال عبر الهاتف المحمول. "
     "وتسجل القاعدة تجميع الاقتصادات منخفضة الدخل لسنة 2021 ومشاهدة اليمن لسنة 2022 ضمن موجة مسح واحدة، وتصنف الاقتصادات "
     "وفق تصنيف الدخل المعتمد في البنك الدولي للسنة المالية 2024 (نصيب الفرد من الدخل القومي الإجمالي لعام 2022 بطريقة "
     "أطلس 1,135 دولارًا أمريكيًا أو أقل)."),
    ("6B-1e", O6, "CLM-001", "method_ar", "ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن:",
     "ولم تُطرح أسئلة خدمات الأموال عبر الهاتف المحمول في مسح اليمن:"),
    ("6B-1e", O6, "CLM-001", "method_ar", "وسلسلة البنك الدولي الخاصة بحسابات الأموال عبر الهاتف لا تتضمن",
     "وسلسلة البنك الدولي الخاصة بحسابات الأموال عبر الهاتف المحمول لا تتضمن"),
    ("6B-1e", O6, "CLM-001", "definition_ar", "خلال الاثني عشر شهرًا السابقة", "خلال الـ12 شهرًا السابقة"),
    ("6B-1e", O6, "VIS-FINDEX-GAPS", "definition_ar", "خلال الاثني عشر شهرًا السابقة", "خلال الـ12 شهرًا السابقة"),
    ("6B-1e", O6, "CLM-001", "limitations_en",
     "Personal use of a mobile-money service, which the World Bank's definition also counts, was not measured in Yemen's "
     "survey.",
     "Personal use of a mobile-money service, which the World Bank's definition also counts, has no published value for "
     "Yemen."),
    ("6B-1a", O6, "CLM-001", "limitations_en",
     "The low-income figure is context, not a benchmark, a target or a ranking: it averages economies in very different "
     "conditions, includes Yemen itself and uses the income classification in the Global Findex Database 2025, while Yemen's "
     "own figure covers only the areas its survey reached.",
     "The low-income figures are context, not a benchmark, a target or a ranking: they average economies in very different "
     "conditions, include Yemen itself and group economies by the World Bank's income classification for fiscal year 2024, "
     "while Yemen's own figure covers only the areas its survey reached. Only the financial-institution figure, 24.5%, "
     "compares with Yemen's 11.9% on the same definition."),
    ("6B-1e", O6, "CLM-001", "limitations_ar",
     "أما الاستخدام الشخصي لخدمة أموال عبر الهاتف المحمول، الذي يشمله تعريف البنك الدولي أيضًا، فلم يُقس في مسح اليمن.",
     "أما الاستخدام الشخصي لخدمة أموال عبر الهاتف المحمول، الذي يشمله تعريف البنك الدولي أيضًا، فلا قيمة منشورة له لليمن."),
    ("6B-1a", O6, "CLM-001", "limitations_ar",
     "ورقم الاقتصادات منخفضة الدخل للسياق فقط، وليس معيارًا ولا هدفًا ولا ترتيبًا: فهو متوسط لاقتصادات ذات ظروف متباينة جدًا، "
     "ويشمل اليمن نفسه، ويستند إلى تصنيف الدخل المعتمد في قاعدة بيانات Global Findex 2025، في حين يقتصر رقم اليمن على المناطق "
     "التي بلغها المسح.",
     "ورقما الاقتصادات منخفضة الدخل للسياق فقط، وليسا معيارًا ولا هدفًا ولا ترتيبًا: فهما يتوسطان اقتصادات ذات ظروف متباينة "
     "جدًا، ويشملان اليمن نفسه، ويصنفان الاقتصادات وفق تصنيف الدخل المعتمد في البنك الدولي للسنة المالية 2024، في حين يقتصر "
     "رقم اليمن على المناطق التي بلغها المسح. ولا يُقارَن بنسبة اليمن البالغة 11.9% على التعريف نفسه إلا رقم الحساب لدى "
     "مؤسسة مالية، 24.5%."),
    ("6B-1e", O6, "CLM-001", "change_trigger_en",
     "A later survey of Yemen that asks the mobile-money questions may show a rise caused by the change of questionnaire, not "
     "by a real change in account ownership.",
     "A later survey of Yemen with published mobile-money values may show a rise caused by the change of measurement, not by "
     "a real change in account ownership."),
    ("6B-1e", O6, "CLM-001", "change_trigger_ar",
     "وقد يُظهر مسح لاحق لليمن يطرح أسئلة خدمات الأموال عبر الهاتف ارتفاعًا سببه تغيّر الاستبيان، لا تغيّر فعلي في امتلاك "
     "الحساب.",
     "وقد يُظهر مسح لاحق لليمن تُنشر له قيم لحسابات الأموال عبر الهاتف المحمول ارتفاعًا سببه تغيّر القياس، لا تغيّر فعلي في "
     "امتلاك الحساب."),
    # ------------------------------------------------------------ 6B-1(e): CLM-026, CLM-027, VIS-FINDEX-GAPS, MA-001, 04 note
    ("6B-1e", O6, "CLM-026", "summary_en",
     "Of the other 16, two were not asked in Yemen's survey and 14 have no World Bank published value for Yemen.",
     "Of the other 16, two are mobile-money measures with no valid answer in the World Bank's public data for the study and "
     "no published value, and 14 have no World Bank published value for Yemen."),
    ("6B-1e", O6, "CLM-026", "summary_ar",
     "أما المقاييس الـ16 الأخرى، فلم يُطرح اثنان منها في مسح اليمن، ولا توجد لـ14 منها قيمة ينشرها البنك الدولي لليمن.",
     "أما المقاييس الـ16 الأخرى، فاثنان منها مقياسان لحسابات الأموال عبر الهاتف المحمول لا توجد لهما إجابة صالحة في البيانات "
     "العامة التي نشرها البنك الدولي للدراسة ولا قيمة منشورة، ولا توجد لـ14 منها قيمة ينشرها البنك الدولي لليمن."),
    ("6B-1e", O6, "CLM-026", "universe_en", "and two mobile-money measures that Yemen's survey did not ask.",
     "and two mobile-money measures with no valid answer in the World Bank's public data for the study and no published value."),
    ("6B-1e", O6, "CLM-026", "universe_ar", "ومقياسان لخدمات الأموال عبر الهاتف لم يطرحهما مسح اليمن.",
     "ومقياسان لحسابات الأموال عبر الهاتف المحمول لا توجد لهما إجابة صالحة في البيانات العامة التي نشرها البنك الدولي "
     "للدراسة ولا قيمة منشورة."),
    ("6B-1e", O6, "CLM-026", "limitations_en",
     "two (using and saving with a mobile-money account) were not asked in Yemen's survey, so no value exists for this wave.",
     "two (using and saving with a mobile-money account) have no valid answer in the World Bank's public data for the study "
     "and no published value, so no value exists for this wave."),
    ("6B-1e", O6, "CLM-026", "limitations_ar",
     "ولم يُطرح سؤالا مقياسين منها (استخدام حساب لخدمات الأموال عبر الهاتف والادخار به) في مسح اليمن، لذلك لا توجد لهما قيمة في "
     "هذه الموجة.",
     "ولا توجد لمقياسين منها (استخدام حساب أموال عبر الهاتف المحمول والادخار به) إجابة صالحة في البيانات العامة التي نشرها "
     "البنك الدولي للدراسة ولا قيمة منشورة، لذلك لا توجد لهما قيمة في هذه الموجة."),
    ("6B-1e", O6, "CLM-026", "currentness_en", "the two that Yemen's survey did not ask have none for this wave.",
     "the two mobile-money measures have none for this wave."),
    ("6B-1e", O6, "CLM-026", "currentness_ar", "ولا قيمة في هذه الموجة للمقياسين اللذين لم يطرحهما مسح اليمن.",
     "ولا قيمة في هذه الموجة لمقياسَي حسابات الأموال عبر الهاتف المحمول."),
    ("6B-1e", O6, "CLM-027", "limitations_en",
     "but Yemen's 2021 study did not ask the mobile-money questions, so its 11.9% also reflects accounts at financial "
     "institutions;",
     "but the World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
     "institution is the same as its account figure, so Yemen's 11.9% for the 2021 wave also reflects accounts at financial "
     "institutions;"),
    ("6B-1e", O6, "CLM-027", "limitations_ar",
     "لكن دراسة اليمن لعام 2021 لم تطرح أسئلة هذه الخدمات، فتعكس نسبة 11.9% فيها كذلك الحسابات لدى المؤسسات المالية؛",
     "لكن البنك الدولي لا ينشر أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية مساوٍ لرقم "
     "ملكية الحساب؛ فتعكس نسبة 11.9% في موجة 2021 كذلك الحسابات لدى المؤسسات المالية؛"),
    ("6B-1e", O6, "VIS-FINDEX-GAPS", "summary_en", "(the survey did not ask the mobile-money questions)",
     "(the World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
     "institution is the same as its account figure)"),
    ("6B-1e", O6, "VIS-FINDEX-GAPS", "summary_ar", "(لم يطرح المسح أسئلة خدمات الأموال عبر الهاتف)",
     "(لا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية مساوٍ لرقم "
     "ملكية الحساب)"),
    ("6B-1e", "11_VISUAL_LIBRARY", "VIS-FINDEX-GAPS", "accessible_summary_en", "(the survey did not ask the mobile-money questions)",
     "(the World Bank publishes no mobile-money-account figure for Yemen, and its figure for an account at a financial "
     "institution is the same as its account figure)"),
    ("6B-1e", "11_VISUAL_LIBRARY", "VIS-FINDEX-GAPS", "accessible_summary_ar", "(لم يطرح المسح أسئلة خدمات الأموال عبر الهاتف)",
     "(لا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية مساوٍ لرقم "
     "ملكية الحساب)"),
    ("6B-1e", O6, "VIS-FINDEX-GAPS", "definition_en",
     "In Yemen's survey the mobile-money questions were not asked, so the values reflect accounts at financial institutions.",
     VALS_EN),
    ("6B-1e", O6, "VIS-FINDEX-GAPS", "definition_ar",
     "ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تعكس القيم الحسابات لدى المؤسسات المالية.", "و" + VALS_AR),
    ("6B-1e", "10_MEASUREMENT_AGENDA", "MA-001", "guardrail_en",
     "Yemen's 2021 study did not ask the mobile-money questions: if a new survey asks them, part of any rise in account "
     "ownership may come from the wider questionnaire, not from real change,",
     "The World Bank publishes no mobile-money-account figure for Yemen's 2021 study, and its figure for an account at a "
     "financial institution is the same as its account figure: if a new survey publishes mobile-money values, part of any "
     "rise in account ownership may come from the wider measure, not from real change,"),
    ("6B-1e", "10_MEASUREMENT_AGENDA", "MA-001", "guardrail_ar",
     "ولم تطرح دراسة اليمن لعام 2021 أسئلة خدمات الأموال عبر الهاتف: فإذا طرحها مسح جديد فقد يأتي جزء من أي ارتفاع في امتلاك "
     "الحساب من اتساع الاستبيان لا من تغيّر فعلي،",
     "ولا ينشر البنك الدولي أي رقم عن حسابات الأموال عبر الهاتف المحمول لدراسة اليمن لعام 2021، ورقمه للحساب لدى مؤسسة مالية "
     "مساوٍ لرقم ملكية الحساب: فإذا نشر مسح جديد قيمًا لهذه الحسابات فقد يأتي جزء من أي ارتفاع في امتلاك الحساب من اتساع "
     "القياس لا من تغيّر فعلي،"),
    ("6B-1e", "04_NAV_UX", "UI-VIS-NOTE-FINDEX-ACCOUNT-FI", 2,
     "Yemen's survey did not ask the mobile-money questions, so the World Bank's values for an account at a financial "
     "institution are the same as for any account.", VALS_EN),
    ("6B-1e", "04_NAV_UX", "UI-VIS-NOTE-FINDEX-ACCOUNT-FI", 3,
     "لم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تطابق قيمُ البنك الدولي لحساب لدى مؤسسة مالية قيمَه لأي حساب.",
     VALS_AR),
    ("6B-1e", "25_FINDEX_BASELINE", "WB-FINDEX-OBS-2022-001", "caveat",
     "In Yemen's survey the mobile-money questions were not asked: fiaccount.t.d equals account.t.d",
     "The World Bank publishes no mobile-money-account value for Yemen, and the study's public metadata print no valid answer "
     "to the mobile-money items: fiaccount.t.d equals account.t.d"),
    # ------------------------------------------------------------ 6B-1(c) with 6B-5(a): VIS-FINDEX-FLOW-CHANNELS
    ("6B-1c", O6, "VIS-FINDEX-FLOW-CHANNELS", "limitations_en", CH_OLD_EN, CH_NEW_EN),
    ("6B-1c", O6, "VIS-FINDEX-FLOW-CHANNELS", "limitations_ar", CH_OLD_AR, CH_NEW_AR),
    ("6B-1c", "11_VISUAL_LIBRARY", "VIS-FINDEX-FLOW-CHANNELS", "prohibited_inference_en", CH_OLD_EN, CH_NEW_EN),
    ("6B-1c", "11_VISUAL_LIBRARY", "VIS-FINDEX-FLOW-CHANNELS", "prohibited_inference_ar", CH_OLD_AR, CH_NEW_AR),
    ("6B-5", O6, "VIS-FINDEX-FLOW-CHANNELS", "summary_en", FLOW_SUM_END_EN, FLOW_SUM_END_EN + BOUND_EN),
    ("6B-5", O6, "VIS-FINDEX-FLOW-CHANNELS", "summary_ar", FLOW_SUM_END_AR, FLOW_SUM_END_AR + BOUND_AR),
    ("6B-5", "11_VISUAL_LIBRARY", "VIS-FINDEX-FLOW-CHANNELS", "accessible_summary_en", FLOW_SUM_END_EN, FLOW_SUM_END_EN + BOUND_EN),
    ("6B-5", "11_VISUAL_LIBRARY", "VIS-FINDEX-FLOW-CHANNELS", "accessible_summary_ar", FLOW_SUM_END_AR, FLOW_SUM_END_AR + BOUND_AR),
    # ------------------------------------------------------------ 6B-1(b): the 2014 borrowing vintage
    ("6B-1b", O6, "CLM-028", "summary_en", "and 0.4% from a financial institution.",
     "and 0.4% from a financial institution (as printed in the Little Data Book 2015; the World Bank's current database gives "
     "0.6% for the same 2014 measure)."),
    ("6B-1b", O6, "CLM-028", "summary_ar", "و0.4% من مؤسسة مالية.",
     "و0.4% من مؤسسة مالية (كما طُبعت في كتيّب البيانات الموجز عن الشمول المالي لعام 2015؛ وتعطي قاعدة البيانات الحالية "
     "للبنك الدولي 0.6% للمقياس نفسه في 2014)."),
    ("6B-1b", O6, "VIS-BORROWING-SOURCES-2014", "summary_en", "and 0.4% from a financial institution.",
     "and 0.4% from a financial institution (as printed in the Little Data Book 2015; the World Bank's current database gives "
     "0.6% for the same 2014 measure)."),
    ("6B-1b", O6, "VIS-BORROWING-SOURCES-2014", "summary_ar", "و0.4% من مؤسسة مالية.",
     "و0.4% من مؤسسة مالية (كما طُبعت في كتيّب البيانات الموجز عن الشمول المالي لعام 2015؛ وتعطي قاعدة البيانات الحالية "
     "للبنك الدولي 0.6% للمقياس نفسه في 2014)."),
    ("6B-1b", "02_SITE_MAP", "/evidence/CLM-028/", "meta_description_en",
     "In the 2014 World Bank weighted profile, 65.9% of adults reported borrowing any money; 51.7% from family or friends, "
     "0.4% from a financial institution.",
     "In the 2014 World Bank profile as printed, 65.9% of adults borrowed any money, 51.7% from family or friends and 0.4% "
     "from a financial institution (0.6% in the current database)."),
    ("6B-1b", "02_SITE_MAP", "/evidence/CLM-028/", "meta_description_ar",
     "في الملف القطري الموزون للبنك الدولي لعام 2014، أفاد 65.9% من البالغين بأنهم اقترضوا أي مبلغ، و51.7% اقترضوا من الأسرة "
     "أو الأصدقاء، و0.4% من مؤسسة مالية.",
     "في الملف القطري للبنك الدولي لعام 2014 كما طُبع، اقترض 65.9% من البالغين أي مبلغ، و51.7% من الأسرة أو الأصدقاء، و0.4% "
     "من مؤسسة مالية (0.6% في قاعدة البيانات الحالية)."),
    ("6B-1b", "33_ANALYTICS_MASTER", "INS-023", 4, "versus 0.4% borrowing from a financial institution,",
     "versus 0.4% borrowing from a financial institution (as printed in the Little Data Book 2015; the World Bank's current "
     "database gives 0.6% for the same 2014 measure),"),
    # ------------------------------------------------------------ 6B-2(a): CLM-059
    ("6B-2a", O6, "CLM-059", "summary_en", YLG_OLD_EN, YLG_EN),
    ("6B-2a", O6, "CLM-059", "summary_ar", YLG_OLD_AR, YLG_AR),
    ("6B-2a", O6, "CLM-059", "definition_en",
     "; and the transactions, guarantees and loan principal of the Yemen Loan Guarantee Program (YLG) since 2017, as the OECD "
     "reports them.",
     "; the letters of guarantee that the Yemen Loan Guarantee Program (YLG) reports issuing, and their amounts, for 2022 and "
     "by year for 2018–2022; and YLG's transactions, guarantees and loan principal since 2017, as the OECD reports them."),
    ("6B-2a", O6, "CLM-059", "definition_ar",
     "والمعاملات والضمانات وأصل القروض في برنامج ضمان القروض اليمني (YLG) منذ عام 2017، كما تفيد بها منظمة التعاون الاقتصادي "
     "والتنمية (OECD).",
     "وخطابات الضمان التي يفيد برنامج ضمان القروض في اليمن (YLG) بإصدارها ومبالغها لعام 2022 وبحسب السنة للفترة 2018–2022؛ "
     "ومعاملات البرنامج وضماناته وأصل قروضه منذ عام 2017، كما تفيد بها منظمة التعاون الاقتصادي والتنمية (OECD)."),
    ("6B-2a", O6, "CLM-059", "universe_en", "; loan transactions guaranteed by the Yemen Loan Guarantee Program (YLG)",
     "; letters of guarantee issued by the Yemen Loan Guarantee Program (YLG), as it reports them, and loan transactions it "
     "guaranteed, as the OECD reports them"),
    ("6B-2a", O6, "CLM-059", "universe_ar", "ومعاملات القروض التي ضمنها برنامج ضمان القروض اليمني (YLG).",
     "وخطابات الضمان التي أصدرها برنامج ضمان القروض في اليمن (YLG) كما يفيد بها، ومعاملات القروض التي ضمنها كما تفيد بها "
     "منظمة التعاون الاقتصادي والتنمية."),
    ("6B-2a", O6, "CLM-059", "method_en",
     "The YLG figures as reported by the OECD in Promoting Economic Resilience in Yemen (2026), page 32.",
     "YLG figures from two publishers, shown side by side and not combined: the programme's own Annual Report 2022, whose "
     "amounts are in thousand YER and are printed rounded as YER 6.4 billion and YER 9.4 billion, and the OECD's Promoting "
     "Economic Resilience in Yemen (2026), page 32. The 2018–2022 total, 6,976, is the sum of the programme's yearly counts in "
     "its Annex I, calculated here; each Annex I breakdown also totals 6,976."),
    ("6B-2a", O6, "CLM-059", "method_ar",
     "وأرقام برنامج YLG كما أوردتها منظمة التعاون الاقتصادي والتنمية (OECD) في تقرير «تعزيز المرونة الاقتصادية في اليمن» "
     "(2026)، الصفحة 32.",
     "وأرقام برنامج ضمان القروض في اليمن من مصدرين يُعرضان جنبًا إلى جنب ولا يُدمجان: التقرير السنوي للبرنامج لعام 2022، "
     "ومبالغه بآلاف الريالات وتُطبع مقرّبة إلى 6.4 مليار ريال و9.4 مليار ريال، وتقرير منظمة التعاون الاقتصادي والتنمية (OECD) "
     "«تعزيز المرونة الاقتصادية في اليمن» (2026)، الصفحة 32. ومجموع 2018–2022، أي 6,976، هو حاصل جمع الأعداد السنوية للبرنامج "
     "في ملحقه الأول، احتُسب هنا؛ ويبلغ مجموع كل تصنيف في الملحق الأول 6,976 أيضًا."),
    ("6B-2a", O6, "CLM-059", "period_en", "cumulative since 2017, reported in 2026 (YLG)",
     "2022 (issued during the year) and 2018–2022 (yearly counts) (YLG Annual Report 2022); since 2017, cutoff not stated "
     "(OECD, on YLG)"),
    ("6B-2a", O6, "CLM-059", "period_ar", "وتراكمي منذ 2017، أُبلغ عنه في 2026 (YLG)",
     "و2022 (ما صدر خلال العام) و2018–2022 (أعداد سنوية) (التقرير السنوي لبرنامج ضمان القروض في اليمن 2022)؛ ومنذ 2017، "
     "من دون تاريخ انتهاء معلن (منظمة التعاون الاقتصادي والتنمية، عن البرنامج)"),
    ("6B-2a", O6, "CLM-059", "limitations_en", YLG_DNE_OLD_EN, YLG_DNE_EN + VER_EN),
    ("6B-2a", O6, "CLM-059", "limitations_ar", YLG_DNE_OLD_AR, YLG_DNE_AR + VER_AR),
    ("6B-2a", O6, "CLM-059", "currentness_en",
     "The YLG figures are cumulative since 2017 as reported in a report published in 2026, which states no end date for that "
     "period.",
     "The programme's own figures refer to 2022 and, by year, to 2018–2022. The OECD's YLG figures are cumulative since 2017, "
     "as reported in 2026, with no stated end date."),
    ("6B-2a", O6, "CLM-059", "currentness_ar",
     "، وأرقام برنامج YLG تراكمية منذ عام 2017 كما وردت في تقرير نُشر عام 2026، لا يذكر تاريخًا لنهاية تلك الفترة.",
     ". وتعود أرقام برنامج ضمان القروض في اليمن الصادرة عنه إلى عام 2022، وبحسب السنة إلى الفترة 2018–2022؛ أما أرقام منظمة "
     "التعاون الاقتصادي والتنمية عن البرنامج فتراكمية منذ عام 2017 كما وردت في تقرير نُشر عام 2026، من دون تاريخ معلن "
     "لنهايتها."),
    ("6B-2a", "02_SITE_MAP", "/evidence/CLM-059/", "meta_description_en",
     "and, via the OECD, by the Yemen Loan Guarantee Program describe the programmes, not all MSMEs in Yemen.",
     "and, side by side, by the Yemen Loan Guarantee Program and the OECD describe the programmes, not all MSMEs in Yemen."),
    ("6B-2a", "02_SITE_MAP", "/evidence/CLM-059/", "meta_description_ar",
     "وأرقام برنامج ضمان القروض اليمني كما تنقلها منظمة التعاون الاقتصادي والتنمية، تصف البرنامجين",
     "وأرقام برنامج ضمان القروض في اليمن ومنظمة التعاون الاقتصادي والتنمية جنبًا إلى جنب، تصف البرنامجين"),
    # ------------------------------------------------------------ 6B-2(b), (c), (d)
    ("6B-2b", "34_EVIDENCE_PASSPORTS", "EP-SMEPS-2024-PROGRAMME", "object",
     "SMEPS 2024 programme reach, jobs and disbursement", "SMEPS 2024 programme reach and disbursement"),
    ("6B-2c", O6, "CLM-062", "limitations_en",
     "The document does not name the survey further, and its question and sample differ from the 2022 survey's.",
     SURVEY141_EN + " Its question and sample differ from the 2022 survey's."),
    ("6B-2c", O6, "CLM-062", "limitations_ar",
     "ولا تسمّي الوثيقة المسح بأكثر من ذلك، ويختلف سؤاله وعينته عن سؤال مسح 2022 وعينته.",
     "و" + SURVEY141_AR + " ويختلف سؤاله وعينته عن سؤال مسح 2022 وعينته."),
    ("6B-2d", "10_MEASUREMENT_AGENDA", "MA-004", "current_evidence_en",
     "can each be used within its own scope; neither supplies a current representative national MSME finance baseline.",
     "can each be used within its own scope, and the Yemen Loan Guarantee Program's reports count guarantees issued, not firms; "
     "none of them supplies a current representative national MSME finance baseline."),
    ("6B-2d", "10_MEASUREMENT_AGENDA", "MA-004", "current_evidence_ar",
     "معلومات مفيدة داخل نطاق كل منهما، ولا يوفر أيٌّ منهما خط أساس",
     "معلومات مفيدة داخل نطاق كل منهما، أما تقارير برنامج ضمان القروض في اليمن فتعدّ خطابات الضمان الصادرة لا المنشآت؛ ولا "
     "يوفر أيٌّ منها خط أساس"),
    ("6B-2d", "10_MEASUREMENT_AGENDA", "MA-004", "missing_evidence_en",
     "covering finance need, application, approval or rejection, amount, terms, source, use, repayment pressure and outcome.",
     "covering finance need, application, approval or rejection, amount, terms, source, use, repayment pressure and outcome; "
     "and unique-firm identification across programme registers, and whether guaranteed loans add to lending "
     "(additionality)."),
    ("6B-2d", "10_MEASUREMENT_AGENDA", "MA-004", "missing_evidence_ar",
     "والمصدر والاستخدام وضغوط السداد والنتيجة.",
     "والمصدر والاستخدام وضغوط السداد والنتيجة؛ وتحديد هوية المنشأة الواحدة عبر سجلات البرامج، ومعرفة ما إذا كانت القروض "
     "المضمونة تضيف إلى الإقراض (الإضافية)."),
    # ------------------------------------------------------------ 6B-4(a): CLM-041 (V4: 1.838 is this resource's ratio, not the
    # IMF's; trade relied mainly on UN Comtrade, with government-reported data used for the split; "all grants" are the official
    # grants from Saudi Arabia and the UAE)
    ("6B-4a", O6, "CLM-041", "limitations_en",
     "The constant ratio of 1.838 between the CBY-Aden and IMF remittance series over 2021–2024, and the 33% population share "
     "that the IMF used for areas under the internationally recognized government, do not apply to other balance-of-payments "
     "components.",
     "The ratio of 1.838 is this resource's ratio of the CBY-Aden remittance series to the IMF's over 2021–2024, and it is "
     "specific to remittances. The 33% population ratio is the IMF's stated rule, as proposed by the authorities, for "
     "splitting its external-sector estimates between areas under the internationally recognized government and other areas; "
     "for trade, the IMF relied mainly on UN Comtrade data and used trade data reported by the government for that split, "
     "and it allocates the official grants from Saudi Arabia and the United Arab Emirates wholly to the government. Neither "
     "ratio converts CBY-Aden values into IMF values for any component."),
    ("6B-4a", O6, "CLM-041", "limitations_ar",
     "لا تنطبق النسبة الثابتة البالغة 1.838 بين سلسلتي الحوالات لدى البنك المركزي اليمني – عدن وصندوق النقد الدولي خلال "
     "2021–2024، ولا حصة السكان البالغة 33% التي استخدمها الصندوق للمناطق الخاضعة للحكومة المعترف بها دوليًا، على مكونات أخرى "
     "من ميزان المدفوعات.",
     "النسبة 1.838 هي نسبة سلسلة الحوالات لدى البنك المركزي اليمني – عدن إلى سلسلة صندوق النقد الدولي خلال 2021–2024 كما "
     "احتسبها هذا المورد، وهي خاصة بالحوالات. أما نسبة السكان البالغة 33% فهي القاعدة التي يذكرها الصندوق، كما اقترحتها "
     "السلطات، لتقسيم تقديراته للقطاع الخارجي بين المناطق الخاضعة للحكومة المعترف بها دوليًا والمناطق الأخرى؛ وفي التجارة "
     "اعتمد الصندوق أساسًا على بيانات قاعدة UN Comtrade واستخدم بيانات التجارة التي أبلغت عنها الحكومة لذلك التقسيم، وينسب "
     "المنح الرسمية من السعودية والإمارات بكاملها إلى الحكومة. ولا تحوّل أيٌّ من النسبتين قيم البنك المركزي اليمني – عدن إلى "
     "قيم الصندوق لأي مكون."),
    # ------------------------------------------------------------ 6B-4(b): CLM-007 and the 23 caveat
    ("6B-4b", O6, "CLM-007", "summary_en",
     "with 33% allocated to areas under the internationally recognized government by population ratio.",
     "with 33% allocated to areas under the internationally recognized government by population ratio, as proposed by the "
     "authorities."),
    ("6B-4b", O6, "CLM-007", "summary_ar", "نُسبت إلى المناطق الخاضعة للحكومة المعترف بها دوليًا وفق نسبة السكان.",
     "نُسبت إلى المناطق الخاضعة للحكومة المعترف بها دوليًا وفق نسبة السكان، كما اقترحتها السلطات."),
    ("6B-4b", O6, "CLM-007", "limitations_en",
     "It does not measure hawala volume, payment-system settlement or how inflows are distributed among households.",
     "It does not measure hawala volume, payment-system settlement or how inflows are distributed among households. The IMF "
     "publishes no whole-of-Yemen total; dividing the series by 33% gives a figure the IMF does not publish."),
    ("6B-4b", O6, "CLM-007", "limitations_ar",
     "لا يقيس هذا الدليل حجم التحويلات عبر نظام الحوالة غير الرسمي، ولا التسوية عبر نظام المدفوعات، ولا توزيع التدفقات على "
     "الأسر.",
     "لا يقيس هذا الدليل حجم التحويلات عبر نظام الحوالة غير الرسمي، ولا التسوية عبر نظام المدفوعات، ولا توزيع التدفقات على "
     "الأسر. ولا ينشر الصندوق أي إجمالي لليمن كله؛ وقسمة السلسلة على 33% تعطي رقمًا لا ينشره الصندوق."),
]

# 23_REMITTANCES caveat_en on RMO-IMF-2018-HIST … RMO-IMF-2024-HIST (6B-4(b))
RMO_IDS = [f"RMO-IMF-{y}-HIST" for y in range(2018, 2025)]
RMO_OLD = ("Not an observed or reported flow: estimated with a demographic and behavioural model (number of Yemenis abroad, "
           "family size, average transfer amounts); the value for areas under the internationally recognized government is 33% "
           "of the modelled total of personal transfers, by population ratio, as proposed by the authorities (")
RMO_NEW = ("Not an observed or reported flow. The IMF states that a demographic and behavioural model (number of Yemenis abroad, "
           "family size, average transfer amounts) and a 33% population ratio for areas under the internationally recognized "
           "government, as proposed by the authorities, were applied; the IMF publishes no whole-of-Yemen total and none is "
           "derived here (CLOSE-6D, 11 October 2026; ")

# 6B-4(c): CLM-039 (V1: WDI BX.TRF.PWKR.CD.DT, Yemen, last non-null 2016 = 3,770,584,000 current US$; 2017-2025 null). The
# "other World Bank interfaces and earlier documented retrievals" have no public locator each (the earlier retrievals are
# lineage, EP-WB-WDI-REMITTANCE-VINTAGE-K04 and CON-045), so the sentence goes; Brief 40's panel (a) stays as the located case.
WHOLE = [
    ("6B-4c", O6, "CLM-039", "summary_en", "World Bank public remittance interfaces do not expose Yemen history uniformly.",
     "World Development Indicators holds no Yemen observation of personal remittances received after 2016 (last: USD 3,770.6 "
     "million in 2016; checked 11 October 2026). What one public interface holds is not evidence that later underlying data "
     "are absent. One World Bank publication is also inconsistent on Yemen: the note to Figure A.4.2 of Migration and "
     "Development Brief 40 (June 2024) says Yemen is excluded “due to data availability”, yet panel (a), remittances in US "
     "dollars for 2023, shows a value for Yemen, and only panel (b), remittances as a share of GDP, omits it. The brief does "
     "not say which panel the note applies to, and this resource takes no value from the figure."),
    ("6B-4c", O6, "CLM-039", "summary_ar", "لا تعرض واجهات البنك الدولي العامة الخاصة بالحوالات",
     "لا تتضمن مؤشرات التنمية العالمية (WDI) أي مشاهدة لليمن للتحويلات الشخصية المستلمة بعد عام 2016 (آخرها: 3,770.6 مليون "
     "دولار أمريكي في 2016؛ جرى التحقق في 11 أكتوبر 2026). وما تتضمنه واجهة عامة واحدة ليس دليلًا على غياب البيانات الأحدث من "
     "مجموعة البيانات الأساسية. ويقع منشور واحد للبنك الدولي أيضًا في عدم اتساق بشأن اليمن: إذ تذكر الملاحظة المرافقة للشكل "
     "A.4.2 في موجز الهجرة والتنمية رقم 40 (يونيو 2024) أن اليمن مستبعد «لأسباب تتعلق بتوفر البيانات»، غير أن اللوحة (a)، "
     "وهي التحويلات بالدولار الأمريكي لعام 2023، تعرض قيمة لليمن، ولا تغفله إلا اللوحة (b)، وهي التحويلات نسبةً إلى الناتج "
     "المحلي الإجمالي. ولا يحدد الموجز اللوحة التي تنطبق عليها الملاحظة، ولا يأخذ هذا المورد أي قيمة من الشكل."),
    ("6B-4c", O6, "CLM-039", "definition_en", "The difference, as reviewed on 10 September 2026,",
     "The span of Yemen observations of personal remittances received that World Development Indicators holds (checked 11 "
     "October 2026), and a World Bank publication that shows a later Yemen value."),
    ("6B-4c", O6, "CLM-039", "definition_ar", "الفرق، كما اطُّلع عليه في 10 سبتمبر 2026،",
     "نطاق مشاهدات اليمن للتحويلات الشخصية المستلمة في مؤشرات التنمية العالمية (جرى التحقق في 11 أكتوبر 2026)، ومنشور للبنك "
     "الدولي يعرض قيمة أحدث لليمن."),
    ("6B-4c", O6, "CLM-039", "method_en", "World Bank data interfaces, including World Development Indicators",
     "World Development Indicators series BX.TRF.PWKR.CD.DT for Yemen, read through the World Bank's open data interface on "
     "11 October 2026; Migration and Development Brief 40 (June 2024), Figure A.4.2."),
    ("6B-4c", O6, "CLM-039", "method_ar", "واجهات بيانات البنك الدولي/WDI",
     "سلسلة مؤشرات التنمية العالمية BX.TRF.PWKR.CD.DT لليمن، قُرئت عبر واجهة البيانات المفتوحة للبنك الدولي في 11 أكتوبر "
     "2026؛ وموجز الهجرة والتنمية رقم 40 (يونيو 2024)، الشكل A.4.2."),
    ("6B-4c", O6, "CLM-039", "period_en", "World Bank public data interfaces as reviewed on 10 September 2026",
     "World Development Indicators as checked on 11 October 2026; Migration and Development Brief 40 (June 2024)"),
    ("6B-4c", O6, "CLM-039", "period_ar", "واجهات بيانات البنك الدولي العامة كما اطُّلع عليها في 10 سبتمبر 2026",
     "مؤشرات التنمية العالمية كما جرى التحقق منها في 11 أكتوبر 2026؛ وموجز الهجرة والتنمية رقم 40 (يونيو 2024)"),
    ("6B-4c", O6, "CLM-039", "currentness_en", "The interfaces were reviewed on 10 September 2026",
     "World Development Indicators was checked on 11 October 2026, and what it holds may change. The record should not be "
     "read as describing a later state of the interface unless it is checked again."),
    ("6B-4c", O6, "CLM-039", "currentness_ar", "اطُّلع على الواجهات في 10 سبتمبر 2026",
     "جرى التحقق من مؤشرات التنمية العالمية في 11 أكتوبر 2026، وقد يتغير ما تتضمنه؛ ولا يُقرأ السجل على أنه يصف ما تعرضه "
     "الواجهة لاحقًا ما لم يُتحقق منها مجددًا."),
    ("6B-4c", O6, "CLM-039", "limitations_en", "The difference does not show that data were deleted or withdrawn",
     "What one interface holds does not show that data were deleted or withdrawn, or why any correction was made, and one "
     "public interface's observations are not a substitute for another's. | What one interface shows does not establish that "
     "the underlying data are absent or deleted, or why they were revised."),
    ("6B-4c", O6, "CLM-039", "limitations_ar", "لا يثبت الاختلاف أن البيانات حُذفت أو سُحبت",
     "لا يثبت ما تتضمنه واجهة واحدة أن البيانات حُذفت أو سُحبت، ولا سبب أي تصحيح، ولا تحل مشاهدات واجهة عامة محل مشاهدات "
     "واجهة أخرى. | ولا يثبت ما تعرضه واجهة واحدة غياب البيانات الأساسية أو حذفها أو سبب مراجعتها."),
]

# ---------------------------------------------------------------------------------------------------------------- 06 value_states
WB = "SRC-WB-FINDEX-AGG-2022"
ED = "SRC-WB-FINDEX-2025-EDITION"
YLG = "SRC-YLG-AR-2022"
OECD = "SRC-OECD-YEM-RESILIENCE-001"
R11 = "; read 11 October 2026"


def vs(t, k, s, src=None, loc=None):
    e = {"t": t, "k": k, "s": s}
    if src:
        e["src"] = src
    if loc:
        e["loc"] = loc
    return e


LIC_FI = ("api.worldbank.org/v2/country/LIC/indicator/fiaccount.t.d?date=2021&format=json&source=28 (World Bank label "
          "'Bank or similar financial institution account (% age 15+)'), value 24.4577497822049, lastupdated 2025-10-06; "
          "snapshot " + FX + R11)
BOUND_LOC = ("CauseWay calculation from two published shares: (fh2 31.9313981068809 - fiaccount.t.d 11.9033656433415) / "
             "31.9313981068809 = 62.722066%; api.worldbank.org/v2/country/YEM/indicator/fh2 and fiaccount.t.d, source 28, date "
             "2022, lastupdated 2025-10-06; snapshot " + FX + R11)
VS = {
    "CLM-001": (["19"], [
        vs("24.5%", "v", "READ", ED, LIC_FI),
        vs("1,135", "v", "READ", ED, "api.worldbank.org/v2/sources/28/country/LIC/series/account.t.d/metadata, SpecialNotes: "
           "'The World Bank's FY24 classification is used, where low-income economies had a 2022 Atlas GNI per capita of "
           "$1,135 or less.'" + R11),
    ]),
    "CLM-028": ([], [vs("0.6%", "v", "READ", WB, "api.worldbank.org/v2/country/YEM/indicator/fin22a?date=2014&format=json&source=28 "
                        "(World Bank label 'Borrowed from a formal bank or similar financial institution (% age 15+)'), value "
                        "0.602877248196788, lastupdated 2025-10-06; snapshot " + FX + R11)]),
    "VIS-BORROWING-SOURCES-2014": ([], [vs("0.6%", "v", "READ", WB, "api.worldbank.org/v2/country/YEM/indicator/fin22a?date=2014"
                                           "&format=json&source=28, value 0.602877248196788, lastupdated 2025-10-06; snapshot "
                                           + FX + R11)]),
    "VIS-FINDEX-FLOW-CHANNELS": ([], [
        vs("62.7%", "v", "DERIVED", WB, BOUND_LOC),
        vs("11.9%", "v", "READ", WB, "api.worldbank.org/v2/country/YEM/indicator/fiaccount.t.d?date=2022&format=json&source=28, "
           "value 11.9033656433415, lastupdated 2025-10-06; snapshot " + FX + R11),
    ]),
    "CLM-059": ([], [
        vs("3,387", "v", "READ", YLG, "YLGP Annual Report 2022, p.8 ('During the fiscal year 2022, 3387 letters of guarantee were "
           "issued'), p.14 (Grand Total), p.4 (panel)" + R11),
        vs("6.4", "v", "READ", YLG, "YLGP Annual Report 2022, p.8 ('in the amount of YER 6.4 billion'); p.14 'Guarantees Amount "
           "(Thousand YER)' Grand Total 6,397,627.81" + R11),
        vs("9.4", "v", "READ", YLG, "YLGP Annual Report 2022, p.8 ('to cover loans worth YER 9.4 billion'); p.14 'Guaranteed Loans "
           "Amount (Thousand YER)' Grand Total 9,371,245.29" + R11),
        vs("12", "v", "READ", YLG, "YLGP Annual Report 2022, p.4 ('12 Total PFIs'), p.17" + R11),
        vs("693", "v", "READ", YLG, "YLGP Annual Report 2022, p.15, Gender table, row 'FEMALE' 693 (text: 'women-led MSMEs')" + R11),
        vs("20%", "v", "READ", YLG, "YLGP Annual Report 2022, p.4 panel '20% Women-led MSMEs'; p.15 'about 20% in 2022'" + R11),
        vs("6,976", "v", "DERIVED", YLG, "Sum of Annex I yearly guarantees, p.29: 301 (2018) + 691 (2019) + 1,270 (2020) + 1,327 "
           "(2021) + 3,387 (2022) = 6,976; each Annex I split (pp.29-31) also totals 6,976; the report does not print the sum"
           + R11),
        vs("72.7%", "v", "READ", OECD, "OECD (2026) Promoting Economic Resilience in Yemen, printed p.32 (PDF p.34): 'of which "
           "72.7% were granted to men-owned businesses'" + R11),
        vs("104%", "v", "DERIVED", OECD, "OECD (2026), printed p.32 (PDF p.34): sector shares of the amount of guarantees 36 + 29 + "
           "19 + 9 + 7 + 4 = 104" + R11),
    ]),
    "CLM-039": (["10 September 2026"], [
        vs("3,770.6", "v", "READ", "SRC-WB-WDI-REMIT-YEM-CURRENT", "api.worldbank.org/v2/country/YEM/indicator/BX.TRF.PWKR.CD.DT"
           "?format=json&per_page=100 (Personal remittances, received (current US$)), 2016 = 3770584000, the last non-null "
           "value (2017-2025 null), lastupdated 2026-10-08; snapshot " + FX + R11),
        vs("11 October 2026", "d", "SITE"),
    ]),
}

# ---------------------------------------------------------------------------------------------------------------- 6B-3(a)
# V3 read the certified copy (cby-ye.com/files/62c2edbaad8eb.pdf): Art. 31(2) is a flat cap (full value up to two million
# rials, two million above it; no partial cover beyond); foreign currency and liquidation are decided by «البنك المركزي»;
# the ceiling may only be raised (Council of Ministers, on the Board's proposal); Art. 33 has the three rules; Art. 13(1)
# «يدفع البنك» 0.002. Constraint (iii): the law requires it. Constraint (iv): the law's own term, and no authority is assigned.
DI_EN = ("Law No. 21 of 2008, which names the scheme a guarantee of bank deposits, provides that deposits in Yemeni rials are "
         "guaranteed in full where a deposit is YER 2,000,000 or less, and for two million rials where it is larger (Art. 31); "
         "deposits in a foreign currency are guaranteed only if the Central Bank decides to subject them to the law. For this "
         "purpose, all of one person's accounts at the same bank, in any of its branches, count as one; the guarantee on a "
         "joint account is divided among its holders by their shares; and the person's obligations to the bank, including as "
         "guarantor of another of its debtors and whether or not they are due, are set off against the person's deposits, the "
         "remaining credit balance being the deposit the guarantee is paid on (Art. 33). The guarantee becomes payable if the "
         "Central Bank decides to liquidate the bank. The law requires each bank to pay an annual contribution of 0.2% of the "
         "deposits subject to it (Art. 13). The two-million-rial ceiling is the figure of 2008; the law allows it to be raised "
         "by decision of the Council of Ministers, and this resource has found no published revision. The law predates the "
         "present institutional situation, in which the Central Bank of Yemen – Aden (CBY-Aden) and the Central Bank of Yemen "
         "in Sana'a each operate, and this resource does not establish which authority would take the decisions the law gives "
         "to “the Central Bank”. The law does not show that the scheme operates today: no source here reports the "
         "Institution's financial statements, fund size, contributions collected or any payout, and the 2025 decision does "
         "not establish that cover operates.")
DI_AR = ("ينص القانون رقم (21) لسنة 2008، الذي يسمي النظام ضمانًا للودائع المصرفية، على أن الودائع بالريال اليمني تُضمن بكامل "
         "قيمتها إذا كانت الوديعة مليوني ريال (2,000,000 ريال) أو أقل، ويكون الضمان مليوني ريال إذا زادت على ذلك (المادة 31)؛ "
         "ولا تُضمن الودائع بالعملة الأجنبية إلا إذا قرر البنك المركزي إخضاعها للقانون. ولهذا الغرض تُعدّ حسابات الشخص الواحد "
         "لدى البنك نفسه، في أي من فروعه، حسابًا واحدًا؛ ويوزَّع الضمان في الحساب المشترك بين أصحابه بنسبة حصة كل منهم؛ "
         "ويُجرى التقاصّ بين ودائع الشخص وما عليه من التزامات للبنك، ولو بصفته كفيلًا لأحد مديني البنك، مستحقةً كانت أم لا، "
         "ويكون الرصيد الدائن الباقي هو الوديعة التي يُدفع عنها الضمان (المادة 33). ويُستحق الضمان إذا قرر البنك المركزي "
         "تصفية البنك. ويُلزم القانون كل بنك بدفع اشتراك سنوي بنسبة اثنين في الألف (0.2%) من الودائع الخاضعة له (المادة 13). "
         "وسقف المليوني ريال هو رقم عام 2008، ويجيز القانون زيادته بقرار من مجلس الوزراء، ولم يجد هذا المورد أي تعديل منشور "
         "له. والقانون سابق للوضع المؤسسي الحالي الذي يعمل فيه البنك المركزي اليمني – عدن والبنك المركزي اليمني في صنعاء، "
         "ولا يثبت هذا المورد أيَّ سلطة ستتخذ القرارات التي يسندها القانون إلى «البنك المركزي». ولا يثبت القانون أن النظام يعمل "
         "اليوم: فلا يورد أي مصدر هنا القوائم المالية للمؤسسة أو حجم صندوقها أو الاشتراكات المحصّلة أو أي تعويض مدفوع، ولا "
         "يثبت قرار 2025 أن الضمان يعمل فعليًا.")
DIL = "SRC-CBY-DIL-21-2008"
DIL_LOC = "cby-ye.com/files/62c2edbaad8eb.pdf (certified copy), "
DI_VS = [
    {"t": "2,000,000", "k": "v", "s": "READ", "src": DIL, "loc": DIL_LOC + "Art. 31(2), p.9: «يكون الضمان بكامل قيمة الوديعة "
     "إذا كانت بمقدار اثنين مليون ريال أو أقل … ويكون الضمان اثنين مليون ريال إذا زادت قيمة الوديعة على ذلك»" + R11},
    {"t": "0.2%", "k": "v", "s": "READ", "src": DIL, "loc": DIL_LOC + "Art. 13(1), p.5: «بنسبة (٠,٠٠٢) اثنين بالألف من مجموع "
     "الودائع الخاضعة»" + R11},
    {"t": "31", "k": "v", "s": "LOCATOR"}, {"t": "33", "k": "v", "s": "LOCATOR"}, {"t": "13", "k": "v", "s": "LOCATOR"},
]
DI_OLD = ("Deposit insurance matters for trust in deposits, but no source here reports cover, premiums or payouts.",
          "لضمان الودائع أهمية في الثقة بالودائع، لكن لا يُبلغ أي مصدر هنا عن التغطية أو الأقساط أو التعويضات.")

# ---------------------------------------------------------------------------------------------------------------- 6B-3(b)
# V3 read cby-ye.com/files/64e6f1e87e2a1.pdf: p.1 «589/CBY/2023» dated 20/8/2023; p.32 signed 20 August 2023; scope Art. 1;
# Art. 9 «آليات التظلم والتعامل مع الشكاوى» (pp.25-30): ج (p.27) reply «بقرار المعالجة» within 10 working days of receipt of
# the complaint and all documents, +10 working days; د (p.28) exceptional cases, notify the CBY and the consumer, settle within
# half the «original» period, «ينبغي» not over 30 working days from submission, waiting time not counted; ذ (p.28) «14 يومًا»
# (unqualified) from the end of the settlement time frame, a later request «عند بيان سبب وجيه». ج and د govern the same stage
# (د cross-refers to ج) but the text does not say how their extensions relate, so they are published item by item (the
# instruction's rule), and nothing is composed into one period. "Resolve" is not the duty in ج (a decision) and is in د
# (settle). The instruction's sentence "The Instructions are the binding text" is not used: its own third condition forbids
# adjudicating which instrument binds; the brochure is described as a summary and its different wording is shown.
CP_EN = ("The Financial Consumer Protection Regulatory Instructions of the Central Bank of Yemen – Aden (CBY-Aden) (ref. "
         "589/CBY/2023, dated 20 August 2023) apply to the financial service providers under CBY-Aden's supervision and to "
         "their agents. Article 9 of the Instructions sets out the complaint path item by item. Item ج requires the provider to "
         "reply to the consumer with its decision on the complaint within at most 10 working days of receiving the complaint "
         "and all necessary documents, extendable by a further 10 working days where the nature of the complaint requires it, "
         "with the complainant told why. Item د requires the provider, if in exceptional cases it cannot settle the complaint "
         "in that time, to notify the central bank and the consumer before the period ends and then to settle it within no "
         "more than half the original period; it adds that handling any complaint should not exceed 30 working days from "
         "submission in all cases, and that time spent waiting for documents the provider requests is not counted. Item ذ "
         "provides that the consumer may take the complaint to CBY-Aden's consumer-protection department, if no reply came in "
         "time or the consumer is not satisfied with the decision, within 14 days of the end of the time frame for settling "
         "the complaint, a date that depends on which period applied and on any time not counted; it also allows a later "
         "request on a stated good reason. The Instructions do not make clear how items ج and د relate. The 2024 awareness "
         "brochure, a summary, gives the escalation window as 14 working days, where the Instructions say 14 days. These are "
         "rules, not measured performance (pp. 25–28).")
CP_AR = ("تسري التعليمات التنظيمية لحماية المستهلك المالي الصادرة عن البنك المركزي اليمني – عدن (المرجع 589/CBY/2023، بتاريخ "
         "20 أغسطس 2023) على مقدمي الخدمات المالية الخاضعين لرقابة البنك المركزي اليمني – عدن وإشرافه وعلى وكلائهم. وتحدد "
         "المادة 9 من التعليمات مسار الشكوى بندًا بندًا. فيُلزم البند (ج) مقدّمَ الخدمة بالرد على المستهلك بقرار معالجة الشكوى "
         "خلال 10 أيام عمل كحد أقصى من تاريخ استلام الشكوى وكافة الوثائق اللازمة، ويجوز تمديدها 10 أيام عمل أخرى إذا كانت "
         "طبيعة الشكوى تستدعي ذلك، مع إعلام مقدم الشكوى بمبررات التمديد. ويُلزم البند (د) مقدّمَ الخدمة، إذا لم يستطع في "
         "الحالات الاستثنائية تسوية الشكوى في ذلك الوقت، بإخطار البنك المركزي والمستهلك قبل انقضاء المدة، ثم بتسويتها في مدة "
         "لا تتعدى نصف المدة الأصلية؛ ويضيف أنه ينبغي ألا تتجاوز مدة معالجة أي شكوى 30 يوم عمل من تاريخ تقديمها في جميع "
         "الأحوال، وأن فترة انتظار الوثائق التي يطلبها مقدم الخدمة لا تُحتسب. وينص البند (ذ) على أنه يجوز للمستهلك رفع الشكوى "
         "إلى الإدارة المختصة بحماية العملاء في البنك المركزي اليمني – عدن، إذا لم يتلقَّ ردًّا في الوقت المحدد أو لم يرضَ "
         "بالقرار، خلال 14 يومًا من نهاية الإطار الزمني المحدد لتسوية الشكوى، وهو تاريخ يتوقف على المدة التي طُبّقت وعلى أي وقت "
         "لا يُحتسب؛ كما يجيز تقديم الطلب بعد ذلك عند بيان سبب وجيه. ولا توضح التعليمات العلاقة بين البندين (ج) و(د). ويذكر "
         "الكتيّب التوعوي الصادر عام 2024، وهو ملخص، أن مهلة الرفع 14 يوم عمل، بينما تنص التعليمات على 14 يومًا. هذه قواعد، "
         "لا أداء مقيس (ص. 25–28).")
VIS_CP_EN = ("The path follows Article 9 of the Financial Consumer Protection Regulatory Instructions of the Central Bank of Yemen – "
             "Aden (CBY-Aden) (ref. 589/CBY/2023, dated 20 August 2023), which apply to the providers under CBY-Aden's "
             "supervision and their agents: the provider's reply within at most 10 working days (item ج); its extension (items "
             "ج and د, whose relationship the Instructions do not make clear); and the consumer's 14-day window for taking the "
             "complaint to CBY-Aden, counted from the end of a settlement period that can be extended and that leaves out time "
             "spent waiting for documents (item ذ). The 2024 awareness brochure gives that window as 14 working days. How "
             "complaints are actually handled is not measured: the evidence base holds no data on complaint volumes, "
             "resolution quality or enforcement.")
VIS_CP_AR = ("يتبع المسار المادة 9 من التعليمات التنظيمية لحماية المستهلك المالي الصادرة عن البنك المركزي اليمني – عدن (المرجع "
             "589/CBY/2023، بتاريخ 20 أغسطس 2023)، التي تسري على مقدمي الخدمات الخاضعين لرقابة البنك المركزي اليمني – عدن "
             "وعلى وكلائهم: رد مقدم الخدمة خلال 10 أيام عمل كحد أقصى (البند ج)؛ وتمديد هذه المدة (البندان (ج) و(د)، ولا توضح "
             "التعليمات العلاقة بينهما)؛ ومهلة 14 يومًا يرفع خلالها المستهلك الشكوى إلى البنك المركزي اليمني – عدن، تُحسب من "
             "نهاية مدة تسوية يمكن تمديدها ولا تُحتسب فيها فترة انتظار الوثائق (البند ذ). ويذكر الكتيّب التوعوي الصادر عام 2024 "
             "أن هذه المهلة 14 يوم عمل. ولا يُقاس الأداء الفعلي لمعالجة الشكاوى، إذ لا تتوفر بيانات عن أعداد الشكاوى أو جودة "
             "معالجتها أو فاعلية الإنفاذ.")
REF_S3 = (("A 2024 consumer-protection brochure from the Central Bank of Yemen – Aden (CBY-Aden) describes a provider complaint "
           "stage of up to 10 business days, possible extension under stated conditions, and escalation to the central bank "
           "within 14 business days. The legal text of the Financial Consumer Protection Regulatory Instructions, announced on "
           "28 August 2023, has not been extracted here.",
           "The Financial Consumer Protection Regulatory Instructions of the Central Bank of Yemen – Aden (CBY-Aden) (ref. "
           "589/CBY/2023, dated 20 August 2023; announced on 28 August 2023) set a complaint path for the providers under "
           "CBY-Aden's supervision and their agents, with time limits for the provider's reply, its extension and the "
           "consumer's escalation to CBY-Aden, each in its own item of Article 9, as the records below set out."),
          ("يصف كتيّب توعوي لحماية المستهلك أصدره البنك المركزي اليمني – عدن في 2024 مرحلةً لمعالجة الشكوى لدى مقدم الخدمة تصل "
           "إلى 10 أيام عمل، مع إمكان التمديد وفق شروط يذكرها، ثم التصعيد إلى البنك المركزي خلال 14 يوم عمل. ولم يُستخرج هنا النص "
           "القانوني للتعليمات التنظيمية لحماية المستهلك المالي المعلنة في 28 أغسطس 2023.",
           "تحدد التعليمات التنظيمية لحماية المستهلك المالي الصادرة عن البنك المركزي اليمني – عدن (المرجع 589/CBY/2023، بتاريخ "
           "20 أغسطس 2023؛ وأُعلن عنها في 28 أغسطس 2023) مسارًا للشكوى لدى مقدمي الخدمات الخاضعين لرقابة البنك المركزي اليمني "
           "– عدن ووكلائهم، بمدد لرد مقدم الخدمة وتمديدها ولرفع المستهلك الشكوى إلى البنك المركزي اليمني – عدن، لكلٍّ منها بند "
           "في المادة 9، كما تبينها السجلات أدناه."))
REF_S3_HEAD = (("Official guidance describes a complaint path; performance is unmeasured",
                "The Instructions set a complaint path; performance is unmeasured"),
               ("الإرشادات الرسمية تصف مسار الشكوى، أما الأداء فغير مقيس", "التعليمات تحدد مسار الشكوى، أما الأداء فغير مقيس"))
INSTR = "SRC-CBY-FCP-INSTR-2023-001"
INSTR_URL = "https://cby-ye.com/files/64e6f1e87e2a1.pdf"
CP_VS = [
    {"t": "20 August 2023", "k": "d", "s": "READ", "src": INSTR, "loc": INSTR_URL + " p.1 'Ref: 589/CBY/2023 Date: 20/8/2023'; "
     "p.32 signed «4 صفر 1445هـ الموافق 20 اغسطس 2023م»" + R11},
    {"t": "589", "k": "v", "s": "READ", "src": INSTR, "loc": INSTR_URL + " p.1, reference 589/CBY/2023" + R11},
    {"t": "30", "k": "v", "s": "READ", "src": INSTR, "loc": INSTR_URL + " Art. 9 item د, p.28: «(30) يوم عمل من تأريخ تقديم الشكوى»" + R11},
    {"t": "9", "k": "v", "s": "LOCATOR"}, {"t": "25", "k": "v", "s": "LOCATOR"}, {"t": "27", "k": "v", "s": "LOCATOR"},
]
CP_DEF = {
    "definition_en": ("The complaint and escalation steps, and their time limits, as set out in Article 9 of the Financial Consumer "
                      "Protection Regulatory Instructions of the Central Bank of Yemen – Aden (CBY-Aden) dated 20 August 2023, "
                      "with the summary of them in its awareness brochure of 23 March 2024."),
    "definition_ar": ("خطوات الشكوى والتصعيد ومددها الزمنية كما تحددها المادة 9 من التعليمات التنظيمية لحماية المستهلك المالي "
                      "الصادرة عن البنك المركزي اليمني – عدن بتاريخ 20 أغسطس 2023، مع ملخصها في الكتيّب التوعوي المؤرخ في 23 "
                      "مارس 2024."),
    "period_en": "Instructions dated 20 August 2023 (announced 28 August 2023); brochure dated 23 March 2024; no outcome data",
    "period_ar": "التعليمات مؤرخة في 20 أغسطس 2023 (وأُعلن عنها في 28 أغسطس 2023)؛ والكتيّب مؤرخ في 23 مارس 2024؛ ولا تتوفر بيانات عن النتائج",
    "universe_en": ("Financial service providers under the supervision of the Central Bank of Yemen – Aden (CBY-Aden), and their "
                    "agents, as the Instructions define their scope (Article 1)"),
    "universe_ar": ("مقدمو الخدمات المالية الخاضعون لرقابة البنك المركزي اليمني – عدن وإشرافه، ووكلاؤهم، كما تحدد التعليمات نطاقها "
                    "(المادة 1)."),
    "method_en": ("The steps and time limits are read from the Instructions in the original (Article 9, pp. 25–28), each "
                  "attributed to its own item; where the 2024 brochure words them differently, both are shown. No legal review "
                  "is claimed or performed, and no total period is composed from items that the Instructions do not relate."),
    "method_ar": ("قُرئت الخطوات والمدد من نص التعليمات الأصلي (المادة 9، ص. 25–28)، ونُسب كلٌّ منها إلى بنده؛ وحيث يصوغها كتيّب "
                  "2024 بصورة مختلفة يُعرض الاثنان. ولا يُدّعى هنا أي مراجعة قانونية ولا تُجرى، ولا تُركّب مدة إجمالية من بنود لا "
                  "توضح التعليمات العلاقة بينها."),
    "currentness_en": ("The rules are those of the Instructions dated 20 August 2023, read in the original on 11 October 2026; the "
                       "brochure is dated 23 March 2024. The record should not be read as describing the rules after any later "
                       "amendment of the Instructions."),
    "currentness_ar": ("القواعد هي قواعد التعليمات المؤرخة في 20 أغسطس 2023، وقد قُرئ نصها الأصلي في 11 أكتوبر 2026؛ والكتيّب مؤرخ "
                       "في 23 مارس 2024. ولا يُقرأ السجل على أنه يصف القواعد بعد أي تعديل لاحق للتعليمات."),
}
CLM011_LIM = (("The brochure describes the complaint path as its publisher presents it; it is not legal advice and not evidence of "
               "compliance or performance.",
               "The Instructions set rules, and the brochure summarises them; neither is evidence of compliance or performance, "
               "and this record is not legal advice. The published text does not make clear how items ج and د of Article 9 "
               "relate, so no total period is given here."),
              ("يصف الكتيّب مسار الشكوى كما تعرضه الجهة الناشرة، وليس رأيًا قانونيًا ولا دليلًا على الامتثال أو الأداء؛",
               "تحدد التعليمات قواعد ويلخصها الكتيّب، وليس أيٌّ منهما دليلًا على الامتثال أو الأداء، وليس هذا السجل مشورة قانونية. "
               "ولا يوضح النص المنشور العلاقة بين البندين (ج) و(د) من المادة 9، لذلك لا تُذكر هنا مدة إجمالية؛"))
VIS_LIM = (("The time limits come from a 2024 awareness brochure, not from an extracted legal text.",
            "The time limits are read from the 2023 Instructions, item by item; the Instructions do not make clear how items ج "
            "and د relate, so no total period is shown."),
           ("والمدد مأخوذة من كتيّب توعوي صادر في 2024، لا من نص قانوني مستخرج.",
            "والمدد مقروءة من تعليمات 2023 بندًا بندًا؛ ولا توضح التعليمات العلاقة بين البندين (ج) و(د)، لذلك لا تُعرض مدة إجمالية."))
VIS11 = {
    "what_it_shows_en": ("The provider's duties under Article 9 of the 2023 Instructions (the reply period of up to 10 working days "
                         "and its extension, and the exceptional-case notice) and the consumer's 14-day window for taking the "
                         "complaint to CBY-Aden, each attributed to its own item, ending with complaint-handling performance, "
                         "which is not measured."),
    "what_it_shows_ar": ("يعرض واجبات مقدم الخدمة بموجب المادة 9 من تعليمات 2023 (مدة الرد البالغة 10 أيام عمل كحد أقصى وتمديدها، "
                         "والإخطار في الحالات الاستثنائية) ومهلة 14 يومًا يرفع خلالها المستهلك الشكوى إلى البنك المركزي اليمني – "
                         "عدن، منسوبًا كلٌّ منها إلى بنده، ثم ينتهي بأداء معالجة الشكاوى، وهو غير مقيس."),
    "encoding_contract": ("Ordered path, each step attributed to its item of Article 9 of the 2023 Instructions: reply within 10 "
                          "working days and its extension (ج); exceptional-case notice, settlement within half the original period "
                          "and the 30-working-day outer statement (د); escalation within 14 days (ذ; the 2024 brochure says 14 "
                          "working days); terminal outcome node OPEN. Items ج and د are not composed into one period."),
    "unit_or_object": "working days and days, as the Instructions state them / regulatory state",
    "denominator_universe": ("Financial service providers under the supervision of the Central Bank of Yemen – Aden (CBY-Aden), and "
                             "their agents, as the 2023 Instructions define their scope"),
    "period": "Instructions dated 20 August 2023 (announced 28 August 2023); brochure dated 23 March 2024; no outcome data",
    "source_period": "Aug-2023 Instructions (Article 9) → Mar-2024 brochure → provider reply → escalation → performance gap",
}
FCP_ARCH = {
    "FCP-ARCH-005": ("Article 9, item ج (p.27) of the 2023 Instructions: the provider replies to the consumer with its decision on "
                     "the complaint within at most 10 working days of receiving the complaint and all necessary documents. (The "
                     "2024 brochure counts the period from submission with the necessary attachments.)",
                     "Complaint received with all necessary documents"),
    "FCP-ARCH-006": ("Article 9, item ج (p.27): the period may be extended by a further 10 working days where the nature of the "
                     "complaint requires it, with the complainant told the reasons. Item د (p.28): in exceptional cases the "
                     "provider notifies the central bank and the consumer before the period ends and settles within no more than "
                     "half the original period; handling should not exceed 30 working days from submission in all cases; time "
                     "waiting for documents the provider requests is not counted. The Instructions do not make clear how the two "
                     "items relate.", "Nature of the complaint requires it (ج); exceptional case (د)"),
    "FCP-ARCH-007": ("Article 9, item ذ (p.28): the consumer may take the complaint to the central bank's consumer-protection "
                     "department if no reply was received within the time the Instructions set, the complaint was not handled as "
                     "they provide, or the consumer is not satisfied with the provider's decision.", None),
    "FCP-ARCH-008": ("Article 9, item ذ (p.28): within 14 days (not qualified as working days in the Instructions) of the end of "
                     "the time frame for settling complaints; a later request may be made on stating a good reason. The 2024 "
                     "brochure states 14 business days.", None),
}
MA006 = (("Official material specifies complaint and escalation architecture, including source-defined time windows; actual "
          "complaint volumes, resolution times and outcomes are not documented in the available evidence.",
          "The 2023 Instructions of CBY-Aden set out the complaint path and its time limits. They require providers to report to "
          "CBY-Aden's consumer-protection department every three months on the complaints they have handled, by nature and type, "
          "with the measures taken (p.7), and provide for CBY-Aden to prepare and publish annual reports of aggregate complaint "
          "information (p.31). No such report was located on cby-ye.com (its news items, publications and rules pages, and its "
          "2024 and 2025 annual reports, checked on 11 October 2026). A duty to report or publish does not show that the data "
          "exist publicly or that providers comply; actual complaint volumes, resolution times and outcomes are not documented in "
          "the available evidence."),
         ("تحدد المواد الرسمية بنية الشكوى والتصعيد والمدد المرتبطة بها، بينما لا توثق الأدلة المتاحة أحجام الشكاوى الفعلية ولا "
          "أزمنة معالجتها ولا نتائجها.",
          "تحدد تعليمات 2023 الصادرة عن البنك المركزي اليمني – عدن مسار الشكوى ومدده. وتُلزم مقدمي الخدمات برفع تقارير كل ثلاثة "
          "أشهر إلى الإدارة المختصة بحماية العملاء في البنك المركزي اليمني – عدن عن الشكاوى التي تعاملوا معها، مصنفةً بحسب "
          "طبيعتها ونوعها، مع الإجراءات المتخذة (ص. 7)، وتنص على أن يعدّ البنك المركزي اليمني – عدن تقارير سنوية تتضمن معلومات "
          "مجمعة عن الشكاوى وينشرها (ص. 31). ولم يُعثر على أي تقرير من هذا النوع في موقع cby-ye.com (أخباره وصفحات المنشورات "
          "والأنظمة، وتقريراه السنويان لعامي 2024 و2025، جرى التحقق في 11 أكتوبر 2026). ولا يثبت واجب الإبلاغ أو النشر أن "
          "البيانات متاحة للعموم أو أن مقدمي الخدمات ملتزمون به؛ ولا توثق الأدلة المتاحة أحجام الشكاوى الفعلية ولا أزمنة "
          "معالجتها ولا نتائجها."))
OECD_FCP = (("The OECD's 2026 review of Yemen's financial sector provides context and recommendations.",
             "The OECD's 2026 review describes the Instructions as adopted in August 2023 and “in the process of being implemented” "
             "(printed p. 33), and states that consumers of money exchange companies currently have “no avenues for complaints or "
             "redress” (printed p. 36). The Instructions apply to the providers under CBY-Aden's supervision and their agents. The "
             "two statements are shown as found; this resource does not reconcile them."),
            ("ويقدّم استعراض منظمة التعاون الاقتصادي والتنمية (OECD) للقطاع المالي في اليمن الصادر في 2026 سياقًا وتوصيات.",
             "ويصف استعراض منظمة التعاون الاقتصادي والتنمية (OECD) لعام 2026 التعليمات بأنها اعتُمدت في أغسطس 2023 و«في طور "
             "التنفيذ» (الصفحة 33 المطبوعة)، ويذكر أن عملاء شركات الصرافة ليست لديهم حاليًا «أي سبل للشكوى أو الإنصاف» (الصفحة 36 المطبوعة). "
             "وتسري التعليمات على مقدمي الخدمات الخاضعين لرقابة البنك المركزي اليمني – عدن ووكلائهم. ويُعرض البيانان كما وردا، ولا "
             "يوفّق هذا المورد بينهما."))
OECD_FCP_ANN = (("announced Financial Consumer Protection Regulatory Instructions on 28 August 2023",
                 "issued Financial Consumer Protection Regulatory Instructions dated 20 August 2023 (ref. 589/CBY/2023), announced on "
                 "28 August 2023,"),
                ("أعلن البنك المركزي اليمني – عدن في 28 أغسطس 2023 إصدار التعليمات التنظيمية لحماية المستهلك المالي،",
                 "أصدر البنك المركزي اليمني – عدن التعليمات التنظيمية لحماية المستهلك المالي بتاريخ 20 أغسطس 2023 (المرجع "
                 "589/CBY/2023)، وأعلن عنها في 28 أغسطس 2023،"))
OECD_VS = [CP_VS[0], CP_VS[1], {"t": "33", "k": "v", "s": "LOCATOR"}, {"t": "36", "k": "v", "s": "LOCATOR"},
           {"t": "August 2023", "k": "d", "s": "READ", "src": "SRC-OECD-YEM-RESILIENCE-001", "loc": "OECD (2026) Promoting "
            "Economic Resilience in Yemen, printed p.33 (PDF p.35): 'adopted by the CBY-Aden in August 2023 and at the time of "
            "writing are in the process of being implemented'" + R11}]
INSTR_SRC = {
    "primary_url": ("https://cby-ye.com/news/567", INSTR_URL),
    "additional_urls": ('["https://www.cby-ye.com/files/64e6f1e87e2a1.pdf"]', '["https://cby-ye.com/news/567"]'),
    "display_title": ("Regulatory Instructions for Financial Consumer Protection (issuance announced 28 August 2023)",
                      "Regulatory Instructions for Financial Consumer Protection (ref. 589/CBY/2023, 20 August 2023; announced "
                      "28 August 2023)"),
    "display_title_ar": ("التعليمات التنظيمية لحماية المستهلك المالي (أُعلن إصدارها في 28 أغسطس 2023)",
                         "التعليمات التنظيمية لحماية المستهلك المالي (المرجع 589/CBY/2023، 20 أغسطس 2023؛ وأُعلن عنها في 28 أغسطس 2023)"),
    "document_date": ("2023-08-28", "2023-08-20"),
    "retrieval_date": ("2026-10-04", "2026-10-11"),
    "non_public_locator_note": (None, "CLOSE-6D (11 October 2026): the instrument, " + INSTR_URL + ", is the primary locator (p.1 "
                                "'Ref: 589/CBY/2023 Date: 20/8/2023'; p.32 signed 20 August 2023; Board approval under Law No. 14 of "
                                "2000); https://cby-ye.com/news/567 is the announcement of 28 August 2023 (the earlier "
                                "www.cby-ye.com address of the PDF is the same file). Lineage: TC-H changed the Arabic date to 28 "
                                "August because the instrument had not been read. news/567 also states a one-year maximum "
                                "adjustment period that the Instructions themselves do not state."),
}
REF_FCP = {"date": ("2023-08-28", "2023-08-20"),
           "text_add": (" Issued 20 August 2023 (ref. 589/CBY/2023; instrument p.1 and p.32); announced 28 August 2023 (news/567); "
                        "the adjustment period is stated in the announcement, not in the Instructions."),
           "url": ("https://cby-ye.com/news/567", INSTR_URL)}

# ======================================================================================================================
# Domain-lens revisions (audit/close_out/v5_reads/REDTEAM_6D.md): verdict KEEP, conditional on B1-B3. Applied to the entries
# above by key, so that the first draft and what the review changed stay legible.
# B1 the thesis keeps its counterweight; B2 the bound is a survey estimate, for surveyed areas; B3 the bound moves to the
# descriptive section 2, section 4 refers to it with a disclaimer about what it bears on (receipt into one's own
# financial-institution account), and the thesis no longer carries it; S1 "usable here", the printed zero named; S2 both
# halves, in order, in sections 8 and 9; S3 the item asks about a bank or mobile-money account; S4 the first heading;
# S5 the routes overlap; S6 Yemen's classification, not its membership; S7 the gender figures are not compared; S8 the
# Instructions' own scope words; S9 how items ج and د relate; S10 the deposit-guarantee exclusions, the search scope and
# the decision named; S11 1.838 described, not denied; S12 the IMF basis; S13 the Postal Savings Fund; B4 12 partners
# reported, not "through"; nits N1, N3, N4, N6, N8.
# ======================================================================================================================
def _sec(route, order, lang, field, old_start, new, which="new"):
    hits = [i for i, e in enumerate(SEC) if e[1:5] == (route, order, lang, field) and e[5].startswith(old_start)]
    if len(hits) != 1:
        raise ValueError(f"review override: {route} s{order} {lang} {old_start[:40]!r}: {len(hits)} entries")
    e = SEC[hits[0]]
    SEC[hits[0]] = e[:6] + (new,) if which == "new" else e[:5] + (new, e[6])


def _cell(sheet, key, field, old_start, new):
    hits = [i for i, e in enumerate(CELL) if e[1:4] == (sheet, key, field) and e[4].startswith(old_start)]
    if len(hits) != 1:
        raise ValueError(f"review override: {sheet} {key}.{field} {old_start[:40]!r}: {len(hits)} entries")
    CELL[hits[0]] = CELL[hits[0]][:5] + (new,)


CWR_SET["thesis_en"] = (
    "In Yemen’s Global Findex 2021 wave, 31.9% of adults in surveyed areas received domestic remittances and 11.9% of adults "
    "in those areas had an account at a financial institution. For that wave, no weighted estimate of the channel usable here "
    "is published or held (the database’s printed zero for receipt into an account conflicts with the World Bank’s own "
    "documentation and is not used); the World Bank’s published variable documentation records that recipients were asked "
    "whether they received the money using a bank or mobile-money account, and that some answered yes. That money sent "
    "between people reaches recipients more through exchange companies and other money-transfer providers than into accounts "
    "of their own remains a hypothesis: the survey counts adults, not households, and its values here cover transfers within "
    "Yemen only. Other routes, such as cash carried by hand, and humanitarian cash fit the same numbers, and survey coverage, "
    "currency and the meaning of “remittance” limit what they show.")
CWR_SET["thesis_ar"] = (
    "في موجة 2021 من المؤشر العالمي للشمول المالي (Global Findex) الخاصة باليمن، تلقى 31.9% من البالغين في المناطق التي شملها "
    "المسح حوالات محلية، وكان لدى 11.9% من البالغين في تلك المناطق حساب لدى مؤسسة مالية. ولتلك الموجة لا يُنشر أي تقدير موزون "
    "للقناة صالح للاستخدام هنا ولا يُحتفظ به (فالصفر الذي تطبعه قاعدة البيانات لاستلام الأموال في حساب يتعارض مع توثيق البنك "
    "الدولي نفسه، ولا يُستخدم)؛ ويسجل توثيق المتغيرات الذي ينشره البنك الدولي أن المتلقين سُئلوا عمّا إذا كانوا قد تلقوا المال "
    "باستخدام حساب مصرفي أو حساب أموال عبر الهاتف المحمول، وأن بعضهم أجاب بنعم. ويبقى القول بأن الأموال المرسلة بين الأفراد تصل "
    "إلى متلقيها عبر شركات الصرافة وغيرها من مقدمي خدمات تحويل الأموال أكثر مما تصل إلى حسابات خاصة بهم فرضيةً: فالمسح يعدّ "
    "البالغين لا الأسر، ولا تغطي قيمه الواردة هنا إلا الحوالات داخل اليمن. وتنسجم الطرق الأخرى، كالنقد الذي يُحمل باليد، "
    "والمساعدات النقدية الإنسانية مع الأرقام نفسها، وتحدّ تغطيةُ المسح والعملةُ ومعنى «الحوالة» مما تُظهره.")
CWR_SET["prohibited_inference_en"] = (
    "A share of adults who received domestic remittances is not a share of households that depend on them; the bound that "
    "CauseWay calculates from the two published shares (at least 62.7% of recipients in surveyed areas without an account at a "
    "financial institution, itself a survey estimate) describes the group, not any individual recipient, does not establish "
    "the channel, and does not rule out an account type for which no Yemen value is published; a roster entry or a branch "
    "count is not a measure of remittance flows; and a price of sending money from abroad is not the cost a household pays to "
    "collect it.")
CWR_SET["prohibited_inference_ar"] = (
    "لا تمثل نسبة البالغين الذين تلقوا حوالات محلية نسبة الأسر التي تعتمد عليها؛ والحدّ الذي تحسبه CauseWay من النسبتين "
    "المنشورتين (62.7% على الأقل من المتلقين في المناطق التي شملها المسح بلا حساب لدى مؤسسة مالية، وهو تقدير مسحي أيضًا) يصف "
    "المجموعة لا أي متلقٍّ بعينه، ولا يثبت القناة، ولا يستبعد نوعًا من الحسابات لا تُنشر له قيمة لليمن؛ وليس القيد في قائمة أو "
    "عدد الفروع مقياسًا لتدفقات الحوالات؛ وليس سعر إرسال المال من الخارج التكلفة التي تتحملها الأسرة لاستلامه.")
S1_HEAD = (("What the evidence supports", "What the evidence establishes, and what remains a hypothesis"),
           ("ما الذي تسنده الأدلة", "ما الذي تثبته الأدلة، وما الذي يبقى فرضية؟"))
META_EN = ("A hypothesis on domestic remittances and accounts in Yemen. For 2021 no usable weighted channel estimate is "
           "published or held; World Bank documentation records the item as asked and answered.")
META_AR = ("فرضية عن الحوالات المحلية والحسابات في اليمن. لموجة 2021 لا يُنشر ولا يُحتفظ هنا بأي تقدير موزون صالح للقناة؛ "
           "ويسجل توثيق البنك الدولي أن السؤال طُرح وأُجيب عنه.")

S2_BOUND_EN = (
    "so the figures give no exact count of the recipients who had an account. The two shares do bound it: by CauseWay’s "
    "calculation from them, at most 11.9% of adults can be both, so at least 62.7% of the adults in surveyed areas who received "
    "domestic remittances did not have an account at a financial institution. Both shares are survey estimates, so the bound "
    "is an estimate too, not an exact floor; it is a bound on the group, not a statement about any individual. It does not "
    "establish the channel: it bears only on whether recipients could have received the money into a financial-institution "
    "account of their own, does not show how they did receive it or how many used an exchange company, and does not rule out "
    "a mobile wallet or another account type for which the World Bank publishes no Yemen value.")
S2_BOUND_AR = (
    "فلا تعطي الأرقام عددًا دقيقًا للمتلقين الذين كان لديهم حساب. لكن النسبتين تحدّانه: فبحساب أجرته CauseWay منهما، لا يمكن "
    "أن يجمع بين الأمرين أكثر من 11.9% من البالغين، أي أن 62.7% على الأقل من البالغين في المناطق التي شملها المسح ممن تلقوا "
    "حوالات محلية لم يكن لديهم حساب لدى مؤسسة مالية. والنسبتان تقديران مسحيان، فالحدّ تقدير أيضًا لا حدّ أدنى دقيق؛ وهو حدّ "
    "يتعلق بالمجموعة لا بأي فرد بعينه. ولا يثبت القناة: فلا يتصل إلا بمسألة ما إذا كان بوسع المتلقين استلام المال في حساب خاص "
    "بهم لدى مؤسسة مالية، ولا يبيّن كيف استلموه فعلًا ولا عدد من استخدم منهم شركة صرافة، ولا يستبعد محفظة إلكترونية أو نوعًا آخر "
    "من الحسابات لا ينشر البنك الدولي له قيمة لليمن.")
_sec(R, 2, "en", "body", "so the figures do not show how many", S2_BOUND_EN)
_sec(R, 2, "ar", "body", "فلا تُظهر الأرقام كم ممن", S2_BOUND_AR)
_sec(R, 3, "en", "body", "For the 2021 wave, this evidence base holds no channel value",
     "For the 2021 wave, no weighted estimate of the channel for domestic remittances usable here is published or held. The "
     "World Bank’s published variable documentation for that wave records that recipients were asked whether they received the "
     "money using a bank or mobile-money account and that some answered yes; these are unweighted counts of answers, not an "
     "estimate for the population, and they are not used here. The World Bank’s database prints zero for receipt into an "
     "account, with no recipient or group value; the two statements cannot both describe the same quantity, so the printed "
     "value is not used either. The World Bank publishes no mobile-money-account figure for Yemen, and its figure for an "
     "account at a financial institution is the same as its account figure.")
_sec(R, 3, "ar", "body", "أما موجة 2021، فلا تتضمن قاعدة الأدلة هذه",
     "أما موجة 2021، فلا يُنشر لها أي تقدير موزون لقناة الحوالات المحلية صالح للاستخدام هنا ولا يُحتفظ به. ويسجل توثيق المتغيرات "
     "الذي ينشره البنك الدولي لتلك الموجة أن المتلقين سُئلوا عمّا إذا كانوا قد تلقوا المال باستخدام حساب مصرفي أو حساب أموال عبر "
     "الهاتف المحمول، وأن بعضهم أجاب بنعم؛ وهذه أعداد غير موزونة من الإجابات، لا تقدير للسكان، ولا تُستخدم هنا. وتطبع قاعدة بيانات "
     "البنك الدولي صفرًا لاستلام الأموال في حساب، من دون قيمة للمتلقين أو للفئات؛ ولا يمكن أن يصف البيانان الكمية نفسها، فلا تُستخدم "
     "القيمة المطبوعة أيضًا. ولا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة "
     "مالية مساوٍ لرقم ملكية الحساب.")
S4_EN = ("This Reading’s hypothesis is that money sent between people within Yemen reaches recipients more through exchange "
         "companies and other money-transfer providers than into accounts of their own. “Into accounts” means receipt into the "
         "recipient’s own account: a transfer can move through the banking system and still be paid out in cash to a recipient "
         "without one, so the hypothesis says nothing about the part banks play in moving money. The two routes are not mutually "
         "exclusive, and the evidence here does not separate them. The evidence bears on whether recipients held accounts and "
         "says nothing about magnitudes: no source here measures what share of households’ cash comes from transfers, how much "
         "money moves through each channel, or how often transfers arrive. The bound set out above, by CauseWay’s calculation at "
         "least 62.7% of recipients in surveyed areas without an account at a financial institution, bears only on whether "
         "recipients could have received the money into such an account of their own; it does not establish the channel, and it "
         "neither confirms nor refutes the hypothesis. Separately, the 2014 profile reports that 31.1% of recipients named a money "
         "transfer operator and 2.0% a financial institution; it does not show how the others received money, a money transfer "
         "operator in the survey is not necessarily an exchange company, and these values do not describe the 2021 wave. This "
         "Reading states a hypothesis, not a finding.")
S4_AR = ("تفترض هذه القراءة أن الأموال المرسلة بين الأفراد داخل اليمن تصل إلى متلقيها عبر شركات الصرافة وغيرها من مقدمي خدمات "
         "تحويل الأموال أكثر مما تصل إلى حسابات خاصة بهم. والمقصود بالوصول «إلى الحسابات» استلامُ المال في حساب المتلقي نفسه: "
         "فقد تنتقل الحوالة عبر النظام المصرفي ثم تُسلَّم نقدًا لمتلقٍّ لا يملك حسابًا، لذلك لا تقول الفرضية شيئًا عن الدور الذي "
         "تؤديه البنوك في نقل الأموال. والطريقان غير متنافيين، ولا تفصل الأدلة الواردة هنا بينهما. وتتصل الأدلة بمسألة امتلاك "
         "المتلقين حسابات، ولا تقول شيئًا عن الأحجام: فلا يقيس أي مصدر هنا حصة الحوالات من النقد الذي تتلقاه الأسر، ولا مقدار ما "
         "ينتقل عبر كل قناة، ولا عدد مرات وصول الحوالات. والحدّ المبيَّن أعلاه، أي أن 62.7% على الأقل من المتلقين في المناطق التي "
         "شملها المسح لم يكن لديهم حساب لدى مؤسسة مالية بحساب أجرته CauseWay، لا يتصل إلا بمسألة ما إذا كان بوسع المتلقين استلام "
         "المال في حساب من هذا النوع خاص بهم؛ فهو لا يثبت القناة، ولا يؤكد الفرضية ولا ينقضها. وبصورة منفصلة، يفيد ملف 2014 بأن "
         "31.1% من المتلقين ذكروا مشغل تحويل أموال، و2.0% مؤسسة مالية؛ ولا يبيّن كيف تلقى الباقون أموالهم، ومشغل تحويل الأموال في "
         "المسح ليس بالضرورة شركة صرافة، ولا تصف هذه القيم موجة 2021. وتطرح هذه القراءة فرضيةً لا نتيجة.")
SECW = [("6B-5", R, 4, "en", "body", "The evidence is consistent with a hypothesis", S4_EN),
        ("6B-5", R, 4, "ar", "body", "تتسق الأدلة مع فرضية", S4_AR)]
SEC += [
    ("6B-5", R, 5, "en", "body", "Money may reach households there differently", "Money may reach recipients there differently"),
    ("6B-5", R, 5, "ar", "body", "وقد يصل المال إلى الأسر فيها بطرق مختلفة", "وقد يصل المال إلى المتلقين فيها بطرق مختلفة"),
]
_sec(R, 7, "en", "body", "It does not show what share of household cash comes from remittances, how",
     "It does not show what share of household cash comes from remittances or how recipients collected the money in the 2021 "
     "wave. The two survey shares bound the share of recipients in surveyed areas who lacked an account at a financial "
     "institution (at least 62.7%, by CauseWay’s calculation, itself an estimate), but that bound describes the group, not any "
     "individual, and does not establish the channel.")
_sec(R, 7, "ar", "body", "فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021، ولا",
     "فلا يُظهر حصة الحوالات من النقد الذي تتلقاه الأسر، ولا كيف استلم المتلقون أموالهم في موجة 2021. وتحدّ نسبتا المسح نسبةَ "
     "المتلقين في المناطق التي شملها المسح الذين لم يكن لديهم حساب لدى مؤسسة مالية (62.7% على الأقل، بحساب أجرته CauseWay، وهو "
     "تقدير أيضًا)، لكن هذا الحدّ يصف المجموعة لا أي فرد بعينه، ولا يثبت القناة.")
_sec(R, 8, "en", "body", "and the only channel values are for 2014;",
     "and the only weighted channel values are for 2014: for the 2021 wave none usable here is published or held, though World "
     "Bank documentation records the item as asked and answered;")
_sec(R, 8, "ar", "body", "وقيم القنوات الوحيدة تخص عام 2014؛",
     "وقيم القنوات الموزونة الوحيدة تخص عام 2014: فلا يُنشر لموجة 2021 أي تقدير موزون صالح للاستخدام هنا ولا يُحتفظ به، وإن كان "
     "توثيق البنك الدولي يسجل أن السؤال طُرح وأُجيب عنه؛")
_sec(R, 9, "en", "body", "- channel values for domestic remittances from a current survey wave;",
     "- weighted channel estimates for domestic remittances: for the 2021 wave none usable here is published or held, though "
     "the World Bank documents that the question was asked and answered; and the World Bank has published no later Yemen wave;")
_sec(R, 9, "ar", "body", "- قيم لقنوات الحوالات المحلية من موجة مسح حديثة؛",
     "- تقديرات موزونة لقنوات الحوالات المحلية: فلا يُنشر لموجة 2021 أي تقدير موزون صالح للاستخدام هنا ولا يُحتفظ به، وإن كان "
     "البنك الدولي يوثّق أن السؤال طُرح وأُجيب عنه؛ ولم ينشر البنك الدولي موجة أحدث لليمن؛")

# B2 on the record that holds the bound
BOUND_EN2 = (" By CauseWay’s calculation from the receiving share and the published share of adults with an account at a "
             "financial institution (11.9%), at least 62.7% of the adults in surveyed areas who received domestic remittances "
             "did not have such an account. Both shares are survey estimates, so the bound is an estimate too; it is a bound on "
             "the group, not on any individual. It does not establish the channel and does not rule out an account type for "
             "which the World Bank publishes no Yemen value.")
BOUND_AR2 = (" وبحساب أجرته CauseWay من نسبة المتلقين ومن النسبة المنشورة للبالغين الذين لديهم حساب لدى مؤسسة مالية (11.9%)، لم "
             "يكن لدى 62.7% على الأقل من البالغين في المناطق التي شملها المسح ممن تلقوا حوالات محلية حساب من هذا النوع. والنسبتان "
             "تقديران مسحيان، فالحدّ تقدير أيضًا؛ وهو حدّ يتعلق بالمجموعة لا بأي فرد بعينه. ولا يثبت القناة، ولا يستبعد نوعًا من "
             "الحسابات لا ينشر البنك الدولي له قيمة لليمن.")
for _sh, _f in ((O6, "summary_en"), ("11_VISUAL_LIBRARY", "accessible_summary_en")):
    _cell(_sh, "VIS-FINDEX-FLOW-CHANNELS", _f, FLOW_SUM_END_EN, FLOW_SUM_END_EN + BOUND_EN2)
for _sh, _f in ((O6, "summary_ar"), ("11_VISUAL_LIBRARY", "accessible_summary_ar")):
    _cell(_sh, "VIS-FINDEX-FLOW-CHANNELS", _f, FLOW_SUM_END_AR, FLOW_SUM_END_AR + BOUND_AR2)

# S6: Yemen's classification, not its membership of the aggregate (the publisher does not say)
LIC_EN = LIC_EN.replace("The aggregate averages economies in very different conditions, includes Yemen itself, and groups "
                        "economies by the World Bank income classification.",
                        "The aggregate averages economies in very different conditions and groups them by the World Bank income "
                        "classification, under which Yemen is itself classed as low income.")
LIC_AR = LIC_AR.replace("ويتوسط التجميع اقتصادات شديدة التباين في أحوالها، ويشمل اليمن نفسه، ويصنف الاقتصادات وفق تصنيف الدخل "
                        "المعتمد في البنك الدولي.",
                        "ويتوسط التجميع اقتصادات شديدة التباين في أحوالها، ويصنفها وفق تصنيف الدخل المعتمد في البنك الدولي، الذي "
                        "يضع اليمن نفسه ضمن فئة الدخل المنخفض.")
assert "under which Yemen is itself classed" in LIC_EN and "يضع اليمن نفسه" in LIC_AR
_sec("/people/", 2, "en", "body", "For context only, the World Bank's figure", LIC_EN)
_sec("/people/", 2, "ar", "body", "وللسياق فقط، يبلغ رقم البنك الدولي", LIC_AR)
_cell(O6, "CLM-001", "limitations_en", "The low-income figure is context",
      "The low-income figures are context, not a benchmark, a target or a ranking: they average economies in very different "
      "conditions and group them by the World Bank's income classification for fiscal year 2024, under which Yemen is itself "
      "classed as low income, while Yemen's own figure covers only the areas its survey reached. Only the financial-institution "
      "figure, 24.5%, compares with Yemen's 11.9% on the same definition.")
_cell(O6, "CLM-001", "limitations_ar", "ورقم الاقتصادات منخفضة الدخل للسياق فقط",
      "ورقما الاقتصادات منخفضة الدخل للسياق فقط، وليسا معيارًا ولا هدفًا ولا ترتيبًا: فهما يتوسطان اقتصادات ذات ظروف متباينة جدًا، "
      "ويصنفانها وفق تصنيف الدخل المعتمد في البنك الدولي للسنة المالية 2024، الذي يضع اليمن نفسه ضمن فئة الدخل المنخفض، في حين "
      "يقتصر رقم اليمن على المناطق التي بلغها المسح. ولا يُقارَن بنسبة اليمن البالغة 11.9% على التعريف نفسه إلا رقم الحساب لدى "
      "مؤسسة مالية، 24.5%.")

# B4, S7, N8: YLG
YLG_EN = YLG_EN.replace("covering loans of YER 9.4 billion, through 12 partner institutions; women-led businesses received 693 "
                        "of them (about 20%).",
                        "covering loans of YER 9.4 billion, and that it has 12 partner institutions; women-led businesses "
                        "received 693 of the letters (about 20%).")
YLG_EN = YLG_EN.replace("The two sets of figures differ in total and in gender split, and the published documents do not "
                        "explain why, so they are shown side by side and not combined.",
                        "The totals differ, and the published documents do not explain why; the gender figures cover different "
                        "periods and use different terms (women-led, men-owned), so they are not compared. The two sets of "
                        "figures are shown side by side and not combined.")
YLG_AR = YLG_AR.replace("تغطي قروضًا بقيمة 9.4 مليار ريال، عبر 12 مؤسسة شريكة، وأن المنشآت التي تقودها نساء حصلت على 693 منها "
                        "(نحو 20%).",
                        "تغطي قروضًا بقيمة 9.4 مليار ريال، وأن عدد مؤسساته الشريكة 12 مؤسسة؛ وأن المنشآت التي تقودها نساء حصلت "
                        "على 693 من هذه الخطابات (نحو 20%).")
YLG_AR = YLG_AR.replace("ويختلف الرقمان في المجموع وفي التوزيع بحسب الجنس، ولا تشرح الوثائق المنشورة سبب ذلك، لذا يُعرضان جنبًا "
                        "إلى جنب ولا يُدمجان في سلسلة واحدة.",
                        "ويختلف المجموعان، ولا تشرح الوثائق المنشورة سبب ذلك؛ أما أرقام الجنس فتغطي فترتين مختلفتين وتستخدم "
                        "مصطلحين مختلفين (تقودها نساء، يملكها رجال)، فلا تُقارن. ويُعرض الرقمان جنبًا إلى جنب ولا يُدمجان في "
                        "سلسلة واحدة.")
assert "it has 12 partner institutions" in YLG_EN and "not compared" in YLG_EN
assert "عدد مؤسساته الشريكة 12" in YLG_AR and "فلا تُقارن" in YLG_AR and "ولا يُدمجان في سلسلة واحدة" in YLG_AR
FIRMS_NEW_EN = ("Guarantee data measure something else. " + YLG_EN + " Both publishers count guarantees or transactions, not firms: "
                "the figures show what the programme backed, not how many firms could borrow, on what terms, or what share of "
                "MSME lending they represent.")
FIRMS_NEW_AR = ("وتقيس بيانات الضمانات شيئًا آخر. " + YLG_AR + " ويعدّ المصدران خطابات الضمان أو المعاملات لا المنشآت: "
                "فتبين الأرقام ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت "
                "الأصغر والصغيرة والمتوسطة.")
_sec("/firms/", 7, "en", "body", "Guarantee data tell a different story:", FIRMS_NEW_EN)
_sec("/firms/", 7, "ar", "body", "وتقدم بيانات الضمانات صورة من نوع آخر:", FIRMS_NEW_AR)
_cell(O6, "CLM-059", "summary_en", "Separately, the Organisation", YLG_EN)
_cell(O6, "CLM-059", "summary_ar", "وبصورة منفصلة، تفيد منظمة", YLG_AR)

# S13, N3, N6
_sec("/methodology/", 4, "en", "body", "Yemen Post is not covered by any evidence record",
     "Yemen Post is not covered here. The World Bank (2024, p. 16) describes the Yemen Post and Postal Savings Authority and the "
     "Postal Savings Fund as providing payment services, savings accounts and other financial products, and gives no count of "
     "their offices, accounts or balances; their network and services would be measured through the postal operator's own "
     "records of offices, services and transactions.")
_sec("/methodology/", 4, "ar", "body", "أما البريد اليمني فلا يغطيه أي سجل دليل",
     "أما البريد اليمني فلا يغطيه هذا المورد. ويصف البنك الدولي (2024، ص. 16) الهيئة العامة للبريد والتوفير البريدي وصندوق التوفير "
     "البريدي بأنهما يقدمان خدمات دفع وحسابات ادخار ومنتجات مالية أخرى، ولا يورد عددًا لمكاتبهما أو حساباتهما أو أرصدتهما؛ ويمكن "
     "قياس شبكتهما وخدماتهما من سجلات مشغل البريد نفسه عن المكاتب والخدمات والمعاملات.")
SEC += [
    ("6B-3c", "/methodology/", 4, "en", "body", "(round; fieldwork 2022–23)", "(the latest round; fieldwork 2022–23)"),
    ("6B-1d", "/finance/", 13, "en", "body",
     "Any such measures would in any case use questions and constructs different from the Global Findex account-ownership "
     "measure and would remain separate evidence rather than a harmonised series.",
     "Such figures would remain separate evidence rather than a harmonised series."),
    ("6B-1d", "/finance/", 13, "ar", "body",
     "وأي مقاييس من هذا النوع تقوم في كل الأحوال على أسئلة ومفاهيم تختلف عن مقياس امتلاك الحساب في Global Findex، فتبقى أدلة "
     "منفصلة لا سلسلة موحدة.", "وتبقى أرقام من هذا النوع أدلة منفصلة لا سلسلة موحدة."),
]

# S11, S12
_cell(O6, "CLM-041", "limitations_en", "The constant ratio of 1.838",
      "The ratio of 1.838 is this resource's ratio of the CBY-Aden remittance series to the IMF's over 2021–2024, and it is "
      "specific to remittances. The 33% population ratio is the IMF's stated rule, as proposed by the authorities, for splitting "
      "its external-sector estimates between areas under the internationally recognized government and other areas; for trade, "
      "the IMF relied mainly on UN Comtrade data and used trade data reported by the government for that split, and it allocates "
      "the official grants from Saudi Arabia and the United Arab Emirates wholly to the government. Neither is a published "
      "conversion factor: 1.838 describes how the two remittance series relate in 2021–2024, not a rule for other years or "
      "components, and the 33% ratio is applied inside the IMF's own estimates.")
_cell(O6, "CLM-041", "limitations_ar", "لا تنطبق النسبة الثابتة البالغة 1.838",
      "النسبة 1.838 هي نسبة سلسلة الحوالات لدى البنك المركزي اليمني – عدن إلى سلسلة صندوق النقد الدولي خلال 2021–2024 كما "
      "احتسبها هذا المورد، وهي خاصة بالحوالات. أما نسبة السكان البالغة 33% فهي القاعدة التي يذكرها الصندوق، كما اقترحتها "
      "السلطات، لتقسيم تقديراته للقطاع الخارجي بين المناطق الخاضعة للحكومة المعترف بها دوليًا والمناطق الأخرى؛ وفي التجارة "
      "اعتمد الصندوق أساسًا على بيانات قاعدة UN Comtrade واستخدم بيانات التجارة التي أبلغت عنها الحكومة لذلك التقسيم، وينسب "
      "المنح الرسمية من السعودية والإمارات بكاملها إلى الحكومة. وليست أيٌّ منهما معامل تحويل منشورًا: فالنسبة 1.838 تصف العلاقة "
      "بين سلسلتي الحوالات خلال 2021–2024، لا قاعدة لسنوات أو مكونات أخرى، ونسبة 33% تُطبَّق داخل تقديرات الصندوق نفسه.")
CELL += [
    ("6B-4b", O6, "CLM-007", "summary_en",
     "The IMF series covers areas under the internationally recognized government, so its level",
     "The IMF's method places the series on the basis of areas under the internationally recognized government, so its level"),
    ("6B-4b", O6, "CLM-007", "summary_ar", "وتغطي سلسلة الصندوق المناطق الخاضعة للحكومة المعترف بها دوليًا، لذلك",
     "ويضع منهج الصندوق السلسلة على أساس المناطق الخاضعة للحكومة المعترف بها دوليًا، لذلك"),
]

# S10: deposit guarantee
DI_EN = DI_EN.replace("deposits in a foreign currency are guaranteed only if the Central Bank decides to subject them to the law.",
                      "deposits in a foreign currency are guaranteed only if the Central Bank decides to subject them to the law. "
                      "Government deposits, deposits between banks, and cash collateral up to the facilities it secures are not "
                      "deposits subject to the law (Art. 13).")
DI_EN = DI_EN.replace("and this resource has found no published revision.", "and this resource found no published revision on "
                      "cby-ye.com.")
DI_EN = DI_EN.replace("and the 2025 decision does not establish that cover operates.",
                      "and Governor's Decision No. 6 of 2025, which provides for moving the Institution's head office to Aden, does "
                      "not establish that cover operates.")
DI_AR = DI_AR.replace("ولا تُضمن الودائع بالعملة الأجنبية إلا إذا قرر البنك المركزي إخضاعها للقانون.",
                      "ولا تُضمن الودائع بالعملة الأجنبية إلا إذا قرر البنك المركزي إخضاعها للقانون. ولا تُعدّ ودائع الحكومة "
                      "والودائع بين البنوك والتأمينات النقدية، بحدود التسهيلات التي تضمنها، من الودائع الخاضعة للقانون (المادة 13).")
DI_AR = DI_AR.replace("ولم يجد هذا المورد أي تعديل منشور له.", "ولم يجد هذا المورد أي تعديل منشور له في موقع cby-ye.com.")
DI_AR = DI_AR.replace("ولا يثبت قرار 2025 أن الضمان يعمل فعليًا.",
                      "ولا يثبت قرار المحافظ رقم (6) لسنة 2025، الذي ينص على نقل المركز الرئيسي للمؤسسة إلى عدن، أن الضمان يعمل "
                      "فعليًا.")
assert DI_EN.count("(Art. 13)") == 2 and "on cby-ye.com" in DI_EN and "Decision No. 6 of 2025" in DI_EN
assert DI_AR.count("(المادة 13)") == 2 and "موقع cby-ye.com" in DI_AR and "رقم (6) لسنة 2025" in DI_AR

# S8, S9, N4: the Instructions' own scope words; how items ج and د relate
_SCOPE_EN = ("The Financial Consumer Protection Regulatory Instructions of the Central Bank of Yemen – Aden (CBY-Aden) (ref. "
             "589/CBY/2023, dated 20 August 2023) apply to the financial service providers under CBY-Aden's supervision and to "
             "their agents.")
_SCOPE_EN2 = ("The Financial Consumer Protection Regulatory Instructions issued by the Central Bank of Yemen – Aden (CBY-Aden) "
              "(ref. 589/CBY/2023, dated 20 August 2023) apply, in their own words, to providers of financial products and "
              "services in the Republic of Yemen under the supervision of “the Central Bank”, and to their agents: as CBY-Aden's "
              "instrument, they reach the providers CBY-Aden supervises.")
_SCOPE_AR = ("تسري التعليمات التنظيمية لحماية المستهلك المالي الصادرة عن البنك المركزي اليمني – عدن (المرجع 589/CBY/2023، بتاريخ "
             "20 أغسطس 2023) على مقدمي الخدمات المالية الخاضعين لرقابة البنك المركزي اليمني – عدن وإشرافه وعلى وكلائهم.")
_SCOPE_AR2 = ("تسري التعليمات التنظيمية لحماية المستهلك المالي الصادرة عن البنك المركزي اليمني – عدن (المرجع 589/CBY/2023، بتاريخ "
              "20 أغسطس 2023)، بحسب نصها، على مقدمي المنتجات والخدمات المالية في الجمهورية اليمنية الخاضعين لرقابة «البنك المركزي» "
              "وإشرافه وعلى وكلائهم؛ وبوصفها أداة صادرة عن البنك المركزي اليمني – عدن، فهي تشمل مقدمي الخدمات الذين يخضعون لرقابته.")
_JD_EN = "The Instructions do not make clear how items ج and د relate."
_JD_EN2 = "Item د refers back to item ج's period, but the Instructions do not say whether its extension replaces or adds to item ج's."
_JD_AR = "ولا توضح التعليمات العلاقة بين البندين (ج) و(د)."
_JD_AR2 = ("ويحيل البند (د) إلى مدة البند (ج)، لكن التعليمات لا تبيّن ما إذا كان تمديده يحل محل تمديد البند (ج) أو يُضاف إليه.")
for _a, _b in ((_SCOPE_EN, _SCOPE_EN2), (_JD_EN, _JD_EN2),
               ("provides that the consumer may take the complaint to CBY-Aden's consumer-protection department, if no reply came "
                "in time or the consumer is not satisfied with the decision,",
                "provides that the consumer may take the complaint to the issuing central bank's consumer-protection department, if "
                "no reply came in time, the complaint was not handled as the Instructions provide, or the consumer is not "
                "satisfied with the decision,")):
    assert CP_EN.count(_a) == 1, _a[:50]
    CP_EN = CP_EN.replace(_a, _b)
for _a, _b in ((_SCOPE_AR, _SCOPE_AR2), (_JD_AR, _JD_AR2),
               ("إلى الإدارة المختصة بحماية العملاء في البنك المركزي اليمني – عدن، إذا لم يتلقَّ ردًّا في الوقت المحدد أو لم يرضَ "
                "بالقرار،",
                "إلى الإدارة المختصة بحماية العملاء في البنك المركزي المُصدِر، إذا لم يتلقَّ ردًّا في الوقت المحدد، أو لم يُتعامل مع "
                "شكواه بالطريقة التي تنص عليها التعليمات، أو لم يرضَ بالقرار،")):
    assert CP_AR.count(_a) == 1, _a[:50]
    CP_AR = CP_AR.replace(_a, _b)
for _a, _b in (("which apply to the providers under CBY-Aden's supervision and their agents:",
                "which apply, in their own words, to providers in the Republic of Yemen under the supervision of “the Central "
                "Bank” and to their agents:"),
               ("(items ج and د, whose relationship the Instructions do not make clear)",
                "(items ج and د; the Instructions do not say whether د's extension replaces or adds to ج's)"),
               ("for taking the complaint to CBY-Aden,", "for taking the complaint to the issuing central bank,")):
    assert VIS_CP_EN.count(_a) == 1, _a[:50]
    VIS_CP_EN = VIS_CP_EN.replace(_a, _b)
for _a, _b in (("التي تسري على مقدمي الخدمات الخاضعين لرقابة البنك المركزي اليمني – عدن وعلى وكلائهم:",
                "التي تسري، بحسب نصها، على مقدمي الخدمات في الجمهورية اليمنية الخاضعين لرقابة «البنك المركزي» وعلى وكلائهم:"),
               ("(البندان (ج) و(د)، ولا توضح التعليمات العلاقة بينهما)",
                "(البندان (ج) و(د)؛ ولا تبيّن التعليمات ما إذا كان تمديد البند (د) يحل محل تمديد البند (ج) أو يُضاف إليه)"),
               ("يرفع خلالها المستهلك الشكوى إلى البنك المركزي اليمني – عدن،", "يرفع خلالها المستهلك الشكوى إلى البنك المركزي المُصدِر،")):
    assert VIS_CP_AR.count(_a) == 1, _a[:50]
    VIS_CP_AR = VIS_CP_AR.replace(_a, _b)
CLM011_LIM = ((CLM011_LIM[0][0], CLM011_LIM[0][1].replace(
                   "The published text does not make clear how items ج and د of Article 9 relate, so no total period is given here.",
                   "Item د of Article 9 refers back to item ج's period, but the Instructions do not say whether its extension "
                   "replaces or adds to item ج's, so no total period is given here.")),
              (CLM011_LIM[1][0], CLM011_LIM[1][1].replace(
                   "ولا يوضح النص المنشور العلاقة بين البندين (ج) و(د) من المادة 9، لذلك لا تُذكر هنا مدة إجمالية؛",
                   "ويحيل البند (د) من المادة 9 إلى مدة البند (ج)، لكن التعليمات لا تبيّن ما إذا كان تمديده يحل محل تمديد البند (ج) "
                   "أو يُضاف إليه، لذلك لا تُذكر هنا مدة إجمالية؛")))
VIS_LIM = ((VIS_LIM[0][0], VIS_LIM[0][1].replace("the Instructions do not make clear how items ج and د relate, so no total "
                                                 "period is shown.",
                                                 "item د refers back to item ج's period, but the Instructions do not say whether "
                                                 "its extension replaces or adds to item ج's, so no total period is shown.")),
           (VIS_LIM[1][0], VIS_LIM[1][1].replace("ولا توضح التعليمات العلاقة بين البندين (ج) و(د)، لذلك لا تُعرض مدة إجمالية.",
                                                 "ويحيل البند (د) إلى مدة البند (ج)، لكن التعليمات لا تبيّن ما إذا كان تمديده يحل "
                                                 "محل تمديد البند (ج) أو يُضاف إليه، لذلك لا تُعرض مدة إجمالية.")))
assert "refers back" in CLM011_LIM[0][1] and "يحيل" in CLM011_LIM[1][1] and "refers back" in VIS_LIM[0][1] and "يحيل" in VIS_LIM[1][1]
FCP_ARCH["FCP-ARCH-006"] = (FCP_ARCH["FCP-ARCH-006"][0].replace(
    "The Instructions do not make clear how the two items relate.",
    "Item د refers back to item ج's period; the Instructions do not say whether its extension replaces or adds to item ج's."),
    FCP_ARCH["FCP-ARCH-006"][1])
assert "refers back" in FCP_ARCH["FCP-ARCH-006"][0]
CP_DEF["universe_en"] = ("Providers of financial products and services in the Republic of Yemen under the supervision of “the "
                         "Central Bank”, and their agents, as the Instructions, issued by the Central Bank of Yemen – Aden "
                         "(CBY-Aden), define their scope (Article 1)")
CP_DEF["universe_ar"] = ("مقدمو المنتجات والخدمات المالية في الجمهورية اليمنية الخاضعون لرقابة «البنك المركزي» وإشرافه، ووكلاؤهم، "
                         "كما تحدد التعليمات الصادرة عن البنك المركزي اليمني – عدن نطاقها (المادة 1).")
VIS11["denominator_universe"] = ("Providers of financial products and services in the Republic of Yemen under the supervision of "
                                 "“the Central Bank”, and their agents, as the 2023 Instructions of CBY-Aden define their scope")
VIS11["what_it_shows_en"] = VIS11["what_it_shows_en"].replace("for taking the complaint to CBY-Aden", "for taking the complaint "
                                                              "to the issuing central bank")
VIS11["what_it_shows_ar"] = VIS11["what_it_shows_ar"].replace("يرفع خلالها المستهلك الشكوى إلى البنك المركزي اليمني – عدن",
                                                              "يرفع خلالها المستهلك الشكوى إلى البنك المركزي المُصدِر")
OECD_FCP = ((OECD_FCP[0][0], OECD_FCP[0][1].replace(
                 "The Instructions apply to the providers under CBY-Aden's supervision and their agents.",
                 "The Instructions apply, in their own words, to providers in the Republic of Yemen under the supervision of “the "
                 "Central Bank” and to their agents.")),
            (OECD_FCP[1][0], OECD_FCP[1][1].replace(
                 "وتسري التعليمات على مقدمي الخدمات الخاضعين لرقابة البنك المركزي اليمني – عدن ووكلائهم.",
                 "وتسري التعليمات، بحسب نصها، على مقدمي الخدمات في الجمهورية اليمنية الخاضعين لرقابة «البنك المركزي» وعلى وكلائهم.")))
MA006 = ((MA006[0][0], MA006[0][1].replace(
              "They require providers to report to CBY-Aden's consumer-protection department every three months",
              "They require the providers they cover to report to the central bank's consumer-protection department every three "
              "months").replace("and provide for CBY-Aden to prepare and publish", "and provide for the central bank to prepare "
                                "and publish")),
         (MA006[1][0], MA006[1][1].replace(
              "وتُلزم مقدمي الخدمات برفع تقارير كل ثلاثة أشهر إلى الإدارة المختصة بحماية العملاء في البنك المركزي اليمني – عدن",
              "وتُلزم مقدمي الخدمات المشمولين بها برفع تقارير كل ثلاثة أشهر إلى الإدارة المختصة بحماية العملاء في البنك المركزي")
          .replace("وتنص على أن يعدّ البنك المركزي اليمني – عدن تقارير سنوية", "وتنص على أن يعدّ البنك المركزي تقارير سنوية")))
for _x in ("covering the providers", ):
    pass
assert "the providers they cover" in MA006[0][1] and "المشمولين بها" in MA006[1][1]
assert "in their own words" in OECD_FCP[0][1] and "بحسب نصها" in OECD_FCP[1][1]

# ======================================================================================================================
# Confirmation-pass revisions (both lenses: KEEP). Domain: s4 names the bound an estimate; the route description says
# "the 2021 wave"; s9's test holds "where the two can be told apart"; s8 punctuation. Arabic: «صالح للاستخدام» on the
# right noun in the route description; the s4 attribution phrase; «الأرقام بحسب الجنس»; item ذ(1) is about the
# complainant («عدم التعامل مع مُقدّم الشكوى»), in both languages.
# ======================================================================================================================
def _secw(lang, new):
    hits = [i for i, e in enumerate(SECW) if e[3] == lang]
    assert len(hits) == 1
    SECW[hits[0]] = SECW[hits[0]][:6] + (new,)


S4_EN = S4_EN.replace("The bound set out above, by CauseWay’s calculation at least 62.7% of recipients in surveyed areas without "
                      "an account at a financial institution, bears only",
                      "The bound set out above, by CauseWay’s calculation at least 62.7% of recipients in surveyed areas without "
                      "an account at a financial institution, itself a survey estimate, bears only")
S4_AR = S4_AR.replace("والحدّ المبيَّن أعلاه، أي أن 62.7% على الأقل من المتلقين في المناطق التي شملها المسح لم يكن لديهم حساب لدى "
                      "مؤسسة مالية بحساب أجرته CauseWay، لا يتصل إلا",
                      "والحدّ المبيَّن أعلاه، وهو بحساب أجرته CauseWay أن 62.7% على الأقل من المتلقين في المناطق التي شملها المسح لم "
                      "يكن لديهم حساب لدى مؤسسة مالية، وهو تقدير مسحي، لا يتصل إلا")
assert "itself a survey estimate, bears only" in S4_EN and "وهو تقدير مسحي، لا يتصل إلا" in S4_AR
_secw("en", S4_EN)
_secw("ar", S4_AR)
META_EN = ("A hypothesis on Yemen's domestic remittances and accounts. For the 2021 wave, no usable weighted channel estimate is "
           "published or held; World Bank documentation records the item as asked and answered.")
META_AR = ("فرضية عن الحوالات المحلية والحسابات في اليمن. لموجة 2021 لا يُنشر ولا يُحتفظ هنا بأي تقدير موزون للقناة صالح "
           "للاستخدام؛ ويسجل توثيق البنك الدولي أن السؤال طُرح وأُجيب عنه.")
assert len(META_EN) <= 200 and len(META_AR) <= 200
_sec(R, 8, "en", "body", "and the only channel values are for 2014;",
     "and the only weighted channel values are for 2014; for the 2021 wave none usable here is published or held, though World "
     "Bank documentation records the item as asked and answered;")
_sec(R, 8, "ar", "body", "وقيم القنوات الوحيدة تخص عام 2014؛",
     "وقيم القنوات الموزونة الوحيدة تخص عام 2014؛ ولا يُنشر لموجة 2021 أي تقدير موزون صالح للاستخدام هنا ولا يُحتفظ به، وإن كان "
     "توثيق البنك الدولي يسجل أن السؤال طُرح وأُجيب عنه؛")
_sec(R, 9, "en", "body", "If households that receive transfers",
     "If adults who receive transfers received them into accounts or wallets of their own more often than through exchange "
     "companies and other money-transfer providers, where the two can be told apart, the hypothesis would fail.")
_sec(R, 9, "ar", "body", "وإذا تبيّن أن الأسر التي تتلقى الحوالات",
     "وإذا تبيّن أن البالغين الذين يتلقون الحوالات يستلمونها في حسابات أو محافظ إلكترونية خاصة بهم أكثر مما يستلمونها عبر شركات "
     "الصرافة وغيرها من مقدمي خدمات تحويل الأموال، حيث يمكن التمييز بينهما، سقطت الفرضية.")
YLG_AR = YLG_AR.replace("أما أرقام الجنس فتغطي فترتين مختلفتين", "أما الأرقام بحسب الجنس فتغطي فترتين مختلفتين")
assert "الأرقام بحسب الجنس" in YLG_AR
FIRMS_NEW_AR = ("وتقيس بيانات الضمانات شيئًا آخر. " + YLG_AR + " ويعدّ المصدران خطابات الضمان أو المعاملات لا المنشآت: "
                "فتبين الأرقام ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت "
                "الأصغر والصغيرة والمتوسطة.")
_sec("/firms/", 7, "ar", "body", "وتقدم بيانات الضمانات صورة من نوع آخر:", FIRMS_NEW_AR)
_cell(O6, "CLM-059", "summary_ar", "وبصورة منفصلة، تفيد منظمة", YLG_AR)
CP_EN = CP_EN.replace("the complaint was not handled as the Instructions provide,", "the complainant was not dealt with as the "
                      "Instructions provide,")
CP_AR = CP_AR.replace("أو لم يُتعامل مع شكواه بالطريقة التي تنص عليها التعليمات،", "أو لم يُتعامل معه بالطريقة التي تنص عليها "
                      "التعليمات،")
assert "the complainant was not dealt with" in CP_EN and "أو لم يُتعامل معه بالطريقة" in CP_AR
