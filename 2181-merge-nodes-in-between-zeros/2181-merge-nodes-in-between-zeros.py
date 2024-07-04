# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = ListNode()
        currResult = resultHead
            
        total = 0
        curr = head.next
        
        while curr:
            if curr.val == 0:
                currResult.next = ListNode(val=total)
                total = 0
                currResult = currResult.next
            else:
                total += curr.val
            curr = curr.next
        
        return resultHead.next