# 23.LLM-API-Call

## Execution Results 

```bash

$make run    
uv run main.py

--- Prompt ---
What is the capital city of Australia
--- Response ---
The capital city of Australia is **Canberra**.

--- Prompt ---
Solve for 2x+1 = 0
--- Response ---
The solution to the equation \(2x + 1 = 0\) is found by isolating \(x\):

1. Subtract 1 from both sides:  
   \(2x = -1\)

2. Divide both sides by 2:  
   \(x = -\frac{1}{2}\)

Thus, the solution is \(x = -\frac{1}{2}\).

--- Prompt ---
How many 'r's are in 'strawberry'?
--- Response ---
There are 3 r's in "strawberry".

```

## Overview
This project is an introductory example for ITEC102 students demonstrating how to interact with Large Language Models (LLMs) via an API endpoint using Python. It uses the `openai` Python package to connect to an OpenAI-compatible API endpoint provided by AI Box.

## Learning Outcomes
By the end of this example, you will be able to:
- Configure Python to load environment variables from a `.env.local` file.
- Use the `openai` package to connect to a compatible API endpoint.
- Send a series of prompts to an LLM and receive the responses.
- Structure a basic Python script for clarity and maintainability.

## Project Structure
- `main.py`: The core script that initializes the API client and sends the prompts.
- `docs/theory.md`: Theoretical background on API calls and LLMs.
- `images/README.md`: Directory intended for screenshots of the script running.
- `QUICKSTART.md`: Step-by-step instructions for running the project.

For instructions on running this project, please refer to the [QUICKSTART.md](./QUICKSTART.md) file.
