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
            return head
        
        slow = head
        fast = head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
            if fast.next:
                fast = fast.next
                
        middle = slow.next
        slow.next = None
        reverseList = None
        
        while middle:
            nextItem = middle.next
            middle.next = reverseList
            reverseList = middle
            middle = nextItem
            
        curr = ListNode()
        while head and reverseList:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = reverseList
            reverseList = reverseList.next
            curr = curr.next
            
        if head:
            curr.next = head
        
        