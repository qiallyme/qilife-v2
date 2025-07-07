import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.fileflow.mover import run_full_pipeline

class FileMonitor:
    """
    Watches a folder for new files and triggers the fileflow pipeline on each.
    """

    def __init__(self, folder_path: str, db_manager, context_memory, vector_storage):
        self.folder_path = folder_path
        self.db_manager = db_manager
        self.context_memory = context_memory
        self.vector_storage = vector_storage
        self.observer = Observer()

    def start(self):
        handler = self._EventHandler(self)
        self.observer.schedule(handler, self.folder_path, recursive=True)
        self.observer.start()
        print(f"📁 Started monitoring: {self.folder_path}")

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print(f"🛑 Stopped monitoring: {self.folder_path}")

    class _EventHandler(FileSystemEventHandler):
        def __init__(self, monitor):
            self.monitor = monitor

        def on_created(self, event):
            if not event.is_directory:
                filepath = event.src_path
                print(f"🆕 Detected file: {filepath}")
                try:
                    run_full_pipeline(
                        filepath,
                        self.monitor.db_manager,
                        self.monitor.context_memory,
                        self.monitor.vector_storage
                    )
                except Exception as e:
                    print(f"❌ Pipeline error for {filepath}: {e}")
# TODO
