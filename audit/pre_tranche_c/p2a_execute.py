# -*- coding: utf-8 -*-
"""P2-A — governed discovery aliases for the high-value WEAK search intents (P2.2).

  python3 p2a_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Aliases are discovery aids only (PB-0492): each maps a topic query to the page that explains that topic. None asserts
that two terms mean the same thing. Rows are appended to the 04 'Search aliases' block (the last block of the sheet).
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

ROWS = [
    ("SEARCH-ALIAS-018", "deposits; deposit; bank deposits", "الودائع; ودائع; الودائع المصرفية", "route:/finance/", None, None),
    ("SEARCH-ALIAS-019", "SME finance; SME; SMEs; MSME; MSMEs; MSME finance; small business finance",
     "المنشآت الصغيرة والمتوسطة; تمويل المنشآت الصغيرة والمتوسطة; المنشآت الصغرى والصغيرة والمتوسطة", "route:/firms/", None, None),
    ("SEARCH-ALIAS-020", "RTGS; real-time gross settlement; real time gross settlement",
     "التسوية الإجمالية الفورية; نظام التسوية الإجمالية الفورية", "route:/payments/ | route:/reforms/", None, None),
    ("SEARCH-ALIAS-021", "FPS; fast payment system; fast payments", "نظام الدفع السريع; الدفع السريع; المدفوعات السريعة",
     "route:/payments/ | route:/reforms/", None, None),
    ("SEARCH-ALIAS-022", "consumer protection; financial consumer protection", "حماية المستهلك; حماية المستهلك المالي", "route:/reforms/", None, None),
    ("SEARCH-ALIAS-023", "complaints; complaint; complaint handling; redress", "الشكاوى; شكوى; معالجة الشكاوى; التظلم", "route:/reforms/",
     "Discovery aid only: the governed complaint rules describe a path and time limits, not how complaints are handled in practice.",
     "وسيلة للعثور على المحتوى فقط: تصف قواعد الشكاوى المعتمدة المسار والمهل، لا طريقة معالجة الشكاوى فعليًا."),
    ("SEARCH-ALIAS-024", "FMIIP; Financial Market Infrastructure and Inclusion Project",
     "FMIIP; مشروع البنية التحتية للأسواق والشمول المالي", "route:/reforms/ | route:/payments/", None, None),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g = Workbook(src).grid("04_NAV_UX")
    last = max(i for i, r in enumerate(g, 1) if any(c not in (None, "") for c in r))
    if g[last - 1][0] != "SEARCH-ALIAS-017":
        raise TxError(f"04 last row is {g[last - 1][0]!r}, expected SEARCH-ALIAS-017")
    for k, row in enumerate(ROWS, 1):
        for j, v in enumerate(row, 1):
            if v not in (None, ""):
                s.set("P2-S01", "04_NAV_UX", last + k, j, v, None, f"{row[0]}.c{j}")
    rep = s.save(out, ledger, [("transaction", "P2-A"), ("scope", "P2.2 governed discovery aliases for high-value weak intents")])
    print(f"P2-A staged: {rep['cells_written']} cells; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
