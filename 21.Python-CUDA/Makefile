.PHONY: up down test

up:
	docker compose up -d

down:
	docker compose down

test:
	docker exec -it app-21-python-cuda bash -c 'export PATH="$$HOME/.local/bin:$$PATH" && uv run pytest tests/'
