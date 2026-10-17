# -*- coding: utf-8 -*-
"""STAGE-A-RESIDUE: the Appendix 2 content defects of the takeover brief of 17 October 2026 (OD-1017-12), EN and AR together.

Every write is an exact-value-guarded substring replacement (or a whole-cell write guarded by the old value), read from
CELL_PLAN.json beside this script, so the transaction fails loudly if a cell has moved on. Arguments as for every
close-out transaction: input Master, staged Master, ledger path, scratch directory.

  PYTHONDONTWRITEBYTECODE=1 python3 audit/stage_a_residue/stage_a_residue.py \
      authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx "$STAGE/master.xlsx" "$STAGE/ledger.json" "$STAGE/work"

Plan entry kinds:
  {"kind": "replace", "finding", "sheet", "key", "field", "old", "new", "header_row"?}   one occurrence of old -> new
  {"kind": "set",     "finding", "sheet", "key", "field", "old", "new", "header_row"?}   whole cell, old guarded
  {"kind": "cell",    "finding", "sheet", "row", "col", "old", "new"}                     by position (03/02 rows), substring
  {"kind": "ui",      "finding", "ui_id", "old_en", "new_en", "old_ar", "new_ar"}         04 interface copy label
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "close_out"))
sys.path.insert(0, str(HERE.parent / "tranche_c"))
from close_lib import Session, TxError, refresh_self_counts, set_ui  # noqa: E402
from tc_lib import Table  # noqa: E402

TX = "STAGE-A-RESIDUE"
EXPECT_INPUT = "620f3368eaf34b100418410928df3a779c6e5fed180711593dc7122099930637"


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != EXPECT_INPUT:
        raise TxError(f"{TX}: unexpected Production Master; inspect/replay against the current Master, never merge the binary")
    s = Session(src, work)
    plan = json.loads((HERE / "CELL_PLAN.json").read_text(encoding="utf-8"))
    tables = {}
    for e in plan:
        finding = f"{TX}:{e['finding']}"
        kind = e["kind"]
        if kind in ("replace", "set"):
            key = (e["sheet"], e.get("header_row", 4))
            if key not in tables:
                tables[key] = Table(s, e["sheet"], e.get("header_row", 4))
            t = tables[key]
            if e["key"] not in t.rows:
                raise TxError(f"{finding}: {e['sheet']} has no row {e['key']}")
            row, col = t.rows[e["key"]], t.col(e["field"])
            if kind == "replace":
                s.replace(finding, e["sheet"], row, col, e["old"], e["new"], f"{e['key']}.{e['field']}")
            else:
                s.set(finding, e["sheet"], row, col, e["new"], e["old"], f"{e['key']}.{e['field']}")
        elif kind == "cell":
            s.replace(finding, e["sheet"], e["row"], e["col"], e["old"], e["new"], f"{e['sheet']}!r{e['row']}c{e['col']}")
        elif kind == "ui":
            set_ui(s, finding, e["ui_id"], e["new_en"], e["new_ar"], e["old_en"], e["old_ar"])
        else:
            raise TxError(f"{finding}: unknown plan kind {kind!r}")
    counts = refresh_self_counts(s, f"{TX}:self-counts")
    rep = s.save(out, ledger, {
        "transaction": TX,
        "decision": "audit/OWNER_DECISIONS_2026-10-17.md OD-1017-12; audit/close_out/TAKEOVER_BRIEF_2026-10-17.md Appendix 2",
        "summary": "Stage A residue: programme attribution of the 45,460 count (item 1); Findex digital-payment Arabic "
                   "(item 2); CWR-012 stray conjunction (item 3); reforms exhibition event label no longer implies operation "
                   "(item 4); CLM-006 universe names the filtered denominator (item 5); one month-on-month rule for the POS "
                   "series, May 2026 derived like January (item 6); methodology states what is bound and what is computed "
                   "(item 7); terms describe the per-source reuse-terms state (item 8). Items 9, 10 and 16 recorded without "
                   "a Master change (audit/close_out/PROGRESS.md).",
        "self_counts": counts,
    })
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    main()
