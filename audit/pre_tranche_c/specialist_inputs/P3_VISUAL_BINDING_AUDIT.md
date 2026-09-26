# Visual binding audit: 36 contracts against the current Master

**Specialist J/B. Read-only. The Team Lead decides.**

**Master read:** SHA-256 `6456add9…`. **Detail:** `visual_binding_audit.json` (bindings, plotted values, 76 inconsistencies).

## Readiness

| State | Count | Contracts |
|---|---|---|
| **DRAWABLE** | 16 | POS ×3, PAYMENT-ANATOMY, FINDEX-GAPS, FIRM ×3, REMITTANCE-COST, REMITTANCE-MACRO, SOURCE-COMPARISON, TARGET-RESULT, MFI-DIVERGENCE, RV-003, RV-004, RV-006 |
| **STATE_ONLY** | 7 | E-MONEY-RULE-STACK, FCP-REDRESS, FL-LADDER, CLASS-LADDER, PAYMENT-RAILS, RV-009, RV-010 |
| **PARTIAL** | 12 | EVIDENCE-GAPS, INCLUSION-TRANSMISSION, MECHANISM-BRIDGE, OECD-FCP-TIMELINE, PROVIDER-OBSERVABILITY, CAPITAL-CONTEXT, ACCESS-LAYER, RV-001, RV-002, RV-005, RV-007, RV-008 |
| **NOT_DRAWABLE** | 1 | EVIDENCE-FRESHNESS |

**Legacy references.** Some legacy references exist only as entries in `16_DATASET_CATALOG`, with no rows in the Master:
- the numbered tables 01, 22, 30, 40, 65, 173/174, 181, 185/186, 189, 191, 196, 198/199, 201/202 and 219;
- `DN-CBY-*`;
- `DS-SYSTEM-CHRONOLOGY`.

Stable IDs do resolve.

**Missing evidence records.** Twelve contracts have no row in `06_EVIDENCE_OBJECTS` and no `/evidence` page: ACCESS-LAYER, MFI-DIVERGENCE and all RV-CWR contracts.

## Signature candidates

**INCLUSION-TRANSMISSION: PARTIAL, with a BLOCKER.** `13_SYSTEM_RELATIONSHIPS` has no evidence-state field. The 26 links split as follows:
- **System links (9):** SL-003/005/007/009 and SL-022–026.
- **Comparison-rule reverse edges (6):** SL-001/002/004/006/008/010.
- **Measurement-agenda links (5):** SL-011–015.
- **Object→page placements (5):** SL-016–020.
- **Navigation (1):** SL-021.

SL-001–021 have no references. SL-022–026 cite an unregistered dataset. `SMEPS-FINACC-2024` exists only in sheet 13. The contract's 7 layers differ from the 6-layer preview in `12_VISUAL_PREVIEWS`.

**EVIDENCE-FRESHNESS: NOT_DRAWABLE.** No governed vintage exists by domain × evidence class. Drawing it would need four derivations:
- **Domain:** from 06 `public_routes`, because 16 `domain` is free text.
- **Evidence class:** a new crosswalk from 34 `authority_class` (49 tokens) or 07 `evidence_badge` (57 tokens).
- **Observation date:** from row-level period fields, some of which are unparseable.
- **Publication date:** not derivable (`retrieval_date` is filled on 1 of 159 sources).

**PROVIDER-OBSERVABILITY: PARTIAL.** The dimensions sit in `22_PROVIDERS_DATA`:
- **Universe:** PUC r65–68.
- **Roster counts:** r139–142.
- **Status events:** r73–87, exchange only.
- **Negative authority:** r91–102, wallets only.
- **Operation:** only entity `operating_state` tokens.

The payment-system-operator class has no row, and the wallet and MFI counts are empty.

**FINDEX-GAPS: DRAWABLE.** The values in `25_FINDEX_BASELINE` r5–10 reconcile. However, the period is labelled "2022 observation", while RV-CWR-007 labels the same data by wave and fieldwork. DA-023/024 are cross-wave changes bound here.

**REMITTANCE-MACRO and RV-CWR-001.**
- **Sources:** 2018–24 are IMF staff-report history (`23_REMITTANCES` r5–11). 2025 is an estimate (r12) and 2026–30 are projections (r13–17), both from the supplement. The line breaks at 2024→2025.
- **Missing predecessor:** the earlier forecast vintage is not held.
- **Passport:** 34 r8 still says "Observed".
- **RV-CWR-001:** the CBY vintage values 6,245 and 3,422.16 exist only as unitless text (YSC-013). The CBY 2021–23 values are absent, so RV-CWR-001 is PARTIAL.

**POS ×3: DRAWABLE.**
- **Reconciles:** Dec→Jan +8.55% (source shows +11%) and +13.87% (source shows +4.9%).
- **Not in the contract:** the June mismatch.
- **Unexplained flags:** December and the January value carry contradiction flags that nothing explains.
- **Gap:** September is missing for value only.
- **Transactions:** peak at 27,187 in July, which the summaries hide.
- **Artefacts:** 20 locators contain "web ref turn…".

**PAYMENT-RAILS: STATE_ONLY.**
- **Duplicate events:** REF-PAY-006/010 and 007/013.
- **Not observed:** go-live and rail-level use.
- **Unbound source:** REF-PAY-001.

## Master cells to correct (proposed text uses only governed fields)

| # | Sheet · row · column | Current | Proposed (source) |
|---|---|---|---|
| 1 | 11 · r22 · freshness_profile / evidence_strength | remittance-macro text / HIGH_MACRO | "event-level / 2026 context" (r22 `period`) / HUMANITARIAN_FINANCE_CONTEXT (35) |
| 2 | 11 · r23 · same | 2025-Q3 / HIGH_QUOTE_BOUNDED | "2022 custom survey" (r24) / PRIMARY_SURVEY (34 r9) |
| 3 | 11 · r25 · same + denominator_universe | Findex text | as #2; base wording from r25 summary |
| 4 | 11 · r9 · same | "2021→2024…" / MEDIUM_MULTI_CLASS | r9 `period` / PRIMARY_OFFICIAL_GUIDANCE (34 r14) |
| 5 | 11 · r10 · period, denominator_universe; 06 · r65 · period_en, currentness_en | "2022 observation" | CLM-001 fields (06 r5) |
| 6 | 11 · r14 · source_period, freshness, period | "2021 baseline" | Drop; first state 2023-08-28 (31 r13) |
| 7 | 19 · r67–86 · source_locator | "…web ref turn…" | "one-page monthly POS infographic" |
| 8 | 22 · r5–60 · current_state_as_of | 46272 / 46282 | 2026-09-07 (r65) / 2026-09-17 (r86) |
| 9 | 33 · r156 · project_state | "FMIIP target" | add Jan-2025 baseline 817 (31 r83) |
| 10 | 34 · r8; 06 · r71 · currentness_en | "Observed 2018–2024"; "bounded to 2018–2030" | 23 `period_state` / `series_vintage` wording |
| 11 | 33 · r28–29 · visual_id | VIS-FINDEX-GAPS | VIS-FINDEX-OBSERVED-WAVES |
| 12 | 13 · r26–30 · evidence_refs; r23 · from | unregistered IDs | DS-V4R3-SYSTEM-CHRONOLOGY (16 r211); CLM-060 |
| 13 | 14 · r18 · fact_en | unitless | "USD million" (CLM-032) |
| 14 | 31 · r18, r21 | duplicate events | merge into REF-PAY-006/007 |
| 15 | 11 · r17; 06 · r67 · summaries | "rose from 8,015 to 24,026" | add July 27,187 peak and September 18,737 (19 r68/r74) |
| 16 | 11 · r30 · encoding_contract | silent | 2015 portfolio = CONTRADICTION (21 r99; CTR-011) |

**For the Lead:**
- **RV-CWR-006:** its title contradicts its own `decision_value`, and it duplicates MFI-DIVERGENCE.
- **Mechanism edges:** 16 edge types in the Master against 4 in the contract.
- **Fractions labelled "percent":** the DA values are stored as fractions.
- **Pipe-packed ceilings:** EMR-007/008/009 put several ceilings in one cell.
- **Humanitarian flows:** 71 flows marked "backend/context only" feed a `/reforms` visual.
