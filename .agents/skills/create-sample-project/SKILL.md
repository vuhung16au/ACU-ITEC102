---
name: create-sample-project
description: Creates a new sample project in the repository based on a project number and learning objective, automatically adhering to the ACU-ITEC102 structural guidelines.
---

# Create New Sample Project Skill

This skill automates the creation of a new, standalone example project for the ACU-ITEC102 unit. These projects are intended for students to learn programming concepts using Python.

## Inputs Required from User

When the user invokes this skill, ensure you have the following information:
1. **Project Number**: The numeric prefix for the project folder (e.g., `01`, `02`). If the user does not provide one, you should analyze the root directory to find the next available project number, or default to `01` if none exist.
2. **Objective (Learning Outcome)**: A description of what the project will showcase (e.g., "Create a dashboard for Australian vehicles, including plotting charts showing trends of new registrations by states and territories, and average age of vehicles by fuel type").

If the user does not provide the objective, ask them for the missing information before proceeding.

## Tech Stack Preferences

We use `Python` ecosystem in this project. We prefer Python 3.14 (which is the currently installed version).

node.js/react/next.js are only used for frontend if needed. In this case, we can use `Next.js` for frontend development, and Python for the backend.

We prefer: 
- **Versions**: For Python, `npm`, and other package managers/tools, prefer to use "fixed" latest and stable versions instead of "latest".

-  **Web Framework**: `Flask` or `FastAPI` for web backend development.
-  **Database**: `PostgreSQL`, `MySQL`, or `SQLite` for relational databases, and `MongoDB` for NoSQL databases. Always provide a Web UI for the database (e.g., `pgadmin` for PostgreSQL, `mongo-express` for MongoDB).
-  ORM: `Django ORM` or `SQLAlchemy` for database interactions, but avoid using ORMs if the learning objective is to demonstrate raw SQL queries.
- **Frontend**: `HTML`, `CSS`, and `JavaScript` for frontend development. Prefer Python-based solutions if possible. If the learning objective requires a more complex frontend, consider using `React` or `Next.js`. For simple project, use can `Jinja2` templates for dynamic HTML rendering. 
- Javascript: Use `vanilla JS` for simple projects, and `React` or `Next.js` for more complex frontend requirements.
- Style libraries: Use `Bootstrap` or `Tailwind CSS` for styling, but avoid heavy frontend frameworks unless necessary for the learning objective.
- (prefer to use docker, but not mandatory) **Containerization**: Use `Docker` and `docker-compose` to containerize the application and its dependencies. Ensure that the `docker-compose.yaml` file is well-documented and includes all necessary services (e.g., web server, database, Web UI). Prefer to use "fixed" versions for Docker images, not "latest".
- When using postgres, always use `pgadmin` as the Web UI (reduce the complexity). When using MongoDB, always use `mongo-express` as the Web UI.
- `streamlit` can be used for simple data science dashboards, but avoid using it for complex web applications. Use `Flask` or `FastAPI` instead.

For data science, we prefer: 
- `pandas` for data manipulation and analysis.
- `numpy` for numerical computations.
- `matplotlib` or `seaborn` (recommended), or `plotly` for data visualization.
- `scikit-learn` for machine learning.
- `pytorch` or `tensorflow` for deep learning (if the learning objective requires it).

Enrichment libs can include: 
- `Polars` for fast data manipulation (if the learning objective requires it).
- `pydantic` for data validation and settings management (if needed). This is an enrichment library


For package mangement, we prefer:
- `uv` and `pyproject.toml` for dependency management and packaging. Avoid using `pipenv` or `poetry` unless necessary for the learning objective.
- `requirements.txt` can be used for simple projects, but prefer `pyproject.toml` for more complex projects.
- `DuckDB`: can be used for in-memory analytics and data processing, but avoid using it for complex projects unless necessary for the learning objective.
- `numba`: can be used for accelerating numerical computations, but avoid using it for complex projects unless necessary for the learning objective.

Because this unit ITEC102 is an introductory programming course about Python for data science, you can also introduce scikit-learn, Pytorch, or TensorFlow if the learning objective is about machine learning or deep learning. But avoid using these libraries too deep, just use them to demonstrate the learning objective.

## Execution Steps

### Create `<root>/AGENTS.md` and says 

- this repo is about Python programming for ITEC102 students (first year CS students), and the projects are designed to be simple, educational, and engaging. The projects should be structured according to the guidelines in this document.
- Python is the primary programming language used in this repository, and all projects should be implemented using Python. The projects should be designed to teach students how to use Python to solve real-world problems, and should be structured in a way that is easy for students to understand and follow.
- Comment the code and provide documentation in the project files to help students understand the purpose and functionality of each component. The documentation should be clear, concise, and easy to follow, and should include examples and explanations of key concepts.
- While maintaining the code quality and readability, the projects should be designed to be simple and easy to understand. Avoid using complex frameworks or design patterns unless they are necessary for the learning objective. The projects should be structured in a way that is easy for students to follow, with clear separation of concerns and modular design.
- All folders/projects should have a `README.md` file that provides an overview of the project, and `QUICKSTART.md` file that provides step-by-step instructions on how to run, connect to, and interact with the project. 

### 1. Determine Folder Name

*   Generate a concise, short name for the project based on the user's objective. (e.g., "querying a sqlite database and show it on a web browser" becomes `Sqlite-RawQuery` or `Sqlite-WebBrowser`).
*   Combine the project number and short name to form the new folder path at the root of the workspace: `<Project Number>.<ProjectShortName>` (e.g., `01.Sqlite-RawQuery`).

### 2. Scaffold the Project Structure

You MUST adhere to the structural guidelines defined in `<root>/AGENTS.md` and keep the project simple, educational, and engaging. Make sure to provide comprehensive documentation and comments (inline or files).

Create the following files and directories within the new project folder:

*   **`docs/`**: Create this folder and populate it with 1-2 markdown files that briefly describe the key theoretical concepts covered in the example.
*   **`images/`**: Create this folder to contain screenshots and screencasts of the project. Include a file `images/README.md` in this folder stating its purpose.
*   **`README.md`**: An overview of the example folder, its purpose, and the learning outcomes. Mention that screenshots and screencasts can be found in the `images` directory.
*   **`QUICKSTART.md`**: Step-by-step instructions on how to run, connect to, and interact with the example. **Important:** Always include documentation on how to access and use the database Web UI.
*   (if we use docker in the project): **`docker-compose.yaml`**: Must be used to define the environment. 
    *   **Web UI**: When spinning up a database, ALWAYS provide a Web UI service alongside it (e.g., `postgres` + `pgadmin`, `mongodb` + `mongo-express`).
    *   **Container Names**: Container names MUST be unique across the repository to prevent conflicts. Always add `<Project Number>-<ProjectShortName>` as a suffix to all `container_name` fields (e.g., `postgres-db-01-Sqlite-RawQuery`).
*   **`Makefile`**: Create a `Makefile` to manage the project lifecycle. It MUST include:
    *   `make up`: to bring up the Docker containers (e.g., `docker compose up -d`).
    *   `make down`: to bring down the Docker containers (e.g., `docker compose down`).
    *   `make test` or `make e2e`: to run the minimum e2e tests.
    *   `make clean`: to clean the project (e.g., remove `.venv`, Python cache directories like `__pycache__` and `.pytest_cache`, and Next.js/Node modules like `node_modules` and `.next`) to save space.
    *   *If Next.js*: Implement `make deploy` (alias to `make deploy-vercel`) to easily deploy the project on Vercel. Make sure the Next.js setup is Vercel-friendly.
*   (if we have a database in the project) **`init-scripts/`**: SQL/NoSQL scripts with DDL and DML that automatically run on database startup. **Always initialize the database with synthetic sample/mock data.**
*   **Tests**: Implement minimum end-to-end (e2e) tests to verify the core functionality.
*   **`.gitignore`**: Check and update `<root>/.gitignore` if needed (e.g., to ignore `node_modules`, `__pycache__`, `.env`, etc.).

### 3. Application Code Guidelines

*   **Content & Language**: Use Australian English (instead of American English) in all docs, comments, and application copy.
*   **Test Data**: When generating synthetic mock data, use names like "Nguyen" or "Vu" if possible, and prefer Australia-related test data (e.g., Australian cities, states, addresses).
*   **Engaging & Educational**: Structure the code so that it clearly illustrates the learning outcome (e.g., separating the database connection logic from the routing logic).
*   **Keep It Simple**: Avoid overly complex frameworks or design patterns unless they are the focus of the objective. For instance, if demonstrating RAW SQL, don't use an ORM.

### 4. Verification

*   Once the files are created, you MUST verify that everything works fine and is in place.
*   Run `make up` to ensure the environment starts correctly.
*   Run `make test` or `make e2e` to ensure the end-to-end tests pass.
*   Bring down the environment with `make down`.

### 5. Finalize

Once verified, provide the user with a summary of the created project structure, the test results, and clickable links to the newly created markdown files (`README.md` and `QUICKSTART.md`).
