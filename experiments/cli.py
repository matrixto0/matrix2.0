"""
Command-line interface for MATRIX2.0 Reproducible Experiment Engine.
"""

import argparse
import json
import sys
from typing import List
from experiments.comparison import compare_results
from experiments.experiment import Experiment
from experiments.registry import list_experiments, run_experiment, get_experiment
from experiments.results import generate_experiment_report
from experiments.runner import generate_parameter_sweeps, ExperimentRunner


def main(args: List[str] = None):
    parser = argparse.ArgumentParser(prog="python -m experiments.cli", description="MATRIX2.0 Experiment Engine CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Command: list
    subparsers.add_parser("list", help="List registered preset experiments")

    # Command: run
    run_parser = subparsers.add_parser("run", help="Run a registered experiment")
    run_parser.add_argument("experiment_id", help="Experiment ID to execute")
    run_parser.add_argument("--seed", type=int, default=42, help="Random seed")
    run_parser.add_argument("--iterations", type=int, default=100, help="Iteration count")
    run_parser.add_argument("--output", type=str, help="Save result to JSON file path")

    # Command: compare
    comp_parser = subparsers.add_parser("compare", help="Compare two experiment result JSON files")
    comp_parser.add_argument("file_a", help="Path to first experiment result JSON")
    comp_parser.add_argument("file_b", help="Path to second experiment result JSON")

    # Command: export
    exp_parser = subparsers.add_parser("export", help="Run and export experiment result to JSON")
    exp_parser.add_argument("experiment_id", help="Experiment ID")
    exp_parser.add_argument("filepath", help="Output JSON file path")

    # Command: sweep
    sweep_parser = subparsers.add_parser("sweep", help="Run a parameter sweep for a model experiment")
    sweep_parser.add_argument("experiment_id", help="Base experiment ID")

    parsed = parser.parse_args(args)

    if parsed.command == "list":
        print("Registered MATRIX2.0 Experiments:")
        for exp_id in list_experiments():
            cfg = get_experiment(exp_id)
            print(f"  - {exp_id:25s} : {cfg.name}")

    elif parsed.command == "run":
        exp = run_experiment(parsed.experiment_id, overrides={"seed": parsed.seed, "iterations": parsed.iterations})
        report = generate_experiment_report(exp)
        print(report)
        if parsed.output:
            with open(parsed.output, "w", encoding="utf-8") as f:
                f.write(exp.to_json())
            print(f"\nResult saved to: {parsed.output}")

    elif parsed.command == "compare":
        with open(parsed.file_a, "r", encoding="utf-8") as f:
            exp_a = Experiment.from_json(f.read())
        with open(parsed.file_b, "r", encoding="utf-8") as f:
            exp_b = Experiment.from_json(f.read())

        report = generate_experiment_report(exp_a, comparison_target=exp_b)
        print(report)

    elif parsed.command == "export":
        exp = run_experiment(parsed.experiment_id)
        with open(parsed.filepath, "w", encoding="utf-8") as f:
            f.write(exp.to_json())
        print(f"Experiment {parsed.experiment_id} exported successfully to {parsed.filepath}")

    elif parsed.command == "sweep":
        base_cfg = get_experiment(parsed.experiment_id)
        if not base_cfg:
            print(f"Experiment '{parsed.experiment_id}' not found.")
            sys.exit(1)

        sweep_params = {"chaos": [0.00, 0.01, 0.05], "variation": [0.00, 0.01]}
        configs = generate_parameter_sweeps(base_cfg, sweep_params)
        runner = ExperimentRunner()

        print(f"Executing parameter sweep ({len(configs)} runs)...")
        for cfg in configs:
            exp = runner.run(cfg)
            mean_score = exp.summary.get("stability_score", {}).get("mean", 0.0)
            print(f"  Run '{cfg.experiment_id}': mean_score = {mean_score}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
