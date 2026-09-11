# ACU-ITEC102: Python Fundamentals for Data Science

Welcome to the **ACU-ITEC102** course repository! This repository provides supplementary teaching and learning materials for the **ITEC102** unit at Australian Catholic University (ACU).

Designed specifically for first-year Computer Science and Information Technology students, this repository offers practical, hands-on code examples, modular weekly lab exercises, and self-contained projects to build a strong foundation in Python programming and introductory data science.

---

## Where to Start

If you are new to this repository or setting up your development workspace for the first time, follow these steps:

1. **Read the Quickstart Guide**: Check out [QUICKSTART.md](QUICKSTART.md) for complete instructions on system requirements, package management with `uv`, and using our automated `make` workflow.
2. **Complete Week 00**: Go through the setup guides in [Week00/](Week00/) to install and configure Python 3.10+, Git/GitHub, Visual Studio Code, and virtual environments.
3. **Set Up the Virtual Environment**: From the root of this repository, run:
   ```bash
   make venv
   ```
   This automatically provisions an isolated `.venv` environment containing all required libraries (NumPy, Pandas, Matplotlib, Jupyter, etc.).
4. **Follow the Weekly Modules**: Work through each weekly folder in sequential order ([Week01/](Week01/) through [Week12/](Week12/)).
5. **Verify and Run Your Code**: Use our built-in test and execution targets:
   ```bash
   make check         # Run syntax, comment, and notebook validation
   make run           # Execute Python scripts and Jupyter notebooks
   make help          # View all available make targets
   ```

---

## Repository Structure

The repository is organised into modular weekly folders, supplementary enrichment tracks, and automated developer tooling:

```text
ACU-ITEC102/
├── README.md               # Repository overview and starting guide (this file)
├── QUICKSTART.md           # Step-by-step setup and command reference (make workflow)
├── AGENTS.md               # Repository guidelines and educational principles
├── Makefile                # Automated commands for environment setup, testing, and execution
├── requirements.txt        # Course Python dependencies
├── scripts/                # Verification and execution scripts for make targets
│   ├── check_py.py         # Python script validator
│   ├── check_ipynb.py      # Jupyter notebook validator
│   ├── run_py.py           # Script test runner
│   └── run_ipynb.py        # Notebook test runner
├── Week00/                 # Environment setup guides (Python, Git, VS Code, uv, Docker)
├── Week01/ – Week12/       # Core weekly curriculum modules (scripts, notebooks, exercises)
└── Enrichment/             # Advanced elective projects beyond the core syllabus
    ├── Data-Engineering/   # ETL, dashboards, and NoSQL projects
    ├── Data-Science/       # Real-world data analytics and visualisation projects
    ├── Machine-Learning/   # APIs, LLMs, and gradient boosting models
    └── Systems-and-Performance/ # Hardware acceleration (CUDA, Apple Metal)
```

---

## Weekly Modules (`Week XX`)

The core syllabus is structured across 13 weekly learning modules:

| Week | Title / Topic | Focus Areas |
| :--- | :--- | :--- |
| **[Week 00](Week00/)** | **Environment Setup** | Installing Python, Git/GitHub, VS Code, virtual environments, `uv`, and Docker |
| **[Week 01](Week01/)** | **Foundations & Tooling** | Python basics, interactive environments (Colab, VS Code + Jupyter, Docker) |
| **[Week 02](Week02/)** | **Python Language Basics** | Syntax semantics, scalar types, operators, conditionals, loops, and string handling |
| **[Week 03](Week03/)** | **Data Structures** | Lists, tuples, sets, dictionaries, comprehensions, and student enrolment mini-project |
| **[Week 04](Week04/)** | **Functions & Files** | Defining functions, parameter passing, variable scope, lambdas, and file I/O |
| **[Week 05](Week05/)** | **Numerical Computing (NumPy)** | Arrays vs lists, NDArray operations, slicing, boolean masks, and universal functions |
| **[Week 06](Week06/)** | **Data Analysis (Pandas)** | Series and DataFrame fundamentals, indexing, reindexing, and data manipulation |
| **[Week 07](Week07/)** | **Data Input/Output & Exploration** | Reading and writing CSV/Excel/JSON files, summarising, and filtering datasets |
| **[Week 08](Week08/)** | **Data Cleaning & Preprocessing** | Handling missing data, imputation, binning, and data sampling techniques |
| **[Week 09](Week09/)** | **Advanced Data Wrangling** | Hierarchical indexing, merging, database-style joins, pivoting, and melting |
| **[Week 10](Week10/)** | **Data Aggregation & GroupBy** | Split-apply-combine, multi-level aggregation, custom functions, and pivot tables |
| **[Week 11](Week11/)** | **Data Visualisation** | Plotting with Matplotlib and Pandas: line plots, bar charts, histograms, and styling |
| **[Week 12](Week12/)** | **Real-World Wrangling & Capstone** | End-to-end data analysis, data ethics, anonymisation, bias, and capstone project |

Each week contains detailed instructional materials, self-contained Python scripts (`.py`), interactive notebooks (`.ipynb`), and challenge exercises.

---

## `Enrichment` Folder

The [`Enrichment/`](Enrichment/) directory hosts optional, supplementary projects designed to extend your learning beyond the standard ITEC102 curriculum.

> [!NOTE]
> Projects in the `Enrichment` folder are **not mandatory** for completing the unit. They are elective sandboxes created for students who wish to challenge themselves, build impressive portfolio projects, and gain exposure to modern industry workflows.

The enrichment tracks cover four primary domains:

1. **[Data Engineering](Enrichment/Data-Engineering/)**: Web scraping ETL pipelines, real-time analytics dashboards, and NoSQL document storage.
2. **[Data Science](Enrichment/Data-Science/)**: Australian vehicle analytics, Sydney UV index tracking, interactive geospatial maps with Plotly, and energy data cleaning.
3. **[Machine Learning](Enrichment/Machine-Learning/)**: Large Language Model (LLM) API integration, machine learning model serving via web APIs, and gradient boosting algorithms.
4. **[Systems and Performance](Enrichment/Systems-and-Performance/)**: GPU-accelerated computing using Python CUDA and Apple Metal (MPS).

Every enrichment project includes its own self-contained `README.md` and `QUICKSTART.md` explaining prerequisites and execution steps.

---

## Additional Resources & Guidelines

- **Quickstart Guide**: Refer to [QUICKSTART.md](QUICKSTART.md) for full commands and troubleshooting tips.
- **Repository Guidelines**: Consult [AGENTS.md](AGENTS.md) for coding conventions, documentation standards, and repository guidelines.
- **License**: This project is licensed under the terms described in the [LICENSE](LICENSE) file.
