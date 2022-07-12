# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
            if fast.next:
                fast = fast.next
                
        temp = slow.next
        slow.next = None
        
        lst1 = self.sortList(head)
        lst2 = self.sortList(temp)
        
        return self.merge(lst1, lst2)
        
    def merge(self, head1, head2):
        result = ListNode()
        curr = result
        
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = ListNode(head1.val)
                head1 = head1.next
            else:
                curr.next = ListNode(head2.val)
                head2 = head2.next
            curr = curr.next
        
        while head1:
            curr.next = ListNode(head1.val)
            head1 = head1.next
            curr = curr.next
            
        while head2:
            curr.next = ListNode(head2.val)
            head2 = head2.next
            curr = curr.next
            
        curr.next = None
        return result.next
        