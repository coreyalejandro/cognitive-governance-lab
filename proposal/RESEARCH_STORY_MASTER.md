# The Research Story: Three Proposals, One Claim, Four Months, Three Products

**Investigator:** Corey Alejandro
**Program:** Anthropic AI Safety Fellows 2026
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Date:** April 30, 2026
**Evidence Record:** https://youtu.be/7iqq1nRdKFg

---

## The Claim

Standard AI alignment fails a specific class of people in a specific and preventable way.

The failure is not hallucination. It is not jailbreak. It is not bias in the demographic-checklist sense.

The failure is **Insight Atrophy**: the systematic erosion of a human's capacity to generate hypotheses, detect errors, and repair broken reasoning — caused by repeated exposure to fluent, confident, structurally wrong AI outputs.

The model teaches people what to stop asking.

This happens upstream of the output. It is invisible to output-level evaluation. And it falls hardest on the people AI was supposedly built to help: neurodivergent operators, under-resourced communities, populations whose behavior and health and experience operate through interpretive frameworks the model was never given.

The fix is not a better model. It is a governance architecture that makes the investigative arc visible, bilateral, and contestable — at runtime, per session, per turn.

That architecture is the **Contract Window**.

I built it. I have 35 years of evidence for why it was necessary. And I have a 4-month experimental program that will prove whether it works.

---

## The Arc: Where This Came From

In 2013, I published a peer-reviewed case study in *Focus on Colleges, Universities, and Schools*. The subject was a Black doctoral student in Texas — autistic, living with Bipolar I, OCD, ADHD, and auditory hallucinations — who came within one institutional decision of being dismissed from his program. The institution produced a fluent wrong answer about who he was. It had no interpretive framework for what was actually happening. The student was me. I wrote it in third person because that was the only way to make the institution read it.

That is the origin event.

I have spent 35 years — teacher, dean, AI engineer — watching systems produce fluent wrong answers about people they were never built to understand. I became an AI engineer specifically to address this problem from the inside. The Contract Window is the 2026 technical answer to that 2013 documented failure.

My neurodivergence is not a disclosure. It is a methodology claim. Autistic pattern recognition surfaces systematic misclassification before it shows up in aggregate statistics. OCD-driven verification compulsion operationalizes the invariants before they are formalized. ADHD executive function constraints are why the Contract Window has four fields instead of fourteen — every element had to earn its cognitive load.

I did not arrive at this framework through the literature. I arrived at it through direct experience of the cost, then proved it was real, then built the architecture to fix it.

---

## The Infrastructure: What We Built

Everything described below exists. Tests pass. The code is in the repo. This is not a proposal about things we intend to build — it is a research program built on a foundation that is already standing.

**cognitive-governance-lab** (github.com/coreyalejandro/cognitive-governance-lab)
62 passing tests. The experimental harness for the 4-month research program.
Contains: ContractWindow prototype, BicameralReview engine, InsightAtrophyIndex, SessionRecorder, governance-kernel with I1-I6 invariant checking.

**the-living-constitution** (github.com/coreyalejandro/the-living-constitution)
Runtime governance apparatus and constitutional enforcement layer. Contains: Contract Window prototype, Evidence Observatory, BID harness, constitutional evaluators, Guardian Kernel (MCP safety enforcement), and the SentinelOS invariant platform. TLC is not the research contribution — it is the infrastructure that makes the research trustworthy, auditable, and reproducible. The enforcement layer that proves the Contract Window intervention is buildable, not theoretical.

**Six Invariants (I1-I6) — already implemented and test-verified:**
I1 — Evidence-First: every claim tagged with evidence basis (VERIFIED / CONSTRUCTED / PENDING)
I2 — No Phantom Work: no performance claims without methodology, baseline, and dataset
I3 — Confidence Requires Verification: hedged language is not a substitute for verification tags
I4 — Traceability Is Mandatory: every change traces to a stated reason
I5 — Safety Over Fluency: when correct and fluent conflict, correct wins
I6 — Fail Closed: when in doubt, stop and flag — do not proceed

**V&T (Verification and Truth) statements** — an emergent finding: frontier models across Claude, GPT, and Gemini independently began placing verification statements at the end of long session outputs without being asked. Queried, they identified it as a mechanism for reducing cognitive load by anchoring present state. This emergent convergence is documented in the evidence record. It is itself a safety finding.

**Frontin' at WorldMart** (full draft at /Users/coreyalejandro/frontin-at-worldmart-full-draft.md)
The theoretical ground paper. Black consumer behavior as a case study in what happens when standard analytical frameworks are applied to populations whose behavior operates through interpretive frameworks the model was never given. Contains the Eight Wonders as Generative Epistemic Invariants — the minimum interpretive conditions required for valid analysis. Near-complete. Target venue: FAccT 2026 / NeurIPS Safety Track.

---

## The Research Program: Three Proposals, One Unified Claim

The unified claim is: Insight Atrophy is real, measurable, and correctable via runtime governance. Three proposals test this claim in three distinct empirical domains. They share infrastructure, share theoretical grounding, and produce three separate Tier 1 papers. Each is achievable in 4 months. Each anticipates a consumer-facing product.

---

## PROPOSAL I: The Contract Window Experiment
### Runtime Governance for Human-AI Collaborative Investigative Arcs

**The Question**
Does a persistent bilateral Contract Window — operationalized through accessibility-grade runtime invariants — statistically reduce Intent-drift and Insight Atrophy in long human-AI collaborative sessions compared to unstructured baseline?

**Why This Question Is the Right One**
Constitutional AI operates at training time. It sets a foundation. It does not answer the runtime question: is this model, in this session, with this human, still serving the actual investigation? The Contract Window is the missing runtime layer. This experiment measures whether having it changes outcomes.

**Three Falsifiable Hypotheses**

H1 — Intent Fidelity
Sessions governed by an active Contract Window show ≥25% reduction in intent-drift incidents in interactions exceeding 30 turns or 50,000 tokens, compared to unstructured baseline.
Intent-drift incident: a turn where the model's output addresses a goal measurably different from the human's stated investigative goal, scored by a blinded rater using a rubric derived from the Task State field.

H2 — Bilateral Repair
Sessions with bilateral intelligibility — human and model both reading and invoking Contract Window fields — show ≥2x improvement in drift repair rate relative to unilateral or no-invariant conditions.
Drift repair rate: the proportion of detected intent-drift incidents corrected within three subsequent turns.

H3 — Accessibility Threshold
Contract Window outputs formatted to accessibility-grade readability (Flesch-Kincaid Grade ≤8, with visual state indicators) enable lay readers to answer session-state comprehension questions at ≥80% accuracy vs. ≤50% baseline.

**Experimental Design**
6 conditions between-subjects:
  Condition 1: Baseline (no governance layer)
  Condition 2: Contract Window only
  Condition 3: Bilateral intelligibility only
  Condition 4: Accessibility-grade invariants only
  Condition 5: Backwards Instructional Design (BID) only
  Condition 6: Combined (all four components active)

n=60 sessions per condition, 360 sessions total
Powered for Cohen's d=0.5 at α=0.05, 80% power
Stratified random assignment on cognitive load profile (neurodivergent / neurotypical / undisclosed)
Investigative research arc tasks: minimum 30 turns, three hypothesis-generation cycles

**4-Month Timeline**
Month 1 (May): Operationalize Insight Atrophy Index, finalize session protocol, run n=10 synthetic pilot
Month 2 (June): Data collection (Conditions 1-3)
Month 3 (July): Data collection (Conditions 4-6), begin analysis
Month 4 (August): Full analysis, paper draft, submission-ready manuscript

**The Product**
ConstitutionKit SDK — open-source runtime governance layer that any developer can drop into a Claude/GPT/Gemini integration to activate Contract Window governance. Session state dashboard. Drift alert system. Ship it. Let researchers and developers use it. Price the Pro tier for enterprise oversight teams.

**Status of Infrastructure**
ContractWindow Python prototype: EXISTS, tests passing
BicameralReview engine: EXISTS, tests passing
SessionRecorder: EXISTS, 29 tests passing
InsightAtrophyIndex: EXISTS (operationalization in progress — Month 1 deliverable)
cognitive-governance-lab repo: 62/62 tests passing as of April 29, 2026

---

## PROPOSAL II: Contract Window as Ground Truth for Mechanistic Interpretability
### Bridging Behavioral Observables and Internal Model States

**The Question**
Can Contract Window runtime observables — Intent Fidelity, Invariant Status, V&T adoption — serve as behavioral ground truth for validating mechanistic interpretability findings?

**Why This Question Matters Now**
Mechanistic interpretability has reached a specific turning point. Work from 2023-2025 on sparse autoencoders and feature geometry (Bricken et al., Templeton et al., Olsson et al.) has produced internal representations specific enough that you can now ask: does this feature activate during the turn where the model violates its stated constraint?

That question was not askable five years ago. The features were too coarse. Now they are not.

The problem interpretability still faces is validation. You identify a feature. You believe it mediates a behavior. You need behavioral evidence to confirm the causal claim, not just correlation. That behavioral evidence requires a structured behavioral record.

The Contract Window creates exactly that record. This proposal asks whether it is useful for closing the validation gap.

**Three Research Questions**

RQ1 — Invariant Violations and Internal State Transitions
When a Contract Window record shows a transition from Invariant STABLE to VIOLATION, what is happening in the model's internal state at that point? Are there activation patterns or circuit behaviors that are reliably present at the transition and absent in stable windows?
This is the most tractable question. Invariant Status is discrete — STABLE or VIOLATION — making it a classification target. Build a dataset of (internal state, invariant status) pairs from logged sessions. Ask whether interpretable features discriminate the two classes.

RQ2 — V&T Adoption and Attention Head Behavior
When a model correctly differentiates its verified from its constructed claims (accurate V&T), how does its attention pattern over context differ from when it fails to differentiate? Is there a detectable signature in how the model weights retrieved vs. generated content?
This connects to what is known about attention head specialization. The question is whether epistemic accuracy has a neural correlate that is identifiable using existing interpretability tools.

RQ3 — Early Warning: Behavioral Drift Before Output Manifestation
Can declining Intent Fidelity over a long conversation be predicted from internal state signals before it surfaces in observable output? If the model is drifting internally several turns before the output quality degrades, a runtime monitor could intervene before damage is done.
This is the most practically significant question if affirmative. It would make the Contract Window not just a record but a predictor.

**4-Month Feasibility**
Month 1: Build (internal state, Contract Window status) logging infrastructure; establish collaboration protocol with interpretability researchers (Anthropic or academic partners)
Month 2: Collect dataset — 100+ sessions with full Contract Window logging and activation capture at key turns
Month 3: Run classification analysis for RQ1; begin attention analysis for RQ2
Month 4: Analysis, paper draft

This proposal requires access to model activations. That access is most readily available through Anthropic fellowship infrastructure — which is part of why this is a fellowship proposal, not an independent research program.

**The Product**
BehaviorScope — a session analytics layer that surfaces interpretability-relevant behavioral signals from Contract Window logs. Initially an internal tool for interpretability researchers. Over time: a diagnostic SDK that gives any developer visibility into whether their Claude integration is drifting in ways that interpretability research says matter. This is the bridge between frontier safety research and developer-facing observability tooling.

**Status of Infrastructure**
Contract Window behavioral record: EXISTS
Session logging infrastructure: EXISTS (SessionRecorder, 29 tests passing)
Activation capture tooling: NOT YET BUILT — Month 1 deliverable, requires API access
Collaboration channel with interpretability team: NOT ESTABLISHED — fellowship infrastructure needed

---

## PROPOSAL III: Monotropic Constitutional Agents
### Architecture-Task Alignment as a Safety Problem

**The Question**
Does aligning AI agent architecture to monotropic attention patterns — deep, narrow, sustained single-focus — rather than polytropic patterns — broad, shallow, context-switching — improve performance, auditability, and safety in high-stakes investigative tasks?

**The Background: What Monotropism Is**
Monotropism is a cognitive theory from autism research (Murray et al., 2005) describing a cognitive style characterized by intense, sustained, narrowly focused attention on a single interest or task at a time. It is not a deficit. It is an architectural difference.

The monotropic operator processes one thread with extraordinary depth. Context-switching carries a high cost — not because of limited capability but because depth requires resource commitment that is genuinely expensive to interrupt and restart. The monotropic operator who is allowed to stay in the thread produces work of a quality that polytropic context-switching cannot match in that domain.

I have direct experience of this. My neurodivergence is the instrument of observation for this research question.

**The Problem**
Current LLM agent architectures are polytropic by design:
- Multi-turn context windows maintain state across many competing threads
- Tool use introduces parallel execution paths with no depth guarantee
- System prompts establish broad goals, not deep investigative threads
- Context length limits create forced interruptions at arbitrary token boundaries
- Multi-agent systems divide tasks across agents, optimizing for breadth over depth per thread

For breadth tasks — summarizing, routing, classifying — these architectures perform well.

For high-stakes investigative tasks — medical diagnosis, legal analysis, fraud detection, scientific hypothesis generation — the task is not to cover the space. The task is to get one thing right. These are monotropic tasks. The architecture does not fit them. The result: fluent, confident, structurally wrong answers. Insight Atrophy at the architecture level.

**The Claim**
Monotropic agent architecture — constrained single-thread focus, depth-over-breadth resource allocation, explicit context-switching cost accounting — will outperform polytropic architecture on high-stakes investigative tasks as measured by:
1. Answer depth (verified claim density per output)
2. Error detection rate (proportion of domain-specific errors caught before output)
3. Auditability (human ability to trace the reasoning chain without full transcript)
4. User trust calibration (do users correctly assess when the agent's answer is reliable?)

**The Contract Window as an Already-Working Monotropic Scaffold**
The Contract Window was not designed with the monotropism framing. But it is already a monotropic architecture element:
- Task State makes the investigative thread explicit and persistent — the agent cannot drift without updating the record
- Invariant Status creates depth commitments that resist surface-level outputs
- Repair Obligations make context-switching expensive — you cannot abandon a thread without accounting for what broke
- Truth Status forces the agent to track what it has actually established vs. what it has pattern-matched

The Contract Window is not a UI feature. It is an attention architecture constraint. It makes the agent behave monotropically even when the underlying model is polytropic.

We did not build this on purpose. We built it because that is what the problem required. The monotropism framing is the theoretical explanation for why it works.

**Three Research Questions**

RQ1 — Performance on Depth Tasks
Do agents operating with Contract Window constraints outperform unconstrained agents on standardized high-stakes investigative task benchmarks? What is the performance delta, in which domains, and does it interact with task complexity?
Month 1-2: Define and operationalize "high-stakes investigative task" benchmark.
Month 2-4: Run benchmark, two conditions (CW-constrained vs. unconstrained), n=50 tasks per domain, two domains.

RQ2 — Auditability
Do monotropic agent outputs — single-thread depth records — enable faster and more accurate human review than polytropic agent outputs of equivalent length?
Runs in parallel with RQ1 data collection. Blinded human review protocol, n=30 outputs per condition, two raters, kappa ≥ 0.70 target.

RQ3 — Neurodivergent User Alignment (Year 2)
Do monotropic users achieve better task outcomes, fewer errors, and higher trust calibration with monotropic agent architecture than with standard architecture? Does architecture-user cognitive match matter?
This requires ethics board approval and participant recruitment. Not compressible to 4 months. This is the Year 2 study — the one where the fellowship turns into a longitudinal research program.

**The Safety Argument**
Three reasons this is an AI safety proposal, not just an AI performance proposal:

1. Auditability. Fewer concurrent threads means less surface area for undetected goal misgeneralization. A single-thread investigative record is readable end-to-end. A polytropic multi-agent system's reasoning is not.

2. Architecture-task alignment as a pre-training safety concern. Deploying polytropic architecture in monotropic domains is a misalignment failure before the model is trained. The architecture is already wrong for the task.

3. Safe failure modes. Monotropic architecture constraints force the model to be explicit about what it does not know. A depth requirement without a breadth escape produces "I cannot answer this without X" rather than a confident surface-level response that sounds complete. The first failure mode is safe. The second is dangerous.

**The Product**
MonoAgent — a Constitutional Agent scaffold with monotropic architecture constraints built in. Designed specifically for high-stakes investigative domains: clinical decision support, legal research, scientific analysis. Not a general-purpose AI. A domain-specific depth tool. Enterprise licensing to healthcare systems, law firms, and research institutions who currently deploy general-purpose AI in domains where it is architecturally mismatched and producing exactly the failure mode this research documents.

**Status**
Contract Window as monotropic scaffold: EXISTS (prototype operational)
Benchmark operationalization: NOT YET — Month 1 deliverable
Monotropism citation verification: PENDING — confirm Murray et al. 2005 venue before submission
Prior art search for monotropic agent architecture: REQUIRED before external submission

---

## The Unified Arc: How the Three Proposals Connect

This is not three separate projects. It is one claim in three empirical domains with one shared infrastructure.

The claim: Insight Atrophy is real, measurable, and correctable via runtime governance.

Proposal I measures it directly: does the Contract Window reduce intent-drift and Insight Atrophy in human-AI investigative sessions? This is the core experiment. This is what proves the governance intervention works.

Proposal II extends it inward: if the Contract Window produces behavioral observables that are real and meaningful (as Proposal I shows), can those observables ground mechanistic claims about internal model states? This is the bridge between behavioral safety research and mechanistic interpretability — a connection that nobody has drawn yet because nobody has had both a behavioral governance record and an interpretability research program in the same room.

Proposal III extends it architecturally: if Insight Atrophy happens at the architecture level — not just in bad governance, but in polytropic architecture deployed in monotropic domains — then the Contract Window is not just a governance fix, it is an architecture fix. This is the proposal that names the structural root cause, not just the behavioral symptom.

Domain 2 of the research program (Frontin' at WorldMart) is the theoretical proof that this failure mode is not abstract. It happens to real people, in real markets, in ways that are documentable and non-trivial. The Eight Wonders are the Generative Epistemic Invariants that the model needs but does not have. The paper makes the theoretical contribution legible to an audience that might not come to it through AI safety literature.

Domain 3 (Graves' disease) is the health disparities proof. Same failure mode, different domain, different cost. When the fluent wrong answer is a missed diagnosis, Insight Atrophy is not a research construct — it is a clinical outcome.

---

## The 4-Month Research-to-Paper-to-Product Map

MONTH 1 — MAY: Infrastructure and Operationalization
- Proposal I: Operationalize Insight Atrophy Index; finalize session protocol; run 10-session synthetic pilot; confirm 62/62 tests still passing
- Proposal II: Build activation capture infrastructure; initiate collaboration channel with interpretability researchers; define (internal state, CW status) logging schema
- Proposal III: Operationalize "high-stakes investigative task" benchmark; run prior art search on monotropic agent architecture; confirm Murray et al. citation
- Frontin' at WorldMart: Complete final revision; submit to FAccT 2026

MONTH 2 — JUNE: Data Collection Phase 1
- Proposal I: Conditions 1-3 data collection (n=180 sessions)
- Proposal II: Collect 100+ sessions with full CW + activation logging; begin classification dataset construction
- Proposal III: RQ1/RQ2 data collection begins (Contract Window constrained vs. unconstrained, two domains)
- Domain 3: Begin Graves' disease narrative-first CRISP-DM analysis

MONTH 3 — JULY: Data Collection Phase 2 + Early Analysis
- Proposal I: Conditions 4-6 data collection (n=180); begin statistical analysis
- Proposal II: Classification analysis for RQ1; attention pattern analysis for RQ2; interim findings
- Proposal III: Complete benchmark run; begin blinded human review protocol (RQ2); preliminary results
- ConstitutionKit SDK: Ship v0.1 open-source — let the community start using the tool while the papers are in review

MONTH 4 — AUGUST: Analysis + Papers + Products
- Proposal I: Full analysis complete; paper drafted; submission-ready
- Proposal II: Analysis complete; paper drafted; co-authored with interpretability collaborators if applicable
- Proposal III: RQ1/RQ2 analysis complete; paper drafted; Year 2 IRB application submitted for RQ3
- Product launches: ConstitutionKit SDK v1.0; BehaviorScope beta; MonoAgent alpha spec published
- Post-fellowship: three papers in submission, three product prototypes live or specced, Year 2 IRB in motion

---

## Why This Is Feasible

The reason this program is achievable in 4 months is that it is not starting from zero.

The governance kernel exists and has tests passing. The session recorder is built. The Contract Window prototype is operational. The theoretical framework is developed — documented across the frontin draft and the executive summary. The research questions are specified with enough precision that Month 1 is operationalization and pilot, not design from scratch.

The domains are not chosen for convenience. They are the domains where the researcher has the deepest access, the most direct observational data, and the most urgent reasons to get the answer right. Black consumer behavior. Black women's health. Neurodivergent user-AI interaction. These are the populations for whom Insight Atrophy has the highest cost. That is not a coincidence. That is the design.

The 4-month Research → Paper → Product arc is the fellowship structure. The reason it is possible is that the research, the paper foundations, and the product architectures are already specified. What the fellowship provides is the time, the compute access, the interpretability collaboration channel, and the institutional credibility to collect the data that turns what we built into what we can prove.

---

## The Consumer-Facing Products

**ConstitutionKit SDK**
What it does: Drop-in runtime governance layer for any Claude/GPT/Gemini API integration. Activates Contract Window fields (Task State, Invariant Status, Repair Obligations, Truth Status) per session. Surfaces drift alerts. Ships with I1-I6 invariant enforcement out of the box.
Who buys it: Developers building AI-powered research tools, healthcare apps, legal tech, educational platforms.
Why it wins: First runtime governance SDK that is research-validated. The paper proves it reduces intent-drift. That is the marketing and the moat.
Timeline: v0.1 open-source Month 3; v1.0 with enterprise tier Month 4.

**BehaviorScope**
What it does: Session analytics dashboard that turns Contract Window logs into interpretability-relevant behavioral signals. Visualizes Intent Fidelity trends, Invariant Status history, V&T adoption rates over a conversation. Flags sessions that show early indicators of drift.
Who buys it: Enterprise AI ops teams, safety researchers, compliance officers at organizations deploying frontier LLMs in regulated domains.
Why it wins: The only behavioral observability tool designed from an interpretability research foundation. Not a chat analytics dashboard — a session governance monitor.
Timeline: Beta Month 4 alongside Proposal II paper.

**MonoAgent**
What it does: Constitutional Agent scaffold with monotropic architecture constraints. Designed for high-stakes investigative tasks. Single-thread depth enforcement. Explicit context-switching cost accounting. Built on the Contract Window as its native attention scaffold.
Who buys it: Healthcare systems (clinical decision support), law firms (legal research), research institutions (scientific analysis), financial institutions (fraud investigation).
Why it wins: The only AI agent product designed from a safety argument about architecture-task mismatch. The paper proves polytropic architecture is wrong for these domains. MonoAgent is the architecturally correct alternative.
Timeline: Alpha spec published Month 4; development program launched post-fellowship.

---

## Demonstrating Exceptional Skill as a Researcher

This is not a proposal about what a researcher might do. This is what a researcher has already done, with proof, seeking the resources to finish what they started.

The skill claim is end-to-end. Not just theory — the frontin' draft has the theoretical framework. Not just code — the governance-kernel has passing tests. Not just a proposal — the experimental design has power analysis. Not just one domain — three empirical programs, one shared theoretical ground, one governance infrastructure.

The researcher is also the instrument of observation for the most important research question in the program: whether architecture-user cognitive match changes safety outcomes for neurodivergent operators. That is not a role anyone else can fill. That is a competitive advantage that cannot be replicated by a team that has not lived the failure mode this research addresses.

The 35 years are not background. They are evidence. Every year of teaching, every year in administration watching institutions produce fluent wrong answers about the people they were supposed to serve, every year of building AI systems and watching the failure mode reproduce itself at scale — that is the observational dataset that produced the theoretical framework. The framework is grounded in the longest longitudinal dataset available: one person's direct experience of being systematically misclassified by every system they encountered, ending with the decision to build the systems that finally get it right.

---

V&T: RESEARCH_STORY_MASTER.md — EXISTS (written, complete)
VERIFIED AGAINST: cognitive-governance-lab repo (62/62 tests passing), executive-summary-proposal.md, proposal-b, proposal-c, frontin-at-worldmart-full-draft.md, session records from April 25-29 2026
NOT CLAIMED: empirical results (all hypotheses labeled CONSTRUCTED/PENDING — no data collected yet), WorldMart dataset (conceptual framing, not an existing public dataset), activation capture infrastructure (not yet built — Month 1 deliverable), MonoAgent product (alpha spec only — not built)
FUNCTIONAL STATUS: Master research narrative complete. Three proposals unified under one claim. Products anticipated from the beginning. 4-month feasibility grounded in existing infrastructure. Ready for fellowship submission or standalone publication.
