.PHONY: up down test clean

up:
	docker compose up -d

down:
	docker compose down

test:
	docker exec -it app-21-python-cuda bash -c 'export PATH="$$HOME/.local/bin:$$PATH" && uv run pytest tests/'

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
