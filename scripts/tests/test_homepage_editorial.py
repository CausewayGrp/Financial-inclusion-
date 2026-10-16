#!/usr/bin/env python3
"""Homepage pilot acceptance: governed reading order, bounded claims and real access.

Uses the generated site and local Chromium through the repository browser harness.
It does not assert human comprehension, WCAG conformance or release readiness.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'scripts/tests'))
from yfie.content import Content
from test_public_tools import serve
from playwright.sync_api import sync_playwright


def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def run():
    content = Content()
    server, base = serve()
    checks = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for lang in ('ar', 'en'):
                governed = content.home(lang)
                sections = {s['order']: s for s in governed['sections']}
                shell = content.shell(lang, '/')
                for width in (320, 390, 768, 1024, 1440):
                    page = browser.new_page(viewport={'width': width, 'height': 844})
                    page.goto(f'{base}/{lang}/')
                    page.evaluate('document.fonts.ready')
                    assert page.locator('h1').count() == 1
                    assert page.locator('html').get_attribute('dir') == ('rtl' if lang == 'ar' else 'ltr')
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
                    assert norm(' '.join(page.locator('#s3 .sent').all_text_contents())) == norm(sections[3]['body'])
                    assert page.locator('#s3 b.fnum').evaluate_all(
                        '(xs)=>xs.every(e=>getComputedStyle(e).direction==="ltr" && getComputedStyle(e).unicodeBidi==="isolate")')
                    assert norm(page.locator('#s4 .mt8').inner_text()) == norm(sections[4]['body'])
                    assert page.locator('#s4').is_visible()
                    assert page.locator('section[id]').evaluate_all('(xs)=>xs.map(x=>x.id)')[:3] == ['s3', 's4', 's9']
                    assert page.locator('#s9 .home-domains').count() == 1
                    assert page.locator('.home-domains h2').count() == 0
                    assert page.locator('.home-domain-grid a').evaluate_all('(xs)=>xs.map(a=>({label:a.textContent,href:a.getAttribute("href")}))') == [
                        {'label': d['label'], 'href': d['href']} for d in shell['domains']]
                    for order in (5, 6, 7, 8):
                        assert page.locator(f'#s{order} details').get_attribute('open') is None
                    for record in governed['records'][:3]:
                        obj = page.locator(f'[data-home-record="{record["id"]}"]')
                        boundary = norm(obj.locator('.home-limit p').inner_text())
                        assert boundary and norm(record['does_not_establish']).startswith(boundary)
                        assert obj.locator(f'a[href="{record["href"]}"]').count() == 1
                        assert norm(obj.locator('.clock .v').inner_text()) == norm(record['period'])
                        assert norm(obj.locator('.compact .small').inner_text()) == norm(record['universe'])
                    # Retain the useful index and destinations formerly offered in the sidebar.
                    for target in ('s3', 's4', 's9', 's5', 's6', 's7', 's8', 'sf'):
                        link = page.locator(f'.strip a[href="#{target}"]')
                        assert link.count() == 1 and link.is_visible()
                        link.focus()
                        assert link.evaluate('(e)=>e===document.activeElement')
                        assert link.evaluate('(e)=>getComputedStyle(e).outlineStyle') != 'none'
                    for route in ('readings', 'measurement', 'data', 'methodology'):
                        assert page.locator(f'a[href="/{lang}/{route}/"]:visible').count() > 0
                    # A section link lands on its visible, keyboard-operable summary.
                    page.locator('.strip a[href="#s6"]').focus()
                    page.keyboard.press('Enter')
                    assert page.locator('#s6 summary').is_visible()
                    page.locator('#s6 summary').focus()
                    page.keyboard.press('Enter')
                    assert page.locator('#s6 details').get_attribute('open') is not None
                    assert page.locator('#system').is_visible()
                    # The established deep link inside the disclosure opens it on arrival.
                    page.goto(f'{base}/{lang}/#system')
                    page.wait_for_function('document.querySelector("#s6 details").open')
                    if width < 900:
                        page.locator('[data-menu]').click()
                        assert page.locator('[data-menu]').get_attribute('aria-expanded') == 'true'
                        assert page.locator('#primary-nav [data-menu-domains] a').count() == 8
                        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
                        page.keyboard.press('Escape')
                    # Genuine keyboard activation of a record, followed by source and return paths.
                    page.locator(f'[data-home-record="CLM-003"] a').focus()
                    page.keyboard.press('Enter')
                    page.wait_for_url(f'**/{lang}/evidence/CLM-003/')
                    assert page.locator('main .source-locator').count() > 0
                    assert page.locator(f'main a[href="/{lang}/payments/"]').count() > 0
                    checks.append({'lang': lang, 'width': width, 'status': 'pass'})
                    page.close()
                # No-JavaScript remains a useful static publication.
                context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
                page = context.new_page()
                page.goto(f'{base}/{lang}/')
                assert page.locator('#s4').is_visible()
                assert page.locator('#s9 .home-domain-grid a').count() == 8
                assert page.locator('[data-home-record="CLM-003"] .home-limit').is_visible()
                page.locator('.controls [data-lang]').click()
                assert page.locator('html').get_attribute('lang') != lang
                context.close()
            browser.close()
    finally:
        server.shutdown()
    print(f'HOMEPAGE EDITORIAL: {len(checks)}/10 bilingual width checks pass; static fallback passes')
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(json.dumps(checks, indent=2) + '\n')


if __name__ == '__main__':
    run()
