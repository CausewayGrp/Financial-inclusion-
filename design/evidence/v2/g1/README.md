# G1 evidence — the direction challenge, 18 October 2026

Built on main `8c78fa0e` (dist/ as committed; Master `03d194a2…`, Page Specs `cf813880…`) with
`design/exploration/v2/build_candidates.py`. The decision is DL-V2-001 (`design/DESIGN_INTEGRATION_V2.md` §4).
Nothing here is authority; the rendered views are proof for the record.

| File | What it is |
|---|---|
| `g1_scoreboard.md` | the scorecard: three blind judges × nine criteria × candidates, the measured columns, the disqualifier and source-owner results, and the second round |
| `judges.json`, `judges_round2.json` | the judges' reports as received (JSON only, as briefed) |
| `judge_mapping.json`, `judge_mapping2.json` | the random label mapping of each round, decoded after the judges reported |
| `<X>_metrics.json` | per candidate: screens, H1 lines, overflow, fonts loaded, P1 proxies at every view |
| `bytes.json` | cold transfer bytes on the wire at 390, by type, both editions, per candidate |
| `disqualifiers.json` | HTML and JS identity with dist/, hidden governed regions, first-answer and first-boundary position |
| `sourceowner.json` | charter §3.5 on the five records (CLM-001, CLM-003, CLM-032, CBY-BANKS-2026-05, VIS-MFI-2014-PANEL), both editions |
| `shots/` | first-screen renders: AR 390 (Home, CLM-001, /payments/, /data/) and EN 1440 (Home, CLM-001) per candidate |
| `specimen/` | the heading specimen (Part 6 item 21): the real governed H1s in Plex Arabic 600 and 700, Noto Naskh Arabic 600, Markazi Text 600 and 700, Amiri 700 at 390; Plex Sans 600 against Plex Serif 600 and 500 at 1440; `w_mapping.json` is the blind label map of the 600/700 crops |

## Candidate fonts: provenance and licence

Tested, not adopted until G2 vendors them: all SIL Open Font License 1.1, verified in each file's name table.

| Face | Source | Version | File used in the test |
|---|---|---|---|
| Markazi Text | google/fonts `ofl/markazitext/MarkaziText[wght].ttf` (commit `6c109f02`, 3 March 2026); project https://github.com/BornaIz/markazitext | 1.001 | static instance at wght 600, subset to the Arabic blocks plus basic Latin and punctuation with fontTools 4.67, WOFF2 (37 KB) |
| IBM Plex Serif | IBM/plex release `@ibm/plex-serif@1.1.0`, `fonts/split/woff2/IBMPlexSerif-SemiBold-Latin1.woff2` (IBM's own Latin-1 split, unchanged) | 3.001 | 24 KB |
| Noto Naskh Arabic | notofonts/arabic release `NotoNaskhArabic-v2.021` | 2.021 | specimen only; not taken into a candidate |
| Amiri | google/fonts `ofl/amiri` | 1.002 | specimen only; not taken into a candidate |

The text faces stay IBM Plex Sans and IBM Plex Sans Arabic as vendored (`vendor/fonts/`, unchanged).
