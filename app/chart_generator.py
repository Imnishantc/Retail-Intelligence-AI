import streamlit as st

def generate_chart(df):

    if len(df.columns) < 2:
        return

    chart_df = df.set_index(df.columns[0])

    st.subheader("Visualization")

    st.bar_chart(chart_df)