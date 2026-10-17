# -*- coding: utf-8 -*-
"""Behavioural regression tests for the public tools of the static baseline (Pre-Tranche-C P2).

  python3 scripts/tests/test_public_tools.py            (after scripts/build.py; needs Python Playwright + Chromium)
  YFIE_SITE_DIR=design/reference/out python3 scripts/tests/test_public_tools.py   (the same tests on another built site)

Serves dist/ (or the directory named by YFIE_SITE_DIR, relative to the repository root or absolute) on a local port and drives the pages in headless Chromium. Each test states the contract it protects
(handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md; site-src/content/content/navigation_interaction.json "interaction_tools").
Exit code 0 = all tests pass; 1 = a behaviour regressed; 2 = the browser harness is unavailable.
"""
import functools, http.server, json, os, re, socket, sys, threading, traceback
from urllib.parse import quote, unquote, urljoin, urlsplit

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIST = os.path.join(ROOT, os.environ.get("YFIE_SITE_DIR") or "dist")   # F9: the reference implementation is tested unchanged
RESULTS = []


def serve():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    handler = functools.partial(Quiet, directory=DIST)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{port}"


def test(name):
    def deco(fn):
        fn.__test_name__ = name
        return fn
    return deco


def records_param(page):
    return page.evaluate("new URLSearchParams(location.search).get('records')")


def slots(page):
    return page.evaluate("['#compare-a','#compare-b','#compare-c','#compare-d'].map(s=>document.querySelector(s).value)")


def selection(page):
    """The comparison state: the ordered list of selected records (an empty optional slot carries no state)."""
    return [x for x in slots(page) if x]


def verdict(page):
    el = page.query_selector("[data-compare-verdict]")
    return el.get_attribute("data-compare-verdict") if el else None


# ------------------------------------------------------------------------------------------------ Compare (P2.1)
@test("compare: default view writes its selection to the URL (2 IDs, slot order)")
def t_default(page, base):
    page.goto(base + "/en/evidence/compare/")
    s = slots(page)
    assert records_param(page) == ",".join(x for x in s if x), (records_param(page), s)
    assert len([x for x in s if x]) == 2 and verdict(page), "default comparison not drawn"


@test("compare: selection serialises deterministically; reload and a copied link reproduce it")
def t_roundtrip(page, base):
    page.goto(base + "/en/evidence/compare/")
    opts = page.evaluate("[...document.querySelectorAll('#compare-c option')].map(o=>o.value).filter(Boolean)")
    page.select_option("#compare-c", opts[2])
    s = selection(page); v = verdict(page); url = page.url
    assert records_param(page) == ",".join(s)
    page.reload()
    assert selection(page) == s and verdict(page) == v, "reload lost the comparison"
    p2 = page.context.new_page(); p2.goto(url)
    assert selection(p2) == s and verdict(p2) == v, "copied link did not reproduce the comparison"
    p2.close()


@test("compare: language switch keeps the comparison (query preserved)")
def t_lang(page, base):
    page.goto(base + "/en/evidence/compare/")
    opts = page.evaluate("[...document.querySelectorAll('#compare-d option')].map(o=>o.value).filter(Boolean)")
    page.select_option("#compare-d", opts[-1])
    s, v = selection(page), verdict(page)
    page.click("[data-lang]")
    page.wait_for_url("**/ar/evidence/compare/**")
    assert selection(page) == s and verdict(page) == v, (selection(page), s)
    assert records_param(page) == ",".join(s), "Arabic page did not keep the same URL state"


@test("compare: one valid reader record loads, and five IDs stay a count error")
def t_count(page, base):
    page.goto(base + "/en/evidence/compare/?records=CLM-001")
    assert page.query_selector("[data-compare-url-error]") is None
    assert page.evaluate("document.querySelector('#compare-a').value") == "CLM-001"
    assert verdict(page) is None
    page.goto(base + "/ar/evidence/compare/?records=CLM-001")
    assert page.query_selector("[data-compare-url-error]") is None
    assert page.evaluate("document.querySelector('#compare-a').value") == "CLM-001"
    page.goto(base + "/en/evidence/compare/?records=CLM-001,CLM-054,CLM-010,CLM-041,CLM-042")
    el = page.query_selector("[data-compare-url-error]")
    assert el and el.get_attribute("data-compare-url-error") == "count" and el.get_attribute("role") == "alert"
    assert verdict(page) is None


@test("compare: unknown ID is a technical input error naming the ID")
def t_unknown(page, base):
    page.goto(base + "/ar/evidence/compare/?records=CLM-001,NOT-A-RECORD")
    el = page.query_selector("[data-compare-url-error]")
    assert el and el.get_attribute("data-compare-url-error") == "unknown" and "NOT-A-RECORD" in el.inner_text()
    assert verdict(page) is None


@test("compare: malformed list is a technical input error")
def t_malformed(page, base):
    for q in ("CLM-001,,CLM-054", "CLM-001,<x>", "", "CLM-001,CLM-054,CLM-010,CLM-041,CLM-042"):
        page.goto(base + "/en/evidence/compare/?records=" + quote(q, safe=","))
        el = page.query_selector("[data-compare-url-error]")
        assert el, f"no technical error for {q!r}"
        assert verdict(page) is None


@test("compare: a duplicated record stays visibly invalid")
def t_duplicate(page, base):
    page.goto(base + "/en/evidence/compare/")
    first = slots(page)[0]
    page.goto(base + f"/en/evidence/compare/?records={first},{first}")
    assert verdict(page) == "same-record", verdict(page)


@test("compare: an error clears once the reader chooses records")
def t_recover(page, base):
    page.goto(base + "/en/evidence/compare/?records=CLM-001")
    opts = page.evaluate("[...document.querySelectorAll('#compare-b option')].map(o=>o.value)")
    page.select_option("#compare-b", opts[1])
    assert page.query_selector("[data-compare-url-error]") is None and verdict(page)
    assert records_param(page).count(",") == 1


@test("compare: IDs containing '+' survive the URL round trip")
def t_plus(page, base):
    page.goto(base + "/en/evidence/compare/")
    ids = page.evaluate("JSON.parse(document.getElementById('yfie-compare').textContent).map(x=>x.id)")
    plus = [i for i in ids if "+" in i]
    if not plus:
        return "SKIP (no compare record carries '+')"
    page.goto(base + "/en/evidence/compare/?records=" + quote(plus[0], safe="") + "," + quote(ids[0], safe=""))
    assert slots(page)[0] == plus[0]


@test("compare: '+' in an ID is percent-encoded by the serialiser and decoded intact")
def t_plus_codec(page, base):
    page.goto(base + "/en/evidence/compare/")
    got = page.evaluate("new URLSearchParams('?records='+['MF-ORIG-001+002','CLM-001'].map(encodeURIComponent).join(',')).get('records')")
    assert got == "MF-ORIG-001+002,CLM-001", got


@test("compare: table semantics and text-labelled states (no colour-only meaning)")
def t_compare_table(page, base):
    page.goto(base + "/ar/evidence/compare/")
    assert page.query_selector(".compare-table caption"), "comparison table has no caption"
    assert page.evaluate("[...document.querySelectorAll('.compare-table th')].every(th=>th.getAttribute('scope'))"), "header cell without scope"
    labels = page.evaluate("[...document.querySelectorAll('.compare-table tbody tr')].map(tr=>tr.querySelector('.compare-state')?.textContent.trim())")
    assert labels and all(labels), "a comparison row has no text state label"


# ------------------------------------------------------------------------------------------------ Search (P2.3 / P2.4)
@test("search: dialog opens by keyboard, focuses its input, closes on Escape and returns focus to the opener")
def t_search_dialog(page, base):
    page.goto(base + "/en/")
    page.focus("[data-search-open]")
    page.keyboard.press("Enter")
    page.wait_for_selector("#search-dialog[open]")
    page.wait_for_function("document.activeElement && document.activeElement.id==='global-search-dialog'", timeout=2000)
    page.keyboard.press("Escape")
    page.wait_for_function("!document.querySelector('#search-dialog').open")
    page.wait_for_function("document.activeElement.matches('[data-search-open]')", timeout=2000)   # focus returns to the opener
    page.keyboard.press("Control+k")
    page.wait_for_selector("#search-dialog[open]")
    assert page.evaluate("document.querySelector('#search-dialog').getAttribute('aria-labelledby')")


@test("search: results render; no match is not presented as no evidence")
def t_search_results(page, base):
    for lang, q, nonsense in (("en", "account ownership", "zzqqxxnotaword"), ("ar", "امتلاك الحساب", "ضضضقققغغغ")):
        page.goto(f"{base}/{lang}/evidence/")
        page.fill("#global-search", q)
        page.wait_for_selector("#search-results .search-hit")
        page.fill("#global-search", nonsense)
        page.wait_for_selector("#search-results [data-search-empty]")
        txt = page.inner_text("#search-results")
        assert ("does not mean" in txt) if lang == "en" else ("لا يعني" in txt), txt


@test("search: the page's own query is URL-addressable, reloadable and survives a language switch")
def t_search_url_state(page, base):
    """EAD-06 / handoff §2: tool state that matters is in the URL. The directory's own search owns the page address;
    the dialog, which floats over whatever page the reader is on, must leave it alone."""
    page.goto(base + "/en/evidence/")
    page.fill("#global-search", "remittances")
    page.wait_for_selector("#search-results .search-hit")
    assert page.evaluate("new URLSearchParams(location.search).get('q')") == "remittances", page.url

    page.goto(base + "/en/evidence/?q=remittances")          # a shared or reloaded address restores the search
    page.wait_for_selector("#search-results .search-hit")
    assert page.input_value("#global-search") == "remittances"

    page.click("[data-lang]")                                 # and it survives the switch to the other edition
    page.wait_for_url("**/ar/evidence/**")
    page.wait_for_selector("#search-results .search-hit")
    assert page.evaluate("new URLSearchParams(location.search).get('q')") == "remittances", page.url

    page.goto(base + "/en/evidence/?q=remittances")           # clearing the field clears the address
    page.wait_for_selector("#search-results .search-hit")
    page.fill("#global-search", "")
    page.wait_for_function("new URLSearchParams(location.search).get('q')===null")

    page.goto(base + "/en/people/")                           # the dialog never rewrites the page it floats over
    page.click("[data-search-open]")
    page.fill("#global-search-dialog", "remittances")
    page.wait_for_selector("#search-dialog .search-hit")
    assert page.evaluate("location.search") == "", page.url


@test("search: capped hits state the true total and lead to the Evidence directory; the result-type filter narrows and is URL-addressable")
def t_search_capped_and_typed(page, base):
    """A6 / C7 and EAD-06 (release candidate G4): the dialog shows ten hits; when more match, the status gives the true
    total in the governed form and a link carries the query to the Evidence directory filtered to evidence records,
    where every match is shown and the result type is read back from the address."""
    page.goto(base + "/en/people/")
    page.click("[data-search-open]")
    page.fill("#global-search-dialog", "remittances")
    page.wait_for_selector("#search-dialog .search-see-all a")
    shown = page.evaluate("document.querySelectorAll('#search-dialog .search-hit').length")
    status = page.inner_text("#search-dialog [data-search-status]")
    m = re.fullmatch(r"Showing (\d+) of (\d+) results", status.strip())
    assert m and int(m.group(1)) == shown == 10 and int(m.group(2)) > 10, status
    href = page.get_attribute("#search-dialog .search-see-all a", "href")
    assert href == urlsplit(base).path + "/en/evidence/?q=remittances&type=evidence", href   # a live origin may carry a path (B1)
    page.goto(urljoin(base, href))
    page.wait_for_selector("#search-results .search-hit")
    assert page.input_value("#global-search + [data-search-type]") == "evidence"
    types = page.evaluate("[...document.querySelectorAll('#search-results .search-hit .meta')].map(e=>e.textContent.split(' · ')[0])")
    assert types and set(types) == {"Evidence record"}, set(types)
    assert page.evaluate("document.querySelectorAll('#search-results .search-see-all').length") == 0   # the directory shows every match
    page.select_option("#global-search + [data-search-type]", "")
    page.wait_for_function("new URLSearchParams(location.search).get('type')===null")
    page.goto(base + "/ar/evidence/?q=remittances&type=evidence")   # the same state in the other edition
    page.wait_for_selector("#search-results .search-hit")
    assert page.get_attribute("#global-search + [data-search-type]", "aria-label") == "نوع النتيجة"


@test("compare: the 'select at least two' prompt shows only while fewer than two records are selected")
def t_compare_prompt(page, base):
    """Release candidate G4 item 6: the governed prompt stands beside the controls and is hidden once a comparison shows."""
    page.goto(base + "/en/evidence/compare/")
    page.wait_for_selector("#compare-output .compare-verdict")
    assert page.evaluate("document.querySelector('[data-compare-prompt]').hidden") is True
    page.goto(base + "/en/evidence/compare/?records=NOT-A-RECORD,ALSO-NOT")   # an input error: no comparison is shown
    page.wait_for_selector("[data-compare-url-error]")
    assert page.evaluate("document.querySelector('[data-compare-prompt]').hidden") is False


@test("citation and print: the copied citation is exactly the visible preview; every page has a print control")
def t_cite_preview(page, base):
    """Part B B9: one citation template, previewed before copying; the canonical address is written into the preview."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"])
    for route in ("/en/people/", "/ar/evidence/CLM-001/"):
        page.goto(base + route)
        preview = page.inner_text("[data-cite-text]").strip()
        assert page.locator("[data-print]").count() >= 1, route
        assert route in preview, preview                       # the canonical address is in the preview
        page.click("section.util [data-cite]")
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
        copied = page.evaluate("navigator.clipboard.readText()")
        assert " ".join(copied.split()) == " ".join(preview.split()), (copied, preview)


@test("search: a query from the URL is rendered as text, never as markup")
def t_search_url_state_is_escaped(page, base):
    page.goto(base + "/en/evidence/?q=" + quote('<img src=x onerror=alert(1)>'))
    page.wait_for_selector("#search-results [data-search-empty], #search-results .search-hit")
    assert page.input_value("#global-search") == '<img src=x onerror=alert(1)>'
    assert page.evaluate("document.querySelectorAll('#search-results img, #search-results script').length") == 0


@test("search: a failed index load is a technical state, announced")
def t_search_failure(page, base):
    page.route("**/static-data/search_index.json", lambda r: r.fulfill(status=503, body="unavailable"))
    page.goto(base + "/en/evidence/")
    page.fill("#global-search", "remittances")
    page.wait_for_selector("#search-results .empty")
    assert "could not be loaded" in page.inner_text("#search-results")
    assert page.query_selector("#search-results .search-hit") is None


@test("search: a Measurement priority result deep-links to its anchor")
def t_measurement_anchor(page, base):
    page.goto(base + "/en/evidence/")
    page.fill("#global-search", "post-transfer persistence")
    page.wait_for_selector("#search-results .search-hit")
    hrefs = page.evaluate("[...document.querySelectorAll('#search-results .search-hit')].map(a=>a.getAttribute('href'))")
    anchored = [h for h in hrefs if "/measurement/#MA-" in h]
    assert anchored, hrefs
    page.goto(urljoin(base, anchored[0]))
    assert page.evaluate(f"!!document.getElementById('{anchored[0].split('#')[1]}')"), "anchor missing on /measurement/"


# ------------------------------------------------------------------------------------------------ Sources, language, records
@test("sources: a deep link opens and focuses its source card")
def t_source_deeplink(page, base):
    page.goto(base + "/en/data/")
    sid = page.evaluate("document.querySelector('[data-source-record]').id.replace('source-','')")
    page.goto(f"{base}/ar/data/?source={sid}#source-{sid}")
    page.wait_for_function(f"document.activeElement && document.activeElement.id==='source-{sid}'")


@test("sources: an unknown source link is an announced technical error, not an empty result")
def t_source_unknown(page, base):
    page.goto(base + "/en/data/?source=SRC-NOT-A-SOURCE")
    st = page.query_selector("[data-source-filter-status]")
    assert st.get_attribute("role") == "alert" and st.get_attribute("data-source-link-error") == "unknown"
    assert page.evaluate("document.querySelectorAll('[data-source-record]:not([hidden])').length") > 0, "all sources should stay visible"


@test("sources: filter no-match is not presented as no evidence")
def t_source_nomatch(page, base):
    page.goto(base + "/en/data/")
    page.fill("[data-source-filter]", "zzqqxxnomatch")
    assert page.is_visible("[data-source-no-results]") and "does not mean" in page.inner_text("[data-source-no-results]")


@test("sources: library filters narrow the list, travel in the URL, and a shared link restores them (B13)")
def t_source_library(page, base):
    for lang in ("en", "ar"):
        page.goto(f"{base}/{lang}/data/")
        assert page.is_visible("[data-source-facets]"), "filters hidden with the runtime running"
        total = page.evaluate("document.querySelectorAll('[data-source-record]:not([hidden])').length")
        year = page.evaluate("[...document.querySelectorAll('[data-source-facet=year] option')].map(o => o.value).find(v => /^\\d{4}$/.test(v))")
        page.select_option("[data-source-facet=year]", year)
        shown = page.evaluate("document.querySelectorAll('[data-source-record]:not([hidden])').length")
        want = page.evaluate(f"document.querySelectorAll('[data-source-record][data-f-year=\"{year}\"]').length")
        assert 0 < shown == want < total, (shown, want, total)
        assert f"year={year}" in page.url, page.url
        page.select_option("[data-source-sort]", "newest")
        assert "sort=newest" in page.url
        shared = page.url
        page.goto(shared)
        assert page.evaluate(f"document.querySelector('[data-source-facet=year]').value") == year
        assert page.evaluate("document.querySelectorAll('[data-source-record]:not([hidden])').length") == want
        page.click("[data-source-facets-clear]")
        assert page.evaluate("document.querySelectorAll('[data-source-record]:not([hidden])').length") == total
        assert "year=" not in page.url


@test("search: numbers with or without separators, Arabic words from their start, governed aliases widen the query (B15)")
def t_search_matching(page, base):
    def hits(lang, q):
        page.goto(f"{base}/{lang}/")
        page.click("[data-search-open]")
        page.fill("[data-search-input]", q)
        page.wait_for_function("document.querySelector('[data-search-status]') && document.querySelector('[data-search-status]').textContent.trim().length > 0")
        page.wait_for_timeout(300)
        return page.evaluate("[...document.querySelectorAll('[data-search-results] a')].map(a => [a.getAttribute('href'), a.textContent])")
    plain, grouped = hits("en", "6245"), hits("en", "6,245")
    assert plain and [h for h, _ in plain] == [h for h, _ in grouped], (plain[:3], grouped[:3])
    assert hits("ar", "٦٬٢٤٥"), "an Arabic-Indic number with its separator finds nothing"
    assert not any("تعزيز" in t for _, t in hits("ar", "تعز")), "a short Arabic word matched inside a longer one"
    assert any("CLM-002" in (h or "") for h, _ in hits("ar", "المرأة")), "the governed alias group did not widen «المرأة»"


@test("language switch keeps route, query and hash")
def t_lang_state(page, base):
    page.goto(base + "/en/measurement/#MA-003")
    page.click("[data-lang]")
    page.wait_for_url("**/ar/measurement/#MA-003")
    page.goto(base + "/ar/data/?source=SRC-WB-FSD-2024-001#source-SRC-WB-FSD-2024-001")
    page.click("[data-lang]")
    page.wait_for_url("**/en/data/?source=SRC-WB-FSD-2024-001#source-SRC-WB-FSD-2024-001")


@test("corrections/contact: the originating record is kept; bad references are technical errors")
def t_record_context(page, base):
    for route in ("/en/corrections/", "/ar/contact/"):
        page.goto(base + route + "?record=CLM-001")
        assert page.is_visible("[data-correction-origin]") and "CLM-001" in page.inner_text("[data-correction-record]")
        assert page.get_attribute("[data-correction-link]", "href").endswith("/evidence/CLM-001/")
    page.goto(base + "/en/corrections/?record=%3Cscript%3E")
    e = page.query_selector("[data-correction-error]")
    assert e.is_visible() and e.get_attribute("data-correction-error") == "malformed" and e.get_attribute("role") == "alert"
    page.goto(base + "/en/contact/?record=CLM-999")
    assert page.get_attribute("[data-correction-error]", "data-correction-error") == "unknown"
    assert not page.is_visible("[data-correction-origin]")


@test("cite: an Evidence Record copies its short citation plus the record link, and its governed long form on request, in both languages")
def t_cite_record(page, base):
    """RC-15 (B15 d, C-2; OWN-04): the short citation (title, record ID, edition, original source and locator) is the
    default; the long form, with the period, population and limits, is the governed citation and copies on its own."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    for lang in ("en", "ar"):
        page.goto(f"{base}/{lang}/evidence/CLM-001/")
        governed = page.evaluate("document.querySelector('meta[name=\"yfie-citation\"]')?.content?.trim()||''")
        short = " ".join(page.inner_text("[data-cite-text]").split())
        page.click(".evidence-cite-button")
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
        text = " ".join(page.evaluate("navigator.clipboard.readText()").split())
        assert text == short and "CLM-001" in text and "/evidence/CLM-001/" in text, (short[:80], text[:80])
        # two lines: this resource with the page address, then the original sources (owner instructions, 3 October 2026, E1)
        lines = page.evaluate("navigator.clipboard.readText()").split("\n")
        assert len(lines) == 2 and "/evidence/CLM-001/" in lines[0] and lines[1].startswith(("Original sources", "المصادر الأصلية")), lines
        assert len(text) < len(governed), "the short citation is not shorter than the long form"
        page.evaluate("navigator.clipboard.writeText('')")
        page.click(".cite-long summary")
        page.click("[data-cite-long]")
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
        long_ = " ".join(page.evaluate("navigator.clipboard.readText()").split())
        assert governed and long_.startswith(" ".join(governed.split())), (governed[:60], long_[:80])
        assert "/evidence/CLM-001/" in long_, long_


@test("share: a record shares its title, period, population and boundary verbatim, with its link (copied where Web Share is absent)")
def t_share_record(page, base):
    """RC-15 (B15 e, U1): without Web Share (a desktop browser) the share text is copied; it carries the governed
    boundary of the record whole and the record's address."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    page.add_init_script("Object.defineProperty(navigator,'share',{value:undefined,configurable:true})")
    for lang in ("en", "ar"):
        page.goto(f"{base}/{lang}/evidence/CLM-002/")
        want = page.get_attribute("[data-share]", "data-share-text")
        page.evaluate("navigator.clipboard.writeText('')")
        page.click("[data-share]")
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
        # The Windows clipboard serializes line breaks as CRLF. Preserve every
        # character except that native newline encoding; do not collapse whitespace.
        text = page.evaluate("navigator.clipboard.readText()").replace("\r\n", "\n")
        assert want and text.startswith(want.strip()), (want[:60], text[:80])
        assert f"/{lang}/evidence/CLM-002/" in text, text


@test("cite: a locator-only source is cited by reference and locator, never with the reference repeated as a title")
def t_cite_source(page, base):
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    page.goto(base + "/en/data/")
    sid = page.evaluate("document.querySelector('.source-locator[data-source-record]').id.replace('source-','')")
    page.goto(f"{base}/en/data/?source={sid}#source-{sid}")   # S1: the group renders closed; the deep link opens it
    btn = page.query_selector(f"#source-{sid} [data-source-cite]")
    btn.scroll_into_view_if_needed(); btn.click()
    page.wait_for_function("document.querySelector('#utility-status').textContent.length>0")
    parts = page.evaluate("navigator.clipboard.readText()").split(" · ")
    assert len(parts) == len(set(parts)) and parts[-1].startswith("http"), parts


# ------------------------------------------------------------------------------------------------ Accessibility baseline (P2.4)
# RC-DATES (owner request, after RC-5): what the runtime writes into an Arabic page — search results, the Compare table,
# its boundaries and source lists — isolates every date, range and identifier left to right, as the rendered page does.
_UNISOLATED_JS = r"""() => { const re=/\d[-\u2010\u2011\u2013\u2212]\d/, out=[];
  const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); let n;
  while((n=w.nextNode())){ const p=n.parentElement; if(!p||p.closest('script,style,svg')||!re.test(n.data)) continue;
    const i=p.closest('[dir="ltr"]'); if(i&&i!==document.documentElement) continue; out.push(n.data.trim().slice(0,90)); }
  return out; }"""


@test("bidi: Arabic search results and Compare print every date, range and identifier isolated")
def t_ar_runtime_isolation(page, base):
    seen = []
    for q in ("2022", "2024", "2026"):
        page.goto(base + "/ar/evidence/?q=" + q)
        page.wait_for_selector(".search-hit", timeout=5000)
        seen += page.evaluate(_UNISOLATED_JS)
    for recs in ("CLM-001,CLM-010,CLM-032", "CLM-033,CLM-035,CLM-037", "CLM-054,CLM-056,FMIIP-BASELINE-2025-01"):
        page.goto(base + "/ar/evidence/compare/?records=" + recs)
        page.wait_for_selector("[data-compare-verdict]", timeout=5000)
        seen += page.evaluate(_UNISOLATED_JS)
    assert not seen, f"{len(seen)} un-isolated runs, e.g. {seen[0]!r}"


@test("a11y: skip link is first in tab order and moves focus into main")
def t_skip(page, base):
    page.goto(base + "/ar/people/")
    page.keyboard.press("Tab")
    assert page.evaluate("document.activeElement.classList.contains('skip')")
    page.keyboard.press("Enter")
    assert page.evaluate("location.hash") == "#main" and page.query_selector("#main")


@test("a11y: mobile menu toggles aria-expanded; Escape closes it and returns focus")
def t_menu(page, base):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(base + "/en/")
    page.click("[data-menu]")
    assert page.get_attribute("[data-menu]", "aria-expanded") == "true"
    page.keyboard.press("Escape")
    assert page.get_attribute("[data-menu]", "aria-expanded") == "false"
    page.focus("[data-menu]"); page.keyboard.press(" ")   # ported (Mohammed Waleed): Space opens the menu like Enter
    assert page.get_attribute("[data-menu]", "aria-expanded") == "true"
    page.keyboard.press("Escape")


@test("a11y: the opened menu's language link keeps a Compare selection (query and anchor) across the switch")
def t_menu_lang_keeps_query(page, base):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(base + "/en/evidence/compare/?records=CLM-001,CLM-003#verdict")
    page.click("[data-menu]")
    page.click("[data-menu-lang]")
    page.wait_for_url("**/ar/evidence/compare/?records=CLM-001,CLM-003#verdict")
    assert page.evaluate("document.documentElement.lang") == "ar"   # the other edition, same selection and anchor (item 11)
    assert page.get_attribute("[data-menu]", "aria-expanded") == "false"   # a fresh page: the menu starts closed


def tab_to(page, selector: str, limit: int = 900) -> bool:
    """Press Tab until the focused element matches `selector` (B10 c: every tool is reached from the keyboard)."""
    for _ in range(limit):
        page.keyboard.press("Tab")
        if page.evaluate("(s) => !!document.activeElement && document.activeElement.matches(s)", selector):
            return True
    return False


@test("a11y: keyboard walk — search, language switch, print, cite, source filter and Compare are reached by Tab and work from the keyboard")
def t_keyboard_walk(page, base):
    for lang in ("en", "ar"):
        page.goto(f"{base}/{lang}/people/")
        assert tab_to(page, "[data-search-open]"), "search opener not reached"
        page.keyboard.press("Enter")
        page.wait_for_function("document.activeElement && document.activeElement.matches('[data-search-input]')")
        page.keyboard.press("Escape")
        page.goto(f"{base}/{lang}/people/")
        assert tab_to(page, "[data-lang]"), "language switch not reached"
        for sel in ("[data-print]", "[data-cite]"):
            page.goto(f"{base}/{lang}/evidence/CLM-001/")
            assert tab_to(page, sel), f"{sel} not reached"
            assert page.evaluate("(s) => { const e = document.activeElement; return (e.getAttribute('aria-label') || e.textContent).trim().length > 0 }", sel)
        page.goto(f"{base}/{lang}/data/")
        assert tab_to(page, "[data-source-filter]"), "source filter not reached"
        page.keyboard.type("CBY")
        page.wait_for_function("document.querySelector('[data-source-filter-status]').textContent.trim().length > 0")
        page.goto(f"{base}/{lang}/evidence/compare/?records=CLM-001,CLM-054")
        before = page.evaluate("new URLSearchParams(location.search).get('records')")
        assert tab_to(page, "#compare-b"), "Compare selector not reached"
        page.keyboard.press("ArrowDown")
        page.wait_for_function("(b) => new URLSearchParams(location.search).get('records') !== b", arg=before)


@test("a11y: technical-error and status regions are announced (role/aria-live)")
def t_announce(page, base):
    page.goto(base + "/en/evidence/compare/?records=CLM-001,CLM-054,CLM-010,CLM-041,CLM-042")
    assert page.get_attribute("[data-compare-url-error]", "role") == "alert"
    page.goto(base + "/en/evidence/")
    assert page.evaluate("document.querySelector('#search-results').getAttribute('aria-live')") == "polite"
    assert page.get_attribute("#utility-status", "role") == "status"


# ------------------------------------------------------------------------------------------------ B2 T (BRIEF W4 T; OD-1017-04(a)): the tools
@test("report: a record's link opens the form pre-filled; a valid report prepares a fixed-format e-mail under a reference code; the invalid states are caught")
def t_report_form(page, base):
    """BRIEF W4 T (report an error): every record carries 'Report an error' → /contact/?record=ID#report; the form
    pre-fills page, record, language and edition; a valid report becomes a mailto whose body is the fixed key: value
    list under YFIE-ERR-<record>-<yyyymmdd-hhmm>; the copy action copies the same body. Negative controls: an empty
    form, an invalid address and an unknown record never produce a report."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    keys = ["Reference", "Page", "Record", "Section", "Language", "Edition", "Error type", "In question", "Should say", "Evidence", "Name", "Reply to"]
    for lang in ("en", "ar"):
        page.goto(f"{base}/{lang}/evidence/CLM-010/")
        href = page.get_attribute("[data-page-tools] [data-report-link]", "href")
        assert href.endswith("?record=CLM-010#report"), href
        page.goto(urljoin(base, href))
        page.wait_for_selector("[data-report]")
        assert page.input_value('[data-rf="record"]') == "CLM-010"
        assert page.input_value('[data-rf="url"]').endswith(f"/{lang}/evidence/CLM-010/"), page.input_value('[data-rf="url"]')
        assert page.input_value('[data-rf="lang"]') == lang and page.input_value('[data-rf="edition"]') != ""
        assert page.evaluate("document.querySelector('[data-report-nojs]').hidden") is True
        assert "CLM-010" in page.inner_text("[data-correction-record]")
    # negative control 1: an empty form reports its missing fields and prepares nothing
    page.evaluate("document.querySelector('[data-report]').dataset.noMail='1'")
    page.click("[data-report-send]")
    errs = page.inner_text("[data-report-errors]")
    assert page.is_visible("[data-report-errors]") and "2" in errs, errs
    assert page.evaluate("document.querySelector('[data-report]').dataset.mailto") is None
    assert page.evaluate("document.activeElement.getAttribute('data-rf')") == "value"
    # negative control 2: an invalid reply address
    page.fill('[data-rf="value"]', "11.9%")
    page.select_option('[data-rf="type"]', "number")
    page.fill('[data-rf="email"]', "not-an-address")
    page.click("[data-report-send]")
    assert page.is_visible('[data-rf-err="email"]') and page.evaluate("document.querySelector('[data-report]').dataset.mailto") is None
    # a valid report
    page.fill('[data-rf="email"]', "reader@example.org")
    page.fill('[data-rf="should"]', "11.8%")
    page.click("[data-report-send]")
    page.wait_for_function("!!document.querySelector('[data-report]').dataset.mailto")
    mailto = page.evaluate("document.querySelector('[data-report]').dataset.mailto")
    address = page.get_attribute("[data-report]", "data-address")
    assert mailto.startswith(f"mailto:{address}?subject=") and "&body=" in mailto, mailto[:90]
    subject = unquote(mailto.split("subject=", 1)[1].split("&body=", 1)[0])
    body = unquote(mailto.split("&body=", 1)[1])
    lines = body.split("\n")
    assert [l.split(":", 1)[0] for l in lines] == keys, lines
    ref = lines[0].split(": ", 1)[1]
    assert re.fullmatch(r"YFIE-ERR-CLM-010-\d{8}-\d{4}", ref), ref
    assert ref in subject and subject.startswith(page.get_attribute("[data-report]", "data-product") + " — "), subject
    assert "Record: CLM-010" in lines and "Error type: number" in lines and "In question: 11.9%" in lines and "Should say: 11.8%" in lines and "Reply to: reader@example.org" in lines and "Language: ar" in lines, lines
    assert page.inner_text("[data-report-ref-code]").strip() == ref
    assert ref in page.inner_text("[data-report-status]")
    # the copy action copies the same body
    page.evaluate("navigator.clipboard.writeText('')")
    page.click("[data-report-copy]")
    page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
    assert page.evaluate("navigator.clipboard.readText()").replace("\r\n", "\n") == body
    # negative control 3: an unknown record is a link error, not a pre-filled report
    page.goto(base + "/en/contact/?record=CLM-999#report")
    page.wait_for_selector("[data-report]")
    assert page.input_value('[data-rf="record"]') == "" and page.is_visible("[data-correction-error]")
    # a figure's link carries its record and figure
    page.goto(base + "/en/people/")
    fig = page.get_attribute("figure .report-l[data-report-link]", "href")
    assert re.search(r"/en/contact/\?record=VIS-[A-Z0-9-]+&figure=VIS-[A-Z0-9-]+#report$", fig), fig
    page.goto(urljoin(base, fig))
    page.wait_for_selector("[data-report]")
    vid = re.search(r"record=([^&]+)", fig).group(1)
    assert page.input_value('[data-rf="record"]') == vid and page.input_value('[data-rf="anchor"]') == vid
    # without a record, the form still opens from any page (the util link) and the no-JS mailto carries the field list
    page.goto(base + "/en/methodology/")
    href = page.get_attribute("#cite-tools [data-report-link]", "href")
    assert href.endswith("/en/contact/#report"), href
    page.goto(base + "/en/contact/")
    page.wait_for_selector("[data-report]")
    nojs = page.get_attribute("[data-report-nojs] a[data-correction-mail]", "href")
    assert nojs.startswith(f"mailto:{address}?subject=") and all(k + ":" in unquote(nojs) for k in keys), nojs[:120]


@test("cite: APA 7, Chicago, BibTeX and RIS carry the record ID, the edition and the access date; BibTeX and RIS parse")
def t_cite_formats(page, base):
    """OD-1017-04(a): the format control renders the citation from the page's governed metadata; the copy action copies
    exactly the rendered text; a parser accepts the BibTeX and the RIS and rejects a broken one."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    bib_rx = re.compile(r"@misc\{([A-Za-z0-9_]+),\n((?:  [a-z]+ = \{[^\n]*\},?\n)+)\}")
    page.goto(base + "/en/evidence/CLM-001/")
    edition = page.evaluate("document.querySelector('meta[name=\"yfie-edition\"]').content")
    assert edition
    for fmt in ("apa", "chicago", "bibtex", "ris"):
        page.select_option("[data-cite-format]", fmt)
        out = page.inner_text("[data-cite-out]")
        assert "CLM-001" in out and edition in out and "/en/evidence/CLM-001/" in out, (fmt, out[:160])
        page.evaluate("navigator.clipboard.writeText('')")
        page.click("section.util [data-cite]")
        page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
        copied = page.evaluate("navigator.clipboard.readText()").replace("\r\n", "\n")
        assert copied.strip() == out.strip(), (fmt, copied[:100], out[:100])
        if fmt == "bibtex":
            m = bib_rx.fullmatch(copied.strip())
            assert m, copied[:200]
            fields = dict(re.findall(r"  ([a-z]+) = \{([^\n]*)\},?\n", m.group(2)))
            assert {"author", "title", "howpublished", "note", "year", "url"} <= set(fields), sorted(fields)
            assert fields["year"].isdigit() and re.search(r"Accessed \d{4}-\d{2}-\d{2}", fields["note"]) and "CLM-001" in fields["howpublished"], fields
        if fmt == "ris":
            lines = copied.strip("\r\n").split("\n")   # "ER  - " keeps its trailing space
            assert all(re.fullmatch(r"[A-Z][A-Z0-9]  - ?.*", l) for l in lines), lines
            tags = [l[:2] for l in lines]
            assert tags[0] == "TY" and tags[-1] == "ER" and {"AU", "TI", "T2", "PY", "ET", "ID", "UR", "Y2"} <= set(tags), tags
            ris = {l[:2]: l[6:] for l in lines}
            assert ris["ID"] == "CLM-001" and re.fullmatch(r"\d{4}/\d{2}/\d{2}", ris["Y2"]) and ris["PY"].isdigit(), ris
        if fmt == "apa":
            assert re.search(r"\(\d{4}\)\. .*\(Evidence Record CLM-001\) \[Evidence record\]\. .*Retrieved \w+ \d{1,2}, \d{4}, from ", out), out
    page.select_option("[data-cite-format]", "plain")
    assert page.evaluate("document.querySelector('[data-cite-out]').hidden") is True
    # negative controls for the parsers: a keyless BibTeX and a RIS without its end tag are rejected
    assert not bib_rx.fullmatch("@misc{,\n  title = {x},\n}")
    assert [l[:2] for l in ["TY  - ELEC", "TI  - x"]][-1] != "ER"
    # the Arabic edition: the Arabic access phrase, Latin digits, the same machine formats
    page.goto(base + "/ar/evidence/CLM-001/")
    page.select_option("[data-cite-format]", "chicago")
    out = page.inner_text("[data-cite-out]")
    assert "تاريخ الاطلاع" in out and "CLM-001" in out and not re.search(r"[٠-٩]", out), out[:160]
    page.select_option("[data-cite-format]", "ris")
    assert page.inner_text("[data-cite-out]").startswith("TY  - ELEC\nAU  - CauseWay\n")
    # a page without a record cites as a page
    page.goto(base + "/en/methodology/")
    page.select_option("[data-cite-format]", "apa")
    out = page.inner_text("[data-cite-out]")
    assert "[Web page]" in out and "Evidence Record" not in out, out[:160]


@test("compare: the verdict carries a one-sentence reason naming the dimension behind it; the summary copies with the verdict")
def t_compare_reason(page, base):
    """SIG-5 / BRIEF W4 T (Compare): each controlled verdict has its one reason, in the governed field words; the copied
    summary carries the verdict, the reason, each record's scope and the comparison link; an input error disables it."""
    page.context.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    page.goto(base + "/en/evidence/compare/")
    page.wait_for_selector("[data-compare-reason]")
    v = verdict(page)
    reason = page.inner_text("[data-compare-reason]").strip()
    starts = {"not-direct": "Differs between these records:", "qualified": "Differs between these records:", "unresolved": "Not recorded on at least one record:",
              "aligned": "Definition, population, method, period and currentness match", "same-record": "The same record is selected"}
    assert reason.startswith(starts[v]), (v, reason)
    assert page.evaluate("document.querySelector('[data-compare-summary]').disabled") is False
    page.click("[data-compare-summary]")
    page.wait_for_function("navigator.clipboard.readText().then(t=>t.length>0)")
    text = page.evaluate("navigator.clipboard.readText()").replace("\r\n", "\n")
    title = page.inner_text("[data-compare-verdict] h3").strip()
    lines = text.split("\n")
    assert lines[0] == "Comparison of 2 records" and lines[1] == f"{title}. {reason}", lines[:2]
    assert sum(1 for l in lines if l.startswith("— ")) == 2 and "?records=" in lines[-1], lines
    ids = page.evaluate("[...document.querySelectorAll('#compare-a option')].map(o=>o.value).filter(Boolean)")
    page.goto(f"{base}/en/evidence/compare/?records={ids[0]},{ids[0]}")
    page.wait_for_selector("[data-compare-reason]")
    assert page.inner_text("[data-compare-reason]").strip() == "The same record is selected more than once."
    page.goto(base + "/en/evidence/compare/?records=NOT-A-RECORD,ALSO-NOT")
    page.wait_for_selector("[data-compare-url-error]")
    assert page.evaluate("document.querySelector('[data-compare-summary]').disabled") is True
    page.goto(base + "/ar/evidence/compare/")
    page.wait_for_selector("[data-compare-reason]")
    assert page.inner_text("[data-compare-reason]").strip().endswith(".") and re.search(r"[؀-ۿ]", page.inner_text("[data-compare-reason]"))


@test("search: an unanswerable query offers the questions hub and the same query in the other edition, and no false hit")
def t_search_zero_help(page, base):
    """BRIEF W4 T (Search, zero-result help): the empty state links the Questions hub and the other edition's directory
    with the query; a near-miss offers the alias term it resembles; nonsense never produces a hit."""
    page.goto(base + "/en/evidence/?q=" + quote("zxqv quantum"))
    page.wait_for_selector("#search-results [data-search-empty]")
    assert page.query_selector("#search-results .search-hit") is None
    other = page.get_attribute("[data-search-other-edition]", "href")
    assert other == urlsplit(base).path + "/ar/evidence/?q=zxqv%20quantum" and page.get_attribute("[data-search-other-edition]", "hreflang") == "ar", other
    assert page.get_attribute("[data-search-help] a", "href").endswith("/en/explore/")
    page.goto(urljoin(base, other))
    page.wait_for_selector("#search-results [data-search-empty]")
    assert page.get_attribute("[data-search-other-edition]", "hreflang") == "en" and page.get_attribute("[data-search-other-edition]", "href").endswith("/en/evidence/?q=zxqv%20quantum")
    page.goto(base + "/en/evidence/?q=lawyers")
    page.wait_for_selector("#search-results .search-hit, #search-results [data-search-empty]")
    if page.query_selector("#search-results [data-search-empty]"):
        tries = page.evaluate("[...document.querySelectorAll('[data-search-suggest]')].map(a=>a.textContent)")
        assert "law" in tries, tries


@test("sources: facet options carry live counts that follow the term and the other facets")
def t_source_facet_counts(page, base):
    """BRIEF W4 T (source directory): each option says how many sources it would leave; the counts move with the other
    facets and return after Clear all."""
    page.goto(base + "/en/data/")
    page.wait_for_selector("[data-source-facets]:not([hidden])")
    read = "[...document.querySelector('[data-source-facet=\"publisher\"]').options].filter(o=>o.value).map(o=>o.textContent)"
    first = page.evaluate(read)
    assert first and all(re.search(r"\((\d+)\)$", t) for t in first), first[:3]
    total = sum(int(re.search(r"\((\d+)\)$", t).group(1)) for t in first)
    shown = int(re.search(r"\d+", page.inner_text("[data-source-filter-status]")).group(0))
    assert total == shown, (total, shown)
    page.select_option('[data-source-facet="type"]', index=1)
    after = page.evaluate(read)
    assert after != first and sum(int(re.search(r"\((\d+)\)$", t).group(1)) for t in after) < total, after[:3]
    page.click("[data-source-facets-clear]")
    assert page.evaluate(read) == first



def main():
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("HARNESS UNAVAILABLE: python playwright not installed"); sys.exit(2)
    if not os.path.exists(os.path.join(DIST, "en", "index.html")):
        print(f"site not built: {DIST} has no index.html (run scripts/build.py, or set YFIE_SITE_DIR to your built site)"); sys.exit(2)
    # the release runbook (step 10) runs the same tests against the live host: YFIE_BASE_URL=https://<domain>
    live = os.environ.get("YFIE_BASE_URL", "").rstrip("/")
    httpd, base = (None, live) if live else serve()
    tests = [v for v in globals().values() if callable(v) and hasattr(v, "__test_name__")]
    only = os.environ.get("YFIE_TOOL_TESTS")   # B2 T: run the tests whose name contains this text (development aid)
    tests = [t for t in tests if not only or only in t.__test_name__]
    failed = 0
    with sync_playwright() as pw:
        exe = os.environ.get("YFIE_CHROMIUM")
        browser = pw.chromium.launch(**({"executable_path": exe} if exe else {}))
        for t in tests:
            # A live host sends the strict policy (script-src 'self'), which forbids the evaluated predicates these tests
            # wait on; the policy itself is test_security_headers.py's, so the tools are tested here with it bypassed.
            ctx = browser.new_context(**({"bypass_csp": True} if live else {}))
            page = ctx.new_page()
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            try:
                note = t(page, base)
                if errors:
                    raise AssertionError("JavaScript error: " + errors[0])
                RESULTS.append(("SKIP" if str(note or "").startswith("SKIP") else "PASS", t.__test_name__, note or ""))
            except Exception as e:
                failed += 1
                RESULTS.append(("FAIL", t.__test_name__, (str(e) or traceback.format_exc().splitlines()[-1])[:300]))
            finally:
                ctx.close()
        browser.close()
    if httpd:
        httpd.shutdown()
    for r in RESULTS:
        print(" | ".join(r))
    skipped = sum(1 for r in RESULTS if r[0] == "SKIP")
    print(f"PUBLIC TOOL TESTS {'PASS' if not failed else 'FAIL'}: {len(RESULTS) - failed - skipped}/{len(RESULTS)} passed, {skipped} not applicable to the current data")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
