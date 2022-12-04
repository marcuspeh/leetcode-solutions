# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        
        start = head
        afterN = head
        for _ in range(n):
            afterN = afterN.next
            
        while afterN.next:
            start = start.next
            afterN = afterN.next
        
        start.next = start.next.next
        
        return head.next