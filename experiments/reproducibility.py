"""
Reproducibility verification engine for MATRIX2.0 Experiment Engine.
"""

from typing import Dict, Any
from experiments.experiment import Experiment


def check_reproducibility(exp_a: Experiment, exp_b: Experiment) -> Dict[str, Any]:
    """Verify exact computational equivalency between two experiment runs."""
    reproducible = True
    mismatches = []

    # 1. Compare parameters
    if exp_a.config.parameters != exp_b.config.parameters:
        reproducible = False
        mismatches.append(f"Parameters mismatch: {exp_a.config.parameters} vs {exp_b.config.parameters}")

    # 2. Compare seed
    if exp_a.config.seed != exp_b.config.seed:
        reproducible = False
        mismatches.append(f"Seed mismatch: {exp_a.config.seed} vs {exp_b.config.seed}")

    # 3. Compare iterations
    if exp_a.config.iterations != exp_b.config.iterations:
        reproducible = False
        mismatches.append(f"Iterations mismatch: {exp_a.config.iterations} vs {exp_b.config.iterations}")

    # 4. Compare numerical measurements
    meas_a = exp_a.measurements
    meas_b = exp_b.measurements

    if set(meas_a.keys()) != set(meas_b.keys()):
        reproducible = False
        mismatches.append(f"Measurement keys mismatch: {list(meas_a.keys())} vs {list(meas_b.keys())}")
    else:
        for key in meas_a:
            vals_a = meas_a[key]
            vals_b = meas_b[key]
            if vals_a != vals_b:
                reproducible = False
                mismatches.append(f"Measurement '{key}' numerical values diverged")

    return {
        "reproducible": reproducible,
        "mismatches": mismatches,
        "experiment_id_a": exp_a.experiment_id,
        "experiment_id_b": exp_b.experiment_id
    }
