# Engineering handoff expectations

What Claude Code must deliver after the Design package is accepted, and the runtime rules the design must already
respect. It makes the semantic and behavioural requirements unambiguous; it does not make Code's engineering choices for
it. The deployment contract (discovery, headers, privacy) is `docs/DEPLOYMENT.md`.

## 1. One authority, one content path, one runtime

- The Production Master stays the only authority; `scripts/generate_projections.py` stays the only way content reaches
  `site-src/content/**`. Code never edits projections, never adds a second content model, CMS or database, and never
  hard-codes copy in components: every interface word is a governed `UI-*` label.
- One production runtime at the end. The target is a static pre-rendered site (React static export or an equivalent
  generator) that emits real, deep-link-safe HTML for every controlled route and language — two documents per Page Spec
  plus the root entry route and the bilingual 404 (the count follows `page_specs.json`). A migration from
  `scripts/build.py` is done in place with parity checks, and the replaced renderer is removed once the new one passes
  every gate. Never leave two production renderers.
- The Master is never shipped in the public output and never parsed by the browser.

## 2. Local-first runtime

- Core use makes zero required external requests: all copy, data, search index, visual data, fonts and brand assets are
  local. Outbound links to original sources are navigation, not dependencies.
- Adapter seams with local defaults, so later services cannot become a second authority: `ContentRepository` (local
  JSON), `SearchProvider` (local index), `IssueReporter` (static correction and contact path), `AnalyticsProvider`
  (disabled — no-op), `RemoteDataProvider` (absent). A future API may feed the same controlled schemas only through a
  documented ingestion and adjudication path.
- A failed local asset, malformed URL state or optional adapter renders a technical state — never "no evidence", "zero",
  "no provider" or any other substantive conclusion.
- Tool state that matters (Compare records, filters, search query) is URL-addressable, reloadable and survives a language
  switch where the object exists.

## 3. Behaviour that must survive the rewrite

Everything tested today must still pass against the new runtime, unmodified in intent:

- `scripts/tests/test_public_tools.py` — Search, Compare, Cite, menu, skip link, live regions, source deep links, record
  context, language state;
- `audit/tranche_c/checks/viewport_acceptance.py` — 320, 390, 640, 1440 px in both languages;
- `scripts/validate.py` — every repository gate, including F6-G01…G08 (discovery, strict-CSP-compatible output, secrets,
  bundled documents, rights) and R86-G01…G04 (handoff state);
- `audit/tranche_c/checks/bilingual_invariance.py` — 0 differing page pairs;
- `scripts/audit_public_literals.py` — every public number traced;
- the canonical search probe (`scripts/search_canonical_probe.json`).

The suites and the invariance check take the site directory from `YFIE_SITE_DIR` (default `dist`). They find elements
by the hooks listed in the Design brief §19 (IDs, `data-*` attributes, classes, JSON block IDs); keep them. Where a test
hard-codes the baseline's markup, adapt the selector, never the assertion. Gate P3-G02 ("the static baseline draws no
chart") protects the pre-design baseline only: when the production runtime draws governed visuals, replace it with a gate
that checks each drawn visual against its contract (tier, rows, labels, markers, fallback) — never simply delete it.

## 4. Discovery

Keep the contract in `scripts/discovery.py` (or port it exactly): unique native titles and descriptions; one `<h1>`;
self-canonical; reciprocal `hreflang` with `x-default` → `/`; robots and sitemap driven by `site-src/deployment.json`;
Open Graph from the governed title and description; JSON-LD `WebSite`, `BreadcrumbList`, `Article` with governed fields
only. Add `og:image` only when the Design social-image templates are generated at build time with governed text. When
the owner sets `public_origin`, every URL becomes absolute and the sitemap is written — nothing else changes.

## 5. Security, privacy, performance

- Serve the headers in `docs/DEPLOYMENT.md` (strict CSP, HSTS, nosniff, referrer and permissions policies). The output
  must stay compatible: no inline executable script, inline style, inline handler, external resource or form; page data
  in `<script type="application/json">` blocks; escaped rendering or Trusted Types.
- No analytics, tracking, cookies or accounts. Adding any needs an owner decision, bilingual Privacy page updates and,
  where required, consent — before it ships.
- Fonts: IBM Plex Sans and IBM Plex Sans Arabic self-hosted from `vendor/fonts/` (unchanged files of `@ibm/plex-sans@1.1.0`
  and `@ibm/plex-sans-arabic@1.1.0`, OFL-1.1, licence shipped); load them efficiently — only the weights the design uses,
  the critical faces preloaded, `font-display` chosen deliberately, IBM's own pre-split Latin subsets where they help; no
  font CDN. The licence reserves the name "Plex": a self-made subset is an owner decision, never a default
  (`vendor/fonts/README.md`).
- Print and portable evidence: ship the Design package's print stylesheets and Reading print layout; generate chart and
  table export frames at build time from governed data only, with the full detached frame; keep every CauseWay-content
  download and export disabled until the owner's licence decision (OWN-04); never offer a third-party document.
- Reporting stays static: the mail action to the governed address with the record reference; any richer reporting
  intent is client-side composition only — no backend, form element, new address or service level.
- Dates: the governed form (day, month name, year; Western digits) with the governed Arabic month names used by
  `date_words` in `scripts/yfie/content.py` (`MONTHS`) — not a locale library's month names, which vary by region.
- Logo: produce web-size derivatives of `site-src/assets/CauseWay_Master_Logo.png` at the sizes in
  `design/08_ASSET_MAP.md` only with the owner's approval (open item EAD-03), by exact downscaling of the unmodified
  master — never redrawn, recoloured, cropped or regenerated. Keep the master file unchanged.
- Remeasure page weight with `docs/SUSTAINABILITY_METHOD.md` after implementation and after deployment; set budgets only
  then; make no green claim.
- Fingerprint asset names before long cache lifetimes; HTML short-cached.

## 6. Accessibility

Implement the outcomes in `audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md` §3 and the Design package's
`design/07_INTERACTION_ACCESSIBILITY.md`. Before any conformance statement: an audit of the implemented site against
WCAG 2.2 (automated plus manual, keyboard, screen readers in Arabic and English, zoom, forced colours). Until then the
Accessibility page keeps saying the resource is designed against WCAG 2.2 and still to be tested.

## 7. Release (not part of the Design handoff)

Release needs, at minimum, the items classed RELEASE_ONLY and OWNER_INPUT in `FINAL_OPEN_ITEMS_REGISTER.md` (public
origin, contact-mailbox confirmation, CauseWay identity and funding statement, content licence, source reuse rights,
security headers at the host), the logo derivatives (EAD-03), the post-implementation accessibility audit (EAD-02), and a
named release acceptance (REL-04). Nothing in this repository declares public
release readiness.

## 8. Working protocol

Branches `code/<slug>`, pull requests to `main`, Verify green before merge, Conventional Commits, manifest and checksums
regenerated per commit (`CONTRIBUTING.md` §3, §5, §7). Code does not redesign: a design gap goes back to Design as a
recorded question; a truth gap goes to the Master as `ESCALATE_TO_MASTER` or `NEEDS_CONTROLLED_CONTENT`.
