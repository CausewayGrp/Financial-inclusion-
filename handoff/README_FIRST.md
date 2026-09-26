> STATUS: **HOLD FOR FINALIZATION — NOT YET THE RECIPIENT START FILE.** The production repository is undergoing final independent product/evidence acceptance. Use the root `README.md` and `authority/YFI_CURRENT_PROJECT_CONTEXT.json` for current state. This file will be promoted only when clean-room handoff closes.

# READ THIS FIRST — FINAL CLAUDE DESIGN → CLAUDE CODE HANDOFF

When this file is promoted (R8.6), the repository will be handed over for **product design execution**, not another review cycle. Until then it is a draft.

The public institutional definition is now settled in the current Master/Page Specs: **Yemen Financial Inclusion Evidence is a bilingual public evidence resource that helps users understand, compare and verify evidence on financial inclusion in Yemen; it supports decision-making by making evidence scope, limits and sources explicit.**

## Start now

Open `handoff/MASTER_IMPLEMENTATION_PROMPT.md` and follow it as the single launch instruction.

For Claude Design, the working material is the actual product: `site-src/content/page_specs.json`, `presentation_priority.json`, navigation/interaction content, visual contracts with their design tiers and data contracts (`handoff/VISUAL_DESIGN_CONTRACT.md`), Readings, Measurement Agenda, source-reference payloads, the current site source and the CauseWay logo.

Do **not** begin by reading historical review/closure documents. They are audit lineage, not design work. Consult authority metadata only if a controlled object appears contradictory.

The current implementation is a **behavioral and semantic regression baseline, not final visual authority**. Claude Design is expected to materially elevate composition, typography, hierarchy, data presentation, page-family identity, RTL/LTR execution and interaction while preserving controlled meaning.

Arabic and English are co-authoritative. Use the supplied CauseWay logo. IBM Plex Sans (English) and IBM Plex Sans Arabic (Arabic) are the default final type system. A departure is allowed only with a written rationale in the design package showing a system that is materially stronger, locally packageable, accessible and equally successful in Arabic and English; a second display face needs the same rationale. Do not introduce a font simply for novelty. The final design must cover the full product, not only Home.

Claude Code starts only after the complete repository-backed `design/` package exists. It then implements one final React static-prerender/export runtime from that design package and the controlled local payloads.

If a substantive controlled field is genuinely missing, use `NEEDS_CONTROLLED_CONTENT`. If the controlled truth itself appears wrong, use `ESCALATE_TO_MASTER`. Otherwise keep designing/building; do not substitute another report or control layer for execution.
