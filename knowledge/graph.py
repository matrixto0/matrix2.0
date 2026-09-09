"""
Graph structure and traversal logic for MATRIX2.0 Knowledge Graph.
"""

from typing import Dict, List, Optional
from knowledge.node import Node
from knowledge.relationship import Relationship


class KnowledgeGraph:
    """Manages nodes, relationships, and graph query traversals."""

    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.relationships: List[Relationship] = []

    def add_node(self, node: Node) -> Node:
        self.nodes[node.id] = node
        return node

    def get_node(self, node_id: str) -> Optional[Node]:
        return self.nodes.get(node_id)

    def add_relationship(self, rel: Relationship) -> Relationship:
        # Avoid duplicate identical relationships
        for existing in self.relationships:
            if (
                existing.source_id == rel.source_id
                and existing.target_id == rel.target_id
                and existing.type == rel.type
            ):
                return existing
        self.relationships.append(rel)
        return rel

    def get_relationships_for_node(self, node_id: str) -> List[Relationship]:
        return [
            rel for rel in self.relationships
            if rel.source_id == node_id or rel.target_id == node_id
        ]

    def get_neighbors(self, node_id: str) -> List[Node]:
        neighbor_ids = set()
        for rel in self.relationships:
            if rel.source_id == node_id:
                neighbor_ids.add(rel.target_id)
            elif rel.target_id == node_id:
                neighbor_ids.add(rel.source_id)

        return [self.nodes[nid] for nid in neighbor_ids if nid in self.nodes]
