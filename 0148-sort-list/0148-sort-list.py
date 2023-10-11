# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left, right = self.split(head)
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeList(left, right)
            
    
    def split(self, head):
        slow = head
        fast = head.next
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        temp = slow.next
        slow.next = None
        return head, temp
        
        
    def mergeList(self, head1, head2):
        result = ListNode()
        curr = result
        
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = ListNode(val=head1.val)
                head1 = head1.next
            else:
                curr.next = ListNode(val=head2.val)
                head2 = head2.next
            curr = curr.next
        
        while head1:
            curr.next = ListNode(val=head1.val)
            head1 = head1.next
            curr = curr.next
            
        while head2:
            curr.next = ListNode(val=head2.val)
            head2 = head2.next
            curr = curr.next
            
        curr.next = None
        return result.next
            