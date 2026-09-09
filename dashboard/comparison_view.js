/**
 * MATRIX2.0 Research Dashboard - Experiment Comparison View
 */

class ComparisonView {
    constructor() {}

    compareResults(resultA, resultB) {
        if (!resultA || !resultB) return null;

        const paramDiffs = {};
        const keys = new Set([
            ...Object.keys(resultA.configuration || {}),
            ...Object.keys(resultB.configuration || {})
        ]);
        keys.forEach(k => {
            paramDiffs[k] = {
                expA: resultA.configuration[k],
                expB: resultB.configuration[k],
                diff: (resultB.configuration[k] || 0) - (resultA.configuration[k] || 0)
            };
        });

        const metricDiffs = {};
        const mKeys = new Set([
            ...Object.keys(resultA.measurements || {}),
            ...Object.keys(resultB.measurements || {})
        ]);
        mKeys.forEach(k => {
            const valA = resultA.measurements[k];
            const valB = resultB.measurements[k];
            const diff = (typeof valA === "number" && typeof valB === "number") ? valB - valA : "N/A";
            metricDiffs[k] = { expA: valA, expB: valB, diff: typeof diff === "number" ? parseFloat(diff.toFixed(4)) : diff };
        });

        return {
            expA_id: resultA.experiment_id,
            expB_id: resultB.experiment_id,
            paramDiffs,
            metricDiffs,
            disclaimer: "Comparison describes differences between model outputs; it does not establish physical causation."
        };
    }
}

window.ComparisonView = ComparisonView;
