import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from mcp_server import search_entities, get_entity_connections

load_dotenv()

def run_gtm_agent(product: str):
    role = "gtm-agent"
    print(f"Agent Role: {role}")
    print(f"Target Product: {product}")
    
    # 1. MCP Graph Retrieval for prospects
    print("\n[Tool Call] search_entities: ", product)
    product_results = search_entities(role, product)
    
    print("\n[Tool Call] search_entities: Persona / ICP")
    icp_results = search_entities(role, "Persona")
    
    # 2. LLM Generation
    print("\nGenerating Prospecting Brief using Gemini...")
    system_prompt = f"You are a GTM Strategist. Write a short prospecting brief for {product}. Based ONLY on the context, include the target company profile, 3 plausible example companies, the persona to contact, and an opening angle grounded in proof points."
    
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            system_prompt,
            f"Context from Graph: {product_results}\n{icp_results}"
        ],
    )
    
    print("\n" + "="*50)
    print("PROSPECTING BRIEF:")
    print("="*50)
    print(response.text)
    print("="*50)

if __name__ == "__main__":
    run_gtm_agent("Inspectly")
