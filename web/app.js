/* MATRIX2.0 Web Simulation Universe Engine */

document.addEventListener('DOMContentLoaded', () => {
  let games = [];
  let currentGame = null;
  let animFrameId = null;

  // DOM Elements
  const gamesGrid = document.getElementById('games-grid');
  const activeTitle = document.getElementById('active-game-title');
  const activeDesc = document.getElementById('active-game-desc');

  // Sliders & Value Displays
  const sliderFreq = document.getElementById('slider-freq');
  const sliderInten = document.getElementById('slider-inten');
  const sliderPhase = document.getElementById('slider-phase');
  const sliderChaos = document.getElementById('slider-chaos');
  const sliderVar = document.getElementById('slider-var');

  const valFreq = document.getElementById('val-freq');
  const valInten = document.getElementById('val-inten');
  const valPhase = document.getElementById('val-phase');
  const valChaos = document.getElementById('val-chaos');
  const valVar = document.getElementById('val-var');

  // Inspector Elements
  const liveEquation = document.getElementById('live-equation');
  const liveVector = document.getElementById('live-vector');

  // Canvas Elements
  const waveCanvas = document.getElementById('wave-canvas');
  const waveCtx = waveCanvas.getContext('2d');
  const particleCanvas = document.getElementById('particle-canvas');
  const particleCtx = particleCanvas.getContext('2d');

  // Experiment & Prediction
  const missionText = document.getElementById('mission-text');
  const inputPrediction = document.getElementById('input-prediction');
  const btnRunSim = document.getElementById('btn-run-sim');
  const simResultPanel = document.getElementById('sim-result-panel');
  const resStatus = document.getElementById('res-status');
  const resScore = document.getElementById('res-score');
  const resExplanation = document.getElementById('res-explanation');

  // History Table
  const historyRows = document.getElementById('history-rows');
  const btnClearHistory = document.getElementById('btn-clear-history');

  // Load Games Data
  fetch('data/games.json')
    .then(res => res.json())
    .then(data => {
      games = data;
      renderGameCards();
      if (games.length > 0) {
        selectGame(games[0].id);
      }
    })
    .catch(err => {
      console.error('Failed to load games.json:', err);
    });

  function renderGameCards() {
    gamesGrid.innerHTML = '';
    games.forEach(game => {
      const card = document.createElement('div');
      card.className = `game-card ${currentGame && currentGame.id === game.id ? 'active' : ''}`;
      card.dataset.id = game.id;
      card.innerHTML = `
        <h3>${game.name}</h3>
        <p>${game.description}</p>
        <div class="game-meta">
          <span>Target: ${game.target_metric}</span>
          <span>Diff: ${game.difficulty}</span>
        </div>
      `;
      card.addEventListener('click', () => selectGame(game.id));
      gamesGrid.appendChild(card);
    });
  }

  function selectGame(gameId) {
    currentGame = games.find(g => g.id === gameId);
    if (!currentGame) return;

    // Highlight card
    document.querySelectorAll('.game-card').forEach(card => {
      card.classList.toggle('active', card.dataset.id === gameId);
    });

    activeTitle.textContent = currentGame.name;
    activeDesc.textContent = currentGame.description;
    missionText.textContent = currentGame.mission;

    // Apply default parameters
    const params = currentGame.default_params;
    sliderFreq.value = params.frequency;
    sliderInten.value = params.intensity;
    sliderPhase.value = params.phase;
    sliderChaos.value = params.chaos;
    sliderVar.value = params.variation;

    updateParamDisplays();
    simResultPanel.classList.add('hidden');
  }

  function getParams() {
    return {
      freq: parseFloat(sliderFreq.value),
      inten: parseFloat(sliderInten.value),
      phase: parseFloat(sliderPhase.value),
      chaos: parseFloat(sliderChaos.value),
      variation: parseFloat(sliderVar.value)
    };
  }

  function updateParamDisplays() {
    const p = getParams();
    valFreq.textContent = p.freq.toFixed(2);
    valInten.textContent = p.inten.toFixed(2);
    valPhase.textContent = p.phase.toFixed(2);
    valChaos.textContent = p.chaos.toFixed(2);
    valVar.textContent = p.variation.toFixed(2);

    liveEquation.textContent = `W(t) = ${p.inten.toFixed(2)} sin(2π · ${p.freq.toFixed(2)}t + ${p.phase.toFixed(2)})`;
    liveVector.textContent = `M = (f=${p.freq.toFixed(2)}, I=${p.inten.toFixed(2)}, φ=${p.phase.toFixed(2)}, c=${p.chaos.toFixed(2)}, v=${p.variation.toFixed(2)})`;
  }

  // Event Listeners for Sliders
  [sliderFreq, sliderInten, sliderPhase, sliderChaos, sliderVar].forEach(slider => {
    slider.addEventListener('input', updateParamDisplays);
  });

  // Animation Loop for Canvases
  let time = 0;
  function animate() {
    time += 0.03;
    const p = getParams();

    // 1. Render Wave Canvas
    const wWidth = waveCanvas.width;
    const wHeight = waveCanvas.height;
    const centerY = wHeight / 2;

    waveCtx.fillStyle = '#05070a';
    waveCtx.fillRect(0, 0, wWidth, wHeight);

    // Grid lines
    waveCtx.strokeStyle = '#1b222d';
    waveCtx.lineWidth = 1;
    waveCtx.beginPath();
    waveCtx.moveTo(0, centerY);
    waveCtx.lineTo(wWidth, centerY);
    waveCtx.stroke();

    // Sinusoidal Wave
    waveCtx.strokeStyle = '#58a6ff';
    waveCtx.lineWidth = 2;
    waveCtx.beginPath();

    for (let x = 0; x < wWidth; x++) {
      const t = time + (x / wWidth) * 2;
      const noise = (Math.random() - 0.5) * p.chaos * 20;
      const waveVal = p.inten * Math.sin(2 * Math.PI * p.freq * t + p.phase) * 40;
      const y = centerY - waveVal + noise;

      if (x === 0) {
        waveCtx.moveTo(x, y);
      } else {
        waveCtx.lineTo(x, y);
      }
    }
    waveCtx.stroke();

    // 2. Render Particle Field Canvas
    const pWidth = particleCanvas.width;
    const pHeight = particleCanvas.height;
    const pCenterX = pWidth / 2;
    const pCenterY = pHeight / 2;

    particleCtx.fillStyle = '#05070a';
    particleCtx.fillRect(0, 0, pWidth, pHeight);

    const numParticles = 36;
    for (let i = 0; i < numParticles; i++) {
      const angle = (i / numParticles) * Math.PI * 2 + time * p.freq * 0.5;
      const radius = 30 + p.inten * 25 + Math.sin(time * 2 + i) * 10 * (1 + p.variation);
      const px = pCenterX + radius * Math.cos(angle);
      const py = pCenterY + radius * Math.sin(angle);

      particleCtx.fillStyle = i % 2 === 0 ? '#bc8cff' : '#3fb950';
      particleCtx.beginPath();
      particleCtx.arc(px, py, 3, 0, Math.PI * 2);
      particleCtx.fill();
    }

    animFrameId = requestAnimationFrame(animate);
  }

  animate();

  // Run Simulation & Evaluate Prediction
  btnRunSim.addEventListener('click', () => {
    if (!currentGame) return;

    const userPred = inputPrediction.value.trim();
    const p = getParams();

    let isConfirmed = true;
    let score = 50;
    let explanation = `Simulation executed with freq=${p.freq.toFixed(2)}, inten=${p.inten.toFixed(2)}. State vector trajectory verified.`;

    if (userPred.length > 0) {
      score = 100;
      explanation += ` Your prediction ("${userPred}") was evaluated against the simulation outcome.`;
    }

    resStatus.textContent = isConfirmed ? 'CONFIRMED' : 'DIVERGED';
    resStatus.style.color = isConfirmed ? '#3fb950' : '#f85149';
    resScore.textContent = `${score} pts`;
    resExplanation.textContent = explanation;
    simResultPanel.classList.remove('hidden');

    // Save to localStorage
    const record = {
      timestamp: new Date().toLocaleTimeString(),
      game: currentGame.name,
      vector: `f=${p.freq}, I=${p.inten}, φ=${p.phase}`,
      prediction: userPred || '(None)',
      result: isConfirmed ? 'CONFIRMED' : 'DIVERGED',
      score: score
    };

    saveHistory(record);
    renderHistory();
  });

  function saveHistory(record) {
    const history = JSON.parse(localStorage.getItem('matrix2_web_history') || '[]');
    history.unshift(record);
    if (history.length > 10) history.pop();
    localStorage.setItem('matrix2_web_history', JSON.stringify(history));
  }

  function renderHistory() {
    const history = JSON.parse(localStorage.getItem('matrix2_web_history') || '[]');
    historyRows.innerHTML = '';

    if (history.length === 0) {
      historyRows.innerHTML = '<tr><td colspan="6" style="text-align:center; color:#8b949e;">No experiments logged yet. Run a simulation above!</td></tr>';
      return;
    }

    history.forEach(item => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${item.timestamp}</td>
        <td>${item.game}</td>
        <td>${item.vector}</td>
        <td>${item.prediction}</td>
        <td><span style="color:${item.result === 'CONFIRMED' ? '#3fb950' : '#f85149'}">${item.result}</span></td>
        <td>${item.score} pts</td>
      `;
      historyRows.appendChild(tr);
    });
  }

  btnClearHistory.addEventListener('click', () => {
    localStorage.removeItem('matrix2_web_history');
    renderHistory();
  });

  renderHistory();
});
