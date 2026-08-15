.PHONY: up down test clean e2e

up:
	docker-compose up -d --build

down:
	docker-compose down

test:
	uv run --with pytest --with httpx pytest tests/

e2e: test

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -f data/model.joblib
