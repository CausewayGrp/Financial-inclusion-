# Owner decisions — 9 October 2026

- **Date:** 9 October 2026
- **Decided by:** the owner (CauseWay)
- **Recorded by:** the session that built the V1 design integration (pull request #15, merged as `b323a441`) and now
  builds Phase B on `claude/design-review-constraints-l9au89`, in the commit that cites this file. The decisions are
  recorded as given; where the owner left a choice open, this record says so and decides nothing.
- **Nothing in this record declares PUBLIC RELEASE READY or claims WCAG conformance.**

| ID | Decision |
|---|---|
| V1 | Pull request #15 (V1 phases 1 and 2, `design/DESIGN_INTEGRATION_V1.md`, DL-V1-001…012) approved for merge once CI stays green, after its description covers phase 2, with "Create a merge commit". Done: CI 9/9 on `1850f59e`; merged as `b323a441` on 9 October 2026. |
| B | Phase B: one new pull request from `main` after that merge. Steward changes are approved by the owner commit by commit; each commit names the finding it closes. |
| B-a | `site-src/content/presentation_priority.json`: add the Home Orientation entry exactly as proposed in `design/ESCALATIONS.md` ("Raised at V1 phase 2"); section 4, "What should not be inferred?", stays always visible. |
| B-b | One Master transaction for interface labels only (no figure, no data), English and Arabic together: the `/finance/` chronology summary label; the `/data/` "About this source" row label (the "Does not establish" line stays outside it); the currentness-strip label bound to the Master's verification date and edition; the Evidence Colophon labels; the numerals 01–05 bound to the five hubs. |
| B-c | `site-src/content/content/navigation_interaction.json`: Cite and Report move to a page-tools row under each H1; the full mobile menu (the five hubs with their numerals, the eight domain answers, Trust, the language switch). Then build what these unlock and re-measure phone screens. |
| Fonts | No Latin serif; IBM Plex stays. Arabic headings stay at SemiBold 600. |
| Rights | **Not decided.** The owner's message set out two options — CC BY 4.0 for CauseWay's own content stands ("no licence" meant regulatory licensing), or withdraw CC BY 4.0 and correct the record Master-first — without choosing. The rights record and the public `/rights/` text are unchanged until the owner chooses. |
| PR #13 | Pull request #13 stays untouched until Phase B merges. |
| Gates | The same gates as before: CI 9/9; no text, link, ID or hook lost; no file deleted. |
| Latitude | The owner asks the session to take the lead on further design elevation that makes the site clearer, with a focus on the quality of the filtering, source and search tools, inside the gates above and the repository's governance. |

Cross-reference (appended 2026-10-10): the Rights row above ("Not decided") is kept as history; it is superseded by
the owner's decision of 10 October 2026, `audit/OWNER_DECISIONS_2026-10-10.md` (OWN-04-R): CC BY 4.0 for CauseWay's own
content stands, and the rights question is closed.
