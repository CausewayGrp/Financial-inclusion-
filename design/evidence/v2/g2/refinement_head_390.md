# G2 refinement (DL-V2-011) — head positions at 390 px on the final tree, both editions

Measured on the built site served gzip (the `g0_measure.py` server), viewport 390 × 844, `getBoundingClientRect` plus the
scroll offset, rounded to the pixel: the title (`h1`), the boundary heading (`.bnd h2`) and the first marked figure
(`.fnum`), as top–bottom in px from the top of the page. Two measurements are kept: on `cd3e951a` (the anchor rule
alone: 2 px rule, 8 px margin, 2 px reclaimed from the tools row, net +8 px per phone head) and on the final tree, after
the tools moved behind the actions in the markup (the spacing rule that had followed the tools no longer applies, so
every head with a statement is 8 px shorter again; record heads, which have no statement, are unchanged).

| View | Title | Boundary heading cd3e951a → final | First figure (final) |
|---|---|---|---|
| ar / | 133–221 | 2856–2888 → 2848–2880 | 670–703 (in the first screen) |
| ar /people/ | 229–317 | 879–911 → 871–903 | — |
| ar /payments/ | 261–349 | 819–851 → 811–843 (in the first screen) | — |
| ar /remittances/ | 229–356 | 796–828 → 788–820 (in the first screen) | — |
| ar /firms/ | 229–317 | 955–987 → 947–979 | — |
| ar /finance/ | 261–333 | 864–896 → 856–888 | — |
| ar /providers/ | 261–349 | 850–882 → 842–874 | — |
| ar /access/ | 229–356 | 796–828 → 788–820 (in the first screen) | — |
| ar /reforms/ | 229–317 | 909–941 → 901–933 | — |
| ar /evidence/CLM-001/ | 196–324 | 2532–2562 → 2532–2562 | 716–749 (in the first screen) |
| en / | 155–234 | 2822–2847 → 2814–2839 | 735–762 (in the first screen) |
| en /people/ | 235–348 | 846–872 → 838–864 | — |
| en /payments/ | 286–399 | 897–948 → 889–940 | — |
| en /remittances/ | 260–353 | 800–851 → 792–843 (in the first screen) | — |
| en /firms/ | 260–374 | 897–923 → 889–915 | — |
| en /finance/ | 286–379 | 876–928 → 868–920 | — |
| en /providers/ | 260–339 | 863–914 → 855–906 | — |
| en /access/ | 260–325 | 772–823 → 764–815 (in the first screen) | — |
| en /reforms/ | 260–325 | 925–976 → 917–968 | — |
| en /evidence/CLM-001/ | 211–304 | 2329–2346 → 2329–2346 | 559–586 (in the first screen) |

Reading: the domain exception of the design record §7.4 (the boundary section follows the head at 1.0–1.2 screens on every
domain) holds on every domain in both editions; on the final tree the AR /payments/ boundary heading is back inside the
first screen (it ended at 843 px before the anchor, 851 px with it, 843 px again now). Home and the record keep the
first figure in the first screen. The figures of a domain's answer are governed prose, not marked (`.fnum` is a Home
and record device, D3).
