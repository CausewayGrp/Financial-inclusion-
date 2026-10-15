#!/usr/bin/env python3
"""Stage A domain-figure navigation: four figures, both editions, mobile and desktop.

No invented Passport destination: figures without one retain their content and lose the misleading action.
Existing domain -> Evidence Record -> back journeys remain usable. Screenshots, when requested, stay outside dist.
"""
import os
from pathlib import Path
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
from test_public_tools import serve

FIGURES = {'finance': ('VIS-MFI-DIVERGENCE', 'VIS-CBY-MONETARY-SNAPSHOT', 'VIS-YER-MARKET-RATE'),
           'access': ('VIS-ACCESS-EVIDENCE-LAYER',)}


def main():
    server, base = serve()
    count = 0
    try:
        with sync_playwright() as p:
            args = {'executable_path': os.environ['YFIE_CHROMIUM']} if os.environ.get('YFIE_CHROMIUM') else {}
            browser = p.chromium.launch(**args)
            for lang in ('en', 'ar'):
                for width in (390, 1440):
                    page = browser.new_page(viewport={'width': width, 'height': 900})
                    for route, vids in FIGURES.items():
                        address = f'{base}/{lang}/{route}/'
                        for vid in vids:
                            page.goto(address, wait_until='networkidle')
                            figure = page.locator(f'figure[data-visual-id="{vid}"]')
                            assert figure.count() == 1, vid
                            # Finance intentionally places the supporting figures in a disclosure.
                            folds = figure.locator('xpath=ancestor::details')
                            for i in range(folds.count()):
                                fold = folds.nth(i)
                                if not fold.evaluate('(el) => el.open'):
                                    fold.locator(':scope > summary').click()
                            assert figure.inner_text().strip(), vid
                            figure.scroll_into_view_if_needed()
                            assert figure.is_visible(), vid
                            assert figure.locator('.canon, .canon-l, .canon-p, .canon-s').count() == 0, (lang, vid, 'misleading record action')
                            # Real, already published records remain reachable through the domain's evidence list.
                            link = page.locator(f'main a[href^="/{lang}/evidence/"]:not([href="/{lang}/evidence/"])').first
                            href = link.get_attribute('href')
                            assert href and href != f'/{lang}/evidence/', (lang, vid, 'missing domain evidence destination')
                            link.click()
                            page.wait_for_url(base + href)
                            assert page.locator('main h1').inner_text().strip()
                            page.go_back(wait_until='networkidle')
                            assert urlsplit(page.url).path == f'/{lang}/{route}/'
                            assert page.locator(f'figure[data-visual-id="{vid}"]').count() == 1
                            count += 1
                        if os.environ.get('YFIE_RECONCILIATION_SCREENSHOTS'):
                            out = Path(os.environ['YFIE_RECONCILIATION_SCREENSHOTS']); out.mkdir(parents=True, exist_ok=True)
                            page.screenshot(path=str(out / f'{route}-{lang}-{width}.png'), full_page=True)
                    page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    print(f'STAGE A FIGURE NAVIGATION PASS: {count} journeys; four figures × EN/AR × 390/1440px')


if __name__ == '__main__':
    main()
