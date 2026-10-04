# Product challenge (Part B B15) — findings, red team, what was built

**Status, 3 October 2026.** One pass, as the brief asks (B15 a–f). The panel read the built site (`dist/`) in both
languages at 390 px and at desktop width. None of its members wrote any part of this pull request. Its findings were
reproduced, then attacked by a red team that could block a finding only for a stated reason of truth, safety,
accessibility or governance, never for effort. This record lists every finding ranked by value to the user, the red
team's verdict, and what happened to it. The roadmap (`docs/ROADMAP_V1_1.md` §3) carries every finding not built, in the
same ranking.

## 1. Panel and method

| Panel | Lenses | Users |
|---|---|---|
| A | Arabic-first reader; accessibility and mobile | U1 a citizen reading Arabic on a phone over a weak connection; U8 a humanitarian cash-programme manager; U10 a government policymaker |
| B | Evidence and measurement lead | U2 a Central Bank of Yemen supervisor; U3 a bank or microfinance strategy officer; U4 a payment or remittance provider; U9 a donor programme officer |
| C | User experience and information architecture; interface (the accepted D7 design is the baseline) | U5 a journalist on deadline; U6 an academic researcher; U7 a World Bank, IMF or development-finance economist |

Each user ran the brief's tasks (B15 b) and recorded where they failed or hesitated. The red team reproduced every
finding against `dist/`. Search was run through a harness of `dist/assets/app.js`.

**Tasks that failed or hesitated, before the fixes.**
- Search in Arabic for a common term: «تعز» returned «تعزيز» titles. «المرأة» missed the gender-gap record that «النساء» found.
- Find the account-ownership gap and say what it does not show: found, but the chart printed 9 and 11.1 where the text
  printed 9.0 and 11.10.
- Judge whether rising POS numbers show more use: answered, but /payments/ said only what POS growth does not show.
- Cite one figure correctly: the copied citation was about 150 words and named no original locator.
- Find what should be measured next: Home named three gaps with no route to the priorities. Explore showed five of the
  eight P0 priorities without saying why.
- Find how many providers are on the official list and what it does not show: found. But the enforcement record said the
  2026 decisions "are matched" with the roster, while /providers/ listed that matching as an open question.
- Search for a number: "6245" found nothing, and "6,245" became "245".

**Tasks that passed.** Find the 2024 CBY circular on unlicensed e-wallets (by "circular", not by "decision"). Compare two
records and say whether they can be compared. Find the sources behind one Reading and open one original. Find who
publishes the resource and how it is funded (on /about/, after a hesitation: C-6). Report an error in a record (A-13
polish only). Understand, in plain Arabic, what share of adults has an account and what that does not mean (A-11
polish). Trace a remittance figure and its revision to the original sources (C-7: page locators would make it faster).

## 2. Findings, ranked by value to the user

**Value** is the red team's score, 1 to 5. **Outcome** is one of:
- **BUILT**, with the commit.
- **PARTLY**, saying what was built and what is in the roadmap.
- **BLOCKED**, with the red team's reason.
- **ESCALATED**, to the steward or the owner.
- **ROADMAP**, not built because its value is low or the next step needs data, a decision or a contract.

| Rank | ID | Value | Finding (page, task, what happened) | Change | Cost / risk | Red team | Outcome |
|---|---|---|---|---|---|---|---|
| 1 | C-5 | 5 | Search for a number: "6245" found nothing; "6,245" became "245"; "11.9%" ranked an enforcement record first | Normalise separators (`,` `٬` `٫`); match numbers whole; mirror the rule in the validator | Code; low | ALLOW WITH CONDITION (mirror in validate.py) | BUILT, 9236ffc |
| 2 | A-2 | 4 | Arabic search matched inside words («تعز» → «تعزيز») | Arabic words match from their start, with proclitics; identifiers and digits keep substring matching | Code; low | ALLOW WITH CONDITION (regression-test the aliases) | BUILT, 9236ffc |
| 2 | A-3 | 4 | «المرأة» missed CLM-002 while «النساء» found 13 | A governed alias group widens the query; literal hits rank first; the boundary note is kept | Code; low | ALLOW WITH CONDITION | BUILT, 9236ffc |
| 3 | A-1 | 4 | After one failed load of the search index, search stayed broken until reload | Drop the failed promise, so the next search retries | Code; none | ALLOW (a retry button needs a new string) | BUILT, ff3a8fa; the retry button is in the roadmap |
| 4 | B-1 | 4 | CLM-019 said the 2026 decisions "are matched" with the roster. The Master marks every subject `BASE_ROSTER_MEMBERSHIP_NOT_YET_RECONCILED`, and /providers/ lists the matching as open | "Would have to be matched with the roster … that matching has not been done", in CLM-019, CLM-009, VIS-PROVIDER-TIME and the site-map description; each decision stays attached to the entities it names; no count added | Master copy; truth fix | ALLOW WITH CONDITION (no names; adversarial review) | BUILT, RC-15 |
| 5 | A-8, B-5 | 4 | Home §7 names three gaps with no links. Explore showed five of eight P0 priorities without saying why. /measurement/ put P1 before P0 | MA-003 and MA-005 bound to Home beside MA-001 and listed by their governed titles, with a governed line that a link is not a claim to close or explain a gap. MA-002, MA-009 and MA-010 bound to Explore, which now shows every P0 item and says so. /measurement/ lists P0 then P1, each in ID order | Master data and copy, code; low | ALLOW WITH CONDITION (governed titles; no sort beyond the governed class) | BUILT, RC-15 (gate RC-B15) |
| 6 | A-7 | 4 | From Explore to /payments/, the Reading on whether transfer accounts stay in use was not reachable from the page, and «المساعدات النقدية» found nothing | Alias 026 gains "cash assistance" and «المساعدات النقدية» | Master data; low | ALLOW | PARTLY, RC-15. Surfacing CWR-010 on /payments/ is not done: an answer page carries at most two Readings and /payments/ has CWR-005 and CWR-009, so which one gives way is an editorial choice. An inline link needs an inline-link mechanism in governed prose. Both are in the roadmap. /payments/ reaches CWR-010 through MA-009's card |
| 7 | C-2 | 4 | The copied citation was about 150 words and named no original locator | Owner decision OWN-04 launches with a short citation: title, record ID, CauseWay, edition, then each original source as publisher, title and locator, then the record's address. The long form, with period, population and limits, stays one disclosure away and copies on its own | Master copy and code; low | ALLOW WITH CONDITION (governed template keeping the ID and edition; long form kept) | BUILT, RC-15. An access date is not added, because the edition date fixes the version. A publisher in the source card's copied reference is in the roadmap |
| 8 | C-1 | 4 | CLM-002 (the gender gap) is men's minus women's account ownership, but its only locator was the total series | The record's source links carry the two series it subtracts, already registered in the source library; the source card lists them | Master data and code; low | ALLOW WITH CONDITION (locators from the register, not built in code) | BUILT, RC-15 |
| 9 | B-6 | 4 | The 32-measure demand-side panel (CLM-026) was buried; /measurement/ did not show it | CLM-026 bound to /measurement/, among the records that revealed the gaps | Master data; low | ALLOW WITH CONDITION (no feasibility upgrade, no ranking) | BUILT, RC-15. Splitting each priority into "analyse what exists" and "collect new" is in the roadmap |
| 10 | A-9, A-10, C-16 | 3 | The gender-gap chart printed "9" and "11.1"; the text printed "9.0" and "11.10". «9 نقطة مئوية» | A difference prints at the precision of the published values it is calculated from (which also settles the Arabic agreement) | Code; none | ALLOW | BUILT, the B15 d figure commit. A-9's request to add the boundary to Home's cards is in the roadmap: CLM-003's boundary alone is 96 words, Home's first screen is already long (C-15), and boundaries may not be collapsed |
| 11 | A-17 | 3 | 43 Arabic pages showed raw left-to-right paths as link text («السجل الكامل: /ar/evidence/…»), often linking a page to itself | On screen, the governed «افتح سجل الدليل» label and no self-link; "Full record:" with the path stays in print and detached frames | Code; low | ALLOW | BUILT, the B15 d figure commit. Arabic month names in meta lines are in the roadmap |
| 12 | B-3 | 3 | CLM-007 said the IMF history "shows materially higher" inflows; the chart legend says "Reported by the source" while CLM-036 documents a model-based reconstruction | "Gives a higher value for remittance inflows in 2024 than in 2018" | Master copy; low | **BLOCK** relabelling the legend "may include model-based" (truth: CLM-036 disclaims the scope of specific values, so it cannot be carried onto the Article IV history unread). ALLOW the wording | BUILT (wording), RC-15. Legend BLOCKED. A link to CLM-036 from the chart's boundary needs an inline-link mechanism; CLM-036 is already bound on /remittances/ |
| 13 | B-10 | 3 | "decision 2024 e-wallets" missed CLM-015. Decision No. 23 of 2024 and the e-wallet circular share 26 June 2024, unexplained | One sentence in CLM-015: the decision carries the same date; the circular and the decision are separate instruments; the record establishes no link between them. The decision is listed among the record's sources, in the context role | Master copy; adversarial review | ALLOW WITH CONDITION ("separate instruments, no link established") | BUILT, RC-15 |
| 14 | C-3 | 3 | Compare's description promised geography and unit rows it does not show | The description and the first section name the rows Compare shows; geography and unit are read on each record | Master copy; low | ALLOW (fix the intro) | BUILT, RC-15 |
| 14 | C-4 | 3 | Compare at 1440 px clipped a four-record table in a 584 px column | Compare's output spans the full width at 1200 px and above | Code; low | ALLOW | BUILT, ff3a8fa |
| 15 | B-12 | 3 | /payments/ said what POS growth does not show, never what the transaction series supports | One sentence: the reported totals are higher in June 2026 than in March 2025, but did not rise steadily and fell in several months; scope continuity across the July 2025 change of format not verified. No change computed. The chart note no longer asserts one reporting scope | Master copy; adversarial review | ALLOW WITH CONDITION (bound to VIS-POS-TRANSACTIONS; no computed May change) | BUILT, RC-15 |
| 16 | A-4 | 3 | «الإنترنت» found nothing, though a governed landscape row names "phone and internet" capability | Alias 028: internet / connectivity, «الإنترنت» / «الاتصال» | Master data; low | ALLOW WITH CONDITION (alias Master-first; landscape rows indexed by the generator) | PARTLY, RC-15. Indexing the landscape rows and linking «ابدأ من الأسئلة» are in the roadmap |
| 17 | A-15 | 2 | The search input overflowed its dialog by 30 px | `box-sizing` and width | Code; none | ALLOW | BUILT, ff3a8fa |
| — | B-2 | 4 | One of the 12 names in the 2024 e-wallet circular is published (NEG-EW-011) and eleven are not; the entity records are not linked from CLM-015 or CLM-019 | Publish a naming rule; treat the 12 alike; link parents to children | Owner decision | ESCALATE names to the owner. Do not name the other 11: the list is dated 2024 and marked DO_NOT_CARRY_FORWARD, a fairness risk. Parent-to-child links: ALLOW | ESCALATED (owner, `design/ESCALATIONS.md`). Parent-to-child links are in the roadmap |
| — | B-7 | 4 | VIS-MFI-SPINE, "observations by date, with gaps and breaks shown", renders no chart or table | A dated table of the governed observations, gaps printed "no usable observation — not zero" | A visual contract that binds the observations | ESCALATE to the owner (A4/C6, table-only record); the title must not promise "gaps shown" meanwhile | ESCALATED (owner). B12's dispositions name the missing input. The red team's condition is met in RC-16: the title reads "…, with their gaps and breaks" |
| — | C-7 | 4 | CLM-032's sources are 51- and 54-page PDFs; the method says only "balance-of-payments tables" | A page and table locator on source links | Master data from reading the sources | ALLOW WITH CONDITION (locators from the source) | ROADMAP (needs the sources read page by page) |
| — | A-11 | 3 | 80 words of abstract before the first number on /ar/; jargon unexplained | A short governed bilingual glossary; link CLM-001 to the access-and-use figure | Master copy | ALLOW WITH CONDITION (no new route) | ROADMAP |
| — | A-12 | 3 | About is not in the 390 px menu; the funding heading does not say funding; the publisher is written only "CauseWay" in Arabic text | About in the menu; an alias; «كوزواي» | Contract and copy | **BLOCK «كوزواي»** (governance: the owner set "CauseWay" in Latin script only). Menu: ESCALATE to the steward | ESCALATED (steward). Alias and heading in the roadmap |
| — | A-16 | 3 | Very long mobile pages; the page index comes after section 01; no back-to-top | Collapse the index at the top; a governed "back to top" | Code and copy | ALLOW WITH CONDITION (collapse only the index, never the evidence or its boundaries) | ROADMAP |
| — | B-8 | 3 | The 2015 microfinance "observed fall" does not say whether the provider set was the same | A "same provider set: yes / no / unknown" flag from the source | Master data | ALLOW WITH CONDITION (from the source; "unknown" is valid) | ROADMAP |
| — | B-9 | 3 | The 2025 and 2026 rosters sit on separate pages; neither warns that the difference is not net market entry | One comparison line with that warning | Master copy | ALLOW WITH CONDITION (no computed difference; licence ≠ operation) | ROADMAP |
| — | C-6 | 3 | Funding sits mid-paragraph on /about/ with no heading; nothing says what CauseWay is | A "Who publishes and funds this" heading; the organisation's description from the owner | Master copy; owner text | ALLOW (heading); the description only from the owner. Menu: ESCALATE | ROADMAP (heading); ESCALATED (menu, steward; description, owner) |
| — | C-8 | 3 | At 390 px, "Cite this page" is not in the header or the menu | Cite in the mobile header | Navigation contract | ESCALATE to the steward | ESCALATED (steward) |
| — | A-5, A-6 | 2 | Cross-language queries return nothing; the first search downloads a 2.0 MB index (324 KB compressed) | Search the other language on zero hits; split the index by language at build time | Code | ALLOW | ROADMAP |
| — | A-13 | 2 | The report link drops the record ID at 390 px; the email subject mixes languages; the body is empty | Carry the record ID; governed Arabic subject; a body without personal-data fields | Code and copy | ALLOW | ROADMAP |
| — | A-14 | 2 | Without JavaScript, search and menu buttons do nothing | Hide script-only controls without script | Code | ALLOW | ROADMAP |
| — | B-4 | 2 | Three remittance gaps have no Measurement priority of their own | A new priority | Master | **BLOCK** the new priority (governance: an eleventh priority is closed, REJ-02). Aliases to MA-001: ALLOW | BLOCKED; aliases in the roadmap |
| — | B-11 | 2 | "Issuing authority: Unknown — not zero"; a check date read as a list date; the slug "microfinance-structural-divergence" while the figures show no divergence | Wording; rename the slug before launch | Master copy | ALLOW (slug only before launch) | ROADMAP. The check-date part was fixed in RC-14 |
| — | C-9 | 2 | A Reading's figure linked to the Reading itself | Suppress the self-link | Code | ALLOW | BUILT with A-17, the B15 d figure commit (a Reading's own figure no longer links the Reading to itself) |
| — | C-10 | 2 | "Data & sources" holds no data; labels blur; no domain strip | A domain strip; labels | Navigation contract and copy | ESCALATE the strip to the steward | ESCALATED (steward); labels in the roadmap |
| — | C-11, C-13, C-14 | 2 | /data/ keeps empty groups when filtering; Compare preselects two records; the 404 opens in Arabic for /en/ paths | Hide empty groups; start Compare empty; the path's language first | Code; hint text governed | ALLOW | ROADMAP |
| — | C-12 | 2 | /evidence/ "Start here" opens with roster and enforcement records, not the headline records | Reorder the /evidence/ Page Spec's bound records | Master data | ALLOW | ROADMAP |
| — | C-15 | 2 | Home's opening fills the 390 px first screen; "Another view of the evidence" repeats a card | Shorten the opening | Master copy | **BLOCK** removing "Another view" (truth and accessibility: it is the system figure's text description and Home's only "not causal, not composite" boundary). Shortening: ALLOW | BLOCKED (removal); shortening in the roadmap |

## 3. Game-changer answers (B15 e)

Each user lens named the one capability that would make the resource indispensable. Each answer was judged against the
evidence the repository holds.

| User | Capability named | Judgement | Outcome |
|---|---|---|---|
| U1 citizen | A one-tap share card in plain Arabic: the record's title, period, population, what not to conclude, and the link | Buildable now with governed fields only, the boundary verbatim and never cut, and one new label | BUILT, RC-15: "Share this record" on every Evidence Record. It uses Web Share on a phone and copies the same text elsewhere. Links stay relative until the public origin is set (OWN-03) |
| U5 journalist | Paste any number and get the record, a safe sentence, what not to say and a short citation | Number-aware search (C-5) and the short citation (C-2) deliver it from governed text; summaries are shown verbatim, never generated | BUILT (C-5, C-2). A "safe sentence" copy control is in the roadmap (Owner Addendum 2) |
| U9 donor | A measurement portfolio that separates "analyse what exists" from "collect new" | Partly buildable: CLM-026 now sits on /measurement/ (B-6). The split needs governed copy per priority; no ranking and no eleventh item | PARTLY; the split is in the roadmap |
| U10 policymaker | A one-page Arabic decision brief per policy question | No new route (rule 2). The existing answer page and its priority card print with their boundaries | Available through print; no strength rating (BLOCKED: none is governed, and composites are closed) |
| U8 cash manager | A checklist for tracking whether transfer accounts stay in use | No file before the licence decision (OWN-04). The Reading CWR-010 and MA-009 print. Any new wording keeps "cash-out is not failure" | Available through print; a checklist is in the roadmap |
| U4 provider | A dated rulebook and status timeline per provider class | Partly buildable from the system chronology and the e-money rule stack. Needs a contract; chronology ≠ causality; no names | ROADMAP |
| U2 supervisor | An entity-level status register | **BLOCKED**: it would publish names and is the closed regulatory record route. The dated table without names stays | BLOCKED |
| U3 strategy officer | Dated observation tables with comparability flags, downloadable | The tables wait on B-7's contract and B-8's flags; downloads wait on the licence | ESCALATED (owner: A4/C6, OWN-04) |
| U6 academic | A fixed citation per record and edition, with BibTeX or RIS | The short citation fixes the record and edition (C-2). A BibTeX or RIS file is an export | PARTLY (C-2); the file ESCALATED to the owner (OWN-04) |
| U7 economist | A versioned dataset of all records | `scripts/exports.py` is ready; `public_downloads` is false (REJ-03 until a licence exists) | ESCALATED (owner, OWN-04) |

## 4. Reviews of the built changes

RC-15 had one bilingual reviewer (Arabic first) and one adversarial reviewer, because it states regulatory facts
(B-1, B-10, B-12). Both returned NOT ACCEPTABLE at the first run. Every finding was folded into one rerun, and the
transaction was then committed (ledger: `audit/release_candidate/runs/RC-15_MASTER_LEDGER.json`, 44 cells).

**Adversarial review**
- **B-1, two limitation fields: wrong as first worded.** The first wording said "each decision would have to be matched
  to named entities … that matching has not been done". But each decision *is* attached to the entities it names: the
  status events record their subjects, and the record's own method says so. What has not been done is matching those
  entities with the roster. The roster's names are not in the Master (`ROW_LEVEL_NAMES_NOT_YET_NORMALIZED`), and all 34
  subject rows read `BASE_ROSTER_MEMBERSHIP_NOT_YET_RECONCILED`. Both languages now say exactly that, and the RC-B15
  gate bans the withdrawn wording.
- **B-10, CLM-015 named Decision No. 23 of 2024 without listing it as a source** (rule 5). The decision is now among the
  record's sources, in the context role, with its locator.
- **B-12: holds, worded more tightly.** Counts fell in 6 of 15 monthly steps. Most of the net rise comes at the July
  2025 change of release format, where scope continuity is not verified. The sentence now says the series "did not rise
  steadily and fell in several months", and names that change.
- **Held as written:** B-1's summaries, B-3 (USD 1,329.2 million in 2018, USD 1,861.7 million in 2024, both
  `HISTORICAL_REPORTED`, Table 4), C-1 (the two series are exactly the ones the method subtracts) and the entity-name
  sweep (no enforcement-decision name in `dist/`).

**Bilingual review**
- **UI-HOME-GAPS-NOTE: blocking.** «أدلةً تنقص إحدى هذه الفجوات» can be read as "evidence that reduces a gap", the
  claim the note exists to deny. It now reads «أدلةً ما زالت مفقودة تتصل بإحدى هذه الفجوات» / "evidence that is still
  missing for one of these gaps", and "Listing it here does not claim…".
- **Minor findings, all applied:**
  - The Explore line names the page and the class apart.
  - VIS-PROVIDER-TIME no longer reads as having two reasons inside one "because"; it also gains a missing comma.
  - The site-map description no longer lets "not yet matched" attach to the roster.
  - CLM-009's Arabic keeps «مطابقة» beside «مع القائمة».
  - /payments/ s2 has a clear referent ("supports only a narrower reading") and the record's own term
    «استمرارية نطاق الإبلاغ».
  - CLM-015 says "the circular and the decision" instead of "the two".
  - CLM-007's Arabic now matches the English «تقدير وتوقعات، لا قيم مُبلَّغ عنها».
  - «الصيغة المطوّلة» replaces «الصيغة الكاملة», so the short citation does not read as incomplete.
  - Alias 028 adds «الاتصال بالإنترنت».
- **An older note contradicted the record.** The /payments/ chart note (UI-VIS-NOTE-POS-H1-WITHHELD, RC-11b) said each
  monthly release reports "within the same reporting scope", but the record says continuity across the July 2025 change
  is not verified. The note now says so.

**Recorded, not changed here.** /providers/ says some 2026 decisions "were issued before the roster and some after it"
while also saying the roster's issue date is not stated. The only date anchor is the roster file's date (22 September
2026). This predates the pull request and is left for the steward (roadmap §3).

## 5. What this record does not do

It does not claim WCAG conformance, legal review, rights clearance, native-language certification or a security
guarantee. It publishes no enforcement-decision entity name. It declares neither DESIGN HANDOFF READY nor PUBLIC RELEASE
READY.

## 6. Erratum (3 October 2026, appended)

- **A-7.** §2 says /payments/ reaches CWR-010 "through MA-009's card". That is wrong. /payments/ shows only the MA-002
  and MA-007 cards (the page's measurement limit), so CWR-010 is two clicks away, through CLM-045 in "Verify it
  yourself". The sub-item audit of Owner Addendum 2 found this. The direct link stays an editorial choice
  (`docs/ROADMAP_V1_1.md` §3, item 2). The RC-15 docstring and changelog repeat the claim; this line corrects all three.
- **B-2 and game-changer U2.** The owner decided on 3 October 2026, 09:05 Cairo (`audit/OWNER_DECISIONS_2026-10-02.md`,
  point 2) to withhold all twelve names of the 2024 circular alike, including NEG-EW-011's. This was done in RC-17, and
  the Addendum's instruction that "We Cash" rank first in search is withdrawn.
- **A-12, C-6, C-8.** About and Cite reach the phone menu through the owner's one-patch steward designation (point 3).
- **C-10.** The domain strip is not in this release (point 4; roadmap §3, item 27).
- **What CauseWay is (C-6).** No new organisational description in this release (point 7).

