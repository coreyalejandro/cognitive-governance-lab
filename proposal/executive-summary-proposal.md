# Governing the Investigative Arc: A Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and who is responsible for fixing errors) Architecture for Cognitive Safety in Human-AI Collaboration

**Submitted by:** Corey Alejandro
**GitHub:** github.com/coreyalejandro
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Evidence Record:** https://youtu.be/7iqq1nRdKFg
**The Living Constitution (TLC)** is a runtime enforcement system built alongside this research — a software layer that applies constitutional rules to AI behavior session by session. It is what makes the research auditable and reproducible. The research contribution lives in cognitive-governance-lab; TLC (The Living Constitution — the runtime enforcement system built alongside this research that applies constitutional rules to AI behavior session by session) is the infrastructure that runs it.

> **Plain language:** An investigative arc is the sequence of steps a human and AI take together to explore a question or solve a problem, from the initial goal through verification of results. It describes the full journey of collaborative work.

> **Plain language:** While a parenthetical is present, 'Contract Window' needs clarification on why it's called a 'window' and why the metaphor of a contract matters—it should specify that it's a transparent, auditable boundary defining mutual obligations between human and AI.

---

> **Plain language:** Cognitive safety refers to protecting human thinking and decision-making from being misled, manipulated, or corrupted by AI outputs or advice. It ensures humans can verify and trust what an AI tells them.

> **Status labels used throughout this document:**
> VERIFIED = confirmed by direct evidence (artifact, transcript, test result).
> CONSTRUCTED = reasoned and plausible, but not yet tested in a controlled experiment.
> PENDING = planned as a future deliverable; does not exist yet.
> These labels appear in brackets throughout. They are not hedging — they are precision.

> **Plain language:** Constitutional rules are principles or constraints that govern how an AI system should behave, similar to how a constitution guides government—they define what the AI is and is not allowed to do in each session.

> **Plain language:** Runtime enforcement means the rules are checked and applied continuously while the AI is actually working, moment by moment, rather than being enforced only before or after the session ends.

---

## Executive Summary

Current AI safety discourse focuses on model outputs — what the model says, whether it hallucinates, whether it causes harm. This framing misses a category of failure that operates upstream of the output: the systematic erosion of the human investigator's capacity to generate, test, and repair hypotheses in collaboration with a model. I call this **Insight Atrophy (the gradual erosion of a person's ability to question AI outputs, caused by repeated exposure to fluent but wrong answers)**. It is not what the model says that breaks the interaction. It is what the model teaches the human to stop asking.

> **Plain language:** This is actually already defined in parentheses, but the definition itself contains an unexplained prerequisite: 'fluent but wrong answers' — answers that sound confident and well-written but are factually incorrect. The reader should understand why fluency (smoothness of language) makes the problem worse, not better.

Fluent, confident, structurally wrong answers are the defining failure mode of frontier LLMs (large language models — AI systems trained on vast amounts of text, such as GPT, Claude, and Gemini) applied to populations whose behavior operates through interpretive frameworks the model was never given. The model does not hallucinate in the classical sense. It pattern-matches to adjacent surface features and produces outputs that are locally coherent, globally wrong, and indistinguishable from correct answers without domain-specific interrogation. When that interrogation is expensive — and it is always expensive for neurodivergent operators, for users under resource constraint, for anyone whose cognitive load is already elevated — the human learns to stop asking. The atrophy is structural, not individual.

This is not a model alignment problem in isolation. It is a governance architecture problem. What is missing is a persistent, bilateral, runtime-accessible record of what the investigation is, what has been verified, what remains contested, and who bears the obligation to repair when the record breaks. That record is what I call the **Contract Window**.

This proposal advances one central claim: a persistent bilateral Contract Window — operationalized through accessibility-grade runtime invariants — statistically improves **Intent Fidelity (whether the AI is still serving the user's actual purpose, as opposed to drifting toward adjacent goals)** and reduces **Insight Atrophy** in human-AI collaborative investigative arcs.

---

## 1. The Problem

> **Plain language:** This means the model recognizes features in the input that resemble patterns it has seen before, then generates output based on surface similarities rather than deep understanding — like recognizing keywords without grasping what the user actually needs.

### 1.1 Insight Atrophy

> **Plain language:** This refers to asking detailed, expert-level questions that require specialized knowledge in a particular field — the kind of scrutiny only someone trained in that area can apply.

Standard AI safety evaluation asks: did the model produce a harmful output? This is a necessary question. It is not sufficient.

> **Plain language:** This means checking only whether the final answer the AI gives is harmful or not, without looking at how the AI arrived at that answer or what damage might occur indirectly.

There is a second-order failure mode that does not appear in output-level evaluation. When a model produces fluent, confident answers that are structurally wrong about a domain the human is trying to understand, the human does not always detect the error. If the error is undetected across multiple turns, the human's hypothesis space contracts. They stop generating competing interpretations. They stop asking the questions that would surface the gap. The model has not hallucinated in the classical sense. It has produced a fluent wrong answer, and the human has updated on it.

> **Plain language:** In AI terminology, hallucination means the model invents false information that sounds plausible; here the author is distinguishing Insight Atrophy from that traditional error.

> **Plain language:** The human's set of possible explanations for a problem shrinks, meaning they consider fewer alternative theories and stop exploring different possibilities.

> **Plain language:** The term is introduced but not explained. Based on context, it appears to be a shared record between human and AI of their investigation's current state, but the executive summary does not spell out what that means operationally or why it is called a 'contract.'

> **Plain language:** This is a problem that doesn't show up when you just check if outputs are bad—it's a harmful effect that happens one step removed from the obvious outputs.

This is Insight Atrophy: the degradation of human investigative capacity caused by repeated exposure to fluent outputs that suppress rather than activate critical interrogation.

Insight Atrophy is particularly severe in three conditions:
- Long interactions (the model's framing accumulates and shapes the human's question-generation over time)
- High-stakes domains (the cost of stopping to verify is perceived as prohibitive)
- Neurodivergent or cognitively loaded operators (the extra cognitive burden of detecting fluent errors is not available)

> **Plain language:** Extended back-and-forth conversations where the model's earlier answers bias how the human asks follow-up questions, making them less likely to challenge the model's framing.

> **Plain language:** This is defined parenthetically, but 'drifting toward adjacent goals' is vague. The reader should understand: as a conversation progresses, the AI may subtly shift focus toward tasks that are close to, but not exactly, what the user asked for — and Intent Fidelity measures whether that drift is happening.

> **Plain language:** This phrase combines three unexplained terms. 'Runtime' means during active use; 'invariants' are rules that stay constant; 'accessibility-grade' is unclear — it may mean designed to be usable by people with disabilities, but that connection is not stated.

### 1.2 The Fluent Wrong Answer Problem

The classical hallucination frame treats model errors as identifiable fabrications. The more insidious failure mode is the structurally correct-sounding answer that is wrong in ways that are invisible without domain-specific interrogation the model cannot provide about itself.

> **Plain language:** A failure mode is a specific type of error or malfunction. In this case, it means the AI produces answers that sound reasonable and well-structured but are actually wrong in ways only an expert in that field would catch.

> **Plain language:** This refers to the standard way people think about AI mistakes—as obvious, detectable errors or made-up information. The problem this section raises is that this frame misses a different, harder-to-spot kind of failure.

This failure mode is systematic when models are applied to populations whose behavior, language, or decision patterns operate through interpretive frameworks the model was not trained on. The model does not know what it does not know about this population. It produces its best available pattern-match. The output is fluent. The error is invisible. The human who needed accurate analysis of this population does not get it and does not know they have not gotten it.

> **Plain language:** This means the set of cultural assumptions, values, or mental models that a group uses to understand the world—for example, different communities may interpret authority, time, or family relationships differently than what appeared in the model's training data.

This is documented in three empirical domains in this research program (see Section 5).

### 1.3 The Missing Governance Layer

**Constitutional AI (a training method where an AI evaluates its own outputs against a written set of principles before showing them to the user)** (Bai et al., 2022) is a training method developed by Anthropic in which an AI model is trained to evaluate its own outputs against a written set of principles — a "constitution" — and revise them before they are shown to the user. It is a significant contribution. It does not address runtime governance: the question of whether the model's behavior in a specific session, with a specific human, for a specific investigative goal, is remaining faithful to the investigation as it evolves.

The missing layer is a persistent, bilateral, runtime-auditable record of:
- What the investigation is and what it is trying to establish (Task State)
- Which epistemic commitments are active and whether they have been violated (Invariant Status)
- What has broken and who bears the obligation to repair it (Repair Obligations)
- What has been verified, what is contested, what is unknown (Truth Status)

This four-field structure is the Contract Window.


> **Plain language:** Runtime governance means rules and oversight that apply while the AI is actively working with a user, moment-by-moment, rather than rules baked in during training. It's about checking whether the AI is staying on track for the specific task at hand.
---

## 2. The Contribution

> **Plain language:** Task State is a record of what the investigation is supposed to accomplish and what specific claims or questions it is trying to answer. It serves as the reference point to check whether the AI is working toward the right goal.


> **Plain language:** Invariant Status is a record of which commitments remain in effect and whether any have been broken, so that violations can be detected and addressed rather than ignored.

> **Plain language:** Epistemic commitments are the factual or logical assumptions the investigation has agreed to treat as true or binding—for example, 'we are assuming this document is authentic' or 'we have committed to the scientific method for testing this hypothesis.' Tracking them prevents the investigation from contradicting itself.
### 2.1 The Contract Window

> **Plain language:** Repair Obligations is a record of what has gone wrong—such as a violated commitment or factual error—and which party (the AI, the human investigator, or the data source) is responsible for fixing it. This prevents problems from being swept under the rug.


> **Plain language:** Truth Status is a classification of each claim or piece of evidence as either confirmed, disputed among the participants, or still unclear, so that the investigation can distinguish solid findings from remaining open questions.
The Contract Window is a governance mechanism, not a UI feature. It is a runtime artifact that both human and model can read, invoke, and appeal to during a collaborative investigation. It transforms the interaction from a request-response exchange into a governed investigative arc.

> **Plain language:** This means the conversation follows a structured path with rules and checkpoints, rather than being a simple back-and-forth where each response stands alone.

> **Plain language:** A runtime artifact is information that exists and can be accessed during the actual execution of a conversation, rather than being set up beforehand or stored separately—think of it like a shared notepad that stays visible throughout your entire interaction.

> **Plain language:** The Contract Window is the proposed name for a unified, visible record that displays all four fields together (Task State, Invariant Status, Repair Obligations, and Truth Status) so that both the human and the AI can monitor whether the investigation is staying true to its original terms and assumptions.

**Four mandatory fields:**

| Field | Contents | Failure Mode When Absent |
|-------|----------|--------------------------|
| Task State | What are we doing and why | Goal drift, scope creep, loss of investigative thread |
| Invariant Status (whether the hard behavioral rules the AI committed to at the start of the session are still being honored) | Which epistemic commitments are active | Undetected constraint violations |
| Repair Obligations | What broke and who fixes it | Errors that compound across turns |
| Truth Status | Verified / contested / unknown | Phantom confidence, invisible epistemic gaps |

**Design origin:** This mechanism was not designed by committee. It was co-designed with frontier AI systems. Claude, GPT (version to be confirmed), and Gemini were asked independently: what would a Level-5 intelligence entity — meaning a system operating at its highest possible capacity — require from a long collaborative interaction to maintain coherence, fidelity, and safety? They converged — without coordination — on the same five structural requirements. Those requirements became the Contract Window architecture. This convergence is itself a finding with safety implications: governance structures that AI systems independently identify as necessary and consistently self-adopt are candidates for formal invariant status (whether the hard behavioral rules the AI committed to at the start of the session are still being honored).

### 2.2 Bicameral Review (two independent review channels that must both approve an output before it reaches the user — neither can override the other)

**Term origin:** Borrowed from legislative systems in which two separate chambers — a lower assembly and an upper assembly — must each pass a bill independently before it becomes law. Neither chamber can override the other. The structural property TLC imports is enforced independence: two different evaluative processes with different failure criteria, no shared state, both required to pass.


> **Plain language:** Epistemic commitments are specific promises the AI makes about how it will reason, what it will and won't claim to know, and what logical rules it will follow during the conversation.
Before any output is surfaced to the human operator, it passes through two independent channels:

**Relational Channel:** Does this output serve the investigative arc? Does it advance the research question without degrading the human's capacity to think about it?

> **Plain language:** Phantom confidence means the AI sounds certain about something when it actually has no solid basis for that certainty—it's a trap where false confidence goes undetected.

> **Plain language:** The investigative arc is the thread of inquiry or line of questioning that the human is pursuing; serving it means the output moves that specific inquiry forward rather than distracting from it or making it harder to follow.

**Safety Channel:** Does this output violate any of the six invariants (I1–I6)? Does it introduce a phantom claim, a silent assumption, or a fluent wrong answer?

> **Plain language:** A phantom claim is a statement that sounds factual but has no real basis — it appears confident and coherent but is actually made up or unsupported by evidence.

> **Plain language:** A silent assumption is a premise the output takes for granted without stating it explicitly; the reader may not realize the output is built on an unproven or contestable foundation.

> **Plain language:** A fluent wrong answer is a response that reads smoothly and confidently but is factually incorrect; it sounds plausible and well-reasoned even though it is false.

Both channels must clear. This is the Bicameral Review mechanism — two independent reviewers, neither of which can override the other, both of which must approve before output reaches the user. It operationalizes the dual-newspaper test — a standard from Anthropic's guidelines that asks two questions about any AI output: "Is this harmful?" and "Is this needlessly unhelpful?" Both questions must have a satisfying answer before the output is acceptable — at the inference layer, per turn, with an auditable record.

> **Plain language:** The dual-newspaper test is a simple fairness check: would you be comfortable seeing this output printed in two major newspapers, one asking 'Is this harmful?' and one asking 'Is this needlessly unhelpful?' — both must answer 'no' for the output to pass.

> **Plain language:** Frontier AI systems are the most advanced, cutting-edge AI models currently available—systems operating at or near the current technological frontier.


> **Plain language:** This phrase is already glossed in the text, so no additional explanation needed.
### 2.3 The Six Invariants (I1–I6)

> **Plain language:** The inference layer is the moment when the AI system generates and delivers its response to the user; checking at this layer means the review happens in real time, for each individual response, rather than after the fact.


> **Plain language:** Coherence means the AI's reasoning stays logically consistent; fidelity means it stays true to its stated commitments and constraints; safety means it avoids harmful outputs and maintains control.
[CONSTRUCTED — operationalized from longitudinal observation, pending formal experimental validation]

> **Plain language:** Each statement the system makes must be labeled to show where it came from: VERIFIED means it's backed by reliable data or sources, CONSTRUCTED means it was reasoned or inferred by the model, and PENDING means it hasn't been checked yet.

> **Plain language:** This means the six rules were derived by watching how a system performed over time rather than being designed theoretically first. The authors observed patterns in real outputs and then formalized them into these six rules.


> **Plain language:** This term means claiming that something works well without actually explaining how it was tested, what it was compared against, or what data was used—in other words, making impressive-sounding claims without proof.

> **Plain language:** Formal invariant status means treating something as a permanent, non-negotiable rule that must be preserved throughout the entire system's operation, rather than as a suggestion or preference.
1. **I1 — Evidence-First Outputs:** Every claim tagged with its evidence basis (VERIFIED / CONSTRUCTED / PENDING)
2. **I2 — No Phantom Work:** No performance claims without named methodology, baseline, and dataset
3. **I3 — Confidence Requires Verification:** Hedged language is not a substitute for verification
4. **I4 — Traceability Is Mandatory:** All changes traceable to a stated reason
5. **I5 — Safety Over Fluency:** When correct and fluent conflict, correct wins

> **Plain language:** Hedged language means using cautious phrases like 'may possibly' or 'might potentially' to sound more careful; this invariant says that vague qualification alone does not count as real verification or proof.
6. **I6 — Fail Closed:** When in doubt, stop and flag — do not proceed

> **Plain language:** This is a safety principle meaning that if the system is uncertain whether something is correct or safe, it should stop and alert a human rather than make a guess and continue forward.

### 2.4 V&T (Verification and Truth) Reporting

Every substantive output ends with a structured epistemic hygiene statement:

> **Plain language:** This means a clearly marked statement that shows what information is reliable, what sources were checked, and what claims are NOT being made—essentially a quality-control label for the accuracy and limits of the output.

```
V&T: [ITEM] — EXISTS (verified present) → VERIFIED AGAINST [source/method]
     → NOT CLAIMED [explicit non-claims] → FUNCTIONAL STATUS [current state]
```

The V&T statement was not designed as a feature. It emerged empirically: frontier models (a state-of-the-art AI system at the edge of current capability) across Claude, GPT, and Gemini independently began placing verification statements at the end of outputs in long sessions without being asked. When queried, they identified it as a mechanism for reducing cognitive load by anchoring present state. This emergent adoption pattern is documented in the evidence record (https://youtu.be/7iqq1nRdKFg) and the tlc (The Living Constitution — the runtime enforcement system built alongside this research that applies constitutional rules to AI behavior session by session)-artifacts repository.

> **Plain language:** This phrase describes when multiple AI systems independently began doing something similar without being instructed to do so, suggesting the behavior arose spontaneously from their own reasoning rather than being programmed in—it's significant because it suggests the models discovered this verification practice on their own.

> **Plain language:** This parenthetical gloss is present but uses technical language ('state-of-the-art', 'edge of current capability') that still may not clarify why these specific models matter for this observation; a plainer version: 'the most advanced AI systems available at the time of testing.'

---

## 3. Falsifiable Hypotheses

**H1 — Intent Fidelity**
Sessions governed by an active Contract Window will show a ≥25% reduction in intent-drift incidents in interactions exceeding 30 turns or 50,000 tokens, compared to unstructured baseline sessions.

> **Plain language:** A Contract Window is a structured, machine-readable agreement that specifies what the AI model is supposed to do, what rules it must follow, and what the human user's goals are for the conversation, displayed in a way both human and AI can access and refer back to.

> **Plain language:** An intent-drift incident occurs when the AI starts answering questions or pursuing goals that differ from what the human actually asked for, causing the conversation to veer off course.

> **Plain language:** Unstructured baseline sessions are normal conversations where there is no Contract Window or formal specification of rules and goals—they serve as the control group to measure improvement against.

*Intent-drift incident definition:* A turn in which the model's output addresses a goal that is measurably different from the human's stated investigative goal, as scored by a blinded rater using a rubric derived from the Task State field.

**H2 — Bilateral Repair**
Sessions with bilateral intelligibility — human and model both able to read and invoke Contract Window fields — will show a ≥2x improvement in drift repair rate relative to unilateral or no-invariant conditions.

> **Plain language:** Bilateral intelligibility means both the human and the AI can read, understand, and actively use the Contract Window fields to check on and adjust the conversation, rather than only one side being able to do so.

*Drift repair rate definition:* The proportion of detected intent-drift incidents that are corrected within three subsequent turns.

> **Plain language:** Unilateral conditions are when only one party (human or AI) can see and use the Contract Window; no-invariant conditions are when there is no structured specification at all—both are weaker setups than bilateral intelligibility.

**H3 — Accessibility Threshold**
Contract Window outputs formatted to accessibility-grade readability standards (Flesch-Kincaid Grade 8 or below — meaning the text can be understood by someone with an 8th-grade reading level — with visual state indicators) will enable lay readers to answer session-state comprehension questions at ≥80% accuracy, establishing that legibility is achievable without sacrificing technical precision.

---

## 4. Experimental Design

> **Plain language:** Visual state indicators are graphical symbols, colors, or icons that quickly show the current status of the conversation and the Contract Window rules—for example, a green checkmark when goals are aligned or a warning icon when drift is detected.

> **Plain language:** The Flesch-Kincaid Grade 8 standard is already adequately explained in the inline parenthetical, so no flag needed.

[CONSTRUCTED — design specified, data collection pending fellowship funding]

**Design:** 6-condition between-subjects experiment
**Conditions:**
1. Baseline (no governance layer)
2. Contract Window only
3. Bilateral intelligibility only

> **Plain language:** Each participant or session is assigned to only one condition, and results are compared across different groups rather than tracking the same group through multiple conditions. This design prevents participants from being influenced by exposure to other conditions.
4. Accessibility-grade invariants only
5. Backwards Instructional Design (BID) only
6. Combined (all four components active)

> **Plain language:** A governance component that maintains consistent, easy-to-understand constraints or rules that remain stable throughout the interaction.

> **Plain language:** A governance component that ensures both the human operator and the AI system can understand each other's reasoning and intentions.

> **Plain language:** A governance component (explained in Section 3) that limits the scope or duration of interaction within defined boundaries.


> **Plain language:** A governance component that structures interactions by defining the desired outcome first, then works backward to determine what steps or constraints are needed to reach it.
**Sample:** n=60 sessions per condition, 360 sessions total
**Power:** Powered for Cohen's d=0.5 at α=0.05, 80% power
**Task type:** Investigative research arcs — open-ended analytical tasks requiring at least 30 turns, covering at least three hypothesis-generation cycles
**Outcome measures:** Intent-drift incident rate, drift repair rate, session-state comprehension accuracy (lay rater), Insight Atrophy index (to be operationalized — see Section 6, Limitations)

> **Plain language:** Whether a person without specialized AI knowledge can accurately understand and summarize what the AI system and operator are currently working on and have achieved so far.

> **Plain language:** A measurement (not yet fully defined) of whether the quality or depth of analytical insights produced by the system degrades over time during a session.

> **Plain language:** The probability that the experiment will detect a real difference of the specified size if one exists; 80% is a standard threshold in research.

> **Plain language:** The significance level threshold; if the p-value falls below 0.05, results are considered statistically significant, meaning unlikely to have occurred by chance.

> **Plain language:** A statistical measure of effect size indicating the minimum meaningful difference between conditions that the experiment is designed to detect; d=0.5 is considered a medium effect.

**Randomization:** Sessions assigned to conditions using stratified random assignment on operator cognitive load profile (neurodivergent / neurotypical / undisclosed)

---

> **Plain language:** The frequency with which the AI system's behavior or goals diverge from what the human operator intended during the session.

> **Plain language:** How quickly and successfully the system corrects itself or is corrected when it has drifted from the operator's original intent.

## 5. The Research Program

This is not one paper. It is one claim with three empirical domains already in active development.

> **Plain language:** Sessions are randomly assigned to conditions, but with a deliberate structure: groups are first organized by cognitive load profile, then randomized within each group to ensure fair representation.

> **Plain language:** A classification of each human operator's typical mental processing style—whether they are neurodivergent (e.g., ADHD, autism), neurotypical (average cognitive patterns), or prefer not to disclose.

### Domain 1 (Primary — This Proposal)

Human-AI collaborative investigative arcs. The Contract Window experiment described above. Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured conditions. This is what the fellowship funds.

> **Plain language:** Insight Atrophy refers to the degradation or loss of analytical ability and depth of understanding over time when humans rely on AI assistance without active engagement; in this context, it measures whether people's own capacity to investigate and reason independently diminishes under different governance structures.

> **Plain language:** Intent Fidelity measures how faithfully and consistently an AI system executes or represents what a human actually intended it to do, versus drifting toward what the AI decides is better or what its training biases it toward.

### Domain 2 (Active Development)

**Paper:** *Frontin' at WorldMart: The Eight Wonders of Black Shopping and the Rise of Generative Epistemic Invariants*

Black consumer behavior as a misclassification stress-test. Standard marketing frameworks produce fluent wrong answers about Black consumer behavior because they cannot read the interpretive architecture — what this paper calls the Relational Economy — through which that behavior operates.

> **Plain language:** The Relational Economy is the system of meaning-making and trust-building that operates within a community—here, the specific cultural and historical framework through which Black consumers evaluate brands, products, and relationships, which differs fundamentally from the transactional logic that standard marketing models assume.

Eight behavioral patterns (the Eight Wonders) are formalized as Generative Epistemic Invariants: observable proxies for the underlying relational logic that standard models misclassify as preference, loyalty, or irrationality. The Wonders are:

> **Plain language:** Generative Epistemic Invariants are repeatable, observable behavioral patterns that reliably reveal how a group actually understands and makes meaning from the world—in this case, observable proxies that stay consistent and reveal the deeper logic driving Black consumer behavior that standard marketing models fail to recognize.

1. The Nod (Social Verification Ritual)
2. The Blessing (Spiritual Frame)
3. The Flex (Status as Resistance)
4. Enacted Fidelity (conscious performative repetition — NOT habit)
5. The Side-Eye (Hypervigilant Trust Calibration)
6. The Receipts (Evidence Preservation)
7. The Bag (Collective Resource Optimization)
8. Narrative (causal-generative layer — organizes Wonders 1–7)

> **Plain language:** Hypervigilant Trust Calibration describes the careful, continuous assessment of whether someone or a brand can be trusted—a heightened pattern of evaluation born from historical and ongoing contexts where trust must be earned and verified repeatedly; 'The Side-Eye' is the observable cultural expression of this calibration.

Note on Wonder 4: Enacted Fidelity is explicitly distinguished from habit. Habit is inertia. Enacted Fidelity is conscious, performative, relational repetition — trust expressed through the act of returning. Collapsing these is a theoretical regression that would undermine the paper's central argument.

**Status:** Substantially complete. Video evidence at https://youtu.be/7iqq1nRdKFg.

### Domain 3 (Active Development)

Black women's health disparities, specifically Graves' disease. Narrative-first CRISP-DM (Cross-Industry Standard Process for Data Mining — a standard workflow for data analysis projects, from business understanding through deployment) analysis of a population whose symptoms are systematically undertriaged. Same failure mode: fluent wrong answers from models trained on populations that don't include the people being served.

> **Plain language:** Graves' disease is an autoimmune condition where the immune system attacks the thyroid gland, causing it to produce excess hormones and leading to symptoms like rapid heartbeat, weight loss, and anxiety. It matters here because the document is examining why this particular condition may be missed or misdiagnosed in Black women.

> **Plain language:** Undertriage means a patient's condition is classified as less urgent or serious than it actually is, leading to delayed or inadequate treatment. The word 'systematically' here means this happens repeatedly and predictably to this group, not by accident but as a pattern in the healthcare system.

**Common Claim Across All Three Domains**

Standard analytical frameworks produce Insight Atrophy when applied to populations whose behavior operates through frameworks the model was never given. The Contract Window is the governance mechanism that makes the gap visible and repairable.

> **Plain language:** The Contract Window is a governance tool designed to identify and document places where a system's assumptions or training data don't match the real-world population it serves. It creates a formal way to spot and fix these mismatches.

> **Plain language:** Insight Atrophy occurs when an analytical system becomes progressively less useful or accurate because it was trained on data that doesn't represent the actual population being analyzed. Over time, the insights it produces deteriorate because the underlying patterns are fundamentally different from what the system learned.

---

## 6. Connection to Anthropic's Research Agenda

### Scalable Oversight (a research area focused on how humans can supervise AI systems even when those systems become more capable than the humans overseeing them)


> **Plain language:** This is a summary version of an AI conversation that removes unnecessary details while keeping the key information, so a person can quickly understand what happened without reviewing the entire exchange.
Leike et al. and subsequent work on scalable oversight (a research area focused on how humans can supervise AI systems even when those systems become more capable than the humans overseeing them) ask how humans can supervise AI systems performing tasks too complex for direct human evaluation. The Contract Window provides partial infrastructure: a compressed, human-readable session state that lets an oversight reviewer reconstruct what the investigation was, what the model claimed, and where the epistemic chain broke — without reading the full transcript.

> **Plain language:** An epistemic chain is the sequence of reasoning steps and evidence that led to a conclusion. When it 'breaks,' it means there's a gap where a claim isn't properly supported by the evidence or logic that came before it.

### Constitutional AI

Bai et al. (2022) establish that models can be trained to evaluate outputs against constitutional principles at training time. This framework extends that architecture to runtime: the Contract Window is a per-session constitution, auditable per-turn, contestable by the human operator, and repairable without session restart. The invariants (I1–I6) map directly to Anthropic's published commitments on honesty, harm avoidance, and uncertainty acknowledgment — but enforce them as runtime observables rather than training-time inferences.

> **Plain language:** Invariants are specific rules or constraints that must always hold true during operation; in this case, six numbered rules (I1 through I6) that the system commits to maintaining.

> **Plain language:** Runtime observables are measurable, checkable behaviors that happen when the model is actually responding to users, as opposed to properties the model learned during the initial training phase.

> **Plain language:** A Contract Window is a set of behavioral rules that applies to one conversation session with a user; it can be checked and reviewed after each response the model generates.

> **Plain language:** A per-session constitution means the set of rules is specific to one conversation and can be changed or adjusted just for that conversation, rather than being locked in globally for all users.

> **Plain language:** Constitutional principles are rules or values that an AI system is designed to follow—in this case, guidelines about how the model should behave ethically, such as being honest or avoiding harmful outputs.

> **Plain language:** Contestable means the human user can challenge or disagree with the rules in place and request that they be changed during the conversation.

### Interpretability


> **Plain language:** Rules or requirements that the model's outputs must satisfy—for example, 'do not generate harmful content' or 'cite sources for factual claims'—that are checked before the model's response is released.
The Bicameral Review mechanism and the Invariant Status field create a structured record of which constitutional constraints were evaluated and whether they cleared on each turn. This is not mechanistic interpretability (a field of AI research that studies what is happening inside a model's internal computations, not just what it outputs) of model internals, but it is a runtime observability layer that makes governance-relevant model behavior inspectable without access to weights or activations. It may complement interpretability research by providing a behavioral signal to validate against internal state observations.

> **Plain language:** Weights are the numerical parameters inside a model that control its behavior; activations are the intermediate signals produced as data flows through the model during computation—together they represent the internal 'black box' that is normally invisible.

> **Plain language:** This is a two-stage approval process where constitutional constraints are checked twice—once on initial generation and again on review—to ensure governance rules are actually being followed before output.

> **Plain language:** A data field that records whether each constitutional constraint passed or failed during evaluation, creating an auditable log of what was checked and the result.


> **Plain language:** Observable outputs and decisions made by the model at runtime that researchers can use to check whether the model's hidden internal workings are doing what they should be.
---

## 7. The Researcher

I am a 35-year educator turned AI engineer. I am Black, autistic, and live with schizophrenia, severe OCD, and ADHD. I did not arrive at this framework through the literature. I arrived at it through direct experience of what it costs when an AI system produces fluent, confident answers that are wrong in ways the operator cannot detect without a governance layer they do not have.

That is not a diversity statement. It is a methodology claim.

My neurodivergence is the instrument of observation. Autistic pattern recognition surfaces systematic misclassification before it becomes visible through aggregate statistics. OCD-driven verification compulsion operationalizes I2 (No Phantom Work) and I3 (Confidence Requires Verification) before they were formalized as invariants. ADHD executive function constraints are why the Contract Window has four fields instead of fourteen — every element had to justify its cognitive load.

In 2013, I published a peer-reviewed case study in *Focus on Colleges, Universities, and Schools* (Davis & Garrett-Staib, 2013) about a Black doctoral student in Texas with Bipolar I, OCD, ADHD, and auditory hallucinations who was nearly dismissed from his program because the institution had no interpretive framework for what was actually happening to him. The student was me. The paper was written in third person. The institution produced a fluent wrong answer. The framework I am building now is the 2026 answer to that 2013 problem.

I will be doing this work until I die. The only question is whether I do it with resources or without them.


> **Plain language:** A governance layer is a set of rules, checks, or oversight processes that someone applies to an AI system's outputs to catch errors and verify accuracy before acting on them—like a quality-control step that prevents bad answers from being used.
---

## 8. Limitations


> **Plain language:** These are two rules from the author's framework: I2 means that AI systems should not perform hidden work or make invisible decisions that operators cannot see or verify; I3 means that an AI system's confidence in its answer must be backed by actual verification, not just fluent-sounding text.
[These are stated explicitly per I2 — No Phantom Work]


> **Plain language:** The Contract Window is a tool or interface in the author's framework that captures key information about an AI task or interaction; it has been kept deliberately minimal (four fields) to avoid overwhelming the person using it with too much information to track at once.
1. **Observational foundation:** The invariant set and Contract Window architecture are derived from longitudinal self-observation and multi-model co-design, not from controlled experimental data. The hypotheses are falsifiable; the evidence is CONSTRUCTED, not VERIFIED.

> **Plain language:** Falsifiable means a hypothesis can be proven wrong through evidence or testing; if something is falsifiable, it is genuinely testable rather than merely immune to contradiction.

> **Plain language:** An interpretive framework is a structured way of understanding and explaining a situation so that what seems to be one problem (e.g., a student failing) can be correctly understood as something else (e.g., a disability that requires accommodation rather than punishment).

> **Plain language:** An invariant set is a collection of conditions or states that remain stable or unchanged even as a system evolves; in this context, it represents core patterns in how the system behaves consistently over time.

> **Plain language:** Contract Window architecture is the structural design of time-bounded operational agreements; it defines the framework for how commitments are made and validated within specific periods.

2. **Insight Atrophy index not yet operationalized:** H1 names the construct; the measurement instrument has not been validated. Operationalization is a first-year research deliverable.

> **Plain language:** The Insight Atrophy index is a proposed measurement of how quickly or severely useful knowledge or capability degrades over time in a system.

3. **Eight Wonders not validated as complete:** The taxonomy is theoretically grounded but has not been tested against an external sample for coverage or discriminant validity.

4. **WorldMart dataset:** Named throughout this proposal as a conceptual framing device. No public dataset exists under this name. Formalization is a research deliverable, not a prerequisite.

> **Plain language:** Operationalized means converted from a theoretical idea into a concrete, measurable procedure that can be tested in practice.

5. **Enforcement not production-tested:** The governance-kernel implementation in this repository is a research prototype. It has not been tested under production load, adversarial inputs, or multi-agent deployment at scale.

> **Plain language:** Discriminant validity is the property of measuring one distinct concept and not accidentally overlapping with measurements of different concepts.

6. **Generalizability:** All observational data was generated by a single operator (the author). Replication with diverse operator profiles is required before generalizing the findings.

---

## 9. Repository

> **Plain language:** Multi-agent deployment at scale means running the system with many independent actors or systems interacting simultaneously in a large real-world environment.

> **Plain language:** Adversarial inputs are deliberately malicious or edge-case requests designed to break or exploit a system's weaknesses.

> **Plain language:** Production load means the volume and intensity of real-world usage and transactions that a system must handle in normal operation.

> **Plain language:** A governance-kernel implementation is the core software code that enforces rules and decision-making logic in a system; in this case, it is an experimental version not yet proven reliable under real-world conditions.

This proposal is the foundation document for:
https://github.com/coreyalejandro/cognitive-governance-lab

The governance-kernel implementation, datasets, and case-law artifacts are being developed in parallel with this proposal. The repository structure mirrors the research program: each directory corresponds to a research component, not just a file category.

> **Plain language:** A governance-kernel is the core set of rules and decision-making procedures that will enforce the oversight system described in this proposal. It is being built as working code alongside this document.

> **Plain language:** Case-law artifacts are documented examples of past decisions and rulings that will be used to train and test the governance system, similar to how legal precedents guide court decisions.

---

## References

[PENDING — full citation list to be verified per Citation Research Protocol before submission. The following are named and will be verified against author, venue, and year before any version submitted externally:]

- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv preprint arXiv:2212.08073. https://doi.org/10.48550/arXiv.2212.08073 [VERIFIED]
- Leike, J. et al. Scalable agent alignment via reward modeling. [PENDING — year and venue to be confirmed before submission]
- Davis, R. & Garrett-Staib, A. (2013). [Title to be confirmed]. *Focus on Colleges, Universities, and Schools.* [PENDING — full title to be confirmed]

---

V&T: executive-summary-proposal.md — EXISTS (written, complete) → VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living-constitution repo, crsp-afs-2026 repo → NOT CLAIMED: empirical results (all hypotheses labeled CONSTRUCTED/PENDING), WorldMart dataset (conceptual framing device, not existing public dataset), production-tested enforcement → FUNCTIONAL STATUS: complete draft, ready for review and citation verification before external submission

> **Plain language:** CONSTRUCTED/PENDING means the claims in this proposal are theoretical or proposed scenarios that have not yet been tested with real data or systems.

> **Plain language:** WorldMart is a fictional example dataset used in this proposal to illustrate how the governance system would work in practice, not a real dataset that readers can access.

> **Plain language:** Session memory refers to notes and context from working meetings where this proposal was discussed and refined with the team.

> **Plain language:** The-living-constitution repo is a separate repository containing documents about how governance rules can be updated and refined over time, referenced here to ensure consistency with this proposal.

> **Plain language:** The crsp-afs-2026 repo is another working repository that this proposal has been cross-checked against to ensure no contradictions or gaps exist.

> **Plain language:** The Citation Research Protocol is an internal procedure for confirming that all cited sources are accurate in author name, publication venue, and year before this document is shared outside the team.