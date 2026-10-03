# -*- coding: utf-8 -*-
"""Governed content loader for the Design reference implementation.

Everything public that a page shows is read here from `site-src/content/**` (the Master's projections and the two
controlled contracts) and from the governed interface copy. Nothing is authored: no label, number, date, title, source
name or sentence of controlled meaning originates in this file. The content rules that the baseline renderer applies
(public-locator filter, lineage statements, boundary parts, citation assembly, date words) are re-implemented here as
rules, not as copied text, so the reference implementation renders the same truth as `dist/` from the same projections.

The loader is deliberately presentation-free: it returns dictionaries and lists; it makes no decision about order of
display beyond what a contract states (presentation_priority tiers, Page Spec section order, reading section order).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[2]
# B5 (release candidate): the governed document types grouped on /data/ as "Rules, decisions and official lists"
DECISION_SPLIT = re.compile(r"(?<=[.?؟]),")   # B6: decisions_unlocked items end a sentence, then a comma
REGULATORY_LABELS = ("Enforcement decision", "Circular or instruction", "Regulatory decision", "Regulation", "Official list or roster")
CONTENT = ROOT / "site-src" / "content"

LANGS = ("en", "ar")
MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
}


def _load(rel: str):
    return json.loads((CONTENT / rel).read_text(encoding="utf-8"))


def _facet_key(value) -> str:
    """RC-12 (B13): a language-neutral filter key for a governed English value ("none" when it is not recorded)."""
    k = re.sub(r"[^a-z0-9]+", "-", str(value or "").lower()).strip("-")
    return k or "none"


# RC-17 (Owner Addendum 2, improvement 5): preset comparisons a reader can run, each set of records chosen by the owner's
# addendum and offered only where every record is in the Compare set; the link label is governed (UI-COMPARE-PRESET)
COMPARE_PRESETS = {"/remittances/": ["CLM-032", "CLM-037", "CLM-041"],
                   "/evidence/compare/": ["CLM-001", "CLM-054", "FMIIP-BASELINE-2025-01"]}


class Content:
    """One loaded view of the governed projections."""

    def __init__(self) -> None:
        self.specs = _load("page_specs.json")["page_specs"]
        self.spec_by_route = {s["route"]: s for s in self.specs}
        self.ui = {r["ui_id"]: r for r in _load("content/interface_copy.json")}
        self.nav = _load("content/navigation_interaction.json")
        self.presentation = _load("presentation_priority.json")
        self.questions = _load("content/questions.json")
        self.readings = _load("content/readings.json")
        self.reading_sections = _load("content/reading_sections.json")
        self.evidence_objects = {o["object_id"]: o for o in _load("evidence/evidence_objects.json")}
        self.sources = {s["source_id"]: s for s in _load("sources/source_reference_map.json")}
        self.closure = {(c["object_type"], c["object_id"]): c for c in _load("sources/public_object_source_closure.json")}
        self.visual_contracts = {v["visual_id"]: v for v in _load("visuals/visual_design_contracts.json")["visuals"]}
        self.grammar_labels = _load("visuals/visual_design_contracts.json")["grammar_labels"]
        # A3 / C3 (owner decision, 2 October 2026): on the page, a figure's text alternative is its governed accessible
        # summary, which ends before the boundary; the full alt text (summary · label · inference) is for detached frames
        self.accessible_summary = {v["visual_id"]: v for v in _load("visuals/visual_library.json")}
        self.relationships = _load("visuals/system_relationships.json")
        self.inventory = {c["key"]: int(c["value"]) for c in _load("content/public_inventory.json")["counts"]}
        # Detail routes: every evidence-detail Page Spec, keyed by the object it renders (navigation only).
        self.detail_routes: dict[str, str] = {}
        for s in self.specs:
            if s.get("page_class") != "evidence_detail":
                continue
            for x in (s.get("governed_claims") or []) + (s.get("governed_evidence_objects") or []) + (s.get("governed_visual_contracts") or []):
                oid = x.get("claim_id") or x.get("evidence_object_id") or x.get("object_id") or x.get("visual_id")
                if oid:
                    self.detail_routes[str(oid)] = s["route"]
        self.question_by_route = {self._route(q.get("primary_route")): q for q in self.questions}
        cmp_spec = self.spec_by_route.get("/evidence/compare/") or {}
        self.compare_ids = {str(x.get("evidence_object_id") or x.get("object_id") or x.get("claim_id") or "")
                            for x in (cmp_spec.get("governed_evidence_objects") or []) + (cmp_spec.get("governed_claims") or [])} - {""}
        self.public_source_ids = {sid for sid, r in self.sources.items()
                                  if r.get("metadata_state") == "DISPLAY_READY" or self.public_locator(r.get("primary_url"))}
        self.nav_labels: dict[str, dict[str, str]] = {}
        for item in self.nav.get("global_navigation", []):
            for x in ([item] if item.get("route") else []) + list(item.get("children") or []):
                self.nav_labels[str(x.get("route"))] = {"en": x.get("label_en"), "ar": x.get("label_ar")}
        for item in self.nav.get("trust_navigation", []):
            self.nav_labels[str(item.get("route"))] = {"en": item.get("label_en"), "ar": item.get("label_ar")}
        for group in self.nav.get("footer_groups", []):
            for item in group.get("links", []):
                self.nav_labels.setdefault(str(item.get("route")), {"en": item.get("label_en"), "ar": item.get("label_ar")})
        # D2: the page family of every route (navigation contract), the domain presentation contracts, and the public
        # sources each Evidence Record depends on (for "Evidence records using this source" on /data/).
        self.family_by_route = {str(r.get("route")): r.get("page_family") for r in self.nav.get("routes", [])}
        self.presentation_routes = {str(e.get("route")): e for e in self.presentation.get("routes", []) if e.get("page_family") == "Domain Answer"}
        self.measurement_agenda = _load("content/measurement_agenda.json")
        self.chronology_events = _load("visuals/system_chronology.json")
        self.source_dependents: dict[str, list] = {}
        for s in self.specs:
            if s.get("page_class") != "evidence_detail":
                continue
            obj = (s.get("governed_evidence_objects") or [{}])[0]
            oid = str(obj.get("object_id") or "")
            for ref in s.get("source_references") or []:
                sid = str(ref.get("source_id") or "").strip()
                if oid and sid and sid in self.public_source_ids:
                    self.source_dependents.setdefault(sid, []).append({"route": s["route"], "id": oid, "title_en": self.loc(obj, "title", "en") or oid, "title_ar": self.loc(obj, "title", "ar") or oid,
                                                                      "public_routes": [str(r) for r in obj.get("public_routes") or []]})
        # RC-12 (B13 b): the Evidence Readings whose governed source closure includes a source, for its backlinks on /data/
        self.source_readings: dict[str, list] = {}
        for s in self.specs:
            rt = str(s.get("route") or "")
            if not rt.startswith("/readings/") or rt == "/readings/" or not s.get("governed_readings"):
                continue
            rd = s["governed_readings"][0]
            for ref in s.get("source_references") or []:
                sid = str(ref.get("source_id") or "").strip()
                if sid in self.public_source_ids and not any(x["route"] == rt for x in self.source_readings.get(sid, [])):
                    self.source_readings.setdefault(sid, []).append({"route": rt, "title_en": rd.get("title_en") or rt, "title_ar": rd.get("title_ar") or rt})
        # Home's starting questions and Explore's four clusters: the R8.4A selection and grouping, read from the
        # presentation contract (EAD-11, landed in the release candidate), which the generator validates.
        qsets = {str(e.get("route")): e for e in self.presentation.get("question_sets") or []}
        self.home_question_ids = list(qsets["/"]["starting_question_ids"])
        self.question_groups = [dict(g) for g in qsets["/explore/"]["question_groups"]]

    # ------------------------------------------------------------------------------------------------ primitives
    @staticmethod
    def _route(r) -> str:
        r = str(r or "").strip("/")
        return "/" + r + "/" if r else "/"

    @staticmethod
    def public_locator(v) -> str:
        v = str(v or "").strip()
        return v if v.lower().startswith(("http://", "https://")) else ""

    def t(self, ui_id: str, lang: str) -> str:
        row = self.ui.get(ui_id)
        if not row:
            raise KeyError(f"governed interface copy missing: {ui_id}")
        return row.get(f"label_{lang}") or ""

    def tf(self, ui_id: str, lang: str, **values) -> str:
        s = self.t(ui_id, lang)
        if set(re.findall(r"\{(\w+)\}", s)) != set(values):
            raise ValueError(f"{ui_id} {lang}: placeholders differ from {sorted(values)}")
        return s.format(**values)

    def ui_json(self, lang: str) -> dict:
        return {k: (r.get(f"label_{lang}") or "") for k, r in sorted(self.ui.items()) if k.startswith("UI-JS-")}

    @staticmethod
    def loc(o: dict, key: str, lang: str) -> str:
        return (o or {}).get(f"{key}_{lang}") or (o or {}).get(key) or ""

    def date_words(self, value, lang: str) -> str:
        v = str(value or "").strip()
        m = re.fullmatch(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", v)
        if not m:
            return v
        y, mo, d = m.groups()
        if not mo:
            return y
        name = MONTHS[lang][int(mo) - 1]
        return f"{int(d)} {name} {y}" if d else f"{name} {y}"

    def href(self, route: str, lang: str) -> str:
        clean = str(route or "/").strip("/")
        return f"/{lang}/" + (clean + "/" if clean else "")

    def nav_label(self, route: str, lang: str) -> str:
        pair = self.nav_labels.get(str(route))
        if pair:
            return pair[lang] or ""
        spec = self.spec_by_route.get(str(route)) or {}
        return self.loc(spec, "title", lang) or str(route)

    def question_label(self, route: str, lang: str) -> str:
        q = self.question_by_route.get(route)
        if q:
            return self.loc(q, "question", lang)
        return self.loc(self.spec_by_route.get(route) or {}, "title", lang)

    # ------------------------------------------------------------------------------------------------ shell
    def shell(self, lang: str, route: str) -> dict:
        other = "en" if lang == "ar" else "ar"
        nav = []
        for item in self.nav.get("global_navigation", []):
            kids = item.get("children") or []
            entry = {"label": item.get(f"label_{lang}"), "route": item.get("route"), "children": [
                {"label": k.get(f"label_{lang}"), "route": k.get("route"), "href": self.href(k.get("route"), lang),
                 "active": self._active(k.get("route"), route)} for k in kids]}
            if item.get("route"):
                entry["href"] = self.href(item.get("route"), lang)
                entry["active"] = self._active(item.get("route"), route)
            nav.append(entry)
        trust = [{"label": t.get(f"label_{lang}"), "href": self.href(t.get("route"), lang), "active": self._active(t.get("route"), route)}
                 for t in self.nav.get("trust_navigation", [])]
        footer = [{"label": g.get(f"label_{lang}"), "links": [{"label": l.get(f"label_{lang}"), "href": self.href(l.get("route"), lang)}
                                                              for l in g.get("links", [])]} for g in self.nav.get("footer_groups", [])]
        return {
            "lang": lang, "dir": "rtl" if lang == "ar" else "ltr", "other_lang": other,
            "product": self.t("UI-PRODUCT-NAME", lang), "edition": self.t("UI-CONTENT-VERSION", lang),
            # B9: the governed citation line of a page that is not an Evidence Record (UI-CITE-PAGE-LINE)
            "cite_page_line": self.tf("UI-CITE-PAGE-LINE", lang, product=self.t("UI-PRODUCT-NAME", lang), version=self.t("UI-CONTENT-VERSION", lang)),
            "labels": {
                "skip": self.t("UI-HEADER-SKIP-TO-CONTENT", lang), "primary_nav": self.t("UI-HEADER-PRIMARY-NAVIGATION", lang),
                "trust_nav": self.t("UI-HEADER-TRUST-LINKS", lang), "menu": self.t("UI-HEADER-MENU", lang),
                "search": self.t("UI-SEARCH-SEARCH", lang), "search_title": self.t("UI-SEARCH-SEARCH-THE-PUBLIC-EVIDENCE", lang),
                "search_placeholder": self.t("UI-SEARCH-SEARCH-QUESTIONS-EVIDENCE-READINGS-AND", lang),
                "search_status": self.t("UI-SEARCH-SEARCH-STATUS", lang), "search_close": self.t("UI-SEARCH-CLOSE", lang),
                "new_tab": self.t("UI-EXTERNAL-NEW-TAB", lang),   # release candidate G4 (D5): the visually hidden new-tab cue
                "cite": self.t("UI-HEADER-CITE-THIS-PAGE", lang), "report": self.t("UI-HEADER-REPORT-AN-ISSUE", lang),
                # B9 (release candidate): the visible citation preview, its copy action and the print control
                "cite_preview": self.t("UI-CITATION-PREVIEW", lang), "copy_citation": self.t("UI-JS-COPY-CITATION", lang),
                "print": self.t("UI-PRINT-THIS-PAGE", lang), "current_record": self.t("UI-JS-CURRENT-RECORD", lang),
                # RC-15 (B15 d, C-2; OWN-04): the short citation is copied by default; the long form stays beside it
                "cite_long": self.t("UI-CITE-LONG-FORM", lang), "copy_long": self.t("UI-JS-COPY-LONG-CITATION", lang),
                "share_record": self.t("UI-JS-SHARE-RECORD", lang),   # RC-15 (B15 e, U1)
                "copied": self.t("UI-HEADER-COPIED", lang),
                "lang_switch_name": self.t("UI-LANG-SWITCH-NAME", other), "lang_switch_action": self.t("UI-LANG-SWITCH-ACTION", other),
                "footer_strapline": self.t("UI-FOOTER-STRAPLINE", lang), "footer_rights": self.t("UI-FOOTER-PUBLISHED-EVIDENCE-REMAINS-ATTRIBUTED-TO", lang),
                "footer_nav": self.t("UI-FOOTER-PRODUCT-AND-TRUST-LINKS", lang), "noscript": self.t("UI-NOSCRIPT-NOTE", lang),
                "breadcrumb": self.t("UI-CRUMB-BREADCRUMB", lang), "understand_explore_verify": self.t("UI-DOM-UNDERSTAND-EXPLORE-VERIFY", lang),
            },
            "nav": nav, "trust": trust, "footer": footer, "home_href": self.href("/", lang), "contact_href": self.href("/contact/", lang),
            "ui_json": self.ui_json(lang),
            "mobile_menu": self.nav.get("mobile_menu") or None,   # owner decisions of 3 October 2026, point 3
        }

    @staticmethod
    def _active(target, route) -> bool:
        key = str(target or "/").strip("/").split("/", 1)[0]
        return bool(key) and str(route).startswith("/" + key)

    def breadcrumb(self, family: str, lang: str, current: str) -> dict | None:
        cfg = (self.nav.get("breadcrumbs") or {}).get(family)
        if not cfg:
            return None
        return {"parent_label": cfg.get(f"parent_label_{lang}"), "parent_href": self.href(cfg["parent_route"], lang),
                "current": current, "mode": cfg.get("current_label_mode")}

    # ------------------------------------------------------------------------------------------------ sections
    def sections(self, spec: dict, lang: str) -> list[dict]:
        """Localized sections in numeric order; split-language rows are merged by section_order (brief §2)."""
        rows: dict[int, dict] = {}
        for s in spec.get("sections", []):
            if not (s.get(f"heading_{lang}") or s.get(f"body_{lang}")):
                continue
            rows.setdefault(int(s["section_order"]), {"order": int(s["section_order"]), "role": s.get("section_role"),
                                                     "heading": s.get(f"heading_{lang}") or "", "body": s.get(f"body_{lang}") or "",
                                                     "paragraphs": [p.strip() for p in str(s.get(f"body_{lang}") or "").split("\n") if p.strip()]})
        return [rows[k] for k in sorted(rows)]

    # ------------------------------------------------------------------------------------------------ sources
    def source_card(self, sid: str, lang: str) -> dict | None:
        """A public source: title, publisher line, locator, data-page link. Locator-less sources return None (never named)."""
        s = self.sources.get(sid)
        if not s:
            return None
        url = self.public_locator(s.get("primary_url"))
        if sid not in self.public_source_ids or not url:
            return None
        ar = lang == "ar"
        display_ready = s.get("metadata_state") == "DISPLAY_READY"
        title = ((s.get("display_title_ar") if ar else s.get("display_title")) or "") if display_ready else ""
        publisher = ((s.get("publisher_ar") if ar else None) or s.get("publisher") or "") if display_ready else ""
        kind = ((s.get("document_label_ar") if ar else s.get("document_label")) or "") if display_ready else ""
        date = self.date_words(s.get("document_date"), lang) if display_ready else ""
        return {
            "id": sid, "url": url, "display_ready": display_ready, "title": title,
            "untitled_label": self.t("UI-SOURCE-UNTITLED", lang), "reference_label": self.t("UI-SOURCE-REFERENCE", lang),
            "publisher": publisher, "kind": kind, "date": date,
            "kind_line": " · ".join(x for x in [publisher, kind, date] if x),
            "data_href": f"/{lang}/data/?source={quote(sid)}#source-{quote(sid)}",
            "cite_payload": " · ".join(x for x in [title, sid, url] if x),
            "rights_note": self.t("UI-EVID-THIS-SOURCE-RECORD-DOES-NOT", lang) if s.get("rights_display_state") == "OBJECT_LEVEL_OR_UNSPECIFIED" else "",
            "labels": {"open_source_record": self.t("UI-EVID-OPEN-SOURCE-RECORD", lang),
                       # RC-12 (B13 d): a locator that is an archived copy says so
                       "open_original": self.t("UI-EVID-OPEN-ARCHIVED-COPY" if urlparse(url).netloc == "web.archive.org" else "UI-EVID-OPEN-ORIGINAL-SOURCE", lang),
                       "copy_reference": self.t("UI-EVID-COPY-SOURCE-REFERENCE", lang)},
        }

    def lineage_statement_id(self, closure: dict) -> str | None:
        return {"PARTIALLY_RESOLVED": "UI-VERIFY-PARTIAL", "COMPOSITE_OF_OBJECTS": "UI-VERIFY-COMPOSITE",
                "COMPOSITE_MEMBERS_NOT_LISTED": "UI-VERIFY-COMPOSITE-UNLISTED", "SOURCE_NOT_YET_BOUND": "UI-EVID-UNBOUND",
                "FRAMING_NO_FACT": "UI-EVID-FRAMING"}.get(closure.get("closure_state"))

    def boundary_parts(self, obj: dict, lang: str) -> tuple[str, str]:
        a = self.loc(obj, "does_not_establish", lang)
        b = obj.get(f"measurement_limitation_{lang}") or ""
        if not a:
            raw = self.loc(obj, "limitations", lang)
            a, b = (raw.split(" | ", 1) + [""])[:2] if " | " in raw else (raw, "")
        return a.strip(), b.strip()

    # ------------------------------------------------------------------------------------------------ evidence record
    def citation(self, spec: dict, obj: dict, lang: str) -> str:
        oid = str(obj.get("object_id") or "")
        title = (self.loc(obj, "title", lang) or self.loc(spec, "title", lang) or oid).strip().rstrip(".")
        closure = self.closure.get(("evidence_object", oid)) or {}
        bound = closure.get("closure_state") in ("CLOSED_TO_SOURCE_ID", "PARTIALLY_RESOLVED")
        own = set(closure.get("resolved_source_ids") or [])
        ar = lang == "ar"
        names = []
        if bound:
            for ref in spec.get("source_references") or []:
                sid = str(ref.get("source_id") or "").strip()
                if sid not in own:
                    continue
                card = self.source_card(sid, lang)
                if not card:
                    continue
                s0 = self.sources.get(sid) or {}
                pub = (s0.get("publisher_ar") if ar else None) or s0.get("publisher") or ""
                ref_txt = f"{pub}؛ {sid}" if ar and pub else (f"{pub}; {sid}" if pub else sid)
                names.append(f"{card['title']} ({ref_txt})" if card["title"] else self.tf("UI-CITE-SOURCE-REFERENCE", lang, sid=sid))

        def clause(label, value):
            v = str(value or "").strip().rstrip(".").rstrip("؛").strip()
            return f"{label}: {v}." if v else ""

        limitation, measure_limit = self.boundary_parts(obj, lang)
        parts = [title if title.endswith(("?", "؟", "!")) else f"{title}.",   # B9 review: never "?." after a question title
                 self.tf("UI-CITE-RECORD-LINE", lang, product=self.t("UI-PRODUCT-NAME", lang), oid=oid, version=self.t("UI-CONTENT-VERSION", lang)),
                 clause(self.t("UI-CITE-PERIOD", lang), self.loc(obj, "period", lang)),
                 clause(self.t("UI-CITE-POPULATION", lang), self.loc(obj, "universe", lang)),
                 clause(self.t("UI-DOM-WHAT-NOT-TO-CONCLUDE", lang), limitation),
                 clause(self.t("UI-EVID-MEASUREMENT-LIMITS", lang), measure_limit),
                 clause(self.t("UI-CITE-ORIGINAL-SOURCES", lang), ("؛ " if ar else "; ").join(names)),
                 self.t("UI-CITE-PUBLISHERS-AUTHORITATIVE", lang)]
        return " ".join(p for p in parts if p)

    def compare_preset(self, route: str, lang: str) -> dict | None:
        """RC-17 (Owner Addendum 2, improvement 5): a preset comparison link, offered only when every record is in the
        Compare set."""
        ids = COMPARE_PRESETS.get(route) or []
        if not ids or not all(x in self.compare_ids for x in ids):
            return None
        label = "UI-COMPARE-PRESET-REMITTANCES" if route == "/remittances/" else "UI-COMPARE-PRESET"   # the cards there do not show all three
        return {"href": f"/{lang}/evidence/compare/?records={','.join(ids)}", "label": self.t(label, lang)}

    def short_citation(self, spec: dict, obj: dict, lang: str) -> str:
        """RC-15 (B15 d, C-2; OWN-04): the short citation the launch uses — the governed title, the record line (record
        ID, CauseWay, edition) and each original source as publisher, title, year and public locator. The long form
        (citation()) keeps the period, population and limits beside it."""
        oid = str(obj.get("object_id") or "")
        title = (self.loc(obj, "title", lang) or self.loc(spec, "title", lang) or oid).strip().rstrip(".")
        closure = self.closure.get(("evidence_object", oid)) or {}
        own = set(closure.get("resolved_source_ids") or []) if closure.get("closure_state") in ("CLOSED_TO_SOURCE_ID", "PARTIALLY_RESOLVED") else set()
        ar = lang == "ar"
        names = []
        for ref in spec.get("source_references") or []:
            sid = str(ref.get("source_id") or "").strip()
            card = self.source_card(sid, lang) if sid in own else None
            if not card:
                continue
            s0 = self.sources.get(sid) or {}
            pub = ((s0.get("publisher_ar") if ar else None) or s0.get("publisher") or "") if card["title"] else ""
            name = card["title"] or self.tf("UI-CITE-SOURCE-REFERENCE", lang, sid=sid)
            # RC-16 (Owner Addendum 2, lessons): publisher, title, year, locator — the governed document year, unless the
            # title already carries it
            yr = str(s0.get("document_date") or "")[:4] if card["title"] else ""
            yr = yr if yr.isdigit() and yr not in name else ""
            names.append(("، " if ar else ", ").join(x for x in (pub, name, yr, card["url"]) if x))
        parts = [title if title.endswith(("?", "؟", "!")) else f"{title}.",
                 self.tf("UI-CITE-RECORD-LINE", lang, product=self.t("UI-PRODUCT-NAME", lang), oid=oid, version=self.t("UI-CONTENT-VERSION", lang))]
        if names:
            parts.append(f'{self.t("UI-CITE-ORIGINAL-SOURCES", lang)}: {("؛ " if ar else "; ").join(names)}.')
        return " ".join(parts)

    def share_text(self, spec: dict, obj: dict, lang: str) -> str:
        """RC-15 (B15 e, U1): what "Share this record" sends — the governed title, period, population and what not to
        conclude, each verbatim and never cut, one per line; the runtime adds the record's link."""
        oid = str(obj.get("object_id") or "")
        title = (self.loc(obj, "title", lang) or self.loc(spec, "title", lang) or oid).strip()
        limitation, _ = self.boundary_parts(obj, lang)
        lines = [title] + [f"{self.t(k, lang)}: {v.strip()}" for k, v in (("UI-CITE-PERIOD", self.loc(obj, "period", lang)),
                                                                        ("UI-CITE-POPULATION", self.loc(obj, "universe", lang)),
                                                                        ("UI-DOM-WHAT-NOT-TO-CONCLUDE", limitation)) if v and v.strip()]
        return "\n".join(lines)

    def series_links(self, obj: dict, sid: str, main_url: str) -> list[str]:
        """RC-15 (B15 d, C-1): the indicator series a record names for one source (its 06 source links, a locator whose
        path is /indicator/<code>) that differ from the source's main locator — only those the source library registers
        for that source (primary or additional). Any other extra locator (an earlier file of a list, say) is not a series
        and is not shown here."""
        s0 = self.sources.get(sid) or {}
        extra = s0.get("additional_urls") or []
        if isinstance(extra, str):
            try:
                extra = json.loads(extra)
            except ValueError:
                extra = [x.strip() for x in extra.split(";")]
        registered = {str(s0.get("primary_url") or "")} | {str(x) for x in extra}
        out = []
        for link in obj.get("source_links") or []:
            url = str(link.get("url") or "") if isinstance(link, dict) else ""
            if (isinstance(link, dict) and link.get("source_id") == sid and url and url != main_url and url in registered
                    and self.public_locator(url) and "/indicator/" in urlparse(url).path and url not in out):
                out.append(url)
        return out

    def evidence_record(self, route: str, lang: str) -> dict:
        spec = self.spec_by_route[route]
        obj = (spec.get("governed_evidence_objects") or [{}])[0]
        oid = str(obj.get("object_id") or "")
        contract = (self.presentation.get("family_contracts") or {}).get("Evidence Record") or {}
        closure = self.closure.get(("evidence_object", oid)) or {}
        limitation, measure_limit = self.boundary_parts(obj, lang)
        sources, suppressed = [], 0
        for ref in spec.get("source_references") or []:
            sid = str(ref.get("source_id") or "").strip()
            card = self.source_card(sid, lang) if sid else None
            if card:
                card["series"] = self.series_links(self.evidence_objects.get(oid) or obj, sid, card["url"])
                card["labels"]["series_used"] = self.t("UI-EVID-SERIES-USED", lang)
                sources.append(card)
            elif sid:
                suppressed += 1
        bound_ids = [str(x) for x in (closure.get("resolved_source_ids") or [])]
        no_locator = [sid for sid in bound_ids if not self.public_locator((self.sources.get(sid) or {}).get("primary_url"))]
        statement_id = self.lineage_statement_id(closure)
        members = []
        for m in closure.get("resolved_via_object_ids") or []:
            if m in self.detail_routes:
                ms = self.spec_by_route.get(self.detail_routes[m]) or {}
                members.append({"id": m, "title": self.loc(ms, "title", lang) or m, "href": self.href(self.detail_routes[m], lang)})
        used_in = [{"title": self.loc(x, "title", lang), "href": self.href(x.get("route"), lang)} for x in spec.get("used_in_readings") or []]
        routes_back = []
        for r in obj.get("public_route_list") or []:
            r = self._route(r)
            if r.startswith("/evidence/"):
                continue
            routes_back.append({"label": self.question_label(r, lang), "href": self.href(r, lang)})
        secs = self.sections(spec, lang)
        lead = (secs[0]["body"] if secs and not secs[0]["heading"] else "")
        summary = self.loc(obj, "summary", lang)
        guidance = next((s for s in secs if s["order"] == 2), None)
        L = lambda k: self.t(k, lang)  # noqa: E731
        verification = self.loc(obj, "verification", lang)
        if statement_id and verification == self.t(statement_id, lang):
            verification = ""  # already shown as the lineage statement
        return {
            "family": "Evidence Record", "route": route, "lang": lang, "id": oid,
            "title": self.loc(obj, "title", lang) or self.loc(spec, "title", lang) or oid,
            "meta_description": self.loc(spec, "meta_description", lang),
            "breadcrumb": self.breadcrumb("Evidence Record", lang, oid),
            "summary": summary, "lead": "" if " ".join(lead.split()) == " ".join(summary.split()) else lead,
            "definition": self.loc(obj, "definition", lang), "universe": self.loc(obj, "universe", lang),
            "period": self.loc(obj, "period", lang), "currentness": self.loc(obj, "currentness", lang),
            "does_not_establish": limitation, "measurement_limits": measure_limit,
            # B1 (owner decision A4 / C6 revised, 2 October 2026): every record prints its governed method text, the 13
            # NO_GOVERNED_CONTRACT__TABLE_ONLY records included
            "method": self.loc(obj, "method", lang),
            "change_trigger": self.loc(obj, "change_trigger", lang), "verification": verification,
            "reading_guidance": guidance,
            "contract": {k: contract.get(k) for k in ("primary", "supporting", "progressive", "utility", "mobile_priority", "always_visible_boundaries", "first_load_exclusions")},
            "sources": sources, "suppressed_sources": suppressed,
            "sources_without_locator_note": L("UI-EVID-SOURCES-WITHOUT-LOCATOR") if (sources and no_locator) else "",
            "lineage_statement": L(statement_id) if statement_id else "", "closure_state": closure.get("closure_state"),
            "members": members, "members_heading": L("UI-EVID-MEMBERS-HEADING"),
            "no_source_message": (L("UI-EVID-NO-STANDALONE-PUBLIC-LOCATOR-IS") if suppressed else L("UI-EVID-THIS-RECORD-CURRENTLY-HAS-NO")) if not (sources or statement_id or members) else "",
            "trace_ids": [sid for sid in bound_ids if self.source_card(sid, lang)],
            "used_in_readings": used_in, "routes_back": routes_back,
            "citation": self.citation(spec, obj, lang), "citation_short": self.short_citation(spec, obj, lang),
            "share_text": self.share_text(spec, obj, lang),
            "compare_href": f"/{lang}/evidence/compare/?records={quote(oid)}" if oid in self.compare_ids else "",
            "visual": self.visual(oid, lang) if oid in self.visual_contracts else None,   # a VIS- record is its visual's canonical route (brief §12)
            "hrefs": {"evidence": self.href("/evidence/", lang), "data": self.href("/data/", lang), "methodology": self.href("/methodology/", lang),
                      "rights": self.href("/rights/", lang), "corrections": f"/{lang}/corrections/?record={quote(oid)}",
                      "report": f"/{lang}/contact/?record={quote(oid)}"},
            "labels": {
                "family": L("UI-EVID-EVIDENCE-RECORD"), "establishes": L("UI-EVID-WHAT-DOES-THIS-EVIDENCE-ESTABLISH"), "scope": L("UI-DOM-SCOPE-AND-TIME"),
                "measures": L("UI-EVID-WHAT-DOES-IT-MEASURE"), "applies": L("UI-EVID-WHO-OR-WHAT-DOES-IT"),
                "period": L("UI-EVID-WHEN-WAS-IT-MEASURED-OR"), "currentness": L("UI-EVID-HOW-CURRENT-IS-IT"),
                "does_not_establish": L("UI-EVID-DOES-NOT-ESTABLISH"), "measurement_limits": L("UI-EVID-MEASUREMENT-LIMITS"),
                "boundary": L("UI-DOM-WHAT-NOT-TO-CONCLUDE"),
                "source": L("UI-EVID-ORIGINAL-SOURCE-AND-VERIFICATION"), "source_intro": L("UI-EVID-OPEN-THE-SOURCE-RECORD-HERE"),
                "trace": L("UI-EVID-SOURCE-VERIFICATION-PATH"), "trace_intro": L("UI-EVID-THE-STABLE-RECORD-ID-STAYS"),
                "used_in": L("UI-EVIDENCE-USED-IN-READINGS"), "related": L("UI-EVID-RETURN-TO-INTERPRETATION"),
                "related_intro": L("UI-EVID-RETURN-TO-THE-QUESTION-OR"), "evidence_hub": self.nav_label("/evidence/", lang),
                "data": L("UI-EVID-DATA-SOURCES"), "methodology": L("UI-DOM-METHODOLOGY"),
                "more": L("UI-EVID-METHOD-AND-VERIFICATION-DETAIL"), "more_intro": L("UI-EVID-ADDITIONAL-DETAIL-FOR-REPRODUCING-OR"),
                "method": L("UI-EVID-HOW-WAS-IT-PRODUCED"), "change_trigger": L("UI-EVID-WHEN-DOES-THIS-RECORD-CHANGE"),
                "verification": L("UI-EVID-HOW-CAN-I-VERIFY-IT"), "reading_guidance": L("UI-EVID-HOW-SHOULD-THIS-RECORD-BE"),
                "reference": L("UI-EVID-REFERENCE-ID"), "report": L("UI-EVID-REPORT-AN-ISSUE"), "cite": L("UI-EVID-CITE-THIS-RECORD"),
                "reuse": L("UI-EVID-CITATION-AND-REUSE"), "reuse_note": L("UI-EVID-CITING-THE-EVIDENCE-DOES-NOT"),
                "history": L("UI-EVID-CORRECTIONS-RELEASE-HISTORY"), "source_reference": L("UI-SOURCE-REFERENCE"), "compare": L("UI-PAGE-COMPARE-EVIDENCE"),
                "visual_eyebrow": L("UI-DOM-A-VIEW-THAT-CHANGES-UNDERSTANDING"),
                "state_administrative": self.grammar_labels["UI-VIS-STATE-ADMINISTRATIVE"][lang],
                "state_derived": self.grammar_labels["UI-VIS-STATE-DERIVED"][lang],
                "disagreement": self.grammar_labels["UI-VIS-DISAGREEMENT"][lang],
                "understand_explore_verify": L("UI-DOM-UNDERSTAND-EXPLORE-VERIFY"),
            },
        }

    # ------------------------------------------------------------------------------------------------ reading
    def reading(self, route: str, lang: str) -> dict:
        spec = self.spec_by_route[route]
        r = (spec.get("governed_readings") or [{}])[0]
        rid = str(r.get("reading_id") or "")
        ids_by_order = {int(float(x.get("section_order") or 0)): x.get("section_id") for x in self.reading_sections if x.get("reading_id") == rid}
        secs = []
        for s in self.sections(spec, lang):
            body = s["body"]
            blocks, items = [], []

            def flush():
                if items:
                    blocks.append({"kind": "list", "items": list(items)})
                    items.clear()
            for line in body.split("\n"):
                t = line.strip()
                if not t:
                    continue
                if t.startswith("- "):
                    items.append(t[2:].strip())
                    continue
                flush()
                if t.startswith("> "):
                    blocks.append({"kind": "pull", "text": t[2:].strip()})
                else:
                    blocks.append({"kind": "p", "text": t})
            flush()
            secs.append({**s, "section_id": ids_by_order.get(s["order"]) or "", "blocks": blocks})
        visuals = [self.visual(v.get("visual_id"), lang) for v in spec.get("governed_visual_contracts") or []]
        # Trace: each bound record -> its route, headline, closure state and public sources (P1.5).
        bindings = r.get("verification_bindings") or {}
        ids = [str(x) for x in (bindings.get("claim_ids") or r.get("claim_bindings") or [])]
        ar = lang == "ar"
        steps, seen, unlisted, path_ids = [], set(), 0, []
        for oid in ids:
            route_ = self.detail_routes.get(oid)
            if not route_ or route_ in seen:
                continue
            seen.add(route_)
            path_ids.append(oid)
            ds = self.spec_by_route.get(route_) or {}
            claim = next((c for c in ds.get("governed_claims") or [] if c.get("claim_id") == oid), {})
            obj = (ds.get("governed_evidence_objects") or [{}])[0]
            clo = self.closure.get(("evidence_object", oid)) or {}
            state = clo.get("closure_state")
            flag = ""
            if state == "PARTIALLY_RESOLVED":
                flag = self.t("UI-READING-PATH-RECORD-PARTIAL", lang)
            elif state in ("COMPOSITE_OF_OBJECTS", "COMPOSITE_MEMBERS_NOT_LISTED"):
                flag = self.t("UI-READING-PATH-RECORD-COMPOSITE", lang)
            srcs, hidden = [], 0
            for sid in clo.get("resolved_source_ids") or []:
                card = self.source_card(sid, lang)
                if card:
                    srcs.append(card)
                else:
                    hidden += 1
            if hidden:
                unlisted += 1
            steps.append({"id": oid, "href": self.href(route_, lang),
                          "proposition": self.loc(claim, "headline", lang) or self.loc(obj, "title", lang) or self.loc(ds, "title", lang) or oid,
                          "summary": self.loc(obj, "summary", lang), "period": self.loc(obj, "period", lang),
                          "does_not_establish": self.boundary_parts(obj, lang)[0] if obj else "",
                          "state_flag": flag, "sources": srcs,
                          "no_locator_note": self.t("UI-SOURCE-NO-PUBLIC-LOCATOR", lang) if hidden else ""})
        rstate = (self.closure.get(("reading", rid)) or {}).get("closure_state")
        if rstate == "CLOSED_TO_SOURCE_ID":
            status = self.t("UI-READING-PATH-COMPLETE-UNLISTED" if unlisted else "UI-READING-PATH-COMPLETE", lang)
        else:
            status = self.t("UI-READING-PATH-PARTIAL", lang)
        cmp_ids = [x for x in path_ids if x in self.compare_ids][:4]
        compare_href = f"/{lang}/evidence/compare/?records={','.join(quote(x) for x in cmp_ids)}" if len(cmp_ids) >= 2 else ""
        back = []
        for rt in list(r.get("domain_context_routes") or []) + list(r.get("domain_surface_routes") or []):
            q = self._route(rt)
            if q in self.spec_by_route and q not in [b["route"] for b in back]:
                back.append({"route": q, "label": self.question_label(q, lang), "href": self.href(q, lang)})
        sources = []
        seen_s = set()
        for ref in spec.get("source_references") or []:
            sid = str(ref.get("source_id") or "").strip()
            if not sid or sid in seen_s:
                continue
            seen_s.add(sid)
            card = self.source_card(sid, lang)
            if card:
                sources.append(card)
        related = [{"title": self.loc(x, "title", lang), "thesis": self.loc(x, "thesis", lang), "href": self.href(x.get("route"), lang),
                    "evidence_period": self.loc(x, "evidence_period", lang)} for x in spec.get("related_readings") or []]
        ma_by_id = {str(m.get("measurement_id")): m for m in self.measurement_agenda}   # B6: the Reading's governed priorities
        measurement = [self.measurement_object(ma_by_id[str(x)], lang) for x in (r.get("measurement_bindings") or []) if str(x) in ma_by_id]
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {
            "family": "Reading", "route": route, "lang": lang, "id": rid,
            "title": self.loc(r, "title", lang), "question": self.loc(r, "question", lang), "thesis": self.loc(r, "thesis", lang),
            "meta_description": self.loc(spec, "meta_description", lang),
            "breadcrumb": self.breadcrumb("Reading", lang, self.loc(r, "title", lang)),
            "evidence_period": self.loc(r, "evidence_period", lang), "last_reviewed_iso": r.get("last_reviewed"),
            "last_reviewed": self.date_words(r.get("last_reviewed"), lang),
            "prohibited_inference": self.loc(r, "prohibited_inference", lang),
            "sections": [s for s in secs if s["order"] != 1],  # section 1 repeats the thesis; shown once as the standfirst
            "visuals": visuals, "trace": steps, "trace_status": status, "trace_state": rstate, "compare_href": compare_href,
            "return_to": back, "sources": sources, "related": related, "measurement": measurement,
            "labels": {"eyebrow": L("UI-READING-EYEBROW"), "evidence_period": L("UI-READING-EVIDENCE-PERIOD"), "last_reviewed": L("UI-READING-LAST-REVIEWED"),
                       "do_not_infer": L("UI-READING-DO-NOT-INFER"), "trace": L("UI-READING-TRACE-H"), "trace_intro": L("UI-READING-PATH-INTRO"),
                       "compare": L("UI-READING-TEST-COMPARABILITY-OF-THIS-READING"), "return": L("UI-READING-RETURN"),
                       "related": L("UI-READING-RELATED-H"), "all": L("UI-READING-ALL-H"), "sources": L("UI-SOURCES-SOURCES"), "measurement": L("UI-RELATED-MEASUREMENT"), "measurement_note": L("UI-READING-MEASUREMENT-NOTE"),
                       "source_record": L("UI-SOURCES-SOURCE-RECORD"), "reference": L("UI-SOURCE-REFERENCE"),
                       "open_record": L("UI-EVID-OPEN-EVIDENCE-RECORD"), "readings_index_href": self.href("/readings/", lang),
                       "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang]},
        }

    # ------------------------------------------------------------------------------------------------ visuals
    LANDSCAPE_DOMAINS = ("/people/", "/access/", "/payments/", "/remittances/", "/providers/", "/finance/", "/firms/", "/reforms/")

    def landscape(self, lang: str) -> dict | None:
        """RC-10 (Owner Addendum 2, improvement 3): the evidence landscape, the 00_MASTER block "EVIDENCE LANDSCAPE", as
        rows grouped by the eight domains. Every cell is governed: the row's dimension, the titles and periods of the
        public records it names, categorical labels, the domain pages and the Measurement Agenda priorities."""
        snap = _load("content/master_principles.json")
        rows = snap.get("rows") or []
        hi = next((i for i, r in enumerate(rows) if r and r[0] == "landscape_id"), None)
        if hi is None:
            return None
        hdr = [str(h) if h is not None else "" for h in rows[hi]]
        recs = []
        for r in rows[hi + 1:]:
            if not r or not r[0]:
                break
            recs.append({h: (r[i] if i < len(r) else None) for i, h in enumerate(hdr) if h})
        L = lambda k: self.t(k, lang)  # noqa: E731
        dom_label = {d: L("UI-LAND-DOM-" + d.strip("/").upper()) for d in self.LANDSCAPE_DOMAINS}
        ma_by_id = {str(m.get("measurement_id")): m for m in self.measurement_agenda}
        groups = []
        for d in self.LANDSCAPE_DOMAINS:
            items = []
            for r in [x for x in recs if x.get("domain_route") == d]:
                cov = str(r.get("coverage_state") or "")
                records = [x for x in (self.compact_record(oid, lang) for oid in json.loads(r.get("record_ids") or "[]")) if x]
                classes = [L("UI-LAND-CLASS-" + c.strip()) for c in str(r.get("evidence_class") or "").split(";") if c.strip()]
                items.append({"id": r.get("landscape_id"), "dimension": r.get(f"dimension_{lang}") or "",
                              "records": [{"title": x["title"], "href": x["href"], "period": x["period"]} for x in records],
                              "empty": L("UI-LAND-COV-NO_EVIDENCE") if cov == "NO_EVIDENCE" else L("UI-LAND-NO-PUBLIC-RECORD"),
                              "classes": classes or [L("UI-LAND-COV-NO_EVIDENCE")], "coverage": L("UI-LAND-COV-" + cov),
                              "verify": [{"label": dom_label.get(rt) or rt, "href": self.href(rt, lang)} for rt in json.loads(r.get("verify_routes") or "[]")],
                              "priorities": [{"title": self.loc(ma_by_id[m], "title", lang), "href": f"/{lang}/measurement/#{quote(m)}"}
                                             for m in json.loads(r.get("measurement_ids") or "[]") if m in ma_by_id]})
            if items:
                groups.append({"label": dom_label[d], "rows": items})
        return {"groups": groups, "head": [L(k) for k in ("UI-LAND-COL-DIMENSION", "UI-LAND-COL-EVIDENCE", "UI-LAND-COL-CLASS", "UI-LAND-COL-COVERAGE", "UI-LAND-COL-NEXT")],
                "note": L("UI-LAND-NOTE"), "no_next": L("UI-LAND-NO-NEXT")}

    def visual(self, vid: str, lang: str) -> dict:
        v = self.visual_contracts[vid]
        g = v["governed"]
        c = v.get("contract") or {}
        lab = lambda k: self.grammar_labels[k][lang]  # noqa: E731
        out = {
            "id": vid, "tier": v["tier"], "title": g.get(f"title_{lang}"), "question": g.get(f"question_{lang}"),
            "prohibited_inference": g.get(f"prohibited_inference_{lang}"), "alt_text": g.get(f"alt_text_{lang}"),
            "summary": (self.accessible_summary.get(vid) or {}).get(f"accessible_summary_{lang}"),
            "period": g.get(f"period_{lang}"), "universe": g.get(f"universe_{lang}"),
            "canonical_href": self.href(g.get("canonical_route"), lang),
            "detached_caption": v.get(f"detached_caption_{lang}"),
            "lang": lang, "edition": self.t("UI-CONTENT-VERSION", lang),
            "count_unit": self.t("UI-VIS-UNIT-COUNT", lang),   # G4 item 7: an Arabic count prints in label-value form
            "labels": {"does_not_establish": lab("UI-VIS-DOES-NOT-ESTABLISH"), "source": lab("UI-VIS-SOURCE"), "full_record": lab("UI-VIS-FULL-RECORD"), "open_record": self.t("UI-EVID-OPEN-EVIDENCE-RECORD", lang),
                       "same_year_revision": lab("UI-VIS-SAME-YEAR-REVISION"), "not_comparable": lab("UI-VIS-NOT-COMPARABLE"),
                       "reported": lab("UI-VIS-STATE-REPORTED"), "derived": lab("UI-VIS-STATE-DERIVED"), "unknown": lab("UI-VIS-STATE-UNKNOWN"),
                       "issuer_scope": lab("UI-VIS-ISSUER-SCOPE"),
                       "analytical_question": self.t("UI-DOM-ANALYTICAL-QUESTION", lang), "what_it_shows": self.t("UI-VIS-WHAT-THE-EVIDENCE-SHOWS", lang),
                       "text_alternative": self.t("UI-DOM-ANALYTICAL-TEXT-ALTERNATIVE", lang), "scope": self.t("UI-DOM-SCOPE-AND-TIME", lang),
                       "what_not_to_conclude": self.t("UI-DOM-WHAT-NOT-TO-CONCLUDE", lang),
                       "open_source_record": self.t("UI-EVID-OPEN-SOURCE-RECORD", lang), "source_record": self.t("UI-SOURCES-SOURCE-RECORD", lang),
                       "reference": self.t("UI-SOURCE-REFERENCE", lang), "period": self.t("UI-EVID-WHEN-WAS-IT-MEASURED-OR", lang),
                       "value_unit_per_row": self.t("UI-VIS-VALUE-UNIT-PER-ROW", lang),   # release candidate G4 (D6)
                       "th": {k: self.t(f"UI-VIS-TH-{k.upper()}", lang) for k in ("period", "group", "corridor", "object", "step", "dimension", "date", "item", "source")}},   # B10 (NCC-02)
        }
        if vid == "VIS-EVIDENCE-FRESHNESS":
            out["landscape"] = self.landscape(lang)   # RC-10: the text frame carries the evidence landscape table
        if v.get("table"):                            # RC-12 (B12): a text-first contract's table from governed rows
            t = v["table"]
            def tcell(c: dict) -> dict:
                o = {"span": c.get("span", 1)}
                if "text" in c:
                    o["text"] = c["text"][lang]
                elif "month" in c:
                    o["text"] = self.date_words(c["month"], lang)
                else:
                    o["number"] = c["number"]
                if c.get("unit"):
                    o["unit"] = c["unit"][lang]
                return o
            out["text_table"] = {"head": [h[lang] for h in t["head"]], "caption": [c[lang] for c in t["caption"]],
                                 "rows": [{"marker": r["marker"][lang]} if "marker" in r
                                          else {"group": {"lead": r["group"]["lead"][lang], "number": r["group"]["number"], "unit": r["group"]["unit"][lang]}} if "group" in r
                                          else {"head": r["head"][lang], "cells": [tcell(c) for c in r["cells"]]}
                                          for r in t["rows"]]}
        if c:
            def localise(row: dict) -> dict:
                """A governed row with every `<field>_label` resolved to the page language (the generator's display-label
                rule) and its `metric_label_<lang>` kept; encoding-only fields (caveat, flag) are never printed. A row
                whose `source` is a source-record id with a public locator also carries the record's data-page link and
                governed title (D6: the matrix and the lanes link every dated cell to its source record); a source
                without a public locator is never named or linked."""
                o = {}
                for k, val in row.items():
                    if k.endswith("_label") and isinstance(val, dict):
                        o[k[:-6] + "_text"] = val.get(lang) or ""
                    elif k in ("metric_label_en", "metric_label_ar"):
                        if k.endswith(lang):
                            o["metric_text"] = val
                    elif k in ("label_en", "label_ar"):
                        if k.endswith(lang):
                            o["label_text"] = val
                    elif not isinstance(val, dict):
                        o[k] = val
                # RC-5 (B2 g): a governed Arabic period, where the row has one, is the period the Arabic edition prints
                if lang == "ar" and o.get("date_ar"):
                    o["date"] = o["date_ar"]
                # the names the D1 renderer used
                o["unit"] = o.get("unit_text", "")
                o["series_label"] = o.get("series_label_text", "")
                o["state"] = row.get("grammar_state")
                o["markers"] = row.get("markers") or []
                src = str(row.get("source") or "")
                if src.startswith("SRC-"):
                    card = self.source_card(src, lang)
                    o["source_href"] = card["data_href"] if card else ""
                    o["source_title"] = (card["title"] or card["untitled_label"]) if card else ""
                return o
            out["form"] = c.get("form")
            out["credit"] = (c.get("credit") or {}).get("text_ar" if lang == "ar" else "text") or (c.get("credit") or {}).get("text")   # B4: the Arabic credit in the Arabic edition
            out["frame_labels"] = {k: val.get(lang) for k, val in (c.get("frame_labels") or {}).items()}
            out["series"] = [{"id": s["id"], "state": s.get("state"), "markers": s.get("markers") or [], "missing_x": s.get("missing_x") or [],
                              "values": [localise(val) for val in s.get("values") or []]} for s in c.get("series") or []]
            out["derived"] = [{"id": d["id"], "series": d.get("series"), "x": d.get("x"), "value": d.get("value"), "from": d.get("from") or [],
                               "unit": (d.get("unit_label") or {}).get(lang, ""), "series_label": (d.get("series_label_label") or {}).get(lang), "state": d.get("grammar_state")}
                              for d in c.get("derived") or []]
            out["objects"] = {o["id"]: [localise(r) for r in o.get("records") or []] for o in c.get("objects") or []}
            out["step_mapping"] = c.get("step_mapping") or {}
            out["rules"] = {k: c.get(k) for k in ("ordering", "transformation", "breaks", "annotation", "mobile", "rtl", "fallback", "missing")}
        ev = self.evidence_objects.get(vid) or {}
        out["record_method"] = self.loc(ev, "method", lang)   # B1: the 13 table-only records' method text is printed too
        out["record_limit"] = ev.get(f"measurement_limitation_{lang}") or ""   # the record's own measurement limitation (in frame where a contract asks for it)
        out["record_href"] = self.href(self.detail_routes[vid], lang) if vid in self.detail_routes else ""
        out["state_labels"] = {k[len("UI-VIS-STATE-"):]: v[lang] for k, v in self.grammar_labels.items() if k.startswith("UI-VIS-STATE-")}
        out["marker_labels"] = {k[len("UI-VIS-"):]: v[lang] for k, v in self.grammar_labels.items() if k.startswith(("UI-VIS-BREAK-", "UI-VIS-MISSING", "UI-VIS-DISAGREEMENT", "UI-VIS-NOMINAL", "UI-VIS-WITHHELD", "UI-VIS-NOT-COMPARABLE", "UI-VIS-SAME-YEAR", "UI-VIS-TARGET", "UI-VIS-RESULT", "UI-VIS-BASELINE"))}
        out["chain_labels"] = {k[len("UI-VIS-CHAIN-"):]: v[lang] for k, v in self.grammar_labels.items() if k.startswith("UI-VIS-CHAIN-")}
        if vid == "VIS-PAYMENT-RAILS" and "RV-CWR-009" in self.visual_contracts:
            out["_chain_source"] = self.visual("RV-CWR-009", lang)   # its rationale: reuse the signature chain's deduplicated event set
        if vid == "RV-CWR-004":
            # The people lane is drawn as the fieldwork span stated in the governed period of evidence record CLM-001
            # (the contract's ordering and annotation rules), never as a point at the data year.
            clm = self.evidence_objects.get("CLM-001") or {}
            period = self.loc(clm, "period", lang)
            dates = re.findall(r"\d{4}-\d{2}-\d{2}", period)
            out["people_span"] = {"from": dates[0], "to": dates[-1], "text": period, "href": self.href(self.detail_routes["CLM-001"], lang)} if len(dates) >= 2 else None
        if vid == "VIS-PROVIDER-OBSERVABILITY" and "RV-CWR-009" in self.visual_contracts:
            # The contract's known gap: no governed row exists for payment-system operators; the row is drawn as UNKNOWN
            # with the institution events REF-PAY-011..013 (governed rows of RV-CWR-009) listed as context, never as a
            # named universe. The row's class label is not governed yet (escalated): the row renders when it exists.
            chain = self.visual("RV-CWR-009", lang)
            out["_context_events"] = [e for e in chain["objects"].get("reform_events") or [] if e["id"] in ("REF-PAY-011", "REF-PAY-012", "REF-PAY-013")]
            out["labels"]["class_pso"] = self.t("UI-VIS-CAT-PRV-CLASS-PSO", lang) if "UI-VIS-CAT-PRV-CLASS-PSO" in self.ui else ""
            out["labels"]["context"] = self.t("UI-VIS-MATRIX-CONTEXT", lang) if "UI-VIS-MATRIX-CONTEXT" in self.ui else ""   # RC-5 (B2 h)
            out["matrix_headings"] = {k: (self.t(k, lang) if k in self.ui else "") for k in
                                      ("UI-VIS-MATRIX-AUTHORITY", "UI-VIS-MATRIX-UNIVERSE", "UI-VIS-MATRIX-STATUS", "UI-VIS-MATRIX-NEGATIVE", "UI-VIS-MATRIX-OPERATION")}
        return out

    # ------------------------------------------------------------------------------------------------ home
    def home(self, lang: str) -> dict:
        spec = self.spec_by_route["/"]
        secs = self.sections(spec, lang)
        chosen = self.home_question_ids   # the R8.4A selection (presentation contract, EAD-11)
        qs = {q["question_id"]: q for q in self.questions}
        starting = []
        for qid in chosen:
            q = qs[qid]
            rt = self._route(q.get("primary_route"))
            starting.append({"id": qid, "question": self.loc(q, "question", lang), "gets": self.loc(q, "user_gets", lang),
                             "href": self.href(rt, lang) + ("#system" if rt == "/" else "")})
        records, seen = [], set()
        # JRN-03: every record bound to the page is reachable from it (claims, evidence objects and the visual's record).
        for o in (spec.get("governed_claims") or []) + (spec.get("governed_evidence_objects") or []) + (spec.get("governed_visual_contracts") or []):
            oid = str(o.get("claim_id") or o.get("evidence_object_id") or o.get("object_id") or o.get("visual_id") or "")
            if not oid or oid in seen or oid not in self.detail_routes:
                continue
            seen.add(oid)
            ev = self.evidence_objects.get(oid) or {}
            records.append({"id": oid, "title": self.loc(ev, "title", lang) or self.loc(o, "headline", lang) or self.loc(o, "title", lang) or oid,
                            "href": self.href(self.detail_routes[oid], lang), "summary": self.loc(ev, "summary", lang),
                            "period": self.loc(ev, "period", lang), "universe": self.loc(ev, "universe", lang),
                            "does_not_establish": self.boundary_parts(ev, lang)[0] if ev else "", "is_visual_record": oid.startswith("VIS-")})
        f = spec.get("featured_reading") or {}
        featured = {"id": f.get("reading_id"), "title": self.loc(f, "title", lang), "thesis": self.loc(f, "thesis", lang),
                    "evidence_period": self.loc(f, "evidence_period", lang), "href": self.href(f.get("route"), lang)} if f else None
        system = self.visual("VIS-INCLUSION-TRANSMISSION", lang)
        L = lambda k: self.t(k, lang)  # noqa: E731
        # RC-15 (B15 d, A-8): the measurement priorities bound to "/" (MA-001, MA-003, MA-005), by their governed titles,
        # under the section that names the three gaps
        gaps = [{"id": str(m.get("measurement_id")), "title": self.loc(m, "title", lang),
                 "href": f"/{lang}/measurement/#{quote(str(m.get('measurement_id')))}"} for m in spec.get("governed_measurement_priorities") or []]
        return {
            "family": "Orientation", "route": "/", "lang": lang, "gap_priorities": gaps,
            "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
            "sections": secs, "starting_questions": starting, "records": records, "featured": featured, "system_visual": system,
            "question_count": self.inventory["entry_questions"],
            "hrefs": {"explore": self.href("/explore/", lang), "evidence": self.href("/evidence/", lang), "readings": self.href("/readings/", lang),
                      "measurement": self.href("/measurement/", lang), "data": self.href("/data/", lang), "methodology": self.href("/methodology/", lang)},
            "labels": {"product": L("UI-PRODUCT-NAME"), "start": L("UI-HERO-START-WITH-A-QUESTION"), "verify": L("UI-HERO-VERIFY-EVIDENCE"),
                       "flow": L("UI-DOM-UNDERSTAND-EXPLORE-VERIFY"), "side": L("UI-HERO-THIS-RESOURCE-PRESENTS-THE-STRONGEST"),
                       "questions_eyebrow": L("UI-QUESTIONS-COMMON-STARTING-QUESTIONS"), "questions_title": L("UI-QUESTIONS-START-FROM-THE-PROBLEM-YOU"),
                       "view_all": self.tf("UI-QUESTIONS-VIEW-ALL", lang, n=self.inventory["entry_questions"]),
                       "records_heading": L("UI-HOME-FIGURES-EVIDENCE"), "featured": L("UI-READING-FEATURED"), "open_reading": L("UI-READING-OPEN"),
                       "all_readings": L("UI-READING-ALL-H"), "evidence_period": L("UI-READING-EVIDENCE-PERIOD"),
                       "readings_nav": self.nav_label("/readings/", lang), "measurement_nav": self.nav_label("/measurement/", lang), "data_nav": self.nav_label("/data/", lang),
                       "cta_readings": L("UI-HOME-CROSS-SOURCE-ANALYSIS-THAT-STAYS"), "cta_measurement": L("UI-HOME-WHAT-REMAINS-UNKNOWN-AND-WHAT"),
                       "cta_data": L("UI-HOME-FIND-THE-ORIGINAL-SOURCES-BEHIND"), "open_record": L("UI-DOM-OPEN-EVIDENCE-RECORD"),
                       "open_evidence_record": L("UI-EVID-OPEN-EVIDENCE-RECORD"), "visual_eyebrow": L("UI-DOM-A-VIEW-THAT-CHANGES-UNDERSTANDING"),
                       "scope": L("UI-DOM-SCOPE-AND-TIME"), "boundary": L("UI-DOM-WHAT-NOT-TO-CONCLUDE"),
                       "period": L("UI-EVID-WHEN-WAS-IT-MEASURED-OR"), "applies": L("UI-EVID-WHO-OR-WHAT-DOES-IT"),
                       "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang],
                       "gaps_heading": L("UI-RELATED-MEASUREMENT"), "gaps_note": L("UI-HOME-GAPS-NOTE")},
        }

    # ------------------------------------------------------------------------------------------------ shared (D2)
    def family(self, route: str) -> str:
        return self.family_by_route.get(route) or ("Evidence Record" if route.startswith("/evidence/") and route != "/evidence/compare/" else "Reference / Trust")

    def journey_next(self, route: str, lang: str) -> dict | None:
        """The governed next actions of a route (navigation contract `route_next_actions`)."""
        targets = (self.nav.get("route_next_actions") or {}).get(route) or []
        if not targets:
            return None
        return {"title": self.t("UI-NEXT-CONTINUE-FROM-HERE", lang), "intro": self.t("UI-NEXT-CHOOSE-THE-NEXT-PATH-THAT", lang),
                "links": [{"label": self.nav_label(t, lang), "href": self.href(t, lang)} for t in targets]}

    def compact_record(self, oid: str, lang: str, claim: dict | None = None, show_ref: bool = False) -> dict | None:
        """A bound record as a clock-first compact object: when → title → for whom → boundary → open."""
        if oid not in self.detail_routes:
            return None
        ev = self.evidence_objects.get(oid) or {}
        claim = claim or {}
        title = self.loc(ev, "title", lang) or self.loc(claim, "headline", lang) or oid
        return {"id": oid, "title": title, "href": self.href(self.detail_routes[oid], lang),
                "summary": self.loc(claim, "copy", lang) or self.loc(ev, "summary", lang),
                "period": self.loc(ev, "period", lang), "universe": self.loc(ev, "universe", lang),
                "does_not_establish": (self.boundary_parts(ev, lang)[0] if ev else "") or self.loc(claim, "does_not_prove", lang),
                "is_visual_record": oid.startswith("VIS-"), "ref": oid if show_ref else "", "compare_href": f"/{lang}/evidence/compare/?records={quote(oid)}" if oid in self.compare_ids else ""}

    def bound_records(self, spec: dict, lang: str, show_ref: bool = False) -> list[dict]:
        """JRN-03: every record bound to a page, reachable from it, as compact objects (claims first, with their copy)."""
        out, seen = [], set()
        claims = {str(c.get("claim_id") or ""): c for c in spec.get("governed_claims") or []}
        for o in (spec.get("governed_claims") or []) + (spec.get("governed_evidence_objects") or []) + (spec.get("governed_visual_contracts") or []):
            oid = str(o.get("claim_id") or o.get("evidence_object_id") or o.get("object_id") or o.get("visual_id") or "")
            if not oid or oid in seen:
                continue
            rec = self.compact_record(oid, lang, claims.get(oid), show_ref)
            if rec:
                seen.add(oid)
                out.append(rec)
        return out

    def measurement_object(self, m: dict, lang: str, examined: list | None = None, full: bool = False) -> dict:
        """A Measurement priority as an object: the decision it constrains, what is known, what is missing, what would change it."""
        mid = str(m.get("measurement_id") or "")
        L = lambda k: self.t(k, lang)  # noqa: E731
        out = {"id": mid, "priority": str(m.get("priority") or ""), "domain": str((m.get("domain_ar") if lang == "ar" else m.get("domain")) or "").strip(),
               "title": self.loc(m, "title", lang), "current": self.loc(m, "current_evidence", lang), "missing": self.loc(m, "missing_evidence", lang),
               "unlocked": self.loc(m, "unlocked_decision", lang), "href": f"/{lang}/measurement/#{quote(mid)}",
               "examined": [{"title": self.loc(x, "title", lang), "href": self.href(x.get("route"), lang)} for x in examined or []],
               "labels": {"priority": L("UI-MA-PRIORITY"), "current": L("UI-MA-CURRENT-EVIDENCE"), "missing": L("UI-MA-MISSING-EVIDENCE"), "unlocked": L("UI-MA-DECISION-UNLOCKED"),
                          "open": L("UI-MA-OPEN"), "more": L("UI-MA-MORE"), "examined": L("UI-MEASUREMENT-EXAMINED-IN"), "reference": L("UI-SOURCE-REFERENCE"), "needed": L("UI-BLOCK-EVIDENCE-NEEDED"),
                          "decisions": L("UI-MA-DECISIONS"), "blocked": L("UI-MA-BLOCKED")}}
        if full:
            # B6: the governed decisions_unlocked (items joined by commas after a sentence end) and blocked_evidence
            du = self.loc(m, "decisions_unlocked", lang)
            out["decisions"] = [x.strip() for x in DECISION_SPLIT.split(du) if x.strip()] if du else []
            out["blocked"] = self.loc(m, "blocked_evidence", lang)
            out["more"] = [{"label": L(uid), "text": self.loc(m, f, lang)} for f, uid in (("guardrail", "UI-MA-GUARDRAIL"), ("feasibility", "UI-MA-FEASIBILITY"), ("priority_basis", "UI-MA-BASIS"), ("what_changes", "UI-MA-CHANGES")) if self.loc(m, f, lang)]
        return out

    def governed_blocks(self, spec: dict, lang: str, route_key: str) -> list[dict]:
        """The bound objects a static page carries beside its prose: records (claims and objects), visuals, priorities."""
        records = self.bound_records(spec, lang, show_ref=(route_key == "/evidence"))
        visuals = [self.visual(v.get("visual_id"), lang) for v in spec.get("governed_visual_contracts") or [] if v.get("visual_id") in self.visual_contracts]
        measures = [self.measurement_object(m, lang) for m in spec.get("governed_measurement_priorities") or []]
        rec_h = {"/measurement": "UI-MEASURE-REVEALING-RECORDS", "/evidence": "UI-HUB-START-HERE"}.get(route_key, "UI-RELATED-RECORDS")
        ma_h = "UI-EXPLORE-CANNOT-ANSWER" if route_key == "/explore" else "UI-RELATED-MEASUREMENT"
        out = []
        if records:
            out.append({"kind": "records", "heading": self.t(rec_h, lang), "items": records})
        if visuals:
            out.append({"kind": "visuals", "heading": "", "items": visuals})
        if measures:
            # RC-15 (B15 d, B-5): Explore shows the P0 priorities and says so (gate RC-B15 keeps the set equal to them)
            note = self.t("UI-EXPLORE-MA-BASIS", lang) if route_key == "/explore" else ""
            out.append({"kind": "measurement", "heading": self.t(ma_h, lang), "items": measures, "note": note})
        return out

    def related_questions(self, route: str, lang: str) -> dict | None:
        """JRN-12: the governed system relationships from this answer page to other answer pages (never inferred)."""
        targets = []
        for r in self.relationships:
            a, t = self._route(r.get("from")), self._route(r.get("to"))
            if a == route and t != route and t in self.spec_by_route and t not in targets:
                targets.append(t)
        if not targets:
            return None
        return {"heading": self.t("UI-RELATED-QUESTIONS", lang), "note": self.t("UI-RELATED-QUESTIONS-NOTE", lang),
                "links": [{"label": self.question_label(t, lang), "href": self.href(t, lang)} for t in targets]}

    def chronology(self, lang: str) -> dict | None:
        """The system chronology: dated events, each with its relevance, what it does not establish and its public sources."""
        items = []
        for e in self.chronology_events:
            fact = self.loc(e, "fact", lang)
            if not fact:
                continue
            sources = []
            for sid in [x.strip() for x in str(e.get("source_ids") or "").split("|") if x.strip()]:
                card = self.source_card(sid, lang)
                if card:
                    sources.append({"id": sid, "title": card["title"], "href": card["data_href"]})
            items.append({"id": str(e.get("event_id") or ""), "period": self.loc(e, "period", lang), "fact": fact,
                          "relevance": self.loc(e, "fi_relevance", lang) or self.loc(e, "system_implication", lang),
                          "does_not_establish": self.loc(e, "does_not_establish", lang), "sources": sources,
                          "verification_note": self.loc(e, "verification_note", lang)})   # RC-1 item 3: stated with the event when it has not been checked against its original
        if not items:
            return None
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {"heading": L("UI-CHRONOLOGY-H"), "intro": L("UI-CHRONOLOGY-INTRO"), "items": items,
                "labels": {"relevance": L("UI-CHRONOLOGY-RELEVANCE"), "sources": L("UI-CHRONOLOGY-SOURCES"), "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang]}}

    def reading_object(self, r: dict, lang: str) -> dict:
        full = next((x for x in self.readings if x.get("reading_id") == r.get("reading_id")), r)
        return {"id": r.get("reading_id"), "title": self.loc(r, "title", lang), "thesis": self.loc(r, "thesis", lang), "question": self.loc(full, "question", lang),
                "evidence_period": self.loc(full, "evidence_period", lang), "href": self.href(r.get("route"), lang)}

    def common_labels(self, lang: str) -> dict:
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {"period": L("UI-EVID-WHEN-WAS-IT-MEASURED-OR"), "applies": L("UI-EVID-WHO-OR-WHAT-DOES-IT"), "open_record": L("UI-EVID-OPEN-EVIDENCE-RECORD"),
                "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang], "boundary": L("UI-DOM-WHAT-NOT-TO-CONCLUDE"),
                "reference": L("UI-SOURCE-REFERENCE"), "evidence_period": L("UI-READING-EVIDENCE-PERIOD"), "reading_eyebrow": L("UI-READING-EYEBROW"),
                "open_reading": L("UI-READING-OPEN"), "all_readings": L("UI-READING-ALL-H"), "featured": L("UI-READING-FEATURED"), "go_deeper": L("UI-EXPLORE-GO-DEEPER"),
                "flow": L("UI-DOM-UNDERSTAND-EXPLORE-VERIFY"), "compare": L("UI-PAGE-COMPARE-EVIDENCE"), "scope": L("UI-DOM-SCOPE-AND-TIME"),
                "cite": L("UI-HEADER-CITE-THIS-PAGE"), "search": L("UI-SEARCH-SEARCH")}

    # ------------------------------------------------------------------------------------------------ question entry
    def question_entry(self, lang: str) -> dict:
        spec = self.spec_by_route["/explore/"]
        secs = self.sections(spec, lang)
        qs = {q["question_id"]: q for q in self.questions}
        groups = []
        for g in self.question_groups:
            items = []
            for qid in g.get("question_ids") or []:
                q = qs.get(qid)
                if not q:
                    continue
                rt = self._route(q.get("primary_route"))
                items.append({"id": qid, "question": self.loc(q, "question", lang), "gets": self.loc(q, "user_gets", lang), "href": self.href(rt, lang) + ("#system" if rt == "/" else "")})
            groups.append({"id": g.get("heading_ui_id"), "heading": self.t(g.get("heading_ui_id"), lang), "items": items})
        f = spec.get("featured_reading") or {}
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {"family": "Question Entry", "route": "/explore/", "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
                "list_section": next((s for s in secs if s["order"] == 5), None), "groups": groups,
                "featured": self.reading_object(f, lang) if f else None, "blocks": self.governed_blocks(spec, lang, "/explore"),
                "next": self.journey_next("/explore/", lang), "readings_href": self.href("/readings/", lang),
                "labels": {**self.common_labels(lang), "eyebrow": L("UI-QUESTIONS-QUESTIONS-INTO-THE-EVIDENCE"), "list_title": L("UI-QUESTIONS-FIND-THE-QUESTION-CLOSEST-TO"),
                           "list_intro": L("UI-QUESTIONS-EVERY-ROUTE-KEEPS-PERIOD-POPULATION")}}

    # ------------------------------------------------------------------------------------------------ domain answer
    _DOMAIN_LABELS = {"scope": "UI-DOM-SCOPE-AND-TIME", "boundary": "UI-DOM-WHAT-NOT-TO-CONCLUDE", "unknown": "UI-DOM-WHAT-REMAINS-UNKNOWN", "coverage": "UI-DOM-COVERAGE-LIMIT",
                      "visual": "UI-DOM-A-VIEW-THAT-CHANGES-UNDERSTANDING", "more": "UI-DOM-MORE-EVIDENCE-AND-CONTEXT", "more_intro": "UI-DOM-ADDITIONAL-CONTROLLED-DETAIL-FROM-THIS",
                      "measure": "UI-DOM-WHAT-MEASUREMENT-WOULD-CHANGE-THE", "verify": "UI-DOM-VERIFY-IT-YOURSELF", "verify_intro": "UI-DOM-OPEN-THE-EVIDENCE-RECORD-BEHIND",
                      "evidence": "UI-DOM-OPEN-EVIDENCE", "method": "UI-DOM-METHODOLOGY", "open_record": "UI-DOM-OPEN-EVIDENCE-RECORD", "do_not": "UI-DOM-DO-NOT-INFER",
                      "question_flow": "UI-DOM-UNDERSTAND-EXPLORE-VERIFY", "reading_rule": "UI-DOM-READING-RULE", "reading_rule_copy": "UI-DOM-EVERY-CONSEQUENTIAL-NUMBER-STAYS-ATTACHED",
                      "start": "UI-DOM-EXPLORE-QUESTIONS", "verify_action": "UI-DOM-OPEN-EVIDENCE", "answer_crumb": "UI-ANSWER-CRUMB-LABEL", "all_records": "UI-ANSWER-ALL-RECORDS",
                      "readings": "UI-DOM-EVIDENCE-READINGS-ON-THIS-QUESTION"}

    @staticmethod
    def band_kind(section: dict) -> str:
        role = str(section.get("role") or "")
        low = role.lower()
        if "does not establish" in low or "لا يثبته" in role:
            return "boundary"
        if "know" in low or "نعرف" in role:
            return "unknown"
        return "coverage"

    def domain(self, route: str, lang: str) -> dict:
        spec = self.spec_by_route[route]
        pres = self.presentation_routes[route]
        secs = {s["order"]: s for s in self.sections(spec, lang)}
        def orders(items):
            return [int(x["section_order"]) for x in (items or []) if x.get("kind") == "section" and isinstance(x.get("section_order"), int)]
        primary_visual, after = None, 2
        for x in pres.get("primary") or []:
            if x.get("kind") == "visual" and x.get("object_id"):
                primary_visual, after = str(x["object_id"]), int(x.get("after_primary") or 2)
        verify_ids = [str(v) for x in pres.get("utility") or [] if x.get("kind") == "verification_records" for v in (x.get("object_ids") or [])]
        claims = {str(c.get("claim_id") or ""): c for c in spec.get("governed_claims") or []}
        q = self.question_by_route.get(route)
        visuals = {v.get("visual_id"): self.visual(v.get("visual_id"), lang) for v in spec.get("governed_visual_contracts") or [] if v.get("visual_id") in self.visual_contracts}
        L = lambda k: self.t(k, lang)  # noqa: E731
        labels = {k: L(v) for k, v in self._DOMAIN_LABELS.items()}
        labels.update(self.common_labels(lang))
        labels["data"] = self.nav_label("/data/", lang)
        labels["explore"] = self.nav_label("/explore/", lang)
        return {
            "family": "Domain Answer", "route": route, "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
            "question": self.loc(q, "question", lang) if q else "", "lead": (secs.get(1) or {}).get("body", ""),
            "primary": [secs[o] for o in orders(pres.get("primary")) if o in secs],
            "band": [{**secs[o], "kind": self.band_kind(secs[o])} for o in orders(pres.get("supporting")) if o in secs],
            "progressive": [secs[o] for o in orders(pres.get("progressive")) if o in secs],
            "primary_visual": primary_visual, "visual_after": after, "visuals": visuals,
            "presentation_family": pres.get("presentation_family"), "primary_verify": self.href(pres.get("primary_verify_destination") or "/evidence/", lang),
            "readings": [self.reading_object(r, lang) for r in spec.get("governed_readings") or []],
            "measurement": [self.measurement_object(m, lang) for m in (spec.get("governed_measurement_priorities") or [])[:max(0, int(pres.get("measurement_limit") or 0))]],
            "related": self.related_questions(route, lang),
            "verify": [r for r in (self.compact_record(oid, lang, claims.get(oid)) for oid in verify_ids) if r],
            "all_records": self.bound_records(spec, lang), "chronology": self.chronology(lang) if route == "/finance/" else None,
            # RC-17 (Owner Addendum 2, improvement 1): where an answer rests on regulatory instruments, "Verify it yourself"
            # opens Data & sources at its regulatory group
            "hrefs": {"explore": self.href("/explore/", lang), "evidence": self.href("/evidence/", lang),
                      "data": self.href("/data/", lang) + ("#regulatory" if route in ("/reforms/", "/providers/") else ""),
                      "methodology": self.href("/methodology/", lang)},
            "compare_preset": self.compare_preset(route, lang),
            "labels": labels,
        }

    # ------------------------------------------------------------------------------------------------ evidence directory
    def evidence_directory(self, lang: str) -> dict:
        spec = self.spec_by_route["/evidence/"]
        secs = self.sections(spec, lang)
        groups: dict[str, list] = {}
        for oid, route in sorted(self.detail_routes.items()):
            if not route.startswith("/evidence/") or oid not in self.evidence_objects:
                continue
            ev = self.evidence_objects[oid]
            home = next((self._route(r) for r in ev.get("public_route_list") or [] if self._route(r) in self.question_by_route and self._route(r) != "/evidence/"), "")
            groups.setdefault(home, []).append({"id": oid, "title": self.loc(ev, "title", lang) or oid, "href": self.href(route, lang), "period": self.loc(ev, "period", lang)})
        order = sorted(groups, key=lambda r: (r == "", str(self.question_by_route.get(r, {}).get("question_id") or "ZZ")))
        hub = [{"route": r, "heading": self.question_label(r, lang) if r else self.t("UI-HUB-OTHER", lang), "items": groups[r]} for r in order]
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {"family": "Evidence Directory", "route": "/evidence/", "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "sections": secs, "blocks": self.governed_blocks(spec, lang, "/evidence"), "hub": hub, "record_count": self.inventory["evidence_records"],
                "next": self.journey_next("/evidence/", lang), "compare_href": self.href("/evidence/compare/", lang),
                "labels": {**self.common_labels(lang), "search_placeholder": L("UI-PAGE-SEARCH-CLAIMS-EVIDENCE-READINGS"), "search_status": L("UI-SEARCH-SEARCH-STATUS"),
                           "hub": L("UI-HUB-ALL-RECORDS")}}

    # ------------------------------------------------------------------------------------------------ comparison
    def comparison(self, lang: str) -> dict:
        spec = self.spec_by_route["/evidence/compare/"]
        secs = self.sections(spec, lang)
        claims = {str(c.get("claim_id") or ""): c for c in spec.get("governed_claims") or []}
        evidence, order = {}, []
        for x in spec.get("governed_evidence_objects") or []:
            oid = str(x.get("evidence_object_id") or x.get("object_id") or "")
            if oid and oid not in order:
                order.append(oid)
            if oid:
                evidence[oid] = x
        for oid in claims:
            if oid not in order:
                order.append(oid)
        records = []
        for oid in order:
            ev, cl = evidence.get(oid) or {}, claims.get(oid) or {}
            route = self.detail_routes.get(oid) or ""
            dspec = self.spec_by_route.get(route) or {}
            src_ids = [str(r.get("source_id") or "").strip() for r in dspec.get("source_references") or []]
            src_ids = [sid for sid in dict.fromkeys(src_ids) if sid and self.source_card(sid, lang)]
            a, b = self.boundary_parts(ev, lang)
            boundary = (f'{a} — {self.t("UI-EVID-MEASUREMENT-LIMITS", lang)}: {b}' if b else a) or self.loc(cl, "does_not_prove", lang)
            records.append({"id": oid, "title": self.loc(ev, "title", lang) or self.loc(cl, "headline", lang) or oid, "type": ev.get("object_class") or cl.get("claim_type") or "",
                            "definition": self.loc(ev, "definition", lang), "period": self.loc(ev, "period", lang), "universe": self.loc(ev, "universe", lang),
                            "method": self.loc(ev, "method", lang), "source": ", ".join(src_ids), "currentness": self.loc(ev, "currentness", lang),
                            "boundary": boundary, "verification": self.loc(ev, "verification", lang), "route": route})
        contract = (self.presentation.get("family_contracts") or {}).get("Comparison") or {}
        field_map = {"source_reference": "source"}
        dimensions = [field_map.get(x, x) for x in contract.get("supporting") or [] if field_map.get(x, x) in {"definition", "universe", "geography", "unit", "period", "method", "source", "currentness"}]
        L = lambda k: self.t(k, lang)  # noqa: E731
        return {"family": "Comparison", "route": "/evidence/compare/", "lang": lang, "compare_preset": self.compare_preset("/evidence/compare/", lang), "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
                "records": records, "dimensions": dimensions, "visual": self.visual("VIS-SOURCE-COMPARISON", lang) if "VIS-SOURCE-COMPARISON" in self.visual_contracts else None,
                "next": self.journey_next("/evidence/compare/", lang),
                "labels": {**self.common_labels(lang), "title": L("UI-COMPARE-CAN-THESE-RECORDS-ACTUALLY-BE"), "intro": L("UI-COMPARE-START-WITH-COMPARISON-LEGITIMACY-NOT"),
                           "first": L("UI-COMPARE-FIRST-RECORD"), "second": L("UI-COMPARE-SECOND-RECORD"), "third": L("UI-COMPARE-THIRD-RECORD-OPTIONAL"), "fourth": L("UI-COMPARE-FOURTH-RECORD-OPTIONAL"),
                           "optional": L("UI-COMPARE-OPTIONAL-RECORD"), "never": L("UI-COMPARE-NO-AUTO-AVERAGE-NO-PREFERRED"), "copy_link": L("UI-COMPARE-COPY-LINK-TO-THIS-COMPARISON"),
                           "do_not": L("UI-DOM-DO-NOT-INFER")}}

    # ------------------------------------------------------------------------------------------------ data & source
    _INV_LINE = re.compile(r"^(.+?):\s*(\d{1,3}(?:,\d{3})*)$")

    def data_sources(self, lang: str) -> dict:
        spec = self.spec_by_route["/data/"]
        secs = self.sections(spec, lang)
        for s in secs:
            toks = [t for t in (next((x for x in spec.get("sections", []) if int(x["section_order"]) == s["order"] and x.get(f"body_{lang}")), {}).get("resolved_inventory_tokens") or []) if t.get("field") == f"body_{lang}"]
            lines = s["paragraphs"]
            if toks and lines and all(self._INV_LINE.match(x) for x in lines):
                s["inventory"] = [{"label": self._INV_LINE.match(x).group(1), "value": self._INV_LINE.match(x).group(2)} for x in lines]
        ar = lang == "ar"
        curated_groups: dict[str, list] = {}
        supporting, reference, regulatory, regulatory_also = [], [], [], []
        facet_opts: dict[str, dict] = {"type": {}, "publisher": {}, "year": {}, "domain": {}}
        L = lambda k: self.t(k, lang)  # noqa: E731
        for sid, r in self.sources.items():
            url = self.public_locator(r.get("primary_url"))
            state = r.get("metadata_state")
            if not url:
                continue          # never named: the publication firewall (nine sources without a public locator)
            deps = [{"title": (d["title_ar"] if ar else d["title_en"]), "href": self.href(d["route"], lang)} for d in self.source_dependents.get(sid, [])]
            seen_routes, dependents = set(), []
            for d in deps:
                if d["href"] not in seen_routes:
                    seen_routes.add(d["href"]); dependents.append(d)
            search = " ".join(str(x or "") for x in [sid, r.get("display_title"), r.get("display_title_ar"), r.get("publisher"), r.get("publisher_ar"), r.get("document_label"), r.get("document_label_ar"), r.get("document_type"), url])
            display_ready = state == "DISPLAY_READY"
            card = {"id": sid, "url": url, "search": search, "dependents": dependents, "display_ready": display_ready,
                    "title": ((r.get("display_title_ar") if ar else r.get("display_title")) or "") if display_ready else "",
                    "publisher": ((r.get("publisher_ar") if ar else None) or r.get("publisher") or "") if display_ready else "",
                    "kind": ((r.get("document_label_ar") if ar else r.get("document_label")) or "") if display_ready else "",
                    "date": self.date_words(r.get("document_date"), lang) if display_ready else "",
                    "cite_payload": " · ".join(x for x in [((r.get("display_title_ar") if ar else r.get("display_title")) or "") if display_ready else "", sid, url] if x),
                    "rights_state": L("UI-SRC-REUSE-TERMS-NOT-ASSESSED") if r.get("rights_state") == "NOT_ASSESSED" else L("UI-SRC-REUSE-TERMS-NOT-STATED")}
            if not r.get("document_label"):   # B5 / EAD-07: a listed source with no governed document type says so
                card["kind"] = L("UI-DATA-DOCUMENT-TYPE-NOT-RECORDED")
            # RC-12 (B13): the Readings that use the source; the filter keys (language-neutral, so a shared link works in
            # both editions) and the date the list sorts by, all from governed fields; an archived copy says it is one
            card["readings"] = [{"title": d["title_ar"] if ar else d["title_en"], "href": self.href(d["route"], lang)} for d in self.source_readings.get(sid, [])]
            doms = sorted({rt for d in self.source_dependents.get(sid, []) for rt in d["public_routes"] if self.family_by_route.get(rt) == "Domain Answer"})
            year = str(r.get("document_date") or "")[:4] if display_ready else ""
            card["facets"] = {"type": _facet_key(r.get("document_label")), "publisher": _facet_key(r.get("publisher") if display_ready else None),
                              "year": year if year.isdigit() else "none", "domain": " ".join(rt.strip("/") for rt in doms) or "none",
                              "date": str(r.get("document_date") or "") if display_ready else ""}
            card["archived"] = urlparse(url).netloc == "web.archive.org"
            for fk, label in (("type", card["kind"]), ("publisher", card["publisher"] or L("UI-DATA-FILTER-NOT-RECORDED")),
                              ("year", card["facets"]["year"] if card["facets"]["year"] != "none" else L("UI-DATA-FILTER-NOT-RECORDED"))):
                facet_opts[fk].setdefault(card["facets"][fk], label)
            for rt in doms:   # the domain's governed name, as the evidence landscape prints it (RC-10)
                facet_opts["domain"].setdefault(rt.strip("/"), L("UI-LAND-DOM-" + rt.strip("/").upper()))
            card["regulatory"] = r.get("document_label") in REGULATORY_LABELS
            card["kind_line"] = " · ".join(x for x in [card["publisher"], card["kind"], card["date"]] if x)
            if display_ready and r.get("standalone_resource_card_eligible"):
                card.update({"category": (r.get("resource_category_ar") if ar else r.get("resource_category")) or "", "why": (r.get("why_it_matters_ar") if ar else r.get("why_it_matters")) or "",
                             "does_not_establish": (r.get("does_not_establish_ar") if ar else r.get("does_not_establish")) or ""})
                curated_groups.setdefault(card["category"], {"category": card["category"], "key": _facet_key(r.get("resource_category")), "items": []})["items"].append(card)
                if card["regulatory"]:
                    regulatory_also.append(card)   # the curated card stays under its category; the group links to it
            elif card["regulatory"]:
                regulatory.append(card)            # B5: rules, decisions and official lists, one group
            else:
                (supporting if dependents else reference).append(card)
        # RC-17 (Owner Addendum 2, improvement 1): the regulatory group in document-date order, newest first; an undated
        # document last (the sort is stable, so equal dates keep their governed order)
        regulatory.sort(key=lambda c: c["facets"].get("date") or "", reverse=True)
        return {"family": "Data & Source", "route": "/data/", "regulatory": regulatory, "regulatory_also": regulatory_also, "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
                "curated": list(curated_groups.values()), "supporting": supporting, "reference": reference,
                "curated_count": sum(len(v["items"]) for v in curated_groups.values()), "chronology": self.chronology(lang), "blocks": self.governed_blocks(spec, lang, "/data"),
                "next": self.journey_next("/data/", lang),
                "labels": {**self.common_labels(lang), "directory": L("UI-DATA-SOURCE-DIRECTORY-AND-VERIFICATION"), "intro": L("UI-DATA-ONLY-SOURCE-INFORMATION-PERMITTED-BY"),
                           "curated": L("UI-DATA-CURATED-REPORTS-AND-REFERENCES"), "supporting": L("UI-DATA-SOURCES-SUPPORTING-CURRENT-PUBLIC-EVIDENCE"),
                           "reference_group": L("UI-DATA-ADDITIONAL-ORIGINAL-REFERENCES-FOR-VERIFICATION"), "supporting_intro": L("UI-DATA-THESE-SOURCES-ARE-LINKED-DIRECTLY"),
                           "reference_intro": L("UI-DATA-THESE-REFERENCES-ARE-AVAILABLE-FOR"), "filter": L("UI-DATA-FIND-A-SOURCE-BY-TITLE"), "filter_placeholder": L("UI-DATA-E-G-SRC-CBY"),
                           "no_results": L("UI-DATA-NO-SOURCES-MATCH-THIS-SEARCH"), "rights_note": L("UI-DATA-EVERY-SOURCE-HERE-CAN-BE"), "open_original": L("UI-EVID-OPEN-ORIGINAL-SOURCE"),
                           "copy_reference": L("UI-EVID-COPY-SOURCE-REFERENCE"), "dependents": L("UI-EVID-EVIDENCE-RECORDS-USING-THIS-SOURCE"), "untitled": L("UI-SOURCE-UNTITLED"),
                           "record": L("UI-SOURCES-SOURCE-RECORD"), "regulatory": L("UI-DATA-GROUP-REGULATORY"),
                           "regulatory_scope": L("UI-DATA-GROUP-REGULATORY-SCOPE"), "reuse_once": L("UI-DATA-REUSE-TERMS-ONCE"),
                           # RC-12 (B13): the research library's filters, order and backlinks
                           "f_type": L("UI-DATA-FILTER-TYPE"), "f_publisher": L("UI-DATA-FILTER-PUBLISHER"), "f_year": L("UI-DATA-FILTER-YEAR"),
                           "f_domain": L("UI-DATA-FILTER-DOMAIN"), "f_any": L("UI-DATA-FILTER-ANY"), "f_clear": L("UI-DATA-FILTER-CLEAR"),
                           "sort": L("UI-DATA-SORT"), "sort_grouped": L("UI-DATA-SORT-GROUPED"), "sort_newest": L("UI-DATA-SORT-NEWEST"),
                           "readings": L("UI-DATA-READINGS-USING-SOURCE"), "open_archived": L("UI-EVID-OPEN-ARCHIVED-COPY")},
                "facets": {k: sorted(v.items(), key=lambda kv: ((kv[0] == "none"), (-int(kv[0]) if k == "year" and kv[0].isdigit() else 0), str(kv[1])))
                           for k, v in facet_opts.items()}}

    # ------------------------------------------------------------------------------------------------ reading index, measurement, reference
    def reading_index(self, lang: str) -> dict:
        spec = self.spec_by_route["/readings/"]
        secs = self.sections(spec, lang)
        f = spec.get("featured_reading") or {}
        fid = f.get("reading_id")
        return {"family": "Reading Index", "route": "/readings/", "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
                "featured": self.reading_object(f, lang) if f else None, "readings": [self.reading_object(r, lang) for r in self.readings if r.get("reading_id") != fid],
                "next": self.journey_next("/readings/", lang), "labels": self.common_labels(lang)}

    def measurement(self, lang: str) -> dict:
        spec = self.spec_by_route["/measurement/"]
        secs = self.sections(spec, lang)
        examined = spec.get("measurement_readings") or {}
        return {"family": "Measurement", "route": "/measurement/", "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
                "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
                # RC-15 (B15 d, A-8): the governed classes in order (P0, then P1), each in ID order; no item is ranked
                "priorities": [self.measurement_object(m, lang, examined.get(str(m.get("measurement_id"))), full=True)
                               for m in sorted(self.measurement_agenda, key=lambda m: (str(m.get("priority") or ""), str(m.get("measurement_id") or "")))],
                "blocks": self.governed_blocks(spec, lang, "/measurement"), "next": self.journey_next("/measurement/", lang), "labels": self.common_labels(lang)}

    def contact_address(self) -> str:
        spec = next((x for x in self.specs if x.get("template_route") == "/contact"), {})
        found = {m for sec in spec.get("sections") or [] for k in ("body_en", "body_ar") for m in re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", str(sec.get(k) or ""))}
        if len(found) != 1:
            raise ValueError(f"/contact must govern exactly one contact address, found {sorted(found)}")
        return found.pop()

    def reference(self, route: str, lang: str) -> dict:
        spec = self.spec_by_route[route]
        secs = self.sections(spec, lang)
        rt = spec.get("template_route") or route.rstrip("/")
        L = lambda k: self.t(k, lang)  # noqa: E731
        out = {"family": "Reference / Trust", "route": route, "lang": lang, "title": self.loc(spec, "title", lang), "meta_description": self.loc(spec, "meta_description", lang),
               "lead": secs[0]["body"] if secs and not secs[0]["heading"] else "", "sections": [s for s in secs if s["heading"]],
               "blocks": self.governed_blocks(spec, lang, rt), "next": self.journey_next(route, lang), "template": rt, "labels": self.common_labels(lang)}
        if rt in ("/contact", "/corrections"):
            out["context"] = {"mode": "contact" if rt == "/contact" else "corrections", "record_ids": sorted(self.detail_routes),
                              "current": L("UI-ORIGIN-RECORD-YOU-ARE-REPORTING-ON") if rt == "/contact" else L("UI-ORIGIN-RECORD-YOU-CAME-FROM"),
                              "open": L("UI-ORIGIN-OPEN-THE-CURRENT-PUBLIC-RECORD"), "malformed": L("UI-ORIGIN-THE-RECORD-REFERENCE-IN-THIS"), "unknown": L("UI-ORIGIN-THIS-LINK-NAMES-A-REFERENCE"),
                              "title": L("UI-CORR-CURRENT-RECORD-AND-CORRECTION-PATH"), "intro": L("UI-CORR-THIS-RESOURCE-DOES-NOT-MANUFACTURE"), "empty": L("UI-CORR-THIS-PAGE-CURRENTLY-HAS-NO"),
                              "write": L("UI-CONTACT-WRITE-TO-US-ABOUT-THIS"), "address": self.contact_address(), "subject": f'{self.t("UI-PRODUCT-NAME", "en")} — {L("UI-SOURCE-REFERENCE")}'}
        return out

    def not_found(self) -> dict:
        def L(k, lang):
            return self.t(k, lang)
        return {"family": "Not Found", "title": {l: L("UI-404-TITLE", l) for l in LANGS}, "product": {l: L("UI-PRODUCT-NAME", l) for l in LANGS},
                "sections": {l: {"heading": L("UI-404-HEADING", l), "body": L("UI-404-BODY", l), "home": L("UI-404-HOME", l), "explore": L("UI-404-EXPLORE", l),
                                 "evidence": L("UI-404-EVIDENCE", l), "search": L("UI-404-SEARCH", l)} for l in LANGS}}

    # ------------------------------------------------------------------------------------------------ dispatch
    def page(self, route: str, lang: str) -> dict:
        fam = self.family(route)
        if fam == "Orientation":
            return self.home(lang)
        if fam == "Question Entry":
            return self.question_entry(lang)
        if fam == "Domain Answer":
            return self.domain(route, lang)
        if fam == "Evidence Directory":
            return self.evidence_directory(lang)
        if fam == "Evidence Record":
            return self.evidence_record(route, lang)
        if fam == "Comparison":
            return self.comparison(lang)
        if fam == "Reading Index":
            return self.reading_index(lang)
        if fam == "Reading":
            return self.reading(route, lang)
        if fam == "Data & Source":
            return self.data_sources(lang)
        if fam == "Measurement":
            return self.measurement(lang)
        return self.reference(route, lang)

    def routes(self) -> list[str]:
        return [s["route"] for s in self.specs]

    # ------------------------------------------------------------------------------------------------ trio
    def trio(self, lang: str) -> dict:
        return {"/": self.home(lang), "/evidence/CLM-003/": self.evidence_record("/evidence/CLM-003/", lang),
                "/readings/same-year-different-number/": self.reading("/readings/same-year-different-number/", lang)}


def load() -> Content:
    return Content()
