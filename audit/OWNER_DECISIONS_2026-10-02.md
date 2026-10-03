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


## Owner note of 3 October 2026, about 11:15 Cairo (replaces every owner note not yet sent)

Received in this session as a chat message on 3 October 2026; recorded verbatim.

> OWNER NOTE, 3 October 2026, about 11:15 Cairo. This replaces every owner note I have not yet sent. Record it verbatim, append-only, in audit/OWNER_DECISIONS_2026-10-02.md.
>
> 0. BEFORE ANYTHING ELSE
> The last push I can see is b49fe93 (RC-16). Your RESUME POINT says the B16 generator and a sub-item audit live only in the session. Ask yourself what would be lost if this session ended now. If the answer is more than an hour of work, make it safe and push it first.
>
> 1. WHAT THIS IS FOR, AND THE ONE TEST I WANT YOU TO APPLY
> This resource will carry CauseWay's name in public. It succeeds if four people trust it and use it:
> - a Yemeni citizen reading Arabic on a phone;
> - a journalist on deadline;
> - a central-bank supervisor checking line by line;
> - a researcher citing it.
>
> Before you spend effort on anything, in this note or of your own, ask:
> - If this is done, will one of those four understand or trust something they could not before?
> - Can it be verified against an original?
> - Can it be finished and checked inside this pull request?
>
> If all three answers are yes, do it well. If the value is real but it cannot be finished safely here, it belongs to the next edition (section 6). If the value is not real, drop it and say so in one line. That includes my suggestions: tell me which of them you rejected, and why.
>
> You lead. Where this note says DECIDED, it is settled. Everything else is a finding from my own look at the built site, to verify and judge.
>
> 2. FIRST REPLY: A TRIAGE, THEN ACT
> Before building, write a short triage in the PR description, one line per item in sections 4 and 5:
> - reader value;
> - cost;
> - risk;
> - your decision (build here, next edition, or reject);
> - one line of reasoning.
> Then carry on without waiting for me. I will read it and step in only if I disagree. Keep it short; it is a plan, not a report.
>
> 3. DECIDED BY THE OWNER
>
> 3.1 Withheld names
> - public_use of PSE-006, PSE-007, PSE-010, PSE-013 and PSE-014 follows the withholding rule, Master-first.
> - No name from the 2024 e-wallet circular is published, including "We Cash" (NEG-EW-011), for three reasons: consistency with the enforcement rule, fairness to the other eleven, and not presenting a June 2024 status in 2026.
>   - NEG-EW-011 keeps its ID, route, counts, date boundary, limits and CBY link, as one service among twelve. The name stays non-public lineage in the Master.
>   - RC-NAMES must prove that no such name prints anywhere, including search, social images and figures.
>   - The search empty state gets one governed sentence: entity names from the regulator's lists and enforcement decisions are not reproduced here, and the originals are linked from Data & sources.
>   - The earlier instruction that "We Cash" ranks first in search is withdrawn.
>
> 3.2 Phone menu
> - You are steward for one patch to navigation_interaction.json (the EAD-11 precedent): the trust links (About first) and the existing "Cite this page" go inside the opened mobile menu.
> - Use existing labels only, and change nothing else in that file.
>
> 3.3 Release address
> - https://causewaygrp.com/financial-inclusion-evidence/, with Arabic at that root and English under /en/.
> - The whole site must work unchanged under that path, including search, citation, share, canonical, hreflang, og:url, sitemap, the 404 page, the language switch and the header and cache rules in _headers.
> - With public_origin null, the build is byte-identical.
> - A gate with a negative control proves that nothing escapes the path.
> - Every page carries noindex until release.
> - Do not set public_origin.
>
> 3.4 Runbook
> - Facts observed on 3 October:
>   - causewaygrp.com uses DigitalOcean name servers;
>   - it is a Nuxt application;
>   - it sets a "session" cookie on Path=/;
>   - it sends x-robots-tag: index, follow.
> - Routes, in order: Cloudflare Pages proxied by a Nitro routeRules rule in CauseWay's Nuxt site (a later task in that repository); a DigitalOcean App Platform static component, only if our headers survive; evidence.causewaygrp.com with a 301 from the subpath.
> - For each route: how our headers survive; that the corporate robots header, scripts and cookies never reach our responses; and how rollback works.
> - /privacy/ stays true. If the domain cookie can reach these pages, one governed sentence says it is set by causewaygrp.com and not read by this resource.
>
> 3.5 /about/, "CauseWay's role", before the funding paragraph, Master-first
> - Keep the funding paragraph byte-identical.
> - Write "CauseWay" in Latin script in Arabic.
> - The bilingual reviewer checks the pair.
>
> EN: "CauseWay is a Yemeni institutional advisory firm based in Aden (Commercial Registration No. 26666). It works with financial institutions, public institutions and development partners where finance, governance, regulation and implementation meet. Some of those institutions publish evidence used in this resource. That evidence is selected and presented by the method published here, and every record can be checked against its original source and corrected through the published route."
>
> AR: «CauseWay شركة استشارات مؤسسية يمنية مقرّها عدن (سجل تجاري رقم 26666)، تعمل مع المؤسسات المالية والمؤسسات العامة وشركاء التنمية حيث تلتقي المالية والحوكمة والتنظيم والتنفيذ. وتنشر بعض هذه المؤسسات أدلةً يستخدمها هذا المورد؛ وتُختار هذه الأدلة وتُعرض وفق المنهج المنشور هنا، ويمكن التحقق من كل سجل بالرجوع إلى مصدره الأصلي وتصحيحه عبر المسار المنشور.»
>
> 3.6 Licence
> - CC BY 4.0 covers the content CauseWay owns: text, analysis, visual designs, the compiled records, and the structure and annotations of the exports.
> - Third-party documents are not hosted. Source data stay under their publishers' terms, attributed as the two-line citation shows.
> - On /rights/, Master-first in both languages: the licence does not cover third-party material, and there is no claim of rights clearance.
> - public_downloads stays false. Switching it on is one release step, after CauseWay's counsel confirms the text. Dataset structured data may then follow (REJ-03 lifts); prepare it behind the same switch only if it is cheap.
> - The owner's open item becomes "counsel confirms the CC BY 4.0 text".
>
> 3.7 Contact
> - office@causewaygrp.com on every surface.
> - Release step for the owner: the corrections inbox has a named responder.
>
> 3.8 Logo
> - The canonical logo, with «كوزواي» beneath "CauseWay", stays unchanged.
> - The text rule (Latin script) stays.
>
> 3.9 Dispositions
> - Domain strip: roadmap.
> - VIS-MFI-SPINE table: post-launch.
> - 18_CBY_MONETARY: post-launch.
>
> 4. WHAT I SAW ON THE BUILT SITE: verify, triage, act
>
> 4.1 The figure is hidden in a sentence. This is the largest gain I see for a first-time reader.
> - At 390 px in Arabic, Home's first screen is a nine-line description with no figure. 11.9% first appears near the end of a long sentence on the second screen.
> - Record pages hold their value inside prose, with no key-facts line at the top.
> - Most of the owner's early mockups led with the figure, and several of them invented it. The right answer is neither: show the figure large together with its unit, population, period and evidence type, all from governed fields, and keep the governed sentence beneath it.
> - The test is the cropped screenshot: the block alone must still say who, when and within what scope.
> - Judge whether this can be built inside the accepted D7 design for Home's three figures and as a key-facts line on every Evidence Record. If it can, it is worth more than any other single change left.
>
> 4.2 Small items with clear reader value
> - /reforms/ describes Decision No. 23 of 2024 and Decision No. 4 of 2025 without their numbers. Compliance officers search by number.
> - The "Rules, decisions and official lists" group on /data/ has no anchor for "Verify it yourself" to land on.
> - The /payments/ headline is 36 words long, and it doubles as the page, og and search title. A short governed headline should keep the same meaning, with the full sentence as the lead.
> - Compare presets, for the comparisons readers most often get wrong:
>   - CLM-001, CLM-054 and FMIIP-BASELINE-2025-01, under the "three measures" paragraph;
>   - CLM-032, CLM-037 and CLM-041, from /remittances/.
> - Search aliases:
>   - «فيندكس»/Findex and PSP/«مزوّد خدمات الدفع»;
>   - the words citizens actually type: «حوالة»، «تحويل للخارج»، «محفظة»، «كاش»، «صرافة»، «قرض». Check where each lands.
> - /measurement/: each priority's dimensions_en and dimensions_ar are governed but not printed. Funders and statisticians need them.
> - /corrections/: source institutions are not explicitly invited to request a correction. Proposed pair:
>   - EN: "Institutions whose documents or data are used in this resource can request a correction to any record through the same route."
>   - AR: «يمكن للمؤسسات التي تُستخدم وثائقها أو بياناتها في هذا المورد أن تطلب تصحيح أي سجل عبر المسار نفسه.»
> - Home section 05 describes the rule-to-result chain, but its evidence link opens a text record about the system's parts. The drawn chain exists on /reforms/.
>
> 4.3 The three Findex waves
> - The 2011 (3.7%, financial-institution accounts only), 2014 (6.4%) and 2022 (11.9%) observations are governed. Yet they appear nowhere as a drawing, and RV-CWR-004's people lane starts in 2022. I could not find the reason recorded.
> - If the reason is the early "zero new visual contracts" rule, say what that rule protects today. Would one narrow form protect the same thing: observed points, no connecting line, the 2011 definition break marked, the coverage exclusion on the 2022 point?
> - Decide, and record the reasoning where a reviewer will find it.
>
> 4.4 Visual contracts that render as text
> - On the English pages I count 9 drawn, 8 tables and 18 text-only. B12 named each missing input, and that discipline is right.
> - Are there one or two whose missing input is only governed bilingual labels, which are writing rather than new facts? Two possibilities: the rung labels of VIS-FL-EVIDENCE-LADDER, whose OECD values are already bound; the chain mapping of RV-CWR-010.
> - If drawing them would change understanding and fits in this pull request, build them. If not, they go to the next edition.
>
> 4.5 Hosting readiness: think as the engineer who will be paged after launch
> - There is no favicon. The 32 px logo derivative exists.
> - dist/assets/CauseWay_Master_Logo.png is 9.6 MB, ships, and no page references it.
> - The runbook needs a one-page "deploy and verify" section: prerequisites, commands, expected outputs, a ten-minute post-deploy check (headers, three URLs per language, noindex before release and gone after, sitemap, 404) and rollback. Someone who has never seen this repository should succeed from it alone.
> - Add anything else you would want before a stranger hosts this.
>
> 4.6 Records that would mislead the next reader
> - In OPENAI_REENTRY_CHECKPOINT.md §7, the tag message for checkpoint/design-handoff-ready says "Master e24fe737…". The Master at that commit is 17db032b15da16fc4b5b3c3b49f19aebf2ecb4ec46634613fe8505d0f038690b. I will run that command, so correct it.
> - README.md is behind the branch in several places: the transaction count, EXT-01/02/03, the EAD and Design-state blocks, OWN-01/02/05, six merged branches not five, the third CI job, deploy.yml, the runbook, and the start file that disagrees with AGENTS.md.
> - YFI_CURRENT_PROJECT_CONTEXT.json still names pull request #8 as the runtime.
> - Verify each point; they came from a reviewer. Fix them in one records commit near the end.
>
> 5. EVIDENCE THE MASTER HOLDS THAT NO PAGE SHOWS: a judgement, not an expansion of this pull request
> - Across the Master's XML I count these terms: "correspondent" (18 occurrences), "de-risk" (4), "SWIFT" (11), "liquidity" (86), "hawala" (55), "G2P" (48) and "guarantee" (29). "Correspondent" appears on no English page. Correspondent banking is central to how remittances and trade payments reach Yemen.
> - In B16, give one line per topic:
>   - Is the material source-bound?
>   - Is it within the resource's stated scope?
>   - Would a reader of /remittances/ or /payments/ be misled by its absence?
>   - Your disposition: publish now (only if already governed and quick), next edition (with its missing input), or out of scope (with the reason).
>
> 6. THE NEXT EDITION: use everything under one eye
> In the final report, add a ranked plan for the next edition. It should cover what the evidence base could truthfully support that the site does not yet show, ranked by value to the four readers. Draw on the Master's unpublished sheets and topics, the four origin tables that are not Master sheets, the 17 text-only contracts, the provider matrix, the microfinance spine, the regulatory stage table, and the plain-language entry for citizens.
>
> The owner also holds material outside the repository: a literature review, a qualitative evidence register, verification notes on MSME guarantees and on the OECD 2026 regulatory review, research reports, and evidence registers on providers, wallets, payment rails, donors' projects and regulatory chronology. Tell me which kinds of material would most strengthen the next edition, and how each would enter: original source, verification, Master, then page. I will supply them.
>
> 7. WHAT "RELEASE CANDIDATE" MEANS HERE
> It is the build we would publish unchanged if the independent review finds nothing:
> - no known truth defect;
> - every public number traced to its record and its original;
> - the names rule enforced by a gate;
> - the four readers' main tasks succeed on a phone in Arabic and on a desktop in English, judged by looking;
> - Arabic and English carry the same meaning;
> - the build works under the real address, with headers, noindex, sitemap, 404 and page weight in order;
> - a stranger can deploy, verify and roll back from the runbook;
> - the records tell the truth;
> - every item is DONE, NEXT EDITION or REJECTED, with its reason;
> - CI is green on all three jobs;
> - the owner is left with merge, hosting, counsel, the inbox, and tag and sign.
> If something on this list cannot be met here, say so plainly. Do not stretch the definition.
>
> 8. ORDER AND FINISH
> I would work in this order. Change it if you see better.
> 1. Make the work safe (0), then the triage (2).
> 2. The decided items a release cannot ship without (3.1–3.6).
> 3. 4.1, then 4.2 in one transaction.
> 4. 4.3 and 4.4, by your judgement.
> 5. 4.5 and the runbook.
> 6. 4.6 in one records commit.
> 7. B16 (including section 5).
> 8. G0: read Home, the eight domain pages, one record and /about/ at 390 px in Arabic and 1440 px in English, as a first-time reader, and fix what they would stumble on, inside D7.
> 9. B17.
>
> The final report:
> - lists every owner decision here;
> - answers 4.1–4.6 and section 5;
> - judges the branch against section 7;
> - gives the next-edition plan (section 6);
> - says honestly what you would do differently if you began this pull request again;
> - ends with the brief's exact last line.
>
> Budget:
> - one independent bilingual reviewer per transaction;
> - the adversarial reviewer only for names, regulatory statements and new numbers;
> - batch your transactions and pushes (CI now uses the account's minutes).
> If your context or usage runs low, stop at a clean point, push, and write the RESUME POINT. After every push, add a progress line and a provisional RESUME POINT to the PR description.

**How this session reads it.**
- **Section 0.** The owner wrote that the last push visible to them was `b49fe93`. When the note arrived, the branch
  had already been pushed to `ab380cf`: RC-17, the steward patch and the C5 batch. What lived only in the session was:
  - the B16 generator and its inputs;
  - the menu and presentation-pass check scripts;
  - the base-path worktree.
  The first two are committed and pushed at once (`audit/release_candidate/b16/`, `audit/release_candidate/checks/`).
  The worktree's commits enter the branch when its adversarial verification ends.
- **Section 3 (DECIDED).**
  - 3.1, 3.2, 3.5, 3.6 and 3.7 were built in RC-17 (`a4ff911`), the steward patch (`88a0f86`) and `ab380cf`.
  - 3.3 and 3.4 are the base-path work.
  - 3.8 and 3.9 stand as written.
- **3.5, flagged to the owner.** The owner's pair is printed as written, except one phrase that the RC-17 hostile
  review showed to be untrue for seventeen records: "against its original source" reads "against the sources it names"
  / «بالرجوع إلى المصادر التي يسمّيها». The note's own test puts truth first ("never believing something the evidence
  does not support"), so the change stands. If the owner wants the original words, it is one cell in one transaction.
- **Sections 4 and 5.** The triage is in the pull request description, as asked in section 2.


## Owner note of 3 October 2026, 13:00 Cairo (changes no decision)

Received in this session as a chat message on 3 October 2026; recorded verbatim.



**How this session reads it.**
- **Point 1 (CI).** The controls job runs every fault on its own full copy of the work tree, one copy per CPU, inside
  the single job "Gate negative controls". That keeps the job's name, so the required status check does not change,
  and it adds no runner minutes for extra jobs. `--shard K/N` also exists, for a job matrix if the controls ever
  outgrow one runner. Nothing is weakened:
  - every control still runs;
  - each must still fail on its own fault;
  - the clean copies must now also pass first, and a control's expected message must not already appear in the clean
    output, which the old harness never checked.
  The proof, locally and then on CI, is in `docs/CHANGELOG.md` and the pull-request log.
- **Point 2 (base path).** The adversarial verification of `code/base-path-hosting` did return, after this note was
  written (`audit/release_candidate/` records it with the base-path merge). Its verdict:
  - the build side is sound: `dist/` stays byte-identical apart from the noindex meta; there are no escapes; the
    gate's controls fail as they should;
  - the hosting runbook was not ready, and its findings are folded in before the merge.
  The branch then enters `code/release-candidate-fixes` as its own two commits. No branch is deleted.
- **Point 3.**
  - **/about/.** The owner accepts the /about/ change of RC-17 ("against the sources it names" / «بالرجوع إلى المصادر
    التي يسمّيها»). It stands as built in `a4ff911`.
  - **providers_data.json.** Confirmed in `docs/CHANGELOG.md` (the entry for the controls commit): what the file is,
    who reads it, and why it never reaches `dist/`. Three new negative controls prove that RC-NAMES fails if a
    renderer printed the NEG-EW-011 label in either language, or if the projection were copied into the site.
- **Point 4.** Reviews are sized as asked:
  - one bilingual reviewer per transaction, reading only the changed pairs;
  - the adversarial reviewer only for names, regulatory statements and new numbers.
  The G0 presentation pass is done in the browser by this session.

## Owner decisions of 3 October 2026, 22:36 Aden (hosting; Findex observed waves)

Received in this session within the owner's execution brief for finishing pull request #9; the two owner statements it
carries are recorded here, and nothing else from the brief.

**1. Hosting.** Production hosting is DigitalOcean, under CauseWay's domain, at
`https://causewaygrp.com/financial-inclusion-evidence/`. This replaces the runbook's earlier preference order, in which
Cloudflare Pages came first. The release conditions do not change: our security headers, cache rules, 404, redirects
and noindex-until-release must be provable on that platform; the corporate cookie, `X-Robots-Tag` and `X-Powered-By`
must never reach our responses; rollback must be defined. No credential, DNS state or deployment is to be invented.

**2. Findex observed waves (open item 4.3).** The owner permits, and does not require, showing the three observations
— 2011, 3.7%, financial-institution accounts only; 2014, 6.4%; the 2021 wave (World Bank data year 2022), 11.9% in
the areas surveyed — as rows of an existing contract such as RV-CWR-004's people lane, with the definition change
marked and no connecting line.

**How this session reads it.**
- **Point 1.** Applied in `docs/RELEASE_RUNBOOK.md` ("Hosting", route 1), `.github/workflows/deploy.yml`,
  `scripts/hosting_nginx.py`, `site-src/hosting/digitalocean/` and `scripts/tests/test_digitalocean_hosting.py`; the
  reasoning and what the owner still supplies are in the runbook and the pull request.
- **Point 2.** A permission, not an instruction: it is used only if an existing contract takes those rows without a new
  visual family, new Design work or a widened meaning. The disposition is in
  `audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`.
