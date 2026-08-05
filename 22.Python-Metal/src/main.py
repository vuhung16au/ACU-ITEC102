import time
import polars as pl
import numpy as np # Used just for dummy data generation
import mlx.core as mx

def generate_synthetic_data(num_rows=10_000_000):
    print(f"Generating synthetic Australian vehicle data ({num_rows} rows)...")
    np.random.seed(42)
    
    states = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT"]
    fuel_types = ["Petrol", "Diesel", "Electric", "Hybrid"]
    
    data = {
        "vehicle_id": np.arange(num_rows),
        "state": np.random.choice(states, num_rows),
        "fuel_type": np.random.choice(fuel_types, num_rows),
        "age_years": np.random.randint(1, 20, num_rows),
        "price": np.random.uniform(5000, 100000, num_rows)
    }
    
    return pl.DataFrame(data)

def analyze_data(df):
    print("Analyzing data using Polars...")
    start_time = time.time()
    
    # Group by state and fuel type, get average age and price using Polars fast multithreading
    summary = df.group_by(["state", "fuel_type"]).agg(
        pl.col("age_years").mean().alias("avg_age_years"),
        pl.col("price").mean().alias("avg_price")
    )
    
    end_time = time.time()
    print(summary.head())
    print(f"Analysis completed in {end_time - start_time:.4f} seconds.")
    
    return summary

def main():
    try:
        print("MLX is available. Apple Silicon GPU will be utilized.")
        
        # Simple MLX demonstration
        x = mx.array([1, 2, 3, 4, 5])
        y = mx.square(x)
        print("MLX Array:", y)
    except Exception as e:
        print("Failed to run MLX:", e)

    df = generate_synthetic_data(10_000_000)
    
    print("DataFrame Type:", type(df))
    analyze_data(df)

if __name__ == "__main__":
    main()
