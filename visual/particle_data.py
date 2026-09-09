"""
MATRIX2.0 Particle Field Visualization Data Generator

Converts ParticleField states into plot-ready structured particle dictionaries.
Maps phase and value into 2D display coordinates (x, y) for UI rendering.
"""

import math
import os
import sys
from typing import List, Dict, Any, Optional

# Ensure repository root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_particles import ParticleField, MatrixParticle


class ParticleVisualization:
    """
    Generates structured particle field visualization dictionaries.
    Exposes id, value, frequency, intensity, phase, x, y, and full state dictionary.
    """

    def __init__(self, field: Optional[ParticleField] = None):
        self.field = field if field is not None else ParticleField()

    def generate_particle_nodes(self) -> List[Dict[str, Any]]:
        """
        Converts particles into visualization nodes with (x, y) 2D display coordinates.
        Coordinate Mapping:
        x = intensity * cos(phase)
        y = value + intensity * sin(phase)
        """
        nodes = []
        for idx, particle in enumerate(self.field.particles, 1):
            val = particle.value
            freq = particle.frequency
            inten = particle.intensity
            ph = particle.phase

            # Documented 2D polar projection display coordinate mapping
            x_coord = round(inten * math.cos(ph), 6)
            y_coord = round(val + (inten * math.sin(ph)), 6)

            node = {
                "id": idx,
                "value": round(val, 6),
                "frequency": round(freq, 6),
                "intensity": round(inten, 6),
                "phase": round(ph, 6),
                "x": x_coord,
                "y": y_coord,
                "state": particle.describe(),
            }
            nodes.append(node)
        return nodes

    def to_dict(self) -> Dict[str, Any]:
        """Returns structured dictionary containing particle count, average value, and particle nodes."""
        return {
            "particle_count": len(self.field.particles),
            "average_value": round(self.field.get_average_value(), 6),
            "particles": self.generate_particle_nodes(),
        }
