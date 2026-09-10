"""
Symbolic encoder for MATRIX2.0.
Converts text input into a 6D MatrixState vector and metadata payload.
"""

from typing import Tuple, Dict, Any
from matrix_core import MatrixState


def encode(text: str) -> Tuple[MatrixState, Dict[str, Any]]:
    """Encodes string input into a MatrixState and metadata payload."""
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    if not text:
        return MatrixState(value=0.0, frequency=0.0, intensity=0.0, phase=0.0, chaos=0.0, variation=0.0), {"char_codes": [], "length": 0}

    char_codes = [ord(c) for c in text]
    length = len(char_codes)
    avg_code = sum(char_codes) / length if length > 0 else 0.0

    state = MatrixState(
        value=float(length),
        frequency=round(avg_code / 100.0, 4),
        intensity=round((max(char_codes) - min(char_codes)) / 10.0, 4) if length > 1 else 1.0,
        phase=round((char_codes[0] % 360) / 100.0, 4),
        chaos=0.01,
        variation=0.01
    )

    metadata = {
        "char_codes": char_codes,
        "length": length,
        "original_text": text
    }

    return state, metadata
