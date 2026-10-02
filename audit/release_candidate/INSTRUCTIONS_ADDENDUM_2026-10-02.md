════════ PART 2 — BEGIN OWNER ADDENDUM 2 (2 October 2026) ════════

OWNER ADDENDUM 2. This adds to the release-candidate brief in audit/release_candidate/INSTRUCTIONS.md; it does not replace it.

WHERE IT FITS
- A1 and A2 below are release defects.
  - If Part A is not yet complete, do them before PART A COMPLETE.
  - If Part A is already complete, do them first in Part B.
- Everything else belongs to Part B.
  - Where an item extends a brief item (B5, B9, B12, B13, B14e, B15d), do it there.
  - The rest goes inside B15d, in value order.
- The owner designates you to author the governed copy these items need, in both languages, under the Part B designation rules of the brief. This includes A2.
- These are findings from an owner-side review of main at 38a9a97.
  - Verify each on the built site before acting.
  - If one is already fixed or wrong, say so and skip it.
- Do not duplicate work the brief already assigns.

1. THE PUBLIC VALUE RULE
Something new goes public only if all seven hold:
- T: it is true and source-traced.
- V: a named user gains something distinct.
- F: it is in its best form (sentence, link, table or drawing, whichever carries the truth with least effort).
- S: its boundary survives a screenshot or a crop.
- X: it adds no needless complexity.
- G: it survives the design challenge inside the accepted D7 design.
- K: if it were deleted tomorrow, someone specific would miss it.

If any one fails, do not build it; record why.

New facts enter only through the Master-first path under owner rules 1–3, read in the original. They never come from press, summaries or other aggregators.

2. THE RED TEAM (hostile but fair)
Each member attacks from their own expertise and may block only for a stated reason of truth, safety, accessibility or governance.
- A Central Bank of Yemen – Aden payments-supervision director. Checks every instrument's number, date and issuer, and that no rule is described as implemented without evidence.
- A compliance officer at a licensed exchange company in Aden or Sana'a. Checks that nothing implies their firm is unlicensed, suspended or reinstated beyond what a decision says.
- The World Bank FMIIP task-team leader. Checks target ≠ result and project definitions.
- A Global Findex methodologist. Checks weights, the ~23% population exclusion, fieldwork dates, and that no 2021-wave value is called current.
- A Reuters or AFP Yemen correspondent with twenty minutes and a phone, who will quote the first sentence and screenshot the first chart.
- A senior Arabic economics editor at a Gulf daily. Reads the Arabic first, for calques, register and term drift.
- A humanitarian cash working-group lead, asking whether recipients stayed banked.
- A mother in Taiz on a 3G phone, asking whether her wallet is legal and what to do if she is cheated.
- A hostile commentator looking for one sentence that makes the resource look partisan to either authority.

3. FINDINGS TO ACT ON

Release defects
A1. VIS-PAYMENT-RAILS: the figure, its table and its text alternative disagree.
  - The text alternative names "the mobile e-money amendment (9 July 2025)" as a Rule step. The drawing and the table have no such row.
  - Make all three say the same thing, as the contract and its rows support: either bind the governed row (Governor's Decision No. 4 of 2025, SRC-CBY-EMONEY-AMD-2025-001) or remove the step from the text.
  - If a gate fits, add one: a drawn figure's text alternative may not name a step that its rows lack.
A2. Search for "law" / «قانون» returns /reforms/ and /data/ with no law and no note, yet the evidence base holds no primary laws.
  - Master-first, give search alias 001 a boundary note saying that primary laws are not in this evidence base. Follow the pattern alias 025 uses.
  - Extend the B5 scope line on /data/ to say that primary laws, and instruments issued in Sana'a, are not held.

Improvements, in value order
1. Regulatory findability
  - Correct document_type: SRC-CBY-UNLICENSED-EWALLET-2024-001 becomes circular/instruction; SRC-CBY-EMONEY-AMD-2025-001 becomes regulatory decision.
  - Set ENF-10's date if its original states it (EXT-02).
  - Order the B5 group by document date and give it an anchor. Link that anchor from "Verify it yourself" on /reforms/ and /providers/.
  - On /reforms/, name the instruments by number once, where the page already describes them (Decision No. 23 of 2024; Decision No. 4 of 2025), taking the numbers from their governed titles.
  - For "decision" / «قرار», rank rule-making decisions above the 14 enforcement decisions, and say "N of M" when the cap hides results.
  - Once these are done, the per-instrument stage table may stay post-launch.
2. Entity and Arabic search
  - Add a whole-phrase bonus on titles and summaries.
  - Match Arabic tokens of two letters or fewer as whole words only. "We Cash" and «وي كاش» must find their record first; today they rank 7th and 86th.
  - Add the aliases «فيندكس» / Findex and PSP / «مزوّد خدمات الدفع».
  - Alias 007's note should say that «محفظة» means both e-wallet and loan portfolio, and name the two record families.
3. Evidence landscape (inside B12, for VIS-EVIDENCE-FRESHNESS)
  - The input exists: audit/INDICATOR_COVERAGE_MATRIX.csv, with 34 dimensions. Bind its rows Master-first as the contract's rows.
  - Render a table grouped by the eight domains, with five columns:
    - dimension;
    - latest Yemen evidence and its period;
    - evidence class;
    - coverage state;
    - where to verify, and what would change it (the Measurement Agenda priority).
  - Use categorical states only: no colour ramp, no totals, no roll-ups.
  - Write "no evidence in this base", never "none".
  - Remove the process notes.
  - If all 34 rows cannot be bound, 12 rows is still honest.
  - Also render DS-DEMAND-VINTAGE-LENS's ten-function people-side table in the B12 table pattern.
4. Humanitarian and remittance paths
  - Make CWR-010 reachable from /payments/.
  - Cross-reference CLM-045 and YSC-022 using their existing boundary text: delivered ≠ targeted ≠ persistent.
  - MA-001's card on /remittances/ leads with its remittance sentence, or carries a governed title variant. No new priority; REJ-02 stands.
5. Comparisons a reader can run
  - Add a preset link /evidence/compare/?records=CLM-001,CLM-054,FMIIP-BASELINE-2025-01 under the Compare page's "three measures that cannot be combined" paragraph.
  - Add a link to ?records=CLM-032,CLM-037,CLM-041 from /remittances/.
  - The Compare lead names geography and unit; it must not promise dimensions the tool does not compare.
6. Providers
  - Under the matrix that item 18 unlocks, show the dated status events PSE-001…015 as the table of the existing VIS-PROVIDER-TIME record. Columns: date · decision number · class · action. Caption it with CLM-019's boundary.
  - PSE-015 prints "names pending transcription from the original" and is never omitted.
  - On status-event records, use the governed /providers/ sentence (a status event changes formal status, not what is known about customer access) as the frame note.
7. Pairings that carry the insight (governed sentences only)
  - CLM-010 with CLM-050 on /payments/: subscribers ≠ people ≠ active use.
  - YSC-016 with CLM-054: why nominal rial figures cannot be compared across the valuation change.
8. Chronology
  - Render it where its governed relationships already bind it: /reforms/, /payments/ and /remittances/.
  - Use an event variant of the compact object: the date leads, the class is the kicker, and an event never carries the "When was it measured or observed?" label.
  - YSC-020, the analytical rule, becomes a frame note, not a 24th card.
9. Reading load on phones (refine D7, do not redesign)
  - Put the seven trust_navigation links in the opened mobile menu.
  - Where a drawing and a named-column table both exist, move the prose text alternative into a details element; the table stays the visible alternative.
  - Give /payments/ a shorter governed headline, Master-first, with the same meaning; today it is 30 words.
  - Show "How numbers are presented" once, not under all eight domain headings.
  - Put one boundary band before the first answer; the second goes where its content belongs.
  - Make the spine index answer sections, not every structural tail.
  - Make /ar/data/ compact by default; it is 61,060 px tall at 390 px.
  - On a phone, bring Home's first figure higher by moving governed copy, not by rewriting it.
  - Stop labels colliding on the POS line charts.
10. Stale self-description
  - The 00_MASTER and 37_READINESS_CHECKLIST sheets still state 141 pages, 108 records, 59 claims and 159 sources.
  - Correct them Master-first to the counts you measure, if the earlier window has not already done so.
11. Copy
  - Fix "resolve … resolve" / «حسمها … حسمها» on Home and Explore, in B2 and B3.

Lessons from comparable products (apply only where governed fields exist)
- Never label anything "latest"; say "as of <date>". Add a lint gate over titles and meta.
- Every survey-derived record states its coverage: adults 15+ in areas covering about 77% of the population, with the excluded areas named.
  - Add this where the governed universe does not already say it.
  - Verify against the World Bank Microdata Library study page for Findex Yemen 2021.
- Check in the original whether Yemen is absent from Global Findex 2025. If it is, state it Master-first wherever people-side currentness is discussed: missing ≠ unchanged.
- The B9 citation has two lines:
  - this resource: edition, date checked, URL;
  - the original source: publisher, title, year, locator.
- Show the dates the governed fields hold (period observed, checked on, publication) together. Never write "next update".

Currentness and enrichment sweep (in B13d and B14e)
- For each watch point in audit/FINAL_CURRENTNESS_CUTOFF.md, check the publisher's own site:
  - CBY-Aden decisions after No. 18 of 2026;
  - POS releases after January 2026;
  - the IMF SMP;
  - the FMIIP ISR after no. 2;
  - RPW after 2025 Q3;
  - a new Yemen Findex wave.

  A newer original is added Master-first in both languages. If there is none, record the check.
- Read FMIIP ISR no. 2 in the original. If it reports an observed access-point value, that value is the first RESULT row of VIS-TARGET-RESULT-STATE.
- Attempt each of these and record the outcome:
  - the four IMF-attributed chronology events (item 3);
  - the Decision 18 names, from the signed CBY document, Arabic first, never from press (EXT-03);
  - the 2023 SFD/SMED primary source for 78,686 borrowers (EXT-06).
- Run six reverse traces (public object → record → source → locator) and fix any break Master-first:
  1. the Home headline claims;
  2. VIS-FINDEX-GAPS;
  3. VIS-POS-VALUE;
  4. RV-CWR-001;
  5. the /reforms/ chain;
  6. one IMF-attributed chronology event.

Judge, then decide
The default is post-launch, unless all seven conditions hold and the red team agrees.
- 18_CBY_MONETARY holds 686 observations, 2017 to May 2026, and one of its values is public.
  - Would a bounded expression on an existing contract help readers interpret nominal-rial figures?
  - Weigh this against the valuation change and the CBY-Aden scope.
- A publisher facet in the B13 library. Label it "publisher", never "official / unofficial".

Into docs/ROADMAP_V1_1.md (do not build now)
- The Findex 2021 weighted subgroup compute: 188 specified contracts; it needs the microdata file.
- RV-CWR-004's people lane extended back to 2011, as rows, not as a new contract.
- International context from same-source aggregates.
- A "safe sentence" copy control.
- Inline dated source brackets.
- Versioned Readings.
- A domain search facet.
- Reading audiences.
- IOM DTM and VSLA documentation as context for MA-003 and MA-009.
- CPMI-IOSCO as a method reference.

Rejected (record the reasons in B16)
- A composite evidence-maturity score.
- An interpolated account-ownership path.
- Operating-provider counts derived from rosters.
- POS terminals per adult.
- "True level" factors for remittances.
- Access maps built from rosters.
- A provider "2026 status" badge.
- An "is my wallet licensed?" lookup.
- Provider profile pages.
- A rial converter.
- Food-security monitoring.
- The Uzbekistan comparator.
- A "five key numbers" explainer.
- Merging regulatory instruments into the system chronology.

4. COST AND WINDOWS
- Use fewer, sharper subagents rather than many.
- If you reach a usage limit, stop at a clean point, push, write the RESUME POINT, and stop. Never leave work uncommitted.
- One window works on this repository at a time.

════════ END OWNER ADDENDUM 2 ════════
