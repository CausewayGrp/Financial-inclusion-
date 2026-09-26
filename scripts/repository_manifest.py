# -*- coding: utf-8 -*-
"""Write or check FINAL_REPOSITORY_MANIFEST.json: what every tracked file is, and the one path from authority to
recipient (R8.5, directive D7 §F4).

  python3 scripts/repository_manifest.py           # write
  python3 scripts/repository_manifest.py --check   # exit 1 if the committed manifest is stale or a file is unclassified

Hashes live in SHA256SUMS.txt (scripts/checksums.py); this manifest classifies. Every tracked file must match exactly
one class rule below, so a new file cannot enter the repository without being placed.
"""
import fnmatch, hashlib, json, sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "FINAL_REPOSITORY_MANIFEST.json"
MASTER = "authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx"
SPECS = "site-src/content/page_specs.json"
LOGO = "site-src/assets/CauseWay_Master_Logo.png"

# (class, glob patterns) — first match wins; order runs from specific to general.
RULES = [
    ("AUTHORITY_MASTER", [MASTER]),
    ("AUTHORITY_RULES", ["authority/CORE_CONSTITUTION.md"]),
    ("AUTHORITY_POINTER", ["authority/AUTHORITY.json", "authority/YFI_CURRENT_PROJECT_CONTEXT.json"]),
    ("LOGO_AUTHORITY", [LOGO]),
    ("PROJECTION_GENERATOR", ["scripts/generate_projections.py", "scripts/rebind_authority.py", "scripts/projection/*.py",
                              "scripts/projection/README.md", "scripts/projection/tests/*.py"]),
    ("PROJECTION_CONTRACT", ["scripts/projection/master_structure.json", "scripts/projection/projection_manifest.json",
                             "scripts/projection/controlled_inputs/*"]),
    ("GENERATED_PROJECTION", ["site-src/content/*", "site-src/content/**/*"]),
    ("RUNTIME_SOURCE", ["site-src/app.js", "site-src/styles.css", "site-src/lang-redirect.js", "site-src/deployment.json", "site-src/assets/*"]),
    ("BUILD_AND_GATES", ["scripts/build.py", "scripts/validate.py", "scripts/audit_public_literals.py",
                         "scripts/architecture_diagrams.py", "scripts/checksums.py", "scripts/repository_manifest.py", "scripts/discovery.py",
                         "scripts/handoff_inventory.py",
                         "scripts/literal_audit_allowances.json", "scripts/search_canonical_probe.json", "scripts/tests/*",
                         "audit/tranche_c/checks/*.py", "audit/pre_tranche_c/source_lineage_truth_test.py"]),
    ("GENERATED_PUBLIC_BUILD", ["dist/*", "dist/**/*"]),
    ("GENERATED_LITERAL_CLOSURE", ["audit/PUBLIC_LITERAL_CLOSURE.json"]),
    ("GENERATED_DIAGRAMS", ["design/architecture/*"]),
    ("DESIGN_PACKAGE", ["design/*", "design/**/*"]),          # Claude Design's package and reference implementation (R8.6)
    ("RECIPIENT_HANDOFF", ["handoff/*"]),
    ("CURRENT_DOCUMENT", ["README.md", "CONTRIBUTING.md", "AGENTS.md", "CLAUDE.md", "OPENAI_REENTRY_CHECKPOINT.md",
                          "FINAL_OPEN_ITEMS_REGISTER.md", "docs/CHANGELOG.md", "docs/PRODUCTION_REPOSITORY_PROTOCOL.md",
                          "docs/DEPLOYMENT.md", "docs/SUSTAINABILITY_METHOD.md"]),
    ("REPOSITORY_ENGINEERING", [".github/*", ".github/**/*", ".gitattributes", ".gitignore", "package.json",
                                "requirements.txt", "SHA256SUMS.txt"]),
    ("CURRENT_PROGRAMME_RECORD", ["audit/INDEX.md", "audit/READING_PORTFOLIO_*", "audit/F3_*", "audit/R8_5_*", "audit/F5_*",
                                  "audit/F6_*", "audit/R8_6_*", "audit/SUSTAINABILITY_*", "audit/FINAL_*_ACCEPTANCE*",
                                  "audit/directives/D7_*", "audit/directives/README.md", "audit/reading_integration/*", "audit/reading_integration/**/*",
                                  "audit/final_integration/*", "audit/final_integration/**/*"]),
    ("STANDING_POLICY", ["audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md", "audit/BENCHMARK_AND_COMPARATOR_POLICY.md",
                         "audit/ECONOMIC_CONTEXT_USAGE_POLICY.md", "audit/FINAL_CURRENTNESS_CUTOFF.md", "audit/tranche_c/DRAFTING_RULES.md"]),
    ("AUDIT_HISTORY", ["audit/*", "audit/**/*", "docs/*"]),
]
START_PATH = ["README.md", "handoff/README_FIRST.md", "handoff/CLAUDE_DESIGN_MASTER_PROMPT.md"]


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def tracked():
    """The tracked files (git ls-files); in an extracted archive without .git, every file under the root except caches —
    the same file set scripts/checksums.py uses, so the manifest can be checked from the handoff ZIP (F9)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import checksums  # noqa: E402
    return sorted(p for p in checksums.tracked_files() if p and p != OUT.name)


def classify(path):
    for cls, pats in RULES:
        if any(fnmatch.fnmatchcase(path, p) for p in pats):
            return cls
    return None


def build():
    files = tracked()
    rows, unclassified = [], []
    for p in files:
        c = classify(p)
        (rows if c else unclassified).append((p, c))
    counts = Counter(c for _, c in rows)
    doc = OrderedDict([
        ("schema", "YFIE_FINAL_REPOSITORY_MANIFEST/1.0"),
        ("purpose", "What every tracked file is. One authority -> one projection path -> one runtime content path -> one current recipient start path. Hashes: SHA256SUMS.txt."),
        ("authority", OrderedDict([("production_master", MASTER), ("production_master_sha256", sha(MASTER)),
                                   ("page_specs", SPECS), ("page_specs_sha256", sha(SPECS)),
                                   ("logo", LOGO), ("logo_sha256", sha(LOGO)),
                                   ("rule", "The Production Master is the only semantic authority. Everything under site-src/content, dist, design/architecture and audit/PUBLIC_LITERAL_CLOSURE.json is generated from it and never edited by hand.")])),
        ("paths", OrderedDict([
            ("projection", "authority/…Master.xlsx -> scripts/generate_projections.py (scripts/projection/*, contracts: master_structure.json, projection_manifest.json, controlled_inputs/*) -> site-src/content/**"),
            ("runtime", "site-src/content/** + site-src/app.js + site-src/styles.css + site-src/assets/* -> scripts/build.py -> dist/**"),
            ("change", "Master transaction -> audit/tranche_b_execution/run_stage.py (generate, rebind, build, literal audit, diagrams, validate, --check) -> commit"),
            ("recipient_start", START_PATH),
        ])),
        ("class_counts", OrderedDict(sorted(counts.items()))),
        ("files", [OrderedDict([("path", p), ("class", c)]) for p, c in rows]),
    ])
    return doc, unclassified


def main():
    doc, unclassified = build()
    text = json.dumps(doc, ensure_ascii=False, indent=1) + "\n"
    if unclassified:
        print("UNCLASSIFIED FILES:", *[p for p, _ in unclassified], sep="\n  ")
        sys.exit(1)
    if "--check" in sys.argv:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != text:
            print("REPOSITORY MANIFEST STALE: run python3 scripts/repository_manifest.py and commit")
            sys.exit(1)
        print(f"REPOSITORY MANIFEST CURRENT: {len(doc['files'])} files in {len(doc['class_counts'])} classes")
        return
    OUT.write_text(text, encoding="utf-8")
    print(f"REPOSITORY MANIFEST WRITTEN: {len(doc['files'])} files in {len(doc['class_counts'])} classes")


if __name__ == "__main__":
    main()
