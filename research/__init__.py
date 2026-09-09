"""
Research Module for MATRIX2.0.
Provides Hypothesis, Observation, and Conclusion primitives for experimental workflows.
"""

from research.hypothesis import Hypothesis
from research.observation import Observation, ObservationLogger
from research.conclusion import Conclusion

__all__ = [
    "Hypothesis",
    "Observation",
    "ObservationLogger",
    "Conclusion"
]
