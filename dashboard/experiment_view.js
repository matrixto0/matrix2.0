/**
 * MATRIX2.0 Research Dashboard - Experiment Launcher & Execution Engine
 */

class ExperimentView {
    constructor(state) {
        this.state = state;
    }

    /**
     * Executes an experiment deterministically in JavaScript matching Python experiment engine.
     */
    runExperiment(experiment) {
        const { id, name, question, parameters, seed, iterations } = experiment;
        const { f, I, phi, c, v } = parameters;

        // Simple PRNG using seed
        let currentSeed = seed;
        const pseudoRandom = () => {
            currentSeed = (currentSeed * 9301 + 49297) % 233280;
            return currentSeed / 233280;
        };

        const trajectory = [];
        let totalEnergy = 0;
        let totalEntropy = 0;
        let maxEnergy = -Infinity;
        let minEnergy = Infinity;

        for (let step = 0; step < iterations; step++) {
            const t = step * 0.05;
            const noise = (pseudoRandom() - 0.5) * c;
            const waveVal = I * Math.sin(2 * Math.PI * f * t + phi) + noise;
            const energy = waveVal * waveVal;
            const entropy = Math.abs(noise * v);

            trajectory.push({ step, t, waveVal, energy, entropy });

            totalEnergy += energy;
            totalEntropy += entropy;
            if (energy > maxEnergy) maxEnergy = energy;
            if (energy < minEnergy) minEnergy = energy;
        }

        const meanEnergy = totalEnergy / iterations;
        const meanEntropy = totalEntropy / iterations;

        // Compute variance of energy
        const varEnergy = trajectory.reduce((acc, p) => acc + Math.pow(p.energy - meanEnergy, 2), 0) / iterations;
        const stdEnergy = Math.sqrt(varEnergy);

        const result = {
            experiment_id: id,
            name: name,
            question: question,
            timestamp: new Date().toISOString(),
            seed: seed,
            iterations: iterations,
            configuration: parameters,
            measurements: {
                total_steps: iterations,
                mean_energy: parseFloat(meanEnergy.toFixed(4)),
                max_energy: parseFloat(maxEnergy.toFixed(4)),
                min_energy: parseFloat(minEnergy.toFixed(4)),
                std_energy: parseFloat(stdEnergy.toFixed(4)),
                mean_entropy: parseFloat(meanEntropy.toFixed(4))
            },
            trajectory: trajectory,
            interpretation: `Computational model output generated over ${iterations} steps with seed ${seed}. State variance std=${stdEnergy.toFixed(4)}.`
        };

        this.state.saveExperimentToHistory(result);
        this.state.state.currentExperimentResult = result;
        this.state.notify();
        return result;
    }
}

window.ExperimentView = ExperimentView;
