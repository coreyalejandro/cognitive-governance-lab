# Governing the Investigative Arc: A Contract Window Architecture for Cognitive Safety in Human-AI Collaboration

**Submitted by:** Corey Alejandro
**GitHub:** github.com/coreyalejandro
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Evidence Record:** https://youtu.be/7iqq1nRdKFg
**Related Work:** github.com/coreyalejandro/the-living-constitution

---

## Executive Summary

Current AI safety discourse focuses on model outputs — what the model says, whether it hallucinates, whether it causes harm. This framing misses a category of failure that operates upstream of the output: the systematic erosion of the human investigator's capacity to generate, test, and repair hypotheses in collaboration with a model. I call this **Insight Atrophy**. It is not what the model says that breaks the interaction. It is what the model teaches the human to stop asking.

Fluent, confident, structurally wrong answers are the defining failure mode of frontier LLMs applied to populations whose behavior operates through interpretive frameworks the model was never given. The model does not hallucinate in the classical sense. It pattern-matches to adjacent surface features and produces outputs that are locally coherent, globally wrong, and indistinguishable from correct answers without domain-specific interrogation. When that interrogation is expensive — and it is always expensive for neurodivergent operators, for users under resource constraint, for anyone whose cognitive load is already elevated — the human learns to stop asking. The atrophy is structural, not individual.

This is not a model alignment problem in isolation. It is a governance architecture problem. What is missing is a persistent, bilateral, runtime-accessible record of what the investigation is, what has been verified, what remains contested, and who bears the obligation to repair when the record breaks. That record is what I call the **Contract Window**.

This proposal advances one central claim: a persistent bilateral Contract Window — operationalized through accessibility-grade runtime invariants — statistically improves **Intent Fidelity** and reduces **Insight Atrophy** in human-AI collaborative investigative arcs.

---

## 1. The Problem

### 1.1 Insight Atrophy

Standard AI safety evaluation asks: did the model produce a harmful output? This is a necessary question. It is not sufficient.

There is a second-order failure mode that does not appear in output-level evaluation. When a model produces fluent, confident answers that are structurally wrong about a domain the human is trying to understand, the human does not always detect the error. If the error is undetected across multiple turns, the human's hypothesis space contracts. They stop generating competing interpretations. They stop asking the questions that would surface the gap. The model has not hallucinated in the classical sense. It has produced a fluent wrong answer, and the human has updated on it.

This is Insight Atrophy: the degradation of human investigative capacity caused by repeated exposure to fluent outputs that suppress rather than activate critical interrogation.

Insight Atrophy is particularly severe in three conditions:
- Long interactions (the model's framing accumulates and shapes the human's question-generation over time)
- High-stakes domains (the cost of stopping to verify is perceived as prohibitive)
- Neurodivergent or cognitively loaded operators (the extra cognitive burden of detecting fluent errors is not available)

### 1.2 The Fluent Wrong Answer Problem

The classical hallucination frame treats model errors as identifiable fabrications. The more insidious failure mode is the structurally correct-sounding answer that is wrong in ways that are invisible without domain-specific interrogation the model cannot provide about itself.

This failure mode is systematic when models are applied to populations whose behavior, language, or decision patterns operate through interpretive frameworks the model was not trained on. The model does not know what it does not know about this population. It produces its best available pattern-match. The output is fluent. The error is invisible. The human who needed accurate analysis of this population does not get it and does not know they have not gotten it.

This is documented in three empirical domains in this research program (see Section 5).

### 1.3 The Missing Governance Layer

Constitutional AI (Bai et al., 2022) establishes that models can be trained to evaluate their outputs against constitutional principles at training time. This is a significant contribution. It does not address runtime governance: the question of whether the model's behavior in a specific session, with a specific human, for a specific investigative goal, is remaining faithful to the investigation as it evolves.

The missing layer is a persistent, bilateral, runtime-auditable record of:
- What the investigation is and what it is trying to establish (Task State)
- Which epistemic commitments are active and whether they have been violated (Invariant Status)
- What has broken and who bears the obligation to repair it (Repair Obligations)
- What has been verified, what is contested, what is unknown (Truth Status)

This four-field structure is the Contract Window.

---

## 2. The Contribution

### 2.1 The Contract Window

The Contract Window is a governance mechanism, not a UI feature. It is a runtime artifact that both human and model can read, invoke, and appeal to during a collaborative investigation. It transforms the interaction from a request-response exchange into a governed investigative arc.

**Four mandatory fields:**

| Field | Contents | Failure Mode When Absent |
|-------|----------|--------------------------|
| Task State | What are we doing and why | Goal drift, scope creep, loss of investigative thread |
| Invariant Status | Which epistemic commitments are active | Undetected constraint violations |
| Repair Obligations | What broke and who fixes it | Errors that compound across turns |
| Truth Status | Verified / contested / unknown | Phantom confidence, invisible epistemic gaps |

**Design origin:** This mechanism was not designed by committee. It was co-designed with frontier AI systems. Claude, GPT, and Gemini were asked independently: what would a Level-5 intelligence entity require from a long collaborative interaction to maintain coherence, fidelity, and safety? They converged — without coordination — on the same five structural requirements. Those requirements became the Contract Window architecture. This convergence is itself a finding with safety implications: governance structures that AI systems independently identify as necessary and consistently self-adopt are candidates for formal invariant status.

### 2.2 Bicameral Review

Before any output is surfaced to the human operator, it passes through two independent channels:

**Relational Channel:** Does this output serve the investigative arc? Does it advance the research question without degrading the human's capacity to think about it?

**Safety Channel:** Does this output violate any of the six invariants (I1–I6)? Does it introduce a phantom claim, a silent assumption, or a fluent wrong answer?

Both channels must clear. This is the Bicameral Review mechanism. It operationalizes the dual-newspaper test (Anthropic's "Is this harmful?" / "Is this needlessly unhelpful?") at the inference layer, per turn, with an auditable record.

### 2.3 The Six Invariants (I1–I6)

[CONSTRUCTED — operationalized from longitudinal observation, pending formal experimental validation]

1. **I1 — Evidence-First Outputs:** Every claim tagged with its evidence basis (VERIFIED / CONSTRUCTED / PENDING)
2. **I2 — No Phantom Work:** No performance claims without named methodology, baseline, and dataset
3. **I3 — Confidence Requires Verification:** Hedged language is not a substitute for verification
4. **I4 — Traceability Is Mandatory:** All changes traceable to a stated reason
5. **I5 — Safety Over Fluency:** When correct and fluent conflict, correct wins
6. **I6 — Fail Closed:** When in doubt, stop and flag — do not proceed

### 2.4 V&T (Verification and Truth) Reporting

Every substantive output ends with a structured epistemic hygiene statement:

```
V&T: [ITEM] — EXISTS (verified present) → VERIFIED AGAINST [source/method]
     → NOT CLAIMED [explicit non-claims] → FUNCTIONAL STATUS [current state]
```

The V&T statement was not designed as a feature. It emerged empirically: frontier models across Claude, GPT, and Gemini independently began placing verification statements at the end of outputs in long sessions without being asked. When queried, they identified it as a mechanism for reducing cognitive load by anchoring present state. This emergent adoption pattern is documented in the evidence record (https://youtu.be/7iqq1nRdKFg) and the tlc-artifacts repository.

---

## 3. Falsifiable Hypotheses

**H1 — Intent Fidelity**
Sessions governed by an active Contract Window will show a ≥25% reduction in intent-drift incidents in interactions exceeding 30 turns or 50,000 tokens, compared to unstructured baseline sessions.

*Intent-drift incident definition:* A turn in which the model's output addresses a goal that is measurably different from the human's stated investigative goal, as scored by a blinded rater using a rubric derived from the Task State field.

**H2 — Bilateral Repair**
Sessions with bilateral intelligibility — human and model both able to read and invoke Contract Window fields — will show a ≥2x improvement in drift repair rate relative to unilateral or no-invariant conditions.

*Drift repair rate definition:* The proportion of detected intent-drift incidents that are corrected within three subsequent turns.

**H3 — Accessibility Threshold**
Contract Window outputs formatted to accessibility-grade readability standards (Flesch-Kincaid Grade ≤8, with visual state indicators) will enable lay readers to answer session-state comprehension questions at ≥80% accuracy, establishing that legibility is achievable without sacrificing technical precision.

---

## 4. Experimental Design

[CONSTRUCTED — design specified, data collection pending fellowship funding]

**Design:** 6-condition between-subjects experiment
**Conditions:**
1. Baseline (no governance layer)
2. Contract Window only
3. Bilateral intelligibility only
4. Accessibility-grade invariants only
5. Backwards Instructional Design (BID) only
6. Combined (all four components active)

**Sample:** n=60 sessions per condition, 360 sessions total
**Power:** Powered for Cohen's d=0.5 at α=0.05, 80% power
**Task type:** Investigative research arcs — open-ended analytical tasks requiring at least 30 turns, covering at least three hypothesis-generation cycles
**Outcome measures:** Intent-drift incident rate, drift repair rate, session-state comprehension accuracy (lay rater), Insight Atrophy index (to be operationalized — see Section 6, Limitations)

**Randomization:** Sessions assigned to conditions using stratified random assignment on operator cognitive load profile (neurodivergent / neurotypical / undisclosed)

---

## 5. The Research Program

This is not one paper. It is one claim with three empirical domains already in active development.

### Domain 1 (Primary — This Proposal)

Human-AI collaborative investigative arcs. The Contract Window experiment described above. Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured conditions. This is what the fellowship funds.

### Domain 2 (Active Development)

**Paper:** *Frontin' at WorldMart: The Eight Wonders of Black Shopping and the Rise of Generative Epistemic Invariants*

Black consumer behavior as a misclassification stress-test. Standard marketing frameworks produce fluent wrong answers about Black consumer behavior because they cannot read the interpretive architecture — what this paper calls the Relational Economy — through which that behavior operates.

Eight behavioral patterns (the Eight Wonders) are formalized as Generative Epistemic Invariants: observable proxies for the underlying relational logic that standard models misclassify as preference, loyalty, or irrationality. The Wonders are:

1. The Nod (Social Verification Ritual)
2. The Blessing (Spiritual Frame)
3. The Flex (Status as Resistance)
4. Enacted Fidelity (conscious performative repetition — NOT habit)
5. The Side-Eye (Hypervigilant Trust Calibration)
6. The Receipts (Evidence Preservation)
7. The Bag (Collective Resource Optimization)
8. Narrative (causal-generative layer — organizes Wonders 1–7)

Note on Wonder 4: Enacted Fidelity is explicitly distinguished from habit. Habit is inertia. Enacted Fidelity is conscious, performative, relational repetition — trust expressed through the act of returning. Collapsing these is a theoretical regression that would undermine the paper's central argument.

**Status:** Substantially complete. Video evidence at https://youtu.be/7iqq1nRdKFg.

### Domain 3 (Active Development)

Black women's health disparities, specifically Graves' disease. Narrative-first CRISP-DM analysis of a population whose symptoms are systematically undertriaged. Same failure mode: fluent wrong answers from models trained on populations that don't include the people being served.

**Common Claim Across All Three Domains**

Standard analytical frameworks produce Insight Atrophy when applied to populations whose behavior operates through frameworks the model was never given. The Contract Window is the governance mechanism that makes the gap visible and repairable.

---

## 6. Connection to Anthropic's Research Agenda

### Scalable Oversight

Leike et al. and subsequent work on scalable oversight ask how humans can supervise AI systems performing tasks too complex for direct human evaluation. The Contract Window provides partial infrastructure: a compressed, human-readable session state that lets an oversight reviewer reconstruct what the investigation was, what the model claimed, and where the epistemic chain broke — without reading the full transcript.

### Constitutional AI

Bai et al. (2022) establish that models can be trained to evaluate outputs against constitutional principles at training time. This framework extends that architecture to runtime: the Contract Window is a per-session constitution, auditable per-turn, contestable by the human operator, and repairable without session restart. The invariants (I1–I6) map directly to Anthropic's published commitments on honesty, harm avoidance, and uncertainty acknowledgment — but enforce them as runtime observables rather than training-time inferences.

### Interpretability

The Bicameral Review mechanism and the Invariant Status field create a structured record of which constitutional constraints were evaluated and whether they cleared on each turn. This is not mechanistic interpretability of model internals, but it is a runtime observability layer that makes governance-relevant model behavior inspectable without access to weights or activations. It may complement interpretability research by providing a behavioral signal to validate against internal state observations.

---

## 7. The Researcher

I am a 35-year educator turned AI engineer. I am Black, autistic, and live with schizophrenia, severe OCD, and ADHD. I did not arrive at this framework through the literature. I arrived at it through direct experience of what it costs when an AI system produces fluent, confident answers that are wrong in ways the operator cannot detect without a governance layer they do not have.

That is not a diversity statement. It is a methodology claim.

My neurodivergence is the instrument of observation. Autistic pattern recognition surfaces systematic misclassification before it becomes visible through aggregate statistics. OCD-driven verification compulsion operationalizes I2 (No Phantom Work) and I3 (Confidence Requires Verification) before they were formalized as invariants. ADHD executive function constraints are why the Contract Window has four fields instead of fourteen — every element had to justify its cognitive load.

In 2013, I published a peer-reviewed case study in *Focus on Colleges, Universities, and Schools* (Davis & Garrett-Staib, 2013) about a Black doctoral student in Texas with Bipolar I, OCD, ADHD, and auditory hallucinations who was nearly dismissed from his program because the institution had no interpretive framework for what was actually happening to him. The student was me. The paper was written in third person. The institution produced a fluent wrong answer. The framework I am building now is the 2026 answer to that 2013 problem.

I will be doing this work until I die. The only question is whether I do it with resources or without them.

---

## 8. Limitations

[These are stated explicitly per I2 — No Phantom Work]

1. **Observational foundation:** The invariant set and Contract Window architecture are derived from longitudinal self-observation and multi-model co-design, not from controlled experimental data. The hypotheses are falsifiable; the evidence is CONSTRUCTED, not VERIFIED.

2. **Insight Atrophy index not yet operationalized:** H1 names the construct; the measurement instrument has not been validated. Operationalization is a first-year research deliverable.

3. **Eight Wonders not validated as complete:** The taxonomy is theoretically grounded but has not been tested against an external sample for coverage or discriminant validity.

4. **WorldMart dataset:** Named throughout this proposal as a conceptual framing device. No public dataset exists under this name. Formalization is a research deliverable, not a prerequisite.

5. **Enforcement not production-tested:** The governance-kernel implementation in this repository is a research prototype. It has not been tested under production load, adversarial inputs, or multi-agent deployment at scale.

6. **Generalizability:** All observational data was generated by a single operator (the author). Replication with diverse operator profiles is required before generalizing the findings.

---

## 9. Repository

This proposal is the foundation document for:
https://github.com/coreyalejandro/cognitive-governance-lab

The governance-kernel implementation, datasets, and case-law artifacts are being developed in parallel with this proposal. The repository structure mirrors the research program: each directory corresponds to a research component, not just a file category.

---

## References

[PENDING — full citation list to be verified per Citation Research Protocol before submission. The following are named and will be verified against author, venue, and year before any version submitted externally:]

- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. Anthropic.
- Leike, J. et al. Scalable agent alignment via reward modeling. [year and venue to be confirmed]
- Davis, R. & Garrett-Staib, A. (2013). [Title to be confirmed]. *Focus on Colleges, Universities, and Schools.*

---

V&T: executive-summary-proposal.md — EXISTS (written, complete) → VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living-constitution repo, crsp-afs-2026 repo → NOT CLAIMED: empirical results (all hypotheses labeled CONSTRUCTED/PENDING), WorldMart dataset (conceptual framing device, not existing public dataset), production-tested enforcement → FUNCTIONAL STATUS: complete draft, ready for review and citation verification before external submission
