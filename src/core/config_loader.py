# config_loader.py - Part of the core module
# This module handles loading and updating configuration settings from a .env file.
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def get_config():
    config = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "NOTION_API_KEY": os.getenv("NOTION_API_KEY"),
    }
    return config

def update_config(key, value):
    env_path = Path(".env")
    if env_path.exists():
        lines = env_path.read_text().splitlines()
        found = False
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}"
                found = True
                break
        if not found:
            lines.append(f"{key}={value}")
        env_path.write_text("\n".join(lines))
