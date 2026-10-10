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
