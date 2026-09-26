# S01 Navigation, Search & First-Use Stress Test

**Purpose:** close S01 against concrete user tasks rather than route existence alone.  
**Scope:** static build, generated DOM, JavaScript/CSS behavior, route/link validation and local HTTP smoke. This is not a claim of full browser/device/screen-reader acceptance; those gates remain S05/S07/S08.

## Test matrix

| User task / hostile case | Expected behavior | S01 result |
|---|---|---|
| Open the site at 320–390px | Primary nav is not lost; menu and search remain reachable with 44px-class controls. | PASS at CSS/DOM/JS level. |
| Open/close mobile navigation | Toggle has `aria-expanded`; route selection, Escape, outside click and desktop resize close stale menu state. | PASS. |
| Search from any public page | Global modal opens, moves focus to search, returns focus on close, exposes loading/result/error state. | PASS. |
| Keyboard-search without finding the icon | `Ctrl/Cmd+K` opens search; `/` opens search when focus is not inside a typing control. | PASS. |
| Search Arabic with diacritics/alef variants | Search matching removes Arabic diacritics and folds alef variants / alif maqsura without changing the controlled index. | PASS. |
| Search by stable evidence/source ID | Stable IDs receive explicit matching weight; source results keep their controlled public route. | PASS. |
| Duplicate index entries target one destination | Search de-duplicates identical title+route results before the top-ten display and prefers the substantive non-page record over a generic page entry. | PASS. |
| Follow a source search result | `/data/?source=<ID>` resolves to the named source record and moves focus to it. | PASS. |
| Locator-only source | Only stable source ID + original locator appear; no title, publisher, licence or rights are inferred. | PASS. |
| Source with no public locator | It is not rendered as a standalone public source card. | PASS. |
| Follow a stale/shared route | Bilingual 404 offers Home, Explore, Evidence and Search rather than a technical dead end. | PASS. |
| Switch language from a deep route | Equivalent route is preserved, including query string and hash. | PASS at JS path level. |
| Compare evidence on a narrow screen | Comparison table remains usable through horizontal containment rather than viewport overflow. | PASS at CSS/DOM level. |
| Navigate by keyboard | Visible focus treatment exists; search and menu state are keyboard controllable. | PASS at static/interaction-code level; assistive-technology acceptance pending S05. |
| Public Arabic leakage | Generated pages are scanned for prohibited backend expressions including `ساعات الدليل` / `ساعات أدلة` and other internal vocabulary. | PASS after replacing Home wording with `اختلاف توقيت القياس`. |
| Public backend/vendor leakage | Generated HTML is scanned for legacy build/vendor/control strings. | PASS. |
| Internal links and locale direction | All generated internal routes resolve; Arabic is RTL and English LTR. | PASS. |

## Structural regression checks

- 141 controlled Page Specs are consumed.
- 284 locale/public HTML documents are generated including locale routes and root/404 outputs under the existing build convention.
- Source search routes resolve against the 149-record controlled source map; 148 are publicly addressable under current locator/display state, with one no-public-locator dependency withheld from standalone rendering.
- Empty public paragraphs/cards and duplicate stable-ID answer cards are validation failures.
- Top-level current navigation state uses `aria-current="page"`.
- `docs/S01_REFERENCE_CHALLENGE.md` and this stress test are required repository controls.

## Known boundary after S01

S01 does **not** close page-density/composition, full Arabic/English editorial invariance, visual-system quality, real-device RTL, screen-reader behavior, performance/privacy/security deployment, or source-owner revalidation. Those remain intentionally assigned to S02–S08. The repository must not be labelled live-release ready on the basis of S01.
