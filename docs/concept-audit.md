# Concept introduction audit

Reviewed 2026-11-13 against commit **f9b0ce0**.

**2026-11-14 implementation:** the [remediation record](concept-remediation.md)
tracks a source remedy for all 60 flagged items. The table below is retained as
the original baseline, not the status of the revised course.

Follow-up: optional Lesson 0, Probability essentials, and short first-use
definitions in lesson 1 were added after this baseline review. The status counts
below describe the reviewed commit; they have not been presented as a fresh
audit of the revised course. The new refresher brings the learning-page total
to 82. Other findings remain review items.

**Scope: all 81 Monte Carlo Lab learning pages** — 60 core lessons, 16 advanced lessons, three optional application workbooks, the course overview and field notes. This report does not cover Scientific Method Lab or SymPy Lab.

The course has substantial explanations and a coherent set of experiments. However, its promise that basic Python is the only core prerequisite is not yet met. Several explanations arrive after learners need them. The largest repairs are at the opening probability/NumPy foundation, early distribution summaries, confidence intervals, correlated-input construction and the advanced sampler diagnostics.

This is a review record, not a course rewrite. No lesson, code example, visual, interface or published page was changed for this audit.

## Review method and baseline

Reviewed lesson goals, explanatory paragraphs, reference illustrations and their placement, predictions, visible Python, worked-output labels, observation/change tasks, questions, answer options, feedback, hints and scope statements. Also reviewed the overview, before-start guidance and glossary. The essential route was assessed without assuming that optional hints, worked examples or field notes had been opened.

A gap means that a learner needs an idea to understand the explanation, perform the change, interpret an output or answer the question, but has not yet been given enough meaning or an example. A word in a title or an explicitly optional further-study caveat is not automatically a prerequisite gap. A supplied model formula does not require a proof of its derivation.

The declared baseline matters:

- [README](../README.md), Prerequisites: basic Python is the only core prerequisite; advanced work assumes the core, logarithms and elementary probability densities.
- [Field-notes source](../scripts/build.mjs), before-you-start: variables, function calls and a short loop; arrays and probability are promised as course introductions.
- [Author learning design](learning-design.md), opening paragraph: already includes reading arrays in the audience baseline. This conflicts with the learner-facing promise and should be reconciled.
- [Repository learning-design skill](../.agents/skills/learning-design/SKILL.md): define terms before use. [UX skill](../.agents/skills/ux/SKILL.md): keep the next action clear and cognitive load deliberate.

The advanced route's declared log/density prerequisites are respected in this review. Those same ideas still need teaching where they appear in the core route. Ordinary API calls are not individually treated as mathematical prerequisites, but essential array operations need a small code-to-meaning bridge.

**Status meanings**

- **Gap:** missing explanation or an undeclared prerequisite materially affects the activity.
- **Sequence:** an explanation exists, but appears after an essential use on that page or earlier in the course.
- **Support:** a small gloss, symbol key, caveat or wording correction would help; a new lesson is usually unnecessary.
- **Covered:** no additional gap found in the page's new concept, assuming the earlier prerequisite repairs. This is not a novice usability-study result.

**Coverage:** 26 gap; 8 sequence; 21 covered; 26 support. Status counts describe this desk review, not measured learner failure rates.

## Priority findings and repairs

### 1. Teach probability and trial units in the opening lesson

**Evidence:** lesson 1, explain[0], uses “independently attends with probability 0.72”. Its paragraph 2 defines a whole-event trial, while paragraph 3 calls individual guest decisions binomial trials. Explicit independence is not defined until lesson 25, explain[0].

Add a short opening explanation: 0.72 means a 72% chance for each guest under this model; it does not force exactly 108 of 150 guests to attend. Independence means learning that one guest attends does not change another guest's modelled chance. Friends travelling together provide an immediate counterexample.

Separate the three units: one guest decision, one complete 150-guest event, and repeated complete events used to estimate overflow risk. The existing lesson 2 is good reinforcement, but these distinctions are needed before the first run.

### 2. Supply a minimal NumPy bridge

**Evidence:** lessons 1–2 use boolean arrays, averaging, shapes and axes; later activities depend on slicing, elementwise arithmetic, all/any and assertions. None of these follows automatically from knowing Python variables and a loop.

Use a tiny two-event/three-guest attendance matrix. Explain True as 1 and False as 0 for counting/averaging, a row as one complete event, and the result of summing along each axis. Introduce indexing and elementwise operations only as used. Give assertions a simple meaning: stop when a stated model/check fails. Matrix multiplication and transpose need their own later bridge in 28.

This can be a short first-use example with a reusable refresher link. It does not need to become a separate full Python course.

### 3. Repair early distribution sequencing

**Evidence:** lesson 3's code prints profit percentiles before lesson 4 defines quantiles. Lesson 4's explain[1] and change task require a normal/lognormal model, exponential transformation and sigma before SD in 8, normal modelling in 11 and lognormal parameters in 12.

Teach outcome summaries with a small explicit array of invented delay values in 4. The learner can inspect a histogram, median and P90 without simultaneously learning a distribution transformation. Reserve the lognormal generator and sigma change for 12, or provide the required bridge before this use.

Core density plots also need a visible operational definition by 11: probability comes from area across an interval, and density height is not a point probability. Formal density prerequisites are declared only for the advanced route.

### 4. Put symbol meaning before the diagram requires it

**Evidence:** [scripts/quiet.mjs](../scripts/quiet.mjs), renderQuietLesson, inserts each reference immediately after explain[0]. Later paragraphs therefore cannot prepare learners for some of the inserted notation. [scripts/visuals.py](../scripts/visuals.py), FLOWS, introduces E/P/Π in 3, MCSE in 6, products in 35 and min/expectation/EVPI ordering in 53.

The recent visual work made this ordering problem more visible. Keep each illustration, but place it after its prerequisites or add a brief local symbol key. Read important expressions in words. Examples:

- E = model expectation; P = probability; Π = this example's profit.
- A sum adds the indexed values; a product multiplies them.
- (x)+ = max(x,0); argmin returns the option achieving a minimum.
- In N(μ,σ²), μ is the mean and σ² the variance; NumPy's scale argument is σ.
- In an MCMC acceptance rule, x is current, y is proposed, π is the target density and q(y|x) is the forward proposal density.

Do not treat intentional Python syntax such as ** for exponentiation as failed mathematical typesetting. The mathematics and editable code have different jobs. The lognormal hint in lesson 12 was checked with KaTeX/MathML and renders its μ/log notation correctly.

### 5. Make interval interpretation concrete and restore lesson 17

**Evidence:** lessons 16–18; especially lesson 17, explain[0:2], repeats the same plug-in-standard-error failure. The published Python uses an exact binomial interval, but the explanation of that method was displaced.

Explain coverage through many repeated independent runs, each producing an interval for the same fixed model mean or event probability. Explain why two-sided 95% allocates 2.5% to each tail, whereas a one-sided 95% upper bound allocates 5% to the relevant tail. Restore the exact-binomial explanation before presenting its output.

Lesson 18 needs only small additions: Bernoulli means one yes/no outcome, ceiling means round up, and the half-width/critical-value symbols need a consistent key. The course already distinguishes numerical precision from model validity.

### 6. Bridge the larger core mathematics jumps

**Evidence and smallest useful repairs:**

- **21, distribution fitting:** show the SciPy/NumPy parameter mapping explicitly: shape = log SD, loc = 0, scale = exp(log mean).
- **27–28, correlation:** establish the -1 to 1 range, covariance and standardisation before matrix constraints. The current first paragraph of 28 names diagonal, covariance, positive semidefinite and positive definite without defining them.
- **28, correlated inputs:** a two-variable worked construction, X=Z1 and Y=ρZ1+sqrt(1−ρ²)Z2, can teach the core operation with scalar arithmetic. Keep the general matrix/Cholesky method behind a worked refresher or move it to a route with a declared linear-algebra prerequisite.
- **38, categorical transitions:** turn one transition row into cumulative cutoffs and locate one uniform draw. “Use cumulative probabilities” omits the actual selection mechanism.
- **41, queueing:** explain arrival gaps, unfinished work and the work-per-unit-time versus capacity comparison before asking for a stability interpretation.
- **47, control variates:** define bias through the average result across repeated runs; distinguish it from random error in one run.
- **52, sensitivity:** define an interaction with a demand/shortage-penalty example before asking learners to find one.

These repairs need short worked bridges, not formal proofs or additional unrelated terminology.

### 7. Make the advanced weighting route operational

**Evidence:** lessons 64–69 require more than the declared log/density baseline:

- **64:** derive the complete mixture density from its component widths and selection probabilities.
- **65:** define logsumexp and work a three-weight example using a common shift before exponentiation. A numerical-stability routine should not appear as unexplained magic.
- **67–68:** explain the self-normalised weighted ratio before it is used in the ESS diagnostic. Distinguish finite-sample unbiasedness from consistency as the number of draws grows.
- **68:** define second moment as E[X²]; label the gamma-function exact reference as a supplied optional check.
- **69:** make likelihood a function of the parameter with the observed data held fixed, show the beta mean and concentration, and interpret the printed central posterior interval.

The existing target/proposal and accept/reject explanations in 62–63 are comparatively well scaffolded.

### 8. Add a short dependency bridge before advanced diagnostics

**Evidence:** lessons 71–75 rely on stationarity, convergence, symmetry, lag correlation and diagnostic transformations. The field-notes glossary defines some of these, but the essential path does not bring those definitions into use.

Define stationarity as a distribution preserved by a transition and separate it from approaching that distribution from an arbitrary start. Explain why warm-up is used and why discarding a fixed prefix is not a guarantee. Define a symmetric proposal before the Metropolis rule in 71.

Before FFT code in 74, work a simple lag-correlation and mean-ESS example. For the supplied AR(1) reference with ρ=.9, the large-sample mean ESS is approximately N/19; explain the dependence penalty in words. FFT can be labelled as an optional efficient implementation.

Before 75's code, show pooled ranks becoming normal scores and folding as absolute deviation from a pooled median. Explain that bulk/tail ESS and sampler-specific energy/geometry checks are further study. Do not make Fourier analysis or Hamiltonian Monte Carlo hidden prerequisites.

### 9. Introduce each workbook's domain vocabulary locally

The optional application route adds infrastructure concepts that core simulation knowledge does not supply.

- **Sizing/TCO:** expand total cost of ownership; define power versus energy, usable capacity, reserve factor, growth compounding and the stated cost boundary. Label the current five-year totals as undiscounted. A single worked unit calculation is sufficient.
- **Migration:** distinguish concurrent preparation tasks from running old and new services at the same time. Explain the daily charge before using it.
- **Checkpoint economics:** define saved progress, resumption and save-time overhead before comparing interruption policies. Work one failed/successful chunk ledger.

Keep deeper procurement, financial and operational topics optional.

## Two adjacent content errors

1. **Lesson 17:** the duplicated plug-in-SE paragraphs leave the exact-binomial-interval method unexplained. Restore that method explanation rather than adding a third description of zero plug-in error.
2. **Lesson 70, look:** “Their units and targets differ” is incorrect here. The posterior SD of p and the MCSE of an estimated probability are both dimensionless. Their target quantities and interpretation differ.

The field-notes assertion that lessons always introduce terms before use also overstates the current state. Correct it while completing the prerequisite repairs.

## Page-by-page coverage

Numbers 1–76 refer to the main route; 77–79 label the optional workbooks for this audit. Lesson prose is in [src/course.json](../src/course.json), located by the linked page's slug and named field. Corresponding executable sources are in [python](../python); reference illustrations are in [scripts/visuals.py](../scripts/visuals.py). “Covered” does not erase a dependency on an earlier flagged page.

### Core route

| Page | Status | Finding / smallest useful repair |
| --- | --- | --- |
| 1. [Will the room be full?](https://snowch.github.io/monte-carlo-lab/lessons/will-the-room-be-full.html) | Gap | Probability 0.72 and independence are assumed in the opening. Explain 72% as a chance, not a fixed attendance count; distinguish one guest's yes/no opportunity from one whole-event Monte Carlo trial. Explain True/False averaging as a fraction. |
| 2. [What counts as one trial?](https://snowch.github.io/monte-carlo-lab/lessons/what-counts-as-one-trial.html) | Gap | The trial boundary is well explained. Add equal likelihood to the uniform-draw explanation and a tiny matrix example mapping axis=1 to one attendance total per row and axis=0 to one summary per column. |
| 3. [Repeat the whole experiment](https://snowch.github.io/monte-carlo-lab/lessons/repeat-the-whole-experiment.html) | Sequence | The code reports P10/P50/P90 before quantiles are taught in lesson 4. The illustration uses E, P and profit symbol Π without a key. Introduce the indicator as 1 for a loss and 0 otherwise, and expectation as a model-weighted average. |
| 4. [See the outcomes before the headline](https://snowch.github.io/monte-carlo-lab/lessons/see-the-outcomes-before-the-headline.html) | Sequence | Histogram and quantile definitions are useful, but generating and changing lognormal sigma requires normal, exponential/log-scale and SD concepts taught in 8, 11 and 12. Use an explicit small delay array here or move the generator explanation earlier. |
| 5. [Reproduce a random run](https://snowch.github.io/monte-carlo-lab/lessons/reproduce-a-random-run.html) | Covered | Seed and reproducibility are explained. Independent replications rely on repairing lesson 1; no separate new concept gap found. |
| 6. [Check against an exact answer](https://snowch.github.io/monte-carlo-lab/lessons/check-against-an-exact-answer.html) | Sequence | The strict survival-function boundary is explained well. Cumulative probability is not introduced until 61, and MCSE appears in the reference before 15. Define probability at or below a threshold and label the early error comparison in plain language. |
| 7. [Sample weighted alternatives](https://snowch.github.io/monte-carlo-lab/lessons/sample-weighted-alternatives.html) | Support | Valid category probabilities are explained. Before the quiz, define mutually exclusive as exactly one alternative per visitor and distinguish probabilities from relative weights; show why [5,3,2] becomes [.5,.3,.2] only under the relative-weight interpretation. |
| 8. [Count successes in a fixed group](https://snowch.github.io/monte-carlo-lab/lessons/count-successes-in-a-fixed-group.html) | Sequence | Support is immediately described as possible integer values. Variance and SD are defined in paragraph 3, after the inserted illustration. Place their explanation before their visual summaries and distinguish model variance from its sample estimate. |
| 9. [Count arrivals in an interval](https://snowch.github.io/monte-carlo-lab/lessons/count-arrivals-in-an-interval.html) | Gap | Explain homogeneous as a constant rate and independent increments as counts in non-overlapping time windows not informing each other under the model. The rate-times-duration conversion is already clear. |
| 10. [Wait for the next event](https://snowch.github.io/monte-carlo-lab/lessons/wait-for-the-next-event.html) | Support | Memorylessness is explained. Gloss hazard as the instantaneous event rate conditional on not having had the event yet; a plain-language constant-rate description is enough here. |
| 11. [Model symmetric variation](https://snowch.github.io/monte-carlo-lab/lessons/model-symmetric-variation.html) | Gap | A density axis is used without an operational definition. Explain probability as area over an interval, not curve height. Read N(μ,σ²) aloud and connect its variance parameter to NumPy's scale=σ. |
| 12. [Keep positive quantities positive](https://snowch.github.io/monte-carlo-lab/lessons/keep-positive-quantities-positive.html) | Gap | The core route has not introduced logarithms, exponentials or e. Give an exp/log inverse pair and one numerical parameter example before the median/mean formulas. The current hint's TeX renders correctly; no escaping defect found. |
| 13. [Two different kinds of spread](https://snowch.github.io/monte-carlo-lab/lessons/two-different-kinds-of-spread.html) | Covered | Outcome spread and numerical estimation error are explicitly separated. No additional gap in the page's new concept found. |
| 14. [Watch convergence without promising a winner](https://snowch.github.io/monte-carlo-lab/lessons/watch-convergence-without-promising-a-winner.html) | Support | The convergence claim is qualified. Gloss identically distributed as coming from the same model and finite variance as the condition needed for the displayed error-scaling rule; read the expectation symbol in words. |
| 15. [Calculate Monte Carlo standard error](https://snowch.github.io/monte-carlo-lab/lessons/calculate-monte-carlo-standard-error.html) | Sequence | MCSE is defined, but a quiz option invokes a Markov chain before lesson 38. Use dependent draws in that option or give a brief meaning. Add a local key for sample SD, mean and summation symbols. |
| 16. [An interval for a simulated mean](https://snowch.github.io/monte-carlo-lab/lessons/an-interval-for-a-simulated-mean.html) | Gap | Repeated-simulation coverage needs a concrete explanation: across many independent runs, about 95% of intervals should contain the fixed model mean. Explain why the 97.5th normal percentile gives a two-sided 95% interval. |
| 17. [When zero failures is not zero risk](https://snowch.github.io/monte-carlo-lab/lessons/when-zero-failures-is-not-zero-risk.html) | Gap | Paragraphs 1 and 2 repeat the plug-in-SE failure. The exact-binomial-interval explanation is missing although the code uses it. Restore that explanation and illustrate one-sided versus two-sided tail allocation before comparing bounds. |
| 18. [Plan a precision budget](https://snowch.github.io/monte-carlo-lab/lessons/plan-a-precision-budget.html) | Support | Define a Bernoulli outcome as one yes/no value, ceiling as rounding up, and identify z and the requested half-width consistently between prose, code and figure. The budgeting rationale is explained. |
| 19. [An input needs a source](https://snowch.github.io/monte-carlo-lab/lessons/an-input-needs-a-source.html) | Covered | Evidence provenance, units and rate conversions are taught explicitly. No additional gap found. |
| 20. [Sample the observations you have](https://snowch.github.io/monte-carlo-lab/lessons/sample-the-observations-you-have.html) | Support | Sampling with replacement is explained. Translate exchangeable into the modelling assumption that the selected days can play the same role for this question; keep blocks and covariates as optional further-study terms. |
| 21. [Fit a shape and inspect the fit](https://snowch.github.io/monte-carlo-lab/lessons/fit-a-shape-and-inspect-the-fit.html) | Gap | SciPy shape/location/scale are named but their relation to the earlier NumPy model is omitted. State shape=log SD, loc=0 and scale=exp(log mean), with one matched example. |
| 22. [Turn an expert estimate into a model](https://snowch.github.io/monte-carlo-lab/lessons/turn-an-expert-estimate-into-a-model.html) | Support | Mode is defined as the density peak, but appears after the illustration. Ensure the figure itself labels that peak; translate elicited and calibrated into plain language if retained. Density should already be taught in 11. |
| 23. [The parameters are estimates too](https://snowch.github.io/monte-carlo-lab/lessons/the-parameters-are-estimates-too.html) | Gap | The output reports a percentile bootstrap interval without explaining how the 2.5% and 97.5% bootstrap-mean cutoffs are obtained or its assumptions. The classroom transfer task also needs a one-line explanation of clustering as shared group dependence. |
| 24. [A scenario is not a probability](https://snowch.github.io/monte-carlo-lab/lessons/a-scenario-is-not-a-probability.html) | Support | Scenario conditioning is explained. Give a local reading of the vertical bar in conditional probability and identify λ as the expected count in the specified window. |
| 25. [Independence changes the answer](https://snowch.github.io/monte-carlo-lab/lessons/independence-changes-the-answer.html) | Sequence | This page supplies the first explicit independence definition, after 24 earlier lessons have relied on it. Move a small version to lesson 1. Name marginal as one variable's distribution considered on its own. |
| 26. [Make the shared cause visible](https://snowch.github.io/monte-carlo-lab/lessons/make-the-shared-cause-visible.html) | Support | The common-cause story is clear. Identify the latent/shared factor as an unobserved condition affecting several inputs; read the factor symbol locally. |
| 27. [Correlation does not tell the whole story](https://snowch.github.io/monte-carlo-lab/lessons/correlation-does-not-tell-the-whole-story.html) | Gap | Explain what linear association means and that correlation ranges from -1 to 1 before the next lesson's invalid-correlation task. Include the meanings of the endpoints and zero; the nonlinear counterexample itself is well explained. |
| 28. [Generate correlated normal inputs](https://snowch.github.io/monte-carlo-lab/lessons/generate-correlated-normal-inputs.html) | Gap | Covariance, standardisation, matrix diagonal/transpose, positive semidefiniteness and Cholesky are introduced together without a bridge. Use a two-variable scalar construction or a worked matrix refresher before requiring matrix operations. |
| 29. [Sample one condition after another](https://snowch.github.io/monte-carlo-lab/lessons/sample-one-condition-after-another.html) | Covered | Conditional generation and averaging over conditions are explained. Reuses distribution and dependence concepts from earlier pages. |
| 30. [Stress-test the dependency assumption](https://snowch.github.io/monte-carlo-lab/lessons/stress-test-the-dependency-assumption.html) | Covered | The stress test reuses the correlated-input construction from 28. No separate new gap found; it inherits that prerequisite problem. |
| 31. [Will the project finish on time?](https://snowch.github.io/monte-carlo-lab/lessons/will-the-project-finish-on-time.html) | Covered | Sequential task aggregation and deadline comparison are explicit. Distribution and quantile prerequisites are available earlier. |
| 32. [How much contingency is enough?](https://snowch.github.io/monte-carlo-lab/lessons/how-much-contingency-is-enough.html) | Covered | Reserve, baseline percentile and zero-floor calculation are explained. No additional gap found. |
| 33. [Enough food without too much waste](https://snowch.github.io/monte-carlo-lab/lessons/enough-food-without-too-much-waste.html) | Support | The shortage/waste calculation is explained. Define (x)+ as max(x,0) next to its first formula and connect it to the code's clipping operation. |
| 34. [How uncertain is a calculated measurement?](https://snowch.github.io/monte-carlo-lab/lessons/how-uncertain-is-a-calculated-measurement.html) | Support | The propagation calculation is explained. Define calibration and distinguish uncertainty about a measurement from repeated-reading noise; identify which of these the toy inputs represent. |
| 35. [How reliable is a whole product?](https://snowch.github.io/monte-carlo-lab/lessons/how-reliable-is-a-whole-product.html) | Support | Series and parallel success logic is explained in words. Read ∏ as multiply all component probabilities and connect all/any to all components versus at least one. |
| 36. [Estimate an integral by sampling](https://snowch.github.io/monte-carlo-lab/lessons/estimate-an-integral-by-sampling.html) | Support | Sampling an area is explained without requiring a prior calculus course. Add a local key for the integral sign, integration limits and function being averaged. |
| 37. [Follow a random walk](https://snowch.github.io/monte-carlo-lab/lessons/follow-a-random-walk.html) | Covered | Walk, state, step and complete path are introduced operationally. No additional gap found. |
| 38. [Move between states](https://snowch.github.io/monte-carlo-lab/lessons/move-between-states.html) | Gap | Markov state and transition rows are defined. Show how [.75,.20,.05] becomes cumulative cutoffs [.75,.95,1], then locate one uniform draw. Explain the row-validity assertions as checks. |
| 39. [Parallel work changes the critical path](https://snowch.github.io/monte-carlo-lab/lessons/parallel-work-changes-the-critical-path.html) | Support | The max(A,B)+review rule is clear. Define critical path as the chain of dependent tasks that controls completion; distinguish a dependency constraint from limited resources. |
| 40. [Keep an inventory ledger](https://snowch.github.io/monte-carlo-lab/lessons/keep-an-inventory-ledger.html) | Support | Stock ledger and delivery timing are explicit. Define backorder as unmet demand retained for later delivery, contrasting that policy with the page's lost-sales convention. |
| 41. [A queue remembers earlier arrivals](https://snowch.github.io/monte-carlo-lab/lessons/a-queue-remembers-earlier-arrivals.html) | Gap | Explain inter-arrival as the gap between arrivals, and steady state as a distribution no longer changing with time under stable conditions. Relate arrival rate times mean service work to capacity before asking learners to interpret growing waits. |
| 42. [Failure and repair use up time](https://snowch.github.io/monte-carlo-lab/lessons/failure-and-repair-use-up-time.html) | Covered | Finite-window availability, clipping and the long-run reference are explained and distinguished. No additional gap found. |
| 43. [Vectorise without changing the question](https://snowch.github.io/monte-carlo-lab/lessons/vectorise-without-changing-the-question.html) | Covered | Vectorisation is explicitly defined and checked against a loop. The array-equality check is present; depends on an array primer from 1–2. |
| 44. [Compare options in the same possible world](https://snowch.github.io/monte-carlo-lab/lessons/compare-options-in-the-same-possible-world.html) | Support | The paired-world comparison is explained. Before the covariance hint, show that variance of B−A equals Var(B)+Var(A)−2Cov(A,B), with a plain-language explanation of the reduction. |
| 45. [Give every part of the domain a turn](https://snowch.github.io/monte-carlo-lab/lessons/give-every-part-of-the-domain-a-turn.html) | Covered | Strata, allocations and weighting are explained operationally. No additional gap found. |
| 46. [Pair opposite draws](https://snowch.github.io/monte-carlo-lab/lessons/pair-opposite-draws.html) | Covered | Opposite draws and the monotonicity condition are explained. Relies on the earlier covariance bridge. |
| 47. [Subtract a fluctuation you can explain](https://snowch.github.io/monte-carlo-lab/lessons/subtract-a-fluctuation-you-can-explain.html) | Gap | Bias and unbiasedness are used without an explicit repeated-simulation definition. Explain systematic average error versus random error in one run, then why the known-mean adjustment has zero expectation. |
| 48. [Spread points with randomised Sobol sampling](https://snowch.github.io/monte-carlo-lab/lessons/spread-points-with-randomised-sobol-sampling.html) | Covered | Randomised Sobol points, independent scrambles and powers-of-two sample sizes are described. No additional mathematical prerequisite is needed for the stated activity. |
| 49. [Define what a bad outcome costs](https://snowch.github.io/monte-carlo-lab/lessons/define-what-a-bad-outcome-costs.html) | Covered | The loss objective is defined. Requires the positive-part notation gloss from 33. |
| 50. [Compare feasible options](https://snowch.github.io/monte-carlo-lab/lessons/compare-feasible-options.html) | Support | The feasibility procedure is explained. Read argmin as the option achieving the smallest loss, distinct from min as the smallest loss value. |
| 51. [Inspect the downside as well as the mean](https://snowch.github.io/monte-carlo-lab/lessons/inspect-the-downside-as-well-as-the-mean.html) | Covered | Quantile, tail mean and the handling of ties are explicitly distinguished. No VaR/CVaR prerequisite is needed. |
| 52. [Find where the decision changes](https://snowch.github.io/monte-carlo-lab/lessons/find-where-the-decision-changes.html) | Gap | The change task asks learners to look for interactions without defining one. Show how the effect of changing demand can depend on the shortage penalty. |
| 53. [What would better information be worth?](https://snowch.github.io/monte-carlo-lab/lessons/what-would-better-information-be-worth.html) | Sequence | Regret is introduced clearly. The inserted illustration uses EVPI and min/expectation ordering before paragraph 2 defines the information-value quantity. Move or annotate that illustration. |
| 54. [A policy can respond to new information](https://snowch.github.io/monte-carlo-lab/lessons/a-policy-can-respond-to-new-information.html) | Support | The policy's response to information is explained. Gloss latent as unobserved and state what information the policy actually sees. |
| 55. [Test a small case you can solve](https://snowch.github.io/monte-carlo-lab/lessons/test-a-small-case-you-can-solve.html) | Covered | Verification, solvable cases and boundary checks are explained. Assertion syntax belongs in the earlier NumPy/code refresher. |
| 56. [Compare predictions with observations](https://snowch.github.io/monte-carlo-lab/lessons/compare-predictions-with-observations.html) | Support | Held-out data are explained. Clarify nominal as the model's stated level and why discrete counts can put less than 10% strictly above a nominal P90 cutoff. |
| 57. [Push the boundaries deliberately](https://snowch.github.io/monte-carlo-lab/lessons/push-the-boundaries-deliberately.html) | Covered | Invariant checks and accounting identities are introduced with inspectable examples. No additional gap found. |
| 58. [Give parallel runs independent streams](https://snowch.github.io/monte-carlo-lab/lessons/give-parallel-runs-independent-streams.html) | Covered | SeedSequence and separate random streams are explained for the activity. A stream can be linked back to the repeatable sequence in 5. |
| 59. [Write a claim the evidence supports](https://snowch.github.io/monte-carlo-lab/lessons/write-a-claim-the-evidence-supports.html) | Covered | The conditional claim, assumptions and numerical uncertainty are explained. Reuses earlier interval concepts. |
| 60. [Publish your own investigation](https://snowch.github.io/monte-carlo-lab/lessons/publish-your-own-investigation.html) | Support | The capstone choices are appropriate transfer tasks. Add a short units/model brief for each starter and identify the πr² area relation in the measurement case; define the CSV column's meaning per selected case. |

### Advanced route

| Page | Status | Finding / smallest useful repair |
| --- | --- | --- |
| 61. [Invert a cumulative distribution](https://snowch.github.io/monte-carlo-lab/lessons/invert-a-cumulative-distribution.html) | Support | CDF and inverse mapping are explicitly introduced. Define generalised inverse as the smallest x reaching the requested cumulative probability, or keep that technical qualification optional. |
| 62. [Accept or reject a proposal](https://snowch.github.io/monte-carlo-lab/lessons/accept-or-reject-a-proposal.html) | Covered | Target, proposal, envelope and rejection rule are explained. Logarithms and elementary densities are declared advanced prerequisites. |
| 63. [Weight samples from another distribution](https://snowch.github.io/monte-carlo-lab/lessons/weight-samples-from-another-distribution.html) | Support | The target/proposal weighting rule is explained. Replace suitable moments with the needed finite-variance condition for the weighted contribution when using ordinary MCSE. |
| 64. [A proposal must reach the answer](https://snowch.github.io/monte-carlo-lab/lessons/a-proposal-must-reach-the-answer.html) | Gap | Derive the complete mixture density before using its reciprocal: an 80% uniform draw on [0,.5] plus a 20% draw on [0,1] gives density 1.8 on the left and .2 on the right. Identify density as reciprocal interval width for each uniform component. |
| 65. [Keep weights stable on a log scale](https://snowch.github.io/monte-carlo-lab/lessons/keep-weights-stable-on-a-log-scale.html) | Gap | logsumexp is named as the recipe without being defined. Show log(sum(exp(log weights))) and a max-shift example. Likelihood first appears here before its Bayesian definition in 69; use density products or give a short meaning. |
| 66. [See a rare event more often](https://snowch.github.io/monte-carlo-lab/lessons/see-a-rare-event-more-often.html) | Covered | Rare-event reweighting reuses the earlier importance-sampling rule. No additional concept gap found once those foundations are repaired. |
| 67. [When one weight dominates](https://snowch.github.io/monte-carlo-lab/lessons/when-one-weight-dominates.html) | Sequence | The code uses a self-normalised weighted estimate before lesson 68 explains the ratio estimator. Add the ratio and its status locally or teach 68 before this diagnostic. |
| 68. [An unknown normalising constant](https://snowch.github.io/monte-carlo-lab/lessons/an-unknown-normalising-constant.html) | Gap | Consistency is required by the quiz without being defined. Contrast approach to the target as n grows with unbiasedness at a fixed n. Define second moment as E[X²]; mark the gamma-function reference as an optional supplied check. |
| 69. [Update a probability with evidence](https://snowch.github.io/monte-carlo-lab/lessons/update-a-probability-with-evidence.html) | Gap | Clarify likelihood as a function of the parameter with observed data fixed. Give the beta mean a/(a+b), one concentration example, and the meaning of the printed 95% posterior interval before asking about stronger priors. |
| 70. [Sample a posterior directly](https://snowch.github.io/monte-carlo-lab/lessons/sample-a-posterior-directly.html) | Support | Posterior uncertainty versus numerical error is explained. Correct the claim that their units differ: p's posterior SD and MCSE for a probability estimate are both dimensionless; they describe different quantities. |
| 71. [Build a Metropolis chain](https://snowch.github.io/monte-carlo-lab/lessons/build-a-metropolis-chain.html) | Gap | Define symmetric proposal before using the symmetric ratio, and explain preserving a stationary distribution versus reaching it from a chosen start. Explain the purpose and limitations of warm-up, not just its removal. |
| 72. [Correct an asymmetric proposal](https://snowch.github.io/monte-carlo-lab/lessons/correct-an-asymmetric-proposal.html) | Gap | Read q(y\|x) as the density of proposing y from current x; identify current x, candidate y and target π locally. Define stationary distribution and translate irreducibility as reachability of relevant target regions. |
| 73. [Update one conditional at a time](https://snowch.github.io/monte-carlo-lab/lessons/update-one-conditional-at-a-time.html) | Support | Gibbs updates, the latest-coordinate rule and a sweep are explained. Define lag-one correlation as correlation between neighbouring recorded states before the reported diagnostic. |
| 74. [Account for serial dependence](https://snowch.github.io/monte-carlo-lab/lessons/account-for-serial-dependence.html) | Gap | Stationarity, lag sums, integrated correlation time and the FFT-based truncation arrive together. Work a short lag/ESS example first; label FFT as the optional fast implementation. Explain the AR(1) recurrence and its N(1−ρ)/(1+ρ) reference. |
| 75. [Compare multiple chains](https://snowch.github.io/monte-carlo-lab/lessons/compare-multiple-chains.html) | Gap | Rank-normalisation and folding are named without a small operational example. Explain pooled ranks → normal scores, and absolute deviations from the pooled median. Bulk/tail ESS and energy/geometry diagnostics need optional further-study labels. |
| 76. [Predict new observations](https://snowch.github.io/monte-carlo-lab/lessons/predict-new-observations.html) | Support | The two-stage posterior predictive construction is explained. A frequentist p-value appears only in the final warning; remove that dependency or link an optional definition rather than requiring a hypothesis-testing detour. |

### Optional application workbooks

| Page | Status | Finding / smallest useful repair |
| --- | --- | --- |
| 77. [Sizing and total cost](https://snowch.github.io/monte-carlo-lab/lessons/sizing-and-total-cost.html) | Gap | Expand TCO and define the stated cost boundary, capex, kW versus kWh, compound annual growth and the .8 usable-capacity factor. Work one capacity/energy/cost chain and label the five-year totals as undiscounted. |
| 78. [Migration deadline and budget](https://snowch.github.io/monte-carlo-lab/lessons/migration-deadline-and-budget.html) | Gap | Parallel preparation tasks and parallel running of old/new services have different meanings. Define the latter before its daily charge; gloss cutover and rollback where mentioned. |
| 79. [GPU job and checkpoint economics](https://snowch.github.io/monte-carlo-lab/lessons/gpu-job-and-checkpoint-economics.html) | Gap | Define checkpoint as saved progress used to resume, overhead as time spent saving it, and hazard as conditional interruption rate. Show one failed attempt followed by a successful chunk with its time ledger. |

### Entry and reference pages

| Page | Status | Finding / smallest useful repair |
| --- | --- | --- |
| [Course overview](https://snowch.github.io/monte-carlo-lab/) | Support | The core/advanced/workbook routes and Before you start link are clear. Topic names in the contents are not counted as unexplained concepts. Make the repaired probability/array refresher easy to find from this entry point. |
| [Field notes](https://snowch.github.io/monte-carlo-lab/field-notes.html) | Support | The glossary supplies useful definitions, including stationarity and warm-up, but essential first-use teaching cannot rely on opening it. Align the basic-Python promise with the author document's array assumption. Correct the unconditional claim that lessons introduce every term before use. |

## Recommended repair order and evidence limits

1. Repair lessons 1–4 and the prerequisite contract. These changes support nearly every later page.
2. Add local notation keys and adjust illustration placement where definitions follow the figure.
3. Repair intervals 16–18, parameter mapping 21, core mathematics 27–28 and the state/queue bridges.
4. Repair the advanced weighting, Bayesian and MCMC prerequisite chains.
5. Add the workbook domain introductions and complete the smaller Support items.

Keep one main outcome per lesson and the current quiet reading flow. Put essential meaning at first use; use a small refresher link for repeated reference. The remedy should not recreate duplicate goal cards, long visible glossaries or a forest of optional panels.

After content changes, verify that a learner can read, predict, make the requested change and answer the transfer question with optional panels closed. Re-run the repository's native, build/link and browser checks when course content or rendering changes. Check novice comprehension separately: this source/sequence audit is author review, not evidence of improved learning.

**Validation for this review record:** all 79 lesson/workbook slugs are covered exactly once, plus the overview and field notes; relative report links and documentation whitespace were checked. No course source, generated site or deployment was changed. No execution suite was rerun for these documentation-only findings.
