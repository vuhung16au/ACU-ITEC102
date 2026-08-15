.PHONY: up down test clean e2e

up:
	docker-compose up -d --build

down:
	docker-compose down

test:
	PYTHONPATH=. uv run --with pytest pytest tests/

e2e: test

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
