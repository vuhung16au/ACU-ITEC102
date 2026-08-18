.PHONY: run test clean

run:
	uv run streamlit run app.py

test:
	PYTHONPATH=. uv run pytest tests/

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -r {} +
