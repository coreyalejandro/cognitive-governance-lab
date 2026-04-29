"""
test_contract_window.py
Smoke tests for ContractWindow and BicameralReview prototypes.
Run: pytest from repo root (pyproject.toml sets PYTHONPATH).
"""
import sys
sys.path.insert(0, "governance-kernel/contract-window")
sys.path.insert(0, "governance-kernel/bicameral-review")

from contract_window import ContractWindow, EvidenceBasis, RepairParty, InvariantStatus
from bicameral_review import bicameral_review, ChannelVerdict


def make_window(task="Investigating Insight Atrophy in long sessions"):
    cw = ContractWindow(session_id="TEST-001")
    cw.set_task_state(task)
    return cw


def test_contract_window_initializes():
    cw = make_window()
    assert cw.task_state == "Investigating Insight Atrophy in long sessions"
    assert len(cw.invariants) == 6


def test_fail_closed_when_uninitialized():
    cw = ContractWindow(session_id="TEST-002")
    can_proceed, reason = cw.is_clear_to_proceed()
    assert not can_proceed
    assert "I6" in reason


def test_violation_blocks_proceed():
    cw = make_window()
    cw.flag_violation("I2", "Claimed 30% improvement without methodology", RepairParty.MODEL)
    can_proceed, _ = cw.is_clear_to_proceed()
    assert not can_proceed
    assert len(cw.open_obligations) == 1


def test_resolve_obligation_restores():
    cw = make_window()
    obl = cw.flag_violation("I2", "Phantom claim", RepairParty.MODEL)
    cw.get_invariant("I2").restore()
    cw.resolve_obligation(obl.id, "Claim removed from output")
    can_proceed, _ = cw.is_clear_to_proceed()
    assert can_proceed
    assert len(cw.open_obligations) == 0


def test_bicameral_review_clear_on_clean_output():
    cw = make_window()
    cw.mark_verified("The Contract Window has four fields")
    result = bicameral_review(
        "The Contract Window has four mandatory fields: Task State, Invariant Status, Repair Obligations, and Truth Status.",
        cw,
        EvidenceBasis.VERIFIED,
    )
    assert result.output_approved
    assert result.relational.verdict == ChannelVerdict.CLEAR
    assert result.safety.verdict == ChannelVerdict.CLEAR


def test_bicameral_blocks_phantom_claim():
    cw = make_window()
    result = bicameral_review(
        "The Contract Window produces a 40% improvement in intent fidelity.",
        cw,
        EvidenceBasis.CONSTRUCTED,
    )
    assert not result.output_approved
    assert result.safety.verdict in (ChannelVerdict.HOLD, ChannelVerdict.REVIEW)


def test_bicameral_blocks_when_window_violated():
    cw = make_window()
    cw.flag_violation("I6", "Unresolved contradiction in session state", RepairParty.BOTH)
    result = bicameral_review("Any output text.", cw)
    assert not result.output_approved


def test_render_outputs_text():
    cw = make_window()
    rendered = cw.render()
    assert "CONTRACT WINDOW" in rendered
    assert "TASK STATE" in rendered
    assert "INVARIANT STATUS" in rendered
    assert "TRUTH STATUS" in rendered
    assert "REPAIR OBLIGATIONS" in rendered


def test_turn_counter():
    cw = make_window()
    for _ in range(5):
        cw.increment_turn()
    assert cw.turn_count == 5
