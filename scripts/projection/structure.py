# -*- coding: utf-8 -*-
"""Sheet structure model for the Production Master: main header, titled sub-blocks, keyed records.

Conventions (as used by every governed projection since R4):
  * main header row  = first row among rows 1..6 with >= 3 non-empty cells;
  * a titled sub-block = a row whose only non-empty cell is column A, followed by a header row
    with >= 2 non-empty cells; the block's records run until the next titled sub-block or sheet end;
  * a keyed record   = a non-blank row inside a block, mapped header-label -> value
    (columns whose header is blank are named colN, N = 0-based column index).

StructureError is raised for anything that does not fit these conventions. Keyed projection
families additionally assert their declared column contract (see families.py).
"""
from .master_reader import MasterReadError


class StructureError(MasterReadError):
    pass


def _nonblank(v):
    return v not in (None, "")


def main_header_index(grid, sheet):
    for i, row in enumerate(grid[:6]):
        if sum(1 for c in row if _nonblank(c)) >= 3:
            return i
    raise StructureError(f"{sheet}: no header row (>=3 non-empty cells) in rows 1-6")


def header_labels(row):
    return [str(c) if _nonblank(c) else f"col{j}" for j, c in enumerate(row)]


def blocks(grid, sheet):
    """Return [{'title': str|None, 'title_row': int|None, 'header_row': int, 'first': int, 'last': int, 'labels': [...]}]
    with 1-based Excel row numbers. The first block is the main block (title None)."""
    h = main_header_index(grid, sheet)
    out = [{"title": None, "title_row": None, "header_row": h + 1, "labels": header_labels(grid[h]), "first": h + 2}]
    i = h + 1
    n = len(grid)
    while i < n:
        row = grid[i]
        only_a = _nonblank(row[0]) if row else False
        others = sum(1 for c in row[1:] if _nonblank(c))
        if only_a and others == 0 and i + 1 < n and sum(1 for c in grid[i + 1] if _nonblank(c)) >= 2:
            # A single-cell row followed by a header-like row starts a titled block only if the previous
            # row is blank (block separator). Otherwise it is a sparse data row of the current block.
            prev_blank = i > 0 and not any(_nonblank(c) for c in grid[i - 1])
            if prev_blank:
                out[-1]["last"] = i  # rows before the title row
                out.append({"title": str(row[0]), "title_row": i + 1, "header_row": i + 2,
                            "labels": header_labels(grid[i + 1]), "first": i + 3})
                i += 2
                continue
        i += 1
    out[-1]["last"] = n
    return out


def keyed_records(grid, sheet, block=None):
    """Records of one block (default: main block) as (excel_row, {label: value}) with blank rows skipped.
    Blank-labelled columns are dropped (they carry no governed field)."""
    bl = blocks(grid, sheet)
    b = bl[0] if block is None else next((x for x in bl if x["title"] == block), None)
    if b is None:
        raise StructureError(f"{sheet}: block {block!r} not found")
    labels_raw = grid[b["header_row"] - 1]
    out = []
    for r in range(b["first"], b["last"] + 1):
        row = grid[r - 1]
        if not any(_nonblank(c) for c in row):
            continue
        rec = {}
        for j, lab in enumerate(labels_raw):
            if _nonblank(lab):
                rec[str(lab)] = row[j] if j < len(row) else None
        out.append((r, rec))
    return out
