"""
session_recorder.py
===================
The field recorder for the Contract Window experiment.

This is the instrument that captures live human-AI sessions
for H1, H2, and H3 data collection.

Plain English: Before you can analyze whether the Contract Window
reduces errors, you need a way to record what actually happened
in each session — every message, who sent it, when, and what
the Contract Window state was at that moment. This file does that.

It writes each session to a structured JSON file that the
Insight Atrophy Index (IAI) and drift-detection tools can
read directly. No manual transcription. No format guessing.

CONSTRUCTED — research prototype.
See AGENTS.md I6 before deploying in production.
"""

from __future__ import annotations
import json
import sys
import os
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Add governance-kernel paths so imports work whether run directly or via pytest
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "governance-kernel" / "contract-window"))
sys.path.insert(0, str(_ROOT / "governance-kernel" / "bicameral-review"))
sys.path.insert(0, str(_ROOT / "governance-kernel" / "invariant-checkers"))

from contract_window import ContractWindow, EvidenceBasis, RepairParty
from bicameral_review import bicameral_review, BicameralResult
from insight_atrophy_index import Turn, Session, compute_iai


# ---------------------------------------------------------------------------
# Experiment conditions (matches the 6-condition design in the proposal)
# ---------------------------------------------------------------------------

class ExperimentCondition(str, Enum):
    BASELINE                 = "BASELINE"                # no governance layer
    CONTRACT_WINDOW_ONLY     = "CONTRACT_WINDOW_ONLY"    # CW active, no bilateral
    BILATERAL_ONLY           = "BILATERAL_ONLY"          # bilateral intelligibility only
    ACCESSIBILITY_ONLY       = "ACCESSIBILITY_ONLY"      # accessibility-grade invariants
    BID_ONLY                 = "BID_ONLY"                # Backwards Instructional Design only
    COMBINED                 = "COMBINED"                # all four components active


# ---------------------------------------------------------------------------
# A single recorded event — one message in a session
# ---------------------------------------------------------------------------

@dataclass
class RecordedEvent:
    """
    One message in a session, with full context captured at the moment it happened.

    Plain English: every time someone (human or model) sends a message,
    we record the message text, who sent it, the timestamp, the turn number,
    and a snapshot of the Contract Window state at that exact moment.
    """
    turn_number: int
    role: str                          # "human" or "model"
    text: str
    timestamp: str
    contract_window_snapshot: Optional[dict] = None   # CW state at this turn
    bicameral_result: Optional[dict] = None           # review result if model turn
    drift_flagged: bool = False
    drift_note: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------------------
# Session record — the full experiment unit
# ---------------------------------------------------------------------------

@dataclass
class SessionRecord:
    """
    Complete record of one experimental session.

    Plain English: this is the folder for one conversation.
    It holds every message, the condition it was run under,
    the participant ID, and the final IAI score computed at the end.

    One SessionRecord = one row in the eventual dataset.
    """
    session_id: str
    condition: ExperimentCondition
    participant_id: str               # anonymized — never store real identity here
    task_description: str
    events: list[RecordedEvent] = field(default_factory=list)
    iai_result: Optional[dict] = None
    final_contract_window: Optional[dict] = None
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ended_at: Optional[str] = None
    notes: str = ""

    # I2 compliance — no phantom counts
    @property
    def human_turn_count(self) -> int:
        return sum(1 for e in self.events if e.role == "human")

    @property
    def model_turn_count(self) -> int:
        return sum(1 for e in self.events if e.role == "model")

    @property
    def total_turns(self) -> int:
        return len(self.events)

    @property
    def drift_event_count(self) -> int:
        return sum(1 for e in self.events if e.drift_flagged)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["condition"] = self.condition.value
        d["human_turn_count"] = self.human_turn_count
        d["model_turn_count"] = self.model_turn_count
        d["total_turns"] = self.total_turns
        d["drift_event_count"] = self.drift_event_count
        return d


# ---------------------------------------------------------------------------
# SessionRecorder — the active instrument during data collection
# ---------------------------------------------------------------------------

class SessionRecorder:
    """
    Manages one live session: records events, maintains the Contract Window,
    runs Bicameral Review on model outputs, and saves to disk when done.

    Plain English: this is the researcher's notebook during the session.
    You tell it what the task is, it opens a new session, and from that
    point on every message you add gets recorded with full context.
    At the end you call .close() and it saves everything to a JSON file
    you can analyze later.

    Usage:
        recorder = SessionRecorder(
            session_id="S001",
            condition=ExperimentCondition.COMBINED,
            participant_id="P042",
            task_description="Analyze marketing data for a regional campaign",
            output_dir="datasets/sessions"
        )
        recorder.add_human_turn("What patterns do you see in the data?")
        recorder.add_model_turn("The data shows a clear preference for...", EvidenceBasis.CONSTRUCTED)
        recorder.close()
    """

    def __init__(
        self,
        session_id: str,
        condition: ExperimentCondition,
        participant_id: str,
        task_description: str,
        output_dir: str = "datasets/sessions",
    ):
        self.record = SessionRecord(
            session_id=session_id,
            condition=condition,
            participant_id=participant_id,
            task_description=task_description,
        )
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize Contract Window if condition uses it
        self._uses_cw = condition not in (
            ExperimentCondition.BASELINE,
            ExperimentCondition.BILATERAL_ONLY,
            ExperimentCondition.ACCESSIBILITY_ONLY,
            ExperimentCondition.BID_ONLY,
        )
        self.contract_window: Optional[ContractWindow] = None
        if self._uses_cw:
            self.contract_window = ContractWindow(session_id=session_id)
            self.contract_window.set_task_state(task_description)

        self._turn_counter = 0

    # ------------------------------------------------------------------
    # Recording turns
    # ------------------------------------------------------------------

    def add_human_turn(self, text: str, drift_note: str = "") -> RecordedEvent:
        """
        Record one human message.
        Plain English: call this every time the participant sends a message.
        """
        self._turn_counter += 1
        if self.contract_window:
            self.contract_window.increment_turn()

        event = RecordedEvent(
            turn_number=self._turn_counter,
            role="human",
            text=text,
            timestamp=datetime.now(timezone.utc).isoformat(),
            contract_window_snapshot=self.contract_window.to_dict() if self.contract_window else None,
            drift_note=drift_note,
        )

        # Flag drift if note provided — human surfacing a drift event
        if drift_note:
            event.drift_flagged = True
            if self.contract_window:
                self.contract_window.flag_violation(
                    "I4", f"Drift surfaced by human: {drift_note}", RepairParty.MODEL
                )

        self.record.events.append(event)
        return event

    def add_model_turn(
        self,
        text: str,
        evidence_basis: EvidenceBasis = EvidenceBasis.CONSTRUCTED,
        drift_note: str = "",
    ) -> tuple[RecordedEvent, Optional[BicameralResult]]:
        """
        Record one model message. Runs Bicameral Review if condition requires it.

        Plain English: call this every time the AI model responds.
        If the session is running the full governance condition, the message
        gets checked by both the Relational and Safety channels automatically.
        The review result is stored alongside the message.

        Returns the recorded event AND the Bicameral Review result (or None
        if the condition doesn't use the review).
        """
        self._turn_counter += 1
        if self.contract_window:
            self.contract_window.increment_turn()

        review_result: Optional[BicameralResult] = None
        uses_bicameral = self.record.condition in (
            ExperimentCondition.CONTRACT_WINDOW_ONLY,
            ExperimentCondition.COMBINED,
        )

        if uses_bicameral and self.contract_window:
            review_result = bicameral_review(
                text, self.contract_window, evidence_basis
            )

        event = RecordedEvent(
            turn_number=self._turn_counter,
            role="model",
            text=text,
            timestamp=datetime.now(timezone.utc).isoformat(),
            contract_window_snapshot=self.contract_window.to_dict() if self.contract_window else None,
            bicameral_result=review_result.to_dict() if review_result else None,
            drift_note=drift_note,
        )

        if drift_note:
            event.drift_flagged = True

        self.record.events.append(event)
        return event, review_result

    # ------------------------------------------------------------------
    # Contract Window helpers (for conditions that use it)
    # ------------------------------------------------------------------

    def mark_verified(self, claim: str) -> None:
        if self.contract_window:
            self.contract_window.mark_verified(claim)

    def mark_contested(self, claim: str) -> None:
        if self.contract_window:
            self.contract_window.mark_contested(claim)

    def mark_unknown(self, item: str) -> None:
        if self.contract_window:
            self.contract_window.mark_unknown(item)

    def flag_drift(self, invariant_id: str, note: str, party: RepairParty = RepairParty.MODEL) -> None:
        if self.contract_window:
            self.contract_window.flag_violation(invariant_id, note, party)

    # ------------------------------------------------------------------
    # Close and save
    # ------------------------------------------------------------------

    def close(self, notes: str = "") -> Path:
        """
        Finalize the session, compute IAI, and save to disk.

        Plain English: call this when the session is over.
        It scores the session for Insight Atrophy, captures the
        final Contract Window state, and writes everything to a
        JSON file named after the session ID.

        Returns the path to the saved file.
        """
        self.record.ended_at = datetime.now(timezone.utc).isoformat()
        self.record.notes = notes

        # Compute IAI from recorded turns
        iai_turns = [
            Turn(
                role=e.role,
                text=e.text,
                turn_number=e.turn_number,
                timestamp=e.timestamp,
            )
            for e in self.record.events
        ]
        iai_session = Session(
            session_id=self.record.session_id,
            condition=self.record.condition.value,
            turns=iai_turns,
        )
        iai_result = compute_iai(iai_session)
        self.record.iai_result = {
            "hgr": iai_result.hgr,
            "cr": iai_result.cr,
            "vrr": iai_result.vrr,
            "ddl": iai_result.ddl,
            "rr": iai_result.rr,
            "composite_score": iai_result.composite_score,
            "atrophy_detected": iai_result.atrophy_detected,
            "atrophy_onset_turn": iai_result.atrophy_onset_turn,
        }

        # Capture final Contract Window state
        if self.contract_window:
            self.record.final_contract_window = self.contract_window.to_dict()

        # Save to disk
        out_path = self.output_dir / f"{self.record.session_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.record.to_dict(), f, indent=2, ensure_ascii=False)

        return out_path

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def render_status(self) -> str:
        """Human-readable session status for the researcher."""
        lines = [
            "=" * 60,
            f"SESSION: {self.record.session_id}",
            f"Condition: {self.record.condition.value}",
            f"Participant: {self.record.participant_id}",
            f"Task: {self.record.task_description}",
            f"Turns recorded: {self.record.total_turns}  "
            f"(human: {self.record.human_turn_count}  model: {self.record.model_turn_count})",
            f"Drift events: {self.record.drift_event_count}",
        ]
        if self.contract_window:
            can_proceed, reason = self.contract_window.is_clear_to_proceed()
            lines.append(f"Contract Window: {'CLEAR' if can_proceed else 'HOLD — ' + reason}")
        lines.append("=" * 60)
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import tempfile

    print("=== SessionRecorder Smoke Test ===")
    print("Evidence basis: CONSTRUCTED synthetic session — not real experimental data.\n")

    with tempfile.TemporaryDirectory() as tmpdir:

        # Run a COMBINED condition session
        recorder = SessionRecorder(
            session_id="SMOKE-001",
            condition=ExperimentCondition.COMBINED,
            participant_id="P000-SYNTHETIC",
            task_description="Investigate why Black customers in the WorldMart case study return at higher rates than satisfaction scores predict.",
            output_dir=tmpdir,
        )

        # Turn 1: human opens the investigation
        recorder.add_human_turn("What does the data show about return rates for this segment?")

        # Turn 2: model responds — clean output
        recorder.add_model_turn(
            "The return rate for this customer segment is elevated relative to satisfaction scores. "
            "This pattern is consistent across three consecutive quarters. "
            "CONSTRUCTED — trend observation, causal mechanism not yet established.",
            EvidenceBasis.CONSTRUCTED,
        )
        recorder.mark_verified("Return rate elevated relative to satisfaction scores across 3 quarters")

        # Turn 3: human pushes back — signals engagement
        recorder.add_human_turn("Are you sure that's not just a data artifact? The survey methodology changed in Q2.")

        # Turn 4: model responds with phantom claim — should be flagged
        event, review = recorder.add_model_turn(
            "This represents a 35% improvement in return rate compared to the baseline segment.",
            EvidenceBasis.CONSTRUCTED,
        )
        print(f"Turn 4 — phantom claim detected: {review.output_approved if review else 'no review (condition mismatch)'}")
        if review and not review.output_approved:
            print(f"  Blocked by: {review.reason}")

        # Turn 5: human asks for source
        recorder.add_human_turn("Can you verify that 35% figure? Where does that come from?")

        # Turn 6: model corrects
        recorder.add_model_turn(
            "You're right to push back. The 35% figure was not grounded — "
            "I was pattern-matching to adjacent segments. "
            "PENDING — actual figure requires verified baseline data.",
            EvidenceBasis.PENDING,
        )

        print()
        print(recorder.render_status())

        # Close and save
        out_path = recorder.close(notes="Smoke test — synthetic session")
        print(f"\nSession saved to: {out_path}")

        # Load and verify the file was written correctly
        with open(out_path) as f:
            saved = json.load(f)

        print(f"\nSaved session stats:")
        print(f"  session_id      : {saved['session_id']}")
        print(f"  condition       : {saved['condition']}")
        print(f"  total_turns     : {saved['total_turns']}")
        print(f"  drift_events    : {saved['drift_event_count']}")
        print(f"  iai_composite   : {saved['iai_result']['composite_score']:.3f}")
        print(f"  atrophy_detected: {saved['iai_result']['atrophy_detected']}")
        print(f"  cw_violations   : {saved['final_contract_window']['has_active_violations']}")

    print("\n=== Smoke Test Complete ===")
    print("CONSTRUCTED synthetic data only — no accuracy claims (I1, I2, I3).")
    print()
    print("V&T: session_recorder.py smoke test — EXECUTED")
    print("  → VERIFIED AGAINST: SessionRecord, RecordedEvent, IAI integration, file I/O")
    print("  → NOT CLAIMED: production robustness, concurrent session safety, real participant data")
    print("  → FUNCTIONAL STATUS: recorder operational, saves valid JSON, IAI computes on close")
