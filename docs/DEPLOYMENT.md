# Deployment

The canonical Google Drive repository stores the Production Master, governed source/control inputs and implementation sources. Generated `dist/` state is disposable and is **not** stored as canonical Drive state.

Before preview or deployment, run:

```bash
npm run verify
```

This regenerates `dist/` and validates the public build. Deploy **only the resulting `dist/` contents** as the static site. The authority workbook at `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`, internal controls, and non-public source material must never be copied into the public bundle.

Configure the host to serve `404.html` for unknown routes and preserve trailing-slash paths. Root redirects Arabic-first to `/ar/`; English is available at `/en/`.

No database, secret or live API is required for the initial static build. Future APIs/adapters may replace or refresh local payload sources only after their endpoint, schema, rights, cadence and semantic mapping are controlled; the UI must not depend on those future services for the first complete handoff.

The public bundle must not be modified to add unfiltered source files, internal evidence objects, the Production Master, or restricted material. Future content/data refreshes must originate in the Production Master where semantic changes are material, then regenerate the controlled projections and pass the repository validator.

Deployment itself does not constitute release approval. Browser/runtime, RTL/mobile, accessibility, security/privacy, correction/version behavior, publication filtering and named release approval remain separate gates.
