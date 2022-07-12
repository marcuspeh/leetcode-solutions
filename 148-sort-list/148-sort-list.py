# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        lst.sort()
        
        result = ListNode()
        curr = result
        
        for l in lst:
            curr.next = ListNode(l)
            curr = curr.next
        return result.next
        
        
        