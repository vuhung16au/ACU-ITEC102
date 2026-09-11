# Week 05: Numerical Computing with NumPy

Welcome to Week 05 of ACU-ITEC102. This week introduces **NumPy (Numerical Python)**, the foundational numerical computing engine in Python data science and machine learning. Students learn why vectorized array operations outperform native Python loops, explore the internal structure of the `ndarray`, master multi-dimensional indexing and slicing, filter data using boolean masks, and perform high-speed computations using universal functions (`ufuncs`).

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Understand NumPy's Core Architecture**: Identify why contiguous memory layouts and homogeneous typing enable high-performance vectorized computations.
2. **Benchmark Lists vs Arrays**: Compare execution speed and memory footprints between Python lists and NumPy arrays for mathematical tasks.
3. **Create and Inspect NDArrays**: Instantiate arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()`, inspecting `.shape`, `.ndim`, and `.dtype`.
4. **Master Multi-Dimensional Slicing**: Index and slice 1D and 2D arrays using `[row, column]` syntax and distinguish between view references and deep copies.
5. **Filter Data with Boolean Masks**: Formulate conditional masks (`arr > val`) to filter, subset, and conditionally assign array values without explicit loops.
6. **Execute Vectorized Universal Functions**: Apply element-wise math functions, statistical aggregations (`np.mean()`, `np.sum()`, `np.std()`), and conditional selection via `np.where()`.

---

## Topic Navigation

| Topic | Focus Area | Key NumPy Functions |
| :--- | :--- | :--- |
| [01. Intro to NumPy](01.IntroToNumPy/) | Why NumPy, vectorized operations vs Python loops, basic array math | `np.array()`, vectorized arithmetic |
| [02. Lists vs Arrays](02.ListsVsArrays/) | Performance benchmarking, contiguous memory layout, type homogeneity | Memory inspection, speed comparison |
| [03. The NDArray](03.NDArray/) | Dimensions, shapes, data types, and creation routines | `arr.shape`, `arr.dtype`, `np.zeros()`, `np.ones()`, `np.arange()` |
| [04. Indexing and Slicing](04.IndexingAndSlicing/) | 1D & 2D slicing, row/column selection, views vs copies | `arr[row, col]`, `arr[:, 0]`, sub-array extraction |
| [05. Filtering with Masks](05.FilteringWithMasks/) | Conditional expressions, boolean indexing, element filtering | `mask = arr > val`, `arr[mask]`, compound `&` / `\|` |
| [06. Universal Functions (Ufuncs)](06.Ufuncs/) | Fast element-wise operations, statistical aggregations, conditional branching | `np.mean()`, `np.sum()`, `np.max()`, `np.where()` |

---

## Folder Structure

Each topic folder is structured consistently:
```text
Topic-Folder/
├── notebooks/       # Interactive Jupyter notebooks with step-by-step guidance & exercises
├── src/             # Clean, runnable Python scripts containing all demonstrations
├── docs/            # Conceptual summaries and syntax reference guides
├── Makefile         # Commands to run scripts or launch Jupyter Lab
├── README.md        # Topic-level learning objectives and instructions
└── QUICKSTART.md    # Step-by-step setup and execution guide
```

---

## Recommended Learning Flow
1. Work through the topics sequentially from `01` to `06` to build a solid mental model of NumPy arrays.
2. Run each script in `src/` to observe terminal execution and benchmark metrics.
3. Open the corresponding notebook in `notebooks/` to work through interactive explanations and solve the exercises.
