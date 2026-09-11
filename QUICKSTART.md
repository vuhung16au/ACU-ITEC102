# Quickstart Guide

Welcome to the **ITEC102 Python Projects** repository!

In this course, we use **`make`** to automate project setup, dependency management, code execution, and quality checks.

Instead of running lengthy and error-prone "raw" Python commands (such as manually creating virtual environments, activating platform-specific shell scripts, installing libraries with pip, or typing long file paths), `make` provides simple, consistent commands that automate these tasks for you.

---

## 1. Prerequisites

Before running commands, ensure you have:

1. **Python 3.10+** (Python 3.14 recommended) installed on your system.
2. **`uv`** installed (a modern, high-performance Python package and environment manager):
   - **macOS / Linux:**
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   - **Windows (PowerShell):**
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```
3. A terminal that supports `make`:
   - **macOS / Linux:** Built-in Terminal (if prompted on macOS, install developer tools using `xcode-select --install`).
   - **Windows:** **Git Bash** (included with Git for Windows) or **WSL** (Windows Subsystem for Linux).

---

## 2. Quickstart with `make` (Recommended Approach)

All commands are run from the root folder of this repository (`ACU-ITEC102`).

### Step 1: View Available Commands (`make help`)
To see the full list of automated tasks:
```bash
make help
```
Output:
```text
Available commands in ACU-ITEC102:
  make check         - Run all checks (check-py and check-ipynb) across Weeks 01-12
  make check-py      - Validate comments and error-free execution of all .py files
  make check-ipynb   - Validate structure and error-free execution of all .ipynb notebooks
  make run           - Execute all Python scripts and Jupyter notebooks across Weeks 01-12
  make run-py        - Execute all Python scripts and display program output
  make run-ipynb     - Execute all Jupyter notebooks and display output
  make venv          - Create and provision the .venv virtual environment using uv
  make clean         - Clean up working virtual environment (.venv) and Python caches
  make distclean     - Full reset: run clean and delete .venv_global (alias: clean-all)
  make clean-all     - Alias for make distclean

Tip: Run for a specific week with WEEK=WeekXX (e.g., make check-py WEEK=Week04)
```

---

### Step 2: Set Up the Environment (`make venv`)
Provision the course virtual environment with all required packages (Jupyter, Pandas, Matplotlib, NumPy, etc.) with one command:
```bash
make venv
```
> **What this does automatically:**
> - Creates a isolated `.venv` environment using `uv`.
> - Installs all necessary dependencies from `requirements.txt` (or links to `.venv_global` if present).
> - No manual `python -m venv` or individual `pip install` commands required!

---

### Step 3: Run Code Quality Checks (`make check`)
Before submitting your work, run automated checks to ensure your code is error-free and well-commented:

* **Check everything across Weeks 01–12:**
  ```bash
  make check
  ```
* **Check only Python scripts (`.py`):**
  Validates syntax, ensures required educational comments/docstrings are present, and tests execution:
  ```bash
  make check-py
  ```
* **Check only Jupyter Notebooks (`.ipynb`):**
  Ensures notebooks have explanatory markdown cells and execute without runtime errors:
  ```bash
  make check-ipynb
  ```
* **Check a specific week only:**
  Add `WEEK=WeekXX` to filter:
  ```bash
  make check-py WEEK=Week04
  make check-ipynb WEEK=Week04
  ```

---

### Step 4: Execute Scripts and Notebooks (`make run`)

* **Run all Python scripts and notebooks across the course:**
  ```bash
  make run
  ```
* **Run only Python scripts and see output:**
  ```bash
  make run-py
  ```
* **Run only a specific week:**
  ```bash
  make run-py WEEK=Week01
  make run-ipynb WEEK=Week06
  ```

---

### Step 5: Clean Up (`make clean` vs `make distclean`)

* **Standard cleanup (`make clean`):**
  Removes temporary working environments (`.venv`), Python `__pycache__` directories, `.pytest_cache`, and checkpoint files while preserving the global package cache for fast subsequent runs:
  ```bash
  make clean
  ```
* **Full reset (`make distclean` or `make clean-all`):**
  Runs `make clean` and also deletes `.venv_global` for a complete, from-scratch reset:
  ```bash
  make distclean
  # or
  make clean-all
  ```

---

## 3. Why Use `make` Instead of Raw Python Commands?

Here is a side-by-side comparison of common workflows:

| Task | With `make` (Recommended) | Traditional / Raw Python Commands |
| :--- | :--- | :--- |
| **Create Environment** | `make venv` | `python3 -m venv venv` |
| **Activate Environment** | *Automatic* in all `make` targets | `source venv/bin/activate` *(macOS/Linux)*<br>`venv\Scripts\activate` *(Windows)* |
| **Install Dependencies** | *Automatic* via `make venv` | `pip install -r requirements.txt` |
| **Validate Code & Comments** | `make check-py WEEK=Week03` | Manually inspect files and run each script |
| **Run All Exercises** | `make run-py WEEK=Week02` | Manually run each `.py` file one by one |
| **Clean Caches & Build Files** | `make clean` | Manually search and delete `__pycache__`, `.pytest_cache`, etc. |

---

## 4. Interactive Jupyter Notebooks

When you want to open and interactively edit `.ipynb` notebooks in your browser:

1. **Activate the project environment:**
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **Windows (Git Bash):**
     ```bash
     source .venv/Scripts/activate
     ```
2. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```
   *(or `jupyter lab`)*
3. In the browser interface, navigate to the topic notebook (e.g., `Week01/01.Introduction/notebooks/...`).
4. Verify that the notebook kernel is set to **Python (.venv)**.

---

## 5. Alternative: Running Individual Python Scripts Manually (Reference)

If you need to test or debug an individual Python script directly:

1. Activate your environment:
   ```bash
   source .venv/bin/activate   # macOS / Linux
   ```
2. Run the script using its path from the root directory:
   ```bash
   python Week01/01.Introduction/src/hello_world.py
   ```
   *(Or navigate into the subfolder: `cd Week01/01.Introduction/src && python hello_world.py`)*
