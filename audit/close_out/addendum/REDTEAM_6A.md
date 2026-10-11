# Red-team review: CLOSE-6A draft

- **Draft reviewed:** `scratchpad/addendum/review/close_6a_draft.py`, timestamp 06:11. It is byte-identical to the untracked `audit/close_out/close_6a.py`.
- **Working copy:** `scratchpad/wk6a/audit/close_out/close_6a.py`, timestamp 06:16. It differs from the draft only by two "September 2022" value states (see B4).
- **Evidence I used:**
  - reads R1, R2, R4 and R6;
  - the WDI snapshot in `addendum/dl/wdi/`;
  - the MICS text in `addendum/txt/mics.txt`;
  - the current projections under `site-src/content/`;
  - the dry-run build and logs in `scratchpad/wk6a/` and `scratchpad/wk6alogs/`.

Line numbers (`L…`) refer to the draft. Nothing under the repository was modified.

---

## BLOCKER

### B1. CR-21 misses one form of the date, so day-precise fieldwork dates stay public

- **What the draft does.** `CR21_PHRASES` (L282-287) matches only the "to"/"إلى" forms and the ISO form.
- **What it misses.** The 08_READINGS `evidence_period` of the gender-gap reading uses an en dash:
  - `"Global Findex, Yemen fieldwork 7 November 2022 – 9 January 2023"`
  - `"مسح Findex العالمي، العمل الميداني في اليمن 7 نوفمبر 2022 – 9 يناير 2023"`
- **Evidence:**
  - `site-src/content/content/readings.json:535-536`.
  - The dry-run build still prints the day-precise period on `/en|ar/people/`, `/readings/`, `/readings/gender-gap-measured-causes-open/` and `/readings/reforms-newer-than-people-evidence/`. Running grep on the `wk6a/dist` HTML for "9 January 2023" or "9 يناير 2023" returns those pages plus CLM-023.
  - A scan of every content JSON finds no other uncovered variant.
- **Why no gate catches it.** The `changed < 100` guard passes, and E2-DATES passes because the day states stay in the records as provenance. The failure is silent.
- **A knock-on error.** The new CLM-023 note says "elsewhere this resource gives the period as November 2022 to January 2023". That would be false.
- **Fix:**
  - Add `("7 November 2022 – 9 January 2023", "November 2022 – January 2023")` and `("7 نوفمبر 2022 – 9 يناير 2023", "نوفمبر 2022 – يناير 2023")`. This matches the featured reading's existing style, "Global Findex fieldwork November 2022 – January 2023".
  - Add a post-condition: outside CLM-023 `method_*`, the skipped columns and `value_states`, no cell may contain "9 January 2023", "9 يناير 2023" or "2023-01-09".

### B2. FAS-YEM-2015 calls depositors "access points" (firewall: access ≠ use)

- **The strings:**
  - `title_en` "Access points per adult: the IMF Financial Access Survey's last values for Yemen (2015)" (L106);
  - `summary_en` "…these are dated historical values, not a current measure of access" (L111);
  - `meta_en` "…dated history, not access today" (L156).
- **The problem:**
  - Depositors with commercial banks per 1,000 adults (FB.CBK.DPTR.P3) counts depositors. That is use or ownership, not an access point.
  - The title's unit "per adult" is also wrong. The series are per 100,000 and per 1,000 adults (WDI indicator names in `dl/wdi/data_*.json`).
  - The record's own limitations already separate the two ideas ("a count of depositors is not a count of unique people with an account").
- **Fix, title:** "Bank branches, ATMs and depositors: the last values the World Development Indicators publish for Yemen from the IMF Financial Access Survey (2015)".
- **Fix, summary and meta ending:** "…these are dated historical values, not a current measure of access to, or use of, financial services."
- **Fix, MA-005.** The transaction already edits MA-005 for 1.5, so make the same change there (`current_evidence_en`: "…not a current measure of access") and in Arabic.

### B3. The Arabic FAS text fails validate ("backend Arabic public leak المقام")

- **The strings:**
  - `universe_ar` "…بالمقامات السكانية التي يستخدمها صندوق النقد الدولي…" (L125);
  - `limitations_ar` "ومقاماتها السكانية هي مقامات صندوق النقد الدولي" (L137).
- **Evidence:**
  - `wk6alogs/validate.log`: "HTML=298 ERRORS=2 … FAIL backend Arabic public leak المقام in …/ar/evidence/FAS-YEM-2015/ … and …/ar/measurement/".
  - The banned term is at `scripts/validate.py:68`.
- **Fix:** use the term MA-005 already uses, "قواعد الاحتساب السكانية":
  - `universe_ar` "…بقواعد الاحتساب السكانية التي يعتمدها صندوق النقد الدولي…"
  - `limitations_ar` "…وقواعد الاحتساب السكانية فيها هي التي يعتمدها الصندوق؛…"
  - The English is unchanged: "population denominators".

### B4. Two dates in the draft have no value state, so E2-DATES fails

- **The strings:**
  - MICS `period_en` and `period_ar` "July–September 2022 …" (L176-177). The gate reads this as 2022-09.
  - YMPS "August–September 2022" in `title`, `summary`, `period` and `currentness`.
- **Evidence:** `scripts/validate.py` `_e2_dates` matches "September 2022". The MICS states (L202-206) hold only "May 2023", and the YMPS states (L251-256) hold no 2022 date.
- **Fix:** the working copy in `wk6a` already adds both states (`vs("September 2022", "d", "READ", MICS_SRC, "…section 5.17, printed p.5…")` and `vs("September 2022", "d", "READ", YMPS_SRC, "catalog 5999, Dates of Data Collection: 2022-08 to 2022-09")`). Run that copy, not the review draft.

---

## SHOULD-FIX

### S1. The MA-003 binding contradicts the priority's own text

- **The string:** MA-003 `current_evidence_en` "Comparable current differences by age group and displacement status are not established in the evidence base".
- **The contradiction:** bound record VIS-FINDEX-GAPS reports, from the same wave, "5.0% of adults aged 15–24 and 16.1% of those aged 25 and over, a difference of 11.1 percentage points". It also reports an education gap of 12.5 points.
- **Fix:** "…Within the same wave, account ownership also differs by 11.1 percentage points between adults aged 15–24 (5.0%) and those aged 25 and over (16.1%). Comparable differences by displacement status, and finer age groups, are not established in the evidence base…" Change `priority_basis` to match.

### S2. MA-001 does not bind the record behind "also by group (shown on /people/)"

- **The string:** "…17.7% … sent them and 31.9% received them, also by group (shown on /people/)".
- **The gap:** the by-group values are in VIS-FINDEX-FLOW-CHANNELS ("The table gives each share by sex, age, education, income and labour-force status"). CLM-026 holds only the totals.
- **Fix:** add `VIS-FINDEX-FLOW-CHANNELS` to the MA-001 evidence bindings.

### S3. MA-005 binds one unsupported record and misses one supporting record

- **The string:** "Current official rosters establish selected listing, licensing and event states".
- **Missing record:** "event states" are held by CLM-019 ("Enforcement decisions are events, not a market census"), which is not bound.
- **Unsupported record:** XW-FMIIP-005 (the FMIIP target is not comparable) supports no sentence of MA-005's current evidence.
- **Fix:** bind `CLM-019`. Drop `XW-FMIIP-005`, or add a sentence that uses it.

### S4. MA-007's "KYC … rules are documented" has no binding

- **The gap:** neither CLM-012 nor VIS-E-MONEY-RULE-STACK mentions KYC (checked by grep). The library holds `SRC-CBY-EKYC-2023`, the e-KYC instructions of 9 November 2023 (ref. 840/CBY/2023), which no record uses.
- **Fix:** set MA-007 `source_bindings` to `["SRC-CBY-EKYC-2023"]`.
- **A caution:** R2 §8 says the e-KYC file was not opened. To keep the claim to existence only, consider "CBY-Aden's e-money rules and its 2023 electronic know-your-customer instructions are documented, but…".

### S5. MA-008 left unbound: consistent, but its text claims knowledge the resource does not hold

- **The strings:**
  - `priority_basis_en` "…because legal/institutional existence is known…";
  - `current_evidence_en` "…are not yet documented as one complete evidence chain" (which implies partial documentation).
- **The gap:** no evidence record and no source in `source_library.json` concerns a credit bureau, credit information or a collateral registry (grep found nothing). Leaving MA-008 unbound is right only if the text stops asserting that knowledge.
- **Fix, `priority_basis_en`:** "P1 … because this resource holds no evidence on whether credit-information or collateral infrastructure reaches lending decisions."
- **Fix, current evidence:** "…Legal texts, project documents and institutional records could establish whether credit infrastructure exists; this resource holds none of them, and no current measure of its reach or use."
- **The alternative:** read the CBY-Aden credit-information circular (listed on cby-ye.com, R2 §7) and bind it.

### S6. The FAS title and meta are scoped to the IMF, but only WDI was checked

- **The strings:**
  - title "…the IMF Financial Access Survey's last values for Yemen (2015)";
  - `meta_en` "The IMF Financial Access Survey's last values for Yemen, 2015".
- **The gap:** only the WDI API was read. The IMF's own FAS database was not checked for later Yemen years.
- **Fix:** "…as published in the World Development Indicators" (see B2), or check data.imf.org.

### S7. The FAS rounded values are stated READ; they are DERIVED

- **The strings:** `vs("5.81", "v", "READ", …)`, `vs("1.5", …"READ"…)` and `vs("103.1", …"READ"…)` (L150-152).
- **Why it matters:** the API holds 5.80977…, 1.47559… and 103.0546…. The rounded figures are computed, and the method says so ("rounded half up").
  - E2-7 defines DERIVED as "computed from values read there".
  - CLOSE-3D, whose rule the docstring cites, used `"DERIVED"` for the same operation (`close_3d.py:350`).
- **Fix:** state `"DERIVED"` and keep the locators.
- **The 1.5 decision itself is sound.** The API `decimal` field is 1 for FB.CBK.BRCH.P5 and FB.CBK.DPTR.P3 and 2 for FB.ATM.TOTL.P5. Rounding half up gives 5.81, 1.5 and 103.1. No other cell prints 1.48.

### S8. The FAS locator cites a fixture that does not exist

- **The string:** `FAS_LOC` "…; audit/close_out/fixtures/wdi_fas_yem_2026-10-11.json" (L98-99).
- **Evidence:** `audit/close_out/fixtures/` holds only findex_api, findex_rural_urban and wdi_rmt_cost. The snapshot exists only as six files in `scratchpad/addendum/dl/wdi/`.
- **The same applies to the reads.** The docstring says reads R1, R2, R4 and R6 are "kept in audit/close_out/addendum/", which does not exist.
- **Fix:** commit the fixture, built from `dl/wdi/data_*.json`, and the reads before running.

### S9. The MICS title overclaims "not tabulated"

- **The string:** `title_en` "MICS 2022–2023: one household question on bank accounts, not tabulated".
- **The gap:** R6 2e verified only that the item is not found in the findings report's extracted text. The microdata could be tabulated.
- **Fix:** "MICS 2022–2023: one household question on bank accounts, not tabulated in its findings report".
- **Also in `method_en`:** change "No results table of the report uses the item" to "A text search of the report finds the item only in the questionnaire."

### S10. The MICS record says "one question on finance", but the survey also asks about cash transfers

- **The string:** "Its household questionnaire asks one question on finance…". The Arabic reads "…عن الخدمات المالية".
- **The gap:** the household questionnaire's Social Transfers module asks about receipt of the "UNICEF/WB SUPPORTED EMERGENCY CASH TRANSFER" (ST1-ST4, printed p.331). The report tabulates coverage in Tables EQ.2.5-EQ.2.7 (`txt/mics.txt` around lines 407 and 19758). A reader may count that as finance.
- **Fix, EN:** "…asks one question on financial accounts, whether any member of the household has a bank account (item HC19)…"
- **Fix, AR:** "…سؤالًا واحدًا عن الحسابات المالية…"
- **Optional:** note that receipt of the emergency cash transfer is asked and tabulated, without the payment channel, and bind the record to MA-009.

### S11. The MICS record lacks a limitation on its split fieldwork

- **The gap:** the two hubs were fielded six months apart, and five governorates were collected partly by each hub.
- **Evidence:** R6 2c, section 5.17: "Since the data collection was conducted at different periods in Aden and Sana'a hubs, effects of seasonality on some indicators … may vary across the governorates." Footnote 6: "Data collected partly from Aden and Sana'a hubs."
- **Fix, add to `limitations_en`:** "The two halves of the sample were fielded six months apart (July–September 2022 and January–May 2023), with five governorates collected partly by each hub, so any tabulation of the item would mix periods across areas."

### S12. The YMPS response rate is described as something the source does not say, and the limitation overclaims

- **The strings:**
  - `universe_en` "…about 28 percent of those contacted completed the interview";
  - `limitations_en` "…a survey that about 28 percent of those contacted completed does not represent all of them".
- **Evidence:** R6 1a: "…resulting in a response rate of around 28 percent". The denominator is not defined. R6 also gives a "Deviations" quote that the record omits: "Some governorate quotas were not achieved…"
- **Fix, `universe_en`:** "…; the catalogue reports a response rate of around 28 percent."
- **Fix, `limitations_en`:** "Adults with mobile phones are not all adults; with a response rate of around 28 percent, and some governorate quotas not achieved, respondents may not represent all adults with mobile phones; …"
- **Arabic:** make the same changes.

### S13. YMPS "18" governorates has no locator

- **The string:** `limitations_en` "…the catalogue's sampling text names 18 governorates while its abstract says 21".
- **The gap:** the only "18" state (L252) locates "18 years of age and older". The literal audit passes by substring match, so the gap is silent.
- **Fix:** add or extend a state for "18": Sampling > Sampling Procedure, which lists 18 governorate names (R6 1a). Mark it DERIVED, because it is a count of names.

### S14. "De facto authorities" expands an abbreviation the catalogue does not expand

- **The string:** "records each respondent's area of control, the internationally recognized government or the de facto authorities" (L215-217; also in MA-001).
- **Is it fair? Yes, in substance.** It is the neutral UN term, and the site already uses it (CLM-027, citing ACAPS).
- **The gap:** R6 1d: "the abbreviation 'DFA' is not expanded anywhere on the fetched pages (I did not infer 'de facto authorities')". The catalogue also carries a five-category `sec1_dom_act` ("Dominant actor").
- **Fix:** "…records each respondent's area of control, coded as the internationally recognized government or 'DFA', which this resource reads as the de facto authorities (the catalogue does not expand the abbreviation)." Alternatively, cite the World Bank report (openknowledge 10986/40265) after checking it.

### S15. The YMPS Arabic meta adds "about" (نحو) to 1,297

- **The strings:** `meta_ar` "…عام 2022 نحو 1,297 بالغًا…" (L258), against `meta_en` "interviewed 1,297 adults". Numbers must not drift between the two languages.
- **Fix:** "قابل مسح الهاتف المحمول للبنك الدولي عام 2022 ‏1,297 بالغًا يملكون هواتف محمولة…"

### S16. The e-money history implies operation, and may imply an e-money change in 2022 that is not verified

1. **"Opened e-money provision" (firewall: licence ≠ operation).**
   - The string: "…the Central Bank of Yemen in Sana'a opened e-money provision to non-bank institutions from March 2020…" (L360). The Arabic reads "فتح … باب تقديم النقود الإلكترونية".
   - Evidence: the paper (p.18) says the directive "expanded the scope of … eligible to obtain a license" and "paved the way". R2 p.30 records that ONE Cash was licensed but had not launched as of March 2022.
   - Fix: "…opened e-money licensing to non-bank institutions from March 2020…"; AR "…فتح باب الترخيص لإصدار النقود الإلكترونية أمام مؤسسات غير مصرفية…".
2. **The 14 September 2022 sentence.**
   - The string: "CBY-Aden's own instructions of 14 September 2022 then defined payment service providers as non-bank financial institutions licensed by the central bank."
   - The risk: after "kept the pre-war, bank-led framework", readers will take this as the end of bank-led e-money. R2 §8 says whether these instructions cover e-money issuance is "NOT VERIFIED" (pp.6-33 unread). The record's own summary already says it is the 9 August 2023 instructions that "regulate e-money services of non-bank financial institutions". The advisor's "until its own 2023 instructions" may therefore be right for e-money.
   - Fix: "…while CBY-Aden, as of the paper's writing, kept the pre-war, bank-led framework. CBY-Aden later issued instructions for payment service providers, which it defines as non-bank financial institutions licensed by the central bank (14 September 2022), and the e-money instructions of 9 August 2023 described above."

### S17. CLM-012: a central bank does not administer areas

- **The string:** "…not those the Central Bank of Yemen in Sana'a has issued for the areas it administers." The Arabic reads "للمناطق التي يديرها".
- **Fix:** "…and these are CBY-Aden's rules, not those the Central Bank of Yemen in Sana'a has issued." If scope is needed, cite the paper (p.18): those measures "only pertain to" areas under the Sana'a-based authorities.

### S18. CLM-039 calls one publication's inconsistency "publications differ", and the Arabic inverts the quote

- **The string:** "The World Bank's own publications also differ on Yemen: the note to Figure A.4.2 … says Yemen is excluded … while panel (a) of the same figure shows a value for Yemen for 2023".
- **What R1 shows:** this is one figure in one publication. Yemen is absent from panel (b) (% of GDP). The asterisk sits on both panel subtitles. The note's intended scope is "NOT VERIFIED" (R1 B2). As drafted, the sentence hides the benign reading.
- **Fix, EN:** "One World Bank publication is also inconsistent on Yemen: the note to Figure A.4.2 of Migration and Development Brief 40 (June 2024) says Yemen is excluded "due to data availability", yet panel (a), remittances in US dollars for 2023, shows a value for Yemen, and only panel (b), remittances as a share of GDP, omits it. The brief does not say which panel the note applies to, and this resource takes no value from the figure."
- **The Arabic problem:** «بسبب توفر البيانات» reads literally as "because data are available", the opposite of the intended sense.
- **Fix, AR:** «لأسباب تتعلق بتوفر البيانات» (or add "(due to data availability)" in English).

### S19. CWR-010 s6 (CCY): the dates imply the limits ended, and "recipients" ties the finding to the wrong programme

1. **Dates.**
   - The string: "…it reports that from late February to mid-May 2026 banks and currency exchangers … limited rial withdrawals and currency exchange."
   - Evidence (R4 1a): exchange limits start "In February" / "By late February". The YER 80,000/day withdrawal cap applies "Since late April". "Mid-May" appears only in the un-footnoted Key Takeaways, after the data window (survey 26 April–3 May). The Conclusion speaks of "Continued caps".
   - Fix: "…it reports that from late February 2026 currency exchangers and banks in areas administered by the internationally recognized government limited currency exchange and, from late April, rial withdrawals; its summary gives the period as late February to mid-May, and it does not report the limits ending."
2. **"Recipients."**
   - The string: "not a measure of how many recipients were affected".
   - The problem: in this reading "recipients" means the transfer programme's recipients, and s6 itself says that programme has run no payment cycle since January 2025. The report concerns the general public and multi-purpose cash beneficiaries.
   - Fix: "…not a measure of how many people were affected".
3. **Cause.**
   - The string: "the report does not establish its cause".
   - The problem: the report's title and text attribute the crisis to the regional conflict and to cash hoarding (R4 1b), so this wording reads as a contradiction of the source.
   - Fix: "…and the report attributes it to the regional conflict and to cash hoarding without testing that explanation."
4. **The reading's clock.**
   - The gap: CWR-010 `evidence_period_en` still reads "Cash Consortium of Yemen study (2026) and World Bank project documents (2025–2026)" (dry run, `wk6a` readings.json).
   - Fix: "…Cash Consortium of Yemen study (2026) and report (May 2026) and World Bank project documents (2025–2026)", with the Arabic to match.

### S20. CR-22 says intervals ignore clustering but not what that means

- **The string:** "…so these intervals do not reflect clustering;".
- **The gap:** R1 A3 footnote b and R1's note: the 1.9 is a weights-only design effect for a clustered sample. A reader is not told the direction of the effect.
- **Fix:** "…so these intervals leave out the extra uncertainty that clustering usually adds and may be narrower than the true sampling uncertainty;".
- **Also:** split the 70-word sentence into two.

### S21. VIS-INCLUSION-TRANSMISSION as FRAMING_NO_FACT conflicts with the record's own wording

- **The conflict:** the governed framing text says "…It does not report a figure from a source, so there is no original source to check." But the record says relationships are "documented … where evidence supports them" (summary) and "Compiled from the relationships between system parts documented in this resource's evidence base" (method).
- **The other four are honest.** VIS-SOURCE-COMPARISON, VIS-MECHANISM-METRIC-BRIDGE, VIS-EVIDENCE-CLASS-LADDER and VIS-EVIDENCE-GAPS are rules or typologies. They print no figure (checked on the built `/evidence/`, `/evidence/compare/` and `/measurement/`).
- **Fix:** either keep it COMPOSITE and list the records behind each relationship, or reword its summary and method as a reading frame. Suggested method: "A reading frame that names the parts of the system and the kinds of relationship to look for (context, dependency, plausible mechanism); each relationship must be checked in the evidence records of the parts it joins."

### S22. The VIS-PROVIDER-OBSERVABILITY members omit the source for its microfinance claim

- **The string:** "Non-bank microfinance institutions: the evidence base holds only network membership pages, not a licensing list."
- **The gap:** none of the listed members (CLM-008, 055, 009, 019, 010, 015) holds that claim. It rests on `SRC-YMN-MEMBERS-2026-001` ("Yemen Microfinance Network website: membership pages").
- **Fix:** append `SRC-YMN-MEMBERS-2026-001` to the members.
- **The rest of the list fits the text:**
  - DS-DEMAND-VINTAGE-LENS = the VIS-DEMAND-VINTAGE-LADDER list. Adding CLM-026 is right, since it holds 21.6%, 51.3% and 9.3%.
  - CLM-014 = VIS-EVIDENCE-FRESHNESS's 37 members exactly.
  - VIS-MFI-DIVERGENCE with MFI-SPINE-2015-Q4 holds 509,590 and YER 6.741 bn.
  - VIS-ACCESS-EVIDENCE-LAYER fits.

---

## NIT

1. **CR-22 English drops "because".** "…does not incorporate intraclass correlation, which varies by question" drops the source's causal "because they vary by question". The Arabic "لأنه يختلف" keeps it. Fix: "…does not incorporate intraclass correlation, because it varies by question…"
2. **MICS "41" has no denominator.** Fix: "41 of the 880 selected enumeration areas". R6 2b: "target sample size … 880 clusters".
3. **MICS implementer: the two languages differ.** EN "of the Central Statistical Organization and UNICEF"; AR "أجراه الجهاز المركزي للإحصاء بدعم من اليونيسف". The report says "carried out … by the Central Statistical Organization Yemen … Technical and financial support were provided by … UNICEF" (`mics.txt` line 12). Fix EN: "…carried out by the Central Statistical Organization with technical and financial support from UNICEF".
4. **YMPS "their three most important sources of income".** The catalogue label ("Can you rank the three most important source?") does not say whether the income is the respondent's or the household's. Fix: "…to rank the three most important sources of income".
5. **YMPS already asks about financial aid.** It asks "Did you recieve any financial aid?" (`sec4_q02_2a`, R6 1e), which bears directly on MA-009. Consider adding: "It also asks whether the respondent received any financial aid, but not how it was received or used."
6. **YMPS currentness does not say whether later rounds were checked.** Fix: "Round I … ; whether later rounds have been published was not checked."
7. **E-money "11" is stated TRIVIAL.** The circular number comes from the source. By analogy with CLM-012's `'4'` (READ), state it as READ, Sana'a paper p.12.
8. **CLM-023 note: name which date differs.** Fix: "…differ by one day on the end date:…".
9. **CWR-010: two CCY items in one paragraph.** Fix: "The third, a separate May 2026 report by the Cash Consortium of Yemen,…".
10. **VIS-ACCESS-EVIDENCE-LAYER `data_inputs` could add members.** "payment-infrastructure totals" lists only POS (CLM-003). ATM totals are in VIS-PAYMENT-ANATOMY, and `/access/` also shows CLM-050 (807,919 accounts; 23% dormant). Consider adding both.
11. **Source library retrieval date.** `source_library.json` gives SRC-WB-WDI-FAS-YEM-001 `retrieval_date` 2026-10-10, while the record says "as fetched on 11 October 2026". Align them.

---

## Checked and found sound

- **WDI values.** 5.80977836621394 rounds to 5.81 (decimal 2); 1.47559111890891 to 1.5 (decimal 1); 103.054647215096 to 103.1 (decimal 1). `lastupdated` is 2026-10-08, and Yemen has no value after 2015 in any of the three series.
- **MICS facts against R6.** 22 governorates, 41 enumeration areas, HC19 at printed p.330, sections 5.12 and 5.17, and the hub periods all match. I confirmed in `mics.txt` that the report contains no "borrow", "loan", "credit" or "mobile money" and no saving item.
- **YMPS facts against R6.** 1,297, aged 18 and over, 21 governorates, about 28% and August–September 2022 all match.
- **CR-21 at month precision is safe.** Both World Bank records agree on November 2022 and January 2023. CLM-023's 9 January (catalogue 5862) and 10 January (Table A.1, printed p.17) match R1. Fix B1 first.
- **CR-22 against R1.** The quotations from note b and "approximately 23% of the population" are accurate.
- **CLM-039.** The advisor's "corroboration" is rightly rejected, and no value is taken from the figure.
- **Naming.** "the Central Bank of Yemen in Sana'a" and "CBY-Aden" are used neutrally throughout.
- **MA-002, MA-004, MA-006, MA-009 and MA-010.** Each bound record supports its priority's text.
- **The rest of the dry run.** All other gates in `wk6alogs` pass, including literals (`unresolved=0`).
