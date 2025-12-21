import streamlit as st
import pandas as pd
import numpy as np

st.title("Statistical Analysis.App")
    
# dataset upload
uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    # to select numeric column ONLY
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    if numeric_cols:
        column = st.selectbox("Select numeric column", numeric_cols)
        data = df[column].dropna().tolist()
        
        st.write("Selected column data (first 10 values):", data[10])
    else:
        st.error("No numeric columns found in dataset.")
        
else:
    st.info("Please upload a CSCV file to continue")