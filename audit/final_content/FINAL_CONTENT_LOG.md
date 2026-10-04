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
