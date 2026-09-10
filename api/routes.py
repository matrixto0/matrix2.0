"""
Routing and request handling logic for MATRIX2.0 Local Research API.
"""

import json
from urllib.parse import urlparse, parse_qs
from matrix_core import MatrixState
from matrix_dynamics import step, evolve
from knowledge.registry import build_system_graph
from knowledge.query import QueryEngine
from knowledge.discovery import DiscoveryEngine
from knowledge.export import GraphExporter

SYSTEM_GRAPH = build_system_graph()
QUERY_ENGINE = QueryEngine(SYSTEM_GRAPH)
DISCOVERY_ENGINE = DiscoveryEngine()

CURRENT_STATE = MatrixState(value=1.0, frequency=1.0, intensity=1.0, phase=0.0, chaos=0.1, variation=0.1)


def handle_api_request(path: str, method: str = "GET", body_data: dict = None) -> tuple[int, dict]:
    """Routes HTTP API request paths to structured JSON responses."""
    global CURRENT_STATE
    parsed_url = urlparse(path)
    clean_path = parsed_url.path.rstrip("/")

    # GET /api/health
    if clean_path in ("/api/health", "/health"):
        return 200, {
            "status": "ok",
            "name": "MATRIX2.0 Research API",
            "version": "2.0.0",
            "components": {
                "core": True,
                "experiments": True,
                "knowledge_graph": True,
                "discovery_engine": True
            }
        }

    # GET /api/state
    if clean_path in ("/api/state", "/state") and method == "GET":
        return 200, {"state": CURRENT_STATE.to_dict()}

    # POST /api/state
    if clean_path in ("/api/state", "/state") and method == "POST":
        if not body_data:
            return 400, {"error": "Missing body payload"}
        try:
            CURRENT_STATE = MatrixState.from_dict(body_data)
            return 200, {"status": "updated", "state": CURRENT_STATE.to_dict()}
        except Exception as e:
            return 400, {"error": f"Invalid state payload: {str(e)}"}

    # GET /api/experiments
    if clean_path in ("/api/experiments", "/experiments") and method == "GET":
        experiments = [
            {"id": "exp_001_phase_stability", "name": "Phase Stability Under Variation", "seed": 42},
            {"id": "exp_002_chaos_transition", "name": "Chaos Perturbation Transition", "seed": 123}
        ]
        return 200, {"experiments": experiments, "count": len(experiments)}

    # POST /api/experiments/{id}/run
    if clean_path.startswith("/api/experiments/") and clean_path.endswith("/run") and method == "POST":
        exp_id = clean_path.split("/")[-2]
        trajectory = evolve(CURRENT_STATE, steps=10)
        return 200, {
            "experiment_id": exp_id,
            "seed": 42,
            "steps": len(trajectory),
            "measurements": {"mean_value": CURRENT_STATE.value, "mean_energy": CURRENT_STATE.intensity ** 2}
        }

    # GET /api/games
    if clean_path in ("/api/games", "/games") and method == "GET":
        games = [
            {"id": "game_phase_shift", "title": "Phase Shift Predictor", "genre": "Predictive Dynamics"}
        ]
        return 200, {"games": games, "count": len(games)}

    # GET /api/metrics
    if clean_path in ("/api/metrics", "/metrics") and method == "GET":
        return 200, {"metrics": {"system_load": 0.05, "active_nodes": len(SYSTEM_GRAPH.nodes)}}

    # GET /api/knowledge/nodes
    if clean_path in ("/api/knowledge/nodes", "/knowledge/nodes"):
        nodes = [n.to_dict() for n in SYSTEM_GRAPH.nodes.values()]
        return 200, {"nodes": nodes, "count": len(nodes)}

    # GET /api/knowledge/nodes/{id}
    if clean_path.startswith("/api/knowledge/nodes/"):
        node_id = clean_path.split("/")[-1]
        node = QUERY_ENGINE.find_node_by_id(node_id)
        if node:
            return 200, {"node": node.to_dict()}
        return 404, {"error": "Node not found", "id": node_id}

    # GET /api/knowledge/relationships
    if clean_path in ("/api/knowledge/relationships", "/knowledge/relationships"):
        rels = [r.to_dict() for r in SYSTEM_GRAPH.relationships]
        return 200, {"relationships": rels, "count": len(rels)}

    # GET /api/knowledge/neighbors/{id}
    if clean_path.startswith("/api/knowledge/neighbors/"):
        node_id = clean_path.split("/")[-1]
        neighbors = SYSTEM_GRAPH.get_neighbors(node_id)
        return 200, {"node_id": node_id, "neighbors": [n.to_dict() for n in neighbors]}

    # GET /api/knowledge/discoveries
    if clean_path in ("/api/knowledge/discoveries", "/knowledge/discoveries"):
        sample_results = [
            {"experiment_id": "exp_1", "seed": 42, "configuration": {"f": 1.0}, "measurements": {"mean_energy": 1.0}},
            {"experiment_id": "exp_2", "seed": 42, "configuration": {"f": 2.0}, "measurements": {"mean_energy": 4.0}}
        ]
        discoveries = DISCOVERY_ENGINE.analyze_experiment_results(sample_results)
        return 200, {"discoveries": [d.to_dict() for d in discoveries]}

    # GET /api/knowledge/export
    if clean_path in ("/api/knowledge/export", "/knowledge/export"):
        export_data = GraphExporter.export_json(SYSTEM_GRAPH)
        return 200, json.loads(export_data)

    return 404, {"error": "Endpoint not found", "path": path}
