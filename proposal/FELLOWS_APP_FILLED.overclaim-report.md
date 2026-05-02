# Overclaim Audit Report

**File:** FELLOWS_APP_FILLED.md
**Audited:** 2026-05-01T08:01:56.395428+00:00
**Violations found:** 36
**Standard:** Verification and Truth (V&T) — overclaim subcategory

---

## Overclaim Categories

**OC-1** Quantitative claim without artifact reference
**OC-2** Temporal superlative or novelty claim without scoped literature search
**OC-3** Causal claim without stated mechanism
**OC-4** Status/completion claim without artifact pointer
**OC-5** Absolute rate claim without test corpus specification
**OC-6** Internal inconsistency between sections

---

## Result: VIOLATIONS FOUND

Each violation below requires author correction.
The checker does not rewrite claims — you must resolve each one.

### OC-1 — 7 violation(s)

| # | Line | Claim | Why It Matters | Correction Required |
|---|------|-------|----------------|---------------------|
| 1 | 148 | The prototype is built, 62/62 tests pass, synthetic pilot kappa is 0.762, and th | Test pass-rate claim appears without a cited artifact, test log, or data source  | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 2 | 207 | Very likely — 85% estimate. The honest 15% is not hesitation about Anthropic. It | Percentage claim appears without a cited artifact, test log, or data source refe | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 3 | 222 | 100%. This is not a career detour. This is the work. I have 35 years of evidence | Percentage claim appears without a cited artifact, test log, or data source refe | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 4 | 388 | EXISTS (Verified Present): cognitive-governance-lab repo with 62/62 tests passin | Test pass-rate claim appears without a cited artifact, test log, or data source  | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 5 | 389 | ContractWindow prototype 9/9 tests passing; BicameralReview patched, phantom det | Test pass-rate claim appears without a cited artifact, test log, or data source  | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 6 | 390 | kappa 0.762; SessionRecorder 29/29 tests passing; InsightAtrophyIndex operationa | Test pass-rate claim appears without a cited artifact, test log, or data source  | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |
| 7 | 440 | - The 85% / 100% estimates on full-time and safety commitment are honest and | Percentage claim appears without a cited artifact, test log, or data source refe | Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED]  |

#### OC-1 Violation 1 — Line 148

**Claim:** `The prototype is built, 62/62 tests pass, synthetic pilot kappa is 0.762, and the`

**Why this is an overclaim:** Test pass-rate claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 2 — Line 207

**Claim:** `Very likely — 85% estimate. The honest 15% is not hesitation about Anthropic. It is`

**Why this is an overclaim:** Percentage claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 3 — Line 222

**Claim:** `100%. This is not a career detour. This is the work. I have 35 years of evidence for why`

**Why this is an overclaim:** Percentage claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 4 — Line 388

**Claim:** `EXISTS (Verified Present): cognitive-governance-lab repo with 62/62 tests passing;`

**Why this is an overclaim:** Test pass-rate claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 5 — Line 389

**Claim:** `ContractWindow prototype 9/9 tests passing; BicameralReview patched, phantom detection`

**Why this is an overclaim:** Test pass-rate claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 6 — Line 390

**Claim:** `kappa 0.762; SessionRecorder 29/29 tests passing; InsightAtrophyIndex operational (heuristic);`

**Why this is an overclaim:** Test pass-rate claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

#### OC-1 Violation 7 — Line 440

**Claim:** `- The 85% / 100% estimates on full-time and safety commitment are honest and`

**Why this is an overclaim:** Percentage claim appears without a cited artifact, test log, or data source reference in the surrounding text.

**Required correction:** Add an artifact reference: commit hash, file path, DOI, or inline [CONSTRUCTED] tag if the number is an estimate.

### OC-3 — 13 violation(s)

| # | Line | Claim | Why It Matters | Correction Required |
|---|------|-------|----------------|---------------------|
| 1 | 51 | Constitutional AI governs what a model says at training time; it has no mechanis | Claims that Constitutional AI 'has no mechanism' for faithfulness across session | Cite specific studies or benchmarks showing that current Constitutional AI metho |
| 2 | 53 | Four-field runtime structure producing a continuous per-turn behavioral record | Claims the structure 'produces' a behavioral record without explaining the mecha | Explain how each field contributes to record generation and what prevents gaps o |
| 3 | 56 | Contract Window session records are: timestamped, naturalistic, per-turn annotat | Claims that records are 'per-turn annotated' without stating a mechanism, valida | Specify the annotation process, inter-rater reliability (if human-annotated), or |
| 4 | 61 | on April 24, 2026, Kimi (Moonshot AI) independently embedded V&T structure into  | Claims Kimi 'embedded V&T structure' as a causal fact without stating evidence t | Provide evidence (e.g., prompt logs, system inspection, vendor confirmation) tha |
| 5 | 86 | The build system is the research instrument. | Claims a causal relationship between build system and research validity without  | State explicitly: what specific research claims does the build system support, w |
| 6 | 88 | Without TLC, the interpretability study in Proposal II has no data pipeline. | Claims TLC is necessary/causal for the interpretability study without explaining | Specify: what data does TLC collect, what interpretability metrics does it enabl |
| 7 | 88 | V&T structure was spontaneously adopted across five cognitive mode levels withou | Claims spontaneous adoption without stating: what counts as 'adoption,' what mea | Define operationally: how was V&T adoption detected and quantified, what thresho |
| 8 | 133 | The Contract Window closes that gap — produces a continuous per-turn behavioral  | Claims the system 'closes' a gap and 'produces' a record without explaining the  | Explain the causal pathway: how do the four fields (Task State, Invariant Status |
| 9 | 142 | sparse autoencoder features discriminate Contract Window Invariant Status transi | Claims that feature discrimination implies the ability to detect drift before it | Clarify the mechanism: how does detecting a feature transition causally lead to  |
| 10 | 157 | autistic pattern recognition surfaces systematic misclassification before it sho | Claims that a cognitive trait causally enables early detection of statistical mi | Either remove this as a methodology claim or provide explicit evidence (pilot da |
| 11 | 228 | I intend to have three papers in submission and three product prototypes live or | Claims a specific causal outcome (three papers in submission, three prototypes)  | Add: how the fellowship structure enables this output, what specific research ac |
| 12 | 230 | The three papers in submission and the product builds that come out of the fello | Claims that fellowship period activities will produce 'launchable' outputs witho | Specify: research scope per paper, prototype MVP definition, resource dependenci |
| 13 | 384 | being on-site with the interpretability and alignment teams is not optional for  | A causal claim that physical proximity 'requires' or 'is necessary for' the vali | Specify the concrete bottleneck: e.g., 'requires real-time access to internal ac |

#### OC-3 Violation 1 — Line 51

**Claim:** `Constitutional AI governs what a model says at training time; it has no mechanism for whether the model remains faithful to a user's investigative int`

**Why this is an overclaim:** Claims that Constitutional AI 'has no mechanism' for faithfulness across sessions—a negative causal claim—without evidence that existing mechanisms are absent or insufficient.

**Required correction:** Cite specific studies or benchmarks showing that current Constitutional AI methods fail to maintain faithfulness across live sessions, or reframe as a hypothesis to be tested.

#### OC-3 Violation 2 — Line 53

**Claim:** `Four-field runtime structure producing a continuous per-turn behavioral record`

**Why this is an overclaim:** Claims the structure 'produces' a behavioral record without explaining the mechanism by which the four fields capture, log, or enforce record generation.

**Required correction:** Explain how each field contributes to record generation and what prevents gaps or loss of fidelity in the record.

#### OC-3 Violation 3 — Line 56

**Claim:** `Contract Window session records are: timestamped, naturalistic, per-turn annotated with Invariant Status transitions and V&T adoption events.`

**Why this is an overclaim:** Claims that records are 'per-turn annotated' without stating a mechanism, validation method, or ground truth for how annotations are generated or verified.

**Required correction:** Specify the annotation process, inter-rater reliability (if human-annotated), or algorithmic validation method, with a reference to annotation artifacts or protocols.

#### OC-3 Violation 4 — Line 61

**Claim:** `on April 24, 2026, Kimi (Moonshot AI) independently embedded V&T structure into all five levels of an output stack — without instruction. That is the `

**Why this is an overclaim:** Claims Kimi 'embedded V&T structure' as a causal fact without stating evidence that this embedding was intentional, structural, or not coincidental.

**Required correction:** Provide evidence (e.g., prompt logs, system inspection, vendor confirmation) that the embedding was deliberate and not a coincidental output pattern, or reframe as a preliminary observation to investigate.

#### OC-3 Violation 5 — Line 86

**Claim:** `The build system is the research instrument.`

**Why this is an overclaim:** Claims a causal relationship between build system and research validity without explaining HOW the system design produces or enables valid research findings.

**Required correction:** State explicitly: what specific research claims does the build system support, what measurement or validation does it perform, and how does commit governance produce evidence for the three proposals?

#### OC-3 Violation 6 — Line 88

**Claim:** `Without TLC, the interpretability study in Proposal II has no data pipeline.`

**Why this is an overclaim:** Claims TLC is necessary/causal for the interpretability study without explaining what specific data TLC collects and how that data answers the interpretability research question.

**Required correction:** Specify: what data does TLC collect, what interpretability metrics does it enable, and how does session recording convert to interpretability evidence?

#### OC-3 Violation 7 — Line 88

**Claim:** `V&T structure was spontaneously adopted across five cognitive mode levels without instruction.`

**Why this is an overclaim:** Claims spontaneous adoption without stating: what counts as 'adoption,' what measurement confirms it occurred, or what alternative explanations (e.g., prompt effect, statistical artifact) were ruled out.

**Required correction:** Define operationally: how was V&T adoption detected and quantified, what threshold constitutes 'adoption,' and what controls rule out confounds?

#### OC-3 Violation 8 — Line 133

**Claim:** `The Contract Window closes that gap — produces a continuous per-turn behavioral record`

**Why this is an overclaim:** Claims the system 'closes' a gap and 'produces' a record without explaining the mechanism by which runtime governance structure actually achieves behavioral measurement.

**Required correction:** Explain the causal pathway: how do the four fields (Task State, Invariant Status, Repair Obligations, Truth Status) mechanistically enable detection of suppressed alignment failures?

#### OC-3 Violation 9 — Line 142

**Claim:** `sparse autoencoder features discriminate Contract Window Invariant Status transitions? If yes, those features become candidates for a live runtime mon`

**Why this is an overclaim:** Claims that feature discrimination implies the ability to detect drift before it surfaces in output, without a stated causal mechanism linking feature activation to output drift prevention.

**Required correction:** Clarify the mechanism: how does detecting a feature transition causally lead to or enable drift detection before output manifestation?

#### OC-3 Violation 10 — Line 157

**Claim:** `autistic pattern recognition surfaces systematic misclassification before it shows up in aggregate statistics`

**Why this is an overclaim:** Claims that a cognitive trait causally enables early detection of statistical misclassification without stating the mechanism or evidence linking neurodivergent cognition to predictive validity.

**Required correction:** Either remove this as a methodology claim or provide explicit evidence (pilot data, prior studies) demonstrating that autistic pattern recognition outperforms other methods for this detection task.

#### OC-3 Violation 11 — Line 228

**Claim:** `I intend to have three papers in submission and three product prototypes live or specced before the program ends on August 31.`

**Why this is an overclaim:** Claims a specific causal outcome (three papers in submission, three prototypes) without stating the mechanism or process for how fellowship activities will produce these, or explaining what counts as 'specced' vs 'live'.

**Required correction:** Add: how the fellowship structure enables this output, what specific research activities will produce each paper/prototype, and clarify deliverable definitions (e.g., 'three papers submitted to peer review' vs. 'three prototype specifications completed').

#### OC-3 Violation 12 — Line 230

**Claim:** `The three papers in submission and the product builds that come out of the fellowship period are designed to be launchable by the end of August.`

**Why this is an overclaim:** Claims that fellowship period activities will produce 'launchable' outputs without explaining the research methodology, scope, or constraints that make this feasible.

**Required correction:** Specify: research scope per paper, prototype MVP definition, resource dependencies, and realistic timelines for peer review preparation or product specification completion.

#### OC-3 Violation 13 — Line 384

**Claim:** `being on-site with the interpretability and alignment teams is not optional for the research program — the activation capture work and the collaborati`

**Why this is an overclaim:** A causal claim that physical proximity 'requires' or 'is necessary for' the validation work, without explaining the specific mechanism or why remote collaboration (e.g., async documentation, recorded sessions, video calls) cannot achieve the same outcome.

**Required correction:** Specify the concrete bottleneck: e.g., 'requires real-time access to internal activation data that cannot be exported remotely' or 'requires hands-on debugging with live model internals that are only available on-site,' rather than stating proximity as inherently necessary.

### OC-4 — 8 violation(s)

| # | Line | Claim | Why It Matters | Correction Required |
|---|------|-------|----------------|---------------------|
| 1 | 4 | # Completed: April 30, 2026 | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 2 | 225 | project I will complete and walk away from. They are the beginning of a research | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 3 | 308 | the paper is near-complete and the submission is a planned deliverable. I am als | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 4 | 388 | EXISTS (Verified Present): cognitive-governance-lab repo with 62/62 tests passin | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 5 | 404 | FUNCTIONAL STATUS: Application complete. Research program launch-ready May 1, 20 | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 6 | 435 | - All narrative answers are in your voice, grounded in verified infrastructure | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 7 | 450 | V&T (FELLOWS_APP_FILLED.md): EXISTS, written, complete | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |
| 8 | 451 | VERIFIED AGAINST: form clone (FELLOWS_APP_BLANK.md), THREE_PROPOSALS_MASTER.md,  | Completion/validation claim with no artifact pointer in surrounding text. A revi | Add an artifact pointer: commit hash, CI run URL, test result file path, or tag  |

#### OC-4 Violation 1 — Line 4

**Claim:** `# Completed: April 30, 2026`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 2 — Line 225

**Claim:** `project I will complete and walk away from. They are the beginning of a research program`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 3 — Line 308

**Claim:** `the paper is near-complete and the submission is a planned deliverable. I am also`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 4 — Line 388

**Claim:** `EXISTS (Verified Present): cognitive-governance-lab repo with 62/62 tests passing;`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 5 — Line 404

**Claim:** `FUNCTIONAL STATUS: Application complete. Research program launch-ready May 1, 2026.`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 6 — Line 435

**Claim:** `- All narrative answers are in your voice, grounded in verified infrastructure`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 7 — Line 450

**Claim:** `V&T (FELLOWS_APP_FILLED.md): EXISTS, written, complete`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

#### OC-4 Violation 8 — Line 451

**Claim:** `VERIFIED AGAINST: form clone (FELLOWS_APP_BLANK.md), THREE_PROPOSALS_MASTER.md, CGL repo`

**Why this is an overclaim:** Completion/validation claim with no artifact pointer in surrounding text. A reviewer cannot verify this claim without a link to the test run, commit, or result log.

**Required correction:** Add an artifact pointer: commit hash, CI run URL, test result file path, or tag as [CONSTRUCTED] if the claim is aspirational.

### OC-5 — 6 violation(s)

| # | Line | Claim | Why It Matters | Correction Required |
|---|------|-------|----------------|---------------------|
| 1 | 48 | Prototype built, 62/62 tests passing, synthetic pilot kappa 0.762 | Absolute pass rate (62/62 = 100%) is stated without defining the test corpus, wh | Specify: (1) what the 62 tests measure, (2) the scope of behaviors tested, (3) h |
| 2 | 88 | Tier 1 evidence corpus: manifest, codebook, annotation guide, and session protoc | Asserts completeness of corpus structure without stating: how many sessions tota | Provide: corpus size (N sessions), composition by model and date, annotation pro |
| 3 | 129 | 62/62 tests pass | Absolute pass rate claimed without stating test corpus size, edge cases handled, | Specify: how many distinct test conditions were evaluated, what edge cases or fa |
| 4 | 150 | synthetic pilot kappa is 0.762 | Absolute inter-rater agreement statistic without stating sample size, number of  | State: how many items were annotated, how many raters participated, what was the |
| 5 | 222 | 100%. This is not a career detour. | An absolute certainty claim about future behavior (100% likelihood of continuing | Replace with a hedged claim: 'I am committed to continuing this work; my 35-year |
| 6 | 372 | cognitive-governance-lab repo with 62/62 tests passing; ContractWindow prototype | Absolute pass rates (100%) are stated without specifying what the test suites co | Add: the scope of each test suite (unit/integration/system), number of test case |

#### OC-5 Violation 1 — Line 48

**Claim:** `Prototype built, 62/62 tests passing, synthetic pilot kappa 0.762`

**Why this is an overclaim:** Absolute pass rate (62/62 = 100%) is stated without defining the test corpus, what each test validates, or how edge cases were handled.

**Required correction:** Specify: (1) what the 62 tests measure, (2) the scope of behaviors tested, (3) how edge cases or failure modes were handled, and (4) a link to test artifacts or methodology documentation.

#### OC-5 Violation 2 — Line 88

**Claim:** `Tier 1 evidence corpus: manifest, codebook, annotation guide, and session protocol included.`

**Why this is an overclaim:** Asserts completeness of corpus structure without stating: how many sessions total, what model-pairs are covered, how many coders, inter-rater reliability, or edge case handling.

**Required correction:** Provide: corpus size (N sessions), composition by model and date, annotation protocol with reliability coefficients, and handling of ambiguous/borderline cases.

#### OC-5 Violation 3 — Line 129

**Claim:** `62/62 tests pass`

**Why this is an overclaim:** Absolute pass rate claimed without stating test corpus size, edge cases handled, or test artifacts location.

**Required correction:** Specify: how many distinct test conditions were evaluated, what edge cases or failure modes were included, and provide a link to the test suite or results artifact.

#### OC-5 Violation 4 — Line 150

**Claim:** `synthetic pilot kappa is 0.762`

**Why this is an overclaim:** Absolute inter-rater agreement statistic without stating sample size, number of raters, annotation categories, or reference to the annotation artifact.

**Required correction:** State: how many items were annotated, how many raters participated, what was the category schema, and provide or reference the annotation dataset.

#### OC-5 Violation 5 — Line 222

**Claim:** `100%. This is not a career detour.`

**Why this is an overclaim:** An absolute certainty claim about future behavior (100% likelihood of continuing) without any corpus of prior commitments, job tenure, or measurable evidence cited.

**Required correction:** Replace with a hedged claim: 'I am committed to continuing this work; my 35-year research history and framework development demonstrate sustained focus in this domain.'

#### OC-5 Violation 6 — Line 372

**Claim:** `cognitive-governance-lab repo with 62/62 tests passing; ContractWindow prototype 9/9 tests passing; SessionRecorder 29/29 tests passing`

**Why this is an overclaim:** Absolute pass rates (100%) are stated without specifying what the test suites cover, how edge cases were handled, or what the test artifacts demonstrate.

**Required correction:** Add: the scope of each test suite (unit/integration/system), number of test cases per category, what failure modes were explicitly tested, and a reference to the test artifact locations or CI logs.

### OC-6 — 2 violation(s)

| # | Line | Claim | Why It Matters | Correction Required |
|---|------|-------|----------------|---------------------|
| 1 | 87 | The researcher operated as an active constitutional relay — copying responses... | Described as 'not a protocol design — it was a working method' yet later named ' | Clarify: was this a designed experimental manipulation (pre-registered) or an em |
| 2 | 372 | ContractWindow prototype 9/9 tests passing; BehaviorScope correlation between CW | ContractWindow is listed as operationally passing tests in the V&T section, but  | Clarify: are the 9/9 ContractWindow tests unit/integration tests on local data,  |

#### OC-6 Violation 1 — Line 87

**Claim:** `The researcher operated as an active constitutional relay — copying responses...deliberately carrying them into sessions with other models.`

**Why this is an overclaim:** Described as 'not a protocol design — it was a working method' yet later named 'Observation 5' as a documented finding, creating internal inconsistency about whether this was planned methodology or post-hoc reframing.

**Required correction:** Clarify: was this a designed experimental manipulation (pre-registered) or an emergent practice later formalized? If post-hoc, state that explicitly as a limitation on causal inference.

#### OC-6 Violation 2 — Line 372

**Claim:** `ContractWindow prototype 9/9 tests passing; BehaviorScope correlation between CW observables and model internals (CONSTRUCTED — requires interpretabil`

**Why this is an overclaim:** ContractWindow is listed as operationally passing tests in the V&T section, but BehaviorScope correlation is later marked as 'CONSTRUCTED' (not yet validated), creating internal inconsistency about the readiness state of the system.

**Required correction:** Clarify: are the 9/9 ContractWindow tests unit/integration tests on local data, or do they include validation against model internals? If the latter is still pending, move that test count to the 'CONSTRUCTED/PENDING' section or subdivide the status by component.
