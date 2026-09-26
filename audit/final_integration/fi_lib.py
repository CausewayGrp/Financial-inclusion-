# -*- coding: utf-8 -*-
"""Helpers for the final-integration transactions (directive D7). Extends audit/tranche_c/tc_lib (unchanged lineage)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402,F401


def ui_rows(s):
    """{ui_id: row} of the 04 governed interface-copy block, located by its end marker (the 'Trust navigation' block),
    with no fixed row limit (the block grew past 300 rows in R85-A)."""
    g04 = s.grid("04_NAV_UX")
    end = next(i for i, x in enumerate(g04, 1) if x and x[0] == "Trust navigation")
    ui = {x[0]: i for i, x in enumerate(g04, 1) if i < end and x and isinstance(x[0], str) and x[0].startswith("UI-")}
    return ui, end


def set_ui(s, finding, ui_id, label_en, label_ar):
    ui, _ = ui_rows(s)
    if ui_id not in ui:
        raise TxError(f"{finding}: 04 has no {ui_id}")
    row = ui[ui_id]
    if label_en is not None:
        s.set(finding, "04_NAV_UX", row, 2, label_en, s.ed.get_value("04_NAV_UX", row, 2), f"{ui_id}.label_en")
    if label_ar is not None:
        s.set(finding, "04_NAV_UX", row, 3, label_ar, s.ed.get_value("04_NAV_UX", row, 3), f"{ui_id}.label_ar")


def insert_ui(s, finding, rows):
    """Append (ui_id, label_en, label_ar, use_rule) rows at the end of the 04 interface-copy block."""
    ui, end = ui_rows(s)
    last = max(ui.values())
    for r in rows:
        if r[0] in ui:
            raise TxError(f"{finding}: 04 already has {r[0]}")
    s.ed.insert_rows("04_NAV_UX", last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in rows])
    for a, b, c, _ in rows:
        s.ledger.append({"finding": finding, "sheet": "04_NAV_UX", "row": None, "col": None, "field": a, "old": None, "new": b + " || " + c})
