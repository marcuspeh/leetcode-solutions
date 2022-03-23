# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth rank
        # Since no weight is stored for the root, can retrieve first kth nodes
        cache = []
        
        def helper(root):
            nonlocal cache
            
            if len(cache) == k:
                return
            
            if not root:
                return
            
            helper(root.left)
            cache.append(root.val)
            helper(root.right)
            
        helper(root)
        
        return cache[k - 1]