# -*- coding: utf-8 -*-
"""Write or check handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json — the Design recipient's route, content and hard-state map.

  python3 scripts/handoff_inventory.py           # write
  python3 scripts/handoff_inventory.py --check   # exit 1 if the committed inventory is stale

Derived only from the generated projections (Page Specs, navigation contract, evidence objects, visual contracts, public
inventory) and the discovery contract, so it can never disagree with them. It adds no content: every title is the
governed title, every state is one the product already has. It exists so that Design never has to guess which routes,
families, bindings and hard states it must cover.
"""
import hashlib, json, sys
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "site-src" / "content"
OUT = ROOT / "handoff" / "ROUTE_CONTENT_AND_STATE_INVENTORY.json"
sys.path.insert(0, str(ROOT / "scripts"))
import discovery  # noqa: E402

# Technical (not evidence) states the static baseline already implements and tests (scripts/tests/test_public_tools.py).
TECHNICAL_STATES = [
    ("compare_wrong_count", "/{L}/evidence/compare/?records=CLM-001", "Announced technical input error; no verdict is drawn"),
    ("compare_unknown_id", "/{L}/evidence/compare/?records=CLM-001,NOT-A-RECORD", "Technical input error naming the unknown reference"),
    ("compare_malformed", "/{L}/evidence/compare/?records=,,", "Technical input error"),
    ("compare_duplicate", "/{L}/evidence/compare/?records=CLM-001,CLM-001", "A visible 'same record' state, never a comparison"),
    ("search_no_match", "/{L}/ then Search for a string with no match", "Says that no match is not absence of evidence"),
    ("search_index_unavailable", "/{L}/ with /static-data/search_index.json unreachable", "Technical-unavailable state, announced; navigation still works"),
    ("source_link_unknown", "/{L}/data/?source=SRC-NOT-A-SOURCE#source-SRC-NOT-A-SOURCE", "Announced link error; every source stays visible"),
    ("source_filter_no_match", "/{L}/data/ then filter with a string with no match", "Says that no match is not absence of evidence"),
    ("record_context_unknown", "/{L}/contact/?record=CLM-999", "Technical link error; the report path still works"),
    ("record_context_malformed", "/{L}/corrections/?record=%3Cx%3E", "Technical link error"),
    ("record_context_valid", "/{L}/contact/?record=CLM-001", "The originating record is carried into the report action"),
    ("not_found", "/{L}/no-such-page/", "Bilingual 404 (Arabic first), noindex, with routes back into the evidence"),
    ("no_javascript", "any page with JavaScript disabled", "Governed noscript note; every page's evidence stays readable"),
    ("language_switch_state", "/en/evidence/compare/?records=CLM-001,CLM-003 → switch language", "Same route, query and hash in the other edition"),
]


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build():
    bundle = load(C / "page_specs.json")
    specs = sorted(bundle["page_specs"], key=lambda s: s["route"])
    nav = load(C / "content" / "navigation_interaction.json")
    fam = {r["route"]: r for r in nav["routes"]}
    hard = defaultdict(list)
    for h in nav.get("hard_state_acceptance") or []:
        r = "/" + h["route"].split("/", 2)[2] if h["route"].startswith(("/ar/", "/en/")) else h["route"]
        hard[r].append(h["state_id"])
    eo = {o["object_id"]: o for o in load(C / "evidence" / "evidence_objects.json")}
    vis = load(C / "visuals" / "visual_design_contracts.json")
    closure = load(ROOT / "scripts" / "projection" / "controlled_inputs" / "closure_templates.json")
    inv = load(C / "content" / "public_inventory.json")

    routes = []
    for s in specs:
        r = s["route"]
        oid = s.get("instance_id")
        ids = lambda arr, k: sorted({str(x.get(k)) for x in (s.get(arr) or []) if x.get(k)})
        readings = set(ids("governed_readings", "reading_id")) | {str(x) for x in (s.get("related_readings") or []) if isinstance(x, str)}
        readings |= {str(x.get("reading_id")) for x in (s.get("related_readings") or []) if isinstance(x, dict) and x.get("reading_id")}
        if isinstance(s.get("featured_reading"), dict) and s["featured_reading"].get("reading_id"):
            readings.add(str(s["featured_reading"]["reading_id"]))
        sd = []
        if r == "/":
            sd.append("WebSite")
        if s.get("page_class") in ("evidence_detail", "reading_detail"):
            sd.append("BreadcrumbList")
        if s.get("page_class") == "reading_detail":
            sd.append("Article")
        routes.append(OrderedDict([
            ("route", r), ("page_family", (fam.get(r) or {}).get("page_family")), ("page_class", s.get("page_class")),
            ("stable_object_id", oid), ("html", OrderedDict((L, "dist" + discovery.localized(r, L) + "index.html") for L in ("en", "ar"))),
            ("title_en", s.get("title_en")), ("title_ar", s.get("title_ar")), ("sections", len(s.get("sections") or [])),
            ("evidence_ids", ids("governed_evidence_objects", "object_id")),
            ("visual_ids", sorted(s.get("allowed_visual_contract_ids") or [])),
            ("reading_ids", sorted(readings)),
            ("measurement_ids", ids("governed_measurement_priorities", "measurement_id")),
            ("source_references", len(s.get("source_references") or [])),
            ("lineage_state", (eo.get(oid) or {}).get("lineage_state") if oid else None),
            ("structured_data", sd),
            ("hard_state_acceptance", hard.get(r, [])),
        ]))

    lin = defaultdict(list)
    for o in eo.values():
        lin[o.get("lineage_state")].append(o["object_id"])
    templates = closure.get("verification_templates") or {}
    lineage = OrderedDict()
    for k in sorted(lin, key=str):
        lineage[str(k)] = OrderedDict([("records", len(lin[k])), ("verification_copy_ui_id", templates.get(k)),
                                       ("example_routes", [f"/en/evidence/{x}/" for x in sorted(lin[k])[:3]])])
    tiers = defaultdict(list)
    for v in vis.get("contracts") or vis.get("visuals") or []:
        tiers[v.get("tier")].append(v.get("visual_id"))
    if not tiers:
        for k, v in vis.items():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "tier" in v[0]:
                for x in v:
                    tiers[x.get("tier")].append(x.get("visual_id"))
    grammar = vis.get("grammar") or {}
    gstates = OrderedDict()
    for group, rows in grammar.items():
        if isinstance(rows, list) and rows and isinstance(rows[0], dict) and "token" in rows[0]:
            gstates[group] = [OrderedDict([("token", x["token"]), ("ui_id", x.get("ui_id"))]) for x in rows]

    doc = OrderedDict([
        ("schema", "YFIE_ROUTE_CONTENT_AND_STATE_INVENTORY/1.0"),
        ("purpose", "Design recipient's map of every route, its family, bindings and the hard states Design must cover. Derived; not authority."),
        ("generated_from", OrderedDict([("production_master_sha256", sha(ROOT / "authority" / "Yemen_Financial_Inclusion_Evidence_Master.xlsx")),
                                        ("page_specs_sha256", sha(C / "page_specs.json")), ("generator", "scripts/handoff_inventory.py")])),
        ("counts", OrderedDict((c["key"], c["value"]) for c in inv.get("counts") or [] if isinstance(c.get("value"), int))),
        ("page_families", nav.get("page_families")),
        ("routes", routes),
        ("hard_states", OrderedDict([
            ("acceptance_cases", [OrderedDict([("state_id", h["state_id"]), ("route", h["route"]), ("must_prove", h["must_prove"])])
                                  for h in nav.get("hard_state_acceptance") or []]),
            ("evidence_lineage_states", lineage),
            ("visual_tiers", OrderedDict((k, sorted(v)) for k, v in sorted(tiers.items(), key=lambda kv: str(kv[0])))),
            ("visual_grammar_states", gstates),
            ("technical_states", [OrderedDict([("state_id", a), ("how_to_reach", b.replace("{L}", "en") if "{L}" in b else b),
                                               ("expected", c)]) for a, b, c in TECHNICAL_STATES]),
        ])),
        ("journeys", [OrderedDict([("journey_id", j.get("journey_id")), ("persona", j.get("persona")), ("job", j.get("job")),
                                   ("path", j.get("path")), ("success_condition", j.get("success_condition"))]) for j in nav.get("journeys") or []]),
    ])
    return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"


def main():
    text = build()
    if "--check" in sys.argv:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != text:
            print("HANDOFF INVENTORY STALE: run python3 scripts/handoff_inventory.py and commit")
            sys.exit(1)
        print("HANDOFF INVENTORY CURRENT")
        return
    OUT.write_text(text, encoding="utf-8")
    print(f"HANDOFF INVENTORY WRITTEN: {len(json.loads(text)['routes'])} routes")


if __name__ == "__main__":
    main()
