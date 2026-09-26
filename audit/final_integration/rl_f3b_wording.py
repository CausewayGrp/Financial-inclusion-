# -*- coding: utf-8 -*-
"""Transaction RL-F3b — narrows one phrase of the RL-F3 card: the authors are affiliated with Al-Amal Microfinance Bank;
"staff of a regulated microfinance bank" asserted an employment and a regulatory status the card does not verify.

  python3 rl_f3b_wording.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402

SID = "SRC-AMB-MFB-SUPERVISION-2026"
EDITS = [("does_not_establish", "A proposal written by staff of a regulated microfinance bank:", "A proposal by authors from a microfinance bank:"),
         ("does_not_establish_ar", "مقترح كتبه موظفون في بنك تمويل أصغر خاضع للرقابة:", "مقترح أعده مؤلفون من بنك للتمويل الأصغر:")]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t = Table(s, "15_SOURCE_LIBRARY")
    for fld, old, new in EDITS:
        cur = t.get(SID, fld)
        if cur.count(old) != 1:
            raise TxError(f"{fld}: guard not found")
        t.set("RL-F3b", SID, fld, cur.replace(old, new), cur)
    rep = s.save(out, ledger, {"transaction": "RL-F3b", "summary": "F3 card: authorship stated as verified (authors from Al-Amal Microfinance Bank)"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
