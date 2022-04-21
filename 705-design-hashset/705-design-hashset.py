class MyHashSet:
    PRIME = 997
    
    def __init__(self):
        self.table = [[] for i in range(MyHashSet.PRIME)]

    def add(self, key: int) -> None:
        hashed = key % MyHashSet.PRIME
        
        # check if key already exists
        if key in self.table[hashed]:
            return
        
        self.table[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = key % MyHashSet.PRIME
        
        # Check if key exists
        if key in self.table[hashed]:
            self.table[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = key % MyHashSet.PRIME
        
        # check if key exists
        if key in self.table[hashed]:
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)