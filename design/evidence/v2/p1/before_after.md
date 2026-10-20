# OD-1018 — before (main `886a8160`) and after (`pr/presentation-canvas`), measured

Same script, routes, widths and server as G0–G3 (`design/evidence/v2/g0_measure.py`, gzip as `_headers` declares;
screens = scrollHeight ÷ viewport height). `base_metrics.json` is main before any change; `p1_metrics.json` is the final
build of this branch. Guard (owner direction §5): no family's AR 390 phone length may exceed its g2r value
(`design/evidence/v2/g0/g2r_metrics.json`) by more than 10 %. Automated measurements, not human reading time.

## Per family

| Route | AR 390 g2r | guard (×1.10) | AR 390 base | AR 390 p1 | guard | EN 390 base → p1 | EN 1440 base → p1 | AR 1440 base → p1 | first .fnum AR 390 base → p1 (px) | H1 lines AR 390 / EN 1440 p1 | AR cold bytes base → p1 | fonts p1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| / | 8.9 | 9.79 | 8.9 | 9.2 | PASS | 8.8 → 9.8 | 5.5 → 5.8 | 5.6 → 5.5 | 669 → 787 | 2 / 3 | 274539 → 293264 | 4 |
| /explore/ | 8.2 | 9.02 | 8.2 | 7.9 | PASS | 8.2 → 8.3 | 5.5 → 5.7 | 5.7 → 5.6 | — → — | 1 / 2 | 272252 → 289612 | 4 |
| /people/ | 13.4 | 14.74 | 13.4 | 12.4 | PASS | 12.9 → 13.3 | 8.6 → 8.5 | 9.1 → 8.1 | — → — | 2 / 2 | 282913 → 300283 | 4 |
| /payments/ | 19.6 | 21.56 | 19.6 | 17.6 | PASS | 19.4 → 19.2 | 13.0 → 12.8 | 13.6 → 12.4 | — → — | 2 / 2 | 285063 → 302434 | 4 |
| /remittances/ | 16.4 | 18.04 | 16.4 | 15.0 | PASS | 15.4 → 15.9 | 9.9 → 9.8 | 10.7 → 9.7 | — → — | 3 / 2 | 281918 → 299288 | 4 |
| /firms/ | 13.6 | 14.96 | 13.6 | 12.4 | PASS | 12.8 → 13.0 | 8.1 → 8.0 | 8.6 → 7.8 | — → — | 2 / 2 | 278922 → 296291 | 4 |
| /finance/ | 12.9 | 14.19 | 12.9 | 11.7 | PASS | 12.4 → 12.5 | 7.9 → 7.6 | 8.3 → 7.5 | — → — | 3 / 3 | 297791 → 315162 | 4 |
| /providers/ | 16.2 | 17.82 | 16.2 | 14.7 | PASS | 15.9 → 16.4 | 10.6 → 10.4 | 11.1 → 9.9 | — → — | 2 / 2 | 279819 → 297189 | 4 |
| /access/ | 9.5 | 10.45 | 9.5 | 8.9 | PASS | 9.4 → 9.6 | 6.1 → 5.9 | 6.2 → 5.8 | — → — | 3 / 2 | 274480 → 291851 | 4 |
| /reforms/ | 20.3 | 22.33 | 20.3 | 18.6 | PASS | 20.3 → 20.8 | 12.8 → 12.7 | 13.3 → 12.0 | — → — | 2 / 2 | 281566 → 298936 | 4 |
| /evidence/ | 13.2 | 14.52 | 13.2 | 12.0 | PASS | 13.3 → 13.3 | 9.9 → 9.4 | 9.8 → 8.5 | — → — | 2 / 2 | 286103 → 303464 | 4 |
| /evidence/CLM-001/ | 10.2 | 11.22 | 10.2 | 9.2 | PASS | 9.5 → 9.3 | 5.3 → 5.2 | 5.7 → 5.3 | 715 → 616 | 2 / 3 | 275180 → 292540 | 4 |
| /evidence/CLM-003/ | 9.9 | 10.89 | 9.9 | 9.3 | PASS | 9.9 → 9.8 | 5.4 → 5.5 | 5.7 → 5.4 | 535 → 535 | 1 / 1 | 274349 → 291710 | 4 |
| /evidence/VIS-POS-TERMINALS/ | 15.8 | 17.38 | 15.8 | 14.9 | PASS | 15.5 → 15.8 | 9.3 → 9.5 | 10.0 → 9.5 | 574 → 535 | 1 / 1 | 277595 → 294955 | 4 |
| /evidence/compare/ | 11.7 | 12.87 | 11.7 | 10.9 | PASS | 10.9 → 11.0 | 6.8 → 6.4 | 6.9 → 6.4 | — → — | 2 / 2 | 283534 → 300895 | 4 |
| /readings/ | 7.9 | 8.69 | 7.9 | 7.2 | PASS | 7.4 → 7.4 | 4.6 → 4.9 | 5.2 → 5.0 | — → — | 1 / 1 | 272423 → 289782 | 4 |
| /readings/how-money-reaches-households/ | 35.8 | 39.38 | 35.8 | 32.1 | PASS | 34.3 → 34.0 | 22.1 → 22.2 | 24.4 → 22.6 | — → — | 2 / 3 | 284413 → 301774 | 4 |
| /data/ | 18.6 | 20.46 | 18.6 | 16.9 | PASS | 18.2 → 18.0 | 17.0 → 15.7 | 16.1 → 14.8 | — → — | 2 / 2 | 332040 → 349402 | 4 |
| /methodology/ | 15.8 | 17.38 | 15.8 | 13.5 | PASS | 16.2 → 15.5 | 10.3 → 9.5 | 10.1 → 8.7 | — → — | 2 / 3 | 277404 → 294765 | 4 |
| /measurement/ | 23.1 | 25.41 | 23.1 | 20.2 | PASS | 23.2 → 22.1 | 15.9 → 14.6 | 15.9 → 14.0 | — → — | 2 / 2 | 294558 → 311915 | 4 |
| /about/ | 7.2 | 7.92 | 7.2 | 6.3 | PASS | 7.7 → 7.1 | 4.3 → 4.0 | 4.1 → 3.8 | — → — | 2 / 3 | 272071 → 289433 | 4 |
| /corrections/ | 5.2 | 5.72 | 5.2 | 4.6 | PASS | 5.3 → 5.0 | 3.3 → 3.0 | 3.3 → 3.1 | — → — | 1 / 1 | 272209 → 289568 | 4 |
| /contact/ | 5.9 | 6.49 | 5.9 | 5.4 | PASS | 5.7 → 5.5 | 3.7 → 3.5 | 3.9 → 3.7 | — → — | 1 / 1 | 272396 → 289755 | 4 |


## The first evidence unit at AR 390 × 844 (value, scope, period, limit, verification link)

A part counts as visible when its element lies wholly inside the first 844 px. Home: the first figure card (the paced
group and its bound record; the limit is the group's last sentence). CLM-001: the record (finding, record line, what it
does not establish, where it comes from). /payments/: the first figure card (panel, caption, foot boundary, record
link). Positions in px from the top of the page (`first_unit_ar390_*.json`).

| Route | Part | base top–bottom | visible | p1 top–bottom | visible |
|---|---|---|---|---|---|
| /ar/ | value | 670–703 | yes | 787–819 | yes |
| /ar/ | scope | 1297–1351 | no | 1246–1266 | no |
| /ar/ | period | 1127–1228 | no | 1106–1190 | no |
| /ar/ | limit | 600–1113 | no | 740–1081 | no |
| /ar/ | link | 1357–1391 | no | 1270–1303 | no |
| /ar/ | **all five** | | no | | no |
| /ar/evidence/CLM-001/ | value | 716–749 | yes | 616–645 | yes |
| /ar/evidence/CLM-001/ | scope | 442–493 | yes | 380–422 | yes |
| /ar/evidence/CLM-001/ | period | 338–438 | yes | 310–372 | yes |
| /ar/evidence/CLM-001/ | limit | 2570–2809 | no | 2180–2388 | no |
| /ar/evidence/CLM-001/ | link | 3578–3611 | no | 3118–3150 | no |
| /ar/evidence/CLM-001/ | **all five** | | no | | no |
| /ar/payments/ | value | 3403–6112 | no | 3193–5623 | no |
| /ar/payments/ | scope | 3243–3391 | no | 3077–3181 | no |
| /ar/payments/ | period | 3243–3391 | no | 3077–3181 | no |
| /ar/payments/ | limit | 6170–6354 | no | 5681–5873 | no |
| /ar/payments/ | link | 6416–6447 | no | 5930–5960 | no |
| /ar/payments/ | **all five** | | no | | no |

## Keyboard-focus walk (the §8.4 method: 70 Tab presses from the top; upward jumps inside `<main>` of more than 12 px)

| View | base: upward jumps | p1: upward jumps | p1: focused elements without a visible indicator |
|---|---|---|---|
| ar:/@390 | 0 | 0 | 0 |
| ar:/payments/@390 | 0 | 0 | 0 |
| ar:/evidence/CLM-001/@390 | 0 | 0 | 0 |
| ar:/explore/@390 | 0 | 0 | 0 |
| ar:/readings/@390 | 0 | 0 | 0 |
| ar:/readings/how-money-reaches-households/@390 | 0 | 0 | 0 |
| ar:/data/@390 | 0 | 0 | 0 |
| ar:/measurement/@390 | 0 | 0 | 0 |
| ar:/methodology/@390 | 0 | 0 | 0 |
| ar:/evidence/compare/@390 | 0 | 0 | 0 |
| ar:/evidence/@390 | 0 | 0 | 0 |
| ar:/about/@390 | 0 | 0 | 0 |
| ar:/contact/@390 | 0 | 0 | 0 |
| en:/@1440 | 2 | 3 | 0 |
| en:/payments/@1440 | 2 | 2 | 0 |
| en:/evidence/CLM-001/@1440 | 1 | 1 | 0 |
| en:/explore/@1440 | 1 | 1 | 0 |
| en:/readings/@1440 | 1 | 1 | 0 |
| en:/readings/how-money-reaches-households/@1440 | 0 | 0 | 0 |
| en:/data/@1440 | 11 | 11 | 0 |
| en:/measurement/@1440 | 1 | 1 | 0 |
| en:/methodology/@1440 | 1 | 1 | 0 |
| en:/evidence/compare/@1440 | 1 | 1 | 0 |
| en:/evidence/@1440 | 1 | 1 | 0 |
| en:/about/@1440 | 1 | 1 | 0 |
| en:/contact/@1440 | 1 | 1 | 0 |
| ar: Home search band, Enter then Escape | — | opens the dialog with its field focused: True; Escape returns focus: True | |
| en: Home search band, Enter then Escape | — | opens the dialog with its field focused: True; Escape returns focus: True | |

The one new wide-screen jump is on Home: inside the figure cards, from the tall first card's record link to the second
card's at the top of the next column (the column-wise pattern G2 recorded for /data/'s two-column source cards). The
others are the patterns recorded in design record §8.4 (Home's topics above the figures; the rail after the page's
last control; /data/'s two-column cards). Zero upward jumps on every phone view.
