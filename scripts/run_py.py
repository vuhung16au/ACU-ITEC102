#!/usr/bin/env python3
"""Execute Python scripts across Week01 to Week12 and display their outputs.

Usage:
    python scripts/run_py.py [optional: WeekXX]
"""

import glob
import os
import subprocess
import sys
import time

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def run_python_scripts(target_week: str | None = None) -> int:
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = (
        f"{target_week}/**/src/*.py"
        if target_week
        else "Week[0-1][0-9]/**/src/*.py"
    )
    search_path = os.path.join(workspace_root, pattern)
    py_files = sorted(glob.glob(search_path, recursive=True))

    py_files = [
        f
        for f in py_files
        if "/Week00/" not in f
        and "/.venv" not in f
        and "/__pycache__" not in f
    ]

    total = len(py_files)
    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    print(f"{BOLD}{CYAN}   Running ITEC102 Python Scripts (Weeks 01-12)                      {RESET}")
    print(f"{BOLD}{CYAN}======================================================================{RESET}")
    print(f"Executing {total} Python script(s)...\n")

    exec_env = os.environ.copy()
    exec_env["MPLBACKEND"] = "Agg"
    exec_env["MPLCONFIGDIR"] = "/tmp/matplotlib_itec102"
    exec_env["PYTHONUNBUFFERED"] = "1"
    python_bin = sys.executable

    failed = []
    for idx, filepath in enumerate(py_files, 1):
        rel_path = os.path.relpath(filepath, workspace_root)
        print(f"\n{BOLD}{CYAN}[{idx}/{total}] Running {rel_path}...{RESET}")
        print("-" * 60)

        file_dir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        start = time.time()
        try:
            res = subprocess.run(
                [python_bin, filename],
                cwd=file_dir,
                capture_output=True,
                text=True,
                timeout=30,
                env=exec_env,
            )
            elapsed = time.time() - start
            if res.stdout:
                print(res.stdout.rstrip())
            if res.returncode == 0:
                print(f"{GREEN}✓ Completed in {elapsed:.2f}s{RESET}")
            else:
                if res.stderr:
                    print(f"{RED}{res.stderr.rstrip()}{RESET}")
                print(f"{RED}✗ Failed with exit code {res.returncode}{RESET}")
                failed.append(rel_path)
        except subprocess.TimeoutExpired:
            print(f"{RED}✗ Timed out after 30s{RESET}")
            failed.append(rel_path)
        except Exception as e:
            print(f"{RED}✗ Exception: {e}{RESET}")
            failed.append(rel_path)

    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    if failed:
        print(f"{BOLD}{RED}Completed with {len(failed)} failure(s):{RESET}")
        for f in failed:
            print(f"  - {f}")
        return 1

    print(f"{BOLD}{GREEN}✓ All {total} Python scripts executed successfully!{RESET}\n")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(run_python_scripts(target))
