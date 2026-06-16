from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

from prompts import SQL_PROMPT
from query_executor import execute_query
from explanation_generator import generate_explanation
from chart_generator import generate_chart


load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["question"],
    template=SQL_PROMPT
)

chain = prompt | llm

while True:

    question = input(
        "\nAsk a business question (type 'exit' to quit): "
    )

    if question.lower() == "exit":
        break

    response = chain.invoke(
        {"question": question}
    )

    sql_query = response.content

    sql_query = (
        sql_query
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    print("\nGenerated SQL:\n")
    print(sql_query)


    result = execute_query(sql_query)

    print("\nResult:\n")
    print(result)

    explanation = generate_explanation(
        question,
        result.to_string()
    )

    print("\nBusiness Insight:\n")
    print(explanation)

    if  len(result.columns) >= 2 and len(result) > 1:
        generate_chart(result)