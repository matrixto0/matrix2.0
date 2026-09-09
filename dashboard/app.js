/**
 * MATRIX2.0 Research Dashboard - Main Application Controller
 */

let vizView = null;
let expView = null;
let compView = null;
let metricsView = null;
let notebookCtrl = null;

document.addEventListener("DOMContentLoaded", () => {
    // Instantiate views
    vizView = new VisualizationView("waveCanvas", "particleCanvas");
    expView = new ExperimentView(window.dashboardState);
    compView = new ComparisonView();
    metricsView = new MetricsView("metricsCanvas");
    notebookCtrl = new NotebookController(window.dashboardState);

    // Load architecture layers from config
    fetch("data/dashboard_config.json")
        .then(res => res.json())
        .then(config => {
            renderArchitecture(config.architecture_layers);
        })
        .catch(err => {
            console.error("Config load error:", err);
        });

    // Subscribe to state updates
    window.dashboardState.subscribe(state => {
        renderStateControls(state.matrix);
        vizView.renderWave(state.matrix, state.simulation);
        vizView.renderParticles(state.matrix, state.particleConfig, state.simulation);
        renderExperimentsList(state.experiments);
        renderHistoryList(state.history);
        renderNotebookEntries(state.notebookEntries);
        updateComparisonDropdowns(state.history);
    });

    // Start render loop
    function loop() {
        if (window.dashboardState.state.simulation.running) {
            window.dashboardState.stepSimulation(0.02);
        } else {
            vizView.renderWave(window.dashboardState.state.matrix, window.dashboardState.state.simulation);
            vizView.renderParticles(window.dashboardState.state.matrix, window.dashboardState.state.particleConfig, window.dashboardState.state.simulation);
        }
        requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);

    // Initial render
    window.dashboardState.notify();
});

function switchTab(tabId) {
    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".tab-section").forEach(sec => sec.classList.remove("active"));

    const activeSec = document.getElementById(`tab-${tabId}`);
    if (activeSec) activeSec.classList.add("active");

    // Highlight button
    const activeBtn = Array.from(document.querySelectorAll(".tab-btn")).find(btn =>
        btn.getAttribute("onclick") && btn.getAttribute("onclick").includes(tabId)
    );
    if (activeBtn) activeBtn.classList.add("active");
}

function renderArchitecture(layers) {
    const container = document.getElementById("arch-flow");
    if (!container || !layers) return;
    container.innerHTML = "";

    layers.forEach((layer, idx) => {
        const step = document.createElement("div");
        step.className = "flow-step";
        step.innerHTML = `
            <div>
                <span class="flow-step-name">${layer.name}</span>
                <span class="flow-step-purpose"> — ${layer.purpose}</span>
            </div>
            <span class="badge-status">${layer.status}</span>
        `;
        container.appendChild(step);

        if (idx < layers.length - 1) {
            const arrow = document.createElement("div");
            arrow.className = "flow-arrow";
            arrow.innerHTML = "↓";
            container.appendChild(arrow);
        }
    });
}

function updateState(key, val) {
    window.dashboardState.updateMatrixState(key, val);
}

function renderStateControls(matrix) {
    ["x", "f", "I", "phi", "c", "v"].forEach(key => {
        const el = document.getElementById(`val-${key}`);
        if (el) el.innerText = parseFloat(matrix[key]).toFixed(2);
    });
}

function toggleSim() {
    const running = !window.dashboardState.state.simulation.running;
    window.dashboardState.setSimulationRunning(running);
    document.getElementById("btn-toggle-sim").innerText = running ? "Pause" : "Start";
}

function resetSim() {
    window.dashboardState.resetSimulation();
}

function updateParticleConfig(key, val) {
    window.dashboardState.state.particleConfig[key] = parseFloat(val);
    const el = document.getElementById(`val-${key === "count" ? "pcount" : key === "f_influence" ? "finf" : key === "I_influence" ? "Iinf" : "cinf"}`);
    if (el) el.innerText = parseFloat(val).toFixed(2);
    window.dashboardState.notify();
}

function renderExperimentsList(experiments) {
    const container = document.getElementById("experiments-list");
    if (!container) return;
    container.innerHTML = "";

    experiments.forEach(exp => {
        const card = document.createElement("div");
        card.className = "flow-step";
        card.style.marginBottom = "0.75rem";
        card.innerHTML = `
            <div>
                <div style="font-weight: 600; color: var(--accent-blue);">${exp.name} (${exp.id})</div>
                <div style="font-size: 0.85rem; color: var(--text-muted);">${exp.question}</div>
                <div style="font-size: 0.8rem; font-family: var(--font-mono); margin-top: 0.25rem;">
                    Seed: ${exp.seed} | Iterations: ${exp.iterations} | Params: ${JSON.stringify(exp.parameters)}
                </div>
            </div>
            <button class="btn" onclick="runExperimentById('${exp.id}')">Run</button>
        `;
        container.appendChild(card);
    });
}

function runExperimentById(id) {
    const exp = window.dashboardState.state.experiments.find(e => e.id === id);
    if (!exp) return;
    const result = expView.runExperiment(exp);

    // Render result card
    const resultCard = document.getElementById("experiment-result-card");
    const details = document.getElementById("result-details");
    resultCard.style.display = "block";

    details.innerHTML = `
        <table class="data-table">
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Total Steps</td><td>${result.measurements.total_steps}</td></tr>
            <tr><td>Mean Energy</td><td>${result.measurements.mean_energy}</td></tr>
            <tr><td>Max Energy</td><td>${result.measurements.max_energy}</td></tr>
            <tr><td>Min Energy</td><td>${result.measurements.min_energy}</td></tr>
            <tr><td>Energy Std Dev</td><td>${result.measurements.std_energy}</td></tr>
            <tr><td>Mean Entropy</td><td>${result.measurements.mean_entropy}</td></tr>
        </table>
        <div style="margin-top: 1rem; font-size: 0.85rem; color: var(--text-muted);">
            <strong>Interpretation:</strong> ${result.interpretation}
        </div>
    `;

    // Render metrics line chart
    metricsView.renderLineChart(result.trajectory, "energy");
}

function exportCurrentResultJSON() {
    const res = window.dashboardState.state.currentExperimentResult;
    if (!res) return;
    const blob = new Blob([JSON.stringify(res, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${res.experiment_id}_result.json`;
    a.click();
}

function openCreateResearchRecordModal() {
    document.getElementById("research-record-form").style.display = "block";
}

function submitResearchRecord() {
    const res = window.dashboardState.state.currentExperimentResult;
    if (!res) return;

    const record = {
        hypothesis: document.getElementById("rr-hypothesis").value || "Default hypothesis",
        experiment_id: res.experiment_id,
        configuration: res.configuration,
        seed: res.seed,
        observations: res.trajectory.slice(0, 5), // Sample
        metrics: res.measurements,
        interpretation: document.getElementById("rr-interpretation").value || res.interpretation,
        conclusion: document.getElementById("rr-conclusion").value || "Hypothesis evaluated against model."
    };

    window.dashboardState.saveResearchRecord(record);
    alert("Research record saved locally!");
    document.getElementById("research-record-form").style.display = "none";
}

function updateComparisonDropdowns(history) {
    const selA = document.getElementById("select-exp-a");
    const selB = document.getElementById("select-exp-b");
    if (!selA || !selB) return;

    const currentA = selA.value;
    const currentB = selB.value;

    selA.innerHTML = '<option value="">-- Select Experiment A --</option>';
    selB.innerHTML = '<option value="">-- Select Experiment B --</option>';

    history.forEach((item, idx) => {
        const label = `${item.name} (${item.timestamp.slice(11, 19)})`;
        selA.innerHTML += `<option value="${idx}">${label}</option>`;
        selB.innerHTML += `<option value="${idx}">${label}</option>`;
    });

    if (currentA) selA.value = currentA;
    if (currentB) selB.value = currentB;
}

function runComparison() {
    const idxA = document.getElementById("select-exp-a").value;
    const idxB = document.getElementById("select-exp-b").value;
    const container = document.getElementById("comparison-output");
    if (!container) return;

    if (idxA === "" || idxB === "") {
        container.innerHTML = '<p style="color: var(--text-muted);">Please select two experiment runs from history.</p>';
        return;
    }

    const expA = window.dashboardState.state.history[idxA];
    const expB = window.dashboardState.state.history[idxB];

    const diffData = compView.compareResults(expA, expB);

    let html = `
        <table class="data-table">
            <thead>
                <tr><th>Metric / Parameter</th><th>Exp A (${expA.experiment_id})</th><th>Exp B (${expB.experiment_id})</th><th>Difference (B - A)</th></tr>
            </thead>
            <tbody>
    `;

    Object.entries(diffData.metricDiffs).forEach(([k, v]) => {
        html += `<tr><td><strong>${k}</strong></td><td>${v.expA}</td><td>${v.expB}</td><td>${v.diff}</td></tr>`;
    });

    html += `</tbody></table>`;
    container.innerHTML = html;
}

function renderHistoryList(history) {
    const container = document.getElementById("history-list");
    if (!container) return;
    if (history.length === 0) {
        container.innerHTML = '<p style="color: var(--text-muted);">No recorded history yet.</p>';
        return;
    }

    container.innerHTML = "";
    history.forEach((res, idx) => {
        const card = document.createElement("div");
        card.className = "flow-step";
        card.style.marginBottom = "0.5rem";
        card.innerHTML = `
            <div>
                <strong>${res.name}</strong> (${res.experiment_id})
                <div style="font-size: 0.8rem; color: var(--text-muted);">${res.timestamp} | Seed: ${res.seed} | Iterations: ${res.iterations}</div>
            </div>
            <div style="font-family: var(--font-mono); font-size: 0.85rem;">
                Mean Energy: ${res.measurements.mean_energy}
            </div>
        `;
        container.appendChild(card);
    });
}

function clearHistory() {
    if (confirm("Clear all experiment history?")) {
        window.dashboardState.clearHistory();
    }
}

function saveNotebookNote() {
    const title = document.getElementById("note-title").value;
    const hypothesis = document.getElementById("note-hypothesis").value;
    const experiment = document.getElementById("note-experiment").value;
    const observation = document.getElementById("note-observation").value;
    const interpretation = document.getElementById("note-interpretation").value;
    const conclusion = document.getElementById("note-conclusion").value;

    notebookCtrl.createEntry(title, hypothesis, experiment, observation, interpretation, conclusion);

    // Reset inputs
    document.getElementById("note-title").value = "";
    document.getElementById("note-hypothesis").value = "";
    document.getElementById("note-experiment").value = "";
    document.getElementById("note-observation").value = "";
    document.getElementById("note-interpretation").value = "";
    document.getElementById("note-conclusion").value = "";

    alert("Note saved!");
}

function renderNotebookEntries(entries) {
    const container = document.getElementById("notebook-entries-list");
    if (!container) return;
    if (entries.length === 0) {
        container.innerHTML = '<p style="color: var(--text-muted);">No notebook entries yet.</p>';
        return;
    }

    container.innerHTML = "";
    entries.forEach(entry => {
        const card = document.createElement("div");
        card.className = "panel-card";
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>${entry.title}</h4>
                <button class="btn btn-danger" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;" onclick="notebookCtrl.deleteEntry('${entry.id}')">Delete</button>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.5rem;">${entry.timestamp}</div>
            <p><strong>Hypothesis:</strong> ${entry.hypothesis || "N/A"}</p>
            <p><strong>Observation:</strong> ${entry.observation || "N/A"}</p>
            <p><strong>Interpretation:</strong> ${entry.interpretation || "N/A"}</p>
            <p><strong>Conclusion:</strong> ${entry.conclusion || "N/A"}</p>
        `;
        container.appendChild(card);
    });
}
