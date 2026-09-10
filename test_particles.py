"""
Unit tests for matrix_particles.py.
"""

import unittest
from matrix_core import MatrixState
from matrix_particles import ParticleField


class TestParticles(unittest.TestCase):

    def test_particle_field_creation_and_update(self):
        field = ParticleField(count=10)
        self.assertEqual(len(field.particles), 10)

        initial_x = field.particles[0].x
        state = MatrixState(frequency=2.0)
        field.update_from_state(state)

        self.assertNotEqual(field.particles[0].x, initial_x)
        self.assertEqual(len(field.to_list()), 10)


if __name__ == "__main__":
    unittest.main()
