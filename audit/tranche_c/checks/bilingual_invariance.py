# -*- coding: utf-8 -*-
"""Tranche C bilingual invariance: for every localized page pair, the numbers printed in <main> are the same in English
and Arabic (as multisets; Arabic-Indic digits and thousands separators normalised; ISO dates and years written out in
words are compared by value).

  python3 audit/tranche_c/checks/bilingual_invariance.py [out.json]

Exit status 1 when any page pair differs (BIL-05 closed by the F2 Reading integration, 26 Sep 2026: the target is zero).
"""
import glob, html, json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
AR = str.maketrans("٠١٢٣٤٥٦٧٨٩٫٬", "0123456789.,")
# Arabic editorial number words that carry a figure (dual and singular forms, ordinals in titles): normalised, not flagged.
AR_WORDS = [(r"ملياري دولار", " 2 مليار دولار"), (r"(?<![\d.])\s(ب?)(ال)?مليار دولار", r" \g<1>1 مليار دولار"),
            (r"الاثني عشر", " 12 "), (r"(العدد|الفصل) الأول", r"\1 1"), (r"(العدد|الفصل) الثاني", r"\1 2")]
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december",
                                      "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"])}


def nums(path):
    raw = open(path, encoding="utf-8").read()
    m = re.search(r"<main.*?</main>", raw, re.S)
    t = re.sub(r"<script.*?</script>", "", m.group(0) if m else raw, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t)).translate(AR)
    t = re.sub(r"\b(\d{4})-(\d{2})-(\d{2})\b", lambda x: f"{int(x.group(3))} {x.group(1)}", t)   # ISO dates → day and year (month names are words in both editions)
    t = re.sub(r"\b(\d{2})(\d{2})[–-](\d{2})\b(?!\d|[,.]\d)", r"\1\2–\1\3", t)   # 2022–23 → 2022–2023 (same years, short form)
    t = re.sub(r"\b[QH][1-4]\b", " ", t)                     # quarter/half labels (Q3, H1) are written in words in Arabic
    t = re.sub(r"\bFY(\d{4})", r"\1", t)                      # FY2026 → 2026
    t = re.sub(r"\b[A-Z]+\d+[A-Z]+[a-z]*\b", " ", t)           # identifiers such as G2P, G2Px
    t = re.sub(r"(\d+(?:\.\d+)?) ألف", lambda m: str(int(round(float(m.group(1)) * 1000))), t)   # Arabic '55 ألف' = 55,000
    for pat, val in AR_WORDS:
        t = re.sub(pat, val, t)
    out = Counter()
    for x in re.findall(r"\d[\d,]*(?:\.\d+)?", t):
        v = x.replace(",", "").rstrip(".")
        if v:
            out[v] += 1
    return out


def main():
    rows = []
    for en in sorted(glob.glob(os.path.join(ROOT, "dist/en/**/index.html"), recursive=True)):
        ar = en.replace(os.sep + "en" + os.sep, os.sep + "ar" + os.sep, 1)
        if not os.path.exists(ar):
            rows.append({"page": en, "issue": "no Arabic page"}); continue
        a, b = nums(en), nums(ar)
        only_en, only_ar = a - b, b - a
        if only_en or only_ar:
            rows.append({"page": os.path.relpath(en, ROOT), "only_en": dict(only_en), "only_ar": dict(only_ar)})
    out = {"pairs_with_differences": len(rows), "rows": rows}
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
    print(f"BILINGUAL NUMERIC INVARIANCE: {len(rows)} page pairs with differing numbers")
    for r in rows[:40]:
        print(" ", r)
    return len(rows)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
