# Handover to a human developer

**State, 10 October 2026.** Content is complete on `main`; its checkpoint is the annotated tag
`checkpoint/2026-10-10-content-complete` (§9). Every gate passes there. **Nothing is deployed, and public release is not
declared.** What follows is every task that remains for a person; a session cannot do any of them. The handover
written on 4 October and updated on 9 October 2026 is kept unchanged at the end of this file as a record. Where it and
this section disagree, this section is current (§8 lists what changed).

---

## 1. Hosting on DigitalOcean App Platform

The host is decided: DigitalOcean (owner decision of 3 October 2026). The site runs as an nginx service in an App
Platform app, reached through the corporate site at `https://causewaygrp.com/financial-inclusion-evidence`. Nothing in
the repository is blocked on code; everything below is account-level configuration. Follow
[`docs/RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md) and [`docs/DEPLOYMENT.md`](DEPLOYMENT.md).

| # | What | Who | Where it is read |
|---|---|---|---|
| 1.1 | A DigitalOcean account with a Container Registry; the App Platform app is created by the first deploy | Owner | runbook steps 1, 6 |
| 1.2 | A personal access token with write access to the registry and App Platform, stored as the secret `DIGITALOCEAN_ACCESS_TOKEN`; the variables `YFIE_DO_REGISTRY`, `YFIE_DEPLOY_ENABLED=true` and, after the first deploy, `YFIE_DO_APP_ID` | Owner | runbook steps 6, 7; `site-src/hosting/digitalocean/` |
| 1.3 | The corporate proxy rule that forwards `/financial-inclusion-evidence` to the app | Web administrator | `scripts/tests/test_corporate_proxy.py` proves it once the route exists |
| 1.4 | The public origin, `null` in `site-src/deployment.json` until the owner sets it | Owner, then Claude Code | runbook step 3 |
| 1.5 | The logging facts for /privacy/ (what the corporate server and App Platform keep, and for how long) | Web administrator and owner | runbook step 9a |
| 1.6 | `Strict-Transport-Security` is the domain's decision | Web administrator | runbook step 9 |

## 2. The licence text (`licence_text_confirmed`): confirmed by the owner, nothing left to do

The reuse licence is decided, and the rights question is closed permanently: CC BY 4.0 for the content CauseWay owns
(`audit/OWNER_DECISIONS_2026-10-10.md`, OWN-04-R and §4). On 10 October 2026 the owner endorsed the text with two
corrections to /rights/ (transaction RIGHTS-FINAL) and **confirmed the CC BY 4.0 text on /rights/, /terms/ and the
footer, in both languages; no counsel review is required** (runbook step 7a). `licence_text_confirmed` is `true` in
`site-src/deployment.json`. Validator RC-B14 fails if it is true without the owner's dated line, and gates PN-G01 and
PN-G02 guard the licence declaration on every page. No legal review is claimed.

/rights/ states facts only about the World Bank Microdata Research License: the three derived 95% intervals on
`CLM-026` are computed from a file CauseWay obtained under it, only aggregate estimates are published, the citation is
printed, and CC BY does not extend to the underlying microdata. The respondent file is not in this repository, in
`dist/` or on the site. Optional: the owner may ask the World Bank Microdata Library for written confirmation
(`FINAL_OPEN_ITEMS_REGISTER.md`, OWN-09); the text no longer depends on it.

## 3. Data downloads stay off (`public_downloads: false`)

The exports are built and gated (`scripts/exports.py`, `scripts/tests/test_exports.py`) but not published. Switching
`public_downloads` on (runbook step 2) is a separate owner decision; §2 no longer stands in its way. Until then the validator and the export test fail
if a download appears in `dist/`.

## 4. Sources that need a person with a browser

This session requested each of these and could not read it. None is published, and nothing on the site depends on
reading them; each would **add** something. They were recorded on 4 October 2026, and this pass did not retry them.

| Source | What blocked it | What a person should do |
|---|---|---|
| SDRPY deposit notice | `sdrpy.gov.sa` failed TLS. The Saudi Press Agency item renders its body in JavaScript | Open `https://spa.gov.sa/en/N2234277` and read the deposit's amount, date and recipient. Keep three things apart: a $300m deposit *in the Central Bank of Yemen*, $200m of budget-deficit support, and a $1.2bn pledge. SPA `N2525739` (1 March 2026, SAR 1.3bn) goes to the Ministry of Finance |
| CBY Sana'a Circular No. 14 of 2024 | No public locator of its own | The record points at UN doc S/2024/731, printed p. 114, Fig. 28.2. **Never cite `cbyemen.com`**, which now serves an unrelated site |
| OECD, *Advancing the Digital Financial Inclusion of Youth* | Cloudflare challenge | Read the printed publication date |
| World Bank FASTT fast-payment-systems paper | Cloudflare challenge; JavaScript-only repository shell | Open it in a browser. Do not substitute *Implementation Considerations for Fast Payment Systems*, which is a different document |
| UNDP Yemen FMIIP project page | 403 bot block (EN and AR) | Open it in a browser |
| CBY-Aden Quarterly Bulletin, June 2021 | CBY's own link points to a CDN with a TLS hostname mismatch | Ask CBY-Aden, or cite another issue |
| IMF press release on the proposed Staff-Monitored Program (16 July 2026) | The IMF website refuses automated requests; /finance/ says the entry was not re-read for this edition | Re-read it in a browser and confirm the dated event |

## 5. A phone check of the live site from Yemen

Once the site is live, open it on a phone on a Yemeni network, in Arabic, and read it. The gates check the markup, and
the viewport checks run at 390 px. Neither is a phone on a real network in the country the product is about.

## 6. OpenAI's independent acceptance review

This is the external gate, and it is not a session's to perform. The recipient starts at `README.md` and
`OPENAI_REENTRY_CHECKPOINT.md`.

## 7. The owner's release approval, and the release tag

These are runbook steps 13 and 14. The owner reviews the live site and the records and accepts the release. Claude Code
then sets `pre_release` to `false`, and the owner pushes the release tag. Nothing in this repository declares PUBLIC
RELEASE READY.

## 8. What changed since the handover of 9 October 2026 (below)

- **The chronology in search is decided and done.** The owner decided INDEX (`audit/OWNER_DECISIONS_2026-10-10.md`
  §3, OWN-14-R). Pull request #13 was closed without merge. The 23 dated events are indexed (CS-1), with the analytical
  rule left out. The "open disagreement" section below is history.
- **Pull requests #11 to #24 are resolved:** #13, #21 (another session's alternative naming, superseded by #19) and #23
  (an earlier draft of this handover, superseded by RIGHTS-FINAL) were closed without merge; the rest merged.
- **RIGHTS-FINAL (#24):** the CC BY 4.0 text was endorsed with two corrections and confirmed by the owner; no counsel
  review is required. The licence gates PN-G01 and PN-G02 landed with it. The status surfaces (README, the checkpoint,
  the Context) were re-dated to 10 October 2026, and their counts match the build (292 HTML documents from 144 Page
  Specs: 288 localized, root, 404, and the two retired-address pages).
- **Public naming and rights presentation** (NB-1, NB-2) were approved by the owner and merged.
- **Legacy-audit follow-through** (LA-A, LA-B, LA-C) is merged: the published FMIIP definitions are stated, four
  Readings are strengthened, and there is a new Evidence Record (CBY-BANKS-2026-05) and a new Reading (CWR-011).
- **Batch C** (IMF FSIs on /finance/, the public contradiction register, the "why the numbers differ" tier) is still
  **not built**. Its research is preserved below and stays valid. **Batch E** (the home-page presentation pilot) is
  still not started. Both are next-edition work, not release blockers.
- **The Master's internal count cells are stale** (`00_MASTER` and `37_READINESS_CHECKLIST`: site pages 143, Readings
  10, sources 165; the sheets hold 144, 11 and 167). They are not projected or public. Fix them Master-first, with the
  formula-cache precedent in `audit/release_candidate/rc_17_addendum2.py`. This is recorded in
  `FINAL_OPEN_ITEMS_REGISTER.md` §10 (OWN-10).

## 9. Repository housekeeping this session could not do

This session's git access pushes only to its own working branch. On 10 October 2026 it was refused (HTTP 403) when it
tried to delete remote branches, and an earlier session recorded the same refusal for tag pushes. A person with
write access does the following.

**Delete 16 merged branches.** Each head was checked to be an ancestor of `main` on 10 October 2026, and none is the
head or base of an open pull request. Re-check before deleting:
`git merge-base --is-ancestor origin/<branch> origin/main && echo merged`.

```
git push origin --delete claude/bold-maxwell-r3o015 claude/claude-md-multi-agent-skill claude/dreamy-archimedes-e8qx5v \
  claude/epic-cori-60fpeb claude/hopeful-mccarthy-jgip83 claude/new-session-giw687 claude/practical-cray-sr26c5 \
  claude/yfie-pr9-rc-finish-jetvaw code/base-path-hosting code/edition-2 code/final-content code/release-candidate-fixes \
  code/steward-gate-and-handover design/d0-orientation design/final-presentation-integration-v1 \
  claude/design-review-constraints-l9au89
```

**Keep these branches:**

- `main` and `safety/pr11-pre-b1b2-2026-10-04`.
- `claude/public-naming-terminology-part-b`: the head of the closed #21, with 1 unique commit (its record of the
  alternative naming, kept for reference).
- `code/final-content-chronology-and-gates`: 2 unique commits; the branch of the closed #13.
- `code/navbar-disclosures-integration`: 3 unique commits. **The owner should review it**; no session in this pass
  wrote it.
- `claude/new-session-s346lg`: this session's working branch.

**The checkpoint tag.** If `git ls-remote --tags origin` does not list `checkpoint/2026-10-10-content-complete`,
create it on the merge commit of the pull request that carries this section, which is the final `main` of 10 October
2026. Never move it once it exists.

```
git tag -a checkpoint/2026-10-10-content-complete <merge-commit> -m "Content complete, 10 October 2026"
git push origin checkpoint/2026-10-10-content-complete
```

---

# Record: the handover of 4 October 2026, updated 9 October 2026 (kept unchanged)

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

## 2. Licence formalities (updated 10 October 2026: the owner confirms; no counsel review is required)

Neither blocks any work in the repository, and both are already applied as decisions.

- **CC BY 4.0** for CauseWay's own content. The owner adopted it on 3 October 2026 and every CauseWay-content
  download and export stays switched off until the owner switches the downloads on. The owner confirmed the CC BY 4.0
  text on /rights/, /terms/ and the footer on 10 October 2026, after RIGHTS-FINAL (`audit/OWNER_DECISIONS_2026-10-10.md`
  §4); `licence_text_confirmed` is `true`. No legal review is claimed.
- **The World Bank Microdata Research License** on the Global Findex respondent file. The owner's decision of
  4 October 2026 — publish aggregate statistics only, cite the dataset, never commit or publish the raw file — is
  applied throughout and recorded in the Master (`28_METHODS_RIGHTS`) and in `SRC-WB-FINDEX-001`. The respondent file
  is not in this repository, in `dist/` or on the site. Nothing is outstanding; optionally, the owner may ask the World Bank
  Microdata Library to confirm in writing that publishing the CLM-026 aggregate intervals is consistent with the Research
  License (`FINAL_OPEN_ITEMS_REGISTER.md`; the /rights/ text no longer depends on it). The required citation is already carried on the source record: Demirgüç-Kunt, Klapper, Singer & Ansar
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

### The chronology in search — an open disagreement, for the owner

The two sessions split on this and it is still unresolved. Commit `cf1b28d4` records: *"The 24 chronology events stay
out of search: no event route and no eligibility field."* The other session implemented the opposite and it is **not**
on `main`.

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
need replaying on the then-current `main`, per `CONTRIBUTING.md` §3). **Nothing depends on the decision** — the rest of
this pass stands either way.
