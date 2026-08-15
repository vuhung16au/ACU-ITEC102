import os
from dotenv import load_dotenv
from openai import OpenAI

def get_llm_response(prompt: str, client: OpenAI, model: str = "deepseek-v4-pro") -> str:
    """
    Sends a prompt to the LLM API and returns the text response.
    """
    print(f"\n--- Prompt ---")
    print(prompt)
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    result = response.choices[0].message.content
    print(f"--- Response ---")
    print(result)
    return result

def main():
    # Load environment variables from .env.local
    load_dotenv(dotenv_path=".env.local")
    
    # Retrieve the API key from environment variables
    api_key = os.getenv("AI_BOX_API_KEY")
    if not api_key:
        raise ValueError("AI_BOX_API_KEY environment variable not found. Please check your .env.local file.")
    
    # Initialize the OpenAI compatible client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.ai-box.vn/v1"
    )
    
    # List of prompts to send to the LLM
    prompts = [
        "What is the capital city of Australia",
        "Solve for 2x+1 = 0",
        "How many 'r's are in 'strawberry'?"
    ]
    
    # Iterate over the prompts and get responses
    for prompt in prompts:
        get_llm_response(prompt, client)

if __name__ == "__main__":
    main()
