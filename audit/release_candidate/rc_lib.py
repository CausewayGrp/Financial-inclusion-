# -*- coding: utf-8 -*-
"""Shared helpers for the release-candidate transactions (RC-1 … RC-3).

audit/tranche_c/tc_lib.py locates the end of the 04 governed interface-copy block with a row bound (< 300) that held
at Tranche C; the block has since grown to row 489. These helpers find the block by its own structure instead — the
last UI-* row before the "Trust navigation" block title — and are otherwise identical. tc_lib.py is a historical
record and is not edited.
"""
import os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402,F401

S04 = "04_NAV_UX"


def ui_block_end(s):
    g04 = s.grid(S04)
    titles = [i for i, x in enumerate(g04, 1) if x and x[0] == "Trust navigation"]
    if len(titles) != 1:
        raise TxError(f"04: 'Trust navigation' title found {len(titles)} times")
    title = titles[0]
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-") and i < title}
    last = max(ui.values())
    if any(c not in (None, "") for c in g04[last]):   # the row after the last UI row is blank, then the title
        raise TxError("04: interface-copy block is not followed by a blank row")
    return last, ui


def insert_ui_rows(s, finding, rows):
    """rows: [(ui_id, label_en, label_ar, use_rule)] appended to the end of the 04 interface-copy block."""
    last, ui = ui_block_end(s)
    for r in rows:
        if r[0] in ui:
            raise TxError(f"{finding}: 04 already has {r[0]}")
    s.ed.insert_rows(S04, last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in rows])
    for a, b, c, _ in rows:
        s.ledger.append(OrderedDict([("finding", finding), ("sheet", S04), ("row", None), ("col", None), ("field", a),
                                     ("old", None), ("new", b + " || " + c)]))


def set_ui(s, finding, ui_id, label_en, label_ar, old_en, old_ar):
    _, ui = ui_block_end(s)
    if ui_id not in ui:
        raise TxError(f"{finding}: 04 has no {ui_id}")
    row = ui[ui_id]
    if label_en is not None:
        s.set(finding, S04, row, 2, label_en, old_en, f"{ui_id}.label_en")
    if label_ar is not None:
        s.set(finding, S04, row, 3, label_ar, old_ar, f"{ui_id}.label_ar")
