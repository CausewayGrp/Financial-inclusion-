# CLOSE-6D domain challenger lens (11 October 2026) — report as delivered

Read-only review of the staged CLOSE-6D texts against the v5 instruction (§4, §8) and the reads V1–V4 and V6. Hats:
survey statistician and analytical-product red team (6B-1, 6B-5); MSME finance specialist (6B-2); central-bank
regulator / legal librarian (6B-3); balance-of-payments statistician (6B-4). Disposition: DISPOSITION_6D.md.

## BLOCKER

- **B1** CWR-012 thesis: the closing counterweight ("Other routes and humanitarian cash fit the same numbers, and survey
  coverage, currency and the meaning of 'remittance' limit what they show") was dropped in the same place the 62.7% bound
  was added; the thesis reads as more confident (instruction l.626). Restore it.
- **B2** The bound is printed as an exact floor for the population. It is derived from two survey estimates (11.9% carries
  about 2.8 pp; 31.9% about 4.0 pp on the same basis), and s4, s7, VIS and prohibited_inference drop "in surveyed areas"
  (V1: excluded areas hold about 23% of the population). Add that the bound is an estimate; write "in surveyed areas".
- **B3** Placement and disclaimer arrange the bound as support for the hypothesis: (i) it sits in the thesis, under
  section 1 ("strongest_reading", heading "What the two published shares establish"); (ii) inside s4 directly after the
  2014 MTO/FI shares; (iii) s2 points to "the hypothesis section below"; (iv) under the narrowed question (receipt into an
  account of one's own) the bound caps receipt into one's own FI account at no more than 37.3% of recipients, so "says
  nothing about how the money travelled" disclaims something other than what it bears on. Move the bound to s2; leave s4 a
  cross-reference; replace the disclaimer ("bears only on whether recipients could have received the money into a
  financial-institution account of their own; … neither confirms nor refutes the hypothesis").
- **B4** CLM-059 and /firms/ s7: "through 12 partner institutions" is wrong for 2022 (12 partners in total; 11 issued
  guarantees in 2022; V2).
- **B5** Test 9 (instruction l.997) may fail on surfaces outside the review set that still print "did not ask" (interface
  copy, visual library, design contracts, evidence objects, public claims). Not verified whether these are projections of
  the staged fields.

## SHOULD-FIX

- **S1** "no weighted estimate of the channel is published": the database publishes fin29 = 0. Write "usable here", and name
  the printed zero as not used.
- **S2** The two halves of 6B-5(c) are reversed in s9; s8 implies the first half alone.
- **S3** The item asks about receipt "using a bank account or a mobile money account" (V1), not "into an account".
- **S4** s1 heading over-promises; suggested "What the evidence establishes, and what remains a hypothesis".
- **S5** The two routes overlap (a provider may both pay out transfers and hold accounts).
- **S6** "includes Yemen itself" is unsupported (V1: the pages do not say whether Yemen's 2022 data are in the LIC 2021
  figure); write that Yemen is itself classed as low income.
- **S7** The gender figures (2022 "women-led" against cumulative "men-owned") cover different periods and terms; do not
  compare them.
- **S8** The Instructions' scope words are "the Central Bank" and "in the Republic of Yemen", not "CBY-Aden"; MA-006 says
  "providers" unqualified.
- **S9** Item د refers back to item ج's period; the open point is whether the extensions replace or add to each other.
- **S10** YSC-028: the search was of cby-ye.com only; Decision No. 6 of 2025 cites the law as No. 40 of 2008; "the 2025
  decision" undefined; the Art. 13(2) exclusions (government, interbank, cash collateral) are omitted.
- **S11** CLM-041 "Neither converts CBY-Aden values into IMF values for any component" is false for 1.838 on remittances in
  2021–2024 (3,422.16 / 1,861.7 = 1.838).
- **S12** CLM-007: the IMF row is not labelled IRG; its basis is implied by Annex IV and the GDP note.
- **S13** Yemen Post: the World Bank names the Yemen Post and Postal Savings Authority and the Postal Savings Fund (p.16).

## NIT

N1 s5 "households" for recipients; N2 CLM-001 method "were not asked" (kept by instruction); N3 /methodology/
"(round; …)" garbled; N4 CLM-011 escalation ground 1 incomplete; N5 USD/US$ mixed; N6 /finance/ "would in any case use
… different questions" unsupported; N7 /reforms/ never carried "9 August 2023"; N8 "tell a different story"; N9 YLG pages
9 and 31.

## CWR-012

- 6B-5(a) passes; (b) passes in question, thesis and s4 (see S3); (c) passes in thesis, meta and s3, fails in s9 and s8
  (S2); (d) passes (B5 open); (e) title and question pass, s1 heading borderline (S4). "consistent with" removed; licensing
  classes out of s4.
- Reads as more confident through B1, B2 and B3. Adults called households: only the s5 slip. The route slug
  "/readings/how-money-reaches-households/" is kept by instruction (l.682); residual.
- Arithmetic: (31.9313981068809 − 11.9033656433415) / 31.9313981068809 = 62.7220656% → "at least 62.7%" correct.
- "Into an account of their own" against fin29_1 (bank or mobile-money account, owner unspecified) and the bound (FI
  account ownership only): coherent only with the mobile-wallet caveat and S3.
- Strongest remaining misreading: "At least 62.7% of Yemenis who receive money from relatives have no account, so the money
  comes through exchange companies; the Reading proves its hypothesis."
- **VERDICT: KEEP, conditional** on B1–B3 (with S1–S3); "If B1–B3 are not fixed in CLOSE-6D, WITHDRAW."

## Departures by the Team Lead, judged

(1) Arabic of 6B-1(c) matched to the English: agree. (2) CLM-041 (1.838 is this resource's ratio; trade mainly UN Comtrade):
agree (V4). (3) "The Instructions are the binding text" dropped: agree. (4) ج and د published separately: agree (see S9).
(5) "an account type for which the World Bank publishes no Yemen value": agree; record it against test 11's literal
wording. (6) USD style: agree (N5). (7) Yemen Post "gives no count": agree (S13).

## Strongest misreading per group

Findex: 11.9 against 24.5 read as a ranking. Firms: guarantees read as firms financed; 20% women-led (2022) against 72.7%
men-owned (cumulative) read as a trend. Regulation: a consumer outside CBY-Aden's reach treats the Article 9 path as
theirs, or dates the 14-day window. Remittances: IMF projections multiplied by 1.838, or divided by 0.33.

## Not verified by this lens

SMEPS figures; the 2014 profile; roster counts; FMIIP and IGC counts; prices; CBY-Aden BoP values; Brief 40; the 141-firm
survey figures; 0.4% (LDB p.160); the rows in 25, 23, 29 and 34 (not in the review packets).
