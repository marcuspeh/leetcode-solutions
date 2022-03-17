# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(next=head)
        prev = newHead
        curr = head
        
        while curr:
            isRepeated = False
            
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                isRepeated = True
                
            if isRepeated:
                curr = curr.next
                prev.next = curr
                
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
                
        return newHead.next