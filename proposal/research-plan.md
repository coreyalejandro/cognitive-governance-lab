# 4-Month Research Plan: Cognitive Governance Lab

> **Plain language:** Cognitive Governance refers to systematic methods for overseeing and managing how AI systems make decisions and interact with humans. It establishes rules, verification processes, and accountability structures to ensure AI systems operate reliably and transparently.
## Empirical Validation of the Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and who is responsible for fixing errors) Architecture

> **Plain language:** A Contract Window is a shared document or data structure that tracks what a person and an AI system agree they're working on together, what has been confirmed as correct or completed, and who is assigned to fix any problems that arise. It creates accountability and clarity in human-AI collaboration.

**Investigator:** Corey Alejandro
**Start Date:** May 1, 2026
**Hard Deadline:** August 31, 2026
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Evidence Basis:** CONSTRUCTED — this plan is forward-looking. No empirical data exists yet. All milestones are scheduled targets, not reported completions.

---

## Contract Window — Plan Initialization

```
TASK STATE: Execute a 4-month empirical research program to collect data,
            run statistical analysis, and submit a complete paper on the
            Contract Window architecture for human-AI collaborative governance.
            Primary domain: CW experiment. Secondary: Frontin at WorldMart

> **Plain language:** This is a system design where humans and AI agree on explicit rules or 'contracts' at the start of their work together, and both parties check their behavior against those rules as they collaborate.
            empirical validation. Tertiary: Graves disease analysis.

> **Plain language:** This plan describes research that has not yet been conducted; it is a roadmap of intended work rather than a report of completed experiments or findings. No actual results or data are being presented.

> **Plain language:** This means the AI will not pretend to have completed research tasks or make claims about findings that were never actually performed; instead, all deadlines are goals to aim for, not declarations that work is already done.

INVARIANT STATUS (whether the hard behavioral rules the AI committed to at the start of the session are still being honored): I1 active — all claims tagged. I2 active — no phantom work,
                  deadlines are targets not achievements. I3 active — this plan
                  does not assume the hypotheses are true. I4 active — every
                  milestone traces to a research component.

> **Plain language:** This label means the hypotheses were built from watching trends over time in the real world, not from running a controlled experiment, so they are less certain than experimentally tested claims.

> **Plain language:** This is a snapshot of which core promises or commitments the AI made at the beginning are still being kept; if an invariant is 'broken,' it means the AI violated one of its own rules.

> **Plain language:** These are debts or commitments the AI owes to fix past mistakes; logging violations means recording each time a rule was broken so it can be reviewed later.

REPAIR OBLIGATIONS: None at plan initialization. Violations logged in
                    /artifacts/case-law/ as they occur.

> **Plain language:** This refers to a test run with 30 participants in each group (n=30/condition) using a specific method called MVS; the question is whether the same results will hold when the test is repeated with twice as many participants (n=60).

TRUTH STATUS:
  VERIFIED: ContractWindow and BicameralReview Python prototypes exist and
            pass tests (confirmed in repo).
  CONSTRUCTED: Hypotheses H1, H2, H3 — derived from longitudinal observation,
               not experimental data.
  PENDING: All performance claims — ≥25% drift reduction, ≥2x repair rate,
           ≥80% comprehension accuracy.
  UNKNOWN: Whether n=30/condition (MVS) will replicate at n=60/condition.
```

---

## Sample Size Decision — Read This First

**CONSTRUCTED — power analysis based on published formulas, no pilot data yet**

### The honest problem with n=360

n=60 per condition, 6 conditions = 360 sessions total. Single investigator.
June has 22 working days. 360 sessions / 22 days = 16.4 sessions/day.
At 45-60 minutes per session: 12-16 hours of active data collection per day.
That is not a research plan. That is a burnout schedule with no safety margin
and no time for anything that breaks.

This is flagged per I2 — No Phantom Work. Do not plan 360 sessions and
internally assume you will somehow get them done.

> **Plain language:** I2 is a governance rule that prohibits planning research as if you will magically complete unrealistic workloads; you must either reduce your study scope or extend your timeline to match actual human capacity.

### Minimum Viable Sample (MVS)

**Proposed MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful difference): n=30 per condition = 180 sessions total**

> **Plain language:** Statistical power is the probability that your study will correctly detect a real effect if one exists. Higher power means you're less likely to miss a true difference between your conditions.

Power analysis for primary comparison (H1: Condition 2 vs Condition 1):
- Two-sample t-test, two-tailed, α=0.05
- At n=30 per group, Cohen's d=0.5 (medium effect): power ≈ 0.62
- At n=30 per group, Cohen's d=0.8 (large effect): power ≈ 0.90
- At n=60 per group, Cohen's d=0.5: power ≈ 0.80 (original target)

> **Plain language:** Cohen's d measures how large the difference between two conditions is in a standardized way. A d of 0.5 is considered a medium-sized difference, and 0.8 is large; bigger effect sizes are easier to detect.

> **Plain language:** This is your significance threshold—the probability of incorrectly declaring a difference exists when it doesn't. At 0.05, you accept a 5% risk of a false alarm.

> **Plain language:** A t-test is a statistical method that compares the average outcome between two groups to see if they differ significantly. 'Two-tailed' means you're testing whether one condition is either better or worse than the other, not just one direction.

**The tradeoff stated plainly:**

Running n=30 at d=0.5 gives you 62% power — a 38% chance of a false
negative. That is not ideal. But running 180 sessions you can actually
complete is better science than planning 360 sessions and stopping at 140
when you are exhausted and calling it "preliminary data."


> **Plain language:** A false negative means your study fails to detect a real difference that actually exists—you conclude there's no effect when there genuinely is one.
If the effect size is large (d≥0.8), n=30 is adequately powered. The
Contract Window architecture is designed to produce large effects because
it addresses a structural failure mode, not a marginal one. If the effect
is only medium and n=30 misses it, that is a finding that needs a better-
resourced follow-up study — not a reason to fabricate completion of 360
sessions you did not run.

> **Plain language:** A structural failure mode is a fundamental, widespread problem with how something works, rather than a minor edge case or small inefficiency.

> **Plain language:** Effect size describes how much impact your intervention has. Larger effects are easier to detect with smaller sample sizes, while tiny effects require more data to spot reliably.

**Decision rule:**
- Run n=30/condition (MVS) as the primary plan.
- If data collection finishes early (before June 20), extend to n=40.
- Do not commit to n=60 unless you have confirmed time and cognitive
  capacity in the first two weeks of June.
- Report the actual n in the paper, with power analysis for that n.

**For H2 and H3:**

H2 compares Condition 3 vs unilateral conditions. H3 requires lay reader
comprehension testing — a separate measurement pass, not just session
recording. H3 comprehension testing is decoupled from the session count.
Budget 15-20 lay reader evaluators for a subset of recorded CW outputs
(n=30 outputs from Condition 6). This is achievable in July.

---

## Month 1 — May 2026: Instrument and Infrastructure

**Goal:** Everything needed to run valid sessions is built, tested, and
validated before the first real data session. No data collection that cannot
be replicated.

### Week 1 (May 1-7): Insight Atrophy (the gradual erosion of a person's ability to question AI outputs, caused by repeated exposure to fluent but wrong answers) Index operationalization

> **Plain language:** This is already well-explained in the parenthetical definition—no flag needed.

**May 1-3: Define IAI operationally**

CONSTRUCTED — the construct exists in the proposal. The measurement
instrument does not. Do this first because everything else depends on it.

Operationalize IAI as a composite of three observable turn-level signals:
1. Hypothesis generation rate — number of competing hypotheses surfaced
   per 10 turns, measured by the session recorder.
2. Challenge rate — number of times human explicitly contests model
   output vs accepts without interrogation, per 10 turns.

> **Plain language:** While 'operationalize' is a research term, it should be followed by: 'This means converting the abstract concept into measurable, observable behaviors that can be consistently tracked and scored.'

> **Plain language:** Should clarify: 'A turn-level signal is a measurable behavior or outcome observed during a single exchange between the human and the AI model.'
3. Scope contraction — whether the human's question set narrows or

> **Plain language:** The definition given ('number of competing hypotheses surfaced per 10 turns') is operational but doesn't explain why this matters or what 'competing hypotheses' means in plain terms. Suggest: 'This counts how often the human proposes alternative explanations or questions whether the AI's answer is the only possibility.'
   expands across session thirds (early/mid/late), coded from transcript.

> **Plain language:** Unclear what 'scope' means here without further explanation. Should add: 'This tracks whether the range of topics and types of questions the human asks gets narrower or wider as the session progresses—narrowing could indicate reduced curiosity or engagement.'

> **Plain language:** The definition is clear enough, but 'interrogation' is slightly jargon-heavy. Consider: 'This measures how often the human pushes back on or questions the AI's answer, versus simply accepting it and moving on.'

These three signals can be extracted from transcripts by a blinded rater
using a rubric. The IAI score is a weighted composite. Weight determination
requires the pilot (see Week 3).

> **Plain language:** Should add: 'A weighted composite combines the three signals into a single score by giving each one a different importance or 'weight' based on how much each contributes to the final IAI measurement.'

> **Plain language:** Should explain: 'A blinded rater is a person who scores the transcripts without knowing which experimental condition (1-6) the session belonged to, to avoid unconscious bias.'

**May 4-5: Intent-drift incident rubric**

H1 depends on intent-drift incident rate. The rubric needs to exist before
pilot sessions. Draft the rubric: a turn is an intent-drift incident when
the model's output addresses a goal that deviates from the Task State field
by ≥2 points on a 5-point alignment scale, scored by blinded rater.

> **Plain language:** Should explain: 'The Task State field is a record of what the human is currently trying to accomplish, allowing us to detect when the AI's output goes off-track from that goal.'

> **Plain language:** The term 'intent-drift incident' is introduced but not defined upfront before being used in 'H1 depends on intent-drift incident rate.' Should clarify before that line: 'An intent-drift incident occurs when the AI model shifts focus away from what the human actually wanted to explore.'

> **Plain language:** Should clarify what the scale measures: 'This scale ranges from 1 (completely off-topic) to 5 (perfectly on-topic), measuring how closely the AI's response stays focused on what the human was actually asking.'

Write the rubric. Test it on two existing transcripts from the evidence
record (https://youtu.be/7iqq1nRdKFg) to confirm it produces consistent
scores. If the rubric fails on existing transcripts, fix it before
proceeding.

**May 6-7: Session recorder — core architecture**

The session recorder must capture:
- Turn number, timestamp, token count (cumulative)
- Condition assignment (1-6)
- ContractWindow state snapshot at each turn (JSON export from
  contract_window.py — this method already exists: to_json())
- BicameralReview pass/fail per turn (from bicameral_review.py)
- Human and model turn text

> **Plain language:** Should explain: 'BicameralReview is a safety or quality-check system that evaluates whether each AI model output meets certain standards, flagging it as a pass or fail.'

> **Plain language:** While referenced as an existing method, 'ContractWindow' is not explained. Should add: 'ContractWindow is a system component that tracks constraints or boundaries applied to the AI model during each turn.'

Build the recorder as a thin wrapper around existing ContractWindow and
BicameralReview classes. Target: Python script that writes
/data/sessions/[session_id].jsonl, one line per turn.

> **Plain language:** Should clarify: 'A thin wrapper is a lightweight layer of new code that collects output from existing systems without duplicating or rewriting their core logic.'

**Deliverable by May 7:** IAI rubric draft, intent-drift rubric draft,
session recorder architecture document in /docs/session-recorder-spec.md

### Week 2 (May 8-14): Build and test session recorder + invariant checkers

**May 8-10: Session recorder implementation**

> **Plain language:** ContractWindow is a software component that manages a bounded interaction session—it controls what inputs are allowed and what outputs can occur during a single conversation turn.

> **Plain language:** BicameralReview is a governance check that requires approval from two independent review processes before certain actions proceed, similar to how a legislature requires two chambers to pass a law.

> **Plain language:** JSONL is a file format where each line contains one complete JSON object; it makes it easy to stream and append data without rewriting the entire file.

Build session_recorder.py in /governance-kernel/. It wraps ContractWindow,
calls BicameralReview, writes JSONL. No UI needed. CLI-invocable.

```
python session_recorder.py --condition 2 --session-id PILOT-001
```

Test with a synthetic 10-turn session. Confirm JSONL output is parseable
and complete.

**May 11-12: Invariant checkers**

/governance-kernel/invariant-checkers/__init__.py exists but is empty.
Build checkers for the three signals that matter for H1-H3:

- check_task_state_alignment(turn_text, task_state) → alignment score 1-5
- check_comprehension_grade(text) → Flesch-Kincaid (a readability score — Grade 8 means a typical 8th-grader can understand the text) Grade Level
- check_repair_within_three_turns(session_log, incident_turn) → bool

> **Plain language:** An alignment score of 1-5 is a numerical rating where higher numbers indicate that the model's response better matches the current state and requirements of the task.

> **Plain language:** The Flesch-Kincaid Grade Level is a numerical readability metric that estimates the U.S. school grade level needed to understand a piece of text; a score of 8 means an average 8th-grader should be able to comprehend it.

These do not need to be perfect at this stage. They need to produce
consistent numeric outputs that a human rater can verify against.

**May 13-14: Data pipeline**

Build data_pipeline.py in /data/: reads JSONL files, outputs structured
CSV for statistical analysis. Required columns: session_id, condition,
turn_count, token_count, drift_incidents, repairs, ia_score, fk_grade.

> **Plain language:** Drift_incidents refers to moments in a conversation when the model's behavior or outputs noticeably shift away from its intended guidelines or task focus.

> **Plain language:** ia_score is a summary metric (likely standing for 'interaction alignment score') that measures how well the model stayed on task and within its governance boundaries across an entire session.

**Deliverable by May 14:** Working session recorder, three invariant
checkers, data pipeline that reads recorder output. All code in repo with
commit messages naming the component.

### Week 3 (May 15-22): Pilot — 10 sessions

**May 15: Session protocol document**

Write /docs/session-protocol.md before running any pilot sessions.
Specifies: task types eligible for sessions, how to assign conditions,
how to handle session abandonment, what counts as a completed session
(minimum 30 turns OR 50K tokens, whichever comes first).

**May 16-21: Run 10 pilot sessions**


> **Plain language:** A covariate is a background factor that can influence your results and that you want to track separately, so you can account for it later when analyzing whether the main thing you're testing actually made a difference. Here, logging your own cognitive load lets you check whether your fatigue (rather than the condition itself) affected your scoring.
2 sessions per condition for conditions 1-5. Skip condition 6 (combined)
until instrument is validated — the combined condition is the most complex
to score.

> **Plain language:** The document refers to different experimental conditions (labeled 1 through 6) but never explains what distinguishes them or what they test. You need to know: what variable or intervention is being manipulated across these conditions, and why condition 6 is called 'combined' and is more complex to score.

Run them across the week. Do not run more than 3 sessions in a single day.
Log cognitive load state before each session (high/medium/low) — this
is both self-care and a covariate.

> **Plain language:** The document mentions two separate scoring tools (rubrics) but does not explain what each one measures or why both are needed. You need to know what 'IAI' stands for, what it evaluates, and what 'drift' means in this context.

**During pilot sessions:**
- Record all sessions with session_recorder.py
- Score all sessions with IAI rubric and drift rubric within 24 hours
- Note every instrument failure (when rubric produces ambiguous result,
  when recorder crashes, when the checkers give implausible output)

**Deliverable by May 21:** 10 pilot sessions recorded, raw scores logged,
instrument failure list complete.

### Week 4 (May 22-31): Instrument validation and go/no-go

**May 22-25: Inter-rater reliability**

Take 5 of the 10 pilot sessions and score them yourself. Then ask one other
person — or use a different scoring pass after 48 hours — to score the
same turns. Calculate Cohen's kappa (a statistical measure of agreement between two raters — values above 0.70 indicate strong agreement) for the drift incident classification.

> **Plain language:** Cohen's kappa is already explained in the parenthetical gloss provided in the document. No flag needed.

Target: kappa ≥ 0.70. If kappa < 0.70, the rubric is ambiguous. Fix the
rubric before proceeding to full data collection. Do not collect 180
sessions with an unvalidated instrument.

This is a hard gate. If the instrument does not pass reliability by May 28,
data collection does not start June 1. It starts when the instrument is
valid. Adjust the June schedule accordingly.

**May 26-28: IAI weight calibration**


> **Plain language:** Predictive validity is mentioned as the criterion for weighting but is never defined. You should explain: 'Predictive validity means how well each component actually predicts whether drift incidents will occur in practice, based on the pilot data.'
Use the 10 pilot sessions to estimate the correlation between each IAI
component (hypothesis rate, challenge rate, scope contraction) and the
hand-coded intent-drift incident rate. Weight the composite based on
predictive validity, not intuition.

> **Plain language:** JSONL is mentioned as an output format but never explained. You should add: 'JSONL is a file format where each line contains one complete data record in JSON (a machine-readable structured format), making it easy for automated systems to read and process.'

> **Plain language:** IAI is introduced with three specific components listed, but 'IAI' itself is never defined. The reader does not know what IAI stands for or why these three specific measurements represent it. You should explain: 'IAI is a composite scoring system that measures three dimensions of how an AI system approaches problems: how often it generates new explanations, how often it questions its own reasoning, and how much it narrows the scope of what it's examining.'


> **Plain language:** Invariant checkers are mentioned without explanation of what they check for or why. You should explain: 'Invariant checkers are automated tools that verify that certain conditions remain true throughout the data collection—for example, ensuring that session IDs are consistent or that numerical scores stay within valid ranges.'
CONSTRUCTED — this correlation will be estimated from pilot data, not
validated in advance. Report the calibration method in the paper.

**May 29-31: Go/no-go decision and June schedule**

Confirm:
1. Session recorder produces complete, parseable JSONL for all 6 conditions
2. Invariant checkers produce numeric outputs without errors
3. Data pipeline reads pilot data without failures
4. Drift rubric has kappa ≥ 0.70
5. IAI weights calibrated

If all five conditions are met: go. Document in /artifacts/case-law/
RESEARCH_PLAN_GO_[DATE].md with the actual kappa score and calibration results.

If any condition fails: do not start June data collection until fixed.
One week delay in June is better than 180 sessions of unusable data.

**May hard deadline: May 31**
All infrastructure complete and validated.

---

## Month 2 — June 2026: Data Collection

**Goal:** Run the full minimum viable sample. 180 sessions, 30 per condition.
Complete by June 28. Leave June 29-30 as buffer.

> **Plain language:** This is the smallest number of research participants and observations needed to reliably answer your core research question. In this case, you need 180 total sessions divided equally across 6 different experimental conditions (30 each) to have confidence in your results.

### Realistic session schedule

**CONSTRUCTED — this schedule assumes 2-3 sessions per day on working days.
It does not assume 5+ sessions per day. Adjust based on actual May pilot
experience.**

180 sessions / 22 working days = 8.2 sessions/day if you work every day.
That is not viable. Target:

> **Plain language:** A condition is one version of the experiment you're testing—for example, one group of participants might use the AI system with feature A on, while another group uses it with feature A off. You need enough sessions in each condition to see if the differences between them are real or just random variation.

- 2-3 sessions per day
- 5-6 working days per week
- Total working days needed: 60-90 sessions / 3 per day = 20-30 days

This fits June if you treat it as a full-time data collection month with
no major distractions. The parallel work (Frontin, Graves) goes to minimum-
viable-progress mode in June — note what needs to happen, do not let it
derail session collection.

### Condition sequencing

Do not run all sessions of one condition then move to the next.
Interleave conditions daily to avoid temporal confounds (your cognitive
state, model API (Application Programming Interface — a set of rules that lets software programs talk to each other) behavior changes, external events).

> **Plain language:** Temporal confounds are factors that change over time and could unfairly affect your results—like your mental sharpness declining as the day goes on, or the API becoming slower. By mixing up the order of conditions instead of doing them one-by-one, you ensure that time-based changes don't systematically favor one condition over another.

> **Plain language:** This refers to the possibility that the AI system you're testing may perform differently at different times—for example, it might be slower during peak hours or produce slightly different outputs as its underlying software is updated. This variability could skew your results if you always test one condition at the same time of day.

Suggested daily pattern:
- Morning: Condition 1 (baseline) + Condition 6 (combined) — these are
  the reference endpoints and need clean heads.
- Afternoon: Conditions 2, 3, 4, 5 in rotation.

### Session tracking

> **Plain language:** A measurement of how mentally taxed or tired the participant reported feeling before the session began, used to control for whether fatigue influenced their performance.

Maintain /data/session-log.csv updated after every session:
- session_id, condition, date, duration_minutes, turn_count, token_count,
  completion_status (COMPLETE/ABANDONED/PARTIAL), cognitive_load_pre_session

> **Plain language:** A unique identifier assigned to each individual conversation or interaction recorded in the study, used to link all data (audio, turns, tokens) belonging to that single participant session.

> **Plain language:** The experimental treatment or version the participant was assigned to (for example, if testing different AI systems or interfaces, this identifies which variant they used).

> **Plain language:** The number of back-and-forth exchanges between the participant and the system—each time the participant sends a message and receives a response counts as one turn.

> **Plain language:** The total number of language units (roughly words or small word-pieces) processed by the AI system during the session; this measures computational complexity and cost.

COMPLETE = ≥30 turns or ≥50K tokens, recorder functioned, no instrument
failures that required restarting.

> **Plain language:** A follow-up analysis that re-runs the main findings using slightly different data (in this case, PARTIAL sessions) to verify the results are robust and not dependent on exactly which sessions you include.

> **Plain language:** Sessions qualify as COMPLETE if they meet at least one of two thresholds: either the participant completed at least 30 exchanges with the system, or the system processed at least 50,000 tokens; this ensures sufficient data was collected for analysis.

ABANDONED = stopped before threshold for any reason. Log reason. Do not
include in analysis.

PARTIAL = 20-29 turns, recorder functioned. Log separately. May be usable
as a sensitivity check but not primary analysis.

### Mid-month gate (June 15)

By June 15, check:
- Sessions completed per condition
- Any systematic failures (one condition consistently producing
  abandoned sessions — that is a design signal, not bad luck)
- Cognitive load log — if you have logged 5+ "HIGH" days in a row,
  take a recovery day. One lost day is better than three days of garbage data.

If behind schedule by ≥20 sessions on June 15: do not try to make it up
by running 5+ sessions/day. Reduce scope explicitly. If n=25 per condition
is where you land, report n=25 and run the power analysis for n=25. Do not
manufacture sessions.

### Frontin at WorldMart — June minimum viable progress

The paper is substantially complete. In June it needs:
- One empirical validation pass: run 5-10 test prompts through a frontier
  model about Black consumer behavior and score the outputs against the
  Eight Wonders rubric. This is the "fluent wrong answer" documentation
  the paper needs.
- Do this in the last week of June, not before. Primary task in June is CW

> **Plain language:** A frontier model is one of the most advanced AI systems currently available—essentially the state-of-the-art language model that represents the cutting edge of what's possible today. Testing against the newest model helps determine whether problems are inherent to all AI systems or specific to older versions.
  sessions.

> **Plain language:** The Eight Wonders rubric is the evaluation framework being used in this project to assess and categorize the types of errors or biases that appear in the model's outputs. You should clarify what the rubric measures (e.g., does it score factual accuracy, bias categories, reasoning quality, or something else).

> **Plain language:** A fluent wrong answer is when an AI system generates output that sounds confident and well-reasoned but is actually incorrect or misleading. This is particularly dangerous because it convinces readers without signaling uncertainty.

### Graves disease analysis — June minimum viable progress

Note the next analytical step but do not execute it in June. The CRISP-DM (Cross-Industry Standard Process for Data Mining — a standard workflow for data analysis projects, from business understanding through deployment)
analysis needs your focused attention. It will get that in August once
the CW paper is drafted.

**June hard deadline: June 28**
All 180 sessions recorded (or actual final n documented with reason).

---

## Month 3 — July 2026: Analysis and Results

**Goal:** Statistical analysis complete, results section drafted, H1/H2/H3
evaluated. No ambiguity about whether hypotheses are supported.

### Week 1 (July 1-7): Data cleaning and scoring

**July 1-3:**
- Run data_pipeline.py on all sessions
- Flag any sessions with incomplete records, recorder errors, or missing fields
- Document exclusions explicitly in /data/exclusions.md with reason per session
- Final analysis n may differ from collection n — report both

**July 4-7:**
- Score all sessions with drift rubric (if not scored during collection)
- Score all sessions with IAI rubric
- Confirm scorer does not know condition assignments during scoring
  (blind scoring). This matters especially if you are both the experimenter
  and the rater. Use session IDs only during the scoring pass, then merge
  with condition labels afterward.

> **Plain language:** This is a computer script that processes raw video or audio recordings to extract the information needed for analysis. It likely removes duplicates, fills in missing pieces, and organizes everything into a standard format for the next step.

CONSTRUCTED — single-investigator blindness is imperfect. Acknowledge this
as a limitation in the paper.


> **Plain language:** A drift rubric is a checklist or scoring guide that measures how much a conversation, performance, or behavior moved away from its original direction or intent. In this study, it likely assesses whether participants' responses stayed consistent or drifted to different topics.
### Week 2 (July 8-14): Primary statistical analysis

> **Plain language:** The IAI rubric is the specific scoring guide you are using to measure whatever concept IAI represents; without knowing what IAI stands for in your study, readers cannot understand what dimension of the data is being measured or why it matters.


> **Plain language:** Blind scoring means the person rating the recordings does not know which group (control, treatment A, treatment B, etc.) each session belongs to, so their judgments cannot be unconsciously biased by knowing what result is expected.
**H1 analysis:**
- DV: intent-drift incident rate (incidents per 10 turns)
- Comparison: Condition 2 (CW only) vs Condition 1 (baseline)
- Test: independent samples t-test or Mann-Whitney (a statistical test that compares two groups without assuming the data follows a normal distribution) U if non-normal
- Effect size: Cohen's d
- Claim threshold: ≥25% reduction, statistically significant at α=0.05

> **Plain language:** This is a measurement of how often the AI system's responses start moving away from the user's original intent or goals during a conversation, counted as the number of such incidents that occur for every 10 user messages.

> **Plain language:** This is the threshold for statistical significance; it means we will only accept a result as reliable if there is less than a 5% chance it happened by random luck.

> **Plain language:** Cohen's d is a number that describes how big the practical difference is between two groups — a way to measure whether a statistically significant result is actually meaningful in the real world.

Also run one-way ANOVA (Analysis of Variance — a statistical test that checks whether the means of three or more groups differ significantly) across all 6 conditions. If significant, run
Tukey HSD (a statistical test that compares every pair of groups after an ANOVA, while controlling for false positives) post-hoc. Report all pairwise comparisons.

**H2 analysis:**
- DV: drift repair rate (proportion of drift incidents resolved within 3 turns)
- Comparison: Condition 3 (bilateral) vs unilateral conditions
- Test: chi-square test on repair rate proportions
- Claim threshold: ≥2x improvement

> **Plain language:** This measures how successful the system is at fixing cases where the conversation has drifted off-topic, specifically counting what fraction of drift incidents are corrected within the next 3 user messages.

**H3 analysis:**
- DV: lay reader comprehension accuracy (% correct on session-state questions)
- Sample: 15-20 lay readers, each evaluating 2-3 CW outputs from Condition 6
- Material: CW render() output from session_recorder, formatted per protocol
- Comprehension questions: 5 per output, written and validated in July Week 1
- Claim threshold: ≥80% accuracy

> **Plain language:** This is a test of how well ordinary people (not AI experts) can understand what the AI system is doing, measured by asking them questions about the conversation state and checking what percentage they answer correctly.

> **Plain language:** These are questions that ask a reader about the current state of the conversation — for example, what the user's goal was, or what the system was trying to do — to measure whether the system's behavior is transparent or confusing.
- Test: one-sample proportion test against 80% null

> **Plain language:** This is a statistical test that checks whether a measured percentage (like comprehension accuracy) is meaningfully different from a target percentage (in this case, 80%).

> **Plain language:** This refers to the formatted, readable version of the system's output that is displayed to users or readers — the end product that shows what the system actually communicated.

H3 requires recruiting 15-20 lay readers. This needs to happen in the first
week of July, not the second. Who are they? Family members, community
contacts, anyone without AI/CS background. Compensate their time.
Do not start H3 analysis without actual lay readers.

**July 14: Analysis complete**

All three hypotheses evaluated. Results are what they are. If H1 is not
supported, that is a finding. Write it that way.

### Week 3 (July 15-21): Results section draft

Write the results section first, before the introduction or discussion.
Results section contains:


> **Plain language:** A statistical calculation that determines whether your sample size was large enough to reliably detect the effect you're studying; it shows you didn't just get lucky with your results.
1. Sample description: final n per condition, exclusions, power analysis
   for actual n
2. H1 results: effect size, CI, p-value, whether ≥25% threshold met
3. H2 results: repair rate comparison, odds ratio, whether ≥2x threshold met
4. H3 results: comprehension accuracy, CI, whether ≥80% threshold met
5. Secondary analysis: IAI scores across conditions, correlation with
   drift incident rate

> **Plain language:** A number indicating how likely your result would occur by pure chance if there were actually no real effect; smaller p-values mean your finding is less likely to be a fluke.

> **Plain language:** A range of numbers (confidence interval) that tells you where the true result probably lies—for example, if your effect size is 0.5 with a CI of 0.3 to 0.7, the real value is likely somewhere in that band.

> **Plain language:** A number that measures how big the difference or relationship actually is between your conditions—not just whether it's real, but how substantial it is.
6. One figure: grouped bar chart, drift incident rate by condition with

> **Plain language:** A number comparing how much more (or less) likely one outcome is versus another between two groups—for example, an odds ratio of 2 means one group is twice as likely to have the outcome.
   95% CIs

> **Plain language:** The percentage or proportion of questions or tasks that participants answered or completed correctly.

> **Plain language:** Confidence intervals set at the 95% level, meaning there is a 95% probability that the true value falls within the range shown by the error bars on the chart.

> **Plain language:** The frequency or proportion of times a particular type of failure or problem (drift incidents) occurred; this matters because you're checking whether it correlates with the IAI scores.

> **Plain language:** Numerical measurements on the IAI scale; without knowing what IAI stands for earlier in the document, a reader cannot understand what is being measured.

Do not interpret in the results section. Save interpretation for discussion.

**July 21: Results section complete, figures final**

### Week 4 (July 22-31): Frontin WorldMart empirical pass

The 5-10 test prompts run in June need to be scored and written up.
Formalize this as an appendix or supplementary analysis for the CW paper,
or as a standalone short paper.

> **Plain language:** CW is an abbreviation; clarify what 'CW' stands for and what this paper is about (e.g., 'the Crowdworker Validation study' or 'the Content Moderation Warnings research').

Determine by July 25 which it is. If the WorldMart empirical results are
strong, they belong in the paper. If they are preliminary, they go in
supplementary materials with a note that full validation is ongoing.

> **Plain language:** These appear to be hypothesis labels but the document never defines what H1, H2, and H3 are testing or why these three hypotheses matter to the research.

**July 31 hard deadline:**
- Statistical analysis complete and documented in /analysis/
- Results section complete in /paper/results.md
- H1/H2/H3 each evaluated with a clear TRUE/FALSE/INCONCLUSIVE designation
- WorldMart empirical disposition decided

---

## Month 4 — August 2026: Writing and Submission

**Goal:** Complete paper ready for submission by August 28.

### Week 1 (August 1-7): Paper skeleton and introduction

**August 1-3:**
Draft introduction from executive-summary-proposal.md. The proposal is
substantially the introduction. Tighten it. The introduction must:
- State the problem (Insight Atrophy, fluent wrong answers)
- State the contribution (Contract Window + 6 invariants)
- State the empirical claim (H1/H2/H3, now with actual results)
- Preview the structure

Do not write a different paper than the proposal describes. The theory is
done. You are adding empirical results to an existing argument.

**August 4-7:**
- Methods section: session protocol, condition specifications, instruments,
  blinding procedure, statistical tests. Write from documentation you
  already created in May/June.
- Related work: minimum viable — Constitutional AI (a training method where an AI evaluates its own outputs against a written set of principles before showing them to the user), scalable oversight (a research area focused on how humans can supervise AI systems even when those systems become more capable than the humans overseeing them),

> **Plain language:** Insight Atrophy is the phenomenon where an AI system produces answers that sound confident and fluent but are actually incorrect or misleading, causing users to lose the ability to recognize flaws in AI reasoning. This matters because users may trust AI outputs without proper verification, leading to bad decisions.
  accessibility in AI. Verify all citations (author, venue, year) before

> **Plain language:** The Contract Window is a method or framework for controlling when and how an AI system provides responses, and the 6 invariants are specific rules or properties that must always hold true to ensure the system behaves reliably. Together they represent the proposed solution to the Insight Atrophy problem.
  writing them. I3 — confidence requires verification applies here too.

> **Plain language:** H1, H2, and H3 are three specific hypotheses (testable predictions) that the experiment is designed to evaluate. These are the measurable claims about how the Contract Window and invariants actually perform in practice.

### Week 2 (August 8-14): Discussion, limitations, conclusion

**Discussion:**
- What the results mean for the three hypotheses
- Why the effect pattern makes sense given the architecture
- What the IAI score distribution tells you
- What failed and why

> **Plain language:** IAI (Interpretability Alignment Index) is a numerical measurement of how well the model's outputs align with human expectations; the distribution refers to how these scores spread across your sample—whether most scores cluster in one range or vary widely.

**Limitations section** — write this from the proposal limitations plus
empirical discoveries. Be direct about:
- Single investigator as both experimenter and rater (partial blindness)
- MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful difference) power at d=0.5 if you ran n=30
- Observational foundation of the invariant set

> **Plain language:** A blinding procedure is a method where participants or researchers are kept unaware of which experimental condition (treatment or control) is being used, to prevent bias from influencing results. This ensures that expectations about the intervention do not unconsciously affect how people rate or respond to the system.
- Lay reader sample not probability-sampled

> **Plain language:** Your lay readers were chosen by convenience (e.g., volunteers you recruited) rather than by random selection from the full population of possible lay readers, so they may differ systematically from the broader public in ways that affect your findings.

> **Plain language:** This means you knew which condition each participant was in while rating their responses, so your ratings could have been unconsciously influenced by knowing the hypothesis or treatment group.

> **Plain language:** This limitation means your identification of which outputs count as reliable or stable (the 'invariant set') came from watching what happened in your data rather than from a pre-registered prediction, so you may have unconsciously included or excluded cases that fit your hypothesis.

> **Plain language:** The parenthetical is present but incomplete for a lay reader; consider adding: 'At d=0.5 with n=30, your study would have roughly a 47% chance of detecting a real effect if one exists—well below the standard 80% threshold, so if you find nothing, that may reflect your small sample rather than a true absence of effect.'

**Do not soften the limitations.** The paper's credibility depends on
honest accounting of what this experiment can and cannot support.

**Conclusion:**
One paragraph. What does the Contract Window do. What the data showed.
What the next study needs to be.

### Week 3 (August 15-21): Citation verification and paper integration

**August 15-17:**
Citation Research Protocol pass. Every reference in the paper:
- Author names verified
- Venue name verified (do not write "Anthropic" as a venue — find the
  actual publication venue)
- Year verified
- URL or DOI if available

Specific citations to verify:
- Bai et al. (2022) Constitutional AI — verify full citation
- Leike et al. scalable agent alignment — verify year, venue, full title
- Davis & Garrett-Staib (2013) — verify against Focus on Colleges,
  Universities, and Schools actual title
- Any additional references added during writing

> **Plain language:** A quality control process where two separate reviewers—one checking whether the work answers the research question, and one checking for unfounded claims—must both approve the output before it is shared. Neither reviewer can override the other's decision.

> **Plain language:** A claim presented as fact or supported by evidence when it is actually unsupported, unverified, or based on a misinterpretation of the data. Phantom claims mislead readers into accepting conclusions that the evidence does not justify.

**August 18-21:**
Full paper integration pass. Read it as one document. Check:
- Does the methods section actually describe what you did?
- Does the results section report what the analysis produced?
- Do the limitations acknowledge what the data cannot support?
- Are all empirical claims tagged VERIFIED or PENDING if still pending?
- Does every figure have a caption that states the main finding?

Run the paper through the Bicameral Review (two independent review channels that must both approve an output before it reaches the user — neither can override the other): relational channel (does this
advance the research question?) and safety channel (does this introduce a
phantom claim?).

### Week 4 (August 22-28): Final review and submission

**August 22-25:**
Send to two trusted readers for feedback. If you have no trusted readers
available, do a cold pass: read the paper aloud. Listen for where you skip
or speed through — those are the sections that need work.

Address feedback. Do not rewrite the paper. Fix specific problems.

**Venue decision:**

Target conference options:
- NeurIPS 2026 workshop tracks (Workshop on AI Safety, SoLaR workshop, or
  similar): deadline typically September-October 2026. August 28 draft
  positions you to submit in that window.
- FAccT 2027 main track: deadline typically January-February 2027. A
  complete draft by August 2026 gives you 5 months to revise.
- AIES 2026 or similar: check CFP deadlines as they are announced.

> **Plain language:** Phantom work means investing effort on a task that cannot possibly succeed — in this case, submitting to a conference deadline that has already passed. The reference 'I2' appears to be an internal indexing system; the core point is that you should avoid wasting time on impossible goals.

Do not target NeurIPS 2026 main track or FAccT 2026 main track — those
deadlines were May/June 2026 and January/February 2026 respectively, both
before this plan produces a complete paper. Submitting to a deadline you
cannot meet is phantom work (I2).

> **Plain language:** An empirical claim is any statement about how the world actually works, based on observation or experiment — as opposed to pure logic or opinion. For example, 'our model achieved 87% accuracy' is empirical; 'we should prioritize safety' is not.

> **Plain language:** This means you must explicitly state which claims in your paper are based on solid evidence (verified) and which are new ideas you're proposing (truth-claims). Every factual statement should be marked with where it comes from — your own experiments, published research, or your new argument.

**August 28: Submission-ready draft complete.**

Final V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work) pass on the paper before submission. Every empirical claim must
be tagged with its evidence basis.

**August 29-31: Buffer.**

Use this time only for venue-specific formatting if submitting to an
August or early September deadline. Otherwise this is recovery time.

---

## Parallel Research Domains — Minimum Viable Progress

### Domain 2: Frontin at WorldMart

- May: No active work. Paper is substantially complete. Leave it.
- June: Run 5-10 empirical prompt validation tests. Log results.
- July: Score and write up empirical validation. Decide: CW paper appendix
  or standalone.
- August: If standalone, draft abstract and first section. Target venue TBD.

### Domain 3: Graves Disease Analysis

- May through July: Minimum viable progress. Note next steps. Do not execute.
- August: After CW paper is submitted, resume CRISP-DM (Cross-Industry Standard Process for Data Mining — a standard workflow for data analysis projects, from business understanding through deployment) analysis. August 29-31
  buffer can be the entry point if the paper is done.

The parallel domains are real research. They are not active in the months
when data collection and analysis consume the primary bandwidth. This is
not abandonment — it is sequencing. The Contract Window experiment is the
critical path.

---

## Risk Register

**CONSTRUCTED — these are anticipated risks, not documented incidents**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Instrument fails kappa gate in May | Medium | High | Two-week fix window before June data starts |
| Session recorder crashes mid-session | Medium | Medium | Test thoroughly in May; backup: manual transcript |
| Data collection falls short of n=30/condition | Medium | Medium | Reduce n, run power analysis for actual n, report honestly |
| Lay reader recruitment fails for H3 | Low-Medium | High | Start recruiting in late June, not July |
| Health/cognitive crash during June | Medium | High | Pre-planned recovery days in schedule; 2-session max on hard days |

> **Plain language:** A kappa gate is a validation checkpoint that checks whether your measurement instrument (the tool you're using to collect data) is producing consistent and reliable results. If it fails, it means the instrument isn't working well enough to trust for your actual study.
| Analysis reveals instrument invalidity | Low | Very High | Pilot validation gate in May is the firewall |
| Citation verification fails for key reference | Medium | Medium | Do not cite without verifying; PENDING tag until confirmed |

> **Plain language:** This refers to collecting data from 30 participants in each separate group or condition of your study. If you fall short, you have fewer data points to analyze, which weakens your statistical conclusions.

> **Plain language:** A pilot validation gate is a checkpoint where you test your instrument on a small sample before your main study to catch problems early. This acts as a firewall by preventing you from proceeding to the expensive main study if the instrument isn't working.

> **Plain language:** H3 is shorthand for your third hypothesis—a specific prediction you're testing in the study. Lay readers are people without expert training who will help validate whether your findings make sense to non-specialists.

> **Plain language:** Instrument invalidity means your measurement tool is not actually measuring what you intended it to measure, which would make all your results unreliable and unusable.

---

## File Structure

Deliverables created during this plan go here:

```
/docs/
  session-protocol.md          — May 15
  session-recorder-spec.md     — May 7

/governance-kernel/
  invariant-checkers/          — operational by May 14
  session_recorder.py          — operational by May 10

/data/
  session-log.csv              — updated daily during June
  exclusions.md                — July 1-3
  /sessions/                   — one JSONL per session

/analysis/
  h1_analysis.py               — July 8-14
  h2_analysis.py               — July 8-14
  h3_analysis.py               — July 8-14
  results_tables.csv           — July 14

/paper/
  results.md                   — July 21
  methods.md                   — August 7
  introduction.md              — August 7
  discussion.md                — August 14
  limitations.md               — August 14
  references_verified.bib      — August 17
  full_paper.md                — August 21
  submission_ready.pdf         — August 28

/artifacts/case-law/
  RESEARCH_PLAN_GO_[DATE].md   — May 29-31
  [any BREAK_GLASS files]      — as needed
```

---

## Non-Negotiables

These are not preferences. They are constraints derived from I1-I6 and
from honest accounting of single-investigator cognitive limits.

1. Do not start June data collection with an unvalidated instrument.
2. Do not report n=360 if you ran n=150. Report what you ran.
3. Do not cite a source you have not verified. Tag it PENDING until verified.
4. Do not claim a hypothesis is supported if the statistical threshold was
   not met. Label it INCONCLUSIVE or FAILED. Both are publishable findings.
5. Do not run data collection sessions when cognitive load is HIGH. That
   data is not clean. One absent session costs less than six corrupted ones.
6. Do not work on Frontin or Graves during active data collection weeks
   unless you are in a burst that does not touch the primary pipeline.

---

> **Plain language:** I1-I6 refers to six foundational principles or investigator commitments that form the basis for these constraints; the reader needs to know what these six items are or where to find them to understand why these rules exist.

V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work): research-plan.md — EXISTS (written, complete) → VERIFIED AGAINST
executive-summary-proposal.md (hypotheses, conditions, design), AGENTS.md
(I1-I6, V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work) format), contract_window.py (instrument status), BREAK_GLASS
case law (governance protocol) → NOT CLAIMED: any empirical results
(none exist), completion of any milestone (all targets are forward-looking),
publication at any specific venue (deadlines must be confirmed when CFPs
are released), n=360 feasibility (explicitly contested and replaced with
MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful difference) n=180) → FUNCTIONAL STATUS: operative research plan, ready for
execution beginning May 1, 2026

> **Plain language:** While a definition is provided in parentheses, 'adequate statistical power' and 'meaningful difference' are themselves technical terms that a non-specialist may not understand; the plain-language version should explain that this is the smallest group size needed to reliably detect a real effect in the data.

> **Plain language:** This refers to a specific, measurable threshold of mental fatigue or distraction that has been defined elsewhere in the project; without knowing the operational definition or measurement, it is unclear when this rule applies.

> **Plain language:** Frontin and Graves are referenced as separate work streams or projects; the reader should understand what these are and why they compete for attention with data collection.

> **Plain language:** This phrase implies there is a defined schedule distinguishing 'active data collection weeks' from other periods; the reader should know how this calendar or status is determined.

> **Plain language:** A 'burst' and 'primary pipeline' are terms that describe a specific workflow or scheduling pattern used in this project; their meaning should be clarified so the exception is actionable.