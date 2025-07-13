# src/fileflow/folder_creator.py

import argparse
from pathlib import Path
import pandas as pd
from rich import print

def get_expected_from_excel(base_path: Path, excel_path: Path) -> list[Path]:
    """
    Reads an Excel file with columns 'folder_Parent_Name' and 'folder_Name',
    computes full paths, and returns a list of Paths under base_path.
    """
    df = pd.read_excel(excel_path)
    df = df.fillna("")  # turn NaN → ""
    path_map = {}
    expected = []
    # We assume the sheet is already sorted: parents before children
    for _, row in df.iterrows():
        parent = row["folder_Parent_Name"].strip()
        name   = row["folder_Name"].strip()
        if not parent or parent == ".":
            full = name
        else:
            parent_path = path_map.get(parent, parent)
            full = f"{parent_path}/{name}"
        path_map[name] = full
        expected.append(base_path / Path(full))
        print(f"🔍 Expecting: {full}")
    return expected

def get_missing_folders(expected: list[Path]) -> list[Path]:
    return [p for p in expected if not p.exists()]

def sync_folder_structure(base_path: Path, excel: Path, dry_run: bool):
    expected = get_expected_from_excel(base_path, excel)
    missing = get_missing_folders(expected)

    if not missing:
        print("[green]✅ All folders exist.[/]")
        return

    print("\n[bold]📁 MISSING FOLDERS:[/]")
    for p in missing:
        print(f"  - {p}")

    if dry_run:
        print(f"\n[yellow]❓ {len(missing)} missing (dry run only)[/]")
        return

    if input(f"\n❓ Create these {len(missing)}? [y/N]: ").strip().lower() != "y":
        print("[red]Aborted[/]")
        return

    for p in missing:
        p.mkdir(parents=True, exist_ok=True)
        print(f"[green]Created:[/] {p}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--base",  type=Path, required=True,  help="Base folder to sync under")
    p.add_argument("--excel", type=Path, required=True,  help="Path to Folder_Structure.xlsx")
    p.add_argument("--dry-run", action="store_true", help="List only, do not create")
    args = p.parse_args()

    sync_folder_structure(
        base_path=args.base,
        excel=args.excel,
        dry_run=args.dry_run
    )
