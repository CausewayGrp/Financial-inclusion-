# -*- coding: utf-8 -*-
"""Mechanics shared by the thesis prototypes: the hooks the browser suites need (skip link, search dialog, utilities),
a mobile-rule doubler (media query + `.vp-m` root class, so a fixed-width canvas artboard can show the narrow form),
and base CSS that carries no design decision (screen-reader-only text, reduced motion, forced colours, print basics)."""
from __future__ import annotations

import re

from proto_common import esc, json_block


def mobile_rules(css: str, max_width: int = 900) -> str:
    """Emit `css` both under a max-width media query and under a `.vp-m` root class."""
    def prefix(s: str) -> str:
        s = s.strip()
        if s.startswith("html"):
            return s.replace("html", "html.vp-m", 1)
        if s.startswith(":root"):
            return ".root.vp-m" + s[5:]
        if s.startswith(".root"):
            return ".root.vp-m" + s[5:]
        if s.startswith("[dir=rtl].root"):
            return "[dir=rtl].root.vp-m" + s[14:]
        return ".vp-m " + s
    rules = []
    for chunk in css.split("}"):
        if "{" not in chunk:
            continue
        sel, body = chunk.split("{", 1)
        sels = ",".join(prefix(s) for s in sel.split(","))
        rules.append(f"{sels}{{{body}}}")
    return f"@media (max-width:{max_width}px){{{css}}}" + "".join(rules)


def base_css(focus: str) -> str:
    return (
        "*,*::before,*::after{box-sizing:border-box}html{-webkit-text-size-adjust:100%}img{max-width:100%;height:auto;display:block}"
        "button,input,select{font:inherit;color:inherit}"
        ".sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}"
        f".skip{{position:absolute;inset-inline-start:16px;top:-200px;padding:12px 16px;background:#fff;color:#111;border:2px solid {focus};z-index:1000;text-decoration:none}}.skip:focus{{top:12px}}"
        f":focus-visible{{outline:3px solid {focus};outline-offset:3px}}"
        ".table-wrap{overflow-x:auto;max-width:100%}.table-wrap:focus-visible{outline-offset:6px}"
        "dialog.search{border:0;padding:0;max-width:min(680px,92vw);width:100%}dialog.search::backdrop{background:rgba(20,32,43,.55)}"
        "@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}"
        "@media (forced-colors:active){.mark,.path,.axis,.grid{forced-color-adjust:auto}[data-boundary],.boundary{border-color:CanvasText!important}}"
        "@media print{header nav,dialog,.utilities,.trail,.toc,footer nav,.noscript{display:none!important}a[href^='http']::after{content:' (' attr(href) ')';font-size:.8em}}"
    )


def search_dialog(shell: dict) -> str:
    L = shell["labels"]
    return (f'<dialog id="search-dialog" class="search" aria-labelledby="search-dialog-title"><div class="search-panel"><div class="search-head"><strong id="search-dialog-title">{esc(L["search_title"])}</strong>'
            f'<button type="button" class="tbtn" data-search-close aria-label="{esc(L["search_close"])}">{esc(L["search_close"])}</button></div>'
            f'<input id="global-search-dialog" data-search-input class="search-input" placeholder="{esc(L["search_placeholder"])}" aria-label="{esc(L["search"])}">'
            f'<div class="search-status" data-search-status role="status" aria-live="polite" aria-label="{esc(L["search_status"])}"></div><div data-search-results class="search-results"></div></div></dialog>')


def utilities(shell: dict, cls: str = "utilities") -> str:
    L = shell["labels"]
    other = shell["other_lang"]
    return (f'<div class="{cls}"><button type="button" class="tbtn" data-search-open aria-label="{esc(L["search"])}">{esc(L["search"])}</button>'
            f'<button type="button" class="tbtn" data-cite aria-label="{esc(L["cite"])}">{esc(L["cite"])}</button>'
            f'<a class="tbtn" href="{shell["contact_href"]}">{esc(L["report"])}</a>'
            f'<button type="button" class="tbtn lang" data-lang="{other}" aria-label="{esc(L["lang_switch_action"])}" lang="{other}" dir="{"ltr" if other == "en" else "rtl"}">{esc(L["lang_switch_name"])}</button>'
            f'<button type="button" class="tbtn menu" data-menu aria-label="{esc(L["menu"])}" aria-controls="primary-nav" aria-expanded="false">{esc(L["menu"])}</button></div>'
            f'<div id="utility-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true" data-copied-label="{esc(L["copied"])}"></div>')


def head(page: dict, shell: dict, route: str, css_href: str, kind: str = "website", extra: str = "", root_class: str = "") -> str:
    import sys
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[3]  # repository root
    sys.path.insert(0, str(ROOT / "scripts"))
    import discovery as DISC
    lang = shell["lang"]
    origin = DISC.origin()
    cls = f' class="{root_class}"' if root_class else ""
    return (f'<!doctype html><html lang="{lang}" dir="{shell["dir"]}"{cls}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(page["title"])} — {esc(shell["product"])}</title><meta name="description" content="{esc(page.get("meta_description"))}">{extra}'
            f'<link rel="stylesheet" href="{css_href}">{DISC.head_links(route, lang, origin)}'
            f'{DISC.social_meta(page["title"], page.get("meta_description") or "", lang, route, shell["product"], kind, origin)}</head><body>')


def tail(shell: dict) -> str:
    return f'{json_block("yfie-ui", shell["ui_json"])}<script src="/assets/app.js" defer></script></body></html>'


def nav_items(shell: dict) -> list[dict]:
    """Flatten the governed primary navigation: groups keep their label; children carry `group`."""
    out = []
    for item in shell["nav"]:
        if item.get("children"):
            out.append({"group": item["label"], "children": item["children"], "active": any(k["active"] for k in item["children"])})
        else:
            out.append({"label": item["label"], "href": item["href"], "active": item.get("active", False)})
    return out


def source_card(s: dict, cls: str = "src") -> str:
    """One public source: governed title or 'Original source' + reference; kind line; actions; rights note."""
    L = s["labels"]
    ref = f'<span class="ref">{esc(s["reference_label"])} <bdi dir="ltr">{esc(s["id"])}</bdi></span>'
    if s["display_ready"] and s["title"]:
        head_ = f'<strong dir="auto">{esc(s["title"])}</strong><span class="kind" dir="auto">{esc(s["kind_line"])}</span>{ref}'
    else:
        head_ = f'<strong>{esc(s["untitled_label"])}</strong>{ref}'
    rights = f'<p class="rights">{esc(s["rights_note"])}</p>' if s["rights_note"] else ""
    return (f'<article class="{cls}" data-evidence-source="{esc(s["id"])}"><div class="src-head">{head_}</div>'
            f'<div class="src-actions"><a href="{s["data_href"]}">{esc(L["open_source_record"])}</a>'
            f'<a href="{esc(s["url"])}" rel="noopener noreferrer" target="_blank">{esc(L["open_original"])}</a>'
            f'<button type="button" class="tbtn" data-source-cite data-source-citation="{esc(s["cite_payload"])}">{esc(L["copy_reference"])}</button></div>{rights}</article>')


def responsive_rules(css: str, media: str, cls: str) -> str:
    """Emit `css` under `@media (media)` and again with every selector scoped to a root class `cls`."""
    def prefix(sel: str) -> str:
        sel = sel.strip()
        if sel.startswith("html"):
            return sel.replace("html", f"html.{cls}", 1)
        if sel.startswith(":root"):
            return f".root.{cls}" + sel[5:]
        if sel.startswith(".root"):
            return f".root.{cls}" + sel[5:]
        if sel.startswith("[dir=rtl].root"):
            return f"[dir=rtl].root.{cls}" + sel[14:]
        if sel.startswith("[dir=rtl]"):
            return f"[dir=rtl].{cls} " + sel[9:].strip() if sel[9:].strip() else f"[dir=rtl].{cls}"
        return f".{cls} " + sel
    rules = []
    for chunk in css.split("}"):
        if "{" not in chunk:
            continue
        sel, body = chunk.split("{", 1)
        rules.append(",".join(prefix(x) for x in sel.split(",")) + "{" + body + "}")
    return f"@media ({media}){{{css}}}" + "".join(rules)
