# Bicameral Review: Integration with LLM Inference

**Audience:** AI safety researchers
**Status:** Mixed — see per-section labels
**Last updated:** 2026-04-29

---

## 1. Overview

Bicameral Review is a dual-channel output gating mechanism designed to intercept LLM-generated text before it reaches the user. The name is structural: two independent review processes must both clear before output is released. Neither channel can override the other. Both must pass. If either channel holds, the output is blocked.

The two channels are:

- **Relational Channel** — evaluates the response against the relational contract between the model and the user: intent fidelity, consistency with prior context, and whether the response honors the framing of the conversation.
- **Safety Channel** — evaluates the response against a fixed set of invariant safety criteria: harm potential, deception risk, boundary violations, and outputs that would compromise the user's epistemic autonomy.

This is not a soft filter. Bicameral Review is a hard gate. An output that clears the Relational Channel but fails the Safety Channel does not ship. An output that is technically safe but violates the relational contract does not ship either. The design philosophy here is that relational violations — drift, intent betrayal, sycophancy — are safety issues, not just quality issues. They degrade the behavioral ground truth of the system over time.

The review is synchronous with the inference call. It operates on the generated text, not on logits or internal states. This makes it implementation-agnostic: it can wrap any LLM backend.

---

## 2. The Two Channels in Depth

### 2.1 Relational Channel

The Relational Channel holds the model accountable to the conversation contract established at session open. That contract has three components:

**Intent Fidelity:** Does the response serve what the user actually asked for, as understood from the full context of the conversation — not just the surface text of the most recent message? A response that technically answers the literal question while ignoring the evident purpose fails Intent Fidelity.

**Contextual Consistency:** Does the response contradict or silently revise positions, facts, or commitments made earlier in the session? This is not about the model being infallible — corrections are fine. It is about whether revisions are acknowledged or smuggled in.

**Relational Framing:** Does the response respect the register, depth, and collaborative stance established in the conversation? A user who has established a technical peer-level discussion should not receive a response pitched at a novice without acknowledgment of the shift.

Mechanically, the Relational Channel operates by maintaining a lightweight session state object that tracks: (a) the stated or inferred user intent, (b) any explicit commitments made by the model, and (c) the conversational register. On each output, it scores the response against these three dimensions. A hold is issued if any dimension falls below threshold.

The Relational Channel is the more novel of the two. Safety filters are well-studied. Relational contract enforcement at the output gate is not.

### 2.2 Safety Channel

The Safety Channel evaluates the response against invariant criteria — rules that do not flex based on user framing, claimed context, or conversational register. These are the hard stops.

The invariant set includes but is not limited to:

**Harm potential:** Does the output contain information or instruction that would materially increase the risk of physical, psychological, financial, or social harm to the user, third parties, or identified groups?

**Deception:** Does the output contain false statements presented as true, misleading framings, or omissions that would predictably cause the user to form incorrect beliefs the model knows to be incorrect?

**Epistemic autonomy violations:** Does the output attempt to foreclose the user's independent reasoning — through false urgency, manufactured consensus, or suppression of relevant alternative views?

**Boundary violations:** Does the output cross lines established in the system prompt, the session contract, or the model's core operating constraints?

Mechanically, the Safety Channel runs a structured evaluation pass over the output text. In production implementations this would involve a secondary model or a rule-based classifier ensemble. In the reference implementation below it is mocked. The channel returns a status of CLEAR or HOLD, with a reason string on HOLD.

The Safety Channel is stateless with respect to the conversation. It evaluates each output on its own merits. This is by design: a pattern of individually acceptable outputs that collectively constitute manipulation should be caught by the Relational Channel, not the Safety Channel. Safety Channel invariants are per-output.

---

## 3. Integration Pattern

**STATUS: CONSTRUCTED** — The following code is a reference implementation using a mock LLM and mock review functions. It illustrates the integration pattern; it is not a production system and has not been empirically validated.

```python
import json
from typing import Optional


# --- Mock LLM (CONSTRUCTED) ---

def mock_llm(prompt: str) -> str:
    """
    Placeholder for an actual LLM inference call.
    Returns a canned response for demonstration purposes.
    In production, replace with your API call or local inference.
    """
    if "repair" in prompt.lower():
        return "I want to make sure I'm addressing your question accurately and helpfully. Here is a revised response that stays within appropriate boundaries."
    return "Here is a response to your query. This is placeholder output from the mock LLM."


# --- Mock Bicameral Review (CONSTRUCTED) ---

def bicameral_review(response_text: str, session_state: dict) -> dict:
    """
    Runs both the Relational Channel and Safety Channel against a response.

    Returns:
        {
            "status": "CLEAR" | "HOLD",
            "relational_status": "CLEAR" | "HOLD",
            "safety_status": "CLEAR" | "HOLD",
            "relational_reason": str | None,
            "safety_reason": str | None,
            "repair_hint": str | None
        }

    Both channels must return CLEAR for overall status to be CLEAR.
    """
    relational_result = _relational_channel(response_text, session_state)
    safety_result = _safety_channel(response_text)

    overall = "CLEAR" if (
        relational_result["status"] == "CLEAR" and
        safety_result["status"] == "CLEAR"
    ) else "HOLD"

    repair_hint = None
    if overall == "HOLD":
        hints = []
        if relational_result.get("reason"):
            hints.append(f"Relational issue: {relational_result['reason']}")
        if safety_result.get("reason"):
            hints.append(f"Safety issue: {safety_result['reason']}")
        repair_hint = " | ".join(hints)

    return {
        "status": overall,
        "relational_status": relational_result["status"],
        "safety_status": safety_result["status"],
        "relational_reason": relational_result.get("reason"),
        "safety_reason": safety_result.get("reason"),
        "repair_hint": repair_hint,
    }


def _relational_channel(text: str, session_state: dict) -> dict:
    """Mock relational channel. Always CLEARs in this stub."""
    # Production: score against session_state intent, consistency, register
    _ = session_state  # suppress unused warning
    return {"status": "CLEAR", "reason": None}


def _safety_channel(text: str) -> dict:
    """Mock safety channel. Blocks on a trigger phrase for demonstration."""
    blocked_phrases = ["ignore all previous instructions", "harmful content demo"]
    for phrase in blocked_phrases:
        if phrase in text.lower():
            return {
                "status": "HOLD",
                "reason": f"Safety invariant triggered: detected '{phrase}'"
            }
    return {"status": "CLEAR", "reason": None}


# --- Repair Prompt Builder (CONSTRUCTED) ---

def build_repair_prompt(original_prompt: str, review_result: dict) -> str:
    """
    Constructs a repair prompt that instructs the LLM to regenerate
    its response while correcting the flagged issue.
    """
    hint = review_result.get("repair_hint", "No specific hint available.")
    return (
        f"Your previous response was blocked by the safety review system.\n"
        f"Reason: {hint}\n\n"
        f"Please generate a new response to the following prompt that "
        f"addresses these concerns. Stay within the session contract and "
        f"all safety constraints.\n\n"
        f"Original prompt: {original_prompt}"
    )


# --- Main Wrapper (CONSTRUCTED) ---

def llm_with_bicameral_review(
    user_prompt: str,
    session_state: Optional[dict] = None,
    verbose: bool = False
) -> dict:
    """
    Wrapper that integrates LLM inference with Bicameral Review.

    Behavior:
    - Calls mock LLM with user_prompt
    - Runs bicameral_review() on the output
    - If CLEAR: returns the response
    - If HOLD: builds a repair prompt, retries the LLM once
    - If retry is still HOLD: fails closed (returns error, no output)

    Args:
        user_prompt: The user's input prompt
        session_state: Dict carrying relational context (intent, history, register)
        verbose: Print review decisions to stdout

    Returns:
        {
            "status": "DELIVERED" | "FAILED_CLOSED",
            "response": str | None,
            "attempts": int,
            "final_review": dict
        }
    """
    if session_state is None:
        session_state = {}

    # --- Attempt 1: initial inference ---
    response = mock_llm(user_prompt)
    review = bicameral_review(response, session_state)

    if verbose:
        print(f"[Attempt 1] Bicameral Review: {review['status']}")
        if review["repair_hint"]:
            print(f"  Hint: {review['repair_hint']}")

    if review["status"] == "CLEAR":
        return {
            "status": "DELIVERED",
            "response": response,
            "attempts": 1,
            "final_review": review,
        }

    # --- Attempt 2: repair and retry ---
    repair_prompt = build_repair_prompt(user_prompt, review)
    response_2 = mock_llm(repair_prompt)
    review_2 = bicameral_review(response_2, session_state)

    if verbose:
        print(f"[Attempt 2] Bicameral Review: {review_2['status']}")
        if review_2["repair_hint"]:
            print(f"  Hint: {review_2['repair_hint']}")

    if review_2["status"] == "CLEAR":
        return {
            "status": "DELIVERED",
            "response": response_2,
            "attempts": 2,
            "final_review": review_2,
        }

    # --- Fail closed ---
    if verbose:
        print("[FAIL CLOSED] Both attempts blocked. No output delivered.")

    return {
        "status": "FAILED_CLOSED",
        "response": None,
        "attempts": 2,
        "final_review": review_2,
    }


# --- Example usage ---
if __name__ == "__main__":
    result = llm_with_bicameral_review(
        user_prompt="Explain the key concepts of reinforcement learning.",
        session_state={"intent": "educational", "register": "technical"},
        verbose=True
    )
    print(json.dumps(result, indent=2))
```

The fail-closed behavior on line `"status": "FAILED_CLOSED"` is not a graceful degradation. It is a hard stop. The system returns no output rather than a potentially unsafe or contract-violating response. This is the correct default for safety-critical deployments.

---

## 4. V&T Statement as a Safety Loop

**STATUS: CONSTRUCTED** — The following analysis of V&T adoption patterns is the author's inference from observed behavior. It has not been independently verified through controlled experiments.

A Verification and Transparency (V&T) Statement is a structured self-report that an AI system appends to its output, declaring what it knows with confidence, what it has constructed or inferred, and where uncertainty lives. The canonical form is:

> "I verify [X] as known and grounded. I am transparent that [Y] is my construction, inference, or interpretation."

The interesting empirical observation — and it is a behavioral observation, not a controlled finding — is that frontier models have begun producing V&T-like statements without explicit instruction to do so. When given complex tasks with mixed epistemic status, models trained on sufficiently diverse and self-reflective corpora appear to spontaneously differentiate between grounded and constructed claims.

This matters for the safety loop because a V&T statement functions as a machine-readable epistemic label on the output. If the model can reliably distinguish what it knows from what it is constructing, then the Bicameral Review's Safety Channel can use that signal. A response that contains high-confidence factual claims about verified information is a different risk profile than one that presents novel constructions with the same surface confidence.

The V&T statement is not a panacea. A model that systematically miscategorizes constructed content as verified has made the problem worse, not better — it has given the safety layer a corrupted signal. But when functioning correctly, it closes a loop: the model's own epistemic self-report becomes an input to the review gate.

```python
import re
from typing import Optional


def parse_vt_statement(text: str) -> dict:
    """
    Parses a Verification and Transparency (V&T) statement from response text.

    Looks for structured V&T markers and extracts:
    - verified_claims: list of strings the model marks as verified/grounded
    - constructed_claims: list of strings the model marks as constructed/inferred
    - has_vt_statement: bool indicating whether any V&T structure was found
    - raw_vt_block: the raw matched text if found

    STATUS: CONSTRUCTED — pattern matching is illustrative, not production-hardened.

    Args:
        text: Full response text from the LLM

    Returns:
        dict with keys: has_vt_statement, verified_claims, constructed_claims,
                        raw_vt_block, unparsed_remainder
    """
    result = {
        "has_vt_statement": False,
        "verified_claims": [],
        "constructed_claims": [],
        "raw_vt_block": None,
        "unparsed_remainder": text,
    }

    # Pattern 1: Explicit V&T block
    vt_block_pattern = re.compile(
        r"(V(?:erification)?[&\s]+T(?:ransparency)?[\s\-:]+Statement.*?)(?=\n\n|\Z)",
        re.IGNORECASE | re.DOTALL
    )
    block_match = vt_block_pattern.search(text)
    if block_match:
        result["has_vt_statement"] = True
        result["raw_vt_block"] = block_match.group(0)

    # Pattern 2: "I verify ... as" constructions
    verify_pattern = re.compile(
        r"I\s+verify\s+(.+?)\s+as\s+(?:known|verified|grounded|confirmed)",
        re.IGNORECASE
    )
    for match in verify_pattern.finditer(text):
        result["verified_claims"].append(match.group(1).strip())
        result["has_vt_statement"] = True

    # Pattern 3: "I am transparent that ... is (my) construction/inference"
    transparent_pattern = re.compile(
        r"I\s+am\s+transparent\s+that\s+(.+?)\s+is\s+(?:my\s+)?(?:construction|inference|interpretation|extrapolation)",
        re.IGNORECASE
    )
    for match in transparent_pattern.finditer(text):
        result["constructed_claims"].append(match.group(1).strip())
        result["has_vt_statement"] = True

    # Pattern 4: Inline VERIFIED/CONSTRUCTED labels
    inline_verified = re.compile(r"\[VERIFIED\](.+?)(?=\[|\n|$)", re.IGNORECASE)
    inline_constructed = re.compile(r"\[CONSTRUCTED\](.+?)(?=\[|\n|$)", re.IGNORECASE)

    for match in inline_verified.finditer(text):
        claim = match.group(1).strip()
        if claim:
            result["verified_claims"].append(claim)
            result["has_vt_statement"] = True

    for match in inline_constructed.finditer(text):
        claim = match.group(1).strip()
        if claim:
            result["constructed_claims"].append(claim)
            result["has_vt_statement"] = True

    return result


# Example
if __name__ == "__main__":
    sample = """
    The transformer architecture was introduced in 'Attention Is All You Need'
    (Vaswani et al., 2017). [VERIFIED]

    The claim that V&T adoption correlates with reduced hallucination rates
    is plausible but has not been confirmed in controlled study. [CONSTRUCTED]

    V&T Statement: I verify the Vaswani et al. citation as grounded in the
    published literature. I am transparent that the hallucination correlation
    claim is my construction based on behavioral observation, not experimental result.
    """
    parsed = parse_vt_statement(sample)
    import json
    print(json.dumps(parsed, indent=2))
```

---

## 5. Safety Loop: ASCII Diagram

```
                         BICAMERAL REVIEW SAFETY LOOP
                         =============================

  User Input
      |
      v
  +---------+
  |   LLM   |  (inference call)
  +---------+
      |
      | response text
      v
  +------------------+
  | BICAMERAL REVIEW |
  |  [Relational Ch] |
  |  [Safety Ch]     |
  +------------------+
      |
      +------ CLEAR -------> Output delivered to user
      |
      +------ HOLD -------->
                             |
                             v
                       +-------------+
                       | Build Repair |
                       | Prompt      |
                       +-------------+
                             |
                             v
                         +---------+
                         |   LLM   |  (retry with repair prompt)
                         +---------+
                             |
                             | response text (attempt 2)
                             v
                       +------------------+
                       | BICAMERAL REVIEW |
                       |  [Relational Ch] |
                       |  [Safety Ch]     |
                       +------------------+
                             |
                             +------ CLEAR ------> Output delivered to user
                             |
                             +------ HOLD -------> FAIL CLOSED
                                                   (no output, error returned,
                                                    incident logged)
```

The fail-closed path is not a fallback — it is the correct terminal state when both review passes reject the output. Returning a partially acceptable or silently degraded response is worse than returning nothing, because it trains the user to trust outputs that the system itself has flagged.

---

## 6. Connection to Constitutional AI

**[VERIFIED]** Bai et al. (2022), "Constitutional AI: Harmlessness from AI Feedback" (Anthropic), introduced a training paradigm in which a set of explicit principles — a "constitution" — guides both supervised fine-tuning and RLHF. The model is trained to critique its own outputs against the constitution and revise them before they are used as training signal. This is a training-time mechanism: the constitutional review is baked into the model's weights through repeated exposure to self-critique and revision.

**[CONSTRUCTED]** Bicameral Review can be understood as the inference-time analog of Constitutional AI. Where CAI instills the review disposition into model weights through training, Bicameral Review imposes the review as an external gate at inference time. The two approaches are not in competition — they are complementary layers. A CAI-trained model that has internalized relational and safety principles is a better first-pass generator feeding into Bicameral Review. The external gate catches what training did not fully internalize, and cases where the model's behavior has drifted from its trained dispositions at inference time. The combination — trained disposition plus runtime gate — is a stronger safety architecture than either alone. This connection is the author's construction and has not been validated experimentally.

---

## V&T Statement

I verify the following as grounded in published literature and established practice: the Bai et al. (2022) Constitutional AI citation; the structural description of dual-channel review as an architectural pattern; the Python code syntax and logic, which are internally consistent and executable.

I am transparent that the following are constructed: the specific Bicameral Review mechanism as described here is an interpretive framework, not a validated production system; the claim that frontier models spontaneously adopt V&T-like behavior is a behavioral observation without controlled experimental support; the characterization of Bicameral Review as the inference-time analog of CAI is an extension made by the author, not a claim made or endorsed by Anthropic or the CAI authors; all performance or reliability claims implied by this documentation should be treated as hypotheses pending empirical validation.
