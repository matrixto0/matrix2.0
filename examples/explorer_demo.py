"""
MATRIX2.0 Explorer Demo

Demonstrates concepts lookup, interactive experiments, what-if calculations,
challenge validation, and achievement tracking.
"""

import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from explorer.concepts import get_concept
from explorer.experiments import exp_1_frequency_change, exp_6_word_to_numbers
from explorer.explanations import explain_state_params, WhatIfEngine, calculate_complexity_score, AchievementTracker
from explorer.challenges import get_challenge


def main():
    print("==================================================")
    print("          MATRIX2.0 EXPLORER DEMO                 ")
    print("==================================================")

    # 1. Concept Lookup
    concept = get_concept("frequency")
    if concept:
        print("\n[Concept: Frequency]")
        print(f"Beginner: {concept.beginner_description}")
        print(f"Deep:     {concept.deep_description}")
        print(f"Formula:  {concept.formula}")

    # 2. Experiment Execution
    exp_res = exp_1_frequency_change(freq_a=0.5, freq_b=2.0)
    print("\n[Experiment 1: Frequency Change]")
    print(f"Observation: {exp_res['observation']}")

    # 3. Parameter Explanation
    explanations = explain_state_params(frequency=1.0, intensity=2.0)
    print("\n[Explanation]")
    print(f"Simple: {explanations['simple']}")
    print(f"Math:   {explanations['mathematical']}")

    # 4. What-If Engine
    initial_state = MatrixState(frequency=1.0, intensity=1.5)
    what_if_res = WhatIfEngine.what_if_frequency_doubles(initial_state)
    print("\n[What-If Engine]")
    print(f"Question:    {what_if_res['question']}")
    print(f"Explanation: {what_if_res['explanation']}")

    # 5. Challenge Validation
    ch = get_challenge("faster_wave")
    if ch:
        state_test = MatrixState(frequency=2.5)
        passed = ch.validate(state_test)
        print(f"\n[Challenge: {ch.title}]")
        print(f"Objective: {ch.objective}")
        print(f"Validation Passed: {passed}")

    # 6. Complexity Score & Achievements
    score_info = calculate_complexity_score(initial_state)
    tracker = AchievementTracker()
    tracker.unlock("FIRST_WAVE")
    tracker.unlock("FIRST_EXPERIMENT")

    print(f"\n[Complexity & Achievements]")
    print(f"Complexity Score: {score_info['score']} ({score_info['level']})")
    print(f"Achievements Progress: {tracker.get_progress()}")
    print("==================================================")


if __name__ == "__main__":
    main()
