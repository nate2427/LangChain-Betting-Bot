import promptlayer
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
import os
from dotenv import load_dotenv
load_dotenv()
promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")
chat = PromptLayerChatOpenAI()
resp = chat([
	SystemMessage(content="You are a helpful assistant that translates English to Spanish."),
	HumanMessage(content="Translate this sentence from English to Spanish. I love programming.")
])
print(resp.content)
# write a new function for data processing
def process_data(data):
    return data