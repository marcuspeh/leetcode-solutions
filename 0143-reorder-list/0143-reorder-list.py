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
        first, second = self.splitList(head)
        return self.combineList(first, second)
        
    
    def splitList(self, head):
        slow = head
        fast = head.next
        if fast:
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
        first = head
        second = slow.next
        slow.next = None
        return first, self.reverseList(second)
        
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def combineList(self, head1, head2):
        newHead = ListNode()
        curr = newHead
        
        while head1 or head2:
            if head1:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
                
            if head2:
                curr.next = head2
                head2 = head2.next
                curr = curr.next
                
        return newHead.next