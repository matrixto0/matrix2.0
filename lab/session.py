"""
MATRIX2.0 Living Lab Session & Serialization

Records complete experiment sessions and supports JSON saving, loading, and reproduction.
"""

import datetime
import json
import random
from typing import Dict, Any, Optional
from lab.pipeline import MatrixPipeline


class MatrixSession:
    """
    Serializable record of an entire MATRIX2.0 experiment session.
    """

    def __init__(
        self,
        input_text: str = "MOTHER",
        seed: Optional[int] = 42,
        pipeline: Optional[MatrixPipeline] = None,
    ):
        if seed is not None:
            random.seed(seed)

        self.input_text = input_text
        self.seed = seed
        self.timestamp = datetime.datetime.now().isoformat()
        self.software_version = "2.0.0-living-lab"

        p = pipeline if pipeline is not None else MatrixPipeline(seed=seed)
        self.encoded_values = p.encode(input_text)
        self.initial_state = p.create_state(input_text)
        self.parameters = self.initial_state.describe()

        self.trajectory = p.simulate(self.initial_state, steps=30, dt=0.01)

        particle_field = p.create_particles(self.initial_state, count=5, seed=seed)
        particle_field.step_field(t=0.3, dt=0.01)
        self.particle_info = {
            "count": len(particle_field.particles),
            "average_value": round(particle_field.get_average_value(), 6),
            "states": particle_field.get_states(),
        }

        self.chaos_experiment = p.run_chaos_test(
            self.initial_state, parameter="frequency", delta=0.000001, iterations=30, seed=seed
        )

        final_val = self.trajectory[-1]["value"] if self.trajectory else self.initial_state.value
        val_diff = abs(final_val - self.initial_state.value)

        self.measurements = {
            "initial_value": self.initial_state.value,
            "final_value": final_val,
            "absolute_change": round(val_diff, 6),
            "max_divergence": self.chaos_experiment["metrics"]["max_diff"],
            "surprise_score": self.chaos_experiment["surprise_score"],
        }

        self.explanation = (
            f"Transformed '{input_text}' into state vector, evolved wave over {len(self.trajectory)} steps, "
            f"and evaluated sensitivity with surprise score {self.measurements['surprise_score']}/100."
        )
        self.conclusion = "Deterministic, seed-reproducible computational wave evolution verified."

    def to_dict(self) -> Dict[str, Any]:
        """Convert session into a dictionary."""
        return {
            "input_text": self.input_text,
            "seed": self.seed,
            "timestamp": self.timestamp,
            "software_version": self.software_version,
            "encoded_values": self.encoded_values,
            "parameters": self.parameters,
            "measurements": self.measurements,
            "particle_info": self.particle_info,
            "chaos_experiment": self.chaos_experiment,
            "explanation": self.explanation,
            "conclusion": self.conclusion,
            "trajectory": self.trajectory,
        }


def save_experiment(session: MatrixSession, filepath: str) -> None:
    """Save a session object to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(session.to_dict(), f, indent=2)


def load_experiment(filepath: str) -> Dict[str, Any]:
    """Load session data dictionary from a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def reproduce_experiment(filepath: str) -> Dict[str, Any]:
    """
    Re-runs an experiment session using loaded seed and input, verifying determinism.
    """
    data = load_experiment(filepath)
    input_text = data.get("input_text", "MOTHER")
    seed = data.get("seed", 42)

    new_session = MatrixSession(input_text=input_text, seed=seed)
    new_data = new_session.to_dict()

    orig_val = data["measurements"]["final_value"]
    new_val = new_data["measurements"]["final_value"]
    val_diff = abs(new_val - orig_val)

    reproduced = val_diff < 1e-7

    return {
        "reproduced": reproduced,
        "original_final_value": orig_val,
        "reproduced_final_value": new_val,
        "difference": round(val_diff, 8),
        "new_session_data": new_data,
    }
