# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            if not lst:
                continue
            heappush(heap, (lst.val, hash(lst), lst))
        
        result = ListNode()
        head = result
        
        while heap:
            _, _, lst = heappop(heap)
            result.next = lst
            result = result.next
            
            if lst.next:
                heappush(heap, (lst.next.val, hash(lst.next), lst.next))
                
        result.next = None
        return head.next