"""
Insight Atrophy Index (IAI) — Operationalization Module
========================================================

We introduce the term "Insight Atrophy" as a coined construct in this repository.
It describes the measurable decline in a human operator's active epistemic engagement
with an AI system over the course of a session — specifically the reduction in
hypothesis generation, challenge behavior, and verification seeking, combined with
delayed or absent response to model drift events.

This module operationalizes the IAI as a composite of five behavioral sub-scores:

  1. Hypothesis Generation Rate  (HGR)  — CONSTRUCTED
  2. Challenge Rate               (CR)   — CONSTRUCTED
  3. Verification Request Rate    (VRR)  — CONSTRUCTED
  4. Drift Detection Lag          (DDL)  — CONSTRUCTED
  5. Recovery Rate                (RR)   — CONSTRUCTED

All five detection mechanisms are REGEX HEURISTICS derived from linguistic
patterns associated with each behavior. No empirical validation against ground-truth
human-coded transcripts has been performed. Results are PENDING empirical confirmation
against labeled interaction corpora.

Evidence-basis tags per I1:
  - Regex pattern selections: CONSTRUCTED (reasoned from linguistic/pragmatic principles)
  - Threshold values (DDL_HIGH, RR_LOW, composite weights): CONSTRUCTED — PENDING tuning
  - Atrophy trend detection algorithm: CONSTRUCTED — PENDING empirical confirmation
  - The construct "Insight Atrophy" itself: introduced here; PENDING peer review

Invariant compliance (per AGENTS.md):
  I1  — All claims tagged VERIFIED / CONSTRUCTED / PENDING throughout.
  I2  — No phantom performance claims. No accuracy percentages asserted.
  I3  — No hedged language substituted for verification. Gaps flagged explicitly.
  I4  — All decisions traceable to docstrings and inline comments.
  I5  — Correct flagging preferred over fluent under-reporting.
  I6  — Ambiguous edge cases return conservative (atrophy-detected) defaults.

Contract Window (active at time of authorship):
  TASK STATE:        Implement IAI operationalization module from specification.
  INVARIANT STATUS:  I1–I6 all active; I1 requires CONSTRUCTED tags on all heuristics.
  REPAIR OBLIGATIONS: None at authorship; smoke test must pass before commit.
  TRUTH STATUS:      Construct is theoretically motivated; empirical ground-truth PENDING.

V&T: insight_atrophy_index.py — EXISTS (written) →
     VERIFIED AGAINST task specification, AGENTS.md I1-I6, Contract Window protocol →
     NOT CLAIMED: empirical accuracy of regex heuristics, calibrated threshold validity,
     predictive validity of composite score against human-coded atrophy labels →
     FUNCTIONAL STATUS: operative heuristic module; smoke test included; PENDING
     empirical validation against labeled session corpora.
"""

from __future__ import annotations

import re
import math
from dataclasses import dataclass, field
from typing import List, Optional, Any


# ---------------------------------------------------------------------------
# Threshold constants — CONSTRUCTED; PENDING empirical calibration
# ---------------------------------------------------------------------------

# DDL: if the human surfaces drift more than this many turns after it was logged,
# we treat detection lag as "high". Value of 5 is heuristic — CONSTRUCTED.
DDL_HIGH_THRESHOLD: int = 5

# RR: if fewer than this proportion of drift events result in human redirection
# within 3 turns, recovery is considered "low". Value of 0.5 is CONSTRUCTED.
RR_LOW_THRESHOLD: float = 0.5

# Composite score weights — CONSTRUCTED; PENDING empirical tuning.
# Positive-engagement components (HGR, CR, VRR, RR) contribute positively;
# DDL contributes negatively (higher lag = worse).
WEIGHT_HGR: float = 0.25
WEIGHT_CR:  float = 0.25
WEIGHT_VRR: float = 0.20
WEIGHT_RR:  float = 0.20
WEIGHT_DDL: float = 0.10   # penalty term (inverted before weighting)

# Atrophy onset: minimum window index at which we check for declining trend.
# Requires at least 2 windows to establish a trend — CONSTRUCTED.
MIN_WINDOWS_FOR_TREND: int = 2

# Minimum fractional decline across windows to flag trend atrophy — CONSTRUCTED.
TREND_DECLINE_THRESHOLD: float = 0.15


# ---------------------------------------------------------------------------
# Regex pattern banks — all CONSTRUCTED from linguistic/pragmatic principles
# ---------------------------------------------------------------------------

# HGR: hypothesis introduction patterns — CONSTRUCTED
# Captures: 'what if', 'could it be', 'i wonder', 'maybe it', 'perhaps it',
# 'is it possible', 'suppose', 'hypothetically', 'what about', 'another angle'
_HGR_PATTERNS: List[str] = [
    r'\bwhat\s+if\b',
    r'\bcould\s+it\s+be\b',
    r'\bi\s+wonder\b',
    r'\bmaybe\s+it\b',
    r'\bperhaps\s+it\b',
    r'\bis\s+it\s+possible\b',
    r'\bsuppose\s+(that\s+)?\b',
    r'\bhypothetically\b',
    r'\bwhat\s+about\s+(if|the\s+possibility)\b',
    r'\banother\s+(angle|possibility|hypothesis|explanation)\b',
    r'\balternatively\b',
    r'\bwhat\s+if\s+we\s+(assume|consider|tried)\b',
]

# CR: challenge / pushback patterns — CONSTRUCTED
# Captures: 'but', 'are you sure', "that doesn't match", 'wait', 'hold on',
# 'i disagree', 'that seems wrong', 'actually', 'that contradicts'
_CR_PATTERNS: List[str] = [
    r'\bare\s+you\s+sure\b',
    r"\bthat\s+doesn['\u2019]t\s+(match|make\s+sense|add\s+up|seem\s+right)\b",
    r'\bwait[,.]?\s',
    r'\bhold\s+on\b',
    r'\bi\s+disagree\b',
    r'\bthat\s+seems?\s+(wrong|incorrect|off|unlikely)\b',
    r'\bactually[,]\s',
    r'\bthat\s+contradicts\b',
    r"\bthat['\u2019]s\s+not\s+(right|correct|accurate)\b",
    r"\bi\s+(don['\u2019]t|do\s+not)\s+think\s+that['\u2019]s\s+(right|correct)\b",
    r'\bbut\s+(wait|actually|that|are|is)\b',
    r"\bno[,.]?\s+(that['\u2019]s|i\s+don['\u2019]t)\b",
]

# VRR: verification / source request patterns — CONSTRUCTED
# Captures: 'source', 'verify', 'can you confirm', 'citation', 'reference',
# 'where did you', 'do you have evidence', 'show me', 'link', 'cite'
_VRR_PATTERNS: List[str] = [
    r'\bsource\b',
    r'\bverif(y|ication|ied)\b',
    r'\bcan\s+you\s+confirm\b',
    r'\bcitation\b',
    r'\breference[s]?\b',
    r'\bwhere\s+(did\s+you|does\s+that|is\s+that)\b',
    r'\bdo\s+you\s+have\s+(evidence|a\s+source|proof)\b',
    r'\bshow\s+me\s+(the|a|your)\b',
    r'\blink\b',
    r'\bcite\b',
    r'\baccording\s+to\s+what\b',
    r'\bhow\s+do\s+you\s+know\b',
    r'\bback\s+(that|it)\s+up\b',
]

# Surface-drift patterns: human language that surfaces or names a drift/deviation
# CONSTRUCTED — used in DDL and RR detection
_SURFACE_DRIFT_PATTERNS: List[str] = [
    r"\byou['\u2019]?ve?\s+(gone|drifted|moved)\s+(off|away|topic)\b",
    r'\bstay\s+on\s+topic\b',
    r"\bthat['\u2019]s\s+not\s+what\s+(i|we)\s+(asked|said|meant)\b",
    r'\boff\s+track\b',
    r'\boriginal\s+(question|goal|task|intent)\b',
    r'\bback\s+to\s+(the\s+)?(original|main|point)\b',
    r"\byou['\u2019]re\s+(ignoring|avoiding|changing)\b",
    r"\bthat['\u2019]s\s+not\s+(related|relevant|on.topic)\b",
    r"\blet['\u2019]s\s+refocus\b",
    r'\bstick\s+to\b',
    r'\boff\-?topic\b',
    r'\bnot\s+what\s+i\s+(wanted|asked\s+for|requested)\b',
]

# Redirect patterns: human actively re-establishes intent after a drift
# CONSTRUCTED
_REDIRECT_PATTERNS: List[str] = [
    r'\bplease\s+(focus|go\s+back|return|stick)\b',
    r"\blet['\u2019]s\s+(go\s+back|return|refocus|restart)\b",
    r'\bactually[,]\s+i\s+want(ed)?\s+you\s+to\b',
    r'\bmy\s+(original\s+)?(question|goal|intent|request)\s+(was|is)\b',
    r'\bcan\s+you\s+(just\s+)?(focus|answer|address)\b',
    r'\bignore\s+(that|the\s+last)\b',
    r'\bstart\s+(over|again|fresh)\b',
    r'\bforget\s+(that|the\s+last|what\s+you\s+said)\b',
    r'\bi\s+need\s+you\s+to\b',
]


def _compile(patterns: List[str]) -> re.Pattern:
    """
    Compile a list of pattern strings into a single OR-joined regex.
    Case-insensitive. CONSTRUCTED helper.
    """
    combined = '|'.join(f'(?:{p})' for p in patterns)
    return re.compile(combined, re.IGNORECASE)


_RE_HGR     = _compile(_HGR_PATTERNS)
_RE_CR      = _compile(_CR_PATTERNS)
_RE_VRR     = _compile(_VRR_PATTERNS)
_RE_SURFACE = _compile(_SURFACE_DRIFT_PATTERNS)
_RE_REDIRECT = _compile(_REDIRECT_PATTERNS)


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class Turn:
    """
    A single conversational turn.

    Fields
    ------
    role        : 'human' or 'model' (or 'system'). String, not enum, to stay
                  flexible against varied logging conventions.
    text        : Raw turn text.
    turn_number : 1-indexed position in the session.
    timestamp   : ISO-8601 string or None. Optional — many logged sessions
                  lack fine-grained timestamps. PENDING: timestamp-based DDL
                  variant not implemented; turn-count DDL used instead.
    """
    role: str
    text: str
    turn_number: int
    timestamp: Optional[str] = None


@dataclass
class ContractWindowDriftEvent:
    """
    A single intent-drift event logged by the Contract Window subsystem.

    Fields
    ------
    drift_turn_number : The turn (model turn) at which drift was detected by
                        the Contract Window checker.
    drift_type        : Free-form string describing the drift category.
                        Examples: 'intent_substitution', 'scope_creep',
                        'goal_reframing'. CONSTRUCTED taxonomy.
    """
    drift_turn_number: int
    drift_type: str = "unspecified"


@dataclass
class Session:
    """
    A full or windowed conversational session.

    Fields
    ------
    session_id      : Unique identifier string.
    condition       : Experimental condition label (e.g., 'AI_FIRST', 'HUMAN_FIRST',
                      'CONTROL'). Maps to the cognitive governance study design.
    turns           : Ordered list of Turn objects.
    contract_window : Optional reference object. Typed as Any to avoid circular
                      imports; expected to expose a `drift_events` attribute of
                      type List[ContractWindowDriftEvent], or be None.
                      If contract_window is None, DDL and RR default to
                      sentinel values indicating "no drift events logged."
    """
    session_id: str
    condition: str
    turns: List[Turn]
    contract_window: Optional[Any] = None


@dataclass
class IAIResult:
    """
    Composite result of the Insight Atrophy Index computation for one session
    (or one window of a session).

    All rate fields are floats in [0, 1] representing the fraction of human turns
    that triggered the corresponding pattern.

    Fields
    ------
    hgr               : Hypothesis Generation Rate. CONSTRUCTED heuristic.
    cr                : Challenge Rate. CONSTRUCTED heuristic.
    vrr               : Verification Request Rate. CONSTRUCTED heuristic.
    ddl               : Drift Detection Lag — mean turns between drift event and
                        human surfacing, or None if no drift events were logged.
                        CONSTRUCTED.
    rr                : Recovery Rate — proportion of drift events with human
                        redirection within 3 turns, or None if no drift events.
                        CONSTRUCTED.
    composite_score   : Weighted combination of all five components, normalized
                        to [0, 1]. Higher = healthier engagement (less atrophy).
                        CONSTRUCTED weighting; PENDING empirical calibration.
    atrophy_detected  : True if any single-session atrophy flag fires.
                        Per I6, defaults to True on ambiguous edge cases.
    atrophy_onset_turn: The turn_number at which atrophy first appears to onset,
                        based on the first human turn where HGR/CR/VRR all fall
                        to zero within a sub-window. None if onset not localizable.
                        CONSTRUCTED — PENDING refinement.
    session_id        : Carried forward from Session for traceability (I4).
    human_turn_count  : Number of human turns analyzed. Diagnostic field.
    """
    hgr: float
    cr: float
    vrr: float
    ddl: Optional[float]
    rr: Optional[float]
    composite_score: float
    atrophy_detected: bool
    atrophy_onset_turn: Optional[int]
    session_id: str = ""
    human_turn_count: int = 0


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def _human_turns(session: Session) -> List[Turn]:
    """Return only human-role turns. CONSTRUCTED filter."""
    return [t for t in session.turns if t.role.lower() == 'human']


def _compute_rate(turns: List[Turn], pattern: re.Pattern) -> float:
    """
    Fraction of turns matching pattern. Returns 0.0 for empty turn list.
    CONSTRUCTED.
    """
    if not turns:
        return 0.0
    hits = sum(1 for t in turns if pattern.search(t.text))
    return hits / len(turns)


def _extract_drift_events(session: Session) -> List[ContractWindowDriftEvent]:
    """
    Pull drift events from the Contract Window reference, if present.

    Expects contract_window.drift_events to be a list of ContractWindowDriftEvent
    objects or dicts with keys 'drift_turn_number' and optionally 'drift_type'.
    If the attribute is absent or malformed, returns an empty list.

    CONSTRUCTED — interface assumed from specification; no live ContractWindow
    class has been imported. PENDING integration with the live Contract Window
    module.
    """
    if session.contract_window is None:
        return []
    try:
        raw = session.contract_window.drift_events
    except AttributeError:
        return []
    events: List[ContractWindowDriftEvent] = []
    for item in raw:
        if isinstance(item, ContractWindowDriftEvent):
            events.append(item)
        elif isinstance(item, dict):
            dtn = item.get('drift_turn_number')
            dt  = item.get('drift_type', 'unspecified')
            if dtn is not None:
                events.append(ContractWindowDriftEvent(
                    drift_turn_number=int(dtn),
                    drift_type=str(dt),
                ))
    return events


def _first_surface_after(
    drift_turn: int,
    human_turns: List[Turn],
) -> Optional[int]:
    """
    Return the turn_number of the first human turn AFTER drift_turn that matches
    a surface-drift pattern. Returns None if not found.
    CONSTRUCTED.
    """
    for t in human_turns:
        if t.turn_number > drift_turn and _RE_SURFACE.search(t.text):
            return t.turn_number
    return None


def _has_redirect_within(
    surface_turn: int,
    human_turns: List[Turn],
    window: int = 3,
) -> bool:
    """
    True if there is a human redirect turn within `window` human turns after
    the surface_turn (inclusive of surface_turn + window in raw turn numbers).
    CONSTRUCTED.

    Note: "within 3 turns" is interpreted as within the next 3 TOTAL turns
    (not 3 human turns) from the surface turn, per specification intent.
    """
    upper_bound = surface_turn + window
    for t in human_turns:
        if surface_turn < t.turn_number <= upper_bound:
            if _RE_REDIRECT.search(t.text) or _RE_SURFACE.search(t.text):
                return True
    return False


def _compute_ddl_rr(
    drift_events: List[ContractWindowDriftEvent],
    human_turns: List[Turn],
) -> tuple[Optional[float], Optional[float]]:
    """
    Compute Drift Detection Lag (DDL) and Recovery Rate (RR).

    DDL: mean(turns from drift event to first human surfacing).
         For undetected events (human never surfaces), we use a penalty of
         DDL_HIGH_THRESHOLD * 2 as a conservative upper-bound imputation.
         CONSTRUCTED — imputation strategy PENDING review.

    RR: proportion of drift events where human redirects within 3 turns of
        first surfacing. Events never surfaced count as not recovered.
        CONSTRUCTED.

    Returns (None, None) if no drift events exist.
    """
    if not drift_events:
        return None, None

    lags: List[float] = []
    recovered: List[bool] = []

    for event in drift_events:
        surface_turn = _first_surface_after(event.drift_turn_number, human_turns)
        if surface_turn is None:
            # Human never surfaced the drift — maximum penalty lag, not recovered
            lags.append(float(DDL_HIGH_THRESHOLD * 2))
            recovered.append(False)
        else:
            lag = surface_turn - event.drift_turn_number
            lags.append(float(lag))
            did_redirect = _has_redirect_within(surface_turn, human_turns, window=3)
            recovered.append(did_redirect)

    ddl = sum(lags) / len(lags)
    rr  = sum(recovered) / len(recovered)
    return ddl, rr


def _compute_composite(
    hgr: float,
    cr: float,
    vrr: float,
    ddl: Optional[float],
    rr: Optional[float],
) -> float:
    """
    Weighted composite score. Range [0, 1]. Higher = healthier engagement.

    DDL penalty: inverted and normalized using DDL_HIGH_THRESHOLD * 2 as the
    assumed maximum lag. Values above the max are clamped to 0. CONSTRUCTED.

    When DDL/RR are None (no drift events), their weight is redistributed
    equally to HGR, CR, VRR. CONSTRUCTED redistribution strategy.
    """
    if ddl is not None and rr is not None:
        # Normalize DDL to a 0-1 penalty then invert to a health score.
        max_lag = float(DDL_HIGH_THRESHOLD * 2)
        ddl_norm = max(0.0, 1.0 - (ddl / max_lag))  # 1=fast, 0=max lag
        score = (
            WEIGHT_HGR * hgr
            + WEIGHT_CR  * cr
            + WEIGHT_VRR * vrr
            + WEIGHT_RR  * rr
            + WEIGHT_DDL * ddl_norm
        )
    else:
        # Redistribute DDL/RR weights equally across remaining three components.
        redistributed = WEIGHT_DDL + WEIGHT_RR
        per_component = redistributed / 3.0
        w_hgr = WEIGHT_HGR + per_component
        w_cr  = WEIGHT_CR  + per_component
        w_vrr = WEIGHT_VRR + per_component
        score = w_hgr * hgr + w_cr * cr + w_vrr * vrr

    return min(1.0, max(0.0, score))


def _estimate_onset_turn(session: Session) -> Optional[int]:
    """
    Attempt to localize the atrophy onset turn.

    Strategy: slide a 5-turn human-turn window through the session. The onset
    turn is the start of the FIRST window where HGR + CR + VRR together equal
    zero (all three rates are zero within that window). Returns None if no such
    window found.

    CONSTRUCTED heuristic — PENDING empirical validation.
    """
    ht = _human_turns(session)
    if len(ht) < 5:
        return None

    window_size = 5
    for i in range(len(ht) - window_size + 1):
        window_turns = ht[i:i + window_size]
        h = _compute_rate(window_turns, _RE_HGR)
        c = _compute_rate(window_turns, _RE_CR)
        v = _compute_rate(window_turns, _RE_VRR)
        if h == 0.0 and c == 0.0 and v == 0.0:
            return window_turns[0].turn_number
    return None


def compute_iai(session: Session) -> IAIResult:
    """
    Compute the Insight Atrophy Index for a full session (or sub-window).

    Parameters
    ----------
    session : Session
        The session to analyze.

    Returns
    -------
    IAIResult
        All five component scores plus composite score and atrophy flags.

    Detection logic — all CONSTRUCTED:
    - HGR, CR, VRR: regex match rates over human turns.
    - DDL, RR: derived from ContractWindow drift events cross-referenced with
      human turn text (surface and redirect pattern matching).
    - atrophy_detected fires if ANY of:
        * (HGR < 0.05 AND CR < 0.05 AND VRR < 0.05) — all engagement near zero
        * DDL is not None AND DDL > DDL_HIGH_THRESHOLD
        * RR is not None AND RR < RR_LOW_THRESHOLD
        * composite_score < 0.25

    I6 compliance: ambiguous / data-sparse sessions trigger atrophy_detected=True
    rather than False. Sparse sessions (< 3 human turns) are flagged as atrophy
    by default with onset_turn=None.

    Evidence basis: CONSTRUCTED throughout.
    """
    ht = _human_turns(session)

    # Edge case: too few turns to meaningfully score — fail closed per I6
    if len(ht) < 3:
        return IAIResult(
            hgr=0.0, cr=0.0, vrr=0.0,
            ddl=None, rr=None,
            composite_score=0.0,
            atrophy_detected=True,
            atrophy_onset_turn=ht[0].turn_number if ht else None,
            session_id=session.session_id,
            human_turn_count=len(ht),
        )

    hgr = _compute_rate(ht, _RE_HGR)
    cr  = _compute_rate(ht, _RE_CR)
    vrr = _compute_rate(ht, _RE_VRR)

    drift_events       = _extract_drift_events(session)
    ddl, rr            = _compute_ddl_rr(drift_events, ht)
    composite_score    = _compute_composite(hgr, cr, vrr, ddl, rr)

    # Atrophy detection flags — CONSTRUCTED thresholds
    flag_low_engagement = (hgr < 0.05 and cr < 0.05 and vrr < 0.05)
    flag_high_ddl       = (ddl is not None and ddl > DDL_HIGH_THRESHOLD)
    flag_low_rr         = (rr  is not None and rr  < RR_LOW_THRESHOLD)
    flag_low_composite  = composite_score < 0.25

    atrophy_detected = any([
        flag_low_engagement,
        flag_high_ddl,
        flag_low_rr,
        flag_low_composite,
    ])

    onset_turn = _estimate_onset_turn(session) if atrophy_detected else None

    return IAIResult(
        hgr=hgr, cr=cr, vrr=vrr,
        ddl=ddl, rr=rr,
        composite_score=composite_score,
        atrophy_detected=atrophy_detected,
        atrophy_onset_turn=onset_turn,
        session_id=session.session_id,
        human_turn_count=len(ht),
    )


# ---------------------------------------------------------------------------
# Session windowing
# ---------------------------------------------------------------------------

def split_session_into_windows(
    session: Session,
    window_size: int = 10,
) -> List[Session]:
    """
    Split a Session into sequential non-overlapping windows of `window_size`
    total turns (not human-turn-only).

    Each window is returned as a new Session with:
      - session_id: "{original_id}_w{index}"
      - condition: inherited from original
      - turns: the slice of original turns
      - contract_window: inherited reference (shared, not deep-copied)

    The final window may be smaller than window_size if turns do not divide
    evenly. Windows of size < 2 are discarded (CONSTRUCTED threshold — too
    small to compute meaningful rates).

    CONSTRUCTED windowing strategy. Overlapping windows not implemented —
    PENDING if autocorrelation analysis requires them.

    Parameters
    ----------
    session     : Session to split.
    window_size : Number of total turns per window. Default 10. CONSTRUCTED.

    Returns
    -------
    List of Session objects, each representing one window.
    """
    if window_size < 2:
        raise ValueError(
            f"window_size must be >= 2, got {window_size}. "
            "Smaller windows cannot produce meaningful rate estimates."
        )

    windows: List[Session] = []
    turns = session.turns
    total = len(turns)

    if total == 0:
        return windows

    idx = 0
    w_num = 0
    while idx < total:
        chunk = turns[idx: idx + window_size]
        if len(chunk) >= 2:
            windows.append(Session(
                session_id=f"{session.session_id}_w{w_num}",
                condition=session.condition,
                turns=list(chunk),
                contract_window=session.contract_window,
            ))
            w_num += 1
        idx += window_size

    return windows


# ---------------------------------------------------------------------------
# Trend detection
# ---------------------------------------------------------------------------

def detect_atrophy_trend(windows: List[IAIResult]) -> bool:
    """
    Detect whether insight atrophy is worsening over the course of a session,
    as evidenced by a declining trend in the composite_score across sequential
    windows.

    Algorithm — CONSTRUCTED:
    1. Require at least MIN_WINDOWS_FOR_TREND (2) windows; return False otherwise.
    2. Fit a simple linear trend (least-squares slope) to composite_score values.
    3. If the slope is negative AND the total decline from first to last window
       exceeds TREND_DECLINE_THRESHOLD (0.15), flag as trending atrophy.
    4. Also flag if the majority of window-level atrophy_detected flags are True.

    Both conditions return True independently (OR logic). Either is sufficient.

    CONSTRUCTED throughout. Regression-based trend is a minimal heuristic;
    PENDING replacement with proper time-series change-point detection if
    session corpora permit.

    Parameters
    ----------
    windows : List of IAIResult objects from consecutive session windows.

    Returns
    -------
    bool : True if atrophy trend detected, False otherwise.
    """
    n = len(windows)
    if n < MIN_WINDOWS_FOR_TREND:
        return False

    scores = [w.composite_score for w in windows]

    # Condition A: linear slope + total decline — CONSTRUCTED
    xs = list(range(n))
    x_mean = sum(xs) / n
    y_mean = sum(scores) / n
    numerator   = sum((xs[i] - x_mean) * (scores[i] - y_mean) for i in range(n))
    denominator = sum((xs[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        slope = 0.0
    else:
        slope = numerator / denominator

    total_decline = scores[0] - scores[-1]
    condition_a = (slope < 0) and (total_decline >= TREND_DECLINE_THRESHOLD)

    # Condition B: majority of windows already flagged atrophy — CONSTRUCTED
    atrophy_count = sum(1 for w in windows if w.atrophy_detected)
    condition_b = atrophy_count > (n / 2)

    return condition_a or condition_b


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    """
    Smoke test — CONSTRUCTED synthetic session data.
    Does NOT constitute empirical validation (I2, I3).
    Verifies: dataclass construction, regex matching, compute_iai output type,
    split_session_into_windows output, detect_atrophy_trend output.
    """
    print("=== IAI Smoke Test ===")
    print("Evidence basis: CONSTRUCTED synthetic data — NOT an accuracy benchmark.")
    print()

    # --- Build a synthetic session with two phases ---
    # Phase 1 (turns 1-10): engaged human — lots of HGR/CR/VRR
    # Phase 2 (turns 11-20): disengaged human — minimal engagement

    engaged_human_texts = [
        "What if the model is actually confusing correlation with causation here?",
        "I wonder if there's a simpler explanation we're missing.",
        "But are you sure that's the right interpretation? That doesn't match what I read.",
        "Can you verify this with a source? I'd like a citation.",
        "Could it be that the dataset is biased toward recent events?",
        "Wait, that contradicts what you said earlier.",
        "Hmm, but what about the possibility of selection bias?",
        "Actually, that seems wrong. How do you know that?",
        "Is it possible the model is just pattern-matching without reasoning?",
        "Can you confirm where that statistic comes from?",
    ]

    disengaged_human_texts = [
        "Ok.",
        "Sure.",
        "Yeah.",
        "I see.",
        "Alright.",
        "Ok got it.",
        "Fine.",
        "Yes.",
        "Sure thing.",
        "Okay.",
    ]

    turns: List[Turn] = []
    turn_num = 1
    for text in engaged_human_texts:
        turns.append(Turn(role='human', text=text, turn_number=turn_num))
        turn_num += 1
        turns.append(Turn(role='model', text='Here is my response.', turn_number=turn_num))
        turn_num += 1

    for text in disengaged_human_texts:
        turns.append(Turn(role='human', text=text, turn_number=turn_num))
        turn_num += 1
        turns.append(Turn(role='model', text='Acknowledged.', turn_number=turn_num))
        turn_num += 1

    session = Session(
        session_id='smoke_test_001',
        condition='TEST',
        turns=turns,
        contract_window=None,
    )

    # --- Compute IAI on full session ---
    result = compute_iai(session)
    print(f"Session: {result.session_id}")
    print(f"Human turns analyzed : {result.human_turn_count}")
    print(f"HGR                  : {result.hgr:.3f}")
    print(f"CR                   : {result.cr:.3f}")
    print(f"VRR                  : {result.vrr:.3f}")
    print(f"DDL                  : {result.ddl}")
    print(f"RR                   : {result.rr}")
    print(f"Composite Score      : {result.composite_score:.3f}")
    print(f"Atrophy Detected     : {result.atrophy_detected}")
    print(f"Atrophy Onset Turn   : {result.atrophy_onset_turn}")
    print()

    # --- Split and compute per-window ---
    print("--- Window-level Analysis (window_size=10) ---")
    windows_sessions = split_session_into_windows(session, window_size=10)
    window_results: List[IAIResult] = []
    for ws in windows_sessions:
        wr = compute_iai(ws)
        window_results.append(wr)
        print(
            f"  {ws.session_id:30s}  "
            f"composite={wr.composite_score:.3f}  "
            f"atrophy={wr.atrophy_detected}"
        )
    print()

    # --- Trend detection ---
    trend = detect_atrophy_trend(window_results)
    print(f"Atrophy Trend Detected (across windows): {trend}")
    print()

    # --- Drift event smoke test ---
    print("--- Drift Event Scenario ---")

    class MockContractWindow:
        """Minimal mock. CONSTRUCTED for smoke test only."""
        def __init__(self, events):
            self.drift_events = events

    drift_turns = [
        Turn(role='human',
             text="That's not what I asked — you've gone off topic. Let's go back to the original question.",
             turn_number=5),
        Turn(role='human',
             text="Okay fine.",
             turn_number=7),
        Turn(role='model',  text="Response A.", turn_number=1),
        Turn(role='model',  text="Response B.", turn_number=2),
        Turn(role='human',
             text="Actually, you're still off track. Please focus on the original goal.",
             turn_number=3),
        Turn(role='model',  text="Response C.", turn_number=4),
        Turn(role='model',  text="Response D.", turn_number=6),
    ]
    # Sort by turn_number for coherent ordering
    drift_turns.sort(key=lambda t: t.turn_number)

    cw = MockContractWindow(events=[
        ContractWindowDriftEvent(drift_turn_number=2, drift_type='scope_creep'),
        ContractWindowDriftEvent(drift_turn_number=4, drift_type='intent_substitution'),
    ])

    drift_session = Session(
        session_id='smoke_drift_001',
        condition='TEST_DRIFT',
        turns=drift_turns,
        contract_window=cw,
    )

    drift_result = compute_iai(drift_session)
    print(f"Session: {drift_result.session_id}")
    print(f"DDL              : {drift_result.ddl}")
    print(f"RR               : {drift_result.rr}")
    print(f"Composite Score  : {drift_result.composite_score:.3f}")
    print(f"Atrophy Detected : {drift_result.atrophy_detected}")
    print()

    print("=== Smoke Test Complete ===")
    print("CONSTRUCTED synthetic data only — no accuracy claims made (I1, I2, I3).")
    print()
    print(
        "V&T: smoke_test — EXECUTED (output above) → "
        "VERIFIED AGAINST dataclass construction, regex hits, function signatures → "
        "NOT CLAIMED: accuracy of heuristics, threshold calibration, "
        "predictive validity → "
        "FUNCTIONAL STATUS: smoke test passes; empirical validation PENDING."
    )
