from abc import ABC, abstractmethod
import time
import threading


class Strategy(ABC):
    def __init__(self, exchange, timeout=60):
        self.exchange = exchange
        self.timeout = timeout
        self.price = None
        self._stop = False
        self._thread = None

    def start(self):
        if not self._thread:
            self._stop = False
            self._thread = threading.Thread(target=self._run)
            self._thread.start()

    def stop(self):
        self._stop = True
        if self._thread:
            self._thread.join()
            self._thread = None

    def _run(self):
        while not self._stop:
            self.run()
            time.sleep(self.timeout)

    @abstractmethod
    def run(self):
        pass
