# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        curr = newHead
        
        carry = 0
        
        while l1 or l2 or carry:
            # Just carry left
            if not l1 and not l2:
                val = carry
            # If just l2 left
            elif not l1:
                val = l2.val + carry
                l2 = l2.next
            # If just l1 left
            elif not l2:
                val = l1.val + carry
                l1 = l1.next
            # If both left
            else:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
        
        return newHead.next