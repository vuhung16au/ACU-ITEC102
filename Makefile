.PHONY: clean

clean:
	@echo "Cleaning up python virtual environments and cache files to free up space..."
	@find . -type d -name ".venv" -prune -exec rm -rf {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name "build" -prune -exec rm -rf {} +
	@find . -type d -name "dist" -prune -exec rm -rf {} +
	@echo "Cleanup complete."
