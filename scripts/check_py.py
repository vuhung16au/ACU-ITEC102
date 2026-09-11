#!/usr/bin/env python3
"""Check Python files across Week01 to Week12 for educational comments and error-free execution.

Usage:
    python scripts/check_py.py [optional: WeekXX]
"""

import ast
import glob
import io
import os
import subprocess
import sys
import time
import tokenize

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def count_comment_and_docstring_lines(filepath: str) -> int:
    """Counts the total number of comment and docstring lines in a Python file."""
    comment_lines = 0
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return 0

    # 1. Count inline comments using tokenize
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(content).readline))
        for tok_type, _, _, _, _ in tokens:
            if tok_type == tokenize.COMMENT:
                comment_lines += 1
    except Exception:
        pass

    # 2. Count docstrings using ast
    try:
        tree = ast.parse(content, filename=filepath)
        mod_doc = ast.get_docstring(tree)
        if mod_doc:
            comment_lines += len(mod_doc.strip().splitlines())
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                doc = ast.get_docstring(node)
                if doc:
                    comment_lines += len(doc.strip().splitlines())
    except Exception:
        pass

    return comment_lines


def check_python_files(target_week: str | None = None) -> int:
    """Scans, audits comments, and executes Python scripts in Week01 to Week12."""
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = (
        f"{target_week}/**/src/*.py"
        if target_week
        else "Week[0-1][0-9]/**/src/*.py"
    )
    search_path = os.path.join(workspace_root, pattern)
    py_files = sorted(glob.glob(search_path, recursive=True))

    # Exclude Week00, virtualenvs, and pycache
    py_files = [
        f
        for f in py_files
        if "/Week00/" not in f
        and "/.venv" not in f
        and "/__pycache__" not in f
    ]

    total_files = len(py_files)
    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    print(f"{BOLD}{CYAN}   ITEC102 Python Files Verification (Weeks 01-12)                   {RESET}")
    print(f"{BOLD}{CYAN}======================================================================{RESET}")
    print(f"Discovered {BOLD}{total_files}{RESET} Python file(s) across weekly topics.\n")

    passed_count = 0
    failed_files: list[tuple[str, str]] = []

    # Prepare execution environment
    exec_env = os.environ.copy()
    exec_env["MPLBACKEND"] = "Agg"
    exec_env["MPLCONFIGDIR"] = "/tmp/matplotlib_itec102"
    exec_env["PYTHONUNBUFFERED"] = "1"
    python_bin = sys.executable

    current_week = ""
    for idx, filepath in enumerate(py_files, 1):
        rel_path = os.path.relpath(filepath, workspace_root)
        week_part = rel_path.split(os.sep)[0]

        if week_part != current_week:
            current_week = week_part
            print(f"\n{BOLD}[{current_week}]{RESET}")

        # 1. Comment / Educational Check
        comment_count = count_comment_and_docstring_lines(filepath)
        if comment_count == 0:
            print(f"  [{idx:02d}/{total_files:02d}] {rel_path} ... {RED}[FAIL - No comments]{RESET}")
            failed_files.append((rel_path, "No educational comments or docstrings found in file."))
            continue

        # 2. Execution Check
        file_dir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        start_time = time.time()
        try:
            result = subprocess.run(
                [python_bin, filename],
                cwd=file_dir,
                capture_output=True,
                text=True,
                timeout=25,
                env=exec_env,
            )
            elapsed = time.time() - start_time
            if result.returncode == 0:
                print(f"  [{idx:02d}/{total_files:02d}] {rel_path} ({comment_count} comments, {elapsed:.2f}s) ... {GREEN}[PASS]{RESET}")
                passed_count += 1
            else:
                error_msg = result.stderr.strip() or result.stdout.strip()
                print(f"  [{idx:02d}/{total_files:02d}] {rel_path} ... {RED}[FAIL - Exit code {result.returncode}]{RESET}")
                failed_files.append((rel_path, f"Execution error:\n{error_msg}"))
        except subprocess.TimeoutExpired:
            print(f"  [{idx:02d}/{total_files:02d}] {rel_path} ... {RED}[FAIL - Timed out]{RESET}")
            failed_files.append((rel_path, "Process timed out after 25s (possible infinite loop or waiting for input)."))
        except Exception as e:
            print(f"  [{idx:02d}/{total_files:02d}] {rel_path} ... {RED}[FAIL - System error]{RESET}")
            failed_files.append((rel_path, str(e)))

    # Summary report
    print(f"\n{BOLD}{CYAN}----------------------------------------------------------------------{RESET}")
    print(f"{BOLD}Summary of Python Checks:{RESET}")
    print(f"  Total Checked: {total_files}")
    print(f"  {GREEN}Passed:        {passed_count}{RESET}")
    print(f"  {RED if failed_files else GREEN}Failed:        {len(failed_files)}{RESET}")
    print(f"{BOLD}{CYAN}----------------------------------------------------------------------{RESET}")

    if failed_files:
        print(f"\n{BOLD}{RED}Failure Diagnostics:{RESET}")
        for path, err in failed_files:
            print(f"\n{BOLD}File:{RESET} {path}")
            print(f"{err}\n")
        return 1

    print(f"{BOLD}{GREEN}✓ All Python scripts passed educational comment & execution checks!{RESET}\n")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(check_python_files(target))
