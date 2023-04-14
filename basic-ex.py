import promptlayer
import os
from dotenv import load_dotenv
load_dotenv()
promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")
openai = promptlayer.openai
openai.api_key =  os.getenv("OPENAI_API_KEY")

# Do something fun 🚀
resp = openai.Completion.create(
  engine="text-ada-001", 
  prompt="My name is", 
  pl_tags=["name-guessing", "pipeline-2"]
)

print(resp.choices[0].text)

