# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        # 1 -> 2 -> 3
        prev = None
        curr = head
        
        while curr.next:
            temp = curr.next
            
            curr.next = prev
            prev = curr
            curr = temp
            
        curr.next = prev
        return curr