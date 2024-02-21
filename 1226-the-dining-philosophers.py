import threading
from collections.abc import Callable


class DiningPhilosophers:
    def __init__(self):
        self.fork_locks = [threading.Lock() for _ in range(5)]
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5
        with self.lock, self.fork_locks[left_fork], self.fork_locks[right_fork]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
