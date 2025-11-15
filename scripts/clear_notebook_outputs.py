"""Clear outputs and execution counts from a Jupyter notebook file.

Usage (from repo root):
    python scripts\clear_notebook_outputs.py "Train_plant_disease.ipynb"

This script overwrites the notebook with outputs removed so it's safe to commit.
"""
import json
import sys
from pathlib import Path


def clear_notebook_outputs(nb_path: Path) -> None:
    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    changed = False
    for cell in cells:
        if cell.get("cell_type") == "code":
            if cell.get("outputs"):
                cell["outputs"] = []
                changed = True
            if cell.get("execution_count") is not None:
                cell["execution_count"] = None
                changed = True

    if changed:
        with nb_path.open("w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"Cleared outputs in: {nb_path}")
    else:
        print(f"No outputs to clear in: {nb_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts\\clear_notebook_outputs.py <notebook.ipynb>")
        sys.exit(1)
    nb_file = Path(sys.argv[1])
    if not nb_file.exists():
        print(f"Notebook not found: {nb_file}")
        sys.exit(1)
    clear_notebook_outputs(nb_file)


if __name__ == "__main__":
    main()
