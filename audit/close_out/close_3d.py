# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-3D: the cost of sending money to Yemen (brief v5 W3c, Appendix B U7; closes FRN-09).
English and Arabic change together.

  python3 close_3d.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes <work_dir>/visual_design_contract.json for run_stage.py --install.

Read on 10 October 2026, never from a live call at run time: the World Bank's open API for World Development Indicators
series SI.RMT.COST.IB.ZS, Yemen (dated snapshot audit/close_out/fixtures/wdi_rmt_cost_2026-10-10.json, lastupdated
2026-10-08), and the UN metadata for SDG indicator 10.c.1 (unstats.un.org, last updated 2026-03-27; definition section
2.a, read in the PDF). The Remittance Prices Worldwide corridor pages refused automated requests that day; the World
Bank's data catalogue still holds the dataset ending with the third quarter of 2025 (audit/close_out/w0/A1_findex_wb.md),
so the corridor values stay at that quarter and say so.

- U7. VIS-REMITTANCE-COST keeps its contract and gains a second panel: the World Bank's yearly average cost of sending
  US$200 to Yemen across the services and corridors Remittance Prices Worldwide surveys (2016, 2017, 2022 and 2023, the
  only years with a value), apart from the 2025 Q3 corridor panel and never compared with it. The values are printed to
  the two decimals the API states for the series (the API carries 4.68109…, 5.70931…, 3.455 and 2.805). The frame says
  that both measure the price of sending, not the cost of collecting money in Yemen or a household's cost, and states
  SDG target 10.c as a reference line in words, not a pass mark and
  not drawn (the 3% applies to the global average and the 5% to each corridor's SmaRT average of the three cheapest
  qualifying services, neither of which the panels show). 23_REMITTANCES gains the four rows; two sources (the WDI series and
  the UN metadata) are added; the corridor note names its panel; the record
  VIS-REMITTANCE-COST and its 11 row describe both panels. FRN-09 (no record of SDG 10.c.1) closes.
"""
import json, os, sys, unicodedata
from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, insert_ui_rows, set_ui  # noqa: E402

F = "CLOSE-3D"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")
FIXTURE = os.path.join(HERE, "fixtures", "wdi_rmt_cost_2026-10-10.json")
TODAY = "2026-10-10"
VID = "VIS-REMITTANCE-COST"
WDI = "SRC-WB-WDI-RMT-COST-YEM"
SDG = "SRC-UN-SDG-10C1-METADATA"
WDI_URL = "https://data.worldbank.org/indicator/SI.RMT.COST.IB.ZS?locations=YE"
WDI_API = "https://api.worldbank.org/v2/country/YEM/indicator/SI.RMT.COST.IB.ZS?format=json&per_page=100"
SDG_URL = "https://unstats.un.org/sdgs/metadata/files/Metadata-10-0c-01.pdf"
YEARS = (2016, 2017, 2022, 2023)
RMT_IDS = {y: f"RMO-WDI-RMTCOST-{y}" for y in YEARS}

# ================================================================================================ the governed strings (04)
UI = [  # (ui_id, en, ar, note)
    ("UI-VIS-PANEL-RMT-RPW", "Two of the corridors to Yemen, by amount sent: third quarter of 2025",
     "ممران من الممرات إلى اليمن، بحسب المبلغ المرسل: الربع الثالث من 2025",
     "Close-out U7. Panel heading of VIS-REMITTANCE-COST (corridor averages)."),
    ("UI-VIS-PANEL-RMT-WDI", "Yemen, across the services the World Bank surveys: yearly average for sending US$200",
     "اليمن، عبر الخدمات التي يرصد البنك الدولي أسعارها: المتوسط السنوي لإرسال 200 دولار أمريكي",
     "Close-out U7. Panel heading of VIS-REMITTANCE-COST (World Development Indicators SI.RMT.COST.IB.ZS)."),
    ("UI-VIS-NOTE-RMT-WDI-YEARS",
     "World Development Indicators carries this yearly average for Yemen for 2016, 2017, 2022 and 2023 only; it holds no "
     "value for 2018 to 2021 or after 2023 (checked on 10 October 2026). A year without a value does not mean zero. The "
     "services and corridors sampled can differ between years, so a change between years is not by itself a change in "
     "what senders pay, and the two panels are not one series.",
     "لا تتضمن مؤشرات التنمية العالمية هذا المتوسط السنوي لليمن إلا للسنوات 2016 و2017 و2022 و2023؛ ولا قيمة فيها للسنوات من "
     "2018 إلى 2021 ولا لما بعد 2023 (جرى التحقق في 10 أكتوبر 2026). وغياب القيمة عن سنةٍ ما لا يعني صفرًا. وقد تختلف "
     "الخدمات والممرات المشمولة بالعيّنة بين سنة وأخرى، فلا يعني التغير بين السنوات بذاته تغيرًا فيما يدفعه المرسلون، واللوحتان ليستا "
     "سلسلة واحدة.", "Close-out U7. Frame note of VIS-REMITTANCE-COST."),
    ("UI-VIS-NOTE-RMT-PRICE",
     "Both panels measure the price of sending money through the services surveyed (fees and the exchange-rate margin), "
     "as simple averages of the prices quoted, not weighted by the amounts sent; not the cost of collecting the money in "
     "Yemen or the cost to a household.",
     "تقيس اللوحتان كلتاهما سعر إرسال المال عبر الخدمات المرصودة (الرسوم وهامش سعر الصرف)، في صورة متوسطات بسيطة للأسعار "
     "المعروضة غير مرجّحة بالمبالغ المرسلة؛ لا تكلفة استلام المال في اليمن ولا التكلفة التي تتحملها الأسرة.",
     "Close-out U7. Frame note of VIS-REMITTANCE-COST (price of sending, brief U7)."),
    ("UI-VIS-NOTE-SDG-10C",
     "Reference, not a pass mark: SDG target 10.c aims, by 2030, to reduce the transaction costs of migrant remittances "
     "to less than 3% and to eliminate corridors with costs higher than 5% (UN metadata for indicator 10.c.1, last updated "
     "27 March 2026). The 3% applies to the global average cost of sending US$200, not to one country; the 5% applies, in "
     "each corridor, to the average of the three cheapest qualifying services (the World Bank's SmaRT measure), not to the "
     "corridor averages shown here. Neither panel shows either measure, and no value here is marked as meeting or missing "
     "the target.",
     "مرجع لا معيار نجاح: تهدف الغاية 10.c من أهداف التنمية المستدامة إلى خفض تكاليف معاملات تحويلات المهاجرين إلى أقل من 3% "
     "بحلول 2030، وإلغاء الممرات التي تزيد تكاليفها على 5% (البيانات الوصفية للمؤشر 10.c.1 الصادرة عن الأمم المتحدة، آخر "
     "تحديث في 27 مارس 2026). وتنطبق نسبة 3% على المتوسط العالمي لتكلفة إرسال 200 دولار أمريكي، لا على بلد بعينه؛ وتنطبق "
     "نسبة 5% في كل ممر على متوسط أرخص ثلاث خدمات مؤهلة (مقياس SmaRT لدى البنك الدولي)، لا على متوسطات الممرين المعروضة "
     "هنا. ولا تعرض أيّةُ لوحة من اللوحتين أيًّا من المقياسين، ولا تُوسَم أي قيمة هنا بأنها تحقق الغاية أو تقصر عنها.",
     "Close-out U7. Frame note of VIS-REMITTANCE-COST (SDG 10.c as a reference line in words; FRN-09)."),
]
# the existing corridor note now stands after two panels: it names its panel (close-out U7)
RPW_NOTE = ("UI-VIS-RPW-AVERAGE-NOTE", "Average of quotes for this amount — not the cost of all remittances",
            "متوسط عروض الأسعار لهذا المبلغ — وليس تكلفة جميع الحوالات",
            "Corridor panel: each value is the average of quotes for its amount — not the cost of all remittances",
            "لوحة الممرين: كل قيمة هي متوسط عروض الأسعار لمبلغها — وليست تكلفة جميع الحوالات")

# ================================================================================================ 23: the yearly averages
ROW = OrderedDict([
    ("source_id", WDI), ("series_vintage", "WDI_LASTUPDATED_2026-10-08"), ("domain", "remittance_country_costs"),
    ("geography", "Yemen (corridors to Yemen in Remittance Prices Worldwide)"), ("period_state", "ANNUAL_PUBLISHED_AVERAGE"),
    ("metric_id", "RMT-003"), ("metric_label_en", "Average cost of sending US$200 to Yemen"),
    ("metric_label_ar", "متوسط تكلفة إرسال 200 دولار أمريكي إلى اليمن"), ("unit", "percent of send amount"),
    ("transaction_amount_usd", 200), ("corridor_destination", "Yemen"), ("evidence_type", "PRIMARY_OFFICIAL_COUNTRY_AVERAGE"),
    ("universe", "Remittance service providers included in Remittance Prices Worldwide for sending US$200 to Yemen"),
    ("calculation_state", "SOURCE_PUBLISHED_AVERAGE"), ("comparability_state", "COUNTRY_AVERAGE__NOT_ONE_SERIES_WITH_CORRIDORS"),
    ("caveat_en", "The World Bank's yearly average for Yemen of the total cost of sending US$200: a simple average of the prices "
                  "quoted by the remittance service providers that Remittance Prices Worldwide includes for Yemen, not weighted by "
                  "the amounts sent. A price of sending (fees and the exchange-rate margin), not the cost of collecting the money "
                  "in Yemen or a household's cost; not one series with the 2025 Q3 corridor averages."),
    ("caveat_ar", "المتوسط السنوي الذي ينشره البنك الدولي لليمن، للتكلفة الإجمالية لإرسال 200 دولار أمريكي: متوسط بسيط للأسعار التي "
                  "يعرضها مقدمو خدمات الحوالات الذين تشملهم قاعدة Remittance Prices Worldwide لليمن، غير مرجّح بالمبالغ المرسلة. "
                  "وهو سعر للإرسال (الرسوم وهامش سعر الصرف)، لا تكلفة استلام المال في اليمن ولا تكلفة تتحملها الأسرة؛ ولا يشكّل مع "
                  "متوسطات الممرين للربع الثالث من 2025 سلسلة واحدة."),
    ("source_url", WDI_URL),
])
INDICATOR = OrderedDict([("dataset_id", "DS-REMITTANCES"), ("indicator_or_metric_id", "RMT-003"),
                         ("label", "Average cost of sending US$200 to Yemen (World Bank yearly average)"),
                         ("domain", "Remittances & exchange"), ("units", "percent of send amount"), ("rows", 4),
                         ("period_min", 2016), ("period_max", 2023),
                         ("use_rule", "Use only within the dataset's comparability/publication rules.")])


def src_row(sid, url, more, use, rows, title, title_ar, pub, pub_ar, label, label_ar, date, issuer=None):
    return OrderedDict([("source_id", sid), ("primary_url", url), ("additional_urls", json.dumps(more) if more else None),
                        ("datasets_or_use", use), ("row_count", rows), ("display_title", title), ("display_title_ar", title_ar),
                        ("publisher", pub), ("publisher_ar", pub_ar), ("issuer", issuer), ("public_card_state", "CITATION_CARD"),
                        ("rights_state", "NOT_ASSESSED"), ("retrieval_date", TODAY), ("document_label", label),
                        ("document_label_ar", label_ar), ("document_date", date)])


NEW_SOURCES = [
    src_row(WDI, WDI_URL, [WDI_API], "DS-REMITTANCES", 4,
            "World Development Indicators: average transaction cost of sending remittances to Yemen (SI.RMT.COST.IB.ZS)",
            "مؤشرات التنمية العالمية: متوسط تكلفة معاملة إرسال الحوالات إلى اليمن (SI.RMT.COST.IB.ZS)",
            "World Bank", "البنك الدولي", "Survey dataset or indicator", "مسح أو مؤشر", "2026-10-08",
            issuer="World Bank, Remittance Prices Worldwide (data); World Bank, World Development Indicators"),
    src_row(SDG, SDG_URL, None, "RESOURCE_LIBRARY_ONLY__REFERENCE_TARGET", 0,
            "SDG indicator metadata 10.c.1: remittance costs as a proportion of the amount remitted (last updated 27 March "
            "2026)",
            "البيانات الوصفية لمؤشر أهداف التنمية المستدامة 10.c.1: تكاليف التحويلات المالية نسبةً من المبلغ المحوَّل (آخر تحديث "
            "في 27 مارس 2026)",
            "United Nations Statistics Division", "الشعبة الإحصائية للأمم المتحدة", "Method or standard", "منهج أو معيار",
            "2026-03-27", issuer="World Bank (custodian agency of indicator 10.c.1)"),
]

# ================================================================================================ 06 and 11: VIS-REMITTANCE-COST
TITLE = ("The cost of sending money to Yemen: two corridors in 2025 Q3 and the World Bank's yearly average",
         "تكلفة إرسال الأموال إلى اليمن: ممران في الربع الثالث من 2025 والمتوسط السنوي للبنك الدولي")
OLD_TITLE = "Quoted cost of sending US$200 and US$500 to Yemen from Saudi Arabia and the UAE, 2025 Q3"
LIM_A = ("The corridor averages cover two corridors, two send amounts and formal products listed by Remittance Prices "
         "Worldwide in one quarter; the yearly averages cover the services it includes for sending US$200 to Yemen. Neither "
         "gives the cost of all remittances to Yemen, and neither covers informal channels; both are prices of sending, not "
         "the cost of collecting the money in Yemen or a household's cost; and the two panels are not one series.",
         "تغطي متوسطات الممرات ممرين ومبلغي إرسال ومنتجات رسمية مدرجة في قاعدة Remittance Prices Worldwide في ربع واحد؛ وتغطي "
         "المتوسطات السنوية الخدمات التي تشملها القاعدة لإرسال 200 دولار أمريكي إلى اليمن. ولا يبيّن أيٌّ منهما تكلفة جميع "
         "الحوالات إلى اليمن، ولا يشمل أيٌّ منهما القنوات غير الرسمية؛ وكلاهما سعر للإرسال، لا تكلفة استلام المال في اليمن ولا "
         "تكلفة تتحملها الأسرة؛ واللوحتان ليستا سلسلة واحدة.")
LIM_B_ADD = (" World Development Indicators carries the yearly average for 2016, 2017, 2022 and 2023 only, and a year without a "
             "value does not mean zero; the services and corridors sampled can differ between years, so a change between years "
             "is not by itself a change in what senders pay.",
             " ولا تتضمن مؤشرات التنمية العالمية المتوسط السنوي إلا للسنوات 2016 و2017 و2022 و2023، وغياب القيمة عن سنةٍ ما لا يعني "
             "صفرًا؛ وقد تختلف الخدمات والممرات المشمولة بالعيّنة بين سنة وأخرى، فلا يعني التغير بين السنوات بذاته تغيرًا فيما يدفعه "
             "المرسلون.")
# the corridor sentence of the summary now points to the yearly average below it (close-out U7 red-team S3)
SUMMARY_FIX = (("they are not a national Yemen remittance-cost average and do not cover all providers or informal channels.",
                "they are not the World Bank's yearly average for Yemen (below) and do not cover all providers or informal "
                "channels."),
               ("وليست متوسطًا وطنيًا لتكلفة الحوالات إلى اليمن، ولا تغطي جميع مقدمي الخدمة أو القنوات غير الرسمية.",
                "وليست المتوسط السنوي الذي ينشره البنك الدولي لليمن (أدناه)، ولا تغطي جميع مقدمي الخدمة أو القنوات غير الرسمية."))
SUMMARY_ADD = (" Separately, the World Bank's yearly average cost of sending US$200 to Yemen, a simple average across the services "
               "Remittance Prices Worldwide includes, was 4.68% in 2016, 5.71% in 2017, 3.46% in 2022 and 2.81% in 2023; World "
               "Development Indicators carries no value for 2018 to 2021 or after 2023. Both kinds of average are prices of "
               "sending, not the cost of collecting the money in Yemen, and they are not one series.",
               " وبمعزل عن ذلك، بلغ المتوسط السنوي الذي ينشره البنك الدولي لتكلفة إرسال 200 دولار أمريكي إلى اليمن، وهو متوسط بسيط عبر "
               "الخدمات التي تشملها قاعدة Remittance Prices Worldwide، 4.68% في 2016، و5.71% في 2017، و3.46% في 2022، و2.81% في "
               "2023؛ ولا تتضمن مؤشرات التنمية العالمية أي قيمة للسنوات من 2018 إلى 2021 ولا لما بعد 2023. وكلا النوعين من المتوسطات "
               "سعرٌ للإرسال، لا تكلفة استلام المال في اليمن، ولا يشكّلان سلسلة واحدة.")
DEFINITION_ADD = (" Separately, the World Bank's yearly average for Yemen: the simple average of the total transaction cost, as a "
                  "percentage of US$200, quoted by each remittance service provider that Remittance Prices Worldwide includes for "
                  "sending to Yemen, not weighted by the amounts sent (World Development Indicators, SI.RMT.COST.IB.ZS).",
                  " وبمعزل عن ذلك، المتوسط السنوي الذي ينشره البنك الدولي لليمن: المتوسط البسيط للتكلفة الإجمالية للمعاملة، نسبةً مئوية "
                  "من 200 دولار أمريكي، التي يعرضها كلُّ مقدّمٍ لخدمات الحوالات تشمله قاعدة Remittance Prices Worldwide للإرسال إلى "
                  "اليمن، غير مرجّح بالمبالغ المرسلة (مؤشرات التنمية العالمية، SI.RMT.COST.IB.ZS).")
PERIOD = ("2025 Q3 (corridor averages); 2016, 2017, 2022 and 2023 (yearly averages)",
          "الربع الثالث من 2025 (متوسطات الممرين)؛ 2016 و2017 و2022 و2023 (المتوسطات السنوية)")
UNIVERSE_ADD = ("; and, for the yearly averages, the remittance service providers Remittance Prices Worldwide includes for "
                "sending US$200 to Yemen",
                "؛ وللمتوسطات السنوية، مقدمو خدمات الحوالات الذين تشملهم قاعدة Remittance Prices Worldwide لإرسال 200 دولار أمريكي "
                "إلى اليمن")
METHOD_ADD = (" The yearly averages are the World Bank's published values of World Development Indicators series "
              "SI.RMT.COST.IB.ZS for Yemen, read from the World Bank's open data API on 10 October 2026 (series last updated 8 "
              "October 2026); they are rounded half up to the two decimals the API states for the series (the API carries "
              "4.68109…, 5.70931…, 3.455 and 2.805). The SDG 10.c reference (a global average below 3% by 2030; in every "
              "corridor, a SmaRT average of the three cheapest qualifying services of 5% or less) is quoted from the UN metadata "
              "for indicator 10.c.1 (last updated 27 March 2026), whose custodian agency is the World Bank.",
              " والمتوسطات السنوية هي القيم التي ينشرها البنك الدولي لسلسلة مؤشرات التنمية العالمية SI.RMT.COST.IB.ZS لليمن، قُرئت "
              "من واجهة البيانات المفتوحة للبنك الدولي في 10 أكتوبر 2026 (آخر تحديث للسلسلة في 8 أكتوبر 2026)؛ وهي مقرّبة إلى "
              "المنزلتين العشريتين اللتين تحددهما الواجهة للسلسلة، بتقريب النصف إلى الأعلى (تحمل الواجهة القيم 4.68109… و5.70931… "
              "و3.455 و2.805). ويُقتبس مرجع الغاية 10.c من أهداف التنمية المستدامة (متوسط عالمي أقل من 3% بحلول 2030؛ وفي كل ممر، "
              "متوسط SmaRT لأرخص ثلاث خدمات مؤهلة لا يزيد على 5%) من البيانات الوصفية للمؤشر 10.c.1 الصادرة عن الأمم المتحدة (آخر "
              "تحديث في 27 مارس 2026)، والوكالة الراعية لهذا المؤشر هي البنك الدولي.")
CURRENT = ("The corridor averages refer to the third quarter of 2025. On 10 October 2026 the corridor pages refused automated "
           "requests, and the World Bank's data catalogue still held the Remittance Prices Worldwide dataset ending with the "
           "third quarter of 2025, so no later quarter could be read. The yearly averages were read on 10 October 2026; the "
           "series was last updated on 8 October 2026 and holds no value after 2023.",
           "تعود متوسطات الممرين إلى الربع الثالث من 2025. وفي 10 أكتوبر 2026 رفضت صفحتا الممرين الطلبات الآلية، وكان فهرس بيانات "
           "البنك الدولي لا يزال يضم مجموعة بيانات Remittance Prices Worldwide المنتهية بالربع الثالث من 2025، فلم يتسنَّ قراءة ربع "
           "أحدث. وقُرئت المتوسطات السنوية في 10 أكتوبر 2026؛ وكان آخر تحديث للسلسلة في 8 أكتوبر 2026، ولا تتضمن أي قيمة بعد 2023.")
V11_SET = OrderedDict([
    ("question_en", ("How do quoted remittance costs differ by corridor and transfer size?",
                     "How do quoted remittance costs differ by corridor and transfer size, and what is the World Bank's yearly "
                     "average for Yemen?")),
    ("question_ar", ("كيف تختلف تكلفة الحوالة المعلنة بحسب الممر ومبلغ التحويل؟",
                     "كيف تختلف تكلفة الحوالة المعلنة بحسب الممر ومبلغ التحويل، وما المتوسط السنوي الذي ينشره البنك الدولي لليمن؟")),
    ("source_period", ("2025-Q3", "2025-Q3; 2016, 2017, 2022, 2023 (annual)")),
    ("freshness_profile", ("2025-Q3", "2025-Q3; WDI last updated 2026-10-08")),
    ("data_inputs", ("17_REMITTANCES RPW corridor quotes + DA-010..013",
                     "23_REMITTANCES RPW corridor quotes (RMO-RPW-*) + DA-010..013; WDI SI.RMT.COST.IB.ZS yearly averages "
                     "(RMO-WDI-RMTCOST-*)")),
    ("unit_or_object", ("percent cost of sending a fixed amount / provider quote",
                        "percent cost of sending a fixed amount / provider quote; yearly average across providers")),
    ("period", ("2025 Q3", "2025 Q3; 2016, 2017, 2022 and 2023")),
])
WHAT_ADD = (" A separate panel shows the World Bank's yearly average cost of sending US$200 to Yemen for the four years with a "
            "value (2016, 2017, 2022 and 2023).",
            " وتعرض لوحة منفصلة المتوسط السنوي الذي ينشره البنك الدولي لتكلفة إرسال 200 دولار أمريكي إلى اليمن للسنوات الأربع التي لها "
            "قيمة (2016 و2017 و2022 و2023).")
ENCODING_ADD = (" A second panel shows the World Bank's yearly average for Yemen (US$200) as one dot per year with a value, on "
                "the same value axis and apart from the corridors; years without a value are named, not drawn; the SDG 10.c "
                "reference is stated in words in the frame, with no line and no pass or fail colouring.")
L_API = ("World Bank open data API (dated snapshot audit/close_out/fixtures/wdi_rmt_cost_2026-10-10.json of " + WDI_API
         + "), SI.RMT.COST.IB.ZS, YEM")
L_SDG = "UN SDG indicator metadata 10.c.1, " + SDG_URL + " (header 'Last updated: 2026-03-27')"


def vs(t, k, s, src=None, loc=None):
    e = OrderedDict([("t", t), ("k", k), ("s", s)])
    if src:
        e["src"], e["loc"] = src, loc
    return e


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    f7 = F + ":U7"

    # ---------------------------------------------------------------- the dated snapshot (never the live API)
    fx = json.load(open(FIXTURE, encoding="utf-8"))
    head, data = fx["data"]
    if head.get("lastupdated") != "2026-10-08":
        raise TxError(f"{f7}: the snapshot is not the 8 October 2026 vintage the text states")
    raw = {int(r["date"]): r for r in data if r["value"] is not None}
    if sorted(raw) != list(YEARS):
        raise TxError(f"{f7}: the snapshot holds values for {sorted(raw)}, not {YEARS}")
    shown, api = {}, {}
    for y in YEARS:
        r = raw[y]
        if r["indicator"]["id"] != "SI.RMT.COST.IB.ZS" or r["countryiso3code"] != "YEM" or r.get("decimal") != 2:
            raise TxError(f"{f7}: {y} is not the Yemen SI.RMT.COST.IB.ZS value with two stated decimals")
        api[y] = repr(r["value"])
        shown[y] = float(Decimal(api[y]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    if [shown[y] for y in YEARS] != [4.68, 5.71, 3.46, 2.81]:
        raise TxError(f"{f7}: the values shown differ from those the brief read on 10 October: {shown}")

    # ---------------------------------------------------------------- 23: four rows
    t23 = Table(s, "23_REMITTANCES")
    h23 = t23.head
    if any(rid in t23.rows for rid in RMT_IDS.values()):
        raise TxError(f"{f7}: 23 already holds the yearly averages")
    last23 = max(t23.rows.values())
    rows = []
    for y in YEARS:
        row = OrderedDict([("observation_id", RMT_IDS[y])] + list(ROW.items()))
        row["period"] = y
        row["value"] = shown[y]
        row["source_table_or_section"] = (f"World Development Indicators SI.RMT.COST.IB.ZS, Yemen, {y}: API value {api[y]}, "
                                          f"rounded half up to the two decimals the API states; read 10 October 2026 (series "
                                          f"last updated 8 October 2026)")
        rows.append(row)
    s.ed.insert_rows("23_REMITTANCES", last23 + 1, [{h23.index(k) + 1: v for k, v in r.items() if v is not None} for r in rows])
    for j, r in enumerate(rows):
        for k, v in r.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", f7), ("sheet", "23_REMITTANCES"), ("row", last23 + 1 + j),
                                             ("col", h23.index(k) + 1), ("field", f"{r['observation_id']}.{k}"),
                                             ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 17: the indicator row (its key repeats, so no Table)
    g17 = s.grid("17_INDICATOR_LIBRARY")
    hi = next(i for i, r in enumerate(g17) if r and r[0] == "dataset_id")
    h17 = [str(x) if x is not None else None for x in g17[hi]]
    body = [i for i, r in enumerate(g17[hi + 1:], start=hi + 1) if r and r[0] not in (None, "")]
    if any(g17[i][h17.index("indicator_or_metric_id")] == "RMT-003" for i in body):
        raise TxError(f"{f7}: 17 already lists RMT-003")
    after = max(i for i in body if g17[i][0] == "DS-REMITTANCES") + 1        # 0-based index of the last DS-REMITTANCES row
    s.ed.insert_rows("17_INDICATOR_LIBRARY", after + 1, [{h17.index(k) + 1: v for k, v in INDICATOR.items()}])
    for k, v in INDICATOR.items():
        s.ledger.append(OrderedDict([("finding", f7), ("sheet", "17_INDICATOR_LIBRARY"), ("row", after + 1),
                                     ("col", h17.index(k) + 1), ("field", f"RMT-003.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 15: two sources
    t15 = Table(s, "15_SOURCE_LIBRARY")
    held = {str(x) for r in s.grid("15_SOURCE_LIBRARY")[4:] if r for x in r[1:3] if x}
    for row in NEW_SOURCES:
        if row["source_id"] in t15.rows or row["primary_url"] in held:
            raise TxError(f"{f7}: {row['source_id']} or its locator is already in the library")
    h15 = t15.head
    last15 = max(t15.rows.values())
    s.ed.insert_rows("15_SOURCE_LIBRARY", last15 + 1,
                     [{h15.index(k) + 1: v for k, v in row.items() if v is not None} for row in NEW_SOURCES])
    for j, row in enumerate(NEW_SOURCES):
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", f7), ("sheet", "15_SOURCE_LIBRARY"), ("row", last15 + 1 + j),
                                             ("col", h15.index(k) + 1), ("field", f"{row['source_id']}.{k}"),
                                             ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 04
    insert_ui_rows(s, F, UI)
    set_ui(s, f7, RPW_NOTE[0], RPW_NOTE[3], RPW_NOTE[4], RPW_NOTE[1], RPW_NOTE[2])

    # ---------------------------------------------------------------- 06: the record VIS-REMITTANCE-COST
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    if t06.get(VID, "title_en") != OLD_TITLE:
        raise TxError(f"{f7}: {VID} is not the record expected")
    for lang, i in (("en", 0), ("ar", 1)):
        t06.set(f7, VID, f"title_{lang}", TITLE[i], t06.get(VID, f"title_{lang}"))
        cur = t06.get(VID, f"summary_{lang}")
        if cur.count(SUMMARY_FIX[i][0]) != 1:
            raise TxError(f"{f7}: {VID}.summary_{lang} does not hold the corridor sentence once")
        t06.set(f7, VID, f"summary_{lang}", cur.replace(SUMMARY_FIX[i][0], SUMMARY_FIX[i][1]).rstrip() + SUMMARY_ADD[i], cur)
        cur = t06.get(VID, f"definition_{lang}")
        t06.set(f7, VID, f"definition_{lang}", cur.rstrip() + DEFINITION_ADD[i], cur)
        t06.set(f7, VID, f"period_{lang}", PERIOD[i], t06.get(VID, f"period_{lang}"))
        cur = t06.get(VID, f"universe_{lang}")
        t06.set(f7, VID, f"universe_{lang}", cur.rstrip().rstrip(".") + UNIVERSE_ADD[i], cur)
        cur = t06.get(VID, f"method_{lang}")
        t06.set(f7, VID, f"method_{lang}", cur.rstrip() + METHOD_ADD[i], cur)
        cur = t06.get(VID, f"limitations_{lang}")
        part_a, sep, part_b = cur.partition(" | ")
        if not sep:
            raise TxError(f"{f7}: {VID}.limitations_{lang} has no part B")
        t06.set(f7, VID, f"limitations_{lang}", LIM_A[i] + " | " + part_b.rstrip() + LIM_B_ADD[i], cur)
        t06.set(f7, VID, f"currentness_{lang}", CURRENT[i], t06.get(VID, f"currentness_{lang}"))
    cur = t06.get(VID, "source_dependencies")
    deps = [x.strip() for x in str(cur).split(";") if x.strip()] if cur and not str(cur).startswith("[") else json.loads(cur or "[]")
    new_deps = deps + [x for x in (WDI, SDG) if x not in deps]
    t06.set(f7, VID, "source_dependencies", "; ".join(new_deps) if cur and not str(cur).startswith("[") else json.dumps(new_deps),
            cur)
    cur = t06.get(VID, "value_states")
    states = json.loads(cur)   # "26 September 2026" stays: other pages print that date and this record states it
    have = {(e["t"], e["k"]) for e in states}
    add = [vs(f"{shown[y]:.2f}%", "v", "DERIVED", WDI, f"{L_API}, date {y}, value {api[y]}, decimal 2, rounded half up to two "
                                                         f"decimals; read 10 October 2026") for y in YEARS]
    add += [vs(api[y][:7] if len(api[y]) > 7 else api[y], "v", "READ", WDI, f"{L_API}, date {y}, value {api[y]}") for y in YEARS]
    add += [vs("3%", "v", "READ", SDG, L_SDG + ", 0.b Target 10.c ('less than 3 per cent') and 4.c (component 1: the "
                                            "global average, a simple average of the total cost for all transparent services)"),
            vs("5%", "v", "READ", SDG, L_SDG + ", 0.b Target 10.c ('eliminate remittance corridors with costs higher than 5 "
                                            "per cent') and 4.c (component 2: in each corridor, the SmaRT average of the three "
                                            "cheapest qualifying services, 5 percent or lower)"),
            vs("10.c", "v", "LOCATOR"), vs("10.c.1", "v", "LOCATOR"),
            vs("10 October 2026", "d", "SITE"),
            vs("8 October 2026", "d", "READ", WDI, L_API + ", response header lastupdated 2026-10-08"),
            vs("27 March 2026", "d", "READ", SDG, L_SDG)]
    states += [e for e in add if (e["t"], e["k"]) not in have]
    t06.set(f7, VID, "value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")), cur)

    # ---------------------------------------------------------------- 11: the visual row
    t11 = Table(s, "11_VISUAL_LIBRARY")
    for lang, i in (("en", 0), ("ar", 1)):
        t11.set(f7, VID, f"title_{lang}", TITLE[i], t11.get(VID, f"title_{lang}"))
        t11.set(f7, VID, f"prohibited_inference_{lang}", LIM_A[i], t11.get(VID, f"prohibited_inference_{lang}"))
        cur = t11.get(VID, f"what_it_shows_{lang}")
        t11.set(f7, VID, f"what_it_shows_{lang}", cur.rstrip() + WHAT_ADD[i], cur)
        cur = t11.get(VID, f"accessible_summary_{lang}")
        if cur.count(SUMMARY_FIX[i][0]) != 1:
            raise TxError(f"{f7}: {VID}.accessible_summary_{lang} does not hold the corridor sentence once")
        t11.set(f7, VID, f"accessible_summary_{lang}",
                cur.replace(SUMMARY_FIX[i][0], SUMMARY_FIX[i][1]).rstrip() + SUMMARY_ADD[i], cur)
    for field, (old, new) in V11_SET.items():
        t11.set(f7, VID, field, new, old)
    cur = t11.get(VID, "denominator_universe")
    t11.set(f7, VID, "denominator_universe", cur.rstrip().rstrip(".") + UNIVERSE_ADD[0], cur)
    cur = t11.get(VID, "encoding_contract")
    t11.set(f7, VID, "encoding_contract", cur.rstrip() + ENCODING_ADD, cur)

    # ---------------------------------------------------------------- the contract: the second panel
    c = json.load(open(CONTRACT, encoding="utf-8"), object_pairs_hook=OrderedDict)
    v = next(x for x in c["visuals"] if x["visual_id"] == VID)
    k = v["contract"]
    if len(k["series"]) != 1 or k["series"][0]["id"] != "rpw":
        raise TxError(f"{f7}: {VID} does not hold the one corridor series expected")
    k["form"] = ("Dot plot: two corridors × two send amounts; the amount is an explicit axis, never pooled. A second panel: the "
                 "World Bank's yearly average for Yemen (US$200), one dot per year with a value, on the same value axis; never "
                 "joined to the corridor panel.")
    k["series"].append(OrderedDict([
        ("id", "wdi"),
        ("rows", OrderedDict([("file", "data/remittances.json"), ("header_key", "observation_id"),
                              ("where", OrderedDict([("observation_id", "^RMO-WDI-RMTCOST-")]))])),
        ("fields", OrderedDict([("x", "period"), ("group", "transaction_amount_usd"), ("y", "value"), ("unit", "unit"),
                                ("flag", "comparability_state"), ("source", "source_id"),
                                ("metric_label_en", "metric_label_en"), ("metric_label_ar", "metric_label_ar")])),
        ("state", "REPORTED"),
        ("expected_x", [str(y) for y in YEARS]),
        ("must_equal", OrderedDict((RMT_IDS[y], shown[y]) for y in YEARS)),
        ("label_fields", OrderedDict([("group", "amount_sent"), ("unit", "unit")]))]))
    k["ordering"] = "Corridor, then send amount ascending; the yearly panel in year order."
    k["missing"] = ("Provider and quote counts are not held; not drawn. The yearly average has no value for 2018 to 2021 or "
                    "after 2023: those years are named in the frame (UI-VIS-NOTE-RMT-WDI-YEARS), not drawn.")
    k["annotation"] = (k["annotation"] + " Panel headings UI-VIS-PANEL-RMT-RPW and UI-VIS-PANEL-RMT-WDI; frame notes "
                       "UI-VIS-NOTE-RMT-WDI-YEARS, UI-VIS-NOTE-RMT-PRICE and UI-VIS-NOTE-SDG-10C (the SDG 10.c reference in "
                       "words: no line, no pass or fail colouring).")
    k["credit"]["source_ids"] = list(k["credit"]["source_ids"]) + [WDI, SDG]
    k["mobile"] = "Two rows of paired dots; then one row per year."
    k["fallback"] = "Table: corridor, amount, cost (%); a second table: year, average cost (%)."
    k["frame_labels"] = ["UI-VIS-PANEL-RMT-RPW", "UI-VIS-PANEL-RMT-WDI"] + list(k.get("frame_labels") or []) + [
        "UI-VIS-NOTE-RMT-WDI-YEARS", "UI-VIS-NOTE-RMT-PRICE", "UI-VIS-NOTE-SDG-10C"]
    v["rationale"] = (v["rationale"] + " Close-out U7: the World Bank's yearly average for Yemen is a second panel, shown "
                      "on the same scale but not as one series with the corridor panel.")
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "U7: the World Bank's yearly average cost of sending US$200 to Yemen (WDI SI.RMT.COST.IB.ZS; 2016, 2017, "
                    "2022, 2023) as a second panel of VIS-REMITTANCE-COST; the price-of-sending note; SDG 10.c as a reference "
                    "line in words (FRN-09); RPW stays at 2025 Q3, the latest quarter readable."),
        ("self_counts", counts)]))
    print(json.dumps({k_: rep[k_] for k_ in ("input_master_sha256", "output_master_sha256", "cells_written")}))


def _nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, tuple):
        return tuple(_nfc(x) for x in o)
    if isinstance(o, list):
        return [_nfc(x) for x in o]
    if isinstance(o, dict):
        return type(o)((_nfc(k), _nfc(v)) for k, v in o.items())
    return o


for _name in [n for n in list(globals()) if n.isupper() and not n.startswith("_")]:
    globals()[_name] = _nfc(globals()[_name])


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
