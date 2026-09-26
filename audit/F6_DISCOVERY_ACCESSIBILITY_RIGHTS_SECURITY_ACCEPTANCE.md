# F6 — Discovery, accessibility, rights, security and privacy (pre-Design acceptance)

**Date:** 26 September 2026 · **Directive:** D7 §F6 · **State:** CLOSED / FROZEN
**Scope:** the reference build in `dist/` and the repository. No Master change (the content is F5's; Master
`ed3c5796…` unchanged). This is a pre-Design, repository-level acceptance: **not** a WCAG conformance claim, not a live
penetration test, not legal review and not rights clearance.

## 1. SEO and discovery

One implementation, [`scripts/discovery.py`](../scripts/discovery.py), used by the build and checked by the validator
(gates F6-G01…G05). The deployment contract is in [`docs/DEPLOYMENT.md`](../docs/DEPLOYMENT.md#discovery-f6).

| D7 requirement | State in the reference build | Gate |
|---|---|---|
| Unique native `<title>` | One per page; 143 unique titles per language, taken from the Master | F6-G01 |
| Unique native meta description | One per page, unique per language, ≤ 200 characters, from the governed description or the page's own opening text | F6-G01 |
| Truthful H1 | Exactly one `<h1>` per page; Reading `<h1>` = the 08 title (TC-G02) | F6-G01, S05.1, TC-G02 |
| Language-correct metadata | `lang`/`dir` match the path (`/ar/` → `ar`, `rtl`) | F6-G01 |
| Self-canonical | Canonical = the same route in the same language | F6-G02 |
| Reciprocal hreflang | Every page lists `en`, `ar`, `x-default`; each pair points to the other page, which exists | F6-G02 |
| `x-default` only for a real neutral entry | `/` is a real neutral entry route: it opens the reader's chosen edition, otherwise Arabic | F6-G02 |
| Sitemap coverage | Written only when the public origin is set (see §1.1); a sitemap built for a test origin covers all 286 localized pages once, each with three alternates | F6-G03 |
| Robots / indexability | Pre-release: `robots.txt` disallows crawling; 404 is `noindex` | F6-G03, F6-G05 |
| BreadcrumbList where implemented | On Evidence Records and Readings (the pages that show a breadcrumb), with the visible names | F6-G04 |
| Article for Readings, true fields only | Headline, description (standfirst), language, publisher CauseWay, part of the resource. **No author** (authorship of the Readings is not governed), **no dates** (the Master holds a review date, not a publication or modification date), **no image** | F6-G04 |
| Dataset only where valid | **None.** The resource publishes evidence records and a source directory, not datasets; `/data/` is a directory of original sources | F6-G04 |
| No fake author/date/image | Enforced | F6-G04 |
| Search index updated | Regenerated from the Master on every run; 435 records; Reading is its own result type (10) | P2.2 canonical probe |
| Internal links correct | Existing link gates; every localized route exists in both languages | validator, F6-G02 |
| No keyword stuffing | Titles and descriptions are governed prose; nothing is added for search engines | — |

### 1.1 Public origin (release-only)

`site-src/deployment.json` holds `public_origin: null`. The release domain is an owner decision and is not guessed. When
it is set, the same build makes canonical, hreflang, sitemap and structured-data URLs absolute, allows crawling and
writes `sitemap.xml`; the validator then requires the sitemap to equal its derivation. Until then the build is a
pre-release build and asks not to be indexed. Open item: RELEASE_ONLY / OWNER_INPUT.

## 2. Evidence Readings across the site

| Surface | Required | Found |
|---|---|---|
| Home | One Featured Reading, not a carousel | One (CWR-004) — RP-G03 |
| Explore | One relevant `Go deeper / تعمّق في التحليل` | One, the same featured Reading — RP-G03 |
| Domain pages | 1–2 relevant Readings at most | At most two — RP-G04 |
| Evidence Record | `Used in this Reading / يُستخدم هذا الدليل في قراءة…` | "Used in these Evidence Readings / يُستخدم هذا الدليل في قراءات الأدلة الآتية" on every bound record — RP-G04 |
| Measurement Agenda | `This gap is examined in… / تناقش هذه الفجوة في…` | On the seven priorities a Reading examines |
| Search | Reading as a distinct result type | `reading` (10 records) |

## 3. Accessibility contract (WCAG 2.2 as the implementation target)

Outcomes the design and the implementation must meet. "Reference build" states what exists now and how it is checked;
nothing here is certified, and conformance can only be stated after the final implementation is audited.

| Outcome | WCAG 2.2 | Reference build now | Design / Code must |
|---|---|---|---|
| Keyboard access | 2.1.1, 2.1.2, 2.4.3 | Skip link first in tab order; every focusable element in `<main>` reachable; menu and search dialog open and close by keyboard, Escape closes, focus returns to the opener | Keep every function operable by keyboard with a logical order; no keyboard trap; no hover-only action |
| Visible focus, not obscured | 2.4.7, 2.4.11 | 3 px focus outline with offset on every interactive element; `scroll-padding-top` keeps focused targets clear of the sticky header | Keep a visible focus indicator of sufficient contrast; focused elements never hidden by sticky or floating UI |
| Target size | 2.5.8 | Buttons and icon controls at least 44 × 44 CSS px; mobile navigation actions 44 px high | At least 24 × 24 CSS px for every target (44 recommended for primary touch controls), or sufficient spacing |
| Zoom and reflow | 1.4.4, 1.4.10 | No horizontal page overflow at 320, 390, 640 and 1440 px in both languages (168/168 page-width checks) | Content reflows at 320 CSS px and 400 % zoom without loss; tables scroll inside a named, focusable region |
| Screen-reader names | 4.1.2, 1.3.1, 2.4.6 | Named navigation landmarks, named dialog, named icon-only buttons, named comparison region with a table caption, `aria-current` in breadcrumbs, live regions for search and technical errors | Every control and landmark has an accessible name; headings describe their sections; one `<h1>` per page |
| Form labels and errors | 3.3.1, 3.3.2, 4.1.3 | Search input, source filter and Compare selects are labelled; malformed or unknown links are announced technical errors (`role="alert"`), and "no result" is never presented as "no evidence" | Keep labels visible or programmatic; describe errors in text; announce status changes |
| No meaning by colour alone | 1.4.1, 1.4.3, 1.4.11 | Comparison states, evidence badges and chart states carry text labels (`data-noncolour-semantic`) | Every colour-coded state also has text or shape; contrast at least 4.5:1 for text and 3:1 for UI and graphic objects |
| Analytical text alternatives for visuals | 1.1.1, 1.3.1 | Every governed visual has an analytical text alternative in both languages, carrying the same scope line (P3 gates) | Keep each visual's text alternative next to it; never convey a number only in an image |
| RTL focus and reading order | 1.3.2, 2.4.3 | Arabic pages declare `dir="rtl"`; layout uses logical CSS properties; DOM order equals reading order | Mirror layout, not meaning: numbers, identifiers and Latin codes keep their own direction (`<bdi>`, `dir="ltr"`); focus order follows the Arabic reading order |
| Reduced motion | 2.3.3 | `prefers-reduced-motion` removes smooth scrolling and transitions (checked in the viewport suite) | No motion is needed to understand anything; honour the reduced-motion preference |
| Mobile touch | 2.5.1, 2.5.2, 2.5.8 | No path-based gestures; menu toggles `aria-expanded`; targets as above | Single-pointer operation for everything; no drag-only interaction; no action on pointer-down |

The checks behind "reference build now" are `scripts/tests/test_public_tools.py`,
`audit/tranche_c/checks/viewport_acceptance.py` and validator gates S05.1–S05.2, P2-G03 and P3-G01…G03. The
Accessibility page says the resource is designed against WCAG 2.2 and is still to be tested; it claims no conformance.

## 4. Rights, security and privacy (pre-Design)

| D7 check | Result | Gate |
|---|---|---|
| No secrets | No key, token, private key or credential pattern in any tracked text file | F6-G06 |
| No private locators | None in the public build or governed content | R85-G07 |
| No bundled restricted source documents | The only tracked office/PDF/archive file is the Production Master; `dist/` holds only web files; sources are linked, never republished | F6-G07 |
| Explicit rights and publication state | Every source record states `rights_state` (all `NOT_ASSESSED`) and `public_card_state`; source cards show the reuse notice; the nine sources without a public locator are never named or linked | F6-G08, S04.1–S04.3 |
| No unsafe raw HTML assumptions | Build output is escaped; `app.js` escapes every value it renders from data | review; F6-G05 |
| CSP / header expectations documented for Code | [`docs/DEPLOYMENT.md`](../docs/DEPLOYMENT.md#security-and-privacy-expectations-for-code): strict CSP, HSTS, nosniff, referrer and permissions policies. The build now satisfies a strict CSP: page data moved from inline scripts to JSON blocks, the root redirect moved to `assets/lang-redirect.js`, no inline style | F6-G05 |
| Privacy-minimal forms | There is no form; reports go by e-mail with a warning not to send personal data | F6-G05 |
| No analytics or tracking without policy | None; one functional preference (`yfie-lang`) on the reader's device, stated on the Privacy page | F6-G05 |

## 5. Changes made in F6

- `scripts/discovery.py` (new) and `site-src/deployment.json` (new): canonical, hreflang (self + pair + `x-default`),
  robots policy, sitemap derivation, JSON-LD.
- `scripts/build.py`: head links and structured data from `discovery.py`; `robots.txt`; sitemap when an origin is set;
  404 `noindex`; bilingual root title from governed copy; root redirect moved to `site-src/lang-redirect.js`; Compare and
  record-context data as JSON blocks.
- `site-src/app.js`: reads page data from the JSON blocks (`DATA(id)`).
- `scripts/validate.py`: gates F6-G01…G08; R85-G05 ignores JSON-LD; S04.2 and P2-G02 follow the JSON blocks.
- `scripts/tests/test_public_tools.py`: reads Compare data from its JSON block.
- `docs/DEPLOYMENT.md`: discovery and header contract.

Public wording and evidence are unchanged; every page gained only head links and structured data.

## 6. Definition of Done (D7 §F6)

| Requirement | State |
|---|---|
| SEO/discovery contract complete and internally consistent | **Met** (§1; one implementation checked by F6-G01…G04) |
| Accessibility outcomes explicit | **Met** (§3) |
| Rights/security/privacy pre-Design gates pass | **Met** (§4; F6-G05…G08) |
| No factual or legal claim invented | **Met** — no author, date, image, dataset, domain, conformance, clearance or security guarantee asserted |
