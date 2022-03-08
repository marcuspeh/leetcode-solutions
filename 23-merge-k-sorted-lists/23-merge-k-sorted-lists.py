# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __lt__(self, other):
#         return self.val - other.val
    

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        counter = 1
        
        pq = []
        
        # O(k * log(k))
        for lst in lists:
            if lst:
                heapq.heappush(pq, (lst.val, counter, lst))
                counter += 1
                
        # O(n * log(k))
        while pq:
            count, top = heapq.heappop(pq)[1:]
            curr.next = ListNode(top.val)
            curr = curr.next
            if top.next:
                heapq.heappush(pq, (top.next.val, count, top.next))
                
        return head.next