# Quickstart: Python on CUDA

This project uses Docker to encapsulate the CUDA environment. 
**Prerequisites**: You must have an NVIDIA GPU, Linux/WSL2, and the NVIDIA Container Toolkit installed to pass the GPU into the container.

## Running the Project

1. **Start the Environment**
   Open your terminal and run:
   ```bash
   make up
   ```
   This command will build the Docker container using a CUDA base image and install all necessary dependencies (CuPy and cuDF) via `uv`.

2. **Execute the Code**
   Once the container is running, you can execute the data science script:
   ```bash
   docker exec -it app-21-python-cuda bash -c 'export PATH="$HOME/.local/bin:$PATH" && uv run python src/main.py'
   ```

3. **Run Tests**
   To verify the setup with tests:
   ```bash
   make test
   ```

4. **Tear Down**
   When finished, stop and remove the container:
   ```bash
   make down
   ```
