# Digital sustainability — method

Stewardship, not marketing. The evidence product comes first: accessibility, Arabic quality, security and evidence
integrity outrank marginal savings in bytes or energy, and nothing in this method may shorten, simplify or remove
evidence, boundaries or text alternatives to make a page lighter.

## What is measured

| Item | Definition |
|---|---|
| Transferred bytes | Bytes received on the wire per page load (Chrome DevTools Protocol `encodedDataLength`), by resource type: HTML, JavaScript, CSS, images, fonts, data |
| Requests | Number of network requests per page load |
| Cache state | **Cold:** new browser context, empty cache. **Warm:** the same page opened again in the same context |
| Route class | One representative page per class, in each language: Home, Explore, domain answer, Evidence index, Evidence Record, Compare, sources directory, Readings index, Reading, Methodology, Measurement Agenda, About/trust |
| Interaction | Opening Search and typing a query (loads the local search index once) |
| Modelled compression | The same responses compressed with gzip level 6, as a typical static host would send them — a model, labelled as such |

Tooling: `audit/final_integration/f7_measure_baseline.py` (headless Chromium via Playwright, local static server).
Record: [`audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`](../audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json) — method,
tool versions, date, commit, system boundary, viewport, hosting assumption, results and uncertainty.

## System boundary

Browser to a local static server. Excluded: network hops, CDN, data centre, the reader's device energy and embodied
emissions. There are no third parties to include: the site loads no web font, analytics, tracker or CDN resource (gate
F6-G05).

## What is deliberately not done

- **No carbon figure before Design.** Converting bytes to energy and emissions needs a model (for example the Sustainable
  Web Design model) and assumptions about the host, the grid and the reader's device. The final pages, images, scripts,
  caching and host will change every input, so a pre-design estimate would be neither stable nor useful.
- **No budget file yet.** A performance or byte budget is set only against a real baseline of the designed site; the
  pre-design reference build is not that baseline.
- **No badge, rating or comparison** with other sites, and no "green", "low-carbon" or similar claim anywhere in the
  product.

## When and how to remeasure

1. After Design, on the designed reference pages, with the same script and route classes.
2. After Code and deployment, on the release host, with compression and caching as served: record the host, region,
   HTTP version and cache headers. Only then may a carbon estimate be added, with the model name and version, every
   assumption and the uncertainty stated.
3. At each release that changes images, scripts, fonts or the search index.

## What the implemented runtime shows (EAD-10, 29 September 2026)

Measured with the same script and the same twelve route classes, so the two records compare like with like:
[`docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`](SUSTAINABILITY_IMPLEMENTED_RUNTIME.json).

| | Pre-design baseline | Implemented runtime |
|---|---|---|
| Cold page, transferred | 9.64–9.99 MB | 9.83–10.19 MB |
| Cold page requests | 4 | 7 |
| Cold page without the logo | 84–444 KB | 285–656 KB |
| — HTML | 14–374 KB | 17–362 KB |
| — CSS | 47 KB | 50 KB |
| — JavaScript | 23 KB | 25 KB |
| — Fonts | 0 KB | 193–220 KB |
| Warm page, transferred | 0 | 0 |
| Search interaction | 1,976,885 B (gzip ~321 KB) | unchanged |

- **The logo is still the page**: 94–97 % of every cold load is the master logo — 10,018,081 bytes on disk, 10,018,273
  bytes on the wire with the response headers (corrected 2 October 2026, release candidate G5). That is now measured on the
  implemented site, which is what EAD-03 was waiting for; the derivatives need the owner's approval. **Done 2 October
  2026** (owner decision EAD-03): every surface serves pure resamples of the unchanged master and cold pages fell from
  10.31–10.71 MB to 0.30–0.69 MB (`audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md`).
- **The whole increase is type.** The baseline named IBM Plex but shipped no font file, so a reader without it installed
  read the product in a fallback face — Arial, or Tahoma for Arabic. The runtime self-hosts the six faces the
  stylesheet declares and preloads the two a first paint needs in the page's language (EAD-08). About 200 KB and three
  requests on a cold page, nothing on a warm one, and the product is legible as designed in both scripts.
- **The social images cost a page nothing** (EAD-09): a platform fetches one when a link is shared; the page never does.
- **Still no external request of any kind** — no CDN, no font service, no analytics, no tracker (gate F6-G05).

This is not the operational footprint. The release host is not chosen (OWN-03), so its compression and caching are
unmeasured, **no budget is set and no carbon figure is computed**. Step 2 below is still open.

## What the pre-design baseline shows

- The canonical master logo (a 10 MB PNG) is about 96–99 % of every cold page. It is never redrawn, regenerated,
  recoloured or cropped in this repository; owner-approved web-size derivatives are release-only engineering (TOOL-02).
- Without the logo a cold page is about 0.09–0.45 MB in four requests (HTML, one stylesheet, one script).
- The search index (about 2 MB, about 0.3 MB with gzip) loads only when Search is opened.
- A warm page load transfers nothing: every file comes from the browser cache.
