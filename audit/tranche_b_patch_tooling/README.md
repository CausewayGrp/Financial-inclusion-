# Tranche B patch tooling (read-only; audit lineage)

Reproduces `audit/MASTER_FIRST_PATCH_SPEC.csv`, `audit/TERMINOLOGY_SWEEP_KEEP_REGISTER.csv` and `audit/SOURCE_PUBLISHER_PROPOSALS.csv` from the Production Master, and simulates applying them. None of these scripts writes to the Master or to any projection.

```
M=authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx
python3 audit/tranche_b_patch_tooling/export_master.py $M /tmp/yfi_master_json      # read-only export, one JSON per sheet
export YFI_MASTER_JSON=/tmp/yfi_master_json
python3 audit/tranche_b_patch_tooling/build_spec.py /tmp/yfi_spec_out              # rebuilds the three CSVs (byte-identical to audit/)
YFI_SIM_OUT=/tmp/sim.json python3 audit/tranche_b_patch_tooling/simulate.py        # collisions, sweep residuals vs KEEP register, forbidden strings
YFI_PARITY_OUT=/tmp/parity.json python3 audit/tranche_b_patch_tooling/parity.py    # EN/AR numeric invariance before/after the spec
YFI_REPO=. python3 audit/tranche_b_patch_tooling/search_probe.py                   # 28-term bilingual search probe on dist/
```

- `pdefs_p1.py` … `pdefs_p4.py`: the patch definitions (P1 lineage; P2 false or misleading; P3/P4 parity, measurement, domains, methodology; P5 editorial). `sweeps.py`: the terminology sweeps PB-0413/0414/0415, resolved per occurrence with KEEP rules.
- `unbound_60.json`: the 60 evidence objects whose Master `source_dependencies` is empty, with the closure fallback that the current projection used (input to PB-0010…0069).
- Requires Python 3 and openpyxl.

## Canonical specification (after the recipient acceptance corrections)

- Build basis: the Stage-0 Master (entry Master `e6980410…` + AIR-001), SHA-256 `b010b60d…`. The spec rows' Excel rows refer to that state.
- `test_spec_determinism.py <Master.xlsx>` rebuilds twice in independent processes (different hash seeds and glob order) and requires identical bytes.
  Result for the canonical spec: `MASTER_FIRST_PATCH_SPEC.csv` SHA-256 `f31ebd49…` (1,001 rows, 395 roots).
- The PB-0413/PB-0414/PB-0415 sweep rows carry the executed per-cell decisions (`LEAD_REVISED_PER_CELL`, `KEEP`), read from
  `audit/tranche_b_execution/stage5_execute.py`.
- Execution is recorded separately: `audit/MASTER_FIRST_PATCH_EXECUTION_LEDGER.csv` (what happened to each root) — the spec records what was proposed.
