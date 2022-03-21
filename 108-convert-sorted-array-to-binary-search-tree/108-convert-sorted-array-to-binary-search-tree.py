# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Height-balance = root is median
        def helper(start, end):
            if end < start:
                return None
        
            mid = (end - start) // 2 + start
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        
        return helper(0, len(nums) - 1)
            