# 21. Python on CUDA

This example project demonstrates how to leverage NVIDIA GPUs to dramatically speed up data science workflows using Python. 

## Learning Outcomes
- Understanding how to offload computations from CPU to GPU.
- Using `CuPy` as a drop-in replacement for `NumPy` for accelerated array operations and matrix math.
- Using `cuDF` (part of RAPIDS) to execute `Pandas` DataFrame operations directly on the GPU.

## Content
- **`src/main.py`**: A script that generates a synthetic dataset of Australian vehicles and processes it using both CuPy and cuDF.
- **`docs/`**: Theoretical concepts regarding CUDA and GPU acceleration.
- **`images/`**: Screenshots and execution outputs.

For instructions on how to run this project, refer to [QUICKSTART.md](QUICKSTART.md).
