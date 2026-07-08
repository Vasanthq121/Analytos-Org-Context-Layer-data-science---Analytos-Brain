import json
import os
import streamlit as st

st.set_page_config(
    page_title="Knowledge Graph Dashboard",
    layout="wide"
)

st.title("Knowledge Graph Dashboard")

MAIN_GRAPH = "graph_main.json"

if not os.path.exists(MAIN_GRAPH):
    st.error("graph_main.json not found.")
    st.info("Run review.py and approve the graph first.")
    st.stop()

with open(MAIN_GRAPH, "r", encoding="utf-8") as f:
    graph = json.load(f)

st.success("Main Knowledge Graph Loaded")

st.divider()

# Recent Changes
st.subheader("Recent Changes")
branch = graph.get("branch", "main")
st.info(f"Latest Commit from branch: **{branch}** | Approved by: **Admin (mock)**")

st.divider()

# Search Box
st.subheader("Search Entities")
search_query = st.text_input("Search (simulating vector+BM25+graph search)", "")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Nodes")

    for node in graph["nodes"]:
        node_text = json.dumps(node).lower()
        if search_query.lower() not in node_text:
            continue


        with st.expander(f"{node['label']} : {node['id']}"):

            st.json(node["properties"])

with col2:

    st.subheader("Relationships")

    for edge in graph["edges"]:

        st.write(
            f"{edge['source']} "
            f"── {edge['relation']} ──► "
            f"{edge['target']}"
        )

st.divider()

st.metric("Total Nodes", len(graph["nodes"]))
st.metric("Total Relationships", len(graph["edges"]))