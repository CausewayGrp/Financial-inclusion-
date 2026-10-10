# -*- coding: utf-8 -*-
"""Legacy-audit follow-through, transaction LA-C: a new system Reading, CWR-011 "Where bank balance sheets sit".

  python3 la_c_cwr011.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner brief "Legacy-audit follow-through" of 10 October 2026, transaction C, approved subject to three conditions, with
the owner's corrections of the same day:
 1. Perimeter stated from the source: CBY-Aden, "Monetary and Financial Developments", Issue No. 54 (May 2026), Appendix,
    printed p. 20: "Banks: All commercial and Islamic financial institutions operating in the Republic of Yemen that
    accept deposits." Territory: the bulletin does not state which parts of Yemen its figures cover (written so).
 2. Every number bound: a new record, CBY-BANKS-2026-05, holds the May 2026 values read in Table 4 (printed p. 15):
    government 2,145.0; private sector 1,350.4; total assets 13,362.1; foreign assets 4,448.0; reserves 2,538.8 (YER
    billion). Derived by this resource from the same table: private-sector credit 10.1% of total assets; the
    government's share of loans and advances 85.1% (December 2022, earlier basis) and 59.5% (December 2022 at
    market exchange rates). The "76% -> 61%" phrasing of the brief is not used (85.1% is the verified pre-revaluation
    share). The frozen treasury-bill legacy: PAD (Report No. PADHI00396, 22 May 2025) paragraph 7, printed p. 2.
 3. The Arabic is reviewed by an independent native economic editor before the transaction is run.
The Reading surfaces on /firms/ (/finance/ already carries its two Readings).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402

F = "LA-C:CWR-011"
RID, SLUG = "CWR-011", "where-bank-balance-sheets-sit"
OID = "CBY-BANKS-2026-05"
CBY, PAD = "SRC-CBY-001", "SRC-WB-FMIIP-P180708"
CBYLOC = ("CBY-Aden, Monetary and Financial Developments, Issue No. 54 (May 2026), Table 4 \"Consolidated Balance Sheet of "
          "Commercial & Islamic Banks - Assets\", printed p. 15 (PDF p. 16), YER billion; read 10 October 2026")
PADLOC = "PAD (Report No. PADHI00396, 22 May 2025), paragraph 7, printed p. 2"

REC = OrderedDict([
    ("object_id", OID), ("object_class", "TEMPORAL_OBSERVATION"), ("public_routes", "/finance/"),
    ("title_en", "Commercial and Islamic banks: consolidated assets at the end of May 2026"),
    ("title_ar", "البنوك التجارية والإسلامية: الأصول المجمعة في نهاية مايو 2026"),
    ("summary_en", "At the end of May 2026 the consolidated balance sheet of commercial and Islamic banks published by the Central Bank "
                   "of Yemen – Aden (CBY-Aden) shows total assets of 13,362.1 billion rials, loans and advances to government of 2,145.0 "
                   "billion, loans and advances to the private sector of 1,350.4 billion, foreign assets of 4,448.0 billion and reserves "
                   "of 2,538.8 billion; credit to the private sector is 10.1% of total assets."),
    ("summary_ar", "تُظهر الميزانية المجمعة للبنوك التجارية والإسلامية التي ينشرها البنك المركزي اليمني – عدن أصولًا إجمالية قدرها "
                   "13,362.1 مليار ريال في نهاية مايو 2026، منها قروض وسلفيات للحكومة قدرها 2,145.0 مليار، وقروض وسلفيات للقطاع الخاص "
                   "قدرها 1,350.4 مليار، وأصول خارجية قدرها 4,448.0 مليار، واحتياطيات قدرها 2,538.8 مليار؛ ويعادل الائتمان الممنوح "
                   "للقطاع الخاص 10.1% من الأصول الإجمالية."),
    ("definition_en", "Positions of the consolidated balance sheet of commercial and Islamic banks at the end of May 2026, in billion rials, "
                      "as published in the monthly bulletin Monetary and Financial Developments (Issue No. 54, Table 4). Loans and advances "
                      "to government are, in the bulletin's definition, treasury bills, treasury bonds and Islamic sukuk; the private-sector "
                      "line covers households as well as firms."),
    ("definition_ar", "مراكز الميزانية المجمعة للبنوك التجارية والإسلامية في نهاية مايو 2026، بمليارات الريالات، كما نُشرت في النشرة "
                      "الشهرية «التطورات النقدية والمالية» (العدد رقم 54، الجدول 4). والقروض والسلفيات للحكومة هي، وفق تعريف النشرة، أذون "
                      "الخزانة وسندات الخزانة والصكوك الإسلامية؛ ويشمل بند القطاع الخاص الأسر إلى جانب المنشآت."),
    ("period_en", "End of May 2026 (one monthly vintage)"), ("period_ar", "نهاية مايو 2026 (إصدار شهري واحد)"),
    ("universe_en", "The bulletin's own perimeter: all commercial and Islamic financial institutions operating in the Republic of Yemen that "
                    "accept deposits. The bulletin does not state which parts of Yemen its figures cover."),
    ("universe_ar", "نطاق النشرة نفسها: جميع المؤسسات المالية التجارية والإسلامية العاملة في الجمهورية اليمنية التي تقبل الودائع. ولا "
                    "تذكر النشرة أيَّ أجزاء من اليمن تغطيها أرقامها."),
    ("method_en", "Values read from Table 4 of the bulletin. Computed by this resource from the same table: private-sector credit as a share "
                  "of total assets (10.1%), and the government's share of loans and advances in December 2022, 85.1% on the earlier basis "
                  "and 59.5% at market exchange rates. The World Bank's appraisal document for FMIIP (May 2025) reports that before the "
                  "conflict about 45% of bank assets were held in government treasury bills, which the Central Bank of Yemen later froze."),
    ("method_ar", "قيم مقروءة من الجدول 4 في النشرة. واحتسب هذا المورد من الجدول نفسه: حصة الائتمان الممنوح للقطاع الخاص من الأصول "
                  "الإجمالية (10.1%)، وحصة الحكومة من إجمالي القروض والسلفيات في ديسمبر 2022، وهي 85.1% على الأساس السابق و59.5% بسعر "
                  "الصرف السوقي. وتذكر وثيقة تقييم مشروع FMIIP الصادرة عن البنك الدولي (مايو 2025) أن نحو 45% من أصول البنوك كان مستثمرًا "
                  "قبل النزاع في أذون الخزانة الحكومية، التي جمّدها البنك المركزي اليمني لاحقًا."),
    ("limitations_en", "One month of one table is not a trend, and shares move with the exchange rate because foreign-currency items are "
                       "valued at market rates. | The record does not show credit by currency or by sector, does not split claims on "
                       "government between frozen and other holdings, and does not establish why banks hold these assets."),
    ("limitations_ar", "شهر واحد من جدول واحد ليس اتجاهًا، والحصص تتحرك مع سعر الصرف لأن البنود المقوّمة بالعملات الأجنبية تُقيَّم بأسعار "
                       "السوق. | ولا يُظهر هذا السجل الائتمان بحسب العملة أو القطاع، ولا يفصل الحقوق على الحكومة بين الأرصدة المجمدة "
                       "وغيرها، ولا يثبت لماذا تحتفظ البنوك بهذه الأصول."),
    ("currentness_en", "The values refer to the end of May 2026, the latest month in the issue read. Later monthly issues may revise or "
                       "extend them; this record keeps the May 2026 vintage."),
    ("currentness_ar", "تشير القيم إلى نهاية مايو 2026، وهو أحدث شهر في العدد المقروء. وقد تعدّلها الأعداد الشهرية اللاحقة أو تضيف إليها؛ "
                       "ويثبّت هذا السجل قيم إصدار مايو 2026."),
])

READING = OrderedDict([
    ("reading_id", RID), ("slug", SLUG), ("route", "/readings/" + SLUG),
    ("title_en", "Where bank balance sheets sit"), ("title_ar", "أين تتركز أصول البنوك"),
    ("question_en", "Do Yemen’s banks lend to firms, or hold claims on the state and assets abroad?"),
    ("question_ar", "هل تُقرض البنوك في اليمن المنشآت، أم تحتفظ بحقوق على الدولة وأصول في الخارج؟"),
    ("thesis_en", "In May 2026 the banks’ consolidated balance sheet held more in claims on government, and far more in foreign assets, "
                  "than in credit to the private sector. That is consistent with banks holding claims on the state and assets abroad "
                  "rather than lending to firms, but it is a hypothesis: weak credit demand, frozen legacy treasury bills, exchange-rate "
                  "valuation and an unstated reporting perimeter fit the same numbers."),
    ("thesis_ar", "في مايو 2026 كانت الميزانية المجمعة للبنوك تحمل من الحقوق على الحكومة أكثر، ومن الأصول الخارجية أكثر بكثير، مما "
                  "تحمله من ائتمان للقطاع الخاص. ويتسق ذلك مع أن البنوك تحتفظ بحقوق على الدولة وأصول في الخارج بدل إقراض المنشآت، لكنه "
                  "يبقى فرضية: فضعف الطلب على الائتمان، وإرث أذون الخزانة المجمدة، وتقييم البنود بسعر الصرف، ونطاق الإبلاغ غير المعلن، "
                  "كلها تنسجم مع الأرقام نفسها."),
    ("claim_bindings", json.dumps([OID, "CLM-033"], separators=(",", ":"))),
    ("evidence_bindings", json.dumps([OID, "CLM-033"], separators=(",", ":"))),
    ("source_bindings", json.dumps([CBY, PAD])),
    ("visual_bindings", "[]"),
    ("audiences", json.dumps(["CBY", "banks/PSPs", "Government", "WB/UN"], separators=(",", ":"))),
    ("prohibited_inference_en", "One month of one balance sheet does not show why banks hold these assets, does not show that firms are refused "
                                "credit and is not a trend; a fall in the government's share across the 2022 revaluation is consistent with "
                                "valuation, not new lending."),
    ("prohibited_inference_ar", "لا يُظهر شهر واحد من ميزانية واحدة لماذا تحتفظ البنوك بهذه الأصول، ولا يثبت أن المنشآت تُحرم من الائتمان، "
                                "وليس اتجاهًا؛ وانخفاض حصة الحكومة عبر إعادة التقييم في 2022 يتسق مع أثر التقييم، لا مع إقراض جديد."),
    ("verification_bindings", json.dumps(OrderedDict([("claim_ids", [OID, "CLM-033"]), ("direct_source_ids", [CBY, PAD]),
                                                      ("dependency_ids", []),
                                                      ("resolution_rule", "Direct SRC-* identifiers resolve in the Source Library. Other dependency identifiers remain lineage/verification anchors and must never be converted into invented URLs or sources.")]),
                                          ensure_ascii=False)),
    ("domain_surface_routes", "/firms/"), ("related_readings", json.dumps(["CWR-002"])), ("measurement_bindings", "[]"),
    ("evidence_period_en", "CBY-Aden monthly bulletin, end of May 2026 (Issue No. 54) · December 2022 for the revaluation comparison"),
    ("evidence_period_ar", "النشرة الشهرية للبنك المركزي اليمني – عدن، نهاية مايو 2026 (العدد رقم 54) · ديسمبر 2022 لمقارنة إعادة التقييم"),
    ("last_reviewed", "2026-10-10"), ("featured", None),
])

SECTIONS = [  # (order, section_id, heading_en, body_en, heading_ar, body_ar)
    (2, "opening", None,
     "Where a banking system puts its assets says something about whom it serves. The monthly bulletin of the Central Bank of Yemen – "
     "Aden (CBY-Aden) for May 2026 (Issue No. 54) consolidates the balance sheet of commercial and Islamic banks — in its own words, all "
     "commercial and Islamic financial institutions operating in the Republic of Yemen that accept deposits. At the end of May 2026 "
     "their total assets were 13,362.1 billion rials. Loans and advances to government — treasury bills, treasury bonds and Islamic "
     "sukuk, in the bulletin’s definition — stood at 2,145.0 billion, loans and advances to the private sector at 1,350.4 billion, "
     "foreign assets at 4,448.0 billion and reserves at 2,538.8 billion. Credit to the private sector was 10.1% of total assets, and that "
     "line covers households as well as firms.\n"
     "The bulletin does not state which parts of Yemen its figures cover.",
     None,
     "يكشف موضع أصول المنظومة المصرفية شيئًا عمّن تخدمه. فالنشرة الشهرية للبنك المركزي اليمني – عدن لشهر مايو 2026 (العدد رقم 54) "
     "تعرض الميزانية المجمعة للبنوك التجارية والإسلامية، وهي بحسب تعريفها جميع المؤسسات المالية التجارية والإسلامية العاملة في "
     "الجمهورية اليمنية التي تقبل الودائع. وفي نهاية مايو 2026 بلغت أصولها الإجمالية 13,362.1 مليار ريال، منها قروض وسلفيات للحكومة — "
     "وهي وفق تعريف النشرة أذون الخزانة وسندات الخزانة والصكوك الإسلامية — قدرها 2,145.0 مليار، وقروض وسلفيات للقطاع الخاص قدرها "
     "1,350.4 مليار، وأصول خارجية قدرها 4,448.0 مليار، واحتياطيات قدرها 2,538.8 مليار. ويعادل الائتمان الممنوح للقطاع الخاص 10.1% من "
     "الأصول الإجمالية، ويشمل هذا البند الأسر إلى جانب المنشآت.\n"
     "ولا تذكر النشرة أيَّ أجزاء من اليمن تغطيها أرقامها."),
    (3, "hypothesis", "A hypothesis, not a finding",
     "The balance sheet is consistent with banks holding claims on the state and assets abroad rather than lending to firms: claims on "
     "government and foreign assets together are several times the credit extended to the private sector. This Reading states that as "
     "a hypothesis. A balance sheet shows where assets sit on one date. It does not show why they sit there, and it does not show what "
     "firms asked for.",
     "فرضية لا نتيجة",
     "تتسق الميزانية مع أن البنوك تحتفظ بحقوق على الدولة وأصول في الخارج بدل إقراض المنشآت: فالحقوق على الحكومة والأصول الخارجية معًا "
     "تبلغ أضعاف الائتمان الممنوح للقطاع الخاص. وتطرح هذه القراءة ذلك فرضيةً. فالميزانية تُظهر أين تقع الأصول في تاريخ واحد، لكنها لا "
     "تُظهر لماذا تقع هناك، ولا ما طلبته المنشآت."),
    (4, "alternatives", "Four other explanations fit the same numbers",
     "- Weak demand for credit. In an uncertain economy firms may not be asking for loans; a small loan book can reflect few "
     "applications as much as few approvals.\n"
     "- The frozen treasury-bill legacy. Before the conflict, about 45% of bank assets were held in government treasury bills; after "
     "the government stopped servicing its debt, the Central Bank of Yemen froze those holdings, as the World Bank’s appraisal document "
     "for FMIIP (May 2025) reports. Part of today’s claims on government may be that legacy rather than new investment decisions.\n"
     "- Valuation. Since December 2022 foreign-currency items have been valued at the market exchange rate, so the shares move with the "
     "rial’s exchange rate. Of loans and advances, the government’s share was 85.1% on the earlier basis in December 2022 and 59.5% when "
     "the same month was revalued at market exchange rates. That drop comes from restating the same month, not from new lending; it is "
     "consistent with valuation, and the bulletin does not split it between valuation and other effects, so nothing here says that "
     "lending to firms has or has not improved.\n"
     "- The reporting perimeter. The bulletin covers the deposit-taking institutions in its data, but it does not state which areas its "
     "figures cover, so the consolidated balance sheet may not describe every bank in every part of the country.",
     "أربعة تفسيرات أخرى تنسجم مع الأرقام نفسها",
     "- ضعف الطلب على الائتمان: ففي اقتصاد غير مستقر قد لا تطلب المنشآت قروضًا، وقد يعكس صِغَر محفظة القروض قلةَ الطلبات بقدر ما يعكس "
     "قلةَ الموافقات.\n"
     "- إرث أذون الخزانة المجمدة: فقبل النزاع كان نحو 45% من أصول البنوك مستثمرًا في أذون الخزانة الحكومية، وحين توقفت خدمة الدين العام "
     "جمّد البنك المركزي اليمني تلك الأرصدة، بحسب وثيقة تقييم مشروع FMIIP الصادرة عن البنك الدولي (مايو 2025). وقد يكون جزء من الحقوق "
     "الحالية على الحكومة هو ذلك الإرث، لا حصيلة قرارات استثمار جديدة.\n"
     "- التقييم: فمنذ ديسمبر 2022 تُقيَّم البنود المقوّمة بالعملات الأجنبية بسعر الصرف السوقي، فتتحرك الحصص مع سعر صرف الريال. ومن "
     "إجمالي القروض والسلفيات، بلغت حصة الحكومة 85.1% على الأساس السابق في ديسمبر 2022 و59.5% حين أُعيد تقييم الشهر نفسه بسعر الصرف "
     "السوقي. وهذا الانخفاض ناتج عن إعادة عرض الشهر نفسه لا عن إقراض جديد؛ وهو يتسق مع أثر التقييم، ولا تفصل النشرة بينه وبين الآثار "
     "الأخرى، لذلك لا تقول هذه القراءة إن إقراض المنشآت قد تحسّن أو لم يتحسّن.\n"
     "- نطاق الإبلاغ: تغطي النشرة مؤسسات قبول الودائع التي تشملها بياناتها، لكنها لا تذكر المناطق التي تغطيها أرقامها، لذلك قد لا تصف "
     "الميزانية المجمعة كل بنك في كل أنحاء البلاد."),
    (5, "boundary", "Where the evidence stops",
     "This is one month of one table. The balance sheet does not show credit by currency or by sector, does not split claims on "
     "government between frozen and other holdings, and does not state its territorial reach. It does not establish that banks prefer "
     "the state to firms, that firms are refused credit, or that any policy caused the pattern.",
     "أين يتوقف الدليل؟",
     "هذا شهر واحد من جدول واحد. فالميزانية لا تُظهر الائتمان بحسب العملة أو القطاع، ولا تفصل الحقوق على الحكومة بين الأرصدة المجمدة "
     "وغيرها، ولا تذكر نطاقها الجغرافي. ولا تثبت أن البنوك تفضّل الدولة على المنشآت، ولا أن المنشآت تُحرم من الائتمان، ولا أن سياسة "
     "بعينها أنتجت هذا النمط."),
    (6, "what_would_change", "What would change this reading?",
     "Four disclosures would test the hypothesis against its alternatives:\n"
     "- credit to the private sector by currency and by sector;\n"
     "- loan applications and approvals, to separate weak demand from limited supply;\n"
     "- a split of claims on government between frozen legacy treasury bills and other holdings;\n"
     "- a stated reporting perimeter: which banks, and which areas, the consolidated balance sheet covers.\n"
     "> Until then, read the balance sheet as a picture of where assets sit, not as an account of why.",
     "ما الذي قد يغيّر هذه القراءة؟",
     "من شأن أربعة إفصاحات أن تختبر الفرضية في مقابل بدائلها:\n"
     "- الائتمان الممنوح للقطاع الخاص بحسب العملة وبحسب القطاع؛\n"
     "- طلبات القروض والموافقات عليها، للتمييز بين ضعف الطلب ومحدودية العرض؛\n"
     "- تقسيم الحقوق على الحكومة بين أذون الخزانة المجمدة الموروثة والأرصدة الأخرى؛\n"
     "- نطاق إبلاغ معلن: أي البنوك وأي المناطق تغطيها الميزانية المجمعة.\n"
     "> وإلى أن تتوافر، تُقرأ الميزانية صورةً لموضع الأصول، لا تفسيرًا لأسبابه."),
]

VALUES = [{"t": t, "k": "v", "s": "READ", "src": CBY, "loc": CBYLOC + ", " + lab}
          for t, lab in (("13,362.1", "Total Assets, May 2026"), ("2,145.0", "Government, May 2026"), ("1,350.4", "Private Sector, May 2026"),
                         ("4,448.0", "Foreign Assets, May 2026"), ("2,538.8", "Reserves, May 2026"))] + [
    {"t": "10.1%", "k": "v", "s": "DERIVED", "src": CBY, "loc": CBYLOC + "; computed 1,350.4 / 13,362.1 = 10.11%"},
    {"t": "85.1%", "k": "v", "s": "DERIVED", "src": CBY, "loc": CBYLOC + "; Dec 2022 (earlier basis), Loans & Advances: Government / Loans & Advances = 1,926.8 / 2,264.8 = 85.08%"},
    {"t": "59.5%", "k": "v", "s": "DERIVED", "src": CBY, "loc": CBYLOC + "; Dec *2022 (*Based on market exchange rates): 1,913.2 / 3,214.8 = 59.51%"},
    {"t": "45%", "k": "v", "s": "READ", "src": PAD, "loc": PADLOC + ": \"around 45 percent of assets invested in government treasury bills (T-bills)\"; read 10 October 2026"},
    {"t": "54", "k": "v", "s": "TRIVIAL"}, {"t": "4", "k": "v", "s": "TRIVIAL"},
    {"t": "May 2026", "k": "d", "s": "READ", "src": CBY, "loc": CBYLOC},
    {"t": "December 2022", "k": "d", "s": "READ", "src": CBY, "loc": CBYLOC},
    {"t": "May 2025", "k": "d", "s": "READ", "src": PAD, "loc": "PAD (Report No. PADHI00396), dated 22 May 2025"},
    {"t": "10 October 2026", "k": "d", "s": "SITE"}]   # the Reading's last-reviewed date, printed on its page


def append_row(s, sheet, header_row, values: OrderedDict):
    g = s.grid(sheet)
    head = [str(x) if x is not None else None for x in g[header_row - 1]]
    row = {head.index(k) + 1: v for k, v in values.items() if v is not None}
    s.ed.insert_rows(sheet, len(g) + 1, [row])
    s.ledger.append(OrderedDict([("finding", F), ("sheet", sheet), ("row", len(g) + 1), ("col", None), ("field", next(iter(values.values()))),
                                 ("old", None), ("new", json.dumps({k: v for k, v in values.items() if v is not None}, ensure_ascii=False)[:400])]))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    if OID in t06.rows:
        raise TxError(f"{F}: 06 already has {OID}")
    std = t06.rows["FMIIP-BASELINE-2025-01"]
    rec = OrderedDict(REC)
    for f in ("change_trigger_en", "change_trigger_ar", "verification_en", "verification_ar"):
        rec[f] = t06.get("FMIIP-BASELINE-2025-01", f)
    rec["source_dependencies"] = f"{CBY}; {PAD}"
    rec["source_links"] = json.dumps([
        {"source_id": CBY, "url": "https://english.cby-ye.com/files/6a5a2e6bcc3cd.pdf", "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"},
        {"source_id": PAD, "url": "https://maps.worldbank.org/projects/wb/pid/P180708?status=active", "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}],
        separators=(",", ":"))
    rec["lineage_state"] = "BOUND_EXACT"
    rec["value_states"] = json.dumps(VALUES, ensure_ascii=False, separators=(",", ":"))
    del std
    append_row(s, "06_EVIDENCE_OBJECTS", 4, rec)
    append_row(s, "08_READINGS", 4, READING)
    g09 = s.grid("09_READING_SECTIONS")
    rows9 = [{1: RID, 2: 1, 3: "strongest_reading", 4: "What the evidence supports", 5: "ما الذي تسنده الأدلة"}]
    rows9 += [{1: RID, 2: o, 3: sid} for o, sid, *_ in SECTIONS]
    s.ed.insert_rows("09_READING_SECTIONS", len(g09) + 1, rows9)
    g03 = s.grid("03_PAGE_SECTIONS")
    rows3 = []
    for o, sid, he, be, ha, ba in SECTIONS:
        r = {1: f"/readings/{SLUG}/", 2: o, 5: be, 7: ba}
        if he:
            r[4], r[6] = he, ha
        rows3.append(r)
    s.ed.insert_rows("03_PAGE_SECTIONS", len(g03) + 1, rows3)
    g02 = s.grid("02_SITE_MAP")
    s.ed.insert_rows("02_SITE_MAP", len(g02) + 1, [
        {1: f"/readings/{SLUG}/", 2: "reading_detail", 3: "/readings/[reading_id]", 4: SLUG},
        {1: f"/evidence/{OID}/", 2: "evidence_detail", 3: "/evidence/[id]", 4: OID}])
    for what in ("09 rows", "03 rows", "02 rows"):
        s.ledger.append(OrderedDict([("finding", F), ("sheet", what), ("row", None), ("col", None), ("field", RID), ("old", None), ("new", "appended")]))
    r = s.save(out, ledger, OrderedDict([("transaction", "LA-C"),
                                         ("summary", "Legacy-audit follow-through C: Reading CWR-011 and its bound record CBY-BANKS-2026-05")]))
    print(json.dumps({k: r[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
