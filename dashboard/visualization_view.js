/**
 * MATRIX2.0 Research Dashboard - Live Wave & Computational Particle Renderers
 */

class VisualizationView {
    constructor(waveCanvasId, particleCanvasId) {
        this.waveCanvas = document.getElementById(waveCanvasId);
        this.particleCanvas = document.getElementById(particleCanvasId);
        this.waveCtx = this.waveCanvas ? this.waveCanvas.getContext("2d") : null;
        this.particleCtx = this.particleCanvas ? this.particleCanvas.getContext("2d") : null;

        this.particles = [];
        this.initParticles(50);
    }

    initParticles(count) {
        this.particles = [];
        for (let i = 0; i < count; i++) {
            this.particles.push({
                x: Math.random(),
                y: Math.random(),
                vx: (Math.random() - 0.5) * 0.01,
                vy: (Math.random() - 0.5) * 0.01,
                phase: Math.random() * Math.PI * 2
            });
        }
    }

    renderWave(matrixState, simState) {
        if (!this.waveCtx) return;
        const ctx = this.waveCtx;
        const width = this.waveCanvas.width;
        const height = this.waveCanvas.height;
        const midY = height / 2;

        ctx.clearRect(0, 0, width, height);

        // Grid lines
        ctx.strokeStyle = "#1f293d";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, midY);
        ctx.lineTo(width, midY);
        ctx.stroke();

        // Wave: W(t) = I * sin(2*pi*f*t + phi)
        ctx.strokeStyle = "#58a6ff";
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        const t = simState.t;
        const { f, I, phi, c, v } = matrixState;

        for (let x = 0; x < width; x++) {
            const relX = x / width; // 0 to 1
            const spatialT = t + relX * 2.0;
            // Deterministic chaos perturbation if enabled
            const noise = (c > 0 || v > 0) ? Math.sin(x * 0.05 + t * 5.0) * c * 0.2 : 0;
            const waveVal = I * Math.sin(2 * Math.PI * f * spatialT + phi) + noise;

            // Map wave value to canvas Y (scale I)
            const y = midY - (waveVal / 5.0) * (height * 0.4);
            if (x === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Info overlay
        ctx.fillStyle = "#8b949e";
        ctx.font = "12px monospace";
        ctx.fillText(`W(t) = ${I.toFixed(2)} sin(2π * ${f.toFixed(2)}t + ${phi.toFixed(2)})`, 10, 20);
        ctx.fillText(`t = ${t.toFixed(2)}s | Baseline = 0.00`, 10, 38);
    }

    renderParticles(matrixState, particleConfig, simState) {
        if (!this.particleCtx) return;
        const ctx = this.particleCtx;
        const width = this.particleCanvas.width;
        const height = this.particleCanvas.height;

        ctx.clearRect(0, 0, width, height);

        // Ensure particle count matches config
        if (this.particles.length !== particleConfig.count) {
            this.initParticles(particleConfig.count);
        }

        const { f, I, c } = matrixState;
        const f_inf = particleConfig.f_influence;
        const I_inf = particleConfig.I_influence;
        const c_inf = particleConfig.c_influence;

        ctx.fillStyle = "#238636";
        this.particles.forEach((p, idx) => {
            // Update particle velocity based on state
            const speedMultiplier = 0.002 * (1 + f * f_inf * 0.5);
            const chaosFactor = (c * c_inf) * (Math.sin(idx + simState.t * 3) * 0.01);

            p.x += p.vx * speedMultiplier + chaosFactor;
            p.y += p.vy * speedMultiplier + chaosFactor;

            // Wrap around boundaries
            if (p.x < 0) p.x = 1;
            if (p.x > 1) p.x = 0;
            if (p.y < 0) p.y = 1;
            if (p.y > 1) p.y = 0;

            const radius = 3 + I * I_inf * 2;
            const px = p.x * width;
            const py = p.y * height;

            ctx.beginPath();
            ctx.arc(px, py, radius, 0, Math.PI * 2);
            ctx.fill();
        });

        // Label
        ctx.fillStyle = "#8b949e";
        ctx.font = "11px monospace";
        ctx.fillText("Computational particle visualization", 10, height - 10);
    }
}

window.VisualizationView = VisualizationView;
