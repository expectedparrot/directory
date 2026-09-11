# Expected Parrot packages

[Browse the visual package directory](https://expectedparrot.github.io/directory/) · [View the HTML source](https://github.com/expectedparrot/directory/blob/main/docs/index.html)

This catalog brings together foundational research tools and application packages from [Expected Parrot](https://www.expectedparrot.com/). Expected Parrot builds open tools for designing, running, and analyzing AI-powered research. Start with Epiq for evidence-backed data, EDSL for surveys and model execution, and AISS for research design and analysis, then explore applications for specific research methods and workflows.

## Foundation packages

Shared tools for storing research evidence and running surveys and experiments.

### Epiq

Epiq is a local-first epistemic database for evidence-backed research. It stores entities, typed questions, source excerpts, and claims in SQLite, preserving the provenance and history behind each answer. Its Python API, CLI, and spreadsheet interface let researchers and application packages build auditable datasets and export them as tables, HTML, or Excel.

[GitHub](https://github.com/expectedparrot/epiq) · [Documentation](https://github.com/expectedparrot/epiq#readme)

### EDSL

EDSL (Expected Parrot Domain-Specific Language) is a Python library for designing and running AI-powered surveys and experiments. Its composable questions, surveys, scenarios, agents, and language models support structured research across many respondents and models, with results that can be analyzed, visualized, and shared. It provides the survey and model-execution foundation used by many of the application packages below.

[GitHub](https://github.com/expectedparrot/edsl) · [Documentation](https://docs.expectedparrot.com) · [Starter tutorial](https://docs.expectedparrot.com/en/latest/starter_tutorial)

### AISS

<p align="center">
  <a href="https://github.com/expectedparrot/aiss"><img src="docs/assets/aiss-artwork.png" width="640" alt="AISS artwork: parrots perched on a causal diagram linking buyer budget, seller minimum, and seller love to whether a deal occurs, inside expectation brackets"></a>
</p>

AISS is a Python package for designing, running, and analyzing AI social science studies with EDSL. It provides serializable research designs, independently versioned analysis plans, causal and factorial analysis, and deterministic scientific reports. Its simulation DSL defines participant roles, private information, treatments, interaction rules, and measurements, with resumable execution and durable attempt tracking.

[GitHub](https://github.com/expectedparrot/aiss) · [Documentation](https://github.com/expectedparrot/aiss#readme) · [Simulation DSL manual (PDF)](https://github.com/expectedparrot/aiss/blob/main/docs/manual/aiss-manual.pdf)

## Application packages

Focused, agent-friendly CLIs and supporting libraries for research workflows, with links to their repositories and available tutorials or documentation.

### Aivis

<p align="center">
  <a href="https://github.com/expectedparrot/aivis"><img src="https://raw.githubusercontent.com/expectedparrot/aivis/main/assets/aivis-overview.png" width="640" alt="Aivis AI brand-visibility measurement overview"></a>
</p>

Aivis is an agent-facing CLI for measuring how brands and competitors appear in AI-generated answers. It administers a reusable prompt library across models, extracts tracked-brand observations with an EDSL judge, and stores deterministic time-series records for share of voice, mention rate, recommendations, sentiment, and citation influence.

[GitHub](https://github.com/expectedparrot/aivis) · [Tutorial](https://github.com/expectedparrot/aivis#install-and-quickstart)

### Ariel

<p align="center">
  <a href="https://github.com/expectedparrot/ariel"><img src="https://raw.githubusercontent.com/expectedparrot/ariel/main/assets/ariel.png" width="640" alt="Ariel artwork: two parrots dividing a seed cake"></a>
</p>

Ariel is an agent-first fair-division package for rent, indivisible goods, bivalued chores, project credit, and shared fares. It combines local mathematical solvers and explicit verification with EDSL participation by humans or simulated subjects, preserves original evidence, and keeps post-allocation reactions separate from submitted inputs. Its state-aware `next` command guides agents through problem setup and execution.

[GitHub](https://github.com/expectedparrot/ariel) · [Tutorial](https://github.com/expectedparrot/ariel#install-and-try-the-offline-example)

### Bewley

<p align="center">
  <a href="https://github.com/expectedparrot/bewley"><img src="https://raw.githubusercontent.com/expectedparrot/bewley/main/docs/assets/bewley-package.png" width="640" alt="Bewley package artwork"></a>
</p>

Bewley is a local-first qualitative-coding CLI for interview transcripts and other text corpora. It maintains an auditable history of codebooks, span annotations, and memos, supports AI-assisted open coding through EDSL, and exports evidence tables, visual explorers, theory diagrams, and narrative summaries.

[GitHub](https://github.com/expectedparrot/bewley) · [Tutorial](https://expectedparrot.github.io/bewley/)

### Conversation

Conversation is an EDSL-based package for simulating structured, multi-agent conversations. It manages turn-taking, parallel conversation runs, retry behavior, and accumulated results so researchers can study interactions among simulated participants rather than isolated survey responses.

[GitHub](https://github.com/expectedparrot/conversation) · [Documentation](https://github.com/expectedparrot/conversation#readme)

### Dewey

<p align="center">
  <a href="https://github.com/expectedparrot/dewey"><img src="https://raw.githubusercontent.com/expectedparrot/dewey/main/assets/dewey-literature-parrot.png" width="640" alt="Dewey package artwork"></a>
</p>

Dewey is an agent-facing CLI for auditable literature reviews. It manages papers, rendered text, short summaries, discovery and citation provenance, staged screening decisions, source relationships, searchable project state, interactive review explorers, and portable full-project archives.

[GitHub](https://github.com/expectedparrot/dewey) · [Tutorial](https://expectedparrot.github.io/dewey/)

### Flyvbjerg

<p align="center">
  <a href="https://github.com/expectedparrot/flyvbjerg"><img src="https://raw.githubusercontent.com/expectedparrot/flyvbjerg/main/docs/flyvbjerg-art.png" width="640" alt="Flyvbjerg package artwork"></a>
</p>

Flyvbjerg is an agent-facing CLI for reference-class forecasting and outside-view analysis. It preserves comparable cases, sources, events, claims, metrics, missingness, dependence clusters, and frozen analyses in an auditable evidence ledger, turning accepted observations into defensible reference-class distributions.

[GitHub](https://github.com/expectedparrot/flyvbjerg) · [Tutorial](https://expectedparrot.github.io/flyvbjerg/)

### Green

<p align="center">
  <a href="https://github.com/expectedparrot/green"><img src="https://raw.githubusercontent.com/expectedparrot/green/main/docs/assets/green-conjoint-artwork.png" width="640" alt="Green package artwork"></a>
</p>

Green is an agent-first toolkit for conjoint analysis and discrete-choice experiments. It helps design choice tasks, generate EDSL fieldwork, estimate preference models, and produce part-worths, willingness-to-pay estimates, market-share simulations, and sensitivity analyses.

[GitHub](https://github.com/expectedparrot/green) · [Tutorial](https://github.com/expectedparrot/green/blob/main/docs/index.html)

### Golden

<p align="center">
  <a href="https://github.com/expectedparrot/golden"><img src="https://raw.githubusercontent.com/expectedparrot/golden/main/docs/assets/golden-artwork.png" width="640" alt="Golden artwork: an Expected Parrot evaluating product ratings"></a>
</p>

Golden is an agent-first CLI for evidence-backed consumer decisions. It combines structured preference interviews, explicit constraints, sourced product research, sensitivity analysis, and an interactive utility-versus-price explorer to help consumers make transparent, auditable choices.

[GitHub](https://github.com/expectedparrot/golden) · [Tutorial](https://github.com/expectedparrot/golden/blob/main/docs/index.html)

### Helmer

<p align="center">
  <a href="https://github.com/expectedparrot/helmer"><img src="https://raw.githubusercontent.com/expectedparrot/helmer/main/docs/assets/helmer-artwork.png" width="640" alt="Helmer artwork: a laurel-crowned parrot at the oracle of Delphi inside expectation brackets"></a>
</p>

Helmer is an agent-first CLI for Delphi expert elicitation. It collects numerical estimates and ratings across repeated rounds, gives each expert anonymous group feedback and their own previous answers, and reports consensus, stability, attrition, and remaining disagreement. It preserves study history, exchanges native EDSL instruments and Results, and supports small workflow pilots with separate participant roles.

[GitHub](https://github.com/expectedparrot/helmer) · [Tutorial](https://github.com/expectedparrot/helmer/blob/main/docs/tutorial.md)

### Ishikawa

<p align="center">
  <a href="https://github.com/expectedparrot/ishikawa"><img src="https://raw.githubusercontent.com/expectedparrot/ishikawa/main/docs/assets/ishikawa-artwork.png" width="640" alt="Ishikawa artwork: a green parrot drawing a fishbone diagram inside expectation brackets"></a>
</p>

Ishikawa is an agent-friendly Python CLI for cause-and-effect analysis and fishbone diagrams. It organizes possible causes into categories and nested why chains, records supporting and contradicting evidence, and tracks investigations and corrective actions. JSON project files, SVG diagrams, and searchable HTML reports preserve hypotheses and assessments without treating them as proven root causes.

[GitHub](https://github.com/expectedparrot/ishikawa) · [Documentation](https://github.com/expectedparrot/ishikawa#readme) · [Quickstart](https://github.com/expectedparrot/ishikawa#install-and-try)

### Kahn

<p align="center">
  <a href="https://github.com/expectedparrot/kahn"><img src="https://raw.githubusercontent.com/expectedparrot/kahn/main/docs/assets/kahn-package.png" width="640" alt="Kahn package artwork"></a>
</p>

Kahn is a two-axis strategic scenario-planning CLI. It turns environmental forces and critical uncertainties into a scenario matrix, develops narratives for the resulting futures, and evaluates strategic options across them.

[GitHub](https://github.com/expectedparrot/kahn) · [Tutorial](https://expectedparrot.github.io/kahn/)

### Katz

<p align="center">
  <a href="https://github.com/expectedparrot/katz"><img src="https://raw.githubusercontent.com/expectedparrot/katz/main/docs/katz-economist-parrot.png" width="640" alt="Katz package artwork"></a>
</p>

Katz is a version-aware ledger for reviewing academic manuscripts. It anchors human and model-generated findings to manuscript sections and Git versions, tracks investigation and resolution history, and produces review reports from the resulting issue record.

[GitHub](https://github.com/expectedparrot/katz) · [Tutorial](https://expectedparrot.github.io/katz/)

### Kean

<p align="center">
  <a href="https://github.com/expectedparrot/kean"><img src="docs/assets/kean-artwork.png" width="640" alt="Kean artwork: a green parrot detective in a fedora and trench coat"></a>
</p>

Kean is an agent-first CLI for evidence-backed event graphs on an ordinary epiq database. It records occurrences, participants, and supported relations, then exposes bitemporal timelines, auditable paths, response delays, unexplained events, and contested claims. Deterministic JSON, DOT, and HTML exports preserve claim and evidence lineage.

[GitHub (private)](https://github.com/expectedparrot/kean) · [Documentation (access required)](https://github.com/expectedparrot/kean#readme)

Local checkout: `~/tools/ep/kean`.

### Labeling

<p align="center">
  <a href="https://github.com/expectedparrot/labeling"><img src="https://raw.githubusercontent.com/expectedparrot/labeling/master/docs/assets/labeling-parrot.png" width="640" alt="Labeling package artwork"></a>
</p>

Labeling is an agent-first CLI for reproducible LLM-as-rater workflows. It manages datasets, labeling specifications, gold standards, rule baselines, multi-rater aggregation, quality metrics, and exports while preserving a complete audit trail and an explicit EDSL execution boundary.

[GitHub](https://github.com/expectedparrot/labeling) · [Tutorial](https://expectedparrot.github.io/labeling/)

### Langley

<p align="center">
  <a href="https://github.com/expectedparrot/langley"><img src="https://raw.githubusercontent.com/expectedparrot/langley/main/docs/assets/langley-package.png" width="640" alt="Langley package artwork"></a>
</p>

Langley is an agent-first implementation of Richards Heuer's Analysis of Competing Hypotheses method. It compares evidence across hypotheses, records a durable audit trail, runs sensitivity analysis, and generates portable EDSL jobs for AI-assisted analysis.

[GitHub](https://github.com/expectedparrot/langley) · [Tutorial](https://expectedparrot.github.io/langley/)

### McCall

<p align="center">
  <a href="https://github.com/expectedparrot/mccall"><img src="https://raw.githubusercontent.com/expectedparrot/mccall/main/assets/mccall-job-post-artwork.png" width="640" alt="McCall job-post testing artwork"></a>
</p>

McCall is an agent-facing CLI for pretesting and refining job posts with EDSL candidate simulations. It preserves role requirements, post variants, persona provenance, portable Jobs and Results, and controlled comparisons so hiring teams can see how different candidate types interpret a post before publishing it.

[GitHub](https://github.com/expectedparrot/mccall) · [Tutorial](https://expectedparrot.github.io/mccall/)

### MCDA

<p align="center">
  <a href="https://github.com/expectedparrot/mcda"><img src="https://raw.githubusercontent.com/expectedparrot/mcda/main/docs/mcda-package.png" width="640" alt="MCDA package artwork"></a>
</p>

MCDA is an agent-first, JSON-enveloped CLI for multi-criteria decision analysis. It records participants, alternatives, criteria, weights, thresholds, and performance assessments, then compares options using transparent weighted-sum or ELECTRE III analysis while preserving auditable project state.

[GitHub](https://github.com/expectedparrot/mcda) · [Tutorial](https://github.com/expectedparrot/mcda#full-example-choosing-an-office-lease)

### Messick

<p align="center">
  <a href="https://github.com/expectedparrot/messick"><img src="https://raw.githubusercontent.com/expectedparrot/messick/main/docs/assets/messick-artwork.png" width="640" alt="Messick package artwork"></a>
</p>

Messick is an agent-first package for pretesting, revising, and validating EDSL survey instruments. It tracks intended constructs and uses, preserves immutable revisions and evidence provenance, and keeps simulation findings distinct from evidence about human respondents.

[GitHub](https://github.com/expectedparrot/messick) · [Tutorial](https://expectedparrot.github.io/messick/)

### Niles

<p align="center">
  <a href="https://github.com/expectedparrot/niles"><img src="https://raw.githubusercontent.com/expectedparrot/niles/master/docs/assets/niles-artwork.png" width="640" alt="Niles package artwork"></a>
</p>

Niles is a local-first CRM CLI for relationship work. It manages contacts, interaction notes, follow-up tasks, teammates, materials, surveys, human intake, and reviewed model recommendations through a machine-readable interface.

[GitHub](https://github.com/expectedparrot/niles) · [Tutorial](https://expectedparrot.github.io/niles/)

### Oneheart

Oneheart is a CLI for designing and recording Concordia-backed multi-agent social simulations. It manages study definitions, agents, treatments, measurements, generated pilot code, run records, and outcome exports for research on agent interactions.

[GitHub](https://github.com/expectedparrot/oneheart) · [Tutorial](https://expectedparrot.github.io/oneheart/)

### Premortem

<p align="center">
  <a href="https://github.com/expectedparrot/premortem"><img src="https://raw.githubusercontent.com/expectedparrot/premortem/main/docs/assets/premortem-mark.png" width="640" alt="Premortem package artwork"></a>
</p>

Premortem facilitates a structured, Gary Klein-style pre-mortem for a decision, project, launch, or strategy. It elicits failure modes from stakeholder personas, builds and scores a causal graph, develops mitigations and a research agenda, and renders a final report.

[GitHub](https://github.com/expectedparrot/premortem) · [Tutorial](https://expectedparrot.github.io/premortem/)

### Pruefung

<p align="center">
  <a href="https://github.com/expectedparrot/pruefung"><img src="https://raw.githubusercontent.com/expectedparrot/pruefung/main/assets/pruefung-artwork.png" width="640" alt="Pruefung package artwork"></a>
</p>

Pruefung is an agent-first CLI for building, checking, deploying, and grading quizzes and exams with EDSL-native questions. It stores inspectable project state, returns structured JSON for agent workflows, and keeps model inference behind an explicit make, run, and ingest boundary.

[GitHub](https://github.com/expectedparrot/pruefung) · [Documentation](https://github.com/expectedparrot/pruefung/blob/main/pruefung-spec.md)

### Roth

<p align="center">
  <a href="https://github.com/expectedparrot/roth"><img src="https://raw.githubusercontent.com/expectedparrot/roth/main/docs/assets/roth-package.png" width="640" alt="Roth package artwork"></a>
</p>

Roth collects preferences on both sides of a market and computes one-to-one stable matches using deferred acceptance. It supports Humanize ranking surveys, organizer-controlled LLM delegation, optional A-versus-B preference benchmarks, frozen inputs, and reports of realized ranks and unmatched participants.

[GitHub](https://github.com/expectedparrot/roth) · [Tutorial](https://expectedparrot.github.io/roth/)

### Rudin

<p align="center">
  <a href="https://github.com/expectedparrot/rudin"><img src="docs/assets/rudin-artwork.png" width="640" alt="Rudin artwork: a geometric parrot inside expectation brackets"></a>
</p>

Rudin is a local-first CLI for designing transparent scoring models. It turns domain rubrics into manual or learned integer scorecards, scores structured answers, and exports EDSL surveys and portable artifacts. Its worked LaTeX manual develops rubric design, fitting, threshold selection, and held-out evaluation through executable synthetic examples.

[GitHub](https://github.com/expectedparrot/rudin) · [Tutorial](https://expectedparrot.github.io/rudin/) · [Manual (PDF)](https://github.com/expectedparrot/rudin/blob/main/docs/rudin-manual.pdf)

### Tommy

<p align="center">
  <a href="https://github.com/expectedparrot/tommy"><img src="https://raw.githubusercontent.com/expectedparrot/tommy/main/docs/assets/tommy-artwork.png" width="640" alt="Tommy package artwork"></a>
</p>

Tommy is an agent-facing CLI for preparing realistic sales roleplays with Expected Parrot. It preserves practice attempts and transcript-grounded reviews, produces self-contained coaching reports, and guides coding agents through each state transition with deterministic recommended actions.

[GitHub](https://github.com/expectedparrot/tommy) · [Tutorial](https://expectedparrot.github.io/tommy/)

### Treffen

<p align="center">
  <a href="https://github.com/expectedparrot/treffen"><img src="https://raw.githubusercontent.com/expectedparrot/treffen/main/docs/assets/treffen-package.png" width="640" alt="Treffen package artwork"></a>
</p>

Treffen is an agent-first CLI for preparing better meetings. It turns a meeting outcome and participant list into typed EDSL surveys and adaptive interviews, person-specific links and QR codes, evidence-backed synthesis, focused agendas and pre-reads, and durable decision records—while supporting both expected and confirmed attendance.

[GitHub](https://github.com/expectedparrot/treffen) · [Tutorial](https://expectedparrot.github.io/treffen/)

### Umriss

<p align="center">
  <a href="https://github.com/expectedparrot/umriss"><img src="https://raw.githubusercontent.com/expectedparrot/umriss/main/docs/assets/umriss-art.png" width="640" alt="Umriss package artwork"></a>
</p>

Umriss is an agent-facing CLI for constructing auditable digital twins from published survey marginals. It builds candidate personas, calibrates their weights to known population responses, and evaluates the resulting synthetic population against held-out survey items.

[GitHub](https://github.com/expectedparrot/umriss) · [Tutorial](https://expectedparrot.github.io/umriss/)

### UXTest

<p align="center">
  <a href="https://github.com/expectedparrot/uxtest"><img src="https://raw.githubusercontent.com/expectedparrot/uxtest/main/docs/assets/uxtest-package.png" width="640" alt="UXTest package artwork"></a>
</p>

UXTest is an agent-first CLI for running synthetic-user UX studies against live web pages. It uses Playwright and EDSL to capture browser journeys, screenshots, traces, and structured findings, preserving an inspectable evidence trail for issue discovery, comparison, and regression testing.

[GitHub](https://github.com/expectedparrot/uxtest) · [Tutorial](https://expectedparrot.github.io/uxtest/)

### Vorhersage

Vorhersage is a forecasting workbench for agents. It turns binary-event questions into durable research workflows, preserving source provenance, probability judgments, reviews, revisions, and outcomes. It integrates with Epiq, supports optional scenario mixtures and related-question checks, and provides configurable monitoring and matched forecast evaluation.

[GitHub](https://github.com/expectedparrot/vorhersage) · [Documentation](https://expectedparrot.github.io/vorhersage/)

### Voting

<p align="center">
  <a href="https://github.com/expectedparrot/voting"><img src="https://raw.githubusercontent.com/expectedparrot/voting/main/docs/assets/voting-mark.png" width="640" alt="Voting package artwork"></a>
</p>

Voting is a JSON-first toolkit for preference research and group-decision analysis. It collects ballots from people or AI personas and compares single- and multi-winner counting rules across plurality, ranked, approval, score, grade, allocation, and Condorcet method families.

[GitHub](https://github.com/expectedparrot/voting) · [Tutorial](https://expectedparrot.github.io/voting/)

### Zitate

Zitate is an agent-facing CLI for auditing whether academic sources support manuscript claims. It inventories citations, preserves the source material and exact evidence used for each judgment, and produces an auditable report without silently modifying the manuscript or treating metadata and search snippets as substantive support.

[GitHub](https://github.com/expectedparrot/zitate) · [Documentation](https://github.com/expectedparrot/zitate#readme)

### Zugunruhe

<p align="center">
  <a href="https://github.com/expectedparrot/zugunruhe"><img src="https://raw.githubusercontent.com/expectedparrot/zugunruhe/main/assets/readme-artwork.png" width="640" alt="Zugunruhe package artwork"></a>
</p>

Zugunruhe is an agent-focused migration CLI for moving Qualtrics and SurveyMonkey instruments to EDSL and Expected Parrot. It provides a staged, machine-readable workflow for capture, conversion, validation, review, and export.

[GitHub](https://github.com/expectedparrot/zugunruhe) · [Tutorial](https://expectedparrot.github.io/zugunruhe/)

### Zwicky

<p align="center">
  <a href="https://github.com/expectedparrot/zwicky"><img src="https://raw.githubusercontent.com/expectedparrot/zwicky/main/docs/assets/zwicky-morphological-parrots.png" width="640" alt="Zwicky package artwork"></a>
</p>

Zwicky is a general morphological-analysis CLI for exploring product and feature design spaces. It defines dimensions and values, generates configurations, applies constraints, and supports AI- and human-assisted evaluation, Pareto analysis, and concept selection.

[GitHub](https://github.com/expectedparrot/zwicky) · [Tutorial](https://expectedparrot.github.io/zwicky/)

### Zwill

<p align="center">
  <a href="https://github.com/expectedparrot/zwill"><img src="https://raw.githubusercontent.com/expectedparrot/zwill/main/docs/assets/zwill-package.png" width="640" alt="Zwill package artwork"></a>
</p>

Zwill is an open validation harness for survey digital twins. It builds twin prompts and EDSL jobs, records inference artifacts, and evaluates individual- and aggregate-level predictive performance against observed survey responses and conventional baselines.

[GitHub](https://github.com/expectedparrot/zwill) · [Tutorial](https://expectedparrot.github.io/zwill/)
