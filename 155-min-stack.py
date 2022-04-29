class MinStack:

    def __init__(self):
        self.m = []

    def push(self, val: int) -> None:
        if self.m:
            self.m.append((val, min(val, self.m[-1][1])))
        else:
            self.m.append((val, val))

    def pop(self) -> None:
        self.m.pop()

    def top(self) -> int:
        return self.m[-1][0]

    def getMin(self) -> int:
        return self.m[-1][1]
