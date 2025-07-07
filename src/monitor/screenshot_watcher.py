# TODO
import threading
import time
from pathlib import Path
from PIL import ImageGrab

class ScreenshotWatcher:
    """
    Periodically captures a screenshot and saves it to a folder.
    """

    def __init__(self, save_folder: str, interval: int = 60):
        self.save_folder = Path(save_folder)
        self.interval = interval
        self._running = False
        self._thread = None

    def start(self):
        self.save_folder.mkdir(parents=True, exist_ok=True)
        self._running = True
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()
        print(f"📸 Started screenshot watcher: every {self.interval}s")

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
        print("🛑 Stopped screenshot watcher")

    def _capture_loop(self):
        while self._running:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image = ImageGrab.grab()
            filename = self.save_folder / f"screenshot_{timestamp}.png"
            image.save(str(filename))
            time.sleep(self.interval)
