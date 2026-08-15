# NVIDIA CUDA Ecosystem

NVIDIA provides a mature GPU acceleration ecosystem for data science through RAPIDS and CuPy.

## CuPy (NumPy on GPU)
CuPy is a library that implements the NumPy API on NVIDIA GPUs. By acting as a drop-in replacement, you can accelerate matrix math and linear algebra operations with minimal code changes. Data is moved from the host (CPU) memory to device (GPU) memory, operated on in parallel across thousands of CUDA cores, and then moved back if necessary.

## cuDF (Pandas on GPU)
cuDF is a part of the RAPIDS suite. It mimics the Pandas API but runs operations on the GPU. For zero code changes, RAPIDS provides `cudf.pandas`, which automatically intercepts Pandas operations and executes them on the GPU if possible, falling back to the CPU only when necessary.
