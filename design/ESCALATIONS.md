# Escalations

Format (README_FIRST §10):
- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>`
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>`

Answered by the steward, Master-first. Items are closed, never deleted.

## Open

Raised at D1 (27 September 2026), from the independent lens critique of the propositions (`01_FOUNDATIONS.md` §3), and
reconciled at D2 by their true authority (DL-D2-002). Each was needed by a design actually rendered; none is filled with
authored copy.

- `NEEDS_CONTROLLED_CONTENT — Home (`/`) section 3 — pacing boundaries — the candidate direction paces the governed
  "three figures" paragraph as figure groups, each followed by its bounded record; the split points are found by the
  governed connectives ("In the same survey", "Separately", "These are different measures" and their Arabic
  equivalents), which couples the build to wording. If the direction is accepted, a controlled marker (sentence or
  group boundaries on the section body) lets the build pace without parsing prose. Until then the reference
  implementation may pace only by these connectives and must fall back to the unpaced paragraph when they are absent.`
  D2: Master-first (the section body carries no marker in either language); open, non-blocking; DEBT-008.
- `ESCALATE_TO_MASTER (question, not a defect claimed) — RV-CWR-001 imf_staff_path — evidence state — the series
  carries state REPORTED while the Reading's prose describes the IMF path as a staff reconstruction with a modelled
  personal-transfers component; the source-institution lens asked whether the lane should carry an estimate state.
  Design impact: if the state changes, the IMF lane and the fallback table carry the state label; the drawing does
  not change otherwise.` D2: an evidence-authority question; REPORTED rendered as governed; open, non-blocking.

Raised at D2 (27 September 2026), each needed by a design actually rendered:

- `NEEDS_CONTROLLED_CONTENT — every drawn figure's fallback table (VIS-FINDEX-GAPS, VIS-REMITTANCE-MACRO, the POS
  panels, VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-COST, RV-CWR-001, the chain) — column labels for the group / object,
  the evidence state and the note columns (the value column is headed by the governed unit label) — without them the
  tables ship with empty column headers (DEBT-013); Design ships them empty rather than inventing "Group", "State" or
  "Note".` D6: narrowed by composition (DL-D6-003) — the state, document and marker qualifiers now travel in the
  caption or in the value's cell, so no data column of the thirteen drawn contracts is unheaded; what remains is the
  provider matrix's five dimension headings (raised below). A governed label for a period / group / object column would
  still read better than the empty corner cell; a preference, not an authority gap.
- `ESCALATE_TO_MASTER (rows requested) — VIS-TARGET-RESULT-STATE (/reforms/ and its record) and VIS-MFI-DIVERGENCE
  (/finance/) — TABLE_TEXT_FIRST contracts whose rationale describes a table (baseline, target and the absent result;
  the divergence table) but whose contract resolves no rows — the governed TARGET and RESULT markers cannot be drawn
  from the alt text; both render as text frames until rows exist. Design impact: with rows, a three-row table with the
  governed markers; without, the text frame stays.`

Raised at D3 (27 September 2026), from the Home cold-reader test (four fresh readers, EN/AR × 390/1440 px; verbatim
reports in `evidence/d3/cold_read/`, DL-D3-001). Each is content or authority, so Design records it and changes nothing;
none blocks the gate. Where the reader's words are quoted they are the reader's, not a finding of fact.

- `NEEDS_CONTROLLED_CONTENT — every text-first visual (TABLE_TEXT_FIRST and SUPPORTING contracts without a drawing) —
  a governed label for the description of a frame that has no view — the only governed heading is
  UI-VIS-TEXT-ALTERNATIVE ("Text description of this view"); on Home a reader took it for a missing diagram. Design keeps
  the heading in the accessibility tree only (DL-D3-002); with a governed label for text-first frames it is shown.`
- `ESCALATE_TO_MASTER (question, not a defect claimed) — VIS-INCLUSION-TRANSMISSION — alt_text — the governed alt text
  ends by restating the contract's prohibited_inference ("Does not establish: The relationships are not causal claims …"),
  so the frame reads the boundary twice however it is composed; readers took the repetition for a templating fault.
  Design impact: none if the alt text is shortened; the frame already prints its own boundary once.`
  2 October 2026: a narrower statement of a general cause — every one of the 36 contracts' `alt_text` ends with the
  prohibited inference by one generator rule; see the escalation raised at the independent acceptance of pull request #8
  (A3 / C3) below, and the owner's decision in `audit/OWNER_DECISIONS_2026-10-02.md`, row A3 / C3.
- `ESCALATE_TO_MASTER (observations, not defects claimed) — Home section 3 and the bound records — three date forms in
  three cards (prose "November 2022 to January 2023"; the clock "2022-11-07 to 2023-01-09"; "Mar-2025–Jan-2026"); three
  years attached to one number (Findex 2021, fieldwork 2022–23, data year 2022) read as an error on first pass; the
  same-wave figures at two decimals (18.35 %, 5.44 %, 12.91 points) beside 11.9 % read as false precision to all four
  readers; "POS", "CBY-Aden", "wave", "rails", "enabling constraints" and the label "Evidence signals" were not understood
  cold. Design impact: none — every value, unit and term renders as governed (Lock: one number rule, precision as
  governed); a governed expansion or gloss would render in place.`
- `ESCALATE_TO_MASTER (question) — CLM record "Financial inclusion is a connected system, not a single score" — its
  currentness "Several periods, varying by domain" under the record clock — readers noted a framing statement clocked like
  a measurement; the record grammar cannot tell them apart. Design impact: a governed record kind (framing vs measured)
  would let the compact object omit or relabel the clock.`
- `NEEDS_CONTROLLED_CONTENT — masthead — the publisher's name as governed text (English and Arabic) — the canonical mark
  is a square lockup whose wordmark and Arabic name stay under 8 px at any masthead size (EAD-04 forbids cropping or a
  derivative), so the publisher is legible only in the footer strapline; three readers took the first screen for a World
  Bank page. Design impact: a governed publisher line beside the product name in the product bar. The mark's web weight
  (the 10 MB master PNG served on every page, as in the baseline) is an owner decision on a derivative (DEBT-016).`
- `ESCALATE_TO_MASTER (Arabic, observations) — Home — "قياس سكاني ممثل" (calque; readers expected "مسح تمثيلي للسكان"),
  "لا درجة واحدة" for "not a single score", "إشارات من الأدلة", "ضمن نطاق الإبلاغ لديه", the ISO date range inside Arabic
  prose, and the title's "أدلة" read cold as "guides/directories" before "evidence" — reported by both Arabic readers as
  terminology, not grammar or direction (direction, mirroring, punctuation and diacritics were judged correct). Design
  impact: none; a native-language review is an owner item and no certification is claimed.`
- `ESCALATE_TO_MASTER (observation) — Home label UI "side" ("This resource presents the strongest defensible answer …") —
  two readers read it as a self-assessment they cannot test; it renders in the spine's flow group, as governed.`

Raised at D5 (27 September 2026), needed by the interaction design:

- `NEEDS_CONTROLLED_CONTENT — every external source link (\`a.source-locator\`, \`target="_blank"\` on the record, the
  Reading and the register) — an accessible cue that the link opens the original in a new window — anticipated at D0
  (brief §10); the D5 keyboard walks reach these links without any cue, and Design authors none. Design impact: a governed
  phrase rendered visually hidden inside the link (or visibly after it) on every external locator.`

Raised at D6 (27 September 2026), each needed by a design actually rendered; none is filled with authored copy:

- `NEEDS_CONTROLLED_CONTENT — VIS-PROVIDER-OBSERVABILITY (its record and /providers/) — the five dimension headings
  of the matrix (issuing authority or source; dated universe or count; dated status decisions; negative authority;
  evidence of operation), one UI-* ID each in both languages: UI-VIS-MATRIX-AUTHORITY, UI-VIS-MATRIX-UNIVERSE,
  UI-VIS-MATRIX-STATUS, UI-VIS-MATRIX-NEGATIVE, UI-VIS-MATRIX-OPERATION — the contract names them in English prose
  only (brief §10 anticipated this). Design impact: the matrix panel and its table print the development placeholder
  ⟦NCC:key⟧ in place of each heading (the only placeholders on the site, asserted by check_visuals.py); every cell keeps
  its own governed label, so the matrix is readable meanwhile; the accepted site cannot carry the placeholders.`
  D7: the matrix is unshipped — the contract renders as its text frame with no placeholder until the six labels are
  governed (DL-D7-001); the built form and its export frame return the day they are, without a code change.
- `NEEDS_CONTROLLED_CONTENT — VIS-PROVIDER-OBSERVABILITY — the class label of the fifth row (payment-system operators;
  UI-VIS-CAT-PRV-CLASS-PSO) — the contract's known gap: no governed universe row exists for the class; the row is
  designed as UNKNOWN in every dimension with the three institution events of RV-CWR-009 (REF-PAY-011…013) listed as
  context, never as a named universe. Design impact: the row renders the day the label exists; until then the matrix
  shows four classes.`
  D7: with the matrix unshipped (DL-D7-001) no class is hidden and no placeholder ships; the label is still needed for
  the matrix to draw at all.
- `ESCALATE_TO_MASTER — VIS-PROVIDER-OBSERVABILITY — the bilingual form of the matrix's dated cells and its ">9" count —
  the governed time boundaries "observed 2026-09-07", "2026-01-22 event", "Official 2026 annual roster; later 2026
  status events separate", "2024 Q3 / 2025 H1 / 2025-09-10 / 2026 event states" and the participant count ">9" are
  English free text in both editions (the brief §10 names them). Design impact: they print as the Master holds them,
  isolated left-to-right and marked lang="en", in the Arabic frame too; nothing is translated or shortened in design.`
- `NEEDS_CONTROLLED_CONTENT — every drawn figure's foot — the export control: the action labels (image; the governed
  data table) and their states (unavailable until the licence decision; licence; file format) — the control and its
  frame are designed (03_COMPONENT_CATALOG.md §1, 06_VISUAL_TABLE_SYSTEM.md §8) and ship unshipped: no label exists
  and every CauseWay-content download waits for OWN-04. Design impact: none until both exist.`
- `ESCALATE_TO_MASTER (rows requested) — VIS-FIRM-CONSTRAINTS (its record and /firms/) — the contract names sixteen
  challenges and resolves eight rows (FFO-2022-CH-01…08); the other eight (FFO-2022-CH-09…16) exist only in the
  REFERENCE-role file firm_finance.json, which the reference may not read. Design impact: the bars draw the eight
  governed rows and the table lists them; with the rows, the figure and table extend without a change of form.`
- `ESCALATE_TO_MASTER (rows requested) — VIS-FIRM-FINANCE-PATH and VIS-FIRM-FINANCE-SEVERITY (their records and
  /firms/) and VIS-INCLUSION-TRANSMISSION (its record and Home) — TABLE_TEXT_FIRST contracts whose rationale describes
  a table (loan sources among 18 valid responses; obstacle severity; the system's relationships) but which resolve no
  rows, and whose vocabulary (the relationships, the severity scale) exists only as English prose in STRUCTURE- or
  REFERENCE-role files. Design impact: text frames until rows exist; with rows, a table in the pattern of
  06_VISUAL_TABLE_SYSTEM.md §4.`
- `ESCALATE_TO_MASTER (question, not a defect claimed) — RV-CWR-004 people lane — the people series carries x = 2022
  (the World Bank reporting year) while the lane is drawn as the fieldwork span 2022-11-07 to 2023-01-09 that CLM-001's
  governed period names in prose; the frame prints that whole governed period under the lane. Design impact: if the
  Master gave the contract row its own fieldwork start and end fields, the lane would bind them directly instead of
  reading the ISO dates inside the period text.`
- `ESCALATE_TO_MASTER (observation) — every page's meta description — 284 of the 286 descriptions open with the page's
  own title ("Financial inclusion in Yemen is not one number. — Yemen Financial Inclusion Evidence is …"); on a shared
  image the title would read twice. Design impact: the social template prints the title once and then the
  description's remainder after the separator (nothing dropped); a description that did not repeat the title would
  print whole.`

Raised at D6 from the independent red-team lenses (27 September 2026; DL-D6-007). Each is content or authority, so
Design records it and changes nothing; where a lens's words are quoted they are the lens's, not a finding of fact:

- `ESCALATE_TO_MASTER (observations) — credit lines — RV-CWR-001's governed credit names the IMF twice ("IMF / Yemeni
  authorities" and "International Monetary Fund") and "Yemeni authorities" is ambiguous in a Reading about Aden versus
  the IMF; VIS-REMITTANCE-MACRO's credit "IMF / Yemeni authorities" covers projection years the IMF attributes to
  staff; RV-CWR-004 lists "World Bank" twice; VIS-PROVIDER-OBSERVABILITY credits YMN and CBY-Aden while a universe cell
  rests on the FMIIP workshop with the World Bank and UNDP. Design impact: none — every credit prints as governed.`
- `ESCALATE_TO_MASTER (question) — VIS-REMITTANCE-COST — the MEASURED state ("Measured in a survey") heads averages of
  price quotes from the Remittance Prices Worldwide database; a source owner may object to "survey". Design impact:
  the state label prints as governed; a different governed state would print in its place.`
- `ESCALATE_TO_MASTER (observation) — VIS-PAYMENT-RAILS — the governed alt text names the mobile e-money amendment of
  9 July 2025 as a rule while the reused event set of RV-CWR-009 holds no such row, so the drawing and its text
  alternative differ in content; the contract carries no credit for this SUPPORTING visual. Design impact: a governed
  event row would join the chain; a governed credit would print in the foot.`
- `ESCALATE_TO_MASTER (question) — RV-CWR-009 and VIS-PAYMENT-RAILS — the governed step mapping lets
  NETWORK_ACTIVITY_SIGNAL (an attributed CBY-Aden statement at an exhibition) evidence the OPERATION step; in
  VIS-PAYMENT-RAILS it carries that step alone, beneath the components the prohibited inference says are not shown
  operating. Design impact: the chain follows the mapping as governed; the foot's boundary guards the reading.`
- `ESCALATE_TO_MASTER (observation) — VIS-FIRM-CONSTRAINTS — the contract's fallback names sixteen challenges and eight
  rows resolve (raised above); nothing in the frame says the list is partial. Design impact: a governed sentence on
  partial coverage would print as a frame note; otherwise the eight rows stand as the contract resolves them.`
- `ESCALATE_TO_MASTER (question) — RV-CWR-004 infrastructure lane and RV-CWR-009 activity rows — the POS values travel
  with their governed object label ("POS terminals · 561 Number") but not with the CBY-Aden reporting-scope qualifier
  that the VIS-POS-* contracts' universe carries; a lane or step crop presents a CBY-Aden count as national. Design
  impact: if the Readings' universes (or the rows) carried the scope, it would print with the lane and the step.`
- `ESCALATE_TO_MASTER (observations) — meta descriptions — several governed descriptions end mid-sentence with "…"
  (Home, About, Data & sources) and Compare's description is a tool instruction ("Select 2–4 records."); on a shared
  card they print as governed. Design impact: none.`
- `NEEDS_CONTROLLED_CONTENT — every fallback table whose rows carry different units under one value column
  (VIS-FINDEX-GAPS: two age rows in their own governed units under "% of adults (ages 15+)") — a governed neutral
  header for a column of values; today each such row prints its own unit in its cell. Design impact: the header would
  replace the panel unit where units vary.`
- `RUNTIME_DEFECT (Code, D7 — not a Master item) — the Compare tool's table — the runtime (`site-src/app.js`, which
  Design never edits) writes each record's governed period into a cell as plain text, and in the Arabic edition the two
  ISO dates render with their parts reversed ("07-11-2022 إلى 09-01-2023" for 2022-11-07 → 2023-01-09; found by the
  Arabic lens on the printed Compare page). The reference pages isolate every ISO date and numeric range
  (`design/reference/yfie/text.py`, `LTR_RUN`); the runtime does not. Fix for Code: when the table renderer writes a
  cell, wrap every match of that same expression in `<bdi dir="ltr">` (or set the cell text through a helper that does).
  Design impact: none on the reference; every Arabic Compare table on the product until fixed.`
  **CLOSED 2026-09-29 by Code (EAD-01 follow-on).** `site-src/app.js` isolates through the renderer's own
  expression (`scripts/yfie/text.py` `LTR_RUN`), character for character, in one helper applied wherever
  governed record text reaches a page: the Compare cells and column heads, the boundaries beneath them, the
  record links, and the search results' titles, summaries and period line. `scripts/validate.py` fails if the
  runtime's expression is not the renderer's or the helper is gone, and two negative controls prove both.
- `ESCALATE_TO_MASTER (observations, Arabic edition — the native-editor lens; each prints as governed) — a count
  followed by its unit noun ("561 العدد", "1,473 العدد") where a reader expects "العدد: 561" or a counted noun; the
  invariant plural "نقاط مئوية" after 12.91, 12.55 and 11.1 where the prose writes "نقطة مئوية"; the exchange-class
  labels read as counted phrases with the wrong number form ("98 شركات الصرافة", "225 منشآت الصرافة الفردية"); the
  comparator island ">9 مشاركون في الفعالية" where the governed conclusion writes "وأكثر من 9 مشاركين"; two terms for
  the index in RV-CWR-001 ("بالرقم القياسي" in the subtitle and prose, "مؤشر، 2021 = 100" in the unit label);
  `UI-VIS-SOURCE` carries a colon in both languages ("Source:" / "المصدر:") and heads a table column; every credit
  line is English only in the Arabic edition. Design impact: a "·" between a count and its label is available as
  composition if the steward prefers it to a governed rewording; otherwise none.`

Raised at D7 (28 September 2026) from the two independent cold readers on the final tree (an English and an Arabic
researcher–regulator–journalist lens; reports in `evidence/d7/cold_read/`). Each is content, authority or runtime, so
Design records it and changes nothing governed; where a reader's words are quoted they are the reader's, not a finding
of fact:

- `ESCALATE_TO_MASTER (defect claimed) — /people/ section 02 and VIS-FINDEX-GAPS — the governed section text states,
  in both editions, that "the matching figure for adults with more education is not in the evidence base, so no
  education gap is stated" ("لا تتضمن قاعدة الأدلة الرقم المقابل لمن تلقوا تعليمًا أعلى، ولذلك لا تُذكر فجوة بحسب
  التعليم"), while the governed contract of VIS-FINDEX-GAPS on the same page binds WB-FINDEX-OBS-2022-007 (adults with
  secondary education or more, 19.53 %) and derives the education gap of 12.55 percentage points from it (with
  WB-FINDEX-OBS-2022-006), and the page's boundary names only the sex and income gaps. The page contradicts itself: the
  English cold reader called it blocking for trust. Design impact: none until the Master decides — the figure prints
  its governed rows and the section its governed prose; if the sentence is corrected the figure stands, if the row is
  withdrawn the bars and the table shrink by one group and one gap without a change of form.`
- `NEEDS_CONTROLLED_CONTENT — the search results status (dialog and inline) — a governed "N of M results" form and a
  way on when the runtime caps the hits — the baseline runtime shows at most ten hits and the governed status reads
  "10 results shown", so a query with 79 matching records ("remittances") reads as a corpus of ten; the no-match copy
  offers a way on, the has-results state does not. Design impact: none in the reference (the runtime and its copy are
  the baseline's); Code shows the total and links the query to the Evidence directory (EAD-06, the `?q=` state).`
- `NEEDS_CONTROLLED_CONTENT — /evidence/compare/ — a governed sentence stating why thirteen of the 110 records form
  the comparable set (the evidence-state rule the Methodology's section 09 states), for the tool's intro and for the
  "not available for comparison here" error — a Home headline record (CLM-003) is refused without a reason. Design
  impact: the sentence renders in the tool's intro and the error stays the runtime's; nothing changes otherwise.`
- `ESCALATE_TO_MASTER (observation) — /evidence/compare/ section 01 ("Three measures that cannot be combined") — the
  governed worked example follows the runtime's output, so after a live comparison its three measures (11.9 %, the
  3.3 million savers, the FMIIP baselines) can read as the analysis of the selected pair; a governed rubric naming it a
  worked example (or the section placed before the tool by the Master's section order) would settle it. Design impact:
  the D2 order (the tool as the first answer, the governed sections after) stands; the section keeps its governed
  ordinal and heading.`
- `ESCALATE_TO_MASTER (observation, restated) — Home, /providers/, /measurement/ — the text-first frames
  ("Another view of the evidence") repeat governed prose the page already carries and print the boundary twice (the
  alt text restates the prohibited inference) — raised at D3 (the alt text; a governed label for text-first frames);
  the D7 English reader read the frames as text-only boxes that add nothing. Design impact: as at D3.`
- `RUNTIME (Code, not a Master item) — the page citation — "Cite this page" copies title, product and URL while the
  record citation carries publisher, edition, period and population; both copy without a preview. Design impact:
  none in the reference (the runtime's templates); Code uses one citation template from the governed citation fields
  with a visible preview (09_CODE_HANDOFF.md, D7 table).`
- `ESCALATE_TO_MASTER (observation) — /payments/, /readings/same-year-different-number/ and their records — one
  governed value in two magnitudes: the prose writes "1.262 مليار ريال" and "6.245 مليار دولار" while the contract rows
  print "1,262" and "6,245" (million) beside decimal values such as "317.639", so a reader meets a decimal point and a
  thousands comma in one table; the Arabic reader read 317.639 as thousands. Design impact: none — every value prints
  as governed with the one number rule; a governed unit or precision per series would print in place.
  **Strengthened at the D7 closure (28 September 2026):** a second, independent Arabic reader made the same mistake on
  the same pattern and reported it as a defect — reading the POS-value series "580.021, 795.006, 783.583, 910.688,
  1,262" (all YER million) as mixing magnitudes "three orders of magnitude apart", when the values differ by about
  1.4×. Two trained readers in two sessions have now misread a governed value by a factor of a thousand from this
  notation alone. It is the strongest reader evidence in the D7 record, and it is a content decision: Design will not
  round, restate or re-unit a governed value.`
- `ESCALATE_TO_MASTER (observation, restated from D3) — the Findex fieldwork window — one number carries three date
  forms across Home, /people/ and the Compare table ("November 2022 to January 2023", "2022-11-07 to 2023-01-09",
  "7 November 2022 to 9 January 2023"); a writer cannot tell which form to cite. Design impact: none — each form is the
  governed field that carries it; a canonical governed form would print everywhere.`
- `NEEDS_CONTROLLED_CONTENT — /payments/ (VIS-POS-TRANSACTIONS beside the withheld H1 2025 transactions figure) — a
  governed sentence naming the withheld release and why the monthly series beside it is admissible; the withheld
  state itself is clear ("يُحجب الرقم إلى أن يُوثَّق تعريفه"). Design impact: the sentence prints as a frame note.`
- `RUNTIME (Code) and NEEDS_CONTROLLED_CONTENT — the Compare tool's Arabic copy — the status "2 سجلات مختارة" (a
  numeral with a template plural), the prompt "اختر سجلين على الأقل" shown while two records are loaded, and the
  boundary sentence printed twice ("لا يثبت:" and "لا يُستنتج:"). Design impact: none in the reference (the runtime's
  copy and state); governed dual and plural forms for the count and one boundary per tool state.`
- `ESCALATE_TO_MASTER (Arabic terminology, observations) — one concept, several governed terms across the corpus: bare
  "التحويلات" beside "التحويلات النقدية" and "الحوالات المحلية"; "خدمة أموال عبر الهاتف المحمول" beside "النقود
  الإلكترونية"; "المحفظة الاسمية"; "نموذج المتبقي البديل" beside "نموذج القيمة المتبقية". Design impact: none; a
  native-language review is an owner item and no certification is claimed.`
- `ESCALATE_TO_MASTER (question) — CLM-003 and VIS-POS-TRANSACTIONS — the governed legend and claim say both figures
  are shown ("يُعرض الرقمان": the 8.55 % computed change and the source graphic's +11 %) while the drawing plots one
  value per month; the +11 % is prose, not a row. Design impact: none — the drawing follows its rows; a governed row for
  the source's figure would be drawn as a marker.`
- `ESCALATE_TO_MASTER (observations) — /data/ and /explore/ — every one of the 151 source cards carries "Reuse terms:
  not assessed" (REL-02, a release item), which reads as unfinished to an official reader; "P0 · People" on Explore is
  expanded only on /measurement/. Design impact: none — a page-level governed statement of the reuse position and a
  governed gloss for the priority code at first use would print in place.`

Raised at the D7 closure (28 September 2026), from the three independent closure lenses on the rendered product
(`design/evidence/d7/cold_read/lens-*-closure.md`). Each was verified on the built pages before being raised.

- `ESCALATE_TO_MASTER (governed overlap) — /evidence/compare/ (VIS-SOURCE-COMPARISON) — the contract's governed
  alt_text ENDS with its governed prohibited_inference verbatim ("The same word does not mean the same measure. The
  comparison does not reconcile differing figures or prefer one number unless evidence on their definitions supports
  it."), so the tool prints those two sentences twice about 70 px apart: once as the tail of the intro, once in the
  boundary voice. Verified in both editions on the built pages. Design impact: none available without editing governed
  text — the boundary must always print in the boundary voice, and the alt text is governed as a whole; Design will
  not truncate a governed string. Either the alt_text should end before the prohibited inference, or the contract
  should record that the two fields overlap by intent.`
  2 October 2026: a narrower statement of the same general cause as the D3 VIS-INCLUSION-TRANSMISSION item — the overlap
  is not a property of this contract's governed text but of the generator rule that composes every `alt_text`; see the
  escalation raised at the independent acceptance of pull request #8 (A3 / C3) below, and `audit/OWNER_DECISIONS_2026-10-02.md`, row A3 / C3.
- `NEEDS_CONTROLLED_CONTENT — /evidence/ CLM-039 — the record's central comparison is entirely qualitative in the
  governed text (one public interface "showed an older span of years" while others "contained later observations"),
  with no years, no interface names and no size of the gap anywhere on the page, and the "earlier documented access"
  it refers to is never dated. A cold reader cannot grasp or check the claim from the record. Design impact: none —
  Design prints what the record governs; a governed sentence carrying the two spans (or their dates) would print in
  question 1 as any other governed value does.`
- `ESCALATE_TO_MASTER (observation) — the record's question 7 summary ("Detail for reproducing or challenging this
  record without changing what it means") reads as internal meta-language to a cold reader. Design impact: none — it
  is governed copy; a plainer governed gloss would print in place.`

Raised at the independent acceptance of pull request #8 (2 October 2026; `audit/PR8_INDEPENDENT_ACCEPTANCE.md` A3,
condition C3), recorded by the session meeting the before-merge conditions:

- `ESCALATE_TO_MASTER (general finding; the steward's) — every drawn and text frame, all 36 contracts, every route that
  binds one — the boundary prints twice because the generator composes every alt text as the accessible summary, the
  governed label UI-VIS-DOES-NOT-ESTABLISH and the prohibited inference (`scripts/projection/derived.py:1324`; 36 of 36
  `alt_text_en` and `alt_text_ar` end with the inference), while the frame foot prints the same inference once more under
  the governed label "What not to conclude" (`04_PAGE_FAMILY_COMPOSITIONS.md` §1: the boundary once per frame). On the
  public build at `38147de` every one of the 58 figures of the English edition prints its inference at least twice
  (VIS-POS-TRANSACTIONS three times); the baseline printed it once because it did not show the alt text visibly.
  `check_visuals.py` `boundary_once_in_foot` and `check_site.py` `boundary_once_per_frame` count the foot only, so the
  design checks pass. The two earlier escalations — VIS-INCLUSION-TRANSMISSION (D3, above) and VIS-SOURCE-COMPARISON
  (D7 closure, above) — are narrower statements of this one cause, not properties of those two contracts. Owner of the
  fix: the steward (one generator rule, no Master change; or a Design rule for the visible alt tail). Decision, 2 October
  2026 (`audit/OWNER_DECISIONS_2026-10-02.md`, row A3 / C3): each figure prints its boundary once on the page, in the frame foot; on
  the page the image's alt attribute and the visible text alternative use the governed accessible summary, which ends
  before the boundary; the full governed alt text, ending with the boundary, stays wherever a figure leaves the page
  (export frames, social frames). Implemented in the release-candidate pull request. Design impact: the frame's foot is
  unchanged; the text alternative loses its repeated tail. Open until that pull request lands.`

Raised in the release-candidate pull request (2 October 2026), by the independent review of transaction RC-3: drawing the
provider observability matrix (RC-3 item 18) brings two gaps into view that only governed content can close:

- `NEEDS_CONTROLLED_CONTENT — VIS-PROVIDER-OBSERVABILITY (/providers/ and its record, Arabic edition) — Arabic text for
  four period values — the matrix prints the governed period of each universe and wallet-count row through \`date_token\`
  (\`scripts/yfie/visuals.py\` provider_matrix), and four of them are English-only Master values with no Arabic column:
  "2024 Q3" and "2025 H1" (22_PROVIDERS_DATA wallet-count rows WCR-001 and WCR-002, \`reference_period\`), "2026-01-22 event"
  (WCR-004) and "observed 2026-09-07" (PUC-MFI-2026-01, \`reference_state\`). The Arabic pages therefore show the words
  "event" and "observed" and the codes "Q3" and "H1" in Latin script, in the drawn form and the fallback table. Needed:
  \`reference_period_ar\` / \`reference_state_ar\` (or a governed period vocabulary) in the Master, read by the loader for the
  Arabic edition. Code does not author Arabic data text; the values are unchanged meanwhile.`
- `NEEDS_CONTROLLED_CONTENT — VIS-PROVIDER-OBSERVABILITY — a lead-in for the payment-system-operators context events —
  the row prints "Unknown — not zero" in every dimension (the contract's \`known_gap\`), and in the status dimension the
  three institution events (REF-PAY-011…013) follow as context; only a dotted rule marks them as context on screen, and
  the fallback table joins them to the UNKNOWN label with a semicolon, so a table or screen-reader user can take a
  restructuring, a founding assembly and a board meeting for status decisions. Needed: a governed label (for example
  "Context:" / «للسياق:») printed before the events in both forms. Code does not author it.`

Raised in the release-candidate pull request (2 October 2026), by the A3 / C3 implementation (G4 item 4):

- `ESCALATE_TO_MASTER (Part B editorial pass, B2 / B3) — five governed accessible summaries restate their figure's
  boundary — with A3 implemented (on the page the text alternative is the governed accessible summary, the boundary
  prints once in the foot) and the design checks extended to count the visible text alternative
  (\`check_visuals.py\` boundary_once_in_foot, \`check_site.py\` boundary_once_per_frame), eight frames still print the
  opening of their boundary twice, because the accessible summary itself closes with a sentence that restates it:
  VIS-REMITTANCE-MACRO (EN, AR), VIS-POS-TRANSACTIONS (EN; its frame on /payments/ and its record), RV-CWR-003 (AR) and
  RV-CWR-005 (AR). The fix is Master-first: drop the restating sentence from \`accessible_summary_*\` in 11, both
  languages checked together. The checks stay strict and report these eight until then.`

## Closed at D2 (27 September 2026) — resolved by an authority the repository already holds

- Arabic credit line (`NEEDS_CONTROLLED_CONTENT — RV-CWR-001 and every visual contract with a credit`): the contract
  answers it — every `credit` carries `language_note` "Publisher names are governed in English only (15, 34); Arabic
  frames print them as isolated left-to-right runs". Every frame now prints the governed credit as an isolated
  left-to-right run. No Master change needed.
- Accessible name for in-page navigation (`NEEDS_CONTROLLED_CONTENT — every page with an in-page index`): resolved by
  accessibility practice without new copy — the index and the strip are named by the `h1` of the object they index
  (`aria-labelledby="page-title"`), each edge group by its own governed heading. DEBT-006 closed. A dedicated governed
  label ("on this page") would read better; it is a preference, not an authority question.
- Home section order (for steward confirmation): decided by the brief — §4.5 states the baseline order "is a
  precedent, not a mandate; keep the `#system` anchor". The Lock item stands; nothing to confirm.

Raised at EAD-01 by Claude Code (29 September 2026), found by the cutover itself:

- `NEEDS_CONTROLLED_CONTENT — Home (`/`) and `/explore/` — the R8.4A question selection and grouping — the four
  questions Home starts from, and which of the four clusters each of the eleven questions sits in, are not governed
  anywhere. Until EAD-01 they were recovered by `scripts/handoff_inventory.py` **scraping the baseline renderer's own
  HTML out of `dist/`**, and the renderer read them back from that inventory: a build that was an input to itself.
  Removing the baseline renderer emptied the scrape and `/explore/` rendered with no questions at all. Code has put
  them in one named place, `scripts/yfie/question_sets.py`, so nothing is parsed from markup and the regenerated
  inventory is byte-identical to the accepted one at `2f9a93c` — but a selection decision held in renderer code is
  exactly what EAD-11 says it should not be.`

  **The change, exactly.** Nothing here is new content: every question, every cluster heading (`UI-QUESTIONS-*`) and
  every destination is already governed. What is needed is the selection and the grouping, in the presentation
  contract beside the other presentation decisions — `site-src/content/presentation_priority.json`, which the steward
  edits in place — as two entries whose values are these, unchanged:

  ```json
  { "route": "/", "page_family": "Orientation",
    "starting_question_ids": ["QE-002", "QE-003", "QE-005", "QE-011"] }
  { "route": "/explore/", "page_family": "Question Entry",
    "question_groups": [
      {"heading_ui_id": "UI-QUESTIONS-UNDERSTAND-THE-WIDER-PICTURE",      "question_ids": ["QE-001", "QE-003"]},
      {"heading_ui_id": "UI-QUESTIONS-PEOPLE-USE-AND-FLOWS",              "question_ids": ["QE-002", "QE-004", "QE-007", "QE-009"]},
      {"heading_ui_id": "UI-QUESTIONS-FIRMS-INSTITUTIONS-AND-PROVIDERS",  "question_ids": ["QE-005", "QE-006", "QE-008"]},
      {"heading_ui_id": "UI-QUESTIONS-VERIFY-AND-DECIDE-WHAT-TO",         "question_ids": ["QE-010", "QE-011"]}
    ] }
  ```

  When that lands, `scripts/yfie/question_sets.py` reads the contract instead of holding the values, and is deleted
  once it holds nothing. Code cannot make this change: the two controlled contracts are the steward's, in a commit
  naming the finding it closes, with every gate run. Open; EAD-11; blocks no gate today.

  2 October 2026 — landed in the release-candidate pull request (G3), the session acting as steward for this patch only by
  owner decision (`audit/OWNER_DECISIONS_2026-10-02.md`, EAD-11): the two entries, values unchanged, sit under
  `question_sets` in `presentation_priority.json` (not in `routes`, which holds the eight Domain Answer routes the
  validator's S03 and the generator's tier check read); the renderer and the inventory read them; `question_sets.py` is
  deleted; Home and Explore are byte-identical before and after in both languages. Closed.

- `NEEDS_CONTROLLED_CONTENT — the search results, every route with a search — a result-type facet needs a name and an
  "all types" option — EAD-06 asks for a result-type facet, and the option labels are governed
  (`UI-JS-TYPE-PAGE` … `UI-JS-TYPE-SOURCE-LOCATOR`). What is missing is the control itself: an accessible name for
  the facet, and the label of the state where no type is chosen. `UI-DATA-FIND-A-SOURCE-BY-TITLE` is the source
  directory's own control and says "Find a source by title", so it cannot stand for either. Code does not author a
  label, so the facet is unshipped until these exist; the `?q=` half of EAD-06 needed no copy and is shipped.
  Design impact: none — nothing in the reference shows a facet.`

- `DESIGN_QUESTION (Code, EAD-02 — not a Master item) — every page with next actions — two navigation landmarks share
  one name — the accessibility audit of the implemented site found that `nav.actions` (the page's "Continue from here"
  section, named by its own `h2`) and the spine's first edge group `nav.edges` (named by its `h3`) carry the **same**
  governed title on the families where the edge group mirrors the next actions. A screen-reader user listing landmarks
  sees "Continue from here" / "تابع من هنا" twice and cannot tell them apart: 20 occurrences across the audited pages.
  This is a best-practice rule rather than a WCAG success criterion, and it appeared when DEBT-014 put the strip and
  the foot spine on the same page. Code did not choose between the options, because which of the two changes, and to
  what, is a composition and naming decision:
    (a) the spine's edge group stops being a landmark (a `div` with its `h3`), keeping the heading and the links —
        but `09_CODE_HANDOFF.md` records "every `nav` named … edge groups by their `h3`" and `check_site.py` asserts
        `aside.spine nav.edges[aria-labelledby]`;
    (b) the edge group is dropped on the families where it duplicates the section entirely (Evidence Directory, Data
        & sources), since it repeats the same heading and the same links;
    (c) a governed label distinguishes one of them — which is controlled content, and would be a fourth escalation.
  Design impact: none on what the page says; a reader who does not use a landmark list sees no difference.`

## Anticipated (not yet raised — each will be raised only when a D1+ design actually needs it)

Recorded so no one fills these gaps silently. Source: brief §10, §12, §15.

- Result-type facet labels exist (`UI-JS-TYPE-*`); a domain facet needs a governed domain field on search records.
- "Type not recorded" group label for the 9 displayed sources without `document_label` (`/data/`, EAD-07).
- Evidence-workbench facet headings/values (verification state, domain), if a facet is designed.
- Report-issue intent labels, if a richer reporting intent is designed.
- Reuse line and download labels following the licence decision (OWN-04) — the export control's labels raised at D6.
- IBM pre-split Latin font subsets (vendoring with provenance).
- Rows for the other TABLE_TEXT_FIRST contracts whose rationale describes a table but resolves no rows (raised at D2 for
  VIS-TARGET-RESULT-STATE and VIS-MFI-DIVERGENCE; the rest as their gate reaches them).

## Process notes (not escalations)

- D1 branch name (2026-09-27): D1 is developed and pushed on `claude/practical-cray-sr26c5`, the branch the execution
  environment is permitted to push, instead of the `design/d1-theses` name planned at D0. One gate, one branch, one pull
  request into `main` still holds; the steward may re-home the branch under `design/` at landing if the convention
  matters for history. No design meaning attaches to the name.

- Tag `checkpoint/design-handoff-ready` was not found at D0 (2026-09-27); commit `6d954c1` used. Steward to confirm.
  Steward, 2026-09-27: confirmed. `6d954c177b5d35cdad063f3a2cef5a92d33e16d4` is the recorded Design-handoff target (`OPENAI_REENTRY_CHECKPOINT.md` §7); the tag is an owner action (tag pushes are refused to the steward's environment). Working from the commit is correct; nothing changes when the tag appears.

- D2 branch name (2026-09-27): D2 is developed and pushed on `claude/epic-cori-60fpeb`, created at the exact accepted
  `main` (`851f496`), instead of the `design/d2-hard-families` name planned at D0; the same convention as D1.

- D3 and D4 on the D2 branch (2026-09-27): D2 was met at `9c263ac` but not yet merged when D3 began; the execution
  environment may push only `claude/epic-cori-60fpeb`, so D3 (met at `beecdbb`) and D4 continue on that branch and pull
  request #4 rather than on branches cut from an accepted `main`. Each gate's records name its own commit; the steward may split the history at landing if one
  gate per pull request matters. No design meaning attaches to the branch.

- D6 branch name (2026-09-27; closed 2026-09-28): D2–D5 were accepted together by the owner's merge of pull request #4 (`main` at `2effd8b`).
  D6 is developed and pushed on `claude/bold-maxwell-r3o015`, created at that exact `main`, instead of the
  `design/d6-visuals-social-print` name planned at D0; the same convention as D1–D5. One gate, one branch, one pull
  request into `main`. No design meaning attaches to the name.
  Closed: the owner declared D6 met on `125aa44` and instructed the session to merge; pull request #5 was merged by the
  repository's normal method (a merge commit, `f4739a5`), the branch left in place like every merged gate branch.
- D7 branch name (2026-09-28): D7 is developed and pushed on `claude/dreamy-archimedes-e8qx5v` (planned
  `design/d7-acceptance`), created at the accepted `main` `0ccdf0128308412b9aca5d59a48b3723d4690214` (the merge of pull
  request #6, D6 accepted and reconciled); one pull request for the gate, as at D6.
