import time
import argparse
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

def benchmark_mlx(mode="gpu", size=4000):
    print(f"Running MLX benchmark on {mode.upper()}...")
    if mode == "cpu":
        mx.set_default_device(mx.cpu)
    else:
        mx.set_default_device(mx.gpu)
    
    # Generate some random matrices
    a = mx.random.normal((size, size))
    b = mx.random.normal((size, size))
    
    # Warmup
    mx.eval(mx.matmul(a, b))
    
    start_time = time.time()
    for _ in range(10):
        c = mx.matmul(a, b)
        mx.eval(c)
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"MLX {mode.upper()} took: {duration:.4f} seconds")
    return duration

def main():
    parser = argparse.ArgumentParser(description="Apple Silicon GPU/CPU Benchmark")
    parser.add_argument("--benchmark", action="store_true", help="Run MLX benchmark comparing CPU and GPU")
    args = parser.parse_args()

    if args.benchmark:
        print("=== Starting Benchmark ===")
        cpu_time = benchmark_mlx("cpu")
        gpu_time = benchmark_mlx("gpu")
        
        print("\n=== Benchmark Results ===")
        print(f"CPU Time: {cpu_time:.4f}s")
        print(f"GPU Time: {gpu_time:.4f}s")
        if cpu_time > gpu_time:
            print(f"GPU is {cpu_time / gpu_time:.2f}x faster than CPU")
        else:
            print(f"CPU is {gpu_time / cpu_time:.2f}x faster than GPU")
        return

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
