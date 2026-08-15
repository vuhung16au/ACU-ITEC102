.PHONY: setup run test clean

setup:
	uv sync

run: setup
	@echo "--- Running Regression Training ---"
	uv run python src/train_regression.py
	@echo "\n--- Running Classification Training ---"
	uv run python src/train_classification.py

test: setup
	uv run pytest tests/ -v

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
