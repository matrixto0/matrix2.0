/**
 * MATRIX2.0 Research Dashboard - Knowledge Graph & Discovery Explorer View
 */

class KnowledgeView {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas ? this.canvas.getContext("2d") : null;
        this.graphData = { nodes: [], relationships: [] };
        this.selectedNode = null;
        this.panX = 0;
        this.panY = 0;
        this.zoom = 1.0;

        if (this.canvas) {
            this.initCanvasEvents();
        }
    }

    initCanvasEvents() {
        let isDragging = false;
        let startX, startY;

        this.canvas.addEventListener("mousedown", e => {
            isDragging = true;
            startX = e.clientX - this.panX;
            startY = e.clientY - this.panY;
        });

        this.canvas.addEventListener("mousemove", e => {
            if (isDragging) {
                this.panX = e.clientX - startX;
                this.panY = e.clientY - startY;
                this.render();
            }
        });

        this.canvas.addEventListener("mouseup", () => isDragging = false);
        this.canvas.addEventListener("mouseleave", () => isDragging = false);
    }

    setGraphData(data) {
        this.graphData = data || { nodes: [], relationships: [] };
        // Assign circular layout positions to nodes
        const nodes = this.graphData.nodes || [];
        const radius = 180;
        const centerX = (this.canvas ? this.canvas.width : 600) / 2;
        const centerY = (this.canvas ? this.canvas.height : 400) / 2;

        nodes.forEach((node, idx) => {
            const angle = (idx / (nodes.length || 1)) * Math.PI * 2;
            node.x = centerX + Math.cos(angle) * radius;
            node.y = centerY + Math.sin(angle) * radius;
        });

        this.render();
    }

    render() {
        if (!this.ctx) return;
        const ctx = this.ctx;
        const w = this.canvas.width;
        const h = this.canvas.height;

        ctx.clearRect(0, 0, w, h);
        ctx.save();
        ctx.translate(this.panX, this.panY);
        ctx.scale(this.zoom, this.zoom);

        const nodesMap = {};
        (this.graphData.nodes || []).forEach(n => nodesMap[n.id] = n);

        // Draw Relationships (Edges)
        ctx.strokeStyle = "#30363d";
        ctx.lineWidth = 1.5;
        (this.graphData.relationships || []).forEach(rel => {
            const src = nodesMap[rel.source_id];
            const tgt = nodesMap[rel.target_id];
            if (src && tgt) {
                ctx.beginPath();
                ctx.moveTo(src.x, src.y);
                ctx.lineTo(tgt.x, tgt.y);
                ctx.stroke();
            }
        });

        // Draw Nodes
        (this.graphData.nodes || []).forEach(node => {
            ctx.fillStyle = node.type === "concept" ? "#58a6ff" : node.type === "experiment" ? "#238636" : "#bc8cff";
            ctx.beginPath();
            ctx.arc(node.x, node.y, 14, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = "#c9d1d9";
            ctx.font = "11px monospace";
            ctx.fillText(node.name || node.id, node.x + 18, node.y + 4);
        });

        ctx.restore();
    }
}

window.KnowledgeView = KnowledgeView;
