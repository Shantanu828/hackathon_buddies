from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class Query(BaseModel):
    query: str
    assets: list[str] = []

@app.post("/")
def solve(q: Query):
    numbers = list(map(int, re.findall(r'-?\d+', q.query)))

    if len(numbers) >= 2:
        return {"output": str(numbers[0] + numbers[1])}

    return {"output": "0"}
