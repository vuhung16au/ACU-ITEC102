# ACU-ITEC102 Course Code Validation and Execution Makefile
# Designed for 1st year Computer Science students learning Python programming.

.PHONY: help venv check check-py check-ipynb run run-py run-ipynb clean

UV ?= uv
VENV ?= .venv
PYTHON ?= $(VENV)/bin/python
WEEK ?=

help:
	@echo "Available commands in ACU-ITEC102:"
	@echo "  make check         - Run all checks (check-py and check-ipynb) across Weeks 01-12"
	@echo "  make check-py      - Validate comments and error-free execution of all .py files"
	@echo "  make check-ipynb   - Validate structure and error-free execution of all .ipynb notebooks"
	@echo "  make run           - Execute all Python scripts and Jupyter notebooks across Weeks 01-12"
	@echo "  make run-py        - Execute all Python scripts and display program output"
	@echo "  make run-ipynb     - Execute all Jupyter notebooks and display output"
	@echo "  make venv          - Create and provision the .venv virtual environment using uv"
	@echo "  make clean         - Clean up virtual environments and Python cache files"
	@echo ""
	@echo "Tip: Run for a specific week with WEEK=WeekXX (e.g., make check-py WEEK=Week04)"

# Provision virtual environment using uv
$(PYTHON):
	@echo "Creating virtual environment $(VENV) using $(UV)..."
	@$(UV) venv $(VENV) --python 3.14
	@if [ -d ".venv_global/lib/python3.14/site-packages" ]; then \
		echo "$$(pwd)/.venv_global/lib/python3.14/site-packages" > $(VENV)/lib/python3.14/site-packages/sitepackages.pth; \
	elif [ -f "requirements.txt" ]; then \
		$(UV) pip install --python $(PYTHON) -r requirements.txt; \
	fi
	@echo "Virtual environment ready at $(VENV)."

venv: $(PYTHON)

# Verification targets
check: check-py check-ipynb

check-py: $(PYTHON)
	@$(UV) run --python $(PYTHON) scripts/check_py.py $(WEEK)

check-ipynb: $(PYTHON)
	@$(UV) run --python $(PYTHON) scripts/check_ipynb.py $(WEEK)

# Execution targets
run: run-py run-ipynb

run-py: $(PYTHON)
	@$(UV) run --python $(PYTHON) scripts/run_py.py $(WEEK)

run-ipynb: $(PYTHON)
	@$(UV) run --python $(PYTHON) scripts/run_ipynb.py $(WEEK)

# Cleanup
clean:
	@echo "Cleaning up python virtual environments and cache files to free up space..."
	@find . -type d -name ".venv" -not -path "./.venv_global/*" -prune -exec rm -rf {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name "build" -prune -exec rm -rf {} +
	@find . -type d -name "dist" -prune -exec rm -rf {} +
	@echo "Cleanup complete."
