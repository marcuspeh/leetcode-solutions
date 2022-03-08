# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        
        curr = head
        while curr:
            result.append(curr)
            curr = curr.next
        
        if n == len(result):
            return head.next
        elif n == 1:
            result[-n - 1].next = None
        else:
            result[-n - 1].next = result[-n + 1]
    
        return head