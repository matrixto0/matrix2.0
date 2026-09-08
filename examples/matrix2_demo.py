"""
MATRIX2.0 Flagship Demonstration Script

Demonstrates the entire computational journey:
MOTHER -> Unicode -> MatrixState -> Wave -> Particle Field -> Perturbation -> Chaos Comparison -> Measurement -> Explanation -> Saved Experiment
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lab.pipeline import MatrixLab
from lab.session import MatrixSession, save_experiment, reproduce_experiment
from lab.state_view import beginner_view, deep_view, generate_report
from lab.metrics import what_changed


def main():
    print("**************************************************")
    print("      MATRIX2.0 FLAGSHIP DEMONSTRATION           ")
    print("**************************************************")

    word = "MOTHER"
    seed = 42

    print(f"\n1. WORD INPUT\nInput Word: '{word}'")

    lab = MatrixLab(seed=seed)
    encoded = lab.pipeline.encode(word)
    print(f"\n2. UNICODE ENCODING\nASCII Codes: {encoded}")

    state = lab.pipeline.create_state(word)
    print(f"\n3. MATRIX STATE VECTOR\nBeginner: {beginner_view(state.describe())}")
    print(f"Deep:     {deep_view(state.describe())}")

    traj = lab.pipeline.simulate(state, steps=10, dt=0.01)
    print(f"\n4. WAVE SIMULATION (10 steps)\nInitial Value: {traj[0]['value']:.6f} -> Final Value: {traj[-1]['value']:.6f}")

    field = lab.pipeline.create_particles(state, count=5, seed=seed)
    field.step_field(t=0.1, dt=0.01)
    print(f"\n5. PARTICLE FIELD\nParticle Count: {len(field.particles)} | Average Value: {field.get_average_value():.6f}")

    chaos_res = lab.pipeline.run_chaos_test(state, parameter="frequency", delta=0.000001, seed=seed)
    print(f"\n6. PERTURBATION & CHAOS COMPARISON\nPerturbed 'frequency' by +0.000001")
    print(f"Max Trajectory Deviation: {chaos_res['metrics']['max_diff']:.6f}")
    print(f"Surprise Score:           {chaos_res['surprise_score']}/100")

    diff_analysis = what_changed(state.describe(), traj[-1])
    print(f"\n7. MEASUREMENT & WHAT CHANGED\nSummary: {diff_analysis['summary']}")

    print(f"\n8. EXPLANATION\n{chaos_res['explanation']['why_sensitive']}")

    session = MatrixSession(input_text=word, seed=seed)
    save_path = "/tmp/mother_experiment.json"
    save_experiment(session, save_path)
    print(f"\n9. SAVED EXPERIMENT\nSaved session to '{save_path}'")

    repro = reproduce_experiment(save_path)
    print(f"\n10. REPRODUCIBILITY VERIFICATION\nDeterministic Reproduction Verified: {repro['reproduced']}")
    print("**************************************************")


if __name__ == "__main__":
    main()
