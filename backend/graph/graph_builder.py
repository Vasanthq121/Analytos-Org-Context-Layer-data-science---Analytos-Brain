try:
    from graph.models import Node, Edge, KnowledgeGraph
except ModuleNotFoundError:
    from models import Node, Edge, KnowledgeGraph


class GraphBuilder:

    def build(self, extraction):

        nodes = []
        edges = []

        product_id = (
            "product_" +
            extraction.product.name.lower().replace(" ", "_")
        )

        nodes.append(
            Node(
                id=product_id,
                label="Product",
                properties={
                    "name": extraction.product.name
                }
            )
        )

        for feature in extraction.features:

            feature_id = (
                "feature_" +
                feature.name.lower().replace(" ", "_")
            )

            nodes.append(
                Node(
                    id=feature_id,
                    label="Feature",
                    properties={
                        "name": feature.name
                    }
                )
            )

            edges.append(
                Edge(
                    source=product_id,
                    relation="HAS_FEATURE",
                    target=feature_id
                )
            )

        for proof in extraction.proof_points:
            proof_id = (
                "proof_" +
                proof.metric.lower().replace(" ", "_")
            )
            nodes.append(
                Node(
                    id=proof_id,
                    label="ProofPoint",
                    properties={
                        "metric": proof.metric,
                        "value": proof.value,
                        "unit": proof.unit
                    }
                )
            )
            if extraction.features:
                first_feature_id = (
                    "feature_" +
                    extraction.features[0].name.lower().replace(" ", "_")
                )
                edges.append(
                    Edge(
                        source=first_feature_id,
                        relation="PROVEN_BY",
                        target=proof_id
                    )
                )

        icp_id = (
            "icp_" +
            extraction.icp_segment.industry.lower().replace(" ", "_")
        )
        nodes.append(
            Node(
                id=icp_id,
                label="ICPSegment",
                properties={
                    "industry": extraction.icp_segment.industry
                }
            )
        )
        edges.append(
            Edge(
                source=product_id,
                relation="TARGETS",
                target=icp_id
            )
        )

        persona_id = (
            "persona_" +
            extraction.persona.title.lower().replace(" ", "_")
        )
        nodes.append(
            Node(
                id=persona_id,
                label="Persona",
                properties={
                    "title": extraction.persona.title
                }
            )
        )
        edges.append(
            Edge(
                source=icp_id,
                relation="HAS_PERSONA",
                target=persona_id
            )
        )

        return KnowledgeGraph(nodes=nodes, edges=edges)