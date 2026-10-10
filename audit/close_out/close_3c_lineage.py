# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-3C-L: the lineage of the visuals CLOSE-3C added (brief v5 W3c, U4 and U5).

  python3 close_3c_lineage.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

CLOSE-3C named a sheet, not records, in the data_inputs of VIS-CBY-MONETARY-SNAPSHOT and VIS-YER-MARKET-RATE: the
lineage projection (scripts/projection/derived.py, public object-source closure) read the first as a composite whose
members are not listed and the second as SOURCE_NOT_YET_BOUND, the only visual in that state. Each now names first the
Evidence Records whose sources bind its rows — CBY-BANKS-2026-05 (the bank balance sheet, Issue No. 54 and 55 values)
and CLM-033 (whose value states carry the market rates and the 2025 episode), both closed to SRC-CBY-001 — and then the
rows themselves in words, which the lineage reader does not take as an identifier. RV-CWR-011 takes its lineage from
Reading CWR-011 and names the same record. Only the three 11_VISUAL_LIBRARY cells change.
"""
import os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts  # noqa: E402

F = "CLOSE-3C-L"
DATA_INPUTS = OrderedDict([   # visual -> (CLOSE-3C value, value naming the bound records first)
    ("VIS-CBY-MONETARY-SNAPSHOT",
     ("18_CBY_MONETARY: market rate, M2, currency in circulation share, FX deposit share, bank total assets, foreign assets, "
      "private credit, loans and advances to government (end of 2025 and June 2026)",
      "CBY-BANKS-2026-05 + CLM-033 + rows of 18_CBY_MONETARY: market rate, M2, currency in circulation share, FX deposit "
      "share, bank total assets, foreign assets, private credit, loans and advances to government (end of 2025 and June "
      "2026)")),
    ("VIS-YER-MARKET-RATE",
     ("18_CBY_MONETARY YER_USD_MARKET_RATE (Table 6)",
      "CLM-033 + rows of 18_CBY_MONETARY YER_USD_MARKET_RATE (Table 6)")),
    ("RV-CWR-011",
     ("18_CBY_MONETARY T4: the CBY-BANKS-2026-05 rows and the June 2026 rows (Issue No. 55)",
      "CBY-BANKS-2026-05 + rows of 18_CBY_MONETARY T4: the CBY-BANKS-2026-05 rows and the June 2026 rows (Issue No. 55)")),
])


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t11 = Table(s, "11_VISUAL_LIBRARY")
    for vid, (old, new) in DATA_INPUTS.items():
        if not t11.set(F, vid, "data_inputs", new, old):
            raise TxError(f"{F}: {vid}.data_inputs already holds the new value")
    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "The three visuals CLOSE-3C added name the Evidence Records that bind their rows (CBY-BANKS-2026-05, "
                    "CLM-033) in data_inputs, so their lineage closes to SRC-CBY-001."),
        ("self_counts", counts)]))
    print({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")})


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
