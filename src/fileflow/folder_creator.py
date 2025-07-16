#!/usr/bin/env python3
import sys
import pandas as pd
from pathlib import Path
from rich import print

def load_structure_df(file_path: Path) -> pd.DataFrame:
    """
    Load folder structure from a CSV or Excel file.
    CSV must have headers 'folder_Parent_Name' and 'folder_Name'.
    Excel must be a valid .xls/.xlsx.
    """
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"[red]❌ Failed to read CSV: {e}[/]")
            sys.exit(1)
    elif suffix in (".xls", ".xlsx"):
        try:
            return pd.read_excel(file_path, engine="openpyxl")
        except ImportError:
            print("[red]❌ Missing dependency: install openpyxl to read Excel files.[/]")
            sys.exit(1)
        except Exception as e:
            print(f"[red]❌ Failed to read Excel: {e}[/]")
            sys.exit(1)
    else:
        print(f"[red]❌ Unsupported file type '{suffix}'. Use .csv, .xls, or .xlsx[/]")
        sys.exit(1)

def get_expected_from_df(base_path: Path, df: pd.DataFrame) -> list[Path]:
    """Builds a list of expected folder Paths based on parent/name columns."""
    df = df.fillna("")  # convert NaN → ""
    path_map = {}
    expected = []
    for _, row in df.iterrows():
        parent = row["folder_Parent_Name"].strip()
        name = row["folder_Name"].strip()
        if not name:
            continue
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

def sync_folder_structure(base_path: Path, struct_file: Path, dry_run: bool):
    df = load_structure_df(struct_file)
    expected = get_expected_from_df(base_path, df)
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
    struct_input = input("Enter path to your folder-structure file (.csv/.xls/.xlsx): ").strip()
    struct_path = Path(struct_input).expanduser().resolve()
    if not struct_path.is_file():
        print(f"[red]❌ File not found: {struct_path}[/]")
        sys.exit(1)

    base_input = input("Enter the base directory to review/create: ").strip()
    base_path = Path(base_input).expanduser().resolve()
    if not base_path.exists():
        if input(f"Directory {base_path} does not exist. Create it? [y/N]: ").strip().lower() == "y":
            base_path.mkdir(parents=True, exist_ok=True)
            print(f"[green]Created base directory: {base_path}[/]")
        else:
            print("[red]Aborted[/]")
            sys.exit(1)

    dry_run = input("Dry run only? (list missing without creating) [Y/n]: ").strip().lower() != "n"

    sync_folder_structure(base_path=base_path, struct_file=struct_path, dry_run=dry_run)
