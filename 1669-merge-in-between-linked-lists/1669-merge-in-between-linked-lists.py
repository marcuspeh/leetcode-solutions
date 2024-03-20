# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = ListNode(next=list1)
        
        curr = head
        for i in range(a):
            curr = curr.next
        
        temp = curr.next
        for i in range(b - a):
            temp = temp.next
        
        curr.next = list2  
        while curr.next:
            curr = curr.next

        curr.next = temp.next
        return head.next