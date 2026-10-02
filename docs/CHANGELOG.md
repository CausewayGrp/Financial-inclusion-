# Repository Change Log

## 2026-10-02 — Release candidate: Owner Addendum 2 saved

`audit/release_candidate/INSTRUCTIONS_ADDENDUM_2026-10-02.md` (with its `audit/INDEX.md` row) holds the owner's second
addendum to the release-candidate brief, verbatim from its BEGIN to its END marker. It adds release defects A1
(VIS-PAYMENT-RAILS: the text alternative names a step its drawing and table lack) and A2 (search for "law" / «قانون»
needs a boundary note; the B5 scope line names what is not held), improvements 1–11 inside B15d, and items for B12,
B13d, B14e and B16. Nothing is applied in this commit; the pull request's checklist carries the items under "Addendum 2".

## 2026-10-02 — Release candidate RC-5: Part B editorial passes B2 (Arabic) and B3 (English)

Transaction `audit/release_candidate/rc_5_editorial.py` through `run_stage.py` (Master `0fb6c16de6db` → `2b609e1928f8`;
454 cells; ledger and run report in `audit/release_candidate/runs/`), with `rc_5_stage_inputs.py` installing the Arabic
period mappings of the provider matrix in the visual design contract. Every change is listed with FROM, TO and reason in
`audit/release_candidate/ARABIC_EDITORIAL_LEDGER.md` (B2: 122 applied) and `ENGLISH_EDITORIAL_LEDGER.md` (B3: 150 applied,
135 with their Arabic pair); no number, unit, period, universe or limit changed. Independent review before commit, Arabic
and English: both NOT ACCEPTABLE before fixes (Arabic: 1 blocking, ISO period cells displayed reversed on `/ar/providers/`;
English: 1 blocking, governorates called districts), every blocking and should-fix finding applied; English finding 15
(a gloss for "P0") is deferred to B15.

- **B2 a–e:** the Arabic observations recorded in `design/ESCALATIONS.md`; one Arabic term per concept; ISO dates in
  Arabic prose; one form of the Findex fieldwork window; further defects on the main pages.
- **B2 f (A3 escalation):** accessible summaries that restated their figure's boundary drop the restating sentence.
- **B2 g, h:** the provider matrix prints Arabic periods and states (new `22_PROVIDERS_DATA` columns
  `reference_state_ar`, `reference_period_ar`) and a governed context lead-in (UI-VIS-MATRIX-CONTEXT, "Context:" / «السياق:»).
- **B3:** the English pass — plain register, consistent terms, and meta descriptions written as sentences of 155
  characters or fewer.
- Renderer: the matrix's Arabic dates (`date_ar`) and context lead-in; the citation preview wraps long isolated identifiers at 320 px.
  13 social images regenerated (their frame text changed); the rest stay byte-identical.

## 2026-10-02 — Release candidate RC-4: Part B items B5, B7, B8, B9

Transaction `audit/release_candidate/rc_4_partb_strings.py` through `run_stage.py` (Master `3c6c66beddedb` → `0fb6c16de6db`;
ledger and run report in `audit/release_candidate/runs/`). Every string is the brief's wording, English and Arabic; one
governed citation line (UI-CITE-PAGE-LINE) re-uses the record line's words. Independent review: NOT ACCEPTABLE before fixes
(1 blocking, 4 should-fix), all applied before commit (ledger `independent_review`).

- **B5 /data/:** "Rules, decisions and official lists" groups the 23 sources whose governed type is an enforcement decision,
  circular or instruction, regulatory decision, regulation, or official list (the one curated card linked, not duplicated),
  with its scope line; sources with no governed type show "Document type not recorded" (EAD-07).
- **B7 Compare:** the "selected set" sentence in the intro and under the "record not available for comparison" error.
- **B8 /data/:** the reuse terms stated once above the source list; the older directory paragraph drops its closing
  reuse clause (each card keeps its label).
- **B9 every page:** a visible citation preview (the record's governed citation, or the page title and UI-CITE-PAGE-LINE,
  with the canonical address), "Copy citation" copying exactly that text, and "Print this page". In Arabic the record and
  source identifiers and the publisher's name are isolated left-to-right (the review's blocking finding); no "?." after a
  question title; the Compare intro keeps its paragraphs.
- Validator RC-GB, two negative controls and a browser test hold all four.

## 2026-10-02 — Release candidate Part B, B1: method text on the 13 table-only records

`scripts/yfie/content.py` no longer suppresses the governed method text of the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY`
records (owner decision A4 / C6 revised): each record page, and each frame that prints its record's method, shows it in
both languages. All 13 were read in full and are reader-facing method statements; none was withheld. Validator PB-0401,
which forbade the text as a "draft encoding note", now requires it like every other record's method (negative control
added). Register EAD-12 carries a dated line; table rows for the 13 stay post-launch.

## 2026-10-02 — Release candidate Part B, B0: the owner's Part B decisions recorded

`audit/OWNER_DECISIONS_2026-10-02.md` gains the dated section "Addendum — 2 October 2026 (Part B)" (append only): A4 / C6
revised (the 13 table-only records' method text is rendered), the human accessibility audit replaced by the extended
automated audit (no conformance claimed), the Part B steward and editor designation, the static architecture, the Arabic
default at the neutral root, the unchanged product name, and the owner rules on numbers, pages and closed decisions,
verbatim.

## 2026-10-02 — Release candidate G5: records reconciliation

`audit/RECORDS_RECONCILIATION_2026-10-02.md` (with its `audit/INDEX.md` row): one row per item of the brief's G5 list —
`implementation_target.ui` names the Python renderer (C9); the context's sustainability pointer names the implemented-runtime
measurement (C9); DEBT-008 reclassified as not blocking release (C8, A8); checkpoint §4 no longer names Design as next;
EAD-07's label request raised; historical ledgers left as they are, register §8 governing; the master logo's byte count
corrected in `docs/SUSTAINABILITY_METHOD.md`; `site-src/deployment.json` state `PRE_RELEASE_PRODUCTION_RUNTIME`
(`public_origin` still null); README's IBM Plex lines checked against the shipped fonts (no change); README status for
after this pull request. The four files inside the runner's snapshot went through `run_stage.py --install`
(`audit/release_candidate/g5_stage_records.py`). C1–C5 confirmed still holding.

**Erratum to the entry of 29 September 2026 (EAD-01, "Every gate keeps its assertion …").** That entry says it "corrects the
planning appendix of 29 September". No such appendix is in the repository: it was the implementing session's working plan
and was never committed. The statement being corrected — that Explore's clusters "already come governed, through the
handoff inventory's `question_groups`" — is described in the EAD-11 escalation in `design/ESCALATIONS.md`. The entry
itself is left as written.

## 2026-10-02 — Release candidate G4 (part 2): EAD-03 — the logo's web-size derivatives

Owner decision EAD-03 (`audit/OWNER_DECISIONS_2026-10-02.md`). `scripts/logo_derivatives.py` writes eight pure Lanczos
resamples of the unchanged master to `site-src/assets/logo/` (32, 40, 48, 64, 72, 80, 96, 144 px; 36,699 bytes in all) and its
`--check` compares each one's pixels with a fresh resample (new CI step; CONTRIBUTING.md §5; Pillow 11.3.0 pinned in
`requirements.txt`). `render.logo()` serves them with `srcset`/`sizes` on the product bar, the institutional band and the
404 head; the export identity line uses 32/64; the social-image template keeps the master, so the 286 images are unchanged.
Validator RC-G4 fails a page that loads the master or names a missing derivative (negative control added). Cold page weight,
EAD-10 method: 10.31–10.71 MB before, 0.30–0.69 MB after (`audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md`).
DEBT-016 closed; `design/08_ASSET_MAP.md` §1 and the register carry dated lines.

## 2026-10-02 — Release candidate G4 (part 1): search, A3, A5, shipped features, Arabic counts

Code only; no Master or contract change. Every behaviour has a validator check (RC-G4, P2-G02) with a negative control, and
the browser suite covers the tools.

- **Search** (item 1, A6 / C7; EAD-06): when the dialog caps its ten hits, the status gives the true total
  (UI-JS-SEARCH-RESULTS-OF, "Showing 10 of {m} results") and a link carries the query to the Evidence directory filtered to
  evidence records (`/evidence/?q=…&type=evidence`); the directory shows every match. A result-type filter
  (UI-JS-SEARCH-TYPE-FACET / -ALL, the governed type labels) narrows both searches; on the directory it is URL-addressable.
- **A3 / C3, the double boundary** (item 4): on the page a figure's text alternative — and the Compare standfirst — is the
  governed accessible summary; the boundary prints once, in the foot. Export frames keep the full alt text (`_detached`).
  `check_visuals.py` boundary_once_in_foot and `check_site.py` boundary_once_per_frame now count the visible text
  alternative too; they report eight frames whose governed summary restates its boundary (escalated for the Part B
  editorial pass in `design/ESCALATIONS.md`).
- **A5 / C4, the retired frame** (item 5): the RETIRE_FROM_DESIGN tier is excluded from the domain depth frames;
  `/reforms/` no longer shows VIS-CAPITAL-CONTEXT and keeps its record link; `never_drawn` rejects a text frame;
  `design/06_VISUAL_TABLE_SYSTEM.md` §1 records the removal.
- **Shipped features** (item 6): every link that opens a new tab carries UI-EXTERNAL-NEW-TAB (visually hidden, or at the end
  of its aria-label); fallback tables whose rows carry different units head the value column with
  UI-VIS-VALUE-UNIT-PER-ROW (VIS-FINDEX-GAPS); the Compare prompt ("Select at least two records.") stands beside the
  controls and shows only while fewer than two records are selected; the Compare status is in label-value form (RC-3).
- **Arabic counts in visuals** (item 7): a count printed with its unit noun reads «العدد: 561», «شركات الصرافة: 98».
- Item 3 (every remaining code FAIL / CONDITION of `audit/PR8_INDEPENDENT_ACCEPTANCE.md`) is A3, A5 and A6, all above.

## 2026-10-02 — Release candidate G3: EAD-11 — the question sets move into the presentation contract

Steward patch by owner decision (`audit/OWNER_DECISIONS_2026-10-02.md`, EAD-11), installed through `run_stage.py`
(`audit/release_candidate/g3_stage_presentation.py`; Master unchanged). The two entries recorded under EAD-11 in
`design/ESCALATIONS.md` — Home's four starting questions and Explore's four groups — sit, values unchanged, under
`question_sets` in `site-src/content/presentation_priority.json`. The generator rejects an unknown question or heading and a
missing or repeated question (`derived.presentation_contract`; unit test `test_question_sets_guards`); the renderer
(`scripts/yfie/content.py`) and the handoff inventory read the sets there, and `scripts/yfie/question_sets.py` is deleted.
Home and Explore are byte-identical before and after in both languages, as is the handoff inventory (hashes in
`audit/release_candidate/runs/G3-EAD-11_RUN_REPORT.json`). EAD-11 closed in the register and in `design/ESCALATIONS.md`.

## 2026-10-02 — Release candidate RC-3: governed interface strings (items 11, 12, 18, 19, 20)

Transaction `audit/release_candidate/rc_3_interface_strings.py` through `run_stage.py` (Master `ecc228beec41` → `3c6c66beddedb`;
ledger and run report in `audit/release_candidate/runs/`). Every label is the brief's own wording, English and Arabic together.

- **New strings** (04): UI-JS-SEARCH-RESULTS-OF (item 11); the five provider-matrix headings and UI-VIS-CAT-PRV-CLASS-PSO
  (item 18); UI-JS-SEARCH-TYPE-FACET, UI-JS-SEARCH-TYPE-ALL, UI-JS-SEARCH-SEE-ALL-EVIDENCE, UI-EXTERNAL-NEW-TAB and
  UI-VIS-VALUE-UNIT-PER-ROW (item 19). Their runtime and renderer use ships in G4.
- **Changed strings**: UI-JS-COMPARE-SELECTED in label-value form, "Records selected: {n}" / «السجلات المختارة: {n}», with the
  Compare status line in `site-src/app.js` filling it (item 19); UI-VIS-UNIT-PP Arabic «نقطة مئوية» (item 20); four source
  records' resource category "Measurement methods and international references" / «مناهج القياس ومراجع دولية» (item 12).
- **Provider observability matrix** (VIS-PROVIDER-OBSERVABILITY, /providers/ and its record): drawn now that its six labels
  are governed (DL-D7-001). The payment-system-operators row prints UNKNOWN in every dimension, the three institution
  events following as context in the status cell and its fallback table (the contract's `known_gap`; `scripts/yfie/visuals.py`).
- **Independent review**: ACCEPTABLE. Two findings need governed content and are escalated in `design/ESCALATIONS.md`: Arabic
  text for four English-only period values the Arabic matrix now shows, and a lead-in marking the operators' context events.

## 2026-10-02 — Release candidate RC-2: trust copy (items 9, 10, 13, 14, 15)

Transaction `audit/release_candidate/rc_2_trust_copy.py` through `run_stage.py` (Master `ebf03d6fe4cf` → `ecc228beec41`;
ledger and run report in `audit/release_candidate/runs/`), with `rc_2_stage_inputs.py` staging the public inventory contract,
the projection manifest and `README.md` (`--install`). Independent bilingual review: ACCEPTABLE; its two should-fix findings
applied before commit (below), two owner-wording notes recorded in the ledger.

- **/about/** §6: the owner-approved funding paragraph, verbatim, after "CauseWay’s role" (item 9; OWN-01).
- **/corrections/** "How history works": the edition statement, cut-off 26 September 2026 (item 10; UI-CONTENT-VERSION unchanged).
- **YSC-012** cites the two 26 June 2024 CBY-Aden instruments; the public count *chronology_events* follows its definition
  ("Dated events") through the new generator rule `count_where_not_in` — 23, YSC-020 (the analytical rule) excluded — with the
  same rule in the validator's recount, `scripts/rebind_authority.py` and the generator unit test (item 13).
- **Sheets 00 and 37**: count statements set to the derived values; the seven COUNTA formula cells keep their formulas and only
  their cached results change (`rc_lib.set_formula_cache`), so the 37 READY/REVIEW checks still compare a live count (item 14).
- **Publisher name**: no Arabic transliteration of CauseWay in any Master cell (item 15; no write).

## 2026-10-02 — Release candidate RC-1: Master truth fixes (items 1–8, 16, 17)

Transaction `audit/release_candidate/rc_1_truth_fixes.py` through `run_stage.py` (Master `17db032b15da` → `ebf03d6fe4cf`;
ledger and run report in `audit/release_candidate/runs/`), with `rc_1_stage_inputs.py` staging the visual design contract and
`master_structure.json` (`--install`). English and Arabic together; an independent bilingual review (1 blocking, 6 should-fix,
8 optional) was applied before commit, its deferrals recorded in the ledger.

- **/people/** §3–4 extend to the education and age gaps that VIS-FINDEX-GAPS draws (item 1); the VIS-SOURCE-COMPARISON
  summaries take the brief's wording (item 2).
- **Methodology and EXT-01, Path B** (item 3): no source host is reachable from this session; the lead sentence is replaced and
  YSC-008/014/015/017 print a verification note (new 14 columns `verification_note_en/_ar`). EXT-01 stays open.
- **Units** (items 4, 17): VIS-POS-VALUE displays whole YER million; remittance prose in USD million; YSC-004, the CBY-Aden rate
  and the SFD savers count in one notation. Sweep and dispositions: `audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md`.
- **CBY-Aden scope** on the RV-CWR-004 lane and RV-CWR-009 rows (item 5); **VIS-FIRM-CONSTRAINTS** partial-list note, Path B
  (item 6); the disagreement legend, CLM-003 and the POS summaries describe only what is drawn (item 7).
- **Firewall adjudications** (item 8): RV-CWR-009 OPERATION KEEP; VIS-REMITTANCE-COST rpw MEASURED → REPORTED; RV-CWR-001
  IMF staff path KEEP.
- **use_rule pointers** to `scripts/yfie/content.py` (item 16; PR #8 acceptance A7 item 8 / C9).
- **Code**: the renderer prints the chronology verification note and the POS scope; `firm_constraints` prints frame labels.
- **Gates**: `scripts/tests/test_content_parity.py` is the standing content gate (CI step, two negative controls); the cutover
  parity test exits 2 ("pinned") once the Master moves past its oracle. Validator S05.1 signature updated for the Reading's new
  unit. Methodology social images regenerated.
- **Register**: dated EXT-01 and VIS-FIRM-CONSTRAINTS lines in `FINAL_OPEN_ITEMS_REGISTER.md` §3.

## 2026-10-02 — Release candidate G1: the owner's decisions recorded under the register rows they affect

`FINAL_OPEN_ITEMS_REGISTER.md` (append only, per its §9 rule): one dated "owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md`"
line under OWN-01, OWN-02, OWN-03, OWN-04 and OWN-05 (§5), under EAD-11 and for D7 (§1; EAD-03 already had its line from the
before-merge commit), and the new item **EAD-12** for A4 / C6 — the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY` records; post-launch;
no change in this edition. No Master, projection, `dist/` or controlled-contract byte changes.

## 2026-10-02 — Release candidate: start (G0)

Branch `code/release-candidate-fixes` from `main` at `38a9a97` (pull request #8 merged; its before-merge conditions met). Baseline
green: checksums current, `WEBSITE REPOSITORY VALIDATION PASS`; Production Master SHA-256 `17db032b…8690b`, Page Specs
`d4574804…b69aa`, both as found. This commit saves the owner's brief verbatim as `audit/release_candidate/INSTRUCTIONS.md`
(indexed in `audit/INDEX.md`; the folder is classed `CURRENT_PROGRAMME_RECORD`) and changes nothing else. The pull request
description carries the checklist of every Part A and Part B item and the progress log.

Not declared: PUBLIC RELEASE READY. Not claimed: WCAG conformance.

## 2026-10-02 — Pull request #8: the before-merge conditions C1–C5 met, in records only

`audit/PR8_INDEPENDENT_ACCEPTANCE.md` returned MERGE AFTER CONDITIONS on the production runtime (head `74d79a1`). This commit
meets its five before-merge conditions and makes the one-line record fixes it listed. No code, test, gate, generator,
Master byte, projection, `dist/` file or controlled contract changes: `git diff 74d79a1..HEAD -- site-src scripts dist
design/reference authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is empty.

- **Owner decisions recorded.** `audit/OWNER_DECISIONS_2026-10-02.md` (indexed in `audit/INDEX.md`): OWN-01 (the funding and
  relationships paragraph, EN and AR), the publisher name, OWN-04 (licence deferred; link-and-citation launch), OWN-03,
  **D7 — the owner's final visual acceptance of the Design package**, the social images, OWN-05, OWN-02, EAD-03 (export
  approved, master file unchanged), relationships, the steward delegation for the EAD-11 patch, and the dispositions of
  A3 / C3, A5 / C4 and A4 / C6. Recorded, not applied: the Master-first and runtime changes belong to the release-candidate
  pull request.
- **C2 — the premise settled.** `design/00_DESIGN_README.md` and `design/10_ACCEPTANCE_CHECKLIST.md` record the owner's
  acceptance of 2 October 2026 and keep the 28 September "withheld" status as dated history; `design/COVERAGE.csv` writes
  `ACCEPTED` on its 1,415 `VERIFIED` rows (18 `DESIGNED` unchanged). Code no longer "waits": `README.md`,
  `handoff/CLAUDE_CODE_MASTER_PROMPT.md` (its first line keeps the literal gate R86-G01 reads, as dated history),
  `handoff/README_FIRST.md`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` `design_prompt_status` (programme state, edited
  directly — `scripts/rebind_authority.py` owns only its hashes and counts) and `OPENAI_REENTRY_CHECKPOINT.md`. `fca7bf1` is
  named as what it is — the last commit of pull request #7, landed on `main`, not a merge commit.
- **C1 — the pull request's records say one thing.** `README.md` rows Next, Claude Code and Working gate carry the EAD
  states as `FINAL_OPEN_ITEMS_REGISTER.md` §1 has them; `design/09_CODE_HANDOFF.md`: the "Not claimed" row states EAD-02's
  true split (automated audit done, two failures fixed, no conformance claimed; the human audit open, release-time), the
  duplicate EAD-11 row is removed, and the test-hooks row reads the measured 27/28 with `scripts/tests/test_public_tools.py`
  modified (two tests added at EAD-06); the register carries a dated correction to its EAD-01 cell.
- **C3 — the double boundary, as a general finding.** `design/ESCALATIONS.md`: every frame prints its boundary twice because
  `scripts/projection/derived.py:1324` ends all 36 contracts' `alt_text` with the prohibited inference while the frame foot
  prints it again; owner the steward; the two per-contract escalations (VIS-INCLUSION-TRANSMISSION, VIS-SOURCE-COMPARISON)
  are marked as narrower statements of the same cause; the register carries a pointer; the decision is the owner's A3 / C3 row.
- **C4 — the `/reforms/` text frame.** `design/06_VISUAL_TABLE_SYSTEM.md` §1 no longer claims the baseline had such a frame
  (it did not): this build shows it, and the owner decided to exclude the RETIRE tier from the domain depth frames (A5 / C4);
  the same note sits on the D7 checklist's "RETIRE never drawn" line.
- **C5 — the register's append rule restored.** A dated erratum in `FINAL_OPEN_ITEMS_REGISTER.md` §9 records the in-place
  rewrite of the eleven "Where it shows today" cells and the class-count cell on 29 September 2026, each previous text
  verbatim with the commit that replaced it; the current cells stand.
- **One-line record fixes** from the acceptance: `README.md` ("The rest are open"; DEBT-008 does not block release and waits
  on the steward and Design, not the owner — A8; the quick start no longer calls `dist/` "the governed baseline");
  `CONTRIBUTING.md` §2 and §4 (`site-src/styles.css` no longer exists); the register's EAD-11 item names
  `scripts/yfie/question_sets.py`; `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` and `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md`
  point to `date_words` in `scripts/yfie/content.py`. `interface_copy.json` and `handoff/IMPLEMENTATION_MANIFEST.json` are
  governed and untouched (fixed in the release-candidate pull request).

Not declared: PUBLIC RELEASE READY. Not claimed: WCAG conformance.

## 2026-09-29 — EAD-02: the implemented site audited; two real failures found and fixed

`scripts/accessibility_audit.py` audits what a machine can decide about the runtime: 24 pages — one per route class,
both languages — at 1440 and 390 px, a 320 px reflow pass (400 % of a 1280 px window), reduced motion, images off and
a keyboard walk, with a pinned general ruleset (axe-core, WCAG 2.0/2.1/2.2 A and AA plus best practice) and the eleven
outcomes of the accessibility contract measured rather than asserted. The record is `docs/ACCESSIBILITY_AUDIT.md` and
`.json`, and it includes the text-alternative table for every drawn visual that the register asks for.

**Two failures against outcomes the contract itself states were found, and fixed.**

- **1.4.3 contrast.** The institutional band's fine print measured **4.42:1** where 4.5:1 is required — on all 288
  pages, in both languages, since D1. `--mute` moved two points darker, `#66717B` → `#646F79`: 4.56:1 on the band,
  5.13:1 on paper. The role is unchanged, the change is imperceptible, and it is the smallest value that meets the
  rule the design published. `design/02_TOKENS.json` regenerated.
- **2.5.8 target size.** Of 129 targets under 24 × 24 px, 117 met one of the criterion's own exceptions — inline, or
  24 px spacing — which is why a bare count would have meant nothing. Twelve met neither: the band's group links, the
  disclosure summaries and the record list inside one, all 22–23 px tall with neighbours closer than 24 px. The design
  already had a rule for exactly this case; it was extended to the three families it had missed.

After the fixes: **0 WCAG violations from the ruleset, 0 contrast failures, 0 targets failing 2.5.8, 0 unnamed
controls or landmarks, 0 unlabelled controls, 0 reflow overflow at 320 px, 0 heading-level jumps, 0 images without
`alt`, and no keyboard trap.**

**Two findings were not fixed, because neither is Code's to decide.** Two navigation landmarks carry the same governed
name — the page's next-actions section and the spine's first edge group — so a screen-reader landmark list shows it
twice; which one changes, and to what, is a composition and naming decision, escalated with three options. And a
figure table's empty corner cell is DEBT-013's recorded preference, which needs a governed label.

**Nothing here claims conformance, at any level.** Screen readers in Arabic and English, whether each heading
describes its section, whether each visual's text alternative carries the same analytical point as the picture, voice
control and switch access, and forced colours judged by eye are all listed as outstanding for the auditor. The
Accessibility page continues to say the resource is designed against WCAG 2.2 and is still to be tested.

## 2026-09-29 — EAD-10: the implemented runtime measured, and what EAD-03 now costs

The pre-design baseline was measured before there was a design. The runtime is measured now, with the same script and
the same twelve route classes in both languages, so the two records compare like with like:
`docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`, with the table in `docs/SUSTAINABILITY_METHOD.md`.

A cold page transfers 9.83–10.19 MB. **94–97 % of that is the canonical logo.** Everything else on the page together —
the document, the stylesheet, the script and the type — is 285–656 KB. A warm page transfers nothing. Opening Search
loads the local index once, about 321 KB with gzip, and only then. The page makes no external request of any kind.

The only increase over the baseline is about 200 KB of self-hosted type, and it buys correctness rather than costing
it: the baseline named IBM Plex and shipped no font file, so a reader without it installed read the product in a
fallback face — Arial, or Tahoma for Arabic. The runtime ships the six faces the stylesheet declares and preloads the
two a first paint needs in the reader's language. HTML is comparable and slightly smaller at the top end; the social
images cost a page nothing, because a platform fetches one when a link is shared and the page never does.

**This sharpens EAD-03 rather than closing it.** The logo's share is no longer an estimate from a pre-design build; it
is measured on the site that would ship. The derivative sizes are listed and the export is one command, but a
derivative of the mark is the owner's to approve, so Code does not run it and the master stays untouched.

**No budget is set and no carbon figure is computed**, and none may be: the release host is not chosen (OWN-03), so
its compression and caching are unmeasured. That half of EAD-10 is release work, and the method says so.

## 2026-09-29 — EAD-06: the search query is URL-addressable; what the facet still waits on

`handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` §2 requires that tool state which matters — Compare records, filters,
the search query — be URL-addressable, reloadable and able to survive a language switch. Compare already met it; the
search did not. The Evidence directory's own search now writes its query to `?q=`, reads it back on load, restores
both the field and the results, carries across the switch to the other edition, and clears the address when the field
is cleared. A query that arrives from the URL is rendered as text and never as markup.

Only the page's own search owns the page address. The dialog floats over whatever page the reader is on, so rewriting
that page's address as they type would change what they would share; a gate and a negative control hold that line in
both directions.

**Two of EAD-06's four parts turned out to be already shipped**, by the accepted design, at the cutover: entry into
Compare from exactly the thirteen comparable records with that record pre-selected, and the mobile form of the
four-column comparison, which stacks below 640 px with every row a block and each cell numbered in the inline-start
gutter. They are recorded rather than rebuilt.

**The result-type facet is blocked, and that is worth stating plainly rather than leaving it to look undone.** Its
option labels are governed (`UI-JS-TYPE-PAGE` … `UI-JS-TYPE-SOURCE-LOCATOR`), but the facet's own accessible name and
the label for the state where no type is chosen are not, and Code does not author a label. The source directory's
control cannot stand in: it says "Find a source by title". Escalated as `NEEDS_CONTROLLED_CONTENT`. The search status
total ("10 of 79" rather than "10 results shown") remains blocked on the governed `{n} of {m}` form escalated at D7 —
a query matching 79 records still reads as a corpus of ten, and no amount of engineering fixes that without the form.

## 2026-09-29 — The D6 runtime defect fixed: governed dates no longer reverse in the Arabic tools

Design found this at D6 on the printed Arabic Compare page and escalated it to Code, because it never edits the
runtime: `site-src/app.js` wrote each record's governed period into a table cell as plain text, and after Arabic
letters the two ISO dates rendered with their parts reversed — "07-11-2022 إلى 09-01-2023" for a period that runs
2022-11-07 to 2023-01-09. The date a reader saw was not the date the record holds.

Every page already isolates those runs in its own text layer. The runtime now uses **the same expression**, character
for character — `scripts/yfie/text.py` `LTR_RUN`, covering ISO dates, numeric ranges and signed values — through one
helper, so a value a tool writes into a page reads the same way as one the page was rendered with. It is applied
wherever governed record text reaches an Arabic page, not only in the cell the lens happened to read: the Compare
table's cells and column heads, the boundary paragraphs beneath it, the record links, and the search results' titles,
summaries and period line.

Two things keep it from drifting back. `scripts/validate.py` fails if the runtime's expression is not the renderer's,
or if the helper is gone; and `scripts/tests/test_gate_negative_controls.py` proves both of those still fail, on the
source file rather than on a built page — the suite now accepts controls on either.

## 2026-09-29 — EAD-05: the Method & Measurement navigation group

Design owned this decision and had made it; it is recorded here as shipped rather than as work. The group is a named
`role="group"` whose governed label is a non-link `glabel`. At 900 px and above a hairline sets it off from the other
destinations and its label sits on the links' baseline; inside the opened menu below that width it stacks under a
quieter label. Both labels and both destinations are unchanged and governed, and the same holds in Arabic.

## 2026-09-29 — EAD-09: the governed social images, and `og:image`

`scripts/social_images.py` rasterises the design's own social templates — one 1200 x 630 frame per route and language,
filled only with governed text (`design/08_ASSET_MAP.md` §4) — into 286 PNGs, and `scripts/build.py` copies them into
`dist/assets/social/`. Every page now carries `og:image` (root-relative before the owner sets a public origin, absolute
after, like every other URL in the discovery contract), its declared size, `og:image:alt` (the page's own title) and
the `summary_large_image` card type. No new text: the templates print what the page already prints.

**Two assertions written for the state before the images existed moved with the feature rather than being dropped.**
Gate F6-G01 asserted that no page carried an `og:image`; it now asserts that each page carries its *own* governed
image, at the declared size, present in the build, described by its own title. `check_acceptance.py`'s `no_og_image`
criterion is repointed the same way. `scripts/tests/test_gate_negative_controls.py` gains two controls that prove both
still fail: an `og:image` naming an image the build does not ship, and one that loses its declared size.

**Why the images are committed rather than made during the build.** Rasterising needs a browser; `scripts/build.py`
must stay standard library only and finish in seconds, because it runs inside every Master transaction and in a CI job
with no Chromium. So they are build inputs, regenerated by one documented command and committed — the same promise
`dist/` makes, that the reviewed bytes are the served bytes. Staleness is caught without rendering anything:
`scripts/social_images.py --check` rebuilds every template in pure Python and compares its SHA-256 with the one
recorded when the image was made, so a governed string changing anywhere fails the check and names the routes to
regenerate. Comparing rendered bytes instead would make a Chromium version bump look like a content change.

**The cost, stated plainly: 17.1 MB of generated PNG, committed.** That is a real addition to the repository, for a
feature that only takes effect once a link to the site is shared publicly. It is recorded in
`FINAL_OPEN_ITEMS_REGISTER.md` with the three steps that reverse it, so the owner can decide otherwise without
archaeology. Git stores the content once even though the files appear both as inputs and inside `dist/`.

## 2026-09-29 — EAD-01 on `claude/hopeful-mccarthy-jgip83`: one production runtime; the replaced renderer removed

The accepted Design implementation becomes the repository's renderer. `design/reference/yfie/` moves to
`scripts/yfie/` (by `git mv`, so its history follows it) and `scripts/build.py` becomes a thin driver over it, writing
the complete static site a host serves: 288 documents in both languages, the neutral root entry, the bilingual 404,
`robots.txt`, and `sitemap.xml` once the owner sets an origin. The 1,643 lines of baseline page composition are
deleted, and `site-src/styles.css` with them. `design/reference/` keeps its harness and its six checks and now builds
**through** the production package, so those checks protect the code that ships; it holds no renderer of its own.
There is one production renderer, reached by one production entry point.

No governed value, wording, unit, universe, period, evidence state, source relationship, limitation or Arabic term
changes, and nothing under `authority/`, `audit/`, the projections or the two controlled contracts is touched.

**EAD-04 closes with it, by construction.** The recolouring of the logo (`brightness(0) invert(1)`) lived only in the
baseline stylesheet, which no longer exists or ships; the accepted stylesheet contains no filter, blend or mask.
**EAD-08 narrows**: the build ships the six IBM Plex faces the stylesheet declares, with their licence, instead of all
twenty-four, and the two first-paint faces stay preloaded per language.

**Parity is proved, not asserted.** The pre-design renderer's own answer was frozen before it was removed:
`scripts/tests/baseline_content_oracle.json` holds, for all 286 documents, the normalised number multiset of `<main>`
and its rendered text as that renderer gave them at `2f9a93c`, with the SHA-256 of every projection it was derived
from. `scripts/tests/test_cutover_parity.py` holds the new output to it at `design/reference/check_content.py`'s
strength — no governed number lost, none gained ungoverned, no governed sentence lost — and reports 286 documents, 0
differing. It was proved in both directions before it was trusted: it fails when a governed paragraph is dropped from
one record and when one governed number is altered.

**The cutover found a real defect, and it is fixed here.** Explore's four question clusters were not governed:
`scripts/handoff_inventory.py` recovered them by scraping the baseline renderer's own HTML out of `dist/`, and the
accepted renderer read them back from that inventory — a build that was an input to itself. Removing the baseline
renderer emptied the scrape, the inventory recorded four empty clusters, and `/explore/` rendered with no questions at
all. The R8.4A sets (Home's four starting questions and Explore's four clusters) now live in one named place,
`scripts/yfie/question_sets.py`; the inventory reads them from there and parses no markup; and the regenerated
inventory is byte-identical to the accepted one at `2f9a93c`, so the selection is provably unchanged. EAD-11 stays
open — the sets belong in a governed contract, which is the steward's to land — but nothing is recovered from rendered
markup any more. This corrects the planning appendix of 29 September, which recorded that Explore's clusters "already
come governed, through the handoff inventory's `question_groups`": they came from the baseline's markup.

**Every gate keeps its assertion and changes only how it finds things.** Built into `dist/`, the accepted design
raised 2,332 validator failures, all of them selectors written against the baseline's class names and attribute order;
all are re-pointed and the validator is green. Two were outright regex faults the new markup exposed rather than
selector drift: `\bid="` also matched `data-record-id="`, so every record page reported a duplicate DOM id, and
`<th(?!…scope=)` also matched `<thead>`, so every table reported a header cell without scope. Where the accepted
design repeats governed text by design — a clock-first object carries its own period, universe and summary — P1-G06
keeps the scope it always had, the page's authored prose, and a duplicated authored paragraph still fails it.

**P3-G02 is replaced, not deleted.** It asked that the pre-design baseline draw nothing. It now checks each drawn
visual against its contract: only a contract the renderer's own registry may draw is drawn, a contract that binds rows
must print every one of its governed row values, its tier must be one that plots, its governed title and the grammar
label of every state and marker it carries must be printed, it must carry the ordered-text fallback and a captioned
value table with a column header, a contract that binds no rows may draw governed structure but no value scale, a
graphic outside a governed figure fails, and every drawable contract must reach both editions.

**Every re-pointed gate is proved to still catch its own fault.** `scripts/tests/test_gate_negative_controls.py`
breaks one thing in the built site at a time — an `aria-current` removed, a breadcrumb dropped, a governed row value
rounded, a question dropped from Explore, a decorative graphic added — and requires the gate to say so. A re-pointed
selector that silently matches nothing would pass the suite and fail these.

Nothing here declares PUBLIC RELEASE READY, and no WCAG conformance is claimed: the EAD-02 audit is still to be done.

## 2026-09-28 — Design D7 closure on `claude/dreamy-archimedes-e8qx5v`: every recorded blocker settled, the product judged by independent lenses; ready for independent acceptance

The closure the owner asked for after withholding acceptance at the technical checkpoint below. It changes the built
product, not the governed content: no governed value, wording, unit, universe, period, evidence state, source
relationship, limitation or Arabic term is touched, and no interface copy is authored.

The one blocker is closed. **DEBT-019** — `/explore/` rendered its governed section 5 twice, the second time as an
answer with no questions under it, and the rubric ordinals disagreed with the page index. The section now renders once,
at the top, as the answer that holds the clusters it introduces (its governed role as the rubric, its governed heading
as the `h2`, its body as the clusters' introduction, the interface lead kept so text parity holds), and a section
rubric's ordinal is now its position in the spine index in every family renderer, which also closed the same latent
mismatch on `/people/`, `/evidence/`, Compare and `/data/` (DL-D7-007).

The four visual debts are settled. **DEBT-016**: the lockup carries the publisher's name in type — the mark plus
**CauseWay** (semibold, the ochre role) above the governed product name, in the product bar of every page, the export
identity line, the social head and the print head, as an isolated left-to-right run in Arabic; the name is the proper
name the governed strapline, citation lines and © line already print, so nothing is authored, and the publisher is now
named on twelve of twelve measured entry screens. The debt stays open on the 10 MB master file alone, which blocks
release, not the gate (DL-D7-008). **DEBT-014/015**: every composed page renders the strip where its phone reader first
needs the map and the foot spine keeps only the edge groups; the governed statement is neither split nor shortened, and
the phone head's rhythm brings the first figure group onto Home's first screen in both languages (DL-D7-009).
**DEBT-007**: decided as restraint, with the reasoning recorded; no motif, border, map, image or new palette.
**DEBT-011 is the closure's recorded no.** Closing both `/data/` dependency groups by default cut the page 44 %
(50,291 → 28,004 px EN, 54,555 → 29,012 px AR at 1440 px) and every design check passed (DL-D7-010), but the full gate
suite then caught that the supporting group is the only place a locator-only source appears: closing it put the
governed "cite a source by its reference and locator" path behind a disclosure and `scripts/tests/test_public_tools.py`
fell from 25/26 to 24/26. Design does not edit a repository test so its own change can pass, so the change was
reverted and the debt left open, with the measured prize and the constraint recorded for whoever takes it next and a
new `check_site.py` assertion (`locator_only_source_reachable`) so the next attempt meets that wall inside the design
checks rather than at the repository gate (DL-D7-013).

The product was judged by three independent lenses on the built pages — an Arabic-first reader, a cold reader arriving
on one Evidence Record, and a phone reader — each writing its report into the repository as it went
(`design/evidence/d7/cold_read/lens-*-closure.md`). Four interface defects they found are fixed (DL-D7-011, DL-D7-012):
the governed source intro promised "Open the source record here" on the ten records that render no source card and was
denied by the next sentence, and now prints only where a source card exists (20 documents affected, 0 remain); the
flagship same-year figure now repeats its governed unit in the axis row, so a hostile crop carries it (the marker that
prevents the figure reading as a fall already survived every such crop); the phone strip on Compare moved from 71 % of
the scroll to 8 %; and every Arabic section heading, which rendered 30 % smaller than the prose it introduced because
the English uppercase-and-tracking device cannot transfer to a script without case, is now sized against its body.

Recorded rather than claimed, each with its measurement: two first-screen shortfalls (the Arabic record's limit index
entry 3 px below the fold at exactly 390 × 844; the Reading's phone screen whose only forward link is the breadcrumb,
because the governed boundary rightly displaces the strip), `/data/` still long on a phone, in-flow targets at
30–33 px against the recorded 24 px minimum, and the percent sign's two individually-correct sides in Arabic. Escalated
as content (`design/ESCALATIONS.md`): the Compare contract's governed `alt_text` ends with its governed
`prohibited_inference` verbatim, so two sentences print twice; CLM-039 carries no values or dates for its central
comparison; and the magnitude notation, strengthened with the closure's evidence — two independent trained readers in
two sessions have now misread a governed value by a factor of a thousand from it alone.

The three reader walks are recorded with what was clumsy, the 18 catalogue-only coverage rows are settled with the
reason each cannot be proved without inventing an evidence record, and the bar of the closure brief is answered surface
by surface in `design/10_ACCEPTANCE_CHECKLIST.md` §K.5. All 73 acceptance lines are met and no design debt is flagged
"blocks D7"; DEBT-008 and DEBT-016 remain open as release items. Records: `design/00_DESIGN_README.md` (status and
DL-D7-007…012), `design/10_ACCEPTANCE_CHECKLIST.md` (§K.4 adjudications updated, §K.5 new),
`design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/08_ASSET_MAP.md`, `design/09_CODE_HANDOFF.md`,
`design/DESIGN_DEBT.md`, `design/COVERAGE.csv`, `design/ESCALATIONS.md`, `design/evidence/d7/`, and the README's
design-programme section and programme tracker. **D7 is not declared accepted and nothing is declared PUBLIC RELEASE
READY:** the owner's visual acceptance, and the content and runtime items escalated to the steward and to Code, remain.

## 2026-09-28 — Design D7 technical checkpoint on `claude/dreamy-archimedes-e8qx5v`: every check green, the technical criteria evidenced; final visual acceptance withheld by the owner

Branch `claude/dreamy-archimedes-e8qx5v` (from the accepted `main` `0ccdf01`, the merge of pull request #6). D7 is the
acceptance of the runnable, fully populated bilingual reference site (`design/reference/`: 288 documents, every tool and
state, both languages, four widths) against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`. At this checkpoint every D1–D6
check, the three repository suites and the new D7 check pass on the tree, and the technical criteria are evidenced line
by line in `design/10_ACCEPTANCE_CHECKLIST.md` (new); the owner has withheld the final visual acceptance, so D7 is not
declared met, the Design package is not declared accepted, `design/COVERAGE.csv` keeps its rows at `VERIFIED`, and the
README is not reconciled. The D7 check `design/reference/check_acceptance.py` (new) asserts what no earlier check did —
strict CSP on every document and frame, the discovery head byte-equal with `dist/` on every edition page, one `h1`, the
skip link, the language switch, the trust layer, no download or bundled document, the nine no-locator sources never
named, the CLM-044 value never printed, every external locator with its cue, the shipped fonts and licences (14,248
static assertions) — and drives the last-ten-percent surfaces of the brief in EN and AR with evidence (59 assertions;
`design/evidence/d7/`). Fixed at the checkpoint: the provider matrix (VIS-PROVIDER-OBSERVABILITY) is unshipped until its
six labels are governed and renders as its contract's text frame, so no `⟦NCC:…⟧` placeholder ships and the device is
removed (DL-D7-001); the structured data the baseline writes (WebSite, BreadcrumbList, Article) is restored in the
reference head through the one discovery implementation (DL-D7-002); the two critical faces of each page's language
are preloaded (DL-D7-005). An attempt to render Explore's governed section 5 once dropped its governed heading and was
reverted (DL-D7-003; DEBT-019).
DEBT-017 closed by measurement (DL-D7-004); DEBT-002 and DEBT-013 closed. Two independent cold readers (EN, AR) read
the checkpoint tree: their reports are in `design/evidence/d7/cold_read/`, every finding is adjudicated in the checklist
§K.4; two verified design findings stay open and block the acceptance until the resumption (DEBT-018, a governed signed
value in Arabic prose outside the text layer's isolate; DEBT-019, Explore's repeated section 5 and its rubric ordinals
against its index), and the
content findings are escalated to the steward (`design/ESCALATIONS.md`, D7 — among them the `/people/` education
sentence against the FINDEX contract). Records: `design/05_RESPONSIVE_RTL_LTR.md` (new), `design/09_CODE_HANDOFF.md`
(the D7 table), `design/DESIGN_DEBT.md`, `design/ESCALATIONS.md`, `design/03`/`04`/`06`/`08` for the waiting matrix,
`design/00_DESIGN_README.md` (status, plan, DL-D7-001…005). No governed content, projection, contract, `dist/` file,
test suite or audit record changed. Not declared: D7 met, DESIGN accepted, PUBLIC RELEASE READY.

## 2026-09-28 — Design D6 accepted by the merge of pull request #5; present-state records reconciled; D7 next

Pull request #5 (`claude/bold-maxwell-r3o015`, head `125aa44`, D6 proved on that exact tree) was merged into `main` at
`f4739a5` by the repository's normal method (a merge commit) on the owner's instruction after the owner declared D6 met
on `125aa44`; Verify (Governance gates, Browser acceptance) is green on the merge commit. Post-merge checks on `main`:
`125aa44` is an ancestor of `f4739a5` and the merge tree is identical to it; `scripts/checksums.py --check`,
`scripts/repository_manifest.py --check` and `scripts/validate.py` pass; the Production Master (`17db032b…`) and the
Page Specs (`d4574804…`) match the fingerprints the checkpoint, the Context and the README record. The present-state
records that described D6 as pending the owner's merge are corrected in place — the README current-state row, the
Design README status, plan row and D6 sentence, `design/09_CODE_HANDOFF.md`, the process note in
`design/ESCALATIONS.md`. No historical entry is rewritten; no governed content, projection, contract, `dist/` file or
audit record changed. D7 (acceptance against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`) is the next gate and has not
begun. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-28 — Design D6 met on `claude/bold-maxwell-r3o015` (pending the owner's merge of pull request #5): the visual system, portable frames and print system, proved on the final tree

Branch `claude/bold-maxwell-r3o015` (from `2effd8b`), draft pull request https://github.com/CausewayGrp/Financial-inclusion-/pull/5.
Every one of the 36 visual contracts now stands in its tier's form on every route that binds it: thirteen drawn (the
three D6 forms — the provider matrix, three dated lanes, bars from zero without ranks — beside the ten drawn at D1–D2),
twenty-two governed text frames (TABLE_TEXT_FIRST contracts without rows, the SUPPORTING contracts, the Compare tool's
own contract), and the one RETIRE contract asserted absent. Every figure carries the detached frame (title, question,
scope, the boundary once, the credit isolated left-to-right, the canonical link, the edition), a text alternative with
a named-column table in a named region, only the palette's colours, no two labels meeting, and fits 320 and 390 px;
one pass over every finished document (`yfie/text.py`) isolates every ISO date and numeric range left-to-right (in
Arabic a plain date renders reversed and a plain range swaps its ends), and governed English time boundaries print as
the Master holds them, isolated and marked. Portable evidence: export frames for the
thirteen drawn contracts (`out/_export/`, 26 documents; the export control designed, unshipped until OWN-04),
five social-image templates over the eleven families (`out/_social/`, 286 frames from governed text only; Code
rasterises), and the print system (chrome hidden, objects whole, figures with their boundary, a print-only provenance
block with the canonical URL and citation last on every page, the Reading as a document). Typography is authored at
three weights (Regular, Medium, SemiBold; emphasis at 600, never a browser default). Verified on the exact final tree:
`design/reference/check_visuals.py`, five phases (36 contracts × EN/AR on every binding route, 2,856 contract
assertions; 52 forced-colours and print checks on the drawn contracts; 26 export and 286 social frames;
133 print checks on the eleven family routes × EN/AR; 598 documents and frames scanned for a date or range outside
an isolate; 0 failures), the D1–D5 gates re-run (`check_content.py --text`, `check_binding.py`, `check_site.py --gate
d2|d3|d4`, `check_journeys.py`, `check_trio.py`, `tokens.py --check`) and the repository suites on the reference site;
the D4 gate caught one regression the first D6 text layer had introduced (an unbreakable identifier isolate overflowing
seven record pages at 320 px), fixed before the final run. Five red-team lenses (measurement and statistics,
information visualisation and editing, native Arabic editing, journalism with a hostile source owner, accessibility and
frontend engineering) reviewed the built output; every MUST-FIX is closed in the layer that owns it, every content or
authority observation is escalated, never fixed in design, and the one runtime defect found (the Compare table's
reversed Arabic dates, `site-src/app.js`) is recorded for Code with its patch (DL-D6-007, `design/ESCALATIONS.md`). Records:
`design/06_VISUAL_TABLE_SYSTEM.md` and `design/08_ASSET_MAP.md` (new), DL-D6-001…007, `design/COVERAGE.csv` (72 D6
rows `VERIFIED`, print and social rows added), `03`, `04`, `07`, `09`, `DESIGN_DEBT.md` (DEBT-010 and DEBT-012 closed,
DEBT-013 narrowed to the six placeholders, DEBT-017 opened), `design/evidence/d6/`. Six placeholders remain on the site until the
steward governs their labels (five matrix headings and the payment-system-operator class). Runtime, projections,
contracts and `dist/` untouched. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D5 accepted by the merge of pull request #4; present-state records reconciled; D6 opened

Pull request #4 (`claude/epic-cori-60fpeb`, D2 met at `9c263ac`, D3 at `beecdbb`, D4 at `aee1e1b`, D5 at `8be8e22`) was
merged by the owner into `main` at `2effd8b`; Verify (Governance gates, Browser acceptance) is green on the merge commit.
The present-state records that still described D1 as the last accepted gate and D5 as pending the merge are corrected
in place — the README current-state row, the Design README status and plan table, `design/09_CODE_HANDOFF.md`,
`design/07_INTERACTION_ACCESSIBILITY.md` — and a process note records the D6 branch (`claude/bold-maxwell-r3o015`,
created at `2effd8b`). No historical entry is rewritten; no governed content, projection, contract, `dist/` file or
audit record changed. D6 (the remaining visual contracts, detached and export frames, social-image templates, print and
portable evidence) is the working gate. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D5 (in progress): every tool state, technical state and journey proved by keyboard; the technical voice

Same branch and draft pull request (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D4 met at `aee1e1b`). `design/reference/check_journeys.py` walks the inventory's thirteen journeys by keyboard at 390 and
1440 px in English and Arabic (52 of 52 walks: a link the page offers takes focus, shows the outline, activates with
Enter; each landing asserted against the journey's success condition) and drives every technical state in both
languages (28 of 28: Compare's link errors and the same-record state, search no-match and index-unavailable, the
register's unknown deep link and no-match, record-context unknown/malformed/valid, the language switch with state, no
script). A third voice is designed for technical states — a dashed hairline, body ink, never the boundary's double rule,
the counter colour or an evidence-gap object (DL-D5-001) — and the same-record state no longer reads as an assessment.
`design/07_INTERACTION_ACCESSIBILITY.md` records the three voices, the keyboard paths, motion, zoom, forced colours, no
script and print, every technical state and journey, and the two verification states no record carries today (designed
with their governed copy, never on an invented record). Records: `design/COVERAGE.csv` (82 D5 rows `VERIFIED`, 4
`DESIGNED`), DL-D5-001…004, `design/03_COMPONENT_CATALOG.md`, `design/09_CODE_HANDOFF.md` (state at D5),
`design/DESIGN_DEBT.md` (DEBT-014 narrowed), `design/ESCALATIONS.md` (the external-link cue raised),
`design/evidence/d5/`. Runtime untouched. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D4 (met at `aee1e1b`): every document bound and asserted; the binding proved

Same branch and draft pull request (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D3 met at `beecdbb`). Every evidence record is asserted against its own governed bundle — the seven questions, the
boundary on first load, the clock before the claim, source cards equal to the bundle's sources with public locators
only, the lineage state and members exactly where carried, the no-locator states, the trace chips, the Compare entry,
the own visual, the boundary once per frame — and the three remaining domain answers (`/firms/`, `/finance/`,
`/providers/`) against their contracts (`design/reference/check_site.py --gate d4`: 904 renders, 452 smoke tests, 3,822
hard-state assertions, 10 degraded renders, all pass; the neutral root entry asserted). `design/reference/check_binding.py`
proves the binding from the inventory's projection roles (every RENDER and CONTRACT projection read by the one content
path; no REFERENCE or VIA_SPEC projection read; 286 edition pages + root + 404; no copied content model) and the one
deviation it found — `public_claims.json` loaded and unused — is removed. Records: `design/COVERAGE.csv` (841 D4 rows
`VERIFIED`; every route row of the ledger is now `VERIFIED`), decision log DL-D4-001…004, `design/09_CODE_HANDOFF.md`
(state at D4), `design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/DESIGN_DEBT.md`, `design/evidence/d4/` (42 PNG). Not
declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D3 (met at `beecdbb`): the synthesis pages composed and proved; the Home cold-reader test run and acted on

Same branch and draft pull request as D2 (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D2 met at `9c263ac`, not yet merged — process note in `design/ESCALATIONS.md`). The Reading index, the ten Readings,
Measurement, Methodology, the eight trust pages and the bilingual 404 are reviewed in both languages at 390 and 1440 px
and asserted on the rendered DOM (`design/reference/check_site.py --gate d3`: 168 renders, 84 smoke tests, 252 hard-state
assertions — the Reading's boundary-before-essay, clocks, trace and measure; Measurement's ten equal, unnumbered,
deep-linkable priorities; About in plain language; Contact and Corrections with the report path — and 18 degraded renders,
all pass; the measure assertion corrected from a guessed width to the measure property, DL-D3-004). Four fresh cold
readers (English and Arabic, 390 and 1440 px) read only the rendered Home page; their reports are kept verbatim in
`design/evidence/d3/cold_read/` (DL-D3-001). The design findings are corrected within the Lock (DL-D3-002): the governed
product statement and its two actions open the page before the first figure (the baseline's order); one link per compact
evidence object, named by the action and the title; the figure's boundary printed once, in the foot, under the governed
"What not to conclude" label; a text frame shows its description as its body; the framing record sits in the section it
frames; the boundary's double rule spans the column; the primary-nav group set off by a hairline; the Arabic rubric 14 px
(`design/02_TOKENS.json` regenerated). The content findings (date forms, precision, jargon, the alt text that restates
its boundary, the text-first label, the publisher's legibility, Arabic calques) are escalated, none filled with authored
copy. `check_site.py` gains the Home assertions and the Orientation hooks. Records: `design/COVERAGE.csv` (164 D3 rows
`VERIFIED`), `design/DESIGN_DEBT.md` (DEBT-014…016), `design/ESCALATIONS.md`, `design/09_CODE_HANDOFF.md` (state at D3),
`design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/03_COMPONENT_CATALOG.md`, `design/evidence/d3/` (38 PNG). Not declared:
DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D2 (met at `9c263ac`): the hard families built and proved; every document renders; the D1 residuals reconciled

Branch `claude/epic-cori-60fpeb` from the accepted `main` (`851f496`, the merge of pull request #3), landing through
draft pull request #4 (https://github.com/CausewayGrp/Financial-inclusion-/pull/4). The one content
path now loads every family (`design/reference/yfie/content.py`), `families.py` composes Explore, the domain answers,
the Evidence directory, Compare and Data & sources in the T4 grammar (and the Reading index, Measurement and trust pages
by the family rule until D3), `visuals.py` draws VIS-FINDEX-GAPS, VIS-REMITTANCE-MACRO, the POS small multiple,
VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-COST and the payment chain per contract with the evidence-state grammar, and
`build.py` writes all 288 documents plus the root entry, the 404 and `robots.txt`. `check_site.py` asserts each §9.2
hard state on the rendered DOM (168 renders, 84 smoke tests, 157 assertions, 20 degraded renders, all pass); the two
repository browser suites (25/26, 168/168), bilingual invariance (0 of 143) and `check_content.py --text` (288
documents; its number rule is bundle-scoped and its text rule inline-tag-safe) pass on the reference site; a rounding
fault in the number formatter was found and fixed. The five D1 residuals are reconciled by their true authority
(DL-D2-002): the Arabic credit line (the contract's own language note; isolated left-to-right), the in-page navigation
name (`aria-labelledby` from governed text; DEBT-006 closed) and Home's order (brief §4.5) are closed; the pacing
marker and the IMF lane state stay open for the steward. Records: `04_PAGE_FAMILY_COMPOSITIONS.md` and
`03_COMPONENT_CATALOG.md` created; `COVERAGE.csv` — 190 D2 rows `VERIFIED` (176) or `DESIGNED` with the gap explained
(14), 1,001 D3/D4 rows `BUILT`; `DESIGN_DEBT.md` (DEBT-004, -006, -009 closed; DEBT-011…013 opened); `ESCALATIONS.md`
(two raised: fallback-table column labels; rows for VIS-TARGET-RESULT-STATE and VIS-MFI-DIVERGENCE);
`09_CODE_HANDOFF.md` state at D2; `02_TOKENS.json` regenerated; `design/evidence/d2/` (60 PNG). README current-state
row updated. No governed content changed; no projection, contract, `dist/` file or audit record edited.

## 2026-09-27 — Design D1 hand-back: second independent pass; residuals closed; verdict recorded

Same branch and pull request; the D1 hand-back is posted on the pull request. A second, fresh repository-only reviewer
confirmed every MUST-FIX of the final review closed and returned "D1 DESIGN COMPLETE — OWNER MERGE REQUIRED"
(`design/exploration/d1_canvas/review/second_pass.md`; `design/01_FOUNDATIONS.md` §6; DL-D1-008). Its residuals are
closed here: the eight verified grammar rows' note field repaired in `design/COVERAGE.csv`; no empty "Source:" line on
a figure without a credit; a round tick step derived once from the data (0 / 2,000 / 4,000 / 6,000); the 320 px table
measurement corrected to 23–80 px (DEBT-010, `01_FOUNDATIONS.md` §2.5, §3.4, §4.4); the lens reports' path corrected;
three overstated sentences corrected (what the checks cover; a selector that matched nothing; the attribution of the
text and degraded checks in README); 24 px hit areas on every non-inline link and button in `main`, asserted by
`check_trio.py` together with a forced-colours emulation; the foot spine's edges kept in print; PNG evidence
regenerated. README current-state row updated. No governed content changed; D1 exit is the owner's merge decision.

## 2026-09-27 — Design D1: independent final review adjudicated; corrections; evidence committed

Same branch and pull request. A repository-only final review (`design/exploration/d1_canvas/review/final_review.md`)
returned NOT ACCEPTED with eight MUST-FIX items; all are closed and re-verified (`design/01_FOUNDATIONS.md` §6, §4.4;
decision DL-D1-008): the Home system visual renders through its contract frame (boundary, scope, credit, link); one
verification spine at any width with the index at the foot on phones; readable fallback tables at 320 px; forced
colours keep chart text; the record's disclosure content prints; the F6 attributes the validator requires are
carried; every governed kicker, label and gloss the baseline prints is rendered and `check_content.py --text` proves
text-block parity; `02_TOKENS.json` is generated and checked by `design/reference/tokens.py`; `check_trio.py` gains a
keyboard-only path, degraded-state checks and the committed PNG evidence (`design/evidence/d1/`, 18 files); records
corrected (`01_FOUNDATIONS.md` status and stub, `09_CODE_HANDOFF.md` rows, DEBT-003 closed, DEBT-010 re-measured,
grammar-state ledger rows reconciled); the nine lens reports and the review committed. Two items recorded rather
than changed (Home section order for steward confirmation; navigation without JavaScript below 900 px). No governed
content changed.

## 2026-09-27 — Design D1 (in progress): reference implementation of the stress trio; Design Intent Lock; tokens

Same branch and pull request. `design/reference/yfie/render.py` (composition of the converged direction with every
brief §19 hook), `theme.py` (the one stylesheet, extracted once from the converged composer; print, focus, reduced
motion and forced colours included) and `visuals.py` (RV-CWR-001 drawn with percentage coordinates, no inline style)
render Home, `/evidence/CLM-003/` and `/readings/same-year-different-number/` in both languages; `check_trio.py`
applies the viewport suite's conditions, the hooks and an interaction smoke test with the baseline runtime (24 renders,
12 smoke tests, all pass); content parity and bilingual invariance pass; `check_content.py` now excludes axis tick
labels. The rendered pages were placed on the canvas as row R beside T4 for the drift review — no drift
(`design/01_FOUNDATIONS.md` §4.4). Written from what renders: the Design Intent Lock (§4: MUST PRESERVE / MAY IMPLEMENT
DIFFERENTLY / MUST ESCALATE), the foundational grammar (§5) and `design/02_TOKENS.json`. Records: decision DL-D1-007,
`COVERAGE.csv` (28 stress-trio rows `VERIFIED`, `code_handoff` YES), `DESIGN_DEBT.md` (DEBT-002 updated; DEBT-009,
DEBT-010 opened), `09_CODE_HANDOFF.md` (implementation, print, runtime, temporary vs intended). No governed content
changed. Not yet: the independent final D1 review; D1 is not exited.

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
