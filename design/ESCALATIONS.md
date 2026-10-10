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

Raised in the release-candidate pull request (2 October 2026; release candidate G5), moved from "Anticipated":

- `NEEDS_CONTROLLED_CONTENT — /data/ (the source register) — EAD-07: a governed group label for sources without a
  document type — a document-type filter on the register is built-ready (142 of the 151 displayed sources carry a governed
  \`document_label\`), but 9 do not, and a filter with no group for them would hide nine sources the register promises are
  discoverable. Needed: a governed label for the no-type group (for example "Type not recorded" / its Arabic), English and
  Arabic together, Master-first in 04. Code ships the filter the day it exists. Raised; EAD-07 in the register.`

Raised at RC-8 (3 October 2026), by the owner's note of 3 October 2026, 03:10, point 1 (`audit/OWNER_DECISIONS_2026-10-02.md`):

- `ESCALATE_TO_MASTER (conflict recorded, nothing printed) — 22_PROVIDERS_DATA status events — entity names — the owner's
  rule withholds the entity names of the CBY-Aden enforcement decisions on every surface (CLM-019, the decision cards,
  the status-event table; only NEG-EW-011 prints a name, from the 2024 circular), and the build prints none: each
  decision shows its date, class and action, and its decision number in the source list. But the governed
  `public_use` field of six status events still allows the subject to be shown: PSE-006, PSE-007 and PSE-010 ("May
  show the exact dated branch-level status event"), PSE-012 (until RC-8: "May show the event subject"), and PSE-013
  and PSE-014 ("May show the exact dated event and subject"). As the owner directed, nothing is printed. RC-8 rewrote
  the two fields it had to touch for other reasons (PSE-012, date; PSE-015, Decision 18) so that they no longer
  allow names. The other five are left as they are, for the owner to decide: either rewrite their `public_use` to
  the withholding rule, or keep them as they are and record that the rule overrides them.` Open, non-blocking:
  nothing prints a name.

Raised in the release-candidate pull request (3 October 2026), by the product challenge (B15;
`audit/release_candidate/PRODUCT_CHALLENGE.md`). The red team sent these to the steward or the owner; nothing is built
around them meanwhile.

- `ESCALATE_TO_STEWARD (navigation contract) — About at 390 px (A-12, C-6) — About is reachable only from the footer on a
  phone; the reader who asks "who publishes and funds this?" does not find it in the menu. Needed: About in the mobile
  menu (\`navigation_interaction.json\`). The publisher's Arabic name stays "CauseWay" in Latin script (owner rule; the
  red team blocked «كوزواي»).` Open.
- `ESCALATE_TO_STEWARD (navigation contract) — Cite at 390 px (C-8) — "Cite this page" is in neither the mobile header nor
  the menu; on CLM-002 the only cite control is 3.7 screens down. Needed: a cite entry in the mobile header or the menu.`
  Open.
- `ESCALATE_TO_STEWARD (navigation contract) — a domain strip (C-10) — there is no direct route across the eight domain
  answers, and "Data & sources" holds no data. Needed: a decision on a domain strip; the labels follow Master-first.`
  Open.
- `ESCALATE_TO_OWNER — a naming rule for the 2024 e-wallet circular (B-2) — one of its 12 names prints (NEG-EW-011) and
  eleven do not. The red team advises against naming the other eleven (the list is dated 2024 and marked
  DO_NOT_CARRY_FORWARD; a fairness risk). Needed: the owner's rule for all twelve alike, either withhold all or
  publish all with the date boundary. Linking the parent records to their children is allowed and is in the roadmap.`
  Open.
- `ESCALATE_TO_OWNER — VIS-MFI-SPINE (B-7) — the record is titled "observations by date, with gaps and breaks shown", but
  it renders no chart and no table (a table-only record, left until after launch by decision A4 / C6). Needed: a
  contract that binds the governed observations, with each gap printed "no usable observation — not zero". Until then
  the title must not promise "gaps shown" (Master-first wording; roadmap).` Open.
- `ESCALATE_TO_OWNER — exports for researchers (game-changers U3, U6, U7) — a versioned dataset of all records, dated
  observation tables, and a citation file (BibTeX or RIS). \`scripts/exports.py\` is ready and \`public_downloads\` is
  false. Needed: the licence decision (OWN-04; REJ-03 keeps Dataset structured data closed until a licence exists).`
  Open; release-dependent.
- `ESCALATE_TO_OWNER — what CauseWay is (C-6) — /about/ says who funds the resource mid-paragraph, but nothing says what
  CauseWay is. A heading is Master copy (roadmap); the organisation's description must come from the owner.` Open.

Closed on 3 October 2026 by the owner's decisions of 3 October 2026 (`audit/OWNER_DECISIONS_2026-10-02.md`). The 09:05
note was restated, with additions, by the consolidated note of 09:50, which governs. Nothing above is rewritten:

- **RC-8, the status events' `public_use`: CLOSED by point 1, in RC-17.**
  - Every status event's `public_use` now says that entity names are non-public lineage and are not printed.
  - The same rule now governs the `public_claim_rule` of the 30 enforcement-subject rows and the provider-status
    passport's display requirement.
  - The events' own text now names each subject by its entity ID.
  - RC-NAMES stays. It is hardened to match short forms, joined spellings and Arabic prefixes, and it now covers the
    branch rows and the social-image frames.
- **B-2, a naming rule for the 2024 circular: CLOSED by point 2, in RC-17.**
  - The twelve names are withheld alike.
  - NEG-EW-011 keeps its ID, route and count, and is rewritten in both languages as one wallet service among twelve.
  - The search empty state carries the governed sentence on names.
  - The "We Cash ranks first" instruction is withdrawn.
  - One consequence goes back to the owner (raised at RC-17, below).
- **C-10, a domain strip: CLOSED for this release by point 4.** It is in `docs/ROADMAP_V1_1.md`, item 28.
- **B-7, VIS-MFI-SPINE: CLOSED for this release by point 5.** It is post-launch.
- **Exports for researchers (U3, U6, U7): CLOSED by the 09:50 note, section E.**
  - The owner adopts CC BY 4.0 for CauseWay's own content.
  - `public_downloads` stays false in this pull request.
  - The switch is one release step, after CauseWay's counsel confirms the licence text.
  - The exports carry the licence.
- **C-6, what CauseWay is: CLOSED by the 09:50 note, section D, in RC-17.** The owner's pair is added to /about/ before the
  funding paragraph, in both languages, and nothing else about the organisation is written. This replaces the 09:05
  point 7.
- **A-12 (About) and C-8 (Cite) at 390 px:** decided by point 3 (09:50 A.3). They close with the steward's patch to the
  navigation contract, in its own commit.

Raised at RC-17 (3 October 2026), by the adversarial review of the owner's point 2:

- `ESCALATE_TO_OWNER — NEG-EW-011's number identifies the service — the circular numbers its twelve names 1 to 12 in the
  order of NEG-EW-001…012, so the record ID is the circular's own item number. With the circular linked from the
  record, a reader who opens it can identify the eleventh listed service: withholding the name does not withhold the
  identity, and the record still singles out one of the twelve. This follows from the owner's "same ID, same route".
  Needed: the owner's choice — accept it as disclosed here, or let /evidence/NEG-EW-011/ point to CLM-015, which
  covers all twelve alike.` Open; nothing prints a name. B16: RELEASE (the owner's choice at release acceptance).

Closed on 3 October 2026 by the steward's patch to the navigation contract (owner decisions of 3 October 2026, 09:05
point 3 and 09:50 A.3; `audit/OWNER_DECISIONS_2026-10-02.md`):

- **A-12 and C-6, About at 390 px: CLOSED.**
  - Below 900 px, the opened menu carries the governed trust links, About first, under the footer's own group label.
  - The contract gains one key, `mobile_menu`, and nothing else in the file changes. Existing labels only.
- **C-8, Cite at 390 px: CLOSED.** The opened menu carries the existing "Cite this page" control; the header itself is
  unchanged.
- **Checks:**
  - The menu was checked at 320 and 390 px in both languages: 7 links, About first, the cite control reachable, no
    overflow, header heights unchanged.
  - Gate RC-NAV holds it on every page, with a negative control. The designation ends with this commit.

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
- "Type not recorded" group label for the 9 displayed sources without `document_label` (`/data/`, EAD-07). **Raised
  2 October 2026** — see "Raised in the release-candidate pull request … EAD-07" under Open.
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

- 2026-10-03 — **B16 disposition** (append-only; the reasons and evidence for each line are in
  [`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`](../audit/release_candidate/OPEN_ITEMS_DISPOSITION.md)):
  - X-ESC-D1-01 — **NEXT EDITION** — Home (/) §3: a controlled pacing marker so the build paces the governed 'three figures' paragraph without parsing connectives (alias DEBT-008). → Named in the B16 brief's expected post-launch list ('the DEBT-008 pacing marker'). Fallback ships (render.py paced_groups). Reclassified in G5 (30523ee; audit/RECORDS_RECONCILIATION_2026-10-02.md row 3). Owner: steward (marker, Master-first) and Design.
  - X-ESC-D1-02 — **DONE** — RV-CWR-001 imf_staff_path carries evidence state REPORTED while the Reading calls the IMF path a staff reconstruction; should the lane carry an estimate state? → Adjudicated KEEP in RC-1, commit 76aaeec; audit/release_candidate/runs/RC-1_MASTER_LEDGER.json item_8.c (IMF rows carry calculation_state SOURCE_REPORTED__IMF_STAFF_CALCULATIONS). No closing line yet in ESCALATIONS.md.
  - X-ESC-D2-01 — **DONE** — Column labels for every drawn figure's fallback table (group/object, state, note); narrowed at D6 to the provider-matrix headings plus an empty corner cell (a p… → Matrix headings governed in RC-3 (d668f11); every fallback table's row-header column labelled in RC-11 B10 b / NCC-02 (a95c7ef); last empty corner cell labelled in 66521a3. axe empty-table-header 0 (docs/ACCESSIBILITY_AUDIT.md).
  - X-ESC-D2-02a — **DONE** — Rows requested for VIS-TARGET-RESULT-STATE (/reforms/ and its record): a TABLE_TEXT_FIRST contract that resolved no rows (baseline, target, absent result). → RC-12, commit 98f43f5: table bound to FMIIP-RF-004 (baseline Jan 2025 817; target Jun 2030 1,021; result row 'No observed result is held … — not zero'); gate RC-B12. The drawing stays open as X-B12-VIS-TARGET-RESULT-STATE-DRAWING.
  - X-ESC-D2-02b — **NEXT EDITION** — Rows requested for VIS-MFI-DIVERGENCE (/finance/): the divergence table its rationale describes resolves no rows. → B12 names the missing input: a governed saver-definition crosswalk, a rial-valuation field per portfolio anchor, EN/AR labels for three state tokens, an Arabic universe state. Same work as EXT-10 and X-B12-VIS-MFI-DIVERGENCE.
  - X-ESC-D3-01 — **NEXT EDITION** — A governed label for the description of a text-first frame (only UI-VIS-TEXT-ALTERNATIVE 'Text description of this view' exists; a Home reader took it for a mis… → Post-launch: a governed label for a text-first frame's description (Design, Master-first). The B15 panel found no task failure from it (PRODUCT_CHALLENGE.md); the heading stays in the accessibility tree.
  - X-ESC-D3-02 — **DONE** — VIS-INCLUSION-TRANSMISSION: the governed alt_text ends by restating the prohibited inference, so the frame reads its boundary twice. → Owner decision A3 / C3 implemented in G4 part 1, commit 7895694 (on the page the text alternative is the accessible summary; boundary once in the foot; checks extended). Closes with X-ESC-PR8-A3.
  - X-ESC-D3-03a — **DONE** — Home §3 cold-reader observations, terms and date forms: 'POS', 'CBY-Aden', 'wave', 'rails', 'enabling constraints', 'Evidence signals' not understood; three dat… → RC-5, commit 1da995e: B3 a glosses / plain labels (B3-001…B3-024) and B2 d one prose form of the Findex window (ENGLISH_ and ARABIC_EDITORIAL_LEDGER.md). Checked in dist/en/index.html: 'Evidence signals' and 'enabling constraints' absent; 'wave (survey round)' printed. ISO clock lines stay ISO by rule B2 c.
  - X-ESC-D3-03b — **NEXT EDITION** — Home §3 residue: same-wave figures at two decimals (18.35 %, 5.44 %, 12.91 points) read as false precision; three years attached to one number; period form 'Mar… → Unchanged on dist/en/index.html (18.35%, 5.44%, 12.91 and 'Mar-2025–Jun-2026' still print). Source precision is governed; a display-precision or period-form rule is a Master-first content decision. Design impact none.
  - X-ESC-D3-04 — **NEXT EDITION** — CLM record 'Financial inclusion is a connected system, not a single score' is clocked like a measurement; a governed record kind (framing vs measured) would let… → Not changed in this pull request. The B16 brief lists 'record-class labels' as expected post-launch.
  - X-ESC-D3-05 — **DONE** — Masthead: the publisher's name as governed text; the 10 MB master PNG served on every page (DEBT-016). → DONE: the publisher's name is set in type in the lockup on every page (DL-D7-008; DEBT-016); its weight fixed by the EAD-03 logo derivatives (fbe9f27).
  - X-ESC-D3-06 — **DONE** — Arabic Home terminology: «قياس سكاني ممثل», «لا درجة واحدة», «إشارات من الأدلة», «ضمن نطاق الإبلاغ لديه», ISO range in Arabic prose, «أدلة» in the title. → RC-5 B2 a (1da995e; ARABIC_EDITORIAL_LEDGER.md B2-006…B2-036, 'One term per concept'); ISO dates in Arabic prose swept (2e1991d, gate RC-DATES). «أدلة» kept by owner decision B0 'Product name … unchanged' (OWNER_DECISIONS addendum). Certification stays REL-03.
  - X-ESC-D3-07 — **DONE** — Home label 'This resource presents the strongest defensible answer …' read as an untestable self-assessment. → RC-5 B3-025 (1da995e): UI-HERO-THIS-RESOURCE-PRESENTS-THE-STRONGEST rewritten ('so you can verify it'); 'strongest defensible' absent from dist/en/index.html.
  - X-ESC-D5-01 — **DONE** — An accessible cue that every external source link opens a new window. → UI-EXTERNAL-NEW-TAB governed in RC-3 (d668f11), shipped in G4 part 1 (7895694); dist pages carry '(opens in a new tab)' in link aria-labels.
  - X-ESC-D6-01 — **DONE** — VIS-PROVIDER-OBSERVABILITY: the five dimension headings of the matrix (UI-VIS-MATRIX-AUTHORITY … -OPERATION). → RC-3 (d668f11) governs the five headings; matrix drawn on /providers/ and its record in both languages (headers verified in dist/en/providers/index.html).
  - X-ESC-D6-02 — **DONE** — VIS-PROVIDER-OBSERVABILITY: class label of the payment-system-operators row (UI-VIS-CAT-PRV-CLASS-PSO). → RC-3 (d668f11): UI-VIS-CAT-PRV-CLASS-PSO governed; row prints UNKNOWN in every dimension with context events.
  - X-ESC-D6-03 — **DONE** — VIS-PROVIDER-OBSERVABILITY: English-only dated cells ('observed 2026-09-07', '2026-01-22 event', '2024 Q3 / 2025 H1', roster note) and '>9' in the Arabic editio… → RC-5 B2 g (1da995e): new 22_PROVIDERS_DATA columns reference_period_ar / reference_state_ar (B2-001…004); '>9' in label-value form (G4 item 7). dist/ar/providers/index.html prints «الربع الثالث 2024», «النصف الأول 2025»; no 'observed'/'roster' English found.
  - X-ESC-D6-04 — **RELEASE** — Export control in every drawn figure's foot: action labels and states (unavailable until the licence decision; licence; file format). → RELEASE: the licence is decided (CC BY 4.0, owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), E). What remains is that CauseWay's counsel confirms the CC BY 4.0 text; then public_downloads goes true, the downloads publish with the licence, and Dataset structured data may be added (REJ-03 lifts). docs/RELEASE_RUNBOOK.md step 2. The figure-foot export control follows the same switch. Same as X-ESC-ANT-05.
  - X-ESC-D6-05 — **DONE** — VIS-FIRM-CONSTRAINTS: rows FFO-2022-CH-09…16 exist only in a REFERENCE-role file; bind them. → DONE: rows FFO-2022-CH-09…16 bound in RC-7 (e82de29; ORIGINAL_SOURCE_VERIFICATION.md §2).
  - X-ESC-D6-06a — **DONE** — Rows requested for VIS-FIRM-FINANCE-PATH (/firms/ and its record). → RC-12, commit 98f43f5: FFO-2022-004 (31 of 328) and FFO-2022-LS-01..04 (10, 1, 5, 2 of 18) with a governed 'not established' marker row. The drawn path stays open as X-B12-VIS-FIRM-FINANCE-PATH-DRAWING.
  - X-ESC-D6-06b — **DONE** — Rows requested for VIS-FIRM-FINANCE-SEVERITY (/firms/ and its record). → B12 'Complete as designed (no table)' (98f43f5): values bound in the record (68.71 %, 23.13 %; 91.84 % derived). The separate base question is X-REG-SEVERITY-BASE.
  - X-ESC-D6-06c — **NEXT EDITION** — Rows requested for VIS-INCLUSION-TRANSMISSION (its record and Home): the system's relationships exist only as English prose in STRUCTURE/REFERENCE files. → Post-launch, as the B16 brief expects ('the 26 governed relationship statements, 21 lack references'): visuals/system_relationships.json holds 26 statements (SL-001…026), 21 without evidence references, English only. Same work as X-B12-VIS-INCLUSION-TRANSMISSION (its 13 relationships).
  - X-ESC-D6-07 — **NEXT EDITION** — RV-CWR-004 people lane: series carries x = 2022 while the lane is drawn as the fieldwork span read from ISO dates inside the period text; give the contract row … → Not changed in this pull request; the lane prints the governed period correctly, so the gain is binding robustness only.
  - X-ESC-D6-08 — **DONE** — Meta descriptions open with the page's own title (284 of 286), so a shared card reads the title twice. → RC-5 B3 b (1da995e) authored 126 routes' descriptions. Measured on current dist/: 40 of 286 (20 routes × 2 languages) still begin with the title: /accessibility/, /corrections/, /privacy/, /rights/, /terms/, /explore/, /readings/, three Readings and ten record pages (e.g. CLM-022, CLM-039, VIS-PAYMENT-RAILS) — routes B3 judged as passing; the social template prints the title once. If the residual 40 matter, POST-LAUNCH.
  - X-ESC-D6-09 — **DONE** — Credit lines: RV-CWR-001 names the IMF twice; VIS-REMITTANCE-MACRO credit covers IMF staff projections; RV-CWR-004 lists 'World Bank' twice; VIS-PROVIDER-OBSERV… → RC-6 / B4, commit fb2cf9b (Arabic credits; duplicates folded). Not verified here: the VIS-PROVIDER-OBSERVABILITY workshop credit and the VIS-REMITTANCE-MACRO projection-years credit — check before closing.
  - X-ESC-D6-10 — **DONE** — VIS-REMITTANCE-COST: MEASURED ('Measured in a survey') heads averages of RPW price quotes. → RC-1 item 8 b, commit 76aaeec (RC-1_MASTER_LEDGER.json item_8).
  - X-ESC-D6-11 — **DONE** — VIS-PAYMENT-RAILS: alt text names the e-money amendment of 9 July 2025, which the drawing's rows lack; the SUPPORTING contract carries no credit. → Owner Addendum 2 A1, RC-8 commit fda3965, gate RC-A1 with a negative control. The 'no credit' half was not verified here.
  - X-ESC-D6-12 — **DONE** — RV-CWR-009 / VIS-PAYMENT-RAILS: NETWORK_ACTIVITY_SIGNAL (an attributed CBY-Aden exhibition statement) evidences the OPERATION step (licence ≠ operation). → Adjudicated KEEP in RC-1 (76aaeec); RC-1_MASTER_LEDGER.json item_8.a gives the reason.
  - X-ESC-D6-13 — **DONE** — VIS-FIRM-CONSTRAINTS: nothing in the frame says the list is partial (8 of 16). → RC-1 added the partial-list note (Path B, 76aaeec); RC-7 bound all sixteen and removed it (e82de29).
  - X-ESC-D6-14 — **DONE** — RV-CWR-004 infrastructure lane and RV-CWR-009 activity rows: POS values lack the CBY-Aden reporting-scope qualifier, so a crop presents a CBY-Aden count as nati… → RC-1 item 5 (76aaeec); RC-8b adds the boundary wherever 1,651 prints (7947347).
  - X-ESC-D6-15 — **DONE** — Meta descriptions ending mid-sentence with '…' (Home, About, Data & sources) and Compare's instruction 'Select 2–4 records.' → RC-5 B3 b (1da995e). Measured on current dist/: 0 of 286 descriptions end with '…'.
  - X-ESC-D6-16 — **DONE** — A governed neutral header for a fallback-table value column whose rows carry different units (VIS-FINDEX-GAPS). → RC-3 label (d668f11); shipped G4 part 1 (7895694).
  - X-ESC-D6-17 — **DONE** — Arabic native-editor lens: count + unit noun ('561 العدد'), «نقاط مئوية», exchange-class labels as counted phrases, '>9 مشاركون', two index terms, 'Source:' col… → Label-value counts G4 item 7 (7895694); «نقطة مئوية» RC-3 item 20 (d668f11); «رقم قياسي» RC-5 B2 (1da995e); Arabic credits RC-6 (fb2cf9b); governed 'Source' corner label RC-12 (98f43f5); '>9 مشاركون' kept with stated reason in the ledger.
  - X-ESC-D7-01 — **DONE** — /people/ §02 says no education gap is in the evidence base while VIS-FINDEX-GAPS on the same page derives a 12.55 pp education gap (defect claimed). → RC-1 item 1, commit 76aaeec.
  - X-ESC-D7-02 — **DONE** — Search status reads '10 results shown' for 79 matches; needs a governed 'N of M' form and a way on. → RC-3 items 11 and 19 (d668f11); G4 item 1 (7895694).
  - X-ESC-D7-03 — **DONE** — /evidence/compare/: a governed sentence saying why 13 of the 110 records form the comparable set, for the intro and the 'not available for comparison' error. → RC-4 B7, commit ae0f3db (owner's wording). Note: it does not restate the evidence-state rule of Methodology §09; the owner's brief chose this sentence.
  - X-ESC-D7-04 — **NEXT EDITION** — /evidence/compare/ §01 'Three measures that cannot be combined': after a live comparison the worked example can read as analysis of the selected pair; a rubric … → Not changed. Owner Addendum 2 improvement 5 (a preset link ?records=CLM-001,CLM-054,FMIIP-BASELINE-2025-01 under that paragraph) is not in dist/ (grep found none); B15 d may build it, otherwise post-launch.
  - X-ESC-D7-05 — **DONE** — Home, /providers/, /measurement/: text-first frames ('Another view of the evidence') repeat governed prose and print the boundary twice. → Boundary-twice half fixed by A3 (7895694) and RC-5 B2 f (1da995e). The 'adds nothing' half is X-ESC-D3-01 and the B12 items.
  - X-ESC-D7-06 — **DONE** — Runtime: 'Cite this page' copies title, product and URL while the record citation carries more; neither has a preview. → RC-4 B9, commit ae0f3db; validator RC-GB and a browser test.
  - X-ESC-D7-07 — **DONE** — /payments/ and the Reading 'Same year, different number': one value in two magnitudes; two Arabic readers misread a YER-million series by a factor of a thousand… → RC-1 items 4 and 17 (76aaeec; audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md); unit disclosure corrected in RC-8b (7947347).
  - X-ESC-D7-08 — **DONE** — Findex fieldwork window in three forms across Home, /people/ and Compare; no canonical form to cite. → RC-5 B2 d (1da995e). Period, data and citation fields keep ISO by rule B2 c (stated in the ledger).
  - X-ESC-D7-09 — **DONE** — /payments/: a governed sentence beside VIS-POS-TRANSACTIONS naming the withheld H1 2025 release and why the monthly series is admissible. → RC-11 B11 (a95c7ef), revised by RC-11b inside RC-12 (98f43f5).
  - X-ESC-D7-10 — **DONE** — Compare tool Arabic copy: '2 سجلات مختارة', the 'select at least two' prompt shown with two loaded, the boundary printed twice. → RC-3 UI-JS-COMPARE-SELECTED (d668f11); G4 item 6 (7895694).
  - X-ESC-D7-11 — **DONE** — Arabic terminology: one concept, several governed terms (التحويلات / الحوالات المحلية; خدمة أموال عبر الهاتف المحمول / النقود الإلكترونية; المحفظة الاسمية; resi… → RC-5 B2 b (1da995e); term table in ARABIC_EDITORIAL_LEDGER.md. Certification stays REL-03.
  - X-ESC-D7-12 — **DONE** — CLM-003 and VIS-POS-TRANSACTIONS: legend says both figures are shown though the drawing plots one value per month. → RC-1 item 7, commit 76aaeec.
  - X-ESC-D7-13a — **DONE** — /data/ and /explore/: all 151 source cards print 'Reuse terms: not assessed', which reads as unfinished; a page-level statement would help. → RC-4 B8 (ae0f3db); the per-card label stays by owner decision OWN-04.
  - X-ESC-D7-13b — **NEXT EDITION** — 'P0 · People' on /explore/ and domain pages is expanded only on /measurement/; a governed gloss for the priority code at first use. → Post-launch: a governed gloss for 'P0' at first use on domain pages (copy, Master-first). Explore now says its priorities are the P0 items (UI-EXPLORE-MA-BASIS, RC-15 0a3ac6f).
  - X-ESC-D7C-01 — **DONE** — /evidence/compare/ (VIS-SOURCE-COMPARISON): alt_text ends with the prohibited inference, so two sentences print twice about 70 px apart. → A3 implemented in G4 part 1 (7895694): the Compare standfirst uses the accessible summary. Closes with X-ESC-PR8-A3.
  - X-ESC-D7C-02 — **NEXT EDITION** — /evidence/CLM-039/: the central comparison is qualitative (no years, interfaces or gap size); the 'earlier documented access' is undated. → Named in the B16 brief's expected post-launch list ('the CLM-039 comparison sentence'). CLM-039 is also a partial-lineage record (EXT-08).
  - X-ESC-D7C-03 — **NEXT EDITION** — Record question 7 summary 'Detail for reproducing or challenging this record without changing what it means' reads as internal meta-language. → Post-launch copy fix, Master-first (UI-EVID-ADDITIONAL-DETAIL-FOR-REPRODUCING-OR). The B15 panel found no task failure from it.
  - X-ESC-PR8-A3 — **DONE** — General finding: every frame prints its boundary twice because the generator ends all 36 alt_text with the prohibited inference while the foot prints it again. → G4 part 1, commit 7895694 (checks extended to count the visible text alternative); the eight residual frames fixed in RC-5 B2 f (1da995e). Closes when pull request #9 merges.
  - X-ESC-RC3-01 — **DONE** — VIS-PROVIDER-OBSERVABILITY Arabic edition: Arabic text for four English-only period values (WCR-001, WCR-002, WCR-004, PUC-MFI-2026-01). → RC-5 B2 g (1da995e); ARABIC_EDITORIAL_LEDGER.md B2-001…004.
  - X-ESC-RC3-02 — **DONE** — VIS-PROVIDER-OBSERVABILITY: a governed lead-in marking the payment-system operators' context events. → RC-5 B2 h (1da995e); label present in interface_copy.json.
  - X-ESC-G4-01 — **DONE** — Five governed accessible summaries restate their boundary, so eight frames still print it twice (VIS-REMITTANCE-MACRO EN/AR, VIS-POS-TRANSACTIONS EN, RV-CWR-003… → RC-5 B2 f (1da995e; B2-126…129 and the English pair, 'AR review 9'). check_visuals.py was not re-run here to confirm zero reports.
  - X-ESC-G5-01 — **DONE** — /data/: EAD-07 — a governed group label for the 9 sources without a document type, so a type filter hides none. → Label UI-DATA-DOCUMENT-TYPE-NOT-RECORDED in RC-4 (ae0f3db); type filter shipped in RC-12 B13 (98f43f5); dist/en/data has the 'none' option and 9 cards.
  - X-ESC-RC8-01 — **DONE** — Governed public_use of status events PSE-006, PSE-007, PSE-010, PSE-013, PSE-014 still allows the subject to be shown, against the owner's withholding rule; own… → DONE in RC-17 `a4ff911`: public_use of PSE-001…010, 012, 013 and 014 rewritten to the withholding rule, Master-first; RC-NAMES stays (owner decisions of 3 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md), point 1).
  - X-ESC-EAD01-02 — **DONE** — Search result-type facet: an accessible name and an 'all types' option. → RC-3 item 19 (d668f11); G4 part 1 (7895694).
  - X-ESC-EAD01-03 — **DONE** — Two navigation landmarks (nav.actions, nav.edges) share one governed name ('Continue from here'), 20 occurrences. → RC-11 B10 a (a95c7ef); axe landmark-unique 0 in the full audit (66521a3).
  - X-ESC-ANT-01 — **NEXT EDITION** — A domain facet in search needs a governed domain field on search records. → Owner Addendum 2 puts 'A domain search facet' into docs/ROADMAP_V1_1.md ('do not build now').
  - X-ESC-ANT-03 — **NEXT EDITION** — Evidence-workbench facet headings and values (verification state, domain), if a facet is designed. → No such facet designed; nothing raised. Not needed for launch.
  - X-ESC-ANT-04 — **NEXT EDITION** — Report-issue intent labels, if a richer reporting intent is designed. → Not designed; /contact/?record= ships.
  - X-ESC-ANT-05 — **RELEASE** — Reuse line and download labels after the licence decision (OWN-04). → RELEASE: the licence is decided (CC BY 4.0, owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), E). What remains is that CauseWay's counsel confirms the CC BY 4.0 text; then public_downloads goes true, the downloads publish with the licence, and Dataset structured data may be added (REJ-03 lifts). docs/RELEASE_RUNBOOK.md step 2. The reuse line and download labels follow the same switch. Same as X-ESC-D6-04.
  - X-ESC-ANT-06 — **NEXT EDITION** — IBM pre-split Latin font subsets (vendoring with provenance). → EAD-08 residual. B14 d measured the fonts as 71–87 % of a cold page (8c977f3); budget met without subsetting.
  - X-ESC-ANT-07 — **NEXT EDITION** — Rows for the other TABLE_TEXT_FIRST contracts whose rationale describes a table but resolves no rows. → Superseded in substance by the B12 dispositions (X-B12-* items).
  - X-ESC-B15-01 — **DONE** — About at 390 px (A-12, C-6): About is reachable only from the footer on a phone. → DONE `88a0f86`: the governed trust links, About first, are in the opened mobile menu; the session designated programme steward for this one patch (owner decisions of 3 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md), point 3).
  - X-ESC-B15-02 — **DONE** — Cite at 390 px (C-8): 'Cite this page' is in neither the mobile header nor the menu. → DONE `88a0f86`: the governed 'Cite this page' control is inside the opened mobile menu, not the header (owner decisions of 3 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md), point 3).
  - X-ESC-B15-03 — **NEXT EDITION** — A domain strip across the eight domain answers (C-10). → Roadmap (owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), A.4); docs/ROADMAP_V1_1.md item 28. The domains are reachable from the main navigation and Explore.
  - X-ESC-B15-04 — **DONE** — A naming rule for the twelve names of the 2024 e-wallet circular (B-2). → DONE in RC-17 `a4ff911`: all twelve names withheld alike; NEG-EW-011 rewritten in both languages as one wallet service among twelve; gate RC-NAMES covers the circular and the search index, with two negative controls (owner decisions of 3 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md), point 2).
  - X-ESC-B15-05 — **NEXT EDITION** — VIS-MFI-SPINE: a contract that binds the governed observations, gaps printed 'no usable observation — not zero' (B-7). → Post-launch (owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), A.5). Its title no longer promises a view of the gaps it does not draw (RC-16).
  - X-ESC-B15-06 — **RELEASE** — Exports for researchers: a versioned dataset, dated observation tables, a citation file (U3, U6, U7). → Licence decided: CC BY 4.0 for CauseWay's own content (owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), E). public_downloads stays false in this pull request; at release CauseWay's counsel confirms the CC BY 4.0 text, then the switch publishes the downloads, which carry the licence (docs/RELEASE_RUNBOOK.md step 2).
  - X-ESC-B15-07 — **DONE** — What CauseWay is (C-6): /about/ says who funds the resource mid-paragraph; nothing says what CauseWay is. → DONE in RC-17 `a4ff911`: the owner's pair on what CauseWay is, added to /about/ before the funding paragraph, in both languages (owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), D). Nothing else about the organisation is written.
  - X-ESC-RC17-01 — **RELEASE** — NEG-EW-011's record ID is the circular's own item number; with the circular linked, withholding the name does not withhold the identity (RC-17 adversarial revie… → The owner's choice at release acceptance: accept it as disclosed, or point /evidence/NEG-EW-011/ to CLM-015. Until then the record keeps its ID and route, as the owner decided (point 2); nothing prints a name.

### 4 October 2026 — closed by the owner decision of 3 October 2026, 23:54 Aden

- X-ESC-RC17-01 — **DONE** — Owner decision of 3 October 2026, 23:54 Aden (`audit/OWNER_DECISIONS_2026-10-02.md`):
  /evidence/NEG-EW-011/ is no longer published as its own record; its address leads to CLM-015, the aggregate record of
  the circular. Applied Master-first in RC-19 (the 02 and 06 rows removed; `site-src/hosting/moved_routes.json`; gate
  RC-19). The circular's names stay non-public lineage in 22_PROVIDERS_DATA, where RC-NAMES reads them. No other
  published per-entity record has an ID equal to an item number of a document it links: PSE-011, the only other
  per-entity record, carries the programme's own status-event number, not a number of Governor's Decision No. 9 of 2026.

## Raised at V1 design integration (9 October 2026)

Raised by the V1 gate (`DESIGN_INTEGRATION_V1.md`), each needed by an item of the owner's design-integration message
that a stylesheet alone cannot deliver. None is filled with authored copy, and no controlled contract is edited.

- `NEEDS_CONTROLLED_CONTENT — every page — currentness strip — a label for "evidence as of <date> · <version>" bound to
  the Master's verification date and edition, in both languages — without it the strip is not built.`
- `NEEDS_CONTROLLED_CONTENT — every page — Evidence Colophon — the single-Master statement, the version and short
  fingerprint labels, "as of", "next review" (only where governed) and the copyable citation line's label — the band is
  restyled (DL-V1-003) but carries only its present governed text until these exist.`
- `NEEDS_CONTROLLED_CONTENT — Home (`/`) §3 — a separator between the three figure records ("≠" or a governed phrase) —
  the cards are drawn (DL-V1-004); the separator is not, because a glyph a screen reader announces is copy.`
- `NEEDS_CONTROLLED_CONTENT — navigation, the five hubs and their breadcrumbs — a governed binding of the numerals 01–05
  to Explore, Evidence, Evidence Readings, Data & sources, Method & Measurement — the numerals are not generated by CSS.`
- `ESCALATE_TO_STEWARD (controlled contract, not changed) — navigation_interaction.json — utilities: cite and report
  move from the header to a page-tools row under each H1; mobile_menu: the five hubs, the eight domain answers, Trust and
  the language switch — the header keeps both links and the tools row is restyled in place (DL-V1-003).`
- `ESCALATE_TO_STEWARD (controlled contract, not changed) — presentation_priority.json and the renderer — the first two
  sections of a long page open, the rest named and collapsed; the phone-screen targets of the brief depend on it (and on
  DEBT-011 for /data/).`
- `DESIGN DEBT (renderer, HTML changes) — every page head with a governed clause break — the two-tone display headline
  needs the clause after the break wrapped by the renderer; not built while documents stay byte-identical.`
- `OWNER DECISION — typography — the Latin display serif of reference 02. Verified: Source Serif 4 release 4.005R
  (Adobe, adobe-fonts/source-serif; npm source-serif 4.5.1), SIL Open Font License 1.1, Reserved Font Name "Source";
  a subset is a Modified Version and must be renamed internally. Blocked by vendor/fonts/README.md ("use the files as
  shipped", "no other typeface"), CONTRIBUTING.md §2 (vendor/fonts changes only by a newer unchanged release),
  handoff/CLAUDE_DESIGN_MASTER_PROMPT.md (typography) and 08_ASSET_MAP.md §2. Plex Sans Arabic Bold 700 is not added
  (owner decision A1): unsubset it would take /ar/data/ over the 350 KB cold-page budget.`
- `ESCALATE_TO_STEWARD (records disagree; not acted on) — rights — the B16 disposition above records "Licence decided:
  CC BY 4.0 for CauseWay's own content", while the owner's message of 9 October 2026 (D6) states that no reuse licence
  has been issued. Raised so the record that is wrong is corrected by its owner, Master-first.`
  - **CLOSED 2026-10-10 by the owner** (`audit/OWNER_DECISIONS_2026-10-10.md`, OWN-04-R and OWN-04-R-a). The records
    did not disagree: the B16 disposition is right and stands. The owner's message of 9 October 2026 (D6, "we have no
    licence / لا نملك ترخيص") is about **regulatory** licensing — CauseWay is not a licensed financial institution and
    claims no such status — not about the reuse licence. CC BY 4.0 for CauseWay's own content stands, as adopted on
    3 October 2026 (`audit/OWNER_DECISIONS_2026-10-02.md`, section E; owner note of about 11:15 Cairo, 3.6). The rights
    question is closed. Nothing is corrected in the Master, a projection or a page: `/rights/` and `/terms/` already
    print CC BY 4.0 in both languages. The release step is unchanged — CauseWay's counsel confirms the CC BY 4.0 text
    (`docs/RELEASE_RUNBOOK.md` step 7a); `licence_text_confirmed` and `public_downloads` stay `false`. In Arabic, رخصة
    is the copyright licence and ترخيص is regulatory licensing.

Process note — V1 branch name (2026-10-09): V1 is developed and pushed on `claude/design-review-constraints-l9au89`, the
branch this execution environment may push, created at `main` `7557866e99c390a6db2fd63ca4a5c63a86ef7e3e`, instead of the
`design/integration-v1` name the owner's message plans; the convention of D1–D7. One gate, one branch, one pull
request. No design meaning attaches to the name. Acceptance is the owner's.

## Raised at V1 phase 2 (9 October 2026)

Raised by the V1 gate's phase 2 (`DESIGN_INTEGRATION_V1.md`, DL-V1-009…012): each would let disclosure go further than
the present contracts allow. None is applied; no controlled contract or Master row is edited.

- `ESCALATE_TO_STEWARD (controlled contract, proposal not applied) — presentation_priority.json — Home (/) has no
  Orientation entry, so no disclosure tier exists for it; a renderer-only tier would be a second contract. Proposed
  minimal addition (section orders as Home renders them today): {"route": "/", "page_family": "Orientation",
  "primary": [{"kind":"section","section_order":3},{"kind":"section","section_order":9}], "supporting":
  [{"kind":"section","section_order":4}], "always_visible_boundaries": [{"kind":"section","section_order":4}],
  "progressive": [{"kind":"section","section_order":5},{"kind":"section","section_order":6},
  {"kind":"section","section_order":7},{"kind":"section","section_order":8}], "first_load_exclusions": (the same four),
  "mobile_priority": [{"kind":"lead"},{"kind":"primary","position":1},{"kind":"supporting","position":1}]} — with the
  validator's Orientation shape check and the renderer reading it (Code, after the steward's change). Section 4 ("What
  should not be inferred?") stays always visible: it is a boundary, and the owner's message listing it among the named
  disclosures conflicts with the semantic firewall; the owner decides. Estimated effect on a phone: about −4 screens.`
- `NEEDS_CONTROLLED_CONTENT — /finance/ — a summary label for the chronology list (EN/AR, e.g. a count phrase of
  "dated events") distinct from UI-CHRONOLOGY-H, which is already the section's heading there — with it the 24-event list
  becomes the same disclosure as on /data/ (about −15 screens on a phone).`
- `NEEDS_CONTROLLED_CONTENT — /data/ source register — a summary label for a source row's detail (EN/AR, e.g. "About this
  source") — with it a row on a phone shows title, publisher, reference, the boundary line and the cite controls, and the
  description opens on demand; DEBT-011's locator-only path stays outside any disclosure. The steward also decides
  whether a source's "Does not establish" line may sit inside that detail (proposed: no).`
- `ESCALATE_TO_STEWARD (controlled contract, question) — presentation_priority.json — domain answers: the always-visible
  band (supporting tier) and the primary figure are first-load by contract; on /people/ they are ≈ 1.3 and ≈ 4.6 phone
  screens. Shorter first loads need a contract decision (for instance, the band's second boundary as progressive), not a
  renderer choice.`

## Closed at Phase B (9 October 2026)

The owner's decisions of 9 October 2026 (`audit/OWNER_DECISIONS_2026-10-09.md`) disposed of the V1 and V1 phase 2
escalations above as follows. The entries above are kept as raised.

- Currentness strip, Evidence Colophon, hub numerals, `/finance/` chronology summary, `/data/` source-row summary
  (NEEDS_CONTROLLED_CONTENT) — **CLOSED** by Master transaction V1B-1 (B-b) and built (`DESIGN_INTEGRATION_V1.md`,
  DL-V1-015…017). The steward's question on the source row is answered as proposed: "Does not establish" stays outside.
- `navigation_interaction.json` — utilities and mobile menu (ESCALATE_TO_STEWARD) — **CLOSED** by B-c: keys
  `page_tools`, `hub_numerals`, `mobile_menu` (DL-V1-014, DL-V1-015).
- `presentation_priority.json` — Home has no Orientation entry — **CLOSED** by B-a as proposed; section 4 stays always
  visible (DL-V1-013).
- Typography — the Latin display serif — **CLOSED, not adopted**: no Latin serif, IBM Plex stays, Arabic stays at
  SemiBold 600.
- Rights — the two records that disagree — **OPEN**: the owner left the choice open; no rights record or `/rights/`
  text changed.
- Still open, unchanged: the separator between Home's figure records (not part of B-b); the two-tone headline (design
  debt); the domain answers' always-visible band and primary figure (contract question, V1 phase 2, last entry);
  `/data/` DEBT-011.

Process note — Phase B branch (2026-10-09): Phase B is developed on `claude/design-review-constraints-l9au89`, restarted
from `main` at `b323a441` after pull request #15 merged, and goes to a new pull request; the convention of D1–D7.
Pull request #13 is untouched. Acceptance is the owner's.

Cross-reference (2026-10-10): the Rights line above (**OPEN** at Phase B) is superseded by the owner's decision of
10 October 2026 (`audit/OWNER_DECISIONS_2026-10-10.md`, OWN-04-R): CC BY 4.0 for CauseWay's own content stands and the
rights escalation is **CLOSED** (see its closure line under "Raised at V1"). The line above is kept as raised.

Cross-reference (2026-10-10, NB-1): the label half of C-10 ("'Data & sources' holds no data", raised at D6 above) is
closed by the naming transaction NB-1 — the hub is "Sources / المصادر" while nothing is downloadable
(`audit/naming/NAMING_DECISIONS_2026-10-10.md`). The domain-strip half stays as raised. The entries above are kept as raised.
