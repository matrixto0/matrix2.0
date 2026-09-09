"""
MATRIX2.0 Arcade Games Package Initialization
"""

from arcade.games.wave_runner import WaveRunnerGame
from arcade.games.phase_shift import PhaseShiftGame
from arcade.games.chaos_race import ChaosRaceGame
from arcade.games.particle_dance import ParticleDanceGame
from arcade.games.resonance_lab import ResonanceLabGame
from arcade.games.pattern_hunter import PatternHunterGame
from arcade.games.state_transformer import StateTransformerGame
from arcade.registry import REGISTRY

# Automatically register all 7 games
REGISTRY.register(WaveRunnerGame())
REGISTRY.register(PhaseShiftGame())
REGISTRY.register(ChaosRaceGame())
REGISTRY.register(ParticleDanceGame())
REGISTRY.register(ResonanceLabGame())
REGISTRY.register(PatternHunterGame())
REGISTRY.register(StateTransformerGame())
