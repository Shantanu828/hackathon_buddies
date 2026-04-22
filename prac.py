from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class Query(BaseModel):
    query: str
    assets: list[str] = []

@app.post("/")
def solve(q: Query):
    text = q.query.strip()

    # Pattern: What is X + Y?
    match = re.search(r'what is\s*(-?\d+)\s*\+\s*(-?\d+)', text.lower())
    if match:
        a = int(match.group(1))
        b = int(match.group(2))
        return {"output": f"The sum is {a + b}."}

    # Pattern: Add X and Y
    match = re.search(r'add\s*(-?\d+)\s*(and|,)\s*(-?\d+)', text.lower())
    if match:
        a = int(match.group(1))
        b = int(match.group(3))
        return {"output": f"The sum is {a + b}."}

    # Fallback: just extract numbers
    numbers = list(map(int, re.findall(r'-?\d+', text)))
    if len(numbers) >= 2:
        return {"output": f"The sum is {numbers[0] + numbers[1]}."}

    return {"output": "The sum is 0."}
