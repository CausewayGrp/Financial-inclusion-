# Records reconciliation — 2 October 2026

Release candidate, Part A G5 (`audit/release_candidate/INSTRUCTIONS.md`). One row per item the brief lists: the finding,
the action, the files. Where a file is generated or inside the runner's snapshot it was changed through its generator or
installed with `audit/tranche_b_execution/run_stage.py --install` (`audit/release_candidate/g5_stage_records.py`,
run report `audit/release_candidate/runs/G5-RECORDS_RUN_REPORT.json`); every other file was edited in place in the same
commit.

**The before-merge conditions C1–C5 still hold.** They were met on pull request #8 (records only) and are not redone here.
Checked against the current bytes after every change of this pull request: no record says Code waits (C1, C2; the one
"CODE NO LONGER WAITS" status line is the corrected state); the general finding of A3 is in `design/ESCALATIONS.md` and its
fix has landed (C3; G4 item 4); the A5 decision and the corrected `design/06_VISUAL_TABLE_SYSTEM.md` §1 sentence stand,
and the frame is removed (C4; G4 item 5); the register's erratum of 2 October 2026 restoring the append rule stands (C5).
The acceptance's one-line record fixes made on pull request #8 are untouched.

| # | Finding | Action | Files |
|---|---|---|---|
| 1 | `handoff/IMPLEMENTATION_MANIFEST.json` `implementation_target.ui` still read "React static pre-render/export" (C9; `audit/PR8_INDEPENDENT_ACCEPTANCE.md` A7 item 3) | Names the Python production renderer in `scripts/yfie` (driven by `scripts/build.py`): static pre-rendered HTML for every controlled route, with the one runtime `site-src/app.js`. Installed through the runner (the file is in its snapshot) | `handoff/IMPLEMENTATION_MANIFEST.json` |
| 2 | `authority/YFI_CURRENT_PROJECT_CONTEXT.json` pointed sustainability at the pre-design baseline, "remeasure after Design and deployment" (C9; A7 item 12) | Points at `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json` (the implemented runtime, remeasured 29 September 2026) and the logo-derivative measurement; only the host remains. Installed through the runner | `authority/YFI_CURRENT_PROJECT_CONTEXT.json` |
| 3 | DEBT-008 "Blocks release" although a fallback ships (C8; A8) | Reclassified: blocks neither D7 nor release; the fallback is the unpaced governed paragraph; owner of the fix the programme steward (a controlled pacing marker, Master-first) and Design. `README.md` already said so (C1 on pull request #8); the register does not list DEBT-008 | `design/DESIGN_DEBT.md` |
| 4 | `OPENAI_REENTRY_CHECKPOINT.md` §4 said "the next work is Claude Design's" | Corrected: Design complete (D7 accepted 2 October 2026), runtime merged (#8), the release candidate is #9, the work after it release-time only. Installed through the runner | `OPENAI_REENTRY_CHECKPOINT.md` |
| 5 | EAD-07's label request sat under "Anticipated (not yet raised)" | Raised as a NEEDS_CONTROLLED_CONTENT entry under Open (the no-type group label for the 9 sources without `document_label`); the anticipated bullet carries a dated pointer to it and is not deleted | `design/ESCALATIONS.md` |
| 6 | Historical ledgers still show items open (`audit/TRANCHE_C_FINDINGS_LEDGER.csv`, `audit/pre_tranche_c/FINDINGS_LEDGER.csv`) | Not edited (historical records are never rewritten). **`FINAL_OPEN_ITEMS_REGISTER.md` §8 governs**: an item those ledgers list as open is open only if the register lists it; the register's §8 records each closure | — |
| 7 | `docs/SUSTAINABILITY_METHOD.md` gave the master logo as 10,018,273 bytes | Corrected to 10,018,081 bytes on disk (10,018,273 bytes on the wire with the response headers), with a dated line for the derivatives' effect | `docs/SUSTAINABILITY_METHOD.md` |
| 8 | `site-src/deployment.json` `state` still read `PRE_RELEASE_REFERENCE_BUILD` after the runtime cutover | `PRE_RELEASE_PRODUCTION_RUNTIME`; `public_origin` stays null (release-only decision) | `site-src/deployment.json` |
| 9 | `docs/CHANGELOG.md` (entry of 29 September, EAD-01) refers to "the planning appendix of 29 September", which is not in the repository | Erratum appended in this pull request's G5 changelog entry (the historical entry is not rewritten): the "appendix" was the session's working plan, never committed; the statement it corrected — that Explore's clusters came governed through the handoff inventory's `question_groups` — is itself recorded in the EAD-11 escalation | `docs/CHANGELOG.md` |
| 10 | `README.md` on IBM Plex, against the shipped runtime | Checked, no change needed: the README says the two families are self-hosted unchanged from `vendor/fonts/` under OFL-1.1 and that the build ships the six faces the stylesheet declares; `dist/assets/fonts/` holds exactly Regular, Medium and SemiBold of each family with their licences, and `yfie.css` declares six `@font-face` rules | — |
| 11 | `README.md` status after this pull request | "Now" names what the release-candidate pull request changes; "Next" says that once it lands the open items are release-time only (register §2); DEBT-016 recorded as closed; the Claude Code start row names #8 merged and #9. Installed through the runner (README is in its snapshot) | `README.md` |
