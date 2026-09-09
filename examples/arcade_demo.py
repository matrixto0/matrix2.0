"""
MATRIX2.0 Simulation Arcade Terminal Demonstration Script

Launches terminal selection menu and executes simulation game experiments.
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arcade.games import REGISTRY


def main():
    print("========================================")
    print("       MATRIX2.0 SIMULATION ARCADE      ")
    print("========================================")

    games = REGISTRY.list_games()
    print("\n[Available Simulation Games]")
    for idx, g in enumerate(games, 1):
        print(f"  {idx}. {g['title']} ({g['id']}) - {g['difficulty']}")
        print(f"     Objective: {g['learning_objective']}")

    print("\n----------------------------------------")
    print("Running Flagship Demonstration: Wave Runner (Game 1)")
    print("----------------------------------------")

    wave_game = REGISTRY.get_game("wave_runner")
    if wave_game:
        res = wave_game.run(
            params={"frequency": 2.0, "intensity": 1.5, "phase": 0.0},
            prediction="I predict doubling frequency will double wave repetition speed",
            seed=42,
        )

        print(f"\nGame Title: {res['title']}")
        print(f"Prediction: {res['prediction_evaluation']['prediction']}")
        print(f"Status:     {res['prediction_evaluation']['status']}")
        print(f"Score:      {res['score']['total_score']} pts")
        print(f"Explanation:{res['explanations']['simple']}")
        print(f"Math View:  {res['explanations']['mathematical']}")

    print("\n----------------------------------------")
    print("Running Flagship Demonstration: Chaos Race (Game 3)")
    print("----------------------------------------")

    chaos_game = REGISTRY.get_game("chaos_race")
    if chaos_game:
        res_chaos = chaos_game.run(
            params={"frequency": 1.0, "parameter": "frequency", "delta": 0.000001},
            prediction="I predict tiny perturbation will diverge over time",
            seed=42,
        )

        print(f"\nGame Title: {res_chaos['title']}")
        print(f"Max Divergence: {res_chaos['master_stroke_data']['metrics']['max_diff']}")
        print(f"Status:     {res_chaos['prediction_evaluation']['status']}")
        print(f"Score:      {res_chaos['score']['total_score']} pts")

    print("\n========================================")


if __name__ == "__main__":
    main()
