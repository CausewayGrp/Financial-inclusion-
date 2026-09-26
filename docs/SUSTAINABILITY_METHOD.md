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

## What the pre-design baseline shows

- The canonical master logo (a 10 MB PNG) is about 96–99 % of every cold page. It is never redrawn, regenerated,
  recoloured or cropped in this repository; owner-approved web-size derivatives are release-only engineering (TOOL-02).
- Without the logo a cold page is about 0.09–0.45 MB in four requests (HTML, one stylesheet, one script).
- The search index (about 2 MB, about 0.3 MB with gzip) loads only when Search is opened.
- A warm page load transfers nothing: every file comes from the browser cache.
