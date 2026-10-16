#!/usr/bin/env python3
"""Keep the public-path documentation aligned with governed navigation and search.

Run with ``python3 scripts/tests/test_public_path_documentation.py``.  This is a
semantic check: harmless SVG styling changes do not affect it.
"""
from __future__ import annotations

import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def svg_element(root: ET.Element, element_id: str) -> ET.Element:
    for element in root.iter():
        if element.get("id") == element_id:
            return element
    raise AssertionError(f"public-path.svg is missing #{element_id}")


def element_text(element: ET.Element) -> str:
    return " ".join(" ".join(element.itertext()).split()).casefold()


class PublicPathDocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        start = cls.readme.index("## Public path")
        end = cls.readme.index("![Public path]", start)
        cls.public_path = " ".join(cls.readme[start:end].split()).casefold()

        cls.svg = ET.parse(ROOT / "docs/diagrams/public-path.svg").getroot()
        cls.domains_group = svg_element(cls.svg, "explore-domains")
        cls.search_group = svg_element(cls.svg, "search-coverage")

        cls.context = load_json("authority/YFI_CURRENT_PROJECT_CONTEXT.json")
        cls.navigation = load_json("site-src/content/content/navigation_interaction.json")
        cls.interface_copy = {
            row["ui_id"]: row for row in load_json("site-src/content/content/interface_copy.json")
        }
        cls.inventory = {row["key"]: row["value"] for row in load_json(
            "site-src/content/content/public_inventory.json")["counts"]}
        cls.search = load_json("site-src/content/content/search_index.json")
        cls.readings = load_json("site-src/content/content/readings.json")

    def test_all_governed_domains_are_visible_and_identified(self):
        expected_routes = self.context["domain_routes"]
        navigation_routes = [
            row["route"] for row in self.navigation["routes"]
            if row.get("page_family") == "Domain Answer"
        ]
        self.assertCountEqual(navigation_routes, expected_routes)
        self.assertEqual(
            self.domains_group.get("data-domain-routes", "").split(),
            expected_routes,
        )

        svg_text = element_text(self.domains_group)
        for route in expected_routes:
            ui_id = f"UI-LAND-DOM-{route.strip('/').upper()}"
            label = self.interface_copy[ui_id]["label_en"].casefold()
            with self.subTest(route=route):
                self.assertIn(label, svg_text)
                self.assertIn(label, self.public_path)

    def test_search_families_are_derived_and_described(self):
        actual_types = {row["type"] for row in self.search}
        documented_types = set(self.search_group.get("data-search-types", "").split())
        self.assertEqual(documented_types, actual_types)

        phrases = {
            "page": "pages",
            "question": "questions",
            "evidence": "evidence records",
            "reading": "readings",
            "measurement": "measurement priorities",
            "source": "source records",
            "source_locator": "source locators",
            "chronology": "dated chronology events",
        }
        self.assertEqual(set(phrases), actual_types, "map any new governed search family explicitly")
        svg_text = element_text(self.search_group)
        for family, phrase in phrases.items():
            with self.subTest(family=family):
                self.assertIn(phrase, svg_text)
                self.assertIn(phrase, self.public_path)

        for document, text in (("README", self.public_path), ("SVG", svg_text)):
            with self.subTest(document=document):
                self.assertIn("does not validate", text)
                self.assertNotIn("not a search family", text)
                self.assertNotIn("chronology stays on the pages", text)

    def test_dated_events_are_searchable_deep_links(self):
        chronology = [row for row in self.search if row["type"] == "chronology"]
        governed = [
            row for row in load_json("site-src/content/visuals/system_chronology.json")
            if row.get("event_class") != "SYSTEM_INTERPRETATION"
        ]
        self.assertEqual(len(chronology), self.inventory["chronology_events"])
        self.assertEqual({row["id"] for row in chronology}, {row["event_id"] for row in governed})
        for row in chronology:
            self.assertEqual(row["route"], f"/finance/#{row['id']}")

    def test_readings_count_and_destinations_match_inventory(self):
        readings = [row for row in self.search if row["type"] == "reading"]
        self.assertEqual(len(readings), self.inventory["readings"])
        actual = {(row["id"], row["route"]) for row in readings}
        expected = {(row["reading_id"], row["route"]) for row in self.readings}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(readings), "Reading search destinations must be unique")

    def test_svg_has_accessible_name_and_description(self):
        self.assertEqual(self.svg.get("role"), "img")
        labelled_by = self.svg.get("aria-labelledby", "").split()
        self.assertEqual(labelled_by, ["t", "d"])
        self.assertTrue(element_text(svg_element(self.svg, "t")))
        description = element_text(svg_element(self.svg, "d"))
        self.assertIn("understand", description)
        self.assertIn("explore", description)
        self.assertIn("verify", description)


if __name__ == "__main__":
    unittest.main(verbosity=2)
