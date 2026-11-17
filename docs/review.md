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

## 2026-11-13 — visual explanations and readable simulation results

Applied the repository learning-design and UX skills before implementation and after screenshot review. Most lessons previously had only numerical text output, while fixed desktop figures shrank on phones. The earlier quiet shell also left the worked reference detached from the editor.

All 79 core, advanced and workbook investigations now have a specific reference illustration. Distribution shapes, full trial matrices, outcome histograms, estimator ranges, joint models, state tables and algorithm diagrams explain the relevant operation or decision. Numerical graphics use the executed published draws or explicit analytic references, with their units, domains and targets stated in captions. The independence example compares the exact triangular and uniform totals: both have mean 60, while their above-70 probabilities are 0.125 and 0.25. The native reference test checks the simulated estimates against those probabilities. References remain separate from the learner's actual run and do not claim real-world validation.

Algorithm diagrams show the operations and assumptions: parallel tasks join at a maximum, a queue inherits unfinished work, a ledger preserves demand, a control variate uses a known mean, proposal weights return to the target, rejected MCMC states stay in the chain, and predictive counts include parameter uncertainty. Comparison cases have no sequential arrows. Importance-proposal support, weight-ESS versus mean-ESS, constructed R-hat examples, fixed fleets, joint migration success and interruption accounting remain explicit. An input model, a precise estimate and a justified decision are not interchangeable.

Mathematical notation uses local KaTeX/MathML, with explicit backticks for literal Python. Long equations break across lines on phones. Large reading/code text is preserved. Violet/teal references and subdued surfaces restore hierarchy without duplicate goal cards, jump bars or idle result panels. Code, actual results and the executed reference now share one surface. Optional notes, hints, prediction recording and tools remain available. CSV/report/progress exports, saved drafts, error recovery and Stop retain their existing semantics. Course data revalidates on load to keep feedback consistent with updated markup.

The opening source now plots its actual attendance draws and a strict overflow boundary. A seat-count edit changes the risk classification and legend while retaining the seeded trials; the exported run keeps that exact source and both SVG layouts. Existing output numbers are unchanged for the default model. The delivery-delay chart labels were shortened without changing its data. A shared rendering helper creates phone/desktop layouts from the same executed figures, never resimulating them; logarithmic axes and plotted values are preserved and checked. Both layouts are exported, with full-size links. The helper and notation/reading components are adapted from the author’s Scientific Method Lab, copied locally so deployments remain independent.

Reviewed reference diagrams at 320px and 820px, selected light/dark phone figures, every generated phone chart and the actual first-lesson execution. The label/equation audit passed for all 79 references. Browser regressions check visible reference content, internal label bounds, equation fit, responsive plot sources and no-JavaScript reading. The full native/Wasm suite retains known statistical targets, weighted-tail accuracy, MCMC checks, scenario invariants, all capstone starters, CSV validation, exact-source exports, recovery, drafts, 320/390px layouts, 820/1024px navigation and 200% text. CI repeats checks before deployment and uploads evidence.

These are author, mathematical-reference and browser checks, not a learner study or proof of improved learning. Phone layouts were reviewed in Chromium at emulated widths; every physical device and browser has not been evaluated.

## 2026-11-13 — concepts introduced before explanation

Reviewed all 81 Monte Carlo Lab learning pages at f9b0ce0: 60 core lessons,
16 advanced lessons, three workbooks, the overview and field notes. Applied the
repository learning-design and UX skills to the essential route with optional
help closed. Reviewed prose, reference diagrams and rendering order, code/output
labels, predictions, changes, questions, feedback, hints and scope statements.
The complete findings and a row for every page are in
[the concept introduction audit](concept-audit.md).

Found 26 substantive prerequisite/explanation gaps, eight sequencing problems,
26 smaller clarification items and 21 pages with no additional gap in their new
concept, assuming earlier prerequisites are repaired. These are author-review
classifications, not measured learner difficulties. Key repairs concern opening
probability/independence and NumPy operations, early lognormal/quantile sequencing,
local notation, confidence-interval coverage, covariance/matrix construction,
advanced weighting/MCMC diagnostics and workbook domain terms. The declared
advanced logarithm/density prerequisites were respected. A late glossary entry
was not treated as sufficient teaching for an essential earlier use.

Two adjacent errors also need correction: lesson 17 repeats its plug-in-SE
explanation while omitting the exact-binomial method explanation; lesson 70
incorrectly says posterior SD of p and MCSE of a probability estimate have
different units. Both quantities are dimensionless. The lesson-12 lognormal
hint was checked with KaTeX/MathML and renders correctly.

Validation: confirmed all 79 lesson/workbook slugs appear exactly once in the
audit, included both support pages, resolved the relative documentation links,
checked table structure and confirmed all page targets in the existing generated
site. Documentation whitespace was checked. No course content, generated site
or deployment was changed. The execution suite was not rerun for this
documentation-only review; content repairs will require the usual native,
build/link and browser checks. Novice comprehension remains untested.

## 2026-11-13 — optional probability lesson 0

Added Probability essentials as a seven-minute optional preparation page before
lesson 1. Its one outcome is reading the opening attendance model in plain
language: a guest's probability, independent attendance and a whole-event trial.
It explains fractions/percentages, why 72% does not force a fixed turnout, how
shared travel can violate independence and why exactly full is not overflow.
The source reference is OpenStax Introductory Statistics, Probability Topics.

Four explicitly invented events support a labelled guest-decision diagram and
a short editable Python counting example. The example demonstrates a fraction;
it does not claim that four hand-picked rows estimate an attendance-model
probability. The illustration appears after its prerequisite explanations and
uses digits/text as well as colour. The change task preserves guest decisions
while changing the seat boundary; the fresh question tests shared attendance.
The complete explanation and worked output remain readable without JavaScript.

Applied the repository learning-design and UX skills before drafting and after
reviewing the essential reading flow with optional panels closed. Entry points
are on the overview, sidebar, first lesson and before-start notes. A direct skip
link and next/previous navigation connect the refresher to lesson 1. Reading
marks, saved drafts and progress import/export include the refresher, while the
main denominator remains 76. Existing lesson slugs and numbers are unchanged.
Lesson 1 also gives brief definitions of chance/independence and explains
True/False averaging, so the optional route is not a required hidden step.

Verification: all 80 published sources executed natively; 12 native tests passed,
including unchanged guest inputs, one overflow out of four with two seats,
three out of four with one seat, and zero with three seats. The build generated
the reference from those published inputs. The link check passed for 82 learning
pages and 7,890 relative links/fragments. All 80 examples passed real-Wasm
execution and native numerical comparison. Browser checks covered the actual
refresher run/change, feedback, skip/return navigation, saved notes, separate
reading count and restoring its records in a fresh browser context. Existing
CSV/export, error/Stop, narrow-layout, theme, no-JavaScript, 200% text and
tablet checks also passed.

Captured new 320/390/820/1440px views and inspected the phone light/dark
screenshots; the guest diagram retains its labels and numbers without whole-page
horizontal overflow.
Evidence is in test-results/lesson-zero-*.png (local test artifacts). These are
author and functional checks, not novice learner validation. The earlier concept
audit remains a baseline record; this change does not claim to resolve all its
other findings.

## 2026-11-14 — concept audit repairs and illustrated homepage

Implemented a remedy for all 60 Gap/Sequence/Support items from the baseline
concept audit. The page-by-page closure is in
[concept-remediation.md](concept-remediation.md); the original findings remain
available with a link to that implementation record. Retained optional lesson 0
and the 76-lesson progress denominator.

Applied the repository learning-design and UX skills before writing and after
reviewing the essential route with optional help closed. Definitions and local
symbol readings precede reference graphics. The opening teaches NumPy shape,
axes and boolean averaging; the summary lesson uses ten explicit invented
delays. Correlated inputs use an inspectable scalar construction. Confidence
coverage/tail conventions, fitting parameters, conditional state selection,
queue load, bias, stable weighting, Bayesian intervals and MCMC diagnostics
have worked bridges. Workbooks introduce their cost/energy, migration and
checkpoint vocabulary at first use. Removed the duplicate paragraph in 17 and
corrected the dimensionless-units claim in 70. Advanced log/density prerequisites
remain explicit, and further-study diagnostics remain optional.

The changed numerical examples execute independently. Added native checks for
tail-value effects on mean/median/P90, marginal variance/correlation preservation,
invalid input rejection and the stationary AR(1) lag/ESS reference. The new lag
calculation states its positive-correlation scope, cap and floor. Saved code
drafts remain intact; a quiet note explains how Tools can download or restore a
current example. Browser coverage exercises that recovery path and checks that
references follow their explanations.

The original possible-event illustration and dark indigo introduction form
part of a coordinated three-lab design. The user-provided Common Ground
screenshot guided the composition; SVG artwork was authored locally. Its shapes
represent concepts, with no quantitative execution result claimed. Large
reading text, one starting action, optional preparation, search and progress
remain. The graphic scales without external image or font requests.

Verification: 15 native tests passed across 80 sources. Build/link checks passed
for 82 learning pages and 7,892 relative links/fragments. The full real-Wasm suite
passed all 80 examples against native results, CSV/run/report/progress export,
saved drafts, error/Stop recovery, no-JavaScript reading, both themes, every page
at 320/390px, 200% text and 820/1024px navigation. A phone check caught unbreakable
inline method/arithmetic text in 17/33; these were rewritten and the complete
narrow-page pass repeated. Final mathematical typesetting changes received
focused rebuild/reflow checks. Shared hero controls were checked again after
the final styling changes.

All three homepages were captured at 320/390/820/1440px and checked at 200% text;
artwork text stays within its SVG view box. Inspected phone, tablet, desktop and
dark-theme captures plus representative repaired lessons. Local evidence is in
test-results/hero-*.png and prerequisite-*-phone.png. These are author,
mathematical and functional checks, not evidence of novice learning gains.

## 2026-11-14 — lesson 00 in the contents

Added the optional Probability essentials lesson as row 00 before module 1.
It uses the existing row typography, duration and saved reading marker; the
standalone title has heading level 3 under Course contents. It participates in
title/body search, with an accurate 80-row result count. Main reading progress
remains 76 lessons and the direct start, hero link and sidebar are retained.

Applied the repository learning-design and UX skills to placement and hierarchy.
Build and link checks passed for 82 pages and 7,893 relative links/fragments.
Focused browser checks passed at 320/390/820/1440px for row order, optional label,
search/empty/reset states, navigation and a saved 00 reading mark alongside
0/76 main progress. Inspected the phone contents capture. Updated the existing
browser regressions for the additional row; CI runs the complete suite before
publication. This navigation check is not a learner study.

## 2026-11-17 — experiment instructions and run recovery

Applied the learning-design and UX skills to lessons 14, 38, 50 and the
capstone. Lesson 14 defines root mean square error and identifies the two
batch sizes to compare after the edit. Lesson 38 shows the state proportions
at steps 1, 5 and 20 for either start. Lesson 50 exposes the shortage limit and
reports when the set of feasible tested options is empty. Each original run
cue is visible before the editor, and the result instructions name the fields
learners need to inspect.

The capstone shows CSV requirements beside the picker and distinguishes the
selected input, a failed attempt and the last successful result. Restoring the
published example keeps the most recently replaced draft for recovery. A failed
execution displays its own message and leaves successful output, plots and
exports available.

Chromium walkthroughs exercised the original lessons, each stated edit and the
capstone’s CSV and error path at 390px in dark mode and at 1280px in light mode.
Checked reflow at both widths in both themes with optional panels closed.
Browser regressions cover keyboard focus for Run, Stop and pending file reads,
long filenames wrapping in the result, and draft recovery after reload and
import. Following a rejected CSV,
the tests recovered the exact successful input, source and output from JSON
and Markdown. The input fixture includes a UTF-8 byte-order mark, CRLF line
endings and a trailing newline. The source includes Markdown fence characters.
The full check passed 15 native tests, all 80 real-Wasm examples, and 7,893
relative links and fragments across 82 pages.

These are functional and author checks. No learner study measured understanding.
