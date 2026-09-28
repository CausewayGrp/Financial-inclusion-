# -*- coding: utf-8 -*-
"""One text layer for every renderer (D6): escaping, left-to-right isolation and the ISO-date rule of the Design
Intent Lock (§4.1.8) — after Arabic letters a plain ISO date renders with its parts reversed, an isolated one never
does. Nothing here authors a word."""
from __future__ import annotations

import html
import re

ISO_DATE = re.compile(r"\d{4}-\d{2}(?:-\d{2})?")


def esc(x) -> str:
    """HTML-escape a governed value (None becomes empty; a numeric 0 stays "0")."""
    return html.escape("" if x is None else str(x), quote=True)


def bdi(x) -> str:
    """An identifier, date or numeric run isolated as an unbroken left-to-right run (HTML text only)."""
    return f'<bdi dir="ltr" class="nw">{esc(x)}</bdi>'


def isolate_iso(escaped: str) -> str:
    """Every ISO date (YYYY-MM or YYYY-MM-DD) inside already-escaped text isolated as an unbroken left-to-right run."""
    return ISO_DATE.sub(lambda m: f'<bdi dir="ltr" class="nw">{m.group(0)}</bdi>', escaped)


def iso(x) -> str:
    """Governed text escaped, with its ISO dates isolated."""
    return isolate_iso(esc(x))
