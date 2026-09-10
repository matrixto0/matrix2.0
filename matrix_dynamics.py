"""
Deterministic dynamics engine for MATRIX2.0.
"""

from typing import List, Optional, Dict, Any
import math
from matrix_core import MatrixState


def step(state: MatrixState, dt: float = 0.05, params: Optional[Dict[str, Any]] = None) -> MatrixState:
    """Evolves MatrixState by one time step dt."""
    f = state.frequency
    I = state.intensity
    phi = state.phase
    c = state.chaos

    new_phase = (phi + 2 * math.pi * f * dt) % (2 * math.pi)
    new_value = state.value + I * math.sin(new_phase) * dt
    noise = c * 0.01 if c > 0 else 0.0

    return MatrixState(
        value=round(new_value, 4),
        frequency=f,
        intensity=I,
        phase=round(new_phase, 4),
        chaos=c,
        variation=state.variation
    )


def evolve(state: MatrixState, steps: int = 10, dt: float = 0.05) -> List[MatrixState]:
    """Evolves MatrixState over multiple steps."""
    trajectory = [state]
    current = state
    for _ in range(steps):
        current = step(current, dt)
        trajectory.append(current)
    return trajectory
