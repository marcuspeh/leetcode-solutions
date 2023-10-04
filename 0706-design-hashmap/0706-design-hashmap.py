
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:
    # Settle collision with link list
        
    def __init__(self):
        self.size = 997
        self.table = [None for i in range(self.size)]

    def put(self, key: int, val: int) -> None:
        keyHash = key % self.size        
        
        curr = self.table[keyHash]
        
        # Find key if present
        if not curr:
            self.table[keyHash] = Node(key, val)
        else:
            while curr.next:
                if curr.key == key:
                    curr.val = val
                    return
                curr = curr.next
            
            if curr.key == key:
                curr.val = val
            else:
                curr.next = Node(key, val)

    def get(self, key: int) -> int:
        keyHash = key % self.size
        
        curr = self.table[keyHash]
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1
        
    def remove(self, key: int) -> None:
        keyHash = key % self.size
        
        prev = None
        curr = self.table[keyHash]
        
        # Assign previous node to next node
        while curr:
            if curr.key == key:
                result = curr.val
                
                if not prev:
                    self.table[keyHash] = curr.next
                else:
                    prev.next = curr.next
                return result
                
            prev = curr
            curr = curr.next
            
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)