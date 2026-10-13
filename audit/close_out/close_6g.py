# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6G (Stage A final instruction v5, 11 October 2026, section 8, gate CO-G07 entry G7-08).

  python3 close_6g.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

CO-G07 pins "any CauseWay-derived aggregate figure printed without its label". The Master has no state named
CAUSEWAY_DERIVED_AGGREGATE; the aggregates CauseWay derives and prints are the two United States–Yemen corridor averages
(RMO-RPW-US-2025Q3-200/-500, 3.92% and 2.30%, calculation_state CAUSEWAY_SIMPLE_MEAN_OF_SOURCE_QUOTES) and the overlap bound
(at least 62.7%, gate entry G7-11). /remittances/ and the Reading CWR-012 label the corridor averages "computed here"; the
summary of VIS-REMITTANCE-COST (06_EVIDENCE_OBJECTS and 11_VISUAL_LIBRARY, both languages), which also reaches
/remittances/, printed them without the label. This transaction adds it. No number changes and none is added.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, TxError, refresh_self_counts  # noqa: E402

F = "CLOSE-6G"
VIS = "VIS-REMITTANCE-COST"
OLD_EN = "and from the United States 3.92% and 2.30%."
NEW_EN = ("and from the United States 3.92% and 2.30%, computed here as the simple average of the quotes the World Bank "
          "lists for the United States–Yemen corridor.")
OLD_AR = "ومن الولايات المتحدة 3.92% و2.30%."
NEW_AR = ("ومن الولايات المتحدة 3.92% و2.30%، محسوبَين هنا بوصفهما متوسطَين بسيطَين لعروض الأسعار التي يدرجها البنك الدولي "
          "لممر الولايات المتحدة–اليمن.")


def nfc(v):
    return unicodedata.normalize("NFC", v)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    cells = []
    for sheet, (ce, ca) in (("06_EVIDENCE_OBJECTS", (6, 7)), ("11_VISUAL_LIBRARY", (21, 22))):
        hits = [i for i, r in enumerate(s.grid(sheet), 1) if r and r[0] == VIS]
        if len(hits) != 1:
            raise TxError(f"{F}: {sheet} holds {VIS} {len(hits)} times")
        cells += [(sheet, hits[0], ce, OLD_EN, NEW_EN, "en"), (sheet, hits[0], ca, OLD_AR, NEW_AR, "ar")]
    for sheet, r, c, old, new, lang in cells:
        s.replace(f"{F}:G7-08", sheet, r, c, nfc(old), nfc(new), f"{VIS}.{sheet}.summary_{lang}")
    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Gate CO-G07 entry G7-08: VIS-REMITTANCE-COST's summary labels the United States–Yemen corridor averages "
                    "(3.92% and 2.30%) as computed here, in both languages; no number changed."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
