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
        
        # Add both till one of the list reach end
        while currL1 and currL2:
            newVal = currL1.val + currL2.val + carry
            if newVal > 9:
                newVal = newVal - 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = newNode
            
            currL1 = currL1.next
            currL2 = currL2.next
            
        # Add the rest of L1
        while currL1:
            newVal = currL1.val + carry
            if newVal > 9:
                newVal = newVal - 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = newNode
            currL1 = currL1.next
            
        # Add the rest of L2
        while currL2:
            newVal = currL2.val + carry
            if newVal > 9:
                newVal = newVal - 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(newVal)
            curr.next = newNode
            curr = newNode
            currL2 = currL2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return head.next
        
         
            