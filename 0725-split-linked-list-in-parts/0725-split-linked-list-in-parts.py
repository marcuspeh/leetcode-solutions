# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = self.getLength(head)
        size = length // k
        extra = length % k
        
        result = []
        while head:
            currSize = size
            if len(result) < extra:
                currSize += 1
            
            currHead = ListNode()
            curr = currHead
            for _ in range(currSize):
                curr.next = head
                head = head.next
                curr = curr.next
                curr.next = None
            
            result.append(currHead.next)
        
        for _ in range(len(result) , k):
            result.append(None)
        return result
                
            
            
    
    def getLength(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count