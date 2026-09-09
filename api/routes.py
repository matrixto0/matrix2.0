"""
Routing and request handling logic for MATRIX2.0 Local Research API.
"""

import json
from urllib.parse import urlparse, parse_qs
from knowledge.registry import build_system_graph
from knowledge.query import QueryEngine
from knowledge.discovery import DiscoveryEngine
from knowledge.export import GraphExporter

SYSTEM_GRAPH = build_system_graph()
QUERY_ENGINE = QueryEngine(SYSTEM_GRAPH)
DISCOVERY_ENGINE = DiscoveryEngine()


def handle_api_request(path: str, method: str = "GET", body_data: dict = None) -> tuple[int, dict]:
    """Routes HTTP API request paths to structured JSON responses."""
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
        # Run discovery on sample runs
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
