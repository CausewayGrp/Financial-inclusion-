# Keyboard-focus walk, 18 October 2026 — before (cd3e951a) and after the markup-order fix, both editions, 390 and 1440 px

Method: Chromium (Playwright) on the built site served gzip; Tab pressed up to 60 times from the top of each page; the
focused element's text, region and page y position recorded after every press; a step counts as an upward jump when focus
moves more than 4 px up the page inside the main content (the masthead and the skip link are excluded). Every focused
element showed a visible focus ring (outline or box shadow). The sixty steps reach past the head, the figures, the index
and the first sections of every page. Not a conformance claim.

| View | Upward jumps before → after | What the remaining jumps are |
|---|---|---|
| ar390/ | 2 → 0 | — |
| ar390/payments/ | 1 → 0 | — |
| ar390/evidence/CLM-001/ | 0 → 0 | — |
| ar390/data/ | 0 → 0 | — |
| ar390/readings/how-money-reaches-households/ | 0 → 0 | — |
| en390/ | 2 → 0 | — |
| en390/payments/ | 1 → 0 | — |
| en390/evidence/CLM-001/ | 0 → 0 | — |
| en390/data/ | 0 → 0 | — |
| en390/readings/how-money-reaches-households/ | 0 → 0 | — |
| ar1440/ | 2 → 2 | Home at 900 px and above keeps the topics line above the figures (G2 pass two, recorded); the markup carries the phone order; after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| ar1440/payments/ | 2 → 1 | after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| ar1440/evidence/CLM-001/ | 1 → 1 | after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| ar1440/data/ | 9 → 9 | two-column source cards at 1200 px: card n ends, card n+1 starts higher (column-wise, expected) |
| ar1440/readings/how-money-reaches-households/ | 0 → 0 | — |
| en1440/ | 2 → 2 | Home at 900 px and above keeps the topics line above the figures (G2 pass two, recorded); the markup carries the phone order; after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| en1440/payments/ | 2 → 1 | after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| en1440/evidence/CLM-001/ | 1 → 1 | after the page's last control, focus enters the desktop rail (a navigation landmark after main; it sits beside the page, sticky) |
| en1440/data/ | 9 → 9 | two-column source cards at 1200 px: card n ends, card n+1 starts higher (column-wise, expected) |
| en1440/readings/how-money-reaches-households/ | 0 → 0 | — |

Before: on every family with a statement, in both editions at both widths, the two tools (cite, report) were tabbed before
the two calls to action although they sit below them; on Home at 390 the eight topic links were tabbed before the first
figure's evidence link, then focus jumped up about 1.4 screens. After: the tools follow the actions in the markup
(`families.head_block`, `render.home`) and the Home figures, the index and the topics block are in the markup in the phone
order (`render.home`); the stylesheet's `order` rules for the phone are gone and only the wide screen reorders the Home
topics line (two declarations). No positive tabindex, no duplicated control, no text changed.
