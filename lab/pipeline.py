"""
MATRIX2.0 Living Lab Pipeline

Connects encoding, decoding, state creation, wave dynamics, particle fields,
and chaos experiments into a unified pipeline.
"""

import os
import sys
from typing import Dict, Any, List, Optional

# Ensure repo root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_encode import encode_text
from matrix_decode import decode_values
from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics, step_dynamics
from matrix_particles import ParticleField, MatrixParticle
from chaos.experiment import master_stroke_experiment
from chaos.sensitivity import analyze_sensitivity


class MatrixPipeline:
    """
    Unified pipeline connecting all MATRIX2.0 computational state operations.
    """

    def __init__(self, seed: Optional[int] = 42):
        self.seed = seed

    def encode(self, text: str) -> List[int]:
        """Convert input text into ASCII unicode integers."""
        return encode_text(text)

    def decode(self, values: List[int]) -> str:
        """Convert ASCII unicode integers back into text."""
        return decode_values(values)

    def create_state(self, text: str) -> MatrixState:
        """Construct initial MatrixState vector from text input."""
        encoded = self.encode(text)
        avg_val = sum(encoded) / len(encoded) if encoded else 0.0

        return MatrixState(
            value=avg_val / 100.0,
            frequency=len(text) / 5.0 if text else 1.0,
            intensity=max(encoded) / 100.0 if encoded else 1.0,
            phase=0.0,
            chaos=0.01,
            variation=0.01,
        )

    def simulate(
        self, state: MatrixState, steps: int = 50, dt: float = 0.01
    ) -> List[Dict[str, float]]:
        """Simulate wave state dynamics over time steps and return trajectory."""
        dynamics = MatrixDynamics(MatrixState(**state.describe()))
        trajectory = []
        for step in range(steps):
            t = step * dt
            updated = dynamics.step(t=t, dt=dt)
            snap = updated.describe()
            snap["time"] = round(t, 6)
            trajectory.append(snap)
        return trajectory

    def create_particles(
        self, state: MatrixState, count: int = 5, seed: Optional[int] = None
    ) -> ParticleField:
        """Generate a particle field based on state parameters."""
        effective_seed = seed if seed is not None else self.seed
        field = ParticleField(seed=effective_seed)
        field.generate_random_particles(
            count=count,
            freq_range=(state.frequency * 0.8, state.frequency * 1.2),
            intensity_range=(state.intensity * 0.8, state.intensity * 1.2),
            chaos_range=(0.0, 0.02),
            variation_range=(0.0, 0.02),
            seed=effective_seed,
        )
        return field

    def run_chaos_test(
        self,
        state: MatrixState,
        parameter: str = "frequency",
        delta: float = 0.000001,
        iterations: int = 50,
        dt: float = 0.01,
        seed: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Execute Master Stroke chaos perturbation test."""
        effective_seed = seed if seed is not None else self.seed
        base_params = state.describe()
        return master_stroke_experiment(
            base_params=base_params,
            parameter=parameter,
            delta=delta,
            iterations=iterations,
            dt=dt,
            seed=effective_seed,
        )


class MatrixLab:
    """
    Beginner-friendly wrapper for the Living Lab pipeline.
    """

    def __init__(self, seed: Optional[int] = 42):
        self.pipeline = MatrixPipeline(seed=seed)
        self.seed = seed

    def explore(self, text: str = "MOTHER") -> Dict[str, Any]:
        """
        Runs a complete beginner exploration pipeline starting from a word.
        """
        encoded = self.pipeline.encode(text)
        initial_state = self.pipeline.create_state(text)
        trajectory = self.pipeline.simulate(initial_state, steps=20, dt=0.01)
        field = self.pipeline.create_particles(initial_state, count=5, seed=self.seed)
        field.step_field(t=0.2, dt=0.01)

        chaos_res = self.pipeline.run_chaos_test(
            initial_state, parameter="frequency", delta=0.000001, iterations=20, seed=self.seed
        )

        final_state = trajectory[-1] if trajectory else initial_state.describe()

        return {
            "what_started_with": f"Word '{text}'",
            "what_numbers_produced": encoded,
            "what_state_created": initial_state.describe(),
            "how_state_changed": {
                "initial_value": initial_state.value,
                "final_value": final_state["value"],
                "trajectory_steps": len(trajectory),
            },
            "particle_field_summary": {
                "particle_count": len(field.particles),
                "average_particle_value": round(field.get_average_value(), 6),
            },
            "chaos_experiment_measured": {
                "surprise_score": chaos_res["surprise_score"],
                "max_deviation": chaos_res["metrics"]["max_diff"],
            },
            "what_learned": (
                f"The word '{text}' was converted into ASCII codes {encoded}, mapped into a MatrixState wave vector, "
                f"evolved over {len(trajectory)} steps, and tested for chaos sensitivity with surprise score {chaos_res['surprise_score']}/100."
            ),
        }
