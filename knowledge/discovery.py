"""
Discovery Engine for detecting computational patterns in experiment results.
"""

from typing import Any, Dict, List
import math
from knowledge.provenance import Provenance


class Discovery:
    def __init__(
        self,
        discovery_id: str,
        discovery_type: str,
        pattern_description: str,
        source_experiments: List[str],
        calculation_method: str,
        confidence_score: float,
        reproducibility_info: Dict[str, Any]
    ):
        self.id = discovery_id
        self.type = discovery_type
        self.pattern_description = pattern_description
        self.source_experiments = source_experiments
        self.calculation_method = calculation_method
        self.confidence_score = confidence_score
        self.reproducibility_info = reproducibility_info
        self.disclaimer = "Observed computational pattern within MATRIX2.0 model; does not establish physical laws."

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "pattern_description": self.pattern_description,
            "source_experiments": self.source_experiments,
            "calculation_method": self.calculation_method,
            "confidence_score": round(self.confidence_score, 4),
            "reproducibility_info": self.reproducibility_info,
            "disclaimer": self.disclaimer
        }


class DiscoveryEngine:
    """Analyzes experiment results and extracts model-specific computational patterns."""

    def __init__(self):
        self.discoveries: List[Discovery] = []

    def analyze_experiment_results(self, experiment_results: List[Dict[str, Any]]) -> List[Discovery]:
        discovered = []

        if len(experiment_results) < 2:
            return discovered

        # Pattern 1: Frequency vs Energy Scaling Pattern
        f_energies = []
        for res in experiment_results:
            params = res.get("configuration", {})
            metrics = res.get("measurements", {})
            if "f" in params and "mean_energy" in metrics:
                f_energies.append((params["f"], metrics["mean_energy"], res.get("experiment_id"), res.get("seed")))

        if len(f_energies) >= 2:
            f_energies.sort(key=lambda x: x[0])
            is_monotonic = all(f_energies[i][1] <= f_energies[i+1][1] for i in range(len(f_energies)-1))
            if is_monotonic:
                exp_ids = [item[2] for item in f_energies]
                seeds = [item[3] for item in f_energies]

                # Ranking score = 0.5 + 0.1 * count (max 1.0)
                score = min(1.0, 0.5 + 0.1 * len(f_energies))

                d = Discovery(
                    discovery_id="disc_monotonic_energy_scaling",
                    discovery_type="parameter_scaling_pattern",
                    pattern_description="Monotonic increase in mean energy observed as frequency increases.",
                    source_experiments=exp_ids,
                    calculation_method="Order-sorted pair comparison of frequency vs mean energy",
                    confidence_score=score,
                    reproducibility_info={"seeds": seeds, "samples": len(f_energies)}
                )
                discovered.append(d)

        self.discoveries.extend(discovered)
        return discovered
