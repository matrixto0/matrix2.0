"""
Serializer for converting KnowledgeGraph instances to JSON and dict structures.
"""

import json
from typing import Any, Dict
from knowledge.graph import KnowledgeGraph
from knowledge.node import Node
from knowledge.relationship import Relationship


class GraphSerializer:
    @staticmethod
    def to_dict(graph: KnowledgeGraph) -> Dict[str, Any]:
        return {
            "nodes": [node.to_dict() for node in graph.nodes.values()],
            "relationships": [rel.to_dict() for rel in graph.relationships]
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> KnowledgeGraph:
        graph = KnowledgeGraph()
        for node_data in data.get("nodes", []):
            graph.add_node(Node.from_dict(node_data))

        for rel_data in data.get("relationships", []):
            graph.add_relationship(Relationship.from_dict(rel_data))

        return graph

    @classmethod
    def to_json(cls, graph: KnowledgeGraph) -> str:
        return json.dumps(cls.to_dict(graph), indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> KnowledgeGraph:
        return cls.from_dict(json.loads(json_str))
