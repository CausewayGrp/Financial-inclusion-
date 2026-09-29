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
| ENGINEERING_AFTER_DESIGN | 11 (EAD-01 and EAD-04 closed 2026-09-29; EAD-08 all but its optional subsetting) |
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
| EAD-02 | Accessibility audit of the implemented site against WCAG 2.2 (automated and manual; keyboard; Arabic and English screen readers; 200 % and 400 % zoom; forced colours; reduced motion; images off), including the text-alternative table for every drawn visual | Outcomes are specified (F6 §3; Page Spec accessibility flags `PENDING_DESIGN_IMPLEMENTATION`); viewport acceptance 168/168 passes on the reference build | An audit record; only then may the Accessibility page state a result | Claude Code, then an auditor | PB-0400, F6 §3 |
| EAD-03 | Web-size derivatives of the 10,018,081-byte master logo (6250 × 6250 px), by exact downscaling of the unmodified file | Every page loads the master PNG (96–99 % of each cold page; `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`) | Sizes listed by Design in `design/08_ASSET_MAP.md`; exported by Code with the owner's approval; master file unchanged | Design (sizes), Code (export), owner (approval) | TOOL-02 |
| EAD-04 | The reference footer whitens the logo with a CSS filter (`brightness(0) invert(1)`), which is a recolouring | **CLOSED 2026-09-29** with EAD-01, by construction: the filter existed only in the pre-design baseline stylesheet, which no longer exists or ships. The accepted stylesheet contains no filter, blend or mask, and the master file is unchanged | The production runtime uses no filter, blend or mask on the logo (Design prompt §8; acceptance criteria I); a reversed version only if the owner supplies one (OWN-06) | Design, Code | F8 |
| EAD-05 | Presentation of the "Method & Measurement" navigation group (the reference header wraps it as a ragged inline row with a non-link label) | Header on all pages; mobile menu | Design decides grouping and prominence within the fixed labels and destinations (Design prompt §4.2) | Design | TOOL-25 |
| EAD-06 | Tools still to build: entry into Compare from the pages of the 13 comparable records, with that record pre-selected; a mobile form of the four-column comparison; a result-type search facet and a `?q=` URL state (a domain facet needs a governed domain field first) | No Compare link on record pages; Compare reachable from `/evidence/compare/` only | Designed in `design/` (Design prompt §10), implemented with the 2–4 record URL contract unchanged; new labels requested as `NEEDS_CONTROLLED_CONTENT` | Design, Code | P2-F11, Tranche A A3 |
| EAD-07 | A document-type filter on the source register | `/data/` offers a text filter only | If designed, it filters by the governed `document_label` / `document_label_ar` only (142 of the 151 displayed sources) and puts the other 9 in a governed "type not recorded" group (Design prompt §10) | Design, Code | P2-F10 |
| EAD-08 | IBM Plex Sans and IBM Plex Sans Arabic self-hosted in the production runtime | **SELF-HOSTED 2026-09-29** with EAD-01: the build ships the six faces the stylesheet declares (three weights per family) with each family's OFL licence, unchanged from `vendor/fonts/`, and preloads the two first-paint faces of the page's language; no font CDN. Open only on the last part — IBM's pre-split Latin subsets are not used, and a self-made subset is an owner decision (the licence reserves the name "Plex") | Design self-hosts them in its reference implementation and Code in production, from `vendor/fonts/` with the licence, files as shipped (the licence reserves the name "Plex"); no font CDN | Design, Code | D7 §F8; F9 |
| EAD-09 | Social images: `og:image` only when Design's per-family templates are generated at build time from governed text | Open Graph without image (F6, F8) | Templates in the Design package; generated at build; gate F6-G01 extended | Design, Code | F6 |
| EAD-10 | Remeasure bytes and requests on the implemented site and on the release host; set budgets only then; no carbon figure or green claim before a named model is applied | Pre-design baseline only | `docs/SUSTAINABILITY_METHOD.md` rerun after implementation and after deployment | Code | F7 |
| EAD-11 | Home's four starting questions and Explore's four question clusters (the R8.4A decision) are ID sets held in `scripts/build.py`, not in a governed contract | **Narrowed 2026-09-29, and more urgent than recorded.** Explore's clusters were never governed: `handoff_inventory.py` recovered them by scraping the baseline renderer's HTML out of `dist/`, and the renderer read them back from the inventory — so EAD-01 emptied them and `/explore/` rendered with no questions. They now live in one named place, `scripts/yfie/question_sets.py`, the inventory reads them from there and parses no markup, and the regenerated inventory is byte-identical to the accepted one at `2f9a93c`. What remains is the original item: move the two sets into a governed contract | The production runtime takes the sets from a governed contract (Master or presentation contract), selection unchanged | Code, with the steward | F9 run 2 |

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
