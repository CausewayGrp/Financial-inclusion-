# -*- coding: utf-8 -*-
"""Stage 2 — false, materially misleading and leaked public statements (P2 roots), Master-first.

  python3 stage2_execute.py <in_master.xlsx> <spec.csv> <out_master.xlsx> <out_dir> <ledger.json>

Writes the staged Master plus the controlled files that change in the same commit (master_structure.json,
presentation_priority.json, page_spec_templates.json) into <out_dir>; run_stage.py installs them after its snapshot.
Stage membership: every P2 root except PB-0390 (Stage 4, source schema), PB-0401/PB-0402 (Stage 4, visual contracts),
PB-0472 (Stage 3, with the full-copy rule PB-0470), SUPERSEDED roots and PB-0390P (SOURCE_PENDING). Execution finding
EXF-001 (non-locator text in 15.primary_url) is corrected here as a leak defect.
"""
import copy, hashlib, json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from engine import Engine, RootFailure, LOC_SUBSTR, apply_presentation_edits, ROOT   # noqa: E402

STAGE = "STAGE-2"
NOT_THIS_STAGE = {"PB-0390": ("DEFERRED", "STAGE-4"), "PB-0401": ("DEFERRED", "STAGE-4"), "PB-0402": ("DEFERRED", "STAGE-4"),
                  "PB-0472": ("DEFERRED", "STAGE-3")}
VSTATE = {"OECD-YEM-001": "CONFIRMED", "OECD-YEM-002": "CONFIRMED",
          "OECD-YEM-003": "NOT_CONFIRMED__INSTRUMENT_AND_PERIOD_UNKNOWN", "OECD-YEM-004": "NOT_CONFIRMED__INSTRUMENT_AND_PERIOD_UNKNOWN",
          "OECD-YEM-005": "NOT_CONFIRMED__INSTRUMENT_AND_PERIOD_UNKNOWN", "OECD-YEM-006": "NOT_VERIFIED_AGAINST_OECD_TEXT",
          "OECD-YEM-007": "NOT_VERIFIED_AGAINST_OECD_TEXT", "OECD-YEM-008": "SUBSTANCE_CONFIRMED_BY_INDEPENDENT_SOURCES__DECISION_NUMBER_UNVERIFIED",
          "OECD-YEM-009": "SUBSTANCE_CONFIRMED_BY_INDEPENDENT_SOURCES", "OECD-YEM-010": "NOT_CONFIRMED", "OECD-YEM-011": "CONFIRMED",
          **{f"OECD-YEM-0{n}": "NOT_VERIFIED_AGAINST_OECD_TEXT" for n in range(12, 18)}}
OECD18 = OrderedDict([
    ("fact_id", "OECD-YEM-018"), ("domain", "People"), ("metric", "Yemen survey scope and attitude-score construction"), ("value", None),
    ("unit", None), ("period", "OECD/INFE 2023 (fieldwork 11 March–1 April 2023)"),
    ("english", "In the OECD/INFE 2023 survey, Yemen's data (sample of 1,000; fieldwork 11 March–1 April 2023; telephone and face-to-face) were collected "
                "in the framework of technical assistance or regional projects; the coordinated 2022/23 financial-attitude score uses the two required "
                "attitude questions, the optional third being excluded."),
    ("arabic", "في مسح OECD/INFE لعام 2023 جُمعت بيانات اليمن (عينة من 1,000 مستجيب؛ عمل ميداني من 11 مارس إلى 1 أبريل 2023؛ عبر الهاتف والمقابلة المباشرة) "
               "في إطار مساعدة فنية أو مشروعات إقليمية، ويستخدم مقياس الاتجاهات المالية في التمرين المنسق 2022/2023 سؤالي الاتجاهات الإلزاميين مع استبعاد السؤال الثالث الاختياري."),
    ("source_id", "SRC-OECD-INFE-2023"), ("url", None)])


def stage_roots(eng):
    out = []
    for root, rows in eng.spec.items():
        st = rows[0]["Claude_status"]
        if rows[0]["priority"] != "P2":
            continue
        out.append(root)
    return out


def main():
    master, spec, out_master, out_dir, ledger = sys.argv[1:6]
    os.makedirs(out_dir, exist_ok=True)
    eng = Engine(master, spec)
    wb = eng.wb
    ed = eng.ed
    extra = OrderedDict()

    def substr(root):
        return eng.apply_substr_rows(root)

    # ---------------- PB-0108: 29 verification states (+ R1–R4 ranking removal rows) ----------------
    def pb0108(root):
        S = "29_OECD_BENCHMARKS"
        g = wb.grid(S)
        if g[32][0] != "Verified Yemen facts" or g[33][:10] != ["fact_id", "domain", "metric", "value", "unit", "period", "english", "arabic", "source_id", "url"]:
            raise RootFailure("29 block 'Verified Yemen facts' not where the spec expects it")
        ed.set_cell(S, 33, 1, "Yemen values attributed to OECD sources — see verification_state", expect="Verified Yemen facts")
        ed.set_cell(S, 34, 11, "verification_state", expect=None)
        seen = []
        for i in range(35, 52):
            fid = g[i - 1][0]
            if fid not in VSTATE:
                raise RootFailure(f"29 r{i}: unexpected fact id {fid!r}")
            ed.set_cell(S, i, 11, VSTATE[fid], expect=None)
            seen.append(fid)
        if any(c not in (None, "") for c in g[51]):
            raise RootFailure("29 r52 is not blank; OECD-YEM-018 would overwrite data")
        for j, (k, v) in enumerate(OECD18.items(), 1):
            if v not in (None, ""):
                ed.set_cell(S, 52, j, v, expect=None)
        ed.set_cell(S, 52, 11, "CONFIRMED", expect=None)
        rows = [r for r in eng.spec[root] if LOC_SUBSTR.match(r["row_locator_if_needed"])]
        done = []
        for r in rows:
            m = LOC_SUBSTR.match(r["row_locator_if_needed"])
            row, n = int(m.group(1)), int(m.group(2))
            ed.replace_in_cell(r["sheet"], row, eng.col(r["sheet"], r["field"]), r["current_value"], r["proposed_value"], count=n)
            done.append(f"{r['patch_id']}: r{row} ×{n}")
        return {"block_title": "Yemen values attributed to OECD sources — see verification_state", "verification_state_rows": len(seen) + 1,
                "new_row": "r52 OECD-YEM-018 (CONFIRMED)", "ranking_clause_rows": done}

    # ---------------- PB-0109: 29 public_use (Annex D table; diagnostic synthesis block) ----------------
    def pb0109(root):
        S = "29_OECD_BENCHMARKS"
        g = wb.grid(S)
        ed.set_cell(S, 5, 13, "public_use", expect=None)
        for i in range(6, 31):
            if not g[i - 1][0]:
                raise RootFailure(f"29 r{i} blank inside Annex D table")
            ed.set_cell(S, i, 13, "NON_PUBLIC__PROVENANCE_DEFECT", expect=None)
        if g[53][0] != "OECD Yemen diagnostic 2026":
            raise RootFailure("29 diagnostic block title not at r54")
        ed.set_cell(S, 55, 7, "public_use", expect=None)
        last = max(i for i in range(56, len(g) + 1) if g[i - 1][0])
        for i in range(56, last + 1):
            ed.set_cell(S, i, 7, "NON_PUBLIC__UNVERIFIED_LEAD_MATERIAL", expect=None)
        return {"annex_d_rows": "6–30", "diagnostic_rows": f"56–{last}",
                "note": "Spec cited rows 54–62; the Master block 'OECD Yemen diagnostic 2026' runs to r66 and every row carries the same unverified recommendation text, so the whole block is marked."}

    # ---------------- PB-0110: 28 Annex A item-level block ----------------
    def pb0110(root):
        S = "28_METHODS_RIGHTS"
        g = wb.grid(S)
        if not str(g[42][0]).startswith("OECD/INFE Annex A item-level"):
            raise RootFailure("28 Annex A block title not at r43")
        ed.set_cell(S, 44, 4, "Question wording (reconstructed; not transcribed from the OECD/INFE toolkit)", expect="Verbatim Survey Question Prompt")
        ed.set_cell(S, 44, 9, "public_use", expect=None)
        last = max(i for i in range(45, len(g) + 1) if g[i - 1][0])
        for i in range(45, last + 1):
            ed.set_cell(S, i, 9, "NON_PUBLIC__RECONSTRUCTED_ITEMS", expect=None)
        return {"header": "r44 D", "public_use_rows": f"45–{last}"}

    # ---------------- PB-0216: /providers/ scope section ----------------
    def pb0216(root):
        return eng.new_section_root(root, role=("Scope", "النطاق"))

    # ---------------- PB-0217: 22 issuing authority ----------------
    def pb0217(root):
        S = "22_PROVIDERS_DATA"
        g = wb.grid(S)
        h = g[3]
        if h[14] != "notes" or len(h) > 15 and h[15] not in (None, ""):
            raise RootFailure("22 main header layout differs from the spec basis")
        ed.set_cell(S, 4, 16, "issuing_authority", expect=None)
        si = h.index("source_id")
        vals = {}
        for i in range(5, 63):
            r = g[i - 1]
            if not r[0]:
                continue
            sid = str(r[si] or "")
            v = "CBY_ADEN" if sid.startswith("SRC-CBY-") else ("NONE__NON_REGULATORY_SOURCE" if sid.startswith("SRC-YMN-") else "UNKNOWN")
            ed.set_cell(S, i, 16, v, expect=None)
            vals[v] = vals.get(v, 0) + 1
        ts = sorted({str(g[i - 1][h.index("territorial_scope")]) for i in range(5, 63) if g[i - 1][0]})
        return {"issuing_authority_counts": vals, "territorial_scope_existing_values": ts,
                "note": "territorial_scope already exists in the Master and holds source-stated scope (no national default found), so it is kept; no public provider-record surface exists in the current build — the render requirement is carried to the status-event table (PB-0525, Stage 3) and the Design contract."}

    # ---------------- PB-0516: 04 build-grammar requirement for /measurement/ ----------------
    def pb0516(root):
        S = "04_NAV_UX"
        g = wb.grid(S)
        last = max(i for i in range(49, len(g) + 1) if g[i - 1][0] and i < 74)
        if g[last][0] not in (None, "") or g[last + 1][0] != "Governed interface copy":
            raise RootFailure("04 Build grammar block does not end where expected")
        ed.insert_rows(S, last + 1, [{1: "/measurement/", 2: "measurement list display",
                                      3: "The ten measurement items render as filterable or expandable items, not as one long paragraph; each exposes current evidence anchor, missing evidence, decision unlocked, proposed method, feasibility, sensitivity or data-responsibility constraints, priority basis and what would change."}])
        return {"inserted_row": last + 1, "block": "Build grammar"}

    # ---------------- PB-0220 / PB-0221: removals archived to audit lineage ----------------
    arch_dir = os.path.join(out_dir, "archive")
    os.makedirs(arch_dir, exist_ok=True)

    def pb0220(root):
        S = "25_FINDEX_BASELINE"
        g = wb.grid(S)
        if not str(g[13][0]).startswith("Attached analytical inputs"):
            raise RootFailure("25 r14 is not the attached analytical-inputs block")
        last = max(i for i in range(14, len(g) + 1) if any(c not in (None, "") for c in g[i - 1]))
        if last != 35:
            raise RootFailure(f"25 block ends at r{last}, spec says r35")
        arch = {"root": root, "disposition": "NOT_ADMITTED__CONTRADICTS_GOVERNED_FINDEX", "sheet": S, "excel_rows": "14–35",
                "source_master_sha256": hashlib.sha256(open(master, "rb").read()).hexdigest(), "rows": g[13:35]}
        json.dump(arch, open(os.path.join(arch_dir, "PB-0220_25_FINDEX_BASELINE_rows_14-35.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        ed.delete_rows(S, 12, 35)
        return {"deleted_rows": "12–35 (blank separator rows 12–13 and block rows 14–35)", "archive": "audit/tranche_b_execution/archive/PB-0220_25_FINDEX_BASELINE_rows_14-35.json"}

    def pb0221(root):
        S = "30_FCS_CONTEXT"
        g = wb.grid(S)
        arch = {"root": root, "disposition": "NOT_ADMITTED__UNSOURCED_COMPARATOR", "sheet": S,
                "source_master_sha256": hashlib.sha256(open(master, "rb").read()).hexdigest(), "rows": g}
        json.dump(arch, open(os.path.join(arch_dir, "PB-0221_30_FCS_CONTEXT_whole_sheet.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        ed.remove_sheet(S)
        app = ed.parts.get("docProps/app.xml")
        note = "docProps/app.xml absent"
        if app is not None:
            t = app.decode("utf-8")
            if "30_FCS_CONTEXT" in t:
                note = "docProps/app.xml lists sheet titles; left unchanged (metadata only, not read by any consumer)"
        return {"removed_sheet": S, "rows_archived": len(g), "archive": "audit/tranche_b_execution/archive/PB-0221_30_FCS_CONTEXT_whole_sheet.json", "app_xml": note}

    # ---------------- PB-0411: 02 governed meta description columns ----------------
    def pb0411(root):
        S = "02_SITE_MAP"
        g = wb.grid(S)
        if g[3][:8] != ["route", "page_class", "template_route", "instance_id", "title_en", "title_ar", "full_copy_en", "full_copy_ar"] or (len(g[3]) > 8 and g[3][8]):
            raise RootFailure("02 header differs from the spec basis")
        ed.set_cell(S, 4, 9, "meta_description_en", expect=None)
        ed.set_cell(S, 4, 10, "meta_description_ar", expect=None)
        return {"columns": ["meta_description_en", "meta_description_ar"], "values": "empty = generation default (title + first sentence of the first rendered section, ≤155 characters, per language)"}

    # ---------------- code/controlled-input roots (applied in the same commit) ----------------
    def code_root(what):
        return lambda root: {"change": what}

    # ---------------- PB-0302 / PB-0303: the visual record that the section embeds carries the education level too ----------------
    # Execution completion (Lead): the section states 6.98% (25_FINDEX_BASELINE WB-FINDEX-OBS-2022-006, within the bound
    # lineage of VIS-FINDEX-GAPS, source SRC-WB-FINDEX-AGG-2022). The embedded visual summary is extended with the same
    # level so that the public number is carried by the governed, source-bound record the page shows.
    COMPLETE = {"PB-0302": ("accessible_summary_en", "differ by about 9.0 percentage points.",
                            "differ by about 9.0 percentage points. Among adults with primary education or less, 6.98% have an account; the matching figure for adults with more education is not in the evidence base."),
                "PB-0303": ("accessible_summary_ar", "نحو 9.0 نقاط مئوية.",
                            "نحو 9.0 نقاط مئوية. وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، ولا تتضمن قاعدة الأدلة الرقم المقابل لمن تلقوا تعليمًا أعلى.")}

    def findex_levels(root):
        done = eng.apply_substr_rows(root)
        f, old, new = COMPLETE[root]
        S = "11_VISUAL_LIBRARY"
        row = next(i for i, r in enumerate(wb.grid(S), 1) if r and r[0] == "VIS-FINDEX-GAPS")
        ed.replace_in_cell(S, row, eng.col(S, f), old, new, count=1)
        return done + [f"execution completion: {S}!r{row}.{f} adds the education level (WB-FINDEX-OBS-2022-006)"]

    def findex_completion(root):
        out = []
        for base in ("PB-0302", "PB-0303"):
            if eng.results.get(base, {}).get("disposition") != "APPLIED":
                raise RootFailure(f"{base} not applied; completion not needed")
            f, old, new = COMPLETE[base]
            S = "11_VISUAL_LIBRARY"
            row = next(i for i, r in enumerate(wb.grid(S), 1) if r and r[0] == "VIS-FINDEX-GAPS")
            ed.replace_in_cell(S, row, eng.col(S, f), old, new, count=1)
            out.append(f"{base}: {S}!r{row}.{f} carries the education level (WB-FINDEX-OBS-2022-006)")
        return out

    handlers = {"PB-0108": pb0108, "PB-0109": pb0109, "PB-0110": pb0110, "PB-0216": pb0216, "PB-0217": pb0217,
                "PB-0411": pb0411, "PB-0516": pb0516,
                "PB-0400": code_root("scripts/projection/controlled_inputs/page_spec_templates.json: accessibility flags PENDING_DESIGN_IMPLEMENTATION + text_alternative_table_contract"),
                "PB-0410": code_root("scripts/build.py: meta description = governed/derived page description, never a *_internal field")}
    late = {"PB-0220": pb0220, "PB-0221": pb0221}
    order = []
    for root in stage_roots(eng):
        st = eng.spec[root][0]["Claude_status"]
        if "SUPERSEDED" in st:
            eng.hold(root, "SUPERSEDED", STAGE, "Superseded by recipient acceptance correction (" + ("A" if "CORRECTION_A" in st else "G") + ").")
        elif "SOURCE_PENDING" in st:
            eng.hold(root, "SOURCE_PENDING", STAGE, "Publisher/issuer values populate only when confirmed from the source itself or authoritative metadata; SOURCE_PUBLISHER_PROPOSALS.csv is a resolution aid, not metadata.")
        elif root in NOT_THIS_STAGE:
            continue
        elif root in ("PB-0160", "PB-0161"):
            eng.hold(root, "HELD", STAGE, "Literal-closure gate: the added magnitude (18_CBY_MONETARY OBS-CBY-00381, BANK_CREDIT_PRIVATE_SECTOR_BN_YER 2026-05 = 1350.4, "
                     "SRC-CBY-001) is verified in the Master, but no Evidence Record bound to /finance/ carries it or binds SRC-CBY-001, so a reader could not trace "
                     "the public number to a record. Adding an Evidence Record would add a public route (route baseline 284 is fixed for this tranche). "
                     "Held for a record-level binding of the CBY monetary series (unresolved queue).")
        elif root in late:
            continue
        else:
            order.append(root)
    for root in order:
        eng.run_root(root, handlers.get(root, substr), STAGE)
    # EXF-001 — execution finding: non-locator text held in 15.primary_url
    def exf001(root):
        S = "15_SOURCE_LIBRARY"
        g = wb.grid(S)
        h = g[3]
        pu = h.index("primary_url") + 1
        ncol = len(h) + 1
        if h[-1] in (None, ""):
            raise RootFailure("15 header has a trailing blank column")
        ed.set_cell(S, 4, ncol, "non_public_locator_note", expect=None)
        moved = []
        for i in range(5, len(g) + 1):
            v = g[i - 1][pu - 1]
            if isinstance(v, str) and v.strip() and not v.strip().lower().startswith(("http://", "https://")):
                ed.set_cell(S, i, ncol, v, expect=None)
                ed.set_cell(S, i, pu, None, expect=v)
                moved.append(g[i - 1][0])
        return {"moved_to_non_public_locator_note": moved}
    eng.run_root("EXF-001", exf001, STAGE)
    eng.run_root("EXC-0302", findex_completion, STAGE)          # after PB-0304…PB-0308 have rewritten the embedded summary
    for root in ("PB-0220", "PB-0221"):
        eng.run_root(root, late[root], STAGE)
    data = ed.save(out_master)
    # ---------------- controlled files changed in the same commit ----------------
    ms = json.load(open(os.path.join(ROOT, "scripts/projection/master_structure.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    sh = ms["sheets"]
    if eng.results.get("PB-0108", {}).get("disposition") == "APPLIED":
        for b in sh["29_OECD_BENCHMARKS"]["blocks"]:
            if b["title"] == "Verified Yemen facts":
                b["title"] = "Yemen values attributed to OECD sources — see verification_state"
    if eng.results.get("PB-0109", {}).get("disposition") == "APPLIED":
        sh["29_OECD_BENCHMARKS"]["main_labels"].append("public_use")
    if eng.results.get("PB-0217", {}).get("disposition") == "APPLIED":
        sh["22_PROVIDERS_DATA"]["main_labels"].append("issuing_authority")
    if eng.results.get("PB-0411", {}).get("disposition") == "APPLIED":
        sh["02_SITE_MAP"]["main_labels"] += ["meta_description_en", "meta_description_ar"]
    if eng.results.get("EXF-001", {}).get("disposition") == "APPLIED":
        sh["15_SOURCE_LIBRARY"]["main_labels"].append("non_public_locator_note")
    if eng.results.get("PB-0220", {}).get("disposition") == "APPLIED":
        t = "Attached analytical inputs — not verified public Findex aggregates"
        sh["25_FINDEX_BASELINE"]["blocks"] = [b for b in sh["25_FINDEX_BASELINE"]["blocks"] if b["title"] != t]
        sh["25_FINDEX_BASELINE"]["numeric_text_columns"].pop(t, None)
        sh["25_FINDEX_BASELINE"]["main_labels"] = [x for x in sh["25_FINDEX_BASELINE"]["main_labels"] if x != "col11"]   # sheet width shrinks with the block
    if eng.results.get("PB-0221", {}).get("disposition") == "APPLIED":
        sh.pop("30_FCS_CONTEXT")
    json.dump(ms, open(os.path.join(out_dir, "master_structure.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(out_dir, "master_structure.json"), "a").write("\n")
    pp = json.load(open(os.path.join(ROOT, "site-src/content/presentation_priority.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    pp, plog = apply_presentation_edits(pp, eng.section_shifts, eng.presentation_edits)
    trailing = open(os.path.join(ROOT, "site-src/content/presentation_priority.json"), encoding="utf-8").read().endswith("\n")
    with open(os.path.join(out_dir, "presentation_priority.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(pp, ensure_ascii=False, indent=2) + ("\n" if trailing else ""))
    tm = json.load(open(os.path.join(ROOT, "scripts/projection/controlled_inputs/page_spec_templates.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    if eng.results.get("PB-0400", {}).get("disposition") == "APPLIED":
        a = tm["accessibility_requirements"]
        a["visuals_must_expose_accessible_summary"] = "PENDING_DESIGN_IMPLEMENTATION"
        a["tables_or_text_alternative_for_quantitative_visuals"] = "PENDING_DESIGN_IMPLEMENTATION"
        a["text_alternative_table_contract"] = OrderedDict([
            ("applies_to", "any record or visual carrying three or more quantities"),
            ("required_independently_of_design", True),
            ("caption", "states what is measured, for whom and when"),
            ("headers", "scoped column and row headers"),
            ("columns", ["unit", "population or base", "period"]),
            ("source_line", "names the bound source record(s)")])
    json.dump(tm, open(os.path.join(out_dir, "page_spec_templates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(out_dir, "page_spec_templates.json"), "a").write("\n")
    rep = OrderedDict([("stage", STAGE), ("input_master_sha256", hashlib.sha256(open(master, "rb").read()).hexdigest()),
                       ("output_master_sha256", hashlib.sha256(data).hexdigest()), ("cells_and_ops", len(ed.log)),
                       ("presentation_changes", plog), ("results", eng.results)])
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    import collections
    print(collections.Counter(v["disposition"] for v in eng.results.values()))
    for k, v in eng.results.items():
        if v["disposition"] not in ("APPLIED",):
            print(k, v["disposition"], str(v["detail"])[:300])
    print("presentation:", plog)
    print(rep["output_master_sha256"])


if __name__ == "__main__":
    main()
