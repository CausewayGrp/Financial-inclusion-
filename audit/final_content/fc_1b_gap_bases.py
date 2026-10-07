# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-1b: the four difference rows state the two bases their interval rests on.

  python3 fc_1b_gap_bases.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-1b:FC-MOE-BASE. Gate FC-MOE, written with FC-1, requires every derivation row to state the base the
interval was computed on, and caught that the four gap rows (CW-FINDEX-MOE-2022-010 ... -013) did not. A margin of
error means nothing without its base, and a difference between two groups rests on two of them, so each row now names
both. The numbers are unchanged.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "FC-1b:FC-MOE-BASE"
S25 = "25_FINDEX_BASELINE"
OLD = ("The two groups are disjoint samples, so the standard error of the difference is the root of the sum of their "
       "squared standard errors.")
BASES = OrderedDict([
    ("CW-FINDEX-MOE-2022-010", "500 and 500 respondents"),
    ("CW-FINDEX-MOE-2022-011", "366 and 634 respondents"),
    ("CW-FINDEX-MOE-2022-012", "430 and 569 respondents"),
    ("CW-FINDEX-MOE-2022-013", "770 and 230 respondents"),
])


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t25 = Table(s, S25, 4)
    for key, base in BASES.items():
        if key not in t25.rows:
            raise TxError("%s has no row %s" % (S25, key))
        new = OLD + " The two bases are %s." % base
        s.replace(F, S25, t25.rows[key], t25.col("caveat"), OLD, new, key + ".caveat")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-1b"),
        ("summary", "Each of the four Findex difference derivations states the two bases its interval rests on "
                    "(gate FC-MOE)")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
