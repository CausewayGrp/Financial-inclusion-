# F-15 first-click test — B1, 17 October 2026 (AI-simulated; no human testing)

**Question (takeover brief Part 6 item 14; G0-F03).** Can a first-time reader reach each of the eight domain answers in one
click from Home on a desktop, and does the grouping (flat eight or four families) matter?

**Method.** Every clickable link on the built Home page (desktop 1440 px: the phone-only menu entries removed) was listed in
reading order, grouped by region and nearest heading, with its target kept in a sidecar the judges never saw
(`firstclick_variants.py`, session scratch; the lists are reproducible from the build). Three variants per edition:

- **A** — the built page after D8 (masthead of five hubs, no topics block).
- **B** — A plus a "Topics" block under the product statement listing the eight domain answers by their governed names
  (the opened menu's labels), flat, and a footer group with the same eight links.
- **C** — as B, the block grouped in four families (people and access · payments and remittances · firms and finance ·
  providers and reforms; placeholder family names).

Six blind judges (one per variant × edition; a language model at low effort, told nothing about the variants or the
hypothesis) each played three first-time visitors — a journalist in a hurry, a World Bank analyst, a university
student — and chose the one link each visitor would click first for eight tasks, judging by link labels and headings only
(0 = would search or give up). A hit is a click whose target is the task's domain answer page.

**Tasks → target.** T1 account ownership and the gender gap → /people/ · T2 where services can be reached → /access/ ·
T3 finance as a constraint for firms → /firms/ · T4 banks and microfinance → /finance/ · T5 terminals, e-wallets, payment
systems → /payments/ · T6 cost of sending money, how remittances arrive → /remittances/ · T7 licensed banks and exchangers
→ /providers/ · T8 rules, reforms, projects → /reforms/.

## Result (one-step hits of 24 judgements per cell)

| Variant | EN desktop | AR desktop | Where the misses went |
|---|---|---|---|
| A — built page after D8 | 5 / 24 (21%) | 6 / 24 (25%) | the Explore hub, Evidence, Sources, a measurement priority, a Reading; AR: six "would search or give up" |
| B — Home topics block, flat eight | 22 / 24 (92%) | 24 / 24 (100%) | EN: two analyst clicks to measurement priorities (T1, T2) |
| C — Home topics block, four families | 23 / 24 (96%) | 23 / 24 (96%) | one click to the Reading "The system is changing…" (T8) in each edition |

Per task, variant A: T3 (firms) reached its page through the question card in all six judgements; T2, T5 and T6 reached
their page in none. Variants B and C: every task reached its page in at least two of three judgements in both editions.

## Decision (DL-V2-007)

B and C tie within one judgement. The flat eight is adopted: it needs no family names, matches the phone menu's flat
list, and keeps the eight governed names as the only labels. Home carries the block under the governed heading
UI-HOME-TOPICS (transaction STAGE-B-S2); every page's footer carries the same eight links as its first group; Home's
map lists the block first (steward edit, S10). The desktop masthead stays the five hubs of D8 — no topics entry is
needed when the block is on Home. The built page was re-listed after the change: the same 19 domain-answer links as
variant B, plus the map's entry.

**Limits.** Language models reading labels, not people; a desktop list, not a rendered page; three personas by
instruction. The before/after measure is the one the brief asked for and is reproducible from the lists; it is not a
usability study.
