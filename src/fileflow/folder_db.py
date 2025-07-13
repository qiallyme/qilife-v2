# src/fileflow/folder_db.py

import sqlite3
from pathlib import Path
import pandas as pd

# Adjust this if your DB lives elsewhere
DB_PATH = Path(__file__).parents[2] / "qlife_db.sqlite"

TABLE_NAME = "folder_structure"


def init_db(db_path: Path = DB_PATH):
    """
    Create the folder_structure table if it doesn't exist.
    """
    conn = sqlite3.connect(db_path)
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        folder_Id            INTEGER PRIMARY KEY,
        folder_Name          TEXT NOT NULL,
        folder_Parent_Id     INTEGER,
        folder_Parent_Name   TEXT,
        folder_Path          TEXT,
        folder_Notes         TEXT,
        folder_Status        TEXT,
        folder_Level         INTEGER,
        sort_order           INTEGER,
        folder_Created       TEXT,
        folder_Can_Delete     TEXT,
        folder_Can_Rename     TEXT,
        folder_Children       TEXT,
        folder_Last_Updated   TEXT,
        folder_Last_Modified_By TEXT
    );""")
    conn.commit()
    conn.close()


def compute_full_paths(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame with columns folder_Id, folder_Parent_Id, folder_Name,
    computes folder_Path for each row by concatenating parent Path + "/" + Name.
    """
    df = df.copy()
    # ensure numeric parent IDs
    df["folder_Parent_Id"] = df["folder_Parent_Id"].astype(pd.Int64Dtype())

    # we'll fill this column
    df["folder_Path"] = ""
    # sort by level then by sort_order so parents come before children
    df_sorted = df.sort_values(["folder_Level", "sort_order"])

    path_map: dict[int,str] = {}
    for _, row in df_sorted.iterrows():
        fid = int(row["folder_Id"])
        name = row["folder_Name"]
        pid = row["folder_Parent_Id"]
        if pd.isna(pid):
            full = name
        else:
            parent_path = path_map[int(pid)]
            full = f"{parent_path}/{name}"
        path_map[fid] = full
        df.loc[df["folder_Id"] == fid, "folder_Path"] = full

    return df


def sync_from_excel(
    excel_path: Path,
    db_path: Path = DB_PATH,
    table: str = TABLE_NAME
):
    """
    Read the Excel (or CSV) file, compute paths, and upsert into SQLite.
    """

    # 1. Load the sheet
    df = pd.read_excel(excel_path)

    # 2. Compute the missing folder_Path column
    df = compute_full_paths(df)

    # 3. Write to SQLite using folder_Id as PK (replace entire table for simplicity)
    conn = sqlite3.connect(db_path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()


def create_directories(
    base_path: Path,
    db_path: Path = DB_PATH,
    table: str = TABLE_NAME
):
    """
    Create folders on disk for every folder_Path stored in the database.
    """
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT folder_Path FROM {table}", conn)
    conn.close()

    for p in df["folder_Path"]:
        # safe mkdir: will skip existing
        (base_path / p).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sync folder_structure DB and create directories.")
    parser.add_argument("--source", type=Path, required=True,
                        help="Path to your Folder_Structure.xlsx or .csv")
    parser.add_argument("--base",   type=Path, required=True,
                        help="Filesystem base directory where folders should live")
    parser.add_argument("--create-folders", action="store_true",
                        help="If set, create the directories on disk after syncing DB")

    args = parser.parse_args()

    print("👉 Initializing database…")
    init_db()

    print(f"👉 Syncing from {args.source} → {DB_PATH}:{TABLE_NAME}")
    sync_from_excel(args.source)

    if args.create_folders:
        print(f"👉 Creating directories under {args.base}")
        create_directories(args.base)
        print("✅ Done creating folders.")
    else:
        print("✅ DB synced. Run with `--create-folders` to actually mkdir.")
