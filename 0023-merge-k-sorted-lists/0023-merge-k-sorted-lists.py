# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        heap = []
        
        for lst in lists:
            if not lst:
                continue
            heapq.heappush(heap, (lst.val, hash(lst), lst))
            
        while heap:
            _, _, lst = heapq.heappop(heap)
            result.next = lst
            result = lst
            
            if lst.next:
                heapq.heappush(heap, (lst.next.val, hash(lst), lst.next))
        
        result.next = None
        return head.next
                