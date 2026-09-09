"""
MATRIX2.0 Visual Universe Pipeline Demo

Demonstrates the step-by-step visual pipeline in terminal output:
MOTHER -> Symbols -> Numbers -> MatrixState -> Wave -> Particles -> Dynamics -> Chaos -> Comparison -> Explanation
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
from visual.visual_state import change_one_parameter, get_visual_preset


def main():
    word = "MOTHER"
    seed = 42

    print("==================================================")
    print("      MATRIX2.0 VISUAL UNIVERSE PIPELINE DEMO     ")
    print("==================================================")

    # 1. Pipeline Encoding & State
    pipeline = MatrixPipeline(seed=seed)
    encoded = pipeline.encode(word)
    state = pipeline.create_state(word)

    print(f"\n[1. INPUT WORD]       '{word}'")
    print(f"[2. SYMBOLS & NUMBERS] ASCII: {encoded}")
    print(f"[3. MATRIX STATE]     {state.describe()}")

    # 4. Wave Visualization Data
    wave_vis = WaveVisualization(state).to_dict(steps=5, dt=0.01)
    print("\n[4. WAVE POINTS (First 5 points)]")
    for pt in wave_vis["points"]:
        print(f"  t={pt['t']:.2f}s | value={pt['value']:.6f}")

    # 5. Particle Field Visualization Data
    field = pipeline.create_particles(state, count=5, seed=seed)
    field.step_field(t=0.1, dt=0.01)
    part_vis = ParticleVisualization(field).to_dict()
    print(f"\n[5. PARTICLE FIELD NODES (Count: {part_vis['particle_count']})]")
    for p in part_vis["particles"]:
        print(f"  Node {p['id']}: (x={p['x']:.4f}, y={p['y']:.4f}) | value={p['value']:.4f}")

    # 6. Change-One-Parameter Experiment & Comparison
    print("\n[6. CHAOS & COMPARISON EXPERIMENT]")
    exp_res = change_one_parameter(state, parameter="frequency", delta=0.5, steps=10, dt=0.01, seed=seed)
    comp = exp_res["comparison"]
    print(f"Parameter Perturbed: 'frequency' (+0.500000)")
    print(f"Max Divergence:      {comp['maximum_divergence']:.6f}")
    print(f"Average Divergence:  {comp['average_divergence']:.6f}")

    # 7. Educational Explanation
    print("\n[7. EDUCATIONAL EXPLANATION]")
    print(f"Beginner: {exp_res['explanations']['beginner']}")
    print("==================================================")


if __name__ == "__main__":
    main()
