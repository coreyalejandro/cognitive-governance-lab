# Proposal C: Monotropic Constitutional Agents for High-Stakes Investigative Domains

**Submitted by:** Corey Alejandro
**Repository:** github.com/coreyalejandro/cognitive-governance-lab
**Status:** CONSTRUCTED — speculative but grounded. Honest about what it would take to validate.

---

## Contract Window — This Document

```
TASK STATE: Propose a research program connecting monotropic attention architecture
            to AI agent safety in high-stakes domains
INVARIANT STATUS: I1 active — evidence basis labeled throughout
                  I2 active — no performance claims without methodology
REPAIR OBLIGATIONS: none
TRUTH STATUS:
  VERIFIED: Monotropism theory exists in autism research literature (Murray et al. 2005 — verify venue/year before citing)
            Attention architecture affects agent task performance (established in LLM literature)
  CONSTRUCTED: All connections between monotropism and AI agent design are the author's extension
  UNKNOWN: Whether monotropic agent architecture has been proposed before — citation search required before submission
```

---

## The Research Question

Does aligning AI agent architecture to monotropic attention patterns — deep, narrow, sustained single-focus — rather than polytropic patterns — broad, shallow, context-switching — improve performance, auditability, and safety in high-stakes investigative tasks?

---

## Background: What Monotropism Is

Monotropism is a cognitive theory, most prominently associated with autistic neurology, that describes a cognitive style characterized by intense, sustained, narrowly focused attention on a single interest or task at a time. It is not a deficit. It is an architectural difference.

The monotropic operator processes one thread with extraordinary depth. Context switching carries a high cost — not because the operator lacks capability, but because depth requires resource commitment that is genuinely expensive to interrupt and restart. The monotropic operator who is allowed to stay in the thread produces work of a quality that polytropic context-switching cannot match in that domain.

The polytropic operator (and the architectures designed for them) processes many threads in parallel with shallower engagement per thread. This is efficient for breadth tasks. It is a liability for depth tasks.

I have direct experience of this. My neurodivergence is the instrument of observation. The systems I have used — educational, institutional, technological — were built for polytropic patterns. Not because monotropic patterns are less capable. Because the designers didn't know I existed, or didn't build for it when they did.

---

## The Problem with Current Agent Architectures

Current LLM agent architectures are polytropic by design:

- Multi-turn context windows maintain state across many competing threads
- Tool use introduces parallel execution paths with no depth guarantee
- System prompts establish broad goals, not deep investigative threads
- Context length limits create forced interruptions at arbitrary token boundaries
- Multi-agent systems divide tasks across agents, optimizing for breadth coverage over depth per thread

For breadth tasks — summarizing, routing, classifying, generating options — these architectures perform well.

For high-stakes investigative tasks — medical diagnosis, legal analysis, fraud detection, scientific hypothesis generation — depth is the requirement. The task is not to cover the space. The task is to get one thing right. These are monotropic tasks. The architecture doesn't fit them.

The result is predictable: agents that produce fluent, confident, structurally wrong answers. The model covers the space. It doesn't go deep enough to hit the floor of the domain. The output sounds complete. It isn't.

This is Insight Atrophy at the architecture level.

---

## The Claim

Monotropic agent architecture — constrained single-thread focus, depth-over-breadth resource allocation, explicit context-switching cost accounting — will outperform polytropic architecture on high-stakes investigative tasks as measured by:

1. Answer depth (verified claim density per output)
2. Error detection rate (proportion of domain-specific errors caught before output)
3. Auditability (human ability to trace the reasoning chain without reading the full transcript)
4. User trust calibration (do users correctly assess when the agent's answer is reliable?)

---

## The Contract Window as a Monotropic Scaffold

The Contract Window is already a monotropic architecture element, though it was not designed with that framing.

It works by forcing depth:
- Task State makes the investigative thread explicit and persistent — the agent cannot drift to adjacent topics without updating the record
- Invariant Status creates a set of depth commitments (I1-I6) that resist surface-level outputs
- Repair Obligations make context-switching expensive — you cannot abandon a thread without accounting for what broke
- Truth Status forces the agent to track what it has actually established vs. what it has pattern-matched

The Contract Window is not a UI feature. It is an attention architecture constraint. It makes the agent behave monotropically even when the underlying model is polytropic.

---

## Three Research Questions

This is the most speculative of the three proposals. These are research questions, not falsifiable hypotheses. Stating them as hypotheses at this stage would violate I2.

**RQ1 — Performance on Depth Tasks:** Do agents operating with Contract Window constraints (which force monotropic attention patterns) outperform unconstrained agents on standardized high-stakes investigative task benchmarks? What is the performance delta, in which domains, and does it interact with task complexity?

**RQ2 — Auditability:** Do monotropic agent outputs — characterized by single-thread depth records — enable faster and more accurate human review than polytropic agent outputs of equivalent length? Is the auditability gain worth the breadth cost?

**RQ3 — Neurodivergent User Alignment:** Do monotropic users (autistic, OCD, ADHD operators — especially those for whom context switching carries a documented cognitive cost) achieve better task outcomes, fewer errors, and higher trust calibration with monotropic agent architecture than with standard architecture? Does the architecture-user cognitive match matter?

RQ3 is the one I am most qualified to study and most invested in answering correctly.

---

## Why This Connects to AI Safety

Three safety arguments, not just one:

**Auditability.** Monotropic agents are more auditable. Fewer concurrent threads means less surface area for undetected goal misgeneralization. A single-thread investigative record is readable end-to-end by a human reviewer. A polytropic multi-agent system's reasoning is not.

**Alignment with high-stakes domain operators.** The humans who most need AI assistance in high-stakes investigative domains — clinicians, lawyers, fraud analysts, researchers — are often monotropic operators working in monotropic domains. Building architecture for polytropic patterns and deploying it in monotropic domains is an alignment failure before the model is even trained. The architecture is already misaligned with the task.

**Failure mode surfacing.** Monotropic architecture constraints force the model to be explicit about what it doesn't know. A depth requirement without a breadth escape route produces "I cannot answer this without X" rather than "Here is a confident surface-level response that sounds complete." The first failure mode is safe. The second is dangerous.

---

## What This Is Not

This is not a claim that polytropic architecture is universally worse. It is a claim that architecture-task mismatch is a safety problem and that high-stakes investigative tasks are monotropic tasks currently served by polytropic architecture.

This is also not a claim that autistic cognition is superior. It is a claim that monotropic cognitive patterns and high-stakes investigative tasks have a structural fit that is currently unexploited and that the people who have the most direct access to that insight — monotropic operators — have been systematically excluded from the design process.

---

## What It Would Take to Validate

[CONSTRUCTED — this is the honest accounting]

To validate RQ1: a benchmark of high-stakes investigative tasks with ground truth answers, a protocol for measuring answer depth vs. answer coverage, and at least two agent configurations (Contract Window constrained vs. unconstrained) run on the same tasks. Minimum viable study: n=50 tasks per domain, two domains, two conditions. Approximately 3 months of infrastructure and data collection.

To validate RQ2: a blinded human review protocol where reviewers evaluate agent outputs for auditability without knowing the condition. Minimum viable study: n=30 outputs per condition, two raters, kappa ≥ 0.70 target. Can run in parallel with RQ1 data collection.

To validate RQ3: a participant study recruiting self-identified monotropic operators (autistic, OCD, ADHD, or diagnosed with conditions associated with monotropic attention). Ethics board approval required. This is the most time-intensive component. Cannot be compressed below 6 months for recruitment, study, and analysis.

RQ1 and RQ2 are achievable within the 4-month research program. RQ3 is a Year 2 deliverable.

---

## The Researcher

I am the instrument of observation for RQ3. I am also the person who built the Contract Window without knowing I was building a monotropic scaffold. That is not a coincidence. The framework was built by a monotropic operator solving a monotropic problem. It works because it fits the cognitive pattern. The research program is partially a formalization of what I already know from direct experience, run through a methodology rigorous enough to constitute evidence.

---

## Limitations

1. Monotropism theory and its empirical validation in neuroscience is pending citation verification — do not cite before confirming author, venue, and year.
2. The connection between monotropic cognition and agent architecture is the author's extension — it is CONSTRUCTED, not established in prior literature. Prior art search is required before submission.
3. RQ3 requires ethics board approval and participant recruitment. These are not trivial constraints. Do not compress this timeline.
4. The definition of "high-stakes investigative task" requires operationalization before any study can be run. This is a Month 1 deliverable.

---

## References

- Murray, D., Lesser, M., & Lawson, W. (2005). Attention, monotropism and the diagnostic criteria for autism. Autism: The International Journal of Research and Practice, 9(2), 139–156. https://doi.org/10.1177/1362361305051398 [VERIFIED]
- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv preprint arXiv:2212.08073. https://doi.org/10.48550/arXiv.2212.08073 [VERIFIED]

---

V&T: proposal-c-monotropic-constitutional-agents.md — EXISTS (written)
  → VERIFIED AGAINST: author's direct experience, Contract Window architecture (existing repo), AGENTS.md invariants
  → NOT CLAIMED: empirical validation of RQ1/RQ2/RQ3 (all CONSTRUCTED), monotropism theory citation (pending venue verification), prior art search for monotropic agent architecture
  → FUNCTIONAL STATUS: complete speculative proposal, honest about validation requirements, ready for internal review before external submission
