# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # values in left subtree < curr < values in right subtree
        
        frontier = []
        curr = root
        prev = -1 << 32
        
        # Go to the minimum node and start checking
        while curr or frontier:
            while curr:
                frontier.append(curr)
                curr = curr.left
            
            curr = frontier.pop()
            
            if curr.val <= prev:
                return False
            
            prev = curr.val
            
            if curr.right:
                curr = curr.right
            else:
                curr = None
                
        return True