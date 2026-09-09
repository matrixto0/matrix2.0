"""
MATRIX2.0 Flagship Visual Universe Demonstration

Demonstrates:
MOTHER -> encode -> state -> wave -> particle field -> master-stroke perturbation -> comparison -> visualization dataset -> explanation
"""

import os
import sys

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from lab.pipeline import MatrixPipeline
from visual.wave_data import WaveVisualization
from visual.particle_data import ParticleVisualization
from visual.trajectory_data import TrajectoryVisualization
from visual.visual_state import change_one_parameter, export_visualization_json, export_visualization_csv


def main():
    word = "MOTHER"
    seed = 42

    print("==================================================")
    print("    MATRIX2.0 FLAGSHIP VISUAL UNIVERSE DEMO      ")
    print("==================================================")

    print(f"\n[1. INPUT WORD] '{word}'")

    pipeline = MatrixPipeline(seed=seed)
    encoded = pipeline.encode(word)
    print(f"[2. UNICODE ENCODING] ASCII: {encoded}")

    state = pipeline.create_state(word)
    print(f"[3. MATRIX STATE] {state.describe()}")

    wave_vis = WaveVisualization(state).to_dict(steps=10, dt=0.01)
    print(f"[4. WAVE POINTS GENERATED] Steps: {len(wave_vis['points'])}")

    field = pipeline.create_particles(state, count=5, seed=seed)
    field.step_field(t=0.1, dt=0.01)
    part_vis = ParticleVisualization(field).to_dict()
    print(f"[5. PARTICLE NODES GENERATED] Particle Nodes: {part_vis['particle_count']}")

    print("\n[6. MASTER-STROKE PERTURBATION EXPERIMENT]")
    exp_res = change_one_parameter(state, parameter="frequency", delta=0.000001, steps=20, dt=0.01, seed=seed)
    comp = exp_res["comparison"]
    print(f"Max Divergence: {comp['maximum_divergence']:.8f}")
    print(f"Avg Divergence: {comp['average_divergence']:.8f}")

    print("\n[7. EXPLANATION]")
    print(exp_res["explanations"]["beginner"])

    json_path = "/tmp/matrix2_visual_dataset.json"
    csv_path = "/tmp/matrix2_visual_dataset.csv"

    export_visualization_json(exp_res, json_path)
    export_visualization_csv(exp_res, csv_path)

    print(f"\n[8. VISUAL DATASETS EXPORTED]")
    print(f"JSON: {json_path}")
    print(f"CSV:  {csv_path}")
    print("==================================================")


if __name__ == "__main__":
    main()
