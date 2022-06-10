import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.cache = {}

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        
        self.cache[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False
        
        index = self.cache[val]
        last = self.list[-1]
        
        self.list[index], self.list[-1] = last, val
        self.cache[last] = self.cache[val]
        self.list.pop()
        del self.cache[val]
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()