import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

from chart_generator import generate_chart
from prompts import SQL_PROMPT
from query_executor import execute_query
from explanation_generator import generate_explanation

load_dotenv()

# Page Config
st.set_page_config(
    page_title="AI SQL Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI SQL Analyst")
st.markdown("Ask business questions in natural language.")

# Mistral LLM
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["question"],
    template=SQL_PROMPT
)

chain = prompt | llm

question = st.text_input(
    "Enter your business question:"
)

if st.button("Analyze"):

    if question:

        with st.spinner("Generating SQL..."):

            response = chain.invoke(
                {"question": question}
            )
            sql_query = (
            response.content
            .replace("```sql", "")
            .replace("```", "")
            .strip()
            )
            sql_query = sql_query.replace(
            "retaildb.retail_sales",
            "retail_sales"
            )
            
        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        try:
            result = execute_query(sql_query)

        except Exception as e:
            st.error(f"SQL Error: {e}")
            st.stop()
        st.subheader("Results")
        st.dataframe(result)

        explanation = generate_explanation(
            question,
            result.to_string()
        )

        st.subheader("Business Insight")
        st.write(explanation)

        if  len(result.columns) >= 2 and len(result) > 1:
            generate_chart(result)