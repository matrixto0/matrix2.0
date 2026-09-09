"""
System registry populating MATRIX2.0 system architecture nodes and relationships.
"""

from knowledge.graph import KnowledgeGraph
from knowledge.node import Node
from knowledge.relationship import Relationship
from knowledge.provenance import Provenance


def build_system_graph() -> KnowledgeGraph:
    """Builds and populates the default MATRIX2.0 architectural knowledge graph."""
    graph = KnowledgeGraph()
    prov = Provenance(source_type="system", source_id="core_architecture", description="System architectural definition").to_dict()

    # Define Architecture Nodes
    nodes = [
        Node("component_core", "concept", "Mathematical Core", "MatrixState vector M=(x, f, I, phi, c, v)", provenance=prov),
        Node("component_encoder", "concept", "Encoder", "Text-to-state symbolic encoder", provenance=prov),
        Node("component_decoder", "concept", "Decoder", "State-to-text symbolic decoder", provenance=prov),
        Node("component_dynamics", "concept", "Dynamics Engine", "Differential state evolutions over time", provenance=prov),
        Node("component_particles", "concept", "Particle System", "State mapping to particle fields", provenance=prov),
        Node("component_chaos", "concept", "Chaos Laboratory", "Attractors and non-linear perturbations", provenance=prov),
        Node("component_lab", "concept", "Living Lab", "Interactive metrics and guided lessons", provenance=prov),
        Node("component_visual", "concept", "Visual Universe", "Visual trajectory and wave state renderers", provenance=prov),
        Node("component_arcade", "concept", "Simulation Arcade", "Interactive state prediction games", provenance=prov),
        Node("component_experiments", "concept", "Experiment Engine", "Deterministic reproducible experiment runner", provenance=prov),
        Node("component_research", "concept", "Research Framework", "Hypothesis, Observation, and Conclusion schema", provenance=prov),
        Node("component_dashboard", "concept", "Research Dashboard", "Browser visual dashboard and local state controls", provenance=prov),
        Node("param_f", "parameter", "Frequency (f)", "Oscillation rate parameter", provenance=prov),
        Node("param_I", "parameter", "Intensity (I)", "Amplitude scaling factor", provenance=prov),
        Node("param_c", "parameter", "Chaos (c)", "Non-linear perturbation coefficient", provenance=prov)
    ]

    for n in nodes:
        graph.add_node(n)

    # Architectural Relationships
    rels = [
        Relationship("component_encoder", "component_core", "PRODUCES", provenance=prov),
        Relationship("component_core", "component_dynamics", "DEPENDS_ON", provenance=prov),
        Relationship("component_dynamics", "component_particles", "PRODUCES", provenance=prov),
        Relationship("component_chaos", "component_dynamics", "RELATED_TO", provenance=prov),
        Relationship("component_experiments", "component_core", "USES_PARAMETER", provenance=prov),
        Relationship("component_visual", "component_core", "VISUALIZES", provenance=prov),
        Relationship("component_experiments", "component_research", "PRODUCES", provenance=prov),
        Relationship("param_f", "component_core", "DEPENDS_ON", provenance=prov),
        Relationship("param_I", "component_core", "DEPENDS_ON", provenance=prov),
        Relationship("param_c", "component_chaos", "DEPENDS_ON", provenance=prov)
    ]

    for r in rels:
        graph.add_relationship(r)

    return graph
