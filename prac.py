from fastapi import FastAPI, Request
import re

app = FastAPI()

@app.post("/")
async def solve(request: Request):
    data = await request.json()

    text = data.get("query", "").lower()

    numbers = list(map(int, re.findall(r'-?\d+', text)))

    if len(numbers) >= 2:
        result = numbers[0] + numbers[1]
        return {"output": f"The sum is {result}."}

    return {"output": "The sum is 0."}
