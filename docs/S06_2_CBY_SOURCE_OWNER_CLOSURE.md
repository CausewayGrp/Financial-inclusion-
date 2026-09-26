# S06.2 — CBY Payments / Providers / Reforms Source-Owner Challenge — CLOSED

**Date:** 2026-09-23  
**Decision:** CLOSED / PASS  
**Next:** S06.3 — IMF / remittances / microfinance / programme / humanitarian source-owner challenge (NOT STARTED)  
**Authority:** Production Master remains the sole semantic/evidence/source/rights/publication authority.

## Scope and original-source checks

S06.2 challenged the admitted payments, providers and reforms evidence against current original Central Bank of Yemen — Aden source-owner surfaces. The review was bounded to source authority, date, measurement object, institutional applicability, publication state and currentness. It did not treat an administrative record as evidence of people-level adoption or outcome.

Original-source surfaces rechecked include:

- CBY monthly payment-system reports: `https://english.cby-ye.com/pages/27`
- CBY Banking Supervision page and current licensed-provider/instruction links: `https://cby-ye.com/pages/14`
- Unified domestic transfers decision of 26 June 2024: `https://cby-ye.com/files/667c596ef3bea.pdf`
- Board decisions on national QR, e-wallet interoperability and fast-payment infrastructure, 29 March 2026: `https://cby-ye.com/news/922`
- Electronic-money regulation amendment, Decision No. 4 of 2025: `https://cby-ye.com/files/6875fc55a253e.pdf`
- Decision No. 17 of 17 September 2026 concerning Al-Buraq Exchange and Transfers Company: `https://cby-ye.com/news/973`

## Dispositions

| Finding | Disposition | Decision |
|---|---|---|
| Monthly POS currentness | NO CHANGE REQUIRED | The official monthly-report index still runs through January 2026. The controlled March 2025 → January 2026 POS series therefore remains bounded to the latest admitted monthly observation and is not extrapolated. |
| POS terminals / transactions / subscribers / cards | NO CHANGE REQUIRED | They remain distinct administrative/system objects. A terminal is not a merchant; a transaction is not a person; a subscriber is not necessarily an active user; cards/accounts are not unique people. Administrative growth is not national inclusion prevalence. |
| Missing September 2025 monthly transaction value | NO CHANGE REQUIRED | The controlled missing observation remains missing. It is not imputed, interpolated, treated as zero or smoothed into a continuous value series. |
| Licensed-bank roster | NO CHANGE REQUIRED | The current controlled roster remains a source-listed licensed-bank universe. Listing/licensing does not establish current operation, branch presence, activity or customer use. |
| 2026 exchange/remittance roster categories | NO CHANGE REQUIRED | The 98 companies, 225 individual exchange establishments and 106 remittance agents remain separate source-defined categories. They are not summed into a deduplicated operating-provider universe and are not read as current operation. |
| Unified domestic transfer network | NO CHANGE REQUIRED | The 26 June 2024 decision is correctly treated as a regulation/rule in force with source-specific exceptions and transition provisions. It does not by itself prove implementation quality, adoption, reach or inclusion outcomes. |
| QR / e-wallet interoperability / fast-payment decisions | NO CHANGE REQUIRED | March 2026 board decisions and related implementation activity establish institutional decisions/steps, not consumer adoption, active use, quality or outcomes. |
| Electronic-money amendment | NO CHANGE REQUIRED | Decision No. 4 of 2025 is regulatory evidence. It does not establish provider operation, market take-up or people-level use. |
| Financial-consumer-protection instructions | NO CHANGE REQUIRED | The controlled 10-day provider-resolution and 14-day CBY-escalation rule remains a regulatory requirement; implementation/effectiveness remain separate evidence questions. |
| Al-Buraq licence suspension / premises closure, Decision No. 17 of 2026 | MASTER-INTEGRATED | A new official currentness event was missing from the canonical provider-status overlay. The Master now carries a dated entity/status event linked to `SRC-CBY-ENF-17-2026`, while explicitly forbidding inference about the full provider universe, other entities or any later status. The event is not mechanically subtracted from the annual roster. |
| CBY exchange-rate construction candidate from predecessor research | DEFERRED — INSUFFICIENT ORIGINAL-SOURCE BASIS | S06.2 did not recover an original methodological source sufficient to establish the exact aggregation/construction claimed by predecessor material. No production wording is widened or silently repaired. |
| Banking-series coverage-change candidate from predecessor research | DEFERRED — INSUFFICIENT ORIGINAL-SOURCE BASIS | The active public products already preserve vintage/valuation/coverage boundaries. No specific original-source coverage break was established here strongly enough to alter a controlled public object. |

## Master-first correction

The canonical Production Master was corrected first. The change adds only the missing dated provider-status event and its source/dependency records:

- `22_PROVIDERS_DATA`: Al-Buraq Exchange and Transfers Company entity/status overlay and `PSE-014`, dated 2026-09-17.
- `15_SOURCE_LIBRARY`: `SRC-CBY-ENF-17-2026`, original locator `https://cby-ye.com/news/973`, publication state `LOCATOR_ONLY`.
- `16_DATASET_CATALOG`: provider-master and provider-status-event coverage/count metadata advanced to include the new source/status event.
- `00_MASTER` and `37_READINESS_CHECKLIST`: controlled source count advanced from 149 to 150.

The following remain unchanged: the 26-bank roster count; the 98 / 225 / 106 source-defined exchange/remittance categories; all public payments values; source-native provider categories; and every prohibition that prevents licence/listing from being treated as operation.

## Derived projection regeneration

After the Master correction, the controlled projections were regenerated in place. The new source is present only where the existing provider-enforcement source family already applies. It is `LOCATOR_ONLY`; no bibliographic or redistribution permission was invented.

Current controlled counts after regeneration:

- Controlled Page Specs: **141**
- Generated HTML target: **284**
- Controlled source-reference records: **150**
- Publicly addressable source records: **149**
- Display-ready source cards: **6**
- Locator-only public records: **143**
- No-public-locator dependencies: **1**
- Public search records: **418**

## What became more true

The provider-status layer now reflects a current, official 17 September 2026 CBY enforcement event without pretending that one status event defines the complete current operating-provider universe.

## What became more complex

The provider record now contains one additional dated status overlay. That complexity is necessary because an annual roster and a later enforcement event answer different questions and must coexist rather than be silently reconciled.

## What can now be removed

Any downstream assumption that the pre-17-September provider-status overlay is current can be removed. No provider count, market-share inference, current-operation claim or synthetic deduplicated total should be added in its place.

## Verification anchors

- Production Master SHA-256: `cfe4599e26026f9ca377b9ac4b9b1120781678b981e09bb0f439091483a37dfe`
- Controlled Page Specs SHA-256: `5b5601c043a4857314a4f483db3bf8d8f39a07a838cbac8500324e7f463ba708`
- Presentation Contract SHA-256: `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266` (unchanged)
- R-042 release-security blocker: OPEN / unchanged
- S07/S08: NOT EXECUTED

**Boundary decision:** S06.2 CLOSED / PASS. S06.3 is next and has not started.
