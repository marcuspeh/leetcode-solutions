# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        # 1 -> 2 -> 3 -> 4
        curr = None
        currNext = head
        
        while currNext:
            temp = currNext.next
            currNext.next = curr
            curr = currNext
            currNext = temp
            
        return curr
        