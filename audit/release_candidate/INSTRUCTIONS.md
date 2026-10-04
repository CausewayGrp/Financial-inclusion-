YFIE — RELEASE CANDIDATE, END TO END (one session and one pull request; if your context runs out, a new window resumes from the RESUME POINT)

MISSION
You are working on CausewayGrp/Financial-inclusion-: "Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن", a bilingual public evidence resource built and maintained by CauseWay. It takes a reader from a question to the strongest answer the evidence supports, then shows what that answer does not establish, what remains unknown, what should be measured next, and the record, method and original source behind it. The production runtime (PR #8) is merged and every gate on main is green.
Your job is to take main to a release candidate that is complete, true, professionally written in both languages, fully verified and ready to host: nothing undecided, nothing broken, nothing left for the owner except merging the pull request, providing the hosting account and domain, deciding the content licence, and signing the release. The quality bar is a senior international institution's flagship publication, in Arabic and in English. You do this in two parts on one pull request: Part A fixes everything already identified; Part B finishes, challenges and hardens the whole product.

OWNERSHIP AND STANDARD
- You own the outcome end to end. You decide, build, verify and report. The owner will not answer questions during the work: every decision you need is in this prompt or can be made from the repository and its sources. When you are unsure, investigate (the repository, the original sources, the built pages) and decide; record the reasoning.
- A problem you can fix within these rules, you fix. You escalate only what truly needs the owner, and you say exactly what and why.
- Nothing is "done" until you have checked it: run the gate, open the page, read the source. Never report a result you did not observe. Report failures as plainly as successes.
- Challenge your own work at every step: could this be clearer, truer, more useful, simpler, faster, more accessible? Act on the answer.
- Judgement over mechanics. The lists in this prompt are the minimum, not the ceiling, and the rules exist to protect truth, not to replace thought. If following an instruction literally would make a page less true, less clear or less useful to a reader, stop, record the conflict and do the right thing within the rules. If a TO string given in this prompt turns out to conflict with the original source, do not apply it: record the conflict and the corrected wording, and apply the corrected wording only if it passes the same rules. Specialist subagents must return specific findings with evidence from the built pages or the sources; reject generic or boilerplate output and send it back.

HOW YOU WORK
- You are the lead and the only one who decides and commits. Run dedicated subagents as specialists throughout, in parallel where the work is independent: a user-experience and interaction designer; an interface designer working inside the accepted D7 design system (refine, do not redesign); an information architect for navigation, search and discovery; an accessibility, mobile and right-to-left engineer; a performance and web-platform engineer; a data and survey-measurement specialist guarding the semantic firewall (people ≠ accounts, access ≠ use, infrastructure ≠ outcome, target ≠ result, licence ≠ operation, observed ≠ estimated ≠ projected, missing ≠ zero, chronology ≠ causality); a payments, remittances and provider-regulation specialist; a Yemen conflict-context specialist; a source, law and currentness librarian; a senior Arab economic editor; a senior institutional English editor; and a hostile-but-fair red team that reads as a Yemeni citizen, a journalist, a central-bank regulator, a bank, a microfinance provider, a payment or remittance provider, a researcher, a development-finance professional, a humanitarian actor, a donor and a source owner.
- Plan before you build: keep a written task list and work through it in order.
- See what users see: build the site, serve it locally, and inspect real pages in a headless browser at 320, 390, 768 and 1440 px in both languages, with screenshots you actually look at, not only scripted assertions.
- Verify against originals: when a fact, date, value or link matters, read the original source with your web tools. Never treat a secondary summary as the source.
- Check as you go: the fast gates after every change, the browser suites after every few commits, the red team before each group closes.

WINDOWS, CONTEXT AND HAND-OVER
- This task is larger than one context window. Expect to hand over several times; a hand-over is normal, not a failure. Work so that any moment is a safe stopping point: one atomic change at a time, pushed as soon as it is green.
- Watch your own context. When it has been compacted, or when you have finished a large group, assess whether the next group fits comfortably. If not, hand over at the boundary rather than inside a group.
- To hand over: finish or roll back the current atomic step (never stop inside a Master transaction or with an uncommitted change); run the commit ritual; push; write at the top of the PR description "RESUME POINT: <the exact next step, the item IDs done and not done, the state of the branch, and anything a fresh reader could not infer from git>"; then end with a message whose last line is exactly: RESUME POINT WRITTEN — OPEN A NEW WINDOW TO CONTINUE.
- Starting in a new window: git fetch origin; check out the pull request's branch; read audit/release_candidate/INSTRUCTIONS.md, the PR description and git log; verify the checklist against the repository itself (files, commits, gates), not against the ticks alone; run the baseline checks; then continue from the RESUME POINT. Do not redo finished items; do not re-plan what is already decided.
- The owner closes a window only when it has written RESUME POINT WRITTEN or the final line of this prompt. Only one window works on the repository at a time.

KEEPING GITHUB CURRENT
- One branch and one pull request for the whole task. Commit and push after every group of work and at least every 45 minutes; never keep unpushed work.
- After each push, check CI (Governance gates, Browser acceptance, Gate negative controls). If a job fails, fix it before starting the next group. Never leave the branch red.
- The pull request description is the live record: a checklist of every item (ticked as you go), a short dated progress log, and the RESUME POINT when there is one. Every commit adds a docs/CHANGELOG.md entry.
- Do not create other branches, do not delete branches, and do not push tags (sessions cannot; tags are owner steps in the release runbook).

RULES
- AGENTS.md and CONTRIBUTING.md govern. Read both in full before any change.
- Production Master first. Every content change goes through a transaction script and audit/tranche_b_execution/run_stage.py (CONTRIBUTING.md §4), English and Arabic together. Never hand-edit site-src/content/**, dist/** or audit/PUBLIC_LITERAL_CLOSURE.json. A file inside the runner's snapshot changes only through its generator or --install.
- site-src/content/content/navigation_interaction.json: do not edit.
- site-src/content/presentation_priority.json: the owner designates this session as programme steward for this file, for the EAD-11 patch in G3 only. No other edit to it.
- Never run audit/tranche_b_execution/post_execution_acceptance.py. Never rewrite historical audit records or register rows: append dated lines. Every new audit record gets its row in audit/INDEX.md (gate R85-G09).
- Never force-push, amend or rebase pushed commits; never commit to main directly; never touch a checkpoint/* tag; never commit ZIPs, caches, secrets or scratch files.
- Keep public_origin null in site-src/deployment.json until the release runbook sets it. Keep public downloads and exports switched off until the owner's licence decision (Part B prepares them behind a switch). Keep the 286 social images. Do not change the first line of handoff/README_FIRST.md. Do not alter the owner's canonical logo or font files (derivatives of the logo per EAD-03 are allowed).
- Architecture: the product is a static site generated from the Production Master, by design: it is secure, cheap to host, resilient on weak connections and easy to archive. Do not add a server, database, API service or third-party runtime dependency.
- Do not declare PUBLIC RELEASE READY. Do not claim WCAG conformance, legal review, rights clearance, native-language certification or security guarantees.
- In Part A, do not author interface copy this prompt does not give you; a missing governed label is appended to design/ESCALATIONS.md as NEEDS_CONTROLLED_CONTENT. Part B's owner designation widens this for Part B.
- Master commits carry the Transaction, Master-Before, Master-After and Findings trailers (CONTRIBUTING.md §3). Before every commit: git add -A && python3 scripts/repository_manifest.py && python3 scripts/checksums.py && git add -A, then python3 scripts/validate.py.
- Quality: before each Master transaction is committed, an independent subagent that did not write the change checks every English/Arabic pair for equal meaning, numbers, units, periods and populations; resolve every disagreement before committing.
- Context running low: follow WINDOWS, CONTEXT AND HAND-OVER.

OWNER RULES ON NUMBERS, PAGES AND CLOSED DECISIONS
1. No unsourced number or claim. A number or claim may be added only through the full Master-first path: read in the original source, bound to a source-traced record, written in both languages, accepted by the literal audit. Numbers that are already governed may be bound as rows of an existing visual contract.
2. No new page or route, unless the product challenge (B15) shows a task failure that cannot be fixed on an existing page and the red team agrees; such a page carries its full Page Spec, both languages, a search record and a social image, and passes every gate.
3. Closed decisions stay closed: dashboards, composite scores, league-table rankings, a synchronised "current state", an eleventh Measurement priority (REJ-02), Dataset structured data before downloads and a licence exist (REJ-03), a carbon figure (REJ-04), a fixed update cadence, a separate regulatory "record" route, and third-party or advertising trackers. Two are refined, not reopened: cookieless, first-party aggregate usage counts (B14) and international context from same-source aggregates (B15).

============================================================

PART A — RELEASE-CANDIDATE FIXES
This part implements (1) the owner's decisions of 2 October 2026, recorded in audit/OWNER_DECISIONS_2026-10-02.md; (2) the after-merge conditions and findings of the independent acceptance of PR #8 (audit/PR8_INDEPENDENT_ACCEPTANCE.md; the before-merge conditions C1–C5 were met before the merge, commit 38a9a97); and (3) the capabilities already built but held back only because a governed label was missing, with the exact labels given below.

G0 — START
1. git fetch origin. Confirm PR #8 is merged: audit/PR8_INDEPENDENT_ACCEPTANCE.md, audit/OWNER_DECISIONS_2026-10-02.md and scripts/yfie/ exist on origin/main. If not, stop, change nothing, and report "PR #8 NOT MERGED".
2. Create the branch code/release-candidate-fixes from origin/main. If this environment assigns a session branch, use it and say so in the PR.
3. Read: AGENTS.md, CONTRIBUTING.md, audit/OWNER_DECISIONS_2026-10-02.md, audit/PR8_INDEPENDENT_ACCEPTANCE.md, FINAL_OPEN_ITEMS_REGISTER.md, design/ESCALATIONS.md, design/09_CODE_HANDOFF.md, design/08_ASSET_MAP.md §1, audit/FINAL_CURRENTNESS_CUTOFF.md.
4. Baseline: python3 scripts/checksums.py --check and python3 scripts/validate.py must pass. Record the Master and Page Specs SHA-256 as you find them; never restore an older hash.
5. Save this whole prompt, unchanged, as audit/release_candidate/INSTRUCTIONS.md (with its audit/INDEX.md row), commit and push it, and open a draft PR titled "Release candidate: owner decisions of 2 October 2026, PR #8 acceptance conditions, and open items". The PR description links that file and holds a checklist of every item of Part A and Part B, ticked as you go, and the RESUME POINT when there is one.

G1 — OWNER DECISIONS (already recorded)
audit/OWNER_DECISIONS_2026-10-02.md was committed on PR #8 before the merge. It governs this pull request; do not rewrite it. Append one dated line ("2026-10-02 — owner decision, see audit/OWNER_DECISIONS_2026-10-02.md") under each affected row of FINAL_OPEN_ITEMS_REGISTER.md that does not have one yet (OWN-01 to OWN-05, EAD-03, EAD-11, D7), and add the register item for A4 / C6 (the 13 NO_GOVERNED_CONTRACT__TABLE_ONLY records; post-launch; no change in this edition). One docs commit, or none if nothing is missing.

G2 — MASTER TRANSACTIONS (content, English and Arabic together)
Write the transaction scripts under audit/release_candidate/ following CONTRIBUTING.md §4 (every cell write states the value it expects to replace). Use at most three transactions, each its own commit: RC-1 truth fixes (items 1–8, 16, 17), RC-2 trust copy (items 9, 10, 13, 14, 15), RC-3 governed interface strings (items 11, 12, 18, 19, 20). Locate every cell by its current text. If a FROM string is not found exactly once in the Master, stop that item, record what you found, and continue with the next.

1. /people/ education gap. The section text contradicts VIS-FINDEX-GAPS on the same page (design/ESCALATIONS.md, D7, "defect claimed").
   FROM EN: Among adults with primary education or less, 6.98% have an account; the matching figure for adults with more education is not in the evidence base, so no education gap is stated.
   TO EN: Among adults with primary education or less, 6.98% have an account, compared with 19.53% of adults with secondary education or more: a gap of 12.55 percentage points.
   FROM AR: وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، بينما لا تتضمن قاعدة الأدلة الرقم المقابل لمن تلقوا تعليمًا أعلى، ولذلك لا تُذكر فجوة بحسب التعليم.
   TO AR: وتبلغ نسبة امتلاك الحساب 6.98% بين البالغين الذين لم يتجاوز تعليمهم المرحلة الابتدائية، مقابل 19.53% بين الحاصلين على تعليم ثانوي فأعلى، أي بفارق 12.55 نقطة مئوية.
   Heading FROM: Measured gaps by sex and income — not yet explanations / فجوات مقاسة بحسب الجنس والدخل — من دون افتراض أسبابها
   Heading TO: Measured gaps by sex, income and education — not yet explanations / فجوات مقاسة بحسب الجنس والدخل والتعليم — من دون افتراض أسبابها
   The sentence rests on the records VIS-FINDEX-GAPS already binds (WB-FINDEX-OBS-2022-006 and WB-FINDEX-OBS-2022-007, source SRC-WB-FINDEX-AGG-2022). If the page boundary names only the sex and income gaps, extend it to education in the same wording it uses for them.

2. Compare description (VIS-SOURCE-COMPARISON summaries and the visual-library accessible summaries). The runtime compares definition, universe, period, method, source and currentness; it does not compare geography or unit.
   FROM EN: The comparison table sets the selected records side by side on definition, period, population or calculation base, source scope and method, and on geography and unit where these are recorded.
   TO EN: The comparison table sets the selected records side by side on definition, population or calculation base, period, method, source and currentness. Check geography and unit in each evidence record before comparing values.
   FROM AR: يضع جدول المقارنة السجلات المختارة جنبًا إلى جنب من حيث التعريف والفترة والمجتمع أو قاعدة الاحتساب ونطاق المصدر والطريقة، ومن حيث الجغرافيا والوحدة حيث تكون مسجلة.
   TO AR: يضع جدول المقارنة السجلات المختارة جنبًا إلى جنب من حيث التعريف والمجتمع أو قاعدة الاحتساب والفترة والطريقة والمصدر ومدى الحداثة. وتحقّق من النطاق الجغرافي والوحدة في سجل كل دليل قبل مقارنة القيم.

3. Methodology scope and the four IMF-attributed chronology events (register EXT-01: YSC-008, YSC-014, YSC-015 and YSC-017 cite IMF Country Report No. 26/80, which has not been read in the original; YSC-008 "from January 2023" is suspected to be October–November 2022; YSC-014 ratio units; YSC-015 wording; YSC-017 reserves of about US$350 million).
   Path A (preferred): read the report itself on imf.org. For each of the four events, confirm or correct date, value, unit and wording Master-first, recording the page or paragraph locator in the transaction ledger. If all four are confirmed or corrected, the Methodology lead sentence stays as it is and EXT-01 gets an appended closing line.
   Path B (only if the report cannot be read in this session): replace the Methodology lead sentence and flag the four events.
     FROM EN: Every published figure has been checked against the source it is attributed to.
     TO EN: Every figure on these pages and in the evidence records has been checked against the source it is attributed to. Dated events in the system chronology carry their sources; where an event has not yet been checked against its original document, this is stated with the event.
     FROM AR: رُوجِع كل رقم منشور هنا مقابل المصدر المنسوب إليه.
     TO AR: رُوجِع كل رقم في صفحات هذا المورد وسجلات أدلته مقابل المصدر المنسوب إليه. وتحمل أحداث السلسلة الزمنية مصادرها، وحيث لم يُراجَع حدث بعدُ مقابل وثيقته الأصلية يُذكر ذلك عنده.
     Flag on each of the four events: EN "Not yet checked against the original document." AR «لم يُراجَع بعدُ مقابل الوثيقة الأصلية.» Use an existing note or caveat field; if a new column is needed, follow CONTRIBUTING.md §9.
   Do one path, not both. Never treat a secondary summary of the report as the report.

4. POS-value notation (/payments/, /readings/same-year-different-number/ and their records; design/ESCALATIONS.md, D7, "strengthened at the D7 closure"). Two independent Arabic readers misread a YER-million series ("580.021, 795.006, 783.583, 910.688, 1,262") by a factor of a thousand, because one series mixes a decimal point and a thousands comma while the prose says "1.262 مليار ريال". Make every value in each affected series, and the prose that cites it, use one unit and one display precision, with the unit written next to the value, in both languages. Do not change any underlying source value, only the unit expression and the display precision. Record the source-native and displayed value of every point in the ledger. Acceptance: no displayed series mixes a decimal point and a thousands separator, and the prose and the table use the same unit.

5. CBY-Aden reporting scope (design/ESCALATIONS.md, D6: RV-CWR-004 infrastructure lane and RV-CWR-009 activity rows). The POS values carry "POS terminals · 561 Number" but not the CBY-Aden reporting-scope qualifier that the VIS-POS-* contracts' universe carries, so a crop presents a CBY-Aden count as national. Add that qualifier, in the exact governed wording the VIS-POS-* universe already uses, to the labels and alt text of these lanes and rows, in both languages.

6. VIS-FIRM-CONSTRAINTS (the contract names sixteen challenges; only FFO-2022-CH-01 to CH-08 are bound, so the figure reads as a complete ranking).
   Path A (preferred): FFO-2022-CH-09 to CH-16 already exist in the Master data (projected to site-src/content/data/firm_finance.json) with source SRC-WB-FSD-2024-001, locator "Annex III, Table 8 / Figure 108, p.146". Check each of the eight values and labels against that page of the original report, then bind them to the contract Master-first, so the figure and table show all sixteen. Keep the source's own caution: these are source-specific challenge rankings, not standard Enterprise Survey "biggest obstacle" indicators.
   Path B (only if the original cannot be read in this session): add a governed frame note instead.
     EN: Partial list: 8 of the 16 recorded constraints are shown.
     AR: قائمة جزئية: تُعرض 8 من أصل 16 قيدًا مسجّلًا.

7. CLM-003 and VIS-POS-TRANSACTIONS legend. The governed legend and claim say both figures are shown ("يُعرض الرقمان": the 8.55% computed change and the source graphic's +11%), but the drawing plots one value per month and the +11% appears only in prose. Correct the legend and claim wording, in both languages, so they describe only what is drawn and say where the +11% is stated. Do not add a row.

8. Three firewall questions in design/ESCALATIONS.md. Adjudicate each against its source and record CHANGE or KEEP, with the reason, in the ledger. Change only where the source does not support the current state.
   a. RV-CWR-009 and VIS-PAYMENT-RAILS: NETWORK_ACTIVITY_SIGNAL (an attributed CBY-Aden statement at an exhibition) evidences the OPERATION step (licence ≠ operation).
   b. VIS-REMITTANCE-COST: the state "Measured in a survey" heads averages of price quotes from Remittance Prices Worldwide.
   c. RV-CWR-001 imf_staff_path: the state is REPORTED while the prose describes an IMF staff reconstruction (observed ≠ estimated).

9. /about/ funding and relationships (owner-approved). Place it in the section headed "CauseWay's role, who remains authoritative, and how to check or challenge", directly after the paragraph that begins "CauseWay's role: CauseWay develops and maintains this resource."
   EN: Funding. CauseWay funded the development of this edition entirely from its own resources. No donor, regulator, source institution or external commissioning party funded it. This resource is not a deliverable of any contract or partnership with the institutions whose data it presents.
   AR: التمويل: موّلت CauseWay تطوير هذا الإصدار بالكامل من مواردها الخاصة، ولم تموّله أي جهة مانحة أو تنظيمية، ولا أي جهة ناشرة لمصدر، ولا أي جهة خارجية كلّفت به. وليس هذا المورد ناتجًا عن أي عقد أو شراكة مع المؤسسات التي يعرض بياناتها.

10. /corrections/: in the section headed "How history works", add:
   EN: This edition reflects what its sources showed when they were checked, up to 26 September 2026. It is not a continuous monitoring service: between editions, the resource states what it held on the edition date.
   AR: يعكس هذا الإصدار ما أظهرته مصادره عند مراجعتها حتى 26 سبتمبر 2026. وهو ليس خدمة رصد مستمر؛ فبين إصدار وآخر يعرض المورد ما كان لديه في تاريخ الإصدار.
   The date is the cut-off in audit/FINAL_CURRENTNESS_CUTOFF.md and Master 04 UI-CONTENT-VERSION. Do not change UI-CONTENT-VERSION in this PR.

11. Search status (design/ESCALATIONS.md, D7: a query with 79 matching records reads "10 results shown"). Add a governed interface string, UI-JS-SEARCH-RESULTS-OF, used when the runtime shows fewer hits than match; keep UI-JS-SEARCH-RESULTS for when all hits are shown.
   EN: Showing {n} of {m} results
   AR: النتائج المعروضة: {n} من {m}

12. Resource category label.
   FROM: Measurement standards and methods / معايير القياس ومناهجه
   TO: Measurement methods and international references / مناهج القياس ومراجع دولية

13. Chronology. Link YSC-012 to SRC-CBY-UNLICENSED-EWALLET-2024-001 and SRC-CBY-DEC-23-2024-001 (the two 26 June 2024 instruments). The public count chronology_events (site-src/content/content/public_inventory.json) is defined as "Dated events in the system chronology" but counts 24 rows, including YSC-020, which is an analytical rule, not a dated event (period "Current analytical rule", no source). Make the count follow its own definition (23), through the generator's counting rule, not by typing a number. Keep the /data/ line in label-value form, as the inventory rule requires for Arabic ("label: N"); if its wording says "events", it now counts only dated events.

14. Stale counts: update the count statements in Master sheets 00 and 37 to the derived values in site-src/content/content/public_inventory.json.

15. Publisher name: confirm no governed text prints an Arabic transliteration of CauseWay; if any does, replace it with "CauseWay" (Latin, isolated left-to-right in Arabic).

16. Governed content named by the acceptance (C9): the interface_copy.json use_rule "build.py _domain_labels[…]" points to code that no longer exists; correct it Master-first to the current location in scripts/yfie. Cite the acceptance item in the Findings trailer. (The double boundary of A3 is not a Master change: see G4 item 4.)

17. Four-digit unit check: run one check over every public figure of four or more digits for the failure in item 4 (a decimal point and a thousands separator mixed in one series, or no unit beside the value). Fix only true instances. Record the check and its result under audit/release_candidate/.

18. Provider observability matrix (design/ESCALATIONS.md, D6; DL-D7-001: the built matrix returns, without a code change, the day these six labels exist). Add to RC-3, wording taken from the contract's own governed alt text:
   UI-VIS-MATRIX-AUTHORITY — EN: Issuing authority or source — AR: الجهة المصدرة أو المصدر
   UI-VIS-MATRIX-UNIVERSE — EN: Dated list or count — AR: القائمة أو العدد المؤرخ
   UI-VIS-MATRIX-STATUS — EN: Dated status decisions — AR: قرارات الوضع المؤرخة
   UI-VIS-MATRIX-NEGATIVE — EN: Official lists of unlicensed names — AR: قوائم رسمية بالأسماء غير المرخصة
   UI-VIS-MATRIX-OPERATION — EN: Evidence of operation — AR: أدلة التشغيل
   UI-VIS-CAT-PRV-CLASS-PSO — EN: Payment-system operators — AR: مشغلو أنظمة الدفع
   Then confirm that /providers/ and the record page draw the matrix in both languages, with the payment-system operators row UNKNOWN in every dimension, and no placeholder anywhere.

19. Other missing labels for built features (add to RC-3):
   UI-JS-SEARCH-TYPE-FACET (accessible name of the result-type filter) — EN: Result type — AR: نوع النتيجة
   UI-JS-SEARCH-TYPE-ALL (the filter's no-type state) — EN: All types — AR: كل الأنواع
   UI-JS-SEARCH-SEE-ALL-EVIDENCE (the way on when hits are capped) — EN: See all matching evidence records — AR: اعرض كل سجلات الأدلة المطابقة
   UI-EXTERNAL-NEW-TAB (visually hidden inside every external source link that opens a new tab) — EN: (opens in a new tab) — AR: (يُفتح في علامة تبويب جديدة)
   UI-VIS-VALUE-UNIT-PER-ROW (header of a fallback-table value column whose rows carry different units) — EN: Value (unit given in each row) — AR: القيمة (الوحدة مذكورة في كل صف)
   UI-JS-COMPARE-SELECTED: FROM "records selected" / «سجلات مختارة» TO EN: Records selected: {n} — AR: السجلات المختارة: {n} (label-value form; the runtime fills {n}).

20. Arabic unit for percentage points: where a governed Arabic unit label prints «نقاط مئوية» after a value (12.91, 12.55, 11.1), change it to «نقطة مئوية», the form the governed prose already uses.

After each transaction: the runner must pass end to end, then the remaining gates; then commit and push.

G3 — EAD-11 (steward patch and code, one commit)
Apply the two entries recorded under EAD-11 in design/ESCALATIONS.md to site-src/content/presentation_priority.json, unchanged, installed through the runner with --install (CONTRIBUTING.md §9). Make the runtime read the Home starting questions and the Explore question groups from that file, delete scripts/yfie/question_sets.py, and prove that the built Home and Explore pages are byte-identical before and after, in both languages. The commit message names EAD-11.

G4 — CODE
1. Search status: use the item 11 string with the true total. When the runtime caps the hits, link the query to the Evidence directory (the ?q= state, EAD-06) with the item 19 label UI-JS-SEARCH-SEE-ALL-EVIDENCE.
2. EAD-03 logo derivatives: produce the sizes listed in design/08_ASSET_MAP.md §1 from site-src/assets/CauseWay_Master_Logo.png by resampling only (no crop, filter, recolour or mask), or one derivative of 50 KB or less covering all sizes. Serve them on every surface listed there, with width, height and alt="CauseWay". The master file stays byte-identical. If a gate asserts that a surface loads the master file, change the assertion to verify the derivative is a pure resample of the master, recording the derivative hashes; never delete an assertion. Re-measure cold page weight by the method already used for EAD-10, and record before and after.
3. Every remaining FAIL or CONDITION in audit/PR8_INDEPENDENT_ACCEPTANCE.md that is code: fix it, with a test or gate where one fits.
4. A3, the double boundary (owner decision A3 / C3). On the page, the image's alt attribute and the visible text alternative both use the governed accessible summary, which ends before the boundary; the boundary prints once, in the frame foot, so a sighted reader and a screen-reader user each meet it once per frame. Export frames and social frames, which leave the page, keep the full governed alt text. Do not change the 286 social images. Extend the design checks (boundary_once_in_foot, boundary_once_per_frame) so they count the visible text alternative too, not only the foot.
5. A5, the retired frame on /reforms/ (owner decision A5 / C4). Exclude the RETIRE_FROM_DESIGN tier from the domain depth frames (the family rule in scripts/yfie/families.py), so /reforms/ no longer shows VIS-CAPITAL-CONTEXT as a frame; its record link stays. Make check_visuals never_drawn reject a text frame for the RETIRE tier. Update design/06_VISUAL_TABLE_SYSTEM.md §1 to say the frame was removed by owner decision.
6. Ship the features unlocked by items 18–19: the result-type filter in search (EAD-06), the "see all" link when hits are capped, the visually hidden new-tab cue on every external source link, the mixed-unit column header where a fallback table's rows carry different units, and the Compare status in label-value form. In the Compare tool, show the "select at least two" prompt only while fewer than two records are selected, and print one boundary per tool state.
7. In the Arabic edition, a count printed with its unit noun inside a visual uses label-value form («العدد: 561», «شركات الصرافة: 98»), the rule public_inventory.json already sets for Arabic counts. No value changes.

G5 — RECORDS RECONCILIATION (one docs commit)
The before-merge conditions C1–C5 and the acceptance's one-line record fixes were made on PR #8. Do not redo them; confirm they still hold after your changes. Create audit/RECORDS_RECONCILIATION_2026-10-02.md (with its audit/INDEX.md row), one row per item below (finding, action, files). Where a file is generated or inside the runner snapshot, change it through its generator or --install.
- handoff/IMPLEMENTATION_MANIFEST.json implementation_target.ui: the Python production renderer in scripts/yfie, not "React static pre-render/export" (C9; runner snapshot).
- authority/YFI_CURRENT_PROJECT_CONTEXT.json: the sustainability pointer ("remeasure after Design and deployment") now points to docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json; only the host remains (C9).
- DEBT-008 (C8): reclassify it in design/DESIGN_DEBT.md as not blocking release (a fallback ships; A8), owner the steward and Design, consistent with README.md and the register.
- OPENAI_REENTRY_CHECKPOINT.md §4: if it still says the next work is Claude Design's, correct it.
- EAD-07: move its label request in design/ESCALATIONS.md from "Anticipated (not yet raised)" to raised.
- Historical ledgers that still show items open (audit/TRANCHE_C_FINDINGS_LEDGER.csv, audit/pre_tranche_c/FINDINGS_LEDGER.csv): do not edit them; state in the reconciliation record that register §8 governs.
- Minor: the master byte count in docs/SUSTAINABILITY_METHOD.md (the file is 10,018,081 bytes on disk); the deployment.json state label after the runtime cutover (keep public_origin null); the CHANGELOG reference to a "planning appendix of 29 September" that is not in the repository; the README statement on IBM Plex, consistent with the shipped runtime.
- README.md: after this pull request, its status names what this pull request changed and that the remaining open items are release-time only.

G6 — GATES AND HAND-BACK
1. Run every gate in CONTRIBUTING.md §5, including both browser suites and the full python3 scripts/tests/test_gate_negative_controls.py. scripts/tests/test_cutover_parity.py is a cutover artefact pinned to the projections it was frozen against; after a Master change follow its own docstring, and treat scripts/tests/test_content_parity.py as the standing content gate. If any gate compares against a frozen snapshot, regenerate the snapshot only through its documented procedure, and show that every difference traces to an item above. Never weaken a gate.
2. Run the commit ritual, add the CHANGELOG entry and push. Do not mark the PR ready for review yet.
3. Write the Part A report in the PR description:
   - a table: item → DONE / KEPT (reason) / ESCALATED (where) / NOT POSSIBLE (why);
   - Master SHA-256 before and after, and the transaction IDs;
   - each gate, pass or fail, and negative controls n/n;
   - cold page weight before and after;
   - anything that needs an owner decision (expected: none).
   End it with the line: PART A COMPLETE — CONTINUING WITH PART B. Then continue with Part B.

============================================================

PART B — FINISH, CHALLENGE AND HARDEN THE WHOLE PRODUCT (same session, same pull request)
Part B starts when the Part A report in the pull request description ends with "PART A COMPLETE — CONTINUING WITH PART B". Do the items in the order written, B0 to B17.

OWNER DESIGNATION FOR PART B
The owner designates this session as programme steward and as English and Arabic editor for Part B. You may author governed copy for Part B's items under these rules:
1. No new facts, numbers, sources, dates or claims except through the owner rules above. Wording comes from governed text already in the Master, from the original sources read in full, or restates them.
2. English and Arabic are written together and mean the same thing. Arabic counts use label-value form ("label: N"), as site-src/content/content/public_inventory.json requires.
3. Before each commit that adds or changes governed copy, an independent subagent that did not write it reviews every pair twice: as a senior Arab economic editor (Arabic first, independently of the English) and as a senior institutional English editor. Resolve every disagreement before committing.
4. No claim of WCAG conformance, native-language certification, legal review, rights clearance or security guarantees.

START OF PART B
1. If you are resuming in a new window, follow WINDOWS, CONTEXT AND HAND-OVER.
2. Baseline: python3 scripts/checksums.py --check and python3 scripts/validate.py must pass. Record the Master SHA-256.
3. Add the Part B checklist (B0–B17) to the PR description.

B0. Record the decisions. Append a dated section "Addendum — 2 October 2026 (Part B)" to audit/OWNER_DECISIONS_2026-10-02.md (append only) with these rows:
- A4 / C6 revised: the governed method text of the 13 NO_GOVERNED_CONTRACT__TABLE_ONLY records is rendered (B1).
- Accessibility: the human audit is not a release gate, because no conformance is claimed; it is replaced by the extended automated audit in B10. An external audit remains welcome after launch.
- Part B designation: this session is steward and English and Arabic editor for Part B.
- The owner rules on numbers, pages and closed decisions in this prompt, verbatim.
- Architecture: static site; no server, database or API service.
- Root language: the neutral root keeps opening the Arabic edition by default; the language switch stays on every page.
- Product name: "Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن" is unchanged.

B1. Method text on the 13 records. Make the renderer print the governed method text (method_en / method_ar) on the 13 NO_GOVERNED_CONTRACT__TABLE_ONLY record pages (scripts/yfie/content.py suppresses it today, around lines 343 and 561). If a record's method text fails the literal audit or reads as internal notes rather than reader-facing method, keep it suppressed for that record and say why in the ledger.

B2. Arabic editorial pass (you are the senior Arab economic editor). Master-first:
a. Every Arabic observation recorded in design/ESCALATIONS.md: the Home calques («قياس سكاني ممثل», «لا درجة واحدة», «إشارات من الأدلة», «ضمن نطاق الإبلاغ لديه»), the competing terms («التحويلات» / «التحويلات النقدية» / «الحوالات المحلية»; «خدمة أموال عبر الهاتف المحمول» / «النقود الإلكترونية»; «المحفظة الاسمية»; «نموذج المتبقي البديل» / «نموذج القيمة المتبقية»), «بالرقم القياسي» against «مؤشر، 2021 = 100», «مشاركون في الفعالية» against «مشاركين», and any other item the escalations list.
b. One Arabic term per concept across the corpus; keep two terms only where the English keeps two concepts apart (for example international remittances and domestic transfers).
c. ISO dates (YYYY-MM-DD) inside Arabic running prose become Arabic dates in words, matching the English; dates in tables, data cells and citations stay as they are.
d. One canonical form per language for the Findex fieldwork window wherever it appears in prose.
e. Up to 30 further Arabic defects (agreement, prepositions, calques, register, ambiguity) on /, /explore/, the eight domain pages, /about/, /methodology/ and the Readings.
Record every change in audit/release_candidate/ARABIC_EDITORIAL_LEDGER.md (location, FROM, TO, reason, English counterpart).

B3. English editorial pass (you are the senior institutional English editor):
a. Terms cold readers did not understand (design/ESCALATIONS.md: "POS", "CBY-Aden", "wave", "rails", "enabling constraints", "Evidence signals", "P0 · People" on /explore/, the Home line "This resource presents the strongest defensible answer …"): expand at first use on each high-traffic page or use a plain governed label, in both languages, without changing meaning.
b. Meta descriptions that end with "…", stop mid-sentence, or are instructions (Compare: "Select 2–4 records."): replace each with a complete description of at most 155 characters, with its Arabic, using only facts from that page.
Record every change in audit/release_candidate/ENGLISH_EDITORIAL_LEDGER.md.

B4. Arabic credit lines. Credits print in English in the Arabic edition. Add Arabic credits with the institutions' Arabic names (for example البنك الدولي، صندوق النقد الدولي، البنك المركزي اليمني – عدن، شبكة اليمن للتمويل الأصغر), keeping an acronym in parentheses where the English uses it; if this needs a new Master column, follow CONTRIBUTING.md §9. Correct the credit duplications recorded in design/ESCALATIONS.md (RV-CWR-001 names the IMF twice; RV-CWR-004 lists "World Bank" twice) where the source supports a single credit.

B5. Regulatory documents on /data/. Group the sources whose document_label is Enforcement decision, Circular or instruction, Regulatory decision, Regulation, or Official list or roster under one heading with one scope line:
   Heading — EN: Rules, decisions and official lists — AR: القواعد والقرارات والقوائم الرسمية
   Scope — EN: These are the regulatory documents held in this evidence base, not a complete register of Yemen's financial regulation. — AR: هذه هي الوثائق التنظيمية المتوفرة في قاعدة الأدلة هذه، وليست سجلًا كاملًا للتنظيم المالي في اليمن.
   Sources with no document_label (EAD-07) — EN: Document type not recorded — AR: نوع الوثيقة غير مسجّل

B6. Measurement linkage. Link each of the 10 Readings to the one or two Measurement Agenda priorities whose stated purpose addresses that Reading's stated unknown, Master-first, with a justification per link in audit/release_candidate/MEASUREMENT_LINKS.md that quotes both. Render the links on each Reading page. Make every priority, MA-009 included, reachable from at least one Reading or domain page where it genuinely belongs. If the priorities' decisions_unlocked and blocked_evidence fields (or their equivalents) are governed and complete in both languages, show them on /measurement/; otherwise record what is missing.

B7. Compare. Add to the Compare intro, and to the note under the "record not available for comparison" error:
   EN: Compare offers a selected set of evidence records in this edition. A record that is not offered here can still be read in full on its own page; its absence from Compare is not a judgement about it.
   AR: تتيح أداة المقارنة في هذا الإصدار مجموعة مختارة من سجلات الأدلة. ويمكن قراءة أي سجل غير متاح هنا كاملًا في صفحته، وغيابه عن المقارنة ليس حكمًا عليه.

B8. Reuse terms, stated once. Above the source list on /data/ (keep the per-card label):
   EN: This resource links to original sources and quotes them briefly. It has not assessed the reuse terms of any source; check each source's own terms before reusing its content.
   AR: يربط هذا المورد بالمصادر الأصلية ويقتبس منها باختصار. ولم يُقيّم شروط إعادة استخدام أي مصدر؛ فتحقّق من شروط كل مصدر قبل إعادة استخدام محتواه.

B9. Citation and print. One citation template from the governed citation fields (publisher, edition, period, population, URL) for both the page and the record citation, with a visible preview before copying; a visible print control on every page using the existing print styles. Reuse existing labels; otherwise: EN Print this page / AR اطبع هذه الصفحة; EN Citation preview / AR معاينة الاستشهاد; EN Copy citation / AR انسخ الاستشهاد.

B10. Accessibility, extended automated audit.
a. Distinct accessible names for the two navigation landmarks that share one (nav.actions and nav.edges; EAD-02), using existing governed headings where one fits.
b. A governed label for the empty table corner headers (NCC-02) that fits each table.
c. Run the repository's accessibility audit (docs/ACCESSIBILITY_AUDIT.md) over all pages in both languages, plus a keyboard walk of every interactive tool (search, filters, Compare, citation, print, language switch). Fix every violation. Update docs/ACCESSIBILITY_AUDIT.md. Claim no conformance.

B11. /payments/: one frame note beside VIS-POS-TRANSACTIONS naming the withheld H1 2025 transactions release and why the monthly series beside it is admissible, written only from the record's governed fields; if a needed fact is not recorded, record what is missing.

B12. Text-first visuals become tables or drawings. For each of the 24 visual contracts that render only as text frames, check whether every value the contract needs is already governed and source-bound, or can be bound from a source already in the source library and read in the original. Where it is, bind the rows Master-first so the contract renders in its designed form (the table pattern of design/06_VISUAL_TABLE_SYSTEM.md §4, or its drawing where the design exists), with red-team review. Start with VIS-TARGET-RESULT-STATE, VIS-MFI-DIVERGENCE and RV-CWR-006, VIS-FIRM-FINANCE-PATH, VIS-FIRM-FINANCE-SEVERITY and VIS-EVIDENCE-FRESHNESS. For each contract you cannot complete, name the missing input.

B13. Literature, sources and methods library on /data/. Turn the source list into a working research library, using governed fields only, with progressive enhancement (the full list stays readable without JavaScript):
a. Filters by document type, publisher, year, domain or question, language and whether a public original exists; sorting by date; a text filter within the list; the filter state in the URL so it can be shared.
b. For every source, which Evidence Records, Readings and visuals use it (backlinks), and a copyable citation from the B9 template.
c. A clear shelf for the "Measurement methods and international references" category, so a reader can see which international frameworks and survey standards the resource draws on and where each is used. Any descriptive text it needs follows the designation rules and is sourced from the framework's own publication.
d. Check every public original link (151 locators) with your web tools. For a broken one, find the publisher's current address for the same document and verify it is the same document; otherwise add an archived copy only from web.archive.org and say so. Changes are Master-first. Record every check in audit/release_candidate/LINK_CHECK.md.

B14. Data and hosting readiness (no deployment, no public_origin).
a. Datasets, prepared and switched off. Build an export step that produces CSV and JSON for the Evidence Records, public claims, sources, visual rows, chronology and Measurement Agenda, with a bilingual codebook (field, meaning, unit, allowed values) and provenance on every row (record ID, source ID, locator, Master SHA-256). Generate them outside dist/ (for example build/exports/) and attach them to CI as an artefact, with a gate that proves every exported value matches the projections. Publishing them is one switch that stays off until the owner's licence decision; document that switch in the runbook.
b. Host configuration for the common static hosts (a _headers file read by Cloudflare Pages and Netlify, and a note for GitHub Pages, which cannot set headers) with the security headers of REL-01: a Content-Security-Policy that matches what the pages actually load, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, frame-ancestors, HSTS for when HTTPS is live, and sensible cache rules (long for hashed or static assets, short for HTML). Serve dist/ locally with those headers and load every page in a headless browser: no policy violation.
c. A deployment workflow, prepared but inactive: choose the static host you recommend for this product (cost, Arabic and RTL neutrality, custom headers, custom domain, reliability from Yemen and the region) and say why in the runbook, with one alternative; write a GitHub Actions workflow that builds, runs the gates and deploys dist/ to it only when the owner has set the repository variable or secret the runbook names. Until then it does nothing.
d. Performance budget. Measure first-load weight and time for each page family on a throttled mobile profile, in both languages. Remove the largest costs without changing the design or the canonical font and logo files (logo derivatives from Part A, preloading, font-display, compression and cache rules in the host configuration). Record before and after in docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json.
e. The currentness re-run as one command, if it is not already a script, against the watch points in audit/FINAL_CURRENTNESS_CUTOFF.md.
f. docs/RELEASE_RUNBOOK.md: the exact steps from "the owner has a hosting account and a domain" to "live": set public_origin; rebuild; confirm canonical, hreflang, sitemap, robots and og:url are absolute; activate the deployment workflow; deploy; check headers and every page on the live host; run the currentness re-run at the release date; run every gate; optionally enable cookieless, first-party aggregate usage counts with no personal data, disclosed on /privacy/ before activation as that page requires; record the owner's release acceptance; the owner pushes the release tag. Each step names who does it. Every step except the account, the domain, the licence decision, the tag and the signature is a Claude Code step.

B15. Independent product challenge, then improvement.
a. Convene a panel of subagents that wrote none of this pull request, working from the built site in both languages at 390 px and at desktop width: a user-experience and information-architecture lead; an interface lead (the accepted D7 design is the baseline); an accessibility and mobile lead; an evidence and measurement lead; an Arabic-first reader; and ten users, each with their own goals and limits: a Yemeni citizen reading Arabic on a phone over a weak connection; a Central Bank of Yemen supervisor; a bank or microfinance institution's strategy officer; a payment or remittance provider; a journalist on deadline; an academic researcher; a World Bank, IMF or development-finance economist; a humanitarian cash-programme manager; a donor programme officer deciding what to fund; and a government policymaker. The red team attacks every finding.
b. Each user performs real tasks and records where they fail or hesitate. At minimum: find the account-ownership gap between women and men and say what it does not show; find the 2024 CBY decision on unlicensed e-wallets; judge whether rising POS numbers show more use; cite one figure correctly in a report; compare two records and say whether they can be compared; find what should be measured next on remittances; find the sources behind one Reading and open one original; find who publishes this resource and how it is funded; report an error in a record; search in Arabic for a common term with and without hamza and taa marbuta; understand, in plain Arabic, what share of adults has an account and what that does and does not mean; find how many providers of one type are on the official list and what the list does not show; find what the evidence says about whether accounts opened for transfers stay in use; trace a remittance figure and its revision to the original sources; name the three largest unknowns and what measuring each would make possible.
c. Write audit/release_candidate/PRODUCT_CHALLENGE.md: every finding ranked by value to the user, with evidence (page, task, what happened), the proposed change, cost, risk and the red team's verdict.
d. Implement every improvement that fixes an observed task failure or makes a named user's task measurably faster or clearer, uses governed data and components the site already has, respects the owner rules, and is not blocked by the red team. New tool capabilities and new angles on existing evidence are welcome — for example Arabic search normalisation (alef, hamza, taa marbuta, ya), better search ranking, the system chronology shown where it explains a page, clearer empty states and 404, links to a page section. The red team may block only for a stated reason of truth, safety, accessibility or governance, never for effort. Build in value order, one revertible commit per improvement, with a test or gate where one fits; stop when what remains is low value or carries real risk.
e. Game-changer test. Each user lens names the one capability that would make this resource indispensable to them, so that they would return to it, cite it and recommend it. Judge each against the evidence the repository actually holds: build it now if it passes the test in d; otherwise put it in the roadmap with exactly what it needs. Record the answers in PRODUCT_CHALLENGE.md.
f. Write docs/ROADMAP_V1_1.md, ranked by user value, with what each item needs (data, a decision, design or code). Put first: international context from same-source aggregates (for example Global Findex regional and income-group values on the same definition), with the caveats it needs (Yemen's sample coverage, wave and fieldwork dates); then public downloads after the licence decision; then everything else the challenge found.

B16. Disposition of every open item. Walk design/ESCALATIONS.md and FINAL_OPEN_ITEMS_REGISTER.md. For every item still open, append a dated disposition: DONE (commit), RELEASE (what remains and who), POST-LAUNCH (reason) or REJECTED (reason, citing the closed decisions). Expected post-launch unless done above: public downloads and exports (licence), the 26 governed relationship statements (21 lack references), a per-instrument stage table on /reforms/, the contracts B12 could not complete (each with its missing input), record-class labels, the DEBT-008 pacing marker, the CLM-039 comparison sentence, table rows for the 13 table-only records. Expected at release: hosting and public origin, live security headers, the currentness re-run at the release date, the owner's release acceptance. Produce audit/release_candidate/OPEN_ITEMS_DISPOSITION.md with counts per class. Zero items may remain without a disposition.

B17. Everything green.
a. Every gate in CONTRIBUTING.md §5, both browser suites, the design checks (design/reference/check_acceptance.py), the new export gate, and the full python3 scripts/tests/test_gate_negative_controls.py. scripts/tests/test_cutover_parity.py is pinned to frozen projections; follow its docstring after Master changes, and treat scripts/tests/test_content_parity.py as the standing content gate. Never weaken a gate; if a gate's expectation must change because of an item above, change it through its documented procedure and show why.
b. A full-site sweep of the built output, every page in both languages: no unresolved token or placeholder; no broken internal link or anchor; no empty heading or section; no console error; no horizontal overflow at 320 px; every image with alt text; every external link with its new-tab cue; Arabic pages right-to-left with numbers and dates isolated correctly. Fix every failure.
c. Commit ritual, push, and wait until all three CI jobs are green on the final head. Then mark the PR ready for review.

FINAL REPORT (PR description and your last message)
- A table of every item in Part A and Part B: DONE / PARTLY (what remains and why) / NOT POSSIBLE (why).
- The editorial ledgers (counts), the link check (counts by outcome), the visuals completed in B12, the product-challenge findings, improvements built and red-team blocks with reasons.
- Datasets and hosting: what is prepared, how each switch is turned on, and the performance before and after.
- The disposition counts (DONE, RELEASE, POST-LAUNCH, REJECTED) and "undecided: 0".
- Master SHA-256 before and after, transaction IDs, every gate result, negative controls n/n, CI status of the three jobs on the final head.
- What the owner must still do: only merge this pull request, provide the hosting account and domain, decide the content licence, push the release tag and sign the release. Anything else is a gap you must close or explain.
The last line, exactly: RELEASE CANDIDATE COMPLETE — ALL ITEMS DISPOSITIONED — FOR INDEPENDENT REVIEW. NOT A PUBLIC RELEASE.
