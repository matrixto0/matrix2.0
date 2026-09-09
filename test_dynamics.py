"""
Unit tests for MATRIX2.0 dynamic state engine (matrix_dynamics.py).
"""

import math
import unittest
from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics, compute_wave_value, step_dynamics


class TestMatrixDynamics(unittest.TestCase):
    def test_compute_wave_value(self):
        """Test pure sine wave calculation."""
        intensity = 1.0
        frequency = 1.0
        t = 0.25
        phase = 0.0

        # sin(2 * pi * 1.0 * 0.25 + 0) = sin(pi/2) = 1.0
        val = compute_wave_value(intensity, frequency, t, phase)
        self.assertAlmostEqual(val, 1.0, places=5)

    def test_deterministic_step(self):
        """Test dynamics step without chaos or variation."""
        state = MatrixState(
            frequency=1.0,
            intensity=2.0,
            phase=0.0,
            chaos=0.0,
            variation=0.0,
        )
        engine = MatrixDynamics(state)

        # At t=0.25, sin(2*pi*1*0.25) = 1.0, intensity=2.0 => value = 2.0
        updated_state = engine.step(t=0.25, dt=0.01)

        self.assertAlmostEqual(updated_state.value, 2.0, places=5)
        # Phase after dt=0.01: 2*pi*1.0*0.01 = 0.02 * pi
        expected_phase = (2.0 * math.pi * 0.01) % (2.0 * math.pi)
        self.assertAlmostEqual(updated_state.phase, expected_phase, places=5)

    def test_step_with_chaos_and_variation(self):
        """Test that chaos and variation alter state value within expected bounds."""
        state = MatrixState(
            frequency=1.02,
            intensity=0.99,
            phase=0.0,
            chaos=0.01,
            variation=0.01,
        )
        engine = MatrixDynamics(state)
        updated_state = engine.step(t=0.0, dt=0.05)

        # Base wave at t=0, phase=0 is 0.0.
        # Max chaotic noise = +-0.01.
        # Variation shift = 0.01 * cos(0) = 0.01.
        # Max bound = 0.02, Min bound = 0.0
        self.assertGreaterEqual(updated_state.value, -0.02)
        self.assertLessEqual(updated_state.value, 0.02)

    def test_step_dynamics_helper(self):
        """Test helper function step_dynamics."""
        state = MatrixState(
            frequency=2.0,
            intensity=1.5,
            phase=0.0,
            chaos=0.0,
            variation=0.0,
        )
        res_state = step_dynamics(state, t=0.125, dt=0.01)
        # sin(2 * pi * 2.0 * 0.125) = sin(pi/2) = 1.0; 1.0 * 1.5 = 1.5
        self.assertAlmostEqual(res_state.value, 1.5, places=5)
        self.assertEqual(res_state.describe()["frequency"], 2.0)


if __name__ == "__main__":
    unittest.main()
