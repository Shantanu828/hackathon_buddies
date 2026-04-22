from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class Query(BaseModel):
    query: str
    assets: list[str] = []

@app.post("/")
def solve(q: Query):
    text = q.query.lower()

    # extract numbers
    numbers = list(map(int, re.findall(r'\d+', text)))

    if len(numbers) >= 2:
        result = numbers[0] + numbers[1]
        return {"output": f"The sum is {result}."}

    return {"output": "Unable to process"}
