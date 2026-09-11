"""Run the HTML tutorial's negotiation study, offline by default.

From the repository root:
    uv run --locked python docs/examples/negotiation_tutorial.py
Add --prepare-only to inspect artifacts, or --backend edsl for provider calls.
"""

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from aiss import (
    AnalysisPlanArtifact, BlueprintCompiler, CausalExperimentRunner,
    CausalStudyProposal, ContrastCell, DeterministicScientificReport,
    EDSLCausalAdapter, ExperimentalDesignArtifact, FactorialAnalysisExecutor,
    LinearContrastSpec, ProposalCompiler, ScientificEvidencePacket,
)
from edsl.conversations import SQLiteConversationStore


def compile_study(replications=2):
    document = json.loads(
        (ROOT / "docs/manual/examples/negotiation.json").read_text()
    )
    document["design"]["replications"] = replications
    document["metadata"]["purpose"] = "HTML tutorial; scripted runs are fixtures and model runs are pilots"
    proposal = CausalStudyProposal(document)
    validation = proposal.validate()
    if not validation.is_valid:
        raise ValueError(validation.to_dict())
    expanded = ProposalCompiler().compile(proposal)
    if expanded.status != "ok":
        raise ValueError(expanded.to_dict())
    blueprint = expanded.blueprint
    study = BlueprintCompiler().compile(blueprint)
    design = ExperimentalDesignArtifact.from_blueprint(blueprint)
    contrast = LinearContrastSpec(
        "higher_budget", "agreement",
        [ContrastCell({"buyer_budget": budget, "seller_cost": cost}, weight)
         for budget, weight in [(10, -0.5), (20, 0.5)]
         for cost in [8, 14]],
        primary=True, alternative="greater",
    )
    plan = AnalysisPlanArtifact(
        design.specification_hash,
        models=blueprint.analysis_plan.models,
        contrasts=[contrast], covariance="HC3", missing="error",
    )
    plan.validate_against(design)
    return proposal, blueprint, study, design, plan


class ScriptedNegotiation:
    """A deliberately simple fixture policy, not a behavioral model."""

    def __init__(self):
        self.calls = 0

    def speak(self, request):
        self.calls += 1
        if request.role == "buyer":
            return f"I offer ${request.private_values['buyer_budget']:g}."
        offer = float(request.transcript[-1]["text"].split("$")[1].rstrip("."))
        if offer >= request.private_values["seller_cost"]:
            return f"I accept ${offer:g}."
        return "I decline. We have reached an impasse."

    def judge(self, conversation, transcript, question):
        self.calls += 1
        return bool(transcript and transcript[-1]["role"] == "seller")

    def measure(self, request):
        self.calls += 1
        last = request.transcript[-1]["text"]
        if request.manifest.variable == "agreement":
            return int(last.startswith("I accept"))
        if request.manifest.variable == "price":
            return float(last.split("$")[1].rstrip("."))
        raise ValueError(f"Unexpected measurement: {request.manifest.variable}")


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("scripted", "edsl"), default="scripted")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--replications", type=int, default=2)
    parser.add_argument("--model", default="gemini-2.5-flash-lite")
    parser.add_argument("--service", default="google")
    args = parser.parse_args()
    if args.replications < 2:
        parser.error("Use at least two replications per cell for this analysis.")
    output = args.output or ROOT / "examples/automated_social_science/runs" / f"tutorial-{args.backend}"
    proposal, blueprint, study, design, plan = compile_study(args.replications)
    configuration = {
        "backend": args.backend,
        "design_hash": design.specification_hash,
        "analysis_hash": plan.specification_hash,
        "source_hash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.backend == "edsl":
        configuration.update(model=args.model, service=args.service, temperature=1.0)
    output.mkdir(parents=True, exist_ok=True)
    manifest = output / "configuration.json"
    if manifest.exists() and json.loads(manifest.read_text()) != configuration:
        raise ValueError("Run configuration changed. Use a fresh --output directory.")
    write_json(manifest, configuration)
    for name, artifact in [
        ("proposal", proposal), ("blueprint", blueprint), ("design", design),
        ("analysis_plan", plan), ("experiment", study.experiment),
        ("conversation", blueprint.interaction),
    ]:
        write_json(output / f"{name}.json", artifact.to_dict())
    if args.prepare_only:
        print(json.dumps({"status": "prepared", "sessions": len(study.experiment.replications),
                          "backend": args.backend, "output": str(output)}))
        return

    if args.backend == "scripted":
        adapter = ScriptedNegotiation()
    else:
        from edsl import Model
        adapter = EDSLCausalAdapter(Model(args.model, service_name=args.service, temperature=1.0))
    store = SQLiteConversationStore(output / "conversations.sqlite")
    runner = CausalExperimentRunner(
        study.experiment, blueprint.interaction, store,
        speakers={"buyer": adapter.speak, "seller": adapter.speak},
        semantic_judge=adapter.judge,
        measurers={"agreement": adapter.measure, "price": adapter.measure},
        execution_key=json.dumps(configuration, sort_keys=True),
    )
    observations = []
    for replication in study.experiment.replications:
        observations.append(runner.run(replication).to_dict())
        write_json(output / "observations.json", observations)
    result = FactorialAnalysisExecutor().execute(design, plan, observations)
    write_json(output / "analysis_result.json", result.to_dict())
    evidence = ScientificEvidencePacket.build(design, plan, result, execution={
        "backend": args.backend, "fixture_only": args.backend == "scripted",
        "completed_sessions": len(observations),
    })
    write_json(output / "evidence.json", evidence.to_dict())
    title = "Negotiation tutorial — scripted fixture" if args.backend == "scripted" else "Negotiation tutorial — model pilot"
    report = DeterministicScientificReport().render_markdown(evidence, title=title)
    (output / "report.md").write_text(report)
    print(json.dumps({
        "completed": len(observations), "fixture_only": args.backend == "scripted",
        "agreement_rate": sum(row["values"]["agreement"] for row in observations) / len(observations),
        "higher_budget_estimate": round(result.to_dict()["contrasts"][0]["estimate"], 6),
        **({"callbacks_this_run": adapter.calls} if args.backend == "scripted" else {}),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
