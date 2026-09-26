# -*- coding: utf-8 -*-
"""Canonical, dependency-free reader for the Production Master workbook.

Reads authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx directly (zip + XML), without
openpyxl, so that the projection layer depends only on the Master bytes and the Python stdlib.

Typing follows the conventions the governed projections were built with:
  * t="s"   shared string            -> str
  * t="str" / t="inlineStr"          -> str (exact characters, no trimming)
  * t="b"                            -> bool
  * t="e"                            -> str (error literal, e.g. '#N/A')
  * numeric (t="n" or absent)        -> int when the stored literal has no '.', 'e' or 'E'; else float
No date conversion is applied (the Master stores dates as text or plain serial numbers).

Grid semantics: rows 1..max_row and columns 1..max_col, where max_row / max_col are the largest
row / column indices of any <c> element (including empty styled cells). Missing cells are None.
This reproduces openpyxl's iter_rows(values_only=True) exactly; tests assert it cell-for-cell.

Failure policy: any structural surprise raises MasterReadError. Nothing is skipped silently.
"""
import hashlib
import re
import zipfile
import xml.etree.ElementTree as ET

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
_M = "{%s}" % NS_MAIN
_CELL_REF = re.compile(r"^([A-Z]{1,3})([0-9]+)$")


class MasterReadError(Exception):
    """Raised when the workbook cannot be read unambiguously."""


def col_index(letters):
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n


def col_letters(idx):
    s = ""
    while idx:
        idx, r = divmod(idx - 1, 26)
        s = chr(65 + r) + s
    return s


def _cast_number(text):
    if text is None or text == "":
        return None
    try:
        if "." in text or "E" in text or "e" in text:
            return float(text)
        return int(text)
    except ValueError as exc:
        raise MasterReadError(f"non-numeric literal in numeric cell: {text!r}") from exc


def _text_of(el):
    """Concatenate all <t> descendants (rich-text runs included), preserving whitespace exactly."""
    return "".join(t.text or "" for t in el.iter(_M + "t"))


class Workbook:
    """Read-only view of the Production Master."""

    def __init__(self, path):
        self.path = path
        with open(path, "rb") as fh:
            self.raw = fh.read()
        self.sha256 = hashlib.sha256(self.raw).hexdigest()
        self._zip = zipfile.ZipFile(path)
        self._shared = self._load_shared_strings()
        self.sheet_names, self._sheet_parts = self._load_sheet_index()
        self._grids = {}

    # -- package ---------------------------------------------------------------------------
    def _read_xml(self, part):
        part = part.lstrip("/")
        try:
            return ET.fromstring(self._zip.read(part))
        except KeyError as exc:
            raise MasterReadError(f"missing workbook part: {part}") from exc

    def _load_shared_strings(self):
        names = self._zip.namelist()
        if "xl/sharedStrings.xml" not in names:
            return []
        root = self._read_xml("xl/sharedStrings.xml")
        return [_text_of(si) for si in root.findall(_M + "si")]

    def _load_sheet_index(self):
        wb = self._read_xml("xl/workbook.xml")
        rels = self._read_xml("xl/_rels/workbook.xml.rels")
        target = {}
        for rel in rels.findall("{%s}Relationship" % NS_PKG):
            t = rel.get("Target")
            if not t.startswith("/"):
                t = "xl/" + t
            target[rel.get("Id")] = t.lstrip("/")
        names, parts = [], {}
        sheets = wb.find(_M + "sheets")
        if sheets is None:
            raise MasterReadError("workbook has no <sheets>")
        for sh in sheets.findall(_M + "sheet"):
            name = sh.get("name")
            rid = sh.get("{%s}id" % NS_REL)
            if rid not in target:
                raise MasterReadError(f"sheet {name!r} relationship {rid!r} not found")
            if name in parts:
                raise MasterReadError(f"duplicate sheet name {name!r}")
            names.append(name)
            parts[name] = target[rid]
        return names, parts

    # -- cells -----------------------------------------------------------------------------
    def _cell_value(self, c, ref):
        t = c.get("t")
        v = c.find(_M + "v")
        if t == "inlineStr":
            is_ = c.find(_M + "is")
            return _text_of(is_) if is_ is not None else ""
        if v is None:
            if c.find(_M + "f") is not None:
                raise MasterReadError(f"{ref}: formula without cached value")
            return None
        text = v.text
        if t == "s":
            try:
                return self._shared[int(text)]
            except (ValueError, IndexError) as exc:
                raise MasterReadError(f"{ref}: bad shared-string index {text!r}") from exc
        if t in ("str",):
            return text if text is not None else ""
        if t == "b":
            return text == "1"
        if t == "e":
            return text
        if t in (None, "n"):
            return _cast_number(text)
        if t == "d":
            raise MasterReadError(f"{ref}: ISO date cell type not supported by the governed reader")
        raise MasterReadError(f"{ref}: unknown cell type {t!r}")

    def grid(self, name):
        """Return the full value grid of a sheet as a list of lists (row-major, 1-based semantics)."""
        if name in self._grids:
            return self._grids[name]
        if name not in self._sheet_parts:
            raise MasterReadError(f"unknown sheet {name!r}")
        root = self._read_xml(self._sheet_parts[name])
        data = root.find(_M + "sheetData")
        if data is None:
            raise MasterReadError(f"{name}: no sheetData")
        cells = {}
        max_r = max_c = 0
        next_r = 0
        for row in data.findall(_M + "row"):
            r_attr = row.get("r")
            r = int(r_attr) if r_attr else next_r + 1
            next_r = r
            next_c = 0
            for c in row.findall(_M + "c"):
                ref = c.get("r")
                if ref:
                    m = _CELL_REF.match(ref)
                    if not m:
                        raise MasterReadError(f"{name}: bad cell reference {ref!r}")
                    ci, ri = col_index(m.group(1)), int(m.group(2))
                    if ri != r:
                        raise MasterReadError(f"{name}: cell {ref} inside row {r}")
                else:
                    ci, ri = next_c + 1, r
                next_c = ci
                val = self._cell_value(c, f"{name}!{col_letters(ci)}{ri}")
                if (ri, ci) in cells:
                    raise MasterReadError(f"{name}: duplicate cell {col_letters(ci)}{ri}")
                cells[(ri, ci)] = val
                max_r, max_c = max(max_r, ri), max(max_c, ci)
        grid = [[None] * max_c for _ in range(max_r)]
        for (ri, ci), val in cells.items():
            grid[ri - 1][ci - 1] = val
        self._grids[name] = grid
        return grid
