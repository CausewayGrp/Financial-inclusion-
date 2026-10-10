# -*- coding: utf-8 -*-
"""Tranche C bilingual invariance: for every localized page pair, the numbers printed in <main> are the same in English
and Arabic (as multisets; Arabic-Indic digits and thousands separators normalised; ISO dates and years written out in
words are compared by value).

  python3 audit/tranche_c/checks/bilingual_invariance.py [out.json]
  YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/bilingual_invariance.py   (another built site)

Exit status 1 when any page pair differs (BIL-05 closed by the F2 Reading integration, 26 Sep 2026: the target is zero).
"""
import glob, html, json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SITE = os.path.join(ROOT, os.environ.get("YFIE_SITE_DIR") or "dist")   # F9: the reference implementation is tested unchanged
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
    # RC-18: a tag boundary is not a word boundary of its own. Inline formatting (a figure set in bold inside its
    # sentence, "<b>7.117</b> مليار") left two spaces where the text has one, so the bare «مليار دولار» rule below (one
    # billion when no figure precedes) fired on "7.117  مليار". One space, as the text reads; the rule is unchanged.
    t = re.sub(r"\s+", " ", t)
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


# LA-A (owner instruction 2a, 10 October 2026): the digit check above does not see numbers written as words, so an
# Arabic page could say "six" where the English says "three" (CLM-026 did) and pass. The words for 3 to 99 are compared
# too, as a set per page pair: a value written in words in one language must be written in words in the other. "Two"
# and "one" are left out (Arabic expresses them by the dual and the singular, not by a number word).
EN_UNITS = {"three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
EN_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
AR_PFX = r"(?:و|ف)?(?:ب|ل|ك)?(?:ال)?"
AR_UNITS = [(r"ثلاث(?:ة)?", 3), (r"أربع(?:ة)?", 4), (r"خمس(?:ة)?", 5), (r"ست(?:ة)?", 6), (r"سبع(?:ة)?", 7), (r"ثمان(?:ية|ي)?", 8), (r"تسع(?:ة)?", 9)]
AR_TENS = [(r"عشر(?:ون|ين)", 20), (r"ثلاث(?:ون|ين)", 30), (r"أربع(?:ون|ين)", 40), (r"خمس(?:ون|ين)", 50), (r"ست(?:ون|ين)", 60),
           (r"سبع(?:ون|ين)", 70), (r"ثمان(?:ون|ين)", 80), (r"تسع(?:ون|ين)", 90)]
# A number word that only one language writes, where the other states the same fact without a count (reviewed by hand).
WORD_ALLOWANCES = {
    "rights/index.html": {"ar": {3}},                       # «ثلاثة أذونات منفصلة»: the heading counts the three permissions it lists
    "evidence/VIS-FL-EVIDENCE-LADDER/index.html": {"en": {3}},   # "Three kinds of evidence": the Arabic lists the three kinds
}


def _text(path):
    raw = open(path, encoding="utf-8").read()
    m = re.search(r"<main.*?</main>", raw, re.S)
    t = re.sub(r"<script.*?</script>", "", m.group(0) if m else raw, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def en_words(t):
    out = set()
    for m in re.finditer(r"(?<![\w-])(" + "|".join(EN_TENS) + r")(?:-(one|two|" + "|".join(k for k in EN_UNITS if EN_UNITS[k] < 10) + r"))?(?![a-z])", t, re.I):
        u = (m.group(2) or "").lower()
        out.add(EN_TENS[m.group(1).lower()] + ({"one": 1, "two": 2}.get(u) or EN_UNITS.get(u, 0)))
    t = re.sub(r"(?<![\w-])(" + "|".join(EN_TENS) + r")(?:-[a-z]+)?", " ", t, flags=re.I)
    for w, v in EN_UNITS.items():
        if re.search(r"(?<![\w-])" + w + r"(?![a-z])", t, re.I):      # "five-provider" counts; "fivefold" does not
            out.add(v)
    return out


def _arval(tok, table):
    for p, v in table:
        if re.fullmatch(AR_PFX + p, tok):
            return v
    return None


def ar_words(t):
    t = t.replace("ـ", "")                              # tatweel: «لـسـتة» is «لستة»
    out, i = set(), 0
    t = re.sub(r"الاثني عشر", " ", t)                       # the definite form is converted to 12 by AR_WORDS and checked as a digit
    for pat, v in ((r"(?:و|ف)?(?:اثنا|اثني|اثنتا|اثنتي) ?عشر(?:ة)?", 12), (r"(?:و|ف)?(?:ال)?(?:أحد|إحدى|الحادي|الحادية) ?عشر(?:ة)?", 11)):
        if re.search(pat, t):
            out.add(v)
            t = re.sub(pat, " ", t)
    toks = re.findall(r"[؀-ۿ]+", t)
    while i < len(toks):
        tk = toks[i]
        tens, unit = _arval(tk, AR_TENS), _arval(tk, AR_UNITS)
        if tens:
            out.add(tens)
        elif unit:
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            if re.fullmatch(r"عشر(?:ة)?", nxt):
                out.add(unit + 10); i += 1
            elif nxt.startswith("و") and _arval(nxt[1:], AR_TENS):
                out.add(unit + _arval(nxt[1:], AR_TENS)); i += 1
            else:
                out.add(unit)
        elif re.fullmatch(AR_PFX + r"عشر(?:ة)?", tk):
            out.add(10)
        i += 1
    return out


def word_rows(pages):
    rows = []
    for en in pages:
        ar = en.replace(os.sep + "en" + os.sep, os.sep + "ar" + os.sep, 1)
        if not os.path.exists(ar):
            continue
        rel = os.path.relpath(en, os.path.join(SITE, "en")).replace(os.sep, "/")
        allow = WORD_ALLOWANCES.get(rel, {})
        we, wa = en_words(_text(en)), ar_words(_text(ar))
        only_en, only_ar = (we - wa) - allow.get("en", set()), (wa - we) - allow.get("ar", set())
        if only_en or only_ar:
            rows.append({"page": rel, "words_only_en": sorted(only_en), "words_only_ar": sorted(only_ar)})
    return rows


def main():
    rows = []
    pages = sorted(glob.glob(os.path.join(SITE, "en", "**", "index.html"), recursive=True))
    if not pages:                                   # an empty or wrong site directory is a failure, never a pass
        print(f"BILINGUAL NUMERIC INVARIANCE: no English pages under {SITE}")
        return 1
    for en in pages:
        ar = en.replace(os.sep + "en" + os.sep, os.sep + "ar" + os.sep, 1)
        if not os.path.exists(ar):
            rows.append({"page": en, "issue": "no Arabic page"}); continue
        a, b = nums(en), nums(ar)
        only_en, only_ar = a - b, b - a
        if only_en or only_ar:
            rows.append({"page": os.path.relpath(en, ROOT), "only_en": dict(only_en), "only_ar": dict(only_ar)})
    wrows = word_rows(pages)
    out = {"pairs_with_differences": len(rows), "rows": rows, "pairs_with_differing_number_words": len(wrows), "word_rows": wrows}
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
    print(f"BILINGUAL NUMERIC INVARIANCE: {len(rows)} page pairs with differing numbers ({len(pages)} pairs checked)")
    for r in rows[:40]:
        print(" ", r)
    print(f"BILINGUAL NUMBER WORDS: {len(wrows)} page pairs with differing spelled-out numbers ({len(pages)} pairs checked)")
    for r in wrows[:40]:
        print(f"  NUMBER WORDS {r['page']}: only in English {r['words_only_en']}, only in Arabic {r['words_only_ar']}")
    return len(rows) + len(wrows)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
