# A5 - Open-items register: true status at main 2ddbfb61 (read-only inventory, no web access)

Evidence key: REG = FINAL_OPEN_ITEMS_REGISTER.md (line numbers), B16 = REG lines 359-481 (B16 disposition of 3 Oct),
CL = docs/CHANGELOG.md, OD = audit/OWNER_DECISIONS_2026-10-0x.md, HO = docs/HANDOVER_TO_DEVELOPER.md.
States: CLOSED / HOSTING / FRONTIER / OWNER-OPTIONAL / DECIDED / WORK (= needs W1-W3 work). "?" = unclear.

## 1. Table of every ID (core register, REG sections 1-6, 8, 10)
| ID | Sect | Text status (REG) | True status + evidence | Proposed | Note |
|---|---|---|---|---|---|
| EAD-01 | 1 | CLOSED 2026-09-29 | closed; REG:36, erratum REG:331+ (suite count 27/28 not 25/26, REG:48) | CLOSED | |
| EAD-02 | 1 | Code half done, auditor half not | B16 REG:361 NEXT EDITION; CL 10 Oct re-run: 288 pages, 0 axe violations; no screen-reader pass | OWNER-OPTIONAL | brief W3f: manual AT audit, never claimed |
| EAD-03 | 1 | BLOCKED ON OWNER APPROVAL | DONE: owner approved (OD-10-02 row EAD-03), 8 derivatives, REG:52,69-72 | CLOSED | stale row; cold page 10.3 MB -> 0.30-0.69 MB |
| EAD-04 | 1 | CLOSED 2026-09-29 | REG:39 | CLOSED | |
| EAD-05 | 1 | CLOSED 2026-09-29 | REG:40 | CLOSED | |
| EAD-06 | 1 | THREE OF FOUR DONE | DONE: facet+N-of-M shipped G4 (7895694), RC-3 labels d668f11, REG:362 | CLOSED | residual domain facet = X-ESC-ANT-01 (post-launch, needs governed field) -> DECIDED |
| EAD-07 | 1 | BLOCKED ON CONTROLLED CONTENT | DONE: label RC-4 ae0f3db, filter RC-12 98f43f5, REG:363 | CLOSED | stale row; the 9 untyped sources remain = EXT-09 |
| EAD-08 | 1 | self-hosted; subsetting open | REG:364 NEXT EDITION, optional, owner decides | OWNER-OPTIONAL | |
| EAD-09 | 1 | CLOSED 2026-09-29 | REG:44 | CLOSED | |
| EAD-10 | 1 | HALF DONE | local budget set 8c977f3; live-host remeasure = runbook step 10, REG:365 | HOSTING | |
| EAD-11 | 1 | Narrowed | DONE: question_sets in presentation_priority.json (G3), REG:73-78 | CLOSED | stale row |
| EAD-12 | 1 (appended) | post-launch | method text DONE (B1 d9df1d2, PB-0401); table rows for 13 records post-launch by owner A4/C6, REG:79-84,366 | WORK? | table rows need Master rows; fits W3c UNLOCK or DECIDED-with-reason. UNCLEAR |
| REL-01 | 2 | open | prepared (_headers, 1ca46dc); live-host headers at release, REG:367 | HOSTING | |
| REL-02 | 2 | NOT_ASSESSED on all 160 | count is 167 (REG:492, CL 10 Oct); B16 NEXT EDITION REG:368 | FRONTIER | |
| REL-03 | 2 | open | optional, REG:369 | OWNER-OPTIONAL | |
| REL-04 | 2 | open | owner, runbook step 13, REG:370 | HOSTING | |
| EXT-01 | 3 | open (stale cell) | CLOSED 3 Oct, RC-7 Path A, REG:133-138 | CLOSED | |
| EXT-02 | 3 | open | CLOSED 3 Oct RC-8, date 2026-06-08, REG:143-145 | CLOSED | |
| EXT-03 | 3 | open | CLOSED 3 Oct RC-8, names held non-public, REG:146-150 | CLOSED | |
| EXT-04 | 3 | open | narrowed 3 Oct (names dropped); B16 NEXT EDITION = ADD2-IMP-6, REG:151,371 | WORK? | needs governed AR event text + contract; UNCLEAR (W3d could do) |
| EXT-05 | 3 | open | not read (OECD CDN blocks), REG:372 | FRONTIER | browser card, see s2 |
| EXT-06 | 3 | open | smed.sfd-yemen.org 503, NOT READ, REG:373 | FRONTIER | |
| EXT-07 | 3 | open | needs microdata; roadmap v1.1, REG:374 | OWNER-OPTIONAL | OWN-09 unlocks the 105 subgroup rows per brief W3f |
| EXT-08 | 3 | open | CLM-039/046/056 partial lineage unchanged, REG:375 | WORK | W3c UNLOCK/bind, else FRONTIER |
| EXT-09 | 3 | open | 9 cards "Document type not recorded", REG:376 | WORK | W3a read each, else FRONTIER |
| EXT-10 | 3 | open | inputs named in B12 (IBS2020 T3/T8, SMEPS AR2024 pp8-9), REG:377 | WORK | W3c; origin tables 198/219 not Master sheets |
| EXT-11 | 3 | open | no trigger recorded, REG:378 | FRONTIER | |
| EXT-12 | 10 | RPW 2025 Q3 | re-read at release; brief W3a lists RPW latest quarter, REG:499 | WORK | W3a (WebFetch/Playwright); else FRONTIER |
| EXT-13 | 10 | IMF FAS stops 2015 | IMF refuses bots, REG:500 | FRONTIER | |
| EXT-14 | 10 | ESPECRP unit | read ISR, REG:501 | WORK | W3a (ISR 30 Jun 2026 / P514855) |
| EXT-15 | 10 | CBY "subscriber" undefined | external, REG:502 | FRONTIER | |
| EXT-16 | 10 | PAD "two percent" vintage | external, REG:503 | FRONTIER | |
| EXT-17 | 10 | CCY originals, no locator | owner; 6 SRC-CCY-* USER_PROVIDED_FILE | FRONTIER | owner could supply public originals |
| EXT-18 | 10 | 26-bank list undated | external, REG:505 | FRONTIER | |
| EXT-19 | 10 | Bulletin Issue 54 vs 55 | W3a names Issues 55 and 56, REG:506 | WORK | roll forward if verified |
| FRN-01..08 | 4 | frontier | B16 NEXT EDITION "closes only with new evidence", REG:390-397; FRN-07 now 8 records not 9 (a95c7ef) | FRONTIER x8 | |
| FRN-09 | 10 | SDG 10.c | owner next-edition decision, REG:507 | FRONTIER | could be OWNER-OPTIONAL; UNCLEAR |
| OWN-01 | 5 | open | DONE: OD-10-02, RC-2, REG:237 | CLOSED | stale |
| OWN-02 | 5 | open | DONE: monitored, REG:240,398 | CLOSED | stale |
| OWN-03 | 5 | open | decided "when hosting ready"; public_origin null, REG:241,399 | HOSTING | |
| OWN-04 | 5 | open | CLOSED 10 Oct (OD-10 s1, OWN-04-R); owner confirmed text, no counsel, REG:100-104,250 | CLOSED | REG:253 still says counsel pending: superseded by REG:100 and OD-10 s4 OWN-RF-04. Code licence undecided |
| OWN-05 | 5 | open | DONE OD-10-02, REG:244,401 | CLOSED | DPG gaps not addressed |
| OWN-06 | 5 | open | REG:402 NEXT EDITION; no reversed logo needed | DECIDED | |
| OWN-07 | 8 | closed 27 Sep | REG:322 | CLOSED | |
| OWN-08 | 8 | closed 27 Sep | REG:323 | CLOSED | |
| OWN-09 | 5 (appended) | optional | World Bank written confirmation, REG:257 | OWNER-OPTIONAL | |
| OWN-10 | 10 | stale Master counts | 143/10/165 vs 144/11/167, REG:508; HO s8 | WORK | W1 (make computed/gated) |
| REJ-01..07 | 6 | rejected | REG:265-271 | DECIDED x7 | |

## 1b. Appended B16 / addendum IDs (REG:359-481), not in section tables
- RELEASE/HOSTING: X-REG-LINK-C12 (unresolved, no archive), X-REG-LINK-AR2015 (503), X-REG-LINK-CDN14 (14 CDN-refused locators), X-LINK-TLS-SIGNIN (OEB-FX TLS; LIQ-2016 sign-in), X-REG-HAND3 (IMF SMP, RPW after Q3, CBY Sana'a host; rerun script), X-REG-FIRSTSCREEN22 (22 values; UNDP July 2025 dates vs WB 1 Sep 2025 = possible conflict). Proposed: browser items -> FRONTIER cards (W3a); currentness rerun -> HOSTING. X-REG-FIRSTSCREEN22 and X-REG-HAND3 UNCLEAR (W3a may close some).
- DONE: X-REG-FMIIP-ISR0, X-REG-SEVERITY-BASE (RC-16 b49fe93) -> CLOSED.
- NEXT EDITION, no input: X-REG-SFD62 (decide caveat; could be DECIDED), X-REG-ORIGIN-TABLES (WORK, W3c/e), X-REG-REGDOCS9 (9 CBY regulatory docs; W3d WORK), 24 x X-B12-* (text-only contracts, each names a missing Master input; 2 drawings + 22 visuals): WORK under W3c UNLOCK, else DECIDED with reason.
- ADD2-REJ-01..14, B15-BLOCK-01..06, ADD2-IMP-2c: REJECTED -> DECIDED (21).
- ADD2-IMP DONE -> CLOSED: A1, A2, 1a, 1b, 1c, 1d, 1e, 2b, 2d, 2e, 3a, 5a, 5b, 9a, 9c, 9d, 9i, 10, 11, L1, L2, L3, L4, J2 (24).
- ADD2-IMP NEXT EDITION: 2a, 3b, 4a, 4b, 4c, 6 (=EXT-04), 7, 8, 9b, 9e, 9f, 9g, 9h, L5, J1 (15) -> WORK (W4 design/W3e) or DECIDED with reason; each is one-line decidable.
- Pointers: A3/C3 double boundary (implemented), D7 acceptance (done), 2026-10-03 dated notes (SFD62, REGDOCS9, origin tables) map to X- rows above.

## 2. EXT-* and "sources that need a browser": human/recheck cards
Locators from site-src/content/sources/source_library.json; blocks from audit/release_candidate/LINK_CHECK.md; HO s3/s4 (4 Oct, not retried).
| Item | URL(s) | Read | Record it changes |
|---|---|---|---|
| EXT-05 | https://doi.org/10.1787/81ed2898-en (SRC-OECD-YEM-RESILIENCE-001, CDN 403) | product-holding and mobile-access figures in the review's own tables | new bound records on /finance/, Master-first; today "not verified, not shown" |
| EXT-06 | smed.sfd-yemen.org (503; no URL in library, LINK_CHECK s3) | 2023 SFD/SMED portfolio doc: 78,686 active borrowers | CLM-053, CLM-054, CLM-057 (RC-14 matched Sana'a Center paper only) |
| EXT-12 | https://remittanceprices.worldbank.org/corridor/Saudi%20Arabia/Yemen ; .../United%20Arab%20Emirates/Yemen ; dataset https://datacatalogfiles.worldbank.org/ddh-published/0037898/DR0095523/rpw_dataset_2011_2025_q3.xlsx | latest quarter and corridor costs (4 values) | SRC-WB-RPW-SA/UAE-YEM-2025Q3-001; VIS-REMITTANCE-COST; UI-CONTENT-VERSION |
| EXT-13 | IMF FAS data portal (no URL recorded; data.imf.org refuses bots) | any Yemen series after 2015 | none published; context only (audit/R8_2_*) |
| EXT-14 | ESPECRP ISR (no URL recorded; World Bank P-number) | unit of reach: households vs individuals | gate for any ESPECRP reach figure (docs/S06_3_*) |
| EXT-15/16/18 | none (external publisher) | CBY-Aden "subscriber" definition; PAD para 9 source; dated 26-bank list | /payments/, /reforms/, CWR-007, bank list |
| EXT-17 | none: SRC-CCY-* are USER_PROVIDED_FILE (REMIT-ESTIMATE-2025, SAM-2024, CASH-DURATION-2026, ISP-2024, AMAL-2025, PRESSURE-2026) | owner supplies public originals or confirms none | non-public source records -> public locators |
| EXT-19 | CBY-Aden Monetary and Financial Developments, Issue 55 (June 2026) and 56; cby-ye.com (Arabic site if EN lags) | whether Issue 54 is still latest | CBY-BANKS-2026-05, CWR-011 |
| EXT-09 | the 9 untyped locator-only source cards (list: /en/data/ "Document type not recorded") | title, publisher, doc type | source_library metadata, Master-first |
| HO browser 1 SDRPY | https://spa.gov.sa/en/N2234277 | deposit amount, date, recipient; keep $300m deposit in CBY / $200m budget support / $1.2bn pledge apart; SPA N2525739 (1 Mar 2026, SAR 1.3bn) is Ministry of Finance | additive: chronology/finance deposit record |
| HO 2 CBY Sana'a Circular 14/2024 | UN doc S/2024/731 p114 Fig 28.2; never cbyemen.com | own locator if one exists | circular's source record |
| HO 3 OECD Youth DFI | https://www.oecd.org/en/publications/advancing-the-digital-financial-inclusion-of-youth_21b829d8-en.html | printed publication date | SRC-OECD-YOUTH-DFI-2020-001 |
| HO 4 WB FASTT | https://fastpayments.worldbank.org/sites/default/files/2021-11/Fast%20Payment%20Flagship_Final_Nov%201.pdf ; /resources | confirm document (not "Implementation Considerations for FPS") | SRC-WB-FASTT-FPS-2021-001 |
| HO 5 UNDP FMIIP | https://www.undp.org/yemen/projects/yemen-financial-market-infrastructure-and-inclusion-project ; AR https://www.undp.org/ar/yemen/projects/mshrw-albnyt-althtyt-llaswaq-walshmwl-almaly-fy-alymn-fmiip | component start dates (July 2025 vs WB ISR 1 Sep 2025) | SRC-UNDP-FMIIP-001; FMIIP dates (X-REG-FIRSTSCREEN22) |
| HO 6 CBY-Aden Bulletin June 2021 | CBY index points to CDN with TLS mismatch | ask CBY-Aden or cite another issue | bulletin source record |
| HO 7 IMF SMP | https://www.imf.org/en/news/articles/2026/07/16/pr26249-yemen-imf-reaches-sla-on-new-staff-monitored-program | confirm 16 Jul 2026 event; also SMP approval ~7 Oct 2026 | SRC-IMF-YEM-SMP-2026; /finance/ chronology; CR-07 |
| LINK_CHECK others | IMF: https://www.imf.org/-/media/files/publications/cr/2026/english/1yemea2026001-source-pdf.pdf (AIV 2025-26), .../d4d-fund-implementation-progress-fy26-midyear-january-2026.pdf; MDPI https://www.mdpi.com/2227-7099/10/10/259; ResearchGate (SRC-LIT-XIDIAN, now NON_PUBLIC); OEB-FX https://asjp.cerist.dz/en/article/273259 (TLS); LIQ-2016 https://search.mandumah.com/Record/932295 (sign-in); AR2015 http://centralbank.gov.ye/App_Upload/Ann_rep2015AR.pdf (503); C12 yemeneco.org/archives/77824 (dead; no archive) | locator opens | 14 CDN-refused sources + 2 + 2 |
| First-screen 22 | IMF CR 26/80 Table 4 and supplement Table 2 (13 values), RPW 4, FMIIP UNDP 4, SFD 93,118 | values | ORIGINAL_SOURCE_VERIFICATION.md s8 |
EXT-01..03 have URLs only as history (eLibrary https://www.elibrary.imf.org/view/journals/002/2026/080/article-A001-en.xml; CBY scan https://www.cby-ye.com/files/6a27bc7883b9c.pdf).

## 3. Duplicates and conflicts
- Class table (REG:22-30) counts are F9-era (11/4/11/8/6/7); true live counts differ (see s4). EXT-12..19, FRN-09, OWN-09, OWN-10, EAD-12 sit outside the class table.
- EXT-04 = ADD2-IMP-6 = EAD-12 family (13 table-only records) = ADD2-IMP-3b: one governed-contract problem tracked four times.
- EXT-10 = X-B12-RV-CWR-005 / -008 / VIS-MFI-DIVERGENCE / -006; X-REG-ORIGIN-TABLES is the same work.
- EXT-09 = EAD-07 residual (9 untyped sources). X-REG-LINK-CDN14 and X-REG-FIRSTSCREEN22 and HO s3/s4 overlap with EXT-05, EXT-12, EXT-13.
- EXT-12/19 duplicate W3a targets and the release-time currentness rerun (X-REG-HAND3).
- OWN-04 conflict: REG:253 ("counsel confirms ... still") is superseded by REG:100-104 and OD-10 s4 (owner confirms; licence_text_confirmed true). OD-10 s1 OWN-04-R-b says confirmation unchanged; same-day s4 reverses it. Use s4.
- OD-09 "Rights: Not decided" superseded by OD-10 s1 (cross-ref already appended).
- REL-02 cell says 160; true 167. FRN-07 says 9; dist shows 8. EAD-01 suite count 25/26 vs 27/28.
- HO s8 says RIGHTS-FINAL is #24 and #23 closed; REG:359+ B16 block is dated 3 Oct and predates RC-17 and Oct 10 closures: B16 lines for OWN-04 and REL-02 pre-date the owner confirmation.
- HO has two handovers (new top s1-9, 4-9 Oct kept below); browser list s4 (7 rows incl. IMF SMP) vs s3 (6 rows) differ by the IMF SMP row.

## 4. Counts by proposed state (core + appended; IDs counted once)
Core register (EAD 12, REL 4, EXT 19, FRN 9, OWN 10, REJ 7 = 61):
- CLOSED 19: EAD-01,03,04,05,06,07,09,11; EXT-01,02,03; OWN-01,02,04,05,07,08; (EAD-12 method text partial, not counted)
- HOSTING 5: EAD-10, REL-01, REL-04, OWN-03 (+ phone check/deploy switch/D5 counts, not in register)
- FRONTIER 21: FRN-01..09, REL-02, EXT-05,06,11,13,15,16,17,18 (EXT-05/06 are browser/primary reads)
- OWNER-OPTIONAL 6: EAD-02, EAD-08, REL-03, EXT-07, OWN-09 (+FRN-09 if chosen)
- DECIDED 8: OWN-06, REJ-01..07
- WORK 8: EXT-04, 08, 09, 10, 12, 14, 19, OWN-10 (EAD-12 table rows unclear)
Appended B16 set (~75 IDs): CLOSED 26, DECIDED ~21, WORK ~39 (24 X-B12 + 15 ADD2-IMP + REGDOCS9, ORIGIN-TABLES), HOSTING/FRONTIER ~7 (X-REG-LINK/CDN/TLS/HAND3/FIRSTSCREEN22).

## 5. Unclear proposed state
EAD-12 (table rows), EXT-04 (WORK vs DECIDED post-launch), EXT-08, EXT-09, EXT-10 (WORK only if W3c unlocks, else FRONTIER), EXT-12/14/19 (WORK only if W3a can read; else FRONTIER), EXT-17 (owner supplies vs FRONTIER), FRN-09 (FRONTIER vs OWNER-OPTIONAL), X-REG-SFD62 (DECIDED "no caveat" vs WORK), X-REG-HAND3, X-REG-FIRSTSCREEN22, X-B12-* (24) and ADD2-IMP NEXT EDITION (15): need per-item WORK/DECIDED call. Exact URLs for EXT-06, EXT-13, EXT-14 and CBY Bulletin June 2021 are not recorded in the register; find via source_library.json or the B12 files.
