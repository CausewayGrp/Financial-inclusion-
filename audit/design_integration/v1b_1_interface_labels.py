# -*- coding: utf-8 -*-
"""Design integration V1, Phase B, transaction V1B-1: interface labels only. English and Arabic together.

  python3 v1b_1_interface_labels.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Owner decisions of 9 October 2026, B-b (audit/OWNER_DECISIONS_2026-10-09.md): "One Master transaction for interface
labels only (no figures, no data): the /finance/ chronology summary label, the /data/ 'About this source' row label (the
'Does not establish' line stays outside it), the currentness-strip label bound to the Master's verification date and
edition, the Evidence Colophon labels, and the numerals 01-05 bound to the five hubs. EN and AR together."

It closes the label escalations of design/ESCALATIONS.md, "Raised at V1 design integration" and "Raised at V1 phase 2"
(NEEDS_CONTROLLED_CONTENT: currentness strip, Evidence Colophon, the hub numerals, the /finance/ chronology summary, the
/data/ source-row summary). Fifteen rows are appended to the 04 interface-copy block; no row is changed, no figure, unit,
period, universe, source or record is touched.

The verification date. The Master states it once, in /corrections/ section 3: "This edition reflects what its sources
showed when they were checked, up to 3 October 2026" («... حتى 3 أكتوبر 2026»), and the edition's own label
(UI-CONTENT-VERSION) is "Edition of 3 October 2026". UI-EDITION-CHECKED-DATE carries that date as the one value the
currentness strip and the colophon print; gate CS-01 (scripts/validate.py) holds it equal to the date in the
/corrections/ sentence and in UI-CONTENT-VERSION in both languages, so the three cannot drift apart. The date and the
edition are kept apart because a later edition may be released after the day its sources were last checked.

The hub numerals. "01" to "05" are labels, not quantities; the navigation contract binds each to its hub by ID
(navigation_interaction.json, global_navigation[].numeral_ui_id), in the order the contract already lists the hubs.

Not added: a "next review" label, because no review date is governed; a separator between Home's figure records, which
the owner did not include in B-b.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, TxError, insert_ui_rows  # noqa: E402

F = "V1B-1:B-b"
RULE = "Design integration V1, owner decisions of 9 October 2026, B-b. "

UI_ROWS = [
    ("UI-CHRONOLOGY-LIST-SUMMARY", "List of dated events", "قائمة الأحداث المؤرخة",
     RULE + "/finance/: the summary of the disclosure that holds the chronology list, followed by the count of events; "
            "distinct from UI-CHRONOLOGY-H, which is the section's heading there. The intro stays outside the disclosure."),
    ("UI-DATA-ABOUT-THIS-SOURCE", "About this source", "عن هذا المصدر",
     RULE + "/data/ source register: the summary of a source row's description. The row's 'Does not establish' line, its "
            "reference, its locator path and its cite controls stay outside the disclosure."),
    ("UI-EDITION-CHECKED-DATE", "3 October 2026", "3 أكتوبر 2026",
     RULE + "The date up to which this edition's sources were checked, as stated in /corrections/ section 3 and in "
            "UI-CONTENT-VERSION; gate CS-01 holds the three equal. Changes only with a governed release."),
    ("UI-CURRENTNESS-STRIP", "Sources checked up to {date}", "رُوجعت المصادر حتى {date}",
     RULE + "Currentness strip on every page; {date} is UI-EDITION-CHECKED-DATE. Printed beside UI-CONTENT-VERSION and "
            "linked to /corrections/ section 3, which says what an edition is."),
    ("UI-COLOPHON-H", "Evidence colophon", "بيان الأدلة",
     RULE + "Heading of the Evidence Colophon in the footer of every page."),
    ("UI-COLOPHON-SINGLE-MASTER",
     "This edition is generated from a single governed evidence base, the one authority for every figure and source it shows.",
     "يُولَّد هذا الإصدار من قاعدة أدلة واحدة خاضعة للحوكمة، هي المرجع الوحيد لكل رقم ومصدر يعرضه.",
     RULE + "Evidence Colophon: the single-Master statement."),
    ("UI-COLOPHON-EDITION", "Edition", "الإصدار",
     RULE + "Evidence Colophon: label of UI-CONTENT-VERSION."),
    ("UI-COLOPHON-CHECKED", "Sources checked up to", "رُوجعت المصادر حتى",
     RULE + "Evidence Colophon: label of UI-EDITION-CHECKED-DATE."),
    ("UI-COLOPHON-FINGERPRINT", "Evidence-base fingerprint (SHA-256, abridged)", "بصمة قاعدة الأدلة (SHA-256، مختصرة)",
     RULE + "Evidence Colophon: label of the first twelve hexadecimal characters of the SHA-256 of the Production Master "
            "the page was built from (authority/AUTHORITY.json production_master.sha256); an identifier, not a quantity."),
    ("UI-COLOPHON-CITATION", "Cite this page", "الاستشهاد بهذه الصفحة",
     RULE + "Evidence Colophon: a link to the page's own citation preview and copy control (section.util), which stays "
            "the one place a citation is copied."),
    ("UI-NAV-HUB-01", "01", "01", RULE + "Numeral of the hub /explore/ (Explore), bound by navigation_interaction.json."),
    ("UI-NAV-HUB-02", "02", "02", RULE + "Numeral of the hub /evidence/ (Evidence), bound by navigation_interaction.json."),
    ("UI-NAV-HUB-03", "03", "03", RULE + "Numeral of the hub /readings/ (Evidence Readings), bound by navigation_interaction.json."),
    ("UI-NAV-HUB-04", "04", "04", RULE + "Numeral of the hub /data/ (Data & sources), bound by navigation_interaction.json."),
    ("UI-NAV-HUB-05", "05", "05", RULE + "Numeral of the hub Method & Measurement (/methodology/, /measurement/), bound by "
                                         "navigation_interaction.json."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    for ui_id, en, ar, _ in UI_ROWS:
        if not en or not ar:
            raise TxError(f"{ui_id}: both languages are required")
        if en.count("{") != ar.count("{"):
            raise TxError(f"{ui_id}: the two languages carry different placeholders")
    insert_ui_rows(s, F, UI_ROWS)
    rep = s.save(out, ledger, OrderedDict([("transaction", "V1B-1"),
                                           ("summary", "Interface labels for design integration V1 Phase B (owner decisions of 9 October 2026, B-b)"),
                                           ("items", OrderedDict([("interface_rows", len(UI_ROWS))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
