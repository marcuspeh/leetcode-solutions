# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast:
            fast = fast.next
            if fast == slow:
                return True
            
            slow = slow.next
            if fast: 
                fast = fast.next
        return False