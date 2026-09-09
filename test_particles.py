"""
Unit tests for MATRIX2.0 particle field model (matrix_particles.py).
"""

import unittest
from matrix_core import MatrixState
from matrix_particles import MatrixParticle, ParticleField


class TestMatrixParticles(unittest.TestCase):
    def test_particle_creation(self):
        """Test creating individual MatrixParticle."""
        p = MatrixParticle(frequency=1.5, intensity=0.8, chaos=0.01)
        self.assertEqual(p.frequency, 1.5)
        self.assertEqual(p.intensity, 0.8)
        self.assertEqual(p.chaos, 0.01)
        self.assertIsInstance(p.state, MatrixState)

    def test_particle_step(self):
        """Test particle step execution."""
        p = MatrixParticle(frequency=1.0, intensity=1.0, phase=0.0, chaos=0.0, variation=0.0)
        p.step(t=0.25, dt=0.01)
        self.assertAlmostEqual(p.value, 1.0, places=5)

    def test_field_updates(self):
        """Test updating all particles in a ParticleField."""
        p1 = MatrixParticle(frequency=1.0, intensity=1.0)
        p2 = MatrixParticle(frequency=2.0, intensity=0.5)

        field = ParticleField(particles=[p1, p2])
        self.assertEqual(len(field.particles), 2)

        states = field.step_field(t=0.1, dt=0.01)
        self.assertEqual(len(states), 2)
        self.assertIsInstance(states[0], MatrixState)

    def test_seed_determinism(self):
        """Test that random seed guarantees deterministic behavior."""
        field1 = ParticleField()
        field1.generate_random_particles(count=5, seed=42)
        field1.step_field(t=0.5, dt=0.01)

        field2 = ParticleField()
        field2.generate_random_particles(count=5, seed=42)
        field2.step_field(t=0.5, dt=0.01)

        states1 = field1.get_states()
        states2 = field2.get_states()

        for s1, s2 in zip(states1, states2):
            self.assertAlmostEqual(s1["value"], s2["value"], places=7)
            self.assertAlmostEqual(s1["frequency"], s2["frequency"], places=7)

    def test_average_value(self):
        """Test calculating average field value."""
        p1 = MatrixParticle(value=1.0)
        p2 = MatrixParticle(value=3.0)
        field = ParticleField(particles=[p1, p2])
        self.assertAlmostEqual(field.get_average_value(), 2.0, places=5)


if __name__ == "__main__":
    unittest.main()
