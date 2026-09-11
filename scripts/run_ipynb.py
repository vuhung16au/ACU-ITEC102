#!/usr/bin/env python3
"""Execute Jupyter Notebooks across Week01 to Week12 and display their execution results.

Usage:
    python scripts/run_ipynb.py [optional: WeekXX]
"""

import glob
import io
import json
import os
import sys
import time
from contextlib import redirect_stderr, redirect_stdout
from typing import Any

try:
    from IPython.display import display
except ImportError:
    display = print

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def run_notebook(filepath: str, workspace_root: str) -> tuple[bool, str]:
    rel_path = os.path.relpath(filepath, workspace_root)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        return False, f"Failed to load notebook JSON: {e}"

    code_cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
    if not code_cells:
        return True, "No code cells to execute"

    nb_dir = os.path.dirname(os.path.abspath(filepath))
    orig_cwd = os.getcwd()

    global_env: dict[str, Any] = {
        "__name__": "__main__",
        "__file__": filepath,
        "display": display,
    }

    os.environ["MPLBACKEND"] = "Agg"
    os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_itec102"

    try:
        os.chdir(nb_dir)
        for idx, cell in enumerate(code_cells, 1):
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue

            clean_lines = []
            for line in source.splitlines():
                stripped = line.strip()
                if stripped.startswith("!") or stripped.startswith("%"):
                    clean_lines.append(f"# {line}")
                else:
                    clean_lines.append(line)
            code_to_exec = "\n".join(clean_lines)

            buf_out = io.StringIO()
            buf_err = io.StringIO()
            with redirect_stdout(buf_out), redirect_stderr(buf_err):
                compiled = compile(code_to_exec, f"{rel_path}:cell_{idx}", "exec")
                exec(compiled, global_env)

            out_text = buf_out.getvalue().strip()
            if out_text:
                # Print sample output if available
                first_lines = "\n".join(out_text.splitlines()[:5])
                print(f"    Cell {idx} output:\n      {first_lines}")
    except Exception as e:
        os.chdir(orig_cwd)
        return False, f"Cell {idx} failed: {type(e).__name__}: {e}"
    finally:
        os.chdir(orig_cwd)

    return True, f"Successfully executed {len(code_cells)} code cell(s)"


def run_all_notebooks(target_week: str | None = None) -> int:
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = (
        f"{target_week}/**/notebooks/*.ipynb"
        if target_week
        else "Week[0-1][0-9]/**/notebooks/*.ipynb"
    )
    search_path = os.path.join(workspace_root, pattern)
    nb_files = sorted(glob.glob(search_path, recursive=True))

    nb_files = [
        f
        for f in nb_files
        if "/Week00/" not in f
        and ".ipynb_checkpoints" not in f
        and "/.venv" not in f
    ]

    total = len(nb_files)
    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    print(f"{BOLD}{CYAN}   Running ITEC102 Jupyter Notebooks (Weeks 01-12)                   {RESET}")
    print(f"{BOLD}{CYAN}======================================================================{RESET}")
    print(f"Executing {total} Jupyter Notebook(s)...\n")

    failed = []
    for idx, filepath in enumerate(nb_files, 1):
        rel_path = os.path.relpath(filepath, workspace_root)
        print(f"\n{BOLD}{CYAN}[{idx}/{total}] Running {rel_path}...{RESET}")

        start = time.time()
        success, msg = run_notebook(filepath, workspace_root)
        elapsed = time.time() - start

        if success:
            print(f"  {GREEN}✓ {msg} ({elapsed:.2f}s){RESET}")
        else:
            print(f"  {RED}✗ {msg} ({elapsed:.2f}s){RESET}")
            failed.append((rel_path, msg))

    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    if failed:
        print(f"{BOLD}{RED}Completed with {len(failed)} failure(s):{RESET}")
        for path, err in failed:
            print(f"  - {path}: {err}")
        return 1

    print(f"{BOLD}{GREEN}✓ All {total} Jupyter Notebooks executed successfully!{RESET}\n")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(run_all_notebooks(target))
