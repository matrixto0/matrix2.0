"""
Unit tests for MATRIX2.0 Knowledge Graph, Query Engine, Discovery Engine, and Exporter.
"""

import unittest
import json
from knowledge.node import Node
from knowledge.relationship import Relationship
from knowledge.provenance import Provenance
from knowledge.graph import KnowledgeGraph
from knowledge.query import QueryEngine
from knowledge.serializer import GraphSerializer
from knowledge.registry import build_system_graph
from knowledge.discovery import DiscoveryEngine
from knowledge.export import GraphExporter


class TestKnowledgeGraph(unittest.TestCase):

    def test_node_creation_and_validation(self):
        node = Node("exp_001", "experiment", "Phase Stability", "Description")
        self.assertEqual(node.id, "exp_001")
        self.assertEqual(node.type, "experiment")

        with self.assertRaises(ValueError):
            Node("bad_id", "invalid_type", "Bad Node")

    def test_relationship_creation_and_validation(self):
        rel = Relationship("exp_001", "param_f", "USES_PARAMETER")
        self.assertEqual(rel.source_id, "exp_001")
        self.assertEqual(rel.type, "USES_PARAMETER")

        with self.assertRaises(ValueError):
            Relationship("a", "b", "INVALID_REL")

    def test_graph_add_and_neighbors(self):
        graph = KnowledgeGraph()
        n1 = Node("n1", "concept", "Node 1")
        n2 = Node("n2", "parameter", "Node 2")
        graph.add_node(n1)
        graph.add_node(n2)

        rel = Relationship("n1", "n2", "PRODUCES")
        graph.add_relationship(rel)

        # Duplicate rel should be ignored
        graph.add_relationship(rel)
        self.assertEqual(len(graph.relationships), 1)

        neighbors = graph.get_neighbors("n1")
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0].id, "n2")

    def test_system_graph_and_queries(self):
        graph = build_system_graph()
        self.assertGreater(len(graph.nodes), 10)
        self.assertGreater(len(graph.relationships), 5)

        query = QueryEngine(graph)
        core_node = query.find_node_by_id("component_core")
        self.assertIsNotNone(core_node)
        self.assertEqual(core_node.name, "Mathematical Core")

        concepts = query.find_nodes_by_type("concept")
        self.assertGreaterEqual(len(concepts), 10)

    def test_discovery_engine(self):
        results = [
            {"experiment_id": "exp_1", "seed": 42, "configuration": {"f": 1.0}, "measurements": {"mean_energy": 1.0}},
            {"experiment_id": "exp_2", "seed": 42, "configuration": {"f": 2.0}, "measurements": {"mean_energy": 4.0}},
            {"experiment_id": "exp_3", "seed": 42, "configuration": {"f": 3.0}, "measurements": {"mean_energy": 9.0}}
        ]

        engine = DiscoveryEngine()
        discoveries = engine.analyze_experiment_results(results)
        self.assertEqual(len(discoveries), 1)

        disc = discoveries[0]
        self.assertEqual(disc.id, "disc_monotonic_energy_scaling")
        self.assertGreater(disc.confidence_score, 0.5)
        self.assertIn("does not establish physical laws", disc.disclaimer)

    def test_json_and_csv_export(self):
        graph = build_system_graph()
        json_str = GraphExporter.export_json(graph)
        self.assertIn("component_core", json_str)

        restored_graph = GraphSerializer.from_json(json_str)
        self.assertEqual(len(restored_graph.nodes), len(graph.nodes))

        csv_str = GraphExporter.export_csv_edges(graph)
        self.assertIn("source,relationship,target", csv_str)
        self.assertIn("component_encoder,PRODUCES,component_core", csv_str)


if __name__ == "__main__":
    unittest.main()
