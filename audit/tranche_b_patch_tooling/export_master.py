# -*- coding: utf-8 -*-
"""Read-only export of the Production Master to one JSON file per sheet (records keyed by header; _row = Excel row).
Usage: python3 export_master.py <Master.xlsx> <outdir>"""
import json, os, sys, openpyxl
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
wb = openpyxl.load_workbook(src, data_only=True)
index = {}
for ws in wb.worksheets:
    rows = list(ws.iter_rows(values_only=True))
    width = max((len(r) for r in rows), default=0)
    rows = [tuple(r) + (None,) * (width - len(r)) for r in rows]
    h = next(i for i, r in enumerate(rows[:6]) if sum(1 for c in r if c not in (None, "")) >= 3)
    cols = [str(c) if c not in (None, "") else f"col{j}" for j, c in enumerate(rows[h])]
    recs = []
    for i, r in enumerate(rows[h + 1:], start=h + 2):
        rec = {cols[j]: v for j, v in enumerate(r) if j < len(cols) and v not in (None, "")}
        if rec: recs.append({"_row": i, **rec})
    index[ws.title] = {"header_row": h + 1, "cols": cols, "n": len(recs)}
    json.dump(recs, open(f"{out}/{ws.title}.json", "w"), ensure_ascii=False, default=str)
json.dump(index, open(f"{out}/_index.json", "w"), ensure_ascii=False)
print("sheets:", len(index))
