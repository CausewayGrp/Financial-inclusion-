# Design package — Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

Status: **D0 Orientation — records opened, landed by the steward (`7c9b8a1`) and directly verified.** No design thesis chosen, no screen
designed, no design system published. Not PUBLIC RELEASE READY.

## 1. What this package is

The Design package of brief §19: decision log (this file), coverage ledger (`COVERAGE.csv`), design-debt register
(`DESIGN_DEBT.md`), escalations (`ESCALATIONS.md`) and the progressive Design→Code mapping (`09_CODE_HANDOFF.md`).
Files `01`–`08`, `10` and `design/reference/` are created at the gate that first needs them (plan, §6).

**Reference implementation: does not exist yet.** At D0 the design package has no runnable site. Until
`design/reference/out/` renders all 288 documents, this package is an incomplete hand-back by definition (brief §19).

Build and preview (to be filled at D1 when the reference stack is chosen): one command writing `design/reference/out/`,
previewed with `python3 -m http.server 4173 --directory design/reference/out`. Baseline meanwhile:
`python3 -m http.server 4173 --directory dist`.

## 2. Authority used

| Item | Value | How verified at D0 |
|---|---|---|
| Repository / branch | `CausewayGrp/Financial-inclusion-` · `main` | read via GitHub |
| Accepted commit | `6d954c177b5d35cdad063f3a2cef5a92d33e16d4` | `main` compared to this SHA on 2026-09-27T05:47Z: no changes |
| Tag `checkpoint/design-handoff-ready` | **not found** (404) at D0 | commit SHA used instead |
| README_FIRST first line | "STATUS: **DESIGN HANDOFF READY.**" | read |
| Production Master SHA-256 | `17db032b…038690b` — matches brief | recorded in `SHA256SUMS.txt`, inventory `generated_from`; **file not hashed directly** (binary could not be fetched into the Design environment) |
| Page Specs SHA-256 | `d4574804…824b69aa` — matches brief | recorded in `SHA256SUMS.txt`, inventory `generated_from`; **file not hashed directly** (file too large for the Design environment's fetch) |
| Inventory, Implementation Manifest | byte hashes computed = `SHA256SUMS.txt` entries | direct SHA-256 in Design environment |

No fingerprint mismatch was found. Direct verification of the two authority hashes and the §8 command suite is left to
the steward (see §7, "Environment").

**Steward verification (2026-09-27, `design/d0-orientation` at `7c9b8a1`, re-run on `main` at the same commit).** The
steward hashed the files directly: Production Master
`17db032b15da16fc4b5b3c3b49f19aebf2ecb4ec46634613fe8505d0f038690b`, Page Specs
`d45748046ea56fd0e67fdf112f9888de65b3fe7fab46ce6f51de3a80824b69aa` — both match the brief. Every `CONTRIBUTING.md` §5
gate was run and passed, the two browser suites included; the evidence is in DEBT-001 (`DESIGN_DEBT.md`, CLOSED). The
Design-environment statements in this table and in §7 are kept as the record of what D0 itself could verify.

## 3. Supplied visual board, colour board or homepage mockup

**None has been supplied in this repository.** `design/` held only `design/architecture/` (programme diagrams:
site map, page-family/state map, full-stack architecture, Design-to-Code flow) — these are structural programme
records, not visual direction. `handoff/DESIGN_STARTING_TOKENS.json` is a stated hypothesis, not a constraint.
`site-src/styles.css` and `dist/` are a behavioural baseline, not an aesthetic authority. Nothing outside the
repository (earlier conversations, ZIPs, Drive copies, screenshots, mockups) is treated as binding.

Binding identity constraints only: canonical logo `site-src/assets/CauseWay_Master_Logo.png` (SHA-256 `5830163d…`,
unaltered, with clear space; never filtered — EAD-04) and the IBM Plex family, self-hosted from `vendor/fonts/`.

## 4. Dependency map (from `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json`, schema 1.3)

Counts (inventory `counts`): 143 Page Specs → 286 edition pages + neutral root + bilingual 404 = 288 documents;
110 Evidence Records; 10 Readings; 10 Measurement priorities; 11 entry questions; 160 sources (151 with public locator);
28 curated resources; 36 visual contracts; 24 chronology events; 435 search records.

| Family | Routes | Governed inputs | Components (to be designed) | States carried |
|---|---|---|---|---|
| Orientation | 1 (`/`) | Page Spec; `collection.starting_question_ids` (QE-002/003/005/011); 1 Featured Reading; section 3 + its 3 records | identity, question entry list, snapshot-as-authored, featured Reading, `#system` visual anchor | none extracted; no figure strip, no state badge (§4.4) |
| Question Entry | 1 | 11 questions in 4 clusters (`UI-QUESTIONS-*`); 1 "Go deeper" | question cluster, question → answer link | — |
| Domain Answer | 8 | Page Spec sections; 1–5 bound visuals (≤1 first screen); ≤2 Readings; first N Measurement cards (`measurement_limit`) | answer block (ANSWER→SCOPE→BOUNDARY→VERIFY), evidence clock, boundary, visual frame, Measurement card, Reading link | dense_domain `/people/`, sparse_unknown `/access/`, institutional_sequence `/payments/`→`/reforms/`, vintage_conflict `/remittances/`, mobile_rtl `/ar/payments/` |
| Evidence Directory | 1 | 110 records; embedded search (`global-search`) | workbench row, search, add-to-Compare (13 comparable only) | search no-match / failed index |
| Evidence Record | 110 | record fields; lineage; verification state; Readings that use it; sources | record header, figure-with-scope, establishes / does not establish, limits, source list, cite, report, Compare entry (13) | 9 verification states (§5 below) |
| Comparison | 1 | 13 comparable records; 6 dimensions (`yfie-compare-dimensions`); verdict set `UI-JS-COMPARE-*` | slot selectors (`<select>`), compatibility-first table, boundary row, verdict | compare_unlike; 5 technical input states |
| Reading Index | 1 | 10 Readings | analytical index entry | — |
| Reading | 10 | `readings.json`, `reading_sections.json`, Page Spec | standfirst, essay, ≤1 signature visual, "What not to conclude", "What would change this reading?", trace, related | reading_longform; RV tiers |
| Data & Source | 1 | 151 displayed sources; 28 curated resources by `resource_category`; chronology | source register, curated card, `?source=` focus, filter, chronology | source_scale; source_link_unknown; filter no-match; 9 without document type; 9 without public locator (never named) |
| Measurement | 1 | 10 priorities `#MA-00x` | priority object (decision constrained / known / unknown / measurement that would change it) | measurement_nonranking |
| Reference / Trust | 8 | Page Specs | trust prose, correction/report journey, contact mail composition | trust_plain_language; record_context_* states |

Visual tiers: SIGNATURE 3 (RV-CWR-001, RV-CWR-009, VIS-PROVIDER-OBSERVABILITY) · CORE_ANALYTICAL 9 · SUPPORTING 12
(no plotted values) · TABLE_TEXT_FIRST 11 (never a chart) · RETIRE_FROM_DESIGN 1 (VIS-CAPITAL-CONTEXT).

Verification states and records: SOURCES_LISTED 90 · SOME_WITHOUT_PUBLIC_LOCATOR 2 (CLM-045, DS-QUAL-EVIDENCE) ·
PARTIALLY_RESOLVED 3 (CLM-039, CLM-046, CLM-056) · COMPOSITE_OF_OBJECTS 4 (CLM-031, DS-FINDEX-HISTORY-CROSSWALK,
VIS-DEMAND-VINTAGE-LADDER, VIS-PROVIDER-TIME) · COMPOSITE_MEMBERS_NOT_LISTED 9 (CLM-014, DS-DEMAND-VINTAGE-LENS, seven
VIS-) · FRAMING_NO_FACT 1 (CLM-004) · ORIGINAL_NOT_PUBLIC 1 (CLM-044, withheld) · SOURCE_NOT_YET_BOUND 0 ·
NO_SOURCE_RECORD 0 (component states only, never on an invented record).

Technical states: 15 (inventory `technical_states`). Journeys: 13 (J01–J13).

Test hooks Code inherits (brief §19) are frozen from D1 on and will be tracked in `09_CODE_HANDOFF.md`.

## 5. D0 comprehension summary (durable)

**Product.** A bilingual, co-authoritative public evidence service that moves a reader from a question to the strongest
defensible answer, its scope, its boundary and a one-step verification path, without deciding anything for anyone. Its
difference: it treats non-comparability as the finding. Yemen's evidence runs on different clocks, populations,
methods and institutions; the product's job is to keep those differences visible and navigable instead of resolving them
into a dashboard.

**Immutable.** Every fact, figure, controlled word, binding, evidence/lineage/verification/rights/publication state,
route set and purpose, required behaviours and test hooks, Arabic–English equality, visual semantics and prohibited
inferences, logo, IBM Plex, citation and source behaviour, the ban on internal language in public.

**Free.** Composition, grid, hierarchy, density, type within Plex, palette (no approved palette exists), component form,
state grammar (within §5), chart form where contracts allow, navigation behaviour (EAD-05), disclosure, motion, Arabic
spatial composition, presentation of search/sources/citation/report, the Methodology and Measurement experiences,
print and export interaction.

**Most dangerous semantic mistakes Design could create.**
1. A shared axis, row, colour or alignment making unlike figures read as one series (people vs accounts; CBY-Aden vs IMF
   remittance levels — FRN-03).
2. Infrastructure growth (POS terminals, CLM-003) visually implying use or outcome.
3. A regulation-to-outcome chain drawn as a flow that implies operation or effect (VIS-PAYMENT-RAILS, `/reforms/`).
4. Measurement P0/P1 styled as a ranking or national priority.
5. Unknown geography on `/access/` rendered as an empty map (= zero).
6. A framing record (CLM-004), thin record (CLM-015) or composite-without-members styled as weak, missing or errored.
7. Progressive disclosure hiding a boundary that changes the headline meaning; a screenshot crop losing period,
   population or "What not to conclude".
8. A withheld value (CLM-044) leaking via chart scale, table cell, export, alt text or tooltip.
9. Chronology laid out as a causal chain; vintages visually "reconciled"; fading by age.
10. Technical states looking like evidence gaps and vice versa; restricted downloads looking like errors.
11. Arabic: right-pointing arrows between numbers, un-isolated IDs/percent signs, mirrored numeric time axes.

**Hardest routes and outliers.** `/evidence/CLM-003/` (raw totals vs the source's own percentage, discrepancy visible);
`/readings/same-year-different-number/` (RV-CWR-001, two panels, same-year revision, not-comparable); `/remittances/`
(REPORTED/ESTIMATED/PROJECTED + BREAK_VINTAGE, and its MA-001 card about households kept apart from the macro
series); `/payments/` (5 visuals incl. WITHHELD, DISAGREEMENT, NOMINAL) and `/ar/payments/` at 320 px; `/access/`
(sparse); `/evidence/compare/` (4 columns on mobile — EAD-06); `/data/` (151 sources without a link wall);
`/readings/after-transfer-persistence/` (longest); `/readings/banking-jump-measurement-basis/` (SUPPORTING visual,
no values); CLM-044, CLM-014, CLM-031, CLM-039, CLM-004, CLM-015, CLM-037; `MF-ORIG-001+002` (a `+` in a route/ID
to isolate in RTL and URLs); 15 routes whose Page Spec sections are split by language.

## 6. Plan D1–D7

| Gate | Branch | Scope | Exit evidence |
|---|---|---|---|
| D0 | `design/d0-orientation` | these records | records committed; plan names theses; escalations listed |
| D1 | `design/d1-theses` | three theses on the trio (Home, `/evidence/CLM-003/`, `/readings/same-year-different-number/`), EN+AR, 390 & 1440; choose; then tokens, state grammar, shell, type proved at 320/390/640/1440 + keyboard | `01_FOUNDATIONS.md`, `02_TOKENS.json`, decision-log entries; trio rows `VERIFIED` |
| D2 | `design/d2-hard-families` | Explore, 5 hard domains, Evidence index, §9.1 record set, Compare, `/data/` | each §9.2 case proved |
| D3 | `design/d3-synthesis` | Readings index + all Readings, Measurement, Methodology, trust, report journey, 404; Home cold-reader test | same; cold-reader record |
| D4 | `design/d4-binding` | all 288 documents via family rules | three suites pass on `design/reference/out/`; all rows ≥ `BUILT` |
| D5 | `design/d5-interaction-a11y` | every tool state and journey, keyboard, zoom, reduced motion, forced colours | `07_INTERACTION_ACCESSIBILITY.md` |
| D6 | `design/d6-visuals-social-print` | visuals per contract, frames, social templates, print | contract-by-contract evidence |
| D7 | `design/d7-acceptance` | last-10-percent audit, final handoff | checklist complete; Code recipient test |

**D1 theses to be tested** (named only — not designed; each must answer type, grid, density, evidence-state grammar and
Arabic composition differently, not as colour variants):

- **T1 · Register.** The evidence record as the organising object: a strict typographic ledger with an inline-start
  margin column that carries each figure's clock, population and state as marginalia; high, controlled density; Plex
  Sans + Plex Mono for IDs/values; Arabic composed with its margin on the reading-start side and its own ledger rhythm.
- **T2 · Argument.** Editorial reading-first: one measured text column; ANSWER / SCOPE / BOUNDARY / VERIFY as distinct
  typographic registers inside the prose; evidence objects expand in place; minimal chrome; low simultaneous load;
  Arabic with independent line length and heading scale.
- **T3 · Layers.** The system made spatial: every consequential page as ordered strata (answer → scope → boundary →
  source) with a persistent, relevance-limited evidence trail; state grammar carried by structure and pattern rather
  than type alone; Arabic strata order and trail placement composed natively.

Selection criteria: `DESIGN_ACCEPTANCE_CRITERIA.md`, the four review tests (§7), hard states carried by the trio, the
audience lenses, Code build cost. Nothing propagates before D1 exits.

## 7. Environment and persistence (D0 statement)

| Capability | Status in the Claude Design environment |
|---|---|
| Read the repository | YES (GitHub read) |
| Write repository files | NO — files are written to the Design project workspace only |
| Create branch `design/d0-orientation` | NO |
| Commit | NO |
| Push | NO |
| Open / update gate PR | NO |
| Run §8 commands (Python, Playwright, Chromium) | NO — every command **NOT RUN** (no shell / Python runtime) |
| Regenerate `FINAL_REPOSITORY_MANIFEST.json`, `SHA256SUMS.txt` | NO — NOT RUN |
| Produce a git bundle / patch series | NO (no git) |

Governed fallback used: the D0 files are delivered as a file set (`design/00_DESIGN_README.md`, `design/COVERAGE.csv`,
`design/DESIGN_DEBT.md`, `design/ESCALATIONS.md`, `design/09_CODE_HANDOFF.md`) for the steward to land on
`design/d0-orientation` with base `6d954c1`, regenerate the manifest and checksums, run the §8 suite and open the D0 PR.
**Nothing is persisted in the repository until the steward lands it.** The reference implementation from D1 onward will
need the same route unless a write-capable environment (e.g. Claude Code acting on these instructions) lands each gate.

§8 commands, all NOT RUN at D0 (reason: no shell): `checksums.py --check`, `generate_projections.py --check`,
`build.py`, `audit_public_literals.py`, `validate.py`, `tests/test_public_tools.py`,
`tranche_c/checks/viewport_acceptance.py`, `tranche_c/checks/bilingual_invariance.py`.

## 8. How the records are used

- **Decision log (§9 below):** one dated entry per material decision, fields of brief §19. Re-read at every gate start.
- **COVERAGE.csv:** seeded at D0 — 1 389 rows, all `NOT_STARTED`: 143 routes × EN/AR × 320/390/640/1440, neutral root,
  bilingual 404 × 4 widths, 12 hard-state cases, 9 verification states, 20 grammar states, 36 visual contracts,
  15 technical states, 13 journeys × mobile/desktop, each × 2 languages. `gate` = planned gate. A row advances only with
  evidence in the `evidence` column; a family template applied is not `REVIEWED`.
- **DESIGN_DEBT.md:** every temporary compromise, closed not deleted, with its D7/release blocking flag.
- **ESCALATIONS.md:** `ESCALATE_TO_MASTER` / `NEEDS_CONTROLLED_CONTENT` only; the unshipped feature is designed and
  listed, never filled with authored copy.
- **09_CODE_HANDOFF.md:** updated at each gate end, never back-filled at D7.

**D7 Definition of Done (interpretation).** A runnable, fully populated bilingual reference site in
`design/reference/out/` — all 288 documents, every tool and state, both languages, four widths, no placeholder, every
label governed or its feature unshipped — passing the three browser/invariance suites and all repository gates; every
acceptance line in `10_ACCEPTANCE_CHECKLIST.md` evidenced; every ledger row `ACCEPTED` or its gap explained; no open
debt flagged "blocks D7"; `09_CODE_HANDOFF.md` final; and the Code recipient test passing on the commit alone. It is
not public release (REL-01…04 remain).

## 9. Decision log

### DL-D0-001 · D0 · 2026-09-27 · Authority baseline and persistence route
- Problem: establish the working authority and how Design work reaches the repository.
- Evidence: README_FIRST §3, §9; brief §2, §21; `main` = `6d954c1` (compare, no changes); tag absent.
- Alternatives: wait for the tag; work from `main` HEAD; work from the accepted SHA.
- Chosen: the accepted SHA `6d954c1` (identical to `main` at D0). Persistence via the brief §21 fallback (file set for
  steward landing) because this environment cannot write, commit or push.
- Arabic / responsive / a11y: none.
- Code: none.
- Compromise: authority hashes verified indirectly; §8 suite NOT RUN → DEBT-001.
- Steward, 2026-09-27: DEBT-001 closed — hashes verified directly and the §8 suite run green (§2).

### DL-D0-002 · D0 · 2026-09-27 · No binding visual reference
- Problem: what visual direction binds D1.
- Evidence: repository contents (§3 above).
- Chosen: none binds beyond logo and IBM Plex; starting tokens and baseline styles are hypotheses to challenge.
- Code: none.

### DL-D0-003 · D0 · 2026-09-27 · Three D1 theses named; ledger gates assigned
- Problem: D1 must test materially different theses; ledger needs planned gates.
- Chosen: T1 Register, T2 Argument, T3 Layers (§6); gate per route as in §6 / `COVERAGE.csv`.
- Code: none until D1 selection.
