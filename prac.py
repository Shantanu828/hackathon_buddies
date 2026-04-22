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

    numbers = list(map(int, re.findall(r'-?\d+', text)))

    if len(numbers) >= 2:
        a, b = numbers[0], numbers[1]

        if any(word in text for word in ["+", "add", "plus"]):
            return {"output": f"The sum is {a + b}."}

        elif any(word in text for word in ["-", "subtract", "minus"]):
            return {"output": f"The difference is {a - b}."}

        elif any(word in text for word in ["*", "multiply", "times"]):
            return {"output": f"The product is {a * b}."}

        elif any(word in text for word in ["/", "divide", "divided"]):
            if b != 0:
                result = a / b
                if result.is_integer():
                    result = int(result)
                return {"output": f"The quotient is {result}."}

    return {"output": "Unable to process"}
