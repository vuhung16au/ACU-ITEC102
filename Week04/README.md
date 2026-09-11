# Week 04: Functions and File Handling

Welcome to Week 04 of ACU-ITEC102. This week transitions from linear scripting to modular, reusable code architectures by exploring **Function Definitions**, **Argument and Parameter Mechanics**, **Variable Scope (LEGB Rule)**, **Higher-Order Functions and Lambdas**, **Safe File I/O**, and synthesizing these techniques into a **Survey Data Mini-Project**.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Define Modular Functions**: Construct reusable functions using `def`, return single and multiple values, and document interfaces with informative docstrings.
2. **Pass Arguments Dynamically**: Differentiate between positional, default, and keyword arguments to build flexible function signatures.
3. **Navigate Variable Scope**: Distinguish between local and global namespaces, understand the LEGB lookup rule, and avoid unintentional side effects.
4. **Apply Anonymous Functions (Lambdas) & Map**: Implement concise inline `lambda` expressions and transform data using higher-order functions like `map()`.
5. **Perform Safe File Input/Output**: Read from and write to external text files using the `with open(...)` context manager and implement robust `try...except FileNotFoundError` error handling.
6. **Build an End-to-End Survey Pipeline**: Coordinate functions and persistent file storage to record, append, and analyse user survey responses.

---

## Topic Navigation

| Topic | Focus Area | Key Concepts & Functions |
| :--- | :--- | :--- |
| [01. Defining and Calling Functions](01.Defining_and_Calling_Functions/) | Function declaration, parameter lists, return statements, and docstrings | `def`, `return`, docstring standards |
| [02. Arguments and Parameters](02.Arguments_and_Parameters/) | Positional parameters, default arguments, and named keyword calls | `func(val)`, `func(arg=val)`, default parameter ordering |
| [03. Variable Scope](03.Variable_Scope/) | Local vs global namespaces, variable lifetime, and LEGB rule | Local variables, `global`, function scope encapsulation |
| [04. Advanced Functions (Map and Lambda)](04.Advanced_Functions_Map_Lambda/) | Anonymous functions, functional programming, mapping iterables | `lambda x: ...`, `map()`, functional transformations |
| [05. File Handling](05.File_Handling/) | Reading, writing, and appending files; context managers; exception handling | `open()`, `with open(...) as f:`, modes `'r'`, `'w'`, `'a'` |
| [06. Mini-Project: Survey Data](06.Mini_Project_Survey_Data/) | Applied file persistence and modular function coordination | Data collection, file appending, survey response processing |

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
1. Work through topics `01` to `04` sequentially to master functional programming fundamentals.
2. Study `05.File_Handling` to master reading and writing files safely.
3. Run each script in `src/` to observe terminal execution.
4. Open the corresponding notebook in `notebooks/` to work through interactive explanations and solve the exercises.
5. Complete `06.Mini_Project_Survey_Data` to synthesize functions and file storage into a working application.
