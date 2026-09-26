# S06.1 — World Bank / Findex + Firms Source-Owner Challenge — CLOSED

**Date:** 2026-09-23  
**Decision:** CLOSED / PASS  
**Next:** S06.2 — CBY source-owner challenge (NOT STARTED)  
**Authority:** Production Master remains sole semantic/evidence/source/rights/publication authority.

## Scope and original-source checks

S06.1 challenged the admitted People/Findex and Firms evidence directly against World Bank original-source surfaces:

- Yemen Global Findex 2021 microdata/DDI: https://microdata.worldbank.org/catalog/5862
- World Bank indicator surface for Yemen account ownership: https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE
- World Bank female/male subgroup indicator surfaces.
- Yemen Financial Sector Diagnostics (P177631), including Annex III: https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf

## Dispositions

| Finding | Disposition | Decision |
|---|---|---|
| Findex wave vs fieldwork date | NO CHANGE REQUIRED | World Bank labels the study Global Findex 2021 while Yemen fieldwork ran 2022-11-07 to 2023-01-09. Current public wording preserves both facts and does not relabel the estimate as a 2026 rate. |
| Adult universe / survey coverage | NO CHANGE REQUIRED | Source confirms adult 15+ design, n=1,000, excluded geography representing about 23% of population, and replacement of over one-fourth of PSUs. Current public limitations preserve these boundaries. |
| 11.9% account-ownership anchor | NO CHANGE REQUIRED | Current Master treats the World Bank public aggregate as the weighted population estimate and keeps raw microdata case shares separate. |
| Female 5.44% / male 18.35% / 12.91 pp gap | NO CHANGE REQUIRED | Same-wave subgroup comparison remains bounded to the World Bank aggregate universe. No causal/current-2026 interpretation is permitted. Source precision is retained; no unsupported statistical-significance claim is added. |
| Raw 199 account cases and 153 conditional account-use cases | REJECTED AS POPULATION ESTIMATE | World Bank variable pages explicitly warn raw case percentages are not population summary statistics. The 153 cases are a conditional routing base for account-use questions, not a denominator for the 11.9% weighted population estimate. |
| Legacy Findex pseudo-codebook block in Master | MASTER-INTEGRATED | `24_FINDEX_CODEBOOK!A121` now explicitly quarantines rows 122 onward as unverified research/lineage only. The verified source-extracted DDI architecture in rows 4–117 remains the production reference. No public number or claim changed. |
| Mobile-money module inference | REJECTED AS PRODUCTION CLAIM FROM LEGACY BLOCK | Yemen's public data dictionary lists mobile-money-use variables, but the legacy block invented an `account_mob` construct/wording not present as a Yemen variable in the verified source-extracted architecture. Variable presence alone is not evidence of an observed Yemen mobile-money ownership rate. |
| Firms sample/universe | NO CHANGE REQUIRED | Annex III confirms September 2022 collection, 328 formal and 217 informal enterprises, and seven selected governorates. Current formal-firm evidence remains explicitly non-national. |
| Formal firms with bank account | NO CHANGE REQUIRED | Source reports 191/328 formal establishments (58.2%) with checking/savings bank accounts. |
| Line of credit | NO CHANGE REQUIRED | Source reports 31/328 formal establishments with a line of credit; this is not a national MSME prevalence estimate. |
| Source of loan denominator | NO CHANGE REQUIRED | Table 6 reports 18 valid responses across lender categories. Current Master preserves the conditional denominator rather than treating 18 as the full sample. |
| Business challenges | NO CHANGE REQUIRED | Source reports electricity 50%, fuel shortages 46%, access to finance 22% in the listed challenge table. Current public claim correctly says finance was not the most frequently cited constraint and does not nationalize the ranking. |
| OECD/INFE candidate in archive queue | DEFERRED WITH NAMED OWNER | Not a World Bank/Findex/Firms source-owner object. Retained for a later explicit source-family admission decision; it is not promoted by S06.1. |

## What became more true

The canonical Master now distinguishes the verified World Bank DDI-derived Findex architecture from a legacy pseudo-codebook block that contained unsupported derivation and mobile-money wording. This removes an internal ambiguity without changing the accepted public People/Firms evidence.

## What became simpler

There is one clear Findex production path: World Bank public aggregates + verified Yemen DDI metadata + controlled evidence/passports. Legacy pseudo-codebook prose cannot be mistaken for source-owner truth.

## Verification

- Production Master SHA-256: `ee001adede94642ba001f3ffd9c4dbdb7b8ca30050bb9cc478636fbf71a79ba4`
- Controlled Page Specs SHA-256: `28c247c4d55be0bb0b69aa854d3fdb0caa68f16e23657452afb5e5e1b1dac02b`
- Presentation Contract SHA-256: `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266` (unchanged)
- Controlled Page Specs: 141
- Page Specs JSON parse: PASS
- Master-hash binding occurrences updated: 142
- Public numbers/claims changed: NONE
- R-042 release-security blocker: OPEN / unchanged
- S07/S08: NOT EXECUTED

**Boundary decision:** S06.1 CLOSED / PASS. S06.2 is next and has not started.
