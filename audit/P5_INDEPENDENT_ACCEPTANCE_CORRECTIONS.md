# P5 — Independent acceptance corrections (closure)

**Programme:** Pre-Tranche-C. **Window:** P5, a narrow correction window after the independent recipient review of P1–P4.
**Date:** 2026-09-26. **Decision authority:** Team Lead.

**Status: PRE-TRANCHE-C ACCEPTED — READY FOR TRANCHE C.**

Scope and boundaries:
- The independent review accepted P1–P4 with three narrow corrections: P5.1, P5.2 and P5.3. All three are closed, as
  set out below.
- P1–P4 were not reopened. No editorial, search, IA, visual-tier or source-lineage work was redone. No unrelated copy was
  changed.
- Tranche C has not been started. This is not DESIGN HANDOFF READY and not PUBLIC RELEASE READY.

## 0. Explicit statements

| Required statement | Result |
|---|---|
| Literal audit deterministic across tested hash seeds | **Yes.** The audit was run under `PYTHONHASHSEED` 0, 1, 2, 3, 7, 42, 1234 and 99991. All eight runs produce byte-identical `audit/PUBLIC_LITERAL_CLOSURE.json`, with SHA-256 `320c3f01c8dd33ba8dab0b3a00fc13590043c9befbe26dcccaf6a87dfdf9f283`, identical record order and identical `source_object` attribution. They also equal the committed file. |
| REF-PAY-001 status | **Closed to a source record.** `SRC-CBY-DEC-23-2024-001` is CBY Governor's Decision No. 23 of 2024 (26 June 2024). VIS-PAYMENT-RAILS is `CLOSED_TO_SOURCE_ID` as both record and visual. RV-CWR-009's credit line resolves and its release blocker is removed. |
| RV-CWR-001 panel-2 status | **READY.** The CBY AR2025 vintage 2021–2024 and the IMF 2025 Article IV staff path 2021–2024 are each indexed to their own 2021 value (2021 = 100) and drawn as two separately labelled lanes. `BLOCKED_ON_DATA` is removed. |
| Remaining release blockers | **None.** The source-lineage truth test asserts that no data contract carries a blocker (`OPEN_RELEASE_BLOCKERS = {}`), and acceptance item 11 reads `release blockers: {}`. |

## 1. Authority state

| Point | Production Master SHA-256 | Page Specs SHA-256 |
|---|---|---|
| P4 hand-back (entry to P5) | `5f3d9404e93bf48528d487a86a653601166b715026f1884d343da367144b463a` | `a78ca8b3b8535675724e7b62c8d6a4bc95bd586639128c95f98a74af57b28670` |
| After P5-A (Master transaction; committed) | `397b330757de7b1dd720cca49c2609ff5bdbb0f944e09857b701de25b1682d9c` | `3b1065492d7c84a90821f3d390804aff74976720acd70fb36599e7731736e510` |
| After P5-B (code and document state; Master unchanged; committed) | `397b330757de7b1dd720cca49c2609ff5bdbb0f944e09857b701de25b1682d9c` | `3b1065492d7c84a90821f3d390804aff74976720acd70fb36599e7731736e510` |

How the two transactions ran:
- Both went through `audit/tranche_b_execution/run_stage.py`. That script snapshots, regenerates, rebinds, builds, runs
  the literal audit, the diagrams, the validator and generator `--check`, and rolls back on any failure.
- Records are in `audit/pre_tranche_c/runs/`: `P5A_MASTER_LEDGER.json`, `P5A_RUN_REPORT.json` and
  `P5B_RUN_REPORT.json`.
- The Master transaction script is `audit/pre_tranche_c/p5a_execute.py`.

Inventory after P5 (from `site-src/content/content/public_inventory.json`):
- **Grew, all from the one new source record:**
  - source records 159 → 160;
  - public original locators 150 → 151;
  - curated resource cards 26 → 27;
  - public search records 423 → 424.
- **Unchanged:**
  - Evidence Records 110;
  - public claims 60;
  - Evidence Passports 55;
  - Page Specs 143;
  - visual contracts 36;
  - chronology events 24.

## 2. P5.1 — Public-literal audit made deterministic

**Reproduction before the fix.**
- Before the fix, seeds 0–5 produced three different file hashes.
- The flip was the one the reviewer reported. The literal 78,686 on `/readings/microfinance-structural-divergence/` was
  attributed to CLM-054 under some seeds and to CLM-057 under others.

**Root cause.**
- `reading_objects()` collected the IDs a Reading binds into `ids = set(...)` and then iterated that set.
- The classifier records the first bound record whose governed text carries the literal. So attribution followed the
  set's hash order, not the Master.

**Canonical rule (declared in `reading_binding_order()`):**
1. Governed binding order is kept: the Reading's `claim_bindings` (08), then its `evidence_bindings` (08), then the
   verification-path claim IDs.
2. De-duplication is ordered: each ID is kept at its first occurrence, and no unordered set is used.
3. A stable-ID tie-break would apply only if a tie remained. None can: every binding list is an ordered list in the
   Master, so the fallback is never reached and is not implemented as a silent sort.

With this rule, 78,686 is attributed to CLM-054, the first bound claim carrying it, under every seed.

**Scan of the rest of the script.** Every set or dict iteration was checked:

| Place | Kind | Effect on emitted identity or order |
|---|---|---|
| `CLOSURE_BY_ID` values (sets of closure states) | membership (`in`, `&` then truth test) | none |
| `bound_objects()` | insertion-ordered dict built from ordered Page Spec lists | order follows the Page Spec |
| `reading_objects()` | now an insertion-ordered dict built from the ordered binding list | order follows the Master |
| `inv` (inventory values per field) | membership only | none |
| `seen` (record de-duplication) | membership only; `ded` is a list in record order | none |
| `summary` | insertion-ordered dict filled in record order | order follows records |

The script header now states this rule.

**Regression test.** `scripts/tests/test_literal_audit_determinism.py` runs the audit in fresh processes under eight
`PYTHONHASHSEED` values, each writing to a temporary file through the new `--out` option. It requires:
- identical bytes, and therefore an identical SHA-256;
- identical record order, by (route, surface, field, token, context);
- identical `source_object` attribution;
- equality with the committed `audit/PUBLIC_LITERAL_CLOSURE.json`.

It exits 1 on any difference. The acceptance matrix runs it for items 16 and 17.

**Result.** All eight seeds give SHA-256 `320c3f01c8dd33ba8dab0b3a00fc13590043c9befbe26dcccaf6a87dfdf9f283`, with 8,285
records and 0 unresolved.

## 3. P5.2 — REF-PAY-001 closed from the primary CBY instrument

Process: SOURCE → VERIFY → ADJUDICATE → MASTER FIRST.

**SOURCE.** REF-PAY-001 already carried the governed locator `https://cby-ye.com/files/667c596ef3bea.pdf`, but no source
record held that locator.

**VERIFY (in this environment).**
- **The announcement page.** The CBY's own announcement, `https://cby-ye.com/news/706` (published 2024-06-26), was read
  twice. It gives:
  - the title «محافظ البنك المركزي يصدر قراراً بشأن مزاولة نشاط التحويلات المالية الداخلية (وثيقة)»;
  - Decision No. 23 of 2024;
  - the operative requirement: all exchange companies and establishments and money-transfer agents must execute every
    new domestic transfer made in cash exclusively through the Unified Money Transfer Network (UNMONEY);
  - the transition: until 30 July 2024, with bank-owned networks not required to comply immediately;
  - the exclusion of licensed e-wallets and payment service providers within prescribed ceilings;
  - a direct link to the governed PDF.
- **The PDF itself.** It is reachable, but it is a scanned image: its text could not be machine-read here. A direct
  download from the shell was refused by the network allowlist and was not attempted by another route.
- **The reference number.** 343/CBY/2024 does not appear on the announcement page. It is recorded as read from the
  instrument by the independent recipient review.

**ADJUDICATE.**
- The identity of the instrument is confirmed from the issuing authority's own page: number, date, title and subject.
  The page links the exact governed locator.
- The evidence role is limited to the rule stage. The instrument requires; it does not show that the requirement was
  implemented, how many transfers moved to the network, or any effect on users.
- Reuse rights have not been assessed, and none are implied.

**MASTER FIRST: 15_SOURCE_LIBRARY, new row `SRC-CBY-DEC-23-2024-001`.**

| Field | Value |
|---|---|
| Issuer | Governor, Central Bank of Yemen — Aden |
| Publisher | Central Bank of Yemen — Aden |
| Title (EN) | Central Bank of Yemen — Governor's Decision No. 23 of 2024 on domestic money-transfer activity (26 June 2024; ref. 343/CBY/2024) |
| Title (AR) | البنك المركزي اليمني — قرار المحافظ رقم (23) لسنة 2024 بشأن مزاولة نشاط التحويلات المالية الداخلية (26 يونيو 2024؛ المرجع 343/CBY/2024) |
| Date; reference | 26 June 2024; 343/CBY/2024 (see the verification note above) |
| Public original locator | `https://cby-ye.com/files/667c596ef3bea.pdf`; additional: `https://cby-ye.com/news/706` |
| Document type | regulatory decision |
| Evidence role | primary regulatory instrument (rule stage only; not implementation, use or outcome) |
| Rights state | `NOT_ASSESSED` (no licence or attribution requirement recorded; no reuse permission implied) |
| Retrieval date | 2026-09-26 |
| Public card | `FULL_PUBLIC_CARD`, with why-it-matters and does-not-establish in English and Arabic ("A regulatory requirement does not establish that it was implemented, how many transfers moved to the network, or any effect on users or on financial inclusion." / «لا يثبت الإلزام التنظيمي أنه نُفذ فعليًا، ولا عدد الحوالات التي انتقلت إلى الشبكة، ولا أي أثر على المستخدمين أو على الشمول المالي.») |
| Datasets | DS-REFORM-EVENTS, DS-PRIMARY-AUTHORITY |

**Bindings.**
- **06 VIS-PAYMENT-RAILS.**
  - `source_dependencies`: `UNBOUND:REF-PAY-001` → `SRC-CBY-DEC-23-2024-001`.
  - `lineage_state`: `BOUND_PARTIAL` → `BOUND_EXACT`.
  - Verification text: the governed `UI-VERIFY-BOUND` template in both languages.
- **REF-PAY-001.** The event row already carries the locator. The generator resolves it to the new record, so RV-CWR-009's
  credit reads "Central Bank of Yemen — Aden; United Nations Development Programme (UNDP)".
- **Other dependents.** No other governed object depended on the unbound token.

**Closure recalculated.**
- VIS-PAYMENT-RAILS is `CLOSED_TO_SOURCE_ID` as both `evidence_object` and `visual`.
- Evidence-Record lineage is now BOUND_EXACT 93, COMPOSITE_OF_OBJECTS 13, FRAMING_NO_FACT 1 and BOUND_PARTIAL 3.
- The objects still partial are CLM-039, CLM-046, CLM-056 and RV-CWR-006. None of them is a P5 item, and each shows its
  partial state.
- The RV-CWR-009 blocker is removed.

**Public result.** The source card appears on `/en|ar/evidence/VIS-PAYMENT-RAILS/` and in the `/data/` source library,
with the does-not-establish line.

**Semantic firewall.** Regulatory requirement ≠ demonstrated implementation ≠ observed use or outcome. The card, the
evidence role and the rail's own prohibited inference all say so.

## 4. P5.3 — RV-CWR-001 panel 2 unblocked from CBY Annual Report 2025

**VERIFY (in this environment).**
- The governed locator of `SRC-CBY-AR2025-BOP`, `https://english.cby-ye.com/files/6a54b8fcd8b68.pdf`, was read four
  times through text extraction.
- The first pass pointed to Table 4-1, which holds only the 2024 and 2025 columns. The multi-year table is on page 52,
  "Balance of Payments (USD million)", with columns "Items 2021 2022 2023 2024 2025".
- Its row reads verbatim: "Remittances 2,900.22 3,066.58 3,240.46 3,422.16 3,614.05".
- This matches the independent review. The table is not a visual page-image review.

**MASTER FIRST: 23_REMITTANCES, three new rows.**
- The rows are RMO-CBY-2021-AR2025 = 2,900.22, RMO-CBY-2022-AR2025 = 3,066.58 and RMO-CBY-2023-AR2025 = 3,240.46.
- They carry the same identity as the governed RMO-CBY-2024-AR2025 = 3,422.16:
  - source `SRC-CBY-AR2025-BOP`;
  - vintage `CBY_ANNUAL_REPORT_2025`;
  - metric RMT-001, unit USD million;
  - `SOURCE_PUBLISHED`.
- They also carry:
  - comparability state `SAME_VINTAGE_PATH__INDEX_ONLY__NOT_LEVEL_COMPARABLE_WITH_IMF`;
  - a caveat in each language saying the path is compared with the IMF series only when indexed, is not level-comparable
    (CLM-037), and is never joined to the IMF series or to the AR2024 vintage.
- A governed unit label was added in 04: `UI-VIS-UNIT-INDEX-2021`, "Index, 2021 = 100" / «مؤشر، 2021 = 100».

**Contract (`scripts/projection/controlled_inputs/visual_design_contract.json`; generator rule `visual_design_contracts`):**
- **Panel 1 is unchanged:** two AR2024/AR2025 markers at reference year 2024, marked `SAME_YEAR_REVISION`, with no
  connecting line and no percentage change between them.
- **Panel 2 series.** Two lanes, each state REPORTED and marker `NOT_COMPARABLE`:
  - `cby_ar2025_path`: RMO-CBY-2021…2024-AR2025;
  - `imf_staff_path`: RMO-IMF-2021…2024-HIST, the 2025 Article IV staff report.
- **Panel 2 derived paths.** `cby_ar2025_index` and `imf_staff_index`, each divided by its own 2021 value × 100 (state
  DERIVED, unit label `UI-VIS-UNIT-INDEX-2021`). Both read 100 / 105.74 / 111.73 / 118.0.
- **The lanes coincide within rounding.** They are drawn with distinct marks and are never merged, joined or presented
  as one harmonised series. Raw levels appear only in the fallback table, beside their own source.
- **Guard `annual_growth_gap_pp`.** The generator recomputes the largest difference in annual growth for 2022–2024 and
  stops if it departs from the governed CLM-037 value of 0.0032 percentage points (tolerance 0.00005).
  - Recomputed independently: 2022 −0.0001, 2023 −0.0006, 2024 −0.0032 pp.
  - The 2024 level ratio is 1.838 (CLM-042).
- **New generator check.** Every panel marked READY must have values for every bound series and a non-empty path for
  every derived series, or generation stops.
- **Credit:** `SRC-CBY-AR2024-BOP`, `SRC-CBY-AR2025-BOP`, passport `EP-REMITTANCE-MACRO`.

**Rules kept.**
- Indexing compares paths, not levels.
- A same-year restatement is not an economic change and never a collapse (CLM-032).
- The CBY and IMF levels are not comparable (CLM-037).
- The AR2025 path is never joined to the AR2024 vintage.

**Not ingested.** The 2025 value (3,614.05) was read from the same row but is outside P5's scope (2021–2023). The IMF
comparison lane ends in 2024, since the IMF 2025 figure belongs to a different vintage, the supplementary revision.
The 2025 value is deferred to Tranche C currentness work (ledger P5-06).

## 5. Controls corrected during P5

- **Runner snapshot gap (ledger P5-04, MATERIAL).**
  - *What happened.* The first P5-A attempt rolled back correctly on P4-G01 (a stale "423 search records" in handoff
    documents) and on P4-G05 (stale diagrams). But `OPENAI_REENTRY_CHECKPOINT.md` is a rebind recipient and was not in
    the runner's snapshot, so it kept the staged hashes after the rollback.
  - *Fix.* The checkpoint was restored by hand to the then-current hashes. `OPENAI_REENTRY_CHECKPOINT.md` and
    `design/architecture` were added to the runner's snapshot, and the diagram step was added to the runner. The second
    attempt committed.
- **Source-lineage truth test, current state (ledger P5-05).**
  - *What it is.* `audit/pre_tranche_c/source_lineage_truth_test.py` writes
    `audit/pre_tranche_c/SOURCE_LINEAGE_TRUTH_TEST.json`. The Tranche B file is lineage and is not rewritten.
  - *Assertion refined.* The Tranche B assertion "dataset tokens appear only as open inputs" already failed before P5,
    because DS-FINDEX-HISTORY-CROSSWALK lists the Evidence Record DS-FINDEX-PUBLIC-HISTORY as a member. A DS- token that
    is itself an Evidence Record ID now counts when it resolves as a listed member. Every other dataset token must still
    stay an open input and is never expanded.
  - *P5 assertions added:*
    - REF-PAY-001 resolves to a source record;
    - VIS-PAYMENT-RAILS is closed as record and visual;
    - every locator a data contract credits resolves to a source record;
    - no release blocker exists outside an empty declared list.
  - *Result:* 8 of 8.
- **Acceptance matrix.** `audit/pre_tranche_c/pre_tranche_c_acceptance.py` now also runs:
  - the seed-determinism test (items 16 and 17);
  - the lineage truth test (items 4 and 17);
  - the diagram check (item 17).
- **Handoff documents.**
  - `handoff/VISUAL_DESIGN_CONTRACT.md` §3.8 now reads "Open blockers: none" and says how both were closed.
  - The count statements in `handoff/` and `README.md` follow the derived inventory, as gate P4-G01 requires.

## 6. Validation (final state, after P5-B)

| Gate | Result |
|---|---|
| Projection generator check | `PROJECTION CHECK PASS` (40 outputs) |
| Generator tests | 21 tests, OK |
| Literal-audit hash-seed determinism | PASS: 8 seeds, one SHA-256 (§2) |
| Build | 288 HTML files from 143 Page Specs |
| Public-literal audit | 8,285 records, 0 unresolved |
| Validator | `HTML=288 ERRORS=0 WARN=0` — `WEBSITE REPOSITORY VALIDATION PASS` |
| Search probe | 60 of 60 canonical intents PASS (validator P2-G01 re-runs it); legacy 28-term probe 54 PASS, 2 WEAK (reasoned in P2) |
| Source-lineage truth test | PASS 8/8 |
| Architecture-diagram check | `ARCHITECTURE DIAGRAMS CURRENT` |
| Browser suite | `PUBLIC TOOL TESTS PASS: 25/26 passed, 1 not applicable to the current data` |
| Pre-Tranche-C acceptance matrix | 17 PASS, 1 PASS_WITH_RECORDED_LIMITS (item 4: four objects remain partial, each showing its partial state), 0 FAIL. Item 11: `release blockers: {}` |
| Checksum manifest | `SHA256SUMS.txt` regenerated over every file except itself, and verified with `sha256sum -c` on the extracted hand-back ZIP |

Packaging check, run on the extracted ZIP before hand-back:
- the ZIP has one root, `Yemen_Financial_Inclusion_Evidence/`;
- `sha256sum -c SHA256SUMS.txt` passes;
- generator `--check` and the validator pass on the extracted copy.

## 7. Recorded limits (not defects of this window)

- **Decision 23.** The PDF could not be machine-read here. The instrument's identity and provisions were verified from
  the issuing authority's announcement page, which links it. The reference number is as read by the independent review.
- **AR2025 table.** The values were verified by text extraction, not by visual page review.
- **Rights.** The new source record's rights are `NOT_ASSESSED`.
- **Inherited closure.** RV-CWR-001's visual closure inherits Reading CWR-001's closure, which includes the CLM-044 method
  record. The withheld estimate and its no-locator material are still not printed anywhere, and firewall gates S04.2 and
  S04.3 hold.
- **Diagram previews.** The PNG previews of the architecture diagrams are re-rendered on every runner pass. The SVGs are
  the checked output.

## 8. Not claimed

- Native Arabic certification.
- Legal review of the instrument.
- Primary-source verification beyond the two sources above, done as described.
- Tranche C work.
- DESIGN HANDOFF READY or PUBLIC RELEASE READY.
- Any change to an external repository (`EXTERNAL_REPOSITORY_SYNC_PENDING` stands).

Sources consulted in this window:
- `https://cby-ye.com/news/706`
- `https://cby-ye.com/files/667c596ef3bea.pdf`
- `https://english.cby-ye.com/files/6a54b8fcd8b68.pdf`
