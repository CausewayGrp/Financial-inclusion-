# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-14: the licensed-bank list's check date in the provider matrix (the re-read of
first-screen and drawn-figure numbers in their originals, 3 October 2026; ORIGINAL_SOURCE_VERIFICATION.md §8).

  python3 rc_14_bank_list_date.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The provider matrix (VIS-PROVIDER-OBSERVABILITY, on /providers/ and its record page) prints the bank row as
"26 · 2026-09-07", under "count from the official list, as dated in the record". The list in force (CBY-Aden's Arabic
file of July 2026, https://cby-ye.com/files/6a665add29feb.pdf) carries no printed date, and RC-8 re-read it on
3 October 2026. That is the date the row's own source title and the /providers/ lead print. RC-8 moved every "as checked
on 7 September 2026" in prose but missed this ISO-format field.

The count, 26, is unchanged. The universe count PUC-BANK-2026-01 and the 26 bank rows (PRV-BANK-001 … -026, whose
`current_state_as_of` is not printed) now carry 2026-10-03. Rows observed on 7 September 2026 for other lists
(exchange companies, microfinance members) keep that date, because it is theirs.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError  # noqa: E402

F = "RC-14:BANK-DATE"
OLD, NEW = "2026-09-07", "2026-10-03"


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g = s.grid("22_PROVIDERS_DATA")
    # the universe-count block, found by its row: its header is the nearest row above that is not a PUC-* row
    puc = [i for i, r in enumerate(g, 1) if r and r[0] == "PUC-BANK-2026-01"]
    if len(puc) != 1:
        raise TxError(f"{F}: PUC-BANK-2026-01 found {len(puc)} times")
    hdr = puc[0] - 1
    while g[hdr - 1] and str(g[hdr - 1][0] or "").startswith("PUC-"):
        hdr -= 1
    tpu = Table(s, "22_PROVIDERS_DATA", hdr)
    tpu.set(F, "PUC-BANK-2026-01", tpu.head[2], NEW, OLD)   # the block's date column (reference_state)
    t = Table(s, "22_PROVIDERS_DATA", 4)
    banks = [k for k in t.rows if str(k).startswith("PRV-BANK-")]
    if len(banks) != 26:
        raise TxError(f"{F}: {len(banks)} bank rows; expected 26")
    for k in banks:
        if t.get(k, "source_id") != "SRC-CBY-BANKLIST-AR-2026-001":
            raise TxError(f"{F}: {k} does not cite the 2026 bank list")
        t.set(F, k, "current_state_as_of", NEW, OLD)
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-14"), ("summary", "bank list check date in the provider matrix"),
                                           ("items", OrderedDict([("universe_count", 1), ("bank_rows", len(banks))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
