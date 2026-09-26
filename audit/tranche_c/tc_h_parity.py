# -*- coding: utf-8 -*-
"""Tranche C transaction TC-H — bilingual parity of the non-record page sections (03).

  python3 tc_h_parity.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The bilingual-invariance test (audit/tranche_c/checks/bilingual_invariance.py) found 28 section pairs in 03 whose English and
Arabic editions print different numbers. Cause: in TC-C the English and Arabic editors worked independently; the English
edits carried evidence corrections (EVM/PAY/JRN/EN-13), the Arabic edits were linguistic, so several Arabic sections kept
superseded content (a 20 August 2023 issue date and an unverifiable reference number on /reforms/, 'current' lists, 'later'
decisions, Reading 'qualifies' sections that still repeated the previous section).

Decision (Lead): the accepted English content is the semantic reference for these sections; the Arabic is re-authored to
carry the same facts in Arabic editorial form. Two English cells change only to write a figure as a numeral or to state an
index base the Arabic already gave. Input: audit/tranche_c/inputs/TC-H_parity.json (each item guarded by its current value).
After writing, every touched section pair must print the same numbers, or the transaction fails.
"""
import json, os, re, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, TxError  # noqa: E402
from ptc_lib import S03, COL03       # noqa: E402

AR = str.maketrans("٠١٢٣٤٥٦٧٨٩٫٬", "0123456789.,")


def numbers(t):
    t = (t or "").translate(AR)
    t = re.sub(r"\b(\d{2})(\d{2})[–-](\d{2})\b(?!\d|[,.]\d)", r"\1\2–\1\3", t)   # 2022–23 -> 2022–2023
    return Counter(x.replace(",", "").rstrip(".") for x in re.findall(r"\d[\d,]*(?:\.\d+)?", t))


def main():
    src, out, ledger, work = sys.argv[1:5]
    spec = json.load(open(os.path.join(HERE, "inputs", "TC-H_parity.json"), encoding="utf-8"))
    s = Session(src, work)
    touched = set()
    for it in spec["items"]:
        f = "TC-H:" + it["finding"]
        if it["mode"] == "full":
            s.set_section(f, it["route"], it["order"], it["lang"], it["field"], it["new"], it["old"])
        else:
            s.replace_section(f, it["route"], it["order"], it["lang"], it["field"], it["old_sub"], it["new_sub"])
        touched.add((it["route"], it["order"]))
    for route, order in sorted(touched):
        vals = {}
        for lang in ("en", "ar"):
            row = s.section_row(route, order, lang)
            vals[lang] = " ".join(str(s.ed.get_value(S03, row, COL03[f"{fld}_{lang}"]) or "") for fld in ("heading", "body"))
        a, b = numbers(vals["en"]), numbers(vals["ar"])
        if a != b:
            raise TxError(f"{route}#s{order}: numbers still differ: only EN {dict(a - b)} only AR {dict(b - a)}")
    rep = s.save(out, ledger, {"transaction": "TC-H", "summary": "03 bilingual parity: Arabic re-authored to the accepted English content in 28 sections"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
