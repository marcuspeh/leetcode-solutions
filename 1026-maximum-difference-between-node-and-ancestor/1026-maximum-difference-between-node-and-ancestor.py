# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node):      
            nonlocal result
            
            minimum = node.val
            maximum = node.val
            
            if node.left:
                leftMin, leftMax = dfs(node.left)
                minimum = min(minimum, leftMin)
                maximum = max(maximum, leftMax)
                result = max(result, abs(node.val - leftMin), abs(node.val - leftMax))
                
            if node.right:
                rightMin, rightMax = dfs(node.right)
                minimum = min(minimum, rightMin)
                maximum = max(maximum, rightMax)
                result = max(result, abs(node.val - rightMin), abs(node.val - rightMax))

            return minimum, maximum
        dfs(root)
        return result