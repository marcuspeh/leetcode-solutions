# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = ListNode()
        newHead.next = head
        
        prev = newHead
        curr = head
        
        while curr:
            duplicated = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                duplicated = True
                
            if duplicated:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
                
        return newHead.next
                