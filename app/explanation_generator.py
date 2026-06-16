from dotenv import load_dotenv
import os

from langchain_mistralai import ChatMistralAI

# Load .env
load_dotenv()

# Create Mistral LLM
llm = ChatMistralAI(
    model="mistral-small-latest",
    mistral_api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0
)

def generate_explanation(question, result):

    prompt = f"""
You are a senior business analyst.

User Question:
{question}

Query Result:
{result}

Instructions:
1. Explain the result in simple business language.
2. Keep the explanation under 3 sentences.
3. Mention important numbers if available.
4. Do not mention SQL.
5. Be concise and professional.

Business Insight:
"""

    try:
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"Error generating explanation: {str(e)}"