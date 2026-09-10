"""
Experimental particle field representation for MATRIX2.0.
"""

from typing import List, Dict, Any
from matrix_core import MatrixState


class Particle:
    def __init__(self, particle_id: int, x: float, y: float, vx: float, vy: float):
        self.id = particle_id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "x": self.x, "y": self.y, "vx": self.vx, "vy": self.vy}


class ParticleField:
    """Computational particle field mapped from MatrixState."""

    def __init__(self, count: int = 20):
        self.particles: List[Particle] = []
        for i in range(count):
            self.particles.append(Particle(i, i * 0.1, i * 0.1, 0.01, 0.01))

    def update_from_state(self, state: MatrixState):
        multiplier = state.frequency * 0.1
        for p in self.particles:
            p.x += p.vx * multiplier
            p.y += p.vy * multiplier

    def to_list(self) -> List[Dict[str, Any]]:
        return [p.to_dict() for p in self.particles]
