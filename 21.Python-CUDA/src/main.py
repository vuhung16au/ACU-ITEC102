import os
import time
import argparse

# Enable cuDF Pandas accelerator
# This allows standard pandas imports to run on the GPU where possible.
os.environ["CUDF_PANDAS_DEBUG"] = "1"
try:
    import cudf.pandas
    cudf.pandas.install()
except ImportError:
    print("cuDF not available, falling back to standard Pandas")

import pandas as pd
import numpy as np

def benchmark_cupy(mode="gpu", size=4000):
    print(f"Running benchmark on {mode.upper()}...")
    if mode == "gpu":
        try:
            import cupy as cp
            # Warmup
            a = cp.random.normal(size=(size, size))
            b = cp.random.normal(size=(size, size))
            cp.matmul(a, b)
            
            start_time = time.time()
            for _ in range(10):
                c = cp.matmul(a, b)
                cp.cuda.Stream.null.synchronize()
            end_time = time.time()
        except ImportError:
            print("CuPy not found. Make sure you are running in a CUDA environment.")
            return float('inf')
    else:
        a = np.random.normal(size=(size, size))
        b = np.random.normal(size=(size, size))
        np.matmul(a, b)
        
        start_time = time.time()
        for _ in range(10):
            c = np.matmul(a, b)
        end_time = time.time()
        
    duration = end_time - start_time
    print(f"CUDA {mode.upper()} took: {duration:.4f} seconds")
    return duration

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
    
    return pd.DataFrame(data)

def analyze_data(df):
    print("Analyzing data...")
    start_time = time.time()
    
    # Group by state and fuel type, get average age and price
    summary = df.groupby(["state", "fuel_type"]).agg({
        "age_years": "mean",
        "price": "mean"
    }).reset_index()
    
    end_time = time.time()
    print(summary.head())
    print(f"Analysis completed in {end_time - start_time:.4f} seconds.")
    
    return summary

def main():
    parser = argparse.ArgumentParser(description="CUDA GPU/CPU Benchmark")
    parser.add_argument("--benchmark", action="store_true", help="Run benchmark comparing CPU and GPU")
    args = parser.parse_args()

    if args.benchmark:
        print("=== Starting Benchmark ===")
        cpu_time = benchmark_cupy("cpu")
        gpu_time = benchmark_cupy("gpu")
        
        print("\n=== Benchmark Results ===")
        print(f"CPU Time: {cpu_time:.4f}s")
        print(f"GPU Time: {gpu_time:.4f}s")
        if cpu_time > gpu_time:
            print(f"GPU is {cpu_time / gpu_time:.2f}x faster than CPU")
        else:
            print(f"CPU is {gpu_time / cpu_time:.2f}x faster than GPU")
        return

    try:
        import cupy as cp
        print("CuPy successfully imported. GPU is available.")
        
        # Simple CuPy demonstration
        x = cp.array([1, 2, 3, 4, 5])
        y = cp.square(x)
        print("CuPy Array:", y)
    except ImportError:
        print("CuPy not found or GPU not available.")

    df = generate_synthetic_data(10_000_000)
    
    print("DataFrame Type:", type(df))
    analyze_data(df)

if __name__ == "__main__":
    main()
