# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = -1
        maxDistance = -1
        
        firstCritIdx = float("inf")
        prevCritIdx = -1
        prev = -1
        curr = head
        i = 0
        
        while curr:
            if self.isCrit(curr, prev):
                if prevCritIdx != -1:
                    dist = i - prevCritIdx
                    minDistance = dist if minDistance == -1 else min(dist, minDistance)
                    maxDistance = i - firstCritIdx
                    
                firstCritIdx = min(i, firstCritIdx)
                prevCritIdx = i
                
            i += 1
            prev = curr.val
            curr = curr.next
        
        return [minDistance, maxDistance]
    def isCrit(self, curr, prev):
        if prev == -1 or not curr.next:
            return False
        
        return prev < curr.val > curr.next.val or prev > curr.val < curr.next.val
    