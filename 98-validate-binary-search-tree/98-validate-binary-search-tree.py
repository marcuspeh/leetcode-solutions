# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In order checker
        result = []
        
        def helper(root):
            nonlocal result
            
            if not root:
                return
            
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        
        helper(root)
        
        for i in range(len(result) - 1):
            if result[i] >= result [i + 1]:
                return False
            
        return True