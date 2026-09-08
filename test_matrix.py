from matrix_core import MatrixState


state = MatrixState(
    value=1.0,
    frequency=0.08,
    intensity=0.12,
    phase=0.0,
    chaos=0.01,
    variation=0.01,
)

print(state.describe())
