/**
 * MATRIX2.0 Research Dashboard - State Management
 */

class DashboardState {
    constructor() {
        this.listeners = [];
        this.state = {
            matrix: {
                x: 1.0,
                f: 1.0,
                I: 1.0,
                phi: 0.0,
                c: 0.1,
                v: 0.1
            },
            simulation: {
                running: false,
                t: 0,
                speed: 1.0
            },
            particleConfig: {
                count: 50,
                f_influence: 0.5,
                I_influence: 0.5,
                c_influence: 0.5
            },
            experiments: [
                {
                    id: "exp_001_phase_stability",
                    name: "Phase Stability Under Variation",
                    question: "How does parameter variation affect phase stability across iterations?",
                    parameters: { f: 1.5, I: 2.0, phi: 0.0, c: 0.05, v: 0.1 },
                    seed: 42,
                    iterations: 100
                },
                {
                    id: "exp_002_chaos_transition",
                    name: "Chaos Perturbation Transition",
                    question: "What is the threshold where chaos dominates wave coherence?",
                    parameters: { f: 2.0, I: 1.5, phi: 0.25, c: 0.4, v: 0.2 },
                    seed: 123,
                    iterations: 150
                },
                {
                    id: "exp_003_particle_coherence",
                    name: "Particle Energy Distribution Coherence",
                    question: "Does particle kinetic dispersion correlate with state intensity?",
                    parameters: { f: 3.0, I: 2.5, phi: 0.5, c: 0.15, v: 0.05 },
                    seed: 999,
                    iterations: 80
                },
                {
                    id: "exp_004_entropy_decay",
                    name: "State Entropy Decay Simulation",
                    question: "How rapidly does state variance decay under zero variation?",
                    parameters: { f: 1.0, I: 1.0, phi: 0.0, c: 0.0, v: 0.0 },
                    seed: 7,
                    iterations: 200
                }
            ],
            currentExperimentResult: null,
            comparison: {
                expA: null,
                expB: null
            },
            history: this.loadHistory(),
            notebookEntries: this.loadNotebook(),
            researchRecords: this.loadResearchRecords()
        };
    }

    subscribe(listener) {
        this.listeners.push(listener);
    }

    notify() {
        this.listeners.forEach(cb => cb(this.state));
    }

    updateMatrixState(key, value) {
        this.state.matrix[key] = parseFloat(value);
        this.notify();
    }

    setSimulationRunning(running) {
        this.state.simulation.running = running;
        this.notify();
    }

    resetSimulation() {
        this.state.simulation.t = 0;
        this.notify();
    }

    stepSimulation(dt = 0.02) {
        if (this.state.simulation.running) {
            this.state.simulation.t += dt * this.state.simulation.speed;
            this.notify();
        }
    }

    saveExperimentToHistory(result) {
        this.state.history.unshift(result);
        localStorage.setItem("matrix2_exp_history", JSON.stringify(this.state.history));
        this.notify();
    }

    loadHistory() {
        try {
            const data = localStorage.getItem("matrix2_exp_history");
            return data ? JSON.parse(data) : [];
        } catch (e) {
            return [];
        }
    }

    clearHistory() {
        this.state.history = [];
        localStorage.removeItem("matrix2_exp_history");
        this.notify();
    }

    saveNotebookEntry(entry) {
        entry.id = "note_" + Date.now();
        entry.timestamp = new Date().toISOString();
        this.state.notebookEntries.unshift(entry);
        localStorage.setItem("matrix2_notebook", JSON.stringify(this.state.notebookEntries));
        this.notify();
    }

    loadNotebook() {
        try {
            const data = localStorage.getItem("matrix2_notebook");
            return data ? JSON.parse(data) : [];
        } catch (e) {
            return [];
        }
    }

    deleteNotebookEntry(id) {
        this.state.notebookEntries = this.state.notebookEntries.filter(e => e.id !== id);
        localStorage.setItem("matrix2_notebook", JSON.stringify(this.state.notebookEntries));
        this.notify();
    }

    saveResearchRecord(record) {
        record.id = "record_" + Date.now();
        record.timestamp = new Date().toISOString();
        this.state.researchRecords.unshift(record);
        localStorage.setItem("matrix2_research_records", JSON.stringify(this.state.researchRecords));
        this.notify();
    }

    loadResearchRecords() {
        try {
            const data = localStorage.getItem("matrix2_research_records");
            return data ? JSON.parse(data) : [];
        } catch (e) {
            return [];
        }
    }
}

window.dashboardState = new DashboardState();
