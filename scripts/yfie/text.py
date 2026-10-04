# -*- coding: utf-8 -*-
"""One text layer for every renderer (D6): escaping and left-to-right isolation under the Design Intent Lock (§4.1.8).
After Arabic letters a plain ISO date renders with its parts reversed, a plain numeric range with its ends
swapped, and a plain signed value with its sign and percent sign thrown to the wrong end ("+11%" as "%11+",
DEBT-018); an isolated run never does. Nothing here authors a word."""
from __future__ import annotations

import html
import re

ISO_DATE = re.compile(r"(?<![A-Za-z0-9_-])\d{4}-\d{2}(?:-\d{2})?(?![\d-])")   # YYYY-MM or YYYY-MM-DD, never part of an identifier
# 2021–2024, 2025-03–2026-01, 80,000–90,000, 15–24 — also at the end of a sentence ("… 2026–2030."), never inside an
# identifier ("SRC-…-2026-2030-001") or a decimal
NUM_RANGE = re.compile(r"(?<![A-Za-z0-9_.,-])(?:\d{4}(?:-\d{2}(?:-\d{2})?)?[–-]\d{4}(?:-\d{2}(?:-\d{2})?)?|\d{1,3}(?:,\d{3})+–\d{1,3}(?:,\d{3})+|\d{1,3}–\d{1,3})(?!\d|[.,]\d)")
SIGNED = re.compile(r"(?<![\w\u0600-\u06FF-])[+\u2212\u2013-]\d[\d,]*(?:\.\d+)?%?(?![\w])")   # +11%, +4.9%, −0.5 — the sign and the percent sign are bidi-neutral, so after Arabic letters an un-isolated run renders "%11+"
# a table or figure number as its source prints it ("Table 4-1"): after Arabic letters its parts would display reversed
# (edition 2, E2-7)
TABLE_NO = re.compile(r"(?<![\w.,\u2013-])\d{1,2}-\d{1,2}(?![\w.,\u2013-])")
LTR_RUN = re.compile(f"(?:{NUM_RANGE.pattern})|(?:{ISO_DATE.pattern})|(?:{SIGNED.pattern})|(?:{TABLE_NO.pattern})")
# A record, source or object identifier with a digit (CLM-001, FMIIP-BASELINE-2025-01, SRC-CBY-AR2022-001): left to right
# and isolated wherever governed text reaches an Arabic page, but never "nw" — it breaks at its own hyphens.
ID_RUN = re.compile(r"(?<![A-Za-z0-9_-])(?=[A-Z][A-Za-z0-9-]*\d)[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)+(?![A-Za-z0-9_-])")
LRI, PDI = "\u2066", "\u2069"   # Unicode isolates, where markup cannot go (the document title, meta content)


def esc(x) -> str:
    """HTML-escape a governed value (None becomes empty; a numeric 0 stays "0")."""
    return html.escape("" if x is None else str(x), quote=True)


def bdi(x) -> str:
    """A governed token isolated left-to-right (HTML text only). A whole ISO date or numeric range never breaks; an
    identifier breaks only at its own hyphens, so a 37-character source id still fits a 288 px column."""
    s = esc(x)
    return f'<bdi dir="ltr" class="nw">{s}</bdi>' if LTR_RUN.fullmatch(s) else f'<bdi dir="ltr">{s}</bdi>'


def isolate_iso(escaped: str) -> str:
    """Every ISO date and numeric range inside already-escaped text isolated as an unbroken left-to-right run."""
    return LTR_RUN.sub(lambda m: f'<bdi dir="ltr" class="nw">{m.group(0)}</bdi>', escaped)


def iso(x) -> str:
    """Governed text escaped, with its ISO dates and numeric ranges isolated."""
    return isolate_iso(esc(x))


def isolate_ids(html_text: str) -> str:
    """Every identifier in the text of an HTML fragment (never inside a tag) isolated left-to-right, breakable."""
    parts = re.split(r"(<[^>]+>)", html_text)
    return "".join(p if p.startswith("<") else ID_RUN.sub(lambda m: f'<bdi dir="ltr">{m.group(0)}</bdi>', p) for p in parts)


def isolate_plain(text: str) -> str:
    """Text that cannot carry markup (a document title, meta content): each identifier, ISO date and numeric range
    between the Unicode isolates LRI and PDI, so an Arabic title or social card reads them as the English does."""
    return re.sub(f"(?:{ID_RUN.pattern})|(?:{LTR_RUN.pattern})", lambda m: f"{LRI}{m.group(0)}{PDI}", text)


_HEAD_TITLE = re.compile(r"(<title>)(.*?)(</title>)", re.S)
_HEAD_META = re.compile(r'(<meta (?:name|property)="(?:description|og:title|og:description|og:image:alt|twitter:title|twitter:description|twitter:image:alt)" content=")([^"]*)(")')


def isolate_head(html_text: str) -> str:
    """An Arabic document's title and its displayed meta content (description, social title, description and image
    text) isolated with Unicode isolates; the machine fields (yfie-citation, ids, URLs) are left as they are."""
    head_end = html_text.find("</head>")
    if head_end < 0:
        return html_text
    head = _HEAD_TITLE.sub(lambda m: m.group(1) + isolate_plain(m.group(2)) + m.group(3), html_text[:head_end])
    head = _HEAD_META.sub(lambda m: m.group(1) + isolate_plain(m.group(2)) + m.group(3), head)
    return head + html_text[head_end:]


_TOKEN = re.compile(r"<!--.*?-->|<[^>]*>|[^<]+", re.S)
_NAME = re.compile(r"</?([a-zA-Z][\w:-]*)")
_RAW = {"script", "style"}                                   # raw text: copied whole, never tokenised
_SKIP = {"svg", "math", "title", "textarea", "option", "pre", "code"}   # text that markup must not enter
_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def _isolate_text(tok: str, rtl: bool) -> str:
    """One text run of a document: ISO dates and numeric ranges isolated unbroken; in a right-to-left document an
    identifier (FMIIP-BASELINE-2025-01, CLM-010) isolated too, breakable, and its digits never read as a date or range
    (edition 2, E2-4b: governed prose that names a record by its ID)."""
    dates = lambda s: LTR_RUN.sub(lambda mm: f'<bdi dir="ltr" class="nw">{mm.group(0)}</bdi>', s)   # noqa: E731
    if not rtl:
        return dates(tok)
    out, last = [], 0
    for m in ID_RUN.finditer(tok):
        out.append(dates(tok[last:m.start()]))
        out.append(f'<bdi dir="ltr">{m.group(0)}</bdi>')
        last = m.end()
    out.append(dates(tok[last:]))
    return "".join(out)


def isolate_document(html_text: str) -> str:
    """The one isolation pass over a finished document: every ISO date and numeric range in its text isolated
    left-to-right, wherever a renderer left it plain. Untouched: script and style (raw), SVG, the title and form
    controls, and text already inside a `dir="ltr"` element other than the root (an identifier's isolate, a
    canonical link) — an isolate is never nested in an isolate. In a right-to-left document the title and the displayed
    meta content, which cannot carry markup, take Unicode isolates instead (`isolate_head`)."""
    out, stack, skip, ltr, pos = [], [], 0, 0, 0
    text = html_text
    rtl = bool(re.match(r'\s*<!doctype html>\s*<html[^>]*\sdir="rtl"', text, re.I))
    while pos < len(text):
        m = _TOKEN.match(text, pos)
        if not m:
            out.append(text[pos:]); break
        tok = m.group(0); pos = m.end()
        if tok.startswith("<!") or tok.startswith("<?"):
            out.append(tok); continue
        if tok.startswith("</"):
            nm = _NAME.match(tok); name = nm.group(1).lower() if nm else ""
            while stack:
                n, sk, lt = stack.pop(); skip -= sk; ltr -= lt
                if n == name:
                    break
            out.append(tok); continue
        if tok.startswith("<"):
            nm = _NAME.match(tok); name = nm.group(1).lower() if nm else ""
            out.append(tok)
            if name in _RAW:   # copy the raw content and its end tag whole
                end = text.find(f"</{name}", pos)
                end = len(text) if end < 0 else end
                close = text.find(">", end)
                close = len(text) if close < 0 else close + 1
                out.append(text[pos:close]); pos = close
                continue
            if name and not tok.endswith("/>") and name not in _VOID:
                sk = 1 if name in _SKIP else 0
                lt = 1 if (name not in ("html", "body") and re.search(r'\sdir="ltr"', tok)) else 0
                stack.append((name, sk, lt)); skip += sk; ltr += lt
            continue
        out.append(tok if (skip or ltr) else _isolate_text(tok, rtl))
    done = "".join(out)
    return isolate_head(done) if re.match(r'\s*<!doctype html>\s*<html[^>]*\sdir="rtl"', done, re.I) else done
