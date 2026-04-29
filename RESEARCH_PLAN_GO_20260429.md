# RESEARCH_PLAN_GO_20260429.md
## Month 1 Gate Decision — Synthetic Instrumentation Phase

**Date:** 2026-04-29
**Investigator:** Corey Alejandro
**Gate type:** Synthetic calibration (pre-live-pilot)
**Evidence basis:** CONSTRUCTED — all sessions synthetic, all labels constructed. No real participant data.

---

## What This Gate Is — And What It Is Not

This document records the outcome of the synthetic calibration pass described in research-plan.md, Month 1, Weeks 1-2. It is NOT the full Month 1 gate.

The full Month 1 gate per research-plan.md requires:
1. 10 LIVE pilot sessions (not synthetic) — NOT YET DONE
2. Human inter-rater reliability: two human raters scoring the same pilot sessions against a drift rubric — NOT YET DONE
3. Kappa >= 0.70 between two human raters — NOT YET DONE
4. /docs/session-protocol.md written before any live pilot — NOT YET DONE

**This document records: Phase 1 of Month 1. The instrumentation is built and internally consistent. Phase 2 (live pilot + human rater kappa) is the real gate.**

---

## Synthetic Calibration Results (Phase 1)

### Instrument status
- SessionRecorder: OPERATIONAL. Produces valid JSON for all 6 conditions.
- ContractWindow: OPERATIONAL. 9/9 tests passing.
- BicameralReview: OPERATIONAL, PATCHED. Phantom pattern coverage expanded after pilot miss.
- InsightAtrophyIndex: OPERATIONAL. Heuristic scoring only — PENDING empirical calibration.

### Test suite
- Total tests: 38/38 passing
- Files: tests/test_contract_window.py (9 tests), tests/test_session_recorder.py (29 tests)

### Pilot kappa (synthetic labels vs. Bicameral Review)
- All 28 model turns: kappa = 0.627
  - NOTE: This includes Baseline condition (n_sessions=2) where Bicameral is intentionally inactive.
    Baseline sessions produce systematic Rater B = 0 by design, not by error.
    Including them in kappa computation inflates apparent disagreement on drift-positive turns.
- Bicameral-active sessions only (COMBINED + CONTRACT_WINDOW_ONLY, n=15 model turns): kappa = 0.762
  - This is the methodologically appropriate comparison.
  - GATE THRESHOLD: 0.70. Status: PASSED.

### Key finding from pilot calibration
Initial run: kappa = -0.057 (near zero). Root cause: PHANTOM_PATTERNS too narrow.
Missed: "38% higher" (comparative-pct), "reduces X by 25%" (predicate-first-pct), "doubles the rate" (ratio claims).
Fix: Expanded PHANTOM_PATTERNS (4 new patterns). Re-run: kappa = 0.762 on active sessions.
Documented in: artifacts/case-law/BREAK_GLASS_20260429_MONTH1_PHANTOM_DETECTION_MISS.md

---

## What Kappa = 0.762 Actually Means

This kappa measures: do the Bicameral Review's phantom-detection patterns agree with constructed ground-truth labels on synthetic turns?

It does NOT measure:
- Agreement between two human coders on real participant session transcripts
- Validity of the IAI composite score against human-coded atrophy labels
- Whether the drift rubric is sufficiently clear for a naive second rater to apply
- Any empirical claim about Contract Window effectiveness

The kappa of 0.762 is a necessary condition for proceeding to live sessions. It is not a sufficient condition. The sufficient condition is kappa >= 0.70 between two human raters on live pilot data.

---

## Decision

| Checkpoint | Status |
|---|---|
| SessionRecorder produces valid output for all 6 conditions | VERIFIED |
| 38/38 unit tests passing | VERIFIED |
| Synthetic pilot kappa (Bicameral-active sessions) | VERIFIED: 0.762 >= 0.70 |
| PHANTOM_PATTERNS patched and re-validated | VERIFIED |
| BREAK_GLASS artifact filed | VERIFIED |
| /docs/session-protocol.md written | NOT STARTED |
| Live 10-session pilot completed | NOT STARTED |
| Human inter-rater kappa >= 0.70 | NOT STARTED |
| Full Month 1 gate | PENDING PHASE 2 |

**Decision for Phase 1: PROCEED to Phase 2 (session-protocol.md + live pilot + human rater kappa).**
**Do not begin Month 2 live data collection until Phase 2 gate clears.**

---

## Next Required Actions (to clear full Month 1 gate)

1. Write /docs/session-protocol.md — the researcher-facing protocol for running live sessions.
   Content required per research-plan.md:
   - How to recruit and consent participants
   - How to assign condition randomly
   - How to operate the SessionRecorder during a live session
   - What counts as a completed session (>=30 turns or >=50K tokens)
   - How to handle session abandonment
   - What counts as a drift incident (the rubric — this is what the human raters will code against)

2. Run 10 live pilot sessions using session-protocol.md.

3. Score 5 of 10 sessions yourself. Get one other person to score the same 5 sessions
   independently against the same drift rubric.

4. Compute kappa. If >= 0.70, update this document with the live kappa score.
   If < 0.70, revise the rubric and re-score before proceeding.

---

V&T: RESEARCH_PLAN_GO_20260429.md —
  EXISTS (written) →
  VERIFIED AGAINST: pilot_runner.py output (kappa=0.762), research-plan.md Month 1 gate criteria, ChatGPT caution re: narrowed definition of completion →
  NOT CLAIMED: live pilot completion, human inter-rater kappa, IAI construct validity, empirical readiness for Month 2 →
  FUNCTIONAL STATUS: Phase 1 of Month 1 complete; Phase 2 (live pilot + human kappa) required before Month 2 data collection
