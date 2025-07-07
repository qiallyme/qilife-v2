import os
import shutil
from pathlib import Path

# === CONFIG ===
base_path = Path("C:/Users/codyr/Documents/Github/qilife-main")
src_path = base_path / "src"
archive_path = base_path / ".ARCHIVE"

# Ensure archive directory exists (with all parents)
archive_path.mkdir(parents=True, exist_ok=True)

# Mapping: current relative path (from base) → future target module inside src/
move_map = {
    # Core
    "add_init_files.py": "core",

    # Monitor
    "c_scripts/log_watcher.py": "monitor",

    # Context
    "src/d-qifileflow/aa04_analyze.py": "context",
    "src/i_qitools/c03_ai/jc04_ocr_metadata_extractor.py": "context",

    # Fileflow
    "src/d-qifileflow/aa06_rename.py": "fileflow",
    "src/d-qifileflow/aa07_filer.py": "fileflow",
    "src/i_qitools/a01_file_manipulators/ja10_consolidate_files.py": "fileflow",

    # Messaging
    "src/f-qimessage": "messaging",

    # GUI
    "src/h_gui": "gui",

    # Qinote
    "src/g-qinote/ac01_nodes.py": "qinote",
    "src/g-qinote/ac02_templates.py": "qinote",

    # Lifelog
    "src/g-qinote/qilifelog/ab01_capture.py": "lifelog",
}

# Create future target folders inside src/
for folder in set(move_map.values()):
    target_folder = src_path / folder
    target_folder.mkdir(parents=True, exist_ok=True)

# Move to archive
for rel_path, future_module in move_map.items():
    source_path = base_path / rel_path
    if source_path.exists():
        archive_dest = archive_path / source_path.name
        print(f"📦 Archiving: {source_path} → {archive_dest}")
        shutil.move(str(source_path), archive_dest)
    else:
        print(f"⚠️ Missing: {source_path}")

print("\n✅ Archive complete. All selected files moved to `.ARCHIVE` for double-check.")
