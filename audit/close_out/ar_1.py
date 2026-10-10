# -*- coding: utf-8 -*-
"""Close-out transaction AR-1: the accepted Arabic edits that depend on no factual fix (brief W2 "AR-1"; D11).

  python3 ar_1.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Source: audit/arabic_review/YFIE_ARABIC_ACCEPTED_EDIT_REGISTER_2026-10-10.csv, every row with apply_in = AR-1, except
AR-035, which the register's own condition put in CLOSE-1 (the transaction that touched /about/). Each row is written
only if its cell still holds exact_old_ar, and exact_old_ar hashes to original_sha256 (close_lib.apply_register_ar):
whole-cell, exact-value writes, never a fuzzy or regex replacement. A mismatch stops that row and is reported; the
others go on. English: CHANGE_EN rows take the register's en_new in the same transaction; PARITY_CHECK rows leave the
English as it is (it already says what the new Arabic says; checked row by row when the register was adjudicated).

AR-062 propagates its one phrase change into the four other cells the register names, only where the identical
sentence occurs there, as an exact single-occurrence substring (the register: "never retype a longer cell"). At
2ddbfb61 the identical sentence occurs in none of them (they word the same figures differently), so nothing is
propagated; the ledger lists the four cells as absent.

ADJ-RG-01 (added by the adjudication): "reuse terms have not been assessed for any source" is false — 166 of the 167
sources are NOT_ASSESSED and one (SRC-WB-FINDEX-001) carries a research licence. Every such sentence in the Master was
searched (EN and AR) and becomes "for most sources": /rights/ section 2 and /data/ section 5 here; /data/ section 1 and
UI-DATA-REUSE-TERMS-ONCE are rewritten whole by AR-008 and AR-056, whose new text already says "most".
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import (Session, TxError, refresh_self_counts, register_rows, register_cell, apply_register_ar,  # noqa: E402
                       apply_register_en)

F = "AR-1"
SKIP = {"AR-035",            # applied in CLOSE-1 with D1 (register condition)
        "ADJ-RG-01"}         # not one cell: applied below, clause by clause

# AR-062: the same phrase change, propagated to the identical sentence in the cells the register lists
AR062_OLD = "بلغت نسبة من يملكون حسابًا 18.3% بين الرجال و5.4% بين النساء بعمر 15 سنة فأكثر"
AR062_NEW = "بلغت نسبة امتلاك الحساب 18.3% بين الرجال و5.4% بين النساء من البالغين بعمر 15 سنة فأكثر"
AR062_ALSO = [("06_EVIDENCE_OBJECTS", 42, 7), ("06_EVIDENCE_OBJECTS", 64, 7), ("11_VISUAL_LIBRARY", 10, 22),
              ("11_VISUAL_LIBRARY", 37, 22)]

# ADJ-RG-01: (route, order, lang, old clause, new clause)
ADJ = [
    ("/rights/", 2, "en", "Reuse terms have not yet been assessed for any source, so",
     "Reuse terms have not yet been assessed for most sources, so"),
    ("/rights/", 2, "ar", "ولم تُقيَّم بعدُ شروط إعادة الاستخدام لأي مصدر، لذلك",
     "ولم تُقيَّم بعدُ شروط إعادة الاستخدام لمعظم المصادر، لذلك"),
    ("/data/", 5, "en", "Reuse terms have not yet been assessed for any source in this library, so no source record states them.",
     "Reuse terms have not yet been assessed for most sources in this library, so most source records do not state them."),
    ("/data/", 5, "ar", "ولم تُقيَّم حتى الآن شروط إعادة الاستخدام لأي مصدر في هذه المكتبة، ولذلك لا يذكرها أي سجل مصدر.",
     "ولم تُقيَّم حتى الآن شروط إعادة الاستخدام لمعظم المصادر في هذه المكتبة، ولذلك لا تذكرها معظم سجلات المصادر."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    reg = register_rows()
    applied, stopped = [], []
    for rid, row in reg.items():
        if row["apply_in"] != "AR-1" or rid in SKIP:
            continue
        try:
            apply_register_ar(s, F, row)
            if row["en_action"].startswith("CHANGE_EN"):
                if not row["en_new"].strip():
                    raise TxError(f"{F} {rid}: CHANGE_EN without en_new")
                apply_register_en(s, F, row, row["en_new"])
            applied.append(rid)
        except TxError as ex:
            stopped.append((rid, str(ex)))
            print("STOPPED", rid, ex)
    # AR-062 propagation
    propagated, not_present = [], []
    for sheet, r, c in AR062_ALSO:
        cur = s.ed.get_value(sheet, r, c)
        if isinstance(cur, str) and cur.count(AR062_OLD) == 1:
            s.replace(F + ":AR-062", sheet, r, c, AR062_OLD, AR062_NEW, f"{sheet}!R{r}C{c}")
            propagated.append(f"{sheet}!R{r}C{c}")
        else:
            not_present.append(f"{sheet}!R{r}C{c}")   # the identical sentence is not there; the register says not to retype
    # ADJ-RG-01
    for route, order, lang, old, new in ADJ:
        s.replace_section(F + ":ADJ-RG-01", route, order, lang, "body", old, new)
    # no "for any source" reuse sentence may remain
    for sheet in ("03_PAGE_SECTIONS", "04_NAV_UX"):
        for i, row in enumerate(s.grid(sheet), 1):
            for j, v in enumerate(row or [], 1):
                if isinstance(v, str) and ("assessed for any source" in v or "reuse terms of any source" in v
                                           or "شروط إعادة الاستخدام لأي مصدر" in v):
                    raise TxError(f"{F}:ADJ-RG-01 {sheet}!R{i}C{j} still says 'any source'")
    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "The accepted Arabic register rows for AR-1, their English actions, AR-062's propagation and ADJ-RG-01"),
        ("register_rows_applied", applied), ("register_rows_stopped", stopped),
        ("ar062_propagated", propagated), ("ar062_identical_sentence_absent", not_present), ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}),
          f"applied={len(applied)} stopped={len(stopped)}")


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
