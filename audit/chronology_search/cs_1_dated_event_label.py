# -*- coding: utf-8 -*-
"""Chronology in search, transaction CS-1: the governed label of the new search-result type. EN and AR together.

  python3 cs_1_dated_event_label.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner decision of 10 October 2026 (the disposition of pull request #13; finish orchestration, step 6): the public dated
events of the system chronology are INDEXED in search, re-implemented on the current main from commit 6a2cfc4a (FC-4).
The result-type filter is built from governed interface copy (site-src/app.js TYPE_LABEL_UI), so the new type needs its
own label or the filter would offer no option for a type the index carries. The label uses the page's own term for these
objects ("Dated events in Yemen's financial system", UI-CHRONOLOGY-H), not a second name.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, insert_ui_rows  # noqa: E402

F = "CS-1:CHRONOLOGY-SEARCH"


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, F, [(
        "UI-JS-TYPE-CHRONOLOGY", "Dated event", "حدث مؤرخ",
        "Owner decision of 10 October 2026 (chronology events indexed in search). The search result type of a dated event of "
        "the system chronology, and its option in the result-type filter (site-src/app.js TYPE_LABEL_UI['chronology']).")])
    rep = s.save(out, ledger, OrderedDict([("transaction", "CS-1"),
                                           ("summary", "The governed label of the dated-event search-result type")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
