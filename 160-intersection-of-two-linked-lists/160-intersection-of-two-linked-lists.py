# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        lengthB = 0
        currA = headA
        currB = headB
        
        # Find length of A
        while currA:
            lengthA += 1
            currA = currA.next
        
        # Find length of B
        while currB:
            lengthB += 1
            currB = currB.next
        
        # Align list
        currA = headA
        currB = headB
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                currA = currA.next
        elif lengthB > lengthA:
            for i in range(lengthB - lengthA):
                currB = currB.next
        
        # Go through all the array and find same node
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        
        return None