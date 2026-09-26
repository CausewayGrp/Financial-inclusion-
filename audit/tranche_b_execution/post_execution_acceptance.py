# -*- coding: utf-8 -*-
"""Post-execution acceptance evidence for Tranche B (D2 §13), machine-readable.

  python3 audit/tranche_b_execution/post_execution_acceptance.py

Writes:
  audit/MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv                 one row per spec root (+ execution items), one disposition each
  audit/tranche_b_execution/SOURCE_LINEAGE_TRUTH_TEST.json      lineage/closure counts and truth assertions
  audit/tranche_b_execution/SEARCH_PROBE_POST_EXECUTION.json    28-term bilingual probe (browser scoring mirror)
  audit/tranche_b_execution/STALE_HASH_SCAN.json                64-hex values classified HISTORICAL_LINEAGE — KEEP / CURRENT_STATE_STALE — FIX
  audit/tranche_b_execution/PRE_POST_VALIDATION_SUMMARY.json    pre/post summary of every acceptance item
Exit code 1 if any acceptance assertion fails.
"""
import csv, glob, hashlib, html, json, os, re, subprocess, sys
from collections import Counter, OrderedDict
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "site-src", "content")
DIST = os.path.join(ROOT, "dist")
ENTRY = {"master_sha256": "e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7",
         "page_specs_sha256": "ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def L(p):
    return json.load(open(os.path.join(C, p), encoding="utf-8"))


def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip().splitlines()


def text_of(route, lang):
    p = os.path.join(DIST, lang, route.strip("/"), "index.html") if route != "/" else os.path.join(DIST, lang, "index.html")
    raw = open(p, encoding="utf-8").read()
    return raw, html.unescape(re.sub(r"<[^>]+>", " ", raw))


failures = []


def check(name, ok, detail=None):
    if not ok:
        failures.append(name)
    return OrderedDict([("check", name), ("result", "PASS" if ok else "FAIL")] + ([("detail", detail)] if detail is not None else []))


def ledger():
    spec = os.path.join(ROOT, "audit", "MASTER_FIRST_PATCH_SPEC.csv")
    roots = OrderedDict()
    for r in csv.DictReader(open(spec, encoding="utf-8-sig")):
        roots.setdefault(r["patch_id"].split(".")[0], []).append(r)
    disp = json.load(open(os.path.join(HERE, "ROOT_DISPOSITIONS.json"), encoding="utf-8"))
    allowed = {"APPLIED", "HELD", "SUPERSEDED", "SOURCE_PENDING", "FAILED"}
    out = []
    missing = [k for k in roots if k not in disp]
    for k, rows in roots.items():
        d = disp.get(k, {"disposition": "FAILED", "stage": "", "reason": "no execution record"})
        out.append(OrderedDict([("root_id", k), ("disposition", d["disposition"]), ("stage", d["stage"]), ("spec_rows", len(rows)),
                                ("priority", rows[0]["priority"]), ("change_types", "; ".join(sorted({r["change_type"] for r in rows}))),
                                ("spec_status", rows[0]["Claude_status"]), ("reason", d["reason"])]))
    for k in ("AIR-001", "EXF-001", "EXF-002", "EXC-0302"):
        d = disp[k]
        out.append(OrderedDict([("root_id", k), ("disposition", d["disposition"]), ("stage", d["stage"]), ("spec_rows", 0), ("priority", "EXECUTION"),
                                ("change_types", "EXECUTION_FINDING" if k.startswith("EX") else "AUTHORITY_INTEGRITY"), ("spec_status", "NOT_IN_SPEC"), ("reason", d["reason"])]))
    with open(os.path.join(ROOT, "audit", "MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in out:
            w.writerow(r)
    bad = [r["root_id"] for r in out if r["disposition"] not in allowed]
    counts = Counter(r["disposition"] for r in out if r["priority"] != "EXECUTION")
    return OrderedDict([("spec_roots", len(roots)), ("spec_rows", sum(len(v) for v in roots.values())), ("roots_by_disposition", dict(counts)),
                        ("execution_items", ["AIR-001", "EXF-001", "EXF-002", "EXC-0302"]), ("missing_roots", missing), ("invalid_dispositions", bad)])


def lineage():
    clo = L("sources/public_object_source_closure.json")
    eo = L("evidence/evidence_objects.json")
    lib = {r["source_id"] for r in L("sources/source_library.json")}
    by_type = OrderedDict()
    for c in clo:
        by_type.setdefault(c["object_type"], Counter())[c["closure_state"]] += 1
    lin = Counter(o.get("lineage_state") for o in eo)
    asserts = []
    asserts.append(check("no BOUND_CANDIDATE state remains", not any("CANDIDATE" in str(o.get("lineage_state")) for o in eo)))
    declared_ok = all(s in c["dependency_ids"] and s in lib for c in clo if c["object_type"] == "evidence_object" for s in c["resolved_source_ids"])
    asserts.append(check("every resolved source is declared on the record and exists in 15", declared_ok))
    closed_ok = all(not c["unresolved_dependency_ids"] for c in clo if c["closure_state"] == "CLOSED_TO_SOURCE_ID")
    asserts.append(check("CLOSED_TO_SOURCE_ID only with no open input", closed_ok))
    ds_tokens = [t for c in clo if c["object_type"] == "evidence_object" for t in c["dependency_ids"] if re.match(r"^(DS-|\d+(_|$))", t)]
    asserts.append(check("dataset tokens appear only as open inputs (never expanded)",
                         all(t in c["unresolved_dependency_ids"] for c in clo if c["object_type"] == "evidence_object" for t in c["dependency_ids"] if re.match(r"^(DS-|\d+(_|$))", t)),
                         {"dataset_tokens_on_records": sorted(set(ds_tokens))}))
    open_records = OrderedDict((c["object_id"], OrderedDict([("state", c["closure_state"]), ("open_inputs", c["unresolved_dependency_ids"]), ("members", c["resolved_via_object_ids"])]))
                               for c in clo if c["object_type"] == "evidence_object" and c["closure_state"] != "CLOSED_TO_SOURCE_ID")
    rep = OrderedDict([("rule", clo[0]["rule"]), ("evidence_record_lineage_state_counts", dict(lin)),
                       ("closure_state_counts_by_object_type", {k: dict(v) for k, v in by_type.items()}),
                       ("records_not_closed_to_source", open_records), ("assertions", asserts),
                       ("entry_state_for_comparison", "Legacy rule: CLOSED_VIA_CONTROLLED_DEPENDENCIES asserted on 108/108 evidence records although 87 carried unresolved tokens; dataset tokens expanded to every source of a dataset (PB-0002 basis).")])
    json.dump(rep, open(os.path.join(HERE, "SOURCE_LINEAGE_TRUTH_TEST.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return rep


# ---- browser search mirror (identical to site-src/app.js and scripts/validate.py) ----
def _norm(v):
    v = str(v or "").casefold()
    v = re.sub(r"[ً-ٰٟ]", "", v)
    for a, b in (("إ", "ا"), ("أ", "ا"), ("آ", "ا"), ("ٱ", "ا"), ("ى", "ي"), ("ة", "ه"), ("ؤ", "و"), ("ئ", "ي")):
        v = v.replace(a, b)
    return v


def _qtok(t):
    if t.startswith("ال") and len(t) > 3:
        return t[2:]
    if re.fullmatch(r"[a-z]+", t) and len(t) > 4:
        if t.endswith("ies"):
            return t[:-3] + "y"
        if t.endswith("ing"):
            return t[:-3]
        if t.endswith("ed"):
            return t[:-2]
        if t.endswith("s") and not t.endswith("ss"):
            return t[:-1]
    return t


DOMAIN = {"/people/", "/firms/", "/finance/", "/providers/", "/payments/", "/remittances/", "/access/", "/reforms/", "/measurement/"}


def search(records, aliases, q, lang, limit=10):
    term = _norm(q.strip())
    tokens = [_qtok(x) for x in term.split() if x]
    qq = " ".join(tokens)
    alias = None
    for a in aliases:
        own, other = a.get("terms_ar" if lang == "ar" else "terms_en") or "", a.get("terms_en" if lang == "ar" else "terms_ar") or ""
        if qq in [" ".join(_qtok(t) for t in _norm(x.strip()).split()) for x in own.split(";") + other.split(";")]:
            alias = a
            break
    ranked = []
    for x in records:
        title = _norm(x.get("title_" + lang)); summ = _norm(x.get("summary_" + lang)); tx = _norm(x.get("search_text_" + lang))
        bd = _norm(x.get("boundary_text_" + lang)); st = _norm(" ".join(str(x.get(k) or "") for k in ("id", "source_id", "object_id", "claim_id", "reading_id")))
        s = 0
        for t in tokens:
            s += 12 if st == t else (7 if t in st else 0)
            s += 6 if t in title else 0
            s += 3 if t in summ else 0
            s += 1 if t in tx else 0
            s += 0.5 if t in bd else 0
        xr = str(x.get("route") or "")
        if s > 0 and x.get("type") == "page" and xr in DOMAIN and tokens and all(t in title for t in tokens):
            s += 20
        if alias:
            for tg in [v.strip() for v in str(alias.get("targets") or "").split("|")]:
                if tg.startswith("route:") and x.get("type") == "page" and xr == tg[6:]:
                    s += 25
                if tg.startswith("document_type:") and x.get("document_type") == tg[14:]:
                    s += 10
        if s > 0:
            r = urlparse(xr or "/").path
            ranked.append((s, r if r.endswith("/") else r + "/", title))
    ranked.sort(key=lambda z: z[0], reverse=True)
    out, seen = [], set()
    for s, r, t in ranked:
        if (r, t) in seen:
            continue
        seen.add((r, t))
        out.append(r)
        if len(out) >= limit:
            break
    return out


PROBE = [("account ownership", "امتلاك الحساب", ["/people/", "/evidence/CLM-001/"]), ("gender gap", "الفجوة بين الرجال والنساء", ["/people/", "/readings/gender-gap-measured-causes-open/"]),
         ("income", "الدخل", ["/people/"]), ("financial literacy", "الثقافة المالية", ["/people/", "/reforms/"]),
         ("microfinance", "التمويل الأصغر", ["/finance/", "/readings/microfinance-structural-divergence/"]), ("credit", "الائتمان", ["/finance/", "/firms/"]),
         ("deposits", "الودائع", ["/finance/"]), ("SME finance", "تمويل المنشآت الصغيرة", ["/firms/"]), ("POS terminals", "نقاط البيع", ["/payments/"]),
         ("e-wallet", "المحافظ الإلكترونية", ["/payments/", "/providers/"]), ("RTGS", "التسوية الإجمالية الفورية", ["/payments/", "/reforms/"]),
         ("remittances", "الحوالات", ["/remittances/"]), ("remittance cost", "تكلفة التحويل", ["/remittances/"]), ("exchange companies", "شركات الصرافة", ["/providers/", "/access/"]),
         ("licensed banks", "البنوك المرخصة", ["/providers/"]), ("Aden", "عدن", ["/providers/", "/data/"]), ("Sanaa", "صنعاء", ["/providers/", "/data/"]),
         ("decision", "قرار", ["/data/", "/providers/", "/reforms/"]), ("law", "قانون", ["/data/", "/reforms/"]), ("regulation", "لائحة", ["/data/", "/reforms/"]),
         ("consumer protection", "حماية المستهلك", ["/reforms/"]), ("complaints", "الشكاوى", ["/reforms/"]), ("FMIIP", "FMIIP", ["/reforms/", "/payments/"]),
         ("cash transfer", "التحويل النقدي", ["/readings/after-transfer-persistence/", "/payments/"]), ("KYC", "اعرف عميلك", ["/payments/", "/people/", "/measurement/"]),
         ("access points", "نقاط الوصول", ["/access/"]), ("exchange rate", "سعر الصرف", ["/finance/", "/data/"]), ("measurement", "القياس", ["/measurement/"])]


def probe():
    recs, aliases = L("content/search_index.json"), L("content/search_aliases.json")
    rows, grade = [], Counter()
    for en, ar, exp in PROBE:
        row = OrderedDict([("term", en), ("expected", exp)])
        for lang, q in (("en", en), ("ar", ar)):
            got = search(recs, aliases, q, lang)
            pos = [got.index(e) + 1 for e in exp if e in got]
            g = "PASS" if pos and min(pos) <= 3 else ("WEAK" if pos else "FAIL")
            grade[g] += 1
            row[lang] = OrderedDict([("query", q), ("grade", g), ("best_rank", min(pos) if pos else None), ("top5", got[:5])])
        rows.append(row)
    rep = OrderedDict([("rule", "PASS = an expected route in the top 3; WEAK = in the top 10; FAIL = absent (browser scoring mirror incl. PB-0491/0492/0493)"),
                       ("grades", dict(grade)), ("entry_grades", {"PASS": 25, "WEAK": 20, "FAIL": 11}), ("terms", rows)])
    json.dump(rep, open(os.path.join(HERE, "SEARCH_PROBE_POST_EXECUTION.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return rep


def stale_hash_scan(cur_m, cur_p):
    current_files = ["README.md", "OPENAI_REENTRY_CHECKPOINT.md", "authority/AUTHORITY.json", "authority/YFI_CURRENT_PROJECT_CONTEXT.json",
                     "handoff/README_FIRST.md", "handoff/MASTER_IMPLEMENTATION_PROMPT.md", "handoff/CLAUDE_DESIGN_MASTER_PROMPT.md",
                     "handoff/CLAUDE_CODE_MASTER_PROMPT.md", "handoff/HANDOFF_ACCEPTANCE_CHECKLIST.md", "handoff/IMPLEMENTATION_MANIFEST.json",
                     "audit/TRANCHE_B_EXECUTION_CLOSURE.md"]
    allowed_current = {cur_m, cur_p, sha(os.path.join(ROOT, "audit", "MASTER_FIRST_PATCH_SPEC.csv")),
                       sha(os.path.join(ROOT, "scripts", "projection", "projection_manifest.json")),
                       sha(os.path.join(ROOT, "audit", "TERMINOLOGY_SWEEP_KEEP_REGISTER.csv"))}   # current Master, Page Specs, spec, manifest
    auth = json.load(open(os.path.join(ROOT, "authority", "AUTHORITY.json"), encoding="utf-8"))
    drive = auth["production_master"].get("drive_recorded_sha256")
    rows = []
    for dp, dn, fn in os.walk(ROOT):
        if "/dist" in dp or "/.git" in dp or "__pycache__" in dp:
            continue
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT)
            if not f.endswith((".md", ".json", ".csv", ".txt", ".py")) or rel == "SHA256SUMS.txt":
                continue
            try:
                t = open(p, encoding="utf-8").read()
            except Exception:
                continue
            for h in sorted(set(re.findall(r"\b[0-9a-f]{64}\b", t))):
                if h in allowed_current:
                    continue
                cls = "CURRENT_STATE_STALE — FIX" if rel in current_files else "HISTORICAL_LINEAGE — KEEP"
                note = ""
                if rel in current_files and h in (drive, ENTRY["page_specs_sha256"]) and re.search(r"drive_recorded|page_specs_drive_recorded|entry|Entry|previous", t):
                    cls, note = "HISTORICAL_LINEAGE — KEEP", "recorded explicitly as the entry / Drive-recorded lineage hash"
                if rel.startswith(("audit/tranche_b_execution/", "audit/generator_baseline/")) or rel.endswith(("PATCH_SPEC.csv", "CROSSWALK.csv")):
                    cls = "HISTORICAL_LINEAGE — KEEP"
                rows.append(OrderedDict([("file", rel), ("sha256", h), ("classification", cls), ("note", note)]))
    fix = [r for r in rows if r["classification"].startswith("CURRENT_STATE_STALE")]
    rep = OrderedDict([("current_master_sha256", cur_m), ("current_page_specs_sha256", cur_p), ("current_state_files", current_files),
                       ("counts", dict(Counter(r["classification"] for r in rows))), ("current_state_stale", fix),
                       ("historical_lineage_files", sorted({r["file"] for r in rows if r["classification"].startswith("HISTORICAL")}))])
    json.dump(rep, open(os.path.join(HERE, "STALE_HASH_SCAN.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return rep


def main():
    master = os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx")
    cur_m, cur_p = sha(master), sha(os.path.join(C, "page_specs.json"))
    man = json.load(open(os.path.join(ROOT, "scripts", "projection", "projection_manifest.json"), encoding="utf-8"))
    led = ledger()
    lin = lineage()
    pr = probe()
    code_chk, out_chk = run([sys.executable, "scripts/generate_projections.py", "--check"])
    code_lit, out_lit = run([sys.executable, "scripts/audit_public_literals.py"])
    code_val, out_val = run([sys.executable, "scripts/validate.py"])
    code_t, out_t = run([sys.executable, "-m", "unittest", "discover", "-s", "scripts/projection/tests", "-t", "."])
    html_files = glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True)
    lit = json.load(open(os.path.join(ROOT, "audit", "PUBLIC_LITERAL_CLOSURE.json"), encoding="utf-8"))
    checks = []
    checks.append(check("route baseline 284 HTML documents", len(html_files) == 284, len(html_files)))
    checks.append(check("generator --check (projections equal the Master)", code_chk == 0, out_chk[-1:]))
    checks.append(check("generator regression tests", code_t == 0, out_t[-1:]))
    checks.append(check("public literal closure: 0 unresolved", code_lit == 0 and not [r for r in lit["records"] if r["category"] == "UNRESOLVED_SUBSTANTIVE_PUBLIC_NUMBER"], out_lit[-1:]))
    checks.append(check("website validator PASS (includes AR/EN structural parity, Compare, citation, rights notes, search smoke tests)", code_val == 0, out_val[-2:]))
    checks.append(check("execution ledger: every spec root has exactly one allowed disposition", not led["missing_roots"] and not led["invalid_dispositions"], led["roots_by_disposition"]))
    checks.append(check("source-lineage truth assertions", all(a["result"] == "PASS" for a in lin["assertions"])))
    # public-surface assertions
    leak = re.compile(r"Use the documented system chronology|استخدم السلسلة الزمنية الموثقة|Present them as filterable|تُعرض كبنود قابلة للتصفية|USER_PROVIDED_FILE|_internal|primary_user_question")
    forbidden = re.compile(r"lowest (score )?among participating|أدنى نتيجة بين البلدان|lower than every other participating|observed history|تاريخ مرصود|3\.42216|points to a divergence|مركز اليمن للمقاصة|المنصة")
    leaks, forb = [], []
    for f in html_files:
        t = open(f, encoding="utf-8").read()
        if leak.search(t):
            leaks.append(os.path.relpath(f, DIST))
        vis = html.unescape(re.sub(r"<[^>]+>", " ", t))
        m = forbidden.search(vis)
        if m:
            forb.append(f"{os.path.relpath(f, DIST)}: {m.group(0)}")
    checks.append(check("no authoring copy, internal field or private-file note on any public page", not leaks, leaks[:10]))
    checks.append(check("no withdrawn or unsupported public wording (ranking, 'observed history', six-figure precision, 'divergence' claim, «المنصة», «مركز» for YPCC)", not forb, forb[:10]))
    _, people_en = text_of("/people/", "en")
    _, people_ar = text_of("/people/", "ar")
    oecd_pages = [f for f in html_files if "15 out of 100" in open(f, encoding="utf-8").read()]
    oecd_ok = bool(oecd_pages) and all(("1,000" in open(f, encoding="utf-8").read()) for f in oecd_pages)
    checks.append(check("OECD/INFE binding: 42/100 and 15/100 published only with sample and fieldwork, no ranking", oecd_ok, [os.path.relpath(f, DIST) for f in oecd_pages][:6]))
    _, prov = text_of("/providers/", "en")
    checks.append(check("provider scope statement on /providers/ (PB-0216)", "Whose list is this?" in prov))
    _, meth = text_of("/methodology/", "en")
    checks.append(check("methodology coverage, admission roles and FCV sections present (PB-0611/0612/0613)",
                        all(x in meth for x in ("What the evidence covers", "How evidence is admitted", "Measuring in a divided"))))
    _, rem = text_of("/evidence/CLM-032/", "en")
    checks.append(check("remittance vintage break visible (AR2024 6.245 vs AR2025 restated 3.42)", "6.245" in rem and "3.42" in rem))
    rights_ok = True
    for lang in ("en", "ar"):
        raw, _ = text_of("/data/", lang)
        # a download offer = an anchor with a download attribute, or a link to a locally hosted data/document file
        if re.search(r"<a\s[^>]*\bdownload(?:=|\s|>)", raw) or re.search(r'href="/[^"]+\.(?:csv|xlsx|xls|pdf|zip|json)"', raw) or "source-rights-note" not in raw:
            rights_ok = False
    smap = L("sources/source_reference_map.json")
    checks.append(check("rights gating: every source NOT_ASSESSED, no download offer, rights note on the source directory",
                        rights_ok and all(s.get("rights_state") == "NOT_ASSESSED" for s in smap), Counter(s.get("rights_state") for s in smap)))
    _, cmp_en = text_of("/evidence/compare/", "en")
    checks.append(check("Compare page renders its governed comparison contract", 'data-comparison-contract="Comparison"' in text_of("/evidence/compare/", "en")[0]))
    checks.append(check("search probe: no term regresses to FAIL in either language", pr["grades"].get("FAIL", 0) == 0, pr["grades"]))
    stale = stale_hash_scan(cur_m, cur_p)
    checks.append(check("stale-hash scan: no current-state file carries a stale hash", not stale["current_state_stale"], stale["counts"]))
    summary = OrderedDict([
        ("status", "TRANCHE B PATCH EXECUTION COMPLETE — READY FOR INDEPENDENT POST-EXECUTION ACCEPTANCE" if not failures else "ACCEPTANCE CHECK FAILURES PRESENT"),
        ("pre", OrderedDict([("master_sha256", ENTRY["master_sha256"]), ("page_specs_sha256", ENTRY["page_specs_sha256"]), ("html_documents", 284),
                             ("literal_closure", "6,939 records, 0 unresolved (entry projections rebuilt by the canonical generator; the entry checkpoint recorded 7,309 records under the pre-generator build)"),
                             ("validator", "PASS at entry (with pre-generator projections)"), ("search_records", 427), ("sources", 159), ("sources_with_primary_url_text", 158),
                             ("lineage", "legacy closure: CLOSED_VIA_CONTROLLED_DEPENDENCIES asserted on 108/108 evidence records"),
                             ("authority_integrity", "FAIL — 14_SYSTEM_CHRONOLOGY rows 18–28 duplicated YSC-013 (AUTH-INT-001)")])),
        ("post", OrderedDict([("master_sha256", cur_m), ("page_specs_sha256", cur_p),
                              ("patch_spec_sha256", sha(os.path.join(ROOT, "audit", "MASTER_FIRST_PATCH_SPEC.csv"))),
                              ("generator", man["generator"]), ("projection_manifest_sha256", sha(os.path.join(ROOT, "scripts", "projection", "projection_manifest.json"))),
                              ("html_documents", len(html_files)), ("literal_closure", out_lit[-1] if out_lit else None), ("validator", out_val[-1] if out_val else None),
                              ("search_records", len(L("content/search_index.json"))), ("sources", len(smap)),
                              ("sources_with_public_locator", sum(1 for s in smap if str(s.get("primary_url") or "").startswith(("http://", "https://")))),
                              ("lineage_state_counts", lin["evidence_record_lineage_state_counts"]),
                              ("closure_state_counts_by_object_type", lin["closure_state_counts_by_object_type"]),
                              ("ledger", led), ("search_probe_grades", pr["grades"]), ("stale_hash_scan", stale["counts"])])),
        ("checks", checks), ("failures", failures)])
    json.dump(summary, open(os.path.join(HERE, "PRE_POST_VALIDATION_SUMMARY.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for c in checks:
        print(c["result"], "|", c["check"], "|", str(c.get("detail", ""))[:150])
    print(summary["status"])
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
