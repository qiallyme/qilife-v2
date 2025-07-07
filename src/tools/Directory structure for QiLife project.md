#Directory structure for QiLife project
#This structure is designed to be modular, scalable, and maintainable
qilife-main/
├── app.py                  # Entry point: launches GUI or CLI
├── requirements.txt
├── README.md
├── .env
├── setup_venv.ps1
├── docker-compose.yml
├── dockerfile
├── .ARCHIVE/               # Staging for old/unused files
├── tests/                  # All unit + integration tests
│
├── src/
│   ├── core/               # App lifecycle, routing, config, logging
│   │   ├── config_loader.py
│   │   ├── module_router.py
│   │   ├── env_manager.py
│   │   └── log_setup.py
│   │
│   ├── monitor/            # Monitors for file changes, screenshots, activity
│   │   ├── screenshot_watcher.py
│   │   ├── file_event_monitor.py
│   │   └── device_state_tracker.py
│   │
│   ├── context/            # AI-based file/content analysis + renaming
│   │   ├── ocr_extractor.py
│   │   ├── text_classifier.py
│   │   ├── file_renamer.py
│   │   ├── metadata_extractor.py
│   │   └── summarizer.py
│   │
│   ├── fileflow/           # Physical file actions: move, sort, dedupe
│   │   ├── mover.py
│   │   ├── folder_merger.py
│   │   ├── rename_rules.py
│   │   ├── folder_creator.py
│   │   └── consolidator.py
│   │
│   ├── calls/              # QiCall: Twilio, voice assistants, speech logging
│   │   ├── call_handler.py
│   │   ├── voice_transcriber.py
│   │   ├── elevenlabs_interface.py
│   │   └── voicemail_router.py
│   │
│   ├── messaging/          # SMS, email, ticketing, chat integration
│   │   ├── sms_router.py
│   │   ├── email_parser.py
│   │   ├── webhook_handler.py
│   │   └── conversation_sync.py
│   │
│   ├── memory/             # Vector DB, embeddings, long-term context
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── memory_logger.py
│   │
│   ├── gui/                # Visual interface, dashboard, splash screen
│   │   ├── main_window.py
│   │   ├── splash_screen.py
│   │   ├── components/
│   │   │   ├── timeline.py
│   │   │   ├── file_review.py
│   │   │   ├── folder_picker.py
│   │   │   └── log_export.py
│   │   └── styles/
│   │
│   ├── lifelog/            # Life activity logging + daily digest engine
│   │   ├── ingestion.py
│   │   ├── digest_creator.py
│   │   ├── spyme.py
│   │   ├── notion_logger.py
│   │   └── activity_feeder.py
│   │
│   ├── qinote/             # Personal nodes, journals, task engine
│   │   ├── node_manager.py
│   │   ├── template_engine.py
│   │   ├── reflection_api.py
│   │   └── notion_cleanup.py
│   │
│   ├── tools/              # Low-level utilities and scripts
│   │   ├── ai/                 # AI helpers, model wrappers
│   │   │   ├── prompt_runner.py
│   │   │   ├── summarizer.py
│   │   │   └── classifier.py
│   │   ├── fileops/           # Manipulate, convert, extract files
│   │   │   ├── pdf_tools.py
│   │   │   ├── image_to_text.py
│   │   │   └── html_parser.py
│   │   ├── folderops/         # Folder management, structure builders
│   │   │   ├── smart_merger.py
│   │   │   ├── auto_sorter.py
│   │   │   └── empty_cleaner.py
│   │   ├── config/            # API clients, settings templates
│   │   │   ├── notion_config.py
│   │   │   └── openai_config.py
│   │   ├── logs/              # Logging and file activity monitors
│   │   │   ├── screen_log.py
│   │   │   ├── log_watcher.py
│   │   │   └── timeline_log.py
│   │   ├── index/             # Deduplication and directory indexing
│   │   │   ├── duplicate_finder.py
│   │   │   └── folder_indexer.py
│   │   └── utils/             # Generic helpers
│   │       ├── string_tools.py
│   │       ├── config_manager.py
│   │       └── hashing.py
│   │
│   └── empower713/          # Branding, philosophy, manifestos, docs
│       ├── manifesto.md
│       ├── brand_intro.txt
│       └── core_principles.py
