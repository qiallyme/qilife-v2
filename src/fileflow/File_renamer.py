#!/usr/bin/env python3
# src/fileflow/file_renamer.py

from pathlib import Path
from rich import print

from src.fileflow.content_extractor import extract_context
from src.config.env import get_config
from src.ai.chatgpt import ask_gpt  # we’ll define this shortly

def build_prompt(context: dict, metadata: dict) -> str:
    text = context["text"][:3000]  # Snippet or preview
    ext = metadata["extension"]
    return f"""
You are a smart assistant. Based on this file's content and metadata, rename it using the following rules:

- Use format: [YYYYMMDD]_[summary_or_topic]_[source/author]{ext}
- Be concise, lowercase, use underscores instead of spaces.
- Do NOT include special characters.
- Use the creation or modification date from metadata if it makes sense.
- Only output the **new filename**, not a full sentence.

Example:
20240712_legal_notice_zaitullah.pdf

Here is the file content:
{text}

And metadata:
{metadata}
"""

def rename_file(path: Path, new_name: str):
    new_path = path.with_name(new_name)
    path.rename(new_path)
    print(f"[green]✅ Renamed:[/] {path.name} → {new_path.name}")

def main(file_path: Path):
    print(f"\n📄 [bold]Processing:[/] {file_path.name}")

    ctx = extract_context(file_path)
    prompt = build_prompt(ctx, ctx["metadata"])
    new_name = ask_gpt(prompt).strip()

    if not new_name or not new_name.endswith(ctx["metadata"]["extension"]):
        print("[red]❌ GPT did not return a valid filename[/]")
        return

    rename_file(file_path, new_name)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: file_renamer.py path/to/file")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"[red]❌ File not found:[/] {path}")
        sys.exit(1)

    main(path)
