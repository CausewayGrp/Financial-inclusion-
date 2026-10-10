# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-2A: the Global Findex corrections that need an original (brief v5 W3b; CR-01, CR-02, CR-14).
English and Arabic change together; the conditional Arabic register rows tied to these findings ride with them.

  python3 close_2a.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Read in the originals on 10 October 2026 (audit/close_out/w0/A1_findex_wb.md):
- CR-01 CONFIRMED. The World Bank's open series give fiaccount.t.d = account.t.d = 11.9033656433415 for Yemen (2022)
  and an empty mobileaccount.t.d (all splits); the public DDI pages of the Yemen study (Microdata Library catalog
  5862) show no valid case for any mobile-money item (fin13a-d, fin17a1, fin34b, fin39b, fin43b) and the Yemen file
  has no mobile-money account variable. No World Bank sentence says "not asked"; the register's own condition for
  AR-001 names exactly this public evidence (DDI variable pages; fiaccount = account; mobileaccount null) as the
  confirmation, so AR-001 and AR-042 take their new_ar, and the evidence is written into CLM-001's method.
- CR-02 CONFIRMED. The Global Findex Database 2021, Appendix A, Table A.1 (printed p.17), Yemen row: 1,000
  interviews, design effect 1.9, margin of error 4.3 (the maximum, at a reported 50%; footnote c gives the formula
  sqrt(0.25/N) x 1.96 x sqrt(DE)). "The World Bank publishes no standard error or confidence interval" is false.
  Brief v5: re-state the intervals only by applying the publisher's design effect to the published estimates,
  labelled "computed by CauseWay", or withdraw them; never recompute from microdata. So:
    * national shares (n = 1,000, published by the World Bank): 95% interval = p +/- 1.96 x sqrt(1.9) x
      sqrt(p(1-p)/1,000) on the World Bank's unrounded value — account 9.1-14.7 (+/-2.8), saved 18.1-25.2,
      borrowed 47.0-55.6, digital payment 6.8-11.8;
    * group shares and the differences between groups: withdrawn. The World Bank publishes its design effect and
      sample size for the whole sample only; this resource does not compute group intervals. The gap stays as the
      arithmetic difference of two published shares, with no claim of significance (as U1 requires).
  ED-034 (/methodology/ section 7): the register's Option A wording (rescaling intervals computed from the
  respondent file) is overtaken by brief v5; its text is written here to the v5 rule, and "may be wider in reality,
  never narrower" is deleted as the register requires in every case.
  AR-NEW-001 (/rights/ section 6): the register's grammar fix sits in the microdata sentence, which its condition
  says to rewrite when CR-02 changes the intervals. CLOSE-1 changed the same cell (D3), so the exact-match check runs
  against the 2ddbfb61 text with the D3 change applied; the merge is recorded in PROGRESS.md.
- CR-14 VERIFIED, no change. 35.2% is the World Bank's own aggregate: the open API gives country LIC,
  account.t.d, 2021 = 35.1821646573129, and GlobalFindexDatabase2025.csv carries the "Low income" row the record
  already cites, with its 19 economies listed in CLM-001's value states. The brief's "31% / 33%" was not found.
  AR-042's placeholder resolves to the World Bank wording, unchanged.
Gate: FC-MOE (which asserted the microdata-derived intervals) is replaced by CO-G03 for the new rule.
"""
import json, math, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import (Session, Table, TxError, refresh_self_counts, register_rows, register_cell,  # noqa: E402
                       apply_register_ar, apply_register_en)

F = "CLOSE-2A"
DATE = "10 October 2026"
METH_URL = ("https://thedocs.worldbank.org/en/doc/fe026d04da1eb78f5ce8bb5e1529d60b-0430062023/original/"
            "Findex2021-22-Methodology.pdf")
METH_LOC = ("The Global Findex Database 2021, Appendix A 'Survey Methodology', Table A.1, Yemen row, printed p.17 ("
            + METH_URL.replace("https://", "") + "): 1,000 interviews; design effect 1.9; margin of error 4.3 "
            "(footnote c: maximum, at a reported 50%, sqrt(0.25/N) x 1.96 x sqrt(DE)); read 10 October 2026")
DE, N = 1.9, 1000
P = {"account": 11.9033656433415, "saved": 21.6445272422787, "borrowed": 51.2811034475895, "digital": 9.33455931917802}


def moe(p):
    return 1.96 * math.sqrt(DE) * math.sqrt(p / 100 * (1 - p / 100) / N) * 100


IV = {k: (round(p - moe(p), 1), round(p + moe(p), 1), round(moe(p), 1)) for k, p in P.items()}
EXPECT = {"account": (9.1, 14.7, 2.8), "saved": (18.1, 25.2, 3.5), "borrowed": (47.0, 55.6, 4.3), "digital": (6.8, 11.8, 2.5)}
if IV != EXPECT:
    raise SystemExit(f"interval arithmetic changed: {IV}")


def comp_loc(row):
    return ("CauseWay computation, close-out CR-02 (" + DATE + "): the World Bank's published unrounded value p "
            "(api.worldbank.org/v2, source 28) +/- 1.96 x sqrt(1.9) x sqrt(p(1-p)/1,000), the World Bank's own "
            "margin-of-error formula with its published design effect for the survey (Findex 2021 Appendix A, "
            "Table A.1, footnote c); 25_FINDEX_BASELINE row " + row + "; no respondent-level data used")


def vs_read(t):
    return OrderedDict([("t", t), ("k", "v"), ("s", "READ"), ("src", "SRC-WB-FINDEX-001"), ("loc", METH_LOC)])


def vs_derived(t, row):
    return OrderedDict([("t", t), ("k", "v"), ("s", "DERIVED"), ("src", "SRC-WB-FINDEX-AGG-2022"), ("loc", comp_loc(row))])


# ------------------------------------------------------------------------------------------------ 06 text edits
# (record, field, old substring, new substring) — each old substring must occur exactly once in the cell
E06 = [
    # CR-01 — CLM-001: definition, method (the evidence), limitations, change trigger
    ("CLM-001", "definition_en",
     "or who report personally using a mobile-money service in the past 12 months (2021 Findex wave, fieldwork 7 November 2022 to 9 January 2023).",
     "or who report personally using a mobile-money service in the past 12 months (2021 Findex wave, fieldwork 7 November 2022 to 9 January 2023). In Yemen's survey the mobile-money questions were not asked, so the figure reflects accounts at banks and other financial institutions."),
    ("CLM-001", "definition_ar",
     "أو باستخدامهم الشخصي خدمة أموال عبر الهاتف المحمول خلال الاثني عشر شهرًا السابقة، كما قيس في موجة 2021 من مسح Findex (العمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023).",
     "أو باستخدامهم الشخصي خدمة أموال عبر الهاتف المحمول خلال الاثني عشر شهرًا السابقة، كما قيس في موجة 2021 من مسح Findex (العمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023). ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تعكس النسبة الحسابات لدى البنوك والمؤسسات المالية الأخرى."),
    ("CLM-001", "method_en",
     "weighted by their adult populations.",
     "weighted by their adult populations. In Yemen's survey the mobile-money questions were not asked: in the World Bank's public data for the study, none of them has a valid answer, the World Bank's mobile-money account series has no value for Yemen, and its series for accounts at a financial institution equals its account-ownership series (11.9%)."),
    ("CLM-001", "method_ar",
     "مرجّحًا بعدد البالغين في كل منها.",
     "مرجّحًا بعدد البالغين في كل منها. ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن: ففي البيانات العامة التي نشرها البنك الدولي لهذه الدراسة لا توجد إجابة صالحة عن أي منها، وسلسلة البنك الدولي الخاصة بحسابات الأموال عبر الهاتف لا تتضمن أي قيمة لليمن، وسلسلته الخاصة بالحساب لدى مؤسسة مالية مساوية لسلسلة امتلاك الحساب (11.9%)."),
    ("CLM-001", "limitations_en",
     "It is not the share of adults with a bank account: accounts at other financial institutions and personal use of a mobile-money service also count.",
     "It is not the share of adults with a bank account only: accounts at other financial institutions also count. Personal use of a mobile-money service, which the World Bank's definition also counts, was not measured in Yemen's survey."),
    ("CLM-001", "limitations_ar",
     "وليست نسبة من يملكون حسابًا مصرفيًا فحسب، إذ تُحتسب أيضًا الحسابات لدى المؤسسات المالية الأخرى والاستخدام الشخصي لخدمة أموال عبر الهاتف المحمول.",
     "وليست نسبة من يملكون حسابًا مصرفيًا فحسب، إذ تُحتسب أيضًا الحسابات لدى المؤسسات المالية الأخرى. أما الاستخدام الشخصي لخدمة أموال عبر الهاتف المحمول، الذي يشمله تعريف البنك الدولي أيضًا، فلم يُقس في مسح اليمن."),
    ("CLM-001", "change_trigger_en",
     "or the conditions for public use change.",
     "or the conditions for public use change. A later survey of Yemen that asks the mobile-money questions may show a rise caused by the change of questionnaire, not by a real change in account ownership."),
    ("CLM-001", "change_trigger_ar",
     "أو تغير شروط الاستخدام العام.",
     "أو تغير شروط الاستخدام العام. وقد يُظهر مسح لاحق لليمن يطرح أسئلة خدمات الأموال عبر الهاتف ارتفاعًا سببه تغيّر الاستبيان، لا تغيّر فعلي في امتلاك الحساب."),
    # CR-01 — CLM-027: the 2011 comparator and the later definition
    ("CLM-027", "limitations_en",
     "The 2011 comparator counts accounts at financial institutions only, which differs from the later account definition that also counts mobile-money use;",
     "The 2011 comparator counts accounts at financial institutions only; the later definition also counts mobile-money use, but Yemen's 2021 study did not ask the mobile-money questions, so its 11.9% also reflects accounts at financial institutions;"),
    ("CLM-027", "limitations_ar",
     "يقتصر مقياس 2011 على الحسابات لدى المؤسسات المالية، ويختلف بذلك عن تعريف الحساب اللاحق الذي يشمل أيضًا استخدام خدمات الأموال عبر الهاتف المحمول؛",
     "يقتصر مقياس 2011 على الحسابات لدى المؤسسات المالية؛ ويشمل التعريف اللاحق أيضًا استخدام خدمات الأموال عبر الهاتف المحمول، لكن دراسة اليمن لعام 2021 لم تطرح أسئلة هذه الخدمات، فتعكس نسبة 11.9% فيها كذلك الحسابات لدى المؤسسات المالية؛"),
    # CR-01 — VIS-FINDEX-GAPS: summary and definition
    ("VIS-FINDEX-GAPS", "summary_en",
     "had an account at a financial institution or with a mobile-money provider. Within the same wave:",
     "had an account at a financial institution (the survey did not ask the mobile-money questions). Within the same wave:"),
    ("VIS-FINDEX-GAPS", "summary_ar",
     "ممن يملكون حسابًا لدى مؤسسة مالية أو لدى مقدم خدمة أموال عبر الهاتف المحمول 11.9%.",
     "ممن يملكون حسابًا لدى مؤسسة مالية 11.9% (لم يطرح المسح أسئلة خدمات الأموال عبر الهاتف)."),
    ("VIS-FINDEX-GAPS", "definition_en",
     "for all adults and by sex, household income, education and age (2021 Findex wave, fieldwork 7 November 2022 to 9 January 2023).",
     "for all adults and by sex, household income, education and age (2021 Findex wave, fieldwork 7 November 2022 to 9 January 2023). In Yemen's survey the mobile-money questions were not asked, so the values reflect accounts at financial institutions."),
    ("VIS-FINDEX-GAPS", "definition_ar",
     "لجميع البالغين وبحسب الجنس ودخل الأسرة والتعليم والعمر (موجة 2021 من مسح Findex، والعمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023).",
     "لجميع البالغين وبحسب الجنس ودخل الأسرة والتعليم والعمر (موجة 2021 من مسح Findex، والعمل الميداني من 7 نوفمبر 2022 إلى 9 يناير 2023). ولم تُطرح أسئلة خدمات الأموال عبر الهاتف في مسح اليمن، لذلك تعكس القيم الحسابات لدى المؤسسات المالية."),
    # CR-02 — VIS-FINDEX-GAPS: method and limitations
    ("VIS-FINDEX-GAPS", "method_en",
     "The 95% intervals shown with these values are derived by this resource from the survey's own weights (a design-based interval for a weighted share), not published by the World Bank.",
     "The margin of error of the figure for all adults is computed by CauseWay with the World Bank's own formula and the design effect the World Bank publishes for the survey; no interval is computed for the groups or for the differences."),
    ("VIS-FINDEX-GAPS", "method_ar",
     "وفترات الثقة 95% المعروضة مع هذه القيم يستخرجها هذا المورد من أوزان المسح نفسها (فترة قائمة على تصميم المسح لنسبة موزونة)، ولم ينشرها البنك الدولي.",
     "وتحتسب CauseWay هامش الخطأ للقيمة الخاصة بجميع البالغين بمعادلة البنك الدولي نفسها وبأثر التصميم الذي ينشره البنك الدولي للمسح؛ ولا تُحتسب فترة ثقة للفئات ولا للفروق."),
    ("VIS-FINDEX-GAPS", "limitations_en",
     "The World Bank publishes no standard error or confidence interval with these values, so this resource derives them from the survey's own weights: on a sample of 1,000 respondents, and fewer in each group, the 95% margin of error is 2.2 points on the figure for all adults, between 2.2 and 3.9 points on each group's share, and between 4.0 and 4.6 points on each of the four differences. Each interval is printed with its figure on that figure's own record. The file open to researchers carries no sampling-unit identifier, so clustering is not captured and the true intervals may be wider, never narrower.",
     "For the whole sample of 1,000 interviews the World Bank publishes a design effect of 1.9 and a maximum margin of error of 4.3 percentage points at the 95% level, for a share of 50%. With that design effect, the margin of error on the figure for all adults (11.9%) is about 2.8 percentage points, computed by CauseWay. No interval is computed for the group shares or for the four differences: each group is a smaller sample, with a larger margin of error, and the World Bank publishes its design effect for the whole sample only. Small differences between groups should not be over-read."),
    ("VIS-FINDEX-GAPS", "limitations_ar",
     "ولا ينشر البنك الدولي مع هذه القيم خطأً معياريًا ولا فترة ثقة، لذلك يستخرجها هذا المورد من أوزان المسح نفسها: ففي عينة من 1,000 مستجيب، وبعدد أقل في كل فئة، يبلغ هامش الخطأ عند ثقة 95% نحو 2.2 نقطة على القيمة الخاصة بجميع البالغين، وبين 2.2 و3.9 نقطة على نسبة كل فئة، وبين 4.0 و4.6 نقطة على كل فرق من الفروق الأربعة. وتُعرض كل فترة مع قيمتها في سجل تلك القيمة. ولا يحمل الملف المتاح للباحثين معرّف وحدة المعاينة، لذلك لا تُحتسب آثار التجمّع العنقودي، وقد تكون الفترات الحقيقية أوسع لا أضيق.",
     "وينشر البنك الدولي للعينة كلها (1,000 مقابلة) أثر تصميم قدره 1.9 وهامش خطأ أقصى قدره 4.3 نقطة مئوية عند مستوى ثقة 95% لنسبة قدرها 50%. وبأثر التصميم هذا يبلغ هامش الخطأ في القيمة الخاصة بجميع البالغين (11.9%) نحو 2.8 نقطة مئوية، من احتساب CauseWay. ولا تُحتسب فترة ثقة لنسب الفئات ولا للفروق الأربعة: فكل فئة عينةٌ أصغر، وهامش خطئها أكبر، ولا ينشر البنك الدولي أثر التصميم إلا للعينة كلها. ولا ينبغي تحميل الفروق الصغيرة بين الفئات أكثر مما تحتمل."),
    # CR-02 — CLM-002: method and limitations (the gender gap)
    ("CLM-002", "method_en",
     "The 95% intervals shown with these values are derived by this resource from the survey's own weights (a design-based interval for a weighted share), not published by the World Bank.",
     "The gap is the arithmetic difference of the two published shares; no interval or test of significance is computed here for it or for the two shares."),
    ("CLM-002", "method_ar",
     "وفترات الثقة 95% المعروضة مع هذه القيم يستخرجها هذا المورد من أوزان المسح نفسها (فترة قائمة على تصميم المسح لنسبة موزونة)، ولم ينشرها البنك الدولي.",
     "والفجوة فرق حسابي بين النسبتين المنشورتين؛ ولا تُحتسب هنا فترة ثقة، ولا يُجرى اختبار دلالة، لها ولا للنسبتين."),
    ("CLM-002", "limitations_en",
     "The World Bank publishes no standard error or confidence interval with these values, so this resource derives them from the survey's own weights: on a sample of 1,000 respondents the 95% interval runs from 3.2% to 7.7% for women and from 14.6% to 22.1% for men, and from 8.5 to 17.3 points for the gap. The file open to researchers carries no sampling-unit identifier, so clustering is not captured and the true intervals may be wider, never narrower.",
     "The World Bank publishes a design effect (1.9) and a maximum margin of error (4.3 percentage points at the 95% level, for a share of 50%) for the whole sample of 1,000 interviews, not for women or men separately. Each group is a smaller sample, so its margin of error is larger; no interval is computed here for the two shares or the gap, and the gap should not be read as precise to a single percentage point."),
    ("CLM-002", "limitations_ar",
     "ولا ينشر البنك الدولي مع هذه القيم خطأً معياريًا ولا فترة ثقة، لذلك يستخرجها هذا المورد من أوزان المسح نفسها: ففي عينة من 1,000 مستجيب تمتد فترة الثقة 95% من 3.2% إلى 7.7% للنساء، ومن 14.6% إلى 22.1% للرجال، ومن 8.5 إلى 17.3 نقطة للفجوة. ولا يحمل الملف المتاح للباحثين معرّف وحدة المعاينة، لذلك لا تُحتسب آثار التجمّع العنقودي، وقد تكون الفترات الحقيقية أوسع لا أضيق.",
     "وينشر البنك الدولي أثر تصميم (1.9) وهامش خطأ أقصى (4.3 نقطة مئوية عند مستوى ثقة 95%، لنسبة قدرها 50%) للعينة كلها البالغة 1,000 مقابلة، لا للنساء والرجال كلٍّ على حدة. وكل فئة عينة أصغر، فهامش خطئها أكبر؛ ولا تُحتسب هنا فترة ثقة للنسبتين ولا للفجوة، ولا ينبغي قراءة الفجوة على أنها دقيقة إلى حدّ النقطة المئوية الواحدة."),
    # CR-02 — CLM-026: the three national intervals
    ("CLM-026", "method_en",
     "The 95% interval beside each is derived by this resource from the same weights (18.4% to 24.9% for saving, 47.1% to 55.5% for borrowing, 7.4% to 11.3% for digital payments); the World Bank publishes none.",
     "The 95% interval beside each is computed by CauseWay from the published value with the World Bank's own formula and the design effect the World Bank publishes for Yemen's survey (1.9, for a sample of 1,000 interviews; its maximum margin of error is 4.3 percentage points, for a share of 50%): 18.1% to 25.2% for saving, 47.0% to 55.6% for borrowing and 6.8% to 11.8% for digital payments."),
    ("CLM-026", "method_ar",
     "وفترة الثقة 95% بجانب كل قيمة يستخرجها هذا المورد من الأوزان نفسها (من 18.4% إلى 24.9% للادخار، ومن 47.1% إلى 55.5% للاقتراض، ومن 7.4% إلى 11.3% للمدفوعات الرقمية)؛ ولا ينشر البنك الدولي أي منها.",
     "وفترة الثقة 95% بجانب كل قيمة تحتسبها CauseWay من القيمة المنشورة بمعادلة البنك الدولي نفسها وبأثر التصميم الذي ينشره البنك الدولي لمسح اليمن (1.9، لعينة من 1,000 مقابلة؛ ويبلغ هامش الخطأ الأقصى 4.3 نقطة مئوية لنسبة قدرها 50%): من 18.1% إلى 25.2% للادخار، ومن 47.0% إلى 55.6% للاقتراض، ومن 6.8% إلى 11.8% للمدفوعات الرقمية."),
    # CR-02 — VIS-FINDEX-ACCESS-USE: the digital-payment interval
    ("VIS-FINDEX-ACCESS-USE", "summary_en",
     "(95% interval 7.4% to 11.3%)",
     "(95% interval 6.8% to 11.8%, computed by CauseWay)"),
    ("VIS-FINDEX-ACCESS-USE", "summary_ar",
     "(فترة ثقة 95% من 7.4% إلى 11.3%)",
     "(فترة ثقة 95% من 6.8% إلى 11.8%، من احتساب CauseWay)"),
    ("VIS-FINDEX-ACCESS-USE", "method_en",
     "The digital-payment share is the World Bank's own published value for the wave, reproduced from the respondent file, with its 95% interval derived from the survey weights.",
     "The digital-payment share is the World Bank's own published value for the wave; its 95% interval is computed by CauseWay from that value and the design effect the World Bank publishes for the survey."),
    ("VIS-FINDEX-ACCESS-USE", "method_ar",
     "ونسبة المدفوعات الرقمية هي القيمة التي نشرها البنك الدولي نفسه للموجة، وأُعيد احتسابها من ملف المستجيبين، مع استخراج فترة الثقة 95% من أوزان المسح.",
     "ونسبة المدفوعات الرقمية هي القيمة التي نشرها البنك الدولي نفسه للموجة، وتحتسب CauseWay فترة الثقة 95% لها من هذه القيمة ومن أثر التصميم الذي ينشره البنك الدولي للمسح."),
]
# 11_VISUAL_LIBRARY accessible summaries of VIS-FINDEX-GAPS carry the same sentence as its 06 summary
E11 = [
    ("VIS-FINDEX-GAPS", "accessible_summary_en",
     "had an account at a financial institution or with a mobile-money provider. Within the same wave:",
     "had an account at a financial institution (the survey did not ask the mobile-money questions). Within the same wave:"),
    ("VIS-FINDEX-GAPS", "accessible_summary_ar",
     "ممن يملكون حسابًا لدى مؤسسة مالية أو لدى مقدم خدمة أموال عبر الهاتف المحمول 11.9%.",
     "ممن يملكون حسابًا لدى مؤسسة مالية 11.9% (لم يطرح المسح أسئلة خدمات الأموال عبر الهاتف)."),
]
# value states: tokens retired, tokens added
VS = {
    "CLM-002": (["3.2%", "7.7%", "14.6%", "22.1%", "8.5", "17.3"],
                [vs_read("1.9"), vs_read("4.3"), vs_read("50%")]),
    "VIS-FINDEX-GAPS": (["2.2", "3.9", "4.0", "4.6"],
                        [vs_read("1.9"), vs_read("4.3"), vs_read("50%"), vs_derived("2.8", "CW-FINDEX-MOE-2022-001")]),
    "CLM-026": (["18.4%", "24.9%", "47.1%", "55.5%", "7.4%", "11.3%"],
                [vs_derived("18.1%", "CW-FINDEX-MOE-2022-015"), vs_derived("25.2%", "CW-FINDEX-MOE-2022-015"),
                 vs_derived("47.0%", "CW-FINDEX-MOE-2022-016"), vs_derived("55.6%", "CW-FINDEX-MOE-2022-016"),
                 vs_derived("6.8%", "CW-FINDEX-MOE-2022-017"), vs_derived("11.8%", "CW-FINDEX-MOE-2022-017"),
                 vs_read("1.9"), vs_read("4.3"), vs_read("50%"), vs_read("1,000")]),
    "VIS-FINDEX-ACCESS-USE": (["7.4%", "11.3%"],
                              [vs_derived("6.8%", "CW-FINDEX-MOE-2022-017"), vs_derived("11.8%", "CW-FINDEX-MOE-2022-017")]),
}

# ------------------------------------------------------------------------------------------------ 03 section edits
E03 = [
    # /people/ section 6: the three national intervals
    ("/people/", 6, "en", "(95% interval 18.4% to 24.9%)", "(95% interval 18.1% to 25.2%)"),
    ("/people/", 6, "en", "(47.1% to 55.5%)", "(47.0% to 55.6%)"),
    ("/people/", 6, "en", "(7.4% to 11.3%)", "(6.8% to 11.8%)"),
    ("/people/", 6, "en", "The intervals are derived by this resource from the survey's own weights; the World Bank publishes none.",
     "The intervals are computed by CauseWay from these published values with the design effect the World Bank publishes for Yemen's survey; they are not the World Bank's own."),
    ("/people/", 6, "ar", "(فترة ثقة 95% من 18.4% إلى 24.9%)", "(فترة ثقة 95% من 18.1% إلى 25.2%)"),
    ("/people/", 6, "ar", "(من 47.1% إلى 55.5%)", "(من 47.0% إلى 55.6%)"),
    ("/people/", 6, "ar", "(من 7.4% إلى 11.3%)", "(من 6.8% إلى 11.8%)"),
    ("/people/", 6, "ar", "والفترات يستخرجها هذا المورد من أوزان المسح نفسها؛ ولا ينشر البنك الدولي أي منها.",
     "والفترات تحتسبها CauseWay من هذه القيم المنشورة بأثر التصميم الذي ينشره البنك الدولي لمسح اليمن، وليست فترات نشرها البنك الدولي."),
    # /methodology/ section 7 (ED-034, written to the v5 rule)
    ("/methodology/", 7, "en",
     "Where it does not, no interval, standard error or significance test is added unless it can be reproduced from the survey's own weights and design. For the Global Findex 2021 wave in Yemen this resource does reproduce it: the respondent file published for researchers carries the survey weight, so a 95% interval is derived for each published share by the design-based method for a weighted share, and shown with the figure. That file carries no sampling-unit identifier, so clustering is not captured and the derived intervals may be wider in reality, never narrower; the method and every interval are recorded with their figures, and the respondent file itself is never republished.",
     "Where it does not, no interval, standard error or significance test is added unless it can be computed from what the publisher states about its own survey design. For the Global Findex 2021 wave in Yemen, the World Bank publishes a design effect of 1.9 and a maximum margin of error of 4.3 percentage points at the 95% level, for a share of 50% on 1,000 interviews. For each published national share, CauseWay computes a 95% interval with the World Bank's own formula and that design effect, and shows it with the figure as computed by CauseWay; the method and every interval are recorded with their figures. No interval is computed for the shares of population groups or for the differences between them: the published design effect describes the whole sample, and each group is a smaller one."),
    ("/methodology/", 7, "ar",
     "وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن إعادة احتسابها من أوزان المسح وتصميمه. وفي موجة Global Findex 2021 في اليمن يعيد هذا المورد احتسابها فعلًا: فملف المستجيبين المنشور للباحثين يحمل وزن المسح، ومن ثَمّ تُستخرج فترة ثقة 95% لكل نسبة منشورة بالطريقة القائمة على تصميم المسح لنسبة موزونة، وتُعرض مع القيمة. ولا يحمل ذلك الملف معرّف وحدة المعاينة، لذلك لا تُحتسب آثار التجمّع العنقودي وقد تكون الفترات المستخرجة أوسع في الواقع لا أضيق؛ والطريقة وكل فترة مسجّلتان مع قيمتهما، ولا يُعاد نشر ملف المستجيبين نفسه أبدًا.",
     "وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن احتسابها مما ينشره المصدر عن تصميم مسحه. وفي موجة Global Findex 2021 في اليمن، ينشر البنك الدولي أثر تصميم قدره 1.9 وهامش خطأ أقصى قدره 4.3 نقطة مئوية عند مستوى ثقة 95%، لنسبة قدرها 50% في 1,000 مقابلة. ولكل نسبة وطنية منشورة تحتسب CauseWay فترة ثقة 95% بمعادلة البنك الدولي نفسها وبأثر التصميم هذا، وتُعرض مع الرقم بوصفها من احتساب CauseWay؛ والطريقة وكل فترة مسجّلتان مع قيمتهما. ولا تُحتسب فترة لنسب الفئات السكانية ولا للفروق بينها: فأثر التصميم المنشور يخص العينة كلها، وكل فئة عينة أصغر منها."),
]

# /rights/ section 6 (AR-NEW-001 + its CR-02 condition; merged with CLOSE-1's D3 change of the same cell)
D3_AR_OLD = "والشيفرة البرمجية للمستودع الذي يبني هذا المورد، فهي خارج نطاق هذه الرخصة."
D3_AR_NEW = ("والشيفرة البرمجية للمستودع الذي يبني هذا المورد، فهي خارج نطاق هذه الرخصة: إذ لا تُتاح الشيفرة بأي رخصة "
             "مفتوحة، وتحتفظ CauseWay بجميع الحقوق فيها.")
RIGHTS_EN_OLD = ("Figures derived from survey microdata: the confidence intervals this resource derives from the Global Findex "
                 "respondent file for Yemen (evidence record CLM-026) are computed from a file CauseWay obtained under the World "
                 "Bank Microdata Research License; only aggregate estimates are published, never respondent-level data. Cite the "
                 "data as that licence requires:")
RIGHTS_EN_NEW = ("Survey uncertainty: the intervals shown with Global Findex shares for Yemen are computed by CauseWay from "
                 "the World Bank's published values and the design effect the World Bank publishes for the survey, not "
                 "from respondent-level data; this resource publishes no respondent-level data. Cite the Global Findex data "
                 "as the World Bank asks:")
RIGHTS_EN_OLD2 = "CC BY 4.0 does not extend to the underlying microdata, which this resource does not host or redistribute."
RIGHTS_EN_NEW2 = "CC BY 4.0 does not extend to the World Bank's data, and this resource does not host or redistribute any survey microdata."
RIGHTS_AR_OLD = ("الأرقام المشتقة من البيانات الجزئية للمسوح: فترات الثقة التي يستخرجها هذا المورد من ملف المستجيبين في مسح "
                 "Global Findex لليمن (سجل الدليل CLM-026) محسوبة من ملف حصلت عليه CauseWay بموجب رخصة البحث للبيانات الجزئية "
                 "لدى البنك الدولي؛ ولا تُنشر إلا تقديرات تجميعية، ولا تُنشر أي بيانات على مستوى المستجيبين. استشهد بالبيانات كما "
                 "تشترط تلك الرخصة:")
RIGHTS_AR_NEW = ("عدم اليقين في المسوح: فترات الثقة المعروضة مع نسب المؤشر العالمي للشمول المالي (Global Findex) لليمن "
                 "تحتسبها CauseWay من القيم التي نشرها البنك الدولي ومن أثر التصميم الذي ينشره للمسح، لا من بيانات على "
                 "مستوى المستجيبين؛ ولا ينشر هذا المورد أي بيانات على مستوى المستجيبين. استشهد ببيانات Global Findex كما "
                 "يطلب البنك الدولي:")
RIGHTS_AR_OLD2 = "ولا تمتد رخصة CC BY 4.0 إلى البيانات الجزئية الأصلية، التي لا يستضيفها هذا المورد ولا يعيد توزيعها."
RIGHTS_AR_NEW2 = "ولا تمتد رخصة CC BY 4.0 إلى بيانات البنك الدولي، ولا يستضيف هذا المورد أي بيانات جزئية للمسوح ولا يعيد توزيعها."

# MA-001 guardrail: the instrument-change trigger (CR-01)
MA_EN_OLD = "and keep core concepts comparable with the previous wave."
MA_EN_NEW = ("and keep core concepts comparable with the previous wave. Yemen's 2021 study did not ask the mobile-money "
             "questions: if a new survey asks them, part of any rise in account ownership may come from the wider "
             "questionnaire, not from real change, so the two definitions must be reported separately.")
MA_AR_OLD = "وأن يحافظ على مفاهيم أساسية قابلة للمقارنة مع الموجة السابقة."
MA_AR_NEW = ("وأن يحافظ على مفاهيم أساسية قابلة للمقارنة مع الموجة السابقة. ولم تطرح دراسة اليمن لعام 2021 أسئلة خدمات "
             "الأموال عبر الهاتف: فإذا طرحها مسح جديد فقد يأتي جزء من أي ارتفاع في امتلاك الحساب من اتساع الاستبيان لا من "
             "تغيّر فعلي، لذلك يجب عرض التعريفين كلٍّ على حدة.")

# 25_FINDEX_BASELINE derivation rows
NATIONAL = {"CW-FINDEX-MOE-2022-001": ("account", "Account ownership (any)"),
            "CW-FINDEX-MOE-2022-014": ("account", "Account at a financial institution"),
            "CW-FINDEX-MOE-2022-015": ("saved", "Saved any money in the past year"),
            "CW-FINDEX-MOE-2022-016": ("borrowed", "Borrowed any money in the past year"),
            "CW-FINDEX-MOE-2022-017": ("digital", "Made or received a digital payment")}
WITHDRAWN = [f"CW-FINDEX-MOE-2022-{i:03d}" for i in range(2, 14)]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    reg = register_rows()
    t06 = Table(s, "06_EVIDENCE_OBJECTS")

    # ---- register rows AR-001 (Home s3) and AR-042 (CLM-001 summary): CR-01 confirmed → new_ar; CR-14 → World Bank wording
    r1 = reg["AR-001"]
    apply_register_ar(s, F, r1)
    apply_register_en(s, F, r1, r1["en_new"], must_start="11.9% of adults aged 15 and over in the areas surveyed")
    r42 = reg["AR-042"]
    ctx_ar = "يبلغ رقم البنك الدولي لموجة المسح نفسها في الاقتصادات منخفضة الدخل الـ19 التي شملتها الموجة، ومنها اليمن، 35.2%."
    ctx_en = ("the World Bank's figure for the same survey wave across the 19 low-income economies surveyed in it, Yemen "
              "among them, is 35.2%.")
    if r42["new_ar"].count("⟦CR-14⟧") != 1 or r42["en_new"].count("⟦CR-14⟧") != 1:
        raise TxError(f"{F} AR-042: placeholder not found exactly once")
    apply_register_ar(s, F, r42, new_ar=r42["new_ar"].replace("⟦CR-14⟧", ctx_ar))
    apply_register_en(s, F, r42, r42["en_new"].replace("⟦CR-14⟧", ctx_en), must_start="The latest representative observation")

    # ---- 06 and 11 text edits
    for rec, field, old, new in E06:
        cur = t06.get(rec, field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F} {rec}.{field}: substring occurs {0 if not isinstance(cur, str) else cur.count(old)} times: {old[:60]!r}")
        t06.set(F, rec, field, cur.replace(old, new), cur)
    t11 = Table(s, "11_VISUAL_LIBRARY")
    for rec, field, old, new in E11:
        cur = t11.get(rec, field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F} 11 {rec}.{field}: substring occurs {0 if not isinstance(cur, str) else cur.count(old)} times")
        t11.set(F, rec, field, cur.replace(old, new), cur)
    # value states
    for rec, (retire, add) in VS.items():
        cur = t06.get(rec, "value_states")
        vs = json.loads(cur)
        have = [e["t"] for e in vs]
        for t in retire:
            if have.count(t) != 1:
                raise TxError(f"{F} {rec}.value_states: {t!r} occurs {have.count(t)} times")
        vs = [e for e in vs if e["t"] not in retire]
        for e in add:
            if any(x["t"] == e["t"] for x in vs):
                continue
            vs.append(e)
        t06.set(F, rec, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)

    # ---- 03 sections
    for route, order, lang, old, new in E03:
        s.replace_section(F, route, order, lang, "body", old, new)
    # /rights/ s6 EN (CR-02 condition of AR-NEW-001)
    s.replace_section(F + ":AR-NEW-001", "/rights/", 6, "en", "body", RIGHTS_EN_OLD, RIGHTS_EN_NEW)
    s.replace_section(F + ":AR-NEW-001", "/rights/", 6, "en", "body", RIGHTS_EN_OLD2, RIGHTS_EN_NEW2)
    # /rights/ s6 AR: AR-NEW-001's exact-match check against its 2ddbfb61 text with CLOSE-1's D3 change merged in,
    # then the register's new_ar (same merge) with the CR-02 rewrite of the microdata sentence
    rn = reg["AR-NEW-001"]
    if rn["exact_old_ar"].count(D3_AR_OLD) != 1 or rn["new_ar"].count(D3_AR_OLD) != 1:
        raise TxError(f"{F} AR-NEW-001: the D3 clause is not where CLOSE-1 changed it")
    merged_old = rn["exact_old_ar"].replace(D3_AR_OLD, D3_AR_NEW)
    final = rn["new_ar"].replace(D3_AR_OLD, D3_AR_NEW)
    if final.count(RIGHTS_AR_OLD) != 1 or final.count(RIGHTS_AR_OLD2) != 1:
        raise TxError(f"{F} AR-NEW-001: microdata sentence not found once in the register's new_ar")
    final = final.replace(RIGHTS_AR_OLD, RIGHTS_AR_NEW).replace(RIGHTS_AR_OLD2, RIGHTS_AR_NEW2)
    apply_register_ar(s, F, rn, new_ar=final, expect_old=merged_old)

    # ---- MA-001 guardrail
    t10 = Table(s, "10_MEASUREMENT_AGENDA")
    for field, old, new in (("guardrail_en", MA_EN_OLD, MA_EN_NEW), ("guardrail_ar", MA_AR_OLD, MA_AR_NEW)):
        cur = t10.get("MA-001", field)
        if cur.count(old) != 1:
            raise TxError(f"{F} MA-001.{field}: anchor not found once")
        t10.set(F + ":CR-01", "MA-001", field, cur.replace(old, new), cur)

    # ---- 25_FINDEX_BASELINE: the national intervals restated, the group intervals withdrawn
    t25 = Table(s, "25_FINDEX_BASELINE")
    for oid, (key, label) in NATIONAL.items():
        lo, hi, m = IV[key]
        old_cav = t25.get(oid, "caveat")
        t25.set(F + ":CR-02", oid, "value", m, t25.get(oid, "value"))
        t25.set(F + ":CR-02", oid, "unit", "percentage points (95% margin of error, from the published design effect)", t25.get(oid, "unit"))
        t25.set(F + ":CR-02", oid, "publisher", "CauseWay computation from World Bank published values and design effect", t25.get(oid, "publisher"))
        t25.set(F + ":CR-02", oid, "source_url", METH_URL, t25.get(oid, "source_url"))
        t25.set(F + ":CR-02", oid, "evidence_state", "CAUSEWAY_COMPUTED_INTERVAL", t25.get(oid, "evidence_state"))
        t25.set(F + ":CR-02", oid, "caveat",
                f"Point estimate {round(P[key], 1)}%; 95% confidence interval {lo}% to {hi}%; base 1,000 interviews (the "
                f"whole sample); design effect 1.9, the value the World Bank publishes for Yemen's survey (The Global "
                f"Findex Database 2021, Appendix A, Table A.1, printed p.17). CauseWay computation (close-out CR-02, "
                f"{DATE}): margin = 1.96 x sqrt(1.9) x sqrt(p(1-p)/1,000), the World Bank's own margin-of-error formula "
                f"(Table A.1, footnote c), applied to the World Bank's published unrounded value p ({P[key]}). No "
                f"respondent-level data are used. This replaces the earlier derivation from the respondent file (FC-1), "
                f"withdrawn under brief v5. Previous record: " + old_cav, old_cav)
    for oid in WITHDRAWN:
        old_cav = t25.get(oid, "caveat")
        t25.set(F + ":CR-02", oid, "value", None, t25.get(oid, "value"))
        t25.set(F + ":CR-02", oid, "evidence_state", "WITHDRAWN__NO_PUBLISHED_GROUP_DESIGN", t25.get(oid, "evidence_state"))
        t25.set(F + ":CR-02", oid, "caveat",
                f"Withdrawn (close-out CR-02, {DATE}): the World Bank publishes its design effect and sample size for "
                f"the whole sample only, so no interval is computed for population groups or for the differences "
                f"between them, and none is published. Previous record: " + old_cav, old_cav)
    # WB-FINDEX-OBS-2022-001: the CR-01 fact beside the World Bank's own label
    cav = t25.get("WB-FINDEX-OBS-2022-001", "caveat")
    t25.set(F + ":CR-01", "WB-FINDEX-OBS-2022-001", "caveat",
            (str(cav or "").rstrip() + " " if cav else "") + "In Yemen's survey the mobile-money questions were not asked: "
            "fiaccount.t.d equals account.t.d (11.9033656433415) and mobileaccount.t.d is empty for Yemen (open API, "
            "source 28, read " + DATE + ").", cav)

    # ---- 15: the Findex 2021 methodology appendix is reachable from the study's source record
    t15 = Table(s, "15_SOURCE_LIBRARY")
    au = t15.get("SRC-WB-FINDEX-001", "additional_urls")
    urls = json.loads(au) if au else []
    if METH_URL not in urls:
        t15.set(F + ":CR-02", "SRC-WB-FINDEX-001", "additional_urls", json.dumps(urls + [METH_URL]), au)

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "CR-01 (mobile-money questions not asked in Yemen's Findex study), CR-02 (World Bank design effect "
                    "1.9 / margin 4.3: national intervals restated, group intervals withdrawn), CR-14 verified; "
                    "register rows AR-001, AR-042, ED-034, AR-NEW-001"),
        ("intervals", {k: {"p": P[k], "lo": v[0], "hi": v[1], "moe": v[2]} for k, v in IV.items()}),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
