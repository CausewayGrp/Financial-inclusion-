# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-2: one display precision for every Global Findex figure (candidate b).

  python3 e2_2_findex_precision.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding R-11 (independent review of 70398d1; X-ESC-D3-03b): the 2021-wave subgroup shares printed to two decimals
(18.35%, 5.44%, 12.91 points) from a sample of 1,000 adults, with no interval. The two decimals were this resource's
choice, not the source's. The rule decided here, applied to every Findex figure at once:

  Every Global Findex share is printed to one decimal place, rounded from the World Bank's unrounded value; a gap
  between two groups is the difference of the two printed shares.

Why one decimal: it is the precision at which the World Bank's own Yemen table publishes these values (The Little Data
Book on Financial Inclusion 2015, p. 159, read on 4 October 2026: "All adults 6.4 … Women 1.7 … All adults, 2011
3.7"), and the precision of every 2011 and 2014 value the Master already holds. Whole points would be more modest, but
would break the match with the World Bank's tables a reader verifies against, and would print the 2014 values 0.4% and
0.0% as 0%, which reads as "nobody" (missing ≠ zero). More than one decimal claims a precision a sample of 1,000 does
not have. Intervals: the World Bank publishes none for Yemen's 2022 survey (its 2025 methodology table covers the 2024
surveys; Yemen was not surveyed), and the microdata (microdata.worldbank.org, catalog 5862) needs a login, so no
interval is computed here; the existing limitations already say so. Owner input: the microdata file (see the log).

Unrounded values, Global Findex Database 2025 (GlobalFindexDatabase2025.csv, account_t_d, YEM 2022, read on
4 October 2026): women 0.0543631, men 0.1834518, primary or less 0.0698166, secondary or more 0.1952705, ages 15-24
0.0500996, ages 25+ 0.1610805, poorest 40% 0.0650494, richest 60% 0.1549671, all 0.1190337. Rounded: 5.4, 18.3 (not
18.4: the Master's 18.35 was itself a rounding of 18.345), 7.0, 19.5, 5.0, 16.1, 6.5, 15.5, 11.9. Gaps of the printed
shares: 12.9, 12.5, 11.1, 9.0 — each equal to the rounded unrounded gap (12.909, 12.545 → 12.5, 11.098, 8.995 → 9.0).
"""
import json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-2:R-11"
TOKENS = OrderedDict([("18.35", "18.3"), ("5.44", "5.4"), ("12.91", "12.9"), ("6.98", "7.0"), ("19.53", "19.5"),
                      ("12.55", "12.5"), ("5.01", "5.0"), ("16.11", "16.1"), ("11.10", "11.1")])
TOK_RX = re.compile(r"(?<![\d.,])(" + "|".join(re.escape(t) for t in TOKENS) + r")(?![\d]|[.,]\d)")
# Every public-text sheet that holds one of the tokens (found by a full scan on 4 October 2026). 33_ANALYTICS_MASTER is
# an internal analysis register that reaches no page; it is left as lineage.
TEXT_SHEETS = ("02_SITE_MAP", "03_PAGE_SECTIONS", "06_EVIDENCE_OBJECTS", "10_MEASUREMENT_AGENDA", "11_VISUAL_LIBRARY")
VALUES = {"WB-FINDEX-OBS-2022-002": (5.44, 5.4), "WB-FINDEX-OBS-2022-003": (18.35, 18.3),
          "WB-FINDEX-OBS-2022-006": (6.98, 7.0), "WB-FINDEX-OBS-2022-007": (19.53, 19.5),
          "WB-FINDEX-OBS-2022-008": (5.01, 5.0), "WB-FINDEX-OBS-2022-009": (16.11, 16.1)}
EXPECTED_CELLS = 31   # text cells holding at least one token (scan of 4 October 2026)

METH_EN = ("A derived value, such as the difference between two percentages, keeps the precision of its inputs, with no "
           "added decimal places, and small differences between estimates are not read as a ranking.",
           "A derived value, such as the difference between two percentages, keeps the precision of its inputs, with no "
           "added decimal places, and small differences between estimates are not read as a ranking. Global Findex "
           "shares are printed to one decimal place, rounded from the World Bank's unrounded values, and a gap between "
           "two groups is the difference of the two printed shares. One decimal place is the precision of the World "
           "Bank's own published tables for Yemen; more would suggest a precision that a survey of about 1,000 adults "
           "does not have.")
METH_AR = ("وتحتفظ القيمة المشتقة، كالفرق بين نسبتين، بدقة مدخلاتها من دون منازل عشرية إضافية، ولا تُقرأ الفروق الطفيفة "
           "بين التقديرات على أنها ترتيب.",
           "وتحتفظ القيمة المشتقة، كالفرق بين نسبتين، بدقة مدخلاتها من دون منازل عشرية إضافية، ولا تُقرأ الفروق الطفيفة "
           "بين التقديرات على أنها ترتيب. وتُعرض نسب المؤشر العالمي للشمول المالي (Global Findex) بمنزلة عشرية واحدة، "
           "مقرّبةً من القيم غير المقرّبة لدى البنك الدولي، والفجوة بين فئتين هي الفرق بين النسبتين المعروضتين. والمنزلة "
           "العشرية الواحدة هي الدقة التي ينشر بها البنك الدولي نفسه جداوله الخاصة باليمن، وأي منازل إضافية توحي بدقة لا "
           "يملكها مسح لنحو 1,000 بالغ.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    n = 0
    for sheet in TEXT_SHEETS:
        g = s.grid(sheet)
        for ri, row in enumerate(g, 1):
            for ci, v in enumerate(row, 1):
                if isinstance(v, str) and TOK_RX.search(v):
                    new = TOK_RX.sub(lambda m: TOKENS[m.group(1)], v)
                    s.set(F, sheet, ri, ci, new, v, f"{row[0]}.c{ci}")
                    n += 1
    if n != EXPECTED_CELLS:
        raise TxError(f"expected {EXPECTED_CELLS} text cells, found {n}")
    t25 = Table(s, "25_FINDEX_BASELINE", 4)
    for key, (old, new) in VALUES.items():
        t25.set(F, key, "value", new, old)
    s.replace_section(F, "/methodology/", 7, "en", "body", *METH_EN)
    s.replace_section(F, "/methodology/", 7, "ar", "body", *METH_AR)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-2"), ("summary", "One display precision for every Global Findex figure: one decimal, from the World Bank's unrounded values")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
