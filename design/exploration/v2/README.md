# Stage B G1 — the direction challenge (18 October 2026)

What this folder is: the G1 candidates of charter §10 and the owner directive of 17 October 2026 (§9, "G1"), each
a token-and-CSS delta over the shipped stylesheet (`scripts/yfie/theme.py`), built outside it as the charter
requires, and the script that regenerates and measures them. The decision is DL-V2-001 in
`design/DESIGN_INTEGRATION_V2.md` §4; the committed evidence (rendered views, measurements, the blind judges'
scores, the specimen) is `design/evidence/v2/g1/`. Nothing here is a second content authority or a parallel design
system; after G2 only the chosen direction exists in the shipped stylesheet. This folder is lineage and is not
deleted (charter §10.5).

| Candidate | Led by | Delta | Hierarchy and reading order |
|---|---|---|---|
| A · Register | the data professional | `cand_A.css` | quiet official-statistical: Plex only, the type scale one notch down, a two-column register head on wide screens (title · statement and actions), text-link page tools, a lighter narrower rail, rules instead of fills; the topics block one compact line |
| B · Argument | the sceptical statistician-journalist | `cand_B.css` | editorial-evidence: the one heading pairing of Part 6 item 21 — Markazi Text 600 (Arabic) and IBM Plex Serif 600 (English) over the unchanged text faces — a ruled masthead, a serif deck, record units as hairline margin units, the boundary as a ruled note; phone order: title, figures, index, boundary, questions, topics |
| C · Compact | the citizen on a phone | `cand_C.css` | compact source-first: Plex at 600, the smallest chrome, a compact scale, record units as rows with the clock inline, the index as an inline list, no rail on a wide screen; phone order: title, figures, boundary, topics, questions |
| D · Incumbent | — | none | the shipped T4 · Instrument presentation on main `8c78fa0e` |
| E · Argument, compact | the hybrid the directive allows when it is materially different | `cand_E.css` | B's identity (the pairing, the ruled masthead, the margin units, no fills) with C's phone economy (chrome, inline index, record rows) and C's phone order; the rail stays on a wide screen |

Regenerate and measure (Python 3.11 with the repository's requirements and Chromium; a scratch folder outside the
repository; the candidate fonts for B and E in a folder of WOFF2 files, see `design/evidence/v2/g1/README.md` for
their provenance):

```bash
python3 design/exploration/v2/build_candidates.py --scratch /tmp/g1 --fonts /tmp/g1/fonts        # all five
python3 design/exploration/v2/build_candidates.py --scratch /tmp/g1 --fonts /tmp/g1/fonts B E    # some
```

Each candidate's HTML and JavaScript are byte-identical to `dist/` (the script checks this): the candidates
differ in presentation only, so content parity, the literal audit and bilingual invariance hold by construction,
and the disqualifiers a stylesheet can fail (a hidden governed region, horizontal overflow at 390, added
JavaScript, byte growth) are measured, not assumed.
