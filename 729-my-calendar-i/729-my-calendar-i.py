class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        if not self.head:
            self.head = Node(start, end)
            return True
        
        node = self.head
        
        while node:
            if start >= node.end:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(start, end)
                    return True
            elif end <= node.start:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(start, end)
                    return True
            else:
                return False
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)