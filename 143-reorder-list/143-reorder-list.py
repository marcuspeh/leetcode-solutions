# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Since it is single direction, store all nodes to prevent continuous looping
        
        nodes = []
        
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        firstPointer = 0
        secondPointer = len(nodes) - 1
        
        while firstPointer < secondPointer:
            nodes[firstPointer].next = nodes[secondPointer]
            firstPointer += 1
            
            if firstPointer >= secondPointer:
                break
            
            nodes[secondPointer].next = nodes[firstPointer]
            secondPointer -= 1
            
        nodes[firstPointer].next = None