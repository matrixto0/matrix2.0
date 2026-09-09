# MATRIX2.0 Web Simulation Universe — API Architecture & Design Specification

## Overview

This document specifies the RESTful and WebSocket API contract for connecting the **MATRIX2.0 Web Simulation Universe** frontend interface with backend Python computational services (`arcade`, `matrix_dynamics`, `matrix_particles`, `chaos`).

---

## 1. Data Models & Schemas

### 1.1 State Vector Schema (`MatrixStateVector`)
Representing the core state vector transferred between client and server:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MatrixStateVector",
  "type": "object",
  "properties": {
    "x": { "type": "number", "description": "Base x position or phase reference" },
    "frequency": { "type": "number", "minimum": 0.0, "description": "Oscillation frequency in Hz" },
    "intensity": { "type": "number", "minimum": 0.0, "description": "State amplitude / intensity" },
    "phase": { "type": "number", "description": "Phase offset in radians" },
    "chaos": { "type": "number", "minimum": 0.0, "maximum": 1.0, "description": "Stochastic noise parameter" },
    "variation": { "type": "number", "minimum": 0.0, "maximum": 1.0, "description": "Systematic parameter drift" }
  },
  "required": ["x", "frequency", "intensity", "phase", "chaos", "variation"]
}
```

---

## 2. REST Endpoints Specification

### 2.1 `GET /api/v1/games`
Returns the list of available arcade simulation games.

**Response `200 OK`**:
```json
[
  {
    "id": "wave_runner",
    "name": "Wave Runner 2.0",
    "description": "Navigate dynamic sinusoidal wave state vectors.",
    "target_metric": "amplitude",
    "difficulty": "Beginner",
    "mission": "Adjust wave parameters to stabilize resonance.",
    "default_params": {
      "frequency": 1.0,
      "intensity": 1.0,
      "phase": 0.0,
      "chaos": 0.0,
      "variation": 0.0
    }
  }
]
```

### 2.2 `POST /api/v1/simulate`
Executes a simulation step or multi-step trajectory based on submitted state parameters.

**Request Body**:
```json
{
  "game_id": "wave_runner",
  "steps": 100,
  "dt": 0.01,
  "state": {
    "x": 0.0,
    "frequency": 1.5,
    "intensity": 1.2,
    "phase": 0.0,
    "chaos": 0.02,
    "variation": 0.01
  }
}
```

**Response `200 OK`**:
```json
{
  "game_id": "wave_runner",
  "trajectory": [
    { "t": 0.00, "val": 0.00, "state_hash": "a1b2c3d4" },
    { "t": 0.01, "val": 0.11, "state_hash": "e5f6g7h8" }
  ],
  "summary": {
    "peak_intensity": 1.2,
    "mean_frequency": 1.5,
    "entropy": 0.024
  }
}
```

### 2.3 `POST /api/v1/predict`
Evaluates a user prediction against a target mission trajectory.

**Request Body**:
```json
{
  "game_id": "chaos_race",
  "prediction": "Increasing chaos above 0.15 will cause phase space divergence.",
  "parameters": {
    "frequency": 2.0,
    "intensity": 1.5,
    "chaos": 0.18
  }
}
```

**Response `200 OK`**:
```json
{
  "prediction_confirmed": true,
  "accuracy_score": 95.0,
  "explanation": "Chaos parameter 0.18 exceeded divergence threshold 0.15. Lyapunov exponent > 0.",
  "rewards": {
    "points_earned": 100,
    "badge": "Chaos Analyst"
  }
}
```

---

## 3. Real-Time Streaming API (WebSocket)

### `WS /ws/v1/live-simulation`
Provides real-time bidirectional state streaming for interactive visualizations.

* **Client Message (Update Parameters)**:
```json
{
  "action": "update_state",
  "params": {
    "frequency": 2.5,
    "intensity": 1.8
  }
}
```

* **Server Message (Frame Stream)**:
```json
{
  "event": "frame",
  "time": 12.45,
  "wave_sample": [0.1, 0.4, 0.8, 0.9, 0.5, -0.1],
  "particle_count": 36,
  "entropy": 0.015
}
```

---

## 4. Epistemological Boundary

The API serves deterministic mathematical representations of simulated wave/particle systems. Outputs are computational state vectors and do not correspond to physical physical systems or energy phenomena.
