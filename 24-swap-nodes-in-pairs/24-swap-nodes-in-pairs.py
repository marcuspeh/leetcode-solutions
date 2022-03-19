# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(next=head)
        prev = newHead
        curr = head
        
        while curr and curr.next:
            temp = curr.next.next
            # a - b - c
            # b - a - c
            b = curr.next
            curr.next = b.next
            b.next = curr
            prev.next = b
            
            prev = curr
            curr = curr.next
            
        return newHead.next