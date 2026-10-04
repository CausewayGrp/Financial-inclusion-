# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-7: every published value carries a state; discrepancies fixed Master-first.

  python3 e2_7_value_states.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Inputs: audit/edition_2/inputs/E2-7_value_states.json (one state per printed value and date of the 109 Evidence Records
the literal audit traces, compiled from the reading of the originals on 4 October 2026) and E2-7_sources.json (sources
opened that day). States: READ (seen in the original, with locator), DERIVED (computed from values read there), SITE
(this resource's own check or review date, or its own count), SEE:<id> (governed by the named record), UNREACHABLE
(the original could not be opened; the page says so beside the value), TRIVIAL (not a value: "15+", a section number).

Writes:
1. 06 gains the column value_states (JSON). Projected as JSON, so its locators are never matched as reader text.
2. Discrepancies, both languages: the POS limitation (every release from March 2025 is a one-page infographic, not "from
   July 2025"); CLM-059 (SMEPS reports the USD 54.7 million as disbursed: Annual Report 2024, Executive Summary, PDF p. 4);
   CLM-062 (informal firms' account holding is Figure 114, p. 151; the base of 217 is on pp. 139 and 141).
3. Sources read for a value but not bound to its record are bound (BOUND_EXACT records only).
4. Unreachable originals are named beside their values: CLM-049 and /reforms/ (IMF press release of 16 July 2026),
   CLM-020 and MF-ORIG-001+002 (the 2012 SFD document dating microfinance to 1997).
5. VIS-REMITTANCE-COST: the four corridor averages, whose pages refuse automated requests, were reproduced exactly from the
   World Bank's RPW quote-level dataset; the number of quotes is now known (8 and 6) and one outlier quote is named.
6. CLM-032 (lead 1): the same-year revision holds further back, read in four CBY-Aden annual reports.
7. 15: retrieval_date for every source opened on 4 October 2026; document_date where the original states one and the
   library had none.
8. 01_SOURCE_ORIGINS: the lineage of the v0.42R3 workbook, recorded truthfully.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-7:VALUE-STATES"
FX = "E2-7:DISCREPANCY"
DAY = "2026-10-04"

POS_EN = ("From July 2025 the monthly releases take the form of a one-page infographic; continuity of the reporting scope "
          "across that change has not been verified.",
          "Every monthly release from March 2025 is a one-page infographic, and its design changes in January and again in "
          "February 2026; continuity of the reporting scope across these changes has not been verified.")
POS_AR = ("وابتداءً من يوليو 2025 تصدر الإصدارات الشهرية في صورة إنفوغرافيك من صفحة واحدة، ولم يُتحقق من استمرارية نطاق "
          "الإبلاغ عبر هذا التغير.",
          "وكل إصدار شهري منذ مارس 2025 إنفوغرافيك من صفحة واحدة، ويتغير تصميمه في يناير ثم في فبراير 2026؛ ولم يُتحقق من "
          "استمرارية نطاق الإبلاغ عبر هذه التغيرات.")
C59 = [
    ("summary_en", "and a USD 54.7 million programme total whose status (committed or disbursed) is not recorded in the evidence base.",
     "and a programme total of USD 54.7 million that it reports as disbursed."),
    ("summary_ar", "وبإجمالي برامجي قدره 54.7 مليون دولار لا تسجّل قاعدة الأدلة ما إذا كان مبلغًا ملتزَمًا به أم مصروفًا.",
     "وبإجمالي برامجي قدره 54.7 مليون دولار تفيد بأنه مصروف."),
    ("limitations_en", " Whether the USD 54.7 million 2021–2024 total is committed or disbursed funding is not recorded in the evidence base.",
     " The USD 54.7 million 2021–2024 total is disbursed funding as SMEPS reports it; it is not shown by an independent account."),
    ("limitations_ar", " ولا تسجّل قاعدة الأدلة ما إذا كان إجمالي 54.7 مليون دولار للفترة 2021–2024 مبلغًا ملتزَمًا به أم مصروفًا.",
     " وإجمالي 54.7 مليون دولار للفترة 2021–2024 تمويل مصروف كما تفيد به الوكالة، ولا يثبته حساب مستقل."),
]
FIRMS7 = [
    ("en", "with a programme total of USD 54.7 million; the evidence base does not specify whether this total is funding "
           "committed or funding disbursed.",
     "with a programme total of USD 54.7 million, which it reports as disbursed."),
    ("ar", "بإجمالي للبرنامج قدره 54.7 مليون دولار، ولا تحدد قاعدة الأدلة ما إذا كان هذا الإجمالي تمويلًا ملتزمًا به أم مصروفًا.",
     "بإجمالي للبرنامج قدره 54.7 مليون دولار تفيد بأنه مصروف."),
]
C62 = [
    ("method_en", "and informal firms' account holding, with its base, Figures 114–115 (p. 151).",
     "and informal firms' account holding, Figure 114 (p. 151), whose base of 217 informal firms is stated on pp. 139 and 141."),
    ("method_ar", "وامتلاك المنشآت غير الرسمية للحسابات مع قاعدتها، الشكلان 114–115 (ص 151).",
     "وامتلاك المنشآت غير الرسمية للحسابات، الشكل 114 (ص 151)، وقاعدته 217 منشأة غير رسمية كما ترد في الصفحتين 139 و141."),
]
IMF_EN = (" The IMF press release could not be re-opened from this resource on 4 October 2026 (the IMF website refuses "
          "automated requests), so the date, the 18-month length and the status above have not been re-read in the original "
          "for this edition.")
IMF_AR = (" وتعذّر على هذا المورد إعادة فتح البيان الصحفي لصندوق النقد الدولي في 4 أكتوبر 2026 (يرفض موقع الصندوق الطلبات "
          "الآلية)، فلم يُتحقق في هذه الطبعة من التاريخ ومدة 18 شهرًا والوضع المذكور أعلاه في الأصل.")
IMF_SEC_EN = (" The IMF release could not be re-opened on 4 October 2026; these details have not been re-read in the original "
              "for this edition.")
IMF_SEC_AR = (" وتعذّرت إعادة فتح بيان الصندوق في 4 أكتوبر 2026، فلم يُتحقق من هذه التفاصيل في الأصل في هذه الطبعة.")
SFD_EN = (" The 2012 SFD document that dates the start of microfinance to 1997 could not be re-opened on 4 October 2026 (its "
          "archived copy is not reachable from this resource), so that date has not been re-read in the original for this "
          "edition.")
SFD_AR = (" وتعذّرت في 4 أكتوبر 2026 إعادة فتح وثيقة الصندوق لعام 2012 التي تؤرخ بداية التمويل الأصغر بعام 1997 (لا يمكن "
          "الوصول إلى نسختها المؤرشفة من هذا المورد)، فلم يُتحقق من هذا التاريخ في الأصل في هذه الطبعة.")
RPW = [
    ("method_en", "from standardized collection of provider price quotes.",
     "from standardized collection of provider price quotes. The corridor pages refuse automated requests; on 4 October 2026 "
     "each of the four averages was reproduced exactly as the simple average of the third-quarter 2025 quotes in the World "
     "Bank's Remittance Prices Worldwide quote-level dataset (8 quotes for Saudi Arabia–Yemen, 6 for United Arab "
     "Emirates–Yemen)."),
    ("method_ar", "استنادًا إلى جمع موحّد لعروض أسعار مقدمي الخدمة.",
     "استنادًا إلى جمع موحّد لعروض أسعار مقدمي الخدمة. وترفض صفحتا الممرين الطلبات الآلية؛ وفي 4 أكتوبر 2026 أُعيد حساب كلٍّ "
     "من المتوسطات الأربعة فطابق المنشور، بوصفه المتوسط البسيط لعروض أسعار الربع الثالث من 2025 في مجموعة بيانات عروض "
     "الأسعار التفصيلية لقاعدة Remittance Prices Worldwide التابعة للبنك الدولي (8 عروض لممر السعودية–اليمن، و6 لممر "
     "الإمارات–اليمن)."),
    ("limitations_en", "the number of providers and quotes behind it is not recorded in the evidence base.",
     "each rests on few quotes (8 and 6), and one of the six United Arab Emirates quotes for US$200, at 22.71%, lifts that "
     "average well above the other five (2.97% to 5.25%)."),
    ("limitations_ar", "ولا تتضمن قاعدة الأدلة عدد مقدمي الخدمة وعروض الأسعار التي يستند إليها.",
     "ويستند كل متوسط إلى عروض قليلة (8 و6)، ويرفع عرضٌ واحد من عروض الإمارات الستة لمبلغ 200 دولار، قدره 22.71%، ذلك "
     "المتوسط كثيرًا فوق العروض الخمسة الأخرى (من 2.97% إلى 5.25%)."),
]
RPW_DATA = "https://datacatalogfiles.worldbank.org/ddh-published/0037898/DR0095523/rpw_dataset_2011_2025_q3.xlsx"
C32 = [
    ("summary_en", "This is a same-year restatement, not evidence of economic movement between years.",
     "This is a same-year restatement, not evidence of economic movement between years. The same holds further back: for "
     "2021, the annual reports of 2022, 2023, 2024 and 2025 print USD 4,043, 5,400.0, 5,625 and 2,900.22 million; for 2022, "
     "USD 4,454, 6,000, 6,000 and 3,066.58 million."),
    ("summary_ar", "وهذه إعادة عرض للسنة نفسها، وليست دليلًا على حركة اقتصادية بين عامين.",
     "وهذه إعادة عرض للسنة نفسها، وليست دليلًا على حركة اقتصادية بين عامين. ويصح ذلك على سنوات أسبق أيضًا: فلعام 2021 "
     "تطبع التقارير السنوية لأعوام 2022 و2023 و2024 و2025 القيم 4,043 و5,400.0 و5,625 و2,900.22 مليون دولار، ولعام 2022 "
     "القيم 4,454 و6,000 و6,000 و3,066.58 مليون دولار."),
    ("method_en", "IMF method documentation from 2024–2025 is used as context for the restatement.",
     "IMF method documentation from 2024–2025 is used as context for the restatement. The earlier vintages are read in the "
     "balance-of-payments tables of four reports: 2022 (Arabic only, Table 4-1, p. 37, workers' remittances), 2023 "
     "(statistical annex, p. 54; Table 4-1, p. 46), 2024 (annex, p. 48) and 2025 (annex, p. 52)."),
    ("method_ar", "وتُستخدم وثائق المنهج لدى صندوق النقد الدولي للفترة 2024–2025 سياقًا لتفسير إعادة العرض.",
     "وتُستخدم وثائق المنهج لدى صندوق النقد الدولي للفترة 2024–2025 سياقًا لتفسير إعادة العرض. وتُقرأ النسخ الأسبق في جداول "
     "ميزان المدفوعات في أربعة تقارير: تقرير 2022 (بالعربية فقط، الجدول 4-1، ص 37، «تحويلات العاملين»)، وتقرير 2023 "
     "(الملحق الإحصائي، ص 54؛ والجدول 4-1، ص 46)، وتقرير 2024 (الملحق، ص 48)، وتقرير 2025 (الملحق، ص 52)."),
    ("limitations_en", "A same-year revision remains distinct from change over time.",
     "A same-year revision remains distinct from change over time. In the 2022 report's statistical annex (p. 45) the row "
     "labels are shifted by one line, so the row labelled remittances there prints the transfers balance; this record uses "
     "Table 4-1 (p. 37)."),
    ("limitations_ar", "وتظل مراجعة النسخة منفصلة عن التغير الزمني.",
     "وتظل مراجعة النسخة منفصلة عن التغير الزمني. وفي الملحق الإحصائي لتقرير 2022 (ص 45) تنزاح تسميات الصفوف سطرًا واحدًا، "
     "فيطبع الصف المسمى «حوالات العاملين» ميزان التحويلات؛ ويعتمد هذا السجل على الجدول 4-1 (ص 37)."),
]
C32_DEPS = ["SRC-CBY-AR2022-001", "SRC-CBY-AR2023-001"]
# 15.document_date: the library had none and the original states one (live data pages and unreached pages excluded)
DOC_SKIP = {"SRC-WB-FINDEX-AGG-2022", "SRC-WB-WDI-REMIT-YEM-CURRENT", "SRC-WB-RPW-SA-YEM-2025Q3-001", "SRC-WB-RPW-UAE-YEM-2025Q3-001"}
ORIGIN = ("Retained as data substrate; historical QA/gate sheets are not carried into the final master.",
          "Retained as data substrate; historical QA/gate sheets are not carried into the final master. Lineage as found on "
          "4 October 2026: no copy of v0.42R3 has been found; the newest predecessor found is v0.43, which the owner compared "
          "with this Master on 4 October 2026; the gaps it showed are recorded as leads in audit/edition_2/EDITION_2_LOG.md.")


def add_deps(t06, oid, extra, finding):
    deps = t06.get(oid, "source_dependencies")
    have = [d.strip() for d in deps.split(";")]
    new = [x for x in extra if x not in have]
    if not new:
        return []
    t06.set(finding, oid, "source_dependencies", deps + "; " + "; ".join(new), deps)
    links = t06.get(oid, "source_links")
    try:
        cur = json.loads(links) if links else []
    except ValueError:
        raise TxError(f"{oid}: source_links is not JSON")
    if cur and all(isinstance(x, str) for x in cur):
        t06.set(finding, oid, "source_links", json.dumps(cur + new, ensure_ascii=False), links)
    return new


def main():
    src, out, ledger, work = sys.argv[1:5]
    vs = json.load(open(os.path.join(HERE, "inputs", "E2-7_value_states.json"), encoding="utf-8"))
    sources = json.load(open(os.path.join(HERE, "inputs", "E2-7_sources.json"), encoding="utf-8"))
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    # 1. the column
    if t06.head[27] != "source_use_roles" or "value_states" in t06.head:
        raise TxError("06 header not at expected state")
    s.set(F, "06_EVIDENCE_OBJECTS", 4, 29, "value_states", None, "header.value_states")
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for oid, states in vs.items():
        t06.set(F, oid, "value_states", json.dumps(states, ensure_ascii=False, separators=(",", ":")), None)
    # 2. discrepancies
    for oid in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE"):
        s.replace(FX, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col("limitations_en"), *POS_EN, f"{oid}.limitations_en")
        s.replace(FX, "06_EVIDENCE_OBJECTS", t06.rows[oid], t06.col("limitations_ar"), *POS_AR, f"{oid}.limitations_ar")
    for field, old, new in C59:
        s.replace(FX, "06_EVIDENCE_OBJECTS", t06.rows["CLM-059"], t06.col(field), old, new, f"CLM-059.{field}")
    for lang, old, new in FIRMS7:
        s.replace_section(FX, "/firms/", 7, lang, "body", old, new)
    for field, old, new in C62:
        s.replace(FX, "06_EVIDENCE_OBJECTS", t06.rows["CLM-062"], t06.col(field), old, new, f"CLM-062.{field}")
    # 3. sources read for a value, bound to its record
    bound = OrderedDict()
    for oid, states in vs.items():
        if t06.get(oid, "lineage_state") != "BOUND_EXACT":
            continue
        extra = []
        for e in states:
            if e["s"] in ("READ", "DERIVED") and e.get("src", "").startswith("SRC-") and e["src"] not in extra:
                extra.append(e["src"])
        new = add_deps(t06, oid, extra, F)
        if new:
            bound[oid] = new
    # 4. unreachable originals named beside their values
    for oid, en, ar in (("CLM-049", IMF_EN, IMF_AR), ("CLM-020", SFD_EN, SFD_AR), ("MF-ORIG-001+002", SFD_EN, SFD_AR)):
        for lang, add in (("en", en), ("ar", ar)):
            cur = t06.get(oid, f"summary_{lang}")
            t06.set(F, oid, f"summary_{lang}", cur.rstrip() + add, cur)
    s.replace_section(F, "/reforms/", 7, "en", "body", "should not be presented as Executive Board approval.",
                      "should not be presented as Executive Board approval." + IMF_SEC_EN)
    s.replace_section(F, "/reforms/", 7, "ar", "body", "ولا يجوز تقديمه كموافقة من المجلس التنفيذي.",
                      "ولا يجوز تقديمه كموافقة من المجلس التنفيذي." + IMF_SEC_AR)
    # 5. RPW reproduced from the quote-level dataset
    for field, old, new in RPW:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["VIS-REMITTANCE-COST"], t06.col(field), old, new, f"VIS-REMITTANCE-COST.{field}")
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    for sid in ("SRC-WB-RPW-SA-YEM-2025Q3-001", "SRC-WB-RPW-UAE-YEM-2025Q3-001"):
        t15.set(F, sid, "additional_urls", json.dumps([RPW_DATA]), None)
    # 6. lead 1: remittance vintages
    for field, old, new in C32:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["CLM-032"], t06.col(field), old, new, f"CLM-032.{field}")
    add_deps(t06, "CLM-032", C32_DEPS, F)
    # 7. source dates
    for sid in sources["retrieved"]:
        if sid in t15.rows:
            t15.set(F, sid, "retrieval_date", DAY, t15.get(sid, "retrieval_date"))
    for sid, d in sources["document_dates"].items():
        if sid in t15.rows and sid not in DOC_SKIP and not t15.get(sid, "document_date"):
            t15.set(F, sid, "document_date", d, None)
    # 8. lineage
    t01 = Table(s, "01_SOURCE_ORIGINS", 4)
    t01.set(F, "Prior master backend", "treatment_in_master", ORIGIN[1], ORIGIN[0])
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-7"), ("summary", "A state for every published value; discrepancies fixed Master-first; unreachable originals named; source dates; remittance vintages"), ("bound", bound)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))
    print(json.dumps(bound))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
