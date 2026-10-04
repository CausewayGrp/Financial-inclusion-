# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-3: the 2022 saving, borrowing and digital-payment values; a false
"no later value" claim removed from five records and one page section.

  python3 fc_3_currentness_2022.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-A-01, opened by the FC-1 reconciliation. Five records and one page section said, in both languages, that
no weighted value later than 2014 exists for saving, borrowing and domestic remittances, and /people/ headed the
section "Saving and borrowing tell a different - older - story". That was false. The World Bank publishes 2022 values
for Yemen in the very series this resource already cites, and the respondent file reproduces each of them exactly:

  save.any.t.d      2014 20.640307   2022 21.644527   -> published 21.6%, derived 95% interval 18.4% to 24.9%
  borrow.any.t.d    2014 65.982360   2022 51.281103   -> published 51.3%, derived 95% interval 47.1% to 55.5%
  g20.any           2014  4.381780   2022  9.334559   -> published  9.3%, derived 95% interval  7.4% to 11.3%
  (api.worldbank.org/v2/country/YEM/indicator/<id>?source=28, read 4 October 2026)

WHAT IS PUBLISHED, AND WHAT IS DELIBERATELY NOT

Saving, borrowing and digital payments are published for 2022 with their derived intervals. The World Bank's own
series carries both 2014 and 2022 for each, so the two years are comparable by the publisher's own construction.

They are NOT printed as a pair beside the 2014 values this resource already shows, and that restraint is deliberate.
The 2014 values on CLM-028 and CLM-029 were read from the Little Data Book on Financial Inclusion 2015, p. 160, and
the World Bank's current database gives a slightly different 2014 value for one of them: 65.982360, which rounds to
66.0, where the printed country page gives 65.9. Subtracting a 2022 database value from a 2014 printed-page value
would mix two vintages of the same publisher and manufacture a change out of a revision. So each record states what
its own source says, names the later observation and says where it is, and no difference between the two is computed.
The revision itself is recorded as finding FC-A-04.

DOMESTIC REMITTANCES are not published for 2022, for a different and stronger reason. The World Bank's current series
for received domestic remittances (fh2) carries a 2022 value, 31.931398 - which the respondent file reproduces
exactly - but carries NO 2014 value at all, while this resource's 2014 figure of 18.3% comes from the 2014 country
profile. A series that does not hold the earlier year is not a series the earlier year can be read against, so the
two are not established as comparable and nothing is published from the pair. The records now say that plainly
instead of saying no later value exists.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "FC-3:FC-A-01"
S06 = "06_EVIDENCE_OBJECTS"
S25 = "25_FINDEX_BASELINE"

API = "https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE"
LOCW = ("api.worldbank.org/v2/country/YEM/indicator/%s?source=28 (Global Financial Inclusion), date 2022, "
        "read 4 October 2026")
LOCD = ("CauseWay derivation FC-1 from the Global Findex 2021 Yemen respondent file; method, base and design effect "
        "in 25_FINDEX_BASELINE row %s")

# the published 2022 observations this transaction adds (World Bank values, one decimal place per the E2-2 rule)
OBS = [("WB-FINDEX-OBS-2022-010", "save.any.t.d", "Saved any money in the past year", 21.6,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (20.6%). "
        "A 95% interval of 18.4% to 24.9% is derived from the respondent file (CW-FINDEX-MOE-2022-015)."),
       ("WB-FINDEX-OBS-2022-011", "borrow.any.t.d", "Borrowed any money in the past year", 51.3,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (66.0%), "
        "which is not the 65.9% printed on the World Bank's own 2014 country page - see finding FC-A-04. "
        "A 95% interval of 47.1% to 55.5% is derived from the respondent file (CW-FINDEX-MOE-2022-016)."),
       ("WB-FINDEX-OBS-2022-012", "g20.any", "Made or received a digital payment", 9.3,
        "Weighted World Bank value for the 2021 Findex wave; the same series also carries a 2014 value (4.4%). "
        "A 95% interval of 7.4% to 11.3% is derived from the respondent file (CW-FINDEX-MOE-2022-017).")]

OLD_CUR_EN = ("The values refer to 2014, from the World Bank's 2014 country profile for Yemen. No weighted value from "
              "a later Yemen wave is available in this resource for these measures, so they should not be read as "
              "describing a later period unless a newer comparable observation is published.")
OLD_CUR_AR = ("تعود هذه القيم إلى عام 2014، "
              "وهي مأخوذة من الملف "
              "القطري لليمن الذي نشره "
              "البنك الدولي لعام 2014. "
              "ولا تتوفر في هذا المورد "
              "قيمة موزونة لهذه المقاييس "
              "من موجة يمنية لاحقة، "
              "لذلك لا تُقرأ على أنها "
              "تصف فترة لاحقة ما لم "
              "تُنشر مشاهدة أحدث "
              "قابلة للمقارنة.")

HEAD_2014_EN = ("The values refer to 2014, from the World Bank's 2014 country profile for Yemen. ")
HEAD_2014_AR = ("تعود هذه القيم إلى عام 2014، "
                "وهي مأخوذة من الملف "
                "القطري لليمن الذي نشره "
                "البنك الدولي لعام 2014. ")

# saving / borrowing: a later observation exists, in the same series, and is named
LATER_SB_EN = ("A later observation does exist: the World Bank's own series gives a 2022 value for the same measure "
               "from the 2021 Findex wave, shown on this resource at /people/ with its interval. The two are not "
               "subtracted from one another here, because the 2014 value on this record was read from the printed "
               "2014 country page and the database gives a slightly different 2014 value for the same indicator; a "
               "difference between the two would be a difference between two vintages of the publisher, not a "
               "measured change.")
LATER_SB_AR = ("وتوجد مشاهدة لاحقة بالفعل: "
               "فسلسلة البنك الدولي "
               "نفسها تعطي قيمة لعام 2022 "
               "للمقياس نفسه من موجة Findex 2021، "
               "وتُعرض في هذا المورد "
               "على صفحة /people/ مع فترتها. "
               "ولا تُطرح القيمتان "
               "إحداهما من الأخرى هنا، "
               "لأن قيمة 2014 في هذا السجل "
               "قُرئت من الصفحة القطرية "
               "المطبوعة لعام 2014، بينما "
               "تعطي قاعدة البيانات "
               "قيمة مختلفة قليلاً "
               "لعام 2014 للمؤشر نفسه؛ "
               "وأي فرق بينهما سيكون "
               "فرقاً بين نسختي نشر "
               "لدى الناشر، وليس تغيراً "
               "مقاساً.")

# domestic remittances: a 2022 value exists in a series that does not hold 2014, so the pair is not comparable
LATER_RM_EN = ("The World Bank's current series for received domestic remittances does carry a 2022 value from the "
               "2021 Findex wave, but it carries no 2014 value at all, while the figure on this record comes from the "
               "2014 country profile. A series that does not hold the earlier year cannot establish a change against "
               "it, so no later value is published here and the two are not read as a trend. What it would take to "
               "compare them is a measurement question, not a presentation one.")
LATER_RM_AR = ("وسلسلة البنك الدولي "
               "الحالية لتلقي الحوالات "
               "المحلية تحمل بالفعل "
               "قيمة لعام 2022 من موجة Findex 2021، "
               "لكنها لا تحمل أي قيمة "
               "لعام 2014، في حين أن القيمة "
               "في هذا السجل مأخوذة من "
               "الملف القطري لعام 2014. "
               "والسلسلة التي لا تحمل "
               "السنة الأقدم لا تستطيع "
               "إظهار تغير مقابلها، "
               "لذلك لا تُنشر هنا قيمة "
               "أحدث ولا تُقرأ القيمتان "
               "اتجاهاً. وما يلزم لمقارنتهما "
               "مسألة قياس، لا مسألة عرض.")

SB = ("CLM-028", "CLM-029", "VIS-BORROWING-SOURCES-2014")
RM = ("CLM-030", "VIS-DOMESTIC-REMITTANCE-PATH-2014")

LADDER_SUM_EN = (
    "The latest weighted evidence differs by financial function: the 2021 Findex wave gives 2022 values for account "
    "ownership (11.9%), for saving (21.6%) and borrowing (51.3%) any money and for making or receiving a digital "
    "payment (9.3%); the latest weighted value this resource publishes for domestic remittances is from 2014 (18.3% "
    "received them), because the World Bank's current series for that measure holds no 2014 value to read it against; "
    "and weighted estimates of resilience and of the reasons for not having an account have not yet been calculated "
    "for the 2021 wave.")
LADDER_SUM_AR = (
    "يختلف أحدث دليل موزون "
    "بحسب الوظيفة المالية: "
    "فموجة Findex 2021 تعطي قيماً لعام 2022 "
    "لامتلاك الحساب (11.9%)، "
    "ولادخار أي مبلغ (21.6%) "
    "واقتراضه (51.3%)، ولإجراء "
    "مدفوعة رقمية أو تلقيها (9.3%)؛ "
    "أما أحدث قيمة موزونة "
    "ينشرها هذا المورد "
    "للحوالات المحلية فهي "
    "من 2014 (تلقاها 18.3%)، لأن سلسلة "
    "البنك الدولي الحالية "
    "لهذا المقياس لا تحمل "
    "قيمة لعام 2014 تُقارن بها؛ "
    "ولا تزال تقديرات "
    "الصمود المالي وأسباب "
    "عدم امتلاك الحساب "
    "لموجة 2021 بانتظار الاحتساب.")

LADDER_CUR_EN = (
    "The latest observations differ by function: 2022 for account ownership, saving, borrowing and digital payments "
    "(2021 Findex wave, fieldwork 7 November 2022 to 9 January 2023) and 2014 for domestic remittances; resilience "
    "and reasons for not having an account have no weighted value yet. None of them describes a later period unless a "
    "newer comparable observation is published.")
LADDER_CUR_AR = (
    "تختلف أحدث المشاهدات "
    "بحسب الوظيفة: 2022 لامتلاك "
    "الحساب والادخار "
    "والاقتراض والمدفوعات "
    "الرقمية (موجة Findex 2021، والعمل "
    "الميداني من 7 نوفمبر 2022 "
    "إلى 9 يناير 2023)، و2014 للحوالات "
    "المحلية؛ ولا توجد بعد "
    "قيمة موزونة للصمود "
    "المالي ولأسباب عدم "
    "امتلاك الحساب. ولا يصف "
    "أي منها فترة لاحقة ما لم "
    "تُنشر مشاهدة أحدث قابلة "
    "للمقارنة.")

PEOPLE_H_EN = "Saving, borrowing and digital payments in the same wave"
PEOPLE_H_AR = ("الادخار والاقتراض "
               "والمدفوعات الرقمية "
               "في الموجة نفسها")
PEOPLE_B_EN = (
    "The same 2021 wave measures more than account ownership. In it, 21.6% of adults reported saving any money "
    "(95% interval 18.4% to 24.9%), 51.3% reported borrowing any money (47.1% to 55.5%) and 9.3% reported making or "
    "receiving a digital payment (7.4% to 11.3%). Borrowing is far more common than saving, and both are far more "
    "common than having an account: borrowing here includes borrowing from family and friends, which needs no "
    "provider at all. The intervals are derived by this resource from the survey's own weights; the World Bank "
    "publishes none.")
PEOPLE_B_AR = (
    "تقيس موجة 2021 نفسها أكثر "
    "من امتلاك الحساب. ففيها "
    "أفاد 21.6% من البالغين "
    "بأنهم ادخروا أي مبلغ "
    "(فترة ثقة 95% من 18.4% إلى 24.9%)، "
    "وأفاد 51.3% بأنهم اقترضوا "
    "أي مبلغ (من 47.1% إلى 55.5%)، "
    "و9.3% بأنهم أجروا مدفوعة "
    "رقمية أو تلقوها (من 7.4% "
    "إلى 11.3%). والاقتراض أشيع "
    "بكثير من الادخار، "
    "وكلاهما أشيع بكثير من "
    "امتلاك حساب: فالاقتراض "
    "هنا يشمل الاقتراض من "
    "الأسرة والأصدقاء، "
    "وهو لا يحتاج مقدم خدمة "
    "أبداً. والفترات "
    "يستخرجها هذا المورد "
    "من أوزان المسح نفسها؛ "
    "ولا ينشر البنك الدولي "
    "أي منها.")
OLD_PEOPLE_H_EN = "Saving and borrowing tell a different — older — story"
OLD_PEOPLE_H_AR = ("الاقتراض والادخار "
                   "يقدمان صورة أخرى — "
                   "لكنها أقدم")


# ---------------------------------------------------------------------------------------------------------------------
# CLM-026 stated three preconditions for publishing a custom weighted estimate: authorized respondent-level data,
# the correct survey weights, and successful reproduction of the official benchmark values. All three are now met, so
# the record publishes the three measures whose published 2022 values this resource reproduced exactly, and keeps the
# rest of the panel pending. Nothing here claims the other 29 measures are measured.
CLM026_SUM_EN = (
    "A 32-metric demand-side panel has been specified across access, barriers, digital use, saving, borrowing, "
    "resilience, remittances, income flows, financial worry and connectivity. Three of its measures now have "
    "published values for the 2021 wave, each reproduced from the respondent file: 21.6% of adults saved any money "
    "in the past year, 51.3% borrowed any money, and 9.3% made or received a digital payment. The other measures "
    "remain unpublished: a published value to reproduce is what they lack, not access to the data.")
CLM026_SUM_AR = (
    "حُدِّدت مجموعة من 32 مقياسًا "
    "لجانب الطلب تغطي الوصول "
    "والعوائق والاستخدام "
    "الرقمي والادخار "
    "والاقتراض والقدرة على "
    "الصمود والحوالات "
    "وتدفقات الدخل والقلق "
    "المالي والاتصال. "
    "وأصبحت لـسـتة من مقاييسها "
    "— بل لـثلاثة منها — قيم "
    "منشورة لموجة 2021، أُعيد "
    "احتساب كل منها من ملف "
    "المستجيبين: فقد ادخر 21.6% "
    "من البالغين أي مبلغ خلال "
    "السنة الماضية، واقترض 51.3% "
    "أي مبلغ، وأجرى 9.3% مدفوعة "
    "رقمية أو تلقاها. وتبقى "
    "المقاييس الأخرى غير "
    "منشورة: فما ينقصها قيمة "
    "منشورة يُعاد احتسابها، "
    "لا الوصول إلى البيانات.")
CLM026_DEF_EN = (
    "This record describes a set of 32 defined people-side measures for the Yemen Findex 2021 study, and carries the "
    "three of them that have a published value for the wave: saving any money in the past year, borrowing any money "
    "in the past year, and making or receiving a digital payment, each as a share of adults aged 15 and over in the "
    "areas the survey covered.")
CLM026_DEF_AR = (
    "يصف هذا السجل مجموعة من 32 "
    "مقياسًا محددًا على جانب "
    "الأفراد لدراسة Findex 2021 الخاصة "
    "باليمن، ويحمل الثلاثة "
    "منها التي لها قيمة منشورة "
    "للموجة: ادخار أي مبلغ خلال "
    "السنة الماضية، واقتراض "
    "أي مبلغ خلالها، وإجراء "
    "مدفوعة رقمية أو تلقيها، "
    "وكل منها نسبة من البالغين "
    "بعمر 15 سنة فأكثر في المناطق "
    "التي شملها المسح.")
CLM026_METH_EN = (
    "The variables, definitions and derivations were specified in advance, and a numeric estimate is published only "
    "after authorized respondent-level data are available, the correct survey weights are applied and the official "
    "benchmark values are reproduced. For these three measures all three conditions are met: the respondent file was "
    "supplied under the World Bank Microdata Research License, the published survey weight was used, and each "
    "measure's weighted estimate reproduces the World Bank's own published value for Yemen in 2022. The 95% interval "
    "beside each is derived by this resource from the same weights (18.4% to 24.9% for saving, 47.1% to 55.5% for "
    "borrowing, 7.4% to 11.3% for digital payments); the World Bank publishes none.")
CLM026_METH_AR = (
    "تُحدد المتغيرات "
    "والتعريفات وطريقة "
    "الاحتساب مسبقًا، ولا "
    "يُنشر تقدير رقمي إلا "
    "بعد توفر بيانات "
    "المستجيبين المصرح "
    "باستخدامها، وتطبيق "
    "أوزان المسح الصحيحة، "
    "وإعادة إنتاج القيم "
    "المرجعية الرسمية. "
    "ولهذه المقاييس الثلاثة "
    "استوفيت الشروط الثلاثة: "
    "فقد أُتيح ملف المستجيبين "
    "بموجب رخصة البحث للبيانات "
    "الجزئية لدى البنك الدولي، "
    "واستُخدم وزن المسح "
    "المنشور، ويعيد التقدير "
    "الموزون لكل مقياس إنتاج "
    "القيمة التي نشرها البنك "
    "الدولي نفسه لليمن في 2022. "
    "وفترة الثقة 95% بجانب كل "
    "قيمة يستخرجها هذا "
    "المورد من الأوزان نفسها "
    "(من 18.4% إلى 24.9% للادخار، ومن 47.1% "
    "إلى 55.5% للاقتراض، ومن 7.4% إلى "
    "11.3% للمدفوعات الرقمية)؛ "
    "ولا ينشر البنك الدولي "
    "أي منها.")
CLM026_LIM_EN = (
    "Twenty-nine of the 32 specified measures are planned, not measured: none of them is a published indicator, "
    "because there is no published value for this wave to reproduce a weighted estimate against. | The three that "
    "are published are shares of all adults in the areas the survey covered, each on its own question base. They do "
    "not add up and are not stages of one process: borrowing any money includes borrowing from family and friends, "
    "which needs no provider, and making or receiving a digital payment does not require owning an account.")
CLM026_LIM_AR = (
    "تسعة وعشرون من المقاييس "
    "المحددة البالغة 32 مخططة "
    "وليست مقاسة: فلا يمثل أي "
    "منها مؤشرًا منشورًا، "
    "لأنه لا توجد قيمة منشورة "
    "لهذه الموجة يُقارن بها "
    "التقدير الموزون. | "
    "والمقاييس الثلاثة "
    "المنشورة نسب من جميع "
    "البالغين في المناطق "
    "التي شملها المسح، ولكل "
    "منها قاعدة سؤاله الخاصة. "
    "ولا تُجمع هذه النسب "
    "ولا تمثل مراحل في مسار "
    "واحد: فاقتراض أي مبلغ "
    "يشمل الاقتراض من الأسرة "
    "والأصدقاء وهو لا يحتاج "
    "مقدم خدمة، وإجراء مدفوعة "
    "رقمية أو تلقيها لا يستلزم "
    "امتلاك حساب.")
CLM026_CUR_EN = (
    "The panel specification and the three published values apply to the Yemen Findex 2021 study, whose fieldwork ran "
    "from 7 November 2022 to 9 January 2023 and which the World Bank reports for 2022. The remaining measures stay "
    "unpublished until a published value exists to reproduce them against; a newer wave would require an updated "
    "panel.")
CLM026_CUR_AR = (
    "تنطبق مواصفة المجموعة "
    "والقيم الثلاث المنشورة "
    "على دراسة اليمن ضمن Findex 2021، "
    "التي نُفذ عملها الميداني "
    "من 7 نوفمبر 2022 إلى 9 يناير 2023 "
    "ويعرضها البنك الدولي "
    "لسنة 2022. وتبقى المقاييس "
    "الأخرى غير منشورة حتى "
    "توجد قيمة منشورة يُعاد "
    "احتسابها مقابلها؛ "
    "وتحتاج أي موجة أحدث "
    "إلى تحديث مجموعة "
    "المقاييس.")

# VIS-FINDEX-ACCESS-USE: a digital-payment value now exists for the wave. It is NOT "used an account digitally" -
# a payment can be made or received without an account - so the ladder's three levels are unchanged and the record
# says what the new value is and is not.
AU_SUM_EN = ("Weighted estimates of how many adults used an account, or used one digitally, have not yet been "
             "produced for this wave, so ownership is the only level available; owning an account does not show that "
             "it is used.",
             "Weighted estimates of how many adults used an account, or used one digitally, have not been produced "
             "for this wave, so ownership is the only level of this ladder available; owning an account does not show "
             "that it is used. A different measure of the same wave is published: 9.3% of adults made or received a "
             "digital payment (95% interval 7.4% to 11.3%). That is not account use, because a payment can be made or "
             "received without an account.")
AU_SUM_AR = ("ولم تُنتج بعد لهذه "
             "الموجة تقديرات موزونة "
             "لنسبة من استخدموا حسابًا "
             "أو استخدموه رقميًا، "
             "لذلك يبقى امتلاك "
             "الحساب المستوى "
             "الوحيد المتاح؛ "
             "وامتلاك الحساب لا "
             "يدل على استخدامه.",
             "ولم تُنتج لهذه الموجة "
             "تقديرات موزونة لنسبة "
             "من استخدموا حسابًا أو "
             "استخدموه رقميًا، لذلك "
             "يبقى امتلاك الحساب "
             "المستوى الوحيد المتاح "
             "في هذا التدرج؛ "
             "وامتلاك الحساب لا يدل "
             "على استخدامه. ويُنشر "
             "مقياس مختلف من الموجة "
             "نفسها: فقد أجرى 9.3% من "
             "البالغين مدفوعة رقمية "
             "أو تلقوها (فترة ثقة 95% من 7.4% "
             "إلى 11.3%). وهذا ليس استخدامًا "
             "للحساب، لأن المدفوعة "
             "الرقمية يمكن إجراءها "
             "أو تلقيها دون حساب.")
AU_METH_EN = ("Account-use and digital-use estimates require weighted calculation from the respondent-level data, "
              "which has not yet been completed.",
              "Account-use and digital-use estimates require weighted calculation from the respondent-level data, "
              "which has not been completed. The digital-payment share is the World Bank's own published value for "
              "the wave, reproduced from the respondent file, with its 95% interval derived from the survey weights.")
AU_METH_AR = ("أما تقديرات استخدام "
              "الحساب والاستخدام "
              "الرقمي فتتطلب احتسابًا "
              "موزونًا من بيانات "
              "المستجيبين، ولم "
              "يُستكمل هذا الاحتساب "
              "بعد.",
              "أما تقديرات استخدام "
              "الحساب والاستخدام "
              "الرقمي فتتطلب احتسابًا "
              "موزونًا من بيانات "
              "المستجيبين، ولم "
              "يُستكمل هذا الاحتساب. "
              "ونسبة المدفوعات "
              "الرقمية هي القيمة التي "
              "نشرها البنك الدولي "
              "نفسه للموجة، وأُعيد "
              "احتسابها من ملف "
              "المستجيبين، مع "
              "استخراج فترة الثقة 95% "
              "من أوزان المسح.")
AU_CUR_EN = ("Account-use and digital-use values have not yet been produced.",
             "Account-use and digital-use values have not been produced. The digital-payment value refers to the same "
             "wave.")
AU_CUR_AR = ("أما قيم استخدام الحساب "
             "والاستخدام الرقمي "
             "فلم تُنتج بعد.",
             "أما قيم استخدام الحساب "
             "والاستخدام الرقمي "
             "فلم تُنتج. وتعود قيمة "
             "المدفوعات الرقمية "
             "إلى الموجة نفسها.")

NEWVALS = [("21.6%", "WB-FINDEX-OBS-2022-010", "save.any.t.d"), ("51.3%", "WB-FINDEX-OBS-2022-011", "borrow.any.t.d"),
           ("9.3%", "WB-FINDEX-OBS-2022-012", "g20.any")]
DERIVED = [("18.4%", "CW-FINDEX-MOE-2022-015"), ("24.9%", "CW-FINDEX-MOE-2022-015"),
           ("47.1%", "CW-FINDEX-MOE-2022-016"), ("55.5%", "CW-FINDEX-MOE-2022-016"),
           ("7.4%", "CW-FINDEX-MOE-2022-017"), ("11.3%", "CW-FINDEX-MOE-2022-017")]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, S06, 4)

    # 1. the false currentness claim, in both languages
    for key in SB:
        t06.set(F, key, "currentness_en", HEAD_2014_EN + LATER_SB_EN, OLD_CUR_EN)
        t06.set(F, key, "currentness_ar", HEAD_2014_AR + LATER_SB_AR, OLD_CUR_AR)
    for key in RM:
        t06.set(F, key, "currentness_en", HEAD_2014_EN + LATER_RM_EN, OLD_CUR_EN)
        t06.set(F, key, "currentness_ar", HEAD_2014_AR + LATER_RM_AR, OLD_CUR_AR)

    # 2. the vintage ladder's own thesis
    t06.set(F, "VIS-DEMAND-VINTAGE-LADDER", "summary_en", LADDER_SUM_EN,
            s.ed.get_value(S06, t06.rows["VIS-DEMAND-VINTAGE-LADDER"], t06.col("summary_en")))
    t06.set(F, "VIS-DEMAND-VINTAGE-LADDER", "summary_ar", LADDER_SUM_AR,
            s.ed.get_value(S06, t06.rows["VIS-DEMAND-VINTAGE-LADDER"], t06.col("summary_ar")))
    t06.set(F, "VIS-DEMAND-VINTAGE-LADDER", "currentness_en", LADDER_CUR_EN,
            s.ed.get_value(S06, t06.rows["VIS-DEMAND-VINTAGE-LADDER"], t06.col("currentness_en")))
    t06.set(F, "VIS-DEMAND-VINTAGE-LADDER", "currentness_ar", LADDER_CUR_AR,
            s.ed.get_value(S06, t06.rows["VIS-DEMAND-VINTAGE-LADDER"], t06.col("currentness_ar")))

    # 3. CLM-026 is the record that said these estimates were unpublished, and why. All three of its stated
    #    preconditions are now met for three of its measures, so it publishes them and keeps the rest pending.
    t06.set(F, "CLM-026", "summary_en", CLM026_SUM_EN,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("summary_en")))
    t06.set(F, "CLM-026", "summary_ar", CLM026_SUM_AR,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("summary_ar")))
    t06.set(F, "CLM-026", "definition_en", CLM026_DEF_EN,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("definition_en")))
    t06.set(F, "CLM-026", "definition_ar", CLM026_DEF_AR,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("definition_ar")))
    t06.set(F, "CLM-026", "method_en", CLM026_METH_EN,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("method_en")))
    t06.set(F, "CLM-026", "method_ar", CLM026_METH_AR,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("method_ar")))
    t06.set(F, "CLM-026", "limitations_en", CLM026_LIM_EN,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("limitations_en")))
    t06.set(F, "CLM-026", "limitations_ar", CLM026_LIM_AR,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("limitations_ar")))
    t06.set(F, "CLM-026", "currentness_en", CLM026_CUR_EN,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("currentness_en")))
    t06.set(F, "CLM-026", "currentness_ar", CLM026_CUR_AR,
            s.ed.get_value(S06, t06.rows["CLM-026"], t06.col("currentness_ar")))

    # 3b. the access/use ladder said no digital-use value exists. A digital-payment value now does, and it is a
    #     different measure: a payment can be made or received without using an account, so the firewall holds.
    for fld, old, new in (("summary_en", AU_SUM_EN[0], AU_SUM_EN[1]), ("summary_ar", AU_SUM_AR[0], AU_SUM_AR[1]),
                          ("method_en", AU_METH_EN[0], AU_METH_EN[1]), ("method_ar", AU_METH_AR[0], AU_METH_AR[1]),
                          ("currentness_en", AU_CUR_EN[0], AU_CUR_EN[1]),
                          ("currentness_ar", AU_CUR_AR[0], AU_CUR_AR[1])):
        s.replace(F, S06, t06.rows["VIS-FINDEX-ACCESS-USE"], t06.col(fld), old, new,
                  "VIS-FINDEX-ACCESS-USE." + fld)

    # 3c. value states: the published values on the records that print them, the derived bounds on CLM-026
    def add(key, published, derived, site=True, trivial=(), dates=()):
        col = t06.col("value_states")
        cur = json.loads(s.ed.get_value(S06, t06.rows[key], col))
        have = {e["t"] for e in cur}
        new = list(cur)
        for tok, code in published:
            if tok not in have:
                new.append(OrderedDict([("t", tok), ("k", "v"), ("s", "READ"),
                                        ("src", "SRC-WB-FINDEX-AGG-2022"), ("loc", LOCW % code)]))
        for tok, obs in derived:
            if tok not in have:
                new.append(OrderedDict([("t", tok), ("k", "v"), ("s", "DERIVED"),
                                        ("src", "SRC-WB-FINDEX-001"), ("loc", LOCD % obs)]))
        if site and "95%" not in have:
            new.append(OrderedDict([("t", "95%"), ("k", "v"), ("s", "SITE")]))
        for tok in trivial:
            if tok not in have:
                new.append(OrderedDict([("t", tok), ("k", "v"), ("s", "TRIVIAL")]))
        for tok, loc in dates:
            if tok not in have:
                new.append(OrderedDict([("t", tok), ("k", "d"), ("s", "READ"),
                                        ("src", "SRC-WB-FINDEX-001"), ("loc", loc)]))
        if len(new) != len(cur):
            t06.set(F, key, "value_states", json.dumps(new, ensure_ascii=False, separators=(",", ":")),
                    json.dumps(cur, ensure_ascii=False, separators=(",", ":")))

    add("CLM-026", [(t, c) for t, _o, c in NEWVALS], DERIVED, trivial=("15", "32"), dates=(
        ("7 November 2022", "microdata.worldbank.org/index.php/catalog/5862/study-description > Data collection > "
                            "Dates of Data Collection: Start 2022-11-07"),
        ("9 January 2023", "microdata.worldbank.org/index.php/catalog/5862/study-description > Data collection > "
                           "Dates of Data Collection: End 2023-01-09")))
    add("VIS-DEMAND-VINTAGE-LADDER", [(t, c) for t, _o, c in NEWVALS], [], site=False)
    add("VIS-FINDEX-ACCESS-USE", [("9.3%", "g20.any")], [("7.4%", "CW-FINDEX-MOE-2022-017"),
                                                         ("11.3%", "CW-FINDEX-MOE-2022-017")])

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-3"),
        ("summary", "The 2021 wave's 2022 values for saving, borrowing and digital payments published with their "
                    "derived intervals; the false claim that no weighted value later than 2014 exists removed from "
                    "five records and one page section, in both languages")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
