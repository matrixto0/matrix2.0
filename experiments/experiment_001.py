"""
MATRIX2.0 EXPERIMENT 001
"MOTHER" Symbolic Transformation Experiment

Pipeline:
1. Input text: "MOTHER"
2. encode_text() -> numeric ASCII values
3. Construct MatrixState from encoded signal
4. Step wave dynamics over time steps
5. Initialize deterministic ParticleField
6. Record and print structured report output
"""

import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from matrix_encode import encode_text
from matrix_dynamics import step_dynamics
from matrix_particles import ParticleField


def run_experiment_001(input_text: str = "MOTHER", seed: int = 42):
    print("==================================================")
    print("          MATRIX2.0 EXPERIMENT 001               ")
    print("==================================================")
    print(f"\n[Input]\nText: {input_text}\nSeed: {seed}")

    # 1. Encoding
    encoded_values = encode_text(input_text)
    avg_char_val = sum(encoded_values) / len(encoded_values) if encoded_values else 0.0

    # Map text signal to initial MatrixState
    initial_state = MatrixState(
        value=avg_char_val / 100.0,
        frequency=len(input_text) / 5.0,
        intensity=max(encoded_values) / 100.0 if encoded_values else 1.0,
        phase=0.0,
        chaos=0.01,
        variation=0.01,
    )

    print(f"\n[Encoded ASCII Values]\n{encoded_values}")
    print(f"\n[Initial MatrixState]\n{initial_state.describe()}")

    # 2. Dynamic Wave Step
    t = 0.5
    dt = 0.01
    dynamic_state = step_dynamics(initial_state, t=t, dt=dt)
    print(f"\n[Dynamic State (t={t}, dt={dt})]\n{dynamic_state.describe()}")

    # 3. Particle Field Evolution
    field = ParticleField(seed=seed)
    field.generate_random_particles(
        count=5,
        freq_range=(initial_state.frequency * 0.8, initial_state.frequency * 1.2),
        intensity_range=(initial_state.intensity * 0.8, initial_state.intensity * 1.2),
        chaos_range=(0.0, 0.02),
        variation_range=(0.0, 0.02),
        seed=seed,
    )
    field.step_field(t=t, dt=dt)
    avg_val = field.get_average_value()

    print(f"\n[Particle Field (Count: {len(field.particles)})]")
    print(f"Average Particle Value: {avg_val:.6f}")
    for idx, p in enumerate(field.particles, 1):
        print(f"  Particle {idx}: value={p.value:.6f}, freq={p.frequency:.4f}, inten={p.intensity:.4f}")

    print("\n[Result Summary]")
    print(f"Input '{input_text}' transformed to mean field wave state value: {avg_val:.6f}")
    print("==================================================")

    return {
        "input": input_text,
        "encoded_values": encoded_values,
        "initial_state": initial_state.describe(),
        "dynamic_state": dynamic_state.describe(),
        "particle_count": len(field.particles),
        "average_value": avg_val,
    }


if __name__ == "__main__":
    run_experiment_001()
