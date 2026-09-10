"""
Symbolic decoder for MATRIX2.0.
Reconstructs original text from MatrixState and metadata payload.
"""

from typing import Optional, Dict, Any
from matrix_core import MatrixState


def decode(state: MatrixState, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Decodes a MatrixState and metadata payload back into the original string."""
    if not isinstance(state, MatrixState):
        raise TypeError("Expected MatrixState object.")

    if metadata and "char_codes" in metadata:
        return "".join(chr(c) for c in metadata["char_codes"])

    if metadata and "original_text" in metadata:
        return metadata["original_text"]

    if state.value == 0.0:
        return ""

    return f"DecodedState(val={state.value}, freq={state.frequency})"
