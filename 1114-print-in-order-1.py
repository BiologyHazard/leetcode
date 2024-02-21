import threading
from collections.abc import Callable


class Foo:
    def __init__(self):
        self.second_lock = threading.Lock()
        self.third_lock = threading.Lock()
        self.second_lock.acquire()
        self.third_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.second_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.third_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.third_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
