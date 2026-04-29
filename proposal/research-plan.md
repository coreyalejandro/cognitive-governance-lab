# 4-Month Research Plan: Cognitive Governance Lab
## Empirical Validation of the Contract Window Architecture

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
            empirical validation. Tertiary: Graves disease analysis.

INVARIANT STATUS: I1 active — all claims tagged. I2 active — no phantom work,
                  deadlines are targets not achievements. I3 active — this plan
                  does not assume the hypotheses are true. I4 active — every
                  milestone traces to a research component.

REPAIR OBLIGATIONS: None at plan initialization. Violations logged in
                    /artifacts/case-law/ as they occur.

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

### Minimum Viable Sample (MVS)

**Proposed MVS: n=30 per condition = 180 sessions total**

Power analysis for primary comparison (H1: Condition 2 vs Condition 1):
- Two-sample t-test, two-tailed, α=0.05
- At n=30 per group, Cohen's d=0.5 (medium effect): power ≈ 0.62
- At n=30 per group, Cohen's d=0.8 (large effect): power ≈ 0.90
- At n=60 per group, Cohen's d=0.5: power ≈ 0.80 (original target)

**The tradeoff stated plainly:**

Running n=30 at d=0.5 gives you 62% power — a 38% chance of a false
negative. That is not ideal. But running 180 sessions you can actually
complete is better science than planning 360 sessions and stopping at 140
when you are exhausted and calling it "preliminary data."

If the effect size is large (d≥0.8), n=30 is adequately powered. The
Contract Window architecture is designed to produce large effects because
it addresses a structural failure mode, not a marginal one. If the effect
is only medium and n=30 misses it, that is a finding that needs a better-
resourced follow-up study — not a reason to fabricate completion of 360
sessions you did not run.

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

### Week 1 (May 1-7): Insight Atrophy Index operationalization

**May 1-3: Define IAI operationally**

CONSTRUCTED — the construct exists in the proposal. The measurement
instrument does not. Do this first because everything else depends on it.

Operationalize IAI as a composite of three observable turn-level signals:
1. Hypothesis generation rate — number of competing hypotheses surfaced
   per 10 turns, measured by the session recorder.
2. Challenge rate — number of times human explicitly contests model
   output vs accepts without interrogation, per 10 turns.
3. Scope contraction — whether the human's question set narrows or
   expands across session thirds (early/mid/late), coded from transcript.

These three signals can be extracted from transcripts by a blinded rater
using a rubric. The IAI score is a weighted composite. Weight determination
requires the pilot (see Week 3).

**May 4-5: Intent-drift incident rubric**

H1 depends on intent-drift incident rate. The rubric needs to exist before
pilot sessions. Draft the rubric: a turn is an intent-drift incident when
the model's output addresses a goal that deviates from the Task State field
by ≥2 points on a 5-point alignment scale, scored by blinded rater.

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

Build the recorder as a thin wrapper around existing ContractWindow and
BicameralReview classes. Target: Python script that writes
/data/sessions/[session_id].jsonl, one line per turn.

**Deliverable by May 7:** IAI rubric draft, intent-drift rubric draft,
session recorder architecture document in /docs/session-recorder-spec.md

### Week 2 (May 8-14): Build and test session recorder + invariant checkers

**May 8-10: Session recorder implementation**

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
- check_comprehension_grade(text) → Flesch-Kincaid Grade Level
- check_repair_within_three_turns(session_log, incident_turn) → bool

These do not need to be perfect at this stage. They need to produce
consistent numeric outputs that a human rater can verify against.

**May 13-14: Data pipeline**

Build data_pipeline.py in /data/: reads JSONL files, outputs structured
CSV for statistical analysis. Required columns: session_id, condition,
turn_count, token_count, drift_incidents, repairs, ia_score, fk_grade.

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

2 sessions per condition for conditions 1-5. Skip condition 6 (combined)
until instrument is validated — the combined condition is the most complex
to score.

Run them across the week. Do not run more than 3 sessions in a single day.
Log cognitive load state before each session (high/medium/low) — this
is both self-care and a covariate.

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
same turns. Calculate Cohen's kappa for the drift incident classification.

Target: kappa ≥ 0.70. If kappa < 0.70, the rubric is ambiguous. Fix the
rubric before proceeding to full data collection. Do not collect 180
sessions with an unvalidated instrument.

This is a hard gate. If the instrument does not pass reliability by May 28,
data collection does not start June 1. It starts when the instrument is
valid. Adjust the June schedule accordingly.

**May 26-28: IAI weight calibration**

Use the 10 pilot sessions to estimate the correlation between each IAI
component (hypothesis rate, challenge rate, scope contraction) and the
hand-coded intent-drift incident rate. Weight the composite based on
predictive validity, not intuition.

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

### Realistic session schedule

**CONSTRUCTED — this schedule assumes 2-3 sessions per day on working days.
It does not assume 5+ sessions per day. Adjust based on actual May pilot
experience.**

180 sessions / 22 working days = 8.2 sessions/day if you work every day.
That is not viable. Target:

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
state, model API behavior changes, external events).

Suggested daily pattern:
- Morning: Condition 1 (baseline) + Condition 6 (combined) — these are
  the reference endpoints and need clean heads.
- Afternoon: Conditions 2, 3, 4, 5 in rotation.

### Session tracking

Maintain /data/session-log.csv updated after every session:
- session_id, condition, date, duration_minutes, turn_count, token_count,
  completion_status (COMPLETE/ABANDONED/PARTIAL), cognitive_load_pre_session

COMPLETE = ≥30 turns or ≥50K tokens, recorder functioned, no instrument
failures that required restarting.

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
  sessions.

### Graves disease analysis — June minimum viable progress

Note the next analytical step but do not execute it in June. The CRISP-DM
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

CONSTRUCTED — single-investigator blindness is imperfect. Acknowledge this
as a limitation in the paper.

### Week 2 (July 8-14): Primary statistical analysis

**H1 analysis:**
- DV: intent-drift incident rate (incidents per 10 turns)
- Comparison: Condition 2 (CW only) vs Condition 1 (baseline)
- Test: independent samples t-test or Mann-Whitney U if non-normal
- Effect size: Cohen's d
- Claim threshold: ≥25% reduction, statistically significant at α=0.05

Also run one-way ANOVA across all 6 conditions. If significant, run
Tukey HSD post-hoc. Report all pairwise comparisons.

**H2 analysis:**
- DV: drift repair rate (proportion of drift incidents resolved within 3 turns)
- Comparison: Condition 3 (bilateral) vs unilateral conditions
- Test: chi-square test on repair rate proportions
- Claim threshold: ≥2x improvement

**H3 analysis:**
- DV: lay reader comprehension accuracy (% correct on session-state questions)
- Sample: 15-20 lay readers, each evaluating 2-3 CW outputs from Condition 6
- Material: CW render() output from session_recorder, formatted per protocol
- Comprehension questions: 5 per output, written and validated in July Week 1
- Claim threshold: ≥80% accuracy
- Test: one-sample proportion test against 80% null

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

1. Sample description: final n per condition, exclusions, power analysis
   for actual n
2. H1 results: effect size, CI, p-value, whether ≥25% threshold met
3. H2 results: repair rate comparison, odds ratio, whether ≥2x threshold met
4. H3 results: comprehension accuracy, CI, whether ≥80% threshold met
5. Secondary analysis: IAI scores across conditions, correlation with
   drift incident rate
6. One figure: grouped bar chart, drift incident rate by condition with
   95% CIs

Do not interpret in the results section. Save interpretation for discussion.

**July 21: Results section complete, figures final**

### Week 4 (July 22-31): Frontin WorldMart empirical pass

The 5-10 test prompts run in June need to be scored and written up.
Formalize this as an appendix or supplementary analysis for the CW paper,
or as a standalone short paper.

Determine by July 25 which it is. If the WorldMart empirical results are
strong, they belong in the paper. If they are preliminary, they go in
supplementary materials with a note that full validation is ongoing.

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
- Related work: minimum viable — Constitutional AI, scalable oversight,
  accessibility in AI. Verify all citations (author, venue, year) before
  writing them. I3 — confidence requires verification applies here too.

### Week 2 (August 8-14): Discussion, limitations, conclusion

**Discussion:**
- What the results mean for the three hypotheses
- Why the effect pattern makes sense given the architecture
- What the IAI score distribution tells you
- What failed and why

**Limitations section** — write this from the proposal limitations plus
empirical discoveries. Be direct about:
- Single investigator as both experimenter and rater (partial blindness)
- MVS power at d=0.5 if you ran n=30
- Observational foundation of the invariant set
- Lay reader sample not probability-sampled

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

**August 18-21:**
Full paper integration pass. Read it as one document. Check:
- Does the methods section actually describe what you did?
- Does the results section report what the analysis produced?
- Do the limitations acknowledge what the data cannot support?
- Are all empirical claims tagged VERIFIED or PENDING if still pending?
- Does every figure have a caption that states the main finding?

Run the paper through the Bicameral Review: relational channel (does this
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

Do not target NeurIPS 2026 main track or FAccT 2026 main track — those
deadlines were May/June 2026 and January/February 2026 respectively, both
before this plan produces a complete paper. Submitting to a deadline you
cannot meet is phantom work (I2).

**August 28: Submission-ready draft complete.**

Final V&T pass on the paper before submission. Every empirical claim must
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
- August: After CW paper is submitted, resume CRISP-DM analysis. August 29-31
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
| Analysis reveals instrument invalidity | Low | Very High | Pilot validation gate in May is the firewall |
| Citation verification fails for key reference | Medium | Medium | Do not cite without verifying; PENDING tag until confirmed |

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

V&T: research-plan.md — EXISTS (written, complete) → VERIFIED AGAINST
executive-summary-proposal.md (hypotheses, conditions, design), AGENTS.md
(I1-I6, V&T format), contract_window.py (instrument status), BREAK_GLASS
case law (governance protocol) → NOT CLAIMED: any empirical results
(none exist), completion of any milestone (all targets are forward-looking),
publication at any specific venue (deadlines must be confirmed when CFPs
are released), n=360 feasibility (explicitly contested and replaced with
MVS n=180) → FUNCTIONAL STATUS: operative research plan, ready for
execution beginning May 1, 2026
