# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-5 — the Part B editorial passes (audit/release_candidate/INSTRUCTIONS.md, Part B items
B2 and B3), with three findings carried from Part A.

  python3 rc_5_editorial.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir> <b2_proposals.json> <b3_proposals.json>

Under the owner's Part B designation (addendum of 2 October 2026) the session is English and Arabic editor; the proposals
were drafted by two editor passes (the senior Arab economic editor, B2; the senior institutional English editor, B3) and
are recorded, with every FROM and TO, in audit/release_candidate/ARABIC_EDITORIAL_LEDGER.md and
ENGLISH_EDITORIAL_LEDGER.md. This script applies them as exact-value-guarded writes:

  * a cell is located by its sheet, its column and its exact current text (rows can move between transactions); a
    meta-description cell, blank today, by its route;
  * three cells touched by both passes are composed (the Home §3 English body; the /people/ §1 pair) or decided (the
    Home §3 rubric takes the English pass's "Evidence" / «الدليل», the label the domain pages use; B2-007 is not applied);
  * B2 item g adds the Arabic period columns reference_state_ar (Provider universe block) and reference_period_ar (Wallet
    count reconciliation block) of 22_PROVIDERS_DATA — the four English-only periods the Arabic matrix printed;
  * B2 item h adds UI-VIS-MATRIX-CONTEXT ("Context:" / «السياق:»), the lead-in of the payment-system operators' context
    events on the provider matrix (both escalated in RC-3's review);
  * B2 item f removes, in both languages, the sentence of five accessible summaries that restated their boundary
    (escalated by the A3 implementation).
No number changes except the day numbers of the Findex fieldwork window, which the period fields already govern.
"""
import json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, TxError, insert_ui_rows  # noqa: E402

COMPOSE = {
    # (sheet, header) of the cell, its exact FROM, and the edits composed from both passes, as (old, new) replacements
    "home_s3_en": ("03_PAGE_SECTIONS", "body_en",
                   [("(fieldwork November 2022 to January 2023;", "(fieldwork 7 November 2022 to 9 January 2023;"),          # B2-006 (d)
                    ("Separately, POS terminals reported", "Separately, point-of-sale (POS) terminals reported")]),          # B3-003 (a)
    "people_s1_en": ("03_PAGE_SECTIONS", "body_en",
                     [("Global Findex 2021 wave (Yemen fieldwork November 2022 to January 2023)",
                       "Global Findex 2021 wave (survey round; Yemen fieldwork 7 November 2022 to 9 January 2023)")]),       # B2-101 (d) + B3-015 (a)
    "people_s1_ar": ("03_PAGE_SECTIONS", "body_ar",
                     [("لعام 2021، التي نُفذ عملها الميداني في اليمن بين نوفمبر 2022 ويناير 2023 —",
                       "لعام 2021، أي جولة المسح التي نُفذ عملها الميداني في اليمن من 7 نوفمبر 2022 إلى 9 يناير 2023 —")]),  # B2-101 + B3-015
}
SKIP = {"B2-007"}                                   # the Home rubric: B3-024 is applied instead
COMPOSED_BY = {"B2-006": "home_s3_en", "B3-003": "home_s3_en", "B2-101": "people_s1", "B3-015": "people_s1"}


def grid_header(s, sheet, col, row):
    """The header of a column at a row: the nearest row above (or the row itself) whose cells name *_en / *_ar fields."""
    g = s.grid(sheet)
    for i in range(row, 0, -1):
        r = g[i - 1] if i - 1 < len(g) else None
        if r and any(isinstance(c, str) and re.search(r"_(en|ar)$", c) for c in r):
            return r[col - 1] if col - 1 < len(r) else None
    return None


def locate(s, sheet, col, text, where, key=None, hint=None):
    """The one row of `sheet` whose cell in `col` equals `text` exactly; where the same text sits in several rows (two
    records sharing a governed definition), the row whose key (first cell) is the proposal's, then the proposal's row."""
    g = s.grid(sheet)
    rows = [i for i, r in enumerate(g, 1) if r and col - 1 < len(r) and r[col - 1] == text]
    if len(rows) > 1 and key is not None:
        rows = [i for i in rows if g[i - 1][0] == key] or rows
    if len(rows) > 1 and hint in rows:
        rows = [hint]
    if len(rows) != 1:
        raise TxError(f"{where}: {sheet} c{col} expected text found {len(rows)} times")
    return rows[0]


def write(s, finding, sheet, col, old, new, field, key=None, hint=None):
    row = locate(s, sheet, col, old, f"{finding} {field}", key, hint)
    s.set(finding, sheet, row, col, new, old, field)
    return row


def main():
    src, out, ledger, work, b2p, b3p = sys.argv[1:7]
    fix_paths = sys.argv[7:]          # the independent reviewers' corrections (applied on top of the proposals)
    b2 = json.load(open(b2p, encoding="utf-8"))
    b3 = json.load(open(b3p, encoding="utf-8"))
    fixes = [json.load(open(f, encoding="utf-8")) for f in fix_paths]
    by_id = {p["id"]: p for p in b2 + b3}
    for fx in fixes:
        for pid, upd in (fx.get("overrides") or {}).items():
            if pid not in by_id:
                raise TxError(f"review override for unknown proposal {pid}")
            by_id[pid].update(upd)
    s = Session(src, work)
    notes = OrderedDict()
    applied = {"B2": 0, "B3": 0, "B2_en": 0, "B3_pair": 0, "composed": 0}

    # ---- the composed cells first (their FROM is the original text both passes read)
    home_en = next(p for p in b2 if p["id"] == "B2-006")["en_counterpart_text"]
    people_en = next(p for p in b2 if p["id"] == "B2-101")["en_counterpart_text"]
    people_ar = next(p for p in b2 if p["id"] == "B2-101")["from"]
    for key, old in (("home_s3_en", home_en), ("people_s1_en", people_en), ("people_s1_ar", people_ar)):
        sheet, header, edits = COMPOSE[key]
        new = old
        for a, b in edits:
            if new.count(a) != 1:
                raise TxError(f"compose {key}: {a[:40]!r} found {new.count(a)} times")
            new = new.replace(a, b)
        col = 5 if header.endswith("_en") else 7
        write(s, f"RC-5:COMPOSED:{key}", sheet, col, old, new, f"{key}.{header}")
        applied["composed"] += 1
    # the Home §3 Arabic body: B2-006's own Arabic edit stands alone
    p = next(p for p in b2 if p["id"] == "B2-006")
    write(s, "RC-5:B2-006", p["sheet"], p["col"], p["from"], p["to"], f'{p["key"]}.{p["header"]}')
    applied["B2"] += 1

    # ---- B2 (Arabic editor): items a–f; g and h below
    for p in b2:
        if p["id"] in SKIP or p["item"] in ("g", "h") or p["id"] in ("B2-006", "B2-101"):
            continue
        write(s, f"RC-5:{p['id']}", p["sheet"], p["col"], p["from"], p["to"], f'{p["key"]}.{p["header"]}', p["key"], p["row"])
        applied["B2"] += 1
        if p.get("en_to") is not None:
            write(s, f"RC-5:{p['id']}:en", p["sheet"], p["en_counterpart_col"], p["en_counterpart_text"], p["en_to"],
                  f'{p["key"]}.{p["en_counterpart_header"]}', p["key"], p.get("en_counterpart_row"))
            applied["B2_en"] += 1

    # ---- B3 (English editor): item a (terms) and item b (meta descriptions)
    g02 = s.grid("02_SITE_MAP")
    for p in b3:
        if p["id"] in ("B3-003", "B3-015"):
            continue
        if p["item"] == "b":
            rows = [i for i, r in enumerate(g02, 1) if r and r[0] == p["key"]]
            if len(rows) != 1:
                raise TxError(f"{p['id']}: route {p['key']} found {len(rows)} times in 02")
            for col, new, hdr in ((p["col"], p["to"], p["header"]), (p["pair_col"], p["pair_to"], p["pair_header"])):
                if grid_header(s, "02_SITE_MAP", col, rows[0]) != hdr:
                    raise TxError(f"{p['id']}: 02 column {col} is not {hdr}")
                s.set(f"RC-5:{p['id']}", "02_SITE_MAP", rows[0], col, new, None, f'{p["key"]}.{hdr}')
            applied["B3"] += 1
            applied["B3_pair"] += 1
            continue
        write(s, f"RC-5:{p['id']}", p["sheet"], p["col"], p["from"], p["to"], f'{p["key"]}.{p["header"]}', p["key"], p["row"])
        applied["B3"] += 1
        if p.get("pair_to") is not None:
            write(s, f"RC-5:{p['id']}:pair", p.get("pair_sheet") or p["sheet"], p["pair_col"], p["pair_from"], p["pair_to"],
                  f'{p.get("pair_key") or p["key"]}.{p["pair_header"]}', p.get("pair_key") or p["key"], p.get("pair_row"))
            applied["B3_pair"] += 1

    # ---- B2 item g: the Arabic period columns of 22_PROVIDERS_DATA
    g22 = s.grid("22_PROVIDERS_DATA")
    for header_key, new_col_name, en_field, values in (
            ("universe_id", "reference_state_ar", "reference_state", {"PUC-MFI-2026-01": next(p["to"] for p in b2 if p["id"] == "B2-004")}),
            ("wallet_count_object_id", "reference_period_ar", "reference_period",
             {"WCR-001": next(p["to"] for p in b2 if p["id"] == "B2-001"), "WCR-002": next(p["to"] for p in b2 if p["id"] == "B2-002"),
              "WCR-004": next(p["to"] for p in b2 if p["id"] == "B2-003")})):
        hdr_rows = [i for i, r in enumerate(g22, 1) if r and r[0] == header_key]
        if len(hdr_rows) != 1:
            raise TxError(f"22: header {header_key} found {len(hdr_rows)} times")
        h = hdr_rows[0]
        hdr = list(g22[h - 1])
        while hdr and hdr[-1] in (None, ""):
            hdr.pop()
        if new_col_name in hdr or en_field not in hdr:
            raise TxError(f"22 {header_key}: header not as expected ({new_col_name} present or {en_field} missing)")
        col = len(hdr) + 1
        s.set("RC-5:B2-g", "22_PROVIDERS_DATA", h, col, new_col_name, None, f"22 {header_key} header")
        en_col = hdr.index(en_field) + 1
        seen = set()
        for i in range(h + 1, len(g22) + 1):
            r = g22[i - 1]
            if not r or r[0] in (None, "") or r[0] == header_key:
                break
            if r[0] in values:
                if not r[en_col - 1]:
                    raise TxError(f"22 {r[0]}: no English {en_field}")
                s.set("RC-5:B2-g", "22_PROVIDERS_DATA", i, col, values[r[0]], None, f"{r[0]}.{new_col_name}")
                seen.add(r[0])
        if seen != set(values):
            raise TxError(f"22 {header_key}: rows not found {set(values) - seen}")

    # ---- B2 item h: the context lead-in on the provider matrix
    h = next(p for p in b2 if p["id"] == "B2-005")
    insert_ui_rows(s, "RC-5:B2-h", [("UI-VIS-MATRIX-CONTEXT", h["en_to"], h["to"],
                                     "RC-5 (Part B B2 h; RC-3 review escalation). VIS-PROVIDER-OBSERVABILITY: printed before the payment-system "
                                     "operators' institution events (REF-PAY-011…013) in the status dimension and its fallback cell, so they read "
                                     "as context, not as status decisions (scripts/yfie/visuals.py provider_matrix).")])

    # ---- the independent reviewers' corrections that are not overrides of a proposal
    def cells(sheet, key, header):
        g = s.grid(sheet)
        out_ = []
        for i, r in enumerate(g, 1):
            if r and r[0] == key:
                for j in range(1, len(r) + 1):
                    if grid_header(s, sheet, j, i) == header:
                        out_.append((i, j))
        return out_
    review_applied = []
    for fx in fixes:
        for sheet, header, key, old, new, why in fx.get("substring") or []:
            hits = [(i, j) for i, j in cells(sheet, key, header) if old in (s.ed.get_value(sheet, i, j) or "")]
            if len(hits) != 1:
                raise TxError(f"review fix ({why}) {sheet} {key} {header}: {old[:40]!r} found in {len(hits)} cells")
            i, j = hits[0]
            cur = s.ed.get_value(sheet, i, j)
            if cur.count(old) != 1:
                raise TxError(f"review fix ({why}): {old[:40]!r} occurs {cur.count(old)} times in the cell")
            s.set(f"RC-5:REVIEW:{why}", sheet, i, j, cur.replace(old, new), cur, f"{key}.{header}")
            review_applied.append(why)
        for sheet, header, key, new, why in fx.get("replace_cell") or []:
            hits = cells(sheet, key, header)
            if len(hits) != 1:
                raise TxError(f"review fix ({why}) {sheet} {key} {header}: {len(hits)} cells")
            i, j = hits[0]
            cur = s.ed.get_value(sheet, i, j)
            s.set(f"RC-5:REVIEW:{why}", sheet, i, j, new, cur, f"{key}.{header}")
            review_applied.append(why)
        for sheet, col, key, new, why in fx.get("col_replace") or []:
            rows = [i for i, r in enumerate(s.grid(sheet), 1) if r and r[0] == key]
            if len(rows) != 1:
                raise TxError(f"review fix ({why}) {sheet} {key}: {len(rows)} rows")
            cur = s.ed.get_value(sheet, rows[0], col)
            s.set(f"RC-5:REVIEW:{why}", sheet, rows[0], col, new, cur, f"{key}.c{col}")
            review_applied.append(why)
        # item f carried to the record summaries: the same restating sentence leaves 06 summary_en/_ar
        import difflib
        for vid in fx.get("drop_restating_in_06_summary") or []:
            for lang in ("en", "ar"):
                pf = next((p for p in b2 if p["item"] == "f" and p["key"] == vid and p["header"] == f"accessible_summary_{lang}"), None)
                pe = next((p for p in b2 if p["item"] == "f" and p["key"] == vid and p.get("en_counterpart_header") == f"accessible_summary_{lang}" and p.get("en_to")), None)
                old_txt, new_txt = (pf["from"], pf["to"]) if pf else ((pe["en_counterpart_text"], pe["en_to"]) if pe else (None, None))
                if old_txt is None:
                    continue
                sm = difflib.SequenceMatcher(None, old_txt, new_txt, autojunk=False)
                removed = "".join(old_txt[a1:a2] for tag, a1, a2, b1, b2_ in sm.get_opcodes() if tag in ("delete", "replace")).strip()
                hits = cells("06_EVIDENCE_OBJECTS", vid, f"summary_{lang}")
                if len(hits) != 1:
                    raise TxError(f"06 {vid} summary_{lang}: {len(hits)} cells")
                i, j = hits[0]
                cur = s.ed.get_value("06_EVIDENCE_OBJECTS", i, j)
                if removed and removed in cur:
                    new = re.sub(r"\s+", " ", cur.replace(removed, "")).strip()
                    s.set("RC-5:REVIEW:AR review 9 (optional)", "06_EVIDENCE_OBJECTS", i, j, new, cur, f"{vid}.summary_{lang}")
                    review_applied.append(f"AR review 9 {vid} {lang}")
    notes["review_fixes_applied"] = review_applied
    notes["applied"] = applied
    notes["composed"] = "Home §3 body_en (B2-006 d + B3-003 a); /people/ §1 body_en and body_ar (B2-101 d + B3-015 a)."
    notes["decided"] = "Home §3 rubric: B3-024 ('Evidence' / «الدليل», the domain pages' label) applied; B2-007 ('What the evidence shows') not applied."
    notes["ledgers"] = "audit/release_candidate/ARABIC_EDITORIAL_LEDGER.md and ENGLISH_EDITORIAL_LEDGER.md list every change with FROM, TO and reason."
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-5"), ("summary", "Part B editorial passes B2 (Arabic) and B3 (English), with B2 f, g, h"),
                                           ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}), json.dumps(applied))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
