.PHONY: up down test clean e2e run-etl

up:
	docker-compose up -d

down:
	docker-compose down

test:
	PYTHONPATH=. uv run --with pytest pytest tests/

run-etl:
	export DB_HOST=localhost && \
	export DB_NAME=etl_db && \
	export DB_USER=postgres && \
	export DB_PASSWORD=postgrespassword && \
	uv run python etl.py

e2e: up test run-etl
	docker-compose down

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
