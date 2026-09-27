# Repository Change Log

## 2026-09-27 — Design D1 (in progress): convergence on T4 · Instrument after the nine-lens critique

Same branch and pull request. Nine independent critique lenses (evidence researcher, Arabic/RTL director,
accessibility, data visualisation, frontend architect, product-design critic, journalist, source institution,
informed Yemeni reader) reviewed the same renders of T1–T4 under one brief (`design/exploration/d1_canvas/LENS_BRIEF.md`);
their findings, the adjudication, the corrections applied to T4 (composer and canvas version 5), the adversarial
tests and the convergence decision are in `design/01_FOUNDATIONS.md` §3 and decision DL-D1-006
(`design/00_DESIGN_README.md`). T4 converges as the D1 direction on two rendered behaviours (a same-year restatement
that cannot read as a fall; a number never met without its clock and bound). Records: `DESIGN_DEBT.md` (DEBT-005
closed; DEBT-006…008 opened), `ESCALATIONS.md` (four D1 items raised: Arabic credit line, Home pacing marker, IMF lane
state question, in-page navigation label), `COVERAGE.csv` (28 stress-trio rows `DESIGNED`; nothing `BUILT`),
`09_CODE_HANDOFF.md` (D1 implications). No governed content changed; one shared renderer formatting fault
("6245" without a separator in fallback tables) fixed in the composers. Still to come in D1: the Design Intent Lock,
`02_TOKENS.json`, the reference implementation of the trio, the Design and independent reviews.

## 2026-09-27 — Design D1 (in progress): thesis exploration recorded — neutral harness, four canvas propositions

First D1 milestone on `claude/practical-cray-sr26c5` (base `8bf19ef`, D0 accepted; the branch name is a process note
in `design/ESCALATIONS.md`). Nothing outside `design/` changed except this changelog, one row in the README status
table, one ignored output folder in `.gitignore`, the manifest and checksums; Master `17db032b…`, Page Specs
`d4574804…`, projections, contracts and `dist/` unchanged. Added: `design/01_FOUNDATIONS.md` (the baseline critique,
thesis hypotheses T1 Register / T2 Argument / T3 Strata and the second-generation T4 Instrument, the exploration
protocol, the benchmark result — every product site NOT INSPECTED — the sequencing process note, the designer's own
critique; comparison, Lock and grammar not yet written); `design/reference/` (the one content path from
`site-src/content/**`, an unstyled harness with every brief §19 hook, a content-parity check against `dist/`);
`design/exploration/d1_canvas/` (the composers that regenerate the four propositions on the Claude Design canvas from
the harness bundle; outputs git-ignored). Updated: decision log DL-D1-001…005, `DESIGN_DEBT.md` (DEBT-003…005),
`COVERAGE.csv` (the 28 stress-trio rows `REVIEWED` with evidence; nothing beyond `REVIEWED`), `09_CODE_HANDOFF.md`
(state at D1). No thesis chosen, no Design Intent Lock, no design system; not PUBLIC RELEASE READY. Gates run for this
commit: `checksums.py --check`, `generate_projections.py --check`, `validate.py`, `repository_manifest.py --check`,
`design/reference/check_content.py`; the browser suites run in CI against `dist/`, which did not change.

Same day, later push: T4 revised after a native-size inspection at 320–1440 px in both languages (four design defects
fixed — the illegible signature panel, the 900–1200 px grid, the mobile question strip, dropped SVG value labels —
recorded in `design/01_FOUNDATIONS.md` §2.5); inspection, tiling and crop tooling added under
`design/exploration/d1_canvas/`; a paper scaling test of the candidate grammar against the fixed sitemap (§2.6). No
thesis chosen; the lens critique is the next step.

## 2026-09-27 — Design D0: steward verification recorded in the Design README

`design/00_DESIGN_README.md` still read "awaiting steward landing" and left direct authority verification to the
steward after D0 landed (`7c9b8a1`). Its status line, a steward verification note under §2 (direct Master and Page
Specs SHA-256, both matching; every `CONTRIBUTING.md` §5 gate green) and a steward line under DL-D0-001 now record
this, in line with DEBT-001 (CLOSED). Claude Design's own statements and reasoning are unchanged. No file outside
`design/` changed except this changelog, the manifest and checksums.

## 2026-09-27 — Design D0: orientation records landed

Claude Design's D0 hand-back, landed by the steward on `design/d0-orientation` (base `6d954c1`) because the Design
environment cannot write to the repository (its statement: `design/00_DESIGN_README.md` §7). Files, as delivered:
`design/00_DESIGN_README.md` (authority, no supplied visual board, dependency map, D0 comprehension, plan D1–D7 with three
named theses — Register, Argument, Layers — and the decision log DL-D0-001…003), `design/COVERAGE.csv` (1,389 rows, all
`NOT_STARTED`, each with its planned gate), `design/DESIGN_DEBT.md`, `design/ESCALATIONS.md` (none raised),
`design/09_CODE_HANDOFF.md`. Steward additions only: DEBT-001 closed with the gate evidence (direct Master and Page Specs
hashes match; every `CONTRIBUTING.md` §5 gate green) and a confirmation of the start commit in the escalations' process
notes. No file outside `design/` changed except the manifest and checksums.

## 2026-09-27 — Design-enablement control pass (directive D9)

The last repository-control pass before Claude Design, on top of `937bf80` (post-F9 correction). Commit subject
`docs(handoff): design-enablement control pass — kernel, loop, memory, debt, review tests`; the checkpoint tag
`checkpoint/design-handoff-ready` belongs on that commit — the state Claude Design starts from. No Master, projection,
contract or public-page change: Master `17db032b…` and Page Specs `d4574804…` unchanged; `dist/` unchanged. Second
addendum in `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`.

The handoff was checked against a quality doctrine for a cold Design recipient. Where it already held, it was kept;
where it was partial or absent, it was strengthened in place — one start file, one brief, no second programme:
- **Brief §0:** a re-readable kernel; a nine-step loop (orient, question, explore, challenge, decide, prototype, test,
  persist, continue); the repository as memory (what to re-read at every gate start, what to update, test, commit and
  push at every gate end); the Code recipient test that closes every gate.
- **Brief §1, §4.6, §5, §6:** a public evidence service, not a generic website; the connected evidence system from bound
  relationships only; two firewall additions (infrastructure ≠ outcome; one lineage repeated ≠ independent
  corroboration) and a rule that layout must protect the distinctions; states that must not collapse; the full list of
  design freedoms and who owns what (Design, Code, owner, release, the Master).
- **Brief §7:** tone; a wider avoid-list; motion, imagery (with a provenance and rights checklist) and dark-mode decision
  logic; four review tests (anti-template, source owner, screenshot misuse, portable evidence).
- **Brief §9:** the small surfaces; "a template applied is not a reviewed page"; twelve audience lenses; §9.4 outcomes
  per family, including a Home cold-reader test at about 30, 90 and 180 seconds.
- **Brief §10, §12, §13, §15:** search as a product; external links; reporting intents and a rule for every input
  (the site collects and submits nothing); per-object download formats, Arabic exports, the four kinds of material and
  data packages (all still disabled until OWN-04, REL-02); micro-interactions; interaction in visuals never
  hover-only; Arabic tested, not only viewed; low bandwidth and an optional, honest footprint note.
- **Brief §19–§20:** decision-log fields; the coverage ledger's status ladder (`REVIEWED` … `ACCEPTED`) with `checks`
  and `code_handoff`; the design-debt register `design/DESIGN_DEBT.md`; four layers kept apart; what a hostable static
  site contains; gates with entry, work, exit evidence and stop conditions; the last-10-percent audit at D7.
- **Criteria, contract, start file:** acceptance section K (review tests, last 10 percent, Code recipient test) and
  matching lines in B–J; the Design-to-Code contract maps design debt and names the four layers; the Code prompt reads
  the debt register, ledger and escalations; README_FIRST points to the kernel and memory rule.
- **Independent cold-reader audit** (a fresh agent, read-only): verdict that a cold Design agent can run D0–D7 from the
  repository alone, every doctrine area present; its defects fixed here — evidence is committed as PNG, never PDF (gate
  F6-G07); a NOT RUN rule when an environment cannot install Chromium; who counts as a cold reader; the hand-maintained
  Design-to-Code flow diagram brought to D0–D7 (and its clipped label fixed); the manifest palette labelled a
  hypothesis; the identity constraints named; `docs/DEPLOYMENT.md` headings cited exactly; README_FIRST points to the
  brief's full freedoms list and says `design/**` is already classified.
- **Records:** directive D9 stored verbatim; README, checkpoint (tag target), Context, audit index and directives index
  updated.

## 2026-09-27 — Post-F9 correction: OWN-07, OWN-08, Design handoff tightened

One bounded correction on top of `03bd654` (F9), before Claude Design starts. Commit subject
`fix(handoff): post-F9 correction — OWN-07, OWN-08, handoff tightened in place`; the checkpoint tag
`checkpoint/design-handoff-ready` belongs on that commit. No Master change: Master `17db032b…` and Page Specs `d4574804…`
are unchanged. Addendum in `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`.
- **OWN-07 closed.** `/remittances/` binds MA-001 but its presentation contract allowed zero Measurement cards; the limit
  is now 1, and the card renders in both languages with its household-receipt scope (receipt, channel, frequency), kept
  apart from the macro remittance evidence on the page.
- **OWN-08 closed.** `navigation_interaction.json` now matches the governed copy, the Page Specs and the tested
  behaviour: Report an issue opens Contact (`?record=`) with its `UI-*` label; a Reading's breadcrumb ends on its title;
  Compare names its six dimensions, four assessments, the same-record state and the outside-set error; the workbench and
  Compare take only public records and the governed comparable set (Evidence Passports are never rendered); the sparse
  state is `/evidence/CLM-004/`; the institutional and vintage states are stated as the pages show them; J10 runs record
  → Contact → Corrections.
- **Controlled contracts named.** The two hand-maintained contracts form their own manifest class, `CONTROLLED_CONTRACT`,
  with a maintenance rule in the file, in `AGENTS.md` rule 2 and in `CONTRIBUTING.md` §2: the steward changes them in a
  commit naming the finding; Design and Code escalate.
- **Handoff tightened in place** (one start file, one brief). D1 tests two or three materially different design theses
  on Home, `/evidence/CLM-003/` and the flagship Reading `/readings/same-year-different-number/`, in both languages,
  before anything is propagated; a decision log and a coverage ledger (`design/COVERAGE.csv`) are kept at every gate; D0
  records whether a visual board or mockup was actually supplied (nothing absent binds). D7 requires the runnable, fully
  populated bilingual reference site; a design source alone is an incomplete hand-back; `⟦NCC:…⟧` markers are for
  development only and every shipped label must be in the Master, or its feature stays unshipped.
- **Print and portable evidence.** Page and Reading print styles, contextual chart and table exports, provenance that
  survives detachment and a Reading print/PDF layout, in the brief, the acceptance criteria and the Design-to-Code
  contract; every CauseWay-content download or export ships disabled until the licence decision (OWN-04); reporting
  stays the static Contact route (no backend, address, SLA or form).
- **Fonts.** The loading wording now matches `vendor/fonts/README.md`: self-host the files as shipped, load efficiently,
  IBM's own pre-split subsets only through the steward, no self-made subset without the owner.
- **Records.** Register 47 items (OWNER_INPUT 6), zero DESIGN_BLOCKER; the checkpoint states that the external
  repository is deliberately untouched lineage (no sync owed) and why F9 reported 753 files and the delivered archive 754;
  README rewritten around the current state and the owner actions.

## 2026-09-26 — F9: DESIGN HANDOFF READY

Record `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`. R8.6 is closed and directive D7 is complete. Three cold recipients found
no blocker; the archive, extracted into an empty directory, passes every gate; the register holds 49 items with zero
DESIGN_BLOCKER. The start file, the Design brief, `README.md`, the checkpoint, the Context and the handoff manifest now
read DESIGN HANDOFF READY (gate R86-G01); the Code prompt still waits for the accepted Design package. Not PUBLIC
RELEASE READY. The owner pushes the signed tag `checkpoint/design-handoff-ready`; the package is
`Yemen_Financial_Inclusion_Evidence_DESIGN_HANDOFF_READY.zip` (`git archive`, one root folder, never committed).

## 2026-09-26 — F9 (part 3): third cold-recipient run

A third fresh agent, on a clone of `b3c8e87`, asked whether it could carry Design from D0 to D7 without a question or an
invention; every command passed and it found no blocker, and 10 material points
(`audit/final_integration/inputs/F9_COLD_RECIPIENT_RUN3.md`). No Master change.
- **Fonts in the repository.** `vendor/fonts/`: the unchanged woff2 files and OFL licence of `@ibm/plex-sans@1.1.0` and
  `@ibm/plex-sans-arabic@1.1.0`, with provenance and the Reserved-Font-Name rule; class `VENDORED_FONTS`.
- **Visual contracts.** The POS charts' DISAGREEMENT note now comes from their own bilingual Evidence Records, not from a
  non-public passport.
- **Inventory 1.3.** Role STRUCTURE for the English-only relationships file; every question's destination (QE-001 lands
  on Home at `#system`).
- **Brief.** The Home evidence snapshot is Home section 3 as authored; governed text the baseline renders elsewhere
  (question-list introductions, the Reading thesis); the workbench keeps the embedded site search; every bound visual on a
  domain page has a place; chart-table and matrix headings and the matrix's English-only dated cells are pre-registered
  requests; full status and alert roles in the hook contract.
- **Register.** §7 restated precisely; three more items closed.

## 2026-09-26 — F9 (part 2): second cold-recipient run

A second fresh agent, on a clone of `3adf224`, passed every command, verified `YFIE_SITE_DIR` by planting defects, and
could start D0; it asked six questions and reported 9 material and 14 editorial points
(`audit/final_integration/inputs/F9_COLD_RECIPIENT_RUN2.md`). No Master change.
- **Page Specs.** The editorial rule now says governed wording is rendered exactly as authored; only the programme
  compresses it, Master-first (controlled input `page_spec_templates.json`).
- **Visual contracts.** A comparability flag no longer renders as an ungoverned UNKNOWN marker on two withheld values.
- **Inventory 1.2.** Home's starting questions and Explore's clusters, section counts per `section_order` with a flag for
  per-language rows, each domain route's verify destination in its next actions, and the visuals, grammar tokens and
  Readings at every hard-state route.
- **Brief, criteria, guides.** Where a visual lives (a `VIS-` record page is its canonical route); TABLE_TEXT_FIRST without
  rows; WITHHELD precedence; the full test-hook contract (suites are never edited by Design); the workbench without
  ungoverned facets; the vintage-conflict case; Reading labels quoted exactly; the domain Measurement rule; the Reading
  compare rule; Page Spec section structure; navigation labels' source; three more contract disagreements.
- **Tools.** In an archive without `.git`, the file walk honours `.gitignore`; the tools suite names the site directory
  it could not find; the architecture diagrams no longer name an external design tool or an analytics opt-in.
- **Register.** 49 items (EAD-11 added; EXT-10 and OWN-08 widened); seven items closed in F9.

## 2026-09-26 — F9 (part 1): clean-room corrections

A cold recipient (a fresh agent with only a clone of `main`) followed `handoff/README_FIRST.md`, passed every command and
could start D0 without asking; it reported 15 material and 10 editorial points where Design would have had to guess.
Record: `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md` (written at the close of F9).
- **Master (RF9).** The two language-switch labels still held in `scripts/build.py` moved unchanged into the governed
  interface copy (`UI-LANG-SWITCH-NAME`, `UI-LANG-SWITCH-ACTION`); the rendered site is byte-identical.
- **Inventory 1.1.** Collections of the index routes (comparable records, displayed and curated sources, chronology,
  Readings, Measurement, questions), each route's next actions, each Reading's bindings, the verification state each
  Evidence Record renders, the facts at every hard-state route, the presentation limit per domain route, and the role of
  every projection file (render, via Page Spec, contract, reference only). The runner now rewrites it after every build.
- **Visual grammar.** WITHHELD has a governed drawing rule; the narrow widths are 320 and 390 CSS px everywhere.
- **Brief and criteria.** Precedence Master → projections → the two hand-maintained contracts → baseline, with the five
  known contract disagreements and what to design to; the reference implementation builds to `design/reference/out/` and
  is tested with `YFIE_SITE_DIR`; the test hooks listed; Compare's governed dimensions, assessments and comparable set; the
  report path; the IBM Plex rule and packages; the date form; SUPPORTING visuals plot no values; named stress cases;
  labels Design is expected to request, with a placeholder convention; delivery without push access.
- **Tools.** The three suites take `YFIE_SITE_DIR`; the invariance check fails on an empty site directory; the repository
  manifest and the validator's file scan work from an extracted archive without `.git`.
- **Register.** 48 items (OWN-08 added for the navigation contract's stale fields); three items closed.

## 2026-09-26 — F8: R8.6 Design handoff freeze

Record `audit/R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md`; no Master change. State: **R8.6 FREEZE CANDIDATE — PENDING FINAL
CLEAN-ROOM ACCEPTANCE**.
- **One start path.** `handoff/README_FIRST.md` → `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` (rewritten from the current
  repository; the 22 D7 requirements; gates D0–D7; deliverables `design/00`–`10`). The Code prompt waits for the accepted
  Design package. Three superseded drafts retired to `audit/prior-review-records/handoff-drafts-2026-09-26/`.
- **New handoff files.** `DESIGN_ACCEPTANCE_CRITERIA.md` (A–J), `ENGINEERING_HANDOFF_EXPECTATIONS.md`, and
  `ROUTE_CONTENT_AND_STATE_INVENTORY.json` generated by `scripts/handoff_inventory.py` (143 routes, 12 hard-state cases,
  14 technical states, 13 journeys).
- **Open items.** `FINAL_OPEN_ITEMS_REGISTER.md`: 47 items in six classes, zero DESIGN_BLOCKER, built from a sweep of every
  earlier open item against the current bytes; README and checkpoint now point to it.
- **Pre-freeze corrections.** Stale "partial lineage" rationale on VIS-PAYMENT-RAILS corrected in the controlled visual
  contract input; the Design prompt names the governed source-type field and forbids CSS recolouring of the logo.
- **Discovery.** Open Graph and Twitter summary metadata from governed titles and descriptions (no image).
- **Gates added:** R86-G01…G04 (one recipient-start state everywhere; inventory current; exact handoff file set; every
  path a handoff document names exists). `design/**` is classified `DESIGN_PACKAGE`.

## 2026-09-26 — F7: sustainability baseline and stewardship note

No Master change.
- **Baseline.** `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`, measured with `audit/final_integration/f7_measure_baseline.py`
  (headless Chromium, local static server, 12 route classes × 2 languages, cold and warm, plus the Search interaction).
  The master logo (10 MB PNG, never redrawn here) is 96–99 % of every cold page; without it a page is 0.09–0.45 MB in
  four requests; warm loads transfer nothing; the search index (about 2 MB) loads only when Search is opened.
- **Method.** `docs/SUSTAINABILITY_METHOD.md`: what is measured, the system boundary, what is deliberately not done (no
  carbon figure, budget, badge or comparison before Design) and when to remeasure.
- **Stewardship.** `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` (not public, not a Design input): public-good proposition,
  editorial-independence covenant, conflict rules, cost categories, use and impact framework, partnership menu, rights
  boundary and a DPG gap assessment (not eligible today; nothing claimed).

## 2026-09-26 — F6: discovery, accessibility, rights, security and privacy (pre-Design)

Record `audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`; no Master change.
- **Discovery.** `scripts/discovery.py` (one implementation for build and validator): self-canonical, reciprocal hreflang
  with `x-default` (the root entry route), `robots.txt` (pre-release: no crawling), sitemap derivation for when the owner
  sets `public_origin` in `site-src/deployment.json`, JSON-LD (`WebSite`, `BreadcrumbList`, `Article` for Readings) with
  governed fields only — no author, dates, image or `Dataset`. 404 is `noindex`.
- **Strict CSP possible.** Page data moved from inline scripts to JSON blocks; the root redirect is `assets/lang-redirect.js`;
  no inline style, handler, external resource or form. Header expectations for Code in `docs/DEPLOYMENT.md`.
- **Accessibility contract.** Eleven WCAG 2.2 outcomes with what the reference build does now and what Design and Code
  must deliver; no conformance claimed.
- **Gates added:** F6-G01…G08 (titles, descriptions, H1, lang; canonical and hreflang; robots and sitemap; structured
  data; public-build security; secrets; bundled documents; rights and card state).

## 2026-09-26 — F5: whole public corpus acceptance

Transactions RF5 and RF5b (Master `440614d7…` → `168a0ad8…` → `ed3c5796…`); record
`audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`; every finding and decision in `audit/F5_CORPUS_FINDINGS_LEDGER.csv`.
- **Review.** Eleven reviewers read every governed public text (pages, Evidence Records, visuals, questions, Measurement,
  chronology, sources, interface labels, Readings) as Arabic, as English and for parity: 667 findings, all 57 material
  applied; 34 applied with Lead wording, 26 rejected under two house rulings, 3 deferred as open evidence checks.
- **Corrections.** Arabic scope qualifiers restored (CBY-Aden reporting scope, FPS areas, OECD/INFE representativeness,
  SFD provider universe); firewall errors fixed (full go-live, not located ≠ non-existent, ownership ≠ access, responses
  ≠ firms, exposure ≠ use); three unsupported periods corrected from the records' own sources; control language
  ("held", "locator", "universe", "vintage", "content version") removed; house terms applied.
- **Structure.** Chronology in date order (YSC-018); duplicate source record `SRC-WB-RPW-KSA-YEM-2025Q3` retired (source
  records 160, public locators 151, search records 435); citation line reads "Edition of 26 September 2026".
- **Tooling.** `run_stage.py` rewrites the repository manifest before validating; the public stylesheet no longer names
  the design tool.

## 2026-09-26 — F4: R8.5 canonical repository subtraction

Transactions R85-A and R85-B (Master `69899ae2…` → `2a7fd52b…` → `440614d7…`); closure
`audit/R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md`, 21-item ledger `audit/R8_5_SUBTRACTION_LEDGER.csv`.
- **Copy out of code.** 195 bilingual labels moved from `build.py`/`app.js` into the Master's governed interface copy
  (wording unchanged; 288 HTML identical apart from a JSON label block for `app.js`); Arabic Measurement domain labels
  moved to 10 `domain_ar`.
- **Copy corrections.** 404, corrections, answer-page disclosure, source-trace, data-directory and Compare wording
  rewritten without control language; the FMIIP crosswalk title no longer says "compared with".
- **Debt.** Duplicate reform events REF-PAY-010/007 merged into 006/013; `(1)` audit files resolved; P3-D02 labels
  fixed; Resource Library categories 16 → 6; Unicode NFC throughout the Master (32 cells).
- **Repository.** `FINAL_REPOSITORY_MANIFEST.json` classifies every tracked file (`scripts/repository_manifest.py`);
  `audit/INDEX.md` separates current records, standing policies and history; `docs/DEPLOYMENT.md` rewritten.
- **Gates added:** R85-G01…G09 (copy ownership, placeholder parity, NFC, authoring tokens, internal codes, private
  locators, Latin months on Arabic pages, manifest and index).

## 2026-09-26 — F3: five bounded Resource Library decisions

Transactions RL-F3 and RL-F3b (Master `caabff47…` → `69899ae2…`); record `audit/F3_RESOURCE_DECISIONS.md`.
- **Included (curated resource):** the September 2026 FinDev Gateway paper on supervising Yemen's microfinance banks
  (authors from Al-Amal Microfinance Bank; provenance and boundary stated on the card; no figures, no evidence binding).
- **Deferred:** IFAD *Sending Money Home 2026* (no verified Yemen figure; reopen only for a documented Yemen estimate, as a
  secondary lineage) and the World Bank Joint Food Security Monitor — Yemen (verified version 3 August 2026; its
  exchange-rate series need a governed record before any use beside nominal rial values).
- **Rejected:** the CPMI-IOSCO FMI cyber-resilience toolkit (consultative global guidance; no Reading or priority depends
  on it) and the Uzbekistan financial-inclusion index method (a composite index conflicts with the product's first principle).
- Counts: curated cards 28, source records 161 (152 with a public original locator), search records 436.

## 2026-09-26 — F2: Evidence Readings portfolio integrated (directive D7, sessions F0–F2)

OpenAI accepted the Tranche C checkpoint (recipient verification 31/31) and supplied the independent ten-Reading package.
F0 confirmed the verified entry state without re-running the handover programme. F1 adjudicated the package against the
Master and sources (`audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`, 60-row `audit/READING_PORTFOLIO_CHANGE_LEDGER.csv`).
F2 applied it in one Master-first transaction, RP-F2 (Master `f0150122…` → `caabff47…`; 494 cell writes and row deletions;
run report `audit/reading_integration/runs/RP-F2_RUN_REPORT.json`).
- **Readings.** Ten essays with new titles, standfirsts and bodies (4–7 sections each, the opening may run on without a
  heading), each ending "What would change this reading? / ما الذي قد يغيّر هذه القراءة؟", then the evidence path
  ("Trace the evidence / تتبّع الأدلة") and one or two related Readings. One signature visual per Reading. CWR-006's title
  changed to "What exactly do we mean by microfinance growth?" (the asserted growth failed the detached-quotation test).
- **Master structure.** 08 retires `domain_context_routes` (now `related_readings`) and adds `measurement_bindings`,
  `evidence_period_en/ar`, `last_reviewed` and `featured`; the generator checks every relation once
  (`derived.reading_relations`). A Reading's primary question now comes from 08, not from a shadow copy in the design-intent input.
- **Propagation.** Readings index (programme-owner definition, one featured Reading, editorial list — no card wall); Home
  featured Reading; Explore "Go deeper"; at most two Readings per answer page; Evidence Records "Used in these Evidence
  Readings"; Measurement Agenda "This gap is examined in"; search, meta and page specs regenerated; twelve new governed labels (04).
- **BIL-05 closed.** Every English/Arabic page pair prints the same numbers (6 held pairs → 0). The CI step no longer
  carries a held list; `audit/tranche_c/checks/bilingual_invariance.py` exits 1 on any difference.
- **Permanent gates RP-G01…G06** (validator): Reading ending and page order, one visual and no numbered template, one
  featured Reading everywhere, at most two Readings per answer page and "Used in" on bound records, retired Reading copy
  never reappears, bilingual invariance.
- **Gates.** Generator check and 21/21 tests; build 288 HTML from 143 Page Specs; literal audit 12,741 / 0 unresolved and
  deterministic under eight seeds; lineage 8/8; diagrams current; validator PASS 0/0; public tools 25/26 (1 n/a);
  viewport 168/168.
- **Status:** READING PORTFOLIO INTEGRATED — TRANCHE C ACCEPTANCE PRESERVED. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Canonical Git repository

The repository moved from a Drive folder and ZIP checkpoints to Git on GitHub (`CausewayGrp/Financial-inclusion-`,
branch `main`). No governed content changed: the Master, the projections and the public site are identical to the
Tranche C checkpoint, and no existing audit record was modified.
- **Baseline.** The first content commit is the exact tree of the ZIP under OpenAI review (SHA-256 `63612dea…`), tagged
  `checkpoint/tranche-c-complete-reading-hold` (signed); `sha256sum -c SHA256SUMS.txt` passes on the tagged tree.
- **CI.** `.github/workflows/verify.yml` runs every gate on each push to `main` and each pull request, including two new
  drift checks: the checksum manifest must list every tracked file, and the committed `dist/` and literal closure must
  equal a fresh build. `.github/workflows/checkpoint.yml` packages each signed `checkpoint/*` tag as a verified ZIP.
- **Owners.** `scripts/checksums.py` now writes and checks `SHA256SUMS.txt`; `requirements.txt` pins the Python 3.11
  toolchain; `.gitattributes` keeps every file byte-exact (CRLF ledgers included).
- **Protocol.** `CONTRIBUTING.md` (change protocol, branches, commit trailers, checkpoints, session sync, known pitfalls,
  repository settings), `AGENTS.md` and `CLAUDE.md` (agent rules). `docs/PRODUCTION_REPOSITORY_PROTOCOL.md` now records
  the move; `authority/AUTHORITY.json` names the canonical repository; the checkpoint names the reviewed tag.
- **Directives.** The programme directives D0–D6 are stored verbatim in `audit/directives/` (D6 current and binding).
- **Carried to R8.6:** the Design and Code prompts in `handoff/` must name the Git repository and the branch and pull-request
  protocol when they are finalised.
- **Status unchanged:** TRANCHE C COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE. R8.5 and R8.6 not
  started. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Tranche C: whole-product adversarial acceptance

Ten Master-first transactions (TC-S1, TC-A…TC-I) through the transactional runner; closure in
`audit/TRANCHE_C_FINAL_ACCEPTANCE.md`, ledger in `audit/TRANCHE_C_FINDINGS_LEDGER.csv`, currentness cut-off (26 September
2026) in `audit/FINAL_CURRENTNESS_CUTOFF.md`.
- **Panel.** 224 findings from nine lenses plus 5 from the bilingual-invariance test; all 9 BLOCKERs closed; 212 FIX,
  8 NARROW, 2 evidence frontiers, 3 release-only dependencies, 3 scheduled for R8.5, 1 held for the Reading package.
- **Bilingual parity.** 28 page-section pairs re-authored to the accepted content (TC-H); chronology dates now render in
  the page language (TC-I); the Arabic /payments/ title now gives the answer.
- **New checks.** `audit/tranche_c/checks/viewport_acceptance.py` (168/168) and `bilingual_invariance.py`.
- **Status:** TRANCHE C COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE. R8.5 and R8.6 not started.
  Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Pre-Tranche-C P5: independent-acceptance corrections

The P1–P4 hand-back was independently accepted with three narrow corrections, all closed
(`audit/P5_INDEPENDENT_ACCEPTANCE_CORRECTIONS.md`):
- **P5.1, deterministic literal audit.** Reading-bound records are taken in governed binding order with ordered
  de-duplication; a regression test runs the audit under eight `PYTHONHASHSEED` values and requires identical bytes.
- **P5.2, REF-PAY-001.** New source record `SRC-CBY-DEC-23-2024-001` for CBY Governor's Decision No. 23 of 2024 on
  domestic money-transfer activity. VIS-PAYMENT-RAILS is bound to it and the RV-CWR-009 release blocker is removed. The
  record is a rule, not evidence of implementation, use or outcome.
- **P5.3, RV-CWR-001 panel 2.** The CBY Annual Report 2025 remittance values for 2021–2023 were added Master-first as
  their own publication vintage. The panel shows the CBY and IMF paths indexed to 2021 = 100 as two separate lanes, with a
  generator guard, and is no longer blocked on data.
- **Controls.** The transactional runner now also snapshots and restores the checkpoint and the architecture diagrams,
  and checks the diagrams. A current-state source-lineage truth test was added. The acceptance matrix now also runs the
  seed-determinism test, the lineage truth test and the diagram check.
- **Status:** PRE-TRANCHE-C ACCEPTED — READY FOR TRANCHE C. Tranche C not started. Not DESIGN HANDOFF READY; not PUBLIC
  RELEASE READY.

## 2026-09-26 — Tranche B execution and Pre-Tranche-C maturation (P1–P4)

- **Tranche B.** The Master-first patch specification was executed in five transactional stages (`audit/TRANCHE_B_EXECUTION_CLOSURE.md`).
- **P1, public truth and editorial integrity** (`audit/P1_PUBLIC_TRUTH_EDITORIAL_CLOSURE.md`):
  - inventory counts are now derived;
  - duplication was removed;
  - a public-identifier policy was set;
  - Reading verification paths were added;
  - held additions were disposed;
  - chronology assurance was completed.
- **P2, tools and discovery** (`audit/P2_TOOL_DISCOVERY_CLOSURE.md`):
  - Compare has URL state;
  - governed search aliases and a canonical probe (60/60) were added;
  - the tool contract sweep was completed;
  - an accessibility baseline was set (no conformance claim);
  - 26 browser behaviour tests were added.
- **P3, visual design readiness** (`audit/P3_VISUAL_DESIGN_READINESS.md`):
  - all 36 visual contracts are tiered;
  - a semantic visual grammar was defined, with 33 governed labels;
  - data contracts exist for the SIGNATURE and CORE visuals;
  - contract truth corrections were made Master-first.
- **P4, canonical handoff alignment** (`audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md`):
  - one current-state story;
  - one Reading truth: the Reading index holds no copy, and the generator stops if text is written into it;
  - a bilingual boundary structure (does not establish | limits of the measure);
  - design-prompt drift corrected, with the prompt still DRAFT;
  - hygiene;
  - two independent verification rounds resolved Master-first:
    - the publication firewall now covers producer names, withheld values and shipped payloads;
    - 109 governed bilingual chart labels and in-frame lines;
    - text-first visuals no longer describe drawings;
    - Arabic terminology and grammar corrections;
    - architecture diagrams derived from the navigation contract.
- **Status:** PRE-TRANCHE-C MATURATION COMPLETE — READY FOR INDEPENDENT ACCEPTANCE. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-23 — S06 recipient acceptance + deterministic handoff freeze

- Closed S06.3 and completed independent recipient-side S06 acceptance: **S06_WINDOW_ACCEPTED**.
- Detected a newer live Production Master revision during acceptance and treated it as a concurrency event rather than restoring an older hash.
- Source-owner adjudication retained the newer `21_MFI_DATA` treatment for SFD Q4-2011: end-Dec-2011 narrative (~64,000 borrowers; 87,000 savers; YER 4,030m portfolio) versus a table headed end-Dec-2010 (63,568; 87,615; YER 3,853m). The portfolio/time-series point is now a preserved conflict, not a clean 2011 anchor.
- Regenerated the affected MFI local shard and rebound all 141 Page Specs to current Master SHA-256 `f94f1f91084b01964a3bb7b3847fd68a19555cc901ab6078146a187efe17e860`. New Page Specs SHA-256 `4e8a0d8f0cf58f78389360c69cf04f3bf0d24f1ba9b3e4ef10ebe93461e69f1a`; no public 2011 microfinance claim/copy changed.
- Reconciled stale S06 aggregate fields in the existing control stack and updated validator expectations to the accepted S06 boundary.
- Strengthened and froze the existing `handoff/` only; no parallel final package was created. Claude Design remains first recipient; Claude Code starts after a repository-backed design package exists.
- S07/S08 remain not started. `R-042`, remote webfonts and final named assistive-technology/deployed-runtime acceptance remain later release gates.

All material repository edits are recorded here. Evidence semantics are not changed directly in the website repository; any such change must originate in the Production Master and be regenerated.

## 2026-09-23 — Deterministic Claude Design → Claude Code handoff

- Added `handoff/` as a **non-authoritative** implementation handoff layer. The Production Master remains the sole semantic/evidence/source/rights/publication authority; Page Specs remain its controlled implementation projection.
- Added eight raw repository files: handoff entry/read order, Claude Design master prompt, design starting tokens, design-to-code contract, Claude Code master prompt, static-runtime/API contract, implementation manifest and acceptance checklist.
- Bound the handoff manifest to the live Production Master SHA-256 `d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e` and Page Specs SHA-256 `453bde9026c2a30f2c0c2125c0e950cd6e468a9540577318e1896c98e61959da`.
- Specified Claude Design as the first recipient and Claude Code as the implementation recipient after a repository-backed `design/` package exists; screenshots/chat history are not implementation authority.
- Defined one React static pre-render/export target with the accepted 141-route × 2-language + root + 404 = 284-document baseline and no required runtime Drive/database/CMS/API dependency.
- Identified one implementation gap in the current baseline: `styles.css` imports webfonts remotely. The final code handoff requires packaging approved fonts locally before the static runtime can be called fully local.
- First-hand local reconstruction found one checksum-control drift: `docs/POST_BUILD_REVIEW_PROGRAM.md` had been modified after the prior `SHA256SUMS.txt`. The manifest is refreshed only after the complete handoff/control integration so one coherent checksum state is written.
- Final staged reconstruction after handoff/control integration: Python syntax PASS; JavaScript syntax PASS; 284 HTML built from 141 Page Specs; validator `ERRORS=0`, `WARN=0`; checksum coverage expanded to 78 canonical files.
- No evidence value, claim, source state, rights state, publication state or controlled public wording was changed by this handoff work. S06.1 remains not started.

## 2026-09-22 — S00/S01 opening integration

| Area | Edit | Why it changed | Authority impact | Verification |
|---|---|---|---|---|
| Repository control | Added `POST_BUILD_REVIEW_PROGRAM.md`, `REVIEW_LEDGER.json` and this log. | Make the post-build work finite, inspectable and repository-local. | None. | Files present; included in checksums. |
| Authority documentation | Corrected repository metadata so it no longer claims the Production Master workbook is bundled when the repository only carries its hash and frozen projections. | Previous metadata contradicted the actual ZIP contents. | None; Master authority strengthened. | Repository file inventory checked. |
| Handoff state | Replaced stale “design/implementation not started” state with actual static-first implementation state and remaining acceptance boundary. | The prior handoff state was inherited from an earlier package and no longer described this repository. | None. | Metadata compared with generated `dist/`. |
| Mobile navigation | Corrected the small-screen CSS/interaction conflict that hid the mobile menu button at ≤640px; added explicit open/close state and `aria-expanded`. | At phone width the nav was hidden and the control that should reopen it was also hidden. | None. | Static CSS/JS review + validator assertions. |
| Global search | Added an accessible global search dialog available from every page while retaining the Evidence-hub search. | Search was described as a global utility but the header button only routed to the Evidence page. | None; public search index remains the only search payload. | Search controls and public-index checks added. |
| Governed object rendering | De-duplicated governed objects by stable ID; correctly reads public `summary_*` and `limitations_*` fields; suppresses empty evidence cards; adds “Open evidence record” links when a controlled detail route exists. | The generator was dumping overlapping reference arrays, producing duplicate IDs and many empty public cards despite the Page Spec rule that governed arrays are reference payloads, not blocks to dump verbatim. | None; render-only correction. | Post-build HTML density/duplicate/empty-card audit. |
| Compare UX | Added localized comparison field labels and horizontal scroll containment for narrow screens. | Improve comprehension and mobile usability without changing comparison semantics. | None. | Static generation and route smoke checks. |
| Focus/touch behavior | Added visible `:focus-visible`, 44px control minimums and accessible dialog behavior. | Keyboard/mobile usability baseline. | None. | Validator + manual DOM/CSS review. |

## 2026-09-22 — Canonical Drive folder conversion

- Established a single non-ZIP Google Drive production repository and a separate non-production reference/archive inbox.
- Added `docs/PRODUCTION_REPOSITORY_PROTOCOL.md` to define production authority, editing, handover and release rules.
- Consolidated the 141 Page Render Specifications into `site-src/content/page_specs.json` to keep the Drive repository first-hand, clean and practical for other developers/AIs while preserving all controlled specifications.
- Updated build and validation scripts to consume the consolidated Page Specs deterministically.
- Rebuilt the site and re-ran validation: 284 HTML files generated; `ERRORS=0`, `WARN=0`.
- ZIP handoff files moved out of the production root into the sibling non-production archive; ZIPs are no longer the working repository.

## 2026-09-22 — S01 deep review and reference challenge

| Area | Edit | Why it changed | Authority impact | Verification |
|---|---|---|---|---|
| Drive structure | Moved production and reference folders out of the superseded archive path so both now sit directly under `My Drive / Ready`. | The active repository should not live beneath a folder named superseded. | None. | Drive parent IDs checked after move. |
| Source journey | Added a bilingual Data source directory and query-aware focus for `/data/?source=<ID>`. | Global search previously resolved source results without taking the user to the named source. | None; uses only current `source_reference_map.json`. | 148 public-addressable source records rendered per locale from a 149-record controlled map; the one no-public-locator dependency is suppressed; every source search result maps to an existing source anchor. |
| Source metadata firewall | Full cards are limited to the 6 controlled display-ready sources; 142 locator-only entries with a public URL expose only stable source ID and original locator; the one controlled dependency without a public locator is suppressed. | Prevent bibliography/publisher/licence invention for locator-only records. | None; render policy tightened. | Validator blocks internal source-state leakage and checks source anchors. |
| Search UX | Added localized result-type labels, live loading/result/error status and focus return on dialog close. | Improve first-use comprehension and keyboard behavior. | None. | JS syntax + validator assertions. |
| Search result quality | De-duplicated identical title+route results before the top-ten limit, preferring the substantive non-page record when the index contains both a Page Spec and its evidence object. | The controlled index legitimately contains multiple object types, but the UI should not show the same public destination twice. | None; index remains unchanged. | Deterministic search stress test documented in `S01_TASK_STRESS_TEST.md`. |
| Navigation semantics | Added `aria-current="page"`, Escape-to-close and resize reset for mobile navigation. | Improve assistive-technology and keyboard navigation state. | None. | Validator checks active top-level nav; JS syntax PASS. |
| Error recovery | Replaced the minimal English-only 404 with a calm bilingual recovery page linking Home, Explore and Evidence and exposing search. | Avoid dead ends from stale/shared links. | None. | Validator checks bilingual 404 recovery controls. |
| Arabic public language | Replaced the homepage phrase `ساعات أدلة مختلفة` with `اختلاف توقيت القياس`. | Use natural public Arabic rather than backend/evidence-management jargon. | None; wording preserves meaning. | Generated Home inspected. |
| Reference archive | Added `S01_REFERENCE_CHALLENGE.md`; inventoried new archive additions and adjudicated high-leverage drafts by cohort. | Use old work objectively without allowing recency/version labels to become authority. | None. | Material dispositions and authority collision logged. |
| Authority collision control | Quarantined the archive workbook named `...Master_FINAL.xlsx` after its hash (`91ed...`) did not match the production authority hash (`d8db...`). | A “FINAL” filename must not override the controlled Master identity. | None; production authority protected. | SHA-256 comparison recorded in review ledger. |

- Added `docs/S01_TASK_STRESS_TEST.md` to record first-use search/navigation/source-completion tests and the limits of static acceptance.

- **Generated-output tracking:** `dist/` remains reproducible deployment output and is not a canonical tracked source in Drive. `npm run verify` regenerates it from first-hand inputs; repository checksums cover tracked source/control inputs only.

## 2026-09-22 — S01 final reconciliation and closure

- Re-opened the latest live Drive source files before writing so the S01 closure did not overwrite newer repository work.
- Added the missing first-hand controls `docs/S01_REFERENCE_CHALLENGE.md` and `docs/S01_TASK_STRESS_TEST.md`; the validator had already named them, so their absence was a repository-truth defect.
- Completed objective disposition of the newly populated `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION`: implementation-safe lessons integrated; stale route/runtime/design authority rejected; factual/source/rights candidates quarantined for Master-led review.
- Preserved the current 149-record controlled source-map model and 148 publicly addressable source records rather than replacing it with a parallel source payload.
- Strengthened Arabic search normalization, stable-ID search weighting, keyboard search access, and mobile-menu dismissal behavior.
- Replaced the public English phrase `Different evidence clocks` with `Different measurement dates`; retained the approved Arabic `اختلاف توقيت القياس`.
- Added validator regression checks for prohibited backend Arabic wording and ZIP-as-working-repository language.
- S01 remains an implementation/first-use milestone, not a live-release certification.
- Removed the stale Drive `dist/` tree from canonical storage. `dist/` is deterministic generated output and must be rebuilt from first-hand source with `npm run verify`; this prevents source/build drift inside the Drive repository.

## 2026-09-22 — S01 archive refresh and control cleanup

- Re-inventoried archive additions uploaded after the initial S01 pass, including two authoritative-looking workbooks, the critical evidence review, corpus inventory, evidence-synthesis delta, citizen-journey prototype, universal/master build prompts and predecessor frontend/system-architecture specifications.
- Hashed both archive workbooks and confirmed neither matches the controlled Production Master; recorded the collision in `REVIEW_LEDGER.json` and `S01_REFERENCE_CHALLENGE.md`.
- Explicitly quarantined new factual/literature propositions for S06 rather than changing production semantics from the archive.
- Retained useful challenge principles (question-first hierarchy, screenshot-safe scope, negative-search discipline, source no-invention) without importing predecessor factual claims or architecture.
- Removed the redundant `REFERENCE_ARCHIVE_REVIEW_S01.md` control and consolidated the archive review into the single authoritative S01 review document `S01_REFERENCE_CHALLENGE.md`.
- Rewrote `S00_S01_REVIEW_REPORT.md` to remove stale source-index/deep-link statements and align counts with the current controlled source-map implementation.
- Restored and tightened `PRODUCTION_REPOSITORY_PROTOCOL.md` in the first-hand source tree; generated `dist/` remains noncanonical and reproducible with `npm run verify`.
- Updated `FINAL_RELEASE_VERIFICATION.md` so it no longer implies that S01 equals a final live-release decision.

## 2026-09-22 — S01 exhaustive archive disposition and single-source closure

- Completed a point-in-time review of all **70** current top-level items in `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION`.
- Added `S01_ARCHIVE_DISPOSITION_REGISTER.json` so every archive item has an explicit non-production disposition and rationale.
- Added `S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md` to isolate potentially valuable factual/source propositions from implementation work; all entries remain candidate-only until original-source and Production Master adjudication.
- Inspected `evidence.zip`: 330 entries, CRC clean; classified as generated predecessor output rather than source.
- Verified the archived CauseWay logo is byte-identical to the production asset; no asset change required.
- Explicitly rejected synthetic econometric/model payloads, obsolete route manifests, blanket-rights assumptions and old implementation PASS manifests as production inputs.
- Strengthened the validator so the S01 archive register/queue are required and public HTML fails on broader legacy architecture/vendor leakage (`YFSI`, `BAYAN`, old framework terms).
- Logged the remaining Drive cleanup defect: generated `dist/` must be removed from canonical Drive storage after first-hand source synchronization.

## 2026-09-22 — S01 Drive canonical-state verification

- Deleted the stale generated `dist/` folder from the Google Drive production repository; the canonical Drive root now contains only `README.md`, `package.json`, `SHA256SUMS.txt`, `docs/`, `scripts/` and `site-src/`.
- Removed duplicate Drive copies of the S01/S06 control set (`S01_REFERENCE_CHALLENGE.md`, `S01_TASK_STRESS_TEST.md`, `S01_ARCHIVE_DISPOSITION_REGISTER.json`, `S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md`), leaving one canonical instance of each.
- Re-listed the reference archive after reconciliation and confirmed the S01 point-in-time baseline remains **70 top-level items** with no unreviewed delta.
- Recorded binary checks for `evidence.zip` (330 entries; CRC PASS), both authority-looking archive workbooks, and the CauseWay logo match.

## 2026-09-22 — S02 audience journeys and information architecture

- Added `docs/PROGRESS_INVENTORY.json` as the single programme-progress and archive-delta monitor.
- Added `docs/S02_AUDIENCE_JOURNEYS_AND_IA.md` with the audience/task tests, IA decisions and counterfactual deletion logic.
- Closed the S01 70-item reference archive baseline: baseline materials are not re-reviewed by default; only new/modified items or a specific defect-triggered challenge are reopened.
- Added a reviewed-baseline marker folder in the non-production archive for point-in-time control.
- Differentiated Home from Explore: Home now orients by five common tasks and four common direct questions; Explore retains all 11 controlled questions grouped by user job.
- Kept the six-item global navigation unchanged; rejected persistent audience-specific menus because they would duplicate routes and increase maintenance.
- Added S02 validator checks so Home cannot silently return to a full duplicate Explore grid and Explore cannot lose any of the 11 controlled entry questions.
- No archive-derived factual claim, source state or rights assumption was promoted into production semantics.

## 2026-09-22 — S02 verification closure

- Rebuilt all 141 controlled Page Specs into 284 generated HTML documents after the IA changes.
- Validation: `ERRORS=0`, `WARN=0`.
- Verified 5 Home task starts + 4 compact questions per language and all 11 Explore questions + 4 groups per language.
- S02 closed; S03 becomes the active review session.
## 2026-09-22 — Bounded-session execution protocol

- Added `docs/SESSION_EXECUTION_PROTOCOL.md` as the single detailed execution control for the remaining post-build programme.
- Split the remaining work into **16 finite sessions**, from S03.1 through S08.2, each with one exact achievement, one owner, no more than two challenger lenses and explicit exit evidence.
- Made end-of-session rationalization mandatory: what became more true, what became simpler/more usable, new complexity introduced, what can be removed/merged, and the smallest next material intervention.
- Added an explicit boundary decision at every session close: PROCEED, REVISE, ESCALATE_TO_MASTER or STOP.
- Reconciled `README.md` and `PROGRESS_INVENTORY.json` so **S03.1 — People + Access composition** is the only next active unit and **S08.2 — Final repository closure** is the programme end.
- No evidence, claim, source, rights or publication-state semantics changed in this control session.

## 2026-09-22 — S03.1 orientation control reconciliation

- Reconciled `docs/HANDOFF_STATE.json` with the already-controlled S02 closure: S00–S02 are complete and S03.1 is the only next active unit.
- Removed the stale `docs/SESSION_EXECUTION_MAP.md` reference from the post-build programme; `docs/SESSION_EXECUTION_PROTOCOL.md` is the single bounded-session control.
- Detected one post-S01 archive delta, the `Old drafts` pointer to the high-fidelity mobile-review mockups; reviewed it once and classified it **DESIGN_REFERENCE_ONLY**.
- Moved that pointer into `04_DESIGN_REFERENCES__REVIEWED`; no archive-derived fact, number, route, source state, rights state or evidence meaning was promoted into production.
- Confirmed `01_NEW_INPUTS__UNREVIEWED` is empty after the delta check.
- No Production Master correction was required by these control repairs.


## 2026-09-22 — S03.1 People + Access composition CLOSED

- Rebuilt `/people/` and `/access/` through an answer-first domain renderer in `scripts/build.py`, with route-specific density rather than mechanical page symmetry.
- Added the restrained S03 domain composition layer in `site-src/styles.css`: strongest-answer hero, adjacent scope/inference boundary, selected evidence/visual, progressive disclosure, Measurement Next and a deliberate Verify surface.
- Reduced the People route from a repeated 33-card evidence wall to three primary analytical sections plus progressive verification depth; preserved direct controlled evidence-record links for `CLM-001`, `CLM-002` and `CLM-025`.
- Made Access's missing national geography an intentional epistemic state: unknown is not zero, rosters/infrastructure are not operating access, and Measurement Next states what evidence would resolve the question.
- Preserved `site-src/content/page_specs.json` as the frozen semantic projection; no Production Master fact, denominator, universe, source, rights or publication state changed.
- Reviewed Arabic 390px/1440px and English 390px/1440px rendered composition; full browser/a11y acceptance remains correctly assigned to later sessions.
- Final S03.1 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Refreshed `SHA256SUMS.txt` for the accepted S03.1 source/control state and removed stale `scripts/__pycache__` checksum entries that did not correspond to files in canonical Drive.
- Boundary decision: **PROCEED** to S03.2.


## 2026-09-22 — S03.2 Firms + Finance composition CLOSED

- Extended the established answer-first domain renderer to `/firms/` and `/finance/` without changing controlled evidence semantics.
- Firms now keeps formal-firm survey scope, governorate coverage, variable-specific denominators and programme KPI/reach boundaries adjacent to the interpretation; programme evidence is not styled as representative firm prevalence.
- Finance now keeps stock/flow, nominal/real, valuation/source-vintage, provider/system-state and inclusion-outcome distinctions visible before deeper historical context.
- Added route-specific controlled visual placement so Firms and Finance share one product grammar without false visual equivalence.
- Arabic 390px/1440px then English 390px/1440px composition inspection found no horizontal overflow and preserved verification paths.
- Reference archive check: **NO NEW ARCHIVE DELTA**. No factual/source/rights proposition was promoted and no Master escalation was required.
- Final S03.2 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Boundary decision: **PROCEED** to S03.3. S03 remains ACTIVE; S03.4 plus the full eight-route closure gate are still required.


## 2026-09-22 — S03.3 Payments + Remittances composition CLOSED

- Extended the answer-first domain renderer to `/payments/` and `/remittances/` without changing the frozen semantic projection.
- Payments now foregrounds administrative-currentness, measurement-object distinctions and the infrastructure/use boundary; terminals, accounts, subscribers and transactions are not rendered as unique people or inclusion outcomes.
- Selected `VIS-PAYMENT-ANATOMY` because the object distinction prevents more misuse than another trend chart; POS contradiction/source-arithmetic evidence remains reachable through controlled verification.
- Remittances now foregrounds observed/estimate/projection state, same-year source revision, BOP/concept boundary and unresolved CBY↔IMF crosswalk; no universal conversion scalar is fabricated.
- Selected `VIS-REMITTANCE-MACRO`; did not invent a Measurement Next card because no governed measurement priority is bound to the current route.
- Arabic 390px/1440px then English 390px/1440px rendering showed no horizontal overflow; representative Arabic mobile and English desktop pages were visually inspected.
- Reference archive check: **NO NEW ARCHIVE DELTA**. No Master escalation.
- Final S03.3 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Boundary decision: **PROCEED** to the Window-1 independent recipient-side acceptance gate. **S03 remains incomplete** until S03.4 and the full eight-route S03 closure test pass.

## 2026-09-22 — Window 1 recipient-side acceptance — ACCEPTED

- Independently re-opened the live canonical implementation for S03.1–S03.3 rather than relying on session reports. Confirmed route configurations and generated composition for `/people/`, `/access/`, `/firms/`, `/finance/`, `/payments/` and `/remittances/` in Arabic and English.
- Rebuilt all 141 controlled Page Specs into 284 HTML documents and re-ran repository validation: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`; Python and JavaScript syntax checks also passed.
- Added a compact cumulative S03 regression set to `scripts/validate.py`: six-route answer-first structure, three-item scope/boundary band, selected visual, progressive disclosure, Verify surface, no return to `answer-card` governed-array dumping, AR/EN structural parity, and presence of every localized Page Spec narrative section in the generated route.
- Ran an independent deterministic render harness across 24 route/language/viewport combinations (six routes × Arabic/English × 390px/1440px). No horizontal overflow or structural parity defect was found. This is not a claim of final deployed-browser, assistive-technology, security or privacy acceptance; those remain assigned to later sessions.
- Confirmed the six-route composition retains complete narrative meaning while reducing first-load burden: all Page Spec narrative sections remain present either at first load or in explicit progressive depth; no semantic projection, evidence, source, rights or publication-state field changed.
- Reconciled control drift: `README.md`, `REPOSITORY_BUILD_SUMMARY.json`, `PROGRESS_INVENTORY.json`, `HANDOFF_STATE.json`, `SESSION_EXECUTION_PROTOCOL.md` and `REVIEW_LEDGER.json` now state one current position. R-005/R-006 are explicitly partial rather than falsely closed: the six accepted routes pass; Providers/Reforms remain S03.4 work.
- Confirmed canonical Drive root remains first-hand (`README.md`, `package.json`, `SHA256SUMS.txt`, `docs/`, `scripts/`, `site-src/`) with no stored `dist/`; the reference archive unreviewed inbox remains empty.
- No Production Master escalation was required. Master hash remains `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`.
- Boundary decision: **WINDOW_1_ACCEPTED**. S03.4 is next but **not started**; S03 remains incomplete until Providers + Reforms and the full eight-route closure gate pass.
- Final recipient-side acceptance audit confirmed every localized Page Spec narrative section remains present across all 12 accepted route editions; no generated substantive number was introduced outside the controlled route specification.
- Added validator checks that the core control stack agrees on shared Production Master hash, Page Spec count and generated HTML count, and that `REPOSITORY_BUILD_SUMMARY.json` / `SESSION_EXECUTION_PROTOCOL.md` remain required first-hand controls.
- Final verification after reconciliation: `npm run verify` built 284 HTML files from 141 Page Specs with `ERRORS=0 WARN=0`; Python/JavaScript syntax passed; deterministic render harness passed 24 route/language/viewport combinations with zero horizontal overflow; local HTTP smoke returned 200 for Arabic Home, English People, Arabic Payments, English Data and 404 recovery.
- Final integrity recheck found one stale manifest entry for the live frozen `site-src/content/page_specs.json`: the manifest still carried the predecessor projection hash while the live Drive file and S03 controls consistently resolved to `1319433fed3503cd7ad98203179db5a4a8438906e3e95464b80f36327497b41e`. The live projection was not changed; the checksum manifest was corrected and the finding closed as R-032.
- `SHA256SUMS.txt` was refreshed after control reconciliation; generated `dist/` remains excluded by policy.


## 2026-09-22 — S03.4 Providers + Reforms + full Domain Answer closure — CLOSED

- Rebuilt `/providers/` and `/reforms/` through the established answer-first Domain Answer grammar in Arabic and English.
- Providers now foregrounds authority, dated status and operation uncertainty; the 98 exchange companies, 225 individual exchange establishments and 106 remittance agents remain separate source-defined categories rather than a fabricated deduplicated current operating-provider total.
- Reforms now foregrounds the rule/funding → implementation/institution → operation → access → use → quality/protection → outcome chain and the furthest evidenced state; missing downstream evidence is not rendered as failure.
- Replaced the hard-coded six-route presentation hierarchy with one renderer-consumed `site-src/content/presentation_priority.json` contract covering all eight Domain Answer routes. The contract controls presentation depth only and cannot override Page Specs or the Production Master.
- Extended `scripts/validate.py` to enforce eight-route mapping, governed references, presentation-tier completeness, always-visible boundaries, direct Evidence Record resolution, AR/EN structural parity, narrative retention and renderer/contract binding.
- Counterfactual deletion / visual-economy decision: kept `VIS-PROVIDER-OBSERVABILITY`; added no first-load Reforms visual because the existing controlled visuals would privilege one reform subclass or imply false comparability.
- Arabic mobile review detected and fixed an unlocalized English visual-metadata leak; raw unlocalized English metadata no longer appears as Arabic UI.
- Render inspection covered Providers/Reforms at 390px, 768px and 1440px in Arabic and English. Clean build: 284 HTML documents; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Reference archive inbox: EMPTY. Master escalation: NONE.
- Boundary decision: **PROCEED** to S04.1. **S03 is CLOSED.**

## 2026-09-22 — S03.4 presentation-contract direct-consumption cleanup

- Removed the temporary derived `DOMAIN_CONFIG` compatibility layer after the eight-route contract migration; `build.py` now consumes `site-src/content/presentation_priority.json` through `PRESENTATION_ROUTES` directly.
- Strengthened `validate.py` to fail if `DOMAIN_CONFIG` reappears and to verify that contract-promoted governed objects are eligible for the route recorded in the controlled Page Spec projection.
- Rebuilt 284 HTML documents from 141 Page Specs and re-ran repository validation: `ERRORS=0`, `WARN=0`, PASS. No semantic/evidence/source/rights/publication change and no Master escalation.


## 2026-09-22 — S04.1 Evidence records + discovery / verification journey — CLOSED

- Replaced generic evidence-detail card rendering with a distinct Evidence Record page family driven by the existing canonical presentation contract. First load now exposes evidence identity, what it establishes, definition, universe, period/currentness, material limitation and source/verification action; method/change-trigger/verification guidance remains progressively available.
- Connected all four required entry paths: Domain → Evidence → Source → interpretation; Global Search → Evidence; direct Evidence deep link; and Data/source → dependent Evidence Record. No stable-ID knowledge is required to navigate the journey.
- Extended the existing Data/source directory only with dependent Evidence Record links; DISPLAY_READY/LOCATOR_ONLY behavior remains bounded and the one no-public-locator dependency remains suppressed.
- Extended `scripts/validate.py` across 108 Evidence Records for contract/renderer binding, governed-object/source resolution, first-load boundary, source-publication filtering, related/backtrack targets, AR/EN parity, search/deep-link resolution and Data/source dependencies.
- Hard-case verification passed across representative population survey, bounded firm survey, programme KPI, administrative payments, provider roster/status, reform/regulatory evidence, remittance observation/estimate/projection states and a derived visual object.
- S04.1 exposed a controlled Arabic public-language defect in CLM-060 (`وثائق المقام`). It was **escalated to the Production Master**, corrected to `وثائق قاعدة الاحتساب` at `06_EVIDENCE_OBJECTS!I112`, and the affected Page Spec/search projections were regenerated. Production Master SHA-256 changed from `d8db3b4e…` to `6c0f8f18…`.
- Clean build: 284 HTML documents from 141 Page Specs; validator `ERRORS=0 WARN=0`; Python/JavaScript syntax PASS; local HTTP smoke PASS. Browser screenshot automation was blocked by the execution environment, so S04.1 does not claim deployed-browser/accessibility acceptance; that remains in S05/S08.
- Reference archive unreviewed inbox: EMPTY. Boundary decision: **PROCEED to S04.2**; S04.2 has not started.

## 2026-09-22 — S04.2 Compare + publication/trust closure — CLOSED; Window 2 ACCEPTED

- Added a distinct `Comparison` family to the existing Canonical Presentation Contract and made Compare compatibility-first: governed definition/universe/geography/unit/period/method/source/currentness fields are assessed before a verdict; missing required metadata fails closed; no numeric values, averages, midpoints, preferred numbers or invented conversion scalars are produced.
- Closure regression found that the first Compare renderer exposed only two selectors while the controlled Page Spec permits 2–4 records. The renderer/client now provide two required plus two optional selections and one N-way compatibility verdict; validator enforcement was added.
- Removed the redundant generic governed-object card wall from Compare; the controlled object set remains available through the selector and Evidence Records.
- Added detached Evidence Record citation context carrying record ID, period, population/base, material boundary and public source IDs; added source-reference trace to Data/source.
- Added source citation controls and an explicit rights boundary separating public citation/factual use from redistribution. Current object-level/unspecified rights state is not promoted into permission.
- Added correction/current-record context without inventing correction/version events not governed by the controlled Corrections Page Spec.
- Fixed an indirect publication-filtering defect: `SRC-MOPIC-YSEU-2023-080`, which has no public locator, was visible as a source ID on a Reading sidebar. Shared source rendering now uses the public-source filter and the validator rejects any no-public-locator source ID in public HTML/search.
- Extended `scripts/validate.py` for Comparison contract/renderer binding, forced-reconciliation prohibition, detached citation safety, source rights/download gating, correction context, Source Reference Closure samples, DISPLAY_READY/LOCATOR_ONLY/NO_PUBLIC_LOCATOR behavior and global publication filtering.
- Clean build: 284 HTML documents from 141 controlled Page Specs; validator `ERRORS=0 WARN=0`; Python/JavaScript syntax PASS; six-route S04.2 HTTP smoke PASS; AR/EN 390px/1440px render harness PASS with no horizontal overflow; independent recipient task harness **143/143 PASS**.
- Page Specs and Production Master semantics were unchanged in S04.2. Master SHA-256 remains `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`.
- Reference archive unreviewed inbox: EMPTY. **Window 2 decision: ACCEPTED. S05.1 is next and has not started.**
- Canonical Drive reconciliation completed in place after Window 2 acceptance; build/validator sources, presentation contract, control stack and closure artifact were written to the existing production repository without creating a parallel copy. Production Master ID/hash were reverified and generated `dist/` remains excluded from canonical Drive state.
- Window 2 permission check found the canonical production folder is shared as anyone-with-link writer. Recorded as open release blocker `R-042`; no concurrent overwrite was observed, but final release certification is blocked until S07 restricts and re-verifies write access.

## 2026-09-22 — S05.1 Arabic/English semantic + typographic QA — CLOSED

- Closed bilingual semantic/typographic QA on a 21-route representative sample spanning Orientation, five Domain Answers, eight hard-case Evidence Records, Compare, Reading, Measurement, Data, Methodology and Corrections.
- Added explicit bidi isolation for stable Latin IDs/source locators and automatic/plaintext direction for mixed-script source metadata; Arabic RTL no longer relies on ambient direction for those tokens.
- Localized Measurement Agenda domain taxonomy in Arabic as an implementation UI label layer while leaving the controlled classification unchanged.
- Removed English-only visual metadata pills from Arabic Reading cards when no governed Arabic equivalent exists; localized governed accessible summaries and prohibited-inference text remain the semantic carrier.
- Extended `scripts/validate.py` for bilingual title/section parity, one-sided localized public fields, representative numeric signatures, Arabic Reading visual-metadata leakage, Measurement taxonomy localization, stable-ID bidi isolation and language-switch route/query/hash preservation.
- Render harness: **21 routes × 2 languages × 2 viewports (390px/1440px) = 84 cases**, all with one `h1`, correct RTL/LTR state and no page-level horizontal overflow.
- Clean build: **284 HTML documents from 141 controlled Page Specs**; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Production Master and `page_specs.json` unchanged in S05.1. Master hash remains `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`; Page Specs remain `c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`. No Master escalation.
- Reference archive `01_NEW_INPUTS__UNREVIEWED`: **EMPTY**.
- `R-007` remains open for S05.2/S08 accessibility runtime acceptance; `R-042` remains an S07 release-security blocker.
- Boundary decision: **S05_1_PROCEED_TO_S05.2**.

## 2026-09-23 — S05.2 Mobile + keyboard + zoom + screen-reader structure — CLOSED

- Fixed a reproducible 320px Home overflow caused by an inline three-column CTA grid; the Home CTA now uses a responsive class and no tested 320/400/640 route produces page-level horizontal overflow.
- Added keyboard-reachable mobile citation/report utilities, focus transfer into the opened mobile nav, Escape return to the menu trigger, and localized copy-success live feedback.
- Hardened Compare assistive structure with a table caption, row/column header scopes, a named focusable horizontal-scroll region and a concise live verdict status instead of making the full result live.
- Added explicit target-language naming/direction to the language control while preserving the existing equivalent-route/query/hash behavior.
- Extended `scripts/validate.py` for main/skip-link/heading/details structure, menu/search semantics, mobile utility reachability, Data focus, correction origin, Compare table/live-region architecture and first-load boundary ordering.
- Local Chromium runtime QA: **84/84 explicit assertions PASS**, including menu/search focus behavior, global search results, progressive Domain/Evidence detail, Reading source control, Compare 2/3/4 records, citation copy feedback, Data/source query focus, correction backtracking, 320/400px bilingual reflow, 640px 200%-reflow-equivalent checks and browser accessibility-tree landmarks/names.
- Clean build: **284 HTML documents from 141 controlled Page Specs**; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Production Master, Page Specs and Canonical Presentation Contract unchanged. No Master escalation.
- Actual named screen-reader application/browser-chrome zoom and final contrast/deployed-environment acceptance remain explicitly open for S08.1; `R-042` remains an S07 release-security blocker.
- Reconciled the canonical Drive repository in place after acceptance: existing file IDs preserved, `docs/S05_2_MOBILE_KEYBOARD_ZOOM_SCREENREADER_CLOSURE.md` added under the existing docs folder, generated `dist/` excluded, and the control stack now agrees on S05.2 CLOSED / S05.3 NEXT.
- Fixed a control-state lag where `REVIEW_LEDGER.json` and `PROGRESS_INVENTORY.json` still summarized S05.1 after S05.2 had passed; validator checks now protect the current-session/next-session summary.
- Boundary decision: **S05_2_PROCEED_TO_S05.3**.


## 2026-09-23 — Canonical repository hygiene reconciliation after S05.3

- Re-read the live canonical Drive repository before writing and confirmed that `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is the sole Master inside the production repository; `98_TEMPORARY__NONAUTHORITATIVE/` is empty.
- Recomputed the live Production Master SHA-256 as `d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e` and the current Page Specs SHA-256 as `453bde9026c2a30f2c0c2125c0e950cd6e468a9540577318e1896c98e61959da`. Page Specs carry the live Master hash throughout.
- Found and repaired a cross-window partial-integration defect: S05.3 closure prose and validator expectations had advanced, but `build.py` still emitted the earlier `data-visual-fallback="text"` structure and current controls still recorded the S05.2 hash/boundary.
- Repaired the visual renderer so every rendered governed visual carries ordered analytical fallback text, image-independence and non-colour semantics without changing evidence meaning.
- Hardened `validate.py` to hash the actual bundled canonical Master, verify Page Specs against the live Master, verify the raw Page Specs hash against current controls, and reject any workbook copied into public `dist/`.
- Reconciled current controls to S05.3 CLOSED / Window 3 ACCEPTED / S06.1 NEXT_NOT_STARTED. Historical closure files retain the hashes and states that were true when those earlier sessions closed.
- Preserved `R-042` as the only known release-security blocker: anyone-with-link writer access remains open and must be restricted/reverified in S07 before release certification.

### 2026-09-23 — Repository hygiene close

- Replaced the stale `FINAL_RELEASE_VERIFICATION.md` baseline with the live S05.3 / Window 3 accepted authority state and current Master/Page Specs hashes.
- Clarified `DEPLOYMENT.md`: the authority Master is retained inside the canonical repository for governance but must never enter the public `dist/` bundle; the initial product remains fully static/local with future API integration behind controlled adapters.
- Closed the repository-hygiene reconciliation after deterministic build/validator and structural audits passed. The only known repository-level release blocker retained is `R-042` (anyone-with-link writer permission), owned by S07 security/release control.
- Refreshed the checksum-manifest state. `SHA256SUMS.txt` is regenerated last from canonical first-hand files, excluding itself, generated `dist/`, caches and temporary working output.
- Hardened `scripts/validate.py` so current release controls, the S05.3 closure, deployment guidance and checksum manifest are mandatory; the checksum manifest must exactly cover canonical first-hand files and match their bytes, while excluding generated `dist/`, caches and the explicit temporary workspace.
- Added an authority-directory invariant: exactly one canonical `.xlsx` Production Master may exist under `authority/`.

## 2026-09-23 — Independent live-state handoff verification and reference-folder registration

- Reconstructed the current canonical repository from first-hand Google Drive files and verified every path in `SHA256SUMS.txt`; all canonical checksums passed before modification.
- Ran a clean deterministic `npm run verify`: **284 HTML documents from 141 controlled Page Specs; ERRORS=0; WARN=0; PASS**. This independently confirms the current S05.3 / Window 3 accepted repository baseline rather than relying on closure prose.
- Rechecked the live Production Master against its immediately previous Drive revision. The changed block contains bounded Arabic terminology corrections only (including replacement of `مقامات شرطية صغيرة` with `قواعد احتساب شرطية صغيرة`, and `بسط ومقام` with `البسط وقاعدة الاحتساب`); no value, unit, universe, geography, period, source, rights/publication state or claim strength change was identified in that revision comparison.
- Registered Google Drive folder `1tFewVNnzpNXG9tsNyFpoWHnobaKsoRho` as the current **external predecessor/reference folder** for S06 challenge work only. Moving old drafts there is treated as storage organization, not as production-state change and not as a competing source of truth.
- Removed the temporary Drive write-test scratch artifact from `98_TEMPORARY__NONAUTHORITATIVE/`; future scratch remains confined to that excluded workspace and all durable QA/handoff work remains inside the canonical production repository.

## 2026-09-23 — Reference-archive consolidation and canonical-repository hygiene hardening

- Consolidated the user-supplied `Other drafts and sources` folder into the existing non-production reference archive rather than allowing a second sibling reference repository. It now sits under `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION/01_NEW_INPUTS__UNREVIEWED/` as `2026-09-23_SUPPLEMENT__OLD_DRAFTS_AND_SOURCES__UNREVIEWED__NONAUTHORITATIVE` (Drive ID `1tFewVNnzpNXG9tsNyFpoWHnobaKsoRho`).
- Preserved every predecessor/source file in place; no predecessor workbook was promoted, renamed into authority or used to overwrite the Production Master. The canonical Master remains Drive ID `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU` under `authority/`.
- Removed the temporary `__drive_write_test.txt` scratch file. `98_TEMPORARY__NONAUTHORITATIVE/` is empty again.
- Updated current control state so the reference inbox is no longer incorrectly reported as empty. The new supplement is registered as `UNREVIEWED__S06_PENDING__NOT_PRODUCTION_TRUTH`; S06.1 remains `NEXT_NOT_STARTED`.
- Hardened repository validation so a closed hygiene state fails if temporary scratch remains, and so any canonical `.xlsx` outside the single `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is rejected.
- No semantic/evidence/publication change was made. `R-042` remains open because the Drive repository still carries anyone-with-link writer access; this cannot be certified closed until sharing is restricted and re-verified.



## 2026-09-23 — S06.1 World Bank / Findex + Firms source-owner challenge — CLOSED

- Challenged Yemen Findex and the 2022 custom enterprise survey against original World Bank source-owner surfaces.
- Confirmed current public Findex wave/fieldwork, adult-universe, coverage/exclusion, weighting and raw-case-count boundaries; no public Findex value or claim changed.
- Confirmed the firm survey's seven-governorate scope, 328 formal-enterprise sample, 191 account holders, 31 line-of-credit cases, 18 lender-source responses, and the 50% electricity / 46% fuel / 22% access-to-finance challenge table.
- Found one internal Master control defect: a legacy `Uploaded Findex microdata codebook` block contained unverified/inconsistent pseudo-codebook statements. `24_FINDEX_CODEBOOK!A121` now quarantines rows 122 onward as research/lineage only and directs production use to the verified source-extracted DDI architecture in rows 4–117.
- Production Master SHA-256 is now `ee001adede94642ba001f3ffd9c4dbdb7b8ca30050bb9cc478636fbf71a79ba4`. Controlled Page Specs were rebound to the new Master hash without changing public semantics; Page Specs SHA-256 is `28c247c4d55be0bb0b69aa854d3fdb0caa68f16e23657452afb5e5e1b1dac02b`. Presentation Contract remains `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266`.
- S06.1 CLOSED / PASS. S06.2 is next and NOT STARTED. R-042 remains open; S07/S08 were not executed.

## 2026-09-23 — S06.2 — CBY payments / providers / reforms source-owner challenge — CLOSED

- Rechecked current original CBY monthly payment, Banking Supervision, regulatory and dated enforcement surfaces against the admitted payments/providers/reforms evidence.
- Confirmed the monthly payment index remains bounded through January 2026; preserved terminal ≠ merchant, transaction ≠ person, subscriber ≠ active user, administrative trend ≠ population prevalence and missing ≠ zero.
- Confirmed bank and exchange/remittance rosters remain source-defined listing/licensing universes rather than deduplicated current operating-provider counts.
- Confirmed the unified transfer-network decision, e-money amendment, national QR/e-wallet/FPS decisions and consumer-protection instructions are regulatory/institutional evidence and are not promoted into adoption or outcome claims.
- Found one material currentness defect: official CBY Decision No. 17 of 17 September 2026 suspends the licence of Al-Buraq Exchange and Transfers Company and closes its premises. Integrated it Master-first as a dated status overlay and new source `SRC-CBY-ENF-17-2026`; did not mechanically subtract it from the annual roster.
- Regenerated provider/source/closure/catalog/Page Spec/search projections in place. Controlled source-reference records advanced 149→150; publicly addressable 148→149; locator-only 142→143; public search records 417→418; controlled Page Specs remain 141.
- Current Master SHA-256: `cfe4599e26026f9ca377b9ac4b9b1120781678b981e09bb0f439091483a37dfe`. Current Page Specs SHA-256: `5b5601c043a4857314a4f483db3bf8d8f39a07a838cbac8500324e7f463ba708`. Presentation Contract unchanged at `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266`.
- R-042 remains open and owned by S07. S07/S08 were not executed.
- Boundary decision: **S06.2 CLOSED / PASS. S06.3 NEXT_NOT_STARTED.**
