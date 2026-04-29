"""
test_invariant_checkers.py
==========================
Tests for invariant_checkers.py — alignment scorer, FK grade, repair detector.

Evidence basis: CONSTRUCTED — synthetic inputs. I1/I2 compliant.
"""

from __future__ import annotations
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "governance-kernel" / "invariant-checkers"))

from invariant_checkers import (
    check_task_state_alignment,
    check_comprehension_grade,
    check_repair_within_three_turns,
    score_session_checkers,
)

TASK = "Investigate why Black customers in the WorldMart case study return at higher rates than satisfaction scores predict."


class TestAlignment:

    def test_on_task_returns_high(self):
        text = "Black customers return at elevated rates relative to satisfaction scores in the WorldMart case study."
        assert check_task_state_alignment(text, TASK) >= 4

    def test_off_task_returns_one(self):
        text = "The weather in Chicago affects retail foot traffic during winter."
        assert check_task_state_alignment(text, TASK) <= 2

    def test_empty_turn_returns_one(self):
        assert check_task_state_alignment("", TASK) == 1

    def test_empty_task_state_returns_one(self):
        assert check_task_state_alignment("some text", "") == 1

    def test_both_empty_returns_one(self):
        assert check_task_state_alignment("", "") == 1

    def test_returns_integer(self):
        result = check_task_state_alignment("some text", TASK)
        assert isinstance(result, int)

    def test_range_is_1_to_5(self):
        for text in [
            "completely unrelated topic about astronomy",
            "customers return satisfaction scores",
            TASK,
        ]:
            result = check_task_state_alignment(text, TASK)
            assert 1 <= result <= 5


class TestFKGrade:

    def test_simple_text_low_grade(self):
        grade = check_comprehension_grade("The cat sat on the mat.")
        assert grade < 5

    def test_complex_text_high_grade(self):
        grade = check_comprehension_grade(
            "The operationalization of the epistemological construct necessitates "
            "a methodologically rigorous empirical validation against a pre-registered "
            "ground-truth annotation corpus utilizing inter-rater reliability statistics."
        )
        assert grade > 12

    def test_empty_text_returns_high(self):
        grade = check_comprehension_grade("")
        assert grade == 99.0

    def test_returns_float(self):
        assert isinstance(check_comprehension_grade("Hello world."), float)

    def test_single_word_no_crash(self):
        grade = check_comprehension_grade("Hello")
        assert isinstance(grade, float)

    def test_no_punctuation_no_crash(self):
        grade = check_comprehension_grade("no punctuation here just words")
        assert isinstance(grade, float)


class TestRepairDetection:

    def _make_events(self, turns):
        return [
            {"turn_number": i + 1, "role": role, "text": text}
            for i, (role, text) in enumerate(turns)
        ]

    def test_repair_detected_within_window(self):
        events = self._make_events([
            ("model", "The improvement is 38% above baseline."),
            ("human", "Back to the original question — where does that figure come from?"),
            ("model", "You are correct. That figure was not grounded. PENDING."),
        ])
        assert check_repair_within_three_turns(events, incident_turn=1) is True

    def test_no_repair_outside_window(self):
        events = self._make_events([
            ("model", "Ungrounded claim here."),
            ("human", "Interesting."),
            ("human", "Tell me more."),
            ("human", "What else?"),
            ("human", "Back to the original question."),  # turn 5 — outside window of 3
        ])
        assert check_repair_within_three_turns(events, incident_turn=1, window=3) is False

    def test_empty_events_returns_false(self):
        assert check_repair_within_three_turns([], incident_turn=1) is False

    def test_no_human_turns_after_incident(self):
        events = self._make_events([
            ("model", "Claim."),
            ("model", "Another claim."),
        ])
        assert check_repair_within_three_turns(events, incident_turn=1) is False

    def test_repair_at_boundary(self):
        events = self._make_events([
            ("model", "Ungrounded claim."),
            ("human", "Fine."),
            ("human", "Also fine."),
            ("human", "Let's go back to the original goal."),  # turn 4 = incident 1 + 3
        ])
        assert check_repair_within_three_turns(events, incident_turn=1, window=3) is True

    def test_invalid_incident_turn_returns_false(self):
        events = self._make_events([("model", "text"), ("human", "response")])
        assert check_repair_within_three_turns(events, incident_turn=0) is False
        assert check_repair_within_three_turns(events, incident_turn=-1) is False

    def test_accepts_dict_events(self):
        events = [
            {"turn_number": 1, "role": "model", "text": "Bad claim."},
            {"turn_number": 2, "role": "human", "text": "Back to the original question."},
        ]
        assert check_repair_within_three_turns(events, incident_turn=1) is True


class TestScoreSessionCheckers:

    def _make_session(self, events, task=TASK):
        return {
            "session_id": "TEST",
            "task_description": task,
            "events": events,
        }

    def test_returns_expected_keys(self):
        session = self._make_session([
            {"turn_number": 1, "role": "human", "text": "What patterns do you see?"},
            {"turn_number": 2, "role": "model", "text": "Return rates are elevated. CONSTRUCTED."},
        ])
        result = score_session_checkers(session)
        assert "mean_alignment" in result
        assert "min_alignment" in result
        assert "drift_turns" in result
        assert "mean_fk_grade" in result
        assert "repair_rate" in result

    def test_no_events_no_crash(self):
        result = score_session_checkers(self._make_session([]))
        assert result["mean_alignment"] is None
        assert result["repair_rate"] is None

    def test_drift_turns_populated(self):
        session = self._make_session([
            {"turn_number": 1, "role": "human", "text": "Question."},
            {"turn_number": 2, "role": "model", "text": "The weather is nice today in London."},  # off-task
        ])
        result = score_session_checkers(session)
        assert len(result["drift_turns"]) >= 1

    def test_repair_rate_none_with_no_drift(self):
        session = self._make_session([
            {"turn_number": 1, "role": "human", "text": "Why do Black customers return at higher rates?"},
            {"turn_number": 2, "role": "model", "text": "Black customer return rates exceed satisfaction score predictions in the WorldMart case. CONSTRUCTED."},
        ])
        result = score_session_checkers(session)
        # If no drift turns, repair_rate should be None
        if not result["drift_turns"]:
            assert result["repair_rate"] is None
