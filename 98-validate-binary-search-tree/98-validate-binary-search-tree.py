# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        prev = -1 << 32
        
        while stack:
            node = stack.pop()
            
            while node.left:
                temp = node.left
                node.left = None
                
                stack.append(node)
                node = temp
            
            if prev >= node.val:
                return False
            
            prev = node.val
            if node.right:
                stack.append(node.right)
            
        return True 