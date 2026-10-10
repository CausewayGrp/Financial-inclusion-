# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-3C: the monetary context of the Central Bank of Yemen – Aden (brief v5 W3c, Appendix B
U4) and the bank-composition visual of Reading CWR-011 (U5). English and Arabic change together.

  python3 close_3c.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes <work_dir>/visual_design_contract.json for run_stage.py --install.

Read in the original: Monetary and Financial Developments, Issue No. 55 (June 2026), Tables 1, 4, 5 and 6 (printed pp.10,
15, 16, 17; PDF pp.11, 16, 17, 18), the definitions (printed p.20) and the Disclaimer (printed p.23, PDF p.24),
english.cby-ye.com/files/6ab393186466e.pdf, on 10 October 2026, with the Arabic edition (cby-ye.com/files/6ab390fcaf357.pdf)
(audit/close_out/w0/A3_cby.md, MFD-55, MFD-T1, MFD-T4, MFD-RATE). Issue No. 56 (July 2026) is not published (W3a).

- U4. 18_CBY_MONETARY gains the June 2026 values of the ten series the new objects use; the end-2025 and May 2026 values
  the tables show beside them must equal Issue No. 55's, or the transaction stops. SRC-CBY-001 now names Issue No. 55
  (Issue No. 54, which carries the back data, stays a locator). Two visuals go to /finance/, in the page's Views, neither
  creating a route: a dated table of eight indicators at the end of 2025 and in June 2026 (VIS-CBY-MONETARY-SNAPSHOT,
  text-first, values and shares as the bulletin prints them; the rate row shows the December 2025 and June 2026 monthly
  averages, the same two columns as every other row) and the monthly average market rate, January 2017 to June 2026
  (VIS-YER-MARKET-RATE, the monthly line primitive of the POS panels; the June to August 2025 move annotated in the
  frame, nothing smoothed). The frame says the rate is the one CBY-Aden publishes, not the rate in Sana'a and not any
  single day's rate (the brief's "street rate" is not used: the English edition calls the series the parallel-market
  rate), and says nothing about why it moved. CLM-033 and Reading CWR-002 gain the 2025 episode: rial values fell as the
  rial strengthened, but the bulletin also amended its monetary and banking data to the IMF's Monetary and Financial
  Statistics Manual (2016) from December 2025, so valuation, the change of method and other movements cannot be
  separated. VIS-POS-VALUE says in its frame that its window spans the 2025 rate move. The firewall line (monetary
  aggregates describe the banking system, not people's access or use) and the coverage line close the tables: the
  bulletin defines banks as those operating in the Republic of Yemen but does not say which banks and branches report.
- U5. RV-CWR-011: the bound CBY-BANKS positions as a text-first table (end of 2025, May 2026, June 2026), with a note
  that the three lines do not add up to total assets; CWR-011 binds it. /finance/ is not added to CWR-011's domain
  surfaces: rule F2 lets an answer page carry at most two Readings and /finance/ carries CWR-002 and CWR-006 (an owner
  question); the same positions reach /finance/ in the dated table.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, insert_ui_rows  # noqa: E402

F = "CLOSE-3C"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")
TODAY = "2026-10-10"
I55 = "https://english.cby-ye.com/files/6ab393186466e.pdf"
I55_AR = "https://cby-ye.com/files/6ab390fcaf357.pdf"
I54 = "https://english.cby-ye.com/files/6a5a2e6bcc3cd.pdf"
T1 = "Issue No. 55 (June 2026), Table 1 'Monetary Survey', printed p.10 (PDF p.11), column June 2026"
T4 = "Issue No. 55 (June 2026), Table 4 'Consolidated Balance Sheet of Commercial & Islamic Banks - Assets', printed p.15 (PDF p.16), column June 2026"
T6 = "Issue No. 55 (June 2026), Table 6 'Average Market Exchange Rates', printed p.17 (PDF p.18), row June, column 2026"

# ================================================================================================ 18: June 2026 (Issue No. 55)
JUNE = OrderedDict([   # indicator -> (value as printed, table locator)
    ("M2_BN_YER", (11925.0, T1)),
    ("CURRENCY_CIRCULATION_BN_YER", (3384.3, T1)),
    ("CURRENCY_CIRCULATION_SHARE_M2_PCT", (28.4, T1)),
    ("FX_DEPOSITS_BN_YER", (5807.6, T1)),
    ("FX_DEPOSITS_SHARE_TOTAL_DEPOSITS_PCT", (68.0, T1)),
    ("BANK_TOTAL_ASSETS_BN_YER", (13761.2, T4)),
    ("BANK_FOREIGN_ASSETS_BN_YER", (4650.0, T4)),
    ("BANK_CLAIMS_GOV_BN_YER", (1966.8, T4)),
    ("BANK_CREDIT_PRIVATE_SECTOR_BN_YER", (1362.9, T4)),
    ("YER_USD_MARKET_RATE", (1560.95, T6)),
])
# The same issue prints the end-2025 and May 2026 values the tables show beside June 2026; the Master's values (read
# from Issue No. 54) must equal them, or the transaction stops.
I55_EARLIER = OrderedDict([   # indicator -> (end of 2025 or December 2025, May 2026), as Issue No. 55 prints them
    ("M2_BN_YER", (11429.3, 11903.3)),
    ("CURRENCY_CIRCULATION_BN_YER", (3270.5, 3501.7)),
    ("CURRENCY_CIRCULATION_SHARE_M2_PCT", (28.6, 29.4)),
    ("FX_DEPOSITS_BN_YER", (5792.8, 5732.2)),
    ("FX_DEPOSITS_SHARE_TOTAL_DEPOSITS_PCT", (71.0, 68.2)),
    ("BANK_TOTAL_ASSETS_BN_YER", (12341.8, 13362.1)),
    ("BANK_FOREIGN_ASSETS_BN_YER", (4116.5, 4448.0)),
    ("BANK_CLAIMS_GOV_BN_YER", (1928.8, 2145.0)),
    ("BANK_CREDIT_PRIVATE_SECTOR_BN_YER", (1392.3, 1350.4)),
    ("YER_USD_MARKET_RATE", (1624.45, 1562.49)),
])
JUNE_NOTE = ("Read in the original on 10 October 2026 (close-out U4): {loc}. Only the series the close-out objects use are "
             "entered for June 2026.")
SRC_CBY = "SRC-CBY-001"
SRC_SET = OrderedDict([
    ("primary_url", I55),
    ("display_title", "Monetary and Financial Developments, Issue No. 55 (June 2026)"),
    ("display_title_ar", "التطورات النقدية والمالية، العدد 55 (يونيو 2026)"),
    ("document_date", "2026-06"),
    ("retrieval_date", TODAY),
])
NOTE_OLD_START = "The monetary series is a periodical. Every observation of this resource's monetary series is read from the issue"
SRC_NOTE = ("The monetary series is a periodical. Each observation records the issue it was read from: the June 2026 values "
            "from Issue No. 55 (June 2026), the primary locator, opened on 10 October 2026 with its Arabic edition, which is "
            "recorded beside it; every earlier value, including those for April and May 2026, from Issue No. 54 (May 2026), "
            "which carries the back-data tables and is also recorded beside it. Issue No. 55 prints the same end-2025 and "
            "May 2026 values for the ten series the close-out tables show. The thirteen issues for December 2021 to December "
            "2022 are recorded so a reader can also reach the issue that first published a monthly value of those two years, "
            "together with the bank's own index of the series and its regulations and publications pages. Issue No. 54 and "
            "those nineteen addresses were opened on 4 October 2026. The issue number of each was read from the document "
            "itself; the May 2022 issue prints no issue number, so none is stated for it.")

# ================================================================================================ the governed strings (04)
UI = [  # (ui_id, en, ar, note)
    ("UI-VIS-TH-CBY-ITEM", "Indicator (unit)", "المؤشر (الوحدة)", "Close-out U4. Row-header column of the CBY tables."),
    ("UI-VIS-TH-CBY-END-2025", "End of 2025", "نهاية 2025", "Close-out U4. Column: the 2025 year-end values of the bulletin."),
    ("UI-VIS-TH-CBY-2026-05", "May 2026", "مايو 2026", "Close-out U5. Column: May 2026 (record CBY-BANKS-2026-05)."),
    ("UI-VIS-TH-CBY-2026-06", "June 2026", "يونيو 2026", "Close-out U4. Column: June 2026, the latest month published."),
    ("UI-VIS-ROW-CBY-RATE", "Average market rate for the month, rials per US dollar (December 2025; June 2026)",
     "متوسط سعر الصرف السوقي للشهر، ريال لكل دولار أمريكي (ديسمبر 2025؛ يونيو 2026)", "Close-out U4. Row header."),
    ("UI-VIS-ROW-CBY-M2", "Broad money, M2 (YER billion)", "العرض النقدي الواسع M2 (مليار ريال يمني)", "Close-out U4. Row header."),
    ("UI-VIS-ROW-CBY-CIC-SHARE", "Currency in circulation (% of M2)", "العملة المتداولة (% من M2)", "Close-out U4. Row header."),
    ("UI-VIS-ROW-CBY-FX-SHARE", "Foreign-currency deposits (% of total deposits)",
     "الودائع بالعملات الأجنبية (% من إجمالي الودائع)", "Close-out U4. Row header."),
    ("UI-VIS-ROW-CBY-ASSETS", "Banks' total assets (YER billion)", "إجمالي أصول البنوك (مليار ريال يمني)",
     "Close-out U4/U5. Row header."),
    ("UI-VIS-ROW-CBY-FOREIGN", "Banks' foreign assets (YER billion)", "الأصول الخارجية للبنوك (مليار ريال يمني)",
     "Close-out U4/U5. Row header."),
    ("UI-VIS-ROW-CBY-PRIVATE", "Banks' credit to the private sector (YER billion)",
     "الائتمان الممنوح من البنوك للقطاع الخاص (مليار ريال يمني)", "Close-out U4/U5. Row header."),
    ("UI-VIS-ROW-CBY-GOV", "Banks' loans and advances to government (YER billion)",
     "قروض البنوك وسلفياتها للحكومة (مليار ريال يمني)", "Close-out U4/U5. Row header."),
    ("UI-VIS-CAP-CBY-MFD-55", "CBY-Aden, Monetary and Financial Developments, Issue No. 55",
     "البنك المركزي اليمني – عدن، التطورات النقدية والمالية، العدد 55", "Close-out U4/U5. Table caption."),
    ("UI-VIS-CAP-CBY-AS-PRINTED", "values and shares as the bulletin prints them; rial values are nominal",
     "القيم والحصص كما ترد في النشرة؛ والقيم بالريال اسمية", "Close-out U4. Table caption."),
    ("UI-VIS-CAP-CBY-VALUES-AS-PRINTED", "values as the bulletin prints them; nominal rials",
     "القيم كما ترد في النشرة؛ بالريال الاسمي", "Close-out U5. Table caption (RV-CWR-011)."),
    ("UI-VIS-NOTE-CBY-FIREWALL",
     "Monetary aggregates and bank balance sheets describe the banking system, not people's access to or use of financial "
     "services.",
     "تصف المجاميع النقدية وميزانيات البنوك الجهاز المصرفي، لا وصول الأفراد إلى الخدمات المالية ولا استخدامهم لها.",
     "Close-out U4. Marker row (firewall line)."),
    ("UI-VIS-NOTE-CBY-COVERAGE",
     "The bulletin defines banks as the commercial and Islamic banks operating in the Republic of Yemen but does not say "
     "which banks and branches report to it; the figures are not shown to cover all of Yemen.",
     "تُعرِّف النشرة البنوك بأنها البنوك التجارية والإسلامية العاملة في الجمهورية اليمنية، لكنها لا تذكر أيُّ البنوك والفروع "
     "تقدم بياناتها إليها؛ ولا يثبت أن الأرقام تغطي اليمن كله.", "Close-out U4/U5. Marker row."),
    ("UI-VIS-NOTE-CBY-NOT-ALL-LINES",
     "The three lines do not add up to total assets: reserves, loans and advances to public enterprises and other assets "
     "are not shown.",
     "لا يساوي مجموع البنود الثلاثة إجمالي الأصول: فالاحتياطيات والقروض والسلفيات للمؤسسات العامة والأصول الأخرى غير "
     "معروضة.", "Close-out U5. Marker row (RV-CWR-011)."),
    ("UI-VIS-NOTE-CBY-RATE-SOURCE",
     "The rate is the monthly average market rate that CBY-Aden publishes; it is not the rate in Sana'a and not any "
     "single day's rate.",
     "السعر هو متوسط سعر الصرف السوقي الشهري الذي ينشره البنك المركزي اليمني – عدن؛ وهو ليس سعر الصرف في صنعاء، ولا سعر يوم "
     "واحد بعينه.", "Close-out U4. Marker row and frame note."),
    ("UI-VIS-NOTE-RATE-2025-MOVE",
     "The line joins the published monthly averages and adds no smoothing of its own. The average was 2,733.85 rials per US "
     "dollar in June 2025, 2,212.7 in July and 1,624.5 in August.",
     "يصل الخط بين المتوسطات الشهرية المنشورة ولا يضيف إليها أي تنعيم. وكان المتوسط 2,733.85 ريالًا للدولار الأمريكي في يونيو "
     "2025، و2,212.7 في يوليو، و1,624.5 في أغسطس.", "Close-out U4. Frame note of VIS-YER-MARKET-RATE (the annotated move)."),
    ("UI-VIS-NOTE-POS-RATE-WINDOW",
     "The months shown span the move in the rial's published market rate between June and August 2025; the values are "
     "nominal rials, not adjusted for it, and the chart does not show whether the move changed them.",
     "تشمل الأشهر المعروضة تحرّك سعر الصرف السوقي المنشور للريال بين يونيو وأغسطس 2025؛ والقيم بالريال الاسمي ولا تُعدَّل "
     "لمراعاة هذا التحرك، ولا يُظهر الرسم ما إذا كان التحرك قد غيّرها.", "Close-out U4. Frame note of VIS-POS-VALUE."),
    ("UI-VIS-UNIT-YER-PER-USD", "Rials per US dollar (monthly average)", "ريال لكل دولار أمريكي (متوسط شهري)",
     "Close-out U4. Unit 'YER per USD'."),
]

# ================================================================================================ 11: three new visuals
SNAP = "VIS-CBY-MONETARY-SNAPSHOT"
RATE = "VIS-YER-MARKET-RATE"
RV11 = "RV-CWR-011"
V11 = OrderedDict([
    (SNAP, OrderedDict([
        ("title_en", "Money and bank balance sheets: the end of 2025 and June 2026"),
        ("title_ar", "النقود وميزانيات البنوك: نهاية 2025 ويونيو 2026"),
        ("visual_form", "TABLE_TEXT_FIRST"),
        ("question_en", "What does the latest issue of CBY-Aden's monthly bulletin (June 2026) show for money and bank "
                        "balance sheets?"),
        ("question_ar", "ماذا يُظهر أحدث عدد من النشرة الشهرية للبنك المركزي اليمني – عدن (يونيو 2026) عن النقود وميزانيات "
                        "البنوك؟"),
        ("what_it_shows_en", "Eight indicators from the monthly bulletin of the Central Bank of Yemen – Aden at the end of 2025 "
                             "and in June 2026: the average market rate, broad money, the shares of currency in "
                             "circulation and of foreign-currency deposits, and the banks' total assets, foreign assets, "
                             "credit to the private sector and loans and advances to government, as the bulletin prints "
                             "them."),
        ("what_it_shows_ar", "ثمانية مؤشرات من النشرة الشهرية للبنك المركزي اليمني – عدن في نهاية 2025 وفي يونيو 2026: متوسط "
                             "سعر الصرف السوقي، والعرض النقدي الواسع، وحصتا العملة المتداولة والودائع بالعملات الأجنبية، "
                             "وإجمالي أصول البنوك وأصولها الخارجية والائتمان الممنوح منها للقطاع الخاص وقروضها وسلفياتها "
                             "للحكومة، كما ترد في النشرة."),
        ("decision_value_en", "Gives two dated positions of the monetary and banking system side by side, in the bulletin's "
                              "own units, before any reading of change."),
        ("decision_value_ar", "يضع مركزين مؤرخين للنظام النقدي والمصرفي جنبًا إلى جنب، بوحدات النشرة نفسها، قبل أي قراءة "
                              "للتغير."),
        ("source_period", "End of 2025; June 2026 (Issue No. 55)"),
        ("evidence_strength", "HIGH_ADMIN"),
        ("freshness_profile", "2025 year-end; 2026-06"),
        ("data_inputs", "18_CBY_MONETARY: market rate, M2, currency in circulation share, FX deposit share, bank total "
                        "assets, foreign assets, private credit, loans and advances to government (end of 2025 and June "
                        "2026)"),
        ("unit_or_object", "YER billion; percent; rials per US dollar, each row in its own unit"),
        ("denominator_universe", "The monetary survey and the consolidated balance sheet of commercial and Islamic banks "
                                 "published by the Central Bank of Yemen – Aden (CBY-Aden) in Monetary and Financial "
                                 "Developments; the bulletin defines banks as those operating in the Republic of Yemen but "
                                 "does not say which banks and branches report to it."),
        ("period", "End of 2025; June 2026"),
        ("encoding_contract", "Table: one row per indicator in its own unit; two dated columns; values and shares as "
                              "printed; no change column and no growth rate."),
        ("prohibited_inference_en", "Monetary aggregates and bank balance sheets describe the banking system, not people's "
                                    "access to or use of financial services. Money and balance-sheet values are nominal "
                                    "rials, partly valued at market exchange rates, so a change between the two columns "
                                    "cannot be read as real growth; the figures are not shown to cover all of Yemen."),
        ("prohibited_inference_ar", "تصف المجاميع النقدية وميزانيات البنوك الجهاز المصرفي، لا وصول الأفراد إلى الخدمات المالية "
                                    "ولا استخدامهم لها. وقيم النقود والميزانيات بالريال الاسمي، ويُقيَّم جزء منها بأسعار الصرف "
                                    "السوقية، فلا يمكن قراءة التغير بين العمودين على أنه نمو حقيقي؛ ولا يثبت أن الأرقام تغطي اليمن "
                                    "كله."),
        ("accessible_summary_en", "From the end of 2025 to June 2026, as the bulletin of the Central Bank of Yemen – Aden "
                                  "prints them: the average market rate went from 1,624.45 to 1,560.95 rials per US dollar "
                                  "(December 2025 and June 2026 monthly averages); broad money from 11,429.3 to 11,925.0 "
                                  "billion rials; currency in circulation from 28.6% to 28.4% of broad money; "
                                  "foreign-currency deposits from 71.0% to 68.0% of total deposits; the banks' total assets "
                                  "from 12,341.8 to 13,761.2 billion rials, their foreign assets from 4,116.5 to 4,650.0 "
                                  "billion, their credit to the private sector from 1,392.3 to 1,362.9 billion and their "
                                  "loans and advances to government from 1,928.8 to 1,966.8 billion. Money and balance-sheet "
                                  "values are in nominal rials; all of these describe the banking system, not people's "
                                  "access or use; the bulletin does not say which banks and branches report to it."),
        ("accessible_summary_ar", "من نهاية 2025 إلى يونيو 2026، كما ترد في نشرة البنك المركزي اليمني – عدن: انتقل متوسط سعر "
                                  "الصرف السوقي من 1,624.45 إلى 1,560.95 ريالًا للدولار الأمريكي (المتوسطان الشهريان لديسمبر "
                                  "2025 ويونيو 2026)؛ والعرض النقدي الواسع من 11,429.3 إلى 11,925.0 مليار ريال؛ والعملة "
                                  "المتداولة من 28.6% إلى 28.4% من العرض النقدي الواسع؛ والودائع بالعملات الأجنبية من 71.0% "
                                  "إلى 68.0% من إجمالي الودائع؛ وإجمالي أصول البنوك من 12,341.8 إلى 13,761.2 مليار ريال، "
                                  "وأصولها الخارجية من 4,116.5 إلى 4,650.0 مليار، والائتمان الممنوح منها للقطاع الخاص من "
                                  "1,392.3 إلى 1,362.9 مليار، وقروضها وسلفياتها للحكومة من 1,928.8 إلى 1,966.8 مليار. وقيم "
                                  "النقود والميزانيات بالريال الاسمي، وكلها تصف الجهاز المصرفي لا وصول الأفراد أو استخدامهم؛ "
                                  "ولا تذكر النشرة أيُّ البنوك والفروع تقدم بياناتها إليها."),
        ("public_routes", '["/finance"]'),
        ("period_ar", "نهاية 2025؛ يونيو 2026"),
        ("universe_ar", "المسح النقدي والميزانية المجمعة للبنوك التجارية والإسلامية كما ينشرهما البنك المركزي اليمني – عدن في "
                        "نشرته الشهرية «التطورات النقدية والمالية»؛ وتُعرِّف النشرة البنوك بأنها العاملة في الجمهورية "
                        "اليمنية، لكنها لا تذكر أيُّ البنوك والفروع تقدم بياناتها إليها."),
    ])),
    (RATE, OrderedDict([
        ("title_en", "The rial's average market rate published by CBY-Aden, monthly"),
        ("title_ar", "متوسط سعر الصرف السوقي للريال كما ينشره البنك المركزي اليمني – عدن، شهريًا"),
        ("visual_form", "LINE_MONTHLY_ANNOTATED"),
        ("question_en", "How has the average market rate that CBY-Aden publishes moved since 2017?"),
        ("question_ar", "كيف تحرك متوسط سعر الصرف السوقي الذي ينشره البنك المركزي اليمني – عدن منذ 2017؟"),
        ("what_it_shows_en", "The monthly average market rate of the rial against the US dollar that the Central Bank of "
                             "Yemen – Aden publishes, from January 2017 to June 2026, drawn as published, with the June to "
                             "August 2025 move annotated rather than smoothed."),
        ("what_it_shows_ar", "متوسط سعر الصرف السوقي الشهري للريال مقابل الدولار الأمريكي الذي ينشره البنك المركزي اليمني – عدن، "
                             "من يناير 2017 إلى يونيو 2026، مرسومًا كما نُشر، مع تعليق توضيحي على التحرك بين يونيو وأغسطس "
                             "2025 بدل تنعيمه."),
        ("decision_value_en", "Puts the published monthly average market rate beside balance-sheet values in rials, so that a "
                              "move in rial values is checked against the rate before it is read as economic change; the "
                              "bulletin does not say which rate, or which day's rate, values the banks' foreign-currency "
                              "items."),
        ("decision_value_ar", "يضع متوسط سعر الصرف السوقي الشهري المنشور بجانب قيم الميزانيات بالريال، حتى يُفحص تحرك القيم "
                              "بالريال في ضوء السعر قبل أن يُقرأ على أنه تغير اقتصادي؛ ولا تبيّن النشرة بأي سعر، ولا بسعر أي "
                              "يوم، تُقيَّم البنود المقوّمة بالعملات الأجنبية لدى البنوك."),
        ("source_period", "2017-01→2026-06 monthly"),
        ("evidence_strength", "HIGH_ADMIN"),
        ("freshness_profile", "2017-01→2026-06"),
        ("data_inputs", "18_CBY_MONETARY YER_USD_MARKET_RATE (Table 6)"),
        ("unit_or_object", "rials per US dollar, monthly average"),
        ("denominator_universe", "The monthly average market exchange rate of the rial against the US dollar published by "
                                 "the Central Bank of Yemen – Aden (CBY-Aden) in Monetary and Financial Developments "
                                 "(Table 6), which the English edition of the bulletin calls the parallel-market rate; not "
                                 "the rate in Sana'a and not any single day's rate."),
        ("period", "January 2017 to June 2026"),
        ("encoding_contract", "Monthly line, one point per published month; the June to August 2025 move is annotated in "
                              "the frame; no smoothing and no trend line."),
        ("prohibited_inference_en", "The line shows the monthly average market rate that CBY-Aden publishes. It is not the "
                                    "rate in Sana'a or any single day's rate; it does not explain why the rate moved, and it "
                                    "does not show that the rate was held or administered."),
        ("prohibited_inference_ar", "يعرض الخط متوسط سعر الصرف السوقي الشهري الذي ينشره البنك المركزي اليمني – عدن. وهو ليس "
                                    "سعر الصرف في صنعاء ولا سعر يوم واحد بعينه؛ ولا يفسر سبب تحرك السعر، ولا يُظهر أن السعر "
                                    "ثُبِّت أو حُدِّد إداريًا."),
        ("accessible_summary_en", "The average market rate of the rial published by the Central Bank of Yemen – Aden went from "
                                  "315.64 rials per US dollar in January 2017 to 2,733.85 in June 2025, then to 2,212.7 in "
                                  "July and 1,624.5 in August 2025, and stood at 1,560.95 in June 2026. The line joins the "
                                  "published monthly averages and adds no smoothing of its own. It is not the rate in Sana'a "
                                  "or any single day's rate, and it does not explain why the rate moved."),
        ("accessible_summary_ar", "انتقل متوسط سعر الصرف السوقي للريال الذي ينشره البنك المركزي اليمني – عدن من 315.64 ريالًا "
                                  "للدولار الأمريكي في يناير 2017 إلى 2,733.85 في يونيو 2025، ثم إلى 2,212.7 في يوليو و1,624.5 "
                                  "في أغسطس 2025، وبلغ 1,560.95 في يونيو 2026. ويصل الخط بين المتوسطات الشهرية المنشورة ولا "
                                  "يضيف إليها أي تنعيم. وهو ليس سعر الصرف في صنعاء ولا سعر يوم واحد بعينه، ولا يفسر سبب تحرك "
                                  "السعر."),
        ("public_routes", '["/finance"]'),
        ("period_ar", "من يناير 2017 إلى يونيو 2026"),
        ("universe_ar", "متوسط سعر الصرف السوقي الشهري للريال مقابل الدولار الأمريكي كما ينشره البنك المركزي اليمني – عدن في "
                        "نشرته الشهرية «التطورات النقدية والمالية» (الجدول 6)، وتسميه النسخة الإنجليزية من النشرة سعر "
                        "السوق الموازية؛ وهو ليس سعر الصرف في صنعاء ولا سعر يوم واحد بعينه."),
    ])),
    (RV11, OrderedDict([
        ("title_en", "Where the banks' assets sit: three dated positions"),
        ("title_ar", "أين تقع أصول البنوك: ثلاثة مراكز مؤرخة"),
        ("visual_form", "TABLE_TEXT_FIRST"),
        ("question_en", "How much of the banks' total assets sits in foreign assets, loans and advances to government and "
                        "credit to the private sector?"),
        ("question_ar", "كم من إجمالي أصول البنوك يقع في الأصول الخارجية، وفي القروض والسلفيات للحكومة، وفي الائتمان الممنوح "
                        "للقطاع الخاص؟"),
        ("what_it_shows_en", "The consolidated balance sheet of commercial and Islamic banks at the end of 2025, in May 2026 "
                             "and in June 2026: total assets, foreign assets, loans and advances to government and credit "
                             "to the private sector, as the bulletin of the Central Bank of Yemen – Aden prints them."),
        ("what_it_shows_ar", "الميزانية المجمعة للبنوك التجارية والإسلامية في نهاية 2025 وفي مايو 2026 ويونيو 2026: إجمالي "
                             "الأصول والأصول الخارجية والقروض والسلفيات للحكومة والائتمان الممنوح للقطاع الخاص، كما ترد في "
                             "نشرة البنك المركزي اليمني – عدن."),
        ("decision_value_en", "Keeps the composition behind the Reading's hypothesis visible in the bulletin's own figures, "
                              "so that the hypothesis is read against them and not against a share alone."),
        ("decision_value_ar", "يُبقي التوزيع الذي تستند إليه فرضية القراءة ظاهرًا بأرقام النشرة نفسها، حتى تُقرأ الفرضية في "
                              "ضوئها لا في ضوء حصة منفردة."),
        ("source_period", "End of 2025; May 2026; June 2026"),
        ("evidence_strength", "HIGH_ADMIN"),
        ("freshness_profile", "2025 year-end; 2026-05; 2026-06"),
        ("data_inputs", "18_CBY_MONETARY T4: the CBY-BANKS-2026-05 rows and the June 2026 rows (Issue No. 55)"),
        ("unit_or_object", "YER billion"),
        ("denominator_universe", "The consolidated balance sheet of commercial and Islamic banks published by the Central "
                                 "Bank of Yemen – Aden (CBY-Aden); the bulletin defines banks as those operating in the "
                                 "Republic of Yemen but does not say which banks and branches report to it."),
        ("period", "End of 2025; May 2026; June 2026"),
        ("encoding_contract", "Table: one row per balance-sheet line, three dated columns, values as printed; no share "
                              "column and no growth rate; a note says the lines shown do not add up to total assets."),
        ("prohibited_inference_en", "The positions do not show why banks hold these assets, a credit allocation decision, or "
                                    "people's access to credit; values are nominal rials, partly valued at market exchange "
                                    "rates."),
        ("prohibited_inference_ar", "لا تُظهر هذه المراكز سبب احتفاظ البنوك بهذه الأصول، ولا قرارًا بتخصيص الائتمان، ولا وصول "
                                    "الأفراد إلى الائتمان؛ والقيم بالريال الاسمي، ويُقيَّم جزء منها بأسعار الصرف السوقية."),
        ("accessible_summary_en", "As the bulletin of the Central Bank of Yemen – Aden prints them, the banks' total assets were "
                                  "12,341.8 billion rials at the end of 2025, 13,362.1 billion in May 2026 and 13,761.2 "
                                  "billion in June 2026; foreign assets 4,116.5, 4,448.0 and 4,650.0 billion; loans and "
                                  "advances to government 1,928.8, 2,145.0 and 1,966.8 billion; and credit to the private "
                                  "sector 1,392.3, 1,350.4 and 1,362.9 billion. The three lines do not add up to total "
                                  "assets, and the positions do not show why banks hold these assets or people's access to "
                                  "credit."),
        ("accessible_summary_ar", "كما ترد في نشرة البنك المركزي اليمني – عدن، بلغ إجمالي أصول البنوك 12,341.8 مليار ريال في "
                                  "نهاية 2025، و13,362.1 مليار في مايو 2026، و13,761.2 مليار في يونيو 2026؛ والأصول الخارجية "
                                  "4,116.5 و4,448.0 و4,650.0 مليار؛ والقروض والسلفيات للحكومة 1,928.8 و2,145.0 و1,966.8 "
                                  "مليار؛ والائتمان الممنوح للقطاع الخاص 1,392.3 و1,350.4 و1,362.9 مليار. ولا يساوي مجموع "
                                  "البنود الثلاثة إجمالي الأصول، ولا تُظهر هذه المراكز سبب احتفاظ البنوك بهذه الأصول ولا وصول "
                                  "الأفراد إلى الائتمان."),
        ("public_routes", '["/readings/where-bank-balance-sheets-sit"]'),
        ("period_ar", "نهاية 2025؛ مايو 2026؛ يونيو 2026"),
        ("universe_ar", "الميزانية المجمعة للبنوك التجارية والإسلامية كما ينشرها البنك المركزي اليمني – عدن؛ وتُعرِّف النشرة "
                        "البنوك بأنها العاملة في الجمهورية اليمنية، لكنها لا تذكر أيُّ البنوك والفروع تقدم بياناتها إليها."),
    ])),
])

# ================================================================================================ U4: CLM-033 and CWR-002, the 2025 episode
B55 = "Issue No. 55 (June 2026)"
EP2025 = ("The same mechanism can run the other way. Between the end of 2024 and the end of 2025 the banks' total assets fell "
          "from 15,329.7 to 12,341.8 billion rials and their foreign-currency deposits from 7,999.9 to 5,792.8 billion, while "
          "the average market rate that CBY-Aden publishes went from 2,059.2 to 1,624.45 rials per US dollar (December "
          "averages). Part of that fall is consistent with revaluing foreign-currency positions at a stronger rial. But the "
          "bulletin also states that its monetary and banking data were amended and updated in line with the IMF's Monetary "
          "and Financial Statistics Manual (2016) from December 2025, and it publishes no line-by-line bridge, so valuation, "
          "the change of method and other movements cannot be separated.")
EP2025_AR = ("ويمكن أن تعمل الآلية نفسها في الاتجاه المعاكس. فبين نهاية 2024 ونهاية 2025 انخفض إجمالي أصول البنوك من 15,329.7 إلى "
             "12,341.8 مليار ريال، وودائعها بالعملات الأجنبية من 7,999.9 إلى 5,792.8 مليار، بينما انتقل متوسط سعر الصرف السوقي "
             "الذي ينشره البنك المركزي اليمني – عدن من 2,059.2 إلى 1,624.45 ريالًا للدولار الأمريكي (متوسطا شهر ديسمبر). "
             "ويتسق جزء من هذا الانخفاض مع إعادة تقييم المراكز بالعملات الأجنبية بسعر ريال أقوى. غير أن النشرة تذكر أيضًا أن "
             "بياناتها النقدية والمصرفية عُدِّلت وحُدِّثت وفق دليل الإحصاءات النقدية والمالية الصادر عن صندوق النقد الدولي (2016) "
             "ابتداءً من ديسمبر 2025، ولا تنشر جسرًا يفصّل ذلك بندًا ببند، فلا يمكن الفصل بين أثر التقييم وأثر تغيير المنهجية "
             "والتحركات الأخرى.")
CLM033_LIM = ("changes in individual lines can be attributed to valuation only as far as the documented valuation note supports.",
              " " + EP2025,
              "ويظل إسناد التغيرات التفصيلية إلى ملاحظة التقييم ضمن الحدود التي يثبتها المصدر.",
              " " + EP2025_AR)
CLM033_CUR = ("It should not be read as describing later positions.",
              "Its note on 2025 compares the end of 2024 and the end of 2025 as printed in " + B55 + " of the monthly "
              "bulletin; it should not be read as describing later positions.",
              "ولا يُقرأ على أنه يصف مراكز لاحقة.",
              "وتقارن ملاحظته عن 2025 بين نهاية 2024 ونهاية 2025 بالقيم الواردة في العدد 55 (يونيو 2026) من النشرة الشهرية؛ ولا يُقرأ "
              "على أنه يصف مراكز لاحقة.")
CLM033_PERIOD = ("2022 positions as published in the 2022 annual report and as restated from the 2023 annual report onward",
                 "2022 positions as published in the 2022 annual report and as restated from the 2023 annual report "
                 "onward; the end of 2024 and of 2025 (Issue No. 55, June 2026)",
                 "مراكز عام 2022 كما نُشرت في التقرير السنوي 2022 وكما أُعيد عرضها ابتداءً من التقرير السنوي 2023",
                 "مراكز عام 2022 كما نُشرت في التقرير السنوي 2022 وكما أُعيد عرضها ابتداءً من التقرير السنوي 2023؛ ونهاية 2024 "
                 "ونهاية 2025 (العدد 55، يونيو 2026)")
L_T1 = "CBY-Aden, Monetary and Financial Developments, " + B55 + ", Table 1 'Monetary Survey', printed p.10 (PDF p.11), " + I55
L_T4 = ("CBY-Aden, Monetary and Financial Developments, " + B55 + ", Table 4 (banks' assets), printed p.15 (PDF p.16), "
        + I55)
L_T5 = ("CBY-Aden, Monetary and Financial Developments, " + B55 + ", Table 5 (banks' liabilities), printed p.16 (PDF p.17), "
        + I55)
L_T6 = ("CBY-Aden, Monetary and Financial Developments, " + B55 + ", Table 6 'Average Market Exchange Rates', printed "
        "p.17 (PDF p.18), " + I55)


def vs(t, loc, k="v", src=SRC_CBY):
    return OrderedDict([("t", t), ("k", k), ("s", "READ"), ("src", src), ("loc", loc + "; read 10 October 2026")])


CLM033_VS = [vs("15,329.7", L_T4 + ", Total Assets, 2024"), vs("12,341.8", L_T4 + ", Total Assets, 2025"),
             vs("7,999.9", L_T5 + ", Deposits – Foreign Currency, 2024"), vs("5,792.8", L_T5 + ", Deposits – Foreign Currency, 2025"),
             vs("2,059.2", L_T6 + ", December 2024"), vs("1,624.45", L_T6 + ", December 2025"),
             # the dates the rial line, its frame note and the /finance/ table print (E2-DATES)
             vs("January 2017", L_T6 + ", January 2017 = 315.64", "d"), vs("June 2025", L_T6 + ", June 2025 = 2,733.85", "d"),
             vs("August 2025", L_T6 + ", August 2025 = 1,624.5 (Issue No. 54 and No. 55)", "d"),
             vs("December 2025", L_T6 + ", December 2025 = 1,624.45; and the Disclaimer, printed p.23 (PDF p.24): 'Beginning "
                "in Dec 2025, monetary and banking data were amended and updated by the Monetary and Financial Statistics "
                "Manual (2016) (IMF)'", "d"),
             vs("June 2026", L_T6 + ", June 2026 = 1,560.95", "d"),
             OrderedDict([("t", "55"), ("k", "v"), ("s", "TRIVIAL")])]   # the issue number (as CBY-BANKS-2026-05 states 54)
CWR002 = "/readings/banking-jump-measurement-basis/"
CWR002_S3 = ("the bulletin does not split any line between valuation and other effects.",
             "the bulletin does not split any line between valuation and other effects.\n" + EP2025.replace("'", "’"),
             "ولا تفصل النشرة أي بند بين أثر التقييم والآثار الأخرى.",
             "ولا تفصل النشرة أي بند بين أثر التقييم والآثار الأخرى.\n" + EP2025_AR)

# ================================================================================================ the contract
MONTHS = [f"{y}-{m:02d}" for y in range(2017, 2027) for m in range(1, 13) if (y, m) <= (2026, 6)]


def snapshot_table(ids):
    """ids: indicator -> (end-2025 row id, June 2026 row id), in row order, with the governed precision of each."""
    rows, objs, must = [], [], OrderedDict()
    for ind, (ui_row, dp, end_id, jun_id, end_v, jun_v) in ids.items():
        for rid, val in ((end_id, end_v), (jun_id, jun_v)):
            objs.append(rid)
            must[rid] = OrderedDict([("value", val)])
        rows.append(OrderedDict([("head", ui_row), ("cells", [OrderedDict([("ref", f"cby.{end_id}.value"), ("dp", dp)]),
                                                             OrderedDict([("ref", f"cby.{jun_id}.value"), ("dp", dp)])])]))
    return rows, objs, must


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    f4, f5 = F + ":U4", F + ":U5"

    # ---------------------------------------------------------------- 18: the June 2026 values (Issue No. 55)
    t18 = Table(s, "18_CBY_MONETARY")
    head = t18.head
    by = {}
    for rid in t18.rows:
        per = t18.get(rid, "period")
        per = int(per) if isinstance(per, float) and per.is_integer() else per
        by.setdefault((t18.get(rid, "indicator_id"), str(per)), rid)
    if any((ind, "2026-06") in by for ind in JUNE):
        raise TxError(f"{f4}: 18 already holds June 2026 rows")
    for ind, (end_v, may_v) in I55_EARLIER.items():   # Issue No. 55 prints the same earlier values the tables show
        end_rid = by[(ind, "2025-12" if ind == "YER_USD_MARKET_RATE" else "2025")]
        for rid, want in ((end_rid, end_v), (by[(ind, "2026-05")], may_v)):
            if float(t18.get(rid, "value")) != want:
                raise TxError(f"{f4}: {rid} ({ind}) holds {t18.get(rid, 'value')!r}; Issue No. 55 prints {want}")
    last_row = max(t18.rows.values())
    last_n = max(int(str(k)[len("OBS-CBY-"):]) for k in t18.rows)
    new_rows, jun_ids = [], OrderedDict()
    for i, (ind, (val, loc)) in enumerate(JUNE.items(), start=1):
        tmpl = by.get((ind, "2026-05"))
        if tmpl is None:
            raise TxError(f"{f4}: no May 2026 row of {ind} to take the series fields from")
        rid = f"OBS-CBY-{last_n + i:05d}"
        row = OrderedDict((f, t18.get(tmpl, f)) for f in head if f)
        row.update([("observation_id", rid), ("period", "2026-06"), ("value", val), ("original_url", I55),
                    ("notes", JUNE_NOTE.format(loc=loc))])
        new_rows.append(row)
        jun_ids[ind] = rid
    s.ed.insert_rows("18_CBY_MONETARY", last_row + 1,
                     [{head.index(k) + 1: v for k, v in r.items() if v not in (None, "")} for r in new_rows])
    for j, r in enumerate(new_rows):
        for k, v in r.items():
            if v not in (None, ""):
                s.ledger.append(OrderedDict([("finding", f4), ("sheet", "18_CBY_MONETARY"), ("row", last_row + 1 + j),
                                             ("col", head.index(k) + 1), ("field", f"{r['observation_id']}.{k}"),
                                             ("old", None), ("new", v)]))
    t15 = Table(s, "15_SOURCE_LIBRARY")
    if t15.get(SRC_CBY, "primary_url") != I54:
        raise TxError(f"{f4}: {SRC_CBY} is not the Issue No. 54 record expected")
    for field, new in SRC_SET.items():
        t15.set(f4, SRC_CBY, field, new, t15.get(SRC_CBY, field))
    note = t15.get(SRC_CBY, "non_public_locator_note")
    if not str(note or "").startswith(NOTE_OLD_START):
        raise TxError(f"{f4}: {SRC_CBY}'s locator note is not the one expected")
    t15.set(f4, SRC_CBY, "non_public_locator_note", SRC_NOTE, note)
    cur = t15.get(SRC_CBY, "additional_urls")
    urls = json.loads(cur) if cur else []
    t15.set(f4, SRC_CBY, "additional_urls", json.dumps([I54, I55_AR] + [u for u in urls if u not in (I54, I55_AR)]), cur)
    rc = t15.get(SRC_CBY, "row_count")
    t15.set(f4, SRC_CBY, "row_count", str(int(float(rc)) + len(new_rows)) if isinstance(rc, str) else int(rc) + len(new_rows), rc)

    # ---------------------------------------------------------------- 04 and 11
    insert_ui_rows(s, F, UI)
    t11 = Table(s, "11_VISUAL_LIBRARY")
    h11 = t11.head
    for vid in V11:
        if vid in t11.rows:
            raise TxError(f"{F}: 11 already holds {vid}")
    last11 = max(t11.rows.values())
    rows11 = [OrderedDict([("visual_id", vid)] + list(f.items())) for vid, f in V11.items()]
    s.ed.insert_rows("11_VISUAL_LIBRARY", last11 + 1, [{h11.index(k) + 1: v for k, v in r.items()} for r in rows11])
    for j, r in enumerate(rows11):
        for k, v in r.items():
            s.ledger.append(OrderedDict([("finding", f5 if r["visual_id"] == RV11 else f4), ("sheet", "11_VISUAL_LIBRARY"),
                                         ("row", last11 + 1 + j), ("col", h11.index(k) + 1),
                                         ("field", f"{r['visual_id']}.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- CLM-033 and CWR-002: the 2025 episode
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for field, (old, new) in (("limitations_en", CLM033_LIM[:2]), ("limitations_ar", CLM033_LIM[2:]),
                              ("currentness_en", CLM033_CUR[:2]), ("currentness_ar", CLM033_CUR[2:])):
        cur = t06.get("CLM-033", field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{f4}: CLM-033.{field} does not hold {old[:50]!r} once")
        t06.set(f4, "CLM-033", field, cur.replace(old, old + new if new.startswith(" ") else new), cur)
    t06.set(f4, "CLM-033", "period_en", CLM033_PERIOD[1], CLM033_PERIOD[0])
    t06.set(f4, "CLM-033", "period_ar", CLM033_PERIOD[3], CLM033_PERIOD[2])
    cur = t06.get("CLM-033", "value_states")
    states = json.loads(cur) if cur else []
    have = {(e.get("t"), e.get("k")) for e in states}
    states += [e for e in CLM033_VS if (e["t"], e["k"]) not in have]
    t06.set(f4, "CLM-033", "value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")), cur)
    s.replace_section(f4, CWR002, 3, "en", "body", CWR002_S3[0], CWR002_S3[1])
    s.replace_section(f4, CWR002, 3, "ar", "body", CWR002_S3[2], CWR002_S3[3])

    # ---------------------------------------------------------------- 08: CWR-011 binds its visual
    # Its domain surfaces stay /firms/: rule F2 (reading_relations) lets an answer page carry at most two Readings, and
    # /finance/ carries CWR-002 and CWR-006. The positions the visual prints reach /finance/ in VIS-CBY-MONETARY-SNAPSHOT.
    t08 = Table(s, "08_READINGS", 4)
    t08.set(f5, "CWR-011", "visual_bindings", json.dumps([RV11]), "[]")

    # ---------------------------------------------------------------- the contract
    end = {ind: by[(ind, "2025")] for ind in JUNE if ind != "YER_USD_MARKET_RATE"}
    end["YER_USD_MARKET_RATE"] = by[("YER_USD_MARKET_RATE", "2025-12")]
    val = lambda rid: float(t18.get(rid, "value"))  # noqa: E731
    jv = {ind: float(v) for ind, (v, _) in JUNE.items()}
    spec = OrderedDict([
        ("YER_USD_MARKET_RATE", ("UI-VIS-ROW-CBY-RATE", 2)), ("M2_BN_YER", ("UI-VIS-ROW-CBY-M2", 1)),
        ("CURRENCY_CIRCULATION_SHARE_M2_PCT", ("UI-VIS-ROW-CBY-CIC-SHARE", 1)),
        ("FX_DEPOSITS_SHARE_TOTAL_DEPOSITS_PCT", ("UI-VIS-ROW-CBY-FX-SHARE", 1)),
        ("BANK_TOTAL_ASSETS_BN_YER", ("UI-VIS-ROW-CBY-ASSETS", 1)), ("BANK_FOREIGN_ASSETS_BN_YER", ("UI-VIS-ROW-CBY-FOREIGN", 1)),
        ("BANK_CREDIT_PRIVATE_SECTOR_BN_YER", ("UI-VIS-ROW-CBY-PRIVATE", 1)), ("BANK_CLAIMS_GOV_BN_YER", ("UI-VIS-ROW-CBY-GOV", 1))])
    rows, ids, must = snapshot_table(OrderedDict(
        (ind, (ui, dp, end[ind], jun_ids[ind], val(end[ind]), jv[ind])) for ind, (ui, dp) in spec.items()))
    snap_table = OrderedDict([
        ("form", "One row per indicator in its own unit; two dated columns (the end of 2025 and June 2026); values and "
                 "shares as the bulletin prints them; governed notes close the table. No change column, no growth rate."),
        ("objects", [OrderedDict([("id", "cby"), ("rows", OrderedDict([("file", "data/cby_monetary.json"),
                                                                       ("header_key", "observation_id"), ("ids", ids)])),
                                  ("fields", OrderedDict([("value", "value"), ("period", "period"), ("source", "source_id")])),
                                  ("must_equal", must)])]),
        ("head", ["UI-VIS-TH-CBY-ITEM", "UI-VIS-TH-CBY-END-2025", "UI-VIS-TH-CBY-2026-06"]),
        ("caption", ["UI-VIS-CAP-CBY-MFD-55", "UI-VIS-CAP-CBY-AS-PRINTED"]),
        ("rows", rows + [OrderedDict([("marker", m)]) for m in
                         ("UI-VIS-NOTE-CBY-RATE-SOURCE", "UI-VIS-NOTE-CBY-FIREWALL", "UI-VIS-NOTE-CBY-COVERAGE")])])
    may = {ind: by[(ind, "2026-05")] for ind in ("BANK_TOTAL_ASSETS_BN_YER", "BANK_FOREIGN_ASSETS_BN_YER",
                                                 "BANK_CLAIMS_GOV_BN_YER", "BANK_CREDIT_PRIVATE_SECTOR_BN_YER")}
    rv_rows, rv_ids, rv_must = [], [], OrderedDict()
    for ind in may:
        ui, dp = spec[ind]
        cells = []
        for rid, v in ((end[ind], val(end[ind])), (may[ind], val(may[ind])), (jun_ids[ind], jv[ind])):
            rv_ids.append(rid)
            rv_must[rid] = OrderedDict([("value", v)])
            cells.append(OrderedDict([("ref", f"cby.{rid}.value"), ("dp", dp)]))
        rv_rows.append(OrderedDict([("head", ui), ("cells", cells)]))
    rv_table = OrderedDict([
        ("form", "One row per balance-sheet line; three dated columns (the end of 2025, May 2026, June 2026); values as the "
                 "bulletin prints them; governed notes close the table. No share column, no growth rate."),
        ("objects", [OrderedDict([("id", "cby"), ("rows", OrderedDict([("file", "data/cby_monetary.json"),
                                                                       ("header_key", "observation_id"), ("ids", rv_ids)])),
                                  ("fields", OrderedDict([("value", "value"), ("period", "period"), ("source", "source_id")])),
                                  ("must_equal", rv_must)])]),
        ("head", ["UI-VIS-TH-CBY-ITEM", "UI-VIS-TH-CBY-END-2025", "UI-VIS-TH-CBY-2026-05", "UI-VIS-TH-CBY-2026-06"]),
        ("caption", ["UI-VIS-CAP-CBY-MFD-55", "UI-VIS-CAP-CBY-VALUES-AS-PRINTED"]),
        ("rows", rv_rows + [OrderedDict([("marker", "UI-VIS-NOTE-CBY-NOT-ALL-LINES")]),
                            OrderedDict([("marker", "UI-VIS-NOTE-CBY-FIREWALL")]),
                            OrderedDict([("marker", "UI-VIS-NOTE-CBY-COVERAGE")])])])
    rate_rows = [rid for (ind, per), rid in by.items() if ind == "YER_USD_MARKET_RATE"]
    first = by[("YER_USD_MARKET_RATE", "2017-01")]
    rate_contract = OrderedDict([
        ("form", "Monthly line of the published average market rate, January 2017 to June 2026; one point per month; no "
                 "smoothing and no trend line."),
        ("series", [OrderedDict([
            ("id", "rate"),
            ("rows", OrderedDict([("file", "data/cby_monetary.json"), ("header_key", "observation_id"),
                                  ("where", OrderedDict([("indicator_id", "^YER_USD_MARKET_RATE$")]))])),
            ("fields", OrderedDict([("x", "period"), ("y", "value"), ("unit", "unit"), ("flag", "comparability_status"),
                                    ("source", "source_id")])),
            ("state", "REPORTED"),
            ("expected_x", MONTHS),
            ("must_equal", OrderedDict([(first, 315.64), (by[("YER_USD_MARKET_RATE", "2025-06")], 2733.85),
                                        (by[("YER_USD_MARKET_RATE", "2025-08")], 1624.5),
                                        (jun_ids["YER_USD_MARKET_RATE"], 1560.95)])),
            ("label_fields", OrderedDict([("unit", "unit")]))])]),
        ("ordering", "Chronological."),
        ("transformation", "None; the monthly averages as published, in rials per US dollar."),
        ("missing", "None: every month from January 2017 to June 2026 is published."),
        ("breaks", "None governed. The June to August 2025 move is a change in the published rate, annotated in the frame, "
                   "not a break in the series."),
        ("annotation", "Frame notes UI-VIS-NOTE-CBY-RATE-SOURCE (what the rate is and is not) and UI-VIS-NOTE-RATE-2025-MOVE "
                       "(the June to August 2025 move with its two published values); no point is marked as a cause."),
        ("credit", OrderedDict([("source_ids", [SRC_CBY])])),
        ("mobile", "Single panel; the line keeps its full span."),
        ("rtl", "Time axis left to right."),
        ("fallback", "Table: month, average market rate (rials per US dollar)."),
        ("frame_labels", ["UI-VIS-NOTE-CBY-RATE-SOURCE", "UI-VIS-NOTE-RATE-2025-MOVE"])])
    if len(rate_rows) != len(MONTHS) - 1:
        raise TxError(f"{f4}: {len(rate_rows)} monthly rates before June 2026, expected {len(MONTHS) - 1}")
    c = json.load(open(CONTRACT, encoding="utf-8"), object_pairs_hook=OrderedDict)
    if any(v["visual_id"] in V11 for v in c["visuals"]):
        raise TxError(f"{F}: the contract already holds a close-out CBY visual")
    c["visuals"].append(OrderedDict([("visual_id", SNAP), ("tier", "TABLE_TEXT_FIRST"),
                                     ("rationale", "Eight indicators of the monetary survey and the banks' consolidated "
                                                   "balance sheet at two dated positions, as the bulletin prints them: a "
                                                   "table, because the rows are in different units and the two columns are "
                                                   "two vintages, not a series."),
                                     ("promotion_requires", "A drawn comparison would need each indicator as a governed "
                                                            "monthly series in one vintage; the table keeps two dated "
                                                            "columns."),
                                     ("table", snap_table)]))
    c["visuals"].append(OrderedDict([("visual_id", RATE), ("tier", "CORE_ANALYTICAL"),
                                     ("rationale", "The published monthly average market rate, beside the rial balance "
                                                   "sheets: the monthly line primitive of the POS panels, the 2025 move "
                                                   "annotated, not smoothed."),
                                     ("contract", rate_contract)]))
    c["visuals"].append(OrderedDict([("visual_id", RV11), ("tier", "TABLE_TEXT_FIRST"),
                                     ("rationale", "The bound CBY-BANKS positions behind Reading CWR-011, at three dated "
                                                   "positions, as the bulletin prints them; levels only, the record "
                                                   "carries the one share it computes."),
                                     ("promotion_requires", "A drawn composition would need governed shares of total "
                                                            "assets for each date (computed by CauseWay and held as "
                                                            "rows)."),
                                     ("table", rv_table)]))
    pos = next(v for v in c["visuals"] if v["visual_id"] == "VIS-POS-VALUE")["contract"]
    if "UI-VIS-NOTE-POS-RATE-WINDOW" in (pos.get("frame_labels") or []):
        raise TxError(f"{f4}: VIS-POS-VALUE already carries the rate-window note")
    pos["frame_labels"] = list(pos.get("frame_labels") or []) + ["UI-VIS-NOTE-POS-RATE-WINDOW"]
    pos["transformation"] = ("None; nominal YER million. No price or exchange-rate adjustment, and the line carries no "
                             "exchange-rate mark (it would invite a causal reading); the frame note "
                             "UI-VIS-NOTE-POS-RATE-WINDOW says the window spans the 2025 move in the published rate.")
    pos["annotation"] = pos["annotation"] + " Frame note UI-VIS-NOTE-POS-RATE-WINDOW."
    ns = c["display_labels"]["namespaces"]["unit"]
    if ns.get("YER per USD") not in (None, "UI-VIS-UNIT-YER-PER-USD"):
        raise TxError(f"{f4}: the unit namespace maps 'YER per USD' elsewhere")
    ns["YER per USD"] = "UI-VIS-UNIT-YER-PER-USD"
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "U4: June 2026 (Issue No. 55) values for ten CBY series; SRC-CBY-001 names Issue No. 55; a dated table "
                    "of eight indicators and the monthly market-rate line on /finance/; the 2025 episode in CLM-033 and "
                    "CWR-002; VIS-POS-VALUE frame note. U5: RV-CWR-011 bound to CWR-011."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


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
