import streamlit as st
import pandas as pd
from data_loader import load_raw_data
from data_cleaner import clean_energy_data
from analytics_engine import generate_brand_comparison, generate_efficiency_distribution, generate_correlation_matrix

st.set_page_config(page_title="Energy Data Cleaner", layout="wide")

def main():
    st.sidebar.title("⚙️ Data Pipeline")
    
    source_type = st.sidebar.radio(
        "Data Source",
        options=["Local", "Online"],
        index=0,
        help="Select Local for fast mock data testing, or Online for real Data.gov.au data."
    )
    
    with st.spinner("Loading raw data..."):
        raw_df = load_raw_data(source_type)
        
    if raw_df.empty:
        st.warning("Failed to load data.")
        return

    st.title("⚡ Energy Rating Data Cleaner & Analytics Engine")
    st.markdown("""
    This application demonstrates a structured data cleaning and transformation pipeline using **Pandas** and **NumPy**.
    It processes messy household appliance energy rating datasets, fixing mixed cases, multiple value cells, and coercing types safely.
    """)

    st.header("1. Raw Data Overview")
    st.write(f"Total Rows: {len(raw_df)}")
    st.dataframe(raw_df.head(10))
    
    st.subheader("Raw Data Health (Nulls & Types)")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Null counts per column:")
        st.dataframe(raw_df.isna().sum().reset_index().rename(columns={"index": "Column", 0: "Null Count"}))
    with col2:
        st.write("Data Types:")
        st.dataframe(raw_df.dtypes.astype(str).reset_index().rename(columns={"index": "Column", 0: "Type"}))

    # Clean the data
    with st.spinner("Cleaning data..."):
        clean_df = clean_energy_data(raw_df)
        
    st.divider()
    
    st.header("2. Cleaned Data Results")
    st.write(f"Total Rows: {len(clean_df)}")
    st.dataframe(clean_df.head(10))
    
    st.subheader("Clean Data Health (Nulls & Types)")
    col3, col4 = st.columns(2)
    with col3:
        st.write("Null counts per column:")
        st.dataframe(clean_df.isna().sum().reset_index().rename(columns={"index": "Column", 0: "Null Count"}))
    with col4:
        st.write("Data Types:")
        st.dataframe(clean_df.dtypes.astype(str).reset_index().rename(columns={"index": "Column", 0: "Type"}))

    st.divider()
    
    st.header("3. Analytics Engine")
    
    tab1, tab2, tab3 = st.tabs(["Brand Comparison", "Efficiency Distribution", "Correlation Matrix"])
    
    with tab1:
        st.subheader("Average Ratings & Consumption by Brand")
        st.dataframe(generate_brand_comparison(clean_df))
        
    with tab2:
        st.subheader("Efficiency Tier Distribution")
        st.bar_chart(generate_efficiency_distribution(clean_df).set_index("Efficiency_Tier"))
        
    with tab3:
        st.subheader("Correlation between Volume & Energy")
        st.dataframe(generate_correlation_matrix(clean_df))

if __name__ == "__main__":
    main()
