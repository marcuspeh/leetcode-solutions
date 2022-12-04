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
            
            leftPath = max(helper(root.left), 0)
            rightPath = max(helper(root.right), 0)
            
            result = max(result, leftPath + rightPath + root.val)
            
            return max(leftPath, rightPath) + root.val
        
        helper(root)
        return result