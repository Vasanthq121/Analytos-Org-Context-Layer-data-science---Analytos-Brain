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
                raise ValueError(f"Invalid Source: {edge.source}")

            if edge.target not in node_ids:
                raise ValueError(f"Invalid Target: {edge.target}")

            if edge.relation not in self.VALID_RELATIONS:
                raise ValueError(f"Invalid Relation: {edge.relation}")

            print("✓ Source Exists")
            print("✓ Target Exists")
            print("✓ Relation Valid")

        print("\n" + "=" * 70)
        print("GRAPH VALIDATION SUCCESSFUL")
        print("=" * 70)
