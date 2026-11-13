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


## 2026-11-13 — visual clutter review

Prompted by the user's tablet screenshots and concern that the UI is noisy. Reviewed the live overview plus first, middle and capstone lessons at 390px, 820px and 1440px. This is a design review; it makes no frontend or deployment change. Browser observations and screenshots are held in the workspace's `scratch/course-ui-review/` directory.

The shared lesson template exposes too much supporting structure at once. At 820px, this course's first explanatory paragraph starts at about 581px and its editor at 1603px. These coordinates are observations of the current initial state, not usability targets or learner-study results. Prior tests checked execution, readability and reflow; they did not establish low cognitive load.

High-priority recommendations:

1. Use one compact lesson navigation bar. Keep one small module/lesson context line, title and one-sentence learning intention. Remove the duplicate outcome card and permanent numbered jump-navigation row from ordinary short lessons.
2. Create an editorial reading flow with plain headings and whitespace. Reserve framing for the executable workspace and meaningful exceptional states. Present the change task and ordinary answer choices without separate coloured or bordered cards.
3. Replace the empty pre-run result panel and repeated ready/no-result/device messages with one compact status. Show the result area after execution; keep one clear provenance label then. Expose Stop during execution and export after a completed run. Keep error, stale-output and recovery information available when relevant.
4. Put runtime details, keyboard help, downloads and ancillary actions behind a secondary control. Make notes and hints optional disclosures. Keep source/provenance and scientific or mathematical limitations available without repeating boilerplate throughout every lesson.
5. Preserve the current large reading/code type, course depth, predictions, experiments, transfer questions and accessibility. The target is a calmer presentation of the same learning design, rather than adding another colour scheme or reducing text size.

Course-specific findings: The first lesson repeats its exact learning goal in the standfirst and the outcome card. Its navigation, empty output and supporting panels reproduce the Scientific Method Lab clutter. The overview also stacks a hero, process strip, route cards, progress panel and a large 12-module curriculum. Preserve the core/advanced/workshop distinction, but present it with a compact route selector and a quieter curriculum.

Proposed default sequence: compact course context; title and one goal; explanation; prediction and experiment; actual results when present; one practice question; next lesson. Optional help belongs beside the relevant activity. Scientific Method Lab is the appropriate reference for a later shared-template simplification, followed by Monte Carlo Lab and SymPy Lab.

Evidence gap: this is a screenshot/live-browser and author review, not an observed learner study. The user's screenshots provide real qualitative evidence that the existing visual hierarchy is distracting. A revised design should be checked at tablet widths as well as the existing phone and desktop widths, including before-run, running, error and completed-result states.


## 2026-11-13 — quiet interface implementation

Implemented the clutter review across the course overview and lesson layout.
The shared renderer is in `scripts/quiet.mjs`, with local copies in each course
so deployment remains independent. `src/quiet.css` is combined into the existing
content-fingerprinted stylesheet.

- One compact header, one context line and one visible learning goal. Removed
  the duplicate outcome card, numbered section-jump bar and secondary mobile bar.
- Prediction questions remain visible; recording a prediction and writing notes
  are optional. Saved text reopens its disclosure. Ordinary instructions, answer
  options, change tasks and reading marks use lightweight editorial styling.
- No empty pre-run output panel or repeated readiness/device boilerplate. Actual
  output and its provenance appear after a result. Stop appears during execution;
  export appears for a recorded run. Runtime information and downloads are under
  Tools. Escape restores focus from support menus.
- Native module disclosures replace the overview's card grid and marketing
  sections. Search opens matching modules, clearing search restores their prior
  state, and module hashes open their target. Example previews and portable-work
  controls remain available below the curriculum.
- SymPy's refreshers remain available as quiet disclosures; labelled equations
  share an unboxed results area. Code, mathematical examples, CSV interfaces,
  reports, exact-source exports and package versions are preserved.

Fresh 820px-wide before/after inspection of the first lesson: explanation starts
at approximately 581px → 255px; editor starts at 1603px → 922px;
initial page height is 4299px → 2608px. These are measured rendering
coordinates for this sample, not learning-outcome claims. Also inspected 390px
and 1440px screenshots. Main reading text remains 20px on desktop/tablet and
18px on phones, with 16px code.

Verification retains the full native and real-Wasm suites, plus initial-state
checks and targeted 820/1024px regressions for tablet navigation, optional tools,
search, module deep links and source access. Existing phone, 200% text, saved
draft, progress, mathematical output, CSV/report, error/Stop and static-reading
checks remain in place. This visual/functional review does not replace a learner
study; further density feedback from actual course use remains valuable.

Local verification completed: the full native and real-Wasm browser suites passed
for the quiet layout. After the final focus/save-error adjustments, rebuilt all
three sites, rechecked their local links and ran focused browser checks for
820/1024px navigation and deep links, Stop focus return, cancelled-run output,
optional hints/notes, saved text reopening and unavailable-storage alerts.
GitHub Actions runs the complete suite again before each Pages deployment.
