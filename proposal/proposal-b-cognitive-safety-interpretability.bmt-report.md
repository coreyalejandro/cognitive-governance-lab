# BMT Audit Report

**File:** proposal-b-cognitive-safety-interpretability.md
**Audited:** 2026-05-01T07:55:04.218578+00:00
**Violations found:** 67 (BMT-1: 1, BMT-2: 66, BMT-4: 0)
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
| 1 | 43 | The Contract Window produces a different kind of behavioral record. It is operational: it captures r | Define "V&T" on first use: V&T (Verification and Truth — a statement that explicitly separates what  |

### BMT-2 Violations (Concepts Without Plain-Language Explanation)

These are the deeper violations — the standard exposed by the ChatGPT
translation benchmark. Each item below is a concept that was introduced
without the follow-up sentence a zero-prior-knowledge reader needs.

| # | Line | Concept | Explanation Inserted |
|---|------|---------|----------------------|
| 1 | 9 | Cognitive Safety as Behavioral Ground Truth for Mechanistic Interpretability | Behavioral ground truth means a reliable, observable measurement of how an AI system actually behave |
| 2 | 21 | These labels appear in brackets throughout. They are not hedging — they are prec | These labels tell readers the strength of evidence behind each claim: VERIFIED means tested and prov |
| 3 | 18 | Contract Window (a structured record of what a human-AI session is trying to acc | This is a framework for documenting a conversation or collaboration between humans and AI systems, r |
| 4 | 20 | Develop a research proposal connecting Contract Window behavioral observables to | This refers to methods for understanding how AI systems make decisions by examining the internal mec |
| 5 | 21 | INVARIANT STATUS: I1 (evidence tagging throughout), I2 (no phantom performance c | These are consistency rules that the document must follow throughout: claims must be tagged with the |
| 6 | 22 | REPAIR OBLIGATIONS: None active at proposal stage — obligations begin at executi | These are commitments to fix or correct problems if they are found; at the proposal stage (before wo |
| 7 | 23 | TRUTH STATUS: The research questions are real and open. The connection between C | This labels the confidence level of different parts of the proposal: the questions being asked are g |
| 8 | 27 | Can Contract Window runtime observables serve as behavioral ground truth | This refers to detailed records of what a software system actually does while running—the inputs it  |
| 9 | 27 | validating mechanistic interpretability findings | This is the field of research that tries to understand how AI models work internally by identifying  |
| 10 | 32 | researchers identify internal model structures (features, circuits, attention pa | These are three types of interpretable structures found inside neural networks: features are learned |
| 11 | 33 | the validation problem in mechanistic interpretability | This is the core difficulty that mechanistic interpretability research faces: identifying internal s |
| 12 | 34 | whether those structures causally relate to the behaviors they appear to explain | This means determining whether the internal structures actually *cause* the observed behavior, rathe |
| 13 | 37 | Work from Anthropic and others on sparse autoencoders | Sparse autoencoders are machine learning tools that break down a neural network's internal decision- |
| 14 | 37 | superposition (in AI: when a model represents more concepts...) | Note: This one HAS a parenthetical gloss, so it is adequate as-is. Not flagging. |
| 15 | 39 | identify candidate features in residual stream activations | Residual stream activations are the intermediate numerical values flowing through a neural network a |
| 16 | 39 | We can trace circuits — paths through the network that appear to mediate specifi | Note: This has an inline gloss ('paths through the network that appear to mediate specific behaviors |
| 17 | 42 | Causal validation — establishing that a feature or circuit is not merely correla | Note: Has inline gloss. NOT flagging. |
| 18 | 45 | Most interpretability research uses behavioral probes: force the model into a si | Note: Has inline explanation ('force the model into a situation, see what activates...'). NOT flaggi |
| 19 | 45 | see whether ablating the identified structure changes the output | Ablating means deliberately removing or disabling a part of the model to see what changes—like remov |
| 20 | 49 | It tracks Intent Fidelity (is the model serving the user's actual purpose?) | Note: Has parenthetical gloss ('is the model serving the user's actual purpose?'). NOT flagging. |
| 21 | 49 | Invariant Status (is the model honoring the hard constraints it committed to?) | Note: Has parenthetical gloss. NOT flagging. |
| 22 | 49 | V&T (Verification and Truth — a statement that explicitly separates...) | Note: Has inline gloss explaining the concept. NOT flagging. |
| 23 | 50 | The Contract Window produces a different kind of behavioral record. It is operat | Operational here means the record captures real, live behavior from actual use, not behavior artific |
| 24 | 51 | Anthropic's work on sparse autoencoders applied to language model activations | Sparse autoencoders are mathematical tools that break down a neural network's internal representatio |
| 25 | 51 | has established that superposition is a real phenomenon: models represent more f | Superposition is when a neural network 'squeezes' more distinct concepts or patterns into its intern |
| 26 | 51 | compressed into overlapping directions in activation space | Activation space is the multi-dimensional geometric landscape where a neural network represents info |
| 27 | 56 | The concept of attention head specialization — heads that perform identifiable f | Attention heads are specific components of a language model that focus on different kinds of pattern |
| 28 | 60 | Contract Window status transitions might provide a behavioral signal that can be | A Contract Window status transition is when the document's tracked compliance status changes categor |
| 29 | 63 | If Invariant Status moves from STABLE to VIOLATION across a conversation | Invariant Status is the compliance tracking system's designation of whether the model is maintaining |
| 30 | 68 | V&T adoption behavior — whether the model differentiates verified from construct | V&T adoption refers to whether the model actually follows the Verification & Transparency requiremen |
| 31 | 71 | Intent Fidelity decline over a long conversation — the model gradually drifting  | Intent Fidelity decline is when a model gradually stops following or understanding what the user act |
| 32 | 71 | Do Invariant Status violations correlate with identifiable internal state transi | An Invariant Status violation occurs when a rule or constraint that the model is supposed to follow  |
| 33 | 71 | When a Contract Window record shows a transition from Invariant STABLE to Invari | A Contract Window record is a logged snapshot of the model's behavior and reasoning during a specifi |
| 34 | 73 | Are there activation patterns, feature directions, or circuit behaviors that are | These are different ways to look at what the model's neural network is 'doing' internally at a given |
| 35 | 79 | This is the most tractable of the three questions because Invariant Status is di | Because Invariant Status has only two possible values (not a range or spectrum), researchers can use |
| 36 | 85 | Any analysis here needs to account for temporal lag between internal state chang | A temporal lag is a delay in time—in this case, the internal change in the model's thinking may happ |
| 37 | 79 | Do V&T adoption patterns correlate with attention head behaviors? | V&T refers to a model's ability to distinguish between Verified statements (claims that can be trace |
| 38 | 81 | Do V&T adoption patterns correlate with attention head behaviors? | Attention heads are components inside a language model that focus on specific parts of the input tex |
| 39 | 85 | When a model produces a V&T statement that accurately differentiates its verifie | An attention pattern is a map showing which words or phrases in the input text the model's attention |
| 40 | 88 | A model that is correctly tracking its own epistemic status might show different | Epistemic status means how confident or certain a model should be about a piece of information — whe |
| 41 | 88 | ...might show different attention to its "retrieved" versus "generated" tokens. | Retrieved tokens are words the model pulls directly from its training data, while generated tokens a |
| 42 | 87 | Can behavioral drift — declining Intent Fidelity over a long conversation | Behavioral drift means the model's responses gradually shift away from what the user actually asked  |
| 43 | 87 | declining Intent Fidelity over a long conversation — be predicted | Intent Fidelity is how accurately the model stays focused on what the user actually wants, rather th |
| 44 | 92 | whether the internal state signals drift before the output does | Internal state signals are measurable patterns of activity inside the model's computation — like whi |
| 45 | 94 | early internal indicators of Intent Fidelity decline — features activating, circ | These are specific measurable changes in how the model processes information internally (analogous t |
| 46 | 96 | a meaningful finding for runtime monitoring | Runtime monitoring means watching the model while it is actively generating responses, so problems c |
| 47 | 98 | requires longitudinal conversation data with annotated Intent Fidelity scores | Longitudinal conversation data means tracking the same conversations over many turns (like watching  |
| 48 | 99 | This proposal is not claiming that Contract Window observables are a better... | Contract Window observables are records of system behavior captured at defined points during a model |
| 49 | 100 | Activation patching, logit lens, sparse autoencoders — these are purpose-built.. | Activation patching is a technique where researchers modify the internal computational states of a n |
| 50 | 100 | Activation patching, logit lens, sparse autoencoders — these are purpose-built.. | Logit lens is a method that examines the internal representations at each layer of a neural network  |
| 51 | 100 | Activation patching, logit lens, sparse autoencoders — these are purpose-built.. | Sparse autoencoders are machine learning models that compress and decompose the complex internal act |
| 52 | 105 | What the proposal claims is that the behavioral record produced by Contract... | A behavioral record is a documented collection of the actual outputs and actions a system produces,  |
| 53 | 105 | ...behavioral record produced by Contract Window governance is structurally suit | A validation signal is information or evidence that confirms whether an interpretation or explanatio |
| 54 | 106 | It is a bridge between the behavioral layer and the mechanistic layer... | The mechanistic layer refers to the internal mathematical operations and component interactions that |
| 55 | 108 | mechanistic interpretability has reached the point where it produces claims spec | Mechanistic interpretability is the field of research that tries to understand how AI models work by |
| 56 | 111 | The work from 2023-2025 on sparse autoencoders and feature geometry is specific  | Sparse autoencoders are a type of AI analysis tool that breaks down a model's internal representatio |
| 57 | 111 | The work from 2023-2025 on sparse autoencoders and feature geometry is specific  | Feature geometry refers to the mathematical arrangement and relationships between these interpretabl |
| 58 | 117 | Contract Window as a structured behavioral framework is recent. | Contract Window is (based on context) a framework for systematically recording and analyzing specifi |
| 59 | 115 | citations to Anthropic interpretability work (Bricken, Templeton, Olsson)… | Mechanistic interpretability is the research field that tries to understand how AI systems make deci |
| 60 | 120 | structural description of Contract Window observables (Intent Fidelity… | Contract Window observables are measurable signals or states within an AI system that indicate wheth |
| 61 | 120 | Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption) | Intent Fidelity measures how closely the AI system's actual behavior matches what it was intended to |
| 62 | 120 | Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption) | Invariant Status tracks whether key properties or rules that should never change within the system r |
| 63 | 120 | Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption) | V&T adoption refers to how widely or thoroughly the system has integrated the verification and trans |
| 64 | 123 | no data exists yet showing that Contract Window observables correlate… | Internal state transitions are shifts in the system's underlying computational configuration—the mom |
| 65 | 124 | connection between V&T adoption and attention head behavior is speculative | Attention heads are specific mathematical components inside transformer-based AI models that learn t |
| 66 | 125 | behavioral drift can be predicted from internal signals before output… | Behavioral drift is when an AI system's outputs and decisions gradually shift away from its original |

#### Full BMT-2 Explanations Inserted

**1. Line 9 — Cognitive Safety as Behavioral Ground Truth for Mechanistic **

Inserted: Behavioral ground truth means a reliable, observable measurement of how an AI system actually behaves in practice—like its outputs or actions—that researchers can use as the true standard against which to check whether their understanding of the system's internal workings is correct.

**2. Line 21 — These labels appear in brackets throughout. They are not hed**

Inserted: These labels tell readers the strength of evidence behind each claim: VERIFIED means tested and proven, CONSTRUCTED means logically sound but untested, PENDING means planned but not done, and UNKNOWN means genuinely uncertain. This lets you judge how much confidence to place in each statement rather than guessing.

**3. Line 18 — Contract Window (a structured record of what a human-AI sess**

Inserted: This is a framework for documenting a conversation or collaboration between humans and AI systems, recording the goal of the work, what has been confirmed as accurate or working, and which person or role is accountable if something goes wrong.

**4. Line 20 — Develop a research proposal connecting Contract Window behav**

Inserted: This refers to methods for understanding how AI systems make decisions by examining the internal mechanisms that produce those decisions, rather than just observing their outputs.

**5. Line 21 — INVARIANT STATUS: I1 (evidence tagging throughout), I2 (no p**

Inserted: These are consistency rules that the document must follow throughout: claims must be tagged with their evidence source, performance metrics must be real and measured (not assumed), vague or cautious language alone cannot substitute for explicit labels showing what has been verified, and accuracy matters more than readability.

**6. Line 22 — REPAIR OBLIGATIONS: None active at proposal stage — obligati**

Inserted: These are commitments to fix or correct problems if they are found; at the proposal stage (before work begins) none are yet assigned, but once the research is executed, specific people will be responsible for correcting errors or shortcomings that emerge.

**7. Line 23 — TRUTH STATUS: The research questions are real and open. The **

Inserted: This labels the confidence level of different parts of the proposal: the questions being asked are genuine and unresolved, but the claimed link between Contract Window data and mechanistic interpretability results is a theoretical proposal that seems reasonable but has not yet been tested or verified.

**8. Line 27 — Can Contract Window runtime observables serve as behavioral **

Inserted: This refers to detailed records of what a software system actually does while running—the inputs it receives, outputs it produces, and intermediate states it passes through—captured during execution of a contract (an agreement with defined terms). In this context, it means precise, timestamped behavioral logs that can serve as a reference standard for comparison.

**9. Line 27 — validating mechanistic interpretability findings**

Inserted: This is the field of research that tries to understand how AI models work internally by identifying and analyzing the specific mathematical structures and operations inside them—similar to reverse-engineering a machine to understand each component's function.

**10. Line 32 — researchers identify internal model structures (features, ci**

Inserted: These are three types of interpretable structures found inside neural networks: features are learned detectors for specific concepts or patterns; circuits are chains of features that combine to perform a recognizable computational task; attention patterns are learned weights that determine which parts of the input the model focuses on. Together, they represent the 'wiring' researchers can observe inside a model.

**11. Line 33 — the validation problem in mechanistic interpretability**

Inserted: This is the core difficulty that mechanistic interpretability research faces: identifying internal structures is not enough—researchers must prove those structures actually cause the model's external behavior, not just correlate with it by coincidence.

**12. Line 34 — whether those structures causally relate to the behaviors th**

Inserted: This means determining whether the internal structures actually *cause* the observed behavior, rather than just appearing alongside it—a critical distinction because correlation alone is not proof of influence.

**13. Line 37 — Work from Anthropic and others on sparse autoencoders**

Inserted: Sparse autoencoders are machine learning tools that break down a neural network's internal decision-making into simpler, interpretable pieces—like taking a complex black box and labeling what each internal switch seems to be 'looking for.'

**14. Line 37 — superposition (in AI: when a model represents more concepts.**

Inserted: Note: This one HAS a parenthetical gloss, so it is adequate as-is. Not flagging.

**15. Line 39 — identify candidate features in residual stream activations**

Inserted: Residual stream activations are the intermediate numerical values flowing through a neural network as it processes information—the 'workspace' where the model's thinking happens step-by-step.

**16. Line 39 — We can trace circuits — paths through the network that appea**

Inserted: Note: This has an inline gloss ('paths through the network that appear to mediate specific behaviors'). However, it may still benefit from clarification on *why* tracing them matters—but the gloss is present. Use judgment: flagging as borderline but the gloss is there, so NOT flagging per instructions.

**17. Line 42 — Causal validation — establishing that a feature or circuit i**

Inserted: Note: Has inline gloss. NOT flagging.

**18. Line 45 — Most interpretability research uses behavioral probes: force**

Inserted: Note: Has inline explanation ('force the model into a situation, see what activates...'). NOT flagging.

**19. Line 45 — see whether ablating the identified structure changes the ou**

Inserted: Ablating means deliberately removing or disabling a part of the model to see what changes—like removing a component from an engine to learn what it does.

**20. Line 49 — It tracks Intent Fidelity (is the model serving the user's a**

Inserted: Note: Has parenthetical gloss ('is the model serving the user's actual purpose?'). NOT flagging.

**21. Line 49 — Invariant Status (is the model honoring the hard constraints**

Inserted: Note: Has parenthetical gloss. NOT flagging.

**22. Line 49 — V&T (Verification and Truth — a statement that explicitly se**

Inserted: Note: Has inline gloss explaining the concept. NOT flagging.

**23. Line 50 — The Contract Window produces a different kind of behavioral **

Inserted: Operational here means the record captures real, live behavior from actual use, not behavior artificially created in a controlled lab setting.

**24. Line 51 — Anthropic's work on sparse autoencoders applied to language **

Inserted: Sparse autoencoders are mathematical tools that break down a neural network's internal representations into simpler, interpretable components by identifying which features are actually being used at any moment. This matters here because it lets researchers see what features the model is relying on when it processes information.

**25. Line 51 — has established that superposition is a real phenomenon: mod**

Inserted: Superposition is when a neural network 'squeezes' more distinct concepts or patterns into its internal storage than it technically has room for, by overlapping them in clever ways. Understanding this helps explain how language models can handle such diverse tasks despite their architectural constraints.

**26. Line 51 — compressed into overlapping directions in activation space**

Inserted: Activation space is the multi-dimensional geometric landscape where a neural network represents information internally—think of it like a high-dimensional coordinate system where different directions represent different semantic concepts. This is where researchers look when trying to understand what the model 'knows' at any given moment.

**27. Line 56 — The concept of attention head specialization — heads that pe**

Inserted: Attention heads are specific components of a language model that focus on different kinds of patterns in text. Specialization means some heads consistently perform particular tasks (like copying a word from earlier in the text, or predicting what word typically comes next).

**28. Line 60 — Contract Window status transitions might provide a behaviora**

Inserted: A Contract Window status transition is when the document's tracked compliance status changes categories (e.g., from STABLE to VIOLATION). This proposal treats such changes as observable signals that something shifted in how the model is processing information.

**29. Line 63 — If Invariant Status moves from STABLE to VIOLATION across a **

Inserted: Invariant Status is the compliance tracking system's designation of whether the model is maintaining its agreed-upon behavioral rules (STABLE) or breaking them (VIOLATION). Tracking when this changes helps the proposal connect observable compliance failures to internal model states.

**30. Line 68 — V&T adoption behavior — whether the model differentiates ver**

Inserted: V&T adoption refers to whether the model actually follows the Verification & Transparency requirement to distinguish between verified and constructed information in its responses. This is a measurable behavior that might reflect specific patterns in which parts of the model's internal attention it relies on.

**31. Line 71 — Intent Fidelity decline over a long conversation — the model**

Inserted: Intent Fidelity decline is when a model gradually stops following or understanding what the user actually wants and instead drifts toward its own patterns or tangents. This proposal suggests such drift might be detectable in the model's internal states before it becomes obvious in the actual output.

**32. Line 71 — Do Invariant Status violations correlate with identifiable i**

Inserted: An Invariant Status violation occurs when a rule or constraint that the model is supposed to follow is broken—for example, if the model was supposed to maintain a consistent commitment but didn't. This question asks whether we can detect warning signs in the model's internal computations when such a violation is about to happen or is happening.

**33. Line 71 — When a Contract Window record shows a transition from Invari**

Inserted: A Contract Window record is a logged snapshot of the model's behavior and reasoning during a specific conversation or interaction, tagged with whether the model was following its constraints (STABLE) or breaking them (VIOLATION). This gives researchers a timestamped record of when and how things went wrong.

**34. Line 73 — Are there activation patterns, feature directions, or circui**

Inserted: These are different ways to look at what the model's neural network is 'doing' internally at a given moment—which neurons are firing (activation patterns), which learned concepts are being emphasized (feature directions), and which combinations of neurons are working together to produce an output (circuit behaviors). The question is whether any of these show a consistent fingerprint right when a violation occurs.

**35. Line 79 — This is the most tractable of the three questions because In**

Inserted: Because Invariant Status has only two possible values (not a range or spectrum), researchers can use standard machine-learning classification techniques—training a model to predict which of the two states applies—rather than trying to predict a continuous number. This makes the analysis mathematically cleaner and more reliable.

**36. Line 85 — Any analysis here needs to account for temporal lag between **

Inserted: A temporal lag is a delay in time—in this case, the internal change in the model's thinking may happen several conversation turns before the actual rule-breaking behavior appears. Researchers need to account for this delay, or they might miss the true cause by looking at the wrong moment in the conversation history.

**37. Line 79 — Do V&T adoption patterns correlate with attention head behav**

Inserted: V&T refers to a model's ability to distinguish between Verified statements (claims that can be traced back to its training data) and Truthful but constructed statements (claims the model generates that are accurate but not from its training data). Adoption patterns mean how consistently and effectively a model learns to use this distinction.

**38. Line 81 — Do V&T adoption patterns correlate with attention head behav**

Inserted: Attention heads are components inside a language model that focus on specific parts of the input text when processing information; their 'behaviors' refer to which parts of the text they focus on and how that focus changes depending on what the model is doing.

**39. Line 85 — When a model produces a V&T statement that accurately differ**

Inserted: An attention pattern is a map showing which words or phrases in the input text the model's attention heads are focusing on at each step; it reveals which parts of the context the model considered important when making a decision.

**40. Line 88 — A model that is correctly tracking its own epistemic status **

Inserted: Epistemic status means how confident or certain a model should be about a piece of information — whether it is quoting something it learned, making an educated guess, or speculating.

**41. Line 88 — ...might show different attention to its "retrieved" versus **

Inserted: Retrieved tokens are words the model pulls directly from its training data, while generated tokens are words the model creates on its own during text production; the distinction matters because retrieved content should be more reliable.

**42. Line 87 — Can behavioral drift — declining Intent Fidelity over a long**

Inserted: Behavioral drift means the model's responses gradually shift away from what the user actually asked for or needs, like slowly drifting off course without a sharp turn.

**43. Line 87 — declining Intent Fidelity over a long conversation — be pred**

Inserted: Intent Fidelity is how accurately the model stays focused on what the user actually wants, rather than substituting its own goals or patterns.

**44. Line 92 — whether the internal state signals drift before the output d**

Inserted: Internal state signals are measurable patterns of activity inside the model's computation — like which mathematical weights are active — that happen before you see the effects in the text it produces.

**45. Line 94 — early internal indicators of Intent Fidelity decline — featu**

Inserted: These are specific measurable changes in how the model processes information internally (analogous to which neurons fire in a brain), which might warn us of problems before they appear in the output.

**46. Line 96 — a meaningful finding for runtime monitoring**

Inserted: Runtime monitoring means watching the model while it is actively generating responses, so problems can be caught and corrected in real time rather than after the fact.

**47. Line 98 — requires longitudinal conversation data with annotated Inten**

Inserted: Longitudinal conversation data means tracking the same conversations over many turns (like watching someone's behavior unfold over time), with expert human judgments about whether the model is staying true to the user's intent at each step.

**48. Line 99 — This proposal is not claiming that Contract Window observabl**

Inserted: Contract Window observables are records of system behavior captured at defined points during a model's operation, used to track what the system actually does rather than how it works internally.

**49. Line 100 — Activation patching, logit lens, sparse autoencoders — these**

Inserted: Activation patching is a technique where researchers modify the internal computational states of a neural network to see how changes affect outputs, helping them understand which internal components matter for specific behaviors.

**50. Line 100 — Activation patching, logit lens, sparse autoencoders — these**

Inserted: Logit lens is a method that examines the internal representations at each layer of a neural network to understand what predictions the model is 'leaning toward' at different depths of computation.

**51. Line 100 — Activation patching, logit lens, sparse autoencoders — these**

Inserted: Sparse autoencoders are machine learning models that compress and decompose the complex internal activity of neural networks into simpler, more interpretable components.

**52. Line 105 — What the proposal claims is that the behavioral record produ**

Inserted: A behavioral record is a documented collection of the actual outputs and actions a system produces, capturing what it does rather than explaining why or how it works internally.

**53. Line 105 — ...behavioral record produced by Contract Window governance **

Inserted: A validation signal is information or evidence that confirms whether an interpretation or explanation of a system's behavior is accurate.

**54. Line 106 — It is a bridge between the behavioral layer and the mechanis**

Inserted: The mechanistic layer refers to the internal mathematical operations and component interactions that produce a system's behavior—how the system actually works at a technical level.

**55. Line 108 — mechanistic interpretability has reached the point where it **

Inserted: Mechanistic interpretability is the field of research that tries to understand how AI models work by examining their internal computational mechanisms—similar to reverse-engineering a piece of software to see exactly what steps it takes to produce an output.

**56. Line 111 — The work from 2023-2025 on sparse autoencoders and feature g**

Inserted: Sparse autoencoders are a type of AI analysis tool that breaks down a model's internal representations into a small number of meaningful, human-interpretable components—think of it like decomposing a complex image into individual recognizable objects rather than leaving it as a blur of pixels.

**57. Line 111 — The work from 2023-2025 on sparse autoencoders and feature g**

Inserted: Feature geometry refers to the mathematical arrangement and relationships between these interpretable components in the model's internal space—essentially, how these meaningful pieces are organized relative to each other in a way that affects the model's behavior.

**58. Line 117 — Contract Window as a structured behavioral framework is rece**

Inserted: Contract Window is (based on context) a framework for systematically recording and analyzing specific moments when an AI model either follows or violates its stated rules or constraints during operation.

**59. Line 115 — citations to Anthropic interpretability work (Bricken, Templ**

Inserted: Mechanistic interpretability is the research field that tries to understand how AI systems make decisions by examining the internal mathematical operations and patterns inside them, rather than just looking at their inputs and outputs.

**60. Line 120 — structural description of Contract Window observables (Inten**

Inserted: Contract Window observables are measurable signals or states within an AI system that indicate whether the system is staying aligned with its intended purpose; they are the specific things you can check to verify the system is behaving as designed.

**61. Line 120 — Contract Window observables (Intent Fidelity, Invariant Stat**

Inserted: Intent Fidelity measures how closely the AI system's actual behavior matches what it was intended to do—essentially, how well it stays true to its original purpose.

**62. Line 120 — Contract Window observables (Intent Fidelity, Invariant Stat**

Inserted: Invariant Status tracks whether key properties or rules that should never change within the system remain stable and unbroken over time.

**63. Line 120 — Contract Window observables (Intent Fidelity, Invariant Stat**

Inserted: V&T adoption refers to how widely or thoroughly the system has integrated the verification and transparency framework described in this proposal.

**64. Line 123 — no data exists yet showing that Contract Window observables **

Inserted: Internal state transitions are shifts in the system's underlying computational configuration—the moment when internal patterns or operations change from one stable mode to another.

**65. Line 124 — connection between V&T adoption and attention head behavior **

Inserted: Attention heads are specific mathematical components inside transformer-based AI models that learn to focus on certain parts of the input when making decisions; their behavior refers to which parts they prioritize and how that prioritization changes.

**66. Line 125 — behavioral drift can be predicted from internal signals befo**

Inserted: Behavioral drift is when an AI system's outputs and decisions gradually shift away from its original intended behavior, usually without any explicit change to its code or training.

---

## Original Violation Details

### Violation 1 — BMT-1

**Line 43:** `The Contract Window produces a different kind of behavioral record. It is operational: it captures r`

**Fix:** Define "V&T" on first use: V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work)

### Violation 2 — BMT-2

**Line 9:** `Cognitive Safety as Behavioral Ground Truth for Mechanistic Interpretability`

**Fix:** Add plain-language explanation after "Behavioral ground truth"

**Explanation inserted:** Behavioral ground truth means a reliable, observable measurement of how an AI system actually behaves in practice—like its outputs or actions—that researchers can use as the true standard against which to check whether their understanding of the system's internal workings is correct.

### Violation 3 — BMT-2

**Line 21:** `These labels appear in brackets throughout. They are not hedging — they are precision.`

**Fix:** Add plain-language explanation after "Status labels (VERIFIED, CONSTRUCTED, PENDING, UNKNOWN) used as precision marker"

**Explanation inserted:** These labels tell readers the strength of evidence behind each claim: VERIFIED means tested and proven, CONSTRUCTED means logically sound but untested, PENDING means planned but not done, and UNKNOWN means genuinely uncertain. This lets you judge how much confidence to place in each statement rather than guessing.

### Violation 4 — BMT-2

**Line 18:** `Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and who`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** This is a framework for documenting a conversation or collaboration between humans and AI systems, recording the goal of the work, what has been confirmed as accurate or working, and which person or role is accountable if something goes wrong.

### Violation 5 — BMT-2

**Line 20:** `Develop a research proposal connecting Contract Window behavioral observables to mechanistic interpretability methodolog`

**Fix:** Add plain-language explanation after "mechanistic interpretability methodology"

**Explanation inserted:** This refers to methods for understanding how AI systems make decisions by examining the internal mechanisms that produce those decisions, rather than just observing their outputs.

### Violation 6 — BMT-2

**Line 21:** `INVARIANT STATUS: I1 (evidence tagging throughout), I2 (no phantom performance claims), I3 (hedged language will not sub`

**Fix:** Add plain-language explanation after "INVARIANT STATUS"

**Explanation inserted:** These are consistency rules that the document must follow throughout: claims must be tagged with their evidence source, performance metrics must be real and measured (not assumed), vague or cautious language alone cannot substitute for explicit labels showing what has been verified, and accuracy matters more than readability.

### Violation 7 — BMT-2

**Line 22:** `REPAIR OBLIGATIONS: None active at proposal stage — obligations begin at execution`

**Fix:** Add plain-language explanation after "REPAIR OBLIGATIONS"

**Explanation inserted:** These are commitments to fix or correct problems if they are found; at the proposal stage (before work begins) none are yet assigned, but once the research is executed, specific people will be responsible for correcting errors or shortcomings that emerge.

### Violation 8 — BMT-2

**Line 23:** `TRUTH STATUS: The research questions are real and open. The connection between Contract Window observables and interpret`

**Fix:** Add plain-language explanation after "TRUTH STATUS"

**Explanation inserted:** This labels the confidence level of different parts of the proposal: the questions being asked are genuine and unresolved, but the claimed link between Contract Window data and mechanistic interpretability results is a theoretical proposal that seems reasonable but has not yet been tested or verified.

### Violation 9 — BMT-2

**Line 27:** `Can Contract Window runtime observables serve as behavioral ground truth`

**Fix:** Add plain-language explanation after "Contract Window runtime observables"

**Explanation inserted:** This refers to detailed records of what a software system actually does while running—the inputs it receives, outputs it produces, and intermediate states it passes through—captured during execution of a contract (an agreement with defined terms). In this context, it means precise, timestamped behavioral logs that can serve as a reference standard for comparison.

### Violation 10 — BMT-2

**Line 27:** `validating mechanistic interpretability findings`

**Fix:** Add plain-language explanation after "mechanistic interpretability"

**Explanation inserted:** This is the field of research that tries to understand how AI models work internally by identifying and analyzing the specific mathematical structures and operations inside them—similar to reverse-engineering a machine to understand each component's function.

### Violation 11 — BMT-2

**Line 32:** `researchers identify internal model structures (features, circuits, attention patterns)`

**Fix:** Add plain-language explanation after "features, circuits, attention patterns"

**Explanation inserted:** These are three types of interpretable structures found inside neural networks: features are learned detectors for specific concepts or patterns; circuits are chains of features that combine to perform a recognizable computational task; attention patterns are learned weights that determine which parts of the input the model focuses on. Together, they represent the 'wiring' researchers can observe inside a model.

### Violation 12 — BMT-2

**Line 33:** `the validation problem in mechanistic interpretability`

**Fix:** Add plain-language explanation after "validation problem in mechanistic interpretability"

**Explanation inserted:** This is the core difficulty that mechanistic interpretability research faces: identifying internal structures is not enough—researchers must prove those structures actually cause the model's external behavior, not just correlate with it by coincidence.

### Violation 13 — BMT-2

**Line 34:** `whether those structures causally relate to the behaviors they appear to explain`

**Fix:** Add plain-language explanation after "causally relate"

**Explanation inserted:** This means determining whether the internal structures actually *cause* the observed behavior, rather than just appearing alongside it—a critical distinction because correlation alone is not proof of influence.

### Violation 14 — BMT-2

**Line 37:** `Work from Anthropic and others on sparse autoencoders`

**Fix:** Add plain-language explanation after "sparse autoencoders"

**Explanation inserted:** Sparse autoencoders are machine learning tools that break down a neural network's internal decision-making into simpler, interpretable pieces—like taking a complex black box and labeling what each internal switch seems to be 'looking for.'

### Violation 15 — BMT-2

**Line 37:** `superposition (in AI: when a model represents more concepts...)`

**Fix:** Add plain-language explanation after "superposition"

**Explanation inserted:** Note: This one HAS a parenthetical gloss, so it is adequate as-is. Not flagging.

### Violation 16 — BMT-2

**Line 39:** `identify candidate features in residual stream activations`

**Fix:** Add plain-language explanation after "residual stream activations"

**Explanation inserted:** Residual stream activations are the intermediate numerical values flowing through a neural network as it processes information—the 'workspace' where the model's thinking happens step-by-step.

### Violation 17 — BMT-2

**Line 39:** `We can trace circuits — paths through the network that appear to mediate specific behaviors.`

**Fix:** Add plain-language explanation after "circuits"

**Explanation inserted:** Note: This has an inline gloss ('paths through the network that appear to mediate specific behaviors'). However, it may still benefit from clarification on *why* tracing them matters—but the gloss is present. Use judgment: flagging as borderline but the gloss is there, so NOT flagging per instructions.

### Violation 18 — BMT-2

**Line 42:** `Causal validation — establishing that a feature or circuit is not merely correlated`

**Fix:** Add plain-language explanation after "Causal validation"

**Explanation inserted:** Note: Has inline gloss. NOT flagging.

### Violation 19 — BMT-2

**Line 45:** `Most interpretability research uses behavioral probes: force the model into a situation`

**Fix:** Add plain-language explanation after "behavioral probes"

**Explanation inserted:** Note: Has inline explanation ('force the model into a situation, see what activates...'). NOT flagging.

### Violation 20 — BMT-2

**Line 45:** `see whether ablating the identified structure changes the output`

**Fix:** Add plain-language explanation after "ablating"

**Explanation inserted:** Ablating means deliberately removing or disabling a part of the model to see what changes—like removing a component from an engine to learn what it does.

### Violation 21 — BMT-2

**Line 49:** `It tracks Intent Fidelity (is the model serving the user's actual purpose?)`

**Fix:** Add plain-language explanation after "Intent Fidelity"

**Explanation inserted:** Note: Has parenthetical gloss ('is the model serving the user's actual purpose?'). NOT flagging.

### Violation 22 — BMT-2

**Line 49:** `Invariant Status (is the model honoring the hard constraints it committed to?)`

**Fix:** Add plain-language explanation after "Invariant Status"

**Explanation inserted:** Note: Has parenthetical gloss. NOT flagging.

### Violation 23 — BMT-2

**Line 49:** `V&T (Verification and Truth — a statement that explicitly separates...)`

**Fix:** Add plain-language explanation after "V&T (Verification and Truth)"

**Explanation inserted:** Note: Has inline gloss explaining the concept. NOT flagging.

### Violation 24 — BMT-2

**Line 50:** `The Contract Window produces a different kind of behavioral record. It is operational`

**Fix:** Add plain-language explanation after "operational"

**Explanation inserted:** Operational here means the record captures real, live behavior from actual use, not behavior artificially created in a controlled lab setting.

### Violation 25 — BMT-2

**Line 51:** `Anthropic's work on sparse autoencoders applied to language model activations`

**Fix:** Add plain-language explanation after "sparse autoencoders"

**Explanation inserted:** Sparse autoencoders are mathematical tools that break down a neural network's internal representations into simpler, interpretable components by identifying which features are actually being used at any moment. This matters here because it lets researchers see what features the model is relying on when it processes information.

### Violation 26 — BMT-2

**Line 51:** `has established that superposition is a real phenomenon: models represent more features than they have dimensions`

**Fix:** Add plain-language explanation after "superposition"

**Explanation inserted:** Superposition is when a neural network 'squeezes' more distinct concepts or patterns into its internal storage than it technically has room for, by overlapping them in clever ways. Understanding this helps explain how language models can handle such diverse tasks despite their architectural constraints.

### Violation 27 — BMT-2

**Line 51:** `compressed into overlapping directions in activation space`

**Fix:** Add plain-language explanation after "activation space"

**Explanation inserted:** Activation space is the multi-dimensional geometric landscape where a neural network represents information internally—think of it like a high-dimensional coordinate system where different directions represent different semantic concepts. This is where researchers look when trying to understand what the model 'knows' at any given moment.

### Violation 28 — BMT-2

**Line 56:** `The concept of attention head specialization — heads that perform identifiable functions such as induction, copying, or `

**Fix:** Add plain-language explanation after "attention head specialization"

**Explanation inserted:** Attention heads are specific components of a language model that focus on different kinds of patterns in text. Specialization means some heads consistently perform particular tasks (like copying a word from earlier in the text, or predicting what word typically comes next).

### Violation 29 — BMT-2

**Line 60:** `Contract Window status transitions might provide a behavioral signal that can be mapped against these known structures`

**Fix:** Add plain-language explanation after "Contract Window status transitions"

**Explanation inserted:** A Contract Window status transition is when the document's tracked compliance status changes categories (e.g., from STABLE to VIOLATION). This proposal treats such changes as observable signals that something shifted in how the model is processing information.

### Violation 30 — BMT-2

**Line 63:** `If Invariant Status moves from STABLE to VIOLATION across a conversation`

**Fix:** Add plain-language explanation after "Invariant Status"

**Explanation inserted:** Invariant Status is the compliance tracking system's designation of whether the model is maintaining its agreed-upon behavioral rules (STABLE) or breaking them (VIOLATION). Tracking when this changes helps the proposal connect observable compliance failures to internal model states.

### Violation 31 — BMT-2

**Line 68:** `V&T adoption behavior — whether the model differentiates verified from constructed claims`

**Fix:** Add plain-language explanation after "V&T adoption behavior"

**Explanation inserted:** V&T adoption refers to whether the model actually follows the Verification & Transparency requirement to distinguish between verified and constructed information in its responses. This is a measurable behavior that might reflect specific patterns in which parts of the model's internal attention it relies on.

### Violation 32 — BMT-2

**Line 71:** `Intent Fidelity decline over a long conversation — the model gradually drifting from the user's evident purpose`

**Fix:** Add plain-language explanation after "Intent Fidelity decline"

**Explanation inserted:** Intent Fidelity decline is when a model gradually stops following or understanding what the user actually wants and instead drifts toward its own patterns or tangents. This proposal suggests such drift might be detectable in the model's internal states before it becomes obvious in the actual output.

### Violation 33 — BMT-2

**Line 71:** `Do Invariant Status violations correlate with identifiable internal state transitions?`

**Fix:** Add plain-language explanation after "Invariant Status violations"

**Explanation inserted:** An Invariant Status violation occurs when a rule or constraint that the model is supposed to follow is broken—for example, if the model was supposed to maintain a consistent commitment but didn't. This question asks whether we can detect warning signs in the model's internal computations when such a violation is about to happen or is happening.

### Violation 34 — BMT-2

**Line 71:** `When a Contract Window record shows a transition from Invariant STABLE to Invariant VIOLATION`

**Fix:** Add plain-language explanation after "Contract Window record"

**Explanation inserted:** A Contract Window record is a logged snapshot of the model's behavior and reasoning during a specific conversation or interaction, tagged with whether the model was following its constraints (STABLE) or breaking them (VIOLATION). This gives researchers a timestamped record of when and how things went wrong.

### Violation 35 — BMT-2

**Line 73:** `Are there activation patterns, feature directions, or circuit behaviors that are reliably present at the transition and `

**Fix:** Add plain-language explanation after "activation patterns, feature directions, or circuit behaviors"

**Explanation inserted:** These are different ways to look at what the model's neural network is 'doing' internally at a given moment—which neurons are firing (activation patterns), which learned concepts are being emphasized (feature directions), and which combinations of neurons are working together to produce an output (circuit behaviors). The question is whether any of these show a consistent fingerprint right when a violation occurs.

### Violation 36 — BMT-2

**Line 79:** `This is the most tractable of the three questions because Invariant Status is discrete: STABLE or VIOLATION. That makes `

**Fix:** Add plain-language explanation after "Invariant Status is discrete: STABLE or VIOLATION. That makes it a classificatio"

**Explanation inserted:** Because Invariant Status has only two possible values (not a range or spectrum), researchers can use standard machine-learning classification techniques—training a model to predict which of the two states applies—rather than trying to predict a continuous number. This makes the analysis mathematically cleaner and more reliable.

### Violation 37 — BMT-2

**Line 85:** `Any analysis here needs to account for temporal lag between internal state change and behavioral manifestation.`

**Fix:** Add plain-language explanation after "temporal lag between internal state change and behavioral manifestation"

**Explanation inserted:** A temporal lag is a delay in time—in this case, the internal change in the model's thinking may happen several conversation turns before the actual rule-breaking behavior appears. Researchers need to account for this delay, or they might miss the true cause by looking at the wrong moment in the conversation history.

### Violation 38 — BMT-2

**Line 79:** `Do V&T adoption patterns correlate with attention head behaviors?`

**Fix:** Add plain-language explanation after "V&T adoption patterns"

**Explanation inserted:** V&T refers to a model's ability to distinguish between Verified statements (claims that can be traced back to its training data) and Truthful but constructed statements (claims the model generates that are accurate but not from its training data). Adoption patterns mean how consistently and effectively a model learns to use this distinction.

### Violation 39 — BMT-2

**Line 81:** `Do V&T adoption patterns correlate with attention head behaviors?`

**Fix:** Add plain-language explanation after "attention head behaviors"

**Explanation inserted:** Attention heads are components inside a language model that focus on specific parts of the input text when processing information; their 'behaviors' refer to which parts of the text they focus on and how that focus changes depending on what the model is doing.

### Violation 40 — BMT-2

**Line 85:** `When a model produces a V&T statement that accurately differentiates its verified from its constructed claims, what is t`

**Fix:** Add plain-language explanation after "attention pattern"

**Explanation inserted:** An attention pattern is a map showing which words or phrases in the input text the model's attention heads are focusing on at each step; it reveals which parts of the context the model considered important when making a decision.

### Violation 41 — BMT-2

**Line 88:** `A model that is correctly tracking its own epistemic status might show different attention to its "retrieved" versus "ge`

**Fix:** Add plain-language explanation after "epistemic status"

**Explanation inserted:** Epistemic status means how confident or certain a model should be about a piece of information — whether it is quoting something it learned, making an educated guess, or speculating.

### Violation 42 — BMT-2

**Line 88:** `...might show different attention to its "retrieved" versus "generated" tokens.`

**Fix:** Add plain-language explanation after "retrieved versus generated tokens"

**Explanation inserted:** Retrieved tokens are words the model pulls directly from its training data, while generated tokens are words the model creates on its own during text production; the distinction matters because retrieved content should be more reliable.

### Violation 43 — BMT-2

**Line 87:** `Can behavioral drift — declining Intent Fidelity over a long conversation`

**Fix:** Add plain-language explanation after "behavioral drift"

**Explanation inserted:** Behavioral drift means the model's responses gradually shift away from what the user actually asked for or needs, like slowly drifting off course without a sharp turn.

### Violation 44 — BMT-2

**Line 87:** `declining Intent Fidelity over a long conversation — be predicted`

**Fix:** Add plain-language explanation after "Intent Fidelity"

**Explanation inserted:** Intent Fidelity is how accurately the model stays focused on what the user actually wants, rather than substituting its own goals or patterns.

### Violation 45 — BMT-2

**Line 92:** `whether the internal state signals drift before the output does`

**Fix:** Add plain-language explanation after "internal state signals"

**Explanation inserted:** Internal state signals are measurable patterns of activity inside the model's computation — like which mathematical weights are active — that happen before you see the effects in the text it produces.

### Violation 46 — BMT-2

**Line 94:** `early internal indicators of Intent Fidelity decline — features activating, circuits engaging`

**Fix:** Add plain-language explanation after "features activating, circuits engaging"

**Explanation inserted:** These are specific measurable changes in how the model processes information internally (analogous to which neurons fire in a brain), which might warn us of problems before they appear in the output.

### Violation 47 — BMT-2

**Line 96:** `a meaningful finding for runtime monitoring`

**Fix:** Add plain-language explanation after "runtime monitoring"

**Explanation inserted:** Runtime monitoring means watching the model while it is actively generating responses, so problems can be caught and corrected in real time rather than after the fact.

### Violation 48 — BMT-2

**Line 98:** `requires longitudinal conversation data with annotated Intent Fidelity scores`

**Fix:** Add plain-language explanation after "longitudinal conversation data"

**Explanation inserted:** Longitudinal conversation data means tracking the same conversations over many turns (like watching someone's behavior unfold over time), with expert human judgments about whether the model is staying true to the user's intent at each step.

### Violation 49 — BMT-2

**Line 99:** `This proposal is not claiming that Contract Window observables are a better...`

**Fix:** Add plain-language explanation after "Contract Window observables"

**Explanation inserted:** Contract Window observables are records of system behavior captured at defined points during a model's operation, used to track what the system actually does rather than how it works internally.

### Violation 50 — BMT-2

**Line 100:** `Activation patching, logit lens, sparse autoencoders — these are purpose-built...`

**Fix:** Add plain-language explanation after "Activation patching"

**Explanation inserted:** Activation patching is a technique where researchers modify the internal computational states of a neural network to see how changes affect outputs, helping them understand which internal components matter for specific behaviors.

### Violation 51 — BMT-2

**Line 100:** `Activation patching, logit lens, sparse autoencoders — these are purpose-built...`

**Fix:** Add plain-language explanation after "logit lens"

**Explanation inserted:** Logit lens is a method that examines the internal representations at each layer of a neural network to understand what predictions the model is 'leaning toward' at different depths of computation.

### Violation 52 — BMT-2

**Line 100:** `Activation patching, logit lens, sparse autoencoders — these are purpose-built...`

**Fix:** Add plain-language explanation after "sparse autoencoders"

**Explanation inserted:** Sparse autoencoders are machine learning models that compress and decompose the complex internal activity of neural networks into simpler, more interpretable components.

### Violation 53 — BMT-2

**Line 105:** `What the proposal claims is that the behavioral record produced by Contract...`

**Fix:** Add plain-language explanation after "behavioral record"

**Explanation inserted:** A behavioral record is a documented collection of the actual outputs and actions a system produces, capturing what it does rather than explaining why or how it works internally.

### Violation 54 — BMT-2

**Line 105:** `...behavioral record produced by Contract Window governance is structurally suited to serve as validation signal...`

**Fix:** Add plain-language explanation after "validation signal"

**Explanation inserted:** A validation signal is information or evidence that confirms whether an interpretation or explanation of a system's behavior is accurate.

### Violation 55 — BMT-2

**Line 106:** `It is a bridge between the behavioral layer and the mechanistic layer...`

**Fix:** Add plain-language explanation after "mechanistic layer"

**Explanation inserted:** The mechanistic layer refers to the internal mathematical operations and component interactions that produce a system's behavior—how the system actually works at a technical level.

### Violation 56 — BMT-2

**Line 108:** `mechanistic interpretability has reached the point where it produces claims specific enough to test`

**Fix:** Add plain-language explanation after "mechanistic interpretability"

**Explanation inserted:** Mechanistic interpretability is the field of research that tries to understand how AI models work by examining their internal computational mechanisms—similar to reverse-engineering a piece of software to see exactly what steps it takes to produce an output.

### Violation 57 — BMT-2

**Line 111:** `The work from 2023-2025 on sparse autoencoders and feature geometry is specific enough`

**Fix:** Add plain-language explanation after "sparse autoencoders"

**Explanation inserted:** Sparse autoencoders are a type of AI analysis tool that breaks down a model's internal representations into a small number of meaningful, human-interpretable components—think of it like decomposing a complex image into individual recognizable objects rather than leaving it as a blur of pixels.

### Violation 58 — BMT-2

**Line 111:** `The work from 2023-2025 on sparse autoencoders and feature geometry is specific enough`

**Fix:** Add plain-language explanation after "feature geometry"

**Explanation inserted:** Feature geometry refers to the mathematical arrangement and relationships between these interpretable components in the model's internal space—essentially, how these meaningful pieces are organized relative to each other in a way that affects the model's behavior.

### Violation 59 — BMT-2

**Line 117:** `Contract Window as a structured behavioral framework is recent.`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** Contract Window is (based on context) a framework for systematically recording and analyzing specific moments when an AI model either follows or violates its stated rules or constraints during operation.

### Violation 60 — BMT-2

**Line 115:** `citations to Anthropic interpretability work (Bricken, Templeton, Olsson)…`

**Fix:** Add plain-language explanation after "mechanistic interpretability"

**Explanation inserted:** Mechanistic interpretability is the research field that tries to understand how AI systems make decisions by examining the internal mathematical operations and patterns inside them, rather than just looking at their inputs and outputs.

### Violation 61 — BMT-2

**Line 120:** `structural description of Contract Window observables (Intent Fidelity…`

**Fix:** Add plain-language explanation after "Contract Window observables"

**Explanation inserted:** Contract Window observables are measurable signals or states within an AI system that indicate whether the system is staying aligned with its intended purpose; they are the specific things you can check to verify the system is behaving as designed.

### Violation 62 — BMT-2

**Line 120:** `Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption)`

**Fix:** Add plain-language explanation after "Intent Fidelity"

**Explanation inserted:** Intent Fidelity measures how closely the AI system's actual behavior matches what it was intended to do—essentially, how well it stays true to its original purpose.

### Violation 63 — BMT-2

**Line 120:** `Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption)`

**Fix:** Add plain-language explanation after "Invariant Status"

**Explanation inserted:** Invariant Status tracks whether key properties or rules that should never change within the system remain stable and unbroken over time.

### Violation 64 — BMT-2

**Line 120:** `Contract Window observables (Intent Fidelity, Invariant Status, V&T adoption)`

**Fix:** Add plain-language explanation after "V&T adoption"

**Explanation inserted:** V&T adoption refers to how widely or thoroughly the system has integrated the verification and transparency framework described in this proposal.

### Violation 65 — BMT-2

**Line 123:** `no data exists yet showing that Contract Window observables correlate…`

**Fix:** Add plain-language explanation after "internal state transitions"

**Explanation inserted:** Internal state transitions are shifts in the system's underlying computational configuration—the moment when internal patterns or operations change from one stable mode to another.

### Violation 66 — BMT-2

**Line 124:** `connection between V&T adoption and attention head behavior is speculative`

**Fix:** Add plain-language explanation after "attention head behavior"

**Explanation inserted:** Attention heads are specific mathematical components inside transformer-based AI models that learn to focus on certain parts of the input when making decisions; their behavior refers to which parts they prioritize and how that prioritization changes.

### Violation 67 — BMT-2

**Line 125:** `behavioral drift can be predicted from internal signals before output…`

**Fix:** Add plain-language explanation after "behavioral drift"

**Explanation inserted:** Behavioral drift is when an AI system's outputs and decisions gradually shift away from its original intended behavior, usually without any explicit change to its code or training.
