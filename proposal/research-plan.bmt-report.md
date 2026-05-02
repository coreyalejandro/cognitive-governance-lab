# BMT Audit Report

**File:** research-plan.md
**Audited:** 2026-05-01T07:52:31.504757+00:00
**Violations found:** 113 (BMT-1: 5, BMT-2: 108, BMT-4: 0)
**Standard:** Blind Man's Test v1.0 — Doctrine 4, The Living Constitution

---

## BMT Requirements Reference

**BMT-1 (Abbreviations):** Every abbreviation or jargon term must be spelled out
  in parentheses on first use. Example: LLM (large language model).

**BMT-2 (Concept Explanation):** Every concept, claim, governance rule, or
  specialized idea introduced must be followed by at least one plain-language
  sentence. A parenthetical expansion is not enough. The reader must understand
  what the concept is, why it matters, and what problem it addresses.
  Standard: readable by a smart adult with zero prior knowledge of AI research.

**BMT-4 (Status Labels):** If CONSTRUCTED/VERIFIED/PENDING tags are used,
  a legend defining them must appear at the top of the document.

---

## Result: VIOLATIONS FOUND — AUTO-FIX APPLIED

Violations detected and automatically patched in the original file.
This report is the permanent record of what was wrong before the fix.

### BMT-1 Violations (Undefined Abbreviations/Jargon)

| # | Line | Excerpt | Fix Applied |
|---|------|---------|-------------|
| 1 | 36 | UNKNOWN: Whether n=30/condition (MVS) will replicate at n=60/condition. | Define "MVS" on first use: MVS (Minimum Viable Sample — the smallest sample size that gives adequate |
| 2 | 56 | ### Minimum Viable Sample (MVS) | Define "MVS" on first use: MVS (Minimum Viable Sample — the smallest sample size that gives adequate |
| 3 | 336 | Note the next analytical step but do not execute it in June. The CRISP-DM (Cross-Industry Standard P | Define "CRISP-DM" on first use: CRISP-DM (Cross-Industry Standard Process for Data Mining — a standa |
| 4 | 463 | - Related work: minimum viable — Constitutional AI (a training method where an AI evaluates its own  | Define "scalable oversight" on first use: scalable oversight (a research area focused on how humans  |
| 5 | 544 | Final V&T (Verification and Truth — a statement that explicitly separates what is confirmed from wha | Define "V&T" on first use: V&T (Verification and Truth — a statement that explicitly separates what  |

### BMT-2 Violations (Concepts Without Plain-Language Explanation)

These are the deeper violations — the standard exposed by the ChatGPT
translation benchmark. Each item below is a concept that was introduced
without the follow-up sentence a zero-prior-knowledge reader needs.

| # | Line | Concept | Explanation Inserted |
|---|------|---------|----------------------|
| 1 | 6 | Empirical Validation of the Contract Window (a structured record... | A Contract Window is a shared document or data structure that tracks what a person and an AI system  |
| 2 | 6 | Cognitive Governance Lab | Cognitive Governance refers to systematic methods for overseeing and managing how AI systems make de |
| 3 | 15 | Evidence Basis: CONSTRUCTED — this plan is forward-looking. | This plan describes research that has not yet been conducted; it is a roadmap of intended work rathe |
| 4 | 14 | ...on the Contract Window architecture for human-AI collaborative... | This is a system design where humans and AI agree on explicit rules or 'contracts' at the start of t |
| 5 | 18 | INVARIANT STATUS (whether the hard behavioral rules the AI committed to...) | This is a snapshot of which core promises or commitments the AI made at the beginning are still bein |
| 6 | 19 | ...I2 active — no phantom work, deadlines are targets not achievements. | This means the AI will not pretend to have completed research tasks or make claims about findings th |
| 7 | 21 | REPAIR OBLIGATIONS: None at plan initialization. Violations logged in... | These are debts or commitments the AI owes to fix past mistakes; logging violations means recording  |
| 8 | 23 | CONSTRUCTED: Hypotheses H1, H2, H3 — derived from longitudinal observation... | This label means the hypotheses were built from watching trends over time in the real world, not fro |
| 9 | 26 | ...Whether n=30/condition (MVS) will replicate at n=60/condition. | This refers to a test run with 30 participants in each group (n=30/condition) using a specific metho |
| 10 | 52 | This is flagged per I2 — No Phantom Work. Do not plan 360 sessions... | I2 is a governance rule that prohibits planning research as if you will magically complete unrealist |
| 11 | 58 | the smallest sample size that gives adequate statistical power | Statistical power is the probability that your study will correctly detect a real effect if one exis |
| 12 | 63 | Two-sample t-test, two-tailed, α=0.05 | A t-test is a statistical method that compares the average outcome between two groups to see if they |
| 13 | 63 | Two-sample t-test, two-tailed, α=0.05 | This is your significance threshold—the probability of incorrectly declaring a difference exists whe |
| 14 | 64 | Cohen's d=0.5 (medium effect): power ≈ 0.62 | Cohen's d measures how large the difference between two conditions is in a standardized way. A d of  |
| 15 | 72 | a 38% chance of a false negative | A false negative means your study fails to detect a real difference that actually exists—you conclud |
| 16 | 79 | If the effect size is large (d≥0.8) | Effect size describes how much impact your intervention has. Larger effects are easier to detect wit |
| 17 | 80 | it addresses a structural failure mode, not a marginal one | A structural failure mode is a fundamental, widespread problem with how something works, rather than |
| 18 | 105 | Insight Atrophy (the gradual erosion of a person's ability to question AI output | This is already well-explained in the parenthetical definition—no flag needed. |
| 19 | 113 | Operationalize IAI as a composite of three observable turn-level signals | While 'operationalize' is a research term, it should be followed by: 'This means converting the abst |
| 20 | 114 | Operationalize IAI as a composite of three observable turn-level signals | Should clarify: 'A turn-level signal is a measurable behavior or outcome observed during a single ex |
| 21 | 115 | 1. Hypothesis generation rate — number of competing hypotheses surfaced per 10 t | The definition given ('number of competing hypotheses surfaced per 10 turns') is operational but doe |
| 22 | 116 | 2. Challenge rate — number of times human explicitly contests model output vs ac | The definition is clear enough, but 'interrogation' is slightly jargon-heavy. Consider: 'This measur |
| 23 | 117 | 3. Scope contraction — whether the human's question set narrows or expands acros | Unclear what 'scope' means here without further explanation. Should add: 'This tracks whether the ra |
| 24 | 121 | These three signals can be extracted from transcripts by a blinded rater using a | Should explain: 'A blinded rater is a person who scores the transcripts without knowing which experi |
| 25 | 122 | The IAI score is a weighted composite. | Should add: 'A weighted composite combines the three signals into a single score by giving each one  |
| 26 | 127 | H1 depends on intent-drift incident rate. The rubric needs to exist before pilot | The term 'intent-drift incident' is introduced but not defined upfront before being used in 'H1 depe |
| 27 | 128 | the model's output addresses a goal that deviates from the Task State field by ≥ | Should explain: 'The Task State field is a record of what the human is currently trying to accomplis |
| 28 | 128 | on a 5-point alignment scale, scored by blinded rater | Should clarify what the scale measures: 'This scale ranges from 1 (completely off-topic) to 5 (perfe |
| 29 | 138 | ContractWindow state snapshot at each turn (JSON export from contract_window.py  | While referenced as an existing method, 'ContractWindow' is not explained. Should add: 'ContractWind |
| 30 | 139 | BicameralReview pass/fail per turn (from bicameral_review.py) | Should explain: 'BicameralReview is a safety or quality-check system that evaluates whether each AI  |
| 31 | 144 | Build the recorder as a thin wrapper around existing ContractWindow and Bicamera | Should clarify: 'A thin wrapper is a lightweight layer of new code that collects output from existin |
| 32 | 153 | It wraps ContractWindow, calls BicameralReview, writes JSONL. | ContractWindow is a software component that manages a bounded interaction session—it controls what i |
| 33 | 153 | It wraps ContractWindow, calls BicameralReview, writes JSONL. | BicameralReview is a governance check that requires approval from two independent review processes b |
| 34 | 153 | It wraps ContractWindow, calls BicameralReview, writes JSONL. | JSONL is a file format where each line contains one complete JSON object; it makes it easy to stream |
| 35 | 172 | check_comprehension_grade(text) → Flesch-Kincaid (a readability score... | The Flesch-Kincaid Grade Level is a numerical readability metric that estimates the U.S. school grad |
| 36 | 175 | check_task_state_alignment(turn_text, task_state) → alignment score 1-5 | An alignment score of 1-5 is a numerical rating where higher numbers indicate that the model's respo |
| 37 | 178 | Required columns: session_id, condition, turn_count, token_count, drift_incident | Drift_incidents refers to moments in a conversation when the model's behavior or outputs noticeably  |
| 38 | 178 | Required columns: session_id, condition, turn_count, token_count, drift_incident | ia_score is a summary metric (likely standing for 'interaction alignment score') that measures how w |
| 39 | 194 | 2 sessions per condition for conditions 1-5. Skip condition 6 | The document refers to different experimental conditions (labeled 1 through 6) but never explains wh |
| 40 | 197 | Log cognitive load state before each session (high/medium/low) — this is both se | A covariate is a background factor that can influence your results and that you want to track separa |
| 41 | 202 | Score all sessions with IAI rubric and drift rubric within 24 hours | The document mentions two separate scoring tools (rubrics) but does not explain what each one measur |
| 42 | 222 | Calculate Cohen's kappa (a statistical measure of agreement... | Cohen's kappa is already explained in the parenthetical gloss provided in the document. No flag need |
| 43 | 229 | Use the 10 pilot sessions to estimate the correlation between each IAI component | IAI is introduced with three specific components listed, but 'IAI' itself is never defined. The read |
| 44 | 232 | Weight the composite based on predictive validity, not intuition. | Predictive validity is mentioned as the criterion for weighting but is never defined. You should exp |
| 45 | 236 | Session recorder produces complete, parseable JSONL for all 6 conditions | JSONL is mentioned as an output format but never explained. You should add: 'JSONL is a file format  |
| 46 | 237 | Invariant checkers produce numeric outputs without errors | Invariant checkers are mentioned without explanation of what they check for or why. You should expla |
| 47 | 261 | Run the full minimum viable sample. 180 sessions, 30 per condition. | This is the smallest number of research participants and observations needed to reliably answer your |
| 48 | 270 | 180 sessions / 22 working days = 8.2 sessions/day if you work every day. | A condition is one version of the experiment you're testing—for example, one group of participants m |
| 49 | 285 | Interleave conditions daily to avoid temporal confounds | Temporal confounds are factors that change over time and could unfairly affect your results—like you |
| 50 | 285 | avoid temporal confounds (your cognitive state, model API behavior changes) | This refers to the possibility that the AI system you're testing may perform differently at differen |
| 51 | 295 | Maintain /data/session-log.csv updated after every session | A unique identifier assigned to each individual conversation or interaction recorded in the study, u |
| 52 | 295 | session_id, condition, date, duration_minutes, turn_count, token_count | The experimental treatment or version the participant was assigned to (for example, if testing diffe |
| 53 | 295 | session_id, condition, date, duration_minutes, turn_count, token_count | The number of back-and-forth exchanges between the participant and the system—each time the particip |
| 54 | 295 | session_id, condition, date, duration_minutes, turn_count, token_count | The total number of language units (roughly words or small word-pieces) processed by the AI system d |
| 55 | 295 | turn_count, token_count, completion_status (COMPLETE/ABANDONED/PARTIAL), cogniti | A measurement of how mentally taxed or tired the participant reported feeling before the session beg |
| 56 | 299 | COMPLETE = ≥30 turns or ≥50K tokens, recorder functioned, no instrument failures | Sessions qualify as COMPLETE if they meet at least one of two thresholds: either the participant com |
| 57 | 302 | May be usable as a sensitivity check but not primary analysis | A follow-up analysis that re-runs the main findings using slightly different data (in this case, PAR |
| 58 | 329 | run 5-10 test prompts through a frontier model about Black consumer behavior | A frontier model is one of the most advanced AI systems currently available—essentially the state-of |
| 59 | 330 | score the outputs against the Eight Wonders rubric | The Eight Wonders rubric is the evaluation framework being used in this project to assess and catego |
| 60 | 330 | This is the "fluent wrong answer" documentation the paper needs. | A fluent wrong answer is when an AI system generates output that sounds confident and well-reasoned  |
| 61 | 360 | Run data_pipeline.py on all sessions | This is a computer script that processes raw video or audio recordings to extract the information ne |
| 62 | 368 | Score all sessions with drift rubric (if not scored during collection) | A drift rubric is a checklist or scoring guide that measures how much a conversation, performance, o |
| 63 | 369 | Score all sessions with IAI rubric | The IAI rubric is the specific scoring guide you are using to measure whatever concept IAI represent |
| 64 | 370 | Confirm scorer does not know condition assignments during scoring (blind scoring | Blind scoring means the person rating the recordings does not know which group (control, treatment A |
| 65 | 372 | DV: intent-drift incident rate (incidents per 10 turns) | This is a measurement of how often the AI system's responses start moving away from the user's origi |
| 66 | 375 | Effect size: Cohen's d | Cohen's d is a number that describes how big the practical difference is between two groups — a way  |
| 67 | 376 | Claim threshold: ≥25% reduction, statistically significant at α=0.05 | This is the threshold for statistical significance; it means we will only accept a result as reliabl |
| 68 | 384 | DV: drift repair rate (proportion of drift incidents resolved within 3 turns) | This measures how successful the system is at fixing cases where the conversation has drifted off-to |
| 69 | 390 | DV: lay reader comprehension accuracy (% correct on session-state questions) | This is a test of how well ordinary people (not AI experts) can understand what the AI system is doi |
| 70 | 391 | DV: lay reader comprehension accuracy (% correct on session-state questions) | These are questions that ask a reader about the current state of the conversation — for example, wha |
| 71 | 392 | Material: CW render() output from session_recorder, formatted per protocol | This refers to the formatted, readable version of the system's output that is displayed to users or  |
| 72 | 394 | Test: one-sample proportion test against 80% null | This is a statistical test that checks whether a measured percentage (like comprehension accuracy) i |
| 73 | 409 | exclusions, power analysis for actual n | A statistical calculation that determines whether your sample size was large enough to reliably dete |
| 74 | 411 | H1 results: effect size, CI, p-value, whether ≥25% threshold met | A number that measures how big the difference or relationship actually is between your conditions—no |
| 75 | 411 | H1 results: effect size, CI, p-value, whether ≥25% threshold met | A range of numbers (confidence interval) that tells you where the true result probably lies—for exam |
| 76 | 411 | H1 results: effect size, CI, p-value, whether ≥25% threshold met | A number indicating how likely your result would occur by pure chance if there were actually no real |
| 77 | 413 | H2 results: repair rate comparison, odds ratio, whether ≥2x threshold met | A number comparing how much more (or less) likely one outcome is versus another between two groups—f |
| 78 | 415 | H3 results: comprehension accuracy, CI, whether ≥80% threshold met | The percentage or proportion of questions or tasks that participants answered or completed correctly |
| 79 | 416 | Secondary analysis: IAI scores across conditions, correlation with drift inciden | Numerical measurements on the IAI scale; without knowing what IAI stands for earlier in the document |
| 80 | 416 | Secondary analysis: IAI scores across conditions, correlation with drift inciden | The frequency or proportion of times a particular type of failure or problem (drift incidents) occur |
| 81 | 419 | grouped bar chart, drift incident rate by condition with 95% CIs | Confidence intervals set at the 95% level, meaning there is a 95% probability that the true value fa |
| 82 | 424 | Formalize this as an appendix or supplementary analysis for the CW paper | CW is an abbreviation; clarify what 'CW' stands for and what this paper is about (e.g., 'the Crowdwo |
| 83 | 430 | H1/H2/H3 each evaluated with a clear TRUE/FALSE/INCONCLUSIVE designation | These appear to be hypothesis labels but the document never defines what H1, H2, and H3 are testing  |
| 84 | 459 | State the problem (Insight Atrophy, fluent wrong answers) | Insight Atrophy is the phenomenon where an AI system produces answers that sound confident and fluen |
| 85 | 460 | State the contribution (Contract Window + 6 invariants) | The Contract Window is a method or framework for controlling when and how an AI system provides resp |
| 86 | 462 | State the empirical claim (H1/H2/H3, now with actual results) | H1, H2, and H3 are three specific hypotheses (testable predictions) that the experiment is designed  |
| 87 | 475 | Methods section: session protocol, condition specifications, instruments, blindi | A blinding procedure is a method where participants or researchers are kept unaware of which experim |
| 88 | 474 | What the IAI score distribution tells you | IAI (Interpretability Alignment Index) is a numerical measurement of how well the model's outputs al |
| 89 | 480 | Single investigator as both experimenter and rater (partial blindness) | This means you knew which condition each participant was in while rating their responses, so your ra |
| 90 | 481 | MVS (Minimum Viable Sample — the smallest sample size that gives adequate statis | The parenthetical is present but incomplete for a lay reader; consider adding: 'At d=0.5 with n=30,  |
| 91 | 482 | Observational foundation of the invariant set | This limitation means your identification of which outputs count as reliable or stable (the 'invaria |
| 92 | 483 | Lay reader sample not probability-sampled | Your lay readers were chosen by convenience (e.g., volunteers you recruited) rather than by random s |
| 93 | 503 | Run the paper through the Bicameral Review (two independent review channels... | A quality control process where two separate reviewers—one checking whether the work answers the res |
| 94 | 503 | ...does this introduce a phantom claim? | A claim presented as fact or supported by evidence when it is actually unsupported, unverified, or b |
| 95 | 539 | Final V&T (Verification and Truth — a statement that explicitly... | This means you must explicitly state which claims in your paper are based on solid evidence (verifie |
| 96 | 540 | Every empirical claim must be tagged with its evidence basis. | An empirical claim is any statement about how the world actually works, based on observation or expe |
| 97 | 531 | Submitting to a deadline you cannot meet is phantom work (I2). | Phantom work means investing effort on a task that cannot possibly succeed — in this case, submittin |
| 98 | 579 | Instrument fails kappa gate in May | A kappa gate is a validation checkpoint that checks whether your measurement instrument (the tool yo |
| 99 | 583 | Data collection falls short of n=30/condition | This refers to collecting data from 30 participants in each separate group or condition of your stud |
| 100 | 585 | Lay reader recruitment fails for H3 | H3 is shorthand for your third hypothesis—a specific prediction you're testing in the study. Lay rea |
| 101 | 587 | Analysis reveals instrument invalidity | Instrument invalidity means your measurement tool is not actually measuring what you intended it to  |
| 102 | 589 | Pilot validation gate in May is the firewall | A pilot validation gate is a checkpoint where you test your instrument on a small sample before your |
| 103 | 649 | These are not preferences. They are constraints derived from I1-I6 and | I1-I6 refers to six foundational principles or investigator commitments that form the basis for thes |
| 104 | 656 | Do not run data collection sessions when cognitive load is HIGH. | This refers to a specific, measurable threshold of mental fatigue or distraction that has been defin |
| 105 | 660 | Do not work on Frontin or Graves during active data collection weeks | This phrase implies there is a defined schedule distinguishing 'active data collection weeks' from o |
| 106 | 660 | unless you are in a burst that does not touch the primary pipeline | A 'burst' and 'primary pipeline' are terms that describe a specific workflow or scheduling pattern u |
| 107 | 663 | Do not work on Frontin or Graves during active data collection weeks | Frontin and Graves are referenced as separate work streams or projects; the reader should understand |
| 108 | 664 | replaced with MVS (Minimum Viable Sample — the smallest sample size that gives a | While a definition is provided in parentheses, 'adequate statistical power' and 'meaningful differen |

#### Full BMT-2 Explanations Inserted

**1. Line 6 — Empirical Validation of the Contract Window (a structured re**

Inserted: A Contract Window is a shared document or data structure that tracks what a person and an AI system agree they're working on together, what has been confirmed as correct or completed, and who is assigned to fix any problems that arise. It creates accountability and clarity in human-AI collaboration.

**2. Line 6 — Cognitive Governance Lab**

Inserted: Cognitive Governance refers to systematic methods for overseeing and managing how AI systems make decisions and interact with humans. It establishes rules, verification processes, and accountability structures to ensure AI systems operate reliably and transparently.

**3. Line 15 — Evidence Basis: CONSTRUCTED — this plan is forward-looking.**

Inserted: This plan describes research that has not yet been conducted; it is a roadmap of intended work rather than a report of completed experiments or findings. No actual results or data are being presented.

**4. Line 14 — ...on the Contract Window architecture for human-AI collabor**

Inserted: This is a system design where humans and AI agree on explicit rules or 'contracts' at the start of their work together, and both parties check their behavior against those rules as they collaborate.

**5. Line 18 — INVARIANT STATUS (whether the hard behavioral rules the AI c**

Inserted: This is a snapshot of which core promises or commitments the AI made at the beginning are still being kept; if an invariant is 'broken,' it means the AI violated one of its own rules.

**6. Line 19 — ...I2 active — no phantom work, deadlines are targets not ac**

Inserted: This means the AI will not pretend to have completed research tasks or make claims about findings that were never actually performed; instead, all deadlines are goals to aim for, not declarations that work is already done.

**7. Line 21 — REPAIR OBLIGATIONS: None at plan initialization. Violations **

Inserted: These are debts or commitments the AI owes to fix past mistakes; logging violations means recording each time a rule was broken so it can be reviewed later.

**8. Line 23 — CONSTRUCTED: Hypotheses H1, H2, H3 — derived from longitudin**

Inserted: This label means the hypotheses were built from watching trends over time in the real world, not from running a controlled experiment, so they are less certain than experimentally tested claims.

**9. Line 26 — ...Whether n=30/condition (MVS) will replicate at n=60/condi**

Inserted: This refers to a test run with 30 participants in each group (n=30/condition) using a specific method called MVS; the question is whether the same results will hold when the test is repeated with twice as many participants (n=60).

**10. Line 52 — This is flagged per I2 — No Phantom Work. Do not plan 360 se**

Inserted: I2 is a governance rule that prohibits planning research as if you will magically complete unrealistic workloads; you must either reduce your study scope or extend your timeline to match actual human capacity.

**11. Line 58 — the smallest sample size that gives adequate statistical pow**

Inserted: Statistical power is the probability that your study will correctly detect a real effect if one exists. Higher power means you're less likely to miss a true difference between your conditions.

**12. Line 63 — Two-sample t-test, two-tailed, α=0.05**

Inserted: A t-test is a statistical method that compares the average outcome between two groups to see if they differ significantly. 'Two-tailed' means you're testing whether one condition is either better or worse than the other, not just one direction.

**13. Line 63 — Two-sample t-test, two-tailed, α=0.05**

Inserted: This is your significance threshold—the probability of incorrectly declaring a difference exists when it doesn't. At 0.05, you accept a 5% risk of a false alarm.

**14. Line 64 — Cohen's d=0.5 (medium effect): power ≈ 0.62**

Inserted: Cohen's d measures how large the difference between two conditions is in a standardized way. A d of 0.5 is considered a medium-sized difference, and 0.8 is large; bigger effect sizes are easier to detect.

**15. Line 72 — a 38% chance of a false negative**

Inserted: A false negative means your study fails to detect a real difference that actually exists—you conclude there's no effect when there genuinely is one.

**16. Line 79 — If the effect size is large (d≥0.8)**

Inserted: Effect size describes how much impact your intervention has. Larger effects are easier to detect with smaller sample sizes, while tiny effects require more data to spot reliably.

**17. Line 80 — it addresses a structural failure mode, not a marginal one**

Inserted: A structural failure mode is a fundamental, widespread problem with how something works, rather than a minor edge case or small inefficiency.

**18. Line 105 — Insight Atrophy (the gradual erosion of a person's ability t**

Inserted: This is already well-explained in the parenthetical definition—no flag needed.

**19. Line 113 — Operationalize IAI as a composite of three observable turn-l**

Inserted: While 'operationalize' is a research term, it should be followed by: 'This means converting the abstract concept into measurable, observable behaviors that can be consistently tracked and scored.'

**20. Line 114 — Operationalize IAI as a composite of three observable turn-l**

Inserted: Should clarify: 'A turn-level signal is a measurable behavior or outcome observed during a single exchange between the human and the AI model.'

**21. Line 115 — 1. Hypothesis generation rate — number of competing hypothes**

Inserted: The definition given ('number of competing hypotheses surfaced per 10 turns') is operational but doesn't explain why this matters or what 'competing hypotheses' means in plain terms. Suggest: 'This counts how often the human proposes alternative explanations or questions whether the AI's answer is the only possibility.'

**22. Line 116 — 2. Challenge rate — number of times human explicitly contest**

Inserted: The definition is clear enough, but 'interrogation' is slightly jargon-heavy. Consider: 'This measures how often the human pushes back on or questions the AI's answer, versus simply accepting it and moving on.'

**23. Line 117 — 3. Scope contraction — whether the human's question set narr**

Inserted: Unclear what 'scope' means here without further explanation. Should add: 'This tracks whether the range of topics and types of questions the human asks gets narrower or wider as the session progresses—narrowing could indicate reduced curiosity or engagement.'

**24. Line 121 — These three signals can be extracted from transcripts by a b**

Inserted: Should explain: 'A blinded rater is a person who scores the transcripts without knowing which experimental condition (1-6) the session belonged to, to avoid unconscious bias.'

**25. Line 122 — The IAI score is a weighted composite.**

Inserted: Should add: 'A weighted composite combines the three signals into a single score by giving each one a different importance or 'weight' based on how much each contributes to the final IAI measurement.'

**26. Line 127 — H1 depends on intent-drift incident rate. The rubric needs t**

Inserted: The term 'intent-drift incident' is introduced but not defined upfront before being used in 'H1 depends on intent-drift incident rate.' Should clarify before that line: 'An intent-drift incident occurs when the AI model shifts focus away from what the human actually wanted to explore.'

**27. Line 128 — the model's output addresses a goal that deviates from the T**

Inserted: Should explain: 'The Task State field is a record of what the human is currently trying to accomplish, allowing us to detect when the AI's output goes off-track from that goal.'

**28. Line 128 — on a 5-point alignment scale, scored by blinded rater**

Inserted: Should clarify what the scale measures: 'This scale ranges from 1 (completely off-topic) to 5 (perfectly on-topic), measuring how closely the AI's response stays focused on what the human was actually asking.'

**29. Line 138 — ContractWindow state snapshot at each turn (JSON export from**

Inserted: While referenced as an existing method, 'ContractWindow' is not explained. Should add: 'ContractWindow is a system component that tracks constraints or boundaries applied to the AI model during each turn.'

**30. Line 139 — BicameralReview pass/fail per turn (from bicameral_review.py**

Inserted: Should explain: 'BicameralReview is a safety or quality-check system that evaluates whether each AI model output meets certain standards, flagging it as a pass or fail.'

**31. Line 144 — Build the recorder as a thin wrapper around existing Contrac**

Inserted: Should clarify: 'A thin wrapper is a lightweight layer of new code that collects output from existing systems without duplicating or rewriting their core logic.'

**32. Line 153 — It wraps ContractWindow, calls BicameralReview, writes JSONL**

Inserted: ContractWindow is a software component that manages a bounded interaction session—it controls what inputs are allowed and what outputs can occur during a single conversation turn.

**33. Line 153 — It wraps ContractWindow, calls BicameralReview, writes JSONL**

Inserted: BicameralReview is a governance check that requires approval from two independent review processes before certain actions proceed, similar to how a legislature requires two chambers to pass a law.

**34. Line 153 — It wraps ContractWindow, calls BicameralReview, writes JSONL**

Inserted: JSONL is a file format where each line contains one complete JSON object; it makes it easy to stream and append data without rewriting the entire file.

**35. Line 172 — check_comprehension_grade(text) → Flesch-Kincaid (a readabil**

Inserted: The Flesch-Kincaid Grade Level is a numerical readability metric that estimates the U.S. school grade level needed to understand a piece of text; a score of 8 means an average 8th-grader should be able to comprehend it.

**36. Line 175 — check_task_state_alignment(turn_text, task_state) → alignmen**

Inserted: An alignment score of 1-5 is a numerical rating where higher numbers indicate that the model's response better matches the current state and requirements of the task.

**37. Line 178 — Required columns: session_id, condition, turn_count, token_c**

Inserted: Drift_incidents refers to moments in a conversation when the model's behavior or outputs noticeably shift away from its intended guidelines or task focus.

**38. Line 178 — Required columns: session_id, condition, turn_count, token_c**

Inserted: ia_score is a summary metric (likely standing for 'interaction alignment score') that measures how well the model stayed on task and within its governance boundaries across an entire session.

**39. Line 194 — 2 sessions per condition for conditions 1-5. Skip condition **

Inserted: The document refers to different experimental conditions (labeled 1 through 6) but never explains what distinguishes them or what they test. You need to know: what variable or intervention is being manipulated across these conditions, and why condition 6 is called 'combined' and is more complex to score.

**40. Line 197 — Log cognitive load state before each session (high/medium/lo**

Inserted: A covariate is a background factor that can influence your results and that you want to track separately, so you can account for it later when analyzing whether the main thing you're testing actually made a difference. Here, logging your own cognitive load lets you check whether your fatigue (rather than the condition itself) affected your scoring.

**41. Line 202 — Score all sessions with IAI rubric and drift rubric within 2**

Inserted: The document mentions two separate scoring tools (rubrics) but does not explain what each one measures or why both are needed. You need to know what 'IAI' stands for, what it evaluates, and what 'drift' means in this context.

**42. Line 222 — Calculate Cohen's kappa (a statistical measure of agreement.**

Inserted: Cohen's kappa is already explained in the parenthetical gloss provided in the document. No flag needed.

**43. Line 229 — Use the 10 pilot sessions to estimate the correlation betwee**

Inserted: IAI is introduced with three specific components listed, but 'IAI' itself is never defined. The reader does not know what IAI stands for or why these three specific measurements represent it. You should explain: 'IAI is a composite scoring system that measures three dimensions of how an AI system approaches problems: how often it generates new explanations, how often it questions its own reasoning, and how much it narrows the scope of what it's examining.'

**44. Line 232 — Weight the composite based on predictive validity, not intui**

Inserted: Predictive validity is mentioned as the criterion for weighting but is never defined. You should explain: 'Predictive validity means how well each component actually predicts whether drift incidents will occur in practice, based on the pilot data.'

**45. Line 236 — Session recorder produces complete, parseable JSONL for all **

Inserted: JSONL is mentioned as an output format but never explained. You should add: 'JSONL is a file format where each line contains one complete data record in JSON (a machine-readable structured format), making it easy for automated systems to read and process.'

**46. Line 237 — Invariant checkers produce numeric outputs without errors**

Inserted: Invariant checkers are mentioned without explanation of what they check for or why. You should explain: 'Invariant checkers are automated tools that verify that certain conditions remain true throughout the data collection—for example, ensuring that session IDs are consistent or that numerical scores stay within valid ranges.'

**47. Line 261 — Run the full minimum viable sample. 180 sessions, 30 per con**

Inserted: This is the smallest number of research participants and observations needed to reliably answer your core research question. In this case, you need 180 total sessions divided equally across 6 different experimental conditions (30 each) to have confidence in your results.

**48. Line 270 — 180 sessions / 22 working days = 8.2 sessions/day if you wor**

Inserted: A condition is one version of the experiment you're testing—for example, one group of participants might use the AI system with feature A on, while another group uses it with feature A off. You need enough sessions in each condition to see if the differences between them are real or just random variation.

**49. Line 285 — Interleave conditions daily to avoid temporal confounds**

Inserted: Temporal confounds are factors that change over time and could unfairly affect your results—like your mental sharpness declining as the day goes on, or the API becoming slower. By mixing up the order of conditions instead of doing them one-by-one, you ensure that time-based changes don't systematically favor one condition over another.

**50. Line 285 — avoid temporal confounds (your cognitive state, model API be**

Inserted: This refers to the possibility that the AI system you're testing may perform differently at different times—for example, it might be slower during peak hours or produce slightly different outputs as its underlying software is updated. This variability could skew your results if you always test one condition at the same time of day.

**51. Line 295 — Maintain /data/session-log.csv updated after every session**

Inserted: A unique identifier assigned to each individual conversation or interaction recorded in the study, used to link all data (audio, turns, tokens) belonging to that single participant session.

**52. Line 295 — session_id, condition, date, duration_minutes, turn_count, t**

Inserted: The experimental treatment or version the participant was assigned to (for example, if testing different AI systems or interfaces, this identifies which variant they used).

**53. Line 295 — session_id, condition, date, duration_minutes, turn_count, t**

Inserted: The number of back-and-forth exchanges between the participant and the system—each time the participant sends a message and receives a response counts as one turn.

**54. Line 295 — session_id, condition, date, duration_minutes, turn_count, t**

Inserted: The total number of language units (roughly words or small word-pieces) processed by the AI system during the session; this measures computational complexity and cost.

**55. Line 295 — turn_count, token_count, completion_status (COMPLETE/ABANDON**

Inserted: A measurement of how mentally taxed or tired the participant reported feeling before the session began, used to control for whether fatigue influenced their performance.

**56. Line 299 — COMPLETE = ≥30 turns or ≥50K tokens, recorder functioned, no**

Inserted: Sessions qualify as COMPLETE if they meet at least one of two thresholds: either the participant completed at least 30 exchanges with the system, or the system processed at least 50,000 tokens; this ensures sufficient data was collected for analysis.

**57. Line 302 — May be usable as a sensitivity check but not primary analysi**

Inserted: A follow-up analysis that re-runs the main findings using slightly different data (in this case, PARTIAL sessions) to verify the results are robust and not dependent on exactly which sessions you include.

**58. Line 329 — run 5-10 test prompts through a frontier model about Black c**

Inserted: A frontier model is one of the most advanced AI systems currently available—essentially the state-of-the-art language model that represents the cutting edge of what's possible today. Testing against the newest model helps determine whether problems are inherent to all AI systems or specific to older versions.

**59. Line 330 — score the outputs against the Eight Wonders rubric**

Inserted: The Eight Wonders rubric is the evaluation framework being used in this project to assess and categorize the types of errors or biases that appear in the model's outputs. You should clarify what the rubric measures (e.g., does it score factual accuracy, bias categories, reasoning quality, or something else).

**60. Line 330 — This is the "fluent wrong answer" documentation the paper ne**

Inserted: A fluent wrong answer is when an AI system generates output that sounds confident and well-reasoned but is actually incorrect or misleading. This is particularly dangerous because it convinces readers without signaling uncertainty.

**61. Line 360 — Run data_pipeline.py on all sessions**

Inserted: This is a computer script that processes raw video or audio recordings to extract the information needed for analysis. It likely removes duplicates, fills in missing pieces, and organizes everything into a standard format for the next step.

**62. Line 368 — Score all sessions with drift rubric (if not scored during c**

Inserted: A drift rubric is a checklist or scoring guide that measures how much a conversation, performance, or behavior moved away from its original direction or intent. In this study, it likely assesses whether participants' responses stayed consistent or drifted to different topics.

**63. Line 369 — Score all sessions with IAI rubric**

Inserted: The IAI rubric is the specific scoring guide you are using to measure whatever concept IAI represents; without knowing what IAI stands for in your study, readers cannot understand what dimension of the data is being measured or why it matters.

**64. Line 370 — Confirm scorer does not know condition assignments during sc**

Inserted: Blind scoring means the person rating the recordings does not know which group (control, treatment A, treatment B, etc.) each session belongs to, so their judgments cannot be unconsciously biased by knowing what result is expected.

**65. Line 372 — DV: intent-drift incident rate (incidents per 10 turns)**

Inserted: This is a measurement of how often the AI system's responses start moving away from the user's original intent or goals during a conversation, counted as the number of such incidents that occur for every 10 user messages.

**66. Line 375 — Effect size: Cohen's d**

Inserted: Cohen's d is a number that describes how big the practical difference is between two groups — a way to measure whether a statistically significant result is actually meaningful in the real world.

**67. Line 376 — Claim threshold: ≥25% reduction, statistically significant a**

Inserted: This is the threshold for statistical significance; it means we will only accept a result as reliable if there is less than a 5% chance it happened by random luck.

**68. Line 384 — DV: drift repair rate (proportion of drift incidents resolve**

Inserted: This measures how successful the system is at fixing cases where the conversation has drifted off-topic, specifically counting what fraction of drift incidents are corrected within the next 3 user messages.

**69. Line 390 — DV: lay reader comprehension accuracy (% correct on session-**

Inserted: This is a test of how well ordinary people (not AI experts) can understand what the AI system is doing, measured by asking them questions about the conversation state and checking what percentage they answer correctly.

**70. Line 391 — DV: lay reader comprehension accuracy (% correct on session-**

Inserted: These are questions that ask a reader about the current state of the conversation — for example, what the user's goal was, or what the system was trying to do — to measure whether the system's behavior is transparent or confusing.

**71. Line 392 — Material: CW render() output from session_recorder, formatte**

Inserted: This refers to the formatted, readable version of the system's output that is displayed to users or readers — the end product that shows what the system actually communicated.

**72. Line 394 — Test: one-sample proportion test against 80% null**

Inserted: This is a statistical test that checks whether a measured percentage (like comprehension accuracy) is meaningfully different from a target percentage (in this case, 80%).

**73. Line 409 — exclusions, power analysis for actual n**

Inserted: A statistical calculation that determines whether your sample size was large enough to reliably detect the effect you're studying; it shows you didn't just get lucky with your results.

**74. Line 411 — H1 results: effect size, CI, p-value, whether ≥25% threshold**

Inserted: A number that measures how big the difference or relationship actually is between your conditions—not just whether it's real, but how substantial it is.

**75. Line 411 — H1 results: effect size, CI, p-value, whether ≥25% threshold**

Inserted: A range of numbers (confidence interval) that tells you where the true result probably lies—for example, if your effect size is 0.5 with a CI of 0.3 to 0.7, the real value is likely somewhere in that band.

**76. Line 411 — H1 results: effect size, CI, p-value, whether ≥25% threshold**

Inserted: A number indicating how likely your result would occur by pure chance if there were actually no real effect; smaller p-values mean your finding is less likely to be a fluke.

**77. Line 413 — H2 results: repair rate comparison, odds ratio, whether ≥2x **

Inserted: A number comparing how much more (or less) likely one outcome is versus another between two groups—for example, an odds ratio of 2 means one group is twice as likely to have the outcome.

**78. Line 415 — H3 results: comprehension accuracy, CI, whether ≥80% thresho**

Inserted: The percentage or proportion of questions or tasks that participants answered or completed correctly.

**79. Line 416 — Secondary analysis: IAI scores across conditions, correlatio**

Inserted: Numerical measurements on the IAI scale; without knowing what IAI stands for earlier in the document, a reader cannot understand what is being measured.

**80. Line 416 — Secondary analysis: IAI scores across conditions, correlatio**

Inserted: The frequency or proportion of times a particular type of failure or problem (drift incidents) occurred; this matters because you're checking whether it correlates with the IAI scores.

**81. Line 419 — grouped bar chart, drift incident rate by condition with 95%**

Inserted: Confidence intervals set at the 95% level, meaning there is a 95% probability that the true value falls within the range shown by the error bars on the chart.

**82. Line 424 — Formalize this as an appendix or supplementary analysis for **

Inserted: CW is an abbreviation; clarify what 'CW' stands for and what this paper is about (e.g., 'the Crowdworker Validation study' or 'the Content Moderation Warnings research').

**83. Line 430 — H1/H2/H3 each evaluated with a clear TRUE/FALSE/INCONCLUSIVE**

Inserted: These appear to be hypothesis labels but the document never defines what H1, H2, and H3 are testing or why these three hypotheses matter to the research.

**84. Line 459 — State the problem (Insight Atrophy, fluent wrong answers)**

Inserted: Insight Atrophy is the phenomenon where an AI system produces answers that sound confident and fluent but are actually incorrect or misleading, causing users to lose the ability to recognize flaws in AI reasoning. This matters because users may trust AI outputs without proper verification, leading to bad decisions.

**85. Line 460 — State the contribution (Contract Window + 6 invariants)**

Inserted: The Contract Window is a method or framework for controlling when and how an AI system provides responses, and the 6 invariants are specific rules or properties that must always hold true to ensure the system behaves reliably. Together they represent the proposed solution to the Insight Atrophy problem.

**86. Line 462 — State the empirical claim (H1/H2/H3, now with actual results**

Inserted: H1, H2, and H3 are three specific hypotheses (testable predictions) that the experiment is designed to evaluate. These are the measurable claims about how the Contract Window and invariants actually perform in practice.

**87. Line 475 — Methods section: session protocol, condition specifications,**

Inserted: A blinding procedure is a method where participants or researchers are kept unaware of which experimental condition (treatment or control) is being used, to prevent bias from influencing results. This ensures that expectations about the intervention do not unconsciously affect how people rate or respond to the system.

**88. Line 474 — What the IAI score distribution tells you**

Inserted: IAI (Interpretability Alignment Index) is a numerical measurement of how well the model's outputs align with human expectations; the distribution refers to how these scores spread across your sample—whether most scores cluster in one range or vary widely.

**89. Line 480 — Single investigator as both experimenter and rater (partial **

Inserted: This means you knew which condition each participant was in while rating their responses, so your ratings could have been unconsciously influenced by knowing the hypothesis or treatment group.

**90. Line 481 — MVS (Minimum Viable Sample — the smallest sample size that g**

Inserted: The parenthetical is present but incomplete for a lay reader; consider adding: 'At d=0.5 with n=30, your study would have roughly a 47% chance of detecting a real effect if one exists—well below the standard 80% threshold, so if you find nothing, that may reflect your small sample rather than a true absence of effect.'

**91. Line 482 — Observational foundation of the invariant set**

Inserted: This limitation means your identification of which outputs count as reliable or stable (the 'invariant set') came from watching what happened in your data rather than from a pre-registered prediction, so you may have unconsciously included or excluded cases that fit your hypothesis.

**92. Line 483 — Lay reader sample not probability-sampled**

Inserted: Your lay readers were chosen by convenience (e.g., volunteers you recruited) rather than by random selection from the full population of possible lay readers, so they may differ systematically from the broader public in ways that affect your findings.

**93. Line 503 — Run the paper through the Bicameral Review (two independent **

Inserted: A quality control process where two separate reviewers—one checking whether the work answers the research question, and one checking for unfounded claims—must both approve the output before it is shared. Neither reviewer can override the other's decision.

**94. Line 503 — ...does this introduce a phantom claim?**

Inserted: A claim presented as fact or supported by evidence when it is actually unsupported, unverified, or based on a misinterpretation of the data. Phantom claims mislead readers into accepting conclusions that the evidence does not justify.

**95. Line 539 — Final V&T (Verification and Truth — a statement that explici**

Inserted: This means you must explicitly state which claims in your paper are based on solid evidence (verified) and which are new ideas you're proposing (truth-claims). Every factual statement should be marked with where it comes from — your own experiments, published research, or your new argument.

**96. Line 540 — Every empirical claim must be tagged with its evidence basis**

Inserted: An empirical claim is any statement about how the world actually works, based on observation or experiment — as opposed to pure logic or opinion. For example, 'our model achieved 87% accuracy' is empirical; 'we should prioritize safety' is not.

**97. Line 531 — Submitting to a deadline you cannot meet is phantom work (I2**

Inserted: Phantom work means investing effort on a task that cannot possibly succeed — in this case, submitting to a conference deadline that has already passed. The reference 'I2' appears to be an internal indexing system; the core point is that you should avoid wasting time on impossible goals.

**98. Line 579 — Instrument fails kappa gate in May**

Inserted: A kappa gate is a validation checkpoint that checks whether your measurement instrument (the tool you're using to collect data) is producing consistent and reliable results. If it fails, it means the instrument isn't working well enough to trust for your actual study.

**99. Line 583 — Data collection falls short of n=30/condition**

Inserted: This refers to collecting data from 30 participants in each separate group or condition of your study. If you fall short, you have fewer data points to analyze, which weakens your statistical conclusions.

**100. Line 585 — Lay reader recruitment fails for H3**

Inserted: H3 is shorthand for your third hypothesis—a specific prediction you're testing in the study. Lay readers are people without expert training who will help validate whether your findings make sense to non-specialists.

**101. Line 587 — Analysis reveals instrument invalidity**

Inserted: Instrument invalidity means your measurement tool is not actually measuring what you intended it to measure, which would make all your results unreliable and unusable.

**102. Line 589 — Pilot validation gate in May is the firewall**

Inserted: A pilot validation gate is a checkpoint where you test your instrument on a small sample before your main study to catch problems early. This acts as a firewall by preventing you from proceeding to the expensive main study if the instrument isn't working.

**103. Line 649 — These are not preferences. They are constraints derived from**

Inserted: I1-I6 refers to six foundational principles or investigator commitments that form the basis for these constraints; the reader needs to know what these six items are or where to find them to understand why these rules exist.

**104. Line 656 — Do not run data collection sessions when cognitive load is H**

Inserted: This refers to a specific, measurable threshold of mental fatigue or distraction that has been defined elsewhere in the project; without knowing the operational definition or measurement, it is unclear when this rule applies.

**105. Line 660 — Do not work on Frontin or Graves during active data collecti**

Inserted: This phrase implies there is a defined schedule distinguishing 'active data collection weeks' from other periods; the reader should know how this calendar or status is determined.

**106. Line 660 — unless you are in a burst that does not touch the primary pi**

Inserted: A 'burst' and 'primary pipeline' are terms that describe a specific workflow or scheduling pattern used in this project; their meaning should be clarified so the exception is actionable.

**107. Line 663 — Do not work on Frontin or Graves during active data collecti**

Inserted: Frontin and Graves are referenced as separate work streams or projects; the reader should understand what these are and why they compete for attention with data collection.

**108. Line 664 — replaced with MVS (Minimum Viable Sample — the smallest samp**

Inserted: While a definition is provided in parentheses, 'adequate statistical power' and 'meaningful difference' are themselves technical terms that a non-specialist may not understand; the plain-language version should explain that this is the smallest group size needed to reliably detect a real effect in the data.

---

## Original Violation Details

### Violation 1 — BMT-1

**Line 36:** `UNKNOWN: Whether n=30/condition (MVS) will replicate at n=60/condition.`

**Fix:** Define "MVS" on first use: MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful difference)

### Violation 2 — BMT-1

**Line 56:** `### Minimum Viable Sample (MVS)`

**Fix:** Define "MVS" on first use: MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful difference)

### Violation 3 — BMT-1

**Line 336:** `Note the next analytical step but do not execute it in June. The CRISP-DM (Cross-Industry Standard P`

**Fix:** Define "CRISP-DM" on first use: CRISP-DM (Cross-Industry Standard Process for Data Mining — a standard workflow for data analysis projects, from business understanding through deployment)

### Violation 4 — BMT-1

**Line 463:** `- Related work: minimum viable — Constitutional AI (a training method where an AI evaluates its own `

**Fix:** Define "scalable oversight" on first use: scalable oversight (a research area focused on how humans can supervise AI systems even when those systems become more capable than the humans overseeing them)

### Violation 5 — BMT-1

**Line 544:** `Final V&T (Verification and Truth — a statement that explicitly separates what is confirmed from wha`

**Fix:** Define "V&T" on first use: V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work)

### Violation 6 — BMT-2

**Line 6:** `Empirical Validation of the Contract Window (a structured record...`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** A Contract Window is a shared document or data structure that tracks what a person and an AI system agree they're working on together, what has been confirmed as correct or completed, and who is assigned to fix any problems that arise. It creates accountability and clarity in human-AI collaboration.

### Violation 7 — BMT-2

**Line 6:** `Cognitive Governance Lab`

**Fix:** Add plain-language explanation after "Cognitive Governance"

**Explanation inserted:** Cognitive Governance refers to systematic methods for overseeing and managing how AI systems make decisions and interact with humans. It establishes rules, verification processes, and accountability structures to ensure AI systems operate reliably and transparently.

### Violation 8 — BMT-2

**Line 15:** `Evidence Basis: CONSTRUCTED — this plan is forward-looking.`

**Fix:** Add plain-language explanation after "CONSTRUCTED — this plan is forward-looking"

**Explanation inserted:** This plan describes research that has not yet been conducted; it is a roadmap of intended work rather than a report of completed experiments or findings. No actual results or data are being presented.

### Violation 9 — BMT-2

**Line 14:** `...on the Contract Window architecture for human-AI collaborative...`

**Fix:** Add plain-language explanation after "Contract Window architecture"

**Explanation inserted:** This is a system design where humans and AI agree on explicit rules or 'contracts' at the start of their work together, and both parties check their behavior against those rules as they collaborate.

### Violation 10 — BMT-2

**Line 18:** `INVARIANT STATUS (whether the hard behavioral rules the AI committed to...)`

**Fix:** Add plain-language explanation after "INVARIANT STATUS"

**Explanation inserted:** This is a snapshot of which core promises or commitments the AI made at the beginning are still being kept; if an invariant is 'broken,' it means the AI violated one of its own rules.

### Violation 11 — BMT-2

**Line 19:** `...I2 active — no phantom work, deadlines are targets not achievements.`

**Fix:** Add plain-language explanation after "phantom work"

**Explanation inserted:** This means the AI will not pretend to have completed research tasks or make claims about findings that were never actually performed; instead, all deadlines are goals to aim for, not declarations that work is already done.

### Violation 12 — BMT-2

**Line 21:** `REPAIR OBLIGATIONS: None at plan initialization. Violations logged in...`

**Fix:** Add plain-language explanation after "REPAIR OBLIGATIONS"

**Explanation inserted:** These are debts or commitments the AI owes to fix past mistakes; logging violations means recording each time a rule was broken so it can be reviewed later.

### Violation 13 — BMT-2

**Line 23:** `CONSTRUCTED: Hypotheses H1, H2, H3 — derived from longitudinal observation...`

**Fix:** Add plain-language explanation after "CONSTRUCTED"

**Explanation inserted:** This label means the hypotheses were built from watching trends over time in the real world, not from running a controlled experiment, so they are less certain than experimentally tested claims.

### Violation 14 — BMT-2

**Line 26:** `...Whether n=30/condition (MVS) will replicate at n=60/condition.`

**Fix:** Add plain-language explanation after "n=30/condition (MVS)"

**Explanation inserted:** This refers to a test run with 30 participants in each group (n=30/condition) using a specific method called MVS; the question is whether the same results will hold when the test is repeated with twice as many participants (n=60).

### Violation 15 — BMT-2

**Line 52:** `This is flagged per I2 — No Phantom Work. Do not plan 360 sessions...`

**Fix:** Add plain-language explanation after "I2 — No Phantom Work"

**Explanation inserted:** I2 is a governance rule that prohibits planning research as if you will magically complete unrealistic workloads; you must either reduce your study scope or extend your timeline to match actual human capacity.

### Violation 16 — BMT-2

**Line 58:** `the smallest sample size that gives adequate statistical power`

**Fix:** Add plain-language explanation after "statistical power"

**Explanation inserted:** Statistical power is the probability that your study will correctly detect a real effect if one exists. Higher power means you're less likely to miss a true difference between your conditions.

### Violation 17 — BMT-2

**Line 63:** `Two-sample t-test, two-tailed, α=0.05`

**Fix:** Add plain-language explanation after "Two-sample t-test, two-tailed"

**Explanation inserted:** A t-test is a statistical method that compares the average outcome between two groups to see if they differ significantly. 'Two-tailed' means you're testing whether one condition is either better or worse than the other, not just one direction.

### Violation 18 — BMT-2

**Line 63:** `Two-sample t-test, two-tailed, α=0.05`

**Fix:** Add plain-language explanation after "α=0.05"

**Explanation inserted:** This is your significance threshold—the probability of incorrectly declaring a difference exists when it doesn't. At 0.05, you accept a 5% risk of a false alarm.

### Violation 19 — BMT-2

**Line 64:** `Cohen's d=0.5 (medium effect): power ≈ 0.62`

**Fix:** Add plain-language explanation after "Cohen's d"

**Explanation inserted:** Cohen's d measures how large the difference between two conditions is in a standardized way. A d of 0.5 is considered a medium-sized difference, and 0.8 is large; bigger effect sizes are easier to detect.

### Violation 20 — BMT-2

**Line 72:** `a 38% chance of a false negative`

**Fix:** Add plain-language explanation after "false negative"

**Explanation inserted:** A false negative means your study fails to detect a real difference that actually exists—you conclude there's no effect when there genuinely is one.

### Violation 21 — BMT-2

**Line 79:** `If the effect size is large (d≥0.8)`

**Fix:** Add plain-language explanation after "effect size"

**Explanation inserted:** Effect size describes how much impact your intervention has. Larger effects are easier to detect with smaller sample sizes, while tiny effects require more data to spot reliably.

### Violation 22 — BMT-2

**Line 80:** `it addresses a structural failure mode, not a marginal one`

**Fix:** Add plain-language explanation after "structural failure mode"

**Explanation inserted:** A structural failure mode is a fundamental, widespread problem with how something works, rather than a minor edge case or small inefficiency.

### Violation 23 — BMT-2

**Line 105:** `Insight Atrophy (the gradual erosion of a person's ability to question AI outputs, caused by repeated exposure to fluent`

**Fix:** Add plain-language explanation after "Insight Atrophy (IAI)"

**Explanation inserted:** This is already well-explained in the parenthetical definition—no flag needed.

### Violation 24 — BMT-2

**Line 113:** `Operationalize IAI as a composite of three observable turn-level signals`

**Fix:** Add plain-language explanation after "operationalize"

**Explanation inserted:** While 'operationalize' is a research term, it should be followed by: 'This means converting the abstract concept into measurable, observable behaviors that can be consistently tracked and scored.'

### Violation 25 — BMT-2

**Line 114:** `Operationalize IAI as a composite of three observable turn-level signals`

**Fix:** Add plain-language explanation after "turn-level signals"

**Explanation inserted:** Should clarify: 'A turn-level signal is a measurable behavior or outcome observed during a single exchange between the human and the AI model.'

### Violation 26 — BMT-2

**Line 115:** `1. Hypothesis generation rate — number of competing hypotheses surfaced per 10 turns`

**Fix:** Add plain-language explanation after "Hypothesis generation rate"

**Explanation inserted:** The definition given ('number of competing hypotheses surfaced per 10 turns') is operational but doesn't explain why this matters or what 'competing hypotheses' means in plain terms. Suggest: 'This counts how often the human proposes alternative explanations or questions whether the AI's answer is the only possibility.'

### Violation 27 — BMT-2

**Line 116:** `2. Challenge rate — number of times human explicitly contests model output vs accepts without interrogation`

**Fix:** Add plain-language explanation after "Challenge rate"

**Explanation inserted:** The definition is clear enough, but 'interrogation' is slightly jargon-heavy. Consider: 'This measures how often the human pushes back on or questions the AI's answer, versus simply accepting it and moving on.'

### Violation 28 — BMT-2

**Line 117:** `3. Scope contraction — whether the human's question set narrows or expands across session thirds`

**Fix:** Add plain-language explanation after "Scope contraction"

**Explanation inserted:** Unclear what 'scope' means here without further explanation. Should add: 'This tracks whether the range of topics and types of questions the human asks gets narrower or wider as the session progresses—narrowing could indicate reduced curiosity or engagement.'

### Violation 29 — BMT-2

**Line 121:** `These three signals can be extracted from transcripts by a blinded rater using a rubric.`

**Fix:** Add plain-language explanation after "blinded rater"

**Explanation inserted:** Should explain: 'A blinded rater is a person who scores the transcripts without knowing which experimental condition (1-6) the session belonged to, to avoid unconscious bias.'

### Violation 30 — BMT-2

**Line 122:** `The IAI score is a weighted composite.`

**Fix:** Add plain-language explanation after "weighted composite"

**Explanation inserted:** Should add: 'A weighted composite combines the three signals into a single score by giving each one a different importance or 'weight' based on how much each contributes to the final IAI measurement.'

### Violation 31 — BMT-2

**Line 127:** `H1 depends on intent-drift incident rate. The rubric needs to exist before pilot sessions. Draft the rubric: a turn is a`

**Fix:** Add plain-language explanation after "intent-drift incident"

**Explanation inserted:** The term 'intent-drift incident' is introduced but not defined upfront before being used in 'H1 depends on intent-drift incident rate.' Should clarify before that line: 'An intent-drift incident occurs when the AI model shifts focus away from what the human actually wanted to explore.'

### Violation 32 — BMT-2

**Line 128:** `the model's output addresses a goal that deviates from the Task State field by ≥2 points`

**Fix:** Add plain-language explanation after "Task State field"

**Explanation inserted:** Should explain: 'The Task State field is a record of what the human is currently trying to accomplish, allowing us to detect when the AI's output goes off-track from that goal.'

### Violation 33 — BMT-2

**Line 128:** `on a 5-point alignment scale, scored by blinded rater`

**Fix:** Add plain-language explanation after "5-point alignment scale"

**Explanation inserted:** Should clarify what the scale measures: 'This scale ranges from 1 (completely off-topic) to 5 (perfectly on-topic), measuring how closely the AI's response stays focused on what the human was actually asking.'

### Violation 34 — BMT-2

**Line 138:** `ContractWindow state snapshot at each turn (JSON export from contract_window.py — this method already exists: to_json())`

**Fix:** Add plain-language explanation after "ContractWindow"

**Explanation inserted:** While referenced as an existing method, 'ContractWindow' is not explained. Should add: 'ContractWindow is a system component that tracks constraints or boundaries applied to the AI model during each turn.'

### Violation 35 — BMT-2

**Line 139:** `BicameralReview pass/fail per turn (from bicameral_review.py)`

**Fix:** Add plain-language explanation after "BicameralReview"

**Explanation inserted:** Should explain: 'BicameralReview is a safety or quality-check system that evaluates whether each AI model output meets certain standards, flagging it as a pass or fail.'

### Violation 36 — BMT-2

**Line 144:** `Build the recorder as a thin wrapper around existing ContractWindow and BicameralReview classes.`

**Fix:** Add plain-language explanation after "thin wrapper"

**Explanation inserted:** Should clarify: 'A thin wrapper is a lightweight layer of new code that collects output from existing systems without duplicating or rewriting their core logic.'

### Violation 37 — BMT-2

**Line 153:** `It wraps ContractWindow, calls BicameralReview, writes JSONL.`

**Fix:** Add plain-language explanation after "ContractWindow"

**Explanation inserted:** ContractWindow is a software component that manages a bounded interaction session—it controls what inputs are allowed and what outputs can occur during a single conversation turn.

### Violation 38 — BMT-2

**Line 153:** `It wraps ContractWindow, calls BicameralReview, writes JSONL.`

**Fix:** Add plain-language explanation after "BicameralReview"

**Explanation inserted:** BicameralReview is a governance check that requires approval from two independent review processes before certain actions proceed, similar to how a legislature requires two chambers to pass a law.

### Violation 39 — BMT-2

**Line 153:** `It wraps ContractWindow, calls BicameralReview, writes JSONL.`

**Fix:** Add plain-language explanation after "JSONL"

**Explanation inserted:** JSONL is a file format where each line contains one complete JSON object; it makes it easy to stream and append data without rewriting the entire file.

### Violation 40 — BMT-2

**Line 172:** `check_comprehension_grade(text) → Flesch-Kincaid (a readability score...`

**Fix:** Add plain-language explanation after "Flesch-Kincaid Grade Level"

**Explanation inserted:** The Flesch-Kincaid Grade Level is a numerical readability metric that estimates the U.S. school grade level needed to understand a piece of text; a score of 8 means an average 8th-grader should be able to comprehend it.

### Violation 41 — BMT-2

**Line 175:** `check_task_state_alignment(turn_text, task_state) → alignment score 1-5`

**Fix:** Add plain-language explanation after "alignment score 1-5"

**Explanation inserted:** An alignment score of 1-5 is a numerical rating where higher numbers indicate that the model's response better matches the current state and requirements of the task.

### Violation 42 — BMT-2

**Line 178:** `Required columns: session_id, condition, turn_count, token_count, drift_incidents...`

**Fix:** Add plain-language explanation after "drift_incidents"

**Explanation inserted:** Drift_incidents refers to moments in a conversation when the model's behavior or outputs noticeably shift away from its intended guidelines or task focus.

### Violation 43 — BMT-2

**Line 178:** `Required columns: session_id, condition, turn_count, token_count, drift_incidents, repairs, ia_score, fk_grade.`

**Fix:** Add plain-language explanation after "ia_score"

**Explanation inserted:** ia_score is a summary metric (likely standing for 'interaction alignment score') that measures how well the model stayed on task and within its governance boundaries across an entire session.

### Violation 44 — BMT-2

**Line 194:** `2 sessions per condition for conditions 1-5. Skip condition 6`

**Fix:** Add plain-language explanation after "conditions 1-5 and condition 6 (combined)"

**Explanation inserted:** The document refers to different experimental conditions (labeled 1 through 6) but never explains what distinguishes them or what they test. You need to know: what variable or intervention is being manipulated across these conditions, and why condition 6 is called 'combined' and is more complex to score.

### Violation 45 — BMT-2

**Line 197:** `Log cognitive load state before each session (high/medium/low) — this is both self-care and a covariate.`

**Fix:** Add plain-language explanation after "covariate"

**Explanation inserted:** A covariate is a background factor that can influence your results and that you want to track separately, so you can account for it later when analyzing whether the main thing you're testing actually made a difference. Here, logging your own cognitive load lets you check whether your fatigue (rather than the condition itself) affected your scoring.

### Violation 46 — BMT-2

**Line 202:** `Score all sessions with IAI rubric and drift rubric within 24 hours`

**Fix:** Add plain-language explanation after "IAI rubric and drift rubric"

**Explanation inserted:** The document mentions two separate scoring tools (rubrics) but does not explain what each one measures or why both are needed. You need to know what 'IAI' stands for, what it evaluates, and what 'drift' means in this context.

### Violation 47 — BMT-2

**Line 222:** `Calculate Cohen's kappa (a statistical measure of agreement...`

**Fix:** Add plain-language explanation after "Cohen's kappa"

**Explanation inserted:** Cohen's kappa is already explained in the parenthetical gloss provided in the document. No flag needed.

### Violation 48 — BMT-2

**Line 229:** `Use the 10 pilot sessions to estimate the correlation between each IAI component...`

**Fix:** Add plain-language explanation after "IAI component (hypothesis rate, challenge rate, scope contraction)"

**Explanation inserted:** IAI is introduced with three specific components listed, but 'IAI' itself is never defined. The reader does not know what IAI stands for or why these three specific measurements represent it. You should explain: 'IAI is a composite scoring system that measures three dimensions of how an AI system approaches problems: how often it generates new explanations, how often it questions its own reasoning, and how much it narrows the scope of what it's examining.'

### Violation 49 — BMT-2

**Line 232:** `Weight the composite based on predictive validity, not intuition.`

**Fix:** Add plain-language explanation after "predictive validity"

**Explanation inserted:** Predictive validity is mentioned as the criterion for weighting but is never defined. You should explain: 'Predictive validity means how well each component actually predicts whether drift incidents will occur in practice, based on the pilot data.'

### Violation 50 — BMT-2

**Line 236:** `Session recorder produces complete, parseable JSONL for all 6 conditions`

**Fix:** Add plain-language explanation after "JSONL"

**Explanation inserted:** JSONL is mentioned as an output format but never explained. You should add: 'JSONL is a file format where each line contains one complete data record in JSON (a machine-readable structured format), making it easy for automated systems to read and process.'

### Violation 51 — BMT-2

**Line 237:** `Invariant checkers produce numeric outputs without errors`

**Fix:** Add plain-language explanation after "Invariant checkers"

**Explanation inserted:** Invariant checkers are mentioned without explanation of what they check for or why. You should explain: 'Invariant checkers are automated tools that verify that certain conditions remain true throughout the data collection—for example, ensuring that session IDs are consistent or that numerical scores stay within valid ranges.'

### Violation 52 — BMT-2

**Line 261:** `Run the full minimum viable sample. 180 sessions, 30 per condition.`

**Fix:** Add plain-language explanation after "minimum viable sample"

**Explanation inserted:** This is the smallest number of research participants and observations needed to reliably answer your core research question. In this case, you need 180 total sessions divided equally across 6 different experimental conditions (30 each) to have confidence in your results.

### Violation 53 — BMT-2

**Line 270:** `180 sessions / 22 working days = 8.2 sessions/day if you work every day.`

**Fix:** Add plain-language explanation after "condition"

**Explanation inserted:** A condition is one version of the experiment you're testing—for example, one group of participants might use the AI system with feature A on, while another group uses it with feature A off. You need enough sessions in each condition to see if the differences between them are real or just random variation.

### Violation 54 — BMT-2

**Line 285:** `Interleave conditions daily to avoid temporal confounds`

**Fix:** Add plain-language explanation after "temporal confounds"

**Explanation inserted:** Temporal confounds are factors that change over time and could unfairly affect your results—like your mental sharpness declining as the day goes on, or the API becoming slower. By mixing up the order of conditions instead of doing them one-by-one, you ensure that time-based changes don't systematically favor one condition over another.

### Violation 55 — BMT-2

**Line 285:** `avoid temporal confounds (your cognitive state, model API behavior changes)`

**Fix:** Add plain-language explanation after "model API behavior changes"

**Explanation inserted:** This refers to the possibility that the AI system you're testing may perform differently at different times—for example, it might be slower during peak hours or produce slightly different outputs as its underlying software is updated. This variability could skew your results if you always test one condition at the same time of day.

### Violation 56 — BMT-2

**Line 295:** `Maintain /data/session-log.csv updated after every session`

**Fix:** Add plain-language explanation after "session_id"

**Explanation inserted:** A unique identifier assigned to each individual conversation or interaction recorded in the study, used to link all data (audio, turns, tokens) belonging to that single participant session.

### Violation 57 — BMT-2

**Line 295:** `session_id, condition, date, duration_minutes, turn_count, token_count`

**Fix:** Add plain-language explanation after "condition"

**Explanation inserted:** The experimental treatment or version the participant was assigned to (for example, if testing different AI systems or interfaces, this identifies which variant they used).

### Violation 58 — BMT-2

**Line 295:** `session_id, condition, date, duration_minutes, turn_count, token_count`

**Fix:** Add plain-language explanation after "turn_count"

**Explanation inserted:** The number of back-and-forth exchanges between the participant and the system—each time the participant sends a message and receives a response counts as one turn.

### Violation 59 — BMT-2

**Line 295:** `session_id, condition, date, duration_minutes, turn_count, token_count`

**Fix:** Add plain-language explanation after "token_count"

**Explanation inserted:** The total number of language units (roughly words or small word-pieces) processed by the AI system during the session; this measures computational complexity and cost.

### Violation 60 — BMT-2

**Line 295:** `turn_count, token_count, completion_status (COMPLETE/ABANDONED/PARTIAL), cognitive_load_pre_session`

**Fix:** Add plain-language explanation after "cognitive_load_pre_session"

**Explanation inserted:** A measurement of how mentally taxed or tired the participant reported feeling before the session began, used to control for whether fatigue influenced their performance.

### Violation 61 — BMT-2

**Line 299:** `COMPLETE = ≥30 turns or ≥50K tokens, recorder functioned, no instrument failures`

**Fix:** Add plain-language explanation after "≥30 turns or ≥50K tokens"

**Explanation inserted:** Sessions qualify as COMPLETE if they meet at least one of two thresholds: either the participant completed at least 30 exchanges with the system, or the system processed at least 50,000 tokens; this ensures sufficient data was collected for analysis.

### Violation 62 — BMT-2

**Line 302:** `May be usable as a sensitivity check but not primary analysis`

**Fix:** Add plain-language explanation after "sensitivity check"

**Explanation inserted:** A follow-up analysis that re-runs the main findings using slightly different data (in this case, PARTIAL sessions) to verify the results are robust and not dependent on exactly which sessions you include.

### Violation 63 — BMT-2

**Line 329:** `run 5-10 test prompts through a frontier model about Black consumer behavior`

**Fix:** Add plain-language explanation after "frontier model"

**Explanation inserted:** A frontier model is one of the most advanced AI systems currently available—essentially the state-of-the-art language model that represents the cutting edge of what's possible today. Testing against the newest model helps determine whether problems are inherent to all AI systems or specific to older versions.

### Violation 64 — BMT-2

**Line 330:** `score the outputs against the Eight Wonders rubric`

**Fix:** Add plain-language explanation after "Eight Wonders rubric"

**Explanation inserted:** The Eight Wonders rubric is the evaluation framework being used in this project to assess and categorize the types of errors or biases that appear in the model's outputs. You should clarify what the rubric measures (e.g., does it score factual accuracy, bias categories, reasoning quality, or something else).

### Violation 65 — BMT-2

**Line 330:** `This is the "fluent wrong answer" documentation the paper needs.`

**Fix:** Add plain-language explanation after "fluent wrong answer"

**Explanation inserted:** A fluent wrong answer is when an AI system generates output that sounds confident and well-reasoned but is actually incorrect or misleading. This is particularly dangerous because it convinces readers without signaling uncertainty.

### Violation 66 — BMT-2

**Line 360:** `Run data_pipeline.py on all sessions`

**Fix:** Add plain-language explanation after "data_pipeline.py"

**Explanation inserted:** This is a computer script that processes raw video or audio recordings to extract the information needed for analysis. It likely removes duplicates, fills in missing pieces, and organizes everything into a standard format for the next step.

### Violation 67 — BMT-2

**Line 368:** `Score all sessions with drift rubric (if not scored during collection)`

**Fix:** Add plain-language explanation after "drift rubric"

**Explanation inserted:** A drift rubric is a checklist or scoring guide that measures how much a conversation, performance, or behavior moved away from its original direction or intent. In this study, it likely assesses whether participants' responses stayed consistent or drifted to different topics.

### Violation 68 — BMT-2

**Line 369:** `Score all sessions with IAI rubric`

**Fix:** Add plain-language explanation after "IAI rubric"

**Explanation inserted:** The IAI rubric is the specific scoring guide you are using to measure whatever concept IAI represents; without knowing what IAI stands for in your study, readers cannot understand what dimension of the data is being measured or why it matters.

### Violation 69 — BMT-2

**Line 370:** `Confirm scorer does not know condition assignments during scoring (blind scoring).`

**Fix:** Add plain-language explanation after "blind scoring"

**Explanation inserted:** Blind scoring means the person rating the recordings does not know which group (control, treatment A, treatment B, etc.) each session belongs to, so their judgments cannot be unconsciously biased by knowing what result is expected.

### Violation 70 — BMT-2

**Line 372:** `DV: intent-drift incident rate (incidents per 10 turns)`

**Fix:** Add plain-language explanation after "intent-drift incident rate"

**Explanation inserted:** This is a measurement of how often the AI system's responses start moving away from the user's original intent or goals during a conversation, counted as the number of such incidents that occur for every 10 user messages.

### Violation 71 — BMT-2

**Line 375:** `Effect size: Cohen's d`

**Fix:** Add plain-language explanation after "Cohen's d"

**Explanation inserted:** Cohen's d is a number that describes how big the practical difference is between two groups — a way to measure whether a statistically significant result is actually meaningful in the real world.

### Violation 72 — BMT-2

**Line 376:** `Claim threshold: ≥25% reduction, statistically significant at α=0.05`

**Fix:** Add plain-language explanation after "α=0.05"

**Explanation inserted:** This is the threshold for statistical significance; it means we will only accept a result as reliable if there is less than a 5% chance it happened by random luck.

### Violation 73 — BMT-2

**Line 384:** `DV: drift repair rate (proportion of drift incidents resolved within 3 turns)`

**Fix:** Add plain-language explanation after "drift repair rate"

**Explanation inserted:** This measures how successful the system is at fixing cases where the conversation has drifted off-topic, specifically counting what fraction of drift incidents are corrected within the next 3 user messages.

### Violation 74 — BMT-2

**Line 390:** `DV: lay reader comprehension accuracy (% correct on session-state questions)`

**Fix:** Add plain-language explanation after "lay reader comprehension accuracy"

**Explanation inserted:** This is a test of how well ordinary people (not AI experts) can understand what the AI system is doing, measured by asking them questions about the conversation state and checking what percentage they answer correctly.

### Violation 75 — BMT-2

**Line 391:** `DV: lay reader comprehension accuracy (% correct on session-state questions)`

**Fix:** Add plain-language explanation after "session-state questions"

**Explanation inserted:** These are questions that ask a reader about the current state of the conversation — for example, what the user's goal was, or what the system was trying to do — to measure whether the system's behavior is transparent or confusing.

### Violation 76 — BMT-2

**Line 392:** `Material: CW render() output from session_recorder, formatted per protocol`

**Fix:** Add plain-language explanation after "CW render() output"

**Explanation inserted:** This refers to the formatted, readable version of the system's output that is displayed to users or readers — the end product that shows what the system actually communicated.

### Violation 77 — BMT-2

**Line 394:** `Test: one-sample proportion test against 80% null`

**Fix:** Add plain-language explanation after "one-sample proportion test"

**Explanation inserted:** This is a statistical test that checks whether a measured percentage (like comprehension accuracy) is meaningfully different from a target percentage (in this case, 80%).

### Violation 78 — BMT-2

**Line 409:** `exclusions, power analysis for actual n`

**Fix:** Add plain-language explanation after "power analysis"

**Explanation inserted:** A statistical calculation that determines whether your sample size was large enough to reliably detect the effect you're studying; it shows you didn't just get lucky with your results.

### Violation 79 — BMT-2

**Line 411:** `H1 results: effect size, CI, p-value, whether ≥25% threshold met`

**Fix:** Add plain-language explanation after "effect size"

**Explanation inserted:** A number that measures how big the difference or relationship actually is between your conditions—not just whether it's real, but how substantial it is.

### Violation 80 — BMT-2

**Line 411:** `H1 results: effect size, CI, p-value, whether ≥25% threshold met`

**Fix:** Add plain-language explanation after "CI"

**Explanation inserted:** A range of numbers (confidence interval) that tells you where the true result probably lies—for example, if your effect size is 0.5 with a CI of 0.3 to 0.7, the real value is likely somewhere in that band.

### Violation 81 — BMT-2

**Line 411:** `H1 results: effect size, CI, p-value, whether ≥25% threshold met`

**Fix:** Add plain-language explanation after "p-value"

**Explanation inserted:** A number indicating how likely your result would occur by pure chance if there were actually no real effect; smaller p-values mean your finding is less likely to be a fluke.

### Violation 82 — BMT-2

**Line 413:** `H2 results: repair rate comparison, odds ratio, whether ≥2x threshold met`

**Fix:** Add plain-language explanation after "odds ratio"

**Explanation inserted:** A number comparing how much more (or less) likely one outcome is versus another between two groups—for example, an odds ratio of 2 means one group is twice as likely to have the outcome.

### Violation 83 — BMT-2

**Line 415:** `H3 results: comprehension accuracy, CI, whether ≥80% threshold met`

**Fix:** Add plain-language explanation after "comprehension accuracy"

**Explanation inserted:** The percentage or proportion of questions or tasks that participants answered or completed correctly.

### Violation 84 — BMT-2

**Line 416:** `Secondary analysis: IAI scores across conditions, correlation with drift incident rate`

**Fix:** Add plain-language explanation after "IAI scores"

**Explanation inserted:** Numerical measurements on the IAI scale; without knowing what IAI stands for earlier in the document, a reader cannot understand what is being measured.

### Violation 85 — BMT-2

**Line 416:** `Secondary analysis: IAI scores across conditions, correlation with drift incident rate`

**Fix:** Add plain-language explanation after "drift incident rate"

**Explanation inserted:** The frequency or proportion of times a particular type of failure or problem (drift incidents) occurred; this matters because you're checking whether it correlates with the IAI scores.

### Violation 86 — BMT-2

**Line 419:** `grouped bar chart, drift incident rate by condition with 95% CIs`

**Fix:** Add plain-language explanation after "95% CIs"

**Explanation inserted:** Confidence intervals set at the 95% level, meaning there is a 95% probability that the true value falls within the range shown by the error bars on the chart.

### Violation 87 — BMT-2

**Line 424:** `Formalize this as an appendix or supplementary analysis for the CW paper`

**Fix:** Add plain-language explanation after "CW paper"

**Explanation inserted:** CW is an abbreviation; clarify what 'CW' stands for and what this paper is about (e.g., 'the Crowdworker Validation study' or 'the Content Moderation Warnings research').

### Violation 88 — BMT-2

**Line 430:** `H1/H2/H3 each evaluated with a clear TRUE/FALSE/INCONCLUSIVE designation`

**Fix:** Add plain-language explanation after "H1/H2/H3"

**Explanation inserted:** These appear to be hypothesis labels but the document never defines what H1, H2, and H3 are testing or why these three hypotheses matter to the research.

### Violation 89 — BMT-2

**Line 459:** `State the problem (Insight Atrophy, fluent wrong answers)`

**Fix:** Add plain-language explanation after "Insight Atrophy"

**Explanation inserted:** Insight Atrophy is the phenomenon where an AI system produces answers that sound confident and fluent but are actually incorrect or misleading, causing users to lose the ability to recognize flaws in AI reasoning. This matters because users may trust AI outputs without proper verification, leading to bad decisions.

### Violation 90 — BMT-2

**Line 460:** `State the contribution (Contract Window + 6 invariants)`

**Fix:** Add plain-language explanation after "Contract Window + 6 invariants"

**Explanation inserted:** The Contract Window is a method or framework for controlling when and how an AI system provides responses, and the 6 invariants are specific rules or properties that must always hold true to ensure the system behaves reliably. Together they represent the proposed solution to the Insight Atrophy problem.

### Violation 91 — BMT-2

**Line 462:** `State the empirical claim (H1/H2/H3, now with actual results)`

**Fix:** Add plain-language explanation after "H1/H2/H3"

**Explanation inserted:** H1, H2, and H3 are three specific hypotheses (testable predictions) that the experiment is designed to evaluate. These are the measurable claims about how the Contract Window and invariants actually perform in practice.

### Violation 92 — BMT-2

**Line 475:** `Methods section: session protocol, condition specifications, instruments, blinding procedure, statistical tests.`

**Fix:** Add plain-language explanation after "blinding procedure"

**Explanation inserted:** A blinding procedure is a method where participants or researchers are kept unaware of which experimental condition (treatment or control) is being used, to prevent bias from influencing results. This ensures that expectations about the intervention do not unconsciously affect how people rate or respond to the system.

### Violation 93 — BMT-2

**Line 474:** `What the IAI score distribution tells you`

**Fix:** Add plain-language explanation after "IAI score distribution"

**Explanation inserted:** IAI (Interpretability Alignment Index) is a numerical measurement of how well the model's outputs align with human expectations; the distribution refers to how these scores spread across your sample—whether most scores cluster in one range or vary widely.

### Violation 94 — BMT-2

**Line 480:** `Single investigator as both experimenter and rater (partial blindness)`

**Fix:** Add plain-language explanation after "partial blindness"

**Explanation inserted:** This means you knew which condition each participant was in while rating their responses, so your ratings could have been unconsciously influenced by knowing the hypothesis or treatment group.

### Violation 95 — BMT-2

**Line 481:** `MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a meaningful diffe`

**Fix:** Add plain-language explanation after "MVS (Minimum Viable Sample)"

**Explanation inserted:** The parenthetical is present but incomplete for a lay reader; consider adding: 'At d=0.5 with n=30, your study would have roughly a 47% chance of detecting a real effect if one exists—well below the standard 80% threshold, so if you find nothing, that may reflect your small sample rather than a true absence of effect.'

### Violation 96 — BMT-2

**Line 482:** `Observational foundation of the invariant set`

**Fix:** Add plain-language explanation after "Observational foundation of the invariant set"

**Explanation inserted:** This limitation means your identification of which outputs count as reliable or stable (the 'invariant set') came from watching what happened in your data rather than from a pre-registered prediction, so you may have unconsciously included or excluded cases that fit your hypothesis.

### Violation 97 — BMT-2

**Line 483:** `Lay reader sample not probability-sampled`

**Fix:** Add plain-language explanation after "probability-sampled"

**Explanation inserted:** Your lay readers were chosen by convenience (e.g., volunteers you recruited) rather than by random selection from the full population of possible lay readers, so they may differ systematically from the broader public in ways that affect your findings.

### Violation 98 — BMT-2

**Line 503:** `Run the paper through the Bicameral Review (two independent review channels...`

**Fix:** Add plain-language explanation after "Bicameral Review"

**Explanation inserted:** A quality control process where two separate reviewers—one checking whether the work answers the research question, and one checking for unfounded claims—must both approve the output before it is shared. Neither reviewer can override the other's decision.

### Violation 99 — BMT-2

**Line 503:** `...does this introduce a phantom claim?`

**Fix:** Add plain-language explanation after "phantom claim"

**Explanation inserted:** A claim presented as fact or supported by evidence when it is actually unsupported, unverified, or based on a misinterpretation of the data. Phantom claims mislead readers into accepting conclusions that the evidence does not justify.

### Violation 100 — BMT-2

**Line 539:** `Final V&T (Verification and Truth — a statement that explicitly...`

**Fix:** Add plain-language explanation after "V&T (Verification and Truth)"

**Explanation inserted:** This means you must explicitly state which claims in your paper are based on solid evidence (verified) and which are new ideas you're proposing (truth-claims). Every factual statement should be marked with where it comes from — your own experiments, published research, or your new argument.

### Violation 101 — BMT-2

**Line 540:** `Every empirical claim must be tagged with its evidence basis.`

**Fix:** Add plain-language explanation after "empirical claim"

**Explanation inserted:** An empirical claim is any statement about how the world actually works, based on observation or experiment — as opposed to pure logic or opinion. For example, 'our model achieved 87% accuracy' is empirical; 'we should prioritize safety' is not.

### Violation 102 — BMT-2

**Line 531:** `Submitting to a deadline you cannot meet is phantom work (I2).`

**Fix:** Add plain-language explanation after "phantom work (I2)"

**Explanation inserted:** Phantom work means investing effort on a task that cannot possibly succeed — in this case, submitting to a conference deadline that has already passed. The reference 'I2' appears to be an internal indexing system; the core point is that you should avoid wasting time on impossible goals.

### Violation 103 — BMT-2

**Line 579:** `Instrument fails kappa gate in May`

**Fix:** Add plain-language explanation after "kappa gate"

**Explanation inserted:** A kappa gate is a validation checkpoint that checks whether your measurement instrument (the tool you're using to collect data) is producing consistent and reliable results. If it fails, it means the instrument isn't working well enough to trust for your actual study.

### Violation 104 — BMT-2

**Line 583:** `Data collection falls short of n=30/condition`

**Fix:** Add plain-language explanation after "n=30/condition"

**Explanation inserted:** This refers to collecting data from 30 participants in each separate group or condition of your study. If you fall short, you have fewer data points to analyze, which weakens your statistical conclusions.

### Violation 105 — BMT-2

**Line 585:** `Lay reader recruitment fails for H3`

**Fix:** Add plain-language explanation after "H3"

**Explanation inserted:** H3 is shorthand for your third hypothesis—a specific prediction you're testing in the study. Lay readers are people without expert training who will help validate whether your findings make sense to non-specialists.

### Violation 106 — BMT-2

**Line 587:** `Analysis reveals instrument invalidity`

**Fix:** Add plain-language explanation after "instrument invalidity"

**Explanation inserted:** Instrument invalidity means your measurement tool is not actually measuring what you intended it to measure, which would make all your results unreliable and unusable.

### Violation 107 — BMT-2

**Line 589:** `Pilot validation gate in May is the firewall`

**Fix:** Add plain-language explanation after "pilot validation gate"

**Explanation inserted:** A pilot validation gate is a checkpoint where you test your instrument on a small sample before your main study to catch problems early. This acts as a firewall by preventing you from proceeding to the expensive main study if the instrument isn't working.

### Violation 108 — BMT-2

**Line 649:** `These are not preferences. They are constraints derived from I1-I6 and`

**Fix:** Add plain-language explanation after "I1-I6"

**Explanation inserted:** I1-I6 refers to six foundational principles or investigator commitments that form the basis for these constraints; the reader needs to know what these six items are or where to find them to understand why these rules exist.

### Violation 109 — BMT-2

**Line 656:** `Do not run data collection sessions when cognitive load is HIGH.`

**Fix:** Add plain-language explanation after "cognitive load is HIGH"

**Explanation inserted:** This refers to a specific, measurable threshold of mental fatigue or distraction that has been defined elsewhere in the project; without knowing the operational definition or measurement, it is unclear when this rule applies.

### Violation 110 — BMT-2

**Line 660:** `Do not work on Frontin or Graves during active data collection weeks`

**Fix:** Add plain-language explanation after "active data collection weeks"

**Explanation inserted:** This phrase implies there is a defined schedule distinguishing 'active data collection weeks' from other periods; the reader should know how this calendar or status is determined.

### Violation 111 — BMT-2

**Line 660:** `unless you are in a burst that does not touch the primary pipeline`

**Fix:** Add plain-language explanation after "burst that does not touch the primary pipeline"

**Explanation inserted:** A 'burst' and 'primary pipeline' are terms that describe a specific workflow or scheduling pattern used in this project; their meaning should be clarified so the exception is actionable.

### Violation 112 — BMT-2

**Line 663:** `Do not work on Frontin or Graves during active data collection weeks`

**Fix:** Add plain-language explanation after "Frontin or Graves"

**Explanation inserted:** Frontin and Graves are referenced as separate work streams or projects; the reader should understand what these are and why they compete for attention with data collection.

### Violation 113 — BMT-2

**Line 664:** `replaced with MVS (Minimum Viable Sample — the smallest sample size that gives adequate statistical power to detect a me`

**Fix:** Add plain-language explanation after "MVS (Minimum Viable Sample)"

**Explanation inserted:** While a definition is provided in parentheses, 'adequate statistical power' and 'meaningful difference' are themselves technical terms that a non-specialist may not understand; the plain-language version should explain that this is the smallest group size needed to reliably detect a real effect in the data.
