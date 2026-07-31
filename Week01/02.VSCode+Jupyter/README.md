# Week 01 — Python Development with VS Code & Jupyter Notebook

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) is a powerful, free code editor with excellent Python and Jupyter Notebook support. This guide will help you run Jupyter Notebooks locally on your machine.

---

## Topics

### 1. Setup VS Code (Revisit Week 00)

If you haven't set up VS Code yet, revisit the Week 00 guide:

- 🔗 [Week 00 — VS Code Setup](https://github.com/vuhung16au/ACU-ITEC102/blob/main/Week00/02.VSCode.md)

**Quick start checklist:**
- [ ] VS Code is installed on your machine
- [ ] The **Python** extension (`ms-python.python`) is installed
- [ ] The **Jupyter** extension (`ms-toolsai.jupyter`) is installed
- [ ] A Python interpreter is selected (`Ctrl/Cmd + Shift + P` → `Python: Select Interpreter`)

---

### 2. Run Your First Jupyter Notebook in VS Code

- 🔗 [Official Guide: Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

**Steps to create and run your first notebook:**

1. **Open VS Code**
2. **Create a new file** with the `.ipynb` extension, e.g., `hello_world.ipynb`
   - Or use the Command Palette: `Ctrl/Cmd + Shift + P` → `Create: New Jupyter Notebook`
3. **Select a kernel** — choose your Python interpreter from the top-right corner of the notebook
4. **Add a code cell** and type your code
5. **Run the cell** by clicking ▶ or pressing `Shift + Enter`

---

## ✅ Verification

Create a new notebook file (`hello_itec102.ipynb`) and run the following code in a code cell:

```python
print("Hello ITEC102")
```

**Expected output:**
```
Hello ITEC102
```

Confirm you see the output displayed directly below the cell. ✅

---

## 💡 VS Code + Jupyter Tips

| Shortcut | Action |
|----------|--------|
| `Shift + Enter` | Run current cell and move to next |
| `Ctrl + Enter` | Run current cell and stay |
| `A` (command mode) | Insert cell above |
| `B` (command mode) | Insert cell below |
| `DD` (command mode) | Delete current cell |
| `M` (command mode) | Convert cell to Markdown |
| `Y` (command mode) | Convert cell to code |
| `Esc` | Enter command mode |
| `Enter` | Enter edit mode |

> **Tip:** Click outside a cell to enter command mode, then use the keyboard shortcuts above.

---

## 🗂 Recommended Workflow

```
project/
├── data/               # Raw data files
├── notebooks/          # Jupyter notebooks (.ipynb)
│   └── hello_world.ipynb
├── src/                # Python source files (.py)
└── requirements.txt    # Project dependencies
```

1. Keep notebooks in a dedicated `notebooks/` folder
2. Use notebooks for exploration and visualization
3. Refactor reusable code into `.py` modules in `src/`

---

## 📚 Additional Resources

- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Working with Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
