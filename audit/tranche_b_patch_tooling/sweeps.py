# -*- coding: utf-8 -*-
"""Terminology sweeps PB-0413 / PB-0414 / PB-0415, resolved per occurrence.

Sweeps run LAST (execution step after every other P1–P4 patch), on the post-patch cell text, so
every row's current_value is the exact text the executor will meet. Each occurrence is classified
REPLACE (exact before → after snippet, restricted to one cell) or KEEP (sense is not the product
self-referent / not the governed-claim noun), with the classification rule stated."""
import re, copy

def rid(sheet, rec):
    keys = [k for k in rec if k != "_row"]
    if sheet == "03_PAGE_SECTIONS":
        return f"{rec.get('route')}#s{rec.get('section_order')}"
    if sheet == "09_READING_SECTIONS":
        return f"{rec.get('reading_id')}#{rec.get('section_id')}"
    return str(rec.get(keys[0])) if keys else "?"



# ---------------- PB-0413: Arabic noun for a governed claim ----------------
AR_CLAIM_REPLACE = [  # exact substring → replacement (feminine agreement handled inside the snippet)
    ("قد يتحول الرقم إلى ادعاء مختلف", "قد يكتسب الرقم معنى مختلفًا"),
    ("ادعاءات عامة مسندة بالأدلة", "خلاصات عامة مسندة بالأدلة"),
    ("للوصول إلى ادعاء أو مؤشر", "للوصول إلى خلاصة أو مؤشر"),
    ("افتح الادعاءات وسجلات الأدلة", "افتح الخلاصات وسجلات الأدلة"),
    ("الدليل وراء الادعاء،", "الدليل وراء الخلاصة،"),
    ("في هذا الادعاء", "في هذه الخلاصة"),
    ("يضيق نطاق الادعاء", "يضيق نطاق الخلاصة"),
]
AR_CLAIM_KEEP = [  # sense = 'to assert / an assertion' (not the product's governed claim)
    ("ليس ادعاءً", "assertion sense: 'not a claim that conformance is achieved'"),
    ("من دون ادعاء", "assertion sense: 'without asserting'"),
    ("من دون الادعاء", "assertion sense: 'without asserting'"),
    ("لا يجوز الادعاء", "assertion sense: 'it may not be asserted that'"),
    ("ولا ادعاء", "assertion sense: 'nor an assertion of'"),
    ("يحتاج ادعاء الشمول", "assertion sense: 'an assertion of inclusion needs separate evidence'"),
    ("الادعاءات الرقمية", "assertion sense: numeric assertions made by qualitative sources"),
    ("إلى ادعاء سببي", "assertion sense: 'into a causal assertion'"),
]

# ---------------- PB-0414: «المنظومة» as the product's self-referent ----------------
# Lead decision: self-referent → «المنصة» (feminine, so every verb and pronoun agreement is preserved);
# «منظومة/المنظومة» meaning the financial(-inclusion) system is kept.
AR_SYS_KEEP = [
    (r"(?<!ال)(?<!لل)منظومة", "indefinite / construct «منظومة …» = the financial(-inclusion) system"),
    (r"المنظومة الأوسع", "the wider financial system"),
    (r"سياق المنظومة", "section label 'System context' (financial system)"),
    (r"علاقات المنظومة", "label 'System relationships' (financial system)"),
    (r"ما المنظومة التي", "'the system the evidence is trying to describe'"),
    (r"هذه المنظومة، لكنه|جزء من هذه المنظومة", "part of the financial system"),
    (r"SYSTEM / المنظومة", "bilingual label pair"),
    (r"والحوالات في المنظومة", "position of exchange/remittance firms in the financial system"),
    (r"مجالات المنظومة", "domains of the financial system (true under either reading)"),
    (r"مترابطة للمنظومة", "connected picture of the financial system"),
    (r"الزمني للمنظومة", "chronology of the financial system"),
]
# EN
EN_SYS_KEEP = [
    (r"The system the evidence is trying to describe", "the financial system"),
    (r"the system link", "the system-context link (financial system)"),
    (r"freezing the system at", "the financial system"),
    (r"matter to the system", "the financial system"),
    (r"Do not call the system effective", "a payment system"),
    (r"launched the product", "a financial product"),
    (r"parts of the system are current", "parts of the financial system"),
]
EN_SELF_MAP = [  # ordered; first match wins at each occurrence
    (r"Why measurement sits inside the system", "Why measurement is part of this resource"),
    (r"The system's evidence is", "The evidence here is"),
    (r"The system's people-side evidence", "The people-side evidence here"),
    (r"available in the system", "available here"),
    (r"in the system", "here"),
    (r"The system", "This resource"), (r"The product", "This resource"),
    (r"the system", "this resource"), (r"the product", "this resource"),
]
AR_SELF_HEADING = [(r"لماذا القياس جزء من المنظومة؟", "لماذا القياس جزء من المنصة؟")]


def _occurrences(text, pat):
    return [m for m in re.finditer(pat, text)]


def _keep_reason(text, start, end, keeps):
    for pat, why in keeps:
        for m in re.finditer(pat, text):
            if m.start() <= start and end <= m.end() or (m.start() <= start < m.end()):
                return why
    return None


def _unique_window(text, s, e, w=18):
    while True:
        a, b = max(0, s - w), min(len(text), e + w)
        snip = text[a:b]
        if text.count(snip) == 1 or (a == 0 and b == len(text)):
            return a, b
        w += 10


def sweep(sheets, rid):
    """sheets = post-patch Master text (dict sheet -> list of records). Returns (rows, keeps, apply_fn)."""
    rows, keeps, ops = [], [], []
    SKIP = {"36_SUPPLEMENT_ARCHIVE", "30_FCS_CONTEXT", "29_OECD_BENCHMARKS", "25_FINDEX_BASELINE", "16_DATASET_CATALOG", "28_METHODS_RIGHTS"}
    for sh, recs in sorted(sheets.items()):  # deterministic sheet order
        if sh in SKIP: continue
        recs = sorted(recs, key=lambda r: int(r["_row"]))
        for r in recs:
            for k, v in r.items():
                if k == "_row" or not isinstance(v, str): continue
                edits = []  # (start, end, new, pid, rule)
                # PB-0413
                for m in _occurrences(v, r"ادعا"):
                    rep = None
                    for old, new in AR_CLAIM_REPLACE:
                        for mm in re.finditer(re.escape(old), v):
                            if mm.start() <= m.start() < mm.end(): rep = (mm.start(), mm.end(), new)
                    if rep:
                        edits.append((*rep, "PB-0413", "governed-claim noun → «خلاصة/الخلاصات»"))
                    else:
                        why = _keep_reason(v, m.start(), m.end(), [(re.escape(a), b) for a, b in AR_CLAIM_KEEP])
                        keeps.append(("PB-0413", sh, r["_row"], k, v[max(0, m.start()-35):m.end()+35], why or "UNCLASSIFIED"))
                # PB-0414
                for m in _occurrences(v, r"منظومة"):
                    s0 = m.start()
                    why = _keep_reason(v, s0, m.end(), AR_SYS_KEEP)
                    head = None
                    for pat, new in AR_SELF_HEADING:
                        for mm in re.finditer(re.escape(pat), v):
                            if mm.start() <= m.start() < mm.end(): head = (mm.start(), mm.end(), new)
                    if head:
                        edits.append((*head, "PB-0414", "self-referent heading → «المنصة»")); continue
                    if why:
                        keeps.append(("PB-0414", sh, r["_row"], k, v[max(0, m.start()-35):m.end()+30], why)); continue
                    # self-referent: «المنظومة» / «للمنظومة» → «المنصة» / «للمنصة»
                    if v[m.start()-2:m.start()] in ("ال", "لل"):
                        edits.append((m.start(), m.end(), "منصة", "PB-0414", "product self-referent «المنظومة» → «المنصة» (feminine: agreement unchanged)"))
                    else:
                        keeps.append(("PB-0414", sh, r["_row"], k, v[max(0, m.start()-35):m.end()+30], "UNCLASSIFIED"))
                # PB-0415
                for m in _occurrences(v, r"\b[Tt]he (system|product)\b(?:'s)?"):
                    why = _keep_reason(v, m.start(), m.end(), EN_SYS_KEEP)
                    if why:
                        keeps.append(("PB-0415", sh, r["_row"], k, v[max(0, m.start()-40):m.end()+30], why)); continue
                    done = False
                    for pat, new in EN_SELF_MAP:
                        for mm in re.finditer(re.escape(pat) if not pat.startswith("(") else pat, v):
                            if mm.start() <= m.start() < mm.end():
                                edits.append((mm.start(), mm.end(), new, "PB-0415", f"repository self-referent '{pat}' → '{new}'")); done = True; break
                        if done: break
                    if not done:
                        keeps.append(("PB-0415", sh, r["_row"], k, v[max(0, m.start()-40):m.end()+30], "UNCLASSIFIED"))
                if not edits: continue
                # de-duplicate overlapping edits (same span found twice)
                edits = sorted(set(edits), key=lambda e: (e[0], -e[1]))
                clean = []
                for e in edits:
                    if clean and e[0] < clean[-1][1]: continue
                    clean.append(e)
                # merge edits whose unique windows overlap into one before/after pair per window
                wins = []
                for s_, e_, new, pid, rule in clean:
                    a, b = _unique_window(v, s_, e_)
                    if wins and a <= wins[-1]["b"]:
                        w = wins[-1]; w["b"] = max(w["b"], b); w["edits"].append((s_, e_, new, pid, rule))
                    else:
                        wins.append({"a": a, "b": b, "edits": [(s_, e_, new, pid, rule)]})
                for w in wins:
                    a, b = w["a"], w["b"]
                    while v.count(v[a:b]) != 1 and (a > 0 or b < len(v)): a, b = max(0, a-10), min(len(v), b+10)
                    before = v[a:b]; after = ""; cur = a
                    for s_, e_, new, pid, rule in w["edits"]:
                        after += v[cur:s_] + new; cur = e_
                    after += v[cur:b]
                    pids = sorted({x[3] for x in w["edits"]}); rules = "; ".join(sorted({x[4] for x in w["edits"]}))
                    rows.append(dict(pid="+".join(pids), sheet=sh, obj=rid(sh, r), row=r["_row"], field=k, old=before, new=after,
                                     rule=rules, n=len(w["edits"])))
                    ops.append((sh, r["_row"], k, before, after))
    return rows, keeps, ops


def apply_ops(sheets, ops):
    idx = {(sh, r["_row"]): r for sh, recs in sheets.items() for r in recs}
    missing = []
    for sh, row, k, before, after in ops:
        r = idx[(sh, row)]
        if r[k].count(before) != 1: missing.append((sh, row, k, before)); continue
        r[k] = r[k].replace(before, after)
    return missing
