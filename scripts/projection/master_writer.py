# -*- coding: utf-8 -*-
"""Surgical, deterministic editor for the Production Master (Master-first corrections).

Edits are applied to the worksheet XML text only; every other part of the package (styles, theme,
drawing, charts, feature property bag, relationships) is copied byte-for-byte, and the zip is rebuilt
with the original entry order and entry metadata, so the same edits always produce the same bytes.

Supported operations (all fail loudly; nothing is fuzzy):
  set_cell(sheet, row, col, value, expect=None)       exact current-value check when expect is given
  replace_in_cell(sheet, row, col, old, new, count)   exact substring; occurrence count must match
  insert_rows(sheet, before_row, rows)                shifts rows, cell refs and merged ranges
  delete_rows(sheet, first, last)                     shifts rows, cell refs and merged ranges up (merges wholly inside are dropped)
  remove_sheet(sheet)                                 removes the part, relationship, content type and entry
Strings are written as t="str" inline values (the Master's own convention); numbers as t="n".
"""
import io
import re
import zipfile
from html import escape

from .master_reader import MasterReadError, col_index, col_letters

_ROW = re.compile(r'<x:row r="(\d+)"([^>]*)>(.*?)</x:row>|<x:row r="(\d+)"([^>]*)/>', re.S)
_CELL = re.compile(r'<x:c r="([A-Z]+)(\d+)"([^>]*?)(?:/>|>(.*?)</x:c>)', re.S)
_MERGE = re.compile(r'<x:mergeCell ref="([A-Z]+)(\d+):([A-Z]+)(\d+)" />')


class MasterWriteError(MasterReadError):
    pass


def _unescape(t):
    return t.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&")


def _cell_text(inner):
    m = re.search(r"<x:v>(.*?)</x:v>", inner or "", re.S)
    return _unescape(m.group(1)) if m else None


class MasterEditor:
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as fh:
            self.raw = fh.read()
        self.zin = zipfile.ZipFile(io.BytesIO(self.raw))
        self.parts = {i.filename: self.zin.read(i.filename) for i in self.zin.infolist()}
        wb = self.parts["xl/workbook.xml"].decode("utf-8-sig")
        rels = self.parts["xl/_rels/workbook.xml.rels"].decode("utf-8-sig")
        rid = {m.group(2): m.group(1).lstrip("/") for m in re.finditer(r'Target="([^"]+)" Id="([^"]+)"', rels)}
        self.sheet_part = {m.group(1): rid[m.group(2)] for m in re.finditer(r'<x:sheet name="([^"]+)" sheetId="\d+" r:id="([^"]+)"', wb)}
        self.sheet_rid = {m.group(1): m.group(2) for m in re.finditer(r'<x:sheet name="([^"]+)" sheetId="\d+" r:id="([^"]+)"', wb)}
        self._xml = {}
        self.log = []

    # ---------------------------------------------------------------------------- sheet text
    def _get(self, sheet):
        if sheet not in self.sheet_part:
            raise MasterWriteError(f"unknown sheet {sheet!r}")
        if sheet not in self._xml:
            self._xml[sheet] = self.parts[self.sheet_part[sheet]].decode("utf-8")
        return self._xml[sheet]

    def _put(self, sheet, text):
        self._xml[sheet] = text

    def _row_span(self, text, row):
        for m in _ROW.finditer(text):
            r = int(m.group(1) or m.group(4))
            if r == row:
                return m
        return None

    def get_value(self, sheet, row, col):
        text = self._get(sheet)
        m = self._row_span(text, row)
        if not m or m.group(4):
            return None
        for c in _CELL.finditer(m.group(3)):
            if col_index(c.group(1)) == col:
                return _cell_text(c.group(4))
        return None

    # ---------------------------------------------------------------------------- cell ops
    @staticmethod
    def _cell_xml(ref, style, value):
        s = f' s="{style}"' if style is not None else ""
        if value is None or value == "":
            return f'<x:c r="{ref}"{s} />'
        if isinstance(value, bool):
            return f'<x:c r="{ref}"{s} t="b"><x:v>{int(value)}</x:v></x:c>'
        if isinstance(value, (int, float)):
            return f'<x:c r="{ref}"{s} t="n"><x:v>{value}</x:v></x:c>'
        return f'<x:c r="{ref}"{s} t="str"><x:v>{escape(str(value), quote=False)}</x:v></x:c>'

    def _style_for(self, text, row, col):
        """Style of the existing cell, else of the same column in the nearest row above, else None."""
        for r in range(row, 0, -1):
            m = self._row_span(text, r)
            if not m or m.group(4):
                continue
            for c in _CELL.finditer(m.group(3)):
                if col_index(c.group(1)) == col:
                    sm = re.search(r's="(\d+)"', c.group(3))
                    return sm.group(1) if sm else None
        return None

    def set_cell(self, sheet, row, col, value, expect="__NOCHECK__"):
        text = self._get(sheet)
        cur = self.get_value(sheet, row, col)
        if expect != "__NOCHECK__" and (cur or None) != (expect or None):
            raise MasterWriteError(f"{sheet}!{col_letters(col)}{row}: current value mismatch\n  expected: {str(expect)[:200]!r}\n  found:    {str(cur)[:200]!r}")
        style = self._style_for(text, row, col)
        ref = f"{col_letters(col)}{row}"
        new_cell = self._cell_xml(ref, style, value)
        m = self._row_span(text, row)
        if m is None:
            # create the row in order
            new_row = f'<x:row r="{row}">{new_cell}</x:row>'
            pos = None
            for mm in _ROW.finditer(text):
                if int(mm.group(1) or mm.group(4)) > row:
                    pos = mm.start(); break
            if pos is None:
                pos = text.index("</x:sheetData>")
            text = text[:pos] + new_row + text[pos:]
        else:
            inner = m.group(3) or ""
            cells = list(_CELL.finditer(inner))
            replaced = False
            out, last = [], 0
            for c in cells:
                ci = col_index(c.group(1))
                if ci == col:
                    out.append(inner[last:c.start()]); out.append(new_cell); last = c.end(); replaced = True
                elif ci > col and not replaced:
                    out.append(inner[last:c.start()]); out.append(new_cell); last = c.start(); replaced = True
            out.append(inner[last:])
            if not replaced:
                out.append(new_cell)
            new_inner = "".join(out)
            attrs = m.group(2) or m.group(5) or ""
            text = text[:m.start()] + f'<x:row r="{row}"{attrs}>{new_inner}</x:row>' + text[m.end():]
        self._put(sheet, text)
        self.log.append(("set_cell", sheet, row, col))

    def replace_in_cell(self, sheet, row, col, old, new, count=1):
        cur = self.get_value(sheet, row, col)
        if cur is None:
            raise MasterWriteError(f"{sheet}!{col_letters(col)}{row}: empty cell; cannot replace {old[:80]!r}")
        n = cur.count(old)
        if n != count:
            raise MasterWriteError(f"{sheet}!{col_letters(col)}{row}: expected {count} occurrence(s) of {old[:120]!r}, found {n}")
        self.set_cell(sheet, row, col, cur.replace(old, new), expect=cur)

    # ---------------------------------------------------------------------------- row ops
    def _shift(self, text, from_row, delta):
        """Renumber every row >= from_row by delta (cells and merged ranges included)."""
        def row_sub(m):
            if m.group(1):
                r = int(m.group(1))
                if r < from_row:
                    return m.group(0)
                nr = r + delta
                inner = _CELL.sub(lambda c: c.group(0).replace(f'r="{c.group(1)}{c.group(2)}"', f'r="{c.group(1)}{int(c.group(2)) + delta}"', 1), m.group(3))
                return f'<x:row r="{nr}"{m.group(2)}>{inner}</x:row>'
            r = int(m.group(4))
            return m.group(0) if r < from_row else f'<x:row r="{r + delta}"{m.group(5)}/>'
        text = _ROW.sub(row_sub, text)

        def merge_sub(m):
            a, r1, b, r2 = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
            if r1 >= from_row:
                r1 += delta
            if r2 >= from_row:
                r2 += delta
            return f'<x:mergeCell ref="{a}{r1}:{b}{r2}" />'
        return _MERGE.sub(merge_sub, text)

    def insert_rows(self, sheet, before_row, rows):
        """rows: list of {col_index: value}. New rows take the cell styles of row before_row-1."""
        text = self._get(sheet)
        text = self._shift(text, before_row, len(rows))
        self._put(sheet, text)
        for i, vals in enumerate(rows):
            r = before_row + i
            for col in sorted(vals):
                self.set_cell(sheet, r, col, vals[col])
        self.log.append(("insert_rows", sheet, before_row, len(rows)))

    def delete_rows(self, sheet, first, last):
        text = self._get(sheet)
        for m in list(_ROW.finditer(text))[::-1]:
            r = int(m.group(1) or m.group(4))
            if first <= r <= last:
                text = text[:m.start()] + text[m.end():]
        for m in list(_MERGE.finditer(text))[::-1]:
            r1, r2 = int(m.group(2)), int(m.group(4))
            if first <= r1 and r2 <= last:                      # merge wholly inside the deleted rows: dropped with them
                text = text[:m.start()] + text[m.end():]
            elif first <= r1 <= last or first <= r2 <= last:
                raise MasterWriteError(f"{sheet}: merged range {m.group(0)} partly intersects deleted rows {first}-{last}")
        text = self._shift(text, last + 1, -(last - first + 1))
        self._put(sheet, text)
        self.log.append(("delete_rows", sheet, first, last))

    def remove_sheet(self, sheet):
        part = self.sheet_part.pop(sheet)
        rid = self.sheet_rid.pop(sheet)
        self._xml.pop(sheet, None)
        wb = self.parts["xl/workbook.xml"].decode("utf-8-sig")
        pat = re.compile(r'<x:sheet name="%s" sheetId="\d+" r:id="%s"[^>]*/>' % (re.escape(sheet), re.escape(rid)))
        if len(pat.findall(wb)) != 1:
            raise MasterWriteError(f"workbook entry for {sheet} not found exactly once")
        bom = self.parts["xl/workbook.xml"].startswith(b"\xef\xbb\xbf")
        self.parts["xl/workbook.xml"] = (("﻿" if bom else "") + pat.sub("", wb)).encode("utf-8")
        rels = self.parts["xl/_rels/workbook.xml.rels"].decode("utf-8-sig")
        rp = re.compile(r'<Relationship [^>]*Id="%s"[^>]*/>' % re.escape(rid))
        if len(rp.findall(rels)) != 1:
            raise MasterWriteError(f"relationship {rid} not found exactly once")
        bom = self.parts["xl/_rels/workbook.xml.rels"].startswith(b"\xef\xbb\xbf")
        self.parts["xl/_rels/workbook.xml.rels"] = (("﻿" if bom else "") + rp.sub("", rels)).encode("utf-8")
        ct = self.parts["[Content_Types].xml"].decode("utf-8-sig")
        cp = re.compile(r'<Override [^>]*PartName="/%s"[^>]*/>' % re.escape(part))
        bom = self.parts["[Content_Types].xml"].startswith(b"\xef\xbb\xbf")
        self.parts["[Content_Types].xml"] = (("﻿" if bom else "") + cp.sub("", ct)).encode("utf-8")
        relpart = part.replace("worksheets/", "worksheets/_rels/") + ".rels"
        if relpart in self.parts:
            raise MasterWriteError(f"{sheet} has its own relationships ({relpart}); refusing to remove")
        del self.parts[part]
        self.log.append(("remove_sheet", sheet))

    # ---------------------------------------------------------------------------- save
    def save(self, out_path):
        for sheet, text in self._xml.items():
            self.parts[self.sheet_part[sheet]] = text.encode("utf-8")
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zout:
            for info in self.zin.infolist():
                if info.filename not in self.parts:
                    continue
                zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                zi.compress_type = info.compress_type
                zi.external_attr = info.external_attr
                zi.create_system = info.create_system
                zout.writestr(zi, self.parts[info.filename])
        data = buf.getvalue()
        with open(out_path, "wb") as fh:
            fh.write(data)
        return data
