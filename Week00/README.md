# ITEC102 - Week 00 — Setting Up Your Development Environment

Welcome to Week 00! Before writing any Python code, you need to set up your tools. Work through the guides below in order — each one builds on the previous.

---

## Guides

### [`00.Python.md`](./00.Python.md) — Install Python

Install **Python 3.14** on Windows, macOS, or Linux. Covers downloading from [python.org](https://www.python.org/downloads/), using Homebrew on macOS, and verifying the installation with `python3 --version`.

### [`01.GitHub.md`](./01.GitHub.md) — Git, GitHub & the `gh` CLI

Install Git and the GitHub CLI (`gh`), configure your identity for commits, authenticate with GitHub, and learn the essential Git commands (`clone`, `add`, `commit`, `push`, `pull`).

### [`02.VSCode.md`](./02.VSCode.md) — VS Code Setup

Install [Visual Studio Code](https://code.visualstudio.com/) and the **Python** and **Jupyter** extensions. Covers selecting a Python interpreter and running your first `.py` file and Jupyter Notebook inside VS Code.

### [`03.Python-venv.md`](./03.Python-venv.md) — Python Virtual Environments

Create and activate an isolated virtual environment with `python3 -m venv .venv` so that project dependencies don't conflict with your system Python. Includes best practices like adding `.venv/` to `.gitignore`.

### [`04.Python-Libraries.md`](./04.Python-Libraries.md) — Managing Python Libraries

Install the core course libraries — **pandas**, **numpy**, **matplotlib**, **seaborn**, and **scikit-learn** — using either `pip` or the faster `uv` package manager. Also covers `requirements.txt` and `pyproject.toml` for dependency management.

### [`05.docker.md`](./05.docker.md) — Docker for Python Development

Install **Docker Desktop** and use `docker compose` to run Python scripts and Jupyter Notebooks inside isolated containers. No local Python installation required — the container provides everything.

### [`06.Google-Colab.md`](./06.Google-Colab.md) — Google Colab

Use [Google Colab](https://colab.research.google.com/) as a free, cloud-based Jupyter environment with all major libraries pre-installed. Covers the recommended **GitHub + Colab** workflow for version control and collaboration, and notes [Kaggle Notebooks](https://www.kaggle.com/code) as a useful alternative.

---

## Verification Checklist

By the end of Week 0, you should be able to check each of these off:

- [ ] `python3 --version` prints `Python 3.14.x`
- [ ] `git --version` and `gh auth status` both succeed
- [ ] VS Code opens a `.py` file and runs it with `F5`
- [ ] A virtual environment activates and `pip list` shows only its packages
- [ ] `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn` import without errors
- [ ] `docker compose up` starts a container successfully
- [ ] Google Colab opens a notebook and runs a code cell
