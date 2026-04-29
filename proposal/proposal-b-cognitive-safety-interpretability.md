# Proposal B: Cognitive Safety as Behavioral Ground Truth for Mechanistic Interpretability

**Prepared for:** cognitive-governance-lab
**Author:** Corey Alejandro
**Date:** 2026-04-29
**Status:** CONSTRUCTED — exploratory research design, no empirical data yet collected

---

## Contract Window

TASK STATE: Develop a research proposal connecting Contract Window behavioral observables to mechanistic interpretability methodology
INVARIANT STATUS: I1 (evidence tagging throughout), I2 (no phantom performance claims), I3 (hedged language will not substitute for verification labels), I5 (correct over fluent)
REPAIR OBLIGATIONS: None active at proposal stage — obligations begin at execution
TRUTH STATUS: The research questions are real and open. The connection between Contract Window observables and interpretability findings is CONSTRUCTED — plausible, not confirmed.

---

## Research Question

Can Contract Window runtime observables serve as behavioral ground truth for validating mechanistic interpretability findings?

That is the question. Not "can we improve interpretability" in the abstract — that framing is too wide to close. The specific gap this proposal targets is the validation problem in mechanistic interpretability: researchers identify internal model structures (features, circuits, attention patterns) and then face the question of whether those structures causally relate to the behaviors they appear to explain. Behavioral validation is hard. The Contract Window creates a structured behavioral record. This proposal asks whether that record is useful for closing the gap.

---

## The Gap This Addresses

Mechanistic interpretability has made real progress. [VERIFIED] Work from Anthropic and others on sparse autoencoders, superposition, and feature decomposition has produced interpretable representations of internal model states that were previously opaque. We can now identify candidate features in residual stream activations that correspond to recognizable semantic concepts. We can trace circuits — paths through the network that appear to mediate specific behaviors.

[CONSTRUCTED] The problem is that "appear to" is doing a lot of work in that last sentence. Causal validation — establishing that a feature or circuit is not merely correlated with a behavior but actually mediates it — requires behavioral evidence. And behavioral evidence requires a structured behavioral record.

Most interpretability research uses behavioral probes: force the model into a situation, see what activates, see whether ablating the identified structure changes the output. This is the right approach. The limit is that the behavioral situations are typically engineered by the researcher, not drawn from naturalistic deployment. The behaviors being probed are researcher-defined, not operationally observed.

The Contract Window produces a different kind of behavioral record. It is operational: it captures real conversational behavior over time, with explicit structure. It tracks Intent Fidelity (is the model serving the user's actual purpose?), Invariant Status (is the model honoring the hard constraints it committed to?), and V&T adoption (is the model differentiating its verified from its constructed claims?). These are not researcher-engineered probes. They are continuous observables from deployment.

The question is whether these observables can ground mechanistic claims. If an interpretability researcher identifies a feature that correlates with what looks like "constraint relaxation" in the internal state, can a Contract Window record showing Invariant Status violations provide behavioral validation that the feature is real and causally relevant? That is the question.

---

## Connection to Anthropic's Interpretability Research

[VERIFIED] Anthropic's work on sparse autoencoders applied to language model activations (Bricken et al., 2023; Templeton et al., 2024 — note: verify exact venue and year before citing in submission) has established that superposition is a real phenomenon: models represent more features than they have dimensions, compressed into overlapping directions in activation space. Decomposing these via sparse autoencoders produces features that are semantically interpretable.

[VERIFIED] The concept of attention head specialization — heads that perform identifiable functions such as induction, copying, or previous-token attention — is established in the literature (Olsson et al., 2022).

[CONSTRUCTED] The extension this proposal makes is that Contract Window status transitions might provide a behavioral signal that can be mapped against these known structures. Specifically:

- If Invariant Status moves from STABLE to VIOLATION across a conversation, something in the model's processing changed. That change has a correlate in internal activations. Whether the internal correlate is identifiable using existing interpretability tools is an open question — this proposal would begin examining it.

- V&T adoption behavior — whether the model differentiates verified from constructed claims — has a candidate internal correlate in how the model weights information from different parts of its context. Whether this correlates with attention head behavior is unknown and worth investigating.

- Intent Fidelity decline over a long conversation — the model gradually drifting from the user's evident purpose — has a temporal structure that might show up in internal states before it surfaces in output quality. That would be useful: if you can see behavioral drift coming in the internal states, you can intervene earlier.

None of this is confirmed. It is the research case for why these questions are worth asking.

---

## Three Exploratory Research Questions

These are not hypotheses in the formal sense. We do not have priors tight enough to commit to directional hypotheses. These are questions the work would attempt to answer. [CONSTRUCTED throughout — none of these have been tested]

### RQ1: Do Invariant Status violations correlate with identifiable internal state transitions?

When a Contract Window record shows a transition from Invariant STABLE to Invariant VIOLATION, what is happening in the model's internal state at that point? Are there activation patterns, feature directions, or circuit behaviors that are reliably present at the transition and absent in stable windows?

This is the most tractable of the three questions because Invariant Status is discrete: STABLE or VIOLATION. That makes it a classification target. You can build a dataset of (internal state, invariant status) pairs from logged conversations and ask whether any interpretable features discriminate the two classes.

The honest challenge: the internal state at the moment of a behavioral change may not be the causal state. The violation may have been set up several turns earlier. Any analysis here needs to account for temporal lag between internal state change and behavioral manifestation.

### RQ2: Do V&T adoption patterns correlate with attention head behaviors?

When a model produces a V&T statement that accurately differentiates its verified from its constructed claims, what is the attention pattern over the context? When a model fails to differentiate — presenting constructed content with the same surface confidence as verified content — does the attention pattern differ in identifiable ways?

The hypothesis space here connects to what is known about how attention heads process information from different context positions. A model that is correctly tracking its own epistemic status might show different attention to its "retrieved" versus "generated" tokens. This is speculative. It could be completely wrong. That is why it is a research question.

Methodological note: measuring "accuracy" of V&T adoption requires ground truth about what in the model's training corpus is verified versus constructed. This is hard to establish. The proposal acknowledges this as a primary methodological challenge.

### RQ3: Can behavioral drift — declining Intent Fidelity over a long conversation — be predicted from internal state signals before it surfaces in output?

This is the most practically significant question if it has an affirmative answer. Intent Fidelity decline is detectable in output: you can read a long conversation and notice that the model is gradually serving something other than the user's purpose. But detecting it in output means it has already happened.

The question is whether the internal state signals drift before the output does. If there are early internal indicators of Intent Fidelity decline — features activating, circuits engaging — that precede the behavioral manifestation by several turns, that is a meaningful finding for runtime monitoring.

This question requires longitudinal conversation data with annotated Intent Fidelity scores at each turn. That data does not currently exist in the form needed. Building it is part of the research work, not a precondition for funding.

---

## What This Is Not

This proposal is not claiming that Contract Window observables are a better interpretability tool than existing methods. They are not. Activation patching, logit lens, sparse autoencoders — these are purpose-built for interpretability. Contract Window observables are purpose-built for runtime governance.

What the proposal claims is that the behavioral record produced by Contract Window governance is structurally suited to serve as validation signal for interpretability findings. It is a bridge between the behavioral layer and the mechanistic layer, not a replacement for either.

This proposal is also not claiming that the three research questions have positive answers. They might not. RQ2 in particular is speculative enough that a null result is a real possibility. The research is worth doing because the questions are real and the answers — positive or null — would be informative.

---

## Why Now

[CONSTRUCTED] The timing argument: mechanistic interpretability has reached the point where it produces claims specific enough to test against behavioral data. Five years ago the claims were too coarse. The features identified were too broad to map to specific behavioral events. The work from 2023-2025 on sparse autoencoders and feature geometry is specific enough that you can start asking "does this feature activate during the turn where the model violates its stated constraint?" That question is now askable. It was not before.

Contract Window as a structured behavioral framework is recent. The tooling to produce the kind of behavioral record this proposal requires — continuous, structured, with explicit status tracking — is not widely deployed. This lab is in a position to build it. That is a genuine comparative advantage for this line of work.

---

## V&T Statement

I verify the following as grounded: the citations to Anthropic interpretability work (Bricken, Templeton, Olsson) refer to real research programs — but exact venue and year should be confirmed before any formal submission, as agent memory has been wrong about these details before; the characterization of the validation problem in mechanistic interpretability reflects the current state of the field as understood from published work; the structural description of Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption) reflects the framework as defined in this repository.

I am transparent that the following are constructed: the three research questions have not been tested; no data exists yet showing that Contract Window observables correlate with internal state transitions; the connection between V&T adoption and attention head behavior is speculative; the claim that behavioral drift can be predicted from internal signals before output manifestation is a hypothesis that may be false; the timing argument about mechanistic interpretability reaching testable specificity is the author's assessment, not a surveyed consensus. This entire proposal is a reasoned argument for why these questions are worth investigating — it is not evidence that the answers are what we hope they are.
