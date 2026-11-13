# Review record

## Scope and sources

Monte Carlo Lab implements 60 core lessons in ten modules, 16 optional advanced lessons in two modules and three optional infrastructure workbooks. Core examples deliberately span attendance, projects, inventory, measurement, reliability and integration. The final core investigation supports three CSV-based starters and an exportable report.

Primary sources: NumPy Generator and SeedSequence documentation; SciPy distribution, fitting, bootstrap, quasi-Monte Carlo and logsumexp documentation; Art Owen's *Monte Carlo theory, methods and examples*; Vehtari et al.'s rank-normalised/folded R-hat paper. Individual lessons cite their relevant source. Original examples use invented values or seeded teaching simulations, labelled at point of use. No empirical business or performance validation is claimed.

The reading shell, large-type styling and workflow were adapted from Scientific Method Lab. Assembly Lab informs the short investigation pattern; Event Streaming Lab informs the browser editor/worker. These are acknowledged in the course and README; package and font licences are retained.

## Learning-design review

The essential route, with optional panels closed, states an outcome, explains one idea in three paragraphs, asks for a prediction and makes Run Python the next action. Inputs are inspectable in complete standalone source. Each lesson includes a deliberate modification, a fresh transfer case, two progressive hints, explanatory feedback, a source and a limitation. The integrated capstone is longer than ordinary lessons by design. Estimates describe initial guided work, not the duration of independent investigation.

The progression separates outcome variation, numerical error, input uncertainty and model uncertainty before decisions. It challenges independence assumptions before stateful models. Advanced sampling starts with known references; MCMC first constructs an analytically tractable posterior, retains rejected states and distinguishes chain agreement from target coverage. The simplified mean-ESS example explicitly states its single-chain stationarity assumptions and does not claim full modern bulk/tail ESS.

Explicit boundaries include finite initially empty queues, healthy-start availability, fixed fleet TCO, a finite EVPI action list and interruption-free checkpoints. Scenarios receive no implied probabilities. Feasibility based on estimated probability is labelled as a point-estimate comparison. Uploaded CSV structure does not establish suitable evidence. Reading marks are not mastery.

## UX review

Before implementation: retain 20px desktop / 18px phone explanatory text, 16px code and output and at least 14px supporting text; rem-based scaling; separate quiet reading and functional editor areas. Replace scientific-method branding with a simulation-led overview and clear core/advanced/workbook choices.

After implementation: inspected desktop overview, lesson and phone screenshots. The first lesson's executed attendance histogram introduces a concrete question, not a decorative generic diagram. Large Sora headings, DM Sans prose, white reading surfaces, restrained blue and mint accents, and a dark editor provide hierarchy. Code and results stay in one flow on ordinary laptops. The overview provides search, resume and portable drafts; long contents are grouped into collapsible modules. Phone contents has a labelled toggle and Escape recovery.

Loading, completed, stale, error and stopped states identify what the displayed result describes. Reset restores the authored source; Stop kills the worker and the next Run can recover. Export preserves exact executed source and input independently of later edits. Upload size and Python validation errors are recoverable. Keyboard labels, focus styles, skip navigation and no-JavaScript reading are retained. Fonts and runtime assets are served locally with Pages-relative paths.

## Verification

Native and browser checks are automated in `npm run check`. The build executes all 79 sources and generates worked output/figures; no worked output is hand authored. Native checks exercise analytical probability references, importance-weighted rare-event accuracy, project and inventory invariants, value-of-information ordering, known MCMC targets, diagnostic scale disagreement and all three capstone paths, including invalid CSV.

The browser suite executes all 79 exact sources through the real locally served Wasm runtime and compares numbers with native worked records. It also checks charts, CSV replacement/validation, exact-source run and Markdown exports, error and Stop recovery, answer feedback, saved notes/code, progress import in a fresh context, light/dark themes, every route at 390px and 320px, 200% text reflow and static reading without JavaScript. Relative-link checks cover all 81 generated pages.

Screenshots, exported run records and progress fixtures are produced under `test-results/`, uploaded as CI evidence. Final check and deployment results are recorded in the GitHub Actions run linked from the repository.

## Evidence gaps

These are author review, executable statistical checks and browser checks, not learner validation. No novice usability study or learning-outcome evaluation has been conducted. Claims about comprehension, completion time and transfer effectiveness remain unvalidated. A useful next evaluation is to observe novices on the first overflow investigation, one dependence lesson, a precision exercise and a fresh capstone without hints, recording task success and misconceptions.
