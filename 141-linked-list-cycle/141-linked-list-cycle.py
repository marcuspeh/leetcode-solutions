# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        
        # At every step, turtle will move
        while rabbit:
            turtle = turtle.next
            
            rabbit = rabbit.next
            
            if rabbit == None:
                return False
            
            rabbit = rabbit.next
            
            if turtle == rabbit:
                return True
            
        return False