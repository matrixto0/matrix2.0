"""
Golden Experiment for MATRIX2.0.
Executes a deterministic benchmark comparing MATRIX2.0 state dynamics against a simple linear baseline.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from typing import Dict, Any
from matrix_core import MatrixState
from matrix_dynamics import evolve


class GoldenExperiment:
    """Golden Experiment comparing MATRIX2.0 non-linear dynamics against a baseline."""

    def __init__(self, seed: int = 42, steps: int = 100, dt: float = 0.05):
        self.experiment_id = "golden_exp_001_phase_energy_scaling"
        self.hypothesis = "MATRIX2.0 non-linear oscillation preserves bounded mean energy variance better than a linear baseline under frequency scaling."
        self.seed = seed
        self.steps = steps
        self.dt = dt

    def run_baseline(self, initial_value: float) -> list:
        """Simple linear baseline model: x(t) = initial_value + 0.1 * t."""
        trajectory = []
        for s in range(self.steps + 1):
            t = s * self.dt
            val = initial_value + 0.1 * t
            energy = val * val
            trajectory.append({"step": s, "t": round(t, 3), "value": round(val, 4), "energy": round(energy, 4)})
        return trajectory

    def run_matrix_model(self, initial_state: MatrixState) -> list:
        """MATRIX2.0 model trajectory evolution."""
        raw_states = evolve(initial_state, steps=self.steps, dt=self.dt)
        trajectory = []
        for s, st in enumerate(raw_states):
            t = s * self.dt
            energy = st.intensity ** 2 * (st.value ** 2)
            trajectory.append({"step": s, "t": round(t, 3), "value": st.value, "energy": round(energy, 4)})
        return trajectory

    def run(self, initial_state: MatrixState) -> Dict[str, Any]:
        baseline_traj = self.run_baseline(initial_state.value)
        matrix_traj = self.run_matrix_model(initial_state)

        b_energies = [p["energy"] for p in baseline_traj]
        m_energies = [p["energy"] for p in matrix_traj]

        b_mean = sum(b_energies) / len(b_energies)
        m_mean = sum(m_energies) / len(m_energies)

        b_var = sum((x - b_mean) ** 2 for x in b_energies) / len(b_energies)
        m_var = sum((x - m_mean) ** 2 for x in m_energies) / len(m_energies)

        return {
            "experiment_id": self.experiment_id,
            "hypothesis": self.hypothesis,
            "seed": self.seed,
            "steps": self.steps,
            "dt": self.dt,
            "initial_state": initial_state.to_dict(),
            "metrics": {
                "baseline_mean_energy": round(b_mean, 4),
                "baseline_energy_variance": round(b_var, 4),
                "matrix_mean_energy": round(m_mean, 4),
                "matrix_energy_variance": round(m_var, 4),
                "variance_ratio_matrix_to_baseline": round(m_var / (b_var if b_var > 0 else 1.0), 4)
            },
            "disclaimer": "Comparison describes differences between model outputs; it does not establish physical causation."
        }


def execute_golden_experiment() -> Dict[str, Any]:
    initial = MatrixState(value=1.0, frequency=2.0, intensity=1.5, phase=0.0, chaos=0.05, variation=0.05)
    exp = GoldenExperiment(seed=42, steps=100, dt=0.05)
    result = exp.run(initial)
    return result


if __name__ == "__main__":
    res = execute_golden_experiment()
    print(json.dumps(res, indent=2))
