# Learning design

Audience: people who can read Python variables, arrays, function calls and a short loop. No prior simulation or Bayesian inference is assumed. Probability, expectation and conditioning are introduced before later algorithms use them. Advanced modules assume the core route, comfort with logarithms and an introductory understanding of probability densities; reference notes supply the needed notation.

Practical outcomes: translate a decision into a trial; specify and challenge input assumptions; implement a repeatable simulation; distinguish outcome spread, numerical error and input/model uncertainty; represent dependence and time; compare policies; validate an estimator against a solvable reference; communicate an auditable conditional claim. Advanced learners additionally construct weighted and Markov-chain estimators and assess their limitations.

Sequence: ten core modules of six lessons (60), then two optional advanced modules of eight (16). Three optional infrastructure workbooks demonstrate transfer without defining the course's main audience. Each investigation has one stated outcome, three short explanatory paragraphs, inspectable inputs, a prediction, complete executable Python, an observation prompt, one deliberate change, a fresh transfer question, two progressive hints and explanatory feedback. Estimated times are for an initial pass; debugging, changes and project work take longer.

Misconceptions addressed explicitly: a seed validates a model; more trials remove bad assumptions; trial count and individual readings are interchangeable; outcome quantiles are confidence intervals; zero observed failures imply zero risk; zero correlation implies independence; scenario labels imply probabilities; a percentile uniquely determines a decision; weight ESS guarantees coverage; accepting many MCMC proposals establishes convergence; R-hat near one proves every mode was visited; a posterior interval is a frequentist confidence interval.

Evidence: all inputs identify invented or simulated provenance. Worked examples are generated from exact published Python; browser output appears only after execution. Primary method references appear per lesson. Capstone input validates CSV structure rather than real-world suitability. Reading marks are self-reported progress, not mastery. Author review and automated checks are not learner validation; no novice study has been conducted.

## Optional lesson 0: probability essentials

Outcome: read the opening attendance model in plain language, identifying a
guest's chance, the independence assumption and one whole-event trial. The
refresher assumes only fractions/percentages and reading basic Python; explain
the conversion between a fraction and a percentage at first use. It is an
optional 7-minute preparation page, outside the 76-lesson progress denominator.
Existing lesson numbers and saved lesson identities remain unchanged.

Use four explicitly invented three-guest events, represented first as a visual
table and then ordinary nested Python lists. Count attendees with a loop, apply
the strict two-seat overflow boundary and compute the observed event fraction.
These hand-picked examples demonstrate the calculation; they are not random
draws, evidence about real attendance or a probability estimate justified by
four observations. The main course introduces random simulation in lesson 1.

Address likely misconceptions: 72% forces exactly 72 of every 100 attendees;
independent means mutually exclusive; one guest is a whole overflow trial;
the guest chance equals overflow risk; exactly full means overflowing. One
prediction, a seat-count change and a fresh independent-attendance scenario
provide the learning activity. Keep the diagram free of new mathematical
notation, use labels as well as colour, and put it after the explanations.
Explain the essential probability/independence meanings briefly in lesson 1
too, so skipping the optional page remains viable. Later distribution families,
variance and inference are outside this refresher's scope.

Entry points: a quiet overview link, a sidebar entry and a lesson-1 reminder.
Lesson 0 has an explicit skip link and leads to lesson 1; lesson 1 can return to
it. Reading status/drafts and portable exports work on this page without
increasing the main progress count. Evaluate navigation, real Python execution,
feedback and saved work, plus no-JavaScript reading and narrow-screen reflow.

UX baseline: retain the revised Scientific Method Lab's large readable type and single-column code/output flow on ordinary laptops. Give the Monte Carlo course its own simulation-led overview, clear core/advanced/workbook routes, accessible controls, visible execution states, editable error recovery, portable records and a phone contents menu. Review the route with optional panels closed before release.

## Quiet presentation

Keep the learning structure while reducing simultaneous scaffolding. Present one
plain learning goal followed by explanation, a visible prediction question, the
experiment and a transfer case. Recording the prediction and keeping field notes
are optional disclosures; saved text reopens them on return. Progressive hints,
worked examples and runtime tools stay available beside the relevant activity.
Results appear after execution, with clear provenance and recoverable error/Stop
states. Course modules are native disclosures; search opens matching modules and
module deep links reveal their contents. Mathematical refreshers remain optional,
readable disclosures where the course provides them.

## Visual reasoning and notation revision

Add one specific reference illustration to each core, advanced and application
lesson. Explain trial boundaries, distributions, numerical error, model inputs,
dependence, path state, variance reduction, decisions, weighted estimators and
MCMC with the representation that fits the idea. Label reference assumptions,
simulations, units and targets. References are separate from the learner's run;
more precise simulation never validates the assumed real-world model.

Typeset mathematical expressions; preserve literal Python as code. Retain a
single goal, prediction, executable source, deliberate change and transfer task.
Show the opening attendance distribution from the actual executed source, with
an explicit strict overflow boundary. Provide phone/desktop versions of the same
executed plots without redrawing random inputs or changing simulated outcomes.
Group code, actual results and the worked reference; preserve drafts, CSVs,
reports, provenance, cancellation and the existing accessible recovery paths.
Review reference label bounds and equation fit on small screens, plus actual
plots in light/dark reading layouts. Author/browser checks do not demonstrate
learning effectiveness.
