# Week 03: Data Structures in Python

Welcome to Week 03 of ACU-ITEC102. This week explores Python's core collection data structures: ordered and mutable **Lists**, immutable **Tuples**, unique and unordered **Sets**, associative key-value **Dictionaries**, concise **Comprehensions**, and applies them to build a practical **Student Enrolment Mini-Project**.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Manipulate Ordered Sequences (Lists)**: Create, index, slice, and mutate lists using methods such as `append()`, `insert()`, `remove()`, and `pop()`.
2. **Utilise Immutable Sequences (Tuples)**: Understand tuple immutability, apply tuple packing and unpacking, and safeguard constant data collections.
3. **Perform Set Operations**: Deduplicate collections and apply mathematical set operations including union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).
4. **Structure Associative Data (Dictionaries)**: Model records using key-value mappings, safely retrieve values with `.get()`, and iterate through keys, values, and items.
5. **Construct Expressive Comprehensions**: Write compact list, set, and dictionary comprehensions with conditional filtering.
6. **Build Practical Data Solutions**: Combine dictionaries, sets, and lists to develop an end-to-end student enrolment and course allocation system.

---

## Topic Navigation

| Topic | Focus Area | Key Concepts & Functions |
| :--- | :--- | :--- |
| [01. Lists](01.Lists/) | Ordered mutable sequences, indexing, negative indexing, slicing, and list methods | `list.append()`, `insert()`, `remove()`, `pop()`, `sort()`, `len()` |
| [02. Tuples](02.Tuples/) | Ordered immutable sequences, tuple packing/unpacking, fixed records | `tuple()`, `(x, y)`, unpacking `lat, lon = coords` |
| [03. Sets](03.Sets/) | Unordered collections of unique items, deduplication, set algebra | `set()`, `.add()`, `.remove()`, union (`\|`), intersection (`&`), difference (`-`) |
| [04. Dictionaries](04.Dictionaries/) | Key-value data mapping, nested dictionaries, record mutation | `dict[key]`, `.get()`, `.keys()`, `.values()`, `.items()` |
| [05. Comprehensions](05.Comprehensions/) | Concise syntax for generating lists, sets, and dictionaries with conditionals | `[x**2 for x in seq if cond]`, `{k: v for ...}` |
| [06. Mini-Project: Student Enrolment](06.Mini-Project-Student-Enrolment/) | Comprehensive application combining dictionaries and sets | Course enrolment management, student lookups, roster queries |

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

Additionally, the [`src/`](src/) folder at the root of Week 03 contains standalone script equivalents of all weekly topics and mini-projects.

---

## Recommended Learning Flow
1. Work through topics `01` through `05` sequentially to master each foundational data structure.
2. Run each script in `src/` to observe terminal execution.
3. Open the corresponding notebook in `notebooks/` to work through the interactive explanations and solve the exercises.
4. Complete `06.Mini-Project-Student-Enrolment` to synthesize your skills into a cohesive application.
