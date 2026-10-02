# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-4 — Part B governed strings given verbatim by the brief (audit/release_candidate/
INSTRUCTIONS.md, Part B items B5, B7, B8, B9).

  python3 rc_4_partb_strings.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

  B5 /data/: the heading and scope line of the regulatory-documents group, and the label for sources with no document
     type (EAD-07).
  B7 /evidence/compare/: the "selected set" sentence, in the Compare intro (Master 03, section 1, before the tool's
     prompt line) and as a governed string printed under the "record not available for comparison" error.
  B8 /data/: the reuse-terms sentence, stated once above the source list.
  B9 every page: "Print this page" and "Citation preview" ("Copy citation" exists: UI-JS-COPY-CITATION).
Every string is the brief's wording, English and Arabic together; nothing is authored here.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, TxError, insert_ui_rows, set_ui  # noqa: E402

B7_EN = ("Compare offers a selected set of evidence records in this edition. A record that is not offered here can still be read "
         "in full on its own page; its absence from Compare is not a judgement about it.")
B7_AR = ("تتيح أداة المقارنة في هذا الإصدار مجموعة مختارة من سجلات الأدلة. ويمكن قراءة أي سجل غير متاح هنا كاملًا في صفحته، "
         "وغيابه عن المقارنة ليس حكمًا عليه.")

NEW_ROWS = [
    ("UI-DATA-GROUP-REGULATORY", "Rules, decisions and official lists", "القواعد والقرارات والقوائم الرسمية",
     "RC-4 (Part B B5). /data/ heading of the group of sources whose document_label is Enforcement decision, Circular or instruction, "
     "Regulatory decision, Regulation, or Official list or roster (scripts/yfie/families.py data_sources)."),
    ("UI-DATA-GROUP-REGULATORY-SCOPE",
     "These are the regulatory documents held in this evidence base, not a complete register of Yemen's financial regulation.",
     "هذه هي الوثائق التنظيمية المتوفرة في قاعدة الأدلة هذه، وليست سجلًا كاملًا للتنظيم المالي في اليمن.",
     "RC-4 (Part B B5). /data/ the regulatory group's one scope line."),
    ("UI-DATA-DOCUMENT-TYPE-NOT-RECORDED", "Document type not recorded", "نوع الوثيقة غير مسجّل",
     "RC-4 (Part B B5; EAD-07). The document type shown, and the type-filter group, for a listed source with no governed document_label."),
    ("UI-JS-COMPARE-NOT-OFFERED", B7_EN, B7_AR,
     "RC-4 (Part B B7). site-src/app.js: printed under the Compare error for a record not available for comparison (reason 'unknown'); "
     "the same sentence stands in the Compare intro (03 /evidence/compare/ section 1)."),
    ("UI-DATA-REUSE-TERMS-ONCE",
     "This resource links to original sources and quotes them briefly. It has not assessed the reuse terms of any source; check each "
     "source's own terms before reusing its content.",
     "يربط هذا المورد بالمصادر الأصلية ويقتبس منها باختصار. ولم يُقيّم شروط إعادة استخدام أي مصدر؛ فتحقّق من شروط كل مصدر قبل إعادة "
     "استخدام محتواه.",
     "RC-4 (Part B B8). /data/ stated once above the source list; each card keeps its own reuse-terms label."),
    ("UI-CITE-PAGE-LINE", "{product}. CauseWay. {version}.", "{product}. CauseWay. {version}.",
     "RC-4 (Part B B9; review finding 4). The citation line of a page that is not an Evidence Record, after its title: the record line "
     "UI-CITE-RECORD-LINE without the record name — product, publisher, edition; no new words (scripts/yfie/render.py page_citation)."),
    ("UI-PRINT-THIS-PAGE", "Print this page", "اطبع هذه الصفحة",
     "RC-4 (Part B B9). The visible print control on every page (scripts/yfie/render.py page_util); the runtime calls the browser's print."),
    ("UI-CITATION-PREVIEW", "Citation preview", "معاينة الاستشهاد",
     "RC-4 (Part B B9). The visible preview of the page's or record's citation before it is copied (UI-JS-COPY-CITATION copies it)."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()
    # B7 · the Compare intro: the sentence stands before the tool's prompt line ("Select at least two records."), which the
    # renderer moves beside the controls (G4) — so the sentence is inserted before the last line of section 1's body
    for lang, col, sent, prompt in (("en", 5, B7_EN, "Select at least two records."), ("ar", 7, B7_AR, "اختر سجلين على الأقل.")):
        row = s.section_row("/evidence/compare/", 1, lang)
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
        if not cur.endswith("\n" + prompt):
            raise TxError(f"/evidence/compare/ section 1 {lang}: body does not end with the prompt line")
        if sent in cur:
            raise TxError(f"/evidence/compare/ section 1 {lang}: sentence already present")
        new = cur[: -len(prompt) - 1] + "\n\n" + sent + "\n" + prompt
        s.set("RC-4:B7", "03_PAGE_SECTIONS", row, col, new, cur, f"/evidence/compare/#s1.body_{lang}")
    insert_ui_rows(s, "RC-4:B5-B7-B8-B9", NEW_ROWS)
    # B8 "stated once" (review finding 5): the older directory paragraph drops its closing reuse clause, which the new line states
    OLD_EN = ("Every source here can be cited and opened where it was originally published. Each card says whether the source’s reuse terms have been "
              "assessed; where they have not, this resource offers no copy of the source for download or republication, so check the source’s own "
              "terms before redistributing its material.")
    OLD_AR = ("يمكن الاستشهاد بكل مصدر هنا وفتحه حيث نُشر أصلًا. وتبيّن كل بطاقة ما إذا كانت شروط إعادة استخدام المصدر قد قُيّمت؛ وحيث لم تُقيَّم، "
              "لا يقدم هذا المورد نسخة من المصدر للتنزيل أو إعادة النشر، فتحقّق من شروط المصدر نفسه قبل إعادة توزيع مادته.")
    NEW_EN = OLD_EN.replace(", so check the source’s own terms before redistributing its material.", ".")
    NEW_AR = OLD_AR.replace("، فتحقّق من شروط المصدر نفسه قبل إعادة توزيع مادته.", ".")
    if NEW_EN == OLD_EN or NEW_AR == OLD_AR:
        raise TxError("B8: the closing reuse clause was not found")
    set_ui(s, "RC-4:B8", "UI-DATA-EVERY-SOURCE-HERE-CAN-BE", NEW_EN, NEW_AR, OLD_EN, OLD_AR)
    notes["B5"] = "DONE — group heading, scope line and the no-type label added (04), verbatim; the renderer groups the regulatory sources."
    notes["B7"] = "DONE — sentence added to the Compare intro (03 section 1, before the prompt line) and as UI-JS-COMPARE-NOT-OFFERED for the error note."
    notes["B8"] = ("DONE — UI-DATA-REUSE-TERMS-ONCE added, verbatim; the older directory paragraph UI-DATA-EVERY-SOURCE-HERE-CAN-BE drops its closing "
                   "'check the source's own terms' clause in both languages, so the terms are stated once (review finding 5; a deletion, no new words).")
    notes["B9"] = ("DONE — UI-PRINT-THIS-PAGE and UI-CITATION-PREVIEW added, verbatim; UI-JS-COPY-CITATION reused; UI-CITE-PAGE-LINE governs the "
                   "page citation line (the record line without the record name; review finding 4).")
    notes["independent_review"] = OrderedDict([
        ("verdict_before_fixes", "NOT ACCEPTABLE: 1 BLOCKING, 4 SHOULD FIX, 7 OPTIONAL; every string verbatim the brief's in both languages"),
        ("applied", ["1 BLOCKING: the Arabic record citation preview ran the record ID and 'CauseWay' together; identifiers and the publisher name are isolated left-to-right in the preview and the print foot",
                     "2: no '.' after a title ending in '?', '؟' or '!' (page and record citations)",
                     "3: the Compare intro splits into paragraphs at its blank line",
                     "4: the page citation line is governed (UI-CITE-PAGE-LINE)",
                     "5: reuse terms stated once (the older paragraph's closing clause removed)",
                     "7 (optional): the link row to the curated regulatory card names the curated group"]),
        ("for_the_owner", ["B5 AR «المتوفرة» / «المتوافرة» and the repeated «هذه»; B5 EN 'evidence base'; B8 AR omits 'own' (brief wording, not changed)",
                           "the record citation carries boundary and sources beyond the brief's field list (publisher, edition, period, population, URL); a shorter citation is an owner choice"]),
        ("recorded", ["6: SRC-CBY-SANAA-C12-2024 and -C14-2024 look like circulars but carry no document_label; outside the group by the brief's rule until read",
                      "8: the supporting group's count now excludes the 22 regulatory sources it also supports",
                      "9: print and copy need JavaScript; the preview shows a relative address until the public origin is set"]),
    ])
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-4"), ("summary", "Part B governed strings given verbatim by the brief: B5, B7, B8, B9"), ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
