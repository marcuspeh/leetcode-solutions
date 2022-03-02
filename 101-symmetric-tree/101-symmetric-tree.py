# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.checkTree(root.left, root.right)
        
    def checkTree(self, left, right):
        if  not left and not right:
            return True
        
        if not left or not right or left.val != right.val:
            return False
        
        return self.checkTree(left.right, right.left) and \
                self.checkTree(left.left, right.right)