# 22. Python on Metal

This example project demonstrates how to leverage Apple Silicon (M-Series chips) to accelerate data science workflows using Python natively on macOS.

## Results 

```bash
$uname -a 
Darwin 25.1.0 Darwin Kernel Version 25.1.0: Mon Oct 20 19:32:41 PDT 2025; root:xnu-12377.41.6~2/RELEASE_ARM64_T6000 arm64

$make benchmark 
uv run python src/main.py --benchmark
=== Starting Benchmark ===
Running MLX benchmark on CPU...
MLX CPU took: 0.6581 seconds
Running MLX benchmark on GPU...
MLX GPU took: 0.1727 seconds

=== Benchmark Results ===
CPU Time: 0.6581s
GPU Time: 0.1727s
GPU is 3.81x faster than CPU
```

## Learning Outcomes
- Understanding the Apple Metal Performance Shaders (MPS) ecosystem.
- Using `MLX` as a NumPy-like array framework optimized for Apple unified memory.
- Using `Polars` for blazingly fast, multi-threaded DataFrame operations as an alternative to Pandas.

## Content
- **`src/main.py`**: A script generating a synthetic dataset of Australian vehicles, demonstrating `mlx` array math and `polars` data grouping.
- **`docs/`**: Theoretical concepts regarding Apple Metal and unified memory.
- **`images/`**: Screenshots and execution outputs.

For instructions on how to run this project, refer to [QUICKSTART.md](QUICKSTART.md).
