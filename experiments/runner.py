"""
Deterministic experiment execution engine for MATRIX2.0.
"""

import itertools
from typing import Any, Dict, List
from experiments.configuration import ExperimentConfig
from experiments.experiment import Experiment
from experiments.statistics import calculate_summary_stats
from matrix_dynamics import WaveState, WaveStepEvaluator
from matrix_encode import text_to_numbers
from matrix_particles import MatrixParticle, ParticleField


class ExperimentRunner:
    """Executes deterministic model experiments and collects metrics."""

    def run(self, config: ExperimentConfig) -> Experiment:
        """Run experiment deterministically based on config parameters and seed."""
        model = config.model

        if model == "wave_stability":
            measurements = self._run_wave_stability(config)
        elif model == "phase_sensitivity":
            measurements = self._run_phase_sensitivity(config)
        elif model == "chaos_divergence":
            measurements = self._run_chaos_divergence(config)
        elif model == "particle_response":
            measurements = self._run_particle_response(config)
        elif model == "encoding_transformation":
            measurements = self._run_encoding_transformation(config)
        else:
            measurements = self._run_wave_stability(config)

        # Calculate metrics summary stats
        summary = {}
        for key, vals in measurements.items():
            if isinstance(vals, list) and vals and isinstance(vals[0], (int, float)):
                summary[key] = calculate_summary_stats([float(v) for v in vals])

        exp = Experiment(
            config=config,
            timestamp="2025-01-01T00:00:00Z",
            measurements=measurements,
            summary=summary,
            reproducible=True
        )
        return exp

    def _run_wave_stability(self, config: ExperimentConfig) -> Dict[str, Any]:
        p = config.parameters
        freq = float(p.get("frequency", 1.0))
        inten = float(p.get("intensity", 1.0))
        phase = float(p.get("phase", 0.0))
        chaos = float(p.get("chaos", 0.0))
        var = float(p.get("variation", 0.0))

        state = WaveState(x=0.0, frequency=freq, intensity=inten, phase=phase, chaos=chaos, variation=var)
        evaluator = WaveStepEvaluator(dt=0.01)

        wave_values = []
        baseline_values = []
        deviations = []

        baseline_state = WaveState(x=0.0, frequency=freq, intensity=inten, phase=phase, chaos=0.0, variation=0.0)

        for i in range(config.iterations):
            w_val = evaluator.evaluate(state, step_index=i)
            b_val = evaluator.evaluate(baseline_state, step_index=i)
            dev = abs(w_val - b_val)

            wave_values.append(round(w_val, 6))
            baseline_values.append(round(b_val, 6))
            deviations.append(round(dev, 6))

        stability_score = round(max(0.0, 100.0 - (sum(deviations) / len(deviations) * 50.0)), 2)

        return {
            "wave_values": wave_values,
            "baseline_values": baseline_values,
            "deviations": deviations,
            "stability_score": [stability_score]
        }

    def _run_phase_sensitivity(self, config: ExperimentConfig) -> Dict[str, Any]:
        p = config.parameters
        freq = float(p.get("frequency", 1.0))
        inten = float(p.get("intensity", 1.0))
        phase_base = float(p.get("phase", 0.0))
        delta_phase = float(p.get("delta_phase", 0.1))

        evaluator = WaveStepEvaluator(dt=0.01)
        state_a = WaveState(x=0.0, frequency=freq, intensity=inten, phase=phase_base, chaos=0.0, variation=0.0)
        state_b = WaveState(x=0.0, frequency=freq, intensity=inten, phase=phase_base + delta_phase, chaos=0.0, variation=0.0)

        diffs = []
        trajectory_a = []
        trajectory_b = []

        for i in range(config.iterations):
            va = evaluator.evaluate(state_a, step_index=i)
            vb = evaluator.evaluate(state_b, step_index=i)
            diff = abs(va - vb)

            trajectory_a.append(round(va, 6))
            trajectory_b.append(round(vb, 6))
            diffs.append(round(diff, 6))

        return {
            "trajectory_a": trajectory_a,
            "trajectory_b": trajectory_b,
            "phase_differences": diffs
        }

    def _run_chaos_divergence(self, config: ExperimentConfig) -> Dict[str, Any]:
        p = config.parameters
        freq = float(p.get("frequency", 1.0))
        inten = float(p.get("intensity", 1.0))
        chaos = float(p.get("chaos", 0.05))

        evaluator = WaveStepEvaluator(dt=0.01)
        state_a = WaveState(x=0.0, frequency=freq, intensity=inten, phase=0.0, chaos=0.0, variation=0.0)
        state_b = WaveState(x=0.0, frequency=freq, intensity=inten, phase=0.0, chaos=chaos, variation=0.0)

        divergences = []
        for i in range(config.iterations):
            va = evaluator.evaluate(state_a, step_index=i)
            vb = evaluator.evaluate(state_b, step_index=i)
            divergences.append(round(abs(va - vb), 6))

        return {
            "divergences": divergences
        }

    def _run_particle_response(self, config: ExperimentConfig) -> Dict[str, Any]:
        p = config.parameters
        freq = float(p.get("frequency", 1.0))
        inten = float(p.get("intensity", 1.0))

        particles = [MatrixParticle(x=i * 0.1, frequency=freq, intensity=inten) for i in range(10)]
        field = ParticleField(particles)

        means = []
        dispersions = []

        for i in range(config.iterations):
            field.step(dt=0.01)
            means.append(round(field.mean_state(), 6))
            dispersions.append(round(field.dispersion(), 6))

        return {
            "field_means": means,
            "field_dispersions": dispersions
        }

    def _run_encoding_transformation(self, config: ExperimentConfig) -> Dict[str, Any]:
        text_input = str(config.input_state or config.parameters.get("text", "MATRIX2.0"))
        nums = text_to_numbers(text_input)

        avg_num = sum(nums) / len(nums) if nums else 0.0
        freq = round(avg_num / 100.0, 4)

        state = WaveState(x=0.0, frequency=freq, intensity=1.0, phase=0.0, chaos=0.0, variation=0.0)
        evaluator = WaveStepEvaluator(dt=0.01)

        outputs = [round(evaluator.evaluate(state, step_index=i), 6) for i in range(config.iterations)]

        return {
            "encoded_numbers": [float(n) for n in nums],
            "derived_frequency": [freq],
            "wave_trajectory": outputs
        }


def generate_parameter_sweeps(base_config: ExperimentConfig, sweep_params: Dict[str, List[Any]]) -> List[ExperimentConfig]:
    """Generate combinations of experiment configurations for parameter sweeps."""
    keys = list(sweep_params.keys())
    value_lists = [sweep_params[k] for k in keys]

    configs = []
    for idx, combo in enumerate(itertools.product(*value_lists)):
        params = dict(base_config.parameters)
        for k, v in zip(keys, combo):
            params[k] = v

        combo_str = "_".join(f"{k}{v}" for k, v in zip(keys, combo))
        exp_id = f"{base_config.experiment_id}_sweep_{idx + 1}_{combo_str}"
        name = f"{base_config.name} (Sweep {idx + 1})"

        cfg = ExperimentConfig(
            experiment_id=exp_id,
            name=name,
            description=base_config.description,
            model=base_config.model,
            parameters=params,
            input_state=base_config.input_state,
            seed=base_config.seed,
            iterations=base_config.iterations,
            metadata=base_config.metadata
        )
        configs.append(cfg)

    return configs
