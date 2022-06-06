# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        # Find length - store tail
        # Get kth node      
        curr = head
        tail = curr
        length = 0
        
        while curr:
            length += 1
            tail = curr
            curr = curr.next
        
        # new head = Kth node - next
        # Kth node - next = None
        # tail.next = old head
        if k % length == 0:
            return head
        kth = length - k % length
        
        
        curr = head
        for _ in range(kth - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        tail.next = head
        
        return newHead