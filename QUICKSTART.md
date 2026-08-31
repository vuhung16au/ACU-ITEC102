# Quickstart Guide

Welcome to the ITEC102 Python Projects repository! This guide will help you set up your Python environment and show you how to run the code and notebooks in this repository.

## 1. Setting up a Python Virtual Environment

A virtual environment keeps your project's dependencies (like installed libraries) separate from other Python projects on your computer. This ensures everything runs smoothly without conflicts.

### Step 1: Create the Virtual Environment
Open your terminal (or Command Prompt/PowerShell on Windows), make sure you are in the root folder of this repository (`ACU-ITEC102`), and run the following command:

**On macOS and Linux:**
```bash
python3 -m venv venv
```

**On Windows:**
```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment
You need to activate the environment every time you open a new terminal to work on the project.

**On macOS and Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You will know it is activated successfully when you see `(venv)` at the beginning of your command prompt.

### Step 3: Install Required Packages
Once activated, install Jupyter and any other required libraries so you can run the notebooks:
```bash
pip install jupyterlab ipykernel
```
*(Note: If the repository later includes a `requirements.txt` file, you can install all dependencies at once by running `pip install -r requirements.txt`)*

---

## 2. Running Jupyter Notebooks

Many lessons and exercises in this repository are provided as Jupyter Notebooks (`.ipynb` files). To open and run them using your virtual environment:

1. Make sure your virtual environment is activated (see Step 2 above).
2. Register your virtual environment so Jupyter knows to use it:
   ```bash
   python -m ipykernel install --user --name=venv --display-name "Python (ITEC102 venv)"
   ```
3. Start the Jupyter Notebook server:
   ```bash
   jupyter notebook
   ```
   *(Alternatively, you can use `jupyter lab`)*
4. Your web browser will automatically open. Navigate to the folder containing the notebook you want to view and click on it.
5. In the top right corner of the notebook, make sure the kernel is set to **Python (ITEC102 venv)**. If it isn't, you can change it by going to **Kernel -> Change Kernel -> Python (ITEC102 venv)**.

---

## 3. Running Python Scripts

Each week's topic is organized into folders following the pattern `WeekXX/YY.<topicName>/`. The actual Python script files (`.py` files) are located inside the `src/` subfolders.

To run a Python script, you have two options:

### Option A: Run from the root folder
You can provide the full path to the script from the root of the repository:
```bash
python WeekXX/YY.<topicName>/src/filename.py
```
*Example:*
```bash
python Week01/01.Introduction/src/hello_world.py
```

### Option B: Navigate to the folder first
You can change your directory to the specific `src` folder, and then run the script directly:
```bash
cd WeekXX/YY.<topicName>/src/
python filename.py
```

> **Note:** Some topic folders might not have a `src/` folder yet. These will be added as the course progresses!
