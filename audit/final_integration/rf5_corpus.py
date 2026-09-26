# -*- coding: utf-8 -*-
"""Transaction RF5 — whole public corpus acceptance (directive D7, session F5).

Nine independent reviewers read every governed public text of the Master (slices of 02, 03, 04, 05, 06, 10, 11, 14,
15) as Arabic, as English and for meaning parity; their 603 findings are inputs/F5_REVIEW_FINDINGS.json. The Team
Lead's decisions are inputs/F5_LEAD_RULINGS.json: every finding not rejected, superseded or deferred there is applied
as proposed or as modified.

  python3 rf5_corpus.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir> [--ledger-csv <path> [--append]]
                        [--tx RF5b --findings inputs/F5B_READINGS_FINDINGS.json --rulings inputs/F5B_LEAD_RULINGS.json]

RF5b is the same procedure for the ten Evidence Readings (08 fields and their 03 essay sections), reviewed in a second
pass after RF5 so that no public surface is left out of F5.

Every edit is an exact substring replacement that must occur exactly once in its cell. Evidence Record (06) and
visual (11) twins receive the same edit field by field; verification templates (04) are mirrored into 06. Two
structural changes follow the cell edits: one chronology row moves into date order and one duplicate source record
is retired.
"""
import csv, json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fi_lib import Session, Table, TxError, ui_rows  # noqa: E402
from ptc_lib import COL03  # noqa: E402

SHEETS = {"02": "02_SITE_MAP", "03": "03_PAGE_SECTIONS", "04": "04_NAV_UX", "05": "05_QUESTIONS", "06": "06_EVIDENCE_OBJECTS",
          "08": "08_READINGS", "10": "10_MEASUREMENT_AGENDA", "11": "11_VISUAL_LIBRARY", "14": "14_SYSTEM_CHRONOLOGY",
          "15": "15_SOURCE_LIBRARY"}
# fields that carry public prose, by sheet (sweeps touch only these; identifiers, bindings and locators are never swept)
PROSE = {
    "02_SITE_MAP": ["title_en", "title_ar", "meta_description_en", "meta_description_ar"],
    "03_PAGE_SECTIONS": ["heading_en", "body_en", "heading_ar", "body_ar"],
    "05_QUESTIONS": ["question_en", "question_ar", "user_gets_en", "user_gets_ar"],
    "06_EVIDENCE_OBJECTS": [f"{f}_{l}" for f in ("title", "summary", "definition", "period", "universe", "method", "limitations",
                                                 "currentness", "change_trigger", "verification") for l in ("en", "ar")],
    "08_READINGS": ["title_en", "title_ar", "question_en", "question_ar", "thesis_en", "thesis_ar", "prohibited_inference_en",
                    "prohibited_inference_ar", "evidence_period_en", "evidence_period_ar"],
    "10_MEASUREMENT_AGENDA": [f"{f}_{l}" for f in ("title", "dimensions", "current_evidence", "missing_evidence", "guardrail",
                                                   "unlocked_decision", "decisions_unlocked", "blocked_evidence", "feasibility",
                                                   "priority_basis", "what_changes", "recommended_visual") for l in ("en", "ar")] + ["domain_ar"],
    "11_VISUAL_LIBRARY": ["title_en", "title_ar", "question_en", "question_ar", "what_it_shows_en", "what_it_shows_ar",
                          "decision_value_en", "decision_value_ar", "denominator_universe", "period", "prohibited_inference_en",
                          "prohibited_inference_ar", "accessible_summary_en", "accessible_summary_ar", "period_ar", "universe_ar"],
    "14_SYSTEM_CHRONOLOGY": ["period_en", "period_ar", "fact_en", "fact_ar", "system_implication_en", "system_implication_ar",
                             "fi_relevance_en", "fi_relevance_ar", "does_not_establish_en", "does_not_establish_ar"],
    "15_SOURCE_LIBRARY": ["display_title", "display_title_ar", "why_it_matters", "why_it_matters_ar", "does_not_establish",
                          "does_not_establish_ar", "publisher", "publisher_ar", "resource_category", "resource_category_ar",
                          "document_label", "document_label_ar"],
}
ALIAS = {"H_EN": "heading_en", "B_EN": "body_en", "H_AR": "heading_ar", "B_AR": "body_ar", "TITLE_EN": "title_en",
         "TITLE_AR": "title_ar", "META_EN": "meta_description_en", "META_AR": "meta_description_ar"}
# 06 Evidence Record field <-> 11 visual field (identical text in the two twins of a VIS-* object)
TWIN = {"title_en": "title_en", "title_ar": "title_ar", "summary_en": "accessible_summary_en", "summary_ar": "accessible_summary_ar",
        "limitations_en": "prohibited_inference_en", "limitations_ar": "prohibited_inference_ar", "period_en": "period",
        "period_ar": "period_ar", "universe_en": "denominator_universe", "universe_ar": "universe_ar"}
TWIN_REV = {v: k for k, v in TWIN.items()}
VERIFY_TEMPLATES = ["UI-VERIFY-BOUND", "UI-VERIFY-UNLISTED", "UI-VERIFY-PARTIAL", "UI-VERIFY-COMPOSITE",
                    "UI-VERIFY-COMPOSITE-UNLISTED", "UI-EVID-UNBOUND", "UI-EVID-FRAMING"]


class Editor:
    def __init__(self, s):
        self.s, self.tables, self.done, self.log = s, {}, set(), []

    def table(self, sheet):
        if sheet not in self.tables:
            self.tables[sheet] = Table(self.s, sheet)
        return self.tables[sheet]

    def locate(self, code, key, field):
        sheet = SHEETS[str(code)[:2]]
        field = ALIAS.get(field, field)
        if sheet == "03_PAGE_SECTIONS":
            route, order = key.rsplit(" s", 1)
            part, lang = field.rsplit("_", 1)
            return sheet, self.s.section_row(route, int(order), lang), COL03[field], f"{route}#s{order}.{field}"
        if sheet == "04_NAV_UX":
            ui, _ = ui_rows(self.s)
            if key not in ui:
                raise TxError(f"04 has no {key}")
            return sheet, ui[key], {"label_en": 2, "label_ar": 3}[field], f"{key}.{field}"
        t = self.table(sheet)
        if key not in t.rows:
            raise TxError(f"{sheet} has no row {key}")
        for f in (field, field[:-3] if field.endswith("_en") else None):
            if f and t.head.count(f) == 1:
                return sheet, t.rows[key], t.head.index(f) + 1, f"{key}.{f}"
        raise TxError(f"{sheet}: no column {field}")

    def replace(self, fid, code, key, field, old, new, origin):
        sheet, row, col, label = self.locate(code, key, field)
        sig = (sheet, row, col, old, new)
        cur = self.s.ed.get_value(sheet, row, col)
        if sig in self.done:
            self.log.append((fid, origin, label, "already applied"))
            return
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{fid} ({origin}): {label}: guard occurs {0 if not isinstance(cur, str) else cur.count(old)} times: {old[:90]!r}")
        self.s.set(fid, sheet, row, col, cur.replace(old, new), cur, label)
        self.done.add(sig)
        self.log.append((fid, origin, label, "applied"))
        # twin propagation 06 <-> 11
        field = ALIAS.get(field, field)
        twin = None
        if sheet == "06_EVIDENCE_OBJECTS" and field in TWIN:
            twin = ("11", TWIN[field])
        elif sheet == "11_VISUAL_LIBRARY" and field in TWIN_REV:
            twin = ("06", TWIN_REV[field])
        if twin and key in self.table(SHEETS[twin[0]]).rows:
            tsheet, trow, tcol, tlabel = self.locate(twin[0], key, twin[1])
            tcur = self.s.ed.get_value(tsheet, trow, tcol)
            if isinstance(tcur, str) and tcur.count(old) == 1 and (tsheet, trow, tcol, old, new) not in self.done:
                self.s.set(fid, tsheet, trow, tcol, tcur.replace(old, new), tcur, tlabel + " (twin)")
                self.done.add((tsheet, trow, tcol, old, new))
                self.log.append((fid, "twin", tlabel, "applied"))
            elif isinstance(tcur, str) and tcur.count(old) > 1:
                raise TxError(f"{fid}: twin {tlabel} holds the guard {tcur.count(old)} times")


def edits_from(findings, rulings):
    """Yield (finding_id, decision, reason, [edit, ...]) for every finding, in file order."""
    rej, sup, dfr, mod = rulings["reject"], rulings["superseded"], rulings["deferred"], rulings["modify"]
    structural = {st["id"] for st in rulings.get("structural", [])}
    for x in findings:
        i = x["id"]
        if i in structural:
            continue                      # recorded by the structural pass
        if i in rej:
            yield i, "REJECTED", rej[i], []
            continue
        if i in sup:
            yield i, "SUPERSEDED", "by " + sup[i], []
            continue
        if i in dfr:
            yield i, "DEFERRED", f"{dfr[i]['class']}: {dfr[i]['reason']}", []
            continue
        m = mod.get(i, {})
        if not m and (x["replacement"] in (None, "None") or x["replacement"] == x["current"]):
            yield i, "NO_TEXT_CHANGE", "query answered without a text change", []
            continue
        e = [dict(sheet=x["sheet"], key=x["key"], field=x["field"], current=m.get("current", x["current"]),
                  replacement=m.get("replacement", x["replacement"]), origin="finding")]
        o = x.get("other_language_change")
        mo = m.get("olc")
        if o or mo:
            o = dict(o or {})
            o.update(mo or {})
            e.append(dict(sheet=o.get("sheet", x["sheet"]), key=o.get("key", x["key"]), field=o["field"],
                          current=o["current"], replacement=o["replacement"], origin="other language"))
        yield i, ("ACCEPTED_MODIFIED" if m else "ACCEPTED"), m.get("reason", ""), e


def sweep(s, ed, sw):
    """Replace every occurrence of sw['old'] in the public prose fields of one language (and the 04 labels)."""
    lang, old, new, n = sw["lang"], sw["old"], sw["new"], 0
    for sheet, fields in PROSE.items():
        g = s.grid(sheet)
        head = [str(x) if x is not None else None for x in g[3]]
        for f in fields:
            is_ar = f.endswith("_ar")
            if (lang == "ar") != is_ar:
                continue
            c = head.index(f)
            for i, r in enumerate(g[4:], start=5):
                v = r[c] if c < len(r) else None
                if isinstance(v, str) and old in v:
                    s.set(sw["id"], sheet, i, c + 1, v.replace(old, new), v, f"{r[0]}.{f}")
                    ed.log.append((sw["id"], "sweep", f"{r[0]}.{f}", "applied"))
                    n += 1
    ui, _ = ui_rows(s)
    col = 3 if lang == "ar" else 2
    for uid, row in ui.items():
        v = s.ed.get_value("04_NAV_UX", row, col)
        if isinstance(v, str) and old in v:
            s.set(sw["id"], "04_NAV_UX", row, col, v.replace(old, new), v, f"{uid}.label_{lang}")
            ed.log.append((sw["id"], "sweep", f"{uid}.label_{lang}", "applied"))
            n += 1
    return n


def move_row(s, st, sheet, key, before):
    t = Table(s, sheet)
    src, dst = t.rows[key], t.rows[before]
    if not dst < src:
        raise TxError(f"move_row {key}: expected to move up")
    g = s.grid(sheet)
    vals = {c + 1: v for c, v in enumerate(g[src - 1]) if v not in (None, "")}
    s.ed.delete_rows(sheet, src, src)
    s.ed.insert_rows(sheet, dst, [vals])
    s.ledger.append(OrderedDict([("finding", st["id"]), ("sheet", sheet), ("row", dst), ("col", None), ("field", f"{key} row"),
                                 ("old", f"row {src}"), ("new", f"row {dst} (before {before})")]))


def retire_source(s, st):
    key, keep = st["key"], st["keep"]
    from ptc_lib import Workbook
    for sheet in Workbook(s.src).sheet_names:
        hits = sum(1 for r in s.grid(sheet) for v in r if isinstance(v, str) and key in v)
        if hits != (1 if sheet == "15_SOURCE_LIBRARY" else 0):
            raise TxError(f"retire {key}: referenced {hits} time(s) in {sheet}")
    t = Table(s, "15_SOURCE_LIBRARY")
    col_ds = t.col("datasets_or_use")
    old_keep = t.get(keep, "datasets_or_use")
    gone = t.get(key, "datasets_or_use")
    uses = [u.strip() for u in (str(old_keep) + "," + str(gone)).replace(";", ",").split(",") if u.strip() and u.strip() != "None"]
    merged = ", ".join(OrderedDict.fromkeys(uses))
    t.set(st["id"], keep, "datasets_or_use", merged, old_keep)
    row = t.rows[key]
    s.ed.delete_rows("15_SOURCE_LIBRARY", row, row)
    s.ledger.append(OrderedDict([("finding", st["id"]), ("sheet", "15_SOURCE_LIBRARY"), ("row", row), ("col", None),
                                 ("field", f"{key} row"), ("old", key), ("new", f"retired (duplicate of {keep})")]))


def main():
    a = sys.argv[1:]
    src, out, ledger, work = a[:4]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    csv_path = opt("--ledger-csv", None)
    tx = opt("--tx", "RF5")
    findings = json.load(open(os.path.join(HERE, opt("--findings", "inputs/F5_REVIEW_FINDINGS.json")), encoding="utf-8"))
    rulings = json.load(open(os.path.join(HERE, opt("--rulings", "inputs/F5_LEAD_RULINGS.json")), encoding="utf-8"))
    s = Session(src, work)
    ed = Editor(s)
    ui_before = {}
    ui, _ = ui_rows(s)
    for k in VERIFY_TEMPLATES:
        ui_before[k] = (s.ed.get_value("04_NAV_UX", ui[k], 2), s.ed.get_value("04_NAV_UX", ui[k], 3))
    rows = []
    for fid, decision, reason, edits in edits_from(findings, rulings):
        for e in edits:
            ed.replace(fid, e["sheet"], e["key"], e["field"], e["current"], e["replacement"], e["origin"])
        rows.append((fid, decision, reason))
    for le in rulings["lead_edits"]:
        ed.replace(le["id"], le["sheet"], le["key"], le["field"], le["current"], le["replacement"], "lead")
        rows.append((le["id"], "LEAD_EDIT", le["reason"]))
    for sw in rulings.get("sweeps", []):
        n = sweep(s, ed, sw)
        if not n:
            raise TxError(f"{sw['id']}: sweep found nothing to change")
        rows.append((sw["id"], "LEAD_SWEEP", f"{sw['reason']} ({n} cells)"))
    # closure rule v2: 06 verification cells carry the governed template of their lineage state
    ui, _ = ui_rows(s)
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for k in VERIFY_TEMPLATES:
        new_en, new_ar = s.ed.get_value("04_NAV_UX", ui[k], 2), s.ed.get_value("04_NAV_UX", ui[k], 3)
        for lang, old, new in (("en", ui_before[k][0], new_en), ("ar", ui_before[k][1], new_ar)):
            if old == new:
                continue
            for oid in t06.rows:
                if t06.get(oid, f"verification_{lang}") == old:
                    t06.set(tx + ":" + k, oid, f"verification_{lang}", new, old)
    for st in rulings.get("structural", []):
        if st["op"] == "move_row":
            move_row(s, st, st["sheet"], st["key"], st["before"])
        elif st["op"] == "retire_source":
            retire_source(s, st)
        rows.append((st["id"], "STRUCTURAL", st["reason"]))
    rep = s.save(out, ledger, {"transaction": tx, "summary": f"F5 whole public corpus acceptance: Lead decisions on {len(findings)} review findings"})
    if csv_path:
        f = {x["id"]: x for x in findings}
        applied = {}
        for fid, origin, label, state in ed.log:
            applied.setdefault(fid, []).append(f"{label} [{origin}{'' if state == 'applied' else ', ' + state}]")
        with open(csv_path, "a" if "--append" in a else "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            if "--append" not in a:
                w.writerow(["finding_id", "reviewer_slice", "severity", "lens", "sheet", "object", "field", "issue",
                            "lead_decision", "lead_reason", "cells_written"])
            for fid, decision, reason in rows:
                x = f.get(fid, {})
                w.writerow([fid, x.get("slice", "lead"), x.get("severity", "LEAD"), x.get("lens", ""), x.get("sheet", ""),
                            x.get("key", ""), x.get("field", ""), x.get("issue", ""), decision, reason,
                            " | ".join(applied.get(fid, []))])
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
