# D1 final review — stress trio (independent, repository-only)

Reviewed: `claude/practical-cray-sr26c5` at `1c0846d` (a commit landed during the review; tree clean, in sync with origin). Master `17db032b…`, Page Specs `d4574804…`, logo `5830163d…` match. Only `design/**`, `docs/CHANGELOG.md`, `README.md`, `.gitignore`, manifest and checksums differ from `origin/main`. Run: build 6 documents; `check_content` PASS; `check_trio --shots` 24/24 renders, 12/12 smoke tests; `bilingual_invariance` 0 of 3 pairs; `checksums --check`, `repository_manifest --check` current. No `_review/degraded/` exists and no committed script produces one.

## 1. Cold-developer test

| Question | Status | Where |
|---|---|---|
| Authoritative | answered | README.md:9–11, 22–23; AGENTS.md |
| Accepted | answered | README.md:20 (D0 at 8bf19ef); 00_DESIGN_README.md:3–8 |
| Provisional | partly | 01_FOUNDATIONS.md §3.7, §4.2 — but its STATUS (3–6) says §4/§5 are "not yet written" |
| Rejected, why | answered | 01_FOUNDATIONS.md §3.2; DL-D1-006 |
| Implemented | partly | 09_CODE_HANDOFF.md D1 table, contradicted by its rows 25, 26, 31, 32 and lines 45–48 |
| Design / Code / Owner-owned | answered | 09_CODE_HANDOFF.md:38–53; ESCALATIONS.md; DESIGN_DEBT.md |
| How it builds | answered | 00_DESIGN_README.md:28–35; build.py |
| Tests that must pass | partly | check_trio / check_content / bilingual named; the degraded-print review and the "programmatic" order comparison (§4.4:632, 655–657) have no tool in the repository |
| Not to be reinterpreted | answered | 01_FOUNDATIONS.md §4.1, §4.3; 09_CODE_HANDOFF.md:38–44 |
| Next | answered | README.md:20; 00_DESIGN_README.md:3–6 |

## 2. Truth and consistency

- 01_FOUNDATIONS.md:3–6 says §4 and §5 "are not yet written"; they are (560–690), and a second "## 5 … Not yet written" stub remains at 692–694. 00_DESIGN_README.md:3–6 and CHANGELOG:3–16 say the opposite.
- 09_CODE_HANDOFF.md:25 "hooks CARRIED by the neutral harness", :26 "TOKENS NOT YET EXTRACTED", :31 "UNDER TEST", :32 "CONSTRAINT NOTED", :45–48 "Nothing implemented by Design yet" — contradicted by 02_TOKENS.json, render.py and DL-D1-007.
- 02_TOKENS.json:53–56: corrupt key `"\n--fs-body"` with an empty role inside `colour`; Latin narrow body size missing from its section. DL-D1-007:364 says the file is "generated" — no generator exists.
- DEBT-010, §2.5:374, §3.4:509: the 320 px table overflows "8–14 px". Measured 40 px (EN) / 46 px (AR), and `.rvtab th{overflow-wrap:anywhere}` with `width:100%` breaks row headers one character per line: the text alternative is unreadable at 320 px, against Lock §4.1.5/.11 ("tables visible").
- §4.4:655–657, DL-D1-007:357–358, 09_CODE_HANDOFF.md:34 cite `_review/degraded/*-print.png, *.pdf` as proof; nothing in the repository writes them. Print, no-CSS and image-off claims are unreproducible.
- §3.1:420–421 keeps the nine lens reports behind DL-D1-006 at a git-ignored path; they are not in the repository.
- §3.3:493 and §5:674 say the Reading's index is the foot spine. render.py:155 emits the foot spine without an index and theme.py hides `.spine .index` below 900 px: Home and the Reading (13–17 k px tall on phones) have no in-page index.
- DL-D1-007:366 "forced colours honoured": in forced-colours dark, `.lbl`/`.val` keep `fill:#3D4954/#17212B` on a black figure; printed values and axis labels vanish (theme.py's block covers marks and lines only).
- COVERAGE.csv:1197–1236: 40 grammar rows carry gate D1 and stay NOT_STARTED while 00_DESIGN_README §6:149 puts "state grammar" in D1; unexplained.
- DEBT-003:10 stays OPEN though its closing condition (convergence) occurred.
- Keyboard: check_trio.py:87–89 tests the first Tab only; search, menu and cite are clicked (104–118). My keyboard pass passed (59 stops, visible focus, Enter/Escape), but the record claims more than the tool proves.

## 3. Governed-content integrity

- Home visual VIS-INCLUSION-TRANSMISSION: render.py:240 hand-builds the frame and drops the contract's prohibited inference ("The relationships are not causal claims…"), scope and credit that dist prints and visuals.py:155–158 would print. A bound visual without its boundary on the flagship page, both languages — a firewall breach (chronology ≠ causality, no composite).
- Duplication: below 900 px both `aside.spine` blocks are visible (render.py:216, 248, 286; theme.py hides `.foot-spine` only ≥900 px), so "Used in these Evidence Readings", "Return to interpretation", the trace and Home's record list print twice on every mobile page. §4.3 says duplication is escalated; §4.4 records "no drift".
- Governed UI strings loaded but never rendered: `UI-HERO-THIS-RESOURCE-PRESENTS-THE-STRONGEST`, `UI-QUESTIONS-COMMON-STARTING-QUESTIONS`, `UI-QUESTIONS-START-FROM-THE-PROBLEM-YOU` (content.py:542–543), `UI-EVID-RETURN-TO-THE-QUESTION-OR` (:347); not recorded as MAY.
- No number outside its bound; parity and invariance pass; no invented public label ("2024 ·", "2021 ·" in visuals.py:136,139 are hard-coded but data-true). check_content.py checks numbers only and strips every `<text class="lbl">` (:28, 63); text omissions such as the Home boundary are invisible to it.
- Home renders sections 3,4,1,9,5,6,7,8 (render.py:230–245) against governed `section_order`; recorded as intent (§4.1.6), not as a reorder.
- The Reading adds a "Sources" section repeating the trace's sources; the figure's alt text prints twice (visuals.py:143 visible, :144 sr-only figcaption).

## 4. Implementation quality

Good: no inline style/script, one stylesheet, §19 hooks and `yfie-ui` byte-equal to dist, head links identical, bdi isolation and Arabic metrics hold, skip link first, focus visible, dialog/menu/cite operable by keyboard, 44 px bar controls.
Defects: print loses everything inside `details.more` — method, change trigger, verification, guidance (render.py:205–208; no print rule); no-JS below 900 px leaves `.nav{display:none}` (routes only via footer); F6 attributes `data-visual-fallback`, `data-noncolour-semantic`, `data-boundary-part`, Home `data-image-independent` are dropped although scripts/validate.py:1206–1236 requires them on public pages; visuals.py hard-codes axis maxima (`vmax=7000`:78; `122-100`:112) and years (:64, 68, 110) — a Master change silently clips the chart; Home pacing keys on hard-coded connectives (render.py:29–31, DEBT-008); standalone action links are 19–23 px tall.

## 5. D1 Definition of Done (00_DESIGN_README §6:149; brief line 859)

Partly met. Met: four propositions on the trio, EN/AR, 390/1440; one chosen with reasons; 01_FOUNDATIONS, 02_TOKENS, DL-D1-001…007; 28 trio rows VERIFIED by reproducible checks at four widths. Missing: the system does not hold at 320 px (unreadable text alternative); a governed boundary is absent on Home; mobile pages duplicate content and lack an index; keyboard under-tested; tokens corrupt; records contradict code (§2).

## 6. Verdict: D1 NOT ACCEPTED — DO NOT START D2

The direction is sound and well argued, the content path is clean, and the trio builds and passes its own checks; but the hand-back fails the truth test the repository sets for itself: the key record declares its Lock unwritten, the Code handoff describes a state that no longer exists, the machine-readable tokens are corrupt, evidence is cited at paths that do not exist, and the implementation breaks Lock items (boundary in frame, tables visible at 320 px, no duplication) that §4.4 certifies as "no drift". Every fix is bounded and Design-owned; once the MUST-FIX list is closed the verdict becomes DESIGN COMPLETE — OWNER MERGE REQUIRED (four escalations still await the steward).

## MUST-FIX (before hand-back)

1. render.py:240 — render the Home visual through `visuals.figure()` so boundary, scope and credit ship in frame.
2. render.py:216/248/286 + theme.py — one spine; below 900 px show edges once and give Home and the Reading an index (strip or foot index).
3. theme.py `.rvtab` — no `overflow-wrap:anywhere` on `th`; let the table exceed the wrapper and scroll; re-measure and correct DEBT-010, §2.5, §3.4.
4. 01_FOUNDATIONS.md:3–6, 692–694 — STATUS to the real state; delete the stub.
5. 09_CODE_HANDOFF.md:25, 26, 31, 32, 45–48 — rows to the D1 state; mark the D0 block as history.
6. 02_TOKENS.json:53–56 — fix the key; add `design/reference/tokens.py` regenerating it from theme.py, with a check.
7. Evidence — add `check_trio.py --degraded` (print, no-CSS, no-JS, image-off PNGs) or strike the claims in §4.4, DL-D1-007, 09_CODE_HANDOFF:34; commit the lens reports or correct §3.1:420.
8. theme.py forced-colors block — `.lbl,.val,.unit{fill:CanvasText}`.

## SHOULD-FIX

- `@media print`: expand `details.more` content, or render it as plain sections.
- check_trio.py — keyboard-only path (Tab, Enter, Escape) and a text-block parity check beside the numeric one.
- Carry `data-visual-fallback`, `data-noncolour-semantic`, `data-boundary-part`, `data-image-independent`; record them in 09_CODE_HANDOFF.
- visuals.py — derive axis maxima and years from the rows; fail loudly on overflow.
- Render, or record as MAY, the four unrendered governed strings; record the Home section reorder in §4.4 and confirm with the steward.
- COVERAGE.csv:1197–1236 — advance the states the trio proves, re-gate the rest, or explain; close DEBT-003.
- Commit first-screen and print PNGs (brief line 829) or record the deviation in a decision.
- Show `.nav` without JS below 900 px; give standalone action links 24 px targets.

## NOTE

- check_content.py:28 — the `lbl` exclusion is a loophole any `<text class="lbl">` can use.
- The figure's "Full record" is the Reading itself (contract route): right in exports, a self-link on page.
- The Reading's Sources section and the doubled alt text repeat governed text; decide and record.
- `discovery.origin()` is None; frame canonicals stay root-relative until OWN-03.
- Commit 1c0846d landed while the final review was pending; that commit is the reviewed state.
