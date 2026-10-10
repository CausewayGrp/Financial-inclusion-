# A3 — CBY-Aden originals (read 10 October 2026, UTC; curl + page-image reading; repo untouched)

All files read in the original on cby-ye.com / english.cby-ye.com. Scans were rendered (pdftoppm) and read as images.
File-ID note: the first 8 hex digits of each /files/<id>.pdf are a Unix upload timestamp (e.g. 623ad771 = 2022-03-23 08:16 UTC;
65806fe2 = 2023-12-18). Several "dates" in the brief are UPLOAD dates, not instrument dates (flagged below).

## 1. Monetary and Financial Developments (التطورات النقدية والمالية)

| ID | verdict | exact finding | locator | note |
|---|---|---|---|---|
| MFD-55 | VERIFIED exists | "Issue No. 55 - June 2026" (AR cover «تقرير شهري العدد 55 – يونيو 2026»). PDF created 16 Sep 2026 | EN https://english.cby-ye.com/files/6ab393186466e.pdf ; AR https://cby-ye.com/files/6ab390fcaf357.pdf ; listed on https://english.cby-ye.com/researchandstatistics and https://cby-ye.com/pages/28 | latest issue held by CBY |
| MFD-56 | NOT FOUND | No July 2026 issue on either listing (last entries: June 2026) | same two listing pages, 10 Oct 2026 | Issue 54 = May 2026 (6a5a2e6bcc3cd) confirmed |
| MFD-RATE | VERIFIED | Table 6 Average Market Exchange Rates (YER/USD): Jun-2026 1,560.95; May-2026 1,562.49; May-2025 2,533.50; Jun-2025 2,733.85; Dec-2025 1624.45; Jan-2026 1,624.69; 2025 annual avg 2,078.30 | Issue 55 Table 6, printed p.17 (PDF p.18); narrative "parallel market" p.7 (PDF p.8) | bulletin calls it the "parallel market" average |
| MFD-T1 | VERIFIED | Table 1 Monetary Survey (YER bn) 2025 / May-26 / Jun-26: M2 11,429.3 / 11,903.3 / 11,925.0; Currency in circulation 3,270.5 / 3,501.7 / 3,384.3; CiC/M2 % 28.6 / 29.4 / 28.4; FX deposits 5,792.8 / 5,732.2 / 5,807.6; FX dep/total dep % 71.0 / 68.2 / 68.0 | Issue 55 Table 1, printed p.10 (PDF p.11) | shares printed by CBY (not computed) |
| MFD-T4 | VERIFIED | Table 4 Banks – Assets (YER bn) 2025 / May-26 / Jun-26: Total Assets 12,341.8 / 13,362.1 / 13,761.2; Foreign Assets 4,116.5 / 4,448.0 / 4,650.0; Loans & Advances–Government 1,928.8 / 2,145.0 / 1,966.8; Private Sector 1,392.3 / 1,350.4 / 1,362.9 | Issue 55 Table 4, printed p.15 (PDF p.16) | "claims on government" = row "Government" under Loans & Advances |
| MFD-T5 | VERIFIED | Table 5 Banks – Liabilities: Deposits 8,496.9 / 8,768.5 / 8,915.9 | Issue 55 Table 5, printed p.16 (PDF p.17) | |
| MFD-RATE-POLICY | VERIFIED | p.7: CBY "set the benchmark interest rate on new savings deposits in the local currency ... at 18% per annum"; Feb-2026 issue said the minimum "remained at 15%" | Issue 55 PDF p.8; Feb-2026 issue https://english.cby-ye.com/files/69f5fee4918e1.pdf PDF p.9 | Feb-2026 EN cover mislabels "Issue No. 51 - February February 2025" |
| SAR-2026 | NOT FOUND | No SAR repricing decision of 13 Feb 2026 on cby-ye.com news, pages/14, or Feb/Mar/Jun-2026 bulletins (EN+AR searched). Nearest original: Board extraordinary meeting 12 Feb 2026 on FX rates, "فوض المجلس الإدارة التنفيذية لاتخاذ ما تراه مناسباً" | https://cby-ye.com/news/918 | FRONTIER card; English news site stale (latest id 193) |

## 2. POS monthly releases

| ID | verdict | exact finding | locator | note |
|---|---|---|---|---|
| POS-2026-07..09 | NOT FOUND | Arabic payments page lists «عمليات نقاط البيع الشهرية» March 2025 → June 2026 only; English page ends Jan 2026 | https://cby-ye.com/pages/33 ; https://english.cby-ye.com/pages/27 (10 Oct 2026) | repo latest = 2026-06 (SRC-CBY-POS-2026-06, OBS-00095..97): SAME |
| POS-2026-01 file | DIFFERS (locator) | AR page now links Jan-2026 to /files/6a6f950da3173.pdf; repo SRC-CBY-POS-2026-01 uses 69b058d4bc306 | pages/33 | re-upload; values not re-read |
| POS-2025-01/02 | NOT FOUND | No Jan or Feb 2025 release on pages/33 or any /pages/1–60; first release is March 2025 | pages/33 | cannot confirm OBS-00036 period |
| OBS-00036 period | NOT CONFIRMED | H1 report prints NO. of Transactions 58,512, NO. of POS 791 (=June-2025 monthly 791 → stock at end-June). March-2025 release: 8,015, "+1%" vs "Feb. 2025" (Feb implied ≈7,936). Mar–Jun monthly sum = 42,086. H1 POS value prints "1,240 مليار ريال يمني" while Mar–Jun monthly values sum to YER 1,560 million → H1 values are not demonstrably Jan–Jun flow sums | H1 https://www.cby-ye.com/files/693a7845e7f26.pdf p.1 POS panel; Mar-2025 https://cby-ye.com/files/6812a1758f5a5.pdf p.1 header "Compared to the previous month - Feb. 2025" | keep OBS-00036 held; reason: no Jan–Feb 2025 releases published; value tile inconsistent with monthly sums |

## 3. CR-13 — H1-2025 sex shares

| ID | verdict | exact finding | locator | note |
|---|---|---|---|---|
| CR-13 81/18/1 | DIFFERS (repo swapped) | In the «الحسابات / Accounts» panel (NO. of Accounts 5,202,019): bars ذكر 81%, أنثى 18%, شركات 1%; box caption «نسبة عدد المواطنين الذين يمتلكون حسابات بنكية وفق النوع» | SRC-CBY-PAYREPORT-H1-2025 p.1, bottom-left panel | belongs to bank accounts (OBS-00038..40 / IND-0018..20 mislabelled "E-wallet subscribers") |
| CR-13 84/16 | DIFFERS (repo swapped) | In the «المحافظ الإلكترونية / E-wallets» panel (NO. of Subscribers 2,102,484; NO. of E-wallets 9): donut 84% (male icon) / 16% (female icon); caption «نسبة عدد المشتركين وفق النوع» | same p.1, bottom-right panel | belongs to e-wallet subscribers (OBS-00041..42 / IND-0021..22 mislabelled "Bank accounts") |
| ATM shares | NOTE | ATM panel heading «أبرز المحافظات ذات التركيز الأعلى للصرافات الآلية»; Sana'a 35%, Aden 20%, Taiz 13%, Hadramout 11%, Marib 4%; NO. of ATMs 914; no perimeter or "governorate vs city" definition printed | same p.1, ATM panel | U6: keep held (perimeter not stated) |

## 4. CR-20 — Deposit insurance

| ID | verdict | exact finding | locator | note |
|---|---|---|---|---|
| Law text | VERIFIED (No. 21) | Ministry of Legal Affairs certified copy: «قانون رقم (٢١) لسنة ٢٠٠٨م بشأن مؤسسة ضمان الودائع المصرفية»; signed Sana'a 17 Rabi' II 1429 / 23 Apr 2008; Art. 47 in force 30 days after Official Gazette publication; Art. 45 all deposit-taking licensed banks must register | https://cby-ye.com/files/62c2edbaad8eb.pdf p.1 title, p.12 signature (listed on https://cby-ye.com/rulesandregulations as «قانون مؤسسة ضمان الودائع») | rule |
| Decision 6/2025 | DIFFERS from lead | Governor's Decision «قرار رقم (6) لسنة 2025م بشأن نقل المركز الرئيسي لمؤسسة ضمان الودائع الى العاصمة المؤقتة عدن», Ref 376/CBY/2025, letterhead date 16/7/2025, signed 20 July 2025, effective on issue. It RELOCATES the Institution's head office from Sana'a to Aden; it does NOT establish it. Its recital cites «القانون رقم (40) لسنة 2008» | https://cby-ye.com/news/833 (2025-07-20); https://cby-ye.com/files/687c9970b82d9.pdf p.1 | the "21 vs 40" conflict is between two CBY-hosted originals: law copy = 21; Decision 6/2025 recital = 40. Cite the law copy as No. 21 and record the recital discrepancy |
| DII activity | NOTE | «مؤسسة ضمان الودائع تعقد أول اجتماع لها لتفعيل عملها من العاصمة عدن»; Board «يقر إنشاء لجنة الحوكمة» | news/926 ; news/948 | implementation, not operation of cover |

## 5. Appendix C instruments

| ID | verdict | title (AR / EN gloss), no., dates, requirement | locator | type |
|---|---|---|---|---|
| Defaulters registry | VERIFIED | «البنك المركزي اليمني يدشن نظام سجل المتعثرين» (CBY launches the defaulters-registry system), 2026-08-05: digital platform to exchange data on defaulting customers among banks operating in Yemen; success "مرهوناً بالتزام جميع البنوك ... بتزويده ببيانات دقيقة" | https://cby-ye.com/news/963 | implementation (launch ≠ coverage) |
| Decision 4/1991 | NOT FOUND as document | Only cited: «قرار محافظ البنك المركزي رقم (4) لسنة 1991م بشأن نظام تبادل المعلومات عن الائتمان بين البنوك» + circulars 33379 (14/8/1991), 54064 (2/7/2006) | https://cby-ye.com/publications/149 | rule (referenced) |
| Pub 149 | VERIFIED | «نظام تبادل معلومات مخاطر الائتمان ومتطلبات الاستمارة رقم (6)» (credit-risk information exchange, Form 6): covers commercial and specialised banks; reporting threshold 500 thousand YER; data due by 15th of following month | https://cby-ye.com/publications/149 (page date 2021-10-06) | rule; 2021-10-06 is the web posting date (legacy circular), not instrument date |
| Pub 150 | VERIFIED | «معلومات مخاطر الائتمان»: no loan/financing before enquiry to the Credit & Banking Risk Dept and obtaining the client code; check notice list per Circular 2/2000 | https://cby-ye.com/publications/150 (page date 2021-10-06) | rule; same dating caveat |
| Decision 7/2026 | VERIFIED | «قرار محافظ البنك المركزي اليمني رقم (7) لسنة 2026م بشأن أسعار الفائدة على الودائع والائتمان لدى البنوك», Ref 220/CBY/2026, dated 9/4/2026 (21 Shawwal 1447), MPC meeting 8 Apr 2026; Art.1 minimum «(18%) سنوياً» on new YER savings deposits at commercial banks; Art.2 FX deposit rates free; Art.4 lending rates free; Art.5 Islamic banks exempt; Art.6 applies to contracts after effect; Art.7 effective «12 أبريل 2026م» | https://cby-ye.com/files/69dcac86e3520.pdf p.1 | rule |
| Decisions 8, 12, 16 of 2026 | NOT FOUND | News ids 900–975 (all 2026 items) publish Decisions 1–6, 9–11, 13–15, 17–18 only; 7 is on pages/14; 8, 12, 16 absent from news and pages/14 | https://cby-ye.com/news?page=1..74 ; https://cby-ye.com/pages/14 | FRONTIER |
| e-KYC | DIFFERS (date) | «تعليمات تنظيم إجراءات إعرف عميلك إلكترونياً», Ref 840/CBY/2023, dated 9/11/2023 (upload 18 Dec 2023); scope banks + licensed mobile e-money providers; remote onboarding "دون الحاجة إلى تواجد العميل بشكل شخصي"; reporting incl. avg minutes to open/activate account. No effective-date clause seen on pp.1–2, 29–30 | https://cby-ye.com/files/65806fe2b3757.pdf pp.1–2, 30 (30 pp) | rule; 18 Dec 2023 = upload date |
| Board 2/11/2022 | DIFFERS (date) | «قرار مجلس إدارة البنك المركزي اليمني رقم (2022/2/11)» amending Decision 12/2010 (MFB Law 15/2009 regulation); Ref 176/CBY/2022, dated 21/3/2022 (18 Sha'ban 1443); Board meeting (2) 27 Feb 2022. Art.10(b) «لا يجوز الجمع بين ممارسة نشاط الصرافة ونشاط التمويل الأصغر»; 10(c) MFB application refused if shareholders own exchange firms unless converting the exchange firm into an MFB; 10(d) prior approvals: exit exchange within one year; Art.15(a) MFB paid-up capital ≥ YER 5 billion | https://cby-ye.com/files/623ad771a78d7.pdf pp.1–2, 9 | rule; "23 Mar 2022" is the upload date |
| Board 3/11/2023 | VERIFIED | «قرار مجلس الإدارة رقم (2023/11/3) لسنة 2023م بشأن رفع رؤوس أموال بنوك التمويل الأصغر ... إلى (15) مليار يمني», Ref 957/CBY/2023, dated 31/12/2023, Board session 27 Dec 2023; min paid-up YER 15,000,000,000; 50% of increase per year from 2024, deadline 31/12/2025; Art.6 licence withdrawal for non-compliance | https://cby-ye.com/files/659aa2ee5852b.pdf pp.1–2 | rule; cites Board decision (8)/2022 on bank capital |
| Circular 2/2025 | VERIFIED | «منشور دوري رقم (2) لسنة 2025م» to all banks and exchange companies/establishments, dated 24/9/2025; AML/CFT supplement to circulars 1/2012, 1/2013, 8/2014, 2/2021 | https://cby-ye.com/files/68dcd80cd12b9.pdf p.1 (7 pp) | rule |
| Circular 3/2025 | VERIFIED | «منشور دوري رقم (3) لسنة 2025م ... بشأن "تعليمات إدارة المخاطر في البنوك"», No. CBY/3/2025, dated 2 Nov 2025; applies to all banks; METAC (IMF) support | https://cby-ye.com/files/690e0e07d4981.pdf p.1 (39 pp) | rule |
| Circular 4/2025 | VERIFIED | «منشور دوري رقم (٤) لسنة ٢٠٢٥م» to banks and exchange firms, dated 02/11/2025: enhanced due diligence and screening against UN Security Council and OFAC lists | https://cby-ye.com/files/690e0e39ce5d9.pdf p.1 (4 pp) | rule |
| Circular 1/2026 | VERIFIED | «منشور رقم (1) لسنة 2026م» «حظر التعامل بالأصول الافتراضية او العملات المشفرة ومع مقدمي خدماتها», Ref CBY/L/258/2026, dated 15/09/2026; scope banks, exchange firms, payment-service providers and e-wallet operators; «يُعمل بهذا المنشور من تاريخ صدوره» | https://cby-ye.com/files/6aaa38b226baa.pdf pp.1, 5 | rule |
| National switch | VERIFIED | «يدشن المرحلة الأولى بالعمل بنظام المقسم الوطني»: launched Thu 7 March [2024], first phase «بربط سبعة بنوك»; official operation after all banks connected | https://cby-ye.com/news/645 (posted 2024-03-09) | implementation |
| Board 28 Mar 2024 | VERIFIED | Board meeting 2 of 2024 reviewed phase 1 of the national switch (ATMs, POS, e-wallets) and the launch of the unified money-transfer network replacing exchange-company networks | https://cby-ye.com/news/656 (2024-03-28) | implementation |
| Buna | VERIFIED | 14 Sep 2023 CBY «انضمام ... الفعلي لمنصة (Buna)»; «سابع بنك مركزي عربي ينضم» | https://cby-ye.com/news/579 | implementation (connection ≠ transaction volume) |
| 2025 enforcement wave | VERIFIED (counts) | 23 Jul–6 Aug 2025: 11 Governor's decisions, Nos. 7–17 of 2025, covering 51 licences: 44 suspensions (Nos. 7:13, 8:5, 9:10, 10:2, 11:7 incl. 1 remittance agent, 12:2, 15:4, 17:1) and 7 withdrawals (13:4 company branches, 14:1, 16:2). Basis: field-inspection report of Banking Supervision Sector | news/834 (23 Jul), 836 (24 Jul), 837 (28 Jul), 838 (29 Jul), 839 (31 Jul), 840/841/843 (3 Aug), 846 (4 Aug), 847 (5 Aug), 848 (6 Aug); PDFs linked from each | implementation; names deliberately not recorded |
| SAR repricing 13 Feb 2026 | NOT FOUND | see SAR-2026 above | news/918 | FRONTIER |

## 6. Bank list

| ID | verdict | exact finding | locator | note |
|---|---|---|---|---|
| Heading/columns | VERIFIED | Heading «كشف بالبنوك المرخصة بالجمهورية اليمنية»; columns: م / اسم البنك / Bank's Name / الموقع الالكتروني / عنوان البنك / Bank's Adress; 26 rows; no date printed (PDF created 26 Jul 2026) | https://cby-ye.com/files/6a665add29feb.pdf (linked on https://cby-ye.com/pages/14 as «قائمة البنوك المرخصة بالجمهورية اليمنية») | |
| 12 MFBs | NOT IN SOURCE (inferred) | The list has NO type/classification column. 12 names carry «للتمويل الأصغر»/"Microfinance": rows 10, 11, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26 | same | "12 microfinance banks" must be worded as "by name", computed by CauseWay; same for ISLAMIC_BANK class. Rows 3 and 6 list Sana'a addresses |

## Repo impact (IDs only)
- SRC-CBY-001 / 18_CBY_MONETARY (cby_monetary.json): add Issue 55 (June 2026); 2026-06 rows; May-2026 values unchanged. Issue 56 not published.
- 19_PAYMENTS_DATA: OBS-00038..40 and IND-0018..20 → bank accounts; OBS-00041..42 and IND-0021..22 → e-wallet subscribers (CR-13). OBS-00036 stays held (no Jan/Feb 2025 releases). SRC-CBY-POS-2026-01 locator re-uploaded (6a6f950da3173). POS latest = 2026-06, no change.
- CR-20 / 33_ANALYTICS_MASTER: law = No. 21 of 2008 (certified copy); Decision 6/2025 recital says 40; Decision 6/2025 = head-office relocation (fix any "establishing" wording).
- Appendix C: new sources for news/963, publications/149–150, 69dcac86e3520, 65806fe2b3757 (date 9 Nov 2023), 623ad771a78d7 (date 21 Mar 2022), 659aa2ee5852b, 68dcd80cd12b9, 690e0e07d4981, 690e0e39ce5d9, 6aaa38b226baa, 62c2edbaad8eb, 687c9970b82d9, news/645, 656, 579; enforcement-wave event (counts). FRONTIER: Decisions 8/12/16 of 2026, SAR repricing, Decision 4/1991 text.
- FINAL_CURRENTNESS_CUTOFF "9 not held": 6 of 9 read here (65806fe2b3757, 68dcd80cd12b9, 690e0e07d4981, 690e0e39ce5d9, 69dcac86e3520, 6aaa38b226baa). Not read: 64bada99e708e (bank balance-sheet report to Dec 2022), 663c8ad5cafdc (FX banknote repatriation rules), 6653499a7181b (Decision 19/2024).
- providers_data.json PRV-BANK-* entity_class (MICROFINANCE_BANK 12, ISLAMIC_BANK 6) is inferred from names; AR-022/ED-035/ED-036 should say "by name".
