"""
Experiment Registry for MATRIX2.0 Reproducible Experiment Engine.
"""

from typing import Dict, List, Optional
from experiments.configuration import ExperimentConfig
from experiments.experiment import Experiment
from experiments.runner import ExperimentRunner

_REGISTRY: Dict[str, ExperimentConfig] = {}
_RUNNER = ExperimentRunner()


def register_experiment(config: ExperimentConfig) -> None:
    """Register an experiment configuration by ID."""
    _REGISTRY[config.experiment_id] = config


def get_experiment(experiment_id: str) -> Optional[ExperimentConfig]:
    """Retrieve an experiment configuration by ID."""
    return _REGISTRY.get(experiment_id)


def list_experiments() -> List[str]:
    """List all registered experiment IDs."""
    return sorted(list(_REGISTRY.keys()))


def run_experiment(experiment_id: str, overrides: Optional[Dict] = None) -> Experiment:
    """Run a registered experiment by ID with optional parameter overrides."""
    config = get_experiment(experiment_id)
    if not config:
        raise ValueError(f"Experiment ID '{experiment_id}' not found in registry.")

    if overrides:
        params = dict(config.parameters)
        params.update(overrides.get("parameters", {}))

        cfg = ExperimentConfig(
            experiment_id=config.experiment_id,
            name=config.name,
            description=config.description,
            model=config.model,
            parameters=params,
            input_state=overrides.get("input_state", config.input_state),
            seed=overrides.get("seed", config.seed),
            iterations=overrides.get("iterations", config.iterations),
            metadata=config.metadata
        )
    else:
        cfg = config

    return _RUNNER.run(cfg)


# Register Preset Experiments
register_experiment(ExperimentConfig(
    experiment_id="wave_stability",
    name="Wave Stability Experiment",
    description="Measures wave stability and deviation from baseline under controlled stochastic chaos.",
    model="wave_stability",
    parameters={"frequency": 1.0, "intensity": 1.0, "phase": 0.0, "chaos": 0.02, "variation": 0.01},
    seed=42,
    iterations=100
))

register_experiment(ExperimentConfig(
    experiment_id="phase_sensitivity",
    name="Phase Sensitivity Experiment",
    description="Measures trajectory sensitivity across small angular phase displacements.",
    model="phase_sensitivity",
    parameters={"frequency": 1.0, "intensity": 1.0, "phase": 0.0, "delta_phase": 0.1},
    seed=42,
    iterations=100
))

register_experiment(ExperimentConfig(
    experiment_id="chaos_divergence",
    name="Chaos Divergence Experiment",
    description="Measures numerical trajectory divergence over time under minute perturbations.",
    model="chaos_divergence",
    parameters={"frequency": 1.0, "intensity": 1.0, "chaos": 0.05},
    seed=42,
    iterations=100
))

register_experiment(ExperimentConfig(
    experiment_id="particle_response",
    name="Particle Response Experiment",
    description="Measures position and dispersion statistics of multi-particle field states.",
    model="particle_response",
    parameters={"frequency": 1.2, "intensity": 1.5},
    seed=42,
    iterations=100
))

register_experiment(ExperimentConfig(
    experiment_id="encoding_transformation",
    name="Encoding Transformation Experiment",
    description="Measures the transformation pipeline from symbolic text to state vectors and dynamics.",
    model="encoding_transformation",
    parameters={"text": "MATRIX2.0"},
    seed=42,
    iterations=100
))
