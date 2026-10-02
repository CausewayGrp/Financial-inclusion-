# Independent acceptance of pull request #8 — the production runtime (EAD-01 … EAD-11)

- **Date:** 2 October 2026
- **Reviewer:** an independent acceptance session that did not build the pull request; mandate: verify, adjudicate,
  record; fix nothing. No code, test, governed file, controlled contract, README or register was changed by this
  review. This file is the only file it adds; the one other edit is a single appended row in `audit/INDEX.md`, which
  gate R85-G09 requires for any audit record to exist, plus the regenerated manifest and checksums.
- **Pull request:** `CausewayGrp/Financial-inclusion-` #8, "code: the production runtime — EAD-01 to EAD-11", branch
  `claude/hopeful-mccarthy-jgip83` into `main`.
- **PR head reviewed:** `38147de7b57de869c3746b961e6478b3110f1499` — as expected: `eb2a868` plus the merge of the
  owner's README edit `f9cc187` (the current `main`, which is also the merge base) plus the checksum regeneration.
  Ten commits (`c390f1d` … `38147de`); 922 files changed, +47,551 / −3,552. No commits beyond the expected head.
- **Scope note:** the identifiers E2M-03, E2M-29 and NCC-10 named in the review brief do not occur anywhere in the
  repository; they are treated as the brief's own finding numbers and adjudicated on the repository bytes.
- **Nothing in this record declares PUBLIC RELEASE READY, claims WCAG conformance, or marks any item accepted outside
  this file.**

## V. Verification

### V1. CI on the PR head

Queried through the GitHub API on 2 October 2026. Workflow run `36973482424` on `38147de`:

| Check | Status | Conclusion | Timing (UTC) |
|---|---|---|---|
| Governance gates | completed | **success** | 06:25:35 → 06:26:38 |
| Browser acceptance | completed | **success** | 06:26:41 → 06:28:05 |
| Gate negative controls | completed | **success** | 06:26:41 → 06:42:11 |

At the first query the controls job was still `in_progress` and the PR reported `mergeable_state: unstable`; at the
second query all three were green. The PR is open, not draft, not merged, base `f9cc187`.

### V2. Local run from a clean tree

Checked out `claude/hopeful-mccarthy-jgip83` at `38147de`; `git status --short` empty before, after the gates, after the
design build and after the negative controls. Python 3.11.15, `requirements.txt` installed, Chromium pre-installed.
No test was edited.

| Command (CONTRIBUTING.md §5 order) | Result |
|---|---|
| `scripts/checksums.py --check` | exit 0 |
| `scripts/generate_projections.py --check` | PROJECTION CHECK PASS |
| `unittest discover -s scripts/projection/tests` | Ran 21 tests — OK |
| `scripts/build.py` | Built 288 HTML files from 143 controlled page specs; tree clean afterwards |
| `scripts/audit_public_literals.py` | exit 0; tree clean afterwards |
| `scripts/validate.py` | WEBSITE REPOSITORY VALIDATION PASS |
| `scripts/repository_manifest.py --check` | exit 0 |
| `scripts/tests/test_literal_audit_determinism.py` | PASS: 8 hash seeds, one SHA-256 |
| `audit/pre_tranche_c/source_lineage_truth_test.py` | PASS 8/8 |
| `scripts/architecture_diagrams.py --check` | exit 0 |
| `scripts/social_images.py --check` | exit 0 |
| `audit/tranche_c/checks/bilingual_invariance.py` | 0 page pairs with differing numbers (143 pairs checked) |
| `scripts/tests/test_cutover_parity.py` | PASS — 286 baseline documents checked, 0 differing |
| `scripts/tests/test_public_tools.py` (browser) | PASS — 27/28 passed, 1 not applicable to the current data (the permanent `+`-in-ID skip) |
| `audit/tranche_c/checks/viewport_acceptance.py` (browser) | 168/168 page-width checks pass |
| `design/reference/build.py` | Built 288 documents with renderer `accepted`; 24 export frames and 286 social frames |
| `design/reference/check_content.py` | CUTOVER PARITY PASS — 286 documents, 0 differing |
| `design/reference/check_binding.py` | PASS — 39 projections by role, 286 edition pages + root + 404, 286 bundles |
| `design/reference/check_acceptance.py` (browser) | PASS — 14,820 static assertions on 288 documents and 310 frames; 59 browser assertions in EN and AR; 0 failures |
| `scripts/tests/test_gate_negative_controls.py` | PASS — 32 of 32 faults caught; tree clean afterwards |

Pass/fail counts: every command above exited 0; 0 failures in any suite. The "three browser suites" of the brief are
read as the two CONTRIBUTING.md §5 browser suites plus the browser phase of `design/reference/check_acceptance.py`,
which is the third suite the pull request itself cites.

### V3. Governed content unchanged

```text
$ git diff --stat origin/main...HEAD -- site-src/content authority
$
```

The output is empty (exit 0, 0 lines). No projection, no controlled contract, no authority file and no Master byte
differs between `main` and the PR head. The generator is also untouched: `git diff --stat origin/main...HEAD --
scripts/projection` is empty.

### V4. One runtime

- `site-src/styles.css` is absent on the PR head (`site-src/` holds `app.js`, `assets`, `content`, `deployment.json`,
  `lang-redirect.js`); the diff records `D site-src/styles.css` and `D dist/assets/styles.css`. `main` had a 286-line
  `site-src/styles.css`.
- `scripts/build.py` is 88 lines on the PR head against 1,643 on `main`; it composes nothing and imports
  `from yfie import content as C, render` (`scripts/build.py:37-38`).
- `scripts/yfie/` holds the ten modules of the renderer, recorded by git as renames from `design/reference/yfie/`
  (`R099`/`R100`), plus the new `question_sets.py`. `design/reference/yfie/` no longer exists.
- `design/reference/build.py:28-29` puts `scripts/` on `sys.path` and imports `yfie`; `check_acceptance.py:38-39`,
  `check_binding.py:34-36`, `check_visuals.py:51-53` do the same. The design build ran through that package (V2 table)
  and its three checks passed on the output.

**V4: confirmed.** There is one renderer and `design/reference/` builds through it.

## A. Adjudication

Verdicts: PASS · PASS WITH CONDITION · FAIL. "Not Code's" means the owner of the fix is the steward, Design or the
owner, and the verdict is about what the pull request ships and records.

### A1. Top trust bar removed; trust links footer-only — **PASS**

Evidence:

- `main` (`git show origin/main:dist/en/people/index.html`) rendered `<nav class="trust-nav" aria-label="Trust links">`
  with the seven links *before* `<header>`. The PR head's page has `nav#primary-nav` as the only navigation in the
  header and renders the seven trust routes in the footer as their own named landmark `<nav aria-label="Trust links">`,
  distinct from `nav.groups` ("Product and trust links"). All seven routes present in both editions.
- Contract: `navigation_interaction.json` `trust_navigation` lists the seven routes, About first, as a separate entry
  mode; the same contract's `route_deletion_test.trust_rule` says the trust jobs "are grouped in the footer rather than
  hidden or merged into one legal page". The contract governs membership, labels and order, not screen position.
- Governed Design decision: the T4 direction accepted at D1 (`main` at `851f496`, pull request #3) — `design/01_FOUNDATIONS.md`
  §1 item 5 "Trust links lead the institutional footer band" and §3 item 4 "the trust links lead the institutional
  band"; `03_COMPONENT_CATALOG.md` ("trust links lead the band"); `05_RESPONSIVE_RTL_LTR.md` ("trust links first in the
  band"). The brief (`handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §4.2) gave Design exactly this freedom: "The grouping and
  prominence you give them are yours; the labels and destinations are not."
- Gates: PB-0423 (`scripts/validate.py:1403-1405`) asserts the contract (About first, the seven routes); R4 asserts the
  six trust links on Home. Neither on `main` nor on the PR head does a gate assert header placement; the one baseline
  class count (`footer-nav-group`) was replaced by a contract-driven assertion, not dropped.

Verdict: a governed Design decision, implemented as accepted; not a Code deviation. Minor record note (no condition):
no decision-log entry names the removal of the baseline's top bar, and the validator comment at
`scripts/validate.py:1389` ("secondary, always visible") predates the design.

### A2. "Explore / <question>" back-link removed on the 8 domain pages — **PASS**

Evidence:

- `main` rendered `<nav class="answer-crumb eyebrow" aria-label="The question this page answers"><a href="/en/explore/">Explore</a> / <span class="answer-question">…</span></nav>`.
- The PR head renders `<span class="rubric">The question this page answers</span><p class="q">Who is being left behind — and where are the measured gaps?</p>` (`dist/en/people/index.html`), keeping the governed label
  `UI-ANSWER-CRUMB-LABEL` (once on `main`, once on the PR head) and the governed question, and keeps the way back to
  Explore as the head's first governed action ("Explore questions" → `/en/explore/`) and in the primary navigation.
- The contract's `breadcrumbs` block governs crumbs for the Evidence Record (parent `/evidence/`) and the Reading
  (parent `/readings/`) only; no domain-answer breadcrumb is governed.
- Recorded decision: `design/04_PAGE_FAMILY_COMPOSITIONS.md` §1 Head — "crumb (where governed), rubric, the governed
  question (`p.q`, where the page answers one)"; §2 Domain Answer — "head (rubric 'The question this page answers', the
  governed question as the framing line, `h1` = the answer, lead = section 1) → … the two governed actions (Explore
  questions; Open evidence)". D2 accepted at `2effd8b` (pull request #4). The cutover parity test holds the rendered
  text of `<main>` to the baseline oracle with 0 differing documents.

Verdict: a recorded Design decision, not a regression.

### A3. Every figure prints its "does not establish" line twice — **FAIL** (confirmed; not Code's to fix; must be recorded)

Evidence:

- On the PR head every one of the 58 figures on the English edition prints its contract's `prohibited_inference` at
  least twice (VIS-POS-TRANSACTIONS three times): once inside the visible text alternative ("Does not establish: …")
  and once in the frame foot under the governed label "What not to conclude". Counted over `dist/en/**/index.html`
  against `visual_library.json`; e.g. `/people/` VIS-FINDEX-GAPS 2, VIS-FL-EVIDENCE-LADDER 2; `/reforms/` all five 2.
- On `main` the same inference printed once per figure (VIS-FINDEX-GAPS on `/people/`: 1; "Does not establish:" 0),
  because the baseline did not show the alt text visibly.
- Cause: the governed alt text is composed by the generator — `scripts/projection/derived.py:1324`
  `alt_text = accessible_summary + UI-VIS-DOES-NOT-ESTABLISH + prohibited_inference` — for all 36 contracts (36 of 36
  `alt_text_en` end with the inference). The design makes the text alternative visible (T4) and prints the boundary
  once in the foot (`04_PAGE_FAMILY_COMPOSITIONS.md` §1: "the boundary printed once per frame (D3)"). `check_visuals.py`
  `boundary_once_in_foot` and `check_site.py` `boundary_once_per_frame` count the foot only, so the checks pass.
  The generator and projections are unchanged by the PR (V3).
- Record state: `design/ESCALATIONS.md` raised it at D3 for VIS-INCLUSION-TRANSMISSION ("readers took the repetition
  for a templating fault"), restated it at D7, and at the D7 closure for VIS-SOURCE-COMPARISON — each as a property of
  that contract's governed alt text. The repository record nowhere says that the rule is general (all 36) and lives
  in `derived.py`, and neither the register nor `09_CODE_HANDOFF.md` lists it as a defect that now ships on every
  figure of the public build.

Verdict: FAIL on the shipped output against Design's own "once per frame" rule; the fix is the steward's (one
generator rule, no Master change: end `alt_text` before the inference, or Design hides the governed tail in the frame).
Condition C3 below.

### A4. The 13 VISUAL records without a contract show no method text and no table — **PASS WITH CONDITION** (intended as applied; accidental in effect)

Evidence:

- The 13 records with `visual_contract_state = NO_GOVERNED_CONTRACT__TABLE_ONLY` (`evidence_objects.json`): VIS-PROVIDER-TIME,
  VIS-MFI-SPINE, VIS-FINDEX-SAMPLE-SUPPORT, VIS-FINDEX-ACCESS-USE, VIS-FINDEX-BARRIERS, VIS-FINDEX-RESILIENCE,
  VIS-FINDEX-FLOW-CHANNELS, VIS-FINDEX-OBSERVED-WAVES, VIS-DEMAND-VINTAGE-LADDER, VIS-BORROWING-SOURCES-2014,
  VIS-DOMESTIC-REMITTANCE-PATH-2014, VIS-MFI-2014-PANEL, VIS-MFI-RUPTURE-LENS. None is among the 36 contracts of
  `visual_design_contracts.json`.
- PB-0401 as applied (`audit/tranche_b_execution/ROOT_DISPOSITIONS.json`, `STAGE4_EXECUTION_LEDGER.json`): "NO_GOVERNED_CONTRACT__TABLE_ONLY
  on 13 records (method text not rendered while the state holds)"; `audit/MASTER_FIRST_PATCH_NARRATIVE.md` line 186:
  "no chart without a contract".
- Renderer: `scripts/yfie/content.py:343` and `:561` set `method` to "" whenever `visual_contract_state` is set — the
  same rule as `main`'s `scripts/build.py:1192`. On `main` and on the PR head all 13 record pages print neither the
  method text nor any `<table>` (checked page by page); parity 0 differing.
- Tranche C transaction TC-A rewrote `method_en`/`method_ar` on these records (e.g. `audit/tranche_c/runs/TC-A_MASTER_LEDGER.json`
  lines 1437–1446 VIS-FINDEX-BARRIERS, 12678–12687 VIS-MFI-SPINE); those fields are never printed while the state
  holds. The state's name promises a table, but no row set exists for any of the 13.

Verdict: intended by the recorded PB-0401 rule and faithfully carried over; accidental in effect — governed method text
rewritten at Tranche C never reaches a reader, and the promised table never existed. Not Code's: a steward decision,
Master-first (render the method text, supply rows, or retire the state), and an open item the register does not hold.
Condition C6.

### A5. VIS-CAPITAL-CONTEXT (RETIRE_FROM_DESIGN) renders as an analytical frame on `/reforms/` — **FAIL** (record and composition; no truth defect)

Evidence:

- Contract: tier `RETIRE_FROM_DESIGN`, rationale "a public relationship graph would present context-only data as a
  public analytical object. The Evidence Record text stays."
- PR head `dist/en/reforms/index.html`: `<figure class="fig fig-text" data-visual-id="VIS-CAPITAL-CONTEXT" data-visual-fallback="ordered-text" …>`
  in the depth group `section#views` ("Another view of the evidence"), with the rubric "Analytical question", the
  governed title and question, "Text description of this view", the accessible summary, scope, the boundary, the
  full-record link and the cite action. The record page carries no figure (0 `data-visual-id`), as the contract asks.
- `main` (`f9cc187`) and the oracle baseline (`2f9a93c`): `/reforms/` names VIS-CAPITAL-CONTEXT once, as a record link
  in "All evidence records on this question"; the accessible summary ("This record distinguishes the pathways …")
  occurs 0 times on `main` and is absent from the oracle's `en/reforms/index.html` text; it occurs once on the PR head.
- Design record: `design/06_VISUAL_TABLE_SYSTEM.md` §1 row — "never drawn; its record has no figure; `/reforms/` keeps
  the baseline's governed text frame for parity". The baseline had no such frame; the justification is false on the
  bytes. `check_visuals.py:167-171` `never_drawn` accepts a text-only frame, so the design check cannot see it; the D7
  checklist line "RETIRE never drawn" is literally met. The page spec binds the visual to `/reforms/`
  (`public_routes ["/reforms"]`) and the family rule (`families.py:196`, every bound visual not placed beside a primary
  section goes to depth) draws it.

Verdict: FAIL — a retired contract ships as a public analytical frame on a route where the baseline had none, on a
recorded justification that does not hold. The frame prints governed text only (no values, no graph, no number), so
nothing it says is untrue; it is a Design decision to make and record (exclude the RETIRE tier from the depth frames,
or correct `06_VISUAL_TABLE_SYSTEM.md` and the D7 checklist to say the frame is intended). Condition C4.

### A6. Search status prints "10 results shown" when more records match — **PASS WITH CONDITION** (known, blocked on controlled content)

Evidence:

- `site-src/app.js:156` `const scored=unique.slice(0,10);` and `:159` sets the status from `UI-JS-SEARCH-RESULTS`
  ("{n} results shown") with `n = scored.length`, so never above 10. The governed strings are "0 results shown" and
  "{n} results shown" (`interface_copy.json`); no `{n} of {m}` form exists, and no `UI-JS-SEARCH-*` label exists for a
  "way on" link.
- The PR shipped the `?q=` half (`app.js:126`, `:175`; two browser tests pass) and recorded the status as blocked:
  `design/ESCALATIONS.md` (D7, `NEEDS_CONTROLLED_CONTENT`), `FINAL_OPEN_ITEMS_REGISTER.md` EAD-06, `docs/CHANGELOG.md`
  EAD-06. The D7 handoff row also asked Code to show the total and carry the query to the Evidence directory; neither
  is possible without a governed string, and the escalation says so.

Verdict: the status is literally true and misleading, exactly as recorded; blocked on the steward's `{n} of {m}` form.
No regression against `main`, which printed the same. Condition C7.

### A7. Record contradictions — **FAIL** (the records do not agree on the premises of the pull request)

1. **D7 acceptance status.** `README.md` ("Last accepted gate: D7 — the whole programme accepted", "Design D7 …
   ACCEPTED AND MERGED (28 Sep 2026, `fca7bf1`)") and `design/09_CODE_HANDOFF.md:7` ("The Design programme is closed")
   versus `design/00_DESIGN_README.md` status ("READY FOR INDEPENDENT ACCEPTANCE … The owner has withheld the final
   visual acceptance: D7 is not declared met, the Design package is not declared accepted"), `design/10_ACCEPTANCE_CHECKLIST.md`
   ("FINAL VISUAL ACCEPTANCE WITHHELD … nothing here declares D7 met"), `design/COVERAGE.csv` (1,415 `VERIFIED`, 18
   `DESIGNED`, 0 `ACCEPTED` — "ACCEPTED is written only at acceptance"), and `09_CODE_HANDOFF.md`'s own D7 table ("final
   visual acceptance withheld by the owner"). `handoff/CLAUDE_CODE_MASTER_PROMPT.md` makes Code's start conditional on
   the package being accepted and the checklist complete; the package's records say it is not.
2. **"Code waits for the Design package."** `README.md:43`, `handoff/CLAUDE_CODE_MASTER_PROMPT.md` (STATUS: WAITING FOR
   THE DESIGN PACKAGE), `handoff/README_FIRST.md:154`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` `design_prompt_status`
   ("Claude Code waits for the accepted Design package") and `OPENAI_REENTRY_CHECKPOINT.md:78` versus `README.md` "Now"
   row and the checkpoint's own addendum ("Code has started … EAD-01 landed").
3. **React target versus the Python renderer.** `handoff/IMPLEMENTATION_MANIFEST.json` `implementation_target.ui`:
   "React static pre-render/export"; the shipped runtime is `scripts/yfie` (Python, standard library, no React; the
   manifest is in the runner snapshot and unchanged by the PR).
4. **EAD statuses, README versus the register.** `README.md:77`: "EAD-01 is done … EAD-04 closed with it. The rest
   are open" versus `FINAL_OPEN_ITEMS_REGISTER.md`: EAD-05 CLOSED, EAD-09 CLOSED, EAD-08 SELF-HOSTED, EAD-02/06/10
   part done. `README.md:25` still sends Code to the waiting prompt. The PR body's check "README, the register and the
   Design → Code handoff state the same thing" is not met.
5. **Register rows rewritten in place.** `git diff origin/main...HEAD -- FINAL_OPEN_ITEMS_REGISTER.md` replaces the
   "Where it shows today" cell of all eleven EAD rows and the class-count cell, against the register's own rule
   (§9: "append a dated line under the item's table … do not delete rows"; header: "Later changes are appended,
   never rewritten") and `CONTRIBUTING.md` §2 (`audit/`, `docs/` — "Append; never rewrite a historical record"). The
   previous cells survive only in git history.
6. **EAD-02 inside `09_CODE_HANDOFF.md`.** Row "EAD-02 (accessibility) | AUDITED; TWO FAILURES FIXED; NO CONFORMANCE
   CLAIMED" versus row "Not claimed | … the EAD-02 audit of the implemented site is still to be done". The same table
   lists EAD-11 twice (rows 17 and 22).
7. **Test-suite claims.** `09_CODE_HANDOFF.md` "Test hooks | KEPT; THE SUITES ARE UNMODIFIED | `test_public_tools.py`
   25/26" and the register's EAD-01 row ("both browser suites unchanged (25/26, 168/168)") versus the PR body and the
   measured result (27/28; `scripts/tests/test_public_tools.py` is `M` in the diff, two tests added).
8. **Stale pointers to `scripts/build.py` and to deleted files.** `FINAL_OPEN_ITEMS_REGISTER.md` EAD-11 item column
   ("ID sets held in `scripts/build.py`" — now `scripts/yfie/question_sets.py`); `CONTRIBUTING.md` §2 row
   "`scripts/`, `site-src/app.js`, `site-src/styles.css`" and §4 "Code outside it (`build.py`, `app.js`, `styles.css`,
   `derived.py`, `families.py` …)" (`styles.css` is deleted); `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md:701` and
   `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md:77` ("`source_date_text` in `scripts/build.py`" — no such function
   exists anywhere under `scripts/` now); `README.md` quick start ("the governed baseline: /en/ and /ar/" — `dist/`
   is now the design); `interface_copy.json` `use_rule` "build.py _domain_labels[…]" (governed text, the Master's).
   `README.md:295` ("`dist/` … `scripts/build.py` only") and `handoff/README_FIRST.md` are correct.
9. **DEBT-008's owner.** `README.md:79`: "DEBT-008 and DEBT-016 … block release and wait on the owner" versus
   `design/DESIGN_DEBT.md` (DEBT-008 waits on a controlled pacing marker — the steward, Master-first) and
   `design/ESCALATIONS.md` ("open, non-blocking; DEBT-008").
10. **The baseline frame on `/reforms/`.** `design/06_VISUAL_TABLE_SYSTEM.md` §1 versus the `main` and oracle bytes (A5).
11. **The double boundary.** `design/ESCALATIONS.md` attributes it to two contracts' alt text; `scripts/projection/derived.py:1324`
    applies it to all 36 (A3).
12. **Sustainability pointer.** `authority/YFI_CURRENT_PROJECT_CONTEXT.json` ("remeasure after Design and deployment")
    versus `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json` (the implemented site is measured; only the host remains).

Items 1–2 are the premise of the pull request and are contradicted by the Design package's own records; items 4–7 are
the PR's own records disagreeing with each other; 3, 8, 9 and 12 are pointers the PR left stale; 10–11 are design
records falsified by the bytes. Conditions C1, C2, C5.

### A8. DEBT-008 "Blocks release" although a fallback exists — **PASS WITH CONDITION** (it does not block)

Evidence:

- `scripts/yfie/render.py:197-211` `paced_groups`: splits Home's governed "three figures" paragraph at the governed
  connectives (`GROUP_STARTS`, `RESOLUTION`, lines 28–29) and, when fewer than two groups are found, returns the whole
  paragraph unchanged. Words and order are intact in both branches; no governed text is altered.
- `design/DESIGN_DEBT.md` DEBT-008: user impact "None while the connectives hold; the paragraph falls back to unpaced
  prose if they change"; Blocks: "Blocks release"; `design/ESCALATIONS.md` D1 item: "open, non-blocking; DEBT-008".
- No CI gate asserts the pacing (`scripts/validate.py` has no such check); `design/reference/check_site.py:74` asserts
  `.paced .compact.bound` on Home, so a wording change would pass CI and fail the design harness — a silent
  presentational degradation in CI, never a truth, accessibility or gate failure.

Verdict: it does not block release. The debt is a robustness wish (a governed pacing marker) and its own impact
column says so; "Blocks release" contradicts the escalation's "non-blocking" and the README misassigns it to the
owner. Condition C8: reclassify (or state the release-level harm) and correct the owner — Design and steward, not Code.

## C. Conditions

Before merge (records only; no code change is required of the pull request):

- **C1.** Reconcile the pull request's own records so they say one thing: `README.md` (rows "Next", "Claude Code",
  "Working gate": the EAD states as the register has them; stop pointing Code at a prompt that says WAITING),
  `design/09_CODE_HANDOFF.md` (the "Not claimed" row's EAD-02 sentence; the duplicate EAD-11 row; the "SUITES ARE
  UNMODIFIED / 25/26" row against the measured 27/28 and the modified test file), the register's EAD-01 row (25/26).
- **C2.** The steward settles the premise in writing: either the Design package is accepted — then `design/00_DESIGN_README.md`,
  `design/10_ACCEPTANCE_CHECKLIST.md` and `design/COVERAGE.csv` (`ACCEPTED`) are reconciled as the owner's merge of #7
  intended — or it is not, and `README.md` stops saying "the whole programme accepted". `handoff/CLAUDE_CODE_MASTER_PROMPT.md`,
  `handoff/README_FIRST.md:154`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` and `OPENAI_REENTRY_CHECKPOINT.md:78` then
  stop saying Code waits.
- **C3.** Append to `design/ESCALATIONS.md` (and the register) the general finding of A3: every drawn and text frame
  prints its boundary twice because `scripts/projection/derived.py:1324` ends every `alt_text` with the inference; owner
  the steward; the fix is one generator rule or a Design rule for the visible alt tail. The two existing per-contract
  escalations are narrowed statements of the same cause.
- **C4.** Design (or the steward) records the decision on A5 — exclude the RETIRE tier from the domain depth frames,
  or correct `design/06_VISUAL_TABLE_SYSTEM.md` §1 and the D7 checklist to say the `/reforms/` text frame is intended —
  and the false "keeps the baseline's governed text frame" sentence is corrected either way.
- **C5.** Restore the register's append rule: the eleven rewritten "Where it shows today" cells are either restored
  with dated status lines appended beneath each row, or the in-place rewrite is recorded as a dated erratum in the
  register's §8/§9 with the commit that made it, so the method is not silently changed.

After merge (open items with an owner; none is Code's):

- **C6.** A4: a steward decision, Master-first, on the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY` records (render the
  Tranche C method text, supply rows, or retire the state), added to the register as its own item.
- **C7.** A6: the governed `{n} of {m}` search-status form and a "way on" label (already escalated).
- **C8.** A8: reclassify DEBT-008 (or state the release-level harm) and correct `README.md:79`'s "wait on the owner".
- **C9.** Stale pointers of A7 item 8, the React target of item 3 (`handoff/IMPLEMENTATION_MANIFEST.json` is in the
  runner snapshot and the steward's), and the sustainability pointer of item 12.

## One-line fixes seen and deliberately not made (the review changes nothing)

`design/09_CODE_HANDOFF.md:29` ("still to be done"); the duplicate EAD-11 row at `:22`; `README.md:77` ("The rest are
open"); `README.md:43` ("waits for the accepted Design package"); `README.md:79` ("wait on the owner");
`CONTRIBUTING.md` §2 and §4 (`styles.css`); `FINAL_OPEN_ITEMS_REGISTER.md` EAD-11 item text (`scripts/build.py`);
`handoff/CLAUDE_DESIGN_MASTER_PROMPT.md:701` and `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md:77` (`source_date_text`);
`README.md` quick start ("the governed baseline"); `design/06_VISUAL_TABLE_SYSTEM.md` §1 (the baseline frame sentence).

## Verdict

What the pull request builds is sound: every gate of `CONTRIBUTING.md` §5 is green locally and in CI, including the
negative controls; governed content and the generator are byte-identical to `main`; there is one renderer and the
design harness builds through it; parity with the pre-design build is proved against a frozen oracle. What it ships
carries two Design-level defects that predate it but reach the public build through it (A3, A5) and one state it
inherits unexamined (A4); what it records contradicts itself and the Design package on the premises of the work (A7).
None of the conditions needs a code change from Code; all of the before-merge conditions are record changes the
pull request can carry.

**MERGE AFTER CONDITIONS** — the runtime is verified; the records are not yet one coherent governed state (C1–C5).
