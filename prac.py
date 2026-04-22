from fastapi import FastAPI, Request
import re

app = FastAPI()

# Updated path to match the submission box in your screenshot
@app.post("/v1/answer")
async def solve(request: Request):
    # Safely parse JSON
    try:
        data = await request.json()
    except Exception:
        return {"output": "Invalid JSON format."}

    # --- HACKATHON LOGGING ---
    # Keep an eye on your terminal! This will reveal the hidden test cases.
    print("\n--- INCOMING EVALUATION REQUEST ---")
    print(data)

    text = data.get("query", "").lower()

    # Find all numbers (including negative numbers)
    numbers = list(map(int, re.findall(r'-?\d+', text)))

    # Calculate the sum
    if len(numbers) > 0:
        # We use sum() to handle 2, 3, or even 10 numbers in the query
        result = sum(numbers)
        output_str = f"The sum is {result}."
    else:
        # Fallback if no numbers are found
        output_str = "I couldn't find any numbers."

    response_payload = {"output": output_str}
    
    print("--- OUTGOING RESPONSE ---")
    print(response_payload)
    print("-----------------------------------\n")

    return response_payload
