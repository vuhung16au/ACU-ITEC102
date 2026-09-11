# Week 01: Python Foundations and Development Environments

Welcome to Week 01 of ACU-ITEC102. This week provides a hands-on refresher on fundamental Python programming concepts and introduces three industry-standard development environments: cloud-hosted notebooks with **Google Colab**, local development with **VS Code & Jupyter**, and containerised workflows using **Docker**.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Understand Core Python Syntax**: Run fundamental Python statements, declare variables, perform arithmetic operations, and manipulate basic lists.
2. **Develop in the Cloud with Google Colab**: Navigate Google Colab, execute interactive notebook cells, connect to remote runtimes, and save work without local installation.
3. **Configure Local Development with VS Code & Jupyter**: Set up Visual Studio Code with the Python and Jupyter extensions, select Python interpreters, and execute `.ipynb` notebooks locally.
4. **Run Containerised Environments with Docker**: Launch a reproducible Jupyter Notebook server using Docker and Docker Compose with zero local dependency conflicts.
5. **Evaluate Development Workflows**: Compare cloud, local, and containerised environments to choose the right setup for coursework, data analysis, and collaboration.

---

## Topic Navigation

| Topic | Focus Area | Key Concepts & Tools |
| :--- | :--- | :--- |
| [00. Python Refresher (W3Schools)](00.w3schools/) | Core syntax review, variables, scalar types, operators, and basic lists | `print()`, `type()`, `int()`, `float()`, `len()`, basic lists |
| [01. Google Colab](01.Google-Colab/) | Cloud-based interactive computing, zero-install setup, and cloud kernels | Colab runtimes, code/markdown cells, Google Drive integration |
| [02. VS Code & Jupyter](02.VSCode+Jupyter/) | Local IDE configuration, Python interpreter selection, and interactive notebooks | VS Code Command Palette, Jupyter kernel, keyboard shortcuts |
| [03. Docker & Jupyter](03.docker+Jupyter/) | Containerised Jupyter server, reproducible environments, and port forwarding | `docker compose up`, port mapping `8888:8888`, volume mounts |

---

## Folder Structure

This week is organised into dedicated environment and concept guides:
```text
Week01/
├── 00.w3schools/         # Python syntax refresher with W3Schools examples
│   ├── src/              # Standalone Python scripts demonstrating core syntax
│   └── README.md         # Syntax refresher guide and quick reference
├── 01.Google-Colab/      # Cloud-based development setup and exercises
│   ├── src/              # Sample Python script for Colab workflows
│   └── README.md         # Step-by-step Colab walkthrough
├── 02.VSCode+Jupyter/    # Local VS Code and Jupyter Notebook setup
│   ├── src/              # Sample Python script for local execution
│   └── README.md         # Configuration guide and extension setup
└── 03.docker+Jupyter/    # Containerised Jupyter environment via Docker
    ├── images/           # Architecture diagrams and UI screenshots
    ├── notebooks/        # Sample starter notebook (hello_itec102.ipynb)
    ├── src/              # Sample Python script for Docker workflows
    ├── docker-compose.yml# Container orchestration configuration
    └── README.md         # Docker execution instructions
```

---

## Recommended Learning Flow
1. Complete the Python refresher in [00.w3schools/](00.w3schools/) to review variables, operations, and lists.
2. Test running code in the cloud via [01.Google-Colab/](01.Google-Colab/) for an immediate, zero-install experience.
3. Configure your primary local environment following [02.VSCode+Jupyter/](02.VSCode+Jupyter/) for day-to-day development.
4. *(Optional / Advanced)* Explore containerised development with [03.docker+Jupyter/](03.docker+Jupyter/) to understand how reproducible environments work.
5. Verify your setup by executing `print("Hello ITEC102")` in your chosen environment.
