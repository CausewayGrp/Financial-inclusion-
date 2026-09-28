# D7 cold read — English edition (28 September 2026)

Reader: a fresh agent with no repository or conversation context, briefed to read the built site at
`design/reference/out` (the checkpoint tree, before the Explore fix of DL-D7-003) as a researcher, a regulator and a
journalist, report only material findings, and change nothing. The report is the reader's, verbatim; its adjudication
is in `design/10_ACCEPTANCE_CHECKLIST.md` §K.4. Its scratch evidence (screenshots, text dumps, link check, search and
cite scripts) was not committed.

---

Read-only cold review, English edition, 13 routes + search, 1440/390 px. No repository file written.

FINDINGS

1. BLOCKING · /en/people/ · §02: "the matching figure for adults with more education is not in the evidence base, so no education gap is stated." The figure beneath (VIS-FINDEX-GAPS) plots "Adults with secondary education or more 19.53 · Calculated here … 12.55 percentage points"; the does-not-establish box names only sex and income gaps. The page asserts a number both exists and does not exist. Fix: align prose with the record (four gaps) or withhold the education/age rows.

2. MATERIAL · search (Home) · "remittances" → "10 results shown", no total, no "more"; "Yemen" and "Findex" also return exactly 10. The served index holds 79 remittance entries (CLM-032/036/037/041/042/043 and the Reading "Same year, different number" never surface). "10 results" reads as the whole corpus. Fix: "10 of N shown" plus a link to the Evidence hub with the query.

3. MATERIAL · /en/explore/ · "04 Start with a question — Questions to start from: Use the questions below…" is followed by no questions; next comes "What the evidence cannot yet answer". Inline 04, TOC 05. Visibly unfinished. Fix: remove the section (the list already sits at the top).

4. MATERIAL · /en/ (also /en/providers/, /en/measurement/) · "Another view of the evidence" boxes are text-only, no chart; on Home the box repeats the "System context" section above it and prints "Does not establish:" again as "What not to conclude:". Fix: drop the text-only box where a section already presents the record; print the boundary once.

5. MATERIAL · /en/people/ (VIS-FINDEX-GAPS) · Under the bar chart, the full "Text description of this view" and a complete data table render visibly (figure block 2,433 px at 1440, 3,322 px at 390): nine values appear three times in one figure. The chart alone is labelled correctly; the density buries the boundary text. Fix: collapse description and table in <details>.

6. MATERIAL · /en/evidence/compare/?records=CLM-001,CLM-010 · "01 Analysis — Three measures that cannot be combined" discusses 11.9%, "3.3 million active savers" and FMIIP baselines, not the selected wallet record; identical text appears for CLM-032,CLM-044 and in the error state. Reads as the analysis of the chosen pair. Fix: label "Worked example", above the selector.

7. MATERIAL · /en/evidence/compare/ · Only 13 records are selectable; ?records=CLM-003,… returns "not available for comparison here: CLM-003" with no reason (a Home headline record). Methodology §09 says evidence state gates Compare; Compare never says so. Fix: one sentence on Compare and in the error: "13 of 110 records are comparable because …".

8. MINOR · figure footers · "Full record: /en/evidence/VIS-FINDEX-GAPS/" is a raw path as link text; on the Reading it links to itself. "Cite this page" copies only "Title — site — URL" (no publisher, edition, date) while "Cite this record" is complete; both copy silently, no preview. Fix: "Open record … →", one citation template with preview.

9. MINOR · /en/data/ · one 50,000 px page: 151 source cards each stamped "Reuse terms: not assessed", plus a 24-event chronology under the H1 "Find the original source…". Filter and ?source= deep link work. Fix: chronology to its own page; state the reuse caveat once.

Works: Home fold answers what/why/where/boundaries within 30 s; CLM-044 withholds value and producer everywhere (page, Compare, search index, meta); all 139 internal links resolve; no console errors; no overflow at 390 px.

VERDICTS

Researcher: Any headline number reaches a record, source card and external locator in three clicks. The People contradiction on education stops trust cold. Search's silent cap makes the corpus look a fifth of its size. Why only 13 records compare is unexplained. Record citations usable; page citations not.

Regulator: Scope of authority (CBY-Aden, not national) travels with every count; listing ≠ operation holds throughout. CLM-044 is withheld correctly; the corrections log is honest ("none yet"). Compare's static analysis under a chosen pair invites misreading. Repeated boundary sentences read as boilerplate. Empty Explore section and text-only "views" signal an unfinished build.

Journalist: In 90 s: "11.9% (2022 fieldwork, 23% of population uncovered), women 5.44% vs men 18.35%, POS 561→1,473 within CBY-Aden scope" — quotable and bounded. The Reading chart screenshots safely ("Same year, different publication" is on the image). The People chart screenshots safely, but its page contradicts it. Search misses most remittance records. A page citation carries no date or publisher.
