# Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن

This is the **single production repository** for Yemen Financial Inclusion Evidence, a bilingual public evidence
resource. It helps users understand, compare and verify evidence on financial inclusion in Yemen.

## Current authority

- **Production Master:** `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`
- **Production Master SHA-256:** `f0150122895d88169e9c9ec947633deda04a02c710a28d7b0de2972214547224`
- **Durable principles:** `authority/CORE_CONSTITUTION.md`
- **Compact current projection, including the programme state:** `authority/YFI_CURRENT_PROJECT_CONTEXT.json`
- **Controlled Page Specs:** `site-src/content/page_specs.json`
- **Page Specs SHA-256:** `bd010a2053898a971944ba63ab3276aeb455428069813097dbc8a07037c88295`

The Production Master is the sole semantic, evidence, source, rights, controlled-product-state and publication-state
authority. Everything else is a subordinate projection or implementation: the Context, the Page Specs, design
artefacts and code. A material content or evidence defect is corrected in the Master first and then regenerated
downstream. External (Drive) copies are `EXTERNAL_REPOSITORY_SYNC_PENDING`.

## Current stage

| Programme | State |
|---|---|
| R0–R8.3 | CLOSED / PASS |
| R8.4 | CLOSED / PASS for every non-Reading surface (Tranche C); Reading prose HELD for the independent Reading package. R8.4A CLOSED / PASS |
| Tranche A; Tranche B specification and execution | CLOSED |
| Pre-Tranche-C maturation P1–P4; corrections P5 | CLOSED; independently accepted |
| Tranche C (whole-product adversarial acceptance) | **COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE** |
| R8.5 subtraction and recipient cleanup; R8.6 clean-room Design handoff | Not started |

- This is **not** DESIGN HANDOFF READY and **not** PUBLIC RELEASE READY.
- The design and implementation prompts in `handoff/` remain **DRAFT — DO NOT EXECUTE YET**.
- Start re-entry at `OPENAI_REENTRY_CHECKPOINT.md`. Current closure: `audit/TRANCHE_C_FINAL_ACCEPTANCE.md`, with
  `audit/TRANCHE_C_FINDINGS_LEDGER.csv` and `audit/FINAL_CURRENTNESS_CUTOFF.md` (cut-off 26 September 2026).
- Earlier closures (lineage): `audit/P1_PUBLIC_TRUTH_EDITORIAL_CLOSURE.md` … `audit/P5_INDEPENDENT_ACCEPTANCE_CORRECTIONS.md`;
  findings ledger `audit/pre_tranche_c/FINDINGS_LEDGER.csv`.

## Product scale

Counts come from `site-src/content/content/public_inventory.json`, which is derived from the Master. The validator checks
the figures below against it.

- 143 controlled Page Specs; 286 localized route documents + root + 404 = 288 static HTML documents.
- 110 Evidence Records, of which 60 are controlled public claims; 55 Evidence Passports.
- 10 Readings; 10 Measurement priorities; 11 governed entry questions.
- 36 governed visual contracts, each with a design tier in `site-src/content/visuals/visual_design_contracts.json`.
- 160 source records, of which 151 expose a public original locator; 27 curated resource cards.
- 24 documented chronology events.
- 435 public search records.

Counts are an inventory, not a measure of evidence strength.

**Public navigation:**
- Primary: Explore · Evidence · Evidence Readings · Data & sources · Method & Measurement (Methodology, Measurement Agenda).
- Trust: About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact.

The navigation is derived from `site-src/content/content/navigation_interaction.json`.

## Reproduce

```bash
python3 scripts/generate_projections.py --check                 # the Master regenerates every projection
python3 -m unittest discover -s scripts/projection/tests -t .    # generator tests
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 scripts/tests/test_public_tools.py                       # browser behaviour tests (Python Playwright + Chromium)
python3 scripts/architecture_diagrams.py --check                 # diagrams show the current navigation and counts
python3 scripts/tests/test_literal_audit_determinism.py          # literal audit identical across PYTHONHASHSEED values
python3 audit/pre_tranche_c/source_lineage_truth_test.py         # source-lineage truth assertions
python3 audit/pre_tranche_c/pre_tranche_c_acceptance.py          # programme acceptance matrix
```

Projections under `site-src/content/` are never edited by hand. Master changes go through
`audit/tranche_b_execution/run_stage.py`, which snapshots, regenerates, rebinds, builds, audits and validates, and rolls
back on any failure.

## Repository map

```text
authority/       sole Production Master + durable constitution + compact current projection
site-src/        controlled projections (content/) and the static behavioural baseline (app.js, styles.css)
scripts/         generator, build, literal audit, validator, rebind, behaviour tests
design/          architecture diagrams, derived from the navigation contract and inventory (aids, not a parallel truth)
handoff/         DRAFT Design → Code recipient package; not executable until promoted
docs/            deployment and repository protocol; the S00–S06 records are historical lineage
audit/           non-authoritative lineage: closures, ledgers, transaction reports, specialist inputs
package.json     local build commands
SHA256SUMS.txt   checksum manifest of this repository state
```

## Semantic firewall

The product must preserve, visually and verbally:

**people ≠ accounts · access ≠ use · infrastructure ≠ outcome · target ≠ result · programme KPI ≠ national prevalence ·
licence/listing ≠ operation · observed ≠ estimated ≠ projected · missing ≠ zero.**

Public experience principle: **UNDERSTAND → EXPLORE → VERIFY**.

## Release boundary

Controlled content and a green validator are not enough to call the product ready for live release. Release also
requires:
- technical, runtime, security and privacy acceptance;
- deployed mobile, RTL and accessibility acceptance;
- publication filtering;
- rights and legal checks where applicable;
- correction and version behaviour;
- named release approval.

## Historical lineage

- The R0–R8 finalization records, the Tranche A/B closures and the S00–S06 documents under `docs/` are kept as lineage
  and are not rewritten.
- `audit/R8_CONTINUATION_MASTER_HANDOVER_TO_NEXT_WINDOW.md` and `audit/FINALIZATION_PROGRAM.md` describe the programme as
  it stood when they were written.
- Current state is always this README, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` and `OPENAI_REENTRY_CHECKPOINT.md`.
