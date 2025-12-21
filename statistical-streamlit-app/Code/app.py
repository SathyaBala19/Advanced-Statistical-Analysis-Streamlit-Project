import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Table

# Dataset upload
st.title("Statistical Analysis App")
uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Select numeric columns only
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if numeric_cols:
        column = st.selectbox("Select numeric column", numeric_cols)

        # KEEP data as Pandas Series
        data = df[column].dropna()

        st.write("Selected column data (first 10 values):")
        st.dataframe(data.head(10))

        # Statistical calculations
        mean = data.mean()
        median = data.median()
        mode = data.mode().iloc[0]
        variance = data.var()
        std_dev = data.std()
        cv = (std_dev / mean) * 100
        
        # outlier detection
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1
        
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = [x for x in data if x < lower or x > upper]
        
        # statistical summary
        st.subheader("Statistical Summary")

        summary = pd.DataFrame({
            "Measure": [
                "Mean", "Median", "Mode",
                "Variance", "Standard Deviation",
                "Coefficient of Variation (%)"
            ],
            "Value": [
                mean, median, mode,
                variance, std_dev, cv
            ]
        })

        st.table(summary.round(3))
        
        # Outlier detect msg
        st.subheader("Outlier Detection (IQR Method)")
        st.write(f"Lower Bound: {round(lower,2)}")
        st.write(f"Upper Bound: {round(upper,2)}")
        
        if outliers:
            st.warning(f"Outliers detected: {outliers}")
        else:
            st.success("No outliers detected")
            
        # visualizations
        st.subheader("Visualization")
        
        fig1, ax1 = plt.subplots()
        sns.histplot(data, kde=True, ax=ax1)
        st.pyplot(fig1)
        
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=data, ax=ax2)
        st.pyplot(fig2)
        
        # grouped frequency distribution
        st.subheader("📊 Grouped Frequency Distribution")

        bins = st.slider("Number of bins", 3, 15, 5)

        freq, bin_edges = np.histogram(data, bins=bins)

        grouped_df = pd.DataFrame({
            "Class Interval": [
                f"{round(bin_edges[i],2)} - {round(bin_edges[i+1],2)}"
                for i in range(len(freq))
            ],
            "Frequency": freq
        })

        st.table(grouped_df)
        
        # exporting results to a csv
        csv = summary.to_csv(index=False).encode("utf-8")
        
        st.download_button(
            "Download Summary as CSV",
            csv,
            "statistical_summary.csv",
            "text/csv"
        )
        
        # export results to pdf
        # function
        def export_pdf(df):
            file_name = "statistical_summary.pdf"
            pdf = SimpleDocTemplate(file_name)
            table = Table([df.columns.tolist()] + df.round(3).values.tolist())
            pdf.build([table])
            return file_name
        # button
        if st.button("Download Summary as PDF"):
            pdf_file = export_pdf(summary)
            with open(pdf_file, "rb") as f:
                st.download_button(
                    "Click to downlooad pdf",
                    f,
                    file_name=pdf_file,
                    mime="application/pdf"
                )
        
    else:
        st.error("No numeric columns found in dataset.")

else:
    st.info("Please upload a CSV file to continue")
