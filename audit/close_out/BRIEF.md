CLOSE EVERYTHING BUT HOSTING — FINAL EXECUTION BRIEF (Claude Code). Version 5, 10 October 2026, Aden.

This brief supersedes every earlier version, YFIE_README_AND_HOUSEKEEPING_PROMPT_2026-10-10.md, the V2/V3 design
prompts, the OpenAI "current-source design handoff" kit, and its Claude Code port mandate. Run this one only.

It rests on:
- an eight-reviewer audit of main 2ddbfb61 (10 October): findings in Appendix A–F, with IDs;
- the adjudicated OpenAI Arabic review: ARABIC_REVIEW_ADJUDICATION_2026-10-10.md and
  YFIE_ARABIC_ACCEPTED_EDIT_REGISTER_2026-10-10.csv.

Findings are leads to verify, not authority: the repository and the originals decide.

═══ EXECUTION PLAN — one window, three stages, committed stage by stage ═══
Run everything in ONE Claude Code window (Opus, maximum reasoning), as three stages in strict order. Nothing waits
until the end: every workstream ends with a merged PR and a PROGRESS.md line.

| Stage | Scope | Ends when |
|---|---|---|
| **A — Evidence and Arabic** | W0, W1, AR-1, W2, W3a–W3f | its last PR is merged |
| **B — Structure, tools, design, visuals and footprint** | W4: G0 → S → T → G1 → G2 → W4F → G3 | its last PR is merged |
| **C — Governance, SEO, documentation, editorial pass and acceptance** | W5, W6, W6S, W7, W8 | the final reply |

Checkpoints:
- After each stage, write a ≤15-line checkpoint in PROGRESS.md ("STAGE A COMPLETE at <sha>", with open issues).
  Send the stage report (format below) and stop.
- The owner forwards the report to the advisor for review. The next stage starts on the CONTINUE message. This is
  the quality gate between stages.
- If the context compacts, or the window ends, the next step is always: read audit/close_out/BRIEF.md (§0, §1, the
  current stage and the appendices it cites) and PROGRESS.md, then continue. Never restart a finished workstream.
- A new window resumes with the one-line resume message in 00_START_MESSAGES_FOR_CLAUDE_CODE.md.

First commit (branch `close-out/a-inputs`, its own PR). Add, unchanged:
- this brief → audit/close_out/BRIEF.md;
- the register and adjudication → audit/arabic_review/;
- the OpenAI package → audit/arabic_review/openai_2026-10-10/, as lineage;
- the house style → audit/naming/ARABIC_HOUSE_STYLE.md.
Classify them in the manifest. None of these is ever projected to a public page.

Stage report format, sent at the end of each stage (the owner forwards it to the advisor for review):
```
STAGE <A|B|C> REPORT — main <sha> — <date>
1. Merged PRs: #<n> <title> <merge sha> (one line each)
2. Findings closed: <IDs> | FRONTIER: <IDs + reason> | stopped: <IDs + reason>
3. Arabic register: applied <n> / conditional resolved <n: outcome> / stopped <n: why>
4. Numbers changed publicly: <record: old → new, locator>
5. Gates: CI 9/9 <yes/no>; negative controls <n caught / n>; new gates added <list>
6. Measurements (Stage B): page → phone screens before/after; G1 scores; DL-V2-001
7. Open questions for the owner (maximum 3, each with your recommended default)
8. Next stage: <ready / blocked by …>
```

Skills and plugins. Load each only when its workstream starts, and only if it is listed in your environment; never
invent one.
- **Always:** multi-agent-m.
- **Design (W4):**
  - frontend-design, webapp-testing;
  - design:design-critique, design:design-system, design:accessibility-review, design:ux-copy;
  - impeccable (if installed); dataviz (for any chart);
  - web-excellence (if installed).
- **SEO (W6S):** marketing:seo-audit.
- **Before each PR in Stages B and C:** engineering:code-review and engineering:testing-strategy.
- **Arabic and English editing:** writing-quality skills where listed.
Skills advise; this brief and the gates decide.

Efficiency rules (no loops, no wasted reads):
- Never load page_specs.json (20 MB), PUBLIC_LITERAL_CLOSURE.json or dist HTML whole. Query them with python or jq.
- Do not re-read a file whose content is already summarised in PROGRESS.md or in a subagent's report.
- Subagents get one bounded task each and return compact tables, never dumps.
  - Never give two subagents the same scan.
  - Use the cheapest capable model for extraction, a mid-tier model for checking originals, and keep judgement
    (Master text, statistics, Arabic meaning, design choice) in the lead thread.
- Open each original once, and check every dependent fact in that pass. Write a decision once and refer to it by ID.
- During development run the targeted tests. Run the full CONTRIBUTING §5 gates once, before each push; CI repeats
  them.
- Failure rule (the only one): if a step fails twice, record it in PROGRESS.md, skip only the steps that depend on
  it, and continue with independent steps. Halt the whole run only on a Master, authority or data-hygiene failure.
  Never loop, and never weaken a gate.

═══ 0. WHO YOU ARE AND THE RULES ═══
You are the programme's lead integrator and the ONLY session writing to CausewayGrp/Financial-inclusion-.
- Base: the latest origin/main (2ddbfb61 or later). Record the SHA.
- At the end exactly one thing may remain open: **hosting**. Everything else ends in exactly one state:
  CLOSED, HOSTING, FRONTIER (a disclosed evidence limit with a verification card), OWNER-OPTIONAL or DECIDED.
- You never invent a fact to close an item. An original you cannot reach becomes a FRONTIER card; it is not guessed.

Rules:
- **Agents.** Load the multi-agent-m skill first and run hub and spoke. Parallel subagents read, verify originals,
  edit language and red-team. You alone write.
- **Branches and merging.**
  - One workstream, one branch, one PR at a time, each rebased on the latest main.
  - CI must pass 9/9; merge with "Create a merge commit". The owner pre-approves merging every PR in this brief.
- **The Master.**
  - Changes go only through audit/tranche_b_execution/run_stage.py, strictly serially, never hand-edited.
  - Bilingual numeric invariance stays at 0.
  - Every new public number is bound to a source-traced record with a public locator (AGENTS rule 5).
- **Read in the original.**
  - Every new or changed fact is read in its original, and the locator is recorded (page/table/paragraph or the
    series URL).
  - A draft, a secondary article or an earlier summary is a lead only.
- **Language.**
  - English and Arabic are written together, and the Arabic is written as Arabic.
  - Use the terminology register (audit/naming/) for every public name.
- **History and pushing.**
  - Never force-push. Never rewrite main, a tag or an audit record (append only).
  - Never delete a tracked file. Two exceptions:
    - a cleanliness BLOCKER (W6) is untracked with `git rm --cached`, recorded;
    - a credential found anywhere, history included, is reported for rotation.
    Branches are removed only by the owner-run workflow (W5).
  - Before every push, confirm that every commit on the branch is from this session. A foreign commit means stop
    and report.
- **Data hygiene.**
  - Never use, request or store a World Bank Microdata API key.
  - Never download, commit or publish respondent microdata (*.dta, *.csv or any respondent file), and never compute
    a figure from it. For Findex values use only the open api.worldbank.org/v2 series and public DDI metadata.
    Published World Bank reports and methodology documents are allowed and required (CR-02, CR-14).
- **Design is in scope (D7).** Page structure and visual design are both executed in this programme, in W4 (Stage
  B), by Claude Code. Claude Design is not used.
- **Content preservation (D13).** Never cut, shorten or paraphrase governed content to make a page shorter.
  - A block may move into a disclosure.
  - A block may be replaced by a link only when the identical text exists at the link target; that is removing a
    duplicate.
  - The primary-tier answer, its limit and its source line stay visible.
  - Length is reduced by structure, rhythm and de-duplication, never by deleting meaning.
- **Claims.** Never declare DESIGN HANDOFF READY or PUBLIC RELEASE READY. Claim no WCAG conformance, legal review,
  rights clearance or certification.
- **Gates.** Never weaken a gate to pass it (failures follow the failure rule above). Where a gate
  encodes a structure this brief deliberately changes (e.g. RC-1115 record-head order), replace it with a gate for
  the new rule, record why, and add a negative control.
- **Progress and reporting.**
  - Keep audit/close_out/PROGRESS.md (append only): one line per finding ID closed, with PR and SHA. A later
    session must be able to resume from it alone.
  - Report one line per merge.
- **Arabic review.** The OpenAI Arabic review has been adjudicated, and only the accepted register is applied (AR-1
  and the rows tied to CLOSE-2/3/5). Whenever this brief merges, splits, renames or removes a section or UI string,
  record it in audit/close_out/KEY_MIGRATION.csv: old_key, new_key, change, PR.

═══ 1. OWNER DECISIONS (record verbatim, append only, in audit/OWNER_DECISIONS_2026-10-10.md) ═══
- **D1 About and funding (OWN-01).** /about/ §6 already says that CauseWay funded this edition from its own
  resources, and that no donor, regulator, source institution or external commissioning party funded it. Keep that
  text.
  - Add one sentence after it, Master-first, in EN and AR: "It was not commissioned by, and is not reviewed or
    endorsed by, any institution whose data it presents."
  - Apply the register row AR-035 (the same page, §1) in the same transaction, CLOSE-1.
- **D2 Contact (OWN-02).** office@causewaygrp.com is monitored. CLOSED.
- **D3 Code licence.** The software code is not openly licensed: all rights reserved, deliberately.
  - State it in the README, on /rights/ (Master-first) and in a short LICENSE-CODE note.
  - CC BY 4.0 covers CauseWay's own content only.
- **D4 Downloads.** public_downloads stays OFF in v1, deliberately: the reuse terms of third-party sources are not
  assessed for most sources (166 of 167; ADJ-RG-01), and bulk export is redistribution. This is a decision, not a pending item.
- **D5 Analytics.**
  - The build ships no analytics script, no cookie and no third-party tracker.
  - At hosting only, the owner may switch on host-side aggregate request counts (decision B14): server logs only, no
    script, no cookie, no profile, no IP address retained in reports.
  - Draft the /privacy/ wording (EN and AR) as a ready transaction payload in docs/RELEASE_RUNBOOK.md step 11. It is
    applied Master-first on the day counts are switched on, never before.
- **D6 Arabic.** No certification is sought or claimed. The external Arabic review is a quality pass, not a release
  blocker.
- **D7 Design (owner, 10 October, 19:45).** Design is executed in this programme by Claude Code (W4). Claude Design is
  not used.
  - handoff/ and the OpenAI offline design kit are superseded. Their valid quality criteria are carried into W4
    (Appendix H).
  - The design direction is chosen by a recorded, criteria-based decision (W4 G1). Before/after screenshots go in the
    PR so the owner can veto, but approval does not block the work.
  - IBM Plex Sans and IBM Plex Sans Arabic remain the only families. Weights and sizes may change on measured
    evidence.
- **D8 Navigation** (owner delegation of 10 October; it supersedes only the hub-numeral part of B-c).
  - Remove the hub numerals (01–05): they imply a sequence the product does not have. Edit `hub_numerals` in
    navigation_interaction.json under D14.
  - "Method and measurement" becomes one link to /methodology/, so the desktop navigation is one row. /methodology/
    carries a prominent first-screen link to /measurement/.
  - This is a Master 04_NAV_UX transaction (run_stage.py), because global_navigation is regenerated from 04_NAV_UX
    (scripts/projection/derived.py). Never hand-edit it.
  - Keep each page's own label: the footer link and breadcrumbs for /methodology/ still say "Methodology", and
    /measurement/ keeps "Measurement priorities". Adjust _align_navigation_contract and gate P4-G03 accordingly, with
    reasons.
  - Update the Context public_navigation and any manifest P4-G03 checks.
  - The phone menu keeps the owner-decided items (A-12, C-6, C-8): hubs, domains, language switch, then the trust
    links and Cite as a compact secondary group. Only presentation changes.
  - Hub labels are unchanged. The Arabic review confirmed them:
    - EN: Questions / Evidence / Readings / Sources / Method and measurement;
    - AR: الأسئلة / الأدلة / القراءات التحليلية / المصادر / المنهج والقياس.
    CLOSED.
- **D9 Scope boundaries.** No new page family, hub or tool route. New detail routes created Master-first are
  allowed (a Reading such as CWR-012, or /evidence/<ID>/ for a new record or visual), with their
  navigation-contract route entries.
  - At most one new Reading (CWR-012, conditional, W3e).
  - Home and /explore/ keep the R8.4A model: no new task taxonomy.
  - Python 3.11 is the minimum, with a fail-fast preflight and no 3.9 shims.
- **D10 Naming providers.** A named provider may carry a figure only when a primary public source (the regulator or
  the provider itself) states it. Otherwise the provider is described, not named. Enforcement names stay
  non-public.
- **D11 Arabic review.** The adjudicated register is final. Rows marked RETAIN are not applied. Conditional rows
  follow their condition. The house style is adopted under the existing naming register
  (audit/naming/NAMING_DECISIONS_2026-10-10.md and terminology_register.json).
- **D12 Environmental footprint (owner, 10 October).** Every page shows a measured, restrained footprint line, and
  /about/ carries one section on the site's footprint and CauseWay's operations (W4F, Appendix G).
  - No generic environmental claims ("green", "eco-friendly", "sustainable website", "carbon neutral", "net zero").
  - CauseWay's operational statements use the exact owner-confirmed wording in Appendix G.
- **D13 Content preservation.** As in §0: nothing governed is cut or shortened for length.
- **D14 Steward designation (owner, 10 October: "give Claude Code the freedom to handle things").** This
  Claude Code run is designated programme steward for the two controlled contracts, for the scoped changes only:
  - navigation_interaction.json: hub_numerals and the phone-menu presentation (D8, CR-S12), and new detail-route
    entries (D9);
  - presentation_priority.json: the measurement-link limit (RD9), and tier groupings if the TOC rule needs them
    (S10).
  Each edit is its own commit naming its finding. AGENTS.md rule 2 is amended in W2 to record this designation
  and its scope.
- **D15 Site-operation metrics.** The footprint values (Appendix G) are measurements of this website, not evidence.
  They sit outside AGENTS rule 5, under their own gate. Amend rule 5 in the W4F PR to say so.

═══ 2. WORKSTREAMS (in this order; every one is in scope) ═══

W0 — Inventory (read-only, parallel; report in ≤15 lines)
- Main SHA, open PRs (expect none), branches, CI on main. Run the full gates and record the results.
- Read FINAL_OPEN_ITEMS_REGISTER.md and give every item its true status. Stale rows known at 2ddbfb61:
  - EAD-03, EAD-06, EAD-07, EAD-11: done;
  - EXT-01, EXT-02, EXT-03: closed 3 October;
  - OWN-01, OWN-02, OWN-05: done; OWN-04: closed 10 October;
  - REL-02: 166 of 167 sources not assessed; one carries a research licence (ADJ-RG-01).
- Launch in parallel now (read-only): the W3a currentness sweep, and the original-reading for every finding in
  Appendix A.

W1 — Master transaction CLOSE-1: decisions and truth fixes (each confirmed by the W0 original-reading first)
- D1 and D3 copy.
- OWN-10: fix the Master's stale self-counts (143 pages, 10 Readings, 165 sources) to the true values. Make them
  computed or gated so they cannot drift again.
- CR-04: fix the locators of WB-FINDEX-OBS-2022-010/011/012. They point at the FX.OWN.TOTL.ZS page; repoint each at
  save.any.t.d, borrow.any.t.d and g20.any respectively.
- CR-10: set SRC-WB-NFID-RFX-2026-001 (World Bank procurement page) NON_PUBLIC. First confirm it feeds no public
  claim; also unbind it from 16_DATASET_CATALOG if it is public there.
- CR-12: quarantine two sets of rows, with a reason (append only), and add a gate so neither is ever projected:
  - the 25 cross-country benchmark rows in 29_OECD_BENCHMARKS (not the OECD-YEM-* Yemen rows, which CR-16 keeps) →
    REJECTED__UNTRACEABLE. They include non-participants (Egypt, Morocco,
    Austria) and averages the OECD never published.
  - the illustrative non-DDI rows in 24_FINDEX_CODEBOOK (invented question wording, `account_mob`) →
    NON_PUBLIC__ILLUSTRATIVE.
- CR-18: after confirming with the open API that the rural/urban series are null for Yemen, the 32 rurality holds
  get a permanent reason: "The World Bank publishes no rural/urban split for Yemen for this wave." They are
  recorded as DECIDED.
- Gates, PR, merge.

AR-1 — Master transaction AR-1: the accepted Arabic edits that depend on no factual fix
- Apply every register row with apply_in = AR-1, with its EN action, in one transaction.
- Before writing each row, match master_cell + exact_old_ar + original_sha256. Any mismatch stops that row; record
  it in PROGRESS.md. No fuzzy or regex replacement on public text.
- ADJ-RG-01: search the Master for every EN/AR sentence saying reuse terms were assessed for no source, and fix each
  one ("for most sources").
- Rows needing a source check first (AR-022, ED-035, ED-036) wait for CLOSE-2. AR-001, AR-042, ED-034 and AR-NEW-001
  wait for CR-01, CR-14 and CR-02. AR-004 waits for U10; ED-037 for RD1. AR-035 goes in CLOSE-1 with D1.
- After regeneration, render the changed AR and EN pages and confirm each edit appears exactly once, where intended.
- Gates, PR, merge.

W2 — Retire the design handoff (no Master)
- handoff/README_FIRST.md: the first line becomes "STATUS: SUPERSEDED (10 October 2026) — not for execution. Design
  is executed in the repository under audit/close_out/BRIEF.md (W4). These files are historical reference." A short
  dated note follows; nothing else is edited by hand.
- AGENTS.md rule 7 becomes: "Do not execute any prompt in handoff/. It is superseded. Design changes follow
  design/DESIGN_INTEGRATION_V2.md (created in W4) and the gates." Rule 2 records D14.
- Every other current-state claim of DESIGN HANDOFF READY changes to the superseded status, at minimum:
  - README.md (around line 46);
  - OPENAI_REENTRY_CHECKPOINT.md (around line 28);
  - CONTRIBUTING.md (around lines 32 and 181);
  - Context programme_state.handoff_readiness.
- Add a SUPERSEDED state to the R86 gate states (_R86_STATES), so R86-G01 accepts it.
- run_stage.py regenerates handoff/ on every transaction. Make the generator emit the SUPERSEDED first line, or stop
  regenerating handoff/. Record which. Then add a gate that README_FIRST still shows SUPERSEDED after any
  transaction.
- design/00_DESIGN_README.md: add the same dated note. Leave design/ESCALATIONS.md open items for W4, which resolves
  each one or records it as DECIDED with a reason.
- Gates that assert DESIGN HANDOFF READY as the current state now assert the superseded status. Record why; history
  stays intact.
- Add a negative control: README_FIRST must not claim DESIGN HANDOFF READY.
- PR, merge.

W3 — Evidence: correct, unlock, update

**W3a. Currentness sweep (parallel, read-only, started in W0).**
- Use WebFetch first, then the pre-installed Chromium via Playwright where a page needs a real browser. Check the
  Arabic CBY site where the English one lags.
- Targets:
  - CBY-Aden "Monetary and Financial Developments" Issues 55 and 56;
  - POS monthly releases for July–September 2026;
  - FMIIP (P180708) ISR sequence 3;
  - World Bank RPW, the latest quarter (the repo uses 2025 Q3);
  - the IMF press release and documents for the Staff-Monitored Programme announced about 7 October 2026;
  - ESPECRP ISR of 30 June 2026 and successor P514855;
  - the "Cash for Nutrition and Livelihoods" PAD (approved 30 June 2026);
  - SMEPS annual report 2025;
  - ESCWA "Enhancing MSME Support Systems in Yemen" (July 2025);
  - the full text of the World Bank Yemen Economic Monitor, Spring 2026;
  - EXT-01…EXT-19 and every "source that needs a browser".
- Verdicts:
  - VERIFIED (exact locator) → a Master transaction;
  - DIFFERS → a Master correction;
  - UNREACHABLE → a FRONTIER card: the dated attempt, the exact human step (URL, what to read, which record it
    changes) and the honest public state.

**W3b. Master transaction CLOSE-2: corrections that need an original** (Appendix A, CR-01…CR-20 not done in W1).
Highest public risk first:
- CR-01: the Findex mobile-money misdescription.
- CR-02: Findex uncertainty.
- CR-05: IMF remittance estimates labelled as reported history.
- CR-07: SMP status.
- CR-08: NPL statement.
- CR-09: untraced inputs.
- Then the rest of Appendix A.
- Gates, PR, merge.

**W3c. Master transaction CLOSE-3: UNLOCK.** Nothing stays hidden out of inertia. Every withheld object either opens,
or keeps a reason that is true today, written in the Master.
- Unlock rules:
  - existing archetypes, tables and visual primitives only;
  - one object, one state: text, visual and record agree;
  - a subagent red-teams each unlock against the semantic firewall first;
  - any value CauseWay computes is labelled "computed by CauseWay from …".
- CR-03 (the false CLM-026 sentence) and CR-06 (payment-anatomy consistency) are corrected here, with U1 and U2.
- Items U1…U14 are in Appendix B. Each row of 19_PAYMENTS_DATA and 27_FINDEX_SUBGROUPS that stays unpublished must
  carry an explicit reason. Nothing is unpublished by default.
- Gates, PR, merge. Report: unlocked count by item; kept count, with reasons.

**W3d. Master transaction CLOSE-4: regulation and chronology** (Appendix C).
- Each instrument is read in the original, the Arabic scans included; read the page images if needed.
- Instruments go to 31_REFORMS_REGULATION and the /data/ regulatory group. Dated events go to 14_SYSTEM_CHRONOLOGY.
- Firewall: rule ≠ implementation ≠ operation. Event wording is neutral on the two authorities.
- Deduplicate the macro-financial chronology: one canonical rendering on /finance/ (folded), and a one-line pointer
  on /data/.
- Gates, PR, merge.

**Arabic rows inside factual transactions.**
- CLOSE-2 also applies AR-001, AR-042, AR-022, ED-034, ED-035, ED-036 and AR-NEW-001, each in its final form after
  the source check named in its condition column.
- CLOSE-3 applies AR-004 with U10.
- CLOSE-5 applies ED-037 with RD1.
- The exact-match check runs against the 2ddbfb61 text recorded in the register. If an earlier transaction in this
  brief changed the same cell, merge both changes and record the merge in PROGRESS.md.

**W3e. Master transaction CLOSE-5: Readings and Measurement Agenda** (Appendix D). Gates, PR, merge.

**W3f. Rebuild the open-items register as one live view.** Prepend "Live status at <SHA>". Every item has exactly
one state:
- **CLOSED**, with the evidence of closure.
- **HOSTING**:
  - REL-01 headers at the host;
  - OWN-03 public origin;
  - EAD-10 host measurement;
  - REL-04 release acceptance;
  - the phone check from Yemen;
  - deployment switch-on;
  - optional aggregate counts (D5).
- **FRONTIER**: a disclosed evidence limit with its verification card and its cadence. This covers FRN-*,
  unreachable EXT-*, REL-02 (reuse terms not assessed) and every W3 item that ended UNREACHABLE.
- **OWNER-OPTIONAL**:
  - OWN-09 (World Bank microdata written confirmation; it would unlock the 105 subgroup rows that need computation);
  - REL-03;
  - EAD-02's manual assistive-technology audit with a human screen-reader user: recommended before launch, never
    claimed.
- **DECIDED**:
  - D1–D13;
  - every REJECT in Appendix E;
  - OWN-06 (no reversed logo is needed; the logo is used on light surfaces only);
  - the Arabic review (applied per the register).
Fix stale rows by append-only correction; the older sections stay below as history. Add a gate: no state outside
this list, and nothing "PENDING" unless its state is HOSTING. Refresh the open-items field in
YFI_CURRENT_PROJECT_CONTEXT.json (via rebind_authority.py if it owns it). PR, merge.

W4 — Structure and visual design (Stage B). Do it after W3, on the final content.
Goal: a calm, formal, premium evidence site in both languages, measured against the best public data and evidence
publishers. The benchmark is their provenance, hierarchy and verification, never their branding. A reader must reach
a correct, bounded answer and its original source faster, with nothing governed lost (D13).

Team for W4 (multi-agent-m, hub and spoke):
- you are the design lead and the only writer;
- challengers (subagents) are:
  - an Arabic editorial typographer and RTL specialist;
  - an information designer and data-visualisation specialist;
  - an accessibility and front-end engineer;
  - three reader judges for G1 (see below).
Challengers test and report. They never write files.

**G0 — Baseline (read-only).**
- Serve dist/. Screenshot and measure every page family at 320, 390, 768 and 1440, AR and EN, in the default state and
  in the meaningful states:
  - menu open;
  - search with results, including a dated event;
  - source filter;
  - Compare verdicts (comparable / qualified / not comparable);
  - cite;
  - report an error;
  - disclosure open;
  - no-JS.
- Record per page: phone screens, H1 lines, TOC entries, ISO dates visible, font files, cold transfer, contrast
  failures, targets under 24 px, and horizontal overflow.
- Run a reader-job audit with six personas: an Arabic phone reader on low bandwidth; a journalist verifying a quoted
  number; a CBY or provider analyst; a World Bank/IMF researcher; a humanitarian programme analyst; an academic.
  For each, time and clicks to: the answer; its scope (universe, period, denominator); its limit; its original
  locator.
- Write the top 10 frictions with evidence (route, screenshot, measurement) to design/DESIGN_INTEGRATION_V2.md §G0.
- **Visual and diagram audit.** For every visual contract (36 today, plus the new ones from W3c: the rial line,
  RV-CWR-011, and the extended VIS-REMITTANCE-COST), record:
  - its state: values shown / withheld / "no values yet";
  - the route where it must appear, and whether it does appear there;
  - its text-description table;
  - its "what not to conclude" line;
  - how it renders in AR.
  Every withheld or "no values yet" visual gets a reason that is true today, or it is filled. Specifically:
  - VIS-FINDEX-RESILIENCE and VIS-FINDEX-FLOW-CHANNELS are table-only objects
    (NO_GOVERNED_CONTRACT__TABLE_ONLY), not visual contracts. Fill their tables from the U1 values (emergency funds;
    domestic remittances sent and received), mapping by label, never by code.
  - VIS-FINDEX-BARRIERS: check the API for the barrier items (FDP-004…009). If they are null for Yemen, it stays
    empty with that verified reason. If they are not null, fill it.
  - VIS-PAYMENT-ANATOMY follows U2 and U6.
  Fix any visual that must appear but does not.

**S — Structure rules** S1–S13 (Appendix F) and the navigation (D8, CR-S12), within the D13 preservation rule.
- Re-measure after S. Targets:
  - /ar/data/ from about 55 phone screens to ≤20;
  - /en/evidence/ from about 28 to ≤14;
  - every domain page −25% or better;
  - /measurement/ −40%.
- Every element ID and data-* hook survives: a moved element keeps its attributes, and a removed anchor is re-hosted
  on its replacement. Prove it with the preservation check against 2ddbfb61, listing deliberate changes only.
- Port from Mohammed Waleed's branch code/navbar-disclosures-integration, by hand on current main, credited to him in
  the CHANGELOG. Take only:
  - the Space-key handler on the menu control (a real keyboard bug), with its test;
  - the menu-close threshold at ≥900 px (it matches the desktop breakpoint), with its test;
  - viewport_acceptance.py: widths 900/960/1100, the headerOverflow check, /rights/, blur before Tab. Update the
    checkpoint's run count.
  Nothing else from that branch.
- Gates, PR, merge.

**T — Tools: elevate search, Compare, the source directory and error reporting.** All of it is progressive
enhancement, first-party JS, with no library or third-party service. Each tool works without JS at a basic level.
Test every claim in a real browser.
- **Search** (site-src/app.js, search_index.json, search_aliases.json).
  - Arabic normalisation (alef and hamza forms, taa marbuta/haa, alif maqsura/yaa, tatweel, diacritics), and
    Western/Arabic-Indic digit equivalence.
  - Aliases and synonyms from search_aliases.json, both directions (e.g. حوالات ↔ تحويلات ↔ remittances,
    CBY ↔ البنك المركزي).
  - Ranking: exact ID, then title, then summary, then body.
  - Every result shows its type, period and scope line, so a number is never shown bare.
  - Typed groups (questions, evidence, Readings, sources, dated events, measurement priorities).
  - Full keyboard use; ?q= state preserved across a language switch.
  - Zero-result help: suggestions, plus "search the other language".
  - Tests: an Arabic query set and an English query set, each with expected top results. Make them a gate.
- **Compare** (/evidence/compare/).
  - A shareable URL for any selection.
  - The verdict (comparable / qualified / not comparable) is explained in one sentence naming the differing
    dimension (unit, universe, period, geography, definition).
  - A printable and copyable summary that carries the verdict.
  - A mobile layout that keeps the verdict above the values.
  - Selection limits and errors in plain words.
- **Source directory** (/data/).
  - Facets for publisher, source type, year and the governed question used on, with live counts.
  - Sorting; state kept in the URL; ?source= and #source-ID open the right group (S1).
  - "Clear all".
  - A per-source "cited by" list linking to the records that use it.
- **Report an error: a proper, structured form, not a bare email link.**
  - Where: on the existing /contact/ page (no new route), as a section with id="report". Every record, figure and
    Reading carries "Report an error", which opens it pre-filled.
  - Fields:
    - page URL, record ID, section anchor, language, edition (all auto-filled, editable);
    - the value or sentence in question (pre-filled when launched from a figure);
    - error type: number / date or period / source or link / scope or definition / translation / accessibility /
      other;
    - what it should say, and the evidence for that (a URL or citation);
    - optional name and email for a reply;
    - a consent line pointing to /privacy/.
  - Accessible labels, inline validation and clear error messages. AR and EN copy goes Master-first (04_NAV_UX).
  - Transport now (static site, no server): on submit, build a structured report with a reference code (e.g.
    YFIE-ERR-<record>-<yyyymmdd-hhmm>) in a fixed "key: value" format. Then:
    - (1) open the mail client to office@causewaygrp.com with that subject and body;
    - (2) offer "Copy report" for webmail users.
    No-JS: a plain mailto link with the same field list as instructions.
  - Transport at hosting (prepared, off by default, a HOSTING item): an optional first-party POST endpoint on the
    host, with spam control (honeypot plus rate limit; no third-party CAPTCHA). Retention is stated in /privacy/
    Master-first on the day it is switched on.
  - Process: write docs/CORRECTIONS_PROCESS.md, linked from /corrections/. It covers:
    - triage (material or editorial) within a stated time;
    - the Master-first fix;
    - the public /corrections/ log entry, against the stable ID and edition;
    - a reply to the reporter if they gave an email.
  - Gates: every Report link carries its context parameters; the form pre-fills from them; the body format is stable
    (test); no third-party request.
- Gates for all the tools; PR, merge. Record the before/after behaviour in design/DESIGN_INTEGRATION_V2.md §T.

**G1 — Direction challenge.** Build three genuinely different compositions as isolated candidate CSS layers, not
recolours:
- (a) quiet official-statistical;
- (b) editorial-interpretive;
- (c) compact source-first.
Build each on four real pages: Home, /payments/, a dense record (CLM-001) and /data/, in AR 390 and EN 1440.
Same content, IDs and hooks.
- Three independent reader judges score each candidate 1–5 against the criteria:
  - (1) an Arabic first-time phone reader;
  - (2) a sceptical statistician-journalist;
  - (3) a World Bank/IMF data professional.
- Criteria:
  - the first-screen answer;
  - the scope and limit are recognised next to the number;
  - clicks to the original locator;
  - long-text readability (measure, rhythm, hierarchy);
  - Arabic typographic quality;
  - tool discoverability;
  - calm and formal tone;
  - performance cost;
  - implementation risk.
- You choose one and record it as DL-V2-001: scores, reasons, and what was rejected and why. Commit the three candidates'
  screenshots under design/evidence/v2/ and link them from the PR, so the owner can veto later.
- Build the candidate CSS layers outside the shipped stylesheet: in scratch, or under design/exploration/v2/ as
  lineage that is never shipped.
- Do not roll out more than one direction.

**G2 — Implement the chosen direction** in the real renderer.
- Where it lives: scripts/yfie/theme.py (the stylesheet source), and render.py/families.py only for a recorded
  DL-V2-xxx markup change.
- Do not edit dist/ or projections by hand. No parallel stylesheet left unintegrated. Remove superseded rules.
- **Typography.**
  - IBM Plex Sans and IBM Plex Sans Arabic only, self-hosted and subset by the existing pipeline. At most 4 font files
    per page.
  - Arabic body text is set larger than Latin (about +1–2 px) with line-height about 1.7–1.9; Latin about 1.5–1.6.
  - Measure: about 60–75 characters for Latin, about 50–70 for Arabic.
  - Arabic is never letter-spaced, never justified, and has no faux-bold.
  - Use tabular figures for numbers in tables, figures and record values.
  - The Arabic heading weight (600 now) may move to 700 only if G1 or rendering tests show a measured legibility gain
    within the font budget. Record it as a DL.
- **System.** A type scale; a 4/8-based spacing scale; a grid; and colour roles with text contrast ≥4.5:1 and UI
  contrast ≥3:1. Evidence states and Compare verdicts carry words or shape, never colour alone.
- **Heavy text** (the core design problem):
  - answer-first sections: the answer, its limit and its source line are visible at once;
  - a clear section rhythm, and a figure-plus-boundary pattern: "what not to conclude" always sits beside the number
    or chart;
  - key numbers carry their unit, universe and period in the same visual unit. A copied or screenshot number keeps its
    scope: test it;
  - progressive disclosure for depth, a sticky desktop TOC, and readable tables (caption; stacked rows or controlled
    scroll on phone; sticky header where useful);
  - a calm source and footnote apparatus.
- **Chrome.**
  - The masthead and navigation follow D8.
  - The currentness strip is one line on phone.
  - The footer holds the licence line (gated), the trust links and the footprint line (W4F).
  - The logo is canonical and unaltered, on light surfaces only.
- **States.** Visible focus everywhere. Hover, active, disabled, empty and error states for search, compare and
  filter. Reduced motion respected; motion only for state change.
- **Print.** Limits, sources, the page URL and the edition print. Navigation does not.
- **Never:**
  - hero photography, stock images or carousels;
  - animated counters, parallax or decorative gradients;
  - card walls, dashboard pastiche or third-party embeds;
  - imitation of any institution's identity.
- **Benchmarks, for quality only:**
  - World Bank Data indicator pages;
  - IMF Data;
  - OECD Data Explorer and OECD publications;
  - UK ONS statistical bulletins;
  - Eurostat Statistics Explained;
  - Our World in Data's citation and reuse apparatus;
  - the GOV.UK Design System's typography, spacing and accessibility patterns.

**G3 — Verify** (after W4F, so the footer line is included; actual runs only; PASS / FAIL / NOT RUN):
- before/after screenshot sets;
- the G0 metrics re-measured;
- accessibility:
  - automated checks (axe via Playwright if installable);
  - keyboard paths;
  - 320 px reflow; 200% and 400% zoom;
  - forced colours and reduced motion;
  - no-JS;
  - screen-reader structure (landmarks, headings, labels);
  - claim no conformance;
- RTL and bidi: dates, percentages, abbreviations, mixed-script source names;
- print preview, and the copy-a-number test;
- the performance budget: scripts/performance_budget.py only measures today. Add a threshold gate (/ar/data/
  ≤350 KB cold, ≤4 font files) with a negative control;
- the redundancy scan: list every passage of 40 words or more that repeats across pages. Each remaining repeat is
  either a deliberate canonical projection (recorded) or becomes a link under D13;
- all CONTRIBUTING §5 gates and negative controls.

**Records.**
- design/DESIGN_INTEGRATION_V2.md: G0 findings, decisions DL-V2-xxx, before/after metrics, and what became more true,
  easier, more complex, or removed.
- Regenerate design/02_TOKENS.json.
- Resolve or decide every open item in design/ESCALATIONS.md.
- PR(s), merge.

W4F — Environmental footprint (Stage B: order G2 → W4F → G3; specification in Appendix G). Gates, PR, merge.

W5 — Repository governance and housekeeping (no Master)
- **`.github/workflows/housekeeping.yml`** (the owner runs it; you never run it):
  - inputs:
    - dry_run (default true);
    - confirm, which must equal "I am the owner" for any real run;
    - checkpoint_sha (default 2ddbfb611bb139d9597aec9b6b79153699cc4d94);
    - checkpoint_tag (default checkpoint/2026-10-10-content-complete);
    - hosting_ready_sha (required; the owner enters it, so there is no default).
  - permissions: `contents: write` only.
  - steps:
    1. create the annotated checkpoint tag, and `checkpoint/<date>-hosting-ready` at hosting_ready_sha. Never move a
       tag; fail if a tag exists at another SHA.
    2. create annotated archive tags `archive/<branch>` at the head of each unmerged branch:
       - claude/public-naming-terminology-part-b;
       - code/final-content-chronology-and-gates;
       - code/navbar-disclosures-integration.
       safety/pr11-pre-b1b2-2026-10-04 is already an ancestor of main. Tag it `archive/` for lineage, then delete it
       with the merged branches.
    3. delete every branch that is an ancestor of origin/main, plus each archived branch whose tag points at its head.
       Never main. Print each SHA first.
    4. write a job summary.
  - Add a test asserting: dry_run defaults true; the confirm phrase is required; main is never a target; no --force
    and no tag move.
  - Note: the checkpoint tag cited in README does not exist yet. Until the workflow has run, say "created by the
    owner-run Housekeeping workflow".
- **Before archiving:** copy audit/public_naming/PUBLIC_NAMING_LOG.md and RIGHTS_PRESENTATION.md from
  claude/public-naming-terminology-part-b into audit/naming/lineage/, with a provenance header. This is lineage worth
  keeping.
- **`.github/workflows/currentness.yml`:** monthly plus manual. It re-checks every source's locator and the watch
  list in W3a, and opens ONE issue listing what changed. It never edits.
- **`docs/REPOSITORY_SETTINGS.md`:** the owner's settings checklist, with exact UI paths:
  - a main ruleset: require a PR; require the 9 CI checks by name; block force pushes and deletion;
  - a tag ruleset for checkpoint/* and archive/*: block deletion and update;
  - automatically delete head branches;
  - read-only default workflow permissions.
- **New files:** SECURITY.md (how to report; no security guarantees claimed), CITATION.cff (for the content) and
  LICENSE-CODE (D3).
- **deploy.yml:** add a refusal step if the deploying SHA does not descend from the `*-hosting-ready` tag. Do not
  refuse on pre_release: the runbook deploys while pre_release is true and clears it at step 13. Document it in the
  runbook.
- currentness.yml needs `issues: write`.
- **Stale docs** (append or fix; delete nothing; never prepend to an audit record):
  - append a dated HISTORICAL_LINEAGE closing note to these .md files. The .json files take no note: classify them
    as lineage in the manifest and docs/REPOSITORY_MAP.md:
    - S0x closures, SESSION_*.md, REVIEW_LEDGER.json, S01_ARCHIVE_DISPOSITION_REGISTER.json;
    - POST_BUILD_REVIEW_PROGRAM.md (adjust validate.py:292 so it still reads it);
    - FINAL_RELEASE_VERIFICATION.md, S02_AUDIENCE_JOURNEYS_AND_IA.md;
    - HANDOFF_STATE.json, PROGRESS_INVENTORY.json, REPOSITORY_BUILD_SUMMARY.json.
  - docs/HANDOVER_TO_DEVELOPER.md §9: replace the manual branch list with "run the Housekeeping workflow", and fix
    lines 124 and 349.
  - OPENAI_REENTRY_CHECKPOINT.md: "21 of 21 unit tests" → the true count; clarify the 290/292 line; the PR range runs
    to the last merged PR.
  - Root names (FINAL_*, OPENAI_*) are kept, because validators and audit records hard-code them. Add a one-line
    "current front door" header to each.
- Classify every new file in the manifest. PR, merge.

W6 — README, README.ar.md, diagrams and cleanliness
- **README.md** (GOV.UK plain style: sentence case, "and"; the terminology register for names). It describes the
  stable system and never tracks PRs or sessions. Sections:
  1. identity and a status table: programme state, the checkpoint tag, the Master and Page Specs SHA-256 (validators
     read them), "not deployed", licences per D3. Keep the phrases "single production repository" and "sole
     semantic" (validate.py checks them). No main SHA: it changes on every merge;
  2. **One number, traced**: a Mermaid trace of 11.9% (CLM-001). It runs governed question → domain answer →
     Evidence Record → Passport → original source with locator, and ends with what the page says it does not
     establish. If CR-01 closed as confirmed, it includes that fact: in Yemen's study the mobile-money questions were not asked;
  3. the rules that make it trustworthy: the semantic firewall as a two-column table, one Master, Master-first
     corrections, bilingual co-authority;
  4. how a change reaches the public: a Mermaid flowchart naming every gate and the current negative-control count;
  5. the reader's journey, Understand → Explore → Verify, mapped to the five hubs and eight domains;
  6. what is inside: counts generated or gate-checked, never typed;
  7. a Mermaid repository map, with "edit / never hand-edit" classes;
  8. build and verify locally:
     - Python 3.11 required;
     - pip install -r requirements.txt;
     - playwright install chromium;
     - npm ci;
     - npm run verify, with expected outputs;
  9. contributing, corrections, citing (CITATION.cff), security and licences;
  10. a "Production and release boundary" section: verification is not release approval; deploy is owner-gated;
      downloads are off; release is the owner's decision;
  11. what remains: hosting only, with links to the runbook and the live register.
  Design: describe the implemented design system in one short section, linking design/DESIGN_INTEGRATION_V2.md and
  the footprint method (Appendix G).
- **Harvest from Mohammed Waleed's README draft** (branch code/navbar-disclosures-integration). Credit him in the
  CHANGELOG. Take these elements, updated to current facts and names:
  - the "What it is, and what it is not" paragraph (not a dashboard, regulator, statistical authority, provider
    directory, reform tracker, research blog or marketing site);
  - the ten-line distinctions list, including "the observation date is not the publication date", "disagreement is
    not automatically an error" and "bounded evidence stays bounded";
  - the "Production and release boundary" section;
  - the authority-layers table (Layer → Role) and the repository map table ("why a recipient goes there");
  - the engineering workflow block (pip install, playwright install chromium, npm ci, npm run verify, build, serve
    on port 4173), plus what `npm run verify` checks;
  - the "Engineering invariants" paragraph, and the Verify CI badge.
  Drop its stale parts: DESIGN HANDOFF READY, old hashes, "licence text not yet confirmed", and old labels ("Evidence
  Readings", "Data & sources", "Rights & reuse").
- **README.ar.md:** the same content written as Arabic, with Arabic diagram labels. The two files link to each
  other. An independent Arabic-editor subagent judges it as Arabic.
- **Diagrams and gates:**
  - Regenerate every diagram with scripts/architecture_diagrams.py. Find any diagram elsewhere showing retired
    labels or counts and regenerate it.
  - Python 3.11 fail-fast preflight in scripts/build.py and scripts/validate.py: one clear line on how to install
    3.11.
  - A README gate: every inventory count in both READMEs (pages, records, claims, passports, Readings, priorities,
    visuals, sources, locators, search records) equals the inventory, and the stated hashes match. Mermaid blocks
    pass a structural check (balanced fences, a known diagram type, no empty nodes), or @mermaid-js/mermaid-cli if
    it installs. Add one negative control.
- **Cleanliness sweep:**
  - caches, ZIPs, scratch files, screenshots outside design/evidence, credentials and tokens, *.dta or any respondent
    file. Any hit is a BLOCKER: run `git rm --cached` and add a .gitignore rule; do not rewrite history.
  - Write docs/REPOSITORY_MAP.md: live versus history, and where to start. Link it from both READMEs.
- **Cold-reader test:** a fresh subagent reads only README.md and answers five questions:
  - what is this;
  - why trust 11.9%, and what it does not include;
  - where the authority is;
  - how to fix a wrong number;
  - what is not done.
  Repeat in Arabic with README.ar.md. All answers must be correct.
- PR, merge.

W6S — Search visibility and metadata (SEO), Stage C. Prepare everything; switch indexing on only at hosting.
- **Per page, in EN and AR (Master-first where it is copy):**
  - a unique `<title>`, targeting ≤60 characters. Drop the site suffix on long titles rather than rewriting governed
    titles. The existing F6 gates (validate.py, F6-G01…G04) already cover titles, descriptions, canonical, hreflang
    and the sitemap: extend them; do not duplicate them;
  - a meta description of ≤155 characters stating the page's answer, with no number that lacks its scope;
  - one H1;
  - a logical heading order;
  - `lang` and `dir` on `<html>`.
- **Language and duplication:**
  - reciprocal hreflang links for en and ar, plus x-default;
  - a self-referencing canonical, emitted as absolute URLs once public_origin is set. Until then the build emits
    them relative, or omits them by a single switch, and a test proves the switch.
  - retired addresses (e.g. NEG-EW-011) keep noindex and point to their successor.
- **Crawling:**
  - sitemap.xml with both languages and lastmod from the edition date;
  - robots.txt.
  Both are generated now and gated behind public_origin; noindex stays until hosting, which is a HOSTING item.
- **Structured data (JSON-LD), only what is true.** F6-G04 currently forbids Organization, author and date, and
  allows BreadcrumbList only where a breadcrumb shows.
  - Extending it is a deliberate gate change under §0, with reasons and a negative control.
  - Proposed extension: WebSite with a SearchAction; Organization (CauseWay, as on /about/); BreadcrumbList where a
    breadcrumb shows; Article for Readings, with author CauseWay and dates from the Master.
  - If any of these cannot be made true from the Master, leave it out.
  Do not mark evidence records as Dataset (no distribution is offered; D4).
- **Social and performance:** Open Graph and Twitter cards on every page (the social images exist; check AR
  rendering). Use Core Web Vitals proxies from the performance budget.
- **Gates:** every page has a unique title and description; hreflang pairs are reciprocal; JSON-LD parses and
  validates against schema.org types; no indexable page lacks a canonical once public_origin is set.
- **At hosting (runbook):** verify Google Search Console and Bing Webmaster for the origin, submit the sitemap, and
  remove noindex in the same deploy that sets public_origin.
- PR, merge.

W7 — Editorial and red-team pass on everything this brief changed
- **English:** an independent English-editor subagent reads every changed or new EN string. It checks plain
  institutional English and no overclaim.
- **Arabic:** an independent Arabic economic editor subagent reads every changed or new AR string as Arabic first,
  then against EN for meaning, numbers and limits. It checks register, agreement, one term per concept and the
  neutral naming of the two central banks.
- **Red team:** a hostile-but-fair subagent attacks the changed pages in sequence as:
  - a Yemeni citizen;
  - a journalist;
  - a CBY regulator;
  - a bank;
  - an MFB;
  - a payment provider;
  - an exchange company;
  - a researcher;
  - a World Bank/IMF professional;
  - a humanitarian actor;
  - a donor;
  - a source owner.
  It reports only what is wrong; you fix it Master-first.
- **Arabic house-style conformance**, across every public AR string, not only changed ones (audit/naming/
  ARABIC_HOUSE_STYLE.md).
  - Run a scripted lint for:
    - ISO dates in prose;
    - bare «التحويلات» meaning remittances;
    - internal status words (HOLD, CONTRACT, PENDING) in public text;
    - «في المئة» used for differences between shares (it must be «نقطة مئوية»);
    - inconsistent self-reference («هذا المورد» / «المنصة»);
    - «قائمة» and «كشف» mixed for the same object.
  - Fix confirmed hits Master-first. Make the mechanical rules (ISO in prose, internal status words) permanent gates
    with negative controls.
- **Records:**
  - finalise audit/close_out/KEY_MIGRATION.csv;
  - write audit/close_out/NEW_ARABIC_SINCE_2ddbfb61.csv: every AR string this brief added or changed, with its key,
    its EN pair and the editor's verdict;
  - the advisor reviews this list after the run.
- PR, merge.

W8 — Acceptance package and final verification
- **On the final main:**
  - all CONTRIBUTING §5 gates and every negative control caught;
  - the accessibility audit (record only) and the performance budget;
  - preservation against 2ddbfb61 (deliberate changes listed);
  - every count consistent across README, README.ar, the checkpoint, Context, the manifest, the register and the
    Master.
- **Reader-path checks** (from the Arabic review contract), on the final build, in AR and EN, at 390 and 1440 px and at
  200% zoom:
  - value → record → original source → back, switching language without losing place;
  - copy a number and its scope; print a record;
  - "unknown — does not mean zero" states;
  - bidi of dates and abbreviations;
  - keyboard focus order.
  Report actual results only.
- **Final QA:** run Appendix I item by item. Record PASS / FAIL / NOT RUN with evidence (command, screenshot or
  route) in audit/close_out/QA_CHECKLIST.md. Fix every FAIL that is in scope before the final reply.
- Set the edition date to the final content edition, and "Sources checked up to" to the date of the last original
  actually re-read, Master-first in EN and AR (CR-17).
- Report the final main SHA. The owner enters it as hosting_ready_sha when running Housekeeping. Name the
  acceptance package after the commit it was built from. Commit docs/ACCEPTANCE_PACKAGE.md before building it.
- **Build `YFIE_ACCEPTANCE_PACKAGE_<sha>.zip` in scratch and give it to the owner. It contains:**
  - both READMEs;
  - the live register;
  - the checkpoint and Context;
  - CHANGELOG entries since 26 September;
  - OWNER_DECISIONS for 2–10 October;
  - the naming decisions;
  - the legacy before/after record;
  - PROGRESS.md, KEY_MIGRATION.csv and NEW_ARABIC_SINCE_2ddbfb61.csv;
  - a gate run log;
  - design/DESIGN_INTEGRATION_V2.md and the before/after screenshot index;
  - REVIEWER_BRIEF.md: what to accept, how to verify, the firewall, and what is out of scope (hosting).
- Add docs/ACCEPTANCE_PACKAGE.md: an index of those files by path and SHA.

FINAL REPLY (≤50 lines):
- every PR and merge SHA;
- tables:
  - Appendix A: finding → CLOSED / FRONTIER, with the locator;
  - unlocks: unlocked / kept, with counts;
  - regulation: added / UNREACHABLE;
  - structure and design: before → after screens per page type, and DL-V2-001 with the G1 scores;
  - the Arabic register: applied / stopped on mismatch / conditional outcome per row;
  - footprint: per-page transfer and estimate for 5 representative pages, and the runtime parity test;
- the register's live counts by state, showing only HOSTING open;
- the cold-reader results;
- cleanliness, BLOCKERs first;
- the owner's exact steps:
  1. run Housekeeping (dry run, then real);
  2. apply REPOSITORY_SETTINGS.md;
  3. send the advisor the final main SHA, the acceptance package and NEW_ARABIC_SINCE_2ddbfb61.csv for the
     post-run verification;
  4. hosting, per the runbook;
  5. send the acceptance package to OpenAI;
  6. archive this session.
Final line: "CLAUDE MATURATION HAND-BACK READY — ONLY HOSTING REMAINS".

══════════════════════════════════════════════════════════════════════
APPENDIX A — TRUTH FINDINGS (verify each in the original; fix Master-first, EN and AR)
══════════════════════════════════════════════════════════════════════

CR-01 MATERIAL. 11.9% is described as including mobile money.
- Where: Home, /people/, /evidence/CLM-001/, VIS-FINDEX-GAPS and /evidence/compare/ describe 11.9% as adults with
  an account "at a financial institution or with a mobile-money provider". CLM-001's limitations add that personal
  use of a mobile-money service counts.
- Finding: in Yemen's 2021 Findex study the mobile-money questions were not administered.
  - The World Bank's open data show fiaccount.t.d = account.t.d = 11.9, and mobileaccount.t.d null.
  - The public DDI variable pages (microdata.worldbank.org/catalog/5862) show the fin13 items with no valid cases.
- Fix:
  - keep the World Bank's definition, and add that in Yemen the figure reflects financial-institution accounts,
    because the mobile-money questions were not asked;
  - add a change trigger to CLM-001 and MA-001: a later survey that asks them may show a jump caused by the
    instrument, not by real change;
  - check every other place that pairs 11.9% with wallets.

CR-02 MATERIAL. Findex uncertainty.
- Where: the site says the World Bank "publishes no standard error or confidence interval", and prints a derived
  margin of about 2.2 points that ignores clustering.
- Finding: the Findex 2021 methodology appendix is reported to publish a Yemen margin of error, about 4.3 points,
  with a design effect.
  - The World Bank's DDI entry for the Yemen study (YEM_2022_FINDEX_v01_M; Microdata Library) supports this. It
    describes a clustered, stratified face-to-face design (primary sampling units, random route, gender-matched
    interviewers, n = 1,000). It also says country-specific margins of error are in the Methodology table of the
    Global Findex 2021 report.
- Fix:
  - read the appendix. If it is confirmed, cite the publisher's figure and correct the sentence. Then
    either re-state the published derived intervals (CLM-002, CLM-026, /people/) by applying the publisher's design
    effect to the already-published estimates, labelled "computed by CauseWay", or withdraw them. Never recompute
    from microdata;
  - if it is not confirmed, record the check.

CR-03 MATERIAL. A false sentence in CLM-026.
- Where: CLM-026 says 29 of its 32 measures have "no published value for this wave".
- Finding: 13 have World Bank published values for the same wave (see U1).
- Fix: correct it (done in W1).

CR-04. Wrong locators: WB-FINDEX-OBS-2022-010/011/012 (W1).

CR-05 MATERIAL. IMF remittance estimates are presented as reported history.
- Where: 23_REMITTANCES, CLM-007 and VIS-REMITTANCE-MACRO call the IMF 2018–2024 personal transfers "reported
  history", with geography "Yemen".
- Finding: IMF CR 26/80, Annex IV, reportedly describes a staff estimate from a demographic and behavioural model,
  scoped to IRG-controlled areas.
- Fix: read Annex IV. Relabel as staff-estimated (observed ≠ estimated), with the scope as stated.

CR-06. Text and visual disagree on 5,202,019.
- Where: the figure is public in text (CLM-010, /payments/, /reforms/, /providers/, /evidence/compare/), with its
  caveat. VIS-PAYMENT-ANATOMY withholds it as OBS-00037.
- Fix:
  - unlock it in the visual with the same caveat: no published definition; accounts, not people;
  - keep OBS-00036 (POS H1, 58,512) held until the January–February 2025 releases confirm the period, and record
    that reason.

CR-07. A stale SMP status.
- Where: /finance/ and /data/ say "staff-level agreement of July 2026, subject to Management approval".
- Fix: read the IMF primary release (about 7 October 2026) and update. If no primary release is found, keep the
  wording and record the check.

CR-08. NPL ratios.
- Where: /finance/ says no harmonised set of NPL ratios exists.
- Finding: IMF CR 26/80, Table 5, prints sector NPL ratios of about 55–61% for 2020–August 2025, and 0.0 for 2014–19.
- Fix: read it and state what the IMF publishes and its scope. Treat the 0.0 values as not reported
  (missing ≠ zero). No bank is named.

CR-09. Untraced inputs.
- Where: CLM-039, CLM-046 and CLM-056 say some inputs "have not yet been linked to a specific original source".
- Fix: trace each one, or remove the untraced figure. Then check CLM-056's naming of a provider's share against D10.

CR-10. The NFID procurement source goes NON_PUBLIC (W1).

CR-11. DS-QUAL-EVIDENCE binds SRC-CCY-PRESSURE-2026.
- Finding: its publisher is not established. A public copy exists at calpnetwork.org ("Economic Impact of Iran-US
  War on Yemen", May 2026).
- Fix:
  - publisher established in the document → public locator;
  - otherwise unbind it, consistent with LA-A DIV-04.

CR-12. Quarantine the OECD benchmark rows and the illustrative codebook rows (W1).

CR-13. A sex-composition label conflict in the H1-2025 shares.
- Where: 19_PAYMENTS_DATA assigns 81/18/1 to e-wallet subscribers and 84/16 to bank accounts.
- Finding: the legacy records give 81/18/1 to bank accounts, and "1% companies" fits accounts.
- Fix: re-read SRC-CBY-PAYREPORT-H1-2025 p.1 and fix the Master before any use (U6).

CR-14. Wording of the low-income comparator.
- Where: the site shows 35.2%, computed by CauseWay from 19 economies.
- Finding: World Bank documents give 31% (2021) and 33% (2024).
- Fix: label the value as computed by CauseWay, or use the World Bank's published figure. Never call a computed
  value "the World Bank's figure".

CR-15. Is the CBY still producing remittance data?
- Finding: the Yemen Economic Monitor, Spring 2026, reportedly says the CBY "has discontinued remittance data
  production", while the product uses CBY AR2025's 2025 value.
- Fix: read the full report and reconcile the wording.

CR-16. OECD/INFE Yemen scores 15 and 42 are chart-read values. Re-read Figures 2.1 and 4.1 once and record it.

CR-17. Stale edition labels.
- Where: every page says "Edition of 3 October 2026" (CWR-011 carries 10 October data).
- Fix: in W8.

CR-18. Rurality holds get a permanent reason (W1).

CR-19. The CLM-056 provider share under D10. Keep it only if the 91% figure is in a primary public source;
otherwise describe the provider without naming it.

CR-20. The deposit-insurance law number.
- Where: held in 33_ANALYTICS_MASTER as "21 vs 40".
- Finding: a 2008 announcement reportedly gives Law No. 21 of 2008.
- Fix: read the original. Close the hold, or keep it with the attempt recorded.

══════════════════════════════════════════════════════════════════════
APPENDIX B — UNLOCKS (W3c)
══════════════════════════════════════════════════════════════════════

U1. Findex 2021 published values (World Bank Global Findex source 28, open API).
- Fill the 51 contract rows of 27_FINDEX_SUBGROUPS that the World Bank publishes for Yemen. These are FDP-002, 014,
  015, 017, 018, 019, 021, 026, 027 and 028 by sex, age, education, income and workforce, and FDP-001 by workforce.
- Add the 13 national values CLM-026 lacks:
  - FDP-011 (fin17a, 3.1);
  - FDP-013 (fin22a, 1.8);
  - FDP-020 (fin37, 3.8);
  - FDP-032 (merchant.pay, 0.6);
  - the remaining FDP rows the API returns.
- Map by indicator label, never by code: the microdata codes fin26/fin28 do not match the open codes.
- The locator is each series URL.
- Period wording copies CLM-001: World Bank Data labels the year 2022; the study is the Yemen Global Findex 2021,
  fielded 7 November 2022 to 9 January 2023.
- Each subgroup value carries:
  - "no interval published here" (EXT-07 stays held);
  - smaller subgroup samples;
  - no cause (CAUSE_HELD).
- A gap between two published values may be shown as arithmetic, with no claim of significance.
- Show the values in the existing /people/ subgroup table and the CLM-026 panel.
- The 105 rows the World Bank does not publish stay "contract only", with the reason "requires computation from
  licensed microdata (OWN-09)".
- Gate: commit a dated snapshot of the API responses (audit/close_out/fixtures/findex_api_<date>.json). The gate
  compares the Master to the snapshot, never to the live API. currentness.yml refreshes the snapshot and flags any
  drift.

U2. OBS-00037 in VIS-PAYMENT-ANATOMY (CR-06).

U3. Cash Consortium of Yemen sources.
- Promote to public locators, after confirming the title and document match:
  - CCY-SAM-2024: calpnetwork.org …/2024/11/SAM_Multiplie-Effect-of-Cash-Study.pdf;
  - CCY-CASH-DURATION-2026: calpnetwork.org …/gf-uploads/2026/06/Cash-Duration-Report_CCY_2026.06.22.pdf;
  - CCY-ISP-2024: ReliefWeb, "The Unseen Assistance";
  - CCY-PRESSURE-2026: only per CR-11.
- CCY-REMIT-ESTIMATE-2025 and CCY-AMAL-2025 have no public copy: they stay non-public (CLM-044 stays withheld).
- Then strengthen CWR-010 with two findings, each with its sample, place and design limits stated:
  - Cash Duration: longer assistance protects consumption but does not build savings (274 households; 6 vs
    3 months; no unassisted control);
  - last-mile cash-out constraints from the public reports.

U4. CBY monetary context (18_CBY_MONETARY; source SRC-CBY-001, public).
- **On /finance/:** one dated table of at most 8 indicators:
  - the Aden market rate, YER/USD (May 2026 and May 2025);
  - M2;
  - currency in circulation as a share of M2;
  - FX deposits as a share of total deposits;
  - bank total assets;
  - foreign assets;
  - private credit;
  - claims on government.
  Show end-2025 and the latest month, updated to Issue 55/56 if W3a finds them. Write "computed by CauseWay" where
  a ratio is derived.
- **Governed visual of the monthly rate** (113 months, January 2017 → latest), using the existing monthly-line
  primitive:
  - the label says it is the CBY-Aden published average market rate, not the Sana'a or street rate;
  - the August 2025 move is annotated, not smoothed;
  - no inference that the rate was "held" or "administered".
- **CWR-002:** add the 2025 episode. YER balance-sheet values fell as the rial strengthened, "consistent with
  revaluation; the two effects cannot be separated".
- **VIS-POS-VALUE caption:** the window spans the June–August 2025 rate move, and values are nominal YER.
- **Firewall line:** monetary aggregates describe the banking system, not people's access or use. The bulletin does
  not state its territorial coverage.

U5. RV-CWR-011: a bank-composition visual for CWR-011, using the same primitive as RV-CWR-002 and the bound
CBY-BANKS records. Add /finance/ to CWR-011's domain surfaces.

U6. Held payment observations (19_PAYMENTS_DATA).
- Publish into VIS-PAYMENT-ANATOMY the 2024 Q3 channel values: ATM, cheques, local SWIFT and POS. The cheque
  universe covers named CBY branches only. Values are not people.
- After CR-13, publish the H1-2025 composition shares as "shares of accounts / subscribers / cards, not of people".
  Show them in CWR-007 as a limitation, never as a gender-gap estimate.
- ATM governorate shares: publish them as "share of ATMs reported by CBY-Aden" only if the source states the
  perimeter and that "Sana'a" means the governorate. Otherwise keep them, with that reason.
- Keep the 2024 POS value series held: the Q1 figure is 31m against 1,642m in Q2, unexplained. Record the reason.
- Every row that stays unpublished gets an explicit reason.

U7. Remittance cost.
- Extend the existing VIS-REMITTANCE-COST (no new contract) with the World Bank series SI.RMT.COST.IB.ZS, the
  average cost of sending remittances to Yemen. Values read on 10 October: 2016 4.68, 2017 5.71, 2022 3.46,
  2023 2.81. Re-fetch, and use the fetched values.
- Add the UN SDG 10.c.1 metadata (target 3%; corridors above 5% to be eliminated) as a reference line in the
  caption. No pass/fail colouring.
- Say that this measures the price of sending, not last-mile or household cost.
- Update RPW to the latest quarter.
- This closes FRN-09.

U8. IMF Financial Access Survey (via WDI; values read on 10 October; re-fetch). Last Yemen year 2015: ATMs 5.81 and branches 1.48 per 100,000 adults;
depositors 103.1 per 1,000 adults. Add these as dated historical context in MA-005's current evidence, noting that
the series stopped in 2015 and the population denominators are the IMF's.

U9. FMIIP PAD additions (SRC-WB-FMIIP-P180708, public; read each paragraph).
- **¶10:** firm access to a bank branch in 2018 (a 141-firm survey), as a dated limitation on /firms/ or CWR-008.
- **¶7:** money-exchanger branches 876 → 3,244 (2017–19). Add a /evidence/compare/ case: IGC (YEM-24338 §3.1/3.4)
  labels the same pair as entities, including MFIs.
- **¶7:** "19 operating banks, 4 of them microfinance banks", shown on /providers/ as a dated third-party statement
  beside the CBY-Aden list (26) and IGC (31). Listed ≠ operating.
- **The PAD's statement on beneficiaries travelling more than 10 km** (if bound to the programme population): add it
  to /access/.
- **The FPS design:** it excludes walk-in/OTC users until a National Risk Assessment, and requires registered
  clients. Add this to CLM-018 / /payments/; design ≠ operation.
- **Access-point universes:** IBS 2019 (agents and acceptance points of 5 providers) against FMIIP January 2025
  (817 points). Add it as a compare case only after checking the reported coincidence with the Aide Memoire
  payment-site total.

U10. Women's evidence concordance (CWR-007).
- World Bank FSD 2024 (held, SRC-WB-FSD-2024-001), p.25: the "1% of women" statement, and the "99% unbanked"
  statement if found. Add them as statements, not measurements.
- YMN 2021, Table 5: 34% female share of active microfinance borrowers (February 2021, 9 providers), as a dated panel
  figure.
- SMEPS 2024: 44% female-owned (programme ≠ national).
- ACAPS "Mahram practice" (14 December 2023) as support for a named hypothesis only.

U11. CWR-001 compare case. Remittances as a share of output for 2024 are about 38.6% (YEM Spring 2025) and about
25% (YEM Spring 2026): the same year, a different basis.
- Read both editions in English.
- The Arabic Spring 2025 edition is World Bank document IDU-7e9c81f8-af50-45f0-b454-e73ae077727e (June 2025).
  Cite it only for Arabic wording.

U12. UCT status (CWR-010, CLM-045):
- no payment cycle since January 2025;
- ESPECRP closes 31 December 2026;
- successor P514855 signed 2 September 2026.
Verify each in the ISR and the project page.

U13. MICS 2022–23 (UNICEF/CSO): all governorates and no financial questions. Note it in MA-001 as the cheapest
delivery vehicle for a finance module.

U14 (conditional). The World Bank Yemen phone survey "Monitoring Food Insecurity and Employment", round 1
(August–September 2022, adults 18+, about 1,297 respondents).
- It records the area of control (IRG and DFA) and ranks household income sources, including international and
  national remittances and humanitarian cash transfers.
- If a public catalogue entry or published results exist, add it as a source card, and note it in MA-001 and MA-009
  as an existing instrument that covers both areas.
- Do not compute figures from its microdata.
- If there is no public entry, record nothing public.

══════════════════════════════════════════════════════════════════════
APPENDIX C — REGULATION AND CHRONOLOGY (W3d; read each in the original)
══════════════════════════════════════════════════════════════════════
Start from audit/FINAL_CURRENTNESS_CUTOFF.md (the nine documents not held) and close it. Candidate items, with their
known locators:
- CBY central defaulters registry launch, 5 August 2026 (cby-ye.com/news/963). Launch ≠ coverage. It also gives a
  locator to passport EP-CBY-CREDIT-INFO-SPINE-K04.
- Credit-risk information instruments: Decision 4 of 1991; the circulars of 6 October 2021 (cby-ye.com/publications
  /149 and /150; verify).
- Governor's Decision No. 7 of 2026: an 18% minimum on new rial savings, effective 12 April 2026
  (cby-ye.com/files/69dcac86e3520.pdf).
- Also locate the missing 2026 decisions No. 8, 12 and 16.
- e-KYC instructions, 18 December 2023 (cby-ye.com/files/65806fe2b3757.pdf).
- Board resolutions:
  - 2/11/2022, separating exchange and microfinance-bank ownership;
  - 3/11/2023, on MFB capital;
  - the capital reset of 23 March 2022.
  Sources: cby-ye.com/files/623ad771a78d7.pdf and 659aa2ee5852b.pdf (scans). This feeds CWR-006: a licence
  conversion can be reclassification, not inclusion.
- Circulars 2, 3 and 4 of 2025 and Circular 1 of 2026 (cby-ye.com/files/68dcd80cd12b9, 690e0e07d4981, 690e0e39ce5d9,
  6aaa38b226baa).
- The payment-rail sequence:
  - national switch phase 1, 7 March 2024 (news/645);
  - Board, 28 March 2024 (news/656);
  - the Buna connection, 14 September 2023 (news/579).
- The 2025 exchange-sector enforcement wave, 23 July–6 August 2025, as dated events with counts only, no names.
- The February 2026 exchange-rate pricing decision (SAR repricing, 13 February 2026), from the bulletin appendix or
  the CBY original.
- Governor's Decision 6 of 2025: the Deposit Insurance Institution, 20 July 2025.
- July 2024: licence revocations and the de-escalation of 23 July 2024 (UN Special Envoy statement), as a neutral
  event entry.
Any item not found or unreadable becomes a FRONTIER card with the dated attempt.

══════════════════════════════════════════════════════════════════════
APPENDIX D — READINGS AND MEASUREMENT AGENDA (W3e)
══════════════════════════════════════════════════════════════════════

RD1. CWR-011 becomes a full Reading:
- U5 visual;
- /finance/ surface;
- related to CWR-002, and CWR-002 related back;
- MA-008 binding;
- the latest bulletin, with at least two month-ends;
- the alternatives kept: weak demand, the treasury-bill legacy, valuation, perimeter, and asset quality from CR-08.

RD2. A "use" section (the existing section_id) on the 9 Readings that lack one. It answers: what a regulator, donor
or provider should check before relying on the number or the claim. It is non-prescriptive.

RD3. CWR-005: bridge to the 2024–26 e-wallet record already held, keeping historical and current separate.

RD4. CWR-008: SMEPS 2025 and ESCWA 2025, if W3a finds them, plus U9 ¶10.

RD5. CWR-010: U3 and U12, and the Cash for Nutrition PAD if relevant.

RD6. CWR-003 and CWR-009: the POS months after June 2026; FMIIP ISR sequence 3.

RD7. CWR-001: U11, and any new SMP remittance vintage.

RD8. CWR-012 (conditional): "How money reaches households" — the system lens for QE-007, which today has only a
measurement Reading.
- **Evidence:**
  - Findex domestic remittances sent 17.7% and received 31.9%, with subgroups (U1);
  - the cost series and RPW (U7);
  - the CBY remittance vintages (CWR-001);
  - exchanger counts (U9);
  - the CCY Unseen Assistance and SAM reports (U3).
- **Hypotheses:** remittances and informal transfers are a main liquidity channel for households, routed through
  exchange companies rather than accounts. Stated as hypotheses.
- **Alternatives named:** survey coverage; humanitarian cash; currency; definitions of "remittance".
- **It ends with** what would confirm or overturn it.
- **Conditions:** every number bound; the Arabic written and reviewed to a native economic editor's standard;
  firewall-clean. Drop it, with a note, if any condition fails.
- **Downstream:** Readings 11 → 12; Page Specs, search, sitemap, social image, README, checkpoint and Context
  rebind.

RD9. Link fixes:
- /measurement/ links CWR-001, CWR-002 and CWR-011;
- lift the two-link cap so each domain page links every measurement priority whose affected_route_list names it
  (/people/ MA-003 and MA-007; /reforms/ MA-008, MA-009 and MA-010; /payments/ MA-009 and MA-010);
- /methodology/ links VIS-EVIDENCE-CLASS-LADDER, VIS-EVIDENCE-FRESHNESS, VIS-SOURCE-COMPARISON and
  VIS-MECHANISM-METRIC-BRIDGE;
- CWR-007 gains an inbound link from a related Reading.

RD10. Answer-first openings for all 11 (or 12) Readings, EN and AR.
- The first paragraph states the Reading's finding and its main limit before the background.
- Use only facts already in the Reading. Add no claim and no cause.
- Where a register row already fixed the opening (AR-003, AR-004, AR-005, ED-037), keep the adjudicated wording
  verbatim. Only reorder whole sentences. Any other change is new Arabic, listed in NEW_ARABIC_SINCE_2ddbfb61.csv.
- Editor subagents propose; you approve; apply Master-first.
- Keep each Reading analytical and engaging: a question, a tension, a bounded answer. No rhetoric that outruns the
  evidence.

M1. Measurement Agenda: keep 10 priorities and add dimensions:
- MA-001:
  - household remittance module (receipt, channel, currency, frequency);
  - financial-capability outcomes;
  - collateral and shop or supplier credit;
  - the mobile-money module change trigger (CR-01);
  - MICS as vehicle (U13).
- MA-003: administrative-area coverage (both seats); digital literacy.
- MA-004 or MA-005: a microfinance provider panel and its reporting universe. QE-006 has no priority today.
- MA-005:
  - exchanger points and flows;
  - agent and till liquidity, denominations, withdrawal caps;
  - FAS historical (U8).
- MA-008: insolvency, and CWR-011 bound.
- MA-009: cash-out constraints.

M2. Record the scope of four items in the /methodology/ gap list: the ICT/telecom layer, insolvency, digital
literacy, and Yemen Post. Financial-inclusion diagnostics commonly cover them, but this resource does not measure
them. Each gets one line on why, and where it would be measured. Do not cite or name any procurement document
publicly (CR-10).

══════════════════════════════════════════════════════════════════════
APPENDIX E — REJECTED, with reasons (recorded as DECIDED; nothing here is pending)
══════════════════════════════════════════════════════════════════════
- **POS value in USD.** A rate choice would become a converter (ADD2-REJ-10).
- **The legacy reading that the rate plateau was "held/administered".** It infers a policy actor from data alone.
- **"Implied 80% dormant" and "targets below reported numbers".** Accounts ≠ people; the units do not match.
- **Enforcement names and sanctioned-entity names.** Naming policy.
- **A C3 contradiction-index page, a coverage matrix, a 39-gap register page, and FAQ/benchmark pages.** These need
  new routes and duplicate Compare, the evidence-gap visuals and the Agenda. The coverage matrix counts come from a
  14-source corpus. The benchmarks rest on unsourced comparators.
- **The five-systems material.** The food basket is out of scope; the remaining items are industry or modelled data,
  causal verdicts or names. Only the UCT and July 2024 items are taken (U12, Appendix C).
- **Doing Business 2020 "getting credit".** The series was discontinued over data integrity; MA-008 states that no
  current credit-infrastructure measure exists instead.
- **The FATF listing narrative, OFAC, Saudi transfer caps, and comparator countries (Somalia, Libya, Sudan, Syria).**
  Conflict-sensitivity risk, or non-Yemen facts with no inclusion evidence.
- **Unweighted raw shares from the 2026 syntheses and PDFs** (OTC remittances 19.0%, family borrowing 47.5%, and
  others). They are raw sample shares (CLM-024).
- **Rural/urban values.** The World Bank publishes none for Yemen (CR-18).
- **"50% without national ID" and "78% of Muhamasheen".** Unsourced.
- **Corridor origin shares (Saudi about 60%).** No period is stated; take them only if the YEM full text gives a
  period.
- **Workbook lead figures, and the legacy Humanitarian_Cash and Macro_Currency CSVs.** Unsourced or fabricated-
  looking.
- **CauseWay-internal inferences** (the "rate pin" test, the whole-of-Yemen IMF implied figure).
- **Insurance, postal savings and capital markets.** Scope.
- **Documents re-offered on 10 October:**
  - WBG Country Survey FY14 (a client-perception questionnaire): not evidence on financial inclusion.
  - "Impact of Yemeni crisis on efficiency of Yemeni banks" (SEBR 2025, DOI 10.48185/sebr.v6i1.1674): the venue is
    not established, and bank-efficiency scores are outside the product's questions.
  - The 2009/2010 Enterprise Survey questionnaires, screener, implementation note and indicator definitions: no
    results in them. Their sampling frames differ from the 2022 survey, so no trend may be drawn. The 2013 profile is
    already held as a citation card.
  - The Findex respondent files (CSV, DTA): never used by this brief (data hygiene).

══════════════════════════════════════════════════════════════════════
APPENDIX F — STRUCTURE RULES (W4). IDs and data-* hooks preserved; savings measured on the phone at 390 px.
══════════════════════════════════════════════════════════════════════

S1. Source groups closed by default.
- On /data/, the regulatory and supporting `details.grp` render closed (families.py:419, 426).
- JS opens the group that contains a match for the filter or facets, or a #source-ID / ?source= target.
- Update test_public_tools so the locator-only control is reached via ?source=. The assertion stays identical (steward
  approval for DEBT-011 is given here).
- Expected: /ar/data/ −33 screens.

S2. One rights statement per list.
- Keep the page-level reuse line.
- Move each card's rights line, its "Does not establish" line and its dependency details into one per-card
  disclosure, "About this source". Attributes are kept.
- Record pages use one shared rights line per source list.
- Files: families.source_row, render.source_card.

S3. Figure data tables behind a disclosure.
- "What the evidence shows" and "What not to conclude" stay visible beside every figure: detached use must never lose
  its limit.
- The data table goes in `<details>` ("Show the data table"). It stays in print and in screen-reader order.
- Files: visuals.py, theme.py print rule.

S4. No phone foot-spine on pages that already render Verify, Readings and Related sections below 900 px. The desktop
spine is unchanged. File: render.spine.

S5. Curated lists capped at 6 cards: "Start here" on /evidence/ and related records on /methodology/. Each list then
links to the full list. The order stays Master-driven.

S6. Verify is a link list. A domain page's #verify shows title, reference and period per record; the full statement
lives on the record.

S7. Teasers are a title plus one line.
- Readings, Measurement and More on domains show title, period and one sentence.
- /explore/'s "What the evidence cannot yet answer" becomes a title list linking to /measurement/#ID.

S8. Measurement priority cards.
- Visible: priority, domain, title, current evidence, and the decision it would strengthen.
- Dimensions, Questions it would answer and Evidence needed go in one `<details>` with the existing IDs.
- Adjust the validate.py priority-clock check.

S9. /data/ order.
- What the catalogue holds and the coverage counts come before the directory.
- The six short boundary sections merge into one, with one open paragraph and the rest folded.
- "Reports, methods…" folds into the curated-shelf heading.
- The macro chronology becomes a pointer to /finance/ (W3d).
- The TOC goes from 12 entries to ≤5.
- These are Master 03_PAGE_SECTIONS changes; record each in KEY_MIGRATION.

S10. TOC of at most 6 entries, and none on pages under 6 phone screens.
- Group by the tiers already in presentation_priority.json.
- Domains: Answer and limits · What the evidence shows · How to read it · More evidence · Go further (Readings,
  Related, Measure) · Verify.
- Methodology: What is measured · How evidence is accepted · Uncertainty and derivation · Comparison and composites ·
  What the method does not claim · Corrections and challenge.
- Group labels are new UI strings, added Master-first. They link to their first existing anchor.

S11. Domain H1 = short thesis.
- At most about 8 words in EN, no dates or numbers. The dated finding stays as the lead's first sentence.
- Master 02_SITE_MAP titles, EN and AR together. The Arabic is written as Arabic and fixes the AR /access/ parity
  drift (21 words against 10).
- Starting drafts, to be checked by the evidence specialist:
  - /payments/ "Payments: more reported terminals, use not measured";
  - /providers/ "Providers: listed is not the same as operating";
  - /firms/ "Firms: the answer depends on the question asked".
- #page-title is unchanged.

S12. Record head order.
- New order: crumb → rubric → H1 → one record line "When · For whom" (human dates) → tools → q1.
- Drop q3 where its body equals the For-whom line, and move id="q3" onto the record line.
- Replace only part (2) of gate RC-1115 (the record-head order) and its control at
  test_gate_negative_controls.py:582–584. Keep parts 1 and 3–6.

S13. Human dates in public text.
- A display formatter turns YYYY-MM-DD into "7 November 2022" / «7 نوفمبر 2022», and "Mar-2025" into "March 2025".
- datetime attributes and machine fields keep ISO.
- Check the public-literal closure. If display formatting cannot satisfy it, make a Master period-text transaction.
- Target: 0 ISO dates in public prose and record headers (about 632 tokens on 42 pages today).

CR-S12. Navigation per D8, in navigation_interaction.json, by you as steward. Adjust nav tests and the
header-overflow check.

══════════════════════════════════════════════════════════════════════
APPENDIX G — ENVIRONMENTAL FOOTPRINT (W4F, D12)
══════════════════════════════════════════════════════════════════════

Principle: measure what can be measured exactly (bytes transferred); estimate what cannot (emissions); say which is
which. No third-party script or badge, no data sent anywhere, no cookies.

G-1. Build-time measurement.
- In Python (stdlib only; the gates job has no browser), compute for every page the cold-load bytes of its
  first-party resources: HTML, CSS, JS, fonts and images, as referenced by the page.
- Use gzip, as _headers and the nginx host serve them, and the same method as scripts/performance_budget.py, so one
  page has one byte figure.
- The footer digits change the page's own size: resolve this deterministically by fixed-width rounding or a second
  pass, and test it.
- Cross-check against Playwright in the browser job only.
- Re-measure on the real host at hosting; that is a HOSTING item.
- Emit a generated per-page metric file.
- Gate: the value shown on each page equals the measured value at the stated rounding.

G-2. Estimate.
- Convert bytes to an emissions estimate with the Sustainable Web Design Model, version 4, as implemented by CO2.js
  (@tgwf/co2, pinned exact version). Inline the published SWD v4 coefficients in
  Python (build) and JS (runtime), and test both against pinned CO2.js in the browser job only. Keep Node out of
  build.py.
- Use the global average grid intensity and state it. Round to 2 significant figures.
- Record the model version, constants and CO2.js version as a dated D12 section appended to the existing
  docs/SUSTAINABILITY_METHOD.md. Do not create a parallel method file. Update its "no carbon figure until the release
  host" line and the EAD-10 row accordingly: the build estimate now exists; host re-measurement remains HOSTING.
- Show it as "≈ x g CO₂e (estimate)". Never present it as a measurement.

G-3. Runtime, per visit (progressive enhancement in site-src/app.js).
- Sum transferSize across PerformanceNavigationTiming and PerformanceResourceTiming for the current page view. Cached
  resources count as 0, which is honest.
- Keep a running total for this tab only, in sessionStorage, wrapped in try/catch.
- Apply the same SWD v4 coefficients, inlined.
- Test: the runtime result equals CO2.js for the same bytes.
- Without JS, the build-time value is shown.

G-4. Display.
- One quiet footer line on every page, after the licence line:
  - EN: "This page: 186 KB · ≈ 0.04 g CO₂e (estimate) · How this is measured";
  - AR: «هذه الصفحة: 186 كيلوبايت · نحو 0.04 غ مكافئ ثاني أكسيد الكربون (تقدير) · طريقة القياس».
  The numbers shown here are illustrative; the real ones are generated.
- With JS, a second clause: "This visit: 4 pages · 410 KB · ≈ 0.09 g CO₂e".
- The link goes to /about/#footprint. The line never competes with evidence styling.
- Public-literal closure: register these values as a generated SITE_OPERATION_METRIC class with its own gate (value
  equals measurement). They are not evidence (D15), and the closure gate is not weakened.

G-5. /about/ section "The footprint of this site" (Master-first, EN and AR, id="footprint"). It states:
- What is measured and how (G-1 to G-3), and what is excluded or uncertain: device and network variation, grid mix,
  the model's assumptions.
- The design choices that keep transfer low, which are also accessibility choices for low-bandwidth users in Yemen:
  - static pages; no trackers or third-party scripts;
  - self-hosted subset fonts; no video;
  - caching.
- How CauseWay operates. Exact owner-confirmed wording, without adding or upgrading claims:
  - EN: "Our office in Aden runs on solar power. We do not use single-use plastics in the office. We are moving our
    internal processes to paperless workflows."
  - AR: «يعمل مكتبنا في عدن بالطاقة الشمسية، ولا نستخدم البلاستيك أحادي الاستخدام في المكتب، ونعمل على تحويل
    إجراءاتنا الداخلية إلى إجراءات بلا ورق.»
- One sentence of references: the Sustainable Web Design Model v4 (sustainablewebdesign.org); CO2.js (Green Web
  Foundation); the W3C Web Sustainability Guidelines (verify its current status and date before citing).
- Language rules:
  - specific and verifiable only;
  - never "green building", "eco-friendly", "sustainable website", "carbon neutral" or "net zero";
  - never imply the hosting is green until the host is verified (Green Web Foundation check at hosting, HOSTING item).
  These follow the logic of the UK CMA Green Claims Code and EU Directive 2024/825 (generic claims banned from
  27 September 2026).
- /privacy/ (Master-first, now, because it will be true when built): one sentence. The footprint line reads
  transfer sizes in your browser, stores a running total only in this tab's session storage, and sends nothing.

══════════════════════════════════════════════════════════════════════
APPENDIX H — THE PREVIOUS DESIGN PROMPTS: what is carried over, what is rejected
══════════════════════════════════════════════════════════════════════

Carried over:
- **From the OpenAI current-source kit:**
  - a real baseline from current pages and states;
  - reader-job testing;
  - three genuinely distinct compositions, then one decision;
  - provenance, limits and not-comparable states as first-class visual objects;
  - native Arabic typography and data isolation;
  - non-colour states;
  - 320/390/768/1440 px plus 200%/400% zoom, forced colours, no-JS and print;
  - "what became more true / easier / more complex / removed";
  - no invented content. Design changes the Master only for the recorded structural copy in S9–S11, S13 and G-5,
    through run_stage.py, and never for evidence meaning.
- **From V2/V3:** measurable craft checks, used as defaults the lead may override with a recorded reason:
  - targets ≥24 px; text contrast ≥4.5:1; ≤4 font files;
  - the licence line legible on every page;
  - no tracked capitals in Arabic;
  - no decorative shadows or left-accent cards.

Rejected:
- the offline ZIP/bootstrap route and the "no GitHub" constraint (Claude Code works on the repository with CI);
- the 41-page sandbox;
- the separate Claude Design stage and the owner-approval gate (D7);
- CSS-only as a dogma (recorded markup changes are allowed);
- page-length targets that would cut content (D13);
- any font family beyond IBM Plex.


══════════════════════════════════════════════════════════════════════
APPENDIX I — FINAL QA CHECKLIST (W8; each item PASS / FAIL / NOT RUN, with evidence)
══════════════════════════════════════════════════════════════════════

I-1. Truth and evidence
- Every Appendix A finding is CLOSED or FRONTIER, with its locator.
- Bilingual numeric invariance is 0, number words included.
- Public-literal closure regenerated; there is no public number without a bound record.
- The source-reference closure passes, and every public source has a public locator (rule 5).
- No held, internal or non-public text leaks (HOLD, CONTRACT, NON_PUBLIC values, names under D10, procurement
  sources).
- Spot-check the firewall on 20 random claims: people ≠ accounts; listed ≠ operating; target ≠ result;
  observed ≠ estimated; missing ≠ zero; chronology ≠ causality.

I-2. Arabic and English
- Every register row is applied, stopped with a reason, or resolved by its condition.
- The house-style lint is clean, and the mechanical rules are gated.
- The EN editor and AR editor verdicts are recorded for every changed string.
- No ISO date appears in prose or record headers.

I-3. Every page family, AR and EN, at 320/390/768/1440 px:
- Home; Explore;
- the 8 domains;
- the evidence index and 3 records (full, partial, held);
- Compare;
- the Readings index and all Readings;
- /measurement/, /methodology/, /data/;
- /about/ (funding, footprint), /rights/, /privacy/, /terms/, /accessibility/, /corrections/, /contact/;
- 404; the retired address.
On each: one H1; TOC within the rule; the answer, limit and source visible on the first screen of domain and record
pages; no horizontal overflow; no clipped text; figures and their limits shown together.

I-4. Functions
- Search: typed results, dated events, ?q= state, empty and error states, keyboard use, and the AR and EN query
  sets (gate).
- Compare: preselect, a shareable URL, a one-sentence verdict reason, verdict words or shape, a printable summary,
  and a mobile fallback.
- /data/ filters and facets, and deep links (?source=, #source-ID) that open the right group.
- Cite and copy.
- The report-an-error form:
  - pre-fills from every record, figure and Reading;
  - validates its fields;
  - produces the structured body and reference code;
  - offers "Copy report", and the no-JS mailto fallback;
  - docs/CORRECTIONS_PROCESS.md is linked from /corrections/.
- Language switch keeps your place. The menu opens with Enter and Space and closes at ≥900 px. Disclosures work.
- No-JS: all content reachable; the footprint shows the build-time value.
- Print: limits, sources, URL and edition.

I-5. Accessibility (claim no conformance)
- Automated checks clean, or each issue recorded.
- Keyboard paths and visible focus.
- 200% and 400% zoom; forced colours; reduced motion.
- Landmarks, headings, labels, and alt text or a table for every visual.
- Targets ≥24 px; text contrast ≥4.5:1 and UI ≥3:1.

I-6. Design and visuals
- DL-V2-001 recorded, with G1 scores and screenshots.
- G0 metrics re-measured against the S and G2 targets.
- Every visual contract is in a recorded state, and no withheld visual lacks a true reason.
- At most 4 font files per page; IBM Plex only.
- The logo is canonical.
- The redundancy scan is resolved.

I-7. Performance and footprint
- The performance budget passes (/ar/data/ ≤350 KB cold).
- Footprint values equal the measurements.
- The runtime meter matches CO2.js for the same bytes.
- No third-party request.

I-8. SEO
- Unique titles and descriptions; reciprocal hreflang; the canonical switch tested.
- JSON-LD validates; sitemap and robots are generated and gated.
- Social cards render in AR and EN.

I-9. Security and release boundary
- Security headers prepared (_headers) and tested; CSP without unsafe inline (or the recorded exception).
- deploy.yml refuses a SHA that does not descend from the hosting-ready tag; public_downloads is false; no analytics.
- No secrets, *.dta or respondent files tracked.

I-10. Repository
- The register's live view shows only HOSTING items open.
- Counts are consistent across README, README.ar, the checkpoint, Context, the manifest and the Master.
- Every new file is classified; SHA256SUMS regenerated.
- The housekeeping workflow and its tests are present; REPOSITORY_SETTINGS.md is present.
- Lineage closing notes are appended to the historical .md docs, and the historical JSON is classified as lineage. There are no stale DESIGN HANDOFF READY claims.
- Mohammed Waleed's three items are ported, with credit. His branch is listed for archive.
- The cold-reader tests pass in EN and AR.
