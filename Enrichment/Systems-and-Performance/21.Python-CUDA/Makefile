.PHONY: up down test clean benchmark run

up:
	docker compose up -d

down:
	docker compose down

run:
	docker exec -it app-21-python-cuda bash -c 'export PATH="$$HOME/.local/bin:$$PATH" && uv run python src/main.py'

benchmark:
	docker exec -it app-21-python-cuda bash -c 'export PATH="$$HOME/.local/bin:$$PATH" && uv run python src/main.py --benchmark'

test:
	docker exec -it app-21-python-cuda bash -c 'export PATH="$$HOME/.local/bin:$$PATH" && uv run pytest tests/'

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
