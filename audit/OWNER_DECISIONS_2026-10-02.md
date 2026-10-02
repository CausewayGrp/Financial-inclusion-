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
