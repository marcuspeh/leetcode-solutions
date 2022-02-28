# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        newHead = ListNode(-101)
        curr = newHead
        listCurr = head
        
        # Add to list
        while listCurr:
            if curr.val != listCurr.val:
                curr.next = ListNode(listCurr.val)
                curr = curr.next
                
            listCurr = listCurr.next
        
        return newHead.next