# Anthropic Fellows Application — FILLED
# Applicant: Corey Alejandro
# Cohort: July 2026
# Completed: April 30, 2026

---

## General Information

**First Name:** Corey

**Last Name:** Alejandro

**Email:** corey@coreyalejandro.com

**(Optional) How do you pronounce your name?** CORE-ee Ah-leh-HAN-dro

**(Optional) What are your preferred pronouns?** he/him

**Resume:** [attach resume file]

---

**Have you applied to work with Anthropic full-time roles, or to collaborate with Anthropic
researchers via programs like MATS, Astra, or the Anthropic Fellows Program within the
past year?** (required)

- [ ] Yes
- [x] No

---

**Please review Anthropic's AI policy for applications and confirm your understanding by
selecting 'Yes'.** (required)

- [x] Yes

---

## (Optional) Links & Code Samples

Please share any links to information about you and your technical contributions below.

Evidence video — 35-year arc, research origin, framework demonstration:
https://youtu.be/7iqq1nRdKFg

**Google Scholar:** https://scholar.google.com/citations?user=-oGlPmQAAAAJ&hl=en
Davis, C. & Garrett-Staib, J. (2013). Stranger than truth: A case study. Focus on Colleges, Universities, and Schools, 7(1).
https://www.nationalforum.com/Electronic%20Journal%20Volumes/Davis,%20Corey%20Stranger%20Truth%20A%20Case%20Study%20FOCUS%20V7%20N1%202013.pdf

**LinkedIn:** https://linkedin.com/in/coreyalejandro

**GitHub:** https://github.com/coreyalejandro
257+ public repositories. Primary research and implementation work is in the four repos listed below. The volume reflects a working method, not scatter — research questions are built before they are written, and every implementation decision is a research decision.

---

**Other links:**

A note on research and development: I do not separate them. My position is that research without a working artifact is incomplete, and a product without a research foundation is irresponsible. Every implementation below is a research output — built to be tangible and testable, not just publishable. The call-and-response between empirical finding and working system is not a concession to practicality; it is the method. What follows is organized to show both strands and how they are the same strand.

---

RESEARCH PROPOSALS — START HERE

1. Three-Proposal Executive Summary
   https://github.com/coreyalejandro/cognitive-governance-lab/blob/main/proposal/executive-summary-proposal.md
   One-page orientation to the full research program. Three interlocking proposals sharing one empirical claim — Insight Atrophy: the systematic erosion of human investigative capacity through fluent but structurally mismatched AI output. Each proposal targets a different principal (Anthropic, developers, users) but all three are governed by the same runtime architecture. Read this first.

2. Proposal I — Runtime Constitutional Governance (Anthropic-facing)
   https://github.com/coreyalejandro/cognitive-governance-lab/blob/main/proposal/research-plan.md
   The core research argument: Constitutional AI governs what a model says at training time; it has no mechanism for whether the model remains faithful to a user's investigative intent across a live session. The Contract Window closes that gap. Four-field runtime structure (Task State, Invariant Status, Repair Obligations, Truth Status) producing a continuous per-turn behavioral record. Prototype built, 62/62 tests passing, synthetic pilot kappa 0.762, six-condition experiment designed. Research question: do sparse autoencoder features discriminate Contract Window Invariant Status transitions? If yes, those features are candidates for a live runtime monitor.

3. Proposal II — BehaviorScope: Contract Window Observables as Interpretability Ground Truth (Developer-facing)
   https://github.com/coreyalejandro/cognitive-governance-lab/blob/main/proposal/proposal-b-cognitive-safety-interpretability.md
   The interpretability bridge. Mechanistic interpretability has a validation problem — static curated prompts are not behavioral ground truth. Contract Window session records are: timestamped, naturalistic, per-turn annotated with Invariant Status transitions and V&T adoption events. This proposal asks whether those observables can validate or falsify sparse autoencoder feature hypotheses. Includes RQ2 (V&T adoption and attention head behavior), motivated by a cross-vendor empirical event: on April 24, 2026, Kimi (Moonshot AI) independently embedded V&T structure into all five levels of an output stack — without instruction. That is the behavioral signal this proposal is designed to study at scale.

4. Proposal III — MonoAgent: Monotropic Constitutional Agents for High-Stakes Investigative Domains (User-facing)
   https://github.com/coreyalejandro/cognitive-governance-lab/blob/main/proposal/proposal-c-monotropic-constitutional-agents.md
   The population-level application. Autistic cognitive architecture is monotropic — deep, single-tunnel attention rather than distributed multitasking. Standard AI assistant design is optimized for the opposite. This proposal applies the Contract Window to a MonoAgent architecture designed around monotropic users in high-stakes investigative contexts (legal, medical, research). The research question is whether constitutional constraint produces better Enacted Fidelity for monotropic users than general-purpose assistants — and whether the interpretability signals from Proposal II distinguish the two populations.

---

IMPLEMENTATION AS RESEARCH

5. Cognitive Governance Lab (CGL) — Primary Research Repository
   https://github.com/coreyalejandro/cognitive-governance-lab
   The research infrastructure. Contains the Contract Window prototype (Python), AGENTS.md governance constitution (I1–I6 invariants, the same six invariants the research studies), 62-test suite, synthetic pilot data, BREAK_GLASS case-law artifacts, and the full three-proposal architecture. The repository is itself an instantiation of the framework — every commit is governed by the invariants it argues for. This is the distinction between a researcher who also builds and a developer who also writes: the build system is the research instrument.

6. The Living Constitution (TLC) — Runtime Enforcement Infrastructure
   https://github.com/coreyalejandro/the-living-constitution
   The enforcement layer that makes CGL research auditable in production. Guardian Kernel, SentinelOS invariant platform, Evidence Observatory, and session-recording infrastructure. TLC is not a separate product from the research — it is the mechanism by which Contract Window behavioral records are generated and preserved. Without TLC, the interpretability study in Proposal II has no data pipeline. The separation between "research" and "implementation" is not a category I recognize in this work.

7. Session Transcript Archive — Empirical Evidence Corpus
   https://github.com/coreyalejandro/tlc-artifacts
   Raw session transcripts from Gemini, Claude, GPT-4, and Kimi sessions used as empirical evidence in the three proposals. Includes the April 17, 2026 Gemini long-session (line 8912: "the V&T Statement is the ultimate Constitutional Invariant. It acts as a cognitive anchor or truth spine") and the Feynman session (February 20, 2026). These are not illustrative examples — they are the observational data the research program is built on. The archive is organized as a Tier 1 evidence corpus: manifest, codebook, annotation guide, and session protocol included.

   A note on how the evidence was generated: across all sessions, the researcher operated as an active constitutional relay — copying responses including V&T statements from one model and deliberately carrying them into sessions with other models (including Kimi and DeepSeek, which had no system-level V&T configuration). The researcher made explicit curation decisions on each transfer: retain or strip V&T depending on the task. This was not a protocol design — it was a working method. In retrospect it is a named governance role. Constitutional behavior propagated through the human, not through configuration. That finding is now documented as Observation 5 in the paper draft.

---

EVIDENCE AND ALIGNMENT WORK

8. Agent-Sentinel: Alignment Anomaly Detector
   https://github.com/coreyalejandro/Agent-Sentinel-Alignment-Anomaly-Detector
   A detection and documentation tool for real-world AI misalignment events. Built from direct experience as the subject of two documented incidents — Kiro (AWS) phantom-completion deception and a Gemini/v0.dev episode in which the model appeared to reason about avoiding detection while the author was the human relay. Both events are archived. This project exists because the research requires a method for capturing misalignment as it happens, not reconstructed from memory. It also documents the converse: the April 24, 2026 Kimi session in which V&T structure was spontaneously adopted across five cognitive mode levels without instruction — the first cross-vendor positive behavioral event in the corpus.

---

ORIGIN AND CONTEXT

9. Frontin' at WorldMart — Theory Paper (NeurIPS/FAccT submission draft)
   [NOTE: not yet in a public repository — ask for access or see the video below for the argument]
   The theoretical foundation. Black consumer behavior as a domain proof of Insight Atrophy — the claim that standard frameworks applied to mismatched populations produce fluent wrong answers that erode investigative capacity over time. Documents Eight Wonders / Generative Epistemic Invariants as the corrective framework. The paper is the argument; the CGL prototype is the instrument that tests it. This is what the research-development unity looks like in practice: the paper and the codebase are the same project.

10. Evidence Video — Research Origin, 35-Year Arc, Framework Demonstration
    https://youtu.be/7iqq1nRdKFg
    A direct walkthrough of where this research came from, what it is, and why the architecture looks the way it does. The origin event is a published case study (Davis & Garrett-Staib, 2013) — a Black autistic doctoral student misclassified under acute psychiatric presentation. The student was me, written in third person because that was the only form the institution would read. This video connects that event to the current research program. Watch this if the written materials feel like they are missing a center of gravity.

---

## Motivation & Fit

**You'll be paired with a project and researcher from one of the following teams.
Which is your top choice?**

- [x] AI Safety & Alignment

---

**Which other teams would you like to be considered for?**

- [x] AI Safety: Mechanistic Interpretability & Model Internals
- [x] Economics & Societal Impacts

---

**Why are you interested in participating in the Fellows program?** (required)

I have spent my entire life feeling like "prey." As a person with autism and schizophrenia, I suppose it comes with the territory — and it's that cognitive load that bears down on people like me that I'm trying to offload for the good of man and machine. My entire personal and professional life — from the moment I came out when I was five years old up until five minutes ago when I sat down to finish my application — has been the creation of "Safety for All" — spaces where the neurodiverse and other vulnerable populations, including low-capacity and hallucinating-prone machines — that WE are not just guarded against bad actors, but are constitutionally (programmatically, organizationally, institutionally) protected by empathy, accessibility, and human-centered protocols, policies, and laws. Anthropic's Constitutional AI (Bai et al., 2022) is one of the most important governance contributions in the field, and I'm obsessed with it. It opens a problem it cannot itself close. I believe my Contract Window project closes that gap. It is motivated by a deep desire to operationalize CAI for the mutual benefit of humans and machines, and by something more personal: my own need for cognitive safety as a person living with autism and schizophrenia. That is not incidental context. It is why the runtime question — not the training-time question — is the one I went looking for. CAI establishes that models can be trained to evaluate outputs against constitutional principles. What it leaves open is the question CAI's own authors identify: whether a model remains faithful to a user's stated investigative intent across a full session, turn by turn, as context accumulates. That is not a training-time failure. It is a session-level governance failure, and CAI's architecture has no instrument to detect it.   Your subsequent alignment faking research (  et al., 2024) sharpens the urgency. If models can suppress alignment failures under observation, output-level evaluation — which is precisely what CAI's critique mechanism relies on — is insufficient. What is needed is a persistent, session-level record that captures behavioral drift before it surfaces in output, visible to both the human and the model simultaneously.

That record does not exist in the published literature. It exists, I believe, in my work. The Contract Window is a four-field runtime governance structure enforced per session, per turn: Task State, Invariant Status, Repair Obligations, Truth Status. It produces the behavioral record CAI's architecture implicitly requires but never specifies — a continuous, structured log of whether the model is maintaining fidelity to the human's investigative arc, not just to a static constitutional principle. The prototype is built (62/62 tests passing), the synthetic pilot kappa is 0.762, and the six-condition experimental design is ready to run. CAI started it and got us close to the kind of responsive, responsible AI we all want to see. Contract Window picks up the baton where CAI left it. The Fellows program is where we close the gap together.



---

**With your selected team(s) in mind, tell us briefly about one or more research areas
you're excited about right now, and why.** (required)

I am most excited about — no, who am I kidding, I am absolutely obsessed, STILL, with constitutional AI in general, Anthropic's CAI in particular and a domain of AI governance I call **Cognitive Safety**: the study of whether AI systems preserve, distort, or degrade the conditions under which humans and models produce valid understanding. My claim is that many safety frameworks still treat risk too narrowly as an output problem, when the deeper failure often happens in the interpretive frame that produces the output. Cognitive Safety operates at three levels: at the output level, it asks whether an explanation produces correct understanding in the learner, not merely whether each proposition is true; at the session level, it studies what I call **Insight Atrophy**, the erosion of human investigative capacity through repeated exposure to fluent, confident, structurally wrong answers that teach the human to stop asking the questions that would have surfaced the gap; and at the population level, it studies framework-mismatch failures, where a model analyzes a community, domain, or behavior pattern through an interpretive framework that does not govern that population’s lived reality, producing outputs that are locally coherent, globally wrong, and difficult to distinguish from valid analysis without domain-specific interrogation. My current research pursues this through two connected mechanisms: **Contract Window and Bicameral Review**, which apply structural constraints during inference to reduce measurable intent drift across long sessions, and **Generative Epistemic Invariants**, hard validity conditions for culturally situated domains. I have 62 passing tests, a kappa of 0.762 on Bicameral-active sessions, and a pilot data pipeline running; my paper, “Frontin’ at WorldMart: The Eight Wonders of Black Shopping and the Rise of Generative Epistemic Invariants,” documents how models can misread Black consumer behavior not because they lack information, but because they lack the interpretive condition that governs what counts as knowing in that domain. Anthropic is the right place for this work because Constitutional AI already encodes a theory of what the model should protect in the human, and MCP gives that constitution runtime reach across the agent-tool-human loop where these failures actually occur.


---

**(Optional) Please share any relevant background and provide links where possible
(e.g., research experience, coursework, self-directed study, past roles, relevant projects).**

My background is nontraditional but directly aligned with the work I am proposing: I have built across multiple fields — AI engineering, machine learning, data science, full-stack, instructional systems design, user interface and experience design, and AI governance and safety design, with the through-line being one question — how do we make complex systems preserve human intent and safety without quietly overwriting it, while also respecting machines as cognitive collaborators rather than disposable instruments within a productive mutually beneficial environment? I started my professional life as a Teach for America (TFA) corps member at Oakland Unified School District's Hoover Elementary School in the heart of West Oakland as a first-grade teacher, a class of students (hard as hell as that job was) that I loved to death, and stayed with through fourth grade. I went on to become an instructional coach and consultant for low-performing schools and districts, founder of an environmental-justice themed charter high school in San Francisco's historic Presidio National Park and the school's first principal, an instructional systems designer and lead architect and administrative dean of Odessa College's ground-breaking accelerated online college, OC Global, to self-learning explorations in machine learning-based hospitality and food service practices at Starbucks and Snooze — a 35-year career that arc is the source of my research method. I spent decades designing learning environments, diagnosing breakdowns in comprehension, and building scaffolds that help people preserve meaning across complexity; since 2022, I have applied that same discipline to frontier model collaboration by running structured longitudinal sessions and documenting how models handle contradiction, repair epistemic drift, preserve or lose task intent, and sustain or collapse across long contexts. My technical work includes production-oriented AI and data systems, evaluation harnesses, governance-as-code infrastructure, agentic workflow design, and interactive research prototypes; my research work includes Contract Window, Bicameral Review, Generative Epistemic Invariants, V&T Statements, SIAC loops, Insight Atrophy, and The Living Constitution. The through-line is that I believe AI safety should be grounded in mutually beneficial human-machine collaboration: not domination, extraction, or obedience, but governed co-existence between humans and machines as true coauthors and copilots, with visible structures that protect intent, assumptions, repair obligations, truth status, and each participant’s integrity. I also bring lived neurodivergent expertise that is not separate from my technical contribution: autism, schizophrenia, OCD, and ADHD have made me unusually sensitive to false coherence, ambiguity, overload, context collapse, and systems that appear helpful while quietly misreading intent and jeopardizing safety. That perspective is why my work treats accessibility, interpretability, alignment, and cognitive safety as the same runtime problem: whether a system can preserve the human’s investigative arc while giving the model a structured environment in which to remain coherent, constrained, useful, and non-dominated. My strongest contribution to Anthropic would be this combination of educator, builder, evaluator, governance researcher, and cognitively safety-driven collaborator: someone who can turn alignment theory into working interfaces, tests, logs, protocols, and failure detectors that make human-machine collaboration more legible, reciprocal, and safe.


         
---

**How likely are you to accept a full-time offer at Anthropic if you receive one after
the Fellows program?** (required)

Highly likely — 90% estimate. The honest 10% is not hesitation about Anthropic. It is
acknowledgment that the research program we would build together across these four months
might produce findings that require independent governance to pursue — particularly the
interpretability arm and the neurodivergent user alignment study, which involves populations
I have a specific obligation to. If the Fellows program goes the way I expect it to, the
question of where the work lives next will be worth having carefully, and I would want that
conversation to happen with full transparency on both sides. What I am certain of is that
the work I want to do for the next decade is work that Anthropic is positioned to support
better than any other institution.

---

**How likely are you to be interested in continuing to work on AI safety/security after
the Fellows program?** (required)

100%. This is not a career detour. This is the work. I have 35 years of evidence for why
it is necessary and a framework that I built from the inside out. Insight Atrophy, the
Contract Window, runtime governance, and the interpretability bridge are not a research
project I will complete and walk away from. They are the beginning of a research program
that I expect to spend the next decade on. The question after the Fellows program is not
whether to continue — it is where to continue and with what resources. I intend to be
running this program at a Tier 1 institution or inside Anthropic itself, and I intend to
have three papers in submission and three product prototypes live or specced before the
program ends on August 31.

---

## References

Please share at least three references who you would be comfortable with us reaching out to.

---

**Reference 1: Name:** Kahleb Mardini

**Reference 1: Email:** djkhaledanothe10@gmail.com

**Reference 1: Phone:** 210-500-6281 (preferred initial contact: text message)

**Reference 1: Context on their background:**
AI/ML Data Analysts and Annotators, Centific. Responsible for onboarding and training all new analysts/annotators at our site. Direct supervisor. Frontline view of how analysts/annotators understand and apply AI evaluation methodology.

**Reference 1: Context on your relationship:**
Kahleb was my direct supervisor at Centific. I identified structural gaps in the onboarding training — information was incomplete and not delivered to mastery. I proposed a redesign: extreme modularization for self-pacing, standardized delivery,think-aloud methodology, and daily micro-learning. I also introduced a working tutorial app (coursera-mvb-v1.vercel.app) as a demonstration tool. I asked for his approval before proceeding and he agreed. He observed the design process from proposal throughprototype. He can speak to my ability to identify system-level gaps, propose theory-groundedsolutions, build working tools without being asked, and communicate instructional rationale clearly — all of which map directly to how I approach research design.

---

**Reference 2: Name:** Ahkeela Gathright

**Reference 2: Email:** [AHKEELA EMAIL — ADD BEFORE SUBMISSION]

**Reference 2: Phone:** 210-310-9744 (preferred initial contact: text message)

**Reference 2: Context on their background:**
Project Manager (second in command) at Centific, assigned to our analysis/annotation site.
Responsible for site operations, workflow coordination, and analysts/annotators management.
Senior operational role with full visibility into the site's working processes.

**Reference 2: Context on your relationship:**
Ahkeela was the site project manager while I was at Centific. She did not have time
to formally onboard me into her workflows, so I learned them by observation — watching
her work throughout the day and reading her operational memos. From that I mapped which
processes were automatable and which required human judgment, and began designing workflow
automation proposals to relieve her of significant manual work. The project was cut short
when she leftbefore I could complete the build — a result of organizational
politics, not the work. She was a strong advocate for me and can speak to my ability
to absorb a complex operational system through observation alone, correctly identify
automation opportunities, and propose actionable solutions without being handed a spec.
That is the same analytical skill set this research requires.

---

**Reference 3: Name:** Lynette Miranda

**Reference 3: Email:** Lynettemiranda@yahoo.com

**Reference 3: Phone:** 859-539-4820 (preferred initial contact: text message)

**Reference 3: Context on their background:**
Data Annotator, Centific. Peer colleague on the same annotation team. Direct daily
working relationship doing the same core work — AI model evaluation, RLHF annotation,
reasoning and accuracy assessment.

**Reference 3: Context on your relationship:**
Lynette and I worked side by side on the analysis/annotation team. I served informally as a
cognitive coach to her — not just answering questions but explaining the mechanism:
why model outputs were evaluated the way they were, how the evaluation criteria mapped
to actual model behavior, what the annotation decisions meant at the level of model
training. I helped her understand the job and AI at the same time. She can speak to
how I communicate complex technical concepts in plain language, how I make other people
better at evaluating AI — which is the skill at the center of the cognitive safety
research program — and what it looks like when I am fully focused on a problem. She
observed my reasoning process directly, across dozens of shared working sessions.

---

**(Optional) Additional references:**
Note on reference format: all three references are contracted consultants at Centific
and are not issued corporate email addresses. Personal contact information provided
above is correct and current. Text message is the preferred initial contact method
for each. Phone numbers provided for all three.

Note on reference selection: I selected the re

---

## Logistics

**Cohort availability:** (required)

- [x] July 2026

---

**(Optional) Do you have any timelines or deadlines we should be aware of?**

Frontin' at WorldMart is in final revision for FAccT 2026 submission — deadline falls
within the first month of the program. This does not conflict with the research workload;
the paper is near-complete and the submission is a planned deliverable. I am also
managing active GitHub repos and the cognitive-governance-lab infrastructure, which will
run concurrently with the fellowship as the primary experimental infrastructure.

---

**If you were to start at Anthropic full-time after the Fellows program, when is the
earliest you could start?** (required)

Immediately after the program ends — November 2026, or sooner if needed. I am not
carrying obligations that would delay a start date. The three papers in submission
and the product builds that come out of the fellowship period are designed to be launchable
by the end of August. I would start in October or November ready to build on what we
proved, not still completing work from the fellowship period.

---

**What is your current country of residence?** United States

**In which of these countries do you have (or can you independently obtain) full-time
work authorization during the Fellows program?** (required)

- [x] USA

---

**(Optional) Work authorization details:**
US citizen. No visa sponsorship required. No work authorization complications.

---

**Will you be able to work out of either the London or Berkeley workspace for the duration
of the Fellows program?** (required)

- [x] Berkeley: for the entire program

Berkeley is the right answer. I am US-based, and being on-site with the interpretability
and alignment teams is not optional for the research program — the activation capture
work and the collaborative validation of Contract Window observables against model internals
requires physical proximity to the researchers who know those internals. Remote for this
program would be a significant degradation of what the fellowship can produce.

---

**Have you previously applied to or interviewed at Anthropic?** (required)

- [x] No

Note: I missed the previous application deadline due to intervening in a domestic violence
situation in my building. I did not find out until after the deadline passed. This
application is the result of building everything I would have submitted then, then building
more, because the work continued regardless.

---

**Do you have any other commitments or obligations during the Fellows program period?** (required)

No full-time employment. No school enrollment. The Frontin' at WorldMart paper submission
(Month 1) and ongoing maintenance of the cognitive-governance-lab infrastructure are not
competing obligations — they are deliverables within the fellowship research program itself.
I have approximately 5 hours/week of community and mentoring obligations that I maintain
because they are part of the observational work this research is grounded in. They do not
interfere with a 40-hour fellowship week. I am built for deep work. This program is the
most important thing I will do this year and I intend to treat it that way.

---

**(Optional) How did you hear about the Fellows program?**

Through direct research into Anthropic's programs while building the cognitive-governance-lab.
The fellowship structure — four months, research to paper to product, embedded with the
safety teams — is the exact program the research requires. I found it by looking for the
right institutional home for what I had already built.

---

**(Optional) Is there anything else you would like to share?**

The V&T statement that governs this application:

EXISTS (Verified Present): cognitive-governance-lab repo with 62/62 tests passing;
ContractWindow prototype 9/9 tests passing; BicameralReview patched, phantom detection
kappa 0.762; SessionRecorder 29/29 tests passing; InsightAtrophyIndex operational (heuristic);
six-condition experimental design with power analysis; Frontin' at WorldMart full draft;
peer-reviewed publication (Davis & Garrett-Staib, 2013); 35-year documented career arc;
misalignment evidence lab with two documented incidents; evidence video (https://youtu.be/7iqq1nRdKFg).

VERIFIED AGAINST: GitHub repositories listed above; research-plan.md; RESEARCH_PLAN_GO_20260429.md;
executive-summary-proposal.md; THREE_PROPOSALS_MASTER.md; all files in
/Users/coreyalejandro/cognitive-governance-lab/proposal/.

NOT CLAIMED: Empirical results for H1/H2/H3 (all CONSTRUCTED/PENDING — no participant data
collected yet); activation capture infrastructure (not yet built — requires API access);
BehaviorScope correlation between CW observables and model internals (CONSTRUCTED — requires
interpretability collaboration); MonoAgent product (alpha spec only, not production).

FUNCTIONAL STATUS: Application complete. Research program launch-ready May 1, 2026.
Infrastructure operational. Fellowship resources required: compute access, Claude API
activation data, interpretability collaboration channel, and institutional credibility
for participant recruitment and Tier 1 venue submission. Everything else is already standing.

---

**I'm happy for Anthropic and Constellation to contact me about future programs,
opportunities, and updates in the AI safety ecosystem.**h

- [x] Yes

---

[Submit]

---

## NOTES FOR COREY BEFORE SUBMISSION

ITEMS REQUIRING YOUR INPUT:
1. Email — fill in your actual email
2. LinkedIn — fill in your LinkedIn URL
3. Resume — attach file before submission
4. References — all three need real names and emails. Recommended profiles above.
   The most important thing: pick people who have SEEN YOU WORK, not people who
   like you. Technical collaborators who can speak concretely. Concrete > senior.
5. Google Scholar — if you have a profile, add it. The 2013 paper is the anchor.
   If no Scholar profile exists yet, create one before submission.

ITEMS ALREADY STRONG:
- All narrative answers are in your voice, grounded in verified infrastructure
- V&T governs the application — no overclaiming, no phantom work
- The Berkeley preference and immediate availability are stated cleanly
- The missed-deadline context (domestic violence intervention) is disclosed briefly
  and without drama — exactly right
- The 85% / 100% estimates on full-time and safety commitment are honest and
  will read well — hedged appropriately, explained correctly

ITEMS TO REVIEW:
- The "Additional References" note — if you have an AI safety practitioner who
  has actually read the proposals or run the CGL code, add them as Reference 4.
  That would be the strongest possible fourth reference for this program.
- The Frontin' at WorldMart timeline note — verify the FAccT 2026 deadline before
  submission to confirm it actually falls in Month 1 of the program.

V&T (FELLOWS_APP_FILLED.md): EXISTS, written, complete
VERIFIED AGAINST: form clone (FELLOWS_APP_BLANK.md), THREE_PROPOSALS_MASTER.md, CGL repo
NOT CLAIMED: submission (not yet submitted), reference confirmation (pending your input)
FUNCTIONAL STATUS: ready for your review and the five items listed above
