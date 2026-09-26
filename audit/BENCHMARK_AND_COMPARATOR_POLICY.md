# Benchmark and comparator policy

> **Execution-state correction (Tranche B execution, 2026-09-26).** Acceptance correction A: the OECD/INFE 2023 Yemen values are verified and published with their survey scope; the comparator rule (no ranking, no gap to an average) is unchanged.


**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

## 1. Rule

Benchmark and comparator material may improve **method, measurement design or interpretation**. It is **never Yemen evidence**. It never fills a Yemen gap, and it never becomes a league table, a rank or an unsupported performance judgement.

Every comparator shown publicly carries the tag **"BENCHMARK / METHOD REFERENCE — NOT YEMEN EVIDENCE"**, or «مرجع منهجي أو مقارن — ليس دليلًا يمنيًا».

## 2. Three permitted comparator types

| Type | What it may do | What it may not do | Example in this product |
|---|---|---|---|
| **MEASUREMENT EXEMPLAR** | Show how a concept is defined or measured well (instrument, definition, indicator design) | Supply a value for Yemen | OECD/INFE 2023 instrument (SRC-OECD-INFE-2023); Global Findex 2025 methodology (SRC-WB-FINDEX-2025-EDITION, whose card already states that it "does not create a newer Yemen population estimate"); BIS-CPMI FPS/RTGS and PAFI guidance; CGAP Arab measurement (2017) |
| **STRUCTURAL COMPARATOR** | Explain a mechanism or institutional design (e.g. how G2P digitisation is sequenced) | Imply that Yemen follows the same path or will get the same result | World Bank G2Px (SRC-WB-G2PX-001), used with the Yemen pilot card SRC-WB-G2PX-YEM-UCT-2024-001, which is Yemen evidence in its own right |
| **STATISTICAL COMPARATOR** | Place a *verified* Yemen value beside a *published* cross-country figure from the same instrument and round, with both labelled | Rank Yemen, compute a gap to an average for effect, or compare across instruments | **None published today.** The Yemen row is now verified from the OECD/INFE 2023 report (overall financial literacy 42 out of 100, Figure 2.1; financial well-being 15 out of 100, Figure 4.1; sample 1,000; fieldwork 11 March–1 April 2023; acceptance correction A) and is published survey-scoped on /people/ and /reforms/. The cross-country averages (well-being 42/47, literacy 60/63) are **not** set beside it: no ranking and no gap to an average is published. **Comparator row withheld.** |

## 3. Decisions on the Master's own comparator material

| Master object | Decision | Patch |
|---|---|---|
| 30_FCS_CONTEXT (FCS peer matrix: account, mobile-money and other rates for peer countries) | **Removed from the Master into audit lineage.** It is a league-table-shaped object with unverified values and no public use. | PB-0221 |
| 29_OECD_BENCHMARKS Annex D table (rows 5–30, "Global Average 60.5") | **NON-PUBLIC** (provenance defect: the report's average is 60) | PB-0109 |
| 29 "Verified Yemen facts" (rows 35–51) | Per-row `verification_state`; only CONFIRMED rows may feed copy | PB-0108 |
| 28 OECD/INFE item prompts (rows 43–68, "Verbatim") | Relabelled as reconstructed and NON-PUBLIC | PB-0110 |
| 25_FINDEX_BASELINE rows 14–35 ("Attached analytical inputs — not verified") | Removed from the Master into audit lineage | PB-0220 |

## 4. Addendum §2 benchmark list

The list: WB/G20, Findex 2025, PAFI, G2Px, ID4D, CGAP 2026, FinNeeds/AFI, FinAccess Kenya, UNCDF IDES, UNHCR, Data360.

**Admitted today as method references only:**
- Findex 2025 (methodology);
- PAFI (BIS-CPMI);
- G2Px;
- CGAP (Arab measurement, 2017).

**Not admitted in this window:**
- ID4D, FinNeeds/AFI, FinAccess Kenya, UNCDF IDES, UNHCR, Data360, CGAP 2026, WB/G20.

These were not retrieved. The directive limits retrieval to named material uncertainties, and none of them closes one. Each may be admitted later as a **MEASUREMENT EXEMPLAR** if it improves a specific measurement priority, for example:
- FinAccess or FinNeeds instruments for MA-001;
- ID4D for MA-007;
- UNHCR for displacement disaggregation under MA-003.

**Conditions for admission:**
- the source card gives publisher, title, date, version, URL, retrieval date, role and does-not-establish;
- the card is tagged as not Yemen evidence.

## 5. Forbidden uses

- League tables, "Yemen ranks Nth", "below the regional average" statements, or colour-coded peer maps.
- A composite score assembled from benchmark dimensions.
- Global or regional averages substituted for a missing Yemen value, including "for context" on a Yemen chart axis.
- A comparator from a different instrument, round or definition set beside a Yemen value.
