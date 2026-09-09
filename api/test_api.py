"""
Unit tests for MATRIX2.0 Local Research API endpoints.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.routes import handle_api_request


class TestAPI(unittest.TestCase):

    def test_health_endpoint(self):
        code, resp = handle_api_request("/api/health")
        self.assertEqual(code, 200)
        self.assertEqual(resp["status"], "ok")
        self.assertTrue(resp["components"]["knowledge_graph"])

    def test_knowledge_nodes_endpoints(self):
        code, resp = handle_api_request("/api/knowledge/nodes")
        self.assertEqual(code, 200)
        self.assertGreater(resp["count"], 0)

        # Single node fetch
        code, resp = handle_api_request("/api/knowledge/nodes/component_core")
        self.assertEqual(code, 200)
        self.assertEqual(resp["node"]["name"], "Mathematical Core")

        # Missing node fetch
        code, resp = handle_api_request("/api/knowledge/nodes/non_existent_node")
        self.assertEqual(code, 404)

    def test_knowledge_relationships_and_neighbors(self):
        code, resp = handle_api_request("/api/knowledge/relationships")
        self.assertEqual(code, 200)
        self.assertGreater(resp["count"], 0)

        code, resp = handle_api_request("/api/knowledge/neighbors/component_core")
        self.assertEqual(code, 200)
        self.assertIn("neighbors", resp)

    def test_discoveries_and_export_endpoints(self):
        code, resp = handle_api_request("/api/knowledge/discoveries")
        self.assertEqual(code, 200)
        self.assertIn("discoveries", resp)

        code, resp = handle_api_request("/api/knowledge/export")
        self.assertEqual(code, 200)
        self.assertIn("nodes", resp)


if __name__ == "__main__":
    unittest.main()
