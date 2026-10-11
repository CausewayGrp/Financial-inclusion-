STAGE A FINAL INSTRUCTION v5 (11 October 2026, corrected at 15:40 after the owner's decisions and a second
independent review)

This is the only instruction to act on. It replaces the "Stage A Closure Addendum" and addenda v1, v2, v3 and v4.
Neither v3 nor v4 was ever delivered to you; where this file names them it is explaining its own lineage, and
there is nothing for you to look for. v4 was superseded the same day by an independent review and by verification that
changed two of its own instructions: see "WHAT VERIFICATION CHANGED IN THIS INSTRUCTION" in §0. Where this file
differs from anything you were told earlier, this file wins. Stage B
is NOT authorised. When the owner sends this message, that approves exactly this scope and the owner decisions in §1.
Anything outside it needs the owner's approval first.

From the programme steward's independent counsel. Checked on 11 October 2026 against the live repository:
- main 2a994eb6686a9bc5032534bb5550eaafe3a68d10 (PR #42, merged 09:05:59Z);
- Master SHA-256 7627f97cd96ca8719fe2aa778e9d69d80ebca4ca27e7292e8102159f1702f092, which README.md and
  authority/YFI_CURRENT_PROJECT_CONTEXT.json both carry;
- open pull requests: none;
- CI on that commit: nine checks green (Governance gates, Browser acceptance, Gate negative controls and its six
  shards); the deploy and manual-verification workflows skipped, as designed;
- the original documents;
- OpenAI's packages (Session 2, Session 3 and V6).
Page numbers are PDF pages unless marked "printed".

====================================================================================================================
START HERE. DO THIS BEFORE READING THE REST
====================================================================================================================
Your role in this session: Team Lead and the only writer. This session closes the **content** of Stage A. It is not
Stage B, and it does not declare Stage A closed; that is the owner's decision on your report.

1. Open the session exactly as AGENTS.md requires, and read the output before you continue:

   git fetch origin && git status
   python3 scripts/checksums.py --check && python3 scripts/validate.py

2. Verify the entry state against what this instruction was written on. **If anything differs, stop.** Do not
   reconcile it silently, do not restore anything, and do not start a transaction:
   - main = 2a994eb6686a9bc5032534bb5550eaafe3a68d10
   - Master SHA-256 = 7627f97cd96ca8719fe2aa778e9d69d80ebca4ca27e7292e8102159f1702f092
   - open pull requests = none
   - the nine CI checks green on that commit
   Report the difference, say what you think caused it, and wait. A changed entry state means someone or something
   else has written to the repository, and every item below was adjudicated against the state above.

3. Read these, in this order, and nothing else first:
   - README.md
   - OPENAI_REENTRY_CHECKPOINT.md
   - authority/CORE_CONSTITUTION.md
   - CONTRIBUTING.md (the change protocol, §4 and §5)
   - audit/close_out/BRIEF.md
   - audit/close_out/PROGRESS.md, the tail from "Stage A addendum" onward
   - audit/OWNER_DECISIONS_2026-10-10.md
   Do not begin by reading historical audit documents. Read history only when an item below names an uncertainty
   that needs it.

4. Then read this file in order: §0 what is already on main and must not be redone; §1 the three owner decisions to
   append as D16, D17 and D18; §2 the rules and the model routing; §3 the four pull requests; then the items.

5. Scope. Nothing outside this file is authorised. If you find something that needs doing and is not here, record it
   in the W3f register and name it in the report. Do not do it, and do not open a second instruction's worth of work.
   You may challenge any item with evidence: put the challenge in the report and carry on. Your three challenges in
   the last run were all correct and all accepted, so challenge freely.

6. What finishing looks like, and the only way this session ends well:
   - PR-3, PR-4, PR-5 and PR-6 merged, each at 9/9 CI with its negative controls n/n;
   - the public-literal closure re-stated after the last merge, over the new total;
   - CWR-012 resolved in one direction: repaired and kept, or withdrawn with its content resited — never left live
     and unrepaired;
   - every item in one of the four states, **each with the test that confirmed it** (§10);
   - the Stage A addendum report returned, then **STOP**.
   Do not declare Stage A closed. Do not declare DESIGN HANDOFF READY or PUBLIC RELEASE READY. Do not touch the
   Stage B charter, the amendments file, the design layer or `handoff/`. Nine green checks are a structural result,
   not an acceptance and not a release.

====================================================================================================================
0. WHAT IS DONE ON MAIN (DO NOT REDO), AND WHAT THIS MESSAGE CHANGES
====================================================================================================================
Merged, reviewed and accepted: #39 (public-literal audit v3), #40 CLOSE-6A at 2b6b2b2c, #41 CLOSE-6B at d15dece0,
#42 CLOSE-6C at 2a994eb6. Reopen none of it. Where v3 asked for something that is now on main, that text is
withdrawn. Verified done:
- the Measurement Agenda bindings; FAS-YEM-2015, MICS-YEM-2022-23 and YMPS-YEM-2022-R1 with their D9 routes;
  composite members listed or framing stated; literal closure 0 unresolved / 0 open over 18,223 public numbers;
  CR-21; CR-22; CLM-039 recorded as an inconsistency; the e-money attribution; the CWR-010 limit finding;
- the two Sana'a Center duplicates retired with the authors corrected to Sana'a Center Economic Unit; six sources
  withheld; the C12, University of Aden, Quarterly Bulletin, AMB and CCY cards completed; ten regulatory cards
  projected with why-it-matters and boundary text; the /data/ count derived from the rendered cards with its gate and
  negative control; the chronology at 31 events (e-KYC 2023 to MA-007, Decision 19/2024 paired neutrally with
  CBY-Sana'a Circular No. 12, Decision 7/2026, news/832 as a first meeting); SOURCE_UTILISATION_2026-10-11.csv over
  200 source records; search alias 001; the Arabic bidi fix for reference numbers;
- X-REG-LINK-C12 closed; the 2015 annual report and CURR-2024 withheld as unverifiable; KfW 47229 left undated.
Your three challenges are accepted as correct: MA-005 prints 1.5, not the 1.4756 I quoted; Brief 40 is not
corroboration; "until 2023" is right for e-money and is completed by CBY-Aden's instructions of 14 September 2022.

CWR-012. v2 and v3 both told you to keep it retired. On the published text, I withdraw that instruction. The
retirement rested on three grounds: an inference from two marginal shares that cannot identify a channel; an Arabic
text that had had no native economic review; and the Cash Consortium findings not being held as records. Your run
removed all three — CCY-ISP-2024 and CCY-SAM-2024 created from both studies read in full, the red-team HOLD on
"informal", on "mainly" and on "the economy as a whole", and the Arabic pass with no numeral drift over 37 pairs. The
published thesis states the comparison as a hypothesis, keeps adults distinct from households, says that no channel
value for that wave is held, and names the rival explanations. That is the discipline the retirement was protecting,
so the Reading stands. Two consequences, both binding:
- the single new-Reading slot under D9 is now spent. CWR-013 is RESERVED, not published (D17, amended in §1);
- one editorial item is open, and it is mine, not a red-team leftover: the title and the question say "households" /
  «الأسر» while the Findex evidence counts adults, and only the Cash Consortium surveys speak to households. In PR-3,
  decide between (i) retitling to people / «الناس», and (ii) keeping the title and adding one clause to the question
  that attributes the household evidence to the Cash Consortium surveys alone. Either is defensible. Record which,
  and why, and make the Arabic follow the English decision in the same transaction.

WHAT VERIFICATION CHANGED IN THIS INSTRUCTION. Two things v4 told you to do were wrong, and I found it by checking
the publisher rather than by re-reading my own draft. Both are corrected in §4, 6B-1.
- v4 had you publish "the 19 low-income economies" as the World Bank's basis. The World Bank publishes no economy
  count for that aggregate and that wave. The count is right and reproducible; the attribution would have been false.
  v4 would have introduced an error the site does not currently have.
- v4 had you repeat that Yemen's survey "did not ask" the mobile-money questions. The World Bank nowhere states that.
  The site's own CLM-001 states it correctly, with its basis attached; the flat restatements elsewhere do not. So the
  fix is not to the record, it is to the restatements. New item 6B-1(e).
A third correction came from the same check and is in the site's favour: 35.2% is the publisher's own published
aggregate, so the site can stop reproducing it from member economies and cite the publisher instead. That removes a
derivation and a count from a public surface.

THE DELETION TEST ON BOTH READINGS, and a correction to my own first answer. I ran the test, recorded a basis for
keeping CWR-012, then had a red team attack that basis. The red team was right and I was wrong, so the basis below is
the corrected one. I am recording the error rather than quietly replacing it, because the same discipline applies to
me as to the Master.
What I claimed, and what is actually true. I listed eight things a reader would lose if CWR-012 were withdrawn, "with
nothing else carrying it". Six of the eight are carried elsewhere on main, and I verified each one myself after the
challenge:
- the 2026 roster read as roster classes, not operating providers: /providers/ sections 1 and 4, /access/ section 3,
  CLM-009 and VIS-PROVIDER-TIME. /access/ section 3 states "Listing or licensing is not operation" outright;
- the 876-to-3,244 branch pair with both attributions: /providers/ section 10 carries it in full, and adds that
  branches and entities are different units. My claim that it "exists nowhere else" was simply false. Only the words
  "citing no source" and "World Bank estimates" are unique to the Reading;
- the 2014 channel shares read as shares of recipients: /people/ section 7, /remittances/ section 6, CLM-030 and
  VIS-DOMESTIC-REMITTANCE-PATH-2014, and /people/ section 7 states the base change more sharply than the Reading;
- the 26 June 2024 unified-network decision: VIS-PAYMENT-RAILS, which puts it on a stage ladder as a rule;
- the Cash Consortium material as a rival channel: CWR-010 section 6 and both evidence records;
- "a channel value that is missing is unknown, not zero": /access/ section 4.
Two things are genuinely exclusive: the definitional triangulation ("in the survey it is money moved within Yemen, in
CBY-Aden's balance of payments a cross-border dollar flow, in the price data a formal product for sending money in.
The three share a word, not a measure"), and the hypothesis framing with its stated falsification condition in
section 9. And the 31.9/11.9 juxtaposition is already on CLM-026 and VIS-DEMAND-VINTAGE-LADDER, so the Reading is not
what stops a reader making the comparison unaided; it is where the comparison is disciplined.
I also counted 28 source bindings and a controlled-contract edit as reasons to keep. That was lock-in dressed as
truth value, and the red team was right to say I applied one standard to CWR-012 and the opposite one to CWR-013.

THE CORRECTED RULING. CWR-012 stays, on narrower grounds and on one condition.
The grounds: the product's architecture gives a Reading a job no page section performs. A page section states facts
with their boundaries; a Reading takes a question a reader will actually ask, gives the strongest defensible answer,
sets out the rival explanations, says where the evidence stops and states what would falsify it. Sections 5 and 9 do
that here and exist nowhere else, and section 9's falsification condition is the strongest single thing in the
Reading. That is worth a route. The facts being available on six other pages is not an argument against the
adjudication; it is what the adjudication is built from.
The condition, as the owner decided it: **one disciplined repair attempt**, and correcting the overlap bound is not
enough on its own. The thesis itself must pass the inference test and the uniqueness test. If after the repair the
Reading is still only a hypothesis about channels the evidence does not measure, then its form as a Reading is
withdrawn: what deserves to be kept goes into the Evidence Records and the Measurement Agenda, and the links, the
search records, the closure entry and the indexes are all handled in the same transaction. One attempt, then a
decision either way. No second attempt, and no leaving it live unrepaired. The five defects are in §4 as item 6B-5.

Two repository findings of my ownTwo repository findings of my own, both verified on main, both for PR-5:
1. OPENAI_REENTRY_CHECKPOINT.md states "476 search records". site-src/content/content/search_index.json holds 514.
   AGENTS.md requires README.md, the checkpoint and the Context to agree. Correct the count, and the date of the
   paragraph that carries it.
2. README.md's "Current state" table still reads "Content | Complete on main, 10 October 2026" and records neither
   STAGE A COMPLETE at 53dccc4d nor the Stage A addendum of 11 October. Its Master and Page Specs hashes are current,
   so this is a programme-state gap, not an authority gap. Bring the state up to date and claim nothing new: not
   DESIGN HANDOFF READY, not PUBLIC RELEASE READY.

Withdrawn, as in v3: "KfW 47229: EUR 4.5 million matches phase I". I never verified it. Make no phase claim beyond
your own undated finding.
====================================================================================================================
1. OWNER DECISIONS THIS MESSAGE RECORDS (append them to audit/OWNER_DECISIONS_2026-10-10.md as D16–D18)
====================================================================================================================
D16. CauseWay-derived aggregates from public-use microdata.
- Weighted aggregate shares computed by CauseWay from the World Bank Global Findex 2021 Yemen public-use file may be
  published as a distinct evidence class, CAUSEWAY_DERIVED_AGGREGATE.
- The Microdata Library terms allow the user to report aggregated information with citation. They forbid
  redistribution and any attempt to identify respondents.
- Conditions:
  - Report point estimates and unweighted bases only. Report no interval: the file has no PSU or stratum, which is
    consistent with CR-02.
  - Suppress any share whose base is under 100 or whose numerator is under 10.
  - Label every figure "computed by CauseWay from World Bank microdata; not a World Bank published statistic", and
    cite DOI 10.48529/10py-nv58.
  - The respondent file never enters the repository, CI, Claude Code or any public surface. Only the owner-generated
    aggregate JSON and the script that produced it are committed.
  - Only version 4 of the script, dated 11 October 2026, may be run. Versions 1 to 3 had nine defects between them,
    each found in review and each now fixed and covered by a synthetic-data regression that must pass before a real
    run: a withheld share printed the exact numerator it was withholding; a missing answer was counted as "no", so a
    respondent who did not answer the second channel item fell into "neither cash nor a money transfer operator"; the
    conditional shares were based on the whole filter group rather than on the non-missing answers to their own item;
    the anchors were displayed but not enforced; the channel cells are additively linked, so withholding one while
    publishing its complements disclosed it exactly (both = cash + MTO - 1 + neither); the money-transfer-operator
    shares used the cash item's base rather than their own; the QA block published exact small counts, among them the
    count of recipients reporting receipt into an account while holding no financial-institution account, which is the
    most identifying number in the output; a failed run still printed a complete-looking aggregate before exiting; and
    the fieldwork end date followed one publisher surface without recording that the other differs.
  - Disclosure control is a condition of D16, not a detail of the script. Before any figure is published, the set
    must be checked so that a withheld cell cannot be recovered from the cells that are published, from the bases, or
    from the totals. A linked set is withheld as a whole. Every count in the output, in the results and in the QA
    block alike, is banded below the threshold rather than printed. The run exits non-zero and emits no aggregate at
    all unless it reproduces the publisher's own unrounded values - 11.9033656433415, 31.9313981068809,
    17.6714332248251 and 37.7705325180586 - within 0.1 percentage points. Commit the script with its regressions and
    record, in the report, the result of each: disclosure control, the denominators, the weights and the anchors.
    Nothing is published on the strength of "the tests passed".
  - Record the rule in 28_METHODS_RIGHTS.
- This replaces the earlier blanket "no figure computed from microdata". The ban on the World Bank Microdata API key
  stands.
D17 (amended 11 October 2026, twice). A Reading is added or kept on whether it is unique and useful, never on how
     many Readings exist. The count is not the test and must not be cited as one.
     - CWR-013 "Programmes count guarantees and grants. Can firms borrow?" is not added now, because it fails that
       test: /firms/ sections 7 to 9, MA-004 and CWR-008 already carry its argument, and its proposed visual would
       restate a ladder /firms/ section 9 already carries in prose. Its two genuinely new elements, the IFAD
       evaluation and the stage-labelling of each programme figure, are published inside those existing objects.
     - CWR-012 keeps its route only if the repaired Reading passes the same test. Any later Reading is judged the
       same way, on merit, with the owner's word.
D18. The plain-language pass on page leads is done in Stage B, through Master-first copy transactions, together with
     the design and the six-persona test. It is not a new route or module.

====================================================================================================================
2. RULES
====================================================================================================================
1. Change the Master first, through `audit/close_out/close_6*.py` and `run_stage.py`.
   - English and Arabic change in the same transaction.
   - Audit records are append-only.
   - A failed run rolls back. A merged change is undone only by a revert PR. Never force-push.
2. Each transaction has one decision owner (you, as Team Lead) and at most two challenger lenses: the domain lens named
   on the transaction, and the Arabic-editor lens.
3. Every new number needs:
   - a bound, source-closed record with a value state;
   - a public locator;
   - the page quoted in the verification field;
   - identical values in English and Arabic.
   Recompute every value from the original. If the original differs from this message, the original wins: record the
   difference.
4. New routes are allowed only as D9 detail routes for the Evidence Records named here. No new Reading route: the one
   slot D9 allows is spent on CWR-012, already published. Add no page family, hub, tool or module.
5. Cite facts and link to publishers. Never host or reproduce third-party PDFs, charts or tables.
6. Never use, request or store a World Bank Microdata API key. Never read the respondent file (D16).
7. Do not touch the Stage B charter or the design layer. Stage B is a separate, later session.
8. You may challenge any item with evidence. Put the challenge in the report; do not stall on it.
9. Transaction names continue the merged series. CLOSE-6A, CLOSE-6B and CLOSE-6C are used on main and are never
   reused: this run is CLOSE-6D, CLOSE-6E and CLOSE-6F.

Model routing for this run:
- **You, Team Lead (top model):** Master transactions, final wording, EN/AR acceptance, merges.
- **Arabic-editor lens (top model):** quality-critical.
- **Read-only verification agents (mid-tier model):** re-reading originals and checking page numbers.
- **Mechanical agents (small model):** string scans and dist assertions.
No agent writes to the repository except you. The negative controls run in the harness, not through agents.

====================================================================================================================
====================================================================================================================
3. SEQUENCE
====================================================================================================================
There is no PR-2: #40 is merged.
PR-3  CLOSE-6D: the truth corrections (§4), including the CWR-012 repair (6B-5), which ships in the same
      transaction as 6B-1(c) and never in a different one. If the repaired Reading does not pass both lenses, it is
      withdrawn in this same PR and its two exclusive paragraphs move to /remittances/ and CLM-030.
PR-4  CLOSE-6E: evidence strengthening (§5). The Findex record only if the owner's aggregate file has arrived.
PR-5  CLOSE-6F: sources, the regulation projection, the chronology, Master hygiene, the registers and the two
      repository findings (§7).
PR-6  Gate CO-G07, the W3f entries for the RESERVED items including CWR-013, and the report (§8, §9, §10).
Then STOP.
====================================================================================================================
4. CLOSE-6D — TRUTH CORRECTIONS (each fixes a public statement that is wrong, contradicted or under-caveated)
====================================================================================================================
--- 6B-1 People and Findex · lens: survey statistician + Arabic editor ---------------------------------------------
(a) The low-income comparator is like-for-unlike, and the site currently reproduces what the publisher itself
    publishes. Both halves were verified on the publisher's interface on 11 October 2026; v4 got this wrong in two
    ways and is corrected here.
    Where: CLM-001 (method_en/method_ar and limitations); the /people/ sections that print 35.2%; the
    25_FINDEX_BASELINE caveat "same wave and indicator".
    What the publisher publishes, Global Findex database (World Bank API source 28), aggregate "Low income" (LIC),
    year 2021, retrieved 11 October 2026, lastupdated 2025-10-06:
      - account.t.d, "Account (% age 15+)" = 35.1821646573129;
      - fiaccount.t.d, "Bank or similar financial institution account (% age 15+)" = 24.4577497822049;
      - mobileaccount.t.d, "Mobile money account (% age 15+)" = 18.3073126606225.
    Store all three as an API fixture with the indicator names as the publisher gives them, the retrieval date and the
    locator https://api.worldbank.org/v2/country/LIC/indicator/<code>?date=2021&format=json&source=28 .
    Four things follow, and each is a correction:
    - 35.2% is the publisher's own aggregate. CLM-001's method currently says this resource "reproduced it as the
      average of the published values of the 19 low-income economies surveyed in the wave, weighted by their adult
      populations". That reproduction is accurate — it was checked against the publisher's figure and matches — but it
      is unnecessary, and it puts a CauseWay derivation and an economy count on a public surface where the publisher's
      own number will do. Cite the publisher's aggregate directly and delete the reproduction sentence and the count
      from the public method text. Keep the derivation in the Master as the check that it is, with its result.
    - Do not print "19 low-income economies" anywhere, and do not attribute a count to the World Bank. The publisher
      states no economy count for this aggregate and this wave: not in the 2021-22 survey methodology, not in the
      report, not in the DataBank aggregate definition. The count is right and reproducible from the publisher's
      country-level file; it is still not a published figure, so it is not ours to print as one.
    - Add fiaccount.t.d as the like-for-like comparator. It is the publisher's own aggregate, needs no derivation, and
      is the only one of the three that compares with Yemen's 11.9% on the same definition.
    - Do not publish 18.31 at all, and record why in the fixture: in the publisher's own aggregate Yemen's missing
      mobile-money value enters the numerator as a zero while Yemen's adults stay in the denominator, so it is not a
      like-for-like comparator for Yemen and it is a missing-is-not-zero problem inside someone else's arithmetic.
      That finding is CauseWay's reconstruction of the publisher's method, not a published statement, so it stays in
      the Master and on no public page.
    Precision that must survive: the publisher files the low-income aggregate at year 2021 and Yemen's own
    observation at year 2022, within one survey wave; `date=2021` returns no value for Yemen. Say "the same survey
    wave", never "the same year". The aggregate's grouping basis is the World Bank income classification, and the
    database's own metadata names the FY24 classification (2022 Atlas GNI per capita of $1,135 or less); the printed
    2022 report names the 2020 classification instead. These figures come from the database, so cite the database's
    FY24 basis, and correct CLM-001's limitations text where it instead says the classification "in the Global Findex
    Database 2025".
    This is new evidence. It does not reopen CR-14: CR-14 checked the value, not the definition.
    EN: "For context only, and not as a benchmark, a target or a ranking: the World Bank's own aggregate for
    low-income economies in the same survey wave puts adults with an account at a financial institution at 24.5%. Its
    headline account figure for those economies, 35.2%, also counts mobile-money accounts, and the World Bank
    publishes no mobile-money figure for Yemen, so 35.2% does not compare with Yemen's 11.9% on the same definition.
    The aggregate averages economies in very different conditions, includes Yemen itself, and groups economies by the
    World Bank income classification."
    AR: «للسياق فقط، وليس معيارًا أو هدفًا أو ترتيبًا: يضع تجميع البنك الدولي نفسه للاقتصادات منخفضة الدخل، ضمن موجة
    المسح نفسها، نسبة البالغين الذين لديهم حساب لدى مؤسسة مالية عند 24.5%. أما رقمه الرئيسي لملكية الحساب في هذه
    الاقتصادات، 35.2%، فيشمل أيضًا حسابات الأموال عبر الهاتف المحمول، ولا ينشر البنك الدولي أي رقم لليمن عن هذه
    الحسابات؛ فلا تُقارَن نسبة 35.2% بنسبة اليمن البالغة 11.9% على التعريف نفسه. ويتوسط التجميع اقتصادات متباينة
    الأحوال تمامًا، ويشمل اليمن نفسه، ويصنف الاقتصادات وفق تصنيف الدخل المعتمد في البنك الدولي.»
    Add the fiaccount.t.d row, and both year labels, to 25_FINDEX_BASELINE.

(e) The mobile-money wording, everywhere it travels. This is a finding of this review, not of the earlier rounds.
    The World Bank nowhere states that the mobile-money module was not asked in Yemen. Searched on 11 October 2026:
    the report, the 2021-22 survey methodology (Yemen's Table A.1 row gives fieldwork, sample, exclusions and the PSU
    replacement, and says nothing about mobile money), and the methodology landing page. The questionnaire attached to
    Yemen's own catalogue record is the generic 2021 instrument and does contain the mobile-money section, so it
    cannot be cited as evidence of an omission either.
    CLM-001's method field states the claim correctly, because the basis travels with it: no valid answer to any of
    the mobile-money items in the public data, no mobile-money series value for Yemen, and the financial-institution
    series equal to the account series. Keep that. What must change is every flat restatement elsewhere, which asserts
    a cause as fact without its basis. At least these: /people/ (03_PAGE_SECTIONS, the "no single figure" section),
    interface_copy label, MA-001 guardrail, CWR-012 section `evidence_channels`, and each record that repeats it —
    scan for "not asked", "were not asked", "did not ask" and their Arabic.
    Rule: a flat "the questions were not asked" may stand only where the three observed facts stand with it.
    Everywhere else, state the observation, not the cause.
    EN, the short form for those places: "The World Bank publishes no mobile-money-account figure for Yemen, and its
    figure for an account at a financial institution is the same as its account figure, so this value reflects
    accounts at financial institutions."
    AR: «لا ينشر البنك الدولي أي رقم لليمن عن حسابات الأموال عبر الهاتف المحمول، ورقمه للحساب لدى مؤسسة مالية
    مساوٍ لرقم ملكية الحساب؛ فهذه القيمة تعبر عن الحسابات لدى المؤسسات المالية.»
    Do not write that the module was withheld, skipped or unavailable: none of that is published either.

(b) The 2014 borrowing vintage (CLM-028, VIS-BORROWING-SOURCES-2014).
    - 0.4% comes from the Little Data Book 2015 (printed p.160). The current database gives 0.6% for fin22a 2014
      (0.603) and 1.8% for 2022.
    - Keep 0.4% where the profile is reproduced as printed, and label it: "as printed in the Little Data Book 2015; the
      World Bank's current database gives 0.6% for the same 2014 measure".
    - Any sentence that compares 2014 with 2022 uses 0.6%.
    - Add the fin22a 2014 row to 25_FINDEX_BASELINE.

(c) VIS-FINDEX-FLOW-CHANNELS, the reason text. This is corrected using the World Bank's public DDI, not the respondent
    file.
    Before writing anything here: read the DDI's own definition and derivation of fin29 and fin29_1, and check
    whether the published series is defined over a different universe or derived differently from the variable whose
    documentation shows positive answers. A difference in definition or derivation could produce a published 0
    without any error by the publisher. **Positive answers in the variable documentation do not, on their own,
    establish that the World Bank miscomputed a published indicator**, and this resource does not say that it did.
    Report the two publisher statements as found, state that they cannot both describe the same quantity, say that
    the printed value is not used here, and offer no explanation that is not established. If the definitions do
    explain the difference, say so and drop the conflict.
    - The database's fin29 ("received domestic remittances into an account") prints 0 for Yemen, with no recipient or
      group value.
    - The World Bank's public variable page for fin29_1 (catalog 5862, variable V67) shows the question was asked of 393
      recipients, and 39 answered yes (unweighted).
    EN, if the definitions do not explain the difference: "For domestic remittances the World Bank's database prints
    0 for receipt into an account, with no recipient or group value. Its published variable documentation for the
    same wave records that the question was asked and that some recipients answered yes, as unweighted response
    counts. The two statements cannot both describe the same quantity, so the printed value is not used here and no
    reason for the difference is offered. The database publishes no cash or money-transfer-operator series."
    AR: «في التحويلات المحلية تطبع قاعدة بيانات البنك الدولي صفرًا لاستلام الأموال في حساب، من دون قيمة للمستلمين أو
    للفئات. ويُظهر توثيق المتغيرات الذي ينشره البنك أن السؤال طُرح وأن بعض المستلمين أجابوا بنعم، فالصفر المطبوع ليس صفرًا
    مقيسًا ولا يُستخدم. ولا تنشر القاعدة أي سلسلة للاستلام نقدًا أو عبر شركات تحويل الأموال.»
    If the D16 record exists (§5, 6C-6), add "See the CauseWay tabulation of channels" with its link.

(d) /finance/ (03_PAGE_SECTIONS row 117): the stale OECD "not yet verified" sentence.
    EN: "The OECD's 2026 review prints figures for current accounts, savings accounts and mobile-phone access without
    naming the survey or period behind them. They are not used here, they are not 2026 measurements, and they are not
    comparable with the Global Findex."
    AR: «تورد مراجعة منظمة التعاون الاقتصادي والتنمية لعام 2026 أرقامًا عن الحسابات الجارية وحسابات الادخار والنفاذ إلى
    الهاتف المحمول من دون تسمية المسح أو الفترة التي تستند إليها. ولا تُستخدم هنا، وليست قياسات لعام 2026، ولا تُقارَن
    بقاعدة Global Findex.»
    Print none of the three numbers.

--- 6B-2 Firms and programmes · lens: MSME finance specialist + Arabic editor --------------------------------------
(a) YLG: two publishers, shown side by side. Neither overwrites the other; nothing is subtracted, averaged or merged.
    What the documents show:
    - OECD 2026, printed p.32:
      - 5,731 transactions "since 2017";
      - USD 42.8m of guarantees and USD 63.6m of loan principal;
      - 72.7% to men-owned businesses, 60% rural, 55% young-owned.
    - YLGP Annual Report 2022, Annex I (p.29): yearly guarantees issued were 301, 691, 1,270, 1,327 and 3,387, which
      sum to 6,976. Every Annex I split also totals 6,976.
    - The difference is a comparability problem whose cause is not established. Possible causes are the cutoff,
      revisions, eligibility, repeat guarantees, category definitions, and the terms used ("women-led" versus
      "men-owned").
    - Ledger note, not public text: the cutoff alone cannot explain the gender split, because women's total to the end
      of 2022 is 1,525, which is under 27.3% of 5,731.
    New source SRC-YLG-AR-2022 (next vacant 15_SOURCE_LIBRARY row; check first for a duplicate publisher or URL):
    - publisher Yemen Loan Guarantee Program;
    - type PRIMARY_PROGRAMME_REPORT;
    - locator https://www.ylg-yemen.org/_files/ugd/82b85d_8562d5fe47644538ab12044bb8938bc6.pdf;
    - fiscal year 2022;
    - pages 4, 8, 14–17, 29–30;
    - rights NOT_ASSESSED: facts cited, nothing reproduced.
    Data rows in 20_FIRM_FINANCE (row-4 schema, native units):
    - public:
      - issued 2022: 3,387;
      - guarantee amount: YER 6,397,627.81 thousand;
      - covered principal: YER 9,371,245.29 thousand;
      - female-led: 693 of 3,387;
      - partner institutions: 12;
      - yearly counts 2018–2022, plus the declared sum 6,976;
    - held, not public:
      - youth 1,907 and rural 1,748 of 3,387;
      - outstanding 3,526 and about YER 4.6 billion (the as-of date is not stated);
    - not stored: PAR 8.54% (its base is not stated).
    CLM-059 (06/07), the YLG part, and /firms/ §7 (03 rows 128–129). Keep the SMEPS part.
    EN: "Two publishers report on the Yemen Loan Guarantee Program (YLG), which shares credit risk with partner banks and
    microfinance providers on loans to micro, small and medium enterprises. The programme's own Annual Report 2022 states
    that in 2022 it issued 3,387 letters of guarantee, worth YER 6.4 billion and covering loans of YER 9.4 billion, through
    12 partner institutions; women-led businesses received 693 of them (about 20%). Its yearly counts for 2018–2022 sum
    to 6,976 guarantees. Separately, the OECD (2026) reports that YLG has guaranteed 5,731 transactions since 2017, with
    USD 42.8 million of guarantees for USD 63.6 million of loan principal in nominal terms, 72.7% of them to men-owned
    businesses; it states neither a cutoff date nor an exchange rate. The two sets of figures differ in total and in
    gender split, and the published documents do not explain why, so they are shown side by side and not combined."
    AR: «يتناول مصدران برنامجَ ضمان القروض في اليمن، الذي يتقاسم مخاطر الائتمان مع البنوك ومؤسسات التمويل الأصغر الشريكة
    على قروض المنشآت متناهية الصغر والصغيرة والمتوسطة. يذكر التقرير السنوي للبرنامج لعام 2022 أنه أصدر في ذلك العام 3,387
    خطاب ضمان بقيمة 6.4 مليار ريال، تغطي قروضًا بقيمة 9.4 مليار ريال، عبر 12 مؤسسة شريكة، وأن المنشآت التي تقودها نساء
    حصلت على 693 منها (نحو 20%). وتبلغ أعداده السنوية للفترة 2018–2022 في مجموعها 6,976 ضمانًا. وفي مصدر منفصل، تذكر
    منظمة التعاون الاقتصادي والتنمية (2026) أن البرنامج ضمن منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات قدرها 42.8
    مليون دولار لأصل قروض قدره 63.6 مليون دولار بالقيمة الاسمية، 72.7% منها لمنشآت يملكها رجال، من دون أن تذكر تاريخ
    انتهاء بياناتها أو سعر الصرف المستخدم. ويختلف الرقمان في المجموع وفي التوزيع بحسب الجنس، ولا تشرح الوثائق المنشورة
    سبب ذلك، لذا يُعرضان جنبًا إلى جنب ولا يُدمجان في سلسلة واحدة.»
    does_not_establish, EN: "Both publishers count guarantees or transactions, not firms. Neither shows how many MSMEs
    could borrow, on what terms, or whether guaranteed loans would have been made anyway. Programme amounts are nominal
    rials as reported; the report does not say in which area's rial loans were made, and nothing is converted here. 2022
    is the latest year for which a programme report was verified in this review; later reports were not searched."
    Arabic to the same meaning. Do not write that 2022 is the latest year the programme has published: that would be
    a claim about the programme's whole output, and it was not checked.
    Verification field: the OECD's six sector shares sum to 104%, so they are shown neither as a breakdown nor
    renormalised; the programme's PAR has no stated base.
    Period field: "2022 (issued during the year); 2018–2022 (yearly counts); OECD: since 2017, cutoff not stated".
    Note on OECD-YEM-015, 016 and 017: "NOT_RECONCILED_WITH_SRC-YLG-AR-2022: cutoff and definitions differ; not
    combined". They stay projected.

(b) EP-SMEPS-2024-PROGRAMME: remove "jobs" from the title, in both languages.

(c) The 2018 "141-firm" survey.
    Where: /firms/, CLM-062, /readings/define-what-you-count/, /readings/finance-constraint-different-questions/.
    EN: "The appraisal document gives no title, fieldwork dates, sampling frame or size definitions for this survey."
    AR: «لا تذكر وثيقة التقييم عنوانًا لهذا المسح ولا تواريخ عمله الميداني ولا إطار المعاينة ولا تعريفات أحجام المنشآت.»

(d) MA-004.
    - Add to current_evidence: "the Yemen Loan Guarantee Program's reports count guarantees issued, not firms".
    - Add a missing-evidence dimension: "unique-firm identification across programme registers, and whether guaranteed
      loans add to lending (additionality)".
    Arabic to match. CWR-008 is unchanged.

--- 6B-3 Regulation and consumer protection · lens: CBY regulator / legal librarian + Arabic editor -----------------
(a) Deposit insurance (YSC-028, fi_relevance; check REF-REG-006 for the same claim).
    Verified on the certified copy of SRC-CBY-DIL-21-2008:
    - Art. 13(1), p.5: 0.002 of the deposits subject to the law. Art. 13(2) excludes government, interbank and
      cash-collateral deposits.
    - Art. 31, p.9: cover is full up to YER 2 million and capped above it; foreign currency only by CBY decision;
      payable on a CBY liquidation decision.
    - Art. 33, p.10: one person's accounts at the same bank count as one; joint accounts are split by share; debts to
      the bank are offset.
    Five constraints on this text, each from attacking it. (i) Do not write "caps cover at that amount". My own note
    says Art. 31 makes cover "full up to YER 2 million and capped above it", and that is ambiguous between a payout
    that stops there and partial cover above it up to some higher ceiling. Re-read Art. 31 and publish only what it
    says; understating a legal entitlement is the one direction in which this resource could cause a depositor to
    forgo a claim. (ii) Publish all three of Art. 33's rules or none: the aggregation of one person's accounts, the
    splitting of joint accounts by share, and the offset of debts to the bank. All three change the number a reader
    would expect, and publishing only the aggregation keeps one adverse rule while hiding two others - a
    microfinance borrower with a deposit at the same bank is the reader most misled. (iii) Use the tense the evidence
    supports. "Banks pay an annual contribution" is a present-tense claim about conduct that the next sentence says
    nothing establishes. Write that the law requires it. (iv) Name the authority as the law names it, and say that the
    law predates the present institutional situation and that this resource does not establish which authority would
    decide: an unqualified "the Central Bank" deciding a liquidation is the whole of the entitlement, and this product
    writes "Central Bank of Yemen - Aden (CBY-Aden)" everywhere else. (v) Date the ceiling. YER 2 million is a 2008
    figure and nothing here shows it has been revised; publish it with its year and that fact, or a reader and a
    journalist will both take it as a meaningful sum today.
    EN, subject to (i) to (v): "The law covers rial deposits in full up to YER 2 million and caps cover at that amount, counting all of one
    person's accounts at the same bank as one (Arts 31 and 33); foreign-currency deposits are covered only if the Central
    Bank decides. Cover becomes payable when the Central Bank decides to liquidate a bank. Banks pay an annual
    contribution of 0.2% of the deposits subject to the law (Art. 13). The law does not show that the scheme operates
    today: no source here reports the Institution's financial statements, fund size, contributions collected or any
    payout, and the 2025 decision does not establish that cover operates."
    AR: «يغطي القانون الودائعَ بالريال اليمني بكامل قيمتها حتى مليوني ريال، ويقف الضمان عند هذا المبلغ، وتُعدّ حسابات
    الشخص الواحد لدى البنك نفسه حسابًا واحدًا لهذا الغرض (المادتان 31 و33)؛ ولا تُضمن الودائع بالعملة الأجنبية إلا إذا
    قرّر البنك المركزي إخضاعها. ويُستحق الضمان إذا قرّر البنك المركزي تصفية البنك. وتدفع البنوك اشتراكًا سنويًا بنسبة
    اثنين في الألف من الودائع الخاضعة للقانون (المادة 13). ولا يثبت القانون أن النظام يعمل اليوم: فلا يورد أي مصدر هنا
    القوائم المالية للمؤسسة أو حجم صندوقها أو الاشتراكات المحصّلة أو أي تعويض مدفوع، ولا يثبت قرار 2025 أن الضمان يعمل
    فعليًا.»
    - The OECD's (2026) statements on the scheme stay attributed in 29_OECD_BENCHMARKS and are not published:
      - "some 70% of deposits would be covered";
      - its funds are held at CBY-Sana'a and invested in distressed bonds.
      They have no stated basis and no second source.

(b) The consumer-protection instrument, cby-ye.com/files/64e6f1e87e2a1.pdf.
    What it says:
    - p.1: "Ref: 589/CBY/2023 Date: 20/8/2023", with Board approval under Law No. 14 of 2000.
    - p.32: signed 20 August 2023.
    - 28 August 2023 is the announcement date (news/567).
    Changes:
    - SRC-CBY-FCP-INSTR-2023-001: the PDF becomes the primary locator; date 2023-08-20; reference 589/CBY/2023; keep
      news/567 as an additional URL, labelled "announcement, 28 August 2023".
    - REF-FCP-001: issued 2023-08-20; announced 2023-08-28.
    - Record the lineage: TC-H changed the Arabic date to 28 August because the instrument had not been read.
    - The complaint path.
      Where: FCP-ARCH-005 to 008, CLM-011, VIS-FCP-REDRESS-PATH, /reforms/, and every other place that prints "14 business
      days" or its Arabic.
      Verified on pp.27–28:
      - item ج: 10 working days counted from receipt of the complaint and all necessary documents, extendable by a
        further 10 with reasons;
      - item د: the provider notifies the CBY and the consumer before the deadline; any extension is no more than half
        the original period; no more than 30 working days from submission "in all cases"; time spent waiting for
        documents the provider requests is not counted;
      - item ذ: the consumer may take the complaint to CBY-Aden's consumer-protection department if there is no reply in
        time or the consumer is not satisfied, "within 14 days" of the end of the settlement period; the CBY may
        accept a later complaint for a stated reason.
      Confirm the article number from the heading.
      Four things must be true of whatever is published here, because a consumer may act on it and a time bar can
      extinguish a right. First, scope: the published sentence must say, in itself and not in another object, that
      the Instructions reach providers supervised by CBY-Aden and their agents. "A provider" unqualified tells a
      consumer under the other authority that they have a path they do not have. Second, the escalation clock must
      not be published as a deadline a reader cannot compute: if its start depends on the end of a period that is
      itself extendable and suspended while the provider waits for documents, say so in the same sentence, or publish
      the window without implying the reader can date it. Third, posture: the live CLM-011 says these limits "come
      from the brochure, not from an extracted legal text", and reading the instrument is an improvement on that - but
      the improvement is in the evidence, not a licence to tell a reader what their rights are. Write what the
      instrument requires of providers, attributed to its paragraphs; do not write what the consumer "may" do as
      though this resource had established it, and do not adjudicate which instrument binds. No legal review is
      claimed or performed here. Fourth, do not propagate by string match: at least VIS-E-MONEY-RULE-STACK and
      /reforms/ carry a separate, correctly sourced 10-business-day rule from the e-money instructions of 9 August
      2023, with no escalation window. Changing "14 business days" must not overwrite those.
      Before writing any of this: establish from the headings which article and which paragraph each deadline belongs
      to, and what each one is a deadline for. "Resolve" may be the wrong duty: the escalation trigger speaks of a
      reply, so if the obligation is to respond or to settle, do not write "resolve". Items ج and د may or may not govern the same stage, and if they do, a
      10-working-day extension and an extension of "no more than half the original period" cannot both be true of it.
      Do not compose them into one rule to make a readable sentence. If the scope of each is established, publish the
      composed sentence below. If it is not, publish each item separately, attributed to its own paragraph, and say in
      the record that the published text does not make their relationship clear. A readable sentence that resolves an
      ambiguity the instrument does not resolve is worse than two plain ones.
      EN: "The 2023 Instructions (ref. 589/CBY/2023) require a provider to resolve a complaint within 10 working days of
      receiving it with its documents, with a limited extension when it gives its reasons, and within 30 working days
      of submission in all cases (time spent waiting for documents the provider asks for is not counted). If there is
      no reply in time or the consumer is not satisfied, the consumer may take the complaint to CBY-Aden's
      consumer-protection department within 14 days of the end of that period, and the Central Bank may accept a later
      complaint for a stated reason (pp.27–28). The Instructions are the binding text; the 2024 awareness brochure
      gives the escalation window as 14 working days. These are rules, not measured performance."
      AR: «تُلزم تعليمات 2023 (المرجع 589/CBY/2023) مقدّمَ الخدمة بتسوية الشكوى خلال 10 أيام عمل من استلامها مع
      وثائقها، مع تمديد محدود إذا أبدى مبرّراته، وبما لا يتجاوز 30 يوم عمل من تاريخ تقديمها في جميع الأحوال (ولا تُحتسب
      مدة انتظار الوثائق التي يطلبها مقدّم الخدمة). وإذا لم يتلقَّ المستهلك ردًّا في الموعد أو لم يرضَ به، جاز له رفع
      الشكوى إلى إدارة حماية العملاء في البنك المركزي اليمني – عدن خلال 14 يومًا من نهاية تلك المدة، وللبنك المركزي
      قبول شكوى متأخرة لسبب مقبول (ص 27–28). والتعليمات هي النص الملزم؛ أما الكتيّب التوعوي الصادر عام 2024 فيذكر أن مهلة
      الرفع 14 يوم عمل. هذه قواعد، لا أداء مقيس.»
    - MA-006:
      EN: "The 2023 Instructions require providers to report all complaints, by type, to CBY-Aden's consumer-protection
      department every quarter (p.7), and provide for CBY-Aden to prepare and publish annual reports of aggregate
      complaint information (p.31). No such report was located on cby-ye.com (publications, news and the rules page,
      checked on the date of the search, which you write in full; a literal placeholder must never reach a page). A duty to report or publish does not show that the data exist publicly or that providers comply."
      Arabic to match.
    - VIS-OECD-FCP-TIMELINE ("sources differ"):
      EN: "The OECD (2026, p.35) describes the Instructions as adopted in August 2023 and 'in the process of being
      implemented', and states that customers of money exchange companies currently have no avenue for complaints or
      redress. The Instructions apply to all providers supervised by CBY-Aden and their agents. The two statements are
      shown as found; this resource does not reconcile them."
      Arabic to match.

(c) /methodology/, Yemen Post. Replace "any financial services it may offer" with:
    EN: "Yemen Post is not covered here. The World Bank (2024) describes the postal authority as providing payment and
    savings services; no count of its offices, accounts or balances is published."
    Arabic to match. First verify the wording in WB FSD 2024 and cite its page; if it is absent, leave the sentence
    unchanged and report why.

--- 6B-4 Remittances · lens: balance-of-payments statistician + Arabic editor --------------------------------------
(a) CLM-041 does_not_establish.
    - It currently says "do not apply to other balance-of-payments components". That contradicts IMF CR 26/80, Annex IV
      para 2 (printed p.41).
    EN: "The 1.838 ratio is specific to the remittance series. The 33% population ratio is the IMF's stated rule, as
    proposed by the authorities, for splitting its external-sector estimates between areas under the internationally
    recognized government and other areas; trade comes from government-reported data, and official grants are allocated
    wholly to the government. Neither converts CBY-Aden values into IMF values for any component."
    Arabic to match.

(b) CLM-007.
    - Add "as proposed by the authorities".
    - Add to does_not_establish: "The IMF publishes no whole-of-Yemen total; dividing by 0.33 gives a figure the IMF does
      not publish."
    - The 23_REMITTANCES caveat on RMO-IMF-2018 to 2024 currently reads "33% of the modelled total". Replace it with: "The
      IMF states that a demographic and behavioural model and a 33% population ratio for areas under the internationally
      recognized government, as proposed by the authorities, were applied; the IMF publishes no whole-of-Yemen total and
      none is derived here."
    Arabic to match.

(c) CLM-039, after PR #40.
    - Name the interface: "World Development Indicators holds no Yemen observation of personal remittances received
      after 2016 (last: US$3,770.6 million in 2016; checked 11 October 2026)."
    - Keep "other World Bank interfaces and earlier documented retrievals contained later observations" only with a
      locator for each. Otherwise remove it.
    Arabic to match.

--- 6B-5 The CWR-012 repair · lens: survey statistician + analytical-product red team + Arabic editor ---------------
The Reading stays only if this passes. Five defects, each found by attacking the published text.

(a) The prohibited-inference field is logically false, and it disclaims the one inference the numbers do support.
    Current, in both languages: "a higher share of recipients than of account holders does not show that recipients
    lack accounts" / «وارتفاع نسبة المتلقين عن نسبة أصحاب الحسابات لا يثبت أن المتلقين لا يملكون حسابات».
    That is wrong. Both shares are over the same universe and the same wave, so at most 11.9 percentage points of
    adults can be both recipients and account holders, and recipients without such an account are therefore at least
    the difference, as a share of recipients. The marginals do bound the overlap.
    Compute the bound from the publisher's own unrounded values, not from the rounded ones, because the publisher
    publishes both at full precision and the rounded inputs would only establish a weaker floor of about 62.5%:
      - received domestic remittances, indicator fh2, Yemen, database year 2022 = 31.9313981068809;
      - account at a financial institution, indicator fiaccount.t.d, same economy and year = 11.9033656433415;
      - (31.9313981068809 - 11.9033656433415) / 31.9313981068809 = 62.722066%, so the published figure is
        "at least 62.7%".
    Store both inputs in the API fixture with their indicator codes, their retrieval date and their locators. Verify
    the arithmetic yourself before writing it; if the publisher's values have moved, recompute and use yours.
    How it must be presented, and this is binding:
    - it is a bound that CauseWay calculates from two of the publisher's published shares, not a published statistic
      and not a World Bank figure. Label it as a calculation and name both inputs;
    - it is a bound on the group, not a statement about any individual recipient;
    - **it does not establish the channel.** It says nothing about how the money travelled, and it must never be
      used, quoted or arranged so as to support the channel hypothesis;
    - **it does not negate other means of holding money.** The survey measured an account at a financial
      institution. It does not rule out a mobile wallet or any account type the survey did not measure, and the
      World Bank publishes no mobile-money figure for Yemen at all, so the absence of one is not a zero.
    This correction makes the Reading more exact, not more confident. If it reads as more confident, it is wrong.
    EN, replacing that clause: "The two shares bound how far they can overlap: at most 11.9% of adults can be both,
    so at least 62.7% of the adults who received domestic remittances did not have an account at a financial
    institution. That is a bound on the group, not a statement about any individual, and it says nothing about how
    the money travelled."
    AR: «تحدّ النسبتان مدى التقاطع بينهما: فلا يمكن أن يجمع بين الأمرين أكثر من 11.9% من البالغين، أي أن 62.7% على الأقل ممن تلقّوا
    حوالات محلية لم يكن لديهم حساب لدى مؤسسة مالية. وهذا حدّ يتعلق بالمجموعة لا بأي فرد بعينه، ولا يقول شيئًا عن الطريق التي
    انتقلت بها الأموال.»
    The same false clause recurs in section 4 ("the survey values do not show whether the adults who received money
    were those without an account") and in section 7. Correct all three together, and keep the channel disclaimer.

(b) "Through accounts" never says whose account, and the Reading's central move depends on it.
    The question asks whether money reaches households "more through exchange companies than through accounts", while
    11.9% measures the recipient's own account ownership. A transfer can move through the banking system and be paid
    out in cash to a recipient with no account, so recipient account ownership does not settle whether the money moved
    "through accounts". Either the question means receipt into the recipient's account, which is what fin29_1
    measures, or the comparison cannot address it. Make the narrow meaning explicit in the question, the thesis and
    the hypothesis section: the subject is whether recipients received into an account of their own. A bank would
    otherwise have a fair complaint that its channel was dismissed with a statistic about customers' account
    ownership.

(c) The thesis goes stale the moment this instruction executes, and my own acceptance rules contradicted each other
    about it. Both are fixed here, by drawing the distinction they were missing.
    **The distinction.** Three different things must never be collapsed:
    - a **publicly documented response count**: the publisher's variable documentation records that the question was
      asked and that some recipients answered yes, as unweighted counts of respondents. This is documentation that
      the item exists and was answered. It is not an estimate of anything about the population;
    - a **weighted population estimate** of a channel for that wave: none is published by anyone, and none is held
      here unless the D16 tabulation exists and passes its anchor and disclosure checks;
    - a **historical channel value**: the 2014 profile, which is published, weighted, and not current.
    **What the Reading may and may not say, after this.** It may say that for the 2021 wave no weighted channel
    estimate is published or held. It may say that the publisher's variable documentation records the item as asked
    and answered. It may not say that the evidence base holds no 2021-wave channel evidence of any kind, because
    after 6B-1(c) it holds documentation; and it may not say that a channel value or estimate for that wave is held,
    because it is not. Write both halves, in that order, in both languages.
    So 6B-1(c) and this repair ship in the same transaction, never in different ones, and section 9's "channel
    values for domestic remittances from a current survey wave" is updated to name what is documented, what is
    estimated, and what is still missing.

(d) The flat mobile-money sentence is inside the Reading being kept.
    Section 3 reads "Yemen's survey did not ask the mobile-money questions". That is the sentence 6B-1(e) finds
    unsupported. It also travels into CLM-026's limitations as "two (using and saving with a mobile-money account)
    were not asked in Yemen's survey". Fix both here, with 6B-1(e)'s short form. Do not record the decision to keep
    the Reading on a text that still contains it.

(e) The title, the question and the first heading pull against the hedge.
    "How money reaches households" promises a mechanism; the question is a closed yes/no the evidence cannot answer
    either way; and section 1's heading, "What the evidence supports" / «ما الذي تسنده الأدلة», asserts
    evidentiary support over a paragraph whose content is a hypothesis. The Arabic «تسنده» is stronger than the
    English. A reader who reads the title, the question and the first section in order receives the channel
    conclusion with an endorsement, and meets the hedges two sections later. The owner has set the candidate to test
    first: a title and question that promise what the evidence can deliver rather than an answer it cannot, on the
    pattern of AR «الحوالات المحلية والحسابات: ما الذي تثبته الأدلة؟» and EN "Domestic remittances and accounts: what
    the evidence establishes". Test it against the alternatives in both languages, and give section 1 a heading that
    does not claim support for a hypothesis. If you keep a different title, say why in the report. Either way the
    title must not promise a mechanism the evidence does not measure, and the Arabic and the English must promise the
    same thing. The route does not change with the title.

Also, in the same transaction: section 4 asserts the evidence is "consistent with" a hypothesis about magnitudes -
"a main channel", "many households", a share of household cash - and then says no source measures any of them.
Silent is not the same as consistent. State that the evidence bears on whether recipients held accounts and says
nothing about magnitudes. And section 4 offers CBY-Aden's licensing classes as one of three supports for a
behavioural hypothesis, three sentences before the Reading itself says a listing is not operation. Remove it from
the supports; it belongs only where the Reading describes what the roster is.

====================================================================================================================
5. CLOSE-6E — EVIDENCE STRENGTHENING (each passes the deletion test: without it a reader loses a decision-relevant fact)
====================================================================================================================
--- 6C-1 Firms · lens: MSME specialist + Arabic editor -------------------------------------------------------------
(a) Informal firms, extending CLM-062. Source: WB FSD 2024, Annex III, Figs 114–116; rows FFO-2022-INF-*. State each
    base as the figure states it.
    EN (adjust to the bases): "Among 217 informal firms in the same 2022 survey, 49.8% of owners reported business-related
    debt. The sources named most often were own savings (54.4%), relatives (47.0%) and money lenders (22.1%); 1.8% named
    microfinance and 2.8% buying goods on credit. Firms could give more than one answer. The sample was drawn from lists
    of activities and locations and does not represent informal firms. These shares are not comparable with formal
    firms' 1.31%, which is supplier credit's average share of working capital among 328 formal firms."
    Arabic to match. Check that CWR-008 stays consistent.

(b) Add to CLM-059: "most of the 8,217 MSMEs SMEPS supported in 2024 (7,257) were smallholder producers and micro
    supply-chain enablers" (SMEPS AR 2024, printed p.9). Arabic to match.

--- 6C-2 After a transfer · lens: humanitarian cash / FCV + Arabic editor ------------------------------------------
    Extend CLM-045 and CWR-010. Paraphrase; no respondent quotations.
(a) Scale and channels of the programme around the pilot.
    New sources:
    - SRC-UNICEF-UCT-2024-10: "1.43 million vulnerable families supported with cash assistance across Yemen", 2 October
      2024, https://www.unicef.org/yemen/press-releases/143-million-vulnerable-families-supported-cash-assistance-across-yemen
    - SRC-UNICEF-UCT-2024-12: "UNICEF and partners launch the 19th Payment Cycle…", 7 December 2024,
      https://www.unicef.org/yemen/press-releases/unicef-and-partners-launch-19th-payment-cycle-current-unconditional-cash-transfer
    EN (CWR-010 boundary or interpretation_choice): "The pilot sat inside a much larger programme. UNICEF reported that
    the World Bank-funded unconditional cash transfer, implemented with the Social Fund for Development, reached more
    than 1.43 million families in its October 2024 cycle, paid at payment sites, through mobile teams and home outreach,
    and in an e-wallet pilot. Its 19th cycle, from 11 December 2024, ended the programme in its then-current form. The
    pilot's 45,460 recipients and the programme's 1.43 million families are different counts, and one is not a share of
    the other; families reached are not account holders."
    Arabic to match. Do not use the US$62.5 million: it was planned, not confirmed.
    The v2 plan to use ISR No. 9 (1,423,726) is dropped: UNICEF's releases are clearer on unit and channel.

(b) Cash-out at agents. Source: Pressure, p.8, fn 31–32. This is not the withdrawal limit, which PR #40 already
    carries.
    EN: "The same study reports what one programme manager told its authors: most cash assistance there was paid through
    microfinance banks as vouchers cashed at agents, and during Ramadan and Eid al-Adha 2026 agents often lacked enough
    cash, with waits of four to five hours and notes released only in YER 100 and 200 denominations. An e-wallet pilot
    disbursed funds without delays. This is one interview account; the e-wallet result concerns disbursement, not
    whether recipients could obtain cash."
    Arabic to match. Use «الصرف» for disbursement.

(c) Debt clearing. Sources: SAM 2024, p.16 and p.32; Cash Duration 2026, the endline "improved most" figure.
    EN: "Two studies of cash-assistance recipients in areas administered from Aden point to debt repayment as an early use
    of transfers. In a 2024 survey of recipient households, 40% reported debt repayment as a regular expense. In a 2026
    programme study, 'debts are paid off' was one of the two most common answers to which part of the household economy
    improved most, and was given more often by households that received six payments. In the 2024 study, 11 of 21
    business owners in one district and 10 of 21 in another said that fewer customers bought on credit when cash was
    distributed. Immediate cash-out is therefore not, by itself, a sign that a transfer failed."
    Limits: local samples of aid recipients; business-owner counts are not credit volumes; not national. Cite SAM by
    publication date (November 2024).

(d) /people/ ("Saving, borrowing and digital payments in the same wave"), bound to CLM-045:
    EN: "The borrowing sources shown here are family or friends and financial institutions. Shop credit, which local
    studies of cash-assistance recipients observe, is not among them."
    Arabic to match.

(e) Measurement Agenda evidence, through evidence bindings:
    - MA-009: UNICEF scale and channels, the programme's end, cash-out constraints;
    - MA-005: agent liquidity and banknote denominations, as local observations;
    - MA-001: SAM and Pressure for the shop/supplier-credit dimension.
    Never reuse "12% … as of 2026". Do not print ISP figures.

--- 6C-3 Remittance cost · lens: remittance statistician + Arabic editor -------------------------------------------
    VIS-REMITTANCE-COST: from two corridors to three (Saudi Arabia, the UAE and the United States).
    - Recompute US→Yemen for 2025 Q3 from the library's RPW dataset, as the simple mean of quotes at US$200 and at
      US$500. Our check: 12 quotes; 3.92% at US$200 and 2.30% at US$500.
    - Add rows RMO-RPW-US-2025Q3-200/500.
    - Keep the same limits. Update the caption and accessible text.

--- 6C-4 Credit infrastructure and regulation · lens: CBY regulator + Arabic editor --------------------------------
(a) REF-REG-012 and YSC-030.
    - The reporting rule (publications/149) cites Law No. 38 of 1998, Governor's Decision No. 4 of 1991, and Circulars
      33379 (1991) and 54064 (2006).
    - The enquiry rule (publications/150) applies "for any loan or financing, whatever its size", with customers checked
      against the notification list under Circular No. 2 of 2000.
    - The defaulters registry: "The 5 August 2026 announcement cites no instrument and publishes no coverage, threshold
      or record count."
    Arabic to match.

(b) MA-008, the Doing Business 2020 line.
    New source SRC-WB-DB2020-YEM-001: doingbusiness.org …/yemen/YEM.pdf, p.30.
    EN: "The last independent measure, the World Bank's Doing Business 2020 (data collected to May 2019; city covered:
    Sana'a; series since discontinued), put public credit-registry coverage at 1.3% of adults (216,245 individuals and
    firms) and private-bureau coverage at 0%. It is a historical reference, not a baseline for the registry CBY-Aden
    launched in 2026."
    Arabic to match. No index scores.

(c) FATF: add only if read on fatf-gafi.org itself; otherwise it is RESERVED.

--- 6C-5 Independent evaluation of rural credit · lens: MSME/microfinance specialist + Arabic editor ---------------
    New source SRC-IFAD-CPE-YEM-2011: IFAD Independent Office of Evaluation, "Republic of Yemen: Country Programme
    Evaluation", EC 2011/69/W.P.4/Rev.1, 6 October 2011, distribution Public,
    https://webapps.ifad.org/members/ec/69/docs/EC-2011-69-W-P-4-Rev-1.pdf
    New Evidence Record IFAD-CPE-YEM-2011-RF, with a D9 route, bound to /finance/ and /firms/.
    Verified:
    - para 176–177, printed p.40:
      - in completed projects, credit lines disbursed US$4.165 million (31% of US$13.37 million) to 3,723 clients (6%
        of 58,867 planned);
      - repayment ranged from 31% to 64%;
      - in Raymah, fewer than 1% of farmers in the project area received financing, against a 10% target;
      - in Tihama, 6% of households obtained loans;
      - in the Southern Governorates, the component was not implemented;
    - para 138–140, printed p.33:
      - the government bank partner (CACB) faced collateral demands, high transaction costs, long procedures and
        reluctance over interest;
      - women lacked land collateral;
      - project-built branches were sited away from commercial centres.
    EN: "An independent evaluation of IFAD's Yemen programme from 1993 to 2010 found that, in the completed projects,
    credit lines disbursed US$4.165 million, 31% of the US$13.37 million provided, to 3,723 clients, 6% of the 58,867
    planned. In one project area fewer than 1% of farmers received financing. The evaluators linked the shortfall to
    collateral requirements that women and sharecroppers could rarely meet, high transaction costs, long approval
    procedures, reluctance to deal with interest-bearing credit, and branches sited away from commercial centres."
    does_not_establish: "These are historical findings for specific project areas before the conflict; they are not a
    measure of rural access to finance today, and the delivery channels have since changed." Arabic to match.
    - MA-004: cite the record under the collateral and terms dimensions.
    - The new Reading (§6) uses it.

--- 6C-6 Domestic transfer channels (D16) · lens: survey statistician + Arabic editor ------------------------------
    Run this item ONLY when the owner supplies `findex_yem_channels_aggregates.json`, produced by
    `findex_domestic_channels_aggregates.py` (committed under audit/close_out/fixtures/ with the JSON; the data never are).
    1. Check the anchors first. If any anchor fails to reproduce, stop the item and report:
       - account at a financial institution: 11.9;
       - received domestic remittances: 31.9;
       - sent domestic remittances: 17.7;
       - sent or received: 37.8.
    2. New Evidence Record FINDEX-YEM-DOM-CHANNELS, class CAUSEWAY_DERIVED_AGGREGATE, with a D9 route. It is bound to
       /remittances/ ("Household behaviour is a different evidence layer"), /people/ and MA-001.
    Content: among adults who received domestic remittances in the 2021 wave (fieldwork November 2022 to January 2023):
    - the share who own a financial-institution account;
    - the share who received through an account;
    - among those asked the follow-up, the shares who received in cash and through a money transfer operator, noting
      that both can apply.
    Rules for the record:
    - Round every share to a whole number.
    - Give the unweighted bases.
    - Give no interval.
    - Note that receiving into an account does not mean owning one: some recipients without an account reported it.
    - Universe: the areas surveyed (about 23% of the population excluded). Not 2026. Domestic transfers between people,
      not remittances from abroad and not aid payments.
    Label: "computed by CauseWay from World Bank microdata; not a World Bank published statistic".
    Change MA-001 from "channels are not shown" to "channels were asked in the survey; a CauseWay tabulation of the
    respondent file is shown in FINDEX-YEM-DOM-CHANNELS; the World Bank's database publishes no channel series".
    Substitute the record's real identifier if you create it under a different one, and never leave a bracketed
    placeholder in any field: a placeholder that reaches a page is a defect, and gate CO-G07 looks for one.
    If the file has not arrived, record a FRONTIER card: "owner to run the aggregate script".

====================================================================================================================
6. CWR-013 — RESERVED, NOT PUBLISHED (D17 as amended)
====================================================================================================================
Do not publish this Reading and do not build its visual. CWR-012 took the one new-Reading slot D9 allows, and it is
published and sound. The reason is not the slot alone: CWR-013 fails the deletion test against /firms/ sections 7 to
9, MA-004 and CWR-008, and its stage-ladder visual would restate a ladder /firms/ section 9 already carries in prose.
The evidence for both verdicts is in §0. Record CWR-013 in W3f as RESERVED with this trigger: "the owner grants a second new-Reading
slot". Nothing of its argument is lost in this run: the same evidence and the same boundaries are published inside
/firms/, CLM-059, CLM-060, CLM-062 and MA-004 by §4 (6B-2) and §5 (6C-1, 6C-5), which needs no new route.

The specification below is held unchanged, so that if the owner later grants the slot the brief is ready and no
re-adjudication is needed. Do not act on it now.

HELD SPECIFICATION · lens, if ever run: analytical-product red team + Arabic editor
- EN title: "Programmes count guarantees and grants. Can firms borrow?"
- AR title: «البرامج تعدّ الضمانات والمنح. فهل تستطيع المنشآت الاقتراض؟»
Question: what programme figures (guarantees, grants, credit lines, KPIs) can and cannot tell a reader about MSME
access to credit in Yemen.
Thesis: programme figures measure programme activity, at the stage each one records:
- funding;
- issued guarantees;
- supported firms;
- a KPI against a target.
They do not measure whether firms can borrow. The only independent evaluation held in this evidence base found
delivery far below plan, and the firm surveys show bank credit is rare and informal sources dominate.
Bindings, existing and new records only:
- CLM-059 (SMEPS; YLG with both publishers);
- CLM-060 (SMEPS 19% against a 40% target);
- IFAD-CPE-YEM-2011-RF;
- CLM-062 (formal: 31/328, 1.31%; informal: 217 firms, money lenders and relatives);
- CLM-005 and CLM-006;
- MA-004.
Prohibited inferences:
- no guarantee count turned into firms or borrowers;
- no programme KPI turned into national prevalence;
- no 2011 evaluation turned into a 2026 rate;
- no OECD–YLG difference called an error;
- no USD conversion of rial amounts;
- no causal claim that programmes raised or failed to raise lending.
Sections:
- the standard house sections;
- one Reading visual, RV-CWR-013. It is a stage ladder (funded → issued/supported → reached firms → firms borrowing
  → outcome), with each stage marked "reported by the programme", "independently evaluated" or "not measured". It
  contains no numbers that are not in the bound records.
Placement:
- related reading on /firms/ (respect F2);
- link from MA-004.
Gate: publish only if both lenses pass, and the Arabic is read as Arabic, not checked against the English. Otherwise
keep it as development material with a FRONTIER card. It must not hold the other PRs.

====================================================================================================================
7. CLOSE-6F — SOURCES, REGULATION, HYGIENE, REGISTERS AND THE TWO REPOSITORY FINDINGS
====================================================================================================================
Most of v3's §7 is on main after #41 and #42 (§0). What is listed here is what remains. If any line is already true
when you reach it, drop it and say so.

--- 7a Source library · lens: source librarian + Arabic editor -----------------------------------------------------
- SRC-OECD-YEM-RESILIENCE-001: add the chapter HTML locator, and
  https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/promoting-economic-resilience-in-yemen_b66657c1/81ed2898-en.pdf
  as provenance ("publisher text read 11 October 2026"). The rights state does not change; nothing is reproduced.
- EXT-23, the January 2026 POS file:
  - keep 69b058d4bc306 as the primary locator;
  - add 6a6f950da3173 as an additional URL, noted "re-issued in a redesigned layout on 2 August 2026; values
    identical";
  - record both SHA-256 values. The FRONTIER card then closes, or says which half could not be fetched.
- CR-11: close it, or state in the report why it stays open.

--- 7b Regulation projection and chronology · lens: CBY regulator + Arabic editor ----------------------------------
- Confirm that all nine of REF-REG-002, 004, 005 and 007–011 carry why_it_matters and does_not_establish on their
  /data/ cards, and name any that does not. Ten cards were projected in CLOSE-6B; this is the check, not a redo.
- The CBY-Aden board's SAR cross-rate settings (31 August 2025; 13 February 2026): publish only on a located primary.
  Write "the board set", never "pinned". With no primary, RESERVED with its trigger. Do not infer the rate.
- The chronology rule is unchanged: an event enters only if a current public answer refers to the shift it explains,
  and the verb is "issued", never "implemented".

--- 7c Master hygiene (non-public) · lens: survey statistician + source librarian ----------------------------------
None of this was reported done; all of it stands.
- 24_FINDEX_CODEBOOK fin11a–f and the 27_FINDEX_SUBGROUPS compute contracts: relabel them
  NOT_PUBLISHED__DERIVATION_REQUIRES_D16_REVIEW. Under D16 they become possible; none is approved here.
- fin34a: correct the codebook label (published: 3.11% in 2022, 1.75% in 2014). Add both values to 25_FINDEX_BASELINE
  as data only.
- Mark 605 and 1,114 UNVERIFIED__DO_NOT_PROJECT in 00_MASTER and 12_VISUAL_PREVIEWS, and confirm that
  master_principles.json carries neither.
- Label OECD-YEM-012/013/014 NOT_PROJECTED__DIFFERENT_UNIT_AND_WINDOW_FROM_SMEPS_AR2024. Do not call them
  "superseded".
- In 29_OECD_BENCHMARKS, record these OECD 2026 assertions as ATTRIBUTED__NOT_PROJECTED, each with its reason:
  - 12% current account, 11% savings account, 68% phone access;
  - "almost 70%" of transactions outside the formal sector;
  - "some 70%" of deposits covered;
  - the YLG sector shares (sum 104%);
  - "22 banks operating";
  - Board decisions 7–11/2022. Their two-part numbers probably abbreviate CBY three-part numbers; do not map them
    until the signed decisions are read.
  Correct any earlier "not published by any source" state for these, appended with a date.
- 2013 Enterprise Survey collateral: 281.5% is held, the review read 284.3%. Re-read the original and correct if
  wrong.

--- 7d Registers, and the two repository findings · lens: source librarian + red team ------------------------------
- SOURCE_UTILISATION_2026-10-11.csv exists over 200 sources. Extend it, from the same committed script, to every
  source added in PR-3 and PR-4, keeping one row per source, the use_state, the reason code and the bound objects.
- W3f: one entry per RESERVED item in §9, with its reason and trigger — including CWR-013 and the SAR settings.
  ADD3-O1, the Cash Consortium's own Arabic name, stays OWNER-OPTIONAL and is not changed in this run.
- W3f, CWR-012: replace v3's planned retirement record with the facts. "Published on 11 October 2026 in CLOSE-6C. The
  steward's instruction to keep it retired was withdrawn the same day: the three grounds for retirement — a
  marginal-shares inference, an unreviewed Arabic text, and the Cash Consortium findings not held as records — were
  each met in the transaction. The retirement was never caused by a ban on microdata." Add the open editorial item on
  "households" and its PR-3 decision.
- OPENAI_REENTRY_CHECKPOINT.md: the search-record count is 514, not 476. Correct it and the date of that paragraph.
  Check every other count in the same paragraph against the bytes and correct any other drift the same way.
- README.md "Current state": record STAGE A COMPLETE at 53dccc4d and the Stage A addendum (#39 to #42, 11 October
  2026), with the current public inventory. Claim no new status.
====================================================================================================================
8. ACCEPTANCE TESTS AND GATE CO-G07 (CO-G07 is added in PR-6)
====================================================================================================================
Global, after each PR:
- 9/9 CI;
- negative controls n/n;
- generate_projections --check;
- bilingual_invariance 0;
- test_content_parity;
- literal audit 0 / 0.

CO-G07 extends validate.py's close-out family with one negative control. **It pins retired assertions in their
context, never bare strings.** A gate that forbids a string forbids the legitimate uses of that string too, and a
number or a date is not false in itself. Each entry names the assertion, the surface it is forbidden on, and the
context that makes it legitimate elsewhere:
- "14 business days" as the escalation window, outside an attribution to the 2024 brochure, and its Arabic;
- "no source here reports cover, premiums or payouts" as a statement about the deposit-insurance scheme;
- "do not apply to other balance-of-payments components", as CLM-041's non-establishment;
- "12% of adults" as an account-ownership figure for Yemen;
- "1,149" as a count of removed sites, and "8.54" as a portfolio-at-risk figure;
- 35.2% presented as a comparator for Yemen's 11.9% without 24.5% in the same paragraph;
- 5,731 without OECD attribution in the same sentence;
- any CAUSEWAY_DERIVED_AGGREGATE figure printed without its label;
- "the channel is not measured", and its Arabic, as a route description;
- any count of economies attributed to the World Bank for the low-income aggregate, "19" among them;
- "at least 62.7%" printed without the label naming it as CauseWay's calculation.
One entry from the earlier draft is withdrawn, and the reason is recorded with the gate: a bare ban on the string
"9 January 2023" would forbid a correct publisher statement. The microdata catalogue gives the fieldwork end as
9 January 2023 and the survey methodology table prints 10 January 2023; both are the publisher's own, the public
pages carry month precision, and the day-level pair belongs in the record with both locators, not in a prohibition.
For the same reason the gate never forbids a legitimate number, only an assertion made with it.

Specific checks, in dist, in both languages:
1. 3,387, YER 6.4 billion, YER 9.4 billion and 6,976 appear with "letters of guarantee" / «خطاب ضمان» and "sum".
   3,526, 8.54 and any YLG sector share appear nowhere.
2. «مليوني ريال» and "Art. 33" / «المادة 33» are on the deposit-insurance entry. No OECD "70%" appears anywhere.
3. "20 August 2023" and "589/CBY/2023" appear on /reforms/. "28 August 2023" appears only as the announcement date.
4. The IFAD record carries "1993 to 2010" and its does_not_establish.
5. The UNICEF sentence says the counts "are different counts, and one is not a share of the other".
6. Reverse traces run both ways for CLM-059, IFAD-CPE-YEM-2011-RF and (if created) FINDEX-YEM-DOM-CHANNELS: page →
   record → source → locator → page and rights.
7. On the Reading's route and its route description, in both languages: the hypothesis wording survives, adults are
   never called households, and the two halves of 6B-5(c) are both present - no weighted channel estimate for the
   2021 wave is published or held, and the publisher's variable documentation records the item as asked and
   answered. Neither half may appear without the other.
8. "19" appears nowhere as a count of economies, in either language, and no page attributes an economy count to the
   World Bank. 18.31, 18.3% as a mobile-money aggregate, and "mobile money account" as a low-income comparator appear
   nowhere.
9. Every surviving "not asked" / "did not ask" about the mobile-money questions, and its Arabic, sits in the same
   field as all three observed facts. Everywhere else the short form of 6B-1(e) is used instead.
10. "the latest year the programme has published", and its Arabic, appears nowhere.
11. On CWR-012, in both languages: the corrected bound appears as "at least 62.7%", labelled as CauseWay's
    calculation from two named published inputs, with its group caveat, with the sentence that it does not establish
    the channel, and with the sentence that it does not rule out an account type the survey did not measure. No
    sentence says the shares cannot show whether recipients lacked accounts. The question and thesis say whose
    account. No section says the evidence base holds no 2021-wave channel evidence of any kind. The licensing
    classes are not offered as support for the hypothesis.
12. The complaint text names the supervision scope in its own sentence; no page says "a provider" unqualified. The
    e-money 10-business-day rule on VIS-E-MONEY-RULE-STACK and /reforms/ is unchanged and still attributed to the
    instructions of 9 August 2023.
13. The deposit-insurance entry carries Art. 33's three rules, the year of the YER 2 million ceiling, the authority
    as the law names it, and no present-tense claim that banks pay. No literal "[date]" or other placeholder appears
    anywhere in dist, in either language.

Arabic-editor acceptance:
- «خطاب ضمان», never «منشأة مستفيدة»;
- «تقودها نساء» and «يملكها رجال» kept distinct;
- «يوم عمل» and «يومًا» used exactly as the instrument uses them;
- «حساب لدى مؤسسة مالية» and «حساب أموال عبر الهاتف المحمول» kept distinct;
- «بالقيمة الاسمية» attached to the OECD dollars;
- «ولا يُدمجان في سلسلة واحدة»;
- «أسر» (families) is never rendered «أصحاب حسابات»;
- «فرضية» stays in the CWR-012 thesis;
- both authorities named neutrally.

Red-team acceptance: per transaction, the domain lens names the strongest remaining misreading. Fix it or record it.
====================================================================================================================
9. RESERVED AND EXCLUDED (record them in W3f; do none of them now)
====================================================================================================================
RESERVED. Each item is admissible but not needed for a current answer. Record its trigger.
- WFP 2025 audit, and WFP annual country reports. The public summary has no channel or account data; read the full
  report only if MA-009 needs it.
- UNDP ESPECRP achievements (716 VSLAs; 10,020 MSMEs; 131,178 households), CGAP and CARE savings-group counts:
  programme outputs, no activity evidence.
- OECD/INFE comparator averages (by owner decision only).
- The WB Yemen Economic Monitor line on CBY remittance data (CR-15 placed it in CLM-043).
- YLG stock, youth and rural shares, and PAR. YLG reports after 2022.
- The ESPECRP funds frozen at YKB (RES00988): verified, but no pathway to people.
- CPMI–SWIFT data ending in 2022.
- The OECD DGS statements, and Box 2.1 decisions 7–11/2022.
- The 2007 WB MSE survey.
- Primary copies of Decree-Law 37/1992, Law 40/2006, Circular 11/2014 and Law 64/1991.
- The 2022 and 2023 exchange registers, and the 2025 enforcement wave.
- Board Decision 8/2022.
- The FAS branch series; IDA H870; fin30; crypto awareness.
- CCY "Barriers to Interoperability".
- P514855 targets; the UNJSPF hold.
- The SAM p.37 note on hawala and debt as income.
- The FATF line, if not read at source; the SAR settings, if no primary.

EXCLUDED. Never publish; record the reason.
- The respondent file itself, any row-level output, and any derived figure outside D16's conditions. The Microdata API
  key.
- RI-001…005; 605 / 1,114; "~800 unlicensed"; "700–800 providers".
- The predecessor's computations and withdrawn repairs (FX pin, Monte Carlo, Shapley, deflation signs, 72.1%,
  localisation analytics, donor AR(1), ÷0.33).
- YLG: a sector pie or renormalisation, PAR, growth rates, partner and governorate tables, USD conversions,
  repeat-borrower inference. "1,149 of 3,371 sites removed".
- AMAL; CCY "Estimates and Impact"; IGC survey prevalence and its USD 3.8 billion; corridor shares 60/18/5/5; SAMA
  outflows; OCHA funding totals as inclusion results.
- UNICEF Al-Khawkha 2026 (a local case) and the UNICEF SPSF 2025–2030 targets presented as results.
- CGAP's responsible digital credit framework as Yemen evidence.
- OFAC GL 24A interpretation, exchange-company designations, MENAFATF reports.
- OECD 12/11/68, both "70%" figures and "22 banks operating" as public figures.
- Every "12%" restatement; fin29 printed as 0; Doing Business index scores; ISP chart-read shares.

ADDED 11 OCTOBER 2026, AFTER PR #42.
THE CASH CONSORTIUM'S ARABIC NAME (ADD3-O1), as the owner has now decided it: use a natural institutional Arabic
rendering and show the original English name beside it on first use. **Do not present any Arabic rendering as the
organisation's official name without a document from the organisation that uses it.** My earlier note treated
«اتحاد المساعدات النقدية في اليمن» as the consortium's own name; that was not documented, and it is withdrawn. If a
document from the consortium establishes a name it uses for itself, record the locator and use that; otherwise keep
the current rendering with the original shown, and record that no self-naming document was located. This stays
OWNER-OPTIONAL, and it is one transaction when it comes, not a find-replace across 89 places.

ARABIC-EDITOR QUESTION, not a change in this run: the Arabic names the Global Findex
«المؤشر العالمي للشمول المالي» in 574 places, while elsewhere it writes «قاعدة بيانات Global Findex». A red team
read «مؤشر» as turning a database into an index or a ranking, which is the thing this product refuses elsewhere. I am
not ordering a 574-place change on that reading. Put the question to the Arabic editor properly: what does the World
Bank's own Arabic material call it, is «مؤشر» the established Arabic for Findex, and does the inconsistency between the
two forms matter more than either form? Record the ruling; change nothing in this run.

STAGE B DELIVERY CONDITIONS, not work for this run and not part of closing Stage A: the Stage B charter and the
amendments file it depends on are **not in the repository**. The charter exists only outside it and instructs that it
be committed as audit/close_out/STAGE_B_DESIGN_CHARTER.md, and it cites AMENDMENTS_D16_D22.md, which is also absent
from main. Before Stage B is handed to anyone, both must be committed, the approved text of each must be established
rather than assumed from a filename, and the authority of decisions D16 to D22 must be recorded. Do none of it now,
do not start W4, and do not let it enter a Stage A transaction. Record it as a Stage B precondition with that wording.

STAGE B INPUT, not work for this run: CWR-012 has no governed visual. Its visual_bindings is empty and there is no
RV-CWR-012 in either visuals file, where comparable Readings carry one (CWR-008 carries RV-CWR-008 through the
library, the design contracts, the closure file and its page spec). Record it as a Stage B item for the
visualisation lens and do not build a visual now.
RESERVED:
- CWR-013 (§6). Trigger: the owner grants a second new-Reading slot.
- The CBY-Aden board's SAR cross-rate settings. Trigger: a located primary document.
- The Cash Consortium's own Arabic name, «اتحاد المساعدات النقدية في اليمن», against the site's «تحالف النقد في
  اليمن» in 89 places (ADD3-O1). Trigger: the owner's word. It is one transaction when it comes, not a find-replace.
EXCLUDED: nothing new.

====================================================================================================================
10. STAGE A ADDENDUM REPORT, THEN STOP
====================================================================================================================
1. PRs with merge SHAs, and the Master SHA before and after each transaction.
2. Literal closure after each PR.
3. Each item, in one of four states, **and the test that confirmed it**. A state without a named test is not a
   result. The test is one of: a dist assertion in §8 (name its number); a gate or negative control (name it); a
   reverse trace from page to record to source to locator and back; a re-read of the original with its page number;
   or, where none of those applies, the words "no test applies" with the reason, which I will review. The four
   states:
   - merged;
   - changed by evidence (quote the original);
   - blocked (name the blocker);
   - dropped as already done.
4. A table of new sources, new records and new numbers.
5. Whether the D16 aggregate arrived, and its anchor check.
6. CWR-013: the W3f RESERVED entry, and where in /firms/ and MA-004 its argument was published instead.
7. Source utilisation counts, and the W3f, RESERVED and EXCLUDED registers.
8. Gates: 9 checks, negative controls n/n, CO-G07.
9. What was verified locally, what only in CI, and what not at all (browser, RTL and mobile on /firms/, /reforms/
   and /remittances/ at least).
10. Any challenge to this instruction.
11. The CWR-012 title decision, its reason, and the CO-G07 entry that protects it. Then one of two outcomes for the
    Reading, stated plainly: repaired and kept, with both lens verdicts and the corrected overlap bound as published;
    or withdrawn, with where each exclusive paragraph went and what the withdrawal touched.
12. The two repository findings: the checkpoint's search-record count and README's programme state, each with the
    commit that closed it, and any other count drift the same check found.
Then STOP. 9/9 CI is not release approval. Stage B starts only on the owner's word, in a separate session.
