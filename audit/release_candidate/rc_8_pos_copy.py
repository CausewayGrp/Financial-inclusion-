# -*- coding: utf-8 -*-
"""RC-8, part POS — the copy that moves the CBY-Aden monthly POS series from January 2026 to June 2026.

Read in the originals on 3 October 2026 (audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md): the February–June 2026
releases are listed on CBY-Aden's Arabic payments page (https://cby-ye.com/pages/33) only; the English page
(https://english.cby-ye.com/pages/27) still ends at January 2026. Drafted cell by cell against the 148 Master cells that
named the January endpoint or the 26 September check (115 changed here, 33 left with a reason in LEAVE), plus 23 cells
outside that set that must move with them (EXTRA).

Owner note of 3 October 2026, 03:10, point 2: the May 2026 release contradicts itself (terminals +2.4% and transactions
+9.9% displayed against totals that do not give them). Nothing here resolves that or computes the change the source
contradicts: the totals and the displayed percentage are printed, and the derived change is withheld with its reason.

SPEC/EXTRA entries: (R, [(old, new), ...]) replaces each `old` substring, which must occur exactly once; (F, text) replaces
the whole cell, guarded by the SHA-256 prefix of the text it expects to find (OLD_SHA).
"""
import hashlib

CUR_EN = ("The latest observation in this record refers to June 2026; the series runs monthly from March 2025{gap}. "
          "June 2026 was the latest monthly POS release on the Arabic payments page of the Central Bank of Yemen – Aden "
          "(CBY-Aden) when checked on 3 October 2026; the English payments page still listed January 2026 as the latest. "
          "The figures should not be read as describing a later period unless a newer comparable release is published.")
CUR_AR = ("تعود أحدث مشاهدة في هذا السجل إلى يونيو 2026، وتمتد السلسلة شهريًا منذ مارس 2025{gap}. "
          "وكان يونيو 2026 أحدث إصدار شهري لنقاط البيع في صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن "
          "كما اطُّلع عليها في 3 أكتوبر 2026، بينما كانت صفحة المدفوعات بالإنجليزية لا تزال تعرض يناير 2026 بوصفه أحدث إصدار. "
          "ولا تُقرأ الأرقام على أنها تصف فترة لاحقة ما لم يُنشر إصدار أحدث قابل للمقارنة.")
GAP_EN = ", with no value for September 2025"
GAP_AR = " من دون قيمة لشهر سبتمبر 2025"

# May 2026 (owner note, 3 October 2026, point 2): the release displays a change its own totals do not give. The totals
# and the displayed percentage are printed; no change is derived for April to May 2026, and the reason is stated.
MAY_TERM_EN = ("The May 2026 source graphic displays +2.4%, which the published totals for April 2026 (1,583) and May 2026 "
               "(1,636) do not give; because the source contradicts itself, this resource computes no change for April to May 2026.")
MAY_TERM_AR = ("ويعرض رسم مصدر مايو 2026 نسبة +2.4%، ولا يعطيها الإجماليان المنشوران لشهري أبريل 2026 (1,583) ومايو 2026 "
               "(1,636)؛ ولأن المصدر يناقض نفسه، لا يحسب هذا المورد نسبة تغير بين أبريل ومايو 2026.")
MAY_TXN_EN = ("The May 2026 source graphic displays +9.9%, which the published totals for April 2026 (30,559) and May 2026 "
              "(36,201) do not give; because the source contradicts itself, this resource computes no change for April to May 2026.")
MAY_TXN_AR = ("ويعرض رسم مصدر مايو 2026 نسبة +9.9%، ولا يعطيها الإجماليان المنشوران لشهري أبريل 2026 (30,559) ومايو 2026 "
              "(36,201)؛ ولأن المصدر يناقض نفسه، لا يحسب هذا المورد نسبة تغير بين أبريل ومايو 2026.")

TERM_SUM_EN = ("POS terminals reported by the Central Bank of Yemen – Aden (CBY-Aden) rose from 561 in March 2025 to 1,651 in June 2026, "
               "within CBY-Aden's reporting scope. Between December 2025 (1,357) and January 2026 (1,473), the raw totals imply growth "
               "of 8.55%, while the January source graphic displays +11%. " + MAY_TERM_EN + " The chart plots the reported totals, "
               "the publisher's displayed percentages are given in the chart note, and each mismatch is recorded as a discrepancy "
               "within the source. Terminal counts are devices, not merchants, unique users or an inclusion outcome.")
TERM_SUM_AR = ("ارتفع عدد أجهزة نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 561 جهازًا في مارس 2025 إلى 1,651 جهازًا في "
               "يونيو 2026، ضمن نطاق إبلاغه. وبين ديسمبر 2025 (1,357) ويناير 2026 (1,473) تعطي الإجماليات الخام نموًا نسبته 8.55%، "
               "بينما يعرض الرسم المنشور في مصدر يناير نسبة +11%. " + MAY_TERM_AR + " ويعرض الرسم البياني الإجماليات المنشورة، "
               "وتُذكر في ملاحظة الرسم النسب التي عرضها الناشر، ويُسجَّل كل فرق بوصفه اختلافًا داخل المصدر. وعدد الأجهزة لا يساوي "
               "عدد التجار أو المستخدمين الفريدين ولا يثبت نتيجة في الشمول المالي.")
TXN_SUM_EN = ("POS transactions reported by the Central Bank of Yemen – Aden (CBY-Aden) rose from 8,015 in March 2025 to 27,504 in "
              "June 2026, within CBY-Aden's reporting scope, but not steadily: the monthly high was 36,201 in May 2026. Between December "
              "2025 (21,099) and January 2026 (24,026), the raw totals imply growth of 13.87%, while the January source graphic displays "
              "+4.9%. " + MAY_TXN_EN + " The chart plots the reported totals, the displayed percentages are given in the chart note, "
              "and each mismatch is recorded as a discrepancy within the source.")
TXN_SUM_AR = ("ارتفع عدد معاملات نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 8,015 معاملة في مارس 2025 إلى 27,504 معاملات "
              "في يونيو 2026، ضمن نطاق إبلاغه، ولكن ليس بصورة مطردة: فقد بلغ أعلى مستوى شهري 36,201 معاملة في مايو 2026. وبين "
              "ديسمبر 2025 (21,099) ويناير 2026 (24,026) تعطي الإجماليات الخام نموًا نسبته 13.87%، بينما يعرض رسم مصدر يناير نسبة "
              "+4.9%. " + MAY_TXN_AR + " ويعرض الرسم البياني الإجماليات المنشورة، وتُذكر النسب المعروضة في ملاحظة الرسم، ويُسجَّل كل "
              "فرق بوصفه اختلافًا داخل المصدر.")
VAL_SUM_EN = ("The nominal value of POS transactions reported by the Central Bank of Yemen – Aden (CBY-Aden) rose from YER 320 million "
              "in March 2025 to YER 1,045 million in June 2026, within CBY-Aden's reporting scope, but not steadily: the monthly high "
              "was YER 1,579 million in May 2026. The September 2025 value is missing because no verified value is available for that "
              "month. From the January 2026 release onward the value is labelled “billion”; this resource reads it as YER "
              "million, the unit the earlier releases state, because only that reading reconciles with the month-on-month changes the "
              "releases print. The series is nominal and does not establish real-value growth, purchasing-power change, unique-user "
              "growth or financial-inclusion impact.")
VAL_SUM_AR = ("ارتفعت القيمة الاسمية لمعاملات نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 320 مليون ريال يمني في مارس "
              "2025 إلى 1,045 مليون ريال في يونيو 2026، ضمن نطاق إبلاغه، ولكن ليس بصورة مطردة: فقد بلغ أعلى مستوى شهري 1,579 مليون "
              "ريال في مايو 2026. وقيمة سبتمبر 2025 مفقودة لعدم توفر قيمة متحقق منها لذلك الشهر. وابتداءً من إصدار يناير 2026 "
              "تُدرج القيمة تحت وحدة «مليار»، لكن هذا المورد يقرؤها بملايين الريالات، وهي الوحدة التي تذكرها الإصدارات "
              "السابقة، لأن هذه القراءة وحدها تتسق مع نسب التغير الشهرية التي تطبعها الإصدارات. والسلسلة اسمية ولا تثبت نموًا "
              "بالقيمة الحقيقية أو تغيرًا في القوة الشرائية أو زيادة عدد المستخدمين الفريدين أو أثرًا على الشمول المالي.")
TERM_LIM_EN_OLD = "The +11% displayed in the January 2026 release and the 8.55% change derived from the raw totals are not arithmetically consistent."
TERM_LIM_EN_NEW = (TERM_LIM_EN_OLD + " Nor do the published April and May 2026 totals give the +2.4% displayed in the May 2026 release; "
                   "no change is computed for that month.")
TERM_LIM_AR_OLD = "وليست نسبة +11% المعروضة في إصدار يناير 2026 ونسبة التغير البالغة 8.55% المشتقة من الإجماليات الخام متسقتين حسابيًا."
TERM_LIM_AR_NEW = (TERM_LIM_AR_OLD + " كما لا يعطي الإجماليان المنشوران لشهري أبريل ومايو 2026 نسبة +2.4% المعروضة في إصدار مايو 2026، "
                   "ولا تُحسب نسبة تغير لذلك الشهر.")
TXN_LIM_EN_OLD = ("and the +4.9% displayed in the January 2026 release and the 13.87% change derived from the raw totals are not "
                  "arithmetically consistent.")
TXN_LIM_EN_NEW = (TXN_LIM_EN_OLD + " Nor do the published April and May 2026 totals give the +9.9% displayed in the May 2026 release; "
                  "no change is computed for that month.")
TXN_LIM_AR_OLD = "وليست نسبة +4.9% المعروضة في إصدار يناير 2026 ونسبة التغير البالغة 13.87% المشتقة من الإجماليات الخام متسقتين حسابيًا."
TXN_LIM_AR_NEW = (TXN_LIM_AR_OLD + " كما لا يعطي الإجماليان المنشوران لشهري أبريل ومايو 2026 نسبة +9.9% المعروضة في إصدار مايو 2026، "
                  "ولا تُحسب نسبة تغير لذلك الشهر.")

R = 'R'   # replacement-list marker
F = 'F'   # full-text marker
SPEC = {}
def rep(sheet, r, c, pairs, reason): SPEC[(sheet, r, c)] = (R, pairs, reason)
def full(sheet, r, c, text, reason): SPEC[(sheet, r, c)] = (F, text, reason)

JUN = [("January 2026", "June 2026")]
JUN_AR = [("يناير 2026", "يونيو 2026")]
WHY_PERIOD = "Series now runs to June 2026 (CBY-Aden Arabic-page releases for February–June 2026, checked 3 October 2026)."
WHY_LATEST = "States January 2026 / the January values as the latest POS month; updated to the June 2026 release."

# 02_SITE_MAP -------------------------------------------------------------------------------------------------
rep('02_SITE_MAP', 13, 7, JUN, WHY_PERIOD)
rep('02_SITE_MAP', 13, 8, JUN_AR, WHY_PERIOD)
full('02_SITE_MAP', 27, 7, "As checked on 3 October 2026, the latest monthly point-of-sale (POS) release on the Arabic payments page of the Central Bank of Yemen – Aden was June 2026.",
     "CLM-017 meta description: latest release is June 2026 on the Arabic page (checked 3 October 2026). Kept within 155 characters, so the English-page clause stays in the record body; EN and AR say the same.")
full('02_SITE_MAP', 27, 8, "عند الاطلاع في 3 أكتوبر 2026، كان يونيو 2026 أحدث إصدار شهري لنقاط البيع في صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن.",
     "Arabic pair of the CLM-017 meta description.")
rep('02_SITE_MAP', 109, 7, JUN, WHY_PERIOD)
rep('02_SITE_MAP', 109, 8, JUN_AR, WHY_PERIOD)
rep('02_SITE_MAP', 110, 7, JUN, WHY_PERIOD + " Transactions still rose overall (8,015 to 27,504) and still not steadily.")
rep('02_SITE_MAP', 110, 8, JUN_AR, WHY_PERIOD + " Transactions still rose overall and still not steadily.")
rep('02_SITE_MAP', 127, 5, [("1,473", "1,651"), ("January 2026", "June 2026")], WHY_LATEST + " Payments page title.")
rep('02_SITE_MAP', 127, 6, [("1,473", "1,651"), ("يناير 2026", "يونيو 2026")], WHY_LATEST + " Payments page title (Arabic).")

# 03_PAGE_SECTIONS --------------------------------------------------------------------------------------------
rep('03_PAGE_SECTIONS', 8, 5, [("to 1,473 in January 2026", "to 1,651 in June 2026")], WHY_LATEST + " Home page.")
rep('03_PAGE_SECTIONS', 9, 7, [("إلى 1,473 في يناير 2026", "إلى 1,651 في يونيو 2026")], WHY_LATEST + " Home page (Arabic).")
rep('03_PAGE_SECTIONS', 35, 5, [("1,473 point-of-sale (POS) terminals in January 2026", "1,651 point-of-sale (POS) terminals in June 2026")], WHY_LATEST + " /access/.")
rep('03_PAGE_SECTIONS', 35, 7, [("وإجمالي 1,473 جهاز نقاط بيع أبلغ عنه في يناير 2026", "وإجمالي 1,651 جهاز نقاط بيع أبلغ عنه في يونيو 2026")], WHY_LATEST + " /access/ (Arabic).")
rep('03_PAGE_SECTIONS', 40, 5, [("to 1,473 in January 2026", "to 1,651 in June 2026")], WHY_LATEST + " /access/.")
rep('03_PAGE_SECTIONS', 41, 7, [("إلى 1,473 جهازًا في يناير 2026", "إلى 1,651 جهازًا في يونيو 2026")], WHY_LATEST + " /access/ (Arabic).")
rep('03_PAGE_SECTIONS', 175, 5, [(
    "rose from 561 to 1,473 between March 2025 and January 2026, transaction counts from 8,015 to 24,026 (after a high of 27,187 in July 2025) and nominal transaction value from YER 320 million to YER 1,262 million.",
    "rose from 561 to 1,651 between March 2025 and June 2026, transaction counts from 8,015 to 27,504 (after a high of 36,201 in May 2026) and nominal transaction value from YER 320 million to YER 1,045 million (after a high of YER 1,579 million in May 2026).")],
    WHY_LATEST + " The transaction high moves from 27,187 (July 2025) to 36,201 (May 2026); the value series is now non-monotonic at the end, so its May 2026 high is stated the same way as the transaction high.")
rep('03_PAGE_SECTIONS', 176, 7, [(
    "ارتفع بين مارس 2025 ويناير 2026 العدد المنشور لأجهزة نقاط البيع من 561 إلى 1,473 جهازًا، وعدد المعاملات من 8,015 إلى 24,026 (بعد ذروة بلغت 27,187 معاملة في يوليو 2025)، والقيمة الاسمية للمعاملات من 320 مليون ريال إلى 1,262 مليون ريال.",
    "ارتفع بين مارس 2025 ويونيو 2026 العدد المنشور لأجهزة نقاط البيع من 561 إلى 1,651 جهازًا، وعدد المعاملات من 8,015 إلى 27,504 (بعد ذروة بلغت 36,201 معاملة في مايو 2026)، والقيمة الاسمية للمعاملات من 320 مليون ريال إلى 1,045 مليون ريال (بعد ذروة بلغت 1,579 مليون ريال في مايو 2026).")],
    "Arabic pair of r175.")
full('03_PAGE_SECTIONS', 177, 4, "June 2026 was the latest monthly POS release on CBY-Aden's Arabic payments page as checked on 3 October 2026; its English page still ends at January 2026",
     "Payments heading: latest month and check date updated; the English page still ending at January 2026 is stated (fact c).")
full('03_PAGE_SECTIONS', 177, 5, "The Arabic payments page of the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 October 2026, publishes monthly POS releases from March 2025 through June 2026; the English payments page, checked the same day, still ends at January 2026. This resource therefore stops the monthly series at June 2026. That does not mean activity stopped; it means no later monthly release had been published on the Arabic page when it was checked.",
     "Payments currentness body: Arabic page to June 2026, English page to January 2026, both checked 3 October 2026; same structure and boundary sentence.")
full('03_PAGE_SECTIONS', 178, 6, "يونيو 2026 هو أحدث إصدار شهري لنقاط البيع في صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن، كما اطُّلع عليها في 3 أكتوبر 2026؛ ولا تزال صفحته بالإنجليزية تنتهي عند يناير 2026",
     "Arabic pair of r177 heading.")
full('03_PAGE_SECTIONS', 178, 7, "تعرض صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن، كما اطُّلع عليها في 3 أكتوبر 2026، إصدارات شهرية لنقاط البيع من مارس 2025 حتى يونيو 2026، بينما لا تزال صفحة المدفوعات بالإنجليزية، التي اطُّلع عليها في اليوم نفسه، تنتهي عند يناير 2026. لذلك تنتهي السلسلة الشهرية عند يونيو 2026. ولا يعني ذلك أن النشاط توقف؛ بل يعني أن الصفحة بالعربية، كما اطُّلع عليها، لا تعرض إصدارًا شهريًا أحدث.",
     "Arabic pair of r177 body.")
rep('03_PAGE_SECTIONS', 247, 5, [("rose from 561 to 1,473 between March 2025 and January 2026", "rose from 561 to 1,651 between March 2025 and June 2026")], WHY_LATEST + " Reading define-what-you-count.")
rep('03_PAGE_SECTIONS', 247, 7, [("من 561 إلى 1,473 بين مارس 2025 ويناير 2026", "من 561 إلى 1,651 بين مارس 2025 ويونيو 2026")], WHY_LATEST + " Reading (Arabic).")
rep('03_PAGE_SECTIONS', 264, 5, [("to 1,473 in January 2026", "to 1,651 in June 2026")], WHY_LATEST + " Reading from-rail-to-result; the following sentence on June–August 2026 institution-building stays (chronology, no causal link drawn).")
rep('03_PAGE_SECTIONS', 264, 7, [("إلى 1,473 جهازًا في يناير 2026", "إلى 1,651 جهازًا في يونيو 2026")], WHY_LATEST + " Reading (Arabic).")
rep('03_PAGE_SECTIONS', 281, 5, [("A January 2026 count of POS terminals", "A June 2026 count of POS terminals")], WHY_LATEST + " Reading reforms-newer-than-people-evidence.")
rep('03_PAGE_SECTIONS', 281, 7, [("وعدد أجهزة نقاط البيع في يناير 2026 دليل", "وعدد أجهزة نقاط البيع في يونيو 2026 دليل")], WHY_LATEST + " Reading (Arabic).")
rep('03_PAGE_SECTIONS', 282, 5, [("to 1,473 in January 2026", "to 1,651 in June 2026")], WHY_LATEST + " Reading reforms-newer-than-people-evidence.")
rep('03_PAGE_SECTIONS', 282, 7, [("إلى 1,473 في يناير 2026", "إلى 1,651 في يونيو 2026")], WHY_LATEST + " Reading (Arabic).")

# 06_EVIDENCE_OBJECTS · CLM-003 --------------------------------------------------------------------------------
full('06_EVIDENCE_OBJECTS', 6, 6,
     "POS terminals reported by the Central Bank of Yemen – Aden (CBY-Aden) rose from 561 in March 2025 to 1,651 in June 2026, within CBY-Aden's reporting scope. The December 2025 total of 1,357 and the January 2026 total of 1,473 imply growth of 8.55%, while the January source graphic displays +11%. The May 2026 source graphic displays +2.4%, which the April 2026 total of 1,583 and the May 2026 total of 1,636 do not give; because the source contradicts itself, no change is computed for April to May 2026. The POS terminals chart plots the published totals, the displayed percentages are stated under 'How was it produced?' in this record, and each difference is recorded as an inconsistency within the source.",
     "Endpoint to June 2026. The 8.55% sentence is kept (the January contradiction, a closed decision). The May 2026 contradiction is shown, not resolved: the totals and the displayed +2.4% are printed and no change is derived (owner note, 3 October 2026, point 2).")
full('06_EVIDENCE_OBJECTS', 6, 7,
     "ارتفع عدد أجهزة نقاط البيع التي يُبلغ عنها البنك المركزي اليمني – عدن من 561 جهازًا في مارس 2025 إلى 1,651 جهازًا في يونيو 2026، ضمن نطاق الإبلاغ لدى البنك المركزي في عدن. ويعطي الانتقال من 1,357 جهازًا في ديسمبر 2025 إلى 1,473 جهازًا في يناير 2026 نموًا نسبته 8.55%، بينما يعرض رسم المصدر لشهر يناير +11%. ويعرض رسم المصدر لشهر مايو 2026 نسبة +2.4%، ولا يعطيها إجمالي أبريل 2026 البالغ 1,583 جهازًا وإجمالي مايو 2026 البالغ 1,636 جهازًا؛ ولأن المصدر يناقض نفسه، لا تُحسب نسبة تغير بين أبريل ومايو 2026. ويعرض الرسم البياني لأجهزة نقاط البيع الإجماليات المنشورة، وتُذكر النسب المعروضة تحت «كيف أُنتج؟» في هذا السجل، ويُسجَّل كل فرق بوصفه تعارضًا داخل المصدر نفسه.",
     "Arabic pair of CLM-003 summary.")
rep('06_EVIDENCE_OBJECTS', 6, 8, JUN, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 6, 9, JUN_AR, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 6, 11, JUN_AR, WHY_PERIOD + " English pair is period_en c10 'Mar-2025–Jan-2026' (outside the dump; see proposals_extra.json).")
rep('06_EVIDENCE_OBJECTS', 6, 14, [("It is shown beside the +11% displayed in the January release rather than replacing it.",
     "It is shown beside the +11% displayed in the January release rather than replacing it. The May 2026 release displays +2.4%, which the published April (1,583) and May (1,636) totals do not give. Because the release contradicts itself, this resource derives no change for April to May 2026; it shows the two published totals and the displayed percentage.")],
     "The May 2026 terminal contradiction, shown and not resolved (owner note, 3 October 2026, point 2).")
rep('06_EVIDENCE_OBJECTS', 6, 15, [("وتُعرض إلى جانب نسبة +11% المعروضة في إصدار يناير من دون أن تحل محلها.",
     "وتُعرض إلى جانب نسبة +11% المعروضة في إصدار يناير من دون أن تحل محلها. ويعرض إصدار مايو 2026 نسبة +2.4%، ولا يعطيها الإجماليان المنشوران لشهري أبريل (1,583) ومايو (1,636). ولأن الإصدار يناقض نفسه، لا يشتق هذا المورد نسبة تغير بين أبريل ومايو 2026، بل يعرض الإجماليين المنشورين والنسبة المعروضة.")],
     "Arabic pair of CLM-003 method.")
rep('06_EVIDENCE_OBJECTS', 6, 16, [("and the January 2026 release shows material discrepancies between its displayed growth percentages and the raw terminal and transaction totals.",
     "and the January 2026 and May 2026 releases show material discrepancies between their displayed growth percentages and the raw terminal and transaction totals.")],
     "Fact (a): the May 2026 release joins January 2026 as a release whose displayed changes do not reconcile with its totals.")
rep('06_EVIDENCE_OBJECTS', 6, 17, [("كما يتضمن إصدار يناير 2026 فروقًا جوهرية", "كما يتضمن إصدارا يناير 2026 ومايو 2026 فروقًا جوهرية")], "Arabic pair of CLM-003 limitations.")
full('06_EVIDENCE_OBJECTS', 6, 18, CUR_EN.format(gap=""), "Currentness: latest observation June 2026; Arabic page checked 3 October 2026; English page still at January 2026 (fact c).")
full('06_EVIDENCE_OBJECTS', 6, 19, CUR_AR.format(gap=""), "Arabic pair of CLM-003 currentness.")

# 06_EVIDENCE_OBJECTS · CLM-017 --------------------------------------------------------------------------------
full('06_EVIDENCE_OBJECTS', 22, 4, "Latest monthly point-of-sale (POS) release listed by CBY-Aden: June 2026 on its Arabic page, January 2026 on its English page (checked 3 October 2026)",
     "CLM-017 title: June 2026 on the Arabic page; the English page still lists January 2026 (required by the brief); check date 3 October 2026. Both pages are named in the title because the record is shown in lists to English readers who would otherwise find January on the English page.")
full('06_EVIDENCE_OBJECTS', 22, 5, "أحدث إصدار شهري لنقاط البيع لدى البنك المركزي اليمني – عدن: يونيو 2026 في صفحته بالعربية، ويناير 2026 في صفحته بالإنجليزية (اطُّلع عليهما في 3 أكتوبر 2026)",
     "Arabic pair of CLM-017 title.")
full('06_EVIDENCE_OBJECTS', 22, 6, "The Arabic payments page of the Central Bank of Yemen – Aden (CBY-Aden) lists monthly POS releases from March 2025 to June 2026; the English payments page lists them only to January 2026. When both pages were checked on 3 October 2026, June 2026 was the latest release listed on the Arabic page and January 2026 on the English page; no later month is inferred.",
     "CLM-017 summary rewritten for two pages; 'no later month is inferred' kept.")
full('06_EVIDENCE_OBJECTS', 22, 7, "تعرض صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن إصدارات شهرية لنقاط البيع من مارس 2025 إلى يونيو 2026، بينما لا تعرضها صفحة المدفوعات بالإنجليزية إلا حتى يناير 2026. وعند الاطلاع على الصفحتين في 3 أكتوبر 2026 كان إصدار يونيو 2026 أحدث إصدار مدرج في الصفحة بالعربية، وإصدار يناير 2026 أحدث إصدار مدرج في الصفحة بالإنجليزية، من دون استنتاج أي شهر لاحق.",
     "Arabic pair of CLM-017 summary.")
full('06_EVIDENCE_OBJECTS', 22, 10, "Monthly releases for March 2025 to June 2026 on the Arabic page (to January 2026 on the English page); pages checked on 3 October 2026",
     "CLM-017 period.")
full('06_EVIDENCE_OBJECTS', 22, 11, "إصدارات شهرية من مارس 2025 إلى يونيو 2026 في الصفحة بالعربية (وحتى يناير 2026 في الصفحة بالإنجليزية)؛ واطُّلع على الصفحتين في 3 أكتوبر 2026",
     "Arabic pair of CLM-017 period.")
full('06_EVIDENCE_OBJECTS', 22, 14, "The lists of monthly POS releases on the Arabic and English payments pages of the Central Bank of Yemen – Aden (CBY-Aden) were checked on 3 October 2026; the latest release listed was June 2026 on the Arabic page and January 2026 on the English page. Values are taken as published, and arithmetic discrepancies within the releases are kept.",
     "CLM-017 method: both pages, one check date.")
full('06_EVIDENCE_OBJECTS', 22, 15, "اطُّلع في 3 أكتوبر 2026 على قائمتي الإصدارات الشهرية لنقاط البيع في صفحتي المدفوعات بالعربية وبالإنجليزية لدى البنك المركزي اليمني – عدن، وكان آخر إصدار مدرج هو إصدار يونيو 2026 في الصفحة بالعربية وإصدار يناير 2026 في الصفحة بالإنجليزية. وتُؤخذ القيم كما نُشرت، مع الإبقاء على الفروق الحسابية الواردة في الإصدارات.",
     "Arabic pair of CLM-017 method.")
full('06_EVIDENCE_OBJECTS', 22, 16, "It does not show that POS activity stopped after June 2026; it identifies only the latest monthly release listed on the Arabic payments page of the Central Bank of Yemen – Aden (CBY-Aden) when checked on 3 October 2026. That the English payments page still ends at January 2026 does not mean that no later release was published.",
     "CLM-017 limitations: boundary moved to June 2026; adds the converse boundary for the English page.")
full('06_EVIDENCE_OBJECTS', 22, 17, "لا يعني ذلك توقف نشاط نقاط البيع بعد يونيو 2026؛ بل يحدد فقط أحدث إصدار شهري مدرج في صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن كما اطُّلع عليها في 3 أكتوبر 2026. ولا يعني توقف صفحة المدفوعات بالإنجليزية عند يناير 2026 أنه لم يصدر إصدار لاحق.",
     "Arabic pair of CLM-017 limitations.")
full('06_EVIDENCE_OBJECTS', 22, 18, "June 2026 was the latest monthly POS release on the Arabic payments page of the Central Bank of Yemen – Aden (CBY-Aden) when checked on 3 October 2026; the English payments page still listed January 2026 as the latest. A later release, once listed, would replace it as the latest observation.",
     "CLM-017 currentness.")
full('06_EVIDENCE_OBJECTS', 22, 19, "كان يونيو 2026 أحدث إصدار شهري لنقاط البيع في صفحة المدفوعات بالعربية لدى البنك المركزي اليمني – عدن كما اطُّلع عليها في 3 أكتوبر 2026، بينما كانت صفحة المدفوعات بالإنجليزية لا تزال تعرض يناير 2026 بوصفه أحدث إصدار. وإذا أُدرج إصدار لاحق فإنه يحل محله بوصفه أحدث مشاهدة.",
     "Arabic pair of CLM-017 currentness.")

# 06_EVIDENCE_OBJECTS · VIS-POS-TERMINALS ---------------------------------------------------------------------
full('06_EVIDENCE_OBJECTS', 66, 6, TERM_SUM_EN, "Endpoint to June 2026; the January contradiction is kept and the May 2026 one (fact a) added in the same form. Identical to the 11_VISUAL_LIBRARY accessible summary.")
full('06_EVIDENCE_OBJECTS', 66, 7, TERM_SUM_AR, "Arabic pair.")
rep('06_EVIDENCE_OBJECTS', 66, 8, JUN, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 66, 9, JUN_AR, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 66, 11, JUN_AR, WHY_PERIOD + " English pair is period_en c10 (outside the dump; see proposals_extra.json).")
rep('06_EVIDENCE_OBJECTS', 66, 14, [("neither figure replaces the other. A smaller mismatch",
     "neither figure replaces the other. The May 2026 release displays +2.4%, which the published April (1,583) and May (1,636) totals do not give; because the release contradicts itself, no April to May change is derived, and the two totals and the displayed percentage are shown as published. A smaller mismatch")],
     "The May 2026 contradiction in the chart note (the method renders under the chart).")
rep('06_EVIDENCE_OBJECTS', 66, 15, [("ولا تحل إحدى القيمتين محل الأخرى. ويُبقى أيضًا",
     "ولا تحل إحدى القيمتين محل الأخرى. ويعرض إصدار مايو 2026 نسبة +2.4%، ولا يعطيها الإجماليان المنشوران لشهري أبريل (1,583) ومايو (1,636)؛ ولأن الإصدار يناقض نفسه، لا يُشتق تغير بين أبريل ومايو، ويُعرض الإجماليان والنسبة المعروضة كما نُشرت. ويُبقى أيضًا")],
     "Arabic pair.")
rep('06_EVIDENCE_OBJECTS', 66, 16, [(TERM_LIM_EN_OLD, TERM_LIM_EN_NEW)], "Fact (a) in the limitations.")
rep('06_EVIDENCE_OBJECTS', 66, 17, [(TERM_LIM_AR_OLD, TERM_LIM_AR_NEW)], "Arabic pair.")
full('06_EVIDENCE_OBJECTS', 66, 18, CUR_EN.format(gap=""), "Currentness, as CLM-003.")
full('06_EVIDENCE_OBJECTS', 66, 19, CUR_AR.format(gap=""), "Arabic pair.")

# 06_EVIDENCE_OBJECTS · VIS-POS-TRANSACTIONS ------------------------------------------------------------------
full('06_EVIDENCE_OBJECTS', 67, 6, TXN_SUM_EN, "Endpoint 27,504 (June 2026); monthly high now 36,201 in May 2026 (fact d); January contradiction kept, May 2026 one added (fact a). Identical to the accessible summary.")
full('06_EVIDENCE_OBJECTS', 67, 7, TXN_SUM_AR, "Arabic pair; «27,504 معاملات» follows the last-element agreement rule (…وأربع معاملات).")
rep('06_EVIDENCE_OBJECTS', 67, 8, JUN, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 67, 9, JUN_AR, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 67, 11, JUN_AR, WHY_PERIOD + " English pair is period_en c10 (outside the dump).")
rep('06_EVIDENCE_OBJECTS', 67, 14, [("is kept beside the +4.9% displayed in the January release.",
     "is kept beside the +4.9% displayed in the January release. The May 2026 release displays +9.9%, which the published April (30,559) and May (36,201) totals do not give; because the release contradicts itself, no April to May change is derived, and the two totals and the displayed percentage are shown as published.")],
     "The May 2026 contradiction in the chart note.")
rep('06_EVIDENCE_OBJECTS', 67, 15, [("ويُبقيه إلى جانب نسبة +4.9% المعروضة في إصدار يناير.",
     "ويُبقيه إلى جانب نسبة +4.9% المعروضة في إصدار يناير. ويعرض إصدار مايو 2026 نسبة +9.9%، ولا يعطيها الإجماليان المنشوران لشهري أبريل (30,559) ومايو (36,201)؛ ولأن الإصدار يناقض نفسه، لا يُشتق تغير بين أبريل ومايو، ويُعرض الإجماليان والنسبة المعروضة كما نُشرت.")],
     "Arabic pair.")
rep('06_EVIDENCE_OBJECTS', 67, 16, [(TXN_LIM_EN_OLD, TXN_LIM_EN_NEW)], "Fact (a) in the limitations.")
rep('06_EVIDENCE_OBJECTS', 67, 17, [(TXN_LIM_AR_OLD, TXN_LIM_AR_NEW)], "Arabic pair.")
full('06_EVIDENCE_OBJECTS', 67, 18, CUR_EN.format(gap=""), "Currentness, as CLM-003.")
full('06_EVIDENCE_OBJECTS', 67, 19, CUR_AR.format(gap=""), "Arabic pair.")

# 06_EVIDENCE_OBJECTS · VIS-POS-VALUE -------------------------------------------------------------------------
full('06_EVIDENCE_OBJECTS', 68, 6, VAL_SUM_EN, "Endpoint YER 1,045 million (June 2026); high YER 1,579 million in May 2026 (fact d); unit disclosure (fact b). Identical to the accessible summary.")
full('06_EVIDENCE_OBJECTS', 68, 7, VAL_SUM_AR, "Arabic pair.")
rep('06_EVIDENCE_OBJECTS', 68, 8, JUN, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 68, 9, JUN_AR, WHY_PERIOD)
rep('06_EVIDENCE_OBJECTS', 68, 11, JUN_AR, WHY_PERIOD + " English pair is period_en c10 (outside the dump).")
full('06_EVIDENCE_OBJECTS', 68, 18, CUR_EN.format(gap=GAP_EN), "Currentness, as CLM-003, keeping the September 2025 gap.")
full('06_EVIDENCE_OBJECTS', 68, 19, CUR_AR.format(gap=GAP_AR), "Arabic pair.")

# 08_READINGS -------------------------------------------------------------------------------------------------
for r in (7, 8, 13):
    rep('08_READINGS', r, 21, [("March 2025 – January 2026", "March 2025 – June 2026")], WHY_PERIOD + " Reading evidence-period line.")
    rep('08_READINGS', r, 22, [("مارس 2025 – يناير 2026", "مارس 2025 – يونيو 2026")], WHY_PERIOD + " Reading evidence-period line (Arabic).")

# 11_VISUAL_LIBRARY -------------------------------------------------------------------------------------------
full('11_VISUAL_LIBRARY', 16, 7, "Monthly POS-terminal totals as published. For December 2025 to January 2026 the source displays +11%, while the totals of 1,357 and 1,473 imply +8.55%; for April to May 2026 it displays +2.4%, which the totals of 1,583 and 1,636 do not give, and no change is derived for that month. The published figures are kept and none is corrected.",
     "The May 2026 contradiction in what the chart shows; no change derived.")
full('11_VISUAL_LIBRARY', 16, 8, "يعرض الإجماليات الشهرية لأجهزة نقاط البيع كما نُشرت. وبين ديسمبر 2025 ويناير 2026 يعرض المصدر نسبة +11%، بينما يعطي الإجماليان 1,357 و1,473 نسبة +8.55%؛ وبين أبريل ومايو 2026 يعرض نسبة +2.4% لا يعطيها الإجماليان 1,583 و1,636، ولا يُشتق تغير لذلك الشهر. وتبقى الأرقام المنشورة ظاهرة ولا يُصحَّح أي منها.",
     "Arabic pair.")
full('11_VISUAL_LIBRARY', 16, 18, "Raw monthly line with exact month/source detail and explicit contradiction annotations for Dec-2025→Jan-2026 (1,357→1,473 ≈ +8.55%; source graphic displays +11%) and Apr-2026→May-2026 (1,583→1,636; source graphic displays +2.4%; no change derived, because the source contradicts itself). No smoothing or silent overwrite.",
     "Encoding contract gains the May 2026 annotation; the 2026-04/05 rows carry the contradiction state.")
rep('11_VISUAL_LIBRARY', 16, 19, [(TERM_LIM_EN_OLD, TERM_LIM_EN_NEW)], "Mirrors the 06 limitations (fact a).")
rep('11_VISUAL_LIBRARY', 16, 20, [(TERM_LIM_AR_OLD, TERM_LIM_AR_NEW)], "Arabic pair.")
full('11_VISUAL_LIBRARY', 16, 21, TERM_SUM_EN, "Identical to 06 VIS-POS-TERMINALS summary.")
full('11_VISUAL_LIBRARY', 16, 22, TERM_SUM_AR, "Arabic pair.")
full('11_VISUAL_LIBRARY', 17, 7, "Raw monthly POS-transaction totals. Between December 2025 (21,099) and January 2026 (24,026) the raw totals imply +13.87% growth, while the January source graphic displays +4.9%; between April 2026 (30,559) and May 2026 (36,201) the May source graphic displays +9.9%, which the totals do not give, and no change is derived for that month. In each case the published figures stay visible as a discrepancy within the source and none is corrected silently.",
     "The May 2026 contradiction in what the chart shows; no change derived.")
full('11_VISUAL_LIBRARY', 17, 8, "يعرض الإجماليات الشهرية الخام لعدد معاملات نقاط البيع. وبين ديسمبر 2025 (21,099) ويناير 2026 (24,026) تعطي الأرقام الخام نموًا نسبته +13.87%، بينما يعرض رسم المصدر لشهر يناير نسبة +4.9%؛ وبين أبريل 2026 (30,559) ومايو 2026 (36,201) يعرض رسم مصدر مايو نسبة +9.9% لا يعطيها الإجماليان، ولا يُشتق تغير لذلك الشهر. وتبقى الأرقام المنشورة ظاهرة في كل حالة بوصفها اختلافًا داخل المصدر، ولا يُصحَّح أي منها بصمت.",
     "Arabic pair.")
full('11_VISUAL_LIBRARY', 17, 18, "Raw monthly line with exact month/source detail and explicit contradiction annotations for Dec-2025→Jan-2026 (21,099→24,026 ≈ +13.87%; source graphic displays +4.9%) and Apr-2026→May-2026 (30,559→36,201; source graphic displays +9.9%; no change derived, because the source contradicts itself). No smoothing, interpolation or silent overwrite.",
     "Encoding contract gains the May 2026 annotation.")
rep('11_VISUAL_LIBRARY', 17, 19, [(TXN_LIM_EN_OLD, TXN_LIM_EN_NEW)], "Mirrors the 06 limitations (fact a).")
rep('11_VISUAL_LIBRARY', 17, 20, [(TXN_LIM_AR_OLD, TXN_LIM_AR_NEW)], "Arabic pair.")
full('11_VISUAL_LIBRARY', 17, 21, TXN_SUM_EN, "Identical to 06 VIS-POS-TRANSACTIONS summary.")
full('11_VISUAL_LIBRARY', 17, 22, TXN_SUM_AR, "Arabic pair.")
full('11_VISUAL_LIBRARY', 18, 21, VAL_SUM_EN, "Identical to 06 VIS-POS-VALUE summary.")
full('11_VISUAL_LIBRARY', 18, 22, VAL_SUM_AR, "Arabic pair.")
rep('11_VISUAL_LIBRARY', 34, 21, [("to 1,473 in January 2026.", "to 1,651 in June 2026.")], WHY_LATEST + " RV-CWR-004 text description; the lane itself is data-driven (regex on IND-0002) and moves to June once the rows exist.")
rep('11_VISUAL_LIBRARY', 34, 22, [("إلى 1,473 جهازًا في يناير 2026.", "إلى 1,651 جهازًا في يونيو 2026.")], "Arabic pair.")
rep('11_VISUAL_LIBRARY', 39, 21, [("POS figures for January 2026 within CBY-Aden's reporting scope (1,473 terminals; 24,026 transactions)",
     "POS figures for June 2026 within CBY-Aden's reporting scope (1,651 terminals; 27,504 transactions)")],
    WHY_LATEST + " RV-CWR-009 text description. APPLY ONLY WITH the contract/code change that moves the figure's pos_activity rows from OBS-00080/81 to the June 2026 rows (NOTES §3); the 'January 2026' unified-network statement in the same cell is a different source and stays.")
rep('11_VISUAL_LIBRARY', 39, 22, [("لشهر يناير 2026 (1,473 جهازًا و24,026 معاملة)", "لشهر يونيو 2026 (1,651 جهازًا و27,504 معاملات)")], "Arabic pair (same dependency).")

# 22_PROVIDERS_DATA · PAYCUR-001 ------------------------------------------------------------------------------
full('22_PROVIDERS_DATA', 124, 3, "CBY current payments pages rechecked on 2026-10-03; the Arabic page lists monthly POS objects March 2025 through June 2026; the English page still lists them only through January 2026",
     "Currentness control row (internal). Paired data cells c4/c5/c7/c8 listed in NOTES §3.")
full('22_PROVIDERS_DATA', 124, 6, "Use the controlled monthly POS sequence only through June 2026, with source-specific values/units and missingness preserved.",
     "Currentness control row (internal).")

# 33_ANALYTICS_MASTER -----------------------------------------------------------------------------------------
rep('33_ANALYTICS_MASTER', 8, 8, JUN, "DA-003 interpretation. APPLY ONLY WITH c4 'Mar-2025 to Jun-2026' and c5 = 1651/561 − 1 = 1.9429590017825311 (NOTES §3); otherwise leave the row as a dated Jan-2026 analytic.")
rep('33_ANALYTICS_MASTER', 8, 9, JUN_AR, "Arabic pair (same dependency).")
full('33_ANALYTICS_MASTER', 43, 4, "Reported POS terminals rose from 561 in Mar-2025 to 1,651 in Jun-2026, while monthly POS transactions rose, not steadily, from 8,015 to 27,504 (high of 36,201 in May-2026).",
     "INS-002 comparison (internal); depends on DA-003/DA-004 being moved to Jun-2026.")

# 34_EVIDENCE_PASSPORTS ---------------------------------------------------------------------------------------
full('34_EVIDENCE_PASSPORTS', 6, 9, "The September 2025 POS transaction-value observation in YER is missing; the September terminal count itself is present at 1,060. For December 2025→January 2026, terminal totals 1,357→1,473 imply approximately +8.55% while the January source graphic displays +11%; transaction totals 21,099→24,026 imply approximately +13.87% while the January source graphic displays +4.9%. For April 2026→May 2026, the May source graphic displays +2.4% for terminals and +9.9% for transactions, which the published totals (1,583→1,636; 30,559→36,201) do not give; because the source contradicts itself, no change is derived for that month (owner note, 3 October 2026). A smaller source-internal mismatch also appears in June 2025: 733→791 terminals imply approximately +7.91%, while the June graphic displays +7.6%. The February 2026 release displays +1.9% for terminals and −2.3% for value where the totals give about +1.97% and −2.38%; this is read as truncation, not contradiction. From the January 2026 release onward the YER value tile is labelled “billion” (مليار), while earlier releases state million YER; the printed month-on-month changes reconcile only in YER million, so the values are read as YER million. The February–June 2026 releases are listed on the Arabic payments page only. Keep raw totals and source-displayed percentages distinct rather than silently reconciling them.",
     "Passport (internal): the May 2026 contradictions shown and not resolved; the value-unit label; the Arabic-page-only provenance.")
rep('34_EVIDENCE_PASSPORTS', 6, 12, [("Show the January 2026 discrepancies prominently;", "Show the January 2026 and May 2026 discrepancies prominently;")],
    "Display requirement extended to the May 2026 discrepancies (they are of the same size class as January's for transactions).")

# ---- the 33 left unchanged ----------------------------------------------------------------------------------
LEAVE = {
 ('04_NAV_UX', 210, 2): "22 January 2026 exhibition participation count (e-wallets), not the POS series.",
 ('04_NAV_UX', 210, 3): "Arabic pair of the above.",
 ('06_EVIDENCE_OBJECTS', 79, 6): "VIS-PAYMENT-RAILS: 'January 2026' is the CBY-Aden statement on unified-network activity (22 January 2026 event), not POS.",
 ('06_EVIDENCE_OBJECTS', 79, 7): "Arabic pair of the above.",
 ('11_VISUAL_LIBRARY', 26, 21): "VIS-PAYMENT-RAILS accessible summary: same unified-network statement, not POS.",
 ('11_VISUAL_LIBRARY', 26, 22): "Arabic pair of the above.",
 ('19_PAYMENTS_DATA', 84, 12): "OBS-00080 January 2026 observation value (1473): historical data row, stays.",
 ('19_PAYMENTS_DATA', 84, 15): "OBS-00080 caveat on the January +11% contradiction: still true of the January release.",
 ('19_PAYMENTS_DATA', 85, 12): "OBS-00081 January 2026 observation value (24026): historical data row, stays.",
 ('19_PAYMENTS_DATA', 85, 15): "OBS-00081 caveat on the January +4.9% contradiction: still true.",
 ('19_PAYMENTS_DATA', 86, 12): "OBS-00082 January 2026 value (1262.0): historical data row, stays.",
 ('19_PAYMENTS_DATA', 86, 15): "OBS-00082 caveat (YER 1,262 million): still true. Optional: the caller may append the «مليار» label note here as data; not proposed as copy.",
 ('22_PROVIDERS_DATA', 118, 12): "WCR-004 reference period: 22 January 2026 event, not POS.",
 ('33_ANALYTICS_MASTER', 108, 4): "CTR-001: the Dec-2025→Jan-2026 terminal contradiction record; still true. The May 2026 contradiction needs a NEW CTR row (data), not an edit here.",
 ('33_ANALYTICS_MASTER', 109, 4): "CTR-002: the Dec-2025→Jan-2026 transaction contradiction record; still true. New CTR row needed for May 2026.",
}
for r in range(7, 13):
    LEAVE[('15_SOURCE_LIBRARY', r, 6)] = "Source title of a dated Governor's decision (January 2026), not POS."
    LEAVE[('15_SOURCE_LIBRARY', r, 12)] = "Arabic source title of the same decision."
LEAVE[('15_SOURCE_LIBRARY', 33, 6)] = "Source title of the January 2026 POS release itself; it stays a source (still cited for the January observations)."
LEAVE[('15_SOURCE_LIBRARY', 33, 12)] = "Arabic title of the January 2026 POS release."
LEAVE[('15_SOURCE_LIBRARY', 63, 6)] = "Source title of the 22 January 2026 digital-payments exhibition, not POS."
LEAVE[('15_SOURCE_LIBRARY', 63, 12)] = "Arabic pair."
LEAVE[('15_SOURCE_LIBRARY', 106, 6)] = "IMF D4D-II progress report dated January 2026, not POS."
LEAVE[('15_SOURCE_LIBRARY', 106, 12)] = "Arabic pair."

# ---- extras (outside the 148-cell dump) ---------------------------------------------------------------------
EXTRA = {}
def xfull(sheet, r, c, text, reason): EXTRA[(sheet, r, c)] = (F, text, reason)
def xrep(sheet, r, c, pairs, reason): EXTRA[(sheet, r, c)] = (R, pairs, reason)
P = [("Jan-2026", "Jun-2026")]
xrep('06_EVIDENCE_OBJECTS', 6, 10, P, "CLM-003 period_en, rendered publicly ('When was it measured or observed? Mar-2025–Jan-2026'); English pair of c11, which is in the dump.")
xrep('06_EVIDENCE_OBJECTS', 66, 10, P, "VIS-POS-TERMINALS period_en; pair of c11.")
xrep('06_EVIDENCE_OBJECTS', 67, 10, P, "VIS-POS-TRANSACTIONS period_en; pair of c11.")
xrep('06_EVIDENCE_OBJECTS', 68, 10, P, "VIS-POS-VALUE period_en; pair of c11.")
xfull('06_EVIDENCE_OBJECTS', 22, 8, "The most recent month covered by a monthly point-of-sale (POS) release on the Arabic and English payments pages of the Central Bank of Yemen – Aden (CBY-Aden), as checked on 3 October 2026.",
      "CLM-017 definition still says 'as checked on 26 September 2026'; it must move with the rest of the record.")
xfull('06_EVIDENCE_OBJECTS', 22, 9, "أحدث شهر يغطيه إصدار شهري لنقاط البيع في صفحتي المدفوعات بالعربية وبالإنجليزية لدى البنك المركزي اليمني – عدن، كما اطُّلع عليهما في 3 أكتوبر 2026.",
      "Arabic pair.")
xrep('06_EVIDENCE_OBJECTS', 68, 14, [("not adjusted for inflation or exchange-rate changes. No value",
      "not adjusted for inflation or exchange-rate changes. From the January 2026 release onward the value is labelled “billion”, while the earlier releases state million YER; the month-on-month changes the releases print reconcile only when the values are read in millions, so this resource continues to read them as YER million. No value")],
     "Fact (b), the unit disclosure, in the VIS-POS-VALUE method (rendered as the value chart's note on /payments/), where the normalisation to millions is already explained.")
xrep('06_EVIDENCE_OBJECTS', 68, 15, [("غير معدلة لأثر التضخم أو تغيرات سعر الصرف. ولا تتوفر",
      "غير معدلة لأثر التضخم أو تغيرات سعر الصرف. وابتداءً من إصدار يناير 2026 تُدرج القيمة تحت وحدة «مليار»، بينما تذكر الإصدارات السابقة أنها بملايين الريالات؛ ولا تتسق نسب التغير الشهرية التي تطبعها الإصدارات إلا إذا قُرئت القيم بالملايين، لذلك يواصل هذا المورد قراءتها بملايين الريالات. ولا تتوفر")],
     "Arabic pair.")
xrep('11_VISUAL_LIBRARY', 16, 11, P, "source_period (internal/caption).")
xrep('11_VISUAL_LIBRARY', 16, 17, P, "period: printed in the chart caption ('Mar-2025–Jan-2026 monthly · …').")
xrep('11_VISUAL_LIBRARY', 16, 13, [("2026-01", "2026-06")], "freshness_profile.")
xrep('11_VISUAL_LIBRARY', 17, 11, P, "source_period.")
xrep('11_VISUAL_LIBRARY', 17, 17, P, "period (chart caption).")
xrep('11_VISUAL_LIBRARY', 17, 13, [("2026-01", "2026-06")], "freshness_profile.")
xrep('11_VISUAL_LIBRARY', 18, 11, P, "source_period.")
xrep('11_VISUAL_LIBRARY', 18, 17, P, "period (chart caption).")
xrep('11_VISUAL_LIBRARY', 18, 13, [("2026-01", "2026-06")], "freshness_profile.")
xrep('11_VISUAL_LIBRARY', 17, 9, [("making the January source-arithmetic discrepancy inspectable", "making the January and May 2026 source-arithmetic discrepancies inspectable")],
     "decision_value_en names only the January discrepancy; fact (a).")
xrep('11_VISUAL_LIBRARY', 17, 10, [("مع جعل الاختلاف الحسابي في مصدر يناير قابلًا للفحص", "مع جعل الاختلافين الحسابيين في مصدري يناير ومايو 2026 قابلين للفحص")], "Arabic pair.")
xfull('15_SOURCE_LIBRARY', 70, 6, "Monthly Point of Sale Transactions: publication pages, Arabic and English (as checked on 3 October 2026)",
      "Publication-page source cited by CLM-017: check date and the two pages. Pair with retrieval_date 2026-10-03 and the Arabic URL https://cby-ye.com/pages/33 (NOTES §3).")
xfull('15_SOURCE_LIBRARY', 70, 12, "معاملات نقاط البيع الشهرية: صفحتا الإصدارات بالعربية وبالإنجليزية (كما اطُّلع عليهما في 3 أكتوبر 2026)", "Arabic pair.")
xrep('34_EVIDENCE_PASSPORTS', 6, 6, P, "Passport reference period (internal).")
xrep('33_ANALYTICS_MASTER', 124, 4, [("monthly POS reaches Jan-2026", "monthly POS reaches Jun-2026 (Arabic page; English page Jan-2026)")], "CON-036 freshness note (internal).")


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def plan():
    """[(sheet, row, col, kind, payload, reason, in_dump)] in sheet/row/col order."""
    out = [(k[0], k[1], k[2], v[0], v[1], v[2], True) for k, v in SPEC.items()]
    out += [(k[0], k[1], k[2], v[0], v[1], v[2], False) for k, v in EXTRA.items()]
    return sorted(out, key=lambda x: (x[0], x[1], x[2]))


def apply(s, finding):
    """Apply every SPEC/EXTRA entry through the session (exact-value guarded). Run before any row insertion."""
    n = 0
    for sheet, r, c, kind, payload, reason, _ in plan():
        cur = s.ed.get_value(sheet, r, c)
        if not isinstance(cur, str):
            raise ValueError(f"{sheet}!r{r}c{c} is not text")
        if kind == R:
            for old, new in payload:
                s.replace(finding, sheet, r, c, old, new, f"POS r{r}c{c}")
        else:
            if _sha(cur) != OLD_SHA.get((sheet, r, c)):
                raise ValueError(f"{sheet}!r{r}c{c} holds text other than the one this rewrite was drafted against: {cur[:90]!r}")
            s.set(finding, sheet, r, c, payload, cur, f"POS r{r}c{c}")
        n += 1
    return n


# SHA-256 prefix of the text each full rewrite was drafted against (Master 5c0688d3d29d, 3 October 2026)
OLD_SHA = {
 ('02_SITE_MAP', 27, 7): 'ffa6888c6ec8ef37',
 ('02_SITE_MAP', 27, 8): '359024b5e56774f0',
 ('03_PAGE_SECTIONS', 177, 4): '723759efd6c99b79',
 ('03_PAGE_SECTIONS', 177, 5): '26a42d8089a36d45',
 ('03_PAGE_SECTIONS', 178, 6): '7bd4fa73da89abf8',
 ('03_PAGE_SECTIONS', 178, 7): '81e8d416fd26c3ae',
 ('06_EVIDENCE_OBJECTS', 6, 6): 'e582747dab4e118e',
 ('06_EVIDENCE_OBJECTS', 6, 7): 'def3316bb92c3e9a',
 ('06_EVIDENCE_OBJECTS', 6, 18): 'dd36d9d7e4e58a7f',
 ('06_EVIDENCE_OBJECTS', 6, 19): '2a894daca6676335',
 ('06_EVIDENCE_OBJECTS', 22, 4): '25bd5458b4f4d1f7',
 ('06_EVIDENCE_OBJECTS', 22, 5): '9ea90a3e6a6baab3',
 ('06_EVIDENCE_OBJECTS', 22, 6): '8016ef3a0734f74d',
 ('06_EVIDENCE_OBJECTS', 22, 7): '6a3abeb10d61706c',
 ('06_EVIDENCE_OBJECTS', 22, 8): '1091e1c0fa63332f',
 ('06_EVIDENCE_OBJECTS', 22, 9): 'a9ea42c752dffbf1',
 ('06_EVIDENCE_OBJECTS', 22, 10): '699cdb4d08e99c83',
 ('06_EVIDENCE_OBJECTS', 22, 11): '47892f70588a649f',
 ('06_EVIDENCE_OBJECTS', 22, 14): '1bbafb5cbb585bce',
 ('06_EVIDENCE_OBJECTS', 22, 15): 'e7f1bddd5633cc0d',
 ('06_EVIDENCE_OBJECTS', 22, 16): 'bf155f769b668ebe',
 ('06_EVIDENCE_OBJECTS', 22, 17): '1b11333f86ff4669',
 ('06_EVIDENCE_OBJECTS', 22, 18): '4b51c0c790c2f1ed',
 ('06_EVIDENCE_OBJECTS', 22, 19): '326b3360006a9950',
 ('06_EVIDENCE_OBJECTS', 66, 6): '4b3ad1ae2be363a1',
 ('06_EVIDENCE_OBJECTS', 66, 7): '7f33b1fefc61a688',
 ('06_EVIDENCE_OBJECTS', 66, 18): 'dd36d9d7e4e58a7f',
 ('06_EVIDENCE_OBJECTS', 66, 19): '2a894daca6676335',
 ('06_EVIDENCE_OBJECTS', 67, 6): 'f19db0bcdc5475ac',
 ('06_EVIDENCE_OBJECTS', 67, 7): 'f0ecb4c8dbd865e0',
 ('06_EVIDENCE_OBJECTS', 67, 18): 'dd36d9d7e4e58a7f',
 ('06_EVIDENCE_OBJECTS', 67, 19): '2a894daca6676335',
 ('06_EVIDENCE_OBJECTS', 68, 6): '3bdda95e59d0e00b',
 ('06_EVIDENCE_OBJECTS', 68, 7): '0a1dcccc3e6f9109',
 ('06_EVIDENCE_OBJECTS', 68, 18): '588d072b61a2df91',
 ('06_EVIDENCE_OBJECTS', 68, 19): '0c0565bb64d92776',
 ('11_VISUAL_LIBRARY', 16, 7): '677c251753dcd902',
 ('11_VISUAL_LIBRARY', 16, 8): '8b6728ff807ef718',
 ('11_VISUAL_LIBRARY', 16, 18): 'bd0394c58bdb6df1',
 ('11_VISUAL_LIBRARY', 16, 21): '4b3ad1ae2be363a1',
 ('11_VISUAL_LIBRARY', 16, 22): '7f33b1fefc61a688',
 ('11_VISUAL_LIBRARY', 17, 7): 'c1cf793c0a60f553',
 ('11_VISUAL_LIBRARY', 17, 8): '8d0ee2bbc479d5d5',
 ('11_VISUAL_LIBRARY', 17, 18): '49c8c7e7c0a22902',
 ('11_VISUAL_LIBRARY', 17, 21): 'f19db0bcdc5475ac',
 ('11_VISUAL_LIBRARY', 17, 22): 'f0ecb4c8dbd865e0',
 ('11_VISUAL_LIBRARY', 18, 21): '3bdda95e59d0e00b',
 ('11_VISUAL_LIBRARY', 18, 22): '0a1dcccc3e6f9109',
 ('15_SOURCE_LIBRARY', 70, 6): '9cbce8280ccff485',
 ('15_SOURCE_LIBRARY', 70, 12): 'c27225399ab44eb7',
 ('22_PROVIDERS_DATA', 124, 3): '765e135bdae3e1d8',
 ('22_PROVIDERS_DATA', 124, 6): '7ccbf359654efe23',
 ('33_ANALYTICS_MASTER', 43, 4): '268c2eae83bfad28',
 ('34_EVIDENCE_PASSPORTS', 6, 9): 'f7ca234f3b336a51',
}
