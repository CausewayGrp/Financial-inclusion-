# V6: CBY POS January 2026 and OECD (2026) locator checks

Run: 2026-10-11, about 13:07 to 13:16 UTC. Read-only. Downloads are in `scratchpad/v5/dl/V6/` (new folder). Nothing under `<repository>` was touched.

## 1. CBY-Aden monthly POS transactions, January 2026

### 1.1 The two files

| | A: original (text layer) | B: redesign (image only) |
|---|---|---|
| URL | https://www.cby-ye.com/files/69b058d4bc306.pdf | https://cby-ye.com/files/6a6f950da3173.pdf |
| HTTP | 200 | 200 |
| Bytes | 2,294,532 | 3,806,999 |
| SHA-256 | 6036fcdc445c28289c45b86a4f3e37578fba10636251f46ebde52ac3e5025d88 | 52fa66f423f5072a3b73185dff24398dc289d8d3a448214420d19c61d4af46bf |
| Pages | 1 (750 x 1334 pt) | 1 (567 x 319 pt) |
| Producer, created | Adobe Illustrator 27.8, 4 Mar 2026 | Adobe Photoshop 22.5, 2 Aug 2026 18:55 UTC |
| Last-Modified | Tue, 10 Mar 2026 17:45:56 GMT | Sun, 02 Aug 2026 19:05:49 GMT |
| Text layer | Yes (pdftotext -layout) | None. One embedded 2268 x 1276 JPEG. No OCR tool is installed, so values were read visually and the governorate table was checked at 2x. |

The English listing's January file, https://english.cby-ye.com/files/69b05c24bea8d.pdf, returns HTTP 200 with the same size and SHA-256 as A.

### 1.2 Values in A (main table, from the text layer and a 110 dpi render)

Total:
- No. of POS 1,473 (+11%)
- No. of transactions 24,026 (+4.9%)
- Value SAR 602,382 (+88.6%)
- Value USD 177,965 (-38.3%)
- Value YER 1,262 (Arabic label "مليار", billion) (+38.5%)

Governorates. Values are listed in the order SAR, USD, YER, transactions, POS, each followed by its change:
- Aden: 174,425 (+866%); 7,344 (+22.6%); 586,417 M (+134%); 13,676 (+26.6%); 474 (+21%)
- Hadhramout: 380,810 (+41.5%); 65,346 (+58.8%); 563,742 M (-0.4%); 9,180 (+1.2%); 848 (+3.7%)
- Almaharah: 36,667 (+50.8%); 12,583 (+33%); 102,676 M (+18%); 1,036 (+0.8%); 91 (+3.4%)
- Shabwah: 480 (-91%); 0 (-100%); 835,700 (-46%); 35 (+62.7%); 18 (0%)

Sectors, share of transactions: Shopping 74%, Restaurants 14%, Pharmacies 3%, Hotels and Resorts 2%, Diff. Services 2%, Exchange Companies 2%, Gas Stations 2%, Hospitals 1%. Total 100%.

### 1.3 Values in B and the differences

B's KPI boxes: POS 1,473 (+11%), transactions 24,026 (+4.9%), YER 1,262 Billion (+38.5%), USD 178 Thousand (-38.3%), SAR 602 Thousand (+88.6%). These match A, with USD and SAR rounded to thousands. The sector shares are identical; the label "Diff. Services" becomes "Other Services".

Governorate cells that differ (confirmed in the 2x crop):

| Cell | A | B |
|---|---|---|
| Aden, SAR % change | +866% | +86.6% |
| Hadhramout, YER % change | -0.4% (down arrow) | +0.4% (up arrow) |
| Shabwah, YER % change | -46% (down arrow) | +46% (up arrow) |
| Shabwah, SAR value and % change | 480, -91% | 0, = 0% |

All other governorate cells match A.

**Verdict: not identical.** The totals and sector shares match, but four governorate cells differ. B does not differ from A only in layout.

**Arithmetic check** (rounded % changes, so approximate). The total SAR change implies a December 2025 total of about 319,397. With Aden at +866%, the four listed governorates' December values sum to about 316,828, which fits under that total. With Aden at +86.6%, they sum to about 392,247, which is 72,851 over. So A's +866% fits the published total and B's +86.6% does not. The Shabwah SAR cannot be settled this way: the current listed sums leave 10,000 (A) or 10,480 (B) for unlisted governorates. The YER arrows cannot be checked without December figures, which the files do not give.

### 1.4 What the listing pages show

Both pages returned HTTP 200 (Arabic 35,398 bytes; English 31,167 bytes). They show month labels only. There are no per-entry dates and no re-issue note.

Arabic, https://cby-ye.com/pages/33:
- January 2026 links to /files/6a6f950da3173.pdf (= B). December 2025 links to /files/69b058981b681.pdf (Last-Modified 10 Mar 2026).
- February to June 2026 link to five more August 2026 files: 6a6f958d49cc2, 6a6f960871730, 6a6f968423908, 6a6f96ed5c009, 6a6f973c98c25. Their Last-Modified times are 2 Aug 2026 at 19:07:57, 19:10:00, 19:12:04, 19:13:49 and 19:15:08 GMT.
- Neither page links A by its own path (69b058d4bc306).

English, https://english.cby-ye.com/pages/27:
- January 2026 links to /files/69b05c24bea8d.pdf, which is byte-identical to A (Last-Modified 10 Mar 2026). It is still the original, not the redesign.
- No redesigned files appear on the English page.

**Answer to "re-issued in a redesigned layout on 2 August 2026":** Confirmed for the Arabic listing. The January 2026 entry and the February to June 2026 entries carry 2 Aug 2026 Last-Modified times (19:05 to 19:15 GMT), and B's PDF creation date is 2 Aug 2026. The listing page shows no date; the date comes from HTTP headers and PDF metadata. The English listing still shows the March original and no redesign. Not confirmed: any announcement of the re-issue, or whether B differs from A anywhere outside the main table.

## 2. OECD (2026) Promoting Economic Resilience in Yemen

**PDF:** https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/promoting-economic-resilience-in-yemen_b66657c1/81ed2898-en.pdf
- HTTP 200, 2,028,063 bytes, SHA-256 4ae2f699e06796b25e2e13312f125fa2582a37b9a7b0aa108bf81606a6ef33b0.
- 71 pages. PDF title metadata "Promoting Economic Resilience in Yemen (EN)", author OECD, created 14 Jan 2026 (the URL path says 2026/02).
- Page 1 text begins "Promoting Economic Resilience in Yemen".

**DOI:** https://doi.org/10.1787/81ed2898-en redirects once to https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en.html. That page returns HTTP 403 with `cf-mitigated: challenge` (a Cloudflare "Just a moment..." page). I did not try to get past the challenge, so the landing page and the chapter HTML could not be read from this client.

**Chapter and read-online URLs.** These were found by a web search restricted to oecd.org. They were not fetched, and each returns 403 to this client:
- Full report (HTML with chapter navigation): https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report.html
- Introduction: https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/introduction_bf2047ce.html
- Chapter 1, Domestic Revenue Mobilisation: https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/domestic-revenue-mobilisation_c0ce5075.html
- Chapter 2, The Financial Sector: https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/the-financial-sector_4d6228a4.html
- Chapter 3, Capacity for Economic Data Collection and Analysis: https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/capacity-for-economic-data-collection-and-analysis_a909c60d.html
- Chapter 4 (public-private dialogue): no chapter URL found; the search showed only table references.

The search excerpt gives a publication date of 16 Feb 2026. That is not verified here.

## 3. Files in the V6 folder

`scratchpad/v5/dl/V6/`: `pos_a.pdf`, `pos_a.txt`, `pos_a.headers`, `pos_a_render.png`; `pos_b.pdf`, `pos_b.headers`, `pos_b.txt` (empty, no text layer), `pos_b_img-000.jpg`, `pos_b_gov_crop.png`; `pos_en_jan.pdf`, `pos_en_jan.txt`; `cby-ye_com_pages_33.html`, `english_cby-ye_com_pages_27.html`; `oecd_pyer_2026.pdf`, `oecd_p1.txt`; `oecd_doi_landing.html` (the Cloudflare challenge page).

## 4. Open items

- B's values are visual readings from an image. The four differing cells were confirmed in the 2x crop. CBY should confirm which version is authoritative, since the files alone cannot settle the Shabwah SAR value or the two YER arrows.
- The oecd.org chapter URLs need a browser to confirm.
- The "M" suffix on the governorate YER values is not expanded in either file. It is reported as printed.
