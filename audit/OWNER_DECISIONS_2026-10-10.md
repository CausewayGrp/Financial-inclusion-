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
