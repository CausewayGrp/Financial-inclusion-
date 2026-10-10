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
- 2026-10-10 · A · W3c · PR #31 merged at `4ce74e68` (9/9 CI; negative controls 6/6 shards). Closed: U1, CR-03.
- 2026-10-10 · A · W3c · CLOSE-3B run (runner COMMITTED; Master `52fb937a4f50` → `d2cd2ad16bd8`; contract installed):
  U2/CR-06 CLOSED (5,202,019 accounts drawn with CLM-010's caveat; 58,512 kept held: no Jan–Feb 2025 release, value
  tile ≠ monthly sum), U6 CLOSED (19_PAYMENTS_DATA: 11 rows newly drawn — 10 in a separate 2024 Q3 panel, never
  compared, plus OBS-00037 — 5 newly published as text (H1-2025 shares in CLM-027 and CWR-007, base undefined, not a
  gap), 25 kept with reasons: bank set changed 3, latest quarter only 7, 2024 POS value unexplained 3, e-money stock or
  flow 3, card types 3, ATM perimeter 5, OBS-00036 1; Q3 page locators corrected PDF k+1 / printed k−2, 151 POS
  terminals checked on the page image), U3 CLOSED (3 CCY reports public; cash-duration finding with its limits: savings
  not comparable, 274 not the sample; last-mile finding from the CNL PAD ¶38/¶47, the programme's own monitoring), U8
  CLOSED (MA-005: FAS 2015 via WDI), U9 CLOSED (PAD locator; FPS design incl. risk mitigation; 141-firm survey; 19
  operating banks with IGC's 2015 19 and 31, four vs 12 MFBs not reconciled; 876 → 3,244 branches vs entities on
  /evidence/compare/; 10 km and access-point case not added, reasons in the docstring), U10 CLOSED (FSD p.15 "99% of
  women", not p.25 "1%"; YMN 34% as printed in the total row; SMEPS 44%; ACAPS hypothesis only), U11 CLOSED (38.6% vs
  "around one quarter", no year; no WB 2024 ~25%), U12 CLOSED (no cycle since Jan 2025; closing 31 Dec 2026; CNL
  signed 2 Sep 2026, designed to pay a different benefit; "successor" not used), U13 CLOSED (MICS: 22 governorates by
  design, 41 EAs not visited, one bank-account item HC19 not tabulated; "cheapest" not claimed), U14 CLOSED (catalogue
  5999 metadata only; no microdata). Register AR-004 APPLIED (condition true: four figures, two measurements; English
  per the register's instruction; text NFC-normalised for R85-G04 — the register orders shadda before tanwin in «أيٌّ»,
  the same text). Red-team: 1 blocker + 11 should-fix applied ("no payment since" → no cycle since January 2025), 1
  kept (four figures: the concordance discusses four). Arabic editor: 3 must-fix + 14 should-fix applied; period-form
  unification left. Gate CO-G05 added (+3 controls). Trial runs fixed: P2-G01 (CLM-002 was lifted above CLM-001 for
  «امتلاك الحساب»; the women's shares moved to CLM-027), P4-G01 (checkpoint 174/167/476), R85-G04 (NFC).
- 2026-10-10 · A · W3c · PR #32 merged at `4bd931d0` (9/9 CI; negative controls 6/6 shards). Closed: U2, U3, U6,
  U8–U14, CR-06; register AR-004 applied. Note: the Master commit `da858d55` carries its trailers as
  `Master-Transaction:` and `Findings-Closed:` instead of CONTRIBUTING's `Transaction:` and `Findings:` (Master-Before
  and Master-After are standard); history is not rewritten, so this line records it.
- 2026-10-10 · A · W3c · CLOSE-3C run (runner COMMITTED; Master `d2cd2ad16bd8` → `fb065fa69583`; contract installed):
  U4 CLOSED (18: ten June 2026 rows from Issue No. 55; guard: the end-2025 and May 2026 values equal Issue No. 55's;
  SRC-CBY-001 → Issue No. 55, Issue No. 54 and the Arabic edition kept as locators, locator note rewritten; on /finance/
  VIS-CBY-MONETARY-SNAPSHOT, 8 indicators × end-2025 / June 2026, and VIS-YER-MARKET-RATE, 114 months; CLM-033 and
  CWR-002 s3 gain the 2025 episode with the December 2025 change of method; VIS-POS-VALUE frame note), U5 CLOSED
  (RV-CWR-011, 4 lines × 3 dates, bound to CWR-011). Departures, each recorded in the docstring: (1) the table's rate row
  shows December 2025 and June 2026 (the brief: "May 2026 and May 2025"), so every row has the same two columns; June
  2025 (2,733.85) is in the line's annotation; (2) "not the street rate" is worded "not any single day's rate": the
  English edition calls the series the parallel-market rate (the Arabic edition does not); (3) the coverage line says
  the bulletin defines banks as those operating in the Republic of Yemen but does not say which report (the brief: "does
  not state its territorial coverage"; the bulletin's definitions, printed p.20, say more than that); (4) /finance/ is
  not added to CWR-011's domain surfaces: rule F2 caps an answer page at two Readings and /finance/ carries CWR-002 and
  CWR-006 — owner question; (5) both /finance/ visuals sit in the page's Views (the 114-row table of the rate line would
  otherwise add about six phone screens to the first load). Red-team: 1 blocker applied (the Disclaimer, printed p.23:
  data amended to the IMF MFSM 2016 from December 2025, so valuation, method and other movements cannot be separated),
  4 should-fix and 7 nits applied; 37/37 numbers and all 114 months match Issue No. 55. Arabic editor: 2 must-fix
  («مراكز» not «مواقع»; "parallel market" is in the English edition only) and 9 should-fix applied; second read of the
  rewritten strings: 1 must-fix (the decision value said the bulletin names no rate at all) and 3 should-fix applied. Gate RC-B12 extended to canonical pages (+1 control); renderer: long monthly axes.
- 2026-10-10 · A · W3c · CLOSE-3C-L run (runner COMMITTED; Master `fb065fa69583` → `49de81b3bc53`, 3 cells): the gate
  run after CLOSE-3C showed VIS-YER-MARKET-RATE as the only SOURCE_NOT_YET_BOUND visual and VIS-CBY-MONETARY-SNAPSHOT
  as a composite with no listed members (their data_inputs named the sheet, not records). The three new visuals now
  name CBY-BANKS-2026-05 and CLM-033 (both closed to SRC-CBY-001); lineage: COMPOSITE_OF_OBJECTS 2 → 4,
  SOURCE_NOT_YET_BOUND back to 0. A corrective transaction, not a re-run: the working-tree reset was refused, and the
  audit trail stays append-only.
- 2026-10-10 · A · W3c · PR #33 merged at `cf37e210` (9/9 CI; negative controls 6/6 shards). Closed: U4, U5.
  Owner question recorded: /finance/ is not on CWR-011's domain surfaces (rule F2 caps an answer page at two Readings).
- 2026-10-10 · A · W3c · CLOSE-3D run (runner COMMITTED; Master `49de81b3bc53` → `c447171006a8`, 180 cells; contract
  installed): U7 CLOSED (VIS-REMITTANCE-COST second panel: WDI SI.RMT.COST.IB.ZS for Yemen, 4.68 / 5.71 / 3.46 / 2.81 for
  2016 / 2017 / 2022 / 2023, rounded half up from the API's 4.68109…, 5.70931…, 3.455, 2.805 with decimal 2; dated
  snapshot audit/close_out/fixtures/wdi_rmt_cost_2026-10-10.json, lastupdated 2026-10-08; price-of-sending and
  simple-average notes; RPW stays 2025 Q3: corridor pages refused, the data catalogue ends at 2025 Q3), FRN-09 CLOSED
  (SDG 10.c as a reference line in words: the 3% applies to the global average and the 5% to each corridor's SmaRT
  average of the three cheapest qualifying services, neither shown; no pass/fail colouring). Red-team: 2 blockers
  (the SmaRT definition of the 5% component; the method's wording of it), 7 should-fix and 7 nits applied, one kept
  (the 26 September 2026 date state stays: other pages print that date). Arabic editor: 2 must-fix (TERM-021, «لا يعني
  صفرًا») and 9 should-fix applied; second read 3 should-fix applied. Renderer: remittance_cost draws each series as a
  headed panel on one axis (one series unchanged).
