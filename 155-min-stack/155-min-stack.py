class Node:
    def __init__(self, val, nextNode):
        self.nextNode = nextNode
        self.val = val
        if nextNode:
            self.minValue = min(nextNode.minValue, val)
        else:
            self.minValue = val

class MinStack:

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        self.stack = Node(val, self.stack)

    def pop(self) -> None:
        curr = self.stack
        self.stack = self.stack.nextNode

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