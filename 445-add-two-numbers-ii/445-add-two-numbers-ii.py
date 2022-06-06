# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode(val=0)

        list1 = self.reverseList(l1)
        list2 = self.reverseList(l2)
        
        newHead = None
        carry = 0
        
        while list1 and list2:
            total = list1.val + list2.val + carry
            carry = total // 10
            total %= 10
            
            newHead = ListNode(val=total, next=newHead)
            list1 = list1.next
            list2 = list2.next
        
        while list1:
            total = list1.val + carry
            carry = total // 10
            total %= 10
            
            newHead = ListNode(val=total, next=newHead)
            list1 = list1.next
        
        while list2:
            total = list2.val + carry
            carry = total // 10
            total %= 10
            
            newHead = ListNode(val=total, next=newHead)
            list2 = list2.next
            
        if carry:
            newHead = ListNode(val=carry, next=newHead)
        
        return newHead
            
        
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        first.next = None
        
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
            
        return first