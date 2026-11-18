# Full wording and interface review

## Opening check

The baseline was `74bc62e`. Consulted the repository [learning-design guidance](../.agents/skills/learning-design/SKILL.md),
[UX guidance](../.agents/skills/ux/SKILL.md), [concept remediation](concept-remediation.md)
and [earlier experiment review](review.md#2026-11-17--experiment-instructions-and-run-recovery).
The core assumes basic Python, including variables, function calls and a short
loop. Optional lesson 0 prepares readers for the attendance example. The
advanced sequence assumes the core, logarithms and elementary densities.

Reviewed the course overview, field notes and each investigation with optional
help closed. Compared headings, learning prose, plot captions, controls, labels,
prediction, practice and feedback with the editable source and its actual
results. The concept review had already made most terms readable where they
first appear. The opening pass found that only three pages explicitly identified
the original-run action and some change tasks still left a learner to guess a
value, a matching formula, a code location or a result field. This could produce
an output label that described the original setting after an edit. The notes
also displayed a saved claim before any successful write, and denied storage
could produce an empty progress download with a success message.

## Route checks

| Page | Published and edited evidence checked |
| --- | --- |
| [Course overview](https://snowch.github.io/monte-carlo-lab/) | Start, optional preparation, progress, search and portable work remain available. A blocked progress read produces no file. |
| [Field notes](https://snowch.github.io/monte-carlo-lab/field-notes.html) | State prerequisites, clarify output that remains after failure, and distinguish progress transfer from run, CSV and report records. |
| [00. Probability essentials](https://snowch.github.io/monte-carlo-lab/lessons/probability-essentials.html) | Count the four invented events and compare 1 of 4 with 3 of 4 when the seat limit changes. |
| [01. Will the room be full?](https://snowch.github.io/monte-carlo-lab/lessons/will-the-room-be-full.html) | Keep the seeded attendance and move the boundary from 110 to 120. The mean stays 107.98 and the modelled overflow fraction falls from 0.3211 to 0.0105. |
| [02. What counts as one trial?](https://snowch.github.io/monte-carlo-lab/lessons/what-counts-as-one-trial.html) | Keep eight guest decisions per row while adding events. Compare the event overflow fraction with the guest attendance fraction. |
| [03. Repeat the whole experiment](https://snowch.github.io/monte-carlo-lab/lessons/repeat-the-whole-experiment.html) | Add £100 of fixed cost. The mean moves from £74.80 to −£25.20 and every printed profit quantile falls by £100. |
| [04. See the outcomes before the headline](https://snowch.github.io/monte-carlo-lab/lessons/see-the-outcomes-before-the-headline.html) | Edit only the largest invented delay. Mean 4→5.5, median 3→3 and P90 6→7.5 days describe those ten values. |
| [05. Reproduce a random run](https://snowch.github.io/monte-carlo-lab/lessons/reproduce-a-random-run.html) | Consume one draw from the replay generator. The published replay matches and the edited replay differs. |
| [06. Check against an exact answer](https://snowch.github.io/monte-carlo-lab/lessons/check-against-an-exact-answer.html) | Include 110 attendees in both methods. The exact reference uses a strict tail above 109. |
| [07. Sample weighted alternatives](https://snowch.github.io/monte-carlo-lab/lessons/sample-weighted-alternatives.html) | Move 0.1 of probability from standard to premium and read the two sample frequencies and mean cost. |
| [08. Count successes in a fixed group](https://snowch.github.io/monte-carlo-lab/lessons/count-successes-in-a-fixed-group.html) | Lower the pass chance to 0.5 and compare the separate sample and model means and variances. |
| [09. Count arrivals in an interval](https://snowch.github.io/monte-carlo-lab/lessons/count-arrivals-in-an-interval.html) | Keep the hourly rate fixed and extend the duration. The model expected count rises from 2 to 8 and zero counts become rarer. |
| [10. Wait for the next event](https://snowch.github.io/monte-carlo-lab/lessons/wait-for-the-next-event.html) | Double the hourly rate, compare the unconditional and conditional means, and retain the half-hour cutoff. |
| [11. Model symmetric variation](https://snowch.github.io/monte-carlo-lab/lessons/model-symmetric-variation.html) | Expose the error SD as a setting. Doubling it doubles the reading SD while the fraction inside two error SDs stays 0.9532. |
| [12. Keep positive quantities positive](https://snowch.github.io/monte-carlo-lab/lessons/keep-positive-quantities-positive.html) | Increase log-scale SD. Read the unchanged model median and larger arithmetic mean. |
| [13. Two different kinds of spread](https://snowch.github.io/monte-carlo-lab/lessons/two-different-kinds-of-spread.html) | Double the outcome SD and compare spread within batches and spread of their means at the same draw counts. |
| [14. Watch convergence without promising a winner](https://snowch.github.io/monte-carlo-lab/lessons/watch-convergence-without-promising-a-winner.html) | Recheck the exact 6,400→10,000 edit. RMSE for 10,000 draws is about one tenth of that for 100 in this run. |
| [15. Calculate Monte Carlo standard error](https://snowch.github.io/monte-carlo-lab/lessons/calculate-monte-carlo-standard-error.html) | Increase draws fourfold and compare the three independently interpretable numerical-error rows. |
| [16. An interval for a simulated mean](https://snowch.github.io/monte-carlo-lab/lessons/an-interval-for-a-simulated-mean.html) | Change to 20 skewed outcomes and check a second seed against the known expectation. Interval endpoints are numerical uncertainty for a mean. |
| [17. When zero failures is not zero risk](https://snowch.github.io/monte-carlo-lab/lessons/when-zero-failures-is-not-zero-risk.html) | Compare two distinct upper-bound conventions when the failure-free count is 1,000 or 10,000. |
| [18. Plan a precision budget](https://snowch.github.io/monte-carlo-lab/lessons/plan-a-precision-budget.html) | Add a half-width of 0.005 and compare the planned count with 0.01. This is a planning calculation. |
| [19. An input needs a source](https://snowch.github.io/monte-carlo-lab/lessons/an-input-needs-a-source.html) | Add a service-time SD with a unit and assumption label. The input table does not certify its source. |
| [20. Sample the observations you have](https://snowch.github.io/monte-carlo-lab/lessons/sample-the-observations-you-have.html) | Add one invented observation at 150 and inspect the resampled upper range and the empirical model’s tail fraction. |
| [21. Fit a shape and inspect the fit](https://snowch.github.io/monte-carlo-lab/lessons/fit-a-shape-and-inspect-the-fit.html) | Remove the largest observation for a separate sensitivity comparison and inspect both P90 values. |
| [22. Turn an expert estimate into a model](https://snowch.github.io/monte-carlo-lab/lessons/turn-an-expert-estimate-into-a-model.html) | Increase the expert hard bound from 12 to 20 and compare the model mean and upper quantile. |
| [23. The parameters are estimates too](https://snowch.github.io/monte-carlo-lab/lessons/the-parameters-are-estimates-too.html) | Copy every invented row ten times. The bootstrap interval narrows even though the edit supplies no new information. |
| [24. A scenario is not a probability](https://snowch.github.io/monte-carlo-lab/lessons/a-scenario-is-not-a-probability.html) | Add a separate extreme scenario. The new conditional probability does not imply a scenario weight. |
| [25. Independence changes the answer](https://snowch.github.io/monte-carlo-lab/lessons/independence-changes-the-answer.html) | Add the lower-tail print to the loop. Read independent and shared input totals on both sides of the mean. |
| [26. Make the shared cause visible](https://snowch.github.io/monte-carlo-lab/lessons/make-the-shared-cause-visible.html) | Redraw the spending factor independently. Compare the printed correlation and revenue summaries. |
| [27. Correlation does not tell the whole story](https://snowch.github.io/monte-carlo-lab/lessons/correlation-does-not-tell-the-whole-story.html) | Draw a near-linear alternative, update the plot label and expect the original absolute-value diagnostic to disagree. |
| [28. Generate correlated normal inputs](https://snowch.github.io/monte-carlo-lab/lessons/generate-correlated-normal-inputs.html) | Switch correlation from +0.7 to −0.7. Compare marginal variance estimates, covariance and total-cost SD. |
| [29. Sample one condition after another](https://snowch.github.io/monte-carlo-lab/lessons/sample-one-condition-after-another.html) | Match the mean with a fixed-chance count and print the same high-attendance event in each case. The model means are both 71 and the fractions differ. |
| [30. Stress-test the dependency assumption](https://snowch.github.io/monte-carlo-lab/lessons/stress-test-the-dependency-assumption.html) | Add the intermediate correlation row. Apply the same conditional decision threshold to each row without weighting them. |
| [31. Will the project finish on time?](https://snowch.github.io/monte-carlo-lab/lessons/will-the-project-finish-on-time.html) | Raise the second task’s maximum to 16 days and compare the completion quantiles with the same deadline. |
| [32. How much contingency is enough?](https://snowch.github.io/monte-carlo-lab/lessons/how-much-contingency-is-enough.html) | Compare three reserve coverage levels on the same trial costs. The baseline budget stays fixed. |
| [33. Enough food without too much waste](https://snowch.github.io/monte-carlo-lab/lessons/enough-food-without-too-much-waste.html) | Increase the shortage penalty to 30. Compare the chosen meal count and unchanged shortage probabilities. |
| [34. How uncertain is a calculated measurement?](https://snowch.github.io/monte-carlo-lab/lessons/how-uncertain-is-a-calculated-measurement.html) | Add one shared offset per measurement trial. Compare area summaries at the same physical specification. |
| [35. How reliable is a whole product?](https://snowch.github.io/monte-carlo-lab/lessons/how-reliable-is-a-whole-product.html) | Add a common service failure and inspect the parallel result against the independent baseline. |
| [36. Estimate an integral by sampling](https://snowch.github.io/monte-carlo-lab/lessons/estimate-an-integral-by-sampling.html) | Move the integration interval to 1–3. The existing exact formula updates and the estimate still uses interval width. |
| [37. Follow a random walk](https://snowch.github.io/monte-carlo-lab/lessons/follow-a-random-walk.html) | Give a positive step probability of 0.55. Compare whether a path ever crosses with where it finishes. |
| [38. Move between states](https://snowch.github.io/monte-carlo-lab/lessons/move-between-states.html) | Compare the original clear start and the wet start at steps 1, 5 and 20. The first step differs most in this comparison. |
| [39. Parallel work changes the critical path](https://snowch.github.io/monte-carlo-lab/lessons/parallel-work-changes-the-critical-path.html) | Add a half-serial policy. Its median 11.481 days sits between the original serial and parallel medians. |
| [40. Keep an inventory ledger](https://snowch.github.io/monte-carlo-lab/lessons/keep-an-inventory-ledger.html) | Increase lead time from two to four and compare lost sales and final stock under the unchanged reorder rule. |
| [41. A queue remembers earlier arrivals](https://snowch.github.io/monte-carlo-lab/lessons/a-queue-remembers-earlier-arrivals.html) | Raise arriving work past capacity, then increase customers per trace. Inspect the final customer’s wait rather than treating customer observations as independent. |
| [42. Failure and repair use up time](https://snowch.github.io/monte-carlo-lab/lessons/failure-and-repair-use-up-time.html) | Extend the healthy-start observation window. Read the same long-run reference on both runs. |
| [43. Vectorise without changing the question](https://snowch.github.io/monte-carlo-lab/lessons/vectorise-without-changing-the-question.html) | Apply the squared term to loop, vector and chunk forms using the same arithmetic. Check both exact comparisons. |
| [44. Compare options in the same possible world](https://snowch.github.io/monte-carlo-lab/lessons/compare-options-in-the-same-possible-world.html) | Reverse how the paired outcomes move together and update the exact reference. Paired MCSE now exceeds separate MCSE in the example. |
| [45. Give every part of the domain a turn](https://snowch.github.io/monte-carlo-lab/lessons/give-every-part-of-the-domain-a-turn.html) | Use the same bounded threshold indicator in ordinary and stratified estimates. Compare repeat-level spread at equal cost. |
| [46. Pair opposite draws](https://snowch.github.io/monte-carlo-lab/lessons/pair-opposite-draws.html) | Use the symmetric squared function in both methods and update the exact mean. Opposite draws now have the same function value. |
| [47. Subtract a fluctuation you can explain](https://snowch.github.io/monte-carlo-lab/lessons/subtract-a-fluctuation-you-can-explain.html) | Use a wrong control mean. The controlled mean shifts while its MCSE stays the same in this seeded comparison. |
| [48. Spread points with randomised Sobol sampling](https://snowch.github.io/monte-carlo-lab/lessons/spread-points-with-randomised-sobol-sampling.html) | Use the same small-region indicator and exact area with scrambled Sobol and ordinary samples. Compare across independent replicate estimates. |
| [49. Define what a bad outcome costs](https://snowch.github.io/monte-carlo-lab/lessons/define-what-a-bad-outcome-costs.html) | Change shortage cost from 10 to 3 and inspect the stock ranking with fixed demand draws. |
| [50. Compare feasible options](https://snowch.github.io/monte-carlo-lab/lessons/compare-feasible-options.html) | Recheck the 10%, 2% and 0.5% shortage limits. Selected stock shifts from 32 to 36 and the tightest limit leaves no feasible tested option. |
| [51. Inspect the downside as well as the mean](https://snowch.github.io/monte-carlo-lab/lessons/inspect-the-downside-as-well-as-the-mean.html) | Increase log-scale spread and compare mean loss, P95 and the threshold-based upper-tail mean. |
| [52. Find where the decision changes](https://snowch.github.io/monte-carlo-lab/lessons/find-where-the-decision-changes.html) | Compare two penalties across a matching demand grid. Options change at four of five grid points in the seeded example. |
| [53. What would better information be worth?](https://snowch.github.io/monte-carlo-lab/lessons/what-would-better-information-be-worth.html) | Restrict the stock menu and observe how the fixed choice and perfect-information choice depend on that list. |
| [54. A policy can respond to new information](https://snowch.github.io/monte-carlo-lab/lessons/a-policy-can-respond-to-new-information.html) | Keep the signal policy unchanged while increasing signal noise. Compare its loss with the fixed policy. |
| [55. Test a small case you can solve](https://snowch.github.io/monte-carlo-lab/lessons/test-a-small-case-you-can-solve.html) | Check the zero-stock and fractional-cost cases independently. The latter must preserve 2.5 rather than round it to 2. |
| [56. Compare predictions with observations](https://snowch.github.io/monte-carlo-lab/lessons/compare-predictions-with-observations.html) | Change the assumed mean and compare the resulting coverage fractions. Using the comparison set to choose a model means a fresh evaluation needs other evidence. |
| [57. Push the boundaries deliberately](https://snowch.github.io/monte-carlo-lab/lessons/push-the-boundaries-deliberately.html) | Introduce the documented broken allocation. Its assertion should fail, keep the successful result, and pass after Restore example. |
| [58. Give parallel runs independent streams](https://snowch.github.io/monte-carlo-lab/lessons/give-parallel-runs-independent-streams.html) | Print four same-seed batches next to spawned batches. The first draws repeat across all four same-seed generators. |
| [59. Write a claim the evidence supports](https://snowch.github.io/monte-carlo-lab/lessons/write-a-claim-the-evidence-supports.html) | Expose the model mean as a setting and print the actual target. At mean 30, the interval is still conditional on that model. |
| [60. Publish your own investigation](https://snowch.github.io/monte-carlo-lab/lessons/publish-your-own-investigation.html) | Run invented inventory and project starters. Under the same project trial budget, the printed multipliers have different deadline fractions and duration quantiles. |
| [61. Invert a cumulative distribution](https://snowch.github.io/monte-carlo-lab/lessons/invert-a-cumulative-distribution.html) | Evaluate the inverse at 0, 0.5 and 0.99 and attach units to the cutoffs. |
| [62. Accept or reject a proposal](https://snowch.github.io/monte-carlo-lab/lessons/accept-or-reject-a-proposal.html) | Change the accepted density and both comparison targets. Acceptance approaches 1/3 and the conditional mean approaches 3/4. |
| [63. Weight samples from another distribution](https://snowch.github.io/monte-carlo-lab/lessons/weight-samples-from-another-distribution.html) | Compare proposal means 0, 0.5 and 1 at the same sample size. The unweighted average changes target. |
| [64. A proposal must reach the answer](https://snowch.github.io/monte-carlo-lab/lessons/a-proposal-must-reach-the-answer.html) | Update both the component probability and its complete density, then change the seed. The smaller right-side sample can make the weighted estimate less stable. |
| [65. Keep weights stable on a log scale](https://snowch.github.io/monte-carlo-lab/lessons/keep-weights-stable-on-a-log-scale.html) | Make all three log weights equal. Direct exponentiation still underflows while stable normalisation gives thirds. |
| [66. See a rare event more often](https://snowch.github.io/monte-carlo-lab/lessons/see-a-rare-event-more-often.html) | Compare shifts 3, 5 and 7. At shift 7 the hit fraction is higher than at 5 and so is the estimated MCSE. |
| [67. When one weight dominates](https://snowch.github.io/monte-carlo-lab/lessons/when-one-weight-dominates.html) | Add shift 6 and repeat with another seed. Compare observed weight dominance with the weighted target estimate. |
| [68. An unknown normalising constant](https://snowch.github.io/monte-carlo-lab/lessons/an-unknown-normalising-constant.html) | Compare counts 100, 1,000 and 20,000 with a second seed at 1,000. Repeated numerical variation cannot alone establish finite-sample bias. |
| [69. Update a probability with evidence](https://snowch.github.io/monte-carlo-lab/lessons/update-a-probability-with-evidence.html) | Use a more concentrated beta prior with the same mean. The posterior mean shifts less after the same observations. |
| [70. Sample a posterior directly](https://snowch.github.io/monte-carlo-lab/lessons/sample-a-posterior-directly.html) | Move the event boundary in the simulation, label and exact reference. Posterior SD stays fixed while the probability estimate changes. |
| [71. Build a Metropolis chain](https://snowch.github.io/monte-carlo-lab/lessons/build-a-metropolis-chain.html) | Compare scales 0.005, 0.12 and 0.8. Movement and repeated-state fraction are distinct from the acceptance headline. |
| [72. Correct an asymmetric proposal](https://snowch.github.io/monte-carlo-lab/lessons/correct-an-asymmetric-proposal.html) | Change both the independent proposal draw and its density, then use another seed. The beta target mean stays 20/34. |
| [73. Update one conditional at a time](https://snowch.github.io/monte-carlo-lab/lessons/update-one-conditional-at-a-time.html) | Raise the dependence parameter and inspect lag-one correlation and the covariance entries. |
| [74. Account for serial dependence](https://snowch.github.io/monte-carlo-lab/lessons/account-for-serial-dependence.html) | Check 0.3 and 0.95 and a second 0.95 run against the long-run reference. The independence-based SE does not describe the chain mean. |
| [75. Compare multiple chains](https://snowch.github.io/monte-carlo-lab/lessons/compare-multiple-chains.html) | Replace scale disagreement with a location shift and change its label. Compare raw and rank/folded diagnostics on the constructed draws. |
| [76. Predict new observations](https://snowch.github.io/monte-carlo-lab/lessons/predict-new-observations.html) | Increase the group size from 20 to 100. Compare the larger variance gap between full predictive and plug-in counts. |
| [Sizing and total cost](https://snowch.github.io/monte-carlo-lab/lessons/sizing-and-total-cost.html) | Add £300 annual support per installed unit. The larger fleet’s P90 cost rises from £98,322 to £116,322 while capacity estimates stay fixed. |
| [Migration deadline and budget](https://snowch.github.io/monte-carlo-lab/lessons/migration-deadline-and-budget.html) | Charge the same 10% simulated rollback event across options. Standard joint success falls from 0.768 to 0.733 while the duration P90 stays 28.77 days. |
| [GPU job and checkpoint economics](https://snowch.github.io/monte-carlo-lab/lessons/gpu-job-and-checkpoint-economics.html) | Edit checkpoint overhead to 0.25 hours. The half-hour policy’s mean bill rises from £67.88 to £91.88 against £69.49→£75.49 for the two-hour policy. |

## Closing check

| Requested criterion | Review outcome |
| --- | --- |
| Clear wording | Added the visible first-run cue and named the editable source, literal changes, Run Python action and evidence. The cue gives way to the current editor state after an edit or CSV selection. Preserved the concept progression and revisited the worked output and captions where the edits changed their interpretation. |
| Purpose and validity | Each comparison names an evidence field and a question it can answer. Changed exact references and labels with the model when needed. Retained invented, simulated, exact-model and measured-data distinctions. |
| Progression and layout | Kept one primary Run Python action. The lesson proceeds from model and prediction to code, result, edit and fresh case. The optional CSV selector opens on demand. The edit links keyboard focus back to the code. Original output, run details, hints and notes have their own disclosures. |
| Feedback and recovery | Separated Python failure from the previous result, and selected CSV from the CSV used for that result. Saved code and backups stay available after reload. Note, report and reading-mark feedback reflect failed writes. A failed progress read does not produce a misleading download. |
| Accessibility and use | Checked ordinary result flow with optional help closed, and opened optional controls to check the tasks they support. Reviewed width, both themes, keyboard operation, Stop and error recovery, text reflow and JavaScript-free reading. |

### Functional verification

The repository checks cover 16 native tests, 82 generated routes and 7,973
links and fragments, as well as all 80 original browser simulations. Native
checks also run the literal replacements in [the exercise fixtures](../tests/lesson-edits.json).

A separate Chromium walkthrough ran every original and all 93 documented edit
variants on the actual lesson routes at 320, 390, 820 and 1,440 CSS pixels in
light and dark themes. It took the return-to-editor link by keyboard and
compared each result with its executed native counterpart, allowing numerical
rounding. The intended assertion failure preserved the last successful
output and the published source ran again after restoration. Retested the room,
the shared-failure example, the rare-event shifts and the capstone after the
last layout and status changes. Checked a rejected capstone report write, a
later successful write to a different field, the current exported text and the
older saved value after reload.

### Learning effectiveness

The author review and execution checks cover clarity, numerical results and
interface behaviour. How reliably learners interpret the evidence or transfer
these methods to a new investigation remains unmeasured.
