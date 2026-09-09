"""
Query engine for MATRIX2.0 Knowledge Graph.
"""

from typing import Any, List, Optional
from knowledge.graph import KnowledgeGraph
from knowledge.node import Node
from knowledge.relationship import Relationship


class QueryEngine:
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def find_node_by_id(self, node_id: str) -> Optional[Node]:
        return self.graph.get_node(node_id)

    def find_nodes_by_type(self, node_type: str) -> List[Node]:
        return [n for n in self.graph.nodes.values() if n.type == node_type]

    def find_relationships_by_type(self, rel_type: str) -> List[Relationship]:
        return [r for r in self.graph.relationships if r.type == rel_type]

    def find_experiments_using_parameter(self, param_name: str) -> List[Node]:
        exp_nodes = self.find_nodes_by_type("experiment")
        matching = []
        for exp in exp_nodes:
            params = exp.metadata.get("parameters", {})
            if param_name in params:
                matching.append(exp)
        return matching

    def find_metrics_for_experiment(self, experiment_id: str) -> List[Node]:
        rels = self.graph.get_relationships_for_node(experiment_id)
        metric_nodes = []
        for r in rels:
            if r.source_id == experiment_id and r.type in ("GENERATES", "MEASURES"):
                target = self.graph.get_node(r.target_id)
                if target and target.type in ("metric", "result"):
                    metric_nodes.append(target)
        return metric_nodes

    def find_visualizations_for_result(self, result_id: str) -> List[Node]:
        rels = self.graph.get_relationships_for_node(result_id)
        viz_nodes = []
        for r in rels:
            if r.type == "VISUALIZES" and (r.target_id == result_id or r.source_id == result_id):
                other_id = r.source_id if r.target_id == result_id else r.target_id
                target = self.graph.get_node(other_id)
                if target and target.type == "visualization":
                    viz_nodes.append(target)
        return viz_nodes
