# Stage B — the Folio visual proof (18 October 2026, owner-authorized, Decision 2)

What this folder is: one isolated, presentation-only visual treatment ("Folio") over the accepted G2 build, built the
way the G1 candidates were built (charter §10; `design/exploration/v2/`): CSS appended to a scratch copy of `dist/`,
the HTML and JavaScript byte-identical to `dist/` (the build script checks this), so every word, number, link,
boundary and citation is the shipped one and content parity, the literal audit and bilingual invariance hold by
construction. Nothing here is a second content authority, a parallel design system or a release candidate: the
shipped stylesheet is still `scripts/yfie/theme.py`, and the treatment is adopted only by an owner decision and a
Stage C transaction of its own. The decision record is `design/DESIGN_INTEGRATION_V2.md` §9; the before/after
evidence is `design/evidence/v2/proof/`.

| Variant | What it is | Fonts per edition | AR /data/ cold at 390 |
|---|---|---|---|
| D | the baseline: `dist/` as built at the G2 integration head (PR #62) | 3 | 322 KB |
| T0 | Folio on the incumbent faces (IBM Plex Sans / Plex Sans Arabic) — `folio.css` | 3 | 324 KB |
| T1 | Folio with the display faces — `folio.css` + `faces_T1.css`: Noto Naskh Arabic 700 for Arabic titles and section headings, IBM Plex Serif 600 for English; body, controls, clocks and numerals unchanged | 4 | 346 KB |
| T2 | Folio with Amiri 700 / IBM Plex Serif 600 — `faces_T2.css`; built and viewed, not taken further (classical book voice; 128 KB file) | 4 | 393 KB on Home |

The owner's three references (an Arabic-first Home with a large right-aligned headline and a bounded evidence
example; an English-led Home; a bilingual publication mockup) were read for their qualities — a dominant native
title, a parted statement, a bounded evidence register beside the thesis, brass detailing, air between sections — and
not for their elements: none of their readings, figures, illustrations, icons, cards, routes or modules appears here.

## The treatment (`folio.css`, ten numbered blocks)

1. Scale and voice: display 34/32 px on phones (EN/AR), 52/46 at 900 px and above; the statement in the secondary
   ink; the brass anchor 56 × 2 px in brass-700. 2. The register head's title column wider. 3. Square calls to action,
   the tools in the muted ink. 4. Sections: more air, darker hairlines, brass numerals, headings one step up (the
   topics label excepted). 5. The boundary band on a single firm rule. 6. Home's three figures as one bounded evidence
   register (hairline, white). 7. The record head's clocks as a ruled two-column register with brass labels. 8. One
   ink hairline under the masthead, brass for the current hub, a brass top rule on the rail. 9. The long reading one
   step larger with more air between sections. 10. Home at 1200 px and above as an asymmetric spread: the thesis, the
   topics, the boundary and the starting questions on the start side, the bounded evidence register beside them; the
   markup order (figures first) is the reading order; the phone keeps its single column; the rail stays.

## Fonts: provenance, licence, subsetting

| File | Source | Licence | Bytes |
|---|---|---|---|
| `fonts/NotoNaskhArabic-Bold-subset.woff2` | google/fonts `ofl/notonaskharabic` (the G1 specimen file, `design/evidence/v2/g1/README.md`), subset with fontTools 4.x: U+0020–007E, U+00A0–00FF, Arabic letters U+0620–064A, marks U+064B–0652, digits U+0660–0669, U+066A–066D, U+0670–0671, U+06D4, punctuation U+2010–2015, U+2018–201D, U+2026, U+2030, U+2212; every layout feature kept | OFL 1.1 | 23 KB (57 KB whole) |
| `IBMPlexSerif-SemiBold-Latin1.woff2` (from the G1 folder, not copied here) | IBM/plex `@ibm/plex-serif@1.1.0`, IBM's own Latin-1 split | OFL 1.1 | 24 KB |
| `Amiri-Bold.woff2` (T2 only, from the G1 folder, not copied here) | google/fonts `ofl/amiri` 1.002 | OFL 1.1 | 128 KB |

The subset's glyph coverage was verified on the rendered Arabic titles and section headings of every proof view
(ligatures, diacritics, the Latin inside Arabic titles); a glyph the subset lacks falls back to IBM Plex Sans Arabic by
the `font-family` list and would show as a weight change, which none of the views shows. Before adoption the subset
would be rebuilt from the current upstream release and recorded in `design/08_ASSET_MAP.md` with the other fonts.

## Regenerate and measure

```bash
python design/exploration/v3/build_proof.py <scratch outside the repository> D T0 T1 T2
```

The script copies `dist/`, appends the deltas, copies the fonts, serves each copy gzip as `_headers` declares, and
for every variant renders the same six routes in both editions at 390 × 844 and 1440 × 900 (first screen; Home and the
record also full-page), measuring screens, title lines, the first-answer and first-boundary positions, hidden governed
text, horizontal overflow and cold bytes at 390. It needs the G1 font folder (`--fonts` path inside the script) and the
repository's Python 3.11 environment with Chromium.
