# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-4: the governed label for the chronology search-result type.

  python3 fc_4_chronology_search.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-4:B-TOOLS. The tool audit found the chronology was a public governed family with no search record at all:
24 events, each with its own anchor on /finance/ and /data/, its governed fact, relevance and boundary, and a reader
who searched a word they had just read on the page ("banknotes") got nothing. The generator now indexes them on the
same anchor-and-fragment pattern the measurement priorities use. The result-type filter is built from governed
interface copy, so the new type needs its own label or the filter would offer no option for a type the index carries -
the same asymmetry this pass fixed in the /data/ filter. This transaction adds that label.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, insert_ui_rows  # noqa: E402

F = "FC-4:B-TOOLS"


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, F, [(
        "UI-JS-TYPE-CHRONOLOGY",
        "Chronology event",
        "حدث في التسلسل الزمني",
        "site-src/app.js TYPE_LABEL_UI['chronology']")])
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-4"),
        ("summary", "The governed label for the chronology search-result type, so the result-type filter offers an "
                    "option for every type the index carries")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
