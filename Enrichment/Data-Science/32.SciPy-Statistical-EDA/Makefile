.PHONY: setup up run test e2e down clean

setup:
	uv sync

up: run

run: setup
	uv run python main.py

test: setup
	PYTHONPATH=. uv run pytest tests/ -v

e2e: test

down:
	@echo "No background services or containers to stop."

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
