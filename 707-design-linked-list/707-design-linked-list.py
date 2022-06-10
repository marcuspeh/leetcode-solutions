class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def print(self):
        if not self.next:
            print(self.val)
        else:
            print(self.val, end=" ")
            self.next.print()

class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        self.length += 1
        
        if self.tail == self.head:
            self.tail = self.head.next

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return 
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
            
        curr.next = Node(val, curr.next)
        self.length += 1
        
        if self.tail == curr:
            self.tail = curr.next

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return 
        
        if self.length == 0:
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        if curr.next == self.tail:
            curr.next = None
            self.tail = curr
        else:
            curr.next = curr.next.next
        
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)