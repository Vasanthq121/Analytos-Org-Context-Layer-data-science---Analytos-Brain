from dataclasses import dataclass

# ==========================
# Graph Models
# ==========================

@dataclass
class Node:
    id: str
    label: str
    properties: dict


@dataclass
class Edge:
    source: str
    relation: str
    target: str


@dataclass
class KnowledgeGraph:
    nodes: list
    edges: list


# ==========================
# Graph Builder
# ==========================

class GraphBuilder:

    def build(self):

        nodes = [
            Node(
                id="product_stockly",
                label="Product",
                properties={
                    "name": "Stockly"
                }
            ),

            Node(
                id="feature_ai_forecasting",
                label="Feature",
                properties={
                    "name": "AI Forecasting"
                }
            ),

            Node(
                id="feature_inventory_optimization",
                label="Feature",
                properties={
                    "name": "Inventory Optimization"
                }
            ),

            Node(
                id="proof_inventory_reduction",
                label="ProofPoint",
                properties={
                    "metric": "Inventory Reduction",
                    "value": 22,
                    "unit": "%"
                }
            ),

            Node(
                id="icp_retail",
                label="ICPSegment",
                properties={
                    "industry": "Retail Chains"
                }
            ),

            Node(
                id="persona_supply_chain_manager",
                label="Persona",
                properties={
                    "title": "Supply Chain Manager"
                }
            )
        ]

        edges = [

            Edge(
                source="product_stockly",
                relation="HAS_FEATURE",
                target="feature_ai_forecasting"
            ),

            Edge(
                source="product_stockly",
                relation="HAS_FEATURE",
                target="feature_inventory_optimization"
            ),

            Edge(
                source="feature_ai_forecasting",
                relation="PROVEN_BY",
                target="proof_inventory_reduction"
            ),

            Edge(
                source="product_stockly",
                relation="TARGETS",
                target="icp_retail"
            ),

            Edge(
                source="icp_retail",
                relation="HAS_PERSONA",
                target="persona_supply_chain_manager"
            )

        ]

        return KnowledgeGraph(nodes, edges)


# ==========================
# Graph Validator
# ==========================

class GraphValidator:

    VALID_NODE_TYPES = {
        "Product",
        "Feature",
        "ProofPoint",
        "Persona",
        "ICPSegment"
    }

    VALID_RELATIONS = {
        "HAS_FEATURE",
        "PROVEN_BY",
        "TARGETS",
        "HAS_PERSONA"
    }

    def validate(self, graph):

        print("\n" + "=" * 70)
        print("GRAPH VALIDATION")
        print("=" * 70)

        node_ids = set()

        print("\nChecking Nodes...")

        for node in graph.nodes:

            print(f"\nNode : {node.id}")

            if not node.id:
                raise ValueError("Missing Node ID")
            print("✓ Node ID Present")

            if node.label not in self.VALID_NODE_TYPES:
                raise ValueError(f"Invalid Label : {node.label}")
            print(f"✓ Valid Label : {node.label}")

            if node.id in node_ids:
                raise ValueError(f"Duplicate Node : {node.id}")

            node_ids.add(node.id)

            print("✓ Unique Node")
            print(f"✓ Properties : {node.properties}")

        print("\nChecking Relationships...")

        for edge in graph.edges:

            print(f"\n{edge.source} --{edge.relation}--> {edge.target}")

            if edge.source not in node_ids:
                raise ValueError("Invalid Source")

            if edge.target not in node_ids:
                raise ValueError("Invalid Target")

            if edge.relation not in self.VALID_RELATIONS:
                raise ValueError("Invalid Relation")

            print("✓ Source Exists")
            print("✓ Target Exists")
            print("✓ Relation Valid")

        print("\n" + "=" * 70)
        print("GRAPH VALIDATION SUCCESSFUL")
        print("=" * 70)


# ==========================
# MAIN
# ==========================

builder = GraphBuilder()

graph = builder.build()

validator = GraphValidator()

validator.validate(graph)

print("\n")
print("=" * 70)
print("KNOWLEDGE GRAPH")
print("=" * 70)

print("\nNODES\n")

for node in graph.nodes:
    print(f"""
ID : {node.id}
TYPE : {node.label}
PROPERTIES : {node.properties}
""")

print("\nRELATIONSHIPS\n")

for edge in graph.edges:
    print(
        f"{edge.source} --[{edge.relation}]--> {edge.target}"
    )

print("""

========================================================================

                    Product
                  product_stockly
                         |
        +----------------+----------------+
        |                                 |
  HAS_FEATURE                      TARGETS
        |                                 |
        V                                 V
 AI Forecasting                  Retail Chains
        |
   PROVEN_BY
        |
        V
Inventory Reduction (22%)

========================================================================

""")