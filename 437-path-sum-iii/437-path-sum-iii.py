# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        
        def helper(root, table):
            nonlocal result
            if not root:
                return 
            
            newTable = []
            for entry in table:
                entry += root.val
                
                if entry == targetSum:
                    result += 1
                newTable.append(entry)
                    
            if root.val == targetSum:
                result += 1
            newTable.append(root.val)
            
            helper(root.left, newTable)
            helper(root.right, newTable)
        
        helper(root, [])
        return result