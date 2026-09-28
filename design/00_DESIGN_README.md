# Design package — Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

Status: **D6 met on `claude/bold-maxwell-r3o015` (draft pull request #5, pending the owner's merge) — the visual system,
the portable frames and the print system proved on the final tree in both languages: every one of the 36 visual
contracts stands in its tier's form on every route that binds it (`design/reference/check_visuals.py`: 36 contracts ×
EN/AR, 2,856 contract assertions; 52 forced-colours and print checks on the thirteen drawn contracts; 26 export frames;
286 social frames; 133 print checks on the eleven family routes × EN/AR; 598 documents and frames scanned for a date or
range outside an isolate; 0 failures), and every D1–D5 check passes on the same tree (the D4 gate caught one D6
regression, fixed). The last accepted gate is D5: D2 was met at `9c263ac`, D3 at `beecdbb`, D4 at `aee1e1b` and D5 at
`8be8e22`; the four gates were accepted together by the owner's merge of pull request #4 (`main` at
`2effd8be9a481fed2881da61e8111bf16cceb814`, Verify green on the merge). D7 has not begun (process note in
`ESCALATIONS.md`).** D1 was accepted by the owner's merge (`main` at `851f496078776356b38892c946d40d154c819067`, pull
request #3). D2–D5 were developed on `claude/epic-cori-60fpeb` (created from that exact `main`) and landed through one
draft pull request (https://github.com/CausewayGrp/Financial-inclusion-/pull/4). At that merge every one of the 288
documents renders from the one content path (`design/reference/build.py`); Explore, the five hard domain answers, the
Evidence directory, the §9.1 record set, Compare and Data & sources are composed in the T4 grammar and each §9.2 hard
state on those routes is asserted on the rendered DOM (`design/reference/check_site.py`); the two repository browser
suites, bilingual invariance and content parity pass on the reference site; the five D1 residuals are reconciled
(DL-D2-002). At D3 (same branch and pull request, process note in `ESCALATIONS.md`) the Reading index, the ten Readings,
Measurement, Methodology, the eight trust pages and the bilingual 404 are composed, reviewed in both languages and
asserted (`check_site.py --gate d3`: 168 renders, 84 smoke tests, 252 hard-state assertions, 18 degraded renders), and
four fresh cold readers (EN/AR × 390/1440 px) read Home; their verbatim reports are in `evidence/d3/cold_read/`, the
design corrections in DL-D3-001 and DL-D3-002, the content observations in `ESCALATIONS.md`. At D4 (same branch) every
one of the 288 documents is asserted on its own row: all 110 evidence records against their governed bundles and the
three remaining domain answers against their contracts (`check_site.py --gate d4`: 904 renders, 452 smoke tests, 3,822
hard-state assertions), the neutral root entry, and the binding itself (`check_binding.py`: every RENDER and CONTRACT
projection read, no REFERENCE or VIA_SPEC projection read, no copied content model). At D5 (same branch) the thirteen
journeys are walked by keyboard at 390 and 1440 px in both languages and every technical state is driven and rendered in
a third, technical voice (`check_journeys.py`: 52 walks, 28 state drives; `07_INTERACTION_ACCESSIBILITY.md`). At D6
(branch `claude/bold-maxwell-r3o015`, pull request #5) the remaining visual contracts are drawn or framed per tier,
every figure carries its detached frame and its named-column table, every date and range is isolated by one pass over
every document, the export frames, the five social-image templates and the print system exist and are asserted
(`check_visuals.py`, five phases), five red-team lenses reviewed the built output (DL-D6-007), and
`06_VISUAL_TABLE_SYSTEM.md` and `08_ASSET_MAP.md` record the system; evidence in `evidence/d6/`. D2 records:
`04_PAGE_FAMILY_COMPOSITIONS.md`, `03_COMPONENT_CATALOG.md` (seeded), the decision log below (DL-D2-*),
`design/evidence/d2/`. Not PUBLIC RELEASE READY.

## 1. What this package is

The Design package of brief §19: decision log (this file), coverage ledger (`COVERAGE.csv`), design-debt register
(`DESIGN_DEBT.md`), escalations (`ESCALATIONS.md`) and the progressive Design→Code mapping (`09_CODE_HANDOFF.md`).
Files `01`–`08`, `10` and `design/reference/` are created at the gate that first needs them (plan, §6).

**Reference implementation (D2: every document builds; the hard families composed).** `design/reference/` holds one
content path (`yfie/content.py` reads `site-src/content/**` for all eleven families; never a copied content model, never
retyped text), the neutral harness (`yfie/neutral.py`), the accepted renderer of the converged direction
(`yfie/render.py` — shell, objects, the trio; `yfie/families.py` — the other families; `theme.py`, the one stylesheet;
`visuals.py`, the contract drawings) and the checks (`check_content.py`: numeric and text-block parity with `dist/` on
every document; `check_trio.py`: the D1 trio; `check_site.py`: the D2 routes with the family hooks, the §9.2 hard-state
assertions, degraded renders and the evidence writer). The package is still an incomplete hand-back until every family is
composed and reviewed on its own ledger row (D3–D4) and the acceptance checklist is complete (D7).

Build and preview: `python3 design/reference/build.py` (renderer `accepted`; `--routes trio` for the D1 build; `--renderer
neutral` for the harness) writes `design/reference/out/` — the 286 localized documents, the root entry, the 404,
`robots.txt`, `assets/yfie.css`, the unchanged fonts and logo, the baseline runtime, and `out/_bundle/<route>__<lang>.json`,
the exact content structures a renderer receives, and — with the accepted renderer — the portable frames of D6:
`out/_export/<visual>__<lang>.html` (one per drawn contract) and `out/_social/<route>__<lang>.html` (one per page).
Check with `python3 design/reference/check_content.py --text`, `python3 design/reference/check_binding.py`,
`python3 design/reference/check_site.py --gate d2 --degraded`, `… --gate d3 --degraded`, `… --gate d4`,
`python3 design/reference/check_journeys.py`, `python3 design/reference/check_trio.py --degraded`,
`python3 design/reference/check_visuals.py` (D6: every contract on every binding route in both languages, forced
colours and print on the drawn ones, every export and social frame, one route per family printed to PDF;
`--phases` for a subset, `--evidence DIR` for the record), `python3 design/reference/tokens.py --check`, and the
repository suites on the site:
`YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_public_tools.py`, `… audit/tranche_c/checks/viewport_acceptance.py`,
`… audit/tranche_c/checks/bilingual_invariance.py`; preview with `python3 -m http.server 4173 --directory design/reference/out`
(`/en/`, `/ar/`). Baseline: `python3 -m http.server 4173 --directory dist`. The D1 canvas composers
(`design/exploration/d1_canvas/`) are lineage; the reference renderer supersedes them.

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
| D2 | `claude/epic-cori-60fpeb` (planned `design/d2-hard-families`; the branch this environment may push, as at D1) | Explore, 5 hard domains, Evidence index, §9.1 record set, Compare, `/data/` | each §9.2 case proved (`check_site.py`); ledger rows `VERIFIED` or gap explained — **accepted at `2effd8b`, the merge of pull request #4** |
| D3 | `claude/epic-cori-60fpeb` (continued on the D2 branch and pull request; process note in `ESCALATIONS.md`) | Readings index + all Readings, Measurement, Methodology, trust, report journey, 404; Home cold-reader test | same; cold-reader record — **accepted at `2effd8b`, the merge of pull request #4** (`check_site.py --gate d3`; `evidence/d3/cold_read/`) |
| D4 | `claude/epic-cori-60fpeb` (continued; process note in `ESCALATIONS.md`) | all 288 documents via family rules | three suites pass on `design/reference/out/`; all rows ≥ `BUILT` — **accepted at `2effd8b`, the merge of pull request #4**: every route row `VERIFIED` (`check_site.py --gate d4`, `check_binding.py`) |
| D5 | `claude/epic-cori-60fpeb` (continued; process note in `ESCALATIONS.md`) | every tool state and journey, keyboard, zoom, reduced motion, forced colours | `07_INTERACTION_ACCESSIBILITY.md` — **accepted at `2effd8b`, the merge of pull request #4** (`check_journeys.py`; D5 rows `VERIFIED`, the two unbound verification states `DESIGNED`) |
| D6 | `claude/bold-maxwell-r3o015` (planned `design/d6-visuals-social-print`; created at the accepted `main` `2effd8b`; process note in `ESCALATIONS.md`) | visuals per contract, frames, social templates, print | contract-by-contract evidence — **met on this branch** (`check_visuals.py`: every contract, every export and social frame, every family route printed; `06_VISUAL_TABLE_SYSTEM.md`, `08_ASSET_MAP.md`, `evidence/d6/`; D6 rows `VERIFIED`); awaiting the owner's merge decision on the D6 pull request |
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
  Design Intent Lock and grammar; its status line states what is proven and what is not (D2 addendum in §2.6).
- **04_PAGE_FAMILY_COMPOSITIONS.md** (from D2): the deterministic module order and composition rules of every family, the
  first-screen contract, depth, next actions, and where each bound visual sits.
- **03_COMPONENT_CATALOG.md** (seeded at D2): every object with its governed inputs, states, widths, Arabic, names and
  keyboard, colour-free survival, fallback and the limitation it keeps visible; the figure anatomy; the evidence-state
  grammar with what is drawn and what is designed only.
- **06_VISUAL_TABLE_SYSTEM.md** (D6): every contract's form against its tier and rows, the detached frame, the table
  pattern, the text frames, the print system, the export frames and the export control, the social templates, the
  verification and the red-team record.
- **08_ASSET_MAP.md** (D6): the mark's placements and sizes, the three type faces and their roles, the glyphs, the
  social-image templates, the export identity line, what `out/assets/` holds.
- **07_INTERACTION_ACCESSIBILITY.md** (D5; D6 additions): the three voices, keyboard, motion, zoom, forced colours, no
  script, print, every technical state and journey.

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
- Second pass (same day): a fresh reviewer confirmed every MUST-FIX closed and returned "D1 DESIGN COMPLETE — OWNER
  MERGE REQUIRED" (`01_FOUNDATIONS.md` §6); its small residuals — a corrupt ledger note, an empty credit line on the
  Home figure, non-round ticks, a wrong table measurement, a stale path, three overstated sentences, hit areas — are
  closed in the hand-back commit, with forced colours and target size now asserted by `check_trio.py`.

### DL-D2-001 · D2 · 2026-09-27 · D2 authority, branch and persistence
- Problem: establish the D2 start state after the owner's merge of D1, and how D2 reaches the repository.
- Evidence: `origin/main` = `851f496078776356b38892c946d40d154c819067` (the merge of pull request #3; D1 head `604201d`
  contained); tree clean; `checksums.py --check` and `validate.py` pass; Production Master `17db032b…038690b`, Page
  Specs `d4574804…824b69aa`, logo `5830163d…60c6a90` hashed directly and unchanged.
- Alternatives: continue on the merged D1 branch; the planned `design/d2-hard-families`; the branch this environment
  may push.
- Chosen: `claude/epic-cori-60fpeb`, created at exactly `851f496`; one gate, one draft pull request into `main`; the
  steward may re-home the name. Milestone commits carry the records; work not pushed does not exist.
- Arabic / responsive / a11y: none. Code: none. Compromise: none.

### DL-D2-002 · D2 · 2026-09-27 · The five D1 residuals reconciled by their true authority
- Problem: the hand-back left four escalations and one composition question for the steward; D2 must not wait on
  items the repository already decides, nor invent what it does not.
- Evidence: `visual_design_contracts.json` — every `credit` carries `language_note`: "Publisher names are governed in
  English only (15, 34); Arabic frames print them as isolated left-to-right runs"; Home section 3 carries no newline or
  marker in either language; `interface_copy.json` holds no "on this page" label; brief §4.5: Home's baseline order "is a
  precedent, not a mandate; keep the `#system` anchor".
- Alternatives: ask the steward for all five; resolve none; classify each by its authority and resolve what the
  repository already determines.
- Chosen: (1) Arabic credit line — PAGE SPEC / CONTROLLED CONTENT, already answered by the contract: every frame prints
  the governed credit as `<bdi dir="ltr">`; escalation closed. (2) Home pacing marker — Master-first; stays open,
  non-blocking (the Lock's connective rule with the whole-paragraph fallback holds; DEBT-008). (3) IMF lane evidence
  state — MASTER / EVIDENCE AUTHORITY; a question only the steward answers; REPORTED rendered as governed; stays open.
  (4) In-page navigation name — ENGINEERING / ACCESSIBILITY: the index is named by the `h1` of the object it indexes
  (`aria-labelledby="page-title"`), the strip likewise, each edge group by its own governed heading; no label authored;
  DEBT-006 and the escalation closed. (5) Home section order — DESIGN, decided by brief §4.5; closed.
- Arabic / responsive / a11y: the credit run keeps its Latin order inside Arabic text; every `nav` on every page now
  has an accessible name (`check_site.py` fails on an unnamed `nav`).
- Code: inherits the `aria-labelledby` pattern and the credit isolation. Compromise: a dedicated governed label would
  read better than the page title for the index; it is not an authority question, so it is not escalated.

### DL-D2-003 · D2 · 2026-09-27 · The paper scaling test made real: one grammar, eleven families, varied intensity
- Problem: prove that the D1 evidence intelligence scales across the real product without a second grammar and
  without repetition, timidity, dashboards or English-first composition (brief §9.4; hand-back §R).
- Evidence: all 288 documents render from `content.py` → `render.py`/`families.py`; `04_PAGE_FAMILY_COMPOSITIONS.md`;
  `design/evidence/d2/` (first screens at 390 and 1440 px, EN and AR, of the hard routes; figure crops); the two
  repository suites and invariance pass on the site.
- Alternatives: a template per family; one identical template; one grammar with composition rules per family.
- Chosen: one page object (head → answers → boundary voice → figures → compact objects → depth → next → foot → spine)
  with composition rules per family and intensity that follows the evidence structure: Explore is a numbered question
  index; the domain answers open on their contract's always-visible limits and vary by `presentation_family`; the
  directory is search plus a question-grouped register of 110 rows; Compare leads with the boundary and recomposes its
  table at 320 px as numbered slot blocks; Data & sources is a register of curated categories and dependency groups.
  Where a bound visual sits is a recorded table, not a per-route guess.
- Arabic / responsive / a11y: Arabic composed on its own tokens throughout; identifiers, dates and codes isolated; axes
  left-to-right; one column below 600 px, the spine from 900 px, the rubric column from 1200 px; every landmark named.
- Code: `families.py` is implementation-grade composition; the placement table is data Code reuses.
- Compromise: the D3 families (Reading index, Measurement, trust) build by the family rule and are `BUILT`, not
  reviewed; Yemen material grounding beyond abstraction is still not attempted (DEBT-007).

### DL-D2-004 · D2 · 2026-09-27 · The domain answer and the record's evidence states
- Problem: compose eight domain answers from the presentation contract without a chart wall, with the limits first
  and the depth honest; keep framing, composite, partial, thin and withheld records from looking weaker or broken.
- Evidence: `presentation_priority.json` (`mobile_priority`: lead → supporting → primary → verify; `after_primary`);
  brief §12 on several visuals per page; `check_site.py` assertions for CLM-004, -014, -015, -031, -039, -044, -045.
- Alternatives: the baseline order (hero, band, primary); limits after the answers as on the Record; the contract's
  mobile priority everywhere.
- Chosen: the contract's order — the band (boundary voice) before the answers; the first-screen visual after
  `after_primary`; the small multiple and unplaced visuals in a depth group under the governed "Another view" rubric;
  progressive sections in one disclosure; then Readings, related questions, Measurement, Verify. On the Record the
  lineage statement (framing, composite, partial) is question 6's answer in the body voice; a record without a public
  locator says so in the body voice; the governed source intro is printed unless the record is a framing rule; the 13
  comparable records carry a Compare entry; a `VIS-` record draws its visual under its first answer (its canonical route).
- Arabic / responsive / a11y: the band's double rule and label carry the limit without colour; every disclosure has a
  governed summary.
- Code: the composition rules in `04_PAGE_FAMILY_COMPOSITIONS.md` §2–§3.
- Compromise: the source intro's absence on the framing record is a recorded exception of the text-parity check.

### DL-D2-005 · D2 · 2026-09-27 · The D2 figures: forms per contract, one anatomy, the state grammar drawn
- Problem: draw VIS-FINDEX-GAPS, VIS-REMITTANCE-MACRO, the POS small multiple, VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-COST
  and the payment chain truthfully, in both languages, at every width, under strict CSP, so that the hard states can be
  asserted rather than argued.
- Evidence: each contract's `form`, `annotation`, `missing`, `breaks`, `mobile` and `rtl` fields; the grammar table;
  RV-CWR-009's `step_mapping` and event objects (VIS-PAYMENT-RAILS's rationale asks for that reuse); `check_site.py`
  assertions (bars 9, gaps 4 as brackets; 3 states keyed, break not joined, 5 dashed segments; 3 panels with own axes,
  3 rings, 1 labelled gap; 7 objects, 2 withheld without digits; chain 7 steps, 3 evidenced, the first open step marked).
- Alternatives: one generic chart per form; contract-specific drawings sharing one frame.
- Chosen: the D1 anatomy for every figure (rubric, title, question, scope, panels, notes, boundary, credit, canonical
  link, cite, visible text alternative with the table) with six forms (`03_COMPONENT_CATALOG.md` §2): bars with
  bracket gaps; state-keyed time series with the break, missing, disagreement and nominal grammar and a key of states
  with their source document; dot rows; an object list with WITHHELD in place of a value; the chain ladder with the
  first open step in the boundary voice; text frames for every contract without rows. One number rule with precision
  as governed (a rounding fault found by the parity check was fixed). Value labels on every point, on two rows for
  dense series, and below 600 px only the first, last, marked and state-change points.
- Arabic / responsive / a11y: value and time axes left-to-right; labels, panel order and rows follow the reading
  direction; the credit isolated; forced colours keep marks, bars, rules and chart text; print keeps each figure whole.
- Code: `visuals.py` drawers and the percentage-coordinate technique; the grammar table is the contract for D6.
- Compromise: seven grammar states have no contract row anywhere and are designed only; the fallback tables head only
  the value column (escalated); dense labels rely on the table below 600 px (DEBT-012).

### DL-D2-006 · D2 · 2026-09-27 · Compare and the source register: tools composed, runtime untouched
- Problem: give Compare and Data & sources the T4 grammar while keeping `site-src/app.js` and every test hook unchanged,
  and prove compare_unlike and source_scale.
- Evidence: `test_public_tools.py` 25/26 on the reference site; `check_site.py` (boundary before controls, verdict
  before table and in the boundary voice, no numeric columns, text-labelled states; 151 sources, 28 curated in 6
  categories, supporting open, reference closed, every source named or referenced, no locator-less source named).
- Alternatives: a new runtime; CSS-only composition of the runtime's output.
- Chosen: the runtime's output is styled, not rewritten: the verdict as the boundary voice; the table in its named
  region; at 320–639 px each dimension row becomes a block with its cells numbered in slot order by CSS counters (the
  slot labels are governed) — a recomposition, not a shrink (EAD-06). The register: curated cards by
  `resource_category`, citation cards by governed title, locator-only sources by reference and locator, dependency
  disclosures, the filter and statuses as hooks.
- Arabic / responsive / a11y: `<select>` controls ≥ 44 px; the copy-link and copy-reference actions are buttons; the
  filter has a visible governed label; every hidden row uses `[hidden]`.
- Code: the CSS recomposition rule and the register composition; nothing in the runtime.
- Compromise: the supporting group is open by default and long (94 rows) — paging or a category filter is a D5/D6
  question (DEBT-011).

### DL-D2-007 · D2 · 2026-09-27 · Every document builds; the repository suites run on the reference site; the checks are widened honestly
- Problem: a green test must correspond to the implementation being accepted; the D1 build could not run the
  repository suites (DEBT-009), and the D2 routes need their own proof.
- Evidence: `build.py` builds all 288 documents plus the root, the 404 and `robots.txt`; `test_public_tools.py` 25/26
  (1 not applicable, as on `dist/`), `viewport_acceptance.py` 168/168, `bilingual_invariance.py` 0 of 143 — all with
  `YFIE_SITE_DIR=design/reference/out`; `check_site.py` 168 renders, 84 smoke tests, 157 hard-state assertions, 20
  degraded renders; `check_content.py --text` PASS on 288 documents; `check_trio.py` 24/12 unchanged.
- Alternatives: keep the trio-only build until D4; build everything with the family rule now.
- Chosen: build everything now (the D3 families by the family rule, recorded as `BUILT`), run the suites unchanged, add
  `check_site.py` with hard-state assertions per route as the D2 evidence, and widen `check_content.py` in two bounded
  ways: a number the reference prints beyond the baseline may also be a number in the governed content the loader gave
  that page (the bundle), and inline elements no longer count as word breaks (a tag-stripping artefact). Both were
  found by real faults (a rounding error; a linkified address).
- Arabic / responsive / a11y: the suites cover both editions at four widths. Code: the suites are the contract.
- Compromise: `check_content.py` fails on an unbuilt site (a guard added after it once passed on nothing).

### DL-D2-008 · D2 · 2026-09-27 · Records, debt and escalations at D2
- Problem: keep the durable records the only memory.
- Chosen: `COVERAGE.csv` — 190 D2 rows `VERIFIED` (176) or `DESIGNED` with the gap explained (14: grammar states no
  contract row carries); 1,001 D3/D4 rows `BUILT`; the seven D2 figures' D6 rows `VERIFIED`, the text frames `BUILT`.
  `DESIGN_DEBT.md`: DEBT-004, -006, -009 closed; DEBT-002 advanced; DEBT-011…013 opened. `ESCALATIONS.md`: three
  closed, two open, two raised (fallback-table column labels; rows for VIS-TARGET-RESULT-STATE and VIS-MFI-DIVERGENCE).
  `09_CODE_HANDOFF.md`: state at D2. `04_PAGE_FAMILY_COMPOSITIONS.md` and `03_COMPONENT_CATALOG.md` created.

### DL-D3-001 · D3 · 2026-09-27 · The Home cold-reader test: who read, how, what they said
- Problem: the brief's test — a person who has never seen the product reads Home and says what it is, what it can do and
  whether it can be trusted — had not been run on the rendered product.
- Method: four fresh agents with no access to the repository, one per language and width (English and Arabic at 390 and
  1440 px), each shown only five captures of the rendered Home page (four screens in order, then the full page) and asked,
  in stages (30 s, 90 s, 180 s), what the site is, where they would start, whether scope and limits are stated, which link
  they would click and what they expect behind it, what confused them, what a screenshot of the first screen could make
  someone misread, and whether the page reads as serious, trustworthy and clear (the Arabic readers also: whether the
  Arabic reads naturally). Their reports are recorded verbatim in `evidence/d3/cold_read/home-<lang>-<width>.md`.
- What they said, in common: serious and restrained, every number bounded, the "not one number" thesis retained; but the
  product's own statement of what it is arrives only on the third screen; two links per record card with no stated
  difference; the boundary's double rule shorter than the other rules; the system frame's "What not to conclude" printed
  three times and its "Text description of this view" heading a view that does not exist; the sidebar count "(4)" against
  one inline card labelled "behind these figures"; the publisher legible only in the footer; the nav group label read as a
  stray tooltip in Arabic; the small gold labels hard to read in Arabic; and, in the content, three date formats, two-decimal
  precision, three years attached to one number, jargon (POS, CBY-Aden, wave, rails, "Evidence signals") and Arabic
  calques.
- Classified: design and engineering findings corrected at D3 (DL-D3-002); content and authority findings recorded in
  `ESCALATIONS.md` ("Raised at D3"), none filled with authored copy; the phone-length findings recorded as debt (DEBT-014,
  DEBT-015); the publisher-mark finding as debt and escalation (DEBT-016).
- Rejected: shortening or splitting the governed product statement; authoring a one-line strapline; a "start here" label;
  renaming the nav; any change to governed numbers, dates or terms.

### DL-D3-002 · D3 · 2026-09-27 · Home and the shared objects corrected from the test (within the Lock)
- Problem: the findings above that are design or engineering.
- Chosen: (1) the head carries the governed product statement (section 1) and its two governed actions under the
  headline, before the first figure — the baseline's own order, which D1 had moved below the figures (Lock §4 keeps
  clock-before-claim: the figures still open with their clocks); the product rubric stays on wide screens and is not shown
  under 600 px, where the masthead already names the product; (2) one link per compact evidence object: the governed action
  ("Open evidence record") is the link and its accessible name is the action followed by the record's title
  (`aria-labelledby` over the two governed strings) — the title is no longer a second link to the same record; (3) the
  figure prints its boundary once, in the foot, under the governed `UI-DOM-WHAT-NOT-TO-CONCLUDE` label (the label the
  baseline uses for a visual); the text alternative carries what the view shows, its scope and the table; (4) a text frame
  (no drawing) presents the governed description as its body — its "Text description of this view" heading stays in the
  accessibility tree only and it carries no hidden second copy; (5) the framing record bound to Home ("a connected system,
  not a single score") sits in the system-context section it frames, so nothing on the page is labelled "behind these
  figures" but the spine's edge, which lists all four; (6) the boundary's double rule spans the column, the text inside
  keeps the measure; (7) the primary-nav group is set off by a hairline and its label aligned to the links' baseline; the
  masthead's cite and report actions in the body ink, not the muted grey that read as disabled; (8) the Arabic rubric size
  13 → 14 px (`02_TOKENS.json` regenerated); (9) the governed instruction and body of "Questions to start from" read as one
  paragraph. `check_site.py` asserts (1)–(3), (5) and (6) on Home (`statement_in_head`, `statement_before_first_figure`,
  `one_link_per_bound_object`, `boundary_once_per_frame`, `records_edge_lists_all`, `double_rule_spans_column`).
- Rejected: shortening the statement on phones (governed; DEBT-015); a collapsed index on phones (Lock: one visible spine;
  DEBT-014); enlarging the logo (the mark's own clear space keeps its wordmark under 8 px at any masthead size; DEBT-016).

### DL-D3-003 · D3 · 2026-09-27 · The synthesis families composed and reviewed
- Problem: the Reading index, the ten Readings, Measurement, Methodology, the eight trust pages and the 404 were built by
  the family rule at D2 and not yet composed or reviewed on their own rows.
- Chosen: each route reviewed in both languages at 390 and 1440 px (first screens in `evidence/d3/`) and asserted per
  family (`check_site.py --gate d3`): the Reading opens on the question, the title, the thesis and its two clocks, its
  boundary before the essay, at most one figure after the opening, the trace to records with the source record or the
  governed path state, one or two related Readings and no lifted number in the standfirst; the essay measure is the
  language's own (64ch Latin, 34em Arabic), never the column; Measurement carries ten equal-weight, deep-linkable priorities
  with no ordinal numbering (`measurement_nonranking`); About reads without backend terminology
  (`trust_plain_language`); Contact and Corrections keep the runtime's report path; the 404 is bilingual, Arabic first. The
  family rules stood: no composition changed beyond the shared objects of DL-D3-002.
- Rejected: a separate composition per trust page (they share one page object by design); numbering the priorities.

### DL-D3-004 · D3 · 2026-09-27 · The Reading measure assertion corrected
- Problem: the first D3 run failed `measure_bounded` on every Reading at 1440 px because the assertion assumed a 760 px
  paragraph; the essay measure is `--measure` (64ch at the reading size ≈ 704 px Latin, 680 px Arabic).
- Chosen: assert the property, not a guess — a reading paragraph is narrower than the page object and never wider than
  720 px; re-run green. Recorded so a green test corresponds to the implementation accepted.

### DL-D3-005 · D3 · 2026-09-27 · Records at D3
- Chosen: `COVERAGE.csv` — 164 D3 rows `VERIFIED` (160 route rows, 4 hard-state rows), the Home rows annotated;
  `DESIGN_DEBT.md`: DEBT-014…016 opened, DEBT-002 and DEBT-007 advanced; `ESCALATIONS.md`: the cold-reader content
  observations raised, a process note on the branch; `09_CODE_HANDOFF.md`: state at D3; `04_PAGE_FAMILY_COMPOSITIONS.md`
  and `03_COMPONENT_CATALOG.md` updated; the four cold-reader reports kept verbatim under `evidence/d3/cold_read/`.

### DL-D4-001 · D4 · 2026-09-27 · Every evidence record asserted from its own bundle
- Problem: 102 records outside the §9.1 set were built by the family rule and never looked at; a route-by-route review of
  880 renders would be theatre, and a hand-kept list of expectations would drift from the Master.
- Chosen: the check reads each record's governed bundle as the build wrote it (`out/_bundle/<route>__<lang>.json`, the
  same file `check_content.py` reads) and asserts what the page must show for that record: the seven questions; the
  boundary on first load; the clock before the claim; as many source cards as the bundle has sources, with a public
  locator on every one; the lineage statement with its state exactly when the bundle carries one; the members list with
  the bundle's members exactly when it is a composite of objects; the no-locator and some-without-locator states exactly
  when stated; a trace chip per source id; the Compare entry exactly when the record is comparable; the record's own
  visual under the first answer exactly when it has one; the boundary printed once per frame; and that nothing looks
  empty. 3,822 assertions pass over 880 record renders (`check_site.py --gate d4`), on top of the smoke test at 390 and
  1440 px and the render conditions at four widths. One record per verification state outside the §9.1 set is kept as
  evidence (`evidence/d4/`).
- Rejected: a fixed list of expected values per route (drifts from the Master); sampling (the gate's exit is every row).

### DL-D4-002 · D4 · 2026-09-27 · The three remaining domain answers
- Problem: `/firms/`, `/finance/` and `/providers/` were built by the Domain Answer rule at D2 and not reviewed.
- Chosen: reviewed in both languages at 390 and 1440 px and asserted from their bundles — the governed question before the
  answer, the contract's band before the answers, the primary visual framed as its text frame (VIS-FIRM-CONSTRAINTS,
  VIS-MFI-DIVERGENCE, VIS-PROVIDER-OBSERVABILITY: TABLE_TEXT_FIRST or SUPPORTING contracts without rows; D6), every
  verification, measurement and Reading object bound, the depth in one disclosure, the governed related questions, and
  the 24-event chronology on `/finance/` (JRN-09). The family rule stood; no route-specific composition was needed.
- Rejected: drawing the three visuals at D4 (a visuals-gate decision; VIS-MFI-DIVERGENCE's rows are escalated).

### DL-D4-003 · D4 · 2026-09-27 · The neutral root entry and the binding proved
- Problem: the root entry and the "complete binding" claim had no check.
- Chosen: `root_checks` in `check_site.py` (no inline script or style; both `hreflang` alternates and `x-default`; Arabic by
  default; the stored edition kept) and `design/reference/check_binding.py`, which reads the inventory's projection roles
  and proves that every RENDER and CONTRACT projection is read by the one content path (or shipped unchanged for the
  runtime: the search index and aliases), that no REFERENCE or VIA_SPEC projection is read by any reference module, that
  a STRUCTURE projection is read only for its ids and links, and that the built site holds 286 edition pages, the root,
  the 404, one bundle per page and no copied content model. The one deviation it found — `public_claims.json` (VIA_SPEC)
  loaded by the content path and never used — is removed.
- Rejected: a bodied root page with authored edition links (no governed copy exists for it; the baseline's no-script
  refresh to Arabic stands).

### DL-D4-004 · D4 · 2026-09-27 · Records at D4
- Chosen: `COVERAGE.csv` — 841 D4 rows `VERIFIED` (816 record rows, 24 domain rows, the root entry); every route row of
  the ledger is now `VERIFIED`; the D5 (tool states, journeys) and D6 (visuals) rows remain. `DESIGN_DEBT.md`: DEBT-002
  and DEBT-007 advanced. `09_CODE_HANDOFF.md`: state at D4. `04_PAGE_FAMILY_COMPOSITIONS.md`: the three answers and the
  record assertion recorded. `evidence/d4/` (42 PNG).

### DL-D5-001 · D5 · 2026-09-27 · The technical voice
- Problem: the runtime's technical states (Compare link errors, the same-record state, search and register statuses and
  no-match states, record-context link errors, the no-script note) rendered in the body voice or, for the same-record
  state, in the boundary voice — a technical failure could read as a statement about the evidence, and the same-record
  state as an assessment.
- Chosen: a third voice with one non-colour signal — a dashed hairline above the message, body ink (`--ink-2`), the
  governed title where the runtime writes one — never the double rule, the counter colour or the plaster surface, and
  never inside a boundary section or an evidence-gap object. Applied to every hook the runtime writes into
  (`03_COMPONENT_CATALOG.md` §1, technical state). `check_journeys.py` drives all fourteen runtime states in both
  languages and asserts the announcement (alert or status), the dashed rule, the absence of a verdict where none is due,
  and that navigation keeps working; the same-record state is asserted to be the only `[data-compare-verdict]` value.
- Rejected: an icon or a colour for "technical" (colour never carries meaning alone; no icon vocabulary exists); hiding
  the states (the runtime's behaviour is the baseline's and is proved by `test_public_tools.py`).

### DL-D5-002 · D5 · 2026-09-27 · The thirteen journeys walked by keyboard
- Problem: the acceptance criterion — the thirteen journeys succeed by keyboard, on mobile and desktop, in both
  languages — had no proof on the rendered product.
- Chosen: `check_journeys.py` walks each journey of the inventory at 390 and 1440 px in English and Arabic: from every
  page of the path a link the page itself offers (in the page object, the spine, the product bar or the footer — the
  first one visible at that width) takes keyboard focus, shows the focus outline, sits in the viewport and activates with
  Enter; on a phone a primary-nav link is reached by opening the menu with the keyboard first; every landing is asserted
  against the journey's success condition (`07_INTERACTION_ACCESSIBILITY.md` §5). 52 of 52 walks pass. Two walks failed
  on the first run because the checker followed a hidden side-spine link on a phone; the product offered the same link
  in the foot spine, which is the phone's verification path — the checker was corrected, the product was not.
- Rejected: a tab-through of every page (hundreds of links on `/data/`; a focus-and-Enter on the offered link proves the
  same reachability); scripting the journeys through the URL bar (that proves nothing about the product).

### DL-D5-003 · D5 · 2026-09-27 · Motion, zoom, forced colours, no script, and the two unbound verification states
- Chosen: recorded in `07_INTERACTION_ACCESSIBILITY.md` §3 as proved by the existing checks (the 320 px renders stand for
  400 % zoom of a 1280 px window; the forced-colours and no-stylesheet renders of every gate; reduced motion removes
  every transition, and no state depends on motion); the no-script note in the technical voice on every page, with the
  evidence readable (asserted). `SOURCE_NOT_YET_BOUND` and `NO_SOURCE_RECORD`, which no record carries today, are designed
  as states of the record's question 6 with their governed copy (`UI-EVID-UNBOUND`, `UI-EVID-THIS-RECORD-CURRENTLY-HAS-NO`)
  in the body voice; the content path carries both branches; nothing is rendered on an invented record (ledger rows
  `DESIGNED`).
- Rejected: an authored "(opens in a new window)" cue on external source links — governed copy, raised in
  `ESCALATIONS.md` (anticipated at D0, needed now).

### DL-D5-004 · D5 · 2026-09-27 · Records at D5
- Chosen: `COVERAGE.csv` — 82 D5 rows `VERIFIED` (52 journeys, 30 technical states), 4 `DESIGNED` (the two unbound
  verification states); `07_INTERACTION_ACCESSIBILITY.md` written; `03_COMPONENT_CATALOG.md` technical state;
  `09_CODE_HANDOFF.md` state at D5; `DESIGN_DEBT.md` DEBT-014 narrowed; `ESCALATIONS.md` the external-link cue raised;
  `evidence/d5/` (journey end screens, technical-state screens).

### DL-D6-001 · D6 · 2026-09-27 · The thirty-six contracts: what is drawn, what stays text, and why
- Problem: after D2, thirteen contracts had a drawn form and twenty-three rendered as text frames; D6 had to decide the
  form of every remaining contract from its tier and its rows, not from the presence of numbers.
- Evidence: the contracts file (three SIGNATURE, nine CORE_ANALYTICAL, twelve SUPPORTING, eleven TABLE_TEXT_FIRST, one
  RETIRE); the rows each resolves (`06_VISUAL_TABLE_SYSTEM.md` §1); brief §12 (a SUPPORTING diagram only from governed
  words and grammar labels; TABLE_TEXT_FIRST never a chart; rows never built from a reference file).
- Chosen: draw the four with rows and a governed vocabulary — RV-CWR-009 as the full chain with its POS activity
  values, VIS-PROVIDER-OBSERVABILITY as a provider matrix, RV-CWR-004 as three dated lanes, VIS-FIRM-CONSTRAINTS as
  bars from zero without ranks — and keep every SUPPORTING and TABLE_TEXT_FIRST contract without rows as the governed
  text frame: their rungs, layers and relationships exist only as English prose in STRUCTURE- or REFERENCE-role files,
  so a diagram would author its labels. VIS-SOURCE-COMPARISON stays the Compare tool itself (D4); VIS-CAPITAL-CONTEXT
  is never drawn and `/reforms/` keeps the baseline's governed text frame for parity.
- Rejected: a ladder for VIS-FL-EVIDENCE-LADDER and VIS-EVIDENCE-CLASS-LADDER and a stack for VIS-E-MONEY-RULE-STACK
  from their alt text (authored rung labels); a three-row table for VIS-TARGET-RESULT-STATE from the record's prose
  (no rows; escalated at D2); VIS-FIRM-CONSTRAINTS with the eight rows of `firm_finance.json` (a REFERENCE file the
  reference may not read; the rows are requested).
- Arabic, responsive, accessibility: each form's narrow form and RTL rule in `06_VISUAL_TABLE_SYSTEM.md` §3; asserted
  by `check_visuals.py` on every binding route in both languages.
- Code: `visuals.DRAWERS`; the content path's additions (`09_CODE_HANDOFF.md`, state at D6).

### DL-D6-002 · D6 · 2026-09-27 · The three D6 forms
- Problem: the matrix, the dated lanes and the multi-response bars had no precedent in the grammar and each carried a
  firewall risk — a licence read as operation, a sequence read as cause, an ordered list read as a ranking.
- Chosen: **the matrix** keeps five dimensions apart per class in self-labelled cells of governed words and dates
  (never a dot, a bar or a score), prints UNKNOWN wherever no governed row exists, lists wallet counts by date and
  wording rather than as one number, counts the roster by category and never as a total of providers, ends each class
  with its governed limit in the boundary voice, and links every dated status to its source record; its headings are
  placeholders until governed. **The lanes** share one left-to-right time axis but no value axis: the people lane is
  the governed fieldwork span with the survey value and state, the infrastructure lane a dated presence with its first
  and latest governed values, the institutions lane dated events keyed to a list, the outcome an open node in the chain
  vocabulary, the governed not-comparable label between lanes. **The bars** keep the contract's descending order but
  print no ordinal and print the record's measurement limitation in the frame, so the order reads as the source's, not
  as a rank.
- Rejected: dots or bars in the matrix (a share or a size would be read); a single "providers" total (429 rows are not
  429 providers); the survey point placed on the time axis as one date (its governed boundary is a fieldwork span and a
  reporting year); rank numbers on the bars; a stacked bar (the responses are not exclusive; the base is not held).
- Arabic: the lanes and bars keep left-to-right axes with mirrored labels and lists; the matrix cells mirror; every ISO
  date and every English governed time boundary is isolated left-to-right (DL-D6-004).
- Code: `visuals.provider_matrix`, `dated_lanes`, `firm_constraints`; `theme.CSS_D6` (container-query grid for the
  matrix cells at ≥ 480 / ≥ 760 px container width).

### DL-D6-003 · D6 · 2026-09-27 · One table pattern: named columns, qualifiers in the caption or the cell
- Problem: the D2 fallback tables had four columns, three of them with empty headers (DEBT-013), and at 320 px they
  scrolled inside their wrapper (DEBT-010); a screen-reader user heard unlabelled columns and the same state repeated on
  every row.
- Chosen: `visuals.table()` refuses an unnamed data column; every table is the row header plus a value column headed by
  the governed unit (plus `UI-VIS-SOURCE` or `UI-VIS-WHAT-THE-EVIDENCE-SHOWS` where a second data column is needed); a
  qualifier that holds for every row — state, source document, a marker every object carries — is stated once in the
  caption, and one that varies travels in the value's own cell after a middle dot; the corner cell above the row
  headers is empty by table convention. Two or three columns fit 256 px in both languages on all thirteen drawn
  contracts; only the matrix's six-column table is declared wide. The table sits in a region named by the text
  alternative's heading and the figure's title. `check_visuals.py` fails an unnamed column, an unnamed region, and a
  table that scrolls without the declaration.
- Rejected: stacked column groups at 320 px (a second table structure, duplicated governed text); hyphenation or a
  smaller type to squeeze four columns (legibility); repeating a uniform state on every row (noise for every reader).
- Code: `table()`, `qual()`, `uniform()`, `table_region()`; the D2 checker's assertions unchanged.

### DL-D6-004 · D6 · 2026-09-27 · Bidi: every ISO date, numeric range and English governed time boundary isolated
- Problem: after Arabic letters, a plain ISO date renders with its parts reversed (the bidi algorithm makes the digits
  Arabic numbers and the hyphens neutrals: "2024-06-26" shows as "26-06-2024"); the recomposed tables put governed
  Arabic text before dates, and a probe confirmed the reversal on the page and its absence inside a `bdi`. The matrix's
  time boundaries are English free text ("observed 2026-09-07", "2026-01-22 event").
- Chosen: one isolation pass over every finished document (`text.isolate_document`, called by `render.render`, the
  neutral files and both portable frames): every ISO date and every numeric range ("2021–2024", "2025-03–2026-01",
  "15–24") in any text becomes an unbroken left-to-right run, wherever a renderer left it plain — script, style, SVG,
  the title and form controls untouched, an isolate never nested in an isolate. The Arabic lens found the ranges: in
  Arabic prose a plain range renders with its ends swapped ("2030–2018" beside an isolated legend "2018–2024") and
  breaks at the dash at 390 px. An identifier (`text.bdi`) is isolated but breaks only at its own hyphens — the D4 gate
  on the corrected tree caught the first D6 text layer making identifiers unbreakable, so a 37-character source id
  overflowed seven record pages at 320 px. A governed time boundary prints exactly as the Master holds it, isolated
  and marked `lang="en"` — its qualifier is part of the boundary and is never dropped (an earlier D6 pass printed only
  the date part; reversed). Asserted three ways: statically on all 598 documents and frames (`check_visuals.py`
  `--phases text`, the renderer's own `LTR_RUN`), in the browser on every figure and every frame, and by the fit test
  on both edges of the figure and the whole document at 320, 390 and 600 px.
- Rejected: printing only the date of a governed time boundary (lossy); translating the qualifiers (authored copy —
  the bilingual form is escalated); leaving ranges to the reader's direction (two conventions in one figure);
  isolating every Latin run in Arabic text (a long run would overflow 320 px; DEBT-017).
- Code: `text.py` (`LTR_RUN`, `bdi`, `isolate_iso`, `isolate_document`), `date_token`, `check_visuals.check_text`.

### DL-D6-005 · D6 · 2026-09-27 · The narrow time series prints its landmarks; the table carries every value
- Problem: DEBT-012 — below 600 px a series of more than eight points cannot print thirteen value labels legibly with
  percentage coordinates, and the decision was deferred to D6.
- Chosen: decided, not deferred — the narrow panel prints the first, last, marked and state-change values; the
  two-column table under the figure, which now fits 256 px, is the narrow carrier of every value; the export frame at
  800 px prints every value. Closed as a decision.
- Rejected: a horizontal-rows form (thirteen rows per POS panel, three panels); a two-row label lattice (does not fit
  300 px legibly); rotated labels (not available with percentage coordinates).
- Labels never meet (after the red teams): a value label takes the first of three rows above its mark (12, 26 and
  40 px) at which its ink — digits have no descender: 9 px at 12.5 px — keeps 4 px from every earlier label it could
  touch horizontally, judged in the wide regime (every label visible, the 536 px panel, measured) and, for a landmark
  label, the narrow one too (landmarks only, the 256 px panel); the on-panel state labels are placed first as
  obstacles, on rows 15 px apart; under 480 px of figure width only the first, middle and last time-axis labels show.
  `check_visuals.py` asserts `labels_clear` on every drawn figure at 320, 390, 600 and 1440 px and in every export
  frame, by the same ink-box measure (a projection pair that touched at 584 px and overlapped at 390 px is what the
  visual and Arabic lenses saw).

### DL-D6-006 · D6 · 2026-09-27 · Portable evidence and the print system
- Problem: nothing that left the page — a printed page, a shared image, an exported figure — carried its provenance and
  limits; the D1 print rule that kept the whole page object together began every printout on its second page (found by
  the print check on `/people/`); a boundary band of several sections was one unbreakable chain.
- Chosen: **export frames** (`frames.export_document`, one per drawn contract and language, the figure with its complete
  frame and an identity line; the export control designed and unshipped until its labels are governed and OWN-04 is
  decided); **social templates** (`frames.social_document`, five templates from governed text only — a record's card
  with its clocks, reference and boundary, a Reading's with its question, evidence period and prohibited inference, a
  domain answer's with its question and first-screen boundary, the product's and the hubs' with the title and the
  description after it without repeating it; type steps down with length, never a crop; Code rasterises and adds
  `og:image`); **the print system** (`theme.CSS_D6`: chrome hidden, the page object and answers breaking freely,
  objects that fit a page whole, a boundary with the claim before it, figures whole with their foot, list panels
  breakable between items, table headers repeated, black inks; the print-only provenance block on every page; the
  Reading as a document). Asserted: `check_visuals.py --phases frames,print` — every export and social frame; one route
  per family × EN/AR printed to PDF, the title on page one (an order-aware word matcher with a self-test and a
  cross-route negative control), the provenance block, every figure whole with its boundary.
- Rejected: `og:image` on the reference site (Code generates the images; F6 keeps Open Graph without image); a hosted
  PDF (a download, gated); dropping the meta description from the card (the title would still read once, but the
  description's remainder is governed context — kept, deduplicated without loss).
- Code: `frames.py`, `render.print_foot`, `build.py` (`_export/`, `_social/`), the print block of `theme.CSS_D6`.
- Result on the final tree (`check_visuals.py`, five phases, record `out/_review_visuals.json`, evidence
  `evidence/d6/`): 36 contracts × EN/AR on every binding route, 2,856 contract assertions; 52 forced-colours and print
  checks on the thirteen drawn contracts; 26 export frames; 286 social frames; 133 print checks on the eleven family
  routes × EN/AR; 598 documents and frames scanned for a date or range outside an isolate; 0 failures; the six
  placeholders exactly the escalated set. On the same tree: `check_site.py` D2 (168 renders, 553 hard-state assertions, 20
  degraded), D3 and D4 (904 renders, 3,822 assertions), `check_journeys.py` (52 walks, 28 drives), `check_trio.py`, the
  two repository browser suites, bilingual invariance, content parity (288 documents), the binding check and `tokens.py
  --check`.

### DL-D6-007 · D6 · 2026-09-27 · The red teams and what they changed
- Problem: the gate's own checks prove what they assert, not what a hostile reader sees. Five independent lenses
  reviewed the built figures, portable frames and print pages of the first D6 pass: a financial-inclusion measurement
  expert with a statistician (semantic firewall), an information-visualisation expert with an editor (form,
  legibility, genericity), a native Arabic editor (composition, terminology), a journalist with a hostile source owner
  (screenshot misuse, portable evidence), and an accessibility specialist with a frontend engineer (DOM, CSS, print,
  code). Four reported in full; the Arabic lens was cut off twice by session limits and re-run on the corrected tree
  (its findings, in the same record, close the entry).
- Found and fixed (every MUST-FIX, and the SHOULD items that improve truth or legibility within the Lock):
  the fifth provider class (payment-system operators, the contract's known gap) was absent because its label is not
  governed — the one class with no evidence had no UNKNOWN cell; it is now always drawn, UNKNOWN in every dimension,
  under a placeholder heading, in the panel and the table · the wallets' authority cell was empty in the table while
  the panel listed four documents · a hollow square and a ring keyed publications and send amounts while hollow means
  "not an observation" in the state grammar — publications and groups now take filled shapes (circle, square, diamond);
  RV-CWR-001 prints its REPORTED state in the panel and the same-year marker between its two rows, so a crop of the
  rows never reads as a fall · the break legend put an arrow between two numbers (forbidden in Arabic) — the two periods
  now stand without an arrow · value labels of the time series collided with the axis ticks, with each other and with
  the break rule — the panel is inset, the first and last labels start and end at their marks, a label beside a break
  keeps to its side, a dense series chooses its label row by the distance to its neighbour, and the states stand on the
  panel above their segments · the dated lanes' keys and labels collided at 390 px — keys cluster at 4 % of the axis,
  a short infrastructure span labels outside itself, the axis is padded, and below 600 px the lanes become the dated
  lists the contract prescribes · "ATMs" printed as "ATMS" (a governed value label in the rubric role took the
  uppercase transform) · a source-record link's accessible name dropped its visible date (Label in Name) · the "↗"
  locators were under 24 px, and the interaction record claimed a target-size assertion that did not exist — both the
  targets and the assertion now exist · the matrix's wide table was cut off in print — the fallback is now one
  two-column table per class, dimension by dimension, and nothing is declared wide · the English credit line and the
  English governed time boundaries carry `lang="en"` in Arabic frames · a figure's inner headings sit one level under
  its title (they were `h3` everywhere) · the figure's accessible name is its governed title, not the 300-word alt
  text · a table's region is focusable only when it can scroll · a marker every valued row carries stands once in the
  caption; the FINDEX gaps and the lanes' rows sit in their own row groups with their own header · every object card
  carries its governed period and state · the social card's clocks and boundary never fall under 20 px at 1200 px
  (the title gives way instead) · print: a boundary no longer pulls a page break into the answer before it, a depth
  figure stays with its rubric, orphans and widows are limited, the search block does not print, every line and rule
  is black, the provenance block is the last thing on the page (it moved into the footer), and the D1 print rules that
  D6 restated are gone · compact-object ids restart on every page (deterministic output whatever the route order) ·
  one text layer (`yfie/text.py`) for escaping and isolation in every renderer.
- Recorded, not changed (content or authority — `ESCALATIONS.md`, D6): the credit lines that name a publisher twice or
  ambiguously; "Measured in a survey" over price quotes; VIS-PAYMENT-RAILS' alt text naming an amendment its event set
  lacks, and its lack of a credit; the step mapping that lets a network-activity statement evidence OPERATION; the
  eight VIS-FIRM-CONSTRAINTS rows the contract names but does not resolve; the CBY-Aden reporting scope that the POS
  contracts' universe carries but the Readings' universes do not; the meta descriptions that restate the title and one
  that is a tool instruction; a governed neutral column header for values of mixed units.
- Rejected: hiding the fifth class until its label exists (the missing≠zero failure the matrix exists to prevent);
  the en-dash range form for the break ("2024–2025" reads as a span); the contract's mobile form of the time series
  taken literally at 390 px (three governed state labels do not fit a 290 px panel without overlap; the key directly
  under the plot carries them there, and the labels return from 480 px of container width); a definition list as the
  matrix fallback under 900 px (the per-class tables serve every width without a second structure); a second table
  structure for narrow widths anywhere.
- Genericity (DEBT-007): the visual lens's verdict — not a template, an editorial identity: the frame anatomy repeated
  on thirteen figures, the one boundary voice inside the drawings, the plaster inset, hairline discipline, tabular
  numerals and the mark vocabulary carry it; the marks themselves and the type face do not. The remaining levers are
  precision and rhythm, which this entry's fixes serve; no motif, border, map or image (Lock §4.2).
- The Arabic lens (received last, on the corrected tree; the figures, the D6 forms, the exports, the social cards and
  the print pages). Found and fixed: plain numeric ranges in governed Arabic prose swapped their ends and broke at the
  dash (isolation extended from dates to ranges by one pass over every document, DL-D6-004); the matrix's per-class
  table and the chain tables squeezed their row-header column to its narrowest word (a placeholder heading may break
  anywhere, so the column has a 7 em floor); Latin joiners inside Arabic cells (the Arabic semicolon and comma in the
  Arabic edition — punctuation, never a word); "11.9 % من البالغين" with the sign on the wrong side of its digits (a
  value and its "%" are one isolate, closed, as the governed prose writes it); the "↗" locator alone on a line (bound
  to its word by a no-break space); a printed URL continuing at the far right of an Arabic paragraph (its own
  left-to-right line under the link); the projection labels touching (the ink-box placement, DL-D6-005); the Arabic
  state labels touching in the band (rows 15 px apart). Stale when read: the matrix clipped at 390 px (fixed before
  the lens read; the fit test now reads both edges). Recorded, not changed (`ESCALATIONS.md`): the Compare table's
  reversed dates — the runtime renders that table, untouched by Design, and the fix is the isolation the reference
  applies (a Code item with its patch); count nouns after values, the invariant plural, the comparator island, two
  terms for index, a header label carrying a colon, English-only credit lines. Rejected: mirroring "↗" for Arabic (part
  of the open cue escalation); a heavier Arabic rubric (it is SemiBold 600 like the English; Bold is not declared);
  keeping Latin phrases in Arabic titles on one line (DEBT-017, for D7's audit).
- The D4 gate on the corrected tree (904 renders) found one regression D6 had introduced — the unbreakable identifier
  isolate (DL-D6-004) — and passes after the fix; the D2 and D3 gates, the journeys, the trio and the repository suites
  pass unchanged (DL-D6-006, the verification numbers).
