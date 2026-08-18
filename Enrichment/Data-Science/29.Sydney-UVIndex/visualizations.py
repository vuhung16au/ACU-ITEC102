import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_uv_timeline(df):
    """
    Creates a time-series plot of the UV Index.
    Expects df to have a DatetimeIndex and a 'UV_Index' column.
    """
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Plot the data
    ax.plot(df.index, df['UV_Index'], color='orange', label='UV Index', linewidth=2)
    
    # Thresholds
    ax.axhline(y=3, color='blue', linestyle='--', label='Protection Required (3+)')
    ax.axhline(y=11, color='red', linestyle='-', label='Extreme (11+)')
    
    # Formatting
    ax.set_title('UV Index Timeline', fontsize=16)
    ax.set_xlabel('Date and Time', fontsize=12)
    ax.set_ylabel('UV Index', fontsize=12)
    
    # Date formatting on X-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    
    return fig

def plot_uv_histogram(df):
    """
    Creates a histogram showing the frequency of different UV intensity levels.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # We only care about times when there's actual UV (e.g., ignore all the night 0s if desired, 
    # but for completeness we can plot all, or filter > 0)
    # Let's filter > 0 to show meaningful daytime distribution
    daylight_uv = df[df['UV_Index'] > 0]['UV_Index']
    
    ax.hist(daylight_uv, bins=15, color='coral', edgecolor='black')
    
    # Formatting
    ax.set_title('Distribution of Daytime UV Index Levels', fontsize=16)
    ax.set_xlabel('UV Index', fontsize=12)
    ax.set_ylabel('Frequency (Hours)', fontsize=12)
    
    ax.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    
    return fig
