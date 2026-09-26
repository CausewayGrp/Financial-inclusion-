# Final currentness cut-off — Tranche C

**Cut-off:** 26 September 2026 (content version "26 September 2026", Master 04 `UI-CONTENT-VERSION`).
**Authority after Tranche C:** Production Master SHA-256 `f0150122895d88169e9c9ec947633deda04a02c710a28d7b0de2972214547224`.

## Rule

The gate was bounded: only candidates that could change a public claim, a status, a library entry or a measurement priority were checked, against the publisher's own page. Each candidate has exactly one disposition:

| Disposition | Meaning |
|---|---|
| PUBLIC CLAIM CHANGE | A public claim, figure or date changes in the Master (Master first, then regeneration) |
| STATUS EVENT | A dated event is added to or confirmed on a provider/regulatory status history; no claim changes |
| LIBRARY/CONTEXT ONLY | The source enters or updates the library as context; no public figure depends on it |
| MEASUREMENT IMPLICATION | The finding changes a Measurement Agenda priority, not a claim |
| NO CHANGE | Checked; nothing newer that changes the product |

A check records what the publisher's page showed on the check date. It does not assert that nothing newer exists elsewhere.

## Dispositions

| Candidate | What was checked | Finding at cut-off | Disposition | Where |
|---|---|---|---|---|
| CBY-Aden governor's decisions (licence suspension, withdrawal, closure) | CBY-Aden decisions listing, 26 Sep 2026 | Decision No. 18 of 2026 is the latest; none numbered 19 or higher found | STATUS EVENT | CLM-019 binds the 2026 decisions; roster/decision dating stated on /providers/ and /access/ (TC-H) |
| CBY-Aden monthly POS releases | CBY-Aden payments page, 26 Sep 2026 | January 2026 is the latest monthly release; from July 2025 releases are one-page infographics | NO CHANGE (form change disclosed) | CLM-017; VIS-POS-* limitations (TC-G, PAY-11) |
| IMF Staff-Monitored Program | IMF press material | Staff-level agreement announced 16 July 2026, subject to IMF Management approval; no approval notice found (limited check) | NO CHANGE | /reforms/ §7; Reading "reforms newer than people evidence" §3 |
| World Bank FMIIP (P180708) Implementation Status Report | World Bank project page | ISR No. 2 of 8 April 2026 is the latest found | NO CHANGE | XW-FMIIP-*, chronology YSC-018 |
| World Bank Remittance Prices Worldwide | RPW corridor pages | 2025 Q3 remains the latest Yemen corridor quarter held | NO CHANGE | VIS-REMITTANCE-COST |
| Global Findex — Yemen | Findex 2025 edition | No Yemen wave newer than the 2021 wave (fieldwork 7 Nov 2022 – 9 Jan 2023) | NO CHANGE | CLM-001/002, /people/ |
| Global Findex — FCS comparators (Somalia, Yemen group, other low-income) | Findex 2025 edition aggregates | Comparator values ingested with their own universes | PUBLIC CLAIM CHANGE | TC-A records (comparators kept separate from Yemen values) |
| CBY-Aden Annual Report 2025 — value for reference year 2025 | AR2025 BOP table | 3,614.05 (US$ million) held as context; no public claim built on it | LIBRARY/CONTEXT ONLY | 15_SOURCE_LIBRARY |
| Financial Consumer Protection Regulatory Instructions | CBY-Aden announcement | Announced 28 August 2023; the legal text is not extracted here | PUBLIC CLAIM CHANGE | DS-FCP-ARCH; /reforms/ §3 and §11 (EN in TC-C; AR aligned in TC-H) |
| CBY-Aden list of licensed banks | CBY-Aden list page | 26 banks, checked 7 September 2026; the list states no issue date | Copy fix (dated check, no "current list") | CLM-008/055; /providers/, /finance/, /access/ (TC-C EN, TC-H AR) |
| CBY-Aden payments page recheck (PAYCUR) | CBY-Aden payments page | Rechecked 26 September 2026; no newer monthly release | NO CHANGE | CLM-017 currentness |

## Measurement implications

None of the candidates changes a Measurement Agenda priority. The frontiers they confirm (no newer population measure; POS form change; unreconciled roster/decision dating) are already carried by the existing priorities.

## What this cut-off does not establish

- It is not a continuous monitoring service. After 26 September 2026 the product states only what it held on that date.
- A "no newer item found" result is limited to the publisher pages named above.
- Reading prose will be revised by the independent Reading package; any currentness statement inside a Reading is re-checked against this cut-off when that package is applied.
