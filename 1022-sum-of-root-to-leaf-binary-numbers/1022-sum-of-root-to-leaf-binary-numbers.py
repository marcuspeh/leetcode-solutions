# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        num = 0
        stack = [(0, root)]
        while stack:
            prev, node = stack.pop()
            curr = (prev << 1) + node.val
            if not node.left and not node.right:
                num += curr
                continue
            
            if node.left:
                stack.append((curr, node.left))
            if node.right:
                stack.append((curr, node.right))
            
        return num