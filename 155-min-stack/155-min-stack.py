class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = val
        if self.stack:
            minimum = min(minimum, self.stack[-1][0])
        
        self.stack.append((minimum, val))

    def pop(self) -> None:
        return self.stack.pop()[1]
        

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()