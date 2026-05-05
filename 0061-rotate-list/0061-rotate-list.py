# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        curr = ListNode(next=head)
        count = 0
        while curr.next:
            curr = curr.next
            count += 1

        k %= count
        curr = ListNode(next=head)
        for i in range(count - k):
            curr = curr.next
        
        if curr.next:
            newHead = curr.next
            curr.next = None
            curr = newHead
            while curr.next:
                curr = curr.next
            curr.next = head
        
            return newHead
        
        return head
