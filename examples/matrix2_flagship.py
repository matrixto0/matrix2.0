"""
MATRIX2.0 Flagship Demonstration Script: Complexity-to-Simplicity Engine

Executes the complete pipeline:
"MOTHER" -> Unicode -> MatrixState -> Wave -> Particles -> Perturbation -> Chaos -> Measurement -> Explanation -> Saved Experiment
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_lab import MatrixLab, save_experiment_data, reproduce_experiment_data


def main():
    print("==================================================")
    print("     MATRIX2.0 COMPLEXITY-TO-SIMPLICITY ENGINE   ")
    print("==================================================")

    word = "MOTHER"
    seed = 42

    lab = MatrixLab(seed=seed)

    print(f"\n[1. EXPLORE JOURNEY FOR '{word}']")
    exp_res = lab.explore(word)

    print("\n--- BEGINNER MODE ---")
    print(exp_res["beginner_mode"])

    print("\n--- DEEP MODE (MATHEMATICS) ---")
    print(exp_res["deep_mode"])

    print("\n--- AHA INSIGHT MOMENT ---")
    print(exp_res["aha_moment"])

    print("\n--- EXPERIMENT CARD ---")
    print(exp_res["experiment_card"])

    print("\n[2. ASK QUESTION]")
    question = "What happens if frequency increases?"
    ask_res = lab.ask(question, base_text=word)
    print(f"Question:  {question}")
    print(f"Tested:    {ask_res['parameter_tested']} (delta: +{ask_res['delta_applied']:.4f})")
    print(f"Surprise:  {ask_res['surprise_score']}/100")
    print(f"Insight:   {ask_res['aha_moment']}")

    print("\n[3. PREDICTION MODE]")
    pred_statement = "I predict increasing frequency increases wave cycle speed"
    pred_res = lab.predict(pred_statement, base_text=word)
    print(f"Prediction: {pred_statement}")
    print(f"Result:     {pred_res['result']}")
    print(f"Reasoning:  {pred_res['explanation']}")

    print("\n[4. SAVE & REPRODUCE EXPERIMENT]")
    save_path = "/tmp/matrix2_flagship_session.json"
    save_experiment_data(exp_res, save_path)
    print(f"Experiment saved to: {save_path}")

    repro_res = reproduce_experiment_data(save_path)
    print(f"Reproducibility Verified: {repro_res['reproduced']} (Diff score: {repro_res['difference']})")
    print("==================================================")


if __name__ == "__main__":
    main()
