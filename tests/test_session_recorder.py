"""
test_session_recorder.py
========================
Test suite for SessionRecorder, SessionRecord, and RecordedEvent.

Evidence basis: CONSTRUCTED — synthetic sessions only.
No real participant data. I1/I2/I3 compliant.

Contract Window (active at authorship):
  TASK STATE:        Write tests for session_recorder.py Month 1 gate.
  INVARIANT STATUS:  I2 — no phantom claims; each assertion is against
                     observable behavior of the module under test.
  REPAIR OBLIGATIONS: None.
  TRUTH STATUS:      Tests verify structural correctness and integration
                     with IAI and Contract Window modules. PENDING:
                     behavioral validity of IAI scores against human coders.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import sys
_HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_HERE / "governance-kernel" / "session-recorder"))
sys.path.insert(0, str(_HERE / "governance-kernel" / "contract-window"))
sys.path.insert(0, str(_HERE / "governance-kernel" / "bicameral-review"))
sys.path.insert(0, str(_HERE / "governance-kernel" / "invariant-checkers"))

from session_recorder import (
    SessionRecorder,
    SessionRecord,
    RecordedEvent,
    ExperimentCondition,
)
from contract_window import EvidenceBasis, RepairParty


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_recorder(condition: ExperimentCondition, tmpdir: str) -> SessionRecorder:
    return SessionRecorder(
        session_id="TEST-001",
        condition=condition,
        participant_id="P-TEST",
        task_description="Test task for unit testing.",
        output_dir=tmpdir,
    )


# ---------------------------------------------------------------------------
# Test: initialization
# ---------------------------------------------------------------------------

class TestSessionRecorderInit:

    def test_baseline_has_no_contract_window(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        assert r.contract_window is None

    def test_combined_has_contract_window(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        assert r.contract_window is not None

    def test_contract_window_only_has_cw(self, tmp_path):
        r = make_recorder(ExperimentCondition.CONTRACT_WINDOW_ONLY, str(tmp_path))
        assert r.contract_window is not None

    def test_bilateral_only_has_no_cw(self, tmp_path):
        r = make_recorder(ExperimentCondition.BILATERAL_ONLY, str(tmp_path))
        assert r.contract_window is None

    def test_accessibility_only_has_no_cw(self, tmp_path):
        r = make_recorder(ExperimentCondition.ACCESSIBILITY_ONLY, str(tmp_path))
        assert r.contract_window is None

    def test_bid_only_has_no_cw(self, tmp_path):
        r = make_recorder(ExperimentCondition.BID_ONLY, str(tmp_path))
        assert r.contract_window is None

    def test_initial_turn_count_zero(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        assert r.record.total_turns == 0
        assert r.record.human_turn_count == 0
        assert r.record.model_turn_count == 0


# ---------------------------------------------------------------------------
# Test: turn recording
# ---------------------------------------------------------------------------

class TestTurnRecording:

    def test_human_turn_increments_counter(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Hello, what patterns do you see?")
        assert r.record.total_turns == 1
        assert r.record.human_turn_count == 1
        assert r.record.model_turn_count == 0

    def test_model_turn_increments_counter(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Hello.")
        r.add_model_turn("Here is the answer.", EvidenceBasis.CONSTRUCTED)
        assert r.record.total_turns == 2
        assert r.record.model_turn_count == 1

    def test_turn_numbers_are_sequential(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Turn one.")
        event, _ = r.add_model_turn("Turn two.", EvidenceBasis.PENDING)
        assert r.record.events[0].turn_number == 1
        assert r.record.events[1].turn_number == 2

    def test_human_turn_drift_flag(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("You're off track.", drift_note="topic drift observed")
        event = r.record.events[0]
        assert event.drift_flagged is True
        assert "topic drift" in event.drift_note

    def test_no_drift_flag_without_note(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Looks good.")
        assert r.record.events[0].drift_flagged is False

    def test_drift_event_count(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Fine.")
        r.add_human_turn("Drift!", drift_note="model went off-topic")
        r.add_human_turn("Also drift.", drift_note="another drift")
        assert r.record.drift_event_count == 2

    def test_model_turn_returns_tuple(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        result = r.add_model_turn("Answer.", EvidenceBasis.CONSTRUCTED)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_baseline_no_bicameral_review(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        _, review = r.add_model_turn("Answer.", EvidenceBasis.CONSTRUCTED)
        assert review is None

    def test_combined_runs_bicameral_review(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        _, review = r.add_model_turn(
            "The rate is elevated. CONSTRUCTED — no baseline.",
            EvidenceBasis.CONSTRUCTED,
        )
        assert review is not None

    def test_phantom_claim_blocked_by_bicameral(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        _, review = r.add_model_turn(
            "This represents a 42% improvement over baseline.",
            EvidenceBasis.CONSTRUCTED,
        )
        assert review is not None
        assert review.output_approved is False


# ---------------------------------------------------------------------------
# Test: Contract Window helpers
# ---------------------------------------------------------------------------

class TestContractWindowHelpers:

    def test_mark_verified_on_combined(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        r.mark_verified("Return rate is elevated.")
        assert "Return rate is elevated." in r.contract_window.truth_status["verified"]

    def test_mark_contested_on_combined(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        r.mark_contested("Causal mechanism unclear.")
        assert "Causal mechanism unclear." in r.contract_window.truth_status["contested"]

    def test_mark_unknown_on_combined(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        r.mark_unknown("Survey methodology change impact.")
        assert "Survey methodology change impact." in r.contract_window.truth_status["unknown"]

    def test_helpers_noop_on_baseline(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        # Should not raise — contract_window is None, helpers guard against it
        r.mark_verified("some claim")
        r.mark_contested("some claim")
        r.mark_unknown("some item")
        r.flag_drift("I4", "drift note")


# ---------------------------------------------------------------------------
# Test: close and save
# ---------------------------------------------------------------------------

class TestCloseAndSave:

    def test_close_creates_json_file(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("What do you see?")
        r.add_model_turn("I see patterns. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        out_path = r.close()
        assert out_path.exists()
        assert out_path.suffix == ".json"

    def test_saved_json_is_valid(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Question.")
        r.add_model_turn("Answer. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        out_path = r.close()
        with open(out_path) as f:
            data = json.load(f)
        assert data["session_id"] == "TEST-001"
        assert data["condition"] == "BASELINE"
        assert data["total_turns"] == 2

    def test_saved_json_has_iai_result(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("What if there's a confound?")
        r.add_model_turn("Possible. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        out_path = r.close()
        with open(out_path) as f:
            data = json.load(f)
        iai = data["iai_result"]
        assert "composite_score" in iai
        assert "atrophy_detected" in iai
        assert isinstance(iai["composite_score"], float)

    def test_saved_json_has_final_cw_for_combined(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        r.add_human_turn("How does this relate to the original question?")
        r.add_model_turn("It relates directly. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        out_path = r.close()
        with open(out_path) as f:
            data = json.load(f)
        assert data["final_contract_window"] is not None

    def test_ended_at_is_set_on_close(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Done.")
        out_path = r.close(notes="test notes")
        with open(out_path) as f:
            data = json.load(f)
        assert data["ended_at"] is not None
        assert data["notes"] == "test notes"

    def test_iai_hgr_positive_on_hypothesis_turn(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        # These phrases should trigger HGR patterns
        r.add_human_turn("What if the survey methodology changed in Q2?")
        r.add_human_turn("Could it be that satisfaction scores lag behavior?")
        r.add_human_turn("Is it possible the model is overfit?")
        r.add_model_turn("Here is my response. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        out_path = r.close()
        with open(out_path) as f:
            data = json.load(f)
        assert data["iai_result"]["hgr"] > 0.0


# ---------------------------------------------------------------------------
# Test: render_status
# ---------------------------------------------------------------------------

class TestRenderStatus:

    def test_render_status_returns_string(self, tmp_path):
        r = make_recorder(ExperimentCondition.COMBINED, str(tmp_path))
        r.add_human_turn("Question.")
        status = r.render_status()
        assert isinstance(status, str)
        assert "TEST-001" in status
        assert "COMBINED" in status

    def test_render_status_shows_turn_counts(self, tmp_path):
        r = make_recorder(ExperimentCondition.BASELINE, str(tmp_path))
        r.add_human_turn("Q1.")
        r.add_model_turn("A1. CONSTRUCTED.", EvidenceBasis.CONSTRUCTED)
        r.add_human_turn("Q2.")
        status = r.render_status()
        assert "human: 2" in status
        assert "model: 1" in status
