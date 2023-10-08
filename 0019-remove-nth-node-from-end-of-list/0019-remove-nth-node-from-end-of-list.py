# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummyHead = ListNode(next=head)
        
        length = 0
        curr = dummyHead
        while curr:
            curr = curr.next
            length += 1
        
        curr = dummyHead
        for _ in range(length - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummyHead.next