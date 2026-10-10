# Rights presentation — log

The owner's brief of 10 October 2026, Part B4: present the rights of this resource to the standard of the World Bank
or Our World in Data, Master-first, English and Arabic together. The rights **decision** was taken on 3 October 2026
and closed on 10 October 2026 (`audit/OWNER_DECISIONS_2026-10-10.md`, OWN-04-R); nothing here decides anything about
it. **No claim of rights clearance, legal review or certification is made anywhere in this work, and none may be
inferred from it.**

## 1. What the pages already said, before this work

`/rights/` already stated the licence correctly, in both languages, in six sections: that CauseWay's own content is
under CC BY 4.0 while other publishers' material stays under their terms; that citation, factual use and
redistribution are three separate permissions; what a rights restriction changes; that the source's own terms remain
authoritative; why source files are linked and not hosted; and, in its sixth section, the licence itself — its scope
(text, analysis, visual designs, the compiled evidence records, and the structure and annotations of the data exports
when they are published), the exclusion of the logo, the three conditions (credit, link to the licence, indicate
changes), the exclusion of third-party material, the two-line attribution, and the plain statement that the page
"does not state that any third-party rights have been cleared". `/terms/` section 3 carries the same substance.

So Part A changed no page text, and this part adds rather than corrects.

## 2. What was verified from the publishers' own pages

| Fact | Result | Where |
|---|---|---|
| The CC BY 4.0 human-readable deed | Resolves; the page itself says it "is not a license and has no legal value" | `https://creativecommons.org/licenses/by/4.0/` |
| The CC BY 4.0 legal code | Resolves; "Attribution 4.0 International", with 33 language links | `https://creativecommons.org/licenses/by/4.0/legalcode` |
| An **official** Arabic translation of the **legal code** | **Exists.** Creative Commons announced it on 23 February 2017 as "the official translation of the Creative Commons 4.0 licenses into Arabic"; its legal-tools translation wiki records Arabic 4.0 as "Final — published February 2017" | `https://creativecommons.org/licenses/by/4.0/legalcode.ar`; `https://creativecommons.org/2017/02/23/arabic-croatian-translations/` |
| Whether that Arabic legal code is the corrected text | **NOT VERIFIED.** Creative Commons' notice of 13 April 2020 says that, after six years of publishing official translations, it found one official translation with "known material errors", hid it, and would publish a corrected version. **The notice does not name the language**, and the current page carries no version marker | `https://creativecommons.org/2020/04/13/update-to-ccs-policy-on-legal-code-corrections/` |
| The canonical machine-readable licence URI | `https://creativecommons.org/licenses/by/4.0/` — the deed's own "Canonical URL", with no language or `legalcode` suffix | the deed page |
| Creative Commons' recommended attribution practice | Title, Author, Source, Licence (TASL), "whether you're sharing the work as-is or if you have made an adaptation"; links to each where possible; title is "a requirement of all CC licenses version 3.0 or earlier, and it is optional for the 4.0 suites"; for an adaptation, keep the original attribution, say it is an adaptation, and add the new work's attribution "so viewers can see what has changed" | `https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution` |
| The licence of the World Bank's **published Findex aggregate indicators** | CC BY 4.0, with the World Bank's additional terms (its own attribution format, and mediation then UNCITRAL arbitration) | `https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS`; `https://datacatalog.worldbank.org/public-licenses`; `https://data.worldbank.org/summary-terms-of-use` |

## 3. The Findex microdata question — ESCALATED

The brief asks: check whether any published figure derives from the World Bank Findex microdata; if so, confirm that
the World Bank Microdata Research License permits publishing it, cite it as that licence requires, say that CC BY does
not extend to the underlying data, and **escalate if in doubt**.

**Published figures do derive from it.** The 95% intervals on `/evidence/CLM-026/` — 18.4% to 24.9% for saving, 47.1%
to 55.5% for borrowing, 7.4% to 11.3% for digital payments — are CauseWay derivations (transaction FC-1) from
`micro_yem.dta` (study `YEM_2022_FINDEX_v01_M`, 334,544 bytes), using the published survey weight and a Hajek variance
estimator. The record already says so publicly, in both languages: "the respondent file was supplied under the World
Bank Microdata Research License, the published survey weight was used, and each measure's weighted estimate reproduces
the World Bank's own published value for Yemen in 2022 … The 95% interval beside each is derived by this resource from
the same weights; the World Bank publishes none." The page-spec locators record that the file is "held under the World
Bank Microdata Research License and never redistributed."

**Whether that licence permits publishing those intervals is not unambiguous, and this session may not decide it.**
The Microdata Library terms, read from `https://microdata.worldbank.org/index.php/terms-of-use` and
`https://datacatalog.worldbank.org/public-licenses`, say:

> "Data and other material provided by the Microdata Library will be used solely by the user, and shall not be
> redistributed or sold to other individuals, institutions or organizations without the Microdata Library's prior
> written agreement …"

> "The data will be used for statistical and scientific research purposes only. They will be used solely for
> generating, and perhaps reporting, aggregated information and not for investigations into specific individuals or
> organizations …"

> "Any books, articles, conference papers, theses, dissertations, reports or other publications employing data
> obtained from the Microdata Library will cite the source, in line with the citation requirement provided with the
> dataset."

> *(Licensed files only)* "The intended use of the data, including a list of expected outputs and the organization's
> dissemination policy must be identified and no different uses shall be permitted without prior written consent from
> the World Bank."

Nothing in that text mentions survey weights, confidence intervals, or the licence of published results, and the
study's own pages — the Yemen file `catalog/5862`, the global study `catalog/4607`, their get-microdata pages, the
study metadata JSON and the Global Findex collection page — **do not state which access category the study falls in**
(the terms distinguish Open Access, Direct Access, Public Use, Licensed, External and no Access, and the Licensed
category carries the extra clause quoted above). So three things are unresolved: whether "perhaps reporting,
aggregated information" covers a published confidence interval; whether the study is a Licensed file whose expected
outputs must be identified in advance; and what the World Bank's view of onward CC BY licensing of a derived statistic
is, on which the terms are silent.

**Escalated to the owner, for counsel** (`design/ESCALATIONS.md`). This session has not withdrawn, changed or
re-derived any figure: the intervals, their method and their provenance statement are exactly as they were. What it
has done is (a) state on `/rights/` that CC BY 4.0 does not extend to the underlying microdata or to figures derived
from it, which is true on any reading of the licence, and (b) record the citation the World Bank requires. The
question of permission is the owner's and counsel's, not the steward's, and **no legal conclusion is stated here**.

The citation requirement the study page carries, recorded so it can be printed verbatim when the owner decides:

> Demirgüç-Kunt, Asli, Leora Klapper, Dorothe Singer, Saniya Ansar. 2022. *The Global Findex Database 2021: Financial
> Inclusion, Digital Payments, and Resilience in the Age of COVID-19.* Washington, DC: World Bank.

Study ID `WLD_2021_FINDEX_v03_M`; DOI `https://doi.org/10.48529/jq97-aj70`. The study's own disclaimer: "The user of
the data acknowledges that the original collector of the data, the authorized distributor of the data, and the
relevant funding agency bear no responsibility for use of the data or for interpretations or inferences based upon
such uses."

## 4. What this part adds

Master-first, English and Arabic together, in transaction PN-2. Nothing here changes a figure, a period, a universe,
a limit or a source.

1. **A licence line in every page's footer.** Text only, no badge image, beside the existing copyright and edition
   line: that CauseWay's own content is under CC BY 4.0 unless otherwise noted, that third-party material stays under
   its owners' terms, and a link to `/rights/`.
2. **`<link rel="license">` in every page's head**, pointing at the canonical licence URI
   `https://creativecommons.org/licenses/by/4.0/` — the deed's own canonical URL, with no language suffix.
3. **`/rights/` states the scope exactly**, as the brief sets it out, with a covered list and a not-covered list:
   - **Covered:** CauseWay's text, analysis, visual designs, compiled records, the structure and annotations of the
     exports, and its annotations.
   - **Not covered:** third-party material; **the CauseWay name, logo and marks**; **the repository's software code**,
     of which the page says only that it is outside this licence and decides nothing about it; and **figures derived
     from the World Bank Findex microdata**, with the statement that CC BY does not extend to the underlying data.
4. **The official deed and the legal code are both linked**, with the English legal code named as the canonical text
   and the official Arabic legal code linked beside it in the Arabic edition. The Arabic legal code is linked as an
   official translation because Creative Commons published it as one; it is not presented as the canonical text,
   because Creative Commons' own canonical URL is the English one and its 2020 corrections notice leaves the current
   Arabic text's status unverifiable (§2).
5. **Attribution follows TASL practice** — title, author, source, licence, plus whether changes were made — inside the
   existing two-line format, which already names this resource, the record, CauseWay, the edition and the page
   address on the first line and the original source's publisher, title, year and link on the second.

What it does **not** do: claim rights clearance, legal review, certification or any permission from the World Bank;
change `licence_text_confirmed` or `public_downloads`, which stay `false`; add a licence file to the repository; or
decide anything about the code licence.

## 5. Transaction PN-2

Script `pn_2_rights_presentation.py`; ledger `runs/PN-2_MASTER_LEDGER.json`; run report `runs/PN-2_RUN_REPORT.json`.
Four cells: two rows appended to the `04_NAV_UX` governed interface-copy block, and `/rights/` section 6 restated in
both languages in `03_PAGE_SECTIONS`. Master `849bc562dc3b…` → `85593e5a4f60…`. No figure, unit, period, universe,
limit, source or record is touched, and nothing is removed from `/rights/`.

### The two governed rows

| UI id | English | Arabic |
|---|---|---|
| UI-FOOTER-LICENCE | Text, analysis and visual designs © 2026 CauseWay, licensed under CC BY 4.0 unless otherwise noted; third-party material remains under its owners' terms. See Rights and reuse. | النصوص والتحليلات والتصاميم المرئية © 2026 CauseWay، وتُتاح بموجب رخصة CC BY 4.0 ما لم يُذكر خلاف ذلك؛ وتبقى مواد الجهات الأخرى خاضعة لشروط أصحابها. انظر صفحة الحقوق وإعادة الاستخدام. |
| UI-RIGHTS-ATTRIBUTION-NOTE | Where you have changed what you reused — recalculated, reformatted, translated, cropped or combined it — say so, so a reader can tell your version from this one. | وإذا غيّرت ما أعدت استخدامه — بإعادة الحساب أو إعادة التنسيق أو الترجمة أو الاقتطاع أو الدمج — فاذكر ذلك، ليتمكن القارئ من التمييز بين نسختك وهذه النسخة. |

### Where they print

- The footer line sits under the existing copyright and edition line, in its own `div.fine.licence`, on every page
  that carries the institutional band. Text only; no badge image.
- `<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">` is in the head of **285 of the 288
  documents**. The three without it are redirects with no licensable content: the root language redirect
  (`dist/index.html`) and the two `NEG-EW-011` stubs that forward to `CLM-015`. The bilingual 404 carries the link
  but not the footer band.
- The URI is the licence deed's own canonical URL, with no language and no `legalcode` suffix, so one URI serves both
  editions.

### Renderer changes, and why they are not "a new feature"

`scripts/yfie/render.py` (the `LICENCE_URI` constant, the head link and the footer line),
`scripts/yfie/families.py` (the 404's head link), `scripts/yfie/content.py` (the shell label) and
`scripts/yfie/theme.py` (the licence line sits under the copyright line without a second rule). Every string printed
is a governed label; the code adds no wording of its own. The brief commissions both the footer line and the
machine-readable link, so this is the rights presentation it asks for rather than a widening of scope.

### Gate PN-G01, and its five negative controls

`scripts/validate.py` asserts that the footer licence line is the governed string for the page's language, that the
machine-readable link carries the canonical URI, and that the line names CC BY 4.0 in both languages — on every
content page, with the three redirects named as the only exclusions. Five controls in
`scripts/tests/test_gate_negative_controls.py` prove the gate fails on its own faults: a page losing the link; the
link pointing at a translation instead of the canonical URL; a page losing the footer line; the footer line dropping
the third-party clause; and the governed line stopping naming the licence. **All five caught.** No existing gate's
logic was changed, and no existing fault string was touched.

### What is unchanged

`licence_text_confirmed` and `public_downloads` stay `false`. The licence decision, its scope and the two-line
attribution format are unchanged in substance. No licence file is added to the repository, and nothing is decided
about the code licence. No rights clearance, legal review or certification is claimed, and the page now says in both
languages that it is not legal advice.
