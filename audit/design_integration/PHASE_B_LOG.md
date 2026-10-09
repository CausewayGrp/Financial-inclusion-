# Design integration V1, Phase B — log

The owner's decisions of 9 October 2026 (`audit/OWNER_DECISIONS_2026-10-09.md`) approved three steward changes for
Phase B, each in its own commit naming the finding it closes: B-a, Home's Orientation tier in
`presentation_priority.json`; B-b, one Master transaction for interface labels only; B-c, the navigation contract. This
folder holds the Master transaction of B-b; the design record is `design/DESIGN_INTEGRATION_V1.md`.

Entry state: `main` at `b323a441` (merge of pull request #15), Master
`fdb24bdfeae5c2604e326dd19effb4d79a783d44272f4dc08da2373979893999`.

## V1B-1 · interface labels (finding V1B-1:B-b)

Script `v1b_1_interface_labels.py`; ledger `runs/V1B-1_MASTER_LEDGER.json`; run report `runs/V1B-1_RUN_REPORT.json`.
Fifteen rows appended to the 04 interface-copy block, English and Arabic together; no existing row, figure, unit,
period, universe, source or record changed.

| ID | English | Arabic | Use |
|---|---|---|---|
| UI-CHRONOLOGY-LIST-SUMMARY | List of dated events | قائمة الأحداث المؤرخة | /finance/: summary of the chronology disclosure |
| UI-DATA-ABOUT-THIS-SOURCE | About this source | عن هذا المصدر | /data/: summary of a source row's description; "Does not establish" stays outside |
| UI-EDITION-CHECKED-DATE | 3 October 2026 | 3 أكتوبر 2026 | the date /corrections/ §3 states for the edition |
| UI-CURRENTNESS-STRIP | Sources checked up to {date} | رُوجعت المصادر حتى {date} | currentness strip, beside the edition label |
| UI-COLOPHON-H | Evidence colophon | بيان الأدلة | colophon heading |
| UI-COLOPHON-SINGLE-MASTER | This edition is generated from a single governed evidence base, … | يُولَّد هذا الإصدار من قاعدة أدلة واحدة … | single-Master statement |
| UI-COLOPHON-EDITION | Edition | الإصدار | label of UI-CONTENT-VERSION |
| UI-COLOPHON-CHECKED | Sources checked up to | رُوجعت المصادر حتى | label of the checked date |
| UI-COLOPHON-FINGERPRINT | Evidence-base fingerprint (SHA-256, abridged) | بصمة قاعدة الأدلة (SHA-256، مختصرة) | label of the Master's short hash |
| UI-COLOPHON-CITATION | Cite this page | الاستشهاد بهذه الصفحة | link to the page's citation tools |
| UI-NAV-HUB-01 … 05 | 01 … 05 | 01 … 05 | hub numerals, bound in the navigation contract |

**Binding of the date.** The Master states the edition's check date once, in `/corrections/` section 3 ("… up to
3 October 2026"), and the edition label carries the same date. Gate CS-01 (`scripts/validate.py`) holds
UI-EDITION-CHECKED-DATE equal to both, in both languages. The date and the edition stay separate values because a
later edition may be released after the day its sources were last checked.

**Not added.** A "next review" label (no review date is governed) and a separator between Home's figure records (not
part of B-b).

## B-c · navigation contract (finding V1-ESC-NAV)

`site-src/content/content/navigation_interaction.json`: new keys `page_tools` (Cite and Report under each h1) and
`hub_numerals` (each hub matched by route to UI-NAV-HUB-0n; validated by the generator, because `global_navigation` is
generated from 04), `mobile_menu` rewritten (five hubs with numerals, the eight domain answers under Explore, trust
links, language, cite), `utilities` given their placement. Gate RC-NAV reads the new keys.

## Built on B-a, B-b and B-c

Currentness strip, Evidence Colophon, the `/finance/` and `/data/` disclosures, search and filter quality. Gates CS-01
and CS-02. Design record: `design/DESIGN_INTEGRATION_V1.md` §6 (DL-V1-013…018), with the re-measured phone screens.
