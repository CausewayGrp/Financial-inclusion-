# -*- coding: utf-8 -*-
"""Portable evidence (D6, brief §10, §16): the standalone frames a figure or a page can leave the site in.

- An **export frame** is a self-contained document that holds one drawn figure with its detached frame — title,
  question, period and universe, the governed panels and markers, the prohibited inference, the credit, the canonical
  link and the edition — plus the resource's identity line (the canonical logo, unaltered, at 32 px). The build writes
  one per drawn contract and language into `out/_export/` (an underscore path: not part of the hostable site). The
  export *control* on pages is designed (`03_COMPONENT_CATALOG.md`) but unshipped: every CauseWay-content export ships
  disabled until the owner's licence decision (OWN-04), and its labels are not governed yet (ESCALATIONS.md).
- A **social frame** is the 1200 × 630 template of a page's shared image, built only from governed text: the product
  name and the logo (72 px), the family rubric, the governed question where the page answers one, the title, the
  page's clock (a record's period and universe and its reference; a Reading's evidence period), the governed boundary
  (every record's "does not establish", a Reading's prohibited inference, a domain answer's first-screen figure
  boundary), the canonical link and the edition; on a card without a boundary the governed meta description follows
  the title without repeating it — 284 of the 286 descriptions open with the page title (ESCALATIONS.md, D6
  observation), so the card prints the title once and then the description's remainder, losing nothing but the
  separator. The build writes one per page and language into `out/_social/`; Code
  generates the images at build time and adds `og:image` only then (the reference site keeps Open Graph without image,
  gate F6-G01). Type sizes step down with the length of the governed text so that nothing is truncated: a shared image
  never crops a boundary.

Neither module authors a word: every string is a governed label, a governed field, a URL or the edition.
"""
from __future__ import annotations

import sys
from pathlib import Path

from .text import esc, iso  # the one text layer (escaping; ISO dates isolated, Lock §4.1.8)

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import discovery as DISC  # noqa: E402


def _doc(lang: str, title: str, body_class: str, body: str) -> str:
    d = "rtl" if lang == "ar" else "ltr"
    return (f'<!doctype html><html lang="{lang}" dir="{d}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>{esc(title)}</title><link rel="stylesheet" href="/assets/yfie.css"></head>'
            f'<body class="{body_class}"><main id="main">{body}</main></body></html>')


# ------------------------------------------------------------------------------------------------ export frame
def export_document(figure_html: str, v: dict, shell: dict) -> str:
    """One drawn figure as a portable document: identity line, then the figure with its detached frame."""
    ident = (f'<p class="exp-id"><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay" width="32" height="32"><span><b>{esc(shell["product"])}</b> · {esc(shell["edition"])}</span></p>')
    return _doc(shell["lang"], f'{v["title"]} — {shell["product"]}', "export-doc", f'<div class="exp">{ident}{figure_html}</div>')   # one box: identity inside its rules, a closing rule under the foot


# ------------------------------------------------------------------------------------------------ social frame
def _size(text: str, steps: tuple[tuple[int, str], ...]) -> str:
    """The class that steps the type size down with the governed text's length (never a crop)."""
    n = len(text or "")
    for limit, cls in steps:
        if n <= limit:
            return cls
    return steps[-1][1]


def after_title(title: str, desc: str) -> str:
    """The governed meta description without the title it opens with (284 of 286 do): the card prints the title once
    and then the description's remainder, so title + remainder is the whole description — nothing is dropped but the
    separator; a description that does not open with the title is printed whole."""
    t, d = (title or "").strip(), (desc or "").strip()
    core = t.rstrip(".。؟?!:")
    if core and d.startswith(core):
        rest = d[len(core):]
        rest = rest.lstrip(" .:;,·—–-؛،؟!")   # the separator between the title and the rest
        return rest
    return d


def social_document(page: dict, shell: dict, route: str) -> str:
    """The family's template, filled with the page's governed text (`08_ASSET_MAP.md` §3 lists the templates)."""
    lang = shell["lang"]; fam = page["family"]
    origin = DISC.origin()
    canon = DISC.url(DISC.localized(route, lang), origin)
    L = page.get("labels") or {}
    title = page.get("title") or ""
    rubric, question, clocks, boundary, b_label = "", "", [], "", ""
    desc = after_title(title, page.get("meta_description") or "") if fam not in ("Evidence Record", "Reading") else ""   # a record's or Reading's card carries its clocks and boundary instead
    if fam == "Evidence Record":
        b_label = L.get("boundary", "")
        rubric = L.get("family", "")
        clocks = [(L.get("period", ""), page.get("period", "")), (L.get("applies", ""), page.get("universe", ""))]
        boundary = page.get("does_not_establish") or ""   # every record's card shows its dates, so every card carries its boundary (brief §16)
        clocks.append((L.get("reference", ""), f'<bdi dir="ltr">{esc(page.get("id", ""))}</bdi>'))   # the record ID, isolated (Lock §4.1.8)
    elif fam == "Reading":
        rubric = L.get("eyebrow", ""); b_label = L.get("do_not_infer", "")
        question = page.get("question") or ""
        clocks = [(L.get("evidence_period", ""), page.get("evidence_period", ""))]
        boundary = page.get("prohibited_inference") or ""
    elif fam == "Domain Answer":
        rubric = L.get("answer_crumb", "") if page.get("question") else L.get("question_flow", ""); b_label = L.get("do_not", "")
        question = page.get("question") or ""
        pv = (page.get("visuals") or {}).get(page.get("primary_visual") or "")
        if pv:
            boundary = pv.get("prohibited_inference") or ""
    elif fam == "Measurement":
        rubric = L.get("flow", "")
    elif fam == "Orientation":
        rubric = shell["product"]
    elif fam == "Reference / Trust":
        rubric = L.get("flow", "")
    else:   # Question Entry, Evidence Directory, Comparison, Reading Index, Data & Source: the shared hub template
        rubric = L.get("flow", "") or shell["labels"].get("understand_explore_verify", "")
    tcls = _size(title, ((60, ""), (110, "long"), (10**9, "xlong")))
    # the whole frame steps down when the governed text is long in total (a shared image never crops a boundary)
    total = len(title) + len(question) + sum(len(k) + len(val) for k, val in clocks) + len(boundary) + (len(desc) if not boundary else 0)
    dense = "xdense" if total > 470 else ("dense" if total > 330 else "")
    head = (f'<div class="soc-head"><img src="/assets/CauseWay_Master_Logo.png" alt="CauseWay" width="72" height="72"><span>{esc(shell["product"])}'
            + (f'<span class="soc-fam">{esc(rubric)}</span>' if rubric and rubric != shell["product"] else "") + "</span></div>")
    body = []
    if question:
        body.append(f'<p class="soc-q">{iso(question)}</p>')
    body.append(f'<h1 class="soc-title {tcls}">{iso(title)}</h1>')
    for k, val in clocks:
        if val or k:
            body.append(f'<p class="soc-clock"><span class="k">{esc(k)}</span>{val if val.startswith("<bdi") else iso(val)}</p>' if val else f'<p class="soc-clock"><span class="k">{esc(k)}</span></p>')
    if desc and not boundary:
        body.append(f'<p class="soc-desc {_size(desc, ((160, ""), (10**9, "long")))}">{iso(desc)}</p>')
    if boundary:
        b_label = b_label or (page.get("labels") or {}).get("does_not_establish", "")
        body.append(f'<p class="soc-bnd {_size(boundary, ((170, ""), (10**9, "long")))}"><b>{esc(b_label)}{"" if b_label.endswith(":") else ":"}</b> {iso(boundary)}</p>')
    foot = f'<div class="soc-foot"><span class="canon"><bdi dir="ltr">{esc(canon)}</bdi></span><span class="ed">{esc(shell["edition"])}</span></div>'
    return _doc(lang, f'{title} — {shell["product"]}', f"social-doc {dense}".strip(), head + f'<div class="soc-body">{"".join(body)}</div>' + foot)
