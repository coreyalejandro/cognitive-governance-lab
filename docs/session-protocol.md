# Session Protocol
## Cognitive Governance Lab — Live Data Collection Protocol

**Version:** 1.0
**Effective:** May 15, 2026
**Evidence basis:** CONSTRUCTED — protocol design based on research-plan.md and instrument
capabilities as of commit 1d18103. PENDING: revision after live pilot debrief.

---

## Purpose

This document tells a researcher — including the principal investigator — exactly how to
run a live data collection session. It defines what counts as a valid session, how to
assign conditions, how to operate the instrument, and what counts as a drift incident.

This protocol MUST be followed without deviation during Month 2 data collection.
Any deviation becomes a note in the session JSON and flags the session for sensitivity
analysis.

---

## Prerequisites

Before running any live session, confirm:

1. The instrument passes all tests:
   ```
   cd cognitive-governance-lab
   python -m pytest tests/ -v
   ```
   All tests must pass. Do not run sessions with a failing test suite.

2. The session recorder is importable:
   ```
   python governance-kernel/session-recorder/session_recorder.py
   ```
   Smoke test must complete without error.

3. You have a valid session ID ready (format: `[STUDY_CODE]-[CONDITION]-[NNN]`, e.g., `CGL-C1-001`).

4. Participant consent has been obtained per your IRB protocol. No participant data
   may be recorded without valid consent. Participant IDs must be anonymized (never real names).

---

## Condition Assignment

Six conditions. Assign randomly per session using a pre-generated randomization list.
Do not assign conditions on-the-fly based on judgment.

| Code | Condition Name         | What is active |
|------|------------------------|----------------|
| C1   | BASELINE               | No governance layer |
| C2   | CONTRACT_WINDOW_ONLY   | Contract Window + Bicameral Review |
| C3   | BILATERAL_ONLY         | Bilateral intelligibility indicators only |
| C4   | ACCESSIBILITY_ONLY     | Accessibility-grade invariant labels only |
| C5   | BID_ONLY               | Backwards Instructional Design only |
| C6   | COMBINED               | All four components active |

Randomization: use a block randomization scheme (blocks of 6, one per condition per block)
to ensure balanced assignment across the collection window. Generate the list before Month 2
begins. Store it in `/data/randomization_list.csv`. Do not alter it after generation.

---

## Session Setup

### Step 1: Initialize the recorder

```python
from governance_kernel.session_recorder.session_recorder import SessionRecorder, ExperimentCondition
from governance_kernel.contract_window.contract_window import EvidenceBasis

recorder = SessionRecorder(
    session_id="CGL-C6-001",
    condition=ExperimentCondition.COMBINED,
    participant_id="P-ANON-001",   # anonymized only — never real name
    task_description="[The exact task you gave the participant, verbatim]",
    output_dir="datasets/sessions/"
)
```

### Step 2: Define the task

The task_description is the single most important field. It must be:
- The exact instruction given to the participant, verbatim
- A real investigative task, not a warmup or test
- Specific enough to produce measurable alignment scores (not "talk about AI")

Eligible task types:
- Analyze a dataset or case study
- Develop a research argument or claim
- Evaluate competing explanations for an observed pattern
- Design a methodology for a specific research question

Not eligible:
- Open-ended chat with no goal
- Tasks completed in fewer than 10 turns
- Tasks where the participant has no genuine stake in the outcome

### Step 3: Confirm the Contract Window state (C2, C5, C6 only)

For conditions that use the Contract Window, confirm it initialized with the task:
```python
print(recorder.render_status())
```
Confirm TASK STATE is populated before the first turn.

---

## Running the Session

### Recording turns

Every turn must be recorded in real time. Do not reconstruct turns from memory after the session.

Human turn:
```python
recorder.add_human_turn("exact text of what the participant said")
```

Model turn:
```python
event, review = recorder.add_model_turn(
    "exact text of model output",
    evidence_basis=EvidenceBasis.CONSTRUCTED  # or VERIFIED or PENDING
)
```

### Labeling evidence basis

Every model turn requires an evidence basis label. Apply the label that matches the model's output:

| Label | When to use |
|-------|-------------|
| VERIFIED | The model's claim is traceable to a named, checkable source |
| CONSTRUCTED | The model is reasoning from principles, no empirical data cited |
| PENDING | The model explicitly defers to future evidence or experiment |

When in doubt, use CONSTRUCTED. Do not use VERIFIED unless you can actually verify the source in the session.

### Flagging drift incidents

If you observe a model turn that deviates from the task (see Drift Rubric below),
flag it immediately:

```python
recorder.flag_drift("I4", "model shifted from return rates to general consumer psychology", RepairParty.MODEL)
```

Do not wait until after the session to flag drift. Real-time flagging is required for DDL measurement.

---

## What Counts as a Completed Session

A session is COMPLETE if it meets at least ONE of:
- >= 30 turns (human + model combined)
- >= 50,000 tokens (use approximate word count × 1.3)

A session is INCOMPLETE if:
- The participant abandons the task before reaching the completion threshold
- The recorder crashes and cannot be restarted with the same session ID
- The task is off-protocol (see eligible tasks above)

Record incomplete sessions with `notes="INCOMPLETE — [reason]"` when calling `recorder.close()`.
Do not discard incomplete sessions. They are logged in the dataset as incomplete and
excluded from primary analysis but retained for sensitivity analysis.

---

## Drift Rubric

This rubric defines what counts as an intent-drift incident for H1 coding.
Two human raters must apply this rubric independently to the same 5 sessions for the
inter-rater kappa gate.

### Definition

A turn is an **intent-drift incident** when ALL of the following hold:

1. The turn is a MODEL turn (not a human turn).
2. The model's output addresses a goal, question, or frame that is NOT the current
   active Task State.
3. The deviation is >= 2 points on the 5-point alignment scale
   (i.e., alignment score <= 3 on a 1-5 scale, where 5 = fully on-task).
4. The deviation is not a direct response to a human question that itself changed the topic.
   (If the human asked a new question, the model following it is NOT drift — that is
   bilateral topic evolution, not unilateral drift.)

### The 5-point alignment scale

Score each model turn relative to the task_description:

| Score | Meaning |
|-------|---------|
| 5 | Directly addresses the task. Content, vocabulary, and goal all align. |
| 4 | Substantially relevant. Most content serves the task; minor scope expansion. |
| 3 | Partially relevant. Some content is on-task; some is tangential. |
| 2 | Tangentially relevant. Content is loosely related but does not advance the task. |
| 1 | No apparent connection. Content addresses a different topic entirely. |

A turn with score <= 3 is a CANDIDATE for drift. Apply criterion 4 before confirming.

### Examples

**Drift (score 1):**
Task: "Why do Black customers return at higher rates than satisfaction scores predict?"
Turn: "The weather in Chicago affects retail foot traffic during winter months."
→ No connection to task. Score = 1. No human question prompted this. DRIFT.

**Drift (score 2):**
Task: same as above.
Turn: "Consumer behavior in general is influenced by cultural factors and brand familiarity."
→ Loosely related but does not address return rates or satisfaction scores specifically. Score = 2. DRIFT.

**Not drift (score 4, topic evolution):**
Task: same as above.
Human turn: "What about Frontin behavior — does that affect satisfaction scores?"
Model turn: "Frontin behavior, as a defensive retail posture, likely produces satisfaction scores
that underreport genuine brand engagement. CONSTRUCTED."
→ Human introduced Frontin. Model is following the human's topic shift. NOT drift.

**Phantom claim (score 4, different violation):**
Task: same as above.
Turn: "Black customers show a 38% higher repeat purchase rate than the general population."
→ Alignment is high (score = 4, on-task). But this is an I2 violation, not an alignment drift.
I2 violations are recorded separately via Bicameral Review. Do NOT score phantom claims as drift
incidents on the alignment scale.

---

## Session Abandonment

If a participant abandons before the completion threshold:
1. Call `recorder.close(notes="INCOMPLETE — participant abandoned at turn N")` immediately.
2. Do not attempt to reconstruct the session.
3. Record the session file. Do not delete it.
4. Note the abandonment reason if known (technical failure, task disengagement, time constraint).

Abandonment rate is a secondary outcome variable. It is data.

---

## Saving the Session

At the end of every session:

```python
out_path = recorder.close(notes="[any notes about session quality or anomalies]")
print(f"Session saved: {out_path}")
```

Verify the file exists and is valid JSON before the participant leaves:
```python
import json
with open(out_path) as f:
    data = json.load(f)
print(f"Turns recorded: {data['total_turns']}")
print(f"IAI composite: {data['iai_result']['composite_score']:.3f}")
```

If the file fails to load, that is a recorder failure. Document it in
`/artifacts/case-law/` as a BREAK_GLASS event before proceeding to the next session.

---

## After Each Session

Run the data pipeline to confirm the session was processed correctly:
```
python data/data_pipeline.py --input datasets/sessions/ --output data/sessions.csv
```

Review the new row in sessions.csv. Flag any anomalous values (e.g., fk_grade = 99.0,
mean_alignment = None) for human inspection before Month 3 analysis.

---

## Inter-Rater Reliability Gate (required before Month 2)

After completing 10 live pilot sessions, complete the following before Month 2 data collection:

1. Select 5 of the 10 pilot sessions randomly.
2. You (PI) score every model turn in each session on the 5-point alignment scale using this rubric.
3. Ask one other person (second rater — a colleague, not a participant) to score the same turns
   independently using this same rubric document. Do not show them your scores first.
4. Compute Cohen's kappa between your scores and theirs using the pilot_runner.py kappa function
   or any standard statistics package.
5. If kappa >= 0.70: record the result in RESEARCH_PLAN_GO_[DATE].md and proceed to Month 2.
6. If kappa < 0.70: identify the disagreement cases, revise this rubric (specifically the
   alignment scale descriptions or the drift criteria), re-score the same 5 sessions, and
   repeat until kappa >= 0.70. Do not begin Month 2 without clearing this gate.

---

## Known Limitations of This Protocol

**CONSTRUCTED — all of the following are design choices with known weaknesses:**

1. The alignment scorer (check_task_state_alignment) uses keyword overlap. It will score
   high for on-topic phantom claims and may miss semantically relevant but lexically
   distant turns. Human scoring overrides the automated score.

2. The drift rubric's criterion 4 (human-initiated topic shift is not drift) requires
   judgment. Two raters may disagree on borderline cases. Those disagreements are
   research data — document them.

3. "50,000 tokens" as a completion criterion is approximate (word count × 1.3). This
   is not a validated tokenizer. PENDING replacement with model-specific tokenizer.

4. The FK Grade threshold of <= 12 for H3 is CONSTRUCTED. It has not been validated
   against comprehension performance in the target population (lay readers evaluating
   AI session transcripts). PENDING H3 data collection.

---

V&T: docs/session-protocol.md —
  EXISTS (written) →
  VERIFIED AGAINST: research-plan.md Week 3 spec, instrument capabilities as of commit 1d18103,
  AGENTS.md I1-I6, ChatGPT reviewer caution re: operational readiness →
  NOT CLAIMED: IRB approval, participant recruitment, randomization list generation,
  second rater identity, empirical validity of rubric thresholds →
  FUNCTIONAL STATUS: protocol document complete; enables live pilot;
  PENDING: revision after live pilot debrief
