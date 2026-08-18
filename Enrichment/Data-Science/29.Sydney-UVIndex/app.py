import streamlit as st
import pandas as pd
from data_handler import fetch_and_process_data
from visualizations import plot_uv_timeline, plot_uv_histogram

# Setup page config
st.set_page_config(page_title="Sydney UV Index Visualizer", layout="wide")

def main():
    st.sidebar.title("Configuration")
    
    # Toggle for Data Source
    data_source = st.sidebar.radio(
        "Data Source",
        options=["Offline (Local Sample)", "Live (data.gov.au)"],
        index=0
    )
    source_arg = "online" if "Live" in data_source else "offline"

    # Fetch Data
    with st.spinner("Loading data..."):
        df = fetch_and_process_data(source=source_arg)

    if df.empty:
        st.warning("No data found.")
        return

    # Date Range Slider
    st.sidebar.subheader("Filter Data")
    min_date = df.index.min().date()
    max_date = df.index.max().date()

    if min_date == max_date:
        # Streamlit slider needs a range, if same day, just use inputs
        start_date = min_date
        end_date = max_date
        st.sidebar.info("Dataset only covers a single day.")
    else:
        date_range = st.sidebar.slider(
            "Select Date Range",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date)
        )
        start_date, end_date = date_range

    # Filter dataframe based on selection
    mask = (df.index.date >= start_date) & (df.index.date <= end_date)
    filtered_df = df.loc[mask]

    # Main Canvas
    st.title("☀️ Sydney UV Index Visualizer")
    st.markdown("""
    Welcome to the Sydney UV Index Visualizer! This dashboard helps you analyze the UV Index in Sydney over time.
    It demonstrates how to integrate `pandas` for data manipulation, `matplotlib` for creating static visual charts, 
    and Streamlit's built-in mapping and layout tools.
    """)

    if filtered_df.empty:
        st.warning("No data available for the selected date range.")
        return

    # Row 1 (Map & Metrics)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Data Collection Location")
        # Extract unique coordinates for the map
        # dropna to avoid mapping issues if coords are missing
        map_df = filtered_df[['Lat', 'Lon']].dropna().drop_duplicates()
        if not map_df.empty:
            # st.map expects lowercase 'lat' and 'lon' or 'latitude' and 'longitude'
            map_df = map_df.rename(columns={'Lat': 'lat', 'Lon': 'lon'})
            st.map(map_df, zoom=10)
        else:
            st.info("No coordinate data available for mapping.")

    with col2:
        st.subheader("Key Metrics")
        max_uv = filtered_df['UV_Index'].max()
        avg_uv = filtered_df['UV_Index'].mean()
        
        # Determine risk level based on max UV
        if max_uv >= 11:
            risk = "Extreme"
        elif max_uv >= 8:
            risk = "Very High"
        elif max_uv >= 6:
            risk = "High"
        elif max_uv >= 3:
            risk = "Moderate"
        else:
            risk = "Low"

        st.metric("Max UV Index", f"{max_uv:.1f}", risk)
        st.metric("Average UV Index", f"{avg_uv:.1f}")
        st.metric("Total Records", f"{len(filtered_df)}")

    st.divider()

    # Row 2 (Primary Visuals)
    st.subheader("UV Index Timeline")
    fig_timeline = plot_uv_timeline(filtered_df)
    st.pyplot(fig_timeline)

    st.subheader("UV Index Distribution")
    fig_hist = plot_uv_histogram(filtered_df)
    st.pyplot(fig_hist)


if __name__ == "__main__":
    main()
