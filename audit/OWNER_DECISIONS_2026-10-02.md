# Owner decisions — 2 October 2026

- **Date:** 2 October 2026
- **Decided by:** the owner (CauseWay)
- **Recorded by:** the session meeting the before-merge conditions C1–C5 of
  [`PR8_INDEPENDENT_ACCEPTANCE.md`](PR8_INDEPENDENT_ACCEPTANCE.md) on pull request #8 (`claude/hopeful-mccarthy-jgip83`),
  in the commit that cites this file. The decisions are recorded as given; nothing here is applied to the Master, a
  projection, a page or a controlled contract by this record. Where a row says "applied Master-first in the
  release-candidate pull request" or "implemented in the release-candidate pull request", that pull request carries the
  change through the protocol of `CONTRIBUTING.md` §4 and §5.
- **Nothing in this record declares PUBLIC RELEASE READY or claims WCAG conformance.**

| ID | Decision |
|---|---|
| OWN-01 | Approve this /about/ funding and relationships paragraph, applied Master-first in the release-candidate pull request. EN: "Funding. CauseWay funded the development of this edition entirely from its own resources. No donor, regulator, source institution or external commissioning party funded it. This resource is not a deliverable of any contract or partnership with the institutions whose data it presents." AR: «التمويل: موّلت CauseWay تطوير هذا الإصدار بالكامل من مواردها الخاصة، ولم تموّله أي جهة مانحة أو تنظيمية، ولا أي جهة ناشرة لمصدر، ولا أي جهة خارجية كلّفت به. وليس هذا المورد ناتجًا عن أي عقد أو شراكة مع المؤسسات التي يعرض بياناتها.» Footer unchanged ("Developed and maintained by CauseWay"). |
| Publisher name | "CauseWay" in Latin script in both languages. No Arabic transliteration. |
| OWN-04 | Licence deferred. Launch is link-and-short-citation only; downloads and exports stay disabled; the "reuse terms not assessed" wording stays. Not a gate for a link-and-citation launch. |
| OWN-03 | Public origin decided when hosting is ready; public_origin stays null until then. |
| D7 | The owner records final D7 visual acceptance of the Design package on 2 October 2026. |
| Social images | Keep the 286 social images; scripts/discovery.py makes og:image absolute once public_origin is set. |
| OWN-05 | CauseWay maintains the resource; whole-system review at each new edition; no fixed update cadence is promised. |
| OWN-02 | Confirmed: office@causewaygrp.com is monitored. |
| EAD-03 | Approved: export web-size logo derivatives by resampling only; the master logo file stays unchanged. |
| Relationships | CauseWay holds no active contract or partnership with any source institution related to Yemen financial inclusion. |
| Steward | For the release-candidate pull request only, the implementing session is programme steward for site-src/content/presentation_priority.json, limited to the EAD-11 patch recorded in design/ESCALATIONS.md. |
| A3 / C3 | Each figure prints its "does not establish" boundary once on the page, in the frame foot; on the page, the image's alt attribute and the visible text alternative use the governed accessible summary, which ends before the boundary. The full governed alt text, which ends with the boundary, stays wherever a figure leaves the page (export frames, social frames). Implemented in the release-candidate pull request. |
| A5 / C4 | The RETIRE_FROM_DESIGN tier is excluded from the domain depth frames: VIS-CAPITAL-CONTEXT is no longer shown as a frame on /reforms/; its Evidence Record text stays. Implemented in the release-candidate pull request. |
| A4 / C6 | The 13 NO_GOVERNED_CONTRACT__TABLE_ONLY records: a register item, post-launch; no change in this edition. |

## Addendum — 2 October 2026 (Part B)

Appended by the implementing session in the release-candidate pull request (#9), Part B item B0 of
`audit/release_candidate/INSTRUCTIONS.md`, recording the owner's decisions that brief carries. The rows above are unchanged.

| ID | Decision |
|---|---|
| A4 / C6 revised | The governed method text of the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY` records is rendered on their record pages (Part B item B1). This revises the row A4 / C6 above, which deferred it. |
| Accessibility | The human accessibility audit is not a release gate, because no conformance is claimed; it is replaced by the extended automated audit of Part B item B10. An external audit remains welcome after launch. |
| Part B designation | For Part B of the release-candidate pull request, the implementing session is programme steward and English and Arabic editor, under the designation rules of the brief (no new facts; both languages together; independent review of every pair before commit; no conformance, certification, legal, rights or security claims). |
| Architecture | Static site; no server, database or API service. |
| Root language | The neutral root keeps opening the Arabic edition by default; the language switch stays on every page. |
| Product name | "Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن" is unchanged. |
| Owner rules | Verbatim below. |

> OWNER RULES ON NUMBERS, PAGES AND CLOSED DECISIONS
> 1. No unsourced number or claim. A number or claim may be added only through the full Master-first path: read in the original source, bound to a source-traced record, written in both languages, accepted by the literal audit. Numbers that are already governed may be bound as rows of an existing visual contract.
> 2. No new page or route, unless the product challenge (B15) shows a task failure that cannot be fixed on an existing page and the red team agrees; such a page carries its full Page Spec, both languages, a search record and a social image, and passes every gate.
> 3. Closed decisions stay closed: dashboards, composite scores, league-table rankings, a synchronised "current state", an eleventh Measurement priority (REJ-02), Dataset structured data before downloads and a licence exist (REJ-03), a carbon figure (REJ-04), a fixed update cadence, a separate regulatory "record" route, and third-party or advertising trackers. Two are refined, not reopened: cookieless, first-party aggregate usage counts (B14) and international context from same-source aggregates (B15).

## Owner note — 3 October 2026, 03:10

Recorded verbatim (append only), as the owner asked, so that it survives compaction and any new window.

1. Decision 18 names. The governed rule withholds entity names for the CBY-Aden enforcement decisions (CLM-019; the 14 decision cards; only NEG-EW-011 prints a name, from the 2024 circular). Apply it consistently:
   - Keep the transcribed names in the Master as non-public lineage only, with the signed scan as locator.
   - Print them nowhere: not on any page, table, search record or social image.
   - In the status-event table, PSE-015 prints what the other decisions print: date, decision number, class, action and the governed withholding wording, not "names pending".
   - If the governed rule actually allows names for some decisions, do not print. Record the conflict in design/ESCALATIONS.md.

2. POS update to June 2026. Update from the CBY-Aden originals as planned, with these conditions:
   - Where a release contradicts itself (May), do not resolve it and do not compute a change the source contradicts. Print the source's totals, and either use the existing "Source figures disagree — both are shown" pattern or withhold the derived change with a stated reason.
   - Keep every boundary (terminals ≠ people ≠ use; the CBY-Aden scope) on every surface the new values reach.
   - Record the Arabic-site discovery and the January locator change in ORIGINAL_SOURCE_VERIFICATION.md.

3. Budget. The account has used 51% of its weekly limit, which resets on 9 October. The release candidate must finish within what remains. From now on:
   - Review depth follows risk.
     - For governed copy, the brief's rule is one independent subagent that did not write the change, reading every pair Arabic first and then English. Use exactly that.
     - Add a second, adversarial reviewer only for new public numbers or for entity and regulatory statements.
     - Do not run three-lens review workflows.
   - Fold review findings into one rerun per transaction.
     - Batch related changes so each transaction carries more and reruns less: RC-8 to RC-10 may merge where they touch different cells.
   - Do not re-verify what is already verified and committed. Do not poll or wait on finished work.
   - Order what remains by value to the release:
     1. truth and currentness (RC-7, A1, A2, POS, the Decision 10 date and locators);
     2. B6;
     3. the evidence landscape;
     4. B10 accessibility;
     5. B12 and B13;
     6. B14;
     7. B15 as a focused challenge: the ten users' tasks, with the named red team in one combined pass;
     8. B16;
     9. B17.
     Low-value polish goes to the roadmap, not into this pull request.
   - If the limit comes close, stop at a clean point, push, write the RESUME POINT and stop. Never leave work uncommitted.
