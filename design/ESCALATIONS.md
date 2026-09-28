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
- `NEEDS_CONTROLLED_CONTENT — VIS-PROVIDER-OBSERVABILITY — the class label of the fifth row (payment-system operators;
  UI-VIS-CAT-PRV-CLASS-PSO) — the contract's known gap: no governed universe row exists for the class; the row is
  designed as UNKNOWN in every dimension with the three institution events of RV-CWR-009 (REF-PAY-011…013) listed as
  context, never as a named universe. Design impact: the row renders the day the label exists; until then the matrix
  shows four classes.`
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

- D6 branch name (2026-09-27): D2–D5 were accepted together by the owner's merge of pull request #4 (`main` at `2effd8b`).
  D6 is developed and pushed on `claude/bold-maxwell-r3o015`, created at that exact `main`, instead of the
  `design/d6-visuals-social-print` name planned at D0; the same convention as D1–D5. One gate, one branch, one pull
  request into `main`. No design meaning attaches to the name.
