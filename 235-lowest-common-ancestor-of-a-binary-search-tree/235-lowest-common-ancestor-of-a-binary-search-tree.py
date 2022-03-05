# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            smaller = q
            bigger = p
        else:
            smaller = p
            bigger = q
        
        curr = root
        
        while curr:
            if bigger.val < curr.val:
                curr = curr.left
            elif smaller.val > curr.val:
                curr = curr.right
            else:
                return curr
        
        return root
                