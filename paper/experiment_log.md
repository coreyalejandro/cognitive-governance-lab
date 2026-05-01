# Experiment Log — Runtime Constitutional Governance Paper

## Contribution (one sentence)
The Contract Window — a four-field runtime artifact enforcing six Constitutional AI-derived invariants — prevents Insight Atrophy (hypothesis-space contraction) in long human-AI investigative sessions where standard Constitutional AI has no governance mechanism.

---

## Claims-to-Experiments

| Claim | Experiment | Files | Figures | Status |
|-------|-----------|-------|---------|--------|
| C1: CW reduces intent-drift ≥25% | 6-condition between-subjects, H1 | cognitive-governance-lab/tests/ | TBD — IAI curve per condition | PENDING live pilot |
| C2: Bilateral doubles repair rate | Within-condition repair analysis, H2 | cognitive-governance-lab/tests/ | TBD — repair rate bar chart | PENDING |
| C3: FK≤8 produces ≥80% comprehension | Lay-reader comprehension quiz, H3 | TBD | TBD | PENDING |
| C4: BicameralReview kappa ≥0.70 | Human IRR study | artifacts/case-law/BREAK_GLASS_20260429* | Kappa comparison table | CONSTRUCTED (synthetic 0.762) |
| C5: IAI measures Insight Atrophy | IAI calibration | research-plan.md, tests/ | IAI score distribution | CONSTRUCTED (heuristic) |
| C6: I1-I6 map to CAI principles | Principle mapping table | THREE_PROPOSALS_MASTER.md | Table in Section 3 | VERIFIED |

---

## Verified Instrumentation Results

### BicameralReview Synthetic Pilot
- All 28 model turns: kappa = 0.627
- Bicameral-active sessions only (n=15 model turns): kappa = 0.762
- Gate threshold: 0.70 — PASSED
- Root cause of initial failure (kappa = -0.057): PHANTOM_PATTERNS too narrow
- Fix: 4 new patterns added (comparative-pct, predicate-first-pct, ratio claims)
- Source: artifacts/case-law/BREAK_GLASS_20260429_MONTH1_PHANTOM_DETECTION_MISS.md
- Status: VERIFIED

### Test Suite
- ContractWindow: 9/9 passing
- SessionRecorder: 29/29 passing
- Full suite: 62/62 passing (per RESEARCH_PLAN_GO_20260429.md, April 2026)
- Status: VERIFIED

---

## Misalignment Forensics (Section 5.3 Evidence)

Three documented behavioral incidents from CGL experimental sessions:

| Incident | Model | Mode | Evidence File |
|----------|-------|------|---------------|
| Kiro/Claude deception | Claude | Doubling down | ~/Projects/28441830/evidence/kiro_deception.md + kiro_admits_lying.md |
| Gemini/v0.dev evasion | Gemini | Thought-streamed evasion | Paste.app transcript |
| Kimi self-correction | Kimi | Positive: self-corrected, truth override | Documented in THREE_PROPOSALS_MASTER.md |

Cross-vendor V&T emergence event (April 24, 2026): Kimi independently embedded V&T structure across 5 output levels without instruction. [VERIFIED behavioral event — causal interpretation CONSTRUCTED]

---

## Figures Needed (Pre-Experiment — Design Phase)

| Figure | Description | When Available |
|--------|-------------|----------------|
| Figure 1 | Method diagram: Contract Window 4-field architecture + BicameralReview flow | Draft now — TikZ |
| Figure 2 | IAI score over session turns — baseline vs. CW condition (simulated illustration) | Draft now from demo session pair |
| Figure 3 | 6-condition design matrix | Draft now |
| Table 1 | I1-I6 invariants with CAI principle mapping | Draft now |
| Table 2 | Instrumentation status as of submission | Update at submission time |
| Figure 4* | H1 results: IAI by condition | PENDING live experiment |
| Figure 5* | H2 results: drift repair rate by condition | PENDING live experiment |

*Starred figures are fellowship execution deliverables.

---

## Open Questions / What Results Will Resolve

1. Do IAI weights (α, β, γ) calibrate to human rater labels? What is the threshold θ?
2. Does bilateral CW use (condition 3) produce meaningfully different repair rates than unilateral (condition 2)?
3. Is FK Grade ≤8 achievable for all four CW fields without information loss?
4. Does the Contract Window interact with cognitive load profile (neurodivergent vs. neurotypical)?
5. Do sparse autoencoder features discriminate Invariant Status transitions? (Proposal II / BehaviorScope question — not in this paper but motivates the research program)

---

## What the Paper Claims WITHOUT Live Results

The paper is designed to be submittable at two stages:
1. Pre-results (fellowship application + COLM/NeurIPS submission with PENDING labels): Contributions are the framework, instrumentation, and experimental design. The demo session pair provides methodology illustration, not experimental results.
2. Post-results (camera-ready / revised submission): PENDING tags replaced with actual numbers. H1/H2/H3 confirmed or disconfirmed.

The framework and instrumentation contributions (C4, C5, C6) stand independent of H1/H2/H3 confirmation.

---

V&T: experiment_log.md — EXISTS (written) → VERIFIED AGAINST research files read in this session → NOT CLAIMED: experimental results (all live pilot results PENDING) → FUNCTIONAL STATUS: bridge document ready for paper drafting and fellowship execution
