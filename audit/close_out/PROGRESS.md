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
- 2026-10-10 · A · W3c · PR #34 merged at `69263241` (9/9 CI; negative controls 6/6 shards). Closed: U7, FRN-09.
- 2026-10-10 · A · W3d · CLOSE-4 run (runner COMMITTED; Master `c447171006a8` → `c24791d6fd22`, 545 cells): Appendix C.
  23 sources (199 records, 192 with a public locator); the nine files of cby-ye.com/pages/14 that the 3 October re-run
  listed as not held are held. 12 rules in 31 (REF-REG-001…012); 6 events in 14 (YSC-025…030: Buna, national switch,
  the 2024 bank measures and the agreement the UN Special Envoy's office announced, the Deposit Insurance Institution
  relocation decision, the 2025 enforcement wave as counts, the defaulters registry launch). /data/ s9 is a one-line
  pointer to /finance/#chronology (generator: content.py, families.py). CWR-006 s6 on licence conversion, with the two
  Board decisions it cites bound. Passport EP-CBY-CREDIT-INFO-SPINE-K04 names its locators. Found by the author after
  both reviews: the /data/ regulatory scope line said the evidence base holds no law; the law copy is labelled Law
  (publisher Republic of Yemen), outside the group, and the line says where it is and that the credit-information pages
  cite older instructions. Dates: the brief's 18 December 2023 (e-KYC) and 23 March 2022 (capital reset) are upload
  times in the file names; the instruments print 9 November 2023 and 21 March 2022 (the 2022 decision carries the YER 5
  billion capital minimum). Decision No. 6 of 2025 has letterhead 16/7/2025 and is signed 20 July 2025 (the signature
  date is used). The UN item: the parties' text is Arabic and has no «جميع»; the UN's English is an informal
  translation that adds "all"; neither edition of the event says "all". Reviews: red-team 2 blockers (YSC-027 said the
  other side's decisions were cancelled; CWR-006 named two decisions without their locators), 6 should-fix, 7 nits;
  Arabic editor 5 must-fix, 10 should-fix, 13 nits; second read 0 must-fix, 3 should-fix, 6 nits (+1 scope point).
  Applied, except: the enforcement source keeps its first posting date as its card date (the title gives the range);
  REF-REG-012 keeps a non-ISO date, as the existing "2025 onward" does (31 rows are not rendered on any page); the
  letterhead date is recorded here, not in a locator; Eastern Arabic digits stay in one verbatim internal locator; no
  date state was added for the range start "23 July" (the gates read the range through the event's period).
  FRONTIER (not found on 10 October 2026; W3a cards): Governor's Decisions Nos. 8, 12 and 16 of 2026 (not on the news
  or files pages read); the February 2026 SAR repricing decision (nearest item news/918, the Board meeting of 12
  February 2026); the text of Decision No. 4 of 1991 (cited by publications/149, not published); a July 2024 licence
  revocation (the 2024 bank measure held is Decision No. 20 of 2024); news/709, /722 and /731 (HTTP 500).
- 2026-10-11 · A · W3d · PR #35 merged at `da4ac79f` (9/9 CI; negative controls 6/6 shards). Closed: W3d (Appendix C);
  FRONTIER items as listed in the CLOSE-4 line. CI: the shard timeout went from 20 to 35 minutes after three shards
  caught every fault and were then cancelled at 20 minutes (run 38096726038).
- 2026-10-11 · A · W3e · CLOSE-5 run (runner COMMITTED; Master `c24791d6fd22` → `d14b36c5c171`, 182 cells) and one
  steward edit (D14, RD9): presentation_priority.json measurement_limit 2/1 → 10 on the eight domain routes, its own
  commit. RD10: seven openings reordered (CWR-002, 003, 004, 005, 008, 009) or rewritten by ED-037 (CWR-011); CWR-001,
  006, 007 and 010 already answer first; AR-003, AR-004 and AR-005 kept verbatim. RD2: nine "use" sections. RD1:
  CWR-011 adds Issue No. 55 and end-2025 as an ordering (no new numbers in the text; the table prints them), five
  alternatives (asset quality, no ratio), related to CWR-002 and back, bound to MA-008 and MA-004. RD3: CWR-005 bridge
  (subscribers ≠ active accounts; no active or dormant share). RD4: CWR-008 PAD ¶10 (CLM-062 '141' LOCATOR → READ);
  SMEPS 2025 not published, ESCWA unreachable. RD5: CWR-010 CNL approval date and cash-out plan. RD6, RD7: no change
  (nothing newer; U11 already in CWR-001). RD9: /measurement/ links CWR-001 (MA-001), CWR-002 (MA-008) and CWR-011;
  domain pages list every priority that names them; /methodology/ lists four evidence-method visuals as related
  records; CWR-004 → CWR-007. M1: dimensions on MA-001, 003, 005, 008, 009; MA-008 says the resource holds no current
  measure. M2: /methodology/ s4 gap paragraph (ICT/telecom, insolvency, digital literacy, Yemen Post). Reviews: Arabic
  editor 1 must-fix, 10 should-fix, 13 nits; red-team 2 blockers (CWR-005 dormancy inference; CWR-011 "other
  movements" dropped), 8 should-fix, 6 nits. Applied, except: N2 (the "18 valid responses" count is not held in a
  record), N4 (the page shows the CNL approval date in the source title), and F9 kept CWR-002 → MA-008 (its "what
  remains usable" names more borrowers and wider access, the gap MA-008 measures; owner may revisit).
  RD8 (CWR-012, conditional): DROPPED per its own rule. A draft exists (audit/close_out/drafts/CWR-012_draft.json) with
  every number bound, but the Arabic cannot be reviewed to a native economic editor's standard in this run (and no
  such review is claimed), and the Cash Consortium reports' findings it should use are not held as records. Owner
  question.
- 2026-10-11 · A · W3e · PR #36 merged at `876f52df` (9/9 CI; negative controls 6/6 shards). Closed: RD1, RD2, RD3, RD4,
  RD5, RD6, RD7 (no change needed), RD9, RD10, M1, M2, ED-037; OWN-12 (the measurement limit, D14). RD8 dropped (owner
  question, OWN-13).
- 2026-10-11 · A · W3a + W3f · The open-items register leads with a live view: 247 items, each in one of five states
  (CLOSED 82, HOSTING 9, FRONTIER 47, OWNER-OPTIONAL 8, DECIDED 101); nothing outside HOSTING says PENDING. Every
  FRONTIER item has a W3a verification card (audit/close_out/FRONTIER_CARDS.md: dated attempt, human step, record it
  changes, public state meanwhile, cadence); the twin audit/close_out/OPEN_ITEMS_STATES.json is checked against the
  view by the new gate CO-G06 (two negative controls). New IDs: REL-05…07 (HOSTING), EXT-20…39 (FRONTIER), OWN-11,
  OWN-13 (OWNER-OPTIONAL), OWN-12 and CLOSE-5 (CLOSED). Sections 1–10 are history and are not rewritten; section 11 is
  appended. The Context's two open_items fields point to the live view. Also recorded in card EXT-23: the CBY-Aden POS
  page now links January 2026 to a different file from SRC-CBY-POS-2026-01's locator; no record was changed.
- 2026-10-11 · A · W3a + W3f · PR #37 merged at `53dccc4d` (9/9 CI; negative controls 6/6 shards). Closed: W3a, W3f.

## STAGE A COMPLETE at `53dccc4d` (11 October 2026)

- Merged, each at 9/9 CI: #26 inputs, #27 CLOSE-1, #28 AR-1, #29 W2, #30 CLOSE-2, #31 CLOSE-3A, #32 CLOSE-3B, #33
  CLOSE-3C, #34 CLOSE-3D, #35 CLOSE-4, #36 CLOSE-5, #37 W3f. Master `58b8f3ec5ac1` → `d14b36c5c171`.
- Closed: D1, D3, CR-01…CR-16, CR-18…CR-20, U1–U14, Appendix C (W3d), RD1–RD7, RD9, RD10, M1, M2, OWN-10, OWN-12,
  W2 (handoff superseded), W3a, W3f. Arabic register: 35 rows applied, 0 stopped; RETAIN AR-028, AR-036, ED-038.
- Gates added: CO-G01, CO-G02, CO-G03 (replaces FC-MOE), CO-G04, CO-G05, CO-G06, RC-B12 (canonical pages),
  R86-G01 (SUPERSEDED state); 150 negative controls, all caught.
- Open: CR-17 (edition label, W8 or runbook step 4). RD8 dropped → OWN-13. Owner questions: OWN-11 (CWR-011 on
  /finance/ under F2), OWN-13 (CWR-012), CWR-002 → MA-008 binding. FRONTIER: 47 items with cards
  (audit/close_out/FRONTIER_CARDS.md), incl. EXT-23 (the CBY POS January 2026 file address changed).
- Next: Stage B, after the owner reviews the STAGE A REPORT. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## Stage A addendum (advisor review of the Stage A report, 11 October 2026)

- 2026-10-11 · A+ · item 1 · Public-literal audit v3 (code PR): scope widened to the Measurement Agenda priorities and
  the Reading fields; the inventory/method fallback removed; composite records trace through a listed member or a
  governed data row; 314 public numbers that cannot yet be traced are listed in scripts/literal_audit_open_traces.json
  (70 entries, closes in CLOSE-6A), reported as open, pinned to the Master. "0 unresolved" in the Stage A report is
  re-stated: under the widened scope, 0 unresolved and 314 open. Five negative controls (LIT-3) caught. Source reads for
  items 2–4 (R1–R5) are in scratch and will be committed with the transactions that use them.
- 2026-10-11 · A+ · items 1a/1b/2 + CR-21/CR-22/CLM-039/CCY/e-money · CLOSE-6A (Master d14b36c5 -> 1d468c2c, 457
  cells): ten priorities bound (MA-008 to sources only), three new Evidence Records (FAS-YEM-2015, MICS-YEM-2022-23,
  YMPS-YEM-2022-R1), composite members listed or framing stated, open-trace list emptied: literal closure 0 unresolved,
  0 open. CR-21 month precision everywhere printed (post-condition), CLM-023 keeps both dates; CR-22 sentence; CLM-039
  recorded as inconsistency; e-money history attributed; CWR-010 third finding. Review pair applied (red-team B1–B4,
  S1–S21; Arabic M1–M8, S1–S16, nits). Reads R1, R2, R4, R6 and both reviews committed in audit/close_out/addendum/;
  WDI snapshot in fixtures. Challenges recorded: MA-005 1.48 -> 1.5; Brief 40 not corroboration; "until 2023" right for
  e-money, completed by the 2022 PSP instructions.
- 2026-10-11 · A+ · item 3 · CLOSE-6B (Master 1d468c2c -> 17c6b5dc, 194 cells): two Sana'a Center duplicates retired into
  their canonical records (authors: Sana'a Center Economic Unit); six sources withheld; C12, the University of Aden
  article, the Quarterly Bulletin, AMB and CCY cards completed; ten regulatory cards carry why-it-matters and boundary
  text from 31_REFORMS_REGULATION; /data/ count = cards rendered (38; gate B5 + negative control); chronology 31 events
  (e-KYC 2023 -> MA-007; Decision No. 7 of 2026; YSC-012 paired with CBY-Sana'a Circular No. 12; news/832 = first
  meeting, not establishment); AML grouped event declined (no access channel). SOURCE_UTILISATION_2026-10-11.csv written.
  X-REG-LINK-C12 CLOSED; AR2015 card updated. Review pair applied (REDTEAM_6B, ARABIC_6B). Challenges recorded: KfW
  47229 undated (no date invented; EUR 4.5m is phase III and phase I); AR2015 and CURR-2024 unverifiable, withheld.
- 2026-10-11 · A+ · CLOSE-6A merged: PR #40 at `2b6b2b2c` (9/9 CI after the CR-21 negative-control fix `2f9fec66`).
  CLOSE-6B opened as PR #41 (156/156 negative controls locally).
- 2026-10-11 · A+ · item 4 · CLOSE-6C (Master 17c6b5dc -> 7627f97c, 79 cells): CWR-012 "How money reaches households"
  promoted at /readings/how-money-reaches-households/ with CCY-ISP-2024 and CCY-SAM-2024 (R5 read both studies in
  full). Review pair: red-team HOLD (B1 "informal" transfers through licensed providers, B2 "mainly", B3 "the economy
  as a whole") -> fixed; confirmation pass NB1 (route description "the channel is not measured", false) -> fixed;
  final PROMOTE. Arabic PASS (M1–M6, S1–S13, C-S1–C-S4 applied; 0 numeral drift over 37 pairs). Search alias 001 said
  the base holds no law -> corrected (found while closing CLOSE-6B). Steward D9 commit for the three routes (508 -> 514
  search records). Build 304 HTML, 150 Page Specs, 115 Evidence Records, 12 Readings; literal closure 0 unresolved, 0
  open (18,223). Owner questions 1 (F2) and 3 (CWR-002 -> MA-008) accepted and kept.
- 2026-10-11 · A+ · item 5 · W3f re-run: live view 265 items (CLOSED 92, HOSTING 9, FRONTIER 46, OWNER-OPTIONAL 8,
  DECIDED 110). New: ADD3-1, CR-21, CR-22, ADD3-EMONEY, ADD3-CCY-PRESSURE, ADD3-3, ADD3-4, ADD3-ALIAS-001 (CLOSED);
  ADD3-D1–D9 (DECIDED); ADD3-O1, CCY's own Arabic name (OWNER-OPTIONAL). OWN-13 CLOSED; X-REG-LINK-C12 CLOSED in
  CLOSE-6B. Context open_items updated.
- 2026-10-11 · v5 · PR-3 · CLOSE-6D (Master 7627f97c -> 6769673f, 281 cells): truth corrections 6B-1 to 6B-5. Reads V1–V6
  (audit/close_out/v5_reads/), API fixture wb_api_close6d_2026-10-11.json (named outside CO-G04's findex_api_* glob),
  D16–D18 appended. 6B-1: 24.5% like-for-like beside 35.2%, no economy count, FY24 classification (Yemen classed low
  income; membership not published); 0.4% as printed / 0.6% database; fin29 printed zero against the DDI (393 asked, 39
  yes, unweighted) shown as found; flat "not asked" replaced everywhere but CLM-001's method. 6B-2: YLG two publishers
  (SRC-YLG-AR-2022; 15 rows in 20); SMEPS title; 2018 survey; MA-004. 6B-3: deposit-guarantee law (flat cap; Arts 13, 31,
  33; 2008 ceiling; "the Central Bank" as the law names it); Instructions 589/CBY/2023 of 20 August 2023, Art. 9 items
  ج/د/ذ separately, «14 يومًا» unqualified; MA-006 (no aggregate report on cby-ye.com); Yemen Post (WB FSD p.16). 6B-4:
  CLM-041, CLM-007, 23 caveat, CLM-039 (WDI last 2016). 6B-5: CWR-012 repaired and KEPT (domain lens KEEP after B1–B3;
  Arabic lens KEEP; confirmation pass both KEEP). Gate E2-CTX revised (24.5% required; economy count rejected) with two
  negative controls. Checkpoint 200 -> 201 source records. Challenges: CLM-041 trade sources and 1.838; "includes Yemen
  itself"; "The Instructions are the binding text"; 6B-1(c) Arabic reason; "an account type the survey did not measure";
  POS January 2026 files not value-identical (for PR-5).
- 2026-10-11 · v5 · PR-3 merged: PR #43 at `eac94b9c` (9/9 CI; negative controls 6/6 shards).
- 2026-10-11 · v5 · PR-4 · CLOSE-6E (Master 6769673f -> 7e4f2cb5, 132 cells): 6C-1 to 6C-5; 6C-6 FRONTIER EXT-40 (no
  aggregate file). Steward D9 commit `22bf5c71` for /evidence/IFAD-CPE-YEM-2011-RF/. Five new sources (UNICEF ×2, RPW US,
  Doing Business 2020, IFAD CPE). Review: domain lens B1 (MPCA ≠ UCT), B2 (US rows computed, not published) and S2–S13
  applied, S1 does not reproduce (SAM p.1); confirmation pass ACCEPT after S-1/S-2 (applied); Arabic lens PASS after B1
  («شملها»), B2 (no causal «فـ») (applied); first Arabic run lost to a rate limit, re-run. Challenges: MA-008 binds no
  record and no new route is allowed, so Doing Business sits on YSC-030; SAM prints no date; Pressure has no shop-credit
  statement; "Eid al-Adha 2026" has no year in the source; FATF unreadable (403). run_stage first rolled back on F6-G01
  (social images for the new route are made after it, as in CLOSE-6C), then COMMITTED with that one message allowed;
  images, build, literal audit (19,847, 0 unresolved), inventory and utilisation (206 sources) re-run after.
- 2026-10-11 · v5 · PR-4 merged: PR #44 at `ca8fabd2` (9/9 CI).
- 2026-10-11 · v5 · PR-5 · CLOSE-6F (Master 7e4f2cb5 -> fcc1195b, 129 cells): 7a OECD and POS source notes; 7b eight cards
  checked, no change; 7c D16 relabel (24 + 95 rows; CO-G04 rejects the retired state, new negative control), fin34a label
  and 2022/2014 values as data, 605 and 1,114 UNVERIFIED__DO_NOT_PROJECT, OECD-YEM-003–005 attributed, 012–014 labelled,
  019–023 added; 7d ADD3-4, ADD5-HH (register 267), checkpoint 522 search records, README Stage A row. Review: B1 series URL
  (first run rolled back on CO-G04), S1–S9 and N1/N2/N4/N5/N7 applied; N3 (check 605 and 1,114 against the held PDF) and
  N6 (packet only) not applied. Second run rolled back on CO-G06 (register heading); third COMMITTED. Challenges: "nine"
  cards named, eight listed; CR-11 already closed; EXT-23 "values identical" false; the search count was 522, not 514.
- 2026-10-11 · v5 · PR-6 · CO-G07 (12 entries, G7-01 to G7-12; one negative control) and CLOSE-6G (Master
  fcc1195b -> 87dafc6f, 4 cells). CO-G07 G7-08 found that VIS-REMITTANCE-COST printed the US averages without "computed
  here"; fixed Master-first. Review pair: ACCEPT after two wording fixes (Arabic dual agreement; name the corridor).
  Register 299 items (§9 RESERVED/EXCLUDED, CWR-013, SB-01/SB-02, AR-FINDEX-NAME). Arabic-editor ruling V9.
  Challenge: no state named CAUSEWAY_DERIVED_AGGREGATE exists; mapped to the CauseWay-computed aggregates (US corridor
  means; the overlap bound).

- 2026-10-15 · operational reconciliation · CLOSE-6F merge recorded: PR #45 merged on 13 October 2026 at `612ec146`. The execution entry above is historical and unchanged.
- 2026-10-15 · operational reconciliation · PR #46 merged on 14 October 2026 at `e46ff9eb`: CO-G07/CLOSE-6G and the Stage A addendum report are integrated. Verify on that merged commit passed 9/9 jobs (run `38582364168`); the subsequent Workers build succeeded. DigitalOcean deployment was skipped. The 299-item register remains CLOSED 92, HOSTING 9, FRONTIER 47, OWNER-OPTIONAL 12, DECIDED 139. This records integration, not formal Stage A closure, Stage B authorization, Stage C acceptance or publication approval; those decision rights and dependencies remain unchanged.
