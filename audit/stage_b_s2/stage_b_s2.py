# -*- coding: utf-8 -*-
"""STAGE-B-S2: the one governed label the F-15 first-click decision needs (DL-V2-007, 17 October 2026) — the heading of
Home's topics block and of the footer's topics group, EN and AR together. Same plan grammar and session API as
audit/stage_b_s/stage_b_s.py (only `ui_insert` is used here).

  PYTHONDONTWRITEBYTECODE=1 python3 audit/stage_b_s2/stage_b_s2.py \
      authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx "$STAGE/master.xlsx" "$STAGE/ledger.json" "$STAGE/work"
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "close_out"))
from close_lib import Session, TxError, insert_ui_rows, refresh_self_counts  # noqa: E402

TX = "STAGE-B-S2"
EXPECT_INPUT = "5b2004068c0c2cfd8aae0f7b3b1c2f2c53cab4609fbe9e9a53366d96f1323b20"


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != EXPECT_INPUT:
        raise TxError(f"{TX}: unexpected Production Master; inspect/replay against the current Master, never merge the binary")
    s = Session(src, work)
    plan = json.loads((HERE / "CELL_PLAN.json").read_text(encoding="utf-8"))
    for e in plan:
        finding = f"{TX}:{e['finding']}"
        if e["kind"] == "ui_insert":
            insert_ui_rows(s, finding, [tuple(r) for r in e["rows"]])
        else:
            raise TxError(f"{finding}: unknown plan kind {e['kind']!r}")
    counts = refresh_self_counts(s, f"{TX}:self-counts")
    rep = s.save(out, ledger, {
        "transaction": TX,
        "decision": "design/DESIGN_INTEGRATION_V2.md DL-V2-007 (17 October 2026): the F-15 first-click test; takeover brief Part 6 item 14; "
                    "audit/OWNER_DIRECTIVE_2026-10-17.md (Phase 2, B1)",
        "summary": "One interface label, UI-HOME-TOPICS (Topics / الموضوعات): the heading of Home's topics block and of the footer's topics "
                   "group, which give every reader a one-step route to the eight domain answers (first-click: 21-25% before, 92-100% after, "
                   "AI-simulated).",
        "self_counts": counts,
    })
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    main()
