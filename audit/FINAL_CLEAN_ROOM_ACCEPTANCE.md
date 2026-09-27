# Final clean-room acceptance (directive D7, session F9)

**State: DESIGN HANDOFF READY.** Not PUBLIC RELEASE READY.

- Date: 26 September 2026.
- Production Master `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`:
  `17db032b15da16fc4b5b3c3b49f19aebf2ecb4ec46634613fe8505d0f038690b` (F9 transaction RF9 moved two interface labels out of
  code; the rendered site was byte-identical).
- Page Specs `site-src/content/page_specs.json`: `d45748046ea56fd0e67fdf112f9888de65b3fe7fab46ce6f51de3a80824b69aa`.
- Logo `site-src/assets/CauseWay_Master_Logo.png`: `5830163d50f9badbef3227ec44e7705548e2fcc8a06b2d6ae33d56ade60c6a90`
  (unchanged since entry).
- Package: `Yemen_Financial_Inclusion_Evidence_DESIGN_HANDOFF_READY.zip`, one root folder
  `Yemen_Financial_Inclusion_Evidence/`, built with `git archive` from the commit that carries this record; never
  committed. Canonical copy: GitHub `CausewayGrp/Financial-inclusion-`, `main`.

## 1. Cold-recipient test

D7 asks that a recipient with only the package, in an empty directory, follow `README_FIRST`, regenerate, rebuild, run
every gate and find authority and the launch path without any earlier conversation. F9 ran it three times, each time with
a fresh agent that had never seen this programme, on a fresh clone of `main`, told only to act as Claude Design in an
acceptance dry run and to report where it would have to guess. Their reports are kept verbatim in
`audit/final_integration/inputs/F9_COLD_RECIPIENT_RUN{1,2,3}.md`.

| Run | Tree | Could start D0 without asking? | Commands | BLOCKER | MATERIAL | EDITORIAL | What followed |
|---|---|---|---|---|---|---|---|
| 1 | `b96e306` (F8 freeze) | Yes, with qualifications | All passed | 0 | 15 | 10 | F9 part 1 (`3adf224`): RF9, inventory 1.1, WITHHELD grammar, `YFIE_SITE_DIR`, archive-safe manifest, precedence table, Compare and report rules, type and date rules, expected labels |
| 2 | `3adf224` | Yes; "close" for D0–D7 (six questions) | All passed; `YFIE_SITE_DIR` proved by planted defects | 0 | 9 | 14 | F9 part 2 (`b3c8e87`): editorial rule, marker fix, inventory 1.2, where visuals live, test-hook contract, workbench, vintage case, diagrams, `.gitignore`-aware archive walk |
| 3 | `b3c8e87` | Yes for D0, D1, D3–D5; D2, D6, D7 needed rules for chart-level content | All passed | 0 | 10 | — | F9 part 3 (`2922449`): fonts in `vendor/fonts/`, POS notes from bilingual records, inventory 1.3, snapshot and superseded-section rules, placement of every bound visual, pre-registered chart-table labels |

Every run found authority and the start path at once (`CLAUDE.md` → `AGENTS.md` → `README.md` → `handoff/README_FIRST.md`),
and none found a blocker. The runs went progressively deeper: from the start path and gates (run 1), to the rules between
documents (run 2), to the content a chart table needs (run 3). Each finding was fixed Master-first or in the generator,
or answered with an explicit rule in the handoff, before the next run; the few that need new governed wording are
pre-registered in the brief §10 as expected `NEEDS_CONTROLLED_CONTENT` / `ESCALATE_TO_MASTER` requests with a
placeholder rule, which is how the Design process is meant to meet them. A fourth run was not commissioned: no run found
a blocker, and the remaining class of finding is the one the escalation path exists for.

## 2. The archive, from an empty directory

`git archive` of `2922449` (the final tree differs only in the status lines and this record) was extracted into an empty
directory with no `.git`, and the commands in `handoff/README_FIRST.md` §8 and every CI gate were run there:

| Gate | Result |
|---|---|
| Checksums (`scripts/checksums.py --check`) | 753 files current — before and after the rebuild (outputs byte-identical) |
| Repository manifest (`--check`) | 753 files in 19 classes, current (file set from the archive walk, which honours `.gitignore`) |
| Generator `--check`; generator tests | `PROJECTION CHECK PASS`; 21 of 21 |
| Build; public-literal audit | 288 HTML from 143 Page Specs; 12,760 records, 0 unresolved |
| Validator | `WEBSITE REPOSITORY VALIDATION PASS`, 0 errors, 0 warnings (all gates through F6-G08 and R86-G04) |
| Handoff inventory `--check` | Current |
| Literal-audit determinism | One SHA-256 under eight hash seeds |
| Source-lineage truth test | 8 of 8 |
| Architecture diagrams `--check` | Current |
| Bilingual numeric invariance | 0 of 143 page pairs differ |
| Public tools (browser) | 25 passed, 1 not applicable to the current data |
| Viewport acceptance (browser) | 168 of 168 |
| `YFIE_SITE_DIR=design/reference/out` (a copy of the build placed where Design's output goes) | Tools 25/26 (1 n/a); invariance 0; checksums, manifest and validator still pass with that ignored output present |

The same gates passed on each F9 commit in the local replica of CI (**Verify**: governance gates and browser acceptance).

## 3. The scans D7 names

| Scan | How | Result |
|---|---|---|
| Stale Reading copy | Validator RP-G05 (retired titles and the retired generic section) | Pass |
| Private and internal leakage | Validator R85-G05…G07; visible text of all 288 pages for internal field names, lineage enums, escalation markers, TODO and placeholder text; the repository for the owner's personal address | 0 hits |
| Rights and source exposure | The nine sources without a public locator: none named in any page or the search index; the withheld CLM-044 value: absent from every page; F6-G07 (no bundled third-party document); F6-G08 (rights and card state per source) | Pass |
| SEO and discovery | Validator F6-G01…G04: titles, descriptions, one `<h1>`, self-canonical, reciprocal hreflang with `x-default`, robots and sitemap rule, structured data | Pass |
| Manifest and checksums | `FINAL_REPOSITORY_MANIFEST.json`, `SHA256SUMS.txt` | Current |

## 4. Definitions of Done, F0–F9

| Session | Definition of Done | Evidence |
|---|---|---|
| F0 | Entry state confirmed without a verification loop; no semantic mutation | `docs/CHANGELOG.md` (F0–F2 entry) |
| F1 | Ten Readings each with one explicit disposition; source questions resolved or held as frontiers; one integration plan | `audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`, `audit/READING_PORTFOLIO_CHANGE_LEDGER.csv` |
| F2 | One Master-first Reading integration; bilingual invariance 0 | RP-F2 run reports in `audit/reading_integration/`; commit `0b94c08` |
| F3 | Exactly five Resource Library decisions, none ambiguous | `audit/F3_RESOURCE_DECISIONS.md` |
| F4 | One root, one Master, one projection path, one start path, no duplicate current artefact, permanent gates | `audit/R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md` |
| F5 | Whole Arabic and English corpus accepted, zero unresolved bilingual mismatch, leakage scan | `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`, `audit/F5_CORPUS_FINDINGS_LEDGER.csv` |
| F6 | Discovery contract, accessibility outcomes, rights/security/privacy gates, nothing invented | `audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`, `docs/DEPLOYMENT.md` |
| F7 | Bounded sustainability method, no green claim, non-public support note | `docs/SUSTAINABILITY_METHOD.md`, `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`, `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` |
| F8 | One README_FIRST, one Design prompt, one logo authority, route/content and hard-state inventory, visual contracts, exact commands, Design-to-Code contract, zero DESIGN_BLOCKER | `audit/R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md` |
| F9 | Cold-recipient test; final gates; final open-items register in six classes with zero DESIGN_BLOCKER; one single-root package | §1–§3 above; `FINAL_OPEN_ITEMS_REGISTER.md` (49 items: 11 engineering after Design, 4 release-only, 11 external evidence dependencies, 8 known evidence frontiers, 8 owner inputs, 7 rejected / no action; zero DESIGN_BLOCKER); §5 below |

## 5. The package against D7's list

| D7 requires | In the package |
|---|---|
| Current Production Master; deterministic generator and contracts; current projections | `authority/…Master.xlsx`; `scripts/generate_projections.py`, `scripts/projection/` (with `controlled_inputs/`); `site-src/content/` |
| Current build/runtime source; all final EN/AR public content; the ten Readings | `scripts/build.py`, `site-src/app.js`, `site-src/styles.css`, `site-src/assets/`; `dist/en/`, `dist/ar/` (288 documents) |
| Source, evidence, passport, measurement and visual bindings | `site-src/content/evidence/`, `sources/`, `visuals/`, `content/`; `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` |
| `FINAL_REPOSITORY_MANIFEST.json`; `audit/INDEX.md`; exact checksum record | Root; `audit/INDEX.md`; `SHA256SUMS.txt` |
| Reading acceptance and change ledger; corpus acceptance; R8.5 and R8.6 closures; SEO/discovery and rights/privacy/security acceptance; sustainability method and baseline; non-public support file | The records in §4 |
| `handoff/README_FIRST.md`, `CLAUDE_DESIGN_MASTER_PROMPT.md`, `DESIGN_ACCEPTANCE_CRITERIA.md`, `ENGINEERING_HANDOFF_EXPECTATIONS.md`, `DESIGN_TO_CODE_CONTRACT.md` | `handoff/` (eleven files, gate R86-G03) |
| `FINAL_OPEN_ITEMS_REGISTER.md` | Root |
| Everything else Design needs, except third-party documents | The fonts (`vendor/fonts/`), the logo, the visual contracts, the test suites; original sources stay reachable through their public locators |

Not in the package, by design: third-party source documents (never redistributed), earlier handovers and prompts (retired
to `audit/prior-review-records/`), any chat.

## 6. Not claimed

No WCAG conformance, legal review, rights clearance, native-language certification, security guarantee or service
level; no CauseWay commissioning or funding fact. Not PUBLIC RELEASE READY: release needs the RELEASE_ONLY and
OWNER_INPUT items of the register, the post-implementation accessibility audit and a named release acceptance.

## 7. After this record

- The owner pushes the signed tag `checkpoint/design-handoff-ready` on the commit carrying this record (this session
  cannot push tags); `.github/workflows/checkpoint.yml` then rebuilds and verifies the same archive and attaches it to a
  pre-release.
- Claude Design starts at `handoff/README_FIRST.md`. Claude Code waits for the accepted Design package.

---

## Addendum — post-F9 correction (27 September 2026)

Appended; §1–§7 above are unchanged and remain the F9 record. Directive: `audit/directives/D8_POST_F9_CORRECTION_2026-09-27.txt`
(verbatim). Entry state: `origin/main` = `03bd654` (the delivered F9 archive), no tag on the remote; nothing newer to
diagnose. Commit: `fix(handoff): post-F9 correction — OWN-07, OWN-08, handoff tightened in place`, the commit that
carries this addendum on `main`; `checkpoint/design-handoff-ready` belongs on it (§7 above said "the commit carrying
this record": read it as this commit). No Master change: Master `17db032b…` and Page Specs `d4574804…` are unchanged.

### A1. What changed

| Item | Change |
|---|---|
| OWN-07 | `/remittances/` binds MA-001; its presentation contract allowed 0 Measurement cards. Limit set to 1. The card renders in `/en/` and `/ar/remittances/` with its household scope ("including remittance receipt, channel and frequency" · «يشمل تلقي الحوالات وقنواته وتكراره»), apart from the page's macro remittance evidence |
| OWN-08 | `navigation_interaction.json` descriptive fields aligned with the governed copy, the Page Specs and the browser tests: Report an issue → `/contact/?record=` with `UI-HEADER-REPORT-AN-ISSUE`; Reading breadcrumb `GOVERNED_TITLE`; Compare's six dimensions, four assessments, same-record state and outside-set error; workbench and Compare limited to public records and the governed comparable set (Evidence Passports never rendered); `verification_sparse` → `/evidence/CLM-004/`; institutional and vintage states as the pages show them; J10 record → Contact → Corrections |
| Contract rule | Class `CONTROLLED_CONTRACT` for the two hand-maintained contracts; rule in `presentation_priority.json`, `AGENTS.md` rule 2 and `CONTRIBUTING.md` §2 |
| Handoff | In place, one start file and one brief: D1 competing theses on Home, `/evidence/CLM-003/` and `/readings/same-year-different-number/` in both languages before propagation; decision log and `design/COVERAGE.csv` kept at every gate; D0 statement on supplied boards or mockups; D7 requires the runnable, fully populated bilingual reference site (a design source alone is an incomplete hand-back); `⟦NCC:…⟧` for development only; print and portable evidence in the brief, the criteria and the Design-to-Code contract, with every CauseWay-content export disabled until OWN-04 and reporting kept on the static Contact route; font loading worded to `vendor/fonts/README.md` |
| Records | Register 47 items (OWNER_INPUT 6), zero DESIGN_BLOCKER; checkpoint, README, Context, changelog, audit index and directives index updated |

### A2. File counts

The checksum and manifest counts cover every tracked file except `SHA256SUMS.txt`. §2 counted 753 on `2922449` (754
tracked). `03bd654` added this record: 754 (755 tracked). The correction adds the D8 directive: 755 (756 tracked). Each
count is right for its commit.

### A3. Gates on the correction (local, before commit)

| Gate | Result |
|---|---|
| Checksums; repository manifest | 755 files current; 755 files in 20 classes |
| Projection check; projection unit tests | Pass; OK |
| Build; public-literal closure | 288 HTML from 143 Page Specs; 12,760 records, 0 unresolved |
| Validator | 0 errors, 0 warnings (R86-G01…G04 included: start path, status agreement, inventory, eleven handoff files) |
| Literal-audit determinism; source-lineage truth test; architecture diagrams | Pass (8 seeds, one hash); 8/8; current |
| Bilingual numeric invariance | 0 of 143 page pairs differ |
| Public tools (browser) | 25 passed, 1 not applicable to the current data |
| Viewport acceptance (browser) | 168 of 168 |
| Affected pages (browser) | `/en/` and `/ar/remittances/`: one MA-001 card each, household scope intact; `/en/` and `/ar/evidence/CLM-001/` → `contact/?record=CLM-001`; Contact links to Corrections; `/evidence/CLM-004/` renders in both languages; the flagship Reading's breadcrumb ends on its title in both languages |

The **Verify** workflow runs the same gates on the pushed commit.

### A4. Still not claimed

As §6: not PUBLIC RELEASE READY; no WCAG conformance, legal review, rights clearance, native-language certification or
security guarantee.

---

## Second addendum — design-enablement control pass (27 September 2026)

Appended; §1–§7 and the first addendum are unchanged. Directive: `audit/directives/D9_DESIGN_ENABLEMENT_CONTROL_PASS_2026-09-27.txt`
(verbatim). Entry state: `origin/main` = `937bf80` (the post-F9 correction), working tree clean, no divergence, no tag on
the remote. Commit: `docs(handoff): design-enablement control pass — kernel, loop, memory, debt, review tests`, the
commit that carries this addendum. **Tag target.** `checkpoint/design-handoff-ready` belongs on that commit — the state
Claude Design starts from — and no longer on `937bf80` as the first addendum said: this pass changes the handoff Design
reads, so the tag must mark the strengthened handoff. `937bf80`, its parent, remains the post-F9 correction commit. No
tag existed, so nothing is moved. No Master, projection, contract or public-page change: Master `17db032b…`, Page Specs
`d4574804…`, `dist/` byte-identical.

### B1. Method

The handoff was read in its own order (README_FIRST → brief → criteria → contract → engineering expectations → visual
contract → inventory → register) and mapped against the directive's §5–§17. Default: no change. A requirement already
met was kept; a partial or absent one was strengthened in place, in the existing files — one start file, one brief, one
criteria list, one contract. The only new record the handoff asks Design to create is `design/DESIGN_DEBT.md`, listed in
the brief's existing §19 package table.

### B2. What was strengthened (all in `handoff/`)

| Area | Where |
|---|---|
| Kernel; nine-step working loop; gate-start re-read and gate-end commit rule; Code recipient test | Brief §0 |
| Public evidence service, not a generic website | Brief §1 |
| Connected evidence system from bound relationships only | Brief §4.6 |
| Firewall: infrastructure ≠ outcome; one lineage repeated ≠ corroboration; layout protects distinctions; states that must not collapse | Brief §5 |
| Full list of freedoms; who owns what (Design, Code, owner, release, Master) | Brief §6 |
| Tone pairs; wider avoid-list; motion; imagery and its provenance checklist; dark-mode logic; four review tests | Brief §7 |
| Identity constraints named; manifest palette labelled a hypothesis | Brief §8; `IMPLEMENTATION_MANIFEST.json` |
| Small surfaces; template ≠ review; twelve audience lenses; per-family outcomes with a Home cold-reader test | Brief §9.1, §9.3, §9.4 |
| Search as a product; external links; reporting intents; a rule for every input; per-object export formats; Arabic exports; four kinds of material; data packages; micro-interactions | Brief §10 |
| Interaction in visuals never hover-only; every contract an analytical decision | Brief §12 |
| Arabic tested, not only viewed | Brief §13 |
| Low bandwidth; an optional honest footprint note | Brief §15 |
| Decision-log fields; coverage status ladder with `checks` and `code_handoff`; design-debt register; evidence files as PNG (gate F6-G07); four layers; hostable static site | Brief §19 |
| Gates with entry, work, exit evidence and stop conditions; last-10-percent audit | Brief §20 |
| Section K and matching lines in B–J | `DESIGN_ACCEPTANCE_CRITERIA.md` |
| Design debt mapped; four layers | `DESIGN_TO_CODE_CONTRACT.md` |
| Code reads the debt register, ledger and escalations | `CLAUDE_CODE_MASTER_PROMPT.md` |
| Kernel and memory pointer; NOT RUN rule; full freedoms pointer | `README_FIRST.md` |

Outside `handoff/`: the hand-maintained `design/architecture/YFIE_DESIGN_TO_CODE_FLOW.svg` (and its PNG preview) now
shows D0–D7 and no longer says "developer placeholders only"; its clipped side label is fixed.

### B3. Independent check

A fresh agent that had not seen the work audited the handoff read-only against the directive's §5–§17. Verdict: a cold
Design agent can start D0 and run to D7 from the repository alone; every area present. It found one provenance gap (this
addendum was not yet written), a PDF-evidence trap against gate F6-G07, no fallback for an environment without Chromium,
an undefined cold reader, the stale flow diagram, and five editorial points; all were fixed in this commit.

### B4. Gates (local, on the final tree)

| Gate | Result |
|---|---|
| Checksums; repository manifest | 756 files current; 756 files in 20 classes |
| Projection check; projection unit tests | Pass; OK |
| Build; public-literal closure | 288 HTML from 143 Page Specs; 12,760 records, 0 unresolved; tree clean after build |
| Validator | 0 errors, 0 warnings |
| Literal-audit determinism; source-lineage truth test; architecture diagrams; handoff inventory | Pass (8 seeds, one hash); 8/8; current; current |
| Bilingual numeric invariance | 0 of 143 page pairs differ |
| Public tools (browser) | 25 passed; 1 skipped as not applicable (no Compare record ID contains "+") |
| Viewport acceptance (browser) | 168 of 168 |

Counts (public inventory): 143 Page Specs, 110 Evidence Records, 60 public claims, 55 Evidence Passports, 10 Readings,
10 Measurement priorities, 11 entry questions, 36 visual contracts, 160 sources, 151 public locators, 28 curated
resources, 24 chronology events, 435 search records. Register: 47 items, zero DESIGN_BLOCKER.

### B5. Still not claimed

As §6: not PUBLIC RELEASE READY; no WCAG conformance, legal review, rights clearance, native-language certification or
security guarantee.
