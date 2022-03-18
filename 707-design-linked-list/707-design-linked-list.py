
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0        

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        
        if not self.head:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
            
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        
        self.length += 1
        if not self.head:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
            
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:        
        if self.length < index or index < 0:
            return 
        
        self.length += 1
        
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            
        newNode = Node(val)
        newNode.next = curr.next
        curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if self.length <= index or index < 0:
            return
        
        self.length -= 1
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            
        curr.next = curr.next.next 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)