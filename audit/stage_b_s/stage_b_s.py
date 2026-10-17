# -*- coding: utf-8 -*-
"""STAGE-B-S: the Master-side copy of Stage B row B1 (W4 Appendix F S10, S11, S13; owner decisions D8 and OD-1017-04(b);
findings G0-F01, G0-F02, G0-F07, G0-F10; the Arabic prose routes; the visual-contract escalations of the G0 audit),
EN and AR together.

Every write is an exact-value-guarded substring replacement or a whole-cell write guarded by the old value, read from
CELL_PLAN.json beside this script, so the transaction fails loudly if a cell has moved on. Arguments as for every
close-out transaction: input Master, staged Master, ledger path, scratch directory.

  PYTHONDONTWRITEBYTECODE=1 python3 audit/stage_b_s/stage_b_s.py \
      authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx "$STAGE/master.xlsx" "$STAGE/ledger.json" "$STAGE/work"

Plan entry kinds (the first four as in audit/stage_a_residue/stage_a_residue.py):
  {"kind": "replace", "finding", "sheet", "key", "field", "old", "new", "header_row"?}   one occurrence of old -> new
  {"kind": "set",     "finding", "sheet", "key", "field", "old", "new", "header_row"?}   whole cell, old guarded
  {"kind": "cell",    "finding", "sheet", "row", "col", "old", "new"}                     by position (04/03 rows), substring
  {"kind": "ui",      "finding", "ui_id", "old_en", "new_en", "old_ar", "new_ar"}         04 interface copy label
  {"kind": "ui_insert",  "finding", "rows": [[ui_id, label_en, label_ar, use_rule], ...]}  appended to the 04 interface block
  {"kind": "row_insert", "finding", "sheet", "header_row"?, "values": {field: value}}      a keyed row appended to a table
  {"kind": "vs_add",     "finding", "sheet", "key", "add": [value-state entries]}          appended to a 06 value_states list
  {"kind": "list_add",   "finding", "sheet", "key", "field", "add": [ids], "form": "semi"|"json"}  ids appended to a list cell
Positional entries come before insertions in the plan, so no row number is read after a block has grown.
"""
import hashlib
import json
import sys
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "close_out"))
sys.path.insert(0, str(HERE.parent / "tranche_c"))
from close_lib import Session, TxError, insert_ui_rows, refresh_self_counts, set_ui  # noqa: E402  (close_lib finds the 04 block end; tc_lib's copy predates its growth)
from tc_lib import Table  # noqa: E402

TX = "STAGE-B-S"
EXPECT_INPUT = "d1807346021996866cb595cb5db89c2c575a2ec290d1727ce65ae6761a14f50b"


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != EXPECT_INPUT:
        raise TxError(f"{TX}: unexpected Production Master; inspect/replay against the current Master, never merge the binary")
    s = Session(src, work)
    plan = json.loads((HERE / "CELL_PLAN.json").read_text(encoding="utf-8"))
    tables = {}

    def table(sheet, hr):
        key = (sheet, hr)
        if key not in tables:
            tables[key] = Table(s, sheet, hr)
        return tables[key]

    seen_insert = set()
    for e in plan:
        finding = f"{TX}:{e['finding']}"
        kind = e["kind"]
        if kind in ("cell",) and e["sheet"] in seen_insert:
            raise TxError(f"{finding}: positional write after an insertion in {e['sheet']}")
        if kind in ("replace", "set"):
            t = table(e["sheet"], e.get("header_row", 4))
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
        elif kind == "ui_insert":
            insert_ui_rows(s, finding, [tuple(r) for r in e["rows"]])
            seen_insert.add("04_NAV_UX")
        elif kind == "row_insert":
            t = table(e["sheet"], e.get("header_row", 4))
            key = e["values"][t.head[0]]
            if key in t.rows:
                raise TxError(f"{finding}: {e['sheet']} already has {key}")
            last = max(t.rows.values())
            cols = {}
            for f, v in e["values"].items():
                cols[t.col(f)] = v
            s.ed.insert_rows(e["sheet"], last + 1, [cols])
            t.rows[key] = last + 1
            s.ledger.append(OrderedDict([("finding", finding), ("sheet", e["sheet"]), ("row", last + 1), ("col", None), ("field", key),
                                         ("old", None), ("new", json.dumps(e["values"], ensure_ascii=False))]))
            seen_insert.add(e["sheet"])
        elif kind == "vs_add":
            t = table(e["sheet"], e.get("header_row", 4))
            row, col = t.rows[e["key"]], t.col("value_states")
            cur = s.ed.get_value(e["sheet"], row, col)
            lst = json.loads(cur)
            have = {(x.get("t"), x.get("k")) for x in lst}
            for x in e["add"]:
                if (x.get("t"), x.get("k")) in have:
                    raise TxError(f"{finding}: {e['key']} value_states already binds {x.get('t')!r}")
                lst.append(x)
            s.set(finding, e["sheet"], row, col, json.dumps(lst, ensure_ascii=False, separators=(",", ":")), cur, f"{e['key']}.value_states")
        elif kind == "list_add":
            t = table(e["sheet"], e.get("header_row", 4))
            row, col = t.rows[e["key"]], t.col(e["field"])
            cur = s.ed.get_value(e["sheet"], row, col)
            if e["form"] == "json":
                lst = json.loads(cur or "[]")
                for x in e["add"]:
                    if x in lst:
                        raise TxError(f"{finding}: {e['key']}.{e['field']} already lists {x}")
                    lst.append(x)
                new = json.dumps(lst, ensure_ascii=False)
            else:
                parts = [x.strip() for x in str(cur or "").split(";") if x.strip()]
                for x in e["add"]:
                    if x in parts:
                        raise TxError(f"{finding}: {e['key']}.{e['field']} already lists {x}")
                    parts.append(x)
                new = "; ".join(parts)
            s.set(finding, e["sheet"], row, col, new, cur, f"{e['key']}.{e['field']}")
        else:
            raise TxError(f"{finding}: unknown plan kind {kind!r}")
    counts = refresh_self_counts(s, f"{TX}:self-counts")
    rep = s.save(out, ledger, {
        "transaction": TX,
        "decision": "audit/OWNER_DIRECTIVE_2026-10-17.md (Phase 2, B1); audit/OWNER_DECISIONS_2026-10-17.md D8, OD-1017-03, OD-1017-04(b), "
                    "OD-1017-08; audit/close_out/BRIEF.md Appendix F S10, S11, S13; design/DESIGN_INTEGRATION_V2.md G0-F01, G0-F02, G0-F07, G0-F10",
        "summary": "Stage B row B1, Master side: the masthead's fifth hub is Methodology and the hub numerals are retired (D8); "
                   "three domain H1s become short theses and the Arabic /access/ H1 matches its English (S11); fourteen "
                   "table-of-contents group labels (S10); three record periods in words (S13); CLM-001 states the survey, the "
                   "universe and the 2.8-point interval in its lead and binds the SDG 8.10.2 definition and its metadata source "
                   "(G0-F01, G0-F10, OD-1017-04(b)); MA-005 states that the SDG 8.10.1 series hold no Yemen value after 2015 and "
                   "binds its sources; the corrections empty state says what it means (G0-F02); the Sana'a coverage sentence on "
                   "/payments/ and /reforms/ (G0-F07); the People page named instead of its route in nine prose cells; the April "
                   "2026 POS observation carries the same internal-contradiction marker as its pair (G0 visual audit); the "
                   "firm-finance severity contract records its text-first form.",
        "self_counts": counts,
    })
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    main()
