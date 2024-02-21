import time
from collections.abc import Callable


class Foo:
    def __init__(self):
        self.printed_first = False
        self.printed_second = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.printed_first = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.printed_first:
            time.sleep(0.001)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.printed_second = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.printed_second:
            time.sleep(0.001)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
