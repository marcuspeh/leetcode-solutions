# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Option 1 -> Find the length of both then iterate (less space but slower)
        # Option 2  -> iterate one and store. Iterate another to check (faster but more space)
        cache = set()
        
        curr = headA
        while curr:
            cache.add(curr)
            curr = curr.next
            
        curr = headB
        while curr:
            if curr in cache:
                return curr
            curr = curr.next