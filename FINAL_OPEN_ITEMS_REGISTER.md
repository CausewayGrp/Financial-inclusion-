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
