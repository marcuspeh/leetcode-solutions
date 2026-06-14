# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        twinSum = [float("-inf") for _ in range(length // 2)]
        curr = head
        for idx in range(len(twinSum)):
            twinSum[idx] = curr.val
            curr = curr.next
        
        for idx in range(len(twinSum)):
            twinSum[-1 - idx] += curr.val
            curr = curr.next
        
        return max(twinSum)