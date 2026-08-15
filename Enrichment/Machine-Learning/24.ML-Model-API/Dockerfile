FROM python:3.10-slim

WORKDIR /app

# Install uv for fast dependency management
RUN pip install uv

# Copy project definition and README
COPY pyproject.toml README.md /app/

# Create a virtual environment and install dependencies
RUN uv venv && uv pip install -e .

# Copy the rest of the application
COPY app /app/app
COPY data /app/data

# Ensure data directory is writable
RUN chmod -R 777 /app/data

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
