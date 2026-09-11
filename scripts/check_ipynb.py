#!/usr/bin/env python3
"""Check Jupyter Notebooks across Week01 to Week12 for structure, error-free execution, and output generation.

Usage:
    python scripts/check_ipynb.py [optional: WeekXX]
"""

import glob
import json
import os
import sys
import time
from typing import Any

try:
    from IPython.display import display
except ImportError:
    display = print

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def check_notebook_file(filepath: str, workspace_root: str) -> tuple[bool, str, int, int]:
    """Audits and executes a single Jupyter notebook file.

    Returns:
        (success, message, code_cell_count, markdown_cell_count)
    """
    rel_path = os.path.relpath(filepath, workspace_root)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        return False, f"Failed to parse notebook JSON: {e}", 0, 0

    cells = nb.get("cells", [])
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]

    if not cells:
        return False, "Notebook is empty.", 0, 0

    if not markdown_cells:
        return False, "Notebook is missing educational markdown explanations.", len(code_cells), 0

    # Set working directory to notebook's directory for proper relative file access
    nb_dir = os.path.dirname(os.path.abspath(filepath))
    orig_cwd = os.getcwd()

    # Shared global environment for cells in the notebook
    global_env: dict[str, Any] = {
        "__name__": "__main__",
        "__file__": filepath,
        "display": display,
    }

    # Set headless matplotlib environment
    os.environ["MPLBACKEND"] = "Agg"
    os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_itec102"

    executed_cells = 0
    try:
        os.chdir(nb_dir)
        for idx, cell in enumerate(code_cells, 1):
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue

            # Strip IPython magics and shell bang commands for standard python execution
            clean_lines = []
            for line in source.splitlines():
                stripped = line.strip()
                if stripped.startswith("!") or stripped.startswith("%"):
                    # Comment out magic commands so line numbers remain aligned
                    clean_lines.append(f"# {line}")
                else:
                    clean_lines.append(line)
            code_to_exec = "\n".join(clean_lines)

            # Compile and execute
            compiled = compile(code_to_exec, f"{rel_path}:cell_{idx}", "exec")
            exec(compiled, global_env)
            executed_cells += 1

    except Exception as e:
        os.chdir(orig_cwd)
        return (
            False,
            f"Error executing code cell {idx}: {type(e).__name__}: {e}",
            len(code_cells),
            len(markdown_cells),
        )
    finally:
        os.chdir(orig_cwd)

    return True, "Executed cleanly", len(code_cells), len(markdown_cells)


def check_notebooks(target_week: str | None = None) -> int:
    """Scans, verifies educational content, and executes all notebooks in Week01 to Week12."""
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = (
        f"{target_week}/**/notebooks/*.ipynb"
        if target_week
        else "Week[0-1][0-9]/**/notebooks/*.ipynb"
    )
    search_path = os.path.join(workspace_root, pattern)
    nb_files = sorted(glob.glob(search_path, recursive=True))

    # Exclude Week00, checkpoints, and virtualenvs
    nb_files = [
        f
        for f in nb_files
        if "/Week00/" not in f
        and ".ipynb_checkpoints" not in f
        and "/.venv" not in f
    ]

    total_notebooks = len(nb_files)
    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    print(f"{BOLD}{CYAN}   ITEC102 Jupyter Notebooks Verification (Weeks 01-12)              {RESET}")
    print(f"{BOLD}{CYAN}======================================================================{RESET}")
    print(f"Discovered {BOLD}{total_notebooks}{RESET} Jupyter notebook(s) across weekly topics.\n")

    passed_count = 0
    failed_notebooks: list[tuple[str, str]] = []

    current_week = ""
    for idx, filepath in enumerate(nb_files, 1):
        rel_path = os.path.relpath(filepath, workspace_root)
        week_part = rel_path.split(os.sep)[0]

        if week_part != current_week:
            current_week = week_part
            print(f"\n{BOLD}[{current_week}]{RESET}")

        start_time = time.time()
        success, message, code_count, md_count = check_notebook_file(filepath, workspace_root)
        elapsed = time.time() - start_time

        if success:
            print(
                f"  [{idx:02d}/{total_notebooks:02d}] {rel_path} "
                f"({code_count} code, {md_count} markdown cells, {elapsed:.2f}s) ... {GREEN}[PASS]{RESET}"
            )
            passed_count += 1
        else:
            print(f"  [{idx:02d}/{total_notebooks:02d}] {rel_path} ... {RED}[FAIL]{RESET}")
            failed_notebooks.append((rel_path, message))

    # Summary report
    print(f"\n{BOLD}{CYAN}----------------------------------------------------------------------{RESET}")
    print(f"{BOLD}Summary of Notebook Checks:{RESET}")
    print(f"  Total Checked: {total_notebooks}")
    print(f"  {GREEN}Passed:        {passed_count}{RESET}")
    print(f"  {RED if failed_notebooks else GREEN}Failed:        {len(failed_notebooks)}{RESET}")
    print(f"{BOLD}{CYAN}----------------------------------------------------------------------{RESET}")

    if failed_notebooks:
        print(f"\n{BOLD}{RED}Notebook Failure Diagnostics:{RESET}")
        for path, err in failed_notebooks:
            print(f"\n{BOLD}Notebook:{RESET} {path}")
            print(f"{err}\n")
        return 1

    print(f"{BOLD}{GREEN}✓ All Jupyter Notebooks passed educational & execution checks!{RESET}\n")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(check_notebooks(target))
