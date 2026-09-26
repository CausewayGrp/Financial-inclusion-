# Canonical Master → projection generator

Every file under `site-src/content/` is produced or rebound from the Production Master
(`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`) by this package. A projection is never edited by hand:
correct the Master, then regenerate.

## Commands (repository root)

| Purpose | Command | npm alias |
|---|---|---|
| Regenerate every projection in place | `python3 scripts/generate_projections.py` | `npm run generate` |
| Check that the committed projections equal the Master (no writes; exit 1 on any difference) | `python3 scripts/generate_projections.py --check` | `npm run check:projections` |
| Write to another folder (review / baseline) | `python3 scripts/generate_projections.py --out DIR` | — |
| Regression tests (structure, block inventory, determinism, lineage truth, locator rule, navigation, full-copy derivation, Master writer) | `python3 -m unittest discover -s scripts/projection/tests -t .` | `npm run test:generator` |
| Rebind control files to the current Master / Page Specs | `python3 scripts/rebind_authority.py --timestamp <ISO-8601>` | — |

`npm run validate` runs the projection check before the literal audit and the website validator; `npm run verify` adds the
generator tests and a build.

## Files

| File | Role |
|---|---|
| `master_reader.py` | Reads the .xlsx package directly (no spreadsheet library): typed cell values per sheet. |
| `structure.py` | Sheet model: main header row, titled sub-blocks (each with its own header), keyed records. |
| `master_structure.json` | Declared structure of every sheet (main header row and labels, titled blocks, numeric-text columns). The generator refuses a Master that does not match it. |
| `families.py` | GENERATED families: keyed records, block records, raw snapshots, field transforms. |
| `derived.py` | DERIVED builders (object-source closure v2, source reference map, search index, page specs) and the two CONTROLLED_CONTRACT rebinders. |
| `generator.py` | Context (Master + contract + manifest + controlled inputs) and the build/check driver. |
| `projection_manifest.json` | One entry per output: path, kind, owning sheet/block, rule, stable key, dependencies, transformation. |
| `controlled_inputs/` | Controlled templates that are **not Master-owned** (see below). |
| `master_writer.py` | Surgical, deterministic Master editor used by the execution scripts (exact current-value checks; no fuzzy matching). |
| `baseline_gate.py` | Entry baseline gate (run once, before any patch; results in `audit/generator_baseline/`). |
| `tests/` | Regression tests. |

## Output kinds (declared per file in `projection_manifest.json`)

- **GENERATED** — one-to-one projection of Master rows (keyed records, titled blocks or raw sheet snapshots).
- **DERIVED** — computed only from GENERATED outputs and controlled inputs: `sources/public_object_source_closure.json`,
  `sources/source_reference_map.json`, `content/search_index.json`, `page_specs.json`, `data/local_data_index.json`,
  `sources/local_dataset_catalog.json`.
- **CONTROLLED_CONTRACT — not Master-generated.** `content/navigation_interaction.json` and `presentation_priority.json`
  are maintained in place. The generator validates them against the Master (routes equal 02; sections and visuals exist)
  and rewrites only their Master-owned parts: global and trust navigation from 04, authority binding, search counts.

Controlled inputs that are not Master-owned: `local_dataset_catalog_template.json`, `closure_templates.json` (closure vocabulary
and rule text), `source_reference_templates.json`, `search_templates.json`, `page_spec_templates.json`,
`page_spec_design_intent.json` (internal per-route design intent; never rendered), `page_spec_binding_overrides.json`.
Public copy never lives in code or in a controlled input: interface copy is in the 04 block "Governed interface copy".

## Rules enforced at generation (fail loudly)

- Master structure equals `master_structure.json`; every titled block is read by its own title and header (PB-0473).
- Stable keys are unique; every page binding references an existing object.
- **Closure rule v2 (Tranche B Stage 1).** An Evidence Record shows only sources bound in `06.source_dependencies`; dataset-level
  tokens are never expanded; `06.lineage_state` must agree with the token classes; `06.verification_*` must equal the governed
  template of its state. Claims and visuals take the lineage of their 06 record; Readings resolve through their source bindings
  and member records.
- `02.full_copy_*` equals title + rendered 03 sections in section order (EXF-002).
- Only an http(s) URL is a public original locator (EXF-001).
