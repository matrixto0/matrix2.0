# MATRIX2.0 Research Dashboard

The **MATRIX2.0 Research Dashboard** is the primary visual interface for MATRIX2.0 computational experimentation. It enables researchers to inspect mathematical state dynamics, launch reproducible experiments, compare computational outputs, and maintain local research records.

## Features

- **Home Screen**: Pipeline flow diagram detailing all MATRIX2.0 layers and implementation status.
- **Live Simulation**: Interactive 6D state inspector $M = (x, f, I, \phi, c, v)$ with real-time wave $W(t) = I \sin(2\pi f t + \phi)$ and particle field rendering.
- **Experiment Launcher**: Integrated execution engine for registered experiments with metrics, statistics, and JSON export.
- **Experiment Comparison**: Side-by-side comparison matrix with parameter and metric diffs.
- **Metrics View**: Native Canvas line and bar chart visualizations for trajectory analysis.
- **History & Research Notebook**: Local persistent tracking via `localStorage` with notebook logging.
- **Zero External Dependencies**: Pure HTML5/JS/CSS implementation running completely local-first.

## Usage

Simply open `dashboard/index.html` in any modern browser or serve via a local HTTP server:

```bash
python3 -m http.server 8000
```

Navigate to `http://localhost:8000/dashboard/`.
