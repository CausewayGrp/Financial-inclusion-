# -*- coding: utf-8 -*-
"""P5-A — independent-acceptance corrections P5.2 and P5.3 (Master-first).

  python3 p5a_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

P5.2  REF-PAY-001 is the CBY Governor's Decision No. 23 of 2024 on domestic money-transfer activity (26 June 2024).
      Verified in this session from the issuing authority: the CBY news page https://cby-ye.com/news/706 (published
      26 June 2024) gives the decision number, date, title and operative provisions and links the instrument at the
      governed locator https://cby-ye.com/files/667c596ef3bea.pdf. The PDF itself is a scanned image: it is reachable but
      its text could not be machine-read here. The reference number 343/CBY/2024 is recorded as read from the instrument
      by the independent recipient review. A source record is created (FULL_PUBLIC_CARD, rights NOT_ASSESSED) and
      VIS-PAYMENT-RAILS is bound to it; the event row already carries the locator, so RV-CWR-009's credit line resolves.
      Scope of the evidence: a regulatory requirement, not demonstrated implementation, use or outcome.
P5.3  CBY Annual Report 2025, statistical table "Balance of Payments" (columns 2021-2025, USD million), row
      "Remittances": 2021 = 2,900.22; 2022 = 3,066.58; 2023 = 3,240.46 (2024 = 3,422.16 already governed). Read from the
      governed locator of SRC-CBY-AR2025-BOP in this session (three consistent extraction passes of the PDF text). The
      2021-2023 values are added to 23_REMITTANCES with the AR2025 publication-vintage identity, the same unit and metric;
      they are never merged with the IMF series. A governed unit label for the indexed panel is added.
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S04, S06, S15, S23 = "04_NAV_UX", "06_EVIDENCE_OBJECTS", "15_SOURCE_LIBRARY", "23_REMITTANCES"
NEW_SOURCE_ID = "SRC-CBY-DEC-23-2024-001"
LOCATOR = "https://cby-ye.com/files/667c596ef3bea.pdf"
NEW_SOURCE = OrderedDict([
    ("source_id", NEW_SOURCE_ID),
    ("primary_url", LOCATOR),
    ("additional_urls", '["https://cby-ye.com/news/706"]'),
    ("datasets_or_use", "DS-REFORM-EVENTS,DS-PRIMARY-AUTHORITY"),
    ("row_count", 1),
    ("display_title", "Central Bank of Yemen — Governor's Decision No. 23 of 2024 on domestic money-transfer activity "
                      "(26 June 2024; ref. 343/CBY/2024)"),
    ("publisher", "Central Bank of Yemen — Aden"),
    ("resource_category", "Primary administrative and statistical material"),
    ("why_it_matters", "The primary instrument behind the unified domestic transfer network. It requires exchange companies and "
                       "money-transfer agents to execute new domestic cash transfers through the Unified Money Transfer Network, with a "
                       "transition for bank-owned networks and exceptions for licensed e-wallets and payment service providers."),
    ("does_not_establish", "A regulatory requirement does not establish that it was implemented, how many transfers moved to the "
                           "network, or any effect on users or on financial inclusion."),
    ("public_card_state", "FULL_PUBLIC_CARD"),
    ("display_title_ar", "البنك المركزي اليمني — قرار المحافظ رقم (23) لسنة 2024 بشأن مزاولة نشاط التحويلات المالية الداخلية "
                         "(26 يونيو 2024؛ المرجع 343/CBY/2024)"),
    ("resource_category_ar", "مواد إدارية وإحصائية أولية"),
    ("why_it_matters_ar", "الأداة التنظيمية الأولية وراء الشبكة الموحدة للحوالات المحلية. تُلزم شركات الصرافة ووكلاء الحوالات بتنفيذ "
                          "الحوالات النقدية الداخلية الجديدة عبر الشبكة الموحدة للحوالات المالية، مع مرحلة انتقالية للشبكات المملوكة "
                          "للبنوك واستثناءات للمحافظ الإلكترونية ومقدمي خدمات الدفع المرخصين."),
    ("does_not_establish_ar", "لا يثبت الإلزام التنظيمي أنه نُفذ فعليًا، ولا عدد الحوالات التي انتقلت إلى الشبكة، ولا أي أثر على "
                              "المستخدمين أو على الشمول المالي."),
    ("non_public_locator_note", None),
    ("issuer", "Governor, Central Bank of Yemen — Aden"),
    ("hosting_platform", "cby-ye.com"),
    ("rights_state", "NOT_ASSESSED"),
    ("licence", None),
    ("attribution_requirement", None),
    ("retrieval_date", "2026-09-26"),
    ("document_type", "regulatory decision"),
    ("evidence_roles", "primary regulatory instrument (rule stage only; not implementation, use or outcome)"),
])

RMT = OrderedDict([
    ("source_id", "SRC-CBY-AR2025-BOP"), ("series_vintage", "CBY_ANNUAL_REPORT_2025"), ("domain", "remittances_macro"),
    ("geography", "CBY publication scope"), ("period_state", "PUBLISHED_VALUE__AR2025_VINTAGE"), ("metric_id", "RMT-001"),
    ("metric_label_en", "External-sector remittances"), ("metric_label_ar", "التحويلات في الحساب الخارجي وفق تعريف المصدر"),
    ("unit", "USD million"), ("evidence_type", "PRIMARY_OFFICIAL_PUBLICATION_VINTAGE"),
    ("universe", "CBY publication-level BOP remittance series"),
    ("source_table_or_section", "CBY Annual Report 2025 — statistical table 'Balance of Payments' (2021–2025), row 'Remittances'"),
    ("calculation_state", "SOURCE_PUBLISHED"), ("comparability_state", "SAME_VINTAGE_PATH__INDEX_ONLY__NOT_LEVEL_COMPARABLE_WITH_IMF"),
    ("caveat_en", "AR2025 publication vintage. Compared with the IMF series only as a path indexed to 2021 = 100; the raw level is not "
                  "comparable with the IMF series (CLM-037), and the path is never joined to the IMF series or to the AR2024 vintage."),
    ("caveat_ar", "نسخة النشر في التقرير السنوي 2025. لا تُقارن بسلسلة صندوق النقد إلا بوصفها مسارًا مؤشَّرًا بأساس 2021 = 100؛ ولا "
                  "يقارن مستواها الخام بسلسلة الصندوق (CLM-037)، ولا يُوصل المسار بسلسلة الصندوق ولا بنسخة التقرير 2024."),
    ("source_url", "https://english.cby-ye.com/files/6a54b8fcd8b68.pdf"),
])
CBY_AR2025_PATH = [("RMO-CBY-2021-AR2025", "2021", 2900.22), ("RMO-CBY-2022-AR2025", "2022", 3066.58), ("RMO-CBY-2023-AR2025", "2023", 3240.46)]
NEW_UI = [("UI-VIS-UNIT-INDEX-2021", "Index, 2021 = 100", "مؤشر، 2021 = 100",
           "Pre-Tranche-C P5.3. Unit of an indexed path (each series divided by its own 2021 value, × 100).")]


def col_of(h, name):
    if name not in h:
        raise TxError(f"column {name} not found")
    return h.index(name) + 1


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)

    # ---- P5.2 VIS-PAYMENT-RAILS bound to the new source record -----------------------------------------------------
    g06 = wb.grid(S06)
    h06 = [str(x) if x is not None else None for x in g06[3]]
    r = next(i for i, x in enumerate(g06, 1) if x and x[0] == "VIS-PAYMENT-RAILS")
    s.replace("P5.2", S06, r, col_of(h06, "source_dependencies"), "UNBOUND:REF-PAY-001", NEW_SOURCE_ID, "VIS-PAYMENT-RAILS.source_dependencies")
    s.set("P5.2", S06, r, col_of(h06, "lineage_state"), "BOUND_EXACT", "BOUND_PARTIAL", "VIS-PAYMENT-RAILS.lineage_state")
    g04 = wb.grid(S04)
    bound = next(x for x in g04 if x and x[0] == "UI-VERIFY-BOUND")
    for lang, text in (("en", bound[1]), ("ar", bound[2])):
        c = col_of(h06, f"verification_{lang}")
        s.set("P5.2", S06, r, c, text, g06[r - 1][c - 1], f"VIS-PAYMENT-RAILS.verification_{lang}")

    # ---- P5.3 remittance rows ----------------------------------------------------------------------------------------
    g23 = wb.grid(S23)
    h23 = [str(x) if x is not None else None for x in g23[3]]
    ids = {x[0] for x in g23 if x}
    last23 = max(i for i, x in enumerate(g23, 1) if x and x[0])
    if g23[last23 - 1][0] != "RMO-CBY-2024-AR2025":
        raise TxError("23: last row is not RMO-CBY-2024-AR2025")
    new_rows = []
    for oid, period, value in CBY_AR2025_PATH:
        if oid in ids:
            raise TxError(f"23: {oid} exists")
        rec = OrderedDict([("observation_id", oid)])
        rec.update(RMT)
        rec["period"] = period
        rec["value"] = value
        new_rows.append({col_of(h23, k): v for k, v in rec.items()})

    # ---- row insertions last (15, 23, 04) ------------------------------------------------------------------------------
    g15 = wb.grid(S15)
    h15 = [str(x) if x is not None else None for x in g15[3]]
    if any(x and x[0] == NEW_SOURCE_ID for x in g15) or any(x and LOCATOR in [str(v) for v in x] for x in g15):
        raise TxError("15: a source record for the instrument already exists")
    last15 = max(i for i, x in enumerate(g15, 1) if x and x[0])
    s.ed.insert_rows(S15, last15 + 1, [{col_of(h15, k): v for k, v in NEW_SOURCE.items() if v is not None}])
    s.ledger.append(OrderedDict([("finding", "P5.2"), ("sheet", S15), ("row", None), ("col", None), ("field", NEW_SOURCE_ID), ("old", None),
                                 ("new", NEW_SOURCE["display_title"] + " || " + LOCATOR)]))
    s.ed.insert_rows(S23, last23 + 1, new_rows)
    for oid, period, value in CBY_AR2025_PATH:
        s.ledger.append(OrderedDict([("finding", "P5.3"), ("sheet", S23), ("row", None), ("col", None), ("field", oid), ("old", None),
                                     ("new", f"{value} USD million ({period}; CBY_ANNUAL_REPORT_2025)")]))
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    last04 = max(i for i in ui.values() if i < 300)
    if any(c not in (None, "") for c in g04[last04]) or g04[last04 + 1][0] != "Trust navigation":
        raise TxError("04: interface-copy block end not where expected")
    if any(a in ui for a, *_ in NEW_UI):
        raise TxError("04: new UI id exists")
    s.ed.insert_rows(S04, last04 + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in NEW_UI])
    for a, b, c, _ in NEW_UI:
        s.ledger.append(OrderedDict([("finding", "P5.3"), ("sheet", S04), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    rep = s.save(out, ledger, [("transaction", "P5-A"), ("scope", "P5.2 source record for REF-PAY-001 (CBY Decision 23/2024); P5.3 CBY AR2025 "
                                "remittance path 2021-2023 and indexed-unit label")])
    print(f"P5-A staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
