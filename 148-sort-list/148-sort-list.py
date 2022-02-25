# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
            
        lst.sort(key=lambda x: x.val)
        
        newHead = ListNode()
        curr = newHead
        
        for i in lst:
            curr.next = i
            curr = curr.next
        
        curr.next = None
        
        return newHead.next