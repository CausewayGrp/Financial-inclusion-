# -*- coding: utf-8 -*-
"""R8.5 copy-out-of-code (AR-29 / EN-09 / TRUST-25): a one-time, mechanical move of the bilingual public copy held in
scripts/build.py into the Master's governed interface copy (04 block "Governed interface copy").

  python3 r85_copy_out_of_code.py extract   <interface_copy.json> <rows_out.json>     # dry run: list rows and edits
  python3 r85_copy_out_of_code.py apply     <interface_copy.json> <rows_out.json>     # rewrite build.py; write the rows

What moves, and how:
  * every inline pair  '<Arabic>' if ar else '<English>'  (plain string literals) becomes ui_text('<ID>',lang);
  * the two label dictionaries _domain_labels / _evidence_labels become tables of interface-copy IDs;
  * a pair that already exists in 04 (same English and Arabic) reuses that ID.
Pairs that need a parameter (f-strings) and structural glyphs (arrows) are left for the hand edits recorded in
audit/R8_5_SUBTRACTION_LEDGER.csv. The rendered site must be byte-identical before and after this step.
This file is lineage: it is run once by the R8.5 transaction and is not part of the build.
"""
import ast, json, re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD = os.path.join(ROOT, "scripts", "build.py")
AR = re.compile(r"[؀-ۿ]")
PREFIX = {
    "search_dialog": "SEARCH", "header": "HEADER", "footer": "FOOTER", "hero": "HERO", "breadcrumb": "CRUMB",
    "journey_next": "NEXT", "question_cards": "QUESTIONS", "home_ctas": "HOME", "measurement_cards": "MA",
    "sources_block": "SOURCES", "render_visual": "VIS", "_visual_fallback": "VIS", "governed_blocks": "BLOCK",
    "governed_block_groups": "BLOCK", "generic": "PAGE", "compare_block": "COMPARE", "source_directory": "DATA",
    "corrections_context_block": "CORR", "contact_context_block": "CONTACT", "record_context_origin": "ORIGIN",
    "public_ref": "REF", "domain_readings": "DOM", "domain_hero": "DOM", "_band_kind": "DOM", "_domain_section": "DOM",
    "domain_scope_band": "DOM", "domain_visual": "DOM", "domain_more": "DOM", "domain_verify": "DOM",
    "domain_measurement_next": "DOM", "source_trust_controls": "SRC", "evidence_citation_context": "CITE",
    "reading_verification_links": "READING", "page": "PAGE", "evidence_record_hero": "EVID", "evidence_scope_band": "EVID",
    "evidence_boundary": "EVID", "evidence_sources": "EVID", "evidence_trace": "EVID", "evidence_related": "EVID",
    "evidence_progressive": "EVID", "evidence_utility": "EVID", "measurement_more": "MA",
}
LIT = r"""(?:'(?:\\.|[^'\\\n])*'|"(?:\\.|[^"\\\n])*")"""
TERN = re.compile(r"(?<![A-Za-z_\]\)'\"])(" + LIT + r")\s+if\s+ar\s+else\s+(" + LIT + r")")


def slug(en, n=5):
    words = re.findall(r"[A-Za-z0-9]+", en)
    return "-".join(w.upper() for w in words[:n]) or "LABEL"


def enclosing(src, pos):
    name, params = "<module>", ""
    for m in re.finditer(r"^def (\w+)\(([^)]*)\)", src, re.M):
        if m.start() > pos:
            break
        name, params = m.group(1), m.group(2)
    return name, params


class Alloc:
    def __init__(self, existing):
        self.by_pair = {(u["label_en"], u["label_ar"]): u["ui_id"] for u in existing}
        self.ids = {u["ui_id"] for u in existing}
        self.rows = []

    def get(self, prefix, en, ar, rule):
        if (en, ar) in self.by_pair:
            return self.by_pair[(en, ar)]
        base = f"UI-{prefix}-{slug(en)}"
        uid, k = base, 2
        while uid in self.ids:
            uid, k = f"{base}-{k}", k + 1
        self.ids.add(uid)
        self.by_pair[(en, ar)] = uid
        self.rows.append([uid, en, ar, rule])
        return uid


def label_table(src, fname, prefix, alloc):
    """Turn def fname(lang): if lang=='ar': return {...} / return {...} into an ID table + a small function."""
    m = re.search(r"^def %s\(lang\):\n(.*?)(?=^\S)" % fname, src, re.M | re.S)
    tree = ast.parse(m.group(0))
    fn = tree.body[0]
    ar_dict = fn.body[0].body[0].value
    en_dict = fn.body[1].value
    def pairs(d):
        out = {}
        for k, v in zip(d.keys, d.values):
            out[k.value] = v.value if isinstance(v, ast.Constant) else ast.get_source_segment(m.group(0), v)
        return out
    a, e = pairs(ar_dict), pairs(en_dict)
    if list(a) != list(e):
        raise SystemExit(f"{fname}: key order differs")
    ids, code = [], []
    for k in e:
        if isinstance(e[k], str) and not e[k].startswith("_nav_label(") and AR.search(a[k] or ""):
            ids.append((k, alloc.get(prefix, e[k], a[k], f"build.py {fname}['{k}']")))
        else:
            code.append((k, e[k].replace("'en'", "lang")))
    table = "_%s_UI = {%s}\n" % (fname.strip("_").upper(), ", ".join(f"'{k}': '{i}'" for k, i in ids))
    body = ("def %s(lang):\n    # R8.5: labels are governed interface copy (04); only computed entries stay in code\n"
            "    out = {k: ui_text(v, lang) for k, v in _%s_UI.items()}\n" % (fname, fname.strip("_").upper()))
    for k, c in code:
        body += f"    out['{k}'] = {c}\n"
    order = list(e)
    body += "    return {k: out[k] for k in %r}\n\n" % (order,)
    return src.replace(m.group(0), table + body)


def main():
    mode, ui_path, rows_out = sys.argv[1:4]
    existing = json.load(open(ui_path, encoding="utf-8"))
    alloc = Alloc(existing)
    src = open(BUILD, encoding="utf-8").read()
    src = label_table(src, "_domain_labels", "DOM", alloc)
    src = label_table(src, "_evidence_labels", "EVID", alloc)
    edits, skipped = [], []
    def repl(m):
        a_lit, e_lit = m.group(1), m.group(2)
        a, e = ast.literal_eval(a_lit), ast.literal_eval(e_lit)
        if not AR.search(a):
            return m.group(0)
        name, params = enclosing(src, m.start())
        if not re.search(r"\blang\b", params):
            skipped.append((name, e))
            return m.group(0)
        uid = alloc.get(PREFIX.get(name, "UI"), e, a, f"build.py {name}()")
        edits.append((name, uid))
        return f"ui_text('{uid}',lang)"
    src = TERN.sub(repl, src)
    json.dump({"rows": alloc.rows, "edits": edits, "skipped": skipped}, open(rows_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"new rows {len(alloc.rows)}; inline edits {len(edits)}; skipped (no lang in scope) {len(skipped)}")
    if mode == "apply":
        open(BUILD, "w", encoding="utf-8").write(src)


if __name__ == "__main__":
    main()
