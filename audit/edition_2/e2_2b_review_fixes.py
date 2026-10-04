# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-2b: the independent bilingual and statistical review of E2-2, folded in (same commit).

  python3 e2_2b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Findings (4 October 2026):
1. "about 9.0" / «نحو 9.0» / «يقارب 9.0»: under the rule a gap is exactly the difference of the printed shares
   (15.5 − 6.5 = 9.0), and the other three gaps carry no hedge; the hedge goes.
2. /methodology/ section 7: "the World Bank's own published tables for Yemen" rested on one table (the Little Data Book
   2015); the World Bank's database publishes unrounded values. And "more would suggest a precision that … does not
   have" implied one decimal is warranted, which a statistician would reject (about 500 respondents per group). The
   sentence now names the one table and says the decimal is a display convention, not a claim of accuracy.
3. Arabic: «نقطة» (singular) after a decimal value, as the chart caption and the other gaps print it.
Docstring of E2-2: the unrounded income gap is 8.992, not 8.995 (15.4967 − 6.5049); 9.0 holds. E2-2 is a historical
record and is not edited.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-2b:REVIEW"
SECTIONS = [
    ("/people/", 3, "en", "differ by about 9.0 percentage points", "differ by 9.0 percentage points"),
    ("/people/", 3, "ar", "(6.5%) نحو 9.0 نقاط مئوية", "(6.5%) 9.0 نقطة مئوية"),
    ("/people/", 4, "ar", "وفارق 9.0 نقاط بين فئتي الدخل", "وفارق 9.0 نقطة بين فئتي الدخل"),
    ("/readings/gender-gap-measured-causes-open/", 3, "en", "a gap of about 9.0 percentage points",
     "a gap of 9.0 percentage points"),
    ("/readings/gender-gap-measured-causes-open/", 3, "ar", "فجوة تقارب 9.0 نقاط مئوية", "فجوة قدرها 9.0 نقطة مئوية"),
]
CELLS = [
    ("06_EVIDENCE_OBJECTS", "VIS-FINDEX-GAPS", "summary_en", "a difference of about 9.0 percentage points",
     "a difference of 9.0 percentage points"),
    ("06_EVIDENCE_OBJECTS", "VIS-FINDEX-GAPS", "summary_ar", "بفارق يقارب 9.0 نقاط مئوية", "بفارق 9.0 نقطة مئوية"),
    ("11_VISUAL_LIBRARY", "VIS-FINDEX-GAPS", "accessible_summary_en", "a difference of about 9.0 percentage points",
     "a difference of 9.0 percentage points"),
    ("11_VISUAL_LIBRARY", "VIS-FINDEX-GAPS", "accessible_summary_ar", "بفارق يقارب 9.0 نقاط مئوية",
     "بفارق 9.0 نقطة مئوية"),
    ("10_MEASUREMENT_AGENDA", "MA-003", "current_evidence_en", "by about 9.0 percentage points",
     "by 9.0 percentage points"),
    ("10_MEASUREMENT_AGENDA", "MA-003", "current_evidence_ar", "بنحو 9.0 نقاط مئوية", "بمقدار 9.0 نقطة مئوية"),
]
METH = [
    ("en", "One decimal place is the precision of the World Bank's own published tables for Yemen; more would suggest a "
           "precision that a survey of about 1,000 adults does not have.",
     "One decimal place matches the World Bank's own country table for Yemen in The Little Data Book on Financial "
     "Inclusion 2015. It is a display convention, not a claim of accuracy to a tenth of a point: with a sample of about "
     "1,000 adults, and fewer in each group, sampling error is far larger than that."),
    ("ar", "والمنزلة العشرية الواحدة هي الدقة التي ينشر بها البنك الدولي نفسه جداوله الخاصة باليمن، وأي منازل إضافية "
           "توحي بدقة لا يملكها مسح لنحو 1,000 بالغ.",
     "وتطابق المنزلة العشرية الواحدة جدول البنك الدولي نفسه الخاص باليمن في كتيّب البيانات الموجز عن الشمول المالي "
     "(The Little Data Book on Financial Inclusion) لعام 2015. وهي اصطلاح في العرض، لا ادعاء بدقة تبلغ عُشر النقطة؛ ففي "
     "عينة من نحو 1,000 بالغ، وبعدد أقل في كل فئة، يتجاوز خطأ المعاينة ذلك بكثير."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for route, order, lang, old, new in SECTIONS:
        s.replace_section(F, route, order, lang, "body", old, new)
    tabs = {}
    for sheet, key, field, old, new in CELLS:
        t = tabs.setdefault(sheet, Table(s, sheet, 4))
        s.replace(F, sheet, t.rows[key], t.col(field), old, new, f"{key}.{field}")
    for lang, old, new in METH:
        s.replace_section(F, "/methodology/", 7, lang, "body", old, new)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-2b"), ("summary", "E2-2 review fixes: no hedge on an exact gap; the precision sentence names its one table and calls itself a convention; Arabic singular after a decimal")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
