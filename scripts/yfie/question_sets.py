# -*- coding: utf-8 -*-
"""The R8.4A question sets: which governed questions Home starts from, and how Explore groups all of them.

Open item EAD-11. These are **selection and grouping decisions**, not content: every question, every cluster heading
(a governed `UI-QUESTIONS-*` label) and every destination is governed and read through the content path, never here —
this module holds identifiers and nothing else. What is not yet governed is which four Home starts from and which
cluster each question sits in. EAD-11 moves that into a governed contract — the Master or the presentation contract —
with the selection unchanged. Code may not edit either controlled contract, so the sets are held here, in one named
place, until the steward lands that change; `design/ESCALATIONS.md` carries the exact patch.

They are held here rather than anywhere else for a reason the cutover found. Before EAD-01, Explore's clusters were
recovered by `scripts/handoff_inventory.py` **scraping the baseline renderer's own HTML** (its question-grid and
question-cluster markup) out of the built site, and the accepted renderer then read them back from that
inventory. Removing the baseline renderer therefore emptied the scrape, the inventory recorded four empty clusters and
Explore rendered with no questions at all — a build whose output was an input to itself. The sets now have one source,
this module; the inventory reads them from here, and nothing is recovered from rendered markup.

Values below are exactly those the accepted build published, taken from the committed inventory at `2f9a93c`.
"""
from __future__ import annotations

# Home starts from four of the eleven (R8.4A): Explore holds all of them.
HOME_STARTING_QUESTION_IDS = ["QE-002", "QE-003", "QE-005", "QE-011"]

# Explore's four clusters, in order: the governed heading label, then the questions it holds, in order.
EXPLORE_QUESTION_GROUPS = [
    {"heading_ui_id": "UI-QUESTIONS-UNDERSTAND-THE-WIDER-PICTURE", "question_ids": ["QE-001", "QE-003"]},
    {"heading_ui_id": "UI-QUESTIONS-PEOPLE-USE-AND-FLOWS", "question_ids": ["QE-002", "QE-004", "QE-007", "QE-009"]},
    {"heading_ui_id": "UI-QUESTIONS-FIRMS-INSTITUTIONS-AND-PROVIDERS", "question_ids": ["QE-005", "QE-006", "QE-008"]},
    {"heading_ui_id": "UI-QUESTIONS-VERIFY-AND-DECIDE-WHAT-TO", "question_ids": ["QE-010", "QE-011"]},
]
