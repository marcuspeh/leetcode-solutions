# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        lengthB = 0
        
        # Find length of A
        curr = headA
        while curr:
            curr = curr.next
            lengthA += 1
            
        # Find length of B
        curr = headB
        while curr:
            curr = curr.next
            lengthB += 1
            
        currA = headA
        currB = headB
        
        if lengthA < lengthB:
            for _ in range(lengthB - lengthA):
                currB = currB.next
        elif lengthB < lengthA:
            for _ in range(lengthA - lengthB):
                currA = currA.next
        
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next