# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0
        stack = [(0, root)]
        
        while stack:
            curr, node = stack.pop()
            newCurr = curr * 10 + node.val
            if not node.left and not node.right:
                result += newCurr
                continue

            if node.left:
                stack.append((newCurr, node.left))
            if node.right:
                stack.append((newCurr, node.right))
        
        return result