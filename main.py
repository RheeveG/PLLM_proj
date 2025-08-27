import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

#print(api_key)
from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)
flag = ""
if (len(sys.argv) < 2):
	raise Exception("No question asked. Exiting.")
user_prompt = sys.argv[1]
if (len(sys.argv) == 3):
	flag = sys.argv[2]

messages = [
	types.Content(role="user", parts=[types.Part(text=user_prompt)])
]
#print(client)

#print(content)
output = client.models.generate_content(
	model="gemini-2.0-flash-001", 
	contents=messages,
)
if(flag=="--verbose"):
	print(f"User prompt: {user_prompt}")
print(output.text)
if(flag=="--verbose"):
	print(f"Prompt tokens: {output.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {output.usage_metadata.candidates_token_count}")


