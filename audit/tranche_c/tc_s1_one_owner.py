# -*- coding: utf-8 -*-
"""Tranche C transaction TC-S1 — one owner per text (structural; no new facts).

  python3 tc_s1_one_owner.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Panel findings: EN-01 (a Reading carried two public titles), TOOL-11 / JRN-13 / VIS-05 (record <title> differed from its
H1), PAY-18 (claim cards and records carried different boundary text), TRUST-16 / EN-23 (a 110-times repeated template
stored in 03). Decision (Lead): 06 owns Evidence Record text and 08 owns Reading titles. From this transaction:
  * 07_PUBLIC_CLAIMS keeps claim metadata only (claim_id, theme, claim_type, evidence_badge, evidence_inputs,
    public_routes); headline/copy/does_not_prove/change_trigger derive from 06 (generator rule public_claims).
  * 02_SITE_MAP keeps the route registry; full_copy is derived (no longer stored); the title cells of Evidence Record
    and Reading routes are blank and derive from 06 / 08 (generator rule site_map).
  * 03_PAGE_SECTIONS holds no Evidence Record route sections; section 1 derives from the 06 summary and section 2 from
    the governed reading guidance (two new 04 interface-copy rows; generator rule page_sections).
Every removed value is archived in the ledger (lineage), so nothing is lost silently.
"""
import os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "pre_tranche_c"))
from ptc_lib import Session, TxError          # noqa: E402
from projection.master_reader import Workbook  # noqa: E402

GUIDE_H = ("UI-EVID-READING-GUIDANCE-H", "How to read this evidence", "كيف تقرأ هذا الدليل",
           "Tranche C TC-S1. Heading of the reading guidance on every Evidence Record (was 03 section 2 on 110 routes).")
GUIDE_EN = ("Read this evidence within the definition, population or group covered, calculation base where relevant, period, "
            "geography and method shown on the page. Before reusing or comparing it, check the source, limitations, evidence "
            "date and correction history. If a value or source link is unavailable, the page says so rather than filling the "
            "gap by inference. This resource does not host source files; where an original-source link is given, check the "
            "publisher’s terms before republishing.")
GUIDE_AR = ("يُقرأ هذا الدليل ضمن التعريف، والمجتمع الذي ينطبق عليه الرقم أو قاعدة الاحتساب عند الحاجة، والفترة، والجغرافيا، "
            "والطريقة المبينة في الصفحة. وقبل إعادة استخدامه أو مقارنته، راجع المصدر والحدود وحداثة الدليل وسجل التصحيح. وإذا "
            "كانت قيمة أو وصلة مصدر غير متاحة، تُذكر الفجوة صراحةً بدل ملئها بالاستنتاج. ولا يستضيف هذا المورد ملفات المصادر؛ "
            "وحيثما وُجد رابط للمصدر الأصلي، تحقق من شروط الناشر قبل إعادة النشر.")
OLD_GUIDE_TAIL_EN = "Download and reuse are offered only where source rights permit."
GUIDE_B = ("UI-EVID-READING-GUIDANCE", GUIDE_EN, GUIDE_AR,
           "Tranche C TC-S1. Reading guidance on every Evidence Record; TRUST-03/EN-23: no download is offered, so the old "
           "'Download and reuse are offered only where source rights permit' sentence is replaced.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    wb = Workbook(src)
    arch = OrderedDict()

    # ---- 06 / 08 owners -------------------------------------------------------------------------------
    g06 = wb.grid("06_EVIDENCE_OBJECTS"); h06 = [str(x) for x in g06[3]]
    t06 = {r[0]: (r[h06.index("title_en")], r[h06.index("title_ar")]) for r in g06[4:] if r and r[0]}
    g08 = wb.grid("08_READINGS"); h08 = [str(x) for x in g08[3]]
    t08 = {"/" + str(r[h08.index("route")]).strip("/") + "/": (r[h08.index("title_en")], r[h08.index("title_ar")]) for r in g08[4:] if r and r[0]}

    # ---- 07: metadata only ------------------------------------------------------------------------------
    g07 = wb.grid("07_PUBLIC_CLAIMS"); h07 = [str(x) if x is not None else None for x in g07[3]]
    want07 = ["claim_id", "theme", "claim_type", "headline_en", "headline_ar", "copy_en", "copy_ar", "evidence_badge", "evidence_inputs",
              "does_not_prove_en", "does_not_prove_ar", "change_trigger_en", "change_trigger_ar", "public_routes"]
    if h07[:14] != want07:
        raise TxError(f"07 header differs: {h07}")
    new07 = ["claim_id", "theme", "claim_type", "evidence_badge", "evidence_inputs", "public_routes"]
    arch["07_retired_text"] = OrderedDict()
    for i, r in enumerate(g07, 1):
        if i < 4 or not r or not any(v not in (None, "") for v in r):
            continue
        if i == 4:
            vals = new07
        else:
            if r[0] not in t06:
                raise TxError(f"07 {r[0]}: no 06 record")
            rec = dict(zip(want07, r))
            arch["07_retired_text"][r[0]] = OrderedDict((k, rec[k]) for k in want07[3:7] + want07[9:13])
            vals = [rec[k] for k in new07]
        for c in range(1, 15):
            cur = r[c - 1] if c - 1 < len(r) else None
            new = vals[c - 1] if c <= 6 else None
            s.set("TC-S1", "07_PUBLIC_CLAIMS", i, c, new, cur, f"07!r{i}c{c}")

    # ---- 02: registry only --------------------------------------------------------------------------------
    g02 = wb.grid("02_SITE_MAP"); h02 = [str(x) if x is not None else None for x in g02[3]]
    want02 = ["route", "page_class", "template_route", "instance_id", "title_en", "title_ar", "full_copy_en", "full_copy_ar",
              "meta_description_en", "meta_description_ar"]
    if h02[:10] != want02:
        raise TxError(f"02 header differs: {h02}")
    arch["02_titles_now_derived"] = OrderedDict()
    for i, r in enumerate(g02, 1):
        if i < 4 or not r or not any(v not in (None, "") for v in r):
            continue
        r = list(r) + [None] * (10 - len(r))
        if i == 4:
            s.set("TC-S1", "02_SITE_MAP", 4, 7, "meta_description_en", "full_copy_en", "02 header")
            s.set("TC-S1", "02_SITE_MAP", 4, 8, "meta_description_ar", "full_copy_ar", "02 header")
            s.set("TC-S1", "02_SITE_MAP", 4, 9, None, "meta_description_en", "02 header")
            s.set("TC-S1", "02_SITE_MAP", 4, 10, None, "meta_description_ar", "02 header")
            continue
        route, cls, inst = r[0], r[1], r[3]
        s.set("TC-S1", "02_SITE_MAP", i, 7, r[8], r[6], f"{route}.meta_description_en (full_copy retired)")
        s.set("TC-S1", "02_SITE_MAP", i, 8, r[9], r[7], f"{route}.meta_description_ar (full_copy retired)")
        s.set("TC-S1", "02_SITE_MAP", i, 9, None, r[8], f"{route}.col9")
        s.set("TC-S1", "02_SITE_MAP", i, 10, None, r[9], f"{route}.col10")
        owner = t06.get(inst) if cls == "evidence_detail" else t08.get(route) if cls == "reading_detail" else None
        if cls in ("evidence_detail", "reading_detail"):
            if owner is None:
                raise TxError(f"02 {route}: no owner")
            arch["02_titles_now_derived"][route] = OrderedDict([("02_title_en", r[4]), ("02_title_ar", r[5]),
                                                                ("owner_title_en", owner[0]), ("owner_title_ar", owner[1]),
                                                                ("differed", (r[4], r[5]) != tuple(owner))])
            s.set("TC-S1", "02_SITE_MAP", i, 5, None, r[4], f"{route}.title_en (derives from owner)")
            s.set("TC-S1", "02_SITE_MAP", i, 6, None, r[5], f"{route}.title_ar (derives from owner)")

    # ---- 04: governed reading guidance --------------------------------------------------------------------
    g04 = wb.grid("04_NAV_UX")
    ui = {x[0]: i for i, x in enumerate(g04, 1) if x and isinstance(x[0], str) and x[0].startswith("UI-")}
    if any(k in ui for k in (GUIDE_H[0], GUIDE_B[0])):
        raise TxError("guidance UI rows exist")
    last04 = max(i for i in ui.values() if i < 300)
    if any(c not in (None, "") for c in g04[last04]) or g04[last04 + 1][0] != "Trust navigation":
        raise TxError("04: interface-copy block end not where expected")

    # ---- 03: remove Evidence Record route sections (verify the template first) -----------------------------
    g03 = wb.grid("03_PAGE_SECTIONS")
    ev_rows = [i for i, r in enumerate(g03, 1) if i > 4 and r and isinstance(r[0], str) and r[0].startswith("/evidence/")
               and r[0] not in ("/evidence/", "/evidence/compare/")]
    arch["03_evidence_route_sections_retired"] = OrderedDict()
    for i in ev_rows:
        r = g03[i - 1]
        if str(r[1]) in ("2", "2.0"):
            if not (r[4] or "").endswith(OLD_GUIDE_TAIL_EN) or r[3] != "How to read this evidence":
                raise TxError(f"03 r{i}: section 2 is not the guidance template")
        elif str(r[1]) in ("1", "1.0"):
            arch["03_evidence_route_sections_retired"][r[0]] = OrderedDict([("s1_body_en", r[4]), ("s1_body_ar", r[6])])
        else:
            raise TxError(f"03 r{i}: unexpected section order {r[1]}")
    if len(ev_rows) != 220:
        raise TxError(f"03: {len(ev_rows)} evidence-route rows, expected 220")
    # contiguous runs, deleted bottom-up; then the 04 insertion (different sheet, independent)
    runs = []
    for i in ev_rows:
        if runs and runs[-1][1] == i - 1:
            runs[-1][1] = i
        else:
            runs.append([i, i])
    for a, b in reversed(runs):
        s.ed.delete_rows("03_PAGE_SECTIONS", a, b)
    s.ledger.append(OrderedDict([("finding", "TC-S1"), ("sheet", "03_PAGE_SECTIONS"), ("row", None), ("col", None),
                                 ("field", f"deleted {len(ev_rows)} Evidence Record route rows in {len(runs)} runs"), ("old", None), ("new", None)]))
    s.ed.insert_rows("04_NAV_UX", last04 + 1, [{1: a, 2: b, 3: c, 4: d} for a, b, c, d in (GUIDE_H, GUIDE_B)])
    for a, b, c, _ in (GUIDE_H, GUIDE_B):
        s.ledger.append(OrderedDict([("finding", "TC-S1"), ("sheet", "04_NAV_UX"), ("row", None), ("col", None), ("field", a), ("old", None), ("new", b + " || " + c)]))

    rep = s.save(out, ledger, [("transaction", "TC-S1"), ("scope", "one owner per text: 07 metadata only; 02 registry only (full copy and "
                               "Evidence/Reading titles derived); 03 Evidence Record sections derived; 04 reading guidance"),
                               ("archive", arch)])
    print(f"TC-S1 staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
