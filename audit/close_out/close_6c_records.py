# -*- coding: utf-8 -*-
"""CLOSE-6C draft: the two Cash Consortium of Yemen findings held as Evidence Records (addendum item 4). Read R5."""
import json
from collections import OrderedDict

ISP, SAM = "SRC-CCY-ISP-2024", "SRC-CCY-SAM-2024"
R5 = "; read 11 October 2026 (audit/close_out/addendum/R5_ccy_isp_sam.md)"


def vs(t, k, s, src=None, loc=None):
    e = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        e["src"] = src
    if loc:
        e["loc"] = loc + R5
    return e


BOUND_EN = ("This record is drawn from the source(s) listed on this page. Open a source record to reach the original document, "
            "and check that the definition, period, population and geography match what is stated here.")
BOUND_AR = ("يستند هذا السجل إلى المصدر أو المصادر المدرجة في هذه الصفحة. افتح سجل المصدر للوصول إلى الوثيقة الأصلية، وتحقق من "
            "تطابق التعريف والفترة والمجتمع والنطاق الجغرافي مع ما يرد هنا.")
TRIGGER_EN = ("This record is updated when an authoritative source is revised or replaced, a newer comparable observation becomes "
              "available, the definition, population or method changes, or the conditions for public use change.")
TRIGGER_AR = ("يُحدَّث هذا السجل عند مراجعة المصدر المعتمد أو استبداله، أو توفر مشاهدة أحدث قابلة للمقارنة، أو تغير التعريف أو المجتمع "
              "أو الطريقة، أو تغير شروط الاستخدام العام.")

NEW_RECORDS = [
    OrderedDict([
        ("object_id", "CCY-ISP-2024"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/remittances/"),
        ("title_en", "Informal support in the cash income of cash-assistance households in three areas (CCY, June 2024)"),
        ("title_ar", "الدعم غير الرسمي في الدخل النقدي لأسر تتلقى مساعدات نقدية في ثلاث مناطق (تحالف النقد في اليمن، يونيو 2024)"),
        ("summary_en",
         "A Cash Consortium of Yemen survey, collected in June 2024, of households receiving multipurpose cash assistance in "
         "three areas that the study calls sub-districts and places in areas under the internationally recognized government "
         "(Al Mudhaffar in Taiz, Qa’tabah in Ad-Dali governorate and Tuban in Lahj) found that the assistance made up the majority of these "
         "households’ cash income; Qa’tabah reported the largest assistance share of the three areas (68%). Loans from informal "
         "support networks were the second-largest share in Al Mudhaffar (47%) and Qa’tabah (26%), and gifts the smallest "
         "share in all three areas. In Al Mudhaffar, "
         "26% of the households reported an increased ability to give to their networks after receiving the assistance, "
         "against 4% reporting an increased ability to receive support."),
        ("summary_ar",
         "وفق مسح لتحالف النقد في اليمن جُمعت بياناته في يونيو 2024 من أسر تتلقى مساعدات نقدية متعددة الأغراض في ثلاث مناطق "
         "تسميها الدراسة عُزلًا وتقول إنها تقع في المناطق الخاضعة للحكومة المعترف بها دوليًا (المظفر في تعز، وقعطبة في محافظة الضالع، وتُبن في "
         "لحج)، شكّلت المساعدات معظم الدخل النقدي لهذه الأسر، وسجّلت قعطبة أكبر حصة للمساعدات بين المناطق الثلاث (68%). "
         "وجاءت القروض من شبكات الدعم غير الرسمية في المرتبة الثانية في المظفر (47%) وقعطبة (26%)، وكانت الهدايا أصغر الحصص "
         "في المناطق الثلاث. وفي المظفر أفادت 26% من الأسر بأن قدرتها على تقديم الدعم "
         "لشبكاتها ازدادت بعد تلقي المساعدات، مقابل 4% أفادت بازدياد قدرتها على تلقي الدعم."),
        ("definition_en",
         "The average share of earnings, gifts, loans and cash assistance in the cash income of sampled households receiving "
         "multipurpose cash assistance, and the changes in giving and receiving support that they reported."),
        ("definition_ar",
         "متوسط حصة الكسب والهدايا والقروض والمساعدات النقدية في الدخل النقدي لأسر العينة التي تتلقى مساعدات نقدية متعددة "
         "الأغراض، والتغيرات التي أفادت بها في تقديم الدعم وتلقيه."),
        ("period_en", "Data collected in June 2024; the period the income questions refer to is not printed"),
        ("period_ar", "جُمعت البيانات في يونيو 2024؛ ولا تُذكر الفترة التي تشير إليها أسئلة الدخل"),
        ("universe_en",
         "Households that received multipurpose cash assistance from a Cash Consortium of Yemen partner from December 2023 to "
         "May 2024 in Al Mudhaffar, Qa’tabah and Tuban, three areas the study calls sub-districts; it describes each sample as "
         "representative of those recipients at sub-district level, and does not state its sampling method or weighting."),
        ("universe_ar",
         "الأسر التي تلقت مساعدات نقدية متعددة الأغراض من أحد شركاء تحالف النقد في اليمن بين ديسمبر 2023 ومايو 2024 في المظفر "
         "وقعطبة وتُبن، وهي ثلاث مناطق تسميها الدراسة عُزلًا؛ وتصف الدراسة كل عينة بأنها ممثلة لأولئك المستفيدين على مستوى العزلة، ولا تذكر "
         "طريقة المعاينة ولا الترجيح."),
        ("method_en",
         "A household survey by Cash Consortium of Yemen partners using Mercy Corps’s Informal Social Protection Index; the "
         "study compares the cash income households report with the assistance amount (YER 240,000). Values and rankings are "
         "those printed in the report’s text (p. 9), not the data labels on its figure, and the shares are not summed."),
        ("method_ar",
         "مسح أسري أجراه شركاء تحالف النقد في اليمن باستخدام مؤشر الحماية الاجتماعية غير الرسمية التابع لمنظمة ميرسي كور "
         "(Mercy Corps)؛ وتقارن الدراسة الدخل النقدي الذي تفيد به الأسر بمبلغ المساعدة (240,000 ريال يمني). والقيم والترتيب هي "
         "المطبوعة في نص التقرير (ص 9)، لا القيم المدوّنة على الشكل البياني، ولا تُجمع الحصص."),
        ("limitations_en",
         "The shares describe cash-assistance recipients in three areas, not households in Yemen, and gifts and loans "
         "from informal networks are not remittances: the study prints no channel, frequency, amount or split between support "
         "from inside and outside Yemen. | The changes in giving and receiving are recipients’ own reports, with no baseline "
         "or comparison group, and the study draws no causal link."),
        ("limitations_ar",
         "تصف الحصص متلقي المساعدات النقدية في ثلاث مناطق، لا الأسر في اليمن، والهدايا والقروض من الشبكات غير الرسمية ليست "
         "حوالات: فالدراسة لا تورد قناةً ولا تكرارًا ولا مبلغًا، ولا توزيعًا للدعم بين ما يأتي من داخل اليمن وما يأتي من "
         "خارجه. | التغيرات في تقديم "
         "الدعم وتلقيه هي ما أفاد به المستفيدون أنفسهم، دون خط أساس أو مجموعة مقارنة، ولا تستخلص الدراسة أي علاقة سببية."),
        ("currentness_en",
         "Data were collected in June 2024; the report prints no date, and ReliefWeb lists it as posted on 14 November 2024 "
         "(checked on 11 October 2026)."),
        ("currentness_ar",
         "جُمعت البيانات في يونيو 2024؛ ولا يحمل التقرير تاريخًا مطبوعًا، ويذكر موقع ReliefWeb أنه نُشر على الموقع في 14 نوفمبر 2024 (جرى "
         "التحقق في 11 أكتوبر 2026)."),
        ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
        ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
        ("source_dependencies", ISP),
        ("lineage_state", "BOUND_EXACT"),
        ("value_states", [
            vs("68%", "v", "READ", ISP, "The Unseen Assistance, printed p.9 (PDF p.10): 'Qa’tabah reporting the largest MPCA proportion (68%)'"),
            vs("47%", "v", "READ", ISP, "same, p.9: 'Loans comprised the second-highest proportion contribution of cash income in Al Mudhaffar (47%)'"),
            vs("26%", "v", "READ", ISP, "same, p.9: 'and Qa’tabah (26%)'; and 'a much greater proportion of HHs reported an increased ability to provide assistance (26%)' (Al Mudhaffar)"),
            vs("4%", "v", "READ", ISP, "same, p.9: 'compared to the proportion reporting an increased ability to receive support (4%)'"),
            vs("240,000", "v", "READ", ISP, "same, p.9: 'the amount of MPCA distributed to a HH (YER 240,000)'"),
            vs("9", "v", "TRIVIAL"),
            vs("June 2024", "d", "READ", ISP, "same, p.5 (PDF p.6): 'Data was collected in June 2024'"),
            vs("December 2023", "d", "READ", ISP, "same, p.5: 'from a CCY partner from December 2023 to May 2024'"),
            vs("May 2024", "d", "READ", ISP, "same, p.5"),
            vs("14 November 2024", "d", "READ", ISP, "ReliefWeb landing page: 'Posted 14 Nov 2024'"),
            vs("11 October 2026", "d", "SITE", None, None)]),
        ("meta_en", "A 2024 Cash Consortium of Yemen survey: cash assistance made up most of recipients’ cash income in three areas; informal loans came second in two."),
        ("meta_ar", "مسح لتحالف النقد في اليمن عام 2024: شكّلت المساعدات النقدية معظم الدخل النقدي للمستفيدين في ثلاث مناطق، وجاءت القروض غير الرسمية ثانيةً في اثنتين منها."),
    ]),
    OrderedDict([
        ("object_id", "CCY-SAM-2024"), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/remittances/"),
        ("title_en", "Income sources reported by cash-assistance households, with a multiplier estimate, in selected villages of Ad-Dali and Ja’ar (CCY pilot study, 2024)"),
        ("title_ar", "مصادر الدخل التي أفادت بها أسر تتلقى مساعدات نقدية، مع تقدير للمضاعف، في قرى مختارة من الضالع وجعار (دراسة تجريبية لتحالف النقد في اليمن، 2024)"),
        ("summary_en",
         "A 2024 Cash Consortium of Yemen pilot study reports that, on average, 61% of the households assessed in selected "
         "villages of Ad-Dali and Ja’ar, two areas it calls sub-districts and places under the internationally recognized "
         "government, named the cash assistance as a main income source in the 30 days before the interview, and 55% casual or "
         "daily wage labour; it notes that some respondents did not count money received by “hawala” (the study’s word) or "
         "debt as income. Using a single social accounting matrix for each locality, built from a survey of households "
         "receiving multipurpose cash assistance and interviews with local business owners, the study estimated that each US dollar of the assistance produced USD 2.56 of economic activity, the transfer included, in the Ad-Dali villages and "
         "USD 2.29 in the Ja’ar villages, and says the two values cannot be directly compared."),
        ("summary_ar",
         "تفيد دراسة تجريبية لتحالف النقد في اليمن عام 2024 بأن 61% في المتوسط من الأسر التي شملها التقييم في قرى مختارة من "
         "الضالع وجعار ذكرت المساعدات النقدية مصدرًا رئيسيًا للدخل خلال 30 يومًا سبقت المقابلة، وأن 55% ذكرت العمل العرضي أو "
         "بالأجر اليومي؛ والضالع وجعار منطقتان تسميهما الدراسة عزلتين وتقول إنهما تقعان في المناطق الخاضعة للحكومة المعترف بها "
         "دوليًا. وتشير الدراسة إلى أن بعض المستجيبين لم يحتسبوا ما تلقوه عن طريق «الحوالة» (بتعبير الدراسة) ولا الديون دخلًا. "
         "وباستخدام مصفوفة محاسبة اجتماعية واحدة لكل منطقة، بُنيت من مسح لأسر تتلقى مساعدات نقدية متعددة الأغراض ومقابلات مع "
         "أصحاب أعمال محليين، قدّرت الدراسة أن كل دولار أمريكي واحد من المساعدات أنتج نشاطًا اقتصاديًا قيمته 2.56 دولار، بما فيه "
         "التحويل النقدي نفسه، في قرى الضالع، و2.29 دولار في قرى جعار، وتذكر أن القيمتين لا تقبلان المقارنة المباشرة."),

        ("definition_en",
         "The main income sources the assessed households reported, and the study’s estimated ratio of total economic activity, "
         "the cash injected included, to the cash assistance injected in each locality."),
        ("definition_ar",
         "مصادر الدخل الرئيسية التي أفادت بها الأسر التي شملها التقييم، ونسبة إجمالي النشاط الاقتصادي، بما فيه النقد المضخوخ، "
         "إلى المساعدات النقدية المضخوخة في كل منطقة، كما تقدّرها الدراسة."),
        ("period_en",
         "The latest assistance distribution, October–December 2023; household survey in January 2024 (the report also gives "
         "January 2023 in one place)"),
        ("period_ar",
         "آخر توزيع للمساعدات بين أكتوبر وديسمبر 2023؛ والمسح الأسري في يناير 2024 (ويذكر التقرير أيضًا يناير 2023 في موضع واحد)"),
        ("universe_en",
         "Selected villages and towns of Ad-Dali (Ad-Dali governorate) and Ja’ar (Khanfar district, Abyan governorate), which "
         "the study calls sub-districts, that received the most assistance and were accessible: 291 household interviews in "
         "Ad-Dali and 209 in Ja’ar, with households that had received at least two rounds of assistance, and interviews with "
         "local businesses."),
        ("universe_ar",
         "قرى وبلدات مختارة من منطقتَي الضالع (محافظة الضالع) وجعار (مديرية خنفر، محافظة أبين)، وتسميهما الدراسة عزلتين، تلقت "
         "أكبر قدر من المساعدات وأمكن الوصول إليها: 291 مقابلة أسرية في الضالع و209 في جعار، مع أسر تلقت جولتين على الأقل من "
         "المساعدات، إضافة إلى مقابلات مع منشآت تجارية محلية."),
        ("method_en",
         "A multiplier from a single social accounting matrix for each locality, a snapshot at constant prices with fixed "
         "spending shares: total economic activity, the injection included, divided by the cash injected. It counts first-round "
         "effects only, leaves out business owners’ and employees’ spending and spending outside the locality, and publishes no "
         "interval or range; Ja’ar’s matrices are not printed, so its value cannot be recomputed from the report."),
        ("method_ar",
         "مضاعف مستخرج من مصفوفة محاسبة اجتماعية واحدة لكل منطقة، تمثل لقطة بأسعار ثابتة وحصص إنفاق ثابتة: إجمالي النشاط "
         "الاقتصادي، بما فيه النقد المضخوخ، مقسومًا على النقد المضخوخ. ولا يحتسب إلا آثار الجولة الأولى من الإنفاق، ويستبعد "
         "إنفاق أصحاب الأعمال والعاملين لديهم والإنفاق خارج المنطقة، ولا تُنشر له فترة ثقة ولا مدى؛ ولم ينشر التقرير مصفوفات "
         "جعار، فلا يمكن إعادة حساب قيمتها منه."),
        ("limitations_en",
         "The multipliers are model estimates for selected villages, not a multiplier for Yemen or a governorate, and measure "
         "economic activity that includes the transfer, not household or local income; they say nothing about how money "
         "reaches households. | The income sources describe assistance recipients chosen for having received at least two "
         "rounds, so the share citing the assistance reflects how the sample was chosen; remittances and loans or support from "
         "family, friends and neighbours carry no printed value, which is missing, not zero."),
        ("limitations_ar",
         "المضاعفان تقديران مستخرجان من نموذج لقرى مختارة، لا مضاعف لليمن أو لمحافظة، ويقيسان نشاطًا اقتصاديًا يشمل التحويل "
         "النقدي نفسه، لا دخل الأسر أو الدخل المحلي؛ ولا يقولان شيئًا عن طريقة وصول المال إلى الأسر. | تصف مصادر الدخل متلقي "
         "مساعدات اختيروا لأنهم تلقوا جولتين على الأقل من المساعدات، فحصة من ذكروا المساعدات تعكس طريقة اختيار العينة؛ ولا تحمل "
         "الحوالات والقروض أو الدعم من الأسرة والأصدقاء والجيران أي قيمة مطبوعة، وهذا غياب للبيانات لا صفر."),
        ("currentness_en",
         "The household survey ran in January 2024; the report prints no date, and its host lists it under November 2024 "
         "(checked on 11 October 2026)."),
        ("currentness_ar",
         "أُجري المسح الأسري في يناير 2024؛ ولا يحمل التقرير تاريخًا مطبوعًا، ويُدرجه الموقع الذي يستضيفه ضمن ملفات نوفمبر 2024 (جرى "
         "التحقق في 11 أكتوبر 2026)."),
        ("change_trigger_en", TRIGGER_EN), ("change_trigger_ar", TRIGGER_AR),
        ("verification_en", BOUND_EN), ("verification_ar", BOUND_AR),
        ("source_dependencies", SAM),
        ("lineage_state", "BOUND_EXACT"),
        ("value_states", [
            vs("2.56", "v", "READ", SAM, "The Multiplier Effect of MPCA, printed p.26 (PDF p.27): 'The estimated multiplier effect for Ad-Dali’s was 2.56'; also p.1 and p.35"),
            vs("2.29", "v", "READ", SAM, "same, p.26: 'The estimated multiplier effect for Ja’ar was 2.29'"),
            vs("61%", "v", "READ", SAM, "same, p.12 (PDF p.13): 'humanitarian cash assistance (61%)'"),
            vs("55%", "v", "READ", SAM, "same, p.12: 'casual/daily wage labor (55%)'; hawala limitation p.36 (PDF p.37)"),
            vs("30", "v", "READ", SAM, "same, p.12: income sources 'in the 30 days prior to the interview'"),
            vs("291", "v", "READ", SAM, "same, p.2 (PDF p.3): '291 HH interviews in Ad-Dali and 209 in Ja’ar'"),
            vs("209", "v", "READ", SAM, "same, p.2"),
            vs("December 2023", "d", "READ", SAM, "same, p.26: cash injection 'between October and December 2023'"),
            vs("January 2024", "d", "READ", SAM, "same, p.7 (PDF p.8): 'In January 2024, the CCY conducted a HH survey'"),
            vs("January 2023", "d", "READ", SAM, "same, p.32 (PDF p.33): 'mid-January 2023' (the report's own inconsistency)"),
            vs("November 2024", "d", "READ", SAM, "host path calpnetwork.org/wp-content/uploads/2024/11/"),
            vs("11 October 2026", "d", "SITE", None, None)]),
        ("meta_en", "A 2024 Cash Consortium of Yemen pilot: on average, 61% of assessed households named aid a main income source; estimated activity per aid dollar in selected villages, aid included: USD 2.56 and 2.29."),
        ("meta_ar", "دراسة تجريبية لتحالف النقد في اليمن عام 2024: ذكرت 61% من الأسر المشمولة، في المتوسط، المساعدات مصدرًا رئيسيًا للدخل؛ والنشاط المقدَّر في قرى مختارة 2.56 و2.29 دولار لكل دولار، بما فيه المساعدات."),
    ]),
]
