# -*- coding: utf-8 -*-
"""Regression tests for the canonical Master -> projection generator.

  python3 -m unittest discover -s scripts/projection/tests -v        (from the repository root)

The tests read the bound Production Master (authority/) and the committed projections (site-src/content/).
"""
import hashlib
import json
import os
import re
import sys
import tempfile
import unittest
import zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from projection.master_reader import Workbook                       # noqa: E402
from projection.structure import blocks, keyed_records              # noqa: E402
from projection import families as F                                # noqa: E402
from projection.generator import Context, build_all, serialize, generate   # noqa: E402
from projection.master_writer import MasterEditor                   # noqa: E402

MASTER = os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx")
CONTENT = os.path.join(ROOT, "site-src", "content")


class MasterStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wb = Workbook(MASTER)
        with open(os.path.join(ROOT, "scripts", "projection", "master_structure.json"), encoding="utf-8") as fh:
            cls.contract = json.load(fh)

    def test_contract_matches_master(self):
        F.validate_structure(self.wb, self.contract)          # raises on any undeclared/missing block or header change

    def test_block_inventory(self):
        """PB-0473: every titled block is read by its own title and header, never by the sheet's first header."""
        declared = sum(len(s["blocks"]) for s in self.contract["sheets"].values())
        found = 0
        for name, spec in self.contract["sheets"].items():
            titles = [b["title"] for b in blocks(self.wb.grid(name), name)[1:]] + list(spec.get("unseparated_block_titles", []))
            self.assertEqual(sorted(titles), sorted(b["title"] for b in spec["blocks"]), name)
            found += len(spec["blocks"])
        self.assertEqual(found, declared)
        recs = keyed_records(self.wb.grid("22_PROVIDERS_DATA"), "22_PROVIDERS_DATA", block="Provider status events")
        self.assertTrue(all(r["status_event_id"].startswith("PSE-") for _, r in recs))
        self.assertIn("PSE-015", [r["status_event_id"] for _, r in recs])

    def test_reader_types(self):
        g = self.wb.grid("25_FINDEX_BASELINE")
        self.assertEqual(g[4][0], "WB-FINDEX-OBS-2022-001")
        self.assertEqual(g[4][5], 11.9)


class Generation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = Context(MASTER, ROOT)
        build_all(cls.ctx)

    def test_committed_projections_are_generated(self):
        rep = generate(MASTER, ROOT, check=True)
        self.assertEqual(rep["differences"], [], "committed projections differ from the Master (run scripts/generate_projections.py)")

    def test_deterministic(self):
        ctx2 = Context(MASTER, ROOT)
        build_all(ctx2)
        for e in self.ctx.manifest["outputs"]:
            a = serialize(self.ctx.out[e["path"]], e.get("trailing_newline", True))
            b = serialize(ctx2.out[e["path"]], e.get("trailing_newline", True))
            self.assertEqual(hashlib.sha256(a.encode()).hexdigest(), hashlib.sha256(b.encode()).hexdigest(), e["path"])

    def test_manifest_covers_content(self):
        paths = {o["path"] for o in self.ctx.manifest["outputs"]}
        files = set()
        for dp, _, fn in os.walk(CONTENT):
            for f in fn:
                files.add(os.path.relpath(os.path.join(dp, f), CONTENT).replace(os.sep, "/"))
        self.assertEqual(files, paths, "every file under site-src/content is declared in the projection manifest")
        kinds = {o["kind"] for o in self.ctx.manifest["outputs"]}
        self.assertLessEqual(kinds, {"GENERATED", "DERIVED", "CONTROLLED_CONTRACT"})

    def test_lineage_truth(self):
        """Stage 1 closure rule v2: only bound sources resolve; dataset tokens never expand; states agree with tokens."""
        lib = {r["source_id"] for r in self.ctx.out["sources/source_library.json"]}
        states = {"BOUND_EXACT", "BOUND_PARTIAL", "COMPOSITE_OF_OBJECTS", "SOURCE_NOT_YET_BOUND", "FRAMING_NO_FACT"}
        for c in self.ctx.out["sources/public_object_source_closure.json"]:
            if c["object_type"] != "evidence_object":
                continue
            self.assertIn(c["lineage_state"], states, c["object_id"])
            for s in c["resolved_source_ids"]:
                self.assertIn(s, c["dependency_ids"], f"{c['object_id']}: {s} resolved without being declared")
                self.assertIn(s, lib)
            if c["closure_state"] == "CLOSED_TO_SOURCE_ID":
                self.assertEqual(c["unresolved_dependency_ids"], [], c["object_id"])
            if c["lineage_state"] in ("COMPOSITE_OF_OBJECTS", "SOURCE_NOT_YET_BOUND", "FRAMING_NO_FACT"):
                self.assertEqual(c["resolved_source_ids"], [], c["object_id"])

    def test_evidence_detail_sources_are_bound(self):
        clo = {(c["object_type"], c["object_id"]): c for c in self.ctx.out["sources/public_object_source_closure.json"]}
        for s in self.ctx.out["page_specs.json"]["page_specs"]:
            if s["page_class"] != "evidence_detail":
                continue
            bound = set(clo[("evidence_object", s["instance_id"])]["resolved_source_ids"])
            self.assertLessEqual({r["source_id"] for r in s["source_references"]}, bound, s["route"])

    def test_public_locator_rule(self):
        for r in self.ctx.out["content/search_index.json"]:
            if r["type"] in ("source", "source_locator"):
                src = next(x for x in self.ctx.out["sources/source_reference_map.json"] if x["source_id"] == r["id"])
                self.assertTrue(str(src["primary_url"]).startswith(("http://", "https://")), r["id"])

    def test_navigation_contract(self):
        nav = self.ctx.out["content/navigation_interaction.json"]
        routes = set()
        for item in nav["global_navigation"]:
            if item.get("route"):
                routes.add(item["route"])
            kids = item.get("children") or []
            if not item.get("route"):
                self.assertGreaterEqual(len(kids), 2)
            routes |= {k["route"] for k in kids}
        self.assertEqual(routes, {"/explore/", "/evidence/", "/readings/", "/data/", "/methodology/", "/measurement/"})
        self.assertEqual(nav["trust_navigation"][0]["route"], "/about/")

    def test_full_copy_is_derived(self):
        secs = {}
        for s in self.ctx.out["content/page_sections.json"]:
            secs.setdefault(s["route"], []).append(s)
        for r in self.ctx.out["content/site_map.json"]:
            ordered = sorted(secs.get(r["route"], []), key=lambda s: s["section_order"])
            for L in ("en", "ar"):
                want = "\n\n".join([r["title_" + L]] + [v for s in ordered for v in (s.get("heading_" + L), s.get("body_" + L)) if v])
                self.assertEqual(r["full_copy_" + L], want, f"{r['route']} {L}")


    def test_public_inventory_contract(self):
        """P1.2: every inventory count is derived from its projection by the declared rule."""
        inv = {c["key"]: c["value"] for c in self.ctx.out["content/public_inventory.json"]["counts"]}
        o = self.ctx.out
        self.assertEqual(inv["evidence_records"], len(o["evidence/evidence_objects.json"]))
        self.assertEqual(inv["public_claims"], len(o["evidence/public_claims.json"]))
        # RC-2: "Dated events in the system chronology" — the analytical rule row (event_class SYSTEM_INTERPRETATION) is not an event
        self.assertEqual(inv["chronology_events"], sum(1 for r in o["visuals/system_chronology.json"] if r.get("event_class") != "SYSTEM_INTERPRETATION"))
        self.assertEqual(len(o["visuals/system_chronology.json"]) - inv["chronology_events"], 1)
        self.assertEqual(inv["sources"], len(o["sources/source_library.json"]))
        self.assertEqual(inv["public_locators"], sum(1 for s in o["sources/source_reference_map.json"]
                                                     if str(s["primary_url"] or "").lower().startswith(("http://", "https://"))))
        self.assertEqual(inv["search_records"], len(o["content/search_index.json"]))
        self.assertEqual(inv["page_specs"], o["page_specs.json"]["spec_count"])

    def test_inventory_tokens_resolved_in_public_text(self):
        """P1.2: Master copy may hold {{n:key}} templates; Page Specs and search records carry values only."""
        pat = re.compile(self.ctx.inputs["public_inventory_contract"]["unresolved_token_pattern"])
        inv = {c["key"]: c["value"] for c in self.ctx.out["content/public_inventory.json"]["counts"]}
        resolved = 0
        for s in self.ctx.out["page_specs.json"]["page_specs"]:
            text = json.dumps([s["full_copy_en"], s["full_copy_ar"], s["meta_description_en"], s["meta_description_ar"], s["sections"]], ensure_ascii=False)
            self.assertIsNone(pat.search(text), s["route"])
            for sec in s["sections"]:
                for t in sec.get("resolved_inventory_tokens", []):
                    self.assertEqual(t["value"], inv[t["key"]])
                    self.assertIn(format(t["value"], ","), sec[t["field"]])
                    resolved += 1
        self.assertGreater(resolved, 0)
        for r in self.ctx.out["content/search_index.json"]:
            self.assertIsNone(pat.search(r.get("search_text_en", "") + r.get("search_text_ar", "")), r["id"])

    def test_inventory_token_guards(self):
        from projection.derived import resolve_inventory_tokens, IntegrityError
        self.assertEqual(resolve_inventory_tokens(self.ctx, "Readings: {{n:readings}}", "t")[0],
                         f"Readings: {len(self.ctx.out['content/readings.json'])}")
        for bad in ("{{n:no_such_key}}", "{{n:search_records}}", "{N_CLAIMS} claims", "{{count}}"):
            with self.assertRaises(IntegrityError, msg=bad):
                resolve_inventory_tokens(self.ctx, bad, "t")


    def test_visual_design_contracts(self):
        """P3: every governed visual is tiered; SIGNATURE/CORE contracts bind resolved rows; governed gaps stay gaps."""
        d = self.ctx.out["visuals/visual_design_contracts.json"]
        lib = [v["visual_id"] for v in self.ctx.out["visuals/visual_library.json"]]
        self.assertEqual(sorted(v["visual_id"] for v in d["visuals"]), sorted(lib))
        by = {v["visual_id"]: v for v in d["visuals"]}
        for v in d["visuals"]:
            self.assertEqual("contract" in v, v["tier"] in ("SIGNATURE", "CORE_ANALYTICAL"), v["visual_id"])
        pos_value = by["VIS-POS-VALUE"]["contract"]["series"][0]
        self.assertEqual([m["x"] for m in pos_value["missing_x"]], ["2025-09"])
        macro = by["VIS-REMITTANCE-MACRO"]["contract"]["series"][0]["values"]
        self.assertEqual([v["id"] for v in macro if "BREAK_VINTAGE" in v["markers"]], ["RMO-IMF-2025-REV"])
        self.assertTrue(all(v["grammar_state"] in ("REPORTED", "ESTIMATED", "PROJECTED") for v in macro))
        anatomy = by["VIS-PAYMENT-ANATOMY"]["contract"]["series"]
        withheld = [v["id"] for s in anatomy for v in s["values"] if v.get("withheld")]
        self.assertEqual(sorted(withheld), ["OBS-00036"])   # close-out CR-06: the H1-2025 accounts count prints with its caveat
        # close-out U6: the third-quarter 2024 bulletin is its own series (panel), every value drawn, none compared
        self.assertEqual([s["id"] for s in anatomy], ["h1_objects", "q3_2024_channels"])
        self.assertTrue(all(v.get("y") is not None for v in anatomy[1]["values"]))

    def test_visual_design_contract_guards(self):
        """A binding that no longer resolves, or a value that no longer equals its guard, stops generation."""
        import copy
        from projection.derived import visual_design_contracts, IntegrityError
        base = self.ctx.inputs["visual_design_contract"]
        try:
            for mutate in (lambda c: c["visuals"][0]["contract"]["series"][0]["rows"]["ids"].append("RMO-NO-SUCH-ROW"),
                           lambda c: c["visuals"][0]["contract"]["series"][0]["must_equal"].update({"RMO-CBY-2024-AR2024": 1}),
                           lambda c: c["visuals"].pop()):
                bad = copy.deepcopy(base)
                mutate(bad)
                self.ctx.inputs["visual_design_contract"] = bad
                with self.assertRaises(IntegrityError):
                    visual_design_contracts(self.ctx, {})
        finally:
            self.ctx.inputs["visual_design_contract"] = base


    def test_question_sets_guards(self):
        """EAD-11: the presentation contract's question sets name only governed questions and headings, Explore's groups
        hold every question once, and Home starts from distinct questions; anything else stops generation."""
        import copy
        from projection import derived
        from projection.structure import StructureError
        base = derived._load_contract(self.ctx, {"path": "presentation_priority.json"})
        self.assertEqual(derived.presentation_contract(self.ctx, {"path": "presentation_priority.json"})["question_sets"], base["question_sets"])
        orig = derived._load_contract
        try:
            for mutate in (lambda c: c["question_sets"][0]["starting_question_ids"].append("QE-999"),
                           lambda c: c["question_sets"][0]["starting_question_ids"].append(c["question_sets"][0]["starting_question_ids"][0]),
                           lambda c: c["question_sets"][1]["question_groups"][0].update({"heading_ui_id": "UI-QUESTIONS-NO-SUCH-HEADING"}),
                           lambda c: c["question_sets"][1]["question_groups"][0]["question_ids"].pop(),
                           lambda c: c["question_sets"].pop()):
                bad = copy.deepcopy(base)
                mutate(bad)
                derived._load_contract = lambda ctx, e, bad=bad: bad
                with self.assertRaises(StructureError):
                    derived.presentation_contract(self.ctx, {"path": "presentation_priority.json"})
        finally:
            derived._load_contract = orig

    def test_visual_display_labels(self):
        """P4 (V-D5/V-D6): every printed chart value carries a governed bilingual label; an unlabelled value stops generation;
        microfinance lanes carry their own id, unit and markers."""
        import copy
        from projection.derived import visual_design_contracts, IntegrityError
        d = self.ctx.out["visuals/visual_design_contracts.json"]
        printed = {"x", "series_label", "lane", "unit", "label", "group", "class", "state", "authority", "count_state", "named", "events", "limit"}
        temporal = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
        for v in d["visuals"]:
            con = v.get("contract")
            if not con:
                continue
            for grp in con["series"] + con["objects"]:
                for it in grp.get("values") or grp.get("records") or []:
                    for f in printed & set(it):
                        val = it[f]
                        if val in (None, "") or temporal.match(str(val)) or (f == "class" and v["visual_id"] in ("RV-CWR-009", "RV-CWR-004")):
                            continue
                        lab = it.get(f + "_label") or {}
                        self.assertTrue(lab.get("en") and lab.get("ar"), f"{v['visual_id']} {grp['id']} {it.get('id')} {f}")
        by = {v["visual_id"]: v for v in d["visuals"]}
        for anatomy in by["VIS-PAYMENT-ANATOMY"]["contract"]["series"]:
            self.assertTrue(all(x.get("is_not_label", {}).get("ar") for x in anatomy["values"]))
            self.assertIn("caveat", anatomy.get("encoding_only_fields", []))
        self.assertTrue(by["VIS-REMITTANCE-COST"]["contract"]["frame_labels"]["UI-VIS-RPW-AVERAGE-NOTE"]["ar"])
        # Tranche C (VIS-03/11/12): non-comparable anchors and unestablished nesting are tables, with a stated promotion condition
        for vid in ("VIS-MFI-DIVERGENCE", "VIS-FIRM-FINANCE-PATH", "VIS-TARGET-RESULT-STATE"):
            self.assertEqual(by[vid]["tier"], "TABLE_TEXT_FIRST")
            self.assertNotIn("contract", by[vid])
            self.assertTrue(by[vid].get("promotion_requires"))
        # VIS-01: a funded project component is placed at the rule/programme step, never at implementation
        mapping = by["RV-CWR-009"]["contract"]["step_mapping"]
        self.assertIn("PAYMENT_RAIL_COMPONENT", mapping["UI-VIS-CHAIN-RULE"])
        self.assertNotIn("PAYMENT_RAIL_COMPONENT", mapping["UI-VIS-CHAIN-IMPLEMENTATION"])
        base = self.ctx.inputs["visual_design_contract"]
        try:
            bad = copy.deepcopy(base)
            bad["display_labels"]["namespaces"]["findex_group"].pop("female")
            self.ctx.inputs["visual_design_contract"] = bad
            with self.assertRaises(IntegrityError):
                visual_design_contracts(self.ctx, {})
        finally:
            self.ctx.inputs["visual_design_contract"] = base

    def test_one_reading_truth(self):
        """P4.2: Reading copy comes from its owners (08 thesis, 03 sections); an edit made only in 09 stops generation."""
        rs = self.ctx.out["content/reading_sections.json"]
        readings = {r["reading_id"]: r for r in self.ctx.out["content/readings.json"]}
        secs = {(F.slash(s["route"]), int(float(s["section_order"]))): s for s in self.ctx.out["content/page_sections.json"]}
        for r in rs:
            rd = readings[r["reading_id"]]
            if int(r["section_order"]) == 1:
                self.assertEqual(r["copy_en"], rd["thesis_en"])
            else:
                self.assertEqual(r["copy_ar"], secs[(F.slash(rd["route"]), int(r["section_order"]))]["body_ar"])
        from projection.derived import IntegrityError
        g = Workbook(MASTER).grid("09_READING_SECTIONS")
        hdr = [str(x) for x in g[3]]
        # 09 is a pure index: no copy in any order, no title after section 1
        for i, x in enumerate(g[4:], 5):
            if not x or not x[0]:
                continue
            self.assertIn(x[hdr.index("copy_en")], (None, ""), f"09 row {i}")
            self.assertIn(x[hdr.index("copy_ar")], (None, ""), f"09 row {i}")
            if int(float(x[1])) > 1:
                self.assertIn(x[hdr.index("title_en")], (None, ""), f"09 row {i}")
        row = next(i for i, x in enumerate(g, 1) if x and x[0] == "CWR-001" and str(x[1]) in ("2", "2.0"))
        col = hdr.index("copy_en") + 1
        # text written into the index stops generation
        with tempfile.TemporaryDirectory() as d:
            ed = MasterEditor(MASTER)
            ed.set_cell("09_READING_SECTIONS", row, col, "A second Reading text", expect=ed.get_value("09_READING_SECTIONS", row, col))
            p = os.path.join(d, "m.xlsx"); ed.save(p)
            with self.assertRaises(IntegrityError):
                build_all(Context(p, ROOT))
        # an edit made once, in the owner (03), reaches the Reading sections without touching 09
        g3 = Workbook(MASTER).grid("03_PAGE_SECTIONS")
        route = F.slash(readings["CWR-001"]["route"])
        r3 = next(i for i, x in enumerate(g3, 1) if x and F.slash(str(x[0])) == route and str(x[1]) in ("2", "2.0") and x[4])
        with tempfile.TemporaryDirectory() as d:
            ed = MasterEditor(MASTER)
            cur = ed.get_value("03_PAGE_SECTIONS", r3, 5)
            ed.set_cell("03_PAGE_SECTIONS", r3, 5, cur + " Owner edit.", expect=cur)
            # Tranche C: full copy is derived by the generator (no longer stored in 02), so one edit in 03 suffices
            p = os.path.join(d, "m.xlsx"); ed.save(p)
            out = build_all(Context(p, ROOT))
            got = next(x for x in out["content/reading_sections.json"] if x["reading_id"] == "CWR-001" and int(x["section_order"]) == 2)
            self.assertTrue(got["copy_en"].endswith(" Owner edit."))

    def test_boundary_parts_bilingual(self):
        """P4.3: 06 limitations carry A | B identically in both languages; the parts are derived, never printed with the delimiter."""
        eo = self.ctx.out["evidence/evidence_objects.json"]
        for r in eo:
            self.assertEqual(bool(r.get("measurement_limitation_en")), bool(r.get("measurement_limitation_ar")), r["object_id"])
            self.assertNotIn(" | ", r.get("does_not_establish_en") or "")
        from projection.structure import StructureError
        g = Workbook(MASTER).grid("06_EVIDENCE_OBJECTS")
        row = next(i for i, x in enumerate(g, 1) if x and x[0] == "CLM-001")
        col = [str(x) for x in g[3]].index("limitations_ar") + 1
        with tempfile.TemporaryDirectory() as d:
            ed = MasterEditor(MASTER)
            cur = ed.get_value("06_EVIDENCE_OBJECTS", row, col)
            ed.set_cell("06_EVIDENCE_OBJECTS", row, col, cur.replace(" | ", " "), expect=cur)
            p = os.path.join(d, "m.xlsx"); ed.save(p)
            with self.assertRaises(StructureError):
                build_all(Context(p, ROOT))


class Writer(unittest.TestCase):
    def test_noop_save_and_row_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            ed = MasterEditor(MASTER)
            out = os.path.join(d, "noop.xlsx")
            ed.save(out)
            with zipfile.ZipFile(MASTER) as a, zipfile.ZipFile(out) as b:
                self.assertEqual(a.namelist(), b.namelist())
                for n in a.namelist():
                    self.assertEqual(a.read(n), b.read(n), n)
            ed = MasterEditor(MASTER)
            before = ed._get("17_INDICATOR_LIBRARY")
            ed.insert_rows("17_INDICATOR_LIBRARY", 6, [{1: "TMP", 2: "row"}])
            ed.delete_rows("17_INDICATOR_LIBRARY", 6, 6)
            self.assertEqual(ed._get("17_INDICATOR_LIBRARY"), before)

    def test_exact_value_guard(self):
        ed = MasterEditor(MASTER)
        with self.assertRaises(Exception):
            ed.set_cell("02_SITE_MAP", 5, 1, "x", expect="not-the-current-value")
        with self.assertRaises(Exception):
            ed.replace_in_cell("02_SITE_MAP", 5, 5, "no-such-substring-xyz", "y", count=1)


if __name__ == "__main__":
    unittest.main()
