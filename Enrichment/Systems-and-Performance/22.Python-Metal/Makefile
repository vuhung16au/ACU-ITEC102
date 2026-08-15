.PHONY: run test clean benchmark

run:
	uv run python src/main.py

test:
	uv run pytest tests/

benchmark:
	uv run python src/main.py --benchmark

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
