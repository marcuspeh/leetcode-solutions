# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newHead.next = head
        
        prev = newHead
        curr = head
        
        while curr:
            hasDuplicate = False
            
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                hasDuplicate = True
                
            if hasDuplicate:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return newHead.next