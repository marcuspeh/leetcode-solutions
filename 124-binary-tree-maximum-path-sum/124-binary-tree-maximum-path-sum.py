# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1 << 32
        
        def helper(root):
            nonlocal result
            
            if not root:
                return 0
            
            # left chain
            left = max(helper(root.left), 0)
            
            # Right chain
            right = max(helper(root.right), 0)
            
            result = max(root.val + left + right, result)
            
            return max(root.val + left, root.val + right)
        
        helper(root)
        
        return result