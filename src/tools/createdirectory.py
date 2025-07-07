import os
from pathlib import Path

# Change this to your desired base location
base_path = Path("C:/Users/codyr/Documents/Github/qilife-refactor")

# List of all directories to create
folders = [
    ".ARCHIVE", "tests",
    "src/core", "src/monitor", "src/context", "src/fileflow",
    "src/calls", "src/messaging", "src/memory", "src/gui/components",
    "src/gui/styles", "src/lifelog", "src/qinote",
    "src/tools/ai", "src/tools/fileops", "src/tools/folderops",
    "src/tools/config", "src/tools/logs", "src/tools/index", "src/tools/utils",
    "src/empower713"
]

# List of all files (relative to base)
files = [
    "app.py", "requirements.txt", "README.md", ".env",
    "setup_venv.ps1", "docker-compose.yml", "dockerfile",
    "src/core/config_loader.py", "src/core/module_router.py", "src/core/env_manager.py", "src/core/log_setup.py",
    "src/monitor/screenshot_watcher.py", "src/monitor/file_event_monitor.py", "src/monitor/device_state_tracker.py",
    "src/context/ocr_extractor.py", "src/context/text_classifier.py", "src/context/file_renamer.py",
    "src/context/metadata_extractor.py", "src/context/summarizer.py",
    "src/fileflow/mover.py", "src/fileflow/folder_merger.py", "src/fileflow/rename_rules.py",
    "src/fileflow/folder_creator.py", "src/fileflow/consolidator.py",
    "src/calls/call_handler.py", "src/calls/voice_transcriber.py", "src/calls/elevenlabs_interface.py",
    "src/calls/voicemail_router.py",
    "src/messaging/sms_router.py", "src/messaging/email_parser.py", "src/messaging/webhook_handler.py",
    "src/messaging/conversation_sync.py",
    "src/memory/embedder.py", "src/memory/vector_store.py", "src/memory/retriever.py", "src/memory/memory_logger.py",
    "src/gui/main_window.py", "src/gui/splash_screen.py",
    "src/gui/components/timeline.py", "src/gui/components/file_review.py",
    "src/gui/components/folder_picker.py", "src/gui/components/log_export.py",
    "src/lifelog/ingestion.py", "src/lifelog/digest_creator.py", "src/lifelog/spyme.py",
    "src/lifelog/notion_logger.py", "src/lifelog/activity_feeder.py",
    "src/qinote/node_manager.py", "src/qinote/template_engine.py",
    "src/qinote/reflection_api.py", "src/qinote/notion_cleanup.py",
    "src/tools/ai/prompt_runner.py", "src/tools/ai/summarizer.py", "src/tools/ai/classifier.py",
    "src/tools/fileops/pdf_tools.py", "src/tools/fileops/image_to_text.py", "src/tools/fileops/html_parser.py",
    "src/tools/folderops/smart_merger.py", "src/tools/folderops/auto_sorter.py", "src/tools/folderops/empty_cleaner.py",
    "src/tools/config/notion_config.py", "src/tools/config/openai_config.py",
    "src/tools/logs/screen_log.py", "src/tools/logs/log_watcher.py", "src/tools/logs/timeline_log.py",
    "src/tools/index/duplicate_finder.py", "src/tools/index/folder_indexer.py",
    "src/tools/utils/string_tools.py", "src/tools/utils/config_manager.py", "src/tools/utils/hashing.py",
    "src/empower713/manifesto.md", "src/empower713/brand_intro.txt", "src/empower713/core_principles.py"
]

# Create folders and __init__.py where appropriate
for folder in folders:
    full_path = base_path / folder
    full_path.mkdir(parents=True, exist_ok=True)
    init_path = full_path / "__init__.py"
    if not init_path.exists():
        init_path.touch()

# Create files with placeholder content
for file in files:
    full_path = base_path / file
    if not full_path.exists():
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text("# TODO\n")

print(f"✅ Full QiLife scaffold created at: {base_path}")
