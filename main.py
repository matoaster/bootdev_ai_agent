from google import genai
from google.genai import types
import os, sys
from dotenv import load_dotenv



def main():
    load_dotenv()
    
    args = sys.argv[1:]
    is_verbose = "--verbose" in args
    prompt_parts = [a for a in args if a != "--verbose"]

    if not args:
        print("Usage: python main.py 'your prompt here'")
        sys.exit(1)
    
    user_prompt = " ".join(prompt_parts) 

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    resp = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    if is_verbose == True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}") 
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")    
    print("Response: ")
    print(resp.text)
if __name__ == "__main__":
    main()
