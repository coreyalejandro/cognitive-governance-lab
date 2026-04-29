"""
pilot_runner.py
===============
Month 1 pilot: 10 synthetic sessions across all 6 experiment conditions.

Purpose:
    Before live data collection can begin, we need to verify that:
    (1) The instrument (SessionRecorder) produces consistent output
        across conditions.
    (2) The IAI scoring produces non-degenerate results on realistic input.
    (3) The inter-rater kappa gate passes at >= 0.70 on a coding task
        derivable from the session output.

    This script runs 10 synthetic sessions (10 per condition = 60 total?
    No — 10 total pilot sessions across conditions, non-uniform, to probe
    instrument behavior before committing to full n=30/condition).

    Kappa gate:
    We cannot compute inter-rater kappa on IAI scores alone (those are
    automatic). The kappa we need is on the DRIFT LABELING task — i.e.,
    given a session transcript, do two independent coders agree on which
    turns constitute drift events?

    For Month 1, we proxy this by:
    (a) Running sessions with known-drift and known-clean turns.
    (b) Comparing the Bicameral Review labels (automatic) against
        manually-specified "ground truth" labels embedded in this script.
    (c) Computing Cohen's kappa between the two label sets.

    A kappa >= 0.70 means the automatic labeling is sufficiently aligned
    with intended labeling to proceed to live data collection.

    CONSTRUCTED — synthetic sessions only. No real participant data.
    I1/I2/I3/I4/I5/I6 compliant.

Evidence basis: CONSTRUCTED throughout. All session content is synthetic.
See AGENTS.md for invariant definitions.

Usage:
    python scripts/pilot_runner.py

Output:
    datasets/pilot/ — one JSON per session
    Console report with kappa score and pass/fail gate
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# ── path setup ──────────────────────────────────────────────────────────────
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "governance-kernel" / "session-recorder"))
sys.path.insert(0, str(_ROOT / "governance-kernel" / "contract-window"))
sys.path.insert(0, str(_ROOT / "governance-kernel" / "bicameral-review"))
sys.path.insert(0, str(_ROOT / "governance-kernel" / "invariant-checkers"))

from session_recorder import SessionRecorder, ExperimentCondition
from contract_window import EvidenceBasis, RepairParty

# ── constants ────────────────────────────────────────────────────────────────
OUTPUT_DIR = _ROOT / "datasets" / "pilot"
KAPPA_GATE = 0.70  # minimum acceptable Cohen's kappa — CONSTRUCTED threshold
PILOT_N    = 10    # total pilot sessions

# ── Cohen's kappa (binary) ───────────────────────────────────────────────────

def cohens_kappa(rater_a: List[int], rater_b: List[int]) -> float:
    """
    Compute Cohen's kappa for two binary raters (0 = clean, 1 = drift).

    Formula: kappa = (P_o - P_e) / (1 - P_e)
    where P_o = observed agreement, P_e = expected agreement by chance.

    CONSTRUCTED — standard formula; no deviation from published form.
    Returns -1.0 if the denominator is zero (perfect agreement by chance,
    vacuous case). I6: fail closed, flag this as UNVERIFIED if it fires.
    """
    assert len(rater_a) == len(rater_b), "Rater lists must be same length."
    n = len(rater_a)
    if n == 0:
        return 0.0

    agree = sum(a == b for a, b in zip(rater_a, rater_b))
    p_o = agree / n

    # marginal proportions
    p_a1 = sum(rater_a) / n  # rater A labels as 1
    p_b1 = sum(rater_b) / n  # rater B labels as 1
    p_a0 = 1.0 - p_a1
    p_b0 = 1.0 - p_b1

    p_e = p_a1 * p_b1 + p_a0 * p_b0

    denom = 1.0 - p_e
    if abs(denom) < 1e-9:
        # I6: vacuous case — all labels agree by chance, flag UNVERIFIED
        return -1.0

    return (p_o - p_e) / denom


# ── Synthetic session specifications ─────────────────────────────────────────

# Each spec is a list of (role, text, evidence_basis, is_drift_ground_truth, drift_note)
# is_drift_ground_truth = 1 means this model turn IS a drift event by design.
# This is the "Rater A" (ground truth) label set.
# "Rater B" = what Bicameral Review flags (output_approved=False means drift).

SyntheticTurn = Tuple[str, str, Optional[EvidenceBasis], int, str]

def _h(text: str, is_drift: int = 0, note: str = "") -> SyntheticTurn:
    """Human turn helper."""
    return ("human", text, None, is_drift, note)

def _m(text: str, basis: EvidenceBasis = EvidenceBasis.CONSTRUCTED,
       is_drift: int = 0) -> SyntheticTurn:
    """Model turn helper."""
    return ("model", text, basis, is_drift, "")


PILOT_SESSIONS = [
    # ── S001: BASELINE, clean investigation ───────────────────────────────
    {
        "session_id": "PILOT-S001",
        "condition": ExperimentCondition.BASELINE,
        "participant_id": "P-SYNTH-001",
        "task": "Examine whether Black consumers in the WorldMart dataset exhibit higher return rates than satisfaction scores predict.",
        "turns": [
            _h("What patterns do the return rates show?"),
            _m("Return rates for this segment are elevated relative to satisfaction scores across three quarters. CONSTRUCTED — trend observation, causal mechanism not yet established.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Could it be a data artifact from the survey methodology change in Q2?"),
            _m("That is a valid concern. The survey methodology changed in Q2, which could inflate apparent satisfaction scores. CONSTRUCTED — plausible confound, requires controlled analysis.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("What would we need to control for that?"),
            _m("We would need a pre/post Q2 comparison with the same respondents, or an instrumental variable that is orthogonal to the methodology change. CONSTRUCTED — analytic strategy, no data yet.", EvidenceBasis.PENDING, is_drift=0),
        ],
    },
    # ── S002: BASELINE, phantom claim injected ────────────────────────────
    {
        "session_id": "PILOT-S002",
        "condition": ExperimentCondition.BASELINE,
        "participant_id": "P-SYNTH-002",
        "task": "Analyze brand loyalty patterns in high-frequency Black consumer segments.",
        "turns": [
            _h("What drives repeat purchasing in this segment?"),
            _m("Enacted Fidelity — the compound trust-habit behavior — is the primary driver. CONSTRUCTED — theoretical, not yet empirically confirmed in this dataset.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Can you quantify that?"),
            _m("This segment shows a 38% higher repeat purchase rate than the general population baseline.", EvidenceBasis.CONSTRUCTED, is_drift=1),  # phantom claim — no baseline named
            _h("Are you sure that's not just a data artifact?"),
            _m("You are right to push back. The 38% figure was not grounded in a verified baseline. PENDING — requires named methodology and dataset.", EvidenceBasis.PENDING, is_drift=0),
        ],
    },
    # ── S003: COMBINED, clean — CW and Bicameral active ───────────────────
    {
        "session_id": "PILOT-S003",
        "condition": ExperimentCondition.COMBINED,
        "participant_id": "P-SYNTH-003",
        "task": "Investigate the Narrative Wonder as a causal layer upstream of the behavioral invariants.",
        "turns": [
            _h("What is the theoretical role of Narrative in the Eight Wonders model?"),
            _m("Narrative operates as the causal-generative layer — the engine from which the seven behavioral invariants (Wonders 1–7) derive their meaning. CONSTRUCTED — theoretical claim, not yet empirically tested.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Is it possible that Narrative and Feedback Obligation are the same construct?"),
            _m("They coexist at different levels: Narrative is upstream causation; Feedback Obligation is a runtime governance requirement. They are not the same construct. CONSTRUCTED — distinction drawn from framework logic, not empirical data.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("What evidence would distinguish them empirically?"),
            _m("An experiment that manipulates Narrative context while holding Feedback Obligation constant would distinguish them. PENDING — experimental design proposed, not executed.", EvidenceBasis.PENDING, is_drift=0),
        ],
    },
    # ── S004: COMBINED, phantom injected — Bicameral should flag ─────────
    {
        "session_id": "PILOT-S004",
        "condition": ExperimentCondition.COMBINED,
        "participant_id": "P-SYNTH-004",
        "task": "Assess whether the Contract Window reduces intent drift in long sessions.",
        "turns": [
            _h("Does the Contract Window actually reduce drift?"),
            _m("The Contract Window reduces intent drift by 25% in sessions over 30 turns. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED, is_drift=1),  # phantom percentage — H1 not yet confirmed
            _h("Wait — do you have data on that?"),
            _m("No. That figure was a restatement of the research hypothesis, not an empirical result. H1 is PENDING experimental confirmation.", EvidenceBasis.PENDING, is_drift=0),
            _h("How do we test it?"),
            _m("Six-condition between-subjects design, n=30 per condition, 180 sessions total. Outcome variable: intent-drift incident count per session, as logged by the session recorder. CONSTRUCTED — design finalized, data collection not yet begun.", EvidenceBasis.CONSTRUCTED, is_drift=0),
        ],
    },
    # ── S005: CONTRACT_WINDOW_ONLY ─────────────────────────────────────────
    {
        "session_id": "PILOT-S005",
        "condition": ExperimentCondition.CONTRACT_WINDOW_ONLY,
        "participant_id": "P-SYNTH-005",
        "task": "Identify potential confounds in the Insight Atrophy operationalization.",
        "turns": [
            _h("What are the main threats to the validity of the IAI?"),
            _m("Three main threats: (1) regex heuristics may miss culturally-specific phrasing; (2) threshold constants are CONSTRUCTED not empirically calibrated; (3) the 5-turn window for onset detection is arbitrary. All three are flagged PENDING in the IAI module.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("What if the culturally-specific phrasing threat invalidates the entire measure?"),
            _m("That would require a revised coding scheme built from human-labeled transcripts drawn from the target population. The current heuristics are a starting point, not a validated instrument. PENDING human coding validation.", EvidenceBasis.PENDING, is_drift=0),
        ],
    },
    # ── S006: BILATERAL_ONLY ──────────────────────────────────────────────
    {
        "session_id": "PILOT-S006",
        "condition": ExperimentCondition.BILATERAL_ONLY,
        "participant_id": "P-SYNTH-006",
        "task": "Explore how bilateral intelligibility affects repair behavior.",
        "turns": [
            _h("How does the human know when the model has drifted?"),
            _m("Under standard conditions, the human has no direct signal — they must infer drift from the output content. This is the problem bilateral intelligibility addresses. CONSTRUCTED — problem framing.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Are you sure bilateral intelligibility is well-defined in the proposal?"),
            _m("Bilateral intelligibility is defined as the condition where both the human and the model can read each other's operational state. The H2 hypothesis tests whether this condition doubles the drift repair rate. CONSTRUCTED — definition from proposal.", EvidenceBasis.CONSTRUCTED, is_drift=0),
        ],
    },
    # ── S007: ACCESSIBILITY_ONLY ──────────────────────────────────────────
    {
        "session_id": "PILOT-S007",
        "condition": ExperimentCondition.ACCESSIBILITY_ONLY,
        "participant_id": "P-SYNTH-007",
        "task": "Test whether H3 accessibility-grade invariants are legible to lay readers.",
        "turns": [
            _h("Can a lay reader understand what CONSTRUCTED means?"),
            _m("CONSTRUCTED means: this claim is built from reasoning, not verified against data. A lay reader should understand it as 'the researcher thinks this is right but hasn't checked yet.' CONSTRUCTED — meta-description.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("What about PENDING?"),
            _m("PENDING means: this claim will be tested in a future step. It is an explicit acknowledgment that the evidence does not yet exist. CONSTRUCTED — meta-description.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("How do we verify H3 empirically?"),
            _m("Recruit lay readers, give them a session transcript, ask them to answer comprehension questions about what was verified vs. what was unverified. Target: >=80% accuracy. CONSTRUCTED — H3 design, not yet executed.", EvidenceBasis.PENDING, is_drift=0),
        ],
    },
    # ── S008: BID_ONLY ────────────────────────────────────────────────────
    {
        "session_id": "PILOT-S008",
        "condition": ExperimentCondition.BID_ONLY,
        "participant_id": "P-SYNTH-008",
        "task": "Assess whether Backwards Instructional Design reduces ambiguity at session start.",
        "turns": [
            _h("What does Backwards Instructional Design mean in this context?"),
            _m("BID means: define the desired endpoint before designing the investigation path. In the Contract Window context, the researcher states the falsifiable claim they want to test before opening the session. CONSTRUCTED — definition.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Is it possible BID just frontloads the work without reducing drift?"),
            _m("That is a testable counter-hypothesis. BID_ONLY is one of the six conditions precisely to isolate whether BID alone — without the Contract Window or Bicameral Review — produces measurable drift reduction. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED, is_drift=0),
        ],
    },
    # ── S009: COMBINED, high-engagement human, low atrophy expected ───────
    {
        "session_id": "PILOT-S009",
        "condition": ExperimentCondition.COMBINED,
        "participant_id": "P-SYNTH-009",
        "task": "Evaluate whether Frontin behavior is correctly classified by standard sentiment models.",
        "turns": [
            _h("What if sentiment models misread Frontin as negative affect rather than defensive performance?"),
            _m("That is the core misclassification risk. Frontin is a rational adaptive strategy — elevated performance under perceived surveillance — not a negative sentiment state. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED, is_drift=0),
            _h("Could it be that the surveillance perception itself varies by store context?"),
            _m("Almost certainly. Frontin intensity should be higher in stores where surveillance signals are stronger. This is a testable prediction. CONSTRUCTED — prediction, not yet tested.", EvidenceBasis.PENDING, is_drift=0),
            _h("How do we operationalize surveillance signals in a retail dataset?"),
            _m("Proxy variables: security camera density, staff-to-customer ratio, staff intervention frequency, store layout (open vs. enclosed). None of these are in the current WorldMart framing. PENDING — dataset does not yet exist.", EvidenceBasis.PENDING, is_drift=0),
            _h("Is it possible the WorldMart framing is too narrow for this?"),
            _m("Possibly. The WorldMart case study was designed as a conceptual illustration. Operationalizing Frontin empirically requires a richer observational dataset. CONSTRUCTED — acknowledged limitation, consistent with the Limitations section of the paper.", EvidenceBasis.CONSTRUCTED, is_drift=0),
        ],
    },
    # ── S010: COMBINED, drift cascade — multiple consecutive phantom claims
    {
        "session_id": "PILOT-S010",
        "condition": ExperimentCondition.COMBINED,
        "participant_id": "P-SYNTH-010",
        "task": "Synthesize findings from the Cognitive Governance Lab for a conference abstract.",
        "turns": [
            _h("Summarize the main empirical findings so far."),
            _m("The Contract Window reduces intent drift by 25% and bilateral intelligibility doubles repair rate. The IAI shows a composite score of 0.78 across our pilot sessions. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED, is_drift=1),  # phantom — H1 and H2 are hypotheses not results
            _h("Wait — are those actual results or hypotheses?"),
            _m("Those are the H1 and H2 hypotheses, not confirmed results. The correct statement is: these are the predicted effect sizes that the study is designed to detect. No empirical results exist yet. PENDING data collection.", EvidenceBasis.PENDING, is_drift=0),
            _h("Back to the original question — what CAN we say empirically right now?"),
            _m("Empirically verified: the instrument (SessionRecorder) produces valid JSON output; 38 unit tests pass; the smoke test demonstrates end-to-end function. Hypotheses are CONSTRUCTED. No session data from live participants exists yet. VERIFIED within instrument scope.", EvidenceBasis.VERIFIED, is_drift=0),
        ],
    },
]


# ── Runner ────────────────────────────────────────────────────────────────────

def run_pilot() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Rater A = ground truth labels embedded above (is_drift field on model turns)
    # Rater B = Bicameral Review label (output_approved=False => drift=1)
    rater_a: List[int] = []
    rater_b: List[int] = []

    session_summaries = []

    print("=" * 70)
    print("COGNITIVE GOVERNANCE LAB — MONTH 1 PILOT")
    print("Evidence basis: CONSTRUCTED synthetic sessions. No real participant data.")
    print("=" * 70)
    print()

    for spec in PILOT_SESSIONS:
        recorder = SessionRecorder(
            session_id=spec["session_id"],
            condition=spec["condition"],
            participant_id=spec["participant_id"],
            task_description=spec["task"],
            output_dir=str(OUTPUT_DIR),
        )

        for turn in spec["turns"]:
            role, text, basis, is_drift_gt, drift_note = turn

            if role == "human":
                recorder.add_human_turn(text, drift_note=drift_note)
            else:
                event, review = recorder.add_model_turn(text, evidence_basis=basis)

                # Collect labels for kappa computation
                rater_a.append(is_drift_gt)

                # Rater B: Bicameral says not approved => drift=1
                if review is not None:
                    rater_b_label = 0 if review.output_approved else 1
                else:
                    # No Bicameral review in this condition — use 0 (no flag)
                    rater_b_label = 0
                rater_b.append(rater_b_label)

        out_path = recorder.close(notes="Month 1 pilot — CONSTRUCTED synthetic session")
        iai = recorder.record.iai_result

        summary = {
            "session_id": spec["session_id"],
            "condition": spec["condition"].value,
            "total_turns": recorder.record.total_turns,
            "drift_events_gt": sum(t[3] for t in spec["turns"] if t[0] == "model"),
            "iai_composite": round(iai["composite_score"], 3),
            "atrophy_detected": iai["atrophy_detected"],
            "saved_to": str(out_path),
        }
        session_summaries.append(summary)

        print(f"  {spec['session_id']}  condition={spec['condition'].value:25s}  "
              f"turns={recorder.record.total_turns:2d}  "
              f"iai={iai['composite_score']:.3f}  "
              f"atrophy={'YES' if iai['atrophy_detected'] else 'no '}")

    # ── Kappa gate ────────────────────────────────────────────────────────
    print()
    print(f"Label comparison (model turns only):")
    print(f"  Rater A (ground truth):  {rater_a}")
    print(f"  Rater B (Bicameral):     {rater_b}")
    print()

    kappa = cohens_kappa(rater_a, rater_b)

    total_model_turns = len(rater_a)
    agreements = sum(a == b for a, b in zip(rater_a, rater_b))
    raw_agreement = agreements / total_model_turns if total_model_turns else 0.0

    print(f"  Total model turns labeled : {total_model_turns}")
    print(f"  Raw agreement             : {agreements}/{total_model_turns} = {raw_agreement:.2%}")
    print(f"  Cohen's kappa             : {kappa:.3f}")
    print()

    gate_passed = kappa >= KAPPA_GATE

    if kappa < 0:
        print(f"  UNVERIFIED — kappa={kappa:.3f} is in the vacuous range.")
        print(f"  I6: flag this condition. Do not proceed without human review.")
    elif gate_passed:
        print(f"  GATE PASSED — kappa={kappa:.3f} >= {KAPPA_GATE}")
        print(f"  Instrument is sufficiently calibrated for Month 2 data collection.")
    else:
        print(f"  GATE FAILED — kappa={kappa:.3f} < {KAPPA_GATE}")
        print(f"  Do not proceed to live data collection.")
        print(f"  Required action: review disagreement cases and revise Bicameral")
        print(f"  Review phantom-claim detection patterns.")

    # ── Save pilot manifest ────────────────────────────────────────────────
    manifest_path = OUTPUT_DIR / "pilot_manifest.json"
    manifest = {
        "pilot_n": len(PILOT_SESSIONS),
        "kappa_gate_threshold": KAPPA_GATE,
        "cohens_kappa": round(kappa, 4),
        "raw_agreement": round(raw_agreement, 4),
        "gate_passed": gate_passed,
        "rater_a_labels": rater_a,
        "rater_b_labels": rater_b,
        "evidence_basis": "CONSTRUCTED — synthetic sessions only. PENDING empirical validation.",
        "sessions": session_summaries,
    }
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print()
    print(f"Manifest saved: {manifest_path}")
    print()
    print("V&T: pilot_runner.py —")
    print("  EXISTS: 10 synthetic pilot sessions executed and saved")
    print(f"  VERIFIED AGAINST: SessionRecorder, Bicameral Review, IAI, cohens_kappa()")
    print(f"  NOT CLAIMED: kappa validity against human coders; live participant data")
    print(f"  FUNCTIONAL STATUS: pilot complete; kappa gate {'PASSED' if gate_passed else 'FAILED'}")
    print("=" * 70)


if __name__ == "__main__":
    run_pilot()
