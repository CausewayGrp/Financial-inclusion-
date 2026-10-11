# Red-team review: CLOSE-6B (source utilisation)

- **Reviewed:**
  - `scratchpad/c6b/close_6b.py` (621 lines, 06:51);
  - `scratchpad/c6b/tools/code_patch.py` (06:51);
  - `scratchpad/c6b/tools/counts.py` (06:57), because it ships with the transaction.
- **Evidence:**
  - reads R2, R3, R4 and R7 (`scratchpad/addendum/reads/`);
  - the current projections under `site-src/content/` and the built `dist/en/data/index.html`;
  - the Master rows 32_QUAL_LITERATURE LIT-YEM-2016-001, LIT-YEM-2025-006 and LIT-ISLAMIC-2024-001, and 33_ANALYTICS_MASTER CTR-007, which I read with openpyxl;
  - `scripts/yfie/content.py`, `scripts/yfie/families.py`, `scripts/validate.py` and `scripts/projection/derived.py`.
- **Guards dry-checked against the projections:** every "expected current value" guard in the script matches what the projections hold. The scope line (EN and AR) occurs once. Each AMB substring occurs once. The AMB and CCY issuers, all four HIST fields, the canonical titles and dates, and the YSC-012 boundary text all match. I expect no TxError.
- Nothing under the repository was modified. `L…` means a line of `close_6b.py`.

---

## BLOCKER

### B1. The C12 card misstates who sets the rate for currencies other than the dollar (EN and AR)

- **Quote (L320-323):**
  > "…and individual transfers in US dollars or other foreign currencies in their Saudi-riyal equivalent, at rates its Foreign Exchange Dealing Unit approves; it applies from 14 March 2024."
  - AR (L325-327): «…بالدولار الأمريكي أو بعملات أجنبية أخرى بما يعادلها بالريال السعودي، بأسعار تعتمدها وحدة التعاملات بالنقد الأجنبي لديه»
- **Evidence:** R3, Item 2, the payout rules.
  - §2(a): dollar transfers are paid at «سعر بيع الدولار مقابل الريال السعودي المعتمد من وحدة التعاملات بالنقد الأجنبي». This is the unit's rate.
  - §3(a): transfers in other foreign currencies are paid «بسعر البيع العالمي للعملة الأجنبية مقابل الريال السعودي يوم إصدار الحوالة». This is the international selling rate on the day the transfer was issued, not a rate the unit approves.
- **Failure:** a public card on the one Sana'a instrument in the group gives the Sana'a bank's FX unit a rate-setting role that the circular does not give it. The card is not true to its source. No gate checks paraphrase against the original.
- **Note:** the YSC-012 fact (L407-413) makes no rate claim and is correct.
- **Proposed wording:**
  - EN: "…transfers in Saudi riyals are paid in Saudi riyals; individual transfers in US dollars are paid in their Saudi-riyal equivalent at the dollar rate its Foreign Exchange Dealing Unit approves, and those in other foreign currencies at the international selling rate against the Saudi riyal on the day the transfer was issued; it applies from 14 March 2024."
  - AR: «…تُصرف الحوالات الواردة بالريال السعودي بالريال السعودي، والحوالات الفردية الواردة بالدولار الأمريكي بما يعادلها بالريال السعودي بسعر الدولار الذي تعتمده وحدة التعاملات بالنقد الأجنبي لديه، والواردة بعملات أجنبية أخرى بما يعادلها بالريال السعودي بسعر البيع العالمي يوم إصدار الحوالة؛ ويُعمل به اعتبارًا من 14 مارس 2024.»

---

## SHOULD-FIX

### S1. The BANKS-BS-2022 card states as fact a negative that R7 marks NOT VERIFIED

- **Quote (L310-312):**
  > "It prints no issue date and no issuing department."
  - AR: «ولا يحمل تاريخ إصدار مطبوعًا ولا اسم الإدارة المصدرة.»
- **Evidence:** R7, Doc 9.
  - "No department or sector is printed on the pages examined: 1–3, 13–16, 32–35. NOT VERIFIED."
  - "Date of issue. None printed on the pages examined. NOT VERIFIED."
  - The report has 35 pages. Pages 17–31 were not examined.
- **Failure:** the card goes beyond the read. The existing title's "(no issue date printed)" was already in place; "no issuing department" is new in this transaction.
- **Proposed wording:**
  - EN: "No issue date or issuing department is printed on the pages read (cover, pp.1–16 and 32–35)."
  - AR: «ولا يظهر تاريخ إصدار ولا اسم الإدارة المصدرة في الصفحات التي قُرئت (الغلاف والصفحات 1–16 و32–35).»
  - Alternatively, drop the department clause.

### S2. YSC-031 relevance line makes an unsourced general claim

- **Quote (L360):**
  > "Identity checks and onboarding are where account access is often lost"
  - AR: «موضعٌ يتعثر فيه الوصول إلى الحسابات كثيرًا»
- **Evidence:**
  - No source in the event supports "often".
  - MA-007 (`content/measurement_agenda.json`) treats where users abandon onboarding as an open question ("Where users abandon onboarding.").
- **Failure:** this is an analytical assertion presented as fact. It runs against the firewall rule that observed ≠ estimated.
- **Proposed wording:**
  - EN: "Identity checks and onboarding are a step at which account access can be lost; …"
  - AR: «التحقق من الهوية وإجراءات فتح الحساب مرحلةٌ قد يتعثر فيها الوصول إلى الحسابات؛ …»

### S3. In YSC-012, the new "In March 2024" is backed by the World Bank's value state

- **Quote (L407):**
  > " In March 2024 Circular No. 12 of the Central Bank of Yemen in Sana'a (13 March 2024, …"
  - AR: «وفي مارس 2024 حدّد التعميم رقم (12)…»
- **Evidence:**
  - `add_states` (L470-477) de-duplicates on (t, k).
  - The only "March 2024" state in YSC-012 is the existing one, with src SRC-WB-YEM-FRAGMENTATION-2025-001 (`visuals/system_chronology.json`, YSC-012 value_states[0]). That state is about the 100-rial coin.
- **Failure:** E2-DATES passes, but the date in the new sentence now traces to the wrong source. The phrase also duplicates the day dates in the parenthesis.
- **Proposed wording:** drop the lead phrase.
  - EN: " Circular No. 12 of the Central Bank of Yemen in Sana'a (13 March 2024, applying from 14 March 2024) set how…"
  - AR: « وحدّد التعميم رقم (12) الصادر عن البنك المركزي اليمني في صنعاء (13 مارس 2024، ويُعمل به من 14 مارس 2024) كيفية…»

### S4. `counts.py` writes a dated-events count that is wrong

- **Quote:**
  - `counts.py`: "dated events 23 -> 25";
  - the new checkpoint text: "25 dated events".
- **Evidence:**
  - `system_chronology.json` holds 30 rows, 29 of them not SYSTEM_INTERPRETATION. That is the count validate.py uses at L1827 and L4245.
  - "23" in OPENAI_REENTRY_CHECKPOINT.md has been stale since CLOSE-4: at commit 3e2f6c8e the chronology held 23 such rows.
  - After CLOSE-6B the true count is 31. The source counts (199 → 200; public locators 192 → 185) are correct.
- **Failure:** the first-read state document would carry a wrong inventory. P4-G01's regex looks for "chronology events", so it does not catch "dated events".
- **Fix:** derive the number, don't type it. Write "31 dated events" and say that CLOSE-4 added six.

### S5. R3 and R7 are cited as kept in `audit/close_out/addendum/` but are not there

- **Quote (L7):**
  > "The reads behind it (11 October 2026) are kept in audit/close_out/addendum/: R2 … R3 … R4 … R7"
- **Evidence:**
  - The repository folder holds only ARABIC_6A, R1, R2, R4, R6 and REDTEAM_6A.
  - `c6b/` holds a copy of R7 but no copy of R3.
- **Failure:** every C12, news/832, DOI, Quarterly Bulletin and withhold locator would point to a read that is not committed.
- **Fix:** commit `R3_cby_completions.md` and `R7_cby_instruments.md` in the same commit.

### S6. The citation-card change contradicts two recorded design rules

- **Evidence:**
  - `design/04_PAGE_FAMILY_COMPOSITIONS.md:119` says "citation cards by governed title".
  - `scripts/projection/derived.py:536` says "CITATION_CARD = governed bibliography only".
  - After the patch, any display-ready citation card with governed text prints "About this source" and "Does not establish". Today that affects only the 10 records in CARDS: no CITATION_CARD in the library carries text now (counted).
- **Failure:** the design and code record no longer match what is built. The definition of done for a slice requires the docs line to be updated.
- **Fix:**
  - Amend 04 §Data & Source: "citation cards by governed title, and, where the record carries it, its why-it-matters (under About this source) and boundary".
  - Amend the derived.py comment.
  - Record the change in `design/DESIGN_INTEGRATION_V1.md` or the change log.

---

## NIT

| # | Quote / location | Evidence | Proposed |
|---|---|---|---|
| N1 | L372 "p.1: ref. 840/CBY/2023, dated 9/11/2023 (25 Rabi' al-Akhir 1445)"; L436 "p.1: ref. 289/CBY/2024, dated 23/5/2024 (15 Dhu al-Qa'da 1445)" | R7: the e-KYC Hijri date is VERIFIED on p.16; Decision 19's issue line is on p.3 | "p.1 (ref., date); Hijri date p.16" and "…; Hijri date p.3" |
| N2 | L12 (YSC-012) asymmetry: "Circular No. 12 of the Central Bank of Yemen in Sana'a" against "CBY-Aden's Governor's Decision No. 19" | Neither form is loaded. Both are factual, and no causal verb is used (chronology ≠ causality holds). The double possessive is awkward. | Use parallel forms: "Circular No. 12 of 2024 of the Central Bank of Yemen in Sana'a … Decision No. 19 of 2024 of the Governor of the Central Bank of Yemen in Aden". In AR, the current forms are already parallel. |
| N3 | C12 titles: "Circular No. 12 of 2024 to all banks…" / «تعميم رقم (12) لسنة 2024 موجه…» | R3: the printed title is «تعميم رقم (12) موجه إلى كافة البنوك…»; "of 2024" / «لسنة 2024» is not printed | Acceptable as a descriptive title. If it is meant to read as verbatim, move the year into the parenthesis: "Circular No. 12 to all banks … (13 March 2024)" |
| N4 | L94 MFB hosting: "same text, earlier cover build" | R2 §S2: the DeepRoot cover's preparation line differs ("informed by input from the Development Champions Forum") | "pages 2–16 identical; the cover's preparation line differs" |
| N5 | L503-506 retired note: 'Its publisher line "DeepRoot Consulting" misstated the paper' | The MFB duplicate's publisher was "Sana'a Center Economic Unit, published by DeepRoot Consulting" | "Its publisher line, which named DeepRoot Consulting as publisher, misstated…" |
| N6 | e-KYC card and YSC-031: "providers report" / «ويُبلغ مقدمو الخدمة» | R7: the obligation falls on every «مؤسسة مالية», banks included; e-KYC also needs the CBY's prior written approval (Fourth, p.6) | "institutions using it report…" / «وتُبلغ المؤسسات التي تطبقها…». Optionally add "subject to CBY-Aden's prior approval" to the YSC-031 implication. |
| N7 | L36-37 docstring: "EUR 4.5 million belongs to phase III" | R4 Item 3 verdict: 4.5 million is also the phase I main measure | Add "(and phase I)". The undated card is still right. |
| N8 | `code_patch.py` L12-15: the first content.py pair has identical old and new strings | It is a no-op | Delete it |
| N9 | Withheld rows keep their unverified display fields (CURR-2024: the title "News item concerning…", the date 2024-06-04, the Saba publisher). The XIDIAN precedent nulls them. | `source_library.json` XIDIAN record | Null the display fields of the withheld rows, or have the note say they are unverified. They are masked publicly either way (`derived.py` L560). |
| N10 | AMB `does_not_establish` becomes a four-clause comma splice | Composed text (dry run) | "…or an independent assessment. It treats the Central Bank of Yemen as a single supervisor, without distinguishing the one in Aden from the one in Sana'a, and it does not show…" |
| N11 | L609 summary: "ten regulatory cards" | BANKS-BS-2022 is a "Statistical release", not in the regulatory group | "nine regulatory cards and one CBY statistical report" |
| N12 | L31 "linked to MA-007" | The link is text only (fi_relevance); 14_SYSTEM_CHRONOLOGY has no measurement-link field | Say "refers to MA-007". Consider `relationship_type` MEASUREMENT_CONTEXT. |
| N13 | The B5 gate has no negative control | `scripts/tests` has no B5 control. The logic is not vacuous: `_m` None → error; the count must equal the articles; cards plus links must equal `_nreg` (38 + 1 = 39 after the change) | Add a control that adds one `<article class="src source-locator" id="source-X">` to the group, and one that removes a `data-source-also` link |
| N14 | `families.py`: `if reg_n` now hides the group when every regulatory source is curated, even with also-links present | Edge case only | Use `if reg_n or page.get("regulatory_also")` |
| N15 | The SRC-ADEN-CBY-LIQ-2016 card prints its reference id, which reads as a CBY-Aden publication | The issuer now says "not a publication of the Central Bank of Yemen" | Keep the id stable; consider an alias later |
| N16 | CCY `publisher_ar` is still English | R4 1d: the cover prints «إتحاد المساعدات النقدية في اليمن» | A follow-up item, outside this transaction |

---

## Checks that hold (no finding)

- **The CBY-Aden instruments against R7.** These all match:
  - e-KYC: no effective-date clause; half-yearly reporting; Annex 5 average times; compliance periods.
  - Decision 7: header date 9/4/2026; Art.7 in force 12 April 2026; 18% on new rial savings deposits at commercial banks; FX and lending rates liberalised; Islamic banks exempt; Art.6 contracts after entry into force. The `value_states` hold 18% READ with a locator, and 7 TRIVIAL.
  - Circular 1/2024: Governor application, ceiling, minimum deposit period, SWIFT and credit advice.
  - Circular 2/2025: supplements 1/2012, 1/2013, 8/2014 and 2/2021.
  - Circular 3/2025: METAC.
  - Circular 4/2025: UN, OFAC, EU, HMT.
  - Circular 1/2026: in force from issue.
  - Decision 19: Art.1(a)/(b), Art.2 sub-agents and liability, Art.3 payout currency.
- **C12 dates.** 13 March 2024 (3/9/1445) and in force 14 March 2024 (4/9/1445) match R3. The host is correctly called a republishing news site, not the issuer. The §9 territorial clause is rightly not reproduced.
- **YSC-015 and news/832.** The fact matches R3 Item 1. The boundary correctly says no establishing decision is stated.
- **Firewall.**
  - Accounts ≠ people (BANKS-BS).
  - Rule ≠ implementation (every card, YSC-012/031/032).
  - Rule ≠ rate paid (YSC-032).
  - Issuance ≠ implementation (YSC-031).
  - No number is printed in a new card without a value state where E2 applies.
- **Withholds and merges.**
  - None of the 2 retired or 6 withheld ids appears in `public_object_source_closure.json`, `evidence/`, `page_specs.json`, readings or the chronology. They appear only in the library, the reference map, the search index (regenerated) and /data/. The Master's 32/33 rows that name them are internal.
  - Both canonical titles carry "Sana’a Center Economic Unit", as R2 requires. The DeepRoot publisher is corrected. EMONEY's document date becomes "2022-03" (R2: the PDF prints only March 2022).
  - The AMB authors match R4 Item 2: the FinDev page names the publisher, and no affiliation is printed. "Does not distinguish" CBY-Aden and CBY-Sana'a is verified (Aden 0, Sana 1 in references).
  - The CCY cover reading matches R4 1d.
  - The LIQ record matches the Crossref metadata in R3 Item 4, with issue 18 and end page 40 marked as inferred.
- **The /data/ count fix and B5.**
  - In the built page, the regulatory group is the first `source-locator-details`, so the next `<details class="source-locator-details` is the supporting group. Today the group holds 37 `<article class="src …" id="source-` plus 1 `data-source-also`.
  - After the change: 38 cards and 1 link, and `_nreg` = 39.
  - The new "about" `<details class="about">` does not collide with the slice terminator.
  - The printed count stays 38. No other /data/ text prints that count.
- **Decision 6.**
  - Not adding a grouped AML event is sound. Circulars 2/2025 and 4/2025, and 1/2026, change compliance duties rather than a dated access channel, and their cards carry the boundary.
  - Keeping KfW 47229 undated, and not printing EUR 4.5 million, is sound. The KfW page has no date, and the narrative sentence is reused across phases (R4).

VERDICT: HOLD — B1
