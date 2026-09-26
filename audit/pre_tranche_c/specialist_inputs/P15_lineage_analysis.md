# P15 — Source lineage, evidence closure and Reading verification paths

**Role:** Specialist (Source · Lineage · Analytical Product). Read-only. No repository file was modified.
**Authority read:** `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`. Observed SHA-256 is `4403a3536e218d537710c12cd0df5340a35c058b35f9f06ef0f401a16b9c6dbd`, which differs from the brief's expected entry hash `e698…`. That difference is for the Lead's authority log. Every row number below refers to this workbook.
**Rule applied:** the closure rule v2 in `scripts/projection/derived.py::object_source_closure` plus the governing instruction:
- Resolve only from governed Master evidence.
- A dataset token is never expanded into "all sources in the dataset".
- A Reading's dataset token is removed only when the proposition it served is carried by a bound member record (shown below), or when the token carries no proposition.
**Companion:** `P15_lineage_analysis.json`, the same content in machine-readable form. It includes the exact from→to values for every 08 field.

Two mechanics matter for every Reading recommendation below:
1. A Reading's lineage closure uses only `source_bindings` and `evidence_bindings`. `claim_bindings` is **not** a closure input.
2. The public "Verify this reading" card list is rendered from `verification_bindings.claim_ids`, falling back to `claim_bindings` (`scripts/build.py::reading_verification_links`).

So a record that a Reading relies on must appear in `evidence_bindings` (for lineage) **and** in `verification_bindings.claim_ids` (for the user's path). Claims should also be added to `claim_bindings`. A member whose own state is `COMPOSITE_OF_OBJECTS` or `PARTIALLY_RESOLVED` keeps the Reading open. Only `CLOSED_TO_SOURCE_ID` and `FRAMING_NO_FACT` count as closed.

---

## 0. Verdict summary

| Object | Now | Verdict | Result |
|---|---|---|---|
| CLM-017 | BOUND_PARTIAL | **CLOSE_TO** SRC-CBY-POS-2026-01 + SRC-CBY-POS-PUBLICATION-PAGE-2026-001 | BOUND_EXACT (high confidence) |
| VIS-PAYMENT-RAILS | BOUND_PARTIAL | **KEEP_PARTIAL** (REF-PAY-001 locator has no 15 record; closing it needs a source promotion) | unchanged |
| CLM-045 | BOUND_PARTIAL | **CLOSE_TO** G2PX + SRC-CCY-SAM-2024 + SRC-CCY-ISP-2024 + SRC-CCY-PRESSURE-2026 (Lead to confirm; one renderer precondition) | BOUND_EXACT (conditional) |
| CLM-046 | BOUND_PARTIAL | **KEEP_PARTIAL** (optional precision: add 4 SPA/IMF sources) | unchanged state |
| CLM-056 | BOUND_PARTIAL | **KEEP_PARTIAL now**, then CLOSE_TO SRC-SANAA-MF-2020 after one Master-first data step | conditional |
| CLM-039 | BOUND_PARTIAL | **KEEP_PARTIAL** | unchanged |
| VIS-PROVIDER-TIME | SOURCE_NOT_YET_BOUND | **Bind as COMPOSITE_OF_OBJECTS**, members CLM-009 and CLM-019 | composite listed |
| VIS-DEMAND-VINTAGE-LADDER | COMPOSITE (unlisted) | **LIST_MEMBERS** CLM-001, CLM-027, CLM-028, CLM-029, CLM-030, VIS-FINDEX-RESILIENCE, VIS-FINDEX-BARRIERS | listed |
| DS-FINDEX-HISTORY-CROSSWALK | COMPOSITE (unlisted) | **LIST_MEMBERS** DS-FINDEX-PUBLIC-HISTORY, CLM-026 (medium confidence) | listed |
| DS-QUAL-EVIDENCE | COMPOSITE (unlisted) | **KEEP_UNLISTED**; alternative for the Lead: restate as BOUND_EXACT (row-level sources) | Lead choice |
| 9 other composites | COMPOSITE (unlisted) | **KEEP_UNLISTED** | unchanged |
| Readings | 10 × PARTIAL_PATH | 08-only changes give **8 FULL_PATH**. CWR-010 becomes FULL when CLM-045 closes. CWR-006 becomes FULL when CLM-056 closes | see §4 |

Additional material finding (§5, P15-F1): **CLM-054 is labelled BOUND_EXACT but carries two figures, 792.69 and 1,529.4, whose governed source (SRC-CBY-001) is not bound.**

---

## 1. The six BOUND_PARTIAL records

### 1.1 CLM-017 — "January 2026 is the latest monthly POS release currently available" (06 r22, 07 r21)
- **Tokens:** `SRC-CBY-POS-2026-01` (SOURCE); `UNBOUND:CBY-PAYMENTS-RELEASE-LISTING` (OPEN). The Stage-1 entry token was the prose "current CBY payments page".
- **Open input:** the listing page that shows the March 2025 → January 2026 span.
- **Evidence that the page is already a governed source record:**
  - 15 r70 `SRC-CBY-POS-PUBLICATION-PAGE-2026-001` has primary_url `https://english.cby-ye.com/pages/27` and additional `https://cby-ye.com/pages/11`. Its datasets_or_use is `DS-PAYMENT-CURRENTNESS`.
  - 15 r23–r33: all eleven monthly release records `SRC-CBY-POS-2025-03 … SRC-CBY-POS-2026-01` carry `additional_urls = ["https://english.cby-ye.com/pages/27"]`. That is the page they are listed on.
  - 16 r66 `DS-PAYMENT-CURRENTNESS` (origin `73_PAYMENT_CURRENTNESS`, which is CLM-017's own 07 evidence_input) has the analytical_role *"Controls latest exposed monthly POS period …"*. Its first sample source is that page record.
  - 33 r124 `CON-036` (CONTEXT, reviewed 2026-09-10): *"monthly POS reaches Jan-2026"*.
  - The Stage-1 basis (*"the CBY payments listing page … has no source record"*) is factually superseded.
  - External corroboration (not governing): a live fetch on 2026-09-26 of english.cby-ye.com/pages/27 shows "Monthly Point of Sale Transactions" from March 2025 to January 2026.
- **Verdict: CLOSE_TO** `SRC-CBY-POS-2026-01; SRC-CBY-POS-PUBLICATION-PAGE-2026-001` (high confidence).
- **Master changes (06 r22):**
  - `source_dependencies`: from `SRC-CBY-POS-2026-01; UNBOUND:CBY-PAYMENTS-RELEASE-LISTING` to `SRC-CBY-POS-2026-01; SRC-CBY-POS-PUBLICATION-PAGE-2026-001`. Adding `; CON-036` is optional; it anchors the review date as CONTEXT.
  - `lineage_state`: BOUND_PARTIAL → BOUND_EXACT.
  - `verification_en` / `verification_ar`: replace with the governed `UI-VERIFY-BOUND` texts. `derived.py` enforces an exact match.
  - Optional: add the page to `source_links`.
- **Consequence:** 07 CLM-017 mirrors to CLOSED. The /payments/, /methodology/ and /evidence/CLM-017/ pages lose the partial statement and gain a LOCATOR_ONLY page card. No Reading binds CLM-017. No copy change is needed in either language.

### 1.2 VIS-PAYMENT-RAILS (06 r79)
- **Open:** `UNBOUND:REF-PAY-001`. This is 31 r6, the 2024-06-26 unified domestic transfer network decision, with locator `https://cby-ye.com/files/667c596ef3bea.pdf`.
- No 15 record carries that locator, either as primary or as an additional URL. The ten other drawn events are already bound (Stage-1 basis).
- **Verdict: KEEP_PARTIAL.** Closing it needs a new 15 record. That is a source promotion (SOURCE→VERIFY→ADJUDICATE→MASTER FIRST), which is a Lead decision, not a binding from existing evidence. The candidate locator is already governed in 31 r6.
- Do **not** strip the `UNBOUND:` prefix. A bare `REF-PAY-001` would classify as CONTEXT and falsely produce BOUND_EXACT.
- Visual bindings do not enter Reading closure, so CWR-004 and CWR-009 are unaffected. The visual itself still shows the partial statement.

### 1.3 CLM-045 — "A successful cash payment is not yet durable financial use" (06 r89)
- **Tokens:** G2PX (SOURCE); `EP-YEM-CASH-FIN-TRANSMISSION-K04` (CONTEXT); `DS-K04-CASH-FIN-TRANSMISSION` (OPEN, 16 r180: 7 sources, 17 rows).
- The claim names four links: *"cash delivery through usability, resilience and local financial relationships"*. Row-level governed evidence exists for each:

| Link in claim | Governed row | Source |
|---|---|---|
| cash delivery | already bound; 15 r163 why_it_matters (G2Px pilot) | SRC-WB-G2PX-YEM-UCT-2024-001 |
| usability | 32 r91 **QQL-014**: quant object `DS-K04-CASH-FIN-TRANSMISSION`; *"Cash-out friction explains why successful electronic delivery may still fail usability"* → 32 r42 QUAL-018 | SRC-CCY-PRESSURE-2026 |
| resilience / relational finance | 32 r90 **QQL-013**: same dataset; *"contextualize resilience and household finance"* → 32 r40 QUAL-016 | SRC-CCY-ISP-2024 |
| local financial relationships | 32 r89 **QQL-012**: same dataset; *"local circulation"* → 32 r38 QUAL-014 | SRC-CCY-SAM-2024 |

- This is a row-level selection of 3 of the dataset's 6 library sources, not a dataset expansion. SRC-CCY-CASH-DURATION-2026, SRC-CCY-AMAL-2025 and SRC-WB-RPW-KSA-YEM-2025Q3 are **not** added, because no governed link row ties them to CLM-045's named links.
- **Verdict: CLOSE_TO** `SRC-WB-G2PX-YEM-UCT-2024-001; SRC-CCY-SAM-2024; SRC-CCY-ISP-2024; SRC-CCY-PRESSURE-2026`. Confidence is medium-high, and the Lead must accept QQL-012/013/014 as the link-level evidence.
- **Precondition (MATERIAL, see F2):** the three CCY sources are USER_PROVIDED_FILE with no public locator.
  - `build.py::evidence_sources()` suppresses them.
  - Once the record is CLOSED, the page shows only the G2PX card, with no lineage statement and no "no public locator" note. The page would imply that G2PX is the sole source.
  - Fix the renderer first, or keep the record partial.
- **Master changes (06 r89):**
  - `source_dependencies`: to `SRC-WB-G2PX-YEM-UCT-2024-001; SRC-CCY-SAM-2024; SRC-CCY-ISP-2024; SRC-CCY-PRESSURE-2026; EP-YEM-CASH-FIN-TRANSMISSION-K04`.
  - `lineage_state`: to BOUND_EXACT.
  - `verification_en/ar`: to the UI-VERIFY-BOUND texts.
- Rights are NOT_ASSESSED, the same as the CLM-044 precedent.

### 1.4 CLM-046 — Saudi support flow states (06 r90)
- **Open:** `DS-K04-SAUDI-SUPPORT-TRANSMISSION` (16 r181: AidData; SPA; SDRPY; IMF; Saudi Aid Platform).
- **Verdict: KEEP_PARTIAL.** The claim's "in-kind support and project cost" states rest on the Saudi Aid Platform, which has no 15 record.
- **Optional precision (Lead decision; the state stays BOUND_PARTIAL):** add `SRC-SPA-SAU-CBY-DEPOSIT-2018-001; SRC-SPA-SAU-CBY-DEPOSIT-2023-001; SRC-IMF-AIV-2025-STAFF-001; SRC-SPA-SAU-BUDGET-2026-001`.
  - These carry the agreement, deposit, made-available, budget-support and FX-auction states in 14 r9 YSC-005, r13 YSC-009, r14 YSC-010 and r24 YSC-019, each with explicit source_ids and CLM-046's no-summing rule.
  - The link to CLM-046 is by identical subject and state vocabulary, not by an ID.
- The Stage-1 basis (*"SPA/SDRPY/IMF documents … are not [in the library]"*) is inaccurate for these four records.

### 1.5 CLM-056 — the 91% statement (06 r100)
- **Open:** `DS-V041-STRICT-COUNSEL`. It supplies the 2016–2019 arithmetic: 91.98% growth share and 82.45% 2019 stock share.
- **Governed pointers to one source, SRC-SANAA-MF-2020:**
  - 07 r59 evidence_inputs.
  - 08 r10 CWR-006 source_bindings and direct_source_ids.
  - 33 r102 INS-K04-024, whose text is exactly the 91.98/82.45 finding.
  - 16 r202 DS-V041-STRICT-COUNSEL, with `source_id_count = 1` and SRC-SANAA-MF-2020 as its only ID.
- **But no governed data row carries the inputs:**
  - 17 r180/181 (MFB91-D01/D02) have no source column.
  - 21 has no Kuraimi 2016/2019 rows.
  - The 21 spine's 2019 savers value is UNKNOWN.
- **External check (not governing; machine-read, needs human confirmation):**
  - Sana'a Center *Rethinking Yemen's Economy No. 6*, Figure 6, reports Kuraimi 431,756 (2016) and 1,062,962 (2019), and industry totals 603,012 and 1,289,251.
  - (1,062,962−431,756)/(1,289,251−603,012) = **91.98%**, and 1,062,962/1,289,251 = **82.45%**. Both figures reproduce exactly.
- **Verdict: KEEP_PARTIAL now.** Path to closure:
  1. The Lead verifies Figure 6.
  2. Master-first: add governed data rows (for example in the 21 provider panel: Kuraimi and industry voluntary depositors for 2016 and 2019) citing SRC-SANAA-MF-2020.
  3. In 06 r100, replace `DS-V041-STRICT-COUNSEL` with `SRC-SANAA-MF-2020`, set BOUND_EXACT, and apply the UI-VERIFY-BOUND texts.

### 1.6 CLM-039 — interface ≠ dataset (06 r110)
- **Open:** `DS-K04-REMIT-SOURCE-LENSES`.
- 33 r133 CON-045 and 34 r43 describe "other World Bank surfaces" and "prior access vintages" only generically. No governed row names the surface or vintage that exposed later observations.
- Choosing SRC-WB-MDB40-2024, IGC/AidData or ACAPS would be dataset expansion.
- **Verdict: KEEP_PARTIAL.**

---

## 2. The twelve COMPOSITE_MEMBERS_NOT_LISTED records

| Record (06 row) | Verdict | Evidence / reason |
|---|---|---|
| **VIS-DEMAND-VINTAGE-LADDER** (r53) | **LIST_MEMBERS** `CLM-001; CLM-027; CLM-028; CLM-029; CLM-030; VIS-FINDEX-RESILIENCE; VIS-FINDEX-BARRIERS` | See note A below the table. |
| **DS-FINDEX-HISTORY-CROSSWALK** (r57) | **LIST_MEMBERS** `DS-FINDEX-PUBLIC-HISTORY; CLM-026` (medium) | See note B below the table. |
| DS-QUAL-EVIDENCE (r20) | **KEEP_UNLISTED** (members) | See note C below the table. |
| VIS-INCLUSION-TRANSMISSION (r11) | KEEP_UNLISTED | 11 r12 data_inputs are prose. 13 SL-001…026 are route→route links. Only SL-016/017/018 anchor CLM-003/001/008, and listing those three would misstate a 6–7-layer map. |
| VIS-EVIDENCE-FRESHNESS (r12) | KEEP_UNLISTED | 11 r7 inputs are dataset and passport level. The universe is every record by vintage. |
| VIS-SOURCE-COMPARISON (r13) | KEEP_UNLISTED | Members are chosen by the user. The XW-* crosswalk rows are 33 context rows; only XW-FMIIP-005 is a 06 record. A fixed candidate set, if wanted, is the 10 records routed to /evidence/compare/. |
| VIS-MECHANISM-METRIC-BRIDGE (r17) | KEEP_UNLISTED | Its edges are 32 QQL rows linking QUAL rows to dataset-level objects. Only QUAL-001 is a 06 record. |
| VIS-PROVIDER-OBSERVABILITY (r18) | KEEP_UNLISTED | No governed mapping from badge to record. The operation/activity and payment-system-operator cells have no records. |
| DS-DEMAND-VINTAGE-LENS (r58) | KEEP_UNLISTED | It covers ten functions (the 109 table is not in the Master). At most seven have records; financial worry and connectivity have none. |
| CLM-014 (r63) | KEEP_UNLISTED | The text says "several … observations" and names no records. Editorial candidates: CLM-003/012/018 versus CLM-001/031. |
| VIS-EVIDENCE-GAPS (r78) | KEEP_UNLISTED | The inputs are prose. The governed gap register is sheet 10, which is not 06. |
| VIS-EVIDENCE-CLASS-LADDER (r80) | KEEP_UNLISTED | Its universe is the whole corpus by class. |

**A. VIS-DEMAND-VINTAGE-LADDER**
- r53 `universe_en` names six functions: *"access, saving, borrowing, remittances, resilience and barriers"*. The summary gives each a period.
- Access 2022 is CLM-001, with the 2011 and 2014 anchors in CLM-027.
- Saving 2014 is CLM-029, borrowing 2014 is CLM-028, remittance 2014 is CLM-030.
- Resilience and barriers "await calculation"; their HOLD contracts are r45 and r44.
- This matches the CLM-031 precedent (r51, Stage-1 PB note). Confidence is high for the five CLM records and medium for the two HOLD contracts.

**B. DS-FINDEX-HISTORY-CROSSWALK**
- r57 and 16 r101: *"Maps 36 historical metrics to latest-wave panel contracts"*.
- The historical side is 107, which is the same ID and title as 06 r56 DS-FINDEX-PUBLIC-HISTORY.
- The panel-contract side is 85_FINDEX_PANEL_CATALOG. Its record is CLM-026 (per 07 evidence_inputs; r41 "32-metric panel has been specified").
- The crosswalk asserts no figure of its own. Its method notes stay at dataset level.

**C. DS-QUAL-EVIDENCE**
- The register is exactly the 20 rows of the 32 block "Qualitative evidence" (r25–r44). Only QUAL-001 is a 06 record.
- **Alternative for the Lead:** restate it as **BOUND_EXACT** to the 10 distinct row-level sources: OECD-YEM-RESILIENCE-001, AJMBFS-CBY-FI-2025-001, CCY-REMIT-ESTIMATE-2025, CCY-SAM-2024, CCY-CASH-DURATION-2026, CCY-ISP-2024, CCY-AMAL-2025, CCY-PRESSURE-2026, AIDDATA-SAUDI-YEM-2015 and IMF-D4D-YEM-ESS-2025.
- This follows the VIS-MFI-SPINE precedent of row-level binding.
- The current "not yet linked individually here" text implies a linkage that cannot exist.
- The CCY renderer caveat from F2 applies.

For each LIST_MEMBERS change: set 06 `source_dependencies` to the member IDs and replace `verification_en/ar` with the `UI-VERIFY-COMPOSITE` texts. The page then shows the "Evidence records assembled in this view" links. There is no other copy change.

## 3. VIS-PROVIDER-TIME (06 r14)
- There is no row in 11. The 06 text maps one-to-one onto two BOUND_EXACT records:
  - *"roster by the classes the source defines"* is **CLM-009** (r7: 98/225/106 by roster class; SRC-CBY-EXCH-LIST-2026-001).
  - *"later dated enforcement events shown separately"* plus the method *"Do not subtract events mechanically"* is **CLM-019** (r24: roster plus 13 ENF decisions; *"must not be mechanically subtracted"*).
- The Stage-1 SOURCE_NOT_YET_BOUND basis (*"BLOCKED … no public render"*) is superseded. 06 `visual_contract_state` is now `NO_GOVERNED_CONTRACT__TABLE_ONLY`, and lineage state and render state are separate axes.
- **Verdict: bind as COMPOSITE_OF_OBJECTS**, members `CLM-009; CLM-019`.
  - 06 r14 `source_dependencies`: (empty) → `CLM-009; CLM-019`.
  - `lineage_state`: SOURCE_NOT_YET_BOUND → COMPOSITE_OF_OBJECTS.
  - `verification_en/ar`: UI-EVID-UNBOUND → UI-VERIFY-COMPOSITE texts.
- Binding it BOUND_EXACT to CLM-019's 14 sources is not recommended, because the entity-level overlay is not yet built.

---

## 4. Readings — verification paths

Legend: **bound** means the record is already in `evidence_bindings`. Every record named below is BOUND_EXACT or FRAMING, unless marked otherwise. Section references ("s") are 09 `section_order`. EN/AR numeric parity of all 09 and 08 copy was checked and passes; the only differences are "2022–23" versus "2022–2023" formatting.

### CWR-001 Same year, different number (08 r5): PARTIAL_PATH now, FULL_PATH after 08-only changes

| Proposition | Record | Sources | In 08? |
|---|---|---|---|
| AR2024 USD 6.245bn vs AR2025 restated ~USD 3.42bn (thesis, s1, s2) | CLM-032 | SRC-CBY-AR2024-BOP; SRC-CBY-AR2025-BOP | yes |
| IMF 2024–25 ESS reconstruction, demographic-behavioural model (s2) | CLM-036 | SRC-IMF-D4D-YEM-ESS-2025; SRC-IMF-YEM-AIV-2025-2026 | yes |
| 2021=100 paths almost identical; max growth difference ~0.0032 pp (s2, s3) | CLM-037 | AR2025; IMF AIV | yes |
| **~1.838 ratio is not a conversion (s5, prohibited_inference)** | CLM-042 (1.838 is stated in CLM-041 limitations) | AR2025; IMF AIV | **no** |
| **IMF 33% population share is not universal (s5, prohibited)** | CLM-041 | AR2025; IMF AIV | **no** |
| **E&O is not hidden remittances (s5, prohibited)** | CLM-043 | AR2025 | **no** |
| **CCY ≥US$7.4bn is not a baseline (s5, prohibited)** | CLM-044 | SRC-CCY-REMIT-ESTIMATE-2025 (no public locator) | **no** |

Dataset tokens:
- `173_CBY_ANNUAL_VINTAGES` is carried by CLM-032 (the Stage-1 basis explicitly replaced 173 with AR2024 and AR2025).
- `181` / `181_REMITTANCE_METHOD_RECON` is carried by CLM-036, CLM-037 and CLM-042 (07 evidence_inputs).
- `191` is carried by CLM-041 and CLM-042.
- `186` (remittance regimes) is not declared by any member. The only regimes the Reading names are CBY, IMF and CCY, and those are carried by CLM-037, CLM-042 and CLM-044.

**Minimal 08 change:**
- Add CLM-041, 042, 043 and 044 to `claim_bindings`, `evidence_bindings` and `verification_bindings.claim_ids`.
- Remove `181, 186, 191` from `evidence_bindings`.
- Remove `173_CBY_ANNUAL_VINTAGES` and `181_REMITTANCE_METHOD_RECON` from `source_bindings` and `verification_bindings.dependency_ids`.

Result: CLOSED. Resolved sources are AR2024, AR2025, IMF-D4D-ESS, IMF-AIV and CCY-REMIT-ESTIMATE.

### CWR-002 Banking jump (08 r6): PARTIAL_PATH (tokens only), then FULL_PATH
- Propositions:
  - Thesis and s2: CLM-033 (AR2022/AR2023). Bound.
  - s2 and s3, 1996 precedent: CLM-038 (EGDDS-1996, AR2023). Bound.
  - s7, "circular not available": an absence statement.
- Tokens:
  - `173`, `173_CBY_ANNUAL_VINTAGES` → CLM-033.
  - `185`, `185_BANKING_VALUATION_RECON` → CLM-038 (07).
  - `174` (analytics derived from 173) → CLM-033. Its analytic rows are already anchored by the context token `AVA-005..008`.
- **Change:** remove `173, 174, 185` from `evidence_bindings`. Remove `173_CBY_ANNUAL_VINTAGES` and `185_BANKING_VALUATION_RECON` from `source_bindings` and `dependency_ids`.

### CWR-003 Define what you count (08 r7): PARTIAL_PATH (tokens only), then FULL_PATH
- Propositions:
  - Thesis and s2, "units differ" and "accounts/transactions are not people": CLM-004 (FRAMING).
  - Thesis, "targets mislead when the unit changes": XW-FMIIP-005 (1,021 access-point target versus ATMs/POS/agents; SRC-UNDP-FMIIP-001 and SRC-CBY-PAYREPORT-H1-2025). It is in `evidence_bindings` but **not** in the Verify list.
  - s2, "1,000 respondents; fieldwork 7-Nov-2022 to 9-Jan-2023": CLM-023.
  - s2, raw case shares: CLM-024.
  - s2, 23% excluded and more than a quarter of PSUs replaced: CLM-025.
- Tokens:
  - 25, 26 → CLM-023 and CLM-025.
  - 87, 29 → CLM-024.
  - 85, 86, 89 → CLM-026.
  - 11, 49 → CLM-004 and XW-FMIIP-005. These are all declared in the members' 07 evidence_inputs.
- **Change:**
  - Remove the 9 dataset tokens from `source_bindings` and `dependency_ids`.
  - Remove `49_METRIC_CROSSWALK` from `evidence_bindings`.
  - Add XW-FMIIP-005 to `verification_bindings.claim_ids`.

### CWR-004 Reform clock versus people clock (08 r8): PARTIAL_PATH, then FULL_PATH
- Propositions:
  - 11.9%, 2021 wave, fieldwork 2022–23: CLM-001. Bound.
  - POS 561 → 1,473: CLM-003. Bound.
  - IMF staff-level agreement, 16 July 2026: CLM-049. Bound.
  - **s3 "material geographic exclusions": CLM-025. Not bound.**
  - **Thesis and s3, "official records show payment-architecture institutionalization in 2026": CLM-018. Not bound.**
- Tokens:
  - 28 → CLM-001.
  - 11 → CLM-003.
  - 194 → CLM-049. Stage-1 noted "'194' adds no input"; 194 is an internal gate with 0 sources.
  - 48 and 73 → CLM-018 and CLM-003.
  - 107 → no proposition uses the 2011/2014 history.
- **Change:**
  - Add CLM-018 and CLM-025 to all three binding fields.
  - Remove `48_REFORM_EVENTS, 73_PAYMENT_CURRENTNESS, 107_FINDEX_PUBLIC_HISTORY` from `evidence_bindings`.
  - Remove `28_FINDEX_OBS, 11_CBY_PAYMENTS, 194` from `source_bindings` and `dependency_ids`.

### CWR-005 Digital workaround (08 r9): PARTIAL_PATH (tokens only), then FULL_PATH
- Propositions:
  - 807,919 accounts, 23% dormant, one-time or imposed use: CLM-050.
  - 57.03%, 29.97% and 2.41% (CauseWay grouping): CLM-051.
  - 93.8% urban, ~13% women: CLM-052.
  - All three are bound to SRC-IBS-EPAY-YEM-2020.
- Tokens:
  - `198` (sole source is IBS) and `199` → CLM-050, 051 and 052 (07). No proposition uses 199's Sana'a 2022 secondary.
  - `196` is `DS-K04-CAUSEWAY-READING-002`, an internal editorial draft reading, *"not public until upstream/right/editorial gates close"*. It is provenance, not evidence, and it is circular as a lineage input.
- **Change:** remove `198, 199, 196` from `evidence_bindings`, and `198, 199` from `source_bindings` and `dependency_ids`.

### CWR-006 Microfinance divergence (08 r10): PARTIAL_PATH; stays PARTIAL until CLM-056 closes

| Proposition | Record | Status |
|---|---|---|
| 93,118 / 88,445 verified; 78,686 secondary (thesis, s1, s2) | CLM-054 (78,686 also in CLM-053) | bound |
| ~80,800 June 2023, a separate chain (s2) | CLM-057 | bound |
| 1.611m / YER33.379bn (2020); 3.3m / ~YER44bn (2023); nominal, valuation unrecorded | CLM-054 | bound (but see F1) |
| 26 banks, 12 MFBs by name | CLM-055 | bound |
| 91% attributed to growth, with the 2025 stock restatement | CLM-056 (MFB-2024, YR-2025) | bound; member partial |
| **~91.98% growth share vs ~82.45% stock share (s2)** | CLM-056 → open DS-V041 | **GAP** (the Reading's direct source SRC-SANAA-MF-2020 is the evidenced origin; §1.5) |
| ~80,000–90,000 through 2021 (s2) | CLM-058 (FSD 2024) | bound |

Tokens:
- `201` → CLM-056, 057 and 058.
- `202` → CLM-054 and 055.
- `15_PROVIDER_MASTER` and `16_PROVIDER_UNIVERSE` → CLM-055.
- `203` is the internal CauseWay Reading 003 draft.

**Change:**
- Remove `201, 202` from `evidence_bindings`.
- Remove `202, 203, 15_…, 16_…, 201` from `source_bindings` and `dependency_ids`.
- Keep the direct sources SRC-SANAA-MF-2020 and SRC-WB-FSD-2024-001.

The only remaining gap is CLM-056. The Reading becomes FULL_PATH once CLM-056 is bound Master-first (§1.5).

### CWR-007 Gender gap (08 r11): PARTIAL_PATH, then FULL_PATH
- Propositions:
  - **5.44% women versus 18.35% men (thesis, s1–s3): VIS-FINDEX-GAPS. Not bound.** CLM-002 states only 12.91. The context row 33 DA-001 names VIS-FINDEX-GAPS as its visual.
  - 12.91 pp: CLM-002 plus DA-001. Bound.
  - **11.9% overall: CLM-001. Not bound.**
  - **Fieldwork 2022–23 and exclusions: CLM-025 and CLM-001. Not bound.**
  - Mechanism list (thesis, s4): no record. It is hypothesis framing, aligned with the MA-003 dimensions. "product design" is not among the MA-003 dimensions (editorial).
- Tokens:
  - 28 → CLM-001, CLM-002 and VIS-FINDEX-GAPS (single source AGG-2022).
  - 41 → the DA-001 context row, which is kept.
  - `22_RESEARCH_COVERAGE` has 0 sources and carries no figure.
- **Change:**
  - `evidence_bindings`: CLM-002, VIS-FINDEX-GAPS, CLM-001, CLM-025.
  - `claim_bindings` gains CLM-001 and CLM-025.
  - The Verify list gains CLM-001, CLM-025 and VIS-FINDEX-GAPS.
  - Remove `28, 41, 22` from `evidence_bindings`, and `28_FINDEX_OBS` from `source_bindings` and `dependency_ids`.

### CWR-008 Finance constraint (08 r12): PARTIAL_PATH, then FULL_PATH
- Propositions:
  - **22% finance versus 50% electricity and 46% fuel (thesis, s3): VIS-FIRM-CONSTRAINTS (FSD 2024). Not bound.** Today these figures reach only the 33 context row INS-004.
  - Ranking: CLM-005.
  - 91.84%: CLM-006.
  - SMEPS 19%, 15% and 40%: CLM-060.
- Tokens:
  - 12 → CLM-005, CLM-006 and VIS-FIRM-CONSTRAINTS.
  - 219 → CLM-060.
  - `50_STRATEGIC_INSIGHTS` has 0 sources; INS-004 is kept as context.
- **Change:**
  - Add VIS-FIRM-CONSTRAINTS to `evidence_bindings` and the Verify list.
  - Remove `12, 219, 50` from `evidence_bindings`, and `12, 219` from `source_bindings` and `dependency_ids`.

### CWR-009 Rail to result (08 r13): PARTIAL_PATH (tokens only), then FULL_PATH
- Propositions:
  - 561 → 1,473: CLM-003.
  - Accounts are not people: CLM-004.
  - June–August 2026 unified network and YPCC: CLM-018.
  - Target is not result: XW-FMIIP-005.
  - All are bound.
- Tokens:
  - 11 → CLM-003 and CLM-004.
  - 49 → CLM-004 and XW-FMIIP-005.
  - 73 → CLM-018.
  - `REF-PAY-010..013` → CLM-018. Stage-1 mapped these four events' locators to CLM-018's four sources.
  - 48 → CLM-018.
  - The range token is not matched by any context pattern. Remove it, or replace it with the four individual CONTEXT IDs.
- **Change:** remove the 5 tokens, and add XW-FMIIP-005 to the Verify list.

### CWR-010 After-transfer persistence (08 r14): PARTIAL_PATH; FULL_PATH if CLM-045 closes
- Propositions:
  - G2Px pilot, 8 districts, 45,460 recipients (s2): **source-direct only**. 15 r163 why_it_matters names the figure, and 14 r17 YSC-024 cites the same source. There is no Evidence Record (F4).
  - Several links; persistence not established: CLM-045, a partial member.
- Tokens: `189` and `189_CASH_FINANCE_TRANSMISSION` → CLM-045 (07).
- **Change:** remove both tokens.
- The Reading closes only when CLM-045 closes (§1.3). Otherwise it remains PARTIAL with that single, honest gap.

**Simulated with the derived.py logic:** 08-only changes make CWR-001, 002, 003, 004, 005, 007, 008 and 009 `CLOSED_TO_SOURCE_ID`. CWR-006 stays open on CLM-056, and CWR-010 stays open on CLM-045. The Reading text changes in neither language; only the Verify card lists grow, with titles taken from the already bilingual records.

---

## 5. Incidental findings for the ledger
- **P15-F1 (MATERIAL).** 06 r98 **CLM-054** states *"average market rate published by the Central Bank in Aden moved from 792.69 to 1,529.4"*.
  - These values are 18 r625 `OBS-CBY-00621` and r661 `OBS-CBY-00657`, with source_id **SRC-CBY-001** (T6_Market_Exchange_Rates).
  - SRC-CBY-001 is not in CLM-054's dependencies, yet the record is labelled BOUND_EXACT ("drawn from the sources listed").
  - **Action:** add `SRC-CBY-001` to 06 r98 `source_dependencies`. The state stays BOUND_EXACT.
  - An automated numeric sweep of all BOUND_EXACT records found no other genuine case. The remaining hits were numeric collisions.
- **P15-F2 (MATERIAL).** Renderer: when a CLOSED record binds both public and locator-less sources, the suppressed sources disappear with no statement.
  - This affects CLM-045 (if closed), the DS-QUAL-EVIDENCE alternative, and CWR-001's source list after CLM-044 is added.
  - **Fix:** always show the governed no-public-locator note when `suppressed_count > 0`.
- **P15-F3 (EDITORIAL).** The Stage-1 adjudication bases are now inaccurate for CLM-017, CLM-046 and VIS-PROVIDER-TIME. Regenerate `SOURCE_LINEAGE_TRUTH_TEST.json` after any change. No test hard-codes the counts.
- **P15-F4 (EDITORIAL).** CWR-010's G2Px figure has no Evidence Record, only a source-direct path. Keep it; creating a record would be new Master content and a Lead decision.
- **P15-F5 (EDITORIAL, for Specialist C).** The held "portfolio" anomaly in 21 r102 (SFD Q4-2018), 943.83 YER m, equals digit-for-digit the 2018 industry saver count of 943,830 in the Sana'a 2020 Figure 6. This may be a label transposition. No change is proposed.

## 6. Proposed Master changes (all route through the Lead; Master first, then regenerate)

| # | Sheet / row | Field | From → To | Confidence |
|---|---|---|---|---|
| 1 | 06 r22 CLM-017 | source_dependencies; lineage_state; verification_en/ar | UNBOUND listing → `SRC-CBY-POS-PUBLICATION-PAGE-2026-001`; BOUND_PARTIAL → BOUND_EXACT; UI-VERIFY-BOUND | High |
| 2 | 06 r14 VIS-PROVIDER-TIME | same three fields | (empty) → `CLM-009; CLM-019`; SNYB → COMPOSITE_OF_OBJECTS; UI-VERIFY-COMPOSITE | High |
| 3 | 06 r53 VIS-DEMAND-VINTAGE-LADDER | source_dependencies; verification | (empty) → 7 members; UI-VERIFY-COMPOSITE | High / medium |
| 4 | 06 r57 DS-FINDEX-HISTORY-CROSSWALK | source_dependencies; verification | (empty) → `DS-FINDEX-PUBLIC-HISTORY; CLM-026`; UI-VERIFY-COMPOSITE | Medium |
| 5 | 06 r98 CLM-054 | source_dependencies | add `SRC-CBY-001` | High |
| 6 | 08 r5–r13 (CWR-001…009) | claim/evidence/source/verification bindings | as in §4 (exact values in JSON `readings.*.08_changes`) | High |
| 7 | 08 r14 CWR-010 | evidence/source bindings | remove `189`, `189_CASH_FINANCE_TRANSMISSION` | High |
| 8c | 06 r89 CLM-045 | deps; state; verification | → G2PX + 3 CCY; BOUND_EXACT | Conditional (Lead confirmation + renderer fix F2) |
| 9c | 06 r100 CLM-056 | deps; state; verification | DS-V041 → `SRC-SANAA-MF-2020` after Master-first data rows | Conditional (SOURCE→VERIFY) |
| 10o | 06 r90 CLM-046 | source_dependencies | add 4 SPA/IMF sources; state unchanged | Optional |
| 11o | 06 r20 DS-QUAL-EVIDENCE | deps; state | → 10 row-level sources; BOUND_EXACT | Optional (Lead) |

**Counts in 06:**

| State | Now | After firm changes 1–5 |
|---|---|---|
| BOUND_EXACT | 87 | 88 |
| BOUND_PARTIAL | 6 | 5 |
| COMPOSITE, members listed | 1 | 4 |
| COMPOSITE, members unlisted | 12 | 10 |
| SOURCE_NOT_YET_BOUND | 1 | 0 |
| FRAMING_NO_FACT | 1 | 1 |

With the conditional changes, BOUND_EXACT reaches 90 and BOUND_PARTIAL falls to 3. Readings go from 0 FULL / 10 PARTIAL to **8 FULL** (08-only), then 9 (with CLM-045), then 10 (with CLM-056).

**What stays open, truthfully:**
- CLM-039: WB surfaces and vintages are not identified.
- CLM-046: the Saudi Aid Platform has no source record.
- VIS-PAYMENT-RAILS: REF-PAY-001 needs a source promotion.
- CLM-056 until its data rows exist, and CLM-045 if the Lead declines the QQL mapping.
- 10 composites without enumerable members.
