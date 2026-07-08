# Step 1
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from extractor.test import result
# Step 2
from graph.graph_builder import GraphBuilder

# Step 3
from graph.validator import GraphValidator

# Step 4
from dataclasses import asdict
import json

builder = GraphBuilder()

graph = builder.build(result)

validator = GraphValidator()

validator.validate(graph)

graph_json = {
    "nodes": [asdict(node) for node in graph.nodes],
    "edges": [asdict(edge) for edge in graph.edges]
}

with open("graph_draft.json", "w") as f:
    json.dump(graph_json, f, indent=4)

print("draft graph created")