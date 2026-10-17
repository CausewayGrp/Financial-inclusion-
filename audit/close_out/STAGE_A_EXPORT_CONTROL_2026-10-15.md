# Stage A export control — 15 October 2026

Authority: the owner's Stage A final reconciliation mandate, issued this date. This is an operational containment and retention decision, not source-rights clearance or public-release approval.

## Verified baseline and immediate control

GitHub main `a2ad120784822ce068aacc5fd638b69429612b73`, repository PRIVATE, no open PRs; Verify run `38718968732` successful. Privacy was checked once; no visibility changes are required or made. `site-src/deployment.json` retains `public_downloads: false`, `pre_release: true`, and a null production origin.

`.github/workflows/verify.yml` generated and uploaded `yfie-data-exports` on every successful governance job. Uploading an archive is distribution to repository-authorized recipients even when it does not enter `dist/`. Remove that upload. Keep `scripts/tests/test_exports.py --out build/exports` unchanged: generation, CSV/JSON parity, provenance, publication filtering, licence attachment and the planted-fault test remain mandatory. All other governance, browser, security, hosting and negative-control jobs remain enforced.

## Existing artifacts: bounded preservation

The complete two-page API inventory contains **119** retained artifacts, all named `yfie-data-exports`, created 3–15 October 2026. IDs, sizes, source heads, run IDs and individual expiry timestamps are preserved in `STAGE_A_EXPORT_ARTIFACT_INVENTORY_2026-10-15.json`. Latest artifact: **11964531677**, run **38718968732**, 585,029 bytes. This is metadata verification, not inspection of the historical ZIP bytes.

An attempted authenticated download redirects to `productionresultssa8.blob.core.windows.net`, which the session's outbound proxy refuses. No successful archive copy exists. Consequently **no historical artifact is deleted**. The approved interim retention path is the existing private repository's Actions artifact store until each recorded expiry, pending a verified private archive transfer and subsequent disposition decision. Repository access controls remain in place. Do not delete required audit records, publish these exports, or claim that prior access or exposure has been reversed. The inventory is preserved in private Git history beyond artifact expiry; original governed inputs and export code remain reproducible there. It is not a substitute for historical archive bytes.

## Redistribution limitations

The current export implementation (`scripts/exports.py`) includes six datasets: evidence records, public claims, sources, visual rows, chronology and measurement agenda, plus a draft bilingual codebook and licence. This inspection establishes what the current code would generate, not byte-for-byte identity with every retained historical artifact. Public locator filtering is a citation/publication control, **not a redistribution licence check**. Source-library rights states travel in the source export, but the exporter does not exclude visual/evidence rows merely because their sources are NOT_ASSESSED or restricted. Therefore redistribution approval for the bundles is **not established**.

Release-relevant examples: `SRC-WB-RPW-US-YEM-2025Q3-001` and `SRC-WB-RPW-SA-YEM-2025Q3-001` feed derived quoted-cost summaries/visual rows; the final report records the RPW workbook's “Restricted Data” terms (§10, item 12). Original permission and applicable scope remain unverified. `SRC-IMF-YEM-AIV-2025-2026` is NOT_ASSESSED; citation and bounded factual discussion do not establish permission to redistribute an extracted compilation. CauseWay's confirmed CC BY 4.0 licence covers only what CauseWay owns. No third-party permission is inferred from that licence, a public URL or a research package. Existing citation and bounded factual use are not blanket-prohibited by this finding.

No bulk adjudication of the remaining source-rights inventory is attempted. Before exports or public downloads are enabled: verify source-specific terms for included material, decide any necessary exclusions, review the codebook bilingually, and obtain the separate owner download/publication authorization. Archive-host access is the precise remaining prerequisite to inspecting and privately preserving the existing bundles; no new repository administrator permission is requested.

## Addendum, 17 October 2026 — finding F-05 (takeover brief, Part 4)

After this containment, a push-triggered workflow on the unreviewed branch `work/privacy-runtime-notice-20261015` (head `7e2cf997`) tarred every tracked file except `dist/` and uploaded the archive as an Actions artifact with one-day retention. It ran successfully twice on 15 October 2026. The branch was never merged. It is archived and deleted by the owner-run Housekeeping workflow (W5), and `docs/REPOSITORY_SETTINGS.md` (W5) recommends restricting workflows on non-default branches to pull-request events or requiring approval. The retained-artifact disposition above is unchanged.
