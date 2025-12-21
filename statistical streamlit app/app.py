import streamlit as st
import pandas as pd

st.title("Statistical Analysis.App")

uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
else:
    st.info("Please upload a csv file to continue")