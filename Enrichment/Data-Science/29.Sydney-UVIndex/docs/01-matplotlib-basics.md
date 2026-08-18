# Matplotlib Basics

`matplotlib` is a comprehensive library for creating static, animated, and interactive visualizations in Python. 

## The Figure and Axes Object
In Matplotlib, a `Figure` is the top-level container that holds all the plot elements. Inside the Figure, you have one or more `Axes` (the actual plots).
Creating a plot typically starts with:
```python
fig, ax = plt.subplots()
```

## Plotting Time Series Data
When your X-axis represents time, you often need to format the ticks so the dates don't overlap and are readable.
Using `matplotlib.dates`, we can apply specific formats to our axes:
```python
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
```

## Integrating with Streamlit
Streamlit has a special command to display Matplotlib figures directly in the app.
Instead of calling `plt.show()` (which would try to open a window on the server), we pass the figure object to Streamlit:
```python
fig, ax = plt.subplots()
# ... plot data ...
st.pyplot(fig)
```
