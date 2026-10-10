# Owner decisions — 10 October 2026

- **Date:** 10 October 2026, Aden.
- **Decided by:** the owner (CauseWay).
- **Recorded by:** the session executing the rights-and-naming brief of 10 October 2026, in the commit that cites this
  file. The decisions are recorded as given; nothing here is applied to the Master, a projection, a page or a controlled
  contract by this record. Part A, which this record belongs to, changes no Master and no public page: `/rights/` and
  `/terms/` already print CC BY 4.0 correctly.
- **Append-only.** No earlier record is rewritten. Where this record supersedes an earlier one, it says so and names it.
- **Nothing in this record declares DESIGN HANDOFF READY anew or PUBLIC RELEASE READY, and it claims no rights
  clearance, legal review or certification.**

## 1. Rights — the question is closed

The owner's decision of 10 October 2026, recorded as given:

> "CC BY 4.0 for CauseWay's own content STANDS, as adopted on 3 October 2026. My message of 9 October ('we have no
> licence / لا نملك ترخيص') referred to REGULATORY licensing: CauseWay is not a licensed financial institution and
> claims no such status. It never referred to the reuse licence. The rights question is closed."

| ID | Decision |
|---|---|
| OWN-04-R | **Rights decided, and closed.** Creative Commons Attribution 4.0 International (CC BY 4.0) covers the content CauseWay owns in this resource — its text, analysis, visual designs, the compiled records, and the structure and annotations of the exports — exactly as adopted on 3 October 2026 (`OWNER_DECISIONS_2026-10-02.md`, owner instructions of 3 October 2026, 09:50 Cairo, section E; owner note of about 11:15 Cairo, 3.6). Nothing about the scope of the licence changes here. |
| OWN-04-R-a | **The two senses of "licence" are distinct.** The owner's message of 9 October 2026 ("we have no licence / لا نملك ترخيص") is about **regulatory** licensing: CauseWay is not a licensed financial institution and claims no such status. It is not about the **reuse** licence. In Arabic: رخصة is the copyright licence; ترخيص is regulatory licensing. |
| OWN-04-R-b | **Not decided, and unchanged:** the release step "CauseWay's counsel confirms the CC BY 4.0 text". `licence_text_confirmed` stays `false` and `public_downloads` stays `false` in `site-src/deployment.json`; `docs/RELEASE_RUNBOOK.md` steps 2 and 7a are unchanged. This record does not alter that gate. |
| OWN-04-R-c | **The repository's software code** is outside the CC BY 4.0 licence and nothing is decided about it here. No code licence is declared, and none is implied. |

### What this supersedes, and what it does not

- It supersedes the **"Rights: Not decided"** row of `audit/OWNER_DECISIONS_2026-10-09.md` (recorded on pull request
  #16, branch `claude/design-review-constraints-l9au89`, not merged at the time of this record). That row stated the
  owner's two options — CC BY 4.0 stands, or withdraw it and correct the record Master-first — without choosing. The
  owner has now chosen the first. The 9 October record is not edited.
- It closes the escalation `ESCALATE_TO_STEWARD (records disagree; not acted on) — rights` in
  `design/ESCALATIONS.md` ("Raised at V1 design integration (9 October 2026)"). The record that was wrong was the
  reading of the 9 October message as a statement about the reuse licence; the B16 disposition
  ("Licence decided: CC BY 4.0 for CauseWay's own content", `design/ESCALATIONS.md` X-ESC-B15-06,
  `audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`) was right and stands.
- It does not reopen `OWN-04` as a decision. `OWN-04` closed on 3 October 2026; the owner's open item has been
  "counsel confirms the CC BY 4.0 text" since then, and still is.
- It changes no public page. `/rights/` and `/terms/` already state CC BY 4.0 in both languages, with the logo and
  third-party material excluded; no public copy claims a regulatory status CauseWay does not hold.

## 2. Steward designation for the public naming and terminology change (Part B)

| ID | Decision |
|---|---|
| OWN-NAME-01 | The owner designates the session executing Part B of the brief of 10 October 2026 as **programme steward for the naming and terminology change**. Under that designation, and under `AGENTS.md` hard rule 2, it may edit `site-src/content/content/navigation_interaction.json` in place, in commits that each name the finding they close, running every gate. `site-src/content/presentation_priority.json` is **not** in scope of this designation. Interface labels live in the Master (`04_NAV_UX`); they change Master-first, through `audit/tranche_b_execution/run_stage.py`, and the projections are regenerated. |
| OWN-NAME-02 | The owner approves names. Part B stops when it is green and hands the owner the final label table; it is not merged by the session. |

Nothing in this designation permits a change to the meaning of evidence, to a number, period, universe or limit, to a
route or URL, or to `presentation_priority.json`.

## 3. Addendum: the owner's corrections and approvals later on 10 October 2026

Recorded by the orchestration session (programme steward) as the owner gave them. Appended; nothing above is edited.

| ID | Decision |
|---|---|
| OWN-STOP-W | A "Stop now" message received by this session was meant for a different session (the one that pushed `0da3a43`). The owner withdrew it for this session: this session owns the repository and resumes the orchestration. |
| OWN-14-R | Pull request #14: `0da3a43` records the opposite of the owner's decision; the decision is **INDEX**. It is reverted with `git revert` (no force-push), CI re-run, then merged. |
| OWN-2a | Transaction A also fixes CLM-026's Arabic summary, which said six of its measures and then three; the English says three. Master-first. The whole Arabic corpus is then scanned for spelled-out numbers that disagree with the English digits, and the numeric-invariance gate is extended to number words with a negative control. |
| OWN-2b | Locators used: the FMIIP project appraisal document (PADHI00396) printed p. 26 for the access-point definition and printed p. 28 for the "active" definitions; The Little Data Book on Financial Inclusion 2015, p. 160. Every locator written is read in the original by this session, not copied from the brief (`legacy_followthrough/SOURCE_VERIFICATION_2026-10-10.md`). |
| OWN-2c | The phrasing "76% → 61%" is dropped everywhere. Only what was verified is stated (85.1% before the 2022 revaluation), or the share is left out. |
| OWN-2d | Reading CWR-011 is included only if the May 2026 balance-sheet values from the CBY bulletin are first created as bound Master records. Territory: the bulletin does not state the territory its figures cover, and the record says so. If the records cannot be bound to the original, CWR-011 is dropped and the reason recorded. |
| OWN-2e | The PAD ¶9 "two percent" line is bound as a record from the PAD (a held source) only because CWR-007's concordance uses it. |
| OWN-2f | The rights work covers the Findex Microdata Research License for the three derived 95% intervals: they are cited as that licence requires, and the page states that CC BY does not extend to the underlying data. |
| OWN-3 | Before every merge the session confirms that every commit on the branch came from this session. |
| OWN-NAME-03 | The labels of pull request #19 (transactions NB-1 and NB-2) are **approved** as built. Pull request #19 is merged; steps 5, 6 and 7 of the orchestration follow. |

## 4. The CC BY 4.0 text: endorsed with two corrections; the rights question closed permanently (10 October 2026)

The owner's decision of 10 October 2026, given after pull request #22 merged and carried out as transaction RIGHTS-FINAL
(`audit/rights_final/`). Appended; nothing above is edited.

| ID | Decision |
|---|---|
| OWN-RF-01 | **The CC BY 4.0 text is endorsed with two corrections, and the rights question is closed permanently.** |
| OWN-RF-02 | **/rights/, correction (a).** The microdata sentence no longer states a legal reading of the licence ("which permits publishing aggregate statistics…"). It states facts only: the CLM-026 confidence intervals are computed from a file CauseWay obtained under the World Bank Microdata Research License, and only aggregate estimates are published, never respondent-level data. The citation sentence and "CC BY 4.0 does not extend to the underlying microdata" are unchanged. The owner's Arabic was reviewed by the independent Arabic editor, who removed one word («منها») because it had no valid referent and added a meaning the English lacks. |
| OWN-RF-03 | **/rights/, correction (b).** Directly after the "Covered:" list: for figures CauseWay calculates from other publishers' data, the licence covers CauseWay's calculation and presentation, and the underlying data stay under their publishers' terms. No other rights wording changes; /terms/ and the footer are unchanged. |
| OWN-RF-04 | **Licence-text confirmation: the owner confirms it, and no counsel review is required.** The release rule changes from "CauseWay's counsel confirms" to "the owner confirms" in `site-src/deployment.json`, `docs/RELEASE_RUNBOOK.md` step 7a, the deploy workflow's refusal message, validator RC-B14, README, the checkpoint, the Context and the handover. `licence_text_confirmed` is set to `true`. `public_downloads` stays `false`, as a separate owner decision. The deploy workflow stays inactive until the owner switches it on. |
| OWN-RF-05 | Optional and not blocking: the owner may request written confirmation from the World Bank Microdata Library that publishing the CLM-026 aggregate intervals is consistent with the Research License. The text no longer depends on it (`FINAL_OPEN_ITEMS_REGISTER.md`, OWN-09). |
| OWN-RF-06 | The licence gates PN-G01 (every content page declares the licence, for a reader and for a machine) and PN-G02 (a rename is never menu-only) land in the same pull request, so the corrected text is guarded from the moment it lands. |

**Owner's confirmation, 10 October 2026:** The owner has read and confirms the CC BY 4.0 text on /rights/, /terms/ and the footer, in both languages, as corrected in RIGHTS-FINAL. No legal review is claimed.

## 5. The close-out brief: owner decisions D1–D15 (brief version 5, 10 October 2026)

Recorded verbatim from `audit/close_out/BRIEF.md` §1 (version 5, which supersedes version 4, kept as
`audit/close_out/BRIEF_v4.md`). The owner's mid-session message of 10 October 2026 named D4, D8 (revised), D9, D11,
D13, D14 and D15 as the version-5 text to record; the whole section is recorded so that every decision the brief
cites has one place. Appended; nothing above is edited. Where a decision here and an earlier section differ, this
section is the later decision.

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
