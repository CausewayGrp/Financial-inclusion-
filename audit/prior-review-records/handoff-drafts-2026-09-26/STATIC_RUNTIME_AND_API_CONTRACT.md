# Static Runtime + Future API Contract

## First complete build

The public product is static-first and locally complete. Core use must work without Google Drive, a database, CMS, server-side rendering service or external API.

### Must be local in the production build

- all controlled public copy in Arabic and English;
- all data required by public views;
- evidence objects, claims and passports used by the site;
- source/citation metadata and public source locators;
- search index;
- governed visual data and accessible fallbacks;
- CauseWay brand assets;
- final webfont assets required for correct typography.

The Production Master itself remains in `authority/` for governance and reproducibility but is **never shipped in public `dist/`** and is not parsed by the browser.

## Runtime network rule

Core rendering and navigation must make zero required external requests. External publisher URLs are links the user may choose to follow. Analytics, issue submission and future live data are optional adapters and must fail safely without damaging the evidence experience.

## Adapter seams for later setup

Implement explicit interfaces with local defaults:

- `ContentRepository` — default: local controlled JSON. Future remote provider must validate schema, authority version and publication state before use.
- `SearchProvider` — default: local `search_index.json`.
- `IssueReporter` — default: static correction/contact path. Future API may submit issues but must not alter evidence directly.
- `AnalyticsProvider` — disabled/no-op by default; future implementation must satisfy privacy and consent decisions.
- `RemoteDataProvider` — absent by default. A future feed may update only through a controlled ingestion/adjudication path; it cannot silently supersede local authority.

## React target

The final presentation implementation should be one React static-pre-render/export application. Prefer a build approach that emits real deep-link-safe HTML for every controlled route and locale. Preserve the accepted baseline of two localized route documents per controlled Page Spec plus root and 404 (286 + 2 = 288 at the time of writing) unless the controlled route set itself changes through authority.

A migration from the current Python static renderer is allowed only as an in-place replacement with parity verification. Remove obsolete presentation code after the React implementation passes the required acceptance suite; do not maintain two production runtimes.

## Font requirement

The current baseline references Google Fonts. The final build must self-host/package the final typography so correct rendering does not require a CDN. Do not expose or distribute font files outside the website build artifacts.

## API activation gate

No future API becomes authoritative merely because it is technically connected. Before activation, document endpoint, publisher, schema, cadence, rights, transformation, failure behavior, cache policy, evidence mapping and Master integration rule.

## R6 interaction-state contract

The first complete public product is not a screenshot export. It is a **fully functioning static application**.

### State that must remain local and deterministic

- Search reads only the packaged public search index.
- Evidence filters read only packaged governed payloads.
- Compare accepts 2–4 public Evidence Record IDs and derives display differences from controlled fields only.
- Source/resource filters read only the packaged source map/library.
- Language switching preserves the same route/object plus query/hash state.
- Citation reads governed citation text where present and appends the canonical public route.
- Correction links may carry the originating route, Evidence Record ID or source ID, but never mutate evidence.

Use URL query state for shareable comparison/filter states where practical. Reloading a deep link must reproduce the same public state without an API call.

### Technical absence is not evidence absence

A failed local asset, malformed URL state or optional adapter must render a **technical error/unavailable state**. It must never be presented as “no evidence”, “zero”, “no provider”, “no access”, or any other substantive conclusion.

### Offline/low-dependency expectation

After the static bundle is loaded, a user must be able to navigate the site, search, inspect evidence, compare records, filter sources, switch language and copy citations without a required network round-trip. Outbound source links are user-initiated navigation, not runtime dependencies.

