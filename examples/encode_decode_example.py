"""
Minimal example demonstrating MATRIX2.0 text encoding and decoding.
"""

import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from matrix_encode import encode_text
from matrix_decode import decode_values


def main():
    text = "HELLO MATRIX"
    print(f"Original Text: '{text}'")

    encoded_values = encode_text(text)
    print(f"Encoded Values: {encoded_values}")

    decoded_text = decode_values(encoded_values)
    print(f"Decoded Text:  '{decoded_text}'")


if __name__ == "__main__":
    main()
