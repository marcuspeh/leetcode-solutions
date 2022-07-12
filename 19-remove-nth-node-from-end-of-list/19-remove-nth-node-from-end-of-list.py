# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        prev = head
        curr = head
        temp = head
        
        for i in range(n - 1):
            temp = temp.next
            
        if not temp.next:
            return head.next
            
        while temp.next:
            temp = temp.next
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
    
        return head
            
            