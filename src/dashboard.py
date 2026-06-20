import streamlit as st
import pandas as pd


st.title("LLM Supply Chain Risk Intelligence")


df = pd.read_csv(
    "outputs/risk_scores.csv"
)


st.subheader("Risk Score by Category")


st.bar_chart(
    df.set_index("risk_category")["risk_score"]
)


st.subheader("Risk Analytics")


st.dataframe(df)