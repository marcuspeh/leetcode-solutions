# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        frontier = []
        
        # stack - push and get smallest node
        # Push all left nodes
        # pop and store then go right
        
        curr = root
        prev = -1 << 32
        
        while curr or frontier:
            while curr:
                frontier.append(curr)
                curr = curr.left
            
            curr = frontier.pop()
            
            if curr.val <= prev:
                return False
            
            prev = curr.val
            curr = curr.right
        
        return True
            