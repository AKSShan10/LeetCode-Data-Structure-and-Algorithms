class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum.append(min(self.minimum[-1], val))
        #print(self.minimum)
        #print(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


'''''
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.pop())
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print('Minimum',param_4)
'''