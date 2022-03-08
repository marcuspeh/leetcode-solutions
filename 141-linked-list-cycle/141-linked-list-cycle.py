# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        rabbit = head.next
        turtle = head
        
        while rabbit:
            if rabbit == turtle:
                return True
            
            turtle = turtle.next
            rabbit = rabbit.next
            
            if not rabbit:
                break
            
            rabbit = rabbit.next
            
        return False
            