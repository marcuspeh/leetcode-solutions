# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def helper(root, maxVal):
            nonlocal result
            
            if not root:
                return
            
            if root.val >= maxVal:
                result += 1
                
            newMaxValue = max(maxVal, root.val)
            helper(root.left, newMaxValue)
            helper(root.right, newMaxValue)
            
        helper(root, -1 << 32)
        return result