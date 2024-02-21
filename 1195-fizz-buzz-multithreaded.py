import threading
from collections.abc import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_lock = threading.Lock()
        self.buzz_lock = threading.Lock()
        self.fizzbuzz_lock = threading.Lock()
        self.number_lock = threading.Lock()
        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()
        self.number_lock.acquire()
        self.release(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for num in range(1, self.n+1):
            if num % 3 == 0 and num % 5 != 0:
                self.fizz_lock.acquire()
                printFizz()
                self.release(num + 1)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for num in range(1, self.n+1):
            if num % 3 != 0 and num % 5 == 0:
                self.buzz_lock.acquire()
                printBuzz()
                self.release(num + 1)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for num in range(1, self.n+1):
            if num % 3 == 0 and num % 5 == 0:
                self.fizzbuzz_lock.acquire()
                printFizzBuzz()
                self.release(num + 1)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for num in range(1, self.n+1):
            if num % 3 != 0 and num % 5 != 0:
                self.number_lock.acquire()
                printNumber(num)
                self.release(num + 1)

    def release(self, num):
        if num % 3 == 0 and num % 5 == 0:
            self.fizzbuzz_lock.release()
        elif num % 3 == 0:
            self.fizz_lock.release()
        elif num % 5 == 0:
            self.buzz_lock.release()
        else:
            self.number_lock.release()
