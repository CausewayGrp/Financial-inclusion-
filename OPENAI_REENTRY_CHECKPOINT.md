# OpenAI re-entry checkpoint — Yemen Financial Inclusion Evidence

**Programme:** Final finite product programme — Tranche C → R8.5 → R8.6.
**Position (current):** OpenAI accepted the Tranche C checkpoint on 26 September 2026 (recipient verification 31/31) and
supplied the independent ten-Reading package with directive D7 (`audit/directives/`). Session F2 integrated the Reading
portfolio Master-first (transaction RP-F2; `audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`). Sessions F3–F9 follow.

**Status: READING PORTFOLIO INTEGRATED — TRANCHE C ACCEPTANCE PRESERVED.** The sections below record the Tranche C
checkpoint as reviewed; the authority hashes in §1 are current.

- R8.4: CLOSED / PASS, Reading prose included (F2; BIL-05 closed: bilingual invariance 0).
- R8.5 (subtraction and recipient cleanup) and R8.6 (clean-room Design handoff) have **not** been started.
- This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY.
- The design and implementation prompts in `handoff/` remain **DRAFT — DO NOT EXECUTE YET** until R8.6.

**Date:** 2026-09-26.

## 1. Authority state (verify first)

| Item | Value |
|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` — SHA-256 `caabff47f4ff9b036943b72f775260197a59dbc3e00cdc4b629bed65f5b4bfc6` |
| Page Specs | `site-src/content/page_specs.json` — SHA-256 `f7edca09185b89378a946c1195c37d6e99d35b2689df7f0ff646c74aeb550e0f` |
| Entry state recorded with the Drive IDs (lineage, not current) | Master `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7`; Page Specs `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` |
| Tranche C entry (P5 close, lineage) | Master `397b3307…` |
| Canonical repository | GitHub `CausewayGrp/Financial-inclusion-`, branch `main`. The state reviewed here is the signed tag `checkpoint/tranche-c-complete-reading-hold`, whose tree is byte-identical to the review ZIP; later commits on `main` add repository infrastructure and documentation only |
| External (Drive) copies | `EXTERNAL_REPOSITORY_SYNC_PENDING` — the Drive files were not replaced; they are lineage, not working copies |
| Generator | `scripts/generate_projections.py`; `PROJECTION CHECK PASS` |
| Generator tests | 21 of 21 |
| Build | 288 HTML documents from 143 Page Specs (286 localized + root + 404) |
| Public-literal audit | 12,720 records, 0 unresolved; identical bytes under 8 `PYTHONHASHSEED` values |
| Source-lineage truth test | 8 of 8 |
| Validator | `WEBSITE REPOSITORY VALIDATION PASS`, 0 errors, 0 warnings (gates through TC-G05) |
| Architecture diagrams | current |
| Browser behaviour tests | `scripts/tests/test_public_tools.py` — 25 passed, 1 not applicable to the current data |
| Viewport acceptance | `audit/tranche_c/checks/viewport_acceptance.py` — 168 of 168 |
| Bilingual numeric invariance | `audit/tranche_c/checks/bilingual_invariance.py` — 6 page pairs differ, all from the three held Reading-prose items (BIL-05) |
| Current counts | `site-src/content/content/public_inventory.json` (derived from the Master; the only source for counts) |

The Master and Page Specs hashes in this file, `README.md`, `authority/AUTHORITY.json`, the Context and the handoff
manifest are rebound by `scripts/rebind_authority.py`; validator gate P4-G04 fails if any of them diverges.

## 2. What Tranche C did

Ten Master transactions, each committed through `audit/tranche_b_execution/run_stage.py` (regenerate, rebind, build,
literal audit, diagrams, validate, generator check; rollback on any failure):

- **TC-S1** one owner per text; **TC-A** evidence-record truth and visual re-tiers; **TC-B** source library display;
  **TC-C** English and Arabic editorial acceptance; **TC-D** data tables; **TC-E** visual contracts; **TC-F** governed
  copy for generator and runtime fixes; **TC-G** residual bindings; **TC-H** 28 page-section pairs brought to bilingual
  parity; **TC-I** chronology dates in both languages, the /payments/ Arabic title and residual record/visual parity.
- 224 panel findings plus 5 bilingual-invariance findings, each with one disposition. All 9 BLOCKERs are closed.
- Currentness cut-off 26 September 2026.

Details: `audit/TRANCHE_C_FINAL_ACCEPTANCE.md`. Ledger: `audit/TRANCHE_C_FINDINGS_LEDGER.csv`. Currentness:
`audit/FINAL_CURRENTNESS_CUTOFF.md`. Per-transaction ledgers and run reports: `audit/tranche_c/runs/`.

## 3. Reading package hold

The Reading sections aligned in TC-H stay as committed; the incoming Reading package supersedes them where it rewrites
them. Three parity items are passed to it (ledger BIL-05): the Arabic thesis of *Reforms newer than people evidence*
(fieldwork months missing), the English question of *Finance constraint, different questions* (2022 seven-governorate
frame missing), and the Arabic of RV-CWR-001/002. The package must enter Master-first through the runner and leave the
invariance check at zero differing pairs.

## 4. Open items carried forward (not defects of this checkpoint)

- **R8.5 (not started):**
  - runtime duplicates REF-PAY-006/010 and REF-PAY-007/013;
  - duplicate `(1)` audit files in `audit/`;
  - public copy still held in `scripts/build.py` and `site-src/app.js` (AR-29, EN-09, TRUST-25);
  - template currentness sentences and analytics-sheet labels (P3-D02);
  - `FINAL_REPOSITORY_MANIFEST.json`, `audit/INDEX.md`, and the permanent gates, including a bilingual-parity gate
    built on `audit/tranche_c/checks/bilingual_invariance.py`.
- **Release-only dependencies:** TOOL-02 (logo asset pipeline for the 10 MB master PNG; never redrawn here), TOOL-25
  (nav-group presentation, Design-owned), TRUST-09 (CauseWay identity and funding statement needs owner input).
- **Known evidence frontiers:** CLM-044 value withheld (no public locator or rights assessment); the ~147-firm base
  implied by the 91.84% table; the CBY-Aden↔IMF remittance level crosswalk; the causes of the gender gap; reconciled
  current operating-provider status; the magnitude of the 2022 banking restatement (EVM-18, VER-23).

## 5. Re-run

```
python3 scripts/generate_projections.py --check
python3 -m unittest discover -s scripts/projection/tests -t .
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 scripts/tests/test_literal_audit_determinism.py
python3 audit/pre_tranche_c/source_lineage_truth_test.py
python3 scripts/tests/test_public_tools.py                 # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/viewport_acceptance.py       # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/bilingual_invariance.py
python3 scripts/architecture_diagrams.py --check
sha256sum -c SHA256SUMS.txt
```

## 6. Boundaries kept

- One authority. Every content change went into the Master first through the runner. No projection was edited by hand.
- Nothing completed earlier in the programme was reopened; Reading prose was not final-frozen.
- **Not claimed:** native Arabic certification, legal review, WCAG conformance, rights clearance, security guarantees,
  service levels.
- No external repository was changed.
