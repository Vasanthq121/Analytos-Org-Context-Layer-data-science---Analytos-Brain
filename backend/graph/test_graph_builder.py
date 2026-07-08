from graph.builder import GraphBuilder

builder = GraphBuilder()

nodes, edges = builder.build(result)

print("Nodes")

for n in nodes:
    print(n)

print()

print("Edges")

for e in edges:
    print(e)