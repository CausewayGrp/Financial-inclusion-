# -*- coding: utf-8 -*-
"""STAGE-B-T: the governed interface labels the Stage B tools need (B2 T, 17 October 2026) — the structured
report-an-error form on /contact/#report, the citation formats of OD-1017-04(a), the Compare verdict reason and
summary (SIG-5), the search zero-result help and the /corrections/ process link — EN and AR together. Same plan
grammar and session API as audit/stage_b_s2/stage_b_s2.py (only `ui_insert` is used).

  PYTHONDONTWRITEBYTECODE=1 python3 audit/stage_b_t/stage_b_t.py \
      authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx "$STAGE/master.xlsx" "$STAGE/ledger.json" "$STAGE/work"
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "close_out"))
from close_lib import Session, TxError, insert_ui_rows, refresh_self_counts  # noqa: E402

TX = "STAGE-B-T"
EXPECT_INPUT = "6a851a14909ebe925c71ada64765f9018c7a204b0e72742efc928c1b88b51260"


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != EXPECT_INPUT:
        raise TxError(f"{TX}: unexpected Production Master; inspect/replay against the current Master, never merge the binary")
    s = Session(src, work)
    plan = json.loads((HERE / "CELL_PLAN.json").read_text(encoding="utf-8"))
    n = 0
    for e in plan:
        finding = f"{TX}:{e['finding']}"
        if e["kind"] == "ui_insert":
            insert_ui_rows(s, finding, [tuple(r) for r in e["rows"]])
            n += len(e["rows"])
        else:
            raise TxError(f"{finding}: unknown plan kind {e['kind']!r}")
    counts = refresh_self_counts(s, f"{TX}:self-counts")
    rep = s.save(out, ledger, {
        "transaction": TX,
        "decision": "audit/OWNER_DIRECTIVE_2026-10-17.md (Phase 2, B2 T); takeover brief Part 6 items 16 and 17; OD-1017-04(a); "
                    "BRIEF W4 T (search, Compare, source directory, report an error); design/DESIGN_INTEGRATION_V2.md §3",
        "summary": f"{n} interface labels (EN and AR): the structured report-an-error form on /contact/#report (fields, error types, actions, "
                   "validation and status messages, the no-JavaScript instruction), the citation format control and its runtime phrases "
                   "(plain text, APA 7, Chicago, BibTeX, RIS), the Compare verdict reason and copied summary, the search zero-result help "
                   "and the /corrections/ process-document link.",
        "self_counts": counts,
    })
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    main()
