# Master-first patch narrative — Tranche B

**Status of every patch described here:** `VERIFIED_BY_CLAUDE_TEAM · SPEC_PENDING_EXECUTION · INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`. Arabic editorial rows also carry `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`. Rows that depend on an unread primary text also carry `PRIMARY_SOURCE_PENDING`. Nothing here is installed.

> The Master→projection generation pipeline is absent from the handed repository and must be recovered or deterministically rebuilt before semantic patch execution.

The spine is `audit/MASTER_FIRST_PATCH_SPEC.csv`. It has **994 rows under 394 patch roots**, in the 22 required columns. This document explains the grouped changes that the CSV alone cannot make safe. It adds no row the CSV does not contain.

## 0. How to execute the spec

1. **Export the Master read-only and rebuild the spec.** Run `audit/tranche_b_patch_tooling/export_master.py` on the Master. Then run `build_spec.py` to regenerate this CSV. The regenerated CSV is byte-identical to the one delivered; this was verified in this window. `simulate.py` then applies every patch to a copy and reports the checks listed in step 4.
2. **Execution order:**
   - P1 schema and generator rows (PB-0001–0008);
   - the per-object bindings (PB-0010–0069);
   - PB-0108 (the OECD fact registration), before or together with PB-0101–0106;
   - all other SUBSTR and CELL rows, in patch-ID order;
   - the terminology sweeps (PB-0413/0414/0415 `.Snnn` rows) **last**. Their before-text is the post-patch text.
   - Generator and build rows (op `GENERATOR_RULE`, `BUILD`, `SCHEMA`) are implemented when the pipeline is rebuilt.
3. **Row types:**
   - **SUBSTR rows** name an exact before-substring and after-substring. Where there are 12 cells or fewer, each cell gets its own row (`.01`, `.02` …, with its Excel row). Otherwise the locator lists every `sheet!row.field`.
   - **CELL / NEW / SCHEMA rows** name the sheet, object, field, current value and proposed value.
   - **An empty after-value is written `(DELETE — …)`.**
4. **Simulation result for this spec** (proposed-patch validation, not repository validation):
   - 0 builder errors and 0 collisions (no patch's before-text is consumed by an earlier patch).
   - 272 per-cell sweep edits, each with a before-text that occurs exactly once in its cell.
   - 0 residual forbidden strings in rendered or public-bearing fields, across 20 patterns.
   - 0 drawing-instruction summaries left in 06 or 11.
   - The only residuals are 7 strings in one non-rendered derived cell pair (02 r139 `full_copy_*`). They are resolved by PB-0472 regeneration.

## 1. Verification integrity — LEAD-B07 / LEAD-M06 (P1)

**Defect.** Every record gets a rendered "Source verification path". That path is the union of all sources on the record's route, not the sources of the record itself. Closure is also stamped `CLOSED_VIA_CONTROLLED_DEPENDENCIES` on 108/108 records, although 87 of them carry unresolved dependency IDs.

**Correction to the handover.** In the Master itself, `source_dependencies` is populated on 48 of the 108 objects. The projection drops it on all 108 (PB-0003). The handover's "empty 108/108" describes the projection only.

**Patch package:**

- **PB-0001 — new `lineage_state` field.** It takes one of five values: `BOUND_EXACT`, `BOUND_CANDIDATE__EXECUTION_CHECK`, `COMPOSITE_OF_OBJECTS`, `SOURCE_NOT_YET_BOUND` or `FRAMING_NO_FACT`.
- **PB-0002 — closure rules.**
  - `CLOSED_*` applies only when there are no unresolved IDs.
  - A dataset token resolves only to the rows the object uses, never to the whole dataset.
  - `NO_SOURCE_EXPECTED` is replaced by the lineage state.
- **PB-0003 — projection fidelity.**
- **PB-0004 / PB-0005 — build.py.** The trace renders only bound sources. `evidence_citation_context` stops using the route union.
- **PB-0006 / PB-0008 — reader copy.** Governed wording for the "unbound", "bound" and "composite" states.
- **PB-0007 / PB-0007A — boilerplate retired.** The producer boilerplate on 107 records is replaced by a per-record path. CLM-019 already has its own path.
- **PB-0010–0069 — object-level decisions for the 60 records with empty dependencies:**
  - **37 × BOUND_EXACT.** Examples:
    - the POS visuals bind only to the 11 monthly CBY-Aden releases (the value chart to the 10 that report value);
    - VIS-REMITTANCE-MACRO binds only to the two IMF documents;
    - VIS-REMITTANCE-COST binds only to the two RPW sources;
    - CLM-008 binds only to the 2026 CBY-Aden bank list.
  - **9 × BOUND_CANDIDATE.** The executor confirms each source against the object's own copy before binding.
  - **13 × COMPOSITE_OF_OBJECTS.** These are cross-domain syntheses. They cite their member objects, not a route union.
  - **1 × SOURCE_NOT_YET_BOUND** (VIS-PROVIDER-TIME). It is rendered as an open gap.
  - **The four known contaminations are removed:**
    - RPW corridor sources attached to the IMF chart;
    - IMF sources attached to the corridor-price chart;
    - 13 enforcement decisions attached to CLM-008;
    - the two BREAK_IN_SERIES publications attached to VIS-POS-TERMINALS.

**After execution:** the closure pass rate will fall. That fall is the honest number. Validation: every trace equals its bound list or states "composite" or "not yet bound".

## 2. The finance package — LEAD-B01 (re-severed BLOCKER → MATERIAL), LEAD-B02, LEAD-B03 (P2)

**Directive correction A applied.** The Tranche A/B plan converted the rial portfolio at the market exchange rate and called the result "FX-deflated −32%". That is a US-dollar conversion, not real deflation. No price deflator is sourced, and the evidence base does not record *which* rial valuation the portfolio uses across Yemen's divided monetary areas. **No real or USD change is therefore published.** The patches (PB-0120–0147) do three things:

- They keep the two nominal figures.
- They name the rate context: the CBY-Aden average market rate, 792.69 → 1,529.4 YER/USD, Dec-2020 → Dec-2023, from SRC-CBY-001. They state that neither a real nor a USD change can be derived.
- They preserve the lesson: nominal growth does not establish real deepening.

**"Sign reversal" withdrawn.** The handover called this a sign reversal. That claim is withdrawn: it depended on the unsupported conversion.

**"Active savers" is the source's term.** It is now quoted and attributed ("what it calls 3.3 million 'active savers'"). It is not shown to equal the 2020 "savers/depositors" measure.

**CLM-054 downgraded.** `BOUNDED_DIRECTIONAL_DIVERGENCE` becomes `SEPARATE_BOUNDED_ANCHORS` (PB-0131). The CWR-006 thesis is rewritten to match (PB-0135/0136). It no longer tells "a story of growth, deepening or divergence", and no longer asserts a borrower direction. The /readings/microfinance-structural-divergence/ slug is kept, for deep-link stability.

**Leaked authoring text removed (LEAD-B02):**
- PB-0150/0151 remove the chronology instruction shipped under /finance/.
- PB-0514–0516 remove a second leak found this window: "Present them as filterable or expandable items…" on /measurement/. The design requirement moves to a non-public 04_NAV_UX note.

**LEAD-B03 — formal credit (directive correction B applied).**
- PB-0160/0161 publish bank credit to the private sector — YER 1,350.4 billion, May 2026, CBY-Aden statistics — with its revaluation caveat.
- **No microfinance/bank-credit ratio is published.** PB-0162/0163 state why: twelve microfinance banks sit on the same bank list, so the two stocks may overlap. Valuation basis, date and institutional coverage also differ.
- The handover's "≈2.6%" is **rejected**.

## 3. OECD/INFE Yemen scores — LEAD-B08 (new BLOCKER) (P2, PRIMARY_SOURCE_PENDING)

**The problem.** The public copy says Yemen scored 15/100 on financial well-being and 42/100 on literacy. The project's own verification record could not confirm either score. "42" matches the genuine cross-country well-being average. The Master also labels the unconfirmed rows "Verified Yemen facts".

**The patches:**
- **PB-0101–0106.** The public copy now states only what is confirmed: Yemen was among the 39 economies, with data collected within a technical-assistance or regional project. It shows no score and no ranking.
- **PB-0107.** The eyebrow changes from "Current evidence" to "Evidence status".
- **PB-0108 — Master rows.** It adds `verification_state` per Master row. It also registers the confirmed participation fact as OECD-YEM-018, quoting the report's Introduction. That is the Master basis for the new sentence, so execute it first.
- **PB-0109 / PB-0110 / PB-0111 — non-public and deleted rows.**
  - PB-0109 marks the Annex D table and the diagnostic block NON-PUBLIC. The 60.5 "average" there contradicts the report's 60.
  - PB-0110 relabels the "Verbatim" item prompts as reconstructed.
  - PB-0111 deletes the two scores from the Master cover.
- **PB-0165/0166.** The OECD 2026 review figures are withheld, because the review text was not read.

## 4. Remittances evidence state and vintages — LEAD-B06 (P2)

- **The error.** The IMF's 2018–2024 values carry `HISTORICAL_REPORTED` with `SOURCE_REPORTED__IMF_STAFF_CALCULATIONS` in the Master. The public copy nevertheless calls them "observed history".
- **The fix.** PB-0170–0196 replace that label with "IMF-reported history (staff calculations)" / «تاريخ وفق تقديرات خبراء الصندوق». They state the two documents, and they break the line between 2024 and 2025 (the Article IV report versus its supplementary revision).
- **CLM-007** and the /remittances/ headings follow. The visual form becomes `…__VINTAGE_BREAK`.
- **Precision (LEAD-M04).** The six-significant-figure BOP value "US$3.42216 billion" becomes "about US$3.42 billion" wherever it is embedded (PB-0313–0315).

## 5. Authority scope and parity — LEAD-M01, LEAD-M02 (P2/P3)

- **CLM-008.** The English `does_not_prove` gains the authority-scope clause that the Arabic already carries (PB-0202). PB-0200/0201 replace the backend voice "The system controls a 26-row…" with "The current CBY-Aden list of licensed banks names 26 banks." The same bank-list change removes the calque «صفًا مصرفيًا».
- **Qualified authority references.** Every "official CBY roster" / «القائمة الرسمية للبنك المركزي» becomes CBY-Aden / «البنك المركزي اليمني – عدن» (PB-0210–0215, PB-0513).
- **New /providers/ section "Whose list is this?" (PB-0216).** It says:
  - the lists come from CBY-Aden instruments;
  - authority has been divided since 2016;
  - some listed banks have Sana'a or Taiz addresses in the source;
  - status under any other authority is not established here;
  - absence from the list does not mean unlicensed, and presence does not mean the provider can operate across all of Yemen.

  It is a scope statement, not a political one.
- **Per-row fields.** PB-0217 adds `issuing_authority` and `territorial_scope` per row.
- **YPCC Arabic name (PB-0230, PRIMARY_SOURCE_PENDING for the exact form).** «مركز اليمن للمقاصة» becomes «الشركة اليمنية للمدفوعات والمقاصة».

## 6. People-side evidence — LEAD-M05, LEAD-M04, LEAD-M03, MA-001 (P2/P4)

**/people/ and VIS-FINDEX-GAPS (PB-0300–0310, PB-0304/0305).** The copy now leads with the levels:
- 5.44% of women and 18.35% of men have an account — a 12.91-point difference;
- the income difference is about 9.0 points (15.5% vs 6.5%);
- 6.98% is reported as the account-ownership **level** for adults with primary education or less (`PARTIAL_HOLD_FOR_COMPLETE_PAIR`). No education gap is stated.
- The 3.37× ratio is not used.

The Reading visual RV-CWR-007 follows in both languages (PB-0436/0445/0449/0450).

**Directive correction C applied.** The handover wanted model-calculated SE, p-values, CIs and ratio intervals. They are **not published**. PB-0311/0312 state the survey-design limits accurately:
- the areas excluded from the sample hold about 23% of the population;
- more than a quarter of PSUs were replaced;
- no confidence intervals are held in the evidence base.

The ratio is dropped on presentation grounds (binding correction #6), not on a manufactured interval.

**MA-003 and the income gap.** MA-003 gains the measured income difference and keeps its causal firewall (PB-0320/0321). A new claim, **CLM-061** (PB-0322), publishes the income-group gap from FSG-0004 = `PUBLIC_SAME_WAVE_GAP_READY`.

**MA-001 remittance receipt (PB-0325–0330).** MA-001 now covers remittance receipt, channel and frequency, and binds /remittances/. Remittance receipt was last published for 2014. The 2021 microdata is held but not estimated. **No MA-011** is created.

## 7. Incompatible magnitudes and FMIIP baselines — LEAD-M10, LEAD-M08 (P4)

**Directive correction D applied: no adult denominator is imported.** PB-0345 adds a /evidence/compare/ section, "Three numbers that cannot be combined". It sets side by side:
- 11.9% — adults 15+ in the covered areas, 2021 wave;
- about 3.3 million — "active savers" as a secondary source calls them, 2023, relationships not people;
- 1,062,441 bank accounts and 375,252 e-wallet accounts — project baselines, Jan-2025, accounts not people.

It says they cannot be added, subtracted, ranked or converted, and that "not comparable" is the correct result.

**FMIIP baselines (PB-0340/0341).**
- They publish the project's Jan-2025 baselines as dated, project-defined observations: 817 access points (target 1,021), 1,062,441 accounts (200,898 owned by women), 375,252, 170 and 65. Each carries its firewall.
- **The zeros are not published.** They add nothing a reader can use, and publishing them invites the prohibited "baseline zero → no translation" reading (binding correction #3).
- PB-0342 moves the results framework to its own sheet. **Correction of a Lead error:** my earlier claim of "misaligned columns" was wrong. The block has its own title and header in rows 78–79; the change is for one-schema-per-sheet only.

## 8. Firms — LEAD-M12 (P2)

- **Multi-response stated (PB-0350/0351).** The copy now says respondents could name more than one challenge, so the shares add up to more than 100%. The base for the question is not held. Adjacent differences are not a ranking.
- **Visual contract changed (PB-0453–0457).** `RANKED_HORIZONTAL_BAR` becomes `HORIZONTAL_BAR__MULTI_RESPONSE__NO_RANK_NUMBERS`, and the multi-response note travels in both accessible summaries.
- **Tranche A over-claim withdrawn.** Tranche A's "access to finance ranks 6th" never reached public copy.

## 9. Arabic and English voice sweeps — LEAD-B05 (P3/P5)

**The Arabic noun for "claim" (PB-0413).** The workbook holds «ادعا…» 65 times in 62 cells. That count corrects my earlier 64/61, which missed the 07 sheet title.
- **41 are the governed-claim noun → «خلاصة / الخلاصات»:**
  - 39 by per-cell rows;
  - 1 by PB-0373 (/data/ count line);
  - 1 by PB-0413.T01 (the sheet title).
- **24 keep the ordinary sense "to assert"** («من دون ادعاء إثباته»، «لا يجوز الادعاء بأن»). Each is listed with its rule in `TERMINOLOGY_SWEEP_KEEP_REGISTER.csv`.
- **build.py strings:** PB-0413.B01–B03, and the strapline PB-0412, which is now governed in 04_NAV_UX.

**The product's Arabic self-referent (PB-0414).** «المنظومة» as the product's self-referent becomes **«المنصة»**. Because the word is feminine, every verb and pronoun agreement survives a one-word substitution; that is the reason it was chosen over «هذا المورد». There are 113 substitutions. The 49 financial-system uses are kept, each listed. build.py line 664, which renders 108 times, becomes «افتح سجل المصدر هنا…».

**The English self-referent (PB-0415).** "The system / the product / in the system" becomes "this resource / here": 122 substitutions. The 11 financial-system or financial-product uses are kept.

**Validation for all three sweeps:** the residual count equals the KEEP register (24/49/11, all matched in simulation).

## 10. Visual-contract voice and binding (P2/P3/P5)

- **English design instructions (PB-0430–0448).** In 19 Reading-visual fields the English is a drawing instruction ("Show…", "Place…") and renders on the Reading pages. Each is rewritten as reader prose carrying the Arabic meaning. RV-CWR-008's English gains the "seven-governorate" scope that the Arabic already states.
- **PB-0500–0512.** The same leak sits in the public `summary_en` of the 13 ungoverned VISUAL-class records.
- **PB-0460–0469, 0458/0459.** The 12 core visuals' `what_it_shows_en` (not rendered today) get the same treatment.
- **Trend verb removed (PB-0451/0452).** VIS-MFI-DIVERGENCE's "fell from" becomes anchor wording.
- **Binding (PB-0401/0402).** The 13 ungoverned VISUAL records become `NO_GOVERNED_CONTRACT__TABLE_ONLY` (no chart without a contract). The 24 governed pages receive their own contract and prohibited inferences.

## 11. IA — LEAD-M09 (P5), aligned to the accepted S01 decision

PB-0420–0424 execute Option B without route changes:
- "Evidence Readings";
- "Data & sources / البيانات والمصادر";
- the "Method & Measurement / المنهج والقياس" family, with **two equally weighted, always-visible children** (Methodology and Measurement Agenda) under a non-interactive family label;
- About in a visible Trust group.

The handover's variant, in which the family resolved to /methodology/, is **not** adopted; it would subordinate the Measurement Agenda, contrary to S01. The interaction contract is in `CLAUDE_TRANCHE_B_CLOSURE.md §4`.

## 12. Structural rules (P3)

- **PB-0470.** `02_SITE_MAP.full_copy_*` becomes a derived field: title plus the rendered sections. 03 is canonical for pages and 09 for Readings. Evidence: 257 of 282 cells are already derivable, and 25 diverge.
- **PB-0471.** Object text embedded in sections becomes generated from the owning object.
- **PB-0472.** Regenerates the divergent CWR-006 cell pair.

## 13. Trust, rights, search, cross-links (P2–P5)

**Trust and rights:**
- PB-0370/0371: /evidence/compare/ dimension parity, and "not comparable" as a valid result.
- PB-0372/0373: the {N_CLAIMS} count on /data/.
- PB-0374: `limitations` split into measurement limitation and prohibited inference.
- PB-0380–0390: /data/ rights promises made true, or withdrawn until the per-source rights and publisher schema exists. The 133 publisher proposals are in `SOURCE_PUBLISHER_PROPOSALS.csv`: 104 proposed, 29 unresolved.
- PB-0410/0411: per-language governed meta description; `*_internal` is never rendered.

**Search (PB-0490–0494):**
- all 159 sources indexed;
- boundaries indexed at low weight;
- EN stemming and AR normalisation;
- 12 governed discovery aliases, with the issuer-only alias rejected;
- domain pages rank first for their core term;
- document-type facet and state/date badges;
- 12 new smoke tests under a top-3 rule.

**Cross-links (PB-0426).** Domain→Reading links are set by the per-pair test. There are 11 surfaced and 8 contextual links; /providers/ gets none.

**Currentness (PB-0480/0481).** The consumer-protection instructions gain their reference and date: No. 589, 20 Aug 2023.


## 13A. Tranche A domain decisions carried into the spec (P3/P4)

Tranche A recorded these as `DECIDED_TARGET__TRANCHE_B` in `CLAUDE_FIELD_LEVEL_CHANGE_LEDGER.csv`. Each now has a Master-first row. In every case the wording is re-tested against the binding corrections.

**/firms/ — CHG-0014 → PB-0520.** A new section publishes the firm behavioural evidence from 20_FIRM_FINANCE:
- 58.2% of formal firms (191/328) hold an account;
- average working-capital shares are 69.12% internal, 16.66% lenders, friends or relatives, 10.15% client advances and 0.56% banks;
- 73.48% use money exchangers and 24.39% banks — multiple response, base not held;
- 80.18% of 217 informal firms hold no account (list-based sample).

**/payments/ — CHG-0017 → PB-0521.** A new section gives e-wallet subscribers: 414,631 → 507,585 → 581,075 for 2024 Q1–Q3, then 2,102,484 for 2025 H1. The break in the series is stated, never spliced. Subscribers are registrations, not people. The Findex 11.9% appears as a different question, not as a comparison.

**/access/ — CHG-0020 → PB-0522 and PB-0523.**
- **Wording.** Uses the binding-correction #4 wording ("official source lists document a substantial exchange and remittance provider presence relevant to the access question"). The Tranche A phrase "largest physical cash-access channel" is **rejected**.
- **Content.** The CBY-Aden roster (98/225/106, never summed), the 26-bank list, and FMIIP's 817 access points (target 1,021) — none of them presented as a map.
- **PB-0523.** Makes page-level prohibited inferences the union of the page's objects' boundaries.

**/finance/ — DOM-FIN-01 → PB-0524.** Provider structure: 12 of the 26 CBY-Aden-listed banks are microfinance banks, and the historical panels change in membership. /finance/ keeps its formal-finance and microfinance scope, so Tranche A's CHG-0015 "tighten to microfinance" is **rejected** (binding correction #2).

**/providers/ — CHG-0016 → PB-0525 and PB-0517.**
- The 14 dated CBY-Aden status events render as a dated table. Entity names are shown only where the source state is primary.
- PB-0517 moves the status-event block (rows 71–86, own header in row 72) to `22B_PROVIDER_STATUS_EVENTS`, the same one-schema-per-sheet fix as PB-0342.

**Decision 18/2026 — CHG-0009 → PB-0518 and PB-0519** (`PRIMARY_SOURCE_PENDING` for the entity names). The source card and status event are added. The event is verified at cby-ye.com/news/975; the names are withheld until the signed text is transcribed.

**/reforms/ — CHG-0019 (baseline-zero ladder): REJECTED.** Binding correction #3 forbids it. The non-zero FMIIP baselines are published instead (§7).

**/remittances/ — CHG-0018.**
- The Measurement node is resolved by extending MA-001 (§6).
- The proposed reordering to "lead with the household thread" is **rejected**. The only household section is a 2014 domestic-remittance profile, and moving it to the top of the page would invite readers to take 12-year-old evidence as current. The page keeps its order; MA-001 and the /evidence/compare/ section state the household gap.

**/people/ — SYS-04 → PB-0526.** The Arabic title now carries the English title's thesis instead of asking a different question.

## 13B. Methodology completeness, parity closure and independent-verifier fixes (P3–P5)

**Methodology (PB-0611–0614).** Four one-paragraph sections are added to /methodology/, bilingual, with every number traced to the Master:
- what the evidence covers and what it does not (from `INDICATOR_COVERAGE_MATRIX.csv`);
- how evidence is admitted and in what role;
- measuring in a divided, conflict-affected setting;
- uncertainty is stated, not manufactured.

**Indicator library (PB-0615).** The 17_INDICATOR_LIBRARY description is corrected. It is a catalogue that indexes the data sheets, not a table of values (addendum §17).

**Parity and invariance (PB-0527–0529, 0560–0577, 0590–0595, 0195A).** A numeric-invariance test ran across 750+ EN/AR field pairs; mismatches fall from 46 to 22, and all 22 are reviewed. It found:
- the Arabic CLM-031 missing its thesis;
- 12 placeholder English universes;
- undated English titles on 2014 records;
- the CWR-007 thesis leading with the gap;
- the Arabic calque «الكون»;
- a remaining «الموثقة» on the Arabic CLM-007 variant.

**Independent verifier 2 (all findings fixed; `TRANCHE_B_RED_TEAM.md` §5):**
- the 91.84% base now states its no-need exclusion in both languages (PB-0583/0584, 0583A–E);
- the Arabic multi-response sum now says the shares **exceed** 100% (PB-0351/0456);
- CBY-Aden now appears in both languages (PB-0580A/0581A/0585A);
- the 817/1,021 pairing is on both the record and the visual (PB-0594/0595);
- heading over-generalisations removed (PB-0520/0522);
- the status-event guard and fields (PB-0519/0525);
- the search document-type and evidence-role columns (PB-0493);
- the block count (PB-0473: 31);
- classification corrections (dates, authority, base and titles are now `semantic=yes`).

**Titled blocks: no sheet moves.** The Master deliberately keeps titled blocks with their own headers inside sheets. PB-0342 and PB-0517 therefore become reader rules under PB-0473; no sheets are moved.

## 14. What is deliberately not in the spec

These are covered by `TRANCHE_B_RED_TEAM.md §4` and `TRANCHE_B_UNRESOLVED_QUEUE.md`:
- any USD or real microfinance change;
- the microfinance/credit ratio;
- model-calculated SE/p/CI and the ratio interval;
- an adult denominator;
- FMIIP zero indicators;
- MA-011;
- mechanical domain→Reading population;
- the issuer-only search alias;
- Decision 18/2026 entity names;
- the OECD/INFE Yemen scores;
- any §23 forbidden object.
