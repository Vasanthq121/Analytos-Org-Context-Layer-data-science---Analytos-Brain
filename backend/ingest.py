import sys
import os
import json
from uuid import uuid4
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__)))

from ingestion.loader import DocumentLoader
from extractor.extractor import Extractor
from graph.graph_builder import GraphBuilder
from dataclasses import asdict

def run_pipeline():
    print("Starting ingestion pipeline...")
    seed_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seed-data")
    
    # 1. Load documents
    loader = DocumentLoader()
    docs = loader.load_documents(seed_folder)
    print(f"Loaded {len(docs)} documents from {seed_folder}")

    # 2. Extract using LLM
    extractor = Extractor()
    builder = GraphBuilder()
    
    all_nodes = []
    all_edges = []
    
    for doc in docs:
        print(f"Extracting doc: {doc.file_name}...")
        try:
            result = extractor.extract(doc.content)
            graph = builder.build(result)
            for n in graph.nodes:
                all_nodes.append(asdict(n))
            for e in graph.edges:
                all_edges.append(asdict(e))
        except Exception as e:
            print(f"Failed extracting {doc.file_name}: {e}")

    # 3. Create graph mutation JSON (to simulate writing to a branch)
    run_id = datetime.now().strftime("%Y%m%d%H%M%S")
    branch_name = f"ingest/{run_id}"
    
    mutation_data = {
        "branch": branch_name,
        "nodes": all_nodes,
        "edges": all_edges
    }
    
    out_file = os.path.join(os.path.dirname(__file__), "graph_output.json")
    with open(out_file, "w") as f:
        json.dump(mutation_data, f, indent=4)
        
    print(f"Ingestion complete. Graph mutations saved to {out_file} on simulated branch '{branch_name}'.")

if __name__ == "__main__":
    run_pipeline()
