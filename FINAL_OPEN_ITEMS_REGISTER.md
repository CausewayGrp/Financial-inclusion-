# Final open-items register

Every item that remains open at the Design handoff, in exactly one class, with where it shows today, what would close it
and who owns it. **There are zero `DESIGN_BLOCKER` items**: each item below is either stated honestly on the page it
affects, part of the scope Design and Code already receive, or needed only for public release.

- **State:** final at the R8.6 clean-room acceptance (directive D7 §F9), 26 September 2026 (full authority hashes in
  `README.md`). Built in F8; F9 added what the cold-recipient test found; the post-F9 correction of 27 September 2026
  closed OWN-07 and OWN-08 (section 8). Later changes are appended, never rewritten.
- **Built from:** a sweep of every audit record that left an item open, deferred, held, carried or release-only (Tranche A
  and B queues, P1–P5, Tranche C, F3, F5, F6, F7), checked against the current repository bytes; 36 items were still
  open, 23 had been closed or superseded later (section 8). F9's three cold-recipient runs (fresh agents with only the
  repository) added EAD-11 and OWN-08, widened EXT-10, and closed ten items (section 8).
- **How Design uses it:** read it once; nothing here asks Design to invent content. Where an item touches a screen, design
  the honest state the page already has (a withheld value, a partial lineage, an undated title) and do not fill it.
- **Class rule:** `ENGINEERING_AFTER_DESIGN` (Design specifies, Code implements after the Design package is accepted) ·
  `RELEASE_ONLY` (needed for a public release, not for design) · `EXTERNAL_EVIDENCE_DEPENDENCY` (needs a source that
  could not be read here; the text stays unchanged until it is) · `KNOWN_EVIDENCE_FRONTIER` (the evidence does not
  establish it; the product says so and must never fill it) · `OWNER_INPUT` (a CauseWay decision or fact; nothing is
  invented to close it) · `REJECTED / NO ACTION` (decided; recorded so nobody reopens it by accident).

| Class | Items |
|---|---|
| ENGINEERING_AFTER_DESIGN | 11 (EAD-01, EAD-04, EAD-05 and EAD-09 closed 2026-09-29; EAD-08 all but its optional subsetting; EAD-02, EAD-06 and EAD-10 at the point where the rest is not Code's) |
| RELEASE_ONLY | 4 |
| EXTERNAL_EVIDENCE_DEPENDENCY | 11 |
| KNOWN_EVIDENCE_FRONTIER | 8 |
| OWNER_INPUT | 6 |
| REJECTED / NO ACTION | 7 |
| **DESIGN_BLOCKER** | **0** |

## 1. ENGINEERING_AFTER_DESIGN

| ID | Item | Where it shows today | What closes it | Owner | Origin |
|---|---|---|---|---|---|
| EAD-01 | One production runtime replaces the reference renderer (`scripts/build.py`), with parity on every gate, then the old renderer is removed | **CLOSED 2026-09-29** — `dist/` is rendered by the accepted design through `scripts/yfie`; `scripts/build.py` is its driver; the replaced composition and `site-src/styles.css` are deleted; `design/reference/` builds through the same package and holds no renderer. Every gate green; parity proved against the frozen pre-design oracle (286 documents, 0 differing); both browser suites unchanged (25/26, 168/168); every re-pointed gate proved to still catch its own fault | `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` §1, §3 met on the new runtime | Claude Code | D7 §F8 |
| EAD-02 | Accessibility audit of the implemented site against WCAG 2.2 (automated and manual; keyboard; Arabic and English screen readers; 200 % and 400 % zoom; forced colours; reduced motion; images off), including the text-alternative table for every drawn visual | **CODE'S HALF DONE 2026-09-29; THE AUDITOR'S HALF IS NOT.** `scripts/accessibility_audit.py` audits the implemented site — 24 pages (one per route class, both languages) at 1440 and 390 px, a 320 px reflow pass (400 % of 1280 px), reduced motion, images off and a keyboard walk — with a pinned general ruleset (axe-core, WCAG 2.0/2.1/2.2 A and AA plus best practice) and the contract's own eleven outcomes measured rather than asserted. Record: `docs/ACCESSIBILITY_AUDIT.md` and `.json`, including the text-alternative table for every drawn visual. **Result: 0 WCAG violations from the ruleset, 0 contrast failures, 0 targets failing 2.5.8, 0 unnamed controls or landmarks, 0 unlabelled controls, 0 reflow overflow, 0 heading-level jumps, 0 images without `alt`, no keyboard trap.** Two real failures were found and fixed (1.4.3: the band's fine print at 4.42:1, the token two points darker; 2.5.8: twelve targets 1–2 px short, the design's own `min-height` rule extended to the three families it had missed). Two best-practice findings are recorded and escalated, not fixed: two landmarks sharing a governed name, and a figure table's empty corner cell (DEBT-013's recorded preference). **No conformance is claimed and the Accessibility page states no result**: screen readers in Arabic and English, and every judgement about meaning, are listed as outstanding for the auditor | An audit record; only then may the Accessibility page state a result | Claude Code, then an auditor | PB-0400, F6 §3 |
| EAD-03 | Web-size derivatives of the 10,018,081-byte master logo (6250 × 6250 px), by exact downscaling of the unmodified file | **BLOCKED ON THE OWNER'S APPROVAL, AND NOW MEASURED ON THE IMPLEMENTED SITE.** Every page loads the master PNG: **94–97 % of every cold page** of the runtime (`docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`, 29 September 2026), against 285–656 KB for everything else on the page together. The sizes are listed in `design/08_ASSET_MAP.md` §1 and the export is one command; Code does not run it, because a derivative of the mark is the owner's to approve and the master is never redrawn, recoloured, cropped or regenerated | Sizes listed by Design in `design/08_ASSET_MAP.md`; exported by Code with the owner's approval; master file unchanged | Design (sizes), Code (export), owner (approval) | TOOL-02 |
| EAD-04 | The reference footer whitens the logo with a CSS filter (`brightness(0) invert(1)`), which is a recolouring | **CLOSED 2026-09-29** with EAD-01, by construction: the filter existed only in the pre-design baseline stylesheet, which no longer exists or ships. The accepted stylesheet contains no filter, blend or mask, and the master file is unchanged | The production runtime uses no filter, blend or mask on the logo (Design prompt §8; acceptance criteria I); a reversed version only if the owner supplies one (OWN-06) | Design, Code | F8 |
| EAD-05 | Presentation of the "Method & Measurement" navigation group (the reference header wraps it as a ragged inline row with a non-link label) | **CLOSED 2026-09-29** — Design decided it and the production runtime ships that decision: the group is a named `role="group"` whose governed label is a non-link `glabel`, set off from the other destinations by a hairline with its label on the links' baseline at 900 px and above (`09_CODE_HANDOFF.md` "Product bar — GROUP SET OFF"; `05_RESPONSIVE_RTL_LTR.md` ≥ 900), and stacked under a quieter label inside the opened menu below it. Both labels and both destinations are unchanged and governed; the same in Arabic | Design decides grouping and prominence within the fixed labels and destinations (Design prompt §4.2) | Design | TOOL-25 |
| EAD-06 | Tools still to build: entry into Compare from the pages of the 13 comparable records, with that record pre-selected; a mobile form of the four-column comparison; a result-type search facet and a `?q=` URL state (a domain facet needs a governed domain field first) | **THREE OF FOUR DONE 2026-09-29.** Compare entry ships from exactly the 13 comparable records (`data-compare-entry` → `?records=<id>`, honoured by the tool) and the four-column comparison stacks below 640 px — every row a block, each cell numbered in the inline-start gutter — both from the accepted design, so both arrived with EAD-01. The **`?q=` URL state is new**: the Evidence directory's own search writes and reads it, it survives reload and the language switch, clearing the field clears it, and the dialog floating over another page never rewrites that page's address (handoff §1, §2; two browser tests, a gate and two negative controls). **The result-type facet is blocked, not deferred**: the option labels are governed (`UI-JS-TYPE-*`) but the facet's own accessible name and its "all types" state are not, and Code does not author a label — escalated in `design/ESCALATIONS.md`. The search status total ("10 of 79") stays blocked on the governed `{n} of {m}` form escalated at D7 | Designed in `design/` (Design prompt §10), implemented with the 2–4 record URL contract unchanged; new labels requested as `NEEDS_CONTROLLED_CONTENT` | Design, Code | P2-F11, Tranche A A3 |
| EAD-07 | A document-type filter on the source register | **BLOCKED ON CONTROLLED CONTENT, CONFIRMED 2026-09-29 ON THE IMPLEMENTED SITE.** `/data/` still offers the governed text filter only. Of the 151 displayed sources, **142 carry a governed `document_label` and 9 do not**, so a type filter with no group for those nine would hide nine sources the register promises are discoverable — the same wall DEBT-011 hit, and the reason `check_site.py` now asserts `locator_only_source_reachable`. The "type not recorded" group label is not governed and Code does not author one (`design/ESCALATIONS.md`, Anticipated). Everything else the filter needs already exists: the labels are in the projection and the rows are rendered with their types | If designed, it filters by the governed `document_label` / `document_label_ar` only (142 of the 151 displayed sources) and puts the other 9 in a governed "type not recorded" group (Design prompt §10) | Design, Code | P2-F10 |
| EAD-08 | IBM Plex Sans and IBM Plex Sans Arabic self-hosted in the production runtime | **SELF-HOSTED 2026-09-29** with EAD-01: the build ships the six faces the stylesheet declares (three weights per family) with each family's OFL licence, unchanged from `vendor/fonts/`, and preloads the two first-paint faces of the page's language; no font CDN. Open only on the last part — IBM's pre-split Latin subsets are not used, and a self-made subset is an owner decision (the licence reserves the name "Plex") | Design self-hosts them in its reference implementation and Code in production, from `vendor/fonts/` with the licence, files as shipped (the licence reserves the name "Plex"); no font CDN | Design, Code | D7 §F8; F9 |
| EAD-09 | Social images: `og:image` only when Design's per-family templates are generated at build time from governed text | **CLOSED 2026-09-29** — `scripts/social_images.py` rasterises the design's own templates to 286 PNGs at 1200 × 630, one per route and language, from governed text only; `scripts/build.py` copies them into `dist/assets/social/` and every page carries `og:image`, its declared size, `og:image:alt` (the page's own title) and `summary_large_image`. Gate F6-G01 is extended from "no `og:image`" to the positive assertion, and `check_acceptance.py`'s `no_og_image` criterion with it. **Cost the owner should weigh: 17.1 MB of generated PNG, committed.** Rasterising needs a browser, so it cannot run inside the standard-library build; the images are therefore build inputs, regenerated by one documented command and committed like every other output this repository publishes. `--check` rebuilds each template in pure Python and compares its SHA-256, so a governed text change is caught in a second without rendering. To reverse: delete `site-src/assets/social/`, pass `image=False` in `discovery.social_meta`, and restore the two negative assertions | Templates in the Design package; generated at build; gate F6-G01 extended | Design, Code | F6 |
| EAD-10 | Remeasure bytes and requests on the implemented site and on the release host; set budgets only then; no carbon figure or green claim before a named model is applied | **HALF DONE 2026-09-29 — the implemented site is measured; the release host is not, and cannot be.** Same script, same twelve route classes, both languages: `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json` and the comparison table in `docs/SUSTAINABILITY_METHOD.md`. A cold page transfers 9.83–10.19 MB of which **94–97 % is the canonical logo**; everything else together is 285–656 KB; a warm page transfers nothing; Search loads its index once (about 321 KB gzipped); no external request of any kind. The only increase over the pre-design baseline is about 200 KB of self-hosted type (EAD-08) — the baseline named IBM Plex and shipped no font file, so most readers saw a fallback face. The social images cost a page nothing. **No budget is set and no carbon figure is computed**, because the release host is not chosen (OWN-03) and its compression and caching are unmeasured. The rest of this item is release work | `docs/SUSTAINABILITY_METHOD.md` rerun after implementation and after deployment | Code | F7 |
| EAD-11 | Home's four starting questions and Explore's four question clusters (the R8.4A decision) are ID sets held in `scripts/yfie/question_sets.py` (until EAD-01: `scripts/build.py`), not in a governed contract | **Narrowed 2026-09-29, and more urgent than recorded.** Explore's clusters were never governed: `handoff_inventory.py` recovered them by scraping the baseline renderer's HTML out of `dist/`, and the renderer read them back from the inventory — so EAD-01 emptied them and `/explore/` rendered with no questions. They now live in one named place, `scripts/yfie/question_sets.py`, the inventory reads them from there and parses no markup, and the regenerated inventory is byte-identical to the accepted one at `2f9a93c`. What remains is the original item: move the two sets into a governed contract | The production runtime takes the sets from a governed contract (Master or presentation contract), selection unchanged | Code, with the steward | F9 run 2 |

- 2026-10-02 — **Correction to the EAD-01 cell above** (condition C1 of `audit/PR8_INDEPENDENT_ACCEPTANCE.md`): the browser suites
  did not both run unchanged. `scripts/tests/test_public_tools.py` was extended at EAD-06 (commit `8ec2365`) by two tests for the
  `?q=` URL state, no existing test changed, and the measured result is **27/28** (the one permanent data skip), not 25/26;
  `audit/tranche_c/checks/viewport_acceptance.py` is unchanged at 168/168. The cell above is left as written.
- 2026-10-02 — **EAD-03**: the owner approved the export of web-size derivatives by resampling only, the master logo file unchanged
  (`audit/OWNER_DECISIONS_2026-10-02.md`, row EAD-03); applied in the release-candidate pull request. The row above stands until then.
- 2026-10-02 — **Pointer (not an EAD item): every figure prints its boundary twice** — `audit/PR8_INDEPENDENT_ACCEPTANCE.md` A3,
  condition C3. One generator rule (`scripts/projection/derived.py:1324`) ends all 36 contracts' `alt_text` with the prohibited
  inference, and the frame foot prints it again. Owner: the steward. Recorded in full in `design/ESCALATIONS.md` (raised at the
  independent acceptance of pull request #8); decision in `audit/OWNER_DECISIONS_2026-10-02.md`, row A3 / C3; implemented in the
  release-candidate pull request.

- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **EAD-11**: for the release-candidate pull request only, the implementing session is programme steward for
  `site-src/content/presentation_priority.json`, limited to the EAD-11 patch recorded in `design/ESCALATIONS.md` (row Steward); applied in that pull request.
- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **D7** (not a register item; recorded here because §1 is the Design → Code section): the owner records final D7 visual
  acceptance of the Design package on 2 October 2026 (row D7). Also recorded there: A3 / C3 (the double boundary) and A5 / C4 (the
  retired frame on `/reforms/`), both implemented in the release-candidate pull request.
- 2026-10-02 — **EAD-12, method text** (release candidate B1; owner decision A4 / C6 revised, addendum of 2 October 2026):
  the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY` record pages now print their governed method text in both languages (each read
  as reader-facing method; none withheld); validator PB-0401 now requires it, with a negative control. Table rows for the
  13 stay post-launch; B16 records the disposition.
- 2026-10-02 — **EAD-03 done** (release candidate G4 item 2): eight web-size derivatives, pure Lanczos resamples of the
  unchanged master (`scripts/logo_derivatives.py`, `--check` in CI), served with `srcset` on every surface of
  `design/08_ASSET_MAP.md` §1 except the offline social-image template (the 286 images unchanged). Cold page weight
  10.31–10.71 MB → 0.30–0.69 MB (`audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md`). DEBT-016 closed. B16 records it.
- 2026-10-02 — **EAD-11 landed** (release candidate G3): the two entries recorded under EAD-11 in `design/ESCALATIONS.md`,
  values unchanged, are in `site-src/content/presentation_priority.json` under `question_sets` (installed through the runner);
  the renderer and the handoff inventory read them there, the generator rejects an unknown question or heading, a missing
  question or a repeated one (unit test `test_question_sets_guards`), and `scripts/yfie/question_sets.py` is deleted. The
  built Home and Explore pages are byte-identical before and after in both languages, as is the handoff inventory
  (`audit/release_candidate/runs/G3-EAD-11_RUN_REPORT.json`). Disposition DONE; B16 records it.
- 2026-10-02 — **EAD-12 (new item; A4 / C6 of `audit/PR8_INDEPENDENT_ACCEPTANCE.md`; owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md`, row A4 / C6)**:
  the 13 Evidence Records with `visual_contract_state = NO_GOVERNED_CONTRACT__TABLE_ONLY` (VIS-PROVIDER-TIME, VIS-MFI-SPINE,
  VIS-FINDEX-SAMPLE-SUPPORT, VIS-FINDEX-ACCESS-USE, VIS-FINDEX-BARRIERS, VIS-FINDEX-RESILIENCE, VIS-FINDEX-FLOW-CHANNELS,
  VIS-FINDEX-OBSERVED-WAVES, VIS-DEMAND-VINTAGE-LADDER, VIS-BORROWING-SOURCES-2014, VIS-DOMESTIC-REMITTANCE-PATH-2014, VIS-MFI-2014-PANEL,
  VIS-MFI-RUPTURE-LENS) print neither their Tranche C method text nor the table their state promises. Owner: the steward, Master-first
  (render the method text, supply rows, or retire the state). Disposition: **post-launch; no change in this edition.**

## 2. RELEASE_ONLY

| ID | Item | Where it shows today | What closes it | Owner | Origin |
|---|---|---|---|---|---|
| REL-01 | Security headers at the host: strict CSP, HSTS, `nosniff`, referrer and permissions policies | Documented only (`docs/DEPLOYMENT.md`); the output is already strict-CSP compatible (F6-G05) | Headers served and checked on the release host | Hosting, Code | F6 §4 |
| REL-02 | Reuse rights of the original sources are not assessed (`rights_state` `NOT_ASSESSED` on all 160) | Source cards carry the reuse notice; no third-party document is bundled or offered for download (F6-G07, G08) | A rights assessment before anything beyond linking and short factual citation is published | Owner, with counsel if needed | Tranche B U-07 |
| REL-03 | Native-speaker certification of the Arabic corpus | F5 accepted the corpus in both languages; that acceptance is not a certification and none is claimed | An external certification, if the owner wants one | Owner | F5 §8 |
| REL-04 | Named release acceptance: deployed mobile, RTL and accessibility checks, publication filtering, correction and version behaviour, legal checks where applicable | README "Release boundary" | A release record naming who accepted what; nothing in this repository declares public release readiness | Owner | README |

- 2026-10-10 — the reuse licence is **not** a release-only open item and no row is added for it: it is decided (CC BY 4.0 for CauseWay's own content, `audit/OWNER_DECISIONS_2026-10-10.md`,
  OWN-04-R) and `/rights/` and `/terms/` already print it in both languages. One release step remains, and it belongs to the owner and counsel, not to this register's classes:
  **CauseWay's counsel confirms the CC BY 4.0 text** that those two pages print, in both languages, before the first deploy makes them public (`docs/RELEASE_RUNBOOK.md` step 7a).
  Until a dated line in `audit/OWNER_DECISIONS_*.md` records that confirmation, `licence_text_confirmed` and `public_downloads` stay `false` in `site-src/deployment.json` and the deploy
  workflow refuses to publish. REL-02 is unchanged and separate: it is about the **original sources'** reuse terms, not CauseWay's own content.

## 3. EXTERNAL_EVIDENCE_DEPENDENCY

The public text stays exactly as it is until the source is read; closing any of these is a Master transaction.

| ID | Item | Where it shows today | What closes it | Origin |
|---|---|---|---|---|
| EXT-01 | IMF Country Report No. 26/80 (source `SRC-IMF-AIV-2025-STAFF-001`) has not been read in the original: YSC-008 (oil exports suspended "from January 2023"), YSC-014 (the units of the two prudential ratios, 148 → 69 and about 5 → about 2.5), YSC-015 (wording "through the formal banking sector"), YSC-017 (operational reserves about US$350 million, September 2025) | The chronology on `/finance/` and `/data/`, attributed to the IMF | A primary read; confirm or correct Master-first | P1-C06, F5 qmc-017/qmc-018 |
| EXT-02 | The date of CBY-Aden Governor's Decision No. 10 of 2026 (`SRC-CBY-ENF-10-2026`) | The source title prints undated (a providers-data row holds 9 June 2026 as cross-corroborated, not printed) | Read the decision page; set `document_date` Master-first | F5 src-046 |
| EXT-03 | Entity names in Governor's Decision No. 18 of 2026 (24 September 2026) exist only in the scanned instrument | The event is public without names (`NAMES_PRIMARY_SOURCE_PENDING`); no page names an entity | Transcribe the names from the instrument in both languages, Master-first | Tranche B U-03 |
| EXT-04 | The status-event table for `/providers/` (15 events) needs governed Arabic event text and Arabic entity names from the source instruments | No table on `/providers/` in either language; the decisions are reachable as sources of CLM-019. This item had no R8.5 disposition and is tracked again here | Arabic event text and names from the instruments, then a bilingual table | PB-0525, P1-H08 |
| EXT-05 | Product-holding and mobile-access figures attributed to the OECD 2026 financial-sector review (`SRC-OECD-YEM-RESILIENCE-001`) | `/finance/` says they have not been verified against the review's text and are not shown | Verification against the review's own tables | Tranche B U-09, PB-0165 |
| EXT-06 | The primary 2023 SFD/SMED loan-portfolio document behind 78,686 active microfinance borrowers (CLM-053, CLM-054, CLM-057) | CLM-053 states the primary document is identified but not yet in the evidence base | Obtain and read the primary; confirm Master-first | Tranche B U-09 |
| EXT-07 | Findex subgroup unweighted base *n* and design-based uncertainty intervals | CLM-002 and `/people/` state that no intervals are published or calculated | Authorised microdata; reproduce the World Bank values first, then compute | Tranche B U-08 |
| EXT-08 | Three Evidence Records with partial lineage: CLM-039, CLM-046, CLM-056 (some dataset-level inputs not linked to a source); CWR-006 inherits the partial state through CLM-056 | Each record page states that some inputs are not yet linked to a source | Bind the remaining inputs to source records Master-first | P1-L11, Tranche B U-11 |
| EXT-09 | Nine source records carry a public locator but no governed title, publisher or document type (the other nine locator-only records have no public locator and are never named) | Shown as "reference · locator" | A primary read of each; promote the metadata Master-first | P2-F10, Tranche B U-07 |
| EXT-10 | Reading visuals RV-CWR-005 (five-provider e-money mix) and RV-CWR-008 (SMEPS indicators) hold their values as governed text, not data rows; the table VIS-MFI-DIVERGENCE's rationale describes (borrowers, savers, portfolio at three anchors) has no resolved rows | SUPPORTING and TABLE_TEXT_FIRST tiers; rendered from governed text | Verify against the source tables and promote the values to rows Master-first | P3; F9 run 2 |
| EXT-11 | IFAD *Sending Money Home 2026*, deferred as a curated resource | Not in the source register | The full report shown to publish a Yemen estimate with a documented method (F3 reopening trigger) | F3 #2 |

- 2026-10-02 — **EXT-01**: Path B of the release-candidate brief applied in transaction RC-1 (the session's network policy refuses
  imf.org and elibrary.imf.org, so the report could not be read): the Methodology lead sentence now says an exception is marked
  where it appears, and YSC-008, YSC-014, YSC-015 and YSC-017 each print "This event has not yet been checked against the
  original source document." (new 14 columns `verification_note_en/_ar`). The row stays open; closing it is still a primary
  read, which also removes the four notes Master-first (`audit/release_candidate/runs/RC-1_MASTER_LEDGER.json`, item 3).
- 2026-10-02 — **VIS-FIRM-CONSTRAINTS, challenges 9–16** (release-candidate brief, item 6): Path B applied in RC-1 for the same
  reason (documents.worldbank.org refused). FFO-2022-CH-09…16 stay unbound; the figure prints the governed frame note
  "Partial list: 8 of the 16 challenges recorded in the source are shown." Closing it is a read of `SRC-WB-FSD-2024-001`,
  Annex III, Table 8 / Figure 108, p.146, then binding the eight rows Master-first (ledger item 6).
- 2026-10-03 — **EXT-01 closed** (transaction RC-7, Path A): IMF Country Report No. 26/80 read in full from the IMF eLibrary
  (www.imf.org refuses automated clients at its CDN). YSC-008 confirmed (staff report ¶6); YSC-014 values confirmed against ¶13
  and corrected in attribution ("the IMF staff report", not "the IMF's banking data") and end value (2½, not "about 2.5"), with
  a note that the report's FSI table (Table 5) gives other values and no unit; YSC-015 corrected to the report's wording (¶8,
  ¶39); YSC-017 corrected to US$350 million (¶12). The four "not yet checked" notes are removed; locators in
  `audit/release_candidate/runs/RC-7_MASTER_LEDGER.json` and `audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md`.
- 2026-10-03 — **VIS-FIRM-CONSTRAINTS, challenges 9–16 closed** (RC-7, Path A): all sixteen values match Table 8 of the
  original (Annex III, p. 146); rows 9–16 are bound with labels in the source's item wording and the partial-list note is
  unbound. The survey is named as the source names it ("the 2022 Yemen Enterprise Survey"); the method cites Table 8 and
  states that Figure 108 differs for transport or road blockades.
- 2026-10-03 — **EXT-02 closed** (transaction RC-8): the signed Decision No. 10 of 2026 (Ref. 345/CBY/2026, scan
  https://www.cby-ye.com/files/6a27bc7883b9c.pdf) is dated 8 June 2026; the held 9 June was the news page's date.
  `SRC-CBY-ENF-10-2026` carries `document_date` 2026-06-08, the scan and the date in its title; PSE-012 prints 2026-06-08.
- 2026-10-03 — **EXT-03 closed** (RC-8, owner note of 3 October 2026, point 1): the four entities of Decision No. 18 are
  transcribed Arabic first from the signed scan and held as non-public lineage only (PRV-EXCH-E023..E025, PRV-REM-E006);
  no page, table, search record or social image names them. PSE-015 prints what the other decisions print; CLM-019 no
  longer says "not yet transcribed". The `public_use` fields that still allow a subject for five other events are an
  open escalation (`design/ESCALATIONS.md`, RC-8), with nothing printed.
- 2026-10-03 — **EXT-04 narrowed** by the same owner note: the status-event table prints no entity names, in either
  language, so "Arabic entity names from the source instruments" is no longer part of this item; it stays open for the
  governed Arabic event text only.
- 2026-10-03 — **New: dates of the other 2026 enforcement decisions** (adversarial review of RC-8). The dates printed for
  Decisions 1–6, 9, 11, 13–15 and 17 of 2026 are the dates of CBY-Aden’s news pages. Decision No. 10 showed that the signed
  instrument's date can differ from that date by a day. Action, at the B14e currentness re-run: read each decision's
  signed scan where the news page links one, and correct the date Master-first wherever the instrument differs.
- 2026-10-03 — **Exchange and remittance roster replaced** (RC-8b). The file linked on 3 October 2026 (created 22 September
  2026) lists 100 companies, 231 establishments and 111 remittance agents; the Master and the site now follow it, and
  CLM-009 states that the roster file has been replaced during 2026.
- 2026-10-03 — **B13d link check** (RC-12, `audit/release_candidate/LINK_CHECK.md`): 156 public locators checked.
  - 129 OK.
  - Five SFD newsletters moved to the publisher's new file names; each was read and matched (locators moved).
  - Four have no current address and now point to the web.archive.org copy of the original address, labelled as an
    archived copy on the site.
  - 14 cannot be verified from this environment because the publisher's CDN refuses automated requests; a person
    checks them with a browser at release.
  - Still open: `SRC-CBY-SANAA-C12-2024`, the CBY Sana'a circular 12 of 2024, has no working address and no archived
    copy. `SRC-CBY-AR2015-HIST-001` returned 503 at both checks; re-check it at B14e.
- 2026-10-03 — **New: SFD newsletter No. 62 exists in two editions** (RC-12). The bound Q2 2013 values (88,169 / 175,447 /
  7,845) follow the original edition. The publisher now hosts another edition, whose provider table totals 84,760 /
  151,465 / 6,845 under the heading "until end of June 2014", while its narrative matches the bound values. The locator is
  the original address's archived copy. Action, owner or steward: decide whether a governed caveat names the two editions.
- 2026-10-03 — **New: the FMIIP ISR's "0"** (B12). The World Bank's Implementation Status Report, sequence 2, prints
  "Actual (Current) 0" for access points and for beneficiaries. That is a reporting placeholder, and it is not bound. The
  promotion condition of VIS-TARGET-RESULT-STATE stands: an observed result under FMIIP-RF-004's definition.
- 2026-10-03 — **New: the base of VIS-FIRM-FINANCE-SEVERITY** (B12). The source's sentence on p. 145 places the
  tabulation under "reasons of not applying". The base may therefore be firms that did not apply, which is narrower than
  the governed universe ("excludes firms that said they did not need a loan"). Action at B16: a governed limitation, or
  leave as is, after a reviewer reads p. 145.
- 2026-10-03 — **New: four origin tables named by `16_DATASET_CATALOG` are not sheets of the Master**
  (`173_CBY_ANNUAL_VINTAGES`, `198_IBS2020_UPSTREAM`, `201_MFB2023_RECON`, `219_SMEPS_PROGRAMME_EVIDENCE`;
  `B12_TEXT_FIRST_DISPOSITIONS.md`). The records still trace to public originals. Action at B16: bring the tables in, or
  record them as external working tables.
- 2026-10-03 — **Closed: dates of the other 2026 enforcement decisions** (RC-13; `ORIGINAL_SOURCE_VERIFICATION.md` §7). The
  twelve signed scans were read. Ten match. Decision No. 13 is dated 5 August 2026 (the news page 6 August) and Decision
  No. 14 is dated 19 August 2026 (the news page 20 August); both are corrected Master-first. Every decision now records
  its scan as a locator.
- 2026-10-03 — **B14 e currentness re-run** (`scripts/currentness_rerun.py`; result appended to
  `audit/FINAL_CURRENTNESS_CUTOFF.md`).
  - Unchanged: POS releases to June 2026, decisions to No. 18, FMIIP ISR of 8 April 2026, and Findex for Yemen still the
    2022 data year.
  - IMF, Remittance Prices Worldwide and the CBY Sana'a host cannot be read from here; they are checked by hand at release.
  - **New: nine CBY-Aden regulatory documents linked on its regulation page (https://cby-ye.com/pages/14) are not in the
    evidence base.** They include Decision No. 7 of 2026 on deposit interest rates and Circular No. 1 of 2026 prohibiting
    dealings in virtual assets. The /data/ regulatory group already says it holds "not a complete register", so nothing
    printed is false.
  - Action at B16: decide which to add. Each must be read in the original and titled in both languages, Master-first.
- 2026-10-03 — **First screens and drawn figures re-read** (`ORIGINAL_SOURCE_VERIFICATION.md` §8).
  - 42 of 65 numbers match their originals. One date did not: the bank row of the provider matrix, which RC-14
    corrects to 2026-10-03.
  - **Open for release (a person with a browser):** 22 values whose hosts now refuse automated requests. These are 13 IMF
    values (CR 26/80 Table 4, supplement Table 2), 4 RPW corridor costs, 4 FMIIP component start dates of July 2025
    (UNDP) and SFD's 93,118.
  - The UNDP dates especially need checking: the World Bank ISR gives the project's effectiveness as 1 September 2025.
- 2026-10-03 — **B12** (RC-12, `audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`): of the 23 text-only
  contracts, 2 now render their designed table from governed rows (VIS-TARGET-RESULT-STATE, VIS-FIRM-FINANCE-PATH) and 4
  are complete as designed. 17 wait on a named Master input; they go to B16.

## 4. KNOWN_EVIDENCE_FRONTIER

These are limits of the evidence, stated on the pages. Design must show them as evidence states, never as errors, and
must never fill them with an estimate, a proxy or a colour.

| ID | Frontier | Where the product states it | Origin |
|---|---|---|---|
| FRN-01 | The CLM-044 residual-model value is withheld: its source has no public locator or rights assessment. The value must never print | `/evidence/CLM-044/` | Tranche C |
| FRN-02 | The firm base (about 147) implied by the 91.84 % filtered enterprise table is not recorded, nor the question's exact wording | `/evidence/CLM-005/` | EVM-07, Reading adjudication §4.2 |
| FRN-03 | No crosswalk between the CBY-Aden and IMF remittance levels; the paths are compared only as indices | `/evidence/CLM-037/`; RV-CWR-001 | Tranche C |
| FRN-04 | The causes of the gender gap are not established | Reading CWR-007; MA-003 | Tranche C |
| FRN-05 | No reconciled view of current operating status across provider classes | `/providers/`; CLM-009, CLM-019 | Tranche C |
| FRN-06 | The magnitude of the 2022 banking restatement is not quantified until the two vintages are reconciled line by line | Reading "banking jump"; CLM-033; RV-CWR-002 | EVM-18, VER-23 |
| FRN-07 | Composite records whose member records are not listed (by object type in the source-closure file: 9 Evidence Records — CLM-014, DS-DEMAND-VINTAGE-LENS and seven `VIS-` records — 8 visuals and 1 claim) | Each page says the view summarises other evidence | P1-L11, Tranche B U-11 |
| FRN-08 | The World Bank Joint Food Security Monitor's sub-national exchange-rate series (definition, area, lineage), deferred as a curated resource | Not in the source register | F3 #5 |

## 5. OWNER_INPUT

| ID | Decision or fact needed from CauseWay | Where it shows today | What happens meanwhile |
|---|---|---|---|
| OWN-01 | Who CauseWay is for this resource, who funds or commissioned it, and its relationships with the institutions whose data it presents | `/about/` states CauseWay's role only | Nothing is invented; the About page keeps its current statement (TRUST-09) |
| OWN-02 | Confirmation that `office@causewaygrp.com` is monitored | `/contact/` names it as the monitored channel | Confirm before release, or change the governed text Master-first |
| OWN-03 | The public origin (`site-src/deployment.json` `public_origin`) | Build is marked not for indexing; no sitemap is written | When set, URLs become absolute, the sitemap is written and robots allows crawling — nothing else changes (`docs/DEPLOYMENT.md`) |
| OWN-04 | A reuse licence for CauseWay content (and, separately, for the code) | No licence file; downloads and exports (a record's fields, a chart's data table or framed image, a citation file, a Reading as a hosted PDF) are designed in disabled and enabled states and ship disabled | They ship only after this decision; the browser's own print and save-as-PDF of a page are not downloads and are always available |
| OWN-05 | Stewardship decisions: maintenance resourcing, an analytics policy (none exists; no analytics ship), Digital Public Good gaps | `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` (non-public) | Nothing public depends on it |
| OWN-06 | A reversed (light-on-dark) logo, only if the design needs one | Not requested yet | Design places the canonical logo on a light field; no derived variant is made (EAD-04) |

- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **OWN-01**: the funding and relationships paragraph is approved (EN and AR as given there), applied Master-first in the
  release-candidate pull request (transaction RC-2); publisher name "CauseWay" in Latin script in both languages; CauseWay holds no active
  contract or partnership with any source institution related to Yemen financial inclusion. Footer unchanged.
- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **OWN-02**: confirmed; `office@causewaygrp.com` is monitored.
- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **OWN-03**: the public origin is decided when hosting is ready; `public_origin` stays null until then.
- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **OWN-04**: licence deferred; launch is link-and-short-citation only; downloads and exports stay disabled; the "reuse
  terms not assessed" wording stays. Not a gate for a link-and-citation launch.
- 2026-10-02 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` — **OWN-05**: CauseWay maintains the resource; whole-system review at each new edition; no fixed update cadence is
  promised; no analytics ship.
- 2026-10-03 — owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md` (owner instructions of 3 October 2026, 09:50 Cairo, section E; owner note of about 11:15 Cairo, 3.6) — **OWN-04**:
  the licence deferral of 2 October is superseded. The owner adopts CC BY 4.0 for the content CauseWay owns in this resource — its text, analysis, visual designs, the compiled records,
  and the structure and annotations of the exports. "The licence decision" leaves the owner's open list and is replaced by "counsel confirms the CC BY 4.0 text". `public_downloads` stays
  `false`; the switch is one release step after that confirmation (`docs/RELEASE_RUNBOOK.md` steps 2 and 7a).
- 2026-10-10 — owner decision, see `audit/OWNER_DECISIONS_2026-10-10.md` — **OWN-04 CLOSED AS A DECISION**: the rights question is closed. CC BY 4.0 for CauseWay's own content stands,
  as adopted on 3 October 2026. The owner's message of 9 October 2026 ("we have no licence / لا نملك ترخيص") was about **regulatory** licensing — CauseWay is not a licensed financial
  institution and claims no such status — and never referred to the reuse licence. Nothing is open for the owner to decide about the reuse licence; the remaining release step is
  CauseWay's counsel confirming the CC BY 4.0 text (`docs/RELEASE_RUNBOOK.md` step 7a; §2, the dated line of 2026-10-10). `licence_text_confirmed` and `public_downloads` stay `false` until then, and no
  licence file is added. The **code** licence is a separate question: the repository's software code is outside CC BY 4.0 and nothing is decided about it. No rights clearance, legal
  review or certification is claimed. The 2026-10-02 line above is history and is not rewritten.

## 6. REJECTED / NO ACTION

| ID | Decision | Why | Record |
|---|---|---|---|
| REJ-01 | Domain answer prose that restates an Evidence Record's sentence stays authored prose (8 verbatim and 13 near-verbatim restatements on non-record routes); it is not replaced by generated record blocks | A domain answer is its own editorial layer; numbers are held identical by the literal audit and bilingual invariance; any wording change is one Master transaction over both sheets (`audit/final_integration/rf5_corpus.py` sweeps twins) | PB-0471 |
| REJ-02 | No second Measurement priority for household remittances (MA-011) | It duplicates MA-001's survey instrument; MA-001 was widened instead | Tranche B, `audit/READINGS_MEASUREMENT_CLOSURE.md` |
| REJ-03 | No `Dataset` structured data | The resource publishes evidence records and a source directory, not datasets | F6 §1 |
| REJ-04 | No carbon figure, byte budget, badge or "green" claim before the implemented site is measured | Needs a named model and the real runtime | `docs/SUSTAINABILITY_METHOD.md` |
| REJ-05 | 26 corpus findings rejected under two house rulings, 7 superseded | Recorded with reasons | `audit/F5_CORPUS_FINDINGS_LEDGER.csv` |
| REJ-06 | Two Resource Library candidates rejected | Recorded with reasons | `audit/F3_RESOURCE_DECISIONS.md` |
| REJ-07 | No sync of the pre-GitHub Drive copies | GitHub `CausewayGrp/Financial-inclusion-` is canonical; the Drive files are lineage | README "Historical lineage" |

## 7. What would have been a DESIGN_BLOCKER, and why none is

A blocker is something without which Design could not proceed, or would have to invent a factual premise, a label or a
behaviour. None remains:

- Every string that exists on the product today is governed (`site-src/content/content/interface_copy.json` and the
  navigation labels the generator writes from the Master). The strings Design will need for components that do not
  exist yet, and for chart tables, are listed in the brief §10 as expected `NEEDS_CONTROLLED_CONTENT` requests, with a
  marked-placeholder rule; the one content defect known in a signature visual (the English-only dated cells of the
  VIS-PROVIDER-OBSERVABILITY matrix) is listed there as a pre-registered `ESCALATE_TO_MASTER`. The steward answers these
  Master-first and appends lasting ones here.
- Every evidence state Design must draw exists in real data (`handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json`: twelve
  hard-state cases with the facts at their routes, nine verification states, fifteen technical states).
- Every open item above either has an honest state on its page, is Design's or Code's own scope, or matters only at
  release; where two sources in the repository disagree, the brief §2 says which governs.

F9 tested this with three cold recipients, each with only a clone of `main` (`audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`). All
three could start D0 without asking and every command passed; each run's contradictions and gaps were fixed or given an
explicit rule before the next.

## 8. Closed since first raised (so they are not reopened)

| Item | Closed by |
|---|---|
| Public copy held in `build.py` and `app.js` (AR-29, EN-09, TRUST-25) | R8.5 (`1a63ee5`); gates R85-G01…G03 |
| Reading-prose parity (BIL-05) | F2 (`0b94c08`); bilingual invariance 0 |
| RV-CWR-001 panel 2 and the REF-PAY-001 locator (P3-B01) | P5; no visual release blocker remains. A stale "BOUND_PARTIAL" note in the VIS-PAYMENT-RAILS design rationale was corrected in F8 |
| 2025 remittance value in CBY-Aden's 2025 annual report (P5-06) | Tranche C (TC-D), held as context |
| Duplicate chronology events, analytics labels, publisher gaps (P3-D02) | R8.5 and F5 |
| CBY decisions 7, 8, 12 and 16 (U-04) | Tranche B; CLM-019 states their scope |
| Viewport and RTL testing at 320–400 px (U-10 part) | Tranche C, 168/168 |
| Held Tranche B page blocks PB-0160/0161, 0322, 0345, 0374, 0470, 0520, 0521, 0522, 0614 | P1.6, P4.2, P4.3 and F2 |
| Literal-audit heuristic (U-14) and duplicate page contracts (U-15) | P1-D; R8.5 |
| Two language-switch labels held as literals in `scripts/build.py` (F9 cold-recipient finding) | F9, transaction RF9: moved unchanged into the Master's interface copy (`UI-LANG-SWITCH-NAME`, `UI-LANG-SWITCH-ACTION`) |
| WITHHELD used as a visual marker without a governed drawing rule (F9) | F9: grammar entry in the controlled visual contract input, regenerated |
| Inventory without collection bindings, next actions or rendered verification states; hard-state cases without the facts at their route (F9) | F9: `scripts/handoff_inventory.py` schema 1.2 |
| The Page Specs' editorial rule allowed "professional compression" without saying by whom (F9 run 2) | F9: controlled input `page_spec_templates.json` — governed wording is rendered as authored; only the programme compresses, Master-first |
| A comparability flag rendered as an ungoverned UNKNOWN marker on two withheld VIS-PAYMENT-ANATOMY values (F9 run 2) | F9: marker mapping removed in the controlled visual contract input; WITHHELD governs those values |
| Architecture diagrams named an external design tool, an analytics opt-in and `/readings/[reading_id]/` (F9 run 2) | F9: `scripts/architecture_diagrams.py` |
| The required fonts were not in the repository (F9 runs 1–3) | F9: `vendor/fonts/` — unchanged woff2 files and licence of `@ibm/plex-sans@1.1.0` and `@ibm/plex-sans-arabic@1.1.0` |
| The POS charts' DISAGREEMENT note pointed to a non-public, English-only Evidence Passport (F9 run 3) | F9: the controlled contract input points to the bilingual method text of the charts' own Evidence Records |
| `visuals/system_relationships.json` was classed as a render input although its prose is English-only (F9 run 3) | F9: inventory role STRUCTURE — IDs and links only |
| From an extracted archive, a locally built `design/reference/out/` would have entered the checksum and file manifests (F9 run 2) | F9: `scripts/checksums.py` honours `.gitignore` when there is no `.git`; the manifest and validator use the same file set |
| Navigation relabel and domain pages without Readings (Tranche A) | Tranche B Stage 4; gate RP-G04 |

### Closed by the post-F9 correction (27 September 2026)

| Item | Closed by |
|---|---|
| OWN-07 — `/remittances/` showed no Measurement card although its Page Spec binds MA-001 | `site-src/content/presentation_priority.json`: `measurement_limit` 1 for `/remittances/`; the MA-001 card (people-side baseline; household remittance receipt as missing evidence) now renders in both languages beside, and distinct from, the macro remittance series. The two hand-maintained contracts are now classed `CONTROLLED_CONTRACT` in `FINAL_REPOSITORY_MANIFEST.json`, with their maintenance rule in the file itself, `AGENTS.md` rule 2 and `CONTRIBUTING.md` §2 |
| OWN-08 — stale descriptive fields in `navigation_interaction.json` | Corrected against governed copy, the Page Specs and the tests: the report-issue route (`/contact/`, `?record=`) and Arabic label («أبلغ عن مشكلة», `UI-HEADER-REPORT-AN-ISSUE`); the Reading breadcrumb (governed title); the six Compare dimensions, four assessments, same-record state and comparable set; the workbench inputs (Evidence Passports removed — they stay reference only) and its add-to-Compare limit; the `verification_sparse` case (now the framing record CLM-004), `institutional_sequence` and `vintage_conflict` sentences; journey J10's path (record → Contact → Corrections) |

## 9. Keeping this register

Close an item by the route its class names (a Master transaction for evidence items), then append a dated line under the
item's table with the commit and record; do not delete rows. A new item gets the next ID in its class. The README and the
checkpoint summarise this file and point here; they do not keep their own lists.

### Erratum, 2 October 2026 — cells of §1 rewritten in place on the pull request #8 branch

On 29 September 2026, on `claude/hopeful-mccarthy-jgip83` (six commits, `5e84f42` … `eb2a868`), the "Where it shows today" cell of all eleven
EAD rows and the ENGINEERING_AFTER_DESIGN count cell of the class table were rewritten in place, against the rule above and the
header's "Later changes are appended, never rewritten" (`audit/PR8_INDEPENDENT_ACCEPTANCE.md` A7 item 5, condition C5). The
current cells are kept as they now read; this erratum records each previous text verbatim from git history, with the commit that
replaced it, so the method is not silently changed. From this date the rule stands: a changed state is a dated line appended under
the table, and a cell is never rewritten. In the same correction the EAD-11 item cell was corrected in place from
"ID sets held in `scripts/build.py`" to name `scripts/yfie/question_sets.py` (the file that holds them since EAD-01; the
acceptance's one-line fix), recorded here for the same reason.

| Cell | Rewritten by | Previous text (verbatim) |
|---|---|---|
| Class table, ENGINEERING_AFTER_DESIGN count | `5e84f42` | 11 |
| Class table, ENGINEERING_AFTER_DESIGN count | `570d995` | 11 (EAD-01 and EAD-04 closed 2026-09-29; EAD-08 all but its optional subsetting) |
| Class table, ENGINEERING_AFTER_DESIGN count | `c1e49ac` | 11 (EAD-01, EAD-04, EAD-05 and EAD-09 closed 2026-09-29; EAD-08 all but its optional subsetting) |
| EAD-01, "Where it shows today" | `5e84f42` | The reference build in `dist/` |
| EAD-04, "Where it shows today" | `5e84f42` | Footer of every page |
| EAD-08, "Where it shows today" | `5e84f42` | The baseline CSS names the families but loads no font file (readers without them installed see the fallback); the files are in `vendor/fonts/` since F9 |
| EAD-11, "Where it shows today" | `5e84f42` | The inventory exposes them for Design (`/` and `/explore/` → `collection`); the cluster headings are governed `UI-QUESTIONS-*` labels |
| EAD-05, "Where it shows today" | `570d995` | Header on all pages; mobile menu |
| EAD-09, "Where it shows today" | `570d995` | Open Graph without image (F6, F8) |
| EAD-06, "Where it shows today" | `8ec2365` | No Compare link on record pages; Compare reachable from `/evidence/compare/` only |
| EAD-03, "Where it shows today" | `639cc3b` | Every page loads the master PNG (96–99 % of each cold page; `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`) |
| EAD-10, "Where it shows today" | `639cc3b` | Pre-design baseline only |
| EAD-02, "Where it shows today" | `c1e49ac` | Outcomes are specified (F6 §3; Page Spec accessibility flags `PENDING_DESIGN_IMPLEMENTATION`); viewport acceptance 168/168 passes on the reference build |
| EAD-07, "Where it shows today" | `eb2a868` | `/data/` offers a text filter only |

- 2026-10-03 — **B16 disposition** (append-only; the reasons and evidence for each line are in
  [`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md`](audit/release_candidate/OPEN_ITEMS_DISPOSITION.md)):
  - EAD-02 — **NEXT EDITION** — Accessibility audit of the implemented site (automated and manual, screen readers in AR/EN, zoom, forced colours…); the Accessibility page states no result unti… → Code half done 2026-09-29 and extended in B10 (66521a3): 286 pages × 2 widths, 0 axe violations, keyboard walk; no conformance claimed. Remaining: screen-reader passes and human judgement, post-launch by owner decision.
  - EAD-06 — **DONE** — Tools: Compare entry from the 13 comparable records, mobile Compare, a result-type search facet and a ?q= URL state (domain facet needs a governed field). → Facet and N-of-M shipped in G4 part 1 (7895694) on RC-3 labels (d668f11); ?q= in 8ec2365. No dated closing line in the register. Domain facet: X-ESC-ANT-01 (post-launch).
  - EAD-07 — **DONE** — A document-type filter on the source register, with a governed 'type not recorded' group for the 9 sources without document_label. → Label in RC-4 (ae0f3db); filter in RC-12 B13 a (98f43f5) with the 'Document type not recorded' option (verified in dist/en/data). No dated closing line in the register.
  - EAD-08 — **NEXT EDITION** — IBM Plex self-hosted (done); open only on IBM's pre-split Latin subsets, a self-made subset being an owner decision. → Optional; the B14 d budget is met without it (8c977f3). Owner decides on subsetting; a performance gain only.
  - EAD-10 — **RELEASE** — Remeasure bytes and requests on the implemented site and on the release host; set budgets only then. → Implemented site measured (29 Sep) and budgeted locally under the host headers (8c977f3). What remains: Claude Code remeasures on the live host, docs/RELEASE_RUNBOOK.md step 10, and records it beside release_candidate_b14d.
  - EAD-12 — **NEXT EDITION** — The 13 NO_GOVERNED_CONTRACT__TABLE_ONLY records: method text (now rendered) and the tables their state promises. → Method text DONE in B1 (d9df1d2; validator PB-0401). Table rows post-launch by owner decision A4 / C6, as the B16 brief expects ('table rows for the 13 table-only records').
  - REL-01 — **RELEASE** — Security headers at the host: strict CSP, HSTS, nosniff, referrer and permissions policies. → Prepared: site-src/hosting/_headers → dist/_headers, test_security_headers.py 0 violations on 288 pages (1ca46dc). At release: owner account and credentials (runbook steps 1, 6, 7); Claude Code deploys, enables HSTS and runs the header test against the live host (steps 8–9).
  - REL-02 — **NEXT EDITION** — Reuse rights of the original sources not assessed (rights_state NOT_ASSESSED on all sources). → The row's own closer is 'before anything beyond linking and short factual citation is published'; the owner chose a link-and-citation launch. Reuse terms stated once on /data/ (RC-4 B8, ae0f3db).
  - REL-03 — **NEXT EDITION** — Native-speaker certification of the Arabic corpus, if the owner wants one. → Optional by its own wording; the B2 Arabic pass (RC-5) and independent bilingual reviews are not a certification and the product claims none.
  - REL-04 — **RELEASE** — Named release acceptance: deployed mobile, RTL and accessibility checks, publication filtering, correction and version behaviour, legal checks where applicable. → Owner, runbook step 13 (a dated, signed line in audit/OWNER_DECISIONS_*.md), after Claude Code's live checks (steps 9–10, with an in-country phone check by a person the owner names) and step 12 (no RELEASE item open).
  - EXT-04 — **NEXT EDITION** — Status-event table for /providers/ (15 events): needs governed Arabic event text (entity names dropped from the item on 3 October). → Post-launch with Owner Addendum 2 improvement 6 (ADD2-IMP-6): the status-event table (date · decision number · class · action) needs its governed contract; the entity names stay withheld (owner decisions of 3 October 2026, points 1–2).
  - EXT-05 — **NEXT EDITION** — Product-holding and mobile-access figures attributed to the OECD 2026 review, not verified against its text and not shown. → Not read in this pull request; the product states they are not shown, so nothing is false meanwhile.
  - EXT-06 — **NEXT EDITION** — The primary 2023 SFD/SMED loan-portfolio document behind 78,686 active microfinance borrowers (CLM-053, -054, -057). → ORIGINAL_SOURCE_VERIFICATION.md §3: smed.sfd-yemen.org reset/503, NOT READ. RC-14 matched 78,686 to the Sana'a Center paper (secondary). CLM-053 states the gap.
  - EXT-07 — **NEXT EDITION** — Findex subgroup unweighted base n and design-based uncertainty intervals. → Owner Addendum 2 sends 'The Findex 2021 weighted subgroup compute … needs the microdata file' to docs/ROADMAP_V1_1.md.
  - EXT-08 — **NEXT EDITION** — Partial lineage on CLM-039, CLM-046, CLM-056 (and CWR-006 through CLM-056). → Not changed in this pull request; pages state the partial state. CLM-039 also X-ESC-D7C-02.
  - EXT-09 — **NEXT EDITION** — Nine source records with a public locator but no governed title, publisher or document type. → Still 9 cards print 'Document type not recorded' on dist/en/data (counted). Now findable through the EAD-07 group; promotion needs a read of each.
  - EXT-10 — **NEXT EDITION** — RV-CWR-005 and RV-CWR-008 hold values as governed text, not rows; VIS-MFI-DIVERGENCE's table has no resolved rows. → B12 names the inputs: IBS 2020 Tables (3)/(8) via origin table 198 for RV-CWR-005; SMEPS AR2024 pp. 8–9 via origin table 219 for RV-CWR-008 panel 3; saver crosswalk and rial-valuation field for VIS-MFI-DIVERGENCE.
  - EXT-11 — **NEXT EDITION** — IFAD Sending Money Home 2026, deferred as a curated resource. → No reopening trigger recorded in this pull request.
  - X-REG-LINK-C12 — **RELEASE** — SRC-CBY-SANAA-C12-2024 (CBY Sana'a circular 12 of 2024): no working address and no archived copy. → A person with a browser re-checks at release (runbook step 4). If still dead, the steward decides Master-first whether the source may stay publicly named with a dead locator (AGENTS.md rule 5: no source named publicly without a public locator).
  - X-REG-LINK-AR2015 — **RELEASE** — SRC-CBY-AR2015-HIST-001 (centralbank.gov.ye): host unavailable (503); re-check at B14 e. → Person with a browser at release (runbook step 4); a 2022 web.archive.org snapshot exists as a Master-first fallback.
  - X-REG-LINK-CDN14 — **RELEASE** — 14 public locators refused by publishers' CDNs (IMF ×6, OECD ×2, MDPI, ResearchGate, UNDP, WB Fast Payments, RPW ×2): not broken, unverifiable here. → A person with a browser, at release (runbook step 4 / step 12).
  - X-LINK-TLS-SIGNIN — **RELEASE** — SRC-LIT-OEB-FX-PRICES-2025 (TLS chain does not verify here) and SRC-ADEN-CBY-LIQ-2016 (database record redirects to sign-in). → RELEASE: a person with a browser checks both locators at release (docs/RELEASE_RUNBOOK.md steps 4 and 12). If a locator stays sign-in only, the source card gets a note under rule 5, Master-first. LINK_CHECK.md records both outcomes.
  - X-REG-SFD62 — **NEXT EDITION** — SFD newsletter No. 62 (Q2 2013) exists in two editions; bound values follow the original (archived) edition; decide whether a governed caveat names both. → Bound values (88,169 / 175,447 / 7,845) follow the edition read; the current file's narrative agrees; locator is the archived original (ORIGINAL_SOURCE_VERIFICATION.md §6). A caveat is enrichment, not a correction; the steward could also decide 'no caveat' now.
  - X-REG-FMIIP-ISR0 — **DONE** — FMIIP ISR sequence 2 prints 'Actual (Current) 0' for access points and beneficiaries — a reporting placeholder, not bound. → DONE: decided in RC-12 (98f43f5; B12_TEXT_FIRST_DISPOSITIONS.md): the ISR's placeholder 0 is not bound. The drawing that waits for an observed result is X-B12-VIS-TARGET-RESULT-STATE-DRAWING.
  - X-REG-SEVERITY-BASE — **DONE** — VIS-FIRM-FINANCE-SEVERITY base: source p. 145 places the tabulation under 'reasons of not applying', possibly narrower than the governed universe ('excludes fir… → DONE in RC-16 (b49fe93): p. 145 read again at the locator (ORIGINAL_SOURCE_VERIFICATION.md §9); the base is ambiguous in the source, and the record's measurement limitation now says so in both languages. No value changes.
  - X-REG-ORIGIN-TABLES — **NEXT EDITION** — 16_DATASET_CATALOG names four origin tables that are not sheets of the Master (173_CBY_ANNUAL_VINTAGES, 198_IBS2020_UPSTREAM, 201_MFB2023_RECON, 219_SMEPS_PROGR… → Post-launch: recorded as external working tables. Records trace to public originals through source IDs. Bringing the tables in is the same work as the B12 rows for RV-CWR-002, -005 and -008.
  - X-REG-REGDOCS9 — **NEXT EDITION** — Nine CBY-Aden regulatory documents linked on cby-ye.com/pages/14 are not in the evidence base (incl. Decision No. 7 of 2026 on deposit rates, Circular No. 1 of … → The /data/ regulatory group already says it is 'not a complete register', so nothing printed is false. The e-KYC instructions (65806fe2b3757.pdf) bear on MECH-ID-KYC and are the strongest candidate.
  - X-REG-HAND3 — **RELEASE** — Currentness watch points unreadable here: IMF SMP approval, Remittance Prices Worldwide after 2025 Q3, CBY Sana'a host; plus the re-run at the release date. → Claude Code runs scripts/currentness_rerun.py --append at the release date and moves UI-CONTENT-VERSION Master-first; a person checks the 'check by hand' points in a browser (runbook step 4).
  - X-REG-FIRSTSCREEN22 — **RELEASE** — 22 first-screen/drawn values not readable on 3 October: 13 IMF values (CR 26/80 Table 4, supplement Table 2), 4 RPW corridor costs, 4 FMIIP component start date… → A person with a browser at release (runbook step 4). Priority: the UNDP July 2025 start dates, since the World Bank ISR gives project effectiveness as 1 September 2025 — a possible truth conflict.
  - FRN-01 — **NEXT EDITION** — CLM-044 residual-model value withheld (no public locator or rights assessment); must never print. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request.
  - FRN-02 — **NEXT EDITION** — Firm base (about 147) implied by the 91.84 % filtered enterprise table, and the question's exact wording, are not recorded. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request.
  - FRN-03 — **NEXT EDITION** — No crosswalk between CBY-Aden and IMF remittance levels; compared only as indices. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request.
  - FRN-04 — **NEXT EDITION** — The causes of the gender gap are not established. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request.
  - FRN-05 — **NEXT EDITION** — No reconciled view of current operating status across provider classes. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request. The provider matrix (RC-3) shows dimensions without a roll-up, by design; Addendum 2 rejects a provider '2026 status' badge.
  - FRN-06 — **NEXT EDITION** — Magnitude of the 2022 banking restatement not quantified until the two vintages are reconciled line by line. → A limit of the evidence stated on its page; closes only with new evidence, Master-first. Not changed in this pull request.
  - FRN-07 — **NEXT EDITION** — Composite records whose member records are not listed (9 Evidence Records). → Narrowed by one: VIS-EVIDENCE-FRESHNESS now lists its member records (RC-11b, a95c7ef) — dist/ shows the 'summarises other evidence records, which are not yet linked' note on 8 records (CLM-014, DS-DEMAND-VINTAGE-LENS, six VIS-), not 9. Otherwise a frontier.
  - FRN-08 — **NEXT EDITION** — World Bank Joint Food Security Monitor sub-national exchange-rate series, deferred as a curated resource. → A limit of the evidence, stated on its page; closes only with new evidence, Master-first. Owner Addendum 2 rejects food-security monitoring (ADD2-REJ-11).
  - OWN-02 — **DONE** — Confirmation that office@causewaygrp.com is monitored. → Owner decision of 2 October 2026 (audit/OWNER_DECISIONS_2026-10-02.md, row OWN-02). No 'closed' word in the register; nothing remains to do.
  - OWN-03 — **RELEASE** — The public origin (site-src/deployment.json public_origin). → Owner provides account and domain (runbook step 1); Claude Code sets public_origin and rebuilds (step 3); deploy workflow refuses a null origin (8c977f3).
  - OWN-04 — **RELEASE** — A reuse licence for CauseWay content (and, separately, for the code). → RELEASE: the licence is decided (CC BY 4.0, owner instructions of 3 October 2026, 09:50 (audit/OWNER_DECISIONS_2026-10-02.md), E). What remains is that CauseWay's counsel confirms the CC BY 4.0 text; then public_downloads goes true, the downloads publish with the licence, and Dataset structured data may be added (REJ-03 lifts). docs/RELEASE_RUNBOOK.md step 2.
  - OWN-05 — **DONE** — Stewardship decisions: maintenance resourcing, an analytics policy, Digital Public Good gaps. → Owner decision of 2 October 2026. Note: Digital Public Good gaps are not addressed by the decision (non-public; nothing depends on it); optional cookieless counts are runbook step 11.
  - OWN-06 — **NEXT EDITION** — A reversed (light-on-dark) logo, only if the design needs one. → The accepted D7 design (owner acceptance 2 October 2026) places the canonical logo on a light field and needs none; dormant unless a future design asks.
  - X-B12-VIS-MFI-DIVERGENCE — **NEXT EDITION** — VIS-MFI-DIVERGENCE: renders only as a text frame; missing input — A governed saver-definition crosswalk and a rial-valuation field on each portfolio anchor (its… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-006 — **NEXT EDITION** — RV-CWR-006: renders only as a text frame; missing input — The same as VIS-MFI-DIVERGENCE, whose anchors it draws. → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-002 — **NEXT EDITION** — RV-CWR-002: renders only as a text frame; missing input — AR2022 vs AR2023 table: origin table 173_CBY_ANNUAL_VINTAGES is not a Master sheet; dual 2022 rows in … → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-003 — **NEXT EDITION** — RV-CWR-003: renders only as a text frame; missing input — A governed programme-lane label and crosswalk XW-FMIIP-005 as a data file (sits in sheet 33 only); lar… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-005 — **NEXT EDITION** — RV-CWR-005: renders only as a text frame; missing input — Rows from the 2020 e-payment study (Table (3) p. 54, Table (8) p. 68) with governed EN/AR type labels,… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-007 — **NEXT EDITION** — RV-CWR-007: renders only as a text frame; missing input — A data file for hypotheses MECH-ID-KYC, MECH-DIGITAL-ACCESS, MECH-ACCESS-PROX, MECH-TRUST (sheet 32 on… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-008 — **NEXT EDITION** — RV-CWR-008: renders only as a text frame; missing input — Panel 3 rows from the SMEPS annual report 2024 (printed pp. 8–9); origin table 219_SMEPS_PROGRAMME_EVI… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-RV-CWR-010 — **NEXT EDITION** — RV-CWR-010: renders only as a text frame; missing input — EN/AR labels for the ladder steps (or a mapping onto UI-VIS-CHAIN-*), and the reference period of the … → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-E-MONEY-RULE-STACK — **NEXT EDITION** — VIS-E-MONEY-RULE-STACK: renders only as a text frame; missing input — One row per ceiling (value, currency, period); Arabic text for EMR-001..013; the rationale… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-FCP-REDRESS-PATH — **NEXT EDITION** — VIS-FCP-REDRESS-PATH: renders only as a text frame; missing input — Numeric limit and unit fields for the 10 and 14 business-day limits; Arabic step labels for … → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-FL-EVIDENCE-LADDER — **NEXT EDITION** — VIS-FL-EVIDENCE-LADDER: renders only as a text frame; missing input — Rung labels EN/AR; a data file for OECD-YEM-001/-002; Arabic for PA-CBY-FL-001..004; corre… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-EVIDENCE-CLASS-LADDER — **NEXT EDITION** — VIS-EVIDENCE-CLASS-LADDER: renders only as a text frame; missing input — A governed class taxonomy with supports / does-not-support text per class, both languag… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-INCLUSION-TRANSMISSION — **NEXT EDITION** — VIS-INCLUSION-TRANSMISSION: renders only as a text frame; missing input — For each of the 13 relationships: evidence reference, source id with a public locator,… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-EVIDENCE-GAPS — **NEXT EDITION** — VIS-EVIDENCE-GAPS: renders only as a text frame; missing input — A typed gap field on 10_MEASUREMENT_AGENDA with EN/AR labels for five types. → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-OECD-FCP-TIMELINE — **NEXT EDITION** — VIS-OECD-FCP-TIMELINE: renders only as a text frame; missing input — Event labels (no FCP entries in the event namespace); an event row in sheet 31 for the 2024… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-MECHANISM-METRIC-BRIDGE — **NEXT EDITION** — VIS-MECHANISM-METRIC-BRIDGE: renders only as a text frame; missing input — Edge types reconciled with the governed relationship taxonomy (promotion condition). → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-ACCESS-EVIDENCE-LAYER — **NEXT EDITION** — VIS-ACCESS-EVIDENCE-LAYER: renders only as a text frame; missing input — The MA-005 register of verified, dated operating locations (promotion condition). → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-FIRM-FINANCE-PATH-DRAWING — **NEXT EDITION** — VIS-FIRM-FINANCE-PATH (drawing): renders only as a text frame; missing input — Table bound in RC-12; a drawn path needs the 2022 questionnaire's skip logic or t… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - X-B12-VIS-TARGET-RESULT-STATE-DRAWING — **NEXT EDITION** — VIS-TARGET-RESULT-STATE (drawing): renders only as a text frame; missing input — Table bound in RC-12; a drawn trajectory needs an observed result under FMIIP-R… → Named missing Master input (B12_TEXT_FIRST_DISPOSITIONS.md, RC-12 98f43f5); the B16 brief expects 'the contracts B12 could not complete (each with its missing input)' post-launch.
  - ADD2-REJ-01 — **REJECTED** — A composite evidence-maturity score. → Composite scores are closed (brief, rule 3); the evidence landscape stays categorical (RC-10, gate RC-LAND).
  - ADD2-REJ-02 — **REJECTED** — An interpolated account-ownership path. → Missing ≠ zero and observed ≠ estimated: the years between Findex waves are not measured (/people/ says so; no interpolation by rule).
  - ADD2-REJ-03 — **REJECTED** — Operating-provider counts derived from rosters. → Licence ≠ operation (semantic firewall); the matching of the 2026 decisions with the roster has not been done (RC-15, B-1).
  - ADD2-REJ-04 — **REJECTED** — POS terminals per adult. → Infrastructure ≠ outcome and people ≠ accounts; no population total is used to turn counts into shares (/evidence/compare/ §2).
  - ADD2-REJ-05 — **REJECTED** — 'True level' factors for remittances. → No crosswalk exists between CBY-Aden and IMF levels (FRN-03); a factor would invent a conversion (Compare: 'no invented conversion factor').
  - ADD2-REJ-06 — **REJECTED** — Access maps built from rosters. → A licensed or listed location is not an operating access point; MA-005 names the register that would be needed.
  - ADD2-REJ-07 — **REJECTED** — A provider '2026 status' badge. → A synchronised 'current state' is closed (brief, rule 3); status events are dated and never summarised as a current status.
  - ADD2-REJ-08 — **REJECTED** — An 'is my wallet licensed?' lookup. → The resource holds no complete named set of licensed wallet providers (CLM-015, VIS-PROVIDER-TIME); a lookup would imply a census. A separate regulatory record route is closed (rule 3).
  - ADD2-REJ-09 — **REJECTED** — Provider profile pages. → No new route unless a task fails on every existing page (rule 2); entity names of enforcement decisions are non-public (owner note, 3 October 2026).
  - ADD2-REJ-10 — **REJECTED** — A rial converter. → No invented conversion factor; the January 2023 valuation change and the CBY-Aden scope make a converter misleading (CLM-033, YSC-016).
  - ADD2-REJ-11 — **REJECTED** — Food-security monitoring. → Outside the resource's scope; the World Bank food-security exchange-rate series stays deferred (FRN-08).
  - ADD2-REJ-12 — **REJECTED** — The Uzbekistan comparator. → Not a same-definition, same-wave aggregate; international context comes from same-source aggregates only (docs/ROADMAP_V1_1.md §1).
  - ADD2-REJ-13 — **REJECTED** — A 'five key numbers' explainer. → League-table framing and figures detached from their boundaries are closed; every number keeps its period, universe and limit.
  - ADD2-REJ-14 — **REJECTED** — Merging regulatory instruments into the system chronology. → Chronology ≠ causality, and a separate regulatory record route is closed (rule 3); instruments stay in the /data/ regulatory group (B5).
  - B15-BLOCK-01 — **REJECTED** — «كوزواي» as the publisher's Arabic name (A-12). → Red team, B15: Governance: the owner set 'CauseWay' in Latin script only.
  - B15-BLOCK-02 — **REJECTED** — Relabelling the IMF remittance history 'may include model-based personal transfers' (B-3). → Red team, B15: Truth: CLM-036 disclaims the formula and scope of specific values, so it cannot be carried onto the Article IV history unread.
  - B15-BLOCK-03 — **REJECTED** — An eleventh Measurement priority for remittances (B-4). → Red team, B15: Governance: REJ-02; aliases to MA-001 are allowed instead.
  - B15-BLOCK-04 — **REJECTED** — Removing Home's 'Another view of the evidence' (C-15). → Red team, B15: Truth and accessibility: it is the system figure's text description and Home's only 'not causal, not composite' boundary.
  - B15-BLOCK-05 — **REJECTED** — An entity-level status register (game-changer U2). → Red team, B15: It would publish names and is the closed regulatory record route.
  - B15-BLOCK-06 — **REJECTED** — A 'strength' rating on a policy brief (game-changer U10). → Red team, B15: None is governed, and composites are closed.
  - ADD2-IMP-A1 — **DONE** — VIS-PAYMENT-RAILS: drawing, table and text alternative agree → RC-8 (fda3965); gate RC-A1 with a negative control.
  - ADD2-IMP-A2 — **DONE** — Search alias 001 boundary note; the /data/ scope line names laws and Sana'a instruments → RC-8 (fda3965), RC-8b (7947347).
  - ADD2-IMP-1a — **DONE** — document_type of the e-wallet circular and the e-money amendment → RC-17 `a4ff911`: instruction/circular and regulatory decision.
  - ADD2-IMP-1b — **DONE** — ENF-10's date from its original → RC-8 (fda3965): 8 June 2026, the signed decision (EXT-02 closed).
  - ADD2-IMP-1c — **DONE** — The regulatory group ordered by document date, with an anchor, linked from 'Verify it yourself' on /reforms/ and /providers/ → RC-17 `a4ff911`: newest first; #regulatory; both pages link it (gate RC-ADD2).
  - ADD2-IMP-1d — **DONE** — /reforms/ names the instruments by number where it describes them → RC-17 `a4ff911`: Governor's Decision No. 4 of 2025 (section 4) and No. 23 of 2024 (VIS-PAYMENT-RAILS, shown on /reforms/), from their governed titles.
  - ADD2-IMP-1e — **DONE** — 'decision' / «قرار' ranks rule-making decisions above enforcement decisions; 'N of M' when capped → RC-17 `a4ff911`: alias 002 targets regulatory decisions; 'Showing N of M' since RC-3 / G4 (d668f11, 7895694).
  - ADD2-IMP-2a — **NEXT EDITION** — A whole-phrase bonus on titles and summaries → Built and tested in RC-17, then withdrawn: it lifted records above the governed primary routes in the search smoke (PB-0494, P2-G01). Its main purpose, 'We Cash' first, was withdrawn by the owner (decisions of 3 October 2026, point 2). Needs the smoke expectations reviewed first.
  - ADD2-IMP-2b — **DONE** — Arabic tokens of two letters or fewer match whole words → 9236ffc (tokens of three letters or fewer match whole, after proclitics).
  - ADD2-IMP-2c — **REJECTED** — 'We Cash' and «وي كاش» find their record first → Withdrawn by the owner: the circular's twelve names are withheld alike and never enter the search index (decisions of 3 October 2026, point 2; RC-17; gate RC-NAMES).
  - ADD2-IMP-2d — **DONE** — Aliases Findex / «فيندكس» and PSP / «مزوّد خدمات الدفع» → RC-17 `a4ff911`: aliases 029 and 030.
  - ADD2-IMP-2e — **DONE** — Alias 007's note that «محفظة» means both e-wallet and loan portfolio → RC-17 `a4ff911`.
  - ADD2-IMP-3a — **DONE** — Evidence landscape table, 34 rows in 8 domains, categorical → RC-10 (ae86d2d); gate RC-LAND.
  - ADD2-IMP-3b — **NEXT EDITION** — DS-DEMAND-VINTAGE-LENS ten-function table → Its origin table (109_DEMAND_VINTAGE_LENS) is not a Master sheet; needs Master rows, a contract and the B12 table pattern (same family as EAD-12).
  - ADD2-IMP-4a — **NEXT EDITION** — CWR-010 reachable from /payments/ → Roadmap item 31 (owner instructions of 3 October 2026, 09:50, C6): an answer page carries at most two Readings and /payments/ has two; a third needs a design decision on which one yields. CWR-010 is two clicks away today (via CLM-045).
  - ADD2-IMP-4b — **NEXT EDITION** — CLM-045 and YSC-022 cross-referenced (delivered ≠ targeted ≠ persistent) → Needs a Master binding and a place in the record template.
  - ADD2-IMP-4c — **NEXT EDITION** — MA-001's card on /remittances/ leads with its remittance sentence → Needs a governed title variant and code; no new priority (REJ-02).
  - ADD2-IMP-5a — **DONE** — Preset Compare links (CLM-001, CLM-054, FMIIP-BASELINE-2025-01; CLM-032, CLM-037, CLM-041) → RC-17 `a4ff911`: under 'Three measures that cannot be combined' and in /remittances/ 'Verify it yourself' (gate RC-ADD2).
  - ADD2-IMP-5b — **DONE** — The Compare lead promises only what Compare compares → RC-15 (0a3ac6f), C-3.
  - ADD2-IMP-6 — **NEXT EDITION** — Status-event table PSE-001…015 under VIS-PROVIDER-TIME; PSE-015 never omitted; a frame note on status-event records → Needs name-free class and action columns, a contract and code. Entity names stay withheld (owner decisions of 3 October 2026, points 1 and 2). EXT-04.
  - ADD2-IMP-7 — **NEXT EDITION** — Pairings: CLM-010 with CLM-050 on /payments/; YSC-016 with CLM-054 → CLM-010 and CLM-050 already sit side by side in 'Verify it yourself'; a pairing note needs a Master binding and code.
  - ADD2-IMP-8 — **NEXT EDITION** — Chronology on /reforms/, /payments/ and /remittances/; an event variant; YSC-020 as a frame note → Roadmap item 29 (owner instructions of 3 October 2026, 09:50, C6): the chronology renders on /finance/ only; an event card is a new component, and each event's relevance would need checking against each page's question (chronology ≠ causality).
  - ADD2-IMP-9a — **DONE** — Trust links in the opened mobile menu → Steward patch to the navigation contract under the owner's designation (decisions of 3 October 2026, point 3), `88a0f86`.
  - ADD2-IMP-9b — **NEXT EDITION** — The prose text alternative in a details element where a drawing and a table exist → A design refinement; the visual contract checks assert the visible text alternative.
  - ADD2-IMP-9c — **DONE** — A shorter /payments/ headline → RC-17 `a4ff911`: a short, dated headline (17 words, from 36) serves as title, og title and search title; the full sentence opens the page as its lead (owner instructions of 3 October 2026, 09:50, C2).
  - ADD2-IMP-9d — **DONE** — 'How numbers are presented' shown once → `ab380cf`: printed once, on /methodology/ (#how-numbers), and linked once from each domain spine (owner instructions of 3 October 2026, 09:50, C5); gate RC-0950.
  - ADD2-IMP-9e — **NEXT EDITION** — One boundary band before the first answer → Steward: the bands are the contract's supporting sections (presentation_priority.json).
  - ADD2-IMP-9f — **NEXT EDITION** — The spine index lists answer sections only → Code; the index also serves the phone's in-page navigation (DEBT-014).
  - ADD2-IMP-9g — **NEXT EDITION** — /ar/data/ compact by default → Roadmap item 30 (owner instructions of 3 October 2026, 09:50, C6): /ar/data/ is complete without JavaScript by rule (DL-D7-013), so lightening it means paging or splitting the source list, which is design work.
  - ADD2-IMP-9h — **NEXT EDITION** — Home's first figure higher on a phone → Governed copy order; steward.
  - ADD2-IMP-9i — **DONE** — POS chart labels no longer collide → RC-10 (ae86d2d); check_visuals.py 0 failures.
  - ADD2-IMP-10 — **DONE** — The 00_MASTER and 37_READINESS_CHECKLIST counts → RC-17 `a4ff911`: 165 sources, 97 payment observations, counted from the sheets.
  - ADD2-IMP-11 — **DONE** — 'resolve … resolve' on Home and Explore → RC-17 `a4ff911`.
  - ADD2-IMP-L1 — **DONE** — Never 'latest' without a date; a lint gate → RC-16 (b49fe93); gate RC-LATEST.
  - ADD2-IMP-L2 — **DONE** — Survey coverage stated on survey records → 2021-wave population records: RC-10, RC-16 (b49fe93). The 2014-wave records need that wave's coverage read from its own source, and the multi-wave records need a wave-specific sentence: docs/ROADMAP_V1_1.md §3, item 26.
  - ADD2-IMP-L3 — **DONE** — Findex 2025's absence stated wherever people-side currency is discussed → RC-10 (ae86d2d) and RC-17 `a4ff911` on the 2021-wave records; the multi-wave records follow item 26 of the roadmap.
  - ADD2-IMP-L4 — **DONE** — A two-part citation: this resource, and the original source with publisher, title, year, locator → RC-15 (0a3ac6f), RC-16 (b49fe93) and `ab380cf`: the short citation is two lines, this resource with the page address, then the original sources (publisher, title, year, link); gate RC-0950.
  - ADD2-IMP-L5 — **NEXT EDITION** — Show the dates the governed fields hold together; never 'next update' → 'Next update' appears nowhere (checked). A checked-on date (retrieval_date) beside the period and the document date needs governed labels and code.
  - ADD2-IMP-J1 — **NEXT EDITION** — 18_CBY_MONETARY: a bounded expression on an existing contract → Deferred post-launch (owner instructions of 3 October 2026, 09:50, C7): the January 2023 valuation break and the CBY-Aden scope make a nominal-rial reading easy to misuse, and no existing contract fits without design.
  - ADD2-IMP-J2 — **DONE** — A publisher facet in the library, labelled 'publisher' → Done in B13 (owner instructions of 3 October 2026, 09:50, C7): RC-12 (98f43f5), B13 a, labelled 'publisher'.

## 10. Content-complete checkpoint, 10 October 2026 (appended)

**Current status.** Content is complete on `main` (checkpoint tag `checkpoint/2026-10-10-content-complete`, `docs/HANDOVER_TO_DEVELOPER.md` §9). Public release is not
declared and nothing is deployed. The class table at the top is the F9 state. Since then, the owner closed OWN-01,
OWN-02 and OWN-04; for the reuse licence, see the dated line under §2. What a person must still do for release is in
`docs/HANDOVER_TO_DEVELOPER.md` §1–7. No item below is a DESIGN_BLOCKER.

**Corrections to earlier cells, appended rather than rewritten:**

- REL-02: the original sources' reuse terms are not assessed on all **167** source records (the cell says 160).

**Items added on 10 October 2026.** New IDs continue each class. Every item is stated honestly on the page it affects,
or is not published.

| ID | Class | Item | Where it shows today | What closes it | Owner |
|---|---|---|---|---|---|
| EXT-12 | EXTERNAL_EVIDENCE_DEPENDENCY | **Remittance Prices Worldwide quarter.** VIS-REMITTANCE-COST shows 2025 Q3 | The visual's title and period carry the quarter | Re-read the latest RPW quarter at release (runbook step 4) and replace by transaction if newer | Claude Code at release |
| EXT-13 | EXTERNAL_EVIDENCE_DEPENDENCY | **IMF Financial Access Survey.** The Yemen series stops at 2015. The IMF website refuses automated requests | Not published (context only, `audit/R8_2_*`) | A person checks the IMF FAS for later Yemen data | A person with a browser |
| EXT-14 | EXTERNAL_EVIDENCE_DEPENDENCY | **ESPECRP unit of reach.** Whether the implementation-status report's reach figures count households or individuals | Not published (`docs/S06_3_*`, about 1.42m households in the 2024 Aide Memoire) | Read the unit from the original ISR before any reach figure is published | Claude Code |
| EXT-15 | EXTERNAL_EVIDENCE_DEPENDENCY | **CBY-Aden "subscriber".** No definition is published. Verified on the H1-2025 payments infographic, 10 October 2026 | /payments/ and /reforms/ say no definition is published (LA-A) | A CBY-Aden definition, if one is published | External (CBY-Aden) |
| EXT-16 | EXTERNAL_EVIDENCE_DEPENDENCY | **The vintage of the PAD's "two percent"** (¶9, p. 2). The sentence gives no year and no source | CWR-007 shows it as what the PAD says, not a measurement (LA-B, OWN-2e) | The World Bank's source for the sentence | External |
| EXT-17 | EXTERNAL_EVIDENCE_DEPENDENCY | **Cash Consortium of Yemen originals.** SRC-CCY-* are files the user supplied, with no public locator | Non-public source records; the CCY figures that are published rest on them as recorded | The publisher's public originals, or confirmation that none exist | Owner |
| EXT-18 | EXTERNAL_EVIDENCE_DEPENDENCY | **Provenance of the 26-bank list.** The CBY-Aden list carries no printed date. The locator is the July 2026 Arabic scan | Bank list "as checked on 3 October 2026" | A dated list from CBY-Aden | External (CBY-Aden) |
| EXT-19 | EXTERNAL_EVIDENCE_DEPENDENCY | **CBY-Aden bulletin currentness.** CBY-BANKS-2026-05 and CWR-011 use Issue No. 54 (May 2026); Issue No. 55 (June 2026) exists | The record and the Reading say May 2026 throughout and claim no later month | At release (runbook step 4), decide whether to roll the record forward by transaction | Claude Code at release |
| FRN-09 | KNOWN_EVIDENCE_FRONTIER | **SDG 10.c.** The resource holds no record of SDG indicator 10.c.1 (remittance costs as a share of the amount sent) or its 3% target | Not published | A next-edition decision whether to set the target beside VIS-REMITTANCE-COST; a target is not a result | Owner |
| OWN-09 | OWNER_INPUT | **Internal Master counts.** `00_MASTER` and `37_READINESS_CHECKLIST` hold site pages 143, Readings 10 and sources 165, both as formula caches and as constants; the sheets hold 144, 11 and 167. The definition behind "bilingual page sections 574" was not re-derived | Internal and unprojected; nothing public shows them | A Master transaction following `audit/release_candidate/rc_17_addendum2.py` (`set_formula_cache`) | Programme steward |
