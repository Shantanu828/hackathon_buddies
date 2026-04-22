from fastapi import FastAPI, Request
import re

app = FastAPI()

@app.post("/")
async def solve(request: Request):
    data = await request.json()

    # handle different possible keys
    text = (
        data.get("query") or
        data.get("question") or
        data.get("input") or
        ""
    )

    # extract numbers
    numbers = list(map(int, re.findall(r'-?\d+', text)))

    if len(numbers) >= 2:
        result = numbers[0] + numbers[1]
        return {"output": str(result)}

    return {"output": "0"}
