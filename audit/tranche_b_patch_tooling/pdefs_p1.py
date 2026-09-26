# -*- coding: utf-8 -*-
"""P1 — VERIFICATION INTEGRITY (LEAD-B07, LEAD-M06). Object-level source lineage."""
import json, os

S = os.path.dirname(os.path.abspath(__file__))
ALT = {x["object_id"]: x for x in json.load(open(f"{S}/unbound_60.json"))}

POS_M = [f"SRC-CBY-POS-2025-{m:02d}" for m in range(3, 13)] + ["SRC-CBY-POS-2026-01"]
POS_V = [s for s in POS_M if s != "SRC-CBY-POS-2025-09"]
SFD_Q = ["SRC-SFD-MF-HISTORY-TOR-2012-001", "SRC-SFD-Q1-2012-001", "SRC-SFD-Q1-2015-001", "SRC-SFD-Q1-2019-001",
         "SRC-SFD-Q2-2013-001", "SRC-SFD-Q2-2014-001", "SRC-SFD-Q3-2015-001", "SRC-SFD-Q3-2016-001",
         "SRC-SFD-Q4-2009-001", "SRC-SFD-Q4-2010-001", "SRC-SFD-Q4-2011-001", "SRC-SFD-Q4-2012-001",
         "SRC-SFD-Q4-2015-001", "SRC-SFD-Q4-2017-001", "SRC-SFD-Q4-2018-001", "SRC-SFD-Q4-2020-001"]
ENF = [f"SRC-CBY-ENF-{n:02d}-2026" for n in (1, 2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 15, 17)]
LDB, F14, AGG, MICRO = "SRC-WB-FINDEX-LDB-2015-001", "SRC-WB-FINDEX-2014-001", "SRC-WB-FINDEX-AGG-2022", "SRC-WB-FINDEX-001"

# decision classes → lineage_state
BE, BC, CO, NB = "BOUND_EXACT", "BOUND_CANDIDATE__EXECUTION_CHECK", "COMPOSITE_OF_OBJECTS", "SOURCE_NOT_YET_BOUND"

BIND = {
 # --- quantitative visuals: derived deterministically from Master observation rows (metric + contracted period)
 "VIS-POS-TERMINALS":   (BE, POS_M, "19_PAYMENTS_DATA rows IND-0002 filtered to contracted period Mar-2025–Jan-2026; excludes SRC-CBY-PAYREPORT-Q3-2024 and -H1-2025 (different publications, break-in-series)."),
 "VIS-POS-TRANSACTIONS":(BE, POS_M, "19_PAYMENTS_DATA rows IND-0003 filtered to contracted period Mar-2025–Jan-2026; excludes the two cross-publication snapshots."),
 "VIS-POS-VALUE":       (BE, POS_V, "19_PAYMENTS_DATA rows IND-0004, Mar-2025–Jan-2026; Sep-2025 has no source value and therefore no source."),
 "VIS-REMITTANCE-MACRO":(BE, ["SRC-IMF-AIV-2025-STAFF-001", "SRC-IMF-AIV-2025-SUPP-001"], "23_REMITTANCES metric RMT-001 only; removes the two World Bank RPW corridor-price sources the dataset-level resolution attached."),
 "VIS-REMITTANCE-COST": (BE, ["SRC-WB-RPW-SA-YEM-2025Q3-001", "SRC-WB-RPW-UAE-YEM-2025Q3-001"], "23_REMITTANCES metric RMT-002 only; removes the two IMF Article IV documents the dataset-level resolution attached."),
 "VIS-FIRM-CONSTRAINTS":(BE, ["SRC-WB-FSD-2024-001"], "20_FIRM_FINANCE metric FFM-007 only; removes SRC-WB-ES-2013-PROFILE-001 (a different survey)."),
 "VIS-FIRM-FINANCE-SEVERITY": (BE, ["SRC-WB-FSD-2024-001"], "20_FIRM_FINANCE metric FFM-006 only; removes SRC-WB-ES-2013-PROFILE-001."),
 "VIS-FIRM-FINANCE-PATH": (BE, ["SRC-WB-FSD-2024-001"], "Loan-source rows of the 2022 custom survey only; removes SRC-WB-ES-2013-PROFILE-001."),
 "VIS-FINDEX-GAPS":     (BE, [AGG], "25_FINDEX_BASELINE rows WB-FINDEX-OBS-2022-001..006 (all source_url data.worldbank.org FX.OWN.* )."),
 "VIS-PAYMENT-ANATOMY": (BE, ["SRC-CBY-PAYREPORT-H1-2025"], "Contract period 2025 H1; 19_PAYMENTS_DATA rows labelled '2025 H1' resolve to this single publication."),
 "VIS-MFI-2014-PANEL":  (BE, ["SRC-YMN-MFMAG-2014-Q1-001", "SRC-YMN-MFMAG-2014-Q2-001"], "21_MFI_DATA rows with period 2014 Q1/Q2."),
 "VIS-MFI-RUPTURE-LENS":(BE, ["SRC-SFD-Q1-2015-001", "SRC-SFD-Q3-2015-001", "SRC-SFD-Q4-2015-001"], "Contracted snapshots 2015-03/09/12 = SFD Q1/Q3/Q4-2015 reports (21_MFI_DATA holds no 2015 rows; lineage token 77_MFI_TEMPORAL_SPINE is catalogued in 16_DATASET_CATALOG)."),
 "VIS-MFI-SPINE":       (BC, SFD_Q, "Spine spans 2010–2024 observations; SFD quarterly/year-end reports are the controlled inputs (same set as CLM-022). Confirm any YMN rows used for 2021+ at execution."),
 "VIS-CAPITAL-CONTEXT": (BE, ["SRC-OCHA-FTS-YEM-2026-001"], "Single controlled input (OCHA FTS 2026)."),
 "VIS-E-MONEY-RULE-STACK": (BE, ["SRC-CBY-PSP-RULES-2022-001", "SRC-CBY-EMONEY-2023-001", "SRC-CBY-EMONEY-AMD-2025-001"], "Contract names exactly: 2022 PSP framework → 2023 mobile e-money rule → 2025 amendment."),
 "VIS-FCP-REDRESS-PATH":(BE, ["SRC-CBY-FCP-INSTR-2023-001", "SRC-CBY-FCP-BROCHURE-2024-001"], "Aug-2023 instrument + Mar-2024 official guidance brochure (the redress windows come from the brochure)."),
 "VIS-OECD-FCP-TIMELINE": (BC, ["SRC-CBY-FCP-INSTR-2023-001", "SRC-CBY-FCP-AWARE-2024-001", "SRC-CBY-FCP-BROCHURE-2024-001", "SRC-OECD-YEM-RESILIENCE-001"], "OECD 2026 text has not been read by the programme (verification record 12-Sep-2026); keep the OECD node labelled as unverified secondary attribution."),
 "VIS-FL-EVIDENCE-LADDER": (BC, ["SRC-CBY-GMW-2023-001", "SRC-CBY-GMW-2024-001", "SRC-CBY-GMW-2024-CLOSE-001", "SRC-CBY-GMW-2025-001", "SRC-OECD-INFE-2023"], "Activity rungs bind to the four GMW records; the population-capability rung binds to OECD/INFE 2023 but carries no Yemen value until PB-0101/PB-0108 are resolved."),
 "VIS-PAYMENT-RAILS":   (BC, None, "Narrow the ten dataset-resolved sources to the FMIIP project record and the dated CBY architecture/institution events actually drawn; confirm at execution."),
 "VIS-TARGET-RESULT-STATE": (BE, ["SRC-WB-FMIIP-P180708"], "All FMIIP-RF targets/baselines in 31_REFORMS_REGULATION cite SRC-WB-FMIIP-P180708; replaces SRC-UNDP-FMIIP-001 reached via 49_METRIC_CROSSWALK."),
 "VIS-FINDEX-ACCESS-USE": (BE, [MICRO], "Method/contract visual on HOLD_WEIGHTED_MICRODATA; publishes no estimate. Source = Findex microdata catalogue."),
 "VIS-FINDEX-BARRIERS":   (BE, [MICRO], "As above (HOLD)."),
 "VIS-FINDEX-RESILIENCE": (BE, [MICRO], "As above (HOLD)."),
 "VIS-FINDEX-FLOW-CHANNELS": (BE, [MICRO], "As above (HOLD)."),
 "VIS-FINDEX-SAMPLE-SUPPORT": (BE, [MICRO], "Sample-support metadata from the DDI; not a population estimate."),
 "VIS-FINDEX-OBSERVED-WAVES": (BE, [LDB, F14, AGG], "2011 comparator and 2014 headline from the 2015 Little Data Book / 2014 database; 2022 aggregate from FX.OWN.TOTL.ZS."),
 "VIS-BORROWING-SOURCES-2014": (BE, [LDB], "Passport EP-FINDEX-2014-NEEDS-FLOWS: The Little Data Book on Financial Inclusion 2015."),
 "VIS-DOMESTIC-REMITTANCE-PATH-2014": (BE, [LDB], "As above."),
 "VIS-SOURCE-COMPARISON": (CO, [], "Compares definitions of other records; each compared record carries its own lineage."),
 "VIS-EVIDENCE-CLASS-LADDER": (CO, [], "Classifies other records by evidence class; asserts no new fact."),
 "VIS-EVIDENCE-FRESHNESS": (CO, [], "Plots the vintage of other records; each point opens its own record."),
 "VIS-EVIDENCE-GAPS": (CO, [], "Gap matrix over other records; a gap cites the record whose absence it describes."),
 "VIS-INCLUSION-TRANSMISSION": (CO, [], "System map; each node must link to the evidence records it summarises, not to sources directly."),
 "VIS-MECHANISM-METRIC-BRIDGE": (CO, [], "Edges link 32_QUAL_LITERATURE rows (each with its own source_id) to quantitative records."),
 "VIS-PROVIDER-OBSERVABILITY": (CO, [], "Each class×dimension badge must cite the record it summarises."),
 "VIS-DEMAND-VINTAGE-LADDER": (CO, [], "One rung per financial function; each rung opens its own Findex record."),
 "VIS-PROVIDER-TIME": (NB, [], "Visual contract state BLOCKED_BY_2026_ROSTER_EXTRACTION_AND_WALLET_UNIVERSE; no public render until unblocked."),
 # --- claims
 "CLM-004": (BC, ["SRC-CBY-PAYREPORT-H1-2025", "SRC-WB-FMIIP-P180708"], "Semantic-boundary claim citing H1-2025 counts and project account counts; drop the eleven monthly POS sources reached via 11_CBY_PAYMENTS. Confirm against copy at execution."),
 "CLM-005": (BE, ["SRC-WB-FSD-2024-001"], "2022 seven-governorate custom survey only; removes SRC-WB-ES-2013-PROFILE-001."),
 "CLM-006": (BE, ["SRC-WB-FSD-2024-001"], "As above."),
 "CLM-008": (BE, ["SRC-CBY-BANKLIST-AR-2026-001"], "The claim concerns the 26-row licensed-bank list only; removes 13 exchange/remittance enforcement decisions attached via 15_PROVIDER_MASTER."),
 "CLM-014": (CO, [], "Freshness-by-domain claim; cite the per-domain evidence records, not a 30-source union."),
 "CLM-015": (BE, ["SRC-CBY-UNLICENSED-EWALLET-2024-001"], "Single dated negative-authority circular."),
 "CLM-016": (BE, ["SRC-CBY-EXCH-LIST-2025-001"], "Single 2025 roster."),
 "CLM-018": (BC, ["SRC-CBY-UNIFIED-NET-2026-001", "SRC-CBY-BANK-NETWORK-MTG-2026-001", "SRC-CBY-YPCC-FOUND-2026-001", "SRC-CBY-YPCC-BOARD-2026-001"], "Institutional-state events 2026-06-17 to 2026-08-04; drops POS, H1-2025 report and FMIIP workshop sources."),
 "CLM-019": (BE, ["SRC-CBY-EXCH-LIST-2026-001"] + ENF, "2026 roster + the thirteen dated enforcement decisions; drops bank list, FMIIP workshop, e-wallet negative list and YMN membership."),
 "CLM-020": (BC, ["SRC-SFD-NEWSLETTER-2000-Q4-001", "SRC-SFD-HIST-2004-Q3-001", "SRC-SFD-MF-HISTORY-TOR-2012-001", "SRC-YMN-IMPACT-2021-001"], "Origin-layer sources; drops 2012/2015 quarterly reports. Confirm locators at execution."),
 "CLM-022": (BE, SFD_Q, "The sixteen SFD reports are exactly the spine inputs."),
 "CLM-024": (BE, [MICRO], "Findex microdata DDI (raw case shares)."),
 "CLM-026": (BE, [MICRO, AGG], "Microdata catalogue + published aggregate."),
 "CLM-027": (BC, [LDB, F14, AGG], "Wave anchors 2011/2014/2022; drop microdata and SRC-WB-FINDEX-003 unless a wave value is drawn from them."),
 "CLM-028": (BE, [LDB], "2014 needs/flows profile."),
 "CLM-029": (BE, [LDB], "2014 needs/flows profile."),
 "CLM-030": (BE, [LDB], "2014 needs/flows profile."),
 "CLM-031": (CO, [], "Vintage-asymmetry claim across functions; cite CLM-001/027/028/029/030 records."),
 # --- dataset objects
 "DS-FCP-ARCH": (BE, ["SRC-CBY-FCP-INSTR-2023-001", "SRC-CBY-FCP-AWARE-2024-001", "SRC-CBY-FCP-BROCHURE-2024-001"], "Instrument (ref. 589, 20-Aug-2023), awareness material, redress brochure."),
 "DS-QUAL-EVIDENCE": (CO, [], "Register of 32_QUAL_LITERATURE rows, each with its own source_id."),
 "DS-FINDEX-PUBLIC-HISTORY": (BC, [LDB, F14, AGG], "Historical public Findex aggregates; confirm SRC-WB-FINDEX-003 role at execution."),
 "DS-FINDEX-HISTORY-CROSSWALK": (CO, [], "Method crosswalk between waves; asserts comparability rules, not values."),
 "DS-DEMAND-VINTAGE-LENS": (CO, [], "Function-level evidence clocks over other records."),
}

def binding_rows():
    out = []
    for oid, (state, srcs, note) in BIND.items():
        alt = ALT[oid]
        if srcs is None:  # candidate narrowed from alt list
            srcs = alt["alt_sources"] or []
        before_alt = alt["alt_sources"] or []
        removed = [s for s in before_alt if s not in srcs]
        out.append(dict(oid=oid, state=state, srcs=srcs, removed=removed, note=note,
                        alt_via=alt["alt_via"], cls=alt["class"]))
    return out

P1 = [
 dict(pid="PB-0001", lead="LEAD-B07", pri="P1", op="SCHEMA", sheet="06_EVIDENCE_OBJECTS", obj="SCHEMA", field="lineage_state (new column after source_links)",
      cur="(column absent)", new="Controlled vocabulary: BOUND_EXACT | BOUND_CANDIDATE__EXECUTION_CHECK | COMPOSITE_OF_OBJECTS | SOURCE_NOT_YET_BOUND | FRAMING_NO_FACT. Populate for all 108 rows: the 48 rows with non-empty source_dependencies → BOUND_EXACT unless re-checked; the 60 empty rows → values in PB-0010..PB-0069.",
      ctype="BOUNDARY_TIGHTENING", sem="yes", lang="n/a",
      basis="Master 06_EVIDENCE_OBJECTS: source_dependencies empty on 60/108 rows; closure file stamps all 108 'CLOSED_VIA_CONTROLLED_DEPENDENCIES'.",
      reason="Lets the public surface say, per record, whether its source is bound, composite, or not yet bound — instead of implying lineage that does not exist.",
      down="evidence_objects.json; public_object_source_closure.json; every /evidence/<id>/ page; search_index.json",
      search="Facet 'Source bound / not yet bound' becomes possible", ia="none", vis="none", rights="Enables rights to attach per bound source",
      val="Regenerate; assert every 06 row has a lineage_state; assert rows with lineage_state=BOUND_* have non-empty source_dependencies whose IDs exist in 15_SOURCE_LIBRARY; assert COMPOSITE rows list member object IDs."),
 dict(pid="PB-0002", lead="LEAD-B07", pri="P1", op="GENERATOR", sheet="GENERATOR: public_object_source_closure", obj="closure rule", field="closure_state derivation",
      cur="CLOSED_VIA_CONTROLLED_DEPENDENCIES asserted on 108/108 records although 87/108 carry non-empty unresolved_dependency_ids; dataset tokens (e.g. 17_REMITTANCES, 15_PROVIDER_MASTER, 11_CBY_PAYMENTS) resolve to every source in the dataset (51 records).",
      new="(1) CLOSED_* only when unresolved_dependency_ids is empty; otherwise PARTIALLY_RESOLVED. (2) A dataset token resolves only to the sources of the observation rows the object actually uses (metric/indicator ID + contracted period from 11_VISUAL_LIBRARY or the claim's evidence_inputs), never to the whole dataset. (3) Replace NO_SOURCE_EXPECTED with the object's lineage_state (PB-0001): SOURCE_NOT_YET_BOUND is an open gap, rendered as such; FRAMING_NO_FACT only for objects that assert no fact.",
      ctype="BOUNDARY_TIGHTENING", sem="yes", lang="n/a",
      basis="public_object_source_closure.json: closure_state counts VIA=108, NO_SOURCE_EXPECTED=75, CLOSED_TO_SOURCE_ID=40; 87 VIA records with unresolved dependencies; 51 resolved via dataset tokens (all 42 tokens governed in 16_DATASET_CATALOG.origin_table).",
      reason="The closure 'pass' currently measures the wrong thing. The honest pass rate will fall; that fall is the truthful number.",
      down="public_object_source_closure.json; build.py evidence_trace; validate.py closure checks",
      search="none", ia="none", vis="Visual trace lists shrink to real inputs", rights="none",
      val="After regeneration: count of CLOSED_* with unresolved>0 must be 0; VIS-REMITTANCE-MACRO resolves to exactly the two IMF sources; CLM-008 to the bank list only; VIS-POS-TERMINALS to the 11 monthly POS sources."),
 dict(pid="PB-0003", lead="LEAD-B07", pri="P1", op="GENERATOR", sheet="GENERATOR: evidence_objects.json", obj="projection fidelity", field="source_dependencies",
      cur="Projection drops the field on 108/108 objects, including the 48 whose Master cell is populated (e.g. CLM-001 → SRC-WB-FINDEX-AGG-2022; SRC-WB-FINDEX-2025-EDITION).",
      new="Project 06_EVIDENCE_OBJECTS.source_dependencies and lineage_state verbatim into evidence_objects.json.",
      ctype="BOUNDARY_TIGHTENING", sem="no", lang="n/a",
      basis="Master vs projection comparison: 48 objects have Master lineage the projection does not carry.",
      reason="Projection-fidelity loss; the Master is already correct for these 48.",
      down="evidence_objects.json", search="none", ia="none", vis="none", rights="none",
      val="Field-level parity test Master↔projection for all 108 objects."),
 dict(pid="PB-0004", lead="LEAD-B07", pri="P1", op="BUILD", sheet="scripts/build.py", obj="_closure_for_object / evidence_trace (lines ~771–827)", field="source-path rendering",
      cur="If the evidence_object closure record has no resolved sources, the renderer falls back to the public_claim or visual record, which resolves through a whole dataset token; the fallback list is rendered as the record's 'Source verification path'.",
      new="Render only sources bound to this object (lineage_state BOUND_*). For COMPOSITE_OF_OBJECTS render 'This view is assembled from these evidence records' with links to the member records. For SOURCE_NOT_YET_BOUND render the governed statement UI-EVID-UNBOUND (PB-0006). Remove the cross-type fallback.",
      ctype="BOUNDARY_TIGHTENING", sem="yes", lang="both",
      basis="build.py lines 771–782 (_closure_for_object preferred-type fallback) and 809–827 (evidence_trace).",
      reason="Verification must never imply that a record is sourced because unrelated sources exist in the same dataset.",
      down="dist/*/evidence/*/index.html (108×2)", search="none", ia="none", vis="none", rights="none",
      val="Spot-check the four known contaminations (VIS-REMITTANCE-MACRO, VIS-REMITTANCE-COST, CLM-008, VIS-POS-TERMINALS) render only their bound sources; unbound records render UI-EVID-UNBOUND."),
 dict(pid="PB-0005", lead="LEAD-B07", pri="P1", op="BUILD", sheet="scripts/build.py", obj="evidence_citation_context (line ~785)", field="'Original source IDs' in citation text",
      cur="source_ids=[sid for sid,_,_ in _public_source_rows(spec)] — the page spec's route-level source_references list.",
      new="Use the object's own bound source_dependencies; omit the 'Original source IDs' clause when lineage_state is not BOUND_*.",
      ctype="BOUNDARY_TIGHTENING", sem="yes", lang="both",
      basis="build.py evidence_citation_context uses _public_source_rows(spec) (route union).",
      reason="A copied citation must not attribute a figure to sources it did not come from.",
      down="dist/*/evidence/*/index.html citation block; any 'copy citation' export", search="none", ia="none", vis="none", rights="Attribution accuracy",
      val="For CLM-008 the citation lists SRC-CBY-BANKLIST-AR-2026-001 only."),
 dict(pid="PB-0006", lead="LEAD-B07", pri="P1", op="NEW", sheet="04_NAV_UX", obj="UI-EVID-UNBOUND (new UI copy row)", field="label_en / label_ar",
      cur="(no governed copy; state not rendered)",
      new="EN: This record has not yet been linked to a specific original source. Treat its figures as unverified for reuse until the link is added. || AR: لم يُربط هذا السجل بعدُ بمصدر أصلي محدد، فلا تُعامل أرقامه على أنها صالحة لإعادة الاستخدام إلى أن يُضاف هذا الربط.",
      ctype="TRUST_COPY_REFINEMENT", sem="yes", lang="both",
      basis="New governed microcopy required by PB-0004.", reason="The open state must be said in words, in both languages.",
      down="build.py evidence labels; dist evidence pages", search="none", ia="none", vis="none", rights="none",
      val="Rendered on every SOURCE_NOT_YET_BOUND record in both languages."),
 dict(pid="PB-0007", lead="LEAD-M06", pri="P1", op="FIELD_ALL", sheet="06_EVIDENCE_OBJECTS", obj="107 rows (all except CLM-019)", field="verification_en",
      cur="Show the definition, population or group covered, calculation base where relevant, period, geography, method, limitations, source and reuse conditions. If a value or source link is unavailable, say so explicitly rather than inferring or inventing it.",
      new="GENERATED per record from lineage_state and bound sources, using governed templates UI-VERIFY-BOUND / UI-VERIFY-COMPOSITE / UI-EVID-UNBOUND (PB-0008). The free-text boilerplate is retired; 'rather than inferring or inventing it' is removed from all public surfaces.",
      ctype="TRUST_COPY_REFINEMENT", sem="yes", lang="en",
      basis="Master: verification_en has 2 distinct values across 108 objects; this one is an instruction to authors, rendered 107× under 'How can I verify it?'.",
      reason="Readers need a verification path for this record, not a production checklist; the clause volunteers that the product might invent sources.",
      down="evidence_objects.json; dist evidence pages 'How can I verify it?' block", search="none", ia="none", vis="none", rights="none",
      val="No public page contains 'rather than inferring or inventing it'; each evidence page's verification block names its own sources or its unbound state."),
 dict(pid="PB-0007A", lead="LEAD-M06", pri="P1", op="FIELD_ALL", sheet="06_EVIDENCE_OBJECTS", obj="107 rows (all except CLM-019)", field="verification_ar",
      cur="يُعرض التعريف، والمجتمع أو النطاق الذي ينطبق عليه الدليل، وقاعدة الاحتساب عند الحاجة، والفترة، والجغرافيا، والطريقة، والحدود، والمصدر، وشروط إعادة الاستخدام. وإذا كانت قيمة أو وصلة مصدر غير متاحة، يُذكر ذلك صراحةً بدل استنتاجها أو اختلاقها.",
      new="يُولَّد لكل سجل من حالة ربطه بالمصدر ومصادره المرتبطة، وفق القوالب المعتمدة UI-VERIFY-BOUND / UI-VERIFY-COMPOSITE / UI-EVID-UNBOUND (PB-0008). ويُلغى النص الموحد، وتُحذف عبارة «بدل استنتاجها أو اختلاقها» من كل الواجهات العامة.",
      ctype="TRUST_COPY_REFINEMENT", sem="yes", lang="ar", basis="As PB-0007.", reason="As PB-0007.",
      down="As PB-0007", search="none", ia="none", vis="none", rights="none", val="As PB-0007 (Arabic)."),
 dict(pid="PB-0008", lead="LEAD-M06", pri="P1", op="NEW", sheet="04_NAV_UX", obj="UI-VERIFY-BOUND / UI-VERIFY-COMPOSITE (new UI copy rows)", field="label_en / label_ar",
      cur="(absent)",
      new="UI-VERIFY-BOUND EN: This record is drawn from the source(s) listed below. Open a source record to reach the publisher's original document and check that the definition, period, population and geography match what is stated here. || AR: يستند هذا السجل إلى المصدر أو المصادر المدرجة أدناه. افتح سجل المصدر للوصول إلى وثيقة الجهة الناشرة، وتحقق من تطابق التعريف والفترة والمجتمع والنطاق الجغرافي مع ما يرد هنا. ##### UI-VERIFY-COMPOSITE EN: This view assembles other evidence records. Check each linked record against its own source. || AR: يجمع هذا العرض سجلات أدلة أخرى، فتحقق من كل سجل مرتبط مقابل مصدره الخاص.",
      ctype="TRUST_COPY_REFINEMENT", sem="yes", lang="both", basis="New governed microcopy for PB-0007.", reason="Reader-facing verification path.",
      down="build.py; dist evidence pages", search="none", ia="none", vis="none", rights="none", val="Templates render with the record's own bound source list."),
]
