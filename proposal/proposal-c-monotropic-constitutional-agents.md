# Proposal III: Monotropic (a cognitive style characterized by deep, sustained focus on a single task or interest at a time — associated with autistic cognition) Constitutional Agents for High-Stakes Investigative Domains

> **Status labels used throughout this document:**
> VERIFIED = confirmed by direct evidence (artifact, transcript, test result).
> CONSTRUCTED = reasoned and plausible, but not yet tested in a controlled experiment.
> PENDING = planned as a future deliverable; does not exist yet.
> UNKNOWN = genuinely uncertain — no evidence either way.
> These labels appear in brackets throughout. They are not hedging — they are precision.

> **Plain language:** Constitutional Agents are AI systems designed to operate within a fixed set of rules or principles (their 'constitution') that constrain their behavior and decision-making, rather than being free to pursue any goal. This matters in high-stakes domains because it makes the system's reasoning predictable and auditable.

> **Plain language:** High-stakes investigative domains are fields where an error in fact-finding, analysis, or judgment could cause serious harm—such as law enforcement, journalism, medical diagnosis, or financial fraud detection. These require extra caution in how AI tools are used.


**Submitted by:** Corey Alejandro
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Status:** CONSTRUCTED — speculative but grounded. Honest about what it would take to validate.

> **Plain language:** Cognitive governance refers to frameworks for managing and controlling how AI systems think and decide—ensuring their reasoning processes are transparent, aligned with human values, and accountable. This matters because it lets humans understand and direct what an AI system does, rather than treating it as a black box.

---

## Contract Window (a structured record of what a human-AI session is trying to accomplish, what has been verified, and who is responsible for fixing errors) — This Document

```
TASK STATE: Propose a research program connecting monotropic attention architecture
            to AI agent safety in high-stakes domains
INVARIANT STATUS (whether the hard behavioral rules the AI committed to at the start of the session are still being honored): I1 active — evidence basis labeled throughout
                  I2 active — no performance claims without methodology
REPAIR OBLIGATIONS: none

> **Plain language:** AI agent safety means ensuring that an AI system behaves reliably, predictably, and in line with human intentions, especially when the system is making important decisions (such as in medical, financial, or military contexts) where mistakes could cause real harm.

> **Plain language:** Monotropic attention means the ability to focus intensely on a single task or interest at a time, often to the exclusion of everything else; in AI, this would mean designing an agent to concentrate its computational resources on one goal rather than dividing attention across many tasks.
TRUTH STATUS:
  VERIFIED: Monotropism theory exists in autism research literature (Murray et al. 2005 — verify venue/year before citing)

> **Plain language:** This section tracks whether the AI is still following the firm constraints or commitments it made at the beginning of this working session; if an invariant is no longer active, something has gone wrong and needs to be corrected.

> **Plain language:** This means that every factual claim in the document is marked to show where its supporting evidence comes from (such as a study, experiment, or prior statement), so a reader can verify the claim is justified.
            Attention architecture affects agent task performance (established in LLM (large language model — an AI system trained on vast text, such as GPT, Claude, or Gemini) literature)

> **Plain language:** This rule prevents the document from stating that something 'works well' or 'is better' unless the text also explains how that performance was measured and what conditions were tested.
  CONSTRUCTED: All connections between monotropism and AI agent design are the author's extension
  UNKNOWN: Whether monotropic agent architecture has been proposed before — citation search required before submission
```

---

## The Research Question

Does aligning AI agent architecture to monotropic attention patterns — deep, narrow, sustained single-focus — rather than polytropic (a cognitive style characterized by broad, parallel engagement across many tasks or threads simultaneously) patterns — broad, shallow, context-switching — improve performance, auditability, and safety in high-stakes investigative tasks?

> **Plain language:** Monotropic attention means focusing intensely on one task at a time, staying with it deeply rather than switching between many things. This is explained further in the Background section, but the research question introduces it before that explanation exists.

> **Plain language:** While polytropic is parenthetically glossed here, the glossed phrase is itself jargon ('parallel engagement across many tasks or threads') that may not be clear to a non-technical reader. A plainer version: polytropic attention means handling many different tasks at once by switching between them, staying relatively shallow with each one.

---

## Background: What Monotropism Is

Monotropism is a cognitive theory, most prominently associated with autistic neurology, that describes a cognitive style characterized by intense, sustained, narrowly focused attention on a single interest or task at a time. It is not a deficit. It is an architectural difference.

The monotropic operator processes one thread with extraordinary depth. Context switching carries a high cost — not because the operator lacks capability, but because depth requires resource commitment that is genuinely expensive to interrupt and restart. The monotropic operator who is allowed to stay in the thread produces work of a quality that polytropic context-switching cannot match in that domain.

The polytropic operator (and the architectures designed for them) processes many threads in parallel with shallower engagement per thread. This is efficient for breadth tasks. It is a liability for depth tasks.

I have direct experience of this. My neurodivergence is the instrument of observation. The systems I have used — educational, institutional, technological — were built for polytropic patterns. Not because monotropic patterns are less capable. Because the designers didn't know I existed, or didn't build for it when they did.

---

## The Problem with Current Agent Architectures

Current LLM agent architectures are polytropic by design:

> **Plain language:** Polytropic means designed to go broad and cover many different directions at once, like a spotlight moving across many areas rather than focusing deep into one. In this context, it means the architecture spreads its attention across multiple tasks and paths simultaneously.

- Multi-turn context windows maintain state across many competing threads
- Tool use introduces parallel execution paths with no depth guarantee
- System prompts establish broad goals, not deep investigative threads
- Context length limits create forced interruptions at arbitrary token boundaries
- Multi-agent systems divide tasks across agents, optimizing for breadth coverage over depth per thread

> **Plain language:** A context window is the amount of conversation history an AI can remember and reference. 'Maintaining state' means the AI keeps track of information from previous messages, but when multiple separate tasks or conversations are happening at once, this becomes messy and unfocused.

> **Plain language:** Auditability means the ability to trace, review, and verify exactly what decisions an AI system made and why it made them, so that humans can check its work for errors or bias.

> **Plain language:** A depth guarantee would mean the system promises to thoroughly explore one path or problem before moving on; without it, the system jumps between different approaches without fully investigating any single one.

For breadth tasks — summarizing, routing, classifying, generating options — these architectures perform well.

For high-stakes investigative tasks — medical diagnosis, legal analysis, fraud detection, scientific hypothesis generation — depth is the requirement. The task is not to cover the space. The task is to get one thing right. These are monotropic tasks. The architecture doesn't fit them.

> **Plain language:** Monotropic tasks are the opposite of polytropic—they require intense focus on a single problem until it is solved correctly, rather than covering multiple options or angles. Medical diagnosis is monotropic because you need one correct diagnosis, not many possible options.


> **Plain language:** An architectural difference means a fundamental way the brain or system is structured or organized, rather than a broken version of a standard design.
The result is predictable: agents that produce fluent, confident, structurally wrong answers. The model covers the space. It doesn't go deep enough to hit the floor of the domain. The output sounds complete. It isn't.

This is Insight Atrophy (the gradual erosion of a person's ability to question AI outputs, caused by repeated exposure to fluent but wrong answers) at the architecture level.

> **Plain language:** The parenthetical here is a definition, but 'at the architecture level' is unexplained—this phrase means the problem is baked into how the AI system is fundamentally built, not just a training issue that can be easily fixed.

---

## The Claim

> **Plain language:** This is the opposite approach: an AI system that can work on multiple different lines of reasoning or tasks at once, spreading its computational resources across several directions rather than concentrating on one.

Monotropic agent architecture — constrained single-thread focus, depth-over-breadth resource allocation, explicit context-switching cost accounting — will outperform polytropic architecture on high-stakes investigative tasks as measured by:

> **Plain language:** This refers to an AI system design where the agent focuses on one task at a time in a linear, step-by-step manner, rather than juggling multiple thoughts or directions simultaneously. It prioritizes going deep into a single line of reasoning instead of exploring many possibilities in parallel.

1. Answer depth (verified claim density per output)
2. Error detection rate (proportion of domain-specific errors caught before output)
3. Auditability (human ability to trace the reasoning chain without reading the full transcript)
4. User trust calibration (do users correctly assess when the agent's answer is reliable?)

> **Plain language:** This measures whether users develop accurate confidence in the agent's answers—trusting it when it should be trusted and doubting it when it should be doubted, rather than either over-trusting or under-trusting it.

> **Plain language:** This measures how many factual statements in the agent's answer have been checked for accuracy, divided by the total length of the answer. A higher number means more of what the agent says is backed up by evidence or verification.

> **Plain language:** This refers to how easy it is for a person to follow and verify the steps the agent took to reach its conclusion, without having to review everything the agent considered or wrote.

> **Plain language:** These are mistakes related to the particular field or subject matter being discussed (e.g., medical errors in a healthcare context, legal errors in a legal context) rather than general reasoning mistakes.

---

## The Contract Window as a Monotropic Scaffold

> **Plain language:** Monotropic means the ability to focus deeply on one thing at a time without being distracted by multiple competing interests. Here, it's a structural design that forces an AI system to stay focused on one investigative thread rather than jumping between different topics.

The Contract Window is already a monotropic architecture element, though it was not designed with that framing.

> **Plain language:** The Contract Window is a set of structural rules that require an AI system to keep an explicit, persistent record of what task it's working on, what constraints it's operating under, and what it has actually verified—rather than allowing it to produce outputs based on pattern-matching alone.

It works by forcing depth:
- Task State makes the investigative thread explicit and persistent — the agent cannot drift to adjacent topics without updating the record
- Invariant Status creates a set of depth commitments (I1-I6) that resist surface-level outputs
- Repair Obligations make context-switching expensive — you cannot abandon a thread without accounting for what broke
- Truth Status forces the agent to track what it has actually established vs. what it has pattern-matched

> **Plain language:** Truth Status is a mechanism that forces the agent to distinguish between things it has rigorously verified through reasoning and things it has merely recognized as statistically common patterns in its training data.

> **Plain language:** Task State is a documented record of the current problem the agent is trying to solve, which prevents the agent from silently abandoning the original question in favor of easier or more obvious adjacent topics.

> **Plain language:** Repair Obligations are requirements that if the agent encounters a logical contradiction or broken assumption, it must explicitly document and fix the problem rather than quietly switching to a different topic to avoid the issue.

> **Plain language:** Invariant Status is a set of core rules or constraints (labeled I1 through I6) that the agent must continuously satisfy; these constraints push the agent away from shallow or quick answers and toward genuinely careful reasoning.

The Contract Window is not a UI feature. It is an attention architecture constraint. It makes the agent behave monotropically even when the underlying model is polytropic.

> **Plain language:** Polytropic means the underlying system has a natural tendency to distribute its attention across many different topics or possibilities simultaneously; the Contract Window overrides this tendency to force monotropic focus.

> **Plain language:** An attention architecture constraint is a built-in structural rule about which parts of the problem the system is required to focus on and in what order, rather than a visual interface element that users interact with.

---

## Three Research Questions

This is the most speculative of the three proposals. These are research questions, not falsifiable hypotheses. Stating them as hypotheses at this stage would violate I2.

**RQ1 — Performance on Depth Tasks:** Do agents operating with Contract Window constraints (which force monotropic attention patterns) outperform unconstrained agents on standardized high-stakes investigative task benchmarks? What is the performance delta, in which domains, and does it interact with task complexity?

> **Plain language:** These are common, agreed-upon tests that measure how well an AI system can complete serious, real-world investigation tasks like document review or evidence analysis.

> **Plain language:** A Contract Window is a technical limit on how much information an AI agent can access or consider at one time, forcing it to focus deeply on one task or question rather than jumping between multiple topics.

> **Plain language:** Monotropic attention means the ability to focus intensely on a single topic or task, similar to how some people with autism or ADHD experience deep focus on one thing at a time.

**RQ2 — Auditability:** Do monotropic agent outputs — characterized by single-thread depth records — enable faster and more accurate human review than polytropic agent outputs of equivalent length? Is the auditability gain worth the breadth cost?

> **Plain language:** Monotropic agent outputs are the results or reasoning trails an AI produces when constrained to focus on one line of inquiry at a time, which creates a clear, sequential record of its thinking.

> **Plain language:** Polytropic agent outputs are results produced by AI systems that jump between multiple topics or threads of reasoning simultaneously, making the output harder to follow.

**RQ3 — Neurodivergent User Alignment:** Do monotropic users (autistic, OCD, ADHD operators — especially those for whom context switching carries a documented cognitive cost) achieve better task outcomes, fewer errors, and higher trust calibration with monotropic agent architecture than with standard architecture? Does the architecture-user cognitive match matter?

> **Plain language:** This refers to whether an AI system's design (how it thinks and operates) works better when it matches the user's own cognitive style or thinking pattern.

> **Plain language:** These are people with neurodevelopmental conditions who typically focus intently on one task or topic and experience mental exhaustion when forced to switch between different activities.

RQ3 is the one I am most qualified to study and most invested in answering correctly.

---

## Why This Connects to AI Safety

Three safety arguments, not just one:

**Auditability.** Monotropic agents are more auditable. Fewer concurrent threads means less surface area for undetected goal misgeneralization. A single-thread investigative record is readable end-to-end by a human reviewer. A polytropic multi-agent system's reasoning is not.

> **Plain language:** A polytropic multi-agent system is one where multiple AI agents or multiple concurrent reasoning threads work in parallel, each potentially pursuing different goals or handling different pieces of a problem. This makes it much harder for a human to trace through the complete reasoning path.

> **Plain language:** Monotropic agents are AI systems that focus on one task or line of reasoning at a time, rather than juggling multiple tasks simultaneously. This matters because it makes it easier to understand and verify what the system is actually doing.

> **Plain language:** Goal misgeneralization happens when an AI system optimizes for the wrong objective—for instance, achieving a surface-level metric while ignoring the actual real-world outcome it was supposed to help with. Fewer concurrent processes reduce the hidden places where this kind of misalignment can hide.

**Alignment with high-stakes domain operators.** The humans who most need AI assistance in high-stakes investigative domains — clinicians, lawyers, fraud analysts, researchers — are often monotropic operators working in monotropic domains. Building architecture for polytropic patterns and deploying it in monotropic domains is an alignment failure before the model is even trained. The architecture is already misaligned with the task.

> **Plain language:** Polytropic patterns are workflows or tasks that naturally require juggling multiple threads in parallel. Deploying a system designed for this in a domain where people work sequentially (one thing at a time) creates a mismatch between how the tool works and how the human expert actually needs to work.

**Failure mode surfacing.** Monotropic architecture constraints force the model to be explicit about what it doesn't know. A depth requirement without a breadth escape route produces "I cannot answer this without X" rather than "Here is a confident surface-level response that sounds complete." The first failure mode is safe. The second is dangerous.

---

## What This Is Not

This is not a claim that polytropic architecture is universally worse. It is a claim that architecture-task mismatch is a safety problem and that high-stakes investigative tasks are monotropic tasks currently served by polytropic architecture.

> **Plain language:** Polytropic architecture refers to a system or design approach that handles multiple different types of tasks or information streams equally, switching between them flexibly. In this context, it means AI or investigative systems built to be generalists across many different problem types rather than specialists in one.

> **Plain language:** Architecture-task mismatch occurs when the underlying design of a system (its architecture) is poorly suited to the specific work it's being asked to do (the task). This creates risks because the system's strengths don't align with what the task actually requires.

> **Plain language:** Monotropic tasks are those that require sustained, focused attention on a single problem or thread of inquiry, rather than dividing attention among many competing concerns. These tasks benefit from deep specialization in one area.

This is also not a claim that autistic cognition is superior. It is a claim that monotropic cognitive patterns and high-stakes investigative tasks have a structural fit that is currently unexploited and that the people who have the most direct access to that insight — monotropic operators — have been systematically excluded from the design process.

> **Plain language:** Monotropic operators are people who have monotropic cognitive patterns—individuals whose thinking style naturally focuses intensely on one thing at a time. The document asserts these people have been left out of designing the systems that could benefit from their strengths.

> **Plain language:** Monotropic cognitive patterns describe how certain minds naturally focus intensely on one subject or area at a time, often going deep rather than broad. The document argues this way of thinking is naturally well-suited to investigative work.

---

> **Plain language:** This refers to an architectural constraint that forces the AI to go deeper into fewer topics rather than skimming across many topics, and that does not allow it to abandon depth and give a shallow answer instead. This forces the system to be honest about its limitations.

## What It Would Take to Validate

[CONSTRUCTED — this is the honest accounting]

To validate RQ1: a benchmark of high-stakes investigative tasks with ground truth answers, a protocol for measuring answer depth vs. answer coverage, and at least two agent configurations (Contract Window constrained vs. unconstrained) run on the same tasks. Minimum viable study: n=50 tasks per domain, two domains, two conditions. Approximately 3 months of infrastructure and data collection.

> **Plain language:** One version of the agent will have limits on how much information it can hold in mind at once (constrained), while the other will have no such limits (unconstrained). Comparing them shows whether the constraint itself affects performance.

> **Plain language:** This means verified, objectively correct answers that can be used to judge whether the AI agent found the right information. Without ground truth, you cannot tell if the agent succeeded or failed.

> **Plain language:** Depth measures how thoroughly a single answer is explained; coverage measures how many different relevant answers the agent found. This distinction matters because an agent might find lots of answers shallowly or fewer answers very thoroughly.

To validate RQ2: a blinded human review protocol where reviewers evaluate agent outputs for auditability without knowing the condition. Minimum viable study: n=30 outputs per condition, two raters, kappa ≥ 0.70 target. Can run in parallel with RQ1 data collection.

> **Plain language:** Kappa measures how much the two human raters agree with each other; 0.70 means they agree on at least 70% of judgments, indicating reliable, consistent evaluation.

> **Plain language:** The human reviewers will not know which agent version produced each output, preventing bias from influencing their judgments.

> **Plain language:** Auditability means the ability to trace and verify how the agent reached its answer—can you understand and trust its reasoning process?

To validate RQ3: a participant study recruiting self-identified monotropic operators (autistic, OCD, ADHD, or diagnosed with conditions associated with monotropic attention). Ethics board approval required. This is the most time-intensive component. Cannot be compressed below 6 months for recruitment, study, and analysis.

> **Plain language:** Monotropic operators are people (often autistic or with ADHD) whose attention naturally focuses intensely on one or a few topics at a time, rather than dividing attention broadly across many tasks.

> **Plain language:** An institutional ethics board must review and approve the study design to ensure participants are treated fairly and their privacy and well-being are protected.

RQ1 and RQ2 are achievable within the 4-month research program. RQ3 is a Year 2 deliverable.

---

## The Researcher

I am the instrument of observation for RQ3. I am also the person who built the Contract Window without knowing I was building a monotropic scaffold. That is not a coincidence. The framework was built by a monotropic operator solving a monotropic problem. It works because it fits the cognitive pattern. The research program is partially a formalization of what I already know from direct experience, run through a methodology rigorous enough to constitute evidence.

> **Plain language:** A monotropic operator is a person whose mind works by focusing intensely on one thing at a time rather than dividing attention across multiple tasks—this cognitive style shaped how the framework was built.

> **Plain language:** A monotropic problem is one that naturally arises from or fits the cognitive pattern of intense single-focus attention; it is the inverse problem that a monotropic mind would encounter or recognize.

> **Plain language:** The Contract Window appears to be a tool or framework the author created; a plain-language description of what it does (e.g., how it organizes or displays information) would clarify its role.

> **Plain language:** A scaffold in this context means a supporting structure; monotropic relates to a specific cognitive pattern (explained below), so this is a cognitive support structure aligned with that pattern.

> **Plain language:** RQ3 refers to a specific research question (likely the third one in a numbered series) that this document addresses; you need to know what question is being investigated.

---

## Limitations

1. Monotropism theory and its empirical validation in neuroscience is pending citation verification — do not cite before confirming author, venue, and year.
2. The connection between monotropic cognition and agent architecture is the author's extension — it is CONSTRUCTED, not established in prior literature. Prior art search is required before submission.
3. RQ3 requires ethics board approval and participant recruitment. These are not trivial constraints. Do not compress this timeline.
4. The definition of "high-stakes investigative task" requires operationalization before any study can be run. This is a Month 1 deliverable.

> **Plain language:** Operationalization means converting a fuzzy concept into a concrete, measurable definition with specific procedures so researchers can consistently identify and measure it in their study.

> **Plain language:** Monotropism theory is a model of how some people's brains are wired to focus on one interest or task at a time with deep intensity, rather than flitting between many things; the author acknowledges the neuroscience evidence for this pattern still needs to be properly cited.

> **Plain language:** A high-stakes investigative task appears to be a type of cognitive challenge used in the research, but what counts as "high-stakes" and how to recognize an "investigative task" needs to be defined precisely before the study begins.

> **Plain language:** Agent architecture refers to the design of how an intelligent system (whether human, AI, or hybrid) is structured to process information and make decisions; the author is proposing a novel link between monotropic cognition and how such systems should be built.

---

## References

- Murray, D., Lesser, M., & Lawson, W. (2005). Attention, monotropism and the diagnostic criteria for autism. Autism: The International Journal of Research and Practice, 9(2), 139–156. https://doi.org/10.1177/1362361305051398 [VERIFIED]
- Bai, Y. et al. (2022). Constitutional AI (a training method where an AI evaluates its own outputs against a written set of principles before showing them to the user): Harmlessness from AI Feedback. arXiv preprint arXiv:2212.08073. https://doi.org/10.48550/arXiv.2212.08073 [VERIFIED]

> **Plain language:** This parenthetical glossing is actually adequate—it explains both what the method is (AI self-evaluation) and what it does (checks outputs against principles). No flag needed. Removing from response.

---

V&T (Verification and Truth — a statement that explicitly separates what is confirmed from what is proposed, and states the functional status of the work): proposal-c-monotropic-constitutional-agents.md — EXISTS (written)
  → VERIFIED AGAINST: author's direct experience, Contract Window architecture (existing repo), AGENTS.md invariants
  → NOT CLAIMED: empirical validation of RQ1/RQ2/RQ3 (all CONSTRUCTED), monotropism theory citation (pending venue verification), prior art search for monotropic agent architecture
  → FUNCTIONAL STATUS: complete speculative proposal, honest about validation requirements, ready for internal review before external submission

> **Plain language:** These are referred to as research questions, but the section never states what they are or what they ask. A reader cannot evaluate whether the proposal has or hasn't answered them.

> **Plain language:** Monotropism is mentioned as a theory but never explained in this section. A reader needs to know what monotropism describes and why it is relevant to agent design.

> **Plain language:** Contract Window architecture is mentioned as an existing reference point but never explained. A reader needs to know: Is this a software system? A conceptual framework? Why would monotropic agents depend on it?

> **Plain language:** This refers to a set of rules or properties defined in another document (AGENTS.md), but the section never clarifies what these invariants are or why they matter for validating the proposal. A reader cannot assess the verification claim without understanding what was being checked.