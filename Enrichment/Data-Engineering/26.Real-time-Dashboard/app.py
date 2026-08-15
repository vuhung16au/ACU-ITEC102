import streamlit as st
import duckdb
import plotly.express as px

st.set_page_config(page_title="Domestic Aviation Dashboard", layout="wide")

st.title("✈️ Domestic Aviation Statistics Dashboard")
st.markdown("Analyze domestic flight routes and passenger counts across Australia.")

@st.cache_resource
def load_data():
    # Connect to an in-memory DuckDB database
    conn = duckdb.connect()
    # Create a view directly on top of the Parquet file
    conn.execute("CREATE VIEW flights AS SELECT * FROM 'data/mock_flights.parquet'")
    return conn

conn = load_data()

# Sidebar filters
st.sidebar.header("Filters")
origins = conn.execute("SELECT DISTINCT origin FROM flights ORDER BY origin").df()['origin'].tolist()
selected_origin = st.sidebar.selectbox("Select Origin Airport", ["All"] + origins)

destinations = conn.execute("SELECT DISTINCT destination FROM flights ORDER BY destination").df()['destination'].tolist()
selected_dest = st.sidebar.selectbox("Select Destination Airport", ["All"] + destinations)

# Build the query
query = "SELECT date, origin, destination, flights, passengers, seats FROM flights WHERE 1=1"
if selected_origin != "All":
    query += f" AND origin = '{selected_origin}'"
if selected_dest != "All":
    query += f" AND destination = '{selected_dest}'"

# Execute query to pandas dataframe for Streamlit
df_filtered = conn.execute(query).df()

# Display Metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Flights", f"{df_filtered['flights'].sum():,}")
col2.metric("Total Passengers", f"{df_filtered['passengers'].sum():,}")
avg_load_factor = (df_filtered['passengers'].sum() / df_filtered['seats'].sum()) * 100 if df_filtered['seats'].sum() > 0 else 0
col3.metric("Avg Load Factor", f"{avg_load_factor:.1f}%")

# Plotting with Plotly
st.subheader("Passenger Traffic Over Time")
# Group by month for cleaner charting
df_filtered['month'] = df_filtered['date'].dt.to_period('M').dt.to_timestamp()
df_monthly = df_filtered.groupby('month', as_index=False)['passengers'].sum()

fig = px.line(df_monthly, x='month', y='passengers', title='Monthly Passengers')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Raw Data Preview")
st.dataframe(df_filtered.head(100))
