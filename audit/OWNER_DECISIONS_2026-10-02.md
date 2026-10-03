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

## Owner decisions on the open escalations — 3 October 2026, 09:05 Cairo

Recorded verbatim, append-only. Each escalation it decides is closed in `design/ESCALATIONS.md` by a dated line that
points here.

> Owner decisions on the open escalations, 3 October 2026, 09:05 Cairo. Record this note verbatim, append-only, in audit/OWNER_DECISIONS_2026-10-02.md, and close each escalation in design/ESCALATIONS.md with a dated line that points to it.
>
> 1. public_use of PSE-006, PSE-007, PSE-010, PSE-013 and PSE-014: rewrite each to the withholding rule, Master-first, so that no governed field allows an enforcement-decision entity name to be shown. RC-NAMES stays.
>
> 2. The 2024 e-wallet circular (SRC-CBY-UNLICENSED-EWALLET-2024-001): withhold all twelve names alike. This reverses the earlier choice to print one (NEG-EW-011, "We Cash"), for consistency with the enforcement-decision rule, fairness to the other eleven, and the risk of presenting a June 2024 status in 2026.
>    - Keep NEG-EW-011 as a record: same ID, same route, same counts. Rewrite it Master-first in both languages as one wallet service among the twelve the circular names, keeping its date boundary ("not a 2026 status"), what it does not establish, and the link to the CBY original. Keep the name in the Master as non-public lineage only.
>    - Remove the name from every surface: title, summary, meta and og descriptions, page sections, page specs, search records, social image and any figure.
>    - Extend RC-NAMES, or add a gate with a negative control, so that no name from the circular can print anywhere, including the search index.
>    - Do not add the name as a search alias; the index is public. Instead, give the search empty state one governed sentence, in both languages: names of entities from the regulator's lists and enforcement decisions are not reproduced here, and the original documents are linked from Data & sources. Withdraw the earlier addendum instruction that "We Cash" must rank first.
>    - The independent review for this change includes the adversarial reviewer (entity statement).
>
> 3. About and Cite on phones (findings A-12, C-6, C-8): the owner designates this session as programme steward for one patch to site-src/content/content/navigation_interaction.json, following the EAD-11 precedent.
>    - Add the governed trust_navigation links (About first) to the opened mobile menu.
>    - Add the existing governed "Cite this page" control inside the mobile menu, not the header, so the 320 px header carries no extra load.
>    - Use existing governed labels only; make no other edit to the file.
>    - Name A-12, C-6 and C-8 in the commit. Run every gate, plus a visual check of the menu at 320 and 390 px in both languages. Record the designation and its scope in the decisions file.
>
> 4. Domain strip (C-10): not in this release. A new navigation element needs design; it goes to docs/ROADMAP_V1_1.md.
>
> 5. VIS-MFI-SPINE table (B-7): post-launch. Its title no longer promises a view it does not draw (RC-16).
>
> 6. Exports (U3, U6, U7): release-dependent on the owner's licence decision. public_downloads stays false; the runbook already names the switch.
>
> 7. What CauseWay is (C-6): no new organisational description in this release. The existing governed text on CauseWay's role and funding stands; nothing about the organisation is to be written that the owner has not supplied.
>
> Then continue: Addendum 2 improvements (build the high-value governed ones, disposition the rest), B16, B17 and the final report. The final report lists these owner decisions. Keep the budget rule.

**Steward designation (point 3), as recorded by this session.** The owner designates this Claude Code session as
programme steward for exactly one patch to `site-src/content/content/navigation_interaction.json`, following the EAD-11
precedent for `presentation_priority.json`. Its scope:
- add the governed trust_navigation links, About first, to the opened mobile menu;
- add the existing governed "Cite this page" control inside the mobile menu, not the header;
- use existing governed labels only, and make no other edit to the file.

The commit names A-12, C-6 and C-8. The designation ends with that commit.


## Owner instructions of 3 October 2026, 09:50 Cairo (consolidated; supersedes any unsent owner note)

Received in this session on 3 October 2026, first in a chat message cut off mid-sentence in section D, then complete as
an uploaded file (`YFIE_OWNER_FINAL_MESSAGE_2026-10-03.md`). Recorded verbatim from the complete file. It restates
decisions 1–5 of 09:05, replaces decision 6 (exports: a licence is now adopted, section E) and decision 7 (what CauseWay
is: the owner supplies the copy, section D), and adds sections B, C, F and G.

> OWNER'S INTENT: read this first.
>
> What this release must be. It must be the most trustworthy public explanation of financial inclusion in Yemen that exists, in Arabic and English:
> - a Yemeni citizen can understand it on a phone;
> - a journalist can quote it without error;
> - a central-bank supervisor can verify it line by line;
> - a researcher can cite it.
> Every page should leave its reader knowing more than they expected, and never believing something the evidence does not support. It will carry CauseWay's name, so every sentence must be one CauseWay can stand behind.
>
> How I want you to work:
> - Own it. You are the lead, editor-in-chief and programme steward. Decide, write one line of reasoning, and move on. Do not ask me: everything you need is in this note or in the repository.
> - Judge value, not volume. Spend effort where a reader's understanding or trust changes, in this order:
>   1. truth defects;
>   2. the first screen of each page;
>   3. paths that fail a named user;
>   4. polish.
>   Stop when what remains is low value.
> - Think as the team you would hire. That team is:
>   - a survey statistician;
>   - a payments and remittance specialist;
>   - a Yemen context analyst;
>   - a regulatory librarian;
>   - senior Arabic and English editors;
>   - an information designer;
>   - an accessibility engineer;
>   - a hostile reviewer.
>   Use subagents for independent review, verification and user testing, and keep every decision yourself.
> - Use your tools fully where they raise quality:
>   - read originals on the web;
>   - look at the built pages in a real browser, at phone and desktop widths, in both languages;
>   - make a gate or test hold every rule you add.
> - Close, never leave hanging. Every item ends as DONE, POST-LAUNCH (with its reason) or REJECTED (with its reason). Nothing stays undecided.
> - Never trade truth for polish. No number without its source and its limit, no name the rules withhold, no claim of conformance or clearance.
>
> The repository was made private by the owner on 3 October 2026. CI now draws on the account's minutes, so batch your pushes.
>
> Owner instructions, 3 October 2026, 09:50 Cairo: one consolidated note that supersedes any unsent owner note. Record it verbatim, append-only, in audit/OWNER_DECISIONS_2026-10-02.md, and close each escalation it settles with a dated line in design/ESCALATIONS.md.
>
> How to read this note:
> - You own the outcome. Where this note leaves a choice, make it.
> - Build now whatever adds value and can be done truthfully. Defer only with a stated reason.
> - Do not wait for the owner on anything below; every decision you need is here.
>
> A. ESCALATIONS
>
> 1. public_use of PSE-006, PSE-007, PSE-010, PSE-013 and PSE-014: rewrite each to the withholding rule, Master-first. RC-NAMES stays.
>
> 2. The 2024 e-wallet circular: withhold all twelve names alike. This reverses the earlier choice to print "We Cash" (NEG-EW-011), for three reasons: consistency with the enforcement rule, fairness to the other eleven, and the risk of presenting a June 2024 status in 2026.
>    - Keep NEG-EW-011 as a record, with the same ID, route and counts. Rewrite it as one wallet service among the twelve, keeping its date boundary, what it does not establish, and the link to the CBY original. The name stays in the Master as non-public lineage only.
>    - Remove the name from every surface: title, summary, meta, og, page sections, page specs, search records, social image and figures.
>    - Extend RC-NAMES so that no name from that list can print, including in the search index. Do not add the name as an alias.
>    - Give the search empty state one governed sentence: entity names from the regulator's lists and enforcement decisions are not reproduced here, and the originals are linked from Data & sources.
>    - The earlier instruction that "We Cash" must rank first is withdrawn.
>    - The adversarial reviewer reviews this change.
>
> 3. About and Cite on phones (A-12, C-6, C-8): the owner designates this session as programme steward for one patch to site-src/content/content/navigation_interaction.json, following the EAD-11 precedent.
>    - Add the governed trust_navigation links (About first) and the existing "Cite this page" control inside the opened mobile menu, not the header.
>    - Use existing labels only, and make no other edit to the file.
>    - Name the findings in the commit, and check the menu at 320 and 390 px in both languages.
>
> 4. Domain strip (C-10): roadmap.
>
> 5. VIS-MFI-SPINE table (B-7): post-launch. Its title is already corrected.
>
> 6. Exports: see E.
>
> 7. What CauseWay is (C-6): see D.
>
> B. RELEASE ADDRESS AND HOSTING
>
> 1. The address is https://causewaygrp.com/financial-inclusion-evidence/: lowercase and hyphenated, Arabic at that root, English under /en/.
>    - Every link, asset and fetch is root-absolute today, so the build would break under a subpath.
>    - Make public_origin able to carry a path, and derive a base path from it.
>    - Every link, asset, stylesheet and app.js fetch must honour it, and so must the search index, social images, canonical, hreflang, og:url, sitemap, structured data, the 404 page and the language switch.
>    - With public_origin null, the build stays byte-identical to today.
> 2. Gate: build with that origin into a temporary directory and serve it under the subpath. Run the link and asset sweep and the public tools against it: search, Compare, citation, share and print. No request may escape the base path. Add a negative control.
> 3. Indexing: until release, every page carries a noindex meta through a pre-release flag, because crawlers ignore a robots.txt that sits under a subpath. In the runbook, add the web administrator's step: reference the sitemap from the domain's root robots.txt, or submit it in Search Console.
> 4. Facts observed on 3 October 2026, which the runbook must reflect:
>    - causewaygrp.com uses DigitalOcean name servers.
>    - The corporate site is a Nuxt application (x-powered-by: Nuxt).
>    - It sets a "session" cookie on Path=/.
>    - It sends "x-robots-tag: index, follow".
>    Because DNS is not on Cloudflare, a Cloudflare Worker route is not available as things stand.
> 5. Write the hosting section of docs/RELEASE_RUNBOOK.md around these routes:
>    - Preferred route: deploy dist/ to our own Cloudflare Pages project, as now recommended. Route /financial-inclusion-evidence/** to it from the corporate Nuxt application with a Nitro routeRules proxy. That is a small change in CauseWay's own frontend repository, done later as its own task, not in this pull request.
>    - Equivalent route: if the corporate site runs on DigitalOcean App Platform, use a static-site component routed at /financial-inclusion-evidence. Use this only if our security headers can be served; otherwise the proxy route stands.
>    - Fallback: evidence.causewaygrp.com, with a 301 from the subpath.
> 6. For each route, state:
>    - how our security headers survive;
>    - that the corporate x-robots-tag, scripts and cookies are never added to our responses;
>    - how rollback works.
> 7. /privacy/ must stay true. This resource sets no cookies. If the domain's own cookie can reach these pages, say so in one governed sentence, in both languages: it is set by causewaygrp.com and not read by this resource.
> 8. Do not set public_origin yet.
>
> C. ADDENDUM ITEMS VERIFIED AS NOT YET DONE ON THE BUILT SITE: build them, governed and Master-first, in as few transactions as possible
>
> 1. /reforms/:
>    - Name the instruments by number once, where the page already describes them (Governor's Decision No. 23 of 2024; Decision No. 4 of 2025), from their governed titles.
>    - Give the "Rules, decisions and official lists" group on /data/ an anchor, and link it from "Verify it yourself" on /reforms/ and /providers/.
> 2. /payments/ headline: it is now 36 words, and it serves as the page title, og title and search title. Give it a short governed headline with the same meaning. The full sentence stays as the lead.
> 3. Compare presets:
>    - ?records=CLM-001,CLM-054,FMIIP-BASELINE-2025-01 under the "three measures" paragraph;
>    - ?records=CLM-032,CLM-037,CLM-041 from /remittances/.
> 4. Search aliases: «فيندكس» / Findex, and PSP / «مزوّد خدمات الدفع».
> 5. "How numbers are presented": print it once, on /methodology/ and as one link in each domain spine, not as a block under every domain heading.
> 6. Into the roadmap, each with its reason:
>    - the chronology on /reforms/, /payments/ and /remittances/ with an event card variant;
>    - a lighter /ar/data/;
>    - CWR-010 on /payments/.
> 7. In B16, record the judge-then-decide items:
>    - 18_CBY_MONETARY: deferred post-launch (valuation break, CBY-Aden scope, no existing contract fits without design);
>    - the publisher facet: done in B13.
>
> D. WHO PUBLISHES THIS: owner-supplied copy, from CauseWay's institutional profile of September 2026
>
> Add to /about/, section "CauseWay's role", before the funding paragraph, Master-first in both languages. Keep "CauseWay" in Latin script in Arabic (owner rule). Keep the owner-approved funding paragraph byte-identical.
>
> EN: "CauseWay is a Yemeni institutional advisory firm based in Aden (Commercial Registration No. 26666). It works with financial institutions, public institutions and development partners where finance, governance, regulation and implementation meet. Some of those institutions publish evidence used in this resource. That evidence is selected and presented by the method published here, and every record can be checked against its original source and corrected through the published route."
>
> AR: «CauseWay شركة استشارات مؤسسية يمنية مقرّها عدن (سجل تجاري رقم 26666)، تعمل مع المؤسسات المالية والمؤسسات العامة وشركاء التنمية حيث تلتقي المالية والحوكمة والتنظيم والتنفيذ. وتنشر بعض هذه المؤسسات أدلةً يستخدمها هذا المورد؛ وتُختار هذه الأدلة وتُعرض وفق المنهج المنشور هنا، ويمكن التحقق من كل سجل بالرجوع إلى مصدره الأصلي وتصحيحه عبر المسار المنشور.»
>
> The bilingual reviewer checks this pair. Do not add anything else about the organisation.
>
> E. LICENCE
>
> The owner adopts Creative Commons Attribution 4.0 International (CC BY 4.0) for the content CauseWay owns in this resource: its text, analysis, visual designs, the compiled records and the data exports' structure and annotations.
>
> 1. Third-party documents are not hosted. Source data remain under their publishers' terms, and reusers must attribute the original source as the two-line citation shows.
> 2. Write this Master-first on /rights/, in both languages, with the two-line attribution format. Say plainly that the licence does not cover third-party material. Make no claim of rights clearance.
> 3. public_downloads stays false in this pull request. In the runbook, the switch is one step at release, after CauseWay's counsel has confirmed the licence text. When it is switched on:
>    - the downloads publish;
>    - the exports carry the licence;
>    - Dataset structured data may then be added (REJ-03 lifts).
>    Prepare that structured data behind the same switch now if it is cheap, or put it in the roadmap.
> 4. Remove "the licence decision" from the owner's open list, and replace it with "counsel confirms the CC BY 4.0 text".
>
> F. CONTACT
>
> The resource prints office@causewaygrp.com, while CauseWay's institutional profile prints info@causewaygrp.com. Keep office@causewaygrp.com unless the repository records the owner choosing another address. Use one address on every surface. In the final report, list "confirm the corrections inbox is monitored and has a named responder" as a release step for the owner.
>
> G0. PRESENTATION PASS (before B17)
> After the items above, open these pages in a browser:
> - Home;
> - the eight domain pages;
> - one Evidence Record;
> - /about/.
> View each at 390 px in Arabic and at 1440 px in English, and read them as a first-time reader. Fix, inside the accepted D7 design:
> - what such a reader would stumble on;
> - what reads as a wall of caveats before the answer;
> - anything misaligned, cramped or unclear.
> Record each fix in PRODUCT_CHALLENGE.md. Do not redesign, and do not add pages.
>
> G. FINISH
>
> 1. Then: B16, B17 and the final report. The report lists every owner decision above and ends with the brief's exact last line.
> 2. Budget rule:
>    - one independent bilingual reviewer per transaction;
>    - the adversarial reviewer only for names, regulatory statements and new numbers;
>    - batch the work.
> 3. If your context runs low, push and write the RESUME POINT. If the usage limit comes close, stop at a clean point.
> 4. After every push, add a progress line and a provisional RESUME POINT to the PR description.

**How this session reads it.**
- **Steward designation (A.3).** Unchanged from 09:05, and recorded above.
- **Superseded at 09:05:**
  - point 6: exports are now governed by section E;
  - point 7: the organisation description is now governed by section D.
- **"Do not add anything else about the organisation" (D).** This session adds only the owner's pair. No heading or
  other copy about CauseWay is written.
- **One truth change to the owner's copy in D, made by this session as editor-in-chief.** The hostile reviewer showed
  that "every record can be checked against its original source" is not true of every record. Seventeen public
  records have no single original source: one framing record has none, and the composite and partly resolved records
  name several. /about/ itself says records name their source "wherever that source can be named publicly". The phrase
  now reads "against the sources it names" / «بالرجوع إلى المصادر التي يسمّيها». Every other word of the pair is the
  owner's, byte for byte, and the funding paragraph is untouched.
