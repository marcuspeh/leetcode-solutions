# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(next=head)
        curr = fakeHead
        removeSet = set(nums)

        while curr.next:
            if curr.next.val in removeSet:
                curr.next = curr.next.next
                continue
            curr = curr.next
        
        return fakeHead.next