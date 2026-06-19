# Advanced Statistical Analysis Streamlit Project

A simple Streamlit web application for performing statistical analysis on CSV datasets.

## Features

- Upload CSV file
- Preview dataset
- Select numeric column
- Calculate:
  - Mean
  - Median
  - Mode
  - Variance
  - Standard Deviation
  - Coefficient of Variation
- Detect outliers using IQR method
- Display histogram and boxplot
- Generate grouped frequency distribution
- Download statistical summary as CSV
- Download statistical summary as PDF

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- ReportLab

## Project Structure

```text
Advanced-Statistical-Analysis-Streamlit-Project/
│
└── statistical-streamlit-app/
    │
    ├── app.py
    └── sample datasets/
        ├── dataset.csv
        └── nvidia dataset.csv
````

## Installation

1. Clone the repository

```bash
git clone https://github.com/SathyaBala19/Advanced-Statistical-Analysis-Streamlit-Project.git
```

2. Navigate to the project folder

```bash
cd Advanced-Statistical-Analysis-Streamlit-Project/statistical-streamlit-app
```

3. Install required packages

```bash
pip install streamlit pandas numpy matplotlib seaborn reportlab
```

## Run the Application

```bash
streamlit run app.py
```

## How to Use

1. Run the app.
2. Upload a CSV file.
3. Select a numeric column.
4. View statistical summary.
5. Check outlier detection result.
6. View histogram and boxplot.
7. Download the summary as CSV or PDF.

## Sample Datasets

The project contains sample datasets inside the `sample datasets` folder. These can be used for testing the app.

## Output

The app displays:

* Dataset preview
* Statistical summary table
* Outlier detection result
* Histogram
* Boxplot
* Grouped frequency distribution
* Downloadable CSV and PDF reports

## Author

Sathya Bala

## License

This project is created for learning and practice purposes.

```
