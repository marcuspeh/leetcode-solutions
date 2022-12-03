# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        newLeft = self.invertTree(root.left)
        newRight = self.invertTree(root.right)
        root.left = newRight
        root.right = newLeft
        
        return root