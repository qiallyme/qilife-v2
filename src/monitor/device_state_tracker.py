# TODO
import threading
import time
import psutil

class DeviceStateTracker:
    """
    Periodically logs basic device stats (CPU, memory).
    """

    def __init__(self, interval: int = 60):
        self.interval = interval
        self._running = False
        self._thread = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._track_loop, daemon=True)
        self._thread.start()
        print(f"⚙️ Started device tracker: every {self.interval}s")

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
        print("🛑 Stopped device tracker")

    def _track_loop(self):
        while self._running:
            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory().percent
            print(f"💻 CPU: {cpu}%, RAM: {mem}%")
            time.sleep(self.interval)
