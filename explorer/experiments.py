"""
MATRIX2.0 Explorer Interactive Experiments

Provides structured, parameterizable experiment functions for learning.
"""

import math
from typing import Dict, Any, List
from matrix_core import MatrixState
from matrix_dynamics import MatrixDynamics, step_dynamics
from matrix_particles import MatrixParticle, ParticleField
from matrix_encode import encode_text
from matrix_decode import decode_values


def exp_1_frequency_change(freq_a: float = 0.5, freq_b: float = 2.0) -> Dict[str, Any]:
    """Experiment 1: What happens when frequency changes?"""
    s_a = MatrixState(frequency=freq_a, intensity=1.0)
    s_b = MatrixState(frequency=freq_b, intensity=1.0)

    res_a = [step_dynamics(s_a, t=t * 0.1).value for t in range(5)]
    res_b = [step_dynamics(s_b, t=t * 0.1).value for t in range(5)]

    return {
        "title": "Frequency Impact Experiment",
        "freq_a": freq_a,
        "wave_a": res_a,
        "freq_b": freq_b,
        "wave_b": res_b,
        "observation": f"Higher frequency ({freq_b}) completes cycles much faster than lower frequency ({freq_a}).",
    }


def exp_2_intensity_change(inten_a: float = 0.5, inten_b: float = 2.5) -> Dict[str, Any]:
    """Experiment 2: What happens when intensity changes?"""
    s_a = MatrixState(frequency=1.0, intensity=inten_a)
    s_b = MatrixState(frequency=1.0, intensity=inten_b)

    val_a = step_dynamics(s_a, t=0.25).value
    val_b = step_dynamics(s_b, t=0.25).value

    return {
        "title": "Intensity Impact Experiment",
        "intensity_a": inten_a,
        "peak_a": val_a,
        "intensity_b": inten_b,
        "peak_b": val_b,
        "observation": f"Higher intensity ({inten_b}) scales wave amplitude linearly relative to lower intensity ({inten_a}).",
    }


def exp_3_phase_change(phase_shift: float = math.pi) -> Dict[str, Any]:
    """Experiment 3: What happens when phase changes?"""
    s_a = MatrixState(frequency=1.0, intensity=1.0, phase=0.0)
    s_b = MatrixState(frequency=1.0, intensity=1.0, phase=phase_shift)

    val_a = step_dynamics(s_a, t=0.0).value
    val_b = step_dynamics(s_b, t=0.0).value

    return {
        "title": "Phase Shift Experiment",
        "initial_val_zero_phase": val_a,
        "initial_val_shifted_phase": val_b,
        "phase_shift_rad": phase_shift,
        "observation": f"Shifting phase by {phase_shift:.2f} rad changes the wave's starting displacement at t=0.",
    }


def exp_4_chaos_disruption(chaos_level: float = 0.05) -> Dict[str, Any]:
    """Experiment 4: Can chaos change a predictable wave?"""
    s_clean = MatrixState(frequency=1.0, intensity=1.0, chaos=0.0)
    s_chaotic = MatrixState(frequency=1.0, intensity=1.0, chaos=chaos_level)

    clean_vals = [step_dynamics(s_clean, t=t * 0.1).value for t in range(5)]
    chaotic_vals = [step_dynamics(s_chaotic, t=t * 0.1).value for t in range(5)]

    diffs = [abs(c - k) for c, k in zip(chaotic_vals, clean_vals)]

    return {
        "title": "Chaos Disruption Experiment",
        "clean_wave": clean_vals,
        "chaotic_wave": chaotic_vals,
        "max_deviation": max(diffs),
        "observation": f"Chaos level {chaos_level} introduces stochastic perturbations disrupting predictability.",
    }


def exp_5_wave_interaction(state_a: MatrixState, state_b: MatrixState) -> Dict[str, Any]:
    """Experiment 5: Can two waves interact?"""
    e_a = MatrixDynamics(state_a)
    e_b = MatrixDynamics(state_b)

    t = 0.25
    v_a = e_a.step(t).value
    v_b = e_b.step(t).value
    combined = v_a + v_b

    return {
        "title": "Wave Interaction Experiment",
        "wave_a_value": v_a,
        "wave_b_value": v_b,
        "superposition_value": combined,
        "observation": "Two waves combine through constructive or destructive linear superposition.",
    }


def exp_6_word_to_numbers(word: str = "MOTHER") -> Dict[str, Any]:
    """Experiment 6: Can a word become numbers?"""
    encoded = encode_text(word)
    return {
        "title": "Word to Numbers Experiment",
        "input_word": word,
        "ascii_numbers": encoded,
        "observation": f"The text '{word}' is transformed into discrete ASCII numerical codes: {encoded}.",
    }


def exp_7_numbers_to_dynamic_state(word: str = "MOTHER") -> Dict[str, Any]:
    """Experiment 7: Can numbers become a dynamic state?"""
    encoded = encode_text(word)
    avg_val = sum(encoded) / len(encoded) if encoded else 0.0

    state = MatrixState(
        value=avg_val / 100.0,
        frequency=len(word) / 5.0,
        intensity=max(encoded) / 100.0 if encoded else 1.0,
    )

    updated = step_dynamics(state, t=0.5)

    return {
        "title": "Numbers to Dynamic State Experiment",
        "encoded_values": encoded,
        "constructed_state": state.describe(),
        "updated_wave_value": updated.value,
        "observation": f"Symbolic values were encoded into initial MatrixState parameters and advanced dynamically.",
    }


def exp_8_particle_field_evolution(particle_count: int = 5, seed: int = 42) -> Dict[str, Any]:
    """Experiment 8: Can multiple particles evolve together?"""
    field = ParticleField(seed=seed)
    field.generate_random_particles(count=particle_count, seed=seed)

    initial_avg = field.get_average_value()
    field.step_field(t=0.5, dt=0.01)
    evolved_avg = field.get_average_value()

    return {
        "title": "Particle Field Evolution Experiment",
        "particle_count": particle_count,
        "seed": seed,
        "initial_avg_value": initial_avg,
        "evolved_avg_value": evolved_avg,
        "observation": f"A field of {particle_count} particles evolved synchronously across time steps.",
    }
