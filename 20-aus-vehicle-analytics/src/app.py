import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Aus-Vehicles Dashboard", layout="wide")

st.title("Australia Road Vehicle Registrations 🚗")
st.markdown("Analyse road vehicle data from Australia.")

@st.cache_data
def load_data():
    file_path = "data/processed/vehicle_data_clean.parquet"
    if not os.path.exists(file_path):
        return None
    return pd.read_parquet(file_path)

df = load_data()

if df is None:
    st.warning("Processed data not found. Please run `uv run python src/fetch_data.py` and `uv run python src/clean_data.py` first.")
    st.stop()

# 1. Motive Power Evolution (Line Chart)
st.header("1. Motive Power Evolution")
st.markdown("Tracking the adoption of Electric/Hybrid vs. Petrol over time.")
df_time = df.dropna(subset=['year_of_manufacture'])
yearly_power = df_time.groupby(['year_of_manufacture', 'motive_power'])['no_vehicles'].sum().reset_index()
fig1 = px.line(yearly_power, x='year_of_manufacture', y='no_vehicles', color='motive_power', title="Vehicle Registrations Over Time by Motive Power")
st.plotly_chart(fig1, width="stretch")

# 2. Top Manufacturers
st.header("2. Top Manufacturers")
st.markdown("The top 10 most popular vehicle makes.")
df_make = df[df['make'] != 'UNKNOWN']
top_makes = df_make.groupby('make')['no_vehicles'].sum().reset_index().sort_values('no_vehicles', ascending=False).head(10)
fig2 = px.bar(top_makes, x='make', y='no_vehicles', title="Top 10 Vehicle Makes", color='no_vehicles')
st.plotly_chart(fig2, width="stretch")

# 3. Vehicle Distribution
st.header("3. Vehicle Distribution")
st.markdown("Distribution of Vehicle Type against Motive Power.")
dist_df = df.groupby(['vehicle_type', 'motive_power'])['no_vehicles'].sum().reset_index()
fig3 = px.bar(dist_df, x='vehicle_type', y='no_vehicles', color='motive_power', title="Vehicle Type vs Motive Power", barmode='stack')
st.plotly_chart(fig3, width="stretch")

# 4. Registration Trends (Overall)
st.header("4. Overall Registration Trends")
st.markdown("Overall vehicle registrations over the years to track industry growth.")
yearly_total = df_time.groupby('year_of_manufacture')['no_vehicles'].sum().reset_index()
fig4 = px.area(yearly_total, x='year_of_manufacture', y='no_vehicles', title="Total Vehicle Registrations Over Time")
st.plotly_chart(fig4, width="stretch")
