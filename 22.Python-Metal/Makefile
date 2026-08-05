.PHONY: run test clean

run:
	uv run python src/main.py

test:
	uv run pytest tests/

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
