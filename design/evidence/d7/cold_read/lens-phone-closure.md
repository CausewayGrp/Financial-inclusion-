# Lens C — phone closure cold read

Independent reviewer, rendered product only (http://localhost:4173). No design records consulted.
Primary viewport 390x844, device scale 2, mobile/touch emulation. 320x568 where noted.
Judged as a phone reader with somewhere to be. Lengths and overflow measured from the DOM
(`getBoundingClientRect()`, `document.documentElement.scrollWidth`), not estimated from pictures.

Date of read: 2026-09-28.

---

## Cross-page measurement table (390x844)

| Page | scrollWidth vs 390 | Total height | Screens (844px) | h1 y | Contents strip y | Footer height |
|---|---|---|---|---|---|---|
| /en/ | 390 / 390 ok | 8189 | 9.7 | 105 | 2046 | 575 |
| /ar/ | 390 / 390 ok | 8514 | 10.1 | 103 | 2132 | 666 |
| /en/explore/ | 390 / 390 ok | 8199 | 9.7 | 128 | 2970 | 575 |
| /en/people/ | 390 / 390 ok | 12976 | 15.4 | 190 | 1723 | 575 |
| /en/data/ | 390 / 390 ok | 31599 | 37.4 | 128 | 487 | 575 |
| /en/evidence/CLM-003/ | 390 / 390 ok | 4933 | 5.8 | 207 | 650 | 575 |
| /en/evidence/compare/ | 390 / 390 ok | 6434 | 7.6 | 128 | 4591 | 575 |
| /en/measurement/ | 390 / 390 ok | 14820 | 17.6 | 128 | 512 | 575 |

No page scrolls horizontally at 390. Overflow-element scan (`right > innerWidth`) returned **0 offenders on
every page**. That is a real, measured pass and it is the strongest thing in this read.

---

## Findings

### 1. No horizontal overflow anywhere — OBSERVATION (positive)
**Pages:** all eight. **Viewport:** 390x844.
`document.documentElement.scrollWidth === window.innerWidth === 390` on every page tested, and a
walk of every element in the DOM found zero elements extending past the viewport in either
direction. The two data tables (`/en/people/` 2-col, w=326; `/en/evidence/compare/` 4-col, w=358)
both sit inside a parent with `overflow-x: auto` and both fit without needing it. Arabic RTL at
`/ar/` is equally clean. This is the cleanest part of the build.

---

### 2. `/en/` first screen is a mission statement, not an answer — SHOULD FIX
**Page:** /en/. **Viewport:** 390x844.
The first screen gives me, in order: the CauseWay brand lockup plus "Yemen Financial Inclusion
Evidence" (publisher: clear, unambiguous, good); H1 at y=105, "Financial inclusion in Yemen is not
one number." (what the page is: clear); then a **357px-tall, eight-line paragraph** of abstract
positioning prose starting at y=217 — "is a bilingual public evidence resource that helps users
understand, compare and verify… It does not make decisions for users or simulate policy outcomes."

Measured: the first *substantive, specific* content — the actual sentence carrying a figure ("The
latest representative population measure is the World Bank's Global Findex 2021 survey…") — begins
at **y=720**, i.e. it is the last thing on the first screen and its first number is cut by the fold.
Everything above it is self-description.

As a phone reader with somewhere to be, I have burned my entire first screen on being told what kind
of website this is. The headline promises "not one number" and then the page spends 357px not giving
me any number. The two actions ("Start with a question", "Verify evidence") sit at y=590 and do
survive the fold, which saves it from BLOCKING.

---

### 3. Primary action links are 30–33px tall — SHOULD FIX
**Pages:** all eight. **Viewport:** 390x844.
Measured heights of the link/button targets in `.actions` and `.open`:

- `/en/` `.actions a` ("Start with a question", "Verify evidence"): **h=33** (w=164, w=120)
- `/en/` `.open a` ("Open evidence record", x4): **h=30** (w=152)
- `/en/explore/` `.open a` ("Open this measurement priority", x5): **h=30** (w=218)
- `/en/people/` `.actions a`: **h=33**; `.open a`: **h=30**
- `/en/data/` `.actions a` / `button.tbtn`: **h=33**
- `/en/evidence/CLM-003/` `.actions`: **h=33** ("Cite this record" w=120, "Citation and reuse" w=144,
  "Corrections & release history" w=228, "Report an issue" w=121)
- `/en/evidence/compare/` `.actions`: **h=33**
- `/en/measurement/` `.open a`: **h=30**; `.actions a` ("Explore" w=60): **h=33**

30px and 33px are below the 44px (iOS HIG) and 48px (Material) minimums. These are not incidental
links — `.open` is *the* way into an evidence record, and it is the shortest target on the page. A
site-wide count of interactive elements under 36px tall: /en/ 26, /ar/ 23, /en/explore/ 24,
/en/people/ 39, /en/data/ **421**, /en/evidence/CLM-003/ 30, /en/evidence/compare/ 19,
/en/measurement/ 37.

The header buttons (Search / العربية / Menu) are correctly sized at **h=44**, which shows the
44px target is understood and simply was not carried into the body. The Arabic build is better
here: `/ar/` `.actions a` measure **h=40** and `.open a` **h=35** — still short, but the Arabic line
box happens to be taller. EN and AR therefore differ in tap comfort while carrying identical content.

---

### 4. The page's own contents index is desktop-only; on phone it is buried mid-page — BLOCKING
**Pages:** all eight, worst on /en/evidence/compare/, /en/explore/, /en/people/. **Viewport:** 390x844.

Every page ships two copies of its in-page index:

- `nav.index`, inside `aside.spine`. Computed style at 390px: **`aside.spine { display: none }`**, so
  `nav.index` measures h=0. This is the desktop sticky side rail. The phone never gets it.
- `nav.strip`, an inline horizontal band of the same links, rendered once in the flow of `<main>`.

So on a phone the strip is the only way to see what a page contains. Measured strip positions:

| Page | strip y | page height | strip depth |
|---|---|---|---|
| /en/data/ | 487 | 31599 | 1.5% |
| /en/measurement/ | 512 | 14820 | 3.5% |
| /en/evidence/CLM-003/ | 650 | 4933 | 13% |
| /en/people/ | 1723 | 12976 | 13% |
| /en/ | 2046 | 8189 | 25% |
| /ar/ | 2132 | 8514 | 25% |
| /en/explore/ | 2970 | 8199 | 36% |
| **/en/evidence/compare/** | **4591** | **6434** | **71%** |

On `/en/evidence/compare/` the contents list — "01 Can these records actually be compared? / 02 Three
measures that cannot be combined / 03 Continue from here" — appears at y=4591, five and a half screens
down, *after* I have already scrolled through the whole of section 01 including the comparison table.
It indexes content I have already passed. The same is true, less severely, on `/en/` (strip at 2046,
indexing a section that starts at y=658) and `/en/explore/` (strip at 2970, indexing a section that
starts at y=366).

I also confirmed there is **no in-page index in the Menu**. Tapping `.tbtn.menu` (`aria-controls="primary-nav"`)
opens a 335px panel whose entire contents are the six site-level destinations: "Explore / Evidence /
Evidence Readings / Data & sources / Method & Measurement / Methodology / Measurement Agenda". Nothing
about the page I am on. There is no sticky element of any kind on any of the eight pages
(`position: sticky|fixed` scan: **zero matches, all eight pages**) — no sticky header, no progress
indicator, no back-to-top.

Net effect for a phone reader: on a 37-screen page (`/en/data/`) and a 17.6-screen page
(`/en/measurement/`) I get one chance at the index in the first 600px and then nothing for the
remaining 31,000 / 14,300 pixels. Once I am deep in the catalogue there is no way to jump, no way to
know how far down I am, and no way back to the top short of flicking. I call this BLOCKING because it
is not a polish gap — the primary wayfinding affordance of these pages exists, is authored, and is
switched off at phone width, with no phone substitute.

---

### 5. The foot of the page is deliberate — OBSERVATION (positive)
**Page:** /en/ (footer is identical, h=575, 13 links, on all EN pages; /ar/ h=666). **Viewport:** 390x844.
Read at y=7300–8189. The foot is ordered and clearly authored, not dumped:

1. "Continue from here" edge cards (3 destinations with one-line descriptions);
2. a rule, then a tinted band;
3. "TRUST AND RESPONSIBLE USE" — About, Corrections, Rights & reuse, Accessibility, Privacy, Terms, Contact;
4. the CauseWay mark with an attribution sentence: "Developed and maintained by CauseWay. A public
   resource linking each claim to its evidence and original source.";
5. "EXPLORE AND VERIFY" (Explore, Evidence, Evidence Readings, Data & sources) and
   "METHOD & MEASUREMENT" (Methodology, Measurement Agenda);
6. "© 2026 CauseWay · Published evidence remains attributed to the original source. · Edition of 26…".

Publisher, provenance, redress and edition are all present at the foot. This is the one place where
the phone gets a complete, self-contained answer to "who is this and can I trust it".

---

### 6. "Continue from here" cards split title from description across a blank band — OBSERVATION
**Pages:** /en/, /en/evidence/compare/ (pattern is site-wide). **Viewport:** 390x844.
In the `nav.edges` list the tappable `<a>` is **42px tall and contains only the title**; the
description is a sibling rendered below it, separated by a conspicuous empty band. Measured: the
`<ul>` is 324px for three items (108px each) of which only 42px is the link. Read on screen, the
sequence is `rule / "Measurement Agenda" / ~60px of nothing / "What remains unknown and what
measurement would strengthen the decision." / rule`, which at phone width reads as two unrelated rows
and briefly suggests the description belongs to the *next* item. The description is also not part of
the tap target.

---

### 7. `/ar/` is a clean RTL mirror and slightly better to tap — OBSERVATION (positive)
**Page:** /ar/. **Viewport:** 390x844.
`dir=rtl`, `lang=ar`. Header order mirrors correctly (logo far right, brand beside it, then بحث / EN /
القائمة running right to left). H1 and body are right-aligned; the actions "ابدأ بسؤال" and "تحقق من
الأدلة" are flush to the right margin, mirroring the flush-left EN placement. Guillemets («…») render
correctly. Latin numerals are used consistently in the Arabic text (11.9%, 2021, 2022), matching EN,
so no digit-form drift. `scrollWidth` 390, zero overflow elements.

Page is 8514px against EN's 8189 (+4%), footer 666px against 575 (+16%) — proportionate, not a break.
The AR H1 wraps to two lines against EN's three, so the AR first screen actually reaches the first
figure (11.9%) at the fold where EN does not. Arabic tap targets measure taller than English
(`.actions a` h=40 vs 33, `.open a` h=35 vs 30), which is a side effect of the Arabic line box rather
than a decision, but it means the two co-authoritative languages are not equally comfortable to tap.

---

### 8. `/en/explore/` spends 611px and three nested framings before the first question — SHOULD FIX
**Page:** /en/explore/. **Viewport:** 390x844.
Measured from H1 top (y=128) to the first question link (y=739): **611px, 0.72 of a screen**, occupied
by three stacked heading-plus-paragraph layers that all say a version of the same thing:

- H1 "Start with the question, not the dataset." + 128px intro ("The question determines what evidence
  is relevant…")
- "01 START WITH A QUESTION / Questions to start from" + 143px ("Use the questions below to enter the
  evidence from the problem you need to resolve…")
- "QUESTIONS THAT LEAD INTO THE EVIDENCE / Find the question closest to your decision" + 44px ("Every
  answer keeps its period, population or calculation base, limits and source in view.")

On a wide screen these three layers sit together in one field of view and read as a hierarchy. Stacked
in a 390px column they read as the page saying "start with a question" three times before letting me
see one. This is the clearest instance of a desktop editorial rhythm transplanted unchanged.

---

### 9. `/en/people/` has the best first screen on the site — OBSERVATION (positive)
**Page:** /en/people/. **Viewport:** 390x844.
The eyebrow "THE QUESTION THIS PAGE ANSWERS / Who is being left behind — and where are the measured
gaps?" sits at y=128, H1 at y=190, and the lead paragraph at y=301 carries the actual figures — 11.9%
of adults, 5.44% of women, 18.35% of men — **entirely above the fold**, together with the wave, the
fieldwork window and the disclaimers ("It is not a 2026 rate, it does not explain the gaps"). A phone
reader who never scrolls still leaves with a correctly-qualified number. Every other page should be
measured against this one.

---

### 10. `/en/people/` bar figures are readable and geometrically truthful at 390 — OBSERVATION (positive)
**Page:** /en/people/. **Viewport:** 390x844, read at y=3280.
The account-ownership figure (`figure.fig`, 358x3322 at y=3114) renders as a labelled horizontal bar
list, each track a 326x30 SVG, on a tinted panel. Unit and method are stated above the bars ("% of
adults (ages 15+) · Measured in a survey"), and the universe is stated above that, including the
exclusion ("the survey frame excludes areas with about 23% of the population").

Bar geometry checked against the values: All adults 11.9 → ~225px, Women 5.44 → ~103px, Men 18.35 →
~347px, poorest 40% 6.5 → ~125px, richest 60% 15.5 → ~293px, primary-or-less 6.98 → ~135px,
secondary-or-more 19.53 → ~370px. Ratios hold to within a pixel (18.35/11.9 = 1.542; 347/225 = 1.542),
so the scale is linear and zero-based and shared across subgroups. No truncated axis, no per-bar
rescaling. Derived gaps are labelled as derived — "Calculated here from published figures · 12.91
Percentage points" — rather than presented as published values. Smallest text in the figure measures
12.5px, which is legible but is the smallest type on the page.

---

### 11. `/en/data/` is 31,599px — 37 phone screens — with no wayfinding below y=1323 — BLOCKING
**Page:** /en/data/. **Viewport:** 390x844.
Total document height **31,599px = 37.4 screens**. Section 01 alone ("Source directory and
verification", y=1036 to y=15229) is **14,193px = 16.8 screens** of continuous catalogue. The page
states "151 sources or references shown" and contains 112 `<details>` elements; each entry renders at
roughly 500–550px (title, publisher/type/year, reference code, description, a "Does not establish"
paragraph, two actions, a reuse-terms line and a disclosure).

The catalogue is internally organised into seven thematic groups — "Research and analysis on Yemen's
financial sector" (y=1484), "Programmes and projects in Yemen" (4071), "Yemen's economy and policy
context" (7180), "Official Yemen documents and statistics" (9158), "Measurement standards and methods"
(11398), "Payment-system design and digital payments" (13159) — **and not one of them is in the
contents strip**, which lists only the eleven H2 sections. So the structure that would actually let me
move around the catalogue is invisible.

There is a partial mitigation: a search input (`type=search`, h=46, placeholder "e.g. SRC-CBY…") at
y=1323. It is correctly sized to tap, but it is 1.6 screens down, and its placeholder invites a
reference code — it looks like a lookup for someone who already knows the code, not a filter for
someone browsing. There is no result count control, no pagination, no group filter, no sticky
section marker and no back-to-top. Once past y=1323, a phone reader has 30,000px of uninterrupted
scroll and no instrument.

This page has 421 interactive elements under 36px tall — by far the highest on the site.

---

### 12. `/en/evidence/CLM-003/` first screen is complete and honest — OBSERVATION (positive)
**Page:** /en/evidence/CLM-003/. **Viewport:** 390x844.
Above the fold, in order: breadcrumb "Evidence / CLM-003" (y=106), the type label "EVIDENCE RECORD",
the measurement window as a labelled pair ("When was it measured or observed? / Mar-2025–Jan-2026"),
H1 "POS infrastructure expanded" (y=207), then the whole of section 01 with its figures — 561 in March
2025 to 1,473 in January 2026, and the declared conflict: "The December 2025 total of 1,357 and the
January 2026 total of 1,473 imply growth of 8.55%, while the January source graphic displays +11%;
both are shown, and the difference is recorded as an inconsistency within the source."

A phone reader gets the claim, the period, the source, and the source's own internal contradiction
without scrolling. At 4,933px (5.8 screens) this is also the shortest page of the eight and the one
that feels proportionate to a phone.

Minor: the contents strip immediately below repeats "01 What does this evidence establish?" as a link
to content I have just finished reading, three inches above it.

---

### 13. `/en/evidence/compare/` renders the same two sentences twice, back to back — SHOULD FIX
**Page:** /en/evidence/compare/. **Viewport:** 390x844, read at y=700.
The long introductory paragraph ends: "…**Does not establish: The same word does not mean the same
measure. The comparison does not reconcile differing figures or prefer one number unless evidence on
their definitions supports it.**" Roughly 70px below, a bordered callout headed "DO NOT INFER:" repeats
the identical two sentences verbatim. Confirmed in the DOM: a paragraph-level count of the string
"The same word does not mean the same measure." returns **2** at both 390 and 320.

On a wide screen the callout is probably an aside beside the prose; stacked on a phone it reads as the
page stuttering. It also means the 456px intro paragraph could lose its tail entirely without any loss
of meaning.

---

### 14. The comparison table reflows well but its record legend scrolls away — OBSERVATION / SHOULD FIX
**Page:** /en/evidence/compare/. **Viewports:** 390x844 and 320x568.
The 4-column, 7-row table does **not** side-scroll on either viewport. Measured: every cell in the
header row reports the full container width (358px at 390, 288px at 320), `table.scrollWidth` equals
the wrapper width, and the wrapper's `overflow-x: auto` is never engaged (`wrap.scrollWidth >
wrap.clientWidth` is false). It has been genuinely reflowed into a stacked layout: the record names
appear once at the top as a numbered legend ("1 Latest representative account-ownership measure
available / 2 Wallet and subscriber counts from different publications are not yet reconciled"), and
every subsequent dimension ("Definition", and so on) is a heading under which each record's value
appears prefixed by its number. This is the right answer for a comparison on a phone, and it is
well executed. Cell text measures 14.5px, readable.

The cost: the table is **1,928px (2.3 screens) at 390 and 2,211px (3.9 screens) at 320**, and the
legend that defines what "1" and "2" mean appears only at the top. By the third dimension the legend
is off-screen and the reader is comparing two anonymous numerals with no sticky header and no
repeated label. At 320 this is worse — nearly four screens between the legend and the last row.
Secondary: "Assessment" is listed in the same top block as the two numbered records without a number,
so on first read it can look like a third record.

The four record selectors are correctly built for touch — `<select>` elements measuring **h=44,
w=358** (288 at 320), the only body controls on the site that meet the 44px target. Their option text
truncates ("Latest representative account-ownership me…"), which is acceptable for a native picker.

At 320x568 the page grows to 7,468px (13.1 screens, from 7.6 at 390) with `scrollWidth` 320 and zero
overflow elements.

---

### 15. `/en/evidence/compare/` puts its contents list at 71% scroll depth — BLOCKING (instance of #4)
**Page:** /en/evidence/compare/. **Viewport:** 390x844.
Recorded separately from #4 because this is the sharpest case. Page height 6,434px. The contents strip
sits at **y=4,591 — 71% of the way down**. Its three entries are "01 Can these records actually be
compared?" (the section that begins at y=530 and contains the entire comparison table), "02 Three
measures that cannot be combined" (y=4,792) and "03 Continue from here" (y=5,404). Two of its three
targets are within one screen of the strip itself; the third is 4,000px above it. As navigation it is
worthless; as a summary it arrives after the work is done. A phone reader scrolling this page never
learns, before committing, that there are only three sections.

---

### 16. `/en/measurement/` withholds its agenda until 4.3 screens down — SHOULD FIX
**Page:** /en/measurement/. **Viewport:** 390x844.
Page height 14,820px (17.6 screens). Measured heading positions:

| y | Heading | kind |
|---|---|---|
| 128 | H1 "Missing evidence matters when it could change a decision." | — |
| 1093 | How to read the agenda | about the agenda |
| 1394 | Stable references for citation | about the agenda |
| 1587 | Priority labels describe evidence sequencing | about the agenda |
| 1943 | Why measurement is part of this resource | about the agenda |
| 2384 | What a measurement priority does not establish | about the agenda |
| 2751 | What remains uncertain about the agenda itself | about the agenda |
| 3060 | How the agenda changes | about the agenda |
| 3362 | Verify each gap | about the agenda |
| **3636** | **Measurements that would change decisions** | **the agenda** |

Eight consecutive sections — 2,543px, three full screens — explain, qualify and caveat the agenda
before the agenda appears at y=3,636 (25% of the page). The first screen shows only the H1, a 255px
paragraph of the same caveats, and the contents list. Nothing a reader came for is visible without
scrolling.

The contents strip is correctly placed here (y=512) and does list the payload section, so the reader
who parses eleven entries can jump. That is the mitigation, and it is why this is SHOULD FIX rather
than BLOCKING — but it asks the reader to notice that entries 01–08 are all preamble.

---

### 17. `/en/` and `/ar/` bury their contents strip a quarter of the way down — SHOULD FIX (instance of #4)
**Pages:** /en/, /ar/. **Viewport:** 390x844.
Strip at y=2,046 (EN) and y=2,132 (AR) on pages of 8,189 / 8,514px — 25% depth, 2.4 screens. Its first
entry, "01 Three figures, three different things measured", links *upward* to y=658, content the reader
passed 1,400px ago. So the homepage's index both arrives late and points backwards. `/en/explore/` is
the same pattern at 36% depth (strip y=2,970, first target y=366).

The strip renders correctly as a vertical numbered list at phone width (rows ~45px, comfortable), so
the component is fine; only its position in the flow is wrong.

---

### 18. Does it look like a desktop page squeezed onto a phone? Partly, and it is diagnosable — SHOULD FIX
**Pages:** all eight. **Viewport:** 390x844.
Three specific symptoms, all measured rather than impressionistic:

1. **A load-bearing desktop component is switched off with no substitute.** `aside.spine`, containing
   `nav.index`, computes to `display: none` at 390px. Its inline stand-in (`nav.strip`) is placed where
   it makes sense in a wide two-column layout — beside or after the opening matter — not where a phone
   reader needs it. Nothing was added to the phone to replace the persistent rail: no sticky header,
   no progress indicator, no back-to-top, no in-page index in the menu (the menu contains only the six
   site destinations).
2. **Editorial layers that coexist on a wide screen serialise into scroll.** `/en/explore/`'s three
   nested framings (611px before the first question), `/en/measurement/`'s eight preamble sections
   (2,543px before the agenda), `/en/evidence/compare/`'s duplicated "does not establish" prose. All of
   these are the sort of thing that reads as texture at 1440px and as repetition at 390px.
3. **Touch sizing was solved in the header and not carried down.** Header buttons h=44; body `.actions`
   h=33; body `.open` h=30; `<select>` h=44. The correct value is clearly known.

Against that, three things are genuinely built for the phone and should be said plainly: zero
horizontal overflow on every page and both viewports; a comparison table that truly reflows to a
stacked layout at 320px rather than side-scrolling; and a figure component whose bars stay
zero-based, linear and correctly labelled at 358px. The site is not a naive desktop squeeze. It is a
responsive build with one structural omission (phone wayfinding) and one unapplied rule (tap size).

---

## Verdict

As a phone reader with somewhere to be, I can trust this site and I cannot move around it. Identity is
never in doubt — the CauseWay lockup and "Yemen Financial Inclusion Evidence" sit at the top of every
page, and the foot closes properly with trust links, an attribution sentence, section groups and an
edition line; that foot is deliberate, not dumped. The rendering is disciplined: no page scrolls
horizontally at 390 or 320, the comparison table reflows into a stacked layout instead of
side-scrolling, and the bar figures on `/en/people/` are zero-based, correctly scaled and honest about
which values are derived. `/en/people/` and `/en/evidence/CLM-003/` both give me a qualified number
above the fold, which is the whole promise of the product, delivered.

What fails is closure. These are pages of 8, 13, 15 and 37 phone screens, and the instrument for
traversing them — the `nav.index` spine — is set to `display: none` at phone width with nothing put in
its place. The inline substitute lands at 71% depth on `/en/evidence/compare/`, 36% on `/en/explore/`,
25% on the two home pages, and on `/en/data/` it never indexes the seven groups that actually organise
151 sources. There is no sticky anything on any page, no progress cue, no back-to-top. On `/en/data/`
that means roughly 30,000px of scroll with one search box, 1.6 screens down, behind a placeholder that
asks for a reference code. A phone reader does not abandon this site because it is untrustworthy; they
abandon it because they cannot tell how much is left or get back to where they were.

Two smaller things compound it. The primary body targets — including `.open`, the way into every
evidence record — measure 30–33px against a 44px header button on the same page, so the site knows the
right number and does not use it where it counts; and the co-authoritative Arabic build happens to tap
better than the English one (35–40px) for reasons of line box rather than decision, which means the two
languages are not equally usable. And several pages front-load self-description: the homepage spends
its entire first screen on an eight-line statement of what kind of resource this is before showing a
single figure, `/en/explore/` says "start with a question" three times across 611px before showing one,
and `/en/measurement/` runs eight sections of caveat across three screens before the agenda it is named
after.

Fix phone wayfinding and the 44px rule and this reads as a site built for the phone. Until then it
reads as a careful, honest, well-typeset publication that assumes a reader with a large screen and no
hurry.

---

### Severity counts

- **BLOCKING: 3** — findings 4, 11, 15
- **SHOULD FIX: 8** — findings 2, 3, 8, 13, 14, 16, 17, 18
- **OBSERVATION: 7** — findings 1, 5, 6, 7, 9, 10, 12

Total 18 findings. Four of the seven observations are positive (1, 5, 9, 10) and two more are
positive with a caveat (7, 12).

### Screenshots read (12, all viewport-clipped, no full-page captures)

`01-en-home-first` · `02-en-home-foot` · `03-ar-home-first` · `04-en-explore-first` ·
`05-en-people-first` · `06-en-people-chart` · `07-en-data-first` · `08-en-data-catalogue` ·
`09-en-clm003-first` · `10-en-compare-table` · `11b-compare-table-320` · `12-en-measurement-first`

All lengths, overflow scans, tap-target heights, bar-width ratios, computed styles and duplicate-text
counts in this report were taken from the DOM, not read off the images.
