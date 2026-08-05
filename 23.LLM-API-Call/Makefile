.PHONY: up down test run

# "up" is maintained for consistency with other projects, though not strictly needed here as no Docker containers are used.
up:
	@echo "No Docker containers to start for this project."

down:
	@echo "No Docker containers to stop for this project."

run:
	uv run main.py

test: e2e

e2e:
	uv run pytest
