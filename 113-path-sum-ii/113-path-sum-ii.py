# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Go through everything
        # Use recusive dfs
        result = []
        
        if not root:
            return result
        
        def dfs(root, lst, total):
            nonlocal result
            if not root.left and not root.right:
                if total + root.val == targetSum:
                    result.append(lst + [root.val])
                return
            if root.left:
                dfs(root.left, lst + [root.val], total + root.val)
            
            if root.right:
                dfs(root.right, lst + [root.val], total + root.val)
            
        dfs(root, [], 0)
        
        return result
                