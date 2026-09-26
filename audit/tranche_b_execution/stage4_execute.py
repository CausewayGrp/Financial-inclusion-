# -*- coding: utf-8 -*-
"""Stage 4 — IA, trust, source discovery, search and visual-contract roots, Master-first.

  python3 stage4_execute.py <in_master.xlsx> <spec.csv> <out_master.xlsx> <out_dir> <ledger.json>

Master changes: SUBSTR roots of the VISUAL-VOICE / TRUST / LEAD-M05 families; 04 navigation (PB-0420…PB-0424 incl. a
'Trust navigation' block), the footer strapline (PB-0412) and the governed search aliases (PB-0492); 15 rights and
source-kind columns (PB-0390, PB-0493b); 06 visual_contract_state (PB-0401) and source_use_roles (PB-0493b).
Controlled files written to <out_dir>: master_structure.json and navigation_interaction.json.
"""
import hashlib, json, os, re, sys
from collections import OrderedDict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from engine import Engine, RootFailure, LOC_SUBSTR, ROOT      # noqa: E402
from stage3_execute import leads, regenerate_full_copy         # noqa: E402

STAGE = "STAGE-4"
S4_LEADS = {"LEAD-M09", "SEARCH-R", "TRUST-F01", "TRUST-F02", "TRUST-F05", "VISUAL-VOICE", "LEAD-M05"}
TRUST_NAV = [("About", "عن الموقع", "/about"), ("Corrections", "التصحيحات", "/corrections"), ("Rights & reuse", "الحقوق وإعادة الاستخدام", "/rights"),
             ("Accessibility", "إتاحة الوصول", "/accessibility"), ("Privacy", "الخصوصية", "/privacy"), ("Terms", "شروط الاستخدام", "/terms"),
             ("Contact", "التواصل", "/contact")]
ALIASES = [
    ("SEARCH-ALIAS-001", "law; laws", "قانون; قوانين", "document_type:law | route:/reforms/ | route:/data/", None, None),
    ("SEARCH-ALIAS-002", "decision; decisions", "قرار; قرارات", "document_type:decision/enforcement | route:/providers/ | route:/reforms/", None, None),
    ("SEARCH-ALIAS-003", "circular; circulars", "تعميم; تعاميم", "document_type:instruction/circular | route:/reforms/", None, None),
    ("SEARCH-ALIAS-004", "regulation; regulations; instructions", "لائحة; لوائح; تعليمات",
     "document_type:regulation | document_type:instruction/circular | route:/reforms/ | route:/data/", None, None),
    ("SEARCH-ALIAS-005", "remittance; remittances", "حوالة; حوالات; تحويلات", "route:/remittances/", None, None),
    ("SEARCH-ALIAS-006", "exchange company; exchange companies", "صرافة; شركات الصرافة; منشآت الصرافة", "route:/providers/", None, None),
    ("SEARCH-ALIAS-007", "wallet; e-wallet; e-wallets; electronic wallet", "محفظة; محافظ; المحافظ الإلكترونية; المحفظة الإلكترونية", "route:/payments/", None, None),
    ("SEARCH-ALIAS-008", "POS; point of sale; POS terminals", "نقاط البيع; نقطة بيع", "route:/payments/", None, None),
    ("SEARCH-ALIAS-009", "microfinance; MFB; MFI", "التمويل الأصغر; تمويل أصغر", "route:/finance/", None, None),
    ("SEARCH-ALIAS-010", "exchange rate", "سعر الصرف; أسعار الصرف", "route:/finance/", None, None),
    ("SEARCH-ALIAS-011", "measurement agenda", "أجندة القياس; القياس", "route:/measurement/", None, None),
    ("SEARCH-ALIAS-012", "financial literacy; financial education", "الثقافة المالية; التثقيف المالي", "route:/people/ | route:/reforms/",
     "Discovery aid only: financial-education activity is not literacy, capability or behaviour.",
     "وسيلة للعثور على المحتوى فقط: النشاط التثقيفي المالي ليس ثقافة مالية ولا قدرة ولا سلوكًا."),
    # Lead additions at execution (PB-0494 probe terms without a governed answer page in the top 3): discovery only.
    ("SEARCH-ALIAS-013", "income; income gap", "الدخل; فجوة الدخل", "route:/people/", None, None),
    ("SEARCH-ALIAS-014", "credit; lending", "الائتمان; الإقراض", "route:/finance/ | route:/firms/", None, None),
]
# PB-0493(b): document kind and evidence roles only where the Master already states them (basis per group).
DOC_KIND = OrderedDict([
    ("decision/enforcement", ([f"SRC-CBY-ENF-{n:02d}-2026" for n in (1, 2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 15, 17, 18)] + ["SRC-CBY-EMONEY-AMD-2025-001"],
                              "22 status events name each 'Governor Decision No. N of 2026'; 31 REF-EMONEY-002 'Decision No. 4 — mobile e-money amendment'")),
    ("instruction/circular", (["SRC-CBY-FCP-INSTR-2023-001", "SRC-CBY-EMONEY-2023-001"], "31 REF-FCP-001 'Financial Consumer Protection Instructions'; REF-EMONEY-001 'Mobile e-money instructions'")),
    ("regulation", (["SRC-CBY-PSP-RULES-2022-001"], "11 VIS-E-MONEY-RULE-STACK names it the 2022 PSP framework")),
    ("provider-status instrument", (["SRC-CBY-BANKLIST-AR-2026-001", "SRC-CBY-EXCH-LIST-2026-001", "SRC-CBY-EXCH-LIST-2025-001", "SRC-CBY-UNLICENSED-EWALLET-2024-001"],
                                    "22 provider rows and roster block (official lists); PSE-001 dated negative-authority list")),
    ("method/standard", (["SRC-IMF-BPM6", "SRC-IMF-BPM6-COMP-GUIDE", "SRC-IMF-BPM7-IMPLEMENTATION"], "06 CLM-047/CLM-048: BPM6 compilation guidance and the BPM7 standard")),
    ("survey", (["SRC-WB-FINDEX-001", "SRC-OECD-INFE-2023"], "Findex microdata (DDI) and the OECD/INFE International Survey of Adult Financial Literacy")),
    ("dataset", (["SRC-WB-FINDEX-AGG-2022", "SRC-WB-WDI-REMIT-YEM-CURRENT"], "25 Findex aggregate indicator rows; WDI indicator page (06 CLM-039)")),
])
ROLE = OrderedDict([
    ("status event", DOC_KIND["decision/enforcement"][0][:-1] + ["SRC-CBY-UNLICENSED-EWALLET-2024-001"]),
    ("primary factual evidence", ["SRC-CBY-BANKLIST-AR-2026-001", "SRC-CBY-EXCH-LIST-2026-001", "SRC-CBY-EXCH-LIST-2025-001", "SRC-WB-FINDEX-AGG-2022", "SRC-WB-FINDEX-001"]),
    ("global method reference", ["SRC-IMF-BPM6", "SRC-IMF-BPM6-COMP-GUIDE", "SRC-IMF-BPM7-IMPLEMENTATION"]),
])
USE_ROLES = OrderedDict([
    ("PSE-011", "SRC-CBY-ENF-09-2026=status event"),
    ("NEG-EW-011", "SRC-CBY-UNLICENSED-EWALLET-2024-001=status event"),
    ("CLM-015", "SRC-CBY-UNLICENSED-EWALLET-2024-001=status event"),
    ("CLM-019", "SRC-CBY-EXCH-LIST-2026-001=primary factual evidence; " + "; ".join(f"SRC-CBY-ENF-{n:02d}-2026=status event" for n in (1, 2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 15, 17))),
])
VIS_NO_CONTRACT = ["VIS-BORROWING-SOURCES-2014", "VIS-DEMAND-VINTAGE-LADDER", "VIS-DOMESTIC-REMITTANCE-PATH-2014", "VIS-FINDEX-ACCESS-USE", "VIS-FINDEX-BARRIERS",
                   "VIS-FINDEX-FLOW-CHANNELS", "VIS-FINDEX-OBSERVED-WAVES", "VIS-FINDEX-RESILIENCE", "VIS-FINDEX-SAMPLE-SUPPORT", "VIS-MFI-2014-PANEL",
                   "VIS-MFI-RUPTURE-LENS", "VIS-MFI-SPINE", "VIS-PROVIDER-TIME"]


def main():
    master, spec, out_master, out_dir, ledger = sys.argv[1:6]
    os.makedirs(out_dir, exist_ok=True)
    eng = Engine(master, spec)
    wb, ed = eng.wb, eng.ed
    LEAD = leads()
    done = json.load(open(os.path.join(HERE, "ROOT_DISPOSITIONS.json"), encoding="utf-8"))
    from projection.master_reader import Workbook
    import tempfile

    def ed_grid(sheet):
        tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=out_dir)
        tmp.close()
        ed.save(tmp.name)
        try:
            return Workbook(tmp.name).grid(sheet)
        finally:
            os.remove(tmp.name)
    eng.ed_grid = ed_grid

    def substr(root):
        rows = eng.spec[root]
        keep = [r for r in rows if not (r["sheet"] == "02_SITE_MAP" and r["field"].startswith("full_copy"))]
        skipped = [r["patch_id"] for r in rows if r not in keep]
        eng.spec[root] = keep
        try:
            out = eng.apply_substr_rows(root) if keep else []
        finally:
            eng.spec[root] = rows
        if skipped:
            out.append("full_copy rows superseded by EXF-002 derivation: " + ", ".join(skipped))
        return out

    N = "04_NAV_UX"
    g4 = wb.grid(N)

    def setj(row, fn):
        cur = g4[row - 1][3]
        obj = json.loads(cur, object_pairs_hook=OrderedDict)
        fn(obj)
        ed.set_cell(N, row, 4, json.dumps(obj, ensure_ascii=False, separators=(",", ":")), expect=cur)

    def pb0420(root):
        if g4[7][0] != 3 or g4[7][1] != "Readings":
            raise RootFailure("04 r8 is not NAV-READINGS")
        ed.set_cell(N, 8, 2, "Evidence Readings", expect="Readings")
        setj(8, lambda o: o["label"].__setitem__("en", "Evidence Readings"))
        ed.set_cell(N, 29, 3, "Evidence Readings", expect="Readings")
        return ["04 r8 label_en + route_or_group label.en = Evidence Readings", "04 r29 route dictionary R-014 surface_en (propagation)"]

    def pb0421(root):
        ed.set_cell(N, 9, 2, "Data & sources", expect="Data")
        ed.set_cell(N, 9, 3, "البيانات والمصادر", expect="البيانات")
        setj(9, lambda o: o.__setitem__("label", OrderedDict([("en", "Data & sources"), ("ar", "البيانات والمصادر")])))
        ed.set_cell(N, 32, 3, "Data & sources", expect="Data")
        ed.set_cell(N, 32, 4, "البيانات والمصادر", expect="البيانات")
        return ["04 r9 labels + JSON = Data & sources / البيانات والمصادر", "04 r32 route dictionary R-017 surfaces (propagation)"]

    def pb0422(root):
        ed.set_cell(N, 10, 2, "Method & Measurement", expect="Methodology")
        ed.set_cell(N, 10, 3, "المنهج والقياس", expect="المنهجية")
        cur = g4[9][3]
        grp = OrderedDict([("id", "NAV-METHOD-MEASUREMENT"), ("label", OrderedDict([("en", "Method & Measurement"), ("ar", "المنهج والقياس")])), ("kind", "GROUP"),
                           ("children", [OrderedDict([("id", "NAV-METHODOLOGY"), ("label", OrderedDict([("en", "Methodology"), ("ar", "المنهجية")])), ("route", "/methodology")]),
                                         OrderedDict([("id", "NAV-MEASUREMENT"), ("label", OrderedDict([("en", "Measurement Agenda"), ("ar", "أجندة القياس")])), ("route", "/measurement")])])])
        ed.set_cell(N, 10, 4, json.dumps(grp, ensure_ascii=False, separators=(",", ":")), expect=cur)
        if g4[30][:2] != ["R-016", "/measurement"] or g4[30][5] is not False:
            raise RootFailure("04 r31 is not R-016 /measurement with in_primary_nav False")
        ed.set_cell(N, 31, 6, True)
        return ["04 r10 = navigation family Method & Measurement with two routed children (/methodology, /measurement); no route change",
                "04 r31 route dictionary R-016 /measurement in_primary_nav = True (child)"]

    def pb0423(root):
        if g4[10][1] != "About":
            raise RootFailure("04 r11 is not NAV-ABOUT")
        if g4[33][:2] != ["R-019", "/about"] or g4[33][5] is not True:
            raise RootFailure("04 r34 is not R-019 /about with in_primary_nav True")
        ed.set_cell(N, 34, 6, False)
        eng._trust_pending = True
        return ["04 r11 NAV-ABOUT leaves the primary navigation (row removed at stage end)", "04 'Trust navigation' block: About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact (AR About = «عن الموقع», correction G)",
                "04 r34 route dictionary R-019 /about in_primary_nav = False", "navigation_interaction.json: /measurement/ entry_modes + global_navigation, prominence PRIMARY_CHILD; /about/ SECONDARY_TRUST; /about/ removed from footer group method_measure and added to trust_use"]

    def pb0424(root):
        return {"implemented_in": "scripts/projection/derived.py navigation_contract (global_navigation items with children; trust_navigation) and scripts/validate.py (every child routed; group ≥2 routed children; both Method & Measurement children present)"}

    def pb0412(root):
        eng._strapline = True
        return ["04 'Governed interface copy' row UI-FOOTER-STRAPLINE", "scripts/build.py footer renders the governed row"]

    def pb0492(root):
        eng._aliases = True
        return ["04 block 'Search aliases' rows SEARCH-ALIAS-001…012", "content/search_aliases.json; site-src/app.js and the validator's search mirror apply them"]

    def pb0390(root):
        S = "15_SOURCE_LIBRARY"
        g = wb.grid(S)
        h = g[3]
        base = len(h)
        cols = ["issuer", "hosting_platform", "rights_state", "licence", "attribution_requirement", "retrieval_date", "document_type", "evidence_roles"]
        for j, c in enumerate(cols, 1):
            ed.set_cell(S, 4, base + j, c, expect=None)
        kinds, roles = {}, {}
        for k, (ids, _) in DOC_KIND.items():
            for s in ids:
                kinds[s] = k
        for r_, ids in ROLE.items():
            for s in ids:
                roles.setdefault(s, []).append(r_)
        n = Counter()
        for i in range(5, len(g) + 1):
            sid = g[i - 1][0]
            if not sid:
                continue
            ed.set_cell(S, i, base + 3, "NOT_ASSESSED", expect=None)
            n["rows"] += 1
            if sid == "SRC-CBY-ENF-18-2026":
                ed.set_cell(S, i, base + 6, "2026-09-25", expect=None)
            if sid in kinds:
                ed.set_cell(S, i, base + 7, kinds[sid], expect=None); n["document_type"] += 1
            if sid in roles:
                ed.set_cell(S, i, base + 8, "; ".join(roles[sid]), expect=None); n["evidence_roles"] += 1
        missing = [s for s in list(kinds) + list(roles) if not any(g[i - 1][0] == s for i in range(5, len(g) + 1))]
        if missing:
            raise RootFailure(f"source IDs for kinds/roles not in 15: {missing}")
        eng._c15 = cols
        return {"columns": cols, "rights_state": f"NOT_ASSESSED on {n['rows']} rows", "document_type_rows": n["document_type"], "evidence_roles_rows": n["evidence_roles"],
                "issuer_hosting_publisher": "left empty (not confirmed from the source or authoritative metadata; PB-0390P SOURCE_PENDING)",
                "retrieval_date": "recorded for SRC-CBY-ENF-18-2026 only (verified 2026-09-25); other retrieval dates are not reconstructed",
                "document_type_basis": {k: v[1] for k, v in DOC_KIND.items()}}

    def pb0401(root):
        S = "06_EVIDENCE_OBJECTS"
        g = wb.grid(S)
        h = g[3]
        c1, c2 = len(h) + 1, len(h) + 2
        ed.set_cell(S, 4, c1, "visual_contract_state", expect=None)
        ed.set_cell(S, 4, c2, "source_use_roles", expect=None)
        rows = {r[0]: i for i, r in enumerate(g, 1) if i > 4 and r and r[0]}
        vis11 = {r[0] for r in wb.grid("11_VISUAL_LIBRARY")[4:] if r and r[0]}
        for v in VIS_NO_CONTRACT:
            if v in vis11:
                raise RootFailure(f"{v} has an 11 contract")
            ed.set_cell(S, rows[v], c1, "NO_GOVERNED_CONTRACT__TABLE_ONLY", expect=None)
        for oid, val in USE_ROLES.items():
            deps = str(g[rows[oid] - 1][h.index("source_dependencies")] or "")
            for part in val.split("; "):
                if part.split("=")[0] not in deps:
                    raise RootFailure(f"{oid}: source_use_roles names {part.split('=')[0]}, which is not bound to the record")
            ed.set_cell(S, rows[oid], c2, val, expect=None)
        eng._c06 = True
        return {"visual_contract_state": f"NO_GOVERNED_CONTRACT__TABLE_ONLY on {len(VIS_NO_CONTRACT)} records (method text not rendered while the state holds)",
                "source_use_roles": f"populated for {list(USE_ROLES)} (PB-0493b relationship-level roles where the Master states the use); other records unassigned"}

    def code(what):
        return lambda root: {"implemented_in": what}

    handlers = {"PB-0420": pb0420, "PB-0421": pb0421, "PB-0422": pb0422, "PB-0423": pb0423, "PB-0424": pb0424, "PB-0412": pb0412,
                "PB-0492": pb0492, "PB-0390": pb0390, "PB-0401": pb0401,
                "PB-0402": code("scripts/projection/derived.py _page_bindings: an /evidence/VIS-*/ page whose instance is an 11 contract binds that contract (and so its prohibited inferences)"),
                "PB-0491": code("search_index.json boundary_text_en/ar (does_not_prove / prohibited_inference / limitations, low weight); site-src/app.js normalisation (Arabic hamza/alef/ta-marbuta, definite article; English light stemming) mirrored in scripts/validate.py"),
                "PB-0493": code("(a) domain-page title/question boost; (b) 15 document_type + evidence_roles, 06 source_use_roles (see PB-0390/PB-0401 details); (c) result cards show record type, evidence period/currentness or document type"),
                "PB-0494": code("navigation_interaction.json search_smoke_tests: 9 kept + 12 added; validator requires the primary expected route in the top 3 for the added tests")}
    order = []
    for root, rows in eng.spec.items():
        if root in done and done[root]["disposition"] not in ("PENDING",):
            continue
        lead = LEAD.get(root, "?")
        if lead in S4_LEADS or root in ("PB-0412", "PB-0390", "PB-0401", "PB-0402"):
            order.append(root)
    for root in order:
        st = eng.spec[root][0]["Claude_status"]
        if "SUPERSEDED" in st:
            eng.hold(root, "SUPERSEDED", STAGE, "Superseded by recipient acceptance correction G (the Arabic About label stays «عن الموقع»).")
        elif root == "PB-0490":
            eng.hold(root, "SUPERSEDED", STAGE, "Superseded by EXF-001 and acceptance correction F: every source with a public (http/https) locator is indexed; the nine sources without a public locator (eight privately supplied files, SRC-MOPIC-YSEU-2023-080) must not appear in public search; publisher and document type are shown only where confirmed (PB-0390/PB-0493b).")
        else:
            eng.run_root(root, handlers.get(root, substr), STAGE)
    # ---- appended 04 rows/blocks (after every cell edit), then the NAV-ABOUT row removal ----
    g4now = ed_grid(N)
    last = max(i for i, r in enumerate(g4now, 1) if any(c not in (None, "") for c in r))
    if g4now[last - 1][0] != "UI-EVID-MEMBERS-HEADING":
        raise SystemExit("04: governed interface copy block is not the last block")
    row = last + 1
    if getattr(eng, "_strapline", False):
        for j, v in enumerate(["UI-FOOTER-STRAPLINE", "Developed and maintained by CauseWay. A public resource linking each claim to its evidence and original source.",
                               "طوّرتها وتديرها CauseWay. مورد عام يربط كل خلاصة بدليلها ومصدرها الأصلي.", "PB-0412. Footer strapline (replaces the hard-coded build.py string)."], 1):
            ed.set_cell(N, row, j, v, expect=None)
        row += 1
    blocks_added = []
    if getattr(eng, "_trust_pending", False):
        row += 1
        ed.set_cell(N, row, 1, "Trust navigation", expect=None)
        for j, v in enumerate(["item_order", "label_en", "label_ar", "route"], 1):
            ed.set_cell(N, row + 1, j, v, expect=None)
        for k, (en, ar, rt) in enumerate(TRUST_NAV, 1):
            for j, v in enumerate([k, en, ar, rt], 1):
                ed.set_cell(N, row + 1 + k, j, v, expect=None)
        row = row + 2 + len(TRUST_NAV)
        blocks_added.append("Trust navigation")
    if getattr(eng, "_aliases", False):
        row += 1
        ed.set_cell(N, row, 1, "Search aliases", expect=None)
        for j, v in enumerate(["alias_id", "terms_en", "terms_ar", "targets", "boundary_note_en", "boundary_note_ar"], 1):
            ed.set_cell(N, row + 1, j, v, expect=None)
        for k, a in enumerate(ALIASES, 1):
            for j, v in enumerate(a, 1):
                if v not in (None, ""):
                    ed.set_cell(N, row + 1 + k, j, v, expect=None)
        blocks_added.append("Search aliases")
    if getattr(eng, "_trust_pending", False):
        ed.delete_rows(N, 11, 11)
    eng.run_root("EXF-002", lambda r: regenerate_full_copy(eng, STAGE), STAGE)
    data = ed.save(out_master)
    # ---- controlled files ----
    ms = json.load(open(os.path.join(ROOT, "scripts/projection/master_structure.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    sh = ms["sheets"]
    for b in blocks_added:
        sh[N]["blocks"].append(OrderedDict([("title", b), ("header", True)]))
    if getattr(eng, "_c15", None):
        sh["15_SOURCE_LIBRARY"]["main_labels"] += eng._c15
    if getattr(eng, "_c06", None):
        sh["06_EVIDENCE_OBJECTS"]["main_labels"] += ["visual_contract_state", "source_use_roles"]
    json.dump(ms, open(os.path.join(out_dir, "master_structure.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(out_dir, "master_structure.json"), "a").write("\n")
    nav = json.load(open(os.path.join(ROOT, "site-src/content/content/navigation_interaction.json"), encoding="utf-8"), object_pairs_hook=OrderedDict)
    if getattr(eng, "_trust_pending", False):
        for r in nav["routes"]:
            if r["route"] == "/measurement/":
                if "global_navigation" not in r["entry_modes"]:
                    r["entry_modes"].insert(1, "global_navigation")
                r["navigation_prominence"] = "PRIMARY_CHILD"
            if r["route"] == "/methodology/":
                r["navigation_prominence"] = "PRIMARY_CHILD"
            if r["route"] == "/about/":
                r["entry_modes"] = [m if m != "global_navigation" else "trust_navigation" for m in r["entry_modes"]]
                r["navigation_prominence"] = "SECONDARY_TRUST"
            if r["route"] in ("/corrections/", "/rights/", "/accessibility/", "/privacy/", "/terms/", "/contact/") and "trust_navigation" not in r["entry_modes"]:
                r["entry_modes"].insert(1, "trust_navigation")
                r["navigation_prominence"] = "SECONDARY_TRUST"
        for grp in nav["footer_groups"]:
            if grp["id"] == "method_measure":
                grp["links"] = [l for l in grp["links"] if l["route"] != "/about/"]
            if grp["id"] == "trust_use" and not any(l["route"] == "/about/" for l in grp["links"]):
                grp["links"].insert(0, OrderedDict([("route", "/about/"), ("label_en", "About"), ("label_ar", "عن الموقع")]))
            if grp["id"] == "explore_verify":
                for l in grp["links"]:
                    if l["route"] == "/readings/":
                        l["label_en"] = "Evidence Readings"
    tests = nav.get("search_smoke_tests", [])
    NEW_TESTS = [("law", "قانون", ["/reforms/", "/data/"]), ("regulation", "لائحة", ["/reforms/", "/data/"]), ("decision", "قرار", ["/providers/", "/reforms/", "/data/"]),
                 ("remittances", "الحوالات", ["/remittances/"]), ("POS terminals", "نقاط البيع", ["/payments/"]), ("income", "الدخل", ["/people/"]),
                 ("financial literacy", "الثقافة المالية", ["/people/", "/reforms/"]), ("microfinance", "التمويل الأصغر", ["/finance/", "/readings/microfinance-structural-divergence/"]),
                 ("exchange rate", "سعر الصرف", ["/finance/", "/data/"]), ("measurement agenda", "أجندة القياس", ["/measurement/"]),
                 ("e-wallet", "المحافظ الإلكترونية", ["/payments/", "/providers/"]), ("credit", "الائتمان", ["/finance/", "/firms/"])]
    if eng.results.get("PB-0494", {}).get("disposition") == "APPLIED" and not any(t.get("rule") for t in tests):
        for en, ar, exp in NEW_TESTS:
            tests.append(OrderedDict([("query_en", en), ("query_ar", ar), ("expected_routes", exp), ("rule", "PRIMARY_EXPECTED_ROUTE_IN_TOP_3"), ("basis", "PB-0494 (SEARCH_DISCOVERY_CLOSURE.md §2)")]))
    with open(os.path.join(out_dir, "navigation_interaction.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(nav, ensure_ascii=False, indent=2) + "\n")
    rep = OrderedDict([("stage", STAGE), ("input_master_sha256", hashlib.sha256(open(master, "rb").read()).hexdigest()),
                       ("output_master_sha256", hashlib.sha256(data).hexdigest()), ("cells_and_ops", len(ed.log)), ("blocks_added", blocks_added), ("results", eng.results)])
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(Counter(v["disposition"] for v in eng.results.values()))
    for k, v in eng.results.items():
        if v["disposition"] != "APPLIED":
            print(k, v["disposition"], str(v["detail"])[:220])
    print(rep["output_master_sha256"])


if __name__ == "__main__":
    main()
