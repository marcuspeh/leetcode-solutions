# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        mockHead = ListNode(next=head)
        curr = mockHead
        for _ in range(count // 2):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return mockHead.next