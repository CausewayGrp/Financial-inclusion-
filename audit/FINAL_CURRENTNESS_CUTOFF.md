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

## Release-candidate recheck — 3 October 2026 (appended; the Tranche C record above is unchanged)

With the network open, the watch points were re-read in their originals on 3 October 2026; every request and result,
"checked on 3 October 2026, nothing newer" included, is in `audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md`
§3, and what the Master now holds in §4 (transaction RC-8). The changes against the table above:

| Candidate | Result on 3 October 2026 | Classification | Where |
|---|---|---|---|
| CBY-Aden payments page recheck (PAYCUR) | The Arabic payments page (https://cby-ye.com/pages/33) lists monthly POS releases to **June 2026**; the English page still ends at January 2026. The 26 September recheck read the English page only | PUBLIC CLAIM CHANGE | CLM-003, CLM-017, VIS-POS-*, /payments/, Home, /access/, Readings; RC-8 |
| CBY-Aden list of licensed banks | Newer Arabic file (July 2026), 26 banks, names unchanged | Copy fix (check date 3 October 2026) and locator | CLM-008/055 and every dated mention; RC-8 |
| CBY-Aden Governor's decisions | Newest is No. 18 (24 September 2026); No. 10 is dated 8 June 2026 on the instrument | Date fix (PSE-012) | /providers/; RC-8 |
| World Bank FMIIP ISR, Global Findex 2025, IMF eLibrary | Nothing newer; Findex 2025 does not cover Yemen | NO CHANGE | — |
| Remittance Prices Worldwide; SFD/SMED | Not readable from this session | NO CHANGE (stays as checked on 26 September 2026; EXT-06 open) | — |

The edition label moves to 3 October 2026 ("This edition reflects what its sources showed when they were checked, up to
3 October 2026"). B14e re-runs this sweep before the release candidate closes and appends its own dated result here.

Addendum, 3 October 2026 (RC-8b, after the independent reviews of RC-8): CBY-Aden's 2026 exchange and remittance roster
was found replaced on its licensing page (https://cby-ye.com/pages/14). The new file is dated 22 September 2026 by its PDF
metadata, with no printed date, and lists 100 companies, 231 establishments and 111 remittance agents. The 19 August file
listed 98, 225 and 106. Classification: PUBLIC CLAIM CHANGE. CLM-009, VIS-PROVIDER-TIME, /providers/ and /access/ are
updated.

## Currentness re-run — 2026-10-03 (`scripts/currentness_rerun.py`; appended)

| Watch point | Held in the Master | Found | Result |
|---|---|---|---|
| CBY-Aden monthly POS releases ([page](https://cby-ye.com/pages/33)) | 2026-06 | 2026-06 | SAME |
| CBY-Aden Governor's enforcement decisions (2026) ([page](https://cby-ye.com/news)) | No. 18 | No. 18 (latest listed) | SAME |
| CBY-Aden licensing and regulation page (bank list, roster, decisions, circulars) ([page](https://cby-ye.com/pages/14)) | 5 of them held | 14 files linked; 9 not held | NOT HELD — decide |
| World Bank FMIIP (P180708) status reports ([page](https://search.worldbank.org/api/v3/wds?format=json&proid=P180708&fl=docdt,docty,display_title&rows=50)) | ISR seq. 2, 2026-04-08 (SRC-WB-FMIIP-ISR2-2026-001) | 2 reports; latest 2026-04-08 | SAME |
| Global Findex — Yemen account ownership ([page](https://api.worldbank.org/v2/country/YEM/indicator/FX.OWN.TOTL.ZS?format=json&per_page=60)) | 2021 wave, data year 2022 (fieldwork 2022-11-07 to 2023-01-09) | latest year with a value: 2022 | SAME |
| IMF Staff-Monitored Program (Yemen) ([page](https://www.imf.org/en/news/articles/2026/07/16/pr26249-yemen-imf-reaches-sla-on-new-staff-monitored-program)) | staff-level agreement, 16 July 2026; no approval notice held | HTTP 403 | CHECK BY HAND |
| Remittance Prices Worldwide — Saudi Arabia to Yemen ([page](https://remittanceprices.worldbank.org/corridor/Saudi%20Arabia/Yemen)) | 2025 Q3 | HTTP 403 | CHECK BY HAND |
| CBY Sana'a annual report 2015 host ([page](http://centralbank.gov.ye/App_Upload/Ann_rep2015AR.pdf)) | locator held; 503 on 3 October 2026 | HTTP 503 | CHECK BY HAND |

- CBY-Aden Governor's enforcement decisions (2026): Only the first page of the news listing is read; it covers the latest ten items.
- CBY-Aden licensing and regulation page (bank list, roster, decisions, circulars): «تقرير تطورات الميزانية المجمعة للبنوك حتى ديسمبر 2022م» (64bada99e708e.pdf); «تعليمات تنظيم اجراءات اعرف عميلك الكترونياً» (65806fe2b3757.pdf); «التعليمات والضوابط المنظمة لعمليات ترحيل فوائض أوراق النقد الأجنبي» (663c8ad5cafdc.pdf); «قرار محافظ البنك المركزي رقم 19 لسنة 2024» (6653499a7181b.pdf); «منشور دوري رقم 2 لسنة 2025م ملحق لمنشورات التعليمات والضوابط الرقابية للبنوك وشركات/ منشآت الصرافة» (68dcd80cd12b9.pdf); «منشور دوري رقم 3 لسنة 2025م موجة الى كافة البنوك العاملة في الجمهورية اليمنية بشان تعليمات ادارة المخاطر في البنوك» (690e0e07d4981.pdf); «منشور دوري رقم 4 لسنة 2025م تعليمات تطبيق إجراءات العناية الواجبة المعززة والتحقق من قوائم العقوبات الدولية» (690e0e39ce5d9.pdf); «قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026م بشأن أسعار الفايدة على الودائع» (69dcac86e3520.pdf); «منشور دوري رقم (1) لسنة 2026م بشأن حظر التعامل بالأصول الافتراضية او العملات المشفرة ومع مقدمي خدماتها» (6aaa38b226baa.pdf)
- IMF Staff-Monitored Program (Yemen): The host refuses automated requests or is unavailable; a person checks it with a browser.
- Remittance Prices Worldwide — Saudi Arabia to Yemen: The host refuses automated requests or is unavailable; a person checks it with a browser.
- CBY Sana'a annual report 2015 host: The host refuses automated requests or is unavailable; a person checks it with a browser.

A result covers only the page named; "CHECK BY HAND" is not "nothing newer". A newer item enters the Master
only through a transaction after it is read in its original.
