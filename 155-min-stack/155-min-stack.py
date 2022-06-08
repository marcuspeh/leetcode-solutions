class Node:
    def __init__(self, val, mini):
        self.val = val
        self.mini = mini

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prevMini = self.stack[-1].mini if self.stack else val
        
        self.stack.append(Node(val, min(val, prevMini)))

    def pop(self) -> None:
        return self.stack.pop().val

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()