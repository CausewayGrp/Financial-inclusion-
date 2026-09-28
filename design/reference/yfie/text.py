# -*- coding: utf-8 -*-
"""One text layer for every renderer (D6): escaping and left-to-right isolation under the Design Intent Lock (§4.1.8).
After Arabic letters a plain ISO date renders with its parts reversed and a plain numeric range with its ends
swapped; an isolated run never does. Nothing here authors a word."""
from __future__ import annotations

import html
import re

ISO_DATE = re.compile(r"(?<![\d-])\d{4}-\d{2}(?:-\d{2})?(?![\d-])")   # YYYY-MM or YYYY-MM-DD, never the tail of an identifier
NUM_RANGE = re.compile(r"(?<![\d.,])(?:\d{4}(?:-\d{2}(?:-\d{2})?)?[–-]\d{4}(?:-\d{2}(?:-\d{2})?)?|\d{1,3}–\d{1,3})(?![\d.,])")   # 2021–2024, 2025-03–2026-01, 15–24
LTR_RUN = re.compile(f"(?:{NUM_RANGE.pattern})|(?:{ISO_DATE.pattern})")


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


_TOKEN = re.compile(r"<!--.*?-->|<[^>]*>|[^<]+", re.S)
_NAME = re.compile(r"</?([a-zA-Z][\w:-]*)")
_RAW = {"script", "style"}                                   # raw text: copied whole, never tokenised
_SKIP = {"svg", "math", "title", "textarea", "option", "pre", "code"}   # text that markup must not enter
_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def isolate_document(html_text: str) -> str:
    """The one isolation pass over a finished document: every ISO date and numeric range in its text isolated
    left-to-right, wherever a renderer left it plain. Untouched: script and style (raw), SVG, the title and form
    controls, and text already inside a `dir="ltr"` element other than the root (an identifier's isolate, a
    canonical link) — an isolate is never nested in an isolate."""
    out, stack, skip, ltr, pos = [], [], 0, 0, 0
    text = html_text
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
        out.append(tok if (skip or ltr) else LTR_RUN.sub(lambda mm: f'<bdi dir="ltr" class="nw">{mm.group(0)}</bdi>', tok))
    return "".join(out)
