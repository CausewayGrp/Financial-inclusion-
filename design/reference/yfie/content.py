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
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "site-src" / "content"

LANGS = ("en", "ar")
MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
}


def _load(rel: str):
    return json.loads((CONTENT / rel).read_text(encoding="utf-8"))


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
        self.claims = {c["claim_id"]: c for c in _load("evidence/public_claims.json")}
        self.sources = {s["source_id"]: s for s in _load("sources/source_reference_map.json")}
        self.closure = {(c["object_type"], c["object_id"]): c for c in _load("sources/public_object_source_closure.json")}
        self.visual_contracts = {v["visual_id"]: v for v in _load("visuals/visual_design_contracts.json")["visuals"]}
        self.grammar_labels = _load("visuals/visual_design_contracts.json")["grammar_labels"]
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
            "labels": {
                "skip": self.t("UI-HEADER-SKIP-TO-CONTENT", lang), "primary_nav": self.t("UI-HEADER-PRIMARY-NAVIGATION", lang),
                "trust_nav": self.t("UI-HEADER-TRUST-LINKS", lang), "menu": self.t("UI-HEADER-MENU", lang),
                "search": self.t("UI-SEARCH-SEARCH", lang), "search_title": self.t("UI-SEARCH-SEARCH-THE-PUBLIC-EVIDENCE", lang),
                "search_placeholder": self.t("UI-SEARCH-SEARCH-QUESTIONS-EVIDENCE-READINGS-AND", lang),
                "search_status": self.t("UI-SEARCH-SEARCH-STATUS", lang), "search_close": self.t("UI-SEARCH-CLOSE", lang),
                "cite": self.t("UI-HEADER-CITE-THIS-PAGE", lang), "report": self.t("UI-HEADER-REPORT-AN-ISSUE", lang),
                "copied": self.t("UI-HEADER-COPIED", lang),
                "lang_switch_name": self.t("UI-LANG-SWITCH-NAME", other), "lang_switch_action": self.t("UI-LANG-SWITCH-ACTION", other),
                "footer_strapline": self.t("UI-FOOTER-STRAPLINE", lang), "footer_rights": self.t("UI-FOOTER-PUBLISHED-EVIDENCE-REMAINS-ATTRIBUTED-TO", lang),
                "footer_nav": self.t("UI-FOOTER-PRODUCT-AND-TRUST-LINKS", lang), "noscript": self.t("UI-NOSCRIPT-NOTE", lang),
                "breadcrumb": self.t("UI-CRUMB-BREADCRUMB", lang), "understand_explore_verify": self.t("UI-DOM-UNDERSTAND-EXPLORE-VERIFY", lang),
            },
            "nav": nav, "trust": trust, "footer": footer, "home_href": self.href("/", lang), "contact_href": self.href("/contact/", lang),
            "ui_json": self.ui_json(lang),
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
            "labels": {"open_source_record": self.t("UI-EVID-OPEN-SOURCE-RECORD", lang), "open_original": self.t("UI-EVID-OPEN-ORIGINAL-SOURCE", lang),
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
        parts = [f"{title}.",
                 self.tf("UI-CITE-RECORD-LINE", lang, product=self.t("UI-PRODUCT-NAME", lang), oid=oid, version=self.t("UI-CONTENT-VERSION", lang)),
                 clause(self.t("UI-CITE-PERIOD", lang), self.loc(obj, "period", lang)),
                 clause(self.t("UI-CITE-POPULATION", lang), self.loc(obj, "universe", lang)),
                 clause(self.t("UI-DOM-WHAT-NOT-TO-CONCLUDE", lang), limitation),
                 clause(self.t("UI-EVID-MEASUREMENT-LIMITS", lang), measure_limit),
                 clause(self.t("UI-CITE-ORIGINAL-SOURCES", lang), ("؛ " if ar else "; ").join(names)),
                 self.t("UI-CITE-PUBLISHERS-AUTHORITATIVE", lang)]
        return " ".join(p for p in parts if p)

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
            "method": "" if obj.get("visual_contract_state") else self.loc(obj, "method", lang),
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
            "citation": self.citation(spec, obj, lang),
            "compare_href": f"/{lang}/evidence/compare/?records={quote(oid)}" if oid in self.compare_ids else "",
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
                "history": L("UI-EVID-CORRECTIONS-RELEASE-HISTORY"), "source_reference": L("UI-SOURCE-REFERENCE"),
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
            "return_to": back, "sources": sources, "related": related,
            "labels": {"eyebrow": L("UI-READING-EYEBROW"), "evidence_period": L("UI-READING-EVIDENCE-PERIOD"), "last_reviewed": L("UI-READING-LAST-REVIEWED"),
                       "do_not_infer": L("UI-READING-DO-NOT-INFER"), "trace": L("UI-READING-TRACE-H"), "trace_intro": L("UI-READING-PATH-INTRO"),
                       "compare": L("UI-READING-TEST-COMPARABILITY-OF-THIS-READING"), "return": L("UI-READING-RETURN"),
                       "related": L("UI-READING-RELATED-H"), "all": L("UI-READING-ALL-H"), "sources": L("UI-SOURCES-SOURCES"),
                       "source_record": L("UI-SOURCES-SOURCE-RECORD"), "reference": L("UI-SOURCE-REFERENCE"),
                       "open_record": L("UI-EVID-OPEN-EVIDENCE-RECORD"), "readings_index_href": self.href("/readings/", lang),
                       "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang]},
        }

    # ------------------------------------------------------------------------------------------------ visuals
    def visual(self, vid: str, lang: str) -> dict:
        v = self.visual_contracts[vid]
        g = v["governed"]
        c = v.get("contract") or {}
        lab = lambda k: self.grammar_labels[k][lang]  # noqa: E731
        out = {
            "id": vid, "tier": v["tier"], "title": g.get(f"title_{lang}"), "question": g.get(f"question_{lang}"),
            "prohibited_inference": g.get(f"prohibited_inference_{lang}"), "alt_text": g.get(f"alt_text_{lang}"),
            "period": g.get(f"period_{lang}"), "universe": g.get(f"universe_{lang}"),
            "canonical_href": self.href(g.get("canonical_route"), lang),
            "detached_caption": v.get(f"detached_caption_{lang}"),
            "labels": {"does_not_establish": lab("UI-VIS-DOES-NOT-ESTABLISH"), "source": lab("UI-VIS-SOURCE"), "full_record": lab("UI-VIS-FULL-RECORD"),
                       "same_year_revision": lab("UI-VIS-SAME-YEAR-REVISION"), "not_comparable": lab("UI-VIS-NOT-COMPARABLE"),
                       "reported": lab("UI-VIS-STATE-REPORTED"), "derived": lab("UI-VIS-STATE-DERIVED"),
                       "analytical_question": self.t("UI-DOM-ANALYTICAL-QUESTION", lang), "what_it_shows": self.t("UI-VIS-WHAT-THE-EVIDENCE-SHOWS", lang),
                       "text_alternative": self.t("UI-DOM-ANALYTICAL-TEXT-ALTERNATIVE", lang), "scope": self.t("UI-DOM-SCOPE-AND-TIME", lang)},
        }
        if c:
            out["form"] = c.get("form")
            out["credit"] = (c.get("credit") or {}).get("text")
            out["frame_labels"] = {k: val.get(lang) for k, val in (c.get("frame_labels") or {}).items()}
            out["series"] = [{"id": s["id"], "state": s.get("state"), "markers": s.get("markers") or [],
                              "values": [{"id": val["id"], "x": val["x"], "y": val["y"], "unit": val["unit_label"][lang], "source": val.get("source"),
                                          "series_label": val["series_label_label"][lang], "state": val.get("grammar_state"), "markers": val.get("markers") or []}
                                         for val in s.get("values") or []]} for s in c.get("series") or []]
            out["derived"] = [{"id": d["id"], "series": d.get("series"), "x": d.get("x"), "value": d.get("value"),
                               "unit": d["unit_label"][lang], "series_label": (d.get("series_label_label") or {}).get(lang), "state": d.get("grammar_state")}
                              for d in c.get("derived") or []]
            out["rules"] = {k: c.get(k) for k in ("ordering", "transformation", "breaks", "annotation", "mobile", "rtl", "fallback")}
        return out

    # ------------------------------------------------------------------------------------------------ home
    def home(self, lang: str) -> dict:
        spec = self.spec_by_route["/"]
        secs = self.sections(spec, lang)
        chosen = ["QE-002", "QE-003", "QE-005", "QE-011"]
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
        return {
            "family": "Orientation", "route": "/", "lang": lang,
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
                       "does_not_establish": self.grammar_labels["UI-VIS-DOES-NOT-ESTABLISH"][lang]},
        }

    # ------------------------------------------------------------------------------------------------ trio
    def trio(self, lang: str) -> dict:
        return {"/": self.home(lang), "/evidence/CLM-003/": self.evidence_record("/evidence/CLM-003/", lang),
                "/readings/same-year-different-number/": self.reading("/readings/same-year-different-number/", lang)}


def load() -> Content:
    return Content()
