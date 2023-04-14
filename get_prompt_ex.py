import promptlayer
import os
from dotenv import load_dotenv
load_dotenv()
promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")

prompt = promptlayer.prompts.get("memory-summarize")
print(prompt)