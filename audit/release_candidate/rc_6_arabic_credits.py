# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-6 — Arabic credit lines (audit/release_candidate/INSTRUCTIONS.md, Part B item B4).

  python3 rc_6_arabic_credits.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

A figure's credit line is composed by the generator from governed publishers: the source library's publisher and
publisher_ar (15; every listed source already has both) and the evidence passports' publisher (34), English only. This
transaction adds 34 publisher_ar for the seven passports a credit line uses (scripts/projection/master_structure.json gains
the column, installed with --install; CONTRIBUTING.md §9). Each Arabic name is the form the Master already governs for
that institution or programme — no name is authored: «البنك المركزي اليمني – عدن» and «البنك الدولي» and «صندوق النقد
الدولي» as the source library writes them; the Findex and Remittance Prices Worldwide as the records' Arabic text names them
(06 summary_ar / method_ar of VIS-FINDEX-GAPS, VIS-REMITTANCE-COST). The Arabic uses the institution's established Arabic
name without a Latin acronym; a product name that Arabic writes in English stays in parentheses.

Independent review before commit (B4): NOT ACCEPTABLE as first staged, every finding applied here and in the generator:
  F1 (blocking) the duplicate rule credited RV-CWR-004's World Bank project event to the Global Findex: an institution's bare
     name now folds into one of its products only when its source's governed title names that product; otherwise the bare
     name is printed once (scripts/projection/derived.py);
  F2 «(IMF)» is not the resource's form: the IMF line uses the bare Arabic name, and the language note says what the rule is;
  F3 the Arabic detached caption printed the English credit: it now prints the Arabic one;
  F4 «مسح المنشآت المخصص» was a calque of "custom" — and "custom" is not the source's word either: the World Bank report
     calls it "the 2022 Yemen Enterprise Survey" (Yemen Financial Sector Diagnostics, 2024, Annex III title; read in the
     original on 3 October 2026), so the passport names it so in both languages.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError  # noqa: E402

PUBLISHER_AR = OrderedDict([
    ("Central Bank of Yemen — Aden", "البنك المركزي اليمني – عدن"),
    ("World Bank Global Findex", "البنك الدولي، المؤشر العالمي للشمول المالي (Global Findex)"),
    ("World Bank 2022 Yemen Enterprise Survey", "مسح المنشآت في اليمن لعام 2022 الذي أجراه البنك الدولي"),
    ("IMF / Yemeni authorities", "صندوق النقد الدولي / السلطات اليمنية"),
    ("World Bank Remittance Prices Worldwide", "قاعدة بيانات البنك الدولي لأسعار الحوالات حول العالم (Remittance Prices Worldwide)"),
])
PASSPORTS = ["EP-CBY-PAY-H1-2025", "EP-CBY-POS-MONTHLY", "EP-CBY-REMITTANCE-VINTAGE-K04", "EP-FINDEX-2022-ACCOUNT", "EP-FIRM-2022",
             "EP-REMITTANCE-MACRO", "EP-WB-RPW-KSA-YEM-K04"]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    S = "34_EVIDENCE_PASSPORTS"
    g = s.grid(S)
    hdr = list(g[3])          # main header row 4
    while hdr and hdr[-1] in (None, ""):
        hdr.pop()
    if hdr[-1] != "display_requirements" or "publisher_ar" in hdr:
        raise TxError(f"34 header not as expected: {hdr[-3:]}")
    col = len(hdr) + 1
    pub = hdr.index("publisher") + 1
    # F4: the survey's English name as its source gives it (the only English publisher this transaction changes)
    t = Table(s, S)
    t.set("RC-6:B4-F4", "EP-FIRM-2022", "publisher", "World Bank 2022 Yemen Enterprise Survey", "World Bank 2022 custom enterprise survey")
    g = s.grid(S)
    s.set("RC-6:B4", S, 4, col, "publisher_ar", None, "34 header")
    seen = set()
    for i, r in enumerate(g, 1):
        if i > 4 and r and r[0] in PASSPORTS:
            en = r[pub - 1]
            if en not in PUBLISHER_AR:
                raise TxError(f"{r[0]}: publisher {en!r} has no governed Arabic form in this transaction")
            s.set("RC-6:B4", S, i, col, PUBLISHER_AR[en], None, f"{r[0]}.publisher_ar")
            seen.add(r[0])
    if seen != set(PASSPORTS):
        raise TxError(f"passports not found: {set(PASSPORTS) - seen}")
    notes = OrderedDict([("B4", "DONE — 34 publisher_ar for the seven passports the credit lines use; the generator composes the Arabic credit from "
                                "15 publisher_ar and 34 publisher_ar and credits each institution once: an exact repeat is dropped; a bare "
                                "institution name folds into one of its products only when its source's title names that product "
                                "(VIS-REMITTANCE-COST: the RPW corridor records); two publications of one institution print its bare name once "
                                "(RV-CWR-004: the Global Findex and the FMIIP record → 'World Bank'; RV-CWR-001: 'IMF / Yemeni authorities' and the "
                                "IMF staff report → 'International Monetary Fund'). The Arabic detached caption credits in Arabic."),
                         ("names", PUBLISHER_AR),
                         ("independent_review", OrderedDict([
                             ("verdict_before_fixes", "NOT ACCEPTABLE: 1 BLOCKING (F1), 3 SHOULD FIX (F2–F4), 8 OPTIONAL"),
                             ("applied", ["F1 RV-CWR-004 credited the World Bank's FMIIP record to the Global Findex: same-publication test on the source title",
                                          "F2 «(IMF)» dropped; the language note states the rule the Arabic follows",
                                          "F3 the Arabic detached caption printed the English credit",
                                          "F4 the survey named as its source names it ('2022 Yemen Enterprise Survey'), English and Arabic; 'custom' is "
                                          "not the source's word (read in the original, 3 October 2026)",
                                          "O6 (optional) the authority's Arabic name is borrowed only when the authority publishes the source"]),
                             ("recorded", ["O1 'Sources:' for two-entry lines needs a new governed label (not added)",
                                           "O2 the source library writes 'Central Bank of Yemen — Aden' with an em dash; English prose uses an en dash",
                                           "O3 'IMF / Yemeni authorities' can read as joint publication (VIS-REMITTANCE-MACRO; for the owner)",
                                           "O4 the survey's tables are published in Yemen Financial Sector Diagnostics (2024); its two Arabic titles are "
                                           "aligned in RC-7",
                                           "O5 the three World Bank lines use three Arabic constructions",
                                           "O7 Latin text inside the Arabic credit carries no lang attribute",
                                           "O8 four design and audit records still say credits are English-only; superseded by B4"])]))])
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-6"), ("summary", "Part B B4: Arabic credit lines"), ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
