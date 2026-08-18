import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page configuration
st.set_page_config(page_title="Geospatial Data Visualizer", layout="wide")

# Constants
DATA_URL = "https://data.gov.au/data/dataset/553b3049-2b8b-46a2-95e6-640d7986a8c1/resource/34076296-6692-4e30-b627-67b7c4eb1027/download/toiletmap.csv"
LOCAL_PATH = os.path.join(os.path.dirname(__file__), "data", "sample_map_data.csv")

# Module 1: Data Handler
@st.cache_data(show_spinner=False)
def load_data(source_type: str) -> pd.DataFrame:
    """
    Loads data from either the online data.gov.au source or local sample.
    """
    if source_type == "Online":
        try:
            df = pd.read_csv(DATA_URL, on_bad_lines='skip', low_memory=False)
        except Exception as e:
            st.error(f"Network error fetching online data: {e}. Falling back to Local data.")
            return load_data("Local")
    else:
        df = pd.read_csv(LOCAL_PATH)
        
    # Data Cleaning
    # Drop rows where Latitude or Longitude are NaN
    df = df.dropna(subset=['Latitude', 'Longitude'])
    
    # Cast to numeric, coerce errors to NaN and drop them
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
    df = df.dropna(subset=['Latitude', 'Longitude'])
    
    # Ensure Category and Name columns exist
    if 'Category' not in df.columns:
        df['Category'] = 'Default'
    if 'Name' not in df.columns:
        df['Name'] = 'Unknown'
        
    return df

# Module 2: Plotly Map Engine
def generate_map(df: pd.DataFrame):
    """
    Generates a Plotly scatter_mapbox.
    """
    # Calculate center of the map
    center_lat = df['Latitude'].mean() if not df.empty else -25.2744
    center_lon = df['Longitude'].mean() if not df.empty else 133.7751

    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Name",
        color="Category",
        zoom=3,
        center={"lat": center_lat, "lon": center_lon}
    )
    
    fig.update_layout(
        mapbox_style="carto-positron",
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    
    return fig

# Module 3: Streamlit UI Layout
def main():
    # Sidebar
    st.sidebar.title("⚙️ Map Controls")
    
    source_type = st.sidebar.radio(
        "Data Source",
        options=["Local", "Online"],
        index=0
    )
    
    with st.spinner("Loading data..."):
        df = load_data(source_type)
        
    if df.empty:
        st.warning("No data available to display.")
        return
        
    # Get unique categories for filtering
    categories = df['Category'].unique().tolist()
    selected_categories = st.sidebar.multiselect(
        "Filter by Category",
        options=categories,
        default=categories
    )
    
    # Filter the dataframe
    if selected_categories:
        filtered_df = df[df['Category'].isin(selected_categories)]
    else:
        filtered_df = pd.DataFrame(columns=df.columns) # Empty if nothing selected
        
    # Main Canvas
    st.title("🗺️ Geospatial Data Visualizer")
    st.markdown(
        "This application demonstrates how to fetch and clean geospatial data using "
        "**Pandas** and visualize it dynamically with **Plotly Mapbox** within a Streamlit app."
    )
    
    if filtered_df.empty:
        st.info("Please select at least one category to display on the map.")
    else:
        # Render map
        fig = generate_map(filtered_df)
        st.plotly_chart(fig, use_container_width=True)
        
    # Raw Data Expander
    with st.expander("View Raw Data"):
        st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
