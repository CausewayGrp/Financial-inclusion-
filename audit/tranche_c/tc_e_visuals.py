# -*- coding: utf-8 -*-
"""Tranche C transaction TC-E — visual contracts: governed labels (04), visual forms (11) and the controlled contract.

  python3 tc_e_visuals.py master <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>
  python3 tc_e_visuals.py contract <in_contract.json> <out_contract.json>

Master part (04, 11, 25 banner) and the controlled visual-contract input
(scripts/projection/controlled_inputs/visual_design_contract.json, installed by run_stage --install).
Findings: VIS-01 (BLOCKER), VIS-02, VIS-03 (BLOCKER), VIS-07, VIS-09, VIS-10, VIS-11, VIS-12, VIS-13, VIS-14, VIS-15,
VIS-16, VIS-17, VIS-19, VIS-20, VIS-21. Lead decisions are stated beside each edit.
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

F = "TC-E"
# ---- 04 labels -----------------------------------------------------------------------------------------------
# existing labels: (ui_id, new_en, new_ar, old_en, old_ar, finding)
SET_UI = [
    ("UI-VIS-CAT-EVT-FPS", "FMIIP component: support for developing a Fast Payment System", "مكوّن في مشروع FMIIP: دعم تطوير نظام الدفع السريع",
     "Fast Payment System", "نظام الدفع السريع", "VIS-01"),
    ("UI-VIS-CAT-EVT-RTGS-CORE", "FMIIP component: support for establishing a real-time gross settlement (RTGS) system and upgrading CBY-Aden core banking",
     "مكوّن في مشروع FMIIP: دعم إنشاء نظام التسوية الإجمالية الفورية (RTGS) وتحديث النظام المصرفي الأساسي للبنك المركزي اليمني – عدن",
     "RTGS and CBY core banking", "نظام التسوية الإجمالية الفورية والنظام المصرفي الأساسي للبنك المركزي", "VIS-01"),
    ("UI-VIS-CAT-EVT-ACCESS-DB", "FMIIP component: access-point database", "مكوّن في مشروع FMIIP: قاعدة بيانات لنقاط الوصول",
     "Access-point database and usage support", "قاعدة بيانات نقاط الوصول ودعم الاستخدام", "VIS-01"),
    ("UI-VIS-CAT-EVT-QR-INTEROP",
     "CBY-Aden board decision: mandatory national QR standard, linking of e-wallets, and CBY-Aden as a main shareholder in the Fast Payment System operator company",
     "قرار مجلس إدارة البنك المركزي اليمني – عدن: معيار وطني إلزامي لرمز الاستجابة السريعة، وربط المحافظ الإلكترونية، ومساهمة البنك المركزي في عدن مساهمًا رئيسيًا في الشركة المشغلة لنظام الدفع السريع",
     None, None, "VIS-01"),
    ("UI-VIS-CAT-EVT-NETWORK-COMPANY", "Unified Money Network company: restructuring, capital increase and new bank shareholders",
     "شركة الشبكة الموحدة للأموال: إعادة الهيكلة وزيادة رأس المال وانضمام بنوك مساهمة جديدة", None, None, "VIS-01"),
    ("UI-VIS-CAT-EVT-YPCC-FOUNDING", "Founding assembly of the Yemeni Payments and Clearing Company (YPCC)",
     "الجمعية التأسيسية للشركة اليمنية للمدفوعات والمقاصة (YPCC)", None, None, "PAY-17"),
    ("UI-VIS-CAT-EVT-YPCC-BOARD", "First board meeting of the Yemeni Payments and Clearing Company (YPCC)",
     "أول اجتماع لمجلس إدارة الشركة اليمنية للمدفوعات والمقاصة (YPCC)", None, None, "PAY-17"),
    ("UI-VIS-CAT-PRV-EVENTS-NONE", "No status events held in this evidence base", "لا تتضمن قاعدة الأدلة أحداثًا لوضع هذه الفئة",
     "None", "لا يوجد", "VIS-10"),
    ("UI-VIS-CAT-PRV-EVENTS-NONE-APPLIED", "Bank status events not reviewed here", "لم تُراجَع هنا أحداث وضع البنوك",
     "No bank status events applied", "لم تُطبَّق أحداث تتعلق بوضع البنوك", "VIS-10"),
]
NEW_UI = [
    ("UI-VIS-CAT-LANE-PEOPLE-SURVEY", "People (survey)", "الأفراد (بيانات مسحية)", "Tranche C TC-E (VIS-02). Lane title, RV-CWR-004."),
    ("UI-VIS-CAT-LANE-PAYMENT-INFRA-ADMIN", "Payment infrastructure (administrative)", "بنية المدفوعات (بيانات إدارية)", "Tranche C TC-E (VIS-02). Lane title, RV-CWR-004."),
    ("UI-VIS-CAT-LANE-INSTITUTIONS-REFORMS", "Institutions and reforms", "المؤسسات والإصلاحات", "Tranche C TC-E (VIS-02). Lane title, RV-CWR-004."),
    ("UI-VIS-CAT-METRIC-ACCOUNT-OWNERSHIP", "Account ownership", "امتلاك الحساب", "Tranche C TC-E (VIS-02). Metric label: Findex account ownership (findex_metric)."),
    ("UI-VIS-NOTE-MFI-2023-SECONDARY", "Sector figure from a secondary source; provider set not verified",
     "رقم للقطاع من مصدر ثانوي؛ ولم يُتحقق من مجموعة مقدمي الخدمات التي يغطيها", "Tranche C TC-E (VIS-03). Note on the 2023 microfinance anchor."),
    ("UI-VIS-NOTE-INDEX-CONCORDANCE",
     "The two indexed paths are almost identical, and the ratio between their levels hardly changes. This closeness does not show that the two series independently confirm the trend.",
     "المساران المؤشَّران شبه متطابقين، ونسبة مستوى أحدهما إلى الآخر شبه ثابتة. ولا يبيّن هذا التقارب أن السلسلتين تؤكدان الاتجاه كلٌّ على نحو مستقل.",
     "Tranche C TC-E (VIS-13). In-frame note, RV-CWR-001 panel 2."),
    ("UI-VIS-NOTE-FINDEX-SAMPLE", "Survey estimates from 1,000 respondents; margins of error are not shown.",
     "تقديرات مسحية من 1,000 مستجيب؛ ولا تُعرض هوامش الخطأ.", "Tranche C TC-E (VIS-15). In-frame sampling note, VIS-FINDEX-GAPS."),
    ("UI-VIS-NOTE-NOT-COMPARABLE-2024Q3", "Not comparable with the 2024 Q3 bulletin", "لا يُقارن بنشرة الربع الثالث 2024",
     "Tranche C TC-E (VIS-19). Card note for flagged payment objects, VIS-PAYMENT-ANATOMY."),
]
# 11 visual forms that contradicted the contract (VIS-07, VIS-03, VIS-11, VIS-12, VIS-21)
SET_11 = [
    ("VIS-FIRM-FINANCE-PATH", "visual_form", "TABLE_TEXT_FIRST", "FUNNEL_PLUS_CONDITIONAL_COMPOSITION"),
    ("VIS-MFI-DIVERGENCE", "visual_form", "TABLE_TEXT_FIRST", "THREE_LANE_BOUNDED_ANCHOR_CHART"),
    ("VIS-MFI-DIVERGENCE", "encoding_contract",
     "Table of dated anchors: date, borrowers, savers, portfolio (YER million) and the evidence state of each value. No line, lane or shared axis joins the anchors.",
     "Do not connect unlike metrics into one line. Each lane shows only its valid source anchors; evidence tier and source break are visible. Nominal portfolio never shares an axis with people/account counts."),
    ("VIS-TARGET-RESULT-STATE", "visual_form", "TABLE_TEXT_FIRST", "TARGET_RESULT_MILESTONE_WITH_COMPATIBILITY_BADGE"),
    ("VIS-TARGET-RESULT-STATE", "encoding_contract", "Table: baseline, target and result (not held); no dated axis and no progress bar.",
     "Target and result states visually distinct; progress bar only after compatibility PASS."),
    ("VIS-EVIDENCE-CLASS-LADDER", "visual_form", "UNORDERED_CATEGORY_CARDS", "EVIDENCE_CLASS_LADDER_WITH_CLAIM_BOUNDARIES"),
    ("VIS-EVIDENCE-CLASS-LADDER", "encoding_contract", "Unordered category cards; no ranking, score or size encoding.",
     "Ordered evidence-state ladder; no numeric score/size encoding."),
]
BANNER_25 = ("Verified World Bank aggregates for Yemen. The Global Findex 2025 edition contains 2024 observations for many economies, "
             "but Yemen's latest available account-ownership observation remains 2022.")


def master(src, out, ledger, work):
    from tc_lib import Session, Table, TxError, insert_ui_rows, ui_block_end, norm
    s = Session(src, work)
    _, ui = ui_block_end(s)
    for uid, en, ar, old_en, old_ar, fnd in SET_UI:
        row = ui[uid]
        cur_en, cur_ar = s.ed.get_value("04_NAV_UX", row, 2), s.ed.get_value("04_NAV_UX", row, 3)
        if old_en is not None and (norm(cur_en) != norm(old_en) or norm(cur_ar) != norm(old_ar)):
            raise TxError(f"{uid}: holds {cur_en!r} / {cur_ar!r}")
        s.set(F + ":" + fnd, "04_NAV_UX", row, 2, en, cur_en, uid + ".label_en")
        s.set(F + ":" + fnd, "04_NAV_UX", row, 3, ar, cur_ar, uid + ".label_ar")
    insert_ui_rows(s, F + ":VIS", NEW_UI)
    t11 = Table(s, "11_VISUAL_LIBRARY")
    for vid, f, new, old in SET_11:
        t11.set(F + ":VIS-07", vid, f, new, old)
    cur = s.ed.get_value("25_FINDEX_BASELINE", 2, 1)
    if not str(cur).startswith("Verified World Bank aggregates appear first.") or "attached-workbook analytical inputs below" not in cur:
        raise TxError("25 banner not as expected")
    s.set(F + ":VER-01", "25_FINDEX_BASELINE", 2, 1, BANNER_25, cur, "25.banner")
    rep = s.save(out, ledger, {"transaction": "TC-E", "summary": "04 visual labels (9 set, 8 new); 11 forms (4 visuals); 25 banner"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


def _v(c, vid):
    return next(x for x in c["visuals"] if x["visual_id"] == vid)


def contract(src, out):
    raw = open(src, encoding="utf-8").read()
    c = json.loads(raw, object_pairs_hook=OrderedDict)
    note = OrderedDict()
    # VIS-16 / VIS-20: global rules
    c["global_rules"]["axes"] = ("Bar and dot value axes start at zero. A line chart may use a non-zero value axis only with the axis "
                                 "origin labelled. Never draw two value axes on one plot. Never encode a value as area, bubble or icon size.")
    c["global_rules"]["rtl"] = c["global_rules"]["rtl"].replace(
        "IDs, currency codes and signed percentages are isolated as left-to-right runs.",
        "IDs, currency codes, signed percentages and index-base or equation expressions (such as 2021 = 100) are isolated as "
        "left-to-right runs. Horizontal numeric value axes run left to right in both languages.")
    ns = c["display_labels"]["namespaces"]
    ns["findex_metric"] = OrderedDict([("Account ownership at a financial institution or with a mobile-money-service provider", "UI-VIS-CAT-METRIC-ACCOUNT-OWNERSHIP"),
                                       ("Account ownership", "UI-VIS-CAT-METRIC-ACCOUNT-OWNERSHIP")])
    # VIS-01 / VIS-02: RV-CWR-009
    v = _v(c, "RV-CWR-009")
    k = v["contract"]
    k["form"] = ("Chain, top to bottom, for the payment-architecture reform as a whole; each step EVIDENCED or OPEN (grammar chain). "
                 "Events are placed by chain step, not by rail: the governed event rows carry no rail field.")
    k["step_mapping"]["UI-VIS-CHAIN-RULE"] = ("NETWORK_RULE and PAYMENTS_ARCHITECTURE_DECISION events, and the funded project steps "
                                               "PROJECT_START, PAYMENT_RAIL_COMPONENT and ACCESS_USAGE_COMPONENT (a project component is a programme, not implementation)")
    k["step_mapping"]["UI-VIS-CHAIN-IMPLEMENTATION"] = "NETWORK_INTEGRATION, UNIFIED_NETWORK_COMPANY and YPCC events, and the POS terminal stock (OBS-00080)"
    k["step_mapping"]["UI-VIS-CHAIN-OPERATION"] = "POS transactions (OBS-00081) and NETWORK_ACTIVITY_SIGNAL; activity counts evidence operation, not use"
    pa = next(o for o in k["objects"] if o["id"] == "pos_activity")
    pa["fields"]["label"] = "indicator_id"
    pa["label_fields"] = OrderedDict([("label", "payment_object"), ("unit", "unit")])
    k["annotation"] = "Each EVIDENCED step shows its dated event(s); the POS values print their governed object label (POS terminals, POS transactions) and unit for the latest month."
    # VIS-02 / VIS-14 / VIS-17: RV-CWR-004
    v = _v(c, "RV-CWR-004")
    k = v["contract"]
    people = next(x for x in k["series"] if x["id"] == "people")
    people["fields"]["group"] = "group"
    people["fields"]["series_label"] = "indicator"
    people["label_fields"] = OrderedDict([("group", "findex_group"), ("series_label", "findex_metric"), ("unit", "unit")])
    infra = next(x for x in k["series"] if x["id"] == "infrastructure")
    infra["fields"]["label"] = "indicator_id"
    infra["label_fields"] = OrderedDict([("label", "payment_object"), ("unit", "unit")])
    k["transformation"] = ("Lanes never share a value axis. Every lane, including infrastructure, is plotted as dated presence (monthly ticks "
                           "for the infrastructure lane), not magnitude; only the first and the latest infrastructure values are labelled, with "
                           "their governed object label. No lane has a value axis.")
    k["annotation"] = (k["annotation"] + " Lane titles are the three governed frame labels, in lane order (people, infrastructure, institutions and reforms).")
    k["frame_labels"] = ["UI-VIS-CAT-LANE-PEOPLE-SURVEY", "UI-VIS-CAT-LANE-PAYMENT-INFRA-ADMIN", "UI-VIS-CAT-LANE-INSTITUTIONS-REFORMS"]
    k["credit"]["source_ids"] = ["SRC-WB-FMIIP-P180708"]
    # VIS-13 / VIS-17: RV-CWR-001
    v = _v(c, "RV-CWR-001")
    k = v["contract"]
    k["form"] = ("Panel 1: two markers at reference year 2024, keyed by publication vintage (SAME_YEAR_REVISION). Panel 2: the CBY AR2025 "
                 "vintage and the IMF 2025 Article IV staff report, each indexed to its own 2021 value (2021 = 100), drawn as two side-by-side "
                 "small panels with their own indexed axes, one per source; the paths are never drawn on one axis, merged, joined or shown as "
                 "one harmonised series. The in-frame note states that their near-identity is not independent confirmation.")
    k["mobile"] = "Panel 1: two stacked labelled dots with the vintage label beside each value. Panel 2 below it: the two small panels stacked, each with its own indexed axis and source label."
    k["frame_labels"] = ["UI-VIS-NOTE-INDEX-CONCORDANCE"]
    k["credit"]["source_ids"] = ["SRC-CBY-AR2024-BOP", "SRC-CBY-AR2025-BOP", "SRC-IMF-AIV-2025-STAFF-001"]
    k["credit"]["passport_ids"] = ["EP-REMITTANCE-MACRO", "EP-CBY-REMITTANCE-VINTAGE-K04"]
    # VIS-10 / VIS-17: provider matrix
    v = _v(c, "VIS-PROVIDER-OBSERVABILITY")
    k = v["contract"]
    k["ordering"] = "Rows: banks, exchange and remittance actors, wallets and e-money, microfinance (non-bank), payment-system operators (UNKNOWN). Columns in the order above."
    k["annotation"] = ("UI-VIS-ISSUER-SCOPE in frame for the rows whose authority is Central Bank of Yemen — Aden (authority field of the "
                       "status and negative-authority rows); the microfinance row's source is the Yemen Microfinance Network's membership pages.")
    k["credit"]["source_ids"] = ["SRC-YMN-MEMBERS-2026-001"]
    # VIS-17: remittance cost
    v = _v(c, "VIS-REMITTANCE-COST")
    v["contract"]["credit"]["source_ids"] = ["SRC-WB-RPW-SA-YEM-2025Q3-001", "SRC-WB-RPW-UAE-YEM-2025Q3-001"]
    # VIS-19: payment anatomy
    v = _v(c, "VIS-PAYMENT-ANATOMY")
    k = v["contract"]
    s0 = k["series"][0]
    s0["flag_markers"]["BREAK_IN_SERIES"] = "NOT_COMPARABLE"
    k["ordering"] = "Series order: cards, ATMs, e-wallets, e-wallet subscribers, POS terminals, POS transactions, accounts."
    k["breaks"] = "Flagged objects carry NOT_COMPARABLE and the card note UI-VIS-NOTE-NOT-COMPARABLE-2024Q3: no comparison with the 2024 Q3 bulletin is drawn. Cards have no line, so no line-break marker is printed."
    k["frame_labels"] = ["UI-VIS-NOTE-NOT-COMPARABLE-2024Q3"]
    # VIS-15: Findex sampling note
    v = _v(c, "VIS-FINDEX-GAPS")
    v["contract"]["frame_labels"] = ["UI-VIS-NOTE-FINDEX-SAMPLE"]
    v["contract"]["annotation"] = v["contract"]["annotation"] + " The governed sampling note (frame_labels) is printed in frame."
    # VIS-03 / VIS-11 / VIS-12: re-tier to TABLE_TEXT_FIRST (the honest form is a table)
    for vid, rat, prom in (
        ("VIS-MFI-DIVERGENCE",
         "Borrowers, savers and nominal portfolio at three dated anchors (21_MFI_DATA spine rows SRC-SFD-Q4-2015-001, SRC-SFD-Q4-2020-001, "
         "SRC-SANAA-MFB-2024) are not comparable enough to draw: saver definitions differ, the rial valuation of the portfolio figures is not "
         "recorded, and the 2023 anchor is a secondary sector figure whose provider set is not verified (UI-VIS-NOTE-MFI-2023-SECONDARY). "
         "Rendered as a table: date, borrowers, savers, portfolio (YER million) and the evidence state of each value. RV-CWR-006 uses the same table.",
         "A governed saver-definition crosswalk and a governed rial-valuation field on each portfolio anchor (Master-first)."),
        ("VIS-FIRM-FINANCE-PATH",
         "The 31 firms with a line of credit out of 328 (FFO-2022-004) and the 18 valid loan-source responses (FFO-2022-LS-01..04) are "
         "rendered as a table (stage, count, base). Two stages drawn in sequence would read as a funnel, which requires the 18 responses to "
         "come from the 31 firms; the Master does not establish that.",
         "The Master states whether the 18 loan-source responses are a subset of the 31 firms with a line of credit."),
        ("VIS-TARGET-RESULT-STATE",
         "The FMIIP access-point baseline and target (FMIIP-RF-004) and the result, which is not held, are rendered as a three-row table "
         "(state, date, value). Two markers on a dated axis would invite a trajectory that no observation supports.",
         "An observed result for the same indicator under the project's own definition (FMIIP-RF-004), Master-first."),
    ):
        v = _v(c, vid)
        v.clear()
        v.update(OrderedDict([("visual_id", vid), ("tier", "TABLE_TEXT_FIRST"), ("rationale", rat), ("promotion_requires", prom)]))
    _v(c, "RV-CWR-006")["rationale"] = "Uses the VIS-MFI-DIVERGENCE table of dated anchors (TABLE_TEXT_FIRST); draws no separate chart."
    # VIS-21: evidence-class figure is unordered
    v = _v(c, "VIS-EVIDENCE-CLASS-LADDER")
    v["rationale"] = "Method explainer on /evidence/; categorical and state-only. Drawn, if at all, as unordered category cards: the classes are not a ranking."
    # VIS-09 closure note: the POS value rows no longer carry the source's percentage contradiction (Master 19, TC-D)
    c["decided_in"] = (c.get("decided_in") or "") + " | Tranche C TC-E (VIS-01..VIS-21)"
    ind = 1 if raw.startswith('{\n "') else 2
    open(out, "w", encoding="utf-8").write(json.dumps(c, ensure_ascii=False, indent=ind) + ("\n" if raw.endswith("\n") else ""))
    print("contract written")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "master":
        from tc_lib import TxError
        try:
            master(*sys.argv[2:6])
        except TxError as ex:
            print("TX ERROR:", ex)
            sys.exit(2)
    else:
        contract(*sys.argv[2:4])
