# Tranche C — whole-product adversarial acceptance

**Date:** 26 September 2026 · **Lead:** Product Lead / Evidence Integrator (Claude)
**Status:** **TRANCHE C COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE.**
Not DESIGN HANDOFF READY. Not PUBLIC RELEASE READY. R8.5 and R8.6 not started.

## 1. Authority at close

| Item | Value |
|---|---|
| Production Master | SHA-256 `f0150122895d88169e9c9ec947633deda04a02c710a28d7b0de2972214547224` |
| Page Specs | SHA-256 `bd010a2053898a971944ba63ab3276aeb455428069813097dbc8a07037c88295` |
| Master at Tranche C entry | `397b330757de…` (P5 close) |
| Build | 288 HTML documents from 143 Page Specs |
| Public-literal audit | 12,720 records, 0 unresolved; identical bytes under 8 hash seeds |
| Counts (derived, `public_inventory.json`) | 110 Evidence Records · 60 public claims · 55 passports · 10 Readings · 10 Measurement priorities · 11 entry questions · 36 visual contracts · 160 sources (151 public locators) · 27 curated resources · 24 chronology events · 435 search records |

## 2. Transactions (Master first, all through `audit/tranche_b_execution/run_stage.py`)

Each row was committed by the transactional runner. The runner regenerates the projections, rebinds, builds, runs the
literal audit and diagrams, validates and runs the generator check, and rolls back on any failure. Ledgers and run
reports are in `audit/tranche_c/runs/`.

| Tx | Master in → out | Cells | Scope |
|---|---|---|---|
| TC-S1 | `397b3307` → `821bf031` | 1,204 | One owner per text: 06 owns record text, 08 owns Reading titles; 02/03/07 derived |
| TC-A | `821bf031` → `b7ee2b73` | 1,718 | Evidence-record truth (06/11), women's figure on CLM-002, FCS comparators, visual re-tiers |
| TC-B | `b7ee2b73` → `3081745b` | 1,007 | Source library: publisher/date/title display, locator fixes, de-duplication |
| TC-C | `3081745b` → `00c0170a` | 567 | English and Arabic editorial acceptance (03/08/10/14/04/05) |
| TC-D | `00c0170a` → `73c84b8e` | 29 | Data tables: unsourced Findex history block removed, provider/passport fixes |
| TC-E | `73c84b8e` → `1b370e06` | 34 | Visual contracts: FMIIP ladder, microfinance divergence as a table, labels |
| TC-F | `1b370e06` → `df36c54c` | 32 | Governed copy for the generator/runtime fixes (citations, crumbs, chronology, search aliases) |
| TC-G | `df36c54c` → `4efc816f` | 12 | Residual: Saudi-support bindings, POS release-form note |
| TC-H | `4efc816f` → `97c93a9e` | 33 | Bilingual parity of 28 page-section pairs (BIL-01) |
| TC-I | `97c93a9e` → `f0150122` | 50 | Chronology period in both languages (BIL-02), /payments/ Arabic title, residual record/visual parity |

Code changes outside the Master: `scripts/build.py`, `site-src/app.js`, `site-src/styles.css`,
`scripts/projection/derived.py`, `families.py`, `scripts/validate.py` (gates TC-G01..G05), the unit tests, and
`scripts/literal_audit_allowances.json` (one Arabic entry for the Compare "2 to 4 records" constant).

## 3. Hostile-fair panel

Nine lenses (AR, EN, EVM, JRN, PAY, TOOL, TRUST, VER, VIS) raised 224 findings: 8 BLOCKER, 166 MATERIAL, 50 EDITORIAL.
The bilingual-invariance test added five (BIL-01…05), one of them BLOCKER-class. Every finding has one disposition in
`audit/TRANCHE_C_FINDINGS_LEDGER.csv`:

| Disposition | Findings |
|---|---|
| FIX | 212 |
| NARROW | 8 |
| EXPLICIT EVIDENCE FRONTIER | 2 (EVM-18, VER-23: banking restatement magnitude) |
| RELEASE-ONLY DEPENDENCY | 3 (TOOL-02 logo asset pipeline; TOOL-25 nav-group presentation, Design-owned; TRUST-09 CauseWay identity and funding statement, needs owner input) |
| FIX — SCHEDULED R8.5 | 3 (AR-29, EN-09, TRUST-25: public copy still held in `build.py`/`app.js`) |
| HELD FOR READING PACKAGE | 1 (BIL-05) |
| REJECT FINDING | 0 |

All nine BLOCKERs are closed:

| ID | Defect | Fix |
|---|---|---|
| EN-01 | Microfinance Reading carried a stale title with an unsupported premise | TC-S1: one title owner (08) |
| TRUST-01 | Sources shown as internal codes although the Data page promised publisher and date | TC-B + generator: display titles, publisher, date |
| EVM-01 | Women's account-ownership figure not quotable from any record | TC-A: CLM-002 carries both sex values |
| JRN-01 | Derived results not reproducible although reproduction was promised | TC-A/TC-D: promise narrowed; frontier stated |
| VER-01 | Unsourced "uploaded 2014–2022" Findex block contradicted verified values | TC-D: removed |
| VIS-01 | FMIIP components shown as "implementation reached" | TC-A/TC-E: ladder stops at the evidenced stage |
| VIS-03 | Microfinance divergence drawn as a trend the evidence denies | TC-A/TC-E: re-tiered to TABLE_TEXT_FIRST |
| TOOL-01 | Compare could only ever return "not a direct comparison" | TC-A/TC-F: required fields are definition, universe, method |
| BIL-02 | Arabic chronology printed English dates | TC-I: `period_en`/`period_ar`; build renders the page language |

Lead frontiers kept explicit rather than filled: the CLM-044 residual-model value stays withheld (no public locator or
rights assessment); the ~147-firm base implied by the 91.84% table (EVM-07); the CBY-Aden↔IMF remittance level
crosswalk; the causes of the gender gap; reconciled current operating-provider status.

## 4. Tests and results at close

| Test | Result |
|---|---|
| Validator (`scripts/validate.py`, incl. TC-G01..G05) | PASS, 0 errors, 0 warnings |
| Generator idempotence (`generate_projections.py --check`) | PASS |
| Generator unit tests | 21/21 |
| Literal-audit determinism (8 seeds) | PASS |
| Source-lineage truth test | 8/8 |
| Architecture diagrams | current |
| Public-tool browser suite (Search, Compare, copy, menu, skip link, live regions) | 25 pass, 1 not applicable to current data |
| Viewport acceptance (21 pages × EN/AR × 320/400/640/1440: overflow, one h1, skip link first, `dir`, alt) | 168/168 |
| Bilingual numeric invariance (`audit/tranche_c/checks/bilingual_invariance.py`) | 6 page pairs differ; all six come from the three Reading-prose items held in BIL-05. Before TC-H/TC-I: 28 section pairs and 26 pages |
| Arabic-page Latin-script scan | Only proper names, source titles and identifiers remain; chronology dates fixed (BIL-02) |
| Backend/AI-trace scan | No repository vocabulary, authoring tokens or internal IDs in public prose outside citation identifiers |

Coverage by the test families required by the programme: detached-use and weaponisation tests (EVM, VER and VIS lenses;
e.g. the Arabic sentence that printed "91.84% of all Yemeni firms" in negated form was removed in TC-H); source and
verification cold test across partial and composite records and all 10 Readings (VER lens); Arabic and English
editorial acceptance, each edition read on its own (AR, EN lenses, TC-C, then TC-H/TC-I for parity); About,
Methodology and Trust (TRUST lens; no unverified promise remains; TRUST-09 carried); 11 hard user journeys (JRN lens,
22 findings); public tools at four widths (TOOL lens and the viewport suite). The 200% zoom, reduced-motion and
image-off checks were done by inspection in the TOOL lens, not by an automated suite. No WCAG conformance is claimed.
Visual acceptance of every SIGNATURE and CORE visual: VIS lens (21 findings), TC-A/TC-E.

## 5. Currentness

Cut-off 26 September 2026. Dispositions in `audit/FINAL_CURRENTNESS_CUTOFF.md`.

## 6. Reading package hold (Lead decision, 26 September 2026)

An independent final Reading package is being closed elsewhere. Reading prose is therefore not final-frozen here, and
nothing already done in Tranche C is reopened. The Reading sections aligned in TC-H stay as committed; the incoming
package supersedes them wherever it rewrites them. Three parity items are passed to that package (BIL-05):

1. 08 thesis of *Reforms newer than people evidence*: the Arabic lacks "November 2022 to January 2023".
2. 08 question of *Finance constraint, different questions*: the English lacks the Arabic's "2022 seven-governorate survey" frame.
3. 11 RV-CWR-001/002 Arabic text: "the same year" and a generic paraphrase where the English names 2024 and "2022 banking positions".

When the package arrives it must enter Master-first through the runner and then pass the invariance check with zero
differing pairs.

## 7. Programme state

| Stage | State |
|---|---|
| R8.4 (Tranche C) | CLOSED / PASS for every non-Reading surface; Reading prose HELD for the independent Reading package |
| R8.5 subtraction and recipient cleanup | NOT STARTED. Carries REF-PAY-006/010 and 007/013, the duplicate `(1)` audit files, public copy in code (AR-29/EN-09/TRUST-25), currentness boilerplate, P3-D02, the manifest, the index and the permanent gates (including a bilingual-parity gate) |
| R8.6 clean-room Design handoff | NOT STARTED. `handoff/` prompts remain DRAFT — DO NOT EXECUTE |

## 8. Not claimed

Native Arabic certification, legal review, WCAG conformance, rights clearance, security guarantees and service levels
are not claimed. External (Drive) copies were not changed (`EXTERNAL_REPOSITORY_SYNC_PENDING`).
