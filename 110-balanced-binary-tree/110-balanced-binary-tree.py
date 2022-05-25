# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0, True
            
            leftHeight, leftChecker = helper(root.left)
            if not leftChecker:
                return 0, False
            
            rightHeight, rightChecker = helper(root.right)
            if not rightChecker:
                return 0, False
            
            return max(leftHeight, rightHeight) + 1, abs(leftHeight - rightHeight) <= 1
        return helper(root)[1]