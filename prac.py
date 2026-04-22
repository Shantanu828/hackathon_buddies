from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    assets: List[str] = []

# --- SKILLS / TOOLS ---

def handle_math(text: str) -> str:
    """A deterministic tool for handling simple addition."""
    numbers = list(map(int, re.findall(r'-?\d+', text)))
    if len(numbers) >= 2:
        return f"The sum is {sum(numbers)}."
    return "Math error: Could not extract enough numbers."

def handle_llm_query(text: str, assets: List[str]) -> str:
    """Placeholder for your LLM or RAG pipeline."""
    # Here is where you would hook up Gemini, OpenAI, or a local model
    # response = llm.invoke(f"Answer {text} using {assets}")
    return "This looks like a text query. My LLM is not connected yet!"

# --- ROUTER ---

def route_query(query: str) -> str:
    """Determines the intent of the query and routes to the right tool."""
    text_lower = query.lower()
    
    # Simple heuristic to detect math queries
    math_keywords = ['+', '-', 'sum', 'add', 'minus', 'what is']
    has_numbers = any(char.isdigit() for char in text_lower)
    
    if has_numbers and any(kw in text_lower for kw in math_keywords):
        return "math"
    return "general"

# --- MAIN ENDPOINT ---

@app.post("/")
async def solve(data: QueryRequest):
    # 1. Decide what kind of query this is
    intent = route_query(data.query)

    # 2. Route to the appropriate tool
    if intent == "math":
        final_answer = handle_math(data.query)
    else:
        final_answer = handle_llm_query(data.query, data.assets)

    # 3. Return the exact JSON structure expected by the evaluator
    return {"output": final_answer}
