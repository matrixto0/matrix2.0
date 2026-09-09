"""
MATRIX2.0 Living Lab Demo

Demonstrates beginner exploration, prediction checks, session serialization,
and report generation.
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lab.pipeline import MatrixLab
from lab.session import MatrixSession, save_experiment, reproduce_experiment
from lab.state_view import generate_report
from lab.lessons import run_prediction_check


def main():
    print("==================================================")
    print("         MATRIX2.0 LIVING LAB DEMO               ")
    print("==================================================")

    # 1. Beginner Exploration
    lab = MatrixLab(seed=42)
    exp_summary = lab.explore("MOTHER")

    print("\n[Beginner Exploration Summary]")
    print("Input:", exp_summary["what_started_with"])
    print("ASCII Numbers:", exp_summary["what_numbers_produced"])
    print("Surprise Score:", exp_summary["chaos_experiment_measured"]["surprise_score"])
    print("Learned:", exp_summary["what_learned"])

    # 2. Prediction Check
    pred_res = run_prediction_check("Increasing frequency will make the wave oscillate faster", "frequency", 1.2)
    print("\n[Prediction Evaluation]")
    print("Statement:", pred_res["prediction_statement"])
    print("Status:   ", pred_res["status"])

    # 3. Session & Report Generation
    session = MatrixSession(input_text="MOTHER", seed=42)
    report_text = generate_report(session.to_dict())
    print("\n" + report_text)

    # 4. Save and Reproduce
    tmp_file = "/tmp/matrix2_demo_session.json"
    save_experiment(session, tmp_file)
    reproduced_info = reproduce_experiment(tmp_file)
    print(f"\n[Reproducibility Check]\nSession Reproduced: {reproduced_info['reproduced']} (Diff: {reproduced_info['difference']})")
    print("==================================================")


if __name__ == "__main__":
    main()
