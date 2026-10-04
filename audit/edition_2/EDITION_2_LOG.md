# Edition 2 — the value lane

- **Opened:** 4 October 2026, on branch `code/edition-2` from `main` at `811fa6c` (the merge of PR #9, containing the
  release candidate `cd7817b`). Master before the lane: `90014e3bd271`.
- **Brief:** the owner's message to a fresh Claude Code window of 4 October 2026 ("YFIE — EDITION 2: THE VALUE LANE"),
  with the next-edition strategic brief of 3 October 2026 as context. The release lane (counsel, corrections responder,
  the five browser-read values, hosting, phone check, acceptance, tag) belongs to the owner and is not touched here.
- **Test for every change:** what can a reader (a citizen on a phone in Arabic, a journalist, a supervisor, a
  researcher) do afterwards that they could not do before? No one-sentence answer, no build.
- **Nothing here declares DESIGN HANDOFF READY or PUBLIC RELEASE READY.**

## Ranking (first reply, 4 October 2026)

0. The payment-rails wording (owner's first transaction): a known truth defect.
1. b — Findex display precision and uncertainty: two decimals from about 1,000 interviews overstate precision on every
   Findex figure; no new number.
2. c — same-source international context: the World Bank API is reachable from the session and holds the same
   indicator and wave, so this is verification, not an owner input.
3. d — "why are these numbers different?" across the site: the largest reader gain, from governed fields only, but the
   widest surface.
4. a — firm finance beyond 2022: new numbers and entity statements; the OECD page refuses automated reading.
5. f — phone length: judged after a–d settle what the pages say; risk of hiding limits.
6. e — the three Findex waves drawn: already printed as text on /people/ and the record; a new visual contract buys the
   least understanding per unit of cost.

## Decisions, one line each

- **E2-1, E2-1b (payment rails).** Read the ISR sequence 2 PDF (documents1.worldbank.org, 8 pages). The reviewer's
  wording was half right: "no later state" is false, because the same report records a later procurement state, so the
  text keeps "no later operational state". Reviewer F1–F6 folded in as E2-1b; F1's dated wording would break RC-A1, so
  the text alternative says "measured the day before it became effective" instead.
- **b, E2-2 / E2-2b (Findex precision) — BUILT.** Rule: one decimal, from the World Bank's unrounded values, gaps
  as differences of printed shares. Why not whole points: it breaks the match with the World Bank's own Yemen table a
  reader verifies against, and prints 2014's 0.4% and 0.0% as "0%", which reads as nobody (missing ≠ zero). Why not
  two: no source and no sample supports it. Intervals: not computable here (no published margin of error for Yemen's
  2022 survey: the 2021 report predates its fieldwork and the 2025 methodology table covers the 2024 surveys; the
  microdata needs a login). Reviewer findings 1–3 folded in as E2-2b. Reader gain: a reader no longer meets a
  precision the survey does not have, and can match every figure to the World Bank's table.
- **b, follow-on — RECORDED.** The same false precision exists outside Findex: the firm survey (91.84%, 68.71%,
  23.13%, 69.12% … on /firms/ and its records) and CLM-051 (57.03%, 29.97%, 2.41%). Remittance prices (two decimals,
  as Remittance Prices Worldwide publishes them) and POS growth (exact arithmetic on counts) are not the same problem.
  Not folded into b: a different source with its own published precision to be read first, and "91.84%" is in a
  Reading's governed title. See the closing list for its disposition.
- **c — finding before building.** The World Bank's Findex 2021-wave aggregates (Global Findex Database 2025 file,
  rows "Low income" and "Middle East & North Africa (excluding high income)", year 2021) are adult-population-weighted
  means that include Yemen's 2022 observation: reproduced exactly here (Low income 35.182% over 19 economies with
  Yemen; MENA excluding high income 45.413% over 10 economies with Yemen, on the FY24 regions, without Afghanistan and
  Pakistan). This corrects the first reply's challenge: the regional series does not include Afghanistan and
  Pakistan, although the World Bank's indicator API now labels it with the new region name. The Little Data Book
  (p. 159) already printed Yemen beside its region and income group: the World Bank's own presentation.
- **c, E2-3 / E2-3b (same-source context) — BUILT.** One row: the World Bank's low-income aggregate for the same wave,
  35.2% (19 economies surveyed in the wave, Yemen included). Income group over region: one row only, and the regional
  mean is dominated by two large economies far from Yemen's conditions. Kept off Home and out of drawings (a lone pair
  reads as a ranking); gate E2-CTX. Reader gain: a journalist or citizen can place 11.9% in the World Bank's own
  context for economies at similar income, without a ranking, and see that Yemen is inside that average.
- **d, E2-4 / E2-4b ("why the numbers differ") — BUILT for three pairs.** Found by sweeping every number on the
  eight domain pages. Reader gain: a journalist meeting 2.1 million subscribers and 375,252 active accounts, or two
  roster totals a year apart, reads in the same paragraph why they differ and what story would be wrong. Lesson from the
  review, now a gate: a record names its counterpart, never quotes its number, or the source trace lies. Next form
  (not built): a typed difference relation (revision, non-comparability, method break, universe or denominator,
  unresolved conflict) as its own block; it needs a new presentation tier, i.e. the steward's contract.
- **Full negative-control suite, 4 October 2026 (before d): 89 of 89 caught locally.**
- **b follow-on, firm survey — DECIDED, not changed.** The firm-survey decimals (91.84%, 68.71%, 69.12% …) are the
  World Bank FSD 2024 report's printed table values; the Findex case differed because the World Bank's database is
  unrounded and its own Yemen table prints one decimal. Printing a source's published value as printed keeps it
  verifiable; the small bases are already stated on each record.
- **a, E2-5 / E2-5b (firm finance beyond 2022; correspondent banking) — BUILT in part.** Route to the OECD text: the
  full-report PDF (oecd.org/content/dam/…/81ed2898-en.pdf) answers where the HTML refuses. YLG volumes bound into CLM-059
  with the firewall in the record and on /firms/; the OECD's correspondent-banking sentence into QUAL-001. Reader gain: an
  MSME owner or journalist sees what the guarantee programme has backed since 2017 and, in the same place, why that is
  not a measure of firms' access to credit; a /finance/ reader sees the OECD's account of why Yemeni banks are cut off
  from correspondents, labelled as an assessment. The search snippet of the OECD page quoted other YLG-adjacent figures
  (150 firms, 47,928 jobs): in the original these are SMEPS figures, not YLG's, which shows why a snippet is never a
  reading. Not built: the IMF CR 26/80 statements (original unreadable here) and the World Bank FSD 2024 Box 5 sentence
  (read and matching; it belongs in a record of its own source, which would be a new route or a widened firm-survey
  record; recorded for the next pass). A dedicated guarantee record (its own route) needs the steward's navigation
  contract.
