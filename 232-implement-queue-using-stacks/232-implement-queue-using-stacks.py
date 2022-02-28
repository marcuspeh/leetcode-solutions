class MyQueue:

    def __init__(self):
        self.stack = []
        self.stackReversed = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stackReversed:
            return self.stackReversed.pop()
        
        while self.stack:
            removed = self.stack.pop()
            self.stackReversed.append(removed)
        
        return self.stackReversed.pop()

    def peek(self) -> int:
        if self.stackReversed:
            return self.stackReversed[-1]
        
        while self.stack:
            removed = self.stack.pop()
            self.stackReversed.append(removed)
        
        return self.stackReversed[-1]        

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.stackReversed) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()