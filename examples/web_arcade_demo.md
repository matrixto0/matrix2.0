# MATRIX2.0 Web Simulation Universe — User Workflow & Demo Guide

This guide demonstrates how to launch and interact with the **MATRIX2.0 Web Simulation Universe**.

---

## Step 1: Launch Local Web Server

Start Python's standard HTTP server from the repository root:

```bash
python3 -m http.server 8080 --directory web
```

Output:
```
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
```

Navigate to `http://localhost:8080` in any modern browser.

---

## Step 2: Select an Arcade Game

On the Arcade Dashboard grid, click on any of the game cards:
- **Wave Runner 2.0**: Focuses on sinusoidal oscillation stability.
- **Phase Shift**: Focuses on wave interference and alignment.
- **Chaos Race**: Demonstrates stochastic noise impact on trajectories.
- **Particle Dance**: Displays multi-particle polar field motion.
- **Resonance Lab**: Tests peak amplitude matching.
- **Pattern Hunter**: Targets precise harmonic frequencies.
- **State Transformer**: Integrates variation state parameter dynamics.

When selected, the controls panel updates with default parameters for that game.

---

## Step 3: Manipulate Parameters & Inspect State Vector

Use the interactive sliders to adjust simulation variables in real-time:
- **Frequency ($f$)**: 0.1 to 5.0 Hz
- **Intensity ($I$)**: 0.1 to 3.0
- **Phase ($\phi$)**: 0.0 to 6.28 radians
- **Chaos ($c$)**: 0.00 to 0.20 stochastic noise
- **Variation ($v$)**: 0.00 to 0.10 parameter drift

Observe immediate updates in the **MATRIX State Vector Inspector**:
```
Equation: W(t) = 1.50 sin(2π · 2.00t + 0.50)
Vector:   M = (f=2.00, I=1.50, φ=0.50, c=0.02, v=0.01)
```

Observe simultaneous 60 FPS animation updates on both the **Live Sinusoidal Wave Canvas** and **Particle Field Polar Projection Canvas**.

---

## Step 4: Execute Scientific Prediction Loop

1. Read the active mission prompt (e.g. *"Adjust wave parameters to stabilize resonance"*).
2. Enter your scientific hypothesis in the input box:
   > *"Increasing frequency to 2.0 Hz will double oscillation rate without destabilizing amplitude."*
3. Click **Run Simulation**.
4. View the evaluated outcome panel:
   - **Result**: `CONFIRMED`
   - **Score**: `100 pts`
   - **Explanation**: Explanation of state vector trajectory behavior.

---

## Step 5: Review Local Experiment History

Scroll to the **Local Experiment History** table to see logged records stored in `localStorage`.
- Each record logs the timestamp, game name, active state vector, user prediction, confirmed status, and earned points.
- Click **Clear Experiment History** to reset local storage whenever desired.
