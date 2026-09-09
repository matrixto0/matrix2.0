# MATRIX2.0 Knowledge Graph Package

The `knowledge` module provides a structured representation of computational artifacts, architectural components, experiment outcomes, and model discoveries within MATRIX2.0.

## Modules

- `node.py`: Defines 11 supported node types (`concept`, `parameter`, `state`, `experiment`, `metric`, `result`, `visualization`, `game`, `research_record`, `observation`, `hypothesis`).
- `relationship.py`: Defines 13 relationship types (`ENCODES`, `PRODUCES`, `DEPENDS_ON`, `MEASURES`, `VISUALIZES`, `COMPARES_WITH`, `DERIVED_FROM`, `USES_PARAMETER`, `GENERATES`, `OBSERVES`, `SUPPORTS`, `CONTRADICTS`, `RELATED_TO`).
- `provenance.py`: Traceable metadata linking nodes and edges to origin experiment IDs, random seeds, and parameter configurations.
- `graph.py`: Core `KnowledgeGraph` container managing node registration and adjacency.
- `query.py`: `QueryEngine` for finding connected components, metrics, parameter usage, and visualizations.
- `registry.py`: `build_system_graph()` helper registering all 13 core MATRIX2.0 architectural components.
- `discovery.py`: `DiscoveryEngine` detecting model-specific computational patterns and transparent ranking metrics.
- `export.py`: Exporter for JSON graph definitions and CSV edge lists.
- `test_knowledge.py`: Unit test suite.
