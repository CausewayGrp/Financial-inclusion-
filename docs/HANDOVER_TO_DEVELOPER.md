# Handover to a human developer

What a person must still do. Everything else in this repository is finished, gated and recorded; the items below are
the ones a session cannot do, plus — stated plainly in §7 — the content work of the owner's final pass of
4 October 2026 that this window did **not** finish.

Written during the owner's final content pass of 4 October 2026 and updated on 9 October 2026, after pull request #11
was merged into `main` (`df5e2026`) and pull request #12 landed on top of it. Section 7 is the important part: it says
what that pass did **not** finish.

---

## 1. Hosting configuration

Nothing in the repository is blocked on code here; it is all account-level configuration the runbook already
specifies. Follow [`docs/RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) and [`docs/DEPLOYMENT.md`](DEPLOYMENT.md).

| # | What | Where it is read |
|---|---|---|
| 1.1 | A DigitalOcean account and an App Platform app | `docs/RELEASE_RUNBOOK.md` steps 1–14 |
| 1.2 | A container registry and a registry token | `site-src/hosting/digitalocean/` |
| 1.3 | The repository variables and secrets the deploy workflow reads | `.github/workflows/` |
| 1.4 | The corporate proxy forwarding rule | `scripts/tests/test_corporate_proxy.py` proves it once the route exists |
| 1.5 | The public origin, which is `null` until the owner sets it | `site-src/deployment.json`; the sitemap derives from it |

## 2. Counsel formalities

Both are formalities that do not block any work in the repository, and both are already applied as decisions.

- **CC BY 4.0** for CauseWay's own content. The owner adopted it on 3 October 2026 and every CauseWay-content
  download and export stays switched off until counsel confirms the licence text.
- **The World Bank Microdata Research License** on the Global Findex respondent file. The owner's decision of
  4 October 2026 — publish aggregate statistics only, cite the dataset, never commit or publish the raw file — is
  applied throughout and recorded in the Master (`28_METHODS_RIGHTS`) and in `SRC-WB-FINDEX-001`. The respondent file
  is not in this repository, in `dist/` or on the site. Counsel's confirmation of the licence text is the only thing
  outstanding. The required citation is already carried on the source record: Demirgüç-Kunt, Klapper, Singer & Ansar
  (2022), *The Global Findex Database 2021*, World Bank.

## 3. Sources that need a person with a browser

Each was requested from this session on 4 October 2026 and could not be read. None is published, and nothing on the
site depends on reading them; they would each **add** something.

| Source | What blocked it | What a person should do |
|---|---|---|
| SDRPY deposit notice | `sdrpy.gov.sa` failed TLS on every attempt; the Saudi Press Agency item that reports the deposit opens but renders its body in JavaScript, so only its headline could be read | Open `https://spa.gov.sa/en/N2234277` in a browser and read the deposit's amount, date and recipient. **Three things must not be merged:** a $300m deposit *in the Central Bank of Yemen*, $200m of budget-deficit support, and a $1.2bn pledge. A later SPA item (`N2525739`, 1 March 2026, SAR 1.3bn) goes to the **Ministry of Finance**, not the central bank |
| CBY Sana'a Circular No. 14 of 2024 | No public locator of its own could be found anywhere | The record now points at the document that reproduces it (UN doc S/2024/731, printed p. 114, Fig. 28.2). If the circular's own locator is found, replace it. **`cbyemen.com` must never be cited:** that domain has been repurposed and serves an unrelated commercial site |
| OECD, *Advancing the Digital Financial Inclusion of Youth* | Cloudflare challenge on oecd.org, OECD iLibrary and the DOI | Open in a browser and read the printed publication date |
| World Bank FASTT fast-payment-systems paper | Cloudflare challenge; the Open Knowledge Repository serves a JavaScript-only shell | Open in a browser. **Do not substitute** the similarly titled *Implementation Considerations for Fast Payment Systems* — it is a different document |
| UNDP Yemen FMIIP project page | 403 bot block on the English and Arabic URLs | Open in a browser |
| CBY-Aden Quarterly Bulletin, June 2021 | The link on CBY's own index points off-site to a CDN with a TLS hostname mismatch — broken at source | Ask CBY-Aden, or cite another issue |

## 4. A phone check of the live site from Yemen

Once the site is live: open it on a phone on a Yemeni network, in Arabic, and read it. The gates assert what the
markup says and the viewport checks run at 390 px, but neither is a phone on a real network in the country the
product is about.

## 5. OpenAI's independent acceptance review

The external gate. Not this session's to perform.

## 6. Optional and future — not required for release

- Rolling the home-page presentation pilot out to other pages. **The pilot itself was not built** (see §7).
- Next-edition firm-finance research (firm finance beyond 2022).
- A dedicated evidence record for the 2022 saving, borrowing and digital-payment measures. They are published now, on
  `CLM-026`, which is the record whose sources give them; a record of their own, with subgroup breakdowns, is a
  next-edition build.
- Findings this pass opened and deliberately did not act on, each recorded in
  [`audit/final_content/FINAL_CONTENT_LOG.md`](../audit/final_content/FINAL_CONTENT_LOG.md):
  **FC-A-02** — the World Bank's own published indicator `fin29` ("Received domestic remittances: into an account")
  prints **0.000000** for Yemen 2022 while the respondent file records 39 respondents answering yes (2.3% of adults
  weighted). A printed zero in the publisher's series is not a measured zero, so no remittance-channel share is
  published from this wave. Worth raising with the World Bank.
  **FC-A-04** — the World Bank's printed 2014 country page gives 65.9% for borrowing where its current database gives
  66.0%. Both are the publisher's; they disagree. No difference across the two vintages is computed anywhere.
- `design/07_INTERACTION_ACCESSIBILITY.md` line 87 names `?records=CLM-001` as the `compare_wrong_count` hard state.
  That example is superseded by FC-4, which makes a single record the Compare entry pre-selection. The design package
  is a closed record and was not rewritten; the live hard-state inventory and the browser tests carry the correct
  example.

---

## 7. NOT DONE in the owner's final pass of 4 October 2026 — read this before planning the next window

The owner's message asked one window to take the product to CONTENT COMPLETE. **It did not get there, and this
handover does not pretend otherwise.** Batches A and B landed and are merged; batches C, D and E were not started.

Two sessions worked that pass concurrently and did batch B independently of each other, reaching the same conclusion
on two of its three defects and **opposite conclusions on the third** — see the chronology note at the end of this
section. Where they overlapped, the merged `main` carries the other session's version; this handover does not relitigate
that.

**Landed (pull request #11, every gate green):**

- **A — the data.** Findex margins of error derived from the owner's microdata and reconciled exactly against the
  publisher's own unrounded values (FC-1, FC-1b); two broken source locators fixed and the CBY monetary series' own
  2021–22 issues recorded (FC-2); a false "no weighted value later than 2014 exists" claim removed from five records
  and one page section, with the 2022 saving, borrowing and digital-payment values published (FC-3, FC-3b).
- **B — the tools.** Three defects found and fixed: the Compare entry button, which answered the product's own
  "Compare evidence" link with a malformed-link error on all 13 comparable records in both languages; the chronology,
  23 public events with no search record at all; and the `/data/` "used on" filter, the only one of four offering no
  option for the 44 sources no domain answer uses (FC-4).

**Not done:**

| Batch | What the owner asked for | State |
|---|---|---|
| **C** | Three items needing steward contracts: IMF Financial Soundness Indicators on a `/finance/` home through a new navigation route; the public contradiction register (the 15 pairs in `audit/edition_2/CONTRADICTION_REGISTER.md`) on a `/methodology/` tier; the reusable "why the numbers differ" block as its own presentation tier | **NOT BUILT.** The research is done and is the expensive half — see below |
| **D** | Correct the stale README status, checkpoint and project context; make the validator enforce their agreement; fix the stale expected counts by formula | **PARTLY DONE by the other session** (`cf1b28d4`, `b5f28251`: the records now say #9 and #10 are merged and #11 is the open content pass). **Re-check against the map below before assuming it is closed** — in particular the `_R86_STATES` allow-list and the stale expected counts, which are a Master change |
| **E** | The home-page presentation pilot | **NOT STARTED** |

### C — what is already in hand, so the next window does not redo it

The IMF source work is **complete and verified**, and it was the hard part. IMF **Country Report No. 26/80**,
*Republic of Yemen: 2025 Article IV Consultation*, April 2026, free-public on the IMF eLibrary
(`https://www.elibrary.imf.org/view/journals/002/2026/080/002.2026.issue-080-en.xml`). **Table 5, "Yemen: Financial
Soundness Indicators, 2014–2025", printed page 31.** Transcribed cell by cell against glyph coordinates:

- **Nonperforming loans to total gross loans** — Dec-14 … Dec-19 all print `0.0`; Dec-20 58.5, Dec-21 60.8,
  Dec-22 60.2, Dec-23 60.5, Dec-24 55.3, **Aug-25** 60.0.
- **Capital to assets (leverage ratio)** — Dec-14 7.7, 8.3, 8.0, 9.1, 5.5, 4.1, 4.0, 4.3, 4.9, 3.2, Dec-24 3.3,
  **Aug-25** 3.8.

**The owner's warning is confirmed, with three independent proofs, and it is the whole point of the item.** Those
`0.0`s are **not zeros**: (a) the same table leaves `Credit growth to private sector` at Dec-19 genuinely *blank*, so
the compilers were willing to blank a cell; (b) at Dec-18 and Dec-19 the table prints NPL-net-of-provisions-to-capital
of **−111.6** and **−144.0** beside an NPL ratio of 0.0 and provisions-to-NPL of 0.0, which is arithmetically
impossible; (c) `Loan concentration` prints 0.0 for Dec-18–19 while loans demonstrably exist. Every zero in the table
falls in Dec-14…Dec-19 and every cell from Dec-20 on is real. **So the only publishable NPL series is Dec-20 → Dec-24
plus an Aug-25 part-year observation; 2014–2019 must be published as missing, never as zero.** Capital to assets is
publishable for the whole span.

Four more things that must survive into whatever is built:

1. **No unit is printed.** Table 5 carries no "(percent)" anywhere, unlike Table 4 on the same page. Do not assert a
   unit as the source's word.
2. **No footnote of any kind.** The only line under the table is "Source: Yemeni Authorities; IMF Staff Calculations".
3. **2025 is Aug-25, not a year end**, despite the table title saying 2014–2025. Label it Aug-25.
4. **Coverage is not stated.** The report never says which banks the FSIs cover. The only defensible statements: the
   figures come from the Yemeni authorities with IMF staff calculations; CBY began FSI reporting in 2025; coverage
   excludes non-bank financial institutions; unregulated money exchangers sit outside the measured sector; and the
   compiled FSIs are not yet aligned to the 2019 FSI Guide. Also note the report's own ¶13 cites **April 2025** values
   (capital/assets "2½", liquid assets 69) that **contradict** Table 5's Aug-25 column (3.8 and 73.6) — publish the
   table value with its Aug-25 label, not the narrative figure.
5. **The IMF FSI database holds no Yemen data at all.** `availableconstraint` on `IMF.STA,FSIC` returns 157 country
   codes and YEM is not among them (Jordan is, as a control). The staff report is the only IMF source; there is
   nothing to cross-check against, and the brief's "or the IMF FSI database" half does not exist.

### D — what the next window should do first, fully mapped

The status surfaces are stale and self-contradictory, exactly as the owner's message said. The mechanism is
**gate R86-G01**, `scripts/validate.py` ~2516–2540: `_R86_STATES` admits only two tokens, and the gate then asserts
the chosen one appears in six places. **Nothing can move until that allow-list gains the new status**, after which all
six change in the same commit:

1. `scripts/validate.py` `_R86_STATES` (keep the `PUBLIC RELEASE READY` refusal and the `WAITING FOR THE DESIGN
   PACKAGE` literal check).
2. `authority/YFI_CURRENT_PROJECT_CONTEXT.json` — `handoff_readiness`, `design_prompt_status`, `production_runtime`,
   `release_candidate`, `as_of`. This is the gate's input; `scripts/rebind_authority.py` propagates it.
3. `README.md` — the whole "Status at a glance" block, the role row, the Design-programme present-state block, and the
   branch paragraph (**ten** remote branches are merged into `origin/main`, not six).
4. `OPENAI_REENTRY_CHECKPOINT.md` — the position block, the status line, its date, and the stale measurements
   (public-literal audit 12,760 → **14,563**; unit tests 21 → **22**; the `RC-*` and `E2-*` gate families missing from
   its gate list).
5. `handoff/README_FIRST.md` line 1, and line 17's description of `dist/` (no longer the plain pre-design baseline).
6. `handoff/IMPLEMENTATION_MANIFEST.json` and `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` line 1; `AGENTS.md` rules 6–7;
   `CONTRIBUTING.md` lines 32 and 181.

**Stale counts, verified against the Master.** In `37_READINESS_CHECKLIST` and in `00_MASTER`: site pages **143 → 142**,
bilingual page sections **574 → 573**, evidence objects **110 → 109**. Correct the owner's brief on one point: the
**60** for public claims is right and needs no change. All are internal (sheet 37 is unprojected; the `00_MASTER`
count table is not rendered publicly), and all must be fixed Master-first through a transaction — some cells carry
formula caches, so follow the `set_formula_cache` precedent in `audit/release_candidate/rc_17_addendum2.py` ~425–446.
`site-src/content/content/master_principles.json` then regenerates; never hand-edit it. Also append dated corrections
to `FINAL_OPEN_ITEMS_REGISTER.md` line 42 (EAD-07: 151/142 → **156/147**) and line 91 (REL-02: 160 → **165**), per
that file's own append-only rule.

**No stale count reaches a public page.** Every public figure resolves from `public_inventory.json`, and `dist/` holds
no unresolved token.

### A gotcha that cost this window a CI cycle

`scripts/social_images.py --check` compares each image against the **governed text** of its route. Any Master
transaction that changes a record's governed copy makes that route's two images stale, and the Governance-gates job
fails on it. Run `python3 scripts/social_images.py` and commit the PNGs **after the last** Master transaction of a
batch, not before.

### The chronology in search — settled, and not open

**Settled on 10 October 2026: the events stay out of search.** The owner closed pull request #13, which carried the
opposite implementation, without merging it. The decision recorded in commit `cf1b28d4` — *"The 24 chronology events
stay out of search: no event route and no eligibility field"* — therefore stands, and nothing here is waiting on a
decision. The two readings are kept below so that nobody reopens the question without seeing what was weighed, and so
that the argument for indexing is on the record rather than lost with the closed branch.

**For leaving them out:** the Master gives a chronology event no route of its own and no eligibility field, so
indexing one means inventing both. That is a real publication-boundary argument.

**For indexing them:** 23 public events each render on `/finance/` **and** `/data/` with their own anchor, governed
fact, relevance and boundary, and none is findable. A reader who searches **"banknotes"**, a word printed on
`/en/finance/`, gets the governed empty state. The "no route of its own" objection is weaker than it looks, because
the **measurement priorities are already indexed exactly this way**, on an anchor fragment (`/measurement/#MA-0xx`).
An implementation that adds no authored text is possible and was built: the record is named by controlled wording plus
the event's **governed period**, exactly as the page labels it, and its summary is the governed fact verbatim; it needs
one governed interface label (`UI-JS-TYPE-CHRONOLOGY`) so the result-type filter offers an option for the new type.

That implementation is preserved on branch `code/final-content-chronology-and-gates` (its Master transaction would
need replaying on the then-current `main`, per `CONTRIBUTING.md` §3), and it is **not** to be revived without a fresh
owner decision. **Nothing depends on the outcome** — the rest of this pass stands either way. What a future window
should take from this is the narrower, undisputed point: a reader searching a word that a public page prints gets the
governed empty state, and whether that is acceptable is a question about the chronology's publication boundary, not a
defect in search.
