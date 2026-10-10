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
