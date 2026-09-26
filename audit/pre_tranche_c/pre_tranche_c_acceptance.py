# -*- coding: utf-8 -*-
"""Pre-Tranche-C acceptance matrix: the programme's Definition of Done, checked against the repository as it is.

  python3 audit/pre_tranche_c/pre_tranche_c_acceptance.py [--no-browser] [--out audit/PRE_TRANCHE_C_ACCEPTANCE_MATRIX.csv]

Runs the canonical gates (generator --check, generator tests, build, public-literal audit, validator, browser behaviour
tests) and reads the derived projections to evaluate each of the 18 Definition-of-Done items. Writes one CSV row per item:
item, requirement, evidence, check, result, status (PASS / PASS_WITH_RECORDED_LIMITS / FAIL / NOT_RUN).
It never rewrites historical audit files. Exit 1 if any item FAILs.
"""
import csv, glob, hashlib, html, json, os, re, subprocess, sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "site-src", "content")
DIST = os.path.join(ROOT, "dist")


def run(cmd):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")      # the gates leave no bytecode caches behind
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=env)
    out = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode, (out[-1] if out else "")


def L(p):
    return json.load(open(os.path.join(C, p), encoding="utf-8"))


def text_of(path):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"<main.*?</main>", t, flags=re.S)
    t = m.group(0) if m else t
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"</(p|h[1-6]|li|div|section|summary|dt|dd|tr|figcaption)>", "\n", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def main():
    args = sys.argv[1:]
    out = os.path.join(ROOT, "audit", "PRE_TRANCHE_C_ACCEPTANCE_MATRIX.csv")
    if "--out" in args:
        out = args[args.index("--out") + 1]
    rows = []

    def add(item, req, evidence, check, ok, result, limits=False, not_run=False):
        status = "NOT_RUN" if not_run else ("FAIL" if not ok else ("PASS_WITH_RECORDED_LIMITS" if limits else "PASS"))
        rows.append(OrderedDict([("item", item), ("requirement", req), ("evidence", evidence), ("check", check), ("result", result), ("status", status)]))

    # canonical gates
    g_check = run([sys.executable, "scripts/generate_projections.py", "--check"])
    g_tests = run([sys.executable, "-m", "unittest", "discover", "-s", "scripts/projection/tests", "-t", "."])
    g_build = run([sys.executable, "scripts/build.py"])
    g_lit = run([sys.executable, "scripts/audit_public_literals.py"])
    g_val = run([sys.executable, "scripts/validate.py"])
    g_seed = run([sys.executable, "scripts/tests/test_literal_audit_determinism.py"])          # P5.1
    g_lin = run([sys.executable, "audit/pre_tranche_c/source_lineage_truth_test.py"])          # P5.2
    g_diag = run([sys.executable, "scripts/architecture_diagrams.py", "--check"])
    browser = None
    if "--no-browser" not in args:
        rc, last = run([sys.executable, "scripts/tests/test_public_tools.py"])
        browser = (rc, last)
    val_ok = g_val[0] == 0 and "VALIDATION PASS" in g_val[1]
    lit_ok = g_lit[0] == 0 and "unresolved=0" in g_lit[1]
    inv = {c["key"]: c["value"] for c in L("content/public_inventory.json")["counts"]}

    # 1 tokens and inventory counts
    tok = re.compile(r"\{\{[^{}]*\}\}|\{[A-Z][A-Z0-9_]{1,40}\}")
    tok_hits = [os.path.relpath(f, DIST) for f in glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True) if tok.search(open(f, encoding="utf-8").read())]
    add(1, "No unresolved public template token or stale inventory count", "content/public_inventory.json; validator P1-G01..G04, P4-G01",
        "scan dist for template tokens; validator", not tok_hits and val_ok, f"template tokens in {len(tok_hits)} pages; validator {'PASS' if val_ok else 'FAIL'}")

    # 2 repetition on flagship pages
    rep = {}
    for lang in ("en", "ar"):
        for r in ("people", "finance", "firms", "payments", "remittances", "providers", "access", "reforms"):
            f = os.path.join(DIST, lang, r, "index.html")
            sents = [s.strip() for s in re.split(r"(?<=[.!?؟])\s+|\n", text_of(f)) if len(s.split()) >= 8]
            dup = sum(1 for _, c in Counter(re.sub(r"\W+", " ", s.lower()) for s in sents).items() if c > 1)
            rep[f"{lang}/{r}"] = dup
    worst = max(rep.values())
    add(2, "Flagship public pages have no material avoidable repetition", "audit/P1_PUBLIC_TRUTH_EDITORIAL_CLOSURE.md §3; P2 closure §6",
        "exact repeated sentences (>= 8 words) on the eight domain pages, EN and AR", worst <= 1, f"max repeats on a domain page = {worst}")

    # 3 identifiers
    add(3, "Public/internal identifier treatment is coherent (PID-1)", "P1 closure §4; validator P1-G05", "validator", val_ok, "validator " + ("PASS" if val_ok else "FAIL"))

    # 4 lineage
    clo = L("sources/public_object_source_closure.json")
    states = Counter(r.get("lineage_state") for r in clo if r.get("object_type") == "evidence_object")
    partial = sorted({r["object_id"] for r in clo if r.get("object_type") in ("evidence_object", "visual") and r.get("closure_state") == "PARTIALLY_RESOLVED"})
    add(4, "Source lineage as complete as governed evidence honestly permits", "sources/public_object_source_closure.json; audit/pre_tranche_c/SOURCE_LINEAGE_TRUTH_TEST.json; validator S04.2/S04.3",
        "lineage states of Evidence Records; partial objects listed once; source-lineage truth test; publication firewall",
        val_ok and g_lin[0] == 0, f"{dict(states)}; partial: {', '.join(partial)}; lineage truth test '{g_lin[1]}'; validator {'PASS' if val_ok else 'FAIL'}",
        limits=bool(partial))

    # 5 held additions
    led = list(csv.DictReader(open(os.path.join(ROOT, "audit", "pre_tranche_c", "FINDINGS_LEDGER.csv"), encoding="utf-8")))
    held = [r for r in led if r["session"].startswith("P1.6")]
    undecided = [r["finding_id"] for r in held if not r["final_status"].startswith(("CLOSED", "DEFERRED"))]
    tracked = [r["finding_id"] for r in led if r["final_status"].startswith("OPEN")]
    add(5, "Every high-value HELD public addition has a final disposition", "P1 closure §7; FINDINGS_LEDGER.csv (session P1.6)",
        "each held-addition row is CLOSED (applied or rejected) or DEFERRED with a destination", not undecided,
        f"{len(held)} held additions: " + ", ".join(f"{r['finding_id']} {r['final_status']}" for r in held) + f"; other tracked open items (not held additions): {tracked}")

    # 6 Reading verification paths
    rd = L("content/readings.json")
    missing = []
    for r in rd:
        for lang in ("en", "ar"):
            f = os.path.join(DIST, lang, r["route"].strip("/"), "index.html")
            if 'class="reading-path"' not in open(f, encoding="utf-8").read():
                missing.append(f"{lang}{r['route']}")
    add(6, "Reading verification paths are explicit", "P1 closure §6; build reading_verification_links", "each Reading page renders its proposition→record→source path",
        not missing, f"{len(rd)} Readings × 2 languages; missing: {missing or 'none'}")

    # 7 Compare URL state; 9 tool behaviour
    js = open(os.path.join(DIST, "assets", "app.js"), encoding="utf-8").read()
    cmp_ok = "get('records')" in js and "history.replaceState" in js and "data-compare-url-error" in js
    if browser is None:
        add(7, "Compare is shareable and reloadable through URL state", "P2 closure §2; scripts/tests/test_public_tools.py", "runtime contract tokens (browser suite not run)", cmp_ok, "tokens present; behaviour not exercised" if cmp_ok else "missing", not_run=True)
    else:
        add(7, "Compare is shareable and reloadable through URL state", "P2 closure §2; scripts/tests/test_public_tools.py", "browser suite (11 Compare tests)",
            browser[0] == 0 and cmp_ok, browser[1])
    probe = json.load(open(os.path.join(ROOT, "audit", "pre_tranche_c", "runs", "SEARCH_CANONICAL_PROBE_BEFORE_AFTER.json"), encoding="utf-8"))
    add(8, "High-value search intents are strong; remaining weak intents are reasoned", "scripts/search_canonical_probe.json; validator P2-G01; P2 closure §3",
        "canonical probe (validator re-runs it)", val_ok and probe["after"]["grades"].get("PASS") == 60, f"after: {probe['after']['grades']}; legacy 28-term: {probe['legacy_28_term_probe']['after']['grades']}")
    add(9, "The behavioural state of every core public tool is known", "audit/P2_TOOL_DISCOVERY_CLOSURE.md §4; browser suite", "browser suite",
        browser is None or browser[0] == 0, browser[1] if browser else "browser suite not run (--no-browser)", not_run=browser is None)

    # 10, 11 visuals
    vdc = L("visuals/visual_design_contracts.json")
    lib = L("visuals/visual_library.json")
    tiered = sum(vdc["tier_counts"].values())
    add(10, "All 36 visual contracts have a presentation-priority disposition", "visuals/visual_design_contracts.json; P3 closure §2", "tier per governed visual",
        tiered == len(lib) == inv["visual_contracts"], f"{vdc['tier_counts']}")
    blockers = {v["visual_id"]: v["contract"]["blockers"] for v in vdc["visuals"] if v.get("contract") and v["contract"]["blockers"]}
    add(11, "Every SIGNATURE/CORE visual is implementation-ready without reverse-engineering", "data contracts; validator P3-G01; handoff/VISUAL_DESIGN_CONTRACT.md",
        "complete data contract per SIGNATURE/CORE visual; release blockers recorded", val_ok, f"release blockers: {blockers}", limits=bool(blockers))

    # 12 Reading authority
    man = json.load(open(os.path.join(ROOT, "scripts", "projection", "projection_manifest.json"), encoding="utf-8"))
    rs = next(o for o in man["outputs"] if o["path"] == "content/reading_sections.json")
    add(12, "One canonical Reading-body authority exists", "P4 closure §3; generator rule reading_sections; test_one_reading_truth",
        "reading_sections.json is DERIVED from 08/03; 09 is a pure index and generation stops if text is written into it; generator tests",
        rs["kind"] == "DERIVED" and rs["rule_id"] == "reading_sections" and g_tests[0] == 0,
        f"{rs['kind']} / {rs['rule_id']}; generator tests: {g_tests[1]}")

    # 13 limitations
    eo = L("evidence/evidence_objects.json")
    b = sum(1 for r in eo if r.get("measurement_limitation_en"))
    parity = all(bool(r.get("measurement_limitation_en")) == bool(r.get("measurement_limitation_ar")) for r in eo)
    add(13, "Limitations and prohibited inference have a deliberate final architecture", "P4 closure §4; 06 limitations A | B; validator S04.1/P4-G02; test_boundary_parts_bilingual",
        "both parts derived; bilingual parity", parity and val_ok, f"{len(eo)} records; {b} with a recorded limit of the measure in both languages")

    # 14 current state
    add(14, "All current-state control and handoff documents describe the actual repository", "P4 closure §2; validator P4-G01 (counts), P4-G03 (navigation), P4-G04 (hashes), P4-G05 (diagrams); rebind_authority.py",
        "validator", val_ok, "validator " + ("PASS" if val_ok else "FAIL"))

    # 15 caches
    caches = [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "**", "__pycache__"), recursive=True)] + \
             [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "**", "*.pyc"), recursive=True)]
    add(15, "Caches and temporary artefacts are absent", "P4 closure §6", "scan for __pycache__ and *.pyc (the gates run with PYTHONDONTWRITEBYTECODE=1)",
        not caches, f"{len(caches)} cache paths" + (f": {caches[:5]}" if caches else ""))

    # 16 determinism
    add(16, "The Master deterministically regenerates every controlled projection", "scripts/generate_projections.py --check; scripts/tests/test_literal_audit_determinism.py",
        "generator --check; literal audit identical across PYTHONHASHSEED values", g_check[0] == 0 and g_seed[0] == 0, f"{g_check[1]}; {g_seed[1]}")

    # 17 gates
    all_green = g_check[0] == 0 and g_tests[0] == 0 and g_build[0] == 0 and lit_ok and val_ok and g_seed[0] == 0 and g_lin[0] == 0 and g_diag[0] == 0 \
        and (browser is None or browser[0] == 0)
    add(17, "All validation gates remain green", "generator check; generator tests; build; literal audit; validator; seed determinism; lineage truth test; diagram check; browser suite",
        "exit codes", all_green, f"check {g_check[0]}; tests {g_tests[0]}; build {g_build[0]}; literal '{g_lit[1]}'; validator '{g_val[1]}'; seed determinism {g_seed[0]}; lineage truth {g_lin[0]}; diagrams {g_diag[0]}; browser {browser[1] if browser else 'not run'}",
        limits=browser is None)

    # 18 one canonical state
    auth = json.load(open(os.path.join(ROOT, "authority", "AUTHORITY.json"), encoding="utf-8"))
    ms = hashlib.sha256(open(os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx"), "rb").read()).hexdigest()
    add(18, "The resulting ZIP is one canonical repository state, not a parallel truth", "SHA256SUMS.txt; single-root ZIP; AUTHORITY.json",
        "Master hash equals AUTHORITY.json; checksum manifest verified at packaging", ms == auth["production_master"]["sha256"], f"Master {ms[:12]}…; ZIP verification recorded in the P5 closure (audit/P5_INDEPENDENT_ACCEPTANCE_CORRECTIONS.md)")

    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    c = Counter(r["status"] for r in rows)
    print(f"PRE-TRANCHE-C ACCEPTANCE: {dict(c)} -> {os.path.relpath(out, ROOT)}")
    sys.exit(1 if c.get("FAIL") else 0)


if __name__ == "__main__":
    main()
