# -*- coding: utf-8 -*-
"""Serving the site under a path of its domain (owner decision B1, 3 October 2026).

The decided address is https://causewaygrp.com/financial-inclusion-evidence/: Arabic at that root, English under /en/.
`public_origin` in site-src/deployment.json may therefore carry a path, and `scripts/discovery.py` derives the base path
from it ("/financial-inclusion-evidence"; "" when there is none).

Two kinds of address leave the build:

- Discovery addresses (canonical, hreflang, og:url, og:image, structured data, the sitemap, and the canonical address
  printed in a citation or under a figure) are the origin plus the page's path. The origin carries the base path, so
  they need nothing more.
- Everything else is root-absolute (`/en/…`, `/assets/…`, `/static-data/…`): links, images, the stylesheet, the font
  preloads, the stylesheet's own `url()`, the runtime's fetches, the language prefix it builds links with, the language
  switch and its stored preference, the root redirect, and the host header file's path patterns. `relocate()` moves
  those under the base path, once, after `scripts/build.py --out DIR` has written the published site.

It runs only for the published site and only when the base path is not empty. `dist/`, the review build every gate
serves at a server root, keeps root-relative links, and a build with no origin, or with an origin at a domain root, is
byte for byte the build made without this module. `scripts/tests/test_base_path.py` builds the decided origin into a
temporary directory, serves it under the path and proves that nothing escapes it; the deploy workflow publishes the
same output and sweeps it again.

What is not rewritten, on purpose: the `route` values of the search index and of the Compare data. They are route keys
(`/evidence/CLM-001/`), not addresses; the runtime joins them to its language prefix, and the prefix carries the base.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

# HTML attributes whose value is one address. The renderer writes every attribute in double quotes.
URL_ATTRS = ("href", "src", "action", "formaction", "poster", "cite", "data", "background", "manifest", "ping")
_ATTR = re.compile(r'(\s(?:' + "|".join(URL_ATTRS) + r')=")(/(?!/)[^"]*)"')
_SRCSET = re.compile(r'(\s(?:srcset|imagesrcset)=")([^"]*)"')
# `content` is an address only in a refresh and in the social metadata (absolute once an origin is set, which a base
# path always has; relocated here all the same, so the rule does not depend on that)
_REFRESH = re.compile(r'(<meta\s[^>]*?\bcontent="\d+;\s*url=)(/(?!/)[^"]*)"', re.I)
_META_URL = re.compile(r'(<meta\s+(?:property|name)="(?:og:(?:image|image:url|image:secure_url|url|audio|video)|twitter:image)"'
                       r'\s+content=")(/(?!/)[^"]*)"')
_CSS_URL = re.compile(r"""url\(\s*(['"]?)(/(?!/)[^'")\s]*)\1\s*\)""")
_STYLE_ATTR = re.compile(r'(\sstyle=")([^"]*)"')
_STYLE_EL = re.compile(r"(<style\b[^>]*>)(.*?)(</style>)", re.S | re.I)

# The runtime builds addresses in code, so its addresses are listed one by one. Each pattern must occur exactly as often
# as stated, or the build stops: a runtime change that adds or moves an address is then relocated on purpose, never by
# accident. {B} is the base path; {BRE} the same, escaped for a JavaScript regular-expression literal.
JS_PATCHES = {
    "assets/app.js": [
        # the language prefix every link the runtime writes starts with (search results, Compare, corrections)
        ("const prefix=location.pathname.startsWith('/en/')?'/en':'/ar';",
         "const prefix=location.pathname.startsWith('{B}/en/')?'{B}/en':'{B}/ar';", 1),
        # the language switch: the same page in the other language, query and hash kept
        ("let p=location.pathname.replace(/^\\/(ar|en)/,'');",
         "let p=location.pathname.replace(/^{BRE}(?:\\/(ar|en))?/,'');", 1),
        ("location.href='/'+target+p+location.search+location.hash;",
         "location.href='{B}/'+target+p+location.search+location.hash;", 1),
        # the search index and its governed aliases
        ("fetch('/static-data/", "fetch('{B}/static-data/", 2),
    ],
    "assets/lang-redirect.js": [
        # the root entry: the edition chosen before (the stored preference), otherwise Arabic
        ('location.replace("/"+l+"/");', 'location.replace("{B}/"+l+"/");', 1),
    ],
}
# Every other quoted literal that starts with "/" (single, double or back quote; a template with ${…} included) is
# counted after the patches, per file, and must occur exactly as often as listed here. These are route keys, which the
# runtime joins to its relocated language prefix, and the normaliser's prefix tests; none is an address on its own. A
# literal that is not listed stops the build until a patch relocates it or it is listed on purpose. (The adversarial
# verification of 3 October 2026 showed that the earlier rule, "a literal naming a top-level entry", let an address
# built by concatenation or a template through: '/'+lang+'/about/', `/${lang}/about/`.)
JS_ROUTE_KEYS = {
    "assets/app.js": {
        "'/'": 5, "'/evidence/'": 1, "'/data/#regulatory'": 1,
        "'/people/'": 1, "'/firms/'": 1, "'/finance/'": 1, "'/providers/'": 1, "'/payments/'": 1,
        "'/remittances/'": 1, "'/access/'": 1, "'/reforms/'": 1, "'/measurement/'": 1,
    },
    "assets/lang-redirect.js": {'"/"': 1},   # the closing slash of "{B}/"+l+"/"
}
_JS_LITERAL = re.compile(r"""(['"`])(/[^'"`\s]*)""")


def _prefix(base: str, path: str) -> str:
    return base + path


def relocate_srcset(base: str, value: str) -> str:
    parts = []
    for cand in value.split(","):
        lead = cand[:len(cand) - len(cand.lstrip())]
        body = cand.strip()
        if body.startswith("/") and not body.startswith("//"):
            body = _prefix(base, body)
        parts.append(lead + body)
    return ",".join(parts)


def relocate_css(base: str, text: str) -> str:
    return _CSS_URL.sub(lambda m: f"url({m.group(1)}{_prefix(base, m.group(2))}{m.group(1)})", text)


def relocate_html(base: str, text: str) -> str:
    text = _REFRESH.sub(lambda m: f'{m.group(1)}{_prefix(base, m.group(2))}"', text)
    text = _META_URL.sub(lambda m: f'{m.group(1)}{_prefix(base, m.group(2))}"', text)
    text = _ATTR.sub(lambda m: f'{m.group(1)}{_prefix(base, m.group(2))}"', text)
    text = _SRCSET.sub(lambda m: f'{m.group(1)}{relocate_srcset(base, m.group(2))}"', text)
    text = _STYLE_ATTR.sub(lambda m: f'{m.group(1)}{relocate_css(base, m.group(2))}"', text)
    return _STYLE_EL.sub(lambda m: m.group(1) + relocate_css(base, m.group(2)) + m.group(3), text)


def relocate_js(base: str, rel: str, text: str) -> str:
    for old, new, count in JS_PATCHES.get(rel, []):
        found = text.count(old)
        if found != count:
            raise SystemExit(f"base path: {rel} holds {found} of {old!r}, expected {count}; "
                             "update scripts/base_path.py JS_PATCHES with the runtime")
        text = text.replace(old, new.replace("{BRE}", base.replace("/", "\\/")).replace("{B}", base))
    found = Counter(m.group(1) + m.group(2) + m.group(1) for m in _JS_LITERAL.finditer(text)
                    if not m.group(2).startswith(base + "/"))
    listed = Counter(JS_ROUTE_KEYS.get(rel, {}))
    if found != listed:
        extra, gone = sorted((found - listed).elements()), sorted((listed - found).elements())
        raise SystemExit(f"base path: {rel} holds slash-leading literals outside the base path that are not listed "
                         f"{extra[:5]!r}, or lacks listed ones {gone[:5]!r}; relocate them in JS_PATCHES or list them "
                         "in JS_ROUTE_KEYS (scripts/base_path.py)")
    return text


def relocate_headers(base: str, text: str) -> str:
    """`_headers`: an unindented line is a path pattern; it is matched against the full request path."""
    out = []
    for line in text.splitlines(keepends=True):
        if line.startswith("/"):
            line = _prefix(base, line)
        out.append(line)
    return "".join(out)


def relocate(out: Path, base: str) -> int:
    """Move every root-absolute reference in the built site `out` under `base`. Returns the number of files changed."""
    if not base:
        return 0
    if not re.fullmatch(r"(?:/[a-z0-9-]+)+", base):
        raise SystemExit(f"base path: {base!r} is not a path of lowercase segments")
    changed = 0
    for f in sorted(p for p in out.rglob("*") if p.is_file()):
        rel = f.relative_to(out).as_posix()
        if f.suffix == ".html":
            fn = lambda t: relocate_html(base, t)  # noqa: E731
        elif f.suffix == ".css":
            fn = lambda t: relocate_css(base, t)  # noqa: E731
        elif f.suffix == ".js":
            fn = lambda t, rel=rel: relocate_js(base, rel, t)  # noqa: E731
        elif rel == "_headers":
            fn = lambda t: relocate_headers(base, t)  # noqa: E731
        else:
            continue   # images, fonts; robots.txt and sitemap.xml are written for the origin by scripts/discovery.py;
            # static-data/*.json holds route keys, which the runtime joins to its (relocated) language prefix
        old = f.read_text(encoding="utf-8")
        new = fn(old)
        if new != old:
            f.write_text(new, encoding="utf-8")
            changed += 1
    return changed
