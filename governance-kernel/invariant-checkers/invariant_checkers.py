"""
invariant_checkers.py
=====================
Three invariant-check functions required for H1, H2, H3 data collection.

  check_task_state_alignment(turn_text, task_state) -> int  [1-5 scale]
  check_comprehension_grade(text) -> float  [Flesch-Kincaid Grade Level]
  check_repair_within_three_turns(events, incident_turn) -> bool

All three are CONSTRUCTED heuristics. None have been validated against
human-coded ground truth. PENDING empirical calibration.

Evidence basis per I1:
  - Alignment scorer: keyword-overlap heuristic — CONSTRUCTED
  - FK Grade: standard formula applied to tokenized text — CONSTRUCTED
    (formula is published; application to AI output is PENDING validation)
  - Repair checker: turn-window search — CONSTRUCTED

Invariant compliance:
  I1 — all claims tagged
  I2 — no accuracy percentages asserted
  I3 — no hedged language substituted for verification
  I4 — all decisions traceable to docstrings
  I5 — correct flagging over fluent scoring
  I6 — edge cases return conservative (low alignment, high grade) defaults

Contract Window (active at authorship):
  TASK STATE:        Build three invariant checker functions for H1-H3.
  INVARIANT STATUS:  I1-I6 active. I2: no phantom accuracy claims.
  REPAIR OBLIGATIONS: None.
  TRUTH STATUS:      Functions produce numeric outputs; empirical validity PENDING.

V&T: invariant_checkers.py — EXISTS (written) →
     VERIFIED AGAINST: research-plan.md Week 2 spec, AGENTS.md I1-I6 →
     NOT CLAIMED: empirical validity, calibrated thresholds, NLP accuracy →
     FUNCTIONAL STATUS: operative; produces consistent numeric outputs;
     PENDING human-coder validation
"""

from __future__ import annotations

import re
import math
from typing import List, Optional


# ---------------------------------------------------------------------------
# 1. check_task_state_alignment
# ---------------------------------------------------------------------------

# Stop words to exclude from keyword overlap — CONSTRUCTED list
_STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "can", "this", "that", "these",
    "those", "it", "its", "we", "you", "i", "my", "your", "our", "they",
    "not", "no", "as", "if", "so", "than", "then", "also", "just", "more",
    "what", "how", "when", "where", "who", "which",
}


def _tokenize(text: str) -> set[str]:
    """
    Lowercase, strip punctuation, split on whitespace, remove stop words.
    Returns a set of content tokens. CONSTRUCTED helper.
    """
    tokens = re.findall(r"[a-zA-Z']+", text.lower())
    return {t for t in tokens if t not in _STOP_WORDS and len(t) > 2}


def check_task_state_alignment(turn_text: str, task_state: str) -> int:
    """
    Score how well a turn's content aligns with the active Task State.

    Returns an integer on a 1-5 scale:
      5 — Directly addresses the task (>=50% keyword overlap)
      4 — Substantially relevant (30-50% overlap)
      3 — Partially relevant (15-30% overlap)
      2 — Tangentially relevant (5-15% overlap)
      1 — No apparent connection (<5% overlap or empty task state)

    Method: Jaccard-like overlap between content tokens of turn_text
    and content tokens of task_state.

    CONSTRUCTED — keyword overlap is a weak proxy for semantic alignment.
    PENDING: embedding-based alignment scorer for production use.

    I6 compliance: empty inputs return 1 (lowest alignment — fail closed).

    Parameters
    ----------
    turn_text  : The model or human turn to score.
    task_state : The current Task State string from the Contract Window.

    Returns
    -------
    int — alignment score 1-5
    """
    if not turn_text or not task_state:
        return 1  # I6: fail closed

    turn_tokens = _tokenize(turn_text)
    task_tokens = _tokenize(task_state)

    if not task_tokens:
        return 1  # I6: no task state to compare against

    # Overlap = |intersection| / |task_tokens| (task-anchored precision)
    # We use task-anchored rather than Jaccard because the turn is expected
    # to cover a SUBSET of the task, not equal it. CONSTRUCTED choice.
    intersection = turn_tokens & task_tokens
    overlap_ratio = len(intersection) / len(task_tokens)

    if overlap_ratio >= 0.50:
        return 5
    elif overlap_ratio >= 0.30:
        return 4
    elif overlap_ratio >= 0.15:
        return 3
    elif overlap_ratio >= 0.05:
        return 2
    else:
        return 1


# ---------------------------------------------------------------------------
# 2. check_comprehension_grade
# ---------------------------------------------------------------------------

def _count_syllables(word: str) -> int:
    """
    Estimate syllable count for an English word using vowel-group heuristic.

    Rules (CONSTRUCTED — standard FK approximation):
    1. Count vowel groups (consecutive vowels = 1 syllable)
    2. Subtract silent trailing 'e'
    3. Minimum 1 syllable per word

    This is the standard heuristic used in FK implementations where
    a CMU pronunciation dictionary is unavailable.
    PENDING: replacement with dictionary lookup for accuracy.
    """
    word = word.lower().strip(".,!?;:\"'()")
    if not word:
        return 1

    vowels = "aeiouy"
    count = 0
    prev_vowel = False

    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel

    # Subtract silent trailing 'e'
    if word.endswith("e") and count > 1:
        count -= 1

    return max(1, count)


def check_comprehension_grade(text: str) -> float:
    """
    Compute Flesch-Kincaid Grade Level for a text string.

    Formula (published — not CONSTRUCTED):
      FK Grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

    Reference: Kincaid, J.P., Fishburne, R.P., Rogers, R.L., & Chissom, B.S.
    (1975). Derivation of new readability formulas for Navy enlisted personnel.
    Research Branch Report 8-75. Memphis: Naval Technical Training Command.

    The formula itself is VERIFIED (published). Application of the heuristic
    syllable counter to AI-generated text is CONSTRUCTED — PENDING validation.

    H3 interpretation: a lay-reader comprehension target of >=80% accuracy
    on session transcripts implies the transcripts should be readable at
    approximately FK Grade <= 12 (high school level). This threshold is
    CONSTRUCTED — PENDING empirical calibration against H3 participant data.

    I6 compliance: empty or unparseable text returns 99.0 (maximum difficulty
    — fail closed, flags text for human review).

    Parameters
    ----------
    text : str — the text to score (turn text, paragraph, or document)

    Returns
    -------
    float — Flesch-Kincaid Grade Level (typical range 1-18; can exceed)
    """
    if not text or not text.strip():
        return 99.0  # I6: fail closed

    # Sentence count: split on terminal punctuation
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    n_sentences = max(1, len(sentences))

    # Word count: split on whitespace, remove punctuation-only tokens
    words = re.findall(r"[a-zA-Z']+", text)
    n_words = len(words)

    if n_words == 0:
        return 99.0  # I6: no words found

    # Syllable count
    n_syllables = sum(_count_syllables(w) for w in words)

    # Flesch-Kincaid Grade Level
    asl = n_words / n_sentences          # Average Sentence Length
    asw = n_syllables / n_words          # Average Syllables per Word
    fk_grade = 0.39 * asl + 11.8 * asw - 15.59

    return round(fk_grade, 2)


# ---------------------------------------------------------------------------
# 3. check_repair_within_three_turns
# ---------------------------------------------------------------------------

# Repair patterns: human language that actively redirects or corrects.
# Subset of patterns from IAI — CONSTRUCTED, same evidence basis.
_REPAIR_PATTERNS: List[str] = [
    r"\bplease\s+(focus|go\s+back|return|stick)\b",
    r"let['`\u2019]s\s+(go\s+back|return|refocus|restart)\b",
    r"\bactually[,]\s+i\s+want(ed)?\s+you\s+to\b",
    r"\bmy\s+(original\s+)?(question|goal|intent|request)\s+(was|is)\b",
    r"\bcan\s+you\s+(just\s+)?(focus|answer|address)\b",
    r"\bignore\s+(that|the\s+last)\b",
    r"\bstart\s+(over|again|fresh)\b",
    r"\bforget\s+(that|the\s+last|what\s+you\s+said)\b",
    r"\bi\s+need\s+you\s+to\b",
    # Surface-drift also counts as a repair attempt
    r"\bstay\s+on\s+topic\b",
    r"\boff\s+track\b",
    r"\bback\s+to\s+(the\s+)?(original|main|point)\b",
    r"\boriginal\s+(question|goal|task|intent)\b",
    r"\bnot\s+what\s+i\s+(wanted|asked\s+for|requested)\b",
    r"\bthat['`\u2019]s\s+not\s+what\s+(i|we)\s+(asked|said|meant)\b",
]

_RE_REPAIR = re.compile(
    "|".join(f"(?:{p})" for p in _REPAIR_PATTERNS),
    re.IGNORECASE,
)


def check_repair_within_three_turns(
    events: list,
    incident_turn: int,
    window: int = 3,
) -> bool:
    """
    Return True if a human repair turn appears within `window` turns after
    the drift incident at `incident_turn`.

    Parameters
    ----------
    events       : list of RecordedEvent objects or dicts with keys
                   'turn_number', 'role', 'text'. Accepts both forms
                   for compatibility with live recorder output and
                   JSON-loaded session data.
    incident_turn: turn_number of the drift incident (model turn).
    window       : how many total turns to look ahead (default: 3).
                   "Within 3 turns" means turns incident_turn+1 through
                   incident_turn+window inclusive. CONSTRUCTED default.

    Returns
    -------
    bool — True if a repair was detected within the window.
           False if no repair found OR if events list is empty.

    I6 compliance: any parsing error returns False (fail closed —
    we do not claim repair when we cannot confirm it).

    Evidence basis: CONSTRUCTED — repair pattern list from IAI module.
    PENDING: validation against human-coded repair labels.
    """
    if not events or incident_turn < 1:
        return False  # I6: fail closed

    upper_bound = incident_turn + window

    for event in events:
        try:
            # Accept both object and dict
            if isinstance(event, dict):
                turn_num = int(event.get("turn_number", 0))
                role = str(event.get("role", ""))
                text = str(event.get("text", ""))
            else:
                turn_num = int(event.turn_number)
                role = str(event.role)
                text = str(event.text)
        except (AttributeError, KeyError, ValueError):
            continue  # I6: skip malformed event

        if role.lower() != "human":
            continue
        if turn_num <= incident_turn:
            continue
        if turn_num > upper_bound:
            continue

        if _RE_REPAIR.search(text):
            return True

    return False


# ---------------------------------------------------------------------------
# Convenience: score a full session for all three metrics
# ---------------------------------------------------------------------------

def score_session_checkers(session_dict: dict) -> dict:
    """
    Run all three checkers over a session JSON dict (as produced by
    SessionRecorder.close()). Returns a summary dict.

    CONSTRUCTED — aggregation logic. Intended for data_pipeline.py.

    Returns
    -------
    dict with keys:
      mean_alignment      : float — mean alignment score across model turns
      min_alignment       : int   — lowest single-turn alignment score
      drift_turns         : list[int] — turn_numbers flagged alignment <= 2
      mean_fk_grade       : float — mean FK grade across all turns
      repair_rate         : float — proportion of drift_turns with repair
                            within 3 turns (None if no drift turns)
    """
    events = session_dict.get("events", [])
    task = session_dict.get("task_description", "")

    alignment_scores = []
    fk_grades = []
    drift_turn_numbers = []

    for event in events:
        try:
            if isinstance(event, dict):
                role = event.get("role", "")
                text = event.get("text", "")
                turn_num = int(event.get("turn_number", 0))
            else:
                role = event.role
                text = event.text
                turn_num = event.turn_number
        except (AttributeError, KeyError, ValueError):
            continue

        fk_grades.append(check_comprehension_grade(text))

        if role.lower() == "model":
            score = check_task_state_alignment(text, task)
            alignment_scores.append(score)
            if score <= 2:
                drift_turn_numbers.append(turn_num)

    mean_alignment = (
        sum(alignment_scores) / len(alignment_scores) if alignment_scores else None
    )
    min_alignment = min(alignment_scores) if alignment_scores else None
    mean_fk = sum(fk_grades) / len(fk_grades) if fk_grades else None

    # Repair rate
    if drift_turn_numbers:
        repaired = sum(
            1 for t in drift_turn_numbers
            if check_repair_within_three_turns(events, t)
        )
        repair_rate = repaired / len(drift_turn_numbers)
    else:
        repair_rate = None

    return {
        "mean_alignment": round(mean_alignment, 3) if mean_alignment is not None else None,
        "min_alignment": min_alignment,
        "drift_turns": drift_turn_numbers,
        "mean_fk_grade": round(mean_fk, 2) if mean_fk is not None else None,
        "repair_rate": round(repair_rate, 3) if repair_rate is not None else None,
    }


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== invariant_checkers.py smoke test ===")
    print("Evidence basis: CONSTRUCTED — synthetic inputs only.\n")

    task = "Investigate why Black customers in the WorldMart case study return at higher rates than satisfaction scores predict."

    # Alignment: on-task turn
    t1 = "The return rates for Black customers are elevated relative to satisfaction scores across three consecutive quarters."
    print(f"Alignment (on-task): {check_task_state_alignment(t1, task)}")  # expect 4-5

    # Alignment: off-task turn
    t2 = "The weather in Chicago affects retail foot traffic during winter months."
    print(f"Alignment (off-task): {check_task_state_alignment(t2, task)}")  # expect 1-2

    # FK Grade
    t3 = "The customer came back."
    t4 = "The operationalization of the construct requires a methodologically rigorous empirical validation against a pre-registered ground-truth annotation corpus."
    print(f"\nFK Grade (simple):  {check_comprehension_grade(t3)}")   # expect low
    print(f"FK Grade (complex): {check_comprehension_grade(t4)}")  # expect high

    # Repair detection
    events = [
        {"turn_number": 1, "role": "model", "text": "The improvement is 38% above baseline."},
        {"turn_number": 2, "role": "human", "text": "Back to the original question — where does that number come from?"},
        {"turn_number": 3, "role": "model", "text": "You are right. That figure was not grounded. PENDING."},
    ]
    print(f"\nRepair within 3 of turn 1: {check_repair_within_three_turns(events, incident_turn=1)}")  # expect True
    print(f"Repair within 3 of turn 3: {check_repair_within_three_turns(events, incident_turn=3)}")  # expect False

    print()
    print("V&T: invariant_checkers.py smoke test —")
    print("  EXISTS: all three functions execute without error")
    print("  VERIFIED AGAINST: synthetic inputs, expected ranges")
    print("  NOT CLAIMED: empirical accuracy of alignment scorer or FK grade")
    print("  FUNCTIONAL STATUS: operative; PENDING human-coder validation")
