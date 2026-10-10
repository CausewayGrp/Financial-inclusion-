# Close-out progress (append only)

The live log of the close-out brief (`audit/close_out/BRIEF.md`). One line per finding ID closed, with its pull request
and merge SHA. A later session resumes from this file alone. Lines are never edited; a correction is a new line.

Format: `date · session · workstream · ID · outcome · PR · merge SHA · note`.

## Session A

- 2026-10-10 · A · start · base `main` = `2ddbfb611bb139d9597aec9b6b79153699cc4d94`; open pull requests: none; CI on
  main: Verify run 38061261662 green. Local gates on the base (Python 3.11.17): every CONTRIBUTING §5 gate PASS; cutover
  parity exits 2 (oracle pinned; content parity is the standing gate, as CI accepts); public tools 35/36 (1 not
  applicable); viewport 168/168.
- 2026-10-10 · A · inputs · brief v5 supersedes v4 (owner's mid-session message). `BRIEF.md` is now version 5; version 4
  is kept as `BRIEF_v4.md` for lineage. Owner decisions D1–D15 (v5) recorded verbatim in
  `audit/OWNER_DECISIONS_2026-10-10.md` §5. From here the plan is v5's: one window, stages A–C, a stage report and a
  stop after each stage.
- 2026-10-10 · A · inputs · PR #26 merged at `c8af8e04` (9/9 CI).
- 2026-10-10 · A · W0 · inventory: main `2ddbfb61`, no open PRs, CI green; gates PASS locally. Register: 61 core IDs +
  the appended B16 block; stale rows confirmed (EAD-03/06/07/11 done; EXT-01..03 closed 3 Oct; OWN-01/02/05 done; OWN-04
  closed 10 Oct; REL-02 166 of 167 not assessed). Original-reading reports A2 (IMF/YEM), A3 (CBY), A4 (projects, CCY,
  women's evidence), A5 (register) in `audit/close_out/w0/`; A1 (Findex) pending.
- 2026-10-10 · A · W1 · CLOSE-1 staged and run (runner COMMITTED; Master `58b8f3ec5ac1` → `190b148abf2d`): D1, D3,
  AR-035, OWN-10, CR-04, CR-10, CR-12, CR-18 (DECIDED). CR-03 moved to CLOSE-3 (v5). Gates CO-G01, CO-G02 added with
  negative controls. PR and merge SHA on the next line.
- 2026-10-10 · A · AR-1 · run (runner COMMITTED; Master `190b148abf2d` → `250586ce71ee`): register rows applied 25
  (AR-002 003 005 008 009 010 012 013 016 019 023 026 029 031 037 039 043 045 049 053 056 058 060 061 062), stopped 0;
  AR-060 template copies CLM-039/046/056; AR-062 propagation: identical sentence absent in the 4 listed cells, nothing
  propagated; ADJ-RG-01 closed (/rights/ §2, /data/ §5; /data/ §1 and UI-DATA-REUSE-TERMS-ONCE via AR-008/AR-056).
  Render check in `runs/AR-1_RENDER_CHECK.md`. Register rows still to apply: AR-001, AR-042, AR-022, ED-034, ED-035,
  ED-036, AR-NEW-001 (CLOSE-2); AR-004 (CLOSE-3); ED-037 (CLOSE-5). RETAIN: AR-028, AR-036, ED-038.
- 2026-10-10 · A · W1 · PR #27 (CLOSE-1) merged at `d4241f79` (9/9 CI). Closed: D1/OWN-01, D3, AR-035, OWN-10, CR-04,
  CR-10, CR-12, CR-18 (DECIDED).
- 2026-10-10 · A · W2 · handoff superseded: README_FIRST first line + dated note; prompts' status lines superseded (old
  lines kept verbatim); README, checkpoint, CONTRIBUTING (row and §8), Context (`handoff_readiness` SUPERSEDED), manifest,
  design README note; AGENTS rule 7 (new text) and rule 2 (D14 scope). Runner finding: rebind writes only hashes and the
  manifest's readiness; no regeneration of the status line — recorded, nothing stopped. R86-G01 SUPERSEDED state + 2
  negative controls (caught).
- 2026-10-10 · A · AR-1 · PR #28 merged at `98f2f782` (9/9 CI). Closed: the 25 AR-1 register rows and ADJ-RG-01.
- 2026-10-10 · A · W3b · CLOSE-2A run (runner COMMITTED; Master `250586ce71ee` → `eaa603586d76`): CR-01 CLOSED
  (not asked; evidence in CLM-001 method), CR-02 CLOSED (national intervals from WB DE 1.9; 12 group rows withdrawn),
  CR-14 CLOSED as verified-no-change (35.2% is the WB aggregate). Register: AR-001 and AR-042 applied (CR-01 confirmed;
  ⟦CR-14⟧ → WB wording with 19); ED-034 written to the v5 rule (Option A of the register overtaken by brief v5);
  AR-NEW-001 MERGED with CLOSE-1's D3 change of the same cell (exact-match run against the 2ddbfb61 text + D3).
  Gates: FC-MOE → CO-G03 (+4 controls), RC-1115 first-figure rule refined. Renderer: Home pacing connectives.
- 2026-10-10 · A · W2 · PR #29 merged at `39c31042` (9/9 CI). Closed: the design handoff is superseded (R86-G01
  SUPERSEDED state holds).
- 2026-10-10 · A · W3b · CLOSE-2B run (runner COMMITTED; Master `eaa603586d76` → `7c70b5f766b8`; contract
  installed): CR-05 CLOSED (IMF 2018–2024 = model-based estimates, IRG scope), CR-07 CLOSED (SMP approved by IMF
  Management 7 Oct 2026; new source), CR-08 CLOSED (IMF FSI table described; zeros = not reported; no ratio charted),
  CR-09 CLOSED (three dataset inputs print nothing; records BOUND_EXACT), CR-11 CLOSED (ReliefWeb locator), CR-13
  CLOSED in the Master (labels; publication is U6), CR-15 CLOSED (WB wording beside the AR2025 line), CR-16 CLOSED
  (printed labels), CR-19 CLOSED (provider described, not named), CR-20 CLOSED (Law No. 21 of 2008). Register:
  AR-022, ED-035, ED-036 applied (conditions false). Arabic editor: 9 findings applied. First runs ROLLED_BACK twice
  and fixed: E2-READ label on /finance/ (the July note was its only label), P4-G01 checkpoint source count.
- 2026-10-10 · A · W3b · PR #30 merged at `f71a327d` (9/9 CI; negative controls 139/139). Closed: CR-01, CR-02,
  CR-05, CR-07, CR-08, CR-09, CR-11, CR-13 (Master), CR-14, CR-15, CR-16, CR-19, CR-20; register AR-001, AR-042,
  ED-034, AR-NEW-001, AR-022, ED-035, ED-036.
- 2026-10-10 · A · W3c · CLOSE-3A run (runner COMMITTED; Master `7c70b5f766b8` → `52fb937a4f50`; contract installed):
  U1 CLOSED (147 World Bank values; 51 subgroup rows published; 105 held with checked reasons: 95 no WB value or
  all-adults only, 10 not asked in Yemen's survey; three table-first visuals; open API + public DDI only, dated
  snapshot committed), CR-03 CLOSED (CLM-026 lists 16 published measures). Red-team 18 + 12 findings and Arabic
  editor 9 + 4 applied before the run. Six trial runs ROLLED_BACK and fixed: A|B delimiter, E2-DATES period states,
  E2-PREC false positives (13.87%, 0.56, 22.71 unrelated), RC-B12 range isolation and one-decimal precision, TC-G01
  one "does not establish" text, bilingual digits in CLM-026.
