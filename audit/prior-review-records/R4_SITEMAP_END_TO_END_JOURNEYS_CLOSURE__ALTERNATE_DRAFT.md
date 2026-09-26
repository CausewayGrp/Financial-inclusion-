# R4 closure — Sitemap + end-to-end journeys

## Decision frame

R4 treated the current repository as the product being finalized, not as a prompt for a new architecture exercise. The Production Master and current Page Specs were re-read as the authority boundary:

- Production Master SHA-256: `3d19c7f3249138aec7d7211027d38a0af34b5443fb0cd40c835b3cb79029e2ea`
- Page Specs SHA-256: `9b12fa08dcbde46ea3d772c417d38a793b781a4d0b7c31321de81c7d5a7dc86d`
- Controlled routes: 141
- R4 made **no semantic/evidence/source/rights/publication change** and therefore did not modify the Production Master or Page Specs.

Owner: information architect. Challenger lenses: journalist/researcher; regulator/technical user.

## What R4 asked

For every controlled route:

1. What unique user job would be lost if this route disappeared?
2. How can a user enter it without already knowing the repository taxonomy?
3. What is the correct first depth for a non-expert and the deeper verification path for an expert?
4. What is the meaningful next action?
5. Does a deep link let the user backtrack?
6. Does the route preserve the semantic firewall rather than creating a shortcut that changes meaning?
7. Is apparent duplication true duplication, or a necessary distinction between discovery, answer, synthesis and verification?

## Counterfactual deletion result

**No controlled route was deleted in R4.** This was a reasoned result, not a default keep-all decision.

The route set resolves into 11 user-facing page families:

| Page family | Routes | Unique job |
|---|---:|---|
| Orientation | 1 | Explain the system and let the user start without knowing taxonomy. |
| Question Entry | 1 | Preserve the complete 11-question entry map. |
| Domain Answer | 8 | Answer bounded financial-inclusion questions before verification depth. |
| Evidence Directory | 1 | Discover public verification records. |
| Evidence Record | 108 | Stable public verification/citation endpoint for one controlled object. |
| Comparison | 1 | Test comparability before comparing values. |
| Reading Index | 1 | Discover bounded analytical synthesis. |
| Reading | 10 | Preserve a distinct evidence-bound analytical thesis and its limits. |
| Data & Source | 1 | Find public source/data records and their evidence dependents. |
| Measurement | 1 | Connect consequential unknowns to decision-relevant measurement needs. |
| Reference / Trust | 8 | Purpose, method and distinct public trust/reuse obligations. |

Deleting an Evidence Record merely because it is not a prominent navigation destination would destroy stable verification value. Deleting a Reading would destroy a bounded synthesis object. Merging Privacy, Rights, Terms, Corrections, Contact or Accessibility would blur different public obligations. The correct R4 intervention was therefore **wayfinding repair, not route destruction**.

## Material defects found and fixed

### 1. Privacy, Rights and Terms were effectively search-only

The routes existed and were indexed, but the static product had no ordinary internal inbound link to them. This is unacceptable for trust/reuse pages.

**Fix:** the footer is now contract-driven and grouped into:
- Explore and verify;
- Method and measurement;
- Trust and responsible use.

Privacy, Rights, Terms, Accessibility, Corrections and Contact are now directly discoverable in both Arabic and English without expanding the six-item global header.

### 2. Reading detail pages told the user to trace the analysis but did not provide the trace

The ten Reading pages had governed claim/evidence bindings, yet their public pages did not link those bindings to the corresponding Evidence Record routes.

**Fix:** each Reading now has a visible **Verify this reading / تحقّق من هذه القراءة** bridge generated from its governed verification bindings. Across the ten Readings, 29 claim bindings now resolve directly to controlled Evidence Record routes. When a Reading binds more than one claim, the user is also offered the Compare surface.

No claim, title, value or inference was rewritten.

### 3. Deep Evidence/Reading links lacked first-screen backtracking

Search, citation and external sharing can land a user directly on one of 108 Evidence Records or 10 Reading details.

**Fix:** both families now render a compact accessible breadcrumb back to Evidence or Readings while preserving the stable ID.

### 4. The handoff already referred to a navigation contract that did not exist

`handoff/MASTER_IMPLEMENTATION_PROMPT.md` instructed Claude Design to read `site-src/content/content/navigation_interaction.json`, but that file was absent.

**Fix:** R4 created that file as a build-bound, explicitly non-semantic `NAVIGATION_AND_INTERACTION_ONLY` contract. It covers all 141 routes exactly once and records:
- global navigation;
- grouped footer navigation;
- utilities;
- breadcrumb behavior;
- 11 page families;
- route entry modes;
- unique-value role;
- next-action policy;
- route deletion disposition;
- 12 end-to-end journey tests;
- 5 bilingual search smoke tests;
- accepted/rejected legacy IA lessons.

The current Python renderer now consumes this contract for global/footer navigation, so it is not another unused control document.

## Route discovery result

After the fixes, Privacy, Rights and Terms are no longer search-only. Twelve Evidence Records remain intentionally search/deep-link-only in the static link graph:

- `/evidence/VIS-BORROWING-SOURCES-2014/`
- `/evidence/VIS-DOMESTIC-REMITTANCE-PATH-2014/`
- `/evidence/VIS-FINDEX-ACCESS-USE/`
- `/evidence/VIS-FINDEX-BARRIERS/`
- `/evidence/VIS-FINDEX-FLOW-CHANNELS/`
- `/evidence/VIS-FINDEX-OBSERVED-WAVES/`
- `/evidence/VIS-FINDEX-RESILIENCE/`
- `/evidence/VIS-INCLUSION-TRANSMISSION/`
- `/evidence/VIS-MFI-2014-PANEL/`
- `/evidence/VIS-MFI-RUPTURE-LENS/`
- `/evidence/VIS-MFI-SPINE/`
- `/evidence/VIS-PROVIDER-TIME/`

These are stable visual Evidence Record endpoints. They remain in the public search index and retain verification/citation value, but the accepted presentation does not force all governed visuals onto primary pages. R4 therefore records their non-prominence as intentional rather than manufacturing navigation just to eliminate an orphan count.

## End-to-end journey acceptance

The generated product was tested through 12 explicit jobs:

1. first-time public reader: Home → Explore → People → `CLM-001`;
2. journalist verifying 11.9%: Search → `CLM-001` → Data/source;
3. journalist challenging a Reading: Gender Reading → `CLM-002` → Data/source;
4. researcher: Evidence → Compare → selected Evidence Record actions;
5. senior regulator: Home → Explore → Reforms → `CLM-011`;
6. payments technical analyst: Payments → `CLM-003` → Data/source;
7. provider/financial institution: Explore → Providers → `CLM-009`;
8. development-partner analyst: People → `CLM-001` → Methodology;
9. humanitarian/social-protection practitioner: Explore → Remittances → `CLM-007` → Data/source;
10. user challenging a record: Evidence Record → Corrections → Contact;
11. researcher/journalist checking reuse: Data → Rights → Terms;
12. accessibility user: Accessibility → Contact.

Every explicit path edge exists in the generated HTML after R4.

Search smoke tests also passed in English and Arabic for stable ID, population measure, POS, gender-gap and same-year-remittance queries.

## Legacy/reference challenge

R4 did not mine legacy material for facts. It used only items already dispositioned as `DEFERRED_DESIGN_INPUT` to challenge interaction design.

Accepted lessons:
- human-centered task framing is valuable when it routes into controlled evidence;
- question-first entry and progressive depth are stronger than route taxonomy;
- deep verification/editorial pages need explicit backtracking and evidence paths;
- the footer should group product, method/measurement and trust/reuse links.

Explicitly rejected:
- a citizen/expert toggle that could create two fact systems;
- legacy calculators or practical advice built on uncontrolled assumptions;
- old 29-route architecture;
- universal four-KPI page templates;
- old branding, typography and palette;
- archive factual propositions.

The existing S06 source-owner dispositions remain closed; R4 did not reopen evidence candidates.

## What became more true

- Every one of the 141 controlled routes now has an explicit unique-value role, intended entry mode and next-action policy.
- Trust/reuse obligations are discoverable without bloating global navigation.
- Reading synthesis now closes visibly back to the Evidence Records it relies on.
- Deep-link users can tell where they are and move back into the verification system.
- Claude Design now receives the navigation file its own launch prompt already expected.

## What became more usable or simpler

- Global navigation remains the same six items.
- The footer is no longer an unexplained flat list.
- Reading verification no longer requires search rediscovery.
- No audience-specific menu or parallel fact system was added.
- Hard-coded header/footer route lists were replaced by one non-semantic contract consumed by the build.

## New complexity introduced

One new subordinate file, `site-src/content/content/navigation_interaction.json`, now exists. The complexity is justified because it replaces implicit/hard-coded route behavior and is already a required design-handoff input. It is explicitly barred from changing semantic truth.

## What can now be removed or retired

- hard-coded header/footer navigation maps in the legacy renderer are no longer the navigation authority;
- the idea of creating separate citizen/expert route systems remains rejected;
- Privacy/Rights/Terms no longer depend on search as their only internal discovery path.

No controlled public route is removed.

## Files changed

- `site-src/content/content/navigation_interaction.json` — new build-bound R4 contract
- `scripts/build.py` — consumes navigation contract; grouped footer; breadcrumbs; Reading → Evidence verification; route next actions
- `site-src/styles.css` — R4 wayfinding component styles and responsive behavior
- `scripts/validate.py` — 141-route coverage, discovery, breadcrumb, Reading verification, journey/search acceptance
- `handoff/IMPLEMENTATION_MANIFEST.json` — records navigation contract
- `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` — binds designer to current journey contract without semantic authority
- `handoff/CLAUDE_CODE_MASTER_PROMPT.md` — adds navigation contract to implementation read order
- `README.md` — current finalization marker
- `audit/FINALIZATION_PROGRAM.md` — current state marker advanced to R4 closed / R5 next
- `audit/R4_SITEMAP_END_TO_END_JOURNEYS_CLOSURE.md` — this closure

## Verification

- Production Master unchanged: `3d19c7f3249138aec7d7211027d38a0af34b5443fb0cd40c835b3cb79029e2ea`
- Page Specs unchanged: `9b12fa08dcbde46ea3d772c417d38a793b781a4d0b7c31321de81c7d5a7dc86d`
- Navigation route matrix: 141/141
- Reading direct verification bindings rendered: 29
- Generated HTML: 284
- Validator: `ERRORS=0`, `WARN=0`
- Result: `WEBSITE REPOSITORY VALIDATION PASS`

## Next bounded session

**R5 — Evidence utilization + synthesis.**

R5 will not perform another broad research sweep. It will ask a different question: whether the evidence already admitted to the Production Master is being used, held or omitted for a defensible reason across public answers, Readings, visuals and Measurement Agenda — and whether any object is overused, underused, misused or stranded. Any material semantic issue found in R5 will be repaired in the Production Master first.
