# -*- coding: utf-8 -*-
"""Transaction RP-F2 — one Master-first integration of the adjudicated Evidence Readings portfolio (Session F2).

  python3 rp_integration.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Input: rp_final_texts.py (F1 decisions; lineage only). Owners written, each once:
  08_READINGS         title, question, thesis (standfirst), prohibited inference, bindings, domain placement; the retired
                      column domain_context_routes becomes related_readings; new columns measurement_bindings,
                      evidence_period_en/ar, last_reviewed, featured
  03_PAGE_SECTIONS    the Reading body (sections 2..n) of every /readings/<slug>/ route, and the /readings/ definition;
                      surplus Reading section rows are deleted (the retired generic "Trace the reading" section among them)
  09_READING_SECTIONS the section index follows the new section count and semantic section ids
  02_SITE_MAP         /readings/ title
  11_VISUAL_LIBRARY   RV-CWR parity and wording (closes BIL-05 with 08 and 03)
  04_NAV_UX           governed interface copy for the Reading family
The staged Master is committed or rolled back by audit/tranche_b_execution/run_stage.py.
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError, insert_ui_rows  # noqa: E402
import rp_final_texts as T  # noqa: E402

S08, S03, S09 = "08_READINGS", "03_PAGE_SECTIONS", "09_READING_SECTIONS"
NEW08 = ["measurement_bindings", "evidence_period_en", "evidence_period_ar", "last_reviewed", "featured"]
F = "RP-F2"


def jl(x):
    return json.dumps(list(x), ensure_ascii=False, separators=(",", ":"))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # ------------------------------------------------------------------ 08 header: retire one relation, add five fields
    head = s.header(S08, 4)
    if head[:19][-1] != "domain_context_routes" or any(h not in (None, "") for h in head[19:]):
        raise TxError(f"08 header not as expected: {head}")
    s.set(F + ":08-HEADER", S08, 4, 19, "related_readings", "domain_context_routes", "08 header (domain_context_routes retired)")
    for i, name in enumerate(NEW08, start=20):
        s.set(F + ":08-HEADER", S08, 4, i, name, None, "08 header")
    t08 = Table(s, S08)
    ids = [r["reading_id"] for r in T.READINGS]
    if list(t08.rows) != sorted(t08.rows) or set(t08.rows) != set(ids):
        raise TxError(f"08 rows differ from the portfolio: {sorted(set(t08.rows) ^ set(ids))}")
    if sum(1 for r in T.READINGS if r["featured"]) != 1:
        raise TxError("exactly one featured Reading is required")

    route_of = {}
    for r in T.READINGS:
        rid = r["reading_id"]
        f = f"{F}:{rid}"
        route_of[rid] = t08.get(rid, "route").rstrip("/") + "/"
        for base in ("title", "question", "thesis", "prohibited_inference"):
            v = r.get(base)
            if v is None:
                continue
            for lang, txt in zip(("en", "ar"), v):
                t08.set(f, rid, f"{base}_{lang}", txt, t08.get(rid, f"{base}_{lang}"))
        for fld in ("claim_bindings", "evidence_bindings"):
            if r.get(fld) is not None:
                t08.set(f, rid, fld, jl(r[fld]), t08.get(rid, fld))
        t08.set(f, rid, "visual_bindings", jl(r["visual_bindings"]), t08.get(rid, "visual_bindings"))
        vb = json.loads(t08.get(rid, "verification_bindings"), object_pairs_hook=OrderedDict)
        claims = [c for c in vb["claim_ids"] if c not in (r.get("verification_remove") or [])]
        for c in r.get("verification_add") or []:
            if c not in claims:
                claims.append(c)
        if claims != vb["claim_ids"]:
            vb["claim_ids"] = claims
            t08.set(f, rid, "verification_bindings", json.dumps(vb, ensure_ascii=False), t08.get(rid, "verification_bindings"))
        t08.set(f, rid, "domain_surface_routes", "; ".join(r["domain_surface_routes"]), t08.get(rid, "domain_surface_routes"))
        t08.set(f, rid, "related_readings", jl(r["related_readings"]), t08.get(rid, "related_readings"))
        t08.set(f, rid, "measurement_bindings", jl(r["measurement_bindings"]), None)
        t08.set(f, rid, "evidence_period_en", r["evidence_period"][0], None)
        t08.set(f, rid, "evidence_period_ar", r["evidence_period"][1], None)
        t08.set(f, rid, "last_reviewed", T.REVIEWED, None)
        if r["featured"]:
            t08.set(f, rid, "featured", "FEATURED", None)

    # ------------------------------------------------------------------ 03 Reading bodies (cell writes first; deletions last)
    g03 = s.grid(S03)
    rows03 = {}
    for i, row in enumerate(g03, 1):
        if i > 4 and row and row[0] and row[1] not in (None, ""):
            rows03.setdefault(row[0], {})[int(float(row[1]))] = i
    drop03 = []
    for r in T.READINGS:
        rid, route = r["reading_id"], route_of[r["reading_id"]]
        have = rows03.get(route) or {}
        if sorted(have) != list(range(2, 10)):
            raise TxError(f"03 {route}: expected section orders 2-9, found {sorted(have)}")
        n = len(r["sections"])
        if not 3 <= n <= 8 or r["sections"][-1][0] != "what_would_change":
            raise TxError(f"{rid}: a Reading has 3-8 body sections ending with 'what would change this reading'")
        for k, (sid, he, ha, be, ba) in enumerate(r["sections"], start=2):
            row = have[k]
            for col, val in ((3, None), (4, he), (5, be), (6, ha), (7, ba)):
                s.set(f"{F}:{rid}", S03, row, col, val, s.ed.get_value(S03, row, col), f"{route}#s{k}.c{col}")
        drop03 += [have[k] for k in range(n + 2, 10)]
    idx = rows03["/readings/"]
    if sorted(idx) != [1]:
        raise TxError("/readings/ has more than one 03 section")
    for col, val in ((4, None), (5, T.INDEX["definition"][0]), (6, None), (7, T.INDEX["definition"][1])):
        s.set(F + ":INDEX", S03, idx[1], col, val, s.ed.get_value(S03, idx[1], col), f"/readings/#s1.c{col}")

    # ------------------------------------------------------------------ 09 section index
    g09 = s.grid(S09)
    rows09 = {}
    for i, row in enumerate(g09, 1):
        if i > 4 and row and row[0]:
            rows09.setdefault(row[0], {})[int(float(row[1]))] = i
    drop09 = []
    for r in T.READINGS:
        rid = r["reading_id"]
        have = rows09.get(rid) or {}
        if sorted(have) != list(range(1, 10)):
            raise TxError(f"09 {rid}: expected orders 1-9, found {sorted(have)}")
        for k, sec in enumerate(r["sections"], start=2):
            s.set(f"{F}:{rid}", S09, have[k], 3, sec[0], s.ed.get_value(S09, have[k], 3), f"{rid}#s{k}.section_id")
        drop09 += [have[k] for k in range(len(r["sections"]) + 2, 10)]

    # ------------------------------------------------------------------ 02 /readings/ title
    t02 = Table(s, "02_SITE_MAP")
    for lang, txt in zip(("en", "ar"), T.INDEX["title"]):
        t02.set(F + ":INDEX", "/readings/", f"title_{lang}", txt, t02.get("/readings/", f"title_{lang}"))

    # ------------------------------------------------------------------ 11 Reading visuals (BIL-05)
    t11 = Table(s, "11_VISUAL_LIBRARY")
    for vid, fld, old, new in T.VISUALS:
        cur = t11.get(vid, fld)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"11 {vid}.{fld}: guard text not found once")
        t11.set(F + ":BIL-05", vid, fld, cur.replace(old, new), cur)

    # ------------------------------------------------------------------ 04 governed interface copy
    insert_ui_rows(s, F + ":UI", T.UI_NEW)

    # ------------------------------------------------------------------ deletions, bottom-up so earlier rows keep their index
    for sheet, rows in ((S03, drop03), (S09, drop09)):
        for row in sorted(rows, reverse=True):
            s.ed.delete_rows(sheet, row, row)
            s.ledger.append(OrderedDict([("finding", F + ":DELETE"), ("sheet", sheet), ("row", row), ("col", None),
                                         ("field", "row deleted"), ("old", None), ("new", None)]))

    rep = s.save(out, ledger, {"transaction": F, "summary": "Evidence Readings portfolio integrated Master-first (F1 adjudication); BIL-05 closed"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
