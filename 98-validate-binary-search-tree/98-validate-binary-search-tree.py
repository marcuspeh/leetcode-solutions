# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        frontier = []
        prev = -1 << 32
        
        while frontier or root:
            while root:
                frontier.append(root)
                root = root.left
               
            root = frontier.pop()
        
            if root.val <= prev:
                return False
                
            prev = root.val
            root = root.right
        
        return True