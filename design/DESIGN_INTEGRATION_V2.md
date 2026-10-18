# Design integration V2 — the Stage B record

Created in Stage B G0 under the owner's takeover brief of 17 October 2026 (OD-1017-01) and the owner directive of
17 October 2026 (`audit/OWNER_DIRECTIVE_2026-10-17.md`), as `AGENTS.md` rule 7 allows. It records presentation
decisions, their evidence and their trade-offs. It decides nothing about content: every value, label and public
sentence comes from the Production Master, EN and AR together (charter v3.2 §0). It is never a content authority.

**How to read it.** Decisions are `DL-V2-nnn` lines (DL-V2-001 is reserved for the G1 direction, charter §10.5).
Findings use the design director's task graph (ENTRY → FIND → UNDERSTAND → QUALIFY → VERIFY → CONTINUE), its friction
taxonomy (`orientation_loss`, `answer_buried`, `label_mismatch`, `search_failure`, `filter_overload`,
`misleading_comparison`, `citation_disconnect`, `source_dead_end`, `context_return_failure`,
`hidden_essential_qualification`, `mobile_occlusion`, `RTL_cognitive_mismatch`, `performance_blocker`,
`accessibility_blocker`), its evidence labels (`OBSERVED_BROWSER`, `OBSERVED_CODE`, `OBSERVED_SOURCE`,
`SUPPORTED_INFERENCE`, `HYPOTHESIS`, `NOT_TESTED`; `OBSERVED_TEXT` = read in a rendered-text extract) and confidence
High / Medium / Low. Test outcomes are PASS / FAIL / NOT_TESTED / INCONCLUSIVE / NOT_APPLICABLE. Reader-job audits are
simulated walkthroughs by AI reviewers with browser measurements; no human testing, native-language certification or
accessibility certification is claimed anywhere in this record. Automated timings are never human reading time.

Evidence files: `design/evidence/v2/g0/` (metrics, scoreboard, visual audit, screenshot set with `INDEX.json`),
`design/evidence/v2/STATE.json` (the live state), `audit/close_out/PROGRESS.md` (one dated line per merged PR).

---

## 0. Decision log (DL-V2)

| ID | Date | Decision | Evidence | Trade-off |
|---|---|---|---|---|
| DL-V2-000 | 2026-10-17 | G0 method: one committed script (`design/evidence/v2/g0_measure.py`) measures every family at 320/390/768/1440 in AR and EN, served gzip as `_headers` declares; screens = scrollHeight ÷ viewport height; the same routes, widths, states and link-graph journeys run again in G3 and W8, so before and after are one measure. Reader jobs are AI-simulated walkthroughs on rendered text with link counts from the built HTML. | `g0_metrics.json` reproduces the brief's Part 2 table to the decimal (Home 8.5 · /data/ 70.5 · /measurement/ 44.7 · /payments/ 26.8). | First-screen proxies look for marked elements (`.fnum`, `.clock`, boundary parts); unmarked prose that carries the same meaning is judged by eye on the decisive views and noted as such. |
| DL-V2-001 | 2026-10-18 | G1 direction: **A · Register** — the quiet official-statistical direction, led by the data professional, chosen over the incumbent and over the editorial-evidence (B), compact (C) and hybrid (E) candidates (§4). Its grammar: a two-column register head on wide screens (title · statement and actions), the page tools as quiet text links, a lighter and narrower rail, rules instead of fills on the boundary, the record unit and the figures, the phone index as a plain numbered list, the topics block as one compact line, the type scale one notch down. Item 21: the one heading pairing (Markazi Text 600 / IBM Plex Serif 600) was built, specimen-tested and blind-judged twice and is **not adopted**: it lost on Arabic quality to the same three judges in both rounds (10 vs 12 of 15, then 9 vs 12) and gained only distinctiveness, mostly on English desktop views; the directive admits it only on a demonstrated readability benefit. The Arabic heading weight stays 600 (blind crop test: 600 preferred, 700 clots counters and diacritics). Item 13: the unit composition that judged best is the ruled unit (sentence, then the record line under a hairline, no plate, no fill). Item 19/32: the first-screen hypothesis is partly confirmed by C and E (the figure enters the AR 390 first screen at 0.7–0.8 screens when the chrome is compact and the tools follow the actions); the question entry with three examples needs markup and is a G2 memo. G0-F04: list beats strip (every judge). Item 29: DROP — no governed audience labels exist and the topics block already gives 92–100 % one-step reach (DL-V2-007). PR #51: assessed as evidence (§4.4), closed without merging. | `design/evidence/v2/g1/`: scorecard (A 108 · B 106 · C 102 · E 102 · incumbent 93 and last for every judge; round 2 A preferred by all three), 36 rendered views, bytes, disqualifiers (HTML and JS identical to dist/, nothing hidden, no overflow), source-owner test PASS on five records in both editions, the specimen. | What A sacrifices: a display face; its identity must come from composition, rules, numerals and rhythm. What B sacrificed: Arabic headings that read as designed in Arabic. What C sacrificed: the desktop route to the record list and the index. What E sacrificed: simplicity. The incumbent sacrificed the first screen to chrome. |
| DL-V2-002 | 2026-10-17 | The evidence unit (directive §5) is the design method for Stage B: value · unit · universe · period · publisher · evidence class · what it does not establish · what would settle it · verification trail, composed at Home, domain, record, Reading, Compare, /data/ and Measurement scale. Its composition is tested in G1, not pre-decided here. | G0 shows no family carries a marked figure, clock and boundary together in its first phone screen (§1.4); personas 4 and 6 fail or stall exactly where a unit field is missing (interval, measurement link, citation). | One shared order across families costs some editorial freedom; it buys the one repeated experience the owner named. |
| DL-V2-003 | 2026-10-17 | G0 dispositions of Part 6 items 13–22 and seeds 23–32 (§1.10): each is ADOPT, ADAPT, DROP or TEST IN G1 with the measure that decides it. | §1.10 cites the G0 measurement or audit line for each. | Items marked TEST IN G1 add candidate scope to G1; the proving pages stay four. |
| DL-V2-004 | 2026-10-17 | S10 executed: the phone table of contents is a grouped map of at most six entries, grouped by the contract's tiers and the Master's section roles (`presentation_priority.json` `toc_rule`, steward edit under OD-1017-03) with governed labels UI-TOC-* (transaction STAGE-B-S); a page under six phone screens (`min_main_words` 700, calibrated on G0 and the B1 re-measurement of the short pages in both editions) renders none, decided per route on both editions together. The desktop spine keeps the full numbered index (DEBT-019). | G0: the strip overflowed in 134 page×width cells (every route at 390, both editions) and exceeded six entries on 17 routes; B1: at most 6 entries on every route and width, 0 overflow (`g0/s1_metrics.json`). | Grouped entries lose the section-level jump on phones; the spine keeps it on desktop. Pages with their own grouping are the eight domains, /methodology/, /measurement/, Home and the Readings; /about/ and /data/ drop "Continue from here" from the map. |
| DL-V2-005 | 2026-10-17 | S13 scope: dates are shown in words in prose, clocks, record lines, lists and figure notes, with the ISO value kept in `<time datetime>`; a data table's period keys (2019-07, 2024) stay as the source publishes them, a machine context like a data file. Four records whose governed period text carried ISO dates were rewritten in words in the Master (CLM-012, CLM-015, CLM-018, CLM-021). | G0: 616 ISO tokens visible in 24 page×width cells; B1: 8 in 4, all on EN /providers/: the status-ledger keys "observed 2026-09-07" and "2026-01-22 event", free-text time boundaries the Master holds in English only and the renderer marks `lang="en"` (an existing D6 escalation); their worded bilingual form is a Master cell for B2. | Table columns stay narrow on phones; the E2-DATES gate reads a worded date's machine value; one EN-only time boundary remains until B2. |
| DL-V2-006 | 2026-10-17 | D8 executed (Part 6 item 11): the masthead holds five direct hubs — Questions, Evidence, Readings, Sources, Methodology — with no numerals; Measurement priorities stays a footer destination and a /methodology/ link. The resulting masthead is the baseline for the first-click test (item 14). | Master transaction STAGE-B-S (04_NAV_UX row 10 DIRECT; UI-NAV-HUB-01…05 retired in place); steward edit of `hub_numerals` (CR-S12, commit eb072951); gates RC-NAV, R4 and PB-0422 follow the five-hub contract. | One fewer masthead destination; the owner's decision, recorded. |
| DL-V2-007 | 2026-10-17 | F-15 / Part 6 item 14: Home gains a topics block — the eight domain answers by their governed names (UI-LAND-DOM-*), flat, under one governed heading (UI-HOME-TOPICS, transaction STAGE-B-S2) — and every page's footer gains the same eight links as its first group; Home's map lists the block first (steward edit, commit efd19111). The desktop masthead stays the five hubs of D8: no topics entry is needed. The four-family grouping of the old mockup is not adopted. | AI-simulated first-click, desktop 1440, three readers × eight tasks × two editions, judges blind to the variants: current (D8 masthead) 5/24 EN and 6/24 AR one-step; flat eight on Home 22/24 EN and 24/24 AR; four families 23/24 EN and 23/24 AR. The two candidates tie within one judgement; the flat eight matches the phone menu and needs no family labels. Material: `g0/firstclick_b1.md`. | Home grows by 0.9 AR 390 screens; its AR first screen no longer shows the figure (G0 did; EN never did) — part of the G1 first-screen hypothesis (item 32). No human testing; the judges are language models reading link labels only. |
| DL-V2-008 | 2026-10-17 | Report an error (BRIEF W4 T): a structured form on /contact/#report — page address, record or chart ID, section, language and edition pre-filled and editable; the value in question; seven error types; what it should say; evidence; optional name and reply address; a consent line to /privacy/. Transport is static and hosting-neutral: a valid report becomes an e-mail to the governed contact address in a fixed `key: value` body under `YFIE-ERR-<record>-<yyyymmdd-hhmm>`, opened in the mail app or copied for webmail; without JavaScript the page offers a pre-addressed e-mail carrying the same field list. Nothing is posted to any endpoint; a first-party endpoint stays a hosting option, off. The process (`docs/CORRECTIONS_PROCESS.md`: triage and classification within ten working days, the Master-first fix, the public log against the stable ID and edition, the reply) is linked from /corrections/ through the canonical repository address. | Browser test `t_report_form` in both editions with three negative controls (empty form, invalid address, unknown record); gate RC-T1 with three negative controls (a link missing the form, a lost field, a form that posts); /contact/ AR 390 4.1 → 6.0 screens. | The stated times are the resource's own commitments (the owner may change them); the repository link is the site's one external link that is not a source; the reporter's mail app must handle `mailto:` bodies. |
| DL-V2-009 | 2026-10-17 | Cite formats (OD-1017-04(a)): beside the governed plain-text preview, APA 7, Chicago, BibTeX and RIS are rendered from the page's own metadata — the governed title, the record ID, the edition, the publisher and the canonical address — with the access date; the copy action copies exactly the rendered text; machine formats keep their English keys; the Arabic edition uses the governed Arabic access phrases with Latin digits. | Browser test `t_cite_formats` parses the BibTeX and the RIS (and rejects a keyless BibTeX and a RIS without its end tag); every format carries the record ID, the edition and the address. | The access date is the reader's clock; APA and Chicago forms are house renderings of the governed metadata, not a style authority's certification. |
| DL-V2-010 | 2026-10-17 | Compare (SIG-5; F-16, Part 6 item 16): every controlled verdict carries one reason sentence naming the dimension behind it in the governed field words (differs: … / not recorded: … / the same record / all match), and a copied summary carries the verdict, the reason, each record's title, period, population and boundary, the no-merge rule and the comparison link. The Master holds no legitimately qualified pair among the 14 comparable records (no two with identical recorded definition, population and method and a different period); the Findex 2011, 2014 and 2021 waves exist as a visual (VIS-FINDEX-OBSERVED-WAVES) and a crosswalk dataset, not as per-wave records, so no pair is admitted and none is manufactured. A one-record entry from a record keeps the prompt for a second record by design. | Scan of the built Compare data (0 candidate pairs); browser test `t_compare_reason` (reason per verdict, summary, same-record, input error). | Compare keeps returning only qualified, not-direct or unresolved verdicts until the owner adds per-wave records by a transaction; F-16 stays open as a content question. |
| DL-V2-011 | 2026-10-18 | G2 refinement (the owner's visual-quality clarification of 18 October 2026, §8): **the brass anchor under every page title** — a 36 × 2 px rule in brass-300 at the start edge, 12 px under the title (8 px on phones) — and **the head statement in the secondary ink** (`--ink-2`), its figures staying in the primary ink. The owner's references were read for their qualities (a dominant title, a parted statement, subtle brass detailing, confident hierarchy), not their elements: no display face, no card, no illustration, no new text, route or font. The only two of three candidate shortcomings that earned a change; the third (a product rubric on the phone head) stays as recorded (the masthead carries it). | `design/evidence/v2/g2/shots/after_*` (re-rendered on the final tree; the committed `before_*` and `pass1_*` unchanged), the live candidate test on four views (v0 none · v1 anchor · v2 anchor + ink-2; v2 chosen on both editions), `g2/refinement_head_390.md` (head, boundary-heading and first-figure positions at 390 on the final tree). | +14 px (desktop) / +8 px (phone) in every head: the AR 390 /payments/ boundary heading ends at 851 px against an 844 px viewport (843 before; the domain exception of §7.4, boundary at 1.0–1.2 screens, holds); the phone actions and tools keep their G2 rhythm rather than being tightened to buy those 8 px back. |

---

## 1. G0 baseline — 17 October 2026, main `d36a51bb` (Master `d1807346…`, Page Specs `0fe9340c…`)

### 1.1 Method and reproducibility

- `python3 design/evidence/v2/g0_measure.py --shots <scratch>` → `g0/g0_metrics.json`, `g0/g0_scoreboard.md` (23 routes,
  one per family plus every domain and the Part 2 rows; 46 route×language rows; 22 interaction states; 14 journey
  targets). Chromium via Playwright; gzip static server from `scripts/performance_budget.py`; 230 s on this host.
- `python3 design/evidence/v2/g0_visuals.py` → `g0/g0_visuals.json`, `g0/g0_visuals.md` (all 42 contracts).
- Screenshots: `g0/shots/` (136 WebP files, 8.35 MB, indexed in `g0/shots/INDEX.json`): first screens at 390 and
  1440 for every route in both languages, 320 and 768 for the four proving pages, full phone pages for Home,
  /payments/ and CLM-001, and the 11 interaction states per language. The other captures stay in scratch.
- Reader jobs: six personas, three AI reviewers (opus), each on rendered-text extracts of the relevant pages with links
  and closed disclosures marked; click counts cross-checked against the link-graph journeys in `g0_metrics.json`.
- Not run in G0: axe (G3), 200%/400% zoom (G3), screen-reader order (G3), throttled-network timing (W4F), human testing (none, by decision).

### 1.2 The scoreboard (Part 2 re-measured; targets from the brief)

| Route | AR 390 | EN 390 | EN 1440 | TOC (AR) | H1 lines AR 390 | Target / note |
|---|---|---|---|---|---|---|
| / | 8.5 | 8.4 | 5.5 | 8 | 2 | P1 first screen; shorter |
| /explore/ | 14.5 | 14.1 | 11.4 | 6 | 1 | S7 (measurement previews bury the 11 questions) |
| /people/ | 20.1 | 18.8 | 13.4 | 11 | 2 | −25% |
| /payments/ | 26.8 | 25.7 | 17.7 | 13 | 4 | −25%; TOC ≤6; H1 ≤3 lines |
| /remittances/ | 24.4 | 22.0 | 15.0 | 12 | 3 | −25% |
| /firms/ | 20.3 | 18.8 | 13.4 | 12 | 3 | −25% |
| /finance/ | 17.0 | 16.3 | 10.9 | 14 | 3 | — |
| /providers/ | 25.6 | 24.5 | 16.5 | 11 | 4 | −25%; 42 ISO dates visible (S13) |
| /access/ | 11.6 | 11.3 | 7.5 | 11 | 5 | H1 ≤3 lines |
| /reforms/ | 28.9 | 28.4 | 18.7 | 12 | 2 | −25%; 26 ISO dates visible |
| /evidence/ | 29.5 | 29.1 | 25.1 | 6 | 2 | EN ≤14 (S5) |
| /evidence/CLM-001/ | 9.0 | 8.4 | 4.8 | 7 | 3 | P1 holds best today |
| /evidence/CLM-003/ | 9.6 | 9.5 | 5.3 | 7 | 1 | — |
| /evidence/VIS-POS-TERMINALS/ | 16.8 | 16.3 | 10.0 | 7 | 2 | — |
| /evidence/compare/ | 11.0 | 10.3 | 6.2 | 3 | 2 | — |
| /readings/ | 7.7 | 7.0 | 4.4 | 3 | 1 | — |
| /readings/how-money-reaches-households/ | 37.2 | 35.6 | 23.6 | 11 | 2 | chrome and tables only |
| /data/ | **70.5** | 68.1 | 53.9 | 12 | 2 | **≤20** (S1, S2, S9) |
| /methodology/ | 25.6 | 25.5 | 18.9 | **16** | 2 | TOC ≤6 |
| /measurement/ | **44.7** | 43.5 | 29.1 | 11 | 2 | −40% (S8) |
| /about/ | 6.6 | 7.2 | 4.1 | 7 | 2 | — |
| /corrections/ | 4.8 | 4.9 | 2.9 | 6 | 1 | — |
| /contact/ | 3.8 | 3.8 | 2.2 | 5 | 1 | — |

### 1.3 Chrome and structure facts (OBSERVED_BROWSER, High)

- **TOC strip overflows sideways on all 23 routes at 390 px, in both languages** (`toc_strip_overflows`); the brief's
  "/data/ and /measurement/ tab strip cut off at the phone edge" is the general case. No page overflows at 320.
- **TOC entries exceed six on 17 of 23 routes** (max 16 on /methodology/, 14 /finance/, 13 /payments/). S10 target ≤6.
- **H1 of four or more lines at AR 390** on /payments/ (4), /providers/ (4), /access/ (5). S11.
- **ISO dates visible in prose:** /providers/ 42, /reforms/ 26, /evidence/ 7; 0 elsewhere. S13 target 0.
- **Interactive targets:** /data/ 1,125 at 390 px; targets under 24 px: 1–2 per record page and Home at 1440 (the
  small chips), 0 elsewhere.
- **Bytes (cold, gzip, AR 390):** 259–317 KB per page; fonts 220 KB (3 files: 83% of a typical page), CSS 17 KB,
  JS 13 KB, HTML 7–65 KB. /ar/data/ 317 KB is inside the 350 KB budget. Font bytes decide every performance
  question in Stage B (W4F, item 21).
- **Interaction states:** phone menu opens with 22 links and works with JavaScript off; search finds «حوالات» and
  «الحوالات» (89 results each), 11.9 and ١١٫٩ (16 each), "remittances" (66): orthographic and numeral equivalence
  already work for these cases (an earlier zero-result reading was a 600 ms timing artefact, withdrawn). The /data/
  facets (type, publisher, year, domain, sort, clear) exist with a live count; `?source=` deep links work; Compare
  with `?records=CLM-001,CLM-003` renders a verdict; the cite button is hidden at both widths in the automated run
  (`[data-cite]` first match is the menu copy) → INCONCLUSIVE, re-tested in B2.

### 1.4 First-screen proxies for charter P1 (answer · clock · boundary · verification link in 390×844)

Proxy = marked element inside the first viewport (`.fnum`, `.clock`, `[data-boundary-part]`/`.bound`/`.isnot`, a link
to /evidence/, an external link). Judged = read by the lead on the decisive views (`g0/shots/ar/*_390_first.webp`).

| Family (route) | figure | clock | boundary | evidence link | source link | Judged reading at AR 390 |
|---|---|---|---|---|---|---|
| Home | yes | no | no | yes | no | Thesis, intro, two CTAs and the first paragraph with 11.9% and its universe fit; the period arrives just below the fold; the cite/report buttons take the band under the H1; "different clocks" is only implied. |
| Domain (/payments/) | no | no | no | no | no | Question label, a 4-line H1, cite/report buttons, then a lead sentence that carries 561→1,651, Mar 2025–Jun 2026 and the limit in unmarked prose; no verification link in view. All eight domains: 0/5 proxies. |
| Record (CLM-001) | yes | yes | no | yes | no | Breadcrumb, rubric, two clock lines *above* the H1 (S12 order), the H1, the buttons, then "01 What does it establish?" with 11.9%; the boundary is below. |
| /data/ | no | no | no | no | no | Breadcrumb, H1, buttons, a 90-word intro, then the tab strip cut at the edge. The first source row is far below. |
| Reading (CWR-012) | no | no | no | no | no | Thesis prose only. |
| /measurement/ | no | no | no | no | no | 153 words of preamble; the first priority starts at word ~662. |

P1 passes nowhere today by proxy; records come closest (figure + clock + evidence link). This is the baseline for G1/G2 (§1.10, item 13).

### 1.5 Six-persona reader-job audit (AI-simulated; links counted on the built HTML)

| Persona | Task | Clicks to answer / scope / limit / original locator | Outcome | Decisive friction |
|---|---|---|---|---|
| 1 Arabic phone reader, slow link | banks or wallets? | 0 / 0 / 1 / 2 | PASS | wallet answer buried mid-sentence; "not a current rate" needs one click |
| 2 Journalist | quote 11.9% with scope; find the correction route | 0 / 0 / 1 / 2 (correction route 2) | PASS with frictions | citation has no domain or access date; /corrections/ contradicts itself |
| 3 CBY / provider analyst | payments and rules, limits | 0 / 0 / 0 / 2 (/payments/ itself: 2) | PASS, naming partly met | no visible Payments route from Home; "Operation — activity recorded · evidence reaches this step" beside an item that says "not evidence of operation"; CBY-Sana'a unnamed on payments/reforms |
| 4 World Bank / IMF professional | definition, denominator, Compare verdict, SDG, citation | 1 / 0 / 1 / 2 | INCONCLUSIVE | no interval on 11.9% though Methodology §07 promises one; no SDG 8.10.2; no BibTeX/RIS; JS Compare table NOT_TESTED |
| 5 Humanitarian analyst | how money reaches households; geographic limits | 3 / 3 / 3–4 / 4 | PASS (marginal) | Reading link at word ~3,610 of /remittances/; 45,460 teaser lacks "eight districts, not national prevalence"; no correction note on the Reading |
| 6 Academic | CLM-001 sample, interval method, fieldwork, locator, citation; measurement agenda | 1 / 1 / 1 / 2 (interval method 3) | FAIL | interval absent on the record; sample n and design effect only on /methodology/; no record → MA-001 link; "what would change" folded on all 10 priorities |

Bank/MFB/exchange company and source owner personas: NOT_TESTED in G0 (W8 audience suite).

### 1.6 The Home contract (Part 6 item 19) and the first-visit journeys

| Measure | Result at AR 390 | Evidence |
|---|---|---|
| 10 s: what this is · different clocks · where to begin | purpose yes (thesis + intro in the first 72 words); clocks only implied; two CTAs visible | OBSERVED_BROWSER + judged |
| 60 s: one bounded answer | 11.9% with universe at word ~99, period and the 23% exclusion by word ~185; "not a current rate" absent on Home (1 click) | OBSERVED_TEXT |
| 3 clicks: an original source | Home → CLM-001 → World Bank indicator page = 2 clicks | link graph |

First-visit journeys: citizen PASS; journalist PASS; CBY analyst PARTIAL (/payments/ in 2, Sana'a unnamed); World Bank/IMF PARTIAL (no SDG, no citation format); humanitarian PASS in 3 clicks with the KPI ≠ prevalence point only implied; researcher PARTIAL (CR-22 statement on /methodology/, no BibTeX); bank/MFI/exchange and source owner NOT_TESTED.

### 1.7 Top-10 frictions (ranked by reader harm; destination row in brackets)

| # | Finding | Stage / type | Evidence | Conf. | Goes to |
|---|---|---|---|---|---|
| G0-F01 | Methodology §07 says CauseWay computes a 95% interval for each published national share "and shows it with the figure"; CLM-001, Home and /people/ show none for 11.9% (VIS-FINDEX-GAPS holds "margin of error of 4"). Either the record lacks its interval or the sentence overclaims. | QUALIFY / hidden_essential_qualification | OBSERVED_CODE | High | B1 (Master, EN+AR) |
| G0-F02 | /corrections/ prints "No material corrections have been recorded yet." and, below, "Correction of 15 October 2026: CWR-011…". Self-contradiction. | CONTINUE / misleading_comparison | OBSERVED_CODE | High | B1 (Master) + seed 25 (B2) |
| G0-F03 | On desktop, five of the eight topics (/finance/, /providers/, /payments/, /remittances/, /access/) have no visible link on Home: not in the header, not in the footer, not in the main content; three reach via question cards. The phone menu holds all eight behind a tap. (F-15) | ENTRY / orientation_loss | OBSERVED_BROWSER | High | B1 (D8 + topics entry; first-click test AR/EN) |
| G0-F04 | The TOC strip overflows sideways on every route at 390 (both languages) and reads as clipped; 17 routes exceed six entries. | FIND / mobile_occlusion | OBSERVED_BROWSER | High | B1 (S10) + G1 (strip vs list) |
| G0-F05 | No domain page meets P1 in its first phone screen; the answer sits in unmarked lead prose after a 2–5 line H1 and the cite/report band; no verification link in view. | UNDERSTAND / answer_buried | OBSERVED_BROWSER | High | B1 (S11, S12) + G1/G2 (unit) |
| G0-F06 | Citation preview gives a relative path, no domain, no access date, no BibTeX/RIS; copy needs JS. | VERIFY / citation_disconnect | OBSERVED_CODE | High | B2 (OD-1017-04a; hosting-neutral form) |
| G0-F07 | Reforms chain marks "Operation — activity recorded · Evidence reaches this step" for the event now labelled "(not evidence of operation)"; CBY-Sana'a is never named on /payments/ or /reforms/ although CWR-012 states the base holds no list from it. | QUALIFY / label_mismatch | OBSERVED_CODE | High | B1 (Master: event step binding; one neutral coverage sentence) |
| G0-F08 | /data/: 70.5 screens, 10,479 words, 1,125 targets, facets far below a 90-word intro; /measurement/: 44.7 screens, preamble to word ~662, "what the measurement would change" folded on all ten, the index at the end. | FIND / filter_overload, answer_buried | OBSERVED_BROWSER | High | B1 (S1, S2, S8, S9) |
| G0-F09 | CLM-001 has no path to MA-001 although MA-001 binds it; the 45,460 teaser on the Reading shows "a count reported by the programme" without "eight districts, not national prevalence". The unit's third part and the teaser scope are missing. | CONTINUE / context_return_failure | OBSERVED_CODE | High | B1 (Master bindings) + G2 (unit) |
| G0-F10 | CLM-001's first sentence reads "the latest survey estimate" without age or date; three time labels (2021 wave, 2022 data year, Nov 2022–Jan 2023 fieldwork) are not ordered; raw routes appear in prose ("(shown on /people/)"). | QUALIFY / label_mismatch | OBSERVED_TEXT | Medium | B1 (OD-1017-08 leads; S13) |

Also recorded (11–16): the Reading link on /remittances/ at word ~3,610 (S7, B1); CLM-003 lists 8 of 16 monthly releases, out of date order (B1); boundary line outside the `<figure>` element on 27 of 42 contracts (G2, SIG-1); the record's "Return to interpretation" label is Home's organising question, not its H1 (B1); "Compare evidence" from a record preloads one record and asks for two (B2); three fonts = 220 KB per page (W4F; item 21 budget).

### 1.8 Visual and diagram audit (42 contracts; `g0/g0_visuals.md`)

Mechanical facts (OBSERVED_CODE, `g0_visuals.py` after its G0 corrections): 52 visual objects — the 42 contracts of
`visual_library.json` plus 10 evidence objects in 06 with the state NO_GOVERNED_CONTRACT__TABLE_ONLY and no contract
(VIS-FINDEX-BARRIERS among them). Of the 42, 27 have an evidence record in 06 and 15 are Reading or domain-inline
visuals without one (RV-CWR-001…011 render inside their Reading; VIS-ACCESS-EVIDENCE-LAYER, VIS-MFI-DIVERGENCE,
VIS-CBY-MONETARY-SNAPSHOT and VIS-YER-MARKET-RATE render inline on /access/ and /finance/). Every contract renders on
its intended routes once two facts are applied: VIS-CAPITAL-CONTEXT is tier RETIRE_FROM_DESIGN (owner decision of
2 October 2026, A5/C4) and renders only as a link, and VIS-SOURCE-COMPARISON is carried by the Compare tool as a JS
table (B12; `design/06` §41). 10 contracts render an SVG, 22 a data table, 20 neither (text-first forms and Reading
visuals). The "what not to conclude" line is on every rendering page, but inside the `<figure>` element on only 15 of
42; /access/, /firms/ and /measurement/ carry no `data-boundary-part` at all although the text is present. EN and AR
render the same routes for every contract (AR parity holds). The `visual_contract_state` column of 06 is empty for
every contracted visual, so it cannot serve as the state source; the Master's 11 `public_routes` and `visual_form`
are stale for two retired or text-first decisions (below).

#### 1.8.2 Per-contract judgement (information-designer review, 17 October 2026; OBSERVED_SOURCE = Master cells or the live World Bank API, OBSERVED_CODE = built pages)

| Contract | Rendered | Stated state and reason | True today? | G0 disposition | Conf. |
|---|---|---|---|---|---|
| VIS-CAPITAL-CONTEXT | link only on /reforms/; no figure | tier RETIRE_FROM_DESIGN; "reports no amounts"; HUMANITARIAN_CONTEXT_ONLY | yes (A5/C4) | KEEP WITH REASON; Master 11 `public_routes` still says /reforms (stale) → B1 transaction | High |
| VIS-SOURCE-COMPARISON | Compare tool (JS table) + record text frame | "the Compare tool renders it as a table" | yes | KEEP WITH REASON; badge after selection NOT_TESTED → B2 | Med-High |
| VIS-PAYMENT-ANATOMY | HTML cards + table | "Figure held back until its definition is documented" (H1 2025 POS transactions, OBS-00036 = 58,512; Mar–Jun monthly sum 42,086) | yes | KEEP WITH REASON | High |
| VIS-POS-TRANSACTIONS | SVG + table | the withheld item is the same H1 aggregate; +18.46% (Apr→May) now shown and DERIVED | yes | KEEP; ESCALATE the marker asymmetry: OBS-00078 (Dec 2025) carries …INTERNAL_PERCENT_CONTRADICTION while OBS-00090 (Apr 2026) is DIRECTLY_COMPARABLE, so one of the two contradicted pairs is unmarked on the chart → B1 transaction | High |
| VIS-REMITTANCE-COST | SVG dots + table | "WDI carries no value for 2018–2021 or after 2023" | yes (API 2026-10-08: 2016 4.681, 2017 5.709, 2022 3.455, 2023 2.805; others null) | KEEP WITH REASON; check-date restamp optional | High |
| VIS-FINDEX-RESILIENCE | full table 11×4 | "publishes no value" refers to the 7-day item only | partly: table already filled from held cells WB-FINDEX-OBS-2022-039…082 by label; **new**: the API now publishes the 2022 main-source-of-emergency-funds series (fin24fam 64.2, work 9.4, sav 5.8, bor 4.7, sell 3.7, other 1.4; fin24aP 89.2), not held, and the boundary sentence "does not show where it would come from" is therefore stale | KEEP the table; ESCALATE: bind the fin24* values Master-first, map by label, revise the boundary → B1 | High / Med |
| VIS-FINDEX-FLOW-CHANNELS | full table 11×5 | channels not shown: no verified weighted distribution | yes for held data (cells 083…158 match by label) | KEEP WITH REASON; ESCALATE the API's fin28/fin29 = 0 for 2022 (sent/received "using an account") for a method note; codebook code collision (fin28) noted; never fill by code | High |
| VIS-EVIDENCE-FRESHNESS | table in a text frame | content sentences only ("not yet durable…") | no state | KEEP (audit false positive, corrected) | High |
| VIS-EVIDENCE-GAPS | text only | "a map layer that cannot yet be built"; blocked on a typed gap field in 10_MEASUREMENT_AGENDA | yes | KEEP WITH REASON; matrix only if the field is added (B1 decides with seed 24) | High |
| VIS-PROVIDER-OBSERVABILITY | table | "names not yet normalised row by row" (22_PROVIDERS_DATA PUC-EXCH-2026-01) | yes | KEEP WITH REASON; FIX RENDERING (boundary inside the figure) | High |
| VIS-PAYMENT-RAILS | HTML timeline + table | "Access/Use/Quality/Outcome — not yet measured — not a failure" | partly: "not yet measured" true; the step "Operation — activity recorded · Evidence reaches this step" is filled only by the node "(not evidence of operation)" | ESCALATE step semantics (G0-F07) → B1 Master; FIX RENDERING (boundary) | Med-High |
| VIS-ACCESS-EVIDENCE-LAYER | text only on /access/; no record page | "holds no verified, dated register of operating locations"; METHOD_CONTRACT_UNTIL_LOCATION_REGISTER_EXISTS | yes; no map is correct | KEEP WITH REASON; FIX RENDERING (boundary marker); record page or link to decide (no 06 object) → B1 | High |
| RV-CWR-004 / RV-CWR-006 / RV-CWR-009 | SVG+table / text / table+chain | "not yet measured"; "a set of providers not yet verified" (21_MFI_DATA) | yes | KEEP WITH REASON; align RV-CWR-009's Operation node with the VIS-PAYMENT-RAILS decision | High |
| VIS-FIRM-FINANCE-SEVERITY | governed text frame | B12: "a sentence carries them better than a stacked bar" | rendering matches the tier; Master 11 `visual_form` = STACKED_BAR and the encoding contract are stale | ESCALATE: Master transaction aligning 11 with the text-first decision → B1 | High |
| VIS-FINDEX-BARRIERS (06 only, no contract) | record page, no figure | "none of its Global Findex series on these reasons has a Yemen value" | yes (API: fin11a…fin11f, fin14d all null for YEM; codebook/API code labels differ, so label-not-code is essential) | KEEP WITH REASON; recorded as the 43rd object; the brief's "fill if not null" does not apply | High |
| the other 27 contracts | SVG/table/text per form | no state word; boundary present on the page | — | KEEP; boundary inside the figure for all in G2 (SIG-1) | — |

G0 escalations from this audit (to B1 unless marked): OBS-00090 comparability marker (Master 19); fin24* main-source
series (Master 25/26, boundary text on VIS-FINDEX-RESILIENCE); fin28/fin29 API zeros (method note); 11 `public_routes`
of VIS-CAPITAL-CONTEXT and `visual_form`/`encoding_contract` of VIS-FINDEX-SEVERITY (Master 11); VIS-PAYMENT-RAILS
step binding (Master 31 / renderer rule); a typed gap field for VIS-EVIDENCE-GAPS (only with seed 24); a record page or
link for VIS-ACCESS-EVIDENCE-LAYER. Renderer fixes to G2: the boundary part inside every `<figure>` (SIG-1), including
/access/, /firms/ and /measurement/. The audit script was corrected after the review: state words now match visible
text only (the earlier "withheld" hit was a CSS class), the Arabic list includes «يُحجب» and «لم تُقس بعد», the Compare
tool and retired tiers are recognised, and the ten table-only objects are listed.

### 1.9 Strengths to preserve (OBSERVED_TEXT, personas 1–6)

- The answer is server-rendered in Home's first section with its universe attached: "11.9% among adults aged 15 and over in the areas surveyed".
- The scope line travels with the POS number on Home, the record, the chart and the citation, unchanged in both languages.
- Source-internal discrepancies are kept side by side and never corrected: "+11% displayed … 8.55% derived … neither figure replaces the other".
- "Open original source ↗ (opens in a new tab)" is visible, not folded, on records and Readings.
- Compare treats "not comparable" as a valid result with reasons, in both languages.
- /contact/ says plainly that a report is an input to review and that no response time has been published.
- CLM-001 is shaped around the reader's questions (establishes / measures / applies / current / does not establish / source / method).
- The mobile-money caveat is precise; EN and AR match on every value, period and exclusion checked.

### 1.10 Dispositions: Part 6 items 13–22 and the directive's seeds 23–32 (DL-V2-003)

| Item | Disposition | Measure that decides it | Where |
|---|---|---|---|
| 13 Known · Not established · What would settle it | ADOPT the unit (DL-V2-002); TEST IN G1 its composition | P1 proxies at AR 390 on Home, /payments/, CLM-001; judges' boundary-comprehension score; phone screens | G1, then G2 |
| 14 Topics in one step (F-15) | ADOPT a one-step route to all eight topics; the grouping (flat eight vs four families) is TEST IN B1 by first-click | first-click success AR/EN before/after (G0: 3 of 8 visible on desktop) | B1 (D8 + CR-S12 steward edit, Master-first labels) |
| 15 "What the numbers do not say" on Home | ADAPT: compose from the five records' existing governed limit sentences; new copy only Master-first; it replaces repeated system-context prose, never adds length | Home words (919 EN / 858 AR today) do not rise; judges' boundary score | G1 (placement), S (copy) |
| 16 Honest Compare | ADOPT the framing; the Findex 2011/2014/2021 qualified pair is TEST IN B2 against the Master | one legitimately qualified verdict exists or the reason is recorded | B2 |
| 17 Faster verification (per-indicator locators, BibTeX/RIS, portable scope) | ADOPT | locator per indicator where the publisher has one; BibTeX and RIS parse in a test; print/copy keep scope | B1 (Master), B2 (cite), G2/G3 |
| 18 The phone is the product | ADOPTED: §1.2 is the scoreboard | before/after per family | every B row |
| 19 First visit makes sense | measured (§1.6); TEST IN G1 the first-screen hypothesis (item 32) | 10 s / 60 s / 3 clicks proxies | G1, G3 |
| 20 International practice as a lens | ADOPT; cite only where a decision changed | a citation in the DL-V2 line | all |
| 21 Typography (Arabic 600 vs 700; one OFL Naskh/editorial pairing) | TEST IN G1 | judges' Arabic readability; ≤4 font files; bytes within the W4F budget (fonts are 220 KB today) | G1 |
| 22 Rejected list | DROP (settled; directive §8) | — | — |
| 23 Machine-readable records (JSON per record, structured data by page type, citation_* meta) | ADOPT the generator and tests; outputs not committed while the repository is public; publication asked once | tests pass on a scratch build; publication filter identical to the pages | B2 (ask once with 28) |
| 24 "From rule to result" as a system chain with coverage per link | ADAPT: derived only from existing Master fields (13_SYSTEM_RELATIONSHIPS, chain bindings); the matrix on /measurement/ only if every cell has a Master source | no fabricated cell; reader finds "what is missing" per link | B1 (feasibility), G2 |
| 25 "What changed in this edition" on /corrections/ from the transaction ledgers | ADOPT: dates, transaction IDs and cell counts are site-operation facts (D15); labels Master-first; it also resolves G0-F02 | the section lists every merged transaction since the edition date | B2 |
| 26 Page and table locators inside sources | ADOPT, Master-first, audited | locator present where the original has pages/tables | B1/W7 |
| 27 Arabic search (equivalences, aliases, question-framed page, test set) | ADOPT: baseline already matches «حوالات»/«الحوالات» and ١١٫٩/11.9; build the committed AR/EN test set with answerable, unanswerable and near-match queries | top-3 success; honest zero-result help; no false hit | B2 |
| 28 Embeddable figure cards | ADOPT generator and tests; no distribution | cards keep scope, limit and source in a test | B2 (ask once with 23) |
| 29 Audience entry on Home | TEST IN G1 inside one candidate only; keep only if first-click improves without displacing the question entry (D9) | first-click; Home length | G1 |
| 30 Words, not icons (measured-object label; the clock; "Explain the denominator"; the firewall as short copy) | ADAPT: labels Master-first; the denominator disclosure on every percentage where a universe field exists | labels present on the unit; no icon-only state | S (copy), G2 |
| 31 Cite · Report · language on every page; period · source · data-class under list titles; counts in chips | ADOPT (cite/report/language already on every page; /data/ shows a live count) | present on every list and chip | G2, B2 |
| 32 Home first screen hypothesis (thesis ≤12 words; one question entry with three examples; one unit) | TEST IN G1 | §1.6 proxies; phone screens; judges | G1 |

### 1.11 Findings ledger (design items from the brief's Part 4, plus G0)

| ID | State | Note |
|---|---|---|
| F-03 phone pages long and getting longer | B1: /data/, /evidence/, /measurement/ and four domains meet their targets; /payments/, /finance/, /access/, /reforms/ (EN) and Home recorded with reasons (§2.2) → G2 | §2.2 |
| F-04 PR #51 adds phone length and pre-empts G1 | OPEN → G1 (challenger evidence) | assessed in DL-V2-001 |
| F-10 domain H1s repeat the lead; 4–5 lines | CLOSED for AR (every H1 ≤3 lines at 390); EN /finance/ runs to 4 lines at 390 → G2 (type size at 390; the S11 thesis stands) | §2.3 |
| F-11 design records incomplete; ESCALATIONS and DESIGN_DEBT open | OPEN → this file exists; escalations resolved in G3 | — |
| F-15 desktop has no direct route to the eight topics | CLOSED in B1 (DL-V2-006, DL-V2-007): one-step 21–25% → 92–100%, AI-simulated | §2.4 |
| F-16 Compare never returns a positive verdict | B2: Compare explains each verdict in one sentence (DL-V2-010); no qualified pair exists in the Master and none is manufactured → OPEN as an owner content question (per-wave Findex records) | §3.4 |
| F-18 diagrams/counts truth (304 vs 306) | OPEN → W6 | — |
| F-19 stale skill project files | handled (craft modules only) | — |
| G0-F01 interval on CLM-001 vs Methodology §07 | CLOSED in B1 (STAGE-B-S): the lead names the survey, the universe and the 2.8-point interval | §2.1 |
| G0-F02 /corrections/ self-contradiction | CLOSED in B1 (Master: the empty state names the selected record); seed 25 stays B2 | §2.1 |
| G0-F03 topics in one step (F-15) | CLOSED (DL-V2-007) | §2.4 |
| G0-F04 TOC >6 and strip overflow | CLOSED (DL-V2-004); strip vs list stays a G1 test | §2.3 |
| G0-F05 domain H1 and head order | S11 and S12 done; the first-screen unit stays G1/G2 | §2.3 |
| G0-F06 citation forms | CLOSED in B2 (DL-V2-009): APA 7, Chicago, BibTeX, RIS with record ID, edition and access date | §3.1 |
| G0-F07 chain step marker; CBY-Sana'a coverage | CLOSED in B1 (Master: signal classes never reach "Operation"; one coverage sentence on /payments/ and /reforms/) | §2.1 |
| G0-F08 /data/ and /measurement/ structure | CLOSED in B1 (S1, S2, S8, S9): AR 390 screens 70.5 → 18.7 and 44.7 → 23.4 | §2.2 |
| G0-F09 record → MA bindings; teaser scope | OPEN → B4b (Master bindings) + G2 (unit) | — |
| G0-F10 CLM-001 lead and clocks | CLOSED in B1 (OD-1017-08 lead; S13 dates; no raw route in prose) | §2.1 |
| 11 Reading link position on /remittances/ (S7) | OPEN → B2 | — |
| 12 CLM-003 source list order | OPEN → B2 | — |
| 13 boundary line outside the figure element (27 of 42) | → G2 (SIG-1) | — |
| 14 the record's "Return to interpretation" label | OPEN → B2 | — |
| 15 "Compare evidence" from a record preloads one record | CLOSED by decision in B2: the prompt for a second record stands; no arbitrary second record is chosen (DL-V2-010) | §3.1 |
| 16 three fonts = 220 KB per page | → W4F | — |
| B2-F02 local gate results were not predictive of CI: the local environment ran Python 3.12 while `requirements.txt` and CI pin 3.11, so PEP 701 f-strings compiled locally and the CI build failed | CLOSED in B2: the report form's fragments hoisted out of the f-string expression parts (rendered HTML byte-identical); `scripts/tests/test_python311_syntax.py` added as the guard and `compileall` added to CI; the repository's own pin is Python 3.11 (`requirements.txt`: "Pinned Python 3.11 toolchain … CI installs exactly this"), so the local environment was aligned to it rather than excused: Python 3.11.9 installed and a second virtual environment built from `requirements.txt` with Chromium, and the local gate chain now runs on it, interpreter version printed first. The 3.12 environment is left in place, unused by the gates, so no earlier result silently changes meaning. | §3.6 |
| B1-F01 tap targets under 24 px that predate B1 (the CC BY link, the contact e-mail links, the record breadcrumb, the long-cite summary) | → W4F/G3; the targets B1 introduced (topics block, measurement lists) were fixed in B1 | §2.3 |

### 1.12 Edition 2 (not built in this programme)

Level 2 by decision (economic-function interpretation, international-literature applicability, measurement
protocols, source-owner channels); public distribution of machine-readable records and embeddable cards (owner
decision under D4 and F-12); a machine-readable indicator dictionary (prepared, not published); question-continuity
route markers beyond a plain "return to the question" link; a Source Edition Lens beyond what Compare already shows.

### 1.13 Memos per family (charter §3.1; first versions, refined in G2)

**Home.** Obvious: the thesis, that evidence has different clocks, the strongest starting evidence, where to begin.
First questions: what is this; is 11.9% today's number; where do I start. Failure: clocks only implied; the
cite/report band sits under the H1; five topics invisible on desktop (§1.6, G0-F03). Options: (a) keep the
composition and add a topics line; (b) first-screen hypothesis (item 32); (c) PR #51's editorial gateway (longer).
Choice: TEST IN G1 (class C). Cost: G1 scope. More true: the clock; more complex: nothing if the unit replaces the
repeated context; removed: the duplicated system-context prose.

**Domain (/payments/).** Obvious: the strongest bounded answer, its main limit, the path to evidence. First
questions: how many terminals, since when, so what. Failure: 4-line H1, 13-entry TOC, answer in unmarked prose, no
verification link in the first screen, 26.8 screens. Options: S11 thesis H1 + S10 TOC + S6/S7 link lists (structure,
class B) and the unit at the head (G1). Choice: S first, unit in G1. Cost: Master transactions for H1s and labels.
Removed: duplicated Verify statements; the foot spine (S4).

**Record (CLM-001).** Obvious: exactly what the evidence is and is not, its source, its method. Failure: clock lines
above the title (S12), no interval, no measurement link, citation without domain or date. Options: S12 head order +
Master interval statement + unit third part. Choice: B1 + G2 (class B). Removed: q3 where it duplicates the record line.

**/data/.** Obvious: the original document and its relation to the public evidence, fast. Failure: 70.5 screens,
intro before the directory, groups open, rights lines repeated per card, tab strip clipped. Options: S1 (groups
closed), S2 (one rights line), S9 (order, merged boundary sections), facets first. Choice: S1+S2+S9 (class B); strip
vs list in G1. Removed: six boundary sections merged into one; per-card rights lines folded.

**Reading (CWR-012).** Obvious: a bounded argument with its evidence inspectable. Failure: 37 screens, chrome and
tables; the KPI teaser without its scope; no correction note. Options: S3 tables folded, teasers with scope (unit),
correction note from the ledger (seed 25). Choice: B1/B2 (class B); prose untouched.

**/measurement/.** Obvious: which missing evidence matters and what would change. Failure: 44.7 screens; preamble to
word ~662; "what would change" folded on all ten; index at the end. Options: S8 cards (priority, domain, title,
current evidence, decision it would strengthen visible; the rest folded), index first. Choice: S8 (class B).

**/methodology/.** Obvious: how evidence is accepted, compared, derived, corrected and bounded. Failure: 16-entry
TOC; §07 overclaims the interval (G0-F01); the D8 "Method and measurement" group. Choice: S10 tiers + Master fix (B1).

**Compare.** Obvious: whether comparison is legitimate before any difference is read. Failure: a record's "Compare
evidence" preloads one record; verdict reasons per field NOT_TESTED. Choice: B2 (T).

**Explore.** Obvious: find the question. Failure: measurement previews take ~2/3 of the page (S7). Choice: B1.

**Trust pages.** Obvious: CauseWay's role, corrections, accessibility, rights, footprint. Failure: /corrections/
self-contradiction (G0-F02); /contact/ report context needs JS. Choice: B1 (Master) + B2 (form).


## 2. B1 — structure rules (S), 17 October 2026, branch `pr/stage-b-s` on main `ce4ae5c8` (B0 merged as PR #57; Master `6a851a14…`, Page Specs `b3197c66…`)

### 2.1 What changed

The thirteen structure rules of BRIEF W4 (S1 source groups closed; S2 one rights statement per list; S3 figure data
tables behind a disclosure; S4 no phone foot-spine where Verify, Readings and Related already render; S5 curated lists
capped at six; S6 Verify as a link list; S7 teasers as a title plus one line; S8 measurement priority cards; S9 /data/
order; S10 a table of contents of at most six entries and none under six phone screens; S11 domain H1 as a short thesis;
S12 record head order; S13 human dates in public text), CR-S12/D8 (DL-V2-006), the F-15 topics decision (DL-V2-007),
OD-1017-04(b) and OD-1017-08 were implemented in the renderer (`scripts/yfie/`), the build (`scripts/build.py`) and the
gates (`scripts/validate.py`: RC-S10 new; RC-NAV, R4, PB-0422, RC-A1, E2-DATES and E2-PREC follow the new forms;
negative controls for each). Content went through two Master transactions, EN and AR together: **STAGE-B-S**
(`audit/stage_b_s/`, Master `5b200406…`, Page Specs `7fa18f0f…`, 74 cells: the D8 masthead row and the five hub labels
retired in place; seven domain theses (S11); nine period texts in words (S13); the CLM-001 lead with survey, universe
and interval (OD-1017-08; G0-F01, G0-F10); SDG 8.10.2 bound on CLM-001 and 8.10.1 stated on MA-005, with the UN
metadata as two new source records (OD-1017-04(b)); the /corrections/ empty state (G0-F02); the CBY-Sana'a coverage
sentence on /payments/ and /reforms/ and the chain step classes (G0-F07); the /people/ route in prose replaced by the
page's name; the POS comparability marker and the firm-finance severity form; the UI-TOC-* labels) and **STAGE-B-S2**
(`audit/stage_b_s2/`, Master `6a851a14…`, one label, UI-HOME-TOPICS). Three steward edits under OD-1017-03, each its own
commit: S10 tiers and caps (`0ef6cd01`), D8 hub numerals (`eb072951`), Home's map starting with the topics block
(`efd19111`). Ported from `code/navbar-disclosures-integration` by hand, credited to Mohammed Waleed in the CHANGELOG:
the Space key on the menu control, the menu-close threshold at 900 px, and the viewport-acceptance widths and checks.
Part 6 item 11 (the opened menu's language link keeps query and anchor) is in `site-src/app.js` with its browser test.
`audit/close_out/KEY_MIGRATION.csv` carries 16 B1 rows.

### 2.2 The scoreboard, G0 → S1 (the same script, routes, widths and states as §1.2)

| Route | AR 390 G0 → S1 | EN 390 G0 → S1 | EN 1440 | TOC (AR) | H1 lines AR 390 | ISO dates AR 390 | Target · result |
|---|---|---|---|---|---|---|---|
| / | 8.5 → **9.4** (+11%) | 8.4 → 9.4 (+12%) | 5.5 → 5.8 | 8 → 6 | 2 → 2 | 0 → 0 | P1 first screen; shorter · MISS by decision (DL-V2-007) |
| /explore/ | 14.5 → **8.6** (-41%) | 14.1 → 8.7 (-38%) | 11.4 → 5.6 | 6 → 6 | 1 → 1 | 0 → 0 | S7 · met |
| /people/ | 20.1 → **13.9** (-31%) | 18.8 → 13.3 (-29%) | 13.4 → 8.7 | 11 → 6 | 2 → 2 | 0 → 0 | −25% · met |
| /payments/ | 26.8 → **20.3** (-24%) | 25.7 → 19.8 (-23%) | 17.7 → 13.1 | 13 → 6 | 4 → 3 | 0 → 0 | −25%; TOC ≤6; H1 ≤3 · MISS (length); TOC and H1 met |
| /remittances/ | 24.4 → **17.3** (-29%) | 22.0 → 16.1 (-27%) | 15.0 → 10.0 | 12 → 5 | 3 → 3 | 0 → 0 | −25% · met |
| /firms/ | 20.3 → **13.9** (-32%) | 18.8 → 13.2 (-30%) | 13.4 → 8.2 | 12 → 6 | 3 → 2 | 0 → 0 | −25% · met |
| /finance/ | 17.0 → **13.4** (-21%) | 16.3 → 13.0 (-20%) | 10.9 → 8.0 | 14 → 6 | 3 → 3 | 0 → 0 | −25% (directive: every domain) · MISS (length) |
| /providers/ | 25.6 → **17.0** (-34%) | 24.5 → 16.6 (-32%) | 16.5 → 10.8 | 11 → 5 | 4 → 2 | 42 → 0 | −25%; ISO dates (S13) · met; ISO met |
| /access/ | 11.6 → **9.9** (-15%) | 11.3 → 9.7 (-14%) | 7.5 → 6.1 | 11 → 5 | 5 → 3 | 0 → 0 | H1 ≤3 lines; −25% (directive) · met (H1); MISS (length) |
| /reforms/ | 28.9 → **21.6** (-25%) | 28.4 → 21.6 (-24%) | 18.7 → 13.1 | 12 → 6 | 2 → 2 | 26 → 0 | −25%; ISO dates · MISS (length); ISO met |
| /evidence/ | 29.5 → **13.6** (-54%) | 29.1 → 13.7 (-53%) | 25.1 → 9.8 | 6 → 6 | 2 → 2 | 7 → 0 | EN ≤14 (S5) · met |
| /evidence/CLM-001/ | 9.0 → **10.4** (+16%) | 8.4 → 9.7 (+15%) | 4.8 → 5.2 | 7 → 6 | 3 → 3 | 0 → 0 | P1 holds · — |
| /evidence/CLM-003/ | 9.6 → **10.0** (+4%) | 9.5 → 9.9 (+4%) | 5.3 → 5.3 | 7 → 6 | 1 → 1 | 0 → 0 | — · — |
| /evidence/VIS-POS-TERMINALS/ | 16.8 → **16.1** (-4%) | 16.3 → 15.8 (-3%) | 10.0 → 9.3 | 7 → 6 | 2 → 2 | 0 → 0 | — · — |
| /evidence/compare/ | 11.0 → **11.9** (+8%) | 10.3 → 11.1 (+8%) | 6.2 → 6.7 | 3 → 3 | 2 → 2 | 0 → 0 | — · — |
| /readings/ | 7.7 → **8.1** (+5%) | 7.0 → 7.4 (+6%) | 4.4 → 4.5 | 3 → 3 | 1 → 1 | 0 → 0 | — · — |
| /readings/how-money-reaches-households/ | 37.2 → **36.1** (-3%) | 35.6 → 34.6 (-3%) | 23.6 → 22.2 | 11 → 6 | 2 → 2 | 0 → 0 | chrome and tables only · — |
| /data/ | 70.5 → **18.7** (-73%) | 68.1 → 18.3 (-73%) | 53.9 → 15.6 | 12 → 6 | 2 → 2 | 0 → 0 | ≤20 (S1, S2, S9) · met |
| /methodology/ | 25.6 → **15.9** (-38%) | 25.5 → 16.5 (-35%) | 18.9 → 10.1 | 16 → 6 | 2 → 2 | 0 → 0 | TOC ≤6 · met |
| /measurement/ | 44.7 → **23.4** (-48%) | 43.5 → 23.8 (-45%) | 29.1 → 15.5 | 11 → 6 | 2 → 2 | 0 → 0 | −40% (S8) · met |
| /about/ | 6.6 → **7.3** (+11%) | 7.2 → 7.8 (+8%) | 4.1 → 4.3 | 7 → 6 | 2 → 2 | 0 → 0 | — · — |
| /corrections/ | 4.8 → **5.2** (+8%) | 4.9 → 5.2 (+6%) | 2.9 → 3.1 | 6 → 0 | 1 → 1 | 0 → 0 | — · — |
| /contact/ | 3.8 → **4.1** (+8%) | 3.8 → 4.1 (+8%) | 2.2 → 2.4 | 5 → 0 | 1 → 1 | 0 → 0 | — · — |

Targets met: /data/ (≤20 in both editions), /evidence/ (EN ≤14), /measurement/ (−40% or better), /explore/ (S7),
/methodology/ (TOC ≤6), and the domains /people/, /remittances/, /firms/ and /providers/ at −25% or better in both
editions, /reforms/ in AR;
TOC ≤6 and H1 ≤3 lines on /payments/ and /access/ (AR 390); ISO dates on /providers/ and /reforms/ gone.
Recorded misses, each with its reason:

- **Home** grows from 8.5 to 9.4 AR 390 screens by decision (DL-V2-007: the topics block and the footer's topics group);
  the first-screen hypothesis (item 32) is G1's.
- **/payments/** 26.8 → 20.3 (-24%) against −25%: the remaining length is governed content — three signal
  groups with their text-first tables and the POS series — which S3 does not fold (it folds chart data only; the
  text-first table is the no-JS and print reading surface); the footer's topics group adds about 0.3 screens to every
  page. A further cut is a G2 composition decision, not a structure rule.
- **/finance/** 17.0 → 13.4 (-21%): four figure groups whose figures and boundary lines stay in view (S3 folds
  only their data); the chronology fold already noted as a G2 lever would take it past −25%.
- **/access/** 11.6 → 9.9 (-15%): the shortest domain; about 3.6 of its screens are the chrome every page shares
  (masthead, record line, map, footer). Its named target (H1 ≤3 lines, from 5) is met.
- **/reforms/** EN 28.4 → 21.6 (−24%) against −25% while AR meets it (28.9 → 21.6, −25%): the EN chain and event list
  run a few lines longer than the AR; the same G2 lever as /payments/ applies.
- Records and trust pages grow by 0.3–1.4 screens without a target: governed additions on CLM-001 (the OD-1017-08
  lead, the interval sentence, the SDG binding, the record line) and the footer's topics group on every page.

### 2.3 Chrome and structure facts after S (OBSERVED_BROWSER, High)

- Table of contents: at most 6 entries on every route and width; strip overflow 0 (G0: 134 cells); none on /corrections/, /contact/,
  /privacy/, /rights/, /terms/, /accessibility/ and the shorter records, decided per route on both editions.
- ISO dates visible: 8 tokens in 4 cells (G0: 616 in 24), all the two EN /providers/ status-ledger keys of DL-V2-005; 0 in prose.
- H1 at 390: every AR H1 ≤3 lines; over three lines in EN only: en /finance/ (4 lines, 84 characters); en /evidence/CLM-001/ (4 lines, 78 characters); en /about/ (4 lines, 84 characters) → G2 (type size at 390; theses unchanged).
- Tap targets under 24 px: 64 in 48 page×width cells (G0: 70 in 51); the ones B1 introduced (the topics block's links and the
  compact measurement lists) were fixed in B1 by the 24 px rule; the rest predate B1 (B1-F01 → W4F/G3).
- No horizontal overflow on any page or width; cold transfer at 390 is 231–318 KB per page with three font files (unchanged; W4F).
- /data/ renders with 0 open disclosures at 390 (G0: 2); its main text is 2628 words (G0: 10479); /measurement/ 3604 (G0: 7211).
- Journeys: every one of the 14 targets is at most 2 clicks from Home in both editions; Compare and the Reading now route through /remittances/.
- Home's first screen at 390: the figure is no longer in view in AR (G0: yes); EN unchanged (no); the evidence link stays in view in both.

### 2.4 First-click test (F-15, Part 6 item 14; `g0/firstclick_b1.md`)

| Variant | EN desktop | AR desktop |
|---|---|---|
| A — the built page after D8 | 5 / 24 (21%) | 6 / 24 (25%) |
| B — Home topics block, flat eight | 22 / 24 (92%) | 24 / 24 (100%) |
| C — Home topics block, four families | 23 / 24 (96%) | 23 / 24 (96%) |

Three AI-simulated first-time readers × eight tasks, judges blind to the variants, link labels and headings only.
B and C tie within one judgement; the flat eight is adopted (DL-V2-007). Not a usability study; no human testing.

### 2.5 Preservation check (IDs and data-* hooks)

Against B0 `d36a51bb`: 305 pages compared, none missing, none new. Gone: `edge-fN` (64; S4 — the link blocks are
re-hosted on `#verify`, `#readings`, `#related` and `#measure`) and `data-hub-num` (304; D8). New: `#shows` (16),
`#topics` (2), two source-record anchors (the UN metadata records), `data-record-line` (232), `data-fig-data` (56),
`data-toc-grouped` (46), `data-boundary-more`, `data-home-topics`, `data-ma-more` (2 each). Against the brief's
reference `2ddbfb61`: 291 pages compared, 14 pages new since (six source records and the Reading); every further
difference is already present in `d36a51bb` and belongs to Stage A's recorded changes. Deliberate changes are the
16 B1 rows of `KEY_MIGRATION.csv`.

### 2.6 Gates (the full set, after the last change)

Validator 306 pages / 0 errors (RC-S10, RC-NAV, R4, PB-0422, RC-A1, E2-DATES, E2-PREC, S04.1, P2-G01, P4-G01, R85-G09,
R86-G02, RP-G06); gate negative controls run locally with `--only`: the three RC-S10 controls and the RC-NAV/D8 controls
(caught), plus the built-in controls of the base-path and no-JavaScript suites — not the full suite (see the correction
below); literal audit 19,883 records, 0 unresolved, determinism one SHA over eight
seeds; source lineage truth 8/8; projections check PASS; generator unit tests 22 OK; content parity 304 documents, 0
differing; bilingual numeric invariance and number words 0 of 152 pairs; viewport acceptance 308/308; public tools
36/37 (one not applicable to the current data); security headers, base path, portable HTTP contract and no-JavaScript
PASS; diagrams, social images (302) and logo derivatives current; re-entry 15 tests OK; manifest and checksums
regenerated last. Idempotence held after each transaction.

**Correction, 17 October 2026 (owner directive in conversation).** PR #58 (`pr/stage-b-s` → main) is OPEN, not merged. CI on
its head `2509d22d` failed Gate negative controls shard 5/6 — "RC-1115 / S12: the FOR WHOM clock loses its q3 anchor" NOT
CAUGHT (27 of 28) — and therefore the aggregate check; Browser acceptance, Governance gates and shards 1–4 and 6 passed;
the Cloudflare Workers Build check is the F-06 owner item. Root cause: S12 keeps the q3 anchor on every record line (232 of
232), but the RC-1115 rule only enforced an aggregate floor (at least 200 record lines with the anchor), so one page
losing its anchor was invisible to it, and the B1 control expected that floor's message ("RC-1115 only …"). Fix, commit
`bf9b8323`: RC-1115 fails per record page whose record line lacks the FOR WHOM clock with id q3, and the control expects that
message. Local verification before the push: `--only RC-1115` caught 9 of 9; the full suite caught 167 of 167. The earlier
wording "negative controls CAUGHT" described only the `--only` subset and is withdrawn; this PR is reported again only
after Verify is 9/9 on its exact head. Also on record: OD-1017-14 (PR #59, merged at `3ef16ade`) prospectively selects a
DigitalOcean Droplet via EasyPanel at https://yemen-financial-inclusion.causewaygrp.com (`public_origin` stays null;
implementation stays Stage C); PR #51 stays as it is, conflicts included, as G1 design evidence to be closed without
merging.

### 2.7 Open after B1 → B2 / G1 / G2

B2 (T): G0-F06 citation forms (OD-1017-04a); seed 25 "what changed in this edition"; seed 27 Arabic search test set;
seeds 23 and 28 (ask once); G0-F09 record → MA bindings; the two EN-only time boundaries on /providers/ (DL-V2-005);
items 11, 12, 14 and 15 of §1.7; fin24*/fin28-29 method note; the report-an-error form. G1: DL-V2-001; strip vs
list; the first-screen hypothesis (Home's figure in AR); PR #51 as evidence. G2: the unit at three scales; the
boundary inside the figure element; /payments/, /finance/ and /reforms/ (EN) length (chronology fold); EN H1 size at 390. W4F: fonts;
B1-F01 tap targets. VIS-CAPITAL-CONTEXT `public_routes`: no defect established (carried, not open).


## 3. B2 — tools (T), 17 October 2026, branch `pr/stage-b-t` on main `8a772350` (Master `03d194a2…`, Page Specs `cf813880…`)

### 3.1 Before → after, per tool (BRIEF W4 T; every behaviour tested in a real browser)

| Tool | Before B2 | After B2 |
|---|---|---|
| Search | Arabic normalisation, aliases (46), ranking, one result per destination, typed facet, ?q= state, capped dialog with "see all", a plain empty state | The same, plus zero-result help: up to three alias terms the query resembles, the Questions hub and the same query in the other edition, each a link (`t_search_zero_help`); every result keeps its type and period line; the query-set gate P2-G01 (30 intents, EN and AR, expected destinations) is the search gate |
| Compare | Shareable `?records=` URL, verdict title and generic copy, boundary cards, copy link, plain-word link errors | One reason sentence per verdict naming the dimension (SIG-5), "Copy summary" with the verdict, reason, each record's scope and the link; the verdict stays above the values at every width (`t_compare_reason`) |
| Source directory (/data/) | Facets by type, publisher, year and domain; order; URL state; ?source= and #source-ID; Clear all; "Evidence records using this source" per source | The same, plus live counts on every facet option, following the term and the other facets (`t_source_facet_counts`); the per-source "used by" list is the brief's "cited by" |
| Report an error | A `mailto:` link that appeared only with a known record; a bare address otherwise | The structured form at /contact/#report (DL-V2-008): pre-filled context, seven error types, inline validation, reference code, fixed-format body, mail app or copy, a no-JavaScript mailto with the field list; every record, Reading and figure links to it with its IDs (`t_report_form`, RC-T1) |
| Cite | The governed short and long citations, previewed and copied | The same, plus APA 7, Chicago, BibTeX and RIS from the page's metadata (DL-V2-009; `t_cite_formats`) |
| Corrections | /corrections/ rules and the per-record history | The same, plus the link to `docs/CORRECTIONS_PROCESS.md` (triage, fix, log, reply, times) |

### 3.2 Content: transaction STAGE-B-T

55 interface labels (04_NAV_UX), EN and AR together (`audit/stage_b_t/`; Master `03d194a2…`, Page Specs `cf813880…`,
COMMITTED with idempotence): the report form (26 static labels and seven runtime messages), the citation format control and
its five runtime phrases, the Compare reason sentences, summary head and governed list separator (seven), the search zero-result help (three) and the
corrections process link (one). The Arabic was drafted with the English and reviewed by an AI Arabic editor against the
existing register (16 rows changed: the house term «إمكانية الوصول», «رابط الصفحة» for a page address, «بلاغ عن خطأ»,
«تاريخ الاطلاع», label-value forms for counts); one English ambiguity it raised ("figure" as a number) was resolved as
"chart". No page copy, number, period or universe changed.

### 3.3 Tests and gates

Browser (`scripts/tests/test_public_tools.py`, 40/41 passed, 1 not applicable): `t_report_form` (both editions;
negative controls: empty form, invalid address, unknown record; the figure link; the no-JS mailto), `t_cite_formats`
(four formats, parsers for BibTeX and RIS with negative controls, the Arabic edition, a page without a record),
`t_compare_reason` (reason per verdict, summary, same-record, input error, Arabic), `t_search_zero_help`,
`t_source_facet_counts`; the old `t_report_issue` is replaced. Validator: RC-T1 (every report link opens the form with
its IDs; the form keeps its fields and address, posts nowhere, keeps its no-JS mailto) with three negative controls
(run locally with `--only 'T:'`: 3 of 3 caught; the full suite, 170 controls with the three B2 additions, run on this tree before the push; its first run caught 169 of 170 and found a second control that B2's markup had outdated — "a record's report link loses its record", fixed in its own commit as RC-1115 was — and the re-run caught 170 of 170 faults caught on the tree at `95554840`). The full gate set after the last change (log `gates_b2b.log`, 0 failures): validator 306 pages / 0 errors;
literal audit 19,883 records / 0 unresolved, determinism one SHA over eight seeds; source lineage 8/8; projections PASS;
generator unit tests 22 OK; content parity 304 documents / 0 differing; bilingual numeric invariance and number words
0 of 152 pairs; viewport acceptance 308/308; security headers, base path, portable HTTP contract and no-JavaScript PASS;
diagrams, social images (302) and logo derivatives current; re-entry 15 tests OK; manifest and checksums regenerated last. Re-measured with the G0 script (`g0/t1_metrics.json`):
/contact/ AR 390 4.1 → 6.0 screens (EN 4.1 → 5.8), Compare 11.9 → 12.1, Home 9.4 → 9.5; TOC ≤6, strip overflow 0; tap targets under 24 px 64 (B1: 64).

### 3.4 F-16: the honest Compare

The Compare page already presents itself as a comparability checker (its governed intro: comparison legitimacy before any
difference). The test the brief asked for — whether the Master already supports one legitimately qualified pair — was run
on the built Compare data: of the 14 comparable records, no two share the recorded definition, population and method with
a different period. The Findex waves of 2011, 2014 and 2021 are published as one visual and one crosswalk dataset, not as
per-wave records, so admitting them would mean new public numbers bound by a transaction — an owner content decision,
not a tool change. Nothing was loosened (DL-V2-010).

### 3.5 Not done in B2, and where it goes

Seeds 23 (machine-readable records) and 28 (figure cards) are prepared only as decisions (ask once, §1.10) → C-stage
with the owner's answer; seed 25 ("what changed in this edition" on /corrections/ from the transaction ledgers) → B4c
with the Master section it needs; seed 27's test set is the existing P2-G01 probe (answerable intents) plus
`t_search_zero_help` (unanswerable and near-miss) — a committed unanswerable set in the probe file is a B4c addition;
G0-F09 bindings → B4b; the first-party report endpoint stays a hosting option (off).

### 3.6 The interpreter-version finding (B2-F02)

The first CI run of this branch failed at the build step: `scripts/yfie/families.py` raised "f-string expression part
cannot include a backslash" on Python 3.11. The report form built its input attributes inside f-string expression parts
(`f'{field("url", inp("url", " type=\"url\""))}'`), which PEP 701 legalised in 3.12 and 3.11 rejects. One cause, four
symptoms: Governance gates died at the build, Browser acceptance and the six negative-control shards were skipped
because they depend on it, and the aggregate failed in two seconds.

Why the local gates did not catch it. The local environment ran Python 3.12.10 while `requirements.txt` is titled
"Pinned Python 3.11 toolchain … (CI installs exactly this)" and all three CI jobs set up 3.11. Every local result,
including the 170-of-170 negative-control run, was therefore produced by an interpreter that accepts syntax CI rejects.
`CONTRIBUTING.md` §9 already stated the rule; nothing enforced it, and the newer interpreter hid the breach.

The closure has three parts. **The fix:** every fragment is hoisted into a local and only the local is interpolated;
the rendered contact pages are byte-identical in both editions, so no behaviour changed. **The guard:**
`scripts/tests/test_python311_syntax.py` reads every tracked Python file's f-strings and rejects a backslash in an
expression part or a nested string that reuses the f-string's own delimiter — the two PEP 701 relaxations a renderer
reaches for. It is textual by necessity: `ast.parse(..., feature_version=(3, 11))` does not re-impose the restriction,
which was verified before relying on it, and the detector was itself tested against five cases, including the
triple-quoted f-strings in the hosting tests that must not be flagged. CI gains `compileall` over `scripts`, `site-src`,
`audit` and `design` as the first governance step, so a syntax breach fails in seconds instead of after the build.
**The evidence after it.** The full chain and all 170 negative controls were re-run on Python 3.11.9 at `d819e4a7`: 0 failures and 170 of 170 faults caught. The identical 170-of-170 result on 3.12 is superseded, because an interpreter that accepts what CI rejects cannot speak for CI.

**The toolchain:** the repository's own pin is Python 3.11 (`requirements.txt`: "Pinned Python 3.11 toolchain … CI installs exactly this"), so the local environment was aligned to it rather than excused: Python 3.11.9 installed and a second virtual environment built from `requirements.txt` with Chromium, and the local gate chain now runs on it, interpreter version printed first. The 3.12 environment is left in place, unused by the gates, so no earlier result silently changes meaning.

What this says about the earlier gate reports: they were honest about what ran, but a pass on the wrong interpreter is
not evidence about CI. The B1 lesson (a control whose selector a structure change outdated) and this one share a shape:
a gate that cannot see the thing it is believed to cover. Both are now mechanically closed.

**Session boundary (owner instruction, 17 October 2026).** B2 is this session's stop. B3 G1 runs in a fresh session,
resuming from `audit/close_out/PROGRESS.md` and `design/evidence/v2/STATE.json` under §12 of the directive; PR #51
stays as it is, conflicts included, and is closed without merging when DL-V2-001 is recorded. Everything else in
`audit/OWNER_DIRECTIVE_2026-10-17.md` stands, including the final-line condition of §13. Hosting is settled on record
only: the appended OD-1017-14 of 17 October 2026 (PR #59 at `3ef16ade`) selects a DigitalOcean Droplet via EasyPanel
at `https://yemen-financial-inclusion.causewaygrp.com` prospectively, with `public_origin` still null, `pre_release`
still true and implementation in Stage C; no build, contract, workflow or DNS state changed in B2.

---

## 4. B3 — G1, the direction challenge, 18 October 2026, branch `pr/stage-b-g1` on main `8c78fa0e` (B2 merged as PR #60; Master `03d194a2…`, Page Specs `cf813880…`)

### 4.1 Method (charter §10; directive §9 "G1")

Candidates are CSS deltas appended to the shipped stylesheet in scratch copies of `dist/` (`design/exploration/v2/`,
regenerated by `build_candidates.py`); the HTML and JavaScript of every candidate are byte-identical to `dist/`, so
content parity, the literal audit and bilingual invariance hold by construction and the disqualifiers a stylesheet can
fail were measured (`g1/disqualifiers.json`: nothing hidden, no overflow, no JS). Proving pages: Home, `/payments/`,
CLM-001, `/data/`; views AR 390, EN 390, EN 1440, AR 1440. Three AI judges (Fable 5.1, high effort), blind to the
labels, scored 30 rendered views each on the nine charter criteria; the mapping was decoded after all three reported.
Measured columns: phone screens and the first-answer position at AR 390, cold bytes by type, font files. The
source-owner test (charter §3.5) ran on the five records in both editions for every candidate. No human testing; the
judges are language models reading rendered pages, and are reported as such.

### 4.2 The candidates

| | Led by | Hierarchy and reading order | Total (45 max per judge, ×3) |
|---|---|---|---|
| A · Register | the data professional | Plex only; two-column register head on wide screens; text-link tools; lighter rail; rules, not fills; list index on phone; topics as one line | **108** (ranks 2 · 1 · 1) |
| B · Argument | the statistician-journalist | the heading pairing (item 21); ruled masthead; serif deck; margin units; boundary as a ruled note; phone order title → figures → boundary → questions → topics | 106 (1 · 4 · 2) |
| C · Compact | the citizen on a phone | smallest chrome; compact scale; record rows with the clock inline; inline index; no rail; phone order title → figures → boundary → topics → questions | 102 (3 · 3 · 3) |
| D · Incumbent | — | T4 · Instrument as shipped | 93 (5 · 5 · 5) |
| E · Argument, compact | the hybrid | B's identity with C's phone economy and order | 102 (4 · 2 · 4) |

Round 2 isolated the pairing: F = A plus the corrected pairing (Latin inside Arabic headings at the Arabic's optical
size through `unicode-range` and `size-adjust`; the deck never above its heading). All three judges preferred A; the
pairing lost Arabic quality 9 to 12 and gained distinctiveness 12 to 9 (`g1/g1_scoreboard.md`).

### 4.3 What the judges saw (used as the G2 levers)

- The incumbent's phone first screen is spent on chrome: a two-line edition strip, boxed cite/report buttons above the
  statement, the topics grid; no figure before the scroll (every judge). A, C and E fix it in different degrees; C and E
  bring the figure to 0.7–0.8 screens by compact chrome and tools after the actions.
- The list index beats the chip strip on every phone view (G0-F04 closed: list).
- Fills read as "UI energy"; rules read as a statistical office (A, B, E all scored higher on tone than D).
- The register head on 1440 is the preferred desktop composition (A); C's rail-less page left the right half empty and
  lost the route to the record list and the index.
- The Arabic reader scored the largest, best-leaded Arabic body (B/E) highest on long text, and A's /data/ single-column
  numbered index highest on calm; A's weakness is the tools between the title and the statement on phones (E's order fixes it).
- The serif pairing: a four-line record title in EN 1440 and a Latin line that stands apart in Arabic titles.

### 4.4 PR #51 as evidence (closed without merging)

Survives into G2 as composition, not code: the page tools as text links (adopted by every candidate); the secondary
call to action as a link beside one filled control (B, E); the limit sentence adjacent to each Home observation
(a markup change: the G2 Home memo tests it against the ruled unit); the boundary before the in-page index on Home.
Not adopted: the second domain list under the questions (the topics block of DL-V2-007 already gives one-step reach);
the paper-coloured institutional footer (the colophon band is the institutional layer, charter §6.1); a body class per
route (the direction is one system). Its screenshots and metrics stay on its branch as lineage.

### 4.5 Item dispositions closed here

13 unit composition → the ruled unit (A); 19/32 first-screen hypothesis → confirmed by proxy, question entry with three
examples to the G2 Home memo (markup); 21 typography → pairing rejected on evidence, weight 600 kept, no new font file;
29 audience entry → DROP; G0-F04 strip vs list → list. Byte budget: A adds 1.0 KB of CSS and no font; AR /data/ stays at
322 KB cold (target ≤ 350 KB). The Medium (500) text weight (74 KB AR, 71 KB EN) is a G2 question: it stays unless the
proving pages show that two weights carry every role.

### 4.6 G2 order (charter §11)

Shell on the proving pages (the register head, the text-link tools after the actions, the one-line edition strip, the
list index, the rail) → Home (memo: the first screen; the limit beside each observation; the question entry) → domain →
record → /data/ → Reading → Methodology → propagation. Two refinement passes on each proving family; every class-C
candidate decided with evidence (the masthead treatment, the desktop TOC presentation, compact source rows, display scale).

---

## 5. B4a — G2, the shell on every family, 18 October 2026, branch `pr/stage-b-g1`

### 5.1 What changed (DL-V2-001 implemented in `scripts/yfie/theme.py`, edited in place; no parallel stylesheet)

- **Type scale** one notch down at every width: display 32/30 → 30/28 px on phones (EN/AR), 52/44 → 42/38 at 900 px and
  above; question headings 20/21 → 19/20 and 23/24 → 22/23; the paced lead 22/23 → 20/21. A governed title over 56
  characters carries `class="long"` (renderer helper `render.h1`, used by every family) and steps down a fifth, so the
  84-character titles of /finance/ and /about/ run to four lines at 1440 instead of six and five; nothing is shortened.
- **The register head** at 900 px and above for every head that has a statement (Home, the eight domains, /data/,
  Readings, /methodology/, /measurement/, the trust pages): title on the left, statement, the two calls to action and
  the tools on the right; the crumb, the family rubric and the governed question stay full-width above. Record heads
  (no statement) keep the stacked order with the clocks under the title.
- **The head actions inside the head** for the domain family (`families.head_block` takes the actions; the
  `.head-rule` wrapper is gone from domains), so the phone order is title, statement, actions, then the tools, and the
  register grid holds. Content parity, the cutover oracle and the literal audit are unchanged (the strings are the same).
- **The tools** (cite, report) are quiet underlined text links, after the actions on phones and in the register's
  right column on wide screens; the record family keeps them under the record line.
- **Rules, not fills**: the boundary section is a brass double rule with no panel; the Home record unit is a hairline
  above the record line with no plate; the figure is a white plate under its deep-green rule, open at the sides; table
  heads are ruled, not filled.
- **The phone index** is a plain numbered list (the chips, their clamp and their sideways layout are gone); the desktop
  rail is lighter and narrower (236 px, no side rule, muted tabular numerals, smaller rows).
- **Home's topics block** is one compact line under a small brass heading. **The edition strip** is one line at 390 in
  both editions (12 px Arabic, 12.5 px English, the clock size from 600 px).
- **Calls to action**: one filled, one outlined at one pixel, 40 px tall.

### 5.2 Class-C decisions (charter §2 C, §11)

| Candidate | Decision | Evidence |
|---|---|---|
| masthead treatment | kept as it is (five hubs, the logo lockup) | not a judged weakness in G1; D8 and the first-click test stand |
| desktop TOC presentation | the lighter rail, accepted | A's rail scored highest on source path and calm with the data professional; C's rail-less page lost the record list |
| compact source rows | decided in B4b on /data/ | — |
| display scale one notch down | accepted | every candidate that stepped down beat the incumbent on calm tone (A 13, C 12, E 12 vs 9) |
| the Home limit beside each observation (PR #51) | rejected | it repeats the records' and the boundary section's governed limits and lengthens Home (item 15: never adds length); the ruled unit with the record line is the composition the judges scored |
| the Home question entry with three examples (item 32) | DROP | the starting questions are section 9 and the search is one tap in the masthead; an entry above the figures would push the first figure out of the first screen, which is the owner's main complaint |

### 5.3 Pass one, measured (`design/evidence/v2/g2/pass1_before_after.md`; the same script and widths as G0)

Every route is shorter on both phones (Home 9.5 → 9.0 AR 390; /payments/ 20.4 → 19.6; /reforms/ 21.7 → 20.3;
/remittances/ 17.4 → 16.4). Home's AR 390 first screen now carries the first figure (11.9 % with its universe) and
the evidence link; records carry figure, clock and evidence link. No overflow at any width; targets under 24 px
unchanged (1 on the record family, carried from B1-F01 to W4F). Gates on the pass-one build: validator 306/0; literal
audit 19,883 / 0; content parity 304/0; cutover oracle; determinism; diagrams, social (frame hash), logo current;
projections; public tools 40/41; security headers; no-JavaScript; HTTP contract; base path; accessibility audit
(axe 4.10.2, 24 pages × 2 widths: 0 rule violations, 0 contrast failures, 30 targets under 24 px — the record under
`docs/ACCESSIBILITY_AUDIT.md`, which is a measurement, never a conformance claim).

### 5.4 The rendered-visibility gate (charter §12.1, new: `scripts/tests/test_rendered_visibility.py`)

One page per family in both editions at 390 and 1440: the answer, the head clocks, the boundary sections and the
tools are rendered and never inside a closed disclosure; no clamp, ellipsis or clip on governed text (the only
`overflow: hidden` allowed is the listed scroll wrappers and screen-reader text); every governed text node is rendered
or belongs to a listed set with its reason (screen-reader labels, the phone index and the foot rail which duplicate
the desktop rail and vice versa, print-only identity, the no-script note, regions the HTML marks hidden, a chart's
width-dependent tick labels, the phone-hidden product rubric the masthead already carries); every closed disclosure
has a visible summary. Two negative controls (`--self-check`: a hidden boundary; a clamped paragraph) are caught by
their own code. 44 page views PASS.

### 5.5 Pass two on the proving families

- **Home on a phone: figures before topics.** Under 900 px the three-figure section, then the index, then the topics
  line, then the boundary; on a wide screen the register keeps the topics line first (G1: the figure-first candidates
  scored 15 and 12 of 15 on first-screen comprehension against 12 for topics-first; the topics stay one step from Home
  at every width, so DL-V2-007 holds). Home AR 390: 9.5 (t1) → 8.9 screens; the first figure at 0.8 screens.
- **Disclosures as ruled rows.** The named bars of the folds (`details.fold`, `details.more`, Home's folds) lose
  their white boxes and sage fills and become ruled rows with the boxed +/− control, consistent with the direction.
- **Compact source rows** (class C): kept as they are — the source card's two-column grid from 1200 px and the stacked
  row on phones; the Arabic reader scored /data/'s single column highest on calm (G1). Decided: accepted as is.
- **The figure boundary inside the figure element** (G2 open item, 27 of 42 in G0): measured on this build, 67 of 67
  figures in the English edition carry the boundary part inside `<figure>` (closed by the B1/B2 frame work; recorded).
- **The English title tracking** stays at the V1 value (−.02 em): a nudge to −.018 em reached the social-card title
  through the generic heading rule and changed all 151 English cards for no visible benefit (fingerprint, §6).

---

## 6. B5 — W4F, 18 October 2026

- **Fonts.** Three files per edition stay (Regular, Medium, SemiBold of the text face): no face added (DL-V2-001),
  none removed. The Medium weight carries the statement, the clocks' labels, the controls and the source kinds; two
  weights would flatten the clock against its value and the kind against the title on the record family, so it earns
  its file. AR /data/ cold bytes 331 KB, within the ≤ 350 KB target; Home AR 274 KB (`g2/w4f_performance.md`).
- **Tap targets (B1-F01).** The accessibility audit on this build measures 5,126 targets, 30 under 24 × 24 px, of
  which 29 meet the inline exception and 1 the spacing exception: 0 meet neither. Closed on measurement
  (`docs/ACCESSIBILITY_AUDIT.md`, a measurement and never a conformance claim).
- **Social cards (charter §12.3).** `scripts/social_images.py --check` now compares a template fingerprint — the
  stylesheet rules the frame uses (token lines and every `social-doc` / `.soc-` rule), the `@font-face` block, the
  shipped font bytes and the logo — recorded in `INDEX.json` as `template_sha256`, with a negative control
  (`--check --control`: one byte of the frame CSS changed in memory reads as stale; CAUGHT). The cards were regenerated
  on the final stylesheet and compared byte for byte with the committed set (§5.5): the frame's own rules are
  untouched by G2, so the images are unchanged and only `INDEX.json` carries the fingerprint.
- **Performance before/after (P6).** `g2/w4f_performance.md` and `g2/perf_g2.json`: the only persistent bytes added
  are stylesheet rules (+1.7 KB gzip on every page); no JavaScript, image or font delta; first paint with the system
  fallback and no layout jump (font-display: swap, the preloads unchanged).
- **The chronology fold** on the long domains already exists (V1B-1); /payments/ 19.6 and /reforms/ 20.3 AR 390
  screens are governed signal tables and event lists (S-stage decisions), carried to the stage report as recorded misses.

---

## 7. B6 — G3 acceptance, 18 October 2026

### 7.1 The independent visual review (one fresh AI reviewer, Fable 5.1, before/after pairs of twelve views, both editions)

Verdict: English improved (calmer rail, demoted tools, better headline breaks); Arabic improved (tighter phone heads,
the boundary on the first phone screen of /payments/, nothing less readable); shaping and diacritics fine everywhere.
Three defects named, most severe first, and their disposition — corrected once, then the affected surfaces rechecked:

| # | Finding (view, region) | Disposition |
|---|---|---|
| 1 | The two-column head with a long statement leaves a blank title column (/data/, /methodology/, the Reading at 1440) and on /payments/ pushes the boundary section below the fold | **Corrected.** The register head is now applied by the renderer only where the statement is short enough to sit beside the title (`render.head_class`: ≤ 420 characters EN, ≤ 360 AR): Home, Explore, /about/, /measurement/. The domains, /data/, /methodology/ and the Readings keep the stacked head at the reading measure. /payments/ EN 1440: the boundary heading is back in the first screen (12.9 screens; before the fix 13.1) |
| 2 | The rail lost its numerals while the sections keep "01, 02 …", so the index no longer maps; the section numeral demoted to label size | **Corrected.** The numerals had hung 21 px into a rail padding the lighter rail no longer has and were clipped by the rail's scroll box; the hang is removed and the numerals are back in the primary green. The section numeral returns to 1.3 em in green as the anchor |
| 3 | Home's topics line absent from the Arabic phone first screen though present on desktop at that point | **Not a defect: a recorded decision** (§5.5, figures before topics under 900 px; the topics stay one step from Home at every width). Recorded here so the reviewer's reading is answered |

Reviewer's preferences, not taken: a lighter group-label weight in the rail's lower groups; the record family's
single column (right as it is, in the reviewer's own words). Also noted and carried: a Reading's figures in prose are
plain weight while the record marks them (`b.fnum` is a record and Home device by design, D3); the long Arabic titles
no longer step down (the `long` rule now applies from 72 Arabic characters).

### 7.2 The editors' reading (P9, charter v3.2): `g2/p9_editors.md`

PRESENTATION VARIANCE ACCEPTED: 0 material, 7 minor differences in hedging, causality or scope across CLM-001 (01, 04),
Home's clocks section, two Reading theses; the Compare verdict is not static. Two Arabic dual forms are correct only
if the Master holds exactly two figures and two reports — a content question for the owner's Arabic editor, not a
presentation item. An AI editorial reviewer; not a native-language certification.

### 7.3 The six-persona reader-job audit, re-run (charter §13): `g2/persona_audit_g3.md`

G0 → G3 outcomes: 1 PASS → PASS; 2 PASS with frictions → PASS; 3 PASS (naming partly met) → PASS (naming met);
4 INCONCLUSIVE → PASS with frictions; 5 PASS (marginal) → PASS; 6 FAIL → PASS with frictions. Closed since G0: the
interval on CLM-001, BibTeX/RIS, SDG 8.10.2 on the record, the Payments route and topics on Home, the definition at
zero clicks, the stage-row tag, CBY-Sana'a named, /corrections/ consistent, the Reading path one click shorter. What
persists is content (Master cells: the 45,460 teaser scope, sample n on CLM-001, the record → MA-001 binding, the
Reading's correction note) or a recorded structure decision (the priorities' fold, the Reading link position with the
index jump); two hosting-stage items (the path-only canonical and no-JS citation address until `public_origin` is set).

### 7.4 P1 on AR 390 per family (charter §13) and the recorded exceptions

Records: figure, clock and evidence link in the first screen (CLM-001, CLM-003, VIS-POS-TERMINALS). Home: the first
figure and the evidence link; the clock is the first record's, one screen down (exception recorded: the statement and
the two actions come first by the Home contract, item 19). Domains: the evidence link; the figure is governed prose on
every domain and the boundary section follows the head (exception recorded: a domain's first screen is its question,
title and statement by S11; the boundary at 1.0–1.2 screens on every domain). /data/, Readings, /methodology/,
/measurement/, trust pages: no figure in the contract; the evidence link where the family has one. Phone screens per
family, before and after: `g2/final_before_after.md`.

### 7.5 Gates on the accepted build

See §5.3 and the PROGRESS line of this PR: every standing gate and the four W4 gates (rendered visibility with its
two controls; the drift of `site-src/content/**` and the route list is zero — no transaction in this PR; the social
fingerprint with its control; the performance before/after) green on the exact tree pushed; the gate negative
controls run in full before the push. Never claimed: accessibility conformance, live performance, release readiness.

---

## 8. B4c — the G2 refinement and the integration branch, 18 October 2026, branch `pr/stage-b-g2` on main `1d37d9c6` (G1 merged as PR #61)

### 8.1 Recovery

PR #61 merged the G1 record and GitHub deleted `origin/pr/stage-b-g1`; the two G2 commits (`520a42f8`, `2e6bc8f4`) sat only in
the local checkout. They were rebased onto `1d37d9c6` as `a8e85144` and `64dd2d23` (trees byte-identical) and the branch
renamed `pr/stage-b-g2`. Nothing was reset, recreated or rewritten; the shipped stylesheet is still `scripts/yfie/theme.py`
edited in place. A second local session had run the gate negative-control suite on the `2e6bc8f4` tree (its PROGRESS line,
170 of 170, stands as that session's record; its worker copies overlapped this session's first edit, so the suite is re-run
on the final tree below).

### 8.2 The owner's visual-quality clarification (18 October 2026) and the three candidate shortcomings

The owner supplied three references — an Arabic Home with a large right-aligned title and an evidence example (primary), a
refined English-led Home (secondary: headline composition, spacing, institutional polish), and a second Arabic Home — as
sources of *quality*, not as templates: their figures, headings, illustrations, icons, cards, routes and layouts are not
reproduced; where a reference conflicts with a settled constraint (the display face, the card wall, the decorative map, the
icon set, the photo hero, the side-by-side bilingual page) the constraint stands. The accepted G2 pages (§5–§7) were
inspected first at AR 390 (Home, CLM-001, /payments/) and EN 1440 (Home, /data/, CLM-001). Against the references' qualities
— exceptional Arabic editorial typography, confident hierarchy, elegant whitespace, balanced asymmetry, subtle brass
detailing — at most three shortcomings were named:

| # | Shortcoming in the accepted G2 output | Disposition |
|---|---|---|
| 1 | The head has no fixed point: rubric, title, statement and actions stack with even gaps, and the finding does not part from its statement (the reference's title carries a short brass rule) | **Changed** (DL-V2-011): a 36 × 2 px brass-300 rule under every page title, at the start edge (right in Arabic), 12 px below the title and 8 px on phones. One rule, every family, both editions; no element, text or font added |
| 2 | Title and statement share the primary ink, so on the Arabic phone head (28 px title, 20 px statement, both dark) the title does not lead | **Changed** (DL-V2-011): the head statement in the secondary ink (`--ink-2`, 8.6 : 1 on the paper), its figures in the primary ink through the existing `.head .st b` rule. V1 had the secondary ink; G2 pass one had set the primary for the register and the Arabic phone paid for it |
| 3 | The Arabic phone head opens bare under the edition strip (the reference carries a small brass rubric above the title) | **Not changed**: the product rubric is hidden on phones by a recorded decision (the masthead already carries the product name; §5.4 lists it among the hidden sets), and a second rubric would push the first figure out of Home's Arabic first screen (the owner's main complaint in G0) |

Candidates were rendered live on the built site (the gzip server of `g0_measure.py`, the rule injected as a style tag, no
file changed): v0 as shipped, v1 the anchor alone, v2 the anchor with the secondary-ink statement, on AR 390 Home and
/payments/ and on EN 1440 Home and CLM-001. v2 read best in both editions: the Arabic title regains its lead, the English
register head reads title → statement → actions in order, and CLM-001's title parts from its clocks. The first-screen
cost on phones was measured and the phone margin set to 8 px (`g2/refinement_head_390.md`).

### 8.3 Verification on the final tree (every number from this tree, the pinned interpreter Python 3.11.9)

- Build deterministic (clean tree after the rebuild); literal audit 19,883 records / 0 unresolved; validator 306 / 0;
  content parity 304 / 0; projections, diagrams, logo current; social cards current with the template fingerprint and its
  control (the anchor rule is not a frame rule; the 302 cards are unchanged); literal-audit determinism.
- Browser: rendered visibility 44 views with both controls; no-JavaScript; security headers 306 pages; base path; public
  tools 40 / 41 (1 not applicable).
- Accessibility audit (axe 4.10.2, 24 pages × 2 widths): 0 rule violations, 0 contrast failures, 5,126 targets, 30 under
  24 px (the same 30 as §6; 0 fail both exceptions) — a measurement, never a conformance claim.
- Phone screens and first-screen proxies re-measured with `g0_measure.py` on the same routes and widths as G0–G3
  (`g0/g2r_metrics.json`, `g2/final_before_after.md` updated with the g2r column): no route moves by more than 0.1
  screen at 390 in either edition, no overflow at any width, the H1 line counts unchanged, Home's and the records'
  first figure still in the Arabic first screen.
- The twelve `after_*` shots re-rendered on this tree; `before_*` and `pass1_*` untouched.
- Gate negative controls, full suite, on this exact tree: the PROGRESS line of this PR records the result.

Never claimed: accessibility conformance, live performance, release readiness. Stage B ends with this PR's report.
