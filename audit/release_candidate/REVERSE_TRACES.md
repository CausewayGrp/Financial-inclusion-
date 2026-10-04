# Six reverse traces — public object → record → source → locator (3 October 2026)

Owner Addendum 2 asks for six reverse traces before B16, and for any break to be fixed Master-first. Each starts from
what a reader sees, finds the governed record that carries it, then the record's sources in the source library, then
each source's public original locator, which was requested on 3 October 2026. Whether each value matches its original
is the separate check of `ORIGINAL_SOURCE_VERIFICATION.md`. Here the question is whether the chain holds without a gap.

**Result: six of six unbroken.** No record is missing, and no drawn value cites a source outside the library. Every
named source has a public locator, and every locator resolves except one: the UNDP project page, which refuses
automated requests (HTTP 403 from its CDN). That is not a broken link; a person checks it with a browser at release
(`LINK_CHECK.md`). Nothing needed fixing.

## 1. Home headline claims

Public object: /en/ and /ar/ headline claims CLM-001, CLM-002, CLM-003. Record(s): `CLM-001`, `CLM-002`, `CLM-003`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-WB-FINDEX-AGG-2022` | https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE | 200 | OK |
| `SRC-WB-FINDEX-2025-EDITION` | https://www.worldbank.org/en/publication/globalfindex/download-data | 200 | OK |
| `SRC-CBY-POS-2025-03` | https://cby-ye.com/files/6812a1758f5a5.pdf | 200 | OK |
| `SRC-CBY-POS-2025-12` | https://www.cby-ye.com/files/69b058981b681.pdf | 200 | OK |
| `SRC-CBY-POS-2026-01` | https://www.cby-ye.com/files/69b058d4bc306.pdf | 200 | OK |
| `SRC-CBY-POS-2026-04` | https://cby-ye.com/files/6a6f968423908.pdf | 200 | OK |
| `SRC-CBY-POS-2026-05` | https://cby-ye.com/files/6a6f96ed5c009.pdf | 200 | OK |
| `SRC-CBY-POS-2026-06` | https://cby-ye.com/files/6a6f973c98c25.pdf | 200 | OK |

## 2. VIS-FINDEX-GAPS

Public object: 9 drawn values (WB-FINDEX-OBS-2022-001, WB-FINDEX-OBS-2022-002, WB-FINDEX-OBS-2022-003, WB-FINDEX-OBS-2022-004, WB-FINDEX-OBS-2022-005, WB-FINDEX-OBS-2022-006…). Record(s): `VIS-FINDEX-GAPS`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-WB-FINDEX-AGG-2022` | https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE | 200 | OK |

## 3. VIS-POS-VALUE

Public object: 15 drawn values (OBS-00053, OBS-00056, OBS-00059, OBS-00062, OBS-00065, OBS-00068…). Record(s): `VIS-POS-VALUE`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-CBY-POS-2025-03` | https://cby-ye.com/files/6812a1758f5a5.pdf | 200 | OK |
| `SRC-CBY-POS-2025-04` | https://www.cby-ye.com/files/690b4cbc99847.pdf | 200 | OK |
| `SRC-CBY-POS-2025-05` | https://www.cby-ye.com/files/690b4ce84d19b.pdf | 200 | OK |
| `SRC-CBY-POS-2025-06` | https://www.cby-ye.com/files/690b4d09cc314.pdf | 200 | OK |
| `SRC-CBY-POS-2025-07` | https://www.cby-ye.com/files/693a7785421c0.pdf | 200 | OK |
| `SRC-CBY-POS-2025-08` | https://www.cby-ye.com/files/693a77a6c52c3.pdf | 200 | OK |
| `SRC-CBY-POS-2025-10` | https://www.cby-ye.com/files/693a7803952d7.pdf | 200 | OK |
| `SRC-CBY-POS-2025-11` | https://www.cby-ye.com/files/69b05862c40b6.pdf | 200 | OK |
| `SRC-CBY-POS-2025-12` | https://www.cby-ye.com/files/69b058981b681.pdf | 200 | OK |
| `SRC-CBY-POS-2026-01` | https://www.cby-ye.com/files/69b058d4bc306.pdf | 200 | OK |
| `SRC-CBY-POS-2026-02` | https://cby-ye.com/files/6a6f958d49cc2.pdf | 200 | OK |
| `SRC-CBY-POS-2026-03` | https://cby-ye.com/files/6a6f960871730.pdf | 200 | OK |
| `SRC-CBY-POS-2026-04` | https://cby-ye.com/files/6a6f968423908.pdf | 200 | OK |
| `SRC-CBY-POS-2026-05` | https://cby-ye.com/files/6a6f96ed5c009.pdf | 200 | OK |
| `SRC-CBY-POS-2026-06` | https://cby-ye.com/files/6a6f973c98c25.pdf | 200 | OK |

## 4. RV-CWR-001

Public object: 10 drawn values (RMO-CBY-2021-AR2025, RMO-CBY-2022-AR2025, RMO-CBY-2023-AR2025, RMO-CBY-2024-AR2024, RMO-CBY-2024-AR2025, RMO-IMF-2021-HIST…). Record(s): `RV-CWR-001`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-CBY-AR2024-BOP` | https://english.cby-ye.com/files/68c2ef16b4225.pdf | 200 | OK |
| `SRC-CBY-AR2025-BOP` | https://english.cby-ye.com/files/6a54b8fcd8b68.pdf | 200 | OK |
| `SRC-IMF-AIV-2025-STAFF-001` | https://www.elibrary.imf.org/view/journals/002/2026/080/article-A001-en.xml | 200 | OK |

## 5. The /reforms/ chain (VIS-PAYMENT-RAILS)

Public object: the chain figure on /reforms/. Record(s): `VIS-PAYMENT-RAILS`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-UNDP-FMIIP-001` | https://www.undp.org/yemen/projects/yemen-financial-market-infrastructure-and-inclusion-project | 403 | NOT VERIFIABLE (publisher refuses automated requests) |
| `SRC-WB-FMIIP-P180708` | https://maps.worldbank.org/projects/wb/pid/P180708?status=active | 200 | OK |
| `SRC-WB-FMIIP-ISR2-2026-001` | https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099040826144025755 | 200 | OK |
| `SRC-CBY-EMONEY-AMD-2025-001` | https://cby-ye.com/files/6875fc55a253e.pdf | 200 | OK |
| `SRC-CBY-DIGITAL-EXPO-2026-001` | https://cby-ye.com/news/915 | 200 | OK |
| `SRC-CBY-PAY-BOARD-2026-001` | https://cby-ye.com/news/922 | 200 | OK |
| `SRC-CBY-BANK-NETWORK-MTG-2026-001` | https://cby-ye.com/news/946 | 200 | OK |
| `SRC-CBY-UNIFIED-NET-2026-001` | https://cby-ye.com/news/957 | 200 | OK |
| `SRC-CBY-YPCC-FOUND-2026-001` | https://cby-ye.com/news/961 | 200 | OK |
| `SRC-CBY-YPCC-BOARD-2026-001` | https://cby-ye.com/news/962 | 200 | OK |
| `SRC-CBY-DEC-23-2024-001` | https://cby-ye.com/files/667c596ef3bea.pdf | 200 | OK |

## 6. IMF-attributed chronology event YSC-014

Public object: 2022–April 2025: According to the IMF staff report, which focuses on areas under the internationally recogn…. Record(s): `YSC-014`.

| Source | Locator | HTTP | Link |
|---|---|---|---|
| `SRC-IMF-AIV-2025-STAFF-001` | https://www.elibrary.imf.org/view/journals/002/2026/080/article-A001-en.xml | 200 | OK |
