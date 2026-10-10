# -*- coding: utf-8 -*-
"""Rights, transaction RIGHTS-FINAL: the two corrections the owner made when endorsing the CC BY 4.0 text. EN and AR together.

  python3 rights_final.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner decision of 10 October 2026 (audit/OWNER_DECISIONS_2026-10-10.md, section 4): the CC BY 4.0 text is endorsed with
two corrections, and the rights question is closed permanently. Only /rights/ section 6 (03_PAGE_SECTIONS row 363)
changes; /terms/ and the footer line stay as they are, and no other rights wording changes.

(a) The microdata sentence stated a legal reading of the World Bank Microdata Research License ("which permits
    publishing aggregate statistics with the data cited"). It now states facts only: the intervals are computed from a
    file CauseWay obtained under that licence, and only aggregate estimates are published. The citation sentence and
    "CC BY 4.0 does not extend to the underlying microdata" are unchanged.
(b) Directly after the "Covered:" list: for figures CauseWay calculates from other publishers' data, the licence covers
    the calculation and presentation; the underlying data stay under their publishers' terms.

The English and Arabic are the owner's, with one correction from the independent Arabic editor (10 October 2026): in
(a) the owner's «ولا يُنشر منها إلا تقديرات تجميعية» drops «منها». Feminine «منها» cannot refer back to «ملف», and
attached to «فترات الثقة» it adds a "from them" the English does not carry. Without it the clause says exactly "only
aggregate estimates are published". Change (b) passed as given.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError  # noqa: E402

F = "RIGHTS-FINAL"
S03, ROW = "03_PAGE_SECTIONS", 363   # /rights/ section 6, "CauseWay's own content: CC BY 4.0"

SUBS = [
    # (a) facts only, EN
    (5, "the confidence intervals this resource derives from the Global Findex respondent file for Yemen (evidence record "
        "CLM-026) are computed under the World Bank Microdata Research License, which permits publishing aggregate "
        "statistics with the data cited.",
        "the confidence intervals this resource derives from the Global Findex respondent file for Yemen (evidence record "
        "CLM-026) are computed from a file CauseWay obtained under the World Bank Microdata Research License; only "
        "aggregate estimates are published, never respondent-level data."),
    # (a) facts only, AR
    (7, "تُحتسب فترات الثقة التي يستخرجها هذا المورد من ملف المستجيبين في مسح Global Findex لليمن (سجل الدليل CLM-026) "
        "بموجب رخصة البحث للبيانات الجزئية لدى البنك الدولي، التي تجيز نشر الإحصاءات التجميعية مع الاستشهاد بالبيانات.",
        "فترات الثقة التي يستخرجها هذا المورد من ملف المستجيبين في مسح Global Findex لليمن (سجل الدليل CLM-026) محسوبة "
        "من ملف حصلت عليه CauseWay بموجب رخصة البحث للبيانات الجزئية لدى البنك الدولي؛ ولا يُنشر إلا تقديرات تجميعية، "
        "ولا تُنشر أي بيانات على مستوى المستجيبين."),
    # (b) after the "Covered:" list, EN
    (5, "when they are published. Not covered:",
        "when they are published. For figures CauseWay calculates from other publishers' data, the licence covers "
        "CauseWay's calculation and presentation; the underlying data stay under their publishers' terms. Not covered:"),
    # (b) after the "Covered:" list, AR
    (7, "وشروحها عند نشرها. ولا تشمل الرخصة:",
        "وشروحها عند نشرها. وفي الأرقام التي تحتسبها CauseWay من بيانات جهات أخرى، تشمل الرخصة عملية الاحتساب وطريقة "
        "العرض، وتبقى البيانات الأصلية خاضعة لشروط ناشريها. ولا تشمل الرخصة:"),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for col, old, new in SUBS:
        s.replace(F, S03, ROW, col, old, new, f"{S03}!r{ROW}c{col}")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "RIGHTS-FINAL"),
        ("summary", "/rights/ section 6: the microdata sentence states facts only; the licence's reach over figures "
                    "CauseWay calculates from other publishers' data")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
