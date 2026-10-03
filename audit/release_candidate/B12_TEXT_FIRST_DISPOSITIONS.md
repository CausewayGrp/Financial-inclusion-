# B12 — Text-first visuals: dispositions, 3 October 2026

Part B item B12. Of the 36 visual contracts in `scripts/projection/controlled_inputs/visual_design_contract.json`, 24
carry no data contract (the brief's "24"): 11 TABLE_TEXT_FIRST, 12 SUPPORTING and 1 RETIRE_FROM_DESIGN. One of them,
VIS-PAYMENT-RAILS (SUPPORTING), is already drawn, so 23 render only as text frames and are in scope here.

For each of the 23, the question was whether every value its rationale needs is already governed and source-bound. If
so, the rows are bound Master-first and the contract renders in its designed form. If not, the missing input is named.

The assessment was a read-only pass over the Master projections and the source library, with the originals read where a
value could come from one. Its findings are below, checked and decided here.

## Bound in RC-12

The generator has a new path for these. The `table` key on a text-first contract selects governed rows with the same
guards a data contract uses (`_vdc_objects`, `must_equal`). Every heading, row header and cell is a governed string or a
governed value. The table renders inside the text frame (`visuals.text_table`).

A contract on these tiers still cannot carry a data `contract` or a drawing (`derived.py`, `test_generator.py`,
`validate.py` P3-G02). Gate RC-B12 checks the table on each record page in both languages: every governed row header,
every bound number, and no other number.

| Contract | Table | Rows bound | Guards |
|---|---|---|---|
| VIS-TARGET-RESULT-STATE | state · date or period · access points as defined by the project | FMIIP-RF-004 (baseline Jan 2025, 817; target Jun 2030, 1,021) | 817, 1,021 |
| VIS-FIRM-FINANCE-PATH | item · number · out of | FFO-2022-004 (31 of 328); FFO-2022-LS-01..04 (10, 1, 5, 2 of 18) | all ten values |

### VIS-TARGET-RESULT-STATE

The result row prints the governed string "No observed result is held in the evidence base — not zero".

The World Bank's Implementation Status Report, sequence 2 (`SRC-WB-FMIIP-ISR2-2026-001`, page 3), prints "Actual
(Current) 0" against the 817 baseline. It does the same for the beneficiaries indicator. That 0 is a reporting
placeholder. Binding it would turn a missing value into a zero, so it is not bound.

No dated axis, no percentage of the target, and no placing beside ATM, POS or agent counts. The promotion condition
for a drawing still stands: an observed result under the project's own definition.

### VIS-FIRM-FINANCE-PATH

A governed marker row stands between the line-of-credit row and the loan-source rows: "Not established: whether the
loan-source responses below come from the establishments with a line of credit above." Each base carries its own unit,
"formal establishments surveyed" or "valid loan-source responses". Rows follow the source's order (Table 6), with no
rank.

Source Table 6 is titled "Number of Loans": these are responses, not firms. The report's own sentence on p. 143 links
the two only in narrative. It moves from a line of credit to loans and does not account for the other 13 of the 31.

The promotion condition for a drawn path stands: the 2022 questionnaire's skip logic or the microdata would settle
whether the 18 are a subset of the 31. Neither is in the source library.

## Complete as designed (no table)

| Contract | Why no table |
|---|---|
| VIS-FIRM-FINANCE-SEVERITY | Its rationale chooses the sentence: "a sentence carries them better than a stacked bar, which invites a prevalence reading". Its values are bound in the record (68.71 %, 23.13 %; 91.84 % derived). |
| VIS-EVIDENCE-FRESHNESS | Done in RC-10: the evidence landscape table, gate RC-LAND. |
| VIS-SOURCE-COMPARISON | The Compare tool renders it as a table on `/evidence/compare/`; its record page keeps the text frame (design/06 §5). |
| VIS-CAPITAL-CONTEXT | RETIRE_FROM_DESIGN. Its data are humanitarian context only, and the owner removed the frame (2 October 2026). Not bound. |

VIS-FIRM-FINANCE-SEVERITY has a register item (3 October 2026). The source's sentence on p. 145 places the tabulation
under "reasons of not applying". The base may therefore be non-applicants only, which is narrower than the governed
universe ("excludes firms that said they did not need a loan").

## Not completable now — the missing input, named

| Contract | Tier | Missing input |
|---|---|---|
| VIS-MFI-DIVERGENCE | TABLE_TEXT_FIRST | A governed saver-definition crosswalk ("savers", "savers/depositors", "active savers"), and a governed rial-valuation field on each portfolio anchor (its promotion condition). The values themselves are bound (spine of `data/mfi_data.json`: 2015, 2020, 2023 anchors). Also needed: governed EN/AR labels for the state tokens `CONTRADICTION`, `VERIFIED_DEFINITION_QA` and `SECONDARY_BOUNDED_DEFINITION_OPEN`, and an Arabic universe state. |
| RV-CWR-006 | SUPPORTING | The same as VIS-MFI-DIVERGENCE, whose anchors it draws. |
| RV-CWR-002 | SUPPORTING | The table its rationale describes compares the CBY-Aden annual reports for 2022 and 2023 (CLM-033). Origin table `173_CBY_ANNUAL_VINTAGES`, named by `16_DATASET_CATALOG`, is not a sheet of the Master. The dual 2022 rows in `data/cby_monetary.json` come from a different source (SRC-CBY-001, MFD No. 54) and have not been shown to equal what AR2022 printed. Also needed: the unit label "YER billion" and the vintage labels. |
| RV-CWR-003 | SUPPORTING | Largely duplicates RV-CWR-009 and VIS-PAYMENT-ANATOMY. Needs a governed programme-lane label and the metric crosswalk XW-FMIIP-005 as a data file; it sits in sheet 33 only. |
| RV-CWR-005 | SUPPORTING | Rows from the 2020 e-payment study (`SRC-IBS-EPAY-YEM-2020`, read on 3 October 2026). Table (3), p. 54: accounts by bank, 807,919 in total, December 2019. Table (8), p. 68: values by type, whose type rows reproduce 57.03 / 29.97 / 2.41. These need governed EN/AR labels for the types, with the grouping marked DERIVED. The table is origin table `198_IBS2020_UPSTREAM`, not a sheet of the Master. Accounts are not people; five banks; one bank holds 646,211 of the total. |
| RV-CWR-007 | SUPPORTING | The two levels are bound (WB-FINDEX-OBS-2022-002, -003; the 12.91 gap is derived). The hypotheses MECH-ID-KYC, MECH-DIGITAL-ACCESS, MECH-ACCESS-PROX and MECH-TRUST sit in sheet 32 with no data file. Income has no mechanism. |
| RV-CWR-008 | SUPPORTING | Panel 1 is bound (FFO-2022-CH-06). Panel 2 is VIS-FIRM-FINANCE-SEVERITY (a sentence by design). Panel 3 needs rows from the SMEPS annual report 2024 (`SRC-SMEPS-AR2024-2025`, printed pp. 8–9, KPI "% of MSMEs supported accessed financial services": 16 %, 7 %, 18 %, 19 %, total 15 %, target 40 %). Origin table `219_SMEPS_PROGRAMME_EVIDENCE` is not a sheet of the Master. A target is not a result. |
| RV-CWR-010 | SUPPORTING | Governed EN/AR labels for the ladder steps from transfer to persistence, or a governed mapping onto the chain steps (UI-VIS-CHAIN-*). The reference period of the 45,460 recipients, which CLM-045 says is not recorded. |
| VIS-E-MONEY-RULE-STACK | SUPPORTING | One row per ceiling (value, currency, period); EMR-007..009 pack them into one cell. Arabic text for EMR-001..013, which are English only. The rationale's "31 rows" does not match the 13 held. |
| VIS-FCP-REDRESS-PATH | SUPPORTING | Numeric limit and unit fields for the 10 and 14 business-day limits, which exist only in prose. Arabic step labels for FCP-ARCH-005..008 and -010. |
| VIS-FL-EVIDENCE-LADDER | SUPPORTING | Rung labels in EN and AR. A data file for OECD-YEM-001 (15/100) and -002 (42/100), which are bound in both languages in sheet 29 but have no projection. Arabic text for PA-CBY-FL-001..004. The rationale's "no Yemen value" is stale; correct it Master-first when the rows are bound. |
| VIS-EVIDENCE-CLASS-LADDER | SUPPORTING | A governed class taxonomy with "supports / does not support" text per class in both languages. UI-LAND-CLASS-* has 7 classes, while the summary names 6 different types. |
| VIS-INCLUSION-TRANSMISSION | TABLE_TEXT_FIRST | For each of the 13 system relationships: an evidence reference, a source id with a public locator, a governed evidence state, and Arabic text. The rows in `visuals/system_relationships.json` are English only, and SL-022..026 carry dataset ids only. |
| VIS-EVIDENCE-GAPS | TABLE_TEXT_FIRST | A typed gap field on `10_MEASUREMENT_AGENDA`, with EN/AR labels for the five types. |
| VIS-OECD-FCP-TIMELINE | TABLE_TEXT_FIRST | Event labels: the `event` namespace has no FCP entries. An event row in sheet 31 for the 2024 awareness release, which sits in sheet 32 only (PA-CBY-FCP-002). A chain-step mapping. REF-FCP-001 and FCP-ARCH-002 are English only. |
| VIS-MECHANISM-METRIC-BRIDGE | TABLE_TEXT_FIRST | The contract's edge types reconciled with the governed relationship taxonomy (its promotion condition). |
| VIS-ACCESS-EVIDENCE-LAYER | TABLE_TEXT_FIRST | The MA-005 register of verified, dated operating locations (its promotion condition). |
| VIS-FIRM-FINANCE-PATH (drawing) | TABLE_TEXT_FIRST | Its table is bound (above). A drawn path still needs the questionnaire's skip logic or the microdata. |
| VIS-TARGET-RESULT-STATE (drawing) | TABLE_TEXT_FIRST | Its table is bound (above). A drawn trajectory still needs an observed result under FMIIP-RF-004's definition. |

## Counts

- 23 contracts in scope (24 without a data contract, less VIS-PAYMENT-RAILS, already drawn).
- 2 bound in RC-12.
- 4 complete as designed without a table: one sentence, one landscape done in RC-10, one Compare tool, one retired.
- 17 not completable now, each with its missing input named above. The last two rows of that table are the drawings of
  the two bound tables; they are not counted again.

All 17 go to B16 as POST-LAUNCH items unless the owner supplies the input sooner.

## A finding beyond B12

`16_DATASET_CATALOG` names four origin tables that are not sheets of the 37-sheet Master workbook:
`173_CBY_ANNUAL_VINTAGES`, `198_IBS2020_UPSTREAM`, `201_MFB2023_RECON` and `219_SMEPS_PROGRAMME_EVIDENCE`. The records
that cite them still trace to public originals, through their source ids. The catalog's pointer, though, leads nowhere
in the Master.

This is a register item (3 October 2026). The fix is Master-first, decided at B16: bring the tables in, or record them
as external working tables.
