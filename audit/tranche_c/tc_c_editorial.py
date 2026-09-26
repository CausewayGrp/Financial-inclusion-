# -*- coding: utf-8 -*-
"""Tranche C transaction TC-C — Arabic and English editorial acceptance of the Master sheets that own page text.

  python3 tc_c_editorial.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Input: audit/tranche_c/inputs/TC-C_editorial.json — final cell values (02, 03 except Evidence Record routes, 04, 05, 08,
10, 13, 14), each written only if the cell still holds its recorded 'old' value. Scope and dropped edits are listed in the
input ('dropped': Evidence Record routes and derived 02 cells, owned by 06/08 since TC-S1; 'superseded': edits already
made by TC-A).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, TxError, norm  # noqa: E402


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    data = json.load(open(os.path.join(HERE, "inputs", "TC-C_editorial.json"), encoding="utf-8"))
    for c in data["cells"]:
        cur = s.ed.get_value(c["sheet"], c["row"], c["col"])
        if norm(cur) != norm(c["old"]):
            raise TxError(f"{c['sheet']} r{c['row']}c{c['col']} {c['stable_key']}: holds {norm(cur)[:80]!r}")
        s.set("TC-C:" + ";".join(c["findings"])[:60], c["sheet"], c["row"], c["col"], c["new"], cur, "/".join(str(x) for x in c["stable_key"]))
    rep = s.save(out, ledger, {"transaction": "TC-C", "input": "audit/tranche_c/inputs/TC-C_editorial.json",
                              "summary": "AR/EN editorial sweep; AR mirrors; meaning mismatches resolved; Measurement field lists"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
