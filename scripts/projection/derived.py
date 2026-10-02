# -*- coding: utf-8 -*-
"""Rule builders referenced by projection_manifest.json (rule_id -> function(ctx, entry))."""
import re
from collections import OrderedDict, defaultdict

from . import families as F
from .structure import StructureError


class IntegrityError(StructureError):
    pass


def _unique(records, key, where):
    seen = set()
    for r in records:
        k = r.get(key)
        if k in (None, ""):
            raise IntegrityError(f"{where}: record without stable key {key!r}")
        if k in seen:
            raise IntegrityError(f"{where}: duplicate stable key {key}={k!r}")
        seen.add(k)


# ------------------------------------------------------------------------------------------------
# GENERATED: keyed records and raw snapshots
# ------------------------------------------------------------------------------------------------
def keyed_projection(ctx, e):
    recs = F.keyed(ctx.wb, e["sheet"], ctx.contract, e.get("fields"))
    if e.get("stable_key"):
        _unique(recs, e["stable_key"], e["path"])
    for d in e.get("derived_fields", []):
        for r in recs:
            src = r.get(d["from"])
            if d["rule"] == "route_list_slash":
                r[d["name"]] = [F.slash(x) for x in (src if isinstance(src, list) else [])]
            elif d["rule"] == "route_list_copy":
                r[d["name"]] = list(src) if isinstance(src, list) else []
            elif d["rule"] == "pipe_list":
                r[d["name"]] = F.pipe_list(src)
            elif d["rule"] == "pipe_list_tail":
                r[d["name"]] = F.pipe_list(src)[1:]
            elif d["rule"] == "boundary_head":
                # P4.3: part A of a boundary cell (what the evidence does not establish), before the authored ' | '
                r[d["name"]] = src.split(" | ", 1)[0].strip() if isinstance(src, str) else src
            elif d["rule"] == "boundary_tail":
                # P4.3: part B (the limit of the measure) after the authored ' | ', or None when not recorded
                r[d["name"]] = src.split(" | ", 1)[1].strip() if isinstance(src, str) and " | " in src else None
            else:
                raise StructureError(f"{e['path']}: unknown derived-field rule {d['rule']!r}")
    # P4.3: a boundary cell carries at most one authored delimiter, and both languages carry the same structure
    for en_f, ar_f in e.get("boundary_parity", []):
        bad = [r.get(e.get("stable_key") or "") for r in recs
               if str(r.get(en_f) or "").count(" | ") > 1 or str(r.get(ar_f) or "").count(" | ") > 1
               or (" | " in str(r.get(en_f) or "")) != (" | " in str(r.get(ar_f) or ""))]
        if bad:
            raise IntegrityError(f"{e['path']}: {en_f}/{ar_f} must carry the same A | B structure in both languages: {bad}")
    # fields whose value must be replaced after derivation (e.g. passport route = first route)
    for k, t in (e.get("post_fields") or {}).items():
        for r in recs:
            r[k] = F.TRANSFORMS[t](r[k])
    return recs


# ------------------------------------------------------------------------------------------------
# ONE OWNER PER TEXT (Tranche C / R8.5): Evidence Record text is authored once in 06 and Reading titles once in 08.
# Claims (07), Evidence Record routes (02 title, 03 sections) and Reading routes (02 title) derive from them; the
# derived projections keep their previous shape so every consumer reads the same fields as before.
# ------------------------------------------------------------------------------------------------
EVIDENCE_GUIDANCE_UI = ("UI-EVID-READING-GUIDANCE-H", "UI-EVID-READING-GUIDANCE")


def _evidence_route(object_id):
    return f"/evidence/{object_id}/"


def public_claims(ctx, e):
    """07 holds only claim metadata (theme, type, badge, inputs, routes). Headline, copy, boundary and change trigger
    are the claim's Evidence Record fields in 06 (title, summary, does-not-establish, change trigger)."""
    recs = keyed_projection(ctx, e)
    eo = OrderedDict((o["object_id"], o) for o in ctx.out["evidence/evidence_objects.json"])
    out = []
    for r in recs:
        o = eo.get(r["claim_id"])
        if o is None:
            raise IntegrityError(f"07 claim {r['claim_id']} has no Evidence Record in 06 (the claim's text lives there)")
        out.append(OrderedDict([
            ("claim_id", r["claim_id"]), ("theme", r["theme"]), ("claim_type", r["claim_type"]),
            ("headline_en", o["title_en"]), ("headline_ar", o["title_ar"]), ("copy_en", o["summary_en"]), ("copy_ar", o["summary_ar"]),
            ("evidence_badge", r["evidence_badge"]), ("evidence_inputs", r["evidence_inputs"]),
            ("does_not_prove_en", o["does_not_establish_en"]), ("does_not_prove_ar", o["does_not_establish_ar"]),
            ("change_trigger_en", o["change_trigger_en"]), ("change_trigger_ar", o["change_trigger_ar"]),
            ("public_routes", r["public_routes"]), ("public_route_list", r["public_route_list"]),
        ]))
    return out


def page_sections(ctx, e):
    """03 sections of every route except Evidence Record routes, whose two sections are derived: section 1 is the
    record's governed summary (06) and section 2 the governed reading guidance (04 interface copy)."""
    recs = keyed_projection(ctx, e)
    ev_routes = {_evidence_route(o["object_id"]) for o in ctx.out["evidence/evidence_objects.json"]}
    held = sorted({r["route"] for r in recs if r["route"] in ev_routes})
    if held:
        raise IntegrityError(f"03 holds sections for Evidence Record routes {held[:5]}: those sections derive from 06 and 04")
    ui = {x["ui_id"]: x for x in ctx.out["content/interface_copy.json"]}
    missing = [k for k in EVIDENCE_GUIDANCE_UI if k not in ui]
    if missing:
        raise IntegrityError(f"interface copy lacks {missing}")
    h, b = (ui[k] for k in EVIDENCE_GUIDANCE_UI)
    for o in ctx.out["evidence/evidence_objects.json"]:
        route = _evidence_route(o["object_id"])
        recs.append(OrderedDict([("route", route), ("section_order", 1), ("section_role", None), ("heading_en", None),
                                 ("body_en", o["summary_en"]), ("heading_ar", None), ("body_ar", o["summary_ar"])]))
        recs.append(OrderedDict([("route", route), ("section_order", 2), ("section_role", "How to read this evidence"),
                                 ("heading_en", h["label_en"]), ("body_en", b["label_en"]), ("heading_ar", h["label_ar"]), ("body_ar", b["label_ar"])]))
    return recs


def _full_copy(title, secs, lang):
    ordered = sorted(secs, key=lambda s: s["section_order"] if isinstance(s.get("section_order"), (int, float)) else 0)
    return "\n\n".join([title or ""] + [v for s in ordered for v in (s.get("heading_" + lang), s.get("body_" + lang)) if v])


def site_map(ctx, e):
    """02 is the route registry. Evidence Record and Reading routes take their title from 06 / 08 (their 02 title cells
    must be blank); full copy is derived (title + sections) and is no longer stored in the Master."""
    recs = keyed_projection(ctx, e)
    eo = {o["object_id"]: o for o in ctx.out["evidence/evidence_objects.json"]}
    rd = {F.slash(r["route"]): r for r in ctx.out["content/readings.json"]}
    secs = defaultdict(list)
    for s in ctx.out["content/page_sections.json"]:
        secs[s["route"]].append(s)
    out = []
    for r in recs:
        route, cls = r["route"], r["page_class"]
        owner = eo.get(r.get("instance_id")) if cls == "evidence_detail" else rd.get(route) if cls == "reading_detail" else None
        if cls in ("evidence_detail", "reading_detail"):
            if owner is None:
                raise IntegrityError(f"02 {route}: no owning {'Evidence Record' if cls == 'evidence_detail' else 'Reading'}")
            if r.get("title_en") or r.get("title_ar"):
                raise IntegrityError(f"02 {route}: title must be blank; it derives from {'06' if cls == 'evidence_detail' else '08'}")
            t_en, t_ar = owner["title_en"], owner["title_ar"]
        else:
            t_en, t_ar = r.get("title_en"), r.get("title_ar")
            if not (t_en and t_ar):
                raise IntegrityError(f"02 {route}: title missing")
        out.append(OrderedDict([
            ("route", route), ("page_class", cls), ("template_route", r["template_route"]), ("instance_id", r.get("instance_id")),
            ("title_en", t_en), ("title_ar", t_ar),
            ("full_copy_en", _full_copy(t_en, secs.get(route, []), "en")), ("full_copy_ar", _full_copy(t_ar, secs.get(route, []), "ar")),
            ("meta_description_en", r.get("meta_description_en")), ("meta_description_ar", r.get("meta_description_ar")),
        ]))
    return out


def raw_snapshot(ctx, e):
    return F.snapshot(ctx.wb, e["sheet"], ctx.contract)


def local_data_index(ctx, e):
    out = []
    for o in ctx.manifest["outputs"]:
        if o["rule_id"] == "raw_snapshot" and o["path"].startswith("data/"):
            snap = ctx.out[o["path"]]
            out.append(OrderedDict([("file", o["path"]), ("source_sheet", o["sheet"]), ("rows", len(snap["rows"]) - 1)]))
    return out


def local_dataset_catalog(ctx, e):
    tmpl = ctx.inputs["local_dataset_catalog_template"]["datasets"]
    out = []
    for t in tmpl:
        snap = ctx.out.get(t["file"])
        if snap is None:
            raise StructureError(f"{e['path']}: template references unknown local file {t['file']}")
        rec = OrderedDict()
        for k in ("dataset_id", "file", "domain"):
            rec[k] = t[k]
        rec["record_rows"] = len(snap["rows"]) - 1
        for k in ("runtime_role", "future_adapter_rule"):
            rec[k] = t[k]
        out.append(rec)
    return out


# ------------------------------------------------------------------------------------------------
# DERIVED: legacy object-source closure (entry rule, reconstructed; superseded by PB-0002 in Stage 1)
# ------------------------------------------------------------------------------------------------
def _split_multi(v):
    return [x.strip() for x in re.split(r"[;,|]", v) if x.strip()] if isinstance(v, str) else []


class _Lineage:
    """Token resolution tables built from the Master (15 source library, 16 dataset catalog)."""

    def __init__(self, ctx):
        self.lib = OrderedDict((r["source_id"], r) for r in ctx.out["sources/source_library.json"])
        cat = ctx.out["sources/master_dataset_catalog.json"]
        self.ds_ids = [r["dataset_id"] for r in cat]
        self.origin = OrderedDict((r["origin_table"], r["dataset_id"]) for r in cat if r.get("origin_table"))
        self.by_name = defaultdict(list)          # dataset id OR origin-table name -> source ids (15.datasets_or_use)
        for sid, r in self.lib.items():
            for d in _split_multi(r.get("datasets_or_use")):
                if sid not in self.by_name[d]:
                    self.by_name[d].append(sid)
        for r in cat:                             # 16.sample_source_ids that are real source IDs
            for d in _split_multi(r.get("sample_source_ids")):
                if d in self.lib and d not in self.by_name[r["dataset_id"]]:
                    self.by_name[r["dataset_id"]].append(d)

    def dataset_sources(self, token):
        """(matched, sources) for a dataset-id, origin-table or numeric-prefix token."""
        if token in self.ds_ids:
            return True, list(self.by_name.get(token, []))
        if token in self.origin:
            out = list(self.by_name.get(self.origin[token], []))
            for s in self.by_name.get(token, []):
                if s not in out:
                    out.append(s)
            return True, out
        if token.isdigit():
            ot = next((o for o in self.origin if o.startswith(token + "_")), None)
            if ot:
                return True, list(self.by_name.get(self.origin[ot], []))
        return False, []


_ID_WORD = re.compile(r"[A-Z0-9][A-Z0-9_.\-]*")


def _lineage_token(part):
    """A dependency segment is an identifier token. A segment containing whitespace contributes its first
    word only when that word is an identifier (upper-case/digits with '_' or '-', at least one letter);
    prose segments contribute nothing."""
    part = part.strip()
    if not part:
        return None
    if not re.search(r"\s", part):
        return part if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.\-]*", part) else None
    w = part.split()[0]
    if _ID_WORD.fullmatch(w) and re.search(r"[A-Z]", w) and re.search(r"[_\-]", w):
        return w
    return None


def _dependencies(kind, rec):
    if kind == "public_claim":
        deps = list(rec.get("evidence_inputs") or [])
        if rec["claim_id"] not in deps:
            deps.append(rec["claim_id"])
        return deps
    if kind == "reading":
        deps = []
        for x in list(rec.get("source_bindings") or []) + list(rec.get("evidence_bindings") or []):
            if x not in deps:
                deps.append(x)
        return deps
    if kind == "visual":                                    # identifiers only: prose phrases are not lineage tokens
        v = rec.get("data_inputs")
        return [t for t in (_lineage_token(x) for x in v.split("+")) if t] if isinstance(v, str) else []
    return []


def object_source_closure_legacy(ctx, e):
    """Entry (pre-Stage-1) rule, kept for the historical baseline gate only; not referenced by the manifest."""
    tmpl = ctx.inputs["closure_templates"]
    L = _Lineage(ctx)
    meta = _source_metadata_states(ctx)
    raw06 = OrderedDict((r["object_id"], r) for _, r in __import__("projection.structure", fromlist=["x"]).keyed_records(ctx.wb.grid("06_EVIDENCE_OBJECTS"), "06_EVIDENCE_OBJECTS"))
    eo = ctx.out["evidence/evidence_objects.json"]
    claims = ctx.out["evidence/public_claims.json"]
    readings = ctx.out["content/readings.json"]
    visuals = ctx.out["visuals/visual_library.json"]
    measures = ctx.out["content/measurement_agenda.json"]
    done = {}
    out = []

    def resolve(kind, oid, deps):
        direct = sorted({d for d in deps if d in L.lib})
        via, via_res, unres = [], set(), []
        for d in deps:
            if d in L.lib:
                continue
            if d in done.get("evidence_object", {}) and not (kind == "evidence_object" and d == oid):
                rr = done["evidence_object"][d]
                if rr["resolved_source_ids"]:
                    via.append(d); via_res |= set(rr["resolved_source_ids"]); unres += rr["unresolved_dependency_ids"]
                continue
            if d in done.get("reading", {}):
                rr = done["reading"][d]
                if rr["resolved_source_ids"]:
                    via.append(d); via_res |= set(rr["resolved_source_ids"]); unres += rr["unresolved_dependency_ids"]
                continue
            matched, s = L.dataset_sources(d)
            if matched and s:
                via.append(d); via_res |= set(s)
            else:
                unres.append(d)
        resolved = sorted(via_res) + [d for d in direct if d not in via_res]
        if not deps:
            state = tmpl["closure_states"]["none"]
        elif direct:
            state = tmpl["closure_states"]["direct"]
        elif via:
            state = tmpl["closure_states"]["via"]
        else:
            state = tmpl["closure_states"]["unresolved"]
        return OrderedDict([("dependency_ids", deps), ("direct_source_ids", direct), ("resolved_source_ids", resolved),
                            ("resolved_via_object_ids", sorted(set(via))), ("unresolved_dependency_ids", sorted(set(unres))),
                            ("source_locators", [OrderedDict([("source_id", s), ("primary_url", L.lib[s].get("primary_url")), ("metadata_state", meta[s])]) for s in resolved if s in L.lib]),
                            ("closure_state", state), ("rule", tmpl["rule"])])

    def emit(kind, oid, routes, deps):
        body = resolve(kind, oid, deps)
        rec = OrderedDict([("object_type", kind), ("object_id", oid), ("public_routes", routes)])
        rec.update(body)
        done.setdefault(kind, {})[oid] = rec
        out.append(rec)

    for r in eo:
        raw = raw06[r["object_id"]]
        deps = [t for t in (_lineage_token(x) for x in (raw.get("source_dependencies") or "").split(";")) if t]
        for link in (r.get("source_links") or []):            # declared dependencies, then source-link IDs
            sid = link.get("source_id") if isinstance(link, dict) else link
            if sid and sid not in deps:
                deps.append(sid)
        emit("evidence_object", r["object_id"], [F.slash(x) for x in F.pipe_list(raw.get("public_routes"))], deps)
    for r in claims:
        emit("public_claim", r["claim_id"], r["public_route_list"], _dependencies("public_claim", r))
    for r in readings:
        emit("reading", r["reading_id"], [r["route"]], _dependencies("reading", r))
    reading_ids = {r["reading_id"] for r in readings}
    for r in visuals:
        deps = _dependencies("visual", r)
        rid_ = r["visual_id"][3:] if r["visual_id"].startswith("RV-") else None
        if rid_ in reading_ids and rid_ not in deps:            # a Reading's own visual depends on the Reading
            deps.append(rid_)
        emit("visual", r["visual_id"], [F.slash(x) for x in (r.get("public_routes") or [])], deps)
    for r in measures:
        emit("measurement", r["measurement_id"], r["affected_route_list"], [])
    return out


# ------------------------------------------------------------------------------------------------
# DERIVED: object-source closure — rule v2 (Tranche B Stage 1, PB-0001…PB-0005)
# ------------------------------------------------------------------------------------------------
def _context_ids(ctx, tmpl):
    ids = set()
    for sheet in tmpl["context_reference_sheets"]:
        for r in ctx.wb.grid(sheet):
            if r and isinstance(r[0], str) and r[0].strip():
                ids.add(r[0].strip())
    return ids


def object_source_closure(ctx, e):
    from .structure import keyed_records
    tmpl = ctx.inputs["closure_templates"]
    CS = tmpl["closure_states"]
    L = _Lineage(ctx)
    meta = _source_metadata_states(ctx)
    raw06 = OrderedDict((r["object_id"], r) for _, r in keyed_records(ctx.wb.grid("06_EVIDENCE_OBJECTS"), "06_EVIDENCE_OBJECTS"))
    ctx_ids = _context_ids(ctx, tmpl)
    pats = [re.compile(p) for p in tmpl["context_reference_patterns"]]
    ui = {r["ui_id"]: r for r in ctx.out["content/interface_copy.json"]}
    problems = []

    def classify(t):
        if t in L.lib:
            return "SOURCE"
        if t.startswith(tmpl["open_input_prefix"]):
            return "OPEN"
        if t in raw06:
            return "MEMBER"
        if t in ctx_ids or any(p.match(t) for p in pats):
            return "CONTEXT"
        return "OPEN"                                   # dataset-level token or unrecognised: never expanded

    def locators(srcs):
        return [OrderedDict([("source_id", s), ("primary_url", L.lib[s].get("primary_url")), ("metadata_state", meta[s])]) for s in srcs]

    def record(kind, oid, routes, deps, state_key, lineage_state, bound, members, context, open_, lineage_from=None):
        rec = OrderedDict([("object_type", kind), ("object_id", oid), ("public_routes", routes), ("lineage_state", lineage_state),
                           ("dependency_ids", deps), ("direct_source_ids", list(bound)), ("resolved_source_ids", list(bound)),
                           ("resolved_via_object_ids", list(members)), ("context_reference_ids", list(context)),
                           ("unresolved_dependency_ids", list(open_)), ("source_locators", locators(bound)),
                           ("closure_state", CS[state_key]), ("rule", tmpl["rule"])])
        if lineage_from:
            rec["lineage_from"] = lineage_from
        return rec

    out, eo_clo = [], OrderedDict()
    for oid, raw in raw06.items():
        deps = F.TRANSFORMS["semicolon_list"](raw.get("source_dependencies"))
        state = raw.get("lineage_state")
        if state not in tmpl["lineage_states"]:
            problems.append(f"{oid}: lineage_state {state!r} not in controlled vocabulary")
            continue
        cls = OrderedDict((t, classify(t)) for t in deps)
        bound = [t for t, c in cls.items() if c == "SOURCE"]
        members = [t for t, c in cls.items() if c == "MEMBER"]
        context = [t for t, c in cls.items() if c == "CONTEXT"]
        open_ = [t for t, c in cls.items() if c == "OPEN"]
        ok = {"BOUND_EXACT": bool(bound) and not open_ and not members,
              "BOUND_PARTIAL": bool(bound) and bool(open_),
              "COMPOSITE_OF_OBJECTS": not bound and not open_,
              "SOURCE_NOT_YET_BOUND": not bound and not members,
              "FRAMING_NO_FACT": not bound and not open_ and not members}[state]
        if not ok:
            problems.append(f"{oid}: lineage_state {state} disagrees with dependency classes {dict(cls)}")
            continue
        key = "COMPOSITE_UNLISTED" if state == "COMPOSITE_OF_OBJECTS" and not members else state
        # Pre-Tranche-C P4 (V-D1): a record bound only to sources without a public locator lists no source on its page; its
        # verification text says so, and it may not print a figure (a number other than a year) taken from that material.
        tkey = key
        if state == "BOUND_EXACT" and bound and not any(str(L.lib[b].get("primary_url") or "").strip().lower().startswith(("http://", "https://")) for b in bound):
            tkey = "BOUND_UNLISTED"
            for fld in ("title", "summary", "definition", "method", "limitations", "currentness"):
                for lang in ("en", "ar"):
                    txt = re.sub(r"(?<!\d)(?:19|20)\d\d(?!\d)", "", str(raw.get(f"{fld}_{lang}") or ""))
                    if re.search(r"\d", txt):
                        problems.append(f"{oid}: {fld}_{lang} prints a figure although every bound source lacks a public locator")
        if oid not in tmpl["verification_template_exceptions"]:
            u = ui.get(tmpl["verification_templates"][tkey])
            if not u or raw.get("verification_en") != u["label_en"] or raw.get("verification_ar") != u["label_ar"]:
                problems.append(f"{oid}: 06 verification text is not the governed template {tmpl['verification_templates'][tkey]}")
        rec = record("evidence_object", oid, [F.slash(x) for x in F.pipe_list(raw.get("public_routes"))], deps, key, state, bound, members, context, open_)
        eo_clo[oid] = rec
        out.append(rec)
    if problems:
        raise IntegrityError("object-source closure v2:\n  " + "\n  ".join(problems))

    def mirror(kind, oid, routes, deps, src):
        return record(kind, oid, routes, deps, next(k for k, v in CS.items() if v == src["closure_state"] and not k.startswith(("reading", "measurement"))),
                      src["lineage_state"], src["resolved_source_ids"], src["resolved_via_object_ids"], src["context_reference_ids"],
                      src["unresolved_dependency_ids"], lineage_from=src["object_id"])

    for r in ctx.out["evidence/public_claims.json"]:
        deps = list(r.get("evidence_inputs") or [])
        if r["claim_id"] not in deps:
            deps.append(r["claim_id"])
        src = eo_clo.get(r["claim_id"])
        if src is None:
            raise IntegrityError(f"claim {r['claim_id']}: no 06 evidence record carries its lineage")
        out.append(mirror("public_claim", r["claim_id"], r["public_route_list"], deps, src))
    rd_clo = OrderedDict()
    for r in ctx.out["content/readings.json"]:
        deps = []
        for x in list(r.get("source_bindings") or []) + list(r.get("evidence_bindings") or []):
            if x not in deps:
                deps.append(x)
        cls = OrderedDict((d, classify(d)) for d in deps)
        direct = [d for d, c in cls.items() if c == "SOURCE"]
        members = [d for d, c in cls.items() if c == "MEMBER"]
        context = [d for d, c in cls.items() if c == "CONTEXT"]
        resolved = list(direct)
        open_ = [d for d, c in cls.items() if c == "OPEN"]
        for m in members:
            c = eo_clo[m]
            for s in c["resolved_source_ids"]:
                if s not in resolved:
                    resolved.append(s)
            if c["closure_state"] not in tmpl["closed_states"]:
                open_.append(m)
        key = "reading_partial" if open_ else ("reading_closed" if resolved else "reading_unbound")
        rec = OrderedDict([("object_type", "reading"), ("object_id", r["reading_id"]), ("public_routes", [r["route"]]), ("lineage_state", None),
                           ("dependency_ids", deps), ("direct_source_ids", direct), ("resolved_source_ids", resolved),
                           ("resolved_via_object_ids", members), ("context_reference_ids", context), ("unresolved_dependency_ids", open_),
                           ("source_locators", locators(resolved)), ("closure_state", CS[key]), ("rule", tmpl["rule"])])
        rd_clo[r["reading_id"]] = rec
        out.append(rec)
    for r in ctx.out["visuals/visual_library.json"]:
        vid = r["visual_id"]
        routes = [F.slash(x) for x in (r.get("public_routes") or [])]
        deps = _dependencies("visual", r)
        if vid in eo_clo:
            out.append(mirror("visual", vid, routes, deps, eo_clo[vid]))
        elif vid.startswith("RV-") and vid[3:] in rd_clo:
            src = rd_clo[vid[3:]]
            rec = OrderedDict(src)
            rec.update([("object_type", "visual"), ("object_id", vid), ("public_routes", routes), ("dependency_ids", deps)])
            rec["lineage_from"] = src["object_id"]
            out.append(rec)
        else:
            # A contract with no 06 record of its own: its data_inputs name member records, or it is an unlisted composite.
            members = [d for d in deps if d in eo_clo]
            other = [d for d in deps if d not in eo_clo]
            if other:
                out.append(record("visual", vid, routes, deps, "SOURCE_NOT_YET_BOUND", "SOURCE_NOT_YET_BOUND", [], [], [], other))
            else:
                out.append(record("visual", vid, routes, deps, "COMPOSITE_OF_OBJECTS" if members else "COMPOSITE_UNLISTED",
                                  "COMPOSITE_OF_OBJECTS", [], members, [], []))
    for r in ctx.out["content/measurement_agenda.json"]:
        out.append(OrderedDict([("object_type", "measurement"), ("object_id", r["measurement_id"]), ("public_routes", r["affected_route_list"]),
                                ("lineage_state", None), ("dependency_ids", []), ("direct_source_ids", []), ("resolved_source_ids", []),
                                ("resolved_via_object_ids", []), ("context_reference_ids", []), ("unresolved_dependency_ids", []),
                                ("source_locators", []), ("closure_state", CS["measurement"]), ("rule", tmpl["rule"])]))
    return out


def _source_metadata_states(ctx):
    rule = ctx.inputs["closure_templates"]["metadata_state_rule"]
    out = OrderedDict()
    for r in ctx.out["sources/source_library.json"]:
        out[r["source_id"]] = rule["display_ready"] if r.get(rule["field"]) in rule["display_ready_values"] else rule["otherwise"]
    return out


# ------------------------------------------------------------------------------------------------
# DERIVED: source reference map (15_SOURCE_LIBRARY + closure links)
# ------------------------------------------------------------------------------------------------
SRC_DISPLAY_FIELDS = ["display_title", "display_title_ar", "publisher", "publisher_ar", "document_label", "document_label_ar",
                      "document_date", "resource_category", "resource_category_ar",
                      "why_it_matters", "why_it_matters_ar", "does_not_establish", "does_not_establish_ar"]
CURATED_CARD_STATE = "FULL_PUBLIC_CARD"      # Tranche C TC-B: curated resource card; CITATION_CARD = governed bibliography only
LINK_FIELDS = [("evidence_object", "linked_evidence_object_ids"), ("public_claim", "linked_claim_ids"), ("reading", "linked_reading_ids"),
               ("visual", "linked_visual_ids"), ("measurement", "linked_measurement_ids")]


def source_reference_map(ctx, e):
    t = ctx.inputs["source_reference_templates"]
    meta = _source_metadata_states(ctx)
    clo = ctx.out["sources/public_object_source_closure.json"]
    links = defaultdict(lambda: defaultdict(set))
    for c in clo:
        for s in c["resolved_source_ids"]:
            links[s][c["object_type"]].add(c["object_id"])
    out = []
    for r in ctx.out["sources/source_library.json"]:
        sid = r["source_id"]
        ready = meta[sid] == ctx.inputs["closure_templates"]["metadata_state_rule"]["display_ready"]
        curated = ready and r.get("public_card_state") == CURATED_CARD_STATE
        rec = OrderedDict([("source_id", sid), ("primary_url", r.get("primary_url")), ("additional_urls", r.get("additional_urls")),
                           ("datasets_or_use", r.get("datasets_or_use")), ("row_count", r.get("row_count")),
                           ("metadata_state", meta[sid]), ("standalone_resource_card_eligible", curated)])
        for f in SRC_DISPLAY_FIELDS:
            rec[f] = r.get(f) if ready else None
        rec["rights_state"] = r.get("rights_state")               # PB-0390: NOT_ASSESSED = locator for citation/verification only
        rec["document_type"] = r.get("document_type")
        rec["evidence_roles"] = r.get("evidence_roles")
        rec["rights_display_state"] = t["rights_display_state"]
        rec["citation_behavior"] = t["citation_behavior"]
        for kind, field in LINK_FIELDS:
            rec[field] = sorted(links[sid][kind])
        rec["rule"] = t["rule"]
        out.append(rec)
    return out


# ------------------------------------------------------------------------------------------------
# Public inventory count contract (Pre-Tranche-C P1.2): repository counts are derived, never typed
# ------------------------------------------------------------------------------------------------
def _inventory_contract(ctx):
    return ctx.inputs["public_inventory_contract"]


def _inventory_count(ctx, key):
    spec = _inventory_contract(ctx)["counts"].get(key)
    if spec is None:
        raise IntegrityError(f"public inventory: unknown count key {key!r}")
    obj = ctx.out.get(spec["projection"])
    if obj is None:
        raise IntegrityError(f"public inventory: {key} needs {spec['projection']}, which is not generated yet at this point")
    rule = spec["rule"]
    if rule == "count_records":
        return len(obj)
    if rule == "count_where_http_primary_url":
        return sum(1 for r in obj if str(r.get(spec["field"]) or "").strip().lower().startswith(("http://", "https://")))
    if rule == "count_where_true":
        return sum(1 for r in obj if r.get(spec["field"]) is True)
    if rule == "count_where_not_in":   # release candidate RC-2: a count that follows its own definition (e.g. dated events only)
        return sum(1 for r in obj if r.get(spec["field"]) not in spec["exclude"])
    if rule == "spec_count":
        return obj["spec_count"]
    raise StructureError(f"public inventory: unknown rule {rule!r} for {key}")


def resolve_inventory_tokens(ctx, text, where):
    """Replace {{n:key}} with the derived count. Returns (text, [(key, value), ...]).
    Raises on an unknown key, a key not cleared for public display, or any template token left unresolved."""
    if not isinstance(text, str):
        return text, []
    c = _inventory_contract(ctx)
    used = []

    def sub(m):
        k = m.group(1)
        spec = c["counts"].get(k)
        if spec is None or not spec.get("public_token"):
            raise IntegrityError(f"{where}: inventory token {{{{n:{k}}}}} is unknown or not cleared for public display")
        v = _inventory_count(ctx, k)
        used.append((k, v))
        return format(v, ",")

    out = re.sub(c["token_pattern"], sub, text) if "{{" in text else text
    if re.search(c["unresolved_token_pattern"], out):
        raise IntegrityError(f"{where}: unresolved template token {re.search(c['unresolved_token_pattern'], out).group(0)!r}")
    return out, used


def public_inventory(ctx, e):
    c = _inventory_contract(ctx)
    counts = []
    for k, spec in c["counts"].items():
        counts.append(OrderedDict([("key", k), ("value", _inventory_count(ctx, k)), ("projection", spec["projection"]), ("rule", spec["rule"]),
                                   ("public_token", bool(spec.get("public_token"))), ("definition_en", spec.get("definition_en"))]))
    return OrderedDict([("schema_version", c["schema_version"]), ("contract_id", c["contract_id"]), ("authority_master_sha256", ctx.master_sha256),
                        ("rule", c["rule"]), ("token_pattern", c["token_pattern"]), ("unresolved_token_pattern", c["unresolved_token_pattern"]),
                        ("number_format", c["number_format"]), ("counts", counts)])


# ------------------------------------------------------------------------------------------------
# DERIVED: bilingual search index
# ------------------------------------------------------------------------------------------------
def _ws(t):
    return re.sub(r"\s+", " ", t or "").strip()


def search_index(ctx, e):
    t = ctx.inputs["search_templates"]
    out = []
    for r in ctx.out["content/site_map.json"]:
        rec = OrderedDict([("id", r["route"]), ("type", "page"), ("route", r["route"]), ("title_en", r["title_en"]), ("title_ar", r["title_ar"])])
        base = {L: _ws(resolve_inventory_tokens(ctx, r["full_copy_" + L], f"search record {r['route']} {L}")[0]) for L in ("en", "ar")}
        for L in ("en", "ar"):                               # Tranche C (EN-34): the summary does not repeat the title
            ttl = _ws(r["title_" + L] or "")
            body = base[L][len(ttl):].strip() if ttl and base[L].startswith(ttl) else base[L]
            rec["summary_" + L] = body[: t["page_summary_chars"]]
        rec["search_text_en"] = base["en"]
        rec["search_text_ar"] = base["ar"]
        out.append(rec)
    for q in ctx.out["content/questions.json"]:              # Tranche C (JRN-05): a typed governed question finds its answer page
        route = "/" + str(q["primary_route"]).strip("/") + "/" if str(q["primary_route"]).strip("/") else "/"
        rec = OrderedDict([("id", q["question_id"]), ("type", "question"), ("route", route), ("title_en", q["question_en"]), ("title_ar", q["question_ar"]),
                           ("summary_en", _ws(q.get("user_gets_en") or "")), ("summary_ar", _ws(q.get("user_gets_ar") or "")),
                           ("search_text_en", _ws(q["question_en"] + " " + (q.get("user_gets_en") or ""))),
                           ("search_text_ar", _ws(q["question_ar"] + " " + (q.get("user_gets_ar") or "")))])
        out.append(rec)
    ev_fields = t["evidence_search_fields"]
    claims = {c["claim_id"]: c for c in ctx.out["evidence/public_claims.json"]}
    for o in ctx.out["evidence/evidence_objects.json"]:
        rec = OrderedDict([("id", o["object_id"]), ("type", "evidence"), ("route", t["evidence_route"].format(id=o["object_id"])),
                           ("title_en", o["title_en"]), ("title_ar", o["title_ar"]),
                           ("summary_en", _ws(o["summary_en"])), ("summary_ar", _ws(o["summary_ar"]))])
        for L in ("en", "ar"):
            rec["search_text_" + L] = _ws(" ".join(o.get(f + "_" + L) or "" for f in ev_fields))
        cl = claims.get(o["object_id"], {})
        for L in ("en", "ar"):                               # PB-0491: boundary text, indexed as a separate low-weight field
            rec["boundary_text_" + L] = _ws(" ".join(x for x in (o.get("limitations_" + L), cl.get("does_not_prove_" + L)) if x))
            rec["meta_" + L] = _ws(o.get("period_" + L) or "")    # PB-0493(c): result card shows the evidence period
        rec["lineage_state"] = o.get("lineage_state")
        out.append(rec)
    for o in ctx.out["content/readings.json"]:
        rec = OrderedDict([("id", o["reading_id"]), ("type", "reading"), ("route", o["route"]), ("title_en", o["title_en"]), ("title_ar", o["title_ar"]),
                           ("summary_en", o["thesis_en"]), ("summary_ar", o["thesis_ar"]),
                           ("search_text_en", _ws(o["question_en"] + " " + o["thesis_en"])), ("search_text_ar", _ws(o["question_ar"] + " " + o["thesis_ar"]))])
        out.append(rec)
    ma_fields = t["measurement_search_fields"]
    for o in ctx.out["content/measurement_agenda.json"]:
        rec = OrderedDict([("id", o["measurement_id"]), ("type", "measurement"), ("route", t["measurement_route"].format(id=o["measurement_id"])), ("title_en", o["title_en"]), ("title_ar", o["title_ar"]),
                           ("summary_en", _ws(o["missing_evidence_en"])), ("summary_ar", _ws(o["missing_evidence_ar"]))])
        for L in ("en", "ar"):
            rec["search_text_" + L] = _ws(" ".join(str(o.get(f + "_" + L) or "") for f in ma_fields))
        out.append(rec)
    for s in ctx.out["sources/source_reference_map.json"]:
        if not str(s.get("primary_url") or "").strip().lower().startswith(("http://", "https://")):
            continue                                    # only an http(s) URL is a public original locator
        sid = s["source_id"]
        if s["standalone_resource_card_eligible"]:
            rec = OrderedDict([("id", sid), ("type", "source"), ("route", t["source_route"].format(id=sid)),
                               ("title_en", s["display_title"]), ("title_ar", s["display_title_ar"]),
                               ("summary_en", s["why_it_matters"]), ("summary_ar", s["why_it_matters_ar"]),
                               ("search_text_en", s["why_it_matters"]), ("search_text_ar", s["why_it_matters_ar"])])
        elif s["metadata_state"] == "DISPLAY_READY":       # Tranche C TC-B: a citation card is named by its governed title
            kind_en = " · ".join(x for x in (s.get("publisher"), s.get("document_label")) if x)
            kind_ar = " · ".join(x for x in (s.get("publisher_ar") or s.get("publisher"), s.get("document_label_ar")) if x)
            rec = OrderedDict([("id", sid), ("type", "source"), ("route", t["source_route"].format(id=sid)),
                               ("title_en", s["display_title"]), ("title_ar", s["display_title_ar"]),
                               ("summary_en", kind_en), ("summary_ar", kind_ar),
                               ("search_text_en", kind_en), ("search_text_ar", kind_ar)])
        else:
            loc = t["source_locator"]
            rec = OrderedDict([("id", sid), ("type", "source_locator"), ("route", t["source_route"].format(id=sid)),
                               ("title_en", loc["title_en"].format(id=sid)), ("title_ar", loc["title_ar"].format(id=sid)),
                               ("summary_en", loc["summary_en"]), ("summary_ar", loc["summary_ar"]),
                               ("search_text_en", loc["summary_en"]), ("search_text_ar", loc["summary_ar"])])
        if s.get("document_type"):                           # PB-0493(b/c): document kind where the Master states it
            rec["document_type"] = s["document_type"]
            rec["search_text_en"] = _ws(rec["search_text_en"] + " " + s["document_type"])
        for L in ("en", "ar"):                               # Tranche C (TOOL-10): the result card shows the kind of document in the reader's language
            lab = s.get("document_label" + ("_ar" if L == "ar" else ""))
            date = str(s.get("document_date") or "")
            meta = " · ".join(x for x in (lab, date) if x)
            if meta:
                rec["meta_" + L] = meta
                rec["search_text_" + L] = _ws(rec["search_text_" + L] + " " + (lab or ""))
        out.append(rec)
    return out


# ------------------------------------------------------------------------------------------------
# DERIVED: Page Specs (join of governed projections + declared design bindings)
# ------------------------------------------------------------------------------------------------
def _page_slug(route):
    s = route.strip("/").replace("/", "__")
    return s or "home"


def _page_sort_key(route, routes):
    s = route.strip("/")
    if not s:
        return "home"
    if any(x != route and x.startswith(route) for x in routes):
        return s + "/index"
    return s


def _page_bindings(route, page_class, instance_id, ctx, overrides):
    b = OrderedDict()
    b["claim_ids"] = [c["claim_id"] for c in ctx.out["evidence/public_claims.json"] if route in c["public_route_list"]]
    raw06 = ctx._raw06
    e = [oid for oid, raw in raw06.items() if route in [F.slash(x) for x in F.pipe_list(raw.get("public_routes"))]]
    if page_class == "evidence_detail":
        if instance_id not in raw06:
            raise IntegrityError(f"page {route}: instance {instance_id!r} is not an evidence object")
        if instance_id not in e:
            e = [instance_id] + e
    b["evidence_object_ids"] = e
    b["visual_ids"] = [v["visual_id"] for v in ctx.out["visuals/visual_library.json"] if route in [F.slash(x) for x in (v.get("public_routes") or [])]]
    if page_class == "evidence_detail" and instance_id not in b["visual_ids"] and any(v["visual_id"] == instance_id for v in ctx.out["visuals/visual_library.json"]):
        b["visual_ids"] = [instance_id] + b["visual_ids"]           # PB-0402: a contract reaches its own evidence page
    b["measurement_ids"] = [m["measurement_id"] for m in ctx.out["content/measurement_agenda.json"] if route in m["affected_route_list"]]
    rds = ctx.out["content/readings.json"]
    b["reading_ids"] = [r["reading_id"] for r in rds] if route == "/readings/" else \
        [r["reading_id"] for r in rds if r["route"] == route or route in [F.slash(x) for x in (r.get("domain_surface_routes") or [])]]
    ov = overrides.get(route)
    if ov:
        if ov.get("evidence_object_ids") == "SAME_AS_CLAIM_IDS":
            b["evidence_object_ids"] = list(b["claim_ids"])
        else:
            raise StructureError(f"page {route}: unknown override {ov}")
    return b


_SENT_END = re.compile(r"(?<=[.!?؟])\s+")


def _meta_description(title, secs, lang, limit=155):
    """PB-0411 default: title + first sentence of the first section that has a body in that language, <= 155 characters."""
    body = next((s.get("body_" + lang) for s in secs if s.get("body_" + lang)), "") or ""
    first = _SENT_END.split(_ws(body), 1)[0] if body else ""
    text = f"{title} — {first}" if first else (title or "")
    if len(text) > limit:
        cut = text[: limit - 1]
        if " " in cut:
            cut = cut[: cut.rfind(" ")]
        text = cut.rstrip(" ,;:—-،") + "…"
    return text


_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
READING_FEATURED_ROUTES = ("/", "/explore/", "/readings/")


def _reading_ref(r, with_thesis=False):
    ref = OrderedDict([("reading_id", r["reading_id"]), ("route", F.slash(r["route"])), ("title_en", r["title_en"]), ("title_ar", r["title_ar"])])
    if with_thesis:
        for k in ("thesis_en", "thesis_ar", "evidence_period_en", "evidence_period_ar"):
            ref[k] = r.get(k)
    return ref


def reading_relations(ctx):
    """F2 (26 Sep 2026): every Reading relation shown on another page derives from 08 and is checked here, once.
    - featured: exactly one Reading carries 08 featured = FEATURED (Home, Explore and the Readings index show it);
    - related: 08 related_readings holds one or two other Readings (shown at the end of a Reading);
    - domains: 08 domain_surface_routes places a Reading on at most two answer pages, and no page carries more than two;
    - measurement: 08 measurement_bindings names existing Measurement Agenda priorities ("This gap is examined in");
    - used in: an Evidence Record lists the Readings whose evidence path binds it (08 claim/evidence/verification ids);
    - every Reading has a governed evidence period in both languages and an ISO review date."""
    rds = ctx.out["content/readings.json"]
    by_id = OrderedDict((r["reading_id"], r) for r in rds)
    ma_ids = {m["measurement_id"] for m in ctx.out["content/measurement_agenda.json"]}
    problems = []
    featured = [r for r in rds if r.get("featured") not in (None, "")]
    if len(featured) != 1 or featured[0].get("featured") != "FEATURED":
        problems.append(f"08 featured: exactly one Reading must be FEATURED, found {[(r['reading_id'], r.get('featured')) for r in featured]}")
    per_route = defaultdict(list)
    measurement = defaultdict(list)
    used_in = defaultdict(list)
    for r in rds:
        rid = r["reading_id"]
        rel = r.get("related_readings")
        if not isinstance(rel, list) or not 1 <= len(rel) <= 2 or len(set(rel)) != len(rel) or rid in rel or any(x not in by_id for x in rel):
            problems.append(f"{rid} related_readings must name one or two other existing Readings: {rel!r}")
        mb = r.get("measurement_bindings")
        if not isinstance(mb, list) or any(x not in ma_ids for x in mb):
            problems.append(f"{rid} measurement_bindings must be a list of existing priorities: {mb!r}")
        else:
            for x in mb:
                measurement[x].append(_reading_ref(r))
        surf = [F.slash(x) for x in (r.get("domain_surface_routes") or [])]
        if not 1 <= len(surf) <= 2:
            problems.append(f"{rid} domain_surface_routes must place the Reading on one or two answer pages: {surf}")
        for x in surf:
            per_route[x].append(rid)
        if not (r.get("evidence_period_en") and r.get("evidence_period_ar")):
            problems.append(f"{rid} evidence period missing in one language")
        if not (isinstance(r.get("last_reviewed"), str) and _ISO_DATE.fullmatch(r["last_reviewed"])):
            problems.append(f"{rid} last_reviewed must be an ISO date: {r.get('last_reviewed')!r}")
        ids = []
        for x in list(r.get("claim_bindings") or []) + list(r.get("evidence_bindings") or []) + list((r.get("verification_bindings") or {}).get("claim_ids") or []):
            if x not in ids:
                ids.append(x)
        for x in ids:
            used_in[x].append(_reading_ref(r))
    for route, lst in per_route.items():
        if len(lst) > 2:
            problems.append(f"answer page {route} would carry {len(lst)} Readings (at most two): {lst}")
    if problems:
        raise IntegrityError("Reading relations (08):\n  " + "\n  ".join(problems))
    return {"by_id": by_id, "featured": _reading_ref(featured[0], with_thesis=True),
            "related": {rid: [_reading_ref(by_id[x], with_thesis=True) for x in r["related_readings"]] for rid, r in by_id.items()},
            "measurement": measurement, "used_in": used_in}


def page_specs(ctx, e):
    tm = ctx.inputs["page_spec_templates"]
    rel = reading_relations(ctx)
    intent = ctx.inputs["page_spec_design_intent"]["routes"]
    overrides = ctx.inputs["page_spec_binding_overrides"]["overrides"]
    from .structure import keyed_records
    ctx._raw06 = OrderedDict((r["object_id"], r) for _, r in keyed_records(ctx.wb.grid("06_EVIDENCE_OBJECTS"), "06_EVIDENCE_OBJECTS"))
    site = ctx.out["content/site_map.json"]
    sections = defaultdict(list)
    for s in ctx.out["content/page_sections.json"]:
        sections[s["route"]].append(s)
    idx = {
        "claim_ids": OrderedDict((c["claim_id"], c) for c in ctx.out["evidence/public_claims.json"]),
        "evidence_object_ids": OrderedDict((o["object_id"], o) for o in ctx.out["evidence/evidence_objects.json"]),
        "visual_ids": OrderedDict((v["visual_id"], v) for v in ctx.out["visuals/visual_library.json"]),
        "reading_ids": OrderedDict((r["reading_id"], r) for r in ctx.out["content/readings.json"]),
        "measurement_ids": OrderedDict((m["measurement_id"], m) for m in ctx.out["content/measurement_agenda.json"]),
    }
    clo = {(c["object_type"], c["object_id"]): c for c in ctx.out["sources/public_object_source_closure.json"]}
    smap = OrderedDict((s["source_id"], s) for s in ctx.out["sources/source_reference_map.json"])
    rx = re.compile(tm["numeric_inventory"]["tokenizer"])
    inv_fields = tm["numeric_inventory"]["fields"]
    type_of = [("public_claim", "claim_ids"), ("evidence_object", "evidence_object_ids"), ("visual", "visual_ids"), ("measurement", "measurement_ids"), ("reading", "reading_ids")]
    missing_intent = [r["route"] for r in site if r["route"] not in intent]
    if missing_intent:
        raise StructureError(f"page_spec_design_intent has no entry for routes: {missing_intent}")
    specs = []
    for r in site:
        route = r["route"]
        # sections in section order (new sections are appended to 03; sheet order is not the reading order)
        secs = sorted(sections.get(route, []), key=lambda s: s["section_order"] if isinstance(s.get("section_order"), (int, float)) else 0)
        b = _page_bindings(route, r["page_class"], r.get("instance_id"), ctx, overrides)
        for k, ids in b.items():
            for i in ids:
                if i not in idx[k]:
                    raise IntegrityError(f"page {route}: {k} references unknown ID {i!r}")
        gov = {k: [idx[k][i] for i in ids] for k, ids in b.items()}
        # verification payload: closure records of every bound object (readings first on Reading pages)
        order = [("reading", "reading_ids"), ("visual", "visual_ids")] if r["page_class"] == "reading_detail" else \
                [("evidence_object", "evidence_object_ids"), ("public_claim", "claim_ids"), ("visual", "visual_ids"), ("measurement", "measurement_ids"), ("reading", "reading_ids")]
        refs = [clo[(t, i)] for t, k in order for i in b[k] if (t, i) in clo]
        src_ids = []
        if r["page_class"] == "evidence_detail":                           # PB-0004: only the record's own bound sources
            src_ids = list(clo[("evidence_object", r.get("instance_id"))]["resolved_source_ids"])
        else:
            for c in refs:
                for s in c["resolved_source_ids"]:
                    if s not in src_ids:
                        src_ids.append(s)
        numeric = []
        for kind, key, fkey in (("claim", "claim_ids", "claim_id"), ("evidence_object", "evidence_object_ids", "object_id"), ("visual", "visual_ids", "visual_id")):
            for rec in gov[key]:
                for f in inv_fields[kind]:
                    t = rec.get(f)
                    if isinstance(t, str) and t:
                        for m in rx.finditer(t):
                            numeric.append(OrderedDict([("source_object", rec[fkey]), ("field", f), ("token", m.group(0)), ("context", t)]))
        prohibited, seen_text = [], set()
        for key, fkey, fields in (("claim_ids", "claim_id", ("does_not_prove_en", "does_not_prove_ar")), ("visual_ids", "visual_id", ("prohibited_inference_en", "prohibited_inference_ar")),
                                  ("reading_ids", "reading_id", ("prohibited_inference_en", "prohibited_inference_ar"))):
            for rec in gov[key]:
                for f in fields:
                    if rec.get(f) and (f[-2:], rec[f]) not in seen_text:       # PB-0523: union, de-duplicated per language
                        seen_text.add((f[-2:], rec[f]))
                        prohibited.append(OrderedDict([("object_id", rec[fkey]), ("field", f), ("text", rec[f])]))
        # F2: Reading relations derive from 08 (reading_relations); each page carries only the ones it shows.
        related = list(rel["related"].get(gov["reading_ids"][0]["reading_id"], [])) if r["page_class"] == "reading_detail" and gov["reading_ids"] else []
        featured = rel["featured"] if route in READING_FEATURED_ROUTES else None
        # F2: a Reading's primary question is its 08 question; the design-intent input holds no shadow copy of it
        if r["page_class"] == "reading_detail":
            if "primary_user_question_internal" in intent[route]:
                raise IntegrityError(f"page {route}: the Reading question is owned by 08; remove it from page_spec_design_intent")
            primary_q = gov["reading_ids"][0]["question_en"]
        else:
            primary_q = intent[route]["primary_user_question_internal"]
        used_in = list(rel["used_in"].get(r.get("instance_id"), [])) if r["page_class"] == "evidence_detail" else []
        measurement_readings = OrderedDict((m["measurement_id"], rel["measurement"].get(m["measurement_id"], []))
                                           for m in ctx.out["content/measurement_agenda.json"]) if route == "/measurement/" else OrderedDict()
        for L in ("en", "ar"):                                                 # EXF-002: full_copy is title + rendered sections
            want = "\n\n".join([r["title_" + L]] + [v for sct in secs for v in (sct.get("heading_" + L), sct.get("body_" + L)) if v])
            if r["full_copy_" + L] != want:
                raise IntegrityError(f"page {route}: 02 full_copy_{L} is not the derivation of title + 03 sections (EXF-002)")
        # P1.2: resolve inventory tokens in the page's public text (the Master keeps the template; the Page Spec carries the value)
        rsecs = []
        for sct in secs:
            s2 = OrderedDict(sct)
            toks = []
            for f in ("heading_en", "body_en", "heading_ar", "body_ar"):
                v, used = resolve_inventory_tokens(ctx, sct.get(f), f"page {route} section {sct.get('section_order')} {f}")
                s2[f] = v
                toks.extend(OrderedDict([("field", f), ("key", k), ("value", val)]) for k, val in used)
            if toks:
                s2["resolved_inventory_tokens"] = toks
            rsecs.append(s2)
        secs = rsecs
        full = {L: resolve_inventory_tokens(ctx, r["full_copy_" + L], f"page {route} full_copy_{L}")[0] for L in ("en", "ar")}
        for L in ("en", "ar"):
            for f in ("title_" + L, "meta_description_" + L):                # titles and authored meta descriptions carry no tokens
                if isinstance(r.get(f), str) and "{{" in r[f]:
                    raise IntegrityError(f"page {route} {f}: inventory tokens are allowed only in 03 section copy")
                resolve_inventory_tokens(ctx, r.get(f), f"page {route} {f}")
        spec = OrderedDict([
            ("page_spec_version", tm["page_spec_version"]), ("authority_master_sha256", ctx.master_sha256),
            ("route", route), ("page_class", r["page_class"]), ("template_route", r["template_route"]), ("instance_id", r.get("instance_id")),
            ("user_job_internal", intent[route]["user_job_internal"]), ("primary_user_question_internal", primary_q),
            ("title_en", r["title_en"]), ("title_ar", r["title_ar"]),
            ("meta_description_en", r.get("meta_description_en") or _meta_description(r["title_en"], secs, "en")),
            ("meta_description_ar", r.get("meta_description_ar") or _meta_description(r["title_ar"], secs, "ar")),
            ("full_copy_en", full["en"]), ("full_copy_ar", full["ar"]),
            ("sections", secs), ("bindings", b),
            ("governed_claims", gov["claim_ids"]), ("governed_evidence_objects", gov["evidence_object_ids"]),
            ("governed_visual_contracts", gov["visual_ids"]), ("governed_readings", gov["reading_ids"]),
            ("governed_measurement_priorities", gov["measurement_ids"]), ("related_readings", related),
            ("featured_reading", featured), ("used_in_readings", used_in), ("measurement_readings", measurement_readings),
            ("source_reference_closure", refs), ("source_references", [smap[s] for s in src_ids if s in smap]),
            ("numeric_strings_in_governed_copy", numeric), ("prohibited_inferences", prohibited),
            ("allowed_visual_contract_ids", list(b["visual_ids"])),
            ("accessibility_requirements", tm["accessibility_requirements"]), ("mobile_priority_internal", tm["mobile_priority_internal"]),
            ("rtl_requirements_internal", tm["rtl_requirements_internal"]), ("render_rule", tm["render_rule"]),
            ("governed_evidence_passports", []), ("frontend_render_policy", tm["frontend_render_policy"]),
        ])
        specs.append(spec)
    routes = [s["route"] for s in specs]
    ordered = sorted(specs, key=lambda s: _page_sort_key(s["route"], routes))
    pages = []
    for i, s in enumerate(ordered, 1):
        b = s["bindings"]
        pages.append(OrderedDict([("page_spec_id", f"PS-{i:03d}"), ("route", s["route"]), ("page_class", s["page_class"]), ("template_route", s["template_route"]),
                                  ("instance_id", s["instance_id"]), ("title_en", s["title_en"]), ("title_ar", s["title_ar"]),
                                  ("file", f"page_specs/{i:03d}__{_page_slug(s['route'])}.json"),
                                  ("claim_count", len(b["claim_ids"])), ("evidence_object_count", len(b["evidence_object_ids"])),
                                  ("visual_count", len(b["visual_ids"])), ("reading_count", len(b["reading_ids"])), ("measurement_count", len(b["measurement_ids"]))]))
    return OrderedDict([("schema_version", tm["schema_version"]), ("spec_count", len(specs)), ("page_specs", specs),
                        ("index", OrderedDict([("authority_master_sha256", ctx.master_sha256), ("spec_count", len(specs)), ("rule", tm["index_rule"]), ("pages", pages)]))])


# ------------------------------------------------------------------------------------------------
# CONTROLLED CONTRACTS (not Master-generated): maintained in place; generator rebinds and validates
# ------------------------------------------------------------------------------------------------
def _load_contract(ctx, e):
    import json, os
    p = os.path.join(ctx.repo, "site-src", "content", e["path"])
    with open(p, encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def _align_navigation_contract(n):
    """Pre-Tranche-C P4 (V-D2/V-D3): labels and counts recorded elsewhere in the hand-governed contract follow the governed
    navigation (04) and the route list, so they cannot drift: footer link labels, the footer group that mirrors a navigation
    family (label and order), breadcrumb parent labels, page-family route counts, and a family's prominence when all of its
    routes share one prominence."""
    label = {}
    for it in n.get("global_navigation") or []:
        for x in ([it] if it.get("route") else []) + list(it.get("children") or []):
            label[x["route"]] = (x["label_en"], x["label_ar"])
    for t in n.get("trust_navigation") or []:
        label[t["route"]] = (t["label_en"], t["label_ar"])
    families = {tuple(sorted(c["route"] for c in it["children"])): it for it in n.get("global_navigation") or [] if it.get("children")}
    for g in n.get("footer_groups") or []:
        for link in g.get("links") or []:
            if link.get("route") in label:
                link["label_en"], link["label_ar"] = label[link["route"]]
        fam = families.get(tuple(sorted(link.get("route") for link in g.get("links") or [])))
        if fam:
            g["label_en"], g["label_ar"] = fam["label_en"], fam["label_ar"]
            order = [c["route"] for c in fam["children"]]
            g["links"] = sorted(g["links"], key=lambda link: order.index(link["route"]))
    for b in (n.get("breadcrumbs") or {}).values():
        if b.get("parent_route") in label:
            b["parent_label_en"], b["parent_label_ar"] = label[b["parent_route"]]
    counts = defaultdict(int)
    for r in n.get("routes") or []:
        counts[r.get("page_family")] += 1
    declared = {f["page_family"] for f in n.get("page_families") or []}
    if set(counts) - declared:
        raise StructureError(f"navigation contract: routes use undeclared page families {sorted(set(counts) - declared)}")
    for f in n.get("page_families") or []:
        f["route_count"] = counts.get(f["page_family"], 0)
        prom = {r.get("navigation_prominence") for r in n["routes"] if r.get("page_family") == f["page_family"]}
        if len(prom) == 1 and prom <= {"GLOBAL_PRIMARY", "PRIMARY_CHILD", "SECONDARY_TRUST"}:
            f["navigation_prominence"] = prom.pop()


def navigation_contract(ctx, e):
    import hashlib
    from .generator import serialize
    n = _load_contract(ctx, e)
    site_routes = [r["route"] for r in ctx.out["content/site_map.json"]]
    if [r["route"] for r in n["routes"]] != site_routes:
        raise StructureError("navigation contract routes differ from 02_SITE_MAP routes; update the contract in the same change")
    from .structure import keyed_records
    nav = []
    site_set = set(site_routes)
    for _, rec in keyed_records(ctx.wb.grid("04_NAV_UX"), "04_NAV_UX"):
        if isinstance(rec.get("item_order"), int):
            spec_ = F.json_or_keep(rec.get("route_or_group"))
            if not isinstance(spec_, dict):
                raise StructureError(f"04_NAV_UX item {rec.get('item_order')}: route_or_group is not a JSON object")
            item = OrderedDict()
            if spec_.get("route"):
                item["route"] = F.slash(spec_["route"])
            item["label_en"], item["label_ar"] = rec["label_en"], rec["label_ar"]
            kids = []
            for c in spec_.get("children") or []:                  # PB-0424: {route?, label_en, label_ar, children:[{route, label_en, label_ar}]}
                if not c.get("route"):
                    raise StructureError(f"04_NAV_UX item {rec.get('item_order')}: child without a route")
                kids.append(OrderedDict([("route", F.slash(c["route"])), ("label_en", c["label"]["en"]), ("label_ar", c["label"]["ar"])]))
            if kids:
                item["children"] = kids
            if not item.get("route") and len(kids) < 2:
                raise StructureError(f"04_NAV_UX item {rec.get('item_order')}: a grouping node needs at least two routed children")
            for r_ in [item.get("route")] + [k["route"] for k in kids]:
                if r_ and r_ not in site_set:
                    raise StructureError(f"04_NAV_UX navigation route {r_} is not a 02 route")
            nav.append(item)
    n["global_navigation"] = nav
    trust = []
    titles = [b["title"] for b in __import__("projection.structure", fromlist=["blocks"]).blocks(ctx.wb.grid("04_NAV_UX"), "04_NAV_UX")]
    if "Trust navigation" in titles:
        for _, rec in keyed_records(ctx.wb.grid("04_NAV_UX"), "04_NAV_UX", block="Trust navigation"):
            r_ = F.slash(rec["route"])
            if r_ not in site_set:
                raise StructureError(f"04 Trust navigation route {r_} is not a 02 route")
            trust.append(OrderedDict([("route", r_), ("label_en", rec["label_en"]), ("label_ar", rec["label_ar"])]))
        n["trust_navigation"] = trust
    _align_navigation_contract(n)
    ps_text = serialize(ctx.out["page_specs.json"], True)
    n["authority_binding"] = OrderedDict([("master_sha256", ctx.master_sha256),
                                          ("page_specs_sha256", hashlib.sha256(ps_text.encode("utf-8")).hexdigest()),
                                          ("page_spec_count", ctx.out["page_specs.json"]["spec_count"])])
    counts = defaultdict(int)
    for s in ctx.out["content/search_index.json"]:
        counts[re.split(r"[?#]", s["route"])[0]] += 1
    for r in n["routes"]:
        r["search_record_count"] = counts.get(r["route"], 0)
    n["public_search_record_count"] = len(ctx.out["content/search_index.json"])
    return n


def presentation_contract(ctx, e):
    p = _load_contract(ctx, e)
    secs = {(s["route"], s["section_order"]) for s in ctx.out["content/page_sections.json"]}
    vis = {v["visual_id"] for v in ctx.out["visuals/visual_library.json"]}
    for r in p.get("routes", []):
        for tier in ("primary", "supporting", "progressive"):
            for item in r.get(tier, []):
                if item.get("kind") == "section" and (r["route"], item["section_order"]) not in secs:
                    raise StructureError(f"presentation contract {r['route']} {tier}: section {item['section_order']} does not exist in 03")
                if item.get("kind") == "visual" and item["object_id"] not in vis:
                    raise StructureError(f"presentation contract {r['route']}: unknown visual {item['object_id']}")
    # EAD-11: Home's starting questions and Explore's groups — every question ID and heading label must be governed
    qids = [str(q.get("question_id")) for q in ctx.out["content/questions.json"]]
    ui = {r.get("ui_id") for r in ctx.out["content/interface_copy.json"]}
    sets = {str(e.get("route")): e for e in p.get("question_sets") or []}
    if set(sets) != {"/", "/explore/"}:
        raise StructureError(f"presentation contract question_sets: routes {sorted(sets)}, expected / and /explore/")
    home = sets["/"].get("starting_question_ids") or []
    if not home or len(set(home)) != len(home) or any(q not in qids for q in home):
        raise StructureError(f"presentation contract question_sets /: starting questions {home} are not distinct governed questions")
    grouped = [q for g in sets["/explore/"].get("question_groups") or [] for q in g.get("question_ids") or []]
    for g in sets["/explore/"].get("question_groups") or []:
        if g.get("heading_ui_id") not in ui:
            raise StructureError(f"presentation contract question_sets /explore/: unknown heading {g.get('heading_ui_id')}")
    if sorted(grouped) != sorted(qids):
        raise StructureError("presentation contract question_sets /explore/: the groups must hold every governed question exactly once")
    return p


# ------------------------------------------------------------------------------------------------
# DERIVED: visual design contracts (Pre-Tranche-C P3) — tiers for all governed visuals; for SIGNATURE and
# CORE_ANALYTICAL visuals, the governed rows a chart binds to, resolved and guarded, plus the governed text a
# detached frame must carry. The controlled input declares bindings and drawing rules only; every value, label and
# sentence comes from the Master (data sheets, 11, 06, 34, 15, 04 interface copy).
# ------------------------------------------------------------------------------------------------
_VDC_TIERS = ("SIGNATURE", "CORE_ANALYTICAL", "SUPPORTING", "TABLE_TEXT_FIRST", "RETIRE_FROM_DESIGN")
_VDC_CONTRACT_TIERS = ("SIGNATURE", "CORE_ANALYTICAL")


def _vdc_blocks(snapshot, header_key, where):
    rows = snapshot.get("rows") or []
    recs, found = [], False
    for i, r in enumerate(rows):
        if not r or r[0] != header_key:
            continue
        found = True
        hdr = [str(x) if x is not None else None for x in r]
        for rr in rows[i + 1:]:
            if not rr or all(c in (None, "") for c in rr) or rr[0] == header_key:
                break
            recs.append(OrderedDict((h, rr[j] if j < len(rr) else None) for j, h in enumerate(hdr) if h))
    if not found:
        raise IntegrityError(f"{where}: no block headed {header_key!r} in {snapshot.get('sheet')}")
    return recs


def _vdc_select(ctx, spec, where):
    snap = ctx.out.get(spec["file"])
    if snap is None:
        raise IntegrityError(f"{where}: {spec['file']} is not generated before visual design contracts")
    recs = _vdc_blocks(snap, spec["header_key"], where)
    key = spec.get("key", spec["header_key"])
    if "ids" in spec:
        idx = OrderedDict()
        for r in recs:
            idx.setdefault(str(r.get(key)), r)
        missing = [i for i in spec["ids"] if i not in idx]
        if missing:
            raise IntegrityError(f"{where}: unresolved row IDs {missing}")
        return [idx[i] for i in spec["ids"]]
    sel = [r for r in recs if all(re.search(p, str(r.get(f) if r.get(f) is not None else "")) for f, p in spec["where"].items())]
    if not sel:
        raise IntegrityError(f"{where}: selector {spec['where']} matched no row")
    return sel


def _vdc_num(v):
    if isinstance(v, bool) or v in (None, ""):
        return None
    if isinstance(v, (int, float)):
        return v
    try:
        f = float(str(v).replace(",", ""))
        return int(f) if f.is_integer() else f
    except ValueError:
        return None


def _vdc_series(ctx, s, where, grammar_tokens):
    recs = _vdc_select(ctx, s["rows"], where)
    f = s["fields"]
    key = s["rows"].get("key", s["rows"]["header_key"])
    values, x_seen = [], []
    prev_src = None
    lanes = s.get("lanes")
    for r in recs:
        rid = str(r.get(key))
        flag = str(r.get(f.get("flag")) or "") if f.get("flag") else ""
        src = r.get(f.get("source")) if f.get("source") else None
        base = OrderedDict([("id", rid)])
        for k, col in f.items():
            if k in ("y",) or (lanes and k in lanes):
                continue
            base[k] = r.get(col)
        emitted = []
        if lanes:
            # P4 (V-D6): one value per lane with its own id (row#lane), unit and markers; a source state that maps to a structure
            # marker (e.g. DISAGREEMENT) keeps the series base state as its evidence state
            for lane, state_field in lanes.items():
                v = OrderedDict(base)
                v["id"] = f"{rid}#{lane}"
                v["row_id"] = rid
                v["lane"] = lane
                if s.get("lane_units"):
                    v["unit"] = s["lane_units"][lane]
                v["y"] = _vdc_num(r.get(f[lane]))
                st = str(r.get(f[state_field]) or "")
                v["source_state"] = st
                g = (s.get("state_map") or {}).get(st, s.get("state"))
                v["grammar_state"] = g if g in grammar_tokens["states"] else s.get("state")
                markers = [g] if g in grammar_tokens["markers"] else []
                for m in list((s.get("lane_markers") or {}).get(lane, [])) + list((s.get("row_markers") or {}).get(rid, [])):
                    if m not in markers:
                        markers.append(m)
                v["markers"] = markers
                if v["y"] is None:
                    v["grammar_state"] = "UNKNOWN"
                if v["grammar_state"] not in grammar_tokens["states"] or any(m not in grammar_tokens["markers"] for m in markers):
                    raise IntegrityError(f"{where}: {v['id']} has an ungoverned state or marker")
                emitted.append(v)
        else:
            v = OrderedDict(base)
            v["y"] = _vdc_num(r.get(f["y"])) if "y" in f else None
            g = (s.get("state_map") or {}).get(flag, s.get("state"))
            v["grammar_state"] = g
            markers = list(s.get("markers") or [])
            for sub, m in (s.get("flag_markers") or {}).items():
                if sub in flag and m not in markers:
                    markers.append(m)
            if s.get("break_between_sources") and prev_src is not None and src != prev_src:
                markers.append(s["break_between_sources"])
            cav = s.get("withhold_when_caveat_matches")
            if cav and cav in str(r.get(f.get("caveat")) or ""):
                v["y"] = None
                v["withheld"] = True
                markers.append("WITHHELD")
            v["markers"] = markers
            emitted.append(v)
        prev_src = src
        x_seen.append(str(r.get(f.get("x"))) if f.get("x") else None)
        values.extend(emitted)
    for rid, expect in (s.get("must_equal") or {}).items():
        got = [v for v in values if v["id"] == rid and not v.get("lane")] or [v for v in values if v.get("row_id") == rid and v.get("lane") == "borrowers"]
        if not got or _vdc_num(got[0]["y"]) != expect:
            raise IntegrityError(f"{where}: guard {rid} = {expect} failed (got {got[0]['y'] if got else None})")
    out = OrderedDict([("id", s["id"]), ("state", s.get("state")), ("markers", s.get("markers") or []), ("values", values)])
    if s.get("expected_x"):
        extra = [x for x in x_seen if x not in s["expected_x"]]
        if extra:
            raise IntegrityError(f"{where}: rows outside the expected periods {extra}")
        missing = [x for x in s["expected_x"] if x not in x_seen]
        for m in s.get("must_be_missing") or []:
            if m not in missing:
                raise IntegrityError(f"{where}: {m} is governed as missing but a row exists")
        out["missing_x"] = [OrderedDict([("x", m), ("marker", "MISSING")]) for m in missing]
    return out


def _vdc_objects(ctx, o, where):
    recs = _vdc_select(ctx, o["rows"], where)
    key = o["rows"].get("key", o["rows"]["header_key"])
    out = []
    months = {m: i for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"), 1)}
    for r in recs:
        rec = OrderedDict([("id", str(r.get(key)))] + [(k, r.get(col)) for k, col in o["fields"].items()])
        for fld in o.get("month_year_fields") or []:                 # P4 (V-D5): "Jan-2025" -> "2025-01", formatted by locale in Design
            m = re.fullmatch(r"([A-Za-z]{3})-(\d{4})", str(rec.get(fld) or ""))
            if not m or m.group(1).lower() not in months:
                raise IntegrityError(f"{where}: {rec['id']}.{fld} is not a month-year value ({rec.get(fld)!r})")
            rec[f"{fld}_iso"] = f"{m.group(2)}-{months[m.group(1).lower()]:02d}"
        out.append(rec)
    for rid, expect in (o.get("must_equal") or {}).items():
        rec = next((x for x in out if x["id"] == rid), None)
        if rec is None:
            raise IntegrityError(f"{where}: guard row {rid} missing")
        checks = expect.items() if isinstance(expect, dict) else [("count", expect)]
        for fld, val in checks:
            if _vdc_num(rec.get(fld)) != val:
                raise IntegrityError(f"{where}: guard {rid}.{fld} = {val} failed (got {rec.get(fld)!r})")
    return OrderedDict([("id", o["id"]), ("records", out)])


_VDC_TEMPORAL = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def _vdc_label_items(items, label_fields, encoding_only, dl, ui, where, problems):
    printed = set(dl.get("printed_fields") or [])
    ns_map = dl.get("namespaces") or {}
    for it in items:
        for fld in sorted(printed & set(it)):
            val = it.get(fld)
            if val in (None, "") or fld in encoding_only or _VDC_TEMPORAL.match(str(val)):
                continue
            ns = label_fields.get(fld)
            if ns is None:
                problems.append(f"{where}: printed field {fld} has no label namespace")
                continue
            uid = (ns_map.get(ns) or {}).get(str(val))
            if uid is None:
                problems.append(f"{where}: {fld}={str(val)[:70]!r} has no governed label in namespace {ns}")
            elif uid not in ui:
                problems.append(f"{where}: label {uid} is not governed interface copy (04)")
            else:
                it[f"{fld}_label"] = OrderedDict([("en", ui[uid]["label_en"]), ("ar", ui[uid]["label_ar"]), ("ui_id", uid)])


def visual_design_contracts(ctx, e):
    c = ctx.inputs["visual_design_contract"]
    ui = {r["ui_id"]: r for r in ctx.out["content/interface_copy.json"]}
    vis = OrderedDict((v["visual_id"], v) for v in ctx.out["visuals/visual_library.json"])
    eo = {r["object_id"]: r for r in ctx.out["evidence/evidence_objects.json"]}
    passports = {r["passport_id"]: r for r in ctx.out["evidence/evidence_passports.json"]}
    sources = {r["source_id"]: r for r in ctx.out["sources/source_library.json"]}
    problems = []

    # grammar: every referenced label must be governed interface copy
    g = c["grammar"]
    states = [x["token"] for x in g["evidence_states"]]
    markers = [x["token"] for x in g["structure_markers"]]
    if "WITHHELD" not in markers:          # governed marker since F9 (grammar entry in the controlled input)
        markers.append("WITHHELD")
    tokens = {"states": states, "markers": markers}
    ui_refs = [x["ui_id"] for x in g["evidence_states"] + g["structure_markers"]] + g["chain"]["steps"] + list(g["chain"]["states"].values())
    ui_refs += ["UI-VIS-WITHHELD", "UI-VIS-DOES-NOT-ESTABLISH", "UI-VIS-SOURCE", "UI-VIS-FULL-RECORD", "UI-VIS-ISSUER-SCOPE", "UI-VIS-BASELINE"]
    for u in ui_refs:
        if u not in ui:
            problems.append(f"grammar label {u} is not governed interface copy (04)")
    if problems:
        raise IntegrityError("visual design contract:\n  " + "\n  ".join(problems))
    labels = OrderedDict((u, OrderedDict([("en", ui[u]["label_en"]), ("ar", ui[u]["label_ar"])])) for u in dict.fromkeys(ui_refs))
    dl = c.get("display_labels") or {}
    label_problems = []

    tiered = [v["visual_id"] for v in c["visuals"]]
    dup = sorted({x for x in tiered if tiered.count(x) > 1})
    if dup:
        problems.append(f"visuals tiered more than once: {dup}")
    if set(tiered) != set(vis):
        problems.append(f"tiering must cover exactly the governed visuals: missing {sorted(set(vis) - set(tiered))}, unknown {sorted(set(tiered) - set(vis))}")
    if problems:
        raise IntegrityError("visual design contract:\n  " + "\n  ".join(problems))

    def text(lang, *parts):
        return " · ".join(p for p in parts if p)

    out_vis = []
    for spec in c["visuals"]:
        vid, tier = spec["visual_id"], spec["tier"]
        where = f"visual design contract {vid}"
        if tier not in _VDC_TIERS:
            raise IntegrityError(f"{where}: unknown tier {tier!r}")
        if (tier in _VDC_CONTRACT_TIERS) != ("contract" in spec):
            raise IntegrityError(f"{where}: a data contract is required for {'/'.join(_VDC_CONTRACT_TIERS)} and only for them")
        v = vis[vid]
        ev = eo.get(vid)
        rec = OrderedDict([("visual_id", vid), ("tier", tier), ("rationale", spec["rationale"])])
        for k in ("family", "promotion_requires"):
            if spec.get(k):
                rec[k] = spec[k]
        gov = OrderedDict()
        for lang in ("en", "ar"):
            gov[f"title_{lang}"] = v.get(f"title_{lang}")
            gov[f"question_{lang}"] = v.get(f"question_{lang}")
            gov[f"prohibited_inference_{lang}"] = v.get(f"prohibited_inference_{lang}")
            gov[f"alt_text_{lang}"] = f"{v.get(f'accessible_summary_{lang}')} {labels['UI-VIS-DOES-NOT-ESTABLISH'][lang]} {v.get(f'prohibited_inference_{lang}')}"
            if ev:
                gov[f"period_{lang}"], gov[f"universe_{lang}"] = ev.get(f"period_{lang}"), ev.get(f"universe_{lang}")
            elif lang == "en":
                gov["period_en"], gov["universe_en"] = v.get("period"), v.get("denominator_universe")
            else:
                gov["period_ar"], gov["universe_ar"] = v.get("period_ar"), v.get("universe_ar")
        routes = v.get("public_routes") or []
        gov["canonical_route"] = f"/evidence/{vid}/" if ev else ((routes[0].rstrip("/") + "/") if routes else None)
        gov["public_routes"] = routes
        rec["governed"] = gov
        if tier in _VDC_CONTRACT_TIERS:
            k = spec["contract"]
            con = OrderedDict((key, val) for key, val in k.items() if key not in ("series", "objects", "derived", "credit", "frame_labels"))
            series = [_vdc_series(ctx, s, f"{where} series {s['id']}", tokens) for s in k.get("series") or []]
            objects = [_vdc_objects(ctx, o, f"{where} objects {o['id']}") for o in k.get("objects") or []]
            derived_vals = []
            flat = {x["id"]: x for s in series for x in s["values"] if not x.get("lane")}
            by_series = {x["id"]: [v for v in x["values"] if not v.get("lane")] for x in series}
            for d in k.get("derived") or []:
                if "index" in d:                  # P5.3: a path indexed to its own base period (never joined to another path)
                    ix = d["index"]
                    vals = by_series.get(ix["series"])
                    base = next((v for v in vals or [] if str(v.get("x")) == str(ix["base_x"])), None)
                    if not vals or base is None or not base.get("y"):
                        raise IntegrityError(f"{where}: derived {d['id']}: series {ix['series']} has no base value at {ix['base_x']}")
                    for v in vals:
                        derived_vals.append(OrderedDict([("id", f"{d['id']}#{v['x']}"), ("series", d["id"]), ("x", v["x"]),
                                                         ("value", round(v["y"] / base["y"] * ix["scale"], 2)), ("unit", d["unit"]),
                                                         ("from", [v["id"], base["id"]]), ("series_label", v.get("series_label")),
                                                         ("grammar_state", d["state"]), ("markers", list(d.get("markers") or []))]))
                    continue
                if "growth_gap" in d:             # P5.3: guard that the governed rows reproduce the governed claim (e.g. CLM-037)
                    gg = d["growth_gap"]
                    ya = {str(v["x"]): v["y"] for v in by_series[gg["a"]]}
                    yb = {str(v["x"]): v["y"] for v in by_series[gg["b"]]}
                    years = [y for y in sorted(ya) if gg["from_x"] <= y <= gg["to_x"]]
                    gaps = []
                    for y in years:
                        prev = str(int(y) - 1)
                        if prev not in ya or prev not in yb or y not in yb:
                            raise IntegrityError(f"{where}: derived {d['id']}: missing value for {prev} or {y}")
                        gaps.append(abs((ya[y] / ya[prev] - yb[y] / yb[prev]) * 100))
                    val = round(max(gaps), 4)
                    if abs(val - d["must_equal"]) > d.get("tolerance", 1e-9):
                        raise IntegrityError(f"{where}: derived {d['id']} = {val}, governed value is {d['must_equal']}")
                    derived_vals.append(OrderedDict([("id", d["id"]), ("value", val), ("unit", d["unit"]), ("from", [gg["a"], gg["b"]]),
                                                     ("grammar_state", d["state"]), ("guard_of", d.get("guard_of"))]))
                    continue
                a, b = (flat[i]["y"] for i in d["minus"])
                val = round(a - b, 2)
                if abs(val - d["must_equal"]) > 1e-9:
                    raise IntegrityError(f"{where}: derived {d['id']} = {val}, governed value is {d['must_equal']}")
                derived_vals.append(OrderedDict([("id", d["id"]), ("value", val), ("unit", d["unit"]), ("from", d["minus"]), ("grammar_state", d["state"])]))
            # credit line: governed publisher or authority only
            cr, cred_src, blockers = k.get("credit") or {}, [], []
            for pid in ([cr["passport_id"]] if cr.get("passport_id") else []) + list(cr.get("passport_ids") or []):
                p = passports.get(pid)
                if not p:
                    raise IntegrityError(f"{where}: passport {pid} does not exist")
                cred_src.append(p.get("publisher"))
            for sid in cr.get("source_ids") or []:
                s0 = sources.get(sid)
                if not s0:
                    raise IntegrityError(f"{where}: source {sid} does not exist")
                if s0.get("publisher"):
                    cred_src.append(s0["publisher"])
                else:
                    blockers.append(f"source {sid} has no governed publisher for the credit line")
            if cr.get("source_urls_from_object"):
                su = cr["source_urls_from_object"]
                ob = next((o for o in objects if o["id"] == su["object"]), None)
                by_url = {}
                for s0 in sources.values():
                    for u in [s0.get("primary_url")] + str(s0.get("additional_urls") or "").split("|"):
                        if u and u.strip():
                            by_url.setdefault(u.strip(), s0)
                for x in ob["records"]:
                    s0 = by_url.get(str(x.get(su["field"]) or "").strip())
                    if s0 is None:
                        blockers.append(f"{x['id']}: locator {x.get(su['field'])} has no source record")
                    elif s0.get("publisher"):
                        cred_src.append(s0["publisher"])
                    else:
                        blockers.append(f"{x['id']}: source {s0['source_id']} has no governed publisher for the credit line")
            if cr.get("from_object"):
                ob = next((o for o in objects if o["id"] == cr["from_object"]), None)
                if cr.get("authority_field"):
                    cred_src.extend(x.get(cr["authority_field"]) for x in ob["records"])
                if cr.get("source_field"):
                    for x in ob["records"]:
                        s0 = sources.get(x.get(cr["source_field"])) or {}
                        if s0.get("publisher"):
                            cred_src.append(s0["publisher"])
                        else:
                            blockers.append(f"source {x.get(cr['source_field'])} has no governed publisher for the credit line")
            credit = "; ".join(dict.fromkeys(x for x in cred_src if x))
            if not credit:
                blockers.append("no governed credit line")
            con["credit"] = OrderedDict([("rule", cr), ("text", credit or None), ("language_note", "Publisher names are governed in English only (15, 34); Arabic frames print them as isolated left-to-right runs.")])
            # P4 (V-D5): every printed value carries its governed bilingual label
            specs_ = {x["id"]: x for x in (k.get("series") or []) + (k.get("objects") or [])}
            for grp in series + objects:
                sp = specs_[grp["id"]]
                items = grp["values"] if "values" in grp else grp["records"]
                _vdc_label_items(items, sp.get("label_fields") or {}, sp.get("encoding_only_fields") or [], dl, ui, f"{where} {grp['id']}", label_problems)
                for name, rule in (sp.get("derived_labels") or {}).items():          # e.g. the 'is not' line of a payment object
                    for it in items:
                        uid = ((dl.get("namespaces") or {}).get(rule["namespace"]) or {}).get(str(it.get(rule["field"])))
                        if uid is None or uid not in ui:
                            label_problems.append(f"{where} {grp['id']}: no governed {name} label for {it.get(rule['field'])!r}")
                        else:
                            it[f"{name}_label"] = OrderedDict([("en", ui[uid]["label_en"]), ("ar", ui[uid]["label_ar"]), ("ui_id", uid)])
                grp["label_fields"] = OrderedDict(sp.get("label_fields") or {})
                if sp.get("encoding_only_fields"):
                    grp["encoding_only_fields"] = list(sp["encoding_only_fields"])
            _vdc_label_items(derived_vals, {"unit": "unit", "series_label": "series"}, [], dl, ui, f"{where} derived", label_problems)
            fl = OrderedDict()
            for uid in k.get("frame_labels") or []:                                  # governed in-frame sentences
                if uid not in ui:
                    label_problems.append(f"{where}: frame label {uid} is not governed interface copy (04)")
                else:
                    fl[uid] = OrderedDict([("en", ui[uid]["label_en"]), ("ar", ui[uid]["label_ar"])])
            if fl:
                con["frame_labels"] = fl
            con["series"] = series
            con["objects"] = objects
            con["derived"] = derived_vals
            for p in k.get("panels") or []:
                if p.get("state") != "READY":
                    blockers.append(f"panel {p['id']}: {p['state']}")
                    continue
                # a READY panel is checked, not asserted: every series it binds resolves to values, every derived path exists
                for sid in p.get("series") or []:
                    if not by_series.get(sid):
                        raise IntegrityError(f"{where}: panel {p['id']} is READY but series {sid} has no governed values")
                for did in p.get("derived") or []:
                    if not any(dv.get("series") == did or dv["id"] == did for dv in derived_vals):
                        raise IntegrityError(f"{where}: panel {p['id']} is READY but derived path {did} is empty")
            con["blockers"] = blockers
            rec["contract"] = con
            for lang in ("en", "ar"):
                rec[f"detached_caption_{lang}"] = text(
                    lang, gov[f"title_{lang}"], gov[f"period_{lang}"], gov[f"universe_{lang}"],
                    f"{labels['UI-VIS-SOURCE'][lang]} {credit}" if credit else None,
                    f"{labels['UI-VIS-DOES-NOT-ESTABLISH'][lang]} {gov[f'prohibited_inference_{lang}']}",
                    f"{labels['UI-VIS-FULL-RECORD'][lang]} /{lang}{gov['canonical_route']}" if gov["canonical_route"] else None)
        out_vis.append(rec)
    if label_problems:
        raise IntegrityError("visual design contract labels:\n  " + "\n  ".join(label_problems))
    counts = OrderedDict((t, sum(1 for x in out_vis if x["tier"] == t)) for t in _VDC_TIERS)
    return OrderedDict([("schema_version", c["schema_version"]), ("contract_id", c["contract_id"]), ("authority_master_sha256", ctx.master_sha256),
                        ("rule", c["rule"]), ("tiers", c["tiers"]), ("tier_counts", counts), ("grammar", g), ("grammar_labels", labels),
                        ("display_label_rule", dl.get("rule")),
                        ("global_rules", c["global_rules"]), ("visuals", out_vis)])


# ------------------------------------------------------------------------------------------------
# DERIVED: Reading sections (Pre-Tranche-C P4.2, tightened in P4-D) — one Reading truth. Section 1 copy is owned by
# 08 thesis; sections 2-9 heading and body are owned by 03_PAGE_SECTIONS (the rendered Reading page). 09 is a pure
# section index (reading_id, section_order, section_id, and the section-1 title that labels the thesis): its copy cells
# (all orders) and title cells (orders 2-9) are empty, and generation stops if text is written into them. An edit is
# therefore made once, in the owner.
# ------------------------------------------------------------------------------------------------
def reading_sections(ctx, e):
    idx = F.keyed(ctx.wb, e["sheet"], ctx.contract, e.get("fields"))
    readings = {r["reading_id"]: r for r in ctx.out["content/readings.json"]}
    secs = {}
    for x in ctx.out["content/page_sections.json"]:
        secs[(F.slash(x["route"]), int(float(x["section_order"])))] = x
    problems, out, covered = [], [], set()
    for r in idx:
        rid, order = r["reading_id"], int(float(r["section_order"]))
        rd = readings.get(rid)
        if rd is None:
            problems.append(f"{rid}: no Reading in 08")
            continue
        route = F.slash(rd["route"])
        rec = OrderedDict(r)
        if order == 1:
            owner = {"copy_en": rd.get("thesis_en"), "copy_ar": rd.get("thesis_ar")}
        else:
            sec = secs.get((route, order))
            if sec is None:
                problems.append(f"{rid} s{order}: no 03 section on {route}")
                continue
            covered.add((route, order))
            owner = {"copy_en": sec.get("body_en"), "copy_ar": sec.get("body_ar"), "title_en": sec.get("heading_en"), "title_ar": sec.get("heading_ar")}
        # F2: the opening section (order 2) may be heading-less in both languages — the essay runs on from the
        # standfirst; a heading present in one language only is still an error.
        open_ok = order == 2 and owner.get("title_en") in (None, "") and owner.get("title_ar") in (None, "")
        for k, v in owner.items():
            if r.get(k) not in (None, ""):
                problems.append(f"{rid} s{order}.{k}: 09 is the section index and holds no copy; edit the owner "
                                f"({'08 thesis' if order == 1 else '03 ' + route})")
            if v in (None, "") and not (open_ok and k.startswith("title_")):
                problems.append(f"{rid} s{order}.{k}: the owner ({'08 thesis' if order == 1 else '03 ' + route}) is empty")
            rec[k] = v
        if order == 1 and (not r.get("title_en") or not r.get("title_ar")):
            problems.append(f"{rid} s1: the section-1 title (09) is missing in one language")
        out.append(rec)
    routes = {F.slash(rd["route"]) for rd in readings.values()}
    orphans = sorted(f"{rt} s{o}" for (rt, o) in secs if rt in routes and (rt, o) not in covered)
    if orphans:
        problems.append(f"03 Reading sections outside the 09 index: {orphans}")
    if problems:
        raise IntegrityError("Reading sections (one Reading truth):\n  " + "\n  ".join(problems))
    return out
