# -*- coding: utf-8 -*-
"""Write or check handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json — the Design recipient's route, content and state map.

  python3 scripts/handoff_inventory.py           # write
  python3 scripts/handoff_inventory.py --check   # exit 1 if the committed inventory is stale

Derived only from the generated projections (Page Specs, navigation and presentation contracts, Readings, Measurement,
questions, evidence objects, source closure, source reference map, chronology, visual contracts, public inventory), the
discovery contract and the reference build in dist/ (for the verification state each Evidence Record actually renders),
so it can never disagree with them. It adds no content: every title is the governed title, every state is one the
product already has. It exists so that Design never has to guess which routes, families, bindings and states it must
cover. The audit runner (audit/tranche_b_execution/run_stage.py) rewrites it after every build.
"""
import hashlib, json, re, sys
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "site-src" / "content"
DIST = ROOT / "dist"
OUT = ROOT / "handoff" / "ROUTE_CONTENT_AND_STATE_INVENTORY.json"
sys.path.insert(0, str(ROOT / "scripts"))
import discovery  # noqa: E402

# How each projection file may be used by Design (F9 clean-room finding M11). Every file under site-src/content must be
# classified here, or --check fails.
#   RENDER       — a direct input: render from it (the governed words, values and states on the page)
#   VIA_SPEC     — its public content already reaches each page through the Page Spec; render the Page Spec's copy
#   CONTRACT     — hand-maintained presentation or navigation contract (not generated from the Master; validated by it)
#   REFERENCE    — not public: read it to understand the system, never render it (values reach pages only through Evidence
#                  Records and the resolved rows in visuals/visual_design_contracts.json)
PROJECTION_ROLES = OrderedDict([
    ("page_specs.json", "RENDER"),
    ("presentation_priority.json", "CONTRACT"),
    ("content/navigation_interaction.json", "CONTRACT"),
    ("content/interface_copy.json", "RENDER"),
    ("content/questions.json", "RENDER"),
    ("content/readings.json", "RENDER"),
    ("content/reading_sections.json", "RENDER"),
    ("content/measurement_agenda.json", "RENDER"),
    ("content/search_index.json", "RENDER"),
    ("content/search_aliases.json", "RENDER"),
    ("content/public_inventory.json", "RENDER"),
    ("content/page_sections.json", "VIA_SPEC"),
    ("content/site_map.json", "REFERENCE"),
    ("content/master_principles.json", "REFERENCE"),
    ("evidence/evidence_objects.json", "RENDER"),
    ("evidence/public_claims.json", "VIA_SPEC"),
    ("evidence/evidence_passports.json", "REFERENCE"),
    ("sources/source_reference_map.json", "RENDER"),
    ("sources/public_object_source_closure.json", "RENDER"),
    ("sources/source_library.json", "REFERENCE"),
    ("sources/indicator_library.json", "REFERENCE"),
    ("sources/local_dataset_catalog.json", "REFERENCE"),
    ("sources/master_dataset_catalog.json", "REFERENCE"),
    ("visuals/visual_design_contracts.json", "RENDER"),
    ("visuals/visual_library.json", "VIA_SPEC"),
    ("visuals/system_chronology.json", "RENDER"),
    ("visuals/system_relationships.json", "RENDER"),
] + [(f"data/{n}", "REFERENCE") for n in (
    "cby_monetary.json", "findex_baseline.json", "findex_codebook.json", "findex_history.json", "findex_subgroups.json",
    "firm_finance.json", "local_data_index.json", "mfi_data.json", "payments_data.json", "providers_data.json",
    "reforms_regulation.json", "remittances.json")])
ROLE_RULES = OrderedDict([
    ("RENDER", "A direct input: render from it."),
    ("VIA_SPEC", "Its public content already reaches each page through the Page Spec; render the Page Spec's copy, not this file."),
    ("CONTRACT", "Hand-maintained presentation or navigation contract, validated by the generator; where it disagrees with governed interface copy or with behaviour asserted by the test suites, those govern (Design brief §2)."),
    ("REFERENCE", "Not public: read it to understand the system; never render it. Its values reach pages only through Evidence Records and the resolved rows in visuals/visual_design_contracts.json."),
])

# Technical (not evidence) states the static baseline already implements and tests (scripts/tests/test_public_tools.py).
TECHNICAL_STATES = [
    ("compare_wrong_count", "/{L}/evidence/compare/?records=CLM-001", "Announced technical input error; no verdict is drawn"),
    ("compare_unknown_id", "/{L}/evidence/compare/?records=CLM-001,NOT-A-RECORD", "Technical input error naming the unknown reference"),
    ("compare_not_comparable_record", "/{L}/evidence/compare/?records=CLM-001,CLM-003", "A real record outside the comparable set: announced as not available for comparison here (a link error, not a finding)"),
    ("compare_malformed", "/{L}/evidence/compare/?records=,,", "Technical input error"),
    ("compare_duplicate", "/{L}/evidence/compare/?records=CLM-001,CLM-001", "A visible 'same record' state, never a comparison"),
    ("search_no_match", "/{L}/ then Search for a string with no match", "Says that no match is not absence of evidence"),
    ("search_index_unavailable", "/{L}/ with /static-data/search_index.json unreachable", "Technical-unavailable state, announced; navigation still works"),
    ("source_link_unknown", "/{L}/data/?source=SRC-NOT-A-SOURCE#source-SRC-NOT-A-SOURCE", "Announced link error; every source stays visible"),
    ("source_filter_no_match", "/{L}/data/ then filter with a string with no match", "Says that no match is not absence of evidence"),
    ("record_context_unknown", "/{L}/contact/?record=CLM-999", "Technical link error; the report path still works"),
    ("record_context_malformed", "/{L}/corrections/?record=%3Cx%3E", "Technical link error"),
    ("record_context_valid", "/{L}/contact/?record=CLM-001", "The originating record is carried into the report action"),
    ("not_found", "/404.html (a static host serves it for any unknown path; python3 -m http.server does not, so open it directly)", "Bilingual 404 (Arabic first), noindex, with routes back into the evidence"),
    ("no_javascript", "any page with JavaScript disabled", "Governed noscript note; every page's evidence stays readable"),
    ("language_switch_state", "/en/evidence/compare/?records=CLM-001,CLM-010 → switch language", "Same route, query and hash in the other edition; the comparison is kept"),
]

# What an Evidence Record's verification section renders, read from the reference build (markers written by build.py).
VERIFICATION_STATES = OrderedDict([
    ("SOURCES_LISTED", ("Original sources listed, each with its source record and original link", ["UI-EVID-OPEN-SOURCE-RECORD", "UI-EVID-OPEN-ORIGINAL-SOURCE"])),
    ("SOURCES_LISTED_SOME_WITHOUT_PUBLIC_LOCATOR", ("Sources listed; a note says some bound sources have no public locator (never named)", ["UI-EVID-SOURCES-WITHOUT-LOCATOR"])),
    ("PARTIALLY_RESOLVED", ("Sources listed, with the governed statement that some inputs are not yet linked to a source", ["UI-VERIFY-PARTIAL"])),
    ("COMPOSITE_OF_OBJECTS", ("Member Evidence Records listed instead of sources, with the composite statement", ["UI-EVID-MEMBERS-HEADING", "UI-VERIFY-COMPOSITE"])),
    ("COMPOSITE_MEMBERS_NOT_LISTED", ("A view that summarises other evidence whose members are not listed: statement only", ["UI-VERIFY-COMPOSITE-UNLISTED"])),
    ("FRAMING_NO_FACT", ("A framing rule with no fact: no source is expected; must not look like missing evidence", ["UI-EVID-FRAMING"])),
    ("SOURCE_NOT_YET_BOUND", ("No source bound yet: the governed unbound statement", ["UI-EVID-UNBOUND"])),
    ("ORIGINAL_NOT_PUBLIC", ("Bound to a source with no public locator: no link and no name; the value may be withheld", ["UI-EVID-NO-STANDALONE-PUBLIC-LOCATOR-IS"])),
    ("NO_SOURCE_RECORD", ("No source record at all", ["UI-EVID-THIS-RECORD-CURRENTLY-HAS-NO"])),
])


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rendered_verification(oid, closure):
    """Classify what dist/en/evidence/<oid>/index.html renders in its source section."""
    p = DIST / "en" / "evidence" / oid / "index.html"
    if not p.exists():
        return None, 0
    t = p.read_text(encoding="utf-8")
    n = t.count('data-evidence-source="')
    m = re.search(r'data-lineage-state="([A-Z_]+)"', t)
    if m:
        return m.group(1), n
    if "data-evidence-source-unavailable" in t:
        return ("ORIGINAL_NOT_PUBLIC" if (closure.get("resolved_source_ids") or []) else "NO_SOURCE_RECORD"), n
    if "data-evidence-sources-without-locator" in t:
        return "SOURCES_LISTED_SOME_WITHOUT_PUBLIC_LOCATOR", n
    return ("SOURCES_LISTED" if n else "NO_SOURCE_RECORD"), n


def build():
    bundle = load(C / "page_specs.json")
    specs = sorted(bundle["page_specs"], key=lambda s: s["route"])
    nav = load(C / "content" / "navigation_interaction.json")
    pres = load(C / "presentation_priority.json")
    pres_routes = {r["route"]: r for r in pres.get("routes") or []}
    fam = {r["route"]: r for r in nav["routes"]}
    hard = defaultdict(list)
    for h in nav.get("hard_state_acceptance") or []:
        r = "/" + h["route"].split("/", 2)[2] if h["route"].startswith(("/ar/", "/en/")) else h["route"]
        hard[r].append(h["state_id"])
    eo = {o["object_id"]: o for o in load(C / "evidence" / "evidence_objects.json")}
    closure = {(x["object_type"], x["object_id"]): x for x in load(C / "sources" / "public_object_source_closure.json")}
    vis = load(C / "visuals" / "visual_design_contracts.json")
    inv = load(C / "content" / "public_inventory.json")
    readings = load(C / "content" / "readings.json")
    reading_by_route = {x["route"]: x for x in readings}
    agenda = load(C / "content" / "measurement_agenda.json")
    questions = load(C / "content" / "questions.json")
    srcmap = load(C / "sources" / "source_reference_map.json")
    chron = load(C / "visuals" / "system_chronology.json")
    next_global = nav.get("route_next_actions") or {}
    tokens_by_visual = visual_tokens(vis)
    ui_by_en = {}
    for r in load(C / "content" / "interface_copy.json"):
        ui_by_en.setdefault(r.get("label_en"), r.get("ui_id"))
    home_qs, explore_groups = baseline_question_sets(ui_by_en)

    # Every projection file is classified.
    have = sorted(str(p.relative_to(C)) for p in C.rglob("*.json"))
    unclassified = [p for p in have if p not in PROJECTION_ROLES]
    missing = [p for p in PROJECTION_ROLES if p not in have]
    if unclassified or missing:
        raise SystemExit(f"handoff_inventory: projection roles out of date: unclassified {unclassified}, missing {missing}")

    public_sources = [x["source_id"] for x in srcmap if discovery_public(x)]
    curated = [x["source_id"] for x in srcmap if x.get("standalone_resource_card_eligible")]
    untyped_displayed = [x["source_id"] for x in srcmap if discovery_public(x) and not x.get("document_label")]
    compare_spec = next(s for s in specs if s["route"] == "/evidence/compare/")
    comparable = []
    for x in (compare_spec.get("governed_evidence_objects") or []) + (compare_spec.get("governed_claims") or []):
        oid = str(x.get("evidence_object_id") or x.get("object_id") or x.get("claim_id") or "")
        if oid and oid not in comparable:
            comparable.append(oid)
    evidence_routes = sorted(s["instance_id"] for s in specs if s.get("page_class") == "evidence_detail" and s.get("instance_id"))
    collections = {
        "/": OrderedDict([("featured_reading", ((next(s for s in specs if s["route"] == "/").get("featured_reading")) or {}).get("reading_id")),
                          ("starting_question_ids", home_qs),
                          ("rule", "Starting questions as the reference build shows them (R8.4A); Explore holds all of them")]),
        "/explore/": OrderedDict([("question_ids", [q.get("question_id") for q in questions]), ("question_groups", explore_groups)]),
        "/evidence/": OrderedDict([("evidence_record_ids", evidence_routes)]),
        "/evidence/compare/": OrderedDict([("comparable_record_ids", comparable),
                                           ("rule", "Only these records can be compared (the Page Spec's governed set); entry into Compare from a record exists only on their pages")]),
        "/readings/": OrderedDict([("reading_ids", [x["reading_id"] for x in readings])]),
        "/measurement/": OrderedDict([("measurement_ids", [m["measurement_id"] for m in agenda])]),
        "/data/": OrderedDict([("displayed_source_ids", public_sources), ("displayed_sources_without_document_type", untyped_displayed),
                               ("curated_resource_ids", curated), ("chronology_event_ids", [c.get("event_id") for c in chron]),
                               ("never_displayed", "sources without a public locator are never named or linked (count: public_inventory sources − public_locators)")]),
    }

    routes, vstates = [], defaultdict(list)
    for s in specs:
        r = s["route"]
        oid = s.get("instance_id")
        ids = lambda arr, *keys: sorted({str(x.get(k)) for x in (s.get(arr) or []) for k in keys if x.get(k)})
        rd_ids = set(ids("governed_readings", "reading_id")) | {str(x) for x in (s.get("related_readings") or []) if isinstance(x, str)}
        rd_ids |= {str(x.get("reading_id")) for x in (s.get("related_readings") or []) if isinstance(x, dict) and x.get("reading_id")}
        if isinstance(s.get("featured_reading"), dict) and s["featured_reading"].get("reading_id"):
            rd_ids.add(str(s["featured_reading"]["reading_id"]))
        evidence_ids = set(ids("governed_evidence_objects", "object_id", "evidence_object_id")) | set(ids("governed_claims", "claim_id"))
        visual_ids = set(s.get("allowed_visual_contract_ids") or [])
        measurement_ids = set(ids("governed_measurement_priorities", "measurement_id"))
        source_ids = set()
        rb = reading_by_route.get(r)
        if rb:
            evidence_ids |= set(rb.get("evidence_bindings") or []) | set(rb.get("claim_bindings") or [])
            visual_ids |= set(rb.get("visual_bindings") or [])
            measurement_ids |= set(rb.get("measurement_bindings") or [])
            source_ids |= set((rb.get("verification_bindings") or {}).get("direct_source_ids") or [])
        sd = []
        if r == "/":
            sd.append("WebSite")
        if s.get("page_class") in ("evidence_detail", "reading_detail"):
            sd.append("BreadcrumbList")
        if s.get("page_class") == "reading_detail":
            sd.append("Article")
        nr = fam.get(r) or {}
        nxt = list(nr.get("explicit_next_actions") or []) + [x for x in (next_global.get(r) or []) if x not in (nr.get("explicit_next_actions") or [])]
        pv = (pres_routes.get(r) or {}).get("primary_verify_destination")
        if pv and pv not in nxt:
            nxt.append(pv)
        row = OrderedDict([
            ("route", r), ("page_family", nr.get("page_family")), ("page_class", s.get("page_class")),
            ("stable_object_id", oid), ("html", OrderedDict((L, "dist" + discovery.localized(r, L) + "index.html") for L in ("en", "ar"))),
            ("title_en", s.get("title_en")), ("title_ar", s.get("title_ar")),
            ("sections", len({x.get("section_order") for x in s.get("sections") or []})),
            ("section_rows_split_by_language", len({x.get("section_order") for x in s.get("sections") or []}) != len(s.get("sections") or [])),
            ("evidence_ids", sorted(evidence_ids)), ("visual_ids", sorted(visual_ids)), ("reading_ids", sorted(rd_ids)),
            ("measurement_ids", sorted(measurement_ids)), ("source_ids", sorted(source_ids)),
            ("source_references", len(s.get("source_references") or [])),
            ("next_actions", nxt), ("next_action_policy", nr.get("next_action_policy")),
        ])
        if r in pres_routes:
            row["presentation_contract"] = OrderedDict([("measurement_limit", pres_routes[r].get("measurement_limit")),
                                                        ("presentation_family", pres_routes[r].get("presentation_family"))])
        if r in collections:
            row["collection"] = collections[r]
        if s.get("page_class") == "evidence_detail" and oid:
            cl = closure.get(("evidence_object", oid)) or {}
            vs, n = rendered_verification(oid, cl)
            row["lineage_state"] = (eo.get(oid) or {}).get("lineage_state")
            row["verification_state"] = vs
            row["public_sources_listed"] = n
            if vs:
                vstates[vs].append(oid)
        row["structured_data"] = sd
        row["hard_state_acceptance"] = hard.get(r, [])
        routes.append(row)

    by_route = {x["route"]: x for x in routes}
    cases = []
    for h in nav.get("hard_state_acceptance") or []:
        base = "/" + h["route"].split("/", 2)[2] if h["route"].startswith(("/ar/", "/en/")) else h["route"]
        rr = by_route.get(base) or {}
        facts = OrderedDict([("page_family", rr.get("page_family"))])
        for k in ("lineage_state", "verification_state", "public_sources_listed"):
            if k in rr:
                facts[k] = rr[k]
        facts["visual_ids"] = rr.get("visual_ids") or []
        facts["visual_grammar_present"] = sorted({tok for v in facts["visual_ids"] for tok in tokens_by_visual.get(v, [])})
        facts["reading_ids"] = rr.get("reading_ids") or []
        cases.append(OrderedDict([("state_id", h["state_id"]), ("route", h["route"]), ("must_prove", h["must_prove"]),
                                  ("data_at_route", facts)]))

    ver = OrderedDict()
    for k, (meaning, ui_ids) in VERIFICATION_STATES.items():
        ver[k] = OrderedDict([("meaning", meaning), ("ui_ids", ui_ids), ("records", sorted(vstates.get(k, [])))])
    stray = sorted(set(vstates) - set(VERIFICATION_STATES))
    if stray:
        raise SystemExit(f"handoff_inventory: unknown rendered verification state(s) {stray}")

    tiers = defaultdict(list)
    for v in vis.get("visuals") or []:
        tiers[v.get("tier")].append(v.get("visual_id"))
    grammar = vis.get("grammar") or {}
    gstates = OrderedDict()
    for group, rows in grammar.items():
        if isinstance(rows, list) and rows and isinstance(rows[0], dict) and "token" in rows[0]:
            gstates[group] = [OrderedDict([("token", x["token"]), ("ui_id", x.get("ui_id"))]) for x in rows]

    doc = OrderedDict([
        ("schema", "YFIE_ROUTE_CONTENT_AND_STATE_INVENTORY/1.2"),
        ("purpose", "Design recipient's map of every route, its family, bindings, collections, next actions and the states Design must cover. Derived; not authority."),
        ("generated_from", OrderedDict([("production_master_sha256", sha(ROOT / "authority" / "Yemen_Financial_Inclusion_Evidence_Master.xlsx")),
                                        ("page_specs_sha256", sha(C / "page_specs.json")), ("generator", "scripts/handoff_inventory.py")])),
        ("counts", OrderedDict((c["key"], c["value"]) for c in inv.get("counts") or [] if isinstance(c.get("value"), int))),
        ("projection_roles", OrderedDict([("rules", ROLE_RULES), ("files", OrderedDict((k, PROJECTION_ROLES[k]) for k in have))])),
        ("page_families", nav.get("page_families")),
        ("routes", routes),
        ("hard_states", OrderedDict([
            ("acceptance_cases", cases),
            ("evidence_lineage_states", OrderedDict((k, len(v)) for k, v in sorted(_group(eo.values(), "lineage_state").items()))),
            ("verification_states", ver),
            ("visual_tiers", OrderedDict((k, sorted(v)) for k, v in sorted(tiers.items(), key=lambda kv: str(kv[0])))),
            ("visual_grammar_states", gstates),
            ("technical_states", [OrderedDict([("state_id", a), ("how_to_reach", b.replace("{L}", "en")), ("expected", c)])
                                  for a, b, c in TECHNICAL_STATES]),
        ])),
        ("journeys", [OrderedDict([("journey_id", j.get("journey_id")), ("persona", j.get("persona")), ("job", j.get("job")),
                                   ("path", j.get("path")), ("success_condition", j.get("success_condition"))]) for j in nav.get("journeys") or []]),
    ])
    return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"


def visual_tokens(vis):
    """Grammar states and structure markers that occur in each visual's resolved rows."""
    out = {}
    def walk(o, acc):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "grammar_state" and isinstance(v, str):
                    acc.add(v)
                elif k in ("markers", "marker") and isinstance(v, (list, str)):
                    acc.update([v] if isinstance(v, str) else [x for x in v if isinstance(x, str)])
                else:
                    walk(v, acc)
        elif isinstance(o, list):
            for x in o:
                walk(x, acc)
    for v in vis.get("visuals") or []:
        acc = set()
        walk(v.get("contract") or {}, acc)
        out[v["visual_id"]] = sorted(acc)
    return out


def baseline_question_sets(ui_by_en):
    """Home's starting questions and Explore's clusters as the reference build renders them (R8.4A decision; the ID sets
    are held in scripts/build.py until the production runtime takes them from a governed contract — register EAD-11)."""
    home, groups = [], []
    p = DIST / "en" / "index.html"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        m = re.search(r'<div class="question-grid compact-grid">(.*?)</div></div></section>', t, re.S)
        home = re.findall(r'data-question-id="([^"]+)"', m.group(1)) if m else []
    p = DIST / "en" / "explore" / "index.html"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for block in re.findall(r'<section class="question-cluster">(.*?)</section>', t, re.S):
            h = re.search(r"<h3>(.*?)</h3>", block, re.S)
            head = h.group(1).strip() if h else ""
            groups.append(OrderedDict([("heading_ui_id", ui_by_en.get(head)), ("question_ids", re.findall(r'data-question-id="([^"]+)"', block))]))
    return home, groups


def discovery_public(src):
    """A source is displayed on /data/ only when it has a public original locator (the publication firewall)."""
    return bool(str(src.get("primary_url") or "").strip())


def _group(items, key):
    out = defaultdict(list)
    for x in items:
        out[str(x.get(key))].append(x)
    return out


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
