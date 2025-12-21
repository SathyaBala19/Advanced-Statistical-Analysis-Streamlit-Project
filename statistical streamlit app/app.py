import streamlit as st
import pandas as pd
import numpy as np

st.title("Statistical Analysis.App")

# Dataset Upload
uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
else:
    st.info("Please upload a csv file to continue")
    
# To select numeric column
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()  # to change into python list

if numeric_cols:
    column = st.selectbox("Select numeric column", numeric_cols)
    data = df[column].dropna().tolist()
else:
    st.error("No numeric columns found.")