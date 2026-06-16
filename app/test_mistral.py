from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

print("Key loaded:", api_key[:10])

llm = ChatMistralAI(
    model="mistral-small-latest",
    mistral_api_key=api_key,
    temperature=0
)

response = llm.invoke("Say hello")

print("\nResponse:")
print(response.content)