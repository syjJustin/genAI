import streamlit as st
import pandas as pd
import plotly.express as px
from excel_handler import ExcelProcessor
import tempfile
import os

# Initialize Excel processor
@st.cache_resource
def get_excel_processor():
    return ExcelProcessor()

processor = get_excel_processor()

# Streamlit UI
st.title("Excel Data Analyzer")

# File upload section
uploaded_file = st.file_uploader("Upload Your Excel File", type=["xlsx", "xls"])
if uploaded_file:
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    # Load Excel data
    df = processor.load_excel(tmp_path)
    os.unlink(tmp_path)  # Clean up temp file
    
    # Show basic info
    with st.expander("Show Raw Data Preview"):
        st.dataframe(df.head())
        st.write(f"Columns: {', '.join(df.columns)}")

# Query section
question = st.text_input(
    "Your question:",
    "E.g. Which team has most win?"
)
