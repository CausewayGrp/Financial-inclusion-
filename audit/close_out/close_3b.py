# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-3B: the held payment observations, the cash-transfer, women's, remittance, provider and
measurement evidence the close-out brief unlocks (brief v5 W3c, Appendix B U2, U3, U6, U8–U14; CR-06). English and
Arabic change together.

  python3 close_3b.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes <work_dir>/visual_design_contract.json for run_stage.py --install (VIS-PAYMENT-ANATOMY gains a second panel).

Every original was read for this transaction (audit/close_out/w0/A3_cby.md, A4_projects.md, and the readings recorded
in PROGRESS.md for U6, U7/U8, U9 and U11). No new public route is created: the navigation contract enumerates routes
and is the programme steward's to edit, so the two compare cases are written into existing records instead.

- U2 / CR-06. VIS-PAYMENT-ANATOMY prints the 5,202,019 accounts of the first half of 2025 with CLM-010's caveat (no
  published definition; accounts, not people). OBS-00036 (58,512 POS transactions) stays held, with its reason.
- U6. The third-quarter 2024 channel values (POS terminals and transactions, ATMs and the amounts withdrawn, cheques at
  the CBY main centre and three branches, local SWIFT transfers) get their own panel in VIS-PAYMENT-ANATOMY, apart from
  2025 and not compared with it. The 2024 POS value series stays held (Q1 YER 31 million against YER 1,642 million in
  Q2, unexplained); the ATM governorate shares stay held (no perimeter stated); the H1-2025 sex-composition shares are
  shown in CLM-027 and the gender-gap Reading as shares of accounts and subscribers, never as a gap estimate. Every 19
  row that stays unpublished carries its reason; the Q3-2024 page locators are corrected (PDF and printed pages).
- U3. Three Cash Consortium of Yemen reports get their public locators; CWR-010 gains the cash-duration finding (with
  its design limits: savings could not be compared, and 274 is not the study's sample) and the last-mile cash-out
  finding, taken from the Cash for Nutrition and Livelihoods PAD (paragraphs 38 and 47), which reports the cash-transfer
  programme's own monitoring.
- U8. MA-005 carries the IMF Financial Access Survey's last Yemen values (2015) as dated context.
- U9. FMIIP PAD: the PAD locator is added; the FPS design rule (registered clients only; walk-in transactions excluded
  until a National Risk Assessment) in CLM-018 and /payments/; the 2018 firm survey (141 firms) as a dated limitation in
  CLM-062 and /firms/; "19 operating banks, four of them microfinance banks" beside the CBY-Aden list (26) and IGC's 31
  registered banks in CLM-008 and /providers/; the 876 → 3,244 exchanger pair, branches in the PAD and entities in
  IGC, in CLM-016 (now offered on /evidence/compare/). Not added, with reasons: the "10 km" sentence (a programme
  monitoring ceiling, not bound to the FMIIP population) and the access-point compare case (the reported coincidence
  with the Aide Memoire payment-site total was not found).
- U10. CWR-007 concordance: the FSD 2024 "99% of women" statement (p.15; a statement, not a measurement), YMN 2021
  (34% of active microfinance borrowers, February 2021, nine providers), SMEPS 2024 (44% female-owned, programme), the
  ACAPS Mahram report (December 2023, hypothesis only).
- U11. CWR-001: remittances as a share of GDP for 2024, 38.6% in the Spring 2025 Yemen Economic Monitor and "around one
  quarter" (no year) in Spring 2026, in CLM-043.
- U12. UCT status (no payment cycle since January 2025; ESPECRP closes 31 December 2026; the Cash for Nutrition and
  Livelihoods Project signed 2 September 2026 builds on it and does not restore the transfers) in CLM-045 and CWR-010.
- U13, U14. MA-001: MICS 2022–23 (one household bank-account item, not tabulated) and the World Bank's 2022 mobile
  phone survey (catalogue 5999; both areas of control); MA-009: the phone survey as an existing two-area instrument.
"""
import json, os, re, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import (Session, Table, TxError, refresh_self_counts, insert_ui_rows, register_rows,  # noqa: E402
                       apply_register_ar, apply_register_en, COL03, S03)

F = "CLOSE-3B"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")
TODAY = "2026-10-10"


# ================================================================================================ U2, U6: payments
PAY_H1 = "SRC-CBY-PAYREPORT-H1-2025"
PAY_Q3 = "SRC-CBY-PAYREPORT-Q3-2024"
OBS37_CAVEAT = ("Accounts as published in the first-half 2025 infographic (Accounts panel, NO. of Accounts), under no published "
                "definition: a count of accounts within the reporting scope of the Central Bank of Yemen – Aden, not of people "
                "or of active accounts (the caveat CLM-010 carries). Shown in VIS-PAYMENT-ANATOMY from close-out CR-06, 10 "
                "October 2026.")
OBS37_LOCATOR = ("page 1, «الحسابات» (Accounts) panel, bottom left: NO. of Accounts 5,202,019; re-read 10 October 2026 "
                 "(close-out CR-06)")
OBS36_ADD = (" Kept held (close-out CR-06, 10 October 2026): no January or February 2025 monthly POS release exists (the "
             "first is March 2025), so 58,512 cannot be confirmed as a January–June total, and the report's first-half POS "
             "value tile does not equal the sum of the March–June monthly POS values.")
Q3_SHOWN = OrderedDict([   # row -> scope note appended to its caveat
    ("OBS-00009", "POS terminals reported in the quarter."),
    ("OBS-00005", "POS transactions in the quarter (a flow)."),
    ("OBS-00010", "ATMs reported in the quarter."),
    ("OBS-00011", "Amount withdrawn from ATMs in rials during the quarter: an amount, not a number of withdrawals."),
    ("OBS-00012", "Amount withdrawn from ATMs in US dollars during the quarter: an amount, not a number of withdrawals."),
    ("OBS-00013", "Amount withdrawn from ATMs in Saudi riyals during the quarter: an amount, not a number of withdrawals."),
    ("OBS-00024", "Cheques at the CBY main centre and its Mukalla, Seiyun and Taiz branches only (the bulletin's perimeter)."),
    ("OBS-00023", "Value of cheques at the CBY main centre and its Mukalla, Seiyun and Taiz branches only (the bulletin's "
                  "perimeter)."),
    ("OBS-00029", "Local transfers through SWIFT between local banks and government institutions, as the bulletin counts "
                  "them."),
    ("OBS-00030", "Value, in rials, of the local transfers through SWIFT between local banks and government institutions."),
])
Q3_SHOWN_TAIL = (" Shown in the third-quarter 2024 panel of VIS-PAYMENT-ANATOMY (close-out U6, 10 October 2026), apart from "
                 "the first-half 2025 counts and not compared with them; values are not people.")
HELD = OrderedDict([   # row(s) -> reason appended to the caveat (every 19 row that stays unpublished says why)
    (("OBS-00001", "OBS-00002", "OBS-00003"),
     "Held (close-out U6, 10 October 2026): the bulletin says the set of banks covered changed between quarters (some "
     "stopped operating, others joined), so the quarterly card counts are not one series; the close-out publishes the "
     "bulletin's ATM, cheque, local SWIFT and POS values."),
    (("OBS-00004",),
     "Held (close-out U6, 10 October 2026): the third-quarter 2024 panel shows the bulletin's latest quarter only; earlier "
     "quarters are not drawn as a series."),
    (("OBS-00006", "OBS-00007", "OBS-00008"),
     "Held (close-out U6, 10 October 2026): the 2024 POS value series is not published, because the bulletin does not "
     "explain why the first-quarter value (YER 31 million) is so far below the second (YER 1,642 million)."),
    (("OBS-00017", "OBS-00018", "OBS-00019"),
     "Held (close-out U6, 10 October 2026): the bulletin does not say whether e-money issued is a stock or a flow."),
    (("OBS-00020",),
     "Published as text in CLM-010 (7 e-wallets in 2024 Q3); not drawn, because the wallet counts of different "
     "publications are not one series."),
    (("OBS-00021", "OBS-00022", "OBS-00025", "OBS-00026", "OBS-00027", "OBS-00028"),
     "Held (close-out U6, 10 October 2026): the third-quarter 2024 panel shows the bulletin's latest quarter only; earlier "
     "quarters are not drawn as a series."),
    (("OBS-00038", "OBS-00039", "OBS-00040", "OBS-00041", "OBS-00042"),
     "Published as text in CLM-027 and the gender-gap Reading (close-out U6, 10 October 2026): shares as the infographic "
     "prints them (its accounts panel does not define their base), not shares of people, and never a gender-gap "
     "estimate."),
    (("OBS-00043", "OBS-00044", "OBS-00045"),
     "Held (close-out U6, 10 October 2026): the infographic defines neither the card types nor the base of the shares."),
    (("OBS-00046", "OBS-00047", "OBS-00048", "OBS-00049", "OBS-00050"),
     "Held (close-out U6, 10 October 2026): the infographic does not state the perimeter of its ATM count or whether "
     "\"Sana'a\" means the governorate or the city, so the shares are not published as shares of ATMs."),
])
PAY_UI = [  # (ui_id, en, ar, note)
    ("UI-VIS-CAT-PAY-ATM-WITHDRAWALS-YER", "ATM withdrawals in rials", "سحوبات الصراف الآلي بالريال اليمني",
     "Close-out U6. Payment object IND-0007."),
    ("UI-VIS-CAT-PAY-ATM-WITHDRAWALS-USD", "ATM withdrawals in US dollars", "سحوبات الصراف الآلي بالدولار الأمريكي",
     "Close-out U6. Payment object IND-0008."),
    ("UI-VIS-CAT-PAY-ATM-WITHDRAWALS-SAR", "ATM withdrawals in Saudi riyals", "سحوبات الصراف الآلي بالريال السعودي",
     "Close-out U6. Payment object IND-0009."),
    ("UI-VIS-CAT-PAY-CHEQUES", "Cheques", "الشيكات", "Close-out U6. Payment object IND-0013."),
    ("UI-VIS-CAT-PAY-CHEQUE-VALUE", "Value of cheques", "قيمة الشيكات", "Close-out U6. Payment object IND-0014."),
    ("UI-VIS-CAT-PAY-SWIFT-LOCAL", "Local SWIFT transfers", "التحويلات المحلية عبر SWIFT",
     "Close-out U6. Payment object IND-0015."),
    ("UI-VIS-CAT-PAY-SWIFT-LOCAL-VALUE", "Value of local SWIFT transfers", "قيمة التحويلات المحلية عبر SWIFT",
     "Close-out U6. Payment object IND-0016."),
    ("UI-VIS-NOT-PAY-ATM-WITHDRAWALS", "An amount withdrawn in the quarter, not a number of withdrawals or people",
     "مبلغ سُحب خلال الربع، لا عدد عمليات سحب ولا أشخاص", "Close-out U6. 'Is not' line, IND-0007/0008/0009."),
    ("UI-VIS-NOT-PAY-CHEQUES", "The CBY main centre and its Mukalla, Seiyun and Taiz branches only; not people",
     "المركز الرئيسي للبنك المركزي وفروعه في المكلا وسيئون وتعز فقط؛ لا أشخاص", "Close-out U6. 'Is not' line, IND-0013/0014."),
    ("UI-VIS-NOT-PAY-SWIFT-LOCAL", "Transfers between local banks and government institutions; not people",
     "تحويلات بين البنوك المحلية والجهات الحكومية؛ لا أشخاص", "Close-out U6. 'Is not' line, IND-0015/0016."),
    ("UI-VIS-UNIT-YER-BILLION", "YER billion (nominal)", "مليار ريال يمني (بالقيمة الاسمية)", "Close-out U6. Unit YER_billion."),
    ("UI-VIS-UNIT-SAR-MILLION", "SAR million", "مليون ريال سعودي", "Close-out U6. Unit SAR_million."),
    ("UI-VIS-PANEL-PAY-2025H1", "First half of 2025: payment report (infographic)", "النصف الأول من 2025: تقرير المدفوعات (إنفوغرافيك)",
     "Close-out U6. Panel heading, VIS-PAYMENT-ANATOMY series h1_objects."),
    ("UI-VIS-PANEL-PAY-2024Q3", "Third quarter of 2024: payments bulletin, a separate publication, not compared",
     "الربع الثالث من 2024: نشرة المدفوعات، وهي إصدار منفصل لا يُقارَن بالإصدار الآخر", "Close-out U6. Panel heading, "
     "VIS-PAYMENT-ANATOMY series q3_2024_channels."),
]
PAY_OBJECT = OrderedDict([("IND-0007", "UI-VIS-CAT-PAY-ATM-WITHDRAWALS-YER"), ("IND-0008", "UI-VIS-CAT-PAY-ATM-WITHDRAWALS-USD"),
                          ("IND-0009", "UI-VIS-CAT-PAY-ATM-WITHDRAWALS-SAR"), ("IND-0013", "UI-VIS-CAT-PAY-CHEQUES"),
                          ("IND-0014", "UI-VIS-CAT-PAY-CHEQUE-VALUE"), ("IND-0015", "UI-VIS-CAT-PAY-SWIFT-LOCAL"),
                          ("IND-0016", "UI-VIS-CAT-PAY-SWIFT-LOCAL-VALUE")])
PAY_NOT = OrderedDict([("IND-0007", "UI-VIS-NOT-PAY-ATM-WITHDRAWALS"), ("IND-0008", "UI-VIS-NOT-PAY-ATM-WITHDRAWALS"),
                       ("IND-0009", "UI-VIS-NOT-PAY-ATM-WITHDRAWALS"), ("IND-0013", "UI-VIS-NOT-PAY-CHEQUES"),
                       ("IND-0014", "UI-VIS-NOT-PAY-CHEQUES"), ("IND-0015", "UI-VIS-NOT-PAY-SWIFT-LOCAL"),
                       ("IND-0016", "UI-VIS-NOT-PAY-SWIFT-LOCAL")])
PAY_UNIT = OrderedDict([("YER_billion", "UI-VIS-UNIT-YER-BILLION"), ("USD_million", "UI-VIS-UNIT-USD-MILLION"),
                        ("SAR_million", "UI-VIS-UNIT-SAR-MILLION")])
Q3_SERIES_IDS = ["OBS-00009", "OBS-00005", "OBS-00010", "OBS-00011", "OBS-00012", "OBS-00013", "OBS-00024", "OBS-00023",
                 "OBS-00029", "OBS-00030"]
ANATOMY = OrderedDict([   # 06 (and 11) text of VIS-PAYMENT-ANATOMY: two publications, two panels, never compared
    ("summary_en",
     "The first-half 2025 payment report of the Central Bank of Yemen – Aden (CBY-Aden) counts cards, ATMs, POS terminals, "
     "POS transactions, e-wallets, e-wallet subscribers and accounts; its third-quarter 2024 payments bulletin, a separate "
     "publication shown in its own panel, counts POS terminals and transactions, ATMs and the amounts withdrawn from them, "
     "cheques at the CBY main centre and three of its branches, and local SWIFT transfers. Each uses its own unit: accounts "
     "and subscribers are not necessarily unique people, transactions are events, amounts are nominal, and terminals are "
     "equipment. They cannot be combined into a people-level inclusion rate, because no documented method exists for "
     "matching and deduplicating them, and the two publications are not compared, because their reporting scope and "
     "definitions have not been reconciled."),
    ("summary_ar",
     "يعدّ تقرير المدفوعات للنصف الأول من 2025 الصادر عن البنك المركزي اليمني – عدن البطاقات وأجهزة الصراف الآلي وأجهزة "
     "نقاط البيع ومعاملات نقاط البيع والمحافظ الإلكترونية ومشتركيها والحسابات؛ أما نشرة المدفوعات للربع الثالث من 2024، "
     "وهي إصدار منفصل يُعرض في لوحة مستقلة، فتعدّ أجهزة نقاط البيع ومعاملاتها، وأجهزة الصراف الآلي والمبالغ المسحوبة منها، "
     "والشيكات في المركز الرئيسي للبنك المركزي وثلاثة من فروعه، والتحويلات المحلية عبر SWIFT. ولكلٍّ منها وحدته: فالحسابات "
     "والمشتركون ليسوا بالضرورة أشخاصًا فريدين، والمعاملات أحداث، والمبالغ اسمية، والأجهزة معدات. ولا يمكن دمجها في نسبة "
     "شمول على مستوى الأشخاص، لعدم وجود طريقة موثقة للمطابقة وإزالة التكرار، ولا يُقارن الإصداران، لأن نطاق الإبلاغ "
     "والتعريفات فيهما لم يُطابَقا."),
    ("definition_en",
     "Counts and amounts of payment-system items reported by the Central Bank of Yemen – Aden (CBY-Aden), each in its own "
     "unit: cards, ATMs, POS terminals, POS transactions, e-wallets, e-wallet subscribers and accounts for the first half "
     "of 2025; and POS terminals and transactions, ATMs, the amounts withdrawn from ATMs by currency, cheques and local "
     "SWIFT transfers for the third quarter of 2024."),
    ("definition_ar",
     "أعداد عناصر نظام المدفوعات ومبالغها كما أبلغ عنها البنك المركزي اليمني – عدن، كلٌّ بوحدته: البطاقات وأجهزة الصراف "
     "الآلي وأجهزة نقاط البيع ومعاملات نقاط البيع والمحافظ الإلكترونية ومشتركوها والحسابات للنصف الأول من 2025؛ وأجهزة نقاط "
     "البيع ومعاملاتها وأجهزة الصراف الآلي والمبالغ المسحوبة منها بحسب العملة والشيكات والتحويلات المحلية عبر SWIFT للربع "
     "الثالث من 2024."),
    ("period_en", "2025 H1; 2024 Q3 (a separate publication)"),
    ("period_ar", "النصف الأول من 2025؛ والربع الثالث من 2024 (إصدار منفصل)"),
    ("universe_en",
     "Payment-system items within the reporting scope of the Central Bank of Yemen – Aden (CBY-Aden) in each publication, "
     "each in its own unit; the 2024 cheques cover the CBY main centre and its Mukalla, Seiyun and Taiz branches only, and "
     "the local SWIFT transfers are transfers between local banks and government institutions."),
    ("universe_ar",
     "عناصر نظام المدفوعات ضمن نطاق الإبلاغ لدى البنك المركزي اليمني – عدن في كل إصدار، كلٌّ بوحدته؛ وتقتصر شيكات 2024 على "
     "المركز الرئيسي للبنك المركزي وفروعه في المكلا وسيئون وتعز، والتحويلات المحلية عبر SWIFT تحويلات بين البنوك المحلية "
     "والجهات الحكومية."),
    ("method_en",
     "Each count or amount is taken as published — in the first-half 2025 payment report (an infographic) and the "
     "third-quarter 2024 payments bulletin of the Central Bank of Yemen – Aden (CBY-Aden) — and kept in its own unit and "
     "panel; nothing is added together or combined into an index. A figure whose definition or period cannot be confirmed "
     "is held back with its reason, as the 2025 POS transaction count and the 2024 POS value series are."),
    ("method_ar",
     "يؤخذ كل عدد أو مبلغ كما نُشر — في تقرير المدفوعات للنصف الأول من 2025 (إنفوغرافيك) وفي نشرة المدفوعات للربع الثالث من "
     "2024 الصادرين عن البنك المركزي اليمني – عدن — ويبقى بوحدته وفي لوحته؛ ولا يُجمع شيء ولا يُدمج في مؤشر مركّب. ويُحجب "
     "الرقم الذي لا يمكن التحقق من تعريفه أو فترته مع ذكر السبب، كما هو حال عدد معاملات نقاط البيع لعام 2025 وسلسلة قيمة "
     "معاملات نقاط البيع لعام 2024."),
    ("limitations_en",
     "Cards, accounts, subscribers, transactions, amounts withdrawn and terminals are not people, and they cannot be "
     "combined into a single digital-inclusion score. The first-half 2025 counts are not compared with the third-quarter "
     "2024 bulletin until the reporting scope and definitions of the two publications are reconciled; the bulletin's "
     "cheques cover the CBY main centre and three of its branches only, and the 2025 accounts count has no published "
     "definition."),
    ("limitations_ar",
     "البطاقات والحسابات والمشتركون والمعاملات والمبالغ المسحوبة والأجهزة ليست أشخاصًا، ولا يمكن دمجها في درجة واحدة للشمول "
     "الرقمي. ولا تُقارن أعداد النصف الأول من 2025 بنشرة الربع الثالث من 2024 إلى أن يُطابَق نطاق الإبلاغ والتعريفات بين "
     "الإصدارين؛ وتقتصر شيكات النشرة على المركز الرئيسي للبنك المركزي وثلاثة من فروعه، ولا تعريف منشورًا لعدد الحسابات في "
     "2025."),
    ("currentness_en",
     "The counts refer to the first half of 2025 and, in a separate panel, to the third quarter of 2024. They should not be "
     "read as describing a later period unless a newer comparable payment report is published."),
    ("currentness_ar",
     "تعود الأعداد إلى النصف الأول من 2025، وفي لوحة منفصلة إلى الربع الثالث من 2024. ولا تُقرأ على أنها تصف فترة لاحقة ما لم "
     "يُنشر تقرير مدفوعات أحدث قابل للمقارنة."),
])
ANATOMY_11 = OrderedDict([
    ("what_it_shows_en", "What each count measures, in two publications kept apart: cards, accounts and subscribers are not "
                         "people or active users, transactions are not unique users, and amounts withdrawn are not numbers "
                         "of withdrawals."),
    ("what_it_shows_ar", "ما يقيسه كل عدد، في إصدارين يبقيان منفصلين: البطاقات والحسابات والمشتركون ليسوا أشخاصًا ولا "
                         "مستخدمين نشطين، والمعاملات ليست مستخدمين فريدين، والمبالغ المسحوبة ليست أعدادًا لعمليات السحب."),
    ("decision_value_en", "Separates cards, ATMs, POS terminals, transactions, wallets, subscribers, accounts, amounts "
                          "withdrawn, cheques and SWIFT transfers by measurement object, and the 2025 report from the 2024 "
                          "bulletin, before any comparison is made."),
    ("decision_value_ar", "يفصل البطاقات وأجهزة الصراف الآلي وأجهزة نقاط البيع والمعاملات والمحافظ والمشتركين والحسابات "
                          "والمبالغ المسحوبة والشيكات وتحويلات SWIFT بحسب موضوع القياس، ويفصل تقرير 2025 عن نشرة 2024، قبل "
                          "إجراء أي مقارنة."),
    ("source_period", "2025 H1; 2024 Q3 (separate panel)"),
    ("freshness_profile", "2025 H1 snapshot; 2024 Q3 bulletin (separate panel)"),
    ("data_inputs", "2025 H1 CBY cards, ATMs, POS, transactions, wallets, subscribers, accounts; 2024 Q3 CBY POS, ATMs, "
                    "ATM withdrawals, cheques, local SWIFT"),
    ("period", "2025 H1; 2024 Q3"),
])
ANATOMY_META = ("The first-half 2025 payment report of the Central Bank of Yemen – Aden counts cards, ATMs, point-of-sale "
                "terminals, transactions, e-wallets and accounts.",
                "The first-half 2025 payment report of the Central Bank of Yemen – Aden counts cards, ATMs, terminals, "
                "transactions, e-wallets and accounts; its third-quarter 2024 bulletin is shown apart.",
                "يعدّ تقرير المدفوعات للنصف الأول من 2025 لدى البنك المركزي اليمني – عدن البطاقات وأجهزة الصراف الآلي وأجهزة "
                "نقاط البيع والمعاملات والمحافظ والحسابات.",
                "يعدّ تقرير المدفوعات للنصف الأول من 2025 الصادر عن البنك المركزي اليمني – عدن البطاقات وأجهزة الصراف الآلي "
                "والأجهزة والمعاملات والمحافظ والحسابات؛ وتُعرض نشرته للربع الثالث من 2024 منفصلة.")

# 11 fields that restate the 06 text (TC-G01: prohibited inference = 06 limitations, part A; accessible summary = summary)
ANATOMY_11_MIRROR = OrderedDict([("prohibited_inference_en", "limitations_en"), ("prohibited_inference_ar", "limitations_ar"),
                                 ("accessible_summary_en", "summary_en"), ("accessible_summary_ar", "summary_ar"),
                                 ("denominator_universe", "universe_en")])
OBS09_CAVEAT_OLD = ("Label/value placement in infographic has been text-verified but should receive a visual QA check before "
                    "public release.")
OBS09_CAVEAT_NEW = ("Label and value checked against the page image on 10 October 2026 (close-out U6): PDF p.4 (printed p.1) "
                    "prints 151 under «عدد أجهزة نقاط الدفع في الربع الثالث» (POS terminals in the third quarter).")
HELD_SUBSCRIBERS = (("OBS-00014", "OBS-00015", "OBS-00016"),
                    "Published as text in CLM-010 (close-out U6, 10 October 2026); not drawn, because the subscriber "
                    "definitions of the 2024 bulletin and the 2025 report have not been reconciled.")
CONTRACT_TEXT = OrderedDict([
    ("form", "Two panels, one per publication: the first-half 2025 payment report and the third-quarter 2024 payments "
             "bulletin. One card per measurement object, each with its 'is not' line; no totals row, no population "
             "denominator and no comparison across the panels."),
    ("ordering", "Panel 1 (2025 H1): cards, ATMs, e-wallets, e-wallet subscribers, POS terminals, POS transactions, accounts. "
                 "Panel 2 (2024 Q3): POS terminals, POS transactions, ATMs, ATM withdrawals in rials, US dollars and Saudi "
                 "riyals, cheques and their value, local SWIFT transfers and their value."),
    ("transformation", "None. No card is summed with another, divided by population or set against a card in the other panel."),
    ("missing", "Values whose governed caveat requires a methodology note before public use are withheld (UI-VIS-WITHHELD): "
                "the object card shows what it counts, not the number. Rows of the 2024 bulletin that are not drawn carry "
                "their reason in their caveat (19_PAYMENTS_DATA)."),
    ("breaks", "Flagged objects carry NOT_COMPARABLE and the frame note UI-VIS-NOTE-NOT-COMPARABLE-2024Q3. The two panels are "
               "separate publications whose reporting scope and definitions have not been reconciled, so no comparison is "
               "drawn between them. Cards have no line, so no line-break marker is printed."),
    ("annotation", "Each panel is headed by its governed panel label (UI-VIS-PANEL-PAY-2025H1, UI-VIS-PANEL-PAY-2024Q3). Each "
                   "card prints its governed object label (x_label) and its governed 'is not' line (is_not_label). The "
                   "caveat field is an internal comparability note and is not printed; the frame prints the governed marker "
                   "labels instead."),
    ("mobile", "Panels and cards stack."),
    ("rtl", "Card order mirrors; the 2025 panel stays first."),
    ("fallback", "One table per panel: object, value or withheld state, what it is not."),
])
CONTRACT_RATIONALE = ("Keeps cards, accounts, subscribers, terminals, transactions, withdrawals, cheques and transfers as "
                      "different objects, and the 2025 report apart from the 2024 bulletin, before any comparison. "
                      "Card-first; no totals.")
PANEL_LABELS = ["UI-VIS-PANEL-PAY-2025H1", "UI-VIS-PANEL-PAY-2024Q3"]

# ================================================================================================ sources
FMIIP = "SRC-WB-FMIIP-P180708"
FMIIP_PAD = ("https://documents.worldbank.org/curated/en/099052825174515006/pdf/"
             "BOSIB-524dd7c7-d52c-4876-80ed-1e3ea9df2463.pdf")
PAD = "PAD (Report No. PADHI00396, 22 May 2025)"
CNL = "SRC-WB-YEM-CNL-2026-001"
CNL_URLS = ["https://projects.worldbank.org/en/projects-operations/project-detail/P514855",
            "https://documents.worldbank.org/curated/en/099061026114019678/pdf/BOSIB-24b35177-1756-452c-a8c5-602402705683.pdf",
            "https://documents.worldbank.org/curated/en/099090226095598089/pdf/P514855-f2c338ed-4910-4743-9b3b-564bebfa4be3.pdf"]
IGC = "SRC-IGC-AIDDATA-REMIT-YEM-2026"
ISR10 = "SRC-WB-ESPECRP-ISR10-2026-001"
YEM25 = "SRC-WB-YEM-ECON-MONITOR-2025-SPRING-001"
YEM26 = "SRC-WB-YEM-ECON-MONITOR-2026-SPRING-001"
FAS = "SRC-WB-WDI-FAS-YEM-001"
MAHRAM = "SRC-ACAPS-MAHRAM-2023-001"
MICS = "SRC-UNICEF-MICS-YEM-2022-001"
YMPS = "SRC-WB-YMPS-R1-2022-001"
FSD = "SRC-WB-FSD-2024-001"
YMN = "SRC-YMN-IMPACT-2021-001"
SMEPS = "SRC-SMEPS-AR2024-2025"


def src_row(sid, url, more, use, title, title_ar, pub, pub_ar, label, label_ar, date, issuer=None, host=None):
    return OrderedDict([("source_id", sid), ("primary_url", url), ("additional_urls", json.dumps(more) if more else None),
                        ("datasets_or_use", use), ("row_count", 0), ("display_title", title), ("display_title_ar", title_ar),
                        ("publisher", pub), ("publisher_ar", pub_ar), ("issuer", issuer), ("hosting_platform", host),
                        ("public_card_state", "CITATION_CARD"), ("rights_state", "NOT_ASSESSED"),
                        ("retrieval_date", TODAY), ("document_label", label), ("document_label_ar", label_ar),
                        ("document_date", date)])


NEW_SOURCES = [
    src_row(FAS, "https://data.worldbank.org/indicator/FB.ATM.TOTL.P5?locations=YE",
            ["https://data.worldbank.org/indicator/FB.CBK.BRCH.P5?locations=YE",
             "https://data.worldbank.org/indicator/FB.CBK.DPTR.P3?locations=YE"],
            "RESOURCE_LIBRARY_ONLY__MEASUREMENT_AGENDA_CONTEXT",
            "World Development Indicators: IMF Financial Access Survey series for Yemen (ATMs, commercial bank branches, "
            "depositors; last year 2015)",
            "مؤشرات التنمية العالمية: سلاسل مسح الوصول المالي لصندوق النقد الدولي لليمن (أجهزة الصراف الآلي وفروع البنوك "
            "التجارية والمودعون؛ آخر سنة 2015)",
            "World Bank", "البنك الدولي", "Survey dataset or indicator", "مسح أو مؤشر", "2026-10-08",
            issuer="International Monetary Fund, Financial Access Survey (data); World Bank, World Development Indicators"),
    src_row(MAHRAM, "https://www.acaps.org/fileadmin/Data_Product/Main_media/20231214_ACAPS_Yemen_Analysis_Hub_Dynamics_and_"
                    "effects_of_the_Mahram_practice_in_Yemen_01.pdf",
            ["https://acaps.org/en/countries/archives/detail/yemen-dynamics-and-effects-of-the-mahram-practice-in-yemen"],
            "RESOURCE_LIBRARY_ONLY__GENDER_HYPOTHESIS_CONTEXT",
            "Yemen: dynamics and effects of the Mahram practice (December 2023)",
            "اليمن: ديناميات ممارسة المَحرم وآثارها (ديسمبر 2023)",
            "ACAPS (Yemen Analysis Hub)", "ACAPS (مركز تحليل اليمن)", "Research or policy paper", "ورقة بحثية أو سياساتية",
            "2023-12-14"),
    src_row(YEM25, "https://documents.worldbank.org/curated/en/099822505292530706",
            ["https://documents.worldbank.org/curated/en/099822505292530706/pdf/IDU-7009880b-d070-472d-9bf2-5cc72a3fc75d.pdf",
             "https://documents.worldbank.org/curated/en/099103206302561755/pdf/IDU-7e9c81f8-af50-45f0-b454-e73ae077727e.pdf"],
            "RESOURCE_LIBRARY_ONLY__CURRENT_YEMEN_MACRO_CONTEXT",
            "Yemen Economic Monitor, Spring 2025: Persistent Fragility amid Rising Risks",
            "المرصد الاقتصادي لليمن، ربيع 2025: هشاشة مستمرة وسط تصاعد المخاطر",
            "World Bank", "البنك الدولي", "Research or policy paper", "ورقة بحثية أو سياساتية", "2025-05-29"),
    src_row(ISR10, "https://documents.worldbank.org/curated/en/099063026134041997/pdf/"
                   "P173582-a6512878-8a11-454d-98f2-213c6f4df820.pdf",
            ["https://projects.worldbank.org/en/projects-operations/project-detail/P173582"],
            "RESOURCE_LIBRARY_ONLY__CURRENT_YEMEN_CASH_IDENTITY_CONTEXT",
            "Yemen Emergency Social Protection Enhancement and COVID-19 Response Project (ESPECRP, P173582): Implementation "
            "Status and Results Report, sequence 10 (30 June 2026)",
            "المشروع الطارئ لتعزيز الحماية الاجتماعية والاستجابة لجائحة كوفيد-19 في اليمن (ESPECRP، P173582): تقرير حالة "
            "التنفيذ والنتائج، التسلسل 10 (30 يونيو 2026)",
            "World Bank", "البنك الدولي", "Project document", "وثيقة مشروع", "2026-06-30"),
    src_row(MICS, "https://www.unicef.org/yemen/documents/yemen-mics-multiple-indicator-cluster-survey",
            ["https://www.unicef.org/yemen/media/9006/file/YEMEN%20MICS%20MULTIPLE%20INDICATOR%20CLUSTER%20SURVEY.pdf"],
            "RESOURCE_LIBRARY_ONLY__MEASUREMENT_AGENDA_CONTEXT",
            "Yemen Multiple Indicator Cluster Survey (MICS) 2022–2023: Survey Findings Report",
            "المسح العنقودي متعدد المؤشرات في اليمن (MICS) 2022–2023: تقرير نتائج المسح",
            "Central Statistical Organization and UNICEF", "الجهاز المركزي للإحصاء واليونيسف", "Statistical release",
            "إصدار إحصائي", None, host="UNICEF Yemen"),
    src_row(YMPS, "https://microdata.worldbank.org/index.php/catalog/5999",
            ["https://doi.org/10.48529/3na0-xa83",
             "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099082223171029962"],
            "RESOURCE_LIBRARY_ONLY__MEASUREMENT_AGENDA_CONTEXT",
            "Yemen Mobile Phone Survey Monitoring, Round I (August–September 2022): Monitoring Food Insecurity and "
            "Employment in Yemen, catalogue entry",
            "مسح الهاتف المحمول في اليمن، الجولة الأولى (أغسطس–سبتمبر 2022): رصد انعدام الأمن الغذائي والعمالة في اليمن، "
            "قيد الفهرس",
            "World Bank", "البنك الدولي", "Survey dataset or indicator", "مسح أو مؤشر", "2023-09-07",
            host="World Bank Microdata Library (catalogue metadata only)"),
]
CCY_PUB = ("Cash Consortium of Yemen (CCY)", "Cash Consortium of Yemen (CCY)")   # the publisher_ar CR-11 set for this consortium
CCY_PROMOTE = OrderedDict([
    ("SRC-CCY-SAM-2024", OrderedDict([
        ("primary_url", "https://www.calpnetwork.org/wp-content/uploads/2024/11/SAM_Multiplie-Effect-of-Cash-Study.pdf"),
        ("display_title", "The Multiplier Effect of Multipurpose Cash Assistance in Ad' Dhali and Ja'ar Sub-districts in Yemen "
                          "(2024)"),
        ("display_title_ar", "الأثر المضاعف للمساعدات النقدية متعددة الأغراض في عزلتَي الضالع وجعار باليمن (2024)"),
        ("issuer", "Cash Consortium of Yemen, with REACH (cover)"), ("hosting_platform", "CALP Network"),
        ("document_date", "2024")])),
    ("SRC-CCY-CASH-DURATION-2026", OrderedDict([
        ("primary_url", "https://www.calpnetwork.org/gf-uploads/2026/06/Cash-Duration-Report_CCY_2026.06.22.pdf"),
        ("display_title", "The More the Merrier? Comparing Outcomes and Preferences for Three- vs. Six-Month Cash Transfers "
                          "(2026)"),
        ("display_title_ar", "كلما زاد كان أفضل؟ مقارنة النتائج والتفضيلات بين التحويلات النقدية لثلاثة أشهر ولستة أشهر "
                             "(2026)"),
        ("issuer", "Cash Consortium of Yemen, with Crisis Analysis (cover)"), ("hosting_platform", "CALP Network"),
        ("document_date", "2026")])),
    ("SRC-CCY-ISP-2024", OrderedDict([
        ("primary_url", "https://reliefweb.int/report/yemen/unseen-assistance-measuring-informal-social-protection-yemen"),
        ("additional_urls", json.dumps(["https://reliefweb.int/attachments/0e243818-f7a7-4d4e-bc03-dcec416b645b/The%20Unseen"
                                        "%20Assistance_Measuring%20Informal%20Social%20Protection%20in%20Yemen.pdf"])),
        ("display_title", "The Unseen Assistance: Measuring Informal Social Protection in Yemen (November 2024)"),
        ("display_title_ar", "المساعدة غير المرئية: قياس الحماية الاجتماعية غير الرسمية في اليمن (نوفمبر 2024)"),
        ("issuer", "Cash Consortium of Yemen and partners (ReliefWeb source list)"), ("hosting_platform", "ReliefWeb"),
        ("document_date", "2024-11-14")])),
])
CCY_COMMON = OrderedDict([("publisher", CCY_PUB[0]), ("publisher_ar", CCY_PUB[1]), ("public_card_state", "CITATION_CARD"),
                          ("non_public_locator_note", None), ("retrieval_date", TODAY),
                          ("document_label", "Research or policy paper"), ("document_label_ar", "ورقة بحثية أو سياساتية")])


def vs(t, src, loc, k="v"):
    return OrderedDict([("t", t), ("k", k), ("s", "READ"), ("src", src), ("loc", loc)])


# ================================================================================================ U3, U12: CLM-045, CWR-010
ISR_LOC = "ESPECRP ISR sequence 10 (ISR08077), archived 30-Jun-2026"
CNL_PAD_LOC = "Cash for Nutrition and Livelihoods Project PAD (9 June 2026), " + CNL_URLS[1]
CLM045_LIM = (
    "no ratio to 45,460 is drawn.",
    " A Cash Consortium of Yemen study (2026) compared three and six monthly transfers using programme data, with no "
    "randomised design and no group of households that received no assistance: the extra three transfers brought modest "
    "further gains in food security and less negative coping, and savings could not be compared, because only three "
    "households, all of them on six transfers, reported putting any money aside. The appraisal document of the Cash for "
    "Nutrition and Livelihoods Project (June 2026) reports from the cash-transfer programme's monitoring that “high "
    "transaction costs and long distances to financial service points severely impeded e-wallet uptake”, and plans for "
    "recipients to cash out through agents hired by financial service providers, given the scarcity of bank branches and "
    "ATMs.",
    "ولا تُحسب منها نسبة إلى 45,460.",
    " وقارنت دراسة لتحالف النقد في اليمن (Cash Consortium of Yemen، 2026) بين ثلاثة تحويلات شهرية وستة باستخدام بيانات "
    "البرنامج، من دون تصميم قائم على التوزيع العشوائي ولا مجموعة من الأسر لم تتلقَّ أي مساعدة: فأتت التحويلات الثلاثة "
    "الإضافية بمكاسب أخرى محدودة في الأمن الغذائي وبتراجع في استراتيجيات التكيّف السلبية، ولم يتسنَّ مقارنة الادخار، لأن "
    "ثلاث أسر فقط، كلها من متلقي التحويلات الستة، أفادت بادخار أي مبلغ. وتذكر وثيقة تقييم مشروع النقد مقابل التغذية وسبل "
    "العيش (يونيو 2026)، استنادًا إلى رصد برنامج التحويلات النقدية، أن «ارتفاع تكاليف المعاملات وبُعد المسافات عن نقاط "
    "الخدمات المالية أعاقا بشدة الإقبال على المحافظ الإلكترونية»، وتخطط لأن يسحب المستفيدون النقد عبر وكلاء يتعاقد معهم "
    "مقدمو الخدمات المالية، نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي.")
CLM045_CUR = (
    "The latest evidence in this record was published in 2026; the pilot material dates from May 2024.",
    " The programme the pilot belonged to has run no payment cycle since January 2025, for lack of funds, according to the "
    "World Bank's implementation report on the emergency social protection project that finances it (ESPECRP), archived "
    "on 30 June 2026; the project is due to close on 31 December 2026. The Cash for Nutrition and Livelihoods Project, "
    "whose financing agreement was signed on 2 September 2026, builds on ESPECRP's delivery systems but is designed to pay "
    "a different benefit, six months of cash for nutrition to pregnant women and mothers of children under two; it does "
    "not restore the unconditional transfers.",
    "نُشرت أحدث الأدلة في هذا السجل في 2026، أما مواد التجربة فصادرة في مايو 2024.",
    " ولم يُجرِ البرنامج الذي جرت ضمنه التجربة أي دورة دفع منذ يناير 2025 بسبب نقص التمويل، وفق تقرير التنفيذ الصادر عن "
    "البنك الدولي لمشروع الحماية الاجتماعية الطارئ الذي يموّله (ESPECRP)، المؤرشف في 30 يونيو 2026؛ ومن المقرر أن يُغلق "
    "المشروع في 31 ديسمبر 2026. أما مشروع النقد مقابل التغذية وسبل العيش، الذي وُقّعت اتفاقية تمويله في 2 سبتمبر 2026، فيبني "
    "على أنظمة الإيصال في مشروع الحماية الاجتماعية الطارئ لكنه مصمَّم لصرف منفعة مختلفة، هي نقد مقابل التغذية لمدة ستة أشهر "
    "للحوامل وأمهات الأطفال دون سن الثانية؛ ولا يعيد التحويلات غير المشروطة.")
CLM045_DEPS_ADD = ["SRC-CCY-CASH-DURATION-2026", ISR10, CNL]
CLM045_VS = [
    vs("30 June 2026", ISR10, ISR_LOC + ", report header and footer", "d"),
    vs("January 2025", ISR10, ISR_LOC + ", PDF p.4-5, section 6.1, comment on the UCT beneficiary indicators: \"No PCs "
                       "conducted since Jan 2025 due to lack of funds.\"", "d"),
    vs("31 December 2026", ISR10, ISR_LOC + ", PDF p.17-18, section 8: \"Operation Closing/Cancellation 31-Dec-2026\"", "d"),
    vs("2 September 2026", CNL, "Financing Agreement, Grant E734-RY, signature block (UNICEF 28-Aug-2026; IDA 02-Sep-2026), "
                           + CNL_URLS[2] + "; project page " + CNL_URLS[0] + ": 'Effective Date September 2, 2026'", "d"),
    vs("June 2026", CNL, CNL_PAD_LOC + ", date of the appraisal document; paragraph 47 (e-wallet uptake) and paragraph 38 "
                    "(cash-out through agents hired by financial service providers)", "d"),
    vs("three households", "SRC-CCY-CASH-DURATION-2026", "Cash Consortium of Yemen, 'The More the Merrier?' (2026), key findings p.1 "
                                             "(three vs six monthly transfers); p.3 (no unassisted control group); p.18 "
                                             "(savings: \"only three HHs, all of whom received six monthly transfers, "
                                             "reported a non-zero allocation to savings at endline\"); read 10 October 2026"),
]
CWR010_S6 = (
    "\n> The pilot material provides evidence",
    "\nThe programme has run no payment cycle since January 2025, for lack of funds, according to the World Bank's "
    "implementation report on ESPECRP, the emergency social protection project that finances it, archived on 30 June "
    "2026; the project is due to close on 31 December 2026. The Cash for Nutrition and Livelihoods Project, whose "
    "financing agreement was signed on 2 September 2026, builds on ESPECRP's delivery systems but is designed to pay a "
    "different benefit, six months of cash for nutrition to pregnant women and mothers of children under two; it does not "
    "restore the unconditional transfers.\n"
    "Two later findings mark where the evidence stops. A Cash Consortium of Yemen study (2026) compared three and six "
    "monthly transfers using programme data, with no randomised design and no group of households without assistance: "
    "the extra three transfers brought modest further gains in food security, and savings could not be compared, because "
    "only three households, all of them on six transfers, reported putting any money aside. And the appraisal document of "
    "the Cash for Nutrition and Livelihoods Project (June 2026) reports from the programme's monitoring that “high "
    "transaction costs and long distances to financial service points severely impeded e-wallet uptake”.\n"
    "> The pilot material provides evidence",
    "\n> تقدم مواد التجربة دليلًا",
    "\nولم يُجرِ البرنامج أي دورة دفع منذ يناير 2025 بسبب نقص التمويل، وفق تقرير التنفيذ الصادر عن البنك الدولي لمشروع "
    "الحماية الاجتماعية الطارئ (ESPECRP)، وهو المشروع الذي يموّل البرنامج، والمؤرشف في 30 يونيو 2026؛ ومن المقرر أن يُغلق "
    "المشروع في 31 ديسمبر 2026. أما مشروع النقد مقابل التغذية وسبل العيش، الذي وُقّعت اتفاقية تمويله في 2 سبتمبر 2026، فيبني "
    "على أنظمة الإيصال في مشروع الحماية الاجتماعية الطارئ لكنه مصمَّم لصرف منفعة مختلفة، هي نقد مقابل التغذية لمدة ستة أشهر "
    "للحوامل وأمهات الأطفال دون سن الثانية؛ ولا يعيد التحويلات غير المشروطة.\n"
    "وتحدّد خلاصتان لاحقتان موضع توقف الدليل. فقد قارنت دراسة لتحالف النقد في اليمن (Cash Consortium of Yemen) صدرت في 2026 "
    "بين ثلاثة تحويلات شهرية وستة باستخدام بيانات البرنامج، من دون تصميم قائم على التوزيع العشوائي ولا مجموعة من الأسر لم "
    "تتلقَّ أي مساعدة: فأتت التحويلات الثلاثة الإضافية بمكاسب أخرى محدودة في الأمن الغذائي، ولم يتسنَّ مقارنة الادخار، لأن "
    "ثلاث أسر فقط، كلها من متلقي التحويلات الستة، أفادت بادخار أي مبلغ. وتذكر وثيقة تقييم مشروع النقد مقابل التغذية وسبل "
    "العيش (يونيو 2026)، استنادًا إلى رصد البرنامج، أن «ارتفاع تكاليف المعاملات وبُعد المسافات عن نقاط الخدمات المالية "
    "أعاقا بشدة الإقبال على المحافظ الإلكترونية».\n"
    "> تقدم مواد التجربة دليلًا")
CWR010_PERIOD = (
    "World Bank and G2Px material, May 2024 · reference period of the recipient figure not recorded",
    "World Bank and G2Px material, May 2024 · reference period of the recipient figure not recorded · Cash Consortium of "
    "Yemen study (2026) and World Bank project documents (2025–2026)",
    "مواد البنك الدولي ومبادرة G2Px، مايو 2024 · الفترة المرجعية لعدد المستفيدين غير مسجلة",
    "مواد البنك الدولي ومبادرة G2Px، مايو 2024 · الفترة المرجعية لعدد المستفيدين غير مسجلة · دراسة لتحالف النقد في اليمن "
    "(Cash Consortium of Yemen، 2026) ووثائق مشروعات البنك الدولي (2025–2026)")

# ================================================================================================ U8: MA-005
MA005_ADD = (
    " The IMF Financial Access Survey, as published in the World Bank's World Development Indicators (series "
    "FB.ATM.TOTL.P5, FB.CBK.BRCH.P5 and FB.CBK.DPTR.P3), last reports Yemen for 2015: 5.81 ATMs and 1.48 commercial bank "
    "branches per 100,000 adults, and 103.1 depositors with commercial banks per 1,000 adults. The series stops in 2015 and "
    "its population denominators are the IMF's; the values are dated historical context, not a current measure of access.",
    " ويعود آخر ما ينشره مسح الوصول المالي لصندوق النقد الدولي عن اليمن، كما تعرضه مؤشرات التنمية العالمية للبنك الدولي "
    "(السلاسل FB.ATM.TOTL.P5 وFB.CBK.BRCH.P5 وFB.CBK.DPTR.P3)، إلى عام 2015: 5.81 جهاز صراف آلي و1.48 فرع للبنوك التجارية "
    "لكل 100,000 بالغ، و103.1 مودِع لدى البنوك التجارية لكل 1,000 بالغ. وتتوقف السلسلة في 2015، وقواعد الاحتساب السكانية "
    "فيها هي التي يعتمدها الصندوق؛ فهذه القيم سياق تاريخي مؤرخ، لا مقياس حالي للوصول.")

# ================================================================================================ U9: FMIIP PAD additions
CLM018_LIM = (
    "no later operational state is recorded here.",
    " The project's appraisal document (May 2025) also sets a design rule for FPS: all users must be registered clients of "
    "financial institutions regulated by CBY-Aden, and walk-in and over-the-counter transactions, in which the sender or "
    "the recipient holds no account at a regulated institution, are excluded until a National Risk Assessment is "
    "completed and risk-mitigation measures are adopted. This is a design condition, not evidence of operation, and it "
    "means that people without such an account could not use FPS.",
    "ولا يسجل هذا الدليل أي وضع تشغيلي لاحق.",
    " وتضع وثيقة تقييم المشروع (مايو 2025) أيضًا قاعدة تصميم لنظام الدفع السريع: أن يكون جميع مستخدميه عملاء مسجلين لدى "
    "مؤسسات مالية خاضعة لتنظيم البنك المركزي اليمني – عدن، وأن تُستبعد معاملات العملاء العابرين والمعاملات عبر الشبّاك، أي "
    "تلك التي لا يملك فيها المرسل أو المستلم حسابًا لدى مؤسسة خاضعة للتنظيم، إلى أن يُستكمل التقييم الوطني للمخاطر وتُعتمد "
    "تدابير للحد منها. وهذا شرط تصميم لا دليل على التشغيل، ويعني أن من لا يملك مثل هذا الحساب لن يستطيع استخدام النظام.")
CLM018_VS = [vs("May 2025", FMIIP, PAD + ", paragraph 26, printed p.8 (PDF p.18): \"All users of the FPS must be registered "
                                   "clients of regulated financial institutions by CBY Aden\" ... \"Walk-in and over-the-"
                                   "counter transactions ... will be excluded from FPS usage until a comprehensive National "
                                   "Risk Assessment is completed\"; read 10 October 2026", "d")]
PAY_S7 = (
    "inclusion outcomes.",
    "inclusion outcomes. The project's appraisal document (May 2025) adds a design rule: only registered clients of "
    "regulated financial institutions may use FPS, and walk-in and over-the-counter transactions, in which the sender or "
    "the recipient holds no account at a regulated financial institution, are excluded until a National Risk Assessment "
    "is completed and risk-mitigation measures are adopted. That is a design condition, which would leave people without "
    "an account outside the system, not evidence that the system operates.",
    "نتائج الشمول.",
    "نتائج الشمول. وتضيف وثيقة تقييم المشروع (مايو 2025) قاعدة تصميم: ألا يستخدم نظام الدفع السريع إلا العملاء المسجلون لدى "
    "مؤسسات مالية خاضعة للتنظيم، وأن تُستبعد معاملات العملاء العابرين والمعاملات عبر الشبّاك، أي تلك التي لا يملك فيها "
    "المرسل أو المستلم حسابًا لدى مؤسسة مالية خاضعة للتنظيم، إلى أن يُستكمل التقييم الوطني للمخاطر وتُعتمد تدابير للحد منها. "
    "وهذا شرط تصميم من شأنه أن يُبقي من لا يملك حسابًا خارج النظام، لا دليل على أن النظام يعمل.")
PAD10 = (PAD + ", paragraph 10, printed p.3 (PDF p.13): \"According to a 2018 World Bank Group survey involving 141 firms, "
         "less than 50 percent of large enterprises, 18.5 percent of medium-sized businesses, and 6.1 percent of small firms "
         "reported having access to a functioning bank branch. Alarmingly, 38.8 percent indicated having no access to any "
         "bank branch whatsoever.\"; read 10 October 2026")
CLM062_LIM = (
    "not comparable with the Findex account-ownership rate.",
    " An older figure is not comparable either: the appraisal document of the World Bank-financed FMIIP project (May 2025) "
    "cites a 2018 World Bank Group survey of 141 firms in which less than 50% of large enterprises, 18.5% of medium-sized "
    "businesses and 6.1% of small firms reported access to a functioning bank branch, and 38.8% reported no access to any "
    "bank branch. The document does not name the survey further, and its question and sample differ from the 2022 survey's.",
    "في المؤشر العالمي للشمول المالي (Global Findex).",
    " ولا يقارَن بها رقم أقدم أيضًا: فوثيقة تقييم مشروع FMIIP الممول من البنك الدولي (مايو 2025) تستشهد بمسح أجرته مجموعة "
    "البنك الدولي في 2018 وشمل 141 منشأة، أفاد فيه أقل من 50% من المنشآت الكبيرة و18.5% من المنشآت المتوسطة و6.1% من "
    "المنشآت الصغيرة بإمكانية الوصول إلى فرع مصرفي يعمل، وأفاد 38.8% بعدم الوصول إلى أي فرع مصرفي. ولا تسمّي الوثيقة المسح "
    "بأكثر من ذلك، ويختلف سؤاله وعينته عن سؤال مسح 2022 وعينته.")
CLM062_VS = [vs("141", FMIIP, PAD10), vs("less than 50%", FMIIP, PAD10), vs("18.5%", FMIIP, PAD10), vs("6.1%", FMIIP, PAD10),
             vs("38.8%", FMIIP, PAD10), vs("May 2025", FMIIP, PAD + ", date of the appraisal document", "d")]
FIRMS_S6 = (
    "do not establish that the programme caused the results.",
    "do not establish that the programme caused the results. In a 2018 World Bank Group survey of 141 firms, cited in the "
    "FMIIP appraisal document (May 2025), 6.1% of small firms, 18.5% of medium-sized businesses and less than 50% of large "
    "enterprises reported access to a functioning bank branch; it is a different survey with a different question, so it "
    "is not a baseline for the 2022 seven-governorate survey.",
    "ولا تثبت أن البرنامج سبب النتيجة.",
    "ولا تثبت أن البرنامج سبب النتيجة. وفي مسح أجرته مجموعة البنك الدولي في 2018 وشمل 141 منشأة، تستشهد به وثيقة تقييم "
    "مشروع FMIIP (مايو 2025)، أفادت 6.1% من المنشآت الصغيرة و18.5% من المنشآت المتوسطة وأقل من 50% من المنشآت الكبيرة "
    "بإمكانية الوصول إلى فرع مصرفي يعمل؛ وهو مسح مختلف بسؤال مختلف، فلا يُتخذ خط أساس لمسح 2022 في المحافظات السبع.")
PAD7_BANKS = (PAD + ", paragraph 7, printed p.2 (PDF p.12): \"Currently, there are 19 operating banks registered in Yemen, four "
              "of which are microfinance banks.\" No source or count date; read 10 October 2026")
IGC31 = ("International Growth Centre final report YEM-24338 (February 2026), section 3.1, printed p.22: \"In 2015, Yemen had "
         "19 operating banks, excluding the National Bank of Commerce and Investment, which was under liquidation. More "
         "recent data from Government CBY indicate an increase in the number of registered banks to 31\"; no date; read 10 "
         "October 2026")
CLM008_LIM = (
    "market share or participation in payment systems.",
    " Two other publishers give other counts, neither taken from a dated list: the appraisal document of the World "
    "Bank-financed FMIIP project (May 2025) states that “there are 19 operating banks registered in Yemen, four of which "
    "are microfinance banks”, citing no source, the same number of operating banks that an International Growth Centre "
    "report gives for 2015; and that report (February 2026) cites government CBY data for 31 registered banks, without a "
    "date. The appraisal document's four microfinance banks are not reconciled with the 12 that this resource identifies "
    "by name on the CBY-Aden list. They count different things at different dates, and none of the three counts "
    "establishes which banks operate.",
    "ولا المشاركة في أنظمة الدفع.",
    " ويورد ناشران آخران عددين آخرين، لا يستند أيٌّ منهما إلى قائمة مؤرخة: إذ تذكر وثيقة تقييم مشروع FMIIP الممول من "
    "البنك الدولي (مايو 2025) أن «هناك 19 بنكًا عاملًا مسجلًا في اليمن، أربعة منها بنوك تمويل أصغر»، من دون ذكر مصدر، وهو "
    "العدد نفسه من البنوك العاملة الذي يورده تقرير للمركز الدولي للنمو لعام 2015؛ ويستشهد ذلك التقرير (فبراير 2026) ببيانات "
    "البنك المركزي اليمني التابع للحكومة عن 31 بنكًا مسجلًا، من دون تاريخ. ولا تُطابَق بنوك التمويل الأصغر الأربعة في وثيقة "
    "التقييم مع البنوك الـ12 التي يحددها هذا المورد بالاسم في قائمة البنك المركزي اليمني – عدن. وهي أعداد لأشياء مختلفة في "
    "تواريخ مختلفة، ولا يثبت أيٌّ من الأعداد الثلاثة أي البنوك تعمل.")
CLM008_VS = [vs("19", FMIIP, PAD7_BANKS), vs("31", IGC, IGC31),
             OrderedDict([("t", "12"), ("k", "v"), ("s", "SEE:CLM-055")]),
             vs("May 2025", FMIIP, PAD + ", date of the appraisal document", "d"),
             vs("February 2026", IGC, "International Growth Centre final report YEM-24338, cover date February 2026", "d")]
PROV_S3 = (
    "or reach to underserved clients.",
    "or reach to underserved clients. Two other publishers give other counts: the appraisal document of the World "
    "Bank-financed FMIIP project (May 2025) states that 19 banks are operating, four of them microfinance banks, citing no "
    "source or count date (an International Growth Centre report gives the same 19 operating banks for 2015); and that "
    "report (February 2026) cites government CBY data for 31 registered banks. These are third-party statements, not "
    "lists; they count different things at different dates, the appraisal document's four microfinance banks are not "
    "reconciled with the 12 named above, and none of the three counts establishes which banks operate.",
    "أو الوصول إلى الفئات الأقل حصولًا على الخدمات.",
    "أو الوصول إلى الفئات الأقل حصولًا على الخدمات. ويورد ناشران آخران عددين آخرين: إذ تذكر وثيقة تقييم مشروع FMIIP الممول "
    "من البنك الدولي (مايو 2025) أن 19 بنكًا تعمل، أربعة منها بنوك تمويل أصغر، من دون ذكر مصدر أو تاريخ للعدّ (ويورد تقرير "
    "للمركز الدولي للنمو العدد نفسه، 19 بنكًا عاملًا، لعام 2015)؛ ويستشهد ذلك التقرير (فبراير 2026) ببيانات البنك المركزي "
    "اليمني التابع للحكومة عن 31 بنكًا مسجلًا. وهذه تصريحات لجهات أخرى لا قوائم؛ وهي تعدّ أشياء مختلفة في تواريخ مختلفة، "
    "ولا تُطابَق بنوك التمويل الأصغر الأربعة في وثيقة التقييم مع البنوك الـ12 المذكورة أعلاه، ولا يثبت أيٌّ من الأعداد "
    "الثلاثة أي البنوك تعمل.")
PAD7_EXCH = (PAD + ", paragraph 7, printed p.2 (PDF p.12): \"the expansion of money exchangers branches from 876 in 2017 to "
             "3,244 in 2019\" (no source); the International Growth Centre report YEM-24338 (February 2026), section 3.4, "
             "printed p.32, presents the same pair as World Bank estimates of entities, including exchange firms and "
             "microfinance institutions; read 10 October 2026")
CLM016_LIM = (
    "and the 2026 roster states no issue date.",
    " Older counts are not comparable either: the FMIIP appraisal document (May "
    "2025) reports money-exchanger branches rising from 876 in 2017 to 3,244 in 2019, citing no source, while an "
    "International Growth Centre report (February 2026) presents the same pair as World Bank estimates of entities, "
    "including exchange firms and microfinance institutions. One pair of numbers carries two labels, branches or "
    "entities, and neither is a roster count, so neither is compared with the 382 entries here.",
    "ولا تذكر قائمة 2026 تاريخ صدورها.",
    " ولا تُقارن بها أعداد أقدم أيضًا: إذ تذكر وثيقة تقييم مشروع FMIIP (مايو 2025) أن فروع شركات الصرافة ارتفعت من 876 "
    "في 2017 إلى 3,244 في 2019، من دون ذكر مصدر، بينما يعرض تقرير للمركز الدولي للنمو (فبراير 2026) الزوج نفسه من الأرقام "
    "بوصفه تقديرات للبنك الدولي لعدد الكيانات، بما فيها شركات الصرافة ومؤسسات التمويل الأصغر. فالزوج الواحد من الأرقام "
    "يحمل وصفين، فروعًا أو كيانات، ولا يمثل أيٌّ منهما عدًّا من قائمة رسمية، لذلك لا يُقارن أيٌّ منهما بالقيود الـ382 هنا.")
CLM016_VS = [vs("876", FMIIP, PAD7_EXCH), vs("3,244", FMIIP, PAD7_EXCH),
             vs("May 2025", FMIIP, PAD + ", date of the appraisal document", "d"),
             vs("February 2026", IGC, "International Growth Centre final report YEM-24338, cover date February 2026", "d")]
PROV_S10 = (
    "branch activity or geographic reach.",
    "branch activity or geographic reach. How many there were before the roster depends on the label: the FMIIP appraisal "
    "document (May 2025) reports money-exchanger branches rising from 876 in 2017 to 3,244 in 2019, and an International "
    "Growth Centre report (February 2026) presents the same pair as entities, including microfinance institutions. "
    "Branches and entities are different units, and neither is a roster count (record CLM-016).",
    "أو نطاق انتشارهم الجغرافي.",
    "أو نطاق انتشارهم الجغرافي. ويتوقف عدد منشآت الصرافة قبل القائمة الرسمية على الوصف المستخدم: فوثيقة تقييم مشروع FMIIP "
    "(مايو 2025) تذكر أن فروع شركات الصرافة ارتفعت من 876 في 2017 إلى 3,244 في 2019، ويعرض تقرير للمركز الدولي للنمو (فبراير "
    "2026) الزوج نفسه من الأرقام بوصفه كيانات تشمل مؤسسات التمويل الأصغر. والفروع والكيانات وحدتان مختلفتان، ولا يمثل أيٌّ "
    "منهما عدًّا من قائمة رسمية (السجل CLM-016).")

# ================================================================================================ U6, U10: women's evidence
PAY_LOC_ACC = ("page 1, «الحسابات» (Accounts) panel, bottom left: bars ذكر 81% / أنثى 18% / شركات 1%, caption «نسبة عدد "
               "المواطنين الذين يمتلكون حسابات بنكية وفق النوع»; re-read 10 October 2026 (close-out CR-13)")
PAY_LOC_EW = ("page 1, «المحافظ الإلكترونية» (E-wallets) panel, bottom right (NO. of Subscribers 2,102,484): donut 84% male / "
              "16% female, caption «نسبة عدد المشتركين وفق النوع»; re-read 10 October 2026 (close-out CR-13)")
YMN_LOC = ("Table 5, printed p.22 (PDF p.22): total row, column «نساء (%)» under the borrowers «المقترضون» = 34%; active "
           "borrowers 89,733; nine providers (two microfinance banks and seven institutions or programmes); data to "
           "February 2021 (table source: SFD); provider shares from 11% to 73%; read 10 October 2026")
SMEPS_LOC = ("SMEPS Annual Report 2024 (published 8 October 2025), Executive Summary, PDF p.4: \"supporting 8,217 MSMEs, of "
             "which 44% were female-owned\"; read 10 October 2026")
MAHRAM_LOC = ("ACAPS, 'Yemen: dynamics and effects of the Mahram practice', 14 December 2023 (5 pp.): mahram requirements "
              "enforced from early 2022 in areas under the de facto authorities; secondary review and 17 key informant "
              "interviews; the text does not mention financial services; read 10 October 2026")
WOMEN_SHARES = (
    " Other records give women's shares of particular services; they are not account-ownership rates and are not "
    "compared with the Findex waves. The first-half 2025 payment report of the Central Bank of Yemen – Aden shows, in its "
    "accounts panel, 81% men, 18% women and 1% companies, shares whose base it does not define (the panel counts "
    "accounts, its caption speaks of citizens, and one category is companies), and, among e-wallet subscribers, 84% men "
    "and 16% women; none of these is a share of people. A Yemen Microfinance Network table prints 34% as women's share in "
    "its total row for the 89,733 active borrowers of nine microfinance providers in February 2021; the providers' own "
    "shares range from 11% to 73%. The Small and Micro Enterprise Promotion Service (SMEPS) reports that 44% of the 8,217 "
    "enterprises it supported in 2024 were female-owned, a programme figure, not a national one. ACAPS (December 2023) "
    "documents the mahram requirement in areas under the de facto authorities, but not its effect on financial services, "
    "so mobility rules remain a hypothesis.",
    " وتعطي سجلات أخرى حصص النساء في خدمات بعينها؛ وهي ليست معدلات لامتلاك الحساب، ولا تُقارن بموجات Findex. فتقرير "
    "المدفوعات للنصف الأول من 2025 الصادر عن البنك المركزي اليمني – عدن يُظهر في لوحة الحسابات 81% للرجال و18% للنساء و1% "
    "للشركات، وهي حصص لا يحدد التقرير أساسها (فاللوحة تعدّ حسابات، وتعليقها يتحدث عن المواطنين، وإحدى الفئات هي الشركات)، "
    "ويُظهر بين مشتركي المحافظ الإلكترونية 84% للرجال و16% للنساء؛ وليس أيٌّ منها حصة من الأشخاص. ويطبع جدول لشبكة اليمن "
    "للتمويل الأصغر نسبة 34% بوصفها حصة النساء في صفّ الإجمالي لـ89,733 مقترضًا نشطًا لدى تسعة مقدمي خدمات تمويل أصغر في "
    "فبراير 2021؛ وتتراوح حصص مقدمي الخدمات أنفسهم بين 11% و73%. وتفيد وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS) بأن 44% "
    "من المنشآت الـ8,217 التي دعمتها في 2024 مملوكة لنساء، وهو رقم برنامجي لا وطني. ويوثّق تقرير ACAPS (ديسمبر 2023) اشتراط "
    "المَحرم في المناطق الخاضعة لسلطات الأمر الواقع، لا أثره على الخدمات المالية، فتبقى قيود التنقل فرضية.")
WOMEN_DEPS = [PAY_H1, YMN, SMEPS, MAHRAM]
WOMEN_VS = [vs("81%", PAY_H1, PAY_LOC_ACC), vs("18%", PAY_H1, PAY_LOC_ACC), vs("1%", PAY_H1, PAY_LOC_ACC),
             vs("84%", PAY_H1, PAY_LOC_EW), vs("16%", PAY_H1, PAY_LOC_EW),
             vs("89,733", YMN, YMN_LOC), vs("34%", YMN, YMN_LOC), vs("11%", YMN, YMN_LOC), vs("73%", YMN, YMN_LOC),
             vs("February 2021", YMN, YMN_LOC, "d"),
             vs("8,217", SMEPS, SMEPS_LOC), vs("44%", SMEPS, SMEPS_LOC),
             vs("December 2023", MAHRAM, MAHRAM_LOC, "d")]
FSD_LOC = ("Yemen Financial Sector Diagnostics (2024), Executive Summary, printed p.15 (PDF p.15): \"The population is "
           "almost entirely unbanked, including about 90% of men and 99% of women.\" No year or footnote on the sentence "
           "(the brief's p.25 and '1% of women' were not found); read 10 October 2026")
CLM027_LIM = (
    "The FMIIP appraisal document (May 2025) says that “two percent” of women hold a bank account, with no date and no "
    "source; that is a statement, not a measurement.",
    "The FMIIP appraisal document (May 2025) says that “two percent” of women hold a bank account, and the World Bank's "
    "Yemen Financial Sector Diagnostics (2024) that the population is “almost entirely unbanked, including about 90% of "
    "men and 99% of women”; neither gives a date or a source, so these are statements, not measurements.",
    "وتذكر وثيقة تقييم مشروع FMIIP (مايو 2025) أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، من دون تاريخ ولا مصدر؛ "
    "وهذا تصريح لا قياس.",
    "وتذكر وثيقة تقييم مشروع FMIIP (مايو 2025) أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، ويذكر تشخيص القطاع "
    "المالي في اليمن الصادر عن البنك الدولي (2024) أن السكان «خارج النظام المصرفي بالكامل تقريبًا، بمن فيهم نحو 90% من "
    "الرجال و99% من النساء»؛ ولا يذكر أيٌّ منهما تاريخًا ولا مصدرًا، فهذان تصريحان لا قياسان.")
CLM027_VS = [vs("90%", FSD, FSD_LOC), vs("99%", FSD, FSD_LOC)]
GENDER = "/readings/gender-gap-measured-causes-open/"
# AR-004 (register R33, apply_in "CLOSE-3 (with U10)"): the adjudicated Arabic of the gender Reading's section 2, in its
# conditional final form (U10 adds the FSD 2024 statement, so the concordance counts four figures, two of them
# measurements), and the register's English instruction applied to the existing English cell.
AR004_COND = [
    ("وترد في المواد المنشورة ثلاثة أرقام عن امتلاك النساء للحساب، لكن اثنين منها فقط ناتجان عن قياس.",
     "وترد في المواد المنشورة أربعة أرقام عن امتلاك النساء للحساب، لكن اثنين منها فقط ناتجان عن قياس."),
    ("أما وثيقة تقييم مشروع FMIIP الممول من البنك الدولي فتذكر أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، من دون "
     "تاريخ أو مصدر، فلا يُستخدم هذا الرقم قياسًا.",
     "أما وثيقة تقييم مشروع FMIIP الممول من البنك الدولي فتذكر أن «اثنين في المئة» من النساء يملكن حسابًا مصرفيًا، ويذكر "
     "تشخيص القطاع المالي في اليمن الصادر عن البنك الدولي (2024) أن السكان «خارج النظام المصرفي بالكامل تقريبًا، بمن فيهم "
     "نحو 90% من الرجال و99% من النساء»؛ ولا يذكر أيٌّ منهما تاريخًا أو مصدرًا، فلا يُستخدم أيٌّ من الرقمين قياسًا."),
]
AR004_EN = [
    ("\nThat moves attention away from “fixing women” and towards the conditions under which access is produced.",
     "\nAnswering it requires independent evidence on the barriers and conditions that shape access, not a prior causal "
     "assumption."),
    ("Three figures for women’s account ownership circulate, and only two of them are measurements.",
     "Four figures for women’s account ownership appear in published material, and only two of them are measurements."),
    ("The appraisal document of the World Bank-financed FMIIP project says that “two percent” of women hold a bank account, "
     "with no date and no source, so it is not used here as a measurement.",
     "The appraisal document of the World Bank-financed FMIIP project says that “two percent” of women hold a bank account, "
     "and the World Bank's Yemen Financial Sector Diagnostics (2024) that the population is “almost entirely unbanked, "
     "including about 90% of men and 99% of women”; neither gives a date or a source, so neither is used here as a "
     "measurement."),
]
GENDER_S3 = (
    "It shows why one-dimensional explanations are risky.",
    "It shows why one-dimensional explanations are risky.\n"
    "Records of particular services give women's shares, not ownership rates, and none of them divides the gap. A Yemen "
    "Microfinance Network table prints 34% as women's share in its total row for the 89,733 active borrowers of nine "
    "microfinance providers in February 2021; 44% of the 8,217 enterprises SMEPS supported in 2024 were female-owned, a "
    "programme figure; and the first-half 2025 payment report of the Central Bank of Yemen – Aden shows women at 18% in "
    "its accounts panel, whose base it does not define, and at 16% of e-wallet subscribers: none of these is a share of "
    "people or a gap estimate. One named hypothesis has documentation: ACAPS (December 2023) describes the mahram "
    "requirement, under which women must travel with a male relative, enforced from early 2022 in areas under the de "
    "facto authorities. It does not mention financial services, so it supports a question to test, not a finding.",
    "لكنه يبين لماذا تنطوي التفسيرات الأحادية على مخاطرة.",
    "لكنه يبين لماذا تنطوي التفسيرات الأحادية على مخاطرة.\n"
    "وتعطي سجلات خدمات بعينها حصص النساء فيها، لا معدلات امتلاك، ولا يقسم أيٌّ منها الفجوة. فجدول لشبكة اليمن للتمويل "
    "الأصغر يطبع نسبة 34% بوصفها حصة النساء في صفّ الإجمالي لـ89,733 مقترضًا نشطًا لدى تسعة مقدمي خدمات تمويل أصغر في فبراير "
    "2021؛ وكانت 44% من المنشآت الـ8,217 التي دعمتها وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS) في 2024 مملوكة لنساء، وهو "
    "رقم برنامجي؛ ويُظهر تقرير المدفوعات للنصف الأول من 2025 الصادر عن البنك المركزي اليمني – عدن النساء بنسبة 18% في لوحة "
    "الحسابات، التي لا يحدد التقرير أساسها، و16% من مشتركي المحافظ الإلكترونية: وليس أيٌّ منها حصة من الأشخاص ولا تقديرًا "
    "للفجوة. ولفرضية واحدة مسمّاة توثيق: إذ يصف تقرير ACAPS (ديسمبر 2023) اشتراط المَحرم، الذي يُلزم النساء بالسفر برفقة قريب "
    "ذكر، المطبَّق منذ مطلع 2022 في المناطق الخاضعة لسلطات الأمر الواقع. ولا يذكر التقرير الخدمات المالية، فهو يدعم سؤالًا "
    "للاختبار لا نتيجة.")

# ================================================================================================ U11: CWR-001
YEM25_LOC = ("Yemen Economic Monitor, Spring 2025 (29 May 2025), Box 3.1 'Impacts of FTO Designation on Yemen's Economy', "
             "printed p.19 (PDF p.31): \"Remittances, accounting for 38.6 percent of GDP in 2024, may also be affected.\" "
             "The sentence names no remittance value, source or area; read 10 October 2026 (Arabic edition, June 2025, "
             "printed p.27: «التي كانت تشكل 38.6% من إجمالي الناتج المحلي في عام 2024»)")
YEM26_LOC = ("Yemen Economic Monitor, Spring 2026 (19 May 2026), Outlook and Risks, printed p.15 (PDF p.27): \"As the primary "
             "source of household income, accounting for around one quarter of GDP\"; no year, source or area stated; "
             "read 10 October 2026")
CLM043_LIM = (
    "no established decomposition shows the residual to be unrecorded capital.",
    " Ratios to GDP move with their basis too: the World Bank's Yemen Economic Monitor put remittances at 38.6% of GDP in "
    "2024 in its Spring 2025 edition, and at “around one quarter of GDP”, with no year, in Spring 2026; between the two "
    "editions its estimate of 2024 GDP rose from USD 17,580 million to USD 19,046 million. Neither edition states, beside "
    "its ratio, the remittance value or area it rests on, and the 2026 edition does not relate its statement to the "
    "earlier figure.",
    "ولا يوجد تفكيك مثبت يبين أن المتبقي رأسُ مال غير مسجل.",
    " وتتغير النسب إلى الناتج المحلي الإجمالي بتغير أساسها أيضًا: فقد قدّر المرصد الاقتصادي لليمن الصادر عن البنك الدولي "
    "الحوالات بنسبة 38.6% من الناتج المحلي الإجمالي في 2024 في إصدار ربيع 2025، وبنحو «ربع الناتج المحلي الإجمالي»، من دون "
    "ذكر سنة، في إصدار ربيع 2026؛ وبين الإصدارين ارتفع تقديره للناتج المحلي الإجمالي لعام 2024 من 17,580 مليون دولار إلى "
    "19,046 مليون دولار. ولا يذكر أيٌّ من الإصدارين، بجانب نسبته، قيمة الحوالات أو النطاق الجغرافي الذي تستند إليه، ولا يربط "
    "إصدار 2026 تصريحه بالرقم السابق.")
CLM043_VS = [vs("38.6%", YEM25, YEM25_LOC), vs("around one quarter of GDP", YEM26, YEM26_LOC),
             vs("17,580", YEM25, "Yemen Economic Monitor, Spring 2025, Table 1.1, printed p.16 (PDF p.28), 'GDP nominal in "
                                 "US$ (millions)', 2024 = 17,580; read 10 October 2026"),
             vs("19,046", YEM26, "Yemen Economic Monitor, Spring 2026, Table 1.1 (continued), printed p.10 (PDF p.22), 'GDP "
                                 "nominal in USD (millions)', 2024 = 19,046; read 10 October 2026")]
SAME_YEAR = "/readings/same-year-different-number/"
SAME_S3 = (
    "The publication vintage has to travel with the reference year.",
    "The publication vintage has to travel with the reference year.\n"
    "The same holds for ratios to output. The World Bank's Yemen Economic Monitor put remittances at 38.6% of GDP in 2024 "
    "in its Spring 2025 edition, and at “around one quarter of GDP”, with no year, in Spring 2026; between the two "
    "editions its estimate of 2024 GDP rose from USD 17,580 million to USD 19,046 million. Neither edition states, beside "
    "its ratio, the remittance value or area it rests on, and the 2026 edition does not relate its statement to the "
    "earlier figure, so the two are not read as a fall.",
    "إذ ينبغي أن ترافق نسخةُ النشر السنةَ المرجعية أينما ذُكر الرقم.",
    "إذ ينبغي أن ترافق نسخةُ النشر السنةَ المرجعية أينما ذُكر الرقم.\n"
    "ويصدق ذلك على النسب إلى الناتج أيضًا. فقد قدّر المرصد الاقتصادي لليمن الصادر عن البنك الدولي الحوالات بنسبة 38.6% من "
    "الناتج المحلي الإجمالي في 2024 في إصدار ربيع 2025، وبنحو «ربع الناتج المحلي الإجمالي»، من دون ذكر سنة، في إصدار ربيع "
    "2026؛ وبين الإصدارين ارتفع تقديره للناتج المحلي الإجمالي لعام 2024 من 17,580 مليون دولار إلى 19,046 مليون دولار. ولا "
    "يذكر أيٌّ من الإصدارين، بجانب نسبته، قيمة الحوالات أو النطاق الجغرافي الذي تستند إليه، ولا يربط إصدار 2026 تصريحه "
    "بالرقم السابق، لذلك لا تُقرأ النسبتان على أنهما انخفاض.")

# ================================================================================================ U13, U14: MA-001, MA-009
MA001_ADD = (
    " Adding a finance module to an existing survey is one route to such a baseline. The Multiple Indicator Cluster Survey "
    "(MICS) 2022–2023 of the Central Statistical Organization and UNICEF was designed for all 22 governorates (41 "
    "enumeration areas could not be visited) and asks one household question on finance, whether any member has a bank "
    "account, which its findings report does not tabulate. The World Bank's mobile phone survey of August–September 2022 "
    "interviewed 1,297 adults aged 18 and over with mobile phones and records each respondent's area of control, the "
    "internationally recognized government or the de facto authorities.",
    " ومن طرق بناء خط الأساس هذا إضافة وحدة عن الخدمات المالية إلى مسح قائم. فقد صُمّم المسح العنقودي متعدد المؤشرات "
    "(MICS) 2022–2023 للجهاز المركزي للإحصاء واليونيسف ليشمل المحافظات الـ22 كلها (وتعذرت زيارة 41 منطقة عدّ)، ويطرح على "
    "الأسرة سؤالًا واحدًا عن الخدمات المالية، هو ما إذا كان أي فرد فيها يملك حسابًا مصرفيًا، ولا يعرض تقرير نتائجه جدولًا له. "
    "وأجرى مسح الهاتف المحمول الذي نفذه البنك الدولي في أغسطس–سبتمبر 2022 مقابلات مع 1,297 بالغًا بعمر 18 سنة فأكثر ممن "
    "يملكون هواتف محمولة، ويسجل منطقة السيطرة لكل مستجيب: الحكومة المعترف بها دوليًا أو سلطات الأمر الواقع.")
MA009_ADD = (
    " An existing instrument records respondents in both areas of control: the World Bank's mobile phone survey of "
    "August–September 2022 records each respondent's area of control and asks respondents to rank their three most "
    "important sources of income; a later round could add questions on how transfers are received and used.",
    " وتوجد أداة قائمة تسجل مستجيبين في منطقتي السيطرة كلتيهما: إذ يسجل مسح الهاتف المحمول الذي أجراه البنك الدولي في "
    "أغسطس–سبتمبر 2022 منطقة السيطرة لكل مستجيب، ويطلب من المستجيبين ترتيب أهم ثلاثة مصادر لدخلهم؛ ويمكن أن تضيف جولة لاحقة "
    "أسئلة عن طريقة استلام التحويلات واستخدامها.")


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


# ================================================================================================ helpers
def edit(t, rec, field, old, new, finding):
    """Replace `old` (found exactly once) in a governed cell: by `new` when `new` starts with `old` or is a rewrite, or
    append `new` after `old` when `new` is an addition (starts with a space)."""
    cur = t.get(rec, field)
    if not isinstance(cur, str) or cur.count(old) != 1:
        raise TxError(f"{finding} {t.sheet} {rec}.{field}: {old[:60]!r} occurs "
                      f"{0 if not isinstance(cur, str) else cur.count(old)} times")
    rep = old + new if new.startswith(" ") and not new.startswith(old) else new
    t.set(finding, rec, field, cur.replace(old, rep), cur)


def append(t, rec, field, add, finding):
    cur = t.get(rec, field)
    if not isinstance(cur, str) or add.strip()[:40] in cur:
        raise TxError(f"{finding} {t.sheet} {rec}.{field}: not the text expected, or already extended")
    t.set(finding, rec, field, cur.rstrip() + add, cur)


def vs_add(t, rec, finding, entries):
    cur = t.get(rec, "value_states")
    states = json.loads(cur) if cur else []
    have = {(e.get("t"), e.get("k")) for e in states}
    states += [e for e in entries if (e["t"], e["k"]) not in have]
    t.set(finding, rec, "value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")), cur)


def deps_add(t, rec, finding, add):
    cur = t.get(rec, "source_dependencies")
    parts = [p.strip() for p in str(cur or "").split(";") if p.strip()]
    t.set(finding, rec, "source_dependencies", "; ".join(parts + [a for a in add if a not in parts]), cur)


def sections(s, finding, route, order, pairs):
    """pairs: en_old, en_new, …, ar_old, ar_new, … (each new replaces its old in the section body)."""
    half = len(pairs) // 2
    for lang, chunk in (("en", pairs[:half]), ("ar", pairs[half:])):
        for i in range(0, len(chunk), 2):
            s.replace_section(finding, route, order, lang, "body", chunk[i], chunk[i + 1])


def caveat_plus(cur, add):
    return (str(cur).rstrip() + " " + add) if cur not in (None, "") else add


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    t07 = Table(s, "07_PUBLIC_CLAIMS")
    t11 = Table(s, "11_VISUAL_LIBRARY")
    t02 = Table(s, "02_SITE_MAP")
    t10 = Table(s, "10_MEASUREMENT_AGENDA")
    t19 = Table(s, "19_PAYMENTS_DATA")

    # ======================================================== U2 / CR-06: the H1-2025 accounts count is printed
    f2 = F + ":CR-06"
    cur = t19.get("OBS-00037", "caveats")
    if "require methodology note before public use" not in str(cur):
        raise TxError(f"{f2}: OBS-00037 is not the withheld row expected")
    t19.set(f2, "OBS-00037", "caveats", OBS37_CAVEAT, cur)
    t19.set(f2, "OBS-00037", "source_locator", OBS37_LOCATOR, "page 1; lines 2-86")
    cur = t19.get("OBS-00036", "caveats")
    if "require methodology note before public use" not in str(cur):
        raise TxError(f"{f2}: OBS-00036 is not the withheld row expected")
    t19.set(f2, "OBS-00036", "caveats", cur + OBS36_ADD, cur)

    # ======================================================== U6: the third-quarter 2024 bulletin, its own panel
    f6 = F + ":U6"
    n = 0
    for rid in list(t19.rows):
        if t19.get(rid, "source_id") != PAY_Q3:
            continue
        cur = t19.get(rid, "source_locator")
        m = re.fullmatch(r"page (\d); lines (\d+-\d+)", str(cur))
        if not m:
            raise TxError(f"{f6}: {rid} locator {cur!r} is not the page/lines form expected")
        k = int(m.group(1))
        t19.set(f6, rid, "source_locator", f"PDF p.{k + 1} (printed p.{k - 2}) of the third-quarter 2024 bulletin; page "
                                           f"corrected 10 October 2026 (close-out U6), previously recorded as {cur!r}", cur)
        n += 1
    if n != 30:
        raise TxError(f"{f6}: {n} rows of the third-quarter 2024 bulletin, expected 30")
    for rid, note in Q3_SHOWN.items():
        cur = t19.get(rid, "caveats")
        base = cur
        if rid == "OBS-00009":
            if cur != OBS09_CAVEAT_OLD:
                raise TxError(f"{f6}: OBS-00009 caveat is not the visual-QA note expected")
            base = OBS09_CAVEAT_NEW
        t19.set(f6, rid, "caveats", caveat_plus(base, note + Q3_SHOWN_TAIL), cur)
    held = list(HELD.items()) + [HELD_SUBSCRIBERS]
    for rows, reason in held:
        for rid in rows:
            cur = t19.get(rid, "caveats")
            t19.set(f6, rid, "caveats", caveat_plus(cur, reason), cur)
    insert_ui_rows(s, f6, PAY_UI)
    for field, new in ANATOMY.items():
        t06.set(f6, "VIS-PAYMENT-ANATOMY", field, new, t06.get("VIS-PAYMENT-ANATOMY", field))
    for field, new in ANATOMY_11.items():
        t11.set(f6, "VIS-PAYMENT-ANATOMY", field, new, t11.get("VIS-PAYMENT-ANATOMY", field))
    for f11, f06 in ANATOMY_11_MIRROR.items():
        t11.set(f6, "VIS-PAYMENT-ANATOMY", f11, ANATOMY[f06], t11.get("VIS-PAYMENT-ANATOMY", f11))
    route = "/evidence/VIS-PAYMENT-ANATOMY/"
    t02.set(f6, route, "meta_description_en", ANATOMY_META[1], ANATOMY_META[0])
    t02.set(f6, route, "meta_description_ar", ANATOMY_META[3], ANATOMY_META[2])
    c = json.load(open(CONTRACT, encoding="utf-8"), object_pairs_hook=OrderedDict)
    v = next(x for x in c["visuals"] if x["visual_id"] == "VIS-PAYMENT-ANATOMY")
    k = v["contract"]
    if [x["id"] for x in k["series"]] != ["h1_objects"] or k.get("frame_labels") != ["UI-VIS-NOTE-NOT-COMPARABLE-2024Q3"]:
        raise TxError(f"{f6}: VIS-PAYMENT-ANATOMY contract is not the one-panel contract expected")
    s1 = json.loads(json.dumps(k["series"][0]), object_pairs_hook=OrderedDict)
    s1["id"] = "q3_2024_channels"
    s1["rows"]["ids"] = list(Q3_SERIES_IDS)
    k["series"].append(s1)
    k["frame_labels"] = ["UI-VIS-NOTE-NOT-COMPARABLE-2024Q3"] + PANEL_LABELS
    for key, text in CONTRACT_TEXT.items():
        if key not in k:
            raise TxError(f"{f6}: contract has no {key}")
        k[key] = text
    v["rationale"] = CONTRACT_RATIONALE
    ns = c["display_labels"]["namespaces"]
    for name, mapping in (("payment_object", PAY_OBJECT), ("payment_object_not", PAY_NOT), ("unit", PAY_UNIT)):
        for key, uid in mapping.items():
            if ns[name].get(key) not in (None, uid):
                raise TxError(f"{f6}: namespace {name} already maps {key} to {ns[name][key]}")
            ns[name][key] = uid
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    # ======================================================== sources (U3, U8, U9, U10, U11, U12, U13, U14)
    fs = F + ":SOURCES"
    t15 = Table(s, "15_SOURCE_LIBRARY")
    for sid, fields in CCY_PROMOTE.items():
        if t15.get(sid, "public_card_state") != "LOCATOR_ONLY" or t15.get(sid, "primary_url"):
            raise TxError(f"{fs}: {sid} is not the locator-only record expected")
        for field, new in list(fields.items()) + list(CCY_COMMON.items()):
            t15.set(fs, sid, field, new, t15.get(sid, field))
    cur = t15.get(FMIIP, "additional_urls")
    urls = json.loads(cur) if cur else []
    if FMIIP_PAD in urls:
        raise TxError(f"{fs}: the FMIIP PAD locator is already held")
    t15.set(fs, FMIIP, "additional_urls", json.dumps(urls + [FMIIP_PAD]), cur)
    if t15.get(CNL, "additional_urls"):
        raise TxError(f"{fs}: {CNL} already has additional locators")
    t15.set(fs, CNL, "additional_urls", json.dumps(CNL_URLS), None)
    held_urls = {str(x) for r in s.grid("15_SOURCE_LIBRARY")[4:] if r for x in r[1:3] if x}
    head = t15.head
    for row in NEW_SOURCES:
        if row["source_id"] in t15.rows or row["primary_url"] in held_urls:
            raise TxError(f"{fs}: {row['source_id']} or its locator is already in the library")
    last = max(t15.rows.values())
    s.ed.insert_rows("15_SOURCE_LIBRARY", last + 1,
                     [{head.index(key) + 1: val for key, val in row.items() if val is not None} for row in NEW_SOURCES])
    for i, row in enumerate(NEW_SOURCES):
        for key, val in row.items():
            if val is not None:
                s.ledger.append(OrderedDict([("finding", fs), ("sheet", "15_SOURCE_LIBRARY"), ("row", last + 1 + i),
                                             ("col", head.index(key) + 1), ("field", f"{row['source_id']}.{key}"),
                                             ("old", None), ("new", val)]))

    # ======================================================== U3, U12: CLM-045 and CWR-010
    f3 = F + ":U3-U12"
    edit(t06, "CLM-045", "limitations_en", CLM045_LIM[0], CLM045_LIM[1], f3)
    edit(t06, "CLM-045", "limitations_ar", CLM045_LIM[2], CLM045_LIM[3], f3)
    edit(t06, "CLM-045", "currentness_en", CLM045_CUR[0], CLM045_CUR[1], f3)
    edit(t06, "CLM-045", "currentness_ar", CLM045_CUR[2], CLM045_CUR[3], f3)
    deps_add(t06, "CLM-045", f3, CLM045_DEPS_ADD)
    vs_add(t06, "CLM-045", f3, CLM045_VS)
    sections(s, f3, "/readings/after-transfer-persistence/", 6, CWR010_S6)
    t08 = Table(s, "08_READINGS", 4)
    t08.set(f3, "CWR-010", "evidence_period_en", CWR010_PERIOD[1], CWR010_PERIOD[0])
    t08.set(f3, "CWR-010", "evidence_period_ar", CWR010_PERIOD[3], CWR010_PERIOD[2])

    # ======================================================== U8: MA-005
    f8 = F + ":U8"
    append(t10, "MA-005", "current_evidence_en", MA005_ADD[0], f8)
    append(t10, "MA-005", "current_evidence_ar", MA005_ADD[1], f8)

    # ======================================================== U9: FMIIP PAD (FPS design, firms 2018, banks, exchangers)
    f9 = F + ":U9"
    edit(t06, "CLM-018", "limitations_en", CLM018_LIM[0], CLM018_LIM[1], f9)
    edit(t06, "CLM-018", "limitations_ar", CLM018_LIM[2], CLM018_LIM[3], f9)
    vs_add(t06, "CLM-018", f9, CLM018_VS)
    sections(s, f9, "/payments/", 7, PAY_S7)
    edit(t06, "CLM-062", "limitations_en", CLM062_LIM[0], CLM062_LIM[1], f9)
    edit(t06, "CLM-062", "limitations_ar", CLM062_LIM[2], CLM062_LIM[3], f9)
    deps_add(t06, "CLM-062", f9, [FMIIP])
    vs_add(t06, "CLM-062", f9, CLM062_VS)
    sections(s, f9, "/firms/", 6, FIRMS_S6)
    edit(t06, "CLM-008", "limitations_en", CLM008_LIM[0], CLM008_LIM[1], f9)
    edit(t06, "CLM-008", "limitations_ar", CLM008_LIM[2], CLM008_LIM[3], f9)
    deps_add(t06, "CLM-008", f9, [FMIIP, IGC])
    vs_add(t06, "CLM-008", f9, CLM008_VS)
    sections(s, f9, "/providers/", 3, PROV_S3)
    edit(t06, "CLM-016", "limitations_en", CLM016_LIM[0], CLM016_LIM[1], f9)
    edit(t06, "CLM-016", "limitations_ar", CLM016_LIM[2], CLM016_LIM[3], f9)
    deps_add(t06, "CLM-016", f9, [FMIIP, IGC])
    vs_add(t06, "CLM-016", f9, CLM016_VS)
    t06.set(f9, "CLM-016", "public_routes", "/evidence/compare/ | /providers/", "/providers/")
    t07.set(f9, "CLM-016", "public_routes", '["/evidence/compare","/providers"]', '["/providers"]')
    sections(s, f9, "/providers/", 10, PROV_S10)

    # ======================================================== U6, U10: women's evidence (CLM-002, CLM-027, CWR-007)
    f10 = F + ":U10"
    # CLM-027 (bound to CWR-007) carries the FSD statement and the women's service shares; CLM-002, the gap itself, is
    # not edited, so the search answer for "account ownership" keeps its order (P2-G01)
    edit(t06, "CLM-027", "limitations_en", CLM027_LIM[0], CLM027_LIM[1] + WOMEN_SHARES[0], f10)
    edit(t06, "CLM-027", "limitations_ar", CLM027_LIM[2], CLM027_LIM[3] + WOMEN_SHARES[1], f10)
    deps_add(t06, "CLM-027", f10, [FSD] + WOMEN_DEPS)
    vs_add(t06, "CLM-027", f10, CLM027_VS + WOMEN_VS)
    row = register_rows()["AR-004"]
    final_ar = row["new_ar"]
    for old, new in AR004_COND:
        if final_ar.count(old) != 1:
            raise TxError(f"{f10}: AR-004 new_ar does not hold {old[:50]!r} once")
        final_ar = final_ar.replace(old, new)
    apply_register_ar(s, f10, row, new_ar=unicodedata.normalize("NFC", final_ar))   # R85-G04: canonical order, same text
    en_row = s.section_row(GENDER, 2, "en")
    final_en = s.ed.get_value(S03, en_row, COL03["body_en"])
    for old, new in AR004_EN:
        if final_en.count(old) != 1:
            raise TxError(f"{f10}: the English of {GENDER} s2 does not hold {old[:50]!r} once")
        final_en = final_en.replace(old, new)
    apply_register_en(s, f10, row, final_en, must_start="In the latest Global Findex wave for Yemen")
    sections(s, f10, GENDER, 3, GENDER_S3)

    # ======================================================== U11: CWR-001 (a ratio to GDP, same year, different basis)
    f11 = F + ":U11"
    edit(t06, "CLM-043", "limitations_en", CLM043_LIM[0], CLM043_LIM[1], f11)
    edit(t06, "CLM-043", "limitations_ar", CLM043_LIM[2], CLM043_LIM[3], f11)
    deps_add(t06, "CLM-043", f11, [YEM25])
    vs_add(t06, "CLM-043", f11, CLM043_VS)
    sections(s, f11, SAME_YEAR, 3, SAME_S3)

    # ======================================================== U13, U14: MA-001, MA-009
    f13 = F + ":U13-U14"
    append(t10, "MA-001", "current_evidence_en", MA001_ADD[0], f13)
    append(t10, "MA-001", "current_evidence_ar", MA001_ADD[1], f13)
    append(t10, "MA-009", "current_evidence_en", MA009_ADD[0], f13)
    append(t10, "MA-009", "current_evidence_ar", MA009_ADD[1], f13)

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "CR-06/U2 (the H1-2025 accounts count printed in VIS-PAYMENT-ANATOMY; 58,512 POS transactions stay "
                    "held), U6 (the 2024 Q3 bulletin as a second panel; page locators corrected; a reason on every row "
                    "kept back), U3 (three CCY reports public; CWR-010), U8 (MA-005: IMF FAS 2015), U9 (FMIIP PAD: FPS "
                    "design, 2018 firm survey, 19 operating banks, exchanger pair on /evidence/compare/), U10 (women's "
                    "evidence concordance), U11 (38.6% vs one quarter of GDP), U12 (no UCT cycle since January 2025), "
                    "U13/U14 (MICS and the 2022 phone survey in MA-001/MA-009)"),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
