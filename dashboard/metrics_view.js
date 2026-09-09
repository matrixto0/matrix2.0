/**
 * MATRIX2.0 Research Dashboard - Metrics Canvas Visualizations
 */

class MetricsView {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas ? this.canvas.getContext("2d") : null;
    }

    renderLineChart(trajectory, key = "energy") {
        if (!this.ctx || !trajectory || trajectory.length === 0) return;
        const ctx = this.ctx;
        const w = this.canvas.width;
        const h = this.canvas.height;
        ctx.clearRect(0, 0, w, h);

        const values = trajectory.map(t => t[key] || 0);
        const maxVal = Math.max(...values, 0.001);
        const minVal = Math.min(...values, 0);

        // Draw axes
        ctx.strokeStyle = "#30363d";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(40, 20);
        ctx.lineTo(40, h - 30);
        ctx.lineTo(w - 20, h - 30);
        ctx.stroke();

        // Draw line
        ctx.strokeStyle = "#58a6ff";
        ctx.lineWidth = 2;
        ctx.beginPath();

        const chartWidth = w - 60;
        const chartHeight = h - 50;

        values.forEach((v, i) => {
            const x = 40 + (i / (values.length - 1)) * chartWidth;
            const normY = (v - minVal) / (maxVal - minVal || 1);
            const y = (h - 30) - normY * chartHeight;
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        });
        ctx.stroke();

        // Labels
        ctx.fillStyle = "#8b949e";
        ctx.font = "11px monospace";
        ctx.fillText(`Trajectory Line Chart: ${key}`, 50, 20);
        ctx.fillText(`Max: ${maxVal.toFixed(3)}`, w - 100, 20);
        ctx.fillText(`Min: ${minVal.toFixed(3)}`, w - 100, h - 10);
    }

    renderBarChart(metrics) {
        if (!this.ctx || !metrics) return;
        const ctx = this.ctx;
        const w = this.canvas.width;
        const h = this.canvas.height;
        ctx.clearRect(0, 0, w, h);

        const entries = Object.entries(metrics).filter(([_, v]) => typeof v === "number");
        if (entries.length === 0) return;

        const maxVal = Math.max(...entries.map(([_, v]) => v), 0.001);
        const barWidth = (w - 80) / entries.length;

        entries.forEach(([key, val], idx) => {
            const x = 50 + idx * barWidth + 10;
            const barH = (val / maxVal) * (h - 60);
            const y = (h - 30) - barH;

            ctx.fillStyle = "#238636";
            ctx.fillRect(x, y, barWidth - 20, barH);

            ctx.fillStyle = "#c9d1d9";
            ctx.font = "10px monospace";
            ctx.fillText(key.slice(0, 8), x, h - 10);
            ctx.fillText(val.toFixed(2), x, y - 5);
        });
    }
}

window.MetricsView = MetricsView;
