# R8.5 — Canonical repository subtraction (Session F4)

**Date:** 26 September 2026 · **Directive:** D7 §F4 (with D6 §16–25) · **State:** CLOSED / FROZEN
**Transactions:** R85-A (`2a7fd52b…`), R85-B (`440614d7…`) — scripts, inputs, ledgers and run reports in
`audit/final_integration/`. Item-by-item decisions: `audit/R8_5_SUBTRACTION_LEDGER.csv` (21 items).

## Outcome

**One authority → one projection path → one runtime content path → one current start path.**

| Path | Now |
|---|---|
| Authority | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` — the only semantic owner, including every public interface label (04 governed interface copy: 412 labels) |
| Projection | Master → `scripts/generate_projections.py` (contracts: `master_structure.json`, `projection_manifest.json` with 39 outputs, `controlled_inputs/`) → `site-src/content/` |
| Runtime | `site-src/content/` + `site-src/app.js` + `site-src/styles.css` + logo → `scripts/build.py` → `dist/` (288 HTML). No public wording lives in code: `build.py` reads `ui_text`/`ui_fmt`; `app.js` reads the page language's `UI-JS-*` labels from a JSON block the build writes |
| Start | `README.md` → `handoff/README_FIRST.md` → `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` (rewritten in F8) |
| Classification | `FINAL_REPOSITORY_MANIFEST.json` classifies every tracked file (18 classes); `audit/INDEX.md` separates current records, standing policies and history |

## What changed publicly

Only the accepted copy corrections: the 404 page, the corrections page and its empty state, the answer-page disclosure
label, source-trace and data-directory wording, Compare labels, the FMIIP crosswalk title, and six Resource Library
categories in place of sixteen. Every correction keeps the control it expressed (no invented history, boundaries kept,
links are not evidence, no conversion factor). No figure, claim, source binding or Reading changed. Bilingual
invariance stays at 0 differing page pairs.

## Permanent gates (all in `scripts/validate.py` unless stated; none weakened)

| Required by D7 | Gate |
|---|---|
| Authority-hash drift | P4-G04 (README, checkpoint, Context, handoff manifest print only current or recorded-lineage hashes) |
| Projection drift | CI `generate_projections.py --check`; run_stage idempotence |
| Multiple semantic owners | Generator one-owner rules (02 titles from 06/08; Reading sections; closure templates); R85-G01/G02 (no public copy in code; every copy ID exists in 04) |
| Template/authoring tokens | R85-G05 |
| Stale inventory counts | P4-G01 |
| Bilingual invariant drift | RP-G06; CI `bilingual_invariance.py` (exit 1 on any difference); R85-G03 placeholder parity; R85-G04 Unicode NFC |
| Latin month / English currentness in Arabic | R85-G08 (no Latin month name in any Arabic page's `<main>`); S05.1 English-only visual metadata on Arabic Readings |
| Private locator/path leakage | R85-G07 (public build and governed content) |
| Invalid source exposure | S04.1–S04.3 (no source named without a public locator; withheld producers and values) |
| Source-lineage misrepresentation | CI `source_lineage_truth_test.py` (8/8) |
| Nondeterministic literal attribution | CI `test_literal_audit_determinism.py` (eight hash seeds) |
| Stale navigation/counts | P4-G01; navigation-contract alignment at generation |
| Invalid Compare state | Browser suite `test_public_tools.py` (URL state, malformed/unknown links); S04.2 |
| Broken Search probe | P2.2 canonical probe (`scripts/search_canonical_probe.json`) |
| Stale Reading bodies | RP-G05 (retired Reading titles and the retired generic section) |
| Internal codes in public text | R85-G06 |
| Unclassified files / unindexed audit records | R85-G09 (manifest `--check`; every top-level audit file listed in `audit/INDEX.md`) |
| Stale recipient-start status | Added with the R8.6 freeze (F8), when the start documents are final |

## Definition of Done

- one clean root, one Master, one projection path, one current start path — **met** (start documents finalised in F8);
- no ambiguous duplicate current artefact — **met** (duplicate events merged; `(1)` files resolved; history indexed);
- permanent gates pass — **met** (validator PASS 0/0; generator 21/21; literal audit 12,741/0; lineage 8/8;
  determinism; diagrams; invariance 0; browser suites);
- public semantics unchanged except accepted F1/F2/F4 copy corrections — **met**.
