# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head = ListNode(val=0, next=head)
        curr = head
        for i in range(left - 1):
            curr = curr.next
            
        beforeStart = curr
        start = curr.next
        if right > left:
            prev = None
            curr = curr.next
            for i in range(right - left + 1):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            start.next = curr
            beforeStart.next = prev
        return head.next