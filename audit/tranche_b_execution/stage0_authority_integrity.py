# -*- coding: utf-8 -*-
"""Stage 0 — authority integrity restoration AIR-001 (before any Tranche B patch root).

Finding AUTH-INT-001: 14_SYSTEM_CHRONOLOGY rows 18–28 of the entry Master are eleven identical copies of YSC-013;
YSC-014…YSC-023 are missing, and YSC-024 system_implication_en holds Arabic text. The manifest-certified projection
site-src/content/visuals/system_chronology.json (SHA-256 8d058126… in SHA256SUMS.txt at entry) holds the last
governed state of every event. This script restores the Master rows from that projection, Master-first:
  * rows 19–28 := YSC-014, 015, 016, 017, 018, 019, 021, 022, 023, 020 (the certified projection's order);
  * row 17 (YSC-024) system_implication_en / _ar := certified projection values.
Every write checks the exact current cell value; any mismatch aborts without writing.

  python3 stage0_authority_integrity.py <entry_master.xlsx> <certified_chronology.json> <out_master.xlsx> <ledger.json>
"""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from projection.master_reader import Workbook               # noqa: E402
from projection.master_writer import MasterEditor           # noqa: E402

ENTRY_MASTER_SHA = "e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7"
CERTIFIED_CHRONO_SHA = "8d058126762ab67dd0e74a6d91c28bc669193fe3b28379afdf45668b6e9ec2c6"
SHEET = "14_SYSTEM_CHRONOLOGY"


def main():
    master, chrono, out, ledger = sys.argv[1:5]
    if hashlib.sha256(open(master, "rb").read()).hexdigest() != ENTRY_MASTER_SHA:
        sys.exit("entry Master hash mismatch — refusing")
    if hashlib.sha256(open(chrono, "rb").read()).hexdigest() != CERTIFIED_CHRONO_SHA:
        sys.exit("certified chronology projection hash mismatch — refusing")
    cert = {r["event_id"]: r for r in json.load(open(chrono, encoding="utf-8"))}
    wb = Workbook(master)
    grid = wb.grid(SHEET)
    header = grid[3]
    cols = {h: j + 1 for j, h in enumerate(header) if h}
    ed = MasterEditor(master)
    rows = []
    plan = list(zip(range(19, 29), ["YSC-014", "YSC-015", "YSC-016", "YSC-017", "YSC-018", "YSC-019", "YSC-021", "YSC-022", "YSC-023", "YSC-020"]))
    for r, eid in plan:
        cur = grid[r - 1]
        if cur[0] != "YSC-013":
            sys.exit(f"row {r}: expected corrupted duplicate YSC-013, found {cur[0]!r}")
        rec = cert[eid]
        for h, c in cols.items():
            new = rec.get(h)
            old = cur[c - 1]
            if (old or None) != (new or None):
                ed.set_cell(SHEET, r, c, new, expect=old)
        rows.append({"row": r, "restored_event_id": eid})
    r17 = grid[16]
    if r17[0] != "YSC-024":
        sys.exit("row 17 is not YSC-024")
    for h in ("system_implication_en", "system_implication_ar"):
        ed.set_cell(SHEET, 17, cols[h], cert["YSC-024"][h], expect=r17[cols[h] - 1])
    data = ed.save(out)
    # verification
    after = Workbook(out)
    ok_sheet = True
    for i, r in enumerate(after.grid(SHEET)[4:], start=5):
        if r[0] in cert:
            for h, c in cols.items():
                if (r[c - 1] or None) != (cert[r[0]].get(h) or None):
                    ok_sheet = False
    ids = [r[0] for r in after.grid(SHEET)[4:] if r[0]]
    others = all(wb.grid(n) == after.grid(n) for n in wb.sheet_names if n != SHEET)
    rep = {"root": "AIR-001", "finding": "AUTH-INT-001", "sheet": SHEET, "entry_master_sha256": ENTRY_MASTER_SHA,
           "certified_projection_sha256": CERTIFIED_CHRONO_SHA, "rows_restored": rows,
           "cells_written": len(ed.log), "row17_fields": ["system_implication_en", "system_implication_ar"],
           "verification": {"sheet_equals_certified_projection": ok_sheet, "event_ids_unique": len(ids) == len(set(ids)),
                            "event_count": len(ids), "other_sheets_unchanged": others},
           "output_master_sha256": hashlib.sha256(data).hexdigest()}
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(rep["verification"]), rep["output_master_sha256"])
    if not (ok_sheet and others and len(ids) == len(set(ids)) == 24):
        sys.exit("AIR-001 verification FAILED")


if __name__ == "__main__":
    main()
