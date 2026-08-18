# Plotly Mapbox Basics

`plotly.express` is a terse, consistent, high-level API for creating figures. One of its powerful features is the ability to create mapbox visualizations using `px.scatter_mapbox`.

## Mapbox Styles without API Keys
By default, some Plotly mapbox tiles require a Mapbox API Token. However, Plotly also supports several free, open-source tile providers that do not require any token, such as:
- `open-street-map`
- `carto-positron`
- `carto-darkmatter`

To use them, simply pass the `mapbox_style` argument in `update_layout`:
```python
fig.update_layout(mapbox_style="carto-positron")
```

## Creating a Scatter Mapbox
You can map a pandas dataframe directly to the map coordinates:
```python
import plotly.express as px

fig = px.scatter_mapbox(
    df, 
    lat="Latitude", 
    lon="Longitude", 
    hover_name="Name", 
    color="Category",
    zoom=3
)
```

## Integrating with Streamlit
Streamlit can natively render Plotly figures using `st.plotly_chart`:
```python
st.plotly_chart(fig, use_container_width=True)
```
