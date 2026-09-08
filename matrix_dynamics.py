"""
MATRIX2.0 Dynamic State Engine

Calculates wave dynamics and applies controlled chaotic variations
to a MatrixState model over time steps.
"""

import math
import random
from matrix_core import MatrixState


def compute_wave_value(intensity: float, frequency: float, t: float, phase: float) -> float:
    """
    Calculate pure sinusoidal wave output at time t.

    Formula: wave(t) = intensity * sin(2 * pi * frequency * t + phase)

    Parameters:
        intensity (float): Amplitude/power of the wave signal.
        frequency (float): Oscillations per time unit (Hz).
        t (float): Current simulation time stamp in seconds/units.
        phase (float): Current wave phase offset in radians.

    Returns:
        float: Instantaneous wave magnitude.
    """
    return intensity * math.sin(2.0 * math.pi * frequency * t + phase)


class MatrixDynamics:
    """
    Engine responsible for advancing MATRIX2.0 state dynamics through time.

    Maintains and updates:
    - value: Current scalar dynamic wave state output.
    - frequency: Base signal oscillation rate.
    - intensity: Wave magnitude / amplitude scale.
    - phase: Progressive angular displacement.
    - chaos: Scale of stochastic / random fluctuation added to parameters.
    - variation: Rate of gradual deterministic drift or modulation.
    """

    def __init__(self, state: MatrixState = None):
        """
        Initialize the dynamics engine with a MatrixState object.
        If no state is provided, a default MatrixState is created.
        """
        if state is None:
            self.state = MatrixState()
        else:
            self.state = state

    def step(self, t: float, dt: float = 0.01) -> MatrixState:
        """
        Advance the simulation state by step size dt at time t.

        1. Calculates basic wave equation value at time t:
           wave(t) = intensity * sin(2 * pi * frequency * t + phase)

        2. Applies controlled stochastic variation bounded by chaos:
           - chaos introduces random noise delta within [-chaos, +chaos].
           - variation introduces systematic parameter drift.

        3. Advances phase by (2 * pi * frequency * dt).

        4. Updates and returns the MatrixState object.
        """
        freq = self.state.frequency
        inten = self.state.intensity
        ph = self.state.phase
        ch = self.state.chaos
        var = self.state.variation

        # Compute base wave value at time t
        base_wave = compute_wave_value(inten, freq, t, ph)

        # Calculate chaotic noise perturbation
        chaotic_noise = random.uniform(-ch, ch) if ch > 0 else 0.0

        # Calculate variation shift (slight smooth modulation)
        variation_shift = var * math.cos(t)

        # Resulting dynamic value combination
        self.state.value = base_wave + chaotic_noise + variation_shift

        # Update phase progression based on frequency and dt
        self.state.phase = (ph + 2.0 * math.pi * freq * dt) % (2.0 * math.pi)

        # Apply small controlled variation/chaos perturbations to state parameters
        if ch > 0:
            freq_delta = random.uniform(-ch * 0.01, ch * 0.01)
            self.state.frequency = max(0.0, freq + freq_delta)

            inten_delta = random.uniform(-ch * 0.01, ch * 0.01)
            self.state.intensity = max(0.0, inten + inten_delta)

        return self.state


def step_dynamics(state: MatrixState, t: float, dt: float = 0.01) -> MatrixState:
    """
    Helper function to process a single time step on a given MatrixState.
    """
    engine = MatrixDynamics(state)
    return engine.step(t, dt)
