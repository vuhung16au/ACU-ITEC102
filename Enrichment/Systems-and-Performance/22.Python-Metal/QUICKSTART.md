# Quickstart: Python on Metal

This project runs natively on macOS (Apple Silicon). We skip Docker in this project because Docker Desktop for Mac cannot directly pass the Metal GPU into Linux containers. Running it natively ensures you fully leverage the M-Series GPU and unified memory architecture.

## Running the Project

1. **Prerequisites**
   Ensure you have `uv` (the fast Python package installer) installed.

2. **Execute the Code**
   Open your terminal and run:
   ```bash
   make run
   ```
   This will use `uv` to automatically install the fixed dependencies (`mlx`, `polars`) and run the script on your Mac.

3. **Run Tests**
   To verify the setup with tests:
   ```bash
   make test
   ```
