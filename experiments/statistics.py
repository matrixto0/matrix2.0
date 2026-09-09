"""
Dependency-free statistical calculation utilities for MATRIX2.0 Experiment Engine.
"""

import math
from typing import Dict, List, Union


def mean(data: List[float]) -> float:
    """Calculate arithmetic mean."""
    if not data:
        return 0.0
    return sum(data) / len(data)


def median(data: List[float]) -> float:
    """Calculate median value."""
    if not data:
        return 0.0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    return float(sorted_data[mid])


def min_val(data: List[float]) -> float:
    """Calculate minimum value."""
    if not data:
        return 0.0
    return float(min(data))


def max_val(data: List[float]) -> float:
    """Calculate maximum value."""
    if not data:
        return 0.0
    return float(max(data))


def variance(data: List[float]) -> float:
    """Calculate population variance."""
    if len(data) <= 1:
        return 0.0
    avg = mean(data)
    return sum((x - avg) ** 2 for x in data) / len(data)


def std_dev(data: List[float]) -> float:
    """Calculate population standard deviation."""
    return math.sqrt(variance(data))


def range_val(data: List[float]) -> float:
    """Calculate statistical range (max - min)."""
    if not data:
        return 0.0
    return float(max(data) - min(data))


def calculate_summary_stats(data: List[float]) -> Dict[str, float]:
    """Compute complete summary statistics dict for a numerical series."""
    if not data:
        return {
            "count": 0,
            "mean": 0.0,
            "median": 0.0,
            "min": 0.0,
            "max": 0.0,
            "range": 0.0,
            "variance": 0.0,
            "std_dev": 0.0
        }

    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "min": min_val(data),
        "max": max_val(data),
        "range": range_val(data),
        "variance": variance(data),
        "std_dev": std_dev(data)
    }
