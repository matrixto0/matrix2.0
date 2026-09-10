"""
Unit tests for matrix_dynamics.py.
"""

import unittest
from matrix_core import MatrixState
from matrix_dynamics import step, evolve


class TestDynamics(unittest.TestCase):

    def test_single_step_evolution(self):
        initial = MatrixState(value=1.0, frequency=1.0, intensity=1.0, phase=0.0)
        next_state = step(initial, dt=0.05)

        self.assertIsInstance(next_state, MatrixState)
        self.assertEqual(next_state.frequency, 1.0)
        self.assertNotEqual(next_state.phase, initial.phase)

    def test_multi_step_trajectory(self):
        initial = MatrixState(value=1.0, frequency=1.0)
        trajectory = evolve(initial, steps=10, dt=0.05)

        self.assertEqual(len(trajectory), 11)
        self.assertEqual(trajectory[0], initial)


if __name__ == "__main__":
    unittest.main()
