# Design package — Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

Status: **D1 in progress — converged on T4 · Instrument (DL-D1-006); the Design Intent Lock (`01_FOUNDATIONS.md` §4)
and the foundational grammar (§5, `02_TOKENS.json`) are written from the reference implementation, which renders the
stress trio in both languages with every hook and passes the rendered checks (DL-D1-007); the independent final
review's MUST-FIX list is closed and re-verified (DL-D1-008); four escalations open; hand-back verdict on the pull
request.** D0 accepted on `main` at
`8bf19efad7505792ca22e0a3bda1db31fb85d33c`. D1 is developed on `claude/practical-cray-sr26c5` (process note in
`ESCALATIONS.md`) and lands through one draft pull request into `main`
(https://github.com/CausewayGrp/Financial-inclusion-/pull/3). D1 records: `01_FOUNDATIONS.md` (hypotheses,
exploration protocol, benchmark result, process notes, critique; comparison, Lock and grammar when reached), the decision
log below (DL-D1-*), `design/reference/` (the neutral harness and the one content path every renderer uses) and
`design/exploration/d1_canvas/` (the composers that regenerate the canvas propositions). Not PUBLIC RELEASE READY.

## 1. What this package is

The Design package of brief §19: decision log (this file), coverage ledger (`COVERAGE.csv`), design-debt register
(`DESIGN_DEBT.md`), escalations (`ESCALATIONS.md`) and the progressive Design→Code mapping (`09_CODE_HANDOFF.md`).
Files `01`–`08`, `10` and `design/reference/` are created at the gate that first needs them (plan, §6).

**Reference implementation: the stress trio only (D1).** `design/reference/` holds one content path
(`yfie/content.py` reads `site-src/content/**`; never a copied content model, never retyped text), the neutral harness
(`yfie/neutral.py`, unstyled, every brief §19 hook), the accepted renderer of the converged direction
(`yfie/render.py` with `theme.py`, the one stylesheet, and `visuals.py`, the contract drawings) and the checks
(`check_content.py`: parity with `dist/`; `check_trio.py`: the rendered conditions of the viewport suite on the trio
plus the hooks and an interaction smoke test with the baseline runtime). Until `design/reference/out/` renders all
288 documents (D4), this package is an incomplete hand-back by definition (brief §19).

Build and preview: `python3 design/reference/build.py` (renderer `accepted`; `--renderer neutral` for the harness)
writes `design/reference/out/` — the trio in both languages, `assets/yfie.css`, the unchanged fonts and logo, the
baseline runtime, and `out/_bundle/<route>__<lang>.json`, the exact content structures a renderer receives. Check with
`python3 design/reference/check_content.py` and `python3 design/reference/check_trio.py --shots`; preview with
`python3 -m http.server 4173 --directory design/reference/out` (`/en/`, `/ar/`). Baseline: `python3 -m http.server
4173 --directory dist`. Canvas propositions and the reference row: `python3 design/exploration/d1_canvas/build_boards.py`
and `reference_boards.py` regenerate the artboards into the git-ignored `design/exploration/d1_canvas/out/`
(`design/exploration/d1_canvas/README.md`).

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
| D1 | `claude/practical-cray-sr26c5` (planned `design/d1-theses`; process note in `ESCALATIONS.md`) | three theses on the trio (Home, `/evidence/CLM-003/`, `/readings/same-year-different-number/`), EN+AR, 390 & 1440; choose; then tokens, state grammar, shell, type proved at 320/390/640/1440 + keyboard | `01_FOUNDATIONS.md`, `02_TOKENS.json`, decision-log entries; trio rows `VERIFIED` |
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

**D1 additions (not a change to the D0 plan).** The three theses are sharpened in `01_FOUNDATIONS.md` §1 (T3 is called
*Strata* there — the same thesis as *Layers*). A fourth, second-generation proposition, **T4 · Instrument**, was authored
after the designer's own critique of T1–T3 (`01_FOUNDATIONS.md` §2.3) under the owner's design-ceiling review
(DL-D1-005): one mental model — an instrument that answers the reader's questions about the evidence and states what it
cannot answer — with clock-first evidence objects, the seven governed record questions as structure and index, the
boundary as a second voice, a verification spine on every page and a structural firewall; composed mobile-first and
Arabic-first. It is a proposition under the same tests, not a chosen direction and not a hybrid.

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
- **01_FOUNDATIONS.md:** D1's working record — hypotheses, exploration protocol and results, critique, comparison,
  Design Intent Lock and grammar; its status line states what is proven and what is not.

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

### DL-D1-001 · D1 · 2026-09-27 · D1 authority, branch and persistence
- Problem: establish the D1 start state and how D1 work reaches the repository.
- Evidence: `main` = `8bf19efad7505792ca22e0a3bda1db31fb85d33c` (D0 merged); Master `17db032b…038690b`, Page Specs
  `d4574804…824b69aa` and the logo `5830163d…` unchanged and re-verified at gate start (`01_FOUNDATIONS.md` head).
- Alternatives: the planned branch `design/d1-theses`; the branch this execution environment is permitted to push.
- Chosen: develop and push on `claude/practical-cray-sr26c5`; one gate, one pull request into `main`; the steward may
  re-home the branch (`ESCALATIONS.md`, process notes). Milestone commits carry the records; work not pushed does not
  exist for the next session.
- Arabic / responsive / a11y: none.
- Code: none.
- Compromise: none.

### DL-D1-002 · D1 · 2026-09-27 · A neutral harness, not a scaffold with taste
- Problem: theses must be tested on the real governed content, in both languages, at every width, without a scaffold
  that pre-decides type, grid, density or state grammar.
- Evidence: the owner's sequencing refinement (the harness must be deliberately neutral); brief §19 hooks; `dist/` as
  the behavioural baseline.
- Alternatives: extend `site-src/styles.css`; write the first thesis straight into `design/reference/`; a
  presentation-free content path with an unstyled renderer.
- Chosen: `design/reference/yfie/content.py` (one content path from `site-src/content/**`, text never retyped),
  `yfie/neutral.py` (unstyled, every hook) and `check_content.py` (every baseline number appears; a number the reference
  adds must be a governed visual-contract value or identifier) — parity PASS on the trio. Every proposition and every
  future renderer binds through this path.
- Arabic / responsive / a11y: the harness carries `lang`/`dir`, one `h1`, the skip link first, the hooks; it decides
  nothing visual. Harness stress run at 320/390/640/1440 × EN/AR on the trio: no horizontal overflow except the
  unstyled fallback table at 320 px, a presentation matter the propositions handle (`.table-wrap`).
- Code: the content module and the hook set are what Code inherits (`09_CODE_HANDOFF.md`).
- Compromise: none.

### DL-D1-003 · D1 · 2026-09-27 · Claude Design explores before any thesis code
- Problem: a T1 renderer had been written before the canvas held any proposition — a sequencing fault.
- Evidence: the owner's sequencing correction; `01_FOUNDATIONS.md` §2.2.
- Alternatives: keep the T1 renderer as the T1 proposition; discard it; hold it unused.
- Chosen: the T1 renderer is PRE-DESIGN / NON-AUTHORITATIVE, held unused outside the repository and excluded as a source
  (DEBT-003). Claude Design (Design Artifact type; canvas "YFIE D1 Thesis Exploration") authors T1, T2 and T3 as
  artboards first — 36 boards (3 surfaces × EN/AR × 1440/390 px) with the governed text inserted mechanically from the
  harness bundle, the eleven IBM Plex faces and the unmodified logo as canvas assets. Local Chromium twins of the same
  boards give the images for critique and the crops for the screenshot-misuse test. CLAUDE DESIGN INVOKED: YES;
  T1/T2/T3 DESIGN PROPOSITION EXISTS: YES.
- Arabic / responsive / a11y: Arabic composed at the same time as English on every board; 390 px composed for every
  surface.
- Code: none yet; thesis renderers follow critique, they do not precede it.
- Compromise: renders are proof, not authority; the canvas lives outside the repository, so the composers that
  regenerate it are committed (`design/exploration/d1_canvas/`, DEBT-004).

### DL-D1-004 · D1 · 2026-09-27 · Benchmarks NOT INSPECTED; no research detour
- Problem: the benchmark review (§2.1 of `01_FOUNDATIONS.md`) could reach no product site from this environment.
- Evidence: `01_FOUNDATIONS.md` §2.1 — every product site blocked; two source repositories' documentation directly
  observed.
- Alternatives: infer from memory; keep trying other paths; record NOT INSPECTED and proceed on primary evidence.
- Chosen: every interface benchmark is NOT INSPECTED; nothing is attributed to an institution not inspected; principles
  used are marked EXISTING PROFESSIONAL DESIGN PRINCIPLE or YFIE-SPECIFIC DESIGN JUDGMENT; D1's evidence is the governed
  content, the canvas exploration, the rendered stress tests, Arabic, mobile and evidence integrity.
- Code: none.

### DL-D1-005 · D1 · 2026-09-27 · A second-generation proposition (T4 · Instrument) before convergence
- Problem: the owner's design-ceiling review asks whether T1–T3 reach the ceiling — an evidence instrument with a YFIE
  signature, a Home that demonstrates "not one number", portable evidence objects, task-architecture navigation, Arabic
  as a design source, authored type roles, Yemen felt by abstraction — before anything converges.
- Evidence: the designer's own critique of T1–T3 (`01_FOUNDATIONS.md` §2.3): T1's apparatus lifts figures out of their
  governed sentence; T2 reads as a magazine and is weak as a professional object; T3 risks the documentation-portal
  pattern with a faint grounding; a vertical value axis lets the two 2024 markers read as a fall.
- Alternatives: converge on the strongest of T1–T3; a hybrid; a second-generation proposition under the same tests.
- Chosen: author T4 · Instrument as a fourth proposition (`01_FOUNDATIONS.md` §1, T4), mobile-first and Arabic-first,
  and hold convergence until T4 is inspected at native sizes, critiqued through the lenses against the strongest
  first-generation proposition and put through the adversarial tests. No automatic hybrid; T4 is challenged, not
  defended.
- Arabic / responsive / a11y: composed from the Arabic 390 px record outward; desktop is the same system with a spine
  column; numeric axes stay left-to-right in Arabic.
- Code: none; T4 stays a proposition until the Lock.
- Compromise: at this commit T4 is rendered (12 boards, no horizontal overflow at 390 and 1440 px) and on the canvas,
  but not yet inspected at 320/360/430/768/1024/1280 px or at high DPI, not critiqued, not compared
  (`01_FOUNDATIONS.md` §2.5).

### DL-D1-006 · D1 · 2026-09-27 · Convergence: T4 · Instrument is the D1 design direction
- Problem: choose one direction from four propositions without scoring, on rendered evidence, against the convergence
  bar ("what does YFIE now allow a user to understand or do that a conventional evidence website does not make nearly
  as easy?").
- Evidence: nine independent lens reports on the same renders (`01_FOUNDATIONS.md` §3.1–3.2), the native-size
  inspection (§2.5), the adversarial tests (§3.4). Every lens ranked T4 first; the decision rests on two behaviours,
  not the ranking: a same-year restatement that cannot be read or screenshotted as a fall (publication-keyed rows with
  printed values on a zero-based axis), and a number that is never met without its clock and bound (clock-before-claim
  objects; 8.55 % / +11 % kept inside their sentence).
- Alternatives: T1 (rejected: the lifted 8.55 % / +11 % apparatus, the composition a source institution would contest;
  side columns that break at 900–1100 px; Arabic table clipping); T2 (rejected: magazine grammar, bold-number scan path
  with whispering bounds, light Arabic on cream, hidden values, corrupted Arabic link); T3 (rejected: donor-portal
  card idiom, chips before content on every mobile surface, a trail that does not match its strata, CSP-illegal inline
  spans); a hybrid (rejected: the borrowed elements — inline tables, verification chips — are already T4's own contract
  alternative and verification voice, not a second grammar).
- Chosen: T4, with the corrections of §3.3 applied in composer/canvas version 5 (Home paced as figure groups each
  bound to its record; one mark per publication; the not-comparable divider between the lanes; baseline at the index
  origin; raw 2021 levels beside the lanes; alt text and tables visible; index as a numbered hairline list; weight
  discipline; headings for the seven questions; contrast and hit-area fixes; no inline styles). Kept against a
  finding: the value axis stays left-to-right in Arabic (governed contract rule).
- Arabic / responsive / a11y: the Arabic rules (own metrics, no letter-spacing, isolated numeric and ISO-date runs,
  balanced titles, Western digits as in governed copy) and the number rule become MUST PRESERVE in the Lock; verified
  0 page overflow at 320–1440 px; the seven questions and the boundary are `h2`; skip link, focus and labelled in-page
  navigation belong to the reference implementation.
- Code: the reference implementation renders T4 on the trio from the same content path; the Design Intent Lock (§4)
  and `02_TOKENS.json` are extracted only from what that implementation proves.
- Compromise: three escalations open (Arabic credit line; Home pacing marker; IMF lane state question); Yemen material
  grounding unresolved (DEBT-007); interaction, print and citation unproven until the implementation.

### DL-D1-007 · D1 · 2026-09-27 · The reference implementation of the trio; Lock and grammar confirmed from it
- Problem: prove the converged direction in real rendered code, with every hook, in both languages, before any Lock
  is treated as more than intent; extract tokens only from what renders.
- Evidence: `design/reference/yfie/render.py`, `theme.py`, `visuals.py`; `check_trio.py` — 24 renders pass, 12
  interaction smoke tests pass; parity PASS; bilingual invariance 0 differing pairs; degraded states and print
  reviewed; canvas row R (version 6) beside T4 for the drift review; `01_FOUNDATIONS.md` §4.4.
- Alternatives: implement from the canvas boards' HTML (rejected: a canvas is not a content path); write a second
  content model for the renderer (rejected: one path, never a copied model).
- Chosen: the accepted renderer binds the same content module as the harness; the stylesheet was extracted once from
  composer version 5 and is maintained in the reference; every drawing uses percentage coordinates without inline
  style; a page-level actions block keeps cite and report reachable at every width; `02_TOKENS.json` is generated from
  the stylesheet's custom properties with roles; §4 of the Lock is confirmed with no drift (§4.4).
- Arabic / responsive / a11y: verified at 320/390/640/1440 px in both languages; skip link first, visible focus in the
  boundary vocabulary, `h2` questions, reduced motion and forced colours honoured; in-page navigation still unnamed
  (DEBT-006).
- Code: inherits `design/reference/` as it stands (`09_CODE_HANDOFF.md`, state at D1).
- Compromise: the repository browser suites cannot run on a trio-only build (DEBT-009); the 320 px fallback table
  scrolls in its wrapper (DEBT-010); the independent final D1 review is still to come.

### DL-D1-008 · D1 · 2026-09-27 · The independent final review adjudicated; every MUST-FIX closed
- Problem: the repository-only review returned NOT ACCEPTED with eight MUST-FIX items — records that overstated the
  state, a corrupt tokens file, evidence cited at unreproducible paths, and three Lock items the build broke (the Home
  visual's frame, one spine, readable tables at 320 px).
- Evidence: `design/exploration/d1_canvas/review/final_review.md`; `01_FOUNDATIONS.md` §6 and §4.4 (corrections);
  `design/reference/check_trio.py --shots --degraded --evidence design/evidence/d1` (24 renders, 12 pointer and
  keyboard smoke tests, 6 degraded renders — all pass); `check_content.py --text` (numeric and text-block parity PASS);
  `tokens.py --check` current.
- Alternatives: contest the findings; fix only the code; fix code and records and re-verify.
- Chosen: every MUST-FIX and SHOULD-FIX closed in code and records (§6 lists them); two items recorded rather than
  changed (Home section order for steward confirmation; navigation without JavaScript below 900 px reachable through
  the institutional band); the lens reports and the review committed under `design/exploration/d1_canvas/review/`;
  the PNG evidence committed under `design/evidence/d1/`; a second independent pass requested to confirm closure
  before the hand-back verdict.
- Arabic / responsive / a11y: forced colours keep chart text; the record's disclosure content prints; 24 px hit areas
  on in-flow actions; keyboard path verified.
- Code: `09_CODE_HANDOFF.md` rows corrected to the implemented state.
- Compromise: `::details-content` printing is verified in Chromium only; DEBT-006, DEBT-008, DEBT-009, DEBT-010 stay
  open as recorded.
