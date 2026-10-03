# B13d — Link check of every public original locator, 3 October 2026

Part B item B13 d. Every source in the Master's source library that exposes a public original locator (156 of 165) was
requested from this environment on 3 October 2026 (curl, a browser user agent, redirects followed; a range-refusing host
re-requested whole; a 403 compared against the response headers and, where possible, the web.archive.org availability
API). A locator that no longer resolves was replaced only by the publisher's current address for the same document,
read and matched against the values the Master cites from it, or else by the web.archive.org copy of the original
address, and the site says the link is an archived copy (`UI-EVID-OPEN-ARCHIVED-COPY`). Changes are Master-first:
transaction `audit/release_candidate/rc_12_b12_b13.py` (RC-12). Downloads from web.archive.org itself are refused by
this environment's egress policy, so an archived copy is the snapshot of the exact original address, not a file read
here; that is said wherever it applies.

## Counts by outcome

| Outcome | Locators |
|---|---|
| OK | 129 |
| NOT VERIFIABLE HERE — publisher refuses automated requests | 14 |
| MOVED — publisher's current address, same document | 5 |
| BROKEN — archived copy | 4 |
| HOST UNAVAILABLE | 1 |
| BROKEN — unresolved | 1 |
| NOT VERIFIABLE HERE — TLS | 1 |
| SIGN-IN REQUIRED | 1 |
| **Total** | **156** |

## Every check

| Source | Host | Outcome | Detail |
|---|---|---|---|
| `SRC-ACAPS-YEM-REMIT-2021` | www.acaps.org | OK | HTTP 206 |
| `SRC-AIDDATA-SAUDI-YEM-2015` | www.aiddata.org | OK | HTTP 200 |
| `SRC-AJMBFS-CBY-FI-2025-001` | ojs.aambfsye.org | OK | HTTP 200 |
| `SRC-AMB-MFB-SUPERVISION-2026` | www.findevgateway.org | OK | HTTP 200 |
| `SRC-BIS-CPMI-FPS-RTGS-2021-001` | www.bis.org | OK | HTTP 206 |
| `SRC-BIS-CPMI-PAFI-FINTECH-2020-001` | www.bis.org | OK | HTTP 206 |
| `SRC-CBY-001` | english.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-AR2022-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-AR2023-001` | www.english.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-AR2024-BOP` | english.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-AR2025-BOP` | english.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-BANK-NETWORK-MTG-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-BANKLIST-AR-2026-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-DEC-23-2024-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-DIGITAL-EXPO-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-EMONEY-2023-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-EMONEY-AMD-2025-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-ENF-01-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-02-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-03-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-04-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-05-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-06-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-09-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-10-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-11-2026` | www.cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-13-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-14-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-15-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-17-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-ENF-18-2026` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-EXCH-LIST-2025-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-EXCH-LIST-2026-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-FCP-AWARE-2024-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-FCP-BROCHURE-2024-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-FCP-INSTR-2023-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-FMIIP-WORKSHOP-2025` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-GMW-2023-001` | www.cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-GMW-2024-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-GMW-2024-CLOSE-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-GMW-2025-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-HIST-METHOD-001` | english.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-PAY-BOARD-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-PAYREPORT-H1-2025` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-PAYREPORT-Q3-2024` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-03` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-04` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-05` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-06` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-07` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-08` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-09` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-10` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-11` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2025-12` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-01` | www.cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-02` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-03` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-04` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-05` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-2026-06` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-POS-PUBLICATION-PAGE-2026-001` | english.cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-PSP-RULES-2022-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-SANAA-C14-2024` | www.ecoi.net | OK | HTTP 206 |
| `SRC-CBY-SANAA-CURR-2024` | www.saba.ye | OK | HTTP 200 |
| `SRC-CBY-UNIFIED-NET-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-UNLICENSED-EWALLET-2024-001` | cby-ye.com | OK | HTTP 206 |
| `SRC-CBY-YPCC-BOARD-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CBY-YPCC-FOUND-2026-001` | cby-ye.com | OK | HTTP 200 |
| `SRC-CGAP-ARAB-MEAS-2017-001` | www.cgap.org | OK | HTTP 200 |
| `SRC-IBS-EPAY-YEM-2020` | www.findevgateway.org | OK | HTTP 200 |
| `SRC-IGC-AIDDATA-REMIT-YEM-2026` | www.theigc.org | OK | HTTP 200 |
| `SRC-IMF-AIV-2025-STAFF-001` | www.elibrary.imf.org | OK | HTTP 200 |
| `SRC-IMF-AIV-2025-SUPP-001` | www.elibrary.imf.org | OK | HTTP 200 |
| `SRC-IMF-YEM-EGDDS-VAL-1996` | dsbb.imf.org | OK | HTTP 200 |
| `SRC-KFW-RMMV-2023-001` | www.kfw-entwicklungsbank.de | OK | HTTP 206 |
| `SRC-KFW-YEM-MSME-FIN-III-47229` | www.kfw-entwicklungsbank.de | OK | HTTP 200 |
| `SRC-LIT-INVEST-ISLAMIC-FI-2024` | jurnal.iainponorogo.ac.id | OK | HTTP 200 |
| `SRC-OCHA-FTS-YEM-2026-001` | fts.unocha.org | OK | HTTP 202 (accepted, asynchronous) |
| `SRC-OECD-INFE-2023` | www.oecd.org | OK | HTTP 206 |
| `SRC-SANAA-EMONEY-2022` | sanaacenter.org | OK | HTTP 206 |
| `SRC-SANAA-MF-2020` | sanaacenter.org | OK | HTTP 200 |
| `SRC-SANAA-MFB-2024` | sanaacenter.org | OK | HTTP 206 |
| `SRC-SANAA-SOCPROT-2024` | sanaacenter.org | OK | HTTP 200 |
| `SRC-SANAA-YR-2025-Q2-MFB` | sanaacenter.org | OK | HTTP 206 |
| `SRC-SC-TRADE-FIN-YEM-2026` | sanaacenter.org | OK | HTTP 206 |
| `SRC-SFD-HIST-2004-Q3-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q1-2015-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q3-2015-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q3-2016-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2009-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2010-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2011-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2012-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2015-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SFD-Q4-2018-001` | www.sfd-yemen.org | OK | HTTP 206 |
| `SRC-SMEPS-AR2024-2025` | smeps.org.ye | OK | HTTP 200 |
| `SRC-SPA-SAU-BUDGET-2026-001` | www.spa.gov.sa | OK | HTTP 200 |
| `SRC-SPA-SAU-CBY-DEPOSIT-2018-001` | www.spa.gov.sa | OK | HTTP 200 |
| `SRC-SPA-SAU-CBY-DEPOSIT-2023-001` | www.spa.gov.sa | OK | HTTP 200 |
| `SRC-WB-ES-2013-PROFILE-001` | www.enterprisesurveys.org | OK | HTTP 200 |
| `SRC-WB-FINDEX-001` | microdata.worldbank.org | OK | HTTP 200 |
| `SRC-WB-FINDEX-003` | microdata.worldbank.org | OK | HTTP 200 |
| `SRC-WB-FINDEX-2014-001` | microdata.worldbank.org | OK | HTTP 200 |
| `SRC-WB-FINDEX-2025-EDITION` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-FINDEX-AGG-2022` | data.worldbank.org | OK | HTTP 200 |
| `SRC-WB-FINDEX-LDB-2015-001` | documents1.worldbank.org | OK | HTTP 416 to a range request; HTTP 200 and a PDF when requested whole |
| `SRC-WB-FMIIP-ISR2-2026-001` | documents.worldbank.org | OK | HTTP 206 |
| `SRC-WB-FMIIP-P180708` | maps.worldbank.org | OK | HTTP 200 |
| `SRC-WB-FSD-2024-001` | documents1.worldbank.org | OK | HTTP 200 |
| `SRC-WB-G2PX-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-G2PX-YEM-UCT-2024-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-MDB40-2024` | documents1.worldbank.org | OK | HTTP 416 to a range request; HTTP 200 and a PDF when requested whole |
| `SRC-WB-NFID-RFX-2026-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-WDI-REMIT-YEM-CURRENT` | data.worldbank.org | OK | HTTP 200 |
| `SRC-WB-YEM-CNL-2026-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-YEM-CPF-2026-2030-001` | documents.worldbank.org | OK | HTTP 206 |
| `SRC-WB-YEM-ECON-2020-04-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-YEM-ECON-MONITOR-2026-SPRING-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-WB-YEM-FRAGMENTATION-2025-001` | documents1.worldbank.org | OK | HTTP 200 |
| `SRC-WB-YEM-MEU-2019-12-001` | documents1.worldbank.org | OK | HTTP 416 to a range request; HTTP 200 and a PDF when requested whole |
| `SRC-WB-YEM-MFI-2004-001` | documents1.worldbank.org | OK | HTTP 416 to a range request; HTTP 200 and a PDF when requested whole |
| `SRC-WB-YEM-MONITOR-FALL2018-001` | documents1.worldbank.org | OK | HTTP 416 to a range request; HTTP 200 and a PDF when requested whole |
| `SRC-WB-YEM-OUTLOOK-2016-001` | www.worldbank.org | OK | HTTP 206 |
| `SRC-YMN-AR-2012-001` | yemennetwork.org | OK | HTTP 206 |
| `SRC-YMN-IMPACT-2021-001` | yemennetwork.org | OK | HTTP 206 |
| `SRC-YMN-MEMBERS-2026-001` | yemennetwork.org | OK | HTTP 200 |
| `SRC-YMN-MFMAG-2014-Q1-001` | yemennetwork.org | OK | HTTP 206 |
| `SRC-YMN-MFMAG-2014-Q2-001` | yemennetwork.org | OK | HTTP 206 |
| `SRC-SFD-MF-HISTORY-TOR-2012-001` | www.sfd-yemen.org | BROKEN — archived copy | → web.archive.org snapshot 20241006192210 of the original address; original kept as an additional locator |
| `SRC-SFD-NEWSLETTER-2000-Q4-001` | www.sfd-yemen.org | BROKEN — archived copy | → web.archive.org snapshot 20250213094943 of the original address; original kept as an additional locator |
| `SRC-SFD-Q2-2013-001` | sfd.sfd-yemen.org | BROKEN — archived copy | → web.archive.org snapshot 20240619144721 of the original address; original kept as an additional locator; the publisher's file now at `Newsletter-Quarter-2-2013.pdf` is another edition of No. 62 (table totals 84,760 / 151,465 / 6,845 against the bound 88,169 / 175,447 / 7,845) |
| `SRC-SFD-SMED-LP-2023-NOV` | smed.sfd-yemen.org | BROKEN — archived copy | → web.archive.org snapshot 20241112185856 of the original address; original kept as an additional locator |
| `SRC-CBY-SANAA-C12-2024` | yemeneco.org | BROKEN — unresolved | 404 at the host (yemeneco.org); no web.archive.org snapshot; no publisher address found (CBY Sana'a site returns 503). Kept; register item |
| `SRC-CBY-AR2015-HIST-001` | centralbank.gov.ye | HOST UNAVAILABLE | 503 at both checks (centralbank.gov.ye); a 2022 web.archive.org snapshot exists. Kept; re-checked at B14e |
| `SRC-SFD-Q1-2012-001` | www.sfd-yemen.org | MOVED — publisher's current address, same document | → `Newsletter-Quarter-1-2012.pdf` (No. 57, January–March 2012; 69,121 / 96,593 / 3,962 found) |
| `SRC-SFD-Q1-2019-001` | www.sfd-yemen.org | MOVED — publisher's current address, same document | → `Newsletter-Quarter-1-2019.pdf` (No. 85, January–March 2019; 85,219 and YR 14.664 billion found) |
| `SRC-SFD-Q2-2014-001` | www.sfd-yemen.org | MOVED — publisher's current address, same document | → `Newsletter-Quarter-2-2014.pdf` (No. 66, April–June 2014; 116,188 / 495,940 / 12,693 found) |
| `SRC-SFD-Q4-2017-001` | www.sfd-yemen.org | MOVED — publisher's current address, same document | → `Newsletter-Quarter-4-2017.pdf` (No. 80, October–December 2017; 85,259 / 746,387 / 7,800 found) |
| `SRC-SFD-Q4-2020-001` | sfd-yemen.org | MOVED — publisher's current address, same document | → `Newsletter-Quarter-4-2020.pdf` (No. 92, October–December 2020; 88,445 / 1,611,206 / 33,379 found) |
| `SRC-LIT-OEB-FX-PRICES-2025` | asjp.cerist.dz | NOT VERIFIABLE HERE — TLS | the host's certificate chain does not verify from this environment |
| `SRC-IMF-BPM6` | data.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260318234907) |
| `SRC-IMF-BPM6-COMP-GUIDE` | www.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260324012741) |
| `SRC-IMF-BPM7-IMPLEMENTATION` | www.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260510212609) |
| `SRC-IMF-D4D-YEM-ESS-2025` | www.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-IMF-YEM-AIV-2025-2026` | www.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-IMF-YEM-SMP-2026` | www.imf.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-LIT-XIDIAN-YEM-FI-2025` | www.researchgate.net | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-MDPI-UTAUT-YEM-2022` | www.mdpi.com | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20250927221012) |
| `SRC-OECD-YEM-RESILIENCE-001` | doi.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-OECD-YOUTH-DFI-2020-001` | www.oecd.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260829055351) |
| `SRC-UNDP-FMIIP-001` | www.undp.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260514020832) |
| `SRC-WB-FASTT-FPS-2021-001` | fastpayments.worldbank.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20260118012109) |
| `SRC-WB-RPW-SA-YEM-2025Q3-001` | remittanceprices.worldbank.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN |
| `SRC-WB-RPW-UAE-YEM-2025Q3-001` | remittanceprices.worldbank.org | NOT VERIFIABLE HERE — publisher refuses automated requests | HTTP 403 from the publisher's CDN; web.archive.org holds a snapshot (20251110132450) |
| `SRC-ADEN-CBY-LIQ-2016` | search.mandumah.com | SIGN-IN REQUIRED | the database record redirects to the publisher's sign-in page |

## What stays open

- `SRC-CBY-SANAA-C12-2024`: no working address and no archived copy; the publisher (CBY Sana'a) site returned 503. Register
  item (`FINAL_OPEN_ITEMS_REGISTER.md`, 3 October 2026).
- `SRC-CBY-AR2015-HIST-001`: host unavailable on 3 October 2026; re-checked at the B14e currentness re-run before any change.
- The 14 locators a publisher's CDN refuses to automated requests (IMF, OECD, MDPI, ResearchGate, UNDP, the World Bank's
  Remittance Prices Worldwide and Fast Payments sites) need a person with a browser at release; they are not broken.
- SFD newsletter No. 62 (Q2 2013): two editions exist; the bound values follow the original edition (archived), whose
  narrative the publisher's current file shares ("88 thousand" borrowers, "176 thousand" savers, portfolio near YR 8
  billion) while its provider table prints other totals under the heading "until end of June 2014". Register item.
