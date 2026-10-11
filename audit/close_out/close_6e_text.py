# -*- coding: utf-8 -*-
"""CLOSE-6E texts (Stage A final instruction v5, 11 October 2026, section 5). Each item is checked against the reads kept in
audit/close_out/v5_reads/ (V3 the CBY-Aden credit-information pages; V4 World Bank FSD 2024 Annex III and Doing Business
2020; V5 UNICEF, the Cash Consortium of Yemen studies, SMEPS, the IFAD evaluation and the RPW quote-level dataset). Where
a read differs from the instruction's draft wording, the read governs and the difference is recorded in DISPOSITION_6E.md."""
from collections import OrderedDict

TODAY = "2026-10-11"
V4 = "; read 11 October 2026 (audit/close_out/v5_reads/V4_imf_wb.md)"
V5 = "; read 11 October 2026 (audit/close_out/v5_reads/V5_cash_smeps_ifad_rpw.md)"
V3 = "; read 11 October 2026 (audit/close_out/v5_reads/V3_cby_legal.md)"

FSD = "SRC-WB-FSD-2024-001"
SMEPS = "SRC-SMEPS-AR2024-2025"
UNI10, UNI12 = "SRC-UNICEF-UCT-2024-10", "SRC-UNICEF-UCT-2024-12"
PRESS, SAM, CDUR = "SRC-CCY-PRESSURE-2026", "SRC-CCY-SAM-2024", "SRC-CCY-CASH-DURATION-2026"
RPWUS = "SRC-WB-RPW-US-YEM-2025Q3-001"
DB20 = "SRC-WB-DB2020-YEM-001"
IFADS = "SRC-IFAD-CPE-YEM-2011"
IFADR = "IFAD-CPE-YEM-2011-RF"
CRI149, CRI150, NEWS963 = "SRC-CBY-CRI-149", "SRC-CBY-CRI-150", "SRC-CBY-NEWS-963"

RPW_XLSX = "https://datacatalogfiles.worldbank.org/ddh-published/0037898/DR0095523/rpw_dataset_2011_2025_q3.xlsx"
DB20_URL = "https://www.doingbusiness.org/content/dam/doingBusiness/country/y/yemen/YEM.pdf"
DB20_STMT = "https://www.worldbank.org/en/news/statement/2021/09/16/world-bank-group-to-discontinue-doing-business-report"
IFAD_URL = "https://webapps.ifad.org/members/ec/69/docs/EC-2011-69-W-P-4-Rev-1.pdf"
UNI10_URL = "https://www.unicef.org/yemen/press-releases/143-million-vulnerable-families-supported-cash-assistance-across-yemen"
UNI12_URL = ("https://www.unicef.org/yemen/press-releases/"
             "unicef-and-partners-launch-19th-payment-cycle-current-unconditional-cash-transfer")


def vs(t, k, s, src=None, loc=None):
    e = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        e["src"] = src
    if loc:
        e["loc"] = loc
    return e


# ==================================================================================================================== 6C-1(a)
# Informal firms, extending CLM-062. The figure's title is "Main Sources of Financing for the Business" (not sources of
# debt) and its base is the 217 firms (V4 B2); 1.31% is Figure 110, the formal-enterprise section, with no n printed, so
# the instruction's "among 328 formal firms" is not written (the record already says the base is not held).
INF_OLD = ("Among the 217 informal firms surveyed, 80.18% had no bank account; that sample was drawn from activity and location "
           "lists rather than a national register.",
           "أما المنشآت غير الرسمية التي شملها المسح، وعددها 217 منشأة، فلم يكن لدى 80.18% منها حساب مصرفي، وقد سُحبت عينتها من "
           "قوائم للأنشطة والمواقع لا من سجل وطني.")
INF_NEW = ("Among the 217 informal firms surveyed, 80.18% had no bank account, and 49.8% of owners reported a loan or debt related "
           "to the business. Asked for the main sources of financing for the business, 54.38% named savings, 47.00% relatives and "
           "22.12% money lenders; 1.84% named a microfinance institution and 2.76% buying goods on credit. The shares add to more "
           "than 100%, so some firms gave more than one answer, and they describe financing in general, not the sources of the "
           "debts reported. That sample was drawn from activity and location lists rather than a national register and does not "
           "represent informal firms. Its shares are not comparable with formal firms' 1.31%, which is supplier credit's average "
           "share of working capital.",
           "أما المنشآت غير الرسمية التي شملها المسح، وعددها 217 منشأة، فلم يكن لدى 80.18% منها حساب مصرفي، وأفاد 49.8% من "
           "أصحابها بأن عليهم قرضًا أو دينًا مرتبطًا بالنشاط. وعند سؤالها عن المصادر الرئيسية لتمويل النشاط، ذكر 54.38% منها "
           "المدخرات، و47.00% الأقارب، و22.12% المقرضين غير الرسميين؛ وذكر 1.84% مؤسسةً للتمويل الأصغر، و2.76% شراء البضائع "
           "بالدَّين. ومجموع هذه النسب يتجاوز 100%، أي إن بعض المنشآت ذكرت أكثر من مصدر، وهي تصف التمويل عمومًا لا مصادر الديون "
           "المذكورة. وقد سُحبت هذه العينة من قوائم للأنشطة والمواقع لا من سجل وطني، ولا تمثل المنشآت غير الرسمية. ولا تُقارن "
           "نسبها بنسبة 1.31% لدى المنشآت الرسمية، وهي متوسط حصة ائتمان الموردين من رأس مالها العامل.")
INF_DEF = (("financial intermediaries used, and informal firms' account holding.",
            "financial intermediaries used, and informal firms' account holding, business debt and main sources of financing."),
           ("والوسطاء الماليون المستخدمون، وامتلاك المنشآت غير الرسمية للحسابات.",
            "والوسطاء الماليون المستخدمون، وامتلاك المنشآت غير الرسمية للحسابات وديونها المرتبطة بالنشاط ومصادر تمويلها الرئيسية."))
INF_METHOD = (("and informal firms' account holding, Figure 114 (p. 151), whose base of 217 informal firms is stated on pp. 139 and "
               "141.",
               "and informal firms' account holding, business-related loan or debt and main sources of financing, Figures 114 to "
               "116 (p. 151), whose base of 217 informal firms is stated on pp. 139 and 141 (the figures print no base; each value "
               "is a whole number of firms out of 217, CauseWay's check)."),
              ("وامتلاك المنشآت غير الرسمية للحسابات، الشكل 114 (ص 151)، وقاعدته 217 منشأة غير رسمية كما ترد في الصفحتين 139 و141.",
               "وامتلاك المنشآت غير الرسمية للحسابات وقروضها أو ديونها المرتبطة بالنشاط ومصادر تمويلها الرئيسية، الأشكال من 114 إلى "
               "116 (ص 151)، وقاعدتها 217 منشأة غير رسمية كما ترد في الصفحتين 139 و141 (لا تطبع الأشكال قاعدتها، وكل قيمة فيها عدد "
               "صحيح من المنشآت من أصل 217، بحسب تحقق CauseWay)."))
INF_LIM = (("and multiple-response percentages are not market shares.",
            "and multiple-response percentages are not market shares. The report's main text (Figure 91, p. 120) gives smaller "
            "percentages for the informal firms' sources of financing; they match the Annex III values re-expressed as shares of "
            "all answers given (CauseWay's check), and this record uses the Annex III values, whose base is the firm."),
           ("ونسب الأسئلة متعددة الإجابات ليست حصصًا سوقية.",
            "ونسب الأسئلة متعددة الإجابات ليست حصصًا سوقية. ويعطي المتن الرئيسي للتقرير (الشكل 91، ص 120) نسبًا أصغر لمصادر تمويل "
            "المنشآت غير الرسمية؛ وهي تطابق قيم الملحق الثالث بعد إعادة حسابها حصصًا من مجموع الإجابات (بحسب تحقق CauseWay)، "
            "ويستخدم هذا السجل قيم الملحق الثالث، وقاعدتها المنشأة."))
F116 = "Annex III, Figure 116 'Main Sources of Financing for the Business', p.151"
INF_VS = [
    vs("49.8%", "v", "READ", FSD, "Annex III, Figure 115 'Owner has Loan or Debt Related to Business', p.151" + V4),
    vs("54.38%", "v", "READ", FSD, F116 + " (Savings)" + V4),
    vs("47.00%", "v", "READ", FSD, F116 + " (Relatives)" + V4),
    vs("22.12%", "v", "READ", FSD, F116 + " (Money lenders)" + V4),
    vs("1.84%", "v", "READ", FSD, F116 + " (Microfinance institute)" + V4),
    vs("2.76%", "v", "READ", FSD, F116 + " (Buying goods on credit)" + V4),
    vs("100%", "v", "TRIVIAL"), vs("116", "v", "TRIVIAL"), vs("91", "v", "TRIVIAL"),
    vs("120", "v", "LOCATOR"),
]

# ==================================================================================================================== 6C-1(b)
# The cover reads "2024 SMEPS EXECUTIVE REPORT" (V5 E); the type rows partition the total (7,257 + 960 = 8,217).
SMEPS_OLD = ("disbursed USD 22,865,322.", "وصرفت 22,865,322 دولارًا.")
SMEPS_NEW = ("disbursed USD 22,865,322. In its key-indicator table, most of these 8,217 MSMEs (7,257) were smallholder producers "
             "and micro supply-chain enablers.",
             "وصرفت 22,865,322 دولارًا. وبحسب جدول المؤشرات الرئيسية في تقريرها، كان معظم هذه المنشآت البالغ عددها 8,217 منشأة "
             "(7,257 منشأة) من صغار المنتجين والمنشآت الأصغر المُمكِّنة لسلاسل الإمداد.")
SMEPS_VS = [vs("7,257", "v", "READ", SMEPS,
               "SMEPS 2024 Executive Report (the cover's title; catalogued as the SMEPS Annual Report 2024), Key indicators table, "
               "printed p.9 (PDF p.5), row 'Smallholder producers & micro supply chain enablers', 2024 column (the 'SMEs and BAs' "
               "row gives 960; 7,257 + 960 = 8,217)" + V5)]

# ==================================================================================================================== 6C-2
# (a) UNICEF: 1.43 million is the cycle's announced reach ("received" and "will be disbursed" in one release), not a count
# of confirmed payments; US$62.5 million is planned and is not used; the 19th cycle starts at fixed payment sites (V5 A).
UCT = ("The pilot sat inside a much larger programme. UNICEF, which implemented the World Bank-funded unconditional cash transfer "
       "programme with the Social Fund for Development, announced in October 2024 that more than 1.43 million families were "
       "receiving assistance in its 18th payment cycle, which ran to mid-October, at payment sites, through mobile teams and home "
       "outreach, and in an e-wallet pilot; the figure is the cycle's announced reach, not a count of confirmed payments. In "
       "December 2024 it announced that the 19th cycle, starting on 11 December 2024 at fixed payment sites, marked the end of the "
       "programme in its then-current form. The pilot's 45,460 recipients and the programme's 1.43 million families are different "
       "counts, and one is not a share of the other; a family reached by a payment cycle does not thereby hold an account.",
       "وكانت التجربة جزءًا من برنامج أكبر بكثير. فقد أعلنت اليونيسف، التي نفّذت برنامج التحويلات النقدية غير المشروطة الممول من "
       "البنك الدولي بالشراكة مع الصندوق الاجتماعي للتنمية، في أكتوبر 2024 أن أكثر من 1.43 مليون أسرة تتلقى المساعدة في دورة الدفع "
       "18، التي امتدت حتى منتصف أكتوبر، في مواقع الصرف، وعبر فرق متنقلة وخدمات الوصول إلى المنازل، وضمن تجربة للمحفظة "
       "الإلكترونية؛ وهذا الرقم هو النطاق المعلن للدورة، لا عدد الدفعات المؤكدة. وفي ديسمبر 2024 أعلنت أن دورة الدفع 19، التي تبدأ "
       "في 11 ديسمبر 2024 في مواقع الصرف الثابتة، تمثل نهاية البرنامج بصيغته القائمة آنذاك. والمستفيدون من التجربة، وعددهم 45,460 "
       "مستفيدًا، والأسر التي يشملها البرنامج، وعددها 1.43 مليون أسرة، عددان مختلفان، وليس أحدهما نسبة من الآخر؛ ولا يعني وصول "
       "دورة الدفع إلى أسرة أن لديها حسابًا.")

# (b) Cash-out at agents (Pressure, printed p.7 = PDF p.8; fn 31 "KII with MPCA program manager April 2026", fn 32 "ibid.").
# The source has no year on "Eid al-Adha", says "denominations", not "notes", and the voucher and denomination sentences
# carry no footnote of their own (V5 B).
_CASH_BODY = ("most cash assistance was disbursed through microfinance banks as vouchers that recipients exchange at local agents "
              "of financial service providers and, citing one interview with a cash-programme manager in April 2026, that during "
              "the Ramadan and Eid holiday period agents often lacked enough cash, with waits of four to five hours. It reports "
              "that funds were released only in denominations of YER 100 and 200 and, citing the same interview, that an e-wallet "
              "pilot disbursed funds without problems or delays. These are reported observations, some of them from a single "
              "interview; the report names neither the programme nor the areas concerned, and the e-wallet result concerns "
              "disbursement, not whether recipients could then obtain cash, which the report itself calls unclear.")
_CASH_BODY_AR = ("معظم المساعدات النقدية صُرفت عبر بنوك التمويل الأصغر في صورة قسائم يستبدلها المستفيدون لدى وكلاء محليين لمقدمي "
                 "الخدمات المالية، وينقل عن مقابلة واحدة مع مدير لبرنامج نقدي في أبريل 2026 أن الوكلاء كثيرًا ما افتقروا خلال فترة "
                 "عطلة رمضان والعيد إلى ما يكفي من النقد، فامتد الانتظار أربع ساعات إلى خمس. ويذكر أن الأموال صُرفت بفئتي 100 و200 "
                 "ريال فقط، وينقل عن المقابلة نفسها أن تجربة للمحفظة الإلكترونية صرفت الأموال دون مشكلات أو تأخير. وهذه ملاحظات "
                 "مُبلَّغ عنها، بعضها من مقابلة واحدة؛ ولا يسمّي التقرير البرنامج ولا المناطق المعنية، ونتيجة المحفظة الإلكترونية "
                 "تخص صرف الأموال، لا قدرة المستفيدين بعد ذلك على الحصول على النقد، وهي مسألة يصفها التقرير نفسه بأنها غير واضحة.")
CASH_READING = ("The same May 2026 report adds an observation on cash-out. It says that " + _CASH_BODY,
                "ويضيف التقرير نفسه الصادر في مايو 2026 ملاحظة عن السحب النقدي، إذ يذكر أن " + _CASH_BODY_AR)
CASH_RECORD = ("On cash-out, a Cash Consortium of Yemen report of May 2026 says that " + _CASH_BODY,
               "وعن السحب النقدي، يذكر تقرير لتحالف النقد في اليمن صدر في مايو 2026 أن " + _CASH_BODY_AR)

# (c) Debt clearing. SAM: January 2024 survey, 291 + 209 interviews, 40% "debt repayment" among regular expenditures in the 30
# days before the interview (printed pp.15-16); 11 of 21 and 10 of 21 business owners (printed p.31); published November
# 2024 (host listing). Cash Duration: Ja'ar sub-district only, endline November 2025, n = 45 and 107, single answer, 60% and
# 40% (printed pp.6-7). The instruction's "areas administered from Aden" is replaced by the studies' own sub-districts.
DEBT = ("Two Cash Consortium of Yemen studies of cash-assistance recipients, in sub-districts that the studies place in areas "
        "under the internationally recognized government, point to debt repayment as an early use of transfers. In a survey of "
        "recipient households in Ad-Dali and Ja’ar in January 2024 (291 and 209 interviews), published in November 2024, 40% "
        "reported debt repayment among their regular expenses in the 30 days before the interview. In a 2026 study comparing three "
        "and six monthly transfers in Ja’ar, “debts are paid off” was one of the two most common answers to which part of the "
        "household economy improved most at the endline in November 2025 (one answer allowed): 60% of the 45 households that "
        "received six transfers gave it, and 40% of the 107 that received three. In the 2024 study, 11 of 21 business owners who "
        "answered in Ad-Dali and 10 of 21 in Ja’ar said that fewer customers bought on credit when cash assistance was "
        "distributed. These are local samples of aid recipients, not national estimates, and the business owners' answers are "
        "counts of interviews, not credit volumes. They are one reason why immediate cash-out is not, by itself, a sign that a "
        "transfer failed.",
        "وتشير دراستان لتحالف النقد في اليمن عن متلقي المساعدات النقدية، في مديريات فرعية تضعها الدراستان في المناطق الخاضعة "
        "للحكومة المعترف بها دوليًا، إلى سداد الديون بوصفه استخدامًا مبكرًا للتحويلات. ففي مسح لأسر متلقية في الضالع وجعار أُجري "
        "في يناير 2024 (291 و209 مقابلات) ونُشر في نوفمبر 2024، أفادت 40% من الأسر بأن سداد الديون من نفقاتها المنتظمة خلال 30 "
        "يومًا سبقت المقابلة. وفي دراسة صدرت في 2026 قارنت بين ثلاثة تحويلات شهرية وستة في جعار، كانت «سُدّدت الديون» إحدى "
        "الإجابتين الأكثر شيوعًا عن سؤال أيّ جوانب اقتصاد الأسرة تحسّن أكثر من غيره في التقييم الختامي في نوفمبر 2025 (مع السماح "
        "بإجابة واحدة): فقد اختارتها 60% من الأسر الـ45 التي تلقت ستة تحويلات، و40% من الأسر الـ107 التي تلقت ثلاثة. وفي دراسة "
        "2024، قال 11 من أصل 21 من أصحاب الأعمال الذين أجابوا في الضالع، و10 من أصل 21 في جعار، إن عدد الزبائن الذين يشترون "
        "بالدَّين انخفض عند توزيع المساعدات النقدية. وهذه عينات محلية من متلقي المساعدات، لا تقديرات وطنية، وإجابات أصحاب "
        "الأعمال أعداد مقابلات لا أحجام ائتمان. وهي من أسباب ألا يُعدّ السحب النقدي الفوري في حد ذاته دليلًا على فشل التحويل.")

U10L = "UNICEF Yemen press release, 2 October 2024"
U12L = "UNICEF Yemen press release, 7 December 2024"
PRL = "Yemen Under Pressure (May 2026), printed p.7 (PDF p.8)"
SAML = "The Multiplier Effect of MPCA (CCY, 2024)"
CDL = "The More the Merrier? (CCY, 2026)"
CLM045_VS = [
    vs("1.43", "v", "READ", UNI10, U10L + ", paragraph 1 ('More than 1.43 million families received cash assistance') and "
       "paragraph 2 ('over 1.43 million families'); planned, not confirmed, payments ('will be disbursed')" + V5),
    vs("1.43 million", "v", "READ", UNI12, U12L + ", paragraph 1: 'over 1.43 million vulnerable families will receive cash "
       "assistance'" + V5),
    vs("18th", "v", "READ", UNI10, U10L + ": 'The current 18th payment cycle'; 'through mid-October'" + V5),
    vs("19th", "v", "READ", UNI12, U12L + ": 'launching the 19th payment cycle'; 'The 19th payment cycle marks the end of the "
       "current UCT program'" + V5),
    vs("11 December 2024", "d", "READ", UNI12, U12L + ": 'Starting 11 December 2024 in the fixed payment sites'" + V5),
    vs("December 2024", "d", "READ", UNI12, U12L + ", dated 07 December 2024" + V5),
    vs("October 2024", "d", "READ", UNI10, U10L + ", dated 02 October 2024" + V5),
    vs("April 2026", "d", "READ", PRESS, PRL + ", footnote 31: 'KII with MPCA program manager April 2026'; footnote 32 "
       "'ibid.'" + V5),
    vs("May 2026", "d", "READ", PRESS, "cover: 'May 2026'" + V5),
    vs("100", "v", "READ", PRESS, PRL + ": 'releasing funds only in denominations of YER 100 and 200'" + V5),
    vs("200", "v", "READ", PRESS, PRL + ": 'releasing funds only in denominations of YER 100 and 200'" + V5),
    vs("January 2024", "d", "READ", SAM, SAML + ", printed p.7 (PDF p.8): 'In January 2024, the CCY conducted a HH survey'" + V5),
    vs("November 2024", "d", "READ", SAM, "host path calpnetwork.org/wp-content/uploads/2024/11/ (the report prints no date)" + V5),
    vs("291", "v", "READ", SAM, SAML + ", printed pp.7-8: '291 HHs in Ad Dali sub-district and 209 HH in Ja'ar sub-district'" + V5),
    vs("209", "v", "READ", SAM, SAML + ", printed pp.7-8" + V5),
    vs("40%", "v", "READ", SAM, SAML + ", printed p.15 (PDF p.16): 'debt repayment (40%)'; Table 3, printed p.16, '% of HH "
       "reporting regular expenditure category', 30 days prior to data collection" + V5),
    vs("30", "v", "READ", SAM, SAML + ", Table 3, printed p.16: '30 days prior to data collection'" + V5),
    vs("11", "v", "READ", SAM, SAML + ", printed p.31 (PDF p.32): 'In Ad-Dali, 11 of 21 (52%) of interviewed business owners "
       "reported that the number of customers buying goods or services on credit decreased'" + V5),
    vs("21", "v", "READ", SAM, SAML + ", printed p.31 (PDF p.32), footnote 80 (four 'don't know' answers in Ad-Dali)" + V5),
    vs("10", "v", "READ", SAM, SAML + ", printed p.31 (PDF p.32): '10 of 21 (48%) interviewed business owners in Ja'ar'" + V5),
    vs("60%", "v", "READ", CDUR, CDL + ", Figure 1, printed p.6 (PDF p.7): 'Debts are paid off' 60% (six-month) and 40% "
       "(three-month), one answer only; text printed p.7" + V5),
    vs("40% of the 107", "v", "READ", CDUR, CDL + ", Figure 1, printed p.6: 'Debts are paid off', three-month recipients 40%" + V5),
    vs("45", "v", "READ", CDUR, CDL + ", printed p.6: '45 HHs that received six-month distributions and 107 HHs that received "
       "three-month distributions'" + V5),
    vs("107", "v", "READ", CDUR, CDL + ", printed p.6" + V5),
    vs("November 2025", "d", "READ", CDUR, CDL + ", printed p.6: 'endline assessments conducted in November 2025'" + V5),
]

# (d) /people/ section 6, bound to CLM-045 (already on /people/)
PEOPLE_S6 = (("and each percentage applies to the all-adult base used by its question.",
              "and each percentage applies to the all-adult base used by its question. The borrowing sources shown here are family "
              "or friends and financial institutions. Shop credit, which local studies of cash-assistance recipients observe, is "
              "not among them."),
             ("وكل نسبة تنطبق على قاعدة جميع البالغين المستخدمة في سؤالها.",
              "وكل نسبة تنطبق على قاعدة جميع البالغين المستخدمة في سؤالها. ومصادر الاقتراض المعروضة هنا هي الأسرة أو الأصدقاء "
              "والمؤسسات المالية؛ أما الشراء بالدَّين من المتاجر، الذي ترصده دراسات محلية عن متلقي المساعدات النقدية، فليس من "
              "بينها."))

# (e) Measurement Agenda, through bindings. Pressure was read for cash access only (V5 B; addendum R4): no shop or supplier
# credit statement was found in it, so MA-001 cites SAM only. "12% ... as of 2026" and the ISP figures are not used.
MA_ADD = OrderedDict([
    ("MA-001", ((" For shop or supplier credit there are local observations, not a baseline: in a 2024 Cash Consortium of Yemen "
                 "study, 11 of 21 business owners who answered in Ad-Dali and 10 of 21 in Ja’ar said that fewer customers bought on "
                 "credit when cash assistance was distributed."),
                (" أما ائتمان المتاجر أو الموردين فلا تتوافر عنه إلا ملاحظات محلية لا خط أساس: ففي دراسة لتحالف النقد في اليمن صدرت "
                 "في 2024، قال 11 من أصل 21 من أصحاب الأعمال الذين أجابوا في الضالع، و10 من أصل 21 في جعار، إن عدد الزبائن الذين "
                 "يشترون بالدَّين انخفض عند توزيع المساعدات النقدية."),
                ["CLM-045"], [SAM])),
    ("MA-004", ((" For collateral and terms the evidence is historical: an independent evaluation of IFAD's rural credit in Yemen "
                 "from 1993 to 2010 reports collateral requirements, high transaction costs and long approval procedures among the "
                 "reasons poor households were said to avoid the partner bank's credit, in specific project areas before the "
                 "conflict."),
                (" أما الضمانات والشروط فأدلتها تاريخية: إذ يورد تقييم مستقل للائتمان الريفي الذي موّله الصندوق الدولي للتنمية "
                 "الزراعية (إيفاد) في اليمن من 1993 إلى 2010 متطلباتِ الضمانات وارتفاعَ تكاليف المعاملات وطولَ إجراءات الموافقة بين "
                 "الأسباب التي قيل إنها جعلت الأسر الفقيرة تُحجم عن ائتمان البنك الشريك، في مناطق مشروعات محددة قبل النزاع."),
                [IFADR], [IFADS])),
    ("MA-005", ((" Local observations point to a liquidity dimension that registers do not capture: a May 2026 report records "
                 "agents lacking enough cash during the Ramadan and Eid holiday period, with waits of four to five hours (from one "
                 "interview with a cash-programme manager), and funds released only in denominations of YER 100 and 200."),
                (" وتشير ملاحظات محلية إلى بُعدٍ للسيولة لا تلتقطه السجلات: إذ يرصد تقرير صدر في مايو 2026 افتقار الوكلاء إلى ما "
                 "يكفي من النقد خلال فترة عطلة رمضان والعيد، مع انتظار يمتد أربع ساعات إلى خمس (نقلًا عن مقابلة واحدة مع مدير لبرنامج "
                 "نقدي)، وصرف الأموال بفئتي 100 و200 ريال فقط."),
                ["CLM-045"], [PRESS])),
    ("MA-008", ((" The last independent measure of credit-registry coverage, the World Bank's Doing Business 2020 (data collected "
                 "to May 2019; city covered: Sana'a; series since discontinued), is given with the defaulters registry's launch in "
                 "the chronology; it is a historical reference, not a baseline for the registry CBY-Aden launched in 2026."),
                (" ويرد آخر قياس مستقل لتغطية سجل الائتمان، وهو تقرير ممارسة أنشطة الأعمال 2020 الصادر عن البنك الدولي (بيانات "
                 "جُمعت حتى مايو 2019؛ المدينة المشمولة: صنعاء؛ وقد توقفت السلسلة لاحقًا)، مع تدشين سجل المتعثرين في التسلسل الزمني؛ "
                 "وهو مرجع تاريخي، لا خط أساس للسجل الذي دشّنه البنك المركزي اليمني – عدن في 2026."),
                [], [DB20])),
    ("MA-009", ((" UNICEF's releases give the programme's announced reach and its channels in the October 2024 payment cycle "
                 "(payment sites, mobile teams and home outreach, and an e-wallet pilot), and announce that the cycle starting on "
                 "11 December 2024 ended the programme in its then-current form; a May 2026 report records, from one interview, "
                 "agents short of cash at cash-out during the Ramadan and Eid holiday period."),
                (" وتعرض بيانات اليونيسف النطاق المعلن للبرنامج وقنواته في دورة الدفع في أكتوبر 2024 (مواقع الصرف، والفرق المتنقلة "
                 "وخدمات الوصول إلى المنازل، وتجربة للمحفظة الإلكترونية)، وتعلن أن الدورة التي تبدأ في 11 ديسمبر 2024 تنهي البرنامج "
                 "بصيغته القائمة آنذاك؛ ويرصد تقرير صدر في مايو 2026، نقلًا عن مقابلة واحدة، نقص النقد لدى الوكلاء عند السحب خلال "
                 "فترة عطلة رمضان والعيد."),
                [], [UNI10, UNI12, PRESS])),
])

# ==================================================================================================================== 6C-3
# US to Yemen, 2025 Q3: 12 quotes, simple means 3.9167 and 2.3000 (V5 G). The three corridors are the only source countries
# for Yemen that quarter (26 quotes: 12 USA, 8 SAU, 6 ARE). The US corridor page refuses automated requests (11 October 2026),
# so the US averages are computed here from the quote-level dataset, as the SA and UAE averages were reproduced.
RPW_TITLE = ("The cost of sending money to Yemen: three corridors in 2025 Q3 and the World Bank's yearly average",
             "تكلفة إرسال الأموال إلى اليمن: ثلاثة ممرات في الربع الثالث من 2025 والمتوسط السنوي للبنك الدولي")
RPW_OLD_TITLE = ("The cost of sending money to Yemen: two corridors in 2025 Q3 and the World Bank's yearly average",
                 "تكلفة إرسال الأموال إلى اليمن: ممران في الربع الثالث من 2025 والمتوسط السنوي للبنك الدولي")
RPW_SUM = (("from the United Arab Emirates (UAE) the averages were 7.53% and 5.62% respectively. These are averages of quotes for "
            "formal products listed by the World Bank Remittance Prices Worldwide database in two corridors;",
            "from the United Arab Emirates (UAE) the averages were 7.53% and 5.62% respectively, and from the United States 3.92% "
            "and 2.30%. These are averages of quotes for formal products listed by the World Bank Remittance Prices Worldwide "
            "database in the three corridors to Yemen it surveyed that quarter;"),
           ("وبلغ المتوسطان من الإمارات 7.53% و5.62% على التوالي. وهذه متوسطات لعروض أسعار منتجات رسمية مدرجة في قاعدة بيانات "
            "البنك الدولي لأسعار الحوالات حول العالم (Remittance Prices Worldwide) في ممرين محددين،",
            "وبلغ المتوسطان من الإمارات 7.53% و5.62% على التوالي، ومن الولايات المتحدة 3.92% و2.30%. وهذه متوسطات لعروض أسعار "
            "منتجات رسمية مدرجة في قاعدة بيانات البنك الدولي لأسعار الحوالات حول العالم (Remittance Prices Worldwide) في الممرات "
            "الثلاثة إلى اليمن التي رصدتها في ذلك الربع،"))
RPW_DEF = (("from Saudi Arabia or the United Arab Emirates to Yemen",
            "from Saudi Arabia, the United Arab Emirates or the United States to Yemen"),
           ("من السعودية أو الإمارات إلى اليمن", "من السعودية أو الإمارات أو الولايات المتحدة إلى اليمن"))
RPW_PERIOD_AR = ("(متوسطات الممرين)", "(متوسطات الممرات)")
RPW_UNIV = (("for the Saudi Arabia–Yemen and United Arab Emirates–Yemen corridors",
             "for the Saudi Arabia–Yemen, United Arab Emirates–Yemen and United States–Yemen corridors"),
            ("لممرَّي السعودية–اليمن والإمارات–اليمن", "لممرات السعودية–اليمن والإمارات–اليمن والولايات المتحدة–اليمن"))
RPW_METHOD = (("(8 quotes for Saudi Arabia–Yemen, 6 for United Arab Emirates–Yemen).",
               "(8 quotes for Saudi Arabia–Yemen, 6 for United Arab Emirates–Yemen). The United States–Yemen averages are "
               "computed here in the same way, as the simple average of that corridor's 12 third-quarter 2025 quotes in the same "
               "dataset (read on 11 October 2026); the corridor page was not read."),
              ("(8 عروض لممر السعودية–اليمن، و6 لممر الإمارات–اليمن)، فطابق القيمة المنشورة حتى منزلتين عشريتين.",
               "(8 عروض لممر السعودية–اليمن، و6 لممر الإمارات–اليمن)، فطابق القيمة المنشورة حتى منزلتين عشريتين. ويُحسب هنا "
               "متوسطا ممر الولايات المتحدة–اليمن بالطريقة نفسها، بوصفهما المتوسط البسيط لعروض أسعار هذا الممر في الربع الثالث من "
               "2025 في مجموعة البيانات نفسها، وعددها 12 عرضًا (قُرئت في 11 أكتوبر 2026)؛ ولم تُقرأ صفحة هذا الممر."))
RPW_LIM1 = (("The corridor averages cover two corridors, two send amounts", "The corridor averages cover three corridors, two send amounts"),
            ("تغطي متوسطات الممرات ممرين ومبلغي إرسال", "تغطي متوسطات الممرات ثلاثة ممرات ومبلغي إرسال"))
RPW_LIM2 = (("each rests on few quotes (8 for Saudi Arabia–Yemen, 6 for United Arab Emirates–Yemen), and",
             "each rests on few quotes (8 for Saudi Arabia–Yemen, 6 for United Arab Emirates–Yemen, 12 for United States–Yemen); "
             "the 12 United States quotes mix products paid by card, from a bank account or in cash, online, by call centre or at "
             "an agent, so their average is the average listed quote, not the cost to a typical sender; and"),
            ("(8 لممر السعودية–اليمن، و6 لممر الإمارات–اليمن)، ويرفع",
             "(8 لممر السعودية–اليمن، و6 لممر الإمارات–اليمن، و12 لممر الولايات المتحدة–اليمن)؛ وتمزج عروض الولايات المتحدة الـ12 "
             "بين منتجات تُدفع بالبطاقة أو من حساب مصرفي أو نقدًا، عبر الإنترنت أو مركز اتصال أو لدى وكيل، فمتوسطها هو متوسط "
             "العروض المدرجة، لا التكلفة على مرسل نموذجي؛ ويرفع"))
RPW_CURR = (("On 10 October 2026 the corridor pages refused automated requests,",
             "On 10 October 2026 the Saudi Arabia and United Arab Emirates corridor pages refused automated requests, as did the "
             "United States page on 11 October 2026,"),
            ("تعود متوسطات الممرين إلى الربع الثالث من 2025. وفي 10 أكتوبر 2026 رفضت صفحتا الممرين الطلبات الآلية،",
             "تعود متوسطات الممرات إلى الربع الثالث من 2025. وفي 10 أكتوبر 2026 رفضت صفحتا ممرَّي السعودية والإمارات الطلبات "
             "الآلية، ورفضتها صفحة ممر الولايات المتحدة في 11 أكتوبر 2026،"))
RPW_SHOWS = (("Average quoted costs in the Saudi Arabia–Yemen and UAE–Yemen corridors",
              "Average quoted costs in the Saudi Arabia–Yemen, UAE–Yemen and United States–Yemen corridors"),
             ("في ممرَي السعودية–اليمن والإمارات–اليمن", "في ممرات السعودية–اليمن والإمارات–اليمن والولايات المتحدة–اليمن"))
RPW_DECISION = (("for Saudi Arabia–Yemen and UAE–Yemen at the same transfer sizes",
                 "for Saudi Arabia–Yemen, UAE–Yemen and United States–Yemen at the same transfer sizes"),
                ("لممري السعودية–اليمن والإمارات–اليمن", "لممرات السعودية–اليمن والإمارات–اليمن والولايات المتحدة–اليمن"))
RPW_ENCODING = ("Dot plot of two corridors by two send amounts", "Dot plot of three corridors by two send amounts")
RPW_VS = [
    vs("3.92%", "v", "DERIVED", RPWUS, "RPW Complete Dataset rpw_dataset_2011_2025_q3.xlsx, sheet \"Dataset (from Q2 2016)\", "
       "period \"2025_3Q\", rows source_code USA / destination_code YEM (12 quotes), simple mean of column \"cc1 total cost %\" "
       "= 3.9167" + V5),
    vs("2.30%", "v", "DERIVED", RPWUS, "same dataset, period \"2025_3Q\", rows USA/YEM, simple mean of column \"cc2 total cost "
       "%\" = 2.3000" + V5),
    vs("12", "v", "READ", RPWUS, "same dataset, period 2025_3Q, United States to Yemen: 12 rows (quotes collected 12 to 26 "
       "August 2025)" + V5),
    vs("11 October 2026", "d", "SITE"),
]
SECTIONS_RPW = [
    ("6C-3", "/remittances/", 5, "en", "body", "For UAE–Yemen they were 7.53% and 5.62%.",
     "For UAE–Yemen they were 7.53% and 5.62%. For United States–Yemen, computed here from the World Bank's quotes, they "
     "were 3.92% and 2.30%."),
    ("6C-3", "/remittances/", 5, "ar", "body", "أما ممر الإمارات–اليمن فبلغ 7.53% و5.62% على التوالي.",
     "أما ممر الإمارات–اليمن فبلغ 7.53% و5.62% على التوالي. وبلغ متوسطا ممر الولايات المتحدة–اليمن، محسوبين هنا من عروض "
     "أسعار البنك الدولي، 3.92% و2.30%."),
    ("6C-3", "/methodology/", 4, "en", "body", "and remittance prices in two corridors.",
     "and remittance prices in three corridors."),
    ("6C-3", "/methodology/", 4, "ar", "body", "وأسعار الحوالات في ممرين.", "وأسعار الحوالات في ثلاثة ممرات."),
    ("6C-3", "/readings/how-money-reaches-households/", 6, "en", "body",
     "one of the two corridors held here (the other, from the United Arab Emirates, averaged 7.53%, lifted by a single high "
     "quote).",
     "one of the three corridors held here (from the United Arab Emirates the average was 7.53%, lifted by a single high quote, "
     "and from the United States 3.92%)."),
    ("6C-3", "/readings/how-money-reaches-households/", 6, "ar", "body",
     "وهو أحد ممرّين تتضمنهما قاعدة الأدلة هذه (وبلغ متوسط الممر الآخر، من الإمارات، 7.53%، ويرفعه عرض سعر مرتفع واحد).",
     "وهو أحد ثلاثة ممرات تتضمنها قاعدة الأدلة هذه (وبلغ المتوسط من الإمارات 7.53%، ويرفعه عرض سعر مرتفع واحد، ومن الولايات "
     "المتحدة 3.92%)."),
]
UI_RPW = [  # (ui_id, new_en, new_ar, old_en, old_ar); None keeps a label
    ("UI-VIS-PANEL-RMT-RPW", "The three corridors to Yemen surveyed, by amount sent: third quarter of 2025",
     "الممرات الثلاثة المرصودة إلى اليمن، بحسب المبلغ المرسل: الربع الثالث من 2025",
     "Two of the corridors to Yemen, by amount sent: third quarter of 2025",
     "ممران من الممرات إلى اليمن، بحسب المبلغ المرسل: الربع الثالث من 2025"),
]
UI_RPW_AR_FIX = [("UI-VIS-RPW-AVERAGE-NOTE", "لوحة الممرين:", "لوحة الممرات:"),
                 ("UI-VIS-NOTE-SDG-10C", "لا على متوسطات الممرين المعروضة هنا", "لا على متوسطات الممرات المعروضة هنا")]
UI_NEW = [("UI-VIS-CAT-CORRIDOR-US", "United States", "الولايات المتحدة الأمريكية",
           "Close-out CLOSE-6E (6C-3). Chart label: corridor value 'United States'.")]
WDI_CAVEAT_AR = ("مع متوسطات الممرين للربع الثالث من 2025", "مع متوسطات الممرات للربع الثالث من 2025")
RPW_ROWS = [
    OrderedDict([("observation_id", f"RMO-RPW-US-2025Q3-{amt}"), ("source_id", RPWUS), ("series_vintage", "RPW_Q3_2025"),
                 ("domain", "remittance_corridor_costs"), ("geography", "United States → Yemen"), ("period", "2025-Q3"),
                 ("period_state", "OBSERVED_QUOTE_COLLECTION_PERIOD"), ("metric_id", "RMT-002"),
                 ("metric_label_en", "Total remittance transfer cost"), ("metric_label_ar", "التكلفة الإجمالية لإرسال التحويل"),
                 ("value", val), ("unit", "percent of send amount"), ("transaction_amount_usd", amt),
                 ("corridor_origin", "United States"), ("corridor_destination", "Yemen"),
                 ("evidence_type", "PRIMARY_OFFICIAL_CORRIDOR_QUOTE_AVERAGE"),
                 ("universe", "RPW quote observations displayed for the specified corridor and send amount"),
                 ("source_table_or_section", f"RPW quote-level dataset rpw_dataset_2011_2025_q3.xlsx, sheet 'Dataset (from Q2 "
                                             f"2016)', period 2025_3Q, source_code USA, destination_code YEM: simple mean of "
                                             f"'{col} total cost %' over the corridor's 12 quotes = {exact}; read 11 October "
                                             f"2026; the corridor page refuses automated requests"),
                 ("calculation_state", "SOURCE_PUBLISHED_AVERAGE"), ("comparability_state", "AMOUNT_SPECIFIC__DO_NOT_COLLAPSE"),
                 ("caveat_en", "Average is transaction-amount specific and can vary by provider, payment instrument, receiving "
                               "method, fee and FX margin. It is not a cost for all remittances into Yemen. Computed here as the "
                               "simple average of the corridor's 12 quotes in the World Bank's dataset, the method that "
                               "reproduces the published Saudi Arabia and United Arab Emirates averages; the corridor page was "
                               "not read."),
                 ("caveat_ar", "المتوسط خاص بقيمة التحويل المحددة، وقد يختلف باختلاف مقدم الخدمة وأداة الدفع وطريقة الاستلام "
                               "والرسوم وهامش سعر الصرف. ولا يمثل تكلفة جميع الحوالات الواردة إلى اليمن. ويُحسب هنا بوصفه المتوسط "
                               "البسيط لعروض الأسعار الـ12 لهذا الممر في مجموعة بيانات البنك الدولي، وهي الطريقة التي تعيد إنتاج "
                               "متوسطَي السعودية والإمارات المنشورين؛ ولم تُقرأ صفحة الممر."),
                 ("source_url", RPW_XLSX)])
    for amt, val, col, exact in ((200, 3.92, "cc1", "3.9167"), (500, 2.3, "cc2", "2.3000"))
]

# ==================================================================================================================== 6C-4
# (a) the credit-information pages and the registry announcement (V3 E). 31_REFORMS_REGULATION holds no Arabic column.
REF_REG_012_START = "Commercial and specialised banks report credit exposures from YER 500,000"
REF_REG_012 = ("Commercial and specialised banks report credit exposures from YER 500,000 on Form No. 6 by the 15th of the "
               "following month (publications/149, which cites Law No. 38 of 1998 on banks, Governor's Decision No. 4 of 1991, "
               "whose text is not published, Circular No. 33379 of 14 August 1991 and Circular No. 54064 of 2 July 2006); and "
               "grant no loan or financing to any customer, whatever its size, before an enquiry to the Credit and Banking Risk "
               "Department, nor any credit or financing before checking that the customer's name is not on the notification list "
               "under Circular No. 2 of 2000 (publications/150). Web posting is not an issue date.")
YSC030_FACT = (" The 5 August 2026 announcement cites no instrument and publishes no coverage, threshold or record count.",
               " ولا يستند إعلان 5 أغسطس 2026 إلى أي أداة تنظيمية، ولا ينشر تغطيةً ولا حدًّا أدنى ولا عدد سجلات.")
YSC030_IMPL_OLD = ("The registry adds a platform to the credit-information rules CBY-Aden publishes (exposure reporting on Form No. "
                   "6 and an enquiry before lending).",
                   "يضيف السجل منصة إلى قواعد معلومات الائتمان التي ينشرها البنك المركزي اليمني – عدن (الإبلاغ عن التعرضات الائتمانية "
                   "على الاستمارة رقم (6) والاستعلام قبل منح الائتمان).")
YSC030_IMPL = ("The registry adds a platform to the credit-information rules CBY-Aden publishes. Its reporting rule has banks "
               "report credit exposures on Form No. 6 and cites Law No. 38 of 1998 on banks, Governor's Decision No. 4 of 1991, "
               "Circular No. 33379 of 14 August 1991 and Circular No. 54064 of 2 July 2006; its enquiry rule bars any loan or "
               "financing, whatever its size, before an enquiry, and any credit or financing before checking that the customer's "
               "name is not on the notification list under Circular No. 2 of 2000. The announcement does not link the registry to "
               "these rules.",
               "يضيف السجل منصة إلى قواعد معلومات الائتمان التي ينشرها البنك المركزي اليمني – عدن. فقاعدة الإبلاغ تُلزم البنوك "
               "بالإبلاغ عن التعرضات الائتمانية على الاستمارة رقم (6)، وتستند إلى القانون رقم (38) لسنة 1998 بشأن البنوك، وقرار "
               "المحافظ رقم (4) لسنة 1991، والتعميم رقم (33379) بتاريخ 14 أغسطس 1991، والتعميم رقم (54064) بتاريخ 2 يوليو 2006؛ "
               "وتحظر قاعدة الاستعلام منح أي قرض أو تمويل، مهما كان حجمه، قبل الاستعلام عن العميل، ومنح أي ائتمان أو تمويل قبل "
               "التأكد من عدم ورود اسمه في قائمة الإشعار وفقًا للمنشور الدوري رقم (2) لعام 2000. ولا يربط الإعلان السجل بهذه "
               "القواعد.")
# (b) Doing Business 2020 (V4 D; the discontinuation statement read 11 October 2026). MA-008 binds no Evidence Record and
# this instruction allows no new route for one, so the figures sit, with their states, on the registry's own chronology event.
YSC030_REL = (" The last independent measure, the World Bank's Doing Business 2020 (data collected to May 2019; city covered: "
              "Sana'a; series since discontinued), put public credit-registry coverage at 1.3% of adults (216,245 individuals and "
              "firms) and private-bureau coverage at 0%; it is a historical reference, not a baseline for this registry.",
              " وكان آخر قياس مستقل، وهو تقرير ممارسة أنشطة الأعمال 2020 الصادر عن البنك الدولي (بيانات جُمعت حتى مايو 2019؛ "
              "المدينة المشمولة: صنعاء؛ وقد توقفت السلسلة لاحقًا)، قد قدّر تغطية سجل الائتمان العام بنسبة 1.3% من البالغين "
              "(216,245 فردًا ومنشأة) وتغطية مكاتب الائتمان الخاصة بنسبة 0%؛ وهو مرجع تاريخي، لا خط أساس لهذا السجل.")
DB20L = "Doing Business 2020, Yemen, Rep. economy profile"
YSC030_VS = [
    vs("1.3%", "v", "READ", DB20, DB20L + ", PDF p.30 ('Page 30'), 'Details – Credit Information', Coverage: Credit registry, "
       "Percentage of adult population 1.3" + V4),
    vs("216,245", "v", "READ", DB20, DB20L + ", p.30, Coverage: Credit registry, Total 216,245 (211,476 individuals + 4,769 "
       "firms)" + V4),
    vs("0%", "v", "READ", DB20, DB20L + ", p.30, Coverage: Credit bureau, Percentage of adult population 0.0" + V4),
    vs("May 2019", "d", "READ", DB20, DB20L + ", p.26: 'The most recent round of data collection for the project was completed "
       "in May 2019'; city covered Sanaa, p.4" + V4),
    vs("2020", "v", "TRIVIAL"),
    vs("14 August 1991", "d", "READ", CRI149, "cby-ye.com/publications/149, opening: «التعميم رقم (33379) بتاريخ 14/8/1991م»" + V3),
    vs("2 July 2006", "d", "READ", CRI149, "cby-ye.com/publications/149, opening: «والتعميم رقم (54064) بتاريخ 2/7/2006م»" + V3),
    vs("1998", "v", "READ", CRI149, "cby-ye.com/publications/149: «القانون رقم (38) لسنة 1998م بشأن البنوك»" + V3),
    vs("2000", "v", "READ", CRI150, "cby-ye.com/publications/150, item 3: «للمنشور الدوري رقم (2) لعام 2000م»" + V3),
]

# ==================================================================================================================== 6C-5 IFAD
IFAD_EN = ("An independent evaluation of IFAD's Yemen programme from 1993 to 2010, by IFAD's Independent Office of Evaluation "
           "(2011), found that, in the completed projects, credit lines disbursed US$4.165 million, 31% of the US$13.37 million "
           "provided, to 3,723 clients, 6% of the 58,867 planned; repayment rates ranged from 31% to 64%. In one project area, "
           "Raymah, fewer than 1% of the farmers in the project area received financing during the project, and in the Southern "
           "Governorates the rural finance component was, in the evaluators' words, not really implemented at all. The evaluation "
           "reports that poor households were said to be reluctant to borrow from the Cooperative and Agriculture Credit Bank "
           "(CACB), the government bank the projects depended on, because of its collateral requirements, high transaction costs "
           "and lengthy approval procedures and a reluctance to deal with an institution seen as charging interest; that women, "
           "who did not generally own land, had little access to its credit, as was also true of sharecroppers; and that branches "
           "built with IFAD support were sited away from commercial centres.")
IFAD_AR = ("وجد تقييم مستقل لبرنامج الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن من 1993 إلى 2010، أجراه مكتب التقييم المستقل "
           "التابع للصندوق (2011)، أن خطوط الائتمان في المشروعات المكتملة صرفت 4.165 مليون دولار أمريكي، أي 31% من 13.37 مليون "
           "دولار خُصصت لها، إلى 3,723 عميلًا، أي 6% من 58,867 عميلًا كان مخططًا الوصول إليهم؛ وتراوحت معدلات السداد بين 31% و64%. "
           "وفي منطقة مشروع واحدة، هي ريمة، حصل أقل من 1% من المزارعين في منطقة المشروع على تمويل خلال فترة المشروع، ولم يُنفَّذ "
           "مكوّن التمويل الريفي في المحافظات الجنوبية فعليًا على الإطلاق، بتعبير المقيّمين. ويذكر التقييم أن الأسر الفقيرة قيل إنها "
           "كانت تُحجم عن الاقتراض من بنك التسليف التعاوني والزراعي، وهو البنك الحكومي الذي اعتمدت عليه المشروعات، بسبب متطلبات "
           "الضمانات وارتفاع تكاليف المعاملات وطول إجراءات الموافقة والإحجام عن التعامل مع مؤسسة يُنظر إليها على أنها تتقاضى فائدة؛ "
           "وأن النساء، اللواتي لم يكنّ في الغالب يملكن أرضًا، كان وصولهن إلى ائتمانه محدودًا، وكذلك المزارعون العاملون بنظام "
           "المشاركة في المحصول؛ وأن فروعًا بُنيت بدعم من الصندوق أُقيمت بعيدًا عن المراكز التجارية.")
IFL = "IFAD IOE, Republic of Yemen Country Programme Evaluation, EC 2011/69/W.P.4/Rev.1"
IFAD_VS = [
    vs("4.165", "v", "READ", IFADS, IFL + ", para 176, printed p.40 (PDF p.57): 'loans valued at US$4.165 million'" + V5),
    vs("US$4.165 million", "v", "READ", IFADS, IFL + ", para 176, printed p.40" + V5),
    vs("31%", "v", "READ", IFADS, IFL + ", para 176, printed p.40: '31 per cent of the total amount of funds provided'; 'Repayment "
       "rates ranged from 31 per cent to 64 per cent'" + V5),
    vs("13.37", "v", "READ", IFADS, IFL + ", para 176, printed p.40: 'lines of credit worth US$13.37 million'" + V5),
    vs("US$13.37 million", "v", "READ", IFADS, IFL + ", para 176, printed p.40" + V5),
    vs("3,723", "v", "READ", IFADS, IFL + ", para 176, printed p.40: 'to 3,723 clients'" + V5),
    vs("6%", "v", "READ", IFADS, IFL + ", para 176, printed p.40: '6 per cent of the planned targets of 58,867 clients'" + V5),
    vs("58,867", "v", "READ", IFADS, IFL + ", para 176, printed p.40" + V5),
    vs("64%", "v", "READ", IFADS, IFL + ", para 176, printed p.40" + V5),
    vs("1%", "v", "READ", IFADS, IFL + ", para 177, printed p.40: 'Less than 1 per cent of the farmers in the project area "
       "received financing during the project period' (footnote 102: 48,000 households assumed)" + V5),
    vs("10%", "v", "READ", IFADS, IFL + ", para 177, printed p.40: 'the 10 per cent of landowning farmers which was given as an "
       "indicator of its success'" + V5),
    vs("48,000", "v", "READ", IFADS, IFL + ", printed p.40, footnote 102" + V5),
    vs("6 October 2011", "d", "READ", IFADS, IFL + ", cover: 'Date: 6 October 2011'" + V5),
    vs("23 September 2011", "d", "READ", IFADS, IFL + ", inner title page (PDF p.2)" + V5),
    vs("176", "v", "LOCATOR"), vs("177", "v", "LOCATOR"), vs("138", "v", "LOCATOR"), vs("140", "v", "LOCATOR"),
    vs("101", "v", "LOCATOR"), vs("40", "v", "LOCATOR"), vs("33", "v", "LOCATOR"), vs("3", "v", "LOCATOR"),
    vs("9", "v", "LOCATOR"), vs("102", "v", "LOCATOR"), vs("69", "v", "LOCATOR"), vs("4", "v", "LOCATOR"),
    vs("11 October 2026", "d", "SITE"),
]
BOUND_EN = ("This record is drawn from the source(s) listed on this page. Open a source record to reach the original document, and "
            "check that the definition, period, population and geography match what is stated here.")
BOUND_AR = ("يستند هذا السجل إلى المصدر أو المصادر المدرجة في هذه الصفحة. افتح سجل المصدر للوصول إلى الوثيقة الأصلية، وتحقق من "
            "تطابق التعريف والفترة والمجتمع والنطاق الجغرافي مع ما يرد هنا.")
TRIGGER_EN = ("This record is updated when an authoritative source is revised or replaced, a newer comparable observation becomes "
              "available, the definition, population or method changes, or the conditions for public use change.")
TRIGGER_AR = ("يُحدَّث هذا السجل عند مراجعة المصدر المعتمد أو استبداله، أو توفر مشاهدة أحدث قابلة للمقارنة، أو تغير التعريف أو المجتمع "
              "أو الطريقة، أو تغير شروط الاستخدام العام.")
IFAD_RECORD = OrderedDict([
    ("object_id", IFADR), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/finance/ | /firms/"),
    ("title_en", "Rural credit in IFAD-financed projects in Yemen, 1993 to 2010: an independent evaluation (IFAD, 2011)"),
    ("title_ar", "الائتمان الريفي في المشروعات التي موّلها الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن، 1993 إلى 2010: تقييم "
                 "مستقل (إيفاد، 2011)"),
    ("summary_en", IFAD_EN), ("summary_ar", IFAD_AR),
    ("definition_en", "Findings on rural finance in IFAD-financed projects in Yemen from 1993 to 2010, from the Country Programme "
                      "Evaluation by IFAD's Independent Office of Evaluation (2011)."),
    ("definition_ar", "نتائج عن التمويل الريفي في المشروعات التي موّلها الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن من 1993 إلى "
                      "2010، من تقييم البرنامج القُطري الذي أجراه مكتب التقييم المستقل التابع للصندوق (2011)."),
    ("period_en", "1993 to 2010 (the projects evaluated); evaluation dated 6 October 2011"),
    ("period_ar", "من 1993 إلى 2010 (المشروعات التي شملها التقييم)؛ والتقييم مؤرخ في 6 أكتوبر 2011"),
    ("universe_en", "IFAD-financed projects in Yemen and their project areas; the lending figures cover the completed projects."),
    ("universe_ar", "المشروعات التي موّلها الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن ومناطقها؛ وتغطي أرقام الإقراض المشروعات "
                    "المكتملة."),
    ("method_en", "Read from the evaluation (document EC 2011/69/W.P.4/Rev.1, dated 6 October 2011, distribution Public; its title "
                  "page is dated 23 September 2011): paragraphs 176 and 177 (printed p. 40) for the lending, outreach and repayment "
                  "figures, which footnote 101 says the evaluation team estimated from the latest information available with the "
                  "CACB; paragraphs 138 to 140 (printed p. 33) for the reasons reported; paragraphs 9 and 10 (printed p. 3) for the "
                  "period covered. In Raymah the share of farmers financed uses the farmers in the project area (footnote 102 "
                  "assumes 48,000 households), while the project's 10% indicator refers to landowning farmers, so the two are not "
                  "one measure and are not set against each other here."),
    ("method_ar", "مقروء من التقييم (الوثيقة EC 2011/69/W.P.4/Rev.1، المؤرخة في 6 أكتوبر 2011، والمتاحة للعموم؛ وصفحة عنوانه مؤرخة "
                  "في 23 سبتمبر 2011): الفقرتان 176 و177 (ص. 40) لأرقام الإقراض والوصول والسداد، التي تذكر الحاشية 101 أن فريق "
                  "التقييم قدّرها من أحدث المعلومات المتاحة لدى بنك التسليف التعاوني والزراعي؛ والفقرات من 138 إلى 140 (ص. 33) "
                  "للأسباب المذكورة؛ والفقرتان 9 و10 (ص. 3) للفترة المشمولة. وفي ريمة تستند نسبة المزارعين الذين حصلوا على تمويل "
                  "إلى المزارعين في منطقة المشروع (تفترض الحاشية 102 وجود 48,000 أسرة)، بينما يشير مؤشر المشروع البالغ 10% إلى "
                  "المزارعين المالكين للأرض، فهما ليسا مقياسًا واحدًا ولا يُقابَل أحدهما بالآخر هنا."),
    ("limitations_en", "These are historical findings for specific project areas before the conflict; they are not a measure of "
                       "rural access to finance today, and the delivery channels have since changed. | The lending figures are the "
                       "evaluators' estimates for the completed projects, not audited accounts, and the reasons for low uptake are "
                       "views the evaluation reports, drawn from project documents and discussions with potential clients."),
    ("limitations_ar", "هذه نتائج تاريخية لمناطق مشروعات محددة قبل النزاع؛ وليست مقياسًا للوصول الريفي إلى التمويل اليوم، وقد تغيرت "
                       "قنوات الإيصال منذ ذلك الحين. | أرقام الإقراض تقديرات المقيّمين للمشروعات المكتملة، لا حسابات مدققة، وأسباب ضعف "
                       "الإقبال آراء يوردها التقييم، مستمدة من وثائق المشروعات ومن نقاشات مع عملاء محتملين."),
    ("currentness_en", "The evaluation is dated 6 October 2011 and covers 1993 to 2010 (checked on 11 October 2026). It should not "
                       "be read as describing a later period."),
    ("currentness_ar", "التقييم مؤرخ في 6 أكتوبر 2011 ويغطي الفترة من 1993 إلى 2010 (جرى التحقق في 11 أكتوبر 2026)، ولا يُقرأ على أنه "
                       "يصف فترة لاحقة."),
    ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
    ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
    ("source_dependencies", IFADS),
    ("source_links", None),       # set from the source library at run time
    ("lineage_state", "BOUND_EXACT"),
    ("value_states", IFAD_VS),
])
IFAD_META = ("An independent evaluation of IFAD's Yemen programme, 1993 to 2010: credit reached 3,723 clients, 6% of those "
             "planned. Historical findings for project areas, not a measure of access today.",
             "تقييم مستقل لبرنامج إيفاد في اليمن، 1993 إلى 2010: وصل الائتمان إلى 3,723 عميلًا، أي 6% من المخطط. نتائج تاريخية "
             "لمناطق مشروعات، لا مقياس للوصول اليوم.")

# ==================================================================================================================== sources
NOTE = "Facts cited; nothing reproduced."
NEW_SOURCES = [
    OrderedDict([("source_id", UNI10), ("primary_url", UNI10_URL), ("datasets_or_use", "RESOURCE_LIBRARY_ONLY__UNICEF_UCT_PROGRAMME_RELEASES"), ("row_count", 0),
                 ("display_title", "1.43 million vulnerable families supported with cash assistance across Yemen (UNICEF press "
                                   "release, 2 October 2024)"),
                 ("publisher", "UNICEF Yemen"), ("public_card_state", "CITATION_CARD"),
                 ("display_title_ar", "1.43 مليون أسرة ضعيفة تتلقى مساعدات نقدية في أنحاء اليمن (بيان صحفي لليونيسف، 2 أكتوبر 2024)"),
                 ("non_public_locator_note", "The unconditional cash transfer's 18th payment cycle; read 11 October 2026 (SHA-256 "
                                             "215a60f659953baa91a4f0d23ca1eb2b67c1ac6ea43f12ffa35888f3d08cf06d). The release's "
                                             "US$62.5 million is stated as to be disbursed (planned) and is not used. " + NOTE),
                 ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", NOTE), ("retrieval_date", TODAY),
                 ("publisher_ar", "اليونيسف – اليمن"), ("document_label", "News release"), ("document_label_ar", "بيان صحفي"),
                 ("document_date", "2024-10-02")]),
    OrderedDict([("source_id", UNI12), ("primary_url", UNI12_URL), ("datasets_or_use", "RESOURCE_LIBRARY_ONLY__UNICEF_UCT_PROGRAMME_RELEASES"), ("row_count", 0),
                 ("display_title", "UNICEF and partners launch the 19th Payment Cycle of the current Unconditional Cash Transfer "
                                   "Project in Yemen (UNICEF press release, 7 December 2024)"),
                 ("publisher", "UNICEF Yemen"), ("public_card_state", "CITATION_CARD"),
                 ("display_title_ar", "اليونيسف وشركاؤها يطلقون دورة الدفع 19 من مشروع التحويلات النقدية غير المشروطة الحالي في اليمن "
                                      "(بيان صحفي لليونيسف، 7 ديسمبر 2024)"),
                 ("non_public_locator_note", "Read 11 October 2026 (SHA-256 f48823f8bc7937138fd665391f854e9f85f787230e3df4ebea6c9e"
                                             "a5c4945184): the 19th cycle starts on 11 December 2024 at fixed payment sites and "
                                             "'marks the end of the current UCT program'; the release gives no amount. " + NOTE),
                 ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", NOTE), ("retrieval_date", TODAY),
                 ("publisher_ar", "اليونيسف – اليمن"), ("document_label", "News release"), ("document_label_ar", "بيان صحفي"),
                 ("document_date", "2024-12-07")]),
    OrderedDict([("source_id", RPWUS), ("primary_url", RPW_XLSX), ("datasets_or_use", "DS-REMITTANCES"), ("row_count", 2),
                 ("display_title", "Remittance Prices Worldwide: United States to Yemen corridor (third quarter of 2025)"),
                 ("publisher", "World Bank"), ("public_card_state", "CITATION_CARD"),
                 ("display_title_ar", "قاعدة بيانات Remittance Prices Worldwide: ممر الحوالات من الولايات المتحدة إلى اليمن (الربع "
                                      "الثالث من 2025)"),
                 ("non_public_locator_note", "The quote-level dataset rpw_dataset_2011_2025_q3.xlsx (sheet 'Dataset (from Q2 2016)', "
                                             "period 2025_3Q, USA to YEM: 12 quotes collected 12 to 26 August 2025); read 11 "
                                             "October 2026 (SHA-256 f1d7265b1856d61812c158d3d03fae686dbff58735deabe016a6bfe23482"
                                             "d2a8). The corridor page refused automated requests on 11 October 2026. The "
                                             "workbook's Terms of Use sheet reads 'Restricted Data'; values are cited, the file is "
                                             "not hosted. " + NOTE),
                 ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", NOTE), ("retrieval_date", TODAY),
                 ("publisher_ar", "البنك الدولي"), ("document_label", "Database or web interface"),
                 ("document_label_ar", "قاعدة بيانات أو واجهة إلكترونية")]),
    OrderedDict([("source_id", DB20), ("primary_url", DB20_URL), ("additional_urls", '["' + DB20_STMT + '"]'),
                 ("datasets_or_use", "RESOURCE_LIBRARY_ONLY__CREDIT_REGISTRY_HISTORICAL_MEASURE,14_SYSTEM_CHRONOLOGY"), ("row_count", 0),
                 ("display_title", "Doing Business 2020: Yemen, Rep. economy profile (World Bank, 2019)"),
                 ("publisher", "World Bank"), ("public_card_state", "CITATION_CARD"),
                 ("display_title_ar", "ممارسة أنشطة الأعمال 2020: الملف الاقتصادي لليمن (البنك الدولي، 2019)"),
                 ("non_public_locator_note", "Credit registry and bureau coverage, 'Details – Credit Information', p.30; data "
                                             "collection completed in May 2019, p.26; city covered Sanaa, p.4. Read 11 October "
                                             "2026 (63 pages, SHA-256 7c9e4ba60891e279ca57167e1a969e3321472bef113a1599fad420269"
                                             "beac375). The World Bank discontinued the Doing Business report (statement of 16 "
                                             "September 2021, the additional URL; read 11 October 2026). Index scores and ranks "
                                             "are not used. " + NOTE),
                 ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", NOTE), ("retrieval_date", TODAY),
                 ("publisher_ar", "البنك الدولي"), ("document_label", "Periodic statistical report"),
                 ("document_label_ar", "تقرير إحصائي دوري"), ("document_date", "2019")]),
    OrderedDict([("source_id", IFADS), ("primary_url", IFAD_URL), ("datasets_or_use", "RESOURCE_LIBRARY_ONLY__IFAD_RURAL_FINANCE_EVALUATION"), ("row_count", 0),
                 ("display_title", "Republic of Yemen: Country Programme Evaluation (IFAD Independent Office of Evaluation, "
                                   "EC 2011/69/W.P.4/Rev.1, 6 October 2011)"),
                 ("publisher", "International Fund for Agricultural Development (IFAD)"), ("public_card_state", "CITATION_CARD"),
                 ("display_title_ar", "الجمهورية اليمنية: تقييم البرنامج القُطري (مكتب التقييم المستقل في الصندوق الدولي للتنمية "
                                      "الزراعية، EC 2011/69/W.P.4/Rev.1، 6 أكتوبر 2011)"),
                 ("non_public_locator_note", "Distribution: Public (cover). Pages used: printed p.3 (paras 9-10), p.33 (paras "
                                             "138-140), p.40 (paras 176-177, Table 6, footnotes 101-102). Read 11 October 2026 "
                                             "(136 pages, SHA-256 a5a9cfd3380264541c5debf5cc4dc93581e261434f314b98edaffcdbf0c5f6"
                                             "87). " + NOTE),
                 ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", NOTE), ("retrieval_date", TODAY),
                 ("publisher_ar", "الصندوق الدولي للتنمية الزراعية (إيفاد)"), ("document_label", "Research or policy paper"),
                 ("document_label_ar", "ورقة بحثية أو سياساتية"), ("document_date", "2011-10-06")]),
]


# ==================================================================================================================== Domain-lens revisions
# REDTEAM_6E.md (B1-B2, S2-S13, N1-N7 applied; S1 does not reproduce: SAM p.1 places both sub-districts under the IRG,
# addendum/R5_ccy_isp_sam.md; S14 recorded for the release rights check).
INF_NEW = (INF_NEW[0].replace(
    "That sample was drawn from activity and location lists rather than a national register and does not represent informal "
    "firms.",
    "That sample was drawn by listing businesses in two to four main market areas in each of the seven governorates and "
    "sampling them by activity, interviewing the first owner who agreed; 179 of the 217 firms were in areas under the de facto "
    "authorities, and the sample does not represent informal firms in Yemen."),
    INF_NEW[1].replace(
    "وقد سُحبت هذه العينة من قوائم للأنشطة والمواقع لا من سجل وطني، ولا تمثل المنشآت غير الرسمية.",
    "وقد سُحبت هذه العينة بحصر المنشآت في منطقتين إلى أربع مناطق سوقية رئيسية في كل محافظة من المحافظات السبع واختيارها بحسب "
    "النشاط، مع مقابلة أول مالك وافق؛ وكانت 179 منشأة من أصل 217 في مناطق خاضعة لسلطات الأمر الواقع، ولا تمثل العينة المنشآت "
    "غير الرسمية في اليمن."))
assert "179" in INF_NEW[0] and "179" in INF_NEW[1]
INF_VS = INF_VS + [vs("179", "v", "READ", FSD, "Annex III, Figure 101, p.141 (informal: 38 IRG + 179 Houthi-controlled = 217); "
                      "sampling, p.140" + V4)]

SMEPS_NEW = (SMEPS_NEW[0][:-1] + "; the other 960 are listed as 'SMEs and BAs', a term the report does not define.",
             SMEPS_NEW[1][:-1] + "؛ وتُدرج الـ960 الأخرى تحت «SMEs and BAs»، وهو مصطلح لا يعرّفه التقرير.")
SMEPS_VS = SMEPS_VS + [vs("960", "v", "READ", SMEPS, "SMEPS 2024 Executive Report, Key indicators table, printed p.9 (PDF p.5), "
                          "row 'SMEs and BAs', 2024 column" + V5)]

DEBT = ("Two Cash Consortium of Yemen studies of cash-assistance recipients, in sub-districts that the studies place in areas "
        "under the internationally recognized government, point to debt repayment as a common use of transfers. In a survey of "
        "recipient households in Ad-Dali and Ja’ar in January 2024 (291 and 209 interviews), posted online by its host in "
        "November 2024, 40% reported debt repayment among their regular expenses in the 30 days before the interview: about 47% "
        "of the households paid in those 30 days and about 30% of those not paid. In a 2026 study comparing three and six "
        "monthly transfers in Ja’ar, “debts are paid off” was one of the two most common answers to which part of the household "
        "economy improved most at the endline in November 2025 (one answer allowed): 60% of the 45 households that received six "
        "transfers gave it, and 40% of the 107 that received three. In the 2024 study, 11 of 21 business owners who answered in "
        "Ad-Dali and 10 of 21 in Ja’ar said that fewer customers bought on credit when cash assistance was distributed. These are "
        "local samples of aid recipients and business owners, not national estimates, and the business owners' answers are "
        "counts of interviews, not credit volumes. They are one reason why immediate cash-out is not, by itself, a sign that a "
        "transfer failed.",
        "وتشير دراستان لتحالف النقد في اليمن عن متلقي المساعدات النقدية، في مديريات فرعية تضعها الدراستان في المناطق الخاضعة "
        "للحكومة المعترف بها دوليًا، إلى سداد الديون بوصفه استخدامًا شائعًا للتحويلات. ففي مسح لأسر متلقية في الضالع وجعار أُجري "
        "في يناير 2024 (291 و209 مقابلات)، ونشره مستضيفه على الإنترنت في نوفمبر 2024، أفادت 40% من الأسر بأن سداد الديون من "
        "نفقاتها المنتظمة خلال 30 يومًا سبقت المقابلة: نحو 47% من الأسر التي تلقت دفعة خلال تلك الأيام الـ30، ونحو 30% من الأسر "
        "التي لم تتلقَّ. وفي دراسة صدرت في 2026 قارنت بين ثلاثة تحويلات شهرية وستة في جعار، كانت «سُدّدت الديون» إحدى الإجابتين "
        "الأكثر شيوعًا عن سؤال أيّ جوانب اقتصاد الأسرة تحسّن أكثر من غيره في التقييم الختامي في نوفمبر 2025 (مع السماح بإجابة "
        "واحدة): فقد اختارتها 60% من الأسر الـ45 التي تلقت ستة تحويلات، و40% من الأسر الـ107 التي تلقت ثلاثة. وفي دراسة 2024، قال "
        "11 من أصل 21 من أصحاب الأعمال الذين أجابوا في الضالع، و10 من أصل 21 في جعار، إن عدد الزبائن الذين يشترون بالدَّين انخفض "
        "عند توزيع المساعدات النقدية. وهذه عينات محلية من متلقي المساعدات ومن أصحاب الأعمال، لا تقديرات وطنية، وإجابات أصحاب "
        "الأعمال أعداد مقابلات لا أحجام ائتمان. وهي من أسباب ألا يُعدّ السحب النقدي الفوري في حد ذاته دليلًا على فشل التحويل.")
CLM045_VS = CLM045_VS + [
    vs("47%", "v", "READ", SAM, SAML + ", printed p.14 (PDF p.15): 'about 47% of HHs that received MPCA reported debt repayment "
       "compared to approximately 30% of HHs that did not receive MPCA within 30 days of the interview'" + V5),
    vs("30%", "v", "READ", SAM, SAML + ", printed p.14 (PDF p.15), as for 47%" + V5),
]

_CASH_BODY = ("most multi-purpose cash assistance (MPCA: the humanitarian cash programmes the report covers, not the unconditional "
              "cash transfer, which has run no payment cycle since January 2025) was disbursed through microfinance banks as "
              "vouchers that recipients exchange at local agents of financial service providers and, citing one interview with an "
              "MPCA programme manager in April 2026, that during the Ramadan and Eid holiday period agents often lacked enough "
              "cash, with waits of four to five hours. It reports that funds were released only in denominations of YER 100 and "
              "200 and, citing the same interview, that an e-wallet pilot disbursed funds without problems or delays. These are "
              "reported observations, some of them from a single interview. The paragraph names no programme or area, though the "
              "report frames the liquidity crisis as affecting areas under the internationally recognized government, rural "
              "recipients most, and says the problems eased after the period of high demand. The e-wallet result concerns "
              "disbursement, not whether recipients could then obtain cash, which the report itself calls unclear.")
_CASH_BODY_AR = ("معظم المساعدات النقدية متعددة الأغراض (وهي برامج النقد الإنساني التي يتناولها التقرير، لا برنامج التحويلات النقدية "
                 "غير المشروطة الذي لم يُجرِ أي دورة دفع منذ يناير 2025) صُرفت عبر بنوك التمويل الأصغر في صورة قسائم يستبدلها "
                 "المستفيدون لدى وكلاء محليين لمقدمي الخدمات المالية، وينقل عن مقابلة واحدة مع مدير لبرنامج للمساعدات النقدية "
                 "متعددة الأغراض في أبريل 2026 أن الوكلاء كثيرًا ما افتقروا خلال فترة عطلة رمضان والعيد إلى ما يكفي من النقد، "
                 "فامتد الانتظار أربع ساعات إلى خمس. ويذكر أن الأموال صُرفت بفئتي 100 و200 ريال فقط، وينقل عن المقابلة نفسها أن "
                 "تجربة للمحفظة الإلكترونية صرفت الأموال دون مشكلات أو تأخير. وهذه ملاحظات مُبلَّغ عنها، بعضها من مقابلة واحدة. ولا "
                 "تسمّي الفقرة برنامجًا ولا منطقة، وإن كان التقرير يصف أزمة السيولة بأنها أصابت المناطق الخاضعة للحكومة المعترف بها "
                 "دوليًا، والمستفيدين في الريف أكثر من غيرهم، ويذكر أن المشكلات خفّت بعد فترة ارتفاع الطلب. ونتيجة المحفظة "
                 "الإلكترونية تخص صرف الأموال، لا قدرة المستفيدين بعد ذلك على الحصول على النقد، وهي مسألة يصفها التقرير نفسه بأنها "
                 "غير واضحة.")
CASH_READING = ("The same May 2026 report adds an observation on cash-out. It says that " + _CASH_BODY,
                "ويضيف التقرير نفسه الصادر في مايو 2026 ملاحظة عن السحب النقدي، إذ يذكر أن " + _CASH_BODY_AR)
CASH_RECORD = ("On cash-out, a Cash Consortium of Yemen report of May 2026 says that " + _CASH_BODY,
               "وعن السحب النقدي، يذكر تقرير لتحالف النقد في اليمن صدر في مايو 2026 أن " + _CASH_BODY_AR)

MA_ADD["MA-001"] = ((" For shop credit to households (customers buying from shops on credit) there are local observations, not a "
                     "baseline: in a 2024 Cash Consortium of Yemen study, 11 of 21 business owners who answered in Ad-Dali and 10 "
                     "of 21 in Ja’ar said that fewer customers bought on credit when cash assistance was distributed."),
                    (" أما الشراء بالدَّين من المتاجر (ائتمان المتاجر للأسر) فلا تتوافر عنه إلا ملاحظات محلية لا خط أساس: ففي دراسة "
                     "لتحالف النقد في اليمن صدرت في 2024، قال 11 من أصل 21 من أصحاب الأعمال الذين أجابوا في الضالع، و10 من أصل 21 "
                     "في جعار، إن عدد الزبائن الذين يشترون بالدَّين انخفض عند توزيع المساعدات النقدية."),
                    ["CLM-045"], [SAM])
MA_ADD["MA-004"] = ((" For collateral and terms the evidence is historical: an evaluation of IFAD-financed rural credit in Yemen "
                     "from 1993 to 2010 by IFAD's Independent Office of Evaluation reports collateral requirements, high "
                     "transaction costs and long approval procedures among the reasons poor households were said to avoid the "
                     "partner bank's credit, in specific project areas before the conflict."),
                    (" أما الضمانات والشروط فأدلتها تاريخية: إذ يورد تقييم أجراه مكتب التقييم المستقل في الصندوق الدولي للتنمية "
                     "الزراعية (إيفاد) للائتمان الريفي الذي موّله الصندوق في اليمن من 1993 إلى 2010 متطلباتِ الضمانات وارتفاعَ "
                     "تكاليف المعاملات وطولَ إجراءات الموافقة بين الأسباب التي قيل إنها جعلت الأسر الفقيرة تُحجم عن ائتمان البنك "
                     "الشريك، في مناطق مشروعات محددة قبل النزاع."),
                    [IFADR], [IFADS])
MA_ADD["MA-005"] = ((" Local observations point to a liquidity dimension that registers do not capture: a May 2026 report on "
                     "humanitarian multi-purpose cash assistance records agents lacking enough cash during the Ramadan and Eid "
                     "holiday period, with waits of four to five hours (from one interview with a programme manager), and funds "
                     "released only in denominations of YER 100 and 200."),
                    (" وتشير ملاحظات محلية إلى بُعدٍ للسيولة لا تلتقطه السجلات: إذ يرصد تقرير صدر في مايو 2026 عن المساعدات "
                     "النقدية الإنسانية متعددة الأغراض افتقار الوكلاء إلى ما يكفي من النقد خلال فترة عطلة رمضان والعيد، مع انتظار "
                     "يمتد أربع ساعات إلى خمس (نقلًا عن مقابلة واحدة مع مدير برنامج)، وصرف الأموال بفئتي 100 و200 ريال فقط."),
                    ["CLM-045"], [PRESS])
MA_ADD["MA-008"] = ((" The most recent published measure of credit-registry coverage that this resource holds, the World Bank's "
                     "Doing Business 2020 (data collected to May 2019; city covered: Sana'a; series since discontinued), is given "
                     "with the defaulters registry's launch in the chronology; it is a historical reference, not a baseline for "
                     "the registry CBY-Aden launched in 2026."),
                    (" ويرد أحدث قياس منشور لتغطية سجل الائتمان يحتفظ به هذا المورد، وهو تقرير ممارسة أنشطة الأعمال 2020 الصادر "
                     "عن البنك الدولي (بيانات جُمعت حتى مايو 2019؛ المدينة المشمولة: صنعاء؛ وقد توقفت السلسلة لاحقًا)، مع تدشين "
                     "سجل المتعثرين في التسلسل الزمني؛ وهو مرجع تاريخي، لا خط أساس للسجل الذي دشّنه البنك المركزي اليمني – عدن "
                     "في 2026."),
                    [], [DB20])
MA_ADD["MA-009"] = ((" UNICEF's releases give the programme's announced reach, not confirmed payments, and its channels in the "
                     "18th payment cycle, to mid-October 2024 (payment sites, mobile teams and home outreach, and an e-wallet "
                     "pilot), and announce that the 19th cycle, from 11 December 2024, would end the programme in its then-current "
                     "form. A May 2026 report on humanitarian multi-purpose cash assistance, a different programme, records from "
                     "one interview agents short of cash at cash-out during the Ramadan and Eid holiday period."),
                    (" وتعرض بيانات اليونيسف النطاق المعلن للبرنامج، لا الدفعات المؤكدة، وقنواته في دورة الدفع 18 حتى منتصف "
                     "أكتوبر 2024 (مواقع الصرف، والفرق المتنقلة وخدمات الوصول إلى المنازل، وتجربة للمحفظة الإلكترونية)، وتعلن أن "
                     "دورة الدفع 19، التي تبدأ في 11 ديسمبر 2024، تنهي البرنامج بصيغته القائمة آنذاك. ويرصد تقرير صدر في مايو 2026 "
                     "عن المساعدات النقدية الإنسانية متعددة الأغراض، وهي برنامج مختلف، نقلًا عن مقابلة واحدة، نقص النقد لدى "
                     "الوكلاء عند السحب خلال فترة عطلة رمضان والعيد."),
                    [], [UNI10, UNI12, PRESS])

for _r in RPW_ROWS:   # B2: a CauseWay computation from the World Bank's quotes, not a published corridor average
    _r["calculation_state"] = "CAUSEWAY_SIMPLE_MEAN_OF_SOURCE_QUOTES"
    _r["evidence_type"] = "DERIVED_FROM_PRIMARY_OFFICIAL_CORRIDOR_QUOTES"
    _r["universe"] = "RPW quote observations in the dataset for the specified corridor and send amount"
RPW_VS = RPW_VS + [
    vs("4%", "v", "READ", RPWUS, "same dataset, period 2025_3Q, USA to YEM, Western Union, instrument cash, access point agent: "
       "'cc1 total cost %' = 4" + V5),
    vs("7.5%", "v", "READ", RPWUS, "same dataset, period 2025_3Q, USA to YEM, Walmart2World, instrument cash, access point agent: "
       "'cc1 total cost %' = 7.5" + V5),
]
SECTIONS_RPW = [x for x in SECTIONS_RPW if not (x[1] in ("/remittances/", "/readings/how-money-reaches-households/"))] + [
    ("6C-3", "/remittances/", 5, "en", "body", "For UAE–Yemen they were 7.53% and 5.62%.",
     "For UAE–Yemen they were 7.53% and 5.62%. For United States–Yemen, computed here from the World Bank's quotes, they "
     "were 3.92% and 2.30%; that average mixes card, bank-account and cash products, and the two quotes for cash paid in at an "
     "agent were 4% and 7.5% at US$200."),
    ("6C-3", "/remittances/", 5, "ar", "body", "أما ممر الإمارات–اليمن فبلغ 7.53% و5.62% على التوالي.",
     "أما ممر الإمارات–اليمن فبلغ 7.53% و5.62% على التوالي. وبلغ متوسطا ممر الولايات المتحدة–اليمن، محسوبين هنا من عروض "
     "أسعار البنك الدولي، 3.92% و2.30%؛ ويمزج هذا المتوسط منتجات تُدفع بالبطاقة أو من حساب مصرفي أو نقدًا، وبلغ العرضان الخاصان "
     "بالدفع نقدًا لدى وكيل 4% و7.5% عند إرسال 200 دولار."),
    ("6C-3", "/readings/how-money-reaches-households/", 6, "en", "body",
     "one of the two corridors held here (the other, from the United Arab Emirates, averaged 7.53%, lifted by a single high "
     "quote).",
     "one of the three corridors held here (from the United Arab Emirates the average was 7.53%, lifted by a single high quote, "
     "and from the United States 3.92%, computed here from the World Bank's quotes and mixing card, bank-account and cash "
     "products)."),
    ("6C-3", "/readings/how-money-reaches-households/", 6, "ar", "body",
     "وهو أحد ممرّين تتضمنهما قاعدة الأدلة هذه (وبلغ متوسط الممر الآخر، من الإمارات، 7.53%، ويرفعه عرض سعر مرتفع واحد).",
     "وهو أحد ثلاثة ممرات تتضمنها قاعدة الأدلة هذه (وبلغ المتوسط من الإمارات 7.53%، ويرفعه عرض سعر مرتفع واحد، ومن الولايات "
     "المتحدة 3.92%، محسوبًا هنا من عروض أسعار البنك الدولي ويمزج منتجات تُدفع بالبطاقة أو من حساب مصرفي أو نقدًا)."),
    ("6C-3", "/methodology/", 4, "en", "body", "This resource has no current Yemen evidence on service reliability,",
     "This resource has no systematic current Yemen evidence on service reliability,"),
    ("6C-3", "/methodology/", 4, "ar", "body", "ولا يملك هذا المورد أدلة يمنية حديثة عن موثوقية الخدمات،",
     "ولا يملك هذا المورد أدلة يمنية حديثة ومنهجية عن موثوقية الخدمات،"),
]

REF_REG_012 = ("Commercial and specialised banks report credit exposures from YER 500,000 on Form No. 6 by the 15th of the "
               "following month (publications/149, which cites Law No. 38 of 1998 on banks, Governor's Decision No. 4 of 1991, "
               "whose text is not published, Circular No. 33379 of 14 August 1991 and Circular No. 54064 of 2 July 2006). "
               "Publications/150 bars any loan or financing to any customer, whatever its size, before an enquiry to the Credit "
               "and Banking Risk Department, and any credit or financing before checking that the customer's name is not on the "
               "notification list under Circular No. 2 of 2000. Web posting is not an issue date.")
YSC030_FACT = (" The 5 August 2026 announcement cites no instrument (it refers only to unnamed regulatory controls) and publishes "
               "no coverage, threshold or record count.",
               " ولا يذكر إعلان 5 أغسطس 2026 أداة تنظيمية بعينها (إذ يكتفي بالإشارة إلى «ضوابط تنظيمية» دون تسميتها)، ولا ينشر "
               "تغطيةً ولا حدًّا أدنى ولا عدد سجلات.")
YSC030_IMPL = ("The registry sits alongside the credit-information rules CBY-Aden publishes. Its reporting rule has banks report "
               "credit exposures on Form No. 6 and cites Law No. 38 of 1998 on banks, Governor's Decision No. 4 of 1991, Circular "
               "No. 33379 of 14 August 1991 and Circular No. 54064 of 2 July 2006; its enquiry rule bars any loan or financing, "
               "whatever its size, before an enquiry, and any credit or financing before checking that the customer's name is not "
               "on the notification list under Circular No. 2 of 2000, without saying who keeps that list or what it holds. The "
               "announcement does not link the registry to these rules.",
               "يقع السجل إلى جانب قواعد معلومات الائتمان التي ينشرها البنك المركزي اليمني – عدن. فقاعدة الإبلاغ تُلزم البنوك "
               "بالإبلاغ عن التعرضات الائتمانية على الاستمارة رقم (6)، وتستند إلى القانون رقم (38) لسنة 1998 بشأن البنوك، وقرار "
               "المحافظ رقم (4) لسنة 1991، والتعميم رقم (33379) بتاريخ 14 أغسطس 1991، والتعميم رقم (54064) بتاريخ 2 يوليو 2006؛ "
               "وتحظر قاعدة الاستعلام منح أي قرض أو تمويل، مهما كان حجمه، قبل الاستعلام عن العميل، ومنح أي ائتمان أو تمويل قبل "
               "التأكد من عدم ورود اسمه في قائمة الإشعار وفقًا للمنشور الدوري رقم (2) لعام 2000، من دون أن تذكر من يحتفظ بهذه "
               "القائمة أو ما تتضمنه. ولا يربط الإعلان السجل بهذه القواعد.")
YSC030_REL = (" The most recent published measure this resource holds, the World Bank's Doing Business 2020 (data collected to May "
              "2019; city covered: Sana'a; series since discontinued), recorded 216,245 individuals and firms in the public credit "
              "registry (211,476 individuals and 4,769 firms), which it expressed as 1.3% of the adult population, and none in a "
              "private credit bureau (0%); it is a historical reference, not a baseline for this registry.",
              " وأحدث قياس منشور يحتفظ به هذا المورد هو تقرير ممارسة أنشطة الأعمال 2020 الصادر عن البنك الدولي (بيانات جُمعت حتى "
              "مايو 2019؛ المدينة المشمولة: صنعاء؛ وقد توقفت السلسلة لاحقًا)، وقد سجّل 216,245 فردًا ومنشأة في سجل الائتمان العام "
              "(211,476 فردًا و4,769 منشأة)، وعبّر عن ذلك بنسبة 1.3% من السكان البالغين، ولم يسجل أحدًا في مكتب ائتمان خاص "
              "(0%)؛ وهو مرجع تاريخي، لا خط أساس لهذا السجل.")
YSC030_VS = YSC030_VS + [
    vs("211,476", "v", "READ", DB20, DB20L + ", p.30, Coverage: Credit registry, Number of individuals 211,476" + V4),
    vs("4,769", "v", "READ", DB20, DB20L + ", p.30, Coverage: Credit registry, Number of firms 4,769" + V4),
]

IFAD_EN = ("An evaluation of IFAD's Yemen programme from 1993 to 2010 by IFAD's Independent Office of Evaluation (2011) reports, "
           "on the evaluation team's estimates from the information held by the Cooperative and Agriculture Credit Bank (CACB), "
           "that in the completed projects credit lines disbursed US$4.165 million, 31% of the US$13.37 million provided, to "
           "3,723 clients, 6% of the 58,867 planned; repayment rates ranged from 31% to 64%. In one project area, Raymah, fewer "
           "than 1% of the farmers in the project area received financing during the project (assuming 48,000 households in the "
           "area), and in the Southern Governorates the rural finance component was, in the evaluators' words, not really "
           "implemented at all. The evaluation reports that poor households were said to be reluctant to borrow from the CACB, "
           "the government bank the projects depended on, because of its collateral requirements, high transaction costs and "
           "lengthy approval procedures and a reluctance to deal with an institution seen as charging interest, contrary to "
           "Islamic precepts; that women, who did not generally own land, had little access to its credit, as was also true of "
           "sharecroppers; and that two branches built with IFAD support, at Al-Jabeen in Raymah and Sayhut in Al-Mahara, were "
           "not located near commercial centres.")
IFAD_AR = ("يورد تقييم لبرنامج الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن من 1993 إلى 2010، أجراه مكتب التقييم المستقل التابع "
           "للصندوق (2011)، استنادًا إلى تقديرات فريق التقييم من المعلومات المتاحة لدى بنك التسليف التعاوني والزراعي، أن خطوط "
           "الائتمان في المشروعات المكتملة صرفت 4.165 مليون دولار أمريكي، أي 31% من 13.37 مليون دولار خُصصت لها، إلى 3,723 عميلًا، "
           "أي 6% من 58,867 عميلًا كان مخططًا الوصول إليهم؛ وتراوحت معدلات السداد بين 31% و64%. وفي منطقة مشروع واحدة، هي ريمة، حصل "
           "أقل من 1% من المزارعين في منطقة المشروع على تمويل خلال فترة المشروع (على افتراض وجود 48,000 أسرة في المنطقة)، ولم "
           "يُنفَّذ مكوّن التمويل الريفي في المحافظات الجنوبية فعليًا على الإطلاق، بتعبير المقيّمين. ويذكر التقييم أن الأسر الفقيرة قيل "
           "إنها كانت تُحجم عن الاقتراض من بنك التسليف التعاوني والزراعي، وهو البنك الحكومي الذي اعتمدت عليه المشروعات، بسبب "
           "متطلبات الضمانات وارتفاع تكاليف المعاملات وطول إجراءات الموافقة والإحجام عن التعامل مع مؤسسة يُنظر إليها على أنها تتقاضى "
           "فائدة، خلافًا لأحكام الشريعة الإسلامية؛ وأن النساء، اللواتي لم يكنّ في الغالب يملكن أرضًا، كان وصولهن إلى ائتمانه "
           "محدودًا، وكذلك المزارعون العاملون بنظام المشاركة في المحصول؛ وأن فرعين بُنيا بدعم من الصندوق، في الجبين بريمة وفي سيحوت "
           "بالمهرة، لم يُقاما قرب المراكز التجارية.")
IFAD_RECORD["summary_en"], IFAD_RECORD["summary_ar"] = IFAD_EN, IFAD_AR
IFAD_RECORD["title_en"] = ("Rural credit in IFAD-financed projects in Yemen, 1993 to 2010: an evaluation by IFAD's Independent "
                           "Office of Evaluation (2011)")
IFAD_RECORD["title_ar"] = ("الائتمان الريفي في المشروعات التي موّلها الصندوق الدولي للتنمية الزراعية (إيفاد) في اليمن، 1993 إلى 2010: "
                           "تقييم أجراه مكتب التقييم المستقل التابع للصندوق (2011)")
IFAD_META = ("An evaluation of IFAD's Yemen programme, 1993 to 2010: credit reached 3,723 clients in completed projects, 6% of "
             "those planned. Historical findings for project areas, not a measure of access today.",
             "تقييم لبرنامج إيفاد في اليمن، 1993 إلى 2010: وصل الائتمان إلى 3,723 عميلًا في المشروعات المكتملة، أي 6% من المخطط. "
             "نتائج تاريخية لمناطق مشروعات، لا مقياس للوصول اليوم.")
CWR010_PERIOD = (" · UNICEF press releases (October and December 2024) · Cash Consortium of Yemen survey of January 2024 (posted "
                 "online November 2024)",
                 " · بيانان صحفيان لليونيسف (أكتوبر وديسمبر 2024) · مسح لتحالف النقد في اليمن أُجري في يناير 2024 (نُشر على "
                 "الإنترنت في نوفمبر 2024)")


# ==================================================================================================================== Confirmation-pass revisions
# Domain confirmation pass (ACCEPT after S-1 and S-2; NITs N-1 to N-6 applied).
def _r(t, old, new):
    assert t.count(old) == 1, (old[:60], t.count(old))
    return t.replace(old, new)


DEBT = (_r(_r(DEBT[0],
              "Two Cash Consortium of Yemen studies of cash-assistance recipients, in sub-districts",
              "Two Cash Consortium of Yemen studies of recipients of the Consortium partners' humanitarian cash assistance, a "
              "programme separate from the unconditional cash transfer, in sub-districts"),
           "about 47% of the households paid in those 30 days and about 30% of those not paid.",
           "about 47% of households that had received a transfer in those 30 days and about 30% of those that had not."),
        _r(_r(DEBT[1],
              "وتشير دراستان لتحالف النقد في اليمن عن متلقي المساعدات النقدية، في مديريات فرعية",
              "وتشير دراستان لتحالف النقد في اليمن عن متلقي المساعدات النقدية الإنسانية التي يقدمها شركاء التحالف، وهي برنامج منفصل "
              "عن برنامج التحويلات النقدية غير المشروطة، في مديريات فرعية"),
           "نحو 47% من الأسر التي تلقت دفعة خلال تلك الأيام الـ30، ونحو 30% من الأسر التي لم تتلقَّ.",
           "نحو 47% من الأسر التي تلقت تحويلًا خلال تلك الأيام الـ30، ونحو 30% من الأسر التي لم تتلقَّه."))
INF_METHOD = ((INF_METHOD[0][0],
               "and informal firms' account holding, business-related loan or debt and main sources of financing, Figures 114 to "
               "116 (p. 151); the informal sample of 217 firms is stated on pp. 139 and 141, and the figures print no base, but "
               "each value is a whole number of firms out of 217 (CauseWay's check)."),
              (INF_METHOD[1][0],
               "وامتلاك المنشآت غير الرسمية للحسابات وقروضها أو ديونها المرتبطة بالنشاط ومصادر تمويلها الرئيسية، الأشكال من 114 إلى "
               "116 (ص 151)؛ وترد عينة المنشآت غير الرسمية البالغة 217 منشأة في الصفحتين 139 و141، ولا تطبع الأشكال قاعدتها، لكن كل "
               "قيمة فيها عدد صحيح من المنشآت من أصل 217 (بحسب تحقق CauseWay)."))
_CASH_BODY = _r(_r(_CASH_BODY, "and says the problems eased after the period of high demand.",
                   "and says that liquidity problems for MPCA programmes eased after the period of high demand."), "", "") \
    if False else _r(_CASH_BODY, "and says the problems eased after the period of high demand.",
                     "and says that liquidity problems for MPCA programmes eased after the period of high demand.")
_CASH_BODY_AR = _r(_CASH_BODY_AR, "ويذكر أن المشكلات خفّت بعد فترة ارتفاع الطلب.",
                   "ويذكر أن مشكلات السيولة في برامج المساعدات النقدية متعددة الأغراض خفّت بعد فترة ارتفاع الطلب.")
CASH_READING = ("The same May 2026 report adds an observation on cash-out. It says that " + _CASH_BODY,
                "ويضيف التقرير نفسه الصادر في مايو 2026 ملاحظة عن السحب النقدي، إذ يذكر أن " + _CASH_BODY_AR)
CASH_RECORD = ("On cash-out, a Cash Consortium of Yemen report of May 2026 says that " + _CASH_BODY,
               "وعن السحب النقدي، يذكر تقرير لتحالف النقد في اليمن صدر في مايو 2026 أن " + _CASH_BODY_AR)
IFAD_EN = _r(IFAD_EN, "and that two branches built with IFAD support, at", "and that two of the branches IFAD helped the CACB build, at")
IFAD_AR = _r(IFAD_AR, "وأن فرعين بُنيا بدعم من الصندوق،", "وأن فرعين من الفروع التي ساعد الصندوق البنك على بنائها،")
IFAD_RECORD["summary_en"], IFAD_RECORD["summary_ar"] = IFAD_EN, IFAD_AR
_m9 = MA_ADD["MA-009"]
MA_ADD["MA-009"] = (_r(_m9[0], " UNICEF's releases give the programme's announced reach, not confirmed payments, and its channels",
                       " UNICEF's releases on the World Bank-funded unconditional cash transfer give its announced reach, not "
                       "confirmed payments, and its channels"),
                    _r(_m9[1], " وتعرض بيانات اليونيسف النطاق المعلن للبرنامج، لا الدفعات المؤكدة، وقنواته",
                       " وتعرض بيانات اليونيسف عن برنامج التحويلات النقدية غير المشروطة الممول من البنك الدولي نطاقه المعلن، لا "
                       "الدفعات المؤكدة، وقنواته"), _m9[2], _m9[3])
_m5 = MA_ADD["MA-005"]
MA_ADD["MA-005"] = (_r(_m5[0], "a May 2026 report on humanitarian multi-purpose cash assistance records",
                       "a May 2026 Cash Consortium of Yemen report, in its section on humanitarian multi-purpose cash assistance, "
                       "records"),
                    _r(_m5[1], "إذ يرصد تقرير صدر في مايو 2026 عن المساعدات النقدية الإنسانية متعددة الأغراض افتقار",
                       "إذ يرصد تقرير لتحالف النقد في اليمن صدر في مايو 2026، في قسمه عن المساعدات النقدية الإنسانية متعددة الأغراض، "
                       "افتقار"), _m5[2], _m5[3])
RPW_ENCODING2 = ("Provider and quote counts are not held and are not drawn.",
                 "Quote counts are given in the record's limitations and are not drawn.")


# ==================================================================================================================== Arabic-lens revisions
# ARABIC_6E.md: B1, B2, SF-1 to SF-7, N-1, N-3 to N-8, N-10, N-11 applied; N-2 already met by the confirmation-pass change;
# N-9 kept (the field's own style, «ص 143»).
UCT = (UCT[0], _r(UCT[1], "والأسر التي يشملها البرنامج،", "والأسر التي شملها البرنامج،"))
_CASH_BODY_AR = _r(_CASH_BODY_AR, "إلى ما يكفي من النقد، فامتد الانتظار أربع ساعات إلى خمس.",
                   "إلى ما يكفي من النقد، مع انتظار امتد أربع ساعات إلى خمس.")
CASH_READING = (CASH_READING[0], "ويضيف التقرير نفسه الصادر في مايو 2026 ملاحظة عن السحب النقدي، إذ يذكر أن " + _CASH_BODY_AR)
CASH_RECORD = (CASH_RECORD[0], "وعن السحب النقدي، يذكر تقرير لتحالف النقد في اليمن صدر في مايو 2026 أن " + _CASH_BODY_AR)
_d = DEBT[1]
for _o, _n in (("في حد ذاته دليلًا على فشل التحويل", "في حد ذاته علامةً على فشل التحويل"),
               ("في مديريات فرعية تضعها الدراستان", "في عُزَل تضعها الدراستان"),
               ("(مع السماح بإجابة واحدة)", "(إجابة واحدة فقط)"),
               ("ونشره مستضيفه على الإنترنت", "ونُشر على موقع الجهة المستضيفة له")):
    _d = _r(_d, _o, _n)
DEBT = (DEBT[0], _d)
_m9 = MA_ADD["MA-009"]
MA_ADD["MA-009"] = (_m9[0], _r(_r(_m9[1], "وتعرض بيانات اليونيسف عن برنامج", "وتعرض البيانات الصحفية لليونيسف عن برنامج"),
                               "عند السحب خلال", "عند السحب النقدي خلال"), _m9[2], _m9[3])
_m1 = MA_ADD["MA-001"]
MA_ADD["MA-001"] = (_m1[0], _r(_m1[1], "فلا تتوافر عنه إلا ملاحظات محلية لا خط أساس", "فتوجد عنه ملاحظات محلية، لا خط أساس"),
                    _m1[2], _m1[3])
_m4 = MA_ADD["MA-004"]
MA_ADD["MA-004"] = (_m4[0], _r(_m4[1], "أما الضمانات والشروط", "أما الضمانات المطلوبة من المقترضين وشروط الإقراض"),
                    _m4[2], _m4[3])
for _r_ in RPW_ROWS:
    _r_["caveat_ar"] = _r(_r_["caveat_ar"], "متوسطَي السعودية والإمارات المنشورين", "متوسطات السعودية والإمارات المنشورة")
YSC030_IMPL = (YSC030_IMPL[0], _r(YSC030_IMPL[1], "وتستند إلى القانون رقم (38)", "وتشير إلى القانون رقم (38)"))
IFAD_EN = _r(IFAD_EN, "seen as charging interest, contrary to Islamic precepts;", "seen as charging interest contrary to Islamic precepts;")
IFAD_AR = _r(_r(IFAD_AR, "على أنها تتقاضى فائدة، خلافًا لأحكام الشريعة الإسلامية؛", "على أنها تتقاضى فائدة تخالف أحكام الشريعة الإسلامية؛"),
             "ويذكر التقييم أن الأسر الفقيرة قيل إنها كانت تُحجم", "ويذكر التقييم أنه قيل إن الأسر الفقيرة كانت تُحجم")
IFAD_RECORD["summary_en"], IFAD_RECORD["summary_ar"] = IFAD_EN, IFAD_AR
_ma = IFAD_RECORD["method_ar"]
for _p in ("40", "33", "3"):
    _ma = _r(_ma, f"(ص. {_p})", f"(ص. {_p} بحسب الترقيم المطبوع)")
IFAD_RECORD["method_ar"] = _ma
PEOPLE_S6 = (PEOPLE_S6[0], (PEOPLE_S6[1][0], _r(PEOPLE_S6[1][1],
             "؛ أما الشراء بالدَّين من المتاجر، الذي ترصده دراسات محلية عن متلقي المساعدات النقدية، فليس من بينها.",
             ". ولا يدخل فيها الشراء بالدَّين من المتاجر، الذي ترصده دراسات محلية عن متلقي المساعدات النقدية.")))
INF_METHOD = ((INF_METHOD[0][0], _r(INF_METHOD[0][1], "but each value is a whole number of firms out of 217",
                                    "but each value corresponds to a whole number of firms out of 217")),
              (INF_METHOD[1][0], _r(INF_METHOD[1][1], "لكن كل قيمة فيها عدد صحيح من المنشآت من أصل 217",
                                    "لكن كل قيمة فيها تقابل عددًا صحيحًا من المنشآت من أصل 217")))
REF_REG_012 = _r(REF_REG_012, "to any customer, whatever its size,", "to any customer, whatever the size of the loan or financing,")
