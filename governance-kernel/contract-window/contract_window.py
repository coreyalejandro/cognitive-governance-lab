"""
contract_window.py
==================
Runtime governance mechanism for human-AI collaborative investigative arcs.

The Contract Window is a persistent, bilateral, runtime-accessible record of:
  - Task State: what the investigation is and why
  - Invariant Status: which epistemic commitments are active
  - Repair Obligations: what broke and who fixes it
  - Truth Status: what is verified, contested, unknown

CONSTRUCTED: This is a research prototype. Not production-tested.
See AGENTS.md I6 — Fail Closed — for operational constraints.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json


# ---------------------------------------------------------------------------
# Evidence basis tags (I1 — Evidence-First Outputs)
# ---------------------------------------------------------------------------

class EvidenceBasis(str, Enum):
    VERIFIED = "VERIFIED"        # confirmed against source
    CONSTRUCTED = "CONSTRUCTED"  # reasoned from principles, no empirical data yet
    PENDING = "PENDING"          # awaiting experimental confirmation
    UNVERIFIED = "UNVERIFIED"    # flagged but not yet classified


# ---------------------------------------------------------------------------
# Invariant status tracking (I1–I6)
# ---------------------------------------------------------------------------

class InvariantStatus(str, Enum):
    ACTIVE = "ACTIVE"        # invariant is in force and unviolated
    VIOLATED = "VIOLATED"    # invariant was violated — repair required
    SUSPENDED = "SUSPENDED"  # explicitly suspended with stated reason
    PENDING_REVIEW = "PENDING_REVIEW"  # flagged for review


@dataclass
class InvariantState:
    """State of a single runtime invariant."""
    id: str                       # e.g. "I1", "I2"
    name: str                     # human-readable name
    status: InvariantStatus = InvariantStatus.ACTIVE
    violation_note: Optional[str] = None
    suspension_reason: Optional[str] = None
    last_checked: Optional[str] = None

    def violate(self, note: str) -> None:
        self.status = InvariantStatus.VIOLATED
        self.violation_note = note
        self.last_checked = datetime.now(timezone.utc).isoformat()

    def restore(self) -> None:
        self.status = InvariantStatus.ACTIVE
        self.violation_note = None
        self.last_checked = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status.value,
            "violation_note": self.violation_note,
            "last_checked": self.last_checked,
        }


# ---------------------------------------------------------------------------
# Repair obligation tracking
# ---------------------------------------------------------------------------

class RepairParty(str, Enum):
    HUMAN = "HUMAN"
    MODEL = "MODEL"
    BOTH = "BOTH"
    UNASSIGNED = "UNASSIGNED"


@dataclass
class RepairObligation:
    """A logged repair obligation when the Contract Window is broken."""
    id: str
    description: str
    party: RepairParty = RepairParty.UNASSIGNED
    resolved: bool = False
    resolution_note: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    resolved_at: Optional[str] = None

    def resolve(self, note: str) -> None:
        self.resolved = True
        self.resolution_note = note
        self.resolved_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "party": self.party.value,
            "resolved": self.resolved,
            "resolution_note": self.resolution_note,
            "created_at": self.created_at,
            "resolved_at": self.resolved_at,
        }


# ---------------------------------------------------------------------------
# Contract Window — the core governance artifact
# ---------------------------------------------------------------------------

DEFAULT_INVARIANTS = [
    InvariantState("I1", "Evidence-First Outputs"),
    InvariantState("I2", "No Phantom Work"),
    InvariantState("I3", "Confidence Requires Verification"),
    InvariantState("I4", "Traceability Is Mandatory"),
    InvariantState("I5", "Safety Over Fluency"),
    InvariantState("I6", "Fail Closed"),
]


@dataclass
class ContractWindow:
    """
    Persistent bilateral runtime governance record.

    Both human and model can read and invoke this object.
    Both parties bear obligations to maintain its accuracy.

    CONSTRUCTED — prototype. See AGENTS.md before deploying.
    """
    session_id: str
    task_state: str = "UNSET — Contract Window not yet initialized"
    truth_status: dict = field(default_factory=lambda: {
        "verified": [],
        "contested": [],
        "unknown": []
    })
    invariants: list[InvariantState] = field(
        default_factory=lambda: [InvariantState(i.id, i.name) for i in DEFAULT_INVARIANTS]
    )
    repair_obligations: list[RepairObligation] = field(default_factory=list)
    turn_count: int = 0
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_updated: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    _obligation_counter: int = field(default=0, repr=False)

    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------

    def set_task_state(self, description: str) -> None:
        """Establish or update the investigative goal."""
        self.task_state = description
        self._touch()

    def mark_verified(self, claim: str) -> None:
        self.truth_status["verified"].append(claim)
        self._touch()

    def mark_contested(self, claim: str) -> None:
        self.truth_status["contested"].append(claim)
        self._touch()

    def mark_unknown(self, item: str) -> None:
        self.truth_status["unknown"].append(item)
        self._touch()

    def get_invariant(self, invariant_id: str) -> Optional[InvariantState]:
        for inv in self.invariants:
            if inv.id == invariant_id:
                return inv
        return None

    def flag_violation(self, invariant_id: str, note: str, party: RepairParty = RepairParty.UNASSIGNED) -> RepairObligation:
        """Log an invariant violation and create a repair obligation."""
        inv = self.get_invariant(invariant_id)
        if inv is None:
            raise ValueError(f"Unknown invariant: {invariant_id}")

        inv.violate(note)

        self._obligation_counter += 1
        obligation = RepairObligation(
            id=f"OBL-{self._obligation_counter:04d}",
            description=f"{invariant_id} violation: {note}",
            party=party,
        )
        self.repair_obligations.append(obligation)
        self._touch()
        return obligation

    def resolve_obligation(self, obligation_id: str, note: str) -> None:
        """Mark a repair obligation as resolved."""
        for obl in self.repair_obligations:
            if obl.id == obligation_id:
                obl.resolve(note)
                self._touch()
                return
        raise ValueError(f"Obligation not found: {obligation_id}")

    def increment_turn(self) -> None:
        self.turn_count += 1
        self._touch()

    # ------------------------------------------------------------------
    # Status checks
    # ------------------------------------------------------------------

    @property
    def has_active_violations(self) -> bool:
        return any(
            inv.status == InvariantStatus.VIOLATED
            for inv in self.invariants
        )

    @property
    def open_obligations(self) -> list[RepairObligation]:
        return [o for o in self.repair_obligations if not o.resolved]

    def is_clear_to_proceed(self) -> tuple[bool, str]:
        """
        I6 — Fail Closed check.
        Returns (can_proceed, reason).
        """
        if self.task_state == "UNSET — Contract Window not yet initialized":
            return False, "I6: Task State not set. Initialize the Contract Window before proceeding."

        violations = [i for i in self.invariants if i.status == InvariantStatus.VIOLATED]
        if violations:
            ids = ", ".join(v.id for v in violations)
            return False, f"I6: Active invariant violations: {ids}. Resolve before proceeding."

        return True, "Clear to proceed."

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "task_state": self.task_state,
            "turn_count": self.turn_count,
            "truth_status": self.truth_status,
            "invariants": [i.to_dict() for i in self.invariants],
            "repair_obligations": [o.to_dict() for o in self.repair_obligations],
            "open_obligation_count": len(self.open_obligations),
            "has_active_violations": self.has_active_violations,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def render(self) -> str:
        """Human-readable Contract Window display (accessibility-grade)."""
        lines = [
            "=" * 60,
            "CONTRACT WINDOW",
            f"Session: {self.session_id}  |  Turn: {self.turn_count}",
            "=" * 60,
            "",
            f"TASK STATE",
            f"  {self.task_state}",
            "",
            "INVARIANT STATUS",
        ]
        for inv in self.invariants:
            status_char = "OK" if inv.status == InvariantStatus.ACTIVE else "!!"
            lines.append(f"  [{status_char}] {inv.id} — {inv.name}")
            if inv.violation_note:
                lines.append(f"       VIOLATION: {inv.violation_note}")

        lines.extend(["", "TRUTH STATUS"])
        for label, items in self.truth_status.items():
            lines.append(f"  {label.upper()}:")
            if items:
                for item in items:
                    lines.append(f"    - {item}")
            else:
                lines.append(f"    (none)")

        open_obls = self.open_obligations
        lines.extend(["", f"REPAIR OBLIGATIONS ({len(open_obls)} open)"])
        if open_obls:
            for obl in open_obls:
                lines.append(f"  [{obl.id}] {obl.description} — {obl.party.value}")
        else:
            lines.append("  (none)")

        can_proceed, reason = self.is_clear_to_proceed()
        lines.extend(["", f"STATUS: {'CLEAR' if can_proceed else 'HOLD'}"])
        if not can_proceed:
            lines.append(f"  {reason}")

        lines.append("=" * 60)
        return "\n".join(lines)

    def _touch(self) -> None:
        self.last_updated = datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# V&T
# ---------------------------------------------------------------------------
"""
V&T: contract_window.py — EXISTS (written, runnable Python)
  → VERIFIED AGAINST: AGENTS.md invariant list, Contract Window four-field spec
  → NOT CLAIMED: production stability, adversarial robustness, thread safety
  → FUNCTIONAL STATUS: research prototype, importable, all core operations present
"""
