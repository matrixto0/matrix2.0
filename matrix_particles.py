"""
MATRIX2.0 Particle Field Model

Implements individual wave particles (MatrixParticle) and multi-particle fields
(ParticleField) built upon MatrixState and MatrixDynamics.
"""

import math
import random
from typing import List, Optional
from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics


class MatrixParticle:
    """
    Represents an individual wave particle in MATRIX2.0 system.

    Attributes:
        state (MatrixState): Holds value, frequency, intensity, phase, chaos, variation.
        dynamics (MatrixDynamics): Engine updating particle dynamics.
    """

    def __init__(
        self,
        value: float = 0.0,
        frequency: float = 1.0,
        intensity: float = 1.0,
        phase: float = 0.0,
        chaos: float = 0.0,
        variation: float = 0.0,
        state: Optional[MatrixState] = None,
    ):
        if state is not None:
            self.state = state
        else:
            self.state = MatrixState(
                value=value,
                frequency=frequency,
                intensity=intensity,
                phase=phase,
                chaos=chaos,
                variation=variation,
            )
        self.dynamics = MatrixDynamics(self.state)

    @property
    def value(self) -> float:
        return self.state.value

    @property
    def frequency(self) -> float:
        return self.state.frequency

    @property
    def intensity(self) -> float:
        return self.state.intensity

    @property
    def phase(self) -> float:
        return self.state.phase

    @property
    def chaos(self) -> float:
        return self.state.chaos

    @property
    def variation(self) -> float:
        return self.state.variation

    def step(self, t: float, dt: float = 0.01) -> MatrixState:
        """Advance the individual particle dynamics by time step dt at time t."""
        return self.dynamics.step(t=t, dt=dt)

    def describe(self) -> dict:
        """Return parameter state dictionary of particle."""
        return self.state.describe()


class ParticleField:
    """
    Container field managing multiple MatrixParticle instances.
    """

    def __init__(
        self,
        particles: Optional[List[MatrixParticle]] = None,
        seed: Optional[int] = None,
    ):
        if seed is not None:
            random.seed(seed)

        self.particles: List[MatrixParticle] = particles if particles is not None else []

    def add_particle(self, particle: MatrixParticle) -> None:
        """Add a particle to the field."""
        self.particles.append(particle)

    def generate_random_particles(
        self,
        count: int,
        freq_range: tuple = (0.5, 2.0),
        intensity_range: tuple = (0.5, 1.5),
        chaos_range: tuple = (0.0, 0.05),
        variation_range: tuple = (0.0, 0.05),
        seed: Optional[int] = None,
    ) -> None:
        """
        Generate `count` randomized particles into the field.
        Determinism is guaranteed when a seed is provided.
        """
        if seed is not None:
            random.seed(seed)

        for _ in range(count):
            freq = random.uniform(*freq_range)
            inten = random.uniform(*intensity_range)
            ph = random.uniform(0.0, 2.0 * math.pi)
            ch = random.uniform(*chaos_range)
            var = random.uniform(*variation_range)

            p = MatrixParticle(
                frequency=freq,
                intensity=inten,
                phase=ph,
                chaos=ch,
                variation=var,
            )
            self.add_particle(p)

    def step_field(self, t: float, dt: float = 0.01) -> List[MatrixState]:
        """
        Update state for all particles in the field for given time t and step dt.
        """
        return [p.step(t=t, dt=dt) for p in self.particles]

    def get_states(self) -> List[dict]:
        """Return descriptions for all particles in field."""
        return [p.describe() for p in self.particles]

    def get_average_value(self) -> float:
        """Compute mean wave value across all field particles."""
        if not self.particles:
            return 0.0
        return sum(p.value for p in self.particles) / len(self.particles)
