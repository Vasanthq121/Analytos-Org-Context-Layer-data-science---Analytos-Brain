import json

with open("graph_main.json", "r", encoding="utf-8") as f:
    graph = json.load(f)

nodes = {node["id"]: node for node in graph["nodes"]}

print("=" * 70)
print("Knowledge Graph AI Agent")
print("=" * 70)

print("""
Example Questions

1. What is the product?
2. What features does Stockly have?
3. Show all features.
4. Who is the target customer?
5. Who is the persona?
6. Show proof points.
7. What business metric is available?
8. Explain the complete graph.
9. Show all relationships.
10. exit
""")

while True:

    question = input("\nQuestion : ").lower().strip()

    if question == "exit":
        break

    # -------------------------------------------------
    # Product
    # -------------------------------------------------

    elif "product" in question:

        for node in graph["nodes"]:
            if node["label"] == "Product":
                print("\nProduct :", node["properties"]["name"])

    # -------------------------------------------------
    # Features
    # -------------------------------------------------

    elif "feature" in question:

        print("\nFeatures\n")

        for edge in graph["edges"]:
            if edge["relation"] == "HAS_FEATURE":

                feature = nodes[edge["target"]]

                print("-", feature["properties"]["name"])

    # -------------------------------------------------
    # Persona
    # -------------------------------------------------

    elif "persona" in question:

        for node in graph["nodes"]:
            if node["label"] == "Persona":

                print("\nPersona :", node["properties"]["title"])

    # -------------------------------------------------
    # ICP
    # -------------------------------------------------

    elif "target" in question or "customer" in question:

        for node in graph["nodes"]:
            if node["label"] == "ICPSegment":

                print("\nTarget Customer :", node["properties"]["industry"])

    # -------------------------------------------------
    # Proof Points
    # -------------------------------------------------

    elif "proof" in question or "metric" in question:

        print("\nProof Points\n")

        for node in graph["nodes"]:
            if node["label"] == "ProofPoint":

                p = node["properties"]

                print(
                    f"{p['metric']} : {p['value']}{p['unit']}"
                )

    # -------------------------------------------------
    # Relationships
    # -------------------------------------------------

    elif "relationship" in question:

        print()

        for edge in graph["edges"]:

            print(
                f"{edge['source']} "
                f"--{edge['relation']}--> "
                f"{edge['target']}"
            )

    # -------------------------------------------------
    # Complete Graph
    # -------------------------------------------------

    elif "graph" in question or "explain" in question:

        print("\nKnowledge Graph Summary\n")

        for edge in graph["edges"]:

            src = nodes[edge["source"]]
            tgt = nodes[edge["target"]]

            print(
                f"{src['label']} "
                f"({src['properties']})"
            )

            print(
                f"   │"
            )

            print(
                f"   └── {edge['relation']}"
            )

            print(
                f"          │"
            )

            print(
                f"          ▼"
            )

            print(
                f"{tgt['label']} "
                f"({tgt['properties']})"
            )

            print()

    else:

        print("\nSorry, I don't understand that question.")