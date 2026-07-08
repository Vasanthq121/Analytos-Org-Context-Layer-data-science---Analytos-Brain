import json
import os
from tempfile import NamedTemporaryFile
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Context Layer")

MAIN_GRAPH = os.path.join(os.path.dirname(__file__), "graph_main.json")

def _check_cedar_policy(role: str, resource_type: str) -> bool:
    """Mock Cedar policy engine check"""
    if role == "admin":
        return True
    elif role == "content-agent":
        if resource_type in ["Product", "Metric", "Feature", "ProofPoint"]:
            return True
        return False
    elif role == "gtm-agent":
        if resource_type in ["Product", "ICPSegment", "Persona", "Feature", "Metric", "ProofPoint"]:
            return True
        return False
    return False

def _read_graph():
    if not os.path.exists(MAIN_GRAPH):
        return {"nodes": [], "edges": []}
    with open(MAIN_GRAPH, "r") as f:
        return json.load(f)

@mcp.tool()
def search_entities(agent_role: str, query: str) -> str:
    """
    Search the Knowledge Graph for entities matching the query.
    Access control is enforced based on the agent_role.
    """
    graph = _read_graph()
    results = []
    
    for node in graph["nodes"]:
        if not _check_cedar_policy(agent_role, node["label"]):
            continue
            
        node_text = json.dumps(node).lower()
        if query.lower() in node_text:
            results.append(node)
            
    if not results:
        return f"No results found or access denied for role '{agent_role}'."
        
    return json.dumps(results, indent=2)

@mcp.tool()
def get_entity_connections(agent_role: str, entity_id: str) -> str:
    """
    Get all connected nodes to a specific entity ID.
    Enforces Cedar-based access control.
    """
    graph = _read_graph()
    results = []
    
    # Check if we have access to this node first
    base_node = next((n for n in graph["nodes"] if n["id"] == entity_id), None)
    if base_node and not _check_cedar_policy(agent_role, base_node["label"]):
        return "Access denied."
        
    for edge in graph["edges"]:
        if edge["source"] == entity_id or edge["target"] == entity_id:
            other_id = edge["target"] if edge["source"] == entity_id else edge["source"]
            target_node = next((n for n in graph["nodes"] if n["id"] == other_id), None)
            
            if target_node and _check_cedar_policy(agent_role, target_node["label"]):
                results.append(target_node)
                
    return json.dumps(results, indent=2)

# Expose the app instance natively so uvicorn CLI can target it directly
app = mcp.sse_app()

if __name__ == "__main__":
    if os.getenv("PORT"):
        import uvicorn
        port = int(os.getenv("PORT", 8000))
        # Bind explicitly to 0.0.0.0 for public accessibility in cloud
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        # Local execution for Claude Desktop (stdio)
        mcp.run()
