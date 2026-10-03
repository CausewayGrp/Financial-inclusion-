# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-9: Part B item B6, measurement linkage.

  python3 rc_9_b6_measurement.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Each Reading is linked to the one or two Measurement Agenda priorities whose stated purpose supplies the evidence the
Reading says is missing; every link is justified, quoting both sides in both languages, in
audit/release_candidate/MEASUREMENT_LINKS.md. Five bindings are added (08_READINGS `measurement_bindings`); the seven
existing ones are kept; CWR-002 stays unlinked because no priority covers reconciling a restated official series (a gap
recorded there, not filled). The bindings now render on each Reading page (scripts/yfie), and /measurement/ shows each
priority's governed `decisions_unlocked` and `blocked_evidence` (complete in both languages for all ten), under two new
interface labels. MA-010's Arabic writes «تاليًا» in the house form.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows  # noqa: E402

F = "RC-9:B6"
BINDINGS = OrderedDict([("CWR-001", ([], ["MA-001"])), ("CWR-003", (["MA-005"], ["MA-005", "MA-002"])),
                        ("CWR-006", ([], ["MA-005"])), ("CWR-007", (["MA-003"], ["MA-003", "MA-007"])),
                        ("CWR-009", (["MA-010"], ["MA-010", "MA-006"]))])
LABELS = [("UI-MA-DECISIONS", "Questions it would answer:", "الأسئلة التي سيجيب عنها القياس:",
           "RC-9 (Part B B6). /measurement/ label before a priority's governed decisions_unlocked items."),
          ("UI-MA-BLOCKED", "Evidence that cannot be produced without it:", "الأدلة التي لا يمكن إنتاجها من دونه:",
           "RC-9 (Part B B6). /measurement/ label before a priority's governed blocked_evidence.")]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t08 = Table(s, "08_READINGS", 4)
    for rid, (old, new) in BINDINGS.items():
        cur = t08.get(rid, "measurement_bindings")
        if json.loads(cur) != old:
            raise TxError(f"{F}: {rid} measurement_bindings holds {cur!r}")
        t08.set(F, rid, "measurement_bindings", json.dumps(new, separators=(",", ":")), cur)
    t10 = Table(s, "10_MEASUREMENT_AGENDA", 4)
    cur = t10.get("MA-010", "decisions_unlocked_ar")
    if cur.count("تالياً") != 1:
        raise TxError(f"{F}: MA-010 decisions_unlocked_ar does not hold «تالياً» once")
    t10.set(F, "MA-010", "decisions_unlocked_ar", cur.replace("تالياً", "تاليًا"), cur)
    insert_ui_rows(s, F, LABELS)
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-9"), ("summary", "Part B B6: measurement linkage"),
                                           ("items", OrderedDict([("B6", "five bindings; two labels; MA-010 spelling")]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
