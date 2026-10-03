# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-8b: the independent reviews of RC-8, folded into one rerun (owner note, 3 October
2026, point 3). Applied to the RC-8 Master (8385ede6ebd9…).

  python3 rc_8b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Bilingual review (Arabic first; NOT ACCEPTABLE, one blocking finding):
  B1  CLM-019 method: "recorded … from the signed decisions" overstated provenance. Only Decisions 10 and 18 have a
      signed-scan locator; the others are read from news pages, and some names are only secondarily corroborated.
      "Lineage" is internal jargon and «تُطبع» a calque. The sentence now says only what holds for every decision.
  S2  "its English page" / «صفحته بالإنجليزية» names the CBY-Aden payments pages ambiguously: /payments/ heading and
      the CLM-017 title now say "payments page" like every other cell.
  S3  The reporting-scope boundary is missing where 1,651 now reaches: the /payments/ title and the quoted
      observation in the Reading "Define what you count".
  S4  The site's page is "Data & sources" / «البيانات والمصادر», not "the Data page" (SEARCH-ALIAS-001).
  S5  «التي تطبعها الإصدارات» → «التي تعرضها الإصدارات» (the site's term for a release's figure); English "print" →
      "display" to match.
  S6  "do not give" is unidiomatic for a computed result: "do not yield".
Adversarial review (BROKEN, two blocking findings; every new number confirmed against the originals):
  A1  The reason given for reading the POS value in YER million was false: percentage changes cannot tell million from
      billion. What holds: every release writes the decimal mark as a comma (the Master already records April 2025's
      "317,639 million" as 317.639); from January 2026 the value is given in billions, so "1,262" under «مليار» is
      1.262 billion, i.e. YER 1,262 million. The disclosure now says that, in the summaries, the chart note, the
      passport and the observation caveats; source_value_as_reported records the label.
  A2  The exchange and remittance roster changed: the file linked on cby-ye.com/pages/14 on 3 October 2026 is
      https://cby-ye.com/files/6ab391c11043b.pdf (created 22 September 2026, 20 pages), whose serial numbering ends at
      100 companies, 231 establishments and 111 remittance agents (442 rows); the section headings were checked by eye.
      The Master held the 19 August file (98 / 225 / 106; 429). Counts, copy, contract pins and the source locator move;
      CLM-009 says the roster file has been replaced during 2026.
  Should-fix applied: the February percentages are "under 0.1 point, recorded, not flagged", not "truncation"; "holds no
  laws" becomes "holds no law as a source document" (two Master records concern laws); the bank list has "no printed
  date"; the value rows' source_value_as_reported carries «مليار». Not changed: the regulatory group's "(23)" counts 22
  cards and a link to the curated card of Decision No. 23 of 2024, which the group renders (verified in dist/).
"""
import json, os, sys, tempfile
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from rc_lib import Session, Table, TxError, set_ui  # noqa: E402
from projection.master_reader import Workbook  # noqa: E402

F = "RC-8b"

CLM019_OLD_EN = ("The names of the entities are recorded in this resource's lineage from the signed decisions and are not "
                 "printed on this site.")
CLM019_NEW_EN = ("Entity names, where transcribed, are held only in this resource's internal source records and are not "
                 "published on this site.")
CLM019_OLD_AR = "وتُسجَّل أسماء الجهات في سجل المصادر الداخلي لهذا المورد من القرارات الموقعة، ولا تُطبع في هذا الموقع."
CLM019_NEW_AR = "وحيثما نُقلت أسماء الجهات، فهي محفوظة في سجل المصادر الداخلي لهذا المورد فقط، ولا تُنشر في هذا الموقع."

# (sheet, row, col, old substring, new substring) — each old substring must occur exactly once in its cell
CELL_SUBS = [
    ("06_EVIDENCE_OBJECTS", 24, 14, CLM019_OLD_EN, CLM019_NEW_EN),
    ("06_EVIDENCE_OBJECTS", 24, 15, CLM019_OLD_AR, CLM019_NEW_AR),
    ("03_PAGE_SECTIONS", 177, 4, "; its English page still ends at January 2026", "; its English payments page still ends at January 2026"),
    ("03_PAGE_SECTIONS", 178, 6, "ولا تزال صفحته بالإنجليزية تنتهي عند يناير 2026", "ولا تزال صفحة المدفوعات بالإنجليزية تنتهي عند يناير 2026"),
    ("06_EVIDENCE_OBJECTS", 22, 4, "June 2026 on its Arabic page, January 2026 on its English page (checked 3 October 2026)",
     "June 2026 on its Arabic payments page, January 2026 on its English payments page (both checked 3 October 2026)"),
    ("06_EVIDENCE_OBJECTS", 22, 5, "يونيو 2026 في صفحته بالعربية، ويناير 2026 في صفحته بالإنجليزية",
     "يونيو 2026 في صفحة المدفوعات بالعربية، ويناير 2026 في صفحة المدفوعات بالإنجليزية"),
    ("02_SITE_MAP", 127, 5, "between March 2025 and June 2026; how many people", "between March 2025 and June 2026, within its reporting scope; how many people"),
    ("02_SITE_MAP", 127, 6, "بين مارس 2025 ويونيو 2026؛ أما عدد", "بين مارس 2025 ويونيو 2026، ضمن نطاق إبلاغه؛ أما عدد"),
    ("03_PAGE_SECTIONS", 247, 5, "rose from 561 to 1,651 between March 2025 and June 2026”",
     "rose from 561 to 1,651 between March 2025 and June 2026, within its reporting scope”"),
    ("03_PAGE_SECTIONS", 247, 7, "من 561 إلى 1,651 بين مارس 2025 ويونيو 2026»", "من 561 إلى 1,651 بين مارس 2025 ويونيو 2026، ضمن نطاق إبلاغه»"),
]
ALIAS = {"boundary_note_en": ("Discovery aid only: this evidence base holds no laws. It holds regulations, circulars, decisions and "
                             "official lists issued by the Central Bank of Yemen – Aden, listed on the Data page.",
                             "Discovery aid only: this evidence base holds no law as a source document. It holds regulations, "
                             "circulars, decisions and official lists issued by the Central Bank of Yemen – Aden, listed on the "
                             "Data & sources page."),
         "boundary_note_ar": ("أداة اكتشاف فقط: لا تضم قاعدة الأدلة هذه أي قانون. وتضم لوائح وتعاميم وقرارات وقوائم رسمية صادرة عن "
                              "البنك المركزي اليمني – عدن، مدرجة في صفحة البيانات.",
                              "أداة اكتشاف فقط: لا تضم قاعدة الأدلة هذه أي قانون بوصفه وثيقة مصدرية. وتضم لوائح وتعاميم وقرارات "
                              "وقوائم رسمية صادرة عن البنك المركزي اليمني – عدن، مدرجة في صفحة البيانات والمصادر.")}
# Substitutions applied wherever they occur in the Master (every occurrence was written by RC-8), with the counts expected
GLOBAL_SUBS = [
    (" do not give", " do not yield", None),
    ("2026 totals give the +", "2026 totals yield the +", None),
]

# ---- A1: the POS value unit ---------------------------------------------------------------------------------------
SUM_OLD_EN = ("From the January 2026 release onward the value is labelled “billion”; this resource reads it as YER million, the unit "
              "the earlier releases state, because only that reading reconciles with the month-on-month changes the releases print.")
SUM_NEW_EN = ("From the January 2026 release onward the value is stated in billions, where the earlier releases stated millions; all "
              "of them write the decimal mark as a comma, so the January figure printed as 1,262 billion is 1.262 billion, that is "
              "YER 1,262 million. This resource keeps the whole series in YER million.")
SUM_OLD_AR = ("وابتداءً من إصدار يناير 2026 تُدرج القيمة تحت وحدة «مليار»، لكن هذا المورد يقرؤها بملايين الريالات، وهي الوحدة التي "
              "تذكرها الإصدارات السابقة، لأن هذه القراءة وحدها تتسق مع نسب التغير الشهرية التي تطبعها الإصدارات.")
SUM_NEW_AR = ("وابتداءً من إصدار يناير 2026 تُذكر القيمة بالمليار، بينما ذكرتها الإصدارات السابقة بالمليون؛ وتستعمل الإصدارات كلها "
              "الفاصلة علامةً عشرية، فرقم يناير المنشور بصيغة 1,262 مليار يعني 1.262 مليار ريال، أي 1,262 مليون ريال. ويُبقي هذا "
              "المورد السلسلة كلها بملايين الريالات.")
MET_OLD_EN = ("From the January 2026 release onward the value is labelled “billion”, while the earlier releases state million YER; the "
              "month-on-month changes the releases print reconcile only when the values are read in millions, so this resource "
              "continues to read them as YER million.")
MET_NEW_EN = ("From the January 2026 release onward the value is stated in billions, while the earlier releases state millions; all "
              "of them write the decimal mark as a comma, so the January figure printed as 1,262 billion is 1.262 billion, that is "
              "YER 1,262 million, and this resource keeps the series in YER million.")
MET_OLD_AR = ("وابتداءً من إصدار يناير 2026 تُدرج القيمة تحت وحدة «مليار»، بينما تذكر الإصدارات السابقة أنها بملايين الريالات؛ ولا تتسق "
              "نسب التغير الشهرية التي تطبعها الإصدارات إلا إذا قُرئت القيم بالملايين، لذلك يواصل هذا المورد قراءتها بملايين الريالات.")
MET_NEW_AR = ("وابتداءً من إصدار يناير 2026 تُذكر القيمة بالمليار، بينما تذكرها الإصدارات السابقة بالمليون؛ وتستعمل الإصدارات كلها "
              "الفاصلة علامةً عشرية، فرقم يناير المنشور بصيغة 1,262 مليار يعني 1.262 مليار ريال، أي 1,262 مليون ريال، ويُبقي هذا "
              "المورد السلسلة بملايين الريالات.")
PAS_OLD = ("From the January 2026 release onward the YER value tile is labelled “billion” (مليار), while earlier releases state "
           "million YER; the printed month-on-month changes reconcile only in YER million, so the values are read as YER million.")
PAS_NEW = ("From the January 2026 release onward the YER value tile is labelled “billion” (مليار), while earlier releases state "
           "million YER. Every release writes the decimal mark as a comma (April 2025 prints 317,639 under million: 317.639 "
           "million; January 2026 prints 1,262 under billion: 1.262 billion = YER 1,262 million), so the series is kept in YER "
           "million. Month-on-month percentages cannot tell the two scales apart; the comma reading, and a value per "
           "transaction close to the Q3 2024 report's (about YER 52,500), do.")
VALUE_ROWS = {89: (1232, "−2.3%"), 92: (1124, "−8.8%"), 95: (1244, "+10.7%"), 98: (1579, "+26.9%"), 101: (1045, "−33.8%")}   # 19 row: (value, displayed)
OLD_CAVEAT = ("Normalized to YER millions. The tile is labelled «مليار» (billion), as in every release from January 2026; it is read "
              "as YER million in continuity with the earlier releases, which state million YER, because only that reading "
              "reconciles with the month-on-month changes the releases print (displayed {pct}).")
NEW_CAVEAT = ("Normalized to YER millions. The tile prints {v:,} under «مليار» (billion) with a comma as the decimal mark: {b} "
              "billion, that is YER {v:,} million, the series unit; the earlier releases print millions the same way (April 2025: "
              "317,639 under million = 317.639 million). Displayed change {pct}.")

# ---- A2: the exchange and remittance roster -------------------------------------------------------------------------
ROSTER_URL = "https://cby-ye.com/files/6ab391c11043b.pdf"
ROSTER_OLD_URL = "https://www.cby-ye.com/files/6a87039fd05bb.pdf"
R_EN = ("98 exchange companies, 225 individual exchange establishments and 106 remittance agents",
        "100 exchange companies, 231 individual exchange establishments and 111 remittance agents")
R_AR = ("98 شركة صرافة و225 منشأة صرافة فردية و106 وكلاء حوالات", "100 شركة صرافة و231 منشأة صرافة فردية و111 وكيلًا للحوالات")
ROSTER_SUBS = [
    ("03_PAGE_SECTIONS", 216, 5, R_EN), ("03_PAGE_SECTIONS", 216, 7, R_AR), ("03_PAGE_SECTIONS", 219, 5, R_EN),
    ("03_PAGE_SECTIONS", 220, 7, R_AR), ("03_PAGE_SECTIONS", 355, 5, R_EN), ("03_PAGE_SECTIONS", 356, 7, R_AR),
    ("06_EVIDENCE_OBJECTS", 7, 6, R_EN), ("06_EVIDENCE_OBJECTS", 7, 7, R_AR), ("06_EVIDENCE_OBJECTS", 14, 6, R_EN),
    ("06_EVIDENCE_OBJECTS", 14, 7, R_AR),
    ("06_EVIDENCE_OBJECTS", 7, 14, ("official 11-page roster", "official 20-page roster")),
    ("06_EVIDENCE_OBJECTS", 7, 14, ("ends at 98, 225 and 106.", "ends at 100, 231 and 111.")),
    ("06_EVIDENCE_OBJECTS", 7, 15, ("المكونة من 11 صفحة", "المكونة من 20 صفحة")),
    ("06_EVIDENCE_OBJECTS", 7, 15, ("عند 98 و225 و106.", "عند 100 و231 و111.")),
    ("06_EVIDENCE_OBJECTS", 7, 18, ("they are separate evidence and are not applied to these counts.",
                                    "they are separate evidence and are not applied to these counts. CBY-Aden has replaced the roster "
                                    "file during 2026; the counts are those of the file linked on its website when checked on 3 October 2026.")),
    ("06_EVIDENCE_OBJECTS", 7, 19, ("وهي أدلة منفصلة لا تُطبَّق على هذه الأعداد.",
                                    "وهي أدلة منفصلة لا تُطبَّق على هذه الأعداد. وقد استبدل البنك المركزي اليمني – عدن ملف القائمة خلال عام "
                                    "2026؛ والأعداد هي أعداد الملف المنشور في موقعه كما اطُّلع عليه في 3 أكتوبر 2026.")),
    ("00_MASTER", 41, 5, ("98 exchange companies, 225 exchange establishments, 106 remittance agents",
                          "100 exchange companies, 231 exchange establishments, 111 remittance agents")),
    ("33_ANALYTICS_MASTER", 55, 4, ("98 companies, 225 individual establishments and 106 remittance agents",
                                    "100 companies, 231 individual establishments and 111 remittance agents")),
    ("33_ANALYTICS_MASTER", 57, 4, ("98 companies, 225 establishments and 106 remittance agents (429 listed rows)",
                                    "100 companies, 231 establishments and 111 remittance agents (442 listed rows)")),
    ("16_DATASET_CATALOG", 215, 10, ("98 exchange companies, 225 individual establishments, 106 remittance agents, plus 429",
                                     "100 exchange companies, 231 individual establishments, 111 remittance agents, plus 442")),
    ("17_INDICATOR_LIBRARY", 217, 9, ("98 listed companies", "100 listed companies")),
    ("17_INDICATOR_LIBRARY", 218, 9, ("225 listed establishments", "231 listed establishments")),
    ("17_INDICATOR_LIBRARY", 219, 9, ("106 listed agents", "111 listed agents")),
    ("17_INDICATOR_LIBRARY", 220, 9, ("429 is an arithmetic", "442 is an arithmetic")),
    ("04_NAV_UX", 197, 4, ("SOURCE_LISTED_ROWS__98_COMPANIES__225_ESTABLISHMENTS__106_REMITTANCE_AGENTS",
                           "SOURCE_LISTED_ROWS__100_COMPANIES__231_ESTABLISHMENTS__111_REMITTANCE_AGENTS")),
    ("15_SOURCE_LIBRARY", 6, 6, ("(undated; as checked on 3 October 2026)", "(no printed date; as checked on 3 October 2026)")),
    ("15_SOURCE_LIBRARY", 6, 12, ("(غير مؤرخ؛ كما اطُّلع عليه في 3 أكتوبر 2026)", "(لا يحمل تاريخًا مطبوعًا؛ كما اطُّلع عليه في 3 أكتوبر 2026)")),
]
SCOPE_SUB_EN = ("The evidence base holds no laws, and this group", "The evidence base holds no law as a source document, and this group")
SCOPE_SUB_AR = ("ولا تضم قاعدة الأدلة أي قانون، ولا تضم هذه المجموعة", "ولا تضم قاعدة الأدلة أي قانون بوصفه وثيقة مصدرية، ولا تضم هذه المجموعة")

UNIT_SUBS = [  # (sheet, row, col, old sentence, new sentence)
    ("06_EVIDENCE_OBJECTS", 68, 6, SUM_OLD_EN, SUM_NEW_EN),
    ("11_VISUAL_LIBRARY", 18, 21, SUM_OLD_EN, SUM_NEW_EN),
    ("06_EVIDENCE_OBJECTS", 68, 7, SUM_OLD_AR, SUM_NEW_AR),
    ("11_VISUAL_LIBRARY", 18, 22, SUM_OLD_AR, SUM_NEW_AR),
    ("06_EVIDENCE_OBJECTS", 68, 14, MET_OLD_EN, MET_NEW_EN),
    ("06_EVIDENCE_OBJECTS", 68, 15, MET_OLD_AR, MET_NEW_AR),
    ("34_EVIDENCE_PASSPORTS", 6, 9, PAS_OLD, PAS_NEW),
    ("34_EVIDENCE_PASSPORTS", 6, 9, "this is read as truncation, not contradiction.", "these differences are under 0.1 point and are recorded, not flagged."),
    ("19_PAYMENTS_DATA", 87, 15, "read as truncation, not contradiction.", "a difference under 0.1 point, recorded, not flagged."),
]


def snapshot(s):
    tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=s.work)
    tmp.close()
    s.ed.save(tmp.name)
    wb = Workbook(tmp.name)
    for name in wb.sheet_names:
        wb.grid(name)
    os.remove(tmp.name)
    return wb


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for sheet, r, c, old, new in CELL_SUBS:
        s.replace(F, sheet, r, c, old, new)
    t04 = Table(s, "04_NAV_UX", 533)
    for field, (old, new) in ALIAS.items():
        t04.set(F, "SEARCH-ALIAS-001", field, new, old)
    # A1: value unit
    for sheet, r, c, old, new in UNIT_SUBS:
        s.replace(F, sheet, r, c, old, new)
    t19 = Table(s, "19_PAYMENTS_DATA", 4)
    for row, (v, pct) in VALUE_ROWS.items():
        oid = f"OBS-{row - 4:05d}"
        if t19.rows.get(oid) != row or t19.get(oid, "value") not in (str(v), v):
            raise TxError(f"{F}: 19 r{row} is not {oid} = {v}")
        t19.set(F, oid, "caveats", NEW_CAVEAT.format(v=v, b=f"{v / 1000:.3f}", pct=pct), OLD_CAVEAT.format(pct=pct))
        t19.set(F, oid, "source_value_as_reported", f"{v:,} مليار", f"{v:,}")
    # A2: roster and the should-fix substitutions at fixed coordinates
    for sheet, r, c, (old, new) in ROSTER_SUBS:
        s.replace(F, sheet, r, c, old, new)
    _, ui = __import__("rc_lib").ui_block_end(s)
    r = ui["UI-DATA-GROUP-REGULATORY-SCOPE"]
    s.replace(F, "04_NAV_UX", r, 2, *SCOPE_SUB_EN)
    s.replace(F, "04_NAV_UX", r, 3, *SCOPE_SUB_AR)
    t22 = Table(s, "22_PROVIDERS_DATA", 142)
    for key, new, old in (("CBY-ROSTER-2026-COMP", 100, 98), ("CBY-ROSTER-2026-EST", 231, 225), ("CBY-ROSTER-2026-AGT", 111, 106),
                          ("CBY-ROSTER-2026-ROWS", 442, 429)):
        t22.set(F, key, "count", new, str(old))
    tpu = Table(s, "22_PROVIDERS_DATA", 64)
    row = tpu.rows["PUC-EXCH-2026-01"]
    for col, old, new in ((5, "429", 442),
                          (6, "SOURCE_LISTED_ROWS__98_COMPANIES__225_ESTABLISHMENTS__106_REMITTANCE_AGENTS",
                              "SOURCE_LISTED_ROWS__100_COMPANIES__231_ESTABLISHMENTS__111_REMITTANCE_AGENTS"),
                          (8, "OFFICIAL_11_PAGE_PDF_VISUALLY_VERIFIED", "OFFICIAL_20_PAGE_PDF_VISUALLY_VERIFIED__FILE_OF_2026-09-22")):
        s.set(F, "22_PROVIDERS_DATA", row, col, new, old)
    s.replace(F, "22_PROVIDERS_DATA", row, 11, "429 is the arithmetic sum", "442 is the arithmetic sum")
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    t15.set(F, "SRC-CBY-EXCH-LIST-2026-001", "primary_url", ROSTER_URL, ROSTER_OLD_URL)
    t15.set(F, "SRC-CBY-EXCH-LIST-2026-001", "additional_urls", json.dumps(["https://cby-ye.com/pages/14", ROSTER_OLD_URL]), None)
    t15.set(F, "SRC-CBY-EXCH-LIST-2026-001", "retrieval_date", "2026-10-03", None)
    wb = snapshot(s)
    counts = OrderedDict()
    for old, new, expect in GLOBAL_SUBS:
        n = 0
        for sheet in wb.sheet_names:
            for i, row in enumerate(wb.grid(sheet), 1):
                for j, v in enumerate(row, 1):
                    if isinstance(v, str) and old in v:
                        cur = s.ed.get_value(sheet, i, j)
                        n += cur.count(old)
                        s.set(F, sheet, i, j, cur.replace(old, new), cur)
        if expect is not None and n != expect or n == 0:
            raise TxError(f"{F}: {old!r} found {n} times, expected {expect}")
        counts[old] = n
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-8b"), ("summary", "RC-8 independent reviews folded into one rerun"),
                                           ("items", OrderedDict([("global_substitutions", counts)]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
