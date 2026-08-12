# Expected Parrot CLI packages

[Browse the visual package directory](https://expectedparrot.github.io/directory/) · [View the HTML source](https://github.com/expectedparrot/directory/blob/main/docs/index.html)

This is a catalog of standalone Python command-line packages from [Expected Parrot](https://www.expectedparrot.com/). Expected Parrot builds open tools for designing, running, and analyzing AI-powered research. Its packages help researchers and coding agents turn methods such as qualitative coding, conjoint analysis, scenario planning, survey validation, and decision analysis into explicit, reproducible workflows.

Many of these tools use [EDSL](https://github.com/expectedparrot/edsl), Expected Parrot's Python library for constructing AI-powered surveys and experiments. EDSL provides composable objects for questions, surveys, scenarios, agents, and language models, making it possible to specify a study in code, run it with large numbers of simulated respondents, and analyze the resulting structured data.

The packages below sit one level above that foundation. Each is a focused, agent-friendly CLI with its own repository, package artwork, and maintained tutorial. They keep project state and artifacts on disk so work can be inspected, repeated, reviewed, and version-controlled.

## Aivis

<p align="center">
  <a href="https://github.com/expectedparrot/aivis"><img src="https://raw.githubusercontent.com/expectedparrot/aivis/main/assets/aivis-overview.png" width="640" alt="Aivis AI brand-visibility measurement overview"></a>
</p>

Aivis is an agent-facing CLI for measuring how brands and competitors appear in AI-generated answers. It administers a reusable prompt library across models, extracts tracked-brand observations with an EDSL judge, and stores deterministic time-series records for share of voice, mention rate, recommendations, sentiment, and citation influence.

[GitHub](https://github.com/expectedparrot/aivis) · [Tutorial](https://github.com/expectedparrot/aivis#install-and-quickstart)

## Bewley

<p align="center">
  <a href="https://github.com/expectedparrot/bewley"><img src="https://raw.githubusercontent.com/expectedparrot/bewley/main/docs/assets/bewley-package.png" width="640" alt="Bewley package artwork"></a>
</p>

Bewley is a local-first qualitative-coding CLI for interview transcripts and other text corpora. It maintains an auditable history of codebooks, span annotations, and memos, supports AI-assisted open coding through EDSL, and exports evidence tables, visual explorers, theory diagrams, and narrative summaries.

[GitHub](https://github.com/expectedparrot/bewley) · [Tutorial](https://expectedparrot.github.io/bewley/)

## Dewey

<p align="center">
  <a href="https://github.com/expectedparrot/dewey"><img src="https://raw.githubusercontent.com/expectedparrot/dewey/main/assets/dewey-literature-parrot.png" width="640" alt="Dewey package artwork"></a>
</p>

Dewey is an agent-facing CLI for auditable literature reviews. It manages papers, rendered text, short summaries, discovery and citation provenance, staged screening decisions, source relationships, searchable project state, interactive review explorers, and portable full-project archives.

[GitHub](https://github.com/expectedparrot/dewey) · [Tutorial](https://expectedparrot.github.io/dewey/)

## Green

<p align="center">
  <a href="https://github.com/expectedparrot/green"><img src="https://raw.githubusercontent.com/expectedparrot/green/main/docs/assets/green-conjoint-artwork.png" width="640" alt="Green package artwork"></a>
</p>

Green is an agent-first toolkit for conjoint analysis and discrete-choice experiments. It helps design choice tasks, generate EDSL fieldwork, estimate preference models, and produce part-worths, willingness-to-pay estimates, market-share simulations, and sensitivity analyses.

[GitHub](https://github.com/expectedparrot/green) · [Tutorial](https://github.com/expectedparrot/green/blob/main/docs/index.html)

## Kahn

<p align="center">
  <a href="https://github.com/expectedparrot/kahn"><img src="https://raw.githubusercontent.com/expectedparrot/kahn/main/docs/assets/kahn-package.png" width="640" alt="Kahn package artwork"></a>
</p>

Kahn is a two-axis strategic scenario-planning CLI. It turns environmental forces and critical uncertainties into a scenario matrix, develops narratives for the resulting futures, and evaluates strategic options across them.

[GitHub](https://github.com/expectedparrot/kahn) · [Tutorial](https://expectedparrot.github.io/kahn/)

## Katz

<p align="center">
  <a href="https://github.com/expectedparrot/katz"><img src="https://raw.githubusercontent.com/expectedparrot/katz/main/docs/katz-economist-parrot.png" width="640" alt="Katz package artwork"></a>
</p>

Katz is a version-aware ledger for reviewing academic manuscripts. It anchors human and model-generated findings to manuscript sections and Git versions, tracks investigation and resolution history, and produces review reports from the resulting issue record.

[GitHub](https://github.com/expectedparrot/katz) · [Tutorial](https://expectedparrot.github.io/katz/)

## Labeling

<p align="center">
  <a href="https://github.com/expectedparrot/labeling"><img src="https://raw.githubusercontent.com/expectedparrot/labeling/master/docs/assets/labeling-parrot.png" width="640" alt="Labeling package artwork"></a>
</p>

Labeling is an agent-first CLI for reproducible LLM-as-rater workflows. It manages datasets, labeling specifications, gold standards, rule baselines, multi-rater aggregation, quality metrics, and exports while preserving a complete audit trail and an explicit EDSL execution boundary.

[GitHub](https://github.com/expectedparrot/labeling) · [Tutorial](https://expectedparrot.github.io/labeling/)

## Langley

<p align="center">
  <a href="https://github.com/expectedparrot/langley"><img src="https://raw.githubusercontent.com/expectedparrot/langley/main/docs/assets/langley-package.png" width="640" alt="Langley package artwork"></a>
</p>

Langley is an agent-first implementation of Richards Heuer's Analysis of Competing Hypotheses method. It compares evidence across hypotheses, records a durable audit trail, runs sensitivity analysis, and generates portable EDSL jobs for AI-assisted analysis.

[GitHub](https://github.com/expectedparrot/langley) · [Tutorial](https://expectedparrot.github.io/langley/)

## MCDA

<p align="center">
  <a href="https://github.com/expectedparrot/mcda"><img src="https://raw.githubusercontent.com/expectedparrot/mcda/main/docs/figures/office_lease_candidate_ranking.png" width="640" alt="MCDA candidate-ranking analysis"></a>
</p>

MCDA is an agent-first, JSON-enveloped CLI for multi-criteria decision analysis. It records participants, alternatives, criteria, weights, thresholds, and performance assessments, then compares options using transparent weighted-sum or ELECTRE III analysis while preserving auditable project state.

[GitHub](https://github.com/expectedparrot/mcda) · [Tutorial](https://github.com/expectedparrot/mcda#full-example-choosing-an-office-lease)

## Messick

<p align="center">
  <a href="https://github.com/expectedparrot/messick"><img src="https://raw.githubusercontent.com/expectedparrot/messick/main/docs/assets/messick-artwork.png" width="640" alt="Messick package artwork"></a>
</p>

Messick is an agent-first package for pretesting, revising, and validating EDSL survey instruments. It tracks intended constructs and uses, preserves immutable revisions and evidence provenance, and keeps simulation findings distinct from evidence about human respondents.

[GitHub](https://github.com/expectedparrot/messick) · [Tutorial](https://expectedparrot.github.io/messick/)

## Premortem

<p align="center">
  <a href="https://github.com/expectedparrot/premortem"><img src="https://raw.githubusercontent.com/expectedparrot/premortem/main/docs/assets/premortem-mark.png" width="640" alt="Premortem package artwork"></a>
</p>

Premortem facilitates a structured, Gary Klein-style pre-mortem for a decision, project, launch, or strategy. It elicits failure modes from stakeholder personas, builds and scores a causal graph, develops mitigations and a research agenda, and renders a final report.

[GitHub](https://github.com/expectedparrot/premortem) · [Tutorial](https://expectedparrot.github.io/premortem/)

## Treffen

<p align="center">
  <a href="https://github.com/expectedparrot/treffen"><img src="https://raw.githubusercontent.com/expectedparrot/treffen/main/docs/assets/treffen-package.png" width="640" alt="Treffen package artwork"></a>
</p>

Treffen is an agent-first CLI for preparing better meetings. It turns a meeting outcome and participant list into typed EDSL surveys and adaptive interviews, person-specific links and QR codes, evidence-backed synthesis, focused agendas and pre-reads, and durable decision records—while supporting both expected and confirmed attendance.

[GitHub](https://github.com/expectedparrot/treffen) · [Tutorial](https://expectedparrot.github.io/treffen/)

## UXTest

<p align="center">
  <a href="https://github.com/expectedparrot/uxtest"><img src="https://raw.githubusercontent.com/expectedparrot/uxtest/main/docs/assets/uxtest-package.png" width="640" alt="UXTest package artwork"></a>
</p>

UXTest is an agent-first CLI for running synthetic-user UX studies against live web pages. It uses Playwright and EDSL to capture browser journeys, screenshots, traces, and structured findings, preserving an inspectable evidence trail for issue discovery, comparison, and regression testing.

[GitHub](https://github.com/expectedparrot/uxtest) · [Tutorial](https://expectedparrot.github.io/uxtest/)

## Umriss

<p align="center">
  <a href="https://github.com/expectedparrot/umriss"><img src="https://raw.githubusercontent.com/expectedparrot/umriss/main/docs/assets/umriss-art.png" width="640" alt="Umriss package artwork"></a>
</p>

Umriss is an agent-facing CLI for constructing auditable digital twins from published survey marginals. It builds candidate personas, calibrates their weights to known population responses, and evaluates the resulting synthetic population against held-out survey items.

[GitHub](https://github.com/expectedparrot/umriss) · [Tutorial](https://expectedparrot.github.io/umriss/)

## Voting

<p align="center">
  <a href="https://github.com/expectedparrot/voting"><img src="https://raw.githubusercontent.com/expectedparrot/voting/main/docs/assets/voting-mark.png" width="640" alt="Voting package artwork"></a>
</p>

Voting is a JSON-first toolkit for preference research and group-decision analysis. It collects ballots from people or AI personas and compares single- and multi-winner counting rules across plurality, ranked, approval, score, grade, allocation, and Condorcet method families.

[GitHub](https://github.com/expectedparrot/voting) · [Tutorial](https://expectedparrot.github.io/voting/)

## Zugunruhe

<p align="center">
  <a href="https://github.com/expectedparrot/zugunruhe"><img src="https://raw.githubusercontent.com/expectedparrot/zugunruhe/main/assets/readme-artwork.png" width="640" alt="Zugunruhe package artwork"></a>
</p>

Zugunruhe is an agent-focused migration CLI for moving Qualtrics and SurveyMonkey instruments to EDSL and Expected Parrot. It provides a staged, machine-readable workflow for capture, conversion, validation, review, and export.

[GitHub](https://github.com/expectedparrot/zugunruhe) · [Tutorial](https://expectedparrot.github.io/zugunruhe/)

## Zwicky

<p align="center">
  <a href="https://github.com/expectedparrot/zwicky"><img src="https://raw.githubusercontent.com/expectedparrot/zwicky/main/docs/assets/zwicky-morphological-parrots.png" width="640" alt="Zwicky package artwork"></a>
</p>

Zwicky is a general morphological-analysis CLI for exploring product and feature design spaces. It defines dimensions and values, generates configurations, applies constraints, and supports AI- and human-assisted evaluation, Pareto analysis, and concept selection.

[GitHub](https://github.com/expectedparrot/zwicky) · [Tutorial](https://expectedparrot.github.io/zwicky/)

## Zwill

<p align="center">
  <a href="https://github.com/expectedparrot/zwill"><img src="https://raw.githubusercontent.com/expectedparrot/zwill/main/docs/assets/zwill-package.png" width="640" alt="Zwill package artwork"></a>
</p>

Zwill is an open validation harness for survey digital twins. It builds twin prompts and EDSL jobs, records inference artifacts, and evaluates individual- and aggregate-level predictive performance against observed survey responses and conventional baselines.

[GitHub](https://github.com/expectedparrot/zwill) · [Tutorial](https://expectedparrot.github.io/zwill/)
