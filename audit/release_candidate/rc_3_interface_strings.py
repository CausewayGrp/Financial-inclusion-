# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-3 — governed interface strings (audit/release_candidate/INSTRUCTIONS.md, Part A, G2 items 11, 12, 18, 19, 20).

  python3 rc_3_interface_strings.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every label is the brief's own wording, EN and AR together; nothing here is authored by the session.
  11 UI-JS-SEARCH-RESULTS-OF — the search status when the runtime shows fewer hits than match.
  12 The source-library resource category "Measurement standards and methods" → "Measurement methods and international references".
  18 The provider observability matrix: five dimension headings and the payment-system operators class label.
  19 The search result-type facet (name and no-type state), the way on when hits are capped, the visually hidden new-tab cue,
     the mixed-unit value column header, and the Compare status in label-value form.
  20 The Arabic percentage-point unit label «نقاط مئوية» → «نقطة مئوية», the form the governed prose uses.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui  # noqa: E402

NEW_ROWS = [
    ("UI-JS-SEARCH-RESULTS-OF", "Showing {n} of {m} results", "النتائج المعروضة: {n} من {m}",
     "RC-3 item 11. site-src/app.js search status when fewer hits are shown than match ({n} shown, {m} matching); UI-JS-SEARCH-RESULTS stays for when all hits are shown."),
    ("UI-VIS-MATRIX-AUTHORITY", "Issuing authority or source", "الجهة المصدرة أو المصدر",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY matrix dimension heading (scripts/yfie/visuals.py provider_matrix); wording from the contract's governed alt text."),
    ("UI-VIS-MATRIX-UNIVERSE", "Dated list or count", "القائمة أو العدد المؤرخ",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY matrix dimension heading."),
    ("UI-VIS-MATRIX-STATUS", "Dated status decisions", "قرارات الوضع المؤرخة",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY matrix dimension heading."),
    ("UI-VIS-MATRIX-NEGATIVE", "Official lists of unlicensed names", "قوائم رسمية بالأسماء غير المرخصة",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY matrix dimension heading."),
    ("UI-VIS-MATRIX-OPERATION", "Evidence of operation", "أدلة التشغيل",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY matrix dimension heading."),
    ("UI-VIS-CAT-PRV-CLASS-PSO", "Payment-system operators", "مشغلو أنظمة الدفع",
     "RC-3 item 18. VIS-PROVIDER-OBSERVABILITY fifth class row (UNKNOWN in every dimension; no governed universe row)."),
    ("UI-JS-SEARCH-TYPE-FACET", "Result type", "نوع النتيجة",
     "RC-3 item 19. site-src/app.js accessible name of the search result-type filter (EAD-06)."),
    ("UI-JS-SEARCH-TYPE-ALL", "All types", "كل الأنواع",
     "RC-3 item 19. site-src/app.js the result-type filter's no-type state."),
    ("UI-JS-SEARCH-SEE-ALL-EVIDENCE", "See all matching evidence records", "اعرض كل سجلات الأدلة المطابقة",
     "RC-3 item 19. site-src/app.js the way on when hits are capped: the query carried to the Evidence directory (?q=, EAD-06)."),
    ("UI-EXTERNAL-NEW-TAB", "(opens in a new tab)", "(يُفتح في علامة تبويب جديدة)",
     "RC-3 item 19. Visually hidden inside every external source link that opens a new tab (scripts/yfie; D5 escalation)."),
    ("UI-VIS-VALUE-UNIT-PER-ROW", "Value (unit given in each row)", "القيمة (الوحدة مذكورة في كل صف)",
     "RC-3 item 19. Header of a fallback-table value column whose rows carry different units (scripts/yfie/visuals.py; D6 escalation)."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()
    # ---- item 19 (existing row) · Compare status in label-value form
    set_ui(s, "RC-3:ITEM-19", "UI-JS-COMPARE-SELECTED", "Records selected: {n}", "السجلات المختارة: {n}", "records selected", "سجلات مختارة")
    # ---- item 20 · Arabic percentage-point unit
    set_ui(s, "RC-3:ITEM-20", "UI-VIS-UNIT-PP", None, "نقطة مئوية", None, "نقاط مئوية")
    # ---- item 12 · resource category label (four source records)
    t15 = Table(s, "15_SOURCE_LIBRARY")
    n12 = 0
    for sid in t15.rows:
        if t15.get(sid, "resource_category") == "Measurement standards and methods":
            t15.set("RC-3:ITEM-12", sid, "resource_category", "Measurement methods and international references", "Measurement standards and methods")
            t15.set("RC-3:ITEM-12", sid, "resource_category_ar", "مناهج القياس ومراجع دولية", "معايير القياس ومناهجه")
            n12 += 1
    if n12 != 4:
        raise TxError(f"item 12: expected 4 source records in the category, found {n12}")
    # ---- items 11, 18, 19 · new rows (appended last: row indices above are unaffected)
    insert_ui_rows(s, "RC-3:ITEMS-11-18-19", NEW_ROWS)
    notes["item_11"] = "DONE — UI-JS-SEARCH-RESULTS-OF added (EN 'Showing {n} of {m} results'; AR «النتائج المعروضة: {n} من {m}»)."
    notes["item_12"] = f"DONE — {n12} source records relabelled in both languages."
    notes["item_18"] = ("DONE — the five matrix headings and UI-VIS-CAT-PRV-CLASS-PSO added; the matrix draws on /providers/ and its record in both "
                        "languages (DL-D7-001). One renderer change rides with this transaction (scripts/yfie/visuals.py provider_matrix): the "
                        "payment-system-operators row printed its three institution events in the status dimension without the UNKNOWN label; it now "
                        "prints UNKNOWN in all five dimensions, the events following as context, in the drawn form and the fallback table (the "
                        "contract's known_gap).")
    notes["independent_review"] = OrderedDict([
        ("reviewer", "independent subagent that did not write the transaction (senior Arab economic editor, senior institutional English editor and accessibility lenses)"),
        ("verdict", "ACCEPTABLE — every string verbatim the brief's wording in both languages; items 12, 18, 20 and the Compare status hold; no placeholder or raw UI id in any body text"),
        ("applied", ["SHOULD FIX 3: this note named no code change; it now records the provider_matrix change (and the renderer docstring says so)"]),
        ("escalated", ["SHOULD FIX 1: four English-only Master period values (WCR-001, WCR-002, WCR-004 reference_period; PUC-MFI-2026-01 reference_state) "
                       "now show on the Arabic matrix — design/ESCALATIONS.md, NEEDS_CONTROLLED_CONTENT, raised 2 October 2026",
                       "SHOULD FIX 2: no governed lead-in marks the payment-system-operators context events as context — design/ESCALATIONS.md, NEEDS_CONTROLLED_CONTENT"]),
        ("for_the_owner", ["OPTIONAL: «9 نقطة مئوية» in the VIS-FINDEX-GAPS frame uses one invariant unit label (prose says «9.0 نقاط مئوية»); the chart prints 9 where the prose prints 9.0 (pre-existing)",
                           "OPTIONAL: «مناهج القياس ومراجع دولية» could read «مناهج القياس والمراجع الدولية»; owner wording, not changed",
                           "OPTIONAL: the English unit prints capitalised after a value ('12.91 Percentage points'; pre-existing)"]),
    ])
    notes["item_19"] = "DONE — five rows added; UI-JS-COMPARE-SELECTED now 'Records selected: {n}' / «السجلات المختارة: {n}»."
    notes["item_20"] = "DONE — UI-VIS-UNIT-PP label_ar «نقطة مئوية» (EN unchanged)."
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-3"), ("summary", "Release-candidate governed interface strings: items 11, 12, 18, 19, 20 of audit/release_candidate/INSTRUCTIONS.md Part A G2"),
                                           ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
