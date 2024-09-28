class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.start = 0
        self.end = 0    
        self.k = k
        self.count = 0
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.start = self.start - 1
        if self.start < 0:
            self.start = self.k - 1
        self.queue[self.start] = value
        self.count += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.end] = value
        self.end += 1
        if self.end == len(self.queue):
            self.end = 0
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.start += 1
        if self.start == len(self.queue):
            self.start = 0
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
    
        self.end -= 1
        if self.end < 0:
            self.end = self.k - 1
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        end = self.end - 1
        if end < 0:
            end = -1
        return self.queue[end]
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()