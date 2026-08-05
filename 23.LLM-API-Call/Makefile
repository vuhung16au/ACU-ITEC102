.PHONY: up down test run clean

# "up" is maintained for consistency with other projects, though not strictly needed here as no Docker containers are used.
up:
	@echo "No Docker containers to start for this project."

down:
	@echo "No Docker containers to stop for this project."

run:
	uv run main.py

test: e2e

e2e:
	uv run pytest

clean:
	rm -rf .venv __pycache__ .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
