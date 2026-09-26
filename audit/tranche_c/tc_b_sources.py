# -*- coding: utf-8 -*-
"""Tranche C transaction TC-B — source citation metadata (TRUST-01, VER-13, VER-19, VER-21).

  python3 tc_b_sources.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Input: audit/tranche_c/inputs/TC-B_sources.json.
  * 15_SOURCE_LIBRARY gains four columns: publisher_ar, document_label, document_label_ar, document_date. document_type
    stays the controlled code used by search; document_label is the reader-facing kind of document.
  * Each drafted source receives its governed title (EN/AR), publisher (EN/AR), document label (EN/AR) and document date,
    and, when it had no curated card, public_card_state CITATION_CARD (bibliographic metadata, no curated summary).
    Sources whose title could not be supported stay locator cards (listed under 'excluded').
  * additional_urls: placeholders replaced by the governed locators; bare strings become JSON arrays; a locator that
    belongs to another source identity is removed from the duplicate record (one locator, one source identity).
  * 32_QUAL_LITERATURE QUAL-020: a label in a URL field is replaced by the governed locator.
  * The Yemen Microfinance Network's Arabic name is aligned Master-wide to the network's own form.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, Table, TxError, norm, insert_ui_rows  # noqa: E402

SHEET = "15_SOURCE_LIBRARY"
NEW_COLS = ["publisher_ar", "document_label", "document_label_ar", "document_date"]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    data = json.load(open(os.path.join(HERE, "inputs", "TC-B_sources.json"), encoding="utf-8"))
    t = Table(s, SHEET)
    if t.head[:24][-1] != "evidence_roles" or any(c in t.head for c in NEW_COLS):
        raise TxError("15 header not at expected state")
    base = 24
    for i, name in enumerate(NEW_COLS, start=1):
        s.set("TC-B:TRUST-01", SHEET, 4, base + i, name, None, f"header.{name}")
    t = Table(s, SHEET)
    for rec in data["sources"]:
        sid = rec["source_id"]
        for f, old in rec["old"].items():
            if f in rec["new"]:
                t.set("TC-B:TRUST-01", sid, f, rec["new"][f], old)
        for f in ("display_title_ar", "publisher_ar", "document_label", "document_label_ar", "document_date"):
            if f in rec["old"]:
                continue
            v = rec["new"].get(f)
            if v not in (None, ""):
                t.set("TC-B:TRUST-01", sid, f, v, t.get(sid, f))
    for fx in data["additional_url_fixes"]:
        t.set("TC-B:VER-19", fx["source_id"], "additional_urls", fx["new"], fx["old"])
    for d in data["url_dedupe"]:
        cur = t.get(d["source_id"], "additional_urls")
        try:
            urls = json.loads(cur)
        except Exception:
            raise TxError(f"{d['source_id']}: additional_urls not a JSON array: {cur!r}")
        keep = [u for u in urls if d["remove_url_containing"] not in u]
        if len(keep) == len(urls):
            raise TxError(f"{d['source_id']}: nothing to remove for {d['remove_url_containing']}")
        t.set("TC-B:VER-21", d["source_id"], "additional_urls", json.dumps(keep, ensure_ascii=False) if keep else None, cur)
    for fx in data["cell_fixes"]:
        g = s.grid(fx["sheet"])
        hits = [(i, j) for i, r in enumerate(g, 1) if r and r[0] == fx["key"] for j, v in enumerate(r, 1) if v == fx["old"]]
        if len(hits) != 1:
            raise TxError(f"{fx['sheet']} {fx['key']}: {len(hits)} cells hold {fx['old']!r}")
        s.set("TC-B:VER-19", fx["sheet"], hits[0][0], hits[0][1], fx["new"], fx["old"], f"{fx['key']}.{fx['field']}")
    # Master-wide Arabic name alignment
    old, new = data["ymn_arabic_name"]["old"], data["ymn_arabic_name"]["new"]
    from projection.master_reader import Workbook  # noqa: E402
    names = Workbook(src).sheet_names
    n = 0
    for sh in names:
        g = s.grid(sh)
        for i, r in enumerate(g, 1):
            for j, v in enumerate(r or [], 1):
                if isinstance(v, str) and old in v:
                    s.set("TC-B:YMN-AR", sh, i, j, v.replace(old, new), v)
                    n += 1
    insert_ui_rows(s, "TC-B:TRUST-01", [
        ("UI-SOURCE-UNTITLED", "Original source", "المصدر الأصلي",
         "Tranche C TC-B. Name of a source card whose title is not governed; the reference is shown separately, never as a name."),
        ("UI-SOURCE-REFERENCE", "Reference", "المرجع", "Tranche C TC-B. Label before a source's stable reference.")])
    rep = s.save(out, ledger, {"transaction": "TC-B", "input": "audit/tranche_c/inputs/TC-B_sources.json",
                              "ymn_cells": n, "summary": "15 citation metadata (+4 columns), locator fixes, YMN Arabic name"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written", "ymn_cells")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
