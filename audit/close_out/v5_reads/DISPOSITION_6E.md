# CLOSE-6E review pair — disposition (11 October 2026)

Two challenger lenses reviewed the staged CLOSE-6E texts before the transaction ran on the Master: the domain lens (MSME
finance for 6C-1; humanitarian cash / FCV for 6C-2; remittance-price statistician for 6C-3; central-bank regulator / legal
librarian for 6C-4; MSME and microfinance for 6C-5) and the Arabic-editor lens. Their reports are REDTEAM_6E.md and
ARABIC_6E.md beside this file; the reads behind the texts are V3, V4, V5 and V7 (V7 records the Doing Business
discontinuation statement and the corridor-page refusal, read during the review). Packets were drawn from the staged Master.

## Domain lens (first pass)

| ID | Finding | Disposition |
|---|---|---|
| B1 | Pressure's cash-out statements concern MPCA, not the UCT | Applied in CLM-045, CWR-010 s6, MA-005, MA-009 |
| B2 | US rows labelled as published averages | Applied: CAUSEWAY_SIMPLE_MEAN_OF_SOURCE_QUOTES; DERIVED_FROM_PRIMARY_OFFICIAL_CORRIDOR_QUOTES; universe "in the dataset" |
| S1 | SAM does not place its sub-districts under the IRG | Does not reproduce: SAM p.1, "both under the control of the Internationally Recognized Government" (addendum/R5_ccy_isp_sam.md) |
| S2 | "early use" overstated | Applied: "a common use"; the 47% / 30% split (SAM printed p.14) |
| S3 | "published November 2024" rests on the host path | Applied: "posted online by its host in November 2024"; evidence period gives the survey month. A challenge to the instruction's "Cite SAM by publication date (November 2024)": the report prints no date |
| S4 | MA-009 lost "announced reach" | Applied |
| S5 | the report frames IRG areas; problems eased | Applied |
| S6 | "shop or supplier credit" conflates two measures | Applied: "shop credit to households" |
| S7 | informal sample design and skew | Applied: market-area listing, first owner who agreed; 179 of 217 in areas under the de facto authorities |
| S8 | "the last independent measure"; discontinuation unrecorded | Applied: "the most recent published measure this resource holds"; V7 records the statement |
| S9 | people ≠ firms in registry coverage | Applied: 211,476 individuals and 4,769 firms; 1.3% as the profile expresses it |
| S10 | fact_ar "rests on" for "cites" | Applied (Arabic and English) |
| S11 | "adds a platform" contradicts "does not link"; list keeper | Applied |
| S12 | IFAD estimates, 48,000 households, Islamic precepts | Applied |
| S13 | US product mix; "computed here" on the Reading | Applied (/remittances/ s5 and CWR-012 s6) |
| S14 | RPW workbook "Restricted Data" | Recorded: rights NOT_ASSESSED; values cited, the file not hosted; the release rights check (REL-02) covers it |
| N1–N7 | 960 "SMEs and BAs"; business owners; the two branches; "an evaluation by IFAD's Independent Office of Evaluation"; meta "in completed projects"; REF-REG-012 two rules; "no systematic current evidence" | Applied. MA-004 keeps "before the conflict" (the instruction's own does_not_establish wording, test 4) |

## Domain lens (confirmation pass on the revised texts)

All first-pass findings RESOLVED (S1 rightly not applied; S14 recorded). New: S-1 the debt studies concern the Consortium
partners' humanitarian cash, separate from the UCT — applied; S-2 the 47% / 30% split concerns households that had received
a transfer — applied; N-1 method_en self-contradiction, N-2 "problems eased" scoped to MPCA liquidity, N-3 "two of the
branches IFAD helped the CACB build", N-4 MA-009 names the programme, N-5 MA-005 the report's MPCA section, N-6 the encoding
contract's "provider and quote counts are not held" (now false) — all applied, the contract's "missing" note with it.
Tests 4 and 5: PASS. **VERDICT: ACCEPT after S-1 and S-2 (applied).**

Strongest remaining misreadings, recorded: P3 the US 3.92% read as a World Bank-published average where only the summary or
chart is seen (the summary says "the three corridors … it surveyed"; method, limitations and page sections say "computed
here"); P5 the meta's "credit reached 3,723 clients" read as audited (the record says estimates).

## Arabic lens

B1, B2, SF-1 to SF-7 applied; N-1, N-3 to N-8, N-10 and N-11 applied; N-2 met by the confirmation-pass change; N-9 kept (the
field's own «ص 143» style). **VERDICT: PASS after B1 and B2 (applied).**

## Departures from the instruction's draft wording (each a challenge recorded for the report)

1. 6C-1(a): Figure 116 is "Main Sources of Financing for the Business" (base 217), not sources of debt; formal firms' 1.31%
   carries no "among 328 firms" (Figure 110 prints no base).
2. 6C-2(a): 1.43 million is the cycle's announced reach, not confirmed payments; the planned US$62.5 million is not used.
3. 6C-2(b): no "Eid al-Adha 2026" (no year in the source); "denominations", not "notes"; MPCA, not the UCT.
4. 6C-2(c): the studies' own sub-districts, not "areas administered from Aden"; SAM's date is its host's posting.
5. 6C-2(e): MA-001 cites SAM only; no shop or supplier credit statement was found in Pressure.
6. 6C-3: the US averages are computed from the quote-level dataset and labelled so (the corridor page refuses automated
   requests).
7. 6C-4(b): MA-008 binds no Evidence Record and v5 allows no new route for one; the Doing Business figures sit on the
   registry's chronology event YSC-030 (shown on /finance/), and MA-008 points to it without figures. "The last independent
   measure" became "the most recent published measure this resource holds".
8. 6C-4(c): FATF RESERVED — fatf-gafi.org returned a Cloudflare challenge (HTTP 403); recorded in W3f in PR-6.
9. 6C-6: the owner's aggregate file has not arrived — FRONTIER card EXT-40.
