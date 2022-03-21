class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        if next:
            self.minValue = min(self.next.minValue, val)
        else:
            self.minValue = val

class MinStack:

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        self.stack = Node(val, self.stack)

    def pop(self) -> None:
        self.stack = self.stack.next
            
    def top(self) -> int:
        return self.stack.val
    def getMin(self) -> int:
        return self.stack.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()