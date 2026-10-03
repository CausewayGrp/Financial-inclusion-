# -*- coding: utf-8 -*-
"""Discovery contract (directive D7 §F6): canonical and alternate links, robots policy, sitemap and structured data.

One module, used by scripts/build.py to write the pages and by scripts/validate.py to check them, so the contract has
one implementation. The public origin lives in site-src/deployment.json. It is null until the owner fixes the release
domain (a release-only decision). With no origin the reference build is a pre-release build: links are root-relative,
robots.txt disallows crawling and no sitemap is written. With an origin every link is absolute, robots.txt allows
crawling and points to sitemap.xml, and the sitemap lists every localized page with its language alternates.

The origin may carry a path (owner decision B1, 3 October 2026: https://causewaygrp.com/financial-inclusion-evidence).
Every absolute URL here is the origin plus the page's path, so it carries that path already; `base_path()` names it for
`scripts/base_path.py`, which relocates the build's root-absolute references under it. `override()` lets one build
(`scripts/build.py --origin URL --out DIR`) use another origin without touching site-src/deployment.json.

Nothing here invents metadata: no author (the Readings' authorship is not governed), no publication or modification
date, and no Dataset type (the resource publishes evidence records and a source directory, not datasets). The one
image is the page's own governed social image (EAD-09), rasterised from the design's template by
`scripts/social_images.py` and copied into the build; it carries no text the page does not already print.
"""
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENT = ROOT / "site-src" / "deployment.json"
LANGS = ("en", "ar")
PUBLISHER = {"@type": "Organization", "name": "CauseWay"}

# https://, a lowercase host (and port), then an optional path of lowercase segments of a-z, 0-9 and "-"; no trailing
# slash, no query, no fragment, no user information.
_LABEL = r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
ORIGIN_RULE = re.compile(rf"https://{_LABEL}(?:\.{_LABEL})*(?::[0-9]{{1,5}})?(?:/[a-z0-9-]+)*")
ORIGIN_RULE_TEXT = ("public_origin must be null or https://<host> with an optional path of lowercase segments "
                    "(a-z, 0-9 and '-'), with no trailing slash, query or fragment")
_OVERRIDE: dict = {}


def check_origin(value, where="site-src/deployment.json"):
    """The origin rule, for the deployment file and for `scripts/build.py --origin`."""
    if value is not None and not (isinstance(value, str) and ORIGIN_RULE.fullmatch(value)):
        raise SystemExit(f"{where}: {ORIGIN_RULE_TEXT} (got {value!r})")
    return value


def override(**values):
    """For one build only (scripts/build.py --origin): the deployment file is read as if it held these values."""
    if "public_origin" in values:
        check_origin(values["public_origin"], "--origin")
    _OVERRIDE.update(values)


def deployment():
    d = json.loads(DEPLOYMENT.read_text(encoding="utf-8"))
    d.update(_OVERRIDE)
    check_origin(d.get("public_origin"))
    return d


def origin():
    return deployment().get("public_origin")


def base_path(org=None):
    """The path the site is served under: "" with no origin or an origin at a domain root, otherwise the origin's path
    ("/financial-inclusion-evidence"), with no trailing slash."""
    return urlsplit(org).path if org else ""


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
    base = base_path(org)
    if not base:
        return f"User-agent: *\nAllow: /\n\nSitemap: {org}/sitemap.xml\n"
    # Under a path this file is not where crawlers look: they read only the domain's own /robots.txt. It is written for
    # completeness; the web administrator names the sitemap there, or in Search Console (docs/RELEASE_RUNBOOK.md).
    return (f"# This site is served under {base}/. Crawlers read only the domain's root /robots.txt, which names the\n"
            f"# sitemap below (or the sitemap is submitted in Search Console): docs/RELEASE_RUNBOOK.md, \"Hosting\".\n"
            f"User-agent: *\nAllow: {base}/\n\nSitemap: {org}/sitemap.xml\n")


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


OG_LOCALE = {"en": "en_GB", "ar": "ar_YE"}


SOCIAL_IMAGE = {"width": 1200, "height": 630}


def social_image_path(route, lang):
    """Where the build puts this page's social image (EAD-09; one per route and language, from the governed template)."""
    return "/assets/social/" + (str(route or "/").strip("/").replace("/", "_") or "home") + f"__{lang}.png"


def social_meta(title, description, lang, route, product, kind="website", org=None, image=True):
    """Open Graph and card metadata from the page's own governed title and description. `og:image` is the page's own
    governed social image, rasterised at build time from the design's template (EAD-09) — absolute with a public
    origin, root-relative before one, exactly as every other URL here behaves. `og:url` only with a public origin."""
    other = "ar" if lang == "en" else "en"
    tags = [("og:type", "article" if kind == "article" else "website"), ("og:site_name", product), ("og:title", title),
            ("og:description", description), ("og:locale", OG_LOCALE[lang]), ("og:locale:alternate", OG_LOCALE[other])]
    if org:
        tags.append(("og:url", url(localized(route, lang), org)))
    if image:
        tags += [("og:image", url(social_image_path(route, lang), org)),
                 ("og:image:width", SOCIAL_IMAGE["width"]), ("og:image:height", SOCIAL_IMAGE["height"]),
                 ("og:image:alt", title)]
    out = "".join(f'<meta property="{k}" content="{html.escape(str(v), quote=True)}">' for k, v in tags)
    return out + f'<meta name="twitter:card" content="{"summary_large_image" if image else "summary"}">'


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
