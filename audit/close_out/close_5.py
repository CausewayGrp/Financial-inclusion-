# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-5: Readings and Measurement Agenda (brief v5 W3e, Appendix D). English and Arabic change together.

  python3 close_5.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The text and the bindings are data, in close_5_text.json next to this script. It was built from drafts that an
independent red-team and an Arabic editor read before the run. Every write checks the exact current value; an
inserted section checks the place it goes.

- RD10: answer-first openings. Whole sentences move, so the finding and its main limit come before the background.
  Where a register row fixed an opening (AR-003 CWR-001, AR-004 CWR-007, AR-005 CWR-010), its wording is kept
  verbatim. ED-037 (CWR-011) is applied here, with RD1.
- RD2: a "use" section (section_id use) on the nine Readings that lacked one. It goes before the last section
  ("what would change"), which moves down by one, in 03 and in the 09 section index.
- RD1 (CWR-011): two more month-ends from the latest bulletin; five alternatives, asset quality (CR-08) among them;
  related to CWR-002 and back; bound to MA-008. /finance/ is not added (rule F2: an answer page carries at most two
  Readings); this is an owner question.
- RD3 (CWR-005): the 2024–2025 e-wallet records beside the 2019 study, not as one series. RD4 (CWR-008): FMIIP PAD
  paragraph 10 as a dated limitation (SMEPS 2025 was not published and the ESCWA paper could not be reached on 10
  October 2026). RD5 (CWR-010): what U3 and U12 add that the Reading did not yet say. RD6 (CWR-003, CWR-009) and RD7
  (CWR-001): no change, because nothing newer was published and U11 is already in CWR-001.
- RD9: /measurement/ links CWR-001 (MA-001), CWR-002 (MA-008) and CWR-011 (MA-008); /methodology/ lists the four
  evidence-method visuals among its related records; CWR-004 relates to CWR-007, which had no inbound link. The
  domain pages' two-priority display cap is set in the controlled contract presentation_priority.json, which only the
  programme steward edits: it is escalated, not changed here.
- M1: dimensions added to MA-001, MA-003, MA-005, MA-008 and MA-009; MA-008 says no current measure covers Yemen. M2:
  the /methodology/ gap list records the ICT and telecommunications layer, insolvency, digital literacy and Yemen
  Post, with where each would be measured; no procurement document is named (CR-10).
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, COL03  # noqa: E402

F = "CLOSE-5"
DATA = os.path.join(HERE, "close_5_text.json")
S03, S09 = "03_PAGE_SECTIONS", "09_READING_SECTIONS"


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, list):
        return [nfc(x) for x in o]
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


def section_text(s, e):
    """A section's heading and body, both languages, at its current order (exact old values)."""
    for lang in ("en", "ar"):
        row = s.section_row(e["route"], e["order"], lang)
        for fld in ("heading", "body"):
            new = e.get(f"new_{fld}_{lang}")
            if new is None:
                continue
            col = COL03[f"{fld}_{lang}"]
            s.set(e["finding"], S03, row, col, new, e[f"old_{fld}_{lang}"], f"{e['route']}#s{e['order']}.{fld}_{lang}")


def insert_use(s, u):
    """The "use" section at order n; the last section (n) moves to n + 1, in 03 and in the 09 index."""
    route, rid, n, fid = u["route"], u["reading_id"], int(u["order"]), u["finding"]
    g03 = s.grid(S03)
    rows = [(i, int(float(r[1]))) for i, r in enumerate(g03, 1) if i > 4 and r and r[0] == route and r[1] not in (None, "")]
    if max(o for _, o in rows) != n or sum(1 for _, o in rows if o == n) != 1:
        raise TxError(f"{fid}: {route} does not end with one section at order {n}: {sorted(o for _, o in rows)}")
    last = next(i for i, o in rows if o == n)
    if g03[last - 1][COL03["heading_en"] - 1] != u["last_heading_en"]:
        raise TxError(f"{fid}: {route} s{n} is not '{u['last_heading_en']}'")
    g09 = s.grid(S09)
    idx = [(i, int(float(r[1])), r[2]) for i, r in enumerate(g09, 1) if i > 4 and r and r[0] == rid and r[1] not in (None, "")]
    if max(o for _, o, _ in idx) != n or [x for _, o, x in idx if o == n] != ["what_would_change"] or any(x == "use" for _, _, x in idx):
        raise TxError(f"{fid}: 09 {rid} does not end with what_would_change at {n}, or already has a use section")
    last9 = next(i for i, o, _ in idx if o == n)
    s.set(fid, S03, last, 2, n + 1, str(n), f"{route}#s{n}.section_order")
    s.ed.insert_rows(S03, last, [{1: route, 2: n, COL03["heading_en"]: u["heading_en"], COL03["body_en"]: u["body_en"],
                                  COL03["heading_ar"]: u["heading_ar"], COL03["body_ar"]: u["body_ar"]}])
    for col, fld in ((1, "route"), (2, "section_order"), (COL03["heading_en"], "heading_en"), (COL03["body_en"], "body_en"),
                     (COL03["heading_ar"], "heading_ar"), (COL03["body_ar"], "body_ar")):
        s.ledger.append(OrderedDict([("finding", fid), ("sheet", S03), ("row", last), ("col", col),
                                     ("field", f"{route}#s{n}.{fld}"), ("old", None), ("new", u.get(fld, route if col == 1 else n))]))
    s.set(fid, S09, last9, 2, n + 1, str(n), f"{rid}.what_would_change.section_order")
    s.ed.insert_rows(S09, last9, [{1: rid, 2: n, 3: "use"}])
    for col, fld, v in ((1, "reading_id", rid), (2, "section_order", n), (3, "section_id", "use")):
        s.ledger.append(OrderedDict([("finding", fid), ("sheet", S09), ("row", last9), ("col", col), ("field", f"{rid}.use.{fld}"),
                                     ("old", None), ("new", v)]))
    s._g03 = None                                            # 03 rows moved: the section index is read again


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    D = nfc(json.load(open(DATA, encoding="utf-8")))

    # ---------------------------------------------------------------- 03: section text at the current orders
    for e in D["sections"]:
        section_text(s, e)

    # ---------------------------------------------------------------- 03 + 09: the "use" sections (RD2)
    for u in D["use_sections"]:
        insert_use(s, u)

    # ---------------------------------------------------------------- 08, 06, 10: fields, bindings and states
    for sheet in ("08_READINGS", "06_EVIDENCE_OBJECTS", "10_MEASUREMENT_AGENDA"):
        t = Table(s, sheet)
        for c in (c for c in D["cells"] if c["sheet"] == sheet):
            t.set(c["finding"], c["key"], c["field"], c["new"], c["old"])

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "W3e: answer-first openings (RD10, ED-037 with RD1), nine 'use' sections (RD2), CWR-011 completed "
                    "(RD1), CWR-005, CWR-008 and CWR-010 updated (RD3–RD5), links (RD9), Measurement Agenda dimensions "
                    "(M1) and the /methodology/ gap list (M2)."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
