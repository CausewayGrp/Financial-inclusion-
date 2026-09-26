# -*- coding: utf-8 -*-
"""Discovery contract (directive D7 §F6): canonical and alternate links, robots policy, sitemap and structured data.

One module, used by scripts/build.py to write the pages and by scripts/validate.py to check them, so the contract has
one implementation. The public origin lives in site-src/deployment.json. It is null until the owner fixes the release
domain (a release-only decision). With no origin the reference build is a pre-release build: links are root-relative,
robots.txt disallows crawling and no sitemap is written. With an origin every link is absolute, robots.txt allows
crawling and points to sitemap.xml, and the sitemap lists every localized page with its language alternates.

Nothing here invents metadata: no author (the Readings' authorship is not governed), no publication or modification
date, no image, and no Dataset type (the resource publishes evidence records and a source directory, not datasets).
"""
import json
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENT = ROOT / "site-src" / "deployment.json"
LANGS = ("en", "ar")
PUBLISHER = {"@type": "Organization", "name": "CauseWay"}


def deployment():
    d = json.loads(DEPLOYMENT.read_text(encoding="utf-8"))
    origin = d.get("public_origin")
    if origin is not None:
        if not (isinstance(origin, str) and origin.startswith("https://") and not origin.endswith("/")):
            raise SystemExit("site-src/deployment.json: public_origin must be null or an https:// origin without a trailing slash")
    return d


def origin():
    return deployment().get("public_origin")


def url(path, org=None):
    """Absolute when an origin is set, root-relative otherwise."""
    return (org + path) if org else path


def localized(route, lang):
    clean = str(route or "/").strip("/")
    return f"/{lang}/" + (clean + "/" if clean else "")


def head_links(route, lang, org=None):
    """Self-canonical in the page's own language; reciprocal hreflang for both editions; x-default is the root, which
    sends a reader to the language they chose before, or to Arabic (the neutral entry route)."""
    out = [f'<link rel="canonical" href="{url(localized(route, lang), org)}">']
    for alt in LANGS:
        out.append(f'<link rel="alternate" hreflang="{alt}" href="{url(localized(route, alt), org)}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{url("/", org)}">')
    return "".join(out)


def robots_txt(org=None):
    if not org:
        return ("# Pre-release reference build: not for indexing.\n"
                "# At release the owner sets public_origin in site-src/deployment.json; the build then allows crawling\n"
                "# and writes sitemap.xml.\n"
                "User-agent: *\nDisallow: /\n")
    return f"User-agent: *\nAllow: /\n\nSitemap: {org}/sitemap.xml\n"


def sitemap_xml(routes, org):
    """Every localized page once, with its reciprocal language alternates and x-default. No lastmod: the Master holds no
    page-level modification date."""
    if not org:
        raise ValueError("a sitemap needs an absolute origin")
    rows = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for route in routes:
        for lang in LANGS:
            rows.append(f"<url><loc>{xml_escape(url(localized(route, lang), org))}</loc>")
            for alt in LANGS:
                rows.append(f'<xhtml:link rel="alternate" hreflang="{alt}" href="{xml_escape(url(localized(route, alt), org))}"/>')
            rows.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{xml_escape(url("/", org))}"/></url>')
    rows.append("</urlset>")
    return "\n".join(rows) + "\n"


def ld_script(obj):
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/ld+json">{text}</script>'


def website_ld(lang, product, org=None):
    return {"@context": "https://schema.org", "@type": "WebSite", "name": product, "inLanguage": lang,
            "url": url(localized("/", lang), org), "publisher": PUBLISHER}


def breadcrumb_ld(parent_route, parent_label, current_name, lang, org=None):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": parent_label, "item": url(localized(parent_route, lang), org)},
        {"@type": "ListItem", "position": 2, "name": current_name}]}


def article_ld(route, lang, headline, description, product, org=None):
    """A Reading is an analytical article published by CauseWay within this resource. Only governed fields are used."""
    return {"@context": "https://schema.org", "@type": "Article", "headline": headline, "description": description,
            "inLanguage": lang, "mainEntityOfPage": url(localized(route, lang), org), "publisher": PUBLISHER,
            "isPartOf": {"@type": "WebSite", "name": product, "url": url(localized("/", lang), org)}}
