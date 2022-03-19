# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second
        # a - b - c
        # c - b - a
        prev = slow
        second = slow.next
        while second.next:
            temp = second.next
            second.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        # Combine
        first = head
        second = slow.next
        while first != slow:
            slow.next = second.next
            second.next = first.next
            first.next = second
            first = second.next
            second = slow.next