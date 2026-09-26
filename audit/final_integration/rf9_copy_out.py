# -*- coding: utf-8 -*-
"""Transaction RF9 — the last interface words held in code (F9 clean-room finding M8).

  python3 rf9_copy_out.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The language switch in scripts/build.py carried its visible name and its accessible name as literals. They move,
unchanged in wording, into the Master's governed interface copy (04). Each label is written in the language it switches
to and is rendered with that language (ui_text(<id>, other_lang)): the Arabic page shows the English label, the English
page the Arabic one. The rendered site is byte-identical before and after.
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, TxError  # noqa: E402

ROWS = [
    ("UI-LANG-SWITCH-NAME", "EN", "العربية",
     "Language switch, visible name of the other edition. Written in the language it switches to and rendered with that language (build.py header)."),
    ("UI-LANG-SWITCH-ACTION", "Switch to English", "التبديل إلى العربية",
     "Language switch, accessible name. Written in the language it switches to and rendered with that language (build.py header)."),
]


def insert_ui_rows(s, finding, rows):
    """Append rows to the end of the 04 interface-copy block, which ends one blank row before 'Trust navigation'.
    (tc_lib.insert_ui_rows assumes the block ends before row 300; since R8.5 it runs to row 487.)"""
    g04 = s.grid("04_NAV_UX")
    trust = [i for i, x in enumerate(g04, 1) if x and x[0] == "Trust navigation"]
    if len(trust) != 1:
        raise TxError("04: expected exactly one 'Trust navigation' row")
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-") and i < trust[0]}
    last = max(ui.values())
    if last != trust[0] - 2 or any(c not in (None, "") for c in g04[last]):
        raise TxError("04: interface-copy block end not where expected")
    for r in rows:
        if r[0] in ui:
            raise TxError(f"{finding}: 04 already has {r[0]}")
    s.ed.insert_rows("04_NAV_UX", last + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in rows])
    for a, b, c, _ in rows:
        s.ledger.append(OrderedDict([("finding", finding), ("sheet", "04_NAV_UX"), ("row", last + 1), ("col", None), ("field", a),
                                     ("old", None), ("new", b + " || " + c)]))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, "RF9:COPY-OUT", ROWS)
    rep = s.save(out, ledger, {"transaction": "RF9", "summary": "Language-switch labels moved out of build.py into 04 (wording unchanged)"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
