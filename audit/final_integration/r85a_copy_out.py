# -*- coding: utf-8 -*-
"""Transaction R85-A — copy out of code (R8.5; AR-29, EN-09, TRUST-25).

  python3 r85a_copy_out.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Writes the bilingual interface copy that scripts/build.py and site-src/app.js held in code into the Master's governed
interface copy (04), unchanged in wording, and the Arabic Measurement Agenda domain labels (translated in code until
now) into a new 10 column domain_ar. Input: inputs/R85A_COPY_OUT_OF_CODE.json (produced by r85_copy_out_of_code.py and
r85_copy_out_of_app.py). The rendered site is the same text before and after; wording changes follow in R85-B.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError, insert_ui_rows  # noqa: E402


def main():
    src, out, ledger, work = sys.argv[1:5]
    data = json.load(open(os.path.join(HERE, "inputs", "R85A_COPY_OUT_OF_CODE.json"), encoding="utf-8"))
    s = Session(src, work)
    insert_ui_rows(s, "R85-A:COPY-OUT", [tuple(r) for r in data["interface_copy_rows"]])
    S10 = "10_MEASUREMENT_AGENDA"
    head = s.header(S10, 4)
    n = max(i for i, h in enumerate(head, 1) if h not in (None, ""))
    if "domain_ar" in head:
        raise TxError("10 already has domain_ar")
    s.set("R85-A:DOMAIN-AR", S10, 4, n + 1, "domain_ar", None, "10 header")
    t10 = Table(s, S10)
    dom = data["measurement_domain_ar"]
    if set(t10.rows) != set(dom):
        raise TxError("10 rows differ")
    for mid, (en, ar) in dom.items():
        if t10.get(mid, "domain") != en:
            raise TxError(f"{mid} domain changed")
        t10.set("R85-A:DOMAIN-AR", mid, "domain_ar", ar, None)
    rep = s.save(out, ledger, {"transaction": "R85-A", "summary": "Interface copy moved out of build.py/app.js into 04 (wording unchanged); 10 domain_ar"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
