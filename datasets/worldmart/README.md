# WorldMart Dataset — Conceptual Framing Document

## Status: CONCEPTUAL FRAMING DEVICE

The WorldMart dataset is named throughout the research program as a conceptual frame for behavioral event logs derived from Black consumer shopping interactions. As of 2026-04-29, no public dataset exists under this name.

This directory is the target for the dataset formalization work. See proposal/executive-summary-proposal.md, Section 8 (Limitations), item 4.

---

## What the Dataset Will Contain (When Formalized)

WorldMart behavioral event logs will capture:

- Shopping interactions coded against the Eight Wonders taxonomy
- Turn-by-turn decision points with relational context preserved
- Frontin' events: instances where surface behavior diverges from relational motivation
- Evidence Preservation sequences (Wonder 6 — The Receipts)
- Social Verification Rituals (Wonder 1 — The Nod)

---

## Formalization Plan

Phase 1: Synthetic data generation — construct scenario-based event logs against each Wonder's proxy signal taxonomy
Phase 2: Annotation protocol — define coder training procedure and inter-rater reliability target (κ ≥ 0.70)
Phase 3: Pilot collection — small convenience sample with participant consent
Phase 4: Public release — anonymized, annotated, with full methodology documentation

---

## Related

- /proposal/executive-summary-proposal.md — primary research proposal
- /governance-kernel/contract-window/contract_window.py — governance mechanism that will be applied to analysis sessions using this dataset
- Frontin' at WorldMart paper (external) — /Users/coreyalejandro/frontin-at-worldmart-full-draft.md

---

V&T: worldmart-dataset-readme.md — EXISTS (written)
  → VERIFIED AGAINST: proposal limitations section, session memory
  → NOT CLAIMED: existing dataset, collected data, validated annotation protocol
  → FUNCTIONAL STATUS: placeholder and formalization roadmap, no data yet
