# Final content pass — log

The owner's message of 4 October 2026, about 18:40 Aden, designated this window the programme steward and asked for one
pass to CONTENT COMPLETE — CLAUDE MATURATION HAND-BACK READY: the data finished, every tool reflecting the whole
governed corpus, the three items that needed steward contracts built, the records agreeing, and a home-page
presentation pilot, isolated. The brief is summarised here; the transaction scripts, Master ledgers and run reports of
the FC-* transactions live beside it in this folder.

Entry state: `main` at `ab21a6f1` (merge of pull request #10, edition 2), Master
`f3e06fb935d0181211cc73f648eff588388ddda41a4c8f7eb2406b8396333514`, Page Specs
`016ca988b57f63419c4685d0b8b2eb31be7984a0554ae5318796f9e64481b12e`; both verified against
`scripts/checksums.py --check` and `scripts/validate.py` before the first change.

## Batch A — the data

### FC-1 · margins of error for every published Global Findex figure (finding FC-1:A1-MOE)

Edition 2 (E2-2) recorded that no interval could be computed for Yemen's 2021-wave Findex figures, because the
respondent file needed a login, and left the public text saying the sampling uncertainty "is not quantified here". The
owner supplied the file with this message, under the World Bank Microdata Research License, with the decision to
publish aggregate statistics only. The file is `micro_yem.dta` (study `YEM_2022_FINDEX_v01_M`, 334,544 bytes, zip
SHA-256 `bcce6d1347fb1f2e89f5c43ea24253c1151974097656835823771bcd6b2dcf99`, which matches the advisor's record). It is
not in this repository, `dist/` or the site, and never will be.

**Method.** Weighted point estimate by the Hájek ratio estimator, `p = Σ(wᵢyᵢ)/Σwᵢ` on the survey weight `wgt`;
design-based variance by Taylor linearisation, `SE = √(Σ wᵢ²(yᵢ−p)²)/Σwᵢ`; interval `p ± 1.959963985·SE`. The weight
CV is 0.9023, so unequal weighting alone inflates variance by about 1.81 (Kish). **Limit stated publicly:** the
public-use file carries the weight but no PSU or stratum identifier, so clustering is not captured and the true
interval may be wider, never narrower.

**Reconciliation against the published source, required before publishing.** Every published World Bank value for
Yemen reproduces from the respondent file to the unrounded value the World Bank itself publishes
(`api.worldbank.org/v2/country/YEM/indicator/<id>?source=28`, read 4 October 2026):

| indicator | World Bank published, unrounded | this derivation |
|---|---|---|
| `account.t.d` | 11.9033656433415 | 11.9033656 |
| women / men | 0.0543631 / 0.1834518 | 0.0543631 / 0.1834518 |
| poorest 40% / richest 60% | 0.0650494 / 0.1549671 | 0.0650494 / 0.1549671 |
| primary or less / secondary or more | 0.0698166 / 0.1952705 | 0.0698166 / 0.1952705 |
| ages 15-24 / ages 25+ | 0.0500996 / 0.1610805 | 0.0500996 / 0.1610805 |
| `save.any.t.d` | 21.6445272422787 | 21.6445272 |
| `borrow.any.t.d` | 51.2811034475895 | 51.2811034 |
| `g20.any` | 9.33455931917802 | 9.3345593 |

**There is no difference to record.** Two method details were settled by that reconciliation, because each changes the
base a margin of error is computed on, and both are recorded in the transaction script:

1. The World Bank's "ages 25+" group is the **complement of ages 15-24** (n = 770): it carries the one respondent whose
   age is not recorded. Taking `age ≥ 25` instead (n = 769) gives 0.1612575, which does not match the published value.
   The published base is used.
2. The `female` variable is coded **1 = female, 2 = male**. The file's own value labels say so, and the resulting
   5.4% / 18.3% match the published female and male anchors exactly. The owner's hold on by-sex figures is released on
   two independent confirmations, not one. (The attached archive contains no codebook; the Stata file's embedded value
   labels are the codebook of record for a public-use file, and the published anchors confirm them independently.)

**Design effect, stated honestly.** Across the fourteen individual estimates the design effect runs from **0.82 to
1.82**. For most of them a simple binomial standard error understates the uncertainty, but for two small domains — the
poorest 40% (0.93) and ages 15-24 (0.82) — it slightly overstates it. The record states the range rather than claiming
one direction.

**What was published.** The interval of every figure the site already prints: account ownership for all adults and for
each of the eight published groups, and each of the four measured differences; plus the interval of the three other
published 2022 indicators of the same wave (saving, borrowing, digital payments) and of financial-institution account
ownership. Seventeen rows `CW-FINDEX-MOE-2022-001` … `-017` in `25_FINDEX_BASELINE`, each with its point estimate,
interval, base, design effect and method. Edition 2's "uncertainty that is not quantified here" is replaced in
`CLM-002` and `VIS-FINDEX-GAPS` in both languages; `/methodology/` section 7 states the method; `28_METHODS_RIGHTS`
records the custody rule (`respondent_microdata_controlled` NO → YES, aggregate statistics only, never redistributed);
`SRC-WB-FINDEX-001` carries the licence and the citation the licence requires. Gate `FC-MOE` asserts the intervals on
what a reader sees, with a negative control.

**Not published, and why.** Subgroup breakdowns of saving, borrowing and digital payments (a next-edition build, not a
margin of error); remittance-channel shares (see the finding below).

### Findings opened by the reconciliation

| # | Finding | Disposition |
|---|---|---|
| FC-A-01 | Five records and one page section said no weighted value later than 2014 exists for saving and borrowing. The World Bank publishes 2022 values for both (`save.any.t.d` 21.6%, `borrow.any.t.d` 51.3%), and this derivation reproduces them exactly. The statement was false. | Fixed Master-first in FC-2 |
| FC-A-02 | The World Bank's published indicator `fin29` ("Received domestic remittances: into an account") prints **0.000000** for Yemen 2022, while the respondent file records 39 respondents answering yes (2.3% of adults weighted, 7.1% of recipients). A printed zero in the publisher's own series is not a measured zero. | Not published; recorded here and carried to the handover. No remittance-channel share is published from this wave. |
| FC-A-03 | `fin22a` as the World Bank publishes it (1.79%) is a composite that includes mobile money; the single microdata variable of the same name gives 1.29%. A definitional difference, not a defect. | No change; recorded so the two are never equated |

### FC-2 · source locators (finding FC-2:A2-LOCATORS)

Every locator written was opened from this session on 4 October 2026 and its status, content type and byte size
observed; every document date and issue number recorded was read off the document itself.

| # | What the sweep found | Done |
|---|---|---|
| 1 | `SRC-CBY-SANAA-C14-2024` pointed at the **wrong document**: not Circular No. 14 of 2024 but the 537-page final report of the UN Panel of Experts on Yemen (UN doc S/2024/731, 11 October 2024), on a mirror. The circular is *inside* it, reproduced as an image at printed page 114, "Figure 28.2 — Circular No 14 dated 26 March 2024 issued by CBY, Sana'a", captioned "Source: Panel". | Locator moved to the UN's own address; the record states the page the circular is reproduced on, so a reader reaches a document that really contains it. No public locator for the circular itself could be opened: the Sana'a bank's own domain is unreachable from here, and **cbyemen.com has been repurposed and now serves an unrelated commercial site — it must never be cited.** |
| 2 | `SRC-CBY-SANAA-C12-2024`'s locator returns **HTTP 404** (observed twice). Not on the owner's list; the sweep found it. | Replaced with the working address on the same host (200, 3-page PDF). |
| 3 | All 686 observations of the CBY monetary series traced to **one** source record — the May 2026 issue — so a reader checking a 2021 or 2022 monthly value was sent to a document published four years later. | The series' own index page, the bank's regulations and publications pages, and the **thirteen 2021–2022 issues** now stand beside it (nineteen addresses, all opened). Issue numbers read from the documents; **May 2022 prints none, so none is claimed for it.** |
| 4 | **The brief's premise was partly out of date.** The five SFD newsletters of 2012–2020 and IGC "From cash to capital" are *already* in the Source Library — twelve SFD records (`SRC-SFD-Q1-2012-001` … `SRC-SFD-Q4-2020-001`) and `SRC-IGC-AIDDATA-REMIT-YEM-2026`. Edition 1 or 2 had closed them. | Not duplicated. The IGC record held only its landing page, so the two documents behind it (a 90-page final report and a 12-page policy brief, both opened) were added to it. |
| 5 | The two Yemen e-money and microfinance-bank papers were genuinely missing. | Added as `SRC-SANAA-CTR-EMONEY-2022` and `SRC-SANAA-CTR-MFB-2024`, with the titles, issuing bodies and dates printed on their own pages. |
| 6 | **Most CBY-Aden documents print no date of their own** — only a period or a year. | Checked one by one; no date was invented. Where a date is recorded it is printed on the document. |

**Left out, with the reason** (all carried to `docs/HANDOVER_TO_DEVELOPER.md`): the SDRPY deposit notice — sdrpy.gov.sa
could not be opened at all (TLS failure on every attempt), and the Saudi Press Agency item that reports the deposit
opens but renders its body in JavaScript, so only its headline could be read; the amount, date and recipient were not
read in the original and **nothing is published from it**. Same reason, different wall: the OECD youth paper, the World
Bank FASTT paper and the UNDP FMIIP project page each answer an automated request with a bot challenge.

### FC-3 / FC-3b · a false currentness claim removed (finding FC-A-01)

Five records and one page section said, in both languages, that no weighted value later than 2014 existed for saving,
borrowing and domestic remittances, and `/people/` headed the section "Saving and borrowing tell a different — older —
story". **That was false**, and the FC-1 reconciliation exposed it: the World Bank publishes 2022 values in the very
series this resource cites, and the respondent file reproduces each exactly.

`CLM-026` was the record that said these estimates were unpublished, and named three preconditions: authorized
respondent-level data, the correct survey weights, and successful reproduction of the official benchmark values.
**All three are now met**, so that record carries the three published values with their derived intervals and keeps the
other 29 measures of its panel explicitly pending. `/people/` leads with them and keeps the 2014 source-and-method
detail below, named as 2014 and explicitly not subtracted from them.

Three restraints, each deliberate:

1. **No 2014 → 2022 difference is computed.** The 2014 values were read from the Little Data Book 2015, p. 160, and the
   World Bank's current database gives 66.0% for 2014 borrowing where the printed page gives 65.9%. Subtracting a 2022
   database value from a 2014 printed-page value would manufacture a change out of a revision (finding FC-A-04).
2. **No domestic-remittance value is published for 2022.** The World Bank's current series for received domestic
   remittances carries 2022 (31.9%, reproduced exactly) but **no 2014 value at all**, while this resource's 2014 figure
   comes from the country profile. A series that does not hold the earlier year cannot establish a change against it.
3. **A digital payment is not account use.** `VIS-FINDEX-ACCESS-USE` said no digital-use value exists; a
   digital-*payment* value now does, and the record says it is a different measure, because a payment can be made or
   received without an account. The access/use ladder is unchanged.

FC-3b exists because two steps of FC-3 — the `/people/` section and the three published observation rows — were lost
when that script was restructured mid-session and did not run. FC-3's own ledger shows the gap. Nothing in FC-3 was
undone.

| # | Finding | Disposition |
|---|---|---|
| FC-A-04 | The World Bank's 2014 value for borrowing any money is 65.982360 in its current database (66.0 at one decimal) but 65.9 on its own printed 2014 country page. Both are the publisher's; they disagree. | Each record keeps the value from the source it was read in, and no difference between the two vintages is computed. Recorded, not repaired. |


## Batch B — tools

B1 and B2 landed on `code/final-content` after Batch A. B1 gives the Used on filter the Not recorded option its sibling filters already had, so the 44 sources with no domain use are reachable. B2 loads a single valid Compare entry into the first slot; a verdict still needs two records.

### B3 · chronology in search

Decision: the 24 chronology events do not become standalone search results.

They have no event route, no publication or search-eligibility field, and `linked_routes` are domain pages, not event destinations. Search admits evidence, measurement and source records only. A chronology hit would need a new result type and a destination this pass does not have. The events stay in `system_chronology.json` and on the pages that already cite them. No search template, index or route was added.

## Batch C — the three steward-contract items

C1, C2 and C3 are the three items Edition 2 recorded as needing a steward contract. None is built in this pass. Each needs a new surface, and this pass does not open one.

| Item | What it is | Why it stays unbuilt |
|---|---|---|
| C1 | A typed difference block (revision, non-comparability, method break, universe, unresolved conflict) | Needs a new presentation tier and a Master relation table. The E2-4 paragraphs remain the public form. |
| C2 | A dedicated guarantee record | Needs a navigation-contract route. CLM-059 remains the public home of the volumes. |
| C3 | A public contradiction register | Needs a methodology tier. The register stays in `audit/edition_2/CONTRADICTION_REGISTER.md`. |

## Batch D — records agree

Programme records that still named pull request #9 as the current release candidate are corrected to the merged history: #9 and #10 are on `main`; the open content pass is pull request #11. This does not declare the content pass complete, and it does not declare public release readiness. The home-page pilot is not in this commit.

## Close of the non-design v1 pass

Owner decisions, not reopened: B1 and B2 complete; B3 closed, chronology is not a Search family; C1, C2 and C3 deferred to post-v1. They are not release blockers. The non-design v1 product is complete. Public release is not declared. The current phase is design / presentation integration.
