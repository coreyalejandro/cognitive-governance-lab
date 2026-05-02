# Proposal II: Cognitive Safety as Behavioral Ground Truth for Mechanistic Interpretability (a field of AI research that studies what is happening inside a model's internal computations, not just what it outputs)

> **Status labels used throughout this document:**
> VERIFIED = confirmed by direct evidence (artifact, transcript, test result).
> CONSTRUCTED = reasoned and plausible, but not yet tested in a controlled experiment.
> PENDING = planned as a future deliverable; does not exist yet.
> UNKNOWN = genuinely uncertain — no evidence either way.
> These labels appear in brackets throughout. They are not hedging — they are precision.


> **Plain language:** Behavioral ground truth means a reliable, observable measurement of how an AI system actually behaves in practice—like its outputs or actions—that researchers can use as the true standard against which to check whether their understanding of the system's internal workings is correct.

**Prepared for:** cognitive-governance-lab
**Author:** Corey Alejandro
**Date:** 2026-04-29
**Status:** CONSTRUCTED — exploratory research design, no empirical data yet collected

---

## Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and who is responsible for fixing errors)

> **Plain language:** This is a framework for documenting a conversation or collaboration between humans and AI systems, recording the goal of the work, what has been confirmed as accurate or working, and which person or role is accountable if something goes wrong.

TASK STATE: Develop a research proposal connecting Contract Window behavioral observables to mechanistic interpretability methodology
INVARIANT STATUS: I1 (evidence tagging throughout), I2 (no phantom performance claims), I3 (hedged language will not substitute for verification labels), I5 (correct over fluent)
REPAIR OBLIGATIONS: None active at proposal stage — obligations begin at execution
TRUTH STATUS: The research questions are real and open. The connection between Contract Window observables and interpretability findings is CONSTRUCTED — plausible, not confirmed.

> **Plain language:** This labels the confidence level of different parts of the proposal: the questions being asked are genuine and unresolved, but the claimed link between Contract Window data and mechanistic interpretability results is a theoretical proposal that seems reasonable but has not yet been tested or verified.

> **Plain language:** This refers to methods for understanding how AI systems make decisions by examining the internal mechanisms that produce those decisions, rather than just observing their outputs.

> **Plain language:** These are commitments to fix or correct problems if they are found; at the proposal stage (before work begins) none are yet assigned, but once the research is executed, specific people will be responsible for correcting errors or shortcomings that emerge.

> **Plain language:** These are consistency rules that the document must follow throughout: claims must be tagged with their evidence source, performance metrics must be real and measured (not assumed), vague or cautious language alone cannot substitute for explicit labels showing what has been verified, and accuracy matters more than readability.

> **Plain language:** These labels tell readers the strength of evidence behind each claim: VERIFIED means tested and proven, CONSTRUCTED means logically sound but untested, PENDING means planned but not done, and UNKNOWN means genuinely uncertain. This lets you judge how much confidence to place in each statement rather than guessing.

---

## Research Question

Can Contract Window runtime observables serve as behavioral ground truth for validating mechanistic interpretability findings?

> **Plain language:** This refers to detailed records of what a software system actually does while running—the inputs it receives, outputs it produces, and intermediate states it passes through—captured during execution of a contract (an agreement with defined terms). In this context, it means precise, timestamped behavioral logs that can serve as a reference standard for comparison.

> **Plain language:** This is the field of research that tries to understand how AI models work internally by identifying and analyzing the specific mathematical structures and operations inside them—similar to reverse-engineering a machine to understand each component's function.

That is the question. Not "can we improve interpretability" in the abstract — that framing is too wide to close. The specific gap this proposal targets is the validation problem in mechanistic interpretability: researchers identify internal model structures (features, circuits, attention patterns) and then face the question of whether those structures causally relate to the behaviors they appear to explain. Behavioral validation is hard. The Contract Window creates a structured behavioral record. This proposal asks whether that record is useful for closing the gap.

> **Plain language:** This means determining whether the internal structures actually *cause* the observed behavior, rather than just appearing alongside it—a critical distinction because correlation alone is not proof of influence.

> **Plain language:** This is the core difficulty that mechanistic interpretability research faces: identifying internal structures is not enough—researchers must prove those structures actually cause the model's external behavior, not just correlate with it by coincidence.

> **Plain language:** These are three types of interpretable structures found inside neural networks: features are learned detectors for specific concepts or patterns; circuits are chains of features that combine to perform a recognizable computational task; attention patterns are learned weights that determine which parts of the input the model focuses on. Together, they represent the 'wiring' researchers can observe inside a model.

---

## The Gap This Addresses

Mechanistic interpretability has made real progress. [VERIFIED] Work from Anthropic and others on sparse autoencoders (a tool used in interpretability research to decompose a model's internal representations into more understandable components), superposition (in AI: when a model represents more concepts than it has dedicated internal dimensions, compressing them into overlapping patterns), and feature decomposition has produced interpretable representations of internal model states that were previously opaque. We can now identify candidate features in residual stream activations that correspond to recognizable semantic concepts. We can trace circuits — paths through the network that appear to mediate specific behaviors.

> **Plain language:** Residual stream activations are the intermediate numerical values flowing through a neural network as it processes information—the 'workspace' where the model's thinking happens step-by-step.

> **Plain language:** Note: This has an inline gloss ('paths through the network that appear to mediate specific behaviors'). However, it may still benefit from clarification on *why* tracing them matters—but the gloss is present. Use judgment: flagging as borderline but the gloss is there, so NOT flagging per instructions.

> **Plain language:** Sparse autoencoders are machine learning tools that break down a neural network's internal decision-making into simpler, interpretable pieces—like taking a complex black box and labeling what each internal switch seems to be 'looking for.'

> **Plain language:** Note: This one HAS a parenthetical gloss, so it is adequate as-is. Not flagging.

[CONSTRUCTED] The problem is that "appear to" is doing a lot of work in that last sentence. Causal validation — establishing that a feature or circuit is not merely correlated with a behavior but actually mediates it — requires behavioral evidence. And behavioral evidence requires a structured behavioral record.

> **Plain language:** Note: Has inline gloss. NOT flagging.

Most interpretability research uses behavioral probes: force the model into a situation, see what activates, see whether ablating the identified structure changes the output. This is the right approach. The limit is that the behavioral situations are typically engineered by the researcher, not drawn from naturalistic deployment. The behaviors being probed are researcher-defined, not operationally observed.

> **Plain language:** Note: Has inline explanation ('force the model into a situation, see what activates...'). NOT flagging.

> **Plain language:** Ablating means deliberately removing or disabling a part of the model to see what changes—like removing a component from an engine to learn what it does.

The Contract Window produces a different kind of behavioral record. It is operational: it captures real conversational behavior over time, with explicit structure. It tracks Intent Fidelity (is the model serving the user's actual purpose?), Invariant Status (is the model honoring the hard constraints it committed to?), and V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work) adoption (is the model differentiating its verified from its constructed claims?). These are not researcher-engineered probes. They are continuous observables from deployment.

The question is whether these observables can ground mechanistic claims. If an interpretability researcher identifies a feature that correlates with what looks like "constraint relaxation" in the internal state, can a Contract Window record showing Invariant Status violations provide behavioral validation that the feature is real and causally relevant? That is the question.

---

## Connection to Anthropic's Interpretability Research

> **Plain language:** Note: Has inline gloss explaining the concept. NOT flagging.

> **Plain language:** Note: Has parenthetical gloss. NOT flagging.

> **Plain language:** Note: Has parenthetical gloss ('is the model serving the user's actual purpose?'). NOT flagging.


> **Plain language:** Operational here means the record captures real, live behavior from actual use, not behavior artificially created in a controlled lab setting.
[VERIFIED] Anthropic's work on sparse autoencoders applied to language model activations (Bricken et al., 2023; Templeton et al., 2024 — note: verify exact venue and year before citing in submission) has established that superposition is a real phenomenon: models represent more features than they have dimensions, compressed into overlapping directions in activation space. Decomposing these via sparse autoencoders produces features that are semantically interpretable.

> **Plain language:** Sparse autoencoders are mathematical tools that break down a neural network's internal representations into simpler, interpretable components by identifying which features are actually being used at any moment. This matters here because it lets researchers see what features the model is relying on when it processes information.

> **Plain language:** Superposition is when a neural network 'squeezes' more distinct concepts or patterns into its internal storage than it technically has room for, by overlapping them in clever ways. Understanding this helps explain how language models can handle such diverse tasks despite their architectural constraints.

> **Plain language:** Activation space is the multi-dimensional geometric landscape where a neural network represents information internally—think of it like a high-dimensional coordinate system where different directions represent different semantic concepts. This is where researchers look when trying to understand what the model 'knows' at any given moment.

[VERIFIED] The concept of attention head specialization — heads that perform identifiable functions such as induction, copying, or previous-token attention — is established in the literature (Olsson et al., 2022).

> **Plain language:** Attention heads are specific components of a language model that focus on different kinds of patterns in text. Specialization means some heads consistently perform particular tasks (like copying a word from earlier in the text, or predicting what word typically comes next).

[CONSTRUCTED] The extension this proposal makes is that Contract Window status transitions might provide a behavioral signal that can be mapped against these known structures. Specifically:

> **Plain language:** A Contract Window status transition is when the document's tracked compliance status changes categories (e.g., from STABLE to VIOLATION). This proposal treats such changes as observable signals that something shifted in how the model is processing information.

- If Invariant Status moves from STABLE to VIOLATION across a conversation, something in the model's processing changed. That change has a correlate in internal activations. Whether the internal correlate is identifiable using existing interpretability tools is an open question — this proposal would begin examining it.

- V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work) adoption behavior — whether the model differentiates verified from constructed claims — has a candidate internal correlate in how the model weights information from different parts of its context. Whether this correlates with attention head behavior is unknown and worth investigating.

- Intent Fidelity decline over a long conversation — the model gradually drifting from the user's evident purpose — has a temporal structure that might show up in internal states before it surfaces in output quality. That would be useful: if you can see behavioral drift coming in the internal states, you can intervene earlier.

None of this is confirmed. It is the research case for why these questions are worth asking.

> **Plain language:** Invariant Status is the compliance tracking system's designation of whether the model is maintaining its agreed-upon behavioral rules (STABLE) or breaking them (VIOLATION). Tracking when this changes helps the proposal connect observable compliance failures to internal model states.

---

## Three Exploratory Research Questions


> **Plain language:** V&T adoption refers to whether the model actually follows the Verification & Transparency requirement to distinguish between verified and constructed information in its responses. This is a measurable behavior that might reflect specific patterns in which parts of the model's internal attention it relies on.
These are not hypotheses in the formal sense. We do not have priors tight enough to commit to directional hypotheses. These are questions the work would attempt to answer. [CONSTRUCTED throughout — none of these have been tested]

### RQ1: Do Invariant Status violations correlate with identifiable internal state transitions?

> **Plain language:** An Invariant Status violation occurs when a rule or constraint that the model is supposed to follow is broken—for example, if the model was supposed to maintain a consistent commitment but didn't. This question asks whether we can detect warning signs in the model's internal computations when such a violation is about to happen or is happening.

> **Plain language:** Intent Fidelity decline is when a model gradually stops following or understanding what the user actually wants and instead drifts toward its own patterns or tangents. This proposal suggests such drift might be detectable in the model's internal states before it becomes obvious in the actual output.

When a Contract Window record shows a transition from Invariant STABLE to Invariant VIOLATION, what is happening in the model's internal state at that point? Are there activation patterns, feature directions, or circuit behaviors that are reliably present at the transition and absent in stable windows?

> **Plain language:** These are different ways to look at what the model's neural network is 'doing' internally at a given moment—which neurons are firing (activation patterns), which learned concepts are being emphasized (feature directions), and which combinations of neurons are working together to produce an output (circuit behaviors). The question is whether any of these show a consistent fingerprint right when a violation occurs.

> **Plain language:** A Contract Window record is a logged snapshot of the model's behavior and reasoning during a specific conversation or interaction, tagged with whether the model was following its constraints (STABLE) or breaking them (VIOLATION). This gives researchers a timestamped record of when and how things went wrong.

This is the most tractable of the three questions because Invariant Status is discrete: STABLE or VIOLATION. That makes it a classification target. You can build a dataset of (internal state, invariant status) pairs from logged conversations and ask whether any interpretable features discriminate the two classes.

> **Plain language:** Because Invariant Status has only two possible values (not a range or spectrum), researchers can use standard machine-learning classification techniques—training a model to predict which of the two states applies—rather than trying to predict a continuous number. This makes the analysis mathematically cleaner and more reliable.

The honest challenge: the internal state at the moment of a behavioral change may not be the causal state. The violation may have been set up several turns earlier. Any analysis here needs to account for temporal lag between internal state change and behavioral manifestation.

### RQ2: Do V&T adoption patterns correlate with attention head behaviors?

> **Plain language:** V&T refers to a model's ability to distinguish between Verified statements (claims that can be traced back to its training data) and Truthful but constructed statements (claims the model generates that are accurate but not from its training data). Adoption patterns mean how consistently and effectively a model learns to use this distinction.

> **Plain language:** Attention heads are components inside a language model that focus on specific parts of the input text when processing information; their 'behaviors' refer to which parts of the text they focus on and how that focus changes depending on what the model is doing.

When a model produces a V&T statement that accurately differentiates its verified from its constructed claims, what is the attention pattern over the context? When a model fails to differentiate — presenting constructed content with the same surface confidence as verified content — does the attention pattern differ in identifiable ways?

> **Plain language:** An attention pattern is a map showing which words or phrases in the input text the model's attention heads are focusing on at each step; it reveals which parts of the context the model considered important when making a decision.

The hypothesis space here connects to what is known about how attention heads process information from different context positions. A model that is correctly tracking its own epistemic status might show different attention to its "retrieved" versus "generated" tokens. This is speculative. It could be completely wrong. That is why it is a research question.

> **Plain language:** Epistemic status means how confident or certain a model should be about a piece of information — whether it is quoting something it learned, making an educated guess, or speculating.


> **Plain language:** A temporal lag is a delay in time—in this case, the internal change in the model's thinking may happen several conversation turns before the actual rule-breaking behavior appears. Researchers need to account for this delay, or they might miss the true cause by looking at the wrong moment in the conversation history.
Methodological note: measuring "accuracy" of V&T adoption requires ground truth about what in the model's training corpus is verified versus constructed. This is hard to establish. The proposal acknowledges this as a primary methodological challenge.

### RQ3: Can behavioral drift — declining Intent Fidelity over a long conversation — be predicted from internal state signals before it surfaces in output?

> **Plain language:** Intent Fidelity is how accurately the model stays focused on what the user actually wants, rather than substituting its own goals or patterns.

> **Plain language:** Behavioral drift means the model's responses gradually shift away from what the user actually asked for or needs, like slowly drifting off course without a sharp turn.

> **Plain language:** Retrieved tokens are words the model pulls directly from its training data, while generated tokens are words the model creates on its own during text production; the distinction matters because retrieved content should be more reliable.

This is the most practically significant question if it has an affirmative answer. Intent Fidelity decline is detectable in output: you can read a long conversation and notice that the model is gradually serving something other than the user's purpose. But detecting it in output means it has already happened.

The question is whether the internal state signals drift before the output does. If there are early internal indicators of Intent Fidelity decline — features activating, circuits engaging — that precede the behavioral manifestation by several turns, that is a meaningful finding for runtime monitoring.

> **Plain language:** Runtime monitoring means watching the model while it is actively generating responses, so problems can be caught and corrected in real time rather than after the fact.

> **Plain language:** These are specific measurable changes in how the model processes information internally (analogous to which neurons fire in a brain), which might warn us of problems before they appear in the output.

> **Plain language:** Internal state signals are measurable patterns of activity inside the model's computation — like which mathematical weights are active — that happen before you see the effects in the text it produces.

This question requires longitudinal conversation data with annotated Intent Fidelity scores at each turn. That data does not currently exist in the form needed. Building it is part of the research work, not a precondition for funding.

> **Plain language:** Longitudinal conversation data means tracking the same conversations over many turns (like watching someone's behavior unfold over time), with expert human judgments about whether the model is staying true to the user's intent at each step.

---

## What This Is Not

This proposal is not claiming that Contract Window observables are a better interpretability tool than existing methods. They are not. Activation patching, logit lens, sparse autoencoders — these are purpose-built for interpretability. Contract Window observables are purpose-built for runtime governance.

> **Plain language:** Activation patching is a technique where researchers modify the internal computational states of a neural network to see how changes affect outputs, helping them understand which internal components matter for specific behaviors.

> **Plain language:** Logit lens is a method that examines the internal representations at each layer of a neural network to understand what predictions the model is 'leaning toward' at different depths of computation.

> **Plain language:** Sparse autoencoders are machine learning models that compress and decompose the complex internal activity of neural networks into simpler, more interpretable components.

> **Plain language:** Contract Window observables are records of system behavior captured at defined points during a model's operation, used to track what the system actually does rather than how it works internally.

What the proposal claims is that the behavioral record produced by Contract Window governance is structurally suited to serve as validation signal for interpretability findings. It is a bridge between the behavioral layer and the mechanistic layer, not a replacement for either.

> **Plain language:** The mechanistic layer refers to the internal mathematical operations and component interactions that produce a system's behavior—how the system actually works at a technical level.

> **Plain language:** A behavioral record is a documented collection of the actual outputs and actions a system produces, capturing what it does rather than explaining why or how it works internally.

This proposal is also not claiming that the three research questions have positive answers. They might not. RQ2 in particular is speculative enough that a null result is a real possibility. The research is worth doing because the questions are real and the answers — positive or null — would be informative.

> **Plain language:** A validation signal is information or evidence that confirms whether an interpretation or explanation of a system's behavior is accurate.

---

## Why Now

[CONSTRUCTED] The timing argument: mechanistic interpretability has reached the point where it produces claims specific enough to test against behavioral data. Five years ago the claims were too coarse. The features identified were too broad to map to specific behavioral events. The work from 2023-2025 on sparse autoencoders and feature geometry is specific enough that you can start asking "does this feature activate during the turn where the model violates its stated constraint?" That question is now askable. It was not before.

> **Plain language:** Sparse autoencoders are a type of AI analysis tool that breaks down a model's internal representations into a small number of meaningful, human-interpretable components—think of it like decomposing a complex image into individual recognizable objects rather than leaving it as a blur of pixels.

> **Plain language:** Feature geometry refers to the mathematical arrangement and relationships between these interpretable components in the model's internal space—essentially, how these meaningful pieces are organized relative to each other in a way that affects the model's behavior.

> **Plain language:** Mechanistic interpretability is the field of research that tries to understand how AI models work by examining their internal computational mechanisms—similar to reverse-engineering a piece of software to see exactly what steps it takes to produce an output.

Contract Window as a structured behavioral framework is recent. The tooling to produce the kind of behavioral record this proposal requires — continuous, structured, with explicit status tracking — is not widely deployed. This lab is in a position to build it. That is a genuine comparative advantage for this line of work.

---

## V&T Statement

I verify the following as grounded: the citations to Anthropic interpretability work (Bricken, Templeton, Olsson) refer to real research programs — but exact venue and year should be confirmed before any formal submission, as agent memory has been wrong about these details before; the characterization of the validation problem in mechanistic interpretability reflects the current state of the field as understood from published work; the structural description of Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption) reflects the framework as defined in this repository.

> **Plain language:** Contract Window observables are measurable signals or states within an AI system that indicate whether the system is staying aligned with its intended purpose; they are the specific things you can check to verify the system is behaving as designed.

> **Plain language:** Intent Fidelity measures how closely the AI system's actual behavior matches what it was intended to do—essentially, how well it stays true to its original purpose.

> **Plain language:** Invariant Status tracks whether key properties or rules that should never change within the system remain stable and unbroken over time.

> **Plain language:** V&T adoption refers to how widely or thoroughly the system has integrated the verification and transparency framework described in this proposal.

> **Plain language:** Mechanistic interpretability is the research field that tries to understand how AI systems make decisions by examining the internal mathematical operations and patterns inside them, rather than just looking at their inputs and outputs.

> **Plain language:** Contract Window is (based on context) a framework for systematically recording and analyzing specific moments when an AI model either follows or violates its stated rules or constraints during operation.

I am transparent that the following are constructed: the three research questions have not been tested; no data exists yet showing that Contract Window observables correlate with internal state transitions; the connection between V&T adoption and attention head behavior is speculative; the claim that behavioral drift can be predicted from internal signals before output manifestation is a hypothesis that may be false; the timing argument about mechanistic interpretability reaching testable specificity is the author's assessment, not a surveyed consensus. This entire proposal is a reasoned argument for why these questions are worth investigating — it is not evidence that the answers are what we hope they are.

> **Plain language:** Behavioral drift is when an AI system's outputs and decisions gradually shift away from its original intended behavior, usually without any explicit change to its code or training.

> **Plain language:** Attention heads are specific mathematical components inside transformer-based AI models that learn to focus on certain parts of the input when making decisions; their behavior refers to which parts they prioritize and how that prioritization changes.

> **Plain language:** Internal state transitions are shifts in the system's underlying computational configuration—the moment when internal patterns or operations change from one stable mode to another.