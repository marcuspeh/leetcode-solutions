# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        currL1 = l1
        currL2 = l2
        carry = 0
        
        # start adding to new list
        while currL1 or currL2 or carry:
            newVal = 0
            
            if currL1:
                newVal += currL1.val
                currL1 = currL1.next
                
            if currL2:
                newVal += currL2.val
                currL2 = currL2.next
                
            if carry:
                newVal += carry
                carry = 0
                
            
            if newVal > 9:
                newVal = newVal - 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = newNode
        
        return head.next
        
         
            