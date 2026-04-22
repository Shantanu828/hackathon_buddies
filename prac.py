from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    assets: List[str] = []

@app.post("/v1/answer")
async def solve(data: QueryRequest):
    text = data.query.lower()
    
    # NEW REGEX: Catches decimals (e.g., 10.5) and negative numbers
    numbers = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', text)]

    if len(numbers) >= 2:
        a, b = numbers[0], numbers[1]
        
        # Determine operation
        if any(w in text for w in ["*", "times", "multiply"]):
            ans = a * b
            op_name = "product"
        elif any(w in text for w in ["-", "minus", "subtract", "difference"]):
            ans = a - b
            op_name = "difference"
        elif any(w in text for w in ["/", "divide", "quotient"]):
            ans = a / b
            op_name = "quotient"
        else:
            ans = sum(numbers)
            op_name = "sum"

        # Format cleanly (remove .0 if it's a whole number)
        if ans.is_integer():
            ans = int(ans)
            
        return {"output": f"The {op_name} is {ans}."}
    
    # Fallback for general questions (like "What is the capital of France?")
    # In Level 2, you'll replace this with an LLM call!
    return {"output": "I am an AI agent. Please provide a math query."}
