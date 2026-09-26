# -*- coding: utf-8 -*-
"""P4-E — governed chart labels and locator form (Master-first; independent verification V-D5, V-D15).

  python3 p4e_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

V-D5  Every category, series, lane, unit, event and state value that a SIGNATURE or CORE_ANALYTICAL chart prints gets a
      bilingual governed label in 04 'Governed interface copy' (UI-VIS-CAT-*, UI-VIS-UNIT-*, UI-VIS-BASELINE), so that Design
      never authors chart text. The table is audit/pre_tranche_c/p4e_labels.py; the generator maps printed values to these
      labels through the controlled input and stops if a printed value has none.
V-D15 25_FINDEX_BASELINE: the income- and education-group locators gain the Yemen filter (?locations=YE) that the total,
      women and men locators already carry. The URL form is aligned; the pages were not re-fetched in this session.
"""
import sys
from collections import OrderedDict
from ptc_lib import Session, TxError
from projection.master_reader import Workbook
from p4e_labels import LABELS, BASELINE, namespaces

S04, S25 = "04_NAV_UX", "25_FINDEX_BASELINE"


def main():
    src, out, ledger, work = sys.argv[1:5]
    namespaces()                                  # table integrity (no duplicate raw value or UI id)
    s = Session(src, work)
    wb = Workbook(src)

    # ---- V-D15 Findex locators ------------------------------------------------------------------------------------
    g25 = wb.grid(S25)
    h25 = [str(x) if x is not None else None for x in g25[3]]
    cu = h25.index("source_url") + 1
    for oid in ("WB-FINDEX-OBS-2022-004", "WB-FINDEX-OBS-2022-005", "WB-FINDEX-OBS-2022-006"):
        r = next(i for i, x in enumerate(g25, 1) if x and x[0] == oid)
        cur = g25[r - 1][cu - 1]
        if not cur.startswith("https://data.worldbank.org/indicator/") or "?" in cur:
            raise TxError(f"{oid}: unexpected locator {cur!r}")
        s.set("V-D15", S25, r, cu, cur + "?locations=YE", cur, f"{oid}.source_url")

    # ---- V-D5 labels (row insertion last) ---------------------------------------------------------------------------
    g04 = wb.grid(S04)
    ids = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    last = max(i for u, i in ids.items() if i < 140)
    if any(c not in (None, "") for c in g04[last]) or g04[last + 1][0] != "Trust navigation":
        raise TxError("04: interface-copy block end not where expected")
    rows = []
    for ns, raw, uid, en, ar in LABELS:
        if uid in ids:
            raise TxError(f"04: {uid} exists")
        rows.append({1: uid, 2: en, 3: ar, 4: f"Pre-Tranche-C P4 (V-D5). Chart label: {ns} value '{raw}'."})
    uid, en, ar = BASELINE
    rows.append({1: uid, 2: en, 3: ar, 4: "Pre-Tranche-C P4 (V-D5). Visual grammar: the starting value of a target/result comparison."})
    s.ed.insert_rows(S04, last + 1, rows)
    for r in rows:
        s.ledger.append(OrderedDict([("finding", "V-D5"), ("sheet", S04), ("row", None), ("col", None), ("field", r[1]), ("old", None),
                                     ("new", r[2] + " || " + r[3])]))
    rep = s.save(out, ledger, [("transaction", "P4-E"), ("scope", "Governed chart labels (V-D5); Findex locator form (V-D15)"),
                               ("labels_added", len(rows))])
    print(f"P4-E staged: {rep['cells_written']} changes ({len(rows)} labels); Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
