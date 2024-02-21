import threading
from collections.abc import Callable


class H2O:
    def __init__(self):
        self.h_semaphore = threading.BoundedSemaphore(2)
        self.o_semaphore = threading.BoundedSemaphore(1)
        self.lock = threading.Lock()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_semaphore.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_semaphore.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.release()

    def release(self):
        if self.h_semaphore._value == 0 and self.o_semaphore._value == 0:
            self.h_semaphore.release(2)
            self.o_semaphore.release(1)
