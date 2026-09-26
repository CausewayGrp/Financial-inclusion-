# P17 — Chronology restoration assurance (AIR-001, 14_SYSTEM_CHRONOLOGY YSC-014…YSC-023)

Role: Specialist F (Source, Law and Currentness Librarian). Read-only. No repository file was modified.
Date of checks: 2026-09-26. Method: Master read through `scripts/projection/master_reader.Workbook`; projection `site-src/content/visuals/system_chronology.json`; source records `site-src/content/sources/source_library.json` and Master `15_SOURCE_LIBRARY`; cross-sheet scan of all 37 Master sheets; original-source checks through WebFetch/WebSearch. The shell cannot reach the source sites (proxy returns 403 on CONNECT).

Current bytes: Master `4403a353…c6dbd`; projection `3959aada…a9f57`. Both match `SHA256SUMS.txt`.

---

## A. Structural and AIR-001 ledger conformance

| Check | Result | Evidence |
|---|---|---|
| Event count and uniqueness (Master) | PASS: 24 IDs, 0 duplicates | Rows 5–28 in `14_SYSTEM_CHRONOLOGY` |
| Event count and uniqueness (projection) | PASS: 24 IDs, 0 duplicates | `system_chronology.json` |
| YSC-013 not duplicated | PASS: one row only (r18) | The 11 corrupt copies (r18–r28) are gone |
| YSC-024 not duplicated | PASS: one row only (r17) | `system_implication_en` is English again (it held Arabic at entry) |
| Row→event map matches the ledger | PASS | r19–r28 = 014, 015, 016, 017, 018, 019, 021, 022, 023, 020, exactly as in `AIR-001_LEDGER.json.rows_restored` |
| Master equals projection | PASS: all 24 events × 16 fields identical | Field-by-field diff returned no differences |
| Ledger `cells_written = 162` reproducible from current values | PASS | In r19–r28, 160 of 160 cells differ from the YSC-013 row, plus the 2 r17 cells. 160 + 2 = 162 |
| Post-AIR-001 edits to sheet 14 | One governed edit only | `PB-0415.S119` (Stage 5, `STAGE5_SWEEP_ROW_LEDGER.csv`, REVISED): YSC-020 `system_implication_en` "The product can trace…" → "This resource can trace…". No other stage ledger or run report touches sheet 14. The Stage 1–5 scripts do not iterate over all sheets. |
| Per-field comparison with the certified projection (sha `8d058126…`) | **NOT POSSIBLE NOW** | The ledger records only hashes and verification flags, not per-field expected values. The certified file is no longer on disk: regeneration overwrote it and it was not archived (a filesystem hash search found no copy). Equality therefore rests on the Stage 0 script's own check (`sheet_equals_certified_projection: true`). I reviewed that script's logic and found it sound (exact-value `expect=` guards; abort on mismatch). The arithmetic test in the previous row also supports it. |

---

## B. Per-event verification

Legend for grades: VERIFIED_AGAINST_ORIGINAL · CONSISTENT_WITH_GOVERNED_RECORDS · DISCREPANCY · UNVERIFIABLE_NOW.

### YSC-014 — 2022–April 2025 — BANKING_LIQUIDITY_CAPITAL_STRESS
| Dimension | Finding |
|---|---|
| Identity | Unique. Observed prudential-ratio fact; the event class fits. |
| Date/period | "2022–April 2025": internally coherent. |
| EN/AR statement | Same meaning; numbers identical (148, 69, 2022, April 2025, ~5, ~2.5). Neither language states the ratio unit (percent). |
| Evidence class | Observed ratios, labelled CONTEXT; the does-not-establish fields are correct (no unique-person inference). |
| Source binding | `SRC-IMF-AIV-2025-STAFF-001` exists. Its URL resolves to IMF Country Report 2026/080 (2025 Article IV, published 3 Apr 2026), confirmed on the imf.org publications page. The same source backs `23_REMITTANCES` RMO-IMF-2018…2024. |
| Original check | eLibrary PDF and XML returned **403** on every route; the imf.org press-release body did not render. Not verified. |
| Cross-check | **No governed Master row holds bank soundness ratios**, so there is no internal cross-check. **Tension, not adjudicated:** the non-governed project literature review (v4.1, citing `YFSI-OFF-001`, the IMF 2025 Art. IV FSI panel, Aden scope) gives liquid assets/short-term liabilities **171.8 → 73.6** (Dec 2014 → Aug 2025) and capital/assets **3.8%** (Aug 2025). That panel differs in dates from YSC-014's 148 (2022) → 69 (Apr 2025) and ~5 → ~2.5, and the two are unreconciled. A capital/assets figure of ~2.5 in April 2025 against 3.8 in August 2025 may be a different table, chart or perimeter within the same report. |
| **Grade** | **UNVERIFIABLE_NOW**, with an open tension flag. Before public reliance, read CR 26/80 to confirm which figure or table gives 148/69/5/2.5 and add the unit. |

### YSC-015 — July 2025 onward — FX_IMPORT_POLICY
| Dimension | Finding |
|---|---|
| Identity | Unique. Institutional or policy creation; the event class fits. MECHANISM_HYPOTHESIS is appropriate. |
| Date/period | "July 2025 onward" is supported by a secondary report of the IMF 9 Oct 2025 Article IV concluding statement (South24: "the establishment of the National Committee for Regulating and Financing Imports in July"). Yemen Monitor (1 Aug 2025) reports the PM decree forming the "**Supreme** National Committee for the Regulation and Financing of Imports". |
| EN/AR statement | Same meaning; no numbers. |
| Evidence class | Creation ≠ outcome. The does-not-establish fields guard this correctly. |
| Source binding | `SRC-IMF-AIV-2025-STAFF-001` (as above). |
| Original check | IMF staff report not reachable (403). |
| Cross-check | No other governed Master row. Secondary sources confirm the purpose: prioritise FX for essential goods, oversight of financing sources, transparency. **Wording risk:** "channel FX through the formal banking sector" may be narrower than the mechanism. The project literature review says requests go through "banks **or exchange companies**". This cannot be adjudicated without the staff report. |
| **Grade** | **UNVERIFIABLE_NOW** against the original; corroborated by secondary reporting of the IMF concluding statement. |

### YSC-016 — Mid-July–early August 2025 — FX_STABILIZATION_EPISODE
| Dimension | Finding |
|---|---|
| Identity | Unique. Observed market episode; the event class fits. |
| Date/period | Coherent with governed data. |
| EN/AR statement | Same meaning; numbers identical (2,900; 1,600; 2025). Both languages keep the IRG-market scope. |
| Evidence class | CONTEXT. "After a package of measures" is temporal; the does-not-establish fields block a causal or stability claim. |
| Source binding | `SRC-IMF-AIV-2025-STAFF-001`. |
| Original check | Not reachable (403). |
| Cross-check | **Governed `18_CBY_MONETARY` (independent source SRC-CBY-001, T6 market rates):** monthly average YER/USD 2,733.85 (Jun 2025), 2,212.7 (Jul), 1,624.5 (Aug), 1,623.99 (Sep). This is consistent with a mid-July peak near 2,900 and about 1,600 by early August. The UK Commons Library briefing CBP-10427 (p. 20) records the rial at "2,905R per US$" in July 2025. |
| **Grade** | **CONSISTENT_WITH_GOVERNED_RECORDS** (cross-source); original not reachable. |

### YSC-017 — September 2025 — RESERVE_CONSTRAINT
| Dimension | Finding |
|---|---|
| Identity | Unique; observed state; the event class fits. |
| Date/period | September 2025. |
| EN/AR statement | Same; US$350 million and "about one month" match in both languages. |
| Evidence class | CONTEXT; the does-not-establish fields are correct. |
| Source binding | `SRC-IMF-AIV-2025-STAFF-001`. |
| Original check | Not reachable (403). |
| Cross-check | No governed Master row. The non-governed project corpus agrees: literature review v4.1 has "operational reserves of US$350m at September 2025, about one month of imports" citing the IMF 2025 Art. IV, and Evidence Synthesis v1.0 X-07 has "IMF US$350m operational at Sep 2025". The IMF Oct 2025 concluding statement, as reported, says reserves "cover **less than** one month of imports". That is a minor wording difference from "roughly one month". **Currentness note:** the project corpus records a later IMF end-2025 figure (US$142m, 0.4 months). The September 2025 event stays correct as a dated point. |
| **Grade** | **UNVERIFIABLE_NOW** against the original; corroborated by the project corpus (non-governed). |

### YSC-018 — 17 June 2025–2030 project period — INTERNATIONAL_INFRASTRUCTURE_SUPPORT
| Dimension | Finding |
|---|---|
| Identity | Unique; approval and status fact; the event class fits. DEPENDENCY is appropriate. |
| Date/period | 17 Jun 2025 approval, 30 Jun 2030 closing, ISR seq. 2 dated 8 Apr 2026. |
| EN/AR statement | Same meaning; numbers identical (20, 17 June 2025, P180708, 30 June 2030, 2, 8 April 2026). **Editorial:** the Arabic project name "مشروع البنية التحتية للأسواق المالية والشمول" differs in word order from the source-library Arabic title "مشروع البنية التحتية للأسواق والشمول المالي". |
| Evidence class | Approval, commitment and ISR are kept separate from adoption and outcomes. Correct. |
| Source binding | `SRC-WB-FMIIP-P180708`, `SRC-UNDP-FMIIP-001` and `SRC-WB-FMIIP-ISR-2026-04` all exist. **Source-identity defect:** `SRC-WB-FMIIP-ISR-2026-04` (LOCATOR_ONLY, no title or publisher) and `SRC-WB-FMIIP-ISR2-2026-001` (FULL_PUBLIC_CARD, "Sequence 2 (8 April 2026)") are **two source records for the same URL** (`documentdetail/099040826144025755`). YSC-018 and `16 DS-FMIIP-IMPLEMENTATION-2026` cite the first. `06 VIS-PAYMENT-RAILS` and `15` r93 use the second. |
| Original check | **WB press release 17 Jun 2025:** "US$30 million in new grants to Yemen", of which "US$20 million" is for FMIIP, implemented by "United Nations Development Programme (UNDP)". **PAD PADHI00396:** "US$20 MILLION" IDA grant, Expected Closing Date "30-Jun-2030", UNDP. **ISR seq. 1 (22 Sep 2025):** Approval Date "17-Jun-2025", Effectiveness "01-Sep-2025", Original Closing "30-Jun-2030". **ISR seq. 2 page:** title "Disclosable Version of the ISR – … – P180708 – Sequence No : 2". The page shows no date text; 8 Apr 2026 is inferred from the WB document-ID pattern (`0990408 26…`). That pattern matched the API or report date for 6 of 7 other P180708 documents; one differed by 6 days. The UNDP page confirms UNDP, the FPS/RTGS components and a June 2030 end. The WB search API still shows a stale "Pipeline" status (last updated 2023), so "active" rests on effectiveness plus the ISRs. ISR1 values the grant at about US$21.12m (SDR revaluation). That is not a discrepancy with the US$20m approval. |
| Cross-check | Governed `31_REFORMS_REGULATION` REF-FMIIP-APPROVAL-2025 (17 Jun 2025, US$20m IDA, UNDP, closing 30 Jun 2030) and REF-FMIIP-ISR2-2026 (2026-04-08) agree. |
| **Grade** | **VERIFIED_AGAINST_ORIGINAL** for approval date, amount, UNDP and closing date. The ISR-2 date is strongly indicated but not quoted from page text. Source-duplication defect noted. |

### YSC-019 — 1 March 2026 — INTERNATIONAL_BUDGET_SUPPORT
| Dimension | Finding |
|---|---|
| Identity | Unique; agreement event. |
| Date/period | 1 Mar 2026: verified. |
| EN/AR statement | Same meaning; SAR1.3bn in both. The Arabic `fact` carries the date inline; the English relies on `period`. Minor asymmetry. |
| Evidence class | Agreement, and the does-not-establish fields correctly block equating it with IMF USD flows. **Recommended tightening:** no field says an **agreement to deposit is not evidence of an actual deposit or disbursement**. The `system_implication` calls it "a fiscal flow". The project's own flow-state passport (`34 EP-SAUDI-SUPPORT-FLOWSTATE-K04`) requires agreement ≠ deposited custody ≠ disbursement. |
| Source binding | `SRC-SPA-SAU-BUDGET-2026-001` exists but is LOCATOR_ONLY, with no title or publisher. |
| Original check | **SPA EN (N2525739), 1 Mar 2026:** "The Saudi Development and Reconstruction Program for Yemen (SDRPY) has signed an agreement with the Yemeni Ministry of Finance to deposit SAR1.3 billion in economic support … the agreement allocates funds to cover operational expenses and salaries". **SPA AR (N2525728):** "…اتفاقية مع وزارة المالية اليمنية، للبدء في إيداع الدعم الاقتصادي البالغ 1.3 مليار ريال سعودي … المُخصصة لتغطية النفقات التشغيلية والرواتب". The governed "to begin depositing" follows the Arabic original; the English original says "to deposit". |
| **Grade** | **VERIFIED_AGAINST_ORIGINAL** |

### YSC-020 — Current analytical rule — SYSTEM_INTERPRETATION
| Dimension | Finding |
|---|---|
| Identity | Unique; a synthesis rule with no factual claim. `source_ids` is empty by design. |
| EN/AR statement | Same meaning. The only post-AIR-001 change is the governed PB-0415.S119 wording edit to `system_implication_en`, so this one cell intentionally differs from the certified value. |
| **Grade** | Not applicable (no source to verify). Structure and parity: PASS. |

### YSC-021 — 4 June 2026 — COUNTRY_STRATEGY_AND_PORTFOLIO
| Dimension | Finding |
|---|---|
| Identity / class | Unique; strategy endorsement plus operation approvals. The class fits; the does-not-establish fields are correct. |
| EN/AR statement | Same meaning; FY2026–FY2030, 4 operations and US$285m in both. The Arabic `fact` adds the date inline. |
| Source binding | `SRC-WB-YEM-CPF-2026-2030-001` exists (FULL_PUBLIC_CARD). **Gap:** its locators are the CPF document and the CPF country page. The "four operations / US$285m / 4 June 2026" facts come from the **4 Jun 2026 press release**, which is not among the source's URLs. |
| Original check | **WB press release, 4 Jun 2026:** "The World Bank Group's Board of Executive Directors today endorsed a new Country Partnership Framework (CPF) for the Republic of Yemen for fiscal years 2026-2030, alongside four new operations totaling US$285 million" and "The four operations approved today…". **CPF page:** outcomes are nutrition, electricity access, and "agribusiness, mariculture, and fisheries"; cross-cutting themes are women's participation and private-sector growth. |
| **Grade** | **VERIFIED_AGAINST_ORIGINAL** |

### YSC-022 — 30 June 2026 — CASH_LIVELIHOODS_IDENTITY_PROJECT
| Dimension | Finding |
|---|---|
| Identity / class | Unique. The fact explicitly marks figures as design or target states. MEASUREMENT_CONTEXT fits. |
| EN/AR statement | Same meaning; US$100m, 1.8m, 55,000 (= "55 ألف") and 675,000 (= "675 ألف") match. The Arabic adds the date inline. |
| Source binding | `SRC-WB-YEM-CNL-2026-001` exists (FULL_PUBLIC_CARD) and is the right document. |
| Original check | **WB press release, 30 Jun 2026:** "The World Bank's Board of Executive Directors approved a US$100 million International Development Association (IDA) grant for the Cash for Nutrition and Livelihoods Project in Yemen"; "expected to reach 1.8 million people"; "Around 55,000 individuals … will join Village Savings and Loan Associations"; "support over 675,000 people in obtaining national identity cards and birth certificates". Implementation is by UNICEF with SFD (not in the fact, and no conflict). |
| **Grade** | **VERIFIED_AGAINST_ORIGINAL** |

### YSC-023 — 16 July 2026 — MACRO_REFORM_PROGRAMME_STAGE
| Dimension | Finding |
|---|---|
| Identity / class | Unique. The staff-level-agreement stage is correctly separated from Board approval, financing and outcomes. |
| EN/AR statement | Same meaning; 18 months in both. The Arabic adds the date inline. **Editorial:** "the mission statement says" / "بيان البعثة" refers to a press release (PR 26/249) quoting the mission. |
| Source binding | `SRC-IMF-YEM-SMP-2026` exists and is the right document. |
| Original check | **imf.org PR 26/249 (page rendered partially):** date "July 16, 2026"; "IMF staff and the Yemeni authorities have reached a staff-level agreement on the key economic policies and reforms"; "The proposed 18-month SMP…"; "This mission will not result in a Board discussion." The body text came from a verbatim republication (Mirage News): "This staff-level agreement is subject to approval by IMF Management."; "…priority on gradually rebuilding international reserves…"; "Strengthening financial sector intermediation, stability, and integrity is a central objective…"; "…phased plan to gradually increase cost recovery in the electricity sector…"; "Monetary policy implementation will be guided by clear quantitative anchors…". Governed `07/06 CLM-049` and `31 REF-IMF-001` agree. |
| **Grade** | **VERIFIED_AGAINST_ORIGINAL**. The Management-approval and priorities passages came from a verbatim republication, not the imf.org render. |

### Adjacent rows (context checks)
- **YSC-024** (not restored; only r17 implication fields were repaired): verified against the original. The WB G2Px event page (30 May 2024) says the programme "piloted digital payments in 8 districts … benefiting 45,460 recipients" with "payments into fully functional accounts along with recipient choice".
- **YSC-013**: single occurrence. 6,245 → 3,422.16 = −45.2% recomputes correctly.

---

## C. Findings for the Team Lead (none is a BLOCKER on the restoration itself)

| ID | Severity (proposed) | Object | Issue | Recommended action |
|---|---|---|---|---|
| P17-01 | MATERIAL | Audit lineage | The certified projection (`8d058126…`) that AIR-001 restored from is no longer retained, so per-field replay is impossible. | Recover the file from the entry ZIP and archive it under `audit/tranche_b_execution/archive/`, or record per-field expected values in the ledger. |
| P17-02 | MATERIAL | YSC-014 | Ratios are unverified against the original. They are in tension with the IMF FSI panel values cited in the project corpus (171.8→73.6; capital/assets 3.8% at Aug 2025). The unit is not stated. | Read CR 26/80 and confirm the figure or table, dates and perimeter behind 148/69/5/2.5; add the unit. Master first if anything changes. |
| P17-03 | MATERIAL | Sources | Duplicate source identity: `SRC-WB-FMIIP-ISR-2026-04` and `SRC-WB-FMIIP-ISR2-2026-001` point to one document. | Consolidate to one ID. Re-point YSC-018 and `DS-FMIIP-IMPLEMENTATION-2026`. |
| P17-04 | MATERIAL | YSC-019 | Semantic firewall: no field states that agreement ≠ deposit ≠ disbursement; the implication calls it a "fiscal flow". | Add an agreement-vs-deposit boundary to `does_not_establish_en/_ar`. |
| P17-05 | EDITORIAL | `16_DATASET_CATALOG` DS-V4R3-SYSTEM-CHRONOLOGY | Stale metadata: 20 rows, period_max 2026-03, 12 sources, origin `244_V4R3_…`. The actual values are 24 rows, through 2026-07-16, 18 distinct source IDs, in `14_SYSTEM_CHRONOLOGY`. | Refresh the catalog row. |
| P17-06 | EDITORIAL | Source metadata | `SRC-IMF-AIV-2025-STAFF-001` and `SRC-SPA-SAU-BUDGET-2026-001` are LOCATOR_ONLY with no title or publisher. The IMF record's `datasets_or_use` lists only DS-REMITTANCES, although 4 chronology events use it. The CPF record lacks the 4 Jun 2026 press-release URL. | Complete the metadata and add the locators. |
| P17-07 | EDITORIAL | YSC-015 | "Through the formal banking sector" may omit exchange companies. | Check the wording against CR 26/80. |
| P17-08 | EDITORIAL | YSC-018 / 023 / 019, 021, 022, 023 | Arabic FMIIP name inconsistent with the source card. "Mission statement" refers to a press release. The Arabic facts carry dates inline where the English does not. | Harmonise during the bilingual pass. |

---

## D. Overall assurance statement

**What was verified and how.**
- **Structure (all events):** 24 unique events, with no duplicate YSC-013 or YSC-024. The row mapping matches the AIR-001 ledger exactly, and Master equals projection field-for-field.
- **Ledger:** `cells_written=162` reproduces arithmetically from current values. The only later governed edit to the sheet is the logged PB-0415.S119 wording change to YSC-020.
- **Original sources:** YSC-018, 019, 021, 022 and 023 (and YSC-024) were checked against the original web documents with WebFetch and quoted above. No DISCREPANCY was found.
- **Cross-source only:** YSC-016 is consistent with independent governed CBY exchange-rate data.
- **Not reachable:** YSC-014, 015 and 017 rest on IMF Country Report 26/80, which returned 403 on every attempt. They are corroborated only by secondary reporting or the project's non-governed corpus. YSC-014 carries an unreconciled tension with another IMF panel.

**Residual risk.**
1. Per-field equality with the certified projection is attested by the Stage 0 script's self-check and indirect arithmetic, not by an independent replay. The certified file is gone.
2. Three IMF-sourced events remain unverified against the original, and YSC-014 needs a primary read.
3. One duplicated source identity (ISR seq. 2) and one semantic-firewall gap (YSC-019) should go through the Master-first route.

I did not verify any fact I could not fetch, and I have not claimed so.
