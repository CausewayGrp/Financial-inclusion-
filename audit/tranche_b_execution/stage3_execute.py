# -*- coding: utf-8 -*-
"""Stage 3 — domain, Reading, Measurement, methodology, coverage and parity roots (P3/P4, plus the P5 roots that
belong to those families), Master-first.

  python3 stage3_execute.py <in_master.xlsx> <spec.csv> <out_master.xlsx> <out_dir> <ledger.json>

Rows of the spec that patch 02_SITE_MAP.full_copy_* are not executed from Stage 3 on: EXF-002 (execution finding)
makes full_copy a derived Master field (title + rendered 03 sections, in section order), rewritten at the end of every
stage from the post-patch sections and enforced by the generator. Each skipped row is listed in its root's detail.
"""
import hashlib, json, os, re, sys
from collections import OrderedDict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from engine import Engine, RootFailure, LOC_SUBSTR, apply_presentation_edits, ROOT   # noqa: E402

STAGE = "STAGE-3"
S4_LEADS = {"LEAD-M09", "SEARCH-R", "TRUST-F01", "TRUST-F02", "TRUST-F05", "VISUAL-VOICE", "LEAD-M05"}
S5_LEADS = {"ENGLISH-VOICE", "ARABIC-CALQUE", "ENGLISH-SELFREF", "ARABIC-SELFREF"}


def leads():
    sys.path.insert(0, os.path.join(ROOT, "audit", "tranche_b_patch_tooling"))
    from pdefs_p1 import P1
    from pdefs_p2 import P2
    from pdefs_p3 import P3, P3_SEARCH
    from pdefs_p4 import P4
    return {d["pid"]: d["lead"] for d in P1 + P2 + P3 + P4 + P3_SEARCH}


def derive_full_copy(g, route, lang, title):
    """title + (heading, body) of every 03 section of the route in section order, joined by blank lines."""
    rows = [r for r in g[4:] if r and r[0] == route]
    rows.sort(key=lambda r: int(float(r[1])) if r[1] not in (None, "") else 0)
    parts = [title]
    hi, bi = (3, 4) if lang == "en" else (5, 6)
    for r in rows:
        for v in (r[hi], r[bi]):
            if v not in (None, ""):
                parts.append(v)
    return "\n\n".join(parts)


def regenerate_full_copy(eng, stage):
    """EXF-002: rewrite 02 full_copy_* from the post-patch 03 sections (exact-value checked against the current cell)."""
    S = "02_SITE_MAP"
    g = eng.ed_grid(S)
    g03 = eng.ed_grid("03_PAGE_SECTIONS")
    changed = []
    for i, r in enumerate(g[4:], start=5):
        if not r or not r[0]:
            continue
        for lang, col, tcol in (("en", 7, 5), ("ar", 8, 6)):
            new = derive_full_copy(g03, r[0], lang, r[tcol - 1])
            cur = r[col - 1]
            if cur != new:
                eng.ed.set_cell(S, i, col, new, expect=cur)
                changed.append(f"{r[0]} {lang}")
    return changed


def main():
    master, spec, out_master, out_dir, ledger = sys.argv[1:6]
    os.makedirs(out_dir, exist_ok=True)
    eng = Engine(master, spec)
    wb, ed = eng.wb, eng.ed
    LEAD = leads()
    done = json.load(open(os.path.join(HERE, "ROOT_DISPOSITIONS.json"), encoding="utf-8"))

    from projection.master_reader import Workbook
    import tempfile

    def ed_grid(sheet):
        """Current (in-editor) grid of a sheet: the editor state is saved to a temporary file and read back."""
        tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=out_dir)
        tmp.close()
        ed.save(tmp.name)
        try:
            return Workbook(tmp.name).grid(sheet)
        finally:
            os.remove(tmp.name)
    eng.ed_grid = ed_grid

    def substr(root):
        out, skipped = [], []
        rows = eng.spec[root]
        keep = [r for r in rows if not (r["sheet"] == "02_SITE_MAP" and r["field"].startswith("full_copy"))]
        skipped = [r["patch_id"] for r in rows if r not in keep]
        eng.spec[root] = keep
        try:
            if keep:
                out = eng.apply_substr_rows(root)
        finally:
            eng.spec[root] = rows
        if skipped:
            out.append("full_copy rows superseded by EXF-002 derivation: " + ", ".join(skipped))
        return out

    def cell(root):
        out = []
        for r in eng.spec[root]:
            m = re.match(r"([A-Z]+-\d+) \(r(\d+)\)", r["stable_object_id"])
            if not m:
                raise RootFailure(f"{r['patch_id']}: no row locator in {r['stable_object_id']!r}")
            row = int(m.group(2))
            if wb.grid(r["sheet"])[row - 1][0] != m.group(1):
                raise RootFailure(f"{r['patch_id']}: {r['sheet']} r{row} is not {m.group(1)}")
            ed.set_cell(r["sheet"], row, eng.col(r["sheet"], r["field"]), r["proposed_value"], expect=r["current_value"])
            out.append(f"{r['patch_id']}: {r['sheet']}!r{row}.{r['field']}")
        return out

    def pb0615(root):
        r = eng.spec[root][0]
        ed.set_cell("17_INDICATOR_LIBRARY", 2, 1, r["proposed_value"], expect=r["current_value"])
        return ["17_INDICATOR_LIBRARY!A2 sheet description"]

    def generator_rule(evidence):
        return lambda root: {"implemented_in": evidence}

    def section(root, role=None):
        return lambda r_: eng.new_section_root(r_, role=role)

    def pb0426(root):
        S = "08_READINGS"
        g = wb.grid(S)
        h = g[3]
        if h[-1] != "verification_bindings":
            raise RootFailure("08 header differs from the spec basis")
        c1, c2 = len(h) + 1, len(h) + 2
        ed.set_cell(S, 4, c1, "domain_surface_routes", expect=None)
        ed.set_cell(S, 4, c2, "domain_context_routes", expect=None)
        rows = {r[0]: i for i, r in enumerate(g, 1) if i > 4 and r and r[0]}
        per_route = Counter()
        out = []
        for r in eng.spec[root]:
            if r["patch_id"] == root:
                continue
            m = re.match(r"domain_surface_routes = (.*?) \|\| domain_context_routes = (.*)$", r["proposed_value"])
            if not m:
                raise RootFailure(f"{r['patch_id']}: unparseable value")
            surf, ctx = [None if x.strip() == "(none)" else x.strip() for x in m.groups()]
            i = rows[r["stable_object_id"]]
            if surf:
                ed.set_cell(S, i, c1, surf, expect=None)
                for x in surf.split(";"):
                    per_route[x.strip()] += 1
            if ctx:
                ed.set_cell(S, i, c2, ctx, expect=None)
            out.append(f"{r['stable_object_id']}: surface={surf or '—'} context={ctx or '—'}")
        over = {k: v for k, v in per_route.items() if v > 2}
        if over:
            raise RootFailure(f"more than two surfaced Readings on {over}")
        return out

    def pb0518(root):
        S = "15_SOURCE_LIBRARY"
        g = wb.grid(S)
        if any(r and r[0] == "SRC-CBY-ENF-18-2026" for r in g):
            raise RootFailure("SRC-CBY-ENF-18-2026 already present")
        h = g[3]
        row = eng.next_free_row(S)
        vals = {"source_id": "SRC-CBY-ENF-18-2026", "primary_url": "https://cby-ye.com/news/975", "datasets_or_use": "DS-PROVIDER-STATUS-EVENTS",
                "row_count": 1, "public_card_state": "LOCATOR_ONLY"}
        for k, v in vals.items():
            ed.set_cell(S, row, h.index(k) + 1, v, expect=None)
        return {"row": row, "values": vals,
                "note": "Locator verified by the Claude team at cby-ye.com/news/975 (dated 2026-09-24; page text names no entity; names only in the scanned PDF). "
                        "Display fields and publisher stay empty on a LOCATOR_ONLY card (acceptance correction F; PB-0390P governs publisher population). "
                        "Retrieval date is recorded with the PB-0390 columns in Stage 4."}

    def pb0519(root):
        S = "22_PROVIDERS_DATA"
        g = wb.grid(S)
        from projection.structure import blocks
        b = next(x for x in blocks(g, S) if x["title"] == "Provider status events")
        labels = g[b["header_row"] - 1]
        last = max(i for i in range(b["first"], b["last"] + 1) if g[i - 1] and g[i - 1][0])
        if g[last - 1][0] != "PSE-014":
            raise RootFailure(f"last status event is {g[last - 1][0]!r}, expected PSE-014")
        vals = OrderedDict([
            ("status_event_id", "PSE-015"), ("event_date", "2026-09-24"), ("source_id", "SRC-CBY-ENF-18-2026"), ("authority", "Central Bank of Yemen — Aden"),
            ("event_scope", "one exchange company, exchange establishments and one remittance agent, as announced"),
            ("affected_class", "EXCHANGE_COMPANY_ESTABLISHMENTS_AND_REMITTANCE_AGENT"), ("event_state", "LICENCE_SUSPENSION_AND_CLOSURE_EVENT"),
            ("normalized_event", "Governor Decision No. 18 of 2026 suspends licences of an exchange company, exchange establishments and a remittance agent and closes their premises"),
            ("entity_subject_state", "NAMES_PRIMARY_SOURCE_PENDING"), ("public_use", "PUBLIC_EVENT__NAMES_WITHHELD_UNTIL_TRANSCRIBED"),
            ("not_proven", "a licence suspension or closure is a dated regulatory action and does not establish permanent cessation; it says nothing about the current operation of other entities and does not change the 2026 roster count"),
            ("source_url", "https://cby-ye.com/news/975")])
        ed.insert_rows(S, last + 1, [{labels.index(k) + 1: v for k, v in vals.items()}])
        return {"inserted_row": last + 1, "event": "PSE-015", "note": "Rows of 22 at and below r%d move down by one; no later spec row targets them." % (last + 1)}

    def holdfn(reason):
        return reason

    LIT = ("Literal-closure rule: the new section states verified Master values ({vals}), but no source-closed record bound to {route} carries them, so a reader could not trace these public numbers to an Evidence Record on the page. Making them traceable needs either new Evidence Records (new public routes; the route baseline 284 is fixed for this tranche) or a governed extension of existing records and their route bindings (an IA change outside this spec). Carried to the unresolved queue with the exact text ready.")
    HOLDS = {
        "PB-0322": ("HELD", "A new public claim CLM-061 would add the public route /evidence/CLM-061/; the route baseline (284) is fixed for this tranche. The income-group gap is published on /people/ (PB-0302/0303) and in MA-003 (PB-0320/0321) with its governed sources; the standalone claim is carried to the unresolved queue."),
        "PB-0374": ("HELD", "Splitting 06 limitations_* into measurement_limitation_* and prohibited_inference_* for 108 records (216 cells) is a per-record editorial adjudication in two languages; a mechanical sentence split would move meaning. Carried to the unresolved queue with its rule."),
        "PB-0470": ("HELD", "The rule has three parts. Two are implemented through EXF-002 (03 is the canonical rendered page copy; 02.full_copy_* is derived from title + rendered sections and enforced by the generator). The third — generating reading-page sections from 09_READING_SECTIONS — would replace the rendered copy of all ten Reading pages: the 03 and 09 bodies differ in every section (0 of 80 identical), so the switch needs a bilingual editorial adjudication. The root is therefore held as a whole; the switch is carried to the unresolved queue."),
        "PB-0471": ("HELD", "Generating embedded object blocks from the owning objects at build time requires removing embedded copies from 03 section cells across the product; this tranche keeps the spec's explicit per-cell patches of every embedding cell (consistency verified by the literal and parity gates). Carried to R8.5 with PB-0470."),
        "PB-0345": ("HELD", LIT.format(vals="11.9%, 1,062,441 active bank accounts, 375,252 active e-wallet accounts", route="/evidence/compare/")),
        "PB-0520": ("HELD", LIT.format(vals="20_FIRM_FINANCE 2022 survey: 58.2% (191 of 328), working-capital shares 69.12/16.66/10.15/0.56%, intermediaries 73.48/24.39%, informal 80.18% of 217", route="/firms/")),
        "PB-0521": ("HELD", LIT.format(vals="19_PAYMENTS_DATA e-wallet subscribers 414,631 / 507,585 / 581,075 (2024 Q1–Q3) and 2,102,484 (H1 2025)", route="/payments/")),
        "PB-0522": ("HELD", LIT.format(vals="2026 roster counts 98 / 225 / 106, 26 listed banks, FMIIP 817 access points vs 1,021 target", route="/access/")),
        "PB-0614": ("HELD", LIT.format(vals="the illustrative 15.5% / 6.5% / 9.0-point example", route="/methodology/")),
        "PB-0525": ("HELD", "The 22 'Provider status events' block holds English-only event descriptions and non-proof notes; a public status-event table on the bilingual /providers/ page needs governed Arabic event text and Arabic entity names taken from the source instruments. Carried to the unresolved queue; the Master rows (PSE-001…PSE-015) are ready for it."),
    }
    handlers = {
        "PB-0320": cell, "PB-0321": cell, "PB-0325": cell, "PB-0615": pb0615, "PB-0426": pb0426,
        "PB-0342": generator_rule("scripts/projection/structure.py blocks()/keyed_records(block=title) and master_structure.json declare and read 31 'FMIIP results framework' by its own title/header; no value change."),
        "PB-0473": generator_rule("scripts/projection/master_structure.json declares every titled block (43 at entry, incl. the unseparated 31 'OECD policy' block); families.validate_structure fails on any undeclared or missing block; tests in scripts/projection/tests."),
        "PB-0517": generator_rule("22 'Provider status events' is read by title/header (structure.keyed_records(block=...)); PSE-015 appended by PB-0519."),
        "PB-0523": generator_rule("scripts/projection/derived.py page_specs: prohibited_inferences de-duplicated per language across claims, visuals and Readings of the page."),
        "PB-0345": section(None), "PB-0520": section(None), "PB-0521": section(None), "PB-0522": section(None), "PB-0524": section(None),
        "PB-0611": section(None), "PB-0612": section(None), "PB-0613": section(None), "PB-0614": section(None),
        "PB-0518": pb0518, "PB-0519": pb0519,
    }
    order = []
    for root, rows in eng.spec.items():
        if root in done and done[root]["disposition"] not in ("PENDING",):
            continue
        pri = rows[0]["priority"]
        lead = LEAD.get(root, "?")
        if root in ("PB-0413", "PB-0414", "PB-0415") or lead in S5_LEADS:
            continue
        if lead in S4_LEADS or root in ("PB-0412", "PB-0390", "PB-0401", "PB-0402"):
            continue
        if pri in ("P1", "P2") and root not in ("PB-0472",):
            continue
        order.append(root)
    for root in order:
        if root in HOLDS:
            eng.hold(root, HOLDS[root][0], STAGE, HOLDS[root][1])
        elif root == "PB-0472":
            eng.hold(root, "SUPERSEDED", STAGE, "Its target cells (02 r139 full_copy_en/ar of /readings/microfinance-structural-divergence/) are regenerated by EXF-002 from the rendered, post-patch 03 sections, which carry the corrected PB-0120…PB-0147 wording; generating them from 09 would make full_copy differ from the rendered page.")
        else:
            eng.run_root(root, handlers.get(root, substr), STAGE)
    eng.run_root("EXF-002", lambda r: regenerate_full_copy(eng, STAGE), STAGE)
    data = ed.save(out_master)
    # controlled files changed in the same commit
    ms = json.load(open(os.path.join(ROOT, "scripts/projection/master_structure.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    if eng.results.get("PB-0426", {}).get("disposition") == "APPLIED":
        ms["sheets"]["08_READINGS"]["main_labels"] += ["domain_surface_routes", "domain_context_routes"]
    json.dump(ms, open(os.path.join(out_dir, "master_structure.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(out_dir, "master_structure.json"), "a").write("\n")
    pp = json.load(open(os.path.join(ROOT, "site-src/content/presentation_priority.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    pp, plog = apply_presentation_edits(pp, eng.section_shifts, eng.presentation_edits)
    with open(os.path.join(out_dir, "presentation_priority.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(pp, ensure_ascii=False, indent=2) + "\n")
    rep = OrderedDict([("stage", STAGE), ("input_master_sha256", hashlib.sha256(open(master, "rb").read()).hexdigest()),
                       ("output_master_sha256", hashlib.sha256(data).hexdigest()), ("cells_and_ops", len(ed.log)),
                       ("presentation_changes", plog), ("results", eng.results)])
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(Counter(v["disposition"] for v in eng.results.values()))
    for k, v in eng.results.items():
        if v["disposition"] != "APPLIED":
            print(k, v["disposition"], str(v["detail"])[:220])
    print("presentation:", plog)
    print(rep["output_master_sha256"])


if __name__ == "__main__":
    main()
