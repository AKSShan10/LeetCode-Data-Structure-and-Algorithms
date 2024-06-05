class MyQueue:

    def __init__(self):
        self.si = []
        self.so = []

    def push(self, x: int) -> None:
        self.si.append(x)

    def pop(self) -> int:
        if not self.so:
            while self.si:
                self.so.append(self.si.pop())

        return self.so.pop()

    def peek(self) -> int:
        if not self.so:
            while self.si:
                self.so.append(self.si.pop())

        return self.so[-1]

    def empty(self) -> bool:
        if not self.si and not self.so:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()