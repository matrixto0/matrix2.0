# MATRIX2.0 Web Simulation Universe

Welcome to the **MATRIX2.0 Web Simulation Universe**, an interactive web-based platform bringing MATRIX2.0 state vector dynamics, sinusoidal wave visualizations, particle field projections, and simulation arcade games directly into standard web browsers.

---

## 🌟 Key Features

1. **Arcade Dashboard**:
   - Live browser cards for all 7 simulation games (`Wave Runner`, `Phase Shift`, `Chaos Race`, `Particle Dance`, `Resonance Lab`, `Pattern Hunter`, `State Transformer`).
2. **Interactive Parameter Controls**:
   - Real-time sliders for frequency ($f$), intensity ($I$), phase ($\phi$), chaos ($c$), and variation ($v$).
3. **Dual HTML5 Canvas Visualizer**:
   - Real-time 60 FPS rendering of dynamic sinusoidal wave profiles $W(t) = I \sin(2\pi ft + \phi)$ and 36-particle field polar projections.
4. **MATRIX State Vector Inspector**:
   - Dynamic formula rendering and real-time numerical state vector display.
5. **Scientific Prediction & Experiment Loop**:
   - Formulate scientific predictions before running simulations; evaluate hypothesis correctness and track scores.
6. **Local Experiment Logging**:
   - Preserves experiment records, state vectors, user predictions, and earned scores across browser sessions via `localStorage`.

---

## 📁 Architecture & File Structure

```
web/
├── data/
│   └── games.json       # Game metadata and default state parameters
├── index.html           # Main UI layout & responsive web workspace
├── style.css            # Dark mode GitHub-inspired styling & layout
├── app.js               # Canvas renderer, state vector inspector, experiment engine
├── API_DESIGN.md        # API specification for REST & WebSocket integrations
├── test_web.py          # Python test suite verifying web assets integrity
└── README.md            # Module overview & quick start guide
```

---

## 🚀 Quick Start (Local Web Server)

You can launch the Web Simulation Universe using Python's built-in HTTP server:

```bash
# Navigate to repository root or web directory
python3 -m http.server 8000 --directory web
```

Then open your browser to:
`http://localhost:8000`

---

## 🧪 Testing

To test web asset validity, structure, and JSON integrity:

```bash
python3 -m unittest web/test_web.py
```

---

## 🔬 Scientific Disclaimer

MATRIX2.0 web simulations represent mathematical state vectors and computational model states. They do not simulate physical matter, physical wave dynamics, or consciousness.
