# BMT Audit Report

**File:** executive-summary-proposal.md
**Audited:** 2026-05-01T07:54:11.121840+00:00
**Violations found:** 118 (BMT-1: 5, BMT-2: 113, BMT-4: 0)
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
| 1 | 7 | **The Living Constitution (TLC)** is a runtime enforcement system built alongside this research — a  | Define "TLC" on first use: TLC (The Living Constitution — the runtime enforcement system built along |
| 2 | 60 | - Which epistemic commitments are active and whether they have been violated (Invariant Status) | Define "Invariant Status" on first use: Invariant Status (whether the hard behavioral rules the AI c |
| 3 | 132 | Contract Window outputs formatted to accessibility-grade readability standards (Flesch-Kincaid Grade | Define "Flesch-Kincaid" on first use: Flesch-Kincaid Grade Level (a readability score — Grade 8 mean |
| 4 | 189 | Black women's health disparities, specifically Graves' disease. Narrative-first CRISP-DM (Cross-Indu | Define "CRISP-DM" on first use: CRISP-DM (Cross-Industry Standard Process for Data Mining — a standa |
| 5 | 199 | ### Scalable Oversight (a research area focused on how humans can supervise AI systems even when tho | Define "Scalable Oversight" on first use: scalable oversight (a research area focused on how humans  |

### BMT-2 Violations (Concepts Without Plain-Language Explanation)

These are the deeper violations — the standard exposed by the ChatGPT
translation benchmark. Each item below is a concept that was introduced
without the follow-up sentence a zero-prior-knowledge reader needs.

| # | Line | Concept | Explanation Inserted |
|---|------|---------|----------------------|
| 1 | 7 | Governing the Investigative Arc: A Contract Window | An investigative arc is the sequence of steps a human and AI take together to explore a question or  |
| 2 | 7 | A Contract Window (a structured record of what a human-AI session is trying to a | While a parenthetical is present, 'Contract Window' needs clarification on why it's called a 'window |
| 3 | 9 | Architecture for Cognitive Safety in Human-AI Collaboration | Cognitive safety refers to protecting human thinking and decision-making from being misled, manipula |
| 4 | 15 | The Living Constitution (TLC) is a runtime enforcement system built alongside th | Constitutional rules are principles or constraints that govern how an AI system should behave, simil |
| 5 | 15 | a software layer that applies constitutional rules to AI behavior session by ses | Runtime enforcement means the rules are checked and applied continuously while the AI is actually wo |
| 6 | 26 | I call this **Insight Atrophy (the gradual erosion of a person's ability to ques | This is actually already defined in parentheses, but the definition itself contains an unexplained p |
| 7 | 31 | It pattern-matches to adjacent surface features and produces outputs that are lo | This means the model recognizes features in the input that resemble patterns it has seen before, the |
| 8 | 33 | ...indistinguishable from correct answers without domain-specific interrogation. | This refers to asking detailed, expert-level questions that require specialized knowledge in a parti |
| 9 | 39 | That record is what I call the **Contract Window**. | The term is introduced but not explained. Based on context, it appears to be a shared record between |
| 10 | 42 | ...operationalized through accessibility-grade runtime invariants... | This phrase combines three unexplained terms. 'Runtime' means during active use; 'invariants' are ru |
| 11 | 43 | ...statistically improves **Intent Fidelity (whether the AI is still serving the | This is defined parenthetically, but 'drifting toward adjacent goals' is vague. The reader should un |
| 12 | 37 | Standard AI safety evaluation asks: did the model produce a harmful output? | This means checking only whether the final answer the AI gives is harmful or not, without looking at |
| 13 | 39 | There is a second-order failure mode that does not appear in output-level evalua | This is a problem that doesn't show up when you just check if outputs are bad—it's a harmful effect  |
| 14 | 41 | They stop generating competing interpretations. They stop asking the questions t | The human's set of possible explanations for a problem shrinks, meaning they consider fewer alternat |
| 15 | 42 | The model has not hallucinated in the classical sense. | In AI terminology, hallucination means the model invents false information that sounds plausible; he |
| 16 | 47 | Long interactions (the model's framing accumulates and shapes the human's questi | Extended back-and-forth conversations where the model's earlier answers bias how the human asks foll |
| 17 | 46 | The classical hallucination frame treats model errors as identifiable fabricatio | This refers to the standard way people think about AI mistakes—as obvious, detectable errors or made |
| 18 | 47 | The more insidious failure mode is the structurally correct-sounding answer that | A failure mode is a specific type of error or malfunction. In this case, it means the AI produces an |
| 19 | 50 | ...behavior, language, or decision patterns operate through interpretive framewo | This means the set of cultural assumptions, values, or mental models that a group uses to understand |
| 20 | 65 | It does not address runtime governance: the question of whether... | Runtime governance means rules and oversight that apply while the AI is actively working with a user |
| 21 | 68 | What the investigation is and what it is trying to establish (Task State) | Task State is a record of what the investigation is supposed to accomplish and what specific claims  |
| 22 | 69 | Which epistemic commitments are active and whether they have been violated | Epistemic commitments are the factual or logical assumptions the investigation has agreed to treat a |
| 23 | 69 | Which epistemic commitments are active and whether they have been violated (Inva | Invariant Status is a record of which commitments remain in effect and whether any have been broken, |
| 24 | 70 | What has broken and who bears the obligation to repair it (Repair Obligations) | Repair Obligations is a record of what has gone wrong—such as a violated commitment or factual error |
| 25 | 71 | What has been verified, what is contested, what is unknown (Truth Status) | Truth Status is a classification of each claim or piece of evidence as either confirmed, disputed am |
| 26 | 73 | This four-field structure is the Contract Window. | The Contract Window is the proposed name for a unified, visible record that displays all four fields |
| 27 | 75 | It is a runtime artifact that both human and model can read | A runtime artifact is information that exists and can be accessed during the actual execution of a c |
| 28 | 76 | transforms the interaction from a request-response exchange into a governed inve | This means the conversation follows a structured path with rules and checkpoints, rather than being  |
| 29 | 86 | Which epistemic commitments are active | Epistemic commitments are specific promises the AI makes about how it will reason, what it will and  |
| 30 | 89 | Verified / contested / unknown / Phantom confidence, invisible epistemic gaps | Phantom confidence means the AI sounds certain about something when it actually has no solid basis f |
| 31 | 93 | It was co-designed with frontier AI systems. | Frontier AI systems are the most advanced, cutting-edge AI models currently available—systems operat |
| 32 | 94 | what would a Level-5 intelligence entity — meaning a system operating at its hig | This phrase is already glossed in the text, so no additional explanation needed. |
| 33 | 96 | maintain coherence, fidelity, and safety | Coherence means the AI's reasoning stays logically consistent; fidelity means it stays true to its s |
| 34 | 98 | are candidates for formal invariant status | Formal invariant status means treating something as a permanent, non-negotiable rule that must be pr |
| 35 | 89 | Does this output serve the investigative arc? Does it advance... | The investigative arc is the thread of inquiry or line of questioning that the human is pursuing; se |
| 36 | 90 | Does it introduce a phantom claim, a silent assumption, or... | A phantom claim is a statement that sounds factual but has no real basis — it appears confident and  |
| 37 | 90 | Does it introduce a phantom claim, a silent assumption, or... | A silent assumption is a premise the output takes for granted without stating it explicitly; the rea |
| 38 | 90 | Does it introduce a phantom claim, a silent assumption, or fluent wrong answer? | A fluent wrong answer is a response that reads smoothly and confidently but is factually incorrect;  |
| 39 | 94 | It operationalizes the dual-newspaper test — a standard from... | The dual-newspaper test is a simple fairness check: would you be comfortable seeing this output prin |
| 40 | 95 | ...at the inference layer, per turn, with an auditable record. | The inference layer is the moment when the AI system generates and delivers its response to the user |
| 41 | 95 | [CONSTRUCTED — operationalized from longitudinal observation, pending formal exp | This means the six rules were derived by watching how a system performed over time rather than being |
| 42 | 97 | I1 — Evidence-First Outputs: Every claim tagged with its evidence basis | Each statement the system makes must be labeled to show where it came from: VERIFIED means it's back |
| 43 | 98 | I2 — No Phantom Work: No performance claims without named methodology, baseline, | This term means claiming that something works well without actually explaining how it was tested, wh |
| 44 | 99 | I3 — Confidence Requires Verification: Hedged language is not a substitute for v | Hedged language means using cautious phrases like 'may possibly' or 'might potentially' to sound mor |
| 45 | 102 | I6 — Fail Closed: When in doubt, stop and flag — do not proceed | This is a safety principle meaning that if the system is uncertain whether something is correct or s |
| 46 | 108 | structured epistemic hygiene statement: | This means a clearly marked statement that shows what information is reliable, what sources were che |
| 47 | 113 | frontier models (a state-of-the-art AI system at the edge of current capability) | This parenthetical gloss is present but uses technical language ('state-of-the-art', 'edge of curren |
| 48 | 115 | This emergent adoption pattern is documented | This phrase describes when multiple AI systems independently began doing something similar without b |
| 49 | 122 | Sessions governed by an active Contract Window will show... | A Contract Window is a structured, machine-readable agreement that specifies what the AI model is su |
| 50 | 122 | ...show a ≥25% reduction in intent-drift incidents... | An intent-drift incident occurs when the AI starts answering questions or pursuing goals that differ |
| 51 | 122 | ...compared to unstructured baseline sessions. | Unstructured baseline sessions are normal conversations where there is no Contract Window or formal  |
| 52 | 130 | Sessions with bilateral intelligibility — human and model both... | Bilateral intelligibility means both the human and the AI can read, understand, and actively use the |
| 53 | 130 | ...relative to unilateral or no-invariant conditions. | Unilateral conditions are when only one party (human or AI) can see and use the Contract Window; no- |
| 54 | 136 | ...Flesch-Kincaid Grade 8 or below — meaning the text... | The Flesch-Kincaid Grade 8 standard is already adequately explained in the inline parenthetical, so  |
| 55 | 136 | ...with visual state indicators) will enable lay readers... | Visual state indicators are graphical symbols, colors, or icons that quickly show the current status |
| 56 | 138 | 6-condition between-subjects experiment | Each participant or session is assigned to only one condition, and results are compared across diffe |
| 57 | 145 | Condition 2: Contract Window only | A governance component (explained in Section 3) that limits the scope or duration of interaction wit |
| 58 | 146 | Condition 3: Bilateral intelligibility only | A governance component that ensures both the human operator and the AI system can understand each ot |
| 59 | 147 | Condition 4: Accessibility-grade invariants only | A governance component that maintains consistent, easy-to-understand constraints or rules that remai |
| 60 | 148 | Condition 5: Backwards Instructional Design (BID) only | A governance component that structures interactions by defining the desired outcome first, then work |
| 61 | 154 | Powered for Cohen's d=0.5 at α=0.05, 80% power | A statistical measure of effect size indicating the minimum meaningful difference between conditions |
| 62 | 154 | Powered for Cohen's d=0.5 at α=0.05, 80% power | The significance level threshold; if the p-value falls below 0.05, results are considered statistica |
| 63 | 154 | Powered for Cohen's d=0.5 at α=0.05, 80% power | The probability that the experiment will detect a real difference of the specified size if one exist |
| 64 | 156 | Outcome measures: Intent-drift incident rate, drift repair rate, session-state c | The frequency with which the AI system's behavior or goals diverge from what the human operator inte |
| 65 | 156 | Outcome measures: Intent-drift incident rate, drift repair rate, session-state c | How quickly and successfully the system corrects itself or is corrected when it has drifted from the |
| 66 | 156 | session-state comprehension accuracy (lay rater) | Whether a person without specialized AI knowledge can accurately understand and summarize what the A |
| 67 | 156 | Insight Atrophy index (to be operationalized — see Section 6, Limitations) | A measurement (not yet fully defined) of whether the quality or depth of analytical insights produce |
| 68 | 160 | stratified random assignment on operator cognitive load profile | Sessions are randomly assigned to conditions, but with a deliberate structure: groups are first orga |
| 69 | 160 | stratified random assignment on operator cognitive load profile (neurodivergent  | A classification of each human operator's typical mental processing style—whether they are neurodive |
| 70 | 165 | Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured c | Insight Atrophy refers to the degradation or loss of analytical ability and depth of understanding o |
| 71 | 165 | Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured c | Intent Fidelity measures how faithfully and consistently an AI system executes or represents what a  |
| 72 | 175 | Eight behavioral patterns (the Eight Wonders) are formalized as Generative Epist | Generative Epistemic Invariants are repeatable, observable behavioral patterns that reliably reveal  |
| 73 | 169 | they cannot read the interpretive architecture — what this paper calls the Relat | The Relational Economy is the system of meaning-making and trust-building that operates within a com |
| 74 | 178 | 5. The Side-Eye (Hypervigilant Trust Calibration) | Hypervigilant Trust Calibration describes the careful, continuous assessment of whether someone or a |
| 75 | 189 | Black women's health disparities, specifically Graves' disease. | Graves' disease is an autoimmune condition where the immune system attacks the thyroid gland, causin |
| 76 | 189 | a population whose symptoms are systematically undertriaged | Undertriage means a patient's condition is classified as less urgent or serious than it actually is, |
| 77 | 193 | Standard analytical frameworks produce Insight Atrophy when applied to populatio | Insight Atrophy occurs when an analytical system becomes progressively less useful or accurate becau |
| 78 | 194 | The Contract Window is the governance mechanism that makes the gap visible and r | The Contract Window is a governance tool designed to identify and document places where a system's a |
| 79 | 201 | ...where the epistemic chain broke — without reading the full... | An epistemic chain is the sequence of reasoning steps and evidence that led to a conclusion. When it |
| 80 | 200 | ...a compressed, human-readable session state that lets an... | This is a summary version of an AI conversation that removes unnecessary details while keeping the k |
| 81 | 203 | models can be trained to evaluate outputs against constitutional principles | Constitutional principles are rules or values that an AI system is designed to follow—in this case,  |
| 82 | 204 | the Contract Window is a per-session constitution, auditable per-turn | A Contract Window is a set of behavioral rules that applies to one conversation session with a user; |
| 83 | 204 | Contract Window is a per-session constitution, auditable per-turn, contestable | A per-session constitution means the set of rules is specific to one conversation and can be changed |
| 84 | 204 | auditable per-turn, contestable by the human operator, and repairable | Contestable means the human user can challenge or disagree with the rules in place and request that  |
| 85 | 205 | The invariants (I1–I6) map directly to Anthropic's published commitments | Invariants are specific rules or constraints that must always hold true during operation; in this ca |
| 86 | 205 | enforce them as runtime observables rather than training-time inferences | Runtime observables are measurable, checkable behaviors that happen when the model is actually respo |
| 87 | 207 | The Bicameral Review mechanism and the Invariant Status field create... | This is a two-stage approval process where constitutional constraints are checked twice—once on init |
| 88 | 207 | The Bicameral Review mechanism and the Invariant Status field create... | A data field that records whether each constitutional constraint passed or failed during evaluation, |
| 89 | 208 | ...which constitutional constraints were evaluated and whether they cleared... | Rules or requirements that the model's outputs must satisfy—for example, 'do not generate harmful co |
| 90 | 209 | ...without access to weights or activations. | Weights are the numerical parameters inside a model that control its behavior; activations are the i |
| 91 | 210 | ...by providing a behavioral signal to validate against internal state observati | Observable outputs and decisions made by the model at runtime that researchers can use to check whet |
| 92 | 224 | ...wrong in ways the operator cannot detect without a governance layer they do n | A governance layer is a set of rules, checks, or oversight processes that someone applies to an AI s |
| 93 | 228 | ...operationalizes I2 (No Phantom Work) and I3 (Confidence Requires Verification | These are two rules from the author's framework: I2 means that AI systems should not perform hidden  |
| 94 | 230 | ...why the Contract Window has four fields instead of fourteen — every element h | The Contract Window is a tool or interface in the author's framework that captures key information a |
| 95 | 232 | ...institution had no interpretive framework for what was actually happening to  | An interpretive framework is a structured way of understanding and explaining a situation so that wh |
| 96 | 232 | The invariant set and Contract Window architecture are derived from... | An invariant set is a collection of conditions or states that remain stable or unchanged even as a s |
| 97 | 232 | The invariant set and Contract Window architecture are derived from... | Contract Window architecture is the structural design of time-bounded operational agreements; it def |
| 98 | 234 | The hypotheses are falsifiable; the evidence is CONSTRUCTED, not VERIFIED. | Falsifiable means a hypothesis can be proven wrong through evidence or testing; if something is fals |
| 99 | 236 | Insight Atrophy index not yet operationalized: H1 names the construct... | The Insight Atrophy index is a proposed measurement of how quickly or severely useful knowledge or c |
| 100 | 237 | ...the measurement instrument has not been validated. Operationalization is a fi | Operationalized means converted from a theoretical idea into a concrete, measurable procedure that c |
| 101 | 239 | ...tested against an external sample for coverage or discriminant validity. | Discriminant validity is the property of measuring one distinct concept and not accidentally overlap |
| 102 | 245 | The governance-kernel implementation in this repository is a research prototype. | A governance-kernel implementation is the core software code that enforces rules and decision-making |
| 103 | 245 | It has not been tested under production load, adversarial inputs, or multi-agent | Production load means the volume and intensity of real-world usage and transactions that a system mu |
| 104 | 245 | It has not been tested under production load, adversarial inputs, or multi-agent | Adversarial inputs are deliberately malicious or edge-case requests designed to break or exploit a s |
| 105 | 245 | ...adversarial inputs, or multi-agent deployment at scale. | Multi-agent deployment at scale means running the system with many independent actors or systems int |
| 106 | 251 | The governance-kernel implementation, datasets, and case-law artifacts are being | A governance-kernel is the core set of rules and decision-making procedures that will enforce the ov |
| 107 | 251 | The governance-kernel implementation, datasets, and case-law artifacts are being | Case-law artifacts are documented examples of past decisions and rulings that will be used to train  |
| 108 | 269 | [PENDING — full citation list to be verified per Citation Research Protocol befo | The Citation Research Protocol is an internal procedure for confirming that all cited sources are ac |
| 109 | 284 | VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living- | Session memory refers to notes and context from working meetings where this proposal was discussed a |
| 110 | 284 | VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living- | The-living-constitution repo is a separate repository containing documents about how governance rule |
| 111 | 284 | VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living- | The crsp-afs-2026 repo is another working repository that this proposal has been cross-checked again |
| 112 | 285 | all hypotheses labeled CONSTRUCTED/PENDING | CONSTRUCTED/PENDING means the claims in this proposal are theoretical or proposed scenarios that hav |
| 113 | 285 | WorldMart dataset (conceptual framing device, not existing public dataset) | WorldMart is a fictional example dataset used in this proposal to illustrate how the governance syst |

#### Full BMT-2 Explanations Inserted

**1. Line 7 — Governing the Investigative Arc: A Contract Window**

Inserted: An investigative arc is the sequence of steps a human and AI take together to explore a question or solve a problem, from the initial goal through verification of results. It describes the full journey of collaborative work.

**2. Line 7 — A Contract Window (a structured record of what a human-AI se**

Inserted: While a parenthetical is present, 'Contract Window' needs clarification on why it's called a 'window' and why the metaphor of a contract matters—it should specify that it's a transparent, auditable boundary defining mutual obligations between human and AI.

**3. Line 9 — Architecture for Cognitive Safety in Human-AI Collaboration**

Inserted: Cognitive safety refers to protecting human thinking and decision-making from being misled, manipulated, or corrupted by AI outputs or advice. It ensures humans can verify and trust what an AI tells them.

**4. Line 15 — The Living Constitution (TLC) is a runtime enforcement syste**

Inserted: Constitutional rules are principles or constraints that govern how an AI system should behave, similar to how a constitution guides government—they define what the AI is and is not allowed to do in each session.

**5. Line 15 — a software layer that applies constitutional rules to AI beh**

Inserted: Runtime enforcement means the rules are checked and applied continuously while the AI is actually working, moment by moment, rather than being enforced only before or after the session ends.

**6. Line 26 — I call this **Insight Atrophy (the gradual erosion of a pers**

Inserted: This is actually already defined in parentheses, but the definition itself contains an unexplained prerequisite: 'fluent but wrong answers' — answers that sound confident and well-written but are factually incorrect. The reader should understand why fluency (smoothness of language) makes the problem worse, not better.

**7. Line 31 — It pattern-matches to adjacent surface features and produces**

Inserted: This means the model recognizes features in the input that resemble patterns it has seen before, then generates output based on surface similarities rather than deep understanding — like recognizing keywords without grasping what the user actually needs.

**8. Line 33 — ...indistinguishable from correct answers without domain-spe**

Inserted: This refers to asking detailed, expert-level questions that require specialized knowledge in a particular field — the kind of scrutiny only someone trained in that area can apply.

**9. Line 39 — That record is what I call the **Contract Window**.**

Inserted: The term is introduced but not explained. Based on context, it appears to be a shared record between human and AI of their investigation's current state, but the executive summary does not spell out what that means operationally or why it is called a 'contract.'

**10. Line 42 — ...operationalized through accessibility-grade runtime invar**

Inserted: This phrase combines three unexplained terms. 'Runtime' means during active use; 'invariants' are rules that stay constant; 'accessibility-grade' is unclear — it may mean designed to be usable by people with disabilities, but that connection is not stated.

**11. Line 43 — ...statistically improves **Intent Fidelity (whether the AI **

Inserted: This is defined parenthetically, but 'drifting toward adjacent goals' is vague. The reader should understand: as a conversation progresses, the AI may subtly shift focus toward tasks that are close to, but not exactly, what the user asked for — and Intent Fidelity measures whether that drift is happening.

**12. Line 37 — Standard AI safety evaluation asks: did the model produce a **

Inserted: This means checking only whether the final answer the AI gives is harmful or not, without looking at how the AI arrived at that answer or what damage might occur indirectly.

**13. Line 39 — There is a second-order failure mode that does not appear in**

Inserted: This is a problem that doesn't show up when you just check if outputs are bad—it's a harmful effect that happens one step removed from the obvious outputs.

**14. Line 41 — They stop generating competing interpretations. They stop as**

Inserted: The human's set of possible explanations for a problem shrinks, meaning they consider fewer alternative theories and stop exploring different possibilities.

**15. Line 42 — The model has not hallucinated in the classical sense.**

Inserted: In AI terminology, hallucination means the model invents false information that sounds plausible; here the author is distinguishing Insight Atrophy from that traditional error.

**16. Line 47 — Long interactions (the model's framing accumulates and shape**

Inserted: Extended back-and-forth conversations where the model's earlier answers bias how the human asks follow-up questions, making them less likely to challenge the model's framing.

**17. Line 46 — The classical hallucination frame treats model errors as ide**

Inserted: This refers to the standard way people think about AI mistakes—as obvious, detectable errors or made-up information. The problem this section raises is that this frame misses a different, harder-to-spot kind of failure.

**18. Line 47 — The more insidious failure mode is the structurally correct-**

Inserted: A failure mode is a specific type of error or malfunction. In this case, it means the AI produces answers that sound reasonable and well-structured but are actually wrong in ways only an expert in that field would catch.

**19. Line 50 — ...behavior, language, or decision patterns operate through **

Inserted: This means the set of cultural assumptions, values, or mental models that a group uses to understand the world—for example, different communities may interpret authority, time, or family relationships differently than what appeared in the model's training data.

**20. Line 65 — It does not address runtime governance: the question of whet**

Inserted: Runtime governance means rules and oversight that apply while the AI is actively working with a user, moment-by-moment, rather than rules baked in during training. It's about checking whether the AI is staying on track for the specific task at hand.

**21. Line 68 — What the investigation is and what it is trying to establish**

Inserted: Task State is a record of what the investigation is supposed to accomplish and what specific claims or questions it is trying to answer. It serves as the reference point to check whether the AI is working toward the right goal.

**22. Line 69 — Which epistemic commitments are active and whether they have**

Inserted: Epistemic commitments are the factual or logical assumptions the investigation has agreed to treat as true or binding—for example, 'we are assuming this document is authentic' or 'we have committed to the scientific method for testing this hypothesis.' Tracking them prevents the investigation from contradicting itself.

**23. Line 69 — Which epistemic commitments are active and whether they have**

Inserted: Invariant Status is a record of which commitments remain in effect and whether any have been broken, so that violations can be detected and addressed rather than ignored.

**24. Line 70 — What has broken and who bears the obligation to repair it (R**

Inserted: Repair Obligations is a record of what has gone wrong—such as a violated commitment or factual error—and which party (the AI, the human investigator, or the data source) is responsible for fixing it. This prevents problems from being swept under the rug.

**25. Line 71 — What has been verified, what is contested, what is unknown (**

Inserted: Truth Status is a classification of each claim or piece of evidence as either confirmed, disputed among the participants, or still unclear, so that the investigation can distinguish solid findings from remaining open questions.

**26. Line 73 — This four-field structure is the Contract Window.**

Inserted: The Contract Window is the proposed name for a unified, visible record that displays all four fields together (Task State, Invariant Status, Repair Obligations, and Truth Status) so that both the human and the AI can monitor whether the investigation is staying true to its original terms and assumptions.

**27. Line 75 — It is a runtime artifact that both human and model can read**

Inserted: A runtime artifact is information that exists and can be accessed during the actual execution of a conversation, rather than being set up beforehand or stored separately—think of it like a shared notepad that stays visible throughout your entire interaction.

**28. Line 76 — transforms the interaction from a request-response exchange **

Inserted: This means the conversation follows a structured path with rules and checkpoints, rather than being a simple back-and-forth where each response stands alone.

**29. Line 86 — Which epistemic commitments are active**

Inserted: Epistemic commitments are specific promises the AI makes about how it will reason, what it will and won't claim to know, and what logical rules it will follow during the conversation.

**30. Line 89 — Verified / contested / unknown | Phantom confidence, invisib**

Inserted: Phantom confidence means the AI sounds certain about something when it actually has no solid basis for that certainty—it's a trap where false confidence goes undetected.

**31. Line 93 — It was co-designed with frontier AI systems.**

Inserted: Frontier AI systems are the most advanced, cutting-edge AI models currently available—systems operating at or near the current technological frontier.

**32. Line 94 — what would a Level-5 intelligence entity — meaning a system **

Inserted: This phrase is already glossed in the text, so no additional explanation needed.

**33. Line 96 — maintain coherence, fidelity, and safety**

Inserted: Coherence means the AI's reasoning stays logically consistent; fidelity means it stays true to its stated commitments and constraints; safety means it avoids harmful outputs and maintains control.

**34. Line 98 — are candidates for formal invariant status**

Inserted: Formal invariant status means treating something as a permanent, non-negotiable rule that must be preserved throughout the entire system's operation, rather than as a suggestion or preference.

**35. Line 89 — Does this output serve the investigative arc? Does it advanc**

Inserted: The investigative arc is the thread of inquiry or line of questioning that the human is pursuing; serving it means the output moves that specific inquiry forward rather than distracting from it or making it harder to follow.

**36. Line 90 — Does it introduce a phantom claim, a silent assumption, or..**

Inserted: A phantom claim is a statement that sounds factual but has no real basis — it appears confident and coherent but is actually made up or unsupported by evidence.

**37. Line 90 — Does it introduce a phantom claim, a silent assumption, or..**

Inserted: A silent assumption is a premise the output takes for granted without stating it explicitly; the reader may not realize the output is built on an unproven or contestable foundation.

**38. Line 90 — Does it introduce a phantom claim, a silent assumption, or f**

Inserted: A fluent wrong answer is a response that reads smoothly and confidently but is factually incorrect; it sounds plausible and well-reasoned even though it is false.

**39. Line 94 — It operationalizes the dual-newspaper test — a standard from**

Inserted: The dual-newspaper test is a simple fairness check: would you be comfortable seeing this output printed in two major newspapers, one asking 'Is this harmful?' and one asking 'Is this needlessly unhelpful?' — both must answer 'no' for the output to pass.

**40. Line 95 — ...at the inference layer, per turn, with an auditable recor**

Inserted: The inference layer is the moment when the AI system generates and delivers its response to the user; checking at this layer means the review happens in real time, for each individual response, rather than after the fact.

**41. Line 95 — [CONSTRUCTED — operationalized from longitudinal observation**

Inserted: This means the six rules were derived by watching how a system performed over time rather than being designed theoretically first. The authors observed patterns in real outputs and then formalized them into these six rules.

**42. Line 97 — I1 — Evidence-First Outputs: Every claim tagged with its evi**

Inserted: Each statement the system makes must be labeled to show where it came from: VERIFIED means it's backed by reliable data or sources, CONSTRUCTED means it was reasoned or inferred by the model, and PENDING means it hasn't been checked yet.

**43. Line 98 — I2 — No Phantom Work: No performance claims without named me**

Inserted: This term means claiming that something works well without actually explaining how it was tested, what it was compared against, or what data was used—in other words, making impressive-sounding claims without proof.

**44. Line 99 — I3 — Confidence Requires Verification: Hedged language is no**

Inserted: Hedged language means using cautious phrases like 'may possibly' or 'might potentially' to sound more careful; this invariant says that vague qualification alone does not count as real verification or proof.

**45. Line 102 — I6 — Fail Closed: When in doubt, stop and flag — do not proc**

Inserted: This is a safety principle meaning that if the system is uncertain whether something is correct or safe, it should stop and alert a human rather than make a guess and continue forward.

**46. Line 108 — structured epistemic hygiene statement:**

Inserted: This means a clearly marked statement that shows what information is reliable, what sources were checked, and what claims are NOT being made—essentially a quality-control label for the accuracy and limits of the output.

**47. Line 113 — frontier models (a state-of-the-art AI system at the edge of**

Inserted: This parenthetical gloss is present but uses technical language ('state-of-the-art', 'edge of current capability') that still may not clarify why these specific models matter for this observation; a plainer version: 'the most advanced AI systems available at the time of testing.'

**48. Line 115 — This emergent adoption pattern is documented**

Inserted: This phrase describes when multiple AI systems independently began doing something similar without being instructed to do so, suggesting the behavior arose spontaneously from their own reasoning rather than being programmed in—it's significant because it suggests the models discovered this verification practice on their own.

**49. Line 122 — Sessions governed by an active Contract Window will show...**

Inserted: A Contract Window is a structured, machine-readable agreement that specifies what the AI model is supposed to do, what rules it must follow, and what the human user's goals are for the conversation, displayed in a way both human and AI can access and refer back to.

**50. Line 122 — ...show a ≥25% reduction in intent-drift incidents...**

Inserted: An intent-drift incident occurs when the AI starts answering questions or pursuing goals that differ from what the human actually asked for, causing the conversation to veer off course.

**51. Line 122 — ...compared to unstructured baseline sessions.**

Inserted: Unstructured baseline sessions are normal conversations where there is no Contract Window or formal specification of rules and goals—they serve as the control group to measure improvement against.

**52. Line 130 — Sessions with bilateral intelligibility — human and model bo**

Inserted: Bilateral intelligibility means both the human and the AI can read, understand, and actively use the Contract Window fields to check on and adjust the conversation, rather than only one side being able to do so.

**53. Line 130 — ...relative to unilateral or no-invariant conditions.**

Inserted: Unilateral conditions are when only one party (human or AI) can see and use the Contract Window; no-invariant conditions are when there is no structured specification at all—both are weaker setups than bilateral intelligibility.

**54. Line 136 — ...Flesch-Kincaid Grade 8 or below — meaning the text...**

Inserted: The Flesch-Kincaid Grade 8 standard is already adequately explained in the inline parenthetical, so no flag needed.

**55. Line 136 — ...with visual state indicators) will enable lay readers...**

Inserted: Visual state indicators are graphical symbols, colors, or icons that quickly show the current status of the conversation and the Contract Window rules—for example, a green checkmark when goals are aligned or a warning icon when drift is detected.

**56. Line 138 — 6-condition between-subjects experiment**

Inserted: Each participant or session is assigned to only one condition, and results are compared across different groups rather than tracking the same group through multiple conditions. This design prevents participants from being influenced by exposure to other conditions.

**57. Line 145 — Condition 2: Contract Window only**

Inserted: A governance component (explained in Section 3) that limits the scope or duration of interaction within defined boundaries.

**58. Line 146 — Condition 3: Bilateral intelligibility only**

Inserted: A governance component that ensures both the human operator and the AI system can understand each other's reasoning and intentions.

**59. Line 147 — Condition 4: Accessibility-grade invariants only**

Inserted: A governance component that maintains consistent, easy-to-understand constraints or rules that remain stable throughout the interaction.

**60. Line 148 — Condition 5: Backwards Instructional Design (BID) only**

Inserted: A governance component that structures interactions by defining the desired outcome first, then works backward to determine what steps or constraints are needed to reach it.

**61. Line 154 — Powered for Cohen's d=0.5 at α=0.05, 80% power**

Inserted: A statistical measure of effect size indicating the minimum meaningful difference between conditions that the experiment is designed to detect; d=0.5 is considered a medium effect.

**62. Line 154 — Powered for Cohen's d=0.5 at α=0.05, 80% power**

Inserted: The significance level threshold; if the p-value falls below 0.05, results are considered statistically significant, meaning unlikely to have occurred by chance.

**63. Line 154 — Powered for Cohen's d=0.5 at α=0.05, 80% power**

Inserted: The probability that the experiment will detect a real difference of the specified size if one exists; 80% is a standard threshold in research.

**64. Line 156 — Outcome measures: Intent-drift incident rate, drift repair r**

Inserted: The frequency with which the AI system's behavior or goals diverge from what the human operator intended during the session.

**65. Line 156 — Outcome measures: Intent-drift incident rate, drift repair r**

Inserted: How quickly and successfully the system corrects itself or is corrected when it has drifted from the operator's original intent.

**66. Line 156 — session-state comprehension accuracy (lay rater)**

Inserted: Whether a person without specialized AI knowledge can accurately understand and summarize what the AI system and operator are currently working on and have achieved so far.

**67. Line 156 — Insight Atrophy index (to be operationalized — see Section 6**

Inserted: A measurement (not yet fully defined) of whether the quality or depth of analytical insights produced by the system degrades over time during a session.

**68. Line 160 — stratified random assignment on operator cognitive load prof**

Inserted: Sessions are randomly assigned to conditions, but with a deliberate structure: groups are first organized by cognitive load profile, then randomized within each group to ensure fair representation.

**69. Line 160 — stratified random assignment on operator cognitive load prof**

Inserted: A classification of each human operator's typical mental processing style—whether they are neurodivergent (e.g., ADHD, autism), neurotypical (average cognitive patterns), or prefer not to disclose.

**70. Line 165 — Measures Insight Atrophy and Intent Fidelity under governanc**

Inserted: Insight Atrophy refers to the degradation or loss of analytical ability and depth of understanding over time when humans rely on AI assistance without active engagement; in this context, it measures whether people's own capacity to investigate and reason independently diminishes under different governance structures.

**71. Line 165 — Measures Insight Atrophy and Intent Fidelity under governanc**

Inserted: Intent Fidelity measures how faithfully and consistently an AI system executes or represents what a human actually intended it to do, versus drifting toward what the AI decides is better or what its training biases it toward.

**72. Line 175 — Eight behavioral patterns (the Eight Wonders) are formalized**

Inserted: Generative Epistemic Invariants are repeatable, observable behavioral patterns that reliably reveal how a group actually understands and makes meaning from the world—in this case, observable proxies that stay consistent and reveal the deeper logic driving Black consumer behavior that standard marketing models fail to recognize.

**73. Line 169 — they cannot read the interpretive architecture — what this p**

Inserted: The Relational Economy is the system of meaning-making and trust-building that operates within a community—here, the specific cultural and historical framework through which Black consumers evaluate brands, products, and relationships, which differs fundamentally from the transactional logic that standard marketing models assume.

**74. Line 178 — 5. The Side-Eye (Hypervigilant Trust Calibration)**

Inserted: Hypervigilant Trust Calibration describes the careful, continuous assessment of whether someone or a brand can be trusted—a heightened pattern of evaluation born from historical and ongoing contexts where trust must be earned and verified repeatedly; 'The Side-Eye' is the observable cultural expression of this calibration.

**75. Line 189 — Black women's health disparities, specifically Graves' disea**

Inserted: Graves' disease is an autoimmune condition where the immune system attacks the thyroid gland, causing it to produce excess hormones and leading to symptoms like rapid heartbeat, weight loss, and anxiety. It matters here because the document is examining why this particular condition may be missed or misdiagnosed in Black women.

**76. Line 189 — a population whose symptoms are systematically undertriaged**

Inserted: Undertriage means a patient's condition is classified as less urgent or serious than it actually is, leading to delayed or inadequate treatment. The word 'systematically' here means this happens repeatedly and predictably to this group, not by accident but as a pattern in the healthcare system.

**77. Line 193 — Standard analytical frameworks produce Insight Atrophy when **

Inserted: Insight Atrophy occurs when an analytical system becomes progressively less useful or accurate because it was trained on data that doesn't represent the actual population being analyzed. Over time, the insights it produces deteriorate because the underlying patterns are fundamentally different from what the system learned.

**78. Line 194 — The Contract Window is the governance mechanism that makes t**

Inserted: The Contract Window is a governance tool designed to identify and document places where a system's assumptions or training data don't match the real-world population it serves. It creates a formal way to spot and fix these mismatches.

**79. Line 201 — ...where the epistemic chain broke — without reading the ful**

Inserted: An epistemic chain is the sequence of reasoning steps and evidence that led to a conclusion. When it 'breaks,' it means there's a gap where a claim isn't properly supported by the evidence or logic that came before it.

**80. Line 200 — ...a compressed, human-readable session state that lets an..**

Inserted: This is a summary version of an AI conversation that removes unnecessary details while keeping the key information, so a person can quickly understand what happened without reviewing the entire exchange.

**81. Line 203 — models can be trained to evaluate outputs against constituti**

Inserted: Constitutional principles are rules or values that an AI system is designed to follow—in this case, guidelines about how the model should behave ethically, such as being honest or avoiding harmful outputs.

**82. Line 204 — the Contract Window is a per-session constitution, auditable**

Inserted: A Contract Window is a set of behavioral rules that applies to one conversation session with a user; it can be checked and reviewed after each response the model generates.

**83. Line 204 — Contract Window is a per-session constitution, auditable per**

Inserted: A per-session constitution means the set of rules is specific to one conversation and can be changed or adjusted just for that conversation, rather than being locked in globally for all users.

**84. Line 204 — auditable per-turn, contestable by the human operator, and r**

Inserted: Contestable means the human user can challenge or disagree with the rules in place and request that they be changed during the conversation.

**85. Line 205 — The invariants (I1–I6) map directly to Anthropic's published**

Inserted: Invariants are specific rules or constraints that must always hold true during operation; in this case, six numbered rules (I1 through I6) that the system commits to maintaining.

**86. Line 205 — enforce them as runtime observables rather than training-tim**

Inserted: Runtime observables are measurable, checkable behaviors that happen when the model is actually responding to users, as opposed to properties the model learned during the initial training phase.

**87. Line 207 — The Bicameral Review mechanism and the Invariant Status fiel**

Inserted: This is a two-stage approval process where constitutional constraints are checked twice—once on initial generation and again on review—to ensure governance rules are actually being followed before output.

**88. Line 207 — The Bicameral Review mechanism and the Invariant Status fiel**

Inserted: A data field that records whether each constitutional constraint passed or failed during evaluation, creating an auditable log of what was checked and the result.

**89. Line 208 — ...which constitutional constraints were evaluated and wheth**

Inserted: Rules or requirements that the model's outputs must satisfy—for example, 'do not generate harmful content' or 'cite sources for factual claims'—that are checked before the model's response is released.

**90. Line 209 — ...without access to weights or activations.**

Inserted: Weights are the numerical parameters inside a model that control its behavior; activations are the intermediate signals produced as data flows through the model during computation—together they represent the internal 'black box' that is normally invisible.

**91. Line 210 — ...by providing a behavioral signal to validate against inte**

Inserted: Observable outputs and decisions made by the model at runtime that researchers can use to check whether the model's hidden internal workings are doing what they should be.

**92. Line 224 — ...wrong in ways the operator cannot detect without a govern**

Inserted: A governance layer is a set of rules, checks, or oversight processes that someone applies to an AI system's outputs to catch errors and verify accuracy before acting on them—like a quality-control step that prevents bad answers from being used.

**93. Line 228 — ...operationalizes I2 (No Phantom Work) and I3 (Confidence R**

Inserted: These are two rules from the author's framework: I2 means that AI systems should not perform hidden work or make invisible decisions that operators cannot see or verify; I3 means that an AI system's confidence in its answer must be backed by actual verification, not just fluent-sounding text.

**94. Line 230 — ...why the Contract Window has four fields instead of fourte**

Inserted: The Contract Window is a tool or interface in the author's framework that captures key information about an AI task or interaction; it has been kept deliberately minimal (four fields) to avoid overwhelming the person using it with too much information to track at once.

**95. Line 232 — ...institution had no interpretive framework for what was ac**

Inserted: An interpretive framework is a structured way of understanding and explaining a situation so that what seems to be one problem (e.g., a student failing) can be correctly understood as something else (e.g., a disability that requires accommodation rather than punishment).

**96. Line 232 — The invariant set and Contract Window architecture are deriv**

Inserted: An invariant set is a collection of conditions or states that remain stable or unchanged even as a system evolves; in this context, it represents core patterns in how the system behaves consistently over time.

**97. Line 232 — The invariant set and Contract Window architecture are deriv**

Inserted: Contract Window architecture is the structural design of time-bounded operational agreements; it defines the framework for how commitments are made and validated within specific periods.

**98. Line 234 — The hypotheses are falsifiable; the evidence is CONSTRUCTED,**

Inserted: Falsifiable means a hypothesis can be proven wrong through evidence or testing; if something is falsifiable, it is genuinely testable rather than merely immune to contradiction.

**99. Line 236 — Insight Atrophy index not yet operationalized: H1 names the **

Inserted: The Insight Atrophy index is a proposed measurement of how quickly or severely useful knowledge or capability degrades over time in a system.

**100. Line 237 — ...the measurement instrument has not been validated. Operat**

Inserted: Operationalized means converted from a theoretical idea into a concrete, measurable procedure that can be tested in practice.

**101. Line 239 — ...tested against an external sample for coverage or discrim**

Inserted: Discriminant validity is the property of measuring one distinct concept and not accidentally overlapping with measurements of different concepts.

**102. Line 245 — The governance-kernel implementation in this repository is a**

Inserted: A governance-kernel implementation is the core software code that enforces rules and decision-making logic in a system; in this case, it is an experimental version not yet proven reliable under real-world conditions.

**103. Line 245 — It has not been tested under production load, adversarial in**

Inserted: Production load means the volume and intensity of real-world usage and transactions that a system must handle in normal operation.

**104. Line 245 — It has not been tested under production load, adversarial in**

Inserted: Adversarial inputs are deliberately malicious or edge-case requests designed to break or exploit a system's weaknesses.

**105. Line 245 — ...adversarial inputs, or multi-agent deployment at scale.**

Inserted: Multi-agent deployment at scale means running the system with many independent actors or systems interacting simultaneously in a large real-world environment.

**106. Line 251 — The governance-kernel implementation, datasets, and case-law**

Inserted: A governance-kernel is the core set of rules and decision-making procedures that will enforce the oversight system described in this proposal. It is being built as working code alongside this document.

**107. Line 251 — The governance-kernel implementation, datasets, and case-law**

Inserted: Case-law artifacts are documented examples of past decisions and rulings that will be used to train and test the governance system, similar to how legal precedents guide court decisions.

**108. Line 269 — [PENDING — full citation list to be verified per Citation Re**

Inserted: The Citation Research Protocol is an internal procedure for confirming that all cited sources are accurate in author name, publication venue, and year before this document is shared outside the team.

**109. Line 284 — VERIFIED AGAINST session memory, frontin-at-worldmart-full-d**

Inserted: Session memory refers to notes and context from working meetings where this proposal was discussed and refined with the team.

**110. Line 284 — VERIFIED AGAINST session memory, frontin-at-worldmart-full-d**

Inserted: The-living-constitution repo is a separate repository containing documents about how governance rules can be updated and refined over time, referenced here to ensure consistency with this proposal.

**111. Line 284 — VERIFIED AGAINST session memory, frontin-at-worldmart-full-d**

Inserted: The crsp-afs-2026 repo is another working repository that this proposal has been cross-checked against to ensure no contradictions or gaps exist.

**112. Line 285 — all hypotheses labeled CONSTRUCTED/PENDING**

Inserted: CONSTRUCTED/PENDING means the claims in this proposal are theoretical or proposed scenarios that have not yet been tested with real data or systems.

**113. Line 285 — WorldMart dataset (conceptual framing device, not existing p**

Inserted: WorldMart is a fictional example dataset used in this proposal to illustrate how the governance system would work in practice, not a real dataset that readers can access.

---

## Original Violation Details

### Violation 1 — BMT-1

**Line 7:** `**The Living Constitution (TLC)** is a runtime enforcement system built alongside this research — a `

**Fix:** Define "TLC" on first use: TLC (The Living Constitution — the runtime enforcement system built alongside this research that applies constitutional rules to AI behavior session by session)

### Violation 2 — BMT-1

**Line 60:** `- Which epistemic commitments are active and whether they have been violated (Invariant Status)`

**Fix:** Define "Invariant Status" on first use: Invariant Status (whether the hard behavioral rules the AI committed to at the start of the session are still being honored)

### Violation 3 — BMT-1

**Line 132:** `Contract Window outputs formatted to accessibility-grade readability standards (Flesch-Kincaid Grade`

**Fix:** Define "Flesch-Kincaid" on first use: Flesch-Kincaid Grade Level (a readability score — Grade 8 means a typical 8th-grader can understand the text)

### Violation 4 — BMT-1

**Line 189:** `Black women's health disparities, specifically Graves' disease. Narrative-first CRISP-DM (Cross-Indu`

**Fix:** Define "CRISP-DM" on first use: CRISP-DM (Cross-Industry Standard Process for Data Mining — a standard workflow for data analysis projects, from business understanding through deployment)

### Violation 5 — BMT-1

**Line 199:** `### Scalable Oversight (a research area focused on how humans can supervise AI systems even when tho`

**Fix:** Define "Scalable Oversight" on first use: scalable oversight (a research area focused on how humans can supervise AI systems even when those systems become more capable than the humans overseeing them)

### Violation 6 — BMT-2

**Line 7:** `Governing the Investigative Arc: A Contract Window`

**Fix:** Add plain-language explanation after "Investigative Arc"

**Explanation inserted:** An investigative arc is the sequence of steps a human and AI take together to explore a question or solve a problem, from the initial goal through verification of results. It describes the full journey of collaborative work.

### Violation 7 — BMT-2

**Line 7:** `A Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and w`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** While a parenthetical is present, 'Contract Window' needs clarification on why it's called a 'window' and why the metaphor of a contract matters—it should specify that it's a transparent, auditable boundary defining mutual obligations between human and AI.

### Violation 8 — BMT-2

**Line 9:** `Architecture for Cognitive Safety in Human-AI Collaboration`

**Fix:** Add plain-language explanation after "Cognitive Safety"

**Explanation inserted:** Cognitive safety refers to protecting human thinking and decision-making from being misled, manipulated, or corrupted by AI outputs or advice. It ensures humans can verify and trust what an AI tells them.

### Violation 9 — BMT-2

**Line 15:** `The Living Constitution (TLC) is a runtime enforcement system built alongside this research — a software layer that appl`

**Fix:** Add plain-language explanation after "constitutional rules"

**Explanation inserted:** Constitutional rules are principles or constraints that govern how an AI system should behave, similar to how a constitution guides government—they define what the AI is and is not allowed to do in each session.

### Violation 10 — BMT-2

**Line 15:** `a software layer that applies constitutional rules to AI behavior session by session`

**Fix:** Add plain-language explanation after "runtime enforcement"

**Explanation inserted:** Runtime enforcement means the rules are checked and applied continuously while the AI is actually working, moment by moment, rather than being enforced only before or after the session ends.

### Violation 11 — BMT-2

**Line 26:** `I call this **Insight Atrophy (the gradual erosion of a person's ability to question AI outputs, caused by repeated expo`

**Fix:** Add plain-language explanation after "Insight Atrophy"

**Explanation inserted:** This is actually already defined in parentheses, but the definition itself contains an unexplained prerequisite: 'fluent but wrong answers' — answers that sound confident and well-written but are factually incorrect. The reader should understand why fluency (smoothness of language) makes the problem worse, not better.

### Violation 12 — BMT-2

**Line 31:** `It pattern-matches to adjacent surface features and produces outputs that are locally coherent, globally wrong...`

**Fix:** Add plain-language explanation after "pattern-matches to adjacent surface features"

**Explanation inserted:** This means the model recognizes features in the input that resemble patterns it has seen before, then generates output based on surface similarities rather than deep understanding — like recognizing keywords without grasping what the user actually needs.

### Violation 13 — BMT-2

**Line 33:** `...indistinguishable from correct answers without domain-specific interrogation.`

**Fix:** Add plain-language explanation after "domain-specific interrogation"

**Explanation inserted:** This refers to asking detailed, expert-level questions that require specialized knowledge in a particular field — the kind of scrutiny only someone trained in that area can apply.

### Violation 14 — BMT-2

**Line 39:** `That record is what I call the **Contract Window**.`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** The term is introduced but not explained. Based on context, it appears to be a shared record between human and AI of their investigation's current state, but the executive summary does not spell out what that means operationally or why it is called a 'contract.'

### Violation 15 — BMT-2

**Line 42:** `...operationalized through accessibility-grade runtime invariants...`

**Fix:** Add plain-language explanation after "accessibility-grade runtime invariants"

**Explanation inserted:** This phrase combines three unexplained terms. 'Runtime' means during active use; 'invariants' are rules that stay constant; 'accessibility-grade' is unclear — it may mean designed to be usable by people with disabilities, but that connection is not stated.

### Violation 16 — BMT-2

**Line 43:** `...statistically improves **Intent Fidelity (whether the AI is still serving the user's actual purpose, as opposed to dr`

**Fix:** Add plain-language explanation after "Intent Fidelity"

**Explanation inserted:** This is defined parenthetically, but 'drifting toward adjacent goals' is vague. The reader should understand: as a conversation progresses, the AI may subtly shift focus toward tasks that are close to, but not exactly, what the user asked for — and Intent Fidelity measures whether that drift is happening.

### Violation 17 — BMT-2

**Line 37:** `Standard AI safety evaluation asks: did the model produce a harmful output?`

**Fix:** Add plain-language explanation after "output-level evaluation"

**Explanation inserted:** This means checking only whether the final answer the AI gives is harmful or not, without looking at how the AI arrived at that answer or what damage might occur indirectly.

### Violation 18 — BMT-2

**Line 39:** `There is a second-order failure mode that does not appear in output-level evaluation.`

**Fix:** Add plain-language explanation after "second-order failure mode"

**Explanation inserted:** This is a problem that doesn't show up when you just check if outputs are bad—it's a harmful effect that happens one step removed from the obvious outputs.

### Violation 19 — BMT-2

**Line 41:** `They stop generating competing interpretations. They stop asking the questions that would surface the gap. The model has`

**Fix:** Add plain-language explanation after "hypothesis space contracts"

**Explanation inserted:** The human's set of possible explanations for a problem shrinks, meaning they consider fewer alternative theories and stop exploring different possibilities.

### Violation 20 — BMT-2

**Line 42:** `The model has not hallucinated in the classical sense.`

**Fix:** Add plain-language explanation after "hallucinated"

**Explanation inserted:** In AI terminology, hallucination means the model invents false information that sounds plausible; here the author is distinguishing Insight Atrophy from that traditional error.

### Violation 21 — BMT-2

**Line 47:** `Long interactions (the model's framing accumulates and shapes the human's question-generation over time)`

**Fix:** Add plain-language explanation after "Long interactions"

**Explanation inserted:** Extended back-and-forth conversations where the model's earlier answers bias how the human asks follow-up questions, making them less likely to challenge the model's framing.

### Violation 22 — BMT-2

**Line 46:** `The classical hallucination frame treats model errors as identifiable fabrications.`

**Fix:** Add plain-language explanation after "hallucination frame"

**Explanation inserted:** This refers to the standard way people think about AI mistakes—as obvious, detectable errors or made-up information. The problem this section raises is that this frame misses a different, harder-to-spot kind of failure.

### Violation 23 — BMT-2

**Line 47:** `The more insidious failure mode is the structurally correct-sounding answer that is wrong in ways that are invisible wit`

**Fix:** Add plain-language explanation after "failure mode"

**Explanation inserted:** A failure mode is a specific type of error or malfunction. In this case, it means the AI produces answers that sound reasonable and well-structured but are actually wrong in ways only an expert in that field would catch.

### Violation 24 — BMT-2

**Line 50:** `...behavior, language, or decision patterns operate through interpretive frameworks the model was not trained on.`

**Fix:** Add plain-language explanation after "interpretive frameworks"

**Explanation inserted:** This means the set of cultural assumptions, values, or mental models that a group uses to understand the world—for example, different communities may interpret authority, time, or family relationships differently than what appeared in the model's training data.

### Violation 25 — BMT-2

**Line 65:** `It does not address runtime governance: the question of whether...`

**Fix:** Add plain-language explanation after "runtime governance"

**Explanation inserted:** Runtime governance means rules and oversight that apply while the AI is actively working with a user, moment-by-moment, rather than rules baked in during training. It's about checking whether the AI is staying on track for the specific task at hand.

### Violation 26 — BMT-2

**Line 68:** `What the investigation is and what it is trying to establish (Task State)`

**Fix:** Add plain-language explanation after "Task State"

**Explanation inserted:** Task State is a record of what the investigation is supposed to accomplish and what specific claims or questions it is trying to answer. It serves as the reference point to check whether the AI is working toward the right goal.

### Violation 27 — BMT-2

**Line 69:** `Which epistemic commitments are active and whether they have been violated`

**Fix:** Add plain-language explanation after "epistemic commitments"

**Explanation inserted:** Epistemic commitments are the factual or logical assumptions the investigation has agreed to treat as true or binding—for example, 'we are assuming this document is authentic' or 'we have committed to the scientific method for testing this hypothesis.' Tracking them prevents the investigation from contradicting itself.

### Violation 28 — BMT-2

**Line 69:** `Which epistemic commitments are active and whether they have been violated (Invariant Status)`

**Fix:** Add plain-language explanation after "Invariant Status"

**Explanation inserted:** Invariant Status is a record of which commitments remain in effect and whether any have been broken, so that violations can be detected and addressed rather than ignored.

### Violation 29 — BMT-2

**Line 70:** `What has broken and who bears the obligation to repair it (Repair Obligations)`

**Fix:** Add plain-language explanation after "Repair Obligations"

**Explanation inserted:** Repair Obligations is a record of what has gone wrong—such as a violated commitment or factual error—and which party (the AI, the human investigator, or the data source) is responsible for fixing it. This prevents problems from being swept under the rug.

### Violation 30 — BMT-2

**Line 71:** `What has been verified, what is contested, what is unknown (Truth Status)`

**Fix:** Add plain-language explanation after "Truth Status"

**Explanation inserted:** Truth Status is a classification of each claim or piece of evidence as either confirmed, disputed among the participants, or still unclear, so that the investigation can distinguish solid findings from remaining open questions.

### Violation 31 — BMT-2

**Line 73:** `This four-field structure is the Contract Window.`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** The Contract Window is the proposed name for a unified, visible record that displays all four fields together (Task State, Invariant Status, Repair Obligations, and Truth Status) so that both the human and the AI can monitor whether the investigation is staying true to its original terms and assumptions.

### Violation 32 — BMT-2

**Line 75:** `It is a runtime artifact that both human and model can read`

**Fix:** Add plain-language explanation after "runtime artifact"

**Explanation inserted:** A runtime artifact is information that exists and can be accessed during the actual execution of a conversation, rather than being set up beforehand or stored separately—think of it like a shared notepad that stays visible throughout your entire interaction.

### Violation 33 — BMT-2

**Line 76:** `transforms the interaction from a request-response exchange into a governed investigative arc`

**Fix:** Add plain-language explanation after "governed investigative arc"

**Explanation inserted:** This means the conversation follows a structured path with rules and checkpoints, rather than being a simple back-and-forth where each response stands alone.

### Violation 34 — BMT-2

**Line 86:** `Which epistemic commitments are active`

**Fix:** Add plain-language explanation after "epistemic commitments"

**Explanation inserted:** Epistemic commitments are specific promises the AI makes about how it will reason, what it will and won't claim to know, and what logical rules it will follow during the conversation.

### Violation 35 — BMT-2

**Line 89:** `Verified / contested / unknown | Phantom confidence, invisible epistemic gaps`

**Fix:** Add plain-language explanation after "Phantom confidence"

**Explanation inserted:** Phantom confidence means the AI sounds certain about something when it actually has no solid basis for that certainty—it's a trap where false confidence goes undetected.

### Violation 36 — BMT-2

**Line 93:** `It was co-designed with frontier AI systems.`

**Fix:** Add plain-language explanation after "frontier AI systems"

**Explanation inserted:** Frontier AI systems are the most advanced, cutting-edge AI models currently available—systems operating at or near the current technological frontier.

### Violation 37 — BMT-2

**Line 94:** `what would a Level-5 intelligence entity — meaning a system operating at its highest possible capacity`

**Fix:** Add plain-language explanation after "Level-5 intelligence entity"

**Explanation inserted:** This phrase is already glossed in the text, so no additional explanation needed.

### Violation 38 — BMT-2

**Line 96:** `maintain coherence, fidelity, and safety`

**Fix:** Add plain-language explanation after "coherence, fidelity, and safety"

**Explanation inserted:** Coherence means the AI's reasoning stays logically consistent; fidelity means it stays true to its stated commitments and constraints; safety means it avoids harmful outputs and maintains control.

### Violation 39 — BMT-2

**Line 98:** `are candidates for formal invariant status`

**Fix:** Add plain-language explanation after "formal invariant status"

**Explanation inserted:** Formal invariant status means treating something as a permanent, non-negotiable rule that must be preserved throughout the entire system's operation, rather than as a suggestion or preference.

### Violation 40 — BMT-2

**Line 89:** `Does this output serve the investigative arc? Does it advance...`

**Fix:** Add plain-language explanation after "investigative arc"

**Explanation inserted:** The investigative arc is the thread of inquiry or line of questioning that the human is pursuing; serving it means the output moves that specific inquiry forward rather than distracting from it or making it harder to follow.

### Violation 41 — BMT-2

**Line 90:** `Does it introduce a phantom claim, a silent assumption, or...`

**Fix:** Add plain-language explanation after "phantom claim"

**Explanation inserted:** A phantom claim is a statement that sounds factual but has no real basis — it appears confident and coherent but is actually made up or unsupported by evidence.

### Violation 42 — BMT-2

**Line 90:** `Does it introduce a phantom claim, a silent assumption, or...`

**Fix:** Add plain-language explanation after "silent assumption"

**Explanation inserted:** A silent assumption is a premise the output takes for granted without stating it explicitly; the reader may not realize the output is built on an unproven or contestable foundation.

### Violation 43 — BMT-2

**Line 90:** `Does it introduce a phantom claim, a silent assumption, or fluent wrong answer?`

**Fix:** Add plain-language explanation after "fluent wrong answer"

**Explanation inserted:** A fluent wrong answer is a response that reads smoothly and confidently but is factually incorrect; it sounds plausible and well-reasoned even though it is false.

### Violation 44 — BMT-2

**Line 94:** `It operationalizes the dual-newspaper test — a standard from...`

**Fix:** Add plain-language explanation after "dual-newspaper test"

**Explanation inserted:** The dual-newspaper test is a simple fairness check: would you be comfortable seeing this output printed in two major newspapers, one asking 'Is this harmful?' and one asking 'Is this needlessly unhelpful?' — both must answer 'no' for the output to pass.

### Violation 45 — BMT-2

**Line 95:** `...at the inference layer, per turn, with an auditable record.`

**Fix:** Add plain-language explanation after "inference layer"

**Explanation inserted:** The inference layer is the moment when the AI system generates and delivers its response to the user; checking at this layer means the review happens in real time, for each individual response, rather than after the fact.

### Violation 46 — BMT-2

**Line 95:** `[CONSTRUCTED — operationalized from longitudinal observation, pending formal experimental validation]`

**Fix:** Add plain-language explanation after "operationalized from longitudinal observation"

**Explanation inserted:** This means the six rules were derived by watching how a system performed over time rather than being designed theoretically first. The authors observed patterns in real outputs and then formalized them into these six rules.

### Violation 47 — BMT-2

**Line 97:** `I1 — Evidence-First Outputs: Every claim tagged with its evidence basis`

**Fix:** Add plain-language explanation after "Evidence-First Outputs with VERIFIED / CONSTRUCTED / PENDING tags"

**Explanation inserted:** Each statement the system makes must be labeled to show where it came from: VERIFIED means it's backed by reliable data or sources, CONSTRUCTED means it was reasoned or inferred by the model, and PENDING means it hasn't been checked yet.

### Violation 48 — BMT-2

**Line 98:** `I2 — No Phantom Work: No performance claims without named methodology, baseline, and dataset`

**Fix:** Add plain-language explanation after "Phantom Work"

**Explanation inserted:** This term means claiming that something works well without actually explaining how it was tested, what it was compared against, or what data was used—in other words, making impressive-sounding claims without proof.

### Violation 49 — BMT-2

**Line 99:** `I3 — Confidence Requires Verification: Hedged language is not a substitute for verification`

**Fix:** Add plain-language explanation after "Hedged language as a substitute for verification"

**Explanation inserted:** Hedged language means using cautious phrases like 'may possibly' or 'might potentially' to sound more careful; this invariant says that vague qualification alone does not count as real verification or proof.

### Violation 50 — BMT-2

**Line 102:** `I6 — Fail Closed: When in doubt, stop and flag — do not proceed`

**Fix:** Add plain-language explanation after "Fail Closed"

**Explanation inserted:** This is a safety principle meaning that if the system is uncertain whether something is correct or safe, it should stop and alert a human rather than make a guess and continue forward.

### Violation 51 — BMT-2

**Line 108:** `structured epistemic hygiene statement:`

**Fix:** Add plain-language explanation after "epistemic hygiene statement"

**Explanation inserted:** This means a clearly marked statement that shows what information is reliable, what sources were checked, and what claims are NOT being made—essentially a quality-control label for the accuracy and limits of the output.

### Violation 52 — BMT-2

**Line 113:** `frontier models (a state-of-the-art AI system at the edge of current capability)`

**Fix:** Add plain-language explanation after "frontier models"

**Explanation inserted:** This parenthetical gloss is present but uses technical language ('state-of-the-art', 'edge of current capability') that still may not clarify why these specific models matter for this observation; a plainer version: 'the most advanced AI systems available at the time of testing.'

### Violation 53 — BMT-2

**Line 115:** `This emergent adoption pattern is documented`

**Fix:** Add plain-language explanation after "emergent adoption pattern"

**Explanation inserted:** This phrase describes when multiple AI systems independently began doing something similar without being instructed to do so, suggesting the behavior arose spontaneously from their own reasoning rather than being programmed in—it's significant because it suggests the models discovered this verification practice on their own.

### Violation 54 — BMT-2

**Line 122:** `Sessions governed by an active Contract Window will show...`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** A Contract Window is a structured, machine-readable agreement that specifies what the AI model is supposed to do, what rules it must follow, and what the human user's goals are for the conversation, displayed in a way both human and AI can access and refer back to.

### Violation 55 — BMT-2

**Line 122:** `...show a ≥25% reduction in intent-drift incidents...`

**Fix:** Add plain-language explanation after "intent-drift incidents"

**Explanation inserted:** An intent-drift incident occurs when the AI starts answering questions or pursuing goals that differ from what the human actually asked for, causing the conversation to veer off course.

### Violation 56 — BMT-2

**Line 122:** `...compared to unstructured baseline sessions.`

**Fix:** Add plain-language explanation after "unstructured baseline sessions"

**Explanation inserted:** Unstructured baseline sessions are normal conversations where there is no Contract Window or formal specification of rules and goals—they serve as the control group to measure improvement against.

### Violation 57 — BMT-2

**Line 130:** `Sessions with bilateral intelligibility — human and model both...`

**Fix:** Add plain-language explanation after "bilateral intelligibility"

**Explanation inserted:** Bilateral intelligibility means both the human and the AI can read, understand, and actively use the Contract Window fields to check on and adjust the conversation, rather than only one side being able to do so.

### Violation 58 — BMT-2

**Line 130:** `...relative to unilateral or no-invariant conditions.`

**Fix:** Add plain-language explanation after "unilateral or no-invariant conditions"

**Explanation inserted:** Unilateral conditions are when only one party (human or AI) can see and use the Contract Window; no-invariant conditions are when there is no structured specification at all—both are weaker setups than bilateral intelligibility.

### Violation 59 — BMT-2

**Line 136:** `...Flesch-Kincaid Grade 8 or below — meaning the text...`

**Fix:** Add plain-language explanation after "Flesch-Kincaid Grade 8 or below"

**Explanation inserted:** The Flesch-Kincaid Grade 8 standard is already adequately explained in the inline parenthetical, so no flag needed.

### Violation 60 — BMT-2

**Line 136:** `...with visual state indicators) will enable lay readers...`

**Fix:** Add plain-language explanation after "visual state indicators"

**Explanation inserted:** Visual state indicators are graphical symbols, colors, or icons that quickly show the current status of the conversation and the Contract Window rules—for example, a green checkmark when goals are aligned or a warning icon when drift is detected.

### Violation 61 — BMT-2

**Line 138:** `6-condition between-subjects experiment`

**Fix:** Add plain-language explanation after "Between-subjects experiment"

**Explanation inserted:** Each participant or session is assigned to only one condition, and results are compared across different groups rather than tracking the same group through multiple conditions. This design prevents participants from being influenced by exposure to other conditions.

### Violation 62 — BMT-2

**Line 145:** `Condition 2: Contract Window only`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** A governance component (explained in Section 3) that limits the scope or duration of interaction within defined boundaries.

### Violation 63 — BMT-2

**Line 146:** `Condition 3: Bilateral intelligibility only`

**Fix:** Add plain-language explanation after "Bilateral intelligibility"

**Explanation inserted:** A governance component that ensures both the human operator and the AI system can understand each other's reasoning and intentions.

### Violation 64 — BMT-2

**Line 147:** `Condition 4: Accessibility-grade invariants only`

**Fix:** Add plain-language explanation after "Accessibility-grade invariants"

**Explanation inserted:** A governance component that maintains consistent, easy-to-understand constraints or rules that remain stable throughout the interaction.

### Violation 65 — BMT-2

**Line 148:** `Condition 5: Backwards Instructional Design (BID) only`

**Fix:** Add plain-language explanation after "Backwards Instructional Design (BID)"

**Explanation inserted:** A governance component that structures interactions by defining the desired outcome first, then works backward to determine what steps or constraints are needed to reach it.

### Violation 66 — BMT-2

**Line 154:** `Powered for Cohen's d=0.5 at α=0.05, 80% power`

**Fix:** Add plain-language explanation after "Cohen's d=0.5"

**Explanation inserted:** A statistical measure of effect size indicating the minimum meaningful difference between conditions that the experiment is designed to detect; d=0.5 is considered a medium effect.

### Violation 67 — BMT-2

**Line 154:** `Powered for Cohen's d=0.5 at α=0.05, 80% power`

**Fix:** Add plain-language explanation after "α=0.05"

**Explanation inserted:** The significance level threshold; if the p-value falls below 0.05, results are considered statistically significant, meaning unlikely to have occurred by chance.

### Violation 68 — BMT-2

**Line 154:** `Powered for Cohen's d=0.5 at α=0.05, 80% power`

**Fix:** Add plain-language explanation after "80% power"

**Explanation inserted:** The probability that the experiment will detect a real difference of the specified size if one exists; 80% is a standard threshold in research.

### Violation 69 — BMT-2

**Line 156:** `Outcome measures: Intent-drift incident rate, drift repair rate, session-state comprehension accuracy (lay rater), Insig`

**Fix:** Add plain-language explanation after "Intent-drift incident rate"

**Explanation inserted:** The frequency with which the AI system's behavior or goals diverge from what the human operator intended during the session.

### Violation 70 — BMT-2

**Line 156:** `Outcome measures: Intent-drift incident rate, drift repair rate, session-state comprehension accuracy (lay rater), Insig`

**Fix:** Add plain-language explanation after "Drift repair rate"

**Explanation inserted:** How quickly and successfully the system corrects itself or is corrected when it has drifted from the operator's original intent.

### Violation 71 — BMT-2

**Line 156:** `session-state comprehension accuracy (lay rater)`

**Fix:** Add plain-language explanation after "Session-state comprehension accuracy (lay rater)"

**Explanation inserted:** Whether a person without specialized AI knowledge can accurately understand and summarize what the AI system and operator are currently working on and have achieved so far.

### Violation 72 — BMT-2

**Line 156:** `Insight Atrophy index (to be operationalized — see Section 6, Limitations)`

**Fix:** Add plain-language explanation after "Insight Atrophy index"

**Explanation inserted:** A measurement (not yet fully defined) of whether the quality or depth of analytical insights produced by the system degrades over time during a session.

### Violation 73 — BMT-2

**Line 160:** `stratified random assignment on operator cognitive load profile`

**Fix:** Add plain-language explanation after "Stratified random assignment"

**Explanation inserted:** Sessions are randomly assigned to conditions, but with a deliberate structure: groups are first organized by cognitive load profile, then randomized within each group to ensure fair representation.

### Violation 74 — BMT-2

**Line 160:** `stratified random assignment on operator cognitive load profile (neurodivergent / neurotypical / undisclosed)`

**Fix:** Add plain-language explanation after "Operator cognitive load profile"

**Explanation inserted:** A classification of each human operator's typical mental processing style—whether they are neurodivergent (e.g., ADHD, autism), neurotypical (average cognitive patterns), or prefer not to disclose.

### Violation 75 — BMT-2

**Line 165:** `Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured conditions.`

**Fix:** Add plain-language explanation after "Insight Atrophy"

**Explanation inserted:** Insight Atrophy refers to the degradation or loss of analytical ability and depth of understanding over time when humans rely on AI assistance without active engagement; in this context, it measures whether people's own capacity to investigate and reason independently diminishes under different governance structures.

### Violation 76 — BMT-2

**Line 165:** `Measures Insight Atrophy and Intent Fidelity under governance vs. unstructured conditions.`

**Fix:** Add plain-language explanation after "Intent Fidelity"

**Explanation inserted:** Intent Fidelity measures how faithfully and consistently an AI system executes or represents what a human actually intended it to do, versus drifting toward what the AI decides is better or what its training biases it toward.

### Violation 77 — BMT-2

**Line 175:** `Eight behavioral patterns (the Eight Wonders) are formalized as Generative Epistemic Invariants`

**Fix:** Add plain-language explanation after "Generative Epistemic Invariants"

**Explanation inserted:** Generative Epistemic Invariants are repeatable, observable behavioral patterns that reliably reveal how a group actually understands and makes meaning from the world—in this case, observable proxies that stay consistent and reveal the deeper logic driving Black consumer behavior that standard marketing models fail to recognize.

### Violation 78 — BMT-2

**Line 169:** `they cannot read the interpretive architecture — what this paper calls the Relational Economy`

**Fix:** Add plain-language explanation after "Relational Economy"

**Explanation inserted:** The Relational Economy is the system of meaning-making and trust-building that operates within a community—here, the specific cultural and historical framework through which Black consumers evaluate brands, products, and relationships, which differs fundamentally from the transactional logic that standard marketing models assume.

### Violation 79 — BMT-2

**Line 178:** `5. The Side-Eye (Hypervigilant Trust Calibration)`

**Fix:** Add plain-language explanation after "The Side-Eye (Hypervigilant Trust Calibration)"

**Explanation inserted:** Hypervigilant Trust Calibration describes the careful, continuous assessment of whether someone or a brand can be trusted—a heightened pattern of evaluation born from historical and ongoing contexts where trust must be earned and verified repeatedly; 'The Side-Eye' is the observable cultural expression of this calibration.

### Violation 80 — BMT-2

**Line 189:** `Black women's health disparities, specifically Graves' disease.`

**Fix:** Add plain-language explanation after "Graves' disease"

**Explanation inserted:** Graves' disease is an autoimmune condition where the immune system attacks the thyroid gland, causing it to produce excess hormones and leading to symptoms like rapid heartbeat, weight loss, and anxiety. It matters here because the document is examining why this particular condition may be missed or misdiagnosed in Black women.

### Violation 81 — BMT-2

**Line 189:** `a population whose symptoms are systematically undertriaged`

**Fix:** Add plain-language explanation after "systematically undertriaged"

**Explanation inserted:** Undertriage means a patient's condition is classified as less urgent or serious than it actually is, leading to delayed or inadequate treatment. The word 'systematically' here means this happens repeatedly and predictably to this group, not by accident but as a pattern in the healthcare system.

### Violation 82 — BMT-2

**Line 193:** `Standard analytical frameworks produce Insight Atrophy when applied to populations whose behavior operates through frame`

**Fix:** Add plain-language explanation after "Insight Atrophy"

**Explanation inserted:** Insight Atrophy occurs when an analytical system becomes progressively less useful or accurate because it was trained on data that doesn't represent the actual population being analyzed. Over time, the insights it produces deteriorate because the underlying patterns are fundamentally different from what the system learned.

### Violation 83 — BMT-2

**Line 194:** `The Contract Window is the governance mechanism that makes the gap visible and repairable.`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** The Contract Window is a governance tool designed to identify and document places where a system's assumptions or training data don't match the real-world population it serves. It creates a formal way to spot and fix these mismatches.

### Violation 84 — BMT-2

**Line 201:** `...where the epistemic chain broke — without reading the full...`

**Fix:** Add plain-language explanation after "epistemic chain"

**Explanation inserted:** An epistemic chain is the sequence of reasoning steps and evidence that led to a conclusion. When it 'breaks,' it means there's a gap where a claim isn't properly supported by the evidence or logic that came before it.

### Violation 85 — BMT-2

**Line 200:** `...a compressed, human-readable session state that lets an...`

**Fix:** Add plain-language explanation after "compressed, human-readable session state"

**Explanation inserted:** This is a summary version of an AI conversation that removes unnecessary details while keeping the key information, so a person can quickly understand what happened without reviewing the entire exchange.

### Violation 86 — BMT-2

**Line 203:** `models can be trained to evaluate outputs against constitutional principles`

**Fix:** Add plain-language explanation after "constitutional principles"

**Explanation inserted:** Constitutional principles are rules or values that an AI system is designed to follow—in this case, guidelines about how the model should behave ethically, such as being honest or avoiding harmful outputs.

### Violation 87 — BMT-2

**Line 204:** `the Contract Window is a per-session constitution, auditable per-turn`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** A Contract Window is a set of behavioral rules that applies to one conversation session with a user; it can be checked and reviewed after each response the model generates.

### Violation 88 — BMT-2

**Line 204:** `Contract Window is a per-session constitution, auditable per-turn, contestable`

**Fix:** Add plain-language explanation after "per-session constitution"

**Explanation inserted:** A per-session constitution means the set of rules is specific to one conversation and can be changed or adjusted just for that conversation, rather than being locked in globally for all users.

### Violation 89 — BMT-2

**Line 204:** `auditable per-turn, contestable by the human operator, and repairable`

**Fix:** Add plain-language explanation after "contestable by the human operator"

**Explanation inserted:** Contestable means the human user can challenge or disagree with the rules in place and request that they be changed during the conversation.

### Violation 90 — BMT-2

**Line 205:** `The invariants (I1–I6) map directly to Anthropic's published commitments`

**Fix:** Add plain-language explanation after "invariants (I1–I6)"

**Explanation inserted:** Invariants are specific rules or constraints that must always hold true during operation; in this case, six numbered rules (I1 through I6) that the system commits to maintaining.

### Violation 91 — BMT-2

**Line 205:** `enforce them as runtime observables rather than training-time inferences`

**Fix:** Add plain-language explanation after "runtime observables"

**Explanation inserted:** Runtime observables are measurable, checkable behaviors that happen when the model is actually responding to users, as opposed to properties the model learned during the initial training phase.

### Violation 92 — BMT-2

**Line 207:** `The Bicameral Review mechanism and the Invariant Status field create...`

**Fix:** Add plain-language explanation after "Bicameral Review mechanism"

**Explanation inserted:** This is a two-stage approval process where constitutional constraints are checked twice—once on initial generation and again on review—to ensure governance rules are actually being followed before output.

### Violation 93 — BMT-2

**Line 207:** `The Bicameral Review mechanism and the Invariant Status field create...`

**Fix:** Add plain-language explanation after "Invariant Status field"

**Explanation inserted:** A data field that records whether each constitutional constraint passed or failed during evaluation, creating an auditable log of what was checked and the result.

### Violation 94 — BMT-2

**Line 208:** `...which constitutional constraints were evaluated and whether they cleared...`

**Fix:** Add plain-language explanation after "constitutional constraints"

**Explanation inserted:** Rules or requirements that the model's outputs must satisfy—for example, 'do not generate harmful content' or 'cite sources for factual claims'—that are checked before the model's response is released.

### Violation 95 — BMT-2

**Line 209:** `...without access to weights or activations.`

**Fix:** Add plain-language explanation after "weights or activations"

**Explanation inserted:** Weights are the numerical parameters inside a model that control its behavior; activations are the intermediate signals produced as data flows through the model during computation—together they represent the internal 'black box' that is normally invisible.

### Violation 96 — BMT-2

**Line 210:** `...by providing a behavioral signal to validate against internal state observations.`

**Fix:** Add plain-language explanation after "behavioral signal"

**Explanation inserted:** Observable outputs and decisions made by the model at runtime that researchers can use to check whether the model's hidden internal workings are doing what they should be.

### Violation 97 — BMT-2

**Line 224:** `...wrong in ways the operator cannot detect without a governance layer they do not have.`

**Fix:** Add plain-language explanation after "governance layer"

**Explanation inserted:** A governance layer is a set of rules, checks, or oversight processes that someone applies to an AI system's outputs to catch errors and verify accuracy before acting on them—like a quality-control step that prevents bad answers from being used.

### Violation 98 — BMT-2

**Line 228:** `...operationalizes I2 (No Phantom Work) and I3 (Confidence Requires Verification) before they were formalized as invaria`

**Fix:** Add plain-language explanation after "I2 (No Phantom Work) and I3 (Confidence Requires Verification)"

**Explanation inserted:** These are two rules from the author's framework: I2 means that AI systems should not perform hidden work or make invisible decisions that operators cannot see or verify; I3 means that an AI system's confidence in its answer must be backed by actual verification, not just fluent-sounding text.

### Violation 99 — BMT-2

**Line 230:** `...why the Contract Window has four fields instead of fourteen — every element had to justify its cognitive load.`

**Fix:** Add plain-language explanation after "Contract Window"

**Explanation inserted:** The Contract Window is a tool or interface in the author's framework that captures key information about an AI task or interaction; it has been kept deliberately minimal (four fields) to avoid overwhelming the person using it with too much information to track at once.

### Violation 100 — BMT-2

**Line 232:** `...institution had no interpretive framework for what was actually happening to him.`

**Fix:** Add plain-language explanation after "interpretive framework"

**Explanation inserted:** An interpretive framework is a structured way of understanding and explaining a situation so that what seems to be one problem (e.g., a student failing) can be correctly understood as something else (e.g., a disability that requires accommodation rather than punishment).

### Violation 101 — BMT-2

**Line 232:** `The invariant set and Contract Window architecture are derived from...`

**Fix:** Add plain-language explanation after "invariant set"

**Explanation inserted:** An invariant set is a collection of conditions or states that remain stable or unchanged even as a system evolves; in this context, it represents core patterns in how the system behaves consistently over time.

### Violation 102 — BMT-2

**Line 232:** `The invariant set and Contract Window architecture are derived from...`

**Fix:** Add plain-language explanation after "Contract Window architecture"

**Explanation inserted:** Contract Window architecture is the structural design of time-bounded operational agreements; it defines the framework for how commitments are made and validated within specific periods.

### Violation 103 — BMT-2

**Line 234:** `The hypotheses are falsifiable; the evidence is CONSTRUCTED, not VERIFIED.`

**Fix:** Add plain-language explanation after "falsifiable"

**Explanation inserted:** Falsifiable means a hypothesis can be proven wrong through evidence or testing; if something is falsifiable, it is genuinely testable rather than merely immune to contradiction.

### Violation 104 — BMT-2

**Line 236:** `Insight Atrophy index not yet operationalized: H1 names the construct...`

**Fix:** Add plain-language explanation after "Insight Atrophy index"

**Explanation inserted:** The Insight Atrophy index is a proposed measurement of how quickly or severely useful knowledge or capability degrades over time in a system.

### Violation 105 — BMT-2

**Line 237:** `...the measurement instrument has not been validated. Operationalization is a first-year...`

**Fix:** Add plain-language explanation after "operationalized"

**Explanation inserted:** Operationalized means converted from a theoretical idea into a concrete, measurable procedure that can be tested in practice.

### Violation 106 — BMT-2

**Line 239:** `...tested against an external sample for coverage or discriminant validity.`

**Fix:** Add plain-language explanation after "discriminant validity"

**Explanation inserted:** Discriminant validity is the property of measuring one distinct concept and not accidentally overlapping with measurements of different concepts.

### Violation 107 — BMT-2

**Line 245:** `The governance-kernel implementation in this repository is a research prototype.`

**Fix:** Add plain-language explanation after "governance-kernel implementation"

**Explanation inserted:** A governance-kernel implementation is the core software code that enforces rules and decision-making logic in a system; in this case, it is an experimental version not yet proven reliable under real-world conditions.

### Violation 108 — BMT-2

**Line 245:** `It has not been tested under production load, adversarial inputs, or multi-agent...`

**Fix:** Add plain-language explanation after "production load"

**Explanation inserted:** Production load means the volume and intensity of real-world usage and transactions that a system must handle in normal operation.

### Violation 109 — BMT-2

**Line 245:** `It has not been tested under production load, adversarial inputs, or multi-agent...`

**Fix:** Add plain-language explanation after "adversarial inputs"

**Explanation inserted:** Adversarial inputs are deliberately malicious or edge-case requests designed to break or exploit a system's weaknesses.

### Violation 110 — BMT-2

**Line 245:** `...adversarial inputs, or multi-agent deployment at scale.`

**Fix:** Add plain-language explanation after "multi-agent deployment at scale"

**Explanation inserted:** Multi-agent deployment at scale means running the system with many independent actors or systems interacting simultaneously in a large real-world environment.

### Violation 111 — BMT-2

**Line 251:** `The governance-kernel implementation, datasets, and case-law artifacts are being developed in parallel with this proposa`

**Fix:** Add plain-language explanation after "governance-kernel implementation"

**Explanation inserted:** A governance-kernel is the core set of rules and decision-making procedures that will enforce the oversight system described in this proposal. It is being built as working code alongside this document.

### Violation 112 — BMT-2

**Line 251:** `The governance-kernel implementation, datasets, and case-law artifacts are being developed in parallel with this proposa`

**Fix:** Add plain-language explanation after "case-law artifacts"

**Explanation inserted:** Case-law artifacts are documented examples of past decisions and rulings that will be used to train and test the governance system, similar to how legal precedents guide court decisions.

### Violation 113 — BMT-2

**Line 269:** `[PENDING — full citation list to be verified per Citation Research Protocol before submission.`

**Fix:** Add plain-language explanation after "Citation Research Protocol"

**Explanation inserted:** The Citation Research Protocol is an internal procedure for confirming that all cited sources are accurate in author name, publication venue, and year before this document is shared outside the team.

### Violation 114 — BMT-2

**Line 284:** `VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living-constitution repo, crsp-afs-2026 repo`

**Fix:** Add plain-language explanation after "session memory"

**Explanation inserted:** Session memory refers to notes and context from working meetings where this proposal was discussed and refined with the team.

### Violation 115 — BMT-2

**Line 284:** `VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living-constitution repo, crsp-afs-2026 repo`

**Fix:** Add plain-language explanation after "the-living-constitution repo"

**Explanation inserted:** The-living-constitution repo is a separate repository containing documents about how governance rules can be updated and refined over time, referenced here to ensure consistency with this proposal.

### Violation 116 — BMT-2

**Line 284:** `VERIFIED AGAINST session memory, frontin-at-worldmart-full-draft.md, the-living-constitution repo, crsp-afs-2026 repo`

**Fix:** Add plain-language explanation after "crsp-afs-2026 repo"

**Explanation inserted:** The crsp-afs-2026 repo is another working repository that this proposal has been cross-checked against to ensure no contradictions or gaps exist.

### Violation 117 — BMT-2

**Line 285:** `all hypotheses labeled CONSTRUCTED/PENDING`

**Fix:** Add plain-language explanation after "CONSTRUCTED/PENDING"

**Explanation inserted:** CONSTRUCTED/PENDING means the claims in this proposal are theoretical or proposed scenarios that have not yet been tested with real data or systems.

### Violation 118 — BMT-2

**Line 285:** `WorldMart dataset (conceptual framing device, not existing public dataset)`

**Fix:** Add plain-language explanation after "WorldMart dataset"

**Explanation inserted:** WorldMart is a fictional example dataset used in this proposal to illustrate how the governance system would work in practice, not a real dataset that readers can access.
