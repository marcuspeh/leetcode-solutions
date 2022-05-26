# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(head, root):
            if not head:
                return True
            
            if not root:
                return False
            
            if head.val != root.val:
                return False
            
            nextHead = head.next
            
            return helper(nextHead, root.left) or helper(nextHead, root.right)
        frontier = [root]
        
        while frontier:
            node = frontier.pop()
            
            if node.val == head.val:
                if helper(head, node):
                    return True
            
            if node.left:
                frontier.append(node.left)
            
            if node.right:
                frontier.append(node.right)
                
        return False
        