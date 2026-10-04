"""Builds open_items.json (read-only extraction for B16). Scratch tool; not part of the repository."""
import json, collections, pathlib

OUT = pathlib.Path(__file__).with_name("open_items.json")
ESC = "design/ESCALATIONS.md"
REG = "FINAL_OPEN_ITEMS_REGISTER.md"
B12 = "audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md"
LNK = "audit/release_candidate/LINK_CHECK.md"
DEBT = "design/DESIGN_DEBT.md"

def item(id, file, section, description, record_class, latest_line, disp, evidence):
    return dict(id=id, file=file, section=section, description=description, record_class=record_class,
                latest_line=latest_line, suggested_disposition=disp, evidence=evidence)

O = []
a = O.append

# ---------------------------------------------------------------- design/ESCALATIONS.md — Open
S = "Open › Raised at D1 (27 September 2026)"
a(item("X-ESC-D1-01", f"{ESC}; {DEBT}", S,
  "Home (/) §3: a controlled pacing marker so the build paces the governed 'three figures' paragraph without parsing connectives (alias DEBT-008).",
  "NEEDS_CONTROLLED_CONTENT; DEBT-008 (Medium; blocks neither, reclassified)",
  "2026-10-02 (DESIGN_DEBT DEBT-008, G5): \"does not block release — a fallback ships (the unpaced governed paragraph, no governed text altered); owner of the fix: the programme steward … and Design\"",
  "POST-LAUNCH",
  "Named in the B16 brief's expected post-launch list ('the DEBT-008 pacing marker'). Fallback ships (render.py paced_groups). Reclassified in G5 (30523ee; audit/RECORDS_RECONCILIATION_2026-10-02.md row 3). Owner: steward (marker, Master-first) and Design."))
a(item("X-ESC-D1-02", ESC, S,
  "RV-CWR-001 imf_staff_path carries evidence state REPORTED while the Reading calls the IMF path a staff reconstruction; should the lane carry an estimate state?",
  "ESCALATE_TO_MASTER (question; evidence authority)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"Firewall adjudications (item 8): RV-CWR-009 OPERATION KEEP; VIS-REMITTANCE-COST rpw MEASURED → REPORTED; RV-CWR-001 IMF staff path KEEP.\" (in-file latest: D2, 'open, non-blocking')",
  "DONE",
  "Adjudicated KEEP in RC-1, commit 76aaeec; audit/release_candidate/runs/RC-1_MASTER_LEDGER.json item_8.c (IMF rows carry calculation_state SOURCE_REPORTED__IMF_STAFF_CALCULATIONS). No closing line yet in ESCALATIONS.md."))

S = "Open › Raised at D2 (27 September 2026)"
a(item("X-ESC-D2-01", ESC, S,
  "Column labels for every drawn figure's fallback table (group/object, state, note); narrowed at D6 to the provider-matrix headings plus an empty corner cell (a preference).",
  "NEEDS_CONTROLLED_CONTENT (narrowed, DL-D6-003)",
  "D6 (27 September 2026): \"A governed label for a period / group / object column would still read better than the empty corner cell; a preference, not an authority gap.\"",
  "DONE",
  "Matrix headings governed in RC-3 (d668f11); every fallback table's row-header column labelled in RC-11 B10 b / NCC-02 (a95c7ef); last empty corner cell labelled in 66521a3. axe empty-table-header 0 (docs/ACCESSIBILITY_AUDIT.md)."))
a(item("X-ESC-D2-02a", ESC, S,
  "Rows requested for VIS-TARGET-RESULT-STATE (/reforms/ and its record): a TABLE_TEXT_FIRST contract that resolved no rows (baseline, target, absent result).",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (register §3, B12 line): \"of the 23 text-only contracts, 2 now render their designed table from governed rows (VIS-TARGET-RESULT-STATE, VIS-FIRM-FINANCE-PATH)\"",
  "DONE",
  "RC-12, commit 98f43f5: table bound to FMIIP-RF-004 (baseline Jan 2025 817; target Jun 2030 1,021; result row 'No observed result is held … — not zero'); gate RC-B12. The drawing stays open as X-B12-VIS-TARGET-RESULT-STATE-DRAWING."))
a(item("X-ESC-D2-02b", ESC, S,
  "Rows requested for VIS-MFI-DIVERGENCE (/finance/): the divergence table its rationale describes resolves no rows.",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (B12_TEXT_FIRST_DISPOSITIONS.md): \"All 17 go to B16 as POST-LAUNCH items unless the owner supplies the input sooner.\"",
  "POST-LAUNCH",
  "B12 names the missing input: a governed saver-definition crosswalk, a rial-valuation field per portfolio anchor, EN/AR labels for three state tokens, an Arabic universe state. Same work as EXT-10 and X-B12-VIS-MFI-DIVERGENCE."))

S = "Open › Raised at D3 (27 September 2026)"
a(item("X-ESC-D3-01", ESC, S,
  "A governed label for the description of a text-first frame (only UI-VIS-TEXT-ALTERNATIVE 'Text description of this view' exists; a Home reader took it for a missing diagram).",
  "NEEDS_CONTROLLED_CONTENT",
  "28 September 2026 (D7, restated): \"the D7 English reader read the frames as text-only boxes that add nothing. Design impact: as at D3.\"",
  "POST-LAUNCH",
  "No new label in site-src/content/content/interface_copy.json; dist/en/index.html still prints the heading as 'alt-h sr-only' (DL-D3-002). No reader harm; candidate for B15 d only if the panel finds a task failure."))
a(item("X-ESC-D3-02", ESC, S,
  "VIS-INCLUSION-TRANSMISSION: the governed alt_text ends by restating the prohibited inference, so the frame reads its boundary twice.",
  "ESCALATE_TO_MASTER (question)",
  "2026-10-02: \"a narrower statement of a general cause — every one of the 36 contracts' alt_text ends with the prohibited inference by one generator rule\"",
  "DONE",
  "Owner decision A3 / C3 implemented in G4 part 1, commit 7895694 (on the page the text alternative is the accessible summary; boundary once in the foot; checks extended). Closes with X-ESC-PR8-A3."))
a(item("X-ESC-D3-03a", ESC, S,
  "Home §3 cold-reader observations, terms and date forms: 'POS', 'CBY-Aden', 'wave', 'rails', 'enabling constraints', 'Evidence signals' not understood; three date forms for one window.",
  "ESCALATE_TO_MASTER (observations)",
  "27 September 2026 (D3): \"'POS', 'CBY-Aden', 'wave', 'rails', 'enabling constraints' and the label 'Evidence signals' were not understood cold.\"",
  "DONE",
  "RC-5, commit 1da995e: B3 a glosses / plain labels (B3-001…B3-024) and B2 d one prose form of the Findex window (ENGLISH_ and ARABIC_EDITORIAL_LEDGER.md). Checked in dist/en/index.html: 'Evidence signals' and 'enabling constraints' absent; 'wave (survey round)' printed. ISO clock lines stay ISO by rule B2 c."))
a(item("X-ESC-D3-03b", ESC, S,
  "Home §3 residue: same-wave figures at two decimals (18.35 %, 5.44 %, 12.91 points) read as false precision; three years attached to one number; period form 'Mar-2025–Jun-2026'.",
  "ESCALATE_TO_MASTER (observations)",
  "27 September 2026 (D3): \"the same-wave figures at two decimals (18.35 %, 5.44 %, 12.91 points) beside 11.9 % read as false precision to all four readers\"",
  "POST-LAUNCH",
  "Unchanged on dist/en/index.html (18.35%, 5.44%, 12.91 and 'Mar-2025–Jun-2026' still print). Source precision is governed; a display-precision or period-form rule is a Master-first content decision. Design impact none."))
a(item("X-ESC-D3-04", ESC, S,
  "CLM record 'Financial inclusion is a connected system, not a single score' is clocked like a measurement; a governed record kind (framing vs measured) would let the object relabel or omit the clock.",
  "ESCALATE_TO_MASTER (question)",
  "27 September 2026 (D3): \"readers noted a framing statement clocked like a measurement; the record grammar cannot tell them apart.\"",
  "POST-LAUNCH",
  "Not changed in this pull request. The B16 brief lists 'record-class labels' as expected post-launch."))
a(item("X-ESC-D3-05", ESC, S,
  "Masthead: the publisher's name as governed text; the 10 MB master PNG served on every page (DEBT-016).",
  "NEEDS_CONTROLLED_CONTENT; owner decision on a derivative",
  "2026-10-02 (DESIGN_DEBT DEBT-016): \"CLOSED 2026-10-02 (release candidate G4 item 2; owner decision EAD-03): every surface serves a pure Lanczos resample of the unchanged master\"",
  "DONE",
  "Publisher name in type in the lockup on every page (DL-D7-008, D7 resumption; DEBT-016 'the identification defect is closed'); weight fixed by EAD-03 derivatives, commit fbe9f27. Needs a closing line in ESCALATIONS.md."))
a(item("X-ESC-D3-06", ESC, S,
  "Arabic Home terminology: «قياس سكاني ممثل», «لا درجة واحدة», «إشارات من الأدلة», «ضمن نطاق الإبلاغ لديه», ISO range in Arabic prose, «أدلة» in the title.",
  "ESCALATE_TO_MASTER (Arabic, observations)",
  "27 September 2026 (D3): \"Design impact: none; a native-language review is an owner item and no certification is claimed.\"",
  "DONE",
  "RC-5 B2 a (1da995e; ARABIC_EDITORIAL_LEDGER.md B2-006…B2-036, 'One term per concept'); ISO dates in Arabic prose swept (2e1991d, gate RC-DATES). «أدلة» kept by owner decision B0 'Product name … unchanged' (OWNER_DECISIONS addendum). Certification stays REL-03."))
a(item("X-ESC-D3-07", ESC, S,
  "Home label 'This resource presents the strongest defensible answer …' read as an untestable self-assessment.",
  "ESCALATE_TO_MASTER (observation)",
  "27 September 2026 (D3): \"two readers read it as a self-assessment they cannot test\"",
  "DONE",
  "RC-5 B3-025 (1da995e): UI-HERO-THIS-RESOURCE-PRESENTS-THE-STRONGEST rewritten ('so you can verify it'); 'strongest defensible' absent from dist/en/index.html."))

S = "Open › Raised at D5 (27 September 2026)"
a(item("X-ESC-D5-01", ESC, S,
  "An accessible cue that every external source link opens a new window.",
  "NEEDS_CONTROLLED_CONTENT",
  "27 September 2026 (D5): \"Design impact: a governed phrase rendered visually hidden inside the link (or visibly after it) on every external locator.\"",
  "DONE",
  "UI-EXTERNAL-NEW-TAB governed in RC-3 (d668f11), shipped in G4 part 1 (7895694); dist pages carry '(opens in a new tab)' in link aria-labels."))

S = "Open › Raised at D6 (27 September 2026)"
a(item("X-ESC-D6-01", ESC, S,
  "VIS-PROVIDER-OBSERVABILITY: the five dimension headings of the matrix (UI-VIS-MATRIX-AUTHORITY … -OPERATION).",
  "NEEDS_CONTROLLED_CONTENT",
  "28 September 2026 (D7): \"the matrix is unshipped … until the six labels are governed (DL-D7-001); the built form and its export frame return the day they are\"",
  "DONE",
  "RC-3 (d668f11) governs the five headings; matrix drawn on /providers/ and its record in both languages (headers verified in dist/en/providers/index.html)."))
a(item("X-ESC-D6-02", ESC, S,
  "VIS-PROVIDER-OBSERVABILITY: class label of the payment-system-operators row (UI-VIS-CAT-PRV-CLASS-PSO).",
  "NEEDS_CONTROLLED_CONTENT",
  "28 September 2026 (D7): \"with the matrix unshipped (DL-D7-001) no class is hidden and no placeholder ships; the label is still needed for the matrix to draw at all.\"",
  "DONE",
  "RC-3 (d668f11): UI-VIS-CAT-PRV-CLASS-PSO governed; row prints UNKNOWN in every dimension with context events."))
a(item("X-ESC-D6-03", ESC, S,
  "VIS-PROVIDER-OBSERVABILITY: English-only dated cells ('observed 2026-09-07', '2026-01-22 event', '2024 Q3 / 2025 H1', roster note) and '>9' in the Arabic edition.",
  "ESCALATE_TO_MASTER",
  "27 September 2026 (D6): \"they print as the Master holds them, isolated left-to-right and marked lang=\\\"en\\\", in the Arabic frame too\"",
  "DONE",
  "RC-5 B2 g (1da995e): new 22_PROVIDERS_DATA columns reference_period_ar / reference_state_ar (B2-001…004); '>9' in label-value form (G4 item 7). dist/ar/providers/index.html prints «الربع الثالث 2024», «النصف الأول 2025»; no 'observed'/'roster' English found."))
a(item("X-ESC-D6-04", ESC, S,
  "Export control in every drawn figure's foot: action labels and states (unavailable until the licence decision; licence; file format).",
  "NEEDS_CONTROLLED_CONTENT; waits on OWN-04",
  "2026-10-02 (register OWN-04): \"licence deferred; launch is link-and-short-citation only; downloads and exports stay disabled\"",
  "POST-LAUNCH",
  "Waits on the owner's licence decision (OWN-04; docs/RELEASE_RUNBOOK.md step 2). Exports prepared behind public_downloads=false (1ca46dc). Same as anticipated item X-ESC-ANT-05."))
a(item("X-ESC-D6-05", ESC, S,
  "VIS-FIRM-CONSTRAINTS: rows FFO-2022-CH-09…16 exist only in a REFERENCE-role file; bind them.",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (register §3): \"VIS-FIRM-CONSTRAINTS, challenges 9–16 closed (RC-7, Path A): all sixteen values match Table 8 of the original (Annex III, p. 146)\"",
  "DONE",
  "RC-7, commit e82de29 (ORIGINAL_SOURCE_VERIFICATION.md §2). Needs a closing line in ESCALATIONS.md."))
a(item("X-ESC-D6-06a", ESC, S,
  "Rows requested for VIS-FIRM-FINANCE-PATH (/firms/ and its record).",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (register §3, B12 line): \"2 now render their designed table from governed rows (VIS-TARGET-RESULT-STATE, VIS-FIRM-FINANCE-PATH)\"",
  "DONE",
  "RC-12, commit 98f43f5: FFO-2022-004 (31 of 328) and FFO-2022-LS-01..04 (10, 1, 5, 2 of 18) with a governed 'not established' marker row. The drawn path stays open as X-B12-VIS-FIRM-FINANCE-PATH-DRAWING."))
a(item("X-ESC-D6-06b", ESC, S,
  "Rows requested for VIS-FIRM-FINANCE-SEVERITY (/firms/ and its record).",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (B12): \"Its rationale chooses the sentence: 'a sentence carries them better than a stacked bar, which invites a prevalence reading'.\"",
  "DONE",
  "B12 'Complete as designed (no table)' (98f43f5): values bound in the record (68.71 %, 23.13 %; 91.84 % derived). The separate base question is X-REG-SEVERITY-BASE."))
a(item("X-ESC-D6-06c", ESC, S,
  "Rows requested for VIS-INCLUSION-TRANSMISSION (its record and Home): the system's relationships exist only as English prose in STRUCTURE/REFERENCE files.",
  "ESCALATE_TO_MASTER (rows requested)",
  "2026-10-03 (B12): \"For each of the 13 system relationships: an evidence reference, a source id with a public locator, a governed evidence state, and Arabic text.\"",
  "POST-LAUNCH",
  "B12 'Not completable now' (rows in visuals/system_relationships.json are English only; SL-022..026 carry dataset ids only). The B16 brief's 'the 26 governed relationship statements (21 lack references)' is probably this item; the counts differ (13 vs 26) — check. Same work as X-B12-VIS-INCLUSION-TRANSMISSION."))
a(item("X-ESC-D6-07", ESC, S,
  "RV-CWR-004 people lane: series carries x = 2022 while the lane is drawn as the fieldwork span read from ISO dates inside the period text; give the contract row its own fieldwork start/end fields.",
  "ESCALATE_TO_MASTER (question)",
  "27 September 2026 (D6): \"if the Master gave the contract row its own fieldwork start and end fields, the lane would bind them directly\"",
  "POST-LAUNCH",
  "Not changed in this pull request; the lane prints the governed period correctly, so the gain is binding robustness only."))
a(item("X-ESC-D6-08", ESC, S,
  "Meta descriptions open with the page's own title (284 of 286), so a shared card reads the title twice.",
  "ESCALATE_TO_MASTER (observation)",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"B3: the English pass — plain register, consistent terms, and meta descriptions written as sentences of 155 characters or fewer.\"",
  "DONE",
  "RC-5 B3 b (1da995e) authored 126 routes' descriptions. Measured on current dist/: 40 of 286 (20 routes × 2 languages) still begin with the title: /accessibility/, /corrections/, /privacy/, /rights/, /terms/, /explore/, /readings/, three Readings and ten record pages (e.g. CLM-022, CLM-039, VIS-PAYMENT-RAILS) — routes B3 judged as passing; the social template prints the title once. If the residual 40 matter, POST-LAUNCH."))

S = "Open › Raised at D6 from the independent red-team lenses (27 September 2026)"
a(item("X-ESC-D6-09", ESC, S,
  "Credit lines: RV-CWR-001 names the IMF twice; VIS-REMITTANCE-MACRO credit covers IMF staff projections; RV-CWR-004 lists 'World Bank' twice; VIS-PROVIDER-OBSERVABILITY credits omit the FMIIP workshop's World Bank/UNDP.",
  "ESCALATE_TO_MASTER (observations)",
  "2026-10-03 (docs/CHANGELOG.md, RC-6): \"The generator (scripts/projection/derived.py) credits each institution once.\"",
  "DONE",
  "RC-6 / B4, commit fb2cf9b (Arabic credits; duplicates folded). Not verified here: the VIS-PROVIDER-OBSERVABILITY workshop credit and the VIS-REMITTANCE-MACRO projection-years credit — check before closing."))
a(item("X-ESC-D6-10", ESC, S,
  "VIS-REMITTANCE-COST: MEASURED ('Measured in a survey') heads averages of RPW price quotes.",
  "ESCALATE_TO_MASTER (question)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"VIS-REMITTANCE-COST rpw MEASURED → REPORTED\"",
  "DONE",
  "RC-1 item 8 b, commit 76aaeec (RC-1_MASTER_LEDGER.json item_8)."))
a(item("X-ESC-D6-11", ESC, S,
  "VIS-PAYMENT-RAILS: alt text names the e-money amendment of 9 July 2025, which the drawing's rows lack; the SUPPORTING contract carries no credit.",
  "ESCALATE_TO_MASTER (observation)",
  "2026-10-03 (docs/CHANGELOG.md, RC-8): \"A1 … the text alternative and record answer of VIS-PAYMENT-RAILS no longer name two steps the drawing lacks; new gate RC-A1\"",
  "DONE",
  "Owner Addendum 2 A1, RC-8 commit fda3965, gate RC-A1 with a negative control. The 'no credit' half was not verified here."))
a(item("X-ESC-D6-12", ESC, S,
  "RV-CWR-009 / VIS-PAYMENT-RAILS: NETWORK_ACTIVITY_SIGNAL (an attributed CBY-Aden exhibition statement) evidences the OPERATION step (licence ≠ operation).",
  "ESCALATE_TO_MASTER (question)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"RV-CWR-009 OPERATION KEEP\"",
  "DONE",
  "Adjudicated KEEP in RC-1 (76aaeec); RC-1_MASTER_LEDGER.json item_8.a gives the reason."))
a(item("X-ESC-D6-13", ESC, S,
  "VIS-FIRM-CONSTRAINTS: nothing in the frame says the list is partial (8 of 16).",
  "ESCALATE_TO_MASTER (observation)",
  "2026-10-03 (register §3): \"rows 9–16 are bound with labels in the source's item wording and the partial-list note is unbound.\"",
  "DONE",
  "RC-1 added the partial-list note (Path B, 76aaeec); RC-7 bound all sixteen and removed it (e82de29)."))
a(item("X-ESC-D6-14", ESC, S,
  "RV-CWR-004 infrastructure lane and RV-CWR-009 activity rows: POS values lack the CBY-Aden reporting-scope qualifier, so a crop presents a CBY-Aden count as national.",
  "ESCALATE_TO_MASTER (question)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"CBY-Aden scope on the RV-CWR-004 lane and RV-CWR-009 rows (item 5)\"",
  "DONE",
  "RC-1 item 5 (76aaeec); RC-8b adds the boundary wherever 1,651 prints (7947347)."))
a(item("X-ESC-D6-15", ESC, S,
  "Meta descriptions ending mid-sentence with '…' (Home, About, Data & sources) and Compare's instruction 'Select 2–4 records.'",
  "ESCALATE_TO_MASTER (observations)",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"meta descriptions written as sentences of 155 characters or fewer\"",
  "DONE",
  "RC-5 B3 b (1da995e). Measured on current dist/: 0 of 286 descriptions end with '…'."))
a(item("X-ESC-D6-16", ESC, S,
  "A governed neutral header for a fallback-table value column whose rows carry different units (VIS-FINDEX-GAPS).",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, G4 part 1): \"fallback tables whose rows carry different units head the value column with UI-VIS-VALUE-UNIT-PER-ROW (VIS-FINDEX-GAPS)\"",
  "DONE",
  "RC-3 label (d668f11); shipped G4 part 1 (7895694)."))
a(item("X-ESC-D6-17", ESC, S,
  "Arabic native-editor lens: count + unit noun ('561 العدد'), «نقاط مئوية», exchange-class labels as counted phrases, '>9 مشاركون', two index terms, 'Source:' colon heading a column, credits English-only.",
  "ESCALATE_TO_MASTER (observations, Arabic)",
  "2026-10-02 (ARABIC_EDITORIAL_LEDGER, 'Escalation items not changed'): \"«561 العدد», «98 شركات الصرافة» and «نقاط مئوية» after 12.91: none of these appear in dist/ar now\"",
  "DONE",
  "Label-value counts G4 item 7 (7895694); «نقطة مئوية» RC-3 item 20 (d668f11); «رقم قياسي» RC-5 B2 (1da995e); Arabic credits RC-6 (fb2cf9b); governed 'Source' corner label RC-12 (98f43f5); '>9 مشاركون' kept with stated reason in the ledger."))

S = "Open › Raised at D7 (28 September 2026), cold readers"
a(item("X-ESC-D7-01", ESC, S,
  "/people/ §02 says no education gap is in the evidence base while VIS-FINDEX-GAPS on the same page derives a 12.55 pp education gap (defect claimed).",
  "ESCALATE_TO_MASTER (defect claimed)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"/people/ §3–4 extend to the education and age gaps that VIS-FINDEX-GAPS draws (item 1)\"",
  "DONE", "RC-1 item 1, commit 76aaeec."))
a(item("X-ESC-D7-02", ESC, S,
  "Search status reads '10 results shown' for 79 matches; needs a governed 'N of M' form and a way on.",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, G4 part 1): \"the status gives the true total (UI-JS-SEARCH-RESULTS-OF, 'Showing 10 of {m} results') and a link carries the query to the Evidence directory\"",
  "DONE", "RC-3 items 11 and 19 (d668f11); G4 item 1 (7895694)."))
a(item("X-ESC-D7-03", ESC, S,
  "/evidence/compare/: a governed sentence saying why 13 of the 110 records form the comparable set, for the intro and the 'not available for comparison' error.",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, RC-4): \"B7 Compare: the 'selected set' sentence in the intro and under the 'record not available for comparison' error.\"",
  "DONE",
  "RC-4 B7, commit ae0f3db (owner's wording). Note: it does not restate the evidence-state rule of Methodology §09; the owner's brief chose this sentence."))
a(item("X-ESC-D7-04", ESC, S,
  "/evidence/compare/ §01 'Three measures that cannot be combined': after a live comparison the worked example can read as analysis of the selected pair; a rubric naming it a worked example would settle it.",
  "ESCALATE_TO_MASTER (observation)",
  "28 September 2026 (D7): \"a governed rubric naming it a worked example (or the section placed before the tool by the Master's section order) would settle it.\"",
  "POST-LAUNCH",
  "Not changed. Owner Addendum 2 improvement 5 (a preset link ?records=CLM-001,CLM-054,FMIIP-BASELINE-2025-01 under that paragraph) is not in dist/ (grep found none); B15 d may build it, otherwise post-launch."))
a(item("X-ESC-D7-05", ESC, S,
  "Home, /providers/, /measurement/: text-first frames ('Another view of the evidence') repeat governed prose and print the boundary twice.",
  "ESCALATE_TO_MASTER (observation, restated)",
  "28 September 2026 (D7): \"the D7 English reader read the frames as text-only boxes that add nothing. Design impact: as at D3.\"",
  "DONE",
  "Boundary-twice half fixed by A3 (7895694) and RC-5 B2 f (1da995e). The 'adds nothing' half is X-ESC-D3-01 and the B12 items."))
a(item("X-ESC-D7-06", ESC, S,
  "Runtime: 'Cite this page' copies title, product and URL while the record citation carries more; neither has a preview.",
  "RUNTIME (Code)",
  "2026-10-02 (docs/CHANGELOG.md, RC-4): \"B9 every page: a visible citation preview … 'Copy citation' copying exactly that text, and 'Print this page'.\"",
  "DONE", "RC-4 B9, commit ae0f3db; validator RC-GB and a browser test."))
a(item("X-ESC-D7-07", ESC, S,
  "/payments/ and the Reading 'Same year, different number': one value in two magnitudes; two Arabic readers misread a YER-million series by a factor of a thousand.",
  "ESCALATE_TO_MASTER (observation, strengthened)",
  "2026-10-03 (docs/CHANGELOG.md, RC-8b): \"From January 2026 they give the value in billions … The disclosure now says so in both languages\"",
  "DONE",
  "RC-1 items 4 and 17 (76aaeec; audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md); unit disclosure corrected in RC-8b (7947347)."))
a(item("X-ESC-D7-08", ESC, S,
  "Findex fieldwork window in three forms across Home, /people/ and Compare; no canonical form to cite.",
  "ESCALATE_TO_MASTER (observation, restated)",
  "2026-10-02 (ARABIC_EDITORIAL_LEDGER, item d): \"Arabic (prose): «من 7 نوفمبر 2022 إلى 9 يناير 2023». English (prose): '7 November 2022 to 9 January 2023'\"",
  "DONE",
  "RC-5 B2 d (1da995e). Period, data and citation fields keep ISO by rule B2 c (stated in the ledger)."))
a(item("X-ESC-D7-09", ESC, S,
  "/payments/: a governed sentence beside VIS-POS-TRANSACTIONS naming the withheld H1 2025 release and why the monthly series is admissible.",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-03 (docs/CHANGELOG.md, RC-11): \"VIS-POS-TRANSACTIONS gains one frame note, written only from governed fields.\"",
  "DONE", "RC-11 B11 (a95c7ef), revised by RC-11b inside RC-12 (98f43f5)."))
a(item("X-ESC-D7-10", ESC, S,
  "Compare tool Arabic copy: '2 سجلات مختارة', the 'select at least two' prompt shown with two loaded, the boundary printed twice.",
  "RUNTIME (Code) and NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, G4 part 1): \"the Compare prompt … shows only while fewer than two records are selected; the Compare status is in label-value form\"",
  "DONE", "RC-3 UI-JS-COMPARE-SELECTED (d668f11); G4 item 6 (7895694)."))
a(item("X-ESC-D7-11", ESC, S,
  "Arabic terminology: one concept, several governed terms (التحويلات / الحوالات المحلية; خدمة أموال عبر الهاتف المحمول / النقود الإلكترونية; المحفظة الاسمية; residual-model terms).",
  "ESCALATE_TO_MASTER (Arabic terminology)",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"B2 a–e: the Arabic observations recorded in design/ESCALATIONS.md; one Arabic term per concept\"",
  "DONE", "RC-5 B2 b (1da995e); term table in ARABIC_EDITORIAL_LEDGER.md. Certification stays REL-03."))
a(item("X-ESC-D7-12", ESC, S,
  "CLM-003 and VIS-POS-TRANSACTIONS: legend says both figures are shown though the drawing plots one value per month.",
  "ESCALATE_TO_MASTER (question)",
  "2026-10-02 (docs/CHANGELOG.md, RC-1): \"the disagreement legend, CLM-003 and the POS summaries describe only what is drawn (item 7)\"",
  "DONE", "RC-1 item 7, commit 76aaeec."))
a(item("X-ESC-D7-13a", ESC, S,
  "/data/ and /explore/: all 151 source cards print 'Reuse terms: not assessed', which reads as unfinished; a page-level statement would help.",
  "ESCALATE_TO_MASTER (observations)",
  "2026-10-02 (docs/CHANGELOG.md, RC-4): \"B8 /data/: the reuse terms stated once above the source list\"",
  "DONE", "RC-4 B8 (ae0f3db); the per-card label stays by owner decision OWN-04."))
a(item("X-ESC-D7-13b", ESC, S,
  "'P0 · People' on /explore/ and domain pages is expanded only on /measurement/; a governed gloss for the priority code at first use.",
  "ESCALATE_TO_MASTER (observation)",
  "2026-10-02 (ENGLISH_EDITORIAL_LEDGER): \"Finding 15 (a governed gloss of 'P0' beside the priority cards) needs a new label and a code change: taken up in Part B B15.\"",
  "POST-LAUNCH",
  "Only the label changed (UI-MA-PRIORITY 'Measurement priority', B3-026, 1da995e); dist/en/explore/index.html still prints 'P0 · People' with no gloss. B15 has not run (no audit/release_candidate/PRODUCT_CHALLENGE.md); DONE only if B15 d builds it."))

S = "Open › Raised at the D7 closure (28 September 2026)"
a(item("X-ESC-D7C-01", ESC, S,
  "/evidence/compare/ (VIS-SOURCE-COMPARISON): alt_text ends with the prohibited inference, so two sentences print twice about 70 px apart.",
  "ESCALATE_TO_MASTER (governed overlap)",
  "2026-10-02: \"a narrower statement of the same general cause as the D3 VIS-INCLUSION-TRANSMISSION item — the overlap is not a property of this contract's governed text\"",
  "DONE", "A3 implemented in G4 part 1 (7895694): the Compare standfirst uses the accessible summary. Closes with X-ESC-PR8-A3."))
a(item("X-ESC-D7C-02", ESC, S,
  "/evidence/CLM-039/: the central comparison is qualitative (no years, interfaces or gap size); the 'earlier documented access' is undated.",
  "NEEDS_CONTROLLED_CONTENT",
  "28 September 2026 (D7 closure): \"a governed sentence carrying the two spans (or their dates) would print in question 1 as any other governed value does.\"",
  "POST-LAUNCH",
  "Named in the B16 brief's expected post-launch list ('the CLM-039 comparison sentence'). CLM-039 is also a partial-lineage record (EXT-08)."))
a(item("X-ESC-D7C-03", ESC, S,
  "Record question 7 summary 'Detail for reproducing or challenging this record without changing what it means' reads as internal meta-language.",
  "ESCALATE_TO_MASTER (observation)",
  "28 September 2026 (D7 closure): \"Design impact: none — it is governed copy; a plainer governed gloss would print in place.\"",
  "POST-LAUNCH",
  "Unchanged: UI-EVID-ADDITIONAL-DETAIL-FOR-REPRODUCING-OR still reads so in interface_copy.json; not in B3's list. Cheap Master-first copy fix if B15 picks it up."))

S = "Open › Raised at the independent acceptance of pull request #8 (2 October 2026; A3 / C3)"
a(item("X-ESC-PR8-A3", f"{ESC}; {REG} §1 (2026-10-02 pointer line)", S,
  "General finding: every frame prints its boundary twice because the generator ends all 36 alt_text with the prohibited inference while the foot prints it again.",
  "ESCALATE_TO_MASTER (general finding; the steward's)",
  "2 October 2026: \"Implemented in the release-candidate pull request. Design impact: the frame's foot is unchanged; the text alternative loses its repeated tail. Open until that pull request lands.\"",
  "DONE",
  "G4 part 1, commit 7895694 (checks extended to count the visible text alternative); the eight residual frames fixed in RC-5 B2 f (1da995e). Closes when pull request #9 merges."))

S = "Open › Raised in the release-candidate pull request (2 October 2026), review of RC-3"
a(item("X-ESC-RC3-01", ESC, S,
  "VIS-PROVIDER-OBSERVABILITY Arabic edition: Arabic text for four English-only period values (WCR-001, WCR-002, WCR-004, PUC-MFI-2026-01).",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"the provider matrix prints Arabic periods and states (new 22_PROVIDERS_DATA columns reference_state_ar, reference_period_ar)\"",
  "DONE", "RC-5 B2 g (1da995e); ARABIC_EDITORIAL_LEDGER.md B2-001…004."))
a(item("X-ESC-RC3-02", ESC, S,
  "VIS-PROVIDER-OBSERVABILITY: a governed lead-in marking the payment-system operators' context events.",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"a governed context lead-in (UI-VIS-MATRIX-CONTEXT, 'Context:' / «السياق:»)\"",
  "DONE", "RC-5 B2 h (1da995e); label present in interface_copy.json."))

S = "Open › Raised in the release-candidate pull request (2 October 2026), A3 / C3 implementation"
a(item("X-ESC-G4-01", ESC, S,
  "Five governed accessible summaries restate their boundary, so eight frames still print it twice (VIS-REMITTANCE-MACRO EN/AR, VIS-POS-TRANSACTIONS EN, RV-CWR-003 AR, RV-CWR-005 AR).",
  "ESCALATE_TO_MASTER (Part B editorial pass, B2 / B3)",
  "2026-10-02 (docs/CHANGELOG.md, RC-5): \"B2 f (A3 escalation): accessible summaries that restated their figure's boundary drop the restating sentence.\"",
  "DONE",
  "RC-5 B2 f (1da995e; B2-126…129 and the English pair, 'AR review 9'). check_visuals.py was not re-run here to confirm zero reports."))

S = "Open › Raised in the release-candidate pull request (2 October 2026; G5)"
a(item("X-ESC-G5-01", ESC, S,
  "/data/: EAD-07 — a governed group label for the 9 sources without a document type, so a type filter hides none.",
  "NEEDS_CONTROLLED_CONTENT (EAD-07)",
  "2026-10-02 (docs/CHANGELOG.md, RC-4): \"sources with no governed type show 'Document type not recorded' (EAD-07).\"",
  "DONE",
  "Label UI-DATA-DOCUMENT-TYPE-NOT-RECORDED in RC-4 (ae0f3db); type filter shipped in RC-12 B13 (98f43f5); dist/en/data has the 'none' option and 9 cards."))

S = "Open › Raised at RC-8 (3 October 2026)"
a(item("X-ESC-RC8-01", ESC, S,
  "Governed public_use of status events PSE-006, PSE-007, PSE-010, PSE-013, PSE-014 still allows the subject to be shown, against the owner's withholding rule; owner to rewrite or record the override.",
  "ESCALATE_TO_MASTER (conflict recorded, nothing printed)",
  "3 October 2026: \"The other five are left as they are, for the owner to decide … Open, non-blocking: nothing prints a name.\"",
  "POST-LAUNCH",
  "site-src/content/data/providers_data.json still holds 'May show the exact dated … event and subject' (PSE-013/014) and '… branch-level status event' (PSE-006/007). Gate RC-NAMES (7387a70) fails any published entity name. Alternative: one cheap Master transaction now, rewriting the five fields to the withholding rule."))

S = "Raised at EAD-01 by Claude Code (29 September 2026)"
a(item("X-ESC-EAD01-02", ESC, S,
  "Search result-type facet: an accessible name and an 'all types' option.",
  "NEEDS_CONTROLLED_CONTENT",
  "2026-10-02 (docs/CHANGELOG.md, G4 part 1): \"A result-type filter (UI-JS-SEARCH-TYPE-FACET / -ALL, the governed type labels) narrows both searches\"",
  "DONE", "RC-3 item 19 (d668f11); G4 part 1 (7895694)."))
a(item("X-ESC-EAD01-03", ESC, S,
  "Two navigation landmarks (nav.actions, nav.edges) share one governed name ('Continue from here'), 20 occurrences.",
  "DESIGN_QUESTION (Code, EAD-02)",
  "2026-10-03 (docs/CHANGELOG.md, RC-11): \"Each edge group in the verification spine is now named by its own heading plus the page's h1.\"",
  "DONE", "RC-11 B10 a (a95c7ef); axe landmark-unique 0 in the full audit (66521a3)."))

S = "Anticipated (not yet raised)"
a(item("X-ESC-ANT-01", ESC, S, "A domain facet in search needs a governed domain field on search records.", "ANTICIPATED",
  "Brief §10 (recorded at D0, 27 September 2026): \"a domain facet needs a governed domain field on search records.\"",
  "POST-LAUNCH", "Owner Addendum 2 puts 'A domain search facet' into docs/ROADMAP_V1_1.md ('do not build now')."))
a(item("X-ESC-ANT-03", ESC, S, "Evidence-workbench facet headings and values (verification state, domain), if a facet is designed.", "ANTICIPATED",
  "Brief §10 (recorded at D0): \"Evidence-workbench facet headings/values (verification state, domain), if a facet is designed.\"",
  "POST-LAUNCH", "No such facet designed; nothing raised. Not needed for launch."))
a(item("X-ESC-ANT-04", ESC, S, "Report-issue intent labels, if a richer reporting intent is designed.", "ANTICIPATED",
  "Brief §10 (recorded at D0): \"Report-issue intent labels, if a richer reporting intent is designed.\"",
  "POST-LAUNCH", "Not designed; /contact/?record= ships."))
a(item("X-ESC-ANT-05", ESC, S, "Reuse line and download labels after the licence decision (OWN-04).", "ANTICIPATED",
  "2026-10-02 (register OWN-04): \"downloads and exports stay disabled; the 'reuse terms not assessed' wording stays.\"",
  "POST-LAUNCH", "Same dependency as X-ESC-D6-04 and OWN-04."))
a(item("X-ESC-ANT-06", ESC, S, "IBM pre-split Latin font subsets (vendoring with provenance).", "ANTICIPATED",
  "2026-09-29 (register EAD-08): \"IBM's pre-split Latin subsets are not used, and a self-made subset is an owner decision\"",
  "POST-LAUNCH", "EAD-08 residual. B14 d measured the fonts as 71–87 % of a cold page (8c977f3); budget met without subsetting."))
a(item("X-ESC-ANT-07", ESC, S, "Rows for the other TABLE_TEXT_FIRST contracts whose rationale describes a table but resolves no rows.", "ANTICIPATED",
  "2026-10-03 (B12): \"17 not completable now, each with its missing input named above.\"",
  "POST-LAUNCH", "Superseded in substance by the B12 dispositions (X-B12-* items)."))

# ---------------------------------------------------------------- FINAL_OPEN_ITEMS_REGISTER.md
S = "§1 ENGINEERING_AFTER_DESIGN"
a(item("EAD-02", REG, S,
  "Accessibility audit of the implemented site (automated and manual, screen readers in AR/EN, zoom, forced colours…); the Accessibility page states no result until then.",
  "ENGINEERING_AFTER_DESIGN (Claude Code, then an auditor)",
  "2026-10-02 (OWNER_DECISIONS addendum, Accessibility): \"The human accessibility audit is not a release gate, because no conformance is claimed … An external audit remains welcome after launch.\"",
  "POST-LAUNCH",
  "Code half done 2026-09-29 and extended in B10 (66521a3): 286 pages × 2 widths, 0 axe violations, keyboard walk; no conformance claimed. Remaining: screen-reader passes and human judgement, post-launch by owner decision."))
a(item("EAD-06", REG, S,
  "Tools: Compare entry from the 13 comparable records, mobile Compare, a result-type search facet and a ?q= URL state (domain facet needs a governed field).",
  "ENGINEERING_AFTER_DESIGN (Design, Code)",
  "2026-09-29 (row): \"The result-type facet is blocked, not deferred … The search status total ('10 of 79') stays blocked on the governed {n} of {m} form\"",
  "DONE",
  "Facet and N-of-M shipped in G4 part 1 (7895694) on RC-3 labels (d668f11); ?q= in 8ec2365. No dated closing line in the register. Domain facet: X-ESC-ANT-01 (post-launch)."))
a(item("EAD-07", REG, S,
  "A document-type filter on the source register, with a governed 'type not recorded' group for the 9 sources without document_label.",
  "ENGINEERING_AFTER_DESIGN (Design, Code)",
  "2026-10-03 (docs/CHANGELOG.md, RC-12): \"Filters by document type, publisher, document year and the domain page that uses the source\"",
  "DONE",
  "Label in RC-4 (ae0f3db); filter in RC-12 B13 a (98f43f5) with the 'Document type not recorded' option (verified in dist/en/data). No dated closing line in the register."))
a(item("EAD-08", REG, S,
  "IBM Plex self-hosted (done); open only on IBM's pre-split Latin subsets, a self-made subset being an owner decision.",
  "ENGINEERING_AFTER_DESIGN (Design, Code)",
  "2026-09-29 (row): \"Open only on the last part — IBM's pre-split Latin subsets are not used, and a self-made subset is an owner decision (the licence reserves the name 'Plex')\"",
  "POST-LAUNCH",
  "Optional; the B14 d budget is met without it (8c977f3). Owner decides on subsetting; a performance gain only."))
a(item("EAD-10", REG, S,
  "Remeasure bytes and requests on the implemented site and on the release host; set budgets only then.",
  "ENGINEERING_AFTER_DESIGN (Code)",
  "2026-10-03 (docs/CHANGELOG.md, B14 d): \"A provisional budget is recorded in docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json (release_candidate_b14d): 350 KB, 8 requests, LCP 2.5 s, load 3 s.\"",
  "RELEASE",
  "Implemented site measured (29 Sep) and budgeted locally under the host headers (8c977f3). What remains: Claude Code remeasures on the live host, docs/RELEASE_RUNBOOK.md step 10, and records it beside release_candidate_b14d."))
a(item("EAD-12", REG, S,
  "The 13 NO_GOVERNED_CONTRACT__TABLE_ONLY records: method text (now rendered) and the tables their state promises.",
  "ENGINEERING_AFTER_DESIGN (steward, Master-first)",
  "2026-10-02 (register): \"the 13 … record pages now print their governed method text in both languages … Table rows for the 13 stay post-launch; B16 records the disposition.\"",
  "POST-LAUNCH",
  "Method text DONE in B1 (d9df1d2; validator PB-0401). Table rows: post-launch per owner decision A4 / C6 and the B16 brief."))

S = "§2 RELEASE_ONLY"
a(item("REL-01", REG, S,
  "Security headers at the host: strict CSP, HSTS, nosniff, referrer and permissions policies.",
  "RELEASE_ONLY (Hosting, Code)",
  "2026-10-03 (docs/CHANGELOG.md, B14 b): \"HSTS stays commented out until HTTPS is confirmed on the release domain. GitHub Pages cannot set headers\"",
  "RELEASE",
  "Prepared: site-src/hosting/_headers → dist/_headers, test_security_headers.py 0 violations on 288 pages (1ca46dc). At release: owner account and credentials (runbook steps 1, 6, 7); Claude Code deploys, enables HSTS and runs the header test against the live host (steps 8–9)."))
a(item("REL-02", REG, S,
  "Reuse rights of the original sources not assessed (rights_state NOT_ASSESSED on all sources).",
  "RELEASE_ONLY (Owner, with counsel if needed)",
  "2026-10-02 (register OWN-04): \"launch is link-and-short-citation only; downloads and exports stay disabled; the 'reuse terms not assessed' wording stays. Not a gate for a link-and-citation launch.\"",
  "POST-LAUNCH",
  "The row's own closer is 'before anything beyond linking and short factual citation is published'; the owner chose a link-and-citation launch. Reuse terms stated once on /data/ (RC-4 B8, ae0f3db)."))
a(item("REL-03", REG, S, "Native-speaker certification of the Arabic corpus, if the owner wants one.", "RELEASE_ONLY (Owner)",
  "26 September 2026 (F9 register state): \"F5 accepted the corpus in both languages; that acceptance is not a certification and none is claimed\"",
  "POST-LAUNCH", "Optional by its own wording; the B2 Arabic pass (RC-5) and independent bilingual reviews are not a certification and the product claims none."))
a(item("REL-04", REG, S,
  "Named release acceptance: deployed mobile, RTL and accessibility checks, publication filtering, correction and version behaviour, legal checks where applicable.",
  "RELEASE_ONLY (Owner)",
  "2026-10-03 (docs/RELEASE_RUNBOOK.md, prepared): \"Release acceptance. The owner reviews the live site and the records, and accepts the release.\"",
  "RELEASE",
  "Owner, runbook step 13 (a dated, signed line in audit/OWNER_DECISIONS_*.md), after Claude Code's live checks (steps 9–10, with an in-country phone check by a person the owner names) and step 12 (no RELEASE item open)."))

S = "§3 EXTERNAL_EVIDENCE_DEPENDENCY"
a(item("EXT-04", REG, S,
  "Status-event table for /providers/ (15 events): needs governed Arabic event text (entity names dropped from the item on 3 October).",
  "EXTERNAL_EVIDENCE_DEPENDENCY",
  "2026-10-03 (register): \"EXT-04 narrowed … so 'Arabic entity names from the source instruments' is no longer part of this item; it stays open for the governed Arabic event text only.\"",
  "POST-LAUNCH",
  "No status-event table on /providers/ (its five tables are the matrix). The status events now carry governed bilingual class and state labels in the visual contract and bilingual decision titles (RC-8, RC-13), so the input may already suffice: Owner Addendum 2 improvement 6 (date · decision number · class · action under the matrix) would close it if B15 d builds it."))
a(item("EXT-05", REG, S, "Product-holding and mobile-access figures attributed to the OECD 2026 review, not verified against its text and not shown.", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "2026-10-03 (LINK_CHECK.md): \"SRC-OECD-YEM-RESILIENCE-001 | doi.org | NOT VERIFIABLE HERE — publisher refuses automated requests\"",
  "POST-LAUNCH", "Not read in this pull request; the product states they are not shown, so nothing is false meanwhile."))
a(item("EXT-06", REG, S, "The primary 2023 SFD/SMED loan-portfolio document behind 78,686 active microfinance borrowers (CLM-053, -054, -057).", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "2026-10-03 (FINAL_CURRENTNESS_CUTOFF.md): \"Remittance Prices Worldwide; SFD/SMED | Not readable from this session | NO CHANGE (stays as checked on 26 September 2026; EXT-06 open)\"",
  "POST-LAUNCH", "ORIGINAL_SOURCE_VERIFICATION.md §3: smed.sfd-yemen.org reset/503, NOT READ. RC-14 matched 78,686 to the Sana'a Center paper (secondary). CLM-053 states the gap."))
a(item("EXT-07", REG, S, "Findex subgroup unweighted base n and design-based uncertainty intervals.", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "26 September 2026 (F9 register state): \"Authorised microdata; reproduce the World Bank values first, then compute\"",
  "POST-LAUNCH", "Owner Addendum 2 sends 'The Findex 2021 weighted subgroup compute … needs the microdata file' to docs/ROADMAP_V1_1.md."))
a(item("EXT-08", REG, S, "Partial lineage on CLM-039, CLM-046, CLM-056 (and CWR-006 through CLM-056).", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "26 September 2026 (F9 register state): \"Each record page states that some inputs are not yet linked to a source\"",
  "POST-LAUNCH", "Not changed in this pull request; pages state the partial state. CLM-039 also X-ESC-D7C-02."))
a(item("EXT-09", REG, S, "Nine source records with a public locator but no governed title, publisher or document type.", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "26 September 2026 (F9 register state): \"A primary read of each; promote the metadata Master-first\"",
  "POST-LAUNCH", "Still 9 cards print 'Document type not recorded' on dist/en/data (counted). Now findable through the EAD-07 group; promotion needs a read of each."))
a(item("EXT-10", REG, S, "RV-CWR-005 and RV-CWR-008 hold values as governed text, not rows; VIS-MFI-DIVERGENCE's table has no resolved rows.", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "2026-10-03 (B12): \"All 17 go to B16 as POST-LAUNCH items unless the owner supplies the input sooner.\"",
  "POST-LAUNCH", "B12 names the inputs: IBS 2020 Tables (3)/(8) via origin table 198 for RV-CWR-005; SMEPS AR2024 pp. 8–9 via origin table 219 for RV-CWR-008 panel 3; saver crosswalk and rial-valuation field for VIS-MFI-DIVERGENCE."))
a(item("EXT-11", REG, S, "IFAD Sending Money Home 2026, deferred as a curated resource.", "EXTERNAL_EVIDENCE_DEPENDENCY",
  "26 September 2026 (F9 register state): \"The full report shown to publish a Yemen estimate with a documented method (F3 reopening trigger)\"",
  "POST-LAUNCH", "No reopening trigger recorded in this pull request."))

S = "§3, dated lines of 3 October 2026"
a(item("X-REG-LINK-C12", f"{REG} §3 (B13d line); {LNK} 'What stays open'", S,
  "SRC-CBY-SANAA-C12-2024 (CBY Sana'a circular 12 of 2024): no working address and no archived copy.",
  "Register line (no class); LINK_CHECK 'BROKEN — unresolved'",
  "2026-10-03 (register): \"Still open: SRC-CBY-SANAA-C12-2024, the CBY Sana'a circular 12 of 2024, has no working address and no archived copy.\"",
  "RELEASE",
  "A person with a browser re-checks at release (runbook step 4). If still dead, the steward decides Master-first whether the source may stay publicly named with a dead locator (AGENTS.md rule 5: no source named publicly without a public locator)."))
a(item("X-REG-LINK-AR2015", f"{REG} §3 (B13d line); {LNK} 'What stays open'; audit/FINAL_CURRENTNESS_CUTOFF.md", S,
  "SRC-CBY-AR2015-HIST-001 (centralbank.gov.ye): host unavailable (503); re-check at B14 e.",
  "Register line; LINK_CHECK 'HOST UNAVAILABLE'",
  "2026-10-03 (B14 e re-run): \"CBY Sana'a annual report 2015 host | locator held; 503 on 3 October 2026 | HTTP 503 | CHECK BY HAND\"",
  "RELEASE",
  "Person with a browser at release (runbook step 4); a 2022 web.archive.org snapshot exists as a Master-first fallback."))
a(item("X-REG-LINK-CDN14", f"{REG} §3 (B13d line); {LNK} 'What stays open'", S,
  "14 public locators refused by publishers' CDNs (IMF ×6, OECD ×2, MDPI, ResearchGate, UNDP, WB Fast Payments, RPW ×2): not broken, unverifiable here.",
  "Register line; LINK_CHECK 'NOT VERIFIABLE HERE'",
  "2026-10-03 (register): \"14 cannot be verified from this environment because the publisher's CDN refuses automated requests; a person checks them with a browser at release.\"",
  "RELEASE", "A person with a browser, at release (runbook step 4 / step 12)."))
a(item("X-LINK-TLS-SIGNIN", LNK, "Every check (outcomes not listed under 'What stays open')",
  "SRC-LIT-OEB-FX-PRICES-2025 (TLS chain does not verify here) and SRC-ADEN-CBY-LIQ-2016 (database record redirects to sign-in).",
  "LINK_CHECK outcomes 'NOT VERIFIABLE HERE — TLS' and 'SIGN-IN REQUIRED'",
  "2026-10-03 (LINK_CHECK.md): \"SRC-LIT-OEB-FX-PRICES-2025 | asjp.cerist.dz | NOT VERIFIABLE HERE — TLS | the host's certificate chain does not verify from this environment\"",
  "RELEASE",
  "Unsure whether open: LINK_CHECK does not list them under 'What stays open'. Suggest adding them to the browser check at release; a sign-in-only locator may also need a note under rule 5."))
a(item("X-REG-SFD62", f"{REG} §3; {LNK} 'What stays open'", S,
  "SFD newsletter No. 62 (Q2 2013) exists in two editions; bound values follow the original (archived) edition; decide whether a governed caveat names both.",
  "Register line (owner or steward)",
  "2026-10-03 (register): \"Action, owner or steward: decide whether a governed caveat names the two editions.\"",
  "POST-LAUNCH",
  "Bound values (88,169 / 175,447 / 7,845) follow the edition read; the current file's narrative agrees; locator is the archived original (ORIGINAL_SOURCE_VERIFICATION.md §6). A caveat is enrichment, not a correction; the steward could also decide 'no caveat' now."))
a(item("X-REG-FMIIP-ISR0", f"{REG} §3; {B12}", S,
  "FMIIP ISR sequence 2 prints 'Actual (Current) 0' for access points and beneficiaries — a reporting placeholder, not bound.",
  "Register line (decision recorded)",
  "2026-10-03 (register): \"That is a reporting placeholder, and it is not bound. The promotion condition of VIS-TARGET-RESULT-STATE stands\"",
  "DONE",
  "Unsure whether open: the line records a decision taken in RC-12 (98f43f5; B12 doc), with no further action. The residual drawing is X-B12-VIS-TARGET-RESULT-STATE-DRAWING."))
a(item("X-REG-SEVERITY-BASE", f"{REG} §3; {B12} 'Complete as designed'", S,
  "VIS-FIRM-FINANCE-SEVERITY base: source p. 145 places the tabulation under 'reasons of not applying', possibly narrower than the governed universe ('excludes firms that said they did not need a loan').",
  "Register line (action at B16)",
  "2026-10-03 (register): \"Action at B16: a governed limitation, or leave as is, after a reviewer reads p. 145.\"",
  "RELEASE",
  "A possible overstatement of a published universe is a truth risk; p. 145 was already read in RC-12 (ORIGINAL_SOURCE_VERIFICATION.md §6), so Claude Code (steward/editor) can add the limitation Master-first or record 'leave as is' before the release acceptance — or in B16 itself (then DONE)."))
a(item("X-REG-ORIGIN-TABLES", f"{REG} §3; {B12} 'A finding beyond B12'", S,
  "16_DATASET_CATALOG names four origin tables that are not sheets of the Master (173_CBY_ANNUAL_VINTAGES, 198_IBS2020_UPSTREAM, 201_MFB2023_RECON, 219_SMEPS_PROGRAMME_EVIDENCE).",
  "Register line (action at B16)",
  "2026-10-03 (register): \"Action at B16: bring the tables in, or record them as external working tables.\"",
  "POST-LAUNCH",
  "Records still trace to public originals through source ids. Bringing tables in is the same work as the B12 rows for RV-CWR-002, -005, -008; B16 can record them as external working tables now."))
a(item("X-REG-REGDOCS9", f"{REG} §3 (B14 e line); audit/FINAL_CURRENTNESS_CUTOFF.md", S,
  "Nine CBY-Aden regulatory documents linked on cby-ye.com/pages/14 are not in the evidence base (incl. Decision No. 7 of 2026 on deposit rates, Circular No. 1 of 2026 on virtual assets, e-KYC instructions).",
  "Register line (action at B16)",
  "2026-10-03 (register): \"Action at B16: decide which to add. Each must be read in the original and titled in both languages, Master-first.\"",
  "POST-LAUNCH",
  "The /data/ regulatory group already says it is 'not a complete register', so nothing printed is false. The e-KYC instructions (65806fe2b3757.pdf) bear on MECH-ID-KYC and are the strongest candidate."))
a(item("X-REG-HAND3", f"{REG} §3 (B14 e line); audit/FINAL_CURRENTNESS_CUTOFF.md", S,
  "Currentness watch points unreadable here: IMF SMP approval, Remittance Prices Worldwide after 2025 Q3, CBY Sana'a host; plus the re-run at the release date.",
  "Register line (release check)",
  "2026-10-03 (register): \"IMF, Remittance Prices Worldwide and the CBY Sana'a host cannot be read from here; they are checked by hand at release.\"",
  "RELEASE",
  "Claude Code runs scripts/currentness_rerun.py --append at the release date and moves UI-CONTENT-VERSION Master-first; a person checks the 'check by hand' points in a browser (runbook step 4)."))
a(item("X-REG-FIRSTSCREEN22", f"{REG} §3; audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md §8", S,
  "22 first-screen/drawn values not readable on 3 October: 13 IMF values (CR 26/80 Table 4, supplement Table 2), 4 RPW corridor costs, 4 FMIIP component start dates of July 2025 (UNDP), SFD's 93,118.",
  "Register line (open for release)",
  "2026-10-03 (register): \"Open for release (a person with a browser): 22 values whose hosts now refuse automated requests.\"",
  "RELEASE",
  "A person with a browser at release (runbook step 4). Priority: the UNDP July 2025 start dates, since the World Bank ISR gives project effectiveness as 1 September 2025 — a possible truth conflict."))

S = "§4 KNOWN_EVIDENCE_FRONTIER"
frn = [
 ("FRN-01", "CLM-044 residual-model value withheld (no public locator or rights assessment); must never print."),
 ("FRN-02", "Firm base (about 147) implied by the 91.84 % filtered enterprise table, and the question's exact wording, are not recorded."),
 ("FRN-03", "No crosswalk between CBY-Aden and IMF remittance levels; compared only as indices."),
 ("FRN-04", "The causes of the gender gap are not established."),
 ("FRN-05", "No reconciled view of current operating status across provider classes."),
 ("FRN-06", "Magnitude of the 2022 banking restatement not quantified until the two vintages are reconciled line by line."),
 ("FRN-07", "Composite records whose member records are not listed (9 Evidence Records)."),
 ("FRN-08", "World Bank Joint Food Security Monitor sub-national exchange-rate series, deferred as a curated resource."),
]
for i, d in frn:
    ev = "A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request."
    if i == "FRN-07":
        ev = ("Narrowed by one: VIS-EVIDENCE-FRESHNESS now lists its member records (RC-11b, a95c7ef) — dist/ shows the "
              "'summarises other evidence records, which are not yet linked' note on 8 records (CLM-014, DS-DEMAND-VINTAGE-LENS, six VIS-), not 9. Otherwise a frontier.")
    if i == "FRN-08":
        ev += " Owner Addendum 2 rejects 'Food-security monitoring' (to be recorded in B16), which supports keeping it out."
    if i == "FRN-05":
        ev += " The provider matrix (RC-3) shows dimensions without a roll-up, by design; Addendum 2 rejects a provider '2026 status' badge."
    a(item(i, REG, S, d, "KNOWN_EVIDENCE_FRONTIER",
      "26 September 2026 (F9 register state; no later dated line): the product states it; \"must never fill them with an estimate, a proxy or a colour.\"",
      "POST-LAUNCH", ev))

S = "§5 OWNER_INPUT"
a(item("OWN-02", REG, S, "Confirmation that office@causewaygrp.com is monitored.", "OWNER_INPUT",
  "2026-10-02 (register): \"owner decision … OWN-02: confirmed; office@causewaygrp.com is monitored.\"",
  "DONE", "Owner decision of 2 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md, row OWN-02). No 'closed' word in the register; nothing remains to do."))
a(item("OWN-03", REG, S, "The public origin (site-src/deployment.json public_origin).", "OWNER_INPUT",
  "2026-10-02 (register): \"OWN-03: the public origin is decided when hosting is ready; public_origin stays null until then.\"",
  "RELEASE", "Owner provides account and domain (runbook step 1); Claude Code sets public_origin and rebuilds (step 3); deploy workflow refuses a null origin (8c977f3)."))
a(item("OWN-04", REG, S, "A reuse licence for CauseWay content (and, separately, for the code).", "OWNER_INPUT",
  "2026-10-02 (register): \"OWN-04: licence deferred; launch is link-and-short-citation only; downloads and exports stay disabled … Not a gate for a link-and-citation launch.\"",
  "POST-LAUNCH", "Exports prepared behind public_downloads=false (1ca46dc); runbook step 2 turns them on after the decision and the codebook's bilingual review. Roadmap item 2."))
a(item("OWN-05", REG, S, "Stewardship decisions: maintenance resourcing, an analytics policy, Digital Public Good gaps.", "OWNER_INPUT",
  "2026-10-02 (register): \"OWN-05: CauseWay maintains the resource; whole-system review at each new edition; no fixed update cadence is promised; no analytics ship.\"",
  "DONE", "Owner decision of 2 October 2026. Note: Digital Public Good gaps are not addressed by the decision (non-public; nothing depends on it); optional cookieless counts are runbook step 11."))
a(item("OWN-06", REG, S, "A reversed (light-on-dark) logo, only if the design needs one.", "OWNER_INPUT",
  "26 September 2026 (F9 register state): \"Not requested yet\"",
  "POST-LAUNCH", "The accepted D7 design (owner acceptance 2 October 2026) places the canonical logo on a light field and needs none; dormant unless a future design asks."))

# ---------------------------------------------------------------- adjacent (referenced by the register)
a(item("DEBT-011", f"{DEBT} (referenced by {REG} EAD-07)", "Design-debt register",
  "/data/: the supporting-sources group is open by default, so the page is very long (about 50,000 px at 1440 px; Addendum 2: /ar/data/ 61,060 px at 390 px).",
  "DESIGN debt (Medium; blocks neither)",
  "28 September 2026 (D7 closure): \"OPEN — attempted and reverted at the D7 closure (DL-D7-010, reverted by DL-D7-013).\"",
  "POST-LAUNCH",
  "Not in ESCALATIONS or the register as an item (included because EAD-07 cites it). The B13 library filters (98f43f5) add a way through but keep the full list open by default. Owner Addendum 2 improvement 9 ('Make /ar/data/ compact by default') is a B15 d candidate; DONE only if built there."))

# ---------------------------------------------------------------- B12 — not completable now
S = "Not completable now — the missing input, named"
b12 = [
 ("VIS-MFI-DIVERGENCE", "TABLE_TEXT_FIRST", "A governed saver-definition crosswalk and a rial-valuation field on each portfolio anchor (its promotion condition); EN/AR labels for state tokens CONTRADICTION, VERIFIED_DEFINITION_QA, SECONDARY_BOUNDED_DEFINITION_OPEN; an Arabic universe state."),
 ("RV-CWR-006", "SUPPORTING", "The same as VIS-MFI-DIVERGENCE, whose anchors it draws."),
 ("RV-CWR-002", "SUPPORTING", "AR2022 vs AR2023 table: origin table 173_CBY_ANNUAL_VINTAGES is not a Master sheet; dual 2022 rows in cby_monetary.json come from another source; unit label 'YER billion' and vintage labels."),
 ("RV-CWR-003", "SUPPORTING", "A governed programme-lane label and crosswalk XW-FMIIP-005 as a data file (sits in sheet 33 only); largely duplicates RV-CWR-009 and VIS-PAYMENT-ANATOMY."),
 ("RV-CWR-005", "SUPPORTING", "Rows from the 2020 e-payment study (Table (3) p. 54, Table (8) p. 68) with governed EN/AR type labels, grouping marked DERIVED; origin table 198_IBS2020_UPSTREAM is not a Master sheet."),
 ("RV-CWR-007", "SUPPORTING", "A data file for hypotheses MECH-ID-KYC, MECH-DIGITAL-ACCESS, MECH-ACCESS-PROX, MECH-TRUST (sheet 32 only); income has no mechanism."),
 ("RV-CWR-008", "SUPPORTING", "Panel 3 rows from the SMEPS annual report 2024 (printed pp. 8–9); origin table 219_SMEPS_PROGRAMME_EVIDENCE is not a Master sheet."),
 ("RV-CWR-010", "SUPPORTING", "EN/AR labels for the ladder steps (or a mapping onto UI-VIS-CHAIN-*), and the reference period of the 45,460 recipients (not recorded, CLM-045)."),
 ("VIS-E-MONEY-RULE-STACK", "SUPPORTING", "One row per ceiling (value, currency, period); Arabic text for EMR-001..013; the rationale's '31 rows' does not match the 13 held."),
 ("VIS-FCP-REDRESS-PATH", "SUPPORTING", "Numeric limit and unit fields for the 10 and 14 business-day limits; Arabic step labels for FCP-ARCH-005..008 and -010."),
 ("VIS-FL-EVIDENCE-LADDER", "SUPPORTING", "Rung labels EN/AR; a data file for OECD-YEM-001/-002; Arabic for PA-CBY-FL-001..004; correct the stale 'no Yemen value' rationale when bound."),
 ("VIS-EVIDENCE-CLASS-LADDER", "SUPPORTING", "A governed class taxonomy with supports / does-not-support text per class, both languages (UI-LAND-CLASS-* has 7 classes, the summary names 6 types)."),
 ("VIS-INCLUSION-TRANSMISSION", "TABLE_TEXT_FIRST", "For each of the 13 relationships: evidence reference, source id with a public locator, governed evidence state, Arabic text (rows English only; SL-022..026 dataset ids only)."),
 ("VIS-EVIDENCE-GAPS", "TABLE_TEXT_FIRST", "A typed gap field on 10_MEASUREMENT_AGENDA with EN/AR labels for five types."),
 ("VIS-OECD-FCP-TIMELINE", "TABLE_TEXT_FIRST", "Event labels (no FCP entries in the event namespace); an event row in sheet 31 for the 2024 awareness release; a chain-step mapping; REF-FCP-001 and FCP-ARCH-002 English only."),
 ("VIS-MECHANISM-METRIC-BRIDGE", "TABLE_TEXT_FIRST", "Edge types reconciled with the governed relationship taxonomy (promotion condition)."),
 ("VIS-ACCESS-EVIDENCE-LAYER", "TABLE_TEXT_FIRST", "The MA-005 register of verified, dated operating locations (promotion condition)."),
 ("VIS-FIRM-FINANCE-PATH-DRAWING", "TABLE_TEXT_FIRST (drawing; not counted in B12's 17)", "Table bound in RC-12; a drawn path needs the 2022 questionnaire's skip logic or the microdata."),
 ("VIS-TARGET-RESULT-STATE-DRAWING", "TABLE_TEXT_FIRST (drawing; not counted in B12's 17)", "Table bound in RC-12; a drawn trajectory needs an observed result under FMIIP-RF-004's definition (ISR 2 has none)."),
]
for cid, tier, miss in b12:
    a(item(f"X-B12-{cid}", f"{B12}; {REG} §3 (2026-10-03 B12 line)", S,
      f"{cid.replace('-DRAWING', ' (drawing)')}: renders only as a text frame; missing input — {miss}",
      tier,
      "2026-10-03 (B12): \"All 17 go to B16 as POST-LAUNCH items unless the owner supplies the input sooner.\"",
      "POST-LAUNCH",
      "Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch."))

# ---------------------------------------------------------------- CLOSED
C = []
def closed(id, file, where):
    C.append(dict(id=id, file=file, closed_by=where))

closed("X-ESC-D6-RUNTIME", ESC, "RUNTIME_DEFECT Compare Arabic dates: 'CLOSED 2026-09-29 by Code (EAD-01 follow-on)'.")
closed("X-ESC-D2C-01", ESC, "Arabic credit line: 'Closed at D2 (27 September 2026)' — answered by the contract's language_note.")
closed("X-ESC-D2C-02", ESC, "Accessible name for in-page navigation: Closed at D2; DEBT-006 closed.")
closed("X-ESC-D2C-03", ESC, "Home section order: Closed at D2 — decided by the brief §4.5.")
closed("X-ESC-EAD01-01 (EAD-11)", ESC, "Question selection and grouping: '2 October 2026 — landed in the release-candidate pull request (G3) … Closed.' (720a8f8).")
closed("X-ESC-ANT-02", ESC, "'Type not recorded' anticipated item: 'Raised 2 October 2026' — superseded by X-ESC-G5-01.")
closed("EAD-01", REG, "Row: 'CLOSED 2026-09-29'.")
closed("EAD-03", REG, "2026-10-02 line: 'EAD-03 done (release candidate G4 item 2)' (fbe9f27).")
closed("EAD-04", REG, "Row: 'CLOSED 2026-09-29 with EAD-01'.")
closed("EAD-05", REG, "Row: 'CLOSED 2026-09-29'.")
closed("EAD-09", REG, "Row: 'CLOSED 2026-09-29'.")
closed("EAD-11", f"{REG}; {ESC}", "2026-10-02 line: 'EAD-11 landed (release candidate G3) … Disposition DONE' (720a8f8).")
closed("EXT-01", REG, "2026-10-03 line: 'EXT-01 closed (transaction RC-7, Path A)' (e82de29); the 2026-10-02 Path B line is superseded by it.")
closed("EXT-02", REG, "2026-10-03 line: 'EXT-02 closed (transaction RC-8)' (fda3965).")
closed("EXT-03", REG, "2026-10-03 line: 'EXT-03 closed (RC-8, owner note of 3 October 2026, point 1)' (fda3965).")
closed("OWN-01", REG, "2026-10-02 line: approved paragraph 'applied Master-first in the release-candidate pull request (transaction RC-2)' (722f08f).")
closed("X-REG-FIRMCH (VIS-FIRM-CONSTRAINTS 9–16)", REG, "2026-10-03 line: 'challenges 9–16 closed (RC-7, Path A)' (e82de29); the 2026-10-02 Path B line superseded.")
closed("X-REG-ENFDATES", REG, "2026-10-03 line: 'Closed: dates of the other 2026 enforcement decisions (RC-13)' (4a90371).")
closed("X-REG-ROSTER", REG, "2026-10-03 line: 'Exchange and remittance roster replaced (RC-8b)' — applied (7947347).")
closed("D7 (not a register item)", REG, "2026-10-02 line: owner records final D7 visual acceptance.")
closed("DEBT-016", f"{DEBT}; {REG} EAD-03 line", "'CLOSED 2026-10-02 (release candidate G4 item 2; owner decision EAD-03)'.")
for i in range(1, 8):
    closed(f"REJ-0{i}", REG, "§6 REJECTED / NO ACTION — decided; recorded so nobody reopens it.")
reg8 = ["Public copy held in build.py and app.js (AR-29, EN-09, TRUST-25)", "Reading-prose parity (BIL-05)",
        "RV-CWR-001 panel 2 and REF-PAY-001 locator (P3-B01)", "2025 remittance value in CBY-Aden 2025 annual report (P5-06)",
        "Duplicate chronology events, analytics labels, publisher gaps (P3-D02)", "CBY decisions 7, 8, 12 and 16 (U-04)",
        "Viewport and RTL testing at 320–400 px (U-10 part)", "Held Tranche B page blocks PB-0160/0161, 0322, 0345, 0374, 0470, 0520–0522, 0614",
        "Literal-audit heuristic (U-14) and duplicate page contracts (U-15)", "Two language-switch labels held as literals (F9)",
        "WITHHELD used as a visual marker without a drawing rule (F9)", "Inventory without collection bindings etc. (F9)",
        "Page Specs 'professional compression' rule (F9 run 2)", "Comparability flag as ungoverned UNKNOWN marker (F9 run 2)",
        "Architecture diagrams named an external tool etc. (F9 run 2)", "Required fonts not in the repository (F9 runs 1–3)",
        "POS charts' DISAGREEMENT note pointed to a non-public passport (F9 run 3)", "system_relationships.json classed as render input (F9 run 3)",
        "design/reference/out/ entering manifests from an archive (F9 run 2)", "Navigation relabel and domain pages without Readings (Tranche A)"]
for n, t in enumerate(reg8, 1):
    closed(f"X-REG8-{n:02d}", REG, f"§8 'Closed since first raised': {t}.")
closed("OWN-07", REG, "§8 'Closed by the post-F9 correction (27 September 2026)'.")
closed("OWN-08", REG, "§8 'Closed by the post-F9 correction (27 September 2026)'.")
for cid, how in [("VIS-TARGET-RESULT-STATE (table)", "Bound in RC-12 (98f43f5)"), ("VIS-FIRM-FINANCE-PATH (table)", "Bound in RC-12 (98f43f5)"),
                 ("VIS-FIRM-FINANCE-SEVERITY", "Complete as designed (a sentence by design)"), ("VIS-EVIDENCE-FRESHNESS", "Complete: evidence landscape table, RC-10 (ae86d2d), gate RC-LAND"),
                 ("VIS-SOURCE-COMPARISON", "Complete: the Compare tool renders it as a table"), ("VIS-CAPITAL-CONTEXT", "RETIRE_FROM_DESIGN; frame removed by owner decision A5 / C4 (7895694)")]:
    closed(f"X-B12-DONE-{cid.split(' ')[0]}{'-TABLE' if '(table)' in cid else ''}", B12, how + ".")
closed("X-LINK-MOVED5", LNK, "Five SFD newsletters moved to the publisher's new file names; read and matched; locators moved in RC-12 (98f43f5).")
closed("X-LINK-ARCHIVED4", LNK, "Four broken locators now point to the web.archive.org copy, labelled on the site (RC-12, 98f43f5).")

# ---------------------------------------------------------------- counts
cnt = collections.Counter(x["suggested_disposition"] for x in O)
by_file = collections.Counter(x["file"].split(";")[0].split(" ")[0] for x in O)
result = {
  "generated": "2026-10-03, read-only extraction at HEAD c055abc (branch code/release-candidate-fixes)",
  "rule": "Open = no later line in the item's own record says closed/done/resolved/applied/superseded and its status is not DONE/CLOSED. Items done in this PR but lacking a closing line are listed as open with suggested DONE.",
  "open_items": O,
  "closed_items": C,
  "counts": {
    "open_total": len(O),
    "open_by_suggested_disposition": dict(sorted(cnt.items())),
    "open_by_primary_file": dict(by_file),
    "closed_total": len(C),
    "notes": [
      "X-B12-* (19 entries) includes the two drawings that B12 does not count again; B12's own count is 17.",
      "Overlaps (same underlying work, separate record lines): X-ESC-D2-02b = EXT-10 (part) = X-B12-VIS-MFI-DIVERGENCE; X-ESC-D6-06c = X-B12-VIS-INCLUSION-TRANSMISSION; EXT-10 also = X-B12-RV-CWR-005 / -008; X-ESC-D6-04 = X-ESC-ANT-05 = OWN-04 dependency; X-ESC-PR8-A3 also covers the register §1 pointer line of 2026-10-02.",
      "DEBT-011 is adjacent (design/DESIGN_DEBT.md), included because register EAD-07 cites it.",
    ],
  },
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(result["counts"], ensure_ascii=False, indent=1))
