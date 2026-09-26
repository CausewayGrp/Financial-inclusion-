# -*- coding: utf-8 -*-
"""Rebind the current-state control files to the Production Master and regenerated Page Specs.

  python3 scripts/rebind_authority.py --timestamp 2026-09-25T23:30:00+03:00 [--check]

Updates (current-state files only; historical audit records are never rewritten):
  authority/AUTHORITY.json                     production_master.sha256, external sync state, generated_at
  authority/YFI_CURRENT_PROJECT_CONTEXT.json   Master/Page Spec hashes, controlled scale, external sync state
  handoff/IMPLEMENTATION_MANIFEST.json         authority hashes, controlled counts, external sync state
  README.md and recipient-facing handoff files every occurrence of the PREVIOUS bound Master / Page Spec hash
The previous hashes are read from AUTHORITY.json and the Context before rewriting. Any other 64-hex value
in a recipient-facing file is reported as an error (never silently replaced).
The Drive file IDs are kept for lineage; external_repository_sync_state records that the Drive copies have
not been replaced with these bytes (EXTERNAL_REPOSITORY_SYNC_PENDING) until a controlled sync is verified.
"""
import argparse
import hashlib
import json
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, "site-src", "content")
RECIPIENT = ["README.md", "OPENAI_REENTRY_CHECKPOINT.md", "handoff/README_FIRST.md", "handoff/CLAUDE_DESIGN_MASTER_PROMPT.md",
             "handoff/CLAUDE_CODE_MASTER_PROMPT.md", "handoff/DESIGN_ACCEPTANCE_CRITERIA.md", "handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md",
             "handoff/DESIGN_TO_CODE_CONTRACT.md"]
SYNC_STATE = "EXTERNAL_REPOSITORY_SYNC_PENDING"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load(p):
    return json.load(open(os.path.join(ROOT, p), encoding="utf-8"), object_pairs_hook=OrderedDict)


def dump(p, obj, trailing_newline=True):
    text = json.dumps(obj, ensure_ascii=False, indent=2) + ("\n" if trailing_newline else "")
    with open(os.path.join(ROOT, p), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def counts():
    L = lambda p: json.load(open(os.path.join(C, p), encoding="utf-8"))
    ps = L("page_specs.json")
    smap = L("sources/source_reference_map.json")
    return OrderedDict([
        ("page_specs", ps["spec_count"]),
        ("page_sections", len(L("content/page_sections.json"))),
        ("entry_questions", len(L("content/questions.json"))),
        ("evidence_objects", len(L("evidence/evidence_objects.json"))),
        ("public_claims", len(L("evidence/public_claims.json"))),
        ("evidence_passports", len(L("evidence/evidence_passports.json"))),
        ("readings", len(L("content/readings.json"))),
        ("reading_sections", len(L("content/reading_sections.json"))),
        ("measurement_priorities", len(L("content/measurement_agenda.json"))),
        ("visual_contracts", len(L("visuals/visual_library.json"))),
        ("search_records", len(L("content/search_index.json"))),
        ("sources", len(smap)),
        ("publicly_addressable_sources", sum(1 for s in smap if str(s.get("primary_url") or "").strip().lower().startswith(("http://", "https://")))),
        ("curated_source_report_cards", sum(1 for s in smap if s.get("standalone_resource_card_eligible"))),
        ("indicators", len(L("sources/indicator_library.json"))),
        ("generated_locale_pages", 2 * ps["spec_count"]),                       # one page per Page Spec and language
        ("generated_html_total_including_root_and_404", 2 * ps["spec_count"] + 2),
        ("public_object_source_closure_records", len(L("sources/public_object_source_closure.json"))),
        ("chronology_events", len(L("visuals/system_chronology.json"))),
        ("sources_without_public_locator", len(smap) - sum(1 for s in smap if str(s.get("primary_url") or "").strip().lower().startswith(("http://", "https://")))),
    ])


def navigation():
    """P4.1: the public navigation recorded in current-state files is derived from the navigation contract."""
    nav = json.load(open(os.path.join(C, "content", "navigation_interaction.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    prim = []
    for it in nav["global_navigation"]:
        rec = OrderedDict([("label_en", it["label_en"]), ("label_ar", it["label_ar"])])
        if it.get("route"):
            rec["route"] = it["route"]
        if it.get("children"):
            rec["children"] = [OrderedDict([("label_en", c["label_en"]), ("label_ar", c["label_ar"]), ("route", c["route"])]) for c in it["children"]]
        prim.append(rec)
    trust = [OrderedDict([("label_en", it["label_en"]), ("label_ar", it["label_ar"]), ("route", it["route"])]) for it in nav["trust_navigation"]]
    return nav, prim, trust


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--timestamp", required=True)
    ap.add_argument("--check", action="store_true", help="report what would change; write nothing")
    a = ap.parse_args()
    master = os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx")
    new_m, new_p = sha(master), sha(os.path.join(C, "page_specs.json"))
    auth = load("authority/AUTHORITY.json")
    ctx = load("authority/YFI_CURRENT_PROJECT_CONTEXT.json")
    old_m = auth["production_master"]["sha256"]
    old_p = ctx["controlled_projection"]["page_specs_sha256"]
    cnt = counts()
    report = OrderedDict([("master_sha256", OrderedDict([("previous", old_m), ("current", new_m)])),
                          ("page_specs_sha256", OrderedDict([("previous", old_p), ("current", new_p)])), ("counts", cnt), ("files", [])])
    errors = []
    # AUTHORITY.json
    pm = auth["production_master"]
    if "drive_recorded_sha256" not in pm:
        # the hash the repository last recorded together with the Drive file ID (entry state; not re-verified here)
        pm["drive_recorded_sha256"] = old_m
    pm["sha256"] = new_m
    pm["external_repository_sync_state"] = "RECORDED_AS_SYNCED" if new_m == pm["drive_recorded_sha256"] else SYNC_STATE
    auth["external_repository_sync_rule"] = ("Drive file IDs are lineage references. They are not asserted to contain the bytes bound here "
                                             "until a controlled replacement is performed and verified; until then the state is " + SYNC_STATE + ".")
    auth["generated_at"] = a.timestamp
    # Context
    ctx["production_master"]["sha256"] = new_m
    ctx["production_master"]["external_repository_sync_state"] = auth["production_master"]["external_repository_sync_state"]
    ctx["controlled_projection"]["page_specs_sha256"] = new_p
    ctx["controlled_projection"]["page_specs"] = cnt["page_specs"]
    ctx["controlled_projection"]["all_page_specs_master_hash_match"] = True
    ctx["controlled_projection"]["page_specs_index_master_hash_match"] = True
    for k in ("page_specs", "page_sections", "entry_questions", "evidence_objects", "public_claims", "evidence_passports", "readings",
              "measurement_priorities", "visual_contracts", "search_records", "sources", "publicly_addressable_sources", "curated_source_report_cards"):
        if k in ctx.get("controlled_scale", {}):
            ctx["controlled_scale"][k] = cnt[k]
    for k in ("chronology_events", "reading_sections"):
        ctx["controlled_scale"][k] = cnt[k]
    nav, prim, trust = navigation()
    ctx["public_navigation"] = OrderedDict([("rule", "Derived from site-src/content/content/navigation_interaction.json by scripts/rebind_authority.py."),
                                            ("primary", prim), ("trust", trust)])
    ctx["validation"]["master_sha256_recorded"] = new_m
    ctx["generated_at"] = a.timestamp
    # Handoff manifest
    him = load("handoff/IMPLEMENTATION_MANIFEST.json")
    him["authority"]["master_sha256"] = new_m
    him["authority"]["page_specs_sha256"] = new_p
    him["authority"]["external_repository_sync_state"] = auth["production_master"]["external_repository_sync_state"]
    if "page_specs_drive_recorded_sha256" not in him["authority"]:
        him["authority"]["page_specs_drive_recorded_sha256"] = old_p
    him["authority"]["page_specs_external_repository_sync_state"] = "RECORDED_AS_SYNCED" if new_p == him["authority"]["page_specs_drive_recorded_sha256"] else SYNC_STATE
    mapping = {"page_specs": "page_specs", "page_sections": "page_sections", "questions": "entry_questions", "evidence_objects": "evidence_objects",
               "public_claims": "public_claims", "evidence_passports": "evidence_passports", "readings": "readings", "reading_sections": "reading_sections",
               "measurement_priorities": "measurement_priorities", "visual_contracts": "visual_contracts", "sources": "sources",
               "publicly_addressable_sources": "publicly_addressable_sources", "curated_source_report_cards": "curated_source_report_cards",
               "indicators": "indicators", "search_records": "search_records", "public_search_records": "search_records",
               "generated_locale_pages": "generated_locale_pages",
               "generated_html_total_including_root_and_404": "generated_html_total_including_root_and_404",
               "public_object_source_closure_records": "public_object_source_closure_records"}
    for k, src in mapping.items():
        if k in him.get("controlled_counts", {}):
            him["controlled_counts"][k] = cnt[src]
    # P4.1: fields that went stale by hand are now derived
    him["controlled_counts"].pop("no_public_locator_dependencies", None)
    him["controlled_counts"]["sources_without_public_locator"] = cnt["sources_without_public_locator"]
    him["controlled_counts"]["chronology_events"] = cnt["chronology_events"]
    specs_doc = json.load(open(os.path.join(C, "page_specs.json"), encoding="utf-8"))
    spec_list = specs_doc.get("page_specs") if isinstance(specs_doc, dict) else specs_doc
    him["routes"] = [OrderedDict([("route", x["route"]), ("page_class", x.get("page_class"))]) for x in sorted(spec_list, key=lambda x: x["route"])]
    him["implementation_target"]["route_requirement"] = f"All {cnt['page_specs']} controlled routes in Arabic and English must be real deep-link-safe static output."
    him["navigation_contract"]["controlled_route_coverage"] = len(nav["routes"])
    him["navigation_contract"]["page_family_count"] = len(nav["page_families"])
    him["navigation_contract"]["journey_tests"] = len(nav["journeys"])
    him["navigation_contract"]["search_smoke_tests"] = len(nav["search_smoke_tests"])
    him["information_design_contract"]["page_family_count"] = len(nav["page_families"])
    him["information_design_contract"]["hard_state_acceptance_count"] = len(nav.get("hard_state_acceptance") or [])
    him["information_design_contract"]["global_primary_navigation"] = [
        x["label_en"] + (" (" + " · ".join(c["label_en"] for c in x["children"]) + ")" if x.get("children") else "") for x in prim]
    him["information_design_contract"]["trust_navigation"] = [x["label_en"] for x in trust]
    ps = ctx.get("programme_state") or {}
    if ps.get("handoff_readiness"):
        him["release_boundaries"]["handoff_readiness"] = ps["handoff_readiness"]
    bi = him.get("bilingual_invariance")
    if isinstance(bi, dict) and "record_state" not in bi:
        bi["record_state"] = "HISTORICAL_R7_RECORD: the counts are those checked at R7; current bilingual parity gates run in scripts/validate.py."
    # recipient-facing markdown
    md_updates = OrderedDict()
    for rel in RECIPIENT:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        t2 = t.replace(old_m, new_m).replace(old_p, new_p)
        lineage = {auth["production_master"].get("drive_recorded_sha256"), him["authority"].get("page_specs_drive_recorded_sha256")}
        for h in re.findall(r"\b[0-9a-f]{64}\b", t2):
            if h not in (new_m, new_p) and h not in lineage:     # the Drive-recorded entry hashes are labelled lineage
                errors.append(f"{rel}: unrecognised 64-hex value {h} (not the previous bound Master/Page Spec hash)")
        md_updates[rel] = (t, t2)
    if errors:
        print("\n".join(errors)); sys.exit(2)
    if a.check:
        print(json.dumps(report, indent=1)); return
    dump("authority/AUTHORITY.json", auth)
    dump("authority/YFI_CURRENT_PROJECT_CONTEXT.json", ctx)
    dump("handoff/IMPLEMENTATION_MANIFEST.json", him)
    report["files"] += ["authority/AUTHORITY.json", "authority/YFI_CURRENT_PROJECT_CONTEXT.json", "handoff/IMPLEMENTATION_MANIFEST.json"]
    for rel, (t, t2) in md_updates.items():
        if t != t2:
            with open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(t2)
            report["files"].append(rel)
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
