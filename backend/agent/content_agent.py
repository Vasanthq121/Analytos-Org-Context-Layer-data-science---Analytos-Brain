import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from mcp_server import search_entities, get_entity_connections

load_dotenv()

def run_content_agent(topic: str):
    role = "content-agent"
    print(f"🕵️ Agent Role: {role}")
    print(f"📝 Topic: {topic}")
    
    # 1. MCP Graph Retrieval
    print("\n[Tool Call] search_entities: ", topic)
    results = search_entities(role, topic)
    
    print("\n[Tool Call] Checking access to restricted data (EmailThread)...")
    email_results = search_entities(role, "Internal-Only")
    print(f"Email Access Result: {email_results.strip()}") # Should be denied
    
    # 2. LLM Generation
    print("\nGenerating Blog Post using Gemini...")
    system_prompt = f"You are a Content Marketer. Write a short blog post about {topic}. Base your facts ONLY on the provided graph context. Mention at least 3 specific graph facts."
    
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            system_prompt,
            f"Context from Graph: {results}"
        ],
    )
    
    print("\n" + "="*50)
    print("✍️ BLOG DRAFT:")
    print("="*50)
    print(response.text)
    print("="*50)

if __name__ == "__main__":
    run_content_agent("Stockly")
