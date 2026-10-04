# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-10: the evidence landscape (Owner Addendum 2, improvement 3, inside B12, for
VIS-EVIDENCE-FRESHNESS).

  python3 rc_10_evidence_landscape.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The 34 dimensions of audit/INDICATOR_COVERAGE_MATRIX.csv become governed rows, Master-first. They form a new block,
"EVIDENCE LANDSCAPE", in 00_MASTER, the overview sheet, which is projected whole to content/master_principles.json.
VIS-EVIDENCE-FRESHNESS renders them as a table grouped by the eight domains, with five columns (scripts/yfie):
  dimension · latest evidence in this base, with its period · evidence type · coverage · where to verify and what
  would change it.
Every cell is governed text:
  - the dimension names (both languages, on the row);
  - the titles and periods of the public records the row names;
  - the categorical labels added here;
  - the domain pages;
  - the titles of the Measurement Agenda priorities.
There are no colour ramps, totals or roll-ups, and no process notes. A row with no evidence says "No evidence in this
base", never "none". Differences from the audit matrix, which is kept as it was:
  - Education and Age are SUFFICIENT_FOR_QUESTION: their account-ownership gaps are on /people/ and in VIS-FINDEX-GAPS
    since RC-1 (Part A item 1), the same basis on which the matrix rates Gender and Income.
  - Income links VIS-FINDEX-GAPS: the matrix named CLM-061, which does not exist.
  - Record links are kept only where the record has a public page.

The same transaction carries the independent bilingual review of RC-9 (B6), tagged RC-9b, in cells RC-10 does not
touch (owner note, 3 October 2026, point 3):
  B1  CWR-001 → MA-001 is removed. The Reading concerns balance-of-payments inflows; MA-001's remittance evidence is
      domestic household receipt, so the link mixed two universes. CWR-001 joins CWR-002 under "Gaps in the agenda"
      (MEASUREMENT_LINKS.md).
  S1  Reading pages say what a link means (new label UI-READING-MEASUREMENT-NOTE).
  S2–S5  Four Arabic fixes in decisions_unlocked_ar: MA-002 «النشاط الإداري»; MA-007 «أكبر» and «اعرف عميلك»;
      MA-004 «تتقدم»; MA-005 «ما السكان».
It also completes RC-8b's roster update (found by design/reference/check_visuals.py, values_printed): the provider
matrix's limit label UI-VIS-CAT-PRV-LIMIT-EXCHANGE and INS-016 still said 429; the roster total is 442.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows  # noqa: E402

F = "RC-10:LANDSCAPE"
HEADER = ["landscape_id", "domain_route", "dimension_en", "dimension_ar", "evidence_class", "coverage_state", "record_ids",
          "verify_routes", "measurement_ids"]
S, P, G, N = "SUFFICIENT_FOR_QUESTION", "PARTIAL", "MEASUREMENT_GAP", "NO_EVIDENCE"
ROWS = [  # domain, EN, AR, classes, coverage, records, verify routes, priorities
    ("/people/", "Account ownership", "امتلاك الحساب", "SURVEY", S, ["CLM-001", "CLM-025"], ["/people/"], ["MA-001"]),
    ("/people/", "Savings", "الادخار", "SURVEY", P, ["CLM-029", "CLM-031"], ["/people/"], ["MA-001"]),
    ("/people/", "Borrowing by people", "اقتراض الأفراد", "SURVEY", P, ["CLM-028"], ["/people/"], ["MA-001"]),
    ("/people/", "Digital payments by people", "المدفوعات الرقمية لدى الأفراد", "SURVEY", G, [], [], ["MA-001", "MA-002"]),
    ("/people/", "Affordability of accounts and services", "القدرة على تحمّل كلفة الحسابات والخدمات", "SURVEY", G, [], [], ["MA-001"]),
    ("/people/", "Financial literacy and capability", "الثقافة المالية والقدرة المالية", "SURVEY;PROGRAMME", P, ["CLM-013", "VIS-FL-EVIDENCE-LADDER"], ["/people/"], ["MA-001"]),
    ("/people/", "Digital capability (phone, internet)", "القدرة الرقمية (الهاتف والإنترنت)", "SURVEY", G, [], [], ["MA-001", "MA-007"]),
    ("/people/", "Financial health and resilience", "الصحة المالية والقدرة على الصمود", "SURVEY", G, ["VIS-FINDEX-RESILIENCE"], [], ["MA-001"]),
    ("/people/", "Gender", "النوع الاجتماعي", "SURVEY", S, ["CLM-002"], ["/people/"], ["MA-003"]),
    ("/people/", "Income", "الدخل", "SURVEY", S, ["VIS-FINDEX-GAPS"], ["/people/"], ["MA-003"]),
    ("/people/", "Education", "التعليم", "SURVEY", S, ["VIS-FINDEX-GAPS"], ["/people/"], ["MA-003"]),
    ("/people/", "Age", "العمر", "SURVEY", S, ["VIS-FINDEX-GAPS"], ["/people/"], ["MA-003"]),
    ("/people/", "Displacement status", "وضع النزوح", "CONTEXT", G, [], [], ["MA-003"]),
    ("/people/", "Disability", "الإعاقة", "", N, [], [], ["MA-003"]),
    ("/access/", "Access points and where services operate", "نقاط الوصول وأماكن عمل الخدمات", "PROGRAMME", G, ["XW-FMIIP-005"], ["/access/"], ["MA-005"]),
    ("/access/", "Rural and urban differences", "الفروق بين الريف والحضر", "ANALYTICAL", G, ["CLM-052"], ["/access/"], ["MA-001", "MA-005"]),
    ("/access/", "Service reliability and quality", "موثوقية الخدمة وجودتها", "", N, [], [], ["MA-010"]),
    ("/payments/", "Active use and how often", "الاستخدام الفعلي ومدى تكراره", "SURVEY;ANALYTICAL;PROGRAMME", P, ["CLM-050"], ["/payments/"], ["MA-002"]),
    ("/payments/", "Payment infrastructure", "البنية التحتية للمدفوعات", "ADMINISTRATIVE", S, ["CLM-003", "CLM-017"], ["/payments/"], ["MA-002", "MA-010"]),
    ("/payments/", "Identity checks and account opening", "التحقق من الهوية وفتح الحسابات", "REGULATORY;SURVEY", P, ["CLM-012"], ["/payments/"], ["MA-007"]),
    ("/payments/", "Humanitarian and government transfers: use afterwards", "التحويلات الإنسانية والحكومية: الاستخدام بعدها", "PROGRAMME", G, ["CLM-045"], ["/payments/"], ["MA-009"]),
    ("/remittances/", "Remittances received by households", "التحويلات التي تتلقاها الأسر", "SURVEY", P, ["CLM-030"], ["/remittances/"], ["MA-001"]),
    ("/remittances/", "Remittance flows to the country", "تدفقات التحويلات إلى البلد", "ADMINISTRATIVE;ANALYTICAL", P, ["CLM-007", "CLM-032"], ["/remittances/"], []),
    ("/remittances/", "Remittance cost", "كلفة التحويلات", "OTHER", P, ["VIS-REMITTANCE-COST"], ["/remittances/"], []),
    ("/providers/", "Provider presence (formal status)", "وجود مقدمي الخدمات (الوضع الرسمي)", "REGULATORY", S, ["CLM-008", "CLM-009", "CLM-019"], ["/providers/"], ["MA-005"]),
    ("/providers/", "Digital safety and fraud", "الأمان الرقمي والاحتيال", "", N, [], [], ["MA-006"]),
    ("/finance/", "Microfinance outreach", "انتشار التمويل الأصغر", "ADMINISTRATIVE;ANALYTICAL", P, ["CLM-053"], ["/finance/"], ["MA-004"]),
    ("/finance/", "Banking system (credit, deposits)", "القطاع المصرفي (الائتمان والودائع)", "ADMINISTRATIVE", P, ["CLM-033", "CLM-038"], ["/finance/"], ["MA-008"]),
    ("/finance/", "Insurance", "التأمين", "", N, [], [], []),
    ("/finance/", "Pensions", "المعاشات التقاعدية", "", N, [], [], []),
    ("/firms/", "Firm finance", "تمويل المنشآت", "SURVEY", P, ["CLM-005", "CLM-006"], ["/firms/"], ["MA-004"]),
    ("/firms/", "Reach of programmes for small firms", "وصول البرامج إلى المنشآت الصغيرة", "PROGRAMME", P, ["CLM-059", "CLM-060"], ["/firms/"], ["MA-004"]),
    ("/reforms/", "Consumer protection and redress", "حماية المستهلك ومعالجة الشكاوى", "REGULATORY", P, ["CLM-011", "DS-FCP-ARCH"], ["/reforms/"], ["MA-006"]),
    ("/reforms/", "Regulatory implementation", "تطبيق الإطار التنظيمي", "REGULATORY", P, ["CLM-012", "CLM-018"], ["/reforms/"], ["MA-010"]),
]
LABELS = [
    ("UI-LAND-COL-DIMENSION", "Dimension", "البُعد"),
    ("UI-LAND-COL-EVIDENCE", "Latest evidence in this base, with its period", "أحدث دليل في قاعدة الأدلة هذه، مع فترته"),
    ("UI-LAND-COL-CLASS", "Evidence type", "نوع الدليل"),
    ("UI-LAND-COL-COVERAGE", "Coverage", "مدى التغطية"),
    ("UI-LAND-COL-NEXT", "Where to verify · what would change it", "أين يُتحقق منه · ما الذي سيغيّره"),
    ("UI-LAND-DOM-PEOPLE", "People", "الأفراد"), ("UI-LAND-DOM-ACCESS", "Access", "الوصول"),
    ("UI-LAND-DOM-PAYMENTS", "Payments", "المدفوعات"), ("UI-LAND-DOM-REMITTANCES", "Remittances", "التحويلات"),
    ("UI-LAND-DOM-PROVIDERS", "Providers", "مقدمو الخدمات"), ("UI-LAND-DOM-FINANCE", "Finance", "التمويل"),
    ("UI-LAND-DOM-FIRMS", "Firms", "المنشآت"), ("UI-LAND-DOM-REFORMS", "Reforms", "الإصلاحات"),
    ("UI-LAND-CLASS-SURVEY", "Survey", "مسح"), ("UI-LAND-CLASS-ADMINISTRATIVE", "Administrative record", "سجل إداري"),
    ("UI-LAND-CLASS-REGULATORY", "Regulatory material", "مادة تنظيمية"), ("UI-LAND-CLASS-PROGRAMME", "Programme record", "سجل برنامج"),
    ("UI-LAND-CLASS-ANALYTICAL", "Secondary analysis", "تحليل ثانوي"), ("UI-LAND-CLASS-CONTEXT", "Context source", "مصدر سياقي"),
    ("UI-LAND-CLASS-OTHER", "Other source", "مصدر آخر"),
    ("UI-LAND-COV-SUFFICIENT_FOR_QUESTION", "Sufficient for its question", "كافٍ لسؤاله"),
    ("UI-LAND-COV-PARTIAL", "Partial", "جزئي"), ("UI-LAND-COV-MEASUREMENT_GAP", "Measurement gap", "فجوة قياس"),
    ("UI-LAND-COV-NO_EVIDENCE", "No evidence in this base", "لا توجد أدلة في قاعدة الأدلة هذه"),
    ("UI-LAND-NO-PUBLIC-RECORD", "No public record in this base", "لا يوجد سجل منشور في قاعدة الأدلة هذه"),
    ("UI-LAND-NOTE", "Categorical states only: no scores and no totals.", "حالات وصفية فقط: لا درجات ولا مجاميع."),
]
RULE = "RC-10 (Owner Addendum 2, improvement 3). Evidence landscape table on VIS-EVIDENCE-FRESHNESS."
F9 = "RC-9b"
MA_AR = [("MA-002", "إلى أي مدى يمكن تفسير النشاط الإداري باعتباره", "إلى أي مدى يمكن تفسير النشاط المسجل في البيانات الإدارية باعتباره"),
         ("MA-007", "ما خطوات الهوية/اعرف عميلك التي تولد أكبر احتكاك في الوقت أو التكلفة أو الرفض؟",
          "ما خطوات التحقق من الهوية وإجراءات «اعرف عميلك» التي تولد احتكاكًا في الوقت أو التكلفة أو الرفض؟"),
         ("MA-004", "وكم تتقدم، وكم يُقبل", "وكم تتقدم بطلب، وكم يُقبل"),
         ("MA-005", "ما السكان أو المناطق", "ما الفئات السكانية أو المناطق")]
NOTE = ("UI-READING-MEASUREMENT-NOTE",
        "Each priority below would supply evidence that this Reading says is missing; the link does not mean the priority would settle the Reading.",
        "من شأن كل أولوية أدناه أن توفر أدلةً تقول هذه القراءة إنها ناقصة، ولا يعني هذا الربط أن الأولوية ستحسم القراءة.",
        "RC-9b (Part B B6, independent review S1). Reading pages: the line under 'Related measurement priorities'.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g = s.grid("00_MASTER")
    if any(r and r[0] == "landscape_id" for r in g):
        raise TxError(f"{F}: 00_MASTER already has a landscape block")
    last = max(i for i, r in enumerate(g, 1) if r and any(c not in (None, "") for c in r))
    rows = [{1: "EVIDENCE LANDSCAPE / مشهد الأدلة"}, {i + 1: h for i, h in enumerate(HEADER)}]
    for n, (dom, en, ar, cls, cov, recs, routes, mas) in enumerate(ROWS, 1):
        rows.append({1: f"ELS-{n:03d}", 2: dom, 3: en, 4: ar, 5: cls or None, 6: cov, 7: json.dumps(recs), 8: json.dumps(routes),
                     9: json.dumps(mas)})
    s.ed.insert_rows("00_MASTER", last + 3, rows)
    for r in rows:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", "00_MASTER"), ("row", None), ("col", None), ("field", r.get(1)),
                                     ("old", None), ("new", " | ".join(str(r[k]) for k in sorted(r)))]))
    insert_ui_rows(s, F, [(a, b, c, RULE) for a, b, c in LABELS])
    # RC-9b: the independent review of B6
    t08 = Table(s, "08_READINGS", 4)
    t08.set(F9, "CWR-001", "measurement_bindings", "[]", '["MA-001"]')
    t10 = Table(s, "10_MEASUREMENT_AGENDA", 4)
    for mid, old, new in MA_AR:
        cur = t10.get(mid, "decisions_unlocked_ar")
        if cur.count(old) != 1:
            raise TxError(f"{F9}: {mid} decisions_unlocked_ar does not hold {old!r} once")
        t10.set(F9, mid, "decisions_unlocked_ar", cur.replace(old, new), cur)
    insert_ui_rows(s, F9, [NOTE])
    # RC-8b's roster total, completed: the matrix's limit label and INS-016
    F8 = "RC-10:ROSTER-442"
    from rc_lib import set_ui, ui_block_end  # noqa: PLC0415
    set_ui(s, F8, "UI-VIS-CAT-PRV-LIMIT-EXCHANGE",
           "442 is the arithmetic sum of rows listed in the source across three classes, not a count of unique providers or of operating providers.",
           "الرقم 442 مجموع حسابي لصفوف مدرجة في المصدر عبر ثلاث فئات، وليس عددًا لمقدمي خدمات فريدين ولا لمقدمي خدمات عاملين.",
           "429 is the arithmetic sum of rows listed in the source across three classes, not a count of unique providers or of operating providers.",
           "الرقم 429 مجموع حسابي لصفوف مدرجة في المصدر عبر ثلاث فئات، وليس عددًا لمقدمي خدمات فريدين ولا لمقدمي خدمات عاملين.")
    _, ui = ui_block_end(s)
    s.replace(F8, "04_NAV_UX", ui["UI-VIS-CAT-PRV-LIMIT-EXCHANGE"], 4, "provider_limit value '429 is the arithmetic sum", "provider_limit value '442 is the arithmetic sum")
    t33 = Table(s, "33_ANALYTICS_MASTER", 41)
    s.replace(F8, "33_ANALYTICS_MASTER", t33.rows["INS-016"], 7, "382→429", "382→442")
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-10"), ("summary", "Evidence landscape (Addendum 2, improvement 3)"),
                                           ("items", OrderedDict([("rows", len(ROWS)), ("labels", len(LABELS))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
