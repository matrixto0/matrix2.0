"""
MATRIX2.0 Knowledge Discovery Demo Script.
Demonstrates running deterministic experiments, graph registration, pattern discovery, and provenance tracing.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from knowledge.registry import build_system_graph
from knowledge.node import Node
from knowledge.relationship import Relationship
from knowledge.provenance import Provenance
from knowledge.discovery import DiscoveryEngine
from knowledge.export import GraphExporter


def run_discovery_demo():
    print("=== MATRIX2.0 Knowledge Discovery Demo ===")

    # 1. Initialize system architectural graph
    graph = build_system_graph()
    print(f"Initialized System Graph: {len(graph.nodes)} nodes, {len(graph.relationships)} relationships.")

    # 2. Simulated Experiment Runs across varying frequency parameters
    experiments_data = [
        {
            "experiment_id": "exp_freq_scale_001",
            "seed": 42,
            "configuration": {"f": 1.0, "I": 2.0},
            "measurements": {"mean_energy": 2.01, "std_energy": 0.12}
        },
        {
            "experiment_id": "exp_freq_scale_002",
            "seed": 42,
            "configuration": {"f": 2.0, "I": 2.0},
            "measurements": {"mean_energy": 8.04, "std_energy": 0.25}
        },
        {
            "experiment_id": "exp_freq_scale_003",
            "seed": 42,
            "configuration": {"f": 3.0, "I": 2.0},
            "measurements": {"mean_energy": 18.09, "std_energy": 0.38}
        }
    ]

    # 3. Register experiments & outputs into Knowledge Graph
    for exp in experiments_data:
        prov = Provenance(
            source_type="experiment_runner",
            source_id=exp["experiment_id"],
            description=f"Ran experiment with seed {exp['seed']}",
            experiment_id=exp["experiment_id"],
            seed=exp["seed"],
            parameters=exp["configuration"]
        ).to_dict()

        # Add experiment node
        exp_node = Node(
            node_id=exp["experiment_id"],
            node_type="experiment",
            name=f"Experiment {exp['experiment_id']}",
            description="Frequency scaling experiment",
            metadata=exp["configuration"],
            provenance=prov
        )
        graph.add_node(exp_node)

        # Add metric node
        metric_id = f"metric_{exp['experiment_id']}_energy"
        metric_node = Node(
            node_id=metric_id,
            node_type="metric",
            name="Mean Energy Metric",
            description=f"Computed mean energy: {exp['measurements']['mean_energy']}",
            metadata=exp["measurements"],
            provenance=prov
        )
        graph.add_node(metric_node)

        # Connect experiment -> GENERATES -> metric
        graph.add_relationship(
            Relationship(exp["experiment_id"], metric_id, "GENERATES", provenance=prov)
        )

    print(f"Updated Graph: {len(graph.nodes)} nodes, {len(graph.relationships)} relationships.")

    # 4. Execute Discovery Engine
    discovery_engine = DiscoveryEngine()
    discoveries = discovery_engine.analyze_experiment_results(experiments_data)

    print("\n--- Discovered Computational Patterns ---")
    for disc in discoveries:
        d_dict = disc.to_dict()
        print(f"Discovery ID: {d_dict['id']}")
        print(f"Type:         {d_dict['type']}")
        print(f"Description:  {d_dict['pattern_description']}")
        print(f"Confidence:   {d_dict['confidence_score']}")
        print(f"Disclaimer:   {d_dict['disclaimer']}")
        print(f"Source Exps:  {d_dict['source_experiments']}")
        print(f"Reproduce:    Seed {d_dict['reproducibility_info']['seeds'][0]}")

    # 5. Export JSON Graph sample
    json_export = GraphExporter.export_json(graph)
    print(f"\nGraph JSON Export generated successfully ({len(json_export)} chars).")


if __name__ == "__main__":
    run_discovery_demo()
