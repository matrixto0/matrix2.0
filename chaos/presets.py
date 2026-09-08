"""
MATRIX2.0 Chaos Presets

Defines numerical parameter presets for chaos and variation levels:
- CALM: Minimal to zero chaos and variation.
- LOW: Slight stochastic noise.
- MEDIUM: Moderate noise and drift.
- HIGH: Strong chaotic perturbation.
- EXTREME: High volatility state dynamics.
"""

from typing import Dict, Any, Optional

CHAOS_PRESETS: Dict[str, Dict[str, float]] = {
    "CALM": {
        "chaos": 0.0,
        "variation": 0.0,
    },
    "LOW": {
        "chaos": 0.005,
        "variation": 0.005,
    },
    "MEDIUM": {
        "chaos": 0.02,
        "variation": 0.02,
    },
    "HIGH": {
        "chaos": 0.08,
        "variation": 0.05,
    },
    "EXTREME": {
        "chaos": 0.25,
        "variation": 0.15,
    },
}


def get_preset(name: str) -> Dict[str, float]:
    """
    Retrieve a preset dictionary by name (case-insensitive).
    Raises ValueError if preset name is invalid.
    """
    key = name.upper().strip()
    if key not in CHAOS_PRESETS:
        raise ValueError(
            f"Unknown preset '{name}'. Available presets: {list(CHAOS_PRESETS.keys())}"
        )
    return dict(CHAOS_PRESETS[key])
