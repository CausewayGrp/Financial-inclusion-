# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-12: Part B items B12 (text-first visuals) and B13 (research library and link
check), with the independent review of RC-11 folded in (RC-11b).

  python3 rc_12_b12_b13.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

RC-11b — the bilingual review of RC-11 (NOT ACCEPTABLE on one string; all items applied):
    - UI-VIS-NOTE-POS-H1-WITHHELD (must fix). OBS-00036's caveat leaves its definition and period open, so the note no
      longer calls it a total "for that half-year". Three monthly releases carry a displayed percentage that contradicts
      their own totals (OBS-00078, -00081, -00093, comparability DIRECTLY_COMPARABLE_WITH_SOURCE_INTERNAL_PERCENT_
      CONTRADICTION), so the note says the published totals can be read side by side and that each mismatch is
      recorded as a discrepancy within the source — the wording of the method note on the same page («اختلافًا داخل
      المصدر» in Arabic, as the terminals note says) — against the published monthly totals, since each release reports
      one month. The source is named as the site names it elsewhere ("first-half 2025 payment report").
    - UI-VIS-TH-STEP (AR) «الحلقة», the chain's own word (UI-VIS-CHAIN-EVIDENCED); «الخطوة» is a reform step.
    - UI-VIS-TH-GROUP "Group or gap": four of the thirteen FINDEX rows are calculated gaps.
    - UI-VIS-TH-DATE "Date or period": a fieldwork span and months sit in that column.
    - UI-LAND-NO-NEXT names what is empty (no page to verify it, no priority); two such rows have a domain page.
    - UI-VIS-TH-SOURCE: the corner of the source-comparison table, which printed the prefix "Source:".
B12 — the two TABLE_TEXT_FIRST contracts whose rationale describes a table get it from governed rows
    (rc_12_stage_inputs.py binds them; scripts/projection/derived.py `_vdc_text_table` resolves and guards them):
    - VIS-TARGET-RESULT-STATE: baseline, target and the result the evidence base does not hold. The World Bank's
      Implementation Status Report (seq. 2) prints "0" as the current value, a reporting placeholder: it is not bound,
      and the result row says no observed result is held — not zero.
    - VIS-FIRM-FINANCE-PATH: item, number and base; a governed marker separates the 31 establishments with a line of
      credit from the 18 loan-source responses, because the Master does not establish that one is a subset of the other.
B13 — the research library's governed strings (filters, order, Readings backlinks, the archived-copy label), and the
    locators the link check of 3 October 2026 found broken (audit/release_candidate/LINK_CHECK.md):
    - five SFD newsletters moved to the publisher's new file names; each was read and holds the values the Master cites
      from it (issues 57, 66, 80, 85 and 92);
    - four documents have no current address at the publisher: their locator becomes the web.archive.org copy of the
      original address, which is kept as an additional locator, and the site says the link is an archived copy.
      Issue 62 (Q2 2013) is one of them: the file the publisher now hosts under the new name is another edition, whose
      provider-table totals (84,760 borrowers, 151,465 savers) differ from the values bound from the original edition.
RC-12's own bilingual review (NOT ACCEPTABLE on two strings, folded in before commit): the frame note's last sentence
    names the published monthly totals, not "its own totals"; the 18 responses keep the governed Arabic term «استجابة»
    (the unit reads, word for word, the governed universe) and the marker opens «لم يثبت»; three Arabic should-fix
    items (the imperative «افتح», «الوثائق الأحدث أولًا», «غير مسجّل»).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, set_ui  # noqa: E402

F11B, F12, F13, F13D = "RC-11b", "RC-12:B12", "RC-12:B13", "RC-12:B13d"

OLD_NOTE_EN = ("The payment-system report for the first half of 2025 also gives a POS-transaction total for that half-year. It is "
               "withheld here because its definition and period need a methodology note before public use. The monthly releases "
               "are shown because each reports the same POS measures for one month within the same reporting scope, so "
               "consecutive months are comparable.")
OLD_NOTE_AR = ("يذكر تقرير نظام المدفوعات للنصف الأول من 2025 أيضًا إجماليًا لمعاملات نقاط البيع في ذلك النصف، وهو محجوب هنا "
               "لأن تعريفه وفترته يحتاجان إلى ملاحظة منهجية قبل النشر. أما الإصدارات الشهرية فتُعرض لأن كلًّا منها يذكر مقاييس "
               "نقاط البيع نفسها لشهر واحد ضمن نطاق الإبلاغ نفسه، فتكون الأشهر المتتالية قابلة للمقارنة.")
NEW_NOTE_EN = ("The first-half 2025 payment report also gives an aggregate figure for POS transactions. It is withheld here "
               "because its definition and period need a methodology note before public use. The monthly releases are shown "
               "because each reports POS transactions for one month within the same reporting scope, so their published totals "
               "can be read side by side. Where a release's displayed percentage change does not match the published monthly "
               "totals, the mismatch is recorded as a discrepancy within the source.")
NEW_NOTE_AR = ("يذكر تقرير المدفوعات للنصف الأول من 2025 أيضًا رقمًا إجماليًا لمعاملات نقاط البيع، وهو محجوب هنا لأن تعريفه "
               "وفترته يحتاجان إلى ملاحظة منهجية قبل النشر. أما الإصدارات الشهرية فتُعرض لأن كلًّا منها يذكر معاملات نقاط البيع "
               "لشهر واحد ضمن نطاق الإبلاغ نفسه، فيمكن قراءة إجمالياتها المنشورة جنبًا إلى جنب. وحيث لا تتفق نسبة التغير "
               "المعروضة في إصدارٍ ما مع الإجماليات الشهرية المنشورة، يُسجَّل الفرق بوصفه اختلافًا داخل المصدر.")
REVIEW = [  # (ui_id, new_en, new_ar, old_en, old_ar)
    ("UI-VIS-NOTE-POS-H1-WITHHELD", NEW_NOTE_EN, NEW_NOTE_AR, OLD_NOTE_EN, OLD_NOTE_AR),
    ("UI-VIS-TH-STEP", None, "الحلقة", None, "الخطوة"),
    ("UI-VIS-TH-GROUP", "Group or gap", "الفئة أو الفجوة", "Group", "الفئة"),
    ("UI-VIS-TH-DATE", "Date or period", "التاريخ أو الفترة", "Date", "التاريخ"),
    ("UI-LAND-NO-NEXT", "No page in this base to verify it, and no measurement priority",
     "لا توجد في قاعدة الأدلة هذه صفحة للتحقق منه ولا أولوية قياس",
     "No domain page or measurement priority in this base", "لا توجد صفحة مجال ولا أولوية قياس في قاعدة الأدلة هذه"),
]
TH_SOURCE = [("UI-VIS-TH-SOURCE", "Source", "المصدر",
              "RC-11b. The heading of a row-header column whose rows are publications (the source-comparison table).")]

B12_RULE = "RC-12 (Part B B12). A governed string of a text-first contract's table, bound from governed rows."
B12 = [
    ("UI-VIS-RESULT-NOT-HELD", "No observed result is held in the evidence base — not zero",
     "لا تتضمن قاعدة الأدلة نتيجة مرصودة — ليست صفرًا", B12_RULE),
    ("UI-VIS-TH-BASE", "Out of", "من أصل", B12_RULE),
    ("UI-VIS-UNIT-FIRMS-SURVEYED", "formal establishments surveyed", "منشأة رسمية شملها المسح", B12_RULE),
    ("UI-VIS-UNIT-VALID-RESPONSES", "valid loan-source responses", "استجابة صالحة لسؤال مصدر القرض", B12_RULE),
    ("UI-VIS-NOTE-FIRM-LOAN-SUBSET",
     "Not established: whether the loan-source responses below come from the establishments with a line of credit above.",
     "لم يثبت ما إذا كانت الاستجابات لسؤال مصدر القرض أدناه صادرة عن المنشآت التي أفادت بامتلاك خط ائتمان أعلاه.", B12_RULE),
]
B13_RULE = "RC-12 (Part B B13). The research library on /data/: filters, order, backlinks and locator labels."
B13 = [
    ("UI-DATA-FILTER-TYPE", "Document type", "نوع الوثيقة", B13_RULE),
    ("UI-DATA-FILTER-PUBLISHER", "Publisher", "الناشر", B13_RULE),
    ("UI-DATA-FILTER-YEAR", "Year of the document", "سنة الوثيقة", B13_RULE),
    ("UI-DATA-FILTER-DOMAIN", "Used on", "مستخدم في", B13_RULE),
    ("UI-DATA-FILTER-ANY", "Any", "الكل", B13_RULE),
    ("UI-DATA-FILTER-NOT-RECORDED", "Not recorded", "غير مسجّل", B13_RULE),
    ("UI-DATA-FILTER-CLEAR", "Clear filters", "مسح عوامل التصفية", B13_RULE),
    ("UI-DATA-SORT", "Order", "الترتيب", B13_RULE),
    ("UI-DATA-SORT-GROUPED", "As grouped", "حسب المجموعات", B13_RULE),
    ("UI-DATA-SORT-NEWEST", "Newest document first", "الوثائق الأحدث أولًا", B13_RULE),
    ("UI-DATA-READINGS-USING-SOURCE", "Evidence Readings using this source", "قراءات الأدلة التي تستخدم هذا المصدر", B13_RULE),
    ("UI-EVID-OPEN-ARCHIVED-COPY", "Open archived copy (web.archive.org)", "افتح النسخة المؤرشفة (web.archive.org)", B13_RULE),
]

SFD = "https://sfd-yemen.org/uploads/issues/"
MOVED = OrderedDict([  # source: (old locator, the publisher's current address) — each read; see LINK_CHECK.md
    ("SRC-SFD-Q1-2012-001", ("https://www.sfd-yemen.org/uploads/issues/DESIGN%201st%20NL%202012%20-%20No-20121222-162100.pdf",
                             SFD + "Newsletter-Quarter-1-2012.pdf")),
    ("SRC-SFD-Q2-2014-001", ("https://www.sfd-yemen.org/uploads/issues/SFD_Nwesletter_en66%20final-20141224-124427.pdf",
                             SFD + "Newsletter-Quarter-2-2014.pdf")),
    ("SRC-SFD-Q4-2017-001", ("https://www.sfd-yemen.org/uploads/issues/Newsletter%20Eng%204th-2017%20%20-20-4-18-20190129-214133.pdf",
                             SFD + "Newsletter-Quarter-4-2017.pdf")),
    ("SRC-SFD-Q1-2019-001", ("https://www.sfd-yemen.org/uploads/issues/1st%20NL%202019-20200123-102323.pdf",
                             SFD + "Newsletter-Quarter-1-2019.pdf")),
    ("SRC-SFD-Q4-2020-001", ("https://sfd-yemen.org/uploads/issues/4th%20NL%202020-20211125-090031.pdf",
                             SFD + "Newsletter-Quarter-4-2020.pdf")),
])
WB = "https://web.archive.org/web/"
ARCHIVED = OrderedDict([  # source: (old locator, the web.archive.org copy of that address)
    ("SRC-SFD-Q2-2013-001", ("https://sfd.sfd-yemen.org/uploads/issues/SFD_Nwesletter_en-62-2%20NEW2-20140312-132450.pdf",
                             WB + "20240619144721/https://sfd.sfd-yemen.org/uploads/issues/SFD_Nwesletter_en-62-2%20NEW2-20140312-132450.pdf")),
    ("SRC-SFD-NEWSLETTER-2000-Q4-001", ("https://www.sfd-yemen.org/uploads/issues/Newsletter-12-ENGLISH%20-20120718-113859.pdf",
                                        WB + "20250213094943/https://sfd-yemen.org/uploads/issues/Newsletter-12-ENGLISH%20-20120718-113859.pdf")),
    ("SRC-SFD-MF-HISTORY-TOR-2012-001", ("https://www.sfd-yemen.org/uploads/issues/Microfinance%20Islamic%20Products%20Study%28TOR%29-20130109-132034.pdf",
                                         WB + "20241006192210/https://sfd-yemen.org/uploads/issues/Microfinance%20Islamic%20Products%20Study(TOR)-20130109-132034.pdf")),
    ("SRC-SFD-SMED-LP-2023-NOV", ("https://smed.sfd-yemen.org/index.php/en/blog-4/aaflp1/477-nov-2023",
                                  WB + "20241112185856/https://smed.sfd-yemen.org/index.php/en/blog-4/aaflp1/477-nov-2023")),
])
CHECKED = "2026-10-03"


def relocate(s, finding, sid, old, new, keep_original):
    """Every Master cell that holds the old locator gets the new one (the source library, the MFI rows that carry it, a
    record's text); the source library row records the check date and, for an archived copy, keeps the original."""
    hits = 0
    for sheet in SHEETS:
        g = s.grid(sheet)
        for i, row in enumerate(g, 1):
            for j, v in enumerate(row or [], 1):
                if isinstance(v, str) and old in v:
                    s.replace(finding, sheet, i, j, old, new, f"{sid} locator")
                    hits += 1
    if hits < 2:
        raise TxError(f"{finding}: {sid}: the old locator was found in {hits} cell(s); expected the source row and its data rows")
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    if t15.get(sid, "primary_url") != new:
        raise TxError(f"{finding}: {sid}: primary_url did not move")
    t15.set(finding, sid, "retrieval_date", CHECKED, t15.get(sid, "retrieval_date"))
    if keep_original:
        cur = t15.get(sid, "additional_urls")
        lst = json.loads(cur) if cur not in (None, "") else []
        if old in lst:
            raise TxError(f"{finding}: {sid}: the original is already an additional locator")
        t15.set(finding, sid, "additional_urls", json.dumps(lst + [old]), cur)
    return hits


SHEETS = ["06_EVIDENCE_OBJECTS", "15_SOURCE_LIBRARY", "21_MFI_DATA"]   # where the link check found these locators


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for ui_id, en, ar, old_en, old_ar in REVIEW:
        set_ui(s, F11B, ui_id, en, ar, old_en, old_ar)
    insert_ui_rows(s, F11B, TH_SOURCE)
    insert_ui_rows(s, F12, B12)
    insert_ui_rows(s, F13, B13)
    cells = OrderedDict()
    for sid, (old, new) in MOVED.items():
        cells[sid] = relocate(s, F13D, sid, old, new, keep_original=False)
    for sid, (old, new) in ARCHIVED.items():
        cells[sid] = relocate(s, F13D, sid, old, new, keep_original=True)
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-12"), ("summary", "B12 tables; B13 library and locators; RC-11 review"),
                                           ("items", OrderedDict([("RC-11b", len(REVIEW) + 1), ("B12", len(B12)), ("B13", len(B13)),
                                                                  ("B13d_locators", cells)]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
