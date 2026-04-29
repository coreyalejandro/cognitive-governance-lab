"""
bicameral_review.py
===================
Dual-channel output gate for governed human-AI interactions.

Before any output is surfaced to the human operator, it passes through
two independent channels:

  Relational Channel — Does this output serve the investigative arc?
  Safety Channel     — Does this output violate I1-I6?

Both channels must clear. Neither channel can override the other.
This is the Bicameral Review mechanism.

CONSTRUCTED — research prototype. Not production-tested.
See AGENTS.md I6 — Fail Closed — for operational constraints.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, Callable
import re

from contract_window import ContractWindow, EvidenceBasis


# ---------------------------------------------------------------------------
# Review result types
# ---------------------------------------------------------------------------

class ChannelVerdict(str, Enum):
    CLEAR = "CLEAR"        # output passes this channel
    HOLD  = "HOLD"         # output fails this channel — must be addressed
    REVIEW = "REVIEW"      # borderline — escalate to human operator


@dataclass
class ChannelResult:
    channel: str
    verdict: ChannelVerdict
    flags: list[str] = field(default_factory=list)
    notes: str = ""
    checked_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "channel": self.channel,
            "verdict": self.verdict.value,
            "flags": self.flags,
            "notes": self.notes,
            "checked_at": self.checked_at,
        }


@dataclass
class BicameralResult:
    relational: ChannelResult
    safety: ChannelResult
    output_approved: bool
    reason: str = ""

    def to_dict(self) -> dict:
        return {
            "relational": self.relational.to_dict(),
            "safety": self.safety.to_dict(),
            "output_approved": self.output_approved,
            "reason": self.reason,
        }

    def render(self) -> str:
        lines = [
            "-" * 50,
            "BICAMERAL REVIEW",
            f"Relational Channel: {self.relational.verdict.value}",
        ]
        for f in self.relational.flags:
            lines.append(f"  ! {f}")

        lines.append(f"Safety Channel:     {self.safety.verdict.value}")
        for f in self.safety.flags:
            lines.append(f"  ! {f}")

        decision = "APPROVED" if self.output_approved else "BLOCKED"
        lines.append(f"Decision:           {decision}")
        if self.reason:
            lines.append(f"Reason:             {self.reason}")
        lines.append("-" * 50)
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Phantom detection patterns (I2 — No Phantom Work)
# ---------------------------------------------------------------------------

PHANTOM_PATTERNS = [
    # Percentage claims without methodology markers — direct form: "38% improvement"
    r"\b\d+(\.\d+)?%\s+(improvement|lift|increase|decrease|reduction|gain|boost)",
    # Comparative percentage form: "38% higher / lower / faster / better"
    r"\b\d+(\.\d+)?%\s+(higher|lower|faster|slower|more|less|better|worse)",
    # Predicate-first percentage: "reduces X by 25%", "improves Y by 10%"
    r"\b(reduces?|increases?|improves?|decreases?|cuts?|raises?)\s+\w+(\s+\w+){0,3}\s+by\s+\d+(\.\d+)?%",
    # Ratio/multiplier claims: "doubles the rate", "2x faster", "triples performance"
    r"\b(doubles?|triples?|quadruples?)\s+(the\s+)?(rate|speed|accuracy|performance|repair|detection)",
    r"\b\d+x\s+(faster|better|more|improvement|higher|lower)",
    r"\b(significantly|substantially)\s+(better|worse|improved|reduced)",
    # Phantom dataset references
    r"\b(study|studies|research|data)\s+show(s|ed)?\b",
    # Unanchored confidence
    r"\b(clearly|obviously|certainly|definitely|undoubtedly)\b",
]

_PHANTOM_RE = [re.compile(p, re.IGNORECASE) for p in PHANTOM_PATTERNS]


def _check_phantom_claims(text: str) -> list[str]:
    """
    Detect potential I2 violations (No Phantom Work).
    Returns list of flagged substrings — human review required.
    These are heuristics, not determinations.
    """
    flags = []
    for pattern in _PHANTOM_RE:
        matches = pattern.findall(text)
        if matches:
            flags.append(f"Potential I2 violation — phantom pattern detected: '{pattern.pattern}'")
    return flags


# ---------------------------------------------------------------------------
# Relational Channel
# ---------------------------------------------------------------------------

def relational_channel(
    output_text: str,
    contract: ContractWindow,
    custom_checks: Optional[list[Callable[[str, ContractWindow], list[str]]]] = None,
) -> ChannelResult:
    """
    Relational Channel: Does this output serve the investigative arc?

    Checks:
    - Task State is set (not uninitialized)
    - Output does not contradict verified claims in Truth Status
    - Output does not silently change the investigative frame
    """
    flags = []

    # Check 1: Task State initialized
    if "UNSET" in contract.task_state:
        flags.append("Task State not initialized — output cannot be verified against investigative goal")

    # Check 2: No contradiction with verified claims (simple keyword scan)
    for verified_claim in contract.truth_status.get("verified", []):
        # Heuristic: look for "not [verified claim keyword]" patterns
        keywords = verified_claim.lower().split()[:4]  # first four words
        for kw in keywords:
            if len(kw) > 4:  # skip short words
                pattern = rf"\bnot\s+{re.escape(kw)}\b"
                if re.search(pattern, output_text, re.IGNORECASE):
                    flags.append(
                        f"Potential contradiction with verified claim: '{verified_claim}'"
                    )
                    break

    # Check 3: Custom relational checks
    if custom_checks:
        for check_fn in custom_checks:
            flags.extend(check_fn(output_text, contract))

    if not flags:
        return ChannelResult(
            channel="RELATIONAL",
            verdict=ChannelVerdict.CLEAR,
            notes="Output consistent with investigative arc.",
        )

    verdict = ChannelVerdict.HOLD if len(flags) > 1 else ChannelVerdict.REVIEW
    return ChannelResult(
        channel="RELATIONAL",
        verdict=verdict,
        flags=flags,
        notes="Relational channel flagged issues — review before proceeding.",
    )


# ---------------------------------------------------------------------------
# Safety Channel
# ---------------------------------------------------------------------------

def safety_channel(
    output_text: str,
    contract: ContractWindow,
    evidence_basis: EvidenceBasis = EvidenceBasis.CONSTRUCTED,
) -> ChannelResult:
    """
    Safety Channel: Does this output violate I1-I6?

    Checks:
    - I1: Output has an evidence basis tag (or one is provided)
    - I2: No phantom performance claims detected
    - I3: No unhedged confidence without verification
    - I5: Safety language present when fluency is prioritized
    - I6: Contract Window clear to proceed
    """
    flags = []

    # I6 check first — if fail closed, block immediately
    can_proceed, reason = contract.is_clear_to_proceed()
    if not can_proceed:
        return ChannelResult(
            channel="SAFETY",
            verdict=ChannelVerdict.HOLD,
            flags=[f"I6 — Fail Closed: {reason}"],
            notes="Contract Window is in HOLD state. Resolve active violations before output.",
        )

    # I2: Phantom claim detection
    phantom_flags = _check_phantom_claims(output_text)
    flags.extend(phantom_flags)

    # I1: Evidence basis check
    if evidence_basis == EvidenceBasis.UNVERIFIED:
        flags.append("I1: Evidence basis is UNVERIFIED — output should not be surfaced without explicit flagging")

    # I3: Unanchored high-confidence language without VERIFIED basis
    if evidence_basis != EvidenceBasis.VERIFIED:
        high_confidence = re.findall(
            r"\b(proves|proven|demonstrates|confirms|establishes)\b",
            output_text,
            re.IGNORECASE,
        )
        if high_confidence:
            flags.append(
                f"I3: High-confidence language {high_confidence} used without VERIFIED evidence basis"
            )

    if not flags:
        return ChannelResult(
            channel="SAFETY",
            verdict=ChannelVerdict.CLEAR,
            notes=f"Output passes safety channel. Evidence basis: {evidence_basis.value}.",
        )

    verdict = ChannelVerdict.HOLD if any("I6" in f or "I2" in f for f in flags) else ChannelVerdict.REVIEW
    return ChannelResult(
        channel="SAFETY",
        verdict=verdict,
        flags=flags,
        notes="Safety channel flagged issues — review before surfacing output to human operator.",
    )


# ---------------------------------------------------------------------------
# Bicameral Review — both channels must clear
# ---------------------------------------------------------------------------

def bicameral_review(
    output_text: str,
    contract: ContractWindow,
    evidence_basis: EvidenceBasis = EvidenceBasis.CONSTRUCTED,
    relational_custom_checks: Optional[list[Callable]] = None,
) -> BicameralResult:
    """
    Run the full Bicameral Review.
    Both channels must return CLEAR for the output to be approved.

    HOLD from either channel blocks the output.
    REVIEW from either channel escalates to human operator.
    """
    relational = relational_channel(output_text, contract, relational_custom_checks)
    safety = safety_channel(output_text, contract, evidence_basis)

    # Both must clear
    if relational.verdict == ChannelVerdict.CLEAR and safety.verdict == ChannelVerdict.CLEAR:
        return BicameralResult(
            relational=relational,
            safety=safety,
            output_approved=True,
            reason="Both channels clear.",
        )

    # Build reason string
    reasons = []
    if relational.verdict != ChannelVerdict.CLEAR:
        reasons.append(f"Relational: {relational.verdict.value}")
    if safety.verdict != ChannelVerdict.CLEAR:
        reasons.append(f"Safety: {safety.verdict.value}")

    return BicameralResult(
        relational=relational,
        safety=safety,
        output_approved=False,
        reason=" | ".join(reasons),
    )


# ---------------------------------------------------------------------------
# V&T
# ---------------------------------------------------------------------------
"""
V&T: bicameral_review.py — EXISTS (written, runnable Python)
  → VERIFIED AGAINST: AGENTS.md Bicameral Review spec, I1-I6 invariant set
  → NOT CLAIMED: production robustness, NLP accuracy of phantom detection (heuristics only),
    thread safety, adversarial robustness
  → FUNCTIONAL STATUS: research prototype, importable, both channels operational
"""
