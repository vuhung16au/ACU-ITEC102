FROM python:3.10-slim

WORKDIR /app

# Install uv for fast dependency management
RUN pip install uv

# Copy project definition
COPY pyproject.toml README.md /app/

# Create a virtual environment and install dependencies
RUN uv venv && uv pip install -e .

# Copy the rest of the application
COPY app.py /app/
COPY data /app/data

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
