#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Four-digit unit check (audit/release_candidate/INSTRUCTIONS.md, Part A, G2 item 17).

  python3 audit/release_candidate/four_digit_unit_check.py [dist_dir] [--write audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md]

One sweep over every public figure of four or more digits in the built site (both editions), for the failure of item 4:

  A. a displayed series that mixes a decimal point and a thousands separator — within one drawn series (the governed
     visual contracts' series values, as the renderer prints them) and within one prose sentence or table (two or more
     numbers of which one carries only a decimal point and another only a thousands comma);
  B. a figure with no unit beside it — a number of four or more digits in `<main>` text whose sentence or cell carries
     no unit, currency, percentage, percentage-point, count noun or quantity label.

Years, ISO dates and months, identifiers (CLM-001, YSC-012, ISBN-like runs, OBS-00051), ordinals and page numbers are
not figures and are excluded. The report lists every candidate with its page, the text around it and the disposition
(TRUE INSTANCE → fixed in RC-1; or NOT AN INSTANCE with the reason), so the check can be re-run after the transaction.
"""
from __future__ import annotations

import html as _html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"

NUM = re.compile(r"(?<![\w.,/-])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+\.\d+|\d{4,})(?![\w.,]*[A-Za-z])%?")
YEARISH = re.compile(r"^(?:19|20)\d{2}$")
ISO = re.compile(r"\b\d{4}-\d{2}(?:-\d{2})?\b")
IDENT = re.compile(r"\b(?:[A-Z]{2,}[A-Z0-9-]*-\d[\w-]*|OBS-\d+|No\.\s*\d+|ref\.\s*\d+|\d+/[A-Z]+/\d{4})\b")
UNIT_WORDS = [
    # English
    "%", "percent", "percentage point", "points", "US$", "USD", "YER", "SAR", "rial", "dollar", "million", "billion", "bn", "m)",
    "terminals", "transactions", "accounts", "wallets", "respondents", "borrowers", "savers", "depositors", "firms", "banks",
    "companies", "establishments", "agents", "participants", "records", "sources", "events", "rows", "locators", "documents",
    "pages", "beneficiaries", "households", "people", "adults", "members", "institutions", "branches", "subscribers", "units",
    "networks", "users", "number", "count", "value", "quotes", "ratio", "index", "score", "times",
    # Arabic
    "ريال", "دولار", "مليون", "مليار", "نقطة", "نقاط", "جهاز", "أجهزة", "معاملة", "معاملات", "حساب", "حسابات", "محفظة", "محافظ",
    "مستجيب", "مقترض", "مدخر", "مودع", "منشأة", "منشآت", "بنك", "بنوك", "شركة", "شركات", "وكيل", "وكلاء", "مشارك", "سجل", "سجلات",
    "مصدر", "مصادر", "حدث", "أحداث", "صف", "صفوف", "مستفيد", "أسرة", "بالغ", "عضو", "فرع", "مشترك", "العدد", "عدد", "قيمة", "مؤشر",
    "درجة", "مرة", "مرات", "رقم قياسي", "من البالغين", "من المبلغ",
]

TAG = re.compile(r"<[^>]+>")
INLINE = re.compile(r"</?(?:bdi|a|b|i|em|strong|span|time|button|sup|sub)\b[^>]*>")
BLOCK_SPLIT = re.compile(r"</(?:p|li|td|th|h[1-6]|dd|dt|figcaption|caption|div)>|<br\s*/?>")
SENT = re.compile(r"(?<=[.؟?!;؛])\s+")


def main_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"<main[^>]*>(.*)</main>", raw, re.S)
    return m.group(1) if m else raw


def blocks(frag: str) -> list[str]:
    """Text blocks of the fragment: one per block-level element (a table cell is its own block)."""
    out = []
    for piece in BLOCK_SPLIT.split(frag):
        txt = re.sub(r"\s+", " ", _html.unescape(TAG.sub(" ", INLINE.sub("", piece)))).strip()
        if txt:
            out.append(txt)
    return out


def figures(text: str) -> list[str]:
    """Numbers of four or more digits in a text, excluding years, dates and identifiers."""
    t = ISO.sub(" ", text)
    t = IDENT.sub(" ", t)
    out = []
    for m in NUM.finditer(t):
        tok = m.group(0)
        digits = re.sub(r"\D", "", tok)
        if len(digits) < 4 or YEARISH.match(tok.rstrip("%")):
            continue
        # a year range or a list of years ("2021–2024", "2022, 2023") is not a figure
        if re.fullmatch(r"\d{4}", tok) and re.search(r"(?:19|20)\d{2}", tok):
            continue
        out.append(tok)
    return out


def has_unit(text: str) -> bool:
    low = text.lower()
    return any(u.lower() in low for u in UNIT_WORDS)


def notation(tok: str) -> str:
    t = tok.rstrip("%")
    if "," in t and "." in t:
        return "both"
    if "," in t:
        return "comma"
    if "." in t:
        return "point"
    return "plain"


def series_check() -> list[dict]:
    """A: every drawn series of the governed visual contracts, as the renderer prints it (plain_num)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from yfie.visuals import plain_num  # noqa: PLC0415
    vc = json.loads((ROOT / "site-src/content/visuals/visual_design_contracts.json").read_text(encoding="utf-8"))
    out = []
    for c in vc["visuals"]:
        k = c.get("contract") or {}
        for s in k.get("series") or []:
            shown = [plain_num(v["y"]) for v in s.get("values") or [] if isinstance(v.get("y"), (int, float))]
            kinds = {notation(x) for x in shown}
            big = [x for x in shown if len(re.sub(r"\D", "", x)) >= 4]
            if "point" in kinds and "comma" in kinds:
                out.append({"visual": c["visual_id"], "series": s["id"], "values": shown, "finding": "mixes a point-only value with a comma-only value"})
            elif big and ("point" in kinds and ("comma" in kinds or "both" in kinds)):
                out.append({"visual": c["visual_id"], "series": s["id"], "values": shown, "finding": "point-only value beside a comma-separated value"})
    return out


def prose_check(dist: Path) -> dict[str, list[dict]]:
    """A (prose/table) and B over every page."""
    found = defaultdict(list)
    for lang in ("en", "ar"):
        for page in sorted((dist / lang).rglob("index.html")):
            route = "/" + str(page.parent.relative_to(dist / lang)).replace("\\", "/").strip(".") + "/"
            route = route.replace("//", "/")
            for blk in blocks(main_html(page)):
                for sent in SENT.split(blk):
                    figs = figures(sent)
                    if not figs:
                        continue
                    kinds = {notation(f) for f in figs}
                    if "point" in kinds and ("comma" in kinds or "both" in kinds):
                        found["A"].append({"lang": lang, "route": route, "figures": figs, "text": sent[:240]})
                    if not has_unit(sent):
                        found["B"].append({"lang": lang, "route": route, "figures": figs, "text": sent[:240]})
    return found


def main(argv: list[str]) -> int:
    dist = Path(argv[0]) if argv and not argv[0].startswith("--") else DIST
    write = Path(argv[argv.index("--write") + 1]) if "--write" in argv else None
    ser = series_check()
    pro = prose_check(dist)
    # one line per distinct (lang, text) so the report stays readable
    seenA, seenB = set(), set()
    A = [x for x in pro["A"] if (x["lang"], x["text"]) not in seenA and not seenA.add((x["lang"], x["text"]))]
    B = [x for x in pro["B"] if (x["lang"], x["text"]) not in seenB and not seenB.add((x["lang"], x["text"]))]
    lines = ["# Four-digit unit check — item 17", "",
             f"Built site: `{dist.relative_to(ROOT) if dist.is_relative_to(ROOT) else dist}`; pages swept: {sum(1 for _ in dist.rglob('index.html'))}.", "",
             "## A. Drawn series mixing a decimal point with a thousands separator", ""]
    lines += [f"- **{x['visual']}** · series `{x['series']}` — {x['finding']}: {', '.join(x['values'])}" for x in ser] or ["- none"]
    lines += ["", "## A. Prose or table sentences mixing a point-only figure with a comma-separated figure", ""]
    lines += [f"- `{x['lang']}` {x['route']} — {', '.join(x['figures'])} — “{x['text']}”" for x in A] or ["- none"]
    lines += ["", "## B. Figures of four or more digits with no unit beside them (sentence or cell carries no unit, currency, percentage or count noun)", ""]
    lines += [f"- `{x['lang']}` {x['route']} — {', '.join(x['figures'])} — “{x['text']}”" for x in B] or ["- none"]
    text = "\n".join(lines) + "\n"
    print(text)
    print(f"SUMMARY series={len(ser)} proseA={len(A)} proseB={len(B)}")
    if write:
        write.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
