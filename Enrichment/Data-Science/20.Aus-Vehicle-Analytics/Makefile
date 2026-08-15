.PHONY: build fetch process data run clean

build:
	@echo "Installing dependencies..."
	uv sync

fetch:
	@echo "Fetching raw data..."
	uv run python src/fetch_data.py

process:
	@echo "Processing data..."
	uv run python src/clean_data.py

data: fetch process

run:
	@echo "Running the Streamlit app..."
	uv run streamlit run src/app.py

clean:
	@echo "Cleaning up virtual environment and data folder..."
	rm -rf .venv
	rm -rf data
