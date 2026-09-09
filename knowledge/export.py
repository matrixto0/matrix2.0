"""
Export utilities for Knowledge Graph JSON and CSV representations.
"""

import csv
import io
import json
from typing import Any, Dict
from knowledge.graph import KnowledgeGraph
from knowledge.serializer import GraphSerializer


class GraphExporter:

    @staticmethod
    def export_json(graph: KnowledgeGraph) -> str:
        return GraphSerializer.to_json(graph)

    @staticmethod
    def export_csv_edges(graph: KnowledgeGraph) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["source", "relationship", "target", "provenance_description", "experiment_id"])

        for rel in graph.relationships:
            prov = rel.provenance
            writer.writerow([
                rel.source_id,
                rel.type,
                rel.target_id,
                prov.get("description", ""),
                prov.get("experiment_id", "")
            ])

        return output.getvalue()
