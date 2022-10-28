class Node: 
    def __init__(self, key="", value=""):
        self.key = key
        self.value = value
        self.before = None
        self.next = None
        
    def removeNode(self):
        self.before.next = self.next
        self.next.before = self.before
        self.before = None
        self.next = None

    def addNodeAfter(self, node):
        # a - b
        # a - c - b
        node.next = self.next
        self.next.before = node
        node.before = self
        self.next = node
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currCap = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.before = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.bringToHead(node)
        return node.value     

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.bringToHead(node)
            return
        
        node = Node(key, value)
        self.head.addNodeAfter(node)
        self.currCap += 1
        self.cache[key] = node
        
        if self.currCap > self.capacity:
            toRemove = self.tail.before
            del self.cache[toRemove.key]
            toRemove.removeNode()
            
    def bringToHead(self, node):
        node.removeNode()
        self.head.addNodeAfter(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)