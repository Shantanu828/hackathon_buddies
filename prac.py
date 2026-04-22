from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/sum")
async def sum_endpoint(q: Question):
    question = q.question
    # Assume format: "what is a+b?"
    if question.startswith('what is ') and '+' in question:
        rest = question[8:]  # after "what is "
        plus_pos = rest.find('+')
        if plus_pos != -1:
            a_str = rest[:plus_pos]
            b_str = rest[plus_pos + 1:]
            # remove trailing ?
            if b_str.endswith('?'):
                b_str = b_str[:-1]
            try:
                a = int(a_str)
                b = int(b_str)
                sum_val = a + b
                return {"answer": f"the sum is {sum_val}"}
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid numbers")
    raise HTTPException(status_code=400, detail="Invalid format")
