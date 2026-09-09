/**
 * MATRIX2.0 Research Dashboard - Research Notebook Controller
 */

class NotebookController {
    constructor(state) {
        this.state = state;
    }

    createEntry(title, hypothesis, experiment, observation, interpretation, conclusion) {
        const entry = {
            title: title || "Untitled Note",
            hypothesis: hypothesis || "",
            experiment: experiment || "",
            observation: observation || "",
            interpretation: interpretation || "",
            conclusion: conclusion || "",
            warning: "Observations are model-dependent and should not be treated as established physical facts."
        };
        this.state.saveNotebookEntry(entry);
        return entry;
    }

    deleteEntry(id) {
        this.state.deleteNotebookEntry(id);
    }
}

window.NotebookController = NotebookController;
