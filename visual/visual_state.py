"""
MATRIX2.0 Visual Presets, Change-One-Parameter Helper, and Multi-Mode Exporters

Provides visual educational presets, central change_one_parameter() helper,
and JSON/CSV export routines preserving seed reproducibility.
"""

import csv
import json
import os
import sys
from typing import Dict, Any, List, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_core import MatrixState
from visual.wave_data import WaveVisualization
from visual.particle_data import ParticleVisualization
from visual.trajectory_data import TrajectoryVisualization
from visual.comparison_data import ComparisonVisualization
from lab.pipeline import MatrixPipeline


VISUAL_PRESETS: Dict[str, Dict[str, Any]] = {
    "CALM_WAVE": {
        "description": "A smooth, deterministic pure sine wave with zero noise or variation.",
        "params": {"frequency": 1.0, "intensity": 1.0, "phase": 0.0, "chaos": 0.0, "variation": 0.0},
    },
    "FAST_WAVE": {
        "description": "High frequency oscillation demonstrating rapid wave repetition.",
        "params": {"frequency": 3.0, "intensity": 1.0, "phase": 0.0, "chaos": 0.0, "variation": 0.0},
    },
    "HIGH_INTENSITY": {
        "description": "Scaled peak amplitude demonstrating wave energy scaling.",
        "params": {"frequency": 1.0, "intensity": 2.5, "phase": 0.0, "chaos": 0.0, "variation": 0.0},
    },
    "PHASE_SHIFT": {
        "description": "Phase offset of pi/2 radians shifting wave cycle alignment at t=0.",
        "params": {"frequency": 1.0, "intensity": 1.0, "phase": 1.570796, "chaos": 0.0, "variation": 0.0},
    },
    "CHAOS_EXPLORER": {
        "description": "Moderate stochastic noise introducing observable trajectory perturbation.",
        "params": {"frequency": 1.0, "intensity": 1.0, "phase": 0.0, "chaos": 0.05, "variation": 0.02},
    },
    "PARTICLE_FIELD": {
        "description": "Multi-particle field container showcasing individual particle dynamics.",
        "params": {"frequency": 1.2, "intensity": 1.5, "phase": 0.0, "chaos": 0.01, "variation": 0.01},
    },
    "DOUBLE_WAVE": {
        "description": "Two-wave configuration prepared for superposition testing.",
        "params": {"frequency": 2.0, "intensity": 1.2, "phase": 0.785398, "chaos": 0.0, "variation": 0.0},
    },
}


def get_visual_preset(name: str) -> Dict[str, Any]:
    """Retrieve visual preset dictionary by key (case-insensitive)."""
    key = name.upper().strip()
    if key not in VISUAL_PRESETS:
        raise ValueError(
            f"Unknown visual preset '{name}'. Available: {list(VISUAL_PRESETS.keys())}"
        )
    return dict(VISUAL_PRESETS[key])


def change_one_parameter(
    base_state: MatrixState,
    parameter: str,
    delta: float,
    steps: int = 50,
    dt: float = 0.01,
    seed: Optional[int] = 42,
) -> Dict[str, Any]:
    """
    Central educational interaction:
    1. Creates baseline state
    2. Modifies exactly one parameter
    3. Runs both simulations
    4. Compares trajectories
    5. Produces plot-ready visualization dataset
    6. Explains the observed difference across Beginner, Deep, and Research modes.
    """
    param_lower = parameter.lower().strip()
    base_params = base_state.describe()

    if param_lower not in base_params:
        raise ValueError(f"Invalid parameter '{parameter}'. Must be one of {list(base_params.keys())}")

    perturbed_params = dict(base_params)
    perturbed_params[param_lower] = perturbed_params.get(param_lower, 0.0) + delta
    perturbed_state = MatrixState(**perturbed_params)

    # Generate wave, trajectory, particle, and comparison visualizations
    wave_vis = WaveVisualization(base_state).to_dict(steps=steps, dt=dt)
    traj_vis = TrajectoryVisualization(base_state).to_dict(steps=steps, dt=dt)

    pipeline = MatrixPipeline(seed=seed)
    particle_field = pipeline.create_particles(base_state, count=5, seed=seed)
    particle_field.step_field(t=steps * dt, dt=dt)
    part_vis = ParticleVisualization(particle_field).to_dict()

    comp_vis = ComparisonVisualization(
        base_state, perturbed_state, steps=steps, dt=dt, seed=seed
    ).compare()

    max_div = comp_vis["maximum_divergence"]
    avg_div = comp_vis["average_divergence"]

    # Educational explanations across modes
    beginner_explanation = (
        f"Changing parameter '{param_lower}' by +{delta:.6f} caused the wave trajectory to "
        f"deviate by a maximum of {max_div:.6f} units over {steps} steps."
    )

    deep_explanation = (
        f"Baseline: M = {base_state.describe()}\n"
        f"Perturbed: M = {perturbed_state.describe()}\n"
        f"Wave Delta: max|W_base(t) - W_pert(t)| = {max_div:.8f}, avg = {avg_div:.8f}"
    )

    research_explanation = {
        "parameter_perturbed": param_lower,
        "delta": delta,
        "steps": steps,
        "dt": dt,
        "seed": seed,
        "baseline_state": base_params,
        "perturbed_state": perturbed_params,
        "metrics": {
            "maximum_divergence": max_div,
            "average_divergence": avg_div,
            "final_difference": comp_vis["final_difference"],
        },
    }

    return {
        "parameter_perturbed": param_lower,
        "delta": delta,
        "baseline_state": base_params,
        "perturbed_state": perturbed_params,
        "comparison": comp_vis,
        "wave_visualization": wave_vis,
        "trajectory_visualization": traj_vis,
        "particle_visualization": part_vis,
        "explanations": {
            "beginner": beginner_explanation,
            "deep": deep_explanation,
            "research": research_explanation,
        },
    }


def export_visualization_json(data: Dict[str, Any], filepath: str) -> None:
    """Export visualization dataset dictionary to JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_visualization_csv(data: Dict[str, Any], filepath: str) -> None:
    """Export trajectory points to CSV file."""
    points = data.get("wave_visualization", {}).get("points", [])
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "value"])
        for p in points:
            writer.writerow([p["t"], p["value"]])
