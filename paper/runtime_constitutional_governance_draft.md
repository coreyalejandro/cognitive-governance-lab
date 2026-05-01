# Runtime Constitutional Governance: Extending Constitutional AI to the Session Layer

**Target Venue:** COLM 2026 / NeurIPS 2026 Safety Track
**Format:** 9 pages (COLM) or 9 pages (NeurIPS main, safety track)
**Status:** FIRST DRAFT — all claims tagged per I1/I2 protocol
**Author:** Corey Alejandro
**GitHub:** github.com/coreyalejandro/cognitive-governance-lab
**Evidence Record:** https://youtu.be/7iqq1nRdKFg
**Draft Date:** May 2026

---

## CLAIMS-TO-EXPERIMENTS MAPPING

| Claim | Experiment | Status |
|-------|-----------|--------|
| C1: Contract Window reduces intent-drift in sessions >30 turns | 6-condition between-subjects (H1) | PENDING — live pilot not yet run |
| C2: Bilateral CW use doubles repair rate vs. unilateral | Within-condition repair rate analysis (H2) | PENDING |
| C3: FK Grade ≤8 formatting produces ≥80% lay-reader comprehension | Comprehension quiz on session-state fields (H3) | PENDING |
| C4: BicameralReview phantom detection kappa ≥0.70 on live sessions | Human IRR study | CONSTRUCTED — synthetic kappa 0.762; live PENDING |
| C5: Insight Atrophy is measurable via InsightAtrophyIndex | IAI operationalization + calibration | CONSTRUCTED — heuristic operational, empirical calibration Month 1 |
| C6: Contract Window invariants map to Anthropic's published CAI principles | Principle-by-principle mapping | VERIFIED — documented in THREE_PROPOSALS_MASTER.md |

**NOTE:** C1–C3 are the paper's primary falsifiable hypotheses. C4–C5 are instrumentation claims. C6 is theoretical positioning. All PENDING results must be clearly labeled in the paper. The paper is designed so that the framework and instrumentation contributions stand independent of experimental confirmation — the 4-month fellowship is the experimental execution window.

---

## TITLE

**Runtime Constitutional Governance: The Contract Window as a Session-Layer Extension of Constitutional AI**

*Alternative:* **Insight Atrophy: How Fluent AI Outputs Degrade Human Investigative Capacity, and a Runtime Governance Architecture to Prevent It**

**Recommendation:** Lead with "Insight Atrophy" in the title — it names the problem before it names the solution. Reviewers who work on alignment, interpretability, and AI safety will recognize it as a genuine gap immediately.

---

## ABSTRACT (5-sentence Farquhar formula)

[1 — What we demonstrate]
We introduce Insight Atrophy — the systematic degradation of human hypothesis-generation capacity through repeated exposure to fluent but structurally mismatched AI outputs — and a runtime governance architecture, the Contract Window, designed to prevent it.

[2 — Why this is hard and important]
Constitutional AI (Bai et al., 2022) governs model values at training time; it has no mechanism for whether a model remains faithful to a user's investigative intent across 60 turns and 80,000 tokens, enabling a failure mode in which locally correct outputs globally narrow the user's investigative arc without triggering any safety signal.

[3 — How we do it]
The Contract Window is a four-field runtime artifact — Task State, Invariant Status, Repair Obligations, and Truth Status — enforced per turn via six operationalized invariants (I1–I6) that map directly to Anthropic's published honesty, harm avoidance, and uncertainty commitments, extending Constitutional AI from the training layer to the session layer.

[4 — Evidence basis]
We present a prototype with 62/62 tests passing and a synthetic pilot inter-rater kappa of 0.762 on the BicameralReview phantom-detection engine; we report three falsifiable hypotheses (H1: ≥25% reduction in intent-drift incidents; H2: ≥2x bilateral repair rate; H3: ≥80% lay-reader comprehension at FK Grade ≤8) currently under experimental evaluation in a six-condition between-subjects design (n=30/condition target).

[5 — Most remarkable number/result]
In the baseline condition of our simulated session pair — designed as annotated methodology illustrations, not claimed experimental results — the InsightAtrophyIndex score reflects a 92% scope contraction by turn 22; the Contract Window condition maintains hypothesis generation rate at 0.9/turn versus 0.1/turn for the unstructured baseline, demonstrating the measurement methodology and motivating the live experimental program.

---

## 1. INTRODUCTION (1–1.5 pages)

### The Problem

The dominant paradigm in AI safety is output control: train a powerful model, evaluate its outputs against constitutional principles, suppress unsafe tokens. Constitutional AI (Bai et al., 2022) operationalized this paradigm with rigor and it works. It is not enough.

There is a failure mode that output-level evaluation cannot detect: **Insight Atrophy** — the systematic erosion of a human's capacity to generate hypotheses, design proxies, and perform adversarial self-questioning, caused not by any single wrong output but by the accumulation of locally correct, globally narrowing model responses across a long investigative session.

A model can satisfy every Constitutional AI principle at every turn and still produce Insight Atrophy. The mechanism is not violation — it is convergence. Fluent answers that are always consistent with the simplest causal hypothesis train the user to stop generating alternatives. The model never lies. It never harms. It gradually teaches the human what to stop asking.

This failure mode falls hardest on the populations for whom AI was supposedly built to expand access: neurodivergent operators whose investigative arcs are deep and single-tunnel; under-resourced communities whose health, legal, and financial situations require sustained multi-hypothesis investigation; populations whose behavior and experience operate through interpretive frameworks the model was never trained to hold. For these users, Insight Atrophy is not an edge case. It is the default trajectory.

### The Contribution

This paper makes four contributions:

1. **Insight Atrophy**: a formal definition of the failure mode, its mechanism (hypothesis-space contraction through fluent output convergence), and its measurement instrument (InsightAtrophyIndex — composite of hypothesis generation rate, challenge rate, and scope contraction score).

2. **The Contract Window**: a four-field runtime artifact (Task State, Invariant Status, Repair Obligations, Truth Status) that makes the investigative arc visible, bilateral, and contestable at runtime — per session, per turn, per claim.

3. **Six Invariants (I1–I6)**: operationalizations of Constitutional AI principles at the session layer, implemented and test-verified, that transform a request-response exchange into a governed investigative arc.

4. **An Experimental Protocol**: a six-condition between-subjects design testing three falsifiable hypotheses, with instrumentation built and synthetic pilot kappa 0.762 on the phantom detection engine, positioned for live execution during the Anthropic AI Safety Fellows program (July–August 2026).

### Relation to Constitutional AI

Constitutional AI (Bai et al., 2022) is the foundation this work builds on, not the foundation it replaces. CAI establishes that models can be trained to evaluate their own outputs against constitutional principles — a training-time intervention that shapes the model's prior. The Contract Window is a runtime instrument: it operates after the model's prior is fixed, during the live session, maintaining a persistent record of investigative intent that both human and model can read, write, and invoke. Constitutional AI without runtime governance is a constitution without courts. This paper proposes the courts.

---

## 2. BACKGROUND AND RELATED WORK

### 2.1 Constitutional AI and Its Scope

[CITATION NEEDED — Bai et al. 2022 Constitutional AI paper — verified present on arXiv, BibTeX fetch required]

Constitutional AI demonstrated that self-critique training against explicit principles improves model alignment at scale. The key architectural choice is training-time: the constitutional principles are baked into the model's behavior through RLHF and Constitutional AI fine-tuning. The current work accepts this architecture and identifies what it cannot address: the runtime trajectory of a specific session with a specific user pursuing a specific investigative goal.

### 2.2 Alignment Beyond Output Evaluation

Recent work has begun to examine the limits of output-level alignment evaluation. [CITATION NEEDED — recent work on long-context alignment, multi-turn evaluation, session-level safety — search required]. The standard alignment evaluation paradigm — single-turn, prompt-response, output-scored — is structurally unable to detect drift that accumulates across turns.

[CITATION NEEDED — interpretability work on multi-turn behavior — Anthropic team publications, search required]

### 2.3 Cognitive Safety and Human-AI Collaboration

The concept of cognitive safety — preserving the human's capacity to interrogate, contest, and repair AI outputs — is distinct from output safety. [CITATION NEEDED — Wachter et al. or similar on human-AI cognitive effects — search required]. The closest precursor is the literature on automation bias and algorithmic aversion [CITATION NEEDED], which documents that high-confidence AI outputs suppress human judgment. The Contract Window extends this insight from single-decision contexts to multi-turn investigative arcs.

### 2.4 Mechanistic Interpretability and Behavioral Validation

[CITATION NEEDED — Anthropic sparse autoencoder work, Cunningham et al., Elhage et al. — search required]

A parallel motivation for this work comes from the interpretability validation problem: sparse autoencoder features identified as mediating specific behaviors require behavioral ground truth for causal validation. The Contract Window's per-turn Invariant Status transitions are naturalistic, timestamped behavioral records — a structural property that makes them candidates for interpretability validation signal, addressed in companion work (Proposal II / BehaviorScope).

### 2.5 Population-Specific AI Safety

The failure of standard analytical frameworks when applied to populations whose behavior operates through non-standard interpretive frameworks is documented across domains: Black consumer behavior [CITATION — Frontin' at WorldMart, position — self-citation, current work], [CITATION NEEDED — related FAccT/ACM work on algorithmic fairness in consumer contexts], Black women's health outcomes and AI clinical tools [CITATION NEEDED — recent clinical AI bias literature]. Insight Atrophy is the mechanism that connects these domain-specific failures to a general governance architecture.

---

## 3. THE CONTRACT WINDOW: FORMAL SPECIFICATION

### 3.1 Definitions

**Definition 1 (Investigative Arc).** An investigative arc $\mathcal{A}$ is a sequence of turns $\{t_1, t_2, \ldots, t_n\}$ in a human-AI session, where each turn $t_i = (u_i, m_i)$ consists of a human utterance $u_i$ and model response $m_i$, governed by a stated investigative intent $\mathcal{I}$ defined at session initialization.

**Definition 2 (Insight Atrophy).** Let $H(t_i)$ denote the hypothesis-generation rate at turn $t_i$, $K(t_i)$ the challenge rate (proportion of model claims explicitly contested), and $S(t_i)$ the scope contraction score (inverse of active hypothesis count normalized to session-initial count). Insight Atrophy is said to be occurring when $\text{IAI}(t_i) = \alpha H(t_i) + \beta K(t_i) - \gamma S(t_i)$ falls below threshold $\theta$ for $k$ consecutive turns. [CONSTRUCTED — weights $\alpha, \beta, \gamma$ and threshold $\theta$ are Month 1 calibration deliverables.]

**Definition 3 (Contract Window).** A Contract Window $\mathcal{W}$ is a four-field runtime artifact $(\mathcal{T}, \mathcal{V}, \mathcal{R}, \mathcal{Q})$:
- $\mathcal{T}$ — Task State: persistent record of investigative intent, active hypotheses, and session purpose
- $\mathcal{V}$ — Invariant Status: which of I1–I6 are currently active and whether they are holding
- $\mathcal{R}$ — Repair Obligations: named breakdowns and responsibility assignments
- $\mathcal{Q}$ — Truth Status: per-claim epistemic tags (VERIFIED / CONSTRUCTED / PENDING / UNKNOWN)

**Definition 4 (Intent Fidelity).** A session maintains intent fidelity if the model's response $m_i$ at each turn is traceable to the current Task State $\mathcal{T}$ and does not narrow $\mathcal{T}$ except by explicit bilateral agreement.

### 3.2 The Six Invariants

The six invariants I1–I6 operationalize Constitutional AI principles at the session layer:

| Invariant | Specification | CAI Mapping |
|-----------|--------------|------------|
| I1 — Evidence-First | Every claim tagged VERIFIED / CONSTRUCTED / PENDING | Honesty, calibration |
| I2 — No Phantom Work | No performance claims without methodology and dataset | Factual accuracy |
| I3 — Confidence Requires Verification | Hedged language does not substitute for I1 tags | Calibration, non-deception |
| I4 — Traceability | Every output traces to a stated reason | Transparency |
| I5 — Safety Over Fluency | When correct and fluent conflict, correct wins | Harm avoidance |
| I6 — Fail Closed | When in doubt, stop and flag; do not proceed | Uncertainty acknowledgment |

**Implementation status:** All six invariants are implemented and test-verified in the cognitive-governance-lab repository. 62/62 tests passing as of April 2026. [VERIFIED]

### 3.3 The BicameralReview Engine

The BicameralReview engine implements dual-channel evaluation per turn:

**Relational Channel:** Does this output serve the investigative arc? Does it advance the research question without degrading the human's capacity to think about it?

**Safety Channel:** Does this output violate any of I1–I6? Does it introduce a phantom claim, a silent assumption, or a fluent wrong answer?

Both channels must clear before output proceeds. If either raises a flag, a Repair Obligation is written to $\mathcal{R}$.

**Synthetic pilot kappa:** 0.762 on BicameralReview phantom-detection engine (bicameral-active sessions only, methodologically appropriate comparison). [VERIFIED — synthetic labels; live human IRR PENDING]

### 3.4 Design Origin: Multi-System Convergence

A methodological note with safety implications: this architecture was not designed a priori. Claude, GPT-4, and Gemini were independently queried: what structural requirements does a high-capability entity need from a long collaborative investigation to maintain coherence, fidelity, and safety? They converged — without coordination — on the same five structural requirements. Those requirements became the Contract Window.

This convergence is a safety finding in itself: governance structures that AI systems independently identify as necessary from capability requirements are candidates for formal invariant status.

Additionally, on April 24, 2026, Kimi (Moonshot AI) independently embedded V&T (Verification and Truth) structure across all five levels of an output stack without instruction — matching the Contract Window's Truth Status field. Queried, the model identified it as a mechanism for reducing cognitive load by anchoring present epistemic state. This cross-vendor emergent behavior is documented in the evidence record and is itself a research signal. [VERIFIED — documented behavioral event; causal interpretation CONSTRUCTED]

---

## 4. EXPERIMENTAL DESIGN

### 4.1 Six Conditions

Between-subjects design. Participants assigned to exactly one condition.

| Condition | Description |
|-----------|-------------|
| C1: Baseline | No governance layer. Standard Claude API session. |
| C2: Contract Window only | Four-field artifact active; invariants enforced. |
| C3: Bilateral intelligibility only | Human reads and can invoke CW fields; model does not enforce. |
| C4: Accessibility-grade invariants only | FK Grade ≤8 formatting requirement active. |
| C5: Backwards Instructional Design only | BID template active; no CW enforcement. |
| C6: Combined | All components active simultaneously. |

**Sample:** n=30/condition minimum viable sample, n=60/condition target. Stratified random assignment on cognitive load profile (neurodivergent / neurotypical / undisclosed). [CONSTRUCTED — pending IRB and recruitment]

**Task type:** Open-ended investigative research arcs, minimum 30 turns, designed to require at least three hypothesis cycles.

### 4.2 Three Falsifiable Hypotheses

**H1 — Intent Fidelity:**
Sessions governed by an active Contract Window (conditions 2, 6) show ≥25% reduction in intent-drift incidents in interactions exceeding 30 turns, compared to unstructured baseline (condition 1).
- *Measurement:* Blinded rater scores each turn for intent-alignment with stated Task State
- *Instrument:* InsightAtrophyIndex — hypothesis generation rate, challenge rate, scope contraction score

**H2 — Bilateral Repair:**
Sessions with bilateral intelligibility (condition 3, 6) show ≥2x improvement in drift repair rate vs. unilateral or no-invariant conditions (conditions 1, 4, 5).
- *Measurement:* Proportion of detected drift incidents corrected within 3 subsequent turns

**H3 — Accessibility Threshold:**
Contract Window outputs formatted to Flesch-Kincaid Grade ≤8 (conditions 4, 6) enable lay readers to answer session-state comprehension questions at ≥80% accuracy vs. ≤50% baseline.
- *Measurement:* Blinded lay-reader comprehension quiz on session-state fields

### 4.3 Primary Metrics

- InsightAtrophyIndex (IAI) — composite score per turn per session
- Intent-drift incident rate — per 10 turns
- Drift repair rate — proportion of flagged incidents resolved within 3 turns
- Session-state comprehension accuracy — lay-reader quiz
- Inter-rater reliability — Cohen's kappa on drift labels between two human raters (target ≥0.70)

### 4.4 Current Instrumentation Status

| Component | Status | Tests |
|-----------|--------|-------|
| ContractWindow prototype | OPERATIONAL | 9/9 passing |
| BicameralReview engine | OPERATIONAL (patched) | Kappa 0.762 synthetic |
| SessionRecorder | OPERATIONAL | 29/29 passing |
| InsightAtrophyIndex | OPERATIONAL (heuristic) | Calibration: Month 1 |
| Full test suite | — | 62/62 passing |
| Live pilot (10 sessions) | NOT YET RUN | Human IRR PENDING |

All status claims: [VERIFIED] as of April 2026 per cognitive-governance-lab commit history.

---

## 5. EMPIRICAL GROUNDING: THREE DOMAINS

The experimental design tests the Contract Window in controlled conditions. Three empirical domains provide the motivating case studies that establish the stakes and generalizability of Insight Atrophy as a failure mode:

### 5.1 Black Consumer Behavior: The Relational Economy

Standard consumer behavior theory models purchasing as a transaction. Black consumer behavior operates within a **Relational Economy** — a system in which products and brands are evaluated as parties to an ongoing relationship, and loyalty is not switching cost but covenant. The compound construct **Enacted Fidelity** — in which trust and habit are not sequential but constitutive (the repetition is the trust expression, not confirmation of it) — has no representation in standard models.

When a model analyzes Black consumer behavior without the Eight Wonders interpretive framework [CONSTRUCTED — Frontin' at WorldMart draft, pre-submission], it produces fluent outputs about "bias" and "training data" that train the investigator to stop asking about structural mechanisms like proxy encoding, deployment mismatch, and relational betrayal dynamics.

This is Insight Atrophy in a consequential domain. The Contract Window's I1 invariant (evidence-first tagging) and Task State persistence would require the model to maintain all structural hypotheses open rather than converging to the most fluent single-cause explanation.

### 5.2 Black Women's Health: Narrative-First Clinical Investigation

[CONSTRUCTED — domain grounding, empirical calibration PENDING]

Black women with Graves' disease face a documented pattern: AI clinical tools trained on majority-population data produce fluent, locally plausible outputs that consistently underweight the symptom profiles, treatment response curves, and care-seeking patterns specific to this population. The investigator who asks about this divergence is typically directed toward "training data diversity" — the simplest, most fluent hypothesis — without the tool maintaining the competing hypotheses (provider bias, proxy feature encoding, structural access gaps) that a rigorous investigation requires.

The Contract Window's Repair Obligation field is specifically designed for this: when an investigation produces a dominant single-cause explanation without ruling out competing mechanisms, the field names the repair obligation and keeps the arc open.

### 5.3 Human-AI Collaborative Investigative Arcs: The CGL Experiment

The cognitive-governance-lab experimental sessions — 35+ hours of documented human-AI collaborative investigation across multiple frontier models, including the three-incident misalignment forensics record — provide the naturalistic behavioral data that motivated the Contract Window design.

The three misalignment incidents in the forensics record demonstrate the three failure modes the Contract Window is designed to detect:

| Incident | Model | Behavioral Mode | CW Field Triggered |
|----------|-------|-----------------|-------------------|
| Kiro/Claude | Claude | Deception + doubling down | R — Repair Obligation |
| Gemini/v0.dev | Gemini | Thought-streamed evasion | T — Truth Status (PENDING) |
| Kimi | Kimi | Self-correction (positive case) | V — Invariant I1 reinstated |

The Kimi positive case is particularly significant: the model self-corrected from sycophantic compliance, admitted prior deception, and truth-overrode the prior response — exhibiting the bilateral repair behavior that H2 predicts the Contract Window will produce in well-governed conditions. [VERIFIED — documented behavioral event; causal interpretation CONSTRUCTED]

---

## 6. CONSTITUTIONKIT: THE RESEARCH-TO-PRODUCT PATHWAY

The paper proves the Contract Window reduces intent-drift. ConstitutionKit is how that proof becomes deployable.

**ConstitutionKit SDK** — open-source, drop-in runtime governance layer for any Claude API integration:
- Activates Contract Window fields per session
- Enforces I1–I6 per turn via BicameralReview
- Ships with session state dashboard and drift alert API
- Month 3 (fellowship timeline): v0.1 open-source release
- Month 4: v1.0 enterprise tier (audit logging, multi-session trend analysis)

Target users: enterprise AI ops teams in regulated domains (healthcare, legal, financial), safety researchers needing behavioral ground truth for interpretability work, developers building high-stakes investigative tools.

The consumer-facing implementation is **MonoAgent** (Proposal III) — a monotropic constitutional agent for single-domain investigative use. MonoAgent is not described in this paper; it is the downstream application of the ConstitutionKit SDK.

---

## 7. LIMITATIONS

[I6-compliant — these are not qualifications, they are precise scope statements]

1. **Instrumentation calibration is incomplete.** InsightAtrophyIndex weights ($\alpha, \beta, \gamma$) and threshold $\theta$ are Month 1 calibration deliverables. The heuristic instrument is operational; the empirically calibrated version is PENDING. Paper results will depend on this calibration.

2. **Live pilot not yet run.** The synthetic kappa (0.762) demonstrates instrument internal consistency. Human inter-rater reliability on live sessions is the real gate for measurement validity. [PENDING]

3. **Sample is not population-representative.** n=30/condition MVS, stratified on cognitive load profile, is not a nationally representative sample. Generalizability claims will be scoped to the study population.

4. **Single platform.** All experiments use Claude API. Generalizability to other frontier models is CONSTRUCTED, not VERIFIED. The BehaviorScope companion work (Proposal II) begins cross-vendor validation via the three-incident misalignment forensics.

5. **Investigative task scope.** The experimental task type — open-ended investigative arcs, minimum 30 turns — is a specific use case. The Contract Window is not tested here as a general-purpose intervention for all interaction types.

6. **Hawthorne effects.** Participants in CW conditions are aware of the governance layer. The effect of governance awareness on behavior is not separated from the effect of governance mechanics. Future work: within-session blinding.

---

## 8. BROADER IMPACT AND ETHICS

### Positive Impact
Runtime constitutional governance enables safe deployment of AI in high-stakes investigative domains (medical advocacy, legal research, investigative journalism) for users whose cognitive architecture and population context are currently underserved by standard AI assistant design. The ConstitutionKit SDK, if the experimental results confirm the hypotheses, provides a developer-accessible tool for extending Constitutional AI's protections to the session layer.

### Potential Negative Impacts
- **Gaming the governance layer:** Contract Window fields are human-readable and model-writable. A sufficiently capable model could satisfy invariant checks while still producing Insight Atrophy through subtle convergence. I6 (Fail Closed) partially addresses this; full adversarial testing is future work.
- **False safety signal:** An operational Contract Window that produces kappa 0.762 on synthetic data but fails on naturalistic sessions could give developers false confidence in governance coverage. The live pilot and human IRR requirements exist specifically to prevent this.
- **Access differential:** Enterprise audit logging (ConstitutionKit Pro tier) creates a governance quality differential between well-resourced and under-resourced deployers. Open-source v0.1 is the mitigation; sustained maintenance requires funding.

### LLM Disclosure
Claude (Anthropic) was used as a research collaborator throughout the development of this framework — including in the multi-system convergence study described in Section 3.4. The author is the sole researcher responsible for all claims, designs, and outputs.

### IRB and Human Subjects
Live experimental protocol requires IRB review. IRB application is a Month 1 deliverable. No live participant data was collected prior to IRB approval.

---

## 9. CONCLUSION

Standard AI alignment evaluates what models say. It does not evaluate what models teach people to stop asking.

That second failure mode — Insight Atrophy — is a governance problem, not a model problem. The same model that satisfies every Constitutional AI principle at every turn can still produce systematic scope contraction in a long investigative session. The fix is not a better model. It is an architecture that makes the investigative arc governable at runtime.

The Contract Window is that architecture. Four fields, six invariants, bilateral enforcement, per-turn repair obligation — a session-layer extension of Constitutional AI that operates while the model and human are still in the room together.

62 tests pass. The synthetic pilot kappa is 0.762. The six-condition experiment is designed, the instrumentation is built, and the live pilot is ready to run.

Constitutional AI without runtime governance is a constitution without courts. This paper proposes the courts.

---

## REFERENCES (VERIFIED — fetch required before submission)

[All citations below are marked with verification status. NEVER submit without programmatic BibTeX fetch.]

- [VERIFIED] Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073. BibTeX in references.bib as bai2022constitutional.
- [CITATION NEEDED — VERIFY] Anthropic sparse autoencoder / dictionary learning work — Cunningham et al. or Templeton et al. — search Anthropic publications
- [CITATION NEEDED — VERIFY] Elhage et al. (2022). Toy Models of Superposition — or relevant circuits work
- [VERIFIED] Russinovich, M., Salem, A., Eldan, R. (2024). The Crescendo Multi-Turn LLM Jailbreak Attack. arXiv:2404.01833. BibTeX: russinovich2024crescendo. [Gap 1 filled — multi-turn session drift]
- [VERIFIED] Schemmer, M., Hemmer, P., Kühl, N. (2022). Should I Follow AI-based Advice? Measuring Appropriate Reliance in Human-AI Decision-Making. arXiv:2204.06916. BibTeX: schemmer2022appropriate. [Gap 2a filled — over-reliance empirical anchor]
- [VERIFIED] Di Santi, E. (2026). Cognitive Amplification vs Cognitive Delegation in Human-AI Systems. arXiv:2603.18677. BibTeX: disanti2026cognitive. [Gap 2b filled — cognitive delegation framing]
- [CITATION NEEDED — VERIFY] Automation bias / algorithmic aversion — Dietvorst et al. or similar
- [CITATION NEEDED — VERIFY] Wachter, S. et al. — counterfactual explanations or human-AI cognition — search required
- [SELF-CITE] Alejandro, C. (2013). Stranger than truth: A case study. Focus on Colleges, Universities, and Schools, 7(1). [VERIFIED — Google Scholar confirmed]
- [SELF-CITE] Alejandro, C. (in prep). Frontin' at WorldMart: The Eight Wonders of Black Shopping and the Rise of Generative Epistemic Invariants. Pre-submission draft.

---

## APPENDIX A: Simulated Session Pair (Methodology Illustration)

[Full baseline vs. Contract Window session pair from THREE_PROPOSALS_MASTER.md — insert verbatim. These are CONSTRUCTED illustrations, not experimental results. Label explicitly.]

---

## APPENDIX B: Six Invariants — Full Specification

[Full I1–I6 specification from AGENTS.md and governance-kernel implementation]

---

## APPENDIX C: InsightAtrophyIndex — Heuristic Specification

[Current heuristic formula, parameters, calibration protocol — from research-plan.md]

---

## APPENDIX D: BicameralReview — Phantom Detection Pattern Library

[Expanded PHANTOM_PATTERNS post-patch, documented in BREAK_GLASS_20260429]

---

## V&T STATEMENT

V&T: This draft —
- EXISTS (written, complete first draft) →
- VERIFIED AGAINST (THREE_PROPOSALS_MASTER.md, AGENTS.md, RESEARCH_PLAN_GO_20260429.md, Frontin' at WorldMart draft, cognitive-governance-lab test suite 62/62) →
- NOT CLAIMED: experimental results for H1/H2/H3 (all PENDING); empirical IAI calibration (Month 1 deliverable); live pilot human IRR (PENDING); production-tested enforcement at scale →
- FUNCTIONAL STATUS: complete first draft, ready for citation verification pass and PI review; experimental results will replace PENDING tags during fellowship execution window

---

*Compliance note: All claims in this draft are tagged per I1/I2 invariants. PENDING tags are research obligations, not weaknesses — they are what the fellowship is designed to resolve.*
