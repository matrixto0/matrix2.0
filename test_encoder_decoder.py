"""
Unit tests for matrix_encode.py and matrix_decode.py.
"""

import unittest
from matrix_encode import encode
from matrix_decode import decode
from matrix_core import MatrixState


class TestEncoderDecoder(unittest.TestCase):

    def test_round_trip_encoding_decoding(self):
        samples = [
            "Hello World",
            "MATRIX 2.0",
            "Unicode: 🚀 Math Σ ∫",
            "",
            "1234567890!@#$%^&*()"
        ]

        for text in samples:
            state, metadata = encode(text)
            self.assertIsInstance(state, MatrixState)
            decoded = decode(state, metadata)
            self.assertEqual(decoded, text)

    def test_empty_string_encode(self):
        state, metadata = encode("")
        self.assertEqual(state.value, 0.0)
        decoded = decode(state, metadata)
        self.assertEqual(decoded, "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            encode(123)


if __name__ == "__main__":
    unittest.main()
